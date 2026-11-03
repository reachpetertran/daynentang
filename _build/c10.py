# Khóa C10 "Nền tảng không cần điện" – trang khóa, 11 bài, công cụ "Sổ nền tảng không cần điện".
# Người đọc: bố mẹ ở nơi thiếu điện, nước, trường học (có phần làm cùng con) và người tự học từ 15 tuổi.
# Thiết kế in trước: một người in giúp, cả nhà học bằng giấy bút, đồ sẵn có.
# Có người đọc dưới 18 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c10  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/nen-tang-khong-can-dien/'
TOOL = '/cong-cu/so-nen-tang/'
G2 = '/khoa-hoc/gia-dinh-0-2/'
G3 = '/khoa-hoc/gia-dinh-2-8/'
G6 = '/khoa-hoc/tien-nha-minh/'
G8 = '/khoa-hoc/nha-gon-nha-an-toan/'
G9 = '/khoa-hoc/gia-dinh-va-cong-dong/'
C3 = '/khoa-hoc/tu-hoc-tu-quan/'
C8 = '/khoa-hoc/cham-tam-tri-co-ban/'
def url(w, slug): return f'{U}bai-{w}/{slug}/'
def sec(n, title, body): return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'
def lines(labels):
    rows = ''.join(f'<tr><th class="w38">{x}</th><td></td></tr>' for x in labels)
    return f'<div class="table-wrap journal"><table><tbody>{rows}</tbody></table></div>'
def table(head, rows):
    h = ''.join(f'<th>{x}</th>' for x in head)
    b = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'
def selftab(items, a='Tuần này', b='Sau 2 tuần'):
    rows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in items)
    return ('<p>0 = chưa làm · 1 = làm được một phần · 2 = làm đều, thành nếp.</p>'
            f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>{a}</th><th>{b}</th></tr></thead><tbody>{rows}</tbody></table></div>')

# ---------- Nguồn (đã tra 03/11/2026, trừ khi ghi khác) ----------
BOIL = '<a href="https://www.who.int/publications/i/item/WHO-FWC-WSH-15.02">WHO – Boil water (bản tóm tắt kỹ thuật, 14/1/2015)</a>'
HWTS = '<a href="https://www.who.int/teams/environment-climate-change-and-health/water-sanitation-and-health/water-safety-and-quality/household-water-treatment-and-safe-storage">WHO – Xử lý và trữ nước tại hộ gia đình</a>'
CDCW = '<a href="https://www.cdc.gov/global-water-sanitation-hygiene/about/about-household-water-treatment.html">CDC – Household Water Treatment (22/4/2024)</a>'
WDIA = '<a href="https://www.who.int/news-room/fact-sheets/detail/diarrhoeal-disease">WHO – Bệnh tiêu chảy (tờ thông tin, 7/3/2024)</a>'
HW = '<a href="https://www.cochrane.org/evidence/CD004265_does-promoting-handwashing-reduce-diarrhoea">Ejemot-Nwadiaro et al. 2021, <em>Cochrane</em> CD004265</a>'
HAP = '<a href="https://www.who.int/news-room/fact-sheets/detail/household-air-pollution-and-health">WHO – Ô nhiễm không khí trong nhà (tờ thông tin, 16/12/2025)</a>'
FOOD = '<a href="https://www.paho.org/en/news/21-12-2015-pahowho-recommends-five-keys-safer-food-healthy-holiday-season">Năm chìa khóa an toàn thực phẩm của WHO (PAHO/WHO)</a>'
BURN = '<a href="https://www.schn.health.nsw.gov.au/kids-health-hub/safety-and-injury-prevention/burns-and-fire/first-aid-burns">Mạng lưới Bệnh viện Nhi Sydney – sơ cứu bỏng</a>'
DROWN = '<a href="https://medlineplus.gov/ency/article/000046.htm">MedlinePlus – Near drowning (duyệt 14/10/2025)</a>'
WHOVN = '<a href="https://www.who.int/vietnam/vi/news/feature-stories/item/in-viet-nam--low-cost-water-safety-actions-help-reduce-child-drowning-deaths">WHO Việt Nam, 12/2023</a>'
HARV = '<a href="https://bettercarenetwork.org/sites/default/files/HCDC_ServeReturn_for_Parents_Caregivers_2019.pdf">Harvard Center on the Developing Child – Serve and Return (2019)</a>'
REACH = '<a href="https://reachupandlearn.com/resources/">Reach Up (CC BY-NC-SA 4.0)</a>'
JAM = '<a href="https://sciencedaily.com/releases/2014/05/140529142354.htm">Gertler et al. 2014, <em>Science</em></a>'
READ = '<a href="https://www.physiciansweekly.com/aap-why-literacy-promotion-is-crucial-during-clinical-visits/">AAP 2024 – khuyến khích đọc sách</a>'
NOBLE = '<a href="https://hira.hope.ac.uk/id/eprint/3756/">Noble et al. 2019, <em>Educational Research Review</em> 28</a>'
DUN = '<a href="https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html">Dunlosky et al. 2013 (thông cáo của APS)</a>'
EEF = '<a href="https://educationendowmentfoundation.org.uk/news/latest-updates-to-the-toolkit/">EEF – Teaching and Learning Toolkit, siêu nhận thức</a>'
CFPB_BB = '<a href="https://www.consumerfinance.gov/consumer-tools/educator-tools/youth-financial-education/learn/">CFPB – các khối nền năng lực tài chính</a>'
CFPB_SAVE = '<a href="https://www.consumerfinance.gov/about-us/newsroom/cfpb-announces-start-small-save-initiative">CFPB 2019 – Start Small, Save Up</a>'
BLDS = '<a href="https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam">Bộ luật Dân sự 2015, Điều 468</a>'
READY = '<a href="https://www.ready.gov/kit">Ready.gov (FEMA) – Build a Kit</a>'
PCTT = '<a href="https://thuvienphapluat.vn/van-ban/Van-hoa-Xa-hoi/Luat-phong-chong-thien-tai-nam-2013-197310.aspx">Luật Phòng, chống thiên tai số 33/2013/QH13 (hiệu lực 01/5/2014; sửa đổi năm 2020)</a>'
HL = '<a href="https://www.rti.org/publication/social-relationships-mortality-risk-meta-analytic-review">Holt-Lunstad et al. 2010, <em>PLoS Medicine</em></a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài chưa được nhân viên y tế, cán bộ phòng chống thiên tai hay giáo viên mầm non duyệt. Bài không thay thế khám, chữa bệnh.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Người từ 18 tuổi có thể góp ý cho bài ở trang '
           '<a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên thật, tên con hay nơi ở.</p>')
TALK = ('Cấp cứu: <strong>115</strong>. Cháy: <strong>114</strong>. Công an: <strong>113</strong>. Cứu nạn: <strong>112</strong>. '
        'Trẻ em gặp nguy hiểm: <strong>111</strong> (24/7). Không có sóng: nhờ hàng xóm, trưởng thôn, trạm y tế gần nhất.')
TEEN = 'Nếu bạn 15–17 tuổi: học cùng bố mẹ, thầy cô hoặc một người lớn bạn tin.'

L = {
 '1': (1, 'hoc-bang-giay-but', 'Bài 1', 'Học bằng giấy bút'),
 '2': (2, 'nuoc-uong-an-toan', 'Bài 2', 'Nước uống an toàn'),
 '3': (3, 'rua-tay-tieu-chay', 'Bài 3', 'Rửa tay, vệ sinh và khi bị tiêu chảy'),
 '4': (4, 'an-du-giu-do-an', 'Bài 4', 'Ăn đủ, giữ đồ ăn không cần tủ lạnh'),
 '5': (5, 'lua-khoi-den', 'Bài 5', 'Lửa, khói và đèn an toàn'),
 '6': (6, 'so-cuu-tay-khong', 'Bài 6', 'Sơ cứu tay không'),
 '7': (7, 'choi-voi-con', 'Bài 7', 'Chơi và học với con bằng đồ sẵn có'),
 '8': (8, 'chu-va-so-cung-con', 'Bài 8', 'Chữ và số cùng con, không cần sách mua'),
 '9': (9, 'so-thu-chi-giay', 'Bài 9', 'Sổ thu chi bằng giấy, để dành nhỏ'),
 '10': (10, 'bao-lu-mat-dien', 'Bài 10', 'Chuẩn bị khi bão lũ, mất điện dài ngày'),
 '11': (11, 'nguoi-co-the-nho', 'Bài 11', 'Người có thể nhờ, kế hoạch gia đình'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn làm 10 thẻ hỏi – đáp và tự kiểm 4 ngày trong tuần.'),
 (2, 'Cả nhà chỉ uống nước đã đun sôi, cất trong can có nắp, 7 ngày.'),
 (3, 'Nhà có chỗ rửa tay có xà phòng; rửa tay đủ 5 lúc, 5 ngày.'),
 (4, 'Bạn ghi bữa ăn 3 ngày, thêm 1 nhóm còn thiếu vào 1 bữa.'),
 (5, 'Bạn sửa ít nhất 2 nguy cơ về khói, dầu hỏa, nến trong nhà.'),
 (6, 'Bạn nói lại 3 bước sơ cứu bỏng và 5 tình huống phải đi viện.'),
 (7, 'Bạn chơi giao – đáp với con 10 phút, 5 ngày trong tuần.'),
 (8, 'Bạn kể chuyện qua tranh và đếm đồ thật với con 5 ngày.'),
 (9, 'Bạn ghi thu chi 7 ngày và để riêng một khoản nhỏ.'),
 (10, 'Nhà có túi khẩn cấp và mọi người biết chỗ để.'),
 (11, 'Nhà có kế hoạch một trang, dán chỗ cả nhà thấy.'),
]

def lesson(k, desc, goals, prep, read, do, note, safety, child, selfq, teacher, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Bài {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Ghi lại 5 phút', 'Không cần điện']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (2 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Ghi lại (5 phút)', note),
        sec(6, 'An toàn', ul(safety + [TEEN, TALK])),
        sec(7, 'Làm cùng con (cho bố mẹ)', ul(child)),
        sec(8, 'Tự theo dõi', selftab(selfq)),
        sec(9, 'Cho người dạy lại: thầy cô, cán bộ thôn, hội phụ nữ', ul(teacher)),
        sec(10, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Nền tảng không cần điện</a> · Bài {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('Z' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026 · In một lần, dùng không cần điện</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Nền tảng không cần điện, bài 1: tự học bằng giấy bút với vòng tự học bốn bước và thẻ hỏi – đáp tự làm.',
 ['Nói được <strong>4 bước</strong> của vòng tự học: đặt mục tiêu – học – tự kiểm – xem lại.',
  'Làm <strong>10 thẻ hỏi – đáp</strong> từ giấy cũ.',
  'Tự kiểm bằng thẻ <strong>4 ngày</strong> trong tuần.'],
 [f'In trang 1 của <a href="{TOOL}">Sổ nền tảng</a>, hoặc lấy một quyển vở.', 'Bút, kéo, giấy cũ (lịch cũ, vỏ hộp, giấy đã viết một mặt).'],
 ['Không có điện, mạng hay máy tính, bạn <strong>vẫn tự học được</strong>. Cần giấy, bút và một nếp nhỏ.',
  '<strong>Bước 1, đặt mục tiêu nhỏ:</strong> viết một việc học xong được trong tuần. Ví dụ: thuộc 10 bước sơ cứu.',
  '<strong>Bước 2, học 15 phút:</strong> chọn một giờ cố định mỗi ngày, lúc trời còn sáng.',
  '<strong>Bước 3, tự kiểm:</strong> gấp sách lại, tự hỏi mình. Tự kiểm giúp nhớ lâu hơn đọc đi đọc lại.',
  '<strong>Thẻ hỏi – đáp:</strong> mặt trước ghi câu hỏi, mặt sau ghi câu trả lời. Tự trả lời rồi mới lật thẻ.',
  'Thẻ trả lời sai thì để lên trên, hỏi lại ngày mai. Thẻ đúng 3 lần thì để sang bên.',
  '<strong>Bước 4, xem lại cuối tuần:</strong> mình học được gì? Cách nào giúp? Tuần sau đổi gì?',
  'Giữ giấy tờ trong túi ni lông, để chỗ khô, xa bếp.'],
 '<p><strong>Bài 1: làm 10 thẻ.</strong> Cắt giấy cũ cỡ bàn tay. Chọn 10 câu hỏi từ bài này hoặc bài bạn đang học.</p>'
 + '<p><strong>Bài 2: mục tiêu tuần này.</strong></p>'
 + lines(['Mục tiêu nhỏ của tôi tuần này', 'Giờ học cố định mỗi ngày', 'Chỗ học (có ánh sáng tự nhiên)']),
 table(['Ngày'] + DAYS, [['Tự kiểm ✓'] + [''] * 7, ['Số thẻ đúng'] + [''] * 7]),
 ['Học bằng ánh sáng tự nhiên khi có thể. Đèn dầu, nến: xem bài 5.', 'Kéo, dao cắt giấy: cất xa trẻ nhỏ.'],
 ['Con từ 5 tuổi: cùng làm thẻ hình. Mặt trước vẽ con vật, mặt sau viết tên.',
  'Hỏi con bằng thẻ 5 phút. Khen cố gắng: "Con nhớ được 3 thẻ rồi."',
  'Con đi học: dùng thẻ để ôn bài ở trường.'],
 ['Tôi có mục tiêu nhỏ cho tuần', 'Tôi học 15 phút mỗi ngày', 'Tôi tự kiểm bằng thẻ'],
 ['Có thể dạy cho cả nhóm ở nhà văn hóa thôn. Mỗi người làm 10 thẻ.',
  'Phát bài in cho từng hộ. Hẹn tuần sau gặp lại, hỏi "Tuần này học được gì?"',
  f'Người học lớp 12 hoặc sinh viên: xem thêm khóa <a href="{C3}">Tự học – tự quản</a>.'],
 [lb('Đã xác nhận', f'Tự kiểm tra và ôn giãn cách được xếp mức hữu ích cao; đọc lại, tô màu mức thấp ({DUN}).'),
  lb('Đã xác nhận', f'Dạy cách lên kế hoạch, theo dõi, xem lại việc học: trung bình khoảng +7 tháng tiến bộ; chủ yếu trong trường học có thầy cô ({EEF}).'),
  lb('Đánh giá chuyên môn', 'Quy tắc "đúng 3 lần thì để sang bên" do daynentang.com soạn, để dễ làm; chưa có nghiên cứu riêng.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Nền tảng không cần điện, bài 2: có nước uống an toàn bằng cách để lắng, lọc qua vải, đun sôi và cất trong can có nắp.',
 ['Làm được <strong>4 bước</strong>: để lắng – lọc qua vải – đun sôi sùng sục – cất can có nắp.',
  'Cả nhà chỉ uống nước đã đun sôi trong <strong>7 ngày</strong>.',
  'Nói được <strong>1 điều</strong> đun sôi không làm được.'],
 ['Nồi có nắp, can hoặc bình sạch có nắp.', 'Một miếng vải sạch (áo bông cũ, khăn).'],
 ['Nước trông trong <strong>vẫn có thể có mầm bệnh</strong>. Mầm bệnh gây tiêu chảy, nhất là ở trẻ nhỏ.',
  '<strong>Để lắng:</strong> nước đục thì để yên trong thùng vài giờ cho đất cát lắng xuống, rồi gạn lấy phần trong.',
  '<strong>Lọc qua vải:</strong> đổ nước qua vải sạch gấp vài lớp. Bước này bớt cặn, chưa làm nước an toàn.',
  '<strong>Đun sôi sùng sục:</strong> đun tới khi sủi bọt mạnh, liên tục, rồi để thêm khoảng 1 phút.',
  'Đun sôi sùng sục diệt được vi khuẩn, vi rút và ký sinh trùng.',
  '<strong>Cất can có nắp:</strong> để nguội trong nồi đậy nắp, rót sang can sạch. Rót ra khi dùng, không nhúng ca hay tay vào.',
  'Thiếu củi, trời nắng to: phơi chai nhựa trong, đựng nước trong, dưới nắng gắt 6–8 giờ (trời âm u: 2 ngày). Đun sôi vẫn là cách chính.',
  '<strong>Đun sôi không khử được hóa chất</strong>, thuốc trừ sâu, dầu. Nước nghi nhiễm hóa chất: hỏi trạm y tế, tìm nguồn khác.'],
 '<p><strong>Bài 1: đun một nồi nước theo 4 bước.</strong> Đánh dấu ✓ khi xong từng bước.</p>'
 + table(['Bước', '✓', 'Ghi chú'], [['1. Để lắng', '', ''], ['2. Lọc qua vải', '', ''], ['3. Đun sôi sùng sục + 1 phút', '', ''], ['4. Cất can có nắp', '', '']])
 + '<p><strong>Bài 2: nhà mình lấy nước ở đâu?</strong></p>'
 + lines(['Nguồn nước nhà mình', 'Ai đun nước, mỗi ngày mấy lần', 'Chỗ để can nước (xa trẻ nhỏ, có nắp)']),
 table(['Ngày'] + DAYS, [['Chỉ uống nước đun sôi ✓'] + [''] * 7]),
 ['Nước sôi gây bỏng nặng. Để nồi xa mép, xa tầm tay trẻ. Sơ cứu bỏng: bài 6.',
  'Thùng, chum, xô có nước: luôn đậy nắp. Trẻ nhỏ có thể đuối nước trong vài phân nước.',
  'Không dùng chai từng đựng dầu, thuốc trừ sâu để chứa nước.'],
 ['Con lớn: cùng dán nhãn "Nước đã đun" lên can.', 'Dạy con rót nước ra cốc, không nhúng cốc vào can.',
  'Con nhỏ: chỉ uống nước đã đun và để nguội. Bố mẹ cầm cốc cho con.'],
 ['Nhà tôi chỉ uống nước đun sôi', 'Can nước luôn có nắp', 'Tôi rót ra, không nhúng ca'],
 ['Làm mẫu 4 bước trước nhóm. Hỏi mỗi người nguồn nước nhà mình.',
  'Nguồn nước nghi nhiễm hóa chất hay sau lũ: báo trạm y tế xã.'],
 [lb('Đã xác nhận', f'Đun nước tới sôi sùng sục đủ để bất hoạt vi khuẩn, vi rút, động vật nguyên sinh gây bệnh ({BOIL}).'),
  lb('Đã xác nhận', f'CDC: đun sôi sùng sục 1 phút (vùng cao trên khoảng 2.000 m: 3 phút), để nguội, cất trong đồ chứa sạch có nắp kín. Phơi nắng: chai trong, 6–8 giờ, trời âm u 2 ngày. Các cách này không khử hóa chất ({CDCW}).'),
  lb('Đã xác nhận', f'Xử lý và trữ nước an toàn tại nhà giúp bớt bệnh tiêu chảy, nhất là nơi dùng nguồn nước chưa an toàn ({HWTS}).'),
  lb('Đánh giá chuyên môn', 'Rót ra thay vì nhúng ca vào can: suy từ nguyên tắc giữ nước sạch sau xử lý; nguồn trên chỉ nói "đồ chứa có nắp kín".'),
  lb('Cần kiểm chứng', 'Chi tiết phơi nắng (loại chai, độ trong của nước) chưa đọc hướng dẫn gốc của WHO.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Nền tảng không cần điện, bài 3: rửa tay với xà phòng đúng 5 lúc, làm chỗ rửa tay không cần vòi, xử lý tiêu chảy bằng oresol và biết dấu hiệu nặng.',
 ['Làm <strong>chỗ rửa tay có xà phòng</strong> gần nhà vệ sinh hoặc bếp.',
  'Rửa tay đủ <strong>5 lúc</strong> trong ngày, 5 ngày trong tuần.',
  'Nói được <strong>3 việc</strong> khi bị tiêu chảy và các dấu hiệu phải đi trạm y tế.'],
 ['Xà phòng (bánh hoặc nước), can nhựa có nắp, dây treo, que nhọn để dùi lỗ (người lớn làm).'],
 ['Rửa tay <strong>với xà phòng</strong> giúp bớt tiêu chảy. Nước không thôi thì kém hơn.',
  '<strong>Năm lúc cần rửa:</strong> sau đi vệ sinh; sau lau rửa cho bé; trước khi nấu; trước khi ăn; trước khi cho con ăn.',
  '<strong>Cách rửa:</strong> làm ướt, xoa xà phòng lòng bàn tay, mu tay, kẽ ngón, móng tay, rồi tráng nước chảy, vẩy khô.',
  '<strong>Chỗ rửa tay không cần vòi:</strong> dùi lỗ nhỏ gần đáy can, nút bằng que. Rút que là có dòng nước chảy.',
  'Nước bẩn sau rửa nên chảy xuống hố hoặc chậu cây, không đọng quanh nhà.',
  '<strong>Khi bị tiêu chảy:</strong> uống oresol, pha đúng lượng nước ghi trên gói. Mua ở trạm y tế, hiệu thuốc.',
  '<strong>Ăn tiếp, bú mẹ tiếp.</strong> Trẻ nhỏ thường được kê thêm kẽm 10–14 ngày: hỏi nhân viên y tế.',
  '<strong>Đi trạm y tế ngay</strong> khi: lả hoặc ngủ li bì, mắt trũng, uống kém, có máu trong phân, tiêu chảy từ 14 ngày.'],
 '<p><strong>Bài 1: làm chỗ rửa tay.</strong> Ghi chỗ đặt và ai lo thay nước, xà phòng.</p>'
 + lines(['Chỗ rửa tay nhà mình', 'Người lo thay nước, xà phòng', 'Chỗ cất gói oresol'])
 + '<p><strong>Bài 2: tập rửa tay đủ bước</strong>, cả nhà cùng làm một lần, đếm chậm tới 20.</p>',
 table(['Lúc rửa tay'] + DAYS, [[x] + [''] * 7 for x in ['Sau đi vệ sinh', 'Sau lau rửa cho bé', 'Trước khi nấu', 'Trước khi ăn', 'Trước khi cho con ăn']]),
 ['Người lớn dùi lỗ can; cất que nhọn, dao xa trẻ.', 'Pha oresol sai lượng nước có thể hại. Đọc kỹ gói hoặc hỏi nhân viên y tế.',
  'Không tự cho trẻ uống thuốc cầm tiêu chảy khi chưa hỏi nhân viên y tế.'],
 ['Hát hoặc đếm chậm cùng con trong lúc rửa tay.', 'Con lớn nhắc cả nhà rửa tay trước bữa ăn.',
  f'Con dưới 2 tuổi bị tiêu chảy: bú mẹ tiếp, theo dõi dấu hiệu mất nước. Xem thêm khóa <a href="{G2}">Gia đình 0–2</a>.'],
 ['Nhà tôi có chỗ rửa tay có xà phòng', 'Tôi rửa tay đủ 5 lúc', 'Tôi biết dấu hiệu tiêu chảy nặng'],
 ['Cùng cả nhóm làm một chỗ rửa tay mẫu ở nhà văn hóa, trường.',
  'Nhắc trạm y tế xã là nơi lấy oresol và hỏi về kẽm.'],
 [lb('Đã xác nhận', f'Vận động rửa tay ở cộng đồng nước thu nhập thấp, trung bình: số đợt tiêu chảy giảm khoảng 29% (bằng chứng mức vừa); ở trường, nhà trẻ nước thu nhập cao: khoảng 30% ({HW}).'),
  lb('Đã xác nhận', f'Phòng tiêu chảy: nước sạch, vệ sinh, rửa tay với xà phòng, bú mẹ hoàn toàn 6 tháng đầu, tiêm vắc xin rota. Điều trị: oresol, kẽm 10–14 ngày, ăn tiếp. Dấu hiệu mất nước và lúc cần đi khám ({WDIA}).'),
  lb('Đánh giá chuyên môn', 'Chỗ rửa tay bằng can dùi lỗ là cách làm phổ biến ở vùng thiếu nước; chưa có nguồn hướng dẫn gốc trong bài.'),
  lb('Cần kiểm chứng', 'Hướng dẫn của Bộ Y tế Việt Nam về liều kẽm cho trẻ.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Nền tảng không cần điện, bài 4: bữa ăn đủ nhóm từ thực phẩm địa phương và cách giữ đồ ăn an toàn khi không có tủ lạnh.',
 ['Ghi bữa ăn <strong>3 ngày</strong>, tìm nhóm còn thiếu.',
  'Thêm <strong>1 nhóm</strong> còn thiếu vào ít nhất 1 bữa mỗi ngày.',
  'Làm theo <strong>4 bước</strong> giữ đồ ăn không cần tủ lạnh.'],
 [f'In trang 4 của <a href="{TOOL}">Sổ nền tảng</a>.'],
 ['Một bữa đủ thường có <strong>3 nhóm</strong>: tinh bột (cơm, ngô, khoai), đạm (cá, trứng, đậu, thịt, tôm, cua), rau quả.',
  'Dùng đồ <strong>địa phương, theo mùa</strong>: rau vườn, đậu, trứng gà nhà, cá đồng thường rẻ hơn đồ mua.',
  'Đậu, lạc, vừng là nguồn đạm rẻ khi thiếu thịt cá.',
  '<strong>Không có tủ lạnh:</strong> nấu vừa đủ ăn một bữa. Ăn khi còn nóng.',
  'Đồ đã nấu chín <strong>không để quá 2 giờ</strong> ở nhiệt độ phòng.',
  'Còn thừa: đậy kín, để chỗ mát, xa ruồi. Ăn lại thì <strong>đun sôi kỹ</strong>.',
  'Giữ riêng đồ sống và đồ chín. Dùng thớt, dao riêng hoặc rửa kỹ giữa hai lần.',
  'Đồ có mùi lạ, nhớt, mốc: <strong>bỏ đi</strong>, kể cả khi tiếc.'],
 '<p><strong>Bài 1: ghi bữa ăn 3 ngày.</strong> Đánh dấu ✓ nhóm có trong bữa.</p>'
 + table(['Bữa', 'Tinh bột', 'Đạm', 'Rau quả'], [[f'Ngày {d} – {b}', '', '', ''] for d in (1, 2, 3) for b in ('trưa', 'tối')])
 + lines(['Nhóm hay thiếu nhất', 'Đồ địa phương mình thêm vào']),
 lines(['Việc giữ đồ ăn nhà mình đã làm', 'Việc sẽ đổi tuần này']),
 ['Đồ ăn của trẻ nhỏ: nấu mới, ăn ngay; không để dành qua bữa.', 'Hạt cứng, lạc nguyên hạt: trẻ dưới 4 tuổi dễ hóc. Nghiền nhỏ hoặc nấu nhừ.',
  'Ruồi nhiều, thức ăn hỏng nhanh: ưu tiên nấu vừa đủ.'],
 ['Con lớn: cùng kể tên 3 nhóm trong mâm cơm.', 'Cho con nhặt rau, rửa rau với bố mẹ.',
  f'Bé dưới 2 tuổi: xem lời khuyên ăn dặm của nhân viên y tế; khóa <a href="{G2}">Gia đình 0–2</a>.'],
 ['Bữa nhà tôi có đủ 3 nhóm', 'Tôi nấu vừa đủ ăn', 'Đồ chín không để quá 2 giờ'],
 ['Cho nhóm kể món địa phương rẻ, có đạm.', 'Không bán, không quảng cáo thực phẩm chức năng trong buổi học.'],
 [lb('Đã xác nhận', f'Năm chìa khóa: giữ sạch; để riêng sống – chín; nấu chín kỹ; giữ đồ ăn ở nhiệt độ an toàn, không để đồ chín quá 2 giờ ở nhiệt độ phòng; dùng nước và nguyên liệu an toàn ({FOOD}).'),
  lb('Đánh giá chuyên môn', 'Cách chia 3 nhóm là cách đơn giản để tự kiểm; không phải khẩu phần chi tiết. Người có bệnh mạn tính, phụ nữ mang thai cần hỏi nhân viên y tế.'),
  lb('Cần kiểm chứng', 'Tuổi an toàn cho trẻ ăn lạc nguyên hạt theo hướng dẫn Bộ Y tế; bài lấy mốc thận trọng dưới 4 tuổi.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Nền tảng không cần điện, bài 5: bớt khói bếp củi, cất dầu hỏa an toàn, dùng nến và đèn dầu không gây cháy.',
 ['Đi một vòng nhà, tìm <strong>nguy cơ</strong> về khói, dầu hỏa, nến, đèn.',
  'Sửa ít nhất <strong>2 nguy cơ</strong> trong tuần.',
  'Nói được việc phải làm khi trẻ <strong>uống nhầm dầu hỏa</strong>.'],
 [f'In trang 5 của <a href="{TOOL}">Sổ nền tảng</a>.'],
 ['Khói từ bếp củi, rơm, than và đèn dầu hỏa <strong>hại phổi</strong>, nhất là ở trẻ nhỏ.',
  'Trẻ hít nhiều khói trong nhà dễ bị viêm phổi hơn.',
  '<strong>Bớt khói:</strong> nấu chỗ thoáng; mở cửa, mở lỗ thoát khói; dùng củi khô; trẻ nhỏ chơi xa bếp.',
  'Có điều kiện thì chuyển dần sang bếp sạch hơn: bếp gas, bếp điện mặt trời, bếp cải tiến ít khói.',
  '<strong>Dầu hỏa:</strong> đựng chai có nhãn rõ, cất cao, có khóa. <strong>Không bao giờ</strong> đựng trong chai nước, chai nước ngọt.',
  'Trẻ uống nhầm dầu hỏa là ngộ độc hay gặp. Gọi <strong>115</strong> hoặc đưa đi viện ngay, mang theo chai.',
  '<strong>Nến, đèn dầu:</strong> đặt trên đế vững, xa màn, rèm, mái lá. Không để trẻ ở một mình với ngọn lửa.',
  'Thổi tắt trước khi ngủ hoặc rời phòng. Để sẵn xô cát hoặc nước gần bếp.'],
 '<p><strong>Bài 1: đi một vòng nhà.</strong> Đánh dấu ✓ điều đã ổn, ✗ điều cần sửa.</p>'
 + table(['Mục', '✓ / ✗', 'Sửa thế nào'], [[x, '', ''] for x in ['Bếp có chỗ thoát khói', 'Trẻ nhỏ chơi xa bếp', 'Dầu hỏa chai có nhãn, cất cao', 'Không có dầu trong chai nước',
                                                                      'Nến, đèn có đế vững', 'Đèn xa màn, mái lá', 'Có xô cát hoặc nước gần bếp', 'Diêm, bật lửa cất cao']]),
 lines(['Nguy cơ 1 tôi đã sửa', 'Nguy cơ 2 tôi đã sửa']),
 ['Cháy: gọi <strong>114</strong>, đưa mọi người ra ngoài trước, không quay lại lấy đồ.', 'Không đổ nước vào chảo dầu đang cháy: đậy nắp, tắt bếp.',
  'Ho kéo dài, khó thở, trẻ thở nhanh: đi khám.'],
 ['Dạy con lớn: "Chai có nhãn đỏ là dầu, không được uống."', 'Con nhỏ: bế xa bếp khi nấu; quây chỗ chơi nếu được.',
  f'Thêm về phòng cháy trong nhà: khóa <a href="{G8}">Nhà gọn, nhà an toàn</a>.'],
 ['Bếp nhà tôi thoáng hơn', 'Dầu hỏa cất đúng chỗ', 'Nến, đèn tắt trước khi ngủ'],
 ['Đi cùng một hộ làm mẫu phần rà soát.', 'Nhắc: không bán, không quảng cáo loại bếp nào trong buổi học.'],
 [lb('Đã xác nhận', f'Khoảng 2,1 tỷ người nấu bằng nhiên liệu gây ô nhiễm (củi, than, rơm, dầu hỏa). Ô nhiễm không khí trong nhà gần như tăng gấp đôi nguy cơ nhiễm khuẩn hô hấp dưới ở trẻ ({HAP}).'),
  lb('Đã xác nhận', f'Trẻ uống nhầm dầu hỏa là nguyên nhân hàng đầu gây ngộ độc ở trẻ (theo WHO); nhiều ca bỏng nặng gắn với bếp, đèn trong nhà ({HAP}).'),
  lb('Đánh giá chuyên môn', 'Mở cửa, lỗ thoát khói, dùng củi khô giúp bớt khói. WHO chủ yếu khuyên chuyển sang nhiên liệu sạch; chưa có số đo cho các cách nhỏ này.'),
  lb('Đánh giá chuyên môn', 'Mang theo chai khi đi viện để nhân viên y tế biết chất gì; không tự gây nôn khi chưa được hướng dẫn.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Nền tảng không cần điện, bài 6: sơ cứu bỏng, vết cắt, đuối nước bằng tay không và năm tình huống phải đi viện ngay.',
 ['Nói lại <strong>3 bước</strong> sơ cứu bỏng.',
  'Nói được <strong>5 tình huống</strong> phải gọi 115 hoặc đi viện ngay.',
  'Chuẩn bị <strong>túi sơ cứu</strong> tối thiểu trong nhà.'],
 ['Một túi ni lông kín, vải sạch, xà phòng.', f'In trang 6 của <a href="{TOOL}">Sổ nền tảng</a>.'],
 ['<strong>Bỏng:</strong> làm mát bằng nước mát đang chảy <strong>20 phút</strong>, kể cả vài giờ sau khi bị bỏng.',
  'Tháo nhẫn, vòng, quần áo gần vết bỏng (trừ chỗ dính vào da).',
  '<strong>Không bôi</strong> đá, kem đánh răng, mỡ, bơ. Vết bỏng phồng rộp hoặc rộng: đi khám.',
  '<strong>Vết cắt:</strong> rửa tay, rửa vết thương dưới nước sạch. Ép chặt bằng vải sạch cho cầm máu.',
  'Ép mãi vẫn chảy, vết sâu, há miệng, do vật bẩn hay con vật cắn: đi trạm y tế.',
  '<strong>Đuối nước:</strong> không nhảy xuống nếu không biết cứu đuối. Đưa sào, cành cây, ném phao, dây.',
  'Người đã ngừng thở: gọi to nhờ giúp, gọi 115, thổi ngạt ngay nếu bạn đã được học.',
  'Người suýt chết đuối, <strong>dù đã tỉnh</strong>, vẫn cần được nhân viên y tế khám.'],
 '<p><strong>Bài 1: đóng vai.</strong> Một người "bị bỏng tay", một người sơ cứu, nói to từng bước.</p>'
 + '<p><strong>Bài 2: năm tình huống phải đi viện ngay.</strong> Viết lại bằng lời của mình.</p>'
 + lines(['1. Bất tỉnh, co giật', '2. Khó thở, tím tái', '3. Chảy máu ép chặt vẫn không cầm', '4. Đuối nước, dù đã tỉnh', '5. Bỏng rộng, phồng rộp nhiều']),
 lines(['Trạm y tế gần nhất, đi mất bao lâu', 'Người có xe chở đi viện khi cần', 'Túi sơ cứu nhà mình để ở']),
 ['Không tự xuống nước sâu để cứu người khi không biết cứu đuối.', 'Rửa tay trước và sau khi chạm vết thương người khác.',
  'Rắn cắn, chó cắn: rửa vết thương, đi trạm y tế ngay, không tự chích, hút nọc.'],
 ['Con lớn tập vai người sơ cứu bỏng: dẫn em ra nước, nói "20 phút", gọi bố mẹ.',
  'Dạy con: thấy bạn rơi xuống nước thì hô to gọi người lớn, ném đồ nổi, không nhảy xuống.',
  'Ao, giếng, thùng nước gần nhà: rào hoặc đậy nắp.'],
 ['Tôi nói được 3 bước sơ cứu bỏng', 'Tôi biết 5 tình huống phải đi viện', 'Nhà tôi có túi sơ cứu'],
 ['Mời nhân viên trạm y tế xã tới dạy thực hành thổi ngạt, ép tim.',
  'Bài này không dạy hồi sức tim phổi; cần học trực tiếp, có người hướng dẫn.'],
 [lb('Đã xác nhận', f'Sơ cứu bỏng: nước mát đang chảy 20 phút, tháo trang sức gần vết bỏng; không bôi đá, kem, kem đánh răng, bơ ({BURN}).'),
  lb('Đã xác nhận', f'Cứu đuối: không tự đặt mình vào nguy hiểm; đưa sào, ném dây có vật nổi; người từng suýt chết đuối cần được khám, kể cả khi trông đã ổn ({DROWN}).'),
  lb('Đã xác nhận', f'Mỗi năm khoảng 2.000 trẻ em Việt Nam tử vong do đuối nước ({WHOVN}).'),
  lb('Đánh giá chuyên môn', 'Rào ao, đậy giếng, thùng nước là cách phòng đuối nước tại nhà; bài này không đo hiệu quả riêng.'),
  lb('Đánh giá chuyên môn', 'Bước cầm máu, xử lý vết cắt, con vật cắn và danh sách 5 tình huống do daynentang.com soạn theo hướng dẫn sơ cứu phổ thông; chưa đối chiếu tài liệu Bộ Y tế.'),
  lb('Cần kiểm chứng', 'Tài liệu sơ cứu chính thức bằng tiếng Việt (Hội Chữ thập đỏ Việt Nam) để dẫn link.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Nền tảng không cần điện, bài 7: chơi giao – đáp với con 10 phút mỗi ngày bằng đồ tự làm từ chai, hộp, lá, vải vụn.',
 ['Chơi <strong>giao – đáp</strong> với con 10 phút, 5 ngày trong tuần.',
  'Làm <strong>2 đồ chơi</strong> từ đồ sẵn có, an toàn cho tuổi của con.',
  'Ghi <strong>1 điều mới</strong> con làm được trong tuần.'],
 ['Chai nhựa có nắp, hộp giấy, lá, que, vải vụn, băng dính.', 'Ống giấy vệ sinh để thử vật nhỏ (nếu con dưới 3 tuổi).'],
 ['Trẻ học nhiều nhất qua <strong>chơi và trò chuyện</strong> với người lớn thương mình.',
  '<strong>Giao – đáp:</strong> con chỉ, nhìn, nói. Bạn đáp lại: nhìn theo, gọi tên thứ con chỉ.',
  '<strong>Chờ con đáp</strong>, rồi đổi lượt. Giống chơi bóng qua lại.',
  'Không cần đồ chơi mua. <strong>Chai có hạt</strong> thành trống lắc. Hộp giấy thành nhà, thành xe.',
  'Lá, que, đá to: xếp hàng, so dài – ngắn, đếm. Vải vụn: chơi ú òa, trốn tìm.',
  'Vừa làm việc nhà vừa nói chuyện: "Mẹ đang nhặt rau. Lá này xanh. Con cầm thử?"',
  'Con chán thì đổi trò. <strong>Mười phút vui</strong> có ích hơn một giờ ép buộc.',
  'Đồ chơi tự làm cũng cần kiểm tra an toàn trước khi đưa con.'],
 '<p><strong>Bài 1: làm 2 đồ chơi.</strong> Ghi tên đồ chơi và trò chơi với nó.</p>'
 + table(['Đồ chơi', 'Làm từ', 'Trò chơi', 'Đã kiểm an toàn ✓'], [['', '', '', ''], ['', '', '', '']])
 + '<p><strong>Bài 2: chơi giao – đáp 10 phút</strong>, ngay hôm nay.</p>',
 table(['Ngày'] + DAYS, [['Chơi 10 phút ✓'] + [''] * 7, ['Con làm gì mới'] + [''] * 7]),
 ['Trẻ dưới 3 tuổi: bỏ mọi vật lọt qua ống giấy vệ sinh (hạt, sỏi, nắp nhỏ, pin, nam châm).',
  'Chai đựng hạt: dán chặt nắp bằng băng dính; kiểm tra lại mỗi ngày.',
  'Không chơi gần ao, giếng, xô nước khi không có người lớn sát bên.', 'Không dùng túi ni lông, dây dài làm đồ chơi cho trẻ nhỏ.'],
 ['Con 0–3 tuổi: mỗi ngày một lúc chơi giao – đáp, kể cả khi bế con đi làm.',
  'Con lớn hơn: cho con tự làm đồ chơi cho em, bố mẹ kiểm an toàn.',
  f'Thêm trò chơi theo tuổi: khóa <a href="{G2}">Gia đình 0–2</a> và <a href="{G3}">Gia đình 2–8</a>.'],
 ['Tôi chơi giao – đáp 10 phút', 'Tôi làm được đồ chơi an toàn', 'Tôi ghi điều mới con làm được'],
 ['Có thể tổ chức buổi "làm đồ chơi" ở nhà văn hóa, mỗi nhà mang đồ cũ tới.',
  'Kiểm từng đồ chơi bằng ống giấy vệ sinh trước khi phát cho trẻ dưới 3 tuổi.'],
 [lb('Đã xác nhận', f'Năm bước giao – đáp giúp xây não trẻ ({HARV}).'),
  lb('Đã xác nhận', f'Chương trình thăm nhà dạy mẹ chơi với con ở Jamaica: 20 năm sau, nhóm được thăm có thu nhập cao hơn khoảng 25% (105 người) ({JAM}). Chương trình có người thăm nhà hằng tuần, không phải tự học.'),
  lb('Đã xác nhận', f'Reach Up chia sẻ tài liệu chơi với trẻ bằng đồ tự làm, giấy phép CC BY-NC-SA 4.0 ({REACH}). Bài này chỉ mượn ý tưởng, viết lại.'),
  lb('Đánh giá chuyên môn', 'Thử bằng ống giấy vệ sinh là mẹo gia đình; ống thử chuẩn của Hoa Kỳ có đường kính 1,25 inch (khoảng 31,7 mm).')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Nền tảng không cần điện, bài 8: kể chuyện qua tranh, đọc chữ quanh nhà và đếm bằng đồ thật cùng con 2–6 tuổi, không cần sách mua.',
 ['Kể chuyện qua tranh cùng con <strong>10 phút</strong>, 5 ngày trong tuần.',
  'Đếm bằng đồ thật cùng con, <strong>1 lần mỗi ngày</strong>.',
  'Làm <strong>1 quyển sách tự làm</strong> 4–6 trang.'],
 ['Tranh từ lịch cũ, bao bì, báo, hoặc giấy và bút để tự vẽ.', 'Quả, nắp chai to, hòn đá to để đếm.'],
 ['Không cần sách mua. <strong>Tranh lịch cũ, bao bì, tranh tự vẽ</strong> đều kể chuyện được.',
  '<strong>Kể qua tranh, đổi lượt:</strong> chỉ tranh – hỏi "Gì đây?" – chờ con đáp – khen, nói thêm một ý.',
  'Hỏi câu mở: "Rồi sao nữa?", "Sao bạn ấy buồn?". Con nói nhiều hơn khi được hỏi.',
  '<strong>Sách tự làm:</strong> gấp 3 tờ giấy làm đôi, khâu hoặc ghim giữa. Mỗi trang một tranh, một câu.',
  '<strong>Chữ quanh nhà:</strong> chỉ chữ trên bao gạo, lịch, biển tên đường. Đọc to, cho con chỉ theo.',
  '<strong>Đếm bằng đồ thật:</strong> chạm từng vật, đọc to một số. Số cuối cùng cho biết có bao nhiêu.',
  'Tập so sánh: "Bên nào nhiều hơn?", "Que nào dài hơn?".',
  'Mười phút đều đặn mỗi ngày dễ giữ hơn một buổi dài.'],
 '<p><strong>Bài 1: làm sách tự làm.</strong> Chọn một chuyện quen: một ngày của con, con gà nhà mình, đi chợ.</p>'
 + lines(['Tên sách', 'Trang 1', 'Trang 2', 'Trang 3', 'Trang 4'])
 + '<p><strong>Bài 2: đếm cùng con</strong> 5 vật thật, rồi 10 vật.</p>',
 table(['Ngày'] + DAYS, [['Kể chuyện 10 phút ✓'] + [''] * 7, ['Đếm đồ thật ✓'] + [''] * 7, ['Con nói được gì mới'] + [''] * 7]),
 ['Trẻ dưới 3 tuổi: chỉ đếm đồ to, không lọt ống giấy vệ sinh. Không dùng hạt, sỏi nhỏ.',
  'Ghim, kim khâu sách: người lớn làm, cất ngay sau khi dùng.'],
 ['Con 2–3 tuổi: chỉ tranh, gọi tên, đếm tới 3–5.', 'Con 4–6 tuổi: con kể lại chuyện; đếm tới 10–20; tìm chữ cái tên mình.',
  'Con đã biết đọc: con đọc sách tự làm cho em nghe.'],
 ['Tôi kể chuyện qua tranh với con', 'Tôi đếm đồ thật với con', 'Nhà tôi có 1 sách tự làm'],
 ['Mỗi nhà làm một sách tự làm, đổi sách cho nhau sau 2 tuần.',
  'Bố mẹ không biết chữ vẫn kể chuyện qua tranh được. Nói rõ điều này để không ai ngại.'],
 [lb('Đã xác nhận', f'AAP khuyến khích bố mẹ đọc, kể chuyện cùng con từ sớm ({READ}).'),
  lb('Đã xác nhận', f'Phân tích gộp về đọc sách chung: tác dụng lên ngôn ngữ trẻ nhỏ (g = 0,19); gần như không còn khi so với nhóm có hoạt động khác; không khác theo mức thu nhập ({NOBLE}).'),
  lb('Suy luận', 'Vì tác dụng nhỏ, bài không hứa con "giỏi hơn". Bài nhắm thói quen trò chuyện, kể chuyện mỗi ngày.'),
  lb('Đánh giá chuyên môn', 'Kể qua tranh đổi lượt, đếm chạm từng vật và sách tự làm do daynentang.com soạn từ ý giao – đáp; chưa có thử nghiệm riêng.')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Nền tảng không cần điện, bài 9: ghi sổ thu chi bằng giấy 7 ngày, để dành trước một khoản nhỏ, tránh vay nóng.',
 ['Ghi <strong>tiền vào, tiền ra</strong> 7 ngày.',
  'Cuối tuần cộng lại, chọn <strong>1 khoản</strong> để bớt.',
  '<strong>Để riêng</strong> một khoản nhỏ mỗi lần có tiền vào.'],
 [f'In trang 9 của <a href="{TOOL}">Sổ nền tảng</a>, hoặc kẻ 3 cột trong vở.', 'Một hộp hoặc túi riêng để dành tiền.'],
 ['Ghi chép giúp thấy <strong>tiền đi đâu</strong>. Nhiều khoản nhỏ cộng lại thành lớn.',
  'Sổ giấy có <strong>3 cột</strong>: ngày – tiền vào – tiền ra (ghi ra cho việc gì).',
  'Mỗi tối ghi, mất khoảng 2 phút. Quên một ngày thì ghi bù theo trí nhớ.',
  'Cuối tuần cộng lại. Hỏi: khoản nào cần? Khoản nào muốn? <strong>Chọn 1 khoản</strong> bớt tuần sau.',
  '<strong>Để dành trước, tiêu sau:</strong> mỗi lần có tiền, để riêng một phần nhỏ ngay, trước khi tiêu.',
  'Quỹ để dành dùng cho <strong>ốm đau, mất mùa, bão lũ</strong>. Bắt đầu nhỏ cũng được.',
  'Cẩn thận <strong>vay nóng</strong>, vay qua người lạ, vay qua mạng: lãi cao, dễ mất nhà, mất đất.',
  'Bài này chỉ dạy thu chi cơ bản. Không tư vấn đầu tư hay vay.'],
 table(['Ngày', 'Tiền vào', 'Tiền ra', 'Cho việc gì'], [[d, '', '', ''] for d in DAYS] + [['Cộng', '', '', '']]),
 lines(['Khoản tôi chọn bớt tuần sau', 'Khoản tôi để riêng mỗi lần có tiền', 'Chỗ cất tiền để dành (an toàn, khô)']),
 ['Cất tiền ở chỗ khô, kín, tránh cháy, tránh nước lũ.', 'Không đưa giấy tờ nhà, đất, căn cước cho người lạ giữ khi vay.',
  'Bị đe dọa khi đòi nợ: gọi <strong>113</strong>.'],
 ['Con từ 6 tuổi: cho con một hũ nhỏ để dành, cùng đếm mỗi tuần.', 'Cho con theo đi chợ, tập so sánh giá hai món.',
  f'Thêm: khóa <a href="{G6}">Tiền nhà mình</a> (bảng thu chi, hũ ba ngăn).'],
 ['Tôi ghi thu chi 7 ngày', 'Tôi chọn được 1 khoản bớt', 'Tôi để riêng một khoản nhỏ'],
 ['Người không biết chữ: ghi bằng hình (bao gạo, con gà) và gạch đếm.',
  'Không xem sổ của người khác nếu họ không muốn. Tiền là chuyện riêng.'],
 [lb('Đã xác nhận', f'CFPB mô tả các khối nền năng lực tài chính: chức năng điều hành, thói quen tiền, kỹ năng ra quyết định ({CFPB_BB}).'),
  lb('Đã xác nhận', f'CFPB khuyến khích bắt đầu để dành nhỏ, đều đặn, để có quỹ cho lúc khó ({CFPB_SAVE}).'),
  lb('Đã xác nhận', f'Lãi suất vay theo thỏa thuận không vượt quá 20%/năm, trừ khi luật khác quy định ({BLDS}).'),
  lb('Cần kiểm chứng', 'Hiệu quả của khóa tài chính tự học với hộ gia đình thu nhập thấp ở nông thôn.')])

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Nền tảng không cần điện, bài 10: chuẩn bị túi khẩn cấp, việc làm trước – trong – sau bão lũ và khi mất điện dài ngày.',
 ['Nhà có <strong>túi khẩn cấp</strong>, mọi người biết chỗ để.',
  'Nói được <strong>việc làm trước – trong – sau</strong> bão lũ.',
  'Biết <strong>chỗ sơ tán</strong> của thôn và đường đi.'],
 [f'In trang 10 của <a href="{TOOL}">Sổ nền tảng</a>.', 'Một túi hoặc thùng có nắp, túi ni lông.'],
 ['<strong>Túi khẩn cấp:</strong> nước uống, đồ ăn khô cho vài ngày, đèn pin và pin, thuốc đang dùng, đồ sơ cứu.',
  'Thêm: giấy tờ quan trọng bọc túi ni lông, áo mưa, áo ấm, còi, ít tiền lẻ, tã, sữa nếu có trẻ nhỏ.',
  'Nước: tính khoảng 4 lít mỗi người mỗi ngày cho uống và vệ sinh.',
  '<strong>Trước bão lũ:</strong> nghe tin qua loa xã, đài; gia cố mái; kê cao lúa gạo, giấy tờ.',
  '<strong>Trong bão lũ:</strong> làm theo chỉ dẫn của chính quyền. <strong>Sơ tán ngay khi được báo</strong>, không đợi nước lên.',
  'Không lội, không bơi qua dòng nước chảy xiết. Trẻ em luôn trong tầm tay người lớn.',
  '<strong>Sau bão lũ:</strong> chờ báo an toàn mới về. Tránh dây điện đứt. Đun sôi nước trước khi uống.',
  '<strong>Mất điện dài ngày:</strong> dùng đèn pin trước nến; không để máy phát chạy trong nhà kín.'],
 '<p><strong>Bài 1: soạn túi khẩn cấp.</strong> Đánh dấu ✓ đồ đã có.</p>'
 + table(['Đồ', '✓', 'Đồ', '✓'], [['Nước uống', '', 'Áo mưa, áo ấm', ''], ['Đồ ăn khô', '', 'Còi', ''], ['Đèn pin, pin', '', 'Ít tiền lẻ', ''],
                                   ['Thuốc đang dùng', '', 'Giấy tờ (bọc ni lông)', ''], ['Đồ sơ cứu', '', 'Tã, sữa cho bé', '']])
 + lines(['Chỗ để túi khẩn cấp', 'Chỗ sơ tán của thôn', 'Đường đi tới chỗ sơ tán']),
 lines(['Người nhà cần giúp khi sơ tán (người già, người ốm, trẻ nhỏ)', 'Ai lo giúp người đó']),
 ['Máy phát điện, bếp than: chỉ dùng ngoài trời, nơi thoáng. Khí độc không mùi có thể gây chết người.',
  'Không chạm vào dây điện đứt, cột điện đổ; báo điện lực, chính quyền.',
  'Thay pin đèn, đồ ăn khô trong túi mỗi năm một lần, trước mùa mưa bão.'],
 ['Cho con lớn cùng soạn túi, biết chỗ để.', 'Tập đi bộ tới chỗ sơ tán một lần, như đi chơi.',
  'Dạy con số 115, 114 và tên bố mẹ, tên thôn.'],
 ['Nhà tôi có túi khẩn cấp', 'Tôi biết chỗ sơ tán', 'Cả nhà đã tập đi tới chỗ sơ tán'],
 ['Phối hợp với ban chỉ huy phòng chống thiên tai xã khi dạy bài này.',
  'Hỏi xã về danh sách hộ có người già, người khuyết tật cần giúp sơ tán.'],
 [lb('Đã xác nhận', f'Túi cơ bản có nước khoảng 1 gallon (khoảng 3,8 lít) mỗi người mỗi ngày trong vài ngày, đồ ăn khô, đèn pin, pin, đồ sơ cứu, còi ({READY}). Nguồn của Hoa Kỳ; bài chuyển sang đồ dùng ở Việt Nam.'),
  lb('Đã xác nhận', f'Hộ gia đình có nghĩa vụ chấp hành chỉ dẫn sơ tán của cơ quan có thẩm quyền (Điều 34); phòng chống thiên tai theo phương châm "bốn tại chỗ" (Điều 4 khoản 3) ({PCTT}).'),
  lb('Cần kiểm chứng', 'Số điều sau Luật sửa đổi năm 2020 (Luật 60/2020/QH14) có đổi không; bài dẫn theo văn bản năm 2013.'),
  lb('Đánh giá chuyên môn', 'Lời khuyên về máy phát điện, bếp than trong nhà kín do nguy cơ khí CO; chưa dẫn nguồn gốc trong bài.')])

# ======================= BÀI 11 =======================
lesson('11', 'Khóa Nền tảng không cần điện, bài 11: vẽ vòng người có thể nhờ trong xóm, viết kế hoạch gia đình một trang và xem lại cả khóa.',
 ['Vẽ <strong>vòng người có thể nhờ</strong> với ít nhất 5 người, nơi.',
  'Viết <strong>kế hoạch gia đình một trang</strong>, dán chỗ cả nhà thấy.',
  'Tự đánh giá lại <strong>cả khóa</strong>, chọn 2 nếp giữ tiếp.'],
 [f'In trang 11 và trang tự đánh giá của <a href="{TOOL}">Sổ nền tảng</a>.'],
 ['Ở nơi xa, thiếu điện, thiếu xe, <strong>hàng xóm</strong> thường là người tới giúp đầu tiên.',
  'Có người để nhờ gắn với sức khỏe tốt hơn. Đây là tương quan, nhưng là lý do để giữ quan hệ.',
  '<strong>Vòng trong:</strong> người trong nhà. <strong>Vòng giữa:</strong> họ hàng, hàng xóm tin cậy.',
  '<strong>Vòng ngoài:</strong> trưởng thôn, trạm y tế, trường, hội phụ nữ, công an xã.',
  'Hỏi trước: "Khi nhà tôi có chuyện ban đêm, tôi gọi anh được không?" Và nhận lời giúp lại họ.',
  '<strong>Kế hoạch gia đình một trang:</strong> chỗ gặp nhau khi có chuyện; ai đón con; số gọi; ai lo người già, người ốm.',
  'Dán kế hoạch chỗ cả nhà thấy. Xem lại mỗi năm, trước mùa mưa bão.',
  'Giúp hàng xóm cũng là cách dạy con về tử tế và trách nhiệm.'],
 '<p><strong>Bài 1: vòng người có thể nhờ.</strong></p>'
 + table(['Vòng', 'Người hoặc nơi', 'Cách liên lạc (số gọi, nhà ở đâu)'], [['Trong', '', ''], ['Giữa', '', ''], ['Giữa', '', ''], ['Ngoài', '', ''], ['Ngoài', '', '']])
 + '<p><strong>Bài 2: kế hoạch gia đình một trang.</strong></p>'
 + lines(['Khi có chuyện, cả nhà gặp nhau ở', 'Người đón con khi bố mẹ vắng', 'Ai lo người già, người ốm', 'Số gọi: 115 · 114 · 113 · 111 · trưởng thôn ……']),
 lines(['Hai nếp tôi giữ tiếp sau khóa', 'Một bài tôi muốn học lại']),
 ['Không ghi số căn cước, số tài khoản vào kế hoạch dán tường.', 'Kế hoạch có tên trẻ: dán trong nhà, không chụp đăng lên mạng.'],
 ['Cho con lớn biết nhà hàng xóm tin cậy và lúc nào được chạy sang.', 'Cùng con làm một việc tốt cho hàng xóm trong tuần.',
  f'Thêm: khóa <a href="{G9}">Gia đình và cộng đồng</a>.'],
 ['Tôi có vòng người có thể nhờ', 'Nhà tôi có kế hoạch một trang', 'Tôi đã tự đánh giá cả khóa'],
 ['Buổi cuối: mỗi nhà nói 1 nếp đã giữ được. Không chấm điểm, không so sánh nhà nào hơn.',
  'Gửi góp ý cho daynentang.com qua trang Chia sẻ (người từ 18 tuổi), không ghi tên người học.'],
 [lb('Đã xác nhận', f'Phân tích gộp 148 nghiên cứu: người có quan hệ xã hội mạnh hơn có khả năng sống lâu hơn; đây là tương quan ({HL}).'),
  lb('Đã xác nhận', f'Phòng chống thiên tai theo "bốn tại chỗ", trong đó có lực lượng tại chỗ ({PCTT}).'),
  lb('Đánh giá chuyên môn', 'Vòng người có thể nhờ và kế hoạch một trang do daynentang.com soạn; chưa có thử nghiệm riêng.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tự học 15 phút mỗi ngày (bài 1)', 'Chỉ uống nước đun sôi (bài 2)', 'Rửa tay đủ 5 lúc (bài 3)', 'Bữa ăn đủ 3 nhóm (bài 4)',
         'Bếp thoáng, dầu hỏa cất đúng (bài 5)', 'Biết sơ cứu bỏng (bài 6)', 'Chơi giao – đáp với con (bài 7)', 'Kể chuyện, đếm với con (bài 8)',
         'Ghi thu chi, để dành nhỏ (bài 9)', 'Có túi khẩn cấp (bài 10)', 'Có kế hoạch một trang (bài 11)']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Sổ nền tảng không cần điện', 'Trang in cho khóa Nền tảng không cần điện: thẻ hỏi – đáp, nước uống, rửa tay, bữa ăn, rà soát lửa khói, sơ cứu, chơi với con, sách tự làm, thu chi, túi khẩn cấp, kế hoạch gia đình.',
f'''
<h1>Sổ nền tảng không cần điện</h1>
<p>Dùng cho khóa <a href="{U}">Nền tảng không cần điện</a>. In đen trắng, một lần. Trang không lưu dữ liệu của bạn. Giữ sổ trong túi ni lông, chỗ khô.</p>
{PRINT_ROW}
<h2>1. Vòng tự học (bài 1)</h2>
{lines(['Mục tiêu nhỏ tuần này', 'Giờ học cố định'])}
{table(['Ngày'] + DAYS, [['Tự kiểm ✓'] + [''] * 7, ['Số thẻ đúng'] + [''] * 7])}
<h2>2. Nước uống an toàn (bài 2)</h2>
<p>Để lắng → lọc qua vải → đun sôi sùng sục + 1 phút → cất can có nắp, rót ra khi dùng.</p>
{table(['Ngày'] + DAYS, [['Chỉ uống nước đun sôi ✓'] + [''] * 7])}
<h2>3. Rửa tay và tiêu chảy (bài 3)</h2>
{table(['Lúc rửa tay'] + DAYS, [[x] + [''] * 7 for x in ['Sau đi vệ sinh', 'Sau lau rửa cho bé', 'Trước khi nấu', 'Trước khi ăn', 'Trước khi cho con ăn']])}
<p><strong>Đi trạm y tế ngay:</strong> lả, ngủ li bì · mắt trũng · uống kém · có máu trong phân · tiêu chảy từ 14 ngày.</p>
<h2>4. Bữa ăn 3 ngày (bài 4)</h2>
{table(['Bữa', 'Tinh bột', 'Đạm', 'Rau quả'], [[f'Ngày {d} – {b}', '', '', ''] for d in (1, 2, 3) for b in ('trưa', 'tối')])}
<p>Đồ chín không để quá 2 giờ ở nhiệt độ phòng. Ăn lại thì đun sôi kỹ.</p>
<h2>5. Rà soát lửa, khói, dầu, đèn (bài 5)</h2>
{table(['Mục', '✓ / ✗', 'Sửa thế nào'], [[x, '', ''] for x in ['Bếp có chỗ thoát khói', 'Trẻ nhỏ chơi xa bếp', 'Dầu hỏa chai có nhãn, cất cao', 'Không có dầu trong chai nước', 'Nến, đèn có đế vững, xa màn', 'Xô cát hoặc nước gần bếp', 'Diêm, bật lửa cất cao']])}
<h2>6. Sơ cứu (bài 6)</h2>
<p><strong>Bỏng:</strong> nước mát đang chảy 20 phút · tháo nhẫn, vòng · không bôi đá, kem đánh răng, mỡ.</p>
<p><strong>Đi viện ngay:</strong> bất tỉnh, co giật · khó thở, tím tái · chảy máu ép chặt vẫn không cầm · đuối nước dù đã tỉnh · bỏng rộng, phồng rộp nhiều.</p>
{lines(['Trạm y tế gần nhất', 'Người có xe chở đi viện', 'Chỗ để túi sơ cứu'])}
<h2>7. Chơi với con (bài 7)</h2>
{table(['Ngày'] + DAYS, [['Chơi 10 phút ✓'] + [''] * 7, ['Con làm gì mới'] + [''] * 7])}
<h2>8. Chữ và số cùng con (bài 8)</h2>
{table(['Ngày'] + DAYS, [['Kể chuyện ✓'] + [''] * 7, ['Đếm đồ thật ✓'] + [''] * 7])}
<h2>9. Thu chi 7 ngày (bài 9)</h2>
{table(['Ngày', 'Tiền vào', 'Tiền ra', 'Cho việc gì'], [[d, '', '', ''] for d in DAYS] + [['Cộng', '', '', '']])}
{lines(['Khoản chọn bớt', 'Khoản để riêng mỗi lần có tiền'])}
<h2>10. Túi khẩn cấp (bài 10)</h2>
{table(['Đồ', '✓', 'Đồ', '✓'], [['Nước uống', '', 'Áo mưa, áo ấm', ''], ['Đồ ăn khô', '', 'Còi', ''], ['Đèn pin, pin', '', 'Ít tiền lẻ', ''], ['Thuốc đang dùng', '', 'Giấy tờ (bọc ni lông)', ''], ['Đồ sơ cứu', '', 'Tã, sữa cho bé', '']])}
{lines(['Chỗ để túi', 'Chỗ sơ tán của thôn', 'Người cần giúp khi sơ tán – ai lo'])}
<h2>11. Kế hoạch gia đình một trang (bài 11)</h2>
{table(['Vòng', 'Người hoặc nơi', 'Cách liên lạc'], [['Trong', '', ''], ['Giữa', '', ''], ['Giữa', '', ''], ['Ngoài', '', ''], ['Ngoài', '', '']])}
{lines(['Khi có chuyện, cả nhà gặp nhau ở', 'Người đón con khi bố mẹ vắng', 'Ai lo người già, người ốm', 'Số gọi: 115 · 114 · 113 · 111 · trưởng thôn ……'])}
<h2>Tự đánh giá đầu và cuối khóa</h2>
<p>0 = chưa làm · 1 = làm được một phần · 2 = làm đều, thành nếp.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Trước bài 1</th><th>Sau bài 11</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Sổ để tự theo dõi. Không thay thế khám bệnh hay chỉ dẫn của chính quyền khi có thiên tai.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Nền tảng không cần điện', 'Khóa tự học miễn phí, in một lần, dùng không cần điện: tự học bằng giấy bút, nước uống an toàn, rửa tay, ăn đủ, lửa khói, sơ cứu, chơi và học với con, thu chi, bão lũ, người có thể nhờ.',
f'''
<p class="eyebrow">Cá nhân · Khóa C10 · Đang thử nghiệm</p>
<h1>Nền tảng không cần điện</h1>
<p class="lead">Mười một bài in ra là dùng được, kể cả khi không có điện, mạng hay màn hình.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Gia đình ở nơi thiếu điện, nước, trường học có những nếp nền tảng giữ sức khỏe, an toàn, học tập và tiền bạc, chỉ với giấy bút và đồ sẵn có</td></tr>
<tr><th>Dành cho</th><td>Bố mẹ ở vùng xa, vùng khó khăn (mỗi bài có phần làm cùng con) và người tự học từ 15 tuổi. Bạn 15–17 tuổi học cùng người lớn tin cậy. Thầy cô, cán bộ thôn, hội phụ nữ có thể in và dạy lại</td></tr>
<tr><th>Thời lượng</th><td>11 bài, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, ghi lại 5 phút</td></tr>
<tr><th>Cần có</th><td>Bản in (một người có điện in giúp), giấy, bút, đồ sẵn có trong nhà. Không cần điện, mạng hay màn hình</td></tr>
<tr><th>Tình trạng</th><td>Đủ 11 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của nhân viên y tế xã, giáo viên mầm non, cán bộ phòng chống thiên tai</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Cả nhà uống nước đã đun sôi, rửa tay với xà phòng đúng lúc.</li><li>Bạn biết sơ cứu bỏng và lúc nào phải đi viện.</li><li>Mỗi ngày có 10 phút chơi, kể chuyện với con.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: thiếu thốn vẫn tự học, tự lo được từng bước nhỏ; nhờ giúp và giúp lại là sức mạnh.</li><li>Kỹ năng: vòng tự học, giữ nước và đồ ăn sạch, để dành trước, chuẩn bị trước thiên tai.</li><li>Một Sổ nền tảng và kế hoạch gia đình dùng nhiều năm.</li></ul></div>
</div>
{figure_block('KHOAZ')}

<h2 id="muoi-mot-bai">Mười một bài</h2>
<div class="table-wrap"><table>
<thead><tr><th>Bài</th><th>Tên</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ nền tảng không cần điện</a>: in đen trắng một lần; có bảng theo dõi cho cả 11 bài, túi khẩn cấp, kế hoạch gia đình một trang và tự đánh giá đầu – cuối khóa.</li></ul>

<h2>Cho người in và dạy lại</h2>
<ul>
<li>In mỗi hộ một bộ, hoặc in một bộ cho nhóm đọc chung.</li>
<li>Gặp nhau mỗi tuần 30–45 phút ở nhà văn hóa, trường, nhà ai đó. Cùng làm phần "Làm".</li>
<li>Người không biết chữ: đọc to cho họ nghe; sổ ghi bằng hình và gạch đếm.</li>
<li>Bài 3, 6, 10 nên mời nhân viên y tế xã, cán bộ phòng chống thiên tai cùng dạy.</li>
<li>Không thu tiền, không bán hàng, không chụp ảnh trẻ em trong buổi học.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{BOIL}; {CDCW}; {HWTS}</td><td>Đun sôi, trữ nước có nắp</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn kỹ thuật WHO, CDC</td></tr>
<tr><td>{HW}; {WDIA}</td><td>Rửa tay với xà phòng; oresol, kẽm, dấu hiệu nặng</td><td><span class="label">[Đã xác nhận]</span> Tổng quan Cochrane (cộng đồng: giảm khoảng 29% đợt tiêu chảy, bằng chứng mức vừa); tờ thông tin WHO</td></tr>
<tr><td>{FOOD}</td><td>Giữ đồ ăn không cần tủ lạnh</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn WHO</td></tr>
<tr><td>{HAP}</td><td>Bớt khói, cất dầu hỏa</td><td><span class="label">[Đã xác nhận]</span> Tờ thông tin WHO</td></tr>
<tr><td>{BURN}; {DROWN}</td><td>Sơ cứu bỏng, cứu đuối</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn bệnh viện nhi, thư viện y khoa Hoa Kỳ</td></tr>
<tr><td>{HARV}; {JAM}; {REACH}</td><td>Chơi giao – đáp, đồ chơi tự làm (chỉ mượn ý)</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm Jamaica theo dõi 20 năm (105 người, có người thăm nhà)</td></tr>
<tr><td>{NOBLE}; {READ}</td><td>Kể chuyện, đọc cùng con</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp: tác dụng nhỏ (g = 0,19)</td></tr>
<tr><td>{CFPB_BB}; {CFPB_SAVE}</td><td>Ghi thu chi, để dành nhỏ</td><td><span class="label">[Đánh giá chuyên môn]</span> Khung của cơ quan bảo vệ người tiêu dùng Hoa Kỳ</td></tr>
<tr><td>{READY}; {PCTT}</td><td>Túi khẩn cấp, sơ tán</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn FEMA; luật Việt Nam</td></tr>
<tr><td>{DUN}; {HL}</td><td>Tự kiểm bằng thẻ; người có thể nhờ</td><td><span class="label">[Đã xác nhận]</span> Tổng quan; phân tích gộp 148 nghiên cứu (tương quan)</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Khóa ghép từ hướng dẫn của cơ quan y tế, an toàn và vài chương trình đã thử nghiệm. Các chương trình đó thường có người hướng dẫn. Khóa tự học này chưa được thử, nên chúng tôi không hứa kết quả.</p>
  <p>Khóa không thay thế khám, chữa bệnh, hay chỉ dẫn của chính quyền khi có thiên tai. Nguồn nước nghi nhiễm hóa chất: hỏi trạm y tế.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trẻ dưới 3 tuổi: bỏ mọi vật lọt ống giấy vệ sinh; nước, ao, xô luôn có người lớn sát bên.</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C10 built')
