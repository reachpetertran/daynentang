#!/usr/bin/env python3
"""Sinh trang truyện cho app từ bộ nguồn sách (ban-chu-va-ma-dan-trang.zip).

Chạy khi truyện đổi:  python3 app/tools/gen_stories.py /đường/dẫn/thư-mục-đã-giải-nén
Ghi vào app/stories/: <id>.html (tiếng Việt), <id>.en.html (tiếng Anh, nếu đã dịch), <id>.webp, stories.json.
Bản dịch tiếng Anh nằm ở app/stories_en/ (<id>.txt và meta_en.json). build_www.py đọc app/stories/.
"""
import html as H, io, json, pathlib, sys

SRC = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(SRC / "build"))
import book  # noqa: E402

APP = pathlib.Path(__file__).resolve().parent.parent
OUT = APP / "stories"
EN = APP / "stories_en"
OUT.mkdir(exist_ok=True)
META_EN = json.loads((EN / "meta_en.json").read_text(encoding="utf-8")) if (EN / "meta_en.json").exists() else {}
EN_COURSES = {"gia-dinh-2-8": "/en/courses/family-2-8/"}

L = {
    "vi": dict(green="Phần xanh · đọc cùng con", orange="Phần cam · từ 15 tuổi", course="Khóa", by="Liêm kể", where="Ở đâu", obj="Đồ vật",
               age="Tuổi đọc", crs="Khóa học", alt="Tranh minh họa truyện", cap="Tranh minh họa do AI tạo, không phải chân dung người thật.",
               objh="Đồ vật của truyện", talk="Cùng trò chuyện", act="Một việc trong tuần này", safe="An toàn", more="Học tiếp, miễn phí", note=""),
    "en": dict(green="Green part · read with children", orange="Orange part · from age 15", course="Course", by="Told by Liêm", where="Where", obj="Object",
               age="Reading age", crs="Course", alt="Illustration for the story", cap="Illustration created with AI; not a portrait of any real person.",
               objh="The object in this story", talk="Talk together", act="One thing to do this week", safe="Safety", more="Keep learning, free",
               note=' <span class="small muted">(course in Vietnamese)</span>'),
}


def paras(text):
    out, first = [], True
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line == "*":
            out.append('<p class="sep" aria-hidden="true">* * *</p>'); first = True; continue
        cls = []
        if line.startswith("!"):
            line = line[1:].strip(); cls.append("bip")
        if first and not line.startswith("—"):
            cls.append("first")
        first = False
        attr = f' class="{" ".join(cls)}"' if cls else ""
        out.append(f"<p{attr}>{H.escape(line)}</p>")
    return "\n".join(out)


def fragment(sid, st, kind, text, slug, cam, lang):
    t = L[lang]
    curl = f"/khoa-hoc/{slug}/"
    note = t["note"]
    if lang == "en" and slug in EN_COURSES:
        curl, note = EN_COURSES[slug], ""
    li = "".join(f"<li><strong>{a}:</strong> {b}</li>" for a, b in st["bullets"])
    return f'''<p class="eyebrow">{t["orange"] if cam else t["green"]} · {t["course"]} {sid.upper()}</p>
<h1>{st["title"]}</h1>
<p class="story-by">{t["by"]}</p>
<div class="table-wrap"><table><tbody>
<tr><th>{t["where"]}</th><td>{st["where"]}</td></tr>
<tr><th>{t["obj"]}</th><td>{st["obj"]}</td></tr>
<tr><th>{t["age"]}</th><td>{st["age"]}</td></tr>
<tr><th>{t["crs"]}</th><td><a href="{curl}">{st["course"]}</a>{note}</td></tr>
</tbody></table></div>
<div class="box"><p><strong>{kind}.</strong> {st["label"]}</p></div>
<figure class="story-plate"><img src="/truyen/tranh/{sid}.webp" alt="{t["alt"]} {H.escape(st["title"])}" width="830" height="1230" loading="lazy">
<figcaption>{t["cap"]}</figcaption></figure>
<div class="story-text">
{paras(text)}
</div>
<div class="card story-object"><div class="story-spot" aria-hidden="true">{st["spot"]}</div>
<p class="eyebrow">{t["objh"]}</p><h2>{st["obj"]}</h2><ul>{li}</ul></div>
<h2>{t["talk"]}</h2>
<ol>{"".join(f"<li>{q}</li>" for q in st["qs"])}</ol>
<h2>{t["act"]}</h2>
<div class="box"><p>{st["act"]}</p></div>
<h2>{t["safe"]}</h2>
<div class="box warn">{"".join(f"<p>{s}</p>" for s in st["safe"])}</div>
<a class="card" href="{curl}"><span class="tag">{t["more"]}</span><h3>{st["course"]}</h3><p>{st["more"]}</p></a>
'''


index, SVGS = [], {}
for f in OUT.glob("*.html"):
    f.unlink()
for sid in book.ORDER:
    st = dict(book.ALL[sid])
    slug = st["url"].rstrip("/").rsplit("/", 1)[1]
    cam = st.get("part") == "cam"
    SVGS[sid] = st["scene"]()
    text = (SRC / "text" / st["file"]).read_text(encoding="utf-8")
    (OUT / f"{sid}.html").write_text(fragment(sid, st, book.KIND[st["kind"]], text, slug, cam, "vi"), encoding="utf-8")
    age = int("".join(ch for ch in st["age"].split("tuổi")[0] if ch.isdigit()))
    row = dict(id=sid, title=st["title"], country=st["country"], age=age, part="cam" if cam else "xanh", slug=slug)
    if sid in META_EN and (EN / f"{sid}.txt").exists():
        en = dict(st); en.update(META_EN[sid])
        en["bullets"] = [tuple(b) for b in en["bullets"]]
        (OUT / f"{sid}.en.html").write_text(fragment(sid, en, en["kind"], (EN / f"{sid}.txt").read_text(encoding="utf-8"), slug, cam, "en"), encoding="utf-8")
        row.update(en_title=en["title"], en_country=en["country"])
    index.append(row)
(OUT / "stories.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")

# Tranh: đổi SVG (có bộ lọc nét chì, nặng với máy yếu) thành ảnh WebP để cuộn mượt
from PIL import Image
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(); pg = b.new_page(viewport={"width": 830, "height": 1230}, device_scale_factor=1.3)
    for sid, svg in SVGS.items():
        svg = svg.replace('width="1660" height="2460"', 'width="830" height="1230"', 1)
        pg.set_content(f'<html><body style="margin:0">{svg}</body></html>')
        png = pg.screenshot(clip={"x": 0, "y": 0, "width": 830, "height": 1230})
        Image.open(io.BytesIO(png)).convert("RGB").save(OUT / f"{sid}.webp", "WEBP", quality=80, method=6)
    b.close()
print(len(index), "truyện,", sum("en_title" in r for r in index), "bản tiếng Anh ->", OUT)
