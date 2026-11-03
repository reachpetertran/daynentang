import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public'))
SITE = 'https://daynentang.com'
UPDATED = '28/10/2026'
UPDATED_EN = '3 November 2026'

NAV = [
    ('/', 'Trang chủ'),
    ('/gia-dinh/', 'Gia đình'),
    ('/ca-nhan/', 'Cá nhân'),
    ('/cong-cu/', 'Công cụ'),
    ('/chia-se/', 'Chia sẻ'),
    ('/gioi-thieu/', 'Giới thiệu'),
]
NAV_EN = [
    ('/en/', 'Home'),
    ('/en/family/', 'Family'),
    ('/en/personal/', 'Personal'),
    ('/en/about/', 'About'),
    ('/en/evidence/', 'Evidence'),
]

# Trang tiếng Việt -> bản tiếng Anh tương ứng (hreflang, nút chuyển ngôn ngữ)
EN_PAGES = {
    '/': '/en/',
    '/gia-dinh/': '/en/family/',
    '/ca-nhan/': '/en/personal/',
    '/gioi-thieu/': '/en/about/',
    '/can-giup-ngay/': '/en/get-help/',
    '/bang-chung/': '/en/evidence/',
    '/khoa-hoc/gia-dinh-2-8/': '/en/courses/family-2-8/',
    '/khoa-hoc/gia-dinh-2-8/tuan-1/t1-minh-tu-lam-duoc/': '/en/courses/family-2-8/week-1/t1-i-can-do-it-myself/',
    '/khoa-hoc/gia-dinh-2-8/tuan-1/k1-noi-hay-chim/': '/en/courses/family-2-8/week-1/k1-float-or-sink/',
    '/khoa-hoc/gia-dinh-2-8/tuan-1/g1-noi-that-long-nhe/': '/en/courses/family-2-8/week-1/g1-honest-and-light/',
}
VI_PAGES = {v: k for k, v in EN_PAGES.items()}

# Dải gợi ý ngôn ngữ (không bao giờ tự chuyển trang):
# - Đã chọn Tiếng Việt -> không hiện. Đã chọn English -> hiện.
# - Trình duyệt dùng tiếng Việt -> không hiện.
# - Còn lại: hỏi /api/vung (Cloudflare cho biết có phải truy cập từ Việt Nam không).
#   Chỉ hiện khi truy cập từ NGOÀI Việt Nam. Lỗi hoặc không rõ -> không hiện (giữ tiếng Việt).
# Lựa chọn lưu trên máy người dùng (localStorage), không gửi đi đâu.
LANG_JS = '''(function(){
  var k='dnt-lang', box=document.getElementById('lang-hint');
  function save(v){try{localStorage.setItem(k,v)}catch(e){}}
  document.querySelectorAll('[data-lang-set]').forEach(function(a){
    a.addEventListener('click',function(){save(a.getAttribute('data-lang-set'))});
  });
  if(!box) return;
  function show(){
    box.hidden=false;
    var stay=document.getElementById('lang-stay');
    if(stay) stay.addEventListener('click',function(){save('vi');box.hidden=true});
  }
  var saved=null; try{saved=localStorage.getItem(k)}catch(e){}
  if(saved==='vi') return;
  if(saved==='en') return show();
  var langs=navigator.languages||[navigator.language||''];
  if(langs.some(function(l){return String(l).toLowerCase().indexOf('vi')===0})) return;
  if(!window.fetch) return;
  fetch('/api/vung',{cache:'no-store'}).then(function(r){return r.ok?r.json():null})
    .then(function(d){if(d&&d.vn===false) show();}).catch(function(){});
})();
'''
os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
with open(os.path.join(ROOT, 'assets', 'lang.js'), 'w', encoding='utf-8') as _f:
    _f.write('// Gợi ý ngôn ngữ – lưu lựa chọn trên máy người dùng, không gửi đi đâu\n' + LANG_JS)
LANG_SCRIPT = '<script src="/assets/lang.js" defer></script>'

def _hint(path):
    en = EN_PAGES.get(path)
    if en:
        msg = (f'This page is in Vietnamese. <a href="{en}" hreflang="en" data-lang-set="en">Read it in English</a>')
    else:
        msg = ('This page is in Vietnamese and has no English version yet. '
               'Use your browser’s Translate option, or <a href="/en/" hreflang="en" data-lang-set="en">start at our English pages</a>')
    return (f'<div class="lang-hint no-print" id="lang-hint" lang="en" hidden><div class="wrap"><p>{msg}. '
            f'<button type="button" class="linkish" id="lang-stay">Stay in Vietnamese</button></p></div></div>')

def page(path, title, desc, body, current=None, lang='vi'):
    en = lang == 'en'
    cur = ' aria-current="page"'
    nav_items = NAV_EN if en else NAV
    nav = ''.join(
        f'<a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in nav_items)
    if en:
        vi_path = VI_PAGES.get(path, '/')
        nav += f'<a class="lang" href="{vi_path}" hreflang="vi" lang="vi" data-lang-set="vi">Tiếng Việt</a>'
        nav += '<a class="help" href="/en/get-help/">Get help now</a>'
    else:
        if path in EN_PAGES:
            nav += f'<a class="lang" href="{EN_PAGES[path]}" hreflang="en" lang="en" data-lang-set="en">English</a>'
        nav += '<a class="help" href="/can-giup-ngay/">Cần giúp ngay</a>'
    full_title = title if title.endswith('daynentang.com') else f'{title} – daynentang.com'
    # hreflang
    alt = ''
    pair = (VI_PAGES.get(path), path) if en else (path, EN_PAGES.get(path))
    if pair[0] and pair[1]:
        alt = (f'<link rel="alternate" hreflang="vi" href="{SITE}{pair[0]}">\n'
               f'<link rel="alternate" hreflang="en" href="{SITE}{pair[1]}">\n'
               f'<link rel="alternate" hreflang="x-default" href="{SITE}{pair[0]}">\n')
    hint = '' if en or path == '/404.html' else _hint(path)
    if en:
        skip, navlab, foot = 'Skip to content', 'Main navigation', f'''<div class="cols">
      <div>
        <p><strong>daynentang.com</strong> – foundations for life, free self-study.</p>
        <p>No ads. No cookies. No user tracking.</p>
      </div>
      <div>
        <p><a href="/en/get-help/">Get help now</a> · <a href="/en/evidence/">Evidence &amp; sources</a></p>
        <p><a href="/en/about/#privacy">Privacy</a> · <a href="/en/about/#licence">Licence</a></p>
      </div>
      <div>
        <p>Translated from Vietnamese. If the two versions differ, the Vietnamese page is the reference.</p>
        <p>Updated: {UPDATED_EN}</p>
      </div>
    </div>'''
    else:
        skip, navlab, foot = 'Bỏ qua, đến nội dung', 'Điều hướng chính', f'''<div class="cols">
      <div>
        <p><strong>daynentang.com</strong> – nền tảng làm người, tự học miễn phí.</p>
        <p>Không quảng cáo. Không cookie. Không theo dõi người dùng.</p>
      </div>
      <div>
        <p><a href="/can-giup-ngay/">Cần giúp ngay</a> · <a href="/bang-chung/">Bằng chứng &amp; nguồn</a></p>
        <p><a href="/gioi-thieu/#rieng-tu">Quyền riêng tư</a> · <a href="/gioi-thieu/#giay-phep">Giấy phép</a></p>
      </div>
      <div>
        <p>Trang chị em: <a href="https://tienganhcanban.com">tienganhcanban.com</a></p>
        <p>Cập nhật: {UPDATED}</p>
      </div>
    </div>'''
    html = f'''<!doctype html>
<html lang="{'en' if en else 'vi'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
{alt}<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#1b2a41">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/logo/daynentang-logo-1024.png">
<meta property="og:locale" content="{'en_US' if en else 'vi_VN'}">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#noi-dung">{skip}</a>
{hint}
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="{'/en/' if en else '/'}"><img src="/assets/logo/daynentang-icon.svg" alt="" width="40" height="40">daynentang.com</a>
    <nav class="nav" aria-label="{navlab}">{nav}</nav>
  </div>
</header>
<main id="noi-dung"><div class="wrap">
{body}
</div></main>
<footer class="site-foot">
  <div class="wrap">
    {foot}
  </div>
</footer>
{LANG_SCRIPT}
</body>
</html>
'''
    out = os.path.join(ROOT, path.lstrip('/'))
    if out.endswith('/'):
        out = os.path.join(out, 'index.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    return out

PRINT_ROW = '''<div class="print-row no-print">
  <button class="btn primary" type="button" onclick="window.print()">In / Lưu PDF</button>
</div>'''
PRINT_ROW_EN = '''<div class="print-row no-print">
  <button class="btn primary" type="button" onclick="window.print()">Print / Save as PDF</button>
</div>'''

HELP_BOX = '''<div class="box warn">
  <h3>Cần giúp ngay</h3>
  <p>Trẻ em gặp nguy hiểm, bị xâm hại: gọi <strong>111</strong> (miễn phí, 24/7). Cấp cứu y tế: <strong>115</strong>.
  Người đang trầm cảm hoặc người thân: <strong>096 306 1414</strong> (Đường dây Ngày Mai). <a href="/can-giup-ngay/">Xem đầy đủ</a>.</p>
</div>'''
HELP_BOX_EN = '''<div class="box warn">
  <h3>Get help now</h3>
  <p><strong>In Vietnam:</strong> child in danger or abused – call <strong>111</strong> (free, 24/7). Medical emergency – <strong>115</strong>.
  Depression or thoughts of self-harm – <strong>096 306 1414</strong> (Ngày Mai line, Vietnamese).
  <strong>Elsewhere:</strong> call your local emergency number. <a href="/en/get-help/">More help</a>.</p>
</div>'''
