# Khóa G1 "Giá trị nhà mình" – trang khóa, 8 bài, 2 công cụ in
import illus_g1  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/gia-tri-nha-minh/'
TOOL_V = '/cong-cu/phieu-gia-tri/'
TOOL_M = '/cong-cu/bien-ban-hop-gia-dinh/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
def sec(n, title, body): return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'
def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>{need}</em></p><ol>{li}</ol>{nt}</div>'
def journal(rows):
    r = ''.join(f'<tr><th class="w38">{x}</th><td></td></tr>' for x in rows)
    return f'<div class="table-wrap journal"><table><tbody>{r}</tbody></table></div>'
J_A = journal(['Bố mẹ đã chốt được gì', 'Điều gì khó', 'Cần sửa gì'])
J_B = journal(['Con làm được gì', 'Con thích gì', 'Cần sửa gì'])

CDC = '<a href="https://www.cdc.gov/parenting-toddlers/structure-rules/rules.html">CDC – Creating Rules</a>'
WHO_CP = '<a href="https://www.who.int/news-room/fact-sheets/detail/corporal-punishment-and-health">WHO 2026</a>'
GG = 'Grusec &amp; Goodnow 1994, <em>Developmental Psychology</em> 30(1):4–19'
FIESE = '<a href="https://pubmed.ncbi.nlm.nih.gov/12561283/">Fiese et al. 2002</a>'
GOLL = '<a href="https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f">Gollwitzer &amp; Sheeran 2006</a>'
MCC = '<a href="https://mcc.gse.harvard.edu/reports/children-mean-raise">Making Caring Common, Harvard 2014</a>'
PLH = '<a href="https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health">Parenting for Lifelong Health (WHO/UNICEF)</a>'
NOVIOL = 'Không đánh, không dọa bỏ rơi, không phạt nhịn ăn. Đánh đòn không có lợi ích nào và gây hại cho trẻ (' + WHO_CP + ').'

L = {
 '1a': (1, '1a-bo-me-chon-gia-tri', '1A', 'Bố mẹ chọn giá trị'),
 '1b': (1, '1b-mai-nha-gia-tri', '1B', 'Mái nhà giá trị'),
 '2a': (2, '2a-gia-tri-thanh-viec-lam', '2A', 'Giá trị thành việc làm'),
 '2b': (2, '2b-tham-tu-gia-tri', '2B', 'Thám tử giá trị'),
 '3a': (3, '3a-soan-noi-quy', '3A', 'Soạn nội quy nhà mình'),
 '3b': (3, '3b-ca-nha-thong-qua-noi-quy', '3B', 'Cả nhà thông qua nội quy'),
 '4a': (4, '4a-thiet-ke-buoi-hop', '4A', 'Thiết kế buổi họp 15 phút'),
 '4b': (4, '4b-hop-gia-dinh-dau-tien', '4B', 'Họp gia đình đầu tiên'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, meta, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'g1-' + k
    note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này đã soạn theo khung của khóa nhưng chưa được dạy thử trong gia đình. '
            f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về bài {code}</a></p></div>')
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Giá trị nhà mình</a> · Tuần {w} · {code}</p>
<h1>{title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block('V' + code)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/gia-dinh/')

# =============== TUẦN 1 ===============
lesson('1a', 'Khóa Giá trị nhà mình, bài 1A: bố mẹ ngồi với nhau 30 phút, chọn 3–5 giá trị chung và đổi thành lời con hiểu.',
 ['Buổi bố mẹ', 'Tuần 1', '30 phút'], [
 sec(1, 'Mục tiêu', ul(['Bố mẹ viết ra <strong>3–5 giá trị</strong> mà cả hai cùng đồng ý.',
   'Mỗi giá trị có <strong>một câu ngắn</strong> mà con khoảng 7 tuổi nói lại được.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In <a href="{TOOL_V}">Phiếu giá trị</a> (20 thẻ), mỗi người một bản. Không in được thì chép tay ra giấy.',
   'Hai cây bút, một tờ giấy trắng.', 'Chọn giờ con đã ngủ. Tắt tivi, úp điện thoại.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người trả lời thầm một câu: <em>"Khi con 25 tuổi, mình mong con là người thế nào?"</em> Chưa nói ra vội.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Nhớ lại (5 phút).</strong> Mỗi người kể một lần mình tự hào về gia đình. Người kia chỉ nghe, không bình luận.',
   '<strong>Tự chọn (5 phút).</strong> Mỗi người tự khoanh 5 thẻ trên phiếu của mình. Không nhìn phiếu người kia.',
   '<strong>So sánh (8 phút).</strong> Đặt hai phiếu cạnh nhau. Giá trị cả hai cùng chọn thì giữ. Giá trị chỉ một người chọn thì hỏi: "Vì sao điều này quan trọng với anh/em?"',
   '<strong>Chốt (4 phút).</strong> Giữ 3–5 giá trị. Ít hơn thì dễ nhớ hơn. Nếu nhà có con 2–3 tuổi, nên bắt đầu với 3.',
   '<strong>Đổi thành lời con hiểu (3 phút).</strong> Ví dụ: "Trách nhiệm" thành "Việc của mình, mình làm".',
   'Viết 3–5 giá trị và câu ngắn lên giấy. Dán ở chỗ chỉ bố mẹ thấy, chờ buổi cả nhà.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Giá trị nào mình đang sống tốt? Giá trị nào mình mới chỉ mong?',
   'Có giá trị nào bố mẹ mình (ông bà) truyền lại mà mình muốn giữ?', 'Giá trị nào mình hay quên nhất khi mệt hoặc khi bực?'])),
 sec(6, 'An toàn và ranh giới', ul(['Nếu hai người bất đồng gay gắt, dừng lại. Chỉ giữ giá trị chung, bàn tiếp tuần sau.',
   'Giá trị là điều nhà mình muốn sống theo, không phải cái cớ để chê bai người khác.',
   'Nếu trong nhà có bạo lực, an toàn đến trước. Gọi 113 khi nguy hiểm tức thì; trẻ em bị hại gọi 111.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 1 phiếu giá trị, 1 cây bút, 20 phút. Có thể gọi video với bố.', [
   ('Phút 0–5.', 'Mẹ tự khoanh 5 thẻ. Chụp phiếu gửi bố, bố cũng khoanh 5 thẻ trên phiếu của mình.'),
   ('Phút 5–15.', 'Gọi video: so sánh hai phiếu, hỏi nhau "vì sao?", chốt 3–5 giá trị.'),
   ('Phút 15–20.', 'Mẹ viết câu ngắn cho từng giá trị. Gửi bố đọc lại.')], [
   ('Nếu nhà chỉ có một bố hoặc một mẹ:', 'tự chọn 3–5 giá trị là đủ. Có thể hỏi ý ông bà hoặc người cùng chăm con.')])),
 sec(8, 'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> mỗi người đọc lại danh sách. Còn đồng ý không?',
   '<strong>Sau 1 tuần:</strong> mỗi người kể một lần mình đã sống đúng một giá trị trong tuần.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Nhóm nghiên cứu Making Caring Common (Harvard) khuyên bố mẹ tự xem lại giá trị mình thực sự đang truyền cho con ({MCC}).'),
   lb('Đánh giá chuyên môn', 'Cách "tự chọn trước, so sánh sau" và phiếu 20 thẻ do daynentang.com thiết kế, chưa có nghiên cứu riêng.'),
   lb('Suy luận', 'Chọn 3–5 giá trị thay vì nhiều hơn là để dễ nhớ; hướng dẫn CDC cho thấy trẻ nhỏ nhớ khoảng 2–3 luật một lúc.')]))
])

lesson('1b', 'Khóa Giá trị nhà mình, bài 1B: cả nhà 15–20 phút. Bố mẹ kể chuyện thật, con vẽ Mái nhà giá trị và dán lên tường.',
 ['Buổi cả nhà', 'Tuần 1', '15–20 phút'], [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn (khoảng 7 tuổi):</strong> nói lại được ít nhất 2 giá trị bằng lời của mình và vẽ Mái nhà giá trị.',
   '<strong>Con nhỏ (khoảng 2 tuổi):</strong> làm theo ít nhất 1 động tác gắn với giá trị.',
   '<strong>Bố mẹ:</strong> kể mỗi giá trị bằng một chuyện thật của nhà mình, không giảng giải.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Danh sách 3–5 giá trị từ bài 1A.', 'Giấy A3 hoặc hai tờ A4 dán lại, bút sáp to.',
   'Nghĩ trước một chuyện thật cho mỗi giá trị. Ví dụ: "Hôm qua con tự nhận làm đổ sữa".'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Nhà nào cũng có mái để che mưa. Hôm nay nhà mình làm một mái nhà đặc biệt: những điều nhà mình coi trọng."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Bố mẹ giới thiệu từng giá trị bằng câu ngắn và một chuyện thật. Mỗi giá trị không quá 1 phút.',
   'Con vẽ ngôi nhà: mái to, bên dưới có 3–5 cột. Mỗi cột ghi hoặc vẽ một giá trị.',
   'Hỏi con: "Tuần này con thấy ai trong nhà làm điều này rồi?"',
   'Cả nhà dán Mái nhà ở chỗ ai cũng thấy, ví dụ cạnh bàn ăn.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Mỗi giá trị một động tác: tay đặt lên ngực là "nói thật", vuốt nhẹ tay là "nhẹ tay", giơ ngón cái là "tự làm".',
   'Bố mẹ làm trước, con bắt chước. Con tô màu một cột cùng anh.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> mời con đề xuất thêm 1 giá trị hoặc đổi câu ngắn cho hợp ý con.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Giá trị nào con thích nhất? Vì sao?', 'Có lúc nào giữ giá trị này khó không?', 'Con muốn nhà mình thêm điều gì nữa?'])),
 sec(6, 'An toàn', ul(['Con nhỏ: bút sáp loại to, không có nắp nhỏ. Cất sáp gãy vụn.', 'Không dùng Mái nhà để chê con ("con không có trung thực"). Mái nhà là để ghi nhận.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: danh sách giá trị, giấy to, bút sáp. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Nói về mái nhà đặc biệt.'),
   ('Phút 2–6 – Kể chuyện.', 'Mẹ kể mỗi giá trị bằng một chuyện thật, thật ngắn.'),
   ('Phút 6–12 – Vẽ.', 'Con lớn vẽ Mái nhà; con nhỏ làm động tác và tô màu cùng.'),
   ('Phút 12–15 – Dán.', 'Dán lên tường, hỏi "Ai đã làm điều này?"')], [
   ('Gọi video với bố:', 'bố có thể kể chuyện thật cho một giá trị qua điện thoại.'),
   ('Nhắn bố 1 câu:', 'giá trị con thích nhất.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi bữa tối:</strong> chỉ lên Mái nhà, hỏi "Hôm nay ai làm điều nào?"', '<strong>Sau 1 tuần:</strong> con nói lại được mấy giá trị? Ghi vào nhật ký.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Theo một mô hình lý thuyết, con tiếp nhận giá trị khi con hiểu đúng thông điệp của bố mẹ và chấp nhận nó ({GG}).'),
   lb('Suy luận', 'Chuyện thật và câu ngắn giúp con hiểu đúng thông điệp hơn lời giảng dài; đây là cách chúng tôi áp dụng mô hình trên.'),
   lb('Đánh giá chuyên môn', 'Mái nhà giá trị và động tác tay do daynentang.com thiết kế.')]))
])

# =============== TUẦN 2 ===============
lesson('2a', 'Khóa Giá trị nhà mình, bài 2A: bố mẹ biến mỗi giá trị thành việc nhìn thấy được, và viết sẵn câu "Nếu… thì…".',
 ['Buổi bố mẹ', 'Tuần 2', '30 phút'], [
 sec(1, 'Mục tiêu', ul(['Mỗi giá trị có <strong>2 việc con làm</strong> và <strong>2 việc bố mẹ làm</strong>, đều nhìn thấy được.',
   'Bố mẹ viết sẵn <strong>3 câu "Nếu… thì…"</strong> cho 3 tình huống hay gặp.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Bảng "Giá trị → việc làm" trong <a href="{TOOL_V}">Phiếu giá trị</a>.', 'Danh sách giá trị từ tuần 1.', 'Nhớ lại 3 lúc trong tuần bố mẹ dễ bực nhất.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Hỏi nhau: <em>"Nếu một người lạ ở nhà mình một ngày, họ thấy việc gì để biết nhà mình coi trọng trung thực?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Việc nhìn thấy được (12 phút).</strong> Với mỗi giá trị, viết 2 việc con làm và 2 việc bố mẹ làm. Tránh từ chung chung như "ngoan", "giỏi".',
   'Ví dụ, "Trung thực": con tự nói khi làm đổ, làm hỏng; bố mẹ nhận khi mình nói sai, giữ lời hứa nhỏ.',
   '<strong>Câu khen gắn giá trị (5 phút).</strong> Mỗi giá trị viết một câu khen cụ thể. Ví dụ: "Con tự nhận làm đổ nước. Đó là nói thật."',
   '<strong>"Nếu… thì…" (8 phút).</strong> Chọn 3 lúc dễ bực. Viết sẵn câu sẽ nói. Ví dụ: "Nếu con làm đổ và nói thật, thì mình nói: Cảm ơn con đã nói thật, mình lau cùng nhé."',
   'Dán 3 câu "Nếu… thì…" ở chỗ bố mẹ hay nhìn, ví dụ cửa tủ lạnh phía trong.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Việc nào trong danh sách mình đang làm chưa tốt?', 'Con học giá trị từ lời mình nói hay từ việc mình làm nhiều hơn?', 'Ai sẽ nhắc ai khi một người quên?'])),
 sec(6, 'An toàn và ranh giới', ul(['Việc của con phải hợp tuổi. Con 2 tuổi chưa thể "tự nhận lỗi" bằng lời; chỉ cần con chỉ tay hoặc đưa đồ.', NOVIOL])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: bảng giá trị → việc làm, 20 phút.', [
   ('Phút 0–10.', 'Mẹ viết việc con làm và việc mẹ làm cho mỗi giá trị.'),
   ('Phút 10–15.', 'Mẹ viết 3 câu "Nếu… thì…".'),
   ('Phút 15–20.', 'Gửi ảnh cho bố. Bố thêm việc bố làm khi về nhà.')], [
   ('Giữ đơn giản:', 'nếu mệt, mỗi giá trị chỉ cần 1 việc con làm và 1 việc mẹ làm.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> mỗi người dùng ít nhất 1 câu khen gắn giá trị.', '<strong>Sau 1 tuần:</strong> câu "Nếu… thì…" nào mình đã dùng được? Câu nào cần sửa?'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Phân tích gộp 94 thử nghiệm: lập kế hoạch "khi nào, ở đâu, làm thế nào" giúp đạt mục tiêu tốt hơn, mức hiệu quả trung bình đến lớn, d = 0,65 ({GOLL}).'),
   lb('Suy luận', 'Các thử nghiệm đó chủ yếu làm với người lớn tự thay đổi bản thân, không riêng cho việc nuôi dạy con.'),
   lb('Đã xác nhận', f'Khen cụ thể là một thành phần của chương trình {PLH}.'),
   lb('Đã xác nhận', f'Theo mô hình của {GG}, con cần hiểu đúng và thấy hợp lý thì mới tự làm theo giá trị.')]))
])

lesson('2b', 'Khóa Giá trị nhà mình, bài 2B: trò Thám tử giá trị. Cả nhà tìm và kể việc tốt của nhau, rồi đóng vai tình huống.',
 ['Buổi cả nhà', 'Tuần 2', '15–20 phút'], [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> kể được ít nhất 3 việc tốt của người khác trong tuần và chọn cách làm hợp giá trị trong 2 tình huống đóng vai.',
   '<strong>Con nhỏ:</strong> làm lại động tác giá trị khi được khen.', '<strong>Bố mẹ:</strong> khen gắn giá trị ít nhất 1 lần mỗi ngày.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Một tờ giấy làm bảng "Nhà mình đã thấy", mỗi giá trị một dòng.', 'Bút sáp, sticker hoặc tự vẽ ngôi sao.', 'Một cái "kính lúp" tự làm bằng bìa (không cần thật).'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Tuần này cả nhà làm thám tử. Thám tử không đi bắt lỗi. Thám tử đi tìm việc tốt."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Bố mẹ làm mẫu: "Bố thấy con tự cất cặp hôm qua. Đó là <em>tự làm</em>." Vẽ một ngôi sao vào dòng đó.',
   'Con làm thám tử: kể một việc tốt con thấy bố, mẹ hoặc em làm. Vẽ sao.',
   'Đóng vai tình huống 1: "Con lỡ làm vỡ cốc của mẹ. Con có hai cách: giấu đi, hoặc nói thật và cùng dọn." Con chọn và giải thích.',
   'Tình huống 2 do con tự nghĩ ra. Bố mẹ đóng vai, con chọn cách hợp với nhà mình.',
   'Thống nhất: cả tuần, ai thấy việc tốt thì kể vào bữa tối và vẽ sao.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Khi con cất đồ, bố mẹ khen: "Con tự cất! Tự làm!" và giơ ngón cái.', 'Con dán sticker vào bảng cùng anh.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> tình huống có thể khó hơn, ví dụ thấy bạn chép bài, hay nhặt được tiền.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Được người khác thấy việc tốt của mình, con thấy thế nào?', 'Trong tình huống cái cốc, vì sao nói thật lại khó?', 'Giá trị nào nhà mình thấy nhiều nhất tuần này?'])),
 sec(6, 'An toàn', ul(['Không biến trò chơi thành "mách lỗi". Chỉ kể việc tốt.', 'Kính lúp tự làm bằng bìa, không dùng kính thật có thể vỡ.', 'Sticker nhỏ: người lớn giữ, con nhỏ dán dưới sự quan sát.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 1 tờ giấy, bút. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', '"Thám tử đi tìm việc tốt."'),
   ('Phút 2–6 – Làm mẫu.', 'Mẹ kể một việc tốt của con lớn, một của con nhỏ. Vẽ sao.'),
   ('Phút 6–12 – Đóng vai.', 'Tình huống cái cốc; con chọn cách và giải thích.'),
   ('Phút 12–15 – Hẹn cả tuần.', 'Kể việc tốt vào bữa tối.')], [
   ('Bố cũng là thám tử:', 'khi gọi video, bố kể một việc tốt bố nghe mẹ kể về con.'),
   ('Nhắn bố 1 câu:', 'việc tốt con kể được.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi bữa tối:</strong> mỗi người kể 1 việc tốt đã thấy, vẽ sao.', '<strong>Sau 1 tuần:</strong> đếm sao. Giá trị nào ít sao? Tuần sau cả nhà để ý giá trị đó hơn.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Making Caring Common khuyên cho trẻ cơ hội thường xuyên để thực hành quan tâm người khác ({MCC}).'),
   lb('Đã xác nhận', 'Truyện khen nhân vật nói thật làm trẻ 3–7 tuổi nhận lỗi nhiều hơn; truyện dọa thì không (Lee et al. 2014, <a href="/bang-chung/">xem trang Bằng chứng</a>).'),
   lb('Đánh giá chuyên môn', 'Trò Thám tử giá trị và bảng sao do daynentang.com thiết kế.')]))
])

# =============== TUẦN 3 ===============
lesson('3a', 'Khóa Giá trị nhà mình, bài 3A: bố mẹ soạn 3–5 nội quy đi ra từ giá trị, nói điều cần làm, có lời khen và hậu quả nhỏ báo trước.',
 ['Buổi bố mẹ', 'Tuần 3', '30 phút'], [
 sec(1, 'Mục tiêu', ul(['Bố mẹ có <strong>bảng nội quy 3–5 điều</strong>; nhà có con 2–4 tuổi thì bắt đầu với 2–3 điều.',
   'Mỗi điều có: giá trị gốc, câu nói điều cần làm, lời khen, và một hậu quả nhỏ báo trước.', 'Mọi người lớn chăm con đều biết bảng này.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Bảng "Nội quy" trong <a href="{TOOL_V}">Phiếu giá trị</a>.', 'Danh sách giá trị và bảng việc làm tuần 2.', 'Ghi lại 3 việc trong nhà hay gây cãi nhau nhất.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Hỏi nhau: <em>"Câu nào mình nói với con nhiều nhất mỗi ngày?"</em> Câu đó thường gợi ý luật nhà mình đang thiếu.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Chọn việc (5 phút).</strong> Từ 3 việc hay gây cãi nhau, chọn 2–3 việc quan trọng nhất. Mỗi việc nối với một giá trị.',
   '<strong>Nói điều cần làm (7 phút).</strong> Đổi "Không đánh em" thành "Tay nhẹ nhàng với em". Đổi "Không bừa bộn" thành "Chơi xong, cất về rổ".',
   '<strong>Lời khen (3 phút).</strong> Mỗi luật một câu khen ngay khi con làm đúng.',
   '<strong>Hậu quả nhỏ (7 phút).</strong> Hậu quả ngắn, liên quan, báo trước. Ví dụ: ném đồ chơi thì đồ chơi đó "nghỉ" đến bữa tối. Áp dụng giống nhau dù con cố ý hay quên.',
   '<strong>Người lớn thống nhất (3 phút).</strong> Ai sẽ nói với ông bà, người giúp việc? Bố mẹ cũng theo nội quy, ví dụ "nói nhỏ trong nhà".'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Luật nào mình đặt ra vì giá trị, luật nào chỉ vì mình mệt?', 'Hậu quả nào mình chắc chắn làm được, kể cả khi mệt?', 'Khi một người đã nói hậu quả, người kia có ủng hộ không?'])),
 sec(6, 'An toàn và ranh giới', ul([NOVIOL, 'Hậu quả không làm con xấu hổ trước người khác và không kéo dài nhiều ngày.',
   'Luật về an toàn (ổ điện, đường phố, nước) thì không bàn lượng: người lớn giữ con ngay, giải thích sau.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: bảng nội quy, 20 phút. Chốt cuối cùng nên có cả bố.', [
   ('Phút 0–10.', 'Mẹ chọn 2–3 việc và viết câu nói điều cần làm.'),
   ('Phút 10–15.', 'Mẹ viết lời khen và hậu quả nhỏ.'),
   ('Phút 15–20.', 'Gọi bố: đọc từng luật, bố đồng ý hoặc sửa. Chỉ dán khi cả hai đồng ý.')], [
   ('Nếu ông bà cùng chăm con:', 'đưa ông bà xem bảng và hỏi "Bố mẹ có góp ý gì không?" Ông bà được hỏi thì dễ ủng hộ hơn.')])),
 sec(8, 'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> mỗi người nói lại các luật mà không nhìn giấy.', '<strong>Sau 1 tuần:</strong> luật nào con theo được? Luật nào khó? Có cần bớt một luật không?'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CDC khuyên với trẻ 2–4 tuổi: giữ 2–3 luật một lúc, nói rõ hành vi muốn thấy, hợp tuổi, mọi người chăm con dùng cùng luật, khen cụ thể khi con theo luật, dán bảng luật có hình ({CDC}).'),
   lb('Đã xác nhận', f'Đánh đòn gây hại sức khỏe thể chất và tinh thần của trẻ, làm hành vi xấu tăng lên theo thời gian và không có kết quả tích cực nào ({WHO_CP}).'),
   lb('Đánh giá chuyên môn', 'Công thức "giá trị – luật – khen – hậu quả" do daynentang.com ghép lại từ các nguồn trên.')]))
])

lesson('3b', 'Khóa Giá trị nhà mình, bài 3B: cả nhà đọc nội quy, con góp ý, vẽ tranh cho mỗi luật và in dấu tay đồng ý.',
 ['Buổi cả nhà', 'Tuần 3', '15–20 phút'], [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> nói lại các luật bằng lời của mình, góp ý ít nhất 1 điều, vẽ tranh cho mỗi luật.',
   '<strong>Con nhỏ:</strong> chỉ đúng tranh của 1 luật khi được hỏi; in dấu tay.', '<strong>Bố mẹ:</strong> nhắc luật bằng một câu, không giảng.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Bảng nội quy từ bài 3A, chép to lên giấy, chừa chỗ vẽ tranh.', 'Màu nước rửa được hoặc mực dấu tay loại an toàn cho trẻ, khăn ướt.', 'Băng dính để dán bảng.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Đội bóng nào cũng có luật chơi. Nhờ có luật mà trận đấu vui và công bằng. Nhà mình cũng có luật."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Bố mẹ đọc từng luật và nói giá trị gốc: "Luật này đi ra từ <em>nhẹ tay</em>."',
   'Con nói lại luật bằng lời của mình. Con góp ý: luật nào khó? Có cần sửa chữ nào không? Bố mẹ sửa nếu hợp lý.',
   'Con vẽ một hình nhỏ cạnh mỗi luật để em nhớ.',
   'Đóng vai nhắc luật: con giả vờ quên, bố mẹ nhắc một câu "Luật nhà mình là…", rồi chờ 5 giây.',
   'Cả nhà in dấu tay ở cuối bảng. Dán ở chỗ ai cũng thấy.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Chỉ tranh và hỏi: "Tay thế nào với em?" Con làm động tác vuốt nhẹ.', 'Con in dấu tay cạnh tay anh.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con có thể đề xuất một luật cho bố mẹ, ví dụ "không xem điện thoại trong bữa ăn".</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Luật nào con thấy dễ nhất? Khó nhất?', 'Vì sao bố mẹ cũng phải theo luật?', 'Khi ai đó quên luật, mình nhắc thế nào cho tử tế?'])),
 sec(6, 'An toàn', ul(['Màu dấu tay loại ghi an toàn cho trẻ em, rửa được. Không để con nhỏ cho tay vào miệng; rửa tay ngay sau đó.', NOVIOL])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: bảng nội quy viết to, màu dấu tay, khăn ướt. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Ví dụ luật chơi bóng.'),
   ('Phút 2–7 – Đọc luật.', 'Con lớn nói lại từng luật, góp ý.'),
   ('Phút 7–12 – Vẽ và in tay.', 'Con lớn vẽ tranh; con nhỏ in dấu tay. Chừa chỗ cho tay bố.'),
   ('Phút 12–15 – Dán.', 'Dán bảng ở chỗ dễ thấy.')], [
   ('Khi bố về:', 'bố in dấu tay vào chỗ đã chừa, đọc lại luật cùng con.'),
   ('Nhắn bố 1 câu:', 'góp ý của con về nội quy.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> khen ngay khi con theo luật, nói rõ luật nào.', '<strong>Sau 1 tuần:</strong> đếm số lần phải nhắc mỗi luật. Mang con số vào buổi họp tuần 4.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CDC khuyên cho trẻ nói lại luật bằng lời của mình, nhắc luật thường xuyên và dán bảng luật có hình cho trẻ chưa biết đọc ({CDC}).'),
   lb('Suy luận', 'Cho con góp ý giúp con thấy luật hợp lý hơn, phù hợp với mô hình tiếp nhận giá trị của Grusec &amp; Goodnow 1994.'),
   lb('Đánh giá chuyên môn', 'In dấu tay đồng ý là nghi thức do daynentang.com đề xuất.')]))
])

# =============== TUẦN 4 ===============
lesson('4a', 'Khóa Giá trị nhà mình, bài 4A: bố mẹ thiết kế buổi họp gia đình 15 phút mỗi tuần và chọn một nghi thức gia đình.',
 ['Buổi bố mẹ', 'Tuần 4', '30 phút'], [
 sec(1, 'Mục tiêu', ul(['Bố mẹ chốt <strong>giờ họp cố định</strong> mỗi tuần và 5 phần của buổi họp 15 phút.',
   'Chọn <strong>1 nghi thức gia đình</strong> giữ đều, ví dụ bữa tối chung không màn hình.', 'Chấm phiếu tự đánh giá cuối khóa.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In <a href="{TOOL_M}">Biên bản họp gia đình</a>.', f'Phiếu tự đánh giá trong <a href="{TOOL_V}">Phiếu giá trị</a> (đã chấm ở tuần 1).', 'Số lần nhắc mỗi luật trong tuần 3.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Hỏi nhau: <em>"Ba tuần qua, điều gì trong nhà đã khác đi, dù rất nhỏ?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Giờ họp (3 phút).</strong> Chọn một giờ cố định, ví dụ tối Chủ nhật sau bữa cơm. Ngắn và đều quan trọng hơn dài.',
   '<strong>5 phần (7 phút).</strong> Cảm ơn (3 phút) – Nhìn lại tuần (3 phút) – Một chuyện cần giải quyết (4 phút) – Kế hoạch tuần (3 phút) – Trò vui (2 phút).',
   '<strong>Luật họp (3 phút).</strong> Một người nói, cả nhà nghe. Không chê, không trách. Chuyện khó thì bố mẹ bàn riêng trước. Hết giờ là dừng.',
   '<strong>Chuyện đầu tiên (4 phút).</strong> Chọn một chuyện nhỏ, dễ giải quyết cho buổi họp đầu, ví dụ luật nào phải nhắc nhiều nhất.',
   '<strong>Nghi thức (4 phút).</strong> Chọn 1 việc cả nhà làm đều, ví dụ bữa tối chung không màn hình 3 lần mỗi tuần, hay đi bộ sáng Chủ nhật.',
   '<strong>Đánh giá cuối khóa (4 phút).</strong> Chấm lại phiếu tự đánh giá. So với tuần 1. Ghi 3 dòng vào nhật ký.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Điều gì sẽ làm buổi họp bị bỏ? Làm sao để tránh?', 'Ai giữ giờ? Ai ghi biên bản?', 'Ba tháng nữa, mình muốn xem lại giá trị nào?'])),
 sec(6, 'An toàn và ranh giới', ul(['Buổi họp không phải buổi xử lỗi. Chuyện riêng của một con, bàn riêng với con đó.',
   'Mâu thuẫn vợ chồng lớn không đưa vào họp có con. Nếu xung đột thành bạo lực, gọi 113.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: biên bản họp, phiếu tự đánh giá, 20 phút.', [
   ('Phút 0–8.', 'Mẹ chọn giờ họp và đọc 5 phần.'),
   ('Phút 8–14.', 'Mẹ chọn chuyện đầu tiên và một nghi thức.'),
   ('Phút 14–20.', 'Mẹ chấm phiếu tự đánh giá; gửi ảnh cho bố cùng chấm.')], [
   ('Bố đi công tác vào giờ họp:', 'bố tham gia qua gọi video phần Cảm ơn và Trò vui là đủ.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tuần:</strong> họp đúng giờ, dù chỉ 10 phút.', '<strong>Sau 3 tháng:</strong> mở lại Mái nhà và phiếu giá trị. Có giá trị nào cần đổi khi con lớn hơn?'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Tổng quan 32 công trình: nếp sinh hoạt và nghi thức gia đình gắn với năng lực nuôi dạy, sự thích nghi của trẻ và sự hài lòng trong hôn nhân. Đây là liên hệ, phương pháp đo chưa thống nhất ({FIESE}).'),
   lb('Đã xác nhận', 'Ăn cơm chung từ 3 lần mỗi tuần gắn với ăn uống lành mạnh hơn ở trẻ; đây là tương quan (Hammons &amp; Fiese 2011, <a href="/bang-chung/">xem trang Bằng chứng</a>).'),
   lb('Đánh giá chuyên môn', 'Họp gia đình 15 phút với 5 phần do daynentang.com thiết kế. Chúng tôi chưa tìm thấy thử nghiệm riêng về họp gia đình tại nhà.')]))
])

lesson('4b', 'Khóa Giá trị nhà mình, bài 4B: buổi họp gia đình 15 phút đầu tiên, con lớn làm thư ký, cả nhà hoàn thành Mái nhà giá trị.',
 ['Buổi cả nhà', 'Tuần 4', '15–20 phút'], [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> nói 1 lời cảm ơn, góp 1 ý cho chuyện cần giải quyết, ghi hoặc vẽ biên bản.',
   '<strong>Con nhỏ:</strong> ngồi cùng ít nhất 5 phút, trao "gậy nói chuyện" cho người kế tiếp.', '<strong>Bố mẹ:</strong> giữ đủ 5 phần trong 15 phút.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Biên bản họp đã in (<a href="{TOOL_M}">tải ở đây</a>), bút.', 'Một "gậy nói chuyện": cái thìa gỗ to hoặc cuộn giấy (như bài T7 khóa Gia đình 2–8).', 'Mái nhà giá trị và bảng nội quy trên tường.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Từ hôm nay, mỗi tuần nhà mình có 15 phút họp. Ai cầm gậy thì nói, người khác nghe."</p>'),
 sec(4, 'Hoạt động chính – 15 phút', ol([
   '<strong>Cảm ơn (3 phút).</strong> Mỗi người cầm gậy, cảm ơn một người về một việc cụ thể trong tuần.',
   '<strong>Nhìn lại (3 phút).</strong> Đếm sao trên bảng "Nhà mình đã thấy". Luật nào phải nhắc nhiều nhất?',
   '<strong>Một chuyện (4 phút).</strong> Cả nhà nghĩ cách cho chuyện bố mẹ đã chọn. Con lớn góp 1 ý. Chọn 1 cách để thử cả tuần.',
   '<strong>Kế hoạch (3 phút).</strong> Ai làm gì tuần tới? Nghi thức gia đình là gì? Con lớn ghi hoặc vẽ vào biên bản.',
   '<strong>Vui (2 phút).</strong> Một trò ngắn con chọn: hát một bài, "Bố bảo", hoặc ôm cả nhà.']) +
   '<p><strong>Con nhỏ:</strong> ngồi lòng bố mẹ, cầm gậy và trao cho người kế tiếp. Rời đi chơi gần đó sau 5 phút cũng được.</p>' +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con có thể làm người điều khiển buổi họp, luân phiên với bố mẹ.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Phần nào của buổi họp con thích nhất?', 'Tuần sau con muốn bàn chuyện gì?', 'Mái nhà của mình đã đủ chưa? Còn thiếu gì?'])),
 sec(6, 'An toàn', ul(['Gậy nói chuyện không có cạnh sắc, đủ to để con nhỏ không cho vào miệng.', 'Không phê bình con trước cả nhà. Chuyện riêng bàn riêng.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: gậy nói chuyện, biên bản họp. Tổng 15 phút. Bố gọi video nếu được.', [
   ('Phút 0–3 – Cảm ơn.', 'Mỗi người cầm gậy cảm ơn một người. Bố cảm ơn qua điện thoại.'),
   ('Phút 3–6 – Nhìn lại.', 'Đếm sao trên bảng.'),
   ('Phút 6–10 – Một chuyện.', 'Cả nhà nghĩ cách, chọn 1 cách thử.'),
   ('Phút 10–13 – Kế hoạch.', 'Con lớn ghi biên bản.'),
   ('Phút 13–15 – Vui.', 'Trò con chọn.')], [
   ('Giữ đúng giờ:', 'hết 15 phút là dừng, kể cả khi chưa xong. Để dành tuần sau.'),
   ('Nhắn bố 1 câu:', 'cách cả nhà chọn thử tuần này.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tuần:</strong> họp đúng giờ, giữ biên bản trong một tập hồ sơ.', '<strong>Sau 1 tháng:</strong> đọc lại 4 biên bản cùng con. Nhà mình đã giải quyết được những chuyện gì?'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Making Caring Common khuyên bố mẹ cùng con bàn các câu hỏi về đúng – sai, coi con như "nhà triết học đạo đức" nhỏ ({MCC}).'),
   lb('Đánh giá chuyên môn', 'Buổi họp gia đình 15 phút, thư ký nhí và gậy nói chuyện do daynentang.com thiết kế, chưa có nghiên cứu riêng.'),
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước – sau 4 tuần không có nhóm đối chứng. Đây là thử nghiệm khả thi, không phải bằng chứng hiệu quả.')]))
])

# =============== TRANG KHÓA ===============
def wk(w, a, b, goal):
    return f'<tr><td>{w}</td><td><a href="{link(a)[0]}">{L[a][3]}</a></td><td><a href="{link(b)[0]}">{L[b][3]}</a></td><td>{goal}</td></tr>'
rows = (wk(1, '1a', '1b', 'Có 3–5 giá trị; con lớn nói lại được 2') + wk(2, '2a', '2b', 'Mỗi ngày ≥1 lời khen gắn giá trị') +
        wk(3, '3a', '3b', 'Bảng nội quy ≤5 điều, dán trên tường') + wk(4, '4a', '4b', 'Họp 15 phút đúng giờ'))
page(U, 'Giá trị nhà mình',
 'Khóa 4 tuần miễn phí cho bố mẹ: chọn 3–5 giá trị gia đình, biến thành việc làm, đặt nội quy và họp gia đình 15 phút mỗi tuần.',
f'''
<p class="eyebrow">Gia đình · Khóa G1 · Đang thử nghiệm</p>
<h1>Giá trị nhà mình</h1>
<p class="lead">Bố mẹ cùng chọn những điều nhà mình coi trọng, rồi biến chúng thành việc làm hằng ngày, nội quy rõ ràng và một buổi họp gia đình ngắn mỗi tuần.</p>

<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Gia đình có giá trị rõ ràng, người lớn thống nhất, con biết vì sao nhà mình làm vậy</td></tr>
<tr><th>Dành cho</th><td>Bố mẹ, ông bà, người chăm sóc trẻ từ 2 tuổi. Bài cả nhà có gợi ý cho con 2 tuổi, 7 tuổi và từ 10 tuổi</td></tr>
<tr><th>Thời lượng</th><td>4 tuần. Mỗi tuần 1 buổi bố mẹ (30 phút) và 1 buổi cả nhà (15–20 phút)</td></tr>
<tr><th>Cần có</th><td>Giấy, bút sáp, máy in nếu có. Trẻ không cần màn hình</td></tr>
<tr><th>Tình trạng</th><td>Đủ 4 tuần, bản chưa dạy thử, sẽ sửa theo nhật ký dạy thật</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bố mẹ có 3–5 giá trị viết ra, cả hai cùng đồng ý.</li><li>Mỗi ngày ít nhất 1 lời khen gắn với giá trị.</li><li>Có sẵn câu "Nếu… thì…" cho lúc dễ bực.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: giá trị là để sống theo, không phải để treo tường.</li><li>Kỹ năng: đặt luật rõ, nhất quán, không bạo lực.</li><li>Nếp họp gia đình hằng tuần, dùng được đến khi con lớn.</li></ul></div>
</div>

<h2>Bốn tuần, bốn bước</h2>
{figure_block('KHOAV')}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Buổi bố mẹ (30')</th><th>Buổi cả nhà (15–20')</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="small muted">Nhà đang học khóa <a href="/khoa-hoc/gia-dinh-2-8/">Gia đình 2–8 tuổi</a>? Bốn giá trị của khóa đó (trung thực, biết ơn, tử tế, trách nhiệm) là điểm bắt đầu tốt cho tuần 1.</p>

<h2>Công cụ</h2>
<ul>
<li><a href="{TOOL_V}">Phiếu giá trị</a>: 20 thẻ giá trị, bảng giá trị → việc làm, bảng nội quy, phiếu tự đánh giá.</li>
<li><a href="{TOOL_M}">Biên bản họp gia đình</a>: 5 phần của buổi họp 15 phút, in cho 4 tuần.</li>
</ul>

<h2>Theo dõi tiến bộ</h2>
<p>Chấm phiếu tự đánh giá ở đầu tuần 1 và cuối tuần 4: 0 = chưa có, 1 = có nhưng chưa đều, 2 = đều đặn.
Đếm thêm số lần khen cụ thể và la mắng trong 3 ngày. Đây là cách tự theo dõi, không phải bài kiểm tra.</p>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{CDC}</td><td>2–3 luật một lúc, nói điều cần làm, nhất quán, bảng luật có hình</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn của cơ quan y tế công cộng Hoa Kỳ, không phải thử nghiệm riêng</td></tr>
<tr><td>{GG}</td><td>Con tiếp nhận giá trị khi hiểu đúng và thấy hợp lý</td><td><span class="label">[Đã xác nhận]</span> Bài tổng quan lý thuyết, không phải thử nghiệm</td></tr>
<tr><td>{GOLL}</td><td>Viết sẵn câu "Nếu… thì…"</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp 94 thử nghiệm, d = 0,65; chủ yếu với người lớn tự thay đổi</td></tr>
<tr><td>{FIESE}</td><td>Nếp sinh hoạt và nghi thức gia đình</td><td><span class="label">[Đã xác nhận]</span> Tổng quan 32 công trình; liên hệ, không phải nhân quả</td></tr>
<tr><td>{MCC}</td><td>Bố mẹ xem lại giá trị mình truyền; cho con thực hành quan tâm</td><td><span class="label">[Đã xác nhận]</span> Khảo sát và khuyến nghị chuyên gia</td></tr>
<tr><td>{PLH}</td><td>Khen cụ thể, hậu quả không bạo lực</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên ở Nam Phi (<a href="/bang-chung/">xem trang Bằng chứng</a>)</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Chưa có thử nghiệm nào kiểm tra trọn bộ "chọn giá trị – nội quy – họp gia đình" như khóa này.
  Các phần được ghép từ hướng dẫn và nghiên cứu riêng lẻ. Khóa đang được dạy thử trong một gia đình, không có nhóm so sánh.</p>
</div>

<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai.</p>

<h2>An toàn cho mọi buổi</h2>
<ul>
<li>{NOVIOL}</li>
<li>Bé dưới 3 tuổi: bút, sticker, màu vẽ không để trong tầm với khi người lớn không ngồi cạnh.</li>
<li>Nếu trong nhà có bạo lực, an toàn đến trước mọi bài học. Gọi 113 khi nguy hiểm tức thì.</li>
</ul>
{HELP_BOX}
''', current='/gia-dinh/')

# =============== CÔNG CỤ ===============
VALUES = ['Trung thực', 'Tử tế', 'Biết ơn', 'Trách nhiệm', 'Chăm chỉ', 'Tôn trọng', 'Kiên nhẫn', 'Dũng cảm', 'Tiết kiệm', 'Giúp nhau',
          'Ham học', 'Vui vẻ', 'Khỏe mạnh', 'Gọn gàng', 'Hiếu thảo', 'Công bằng', 'Khiêm tốn', 'Sáng tạo', 'Giữ lời', 'Tha thứ']
cards = ''.join(f'<tr>' + ''.join(f'<td class="tall">☐ {v}</td>' for v in VALUES[i:i+4]) + '</tr>' for i in range(0, 20, 4))
vrows = ''.join('<tr><td class="tall"></td><td></td><td></td></tr>' for _ in range(5))
rrows = ''.join(f'<tr><td class="tall">{i}.</td><td></td><td></td><td></td></tr>' for i in range(1, 6))
SELF = ['Nhà mình có 3–5 giá trị viết ra', 'Bố mẹ (và ông bà) cùng đồng ý các giá trị', 'Con lớn nói lại được ít nhất 2 giá trị',
        'Có nội quy dán ở chỗ dễ thấy', 'Người lớn nhắc luật giống nhau, không la mắng', 'Cả nhà họp hoặc trò chuyện chung mỗi tuần']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)
page(TOOL_V, 'Phiếu giá trị', 'Phiếu in cho khóa Giá trị nhà mình: 20 thẻ giá trị, bảng giá trị thành việc làm, bảng nội quy, phiếu tự đánh giá.',
f'''
<h1>Phiếu giá trị</h1>
<p>Dùng cho khóa <a href="{U}">Giá trị nhà mình</a>. In mỗi người một bản. Dữ liệu chỉ ở trên giấy của bạn.</p>
{PRINT_ROW}
<h2>1. Hai mươi thẻ giá trị (tuần 1)</h2>
<p>Khoanh đúng 5 thẻ. Thiếu giá trị nhà bạn coi trọng thì viết thêm vào dòng trống.</p>
<div class="table-wrap"><table><tbody>{cards}<tr><td class="tall">☐ ……………</td><td>☐ ……………</td><td>☐ ……………</td><td>☐ ……………</td></tr></tbody></table></div>
<h2>2. Giá trị → việc làm (tuần 2)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Giá trị và lời con hiểu</th><th>2 việc con làm</th><th>2 việc bố mẹ làm</th></tr></thead>
<tbody>{vrows}</tbody></table></div>
<p><strong>Nếu… thì…</strong> (3 câu): 1. ……………………………… 2. ……………………………… 3. ………………………………</p>
<h2>3. Nội quy nhà mình (tuần 3)</h2>
<div class="table-wrap"><table>
<thead><tr><th>Luật nói điều cần làm</th><th>Giá trị gốc</th><th>Lời khen</th><th>Hậu quả nhỏ, báo trước</th></tr></thead>
<tbody>{rrows}</tbody></table></div>
<p class="small muted">Con 2–4 tuổi: bắt đầu với 2–3 luật. Không dùng đánh, dọa, hay phạt nhịn ăn.</p>
<h2>4. Phiếu tự đánh giá (đầu tuần 1 và cuối tuần 4)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table>
<thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 4</th></tr></thead>
<tbody>{srows}
<tr><td>Số lần khen cụ thể mỗi ngày (đếm 3 ngày)</td><td></td><td></td></tr>
<tr><td>Số lần la mắng mỗi ngày (đếm 3 ngày)</td><td></td><td></td></tr></tbody></table></div>
<p class="small muted">Phiếu để gia đình tự theo dõi, không dùng để chấm điểm hay so sánh với nhà khác.</p>
''', current='/cong-cu/')

parts = [('Cảm ơn', '3\''), ('Nhìn lại tuần', '3\''), ('Một chuyện cần giải quyết', '4\''), ('Kế hoạch tuần', '3\''), ('Trò vui', '2\'')]
mrows = ''.join(f'<tr><td><strong>{a}</strong> ({m})</td><td class="tall"></td></tr>' for a, m in parts)
one = f'<div class="table-wrap"><table><thead><tr><th class="w38">Ngày họp: ……/……</th><th>Ghi hoặc vẽ</th></tr></thead><tbody>{mrows}</tbody></table></div>'
page(TOOL_M, 'Biên bản họp gia đình', 'Mẫu in biên bản họp gia đình 15 phút: cảm ơn, nhìn lại, một chuyện, kế hoạch, trò vui.',
f'''
<h1>Biên bản họp gia đình</h1>
<p>Dùng cho khóa <a href="{U}">Giá trị nhà mình</a>. Con lớn làm thư ký: ghi hoặc vẽ một dòng cho mỗi phần.</p>
{PRINT_ROW}
<p><strong>Luật họp:</strong> Một người nói, cả nhà nghe · Không chê, không trách · Chuyện khó bố mẹ bàn riêng trước · Hết giờ là dừng.</p>
{one}{one}
<p class="small muted">In nhiều tờ, giữ trong một tập hồ sơ. Sau một tháng, đọc lại cùng con.</p>
''', current='/cong-cu/')
print('G1 built')
