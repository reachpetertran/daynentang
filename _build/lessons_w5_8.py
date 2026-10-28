import illus2  # noqa: F401  (tạo hình tuần 5–8 trước khi dựng trang)
from lessons import lesson, sec, JOURNAL

U = '/khoa-hoc/gia-dinh-2-8/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
HARVARD = '<a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Harvard Center on the Developing Child</a>'
WATER = '<a href="https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/">CPSC, Hoa Kỳ</a>'
SMALL = 'Mọi vật trong tầm với của con nhỏ phải to hơn lõi giấy vệ sinh.'

L = {
 't5': (5, 't5-viec-quan-trong-lam-truoc', 'T5', 'Việc quan trọng làm trước'),
 'k5': (5, 'k5-anh-sang-va-bong', 'K5', 'Ánh sáng và bóng'),
 'g5': (5, 'g5-viec-nha-cua-con', 'G5', 'Việc nhà của con'),
 't6': (6, 't6-den-do-den-xanh', 'T6', 'Đèn đỏ – Đèn xanh'),
 'k6': (6, 'k6-doc-va-luc', 'K6', 'Dốc và lực'),
 'g6': (6, 'g6-nhan-loi-va-sua-loi', 'G6', 'Nhận lỗi và sửa lỗi'),
 't7': (7, 't7-gay-noi-chuyen', 'T7', 'Gậy nói chuyện'),
 'k7': (7, 'k7-tui-bi-an', 'K7', 'Túi bí ẩn'),
 'g7': (7, 'g7-tham-tu-cam-xuc', 'G7', 'Thám tử cảm xúc'),
 't8': (8, 't8-anh-huong-dan-em', 'T8', 'Anh hướng dẫn em'),
 'k8': (8, 'k8-thoi-tiet', 'K8', 'Thời tiết quanh nhà'),
 'g8': (8, 'g8-cam-on-nguoi-lao-dong', 'G8', 'Cảm ơn người lao động'),
}
ORDER = ['t5','k5','g5','t6','k6','g6','t7','k7','g7','t8','k8','g8']
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
def make(k, desc, meta, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U + 'tuan-4/g4-dung-tho-noi/', 'G4 – Dừng – Thở – Nói')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U + 'tuan-9/t9-cham-cay-cua-minh/', 'T9 – Chăm cây của mình')
    lesson(slug, code, title, '', desc, meta, sections, prev=prev, nxt=nxt, week=w, draft=True)
def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>Mẹ chỉ cần: {need}</em></p><ol>{li}</ol>{nt}</div>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'

# =================== TUẦN 5 ===================
make('t5', 'Bài thói quen tuần 5: việc quan trọng làm trước. Trò "đá to vào trước" và bảng thứ tự trong ngày.',
 ['Mạch A – Thói quen (Ngón giữa)', 'Tuần 5, buổi 1', '20–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> sắp 3 việc trong ngày theo thứ tự "việc chính – việc nhà – chơi" và làm việc chính trước ít nhất 4/7 ngày.',
   '<strong>Con nhỏ:</strong> làm 1 việc nhỏ khi nghe "Đầu tiên…, rồi…" (ví dụ cất xe rồi mới đi tắm).'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 hộp nhựa trong hoặc giỏ nhỏ.', '4–5 khối Duplo to (là "đá to"), 1 nắm giấy vụn vo viên (là "sỏi").',
   'Giấy, bút sáp. 2 tranh nhỏ cho con nhỏ: cái cặp và chiếc xe.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Giơ ngón giữa, ngón cao nhất: "Ngón này nhắc mình: việc quan trọng làm trước." Hỏi con: "Sáng nay việc gì quan trọng nhất?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15–20 phút): Đá to vào trước</h3>' + ol([
   '<strong>Lần 1:</strong> con đổ giấy vụn ("sỏi") vào hộp trước, rồi xếp khối to ("đá to"). Khối to có vừa không?',
   '<strong>Lần 2:</strong> làm lại, xếp khối to trước, rồi rắc giấy vụn vào khe. Lần này thế nào?',
   'Bố mẹ nói: "Khối to giống việc quan trọng: bài, xếp cặp. Giấy vụn giống việc vui: xem tranh, chơi."',
   'Con vẽ bảng thứ tự ngày mai: <em>1. Việc chính · 2. Việc nhà · 3. Chơi</em>. Dán cạnh bảng buổi sáng.']) +
   '<h3>Con nhỏ (5 phút): Đầu tiên… rồi…</h3>' + ol(['Giơ 2 tranh: "Đầu tiên cất cặp, rồi chơi xe."',
   'Cùng con làm việc thứ nhất. Xong, đưa ngay chiếc xe: "Giờ chơi nào!"', 'Lặp lại trong ngày với 1–2 cặp việc khác.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Vì sao lần 2 khối to lại vừa hộp?', 'Việc nào của con là "khối to" mỗi ngày?', 'Nếu con chơi trước rồi mới làm bài thì điều gì có thể xảy ra?'])),
 sec(6,'An toàn', ul(['Giấy vụn chỉ dùng cho con lớn; cất ngay sau buổi.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('hộp nhựa, 4 khối to, giấy vụn, giấy bút. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Giơ ngón giữa: "Việc quan trọng làm trước."'),
   ('Phút 2–10 – Đá to vào trước.', 'Con lớn làm 2 lần: giấy trước, rồi khối trước.'),
   ('Phút 10–13 – Con nhỏ.', '"Đầu tiên cất cặp, rồi chơi xe." Làm cùng con.'),
   ('Phút 13–20 – Bảng thứ tự.', 'Con lớn vẽ 3 việc của ngày mai theo thứ tự.')], [
   ('Giữ lời:', 'đã nói "rồi chơi" thì cho con chơi thật. Lời hứa giữ đúng giúp con tin vào thứ tự.'),
   ('Nhắn bố 1 câu:', '"khối to" của con ngày mai là gì.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> chiều hôm sau hỏi: "Hôm nay khối to là gì? Con làm trước chưa?"',
   '<strong>Sau 1 tuần:</strong> đếm số ngày con làm việc chính trước. Mục tiêu: 4/7 ngày.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Trò "đá to vào trước" là một ẩn dụ phổ biến về sắp xếp ưu tiên; daynentang.com chỉ mượn ý tưởng và tự thiết kế hoạt động.'),
   lb('Cần kiểm chứng', 'Cách "đầu tiên… rồi…" dựa trên nguyên tắc Premack trong phân tích hành vi (việc ít thích làm trước, việc thích làm sau). Mức bằng chứng khi bố mẹ tự dùng ở nhà, chúng tôi chưa kiểm tra được.'),
   lb('Đã xác nhận', f'{HARVARD} gợi ý trẻ 5–7 tuổi tập lập kế hoạch và tự kiểm soát qua trò chơi.')]))
])

make('k5', 'Bài khoa học tuần 5: ánh sáng và bóng. Con dịch đèn gần xa, quan sát bóng to nhỏ, và xem bóng ngoài trời thay đổi trong ngày.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 5, buổi 2', '25–30 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> đoán rồi thử: đèn gần vật thì bóng to hay nhỏ; ghi kết quả 3 khoảng cách.',
   '<strong>Con nhỏ:</strong> chỉ vào bóng trên tường và làm bóng to lên khi tiến lại gần đèn.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 đèn pin loại pin to, nắp pin vặn vít chặt.', '1 bức tường trắng hoặc tờ giấy A3 dán tường. Phòng hơi tối.',
   '1–2 đồ chơi to (khủng long nhựa, khối gỗ).', 'Dải giấy và bút để đánh dấu chiều cao bóng.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Tắt đèn phòng, bật đèn pin chiếu lên tay mình: "Cái gì đen đen trên tường thế? Vì sao lại có nó?"</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (20 phút)</h3>' + ol([
   '<strong>Quan sát:</strong> đặt khủng long cách tường một gang tay. Bật đèn, nhìn bóng.',
   '<strong>Đoán:</strong> đưa đèn lại gần khủng long thì bóng to lên hay nhỏ đi?',
   '<strong>Thử:</strong> để đèn ở 3 chỗ: xa, vừa, gần. Mỗi lần con đánh dấu đỉnh bóng trên giấy.',
   '<strong>Kể lại:</strong> con nói câu: "Đèn càng gần, bóng càng…"',
   '<strong>Ra ngoài</strong> (nếu có nắng): đứng cùng chỗ lúc sáng và lúc chiều, xem bóng dài hay ngắn. Ghi lại cho bài ôn.']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Chiếu đèn lên tường. Cho con giơ tay: "Bóng của con đâu?"',
   'Con tiến lại gần đèn: "Bóng to quá!" Lùi ra: "Bóng nhỏ rồi!"', 'Chơi rối bóng với đồ chơi to.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Vì sao có bóng?', 'Muốn bóng khủng long to như con khủng long thật thì làm sao?', 'Buổi trưa bóng của con ngắn hay dài?'])),
 sec(6,'An toàn', ul(['Không chiếu đèn pin vào mắt ai. Không nhìn thẳng vào mặt trời.', 'Đèn pin phải có nắp pin vặn vít; không dùng đèn dùng pin cúc áo.',
   'Phòng tối: dọn đồ trên sàn để không vấp ngã.', 'Ra ngoài buổi trưa nắng gắt: đội mũ, ở ngoài ngắn.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('đèn pin, 1 khủng long nhựa, tờ giấy dán tường, bút. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Chiếu đèn lên tay, hỏi: "Vì sao có bóng?"'),
   ('Phút 2–6 – Con nhỏ.', 'Con nhỏ tiến lùi để bóng to nhỏ.'),
   ('Phút 6–16 – Thử 3 khoảng cách.', 'Con lớn đoán, đổi chỗ đèn, đánh dấu bóng.'),
   ('Phút 16–20 – Kể lại.', 'Con lớn nói câu kết luận; con nhỏ chỉ bóng to, bóng nhỏ.')], [
   ('Nếu phòng không tối được:', 'kéo rèm, chơi gần tường khuất sáng; bóng vẫn rõ.'),
   ('Nhắn bố 1 câu:', 'câu kết luận của con.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> ngoài trời buổi sáng, cho con nhìn bóng mình và đo bằng bước chân.',
   '<strong>Sau 1 tuần:</strong> đo lại bóng vào buổi trưa. So với buổi sáng thì sao?'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Ý chính của bài thuộc nội dung khoa học lớp mẫu giáo – lớp 2 trong NGSS (K–2 PS4.B; K–2 ESS1): đèn càng gần vật, bóng càng to; mặt trời thấp thì bóng dài (<a href="https://www.nsta.org/sites/default/files/journal-articles/supplemental-resources/3-27-2020%20-%20Lesson%20Plan%20-%20%20Daily%20Do%20-%20Why%20Is%20My%20Shadow%20Always%20Changing.pdf">NSTA</a>).'),
   lb('Đánh giá chuyên môn', 'Hoạt động đánh dấu bóng và rối bóng do daynentang.com thiết kế.')]))
])

make('g5', 'Bài giá trị tuần 5: trách nhiệm qua việc nhà vừa sức. Con chọn việc nhà của mình và tự đánh dấu mỗi ngày.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 5, buổi 3', '20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> chọn 1 việc nhà của riêng mình, làm và tự đánh dấu ít nhất 5/7 ngày.',
   '<strong>Con nhỏ:</strong> làm 1 việc nhỏ cùng người lớn mỗi ngày (cất dép, bỏ đồ bẩn vào giỏ).'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Bảng việc nhà theo tuổi (xem hình), giấy, bút sáp.', '1 bình tưới nhỏ hoặc cốc nhựa, 1 chậu cây.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Trong nhà mình, ai làm việc gì? Bố nấu…, mẹ…, còn con thì sao?" Cùng kể. Rồi nói: "Nhà là của cả nhà, nên ai cũng có một việc."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15 phút)</h3>' + ol([
   'Xem bảng việc nhà theo tuổi. Con chọn 1 việc làm cả tuần, ví dụ tưới cây hoặc dọn bàn sau bữa tối.',
   'Bố mẹ làm mẫu một lần, nói rõ thế nào là "xong": "Tưới cây xong là đất ẩm, không đổ nước ra sàn."',
   'Con làm thử ngay. Con tự kiểm tra theo tiêu chí "xong", rồi đánh dấu ✓ vào bảng tuần.',
   'Đi hết "vòng trách nhiệm": nhận việc → làm → tự kiểm tra → đánh dấu.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Cầm tay con cất đôi dép lên kệ: "Dép về nhà."', 'Cho con bỏ 1 chiếc áo vào giỏ đồ bẩn.', 'Cảm ơn con: "Con giúp nhà mình đấy."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Nếu không ai tưới cây thì cây sẽ thế nào?', 'Khi con làm xong việc của mình, con thấy thế nào?', 'Hôm nào con quên thì mình làm gì?'])),
 sec(6,'An toàn', ul(['Không giao việc liên quan đến bếp nóng, dao, hóa chất tẩy rửa, ổ điện.', 'Con nhỏ chỉ làm việc nhẹ, có người lớn bên cạnh.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('bảng việc nhà, giấy bút, bình tưới nhỏ. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Kể việc của từng người trong nhà.'),
   ('Phút 2–8 – Chọn việc.', 'Con lớn chọn việc của tuần. Mẹ nói rõ thế nào là "xong".'),
   ('Phút 8–14 – Làm thử.', 'Con lớn làm, tự kiểm tra, đánh dấu ✓.'),
   ('Phút 14–20 – Con nhỏ.', 'Cất dép, bỏ áo vào giỏ cùng mẹ.')], [
   ('Không thưởng tiền hay quà cho việc nhà hằng ngày:', 'cảm ơn và để con tự đánh dấu là đủ. Việc nhà là phần của mỗi thành viên.'),
   ('Khi con làm chưa khéo:', 'không làm lại trước mặt con. Chỉ cho con 1 điều để lần sau làm tốt hơn.'),
   ('Nhắn bố 1 câu:', 'việc nhà con chọn.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi tối:</strong> con tự đánh dấu ✓ nếu đã làm.', '<strong>Sau 1 tuần:</strong> đếm số ✓. Con muốn giữ việc này hay đổi việc mới?'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Khảo sát 207 phụ huynh trẻ 5–13 tuổi: trẻ làm việc tự phục vụ và việc nhà có trí nhớ làm việc và khả năng tự kiềm chế tốt hơn. Đây là tương quan, không phải nhân quả (Tepper, Howell &amp; Bennett 2022, qua <a href="https://chadd.org/wp-content/uploads/2022/09/ATTN_10_2022_Doing_Household_Chores.pdf">CHADD</a>).'),
   lb('Suy luận', 'Không thưởng vật chất cho việc nhà hằng ngày là cách áp dụng phát hiện về thưởng làm giảm động lực giúp đỡ ở trẻ nhỏ (Warneken &amp; Tomasello 2008).'),
   lb('Đánh giá chuyên môn', 'Bảng việc nhà theo tuổi là gợi ý của daynentang.com; hãy điều chỉnh theo sức của con.')]))
])

# =================== TUẦN 6 ===================
make('t6', 'Bài thói quen tuần 6: chờ lượt và tự dừng qua trò Đèn đỏ – Đèn xanh. Cuối tuần chấm bảng quan sát giữa khóa.',
 ['Mạch A – Thói quen (Ngón giữa)', 'Tuần 6, buổi 1', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> dừng đúng tín hiệu ít nhất 8/10 lần, và chờ lượt trong một trò chơi bàn cờ.',
   '<strong>Con nhỏ:</strong> dừng khi nghe tín hiệu "Đèn đỏ!" ít nhất 5/10 lần.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['3 tờ giấy tô màu đỏ, vàng, xanh (hoặc 3 chiếc dép khác màu).', 'Một khoảng sàn trống. 1 trò chơi đơn giản cần chờ lượt (cờ cá ngựa, xếp hình theo lượt).'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Ngoài đường, đèn đỏ thì xe làm gì? Vì sao phải dừng?" Hôm nay cơ thể con sẽ làm đèn giao thông.</p>'),
 sec(4,'Hoạt động chính', '<h3>Cả nhà (10 phút): Đèn đỏ – Đèn xanh</h3>' + ol([
   'Người dẫn trò giơ màu: <strong>xanh</strong> = đi (hoặc nhảy), <strong>vàng</strong> = đi chậm, <strong>đỏ</strong> = đứng im như tượng.',
   'Chơi 3 phút. Rồi đổi luật ngược cho con lớn: xanh = đứng im, đỏ = đi. Khó hơn vì phải "tắt" thói quen.',
   'Con lớn làm người dẫn trò một lượt.']) +
   '<h3>Con lớn (8 phút): Chờ lượt</h3>' + ol(['Chơi một ván cờ ngắn hoặc trò xếp hình theo lượt.',
   'Khi chờ, con nói khẽ: "Mình chờ và xem bạn làm."', 'Hết ván, hỏi: "Lúc chờ, con làm gì để không giành lượt?"']) +
   '<h3>Con nhỏ</h3><p>Chơi Đèn đỏ – Đèn xanh cùng cả nhà với 2 màu: xanh đi, đỏ dừng. Khen ngay khi con dừng: "Con dừng giỏi quá!"</p>'),
 sec(5,'Câu hỏi trò chuyện', ol(['Lúc đổi luật ngược, khó ở chỗ nào?', 'Trong ngày, lúc nào con cần "đèn đỏ" cho mình? (khi giận, khi muốn giành đồ)', 'Chờ lượt có lợi gì cho cả nhà?'])),
 sec(6,'An toàn', ul(['Chơi trên sàn không trơn; dọn đồ chơi nhỏ và góc nhọn.', 'Khi "đứng im", không bắt con giữ tư thế khó lâu.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('3 tờ giấy màu, 1 trò chơi theo lượt. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi về đèn giao thông.'),
   ('Phút 2–10 – Đèn đỏ – Đèn xanh.', 'Cả hai con chơi; con lớn thử luật ngược.'),
   ('Phút 10–18 – Chờ lượt.', 'Con lớn và mẹ chơi một ván cờ. Con nhỏ chơi xếp khối cạnh đó.'),
   ('Phút 18–20 – Kết thúc.', 'Hỏi con lớn: "Lúc chờ con làm gì?"')], [
   ('Giữa khóa:', 'cuối tuần này, mẹ hoặc bố chấm lại <a href="/cong-cu/bang-quan-sat/">bảng quan sát 0–1–2</a> (cột tuần 6).'),
   ('Nhắn bố 1 câu:', 'con dừng đúng mấy lần trên 10.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> khi con sắp giành đồ, nói khẽ "Đèn đỏ" và chờ con dừng.',
   '<strong>Cuối tuần 6:</strong> chấm bảng quan sát giữa khóa. So với tuần 0, mục nào đã tiến bộ? Mục nào cần giữ lâu hơn?'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Hướng dẫn hoạt động của {HARVARD} cho trẻ 5–7 tuổi gợi ý các trò vận động cần chú ý và kiềm chế, như trò dừng theo nhạc và trò làm theo lệnh.'),
   lb('Đánh giá chuyên môn', 'Phiên bản "luật ngược" do daynentang.com thêm vào để tăng độ khó cho con lớn.')]))
])

make('k6', 'Bài khoa học tuần 6: dốc và lực. Con thả xe trên dốc thấp và dốc cao, đo quãng đường và tập thí nghiệm công bằng.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 6, buổi 2', '25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> chỉ đổi độ cao dốc, đo quãng đường xe đi bằng bước chân, và nói được "chỉ đổi một điều".',
   '<strong>Con nhỏ:</strong> thả xe từ đỉnh dốc và chỉ xe "đi xa" hay "đi gần".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 tấm bìa cứng dài hoặc tấm gỗ mỏng.', '3–4 cuốn sách dày để kê dốc.', '1 xe đồ chơi to. Băng dính giấy để đánh dấu vạch thả và chỗ xe dừng.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Đi xe đạp xuống dốc thì xe nhanh hay chậm? Dốc cao thì sao?" Ghi lại câu trả lời của con.</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (20 phút)</h3>' + ol([
   'Kê bìa lên 1 cuốn sách. Dán vạch thả ở đầu dốc. Luôn thả xe ở cùng vạch, không đẩy.',
   '<strong>Đoán:</strong> kê 3 cuốn sách thì xe đi xa hơn hay gần hơn?',
   '<strong>Thử:</strong> thả xe ở dốc 1 cuốn, rồi 2 cuốn, rồi 3 cuốn. Mỗi lần đo chỗ xe dừng bằng bước chân, ghi số.',
   '<strong>Công bằng:</strong> hỏi: "Mình đổi điều gì? Điều gì giữ nguyên?" Cùng chỉ vào sơ đồ thí nghiệm công bằng.',
   '<strong>Kể lại:</strong> "Dốc càng cao thì xe…"']) +
   '<h3>Con nhỏ (5–10 phút)</h3>' + ol(['Cho con thả xe từ đỉnh dốc nhiều lần.', 'Nói theo: "Xe đi xa quá!" hoặc "Xe dừng gần."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Nếu vừa đổi dốc vừa đổi xe, mình có biết vì sao xe đi xa không?', 'Ở đâu ngoài đời có dốc? (cầu thang, đường lên cầu, cầu trượt)', 'Con muốn thử đổi điều gì lần sau? (mặt sàn, loại xe)'])),
 sec(6,'An toàn', ul(['Chồng sách thấp, đặt trên sàn, không đặt trên bàn cao.', 'Xe đồ chơi to, không có chi tiết nhỏ rời ra.', 'Không trèo lên tấm bìa hay chồng sách.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('tấm bìa cứng, 3 cuốn sách, 1 xe đồ chơi, băng dính. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi về đi xe xuống dốc.'),
   ('Phút 2–5 – Con nhỏ.', 'Con nhỏ thả xe vài lần.'),
   ('Phút 5–17 – Thử 3 độ cao.', 'Con lớn thả, đo bằng bước chân, ghi số.'),
   ('Phút 17–20 – Kể lại.', 'Con lớn nói kết luận và điều giữ nguyên.')], [
   ('Nếu kết quả không đều:', 'thả lại 2 lần mỗi độ cao. Kết quả lộn xộn cũng là bài học: đo nhiều lần cho chắc.'),
   ('Nhắn bố 1 câu:', 'số bước chân ở dốc cao nhất.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> ở cầu trượt sân chơi, hỏi: "Cầu trượt cao hay thấp thì trượt nhanh hơn?"',
   '<strong>Sau 1 tuần:</strong> con tự đổi một điều khác (thảm và sàn gạch) và giữ nguyên dốc.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', '"Chỉ đổi một điều" (thí nghiệm công bằng) là nền của cách làm khoa học; bài này giúp con làm quen bằng đồ trong nhà.'),
   lb('Đánh giá chuyên môn', 'Quãng đường xe đi phụ thuộc xe, mặt sàn và cách thả; chúng tôi không ghi số sẵn để con tự đo.')]))
])

make('g6', 'Bài giá trị tuần 6: nhận lỗi và sửa lỗi qua năm bước. Bố mẹ chê việc làm, không gắn nhãn con.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 6, buổi 3', '20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> làm đủ 5 bước "dừng – thở – nói thật – xin lỗi – cùng sửa" trong 2 tình huống đóng vai.',
   '<strong>Con nhỏ:</strong> cùng bố mẹ lau chỗ nước đổ sau khi nghe "Đổ rồi, mình lau nhé".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Sơ đồ 5 bước (in hoặc vẽ lại).', '1 cốc nhựa, chút nước, 1 khăn lau.', 'Ôn lại chuyện Khủng long Tí ở bài G1.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Nhớ chuyện Tí làm vỡ chậu cây không? Sau khi nói thật, Tí làm gì tiếp?" (Tí cùng bà trồng lại cây.)</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15 phút)</h3>' + ol([
   'Đọc sơ đồ 5 bước cùng con, mỗi bước làm một động tác: giơ tay dừng, thở bong bóng, chỉ miệng, đặt tay lên ngực, xắn tay áo.',
   'Đóng vai 1: con "lỡ" làm đổ cốc nước (nước thật, ít). Con đi đủ 5 bước, lấy khăn lau.',
   'Đóng vai 2: con lỡ làm rách tranh của em. Bước "cùng sửa" có thể là dán lại hoặc vẽ tặng tranh mới.',
   'Bố mẹ đóng vai người làm sai một lần để con thấy người lớn cũng nhận lỗi.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Đổ "giả" chút nước ra khay. Nói: "Đổ rồi. Mình lau nhé." Đưa khăn cho con lau cùng.', 'Cảm ơn con: "Con lau giúp, sạch rồi."'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Bước nào khó nhất với con? Vì sao?', 'Làm sai một việc có làm con thành người xấu không?', 'Sửa lỗi xong con thấy thế nào?'])),
 sec(6,'An toàn', ul(['Chỉ dùng nước, không dùng đồ vỡ được khi đóng vai.', 'Lau khô sàn ngay.', 'Không dùng hình phạt đau hay làm con xấu hổ trước người khác.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('sơ đồ 5 bước, cốc nhựa, khăn lau. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Nhắc chuyện Tí trồng lại cây.'),
   ('Phút 2–6 – Năm động tác.', 'Cả nhà làm động tác cho 5 bước.'),
   ('Phút 6–14 – Đóng vai.', 'Con lớn đóng vai 2 tình huống. Mẹ đóng vai người làm sai 1 lần.'),
   ('Phút 14–20 – Con nhỏ.', 'Lau nước cùng mẹ; con lớn khen em.')], [
   ('Câu nên nói:', '"Nước đổ rồi, mình lau nhé." "Con làm rách tranh, mình dán lại nhé."'),
   ('Câu nên tránh:', '"Con hư quá", "Lúc nào cũng hậu đậu". Câu gắn nhãn khiến con muốn giấu lỗi.'),
   ('Nhắn bố 1 câu:', 'bước nào con thấy khó.')])),
 sec(8,'Ôn lại', ul(['<strong>Khi có lỗi thật trong tuần:</strong> chỉ vào sơ đồ, cùng con đi 5 bước. Cảm ơn con trước, sửa sau.',
   '<strong>Sau 1 tuần:</strong> hỏi: "Tuần này con đã sửa lỗi nào?"'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Truyện khen nhân vật nói thật làm trẻ 3–7 tuổi nhận lỗi nhiều hơn; truyện dọa thì không (Lee, Talwar et al. 2014, <a href="https://pubmed.ncbi.nlm.nih.gov/24928424/">PubMed</a>).'),
   lb('Suy luận', 'Thêm bước "cùng sửa" giúp nhận lỗi đi kèm hành động tích cực; nghiên cứu trên không thử trực tiếp bước này.'),
   lb('Đánh giá chuyên môn', 'Nguyên tắc "chê việc, không chê con" là khuyến nghị nuôi dạy phổ biến; daynentang.com dùng như quy tắc của khóa.')]))
])

# =================== TUẦN 7 ===================
make('t7', 'Bài thói quen tuần 7: lắng nghe bằng gậy nói chuyện. Ai cầm gậy thì nói, người khác nghe và nhắc lại ý.',
 ['Mạch A – Thói quen (Ngón áp út)', 'Tuần 7, buổi 1', '20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> nhắc lại đúng ý người vừa nói trước khi nói ý mình, ít nhất 2 lần trong buổi.',
   '<strong>Con nhỏ:</strong> chờ lượt cầm "gậy" một lần rồi chuyền đi.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 "gậy nói chuyện": thìa gỗ, bút to hoặc thú bông nhỏ (to hơn lõi giấy).', 'Cả nhà ngồi thành vòng trên sàn hoặc quanh bàn.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Hai người lớn cố tình nói cùng lúc. Hỏi con: "Con nghe được ai không? Vì sao khó nghe?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Cả nhà (12 phút)</h3>' + ol([
   'Luật: ai cầm gậy thì nói; người khác nghe bằng cả cơ thể (xem hình).',
   'Chủ đề vòng 1: "Món ăn con thích nhất." Mỗi người nói 1 câu rồi chuyền gậy.',
   'Vòng 2 (con lớn): trước khi nói, nhắc lại ý người trước: "Mẹ thích canh chua. Còn con thích…"',
   'Vòng 3: chủ đề khó hơn: "Hôm nay có chuyện gì làm con buồn?" Người nghe chỉ nhắc lại, không khuyên.']) +
   '<h3>Con nhỏ</h3><p>Ngồi trong vòng. Khi đến lượt, con cầm gậy, nói 1 từ hoặc chỉ một món đồ, rồi chuyền đi. Cả nhà vỗ tay khi con chuyền gậy.</p>'),
 sec(5,'Câu hỏi trò chuyện', ol(['Khi được người khác nhắc lại ý mình, con thấy thế nào?', 'Phần nào của "nghe bằng cả cơ thể" khó nhất?', 'Nhà mình có thể dùng gậy nói chuyện lúc nào? (bữa tối, khi cãi nhau)'])),
 sec(6,'An toàn', ul(['Gậy là đồ mềm hoặc nhẹ, không nhọn; không dùng để đánh.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('1 thìa gỗ hoặc thú bông. Tổng 15–20 phút, có thể làm trong bữa tối.', [
   ('Phút 0–2 – Mở đầu.', 'Mẹ và con lớn cố tình nói cùng lúc rồi hỏi: "Có nghe được không?"'),
   ('Phút 2–8 – Vòng 1.', 'Món ăn yêu thích. Con nhỏ tham gia.'),
   ('Phút 8–15 – Vòng 2 và 3.', 'Con lớn nhắc lại ý trước khi nói.'),
   ('Phút 15–17 – Kết thúc.', 'Hỏi: "Được nghe trọn vẹn thấy thế nào?"')], [
   ('Gọi video với bố:', 'bố cũng tham gia vòng nói (bố "cầm gậy" khi mẹ chĩa điện thoại về phía bố).'),
   ('Nhắn bố 1 câu:', 'điều con kể ở vòng 3.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> dùng gậy nói chuyện trong bữa tối 5 phút.', '<strong>Sau 1 tuần:</strong> khi hai con tranh cãi, đưa gậy: "Mỗi người nói một lượt, người kia nhắc lại."'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{HARVARD} gợi ý các trò chơi theo lượt và trò hỏi – đáp cho trẻ 5–7 tuổi để luyện chú ý và kiềm chế.'),
   lb('Đánh giá chuyên môn', 'Gậy nói chuyện và bước "nhắc lại ý" do daynentang.com đưa vào khung "Nghe – hiểu – cùng vui".')]))
])

make('k7', 'Bài khoa học tuần 7: dùng các giác quan qua trò túi bí ẩn. Con sờ, ngửi, nghe để đoán đồ vật.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 7, buổi 2', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> dùng ít nhất 3 từ tả cảm giác (mềm, cứng, nhám, trơn, tròn, có góc) để đoán đúng 4/6 đồ vật.',
   '<strong>Con nhỏ:</strong> thò tay vào túi lấy ra 1 đồ và gọi tên hoặc chỉ đồ giống trong nhà.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['1 túi vải hoặc gối có khóa kéo.', '6 đồ to, sạch: quả bóng nhỏ, thìa gỗ, khăn mặt, miếng bọt biển, quả cam, khối gỗ.',
   '3 lọ ngửi (lọ nhựa có lỗ trên nắp): vỏ cam, lá chanh, hoa nhài. 2 hộp lắc: một hộp có gạo, một hộp có khối gỗ (dán chặt nắp).'])),
 sec(3,'Mở đầu (2 phút)', '<p>Chỉ lần lượt mắt, tai, mũi, tay: "Mỗi bộ phận giúp con biết điều gì?" Cùng xem sơ đồ năm giác quan.</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   '<strong>Sờ:</strong> con thò tay vào túi, không nhìn. Nói 2 từ tả: "mềm, tròn".',
   '<strong>Đoán:</strong> "Con đoán là…" rồi mới lấy ra. Đúng thì ghi ✓, sai thì ghi điều mình bỏ sót.',
   '<strong>Ngửi:</strong> nhắm mắt ngửi 3 lọ, đoán mùi.',
   '<strong>Nghe:</strong> lắc 2 hộp, đoán hộp nào có gạo, hộp nào có khối gỗ.',
   '<strong>Kể lại:</strong> giác quan nào giúp con đoán đúng nhiều nhất?']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Bố mẹ cầm miệng túi. Con thò tay lấy 1 đồ.', 'Gọi tên cùng con: "Khăn! Mềm quá."', 'Lặp lại với 3–4 đồ to.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Đồ nào khó đoán nhất? Vì sao?', 'Nếu không nhìn được, con dựa vào giác quan nào?', 'Bài này không nếm. Vì sao không nên nếm đồ lạ?'])),
 sec(6,'An toàn', ul(['Mọi đồ trong túi phải to, sạch, không sắc nhọn, không có chi tiết rời.',
   'Hộp lắc dán chặt nắp; gạo bên trong là vật nhỏ, không để con nhỏ mở.', 'Chỉ ngửi mùi tự nhiên an toàn; không ngửi hóa chất, nước tẩy, tinh dầu đậm đặc.',
   'Không nếm trong bài này. Hỏi trước nếu con dị ứng với cam, chanh hay hoa.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('1 túi vải, 6 đồ to, 2 lọ ngửi. Tổng 20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Chỉ mắt, tai, mũi, tay và hỏi mỗi phần giúp gì.'),
   ('Phút 2–6 – Con nhỏ.', 'Con nhỏ lấy đồ trong túi, mẹ gọi tên.'),
   ('Phút 6–16 – Con lớn.', 'Sờ, tả, đoán 6 đồ. Ngửi 2 lọ.'),
   ('Phút 16–20 – Kể lại.', 'Giác quan nào giúp nhiều nhất?')], [
   ('Nếu không có túi vải:', 'dùng vỏ gối hoặc hộp giấy khoét lỗ vừa tay.'),
   ('Nhắn bố 1 câu:', 'con đoán đúng mấy đồ.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> lúc đi dạo, hỏi: "Con nghe thấy gì? Ngửi thấy gì?"', '<strong>Sau 1 tuần:</strong> con tự chuẩn bị túi bí ẩn để đố bố mẹ.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Tập tả cảm giác bằng từ ngữ giúp con quan sát kỹ hơn; trò túi bí ẩn do daynentang.com thiết kế.'),
   lb('Đánh giá chuyên môn', 'Quy tắc không nếm và chỉ ngửi mùi tự nhiên là quy tắc an toàn của dự án.')]))
])

make('g7', 'Bài giá trị tuần 7: thám tử cảm xúc. Con nhìn mặt, cơ thể và tình huống để đoán cảm xúc người khác, rồi hỏi và giúp.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 7, buổi 3', '20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> nêu 3 manh mối (mặt, cơ thể, tình huống) để đoán cảm xúc trong 3 tranh, và nói một câu hỏi han.',
   '<strong>Con nhỏ:</strong> ôm hoặc đưa đồ chơi cho người đang làm mặt buồn.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['3 thẻ manh mối: Mặt · Cơ thể · Tình huống (vẽ như hình).', '3 tranh tình huống tự vẽ: bạn ngã, bạn mất đồ chơi, bạn được quà.', '4 tranh gương mặt từ bài G4.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Thám tử tìm manh mối để biết chuyện gì đã xảy ra. Hôm nay con làm thám tử cảm xúc."</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15 phút)</h3>' + ol([
   'Kể chuyện ngắn: Mướp mất quả bóng, ngồi cúi đầu. Tí nhìn thấy, hỏi "Mướp buồn à? Tớ giúp nhé." Hai bạn cùng tìm bóng.',
   'Cầm từng tranh tình huống. Con dùng 3 thẻ manh mối: mặt thế nào? cơ thể thế nào? chuyện gì xảy ra?',
   'Con đoán cảm xúc, rồi nói câu hỏi han: "Bạn ổn không?", "Tớ giúp gì được không?"',
   'Bố mẹ diễn một cảm xúc không nói ra (thở dài, khoanh tay). Con làm thám tử đoán.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Bố mẹ làm mặt buồn, khóc giả: "Ô ô…"', 'Hỏi: "Mẹ buồn, con làm gì giúp mẹ?" Chờ con ôm hoặc đưa đồ chơi.', 'Cười ngay: "Cảm ơn con, mẹ vui rồi!"'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Manh mối nào giúp con đoán nhanh nhất?', 'Nếu đoán sai thì sao? (hỏi lại là được)', 'Ở lớp, con thấy bạn nào buồn chưa? Con có thể làm gì?'])),
 sec(6,'An toàn', ul(['Dạy con hỏi han và báo người lớn khi bạn bị đau hay gặp nguy hiểm; không tự xử lý một mình.', 'Không trêu chọc khi đóng vai cảm xúc.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('3 thẻ manh mối, 3 tranh tự vẽ. Tổng 20 phút.', [
   ('Phút 0–3 – Mở đầu.', 'Kể chuyện Tí và Mướp.'),
   ('Phút 3–12 – Thám tử.', 'Con lớn dùng 3 thẻ cho 3 tranh.'),
   ('Phút 12–16 – Mẹ diễn.', 'Mẹ diễn một cảm xúc; con đoán.'),
   ('Phút 16–20 – Con nhỏ.', 'Mẹ làm mặt buồn; con nhỏ an ủi.')], [
   ('Làm mẫu trong tuần:', 'khi thấy ai buồn, mẹ nói to cách mẹ đoán: "Chị kia nhíu mày, chắc chị đang lo."'),
   ('Nhắn bố 1 câu:', 'câu hỏi han con nghĩ ra.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> khi xem tranh truyện, hỏi: "Bạn này đang thấy thế nào? Manh mối là gì?"', '<strong>Sau 1 tuần:</strong> hỏi con đã hỏi han ai trong tuần.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Phân tích gộp 24 nghiên cứu: bố mẹ làm mẫu, đáp lại và chỉ dạy về cảm xúc gắn với kỹ năng cảm xúc tốt hơn ở trẻ mầm non; mức liên hệ nhỏ, phần lớn là tương quan (Zinsser, Gordon &amp; Jiang 2021).'),
   lb('Đánh giá chuyên môn', 'Ba thẻ manh mối và chuyện Tí – Mướp do daynentang.com sáng tác.')]))
])

# =================== TUẦN 8 ===================
make('t8', 'Bài thói quen tuần 8: anh hướng dẫn em theo 4 bước. Cả hai cùng học; người lớn vẫn trông em.',
 ['Mạch A – Thói quen (Ngón áp út)', 'Tuần 8, buổi 1', '20 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> hướng dẫn em một việc nhỏ theo 4 bước, không làm hộ, và khen em một điều cụ thể.',
   '<strong>Con nhỏ:</strong> làm theo anh một bước (đặt một khối, cất một đồ).'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['6–8 khối Duplo to.', 'Sơ đồ 4 bước "Anh dạy em".', 'Một việc nhỏ để anh dạy: xếp tháp 3 khối, cất dép đúng đôi, tưới cây bằng cốc.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Hồi bé ai dạy con xếp khối? Hôm nay con làm thầy giáo nhỏ của em."</p>'),
 sec(4,'Hoạt động chính', '<h3>Hai con cùng làm (15 phút)</h3>' + ol([
   'Bố mẹ dạy con lớn 4 bước trên sơ đồ: <strong>làm mẫu – làm cùng – em làm, anh xem – khen cụ thể</strong>.',
   'Anh dạy em xếp tháp 3 khối. Anh nói câu ngắn: "Đặt khối đỏ xuống. Giờ khối vàng."',
   'Khi em làm sai, anh chờ và chỉ lại, không giành làm.',
   'Kết thúc, anh khen một điều cụ thể: "Em đặt khối thẳng lắm!"',
   'Bố mẹ khen anh: "Con chờ em kiên nhẫn quá."']) +
   '<p><strong>Vai của bố mẹ:</strong> ngồi cạnh, chỉ giúp khi cả hai bế tắc. Bố mẹ vẫn là người trông em.</p>'),
 sec(5,'Câu hỏi trò chuyện', ol(['Dạy em có khó không? Chỗ nào khó?', 'Con học được gì khi làm thầy giáo?', 'Lần sau con muốn dạy em việc gì?'])),
 sec(6,'An toàn', ul(['Anh không chịu trách nhiệm trông em; người lớn luôn ở cạnh.', 'Việc anh dạy phải an toàn cho em: không dao kéo, không nước nóng, không trèo cao.', SMALL])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('6–8 khối Duplo, sơ đồ 4 bước. Tổng 15–20 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi con lớn: "Con muốn dạy em việc gì?"'),
   ('Phút 2–5 – Dạy anh.', 'Mẹ chỉ 4 bước trên sơ đồ.'),
   ('Phút 5–15 – Anh dạy em.', 'Mẹ ngồi cạnh, không xen vào trừ khi cần.'),
   ('Phút 15–18 – Khen.', 'Anh khen em một điều; mẹ khen anh một điều.')], [
   ('Nếu anh mất kiên nhẫn:', 'đổi sang việc dễ hơn hoặc dừng. Không ép anh phải dạy em.'),
   ('Nhắn bố 1 câu:', 'việc anh đã dạy em.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> để anh dạy em một việc nhỏ trong sinh hoạt (cất dép đúng đôi).', '<strong>Sau 1 tuần:</strong> đổi vai: em "dạy" anh một trò của em.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Quan sát 39 gia đình ở Canada có con khoảng 4 và 6 tuổi: anh chị em dạy nhau một cách tự nhiên, thường xuyên; anh chị hay dạy cách làm, em hay hỏi khái niệm (Howe et al., <em>Journal of Cognition and Development</em>; <a href="https://www.sciencedaily.com/releases/2014/07/140709115505.htm">ScienceDaily</a>).'),
   lb('Đánh giá chuyên môn', 'Bốn bước "làm mẫu – làm cùng – tự làm – khen" là trình tự hướng dẫn phổ biến trong giảng dạy; daynentang.com rút gọn cho trẻ.')]))
])

make('k8', 'Bài khoa học tuần 8: thời tiết quanh nhà. Con quan sát trời mỗi sáng, ghi bảng ký hiệu và làm cốc đo mưa.',
 ['Mạch B – Khoa học bằng tay', 'Tuần 8, buổi 2', '25 phút + 2 phút mỗi sáng'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> ghi ký hiệu thời tiết 7 ngày liền, đếm số ngày nắng, mây, mưa và nói ngày nào nhiều nhất.',
   '<strong>Con nhỏ:</strong> chỉ ra cửa sổ và nói "nắng" hoặc "mưa".'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Bảng thời tiết 7 ngày (vẽ như hình), bút sáp.', '1 chai nhựa trong 1,5 lít (người lớn cắt), băng dính, thước hoặc dải giấy chia vạch.'])),
 sec(3,'Mở đầu (2 phút)', '<p>Cùng đứng ở cửa sổ: "Hôm nay trời thế nào? Con nhìn thấy gì? Cảm thấy gì trên da?"</p>'),
 sec(4,'Hoạt động chính – Quan sát → Đoán → Thử → Kể lại', '<h3>Con lớn (20 phút)</h3>' + ol([
   '<strong>Quan sát:</strong> con vẽ ký hiệu hôm nay vào bảng: nắng, mây hay mưa.',
   '<strong>Làm cốc đo mưa:</strong> người lớn cắt chai, dán băng dính kín mép cắt. Úp phần miệng làm phễu. Con dán dải giấy chia vạch.',
   'Đặt cốc ở chỗ trống, không bị mái che, chèn chắc để không đổ.',
   '<strong>Đoán:</strong> tuần này có mấy ngày mưa?',
   '<strong>Kể lại:</strong> xem sơ đồ "nước đi một vòng". Hỏi: "Nước mưa từ đâu ra?"']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Bế con ra cửa sổ: "Nắng hay mưa?"', 'Cho con dán sticker mặt trời hoặc giọt mưa lên bảng.'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Ngày mưa và ngày nắng, nhà mình làm gì khác nhau?', 'Mây ở đâu ra?', 'Cuối tuần, con đoán đúng không?'])),
 sec(6,'An toàn', ul(['Người lớn cắt chai và dán kín mép cắt; con không cầm dao kéo.', 'Không ra ngoài khi có sấm sét. Trời nắng gắt thì đội mũ, ở ngoài ngắn.',
   'Đổ nước trong cốc đo mưa sau khi đọc số; không để nước đọng (tránh muỗi và nguy cơ đuối nước với trẻ nhỏ).'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('bảng thời tiết, bút sáp, sticker (nếu có). Cốc đo mưa có thể để bố làm. Tổng 15 phút.', [
   ('Phút 0–2 – Mở đầu.', 'Đứng ở cửa sổ, hỏi về trời hôm nay.'),
   ('Phút 2–8 – Bảng thời tiết.', 'Con lớn vẽ ký hiệu; con nhỏ dán sticker.'),
   ('Phút 8–15 – Nước đi một vòng.', 'Xem sơ đồ, kể lại bằng lời của con.')], [
   ('Mỗi sáng 2 phút:', 'nhắc con vẽ ký hiệu trước khi đi học.'),
   ('Nhắn bố 1 câu:', 'thời tiết hôm nay con ghi.')])),
 sec(8,'Ôn lại', ul(['<strong>Mỗi sáng:</strong> vẽ ký hiệu. Nếu có mưa, đọc vạch nước rồi đổ đi.', '<strong>Sau 1 tuần:</strong> đếm từng loại; vẽ biểu đồ cột như bài K4.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đánh giá chuyên môn', 'Sơ đồ "nước đi một vòng" là cách nói đơn giản cho trẻ, chưa phải mô tả đầy đủ vòng tuần hoàn của nước.'),
   lb('Đã xác nhận', f'Không để nước đọng trong đồ chứa khi có trẻ nhỏ ({WATER}).'),
   lb('Đánh giá chuyên môn', 'Bảng thời tiết và cốc đo mưa do daynentang.com thiết kế.')]))
])

make('g8', 'Bài giá trị tuần 8: biết ơn người lao động quanh nhà. Con nhận ra ai giúp mình, cảm ơn bằng lời và vẽ thiệp tặng.',
 ['Mạch C – Giá trị và chánh niệm', 'Tuần 8, buổi 3', '20–25 phút'], [
 sec(1,'Mục tiêu', ul(['<strong>Con lớn:</strong> kể tên 5 người lao động giúp nhà mình, vẽ 1 thiệp và tự nói lời cảm ơn khi tặng (có bố mẹ đi cùng).',
   '<strong>Con nhỏ:</strong> vẫy tay chào và nói "cảm ơn" với một người lao động khi đi cùng bố mẹ.'])),
 sec(2,'Chuẩn bị (5 phút)', ul(['Sơ đồ "Ai giúp nhà mình mỗi ngày?" để con điền thêm.', 'Giấy bìa, bút sáp để làm thiệp.'])),
 sec(3,'Mở đầu (2 phút)', '<p>"Sáng nay rác nhà mình đi đâu? Rau mình ăn từ đâu đến? Ai làm những việc đó?"</p>'),
 sec(4,'Hoạt động chính', '<h3>Con lớn (15–20 phút)</h3>' + ol([
   'Xem sơ đồ. Con kể thêm người lao động con biết: bác lao công ở trường, chú sửa xe, cô bán bánh mì.',
   'Với mỗi người, con nói một câu: "Bác thu gom rác giúp nhà mình sạch."',
   'Con chọn 1 người để vẽ thiệp cảm ơn. Viết hoặc vẽ: cảm ơn ai, vì sao.',
   'Hẹn ngày đi cùng bố mẹ để tặng thiệp và nói lời cảm ơn.']) +
   '<h3>Con nhỏ (5 phút)</h3>' + ol(['Xem tranh, chỉ người lao động: "Ai đây? Bác thu gom rác."', 'Tập vẫy tay và nói "cảm ơn".'])),
 sec(5,'Câu hỏi trò chuyện', ol(['Nếu một ngày không ai thu gom rác thì sao?', 'Người lao động có biết con cảm ơn họ không?', 'Khi lớn lên, con muốn làm công việc gì để giúp người khác?'])),
 sec(6,'An toàn', ul(['Con chỉ nói chuyện và tặng quà khi có bố mẹ đi cùng.', 'Không đứng gần xe rác, xe máy đang chạy khi tặng thiệp.'])),
 sec(7,'Cho mẹ dạy (khi bố đi vắng)', mom('sơ đồ, giấy bìa, bút sáp. Tổng 20 phút + 5 phút đi tặng thiệp.', [
   ('Phút 0–2 – Mở đầu.', 'Hỏi rác đi đâu, rau từ đâu.'),
   ('Phút 2–8 – Sơ đồ.', 'Con lớn kể thêm người lao động; con nhỏ chỉ tranh.'),
   ('Phút 8–18 – Vẽ thiệp.', 'Con lớn vẽ thiệp cho một người.'),
   ('Phút 18–20 – Hẹn.', 'Chọn ngày đi tặng thiệp cùng mẹ.')], [
   ('Khi tặng:', 'mẹ đứng cạnh, để con tự nói "Cháu cảm ơn bác…". Không ép nếu con ngại; vẫy tay cũng được.'),
   ('Nhắn bố 1 câu:', 'con tặng thiệp cho ai.')])),
 sec(8,'Ôn lại', ul(['<strong>Sau 1 ngày:</strong> thêm 1 mẩu giấy vào lọ cảm ơn (bài G2) cho một người lao động.',
   '<strong>Sau 1 tuần:</strong> hỏi con đã nói cảm ơn ai trong tuần. Đây cũng là bài cuối tháng thứ hai; cả nhà chọn bài con thích nhất.'])),
 sec(9,'Nhật ký sau buổi', JOURNAL),
 sec(10,'Nguồn và nhãn', ul([
   lb('Đã xác nhận', 'Thử nghiệm với 221 học sinh đầu tuổi thiếu niên: "đếm điều may mắn" làm tăng biết ơn, lạc quan và hài lòng cuộc sống (Froh, Sefick &amp; Emmons 2008).'),
   lb('Suy luận', 'Áp dụng cho trẻ 2–8 tuổi qua hành động cụ thể (thiệp, lời cảm ơn) là thiết kế của daynentang.com; chưa được thử trực tiếp ở độ tuổi này.')]))
])
print('weeks 5-8 built')
