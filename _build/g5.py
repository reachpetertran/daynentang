# Khóa G5 "Vợ chồng đồng lòng" – trang khóa, 6 bài, 1 công cụ in
import illus_g5  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/vo-chong-dong-long/'
TOOL = '/cong-cu/so-tay-vo-chong/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
def sec(n, title, body): return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'
def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>{need}</em></p><ol>{li}</ol>{nt}</div>'
JOURNAL = ('<div class="table-wrap journal"><table><tbody>'
           '<tr><th class="w38">Hai người đã làm được gì</th><td></td></tr><tr><th>Điều gì khó</th><td></td></tr>'
           '<tr><th>Tuần sau thử gì</th><td></td></tr></tbody></table></div>')

FEIN = '<a href="https://pure.psu.edu/en/publications/establishing-family-foundations-intervention-effects-on-coparenti/">Feinberg &amp; Kan 2008, <em>Journal of Family Psychology</em> 22(2)</a>'
META = '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9407961">Zhao et al. 2022, phân tích gộp 93 nghiên cứu</a>'
HAR = '<a href="https://pubmed.ncbi.nlm.nih.gov/29574737/">Harold &amp; Sellers 2018, <em>J Child Psychol Psychiatry</em></a>'
GOT = '<a href="https://washington.edu/news/1999/09/27/first-three-minutes-of-discussion-about-on-going-area-of-marital-conflict-are-predictive-of-divorce-for-newlyweds">Carrère &amp; Gottman 1999, <em>Family Process</em></a>'
LUAT = '<a href="https://luatvietnam.vn/hon-nhan-gia-dinh/luat-phong-chong-bao-luc-gia-dinh-so-13-2022-qh15-238397-d1.html">Luật Phòng, chống bạo lực gia đình số 13/2022/QH15</a>'
SURV = '<a href="https://www.sggp.org.vn/gan-63-phu-nu-o-nuoc-ta-tung-chiu-bao-luc-50-khong-ke-voi-ai-post620554.html">Nghiên cứu quốc gia về bạo lực đối với phụ nữ 2019</a>'
T117 = '<a href="https://thuonghieucongluan.com.vn/tong-dai-117-hoat-dong-24-7-tiep-nhan-tin-bao-bao-luc-gia-dinh-tren-toan-quoc-a333505.html">Tổng đài 117</a>'
DV = ('<div class="box warn"><p><strong>Khóa này không dành cho quan hệ có bạo lực.</strong> Đánh đập, đe dọa, chửi bới, kiểm soát tiền, cấm gặp người thân, ép quan hệ đều là bạo lực gia đình theo luật. '
      'Khi có bạo lực, đừng tập các bài "nói chuyện khó" một mình với người gây bạo lực. An toàn đến trước: gọi <strong>113</strong> khi nguy hiểm tức thì; '
      '<strong>117</strong> là tổng đài quốc gia về phòng, chống bạo lực gia đình (24/7); trẻ em bị hại gọi <strong>111</strong>.</p></div>')

L = {
 '1': (1, 'hai-nguoi-mot-doi', 'Bài 1', 'Hai người, một đội'),
 '2': (2, 'cam-on-va-dap-lai', 'Bài 2', 'Cảm ơn và đáp lại nhau'),
 '3': (3, 'noi-khi-bat-dong', 'Bài 3', 'Nói khi bất đồng'),
 '4': (4, 'khi-nong-gian', 'Bài 4', 'Khi nóng giận: tạm dừng và hàn gắn'),
 '5': (5, 'truoc-mat-con', 'Bài 5', 'Trước mặt con'),
 '6': (6, 'hop-vo-chong', 'Bài 6', 'Họp vợ chồng và giữ đều'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'g5-' + k
    note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này đã soạn theo khung của khóa nhưng chưa được thử. '
            f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn. Xin không ghi tên vợ, chồng hay con.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về {code.lower()}</a></p></div>')
    meta = [f'Tuần {w}', 'Hai vợ chồng 30 phút', 'Việc nhỏ mỗi ngày']
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Vợ chồng đồng lòng</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{DV if k in ('3', '4') else ''}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block('W' + k)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/gia-dinh/')

SAFE = 'Nếu có đánh đập, đe dọa, kiểm soát hay ép buộc: dừng bài, ưu tiên an toàn. Gọi 113 khi nguy hiểm tức thì; 117 tổng đài phòng, chống bạo lực gia đình.'

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Vợ chồng đồng lòng, bài 1: bốn phần của đồng nuôi dạy, tìm điểm giống và khác về nuôi con, đứng cùng một phía.', [
 sec(1, 'Mục tiêu', ul(['Hai người viết ra <strong>3 điều giống nhau</strong> và <strong>3 điều khác nhau</strong> về cách nuôi con.', 'Thống nhất <strong>1 luật</strong>: bất đồng về con thì bàn riêng, nói với con một lời.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In trang 1 của <a href="{TOOL}">Sổ tay vợ chồng</a>, mỗi người một bản.', 'Chọn lúc con ngủ, cả hai không quá mệt. Úp điện thoại.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nói một lần gần đây thấy người kia làm tốt việc gì với con. Cụ thể.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Bốn phần của đồng nuôi dạy (5 phút).</strong> Đồng thuận về hướng nuôi dạy; chia việc; ủng hộ, không phá nhau trước con; cùng xử lý bất đồng, không kéo con vào.',
   '<strong>Tự viết (7 phút).</strong> Mỗi người tự viết 5 điều mình coi trọng khi nuôi con: giờ ngủ, điện thoại, đồ ngọt, học thêm, kỷ luật, việc nhà.',
   '<strong>So sánh (8 phút).</strong> Điều giống nhau ghi vào giữa. Điều khác nhau ghi hai bên. Chưa tranh luận ai đúng.',
   '<strong>Luật đầu tiên (5 phút).</strong> "Bất đồng về con thì bàn riêng. Nói với con một lời." Viết ra, cả hai ký.'])),
 sec(5, 'Việc nhỏ mỗi ngày', ul(['Mỗi ngày, một người nhắn người kia một điều nhỏ về con: "Hôm nay con tự cất cặp."', 'Khi con hỏi điều chưa thống nhất: "Bố mẹ bàn rồi trả lời con sau."'])),
 sec(6, 'Câu hỏi hỏi nhau', ol(['Điều khác nhau nào làm mình hay cãi nhất?', 'Cách nuôi dạy của bố mẹ mỗi người ảnh hưởng mình thế nào?', 'Mình cần người kia ủng hộ điều gì nhất?'])),
 sec(7, 'An toàn và ranh giới', ul([SAFE, 'Không dùng danh sách "khác nhau" để chê người kia. Mục đích là thấy rõ, chưa phải giải quyết.'])),
 sec(8, 'Khi một người đi công tác', mom('Cần: 2 bản trang 1, 30 phút gọi video.', [
   ('Trước cuộc gọi.', 'Mỗi người tự viết 5 điều, chụp gửi nhau.'), ('Trong cuộc gọi.', 'So sánh, viết phần giống và khác, đọc to luật đầu tiên.')], [
   ('Bố mẹ không sống chung:', 'đồng nuôi dạy vẫn quan trọng. Có thể làm bài này qua tin nhắn, chỉ tập trung vào phần về con.')])),
 sec(9, 'Ôn lại', ul(['<strong>Trong tuần:</strong> mỗi lần lỡ cãi trước con, ghi lại. Không trách, chỉ ghi.', '<strong>Cuối tuần:</strong> luật đầu tiên giữ được mấy lần?'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Phân tích gộp 93 nghiên cứu (41.207 người): đồng nuôi dạy tốt gắn với ít vấn đề hành vi, cảm xúc ở trẻ hơn; xung đột trong đồng nuôi dạy là yếu tố liên hệ rõ nhất. Mức liên hệ yếu (r khoảng 0,16–0,20) và là tương quan ({META}).'),
   lb('Đã xác nhận', f'Thử nghiệm ngẫu nhiên với 169 cặp vợ chồng sắp có con đầu lòng: lớp học 8 buổi về đồng nuôi dạy cải thiện sự ủng hộ nhau, giảm trầm cảm, lo âu ở mẹ, cải thiện quan hệ cha mẹ – con ({FEIN}).'),
   lb('Đánh giá chuyên môn', 'Bốn phần của đồng nuôi dạy được tóm tắt từ các nghiên cứu trên; bài tập do daynentang.com soạn, chỉ mượn ý tưởng.')]))
])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Vợ chồng đồng lòng, bài 2: đáp lại lời mời nhỏ của nhau và cảm ơn cụ thể mỗi ngày.', [
 sec(1, 'Mục tiêu', ul(['Mỗi người nói <strong>1 lời cảm ơn cụ thể</strong> mỗi ngày, ít nhất 6/7 ngày.', 'Mỗi người để ý và đáp lại ít nhất <strong>3 lời mời nhỏ</strong> mỗi ngày.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 2 của <a href="{TOOL}">Sổ tay vợ chồng</a>.', 'Giấy nhớ để dán lời cảm ơn.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nhớ lại: <em>"Lần gần nhất mình thấy được người kia ghi nhận là khi nào?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Lời mời nhỏ (7 phút).</strong> "Anh xem này", một câu chuyện, một cái chạm, một tiếng thở dài. Mỗi lần là một lời mời gần nhau.',
   '<strong>Ba cách đáp (5 phút).</strong> Quay sang (đáp lại), quay đi (lờ đi), quay ngược (gắt). Chỉ cần quay sang nhiều hơn.',
   '<strong>Cảm ơn cụ thể (8 phút).</strong> Việc cụ thể + điều nó giúp mình. Mỗi người viết 3 lời cảm ơn cho tuần qua, đọc cho nhau nghe.',
   '<strong>Điều làm mình thấy được yêu thương (5 phút).</strong> Mỗi người nói 2 việc nhỏ người kia làm khiến mình thấy được quan tâm.'])),
 sec(5, 'Việc nhỏ mỗi ngày', ul(['Một lời cảm ơn cụ thể, nói hoặc nhắn.', 'Khi người kia bắt chuyện, đặt điện thoại xuống 1 phút.'])),
 sec(6, 'Câu hỏi hỏi nhau', ol(['Lời mời nào của mình hay bị lỡ?', 'Lúc nào trong ngày mình hay "quay đi" nhất?', 'Việc nhỏ nào người kia làm mà mình chưa từng cảm ơn?'])),
 sec(7, 'An toàn và ranh giới', ul([SAFE])),
 sec(8, 'Khi một người đi công tác', mom('Cần: tin nhắn mỗi ngày.', [
   ('Mỗi ngày.', 'Người đi xa nhắn một lời cảm ơn cụ thể cho người ở nhà, vì người ở nhà đang gánh nhiều hơn.'),
   ('Mỗi tối.', 'Một cuộc gọi ngắn: hỏi "Hôm nay em mệt nhất lúc nào?", nghe hết.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tối:</strong> đánh dấu lời cảm ơn trong ngày.', '<strong>Cuối tuần:</strong> mỗi người nói lời cảm ơn mình nhớ nhất.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Ý tưởng "lời mời nhỏ" và "quay sang – quay đi" phổ biến trong tư vấn hôn nhân; daynentang.com chưa đọc nghiên cứu gốc đủ để nêu số liệu.'),
   lb('Đã xác nhận', f'Thử nghiệm {FEIN} cho thấy can thiệp tăng sự ủng hộ nhau giữa hai vợ chồng khi nuôi con.')]))
])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Vợ chồng đồng lòng, bài 3: mở lời nhẹ khi bất đồng và luyện người nói – người nghe.', [
 sec(1, 'Mục tiêu', ul(['Mỗi người viết lại <strong>1 lời phàn nàn</strong> thành câu mở lời nhẹ.', 'Hai người đi trọn <strong>3 lượt người nói – người nghe</strong> về một chuyện vừa phải.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 3 của <a href="{TOOL}">Sổ tay vợ chồng</a>.', 'Một vật làm "sàn": cái thìa, cây bút.', 'Chọn chuyện vừa phải, không phải chuyện nóng nhất.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nhớ một câu người kia nói làm mình thấy bị tấn công. Không kể ra, chỉ nhớ cảm giác.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Mở lời nhẹ (8 phút).</strong> "Em thấy… khi… vì… Em cần…". Nói về cảm xúc của mình và việc cụ thể, không chê con người.',
   'Ví dụ: "Anh chẳng bao giờ giúp" thành "Em mệt khi tối nào cũng một mình tắm cho con. Em cần anh lo tắm 3 tối một tuần."',
   '<strong>Người nói – người nghe (15 phút).</strong> Người cầm "sàn" nói 2–3 câu. Người nghe nhắc lại: "Ý anh là…?" Người nói sửa nếu chưa đúng. Rồi đổi vai.',
   '<strong>Chưa giải quyết vội (2 phút).</strong> Mục tiêu hôm nay là hiểu nhau. Giải pháp để buổi sau hoặc họp tuần.'])),
 sec(5, 'Việc nhỏ mỗi ngày', ul(['Khi muốn phàn nàn, dừng 5 giây, nói theo mẫu "Em thấy… khi… Em cần…".'])),
 sec(6, 'Câu hỏi hỏi nhau', ol(['Câu mở đầu nào của mình hay làm cuộc nói chuyện hỏng ngay?', 'Khi được nhắc lại đúng ý, mình thấy thế nào?', 'Chuyện nào nên để họp tuần thay vì nói lúc đang mệt?'])),
 sec(7, 'An toàn và ranh giới', ul([SAFE, 'Nếu cuộc nói chuyện nóng lên, dùng ngay tín hiệu tạm dừng (bài 4).'])),
 sec(8, 'Khi một người đi công tác', mom('Cần: gọi video 30 phút, giấy bút.', [
   ('Trong cuộc gọi.', 'Tập mẫu mở lời nhẹ với chuyện nhỏ. Người nghe nhắc lại trước khi trả lời.')], [
   ('Tránh:', 'cãi nhau qua tin nhắn. Chuyện khó thì hẹn giờ gọi, nghe được giọng nhau.')])),
 sec(9, 'Ôn lại', ul(['<strong>Trong tuần:</strong> ghi 1 lần mình mở lời nhẹ được.', '<strong>Cuối tuần:</strong> tập lại người nói – người nghe 1 lượt.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Nghiên cứu 124 cặp mới cưới: những cặp về sau ly hôn có nhiều biểu hiện tiêu cực, ít tích cực hơn ngay trong 3 phút đầu cuộc bàn chuyện bất đồng ({GOT}). Chỉ 17 cặp ly hôn; kết quả trong phòng thí nghiệm, không dùng để dự đoán từng cặp.'),
   lb('Suy luận', 'Vì vậy bài tập trung vào cách mở lời. Mẫu câu và trò người nói – người nghe là kỹ thuật phổ biến trong giáo dục hôn nhân; cách viết do daynentang.com soạn.')]))
])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Vợ chồng đồng lòng, bài 4: tín hiệu tạm dừng khi nóng giận, quay lại sau 20 phút, và câu hàn gắn.', [
 sec(1, 'Mục tiêu', ul(['Hai người thống nhất <strong>tín hiệu tạm dừng</strong>, thời gian quay lại, và mỗi người chọn <strong>1 việc làm dịu</strong>.', 'Mỗi người viết sẵn <strong>2 câu hàn gắn</strong>.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 4 của <a href="{TOOL}">Sổ tay vợ chồng</a>.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người tự nhận: <em>"Khi giận, cơ thể mình báo hiệu thế nào? (nóng mặt, tim đập nhanh, nói to)"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Khi quá nóng, không nói được gì tốt (5 phút).</strong> Lúc đó cần dừng, không phải thắng.',
   '<strong>Tín hiệu dừng (5 phút).</strong> Một câu hay cử chỉ cả hai đồng ý, ví dụ "Mình nghỉ 20 phút nhé". Ai cũng được dùng, người kia tôn trọng.',
   '<strong>Trong 20 phút (5 phút).</strong> Làm việc dịu lại: đi bộ, rửa mặt, thở chậm. Không nghĩ cách cãi tiếp, không nhắn tin.',
   '<strong>Quay lại (3 phút).</strong> Tạm dừng khác bỏ đi: luôn hẹn giờ quay lại. Nếu vẫn nóng, hẹn lại lần nữa.',
   '<strong>Hàn gắn (7 phút).</strong> Câu ngắn: nhận phần mình ("Lúc nãy anh to tiếng, anh xin lỗi"), hiểu người kia, mời bắt đầu lại. Mỗi người viết 2 câu.'])),
 sec(5, 'Việc nhỏ mỗi ngày', ul(['Khi thấy dấu hiệu nóng giận của cơ thể, gọi tên nó trong đầu: "Mình đang nóng."', 'Sau mỗi lần căng thẳng, một người nói câu hàn gắn trước.'])),
 sec(6, 'Câu hỏi hỏi nhau', ol(['Khi giận, mình cần không gian hay cần được ôm?', 'Câu hàn gắn nào mình dễ nghe nhất?', 'Có chuyện cũ nào cần hàn gắn mà chưa nói?'])),
 sec(7, 'An toàn và ranh giới', ul([SAFE, 'Nếu một người không cho người kia rời đi, chặn cửa, giật điện thoại: đó là dấu hiệu nguy hiểm. Rời đi nơi an toàn và gọi giúp.',
   'Không cãi nhau khi có rượu bia. Hẹn nói chuyện lúc tỉnh táo.'])),
 sec(8, 'Khi một người đi công tác', mom('Cần: thống nhất qua điện thoại.', [
   ('Qua điện thoại.', 'Tín hiệu dừng là "Mình gọi lại sau 20 phút nhé". Gác máy nhẹ nhàng, gọi lại đúng hẹn.')], [
   ('Người ở nhà quá tải:', 'nóng giận dễ đến từ mệt. Người đi xa hỏi "Em cần gì để đỡ mệt tuần này?" trước khi bàn chuyện khó.')])),
 sec(9, 'Ôn lại', ul(['<strong>Trong tuần:</strong> ghi số lần dùng tín hiệu dừng và có quay lại không.', '<strong>Cuối tuần:</strong> câu hàn gắn nào đã dùng?'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{LUAT} (thông qua 14/11/2022, hiệu lực 01/07/2023) liệt kê các hành vi bạo lực gia đình gồm thể chất, tinh thần (lăng mạ, xúc phạm), cô lập, kiểm soát kinh tế, tình dục. Tra cứu 28/10/2026.'),
   lb('Đã xác nhận', f'{T117}: tổng đài quốc gia về phòng, chống bạo lực gia đình, hoạt động 24/7 toàn quốc từ tháng 9/2026 theo báo chí; chúng tôi chưa xác nhận có miễn phí hay không.'),
   lb('Đánh giá chuyên môn', 'Thời gian tạm dừng 20 phút và câu hàn gắn là kỹ thuật phổ biến trong tư vấn hôn nhân; con số 20 phút là gợi ý, không phải số liệu nghiên cứu.')]))
])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Vợ chồng đồng lòng, bài 5: bất đồng trước mặt con: bàn riêng, không kéo con về phe, để con thấy bố mẹ làm lành.', [
 sec(1, 'Mục tiêu', ul(['Hai người thống nhất <strong>câu nói mẫu</strong> khi chưa đồng ý trước mặt con.', 'Trong tuần, <strong>không lần nào</strong> chê bố hay mẹ trước con, nhờ con nhắn lời, hay bắt con chọn phe.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 5 của <a href="{TOOL}">Sổ tay vợ chồng</a>.', 'Nhớ lại một lần cãi nhau trước mặt con gần đây.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nhớ: <em>"Hồi nhỏ, khi bố mẹ mình cãi nhau, mình cảm thấy thế nào?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Con nhìn thấy gì (5 phút).</strong> Con để ý cách bố mẹ cãi nhau và làm lành, kể cả khi bố mẹ nghĩ con không nghe.',
   '<strong>Nên tránh (5 phút).</strong> Chê bố hay mẹ trước con; bắt con chọn phe; nhờ con nhắn lời; phá luật người kia vừa đặt.',
   '<strong>Câu nói mẫu (7 phút).</strong> "Bố mẹ đang nghĩ khác nhau. Bố mẹ sẽ bàn và trả lời con sau bữa tối." Tập nói to.',
   '<strong>Để con thấy làm lành (5 phút).</strong> Nếu con đã thấy bố mẹ to tiếng, cũng để con thấy bố mẹ xin lỗi và làm lành. Nói với con: "Bố mẹ đã nói chuyện xong rồi. Không phải lỗi của con."',
   '<strong>Kiểm lại (3 phút).</strong> Lần cãi nhau gần đây: điều gì nên làm khác?'])),
 sec(5, 'Việc nhỏ mỗi ngày', ul(['Nói tốt về người kia trước mặt con ít nhất 1 lần: "Mẹ nấu canh ngon quá."', 'Khi con hỏi điều chưa thống nhất, dùng câu nói mẫu.'])),
 sec(6, 'Câu hỏi hỏi nhau', ol(['Mình có từng than phiền về người kia với con không?', 'Luật nào của người kia mình hay phá ngầm?', 'Con mình có bao giờ hỏi "Bố mẹ có bỏ nhau không?"'])),
 sec(7, 'An toàn và ranh giới', ul([SAFE, 'Để con chứng kiến bạo lực cũng là bạo lực gia đình theo luật. Trẻ em bị hại hay chứng kiến bạo lực: gọi 111.'])),
 sec(8, 'Khi một người đi công tác', mom('Cần: 20 phút gọi video.', [
   ('Trong cuộc gọi.', 'Thống nhất câu nói mẫu. Người ở nhà dùng khi con hỏi về quyết định cần cả hai.'),
   ('Khi gọi video với con.', 'Người đi xa không hỏi con về chuyện của người ở nhà; không nhờ con nhắn lời.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> một lần nói tốt về người kia trước con.', '<strong>Cuối tuần:</strong> có lần nào lỡ kéo con vào không?'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Tổng quan nghiên cứu: xung đột giữa bố mẹ ảnh hưởng đến cảm xúc, hành vi, học tập và các mối quan hệ sau này của con, dù bố mẹ sống chung hay không. Điều quan trọng là cách bố mẹ thể hiện và xử lý xung đột, trên một dải từ im lặng đến bạo lực ({HAR}).'),
   lb('Đã xác nhận', f'Trong phân tích gộp {META}, xung đột và "kéo con vào tam giác" trong đồng nuôi dạy liên hệ với nhiều vấn đề ở trẻ hơn; đây là tương quan.'),
   lb('Đã xác nhận', f'{LUAT}: cưỡng ép chứng kiến bạo lực là một hành vi bạo lực gia đình.')]))
])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Vợ chồng đồng lòng, bài 6: họp vợ chồng 20 phút mỗi tuần, kế hoạch khi đi công tác, và đánh giá cuối khóa.', [
 sec(1, 'Mục tiêu', ul(['Hai người chốt <strong>giờ họp cố định</strong> và làm buổi họp 20 phút đầu tiên.', 'Có <strong>kế hoạch tuần đi công tác</strong>. Chấm phiếu tự đánh giá cuối khóa.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 6 của <a href="{TOOL}">Sổ tay vợ chồng</a>.', 'Lịch tháng tới của cả hai.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nói một điều đã khác đi trong 5 tuần qua, dù rất nhỏ.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Năm phần họp (20 phút):</strong> Cảm ơn (4\') – Lịch tuần (4\') – Chuyện con (5\') – Một chuyện cần bàn (4\') – Hẹn một lúc riêng cho hai người (3\').',
   '<strong>Kế hoạch đi công tác:</strong> việc nào người ở nhà tạm bỏ; ai đỡ người ở nhà (ông bà, hàng xóm); giờ gọi cố định; người đi xa lo việc nghĩ từ xa (hóa đơn, đặt lịch).',
   '<strong>Chăm sóc bản thân:</strong> mỗi người có 1 khoảng thời gian riêng mỗi tuần, người kia trông con.',
   '<strong>Đánh giá cuối khóa (5 phút):</strong> chấm phiếu tự đánh giá, so với tuần 1. Ghi 3 dòng nhật ký.'])),
 sec(5, 'Việc nhỏ mỗi ngày', ul(['Giữ lời cảm ơn mỗi ngày (bài 2).', 'Mỗi tuần một lúc riêng cho hai người, dù chỉ 20 phút uống trà sau khi con ngủ.'])),
 sec(6, 'Câu hỏi hỏi nhau', ol(['Điều gì sẽ làm buổi họp bị bỏ? Làm sao để giữ?', 'Kỹ năng nào trong khóa mình muốn giữ lâu dài?', 'Khi nào mình nên tìm tư vấn hôn nhân?'])),
 sec(7, 'An toàn và ranh giới', ul([SAFE, 'Mâu thuẫn kéo dài, lặp lại, hay một người buồn chán, mất ngủ nhiều tuần: tìm chuyên gia tư vấn hôn nhân hoặc tâm lý. Đường dây Ngày Mai 096 306 1414.'])),
 sec(8, 'Khi một người đi công tác', mom('Cần: 20 phút gọi video mỗi tuần.', [
   ('Mỗi tuần.', 'Họp qua video đúng giờ đã hẹn, đủ 5 phần.'), ('Trước chuyến đi dài.', 'Ngồi lại 15 phút làm kế hoạch đi công tác.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tuần:</strong> họp 20 phút.', '<strong>Sau 3 tháng:</strong> chấm lại phiếu tự đánh giá.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Buổi họp vợ chồng 20 phút và kế hoạch đi công tác do daynentang.com thiết kế, nối với họp gia đình (khóa Giá trị nhà mình) và họp tiền (khóa Tiền nhà mình).'),
   lb('Đã xác nhận', 'Giáo dục quan hệ vợ chồng cho gia đình thu nhập thấp có hiệu quả trung bình rất nhỏ (d = 0,061) theo một phân tích gộp (Hawkins &amp; Erickson). Vì vậy chúng tôi không hứa thay đổi lớn.'),
   lb('Đánh giá chuyên môn', 'Một cặp tự so sánh trước – sau 6 tuần không có nhóm đối chứng; đây không phải bằng chứng hiệu quả.')]))
])

# =============== TRANG KHÓA ===============
rows = ''.join(f'<tr><td>{L[k][0]}</td><td><a href="{link(k)[0]}">{L[k][3]}</a></td><td>{g}</td></tr>' for k, g in zip(ORDER, [
 '3 điểm giống, 3 điểm khác; luật "bàn riêng"', '1 lời cảm ơn cụ thể mỗi ngày, 6/7 ngày', '3 lượt người nói – người nghe',
 'Có tín hiệu dừng, 2 câu hàn gắn', 'Không kéo con vào bất đồng trong tuần', 'Họp 20 phút đầu tiên; chấm phiếu cuối khóa']))
page(U, 'Vợ chồng đồng lòng',
 'Khóa 6 tuần miễn phí cho vợ chồng: cùng một đội khi nuôi con, cảm ơn nhau, nói khi bất đồng, tạm dừng khi giận, không kéo con vào.',
f'''
<p class="eyebrow">Gia đình · Khóa G5 · Đang thử nghiệm</p>
<h1>Vợ chồng đồng lòng</h1>
<p class="lead">Hai người, một đội khi nuôi con. Khóa giúp vợ chồng ghi nhận nhau, nói chuyện khi bất đồng mà không làm tổn thương, và giữ con ngoài các cuộc cãi nhau.</p>
{DV}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Vợ chồng ủng hộ nhau khi nuôi con; bất đồng được xử lý bình tĩnh, riêng tư</td></tr>
<tr><th>Dành cho</th><td>Vợ chồng, cặp đôi đang nuôi con; bố mẹ không sống chung vẫn dùng được phần đồng nuôi dạy</td></tr>
<tr><th>Thời lượng</th><td>6 tuần. Mỗi tuần 30 phút cho hai người và một việc nhỏ mỗi ngày</td></tr>
<tr><th>Cần có</th><td>Giấy, bút, 30 phút yên tĩnh. Một người đi công tác thì gọi video</td></tr>
<tr><th>Tình trạng</th><td>Đủ 6 tuần, bản chưa dạy thử, sẽ sửa theo nhật ký</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Mỗi ngày một lời cảm ơn cụ thể.</li><li>Có luật "bất đồng về con thì bàn riêng".</li><li>Có tín hiệu tạm dừng khi nóng giận.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: hai người một đội, không ai thắng ai.</li><li>Kỹ năng: mở lời nhẹ, lắng nghe, hàn gắn.</li><li>Nếp họp vợ chồng 20 phút mỗi tuần.</li></ul></div>
</div>

<h2>Sáu tuần</h2>
{figure_block('KHOAW')}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ tay vợ chồng</a>: giống và khác về nuôi con, lời cảm ơn, mẫu mở lời nhẹ, tín hiệu dừng, câu nói trước mặt con, họp tuần, phiếu tự đánh giá.</li></ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{FEIN}</td><td>Tập trung vào đồng nuôi dạy: ủng hộ nhau, xử lý bất đồng về con</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên 169 cặp sắp có con đầu lòng, lớp 8 buổi. Chương trình có bản quyền; chúng tôi chỉ mượn ý tưởng</td></tr>
<tr><td>{META}</td><td>Vì sao đồng nuôi dạy quan trọng với con</td><td><span class="label">[Đã xác nhận]</span> 93 nghiên cứu; liên hệ yếu, tương quan</td></tr>
<tr><td>{HAR}</td><td>Cách bố mẹ xử lý xung đột ảnh hưởng đến con</td><td><span class="label">[Đã xác nhận]</span> Tổng quan nghiên cứu</td></tr>
<tr><td>{GOT}</td><td>Cách mở đầu cuộc nói chuyện khó</td><td><span class="label">[Đã xác nhận]</span> 124 cặp, 17 cặp ly hôn; quan sát</td></tr>
<tr><td>{LUAT}; {SURV}</td><td>Ranh giới an toàn, nhận diện bạo lực gia đình</td><td><span class="label">[Đã xác nhận]</span> Luật Việt Nam; nghiên cứu quốc gia: 62,9% phụ nữ từng chịu ít nhất một hình thức bạo lực hoặc kiểm soát từ chồng</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Lớp học có người hướng dẫn cho cặp vợ chồng sắp có con cho kết quả tốt; giáo dục hôn nhân nói chung, nhất là cho gia đình khó khăn, có hiệu quả trung bình rất nhỏ.
  Khóa tự học này chưa được thử. Khóa không thay thế tư vấn hôn nhân hay trị liệu.</p>
</div>

<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai. Xin không ghi tên người trong gia đình.</p>
{HELP_BOX}
''', current='/gia-dinh/')

# =============== CÔNG CỤ ===============
def lines(n): return ''.join('<tr><td class="tall"></td><td></td></tr>' for _ in range(n))
days = ''.join(f'<th>{d}</th>' for d in ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN'])
SELF = ['Bất đồng về con thì bàn riêng', 'Nói với con một lời', 'Cảm ơn nhau cụ thể mỗi ngày', 'Đáp lại lời mời nhỏ của nhau', 'Mở lời nhẹ khi phàn nàn',
        'Dùng tín hiệu tạm dừng và quay lại đúng hẹn', 'Có câu hàn gắn sau cãi nhau', 'Không kéo con vào bất đồng', 'Họp vợ chồng mỗi tuần', 'Có kế hoạch khi một người đi công tác']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)
page(TOOL, 'Sổ tay vợ chồng', 'Trang in cho khóa Vợ chồng đồng lòng: giống và khác về nuôi con, lời cảm ơn, mở lời nhẹ, tạm dừng, họp tuần, phiếu tự đánh giá.',
f'''
<h1>Sổ tay vợ chồng</h1>
<p>Dùng cho khóa <a href="{U}">Vợ chồng đồng lòng</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Giữ sổ ở chỗ riêng của hai người.</p>
{PRINT_ROW}
<h2>1. Giống và khác về nuôi con (tuần 1)</h2>
<div class="table-wrap"><table><thead><tr><th class="w38">Điều hai người giống nhau</th><th>Điều khác nhau (ghi cả hai ý)</th></tr></thead><tbody>{lines(4)}</tbody></table></div>
<p><strong>Luật đầu tiên:</strong> Bất đồng về con thì bàn riêng. Nói với con một lời. &nbsp; Ký: ………… · …………</p>
<h2>2. Lời cảm ơn mỗi ngày (tuần 2)</h2>
<div class="table-wrap"><table><thead><tr><th></th>{days}</tr></thead><tbody><tr><td>Chồng</td>{'<td></td>' * 7}</tr><tr><td>Vợ</td>{'<td></td>' * 7}</tr></tbody></table></div>
<h2>3. Mở lời nhẹ (tuần 3)</h2>
<p>"Em / Anh thấy …………… khi …………………………… vì …………………………… Em / Anh cần ……………………………"</p>
<h2>4. Tạm dừng và hàn gắn (tuần 4)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Tín hiệu dừng của nhà mình</th><td class="tall"></td></tr><tr><th>Quay lại sau</th><td>……… phút</td></tr>
<tr><th>Việc làm dịu của chồng / của vợ</th><td></td></tr><tr><th>Câu hàn gắn của chồng</th><td class="tall"></td></tr><tr><th>Câu hàn gắn của vợ</th><td class="tall"></td></tr>
</tbody></table></div>
<h2>5. Trước mặt con (tuần 5)</h2>
<p><strong>Câu nói mẫu:</strong> "Bố mẹ đang nghĩ khác nhau. Bố mẹ sẽ bàn và trả lời con sau ……………"</p>
<h2>6. Họp vợ chồng và kế hoạch đi công tác (tuần 6)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Giờ họp cố định</th><td></td></tr><tr><th>Cảm ơn (4')</th><td></td></tr><tr><th>Lịch tuần (4')</th><td></td></tr>
<tr><th>Chuyện con (5')</th><td></td></tr><tr><th>Một chuyện cần bàn (4')</th><td></td></tr><tr><th>Lúc riêng cho hai người (3')</th><td></td></tr>
<tr><th>Khi đi công tác: việc tạm bỏ, người đỡ, giờ gọi</th><td class="tall"></td></tr>
</tbody></table></div>
<h2>7. Phiếu tự đánh giá (tuần 1 và tuần 6)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 6</th></tr></thead><tbody>{srows}</tbody></table></div>
<p class="small muted">Có bạo lực: 113 (nguy hiểm tức thì) · 117 (phòng, chống bạo lực gia đình) · 111 (trẻ em).</p>
''', current='/cong-cu/')
print('G5 built')
