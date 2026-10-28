# Khóa G4 "Gia đình có con 10–14" – trang khóa, 7 bài, 1 công cụ in
import illus_g4  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/gia-dinh-10-14/'
TOOL = '/cong-cu/thoa-thuan-gia-dinh/'
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
           '<tr><th class="w38">Con đã nói hay làm gì</th><td></td></tr><tr><th>Bố mẹ đã làm được gì</th><td></td></tr>'
           '<tr><th>Cần sửa gì</th><td></td></tr></tbody></table></div>')

SFP = '<a href="https://foundations.org.uk/toolkit/guidebook/strengthening-families-programme-10-14">Strengthening Families 10–14 (Foundations, Anh)</a>'
PLHT = '<a href="https://www.research.ed.ac.uk/en/publications/parenting-for-lifelong-health-a-pragmatic-cluster-randomised-cont/">Cluver et al. 2018, <em>BMJ Global Health</em></a>'
PLH = '<a href="https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health">Parenting for Lifelong Health (WHO/UNICEF)</a>'
KS = '<a href="https://pubmed.ncbi.nlm.nih.gov/10830980">Kerr &amp; Stattin 2000, <em>Child Development</em></a>'
SG = '<a href="https://www.ksat.com/business/2023/05/23/the-us-surgeon-general-has-some-tips-for-parents-and-teens-on-social-media-use/">khuyến cáo của Tổng Y sĩ Hoa Kỳ (2023)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
PA = '<a href="https://knowledge-for-policy.ec.europa.eu/health-promotion-knowledge-gateway/physical-activity-sedentary-behaviour-table-2a_en">khuyến nghị WHO (bảng tổng hợp của EU)</a>'
RUOU = '<a href="https://luatvietnam.vn/an-ninh-trat-tu/luat-phong-chong-tac-hai-cua-ruou-bia-2019-so-44-2019-qh14-175006-d1.html">Luật Phòng, chống tác hại của rượu, bia số 44/2019/QH14, Điều 5 khoản 3</a>'
TLDT = '<a href="https://baovanhoa.vn/thoi-su/quoc-hoi-ra-nghi-quyet-ve-cam-thuoc-la-dien-tu-thuoc-la-nung-nong-tu-nam-2025-113542.html">Nghị quyết Quốc hội ngày 30/11/2024</a>'
WHO_CP = '<a href="https://www.who.int/news-room/fact-sheets/detail/corporal-punishment-and-health">WHO 2026</a>'
NOVIOL = f'Không đánh, không làm nhục, không đe dọa. Đánh đòn gây hại và không có lợi ích nào cho trẻ ({WHO_CP}).'
TALK = 'Nếu con kể chuyện bị bắt nạt, bị đe dọa, bị xâm hại: tin con, giữ bình tĩnh, cảm ơn con đã kể. Gọi 111 (bảo vệ trẻ em, miễn phí 24/7); nguy hiểm tức thì gọi 113.'

L = {
 '1': (1, 'hieu-tuoi-10-14', 'Bài 1', 'Hiểu tuổi 10–14 và thời gian riêng'),
 '2': (2, 'lang-nghe-de-con-ke', 'Bài 2', 'Lắng nghe để con muốn kể'),
 '3': (3, 'thoa-thuan-nha-minh', 'Bài 3', 'Thỏa thuận nhà mình'),
 '4': (4, 'giai-quyet-van-de-cung-nhau', 'Bài 4', 'Giải quyết vấn đề cùng nhau'),
 '5': (5, 'dien-thoai-va-mang-xa-hoi', 'Bài 5', 'Điện thoại, mạng xã hội, an toàn trên mạng'),
 '6': (6, 'ban-be-ruou-bia-thuoc-la', 'Bài 6', 'Bạn bè, rượu bia, thuốc lá điện tử'),
 '7': (7, 'cam-xuc-va-tuong-lai', 'Bài 7', 'Cảm xúc, khi nào cần giúp, và tương lai'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'g4-' + k
    note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này chưa được dạy thử trong gia đình có con 10–14 tuổi. '
            f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn. Xin không ghi tên hay trường của con.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về {code.lower()}</a></p></div>')
    meta = [f'Tuần {w}', 'Phần bố mẹ 20 phút', 'Phần cùng con 20–30 phút']
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Gia đình có con 10–14</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block('Y' + k)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/gia-dinh/')

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Gia đình có con 10–14, bài 1: hiểu những thay đổi của tuổi 10–14 và bắt đầu thời gian riêng 15 phút với con.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> kể được 4 thay đổi bình thường của tuổi 10–14 và có ít nhất 3 lần thời gian riêng 15 phút với con trong tuần.',
   '<strong>Con:</strong> chọn hoạt động cho thời gian riêng và được bố mẹ đi theo, không bị giảng dạy.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Nghĩ trước 3 việc con thích: đá bóng, nấu món ăn, chơi cờ, đi dạo, nghe nhạc.', 'Úp điện thoại khi ở bên con.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Hồi 12 tuổi, mình cần gì nhất từ bố mẹ? Mình ghét điều gì nhất?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Bốn thay đổi.</strong> Cơ thể dậy thì, lớn nhanh, hay ngủ muộn hơn. Cảm xúc mạnh và đổi nhanh. Bạn bè quan trọng hơn trước. Muốn tự quyết định.',
   '<strong>Bình thường, không phải hư.</strong> Con cãi lại, đóng cửa phòng, đòi riêng tư là một phần lớn lên. Bố mẹ vẫn là chỗ dựa quan trọng nhất.',
   '<strong>Dậy thì.</strong> Bắt đầu ở tuổi khác nhau, bạn trai và bạn gái khác nhau. Dùng từ đúng, trả lời thật, ngắn. Không biết thì nói "để bố mẹ tìm hiểu" và hỏi y tế trường hay bác sĩ.',
   '<strong>Thời gian riêng.</strong> 15 phút, một bố mẹ với một con. Con chọn việc. Bố mẹ đi theo, khen, không sửa, không giảng.'])),
 sec(5, 'Phần cùng con (20 phút)', ol([
   'Nói với con: "Bố mẹ muốn có thời gian riêng với con mỗi tuần. Con chọn mình làm gì nhé."',
   'Làm ngay buổi đầu: 15 phút việc con chọn.',
   'Cuối buổi hỏi: "Con thích nhất lúc nào?" Hẹn 2 lần nữa trong tuần.']) +
   '<p><strong>Nhà có em nhỏ:</strong> người lớn còn lại trông em; hoặc chọn lúc em ngủ.</p>'),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Lần cuối mình ở riêng với con mà không giảng gì là khi nào?', 'Thay đổi nào của con làm mình khó chịu nhất?', 'Mình có đang so con với "hồi xưa" không?'])),
 sec(7, 'An toàn', ul([TALK, 'Hoạt động ngoài trời: đội mũ bảo hiểm khi đi xe đạp, xe máy; có người lớn khi bơi.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 15 phút, 3 lần trong tuần.', [
   ('Lần 1.', 'Mẹ hỏi con chọn việc, làm cùng 15 phút.'), ('Khi bố gọi video.', 'Bố có 10 phút riêng với con: hỏi về một việc con thích, chỉ nghe.')], [
   ('Nhà một bố hoặc một mẹ:', 'thời gian riêng vẫn làm được khi đi chợ, nấu ăn cùng nhau.')])),
 sec(9, 'Ôn lại', ul(['<strong>Trong tuần:</strong> 3 lần thời gian riêng.', '<strong>Cuối tuần:</strong> con có chủ động rủ bố mẹ không?'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Thời gian một – một do con dẫn là một phần của chương trình cho cha mẹ và thanh thiếu niên {PLH}. Thử nghiệm ở Nam Phi (552 gia đình, con 10–18 tuổi): bố mẹ báo cáo hành vi bạo hành giảm, nuôi dạy tích cực tăng; con báo cáo giám sát tốt hơn, nhưng không thấy giảm bạo hành theo lời con ({PLHT}).'),
   lb('Đánh giá chuyên môn', 'Phần "bốn thay đổi" là mô tả chung, viết đơn giản; daynentang.com không đưa số liệu tuổi dậy thì vì khác nhau giữa các trẻ.')]))
])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Gia đình có con 10–14, bài 2: lắng nghe để con muốn kể: dừng việc, nghe hết, nhắc lại, hỏi thêm, khuyên sau.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> dùng đủ 4 bước lắng nghe ít nhất 1 lần mỗi ngày; giảm câu "Bố đã bảo mà".', '<strong>Con:</strong> tự kể về một chuyện ở trường hay với bạn trong tuần.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Chọn thời điểm con hay nói: trên xe, khi nấu ăn, trước giờ ngủ.', 'Viết 3 câu hỏi mở lên giấy dán tủ lạnh.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Lần gần nhất con kể chuyện, mình đáp câu đầu tiên là gì? Con còn kể tiếp không?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Vì sao con không kể.</strong> Con thường im khi sợ bị mắng, bị giảng, bị kể lại cho người khác.',
   '<strong>Bốn bước:</strong> dừng việc và nhìn con; nghe hết, không ngắt; nhắc lại "Ý con là…"; hỏi "Rồi sao nữa?".',
   '<strong>Câu hỏi mở:</strong> "Hôm nay có gì vui, gì chán?" thay cho "Học có tốt không?".',
   '<strong>Khi con kể chuyện xấu:</strong> thở trước, cảm ơn con đã kể, hỏi con muốn bố mẹ nghe hay giúp. Xử lý sau, khi cả hai bình tĩnh.',
   '<strong>Giữ lời:</strong> chuyện con kể không đem đi kể cho người khác, trừ khi có nguy hiểm. Nói rõ điều này với con.'])),
 sec(5, 'Phần cùng con (20 phút)', ol([
   'Trò "phóng viên": con phỏng vấn bố mẹ 5 phút về hồi bố mẹ 12 tuổi. Bố mẹ trả lời thật.',
   'Đổi vai: bố mẹ phỏng vấn con bằng câu hỏi mở. Dùng 4 bước lắng nghe.',
   'Hỏi con: "Khi nào con thấy bố mẹ nghe con nhất? Khi nào con thấy không muốn kể?" Ghi lại, không cãi.']) ),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Câu nào của mình hay làm con im?', 'Mình có giữ được bí mật nhỏ của con không?', 'Lúc nào con hay nói nhất trong ngày?'])),
 sec(7, 'An toàn', ul([TALK, 'Giữ bí mật có giới hạn: nếu con hay người khác gặp nguy hiểm, bố mẹ phải hành động. Nói trước điều này với con.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 20 phút, 3 câu hỏi mở.', [
   ('Một lần.', 'Trò phóng viên với mẹ.'), ('Khi bố gọi video.', 'Bố hỏi 1 câu mở, nghe hết, nhắc lại.')], [
   ('Con không muốn nói:', 'không ép. Ngồi cạnh làm việc gì đó cùng con; chuyện thường đến sau.')])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> một lần lắng nghe 4 bước.', '<strong>Cuối tuần:</strong> con tự kể mấy chuyện?'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Ở thanh thiếu niên, việc con tự kể với bố mẹ giải thích mối liên hệ giữa hiểu biết của bố mẹ và sự thích nghi tốt của con nhiều hơn là việc bố mẹ theo dõi; cảm giác bị kiểm soát gắn với thích nghi kém. Đây là nghiên cứu liên hệ ({KS}).'),
   lb('Suy luận', 'Vì vậy khóa tập trung vào làm cho con muốn kể, thay vì theo dõi chặt.'),
   lb('Đánh giá chuyên môn', 'Bốn bước lắng nghe và trò phóng viên do daynentang.com soạn.')]))
])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Gia đình có con 10–14, bài 3: cùng con viết thỏa thuận nhà mình: luật rõ, đặc quyền, hậu quả nói trước, cả nhà ký.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ và con:</strong> có bản <strong>thỏa thuận 3–5 điều</strong>, mỗi điều có đặc quyền và hậu quả, cả nhà ký.', '<strong>Bố mẹ:</strong> khen cụ thể ít nhất 1 lần mỗi ngày khi con giữ thỏa thuận.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In trang 1 của <a href="{TOOL}">Thỏa thuận gia đình</a>.', 'Bố mẹ thống nhất trước 3 điều quan trọng nhất (giờ về, bài tập, việc nhà, điện thoại).'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Luật nào nhà mình đang có mà con không biết rõ? Luật nào bố và mẹ áp dụng khác nhau?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Luật tốt:</strong> ít (3–5), rõ (đo được), con hiểu lý do, có góp ý của con, giữ đều.',
   '<strong>Đặc quyền đi kèm trách nhiệm:</strong> giữ thỏa thuận thì được thêm tự do, ví dụ đi chơi với bạn lâu hơn.',
   '<strong>Hậu quả nói trước:</strong> liên quan, ngắn, áp dụng bình tĩnh. Không thêm hình phạt lúc đang giận.',
   '<strong>Bố mẹ thống nhất:</strong> hai người nói cùng một điều. Bất đồng thì bàn riêng, không cãi trước con.',
   '<strong>Khen cụ thể:</strong> "Con về đúng giờ, bố yên tâm lắm." Khen việc làm, không chỉ khen kết quả.'])),
 sec(5, 'Phần cùng con (30 phút)', ol([
   'Bố mẹ nêu 3 điều đã chuẩn bị và lý do của mỗi điều.',
   'Con đề xuất 1–2 điều cho bố mẹ, ví dụ "không xem điện thoại trong bữa ăn", "gõ cửa trước khi vào phòng con".',
   'Cùng viết đặc quyền và hậu quả cho mỗi điều. Con có quyền góp ý; bố mẹ có quyết định cuối về an toàn.',
   'Cả nhà ký. Dán ở chỗ ai cũng thấy. Hẹn xem lại sau 1 tháng.']) ),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Điều nào mình khó giữ nhất khi mệt?', 'Mình có đang có quá nhiều luật không?', 'Con đề xuất gì cho bố mẹ? Mình có làm được không?'])),
 sec(7, 'An toàn', ul([NOVIOL, 'Luật về an toàn (giờ về, đi xe, nước, người lạ) không bàn lượng về nguyên tắc, chỉ bàn cách làm.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: bản thỏa thuận, 30 phút. Bố tham gia qua video.', [
   ('Trước buổi.', 'Mẹ và bố thống nhất 3 điều qua điện thoại.'), ('Trong buổi.', 'Bố gọi video phần nêu lý do và phần ký (bố ký khi về).')], [
   ('Ông bà cùng sống:', 'đưa ông bà xem thỏa thuận để cả nhà nhất quán.')])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> khen cụ thể 1 lần.', '<strong>Sau 1 tháng:</strong> xem lại cùng con, sửa điều chưa hợp lý.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Chương trình {SFP} có phần bố mẹ học đặt luật nhà, giới hạn và hậu quả; thử nghiệm ngẫu nhiên ở Mỹ (446 gia đình) cho thấy con ít bắt đầu uống rượu hơn sau 1–2 năm. Foundations xếp mức bằng chứng 3 và nhận xét các thử nghiệm ở châu Âu "chưa rõ ràng" hơn.'),
   lb('Đánh giá chuyên môn', 'Mẫu thỏa thuận và cách cho con đề xuất luật cho bố mẹ do daynentang.com soạn; chỉ mượn ý tưởng, không dùng tài liệu của chương trình.')]))
])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Gia đình có con 10–14, bài 4: hậu quả hợp lý thay cho trừng phạt và năm bước giải quyết vấn đề cùng con.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ và con:</strong> dùng 5 bước giải quyết một vấn đề thật trong nhà.', '<strong>Bố mẹ:</strong> trong tuần không dùng đánh, mắng nhục, hay cấm kéo dài.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['Chọn một vấn đề vừa phải, không quá nóng: tranh máy tính với em, dậy muộn, bài tập dồn cuối tuần.', 'Giấy, bút.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Hình phạt nào mình từng dùng mà không thay đổi được gì?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Hậu quả khác trừng phạt.</strong> Hậu quả liên quan đến việc sai, ngắn, nói trước, giữ tôn trọng. Trừng phạt thường to, dài, làm con xấu hổ.',
   '<strong>Ví dụ.</strong> Dùng máy quá giờ → mai không dùng. Về trễ không báo → cuối tuần sau ở nhà. Làm vỡ đồ → góp sức sửa hoặc đền một phần.',
   '<strong>Khi giận.</strong> Nói "Bố đang giận, mình nói chuyện sau 30 phút." Đi ra chỗ khác. Quay lại khi bình tĩnh.',
   '<strong>Năm bước giải quyết vấn đề:</strong> gọi tên vấn đề, nghĩ nhiều cách (không chê cách nào), chọn một cách cả hai chấp nhận, thử 1 tuần, xem lại.'])),
 sec(5, 'Phần cùng con (30 phút)', ol([
   'Nói: "Nhà mình có một vấn đề. Bố mẹ muốn con cùng nghĩ cách."',
   'Đi qua 5 bước trên giấy. Con nêu ý trước, bố mẹ sau.',
   'Chọn một cách, ghi rõ ai làm gì, từ khi nào.',
   'Hẹn ngày xem lại sau 1 tuần.']) ),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Hậu quả nào mình nói ra lúc giận rồi không làm được?', 'Con có ý nào hay mà mình chưa nghĩ ra?', 'Mình nhận lỗi với con lần cuối là khi nào?'])),
 sec(7, 'An toàn', ul([NOVIOL, 'Nếu xung đột trong nhà thành bạo lực, an toàn đến trước. Gọi 113 khi nguy hiểm tức thì; trẻ em bị hại gọi 111.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: giấy, 30 phút.', [
   ('Trước buổi.', 'Mẹ và bố chọn vấn đề và hậu quả có thể chấp nhận.'), ('Trong buổi.', 'Mẹ và con đi qua 5 bước; gửi ảnh tờ giấy cho bố.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Sau 1 tuần:</strong> xem lại cách đã chọn cùng con.', '<strong>Trong tuần:</strong> đếm số lần mình tạm dừng khi giận.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Đánh đòn gây hại sức khỏe thể chất, tinh thần của trẻ, làm hành vi xấu tăng theo thời gian, không có kết quả tích cực ({WHO_CP}).'),
   lb('Đã xác nhận', f'Trong thử nghiệm PLH cho thanh thiếu niên ở Nam Phi, bố mẹ báo cáo phạt thân thể giảm (tỉ suất 0,55), nhưng con không báo cáo giảm; không đánh giá mù được ({PLHT}).'),
   lb('Đánh giá chuyên môn', 'Năm bước giải quyết vấn đề là kỹ thuật phổ biến trong các chương trình kỹ năng sống; cách viết trong bài do daynentang.com soạn.')]))
])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Gia đình có con 10–14, bài 5: kế hoạch dùng thiết bị gia đình, giấc ngủ, và an toàn trên mạng.', [
 sec(1, 'Mục tiêu', ul(['<strong>Cả nhà:</strong> có <strong>kế hoạch dùng thiết bị</strong> 4 phần, áp dụng cho cả bố mẹ.', '<strong>Con:</strong> nói được 4 dấu hiệu nguy hiểm từ người lạ trên mạng và biết làm gì.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 2 của <a href="{TOOL}">Thỏa thuận gia đình</a>.', 'Mỗi người ước thời gian dùng điện thoại hôm qua (xem trong cài đặt máy nếu có).'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Con thấy mình dùng điện thoại bao nhiêu? Con có thấy mình xem máy trong bữa ăn không?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Kế hoạch 4 phần:</strong> giờ dùng; chỗ không máy (bàn ăn, phòng ngủ); sạc máy ngoài phòng ngủ; bố mẹ làm gương.',
   '<strong>Giấc ngủ:</strong> con 6–12 tuổi cần 9–12 giờ, 13–18 tuổi cần 8–10 giờ mỗi ngày. Tắt màn hình ít nhất 1 giờ trước khi ngủ.',
   '<strong>Mạng xã hội:</strong> nói với con về lợi và hại, quyền riêng tư, ai con kết bạn, con dùng thời gian thế nào.',
   '<strong>Dấu hiệu người lạ nguy hiểm:</strong> khen quá mức, tặng quà; đòi giữ bí mật với bố mẹ; xin ảnh riêng tư; rủ gặp riêng.',
   '<strong>Khi con kể chuyện xấu trên mạng:</strong> không tịch thu máy ngay để phạt, vì lần sau con sẽ giấu. Cảm ơn con, chặn, chụp lại bằng chứng, báo cáo.'])),
 sec(5, 'Phần cùng con (30 phút)', ol([
   'Mỗi người nói thời gian dùng máy hôm qua. Bố mẹ nói trước.',
   'Cùng viết kế hoạch 4 phần. Con đề xuất giờ dùng; bố mẹ góp ý.',
   'Bố mẹ hỏi: "Có ai trên mạng làm con khó chịu chưa?" Nghe, không phán xét.',
   'Cùng đọc 4 dấu hiệu nguy hiểm. Thống nhất: thấy dấu hiệu thì chặn, chụp lại, kể bố mẹ; con sẽ không bị phạt vì đã kể.']) ),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Mình có đăng ảnh của con mà con không thích không?', 'Phần nào của kế hoạch khó nhất cho chính mình?', 'Con có biết cách chặn, báo cáo trên ứng dụng con dùng không?'])),
 sec(7, 'An toàn', ul([TALK, 'Không đăng ảnh, tên, trường, địa chỉ của con lên mạng công khai. Hỏi ý con trước khi đăng ảnh có con.',
   'Bị đe dọa, tống tiền bằng ảnh: không trả tiền, không gửi thêm; giữ bằng chứng, báo công an, gọi 111.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: trang kế hoạch, 30 phút.', [
   ('Trong buổi.', 'Mẹ và con viết kế hoạch; bố đồng ý qua video.'), ('Khi bố đi công tác.', 'Bố cũng giữ "chỗ không máy" khi gọi video với con: không vừa gọi vừa làm việc khác.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tối:</strong> sạc máy ngoài phòng ngủ.', '<strong>Sau 2 tuần:</strong> xem lại kế hoạch cùng con.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Theo {SG}: lập kế hoạch dùng thiết bị gia đình, tạo chỗ và giờ không máy (ngừng ít nhất 1 giờ trước ngủ, bữa ăn không máy), bố mẹ làm gương, nói với con về lợi hại và quyền riêng tư.'),
   lb('Đã xác nhận', f'Giờ ngủ khuyến nghị: 6–12 tuổi 9–12 giờ; 13–18 tuổi 8–10 giờ mỗi ngày ({AASM}).'),
   lb('Đánh giá chuyên môn', 'Bốn dấu hiệu người lạ nguy hiểm là tóm tắt ở mức chung của daynentang.com, không đầy đủ. Khuyên không tịch thu máy ngay khi con kể là đánh giá chuyên môn.')]))
])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Gia đình có con 10–14, bài 6: áp lực bạn bè, rượu bia, thuốc lá điện tử; tập cách nói không và mật mã gọi đón.', [
 sec(1, 'Mục tiêu', ul(['<strong>Con:</strong> tập đủ 4 cách nói không trong đóng vai; nhớ câu mật mã gọi đón.', '<strong>Bố mẹ:</strong> nói rõ quan điểm nhà mình về rượu bia, thuốc lá điện tử, kèm lý do và luật.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 3 (thẻ mật mã) của <a href="{TOOL}">Thỏa thuận gia đình</a>.', 'Bố mẹ tự xem lại thói quen rượu bia, thuốc lá của mình.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Con đang thấy mình uống rượu bia, hút thuốc thế nào? Lời mình nói và việc mình làm có khớp không?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Bạn bè quan trọng.</strong> Muốn được nhóm chấp nhận là bình thường. Con cần câu nói sẵn để từ chối mà không mất mặt.',
   '<strong>Luật Việt Nam.</strong> Cấm bán, cung cấp, khuyến mại rượu bia cho người dưới 18 tuổi. Quốc hội đã cấm thuốc lá điện tử, thuốc lá nung nóng từ năm 2025.',
   '<strong>Quan điểm nhà mình.</strong> Nói rõ, ngắn: "Nhà mình không để con uống rượu bia, không dùng thuốc lá điện tử, vì não con đang lớn và vì luật."',
   '<strong>Mật mã gọi đón.</strong> Thống nhất một câu bình thường, ví dụ "Bố ơi con quên áo". Con nhắn câu đó, bố mẹ đến đón ngay, không tra hỏi lúc đó. Nói chuyện sau, bình tĩnh.'])),
 sec(5, 'Phần cùng con (30 phút)', ol([
   'Bố mẹ kể một lần mình bị bạn rủ làm điều không nên, và mình đã xử lý thế nào.',
   'Học 4 cách nói không: "Không, cảm ơn"; đưa lý do ("Bố mẹ sắp đón"); đổi chủ đề; bỏ đi hoặc gọi mật mã.',
   'Đóng vai 3 tình huống: bạn mời thử thuốc lá điện tử; bạn rủ trốn học; bạn rủ uống bia ở sinh nhật. Đổi vai để con làm người rủ.',
   'Cùng chọn câu mật mã. Con lưu vào máy. Viết vào thẻ.']) ),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Mình có sẵn sàng đón con mà không mắng ngay không?', 'Con biết bạn nào đang dùng thuốc lá điện tử không? Mình hỏi thế nào để con không thấy bị tra?', 'Mình có cần thay đổi thói quen của chính mình không?'])),
 sec(7, 'An toàn', ul(['Nếu con lỡ dùng chất gì và có biểu hiện lạ (lơ mơ, khó thở, co giật): gọi 115 ngay.', TALK, 'Không mua, không đưa rượu bia, thuốc lá cho con, kể cả "cho biết".'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 30 phút, thẻ mật mã.', [
   ('Trong buổi.', 'Mẹ và con đóng vai; bố gọi video làm "người rủ" một lượt.'), ('Mật mã.', 'Cả bố và mẹ lưu câu mật mã; ai gần thì người đó đón.')], [
   ('Bố đi công tác xa:', 'thống nhất thêm một người lớn tin cậy (ông, chú, hàng xóm) có thể đón con.')])),
 sec(9, 'Ôn lại', ul(['<strong>Trước mỗi buổi đi chơi:</strong> nhắc nhẹ mật mã.', '<strong>Sau 1 tháng:</strong> hỏi con đã dùng cách nói không nào chưa.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{RUOU}: nghiêm cấm bán, cung cấp, khuyến mại rượu bia cho người chưa đủ 18 tuổi. Luật thông qua 14/06/2019, hiệu lực 01/01/2020; tra cứu 28/10/2026, chưa thấy khoản này bị bãi bỏ.'),
   lb('Đã xác nhận', f'Quốc hội thông qua ngày 30/11/2024 việc cấm sản xuất, kinh doanh, nhập khẩu, chứa chấp, vận chuyển, sử dụng thuốc lá điện tử, thuốc lá nung nóng từ năm 2025 ({TLDT}).'),
   lb('Cần kiểm chứng', 'Số hiệu nghị quyết và văn bản hướng dẫn xử phạt về thuốc lá điện tử: bài báo nguồn không ghi; chúng tôi chưa đọc văn bản gốc.'),
   lb('Đã xác nhận', f'Thử nghiệm {SFP} ở Mỹ: con ít bắt đầu uống rượu hơn sau 1–2 năm.'),
   lb('Đánh giá chuyên môn', 'Bốn cách nói không và mật mã gọi đón do daynentang.com soạn.')]))
])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Gia đình có con 10–14, bài 7: cảm xúc và căng thẳng, dấu hiệu cần tìm giúp, mục tiêu tương lai và đánh giá cuối khóa.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> nói được các dấu hiệu cần đưa con gặp chuyên gia và biết gọi ai.', '<strong>Con:</strong> chọn 2 cách tự bình tĩnh và viết 1 mục tiêu cho năm tới.', '<strong>Bố mẹ:</strong> chấm phiếu tự đánh giá cuối khóa.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 4 (phiếu tự đánh giá) của <a href="{TOOL}">Thỏa thuận gia đình</a>.', 'Lưu sẵn số 111, 115, 096 306 1414 vào máy của bố mẹ và con.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Tuần này con có lúc nào căng thẳng không? Mình đã thấy dấu hiệu gì?"</em></p>'),
 sec(4, 'Phần bố mẹ (20 phút)', ol([
   '<strong>Nền của cảm xúc:</strong> ngủ đủ, vận động khoảng 60 phút mỗi ngày, ăn đều, có người để nói chuyện.',
   '<strong>Cách tự bình tĩnh:</strong> thở chậm 1 phút, đi bộ, nghe nhạc, viết ra giấy, nói với người tin cậy.',
   '<strong>Dấu hiệu cần tìm giúp:</strong> buồn chán, cáu gắt kéo dài nhiều tuần; bỏ ăn, mất ngủ; rút khỏi bạn bè, bỏ học; nói về cái chết hay làm hại bản thân.',
   '<strong>Khi thấy dấu hiệu:</strong> nói chuyện với con, ở bên con, không chê "yếu đuối". Đưa con gặp bác sĩ, chuyên gia tâm lý. Khẩn cấp gọi 115.',
   '<strong>Đánh giá cuối khóa:</strong> chấm phiếu, so với tuần 1. Ghi 3 dòng nhật ký.'])),
 sec(5, 'Phần cùng con (30 phút)', ol([
   'Mỗi người kể một lần căng thẳng gần đây và mình đã làm gì.',
   'Con chọn 2 cách tự bình tĩnh, viết lên giấy dán bàn học.',
   'Con viết 1 mục tiêu cho năm tới (học, thể thao, kỹ năng, giúp người khác) và 1 bước đầu tiên.',
   'Bố mẹ nói một điều mình tự hào về con trong 7 tuần qua. Cụ thể.',
   'Cả nhà xem lại thỏa thuận và kế hoạch thiết bị. Giữ, sửa hay bỏ điều nào?']) ),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Con có biết có thể nói với ai ngoài bố mẹ (thầy cô, người thân) không?', 'Phần nào của khóa mình muốn giữ lâu dài?', 'Mình có đang chăm sóc sức khỏe tinh thần của chính mình không?'])),
 sec(7, 'An toàn', ul(['Nếu con nói về cái chết hay làm hại bản thân: ở bên con, không để con một mình, cất các vật nguy hiểm, gọi 115 hoặc đưa con đến cơ sở y tế ngay.',
   'Đường dây Ngày Mai 096 306 1414 hỗ trợ người trầm cảm và người thân. Bảo vệ trẻ em: 111.', TALK])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 30 phút, giấy bút.', [
   ('Trong buổi.', 'Mẹ và con làm phần mục tiêu; bố gọi video nói điều tự hào về con.'), ('Sau buổi.', 'Bố mẹ cùng chấm phiếu tự đánh giá qua điện thoại.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> hỏi con về mục tiêu, giúp con bước tiếp.', '<strong>Sau 3 tháng:</strong> chấm lại phiếu tự đánh giá.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'WHO khuyến nghị trẻ và thanh thiếu niên vận động vừa đến mạnh ít nhất khoảng 60 phút mỗi ngày, có hoạt động tăng cơ, xương ít nhất 3 ngày mỗi tuần ({PA}).'),
   lb('Đã xác nhận', f'Thử nghiệm {SFP} ở Mỹ ghi nhận triệu chứng lo âu, trầm cảm tăng chậm hơn trong 1–6 năm.'),
   lb('Đánh giá chuyên môn', 'Danh sách dấu hiệu cần tìm giúp là tóm tắt chung, không dùng để chẩn đoán. Khóa không thay thế điều trị.'),
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước – sau 7 tuần không có nhóm đối chứng; đây không phải bằng chứng hiệu quả.')]))
])

# =============== TRANG KHÓA ===============
rows = ''.join(f'<tr><td>{L[k][0]}</td><td><a href="{link(k)[0]}">{L[k][3]}</a></td><td>{g}</td></tr>' for k, g in zip(ORDER, [
 '3 lần thời gian riêng 15 phút/tuần', 'Lắng nghe 4 bước mỗi ngày; con tự kể ≥1 chuyện', 'Thỏa thuận 3–5 điều, cả nhà ký',
 'Giải quyết 1 vấn đề thật bằng 5 bước', 'Kế hoạch thiết bị 4 phần; sạc máy ngoài phòng ngủ', 'Con tập 4 cách nói không; có mật mã gọi đón', 'Con có 2 cách tự bình tĩnh, 1 mục tiêu; chấm phiếu']))
page(U, 'Gia đình có con 10–14',
 'Khóa 7 tuần miễn phí cho bố mẹ có con 10–14 tuổi: thời gian riêng, lắng nghe, thỏa thuận nhà mình, điện thoại, áp lực bạn bè, cảm xúc.',
f'''
<p class="eyebrow">Gia đình · Khóa G4 · Đang thử nghiệm</p>
<h1>Gia đình có con 10–14</h1>
<p class="lead">Tuổi dậy thì cần cả yêu thương và giới hạn. Bố mẹ học cách gần con, lắng nghe để con muốn kể, đặt thỏa thuận rõ ràng và chuẩn bị cho con trước những áp lực mới.</p>

<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Giữ gắn bó với con tuổi 10–14; ít cãi nhau hơn; con có kỹ năng từ chối và biết tìm giúp</td></tr>
<tr><th>Dành cho</th><td>Bố mẹ, người chăm sóc có con 10–14 tuổi. Mỗi bài có phần bố mẹ học và phần làm cùng con</td></tr>
<tr><th>Thời lượng</th><td>7 tuần. Mỗi tuần phần bố mẹ 20 phút và phần cùng con 20–30 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút, máy in nếu có</td></tr>
<tr><th>Tình trạng</th><td>Đủ 7 tuần, bản chưa dạy thử. Gia đình người soạn chưa có con ở tuổi này; rất cần góp ý của các gia đình khác</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Có 15 phút riêng với con, vài lần mỗi tuần.</li><li>Con kể chuyện nhiều hơn vì được nghe.</li><li>Có thỏa thuận nhà mình rõ ràng, cả nhà ký.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: yêu thương và giới hạn đi cùng nhau.</li><li>Kỹ năng: lắng nghe, giải quyết vấn đề, nói không.</li><li>Biết dấu hiệu cần tìm giúp và gọi ai.</li></ul></div>
</div>

<h2>Bảy tuần</h2>
{figure_block('KHOAY')}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Thỏa thuận gia đình</a>: thỏa thuận nhà mình, kế hoạch dùng thiết bị, thẻ mật mã gọi đón, phiếu tự đánh giá.</li></ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{SFP}</td><td>Phần bố mẹ, phần con, phần cả nhà; yêu thương và giới hạn; luật nhà; từ chối áp lực bạn bè</td><td><span class="label">[Đã xác nhận]</span> Mức 3 theo Foundations; thử nghiệm Mỹ 446 gia đình: ít bắt đầu uống rượu hơn; thử nghiệm châu Âu chưa rõ ràng</td></tr>
<tr><td>{PLH} – cho thanh thiếu niên</td><td>Thời gian một – một, khen, giải quyết vấn đề, kỷ luật không bạo lực</td><td><span class="label">[Đã xác nhận]</span> {PLHT}: 552 gia đình; kết quả theo lời bố mẹ rõ hơn theo lời con. Tài liệu PLH không cho phép phái sinh; chúng tôi chỉ dẫn link</td></tr>
<tr><td>{KS}</td><td>Làm cho con muốn kể thay vì theo dõi</td><td><span class="label">[Đã xác nhận]</span> Nghiên cứu liên hệ</td></tr>
<tr><td>{SG}; {AASM}</td><td>Kế hoạch thiết bị, giờ không máy, giấc ngủ</td><td><span class="label">[Đã xác nhận]</span> Khuyến cáo cơ quan y tế, đồng thuận chuyên gia</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các chương trình gốc làm theo nhóm, có người hướng dẫn, ở nước khác. Khóa tự học này chưa được thử, và chưa được dạy thử trong gia đình người soạn.
  Khóa không thay thế tư vấn tâm lý hay điều trị.</p>
</div>

<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai. Xin không ghi tên, trường của con.</p>

<h2>An toàn cho mọi buổi</h2>
<ul><li>{NOVIOL}</li><li>{TALK}</li><li>Con nói về cái chết hay làm hại bản thân: ở bên con, gọi 115 hoặc đến cơ sở y tế ngay.</li></ul>
{HELP_BOX}
''', current='/gia-dinh/')

# =============== CÔNG CỤ ===============
rrows = ''.join(f'<tr><td class="tall">{i}.</td><td></td><td></td><td></td></tr>' for i in range(1, 6))
SELF = ['Có thời gian riêng với con mỗi tuần', 'Lắng nghe hết trước khi khuyên', 'Con tự kể chuyện với bố mẹ', 'Có thỏa thuận rõ, cả nhà biết',
        'Bố mẹ áp dụng thỏa thuận giống nhau', 'Không đánh, không làm nhục con', 'Có kế hoạch dùng thiết bị, cả bố mẹ theo', 'Có mật mã gọi đón', 'Biết dấu hiệu cần tìm giúp và số điện thoại']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)
page(TOOL, 'Thỏa thuận gia đình', 'Trang in cho khóa Gia đình có con 10–14: thỏa thuận nhà mình, kế hoạch dùng thiết bị, thẻ mật mã gọi đón, phiếu tự đánh giá.',
f'''
<h1>Thỏa thuận gia đình</h1>
<p>Dùng cho khóa <a href="{U}">Gia đình có con 10–14</a>. Chỉ để in, trang không lưu dữ liệu của bạn.</p>
{PRINT_ROW}
<h2>1. Thỏa thuận nhà mình (tuần 3)</h2>
<div class="table-wrap"><table><thead><tr><th>Điều thỏa thuận (rõ, đo được)</th><th>Lý do</th><th>Đặc quyền khi giữ</th><th>Hậu quả nói trước</th></tr></thead><tbody>{rrows}</tbody></table></div>
<p>Điều con đề xuất cho bố mẹ: ……………………………………………………</p>
<p>Ký: Bố ………… &nbsp; Mẹ ………… &nbsp; Con ………… &nbsp; Ngày xem lại: ……/……</p>
<h2>2. Kế hoạch dùng thiết bị gia đình (tuần 5)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Giờ dùng ngày học</th><td></td></tr><tr><th>Giờ dùng cuối tuần</th><td></td></tr>
<tr><th>Chỗ không máy</th><td>Bàn ăn · Phòng ngủ · ……………</td></tr><tr><th>Giờ tắt máy buổi tối</th><td>(ít nhất 1 giờ trước khi ngủ)</td></tr>
<tr><th>Chỗ sạc máy ban đêm</th><td>(ngoài phòng ngủ)</td></tr><tr><th>Bố mẹ hứa</th><td></td></tr>
<tr><th>Khi gặp điều xấu trên mạng</th><td>Chặn · Chụp lại · Kể bố mẹ · Con không bị phạt vì đã kể</td></tr>
</tbody></table></div>
<h2>3. Thẻ mật mã gọi đón (tuần 6)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Câu mật mã</th><td class="tall">"……………………………………"</td></tr>
<tr><th>Gọi ai</th><td>Bố …………… · Mẹ …………… · Người dự phòng ……………</td></tr>
<tr><th>Lời hứa của bố mẹ</th><td>Đến đón ngay, không tra hỏi lúc đó, nói chuyện sau khi bình tĩnh.</td></tr>
<tr><th>Số khẩn cấp</th><td>113 công an · 115 cấp cứu · 111 bảo vệ trẻ em</td></tr>
</tbody></table></div>
<h2>4. Phiếu tự đánh giá (tuần 1 và tuần 7)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 7</th></tr></thead><tbody>{srows}</tbody></table></div>
<p class="small muted">Phiếu để bố mẹ tự theo dõi, không dùng để chẩn đoán.</p>
''', current='/cong-cu/')
print('G4 built')
