# Khóa G6 "Tiền nhà mình" – trang khóa, 12 bài, 2 công cụ in
import illus_g6  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/tien-nha-minh/'
TOOL_B = '/cong-cu/bang-thu-chi/'
TOOL_H = '/cong-cu/hu-ba-ngan/'
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

CFPB_BB = '<a href="https://www.consumerfinance.gov/consumer-tools/educator-tools/youth-financial-education/learn/">CFPB – các khối nền năng lực tài chính</a>'
CFPB_MAYG = '<a href="https://www.consumerfinance.gov/consumer-tools/money-as-you-grow/">CFPB – Money as You Grow</a>'
CFPB_SAVE = '<a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-announces-start-small-save-initiative">CFPB 2019 – Start Small, Save Up</a>'
KAISER = '<a href="https://repository.upenn.edu/prc_papers/676">Kaiser, Lusardi, Menkhoff &amp; Urban</a>'
BLDS = '<a href="https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam">Bộ luật Dân sự 2015, Điều 468</a>'
BLHS = '<a href="https://tapchitoaan.vn/huong-dan-ap-dung-dieu-201-cua-blhs-va-viec-xet-xu-vu-an-cho-vay-lai-nang">Bộ luật Hình sự 2015, Điều 201</a>'
BCA = '<a href="https://baovanhoa.vn/phap-luat/bo-cong-an-canh-bao-ve-bien-tuong-ung-dung-vay-tien-truc-tuyen-64234.html">cảnh báo của Bộ Công an (2020)</a>'
NOADVICE = ('<div class="box"><p><strong>Không phải tư vấn tài chính hay pháp lý.</strong> Khóa chỉ dạy thu chi cơ bản. '
            'Chúng tôi không tư vấn đầu tư, không giới thiệu khoản vay hay sản phẩm tài chính nào.</p></div>')
COINS = 'Con dưới 3 tuổi: không chơi với tiền xu, nắp chai nhỏ hay vật lọt lõi giấy vệ sinh. Dùng tiền giấy hoặc thẻ bìa to tự cắt.'

L = {
 '1a': (1, '1a-tien-di-dau', '1A', 'Tiền nhà mình đi đâu'),
 '1b': (1, '1b-tien-doi-lay-do', '1B', 'Tiền đổi lấy đồ'),
 '2a': (2, '2a-bang-thu-chi-thang', '2A', 'Bảng thu chi tháng'),
 '2b': (2, '2b-can-hay-muon', '2B', 'Cần hay muốn'),
 '3a': (3, '3a-quy-khan-cap', '3A', 'Quỹ khẩn cấp'),
 '3b': (3, '3b-hu-ba-ngan', '3B', 'Hũ ba ngăn'),
 '4a': (4, '4a-vay-an-toan', '4A', 'Vay an toàn, tránh tín dụng đen'),
 '4b': (4, '4b-muon-roi-tra', '4B', 'Mượn rồi trả'),
 '5a': (5, '5a-di-cho-co-ke-hoach', '5A', 'Đi chợ có kế hoạch'),
 '5b': (5, '5b-con-di-cho', '5B', 'Con đi chợ cùng bố mẹ'),
 '6a': (6, '6a-hop-tien-hang-thang', '6A', 'Họp tiền hằng tháng'),
 '6b': (6, '6b-ngan-chia-se', '6B', 'Ngăn Chia sẻ và con kể lại'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, meta, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'g6-' + k
    note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này đã soạn theo khung của khóa nhưng chưa được dạy thử trong gia đình. '
            f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn. '
             'Xin đừng ghi số tiền thật hay thông tin tài khoản.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về bài {code}</a></p></div>')
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Tiền nhà mình</a> · Tuần {w} · {code}</p>
<h1>{title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block('M' + code)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026 · Không phải tư vấn tài chính hay pháp lý</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/gia-dinh/')

A = ['Buổi bố mẹ', None, '30 phút']
B = ['Buổi cùng con', None, '15–20 phút']
def ma(w): return [A[0], f'Tuần {w}', A[2]]
def mb(w): return [B[0], f'Tuần {w}', B[2]]

# =============== TUẦN 1 ===============
lesson('1a', 'Khóa Tiền nhà mình, bài 1A: bố mẹ ghi tiền vào – tiền ra và ghi mọi khoản chi trong 7 ngày, không phán xét.', ma(1), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ viết ra <strong>tổng tiền vào</strong> và <strong>các khoản chi cố định</strong> mỗi tháng.',
   'Cả hai cùng <strong>ghi mọi khoản chi trong 7 ngày</strong>, kể cả khoản nhỏ.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In trang 1 của <a href="{TOOL_B}">Bảng thu chi</a>, hoặc dùng một cuốn sổ nhỏ.', 'Hóa đơn điện, nước, internet tháng trước nếu có.', 'Giờ yên tĩnh, con đã ngủ.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người đoán thầm: <em>"Tháng trước nhà mình tiêu cho ăn uống bao nhiêu?"</em> Ghi số đoán ra giấy. Cuối tuần so với số thật.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Tiền vào (5 phút).</strong> Ghi mọi nguồn tiền vào mỗi tháng: lương, bán hàng, làm thêm. Thu nhập không đều thì lấy tháng thấp nhất gần đây.',
   '<strong>Chi cố định (8 phút).</strong> Ghi các khoản tháng nào cũng phải trả: nhà, điện, nước, học phí, trả góp.',
   '<strong>Cách ghi 7 ngày (5 phút).</strong> Chọn một chỗ ghi duy nhất: sổ dán tủ lạnh hoặc ghi chú điện thoại. Ghi ngay sau khi trả tiền.',
   '<strong>Luật ghi (3 phút).</strong> Ghi hết, kể cả cốc cà phê. Không bình luận khoản chi của người kia trong 7 ngày này.',
   '<strong>Hẹn (4 phút).</strong> Chọn ngày ngồi lại sau 7 ngày, chính là buổi 2A.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Hồi nhỏ, nhà mình nói về tiền thế nào? Điều gì mình muốn giữ, điều gì muốn đổi?', 'Khoản chi nào làm mình hay lo nhất?', 'Mình muốn con lớn lên nghĩ về tiền ra sao?'])),
 sec(6, 'An toàn và ranh giới', ul(['Không ghi số tài khoản, mật khẩu hay mã OTP vào sổ chung.', 'Chuyện tiền dễ gây căng thẳng. Nếu bắt đầu cãi nhau, dừng lại, hẹn hôm khác.',
   'Nếu tiền bạc làm bạn lo âu kéo dài, mất ngủ, hãy nói với người thân tin cậy. Xem khối "Cần giúp ngay" bên dưới.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: sổ ghi, 20 phút. Bố ghi chi tiêu của mình khi đi công tác.', [
   ('Phút 0–10.', 'Mẹ ghi tiền vào và chi cố định. Chỗ chưa rõ thì đánh dấu hỏi bố.'),
   ('Phút 10–15.', 'Nhắn bố: cả hai cùng ghi 7 ngày, mỗi người một chỗ, cuối tuần gộp lại.'),
   ('Phút 15–20.', 'Mẹ dán sổ ghi ở chỗ dễ thấy.')], [
   ('Nhà một bố hoặc một mẹ:', 'tự làm là đủ. Ghi đều quan trọng hơn ghi đẹp.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tối:</strong> 1 phút xem lại sổ, bổ sung khoản quên.', '<strong>Sau 7 ngày:</strong> cộng tổng, so với số đoán ở phần mở đầu.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Phân tích gộp 76 thử nghiệm ngẫu nhiên, hơn 160.000 người: giáo dục tài chính cải thiện hiểu biết và hành vi tài chính ({KAISER}, bản 2020).'),
   lb('Suy luận', 'Các chương trình trong phân tích đó đa dạng; chưa có bằng chứng riêng cho khóa tự học này.'),
   lb('Đánh giá chuyên môn', 'Cách ghi 7 ngày không phán xét do daynentang.com thiết kế.')]))
])

lesson('1b', 'Khóa Tiền nhà mình, bài 1B: con hiểu tiền đổi lấy đồ và tiền đến từ lao động, qua trò chơi cửa hàng trong nhà.', mb(1), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn (khoảng 7 tuổi):</strong> trả đúng tiền cho 3 món trong trò cửa hàng; nói được "tiền đến từ đâu".',
   '<strong>Con nhỏ (khoảng 2 tuổi):</strong> đưa "tiền" và nhận đồ, nói hoặc làm động tác "cảm ơn".'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['4–5 đồ to trong nhà làm "hàng": quả cam, cốc nhựa, đồ chơi to.', 'Giấy nhỏ ghi giá: 1k, 2k, 5k.', 'Tiền giấy mệnh giá nhỏ cho con lớn; thẻ bìa to tự cắt cho con nhỏ.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Sáng nay bố đi làm. Cuối tháng công ty trả lương. Bố dùng lương mua gạo, sữa, sách cho con. Hôm nay mình mở cửa hàng nhé!"</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Con dán giá lên từng món. Bố mẹ làm khách trước, trả tiền, con đếm và đưa hàng.',
   'Đổi vai: con làm khách với 10k. Con chọn mua món nào để vừa đủ tiền?',
   'Hỏi: "Hết tiền thì sao?" Gợi ý: phải chờ đến khi có tiền, hoặc chọn món khác.',
   'Kể ngắn về công việc của bố mẹ: tiền là phần trả cho công sức lao động.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Con cầm thẻ bìa "tiền", đưa cho anh, nhận quả cam.', 'Cả nhà nói "cảm ơn" sau mỗi lần mua bán.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> cho con tính tiền thừa và ghi sổ bán hàng.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Tiền của nhà mình đến từ đâu?', 'Nếu con muốn mua mà không đủ tiền, con làm gì?', 'Con thấy ai trong nhà làm việc để có tiền?'])),
 sec(6, 'An toàn', ul([COINS, 'Rửa tay sau khi cầm tiền giấy thật.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 4 món hàng, giấy ghi giá, tiền giấy và thẻ bìa. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Mẹ kể bố đi làm để có lương.'),
   ('Phút 2–10 – Cửa hàng.', 'Con lớn bán, mẹ và con nhỏ mua. Đổi vai.'),
   ('Phút 10–15 – Trò chuyện.', 'Hỏi 3 câu ở mục 5.')], [
   ('Gọi video với bố:', 'bố kể 1 phút về công việc hôm nay.'), ('Nhắn bố 1 câu:', 'câu con trả lời "tiền đến từ đâu".')])),
 sec(8, 'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> khi đi chợ, cho con lớn đưa tiền và nhận tiền thừa.', '<strong>Sau 1 tuần:</strong> chơi lại cửa hàng, con tự đặt giá.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB: ở tuổi 3–5, giá trị và thái độ cơ bản về tiền bắt đầu hình thành, cùng kỹ năng đếm và con số ({CFPB_BB}).'),
   lb('Đánh giá chuyên môn', 'Trò cửa hàng trong nhà do daynentang.com thiết kế.')]))
])

# =============== TUẦN 2 ===============
lesson('2a', 'Khóa Tiền nhà mình, bài 2A: bố mẹ lập bảng thu chi tháng theo ba nhóm và áp dụng "để dành trước, tiêu sau".', ma(2), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ có <strong>bảng thu chi tháng</strong> chia ba nhóm: cần thiết, tiết kiệm và trả nợ, mong muốn.',
   'Chọn <strong>một khoản để dành cố định</strong>, chuyển ngay ngày nhận lương.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Sổ ghi chi 7 ngày từ bài 1A.', f'Trang 2 của <a href="{TOOL_B}">Bảng thu chi</a>.', 'Máy tính bỏ túi hoặc điện thoại.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>So số đoán ở bài 1A với số thật sau 7 ngày. Lệch nhiều hay ít? Không ai bị trách.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Phân loại (8 phút).</strong> Mỗi khoản trong 7 ngày đánh dấu C (cần thiết), M (mong muốn) hay T (tiết kiệm, trả nợ).',
   '<strong>Nhân lên tháng (5 phút).</strong> Ước chi một tháng: chi 7 ngày nhân khoảng 4, cộng chi cố định.',
   '<strong>So với tiền vào (4 phút).</strong> Tiền vào lớn hơn tiền ra thì còn để dành. Ngược lại, chọn 2 khoản M để giảm ngay.',
   '<strong>Để dành trước (5 phút).</strong> Chọn một số tiền nhỏ, chắc chắn làm được. Chuyển ngay ngày nhận lương, trước khi tiêu.',
   '<strong>Ghi bảng (3 phút).</strong> Điền bảng tháng. Dán ở chỗ hai người cùng xem.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Khoản M nào mình bỏ được mà không buồn?', 'Khoản nào tưởng là C nhưng thật ra là M?', 'Ai giữ bảng? Ai nhắc chuyển khoản để dành?'])),
 sec(6, 'An toàn và ranh giới', ul(['Không dùng bảng để soi xét chi tiêu cá nhân của người kia. Mỗi người có một khoản nhỏ tự quyết, không cần giải thích.',
   'Nếu tiền vào không đủ chi cần thiết, tìm hỗ trợ chính thức ở địa phương; đừng vay nóng để bù.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: sổ 7 ngày, bảng tháng, 20 phút.', [
   ('Phút 0–10.', 'Mẹ phân loại C, M, T và ước chi tháng.'),
   ('Phút 10–15.', 'Mẹ đề xuất số tiền để dành và 2 khoản M có thể giảm.'),
   ('Phút 15–20.', 'Gọi bố, chốt cùng nhau.')], [])),
 sec(8, 'Ôn lại', ul(['<strong>Ngày nhận lương:</strong> chuyển khoản để dành trước.', '<strong>Cuối tháng:</strong> so chi thật với bảng, mang vào buổi 6A.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB khuyến khích bắt đầu để dành từ khoản nhỏ và xây thói quen để dành đều ({CFPB_SAVE}).'),
   lb('Đánh giá chuyên môn', 'Chia ba nhóm và "để dành trước" là cách làm phổ biến trong giáo dục tài chính; tỉ lệ trong hình chỉ là ví dụ, không phải chuẩn.')]))
])

lesson('2b', 'Khóa Tiền nhà mình, bài 2B: con phân biệt "cần" và "muốn" bằng hai rổ tranh, và tập chờ trước khi mua.', mb(2), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> xếp đúng ít nhất 8/10 tranh vào rổ Cần hay Muốn; giải thích 2 lựa chọn.',
   '<strong>Con nhỏ:</strong> chờ 10 giây trước khi nhận đồ ăn vặt, khi bố mẹ đếm cùng.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['10 mẩu giấy vẽ hoặc cắt hình: gạo, nước, áo đi học, thuốc, kẹo, đồ chơi, bóng bay…', '2 cái rổ, dán nhãn CẦN và MUỐN.', 'Một tờ giấy "Danh sách chờ".'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Nếu nhà mình chỉ còn ít tiền, mình mua gạo hay mua kẹo trước?" Nghe con giải thích.</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Giải thích: Cần là thứ phải có để sống khỏe và đi học. Muốn là thứ thích nhưng có thể chờ.',
   'Con xếp 10 tranh vào hai rổ. Tranh nào khó, cả nhà bàn. Ví dụ: áo mới là cần hay muốn?',
   'Con viết một món mình đang muốn vào "Danh sách chờ". Hẹn sau 1 tuần hỏi lại.',
   'Bố mẹ cũng viết một món mình muốn vào danh sách.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Trò "chờ một chút": trước khi đưa miếng chuối, cả nhà đếm đến 10.', 'Con chờ được thì khen: "Con chờ giỏi quá!"']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> cho con xem một hóa đơn đi chợ thật và đánh dấu C hay M.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Tranh nào khó xếp nhất? Vì sao?', 'Chờ một món mình muốn, con thấy thế nào?', 'Bố mẹ có lúc nào phải chọn giữa cần và muốn không?'])),
 sec(6, 'An toàn', ul([COINS, 'Không để bóng bay xẹp hay mảnh bóng bay gần con nhỏ; chỉ dùng tranh vẽ bóng bay.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 10 tranh, 2 rổ, giấy. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi gạo hay kẹo.'), ('Phút 2–10 – Xếp tranh.', 'Con lớn xếp, cả nhà bàn tranh khó.'),
   ('Phút 10–13 – Danh sách chờ.', 'Con lớn và mẹ mỗi người viết 1 món.'), ('Phút 13–15 – Con nhỏ.', 'Trò đếm đến 10.')], [
   ('Nhắn bố 1 câu:', 'món con viết vào danh sách chờ.')])),
 sec(8, 'Ôn lại', ul(['<strong>Khi đi chợ:</strong> hỏi con "món này cần hay muốn?"', '<strong>Sau 1 tuần:</strong> mở danh sách chờ. Con còn muốn món đó không?'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB: chức năng điều hành (lập kế hoạch, tự kiểm soát) là khối nền đầu tiên của năng lực tài chính, bắt đầu hình thành ở tuổi 3–5 ({CFPB_BB}).'),
   lb('Đánh giá chuyên môn', 'Trò hai rổ và danh sách chờ do daynentang.com thiết kế.')]))
])

# =============== TUẦN 3 ===============
lesson('3a', 'Khóa Tiền nhà mình, bài 3A: bố mẹ bắt đầu quỹ khẩn cấp từ một khoản nhỏ, tách riêng và đặt luật dùng quỹ.', ma(3), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ chọn <strong>mốc quỹ đầu tiên</strong>, nhỏ và chắc chắn đạt được.', 'Quỹ <strong>tách riêng</strong> khỏi tiền tiêu và có <strong>luật dùng quỹ</strong> viết ra.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 3 của <a href="{TOOL_B}">Bảng thu chi</a>.', 'Bảng thu chi tháng từ bài 2A.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Hỏi nhau: <em>"Lần gần nhất nhà mình có việc bất ngờ cần tiền là khi nào? Mình đã xoay xở thế nào?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Mốc 1 (5 phút).</strong> Chọn một số tiền nhỏ có thể đạt trong 1–2 tháng.',
   '<strong>Các mốc sau (5 phút).</strong> Mốc 2: chi cần thiết của 1 tháng. Mốc 3: 3 tháng trở lên. Đây là gợi ý, không phải quy định.',
   '<strong>Tách riêng (5 phút).</strong> Để quỹ ở chỗ khác tiền tiêu hằng ngày, không mang theo người.',
   '<strong>Luật dùng quỹ (7 phút).</strong> Viết 3 câu hỏi trước khi dùng: Có bất ngờ không? Có thật sự cần không? Cả hai đồng ý chưa?',
   '<strong>Bù lại (3 phút).</strong> Dùng quỹ xong, tăng khoản để dành tháng sau để bù.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Việc gì nhà mình coi là "khẩn cấp"?', 'Ai được quyền dùng quỹ khi người kia đi vắng?', 'Nếu họ hàng hỏi vay, mình trả lời thế nào?'])),
 sec(6, 'An toàn và ranh giới', ul(['Không giữ nhiều tiền mặt ở nhà. Không chia sẻ mật khẩu, mã OTP cho bất kỳ ai, kể cả người tự xưng là ngân hàng hay công an.',
   'Khóa không tư vấn chọn ngân hàng hay sản phẩm tiết kiệm. Hãy hỏi trực tiếp tổ chức tài chính được cấp phép.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: bảng thu chi, 15 phút.', [
   ('Phút 0–8.', 'Mẹ đề xuất mốc 1 và nơi giữ quỹ.'), ('Phút 8–15.', 'Mẹ viết luật dùng quỹ, gửi bố đọc và đồng ý.')], [])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> tô thêm thanh tiến độ quỹ.', '<strong>Khi đạt mốc 1:</strong> cả nhà ăn mừng nhỏ, không tốn tiền.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB cho rằng ngay cả khoản tiết kiệm nhỏ cũng tạo khác biệt lớn khi có việc bất ngờ ({CFPB_SAVE}).'),
   lb('Đánh giá chuyên môn', 'Các mốc 1 tháng và 3 tháng là gợi ý thường gặp, không phải chuẩn bắt buộc. Mỗi nhà điều chỉnh theo thu nhập.')]))
])

lesson('3b', 'Khóa Tiền nhà mình, bài 3B: con làm hũ ba ngăn Tiết kiệm – Tiêu – Chia sẻ và vẽ thanh mục tiêu.', mb(3), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> tự chia tiền vào 3 hũ và tô thanh mục tiêu cho một món muốn mua.',
   '<strong>Con nhỏ:</strong> bỏ thẻ bìa "tiền" vào đúng hũ có hình con chọn.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['3 hũ hoặc hộp nhựa có nắp, cắt khe to.', f'Nhãn hũ in từ <a href="{TOOL_H}">Hũ ba ngăn</a>, hoặc tự vẽ.', 'Một ít tiền giấy mệnh giá nhỏ cho con lớn.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Mỗi lần có tiền, mình chia làm ba: một phần để dành, một phần tiêu, một phần giúp người khác."</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Con dán nhãn ba hũ: Tiết kiệm, Tiêu, Chia sẻ. Con trang trí tùy thích.',
   'Bố mẹ và con chọn cách chia, ví dụ cứ 3 tờ thì mỗi hũ 1 tờ.',
   'Con vẽ món muốn mua và thanh mục tiêu 5 ô. Mỗi lần bỏ hũ Tiết kiệm, tô một ô.',
   'Thống nhất tiền vào hũ từ đâu: tiền mừng, tiền thưởng nhỏ. Không trả tiền cho việc nhà của chính con.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Con bỏ thẻ bìa "tiền" vào hũ theo hình bố mẹ chỉ.', 'Đếm cùng con: một, hai, ba.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con tự đặt tỉ lệ chia và ghi sổ ba hũ.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Hũ nào con muốn đầy nhất? Vì sao?', 'Bao lâu nữa con đủ tiền cho món muốn mua?', 'Con muốn dùng hũ Chia sẻ cho ai?'])),
 sec(6, 'An toàn', ul([COINS, 'Hũ thủy tinh dễ vỡ: dùng hộp nhựa. Cất hũ ở chỗ con nhỏ không tự mở được.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 3 hộp nhựa, nhãn, tiền giấy, thẻ bìa. Tổng 15 phút.', [
   ('Phút 0–3 – Mở đầu.', 'Giải thích chia ba.'), ('Phút 3–9 – Làm hũ.', 'Con lớn dán nhãn, trang trí.'),
   ('Phút 9–13 – Thanh mục tiêu.', 'Con lớn vẽ món muốn mua.'), ('Phút 13–15 – Con nhỏ.', 'Bỏ thẻ bìa vào hũ.')], [
   ('Nhắn bố 1 câu:', 'món con muốn để dành mua.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi lần con có tiền:</strong> chia ba hũ ngay.', '<strong>Sau 1 tuần:</strong> đếm hũ cùng con, tô thanh mục tiêu.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB: ở tuổi 6–12, thói quen và chuẩn mực về tiền "thật sự hình thành", trẻ học các khái niệm quản lý tiền cơ bản ({CFPB_BB}).'),
   lb('Đánh giá chuyên môn', 'Có hay không trả tiền cho việc nhà là lựa chọn của mỗi nhà; bằng chứng chưa rõ. Khóa gợi ý giữ việc nhà là trách nhiệm chung.'),
   lb('Đánh giá chuyên môn', 'Hũ ba ngăn là công cụ phổ biến; cách dùng trong bài do daynentang.com thiết kế.')]))
])

# =============== TUẦN 4 ===============
lesson('4a', 'Khóa Tiền nhà mình, bài 4A: bố mẹ liệt kê khoản nợ, hiểu trần lãi suất theo luật và nhận diện tín dụng đen, app vay biến tướng.', ma(4), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ có <strong>danh sách mọi khoản nợ</strong>: còn bao nhiêu, lãi bao nhiêu, trả ngày nào.',
   'Cả hai nói được <strong>4 dấu hiệu tín dụng đen</strong> và việc cần làm khi bị đe dọa.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 4 của <a href="{TOOL_B}">Bảng thu chi</a>.', 'Hợp đồng vay, sao kê trả góp nếu có.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Hỏi nhau: <em>"Nhà mình đang nợ ai, bao nhiêu? Có khoản nào mình chưa nói với nhau không?"</em> Nói thật, không trách.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Danh sách nợ (8 phút).</strong> Ghi từng khoản: người cho vay, số còn nợ, lãi suất theo năm, số trả mỗi tháng, ngày đến hạn.',
   '<strong>Đổi lãi ra năm (5 phút).</strong> Lãi tính theo ngày hay tháng thì nhân lên năm để so. Ví dụ 3%/tháng là khoảng 36%/năm.',
   '<strong>Trần lãi suất (4 phút).</strong> Vay giữa người với người, lãi thỏa thuận không vượt 20%/năm, trừ khi luật khác quy định khác. Phần vượt không có hiệu lực.',
   '<strong>Dấu hiệu tín dụng đen (5 phút).</strong> Lãi, phí không ghi rõ; không có tên công ty, địa chỉ; đòi đọc danh bạ; dọa, bôi nhọ khi trả chậm.',
   '<strong>Luật nhà mình (3 phút).</strong> Không vay để trả khoản vay khác. Không vay qua app lạ. Mọi khoản vay mới phải cả hai đồng ý.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Khoản nợ nào lãi cao nhất? Có thể trả trước khoản đó không?', 'Nếu người thân nhờ đứng tên vay, mình trả lời thế nào?', 'Khi bị gọi điện đòi nợ đe dọa, ai làm gì?'])),
 sec(6, 'An toàn và ranh giới', ul(['Bị đe dọa, bôi nhọ khi đòi nợ: giữ lại bằng chứng (tin nhắn, ghi âm, ảnh chụp) và trình báo công an nơi gần nhất. Nguy hiểm tức thì gọi <strong>113</strong>.',
   'Không cung cấp mã OTP, ảnh căn cước, quyền đọc danh bạ cho app hay người lạ.',
   'Đây là thông tin cơ bản, không phải tư vấn pháp lý. Với khoản nợ lớn hay tranh chấp, hỏi luật sư hoặc trợ giúp pháp lý của Nhà nước.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: danh sách nợ, 20 phút.', [
   ('Phút 0–10.', 'Mẹ ghi các khoản nợ mẹ biết; chỗ chưa rõ đánh dấu hỏi bố.'),
   ('Phút 10–15.', 'Mẹ đọc 4 dấu hiệu tín dụng đen.'), ('Phút 15–20.', 'Gọi bố, bổ sung danh sách và chốt luật nhà mình.')], [])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> cập nhật số còn nợ trong buổi 6A.', '<strong>Khi thấy quảng cáo vay "dễ, nhanh, không cần giấy tờ":</strong> đọc lại 4 dấu hiệu.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{BLDS}: lãi suất thỏa thuận không vượt 20%/năm của khoản vay, trừ khi luật liên quan quy định khác; phần vượt không có hiệu lực. Bộ luật số 91/2015/QH13, hiệu lực từ 01/01/2017; vay tại tổ chức tín dụng theo luật riêng. Tra cứu 28/10/2026.'),
   lb('Đã xác nhận', f'{BLHS} quy định tội cho vay lãi nặng: lãi suất gấp 5 lần mức cao nhất trong Bộ luật Dân sự, kèm điều kiện về số tiền thu lợi bất chính.'),
   lb('Cần kiểm chứng', 'Luật số 86/2025/QH15 sửa đổi Bộ luật Hình sự (hiệu lực 01/07/2025) có thay đổi mức phạt của Điều 201 hay không: chúng tôi chưa đọc được văn bản gốc. Vì vậy bài không nêu mức phạt.'),
   lb('Đã xác nhận', f'Dấu hiệu app vay biến tướng theo {BCA}: lãi, phí không rõ; thiếu thông tin doanh nghiệp; đòi nợ bằng đe dọa, bôi nhọ.')]))
])

lesson('4b', 'Khóa Tiền nhà mình, bài 4B: con hiểu mượn thì phải trả, và tiền lãi là giá của việc dùng đồ người khác.', mb(4), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> giải thích "tiền lãi" bằng trò mượn sao; trả lại đồ mượn đúng hẹn trong tuần.',
   '<strong>Con nhỏ:</strong> trả lại đồ chơi đã mượn khi được nhắc một lần.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['10 ngôi sao giấy hoặc 10 khối Duplo to.', 'Một món đồ chơi của anh để em mượn.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>"Hôm qua bố mượn bút của bạn. Bố phải làm gì với cây bút đó?" Nghe con trả lời.</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Trò mượn sao: con mượn bố 5 sao để "mua" một món ở cửa hàng bài 1B.',
   'Bố đặt luật: "Tuần sau con trả 6 sao." Hỏi: "Sao thêm là gì?" Giải thích đó là tiền lãi.',
   'Đổi luật: "Nếu trả 10 sao thì sao?" Con thấy mượn kiểu đó có lợi không?',
   'Kết luận ngắn: vay thì phải trả, thường phải trả thêm. Vay ít, vay của người đàng hoàng, và trả đúng hẹn.',
   'Nối với lời hứa: mượn đồ của bạn ở trường cũng phải trả đúng hẹn.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Em mượn đồ chơi của anh: "Chơi xong trả anh nhé."', 'Sau 2 phút nhắc một lần. Em trả, cả nhà vỗ tay.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> tính cùng con: vay 100 nghìn, lãi 3%/tháng, sau một năm trả bao nhiêu tiền lãi.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Vì sao người cho mượn lại muốn nhận thêm?', 'Nếu không trả đúng hẹn thì lần sau thế nào?', 'Mua bằng tiền để dành và mua bằng tiền vay, cách nào nhẹ nhõm hơn?'])),
 sec(6, 'An toàn', ul([COINS, 'Không kể chi tiết nợ của gia đình làm con lo lắng. Nói ở mức con hiểu, giọng bình tĩnh.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 10 ngôi sao giấy, 1 đồ chơi. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi về cây bút mượn.'), ('Phút 2–10 – Mượn sao.', 'Con lớn mượn 5, trả 6. Hỏi về sao thêm.'),
   ('Phút 10–15 – Con nhỏ.', 'Em mượn đồ của anh và trả.')], [('Nhắn bố 1 câu:', 'con giải thích tiền lãi thế nào.')])),
 sec(8, 'Ôn lại', ul(['<strong>Trong tuần:</strong> con trả 6 sao cho bố đúng hẹn.', '<strong>Sau 1 tuần:</strong> hỏi con "tiền lãi là gì?"'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB: kiến thức và kỹ năng ra quyết định tài chính, như hiểu vay nợ, trở nên quan trọng hơn ở tuổi 13–21; tuổi nhỏ chỉ cần khái niệm cơ bản ({CFPB_BB}).'),
   lb('Đánh giá chuyên môn', 'Trò mượn sao do daynentang.com thiết kế, nối với bài G10 "Giữ lời hứa nhỏ" của khóa Gia đình 2–8.')]))
])

# =============== TUẦN 5 ===============
lesson('5a', 'Khóa Tiền nhà mình, bài 5A: bố mẹ lên thực đơn tuần, viết danh sách đi chợ, so giá theo đơn vị và chờ trước món mua lớn.', ma(5), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ có <strong>thực đơn 7 ngày</strong> và <strong>danh sách đi chợ</strong> kèm số tiền mang theo.', 'Áp dụng luật <strong>chờ trước món mua lớn</strong>.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Bảng thu chi tháng, phần chi ăn uống.', 'Giấy, bút. Tủ lạnh đã kiểm tra còn gì.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Nhìn sổ 7 ngày bài 1A: <em>"Bao nhiêu lần mình mua đồ ăn ngoài kế hoạch?"</em></p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Thực đơn (8 phút).</strong> Viết bữa chính 7 ngày. Dùng lại món đơn giản. Một nguyên liệu dùng cho hai món.',
   '<strong>Danh sách (6 phút).</strong> Chỉ ghi thứ còn thiếu. Ghi số lượng.',
   '<strong>Số tiền mang theo (3 phút).</strong> Ước tổng, mang vừa đủ. Món ngoài danh sách: ghi lại, tuần sau xét.',
   '<strong>So giá theo đơn vị (4 phút).</strong> Chia giá cho số gam hay ml. Hộp to thường rẻ hơn, nhưng không phải luôn luôn, và chỉ đáng mua khi dùng hết.',
   '<strong>Luật chờ (4 phút).</strong> Món mua lớn ngoài kế hoạch: chờ vài ngày, hỏi lại hai người rồi mới mua.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Bữa nào hay ăn ngoài vì mệt? Có món dự phòng nào nấu nhanh?', 'Mình mua theo khuyến mãi bao nhiêu lần rồi bỏ phí?', 'Món mua lớn nào mình đang muốn? Đã chờ chưa?'])),
 sec(6, 'An toàn và ranh giới', ul(['Thực phẩm cho con nhỏ: cắt nhỏ, bỏ hạt cứng; tránh nho nguyên quả, hạt nguyên cho trẻ dưới 4 tuổi.', 'Tiết kiệm không có nghĩa bớt bữa ăn đủ chất của con.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: giấy, bút, 20 phút.', [
   ('Phút 0–10.', 'Mẹ viết thực đơn 7 ngày, ưu tiên món nhanh.'), ('Phút 10–20.', 'Mẹ viết danh sách và số tiền mang theo.')], [
   ('Bố ở xa:', 'gửi ảnh danh sách cho bố; bố góp ý một món con thích.')])),
 sec(8, 'Ôn lại', ul(['<strong>Sau mỗi lần đi chợ:</strong> so số tiêu với số mang theo.', '<strong>Sau 1 tuần:</strong> tổng chi ăn uống tuần này so với tuần trong bài 1A.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Thực đơn tuần, danh sách và so giá theo đơn vị là kỹ năng thực hành phổ biến; chúng tôi chưa tìm nghiên cứu riêng về hiệu quả tiết kiệm.'),
   lb('Đánh giá chuyên môn', 'Luật chờ trước món mua lớn do daynentang.com đề xuất; số ngày chờ do mỗi nhà chọn.')]))
])

lesson('5b', 'Khóa Tiền nhà mình, bài 5B: con đi chợ cùng bố mẹ với danh sách tranh và một ngân sách nhỏ.', mb(5), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> mua 2 món trong danh sách với ngân sách nhỏ, so giá 2 món, tự kiểm tra tiền thừa.',
   '<strong>Con nhỏ:</strong> tìm và chỉ đúng 2 món trong danh sách tranh.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Danh sách tranh từ <a href="{TOOL_H}">Hũ ba ngăn</a> (trang có danh sách đi chợ), hoặc tự vẽ 3–4 món.', 'Một khoản nhỏ tiền giấy cho con lớn, đựng trong ví riêng.', 'Xe đẩy hoặc địu cho con nhỏ.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Ở nhà, trước khi đi: "Hôm nay con là người giữ danh sách. Mình chỉ mua thứ có trong danh sách."</p>'),
 sec(4, 'Hoạt động chính (ở chợ hoặc siêu thị)', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   'Con đọc danh sách, tìm món, đánh dấu khi đã mua.',
   'Với một món, con so 2 loại: loại nào rẻ hơn tính theo gói? Bố mẹ giúp chia.',
   'Con dùng ngân sách nhỏ mua 2 món cần cho bữa tối. Con tự đưa tiền, tự đếm tiền thừa.',
   'Con xin món ngoài danh sách: "Mình ghi vào danh sách chờ nhé."',
   'Về nhà: tiền dư của con bỏ vào hũ Tiết kiệm.']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Con ngồi xe đẩy, cầm danh sách tranh.', 'Thấy món trong tranh, con chỉ và gọi tên.']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con tự lập danh sách cho một bữa và giữ đúng ngân sách.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Món nào con so giá? Con chọn loại nào, vì sao?', 'Có khó khi không mua món ngoài danh sách không?', 'Con còn dư bao nhiêu? Con bỏ vào hũ nào?'])),
 sec(6, 'An toàn', ul(['Chợ đông, xe máy: con nhỏ ngồi xe đẩy hoặc được bế; con lớn nắm tay hoặc đi sát. Hẹn trước chỗ đứng chờ nếu lạc.', COINS,
   'Không cho con nếm thử đồ chưa rửa.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: danh sách tranh, ví nhỏ cho con lớn, xe đẩy. Đi chợ gần, tổng 20 phút.', [
   ('Trước khi đi.', 'Giao con lớn giữ danh sách và ví.'), ('Ở chợ.', 'Con lớn tìm món và trả tiền; con nhỏ chỉ tranh.'),
   ('Về nhà.', 'Con lớn bỏ tiền dư vào hũ, kể lại.')], [
   ('Nếu đi với hai con quá mệt:', 'chỉ làm phần danh sách tranh trong siêu thị nhỏ, hoặc để bài này cho cuối tuần khi bố về.'),
   ('Nhắn bố 1 câu:', 'con tự trả tiền món gì.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi lần đi chợ:</strong> con giữ danh sách.', '<strong>Sau 1 tuần:</strong> con lập danh sách cho một bữa sáng.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB gợi ý dùng các việc thường ngày như đi mua sắm để dạy con về tiền ({CFPB_MAYG}).'),
   lb('Đánh giá chuyên môn', 'Ngân sách nhỏ và danh sách tranh do daynentang.com thiết kế.')]))
])

# =============== TUẦN 6 ===============
lesson('6a', 'Khóa Tiền nhà mình, bài 6A: bố mẹ họp tiền 20 phút mỗi tháng và chấm phiếu tự đánh giá cuối khóa.', ma(6), [
 sec(1, 'Mục tiêu', ul(['Bố mẹ chốt <strong>ngày họp tiền cố định</strong> mỗi tháng và làm buổi họp đầu tiên.', 'Chấm <strong>phiếu tự đánh giá</strong> cuối khóa, so với tuần 1.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Bảng thu chi tháng, quỹ khẩn cấp, danh sách nợ (<a href="{TOOL_B}">Bảng thu chi</a>).', 'Phiếu tự đánh giá đã chấm ở tuần 1.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Mỗi người nói một điều về tiền mà sáu tuần qua mình làm tốt hơn.</p>'),
 sec(4, 'Hoạt động chính (25 phút)', ol([
   '<strong>Xem bảng (5 phút).</strong> Chi thật so với bảng tháng. Khoản nào vượt?',
   '<strong>Quỹ (4 phút).</strong> Quỹ khẩn cấp đến mốc nào? Tô thanh tiến độ.',
   '<strong>Nợ (4 phút).</strong> Còn bao nhiêu? Khoản lãi cao nhất đã giảm chưa?',
   '<strong>Tháng tới (4 phút).</strong> Một việc cần sửa, một khoản lớn sắp tới (học phí, đám cưới, Tết).',
   '<strong>Khen (3 phút).</strong> Mỗi người khen người kia một việc cụ thể.',
   '<strong>Đánh giá cuối khóa (5 phút).</strong> Chấm phiếu tự đánh giá, ghi 3 dòng nhật ký.'])),
 sec(5, 'Câu hỏi bố mẹ hỏi nhau', ol(['Ngày nào trong tháng hợp nhất để họp tiền?', 'Phần nào của khóa mình muốn giữ lâu dài?', 'Con đã thay đổi gì về cách nói chuyện tiền?'])),
 sec(6, 'An toàn và ranh giới', ul(['Họp tiền nói về con số, không trách người.', 'Nếu một người kiểm soát hết tiền và không cho người kia biết hay dùng, đó là dấu hiệu cần nói chuyện nghiêm túc, có thể cần người hỗ trợ bên ngoài.'])),
 sec(7, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: các bảng, 20 phút. Bố gọi video.', [
   ('Phút 0–10.', 'Mẹ chuẩn bị số liệu: bảng tháng, quỹ, nợ.'), ('Phút 10–20.', 'Gọi video với bố đi qua 5 phần.')], [])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> họp tiền đúng ngày.', '<strong>Sau 3 tháng:</strong> chấm lại phiếu tự đánh giá.'])),
 sec(9, 'Nhật ký sau buổi', J_A),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Buổi họp tiền 20 phút với 5 phần do daynentang.com thiết kế, chưa có nghiên cứu riêng.'),
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước – sau 6 tuần không có nhóm đối chứng; đây là thử nghiệm khả thi, không phải bằng chứng hiệu quả.')]))
])

lesson('6b', 'Khóa Tiền nhà mình, bài 6B: con chọn cách dùng ngăn Chia sẻ và kể lại ba điều đã học về tiền.', mb(6), [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> chọn và làm 1 việc với hũ Chia sẻ; kể lại 3 điều về tiền bằng lời của mình.',
   '<strong>Con nhỏ:</strong> trao món quà nhỏ cho người được chọn.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Hũ ba ngăn của con.', 'Giấy vẽ thiệp nếu con chọn tặng quà.'])),
 sec(3, 'Mở đầu (2 phút)', '<p>Đếm hũ Chia sẻ cùng con: "Con muốn dùng phần này để làm ai vui?"</p>'),
 sec(4, 'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Con chọn: quà nhỏ cho ông bà, góp giúp một bạn khó khăn qua trường, mua sách tặng thư viện lớp.',
   'Cùng con làm việc đó trong tuần. Con vẽ thiệp kèm theo.',
   'Con kể lại 3 điều: tiền đến từ đâu, cần và muốn, chia ba hũ.',
   'Nếu nhà có họp gia đình (khóa Giá trị nhà mình), con kể trong phần Cảm ơn.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Con tô thiệp cùng anh.', 'Con trao quà và nói hoặc làm động tác "tặng bà".']) +
   '<p class="small"><strong>Con từ 10 tuổi trở lên:</strong> con tự tìm hiểu một nơi cần giúp và đề xuất cho cả nhà.</p>'),
 sec(5, 'Câu hỏi trò chuyện', ol(['Khi tặng quà bằng tiền của mình, con thấy thế nào?', 'Điều nào về tiền con thấy quan trọng nhất?', 'Con muốn để dành cho mục tiêu gì tiếp theo?'])),
 sec(6, 'An toàn', ul(['Góp tiền qua trường hay tổ chức quen biết; không chuyển tiền cho lời kêu gọi lạ trên mạng.', COINS])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: hũ Chia sẻ, giấy vẽ thiệp. Tổng 15 phút.', [
   ('Phút 0–3 – Đếm hũ.', 'Hỏi con muốn làm ai vui.'), ('Phút 3–10 – Vẽ thiệp.', 'Hai con cùng vẽ.'),
   ('Phút 10–15 – Kể lại.', 'Con lớn kể 3 điều về tiền.')], [('Nhắn bố 1 câu:', 'con chọn dùng hũ Chia sẻ cho ai.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> đếm ba hũ cùng con.', '<strong>Sau 3 tháng:</strong> con đã đạt thanh mục tiêu chưa? Đặt mục tiêu mới.'])),
 sec(9, 'Nhật ký sau buổi', J_B),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CFPB: thói quen và chuẩn mực về tiền của trẻ hình thành qua những gì trẻ thấy và làm hằng ngày trong gia đình ({CFPB_BB}).'),
   lb('Đánh giá chuyên môn', 'Ngăn Chia sẻ gắn với giá trị tử tế và biết ơn trong khóa Gia đình 2–8; bài do daynentang.com thiết kế.')]))
])

# =============== TRANG KHÓA ===============
def wk(w, a, b, goal):
    return f'<tr><td>{w}</td><td><a href="{link(a)[0]}">{L[a][3]}</a></td><td><a href="{link(b)[0]}">{L[b][3]}</a></td><td>{goal}</td></tr>'
rows = (wk(1, '1a', '1b', 'Ghi đủ chi tiêu 7 ngày') + wk(2, '2a', '2b', 'Có bảng thu chi tháng; con xếp đúng ≥8/10 tranh') +
        wk(3, '3a', '3b', 'Quỹ khẩn cấp có mốc 1; con có hũ ba ngăn') + wk(4, '4a', '4b', 'Danh sách nợ đủ; nói được 4 dấu hiệu tín dụng đen') +
        wk(5, '5a', '5b', 'Đi chợ theo danh sách ≥1 lần/tuần') + wk(6, '6a', '6b', 'Họp tiền tháng đầu tiên; chấm phiếu cuối khóa'))
page(U, 'Tiền nhà mình',
 'Khóa 6 tuần miễn phí cho bố mẹ: ghi thu chi, lập bảng tháng, xây quỹ khẩn cấp, tránh tín dụng đen, đi chợ có kế hoạch, dạy con về tiền.',
f'''
<p class="eyebrow">Gia đình · Khóa G6 · Đang thử nghiệm</p>
<h1>Tiền nhà mình</h1>
<p class="lead">Bố mẹ biết tiền đi đâu, có kế hoạch và một khoản dự phòng. Con học tiền đến từ lao động, cần trước muốn sau, và chia ba hũ.</p>

<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Thu chi rõ ràng, có quỹ khẩn cấp, tránh vay nặng lãi; con có thói quen tiền đầu đời</td></tr>
<tr><th>Dành cho</th><td>Bố mẹ, người chăm sóc trẻ từ 2 tuổi. Bài cùng con có gợi ý cho con 2 tuổi, 7 tuổi và từ 10 tuổi</td></tr>
<tr><th>Thời lượng</th><td>6 tuần. Mỗi tuần 1 buổi bố mẹ (30 phút) và 1 buổi cùng con (15–20 phút)</td></tr>
<tr><th>Cần có</th><td>Sổ hoặc giấy, bút, 3 hộp nhựa. Trẻ không cần màn hình</td></tr>
<tr><th>Tình trạng</th><td>Đủ 6 tuần, bản chưa dạy thử, sẽ sửa theo nhật ký dạy thật</td></tr>
</tbody></table></div>
{NOADVICE}

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Biết chính xác 7 ngày qua tiền đi đâu.</li><li>Có bảng thu chi tháng và một khoản để dành đầu tiên.</li><li>Con phân biệt được cần và muốn.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: để dành trước, tiêu sau.</li><li>Kỹ năng: ghi chép, quỹ khẩn cấp, nhận diện tín dụng đen.</li><li>Nếp họp tiền hằng tháng; con có hũ ba ngăn.</li></ul></div>
</div>

<h2>Sáu tuần, sáu bước</h2>
{figure_block('KHOAM')}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Buổi bố mẹ (30')</th><th>Buổi cùng con (15–20')</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul>
<li><a href="{TOOL_B}">Bảng thu chi</a>: ghi chi 7 ngày, bảng tháng, quỹ khẩn cấp, danh sách nợ, phiếu tự đánh giá.</li>
<li><a href="{TOOL_H}">Hũ ba ngăn</a>: nhãn hũ, thanh mục tiêu, tranh cần – muốn, danh sách đi chợ có tranh.</li>
</ul>
<p class="small muted">Công cụ chỉ để in. Trang không lưu số tiền của bạn.</p>

<h2>Theo dõi tiến bộ</h2>
<p>Chấm phiếu tự đánh giá ở đầu tuần 1 và cuối tuần 6: 0 = chưa có, 1 = có nhưng chưa đều, 2 = đều đặn.</p>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{CFPB_BB}; {CFPB_MAYG}</td><td>Ba khối nền theo tuổi; dạy tiền qua việc hằng ngày</td><td><span class="label">[Đã xác nhận]</span> Khung của cơ quan bảo vệ người tiêu dùng tài chính Hoa Kỳ, dựa trên tổng quan nghiên cứu</td></tr>
<tr><td>{CFPB_SAVE}</td><td>Bắt đầu để dành từ khoản nhỏ</td><td><span class="label">[Đã xác nhận]</span> Khuyến nghị cơ quan nhà nước (2019)</td></tr>
<tr><td>{KAISER}</td><td>Giáo dục tài chính có ích</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp 76 thử nghiệm ngẫu nhiên, hơn 160.000 người</td></tr>
<tr><td>{BLDS}; {BLHS}</td><td>Trần lãi suất, nhận diện cho vay nặng lãi</td><td><span class="label">[Đã xác nhận]</span> Văn bản pháp luật Việt Nam, tra cứu 28/10/2026</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các thử nghiệm giáo dục tài chính chủ yếu làm với người lớn ở nước khác, theo nhóm, có người hướng dẫn.
  Khóa tự học này chưa được thử. Chúng tôi không hứa nhà bạn sẽ dư tiền; thu nhập quá thấp cần hỗ trợ khác ngoài kỹ năng.</p>
</div>

<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai. Xin đừng ghi số tiền thật hay thông tin tài khoản.</p>

<h2>An toàn cho mọi buổi</h2>
<ul>
<li>{COINS}</li>
<li>Không chia sẻ mật khẩu, mã OTP, ảnh căn cước cho ai. Ngân hàng và công an không hỏi mã OTP qua điện thoại.</li>
<li>Bị đe dọa đòi nợ: giữ bằng chứng, trình báo công an. Nguy hiểm tức thì gọi 113.</li>
</ul>
{HELP_BOX}
''', current='/gia-dinh/')

# =============== CÔNG CỤ ===============
days = ''.join(f'<tr><td class="tall"></td><td></td><td></td><td></td></tr>' for _ in range(12))
def rows_n(n, cols): return ''.join('<tr>' + '<td class="tall"></td>' + '<td></td>' * (cols - 1) + '</tr>' for _ in range(n))
SELF = ['Biết tổng tiền vào và chi cố định mỗi tháng', 'Có bảng thu chi tháng, cả hai cùng xem', 'Để dành trước khi tiêu, mỗi tháng',
        'Có quỹ khẩn cấp tách riêng', 'Có danh sách nợ, không vay qua app lạ', 'Đi chợ theo danh sách', 'Con có hũ ba ngăn', 'Họp tiền mỗi tháng']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)
page(TOOL_B, 'Bảng thu chi', 'Bảng in cho khóa Tiền nhà mình: ghi chi 7 ngày, bảng thu chi tháng, quỹ khẩn cấp, danh sách nợ, phiếu tự đánh giá.',
f'''
<h1>Bảng thu chi</h1>
<p>Dùng cho khóa <a href="{U}">Tiền nhà mình</a>. Chỉ để in, trang không lưu số tiền của bạn. Không ghi số tài khoản hay mật khẩu.</p>
{PRINT_ROW}
<h2>1. Ghi chi 7 ngày (tuần 1)</h2>
<div class="table-wrap"><table><thead><tr><th>Ngày</th><th>Chi cho gì</th><th>Số tiền</th><th>C / M / T</th></tr></thead><tbody>{days}</tbody></table></div>
<p class="small muted">C = cần thiết · M = mong muốn · T = tiết kiệm, trả nợ. Phân loại ở tuần 2.</p>
<h2>2. Bảng thu chi tháng (tuần 2)</h2>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Dự tính</th><th>Thực tế</th></tr></thead><tbody>
<tr><td><strong>Tiền vào</strong></td><td></td><td></td></tr>
<tr><td>Để dành trước (chuyển ngày nhận lương)</td><td></td><td></td></tr>
<tr><td>Trả nợ</td><td></td><td></td></tr>
<tr><td>Nhà, điện, nước, internet</td><td></td><td></td></tr>
<tr><td>Ăn uống, đi chợ</td><td></td><td></td></tr>
<tr><td>Học, sách vở của con</td><td></td><td></td></tr>
<tr><td>Đi lại, xăng xe</td><td></td><td></td></tr>
<tr><td>Sức khỏe, thuốc</td><td></td><td></td></tr>
<tr><td>Hiếu hỉ, biếu ông bà</td><td></td><td></td></tr>
<tr><td>Mong muốn (ăn ngoài, mua sắm)</td><td></td><td></td></tr>
<tr><td><strong>Tổng tiền ra</strong></td><td></td><td></td></tr>
</tbody></table></div>
<h2>3. Quỹ khẩn cấp (tuần 3)</h2>
<div class="table-wrap"><table><thead><tr><th>Mốc</th><th>Số tiền mục tiêu</th><th>Ngày đạt</th></tr></thead><tbody>
<tr><td>Mốc 1: khoản nhỏ</td><td></td><td></td></tr><tr><td>Mốc 2: 1 tháng chi cần thiết</td><td></td><td></td></tr><tr><td>Mốc 3: 3 tháng trở lên</td><td></td><td></td></tr></tbody></table></div>
<p><strong>Luật dùng quỹ:</strong> Có bất ngờ không? · Có thật sự cần không? · Cả hai đồng ý chưa? · Dùng xong thì bù lại.</p>
<h2>4. Danh sách nợ (tuần 4)</h2>
<div class="table-wrap"><table><thead><tr><th>Vay của ai</th><th>Còn nợ</th><th>Lãi %/năm</th><th>Trả mỗi tháng</th><th>Ngày hạn</th></tr></thead><tbody>{rows_n(5, 5)}</tbody></table></div>
<p class="small muted">Lãi theo tháng nhân 12 để ra lãi theo năm. Vay giữa người với người, lãi thỏa thuận không vượt 20%/năm (Bộ luật Dân sự 2015, Điều 468).</p>
<h2>5. Phiếu tự đánh giá (tuần 1 và tuần 6)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 6</th></tr></thead><tbody>{srows}</tbody></table></div>
<p class="small muted">Không phải tư vấn tài chính hay pháp lý.</p>
''', current='/cong-cu/')

jars = ''.join(f'<td class="tall"><h3>{n}</h3><br><span class="small">{d}</span></td>' for n, d in
               [('TIẾT KIỆM', 'Để dành cho mục tiêu'), ('TIÊU', 'Dùng cho món nhỏ'), ('CHIA SẺ', 'Tặng, giúp người khác')])
CM = ['Gạo', 'Nước uống', 'Áo đi học', 'Thuốc khi ốm', 'Sách vở', 'Kẹo', 'Đồ chơi mới', 'Bóng bay', 'Kem', 'Áo siêu nhân']
cmrows = ''.join('<tr>' + ''.join(f'<td class="tall">{x}</td>' for x in CM[i:i+5]) + '</tr>' for i in (0, 5))
page(TOOL_H, 'Hũ ba ngăn', 'Trang in cho con: nhãn ba hũ Tiết kiệm – Tiêu – Chia sẻ, thanh mục tiêu, tranh cần và muốn, danh sách đi chợ.',
f'''
<h1>Hũ ba ngăn</h1>
<p>Dùng cho khóa <a href="{U}">Tiền nhà mình</a>. In, cắt và dán. Con vẽ thêm hình tùy thích.</p>
{PRINT_ROW}
<h2>1. Nhãn ba hũ (tuần 3)</h2>
<div class="table-wrap"><table><tbody><tr>{jars}</tr></tbody></table></div>
<h2>2. Thanh mục tiêu của con</h2>
<p>Món con muốn: ………………………… &nbsp; Cần: ……… &nbsp; Mỗi ô: ………</p>
<div class="table-wrap"><table><tbody><tr>{''.join(f'<td class="tall">○ {i}</td>' for i in range(1, 11))}</tr></tbody></table></div>
<p class="small muted">Mỗi lần bỏ hũ Tiết kiệm, con tô một ô.</p>
<h2>3. Tranh cần – muốn (tuần 2)</h2>
<p>Cắt rời từng ô. Con vẽ thêm hình rồi xếp vào hai rổ CẦN và MUỐN.</p>
<div class="table-wrap"><table><tbody>{cmrows}</tbody></table></div>
<h2>4. Danh sách đi chợ có tranh (tuần 5)</h2>
<div class="table-wrap"><table><thead><tr><th>Vẽ hình</th><th>Tên món</th><th>Đã mua ✓</th></tr></thead><tbody>{rows_n(5, 3)}</tbody></table></div>
<p class="small muted">Con dưới 3 tuổi: không dùng tiền xu. Dùng thẻ bìa to tự cắt.</p>
''', current='/cong-cu/')
print('G6 built')
