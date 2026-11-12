#!/usr/bin/env python3
"""Sinh trang truyện cho app từ bộ nguồn sách (ban-chu-va-ma-dan-trang.zip).

Chạy một lần khi truyện đổi:  python3 app/tools/gen_stories.py /đường/dẫn/thư-mục-đã-giải-nén
Kết quả ghi vào app/stories/ (đoạn HTML, tranh SVG, stories.json). build_www.py đọc từ đó.
Truyện C7 trong app đã đổi bối cảnh sang Bhutan theo quyết định của Peter (12/11/2026).
"""
import html as H, json, pathlib, sys

SRC = pathlib.Path(sys.argv[1]).resolve()
sys.path.insert(0, str(SRC / "build"))
import book  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent.parent / "stories"
OUT.mkdir(exist_ok=True)

C7_SWAPS = [
    ("Ở vùng trung du xứ Thanh có một xóm nhỏ, đường vào toàn sỏi với đất đỏ.",
     "Ở một thung lũng của Bhutan có một xóm nhỏ nằm lưng chừng núi, đường vào toàn sỏi với đất đỏ."),
    ("như người đi qua cầu khỉ", "như người đi qua cầu treo"),
    ("Khôi đỗ ngành máy tính của một trường đại học lớn ở Hà Nội. Sơn muốn làm bác sĩ, và vào một trường y ở tỉnh khác.",
     "Khôi đỗ ngành máy tính của một trường đại học ở xa nhà. Sơn muốn làm bác sĩ, và vào một trường y ở vùng khác."),
    ("trong một hội trường lớn ở Hà Nội", "trong hội trường lớn của trường đại học"),
    ("Sơn", "Dorji"), ("Khôi", "Tashi"),
]
C7_META = dict(
    country="Bhutan", where="Một xóm lưng chừng núi ở Bhutan",
    kindlabel="Phỏng theo chuyện có thật · đã đổi nơi chốn",
    label="Phỏng theo một chuyện có thật: một cậu bé xin cha mẹ cho cõng người bạn cùng xóm không đi lại được đến trường từ năm lớp hai, "
          "rồi đưa bạn đi học suốt mười năm. Người bạn từ chối vào thẳng lớp mười để tự thi. Cả hai cùng đỗ đại học; năm năm sau, "
          "cậu lại cõng bạn lên nhận bằng tốt nghiệp. Chuyện gốc không xảy ra ở Bhutan: nơi chốn và tên người đã được đổi. "
          "Lời thoại, buổi nói chuyện ở hiên nhà và nhiều chi tiết do người viết thêm vào.",
)


def swap(s):
    for a, b in C7_SWAPS:
        s = s.replace(a, b)
    return s


def paras(st):
    text = (SRC / "text" / st["file"]).read_text(encoding="utf-8")
    if st["id"] == "c7":
        text = swap(text)
        assert "Thanh" not in text and "Hà Nội" not in text and "Sơn" not in text and "Khôi" not in text
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
        out.append(f'<p{" class=" + chr(34) + " ".join(cls) + chr(34) if cls else ""}>{H.escape(line)}</p>')
    return "\n".join(out)


index = []
SVGS = {}
for sid in book.ORDER:
    st = dict(book.ALL[sid])
    kind = book.KIND.get(st.get("kind", "real"), "Dựa trên chuyện có thật")
    if sid == "c7":
        st.update({k: v for k, v in C7_META.items() if k != "kindlabel"})
        kind = C7_META["kindlabel"]
        st["qs"] = [swap(q) for q in st["qs"]]
        st["bullets"] = [(a, swap(t)) for a, t in st["bullets"]]
    slug = st["url"].rstrip("/").rsplit("/", 1)[1]
    cam = st.get("part") == "cam"
    SVGS[sid] = st["scene"]()
    li = "".join(f"<li><strong>{a}:</strong> {t}</li>" for a, t in st["bullets"])
    part = "Phần cam · từ 15 tuổi" if cam else "Phần xanh · đọc cùng con"
    frag = f'''<p class="eyebrow">{part} · Khóa {sid.upper()}</p>
<h1>{st["title"]}</h1>
<p class="story-by">Liêm kể</p>
<div class="table-wrap"><table><tbody>
<tr><th>Ở đâu</th><td>{st["where"]}</td></tr>
<tr><th>Đồ vật</th><td>{st["obj"]}</td></tr>
<tr><th>Tuổi đọc</th><td>{st["age"]}</td></tr>
<tr><th>Khóa học</th><td><a href="/khoa-hoc/{slug}/">{st["course"]}</a></td></tr>
</tbody></table></div>
<div class="box"><p><strong>{kind}.</strong> {st["label"]}</p></div>
<figure class="story-plate"><img src="/truyen/tranh/{sid}.webp" alt="Tranh minh họa truyện {H.escape(st["title"])}" width="830" height="1230" loading="lazy">
<figcaption>Tranh minh họa do AI tạo, không phải chân dung người thật.</figcaption></figure>
<div class="story-text">
{paras(st)}
</div>
<div class="card story-object"><div class="story-spot" aria-hidden="true">{st["spot"]}</div>
<p class="eyebrow">Đồ vật của truyện</p><h2>{st["obj"]}</h2><ul>{li}</ul></div>
<h2>Cùng trò chuyện</h2>
<ol>{"".join(f"<li>{q}</li>" for q in st["qs"])}</ol>
<h2>Một việc trong tuần này</h2>
<div class="box"><p>{st["act"]}</p></div>
<h2>An toàn</h2>
<div class="box warn">{"".join(f"<p>{s}</p>" for s in st["safe"])}</div>
<a class="card" href="/khoa-hoc/{slug}/"><span class="tag">Học tiếp, miễn phí</span><h3>{st["course"]}</h3><p>{st["more"]}</p></a>
'''
    (OUT / f"{sid}.html").write_text(frag, encoding="utf-8")
    age = int("".join(ch for ch in st["age"].split("tuổi")[0] if ch.isdigit()))
    index.append(dict(id=sid, title=st["title"], country=st["country"], age=age, part="cam" if cam else "xanh", slug=slug))
(OUT / "stories.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")

# Tranh: đổi SVG (có bộ lọc nét chì, nặng với máy yếu) thành ảnh WebP để cuộn mượt
import io
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
print(len(index), "truyện ->", OUT)
