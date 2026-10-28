import illus3  # noqa: F401  (tạo hình tuần 9–12 trước khi dựng trang)
from lessons import lesson, sec, JOURNAL

U = '/khoa-hoc/gia-dinh-2-8/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
HARVARD = '<a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Harvard Center on the Developing Child</a>'
WATER = '<a href="https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/">CPSC, Hoa Kỳ</a>'
SMALL = 'Mọi vật trong tầm với của con nhỏ phải to hơn lõi giấy vệ sinh.'

L = {
 't9': (9, 't9-cham-cay-cua-minh', 'T9', 'Chăm cây của mình'),
 'k9': (9, 'k9-khung-long-va-hoa-thach', 'K9', 'Khủng long và hóa thạch'),
 'g9': (9, 'g9-di-cham-an-cham', 'G9', 'Đi chậm, ăn chậm'),
 't10': (10, 't10-goc-binh-tinh', 'T10', 'Góc bình tĩnh'),
 'k10': (10, 'k10-thiet-ke-thuyen', 'K10', 'Thiết kế thuyền'),
 'g10': (10, 'g10-giu-loi-hua', 'G10', 'Giữ lời hứa nhỏ'),
 't11': (11, 't11-chau-rau-gia-dinh', 'T11', 'Chậu rau gia đình'),
 'k11': (11, 'k11-con-hoi-con-thu', 'K11', 'Con hỏi – con thử'),
 'g11': (11, 'g11-tu-te-voi-chinh-minh', 'G11', 'Tử tế với chính mình'),
 't12': (12, 't12-le-ban-tay-nen-tang', 'T12', 'Lễ Bàn tay nền tảng'),
 'k12': (12, 'k12-trien-lam-khoa-hoc', 'K12', 'Triển lãm khoa học gia đình'),
 'g12': (12, 'g12-on-gia-tri-va-uoc-nguyen', 'G12', 'Ôn giá trị và ước nguyện'),
}
ORDER = ['t9','k9','g9','t10','k10','g10','t11','k11','g11','t12','k12','g12']
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
def make(k, desc, meta, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U + 'tuan-8/g8-cam-on-nguoi-lao-dong/', 'G8 – Cảm ơn người lao động')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    lesson(slug, code, title, '', desc, meta, sections, prev=prev, nxt=nxt, week=w, draft=True)
def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>Mẹ chỉ cần: {need}</em></p><ol>{li}</ol>{nt}</div>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'

# =================== TUẦN 9 ===================
make('t9', 'Bài thói quen tuần 9: chăm cây của mình. Con hiểu mình cần ngủ, ăn, vận động như cây cần nước và nắng; lập nếp trước giờ ngủ.',
 ['Mạch A – Thói quen (Ngón út)', 'Tuần 9, buổi 1', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> nói được 3 điều cơ thể cần (ngủ, ăn, vận động) và tự làm đủ 4 bước nếp ngủ ít nhất 5/7 tối.',
   '<strong>Con nhỏ:</strong> làm theo nếp ngủ có tranh với người lớn, đi ngủ cùng giờ ít nhất 5/7 tối.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 chậu cây trong nhà (hoặc chậu mầm đậu từ bài K3).', 'Giấy, bút sáp để vẽ 4 tranh nếp ngủ.', 'Băng dính để dán tranh cạnh giường.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Chỉ vào chậu cây: "Nếu mình quên tưới, cây sẽ thế nào? Còn con, nếu thiếu ngủ thì sao?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   'Xem sơ đồ "Cây cần gì – con cần gì". Con nối: nước ↔ ăn uống, nắng ↔ vận động, đất tốt ↔ giấc ngủ.',
   'Con kể hôm nay mình đã ăn gì, chạy nhảy ở đâu, tối qua ngủ lúc mấy giờ.',
   'Con vẽ 4 tranh nếp ngủ: tắm – đánh răng – đọc truyện – tắt đèn. Dán cạnh giường.',
   'Cả nhà chọn giờ đi ngủ cố định. Bố mẹ xem bảng giờ ngủ theo tuổi để chọn giờ phù hợp.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Cùng con chỉ từng tranh nếp ngủ.', 'Tối nay làm đúng 4 bước, chỉ tranh sau mỗi bước.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Hôm nào con ngủ ít, sáng hôm sau con thấy thế nào?', 'Con thích vận động gì nhất?', 'Bước nào trong nếp ngủ con thích nhất?'])),
 sec(6,'An toàn', ul(['Không dùng màn hình trong 1 giờ trước khi ngủ theo nếp của nhà mình.', 'Nếu con ngáy to, ngưng thở khi ngủ hay rất khó ngủ kéo dài, hỏi bác sĩ nhi.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('chậu cây, giấy bút, băng dính. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi về chậu cây quên tưới.'),
   ('Phút 2–8 – Sơ đồ.', 'Con lớn nối cây cần gì – con cần gì.'),
   ('Phút 8–18 – Vẽ nếp ngủ.', 'Con lớn vẽ 4 tranh; con nhỏ tô màu cùng.'),
   ('Phút 18–20 – Dán tranh.', 'Dán cạnh giường, thống nhất giờ đi ngủ.')], [
   ('Giữ đều:', 'cùng giờ mỗi tối, kể cả cuối tuần. Nếp đều quan trọng hơn một tối hoàn hảo.'),
   ('Gọi video với bố:', 'nếu bố gọi, gọi trước bước "đọc truyện"; bố có thể đọc truyện qua điện thoại.'),
   ('Nhắn bố 1 câu:', 'giờ đi ngủ cả nhà chọn.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi tối:</strong> con tự chỉ tranh nếp ngủ.', '<strong>Sau 1 tuần:</strong> đếm số tối đi ngủ đúng giờ. Mục tiêu: 5/7 tối.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Khuyến nghị giờ ngủ trong 24 giờ: 1–2 tuổi 11–14 giờ, 3–5 tuổi 10–13 giờ (có giấc trưa), 6–12 tuổi 9–12 giờ ({AASM}, <em>Journal of Clinical Sleep Medicine</em>).'),
   lb('Đã xác nhận', '<a href="https://www.who.int/publications/i/item/9789241550536">WHO 2019</a> khuyến nghị trẻ dưới 5 tuổi vận động nhiều trong ngày và hạn chế ngồi lâu trước màn hình.'),
   lb('Đánh giá chuyên môn', 'Sơ đồ "cây cần gì – con cần gì" và nếp ngủ 4 bước do daynentang.com thiết kế.')]))
])

make('k9', 'Bài khoa học tuần 9: khủng long và hóa thạch. Con in dấu đồ vật lên đất nặn và tập "nhìn dấu – đoán vật" như nhà khoa học.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 9, buổi 2', '25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> đoán đúng ít nhất 3/5 đồ vật chỉ bằng dấu in, và kể lại 4 bước hình thành hóa thạch.',
   '<strong>Con nhỏ:</strong> ấn khủng long đồ chơi lên đất nặn và chỉ vào dấu chân.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Đất nặn mua sẵn, loại ghi "an toàn cho trẻ em".', '1–2 khủng long đồ chơi to, 1 chiếc lá, 1 vỏ sò to, 1 nắp chai to, 1 chiếc thìa.', 'Một tấm khăn để che đồ khi đoán.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Không ai sống cùng thời khủng long. Vậy làm sao mình biết khủng long có thật?" Nghe con đoán.</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (20 phút)</h3>' + ol([
   '<strong>Kể:</strong> xem sơ đồ hóa thạch 4 bước. Nhấn mạnh: mất rất, rất lâu.',
   '<strong>Thử làm "hóa thạch":</strong> con ấn chân khủng long và chiếc lá lên đất nặn.',
   '<strong>Đoán:</strong> bố mẹ giấu 5 đồ dưới khăn, bí mật in dấu từng đồ. Con nhìn dấu và đoán.',
   '<strong>So sánh:</strong> mở khăn, đặt đồ cạnh dấu. Đúng mấy cái?',
   '<strong>Kể lại:</strong> "Nhà khoa học nhìn dấu để đoán con vật, giống con vừa làm."']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Cho con ấn khủng long lên đất nặn: "Dấu chân đây!"', 'Đếm ngón chân trên dấu cùng con.', 'Nặn lại, in lại nhiều lần.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Dấu nào dễ đoán nhất? Khó nhất?', 'Nếu chỉ thấy dấu chân, con biết được gì về con vật? (to hay nhỏ, mấy ngón)', 'Ngoài đời, con đã thấy dấu chân gì? (mèo, chim trên cát)'])),
 sec(6,'An toàn', ul(['Dùng đất nặn mua sẵn ghi an toàn cho trẻ; không ăn đất nặn.', 'Đất nặn tự làm với nhiều muối có thể nguy hiểm nếu trẻ nhỏ hoặc thú cưng ăn phải; nếu tự làm, cất xa tầm với.',
   SMALL + ' Nắp chai phải là loại to.', 'Rửa tay sau khi chơi.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('đất nặn, khủng long đồ chơi, chiếc lá, 3 đồ to, 1 khăn. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi làm sao biết khủng long có thật.'),
   ('Phút 2–6 – Con nhỏ.', 'Con nhỏ in dấu khủng long.'),
   ('Phút 6–16 – Nhìn dấu đoán vật.', 'Mẹ giấu 3–5 đồ, in dấu; con lớn đoán.'),
   ('Phút 16–20 – Kể lại.', 'Con lớn kể 4 bước hóa thạch theo sơ đồ.')], [
   ('Nếu con hỏi khủng long sống cách đây bao lâu:', '"Rất, rất lâu, trước khi có người." Có thể tra sách ở thư viện cùng con sau.'),
   ('Nhắn bố 1 câu:', 'con đoán đúng mấy dấu.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> ra sân cát hoặc đất ẩm, tìm dấu chân và đoán.', '<strong>Sau 1 tuần:</strong> con tự in dấu để đố bố mẹ.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Sơ đồ hóa thạch 4 bước là cách nói rất đơn giản cho trẻ; quá trình thật phức tạp và mất hàng triệu năm. Phần giải thích sâu thuộc trang hocsauhocrong.com.'),
   lb('Suy luận', 'Cảnh báo đất nặn tự làm nhiều muối dựa trên các khuyến cáo về ngộ độc muối ở trẻ nhỏ và thú cưng; chúng tôi chưa đọc nguồn y khoa gốc.'),
   lb('Đánh giá chuyên môn', 'Trò "nhìn dấu – đoán vật" do daynentang.com thiết kế.')]))
])

make('g9', 'Bài giá trị tuần 9: chánh niệm qua đi chậm, ăn chậm. Một kỹ năng ngắn để con biết dừng lại và nhận ra.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 9, buổi 3', '15–20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> ăn chậm một miếng chuối qua 5 bước và kể 3 điều mới nhận ra; đi chậm 2 phút và kể 3 âm thanh.',
   '<strong>Con nhỏ:</strong> đi chậm theo bố mẹ như "rùa" trong 1 phút.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 quả chuối chín, cắt khoanh nhỏ (hỏi trước nếu con dị ứng).', 'Một lối đi ngắn trong nhà hoặc sân, sạch, không vật cản.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Hôm nay mình làm rùa, không làm thỏ. Rùa đi chậm nên thấy được nhiều điều."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   '<strong>Ăn chậm:</strong> theo sơ đồ 5 bước: nhìn màu, ngửi mùi, sờ vỏ và ruột, cắn thật nhỏ, nhai chậm rồi kể.',
   'Con kể 3 điều mới nhận ra (ví dụ: mùi thơm, có hạt đen nhỏ, ngọt dần).',
   '<strong>Đi chậm:</strong> đi thật chậm 2 phút, mỗi bước đặt gót rồi mũi chân. Dừng lại, nhắm mắt nghe.',
   'Con kể 3 âm thanh nghe được.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Bố mẹ làm "rùa", con đi theo thật chậm 1 phút.', 'Cho con ăn một khoanh chuối, hỏi: "Ngọt không?"'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Ăn chậm khác ăn nhanh thế nào?', 'Âm thanh nào con chưa từng để ý trước đây?', 'Khi nào trong ngày con muốn "làm rùa"?'])),
 sec(6,'An toàn', ul(['Con ngồi yên khi ăn; không vừa đi vừa ăn.', 'Chuối cắt khoanh nhỏ cho con nhỏ; không dùng nho nguyên quả, hạt cứng.',
   'Lối đi phẳng, không trơn. Nhắm mắt chỉ khi đứng yên.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('1 quả chuối. Tổng 15 phút, có thể làm sau bữa chiều.', [
   ('Phút 0–2 – Mở đầu.', '"Hôm nay mình làm rùa."'),
   ('Phút 2–8 – Ăn chậm.', 'Con lớn theo 5 bước; con nhỏ ăn một khoanh.'),
   ('Phút 8–13 – Đi chậm.', 'Cả ba đi chậm; con lớn kể 3 âm thanh.'),
   ('Phút 13–15 – Kết thúc.', 'Hỏi: "Chậm lại, con thấy gì?"')], [
   ('Không ép:', 'nếu con thấy chán, làm 1 phút là đủ. Đây là kỹ năng ngắn, không phải bài kiểm tra.'),
   ('Nhắn bố 1 câu:', 'điều mới con nhận ra khi ăn chậm.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> ăn chậm miếng đầu tiên của bữa tối.', '<strong>Sau 1 tuần:</strong> đi bộ chậm 2 phút khi ra công viên.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Chương trình chánh niệm đại trà ở trường (MYRIAD, 8.376 học sinh) không vượt nhóm so sánh sau 1 năm. Vì vậy bài này chỉ dùng chánh niệm như một kỹ năng ngắn, tự chọn (<a href="/bang-chung/">xem trang Bằng chứng</a>).'),
   lb('Đánh giá chuyên môn', 'Năm bước ăn chậm và trò "làm rùa" do daynentang.com thiết kế. Phần chánh niệm chuyên sâu thuộc trang tamhonkhoe.com.')]))
])

# =================== TUẦN 10 ===================
make('t10', 'Bài thói quen tuần 10: góc bình tĩnh. Con dùng nhiệt kế cơn giận và góc bình tĩnh để tự lấy lại bình tĩnh, không phải chỗ phạt.',
 ['Mạch A – Thói quen (Ngón út)', 'Tuần 10, buổi 1', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> chỉ đúng mức giận của mình trên nhiệt kế 1–5 và tự dùng góc bình tĩnh ít nhất 1 lần trong tuần.',
   '<strong>Con nhỏ:</strong> chấp nhận ôm gối hoặc thở cùng bố mẹ khi đang khóc giận.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Một góc yên trong nhà, 1 gối ôm hoặc thú bông to.', 'Giấy vẽ nhiệt kế cơn giận 1–5 và 3 thẻ cách bình tĩnh: thở bong bóng, ôm gối, đếm đến 10.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Khi con giận, người con nóng lên như ấm nước sôi. Mình cần chỗ để nước nguội bớt."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15 phút)</h3>' + ol([
   'Con vẽ nhiệt kế cơn giận. Ghi mức 1 đến 5, mỗi mức một màu.',
   'Kể chuyện: "Hôm qua bố bực vì kẹt xe, bố ở mức 3." Con kể một lần mình giận, ở mức mấy.',
   'Cùng con dựng góc bình tĩnh: gối ôm, thẻ cách bình tĩnh, tranh nhiệt kế. Con đặt tên cho góc.',
   'Tập thử: con giả vờ giận mức 3, đi đến góc, chọn 1 thẻ, làm 2 phút, rồi quay lại nói "Con thấy giận vì…".',
   'Thống nhất luật: góc bình tĩnh là chỗ con tự chọn đến; bố mẹ có thể ngồi cùng.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Cho con ngồi góc bình tĩnh, ôm gối, thở bong bóng cùng bố mẹ.', 'Nói nhẹ: "Khi buồn, mình ôm gối nhé."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Ở mức nào thì con nên đến góc bình tĩnh?', 'Thẻ nào giúp con nhanh bình tĩnh nhất?', 'Bố mẹ có cần góc bình tĩnh không?'])),
 sec(6,'An toàn', ul(['Góc bình tĩnh không phải chỗ phạt hay nhốt; không đóng cửa, không bỏ con một mình khi con hoảng sợ.',
   'Nếu cơn giận của con thường xuyên làm con hoặc người khác bị đau, hãy hỏi bác sĩ nhi hoặc chuyên gia tâm lý.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('1 gối ôm, giấy bút. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Ví dụ ấm nước sôi.'),
   ('Phút 2–8 – Nhiệt kế.', 'Con lớn vẽ nhiệt kế 1–5.'),
   ('Phút 8–15 – Dựng góc.', 'Cả nhà dựng góc bình tĩnh; con nhỏ mang gối vào góc.'),
   ('Phút 15–20 – Tập thử.', 'Con lớn đóng vai, đi theo sơ đồ "khi con giận".')], [
   ('Khi con giận thật:', 'mẹ nói ngắn: "Con đang ở mức mấy? Con muốn ra góc bình tĩnh không? Mẹ ngồi cùng nhé." Chưa giảng giải lúc này.'),
   ('Mẹ làm mẫu:', 'khi mẹ bực, mẹ nói to "Mẹ đang mức 3, mẹ thở một chút", rồi làm thật.'),
   ('Nhắn bố 1 câu:', 'con đặt tên góc là gì.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> hỏi con mức giận hôm nay, cả lúc vui (mức 1).', '<strong>Sau 1 tuần:</strong> đếm số lần con tự dùng góc. Khen cụ thể lần con tự đi đến góc.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Bố mẹ làm mẫu, đáp lại và chỉ dạy về cảm xúc gắn với kỹ năng điều chỉnh cảm xúc tốt hơn ở trẻ mầm non; mức liên hệ nhỏ (Zinsser, Gordon &amp; Jiang 2021).'),
   lb('Đã xác nhận', 'Chương trình Parenting for Lifelong Health của WHO/UNICEF có phần giúp cha mẹ và trẻ xử lý cảm xúc và dùng hậu quả không bạo lực (<a href="https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health">WHO</a>).'),
   lb('Đánh giá chuyên môn', 'Nhiệt kế cơn giận và góc bình tĩnh là công cụ do daynentang.com thiết kế, chưa có nghiên cứu riêng.')]))
])

make('k10', 'Bài khoa học tuần 10: thiết kế thuyền chở nhiều đồ nhất. Con làm kỹ sư nhí theo vòng Hỏi – Nghĩ – Làm – Thử – Sửa.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 10, buổi 2', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> vẽ thiết kế, làm 2 thuyền giấy bạc khác dáng, đếm số khối mỗi thuyền chở được, và sửa thiết kế 1 lần.',
   '<strong>Con nhỏ:</strong> đặt khối vào thuyền và nói "chìm rồi!".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Giấy bạc (giấy nhôm) cắt 2 miếng bằng nhau, cỡ 20×20 cm.', 'Chậu nước nông trên khăn tắm cũ.', '10–15 khối Duplo hoặc nắp chai to làm "hàng".'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Có một kho hàng cần chở qua sông. Con là kỹ sư. Thuyền của con chở được bao nhiêu hàng?"</p>'),
 sec(4,'Hoạt động chính – Hỏi → Nghĩ → Làm → Thử → Sửa', '<h3>Con lớn (20–25 phút)</h3>' + ol([
   '<strong>Hỏi:</strong> "Vấn đề là gì?" (chở nhiều hàng mà không chìm).',
   '<strong>Nghĩ và vẽ:</strong> con vẽ 2 kiểu thuyền: một đáy hẹp, một đáy rộng thành cao.',
   '<strong>Làm:</strong> gấp 2 thuyền từ 2 miếng giấy bạc bằng nhau.',
   '<strong>Thử:</strong> thả từng thuyền, xếp khối từng cái. Đếm đến khi thuyền chìm. Ghi số.',
   '<strong>Sửa:</strong> con chọn thuyền tốt hơn, sửa một điều (thành cao hơn, đáy phẳng hơn), thử lại.']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Người lớn ngồi sát. Cho con đặt từng khối vào thuyền.', 'Khi thuyền chìm: "Chìm rồi! Vớt lên nào."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Thuyền nào chở nhiều hơn? Vì sao con nghĩ vậy?', 'Lần sửa, con đổi điều gì? Kết quả thế nào?', 'Kỹ sư ngoài đời làm những gì?'])),
 sec(6,'An toàn', ul(['Người lớn ngồi sát; con nhỏ luôn trong tầm tay. Đổ nước ngay sau buổi.', 'Mép giấy bạc có thể sắc; người lớn gấp mép trước.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('giấy bạc, chậu nước nông, khăn, 10 khối Duplo. Tổng 25 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Kể bài toán chở hàng qua sông.'),
   ('Phút 2–8 – Nghĩ và làm.', 'Con lớn vẽ và gấp 2 thuyền.'),
   ('Phút 8–18 – Thử.', 'Thả thuyền, đếm khối. Con nhỏ đặt khối cùng.'),
   ('Phút 18–23 – Sửa.', 'Con lớn sửa một điều, thử lại.'),
   ('Phút 23–25 – Dọn.', 'Đổ nước ngay, lau sàn.')], [
   ('Trước khi bắt đầu:', 'mẹ đặt điện thoại xa. Phải rời đi thì dừng buổi và bế con nhỏ theo.'),
   ('Nhắn bố 1 câu:', 'thuyền tốt nhất chở được mấy khối.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> hỏi: "Nếu làm lại, con sẽ sửa gì nữa?"', '<strong>Sau 1 tuần:</strong> con dùng vòng Hỏi – Nghĩ – Làm – Thử – Sửa để làm một đồ khác (cầu giấy giữ được sách).'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Chuẩn khoa học NGSS cho lớp mẫu giáo – lớp 2 có phần thiết kế kỹ thuật (K-2-ETS1): xác định vấn đề, vẽ mô hình cho thấy hình dạng giúp vật hoạt động, và so sánh dữ liệu thử của hai thiết kế (<a href="https://www.nextgenscience.org/node/1116">NGSS</a>).'),
   lb('Đánh giá chuyên môn', '"Đáy rộng, thành cao thường chở được nhiều hơn" là điều con tự kiểm chứng trong bài; kết quả phụ thuộc cách gấp.'),
   lb('Đã xác nhận', f'Giữ trẻ trong tầm tay khi chơi với nước và đổ nước sau khi dùng ({WATER}).')]))
])

make('g10', 'Bài giá trị tuần 10: giữ lời hứa nhỏ. Con và bố mẹ cùng tập hứa điều nhỏ và làm đúng, để cả nhà tin nhau hơn.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 10, buổi 3', '15–20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> chọn 1 lời hứa nhỏ cho tuần, giữ ít nhất 5/7 ngày, và tự đánh dấu trên thẻ lời hứa.',
   '<strong>Con nhỏ:</strong> trả lại đồ chơi đã mượn khi được nhắc "Mình hứa trả bạn rồi".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['2 thẻ lời hứa (giấy nhỏ có 7 ô): một của con lớn, một của bố hoặc mẹ.', '1 quả bóng hoặc đồ chơi to để đóng vai mượn – trả.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Kể chuyện ngắn: "Tí mượn bóng của Mướp, hứa chiều trả. Chiều đến, Tí đang chơi vui… Con đoán Tí làm gì?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Kể tiếp: Tí dừng chơi, mang bóng trả Mướp đúng hẹn. Mướp vui và lần sau lại cho Tí mượn.',
   'Xem sơ đồ "vòng lời hứa". Hỏi: "Vì sao Mướp lại cho Tí mượn tiếp?"',
   'Con chọn 1 lời hứa nhỏ, làm được mỗi ngày. Ví dụ: "Con hứa cất cặp sau khi đi học về."',
   'Bố hoặc mẹ cũng chọn 1 lời hứa với con và có thẻ riêng. Ví dụ: "Bố hứa đọc truyện 10 phút mỗi tối."',
   'Mỗi tối, cả hai cùng đánh dấu thẻ của mình.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Đóng vai: con nhỏ mượn bóng của anh, bố mẹ nói "Chơi xong trả anh nhé."', 'Sau 1 phút, nhắc "Mình hứa trả anh rồi." Con trả, cả nhà vỗ tay.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Khi ai đó hứa với con rồi quên, con thấy thế nào?', 'Lời hứa nhỏ và lời hứa lớn, cái nào nên tập trước?', 'Nếu không giữ được lời hứa thì mình làm gì? (nói thật, xin lỗi, hẹn lại)'])),
 sec(6,'An toàn', ul(['Không bắt con hứa những việc quá sức hay không an toàn.', 'Bố mẹ chỉ hứa điều chắc chắn làm được.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('2 thẻ lời hứa, 1 quả bóng. Tổng 15 phút.', [
   ('Phút 0–3 – Kể chuyện.', 'Tí mượn bóng và trả đúng hẹn.'),
   ('Phút 3–6 – Con nhỏ.', 'Đóng vai mượn – trả bóng.'),
   ('Phút 6–13 – Thẻ lời hứa.', 'Con lớn và mẹ mỗi người chọn 1 lời hứa.'),
   ('Phút 13–15 – Kết thúc.', 'Dán 2 thẻ cạnh nhau ở chỗ dễ thấy.')], [
   ('Quan trọng nhất:', 'mẹ giữ đúng lời hứa của mình. Trẻ học giữ lời qua việc người lớn giữ lời.'),
   ('Khi mẹ lỡ quên:', 'nói thật: "Mẹ quên rồi, mẹ xin lỗi. Tối nay mẹ đọc bù." Đó cũng là bài học.'),
   ('Nhắn bố 1 câu:', 'lời hứa con chọn.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi tối:</strong> cùng đánh dấu thẻ lời hứa.', '<strong>Sau 1 tuần:</strong> đếm ô đã đánh dấu. Con muốn giữ lời hứa này hay chọn lời hứa mới?'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Thử nghiệm với 28 trẻ 3,5–6 tuổi: khi người lớn giữ lời hứa trước đó, trẻ chờ trung bình khoảng 12 phút; khi người lớn thất hứa, trẻ chờ khoảng 3 phút (Kidd, Palmeri &amp; Aslin, <em>Cognition</em> 2013, <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3730121/">PMC</a>).'),
   lb('Suy luận', 'Vì vậy bài này yêu cầu cả bố mẹ cùng giữ một lời hứa; nghiên cứu có cỡ mẫu nhỏ và làm trong phòng thí nghiệm.'),
   lb('Đánh giá chuyên môn', 'Thẻ lời hứa và chuyện Tí – Mướp do daynentang.com thiết kế.')]))
])

# =================== TUẦN 11 ===================
make('t11', 'Bài thói quen tuần 11: dự án chậu rau gia đình. Con dùng cả năm ngón tay của Bàn tay nền tảng trong một dự án thật.',
 ['Mạch A – Thói quen (Cả bàn tay)', 'Tuần 11, buổi 1', '30 phút + 3 phút mỗi ngày trong 3–4 tuần'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> lập kế hoạch dự án 5 bước, nhận việc của mình, và chăm chậu rau ít nhất 5/7 ngày.',
   '<strong>Con nhỏ:</strong> tưới chậu rau bằng cốc nhỏ cùng người lớn mỗi ngày.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 chậu nhựa có lỗ thoát nước, đất trồng rau, đĩa lót.', '1 gói hạt rau nhanh lớn (hỏi người bán hạt loại hợp mùa).', 'Bình tưới nhỏ hoặc cốc nhựa, găng tay vải nếu có.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Mười tuần qua mình học 5 ngón tay. Giờ dùng cả bàn tay cho một dự án thật: trồng rau cho cả nhà ăn."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (20–25 phút)</h3>' + ol([
   'Xem sơ đồ kế hoạch 5 bước: chọn hạt → chuẩn bị chậu → gieo → chăm mỗi ngày → thu hoạch.',
   'Nối 5 ngón với việc trong dự án (xem sơ đồ "Cả bàn tay trong một dự án").',
   'Con đặt "đích": ngày dự kiến thu hoạch, ghi lên lịch.',
   'Cùng chuẩn bị chậu, cho đất vào, gieo hạt theo hướng dẫn trên gói.',
   'Con nhận việc hằng ngày: tưới sáng hoặc kiểm tra đất ẩm. Vẽ bảng chăm rau 7 ngày.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Con xúc đất bằng xẻng nhựa to vào chậu (người lớn giữ chậu).', 'Con tưới nhẹ bằng cốc nhỏ. Mỗi ngày tưới cùng anh.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Ngón nào con dùng nhiều nhất trong dự án?', 'Nếu một ngày quên tưới thì sao?', 'Thu hoạch xong, con muốn nấu món gì?'])),
 sec(6,'An toàn', ul(['Người lớn giữ gói hạt; hạt là vật nhỏ, không để con nhỏ cầm.', 'Không ăn đất; rửa tay kỹ sau khi làm. Đeo găng nếu da con dễ kích ứng.',
   'Không dùng phân bón hóa học hay thuốc trừ sâu khi trẻ chăm cây.', 'Rửa rau kỹ trước khi nấu.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('chậu, đất trồng, gói hạt, cốc tưới. Tổng 30 phút.', [
   ('Phút 0–3 – Mở đầu.', 'Nói về dự án dùng cả bàn tay.'),
   ('Phút 3–10 – Kế hoạch.', 'Con lớn xem sơ đồ, đặt ngày thu hoạch.'),
   ('Phút 10–22 – Gieo.', 'Con nhỏ xúc đất; con lớn gieo hạt theo hướng dẫn gói. Mẹ giữ gói hạt.'),
   ('Phút 22–28 – Bảng chăm rau.', 'Con lớn vẽ bảng 7 ngày.'),
   ('Phút 28–30 – Dọn.', 'Rửa tay cả nhà, quét đất rơi.')], [
   ('Mỗi ngày 3 phút:', 'con lớn kiểm tra đất, con nhỏ tưới. Đánh dấu bảng.'),
   ('Nhắn bố 1 câu:', 'ngày con đặt để thu hoạch.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi ngày:</strong> chăm chậu rau và đánh dấu bảng.', '<strong>Mỗi tuần:</strong> đo cây như bài K4 và vẽ thêm vào nhật ký.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Dự án dài ngày giúp con dùng lại các thói quen đã học trong một việc thật; dự án do daynentang.com thiết kế.'),
   lb('Cần kiểm chứng', 'Thời gian thu hoạch phụ thuộc loại hạt, mùa và nơi ở. Hãy làm theo hướng dẫn trên gói hạt.')]))
])

make('k11', 'Bài khoa học tuần 11: con hỏi – con thử. Con biến câu hỏi của mình thành câu "Nếu… thì…?" và tự làm thí nghiệm.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 11, buổi 2', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> tự đặt 1 câu hỏi "Nếu… thì…?", đoán, làm thí nghiệm công bằng và kể kết quả.',
   '<strong>Con nhỏ:</strong> hỏi "Cái gì đây?" hoặc chỉ tay hỏi trong lúc chơi, và làm thử cùng anh.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Danh sách câu hỏi con đã hỏi trong tuần (bố mẹ ghi lại trước).', 'Đồ trong nhà tùy câu hỏi con chọn. Giấy 4 ô: Câu hỏi · Con đoán · Con thử · Kết quả.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Đọc vài câu hỏi con từng hỏi: "Tuần này con hỏi rất hay. Hôm nay con chọn một câu để tự tìm câu trả lời."</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (20–25 phút)</h3>' + ol([
   'Con chọn 1 câu hỏi. Cùng xem sơ đồ "câu hỏi thử được".',
   'Đổi câu "Vì sao…?" thành "Nếu… thì…?". Ví dụ: "Vì sao đá chìm?" → "Nếu thả đá to và đá nhỏ thì cái nào chìm nhanh hơn?"',
   'Con viết hoặc vẽ vào 4 ô. Nhớ luật thí nghiệm công bằng: chỉ đổi một điều.',
   'Con tự làm thí nghiệm. Bố mẹ chỉ giữ an toàn, không làm hộ.',
   'Con kể kết quả và nêu một câu hỏi mới.']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Con nhỏ làm cùng anh: thả đồ, đổ nước, tùy thí nghiệm.', 'Khi con chỉ tay, bố mẹ gọi tên và hỏi lại: "Con nghĩ sẽ thế nào?"'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Câu hỏi nào khó biến thành thí nghiệm? Vì sao?', 'Kết quả có giống con đoán không?', 'Câu hỏi mới của con là gì?'])),
 sec(6,'An toàn', ul(['Bố mẹ duyệt thí nghiệm trước: không lửa, không điện, không hóa chất, không dao, không nếm.', 'Có nước thì người lớn ngồi sát và đổ nước ngay sau đó.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('danh sách câu hỏi của con, giấy 4 ô, đồ trong nhà. Tổng 25 phút.', [
   ('Phút 0–3 – Mở đầu.', 'Đọc câu hỏi con từng hỏi.'),
   ('Phút 3–8 – Đổi câu hỏi.', 'Cùng con biến câu hỏi thành "Nếu… thì…?"'),
   ('Phút 8–20 – Thử.', 'Con lớn làm; con nhỏ phụ. Mẹ chỉ giữ an toàn.'),
   ('Phút 20–25 – Kể lại.', 'Con lớn kể kết quả và câu hỏi mới.')], [
   ('Nếu câu hỏi không thử được ở nhà:', 'ghi lại "để hỏi bố" hoặc "tìm ở thư viện". Không phải câu hỏi nào cũng thử được, và điều đó bình thường.'),
   ('Nhắn bố 1 câu:', 'câu hỏi "Nếu… thì…" của con.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi ngày:</strong> bố mẹ ghi lại câu hỏi hay của con vào "sổ câu hỏi".', '<strong>Sau 1 tuần:</strong> con chọn thí nghiệm hay nhất để mang ra triển lãm tuần 12.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'NGSS cho lớp mẫu giáo – lớp 2 yêu cầu trẻ dùng câu hỏi và quan sát để xác định vấn đề, và so sánh dữ liệu thử (<a href="https://www.nextgenscience.org/node/1116">NGSS K-2-ETS1</a>).'),
   lb('Đánh giá chuyên môn', 'Cách đổi "Vì sao…?" thành "Nếu… thì…?" là kỹ thuật dạy khoa học phổ biến; bài do daynentang.com thiết kế.')]))
])

make('g11', 'Bài giá trị tuần 11: tử tế với chính mình. Khi thất bại, con tập nói với mình lời tử tế như nói với bạn thân.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 11, buổi 3', '15–20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> đổi 2 câu tự chê thành câu tử tế, và làm 3 bước tử tế với chính mình trong một tình huống đóng vai.',
   '<strong>Con nhỏ:</strong> tự ôm mình hoặc đặt tay lên ngực khi bố mẹ nói "Không sao đâu".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Sơ đồ "nói với mình như nói với bạn" và "3 bước tử tế với chính mình".', 'Vài khối gỗ để xếp tháp.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Nếu bạn thân của con làm đổ tháp và khóc, con sẽ nói gì với bạn?" Ghi lại câu con nói.</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (12–15 phút)</h3>' + ol([
   'Hỏi tiếp: "Còn khi tháp của con đổ, con hay nói gì với mình?" (ví dụ "Mình dở quá").',
   'So sánh hai câu trên sơ đồ. Cùng đổi câu tự chê thành câu tử tế: "Mình dở quá" → "Mình làm lại được mà."',
   'Tập 3 bước: <strong>nhận ra</strong> "mình đang buồn" → <strong>nhớ rằng</strong> "ai cũng có lúc thế" → <strong>nói với mình</strong> lời tử tế, tay đặt lên ngực.',
   'Đóng vai: con xếp tháp, bố mẹ "lỡ" làm đổ. Con làm 3 bước.',
   'Bố mẹ kể một lần mình thất bại và cách mình tự an ủi.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Khi tháp của con đổ, bố mẹ đặt tay lên ngực mình: "Không sao đâu." Mời con làm theo.', 'Ôm con và cùng xây lại.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Vì sao mình dễ tử tế với bạn mà khó tử tế với mình?', 'Câu tử tế nào con thích nhất?', 'Tử tế với mình có nghĩa là không cần cố gắng nữa không? (không, mình vẫn thử lại)'])),
 sec(6,'An toàn', ul(['Nếu con thường xuyên nói "con ghét mình" hay có ý làm đau mình, hãy nói chuyện với bác sĩ nhi hoặc chuyên gia tâm lý. Gọi 111 hoặc 115 khi khẩn cấp.',
   'Không chê bai con khi con đang buồn.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('vài khối gỗ, sơ đồ. Tổng 15 phút, nên làm buổi tối.', [
   ('Phút 0–3 – Mở đầu.', 'Hỏi con sẽ nói gì với bạn thân đang buồn.'),
   ('Phút 3–8 – Đổi câu.', 'Cùng con đổi 2 câu tự chê thành câu tử tế.'),
   ('Phút 8–13 – Đóng vai.', 'Xếp tháp, mẹ làm đổ, con làm 3 bước. Con nhỏ làm theo động tác tay.'),
   ('Phút 13–15 – Kết thúc.', 'Mẹ kể một lần mẹ tự an ủi mình.')], [
   ('Để ý lời của mẹ:', 'con học cách nói với chính mình từ cách bố mẹ nói với con và với chính bố mẹ.'),
   ('Nhắn bố 1 câu:', 'câu tử tế con chọn.')])),
 sec(8,'Ôn lại', ul(['<strong>Khi con thất bại trong tuần:</strong> hỏi "Con sẽ nói gì với bạn thân nếu bạn gặp chuyện này?"', '<strong>Sau 1 tuần:</strong> con viết hoặc vẽ câu tử tế yêu thích, dán ở góc bình tĩnh.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Phân tích gộp 19 nghiên cứu với khoảng 7.000 thanh thiếu niên 10–19 tuổi: tự trắc ẩn cao gắn với ít lo âu, trầm cảm, căng thẳng hơn (r = −0,55). Đây là tương quan, phần lớn là nghiên cứu cắt ngang (Marsh, Chan &amp; MacBeth, <em>Mindfulness</em>, <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6061226">PMC</a>).'),
   lb('Suy luận', 'Áp dụng cho trẻ 7 tuổi là cách hiểu của chúng tôi; nghiên cứu làm với tuổi lớn hơn.'),
   lb('Đánh giá chuyên môn', 'Ba bước trong bài phỏng theo ý tưởng tự trắc ẩn (nhận ra, nhớ mình không đơn độc, tử tế với mình), viết lại bằng lời cho trẻ.')]))
])

# =================== TUẦN 12 ===================
make('t12', 'Bài thói quen tuần 12: lễ Bàn tay nền tảng. Con kể lại 5 ngón tay, cả nhà khen cụ thể, và chọn thói quen giữ tiếp.',
 ['Mạch A – Thói quen (Cả bàn tay)', 'Tuần 12, buổi 1', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> kể đủ 5 ngón tay, mỗi ngón kèm một ví dụ mình đã làm, và chọn 2 thói quen giữ tiếp.',
   '<strong>Con nhỏ:</strong> giơ ngón cái khi được hỏi "Ai tự làm được?" và làm một việc tự phục vụ trước cả nhà.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Sơ đồ Bàn tay nền tảng, các bảng và tranh con đã vẽ trong 11 tuần.', 'Bằng khen bố mẹ tự vẽ (không ghi tên con nếu chụp ảnh đăng mạng).', 'Bữa ăn nhẹ hoặc món con thích để làm lễ.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Hôm nay là lễ tốt nghiệp nhỏ của nhà mình. Con là người kể chuyện chính."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (20 phút)</h3>' + ol([
   'Con đặt bàn tay lên giấy, vẽ viền bàn tay. Mỗi ngón ghi hoặc vẽ thói quen của ngón đó.',
   'Con kể từng ngón kèm ví dụ: "Ngón cái: con tự xếp cặp được rồi."',
   'Mỗi người trong nhà khen con một điều cụ thể, gắn với một ngón.',
   'Con chọn 2 thói quen muốn giữ tiếp sau khóa học, đánh dấu lên hình bàn tay.',
   'Trao bằng khen. Dán bàn tay của con lên tường.']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Con làm một việc tự phục vụ trước cả nhà (cất dép, rót nước).', 'Cả nhà giơ ngón cái. Vẽ viền bàn tay nhỏ của con cạnh bàn tay anh.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Ngón nào con thấy mình tiến bộ nhất?', 'Ngón nào con muốn tập thêm?', 'Con muốn khóa tiếp theo học gì?'])),
 sec(6,'An toàn', ul(['Không đăng ảnh mặt con hay bằng khen có tên con lên mạng.', 'Bút vẽ và đồ ăn nhẹ phù hợp với con nhỏ.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('giấy to, bút sáp, bằng khen tự vẽ. Tổng 25 phút. Có thể gọi video để bố cùng khen.', [
   ('Phút 0–2 – Mở đầu.', '"Hôm nay là lễ tốt nghiệp nhỏ."'),
   ('Phút 2–10 – Vẽ bàn tay.', 'Con lớn vẽ viền tay, ghi 5 thói quen.'),
   ('Phút 10–17 – Kể và khen.', 'Con kể từng ngón; mẹ (và bố qua video) khen cụ thể.'),
   ('Phút 17–22 – Con nhỏ.', 'Con nhỏ làm một việc tự phục vụ; vẽ bàn tay nhỏ.'),
   ('Phút 22–25 – Trao bằng.', 'Chọn 2 thói quen giữ tiếp, dán bàn tay lên tường.')], [
   ('Khen cụ thể:', '"Con tự đánh răng mỗi tối mà không cần nhắc" tốt hơn "Con giỏi lắm".'),
   ('Nhắn bố 1 câu:', '2 thói quen con chọn giữ tiếp.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> nhắc 2 thói quen con chọn, đánh dấu trên bảng.', '<strong>Sau 1 tháng:</strong> mở lại hình bàn tay, hỏi con còn giữ thói quen nào.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Khen cụ thể là một thành phần của chương trình nuôi dạy tích cực Parenting for Lifelong Health (WHO/UNICEF).'),
   lb('Đánh giá chuyên môn', 'Lễ Bàn tay nền tảng do daynentang.com thiết kế để con nhìn lại và chọn thói quen giữ tiếp.')]))
])

make('k12', 'Bài khoa học tuần 12: triển lãm khoa học gia đình. Con chọn thí nghiệm hay nhất, làm áp phích và tự giải thích cho khách.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 12, buổi 2', '45–60 phút (cuối tuần)'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> chọn 2–4 thí nghiệm, làm áp phích 4 ô cho mỗi bàn, và tự giải thích cho ít nhất 2 người khách.',
   '<strong>Con nhỏ:</strong> làm lại một thí nghiệm đơn giản (thả vật nổi chìm, tưới mầm) cho khách xem.'])),
 sec(2,'Chuẩn bị (10 phút)', ul(['Đồ của các thí nghiệm con chọn (chậu nổi chìm, cốc mầm, đèn pin, ván dốc…).', 'Giấy to làm áp phích, bút sáp.', 'Mời khách: ông bà, hàng xóm thân, hoặc gọi video với người thân ở xa.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Con là nhà khoa học nhỏ. Hôm nay con mở triển lãm để kể cho mọi người những gì con đã khám phá."</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (35–45 phút)</h3>' + ol([
   'Con chọn 2–4 thí nghiệm thích nhất trong 11 tuần.',
   'Mỗi thí nghiệm một áp phích 4 ô: câu hỏi – con đoán – con thử – kết quả.',
   'Xếp các bàn theo sơ đồ triển lãm. Tập giới thiệu một lần với bố mẹ.',
   'Khi khách đến: con mời khách đoán trước, rồi làm thí nghiệm, rồi giải thích kết quả.',
   'Cuối buổi, hỏi khách: "Bác thích bàn nào nhất? Bác có câu hỏi gì không?"']) +
   '<h3>Con nhỏ (10 phút)</h3>' + ol(['Con nhỏ "phụ trách" bàn nổi – chìm hoặc bàn mầm: thả vật, tưới cây cho khách xem.', 'Khách vỗ tay cảm ơn con.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Khách hỏi câu gì làm con bất ngờ?', 'Thí nghiệm nào con giải thích tốt nhất?', 'Nếu làm triển lãm lần nữa, con muốn thêm thí nghiệm gì?'])),
 sec(6,'An toàn', ul(['Bàn có nước: người lớn đứng cạnh suốt buổi, đổ nước ngay sau đó.', 'Không chụp ảnh mặt con để đăng mạng; nếu muốn lưu, chụp áp phích và tay con.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('đồ 2 thí nghiệm dễ (nổi chìm, mầm), giấy to, bút. Tổng 45 phút, gọi video để bố làm khách.', [
   ('Phút 0–10 – Chọn và chuẩn bị.', 'Con lớn chọn 2 thí nghiệm, bày bàn.'),
   ('Phút 10–25 – Áp phích.', 'Con lớn làm 2 áp phích 4 ô.'),
   ('Phút 25–40 – Triển lãm.', 'Bố gọi video làm khách; ông bà hoặc hàng xóm đến xem nếu được.'),
   ('Phút 40–45 – Dọn.', 'Đổ nước, cất đồ, cảm ơn khách.')], [
   ('Giữ nhẹ nhàng:', 'triển lãm nhỏ trong phòng khách là đủ. Điều quan trọng là con được kể.'),
   ('Nhắn bố 1 câu:', 'câu hỏi hay nhất của khách.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> con kể lại triển lãm cho người chưa đến.', '<strong>Sau 1 tháng:</strong> mở "sổ câu hỏi", chọn một câu mới để thử.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'NGSS K–2 nhấn mạnh việc trẻ thu thập dữ liệu và trình bày, so sánh kết quả (<a href="https://www.nextgenscience.org/node/1116">NGSS</a>).'),
   lb('Đánh giá chuyên môn', 'Triển lãm gia đình và áp phích 4 ô do daynentang.com thiết kế.')]))
])

make('g12', 'Bài giá trị tuần 12: ôn bốn giá trị, vẽ ước nguyện và đánh giá cuối khóa bằng bảng quan sát.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 12, buổi 3', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> kể một ví dụ của mình cho mỗi giá trị (trung thực, biết ơn, tử tế, trách nhiệm) và vẽ một ước nguyện cho gia đình.',
   '<strong>Con nhỏ:</strong> dán ngôi sao lên "cây ước nguyện" và nói "cảm ơn" khi nhận lại.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Sơ đồ bốn giá trị, giấy to vẽ "cây ước nguyện", ngôi sao cắt sẵn.', '<a href="/cong-cu/bang-quan-sat/">Bảng quan sát 0–1–2</a> đã chấm ở tuần 0 và tuần 6.', 'Lọ cảm ơn từ bài G2.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Đổ lọ cảm ơn ra, đọc vài mẩu giấy. "Mười hai tuần qua nhà mình đã cảm ơn bao nhiêu người!"</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   'Xem sơ đồ bốn giá trị. Với mỗi giá trị, con kể một lần mình đã làm: nói thật về… , cảm ơn… , giúp… , giữ lời hứa…',
   'Mỗi người vẽ một ngôi sao ghi ước nguyện cho gia đình, dán lên cây ước nguyện.',
   'Cả nhà đọc to các ước nguyện.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Con dán ngôi sao lên cây.', 'Anh đưa con một ngôi sao, con nói "cảm ơn".']) +
   '<h3>Bố mẹ (sau buổi, 10 phút): Đánh giá cuối khóa</h3>' + ol([
   'Chấm bảng quan sát cột tuần 12 cho từng con.',
   'So với tuần 0 và tuần 6: mục nào tăng, mục nào giữ nguyên.',
   'Đếm lại số lần khen cụ thể và la mắng trong 3 ngày; so với tuần 0.',
   'Ghi 3 dòng: điều tiến bộ nhất, điều chưa được, điều muốn giữ.',
   'Nếu muốn, <a href="/chia-se/?bai=g3-g12#gui">chia sẻ</a> kết quả (ẩn danh hoặc công khai) để giúp các gia đình khác và giúp sửa khóa học.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Giá trị nào con thấy dễ nhất? Khó nhất?', 'Ước nguyện của con có cần cả nhà cùng làm không?', 'Sau khóa này, con muốn cả nhà học gì tiếp?'])),
 sec(6,'An toàn', ul(['Kết quả bảng quan sát chỉ để gia đình tự theo dõi, không dùng để so sánh các con với nhau hay chẩn đoán.',
   'Nếu lo lắng về sự phát triển hay cảm xúc của con, hãy hỏi bác sĩ nhi.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('lọ cảm ơn, giấy to, ngôi sao cắt sẵn, bảng quan sát. Tổng 25 phút + 10 phút chấm bảng.', [
   ('Phút 0–3 – Mở đầu.', 'Đọc vài mẩu giấy trong lọ cảm ơn.'),
   ('Phút 3–12 – Bốn giá trị.', 'Con lớn kể ví dụ cho từng giá trị.'),
   ('Phút 12–22 – Cây ước nguyện.', 'Mỗi người dán một ngôi sao; bố gửi ước nguyện qua tin nhắn để mẹ dán hộ.'),
   ('Phút 22–25 – Kết thúc.', 'Đọc to các ước nguyện.')], [
   ('Chấm bảng cùng bố:', 'nếu được, bố mẹ chấm và so sánh cùng nhau qua điện thoại.'),
   ('Nhắn bố 1 câu:', 'ước nguyện của con.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi tháng:</strong> mở cây ước nguyện và lọ cảm ơn, thêm vào khi có điều mới.', '<strong>Sau 3 tháng:</strong> chấm lại bảng quan sát để xem thói quen còn giữ không.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước và sau 12 tuần không có nhóm đối chứng; thay đổi có thể do con lớn lên. Đây là thử nghiệm khả thi, không phải bằng chứng hiệu quả.'),
   lb('Đã xác nhận', 'Các chương trình nuôi dạy có bằng chứng như Parenting for Lifelong Health đo thay đổi hành vi nuôi dạy tích cực của bố mẹ; khóa này dùng cách đo đơn giản tương tự (đếm khen cụ thể và la mắng).')]))
])
print('weeks 9-12 built')
