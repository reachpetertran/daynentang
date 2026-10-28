from common import page, HELP_BOX, PRINT_ROW

# ---------------- Trang chủ ----------------
page('/', 'Dạy Nền Tảng – nền tảng làm người, tự học miễn phí – daynentang.com',
 'Khóa học miễn phí, dựa trên bằng chứng, giúp gia đình và mỗi người tự học năng lực, đạo đức, tinh thần, thể chất.',
 '''
<section class="hero">
  <div>
    <p class="eyebrow">Tự học miễn phí</p>
    <h1>Nền tảng làm người, bắt đầu từ gia đình</h1>
    <p class="lead">daynentang.com giúp mỗi gia đình và mỗi người tự học bốn nền tảng: năng lực, đạo đức, tinh thần, thể chất.
    Mỗi bài dựa trên bằng chứng và dùng được ngay, kể cả khi không có tiền, không có thầy.</p>
    <div class="cta">
      <a class="btn primary" href="/gia-dinh/">Tôi là bố mẹ</a>
      <a class="btn" href="/ca-nhan/">Tôi tự học</a>
      <a class="btn warm" href="/can-giup-ngay/">Tôi cần giúp ngay</a>
    </div>
  </div>
  <img src="/assets/logo/daynentang-logo.svg" alt="Logo Dạy Nền Tảng: núi, mặt trời và các con vật dưới dải băng chữ" width="400" height="428">
</section>

<h2>Mỗi khóa hứa hai điều</h2>
<div class="two">
  <div class="card"><h3>Giúp ngay</h3><p>Một kết quả thực tế bạn thấy được trong 1–2 tuần.</p></div>
  <div class="card"><h3>Xây lâu dài</h3><p>Một cách nghĩ và một kỹ năng dùng được nhiều năm.</p></div>
</div>

<h2>Khóa đang mở</h2>
<a class="card" href="/khoa-hoc/gia-dinh-2-8/">
  <span class="tag">Đang thử nghiệm · đủ 12 tuần</span>
  <h3>Gia đình 2–8 tuổi: Bàn tay nền tảng</h3>
  <p>12 tuần, 3 buổi mỗi tuần, 30 phút mỗi buổi. Bố mẹ dạy con thói quen tự chủ, tư duy khám phá và giá trị tử tế bằng đồ có sẵn trong nhà. Trẻ không cần màn hình.</p>
</a>
<a class="card" href="/khoa-hoc/gia-tri-nha-minh/">
  <span class="tag">Đang thử nghiệm · đủ 4 tuần</span>
  <h3>Giá trị nhà mình</h3>
  <p>4 tuần, mỗi tuần 1 buổi bố mẹ và 1 buổi cả nhà. Chọn 3–5 giá trị, biến thành việc làm, đặt nội quy và họp gia đình 15 phút mỗi tuần.</p>
</a>
<a class="card" href="/khoa-hoc/tien-nha-minh/">
  <span class="tag">Đang thử nghiệm · đủ 6 tuần</span>
  <h3>Tiền nhà mình</h3>
  <p>6 tuần: ghi thu chi, bảng tháng, quỹ khẩn cấp, tránh tín dụng đen, đi chợ có kế hoạch. Con học cần – muốn và hũ ba ngăn.</p>
</a>
<a class="card" href="/khoa-hoc/viec-nha-chia-deu/">
  <span class="tag">Đang thử nghiệm · đủ 4 tuần</span>
  <h3>Việc nhà chia đều</h3>
  <p>4 tuần: nhìn thấy mọi việc nhà kể cả phần nghĩ, chia lại cho công bằng, dạy con làm việc theo tuổi, dọn nhà 10 phút mỗi ngày.</p>
</a>
<a class="card" href="/khoa-hoc/gia-dinh-0-2/">
  <span class="tag">Đang thử nghiệm · đủ 8 tuần</span>
  <h3>Gia đình 0–2 tuổi – Giao và Đáp</h3>
  <p>8 tuần, 5 phút mỗi ngày: nhận ra và đáp lại lời "giao" của em bé, đọc sách từ sớm, vận động, ngủ an toàn, kế hoạch khi con khóc.</p>
</a>
<a class="card" href="/khoa-hoc/gia-dinh-10-14/">
  <span class="tag">Đang thử nghiệm · đủ 7 tuần</span>
  <h3>Gia đình có con 10–14</h3>
  <p>7 tuần: thời gian riêng, lắng nghe để con muốn kể, thỏa thuận nhà mình, điện thoại và mạng xã hội, áp lực bạn bè, cảm xúc.</p>
</a>
<a class="card" href="/khoa-hoc/vo-chong-dong-long/">
  <span class="tag">Đang thử nghiệm · đủ 6 tuần</span>
  <h3>Vợ chồng đồng lòng</h3>
  <p>6 tuần: hai người một đội khi nuôi con, cảm ơn nhau, mở lời nhẹ khi bất đồng, tạm dừng khi giận, không kéo con vào.</p>
</a>

<h2>Bốn trụ cột</h2>
<div class="grid">
  <div class="card"><h3>Năng lực</h3><p>Tự phục vụ, lập kế hoạch, ưu tiên, quản lý tiền và việc nhà.</p></div>
  <div class="card"><h3>Đạo đức</h3><p>Trung thực, biết ơn, tử tế, trách nhiệm, tinh thần lao động.</p></div>
  <div class="card"><h3>Tinh thần</h3><p>Gọi tên cảm xúc, thở ngắn, bình tĩnh khi giận, biết khi nào cần giúp.</p></div>
  <div class="card"><h3>Thể chất</h3><p>Giấc ngủ, vận động, bữa cơm chung, an toàn trong nhà.</p></div>
</div>

<div class="box">
  <h3>Cách chúng tôi làm</h3>
  <p>Mỗi bài ghi nguồn và nhãn mức độ chắc chắn. Chúng tôi chỉ mượn ý tưởng từ chương trình có bản quyền và viết lại hoàn toàn.
  Bài được gia đình người soạn dạy thử trước khi đăng. <a href="/gioi-thieu/">Đọc nguyên tắc</a>.</p>
</div>
''', current='/')

# ---------------- Gia đình ----------------
FAMILY = [
 ('G3','Gia đình 2–8 tuổi','Thói quen tự chủ, khám phá khoa học, giá trị tử tế qua 30 phút chơi.','12 tuần','/khoa-hoc/gia-dinh-2-8/',True),
 ('G1','Giá trị nhà mình','Cả nhà thống nhất 3–5 giá trị và nội quy; họp gia đình 15 phút mỗi tuần.','4 tuần','/khoa-hoc/gia-tri-nha-minh/',True),
 ('G6','Tiền nhà mình','Bảng thu chi tháng, quỹ khẩn cấp, dạy con làm – tiết kiệm – chi.','6 tuần','/khoa-hoc/tien-nha-minh/',True),
 ('G7','Việc nhà chia đều','Phân công việc nhà công bằng; bảng việc nhà theo tuổi cho con.','4 tuần','/khoa-hoc/viec-nha-chia-deu/',True),
 ('G2','Gia đình 0–2 tuổi','Tương tác "giao và đáp" 5 phút mỗi ngày để xây gắn bó và ngôn ngữ.','8 tuần','/khoa-hoc/gia-dinh-0-2/',True),
 ('G4','Gia đình có con 10–14','Đồng hành tuổi dậy thì: trò chuyện, ranh giới, tự lập.','7 tuần','/khoa-hoc/gia-dinh-10-14/',True),
 ('G5','Vợ chồng đồng lòng','Cùng một đội khi nuôi con; nói chuyện khi bất đồng.','6 tuần','/khoa-hoc/vo-chong-dong-long/',True),
 ('G8','Nhà gọn, nhà an toàn','Rà soát an toàn nhà, thực đơn tuần, lịch bảo trì.','4 tuần',None,False),
 ('G9','Gia đình và cộng đồng','Ông bà, họ hàng, hàng xóm, quy tắc màn hình gia đình.','4 tuần',None,False),
]
cards = ''
for code,name,desc,dur,href,live in FAMILY:
    tag = '<span class="tag">Đang mở</span>' if live else '<span class="tag soon">Đang soạn</span>'
    inner = f'{tag}<h3>{name}</h3><p>{desc}</p><p class="small muted">{dur}</p>'
    cards += f'<a class="card" href="{href}">{inner}</a>' if href else f'<div class="card">{inner}</div>'
page('/gia-dinh/', 'Gia đình', 'Khóa học miễn phí cho bố mẹ: nuôi dạy con, giá trị gia đình, tiền, việc nhà, nhà cửa, quan hệ.',
f'''
<p class="eyebrow">Trọng tâm chính</p>
<h1>Gia đình</h1>
<p class="lead">Các khóa giúp bố mẹ có cách nghĩ, kỹ năng và công cụ để xây một gia đình có giá trị rõ, chăm chỉ, chính trực và tử tế.
Với trẻ nhỏ, bố mẹ là người hướng dẫn và đồng hành cùng con.</p>
<div class="grid">{cards}</div>
<p class="small muted">Khóa "Đang soạn" sẽ mở dần. Mỗi khóa chỉ đăng sau khi được dạy thử và có góp ý của các gia đình khác.</p>
''', current='/gia-dinh/')

# ---------------- Cá nhân ----------------
PERSONAL = [
 ('Lớn lên an toàn','Trẻ 10–14 tuổi (cùng bố mẹ)'),('Hiểu mình','Thiếu niên 13–17'),('Tự học – tự quản','Sinh viên'),
 ('Vững nghề','Học viên học nghề'),('15 phút mỗi ngày','Công nhân, lao động phổ thông'),('Tự tin – an toàn','Phụ nữ, trẻ em gái'),
 ('Tự lập từng bước','Người khuyết tật và gia đình'),('Chăm tâm trí cơ bản','Người gặp khó khăn tâm lý'),
 ('Vận động an toàn','Người yếu sức'),('Nền tảng không cần điện','Nơi thiếu điện, nước, trường học'),
]
pc = ''.join(f'<div class="card"><span class="tag soon">Đang soạn</span><h3>{n}</h3><p class="muted">{a}</p></div>' for n,a in PERSONAL)
page('/ca-nhan/', 'Cá nhân', 'Khóa tự học miễn phí theo từng đối tượng: thiếu niên, sinh viên, người lao động, người khuyết tật và nhiều nhóm khác.',
f'''
<h1>Cá nhân</h1>
<p class="lead">Khóa cho người tự học, theo từng hoàn cảnh. Các khóa này sẽ mở sau trọng tâm Gia đình.</p>
<div class="grid">{pc}</div>
<div class="box"><p>Muốn đi sâu về tinh thần (Khắc kỷ, Phật giáo, thiền và lối sống kỷ luật)? Phần chuyên sâu sẽ có ở trang chị em <strong>tamhonkhoe.com</strong>.</p></div>
{HELP_BOX}
''', current='/ca-nhan/')

# ---------------- Cần giúp ngay ----------------
page('/can-giup-ngay/', 'Cần giúp ngay', 'Số điện thoại hỗ trợ khẩn cấp tại Việt Nam: 111 bảo vệ trẻ em, 115 cấp cứu, Đường dây Ngày Mai.',
'''
<h1>Cần giúp ngay</h1>
<p class="lead">Nếu bạn hoặc người khác đang gặp nguy hiểm, hãy gọi ngay. Trang web này không thay thế bác sĩ, nhà tâm lý hay cơ quan chức năng.</p>
<div class="table-wrap"><table>
<thead><tr><th>Số</th><th>Khi nào gọi</th><th>Thời gian</th></tr></thead>
<tbody>
<tr><td><strong>115</strong></td><td>Cấp cứu y tế</td><td>24/7</td></tr>
<tr><td><strong>111</strong></td><td>Tổng đài quốc gia bảo vệ trẻ em: trẻ bị xâm hại, bạo lực, bỏ rơi hoặc cần tư vấn</td><td>24/7, miễn phí</td></tr>
<tr><td><strong>096 306 1414</strong></td><td>Đường dây nóng Ngày Mai: người đang trầm cảm, có ý nghĩ tự hại, và người thân</td><td>13:00–20:30, thứ Tư đến Chủ nhật</td></tr>
<tr><td><strong>117</strong></td><td>Tổng đài quốc gia về phòng, chống bạo lực gia đình: tư vấn, hỗ trợ, kết nối dịch vụ (vận hành từ 9/2026)</td><td>24/7</td></tr>
<tr><td><strong>112</strong></td><td>Tìm kiếm, cứu nạn</td><td>24/7</td></tr>
<tr><td><strong>113 / 114</strong></td><td>Công an / Cứu hỏa</td><td>24/7</td></tr>
</tbody></table></div>
<p class="small muted">Thông tin tra ngày 28/10/2026 từ tongdai111.vn và duongdaynongngaymai.vn. Chúng tôi kiểm tra lại mỗi quý. Nếu một số không gọi được, hãy gọi 115 hoặc đến cơ sở y tế gần nhất. Bộ Y tế đã đề xuất gộp các số khẩn cấp thành một số chung; khi có thay đổi chính thức, chúng tôi sẽ cập nhật.</p>
<h2>Trong lúc chờ</h2>
<ul>
<li>Ở cạnh người đang gặp nguy hiểm, nếu bạn an toàn.</li>
<li>Cất vật nguy hiểm ra xa: dao, thuốc, dây.</li>
<li>Nói chậm, nghe nhiều. Không cần nói đúng; chỉ cần ở đó.</li>
</ul>
''', current=None)

# ---------------- Giới thiệu ----------------
page('/gioi-thieu/', 'Giới thiệu', 'Sứ mệnh, nguyên tắc, chính sách quyền riêng tư và giấy phép của daynentang.com.',
'''
<h1>Giới thiệu</h1>
<h2>Sứ mệnh</h2>
<p>daynentang.com giúp mỗi gia đình và mỗi người tự học miễn phí bốn nền tảng làm người: năng lực, đạo đức, tinh thần, thể chất.
Mỗi bài dựa trên bằng chứng và dùng được ngay, kể cả khi không có tiền, không có thầy.</p>
<p><strong>Tầm nhìn:</strong> mọi gia đình Việt, dù nghèo hay ở xa, đều có một bộ nền tảng tin cậy để tự đứng vững và giúp người khác.</p>

<h2>Sáu nguyên tắc</h2>
<ol>
<li><strong>Bằng chứng.</strong> Mỗi bài ghi nguồn và một trong bốn nhãn: Đã xác nhận, Suy luận, Đánh giá chuyên môn, Cần kiểm chứng.</li>
<li><strong>Miễn phí thật.</strong> Không thu phí, không quảng cáo, không bán dữ liệu.</li>
<li><strong>Riêng tư cho trẻ.</strong> Không đăng tên, ảnh hay giọng nói của trẻ.</li>
<li><strong>An toàn.</strong> Mỗi bài có mục An toàn. Bài về tâm lý luôn có số đường dây nóng.</li>
<li><strong>Dễ tiếp cận.</strong> Có bản in, chữ rõ, dùng được trên điện thoại yếu và mạng chậm.</li>
<li><strong>Liêm chính.</strong> Không phóng đại hiệu quả, không dùng thương hiệu của người khác, sửa lỗi công khai.</li>
</ol>

<h2>Ai soạn bài?</h2>
<p>Người soạn là một người cha làm công việc đánh giá và đào tạo. Bài được soạn cùng trợ lý AI, kiểm chứng nguồn, rồi dạy thử với chính gia đình trước khi đăng.
Kết quả dạy thử trong một gia đình chưa phải bằng chứng khoa học; chúng tôi ghi rõ điều đó trong từng khóa.</p>

<h2 id="rieng-tu">Quyền riêng tư</h2>
<ul>
<li>Trang không dùng cookie, không có công cụ theo dõi, không có quảng cáo.</li>
<li>Trang không tải phông chữ hay mã từ bên ngoài.</li>
<li>Các công cụ trên trang (nếu có) chỉ lưu dữ liệu trên máy của bạn, không gửi đi đâu.</li>
<li>Nhà cung cấp hạ tầng (Cloudflare) có thể ghi nhật ký kỹ thuật cơ bản để vận hành và chống tấn công.</li>
</ul>

<h2 id="chia-se">Dữ liệu ở trang Chia sẻ</h2>
<ul>
<li><strong>Chúng tôi lưu:</strong> nội dung bạn viết, loại chia sẻ, bài học liên quan, chế độ hiển thị, ngày gửi; và nếu bạn tự điền: tên hiển thị, tỉnh/thành, tuổi con.</li>
<li><strong>Chúng tôi không lưu:</strong> địa chỉ IP, email, số điện thoại, tài khoản hay cookie của bạn.</li>
<li><strong>Duyệt trước khi đăng:</strong> mọi bài được người quản lý trang đọc trước. Bài có thông tin nhận diện trẻ em, quảng cáo, xúc phạm hoặc nội dung nguy hại sẽ bị sửa bỏ phần đó hoặc không đăng.</li>
<li><strong>Riêng tư:</strong> bài chọn "Riêng tư" chỉ người quản lý trang đọc, dùng để sửa bài học, không bao giờ đăng.</li>
<li><strong>Dùng để làm gì:</strong> sửa và cải thiện bài học; tổng hợp ẩn danh (ví dụ: "12 gia đình gặp khó ở bước 3") cho trang web, video và ứng dụng sau này. Không bán, không chia sẻ cho bên thứ ba.</li>
<li><strong>Lưu trữ:</strong> dữ liệu nằm trên dịch vụ cơ sở dữ liệu Cloudflare D1.</li>
<li><strong>Xin xóa bài:</strong> gửi một chia sẻ loại "Góp ý cho bài", ghi "Xin xóa bài #mã" (mã hiện ra sau khi bạn gửi). Chúng tôi xóa khi nhận được.</li>
<li>Chỉ người từ 18 tuổi được gửi chia sẻ.</li>
</ul>

<h2 id="giay-phep">Giấy phép</h2>
<p>Nội dung tự viết trên trang được chia sẻ theo giấy phép <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.vi">CC BY-NC-SA 4.0</a>:
bạn được in, chia sẻ, chỉnh sửa cho mục đích phi thương mại, ghi nguồn daynentang.com và giữ cùng giấy phép.
Tài liệu của tổ chức khác thuộc quyền của họ; chúng tôi chỉ dẫn link.</p>

<h2>Trang chị em</h2>
<ul>
<li><a href="https://tienganhcanban.com">tienganhcanban.com</a> – học tiếng Anh.</li>
<li>tamhonkhoe.com – tinh thần chuyên sâu: Khắc kỷ, Phật giáo, thiền, lối sống kỷ luật (sắp ra mắt).</li>
<li>trachnhiemxahoi.com – trách nhiệm xã hội, quyền con người, quyền lao động (sắp ra mắt).</li>
<li>hocsauhocrong.com – kiến thức học thuật (sắp ra mắt).</li>
</ul>

<h2>Nhật ký sửa đổi</h2>
<ul>
<li>28/10/2026: Mở khóa Vợ chồng đồng lòng (6 tuần, 6 bài, bản chưa dạy thử) kèm 14 hình và Sổ tay vợ chồng. Thêm Tổng đài 117 vào trang Cần giúp ngay.</li>
<li>28/10/2026: Mở khóa Gia đình có con 10–14 (7 tuần, 7 bài, bản chưa dạy thử) kèm 16 hình và Thỏa thuận gia đình.</li>
<li>28/10/2026: Mở khóa Gia đình 0–2 tuổi – Giao và Đáp (8 tuần, 8 bài, bản chưa dạy thử) kèm 18 hình và Nhật ký giao và đáp.</li>
<li>28/10/2026: Mở khóa Việc nhà chia đều (4 tuần, 8 bài, bản chưa dạy thử) kèm 18 hình và Bảng việc nhà.</li>
<li>28/10/2026: Mở khóa Tiền nhà mình (6 tuần, 12 bài, bản chưa dạy thử) kèm 26 hình, Bảng thu chi và Hũ ba ngăn.</li>
<li>28/10/2026: Mở khóa Giá trị nhà mình (4 tuần, 8 bài, bản chưa dạy thử) kèm 26 hình, Phiếu giá trị và Biên bản họp gia đình.</li>
<li>28/10/2026: Thêm bài tuần 9–12 (bản chưa dạy thử) kèm 36 hình; khóa Gia đình 2–8 đủ 12 tuần.</li>
<li>28/10/2026: Thêm bài tuần 5–8 (bản chưa dạy thử) kèm 36 hình, có sơ đồ quy trình và sơ đồ nguyên lý; thêm 3 sơ đồ ở trang khóa học.</li>
<li>28/10/2026: Thêm 36 hình minh họa tự vẽ cho 12 bài học (cùng giấy phép CC BY-NC-SA 4.0; nhân vật là con vật tự sáng tác, không dùng ảnh trẻ em).</li>
<li>28/10/2026: Thêm trang Chia sẻ (ẩn danh hoặc công khai, duyệt trước khi đăng). Thêm bài tuần 2–4 của khóa Gia đình 2–8 (bản chưa dạy thử).</li>
<li>28/10/2026: Ra mắt trang. Mở khóa Gia đình 2–8 tuổi, tuần 1.</li>
</ul>
''', current='/gioi-thieu/')
