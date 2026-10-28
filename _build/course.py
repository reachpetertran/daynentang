from common import page, HELP_BOX, PRINT_ROW

BASE = '/khoa-hoc/gia-dinh-2-8/'

WEEKS = [
 ('1','<a href="tuan-1/t1-minh-tu-lam-duoc/">Mình tự làm được</a>','<a href="tuan-1/k1-noi-hay-chim/">Nổi hay chìm?</a>','<a href="tuan-1/g1-noi-that-long-nhe/">Nói thật, lòng nhẹ</a>','7t: tự làm việc đã chọn ≥4/7 ngày. 2t: cất 3 món đồ chơi khi nhắc'),
 ('2','Thử – sai – thử lại','Nước: rót, đong, thấm','Biết ơn: 3 điều cảm ơn trước ngủ','7t: nói "con thử cách khác". 2t: tự rót nước từ bình nhỏ'),
 ('3','Nhìn đích rồi đi','Gieo hạt đậu xanh, nhật ký mầm','Tử tế: việc tốt bí mật','7t: tự đặt 1 mục tiêu và tự kiểm. 2t: chọn 1 trong 2 tranh việc'),
 ('4','Kế hoạch Trước – Trong – Sau','Đo mầm bằng que, vẽ nhật ký','Dừng – Thở – Nói: gọi tên cảm xúc','7t: vẽ kế hoạch 3 bước. 2t: chỉ đúng 2 gương mặt cảm xúc'),
 ('5','Việc quan trọng làm trước','Ánh sáng và bóng','Trách nhiệm: việc nhà của con','7t: làm việc chính trước ≥4/7 ngày. 2t: cất đồ khi có bài hát'),
 ('6','Chờ lượt: Đèn đỏ – Đèn xanh','Dốc và lực: lăn xe trên ván nghiêng','Trung thực 2: nhận lỗi và sửa lỗi','7t: dừng đúng tín hiệu ≥8/10. 2t: ≥5/10'),
 ('7','Lắng nghe: gậy nói chuyện','Giác quan: túi bí ẩn (đồ to)','Tử tế 2: đoán cảm xúc người khác','7t: nhắc lại ý người khác. 2t: chờ lượt nói 1 lần'),
 ('8','Cùng vui: anh hướng dẫn em','Thời tiết: bảng mây, mưa, nắng','Biết ơn 2: cảm ơn người lao động quanh nhà','7t: hướng dẫn em 1 việc. 2t: làm theo anh 1 bước'),
 ('9','Chăm cây của mình: ngủ, ăn, vận động','Khủng long và hóa thạch: in dấu trên đất nặn','Chánh niệm: đi chậm, ăn chậm','Giờ ngủ đều ≥5/7 ngày (cả hai bé)'),
 ('10','Góc bình tĩnh khi giận','Thiết kế thuyền chở nhiều đồ nhất','Trách nhiệm 2: giữ lời hứa nhỏ','7t: tự dùng góc bình tĩnh 1 lần. 2t: chấp nhận ôm hoặc thở cùng'),
 ('11','Cả bàn tay: chậu rau gia đình','Con hỏi – con thử','Tử tế với chính mình','7t: tự đặt câu hỏi và dự đoán. 2t: gọi tên 3 bộ phận cây'),
 ('12','Lễ Bàn tay nền tảng: con kể 5 ngón','Triển lãm khoa học gia đình','Ôn 4 giá trị, vẽ ước nguyện','Đánh giá cuối khóa'),
]
rows = ''.join(f'<tr><td>{w}</td><td>{t}</td><td>{k}</td><td>{g}</td><td>{m}</td></tr>' for w,t,k,g,m in WEEKS)

page(BASE, 'Gia đình 2–8 tuổi: Bàn tay nền tảng',
 'Khóa 12 tuần miễn phí cho bố mẹ: dạy con 2–8 tuổi thói quen tự chủ, khám phá khoa học và giá trị tử tế bằng đồ có sẵn trong nhà.',
f'''
<p class="eyebrow">Gia đình · Khóa G3 · Đang thử nghiệm</p>
<h1>Gia đình 2–8 tuổi: Bàn tay nền tảng</h1>
<p class="lead">Bố mẹ, kể cả khi chỉ một người dạy, xây cho con ba nền tảng qua 30 phút chơi có chủ đích:
thói quen tự chủ, tư duy khám phá và giá trị tử tế. Đồng thời giảm la mắng trong nhà.</p>

<div class="table-wrap"><table>
<tbody>
<tr><th>Dành cho</th><td>Bố mẹ, ông bà, người chăm sóc trẻ 2–8 tuổi</td></tr>
<tr><th>Thời lượng</th><td>12 tuần × 3 buổi × 30 phút. Bố mẹ chuẩn bị khoảng 30 phút mỗi tuần</td></tr>
<tr><th>Cần có</th><td>Đồ có sẵn trong nhà, giấy, bút sáp to. Trẻ không cần màn hình</td></tr>
<tr><th>Tình trạng</th><td>Tuần 1 đã có. Các tuần sau đăng dần sau khi dạy thử</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Mỗi ngày có một khoảng chơi vui cùng con.</li><li>Con tự làm được ít nhất 1 việc nhỏ.</li><li>Bố mẹ có câu nói mẫu thay cho la mắng.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Chức năng điều hành: chú ý, ghi nhớ, tự kiểm soát.</li><li>Thói quen hỏi, đoán và tự kiểm chứng.</li><li>Trung thực, biết ơn, tử tế, trách nhiệm.</li></ul></div>
</div>

<h2>Bàn tay nền tảng</h2>
<p>Năm ngón tay là năm thói quen. Con nhìn bàn tay mình là nhớ.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ngón</th><th>Thói quen</th></tr></thead>
<tbody>
<tr><td>Ngón cái</td><td>Mình tự làm được</td></tr>
<tr><td>Ngón trỏ</td><td>Nhìn đích rồi đi</td></tr>
<tr><td>Ngón giữa</td><td>Việc quan trọng làm trước</td></tr>
<tr><td>Ngón áp út</td><td>Nghe – hiểu – cùng vui</td></tr>
<tr><td>Ngón út</td><td>Chăm cây của mình (ngủ, ăn, vận động, bình tĩnh)</td></tr>
</tbody></table></div>

<h2>Lịch 12 tuần</h2>
<p>Mỗi tuần 3 buổi: <strong>T</strong> Thói quen, <strong>K</strong> Khoa học bằng tay (Quan sát → Đoán → Thử → Kể lại), <strong>G</strong> Giá trị và chánh niệm.</p>
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>T – Thói quen</th><th>K – Khoa học</th><th>G – Giá trị</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="small muted">7t = con khoảng 7 tuổi; 2t = con khoảng 2 tuổi. Điều chỉnh theo tuổi con nhà bạn.</p>

<h2>Một buổi 30 phút</h2>
<ol>
<li><strong>Kết nối</strong> (0–3'): chào, ngồi gần. Bé 2 tuổi ngồi lòng bố mẹ.</li>
<li><strong>Thở 1 phút</strong> (3–5'): "ngửi hoa – thổi nến".</li>
<li><strong>Hoạt động chính</strong> (5–20'): hai mức độ, cho con lớn và con nhỏ.</li>
<li><strong>Con kể lại</strong> (20–25'): bé 2 tuổi chỉ, gọi tên hoặc bắt chước.</li>
<li><strong>Mang vào đời sống</strong> (25–30'): chọn 1 việc làm trong tuần, dán sticker.</li>
</ol>
<p>Bé 2 tuổi tham gia 10–15 phút rồi chơi song song gần đó. Không ép ngồi đủ 30 phút.</p>

<h2>Theo dõi tiến bộ</h2>
<p>Chấm <a href="/cong-cu/bang-quan-sat/">bảng quan sát</a> ở tuần 0, 6 và 12: 0 = chưa, 1 = cần nhắc, 2 = tự làm.
Ghi thêm số lần bố mẹ khen cụ thể và số lần la mắng trong 3 ngày. Đây là cách tự theo dõi, không phải bài kiểm tra.</p>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td><a href="https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health">Parenting for Lifelong Health</a> (WHO/UNICEF)</td><td>Chơi một – một, khen cụ thể, hướng dẫn rõ, hậu quả không bạo lực</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên ở Nam Phi (296 người chăm sóc): hành vi nuôi dạy tích cực quan sát được tăng 39% sau 4–5 tháng (Ward et al. 2019)</td></tr>
<tr><td><a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Hướng dẫn hoạt động chức năng điều hành</a> (Harvard)</td><td>Trò chơi theo tuổi 18–36 tháng và 5–7 tuổi</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn chuyên gia, không phải thử nghiệm ngẫu nhiên</td></tr>
<tr><td><a href="https://casel.org/what-is-sel/">CASEL</a></td><td>Đặt tên mục tiêu theo 5 năng lực cảm xúc – xã hội</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp 424 nghiên cứu (Cipriano et al. 2023), chủ yếu ở trường học</td></tr>
<tr><td><a href="https://reachupandlearn.com/resources/">Reach Up</a></td><td>Chơi bằng đồ tự làm cho trẻ nhỏ</td><td><span class="label">[Đã xác nhận]</span> Theo dõi dài hạn ở Jamaica (Gertler et al.)</td></tr>
<tr><td>Lee, Talwar et al. 2014, <em>Psychological Science</em></td><td>Kể chuyện khen người nói thật</td><td><span class="label">[Đã xác nhận]</span> 268 trẻ 3–7 tuổi; tác dụng ngắn hạn</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các chương trình trên phần lớn được thử theo nhóm, có người hướng dẫn. Tự học tại nhà chưa được chứng minh cho hiệu quả tương đương.
  Khóa này đang được dạy thử trong một gia đình, không có nhóm so sánh. Chúng tôi không hứa về điểm số hay chỉ số IQ.</p>
</div>

<h2>Xem trước khi dạy</h2>
<ul>
<li><a href="https://developingchild.harvard.edu/resources/videos/how-to-5-steps-for-brain-building-serve-and-return/">5 bước "Giao và đáp" – Harvard Center on the Developing Child</a> (video, tiếng Anh)</li>
<li><a href="https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/">Hướng dẫn hoạt động chức năng điều hành – Harvard</a> (tài liệu PDF, tiếng Anh)</li>
<li><a href="https://reachupandlearn.com/resources/">Reach Up – tài nguyên và video</a> (tiếng Anh)</li>
</ul>

<h2>An toàn cho mọi buổi</h2>
<ul>
<li>Bé dưới 3 tuổi: không để vật nhỏ trong tầm với. Mẹo nhà: vật lọt qua lõi giấy vệ sinh là quá nhỏ.</li>
<li>Không dùng pin cúc áo, nam châm nhỏ, túi nilon, dao kéo sắc gần bé nhỏ.</li>
<li>Chơi với nước: người lớn luôn trong tầm tay; đổ nước ngay sau buổi.</li>
</ul>
{HELP_BOX}
''', current='/gia-dinh/')
