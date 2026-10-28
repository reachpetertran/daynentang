import os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'public'))
SITE = 'https://daynentang.com'
UPDATED = '28/10/2026'

NAV = [
    ('/', 'Trang chủ'),
    ('/gia-dinh/', 'Gia đình'),
    ('/ca-nhan/', 'Cá nhân'),
    ('/cong-cu/', 'Công cụ'),
    ('/chia-se/', 'Chia sẻ'),
    ('/gioi-thieu/', 'Giới thiệu'),
]

def page(path, title, desc, body, current=None):
    cur = ' aria-current="page"'
    nav = ''.join(
        f'<a href="{h}"{cur if h == current else ""}>{t}</a>' for h, t in NAV)
    nav += '<a class="help" href="/can-giup-ngay/">Cần giúp ngay</a>'
    full_title = title if title.endswith('daynentang.com') else f'{title} – daynentang.com'
    html = f'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}{path}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#1b2a41">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE}/assets/logo/daynentang-logo-1024.png">
<meta property="og:locale" content="vi_VN">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<a class="skip" href="#noi-dung">Bỏ qua, đến nội dung</a>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="/"><img src="/assets/logo/daynentang-icon.svg" alt="" width="40" height="40">daynentang.com</a>
    <nav class="nav" aria-label="Điều hướng chính">{nav}</nav>
  </div>
</header>
<main id="noi-dung"><div class="wrap">
{body}
</div></main>
<footer class="site-foot">
  <div class="wrap">
    <div class="cols">
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
    </div>
  </div>
</footer>
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

HELP_BOX = '''<div class="box warn">
  <h3>Cần giúp ngay</h3>
  <p>Trẻ em gặp nguy hiểm, bị xâm hại: gọi <strong>111</strong> (miễn phí, 24/7). Cấp cứu y tế: <strong>115</strong>.
  Người đang trầm cảm hoặc người thân: <strong>096 306 1414</strong> (Đường dây Ngày Mai). <a href="/can-giup-ngay/">Xem đầy đủ</a>.</p>
</div>'''
