# Khóa G7 "Việc nhà chia đều" – trang khóa, 8 bài, 1 công cụ in
import illus_g7  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/viec-nha-chia-deu/'
TOOL = '/cong-cu/bang-viec-nha/'
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
J_A = journal(['Bố mẹ đã làm được gì', 'Điều gì khó', 'Cần sửa gì'])
J_B = journal(['Con làm được gì', 'Con thích gì', 'Cần sửa gì'])

ILO = '<a href="https://www.ilo.org/resource/news/ilo-calls-urgent-action-prevent-looming-global-care-crisis">ILO 2018</a>'
DAM = '<a href="https://inequality.hks.harvard.edu/publications/cognitive-dimension-household-labor">Daminger 2019, <em>American Sociological Review</em> 84(4)</a>'
AAP = '<a href="https://www.healthychildren.org/English/family-life/family-dynamics/communication-discipline/Pages/Chores-and-Responsibility.aspx">AAP – HealthyChildren.org (cập nhật 2024)</a>'
TEP = '<a href="https://neurosciencenews.com/child-chores-brain-function-20827/">Tepper et al. 2022, <em>Australian Occupational Therapy Journal</em></a>'
WT = '<a href="https://scholars.duke.edu/publication/1458228">Warneken &amp; Tomasello 2008</a>'
CHEM = 'Hóa chất tẩy rửa, nước giặt, dao kéo, nước nóng, ổ điện: người lớn làm, cất trên cao hoặc tủ có khóa, giữ nguyên chai gốc. Lỡ nuốt hóa chất: gọi 115 ngay, mang theo chai.'
SMALL = 'Con dưới 3 tuổi: mọi đồ trong tầm với phải to hơn lõi giấy vệ sinh.'

L = {
 '1a': (1, '1a-nhin-thay-moi-viec', '1A', 'Nhìn thấy mọi việc'),
 '1b': (1, '1b-san-viec-nha', '1B', 'Săn việc nhà'),
 '2a': (2, '2a-chia-lai-cong-bang', '2A', 'Chia lại cho công bằng'),
 '2b': (2, '2b-bang-viec-cua-con', '2B', 'Bảng việc của con'),
 '3a': (3, '3a-day-con-lam-viec-nha', '3A', 'Dạy con làm việc nhà'),
 '3b': (3, '3b-muoi-phut-don-nha', '3B', 'Mười phút dọn nhà'),
 '4a': (4, '4a-xem-lai-phan-cong', '4A', 'Xem lại phân công'),
 '4b': (4, '4b-ngay-cam-on-viec-nha', '4B', 'Ngày cảm ơn việc nhà'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, meta, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'g7-' + k
    note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này đã soạn theo khung của khóa nhưng chưa được dạy thử trong gia đình. '
            f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về bài {code}</a></p></div>')
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Việc nhà chia đều</a> · Tuần {w} · {code}</p>
<h1>{title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block('H' + code)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/gia-dinh/')

def ma(w): return ['Buổi bố mẹ', f'Tuần {w}', '30 phút']
def mb(w): return ['Buổi cả nhà', f'Tuần {w}', '15–20 phút']

# =============== TUẦN 1 ===============
lesson('1a', 'Khóa Việc nhà chia đều, bài 1A: bố mẹ liệt kê mọi việc nhà, cả phần làm và phần nghĩ, và ước số giờ mỗi người đang làm.', ma(1), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ có <strong>danh sách đầy đủ việc nhà</strong>, gồm cả việc hằng ngày, hằng tuần, hằng tháng.',
   'Mỗi việc ghi <strong>ai đang lo</strong> phần làm và phần nghĩ. Mỗi người ước <strong>số giờ mỗi tuần</strong>.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In trang 1 của <a href="{TOOL}">Bảng việc nhà</a>, hoặc dùng giấy to.', 'Hai cây bút khác màu, mỗi người một màu.', 'Giờ yên tĩnh, con đã ngủ.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người đoán thầm: <em>"Mỗi tuần mình làm việc nhà bao nhiêu giờ? Người kia bao nhiêu giờ?"</em> Ghi ra giấy, chưa đọc.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Liệt kê (10 phút).</strong> Viết mọi việc theo nhóm: bếp, giặt, dọn, con cái, đi chợ, tiền nong, sửa chữa, họ hàng. Đừng quên việc ít ai thấy: nhớ lịch tiêm, mua quà sinh nhật, hỏi thăm ông bà.',
   '<strong>Phần làm và phần nghĩ (6 phút).</strong> Mỗi việc có phần nghĩ: nhận ra việc cần, nghĩ cách, chọn cách, theo dõi. Đánh dấu ai đang lo phần nghĩ.',
   '<strong>Ai đang lo (5 phút).</strong> Mỗi người tô màu của mình vào việc mình đang lo. Việc làm chung thì tô cả hai màu.',
   '<strong>Ước giờ (4 phút).</strong> Mỗi người ước số giờ mỗi tuần. So với số đoán lúc đầu. Chưa chia lại; tuần 2 mới chia.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Việc nào mình chưa từng biết là người kia đang làm?', 'Việc nào làm mình mệt nhất, kể cả khi mất ít thời gian?', 'Hồi nhỏ, nhà mình chia việc thế nào? Mình muốn giữ hay đổi điều gì?'])),
 sec(6, 'An toàn và ranh giới', ul(['Buổi này để nhìn thấy, không để tính sổ. Nếu bắt đầu trách nhau, dừng lại, hẹn hôm khác.',
   'Nếu bất đồng thành lời lẽ xúc phạm hay bạo lực, an toàn đến trước. Nguy hiểm tức thì gọi 113.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: danh sách việc nhà, 20 phút. Bố bổ sung qua tin nhắn.', [
   ('Phút 0–12.', 'Mẹ liệt kê việc theo nhóm và tô màu việc mẹ lo.'),
   ('Phút 12–20.', 'Chụp gửi bố. Bố tô việc bố lo, thêm việc mẹ chưa ghi.')], [
   ('Khi bố đi công tác dài ngày:', 'ghi riêng những việc chuyển hết sang mẹ trong thời gian đó. Tuần 2 sẽ tính đến.')])),
 sec(8, 'Ôn lại', ul(['<strong>Trong tuần:</strong> mỗi người ghi thêm việc phát hiện ra mà danh sách còn thiếu.', '<strong>Sau 1 tuần:</strong> mang danh sách vào buổi 2A.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Trên thế giới, phụ nữ làm 76,2% tổng số giờ việc chăm sóc không lương, gấp hơn 3 lần nam giới ({ILO}).'),
   lb('Đã xác nhận', f'Nghiên cứu phỏng vấn 35 cặp vợ chồng: "việc nghĩ" trong nhà gồm dự đoán nhu cầu, nghĩ cách, quyết định, theo dõi; phụ nữ làm nhiều hơn phần dự đoán và theo dõi ({DAM}).'),
   lb('Suy luận', 'Hai số liệu trên là chung, không nói về gia đình bạn. Danh sách của chính nhà bạn mới là dữ liệu đúng nhất.')]))
])

lesson('1b', 'Khóa Việc nhà chia đều, bài 1B: con đi "săn việc nhà", kể ra những việc mỗi người đã làm cho cả nhà.', mb(1), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn (khoảng 7 tuổi):</strong> kể được ít nhất 8 việc nhà và ai đã làm.',
   '<strong>Con nhỏ (khoảng 2 tuổi):</strong> bỏ áo bẩn vào giỏ hoặc mang dép về rổ cùng người lớn.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Một "kính lúp" bằng bìa.', 'Một tờ giấy chia cột: Bố, Mẹ, Con lớn, Con nhỏ, Người khác (ông bà, cô giúp việc).', 'Giỏ đựng áo bẩn.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Nhà mình sạch, có cơm ăn, có áo mặc. Ai làm những việc đó? Hôm nay con làm thám tử đi tìm."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Con cầm kính lúp đi quanh nhà: bếp, phòng tắm, chỗ phơi đồ, bàn học.',
   'Thấy dấu hiệu của một việc, con hỏi: "Ai đã làm việc này?" Ghi hoặc vẽ vào cột người đó.',
   'Đếm số việc mỗi cột. Hỏi: "Cột nào nhiều nhất? Con nghĩ gì?"',
   'Con chọn 1 việc nhỏ muốn giúp tuần này. Tuần 2 sẽ đưa vào bảng việc của con.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Bố mẹ làm mẫu bỏ một chiếc áo vào giỏ.', 'Mời con bỏ 2 chiếc. Con làm xong, cả nhà vỗ tay.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con ước thời gian cho mỗi việc và cộng giờ mỗi cột.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Việc nào con chưa biết ai làm?', 'Nếu không ai làm việc đó một tuần, nhà mình sẽ ra sao?', 'Con muốn giúp việc nào?'])),
 sec(6, 'An toàn', ul([CHEM, SMALL])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: kính lúp bìa, tờ giấy chia cột, giỏ áo. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', '"Ai làm những việc này?"'), ('Phút 2–10 – Săn việc.', 'Con lớn đi tìm, ghi vào cột.'),
   ('Phút 10–13 – Con nhỏ.', 'Bỏ áo vào giỏ.'), ('Phút 13–15 – Đếm.', 'Con chọn 1 việc muốn giúp.')], [
   ('Cột của bố khi bố đi vắng:', 'ghi những việc bố làm lúc ở nhà, để con thấy bố cũng góp phần.'),
   ('Nhắn bố 1 câu:', 'việc con chọn giúp.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tối:</strong> con kể 1 việc nhà con thấy ai đó làm hôm nay.', '<strong>Sau 1 tuần:</strong> con đã giúp việc mình chọn mấy lần?'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'AAP: hầu hết trẻ tuổi mẫu giáo có thể bắt đầu góp tay vào việc nhà đơn giản; việc nhà dạy tinh thần đồng đội và kỹ năng sống ({AAP}).'),
   lb('Đánh giá chuyên môn', 'Trò "săn việc nhà" do daynentang.com thiết kế.')]))
])

# =============== TUẦN 2 ===============
lesson('2a', 'Khóa Việc nhà chia đều, bài 2A: bố mẹ chia lại việc theo "người lo trọn" và tính công bằng theo tổng công sức, không phải chia đôi.', ma(2), [
 sec(1, 'Mục tiêu', ul(['Mỗi việc có <strong>một người lo trọn</strong>: từ nhận ra đến theo dõi.',
   'Bố mẹ có bảng <strong>"Ai lo việc gì"</strong> cả hai thấy hợp lý, kèm <strong>kế hoạch khi một người đi vắng</strong>.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Danh sách việc từ bài 1A.', f'Trang 2 của <a href="{TOOL}">Bảng việc nhà</a>.', 'Lịch đi làm, đi công tác của cả hai.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nói: <em>"Việc mình muốn bỏ nhất là…"</em> và <em>"Việc mình không ngại làm là…"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Công bằng là gì (4 phút).</strong> Công bằng không phải mỗi người một nửa số việc. Tính cả giờ đi làm, đường xa, sức khỏe, tuần đi công tác.',
   '<strong>Người lo trọn (8 phút).</strong> Với mỗi việc, chọn một người lo trọn 5 bước: nhận ra, nghĩ, chọn, làm, theo dõi. Người kia có thể giúp làm, nhưng không phải nhắc.',
   '<strong>Chia lại (6 phút).</strong> Ưu tiên chuyển phần nghĩ. Ví dụ bố lo trọn "giặt đồ": tự nhận ra giỏ đầy, tự giặt, tự phơi, tự cất.',
   '<strong>Kế hoạch đi vắng (4 phút).</strong> Khi một người đi công tác: việc nào tạm bỏ, việc nào làm đơn giản, việc nào nhờ ông bà hay người ngoài.',
   '<strong>Ghi và dán (3 phút).</strong> Điền bảng "Ai lo việc gì". Dán ở chỗ hai người cùng thấy.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Khi người lo trọn làm khác cách mình, mình có chịu được không?', 'Việc nào nên làm đơn giản hơn thay vì chia?', 'Mình sẽ nói gì khi thấy người kia quên?'])),
 sec(6, 'An toàn và ranh giới', ul(['Không giao trẻ việc nguy hiểm để bớt việc người lớn: nấu bếp lửa, dùng hóa chất, trông em một mình.',
   'Người lo trọn có quyền làm theo cách của mình, miễn là an toàn và xong việc.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: danh sách việc, 20 phút. Chốt cuối cần có bố.', [
   ('Phút 0–10.', 'Mẹ đánh dấu việc muốn chuyển và việc nhờ được người khác.'),
   ('Phút 10–20.', 'Gọi video với bố: chọn người lo trọn cho từng việc, nhất là việc bố làm được từ xa (đặt hàng, đóng tiền điện, gọi thợ).')], [
   ('Việc bố làm được khi đi công tác:', 'nhiều việc nghĩ làm từ xa được: đặt lịch, trả hóa đơn, nhắc lịch tiêm, gọi hỏi thăm ông bà.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tối:</strong> người lo trọn tự kiểm việc của mình, không cần nhắc.', '<strong>Sau 1 tuần:</strong> việc nào đã chạy, việc nào bị quên?'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Suy luận', f'Chia theo "người lo trọn" là cách chúng tôi áp dụng phát hiện của {DAM}: phần dự đoán và theo dõi dễ bị dồn cho một người.'),
   lb('Đánh giá chuyên môn', 'Định nghĩa "công bằng theo tổng công sức" do daynentang.com đề xuất; chưa có thử nghiệm riêng.')]))
])

lesson('2b', 'Khóa Việc nhà chia đều, bài 2B: con chọn việc của mình theo tuổi, học việc qua bốn bước và tự đánh dấu bảng việc.', mb(2), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> nhận 2 việc hằng ngày và tự đánh dấu bảng ít nhất 5/7 ngày.',
   '<strong>Con nhỏ:</strong> làm 1 việc nhỏ hằng ngày cùng người lớn (cất dép, bỏ áo vào giỏ).'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Bảng việc của con (trang 3 của <a href="{TOOL}">Bảng việc nhà</a>).', 'Danh sách việc theo tuổi bên dưới.', 'Bút sáp, sticker hoặc tự vẽ sao.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Nhà mình là một đội. Ai trong đội cũng có việc. Hôm nay con chọn việc của con."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Gợi ý việc theo tuổi</h3>' +
   '<div class="table-wrap"><table><thead><tr><th>Tuổi</th><th>Việc gợi ý</th></tr></thead><tbody>'
   '<tr><td>2–4 tuổi</td><td>Cất đồ chơi vào rổ, bỏ áo bẩn vào giỏ, mang dép về rổ, lau chỗ đổ bằng khăn (cùng người lớn)</td></tr>'
   '<tr><td>5–7 tuổi</td><td>Dọn giường, bày và dọn bàn ăn, cất đồ chơi, tưới cây, phân loại quần áo, đổ sọt rác nhỏ</td></tr>'
   '<tr><td>8–10 tuổi</td><td>Thêm: quét nhà, phụ nấu ăn, tự làm bữa phụ đơn giản, cất đồ đi chợ, cất quần áo của mình</td></tr>'
   '<tr><td>11–12 tuổi</td><td>Thêm: dọn bếp, thay ga giường, giặt và gấp đồ, nấu món đơn giản khi có người lớn</td></tr>'
   '</tbody></table></div>' +
   '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Con chọn 2 việc từ danh sách và từ việc con muốn giúp ở bài 1B.',
   'Dạy việc bằng 4 bước: bố mẹ làm, con xem → cùng làm → con làm, bố mẹ xem → con tự làm. Hôm nay làm bước 1 và 2.',
   'Con viết hoặc vẽ việc vào bảng. Mỗi ngày làm xong, con tự vẽ sao.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Chọn 1 việc cho con: mang dép về rổ.', 'Hát "Dép về nhà" và làm cùng con. Dán hình chiếc dép lên bảng.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con nhận lo trọn một việc, ví dụ phơi và cất đồ của mình.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Việc nào con thấy dễ? Việc nào con muốn học?', 'Nếu con quên việc của mình, ai bị ảnh hưởng?', 'Con muốn đổi việc sau bao lâu?'])),
 sec(6, 'An toàn', ul([CHEM, 'Con dưới 12 tuổi không trông em một mình. Phụ nấu ăn chỉ khi có người lớn bên cạnh, tránh bếp lửa và dao sắc.', SMALL])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: bảng việc, bút sáp. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', '"Nhà mình là một đội."'), ('Phút 2–8 – Chọn việc.', 'Con lớn chọn 2 việc; con nhỏ 1 việc.'),
   ('Phút 8–13 – Làm thử.', 'Mẹ làm mẫu và làm cùng con.'), ('Phút 13–15 – Dán bảng.', 'Dán ở chỗ con thấy.')], [
   ('Nhắn bố 1 câu:', '2 việc con chọn. Bố khen con qua video.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> con tự vẽ sao khi làm xong.', '<strong>Sau 1 tuần:</strong> đếm sao, chuyển sang bước "con làm, bố mẹ xem".'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Danh sách việc theo tuổi 5–12 dựa trên gợi ý của {AAP}. AAP khuyên dùng bảng việc, thêm từng việc một với trẻ mới bắt đầu, khen cố gắng hơn kết quả.'),
   lb('Đánh giá chuyên môn', 'Gợi ý cho tuổi 2–4 và cách dạy 4 bước do daynentang.com soạn; AAP không đưa danh sách riêng cho tuổi này.'),
   lb('Đã xác nhận', f'Khảo sát 207 phụ huynh có con 5–13 tuổi: việc tự chăm sóc và chăm sóc gia đình gắn với trí nhớ làm việc và khả năng kiềm chế tốt hơn. Đây là tương quan, không phải nhân quả ({TEP}).')]))
])

# =============== TUẦN 3 ===============
lesson('3a', 'Khóa Việc nhà chia đều, bài 3A: bố mẹ thống nhất cách dạy con làm việc nhà: chấp nhận chưa hoàn hảo, khen cụ thể, không trả tiền cho việc chung.', ma(3), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ thống nhất <strong>3 câu nói mẫu</strong> khi con làm chưa khéo, khi con quên, khi con làm tốt.',
   'Thống nhất <strong>việc chung không trả tiền</strong>, và cách xử lý việc thêm.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Bảng việc của con sau 1 tuần.', 'Nhớ lại 1 lần con làm chưa khéo và mình đã phản ứng thế nào.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Hỏi nhau: <em>"Tuần qua, có lúc nào mình làm lại việc con vừa làm không? Con thấy thế nào?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Chưa khéo là bình thường (5 phút).</strong> Con 7 tuổi gấp áo chưa thẳng. Không làm lại trước mặt con. Khen phần làm được, chỉ thêm một bước.',
   '<strong>Ba câu nói mẫu (8 phút).</strong> Viết ra và tập nói. Chưa khéo: "Con gấp được rồi. Thử vuốt thẳng góc này nhé." Quên: "Việc của con là gì nhỉ?" Làm tốt: "Con tự dọn bàn không cần nhắc. Cả nhà nhẹ hơn nhiều."',
   '<strong>Việc nhà và tiền (6 phút).</strong> Gợi ý: việc chung không trả tiền, vì là phần của mỗi người trong đội. Việc thêm ngoài phần của con thì mỗi nhà tự quyết. Nếu nhà học khóa Tiền nhà mình, tiền đó vào hũ ba ngăn.',
   '<strong>Khi con không làm (6 phút).</strong> Chọn một hậu quả nhỏ, báo trước, liên quan. Ví dụ: đồ chơi chưa cất thì nghỉ chơi món đó đến tối. Không la mắng, không đánh.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Mình có đang làm mẫu việc nhà trước mặt con không?', 'Ai hay làm lại việc của con nhất? Vì sao?', 'Khi con làm, mình có đủ kiên nhẫn chờ không?'])),
 sec(6, 'An toàn và ranh giới', ul(['Không dùng việc nhà làm hình phạt kéo dài hay làm con xấu hổ.', 'Không đánh, không dọa. Đánh đòn gây hại cho trẻ và không có lợi ích nào (<a href="https://www.who.int/news-room/fact-sheets/detail/corporal-punishment-and-health">WHO</a>).'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 15 phút, một tờ giấy.', [
   ('Phút 0–8.', 'Mẹ viết 3 câu nói mẫu.'), ('Phút 8–15.', 'Gửi bố, bố dùng đúng 3 câu khi gọi video và khi về nhà.')], [
   ('Ông bà cùng chăm con:', 'đưa ông bà xem 3 câu, nhờ ông bà để con tự làm thay vì làm hộ.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> dùng ít nhất 1 câu nói mẫu.', '<strong>Sau 1 tuần:</strong> mình đã làm lại việc của con mấy lần? Ít hơn tuần trước chưa?'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'AAP khuyên khen cố gắng trong từng việc, không chỉ khen kết quả; lời khen và động viên hiệu quả hơn phần thưởng vật chất ({AAP}).'),
   lb('Đã xác nhận', f'Thí nghiệm với trẻ 20 tháng: trẻ được thưởng vật chất khi giúp người khác thì về sau giúp ít hơn ({WT}).'),
   lb('Đánh giá chuyên môn', 'AAP nêu phụ cấp gắn với việc nhà là một lựa chọn; bằng chứng về trả tiền cho việc nhà chưa rõ. Gợi ý "việc chung không trả tiền" là lựa chọn của daynentang.com.')]))
])

lesson('3b', 'Khóa Việc nhà chia đều, bài 3B: cả nhà dọn nhà 10 phút theo nhạc, mỗi người một khu hợp sức mình.', mb(3), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> dọn xong khu của mình trong 10 phút, tự kiểm theo danh sách 3 điểm.',
   '<strong>Con nhỏ:</strong> cất ít nhất 5 món về đúng chỗ cùng người lớn.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Đồng hồ hẹn giờ hoặc 2–3 bài hát vui (khoảng 10 phút).', 'Chia nhà thành khu: phòng khách, bếp, góc đồ chơi, rổ dép.', 'Mỗi khu một thẻ 3 điểm kiểm, ví dụ: sàn không có đồ, đồ chơi trong rổ, dép xếp đôi.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Thử thách: dọn nhà xong trước khi hết nhạc! Mỗi người một khu."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Cả nhà (10 phút dọn + 5 phút kiểm)</h3>' + ol([
   'Mỗi người nhận một khu. Con lớn nhận góc đồ chơi; con nhỏ nhận rổ dép cùng một người lớn.',
   'Bật nhạc, cả nhà cùng dọn. Người lớn không làm hộ khu của con.',
   'Hết nhạc: mỗi người tự kiểm 3 điểm của khu mình.',
   'Đi tham quan khu của nhau và cảm ơn: "Cảm ơn con, góc đồ chơi gọn quá."',
   'Chọn giờ "10 phút dọn nhà" cố định, ví dụ trước bữa tối.']) +
   '<p><strong>Con nhỏ:</strong> cầm dép đặt vào rổ, cất bóng vào thùng. Làm 5 phút rồi chơi gần đó cũng được.</p>' +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con tự viết thẻ 3 điểm kiểm cho khu của mình.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Dọn với nhạc có khác dọn một mình không?', 'Khu nào khó nhất? Lần sau làm sao cho nhanh hơn?', 'Con muốn đổi khu vào tuần sau không?'])),
 sec(6, 'An toàn', ul([CHEM, 'Không cho con nhỏ cầm túi nilon, đồ thủy tinh, đồ sắc khi dọn.', SMALL])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: điện thoại phát nhạc, 3 thẻ khu. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Thử thách dọn nhà theo nhạc.'), ('Phút 2–12 – Dọn.', 'Con lớn góc đồ chơi; mẹ và con nhỏ rổ dép rồi bếp.'),
   ('Phút 12–15 – Kiểm và cảm ơn.', 'Tham quan khu của nhau.')], [
   ('Ngày mẹ quá mệt:', 'rút còn 5 phút, chỉ một khu. Giữ nếp quan trọng hơn dọn sạch.'),
   ('Nhắn bố 1 câu:', 'khu nào con dọn đẹp nhất.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> 10 phút dọn nhà đúng giờ đã chọn.', '<strong>Sau 1 tuần:</strong> đổi khu cho nhau một lần.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'AAP khuyên giữ việc nhà theo lịch đều, gắn với các nếp khác như bữa ăn, giờ ngủ ({AAP}).'),
   lb('Đánh giá chuyên môn', '"Mười phút dọn nhà theo nhạc" và thẻ 3 điểm kiểm do daynentang.com thiết kế.')]))
])

# =============== TUẦN 4 ===============
lesson('4a', 'Khóa Việc nhà chia đều, bài 4A: bố mẹ xem lại phân công sau 3 tuần, xử lý khi một người quá tải và chấm phiếu cuối khóa.', ma(4), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ xem lại bảng "Ai lo việc gì" và <strong>đổi ít nhất 1 việc</strong> chưa chạy.', 'Có <strong>4 câu hỏi</strong> dùng khi một người quá tải. Chấm phiếu tự đánh giá cuối khóa.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Bảng "Ai lo việc gì" và bảng việc của con.', f'Phiếu tự đánh giá trong <a href="{TOOL}">Bảng việc nhà</a>.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người cảm ơn người kia về một việc người đó đã lo trọn trong 3 tuần qua.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Việc nào chạy, việc nào không (6 phút).</strong> Đánh dấu xanh việc đã chạy đều, đỏ việc bị quên.',
   '<strong>Quá tải (8 phút).</strong> Ai thấy mệt nhất? Hỏi theo thứ tự: Việc nào bỏ được? Làm đơn giản hơn được? Chuyển cho người khác được? Nhờ ngoài được?',
   '<strong>Đổi một việc (4 phút).</strong> Chọn 1 việc đỏ, đổi người lo trọn hoặc đổi cách làm.',
   '<strong>Việc của con (3 phút).</strong> Việc nào con đã tự làm được? Thêm 1 việc mới nếu con sẵn sàng.',
   '<strong>Đánh giá cuối khóa (4 phút).</strong> Chấm phiếu tự đánh giá, so với tuần 1. Hẹn xem lại mỗi tháng, có thể trong buổi họp gia đình.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Phần nghĩ đã được chia lại chưa, hay vẫn dồn về một người?', 'Tháng tới có tuần nào đặc biệt bận (công tác, thi cử, Tết)?', 'Mình muốn con lớn lên nghĩ gì về việc nhà?'])),
 sec(6, 'An toàn và ranh giới', ul(['Quá tải kéo dài gây mệt mỏi, cáu gắt. Nếu một người mất ngủ, buồn chán nhiều tuần, hãy tìm hỗ trợ. Xem khối "Cần giúp ngay".'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: các bảng, 20 phút. Bố gọi video.', [
   ('Phút 0–10.', 'Mẹ đánh dấu xanh, đỏ trên bảng.'), ('Phút 10–20.', 'Gọi video với bố: 4 câu hỏi quá tải, đổi 1 việc, chấm phiếu.')], [])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> 10 phút xem lại phân công.', '<strong>Sau 3 tháng:</strong> chấm lại phiếu tự đánh giá.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'AAP khuyên họp gia đình đều đặn để xem lại tiến bộ và cập nhật việc nhà ({AAP}).'),
   lb('Đánh giá chuyên môn', 'Bốn câu hỏi khi quá tải và vòng xem lại hằng tháng do daynentang.com thiết kế.'),
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước – sau 4 tuần không có nhóm đối chứng; đây là thử nghiệm khả thi, không phải bằng chứng hiệu quả.')]))
])

lesson('4b', 'Khóa Việc nhà chia đều, bài 4B: cả nhà làm thẻ cảm ơn cho việc nhà của nhau và dán bảng "Ai lo việc gì".', mb(4), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> viết hoặc vẽ ít nhất 2 thẻ cảm ơn cụ thể; nói lại 2 việc của mình.',
   '<strong>Con nhỏ:</strong> trao thẻ cảm ơn cho một người.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Giấy màu cắt thành thẻ, bút sáp.', 'Bảng "Ai lo việc gì" đã chốt ở bài 4A.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Bốn tuần qua, ai trong nhà đã làm một việc làm con thấy nhẹ nhõm?"</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Mỗi người làm thẻ cảm ơn cho 2 người, ghi rõ việc: "Cảm ơn mẹ nấu canh chua."',
   'Lần lượt trao thẻ và đọc to.',
   'Bố mẹ giới thiệu bảng "Ai lo việc gì" mới. Con tìm tên và việc của mình.',
   'Dán bảng và thẻ cảm ơn cạnh nhau. Nếu nhà có họp gia đình, đưa phần này vào mục Cảm ơn mỗi tuần.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Con tô thẻ cùng anh.', 'Con trao thẻ cho bố hoặc mẹ, cả nhà ôm nhau.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con đề xuất một việc mới con muốn lo trọn.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Nhận thẻ cảm ơn, con thấy thế nào?', 'Việc nào con tự hào đã làm được?', 'Tháng tới con muốn học việc gì mới?'])),
 sec(6, 'An toàn', ul(['Kéo cắt giấy: người lớn cắt sẵn hoặc dùng kéo đầu tròn cho con lớn.', SMALL])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: giấy màu, bút sáp, bảng phân công. Tổng 15 phút.', [
   ('Phút 0–8 – Làm thẻ.', 'Mỗi người làm 2 thẻ; một thẻ dành cho bố.'), ('Phút 8–12 – Trao thẻ.', 'Đọc to; thẻ của bố chụp ảnh gửi.'),
   ('Phút 12–15 – Dán bảng.', 'Con tìm việc của mình trên bảng.')], [('Nhắn bố 1 câu:', 'thẻ cảm ơn con làm cho bố.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tuần:</strong> mỗi người cảm ơn 1 việc nhà cụ thể.', '<strong>Mỗi tháng:</strong> xem lại bảng cùng con.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Thẻ cảm ơn việc nhà do daynentang.com thiết kế, nối với bài G2 "Ba điều cảm ơn" (khóa Gia đình 2–8) và phần Cảm ơn trong buổi họp gia đình (khóa Giá trị nhà mình).')]))
])

# =============== TRANG KHÓA ===============
def wk(w, a, b, goal):
    return f'<tr><td>{w}</td><td><a href="{link(a)[0]}">{L[a][3]}</a></td><td><a href="{link(b)[0]}">{L[b][3]}</a></td><td>{goal}</td></tr>'
rows = (wk(1, '1a', '1b', 'Danh sách việc đủ, có cả phần nghĩ') + wk(2, '2a', '2b', 'Mỗi việc một người lo trọn; con có 2 việc') +
        wk(3, '3a', '3b', 'Dọn nhà 10 phút ≥5/7 ngày') + wk(4, '4a', '4b', 'Đổi 1 việc chưa chạy; chấm phiếu cuối khóa'))
page(U, 'Việc nhà chia đều',
 'Khóa 4 tuần miễn phí cho bố mẹ: nhìn thấy mọi việc nhà, chia lại cho công bằng, dạy con làm việc theo tuổi và giữ nếp đều.',
f'''
<p class="eyebrow">Gia đình · Khóa G7 · Đang thử nghiệm</p>
<h1>Việc nhà chia đều</h1>
<p class="lead">Mọi người trong nhà đều thấy hết các việc, kể cả việc phải nhớ và lo. Việc được chia công bằng, con có phần việc hợp tuổi, và cả nhà biết cảm ơn nhau.</p>

<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bớt một người quá tải, bớt cãi nhau vì việc nhà, con thành thành viên có trách nhiệm</td></tr>
<tr><th>Dành cho</th><td>Vợ chồng, ông bà, người chăm sóc trẻ từ 2 tuổi. Bài cả nhà có gợi ý cho con 2 tuổi, 7 tuổi và từ 10 tuổi</td></tr>
<tr><th>Thời lượng</th><td>4 tuần. Mỗi tuần 1 buổi bố mẹ (30 phút) và 1 buổi cả nhà (15–20 phút)</td></tr>
<tr><th>Cần có</th><td>Giấy, bút hai màu, nhạc vui. Trẻ không cần màn hình</td></tr>
<tr><th>Tình trạng</th><td>Đủ 4 tuần, bản chưa dạy thử, sẽ sửa theo nhật ký dạy thật</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Cả hai thấy đủ danh sách việc nhà, kể cả phần nghĩ.</li><li>Mỗi việc có một người lo trọn, không phải nhắc.</li><li>Con có 2 việc hằng ngày và tự đánh dấu.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: nhà là một đội, công bằng theo tổng công sức.</li><li>Kỹ năng: dạy việc 4 bước, nói chuyện khi quá tải.</li><li>Nếp dọn nhà 10 phút và xem lại phân công mỗi tháng.</li></ul></div>
</div>

<h2>Bốn tuần, bốn bước</h2>
{figure_block('KHOAH')}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Buổi bố mẹ (30')</th><th>Buổi cả nhà (15–20')</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Bảng việc nhà</a>: danh sách việc có phần nghĩ, bảng "Ai lo việc gì", bảng việc của con 7 ngày, phiếu tự đánh giá.</li></ul>

<h2>Theo dõi tiến bộ</h2>
<p>Chấm phiếu tự đánh giá ở đầu tuần 1 và cuối tuần 4: 0 = chưa có, 1 = có nhưng chưa đều, 2 = đều đặn.</p>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{AAP}</td><td>Việc theo tuổi, bảng việc, thêm từng việc, khen cố gắng, họp gia đình</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn của Viện Nhi khoa Hoa Kỳ cho phụ huynh</td></tr>
<tr><td>{DAM}</td><td>Phần nghĩ của việc nhà: dự đoán, nghĩ cách, quyết định, theo dõi</td><td><span class="label">[Đã xác nhận]</span> Nghiên cứu định tính, 35 cặp vợ chồng ở Mỹ</td></tr>
<tr><td>{ILO}</td><td>Việc chăm sóc không lương thường dồn cho phụ nữ</td><td><span class="label">[Đã xác nhận]</span> Báo cáo thống kê toàn cầu</td></tr>
<tr><td>{TEP}</td><td>Việc nhà và chức năng điều hành của trẻ</td><td><span class="label">[Đã xác nhận]</span> Khảo sát 207 phụ huynh; tương quan</td></tr>
<tr><td>{WT}</td><td>Không thưởng vật chất cho việc giúp đỡ</td><td><span class="label">[Đã xác nhận]</span> Thí nghiệm với trẻ 20 tháng</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Chưa có thử nghiệm nào kiểm tra trọn bộ cách chia việc như khóa này. Các phần được ghép từ hướng dẫn và nghiên cứu riêng lẻ, phần lớn ở nước khác.
  Khóa đang được dạy thử trong một gia đình, không có nhóm so sánh.</p>
</div>

<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai.</p>

<h2>An toàn cho mọi buổi</h2>
<ul><li>{CHEM}</li><li>{SMALL}</li><li>Trẻ dưới 12 tuổi không trông em một mình, không đứng bếp lửa một mình.</li></ul>
{HELP_BOX}
''', current='/gia-dinh/')

# =============== CÔNG CỤ ===============
GROUPS = ['Bếp, nấu ăn', 'Giặt, phơi, cất đồ', 'Dọn dẹp, lau rửa', 'Con cái (đưa đón, học, sức khỏe)', 'Đi chợ, mua sắm', 'Tiền nong, hóa đơn', 'Sửa chữa, bảo trì', 'Họ hàng, hiếu hỉ']
grows = ''.join(f'<tr><td class="tall"><strong>{g}</strong></td><td></td><td></td><td></td></tr>' for g in GROUPS)
blank = ''.join('<tr><td class="tall"></td><td></td><td></td><td></td></tr>' for _ in range(8))
days = ''.join(f'<th>{d}</th>' for d in ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN'])
krows = ''.join(f'<tr><td class="tall">{i}. ……………</td>' + '<td></td>' * 7 + '</tr>' for i in range(1, 4))
SELF = ['Cả hai thấy đủ danh sách việc nhà', 'Phần nghĩ được chia, không dồn một người', 'Mỗi việc có một người lo trọn',
        'Có kế hoạch khi một người đi vắng', 'Con có việc hằng ngày hợp tuổi', 'Không làm lại việc của con trước mặt con', 'Dọn nhà 10 phút đều đặn', 'Cảm ơn việc nhà của nhau']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)
page(TOOL, 'Bảng việc nhà', 'Bảng in cho khóa Việc nhà chia đều: danh sách việc có phần nghĩ, bảng Ai lo việc gì, bảng việc của con, phiếu tự đánh giá.',
f'''
<h1>Bảng việc nhà</h1>
<p>Dùng cho khóa <a href="{U}">Việc nhà chia đều</a>. Chỉ để in, trang không lưu dữ liệu của bạn.</p>
{PRINT_ROW}
<h2>1. Danh sách việc nhà (tuần 1)</h2>
<p>Viết từng việc dưới mỗi nhóm. Cột "Phần nghĩ": ai nhận ra, lên kế hoạch, theo dõi việc đó.</p>
<div class="table-wrap"><table><thead><tr><th>Nhóm / việc</th><th>Ai làm</th><th>Phần nghĩ: ai lo</th><th>Giờ mỗi tuần</th></tr></thead><tbody>{grows}{blank}</tbody></table></div>
<h2>2. Ai lo việc gì (tuần 2)</h2>
<div class="table-wrap"><table><thead><tr><th>Việc</th><th>Người lo trọn</th><th>Người giúp</th><th>Khi người lo trọn đi vắng</th></tr></thead><tbody>{blank}</tbody></table></div>
<h2>3. Bảng việc của con (tuần 2)</h2>
<p>Con viết hoặc vẽ việc của mình. Làm xong ngày nào, con tự vẽ sao ngày đó.</p>
<div class="table-wrap"><table><thead><tr><th>Việc của con</th>{days}</tr></thead><tbody>{krows}</tbody></table></div>
<h2>4. Phiếu tự đánh giá (tuần 1 và tuần 4)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 4</th></tr></thead><tbody>{srows}</tbody></table></div>
<p class="small muted">Phiếu để gia đình tự theo dõi, không dùng để chấm điểm nhau.</p>
''', current='/cong-cu/')
print('G7 built')
