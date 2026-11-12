// Khung app Dạy Nền Tảng. Mọi thứ lưu trên máy (localStorage). Không gọi mạng, không theo dõi.
(function () {
  var KEY = 'dnt.v1';
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function save(s) { try { localStorage.setItem(KEY, JSON.stringify(s)); } catch (e) {} }
  var st = load();
  st.saved = st.saved || {}; st.done = st.done || {};

  // Cỡ chữ và màu nền
  var root = document.documentElement;
  function apply() {
    root.setAttribute('data-size', st.size || 'm');
    if (st.theme === 'light' || st.theme === 'dark') root.setAttribute('data-theme', st.theme);
    else root.removeAttribute('data-theme');
    mark('app-size', st.size || 'm'); mark('app-theme', st.theme || 'auto');
  }
  function mark(id, v) {
    var box = document.getElementById(id); if (!box) return;
    [].forEach.call(box.querySelectorAll('button'), function (b) {
      b.setAttribute('aria-pressed', b.getAttribute('data-v') === v ? 'true' : 'false');
    });
  }
  function bind(id, prop) {
    var box = document.getElementById(id); if (!box) return;
    box.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      st[prop] = b.getAttribute('data-v'); save(st); apply();
    });
  }
  apply(); bind('app-size', 'size'); bind('app-theme', 'theme');
  var aa = document.getElementById('app-aa'), panel = document.getElementById('app-panel');
  if (aa && panel) {
    aa.addEventListener('click', function () { panel.hidden = !panel.hidden; });
    document.addEventListener('click', function (e) {
      if (!panel.hidden && !panel.contains(e.target) && e.target !== aa) panel.hidden = true;
    });
  }

  var path = location.pathname.replace(/index\.html$/, '');
  var h1 = document.querySelector('h1');
  var title = h1 ? h1.textContent.trim() : document.title;
  var isLesson = /^\/khoa-hoc\/[^/]+\/.+/.test(path) || /^\/truyen\/[^/]+\/.+/.test(path) || /^\/truyen\/[^/]+\/$/.test(path);

  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function link(p, t) { return '<a href="' + p + 'index.html">' + esc(t) + '</a>'; }

  // Bài học và truyện: nhớ chỗ đang đọc, nút Lưu, nút Đã học xong
  if (isLesson) {
    st.last = { p: path, t: title, y: (st.last && st.last.p === path) ? st.last.y : 0 }; save(st);
    if (st.last.y > 200) setTimeout(function () { window.scrollTo(0, st.last.y); }, 60);
    var tick = null;
    window.addEventListener('scroll', function () {
      if (tick) return;
      tick = setTimeout(function () { tick = null; st.last.y = Math.round(window.scrollY); save(st); }, 800);
    }, { passive: true });

    var wrap = document.querySelector('main .wrap') || document.querySelector('main');
    if (wrap) {
      var box = document.createElement('div'); box.className = 'app-actions no-print';
      box.innerHTML = '<button type="button" id="app-save"></button><button type="button" id="app-done-btn"></button>';
      wrap.appendChild(box);
      var bs = document.getElementById('app-save'), bd = document.getElementById('app-done-btn');
      var paint = function () {
        var s = !!st.saved[path], d = !!st.done[path];
        bs.textContent = s ? 'Đã lưu bài này' : 'Lưu bài này'; bs.setAttribute('aria-pressed', s);
        bd.textContent = d ? 'Đã học xong' : 'Đánh dấu đã học xong'; bd.setAttribute('aria-pressed', d);
      };
      bs.addEventListener('click', function () { if (st.saved[path]) delete st.saved[path]; else st.saved[path] = title; save(st); paint(); });
      bd.addEventListener('click', function () { if (st.done[path]) delete st.done[path]; else st.done[path] = title; save(st); paint(); });
      paint();
    }
  }

  // Trang chủ: thẻ "Đọc tiếp"
  if (path === '/' && st.last) {
    var w = document.querySelector('main .wrap');
    if (w) {
      var a = document.createElement('a'); a.className = 'app-continue'; a.href = st.last.p + 'index.html';
      a.innerHTML = '<small>Đọc tiếp</small><strong>' + esc(st.last.t) + '</strong>';
      w.insertBefore(a, w.firstChild);
    }
  }

  // Trang Đã lưu
  function fill(id, map) {
    var el = document.getElementById(id); if (!el) return;
    var keys = Object.keys(map); if (!keys.length) return;
    el.className = 'app-list';
    el.innerHTML = keys.map(function (k) { return link(k, map[k]); }).join('');
  }
  if (document.getElementById('app-last') && st.last) {
    var o = {}; o[st.last.p] = st.last.t; fill('app-last', o);
  }
  fill('app-saved', st.saved); fill('app-done', st.done);

  // Đánh dấu ✓ cạnh link tới bài đã học xong
  [].forEach.call(document.querySelectorAll('main a[href]'), function (x) {
    var p = x.pathname.replace(/index\.html$/, '');
    if (st.done[p]) x.insertAdjacentHTML('beforeend', ' <span aria-label="đã học xong">✓</span>');
  });
})();
