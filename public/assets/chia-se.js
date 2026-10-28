// Trang Chia sẻ – daynentang.com. Không cookie, không lưu gì trên máy ngoài bản nháp (nếu trình duyệt cho phép).
(function () {
  var LESSONS = {
    'chung': 'Chung (không gắn bài cụ thể)',
    'g3-t1': 'Gia đình 2–8 · T1 Mình tự làm được',
    'g3-k1': 'Gia đình 2–8 · K1 Nổi hay chìm?',
    'g3-g1': 'Gia đình 2–8 · G1 Nói thật, lòng nhẹ',
    'g3-t2': 'Gia đình 2–8 · T2 Thử – sai – thử lại',
    'g3-k2': 'Gia đình 2–8 · K2 Nước: rót, đong, thấm',
    'g3-g2': 'Gia đình 2–8 · G2 Ba điều cảm ơn',
    'g3-t3': 'Gia đình 2–8 · T3 Nhìn đích rồi đi',
    'g3-k3': 'Gia đình 2–8 · K3 Hạt đậu nảy mầm',
    'g3-g3': 'Gia đình 2–8 · G3 Việc tốt bí mật',
    'g3-t4': 'Gia đình 2–8 · T4 Trước – Trong – Sau',
    'g3-k4': 'Gia đình 2–8 · K4 Mầm cao bao nhiêu?',
    'g3-g4': 'Gia đình 2–8 · G4 Dừng – Thở – Nói',
    'g3-t5': 'Gia đình 2–8 · T5 Việc quan trọng làm trước',
    'g3-k5': 'Gia đình 2–8 · K5 Ánh sáng và bóng',
    'g3-g5': 'Gia đình 2–8 · G5 Việc nhà của con',
    'g3-t6': 'Gia đình 2–8 · T6 Đèn đỏ – Đèn xanh',
    'g3-k6': 'Gia đình 2–8 · K6 Dốc và lực',
    'g3-g6': 'Gia đình 2–8 · G6 Nhận lỗi và sửa lỗi',
    'g3-t7': 'Gia đình 2–8 · T7 Gậy nói chuyện',
    'g3-k7': 'Gia đình 2–8 · K7 Túi bí ẩn',
    'g3-g7': 'Gia đình 2–8 · G7 Thám tử cảm xúc',
    'g3-t8': 'Gia đình 2–8 · T8 Anh hướng dẫn em',
    'g3-k8': 'Gia đình 2–8 · K8 Thời tiết quanh nhà',
    'g3-g8': 'Gia đình 2–8 · G8 Cảm ơn người lao động',
    'g3-t9': 'Gia đình 2–8 · T9 Chăm cây của mình',
    'g3-k9': 'Gia đình 2–8 · K9 Khủng long và hóa thạch',
    'g3-g9': 'Gia đình 2–8 · G9 Đi chậm, ăn chậm',
    'g3-t10': 'Gia đình 2–8 · T10 Góc bình tĩnh',
    'g3-k10': 'Gia đình 2–8 · K10 Thiết kế thuyền',
    'g3-g10': 'Gia đình 2–8 · G10 Giữ lời hứa nhỏ',
    'g3-t11': 'Gia đình 2–8 · T11 Chậu rau gia đình',
    'g3-k11': 'Gia đình 2–8 · K11 Con hỏi – con thử',
    'g3-g11': 'Gia đình 2–8 · G11 Tử tế với chính mình',
    'g3-t12': 'Gia đình 2–8 · T12 Lễ Bàn tay nền tảng',
    'g3-k12': 'Gia đình 2–8 · K12 Triển lãm khoa học gia đình',
    'g3-g12': 'Gia đình 2–8 · G12 Ôn giá trị và ước nguyện'
  };
  var KINDS = { 'kho-khan': 'Khó khăn', 'y-tuong': 'Ý tưởng sáng tạo', 'ket-qua': 'Kết quả', 'gop-y': 'Góp ý cho bài' };

  var $ = function (id) { return document.getElementById(id); };
  var form = $('cs-form'), list = $('cs-list'), msg = $('cs-msg'), sel = $('cs-bai'), filt = $('cs-loc');
  if (!form) return;

  Object.keys(LESSONS).forEach(function (k) {
    [sel, filt].forEach(function (s) {
      var o = document.createElement('option'); o.value = k; o.textContent = LESSONS[k]; s.appendChild(o);
    });
  });
  var allOpt = document.createElement('option'); allOpt.value = ''; allOpt.textContent = 'Tất cả bài'; filt.insertBefore(allOpt, filt.firstChild);

  var params = new URLSearchParams(location.search);
  var pre = params.get('bai');
  if (pre && LESSONS[pre]) { sel.value = pre; filt.value = pre; } else { filt.value = ''; }

  var opened = Date.now();
  function toggleName() {
    var v = (form.querySelector('input[name="visibility"]:checked') || {}).value;
    $('cs-ten-wrap').hidden = v !== 'cong-khai-ten';
  }
  form.addEventListener('change', toggleName); toggleName();

  try { var d = localStorage.getItem('dnt-nhap'); if (d) $('cs-noidung').value = d; } catch (e) {}
  $('cs-noidung').addEventListener('input', function () { try { localStorage.setItem('dnt-nhap', this.value); } catch (e) {} });

  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var key = sel.value.split('-');
    var data = {
      course: key.length > 1 ? key[0] : 'chung',
      lesson: key.length > 1 ? key[1] : 'chung',
      kind: (form.querySelector('input[name="kind"]:checked') || {}).value,
      visibility: (form.querySelector('input[name="visibility"]:checked') || {}).value,
      body: $('cs-noidung').value,
      display_name: $('cs-ten').value,
      region: $('cs-tinh').value,
      child_ages: $('cs-tuoi').value,
      dong_y: $('cs-dongy').checked,
      website: $('cs-web').value,
      t: opened
    };
    msg.className = 'box'; msg.textContent = 'Đang gửi…'; msg.hidden = false;
    fetch('/api/chia-se', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(data) })
      .then(function (r) { return r.json(); })
      .then(function (j) {
        if (j.ok) {
          msg.className = 'box';
          msg.textContent = 'Cảm ơn bạn! Bài đã được nhận' + (j.id ? ' (mã #' + j.id + ')' : '') +
            '. Bài sẽ được đọc và duyệt trước khi hiện lên trang. Bài riêng tư chỉ nhóm soạn bài đọc.';
          form.reset(); toggleName(); opened = Date.now();
          try { localStorage.removeItem('dnt-nhap'); } catch (e) {}
        } else {
          msg.className = 'box warn'; msg.textContent = j.error || 'Chưa gửi được. Vui lòng thử lại.';
        }
      })
      .catch(function () { msg.className = 'box warn'; msg.textContent = 'Mất kết nối. Nội dung vẫn còn trong ô, bạn thử gửi lại nhé.'; });
  });

  function load() {
    var k = filt.value, q = '/api/chia-se?limit=40';
    if (k && k !== 'chung') { var p = k.split('-'); q += '&course=' + p[0] + '&lesson=' + p[1]; }
    else if (k === 'chung') { q += '&course=chung'; }
    list.textContent = 'Đang tải…';
    fetch(q).then(function (r) { return r.json(); }).then(function (j) {
      list.textContent = '';
      if (!j.ok || !j.posts.length) { var p0 = document.createElement('p'); p0.className = 'muted'; p0.textContent = 'Chưa có chia sẻ nào được duyệt cho mục này. Bạn có thể là người đầu tiên.'; list.appendChild(p0); return; }
      j.posts.forEach(function (x) {
        var c = document.createElement('article'); c.className = 'card post';
        var h = document.createElement('p'); h.className = 'small muted';
        var lk = x.course === 'chung' ? 'chung' : x.course + '-' + x.lesson;
        h.textContent = (KINDS[x.kind] || '') + ' · ' + (LESSONS[lk] || 'Chung') + ' · ' + x.ngay;
        var b = document.createElement('p'); b.className = 'post-body'; b.textContent = x.body;
        var f = document.createElement('p'); f.className = 'small';
        var who = x.ten ? x.ten : 'Ẩn danh';
        if (x.region) who += ' · ' + x.region;
        if (x.child_ages) who += ' · con ' + x.child_ages + ' tuổi';
        f.textContent = '— ' + who;
        c.appendChild(h); c.appendChild(b); c.appendChild(f);
        if (x.reply) { var r = document.createElement('p'); r.className = 'reply'; r.textContent = 'Nhóm soạn bài: ' + x.reply; c.appendChild(r); }
        list.appendChild(c);
      });
    }).catch(function () { list.textContent = 'Không tải được. Vui lòng thử lại sau.'; });
  }
  filt.addEventListener('change', load); load();
})();
