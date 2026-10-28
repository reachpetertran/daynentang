from lessons import lesson, sec, JOURNAL

U = '/khoa-hoc/gia-dinh-2-8/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'

HARVARD = '<a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Harvard Center on the Developing Child</a>'
WATER = ('<a href="https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/">CPSC, Hoa Kỳ</a>')
SMALL = 'Mọi vật trong tầm với của con nhỏ phải to hơn lõi giấy vệ sinh.'

L = {
 't2': (2, 't2-thu-sai-thu-lai', 'T2', 'Thử – sai – thử lại'),
 'k2': (2, 'k2-nuoc-rot-dong-tham', 'K2', 'Nước: rót, đong, thấm'),
 'g2': (2, 'g2-ba-dieu-cam-on', 'G2', 'Ba điều cảm ơn'),
 't3': (3, 't3-nhin-dich-roi-di', 'T3', 'Nhìn đích rồi đi'),
 'k3': (3, 'k3-hat-dau-nay-mam', 'K3', 'Hạt đậu nảy mầm'),
 'g3': (3, 'g3-viec-tot-bi-mat', 'G3', 'Việc tốt bí mật'),
 't4': (4, 't4-truoc-trong-sau', 'T4', 'Trước – Trong – Sau'),
 'k4': (4, 'k4-mam-cao-bao-nhieu', 'K4', 'Mầm cao bao nhiêu?'),
 'g4': (4, 'g4-dung-tho-noi', 'G4', 'Dừng – Thở – Nói'),
}
ORDER = ['t2','k2','g2','t3','k3','g3','t4','k4','g4']
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
def nav(k):
    i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i > 0 else (U + 'tuan-1/g1-noi-that-long-nhe/', 'G1 – Nói thật, lòng nhẹ')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U + 'tuan-5/t5-viec-quan-trong-lam-truoc/', 'Tuần 5: T5 – Việc quan trọng làm trước')
    return prev, nxt
def make(k, desc, meta, sections):
    w, slug, code, title = L[k]; prev, nxt = nav(k)
    lesson(slug, code, title, '', desc, meta, sections, prev=prev, nxt=nxt, week=w, draft=True)

def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>Mẹ chỉ cần: {need}</em></p><ol>{li}</ol>{nt}</div>'

def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'

# =================== TUẦN 2 ===================
make('t2', 'Bài thói quen tuần 2: khi làm chưa được, con thử cách khác. Thử thách tháp giấy cho con lớn, tháp cốc cho con nhỏ.',
 ['Mạch A – Thói quen (Ngón cái)', 'Tuần 2, buổi 1', '20–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> khi làm chưa được, tự nói "con thử cách khác" và thử ít nhất 2 cách.',
   '<strong>Con nhỏ:</strong> xây lại tháp cốc sau khi tháp đổ, có người lớn làm cùng.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['10 tờ giấy A4 cũ, 1 cuộn băng dính giấy (người lớn cắt sẵn 10 mẩu dài).',
   '5–6 cốc nhựa hoặc hộp sữa chua rửa sạch cho con nhỏ.', 'Tờ giấy kẻ 3 ô: Cách 1 · Cách 2 · Cách 3.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Bố mẹ kể một lần mình làm sai rồi sửa: "Hôm qua bố nấu cơm bị nhão. Lần sau bố bớt nước. Thử lại thì được." Hỏi con: "Khi làm chưa được, mình có thể làm gì?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15–20 phút): Thử thách tháp giấy</h3>' + ol([
   'Thử thách: dùng 10 tờ giấy và 10 mẩu băng dính, xây tháp đứng được cao nhất. Không dùng thêm đồ khác.',
   '<strong>Cách 1</strong> (5 phút): con tự làm. Tháp đổ cũng không sao. Con vẽ nhanh cách 1 vào ô đầu.',
   'Bố mẹ hỏi: "Tháp đổ ở đâu? Lần này con đổi gì?" Không gợi ý ngay; chờ con nghĩ 10 giây.',
   '<strong>Cách 2</strong> và <strong>Cách 3</strong>: con thử cách mới, ví dụ cuộn giấy thành ống, gấp đôi làm chân. Vẽ vào ô.',
   'So sánh 3 cách: cách nào cao nhất, vì sao? Con nói câu: "Con thử cách khác thì…"']) +
   '<h3>Con nhỏ (5–10 phút): Tháp cốc</h3>' + ol([
   'Úp cốc xếp chồng 3 chiếc. Cho con đẩy đổ, cả nhà cười.',
   'Nói chậm: "Đổ rồi. Thử lại nào!" Cầm tay con xếp lại.',
   'Lặp lại 3–5 lần. Lần nào con tự đặt được 1 cốc, giơ ngón cái.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Lúc tháp đổ lần đầu, con thấy thế nào?', 'Cách nào con nghĩ ra mà bố mẹ không nghĩ ra?',
   'Ngoài xây tháp, việc gì con cũng có thể "thử cách khác"?'])),
 sec(6,'An toàn', ul(['Người lớn cắt băng dính. Cất kéo sau khi dùng.', 'Mẩu băng dính và giấy vụn để xa con nhỏ; con nhỏ chỉ chơi cốc.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('10 tờ giấy, băng dính, 5 cốc nhựa. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Mẹ kể một lần mẹ làm sai rồi sửa. Hỏi con: "Khi làm chưa được thì làm gì?"'),
   ('Phút 2–4 – Con nhỏ tháp cốc.', 'Xếp, đẩy đổ, xếp lại 3 lần. Con lớn giúp em.'),
   ('Phút 4–14 – Tháp giấy.', 'Con lớn thử 2 cách, mỗi cách 5 phút. Mẹ chỉ hỏi "Lần này con đổi gì?"'),
   ('Phút 14–18 – So sánh.', 'Con nói cách nào cao hơn và vì sao.'),
   ('Phút 18–20 – Dọn.', 'Hai con cùng gom giấy, cất cốc.')], [
   ('Khi con bực vì tháp đổ:', '"Đổ rồi, bực thật. Mình thở một hơi rồi thử cách khác nhé." Không làm hộ con.'),
   ('Khen thế nào:', 'Khen cách con nghĩ: "Con gấp đôi giấy làm chân, hay đấy!" Không khen "con thông minh".'),
   ('Nhắn bố 1 câu:', 'cách nào con nghĩ ra.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> khi con làm chưa được việc gì, nhắc nhẹ: "Cách 2 là gì nhỉ?"',
   '<strong>Sau 1 tuần:</strong> đếm số lần con tự nói "con thử cách khác". Ghi vào nhật ký.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đã xác nhận]</span> Các can thiệp "tư duy phát triển" chỉ có hiệu quả trung bình rất nhỏ (Macnamara &amp; Burgoyne 2023, <em>Psychological Bulletin</em>). Vì vậy bài này dạy hành động cụ thể: thử cách khác, so sánh cách.',
   '<span class="label">[Suy luận]</span> Khen chiến lược con dùng thay vì khen trí thông minh là cách áp dụng nguyên tắc trên; chúng tôi không hứa hiệu quả lớn.',
   '<span class="label">[Đánh giá chuyên môn]</span> Thử thách tháp giấy và tháp cốc do daynentang.com thiết kế, chưa có nghiên cứu riêng.']))
])

make('k2', 'Bài khoa học tuần 2: con đoán rồi thử cốc nào chứa nhiều nước hơn, vật nào thấm nhiều nước nhất.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 2, buổi 2', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> đoán trước, rồi đếm số cốc nhỏ để biết cốc nào chứa nhiều hơn và vật nào thấm nhiều nước nhất.',
   '<strong>Con nhỏ:</strong> tự rót nước từ bình nhỏ sang cốc và bóp miếng bọt biển.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 khay hoặc chậu nông, khăn tắm cũ lót sàn.',
   '2 cốc nhựa khác dáng: 1 cao gầy, 1 thấp rộng. 1 cốc nhựa nhỏ làm "cốc đo".',
   '4 vật để thử thấm: miếng bọt biển rửa bát mới, khăn vải, giấy ăn, túi nilon (chỉ con lớn dùng).',
   '1 bình nhựa nhỏ có quai cho con nhỏ. Nước sạch, nông.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Đặt 2 cốc khác dáng cạnh nhau: "Cốc nào đựng được nhiều nước hơn?" Để con đoán và giải thích, chưa nói đáp án.</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (20 phút)</h3>' + ol([
   '<strong>Đoán:</strong> con khoanh cốc nghĩ là chứa nhiều hơn.',
   '<strong>Thử:</strong> rót đầy từng cốc bằng cốc đo, đếm số lần rót. Ghi số.',
   '<strong>Nói lại:</strong> "Cốc cao chưa chắc chứa nhiều hơn. Phải đo mới biết."',
   '<strong>Đoán tiếp:</strong> trong 4 vật, vật nào hút nước nhiều nhất? Con xếp thứ tự.',
   '<strong>Thử:</strong> nhúng từng vật vào khay, nhấc lên, vắt vào cốc đo. Vật nào vắt ra nhiều nước nhất?',
   '<strong>Kể lại:</strong> con kể 1 điều đúng như con đoán và 1 điều bất ngờ.']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Ngồi trước khay, người lớn ngồi sát.',
   'Con rót nước từ bình nhỏ sang cốc. Đổ ra ngoài cũng được; đó là tập luyện.',
   'Đưa con miếng bọt biển: "Nhúng – bóp!" Nói theo: "Nước chảy ra rồi!"'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Vì sao cốc cao lại có thể chứa ít hơn cốc thấp?', 'Ở nhà mình, đồ nào cần thấm nước tốt? Đồ nào cần không thấm?',
   'Lần sau con muốn đo thử cái gì?'])),
 sec(6,'An toàn', ul(['Người lớn ngồi sát, con nhỏ luôn trong tầm tay. Có việc phải đi thì bế con theo.',
   'Không để con lớn trông con nhỏ bên nước.', 'Xong buổi đổ nước ngay, úp khay, lau sàn.',
   'Túi nilon chỉ dùng cho con lớn, cất ngay sau khi thử.', 'Dùng bọt biển mới; không dùng loại có hóa chất tẩy rửa.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('khay nước nông, khăn, 2 cốc khác dáng, 1 cốc đo, bọt biển, khăn vải. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi: "Cốc nào đựng nhiều hơn?" Chưa trả lời.'),
   ('Phút 2–8 – Đo cốc.', 'Con lớn rót và đếm. Con nhỏ rót bình nhỏ vào khay.'),
   ('Phút 8–15 – Thấm nước.', 'Chỉ thử bọt biển và khăn vải. Con lớn vắt và đếm; con nhỏ bóp bọt biển.'),
   ('Phút 15–18 – Kể lại.', 'Con lớn kể 1 điều bất ngờ.'),
   ('Phút 18–20 – Dọn.', 'Đổ nước ngay, lau sàn, con lớn phụ.')], [
   ('Trước khi bắt đầu:', 'mẹ đặt điện thoại xa. Nếu phải rời đi, dừng buổi và bế con nhỏ theo.'),
   ('Nếu con hỏi "vì sao":', '"Mẹ cũng chưa chắc. Mình ghi lại, tối hỏi bố nhé."'),
   ('Nhắn bố 1 câu:', 'cốc nào chứa nhiều hơn.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> khi rót nước uống, hỏi: "Cốc này được mấy cốc đo?"',
   '<strong>Sau 1 tuần:</strong> con tự chọn 2 đồ đựng trong bếp để đoán và đo.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   f'<span class="label">[Đã xác nhận]</span> Trẻ nhỏ có thể đuối nước chỉ với vài inch nước; giữ trẻ trong tầm tay và đổ nước sau khi dùng ({WATER}).',
   '<span class="label">[Đánh giá chuyên môn]</span> Kết quả đo phụ thuộc vào cốc và vật nhà bạn dùng. Chúng tôi không ghi đáp án sẵn; con tự đo.',
   '<span class="label">[Đánh giá chuyên môn]</span> Hoạt động đo bằng "cốc đo" do daynentang.com thiết kế.']))
])

make('g2', 'Bài giá trị tuần 2: thói quen ba điều cảm ơn trước giờ ngủ và một phút thở bong bóng.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 2, buổi 3', '15–20 phút, nên vào buổi tối'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> nói 3 điều cảm ơn trong ngày, mỗi điều kèm "vì…".',
   '<strong>Con nhỏ:</strong> nói hoặc làm động tác "cảm ơn" khi được đưa đồ trong trò chơi.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 hộp hoặc lọ nhựa (không dùng lọ thủy tinh), giấy cắt thành mẩu to, bút sáp.',
   '1 món đồ chơi to để chơi trò "đưa – cảm ơn".'])),
 sec(3,'Mở đầu (2 phút)', '<p>Bố mẹ nói trước: "Hôm nay bố cảm ơn bác bảo vệ, vì bác giữ cửa giúp bố lúc bố bê đồ." Hỏi con: "Hôm nay ai giúp con?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Thở bong bóng (1 phút, cả nhà)</h3>' + ol([
   'Đặt tay lên bụng. Hít vào chậm bằng mũi, bụng phồng như quả bóng.',
   'Thở ra thật chậm bằng miệng như thổi bong bóng. Làm 3 lần.']) +
   '<h3>Con lớn (10–15 phút): Lọ cảm ơn</h3>' + ol([
   'Con nghĩ 3 điều cảm ơn hôm nay. Mỗi điều nói rõ: <em>cảm ơn ai/cái gì, vì sao</em>.',
   'Con viết hoặc vẽ mỗi điều lên một mẩu giấy, bỏ vào lọ.',
   'Bố mẹ cũng bỏ 1 mẩu của mình. Cùng đọc to.',
   'Thứ Bảy cuối tuần, cả nhà đổ lọ ra đọc lại.']) +
   '<h3>Con nhỏ (5 phút): Đưa – cảm ơn</h3>' + ol([
   'Bố mẹ đưa con món đồ chơi: "Bố cho con." Chờ con nói hoặc gật "cảm ơn". Nếu chưa, bố mẹ nói mẫu.',
   'Đổi lượt: con đưa bố mẹ, bố mẹ nói "Cảm ơn con!" thật vui.', 'Lặp lại 4–5 lần.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Điều cảm ơn nào làm con thấy ấm lòng nhất?', 'Người đó có biết con cảm ơn họ không? Mình có thể nói với họ thế nào?',
   'Ngày mai con muốn cảm ơn ai?'])),
 sec(6,'An toàn', ul(['Dùng lọ nhựa, không dùng lọ thủy tinh.', 'Mẩu giấy và bút để xa con nhỏ; con nhỏ chỉ chơi đồ chơi to.',
   'Nếu khi thở con thấy chóng mặt, thở bình thường lại ngay. Chỉ 3 hơi là đủ.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('lọ nhựa, giấy, bút sáp, 1 đồ chơi to. Tổng 15 phút, trước giờ ngủ.', [
   ('Phút 0–2 – Mở đầu.', 'Mẹ nói 1 điều cảm ơn của mẹ hôm nay, kèm "vì…".'),
   ('Phút 2–3 – Thở bong bóng.', 'Cả nhà đặt tay lên bụng, thở 3 hơi.'),
   ('Phút 3–6 – Con nhỏ.', 'Chơi "đưa – cảm ơn" 4 lần. Con lớn làm mẫu cho em.'),
   ('Phút 6–14 – Lọ cảm ơn.', 'Con lớn nói và vẽ 3 điều. Mẹ thêm 1 điều cảm ơn bố.'),
   ('Phút 14–15 – Kết thúc.', 'Đọc to các mẩu giấy, đặt lọ ở chỗ dễ thấy.')], [
   ('Nếu con nói "con không có gì để cảm ơn":', 'gợi ý nhỏ: "Bữa tối nay ai nấu? Ai chơi với con?" Không ép.'),
   ('Tránh:', 'biến lời cảm ơn thành bài kiểm tra hay so sánh với anh em.'),
   ('Nhắn bố 1 câu:', 'một điều con cảm ơn hôm nay.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi tối:</strong> trước khi ngủ, mỗi người nói 1 điều cảm ơn. Chỉ mất 1 phút.',
   '<strong>Sau 1 tuần:</strong> đổ lọ ra đọc lại cùng nhau. Đếm xem có bao nhiêu người được cảm ơn.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đã xác nhận]</span> Thử nghiệm với 221 học sinh đầu tuổi thiếu niên: nhóm "đếm điều may mắn" báo cáo biết ơn, lạc quan và hài lòng với cuộc sống cao hơn (Froh, Sefick &amp; Emmons 2008, <a href="https://proofpositive.org/bc-science/counting-blessings-in-early-adolescents-an-experimental-study-of-gratitude-and-subjective-wellbeing/">tóm tắt</a>).',
   '<span class="label">[Đã xác nhận]</span> Ở 80 trẻ khoảng 5 tuổi, lòng biết ơn gắn với mức hạnh phúc của trẻ; đây là tương quan, không phải nhân quả (Nguyen &amp; Gordon 2020, <em>Journal of Happiness Studies</em>).',
   '<span class="label">[Suy luận]</span> Nghiên cứu trên làm với trẻ lớn hơn hoặc chỉ đo tương quan. Hiệu quả của "lọ cảm ơn" với trẻ 2–8 tuổi chưa được thử trực tiếp.',
   '<span class="label">[Đánh giá chuyên môn]</span> Thở bong bóng là kỹ năng ngắn, tự chọn; chúng tôi không dùng nó như cách chữa lo âu.']))
])

# =================== TUẦN 3 ===================
make('t3', 'Bài thói quen tuần 3: con nhìn đích trước khi làm. Trò ném tất vào rổ và bảng "đích ngày mai".',
 ['Mạch A – Thói quen (Ngón trỏ)', 'Tuần 3, buổi 1', '20–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> tự đặt 1 mục tiêu cho ngày mai, vẽ 2 bước để làm, và tối hôm sau tự đánh dấu.',
   '<strong>Con nhỏ:</strong> chọn 1 trong 2 tranh việc (cất dép hoặc tưới cây) rồi làm việc đó.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['5 đôi tất cuộn tròn, 1 cái rổ.', 'Giấy, bút sáp to. Hai tranh vẽ đơn giản: đôi dép và cái cây.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Giơ ngón trỏ chỉ về cái rổ: "Ngón này chỉ đích. Muốn ném trúng, mình phải nhìn đích trước."</p>'),
 sec(4,'Hoạt động chính', '<h3>Khởi động (cả nhà, 5 phút): Ném tất vào rổ</h3>' + ol([
   'Mỗi người ném 5 lần, đứng sau một vạch. Lượt 1: nhắm mắt ném. Lượt 2: nhìn rổ rồi mới ném.',
   'Đếm số lần trúng. Hỏi: "Lượt nào trúng nhiều hơn? Vì sao?"']) +
   '<h3>Con lớn (12–15 phút): Bảng "đích ngày mai"</h3>' + ol([
   'Con vẽ một hình tròn đích. Bên trong vẽ 1 việc muốn làm được ngày mai. Ví dụ: tự xếp cặp, đọc xong 2 trang sách.',
   'Bên dưới, con vẽ 2 bước để đến đích. Ví dụ: "Bước 1: để cặp cạnh bàn. Bước 2: xếp sách theo thời khóa biểu."',
   'Dán bảng cạnh bảng buổi sáng (bài T1).',
   'Tối mai, con tự tô màu đích nếu làm được. Chưa được thì vẽ dấu hỏi và nói: "Ngày mai con đổi bước nào?"']) +
   '<h3>Con nhỏ (5 phút): Chọn tranh</h3>' + ol([
   'Giơ 2 tranh: dép và cây. "Con muốn làm việc nào?"', 'Con chỉ tranh nào thì cùng con làm việc đó ngay: cất dép lên kệ hoặc tưới cây bằng cốc nhỏ.',
   'Làm xong, cho con chỉ lại tranh: "Xong rồi!"'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Nếu không nhìn rổ, ném trúng có khó không? Làm việc khác cũng vậy không?', 'Đích ngày mai của con là gì? Bước nào khó nhất?',
   'Khi chưa tới đích, con sẽ làm gì?'])),
 sec(6,'An toàn', ul(['Chỉ ném tất cuộn tròn, không ném đồ cứng.', 'Dọn đồ dễ vỡ khỏi khu vực ném.', 'Tưới cây bằng cốc nhỏ; lau nước đổ ngay.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('5 đôi tất, 1 rổ, giấy, bút sáp. Tổng 20 phút.', [
   ('Phút 0–5 – Ném tất.', 'Hai lượt: nhắm mắt và nhìn đích. Đếm số lần trúng.'),
   ('Phút 5–10 – Con nhỏ chọn tranh.', 'Con nhỏ chọn và làm 1 việc. Con lớn giúp em.'),
   ('Phút 10–18 – Đích ngày mai.', 'Con lớn vẽ đích và 2 bước. Mẹ chỉ hỏi, không vẽ hộ.'),
   ('Phút 18–20 – Dán bảng.', 'Dán bảng ở chỗ con nhìn thấy.')], [
   ('Mục tiêu nên nhỏ:', 'việc con làm xong trong 1 ngày. Nếu con chọn việc quá lớn, hỏi: "Ngày mai làm được phần nào?"'),
   ('Tối hôm sau:', 'nhắc con tự đánh dấu. Mẹ không chấm điểm.'),
   ('Nhắn bố 1 câu:', 'đích ngày mai của con.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> con tự tô đích hoặc vẽ dấu hỏi, rồi đặt đích mới.',
   '<strong>Sau 1 tuần:</strong> đếm số đích con tô được. Hỏi: "Bước nào giúp con nhiều nhất?"'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   f'<span class="label">[Đã xác nhận]</span> Hướng dẫn hoạt động của {HARVARD} gợi ý các trò chơi giúp trẻ 5–7 tuổi luyện chú ý, ghi nhớ và lập kế hoạch.',
   '<span class="label">[Đánh giá chuyên môn]</span> Bảng "đích ngày mai" và trò ném tất do daynentang.com thiết kế, chưa có nghiên cứu riêng.']))
])

make('k3', 'Bài khoa học tuần 3: gieo hạt đậu xanh, đoán hạt cần gì để nảy mầm, bắt đầu nhật ký mầm.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 3, buổi 2', '20–25 phút + 2 phút mỗi ngày'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> dựng 2 cốc thí nghiệm (có nước và không nước), đoán kết quả, vẽ nhật ký ngày 0.',
   '<strong>Con nhỏ:</strong> tưới nước cho cốc hạt bằng thìa và chỉ vào cốc khi được hỏi "cây đâu?".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Khoảng 20 hạt đậu xanh khô (người lớn giữ túi hạt).', '2 cốc nhựa trong, bông gòn hoặc giấy ăn gấp nhiều lớp.',
   'Băng dính và bút để dán nhãn "Có nước" và "Không nước".', 'Giấy kẻ bảng nhật ký 7 ngày.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Đưa con xem một hạt đậu: "Hạt nhỏ thế này, làm sao thành cây được? Hạt cần gì?" Ghi lại các ý con nói.</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   '<strong>Quan sát:</strong> con nhìn hạt, sờ vỏ, vẽ hạt vào ô "Ngày 0".',
   '<strong>Đoán:</strong> cốc "Có nước" và cốc "Không nước", cốc nào nảy mầm? Con ghi dự đoán.',
   '<strong>Thử:</strong> lót bông vào 2 cốc. Con đếm 8 hạt cho mỗi cốc. Chỉ cốc "Có nước" được thấm ướt bông.',
   'Đặt 2 cốc cạnh nhau ở chỗ sáng, không nắng gắt. Hai cốc phải giống nhau, chỉ khác nước.',
   '<strong>Kể lại:</strong> con nói lại cách làm cho em nghe. Mỗi ngày con xem và vẽ 1 hình.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Người lớn giữ hạt; con nhỏ không cầm hạt.', 'Con dùng thìa nhỏ tưới vào cốc "Có nước" (người lớn cầm cốc).',
   'Mỗi sáng hỏi: "Cây đâu?" Con chỉ cốc. Khi mầm lên, cho con chạm nhẹ.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Vì sao hai cốc phải giống nhau, chỉ khác nước?', 'Con đoán mầm sẽ lên sau mấy ngày?',
   'Ngoài nước, hạt có thể cần gì nữa? Lần sau mình thử điều gì?'])),
 sec(6,'An toàn', ul(['<strong>Hạt đậu khô là vật nhỏ, có thể gây hóc cho trẻ dưới 3 tuổi.</strong> Người lớn giữ túi hạt; đếm hạt trước và sau buổi.',
   'Con nhỏ chỉ tưới và nhìn, không cầm hạt.', 'Không ăn hạt hay mầm trong thí nghiệm.',
   'Cốc có mốc thì bỏ đi và rửa tay. Rửa tay sau mỗi lần chạm hạt.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('16 hạt đậu xanh, 2 cốc nhựa trong, bông gòn, bút. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi: "Hạt cần gì để thành cây?" Ghi các ý con nói.'),
   ('Phút 2–5 – Dán nhãn.', 'Con lớn dán nhãn "Có nước", "Không nước".'),
   ('Phút 5–12 – Gieo hạt.', 'Con lớn đếm 8 hạt mỗi cốc. Mẹ giữ túi hạt. Con nhỏ tưới cốc "Có nước" bằng thìa.'),
   ('Phút 12–17 – Nhật ký.', 'Con lớn vẽ ngày 0 và ghi dự đoán.'),
   ('Phút 17–20 – Dọn.', 'Đếm lại hạt thừa, cất túi lên cao, rửa tay cả nhà.')], [
   ('Mỗi ngày (2 phút):', 'con lớn vẽ 1 hình; con nhỏ chỉ "cây đâu". Giữ bông cốc "Có nước" luôn ẩm.'),
   ('Nhắn bố 1 câu:', 'con đoán cốc nào sẽ nảy mầm.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> so sánh 2 cốc. Có gì khác chưa?',
   '<strong>Sau 1 tuần:</strong> con kể lại kết quả: đúng hay khác dự đoán? Bài K4 tuần sau sẽ đo mầm.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đánh giá chuyên môn]</span> Thí nghiệm "chỉ đổi một điều" (ở đây là nước) là cách đơn giản để trẻ tập so sánh công bằng.',
   '<span class="label">[Đánh giá chuyên môn]</span> Hạt khô xếp vào nhóm vật nhỏ nguy hiểm cho trẻ dưới 3 tuổi theo quy tắc an toàn của dự án; người lớn giữ hạt.',
   '<span class="label">[Đánh giá chuyên môn]</span> Thời gian nảy mầm thay đổi theo hạt và nhiệt độ; chúng tôi không ghi số ngày sẵn để con tự quan sát.']))
])

make('g3', 'Bài giá trị tuần 3: con làm việc tốt bí mật cho người trong nhà và tự cảm nhận niềm vui khi giúp người.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 3, buổi 3', '15–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> làm 1 việc tốt bí mật mỗi ngày trong 3 ngày, không cần ai khen, và kể lại cảm giác của mình.',
   '<strong>Con nhỏ:</strong> giúp mang 1 món đồ nhẹ đến cho người khác khi được nhờ.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Câu chuyện bên dưới.', '1 cuốn sổ nhỏ làm "sổ bí mật" của con lớn.', '1–2 món đồ nhẹ, to (khăn, gối nhỏ) cho con nhỏ mang.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Có ai từng làm điều tốt cho con mà con không biết là ai không?" Rồi kể chuyện.</p>'),
 sec(4,'Hoạt động chính', '<h3>Câu chuyện: Mèo Mướp và đôi dép của ông</h3>' +
   '''<blockquote class="story">
<p>Ông của Mèo Mướp đi làm vườn về, đôi dép lúc nào cũng nằm mỗi chiếc một nơi.</p>
<p>Một sáng, Mướp dậy sớm. Mướp lặng lẽ xếp đôi dép của ông ngay ngắn trước cửa, mũi dép quay ra ngoài để ông xỏ chân cho dễ.</p>
<p>Ông bước ra, ngạc nhiên: "Ai xếp dép cho ông thế nhỉ?" Mướp nấp sau cửa, cười tủm tỉm, không nói gì.</p>
<p>Ông xỏ dép, vừa đi vừa huýt sáo. Mướp thấy trong lòng ấm như có nắng sớm.</p>
<p>Từ hôm đó, sáng nào Mướp cũng có một việc bí mật. Mướp không cần ai khen. Nhìn ông vui là đủ.</p>
</blockquote><p class="small muted">Truyện viết mới cho daynentang.com.</p>''' +
   '<h3>Con lớn (10–15 phút)</h3>' + ol([
   'Hỏi: "Vì sao Mướp không nói cho ông biết? Mướp vui vì điều gì?"',
   'Cùng con nghĩ 5 việc tốt nhỏ có thể làm bí mật: xếp dép, gấp khăn, rót nước để sẵn, cất đồ chơi của em, vẽ tặng.',
   'Con chọn 3 việc cho 3 ngày tới, ghi hoặc vẽ vào sổ bí mật.',
   'Mỗi tối, con kể riêng với bố hoặc mẹ: đã làm gì, người đó phản ứng ra sao, con thấy thế nào.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Nhờ con: "Con mang khăn cho mẹ nhé." Chỉ người nhận.', 'Người nhận nói: "Cảm ơn con đã giúp!"',
   'Lặp lại 2–3 lần với người khác nhau trong nhà.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Giúp người mà không ai biết, con thấy thế nào?', 'Ai trong nhà mình hay làm việc tốt "bí mật" cho con?',
   'Ngoài nhà mình, con có thể giúp ai?'])),
 sec(6,'An toàn', ul(['Việc tốt phải an toàn: không bê nước nóng, không trèo cao, không dùng dao kéo.', 'Con nhỏ chỉ mang đồ nhẹ, mềm.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('câu chuyện, sổ nhỏ, 1 chiếc khăn. Tổng 15–20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi: "Có ai làm điều tốt cho con mà con không biết không?"'),
   ('Phút 2–6 – Kể chuyện.', 'Đọc chậm chuyện Mèo Mướp.'),
   ('Phút 6–9 – Con nhỏ giúp mang đồ.', '2–3 lượt, người nhận cảm ơn.'),
   ('Phút 9–17 – Sổ bí mật.', 'Con lớn chọn 3 việc cho 3 ngày, ghi vào sổ.'),
   ('Phút 17–20 – Hẹn giờ kể.', 'Hẹn mỗi tối con kể riêng với mẹ.')], [
   ('Quan trọng:', 'không thưởng quà hay kẹo cho việc tốt. Chỉ cảm ơn và hỏi con thấy thế nào (xem nguồn).'),
   ('Nếu mẹ phát hiện việc tốt bí mật:', 'giả vờ không biết, chỉ nói to "Ai giúp mẹ thế nhỉ, mẹ vui quá!"'),
   ('Nhắn bố 1 câu:', 'việc tốt bí mật đầu tiên của con.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> tối hỏi riêng con lớn: "Hôm nay việc bí mật là gì?"',
   '<strong>Sau 1 tuần:</strong> con chọn 1 việc tốt cho người ngoài gia đình, ví dụ cảm ơn cô lao công, tặng tranh cho hàng xóm.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đã xác nhận]</span> Trẻ 20 tháng tuổi được thưởng vật chất khi giúp đỡ thì sau đó giúp ít hơn; trẻ được khen bằng lời hoặc không thưởng vẫn tiếp tục giúp (Warneken &amp; Tomasello 2008, <em>Developmental Psychology</em> 44(6): 1785–1788, <a href="https://scholars.duke.edu/publication/1458228">nguồn</a>).',
   '<span class="label">[Suy luận]</span> Vì vậy bài này không dùng quà thưởng cho việc tốt; nghiên cứu làm với trẻ rất nhỏ trong phòng thí nghiệm.',
   '<span class="label">[Đánh giá chuyên môn]</span> Truyện "Mèo Mướp" viết mới hoàn toàn cho dự án.']))
])

# =================== TUẦN 4 ===================
make('t4', 'Bài thói quen tuần 4: lập kế hoạch Trước – Trong – Sau cho giờ chơi; con nhỏ tập "đầu tiên… rồi…".',
 ['Mạch A – Thói quen (Ngón trỏ)', 'Tuần 4, buổi 1', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> vẽ kế hoạch chơi 3 bước trước khi chơi, xem lại giữa chừng, và sau khi chơi kể lại so với kế hoạch.',
   '<strong>Con nhỏ:</strong> làm đúng 2 việc theo thứ tự khi nghe "Đầu tiên…, rồi…".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Giấy chia 3 cột: Trước · Trong · Sau. Bút sáp.', 'Đồ chơi con lớn hay chơi (Lego, đồ hàng, đất nặn).', '2 tranh nhỏ cho con nhỏ: rửa tay và ăn bánh.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Trước khi xây nhà, người ta vẽ bản vẽ. Hôm nay con làm kiến trúc sư cho giờ chơi của mình."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (20 phút)</h3>' + ol([
   '<strong>Trước</strong> (5 phút): con vẽ kế hoạch: chơi gì, dùng đồ gì, chơi với ai, làm 3 bước nào.',
   '<strong>Trong</strong> (10 phút): con chơi theo kế hoạch. Giữa chừng, bố mẹ hỏi một lần: "Con đang ở bước mấy?"',
   '<strong>Sau</strong> (5 phút): con so sánh với kế hoạch. Giống ở đâu? Đổi ở đâu? Vì sao đổi?',
   'Đổi kế hoạch giữa chừng là được, miễn con nói được vì sao.']) +
   '<h3>Con nhỏ (5 phút): Đầu tiên… rồi…</h3>' + ol([
   'Giơ 2 tranh theo thứ tự: "Đầu tiên rửa tay, rồi ăn bánh."', 'Cùng con làm đúng thứ tự. Xong mỗi việc, chỉ vào tranh.',
   'Thử thêm 1 cặp khác trong ngày: "Đầu tiên cất xe, rồi đi tắm."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Có kế hoạch rồi mới chơi, khác gì so với chơi ngay?', 'Chỗ nào con đổi kế hoạch? Vì sao?',
   'Việc gì trong ngày cũng cần kế hoạch Trước – Trong – Sau?'])),
 sec(6,'An toàn', ul([SMALL + ' Lego nhỏ chỉ dùng khi con nhỏ không ở cạnh; với con nhỏ dùng Duplo.', 'Đất nặn cất ngay sau khi chơi.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('giấy 3 cột, bút sáp, đồ chơi của con, 2 tranh. Tổng 25 phút.', [
   ('Phút 0–2 – Mở đầu.', '"Hôm nay con làm kiến trúc sư cho giờ chơi."'),
   ('Phút 2–5 – Con nhỏ.', '"Đầu tiên rửa tay, rồi ăn bánh." Làm cùng con.'),
   ('Phút 5–10 – Trước.', 'Con lớn vẽ kế hoạch 3 bước.'),
   ('Phút 10–20 – Trong.', 'Con chơi. Mẹ hỏi một lần "Con đang ở bước mấy?" Con nhỏ chơi cạnh.'),
   ('Phút 20–25 – Sau.', 'Con so sánh với kế hoạch và kể lại.')], [
   ('Đừng chấm đúng sai:', 'kế hoạch là để con tập nghĩ trước, không phải để bắt con làm y hệt.'),
   ('Nhắn bố 1 câu:', 'con lên kế hoạch chơi gì.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> trước giờ chơi, hỏi: "Kế hoạch hôm nay là gì?" Con nói miệng là đủ.',
   '<strong>Sau 1 tuần:</strong> dùng Trước – Trong – Sau cho một việc thật, ví dụ dọn góc học tập.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đã xác nhận]</span> Ý tưởng "kế hoạch chơi" có trong một số chương trình mầm non ở Mỹ. Kết quả thử nghiệm ngẫu nhiên của các chương trình này không đồng nhất; chúng tôi chỉ mượn ý tưởng.',
   f'<span class="label">[Đã xác nhận]</span> {HARVARD} gợi ý trẻ 5–7 tuổi tập lập kế hoạch qua trò chơi.',
   '<span class="label">[Đánh giá chuyên môn]</span> Bảng Trước – Trong – Sau do daynentang.com thiết kế.']))
])

make('k4', 'Bài khoa học tuần 4: đo mầm đậu bằng que, khối Lego hoặc thước; vẽ biểu đồ cột đầu tiên.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 4, buổi 2', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> đo chiều cao mầm bằng một đơn vị (khối Lego hoặc thước), ghi số, và vẽ biểu đồ cột cho 2 cốc.',
   '<strong>Con nhỏ:</strong> chỉ vào mầm "cao" và mầm "thấp", cùng bố mẹ đếm lá.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['2 cốc mầm từ bài K3 (nếu cốc "Không nước" chưa nảy mầm, đó cũng là kết quả).',
   'Que kem, giấy màu cắt dải, hoặc khối Duplo; thước kẻ cho con lớn.', 'Giấy kẻ ô để vẽ biểu đồ cột.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Hôm trước con đoán cốc nào sẽ nảy mầm. Giờ mình xem kết quả và đo xem mầm cao bao nhiêu."</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   '<strong>Quan sát:</strong> so 2 cốc. Kết quả đúng hay khác dự đoán tuần trước?',
   '<strong>Đoán:</strong> mầm cao nhất bằng mấy khối Duplo?',
   '<strong>Đo:</strong> dựng dải giấy cạnh mầm, đánh dấu ngọn, rồi đếm khối hoặc đọc thước. Đo 3 mầm, ghi số.',
   '<strong>Vẽ biểu đồ:</strong> mỗi mầm một cột, cao bằng số đo. Cốc "Không nước" ghi số 0 nếu chưa có mầm.',
   '<strong>Kể lại:</strong> "Cốc có nước… Cốc không nước… Vậy hạt cần…"']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Bế con nhìn 2 cốc. Hỏi: "Cây cao đâu? Cây thấp đâu?"', 'Cùng con đếm lá: "Một, hai…"', 'Con tưới nhẹ bằng thìa.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Đo bằng khối và đo bằng thước, cách nào dễ hơn? Cách nào chính xác hơn?', 'Vì sao các mầm trong cùng một cốc cao khác nhau?',
   'Mình nên làm gì tiếp với các mầm này?'])),
 sec(6,'An toàn', ul(['Hạt chưa nảy mầm vẫn là vật nhỏ: người lớn bỏ đi, không để con nhỏ cầm.', 'Không ăn mầm thí nghiệm. Cốc có mốc thì bỏ, rửa tay.', 'Que kem, dải giấy để xa miệng con nhỏ.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('2 cốc mầm, dải giấy hoặc khối Duplo, giấy kẻ ô. Tổng 20 phút.', [
   ('Phút 0–3 – So sánh.', 'Con lớn nói kết quả 2 cốc so với dự đoán.'),
   ('Phút 3–6 – Con nhỏ.', 'Chỉ cây cao, cây thấp, đếm lá.'),
   ('Phút 6–14 – Đo.', 'Con lớn đo 3 mầm, ghi số.'),
   ('Phút 14–20 – Biểu đồ.', 'Con lớn tô cột, rồi kể lại kết luận.')], [
   ('Nếu cả hai cốc đều chưa nảy mầm:', 'đó vẫn là kết quả. Hỏi con: "Có thể vì sao?" rồi gieo lại.'),
   ('Nhắn bố 1 câu:', 'mầm cao nhất được mấy khối.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> đo lại 1 mầm, thêm số mới vào biểu đồ.',
   '<strong>Sau 1 tuần:</strong> con kể cho ông bà nghe thí nghiệm từ đầu đến cuối. Chuyển mầm ra chậu đất nếu muốn.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đánh giá chuyên môn]</span> Đo bằng đơn vị tự chọn (khối, que) trước rồi mới dùng thước là trình tự thường dùng khi dạy đo lường cho trẻ nhỏ.',
   '<span class="label">[Đánh giá chuyên môn]</span> Bài này do daynentang.com thiết kế; kết quả phụ thuộc vào hạt và điều kiện nhà bạn.']))
])

make('g4', 'Bài giá trị tuần 4: gọi tên cảm xúc và tập Dừng – Thở – Nói khi giận hoặc buồn.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 4, buổi 3', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> gọi tên 4 cảm xúc (vui, buồn, giận, sợ) và nói câu "Con thấy… vì…" trong 2 tình huống đóng vai.',
   '<strong>Con nhỏ:</strong> chỉ đúng gương mặt "vui" và "buồn" khi được hỏi.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['4 tấm giấy vẽ 4 gương mặt: vui, buồn, giận, sợ (vẽ to, đơn giản).', '1 chiếc gương nhỏ không vỡ (gương nhựa hoặc gương trên tủ).'])),
 sec(3,'Mở đầu (2 phút)', '<p>Bố mẹ làm mặt giận rồi hỏi: "Bố đang thấy thế nào? Con nhìn chỗ nào mà biết?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Cả nhà (5 phút): Đoán mặt</h3>' + ol([
   'Mỗi người lần lượt làm một gương mặt; người khác đoán và chỉ đúng tấm tranh.',
   'Con lớn soi gương làm 4 gương mặt. Con nhỏ bắt chước mặt vui, mặt buồn.']) +
   '<h3>Con lớn (12–15 phút): Dừng – Thở – Nói</h3>' + ol([
   'Ôn 3 bước từ bài G1: <strong>Dừng</strong> (đứng yên, tay để xuống), <strong>Thở</strong> (thở bong bóng 1 hơi), <strong>Nói</strong> ("Con thấy… vì…").',
   'Đóng vai 1: "Em làm đổ tháp Lego của con." Con làm 3 bước, ví dụ: "Con thấy giận vì con xây lâu lắm."',
   'Đóng vai 2: "Bạn không cho con chơi cùng." Ví dụ: "Con thấy buồn vì con muốn chơi."',
   'Đổi vai: bố mẹ làm 3 bước, con nghe và nói lại: "Bố thấy… vì…"',
   'Hỏi tiếp: "Nói ra rồi, mình có thể làm gì?" Cùng nghĩ 1 cách.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Giơ 2 tranh vui, buồn: "Mặt vui đâu?" Con chỉ.',
   'Khi con buồn thật trong ngày, gọi tên giúp con: "Con buồn vì hết bánh. Bố ôm con nhé."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Cơ thể con thế nào khi giận? (nóng mặt, nắm tay…)', 'Thở một hơi trước khi nói có khác gì không?',
   'Khi thấy người khác buồn, mình có thể làm gì?'])),
 sec(6,'An toàn', ul(['Dùng gương không vỡ.', 'Nếu con kể một chuyện thật làm con sợ hoặc bị đau, hãy dừng trò chơi, nghe con. Khi cần, gọi 111 (bảo vệ trẻ em).',
   'Không chọc con giận thật để luyện tập; chỉ đóng vai.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('4 tranh gương mặt, 1 gương nhựa. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Mẹ làm mặt buồn: "Mẹ đang thấy thế nào?"'),
   ('Phút 2–7 – Đoán mặt.', 'Cả nhà đoán mặt, con nhỏ chỉ tranh vui, buồn.'),
   ('Phút 7–17 – Dừng – Thở – Nói.', 'Con lớn đóng vai 2 tình huống. Mẹ đổi vai 1 lần.'),
   ('Phút 17–20 – Kết thúc.', 'Mỗi người nói "Hôm nay mình thấy… vì…"')], [
   ('Khi con giận thật trong tuần:', 'mẹ nói giúp con trước: "Con đang giận vì…" rồi mới hỏi chuyện. Chưa cần dạy bảo ngay lúc đó.'),
   ('Mẹ làm mẫu:', 'khi mẹ mệt, nói to "Mẹ thấy mệt vì… Mẹ thở một hơi đã." Con học nhiều nhất từ cách bố mẹ làm.'),
   ('Nhắn bố 1 câu:', 'cảm xúc con gọi tên được hôm nay.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> trong bữa tối, mỗi người nói 1 câu "Hôm nay mình thấy… vì…"',
   '<strong>Sau 1 tuần:</strong> đếm số lần con tự dùng Dừng – Thở – Nói. Chấm lại bảng quan sát ở tuần 6.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   '<span class="label">[Đã xác nhận]</span> Phân tích gộp 24 nghiên cứu: việc bố mẹ làm mẫu, đáp lại và chỉ dạy về cảm xúc gắn với kỹ năng cảm xúc tốt hơn ở trẻ mầm non; mức liên hệ nhỏ (r khoảng 0,05–0,19) và phần lớn là nghiên cứu tương quan (Zinsser, Gordon &amp; Jiang 2021, <em>Early Childhood Research Quarterly</em>).',
   '<span class="label">[Suy luận]</span> Vì vậy bài nhấn mạnh việc bố mẹ gọi tên cảm xúc và làm mẫu hằng ngày, không chỉ trong buổi học.',
   '<span class="label">[Đánh giá chuyên môn]</span> Ba bước Dừng – Thở – Nói là khung của daynentang.com.']))
])
print('weeks 2-4 built')
