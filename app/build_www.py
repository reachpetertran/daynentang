#!/usr/bin/env python3
"""Sinh thư mục app/www (nội dung đóng gói trong app) từ thư mục public/ của website.

Chạy: python3 app/build_www.py
- Chép toàn bộ trang tĩnh, bỏ phần cần mạng (Chia sẻ).
- Thay header website bằng khung app: thanh trên có "Cần giúp ngay", thanh tab dưới (Việt / Anh).
- Đổi mọi link thư mục thành .../index.html để chạy được trong WebView khi mất mạng.
- Thêm trang riêng của app: Truyện (19 truyện từ app/stories/), Khóa học, Của tôi.
- Sinh app/index.js: danh mục khóa – bài – truyện để theo dõi lộ trình và tìm kiếm.
Không thu dữ liệu, không gọi mạng.
"""
import html, json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "public"
STORIES_DIR = ROOT / "stories"
OUT = ROOT / "www"
SITE = "https://daynentang.com"
APP_NAME = "Dạy Nền Tảng"

SKIP_DIRS = {"chia-se"}
SKIP_FILES = {"_headers", "robots.txt", "sitemap.xml", "404.html"}

ICONS = {
    "home": '<path d="M3 11.5 12 4l9 7.5M5.5 10v9.5h13V10"/>',
    "book": '<path d="M4 5.5c2.5-1 5.5-1 8 .5 2.5-1.5 5.5-1.5 8-.5v13c-2.5-1-5.5-1-8 .5-2.5-1.5-5.5-1.5-8-.5zM12 6v13"/>',
    "course": '<path d="M4 6h16M4 12h16M4 18h10"/><circle cx="19" cy="18" r="1.4"/>',
    "mine": '<circle cx="12" cy="8.5" r="3.6"/><path d="M4.5 20c1-4 4-5.5 7.5-5.5s6.5 1.5 7.5 5.5"/>',
    "family": '<circle cx="8" cy="8" r="3"/><circle cx="17" cy="10" r="2.3"/><path d="M2.5 20c.6-4 2.8-6 5.5-6s4.900 2 5.500 6M14 20c.3-2.600 1.500-4.200 3.200-4.200s2.900 1.600 3.300 4.200"/>',
}
TABS = {
    "vi": [("home", "Trang chủ", "/index.html"), ("book", "Truyện", "/truyen/index.html"),
           ("course", "Khóa học", "/khoa-hoc/index.html"), ("mine", "Của tôi", "/cua-toi/index.html")],
    "en": [("home", "Home", "/en/index.html"), ("family", "Family", "/en/family/index.html"),
           ("course", "Personal", "/en/personal/index.html"), ("mine", "My learning", "/en/mine/index.html")],
}
T = {
    "vi": dict(help="Cần giúp ngay", helpurl="/can-giup-ngay/index.html", home="/index.html", aa="Cỡ chữ, màu nền, ngôn ngữ",
               size="Cỡ chữ", sizes=["Nhỏ", "Vừa", "Lớn", "Rất lớn"], theme="Màu nền", themes=["Theo máy", "Sáng", "Tối"],
               lang="Ngôn ngữ", nav="Điều hướng chính",
               note="Bản tiếng Anh hiện có các trang chính và vài bài đầu. Các bài khác vẫn là tiếng Việt."),
    "en": dict(help="Get help", helpurl="/en/get-help/index.html", home="/en/index.html", aa="Text size, theme, language",
               size="Text size", sizes=["Small", "Medium", "Large", "Extra large"], theme="Theme", themes=["System", "Light", "Dark"],
               lang="Language", nav="Main navigation",
               note="English covers the main pages and the first lessons so far. Other lessons open in Vietnamese."),
}

# Chạy trước khi vẽ trang: áp cỡ chữ và màu nền đã chọn, tránh nháy màn hình
PRE = ("<script>try{var s=JSON.parse(localStorage.getItem('dnt.v1'))||{},d=document.documentElement;"
       "d.setAttribute('data-size',s.size||'m');if(s.theme==='light'||s.theme==='dark')d.setAttribute('data-theme',s.theme)}catch(e){}</script>")


def tab_of(rel: str) -> str:
    if rel.startswith("en/"):
        for key, pre in (("family", "en/family/"), ("course", "en/personal/"), ("mine", "en/mine/"), ("family", "en/courses/family")):
            if rel.startswith(pre):
                return key
        return "home" if rel == "en/index.html" else ""
    if rel.startswith("truyen/"):
        return "book"
    if rel.startswith(("khoa-hoc/", "gia-dinh/", "ca-nhan/", "cong-cu/")):
        return "course"
    if rel.startswith("cua-toi/"):
        return "mine"
    return "home" if rel == "index.html" else ""


def buttons(vals, labels):
    return "".join(f'<button type="button" data-v="{v}">{l}</button>' for v, l in zip(vals, labels))


def chrome(rel: str, alt: str):
    lang = "en" if rel.startswith("en/") else "vi"
    t, cur = T[lang], tab_of(rel)
    vi_url = alt if lang == "en" and alt else "/index.html"
    en_url = alt if lang == "vi" and alt else "/en/index.html"
    on = ' aria-current="true"'
    top = (
        f'<header class="app-top no-print"><a class="app-brand" href="{t["home"]}">'
        f'<img src="/assets/logo/daynentang-icon.svg" alt="" width="32" height="32"><span>{APP_NAME}</span></a>'
        f'<button type="button" class="app-aa" id="app-aa" aria-label="{t["aa"]}" aria-expanded="false">Aa</button>'
        f'<a class="app-help" href="{t["helpurl"]}">{t["help"]}</a></header>'
        '<div class="app-panel no-print" id="app-panel" hidden>'
        f'<p><strong>{t["size"]}</strong></p><div class="app-row" id="app-size">{buttons("s m l xl".split(), t["sizes"])}</div>'
        f'<p><strong>{t["theme"]}</strong></p><div class="app-row" id="app-theme">{buttons("auto light dark".split(), t["themes"])}</div>'
        f'<p><strong>{t["lang"]}</strong></p><div class="app-row" id="app-lang">'
        f'<a href="{vi_url}" data-v="vi" lang="vi"{on if lang == "vi" else ""}>Tiếng Việt</a>'
        f'<a href="{en_url}" data-v="en" lang="en"{on if lang == "en" else ""}>English</a></div>'
        f'<p class="small muted">{t["note"]}</p></div>'
    )
    page_on = ' aria-current="page"'
    items = "".join(
        f'<a href="{href}"{page_on if key == cur else ""}>'
        f'<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" fill="none" stroke="currentColor" '
        f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg><span>{label}</span></a>'
        for key, label, href in TABS[lang]
    )
    return top, f'<nav class="app-tabs no-print" aria-label="{t["nav"]}">{items}</nav>'


HREF = re.compile(r'(href|action)="([^"]*)"')
ALT = re.compile(r'<link rel="alternate" hreflang="(vi|en)" href="https://daynentang\.com(/[^"]*)">')


def to_index(url: str) -> str:
    path, sep, tail = re.match(r"^([^?#]*)([?#]?)(.*)$", url).groups()
    if path.endswith("/"):
        path += "index.html"
    return f"{path}{sep}{tail}"


def fix_link(m):
    attr, url = m.group(1), m.group(2)
    if url.startswith("/chia-se/"):
        return f'{attr}="{SITE}{url}" target="_blank" rel="noopener"'
    if re.match(r"^(https?:|mailto:|tel:|sms:|#|data:|javascript:)", url) or not url:
        return m.group(0)
    return f'{attr}="{to_index(url)}"'


def transform(text: str, rel: str) -> str:
    lang = "en" if rel.startswith("en/") else "vi"
    alt = ""
    for hl, path in ALT.findall(text):
        if hl != lang and (SRC / path.strip("/") / "index.html").exists():
            alt = to_index(path)
    if rel == "cua-toi/index.html":
        alt = "/en/mine/index.html"
    if rel == "en/mine/index.html":
        alt = "/cua-toi/index.html"
    top, bottom = chrome(rel, alt)
    text = re.sub(r'<header class="site-head">.*?</header>', lambda m: top, text, flags=re.S)
    text = re.sub(r'<div class="lang-hint.*?</div></div>\s*', "", text, count=1, flags=re.S)
    text = re.sub(r'<script src="/assets/(lang|chia-se)\.js" defer></script>\s*', "", text)
    text = re.sub(r'<link rel="(canonical|alternate)"[^>]*>\s*', "", text)
    text = text.replace(
        '<link rel="stylesheet" href="/assets/style.css">',
        '<link rel="stylesheet" href="/assets/style.css">\n<link rel="stylesheet" href="/app/app.css">\n' + PRE,
    )
    text = text.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
    )
    text = text.replace("</body>", f'{bottom}\n<script src="/app/index.js"></script>\n<script src="/app/app.js"></script>\n</body>')
    text = HREF.sub(fix_link, text)
    if rel.endswith(("can-giup-ngay/index.html", "get-help/index.html")):
        # Trong app: bấm vào số là gọi được, kể cả khi mất mạng
        def tel(m):
            parts = [x.strip() for x in m.group(1).split("/")]
            links = " / ".join(f'<a class="app-tel" href="tel:{x.replace(" ", "")}">{x}</a>' for x in parts)
            return f"<td><strong>{links}</strong>"
        text = re.sub(r"<td><strong>([0-9 /]+)</strong>", tel, text)
    return text


def page(title: str, body: str, lang="vi") -> str:
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} – {APP_NAME}</title>
<meta name="theme-color" content="#1b2a41">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<header class="site-head"></header>
<main id="noi-dung"><div class="wrap">
{body}
</div></main>
</body>
</html>
"""


def h1_of(path: Path) -> str:
    m = re.search(r"<h1[^>]*>(.*?)</h1>", path.read_text(encoding="utf-8"), flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip() if m else path.parent.name


def course_index(base: Path, prefix: str, group_of):
    """Danh mục khóa và bài: thứ tự bài theo thứ tự link trên trang khóa."""
    out = []
    for cdir in sorted(p for p in base.iterdir() if p.is_dir() and (p / "index.html").exists()):
        cpath = f"{prefix}{cdir.name}/"
        text = (cdir / "index.html").read_text(encoding="utf-8")
        files = {"/" + f.parent.relative_to(SRC).as_posix() + "/": f for f in cdir.rglob("index.html") if f.parent != cdir}
        order = []
        for href in re.findall(r'href="([^"#?]+)"', text):
            if not href.startswith(("/", "http")):
                href = cpath + href
            if href in files and href not in order:
                order.append(href)
        order += [p for p in sorted(files) if p not in order]
        out.append(dict(p=cpath, t=h1_of(cdir / "index.html"), g=group_of(cdir.name), l=[[p, h1_of(files[p])] for p in order]))
    return out


def load_stories():
    f = STORIES_DIR / "stories.json"
    return json.loads(f.read_text(encoding="utf-8")) if f.exists() else []


def story_cards(items):
    out = []
    for s in items:
        out.append(
            f'<a class="card story-card" href="/truyen/{s["id"]}/"><img src="/truyen/tranh/{s["id"]}.webp" alt="" width="72" height="107" loading="lazy">'
            f'<span><span class="tag">Từ {s["age"]} tuổi · {html.escape(s["country"])} · Khóa {s["id"].upper()}</span>'
            f'<strong>{html.escape(s["title"])}</strong></span></a>'
        )
    return "\n".join(out)


MINE = {
    "vi": ("Của tôi", "Lộ trình của tôi", "Mọi thứ ở đây chỉ nằm trên máy của bạn. App không gửi dữ liệu đi đâu."),
    "en": ("My learning", "My learning", "Everything here stays on your phone. The app sends no data anywhere."),
}


def extra_pages(stories):
    green = [s for s in stories if s["part"] == "xanh"]
    orange = [s for s in stories if s["part"] == "cam"]
    truyen = f"""<p class="eyebrow">Truyện</p>
<h1>Truyện đọc cùng nhau</h1>
<p class="lead">Mười chín truyện từ khắp thế giới. Mỗi truyện có một đồ vật nhỏ và đi cùng một khóa học.</p>
<div id="app-story-progress"></div>
<h2 class="sec-green">Phần xanh · đọc cùng con</h2>
{story_cards(green)}
<h2 class="sec-orange">Phần cam · từ 15 tuổi</h2>
<div class="box warn"><p><strong>Trước khi đọc phần cam.</strong> Ba truyện này nói về tai nạn lao động, mua bán người và khó khăn tâm lý. Không đọc cho trẻ nhỏ. Nếu bạn đang cần giúp, hãy mở <a href="/can-giup-ngay/">Cần giúp ngay</a>.</p></div>
{story_cards(orange)}
<p class="small muted">Chữ và tranh có AI hỗ trợ. Tranh minh họa không phải chân dung người thật.</p>
"""
    khoa = """<p class="eyebrow">Khóa học</p>
<h1>Khóa học</h1>
<label class="app-search"><span class="small muted">Tìm bài, khóa hoặc truyện</span>
<input type="search" id="app-q" placeholder="Ví dụ: tiền, giấc ngủ, an toàn" autocomplete="off"></label>
<div id="app-results" class="app-list" aria-live="polite"></div>
<div id="app-courses-now"></div>
<h2>Tất cả khóa</h2>
<a class="card" href="/gia-dinh/"><span class="tag">9 khóa</span><h3>Gia đình</h3><p>Cho cha mẹ và người chăm sóc trẻ: giá trị, nuôi dạy con, tiền, việc nhà, nhà an toàn.</p></a>
<a class="card" href="/ca-nhan/"><span class="tag">10 khóa</span><h3>Cá nhân</h3><p>Cho người tự học: lớn lên an toàn, hiểu mình, tự học, vững nghề, chăm tâm trí.</p></a>
<a class="card" href="/cong-cu/"><span class="tag">Phiếu và bảng</span><h3>Hộp công cụ</h3><p>Phiếu, bảng và sổ dùng kèm các khóa.</p></a>
<a class="card" href="/bang-chung/"><h3>Bằng chứng và nguồn</h3><p>Mỗi nhận định trong bài đều ghi nguồn và mức chắc chắn.</p></a>
<a class="card" href="/gioi-thieu/"><h3>Giới thiệu, quyền riêng tư, giấy phép</h3><p>Dự án do một cá nhân làm. Miễn phí, không quảng cáo.</p></a>
"""
    pages = {
        "truyen/index.html": page("Truyện", truyen),
        "khoa-hoc/index.html": page("Khóa học", khoa),
    }
    for lang, rel in (("vi", "cua-toi/index.html"), ("en", "en/mine/index.html")):
        eb, h1, lead = MINE[lang]
        pages[rel] = page(h1, f'<p class="eyebrow">{eb}</p>\n<h1>{h1}</h1>\n<p class="lead">{lead}</p>\n<div id="app-mine"></div>\n', lang)
    for s in stories:
        frag = (STORIES_DIR / f'{s["id"]}.html').read_text(encoding="utf-8")
        pages[f'truyen/{s["id"]}/index.html'] = page(s["title"], frag)
    return pages


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    n = 0
    for f in sorted(SRC.rglob("*")):
        rel = f.relative_to(SRC)
        if f.is_dir() or rel.parts[0] in SKIP_DIRS or rel.name in SKIP_FILES:
            continue
        dst = OUT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        if f.suffix == ".html":
            dst.write_text(transform(f.read_text(encoding="utf-8"), rel.as_posix()), encoding="utf-8")
            n += 1
        else:
            shutil.copy2(f, dst)
    stories = load_stories()
    for rel, text in extra_pages(stories).items():
        dst = OUT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(transform(text, rel), encoding="utf-8")
        n += 1
    (OUT / "truyen" / "tranh").mkdir(parents=True, exist_ok=True)
    for img in STORIES_DIR.glob("*.webp"):
        shutil.copy2(img, OUT / "truyen" / "tranh" / img.name)

    fam = set(re.findall(r'href="/khoa-hoc/([^/"]+)/"', (SRC / "gia-dinh" / "index.html").read_text(encoding="utf-8")))
    courses = course_index(SRC / "khoa-hoc", "/khoa-hoc/", lambda slug: "G" if slug in fam else "C")
    if (SRC / "en" / "courses").exists():
        courses += course_index(SRC / "en" / "courses", "/en/courses/", lambda slug: "E")
    data = dict(courses=courses, stories=[[f'/truyen/{s["id"]}/', s["title"], s["part"], s["slug"]] for s in stories])
    (OUT / "app").mkdir(exist_ok=True)
    (OUT / "app" / "index.js").write_text("window.DNT=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";", encoding="utf-8")
    for name in ("app.css", "app.js"):
        shutil.copy2(ROOT / "shell" / name, OUT / "app" / name)
    size = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    lessons = sum(len(c["l"]) for c in courses)
    print(f"{n} trang, {len(courses)} khóa, {lessons} bài, {len(stories)} truyện, {size/1e6:.1f} MB -> {OUT}")


if __name__ == "__main__":
    main()
