#!/usr/bin/env python3
"""Sinh thư mục app/www (nội dung đóng gói trong app) từ thư mục public/ của website.

Chạy: python3 app/build_www.py
- Chép toàn bộ trang tĩnh, bỏ phần cần mạng (Chia sẻ).
- Thay header website bằng khung app: thanh trên có "Cần giúp ngay", thanh tab dưới.
- Đổi mọi link thư mục thành .../index.html để chạy được trong WebView khi mất mạng.
- Thêm các trang riêng của app: Truyện, Khóa học, Đã lưu.
Không thu dữ liệu, không gọi mạng.
"""
import re, shutil, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "public"
OUT = ROOT / "www"
SITE = "https://daynentang.com"

SKIP_DIRS = {"chia-se"}
SKIP_FILES = {"_headers", "robots.txt", "sitemap.xml", "404.html"}

ICONS = {
    "home": '<path d="M3 11.5 12 4l9 7.5M5.5 10v9.5h13V10"/>',
    "book": '<path d="M4 5.5c2.5-1 5.5-1 8 .5 2.5-1.5 5.5-1.5 8-.5v13c-2.5-1-5.5-1-8 .5-2.5-1.5-5.5-1.5-8-.5zM12 6v13"/>',
    "course": '<path d="M4 6h16M4 12h16M4 18h10"/><circle cx="19" cy="18" r="1.4"/>',
    "saved": '<path d="M6.5 4h11v16l-5.5-4-5.5 4z"/>',
}
TABS = [
    ("home", "Trang chủ", "/index.html"),
    ("book", "Truyện", "/truyen/index.html"),
    ("course", "Khóa học", "/khoa-hoc/index.html"),
    ("saved", "Đã lưu", "/da-luu/index.html"),
]


def tab_of(rel: str) -> str:
    if rel.startswith("truyen/"):
        return "book"
    if rel.startswith(("khoa-hoc/", "gia-dinh/", "ca-nhan/", "cong-cu/")):
        return "course"
    if rel.startswith("da-luu/"):
        return "saved"
    if rel == "index.html":
        return "home"
    return ""


def chrome(rel: str):
    cur = tab_of(rel)
    top = (
        '<header class="app-top no-print"><a class="app-brand" href="/index.html">'
        '<img src="/assets/logo/daynentang-icon.svg" alt="" width="32" height="32">Dạy Nền Tảng</a>'
        '<button type="button" class="app-aa" id="app-aa" aria-label="Cỡ chữ và màu nền">Aa</button>'
        '<a class="app-help" href="/can-giup-ngay/index.html">Cần giúp ngay</a></header>'
        '<div class="app-panel no-print" id="app-panel" hidden>'
        '<p><strong>Cỡ chữ</strong></p><div class="app-row" id="app-size">'
        '<button type="button" data-v="s">Nhỏ</button><button type="button" data-v="m">Vừa</button>'
        '<button type="button" data-v="l">Lớn</button><button type="button" data-v="xl">Rất lớn</button></div>'
        '<p><strong>Màu nền</strong></p><div class="app-row" id="app-theme">'
        '<button type="button" data-v="auto">Theo máy</button><button type="button" data-v="light">Sáng</button>'
        '<button type="button" data-v="dark">Tối</button></div></div>'
    )
    items = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if key == cur else ""}>'
        f'<svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" fill="none" stroke="currentColor" '
        f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[key]}</svg><span>{label}</span></a>'
        for key, label, href in TABS
    )
    bottom = f'<nav class="app-tabs no-print" aria-label="Điều hướng chính">{items}</nav>'
    return top, bottom


HREF = re.compile(r'(href|action)="([^"]*)"')


def fix_link(m):
    attr, url = m.group(1), m.group(2)
    if url.startswith("/chia-se/"):
        return f'{attr}="{SITE}{url}" target="_blank" rel="noopener"'
    if re.match(r"^(https?:|mailto:|tel:|sms:|#|data:|javascript:)", url) or not url:
        return m.group(0)
    path, sep, tail = re.match(r"^([^?#]*)([?#]?)(.*)$", url).groups()
    if path.endswith("/"):
        path += "index.html"
    return f'{attr}="{path}{sep}{tail}"'


def transform(text: str, rel: str) -> str:
    top, bottom = chrome(rel)
    text = re.sub(r'<header class="site-head">.*?</header>', top, text, flags=re.S)
    text = re.sub(r'<div class="lang-hint.*?</div></div>\s*', "", text, count=1, flags=re.S)
    text = re.sub(r'<script src="/assets/(lang|chia-se)\.js" defer></script>\s*', "", text)
    text = re.sub(r'<link rel="canonical"[^>]*>\s*', "", text)
    text = text.replace(
        '<link rel="stylesheet" href="/assets/style.css">',
        '<link rel="stylesheet" href="/assets/style.css">\n<link rel="stylesheet" href="/app/app.css">',
    )
    text = text.replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
    )
    text = text.replace("</body>", f'{bottom}\n<script src="/app/app.js"></script>\n</body>')
    text = HREF.sub(fix_link, text)
    return text


def page(title: str, body: str) -> str:
    return f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} – Dạy Nền Tảng</title>
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


# 19 truyện: (khóa, tên, nước, tuổi, đường dẫn khóa)
STORIES_GREEN = [
    ("G1", "Tấm bìa trên cánh cửa bếp", "Philippines", 6, "gia-tri-nha-minh"),
    ("G2", "Chiếc túi đồ chơi ngày thứ Ba", "Jamaica", 6, "gia-dinh-0-2"),
    ("G3", "Chiếc can vàng biết cúi chào", "Ghana", 4, "gia-dinh-2-8"),
    ("G4", "Tin nhắn chỉ có một chữ", "Mỹ", 10, "gia-dinh-10-14"),
    ("G5", "Ấm trà lúc chín giờ", "Thổ Nhĩ Kỳ", 8, "vo-chong-dong-long"),
    ("G6", "Chiếc hộp ba ổ khóa", "Niger", 8, "tien-nha-minh"),
    ("G7", "Tờ giấy dài bằng cánh cửa", "Brazil", 6, "viec-nha-chia-deu"),
    ("G8", "Tiếng chuông lúc nửa đêm", "New Zealand", 5, "nha-gon-nha-an-toan"),
    ("G9", "Chiếc loa trong mưa", "Bangladesh", 8, "gia-dinh-va-cong-dong"),
    ("C1", "Năm mươi chiếc áo hồng", "Canada", 8, "lon-len-an-toan"),
    ("C2", "Cuốn sổ của người sửa đồng hồ", "Nhật Bản", 12, "hieu-minh"),
    ("C3", "Chiếc hộp giày dưới gầm giường", "Kenya", 12, "tu-hoc-tu-quan"),
    ("C4", "Tiếng tách của chiếc cờ lê", "Đức", 12, "vung-nghe"),
    ("C7", "Chiếc xe đạp đi thẳng", "Việt Nam", 6, "tu-lap-tung-buoc"),
    ("C9", "Chiếc nút bấm cạnh giường", "Canada", 6, "van-dong-an-toan"),
    ("C10", "Ba thìa nước ở xóm Hy Vọng", "Sudan", 6, "nen-tang-khong-can-dien"),
]
STORIES_ORANGE = [
    ("C5", "Vết nứt trên tầng ba", "Bangladesh", 15, "15-phut-moi-ngay"),
    ("C6", "Người đàn bà ở trạm biên giới", "Nepal", 15, "tu-tin-an-toan"),
    ("C8", "Chiếc ghế gỗ dưới gốc cây", "Zimbabwe", 15, "cham-tam-tri-co-ban"),
]


def story_cards(items):
    out = []
    for code, name, country, age, slug in items:
        f = SRC / "truyen" / slug / "index.html"  # khi có bản chữ truyện trên website, app tự nối vào
        if f.exists():
            head = f'<a class="card" href="/truyen/{slug}/">'
            tail, state = "</a>", ""
        else:
            head, tail = '<div class="card story-soon">', "</div>"
            state = f'<p class="small"><span class="muted">Truyện sắp có.</span> <a href="/khoa-hoc/{slug}/">Học khóa liên quan →</a></p>'
        out.append(
            f'{head}<span class="tag">Từ {age} tuổi · {html.escape(country)} · Khóa {code}</span>'
            f"<h3>{html.escape(name)}</h3>{state}{tail}"
        )
    return "\n".join(out)


def extra_pages():
    truyen = f"""<p class="eyebrow">Truyện</p>
<h1>Truyện đọc cùng nhau</h1>
<p class="lead">Mười chín truyện từ khắp thế giới. Mỗi truyện có một đồ vật nhỏ và đi cùng một khóa học.</p>
<h2 class="sec-green">Phần xanh · đọc cùng con</h2>
{story_cards(STORIES_GREEN)}
<h2 class="sec-orange">Phần cam · từ 15 tuổi</h2>
<div class="box warn"><p><strong>Trước khi đọc phần cam.</strong> Ba truyện này nói về tai nạn lao động, mua bán người và khó khăn tâm lý. Không đọc cho trẻ nhỏ. Nếu bạn đang cần giúp, hãy mở <a href="/can-giup-ngay/">Cần giúp ngay</a>.</p></div>
{story_cards(STORIES_ORANGE)}
<p class="small muted">Tranh và chữ có AI hỗ trợ; tranh minh họa không phải chân dung người thật.</p>
"""
    khoa = """<p class="eyebrow">Khóa học</p>
<h1>Khóa học</h1>
<p class="lead">Mọi khóa đều đọc được khi mất mạng.</p>
<a class="card" href="/gia-dinh/"><span class="tag">9 khóa</span><h3>Gia đình</h3><p>Cho cha mẹ và người chăm sóc trẻ: giá trị, nuôi dạy con, tiền, việc nhà, nhà an toàn.</p></a>
<a class="card" href="/ca-nhan/"><span class="tag">10 khóa</span><h3>Cá nhân</h3><p>Cho người tự học: lớn lên an toàn, hiểu mình, tự học, vững nghề, chăm tâm trí.</p></a>
<a class="card" href="/cong-cu/"><span class="tag">Phiếu và bảng</span><h3>Hộp công cụ</h3><p>Phiếu, bảng và sổ dùng kèm các khóa.</p></a>
<a class="card" href="/bang-chung/"><h3>Bằng chứng và nguồn</h3><p>Mỗi nhận định trong bài đều ghi nguồn và mức chắc chắn.</p></a>
"""
    daluu = """<p class="eyebrow">Đã lưu</p>
<h1>Đã lưu</h1>
<p class="lead">Danh sách này chỉ nằm trên máy của bạn. App không gửi dữ liệu đi đâu.</p>
<h2>Đọc tiếp</h2><div id="app-last"><p class="muted">Bạn chưa mở bài nào.</p></div>
<h2>Bài đã lưu</h2><div id="app-saved"><p class="muted">Chưa có bài nào. Mở một bài rồi bấm “Lưu bài này”.</p></div>
<h2>Bài đã học xong</h2><div id="app-done"><p class="muted">Chưa có bài nào.</p></div>
"""
    return {
        "truyen/index.html": page("Truyện", truyen),
        "khoa-hoc/index.html": page("Khóa học", khoa),
        "da-luu/index.html": page("Đã lưu", daluu),
    }


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
    for rel, text in extra_pages().items():
        dst = OUT / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(transform(text, rel), encoding="utf-8")
        n += 1
    (OUT / "app").mkdir(exist_ok=True)
    for name in ("app.css", "app.js"):
        shutil.copy2(ROOT / "shell" / name, OUT / "app" / name)
    size = sum(p.stat().st_size for p in OUT.rglob("*") if p.is_file())
    print(f"{n} trang, {size/1e6:.1f} MB -> {OUT}")


if __name__ == "__main__":
    main()
