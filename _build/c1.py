# Khóa C1 "Lớn lên an toàn (10–14)" – trang khóa + bài 1 (các bài 2–8 đang soạn)
# Người đọc chính là trẻ 10–14 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c1  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/lon-len-an-toan/'
G4 = '/khoa-hoc/gia-dinh-10-14/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
def sec(n, title, body): return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'

KH = '<a href="https://kidshealth.org/NortonChildrens/en/parents/understanding-puberty.html?view=ptr">Nemours KidsHealth – Understanding Puberty (duyệt y khoa 5/2022)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
PA = '<a href="https://knowledge-for-policy.ec.europa.eu/health-promotion-knowledge-gateway/physical-activity-sedentary-behaviour-table-2a_en">khuyến nghị WHO (bảng tổng hợp của EU)</a>'
COCH = '<a href="https://www.cochrane.org/news/teaching-children-schools-about-sexual-abuse-may-help-them-report-abuse">Walsh et al. 2015, Cochrane</a>'
ITGSE = '<a href="https://www.unfpa.org/publications/international-technical-guidance-sexuality-education">UNESCO và các tổ chức LHQ 2018 (ITGSE)</a>'
SFP = '<a href="https://foundations.org.uk/toolkit/guidebook/strengthening-families-programme-10-14">Strengthening Families 10–14 (Foundations, Anh)</a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài này viết dựa trên nguồn y khoa và giáo dục, nhưng chưa được bác sĩ hay thầy cô duyệt. Người lớn hãy đọc trước cùng con.</p></div>')
ADULT_ONLY = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. '
              'Người lớn đồng hành (từ 18 tuổi) có thể góp ý ở trang <a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên hay trường của con.</p>')
TALK = ('Ai chạm vào bạn làm bạn khó chịu, đe dọa, hay bắt bạn giữ bí mật: kể ngay cho người lớn tin cậy. '
        'Gọi <strong>111</strong> (miễn phí, 24/7). Nguy hiểm ngay lúc đó: gọi <strong>113</strong>.')

L = {
 '1': (1, 'co-the-minh-dang-lon', 'Bài 1', 'Cơ thể mình đang lớn'),
}
PLAN = [
 (1, 'Cơ thể mình đang lớn', 'Bạn biết các thay đổi khi dậy thì và làm đủ 5 việc chăm cơ thể ít nhất 5/7 ngày.'),
 (2, 'Cơ thể của mình, ranh giới của mình', 'Bạn phân biệt được bí mật vui và bí mật phải kể; viết tên 5 người lớn tin cậy.'),
 (3, 'An toàn trên mạng', 'Bạn kiểm tra cài đặt riêng tư cùng người lớn và nói được 4 dấu hiệu người lạ nguy hiểm.'),
 (4, 'Nhận ra lừa đảo và dụ dỗ', 'Bạn nhận ra 5 dấu hiệu lừa đảo và dùng quy tắc Dừng – Hỏi – Kể.'),
 (5, 'Bạn bè và bắt nạt', 'Bạn có 3 câu nói để giúp bạn bị bắt nạt và biết báo cho ai.'),
 (6, 'Nói "không" mà vẫn giữ bạn', 'Bạn tập 3 cách từ chối và có thẻ mật mã gọi đón.'),
 (7, 'An toàn đường, nước, điện', 'Bạn có checklist ra khỏi nhà và nói được quy tắc an toàn khi ở gần nước.'),
 (8, 'Cảm xúc và khi nào cần giúp', 'Bạn hoàn thành Bản đồ an toàn của tôi và cất ở chỗ dễ tìm.'),
]

def lesson(k, desc, sections, figs_after=3):
    w, slug, code, title = L[k]
    meta = [f'Tuần {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Nói với người lớn 5 phút']
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Lớn lên an toàn (10–14)</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('A' + k)}
{''.join(sections[figs_after:])}
{ADULT_ONLY}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{U}">← Về trang khóa học</a><a href="{U}#tam-tuan">Bài 2 đang soạn →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

# ======================= BÀI 1 =======================
DAYS = ''.join(f'<th>{d}</th>' for d in ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN'])
HABITS = ['Tắm, rửa mặt', 'Đánh răng sáng và tối', 'Thay đồ lót, tất sạch', 'Vận động, chơi ngoài trời', 'Đi ngủ đúng giờ đã chọn: ……']
hrows = ''.join(f'<tr><td>{h}</td>' + '<td></td>' * 7 + '</tr>' for h in HABITS)
HABIT_TABLE = (f'<div class="table-wrap"><table><thead><tr><th class="w38">Việc chăm cơ thể</th>{DAYS}</tr></thead>'
               f'<tbody>{hrows}</tbody></table></div>')
SELF = ['Tôi kể được 4 thay đổi khi dậy thì', 'Tôi làm đủ 5 việc chăm cơ thể', 'Tôi đã hỏi một người lớn tin cậy ít nhất 1 câu']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)

lesson('1', 'Khóa Lớn lên an toàn, bài 1: dậy thì là gì, năm việc chăm cơ thể mỗi ngày, và hỏi người lớn tin cậy.', [
 sec(1, 'Sau bài này, bạn sẽ', ul([
   'Kể được <strong>4 thay đổi</strong> thường gặp khi dậy thì.',
   'Làm đủ <strong>5 việc chăm cơ thể</strong> ít nhất 5 trong 7 ngày.',
   'Hỏi một người lớn tin cậy <strong>ít nhất 1 câu</strong> về cơ thể mình.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['In trang này, hoặc chép bảng 7 ngày ra giấy.', 'Một cây bút. Một chỗ ngồi yên tĩnh.',
   'Nghĩ trước: người lớn nào bạn thấy dễ hỏi nhất?'])),
 sec(3, 'Đọc (10 phút)', ol([
   '<strong>Dậy thì là gì?</strong> Là lúc cơ thể chuyển dần từ trẻ em sang người lớn. Ai cũng trải qua. Không có gì xấu hổ.',
   '<strong>Khi nào bắt đầu?</strong> Bạn gái thường từ 8 đến 13 tuổi. Bạn trai thường từ 9 đến 14 tuổi. Sớm hay muộn hơn bạn bè thường vẫn bình thường.',
   '<strong>Bốn thay đổi hay gặp.</strong> Cao nhanh. Ra nhiều mồ hôi, có mùi, có thể nổi mụn. Mọc lông ở nách và vùng kín. Cảm xúc mạnh hơn, đổi nhanh hơn.',
   '<strong>Thay đổi riêng.</strong> Bạn gái: ngực phát triển trước, kinh nguyệt thường đến khoảng 2 năm sau. Bạn trai: vỡ giọng, vai rộng ra, cơ quan sinh dục lớn lên.',
   '<strong>Giữ sạch.</strong> Tắm mỗi ngày, nhất là sau khi vận động. Rửa mặt 1–2 lần bằng nước ấm. Thay đồ lót và tất mỗi ngày.',
   '<strong>Ngủ và vận động.</strong> Tuổi 6–12 cần ngủ 9–12 giờ, tuổi 13–18 cần 8–10 giờ. Mỗi ngày nên vận động khoảng 60 phút.',
   '<strong>Không so sánh.</strong> Mỗi cơ thể lớn theo lịch riêng. Đừng trêu bạn khác, và đừng để ai trêu cơ thể bạn.'])),
 sec(4, 'Làm (10 phút): bảng 7 ngày', '<p>Chọn giờ đi ngủ của bạn và viết vào dòng cuối. Mỗi tối đánh dấu ✓ việc đã làm.</p>' + HABIT_TABLE +
   '<p><strong>Hộp câu hỏi:</strong> viết 1–3 câu bạn muốn hỏi về cơ thể. Không cần ghi tên.</p>'
   '<div class="table-wrap journal"><table><tbody><tr><th class="w38">Câu hỏi 1</th><td></td></tr><tr><th>Câu hỏi 2</th><td></td></tr><tr><th>Câu hỏi 3</th><td></td></tr></tbody></table></div>'),
 sec(5, 'Nói với người lớn (5 phút)', ol([
   'Chọn một người lớn tin cậy: bố, mẹ, ông bà, cô chú, y tế trường, bác sĩ.',
   'Mở lời bằng một câu dưới đây, rồi hỏi một câu trong hộp câu hỏi.',
   'Người đó chưa biết? Không sao. Hẹn cùng tìm hiểu, hoặc cùng hỏi bác sĩ.']) +
   '<p><strong>Câu mở lời mẫu:</strong></p>' + ul(['<em>"Con đang học bài về dậy thì. Con hỏi bố/mẹ một câu được không?"</em>',
   '<em>"Con có câu hỏi hơi ngại. Mình nói lúc chỉ có hai người nhé?"</em>', '<em>"Hồi bằng tuổi con, bố/mẹ thấy thế nào?"</em>'])),
 sec(6, 'An toàn', ul([
   'Lo vì cơ thể thay đổi sớm hơn hay muộn hơn bạn bè? Nhờ bố mẹ đưa đi khám để hỏi bác sĩ.',
   'Không tự mua thuốc, kem làm trắng, thuốc giảm cân hay thuốc tăng chiều cao trên mạng.',
   'Buồn kéo dài, lo nhiều, hay muốn làm đau bản thân: nói ngay với người lớn và gọi số ở khối "Cần giúp ngay".',
   TALK])),
 sec(7, 'Tự đánh giá', '<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>'
   f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Hôm nay</th><th>Sau 7 ngày</th></tr></thead><tbody>{srows}</tbody></table></div>'),
 sec(8, 'Cho người lớn đồng hành', ul([
   'Đọc bài trước. Trả lời thật, ngắn, dùng từ đúng tên bộ phận cơ thể.',
   'Không biết thì nói "để mình cùng tìm hiểu". Không cười, không trêu, không kể lại cho người khác.',
   f'Khóa dành cho bố mẹ: <a href="{G4}">Gia đình có con 10–14</a>, bài 1 và bài 2.'])),
 sec(9, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Tuổi bắt đầu dậy thì (gái 8–13, trai 9–14), các thay đổi chính, kinh nguyệt khoảng 2 năm sau khi ngực phát triển, cách giữ vệ sinh ({KH}).'),
   lb('Đã xác nhận', f'Giờ ngủ theo tuổi ({AASM}). Vận động khoảng 60 phút mỗi ngày cho tuổi 5–17 ({PA}).'),
   lb('Đã xác nhận', f'Bộ hướng dẫn quốc tế {ITGSE} có chủ đề cơ thể và dậy thì cho tuổi đi học. Bài này chỉ mượn ý tưởng.'),
   lb('Đánh giá chuyên môn', 'Bảng 7 ngày, hộp câu hỏi và câu mở lời do daynentang.com soạn. Lời khuyên "không tự mua thuốc trên mạng" là lời khuyên an toàn chung.')]))
])

# ======================= TRANG KHÓA =======================
rows = ''
for w, title, goal in PLAN:
    k = str(w)
    cell = f'<a href="{url(w, L[k][1])}">{title}</a>' if k in L else f'{title} <span class="small muted">(đang soạn)</span>'
    rows += f'<tr><td>{w}</td><td>{cell}</td><td>{goal}</td></tr>'

page(U, 'Lớn lên an toàn (10–14)', 'Khóa tự học miễn phí cho bạn 10–14 tuổi: cơ thể đang lớn, ranh giới, an toàn trên mạng, lừa đảo, bắt nạt, nói không, khi nào cần giúp.',
f'''
<p class="eyebrow">Cá nhân · Khóa C1 · Đang soạn</p>
<h1>Lớn lên an toàn (10–14)</h1>
<p class="lead">Bạn đang lớn nhanh. Khóa này giúp bạn hiểu cơ thể mình, nhận ra nguy hiểm, biết nói "không" và biết tìm ai khi cần.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn tự chăm cơ thể, nhận ra tình huống không an toàn, và biết nhờ người lớn giúp sớm</td></tr>
<tr><th>Dành cho</th><td>Bạn 10–14 tuổi tự đọc, có một người lớn tin cậy đồng hành. Bố mẹ xem thêm khóa <a href="{G4}">Gia đình có con 10–14</a></td></tr>
<tr><th>Thời lượng</th><td>8 tuần, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, nói với người lớn 5 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút. Không cần điện thoại hay máy tính để học</td></tr>
<tr><th>Tình trạng</th><td>Đang soạn: đã có bài 1, bản chưa dạy thử, chưa có chuyên gia duyệt</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn làm đều 5 việc chăm cơ thể.</li><li>Bạn có tên 3–5 người lớn tin cậy.</li><li>Bạn có mật mã gọi đón và cài đặt riêng tư trên điện thoại.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: dừng lại, nghĩ, rồi mới chọn.</li><li>Kỹ năng: nói "không" mà vẫn giữ bạn.</li><li>Biết nhờ giúp sớm. Kể ra không bao giờ là lỗi của bạn.</li></ul></div>
</div>
{figure_block('KHOAA')}

<h2 id="tam-tuan">Tám tuần</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Cho người lớn đồng hành</h2>
<ul>
<li>Đọc bài trước con. Bài 2 về ranh giới cơ thể nên đọc cùng nhau.</li>
<li>Khi con hỏi: cảm ơn con, trả lời thật và ngắn, dùng từ đúng.</li>
<li>Khi con kể chuyện xấu: tin con, giữ bình tĩnh, không trách. Gọi 111 nếu cần.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{COCH}</td><td>Dạy trẻ về ranh giới cơ thể, bí mật phải kể, người lớn tin cậy</td><td><span class="label">[Đã xác nhận]</span> 24 thử nghiệm, 5.802 trẻ: trẻ hiểu biết hơn, có hành vi tự bảo vệ hơn, kể ra nhiều hơn; ít dấu hiệu gây lo lắng. Chưa rõ có giảm số vụ xâm hại không. Các chương trình làm ở trường</td></tr>
<tr><td>{ITGSE}</td><td>Chủ đề cơ thể, dậy thì, an toàn theo độ tuổi</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn quốc tế của UNESCO, UNFPA, UNICEF, WHO và các tổ chức LHQ khác</td></tr>
<tr><td>{SFP}</td><td>Kỹ năng từ chối áp lực bạn bè, cùng làm với bố mẹ</td><td><span class="label">[Đã xác nhận]</span> Mức 3 theo Foundations (đã dùng ở khóa Gia đình 10–14)</td></tr>
<tr><td>{KH}; {AASM}</td><td>Kiến thức dậy thì, vệ sinh, giấc ngủ</td><td><span class="label">[Đã xác nhận]</span> Tài liệu y khoa cho gia đình; đồng thuận chuyên gia</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các chương trình gốc dạy ở trường, có thầy cô hướng dẫn. Khóa tự học này chưa được thử nghiệm và chưa có chuyên gia duyệt.
  Khóa không thay thế bác sĩ, nhà tâm lý hay cơ quan bảo vệ trẻ em.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C1 built')
