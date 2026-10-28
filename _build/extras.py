import os
from common import page, HELP_BOX, PRINT_ROW, ROOT, SITE

# ---------- Công cụ ----------
page('/cong-cu/', 'Công cụ', 'Công cụ in miễn phí cho gia đình: bảng quan sát tiến bộ của con, bảng thói quen 7 ngày.',
'''
<h1>Công cụ</h1>
<p class="lead">Công cụ in được, dùng ngay. Không cần tài khoản, không lưu dữ liệu của bạn.</p>
<div class="grid">
<a class="card" href="/cong-cu/bang-quan-sat/"><span class="tag">Có thể in</span><h3>Bảng quan sát 0–1–2</h3><p>Theo dõi tiến bộ của con ở tuần 0, 6 và 12 của khóa Gia đình 2–8.</p></a>
<a class="card" href="/cong-cu/bang-thoi-quen/"><span class="tag">Có thể in</span><h3>Bảng thói quen 7 ngày</h3><p>Con tự đánh dấu việc mình tự làm mỗi ngày.</p></a>
<div class="card"><span class="tag soon">Đang soạn</span><h3>Bảng thu chi gia đình</h3><p>Cho khóa Tiền nhà mình.</p></div>
<div class="card"><span class="tag soon">Đang soạn</span><h3>Bảng việc nhà theo tuổi</h3><p>Cho khóa Việc nhà chia đều.</p></div>
</div>
''', current='/cong-cu/')

items = [('Ngón cái','Tự làm một việc tự phục vụ phù hợp tuổi'),('Ngón trỏ','Nói hoặc chỉ được mục tiêu trước khi làm'),
 ('Ngón giữa','Làm việc chính trước khi chơi'),('Ngón áp út','Chờ lượt; nhắc lại ý người khác'),
 ('Ngón út','Đi ngủ đúng giờ; tự dùng cách bình tĩnh'),('Khoa học','Đưa ra dự đoán; kể lại kết quả'),
 ('Trung thực','Tự nhận khi làm đổ hay làm hỏng'),('Biết ơn, tử tế','Tự nói cảm ơn; giúp người khác không cần nhắc')]
rows = ''.join(f'<tr><td><strong>{a}</strong></td><td>{b}</td><td></td><td></td><td></td></tr>' for a,b in items)
page('/cong-cu/bang-quan-sat/', 'Bảng quan sát 0–1–2', 'Bảng in để bố mẹ theo dõi tiến bộ của con trong khóa Gia đình 2–8 tuổi.',
f'''
<h1>Bảng quan sát 0–1–2</h1>
<p>Chấm cho mỗi con một bảng. <strong>0</strong> = chưa làm · <strong>1</strong> = làm khi được nhắc · <strong>2</strong> = tự làm.</p>
{PRINT_ROW}
<p>Con: ……………… (chỉ ghi trên giấy, không đăng lên mạng) &nbsp; Tuổi: ……</p>
<div class="table-wrap"><table>
<thead><tr><th>Mục</th><th>Hành vi quan sát</th><th>Tuần 0</th><th>Tuần 6</th><th>Tuần 12</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<h2>Bố mẹ tự theo dõi (đếm trong 3 ngày)</h2>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Tuần 0</th><th>Tuần 6</th><th>Tuần 12</th></tr></thead>
<tbody><tr><td>Số lần khen cụ thể mỗi ngày</td><td></td><td></td><td></td></tr>
<tr><td>Số lần la mắng mỗi ngày</td><td></td><td></td><td></td></tr></tbody></table></div>
<p class="small muted">Bảng này để tự theo dõi, không dùng để chẩn đoán. Nếu lo lắng về sự phát triển của con, hãy hỏi bác sĩ nhi.</p>
''', current='/cong-cu/')

days = ''.join(f'<th>{d}</th>' for d in ['T2','T3','T4','T5','T6','T7','CN'])
blank = '<td></td>'*7
trows = ''.join(f'<tr><td class="tall">{i}. ……………………</td>{blank}</tr>' for i in range(1,6))
page('/cong-cu/bang-thoi-quen/', 'Bảng thói quen 7 ngày', 'Bảng in cho con tự đánh dấu việc tự làm mỗi ngày trong tuần.',
f'''
<h1>Bảng thói quen 7 ngày</h1>
<p>Con viết hoặc vẽ việc mình tự làm ở cột trái. Mỗi ngày làm được thì con tự vẽ một ngôi sao hoặc dán sticker.</p>
{PRINT_ROW}
<div class="table-wrap"><table>
<thead><tr><th>Việc con tự làm</th>{days}</tr></thead>
<tbody>{trows}</tbody></table></div>
<p class="small muted">Gợi ý: bắt đầu với 1–2 việc. Thêm việc mới khi con đã làm đều 5/7 ngày.</p>
''', current='/cong-cu/')

# ---------- Bằng chứng ----------
EV = [
 ('Parenting for Lifelong Health – trẻ nhỏ: thử nghiệm ngẫu nhiên 296 người chăm sóc ở Nam Phi; hành vi nuôi dạy tích cực quan sát được +39% sau 4–5 tháng, +24% sau 17 tháng','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC7155004/','Ward et al. 2019'),
 ('Tài liệu PLH trên trang WHO dùng giấy phép CC BY-NC-ND 4.0 (không phái sinh)','Đã xác nhận','https://www.who.int/teams/social-determinants-of-health/parenting-for-lifelong-health','WHO'),
 ('Học tập cảm xúc – xã hội: phân tích gộp 424 nghiên cứu, 53 nước; chủ yếu ở trường học','Đã xác nhận','https://eric.ed.gov/?id=EJ1394000','Cipriano et al. 2023'),
 ('Truyện khen nhân vật nói thật làm trẻ 3–7 tuổi nhận lỗi nhiều hơn; truyện dọa không hiệu quả hơn','Đã xác nhận','https://pubmed.ncbi.nlm.nih.gov/24928424/','Lee et al. 2014'),
 ('Can thiệp "tư duy phát triển" có hiệu quả rất nhỏ (d ≈ 0,02–0,05)','Đã xác nhận','https://artscimedia.case.edu/wp-content/uploads/sites/141/2020/06/26110416/Macnamara-Burgoyne-2023.pdf','Macnamara & Burgoyne 2023'),
 ('Chương trình chánh niệm đại trà ở trường (MYRIAD, 8.376 học sinh) không vượt nhóm so sánh sau 1 năm','Đã xác nhận','https://www.kcl.ac.uk/news/schools-based-mindfulness-programme-improves-school-culture-and-reduces-teacher-burnout','Kuyken et al. 2022'),
 ('Hướng dẫn hoạt động chức năng điều hành theo tuổi','Đã xác nhận','https://developingchild.harvard.edu/resources/handouts-tools/activities-guide-enhancing-and-practicing-executive-function-skills/','Harvard Center on the Developing Child'),
 ('Reach Up: tài liệu theo giấy phép CC BY-NC-SA 4.0','Đã xác nhận','https://reachupandlearn.com/resources/','Reach Up'),
 ('Trẻ nhỏ có thể đuối nước chỉ với vài inch nước trong nhà; giữ trẻ trong tầm tay','Đã xác nhận','https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/','CPSC'),
 ('Bữa cơm gia đình ≥3 lần/tuần gắn với ăn uống lành mạnh hơn (tương quan, không phải nhân quả)','Đã xác nhận','https://pmc.ncbi.nlm.nih.gov/articles/PMC3387875/','Hammons & Fiese 2011'),
 ('Tổng đài 111 bảo vệ trẻ em: miễn phí, 24/7','Đã xác nhận','https://tongdai111.vn/','tongdai111.vn'),
 ('Đường dây Ngày Mai 096 306 1414: 13:00–20:30, thứ Tư đến Chủ nhật','Đã xác nhận','https://duongdaynongngaymai.vn/','duongdaynongngaymai.vn'),
 ('113 công an, 114 cứu hỏa, 115 cấp cứu; Bộ Y tế đề xuất gộp thành một số khẩn cấp, chưa có hiệu lực','Đã xác nhận (tra 28/10/2026)','https://thuvienphapluat.vn/hoi-dap-phap-luat/111-113-114-115-la-so-dien-thoai-gi-138013545.html','Thư viện Pháp luật; LuatVietnam'),
 ('Đếm điều may mắn: thử nghiệm 221 học sinh đầu tuổi thiếu niên, tăng biết ơn, lạc quan, hài lòng cuộc sống','Đã xác nhận','https://proofpositive.org/bc-science/counting-blessings-in-early-adolescents-an-experimental-study-of-gratitude-and-subjective-wellbeing/','Froh, Sefick & Emmons 2008'),
 ('Lòng biết ơn gắn với hạnh phúc ở 80 trẻ khoảng 5 tuổi (tương quan)','Đã xác nhận','https://ideas.repec.org/a/spr/jhappi/v21y2020i8d10.1007_s10902-019-00188-6.html','Nguyen & Gordon 2020'),
 ('Thưởng vật chất làm trẻ 20 tháng giúp đỡ ít hơn về sau','Đã xác nhận','https://scholars.duke.edu/publication/1458228','Warneken & Tomasello 2008'),
 ('Bố mẹ làm mẫu, đáp lại, chỉ dạy về cảm xúc gắn với kỹ năng cảm xúc của trẻ mầm non; mức liên hệ nhỏ, chủ yếu tương quan','Đã xác nhận','https://figshare.com/articles/journal_contribution/Parents_socialization_of_preschool-aged_children_s_emotion_skills_A_meta-analysis_using_an_emotion-focused_parenting_practices_framework/14515686','Zinsser, Gordon & Jiang 2021'),
 ('Mẹo "không lọt lõi giấy vệ sinh" để loại vật nhỏ','Đánh giá chuyên môn','',''),
 ('Lịch 12 tuần và các hoạt động của khóa Gia đình 2–8','Đánh giá chuyên môn','',''),
]
def _src(u,s): return f'<a href="{u}">{s}</a>' if u else 'Thiết kế của daynentang.com'
erows = ''.join(f'<tr><td>{c}</td><td><span class="label">[{l}]</span></td><td>{_src(u,s)}</td></tr>' for c,l,u,s in EV)
page('/bang-chung/', 'Bằng chứng và nguồn', 'Bảng kiểm chứng: các nhận định trên daynentang.com, nhãn mức độ chắc chắn và nguồn gốc.',
f'''
<h1>Bằng chứng và nguồn</h1>
<p class="lead">Mỗi nhận định quan trọng trên trang được gắn một trong bốn nhãn.</p>
<ul>
<li><strong>[Đã xác nhận]</strong> – có nguồn đã đọc, ghi rõ bên cạnh.</li>
<li><strong>[Suy luận]</strong> – rút ra từ nguồn, nhưng nguồn không nói trực tiếp.</li>
<li><strong>[Đánh giá chuyên môn]</strong> – ý kiến của người soạn, chưa có nghiên cứu riêng.</li>
<li><strong>[Cần kiểm chứng]</strong> – chưa tìm được nguồn đủ tin cậy.</li>
</ul>
<div class="table-wrap"><table>
<thead><tr><th>Nhận định</th><th>Nhãn</th><th>Nguồn</th></tr></thead>
<tbody>{erows}</tbody></table></div>
<p class="small muted">Tra cứu ngày 28/10/2026. Thấy sai sót? Chúng tôi sửa công khai trong nhật ký sửa đổi ở trang Giới thiệu.</p>
''', current=None)

# ---------- 404 ----------
page('/404.html', 'Không tìm thấy trang', 'Trang bạn tìm không có trên daynentang.com.',
'''<h1>Không tìm thấy trang</h1><p>Trang này không có hoặc đã đổi địa chỉ.</p>
<p><a class="btn primary" href="/">Về trang chủ</a> <a class="btn" href="/gia-dinh/">Khóa cho gia đình</a></p>''')

# ---------- robots, sitemap, headers ----------
urls = []
for d, _, files in os.walk(ROOT):
    if '/.git' in d: continue
    for f in files:
        if f == 'index.html':
            rel = os.path.relpath(d, ROOT)
            urls.append('/' if rel == '.' else '/' + rel + '/')
urls.sort()
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + \
     ''.join(f'  <url><loc>{SITE}{u}</loc><lastmod>2026-10-28</lastmod></url>\n' for u in urls) + '</urlset>\n'
open(os.path.join(ROOT,'sitemap.xml'),'w').write(sm)
open(os.path.join(ROOT,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
open(os.path.join(ROOT,'_headers'),'w').write('''/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  Content-Security-Policy: default-src 'self'; img-src 'self' data:; style-src 'self'; script-src 'self' 'unsafe-inline'; frame-ancestors 'none'; base-uri 'self'; form-action 'none'
  X-Frame-Options: DENY
''')
print(len(urls), 'pages')
