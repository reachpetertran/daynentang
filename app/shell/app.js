// Khung app Dạy Nền Tảng. Mọi thứ lưu trên máy (localStorage). Không gọi mạng, không theo dõi.
(function () {
  var KEY = 'dnt.v1', D = window.DNT || { courses: [], stories: [] };
  var EN = document.documentElement.lang === 'en';
  var L = EN ? {
    save: 'Save this page', saved: 'Saved', done: 'Mark as done', isdone: 'Done ✓', read: 'Mark as read', isread: 'Read ✓',
    next: 'Next lesson', prev: 'Previous lesson', back: 'Back to course', lessonOf: 'Lesson', of: 'of', cont: 'Continue',
    notes: 'My notes', notesPh: 'What did you try? What worked? What will you change?', notesSaved: 'Saved on this phone',
    prog: 'lessons done', start: 'Start', goon: 'Continue', finished: 'Course finished. Well done.', now: 'Courses in progress',
    week: 'This week', days: 'days of learning', last: 'Continue reading', savedH: 'Saved pages', notesH: 'My notes',
    stories: 'Stories read', none: 'Nothing here yet.', wipe: 'Delete all my data on this phone', wipe2: 'Tap again to delete', noRes: 'No results.',
    gateT: 'Before you read this story', gateB: 'This story is in the orange part, for readers aged 15 and over. It deals with accidents at work, human trafficking or mental distress. Do not read it to young children.', gateOk: 'I understand, continue', gateNo: 'Go back', dn: ['M', 'T', 'W', 'T', 'F', 'S', 'S']
  } : {
    save: 'Lưu bài này', saved: 'Đã lưu', done: 'Đánh dấu đã học xong', isdone: 'Đã học xong ✓', read: 'Đánh dấu đã đọc', isread: 'Đã đọc ✓',
    next: 'Bài tiếp theo', prev: 'Bài trước', back: 'Về trang khóa', lessonOf: 'Bài', of: 'trên', cont: 'Đọc tiếp',
    notes: 'Ghi chú của tôi', notesPh: 'Nhà mình đã thử gì? Điều gì được? Lần sau sửa gì?', notesSaved: 'Đã lưu trên máy này',
    prog: 'bài đã xong', start: 'Bắt đầu', goon: 'Học tiếp', finished: 'Bạn đã học xong khóa này.', now: 'Khóa đang học',
    week: 'Tuần này', days: 'ngày có học', last: 'Đọc tiếp', savedH: 'Bài đã lưu', notesH: 'Ghi chú của tôi',
    stories: 'Truyện đã đọc', none: 'Chưa có gì ở đây.', wipe: 'Xóa mọi dữ liệu của tôi trên máy này', wipe2: 'Bấm lần nữa để xóa', noRes: 'Không tìm thấy.',
    gateT: 'Trước khi đọc truyện này', gateB: 'Truyện thuộc phần cam, dành cho người từ 15 tuổi. Truyện nói về tai nạn lao động, mua bán người hoặc khó khăn tâm lý. Không đọc cho trẻ nhỏ.',
    gateOk: 'Tôi hiểu, đọc tiếp', gateNo: 'Quay lại', dn: ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
  };

  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) {} }
  var st = load();
  ['saved', 'done', 'notes', 'days', 'gate'].forEach(function (k) { st[k] = st[k] || {}; });
  function $(id) { return document.getElementById(id); }
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function href(p) { return p + 'index.html'; }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function today(d) { d = d || new Date(); return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }

  // ---------- Cỡ chữ, màu nền, ngôn ngữ ----------
  var root = document.documentElement;
  function mark(id, v) {
    var box = $(id); if (!box) return;
    [].forEach.call(box.querySelectorAll('button'), function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-v') === v ? 'true' : 'false'); });
  }
  function apply() {
    root.setAttribute('data-size', st.size || 'm');
    if (st.theme === 'light' || st.theme === 'dark') root.setAttribute('data-theme', st.theme); else root.removeAttribute('data-theme');
    mark('app-size', st.size || 'm'); mark('app-theme', st.theme || 'auto');
  }
  function bind(id, prop) {
    var box = $(id); if (!box) return;
    box.addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; st[prop] = b.getAttribute('data-v'); save(); apply(); });
  }
  apply(); bind('app-size', 'size'); bind('app-theme', 'theme');
  var aa = $('app-aa'), panel = $('app-panel');
  if (aa && panel) {
    aa.addEventListener('click', function () { panel.hidden = !panel.hidden; aa.setAttribute('aria-expanded', String(!panel.hidden)); });
    document.addEventListener('click', function (e) { if (!panel.hidden && !panel.contains(e.target) && e.target !== aa) { panel.hidden = true; aa.setAttribute('aria-expanded', 'false'); } });
  }
  var lg = $('app-lang');
  if (lg) lg.addEventListener('click', function (e) { var a = e.target.closest('a'); if (a) { st.lang = a.getAttribute('data-v'); save(); } });

  var path = location.pathname.replace(/index\.html$/, '');
  // Mở app lần sau: vào đúng ngôn ngữ đã chọn
  if (path === '/' && st.lang === 'en' && !sessionStorage.getItem('dnt.go')) { sessionStorage.setItem('dnt.go', '1'); location.replace('/en/index.html'); return; }
  try { sessionStorage.setItem('dnt.go', '1'); } catch (e) {}

  // ---------- Danh mục ----------
  var course = null, idx = -1, story = null;
  var SL = D.stories.filter(function (s) { return (s[4] || 'vi') === (EN ? 'en' : 'vi'); });
  D.courses.forEach(function (c) {
    if (c.p === path) course = c;
    c.l.forEach(function (l, i) { if (l[0] === path) { course = c; idx = i; } });
  });
  D.stories.forEach(function (s) { if (s[0] === path) story = s; });
  function count(c) { var n = 0; c.l.forEach(function (l) { if (st.done[l[0]]) n++; }); return n; }
  function nextOf(c) { for (var i = 0; i < c.l.length; i++) if (!st.done[c.l[i][0]]) return c.l[i]; return null; }
  function bar(n, total) { return '<span class="app-bar" role="img" aria-label="' + n + '/' + total + '"><i style="width:' + (total ? Math.round(n / total * 100) : 0) + '%"></i></span>'; }
  function courseCard(c) {
    var n = count(c), nx = nextOf(c);
    return '<a class="app-course" href="' + href(nx ? nx[0] : c.p) + '"><strong>' + esc(c.t) + '</strong>' + bar(n, c.l.length) +
      '<small>' + n + '/' + c.l.length + ' ' + L.prog + (nx ? ' · ' + L.goon + ': ' + esc(nx[1]) : ' · ' + L.finished) + '</small></a>';
  }
  function active() { return D.courses.filter(function (c) { var n = count(c); return n > 0 && n < c.l.length; }); }

  var h1 = document.querySelector('h1');
  var title = h1 ? h1.textContent.trim() : document.title;
  var wrap = document.querySelector('main .wrap') || document.querySelector('main');
  var isRead = idx >= 0 || !!story;

  // ---------- Cổng cảnh báo cho truyện phần cam ----------
  if (story && story[2] === 'cam' && !st.gate[path]) {
    var g = el('div', 'app-gate', '<div role="dialog" aria-modal="true" aria-labelledby="app-gate-t"><h2 id="app-gate-t">' + L.gateT + '</h2><p>' + L.gateB +
      '</p><button type="button" class="btn primary" id="app-gate-ok">' + L.gateOk + '</button> <a class="btn" href="' + (EN ? '/en/stories/index.html' : '/truyen/index.html') + '">' + L.gateNo + '</a></div>');
    document.body.appendChild(g);
    $('app-gate-ok').addEventListener('click', function () { st.gate[path] = 1; save(); g.remove(); });
  }

  // ---------- Bài học và truyện ----------
  if (isRead && wrap) {
    st.days[today()] = 1;
    st.last = { p: path, t: title, y: (st.last && st.last.p === path) ? st.last.y : 0 }; save();
    if (st.last.y > 200) requestAnimationFrame(function () { window.scrollTo(0, st.last.y); });
    var tick = null;
    window.addEventListener('scroll', function () {
      if (tick) return;
      tick = setTimeout(function () { tick = null; st.last.y = Math.round(window.scrollY); save(); }, 800);
    }, { passive: true });

    if (idx >= 0) {
      var crumb = el('a', 'app-crumb no-print', '<small>' + esc(course.t) + ' · ' + L.lessonOf + ' ' + (idx + 1) + ' ' + L.of + ' ' + course.l.length + '</small>' + bar(count(course), course.l.length));
      crumb.href = href(course.p); wrap.insertBefore(crumb, wrap.firstChild);
    }

    var box = el('section', 'app-tools no-print');
    box.innerHTML = '<label class="app-notes"><strong>' + L.notes + '</strong><textarea id="app-note" rows="4" placeholder="' + L.notesPh + '"></textarea>' +
      '<small class="muted" id="app-note-s" aria-live="polite"></small></label>' +
      '<div class="app-actions"><button type="button" id="app-save"></button><button type="button" id="app-done-btn"></button></div><div class="app-nav" id="app-nav"></div>';
    wrap.appendChild(box);
    var ta = $('app-note'), ts = $('app-note-s'), nt = null;
    ta.value = (st.notes[path] && st.notes[path].x) || '';
    ta.addEventListener('input', function () {
      clearTimeout(nt);
      nt = setTimeout(function () { if (ta.value.trim()) st.notes[path] = { t: title, x: ta.value }; else delete st.notes[path]; save(); ts.textContent = L.notesSaved; }, 500);
    });
    var bs = $('app-save'), bd = $('app-done-btn'), nav = $('app-nav');
    var paint = function () {
      var s = !!st.saved[path], d = !!st.done[path];
      bs.textContent = s ? L.saved : L.save; bs.setAttribute('aria-pressed', s);
      bd.textContent = d ? (story ? L.isread : L.isdone) : (story ? L.read : L.done); bd.setAttribute('aria-pressed', d);
      var h = '';
      if (idx > 0) h += '<a class="btn" href="' + href(course.l[idx - 1][0]) + '">← ' + L.prev + '</a>';
      if (idx >= 0 && idx < course.l.length - 1) h += '<a class="btn primary" href="' + href(course.l[idx + 1][0]) + '">' + L.next + ': ' + esc(course.l[idx + 1][1]) + ' →</a>';
      else if (idx >= 0) h += '<a class="btn primary" href="' + href(course.p) + '">' + L.back + '</a>';
      if (story) {
        var i = SL.indexOf(story);
        if (i >= 0 && SL[i + 1]) h += '<a class="btn primary" href="' + href(SL[i + 1][0]) + '">' + esc(SL[i + 1][1]) + ' →</a>';
      }
      nav.innerHTML = h;
    };
    bs.addEventListener('click', function () { if (st.saved[path]) delete st.saved[path]; else st.saved[path] = title; save(); paint(); });
    bd.addEventListener('click', function () { if (st.done[path]) delete st.done[path]; else st.done[path] = title; save(); paint(); });
    paint();
  }

  // ---------- Trang khóa: thanh tiến độ và nút học tiếp ----------
  if (course && idx < 0 && wrap && course.l.length) {
    var n = count(course), nx = nextOf(course);
    var card = el('div', 'app-progress no-print', '<strong>' + n + '/' + course.l.length + ' ' + L.prog + '</strong>' + bar(n, course.l.length) +
      (nx ? '<a class="btn primary" href="' + href(nx[0]) + '">' + (n ? L.goon : L.start) + ': ' + esc(nx[1]) + '</a>' : '<p>' + L.finished + '</p>'));
    var lead = wrap.querySelector('.lead');
    if (lead && lead.nextSibling) wrap.insertBefore(card, lead.nextSibling); else wrap.insertBefore(card, wrap.firstChild);
  }

  // ---------- Trang chủ ----------
  if ((path === '/' || path === '/en/') && wrap) {
    var top = el('div', 'no-print');
    if (st.last) top.innerHTML += '<a class="app-continue" href="' + href(st.last.p) + '"><small>' + L.cont + '</small><strong>' + esc(st.last.t) + '</strong></a>';
    active().slice(0, 3).forEach(function (c) { top.innerHTML += courseCard(c); });
    if (top.innerHTML) wrap.insertBefore(top, wrap.firstChild);
  }

  // ---------- Tab Khóa học: khóa đang học và tìm kiếm ----------
  var now = $('app-courses-now');
  if (now) { var ac = active(); if (ac.length) now.innerHTML = '<h2>' + L.now + '</h2>' + ac.map(courseCard).join(''); }
  var q = $('app-q'), res = $('app-results');
  if (q && res) {
    var norm = function (s) { return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd'); };
    var items = [];
    D.courses.forEach(function (c) {
      if (c.g === 'E') return;
      items.push([c.p, c.t, 'Khóa', norm(c.t)]);
      c.l.forEach(function (l) { items.push([l[0], l[1], c.t, norm(l[1] + ' ' + c.t)]); });
    });
    SL.forEach(function (s) { items.push([s[0], s[1], 'Truyện', norm(s[1])]); });
    q.addEventListener('input', function () {
      var words = norm(q.value).split(/\s+/).filter(Boolean);
      if (!words.length) { res.innerHTML = ''; return; }
      var hit = items.filter(function (it) { return words.every(function (w) { return it[3].indexOf(w) >= 0; }); }).slice(0, 30);
      res.innerHTML = hit.length ? hit.map(function (it) { return '<a href="' + href(it[0]) + '"><small>' + esc(it[2]) + '</small>' + esc(it[1]) + '</a>'; }).join('') : '<p class="muted">' + L.noRes + '</p>';
    });
  }

  // ---------- Tab Truyện ----------
  var sp = $('app-story-progress');
  if (sp) { var r = SL.filter(function (s) { return st.done[s[0]]; }).length; if (r) sp.innerHTML = '<div class="app-progress"><strong>' + L.stories + ': ' + r + '/' + SL.length + '</strong>' + bar(r, SL.length) + '</div>'; }

  // ---------- Tab Của tôi ----------
  var mine = $('app-mine');
  if (mine) {
    var h = '', d = new Date(), dow = (d.getDay() + 6) % 7, got = 0, dots = '';
    for (var i = 0; i < 7; i++) {
      var x = new Date(d); x.setDate(d.getDate() - dow + i);
      var on = !!st.days[today(x)]; if (on) got++;
      dots += '<span class="' + (on ? 'on' : '') + (i === dow ? ' today' : '') + '"><i></i>' + L.dn[i] + '</span>';
    }
    h += '<h2>' + L.week + '</h2><div class="app-week" role="img" aria-label="' + got + ' ' + L.days + '">' + dots + '</div><p class="small muted">' + got + ' ' + L.days + '</p>';
    if (st.last) h += '<h2>' + L.last + '</h2><a class="app-continue" href="' + href(st.last.p) + '"><strong>' + esc(st.last.t) + '</strong></a>';
    var all = D.courses.filter(function (c) { return count(c) > 0; });
    h += '<h2>' + L.now + '</h2>' + (all.length ? all.map(courseCard).join('') : '<p class="muted">' + L.none + '</p>');
    var rs = SL.filter(function (s) { return st.done[s[0]]; }).length;
    if (SL.length) h += '<h2>' + L.stories + '</h2><a class="app-course" href="' + (EN ? '/en/stories/index.html' : '/truyen/index.html') + '"><strong>' + rs + '/' + SL.length + '</strong>' + bar(rs, SL.length) + '</a>';
    var sk = Object.keys(st.saved);
    h += '<h2>' + L.savedH + '</h2>' + (sk.length ? '<div class="app-list">' + sk.map(function (k) { return '<a href="' + href(k) + '">' + esc(st.saved[k]) + '</a>'; }).join('') + '</div>' : '<p class="muted">' + L.none + '</p>');
    var nk = Object.keys(st.notes);
    h += '<h2>' + L.notesH + '</h2>' + (nk.length ? '<div class="app-list">' + nk.map(function (k) { return '<a href="' + href(k) + '"><small>' + esc(st.notes[k].t) + '</small>' + esc(st.notes[k].x.slice(0, 140)) + '</a>'; }).join('') + '</div>' : '<p class="muted">' + L.none + '</p>');
    h += '<p><button type="button" class="linkish app-wipe" id="app-wipe">' + L.wipe + '</button></p>';
    mine.innerHTML = h;
    var wb = $('app-wipe'), armed = false;
    wb.addEventListener('click', function () {
      if (!armed) { armed = true; wb.textContent = L.wipe2; return; }
      try { localStorage.removeItem(KEY); } catch (e) {} location.reload();
    });
  }

  // ---------- Dấu ✓ cạnh link tới bài, truyện đã xong ----------
  [].forEach.call(document.querySelectorAll('main a[href]'), function (x) {
    if (x.closest('.app-tools,.app-continue,.app-course,.app-list,.app-crumb,.app-progress')) return;
    var p = x.pathname.replace(/index\.html$/, '');
    if (st.done[p] && p !== path) { var t = x.querySelector('h3,strong') || x; t.insertAdjacentHTML('beforeend', ' <span class="app-tick" aria-label="✓">✓</span>'); }
  });
})();
