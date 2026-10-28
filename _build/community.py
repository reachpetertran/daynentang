from common import page

page('/chia-se/', 'Chia sẻ khi thực hành',
 'Chia sẻ khó khăn, ý tưởng sáng tạo và kết quả khi thực hành bài học. Ẩn danh hoặc công khai, tùy bạn.',
'''
<p class="eyebrow">Cộng đồng người học</p>
<h1>Chia sẻ khi thực hành</h1>
<p class="lead">Bạn gặp khó khăn gì, nghĩ ra cách hay nào, con phản ứng ra sao? Mỗi chia sẻ giúp bài học sát đời sống hơn.
Khi đủ nhiều chia sẻ, chúng tôi sửa bài dựa trên những gì các gia đình thật sự gặp.</p>

<div class="two">
  <div class="card"><h3>Bạn chọn cách hiện</h3><p>Công khai kèm tên hiển thị, công khai ẩn danh, hoặc riêng tư chỉ gửi nhóm soạn bài.</p></div>
  <div class="card"><h3>Mọi bài đều được đọc trước</h3><p>Bài chỉ hiện lên trang sau khi được duyệt. Thông tin nhận diện trẻ em sẽ bị xóa.</p></div>
</div>

<h2 id="gui">Gửi chia sẻ</h2>
<form id="cs-form" class="cs-form" novalidate>
  <label for="cs-bai">Bài học liên quan</label>
  <select id="cs-bai" name="bai"></select>

  <fieldset><legend>Bạn muốn chia sẻ điều gì?</legend>
    <label class="opt"><input type="radio" name="kind" value="kho-khan" checked> Khó khăn khi thực hành</label>
    <label class="opt"><input type="radio" name="kind" value="y-tuong"> Ý tưởng sáng tạo, cách làm khác</label>
    <label class="opt"><input type="radio" name="kind" value="ket-qua"> Kết quả, điều con làm được</label>
    <label class="opt"><input type="radio" name="kind" value="gop-y"> Góp ý cho bài (sai sót, khó hiểu)</label>
  </fieldset>

  <label for="cs-noidung">Nội dung</label>
  <textarea id="cs-noidung" rows="7" maxlength="3000" placeholder="Ví dụ: Con nhỏ không chịu cất đồ chơi khi hát. Mình thử biến thành trò thi xe tải chở đồ thì con làm ngay."></textarea>
  <p class="small muted">Xin đừng ghi tên thật, trường, địa chỉ, số điện thoại hay ảnh của trẻ.</p>

  <div class="two">
    <div><label for="cs-tuoi">Tuổi con (không bắt buộc)</label><input id="cs-tuoi" type="text" inputmode="numeric" maxlength="20" placeholder="Ví dụ: 2, 7"></div>
    <div><label for="cs-tinh">Tỉnh/thành (không bắt buộc)</label><input id="cs-tinh" type="text" maxlength="40" placeholder="Ví dụ: Đồng Nai"></div>
  </div>

  <fieldset><legend>Hiển thị thế nào?</legend>
    <label class="opt"><input type="radio" name="visibility" value="cong-khai-an-danh" checked> Công khai, <strong>ẩn danh</strong></label>
    <label class="opt"><input type="radio" name="visibility" value="cong-khai-ten"> Công khai, kèm <strong>tên hiển thị</strong> (có thể là biệt danh)</label>
    <label class="opt"><input type="radio" name="visibility" value="rieng-tu"> <strong>Riêng tư</strong>: chỉ nhóm soạn bài đọc, không đăng</label>
  </fieldset>
  <div id="cs-ten-wrap" hidden><label for="cs-ten">Tên hiển thị</label><input id="cs-ten" type="text" maxlength="40" placeholder="Ví dụ: Bố Bin"></div>

  <div class="hp" aria-hidden="true"><label for="cs-web">Để trống ô này</label><input id="cs-web" type="text" tabindex="-1" autocomplete="off"></div>

  <label class="opt consent"><input id="cs-dongy" type="checkbox"> Tôi từ 18 tuổi. Tôi đồng ý để daynentang.com lưu nội dung này và, nếu tôi chọn công khai, đăng lên trang sau khi duyệt.
  Tôi đã đọc <a href="/gioi-thieu/#chia-se">cách xử lý dữ liệu</a>.</label>

  <button class="btn primary" type="submit">Gửi chia sẻ</button>
  <div id="cs-msg" class="box" role="status" hidden></div>
</form>

<div class="box warn small"><p>Trang này không dành cho tình huống khẩn cấp. Nếu trẻ hoặc người lớn đang gặp nguy hiểm, gọi <strong>111</strong> (bảo vệ trẻ em) hoặc <strong>115</strong> (cấp cứu). <a href="/can-giup-ngay/">Xem thêm số hỗ trợ</a>.</p></div>

<h2>Chia sẻ đã duyệt</h2>
<label for="cs-loc">Lọc theo bài</label>
<select id="cs-loc"></select>
<div id="cs-list" class="cs-list" aria-live="polite"></div>
<script src="/assets/chia-se.js" defer></script>
''', current='/chia-se/')
