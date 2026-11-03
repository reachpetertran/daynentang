# Khóa C5 "15 phút mỗi ngày" – trang khóa, 20 bài, công cụ "Sổ 15 phút".
# Người đọc gồm người lao động 15–17 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c5  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/15-phut-moi-ngay/'
TOOL = '/cong-cu/so-15-phut/'
C4U = '/khoa-hoc/vung-nghe/'
G2U = '/khoa-hoc/gia-dinh-0-2/'
G4U = '/khoa-hoc/gia-dinh-10-14/'
G6U = '/khoa-hoc/tien-nha-minh/'
BTC = '/cong-cu/bang-thu-chi/'
THK = '<a href="https://tamhonkhoe.com/">tamhonkhoe.com</a>'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
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
def selftab(items, a='Hôm nay', b='Sau 7 ngày'):
    rows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in items)
    return ('<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>'
            f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>{a}</th><th>{b}</th></tr></thead><tbody>{rows}</tbody></table></div>')
DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']

# ---------- Nguồn (đã tra 03/11/2026) ----------
GS = '<a href="https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f">Gollwitzer &amp; Sheeran 2006</a>'
NSLEEP = '<a href="https://cdc.gov/niosh/bulletin/2012/sleep-and-work.html">NIOSH – Sleep and Work (8/3/2012)</a>'
AASMA = '<a href="https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf">AASM và SRS 2015, <em>J Clin Sleep Med</em> 11(6)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
FOOD = '<a href="https://www.paho.org/en/news/21-12-2015-pahowho-recommends-five-keys-safer-food-healthy-holiday-season">Năm chìa khóa an toàn thực phẩm của WHO (PAHO/WHO)</a>'
HEATI = '<a href="https://elcosh.org/document/1262/d001135/Protecting%2BWorkers%2Bfrom%2BHeat%2BIllness%253A%2BOSHANIOSH%2BInfosheet.html">OSHA/NIOSH – Protecting Workers from Heat Illness</a>'
HEAT = '<a href="https://www.who.int/news/item/22-08-2025-who-wmo-issue-new-report-and-guidance-to-protect-workers-from-increasing-heat-stress">WHO và WMO, 22/8/2025</a>'
MICRO = '<a href="https://pubmed.ncbi.nlm.nih.gov/36044424/">Albulescu et al. 2022, <em>PLOS ONE</em></a>'
WHOPA = '<a href="https://who.int/initiatives/behealthy/physical-activity">WHO – Be Healthy: vận động</a>'
ILO = '<a href="https://www.ilo.org/node/653131">ILO – Improving the Safety and Health of Young Workers (2018)</a>'
WHOH = '<a href="https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss">WHO – Điếc và giảm thính lực (3/3/2026)</a>'
ATVS = '<a href="https://danchuphapluat.vn/quyen-tu-choi-lam-viec-khi-phat-hien-nguy-co-gay-chay-no-de-doa-tinh-mang-9563.html">Luật An toàn, vệ sinh lao động 84/2015/QH13, Điều 6 khoản 1 điểm đ (báo Dân chủ &amp; Pháp luật tóm tắt)</a>'
LDCTN = '<a href="https://lsvn.vn/quy-dinh-ve-su-dung-lao-dong-la-nguoi-chua-thanh-nien1666196792-a125368.html">Bộ luật Lao động 2019, Điều 143–147 (Báo Luật sư Việt Nam, 19/10/2022)</a>'
D17 = '<a href="https://hethongphapluat.com/bo-luat-lao-dong-2019/khoan-1-dieu-17">Bộ luật Lao động 2019, Điều 17 khoản 1</a>'
D8 = '<a href="https://daibieunhandan.vn/nhung-hanh-vi-nao-bi-nghiem-cam-trong-linh-vuc-lao-dong-nam-2024-10338504.html">Bộ luật Lao động 2019, Điều 8 (báo Đại biểu Nhân dân tóm tắt, 3/6/2024)</a>'
D95 = '<a href="https://thuvienphapluat.vn/lao-dong-tien-luong/phieu-luong-la-gi-cong-ty-tra-luong-phai-co-phieu-luong-co-dung-khong-41331.html">Bộ luật Lao động 2019, Điều 95 khoản 3 (Thư viện Pháp luật, 18/5/2025)</a>'
LVL = '<a href="https://luatvietnam.vn/lao-dong-tien-luong/diem-moi-cua-luat-viec-lam-2025-562-102940-article.html">Luật Việc làm 74/2025/QH15, Điều 26 (LuatVietnam tóm tắt)</a>'
DUN = '<a href="https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html">Dunlosky et al. 2013 (thông cáo của APS)</a>'
CEP = '<a href="https://pubmed.ncbi.nlm.nih.gov/16719566/">Cepeda et al. 2006, <em>Psychological Bulletin</em> 132</a>'
BLDS = '<a href="https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam">Bộ luật Dân sự 2015, Điều 468</a>'
LUA = '<a href="https://hatinh.gov.vn/vi/bai-viet/nhung-dau-hieu-canh-bao-lua-dao-viec-lam-nguoi-lao-dong-can-biet">Dấu hiệu lừa đảo việc làm (VOV, đăng lại trên Cổng TTĐT Hà Tĩnh, 1/2/2025)</a>'
DWM = '<a href="https://who.int/publications/i/item/9789240003927">WHO – Doing What Matters in Times of Stress (2020, có bản tiếng Việt)</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'
T111 = '<a href="https://tongdai111.vn/">tongdai111.vn</a>'
HARV = '<a href="https://bettercarenetwork.org/sites/default/files/HCDC_ServeReturn_for_Parents_Caregivers_2019.pdf">Harvard – Serve and Return for Parents (2019)</a>'
HL = '<a href="https://www.rti.org/publication/social-relationships-mortality-risk-meta-analytic-review">Holt-Lunstad et al. 2010, <em>PLoS Medicine</em></a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài viết chưa được cán bộ an toàn lao động, nhân viên y tế hay luật sư duyệt. Phần luật chỉ là thông tin chung, không phải tư vấn pháp lý.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Những gì bạn viết là của riêng bạn. '
           'Tổ trưởng, gia đình (từ 18 tuổi) có thể góp ý ở trang <a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên hay nơi làm.</p>')
TALK = ('Tai nạn, sốc nhiệt, người bị thương nặng: gọi <strong>115</strong>. Cháy nổ: <strong>114</strong>. Bị đe dọa, ép buộc: <strong>113</strong>. '
        'Dưới 18 tuổi bị ép làm việc nguy hiểm, bị đánh, bị xâm hại: <strong>111</strong> (miễn phí, 24/7). Buồn, lo kéo dài: Ngày Mai <strong>096 306 1414</strong>.')

TITLES = [
 ('gio-cua-minh', '15 phút của mình'), ('ngu-du-khi-lam-ca', 'Ngủ đủ khi làm ca'), ('an-uong-khi-lam-ca', 'Ăn, uống khi làm ca'),
 ('nghi-ngan-gian-co', 'Nghỉ ngắn, giãn cơ'), ('lam-viec-khi-nong', 'Làm việc khi trời nóng'),
 ('nhan-ra-nguy-co', 'Nhận ra nguy cơ'), ('do-bao-ho-tieng-on', 'Đồ bảo hộ và tiếng ồn'), ('dung-viec-va-bao-cao', 'Dừng việc nguy hiểm, báo cáo'),
 ('on-de-nho-lau', 'Học 15 phút, nhớ lâu'), ('len-mot-bac', 'Lên một bậc trong nghề'),
 ('luong-di-dau', 'Tiền đi đâu?'), ('chia-luong', 'Chia lương, đọc phiếu lương'), ('tranh-bay-tien', 'Tránh bẫy tiền và bẫy việc làm'),
 ('chu-tin', 'Chữ tín ở chỗ làm'), ('tu-te-noi-lam', 'Tử tế nơi làm việc'),
 ('goi-ten-cam-xuc', 'Gọi tên cảm xúc, thở chậm'), ('khi-qua-tai', 'Khi quá tải, khi nào cần giúp'), ('gan-con-khi-o-xa', 'Gần con khi ở xa'),
 ('nguoi-co-the-nho', 'Người có thể nhờ'), ('xem-lai-bon-tuan', 'Xem lại bốn tuần, giữ thói quen')]
WEEKS = ['Chăm thân', 'An toàn và học nghề', 'Tiền và chữ tín', 'Tâm trí và gia đình']
L = {str(i + 1): ((i // 5) + 1, (i % 5) + 1, slug, f'Bài {i + 1}', title) for i, (slug, title) in enumerate(TITLES)}
ORDER = list(L)
def link(k):
    w, d, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, goals, prep, read, do, note, safety, selfq, adult, src, figs_after=3):
    w, d, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Tuần {w} · Ngày {d}', 'Đọc 5 phút', 'Làm 7 phút', 'Ghi lại 3 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (1 phút)', ul(prep)),
        sec(3, 'Đọc (5 phút)', ol(read)),
        sec(4, 'Làm (7 phút)', do),
        sec(5, 'Ghi lại (3 phút)', note),
        sec(6, 'An toàn', ul(safety + [TALK])),
        sec(7, 'Tự đánh giá', selftab(selfq)),
        sec(8, 'Cho tổ trưởng, người kèm cặp, gia đình', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">15 phút mỗi ngày</a> · Tuần {w}: {WEEKS[w-1]}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('F' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

def note3(q): return lines(q)

# ======================= TUẦN 1: CHĂM THÂN =======================
lesson('1', 'Khóa 15 phút mỗi ngày, bài 1: chọn giờ và chỗ cố định cho 15 phút tự học, viết kế hoạch Nếu… thì…, bắt đầu Sổ 15 phút.',
 ['Chọn <strong>giờ và chỗ cố định</strong> cho 15 phút mỗi ngày.',
  'Viết <strong>1 kế hoạch Nếu… thì…</strong> gắn với việc bạn đã làm hằng ngày.',
  'Đánh dấu <strong>5/5 ngày</strong> trong tuần này.'],
 [f'In trang 1 của <a href="{TOOL}">Sổ 15 phút</a>, hoặc lấy một tờ giấy và cây bút.'],
 ['<strong>Khóa này dành cho người bận.</strong> Mỗi ngày 15 phút, thứ Hai đến thứ Sáu, trong 4 tuần. Nghỉ cuối tuần.',
  '<strong>Ý định chung chung dễ quên.</strong> "Mình sẽ cố gắng" thường không thành việc làm khi đã mệt sau ca.',
  '<strong>Kế hoạch Nếu… thì…</strong> nói rõ lúc nào, ở đâu, làm gì. Ví dụ: "Nếu tắm xong sau ca, thì mình ngồi bàn đọc 1 bài."',
  '<strong>Gắn vào việc có sẵn.</strong> Việc có sẵn (tắm, ăn cơm, gọi về nhà) là cái móc để việc mới bám vào.',
  '<strong>Đổi ca thì đổi móc, không đổi việc.</strong> Ca ngày và ca đêm có thể có hai kế hoạch khác nhau.'],
 '<p><strong>Kế hoạch của tôi.</strong></p>'
 + lines(['Giờ (ca ngày)', 'Giờ (ca đêm, nếu có)', 'Chỗ ngồi', 'Nếu … (việc có sẵn)', 'thì … (15 phút làm gì)', 'Nếu bị cản (mệt, có việc) thì …'])
 + table(['Tuần 1'] + DAYS[:5], [['Đã làm ✓'] + [''] * 5]),
 note3(['Điều làm mình dễ bỏ nhất là', 'Cách mình sẽ xử lý là']),
 ['Chọn giờ không trùng lúc lái xe, đi đường hay đang làm việc với máy.', 'Mệt quá: đọc 5 phút cũng được, đừng bỏ hẳn.'],
 ['Tôi có giờ và chỗ cố định', 'Tôi có 1 kế hoạch Nếu… thì…', 'Tôi đánh dấu được 5/5 ngày'],
 ['Tổ trưởng có thể dành 15 phút đầu giờ hoặc giữa ca cho cả tổ cùng đọc một bài.', 'Gia đình: hỏi "Hôm nay học bài gì?", không hỏi "Sao chưa học?".'],
 [lb('Đã xác nhận', f'Tổng hợp nhiều nghiên cứu cho thấy kế hoạch Nếu… thì… giúp người ta thực hiện điều đã định nhiều hơn so với chỉ có ý định ({GS}).'),
  lb('Suy luận', 'Các nghiên cứu chủ yếu ở nước phương Tây, nhiều nghiên cứu với sinh viên. Chưa có nghiên cứu riêng với công nhân Việt Nam.'),
  lb('Đánh giá chuyên môn', 'Nhịp 15 phút × 5 ngày × 4 tuần do daynentang.com chọn để vừa với lịch làm ca.')])

lesson('2', 'Khóa 15 phút mỗi ngày, bài 2: ngủ đủ khi làm ca, chuẩn bị chỗ ngủ ban ngày tối, yên, mát, ghi giờ ngủ 3 ngày.',
 ['Biết người lớn cần ngủ <strong>ít nhất 7 giờ</strong> mỗi ngày.',
  'Làm <strong>1 thay đổi</strong> cho chỗ ngủ hoặc giờ ngủ.',
  'Ghi <strong>giờ ngủ 3 ngày</strong> liền.'],
 ['Sổ 15 phút, trang giấc ngủ.', 'Nghĩ về chỗ bạn ngủ: sáng hay tối, ồn hay yên, nóng hay mát.'],
 ['<strong>Người lớn cần ngủ ít nhất 7 giờ</strong> mỗi ngày để giữ sức khỏe. Dưới 18 tuổi cần nhiều hơn.',
  '<strong>Thiếu ngủ làm phản xạ chậm</strong>, dễ sai, dễ tai nạn với máy và xe. Mệt mỏi là một mối nguy ở chỗ làm.',
  '<strong>Ngủ sau ca đêm:</strong> chỗ ngủ tối, yên, mát. Rèm dày, bịt mắt, nút tai, quạt giúp được nhiều.',
  '<strong>Trước khi ngủ:</strong> không ăn no nặng, không rượu bia. Ngưng cà phê, trà đặc, nước tăng lực vài giờ trước khi ngủ.',
  '<strong>Giữ giờ ngủ gần giống nhau</strong> trong các ngày cùng ca. Báo người nhà giờ ngủ của mình để họ giữ yên.'],
 '<p><strong>Giờ ngủ 3 ngày.</strong></p>'
 + table(['Ngày', 'Ca', 'Giờ lên giường', 'Giờ dậy', 'Số giờ ngủ', 'Thức giấc vì'], [['', '', '', '', '', ''] for _ in range(3)])
 + lines(['Một thay đổi tôi làm tuần này (rèm, nút tai, giờ cà phê, báo người nhà…)']),
 note3(['Ngày ngủ đủ nhất, mình đã làm gì khác?']),
 ['Buồn ngủ khi lái xe: dừng ở chỗ an toàn, nghỉ, hoặc nhờ người khác đưa về.', 'Mất ngủ nhiều tuần, ngáy to, ngưng thở khi ngủ: đi khám.',
  'Không tự dùng thuốc ngủ khi chưa hỏi bác sĩ.'],
 ['Tôi biết mình cần ngủ bao nhiêu', 'Tôi làm 1 thay đổi cho giấc ngủ', 'Tôi ghi giờ ngủ 3 ngày'],
 ['Tổ trưởng: chú ý người ngáp nhiều, mắt đỏ khi đứng máy; cho nghỉ ngắn hoặc đổi việc an toàn hơn.',
  'Gia đình: giữ nhà yên vào giờ người làm ca đêm ngủ.'],
 [lb('Đã xác nhận', f'Người lớn nên ngủ ít nhất 7 giờ mỗi đêm ({AASMA}). Trẻ 13–18 tuổi: 8–10 giờ ({AASM}).'),
  lb('Đã xác nhận', f'NIOSH khuyên người làm ca: dành đủ thời gian ngủ sau ca; ngủ nơi tối, yên, mát; tránh ăn nặng, rượu và chất kích thích trước khi ngủ ({NSLEEP}).'),
  lb('Đánh giá chuyên môn', 'Lời khuyên dừng xe khi buồn ngủ, mẫu ghi giờ ngủ do daynentang.com soạn.')])

lesson('3', 'Khóa 15 phút mỗi ngày, bài 3: uống nước đủ khi làm ca, hộp cơm an toàn theo năm chìa khóa của WHO.',
 ['Mang theo <strong>nước uống</strong> mỗi ca và uống trước khi khát.',
  'Chuẩn bị <strong>hộp cơm</strong> theo 5 chìa khóa an toàn thực phẩm.',
  'Đánh dấu <strong>5 ngày</strong> có đủ nước.'],
 ['Chai nước của bạn.', 'Nghĩ về bữa ăn trong ca: tự nấu, mua, hay ăn ở căng tin.'],
 ['<strong>Uống ít một, nhiều lần</strong>, trước khi khát. Khát là lúc cơ thể đã thiếu nước.',
  '<strong>Xem màu nước tiểu:</strong> trong hoặc vàng nhạt là đủ nước. Vàng đậm: uống thêm.',
  '<strong>Hộp cơm an toàn:</strong> giữ sạch; tách đồ sống và chín; nấu chín kỹ; giữ lạnh hoặc hâm nóng kỹ; dùng nước và đồ ăn sạch.',
  '<strong>Cơm canh để lâu ở nhiệt độ phòng</strong> dễ hỏng, nhất là trời nóng. Ăn sớm hoặc giữ trong túi giữ lạnh.',
  '<strong>Làm ca đêm:</strong> ăn bữa nhẹ hơn vào nửa đêm. Ăn no nặng sát giờ ngủ làm khó ngủ.'],
 '<p><strong>Kế hoạch nước và cơm.</strong></p>'
 + lines(['Chai nước của tôi (dung tích), đổ đầy mấy lần mỗi ca', 'Hộp cơm: món, giữ lạnh bằng gì, ăn lúc mấy giờ', 'Một việc tôi đổi để hộp cơm an toàn hơn'])
 + table(['Tuần 1'] + DAYS[:5], [['Đủ nước ✓'] + [''] * 5]),
 note3(['Ngày nào khó uống đủ nước, vì sao?']),
 ['Đồ ăn có mùi lạ, chua, nhớt: bỏ, không tiếc.', 'Tiêu chảy, nôn sau bữa ăn chung ở chỗ làm: báo y tế cơ quan để kiểm tra cả bếp.',
  'Có bệnh thận, tim, đang uống thuốc lợi tiểu: hỏi bác sĩ lượng nước phù hợp.'],
 ['Tôi mang nước mỗi ca', 'Tôi uống trước khi khát', 'Hộp cơm của tôi theo 5 chìa khóa'],
 ['Tổ trưởng: để nước uống ở chỗ dễ thấy, gần nơi làm.', 'Gia đình: cùng chuẩn bị hộp cơm, có hộp kín và túi giữ lạnh.'],
 [lb('Đã xác nhận', f'Năm chìa khóa an toàn thực phẩm của WHO: giữ sạch, tách sống – chín, nấu chín kỹ, giữ thực phẩm ở nhiệt độ an toàn, dùng nước và nguyên liệu an toàn ({FOOD}).'),
  lb('Đã xác nhận', f'OSHA/NIOSH: uống ít mà thường, trước khi khát; nước tiểu trong hoặc vàng nhạt cho thấy đủ nước ({HEATI}).'),
  lb('Đánh giá chuyên môn', 'Lời khuyên ăn nhẹ khi làm ca đêm là cách làm phổ biến, chúng tôi chưa tra nghiên cứu riêng.')])

lesson('4', 'Khóa 15 phút mỗi ngày, bài 4: nghỉ ngắn giữa ca, năm động tác giãn cơ nhẹ cho cổ, vai, cổ tay, lưng, bắp chân.',
 ['Làm <strong>5 động tác giãn cơ</strong> trong 5 phút.',
  'Có <strong>2 lần nghỉ ngắn</strong> mỗi ca, khi được phép.',
  'Biết khuyến nghị vận động <strong>150–300 phút</strong> mỗi tuần cho người lớn.'],
 ['Một khoảng trống đủ đứng duỗi tay.', 'Biết giờ nghỉ của chỗ làm.'],
 ['<strong>Ngồi hay đứng một tư thế lâu</strong> làm mỏi cổ, vai, lưng, cổ tay. Nghỉ ngắn và đổi tư thế giúp đỡ mỏi.',
  '<strong>Nghỉ ngắn có tác dụng nhỏ nhưng có thật:</strong> tỉnh táo hơn, bớt mệt. Năng suất chung chưa rõ.',
  '<strong>Năm động tác, mỗi động tác khoảng 1 phút:</strong> nghiêng cổ chậm; xoay vai; duỗi cổ tay; vươn người ưỡn nhẹ; kiễng gót.',
  '<strong>Làm chậm, nhẹ, thở đều.</strong> Căng nhẹ là được. Đau nhói là phải dừng.',
  '<strong>Ngoài giờ làm:</strong> người lớn nên vận động vừa sức 150–300 phút mỗi tuần. Đi bộ nhanh 30 phút, 5 ngày là đủ mức thấp.'],
 '<p><strong>Tập ngay 5 động tác</strong> (đếm chậm 10 nhịp mỗi bên).</p>'
 + table(['Động tác', 'Làm được', 'Chỗ nào còn mỏi'], [['Cổ', '', ''], ['Vai', '', ''], ['Cổ tay', '', ''], ['Lưng', '', ''], ['Bắp chân', '', '']])
 + lines(['Lần nghỉ ngắn 1 (giờ)', 'Lần nghỉ ngắn 2 (giờ)', 'Vận động ngoài giờ tuần này (phút)']),
 note3(['Sau khi giãn cơ, mình thấy thế nào?']),
 ['Không giãn cơ khi đang đứng máy, đang cầm dụng cụ, gần xe nâng.', 'Đau lưng lan xuống chân, tê, yếu tay chân: đi khám.',
  'Mới bị thương, mới mổ, đang mang thai: hỏi nhân viên y tế trước khi tập.'],
 ['Tôi làm được 5 động tác', 'Tôi có 2 lần nghỉ ngắn mỗi ca', 'Tôi vận động ngoài giờ ít nhất 3 lần/tuần'],
 ['Tổ trưởng: cho cả tổ giãn cơ 5 phút đầu ca, ở chỗ an toàn.', 'Gia đình: rủ nhau đi bộ buổi tối.'],
 [lb('Đã xác nhận', f'Tổng hợp 22 mẫu, 2.335 người: nghỉ ngắn tăng cảm giác sảng khoái (d = 0,36) và giảm mệt (d = 0,35); hiệu suất chung chưa có ý nghĩa thống kê ({MICRO}).'),
  lb('Đã xác nhận', f'WHO khuyến nghị người lớn vận động thể lực vừa 150–300 phút mỗi tuần ({WHOPA}).'),
  lb('Đánh giá chuyên môn', 'Năm động tác giãn cơ là bài tập nhẹ thông dụng, do daynentang.com chọn; chưa được chuyên gia vật lý trị liệu duyệt.')])

lesson('5', 'Khóa 15 phút mỗi ngày, bài 5: làm việc khi trời nóng, uống nước, nghỉ mát, nhận ra kiệt sức vì nóng và sốc nhiệt.',
 ['Nói được <strong>dấu hiệu kiệt sức vì nóng</strong> và <strong>dấu hiệu sốc nhiệt</strong>.',
  'Biết <strong>3 việc làm ngay</strong> khi có người sốc nhiệt.',
  'Có <strong>kế hoạch nước và nghỉ mát</strong> cho ngày nóng.'],
 ['Nghĩ về chỗ làm nóng nhất của bạn.'],
 ['<strong>Nóng làm giảm sức và năng suất.</strong> WHO và WMO cho biết trên 20°C, mỗi độ tăng thêm làm năng suất giảm 2–3%.',
  '<strong>Uống ít mà thường:</strong> làm việc vừa sức trong nóng vừa, khoảng 1 cốc (khoảng 240 ml) mỗi 15–20 phút.',
  '<strong>Người mới hoặc nghỉ hơn 1 tuần</strong> cần tăng việc dần, nghỉ nhiều hơn trong tuần đầu.',
  '<strong>Kiệt sức vì nóng:</strong> đau đầu, chóng mặt, buồn nôn, yếu, khát, ra nhiều mồ hôi. Vào chỗ mát, uống nước, báo tổ trưởng.',
  '<strong>Sốc nhiệt là cấp cứu:</strong> lú lẫn, ngất, co giật, người rất nóng. Gọi 115, đưa vào bóng mát, làm mát bằng nước, ở cạnh chờ.'],
 '<p><strong>Kế hoạch ngày nóng.</strong></p>'
 + lines(['Chỗ lấy nước gần nhất', 'Chỗ mát để nghỉ', 'Người tôi báo khi thấy mệt vì nóng'])
 + table(['Dấu hiệu', 'Kiệt sức vì nóng', 'Sốc nhiệt'], [['Đầu óc', 'tỉnh, đau đầu', 'lú lẫn, ngất, co giật'], ['Làm gì', 'nghỉ mát, uống nước, báo', 'gọi 115, làm mát, ở cạnh']]),
 note3(['Ở chỗ làm, giờ nào nóng nhất? Mình đổi được gì?']),
 ['Người lú lẫn, không uống được: không ép uống, gọi 115 ngay.', 'Không uống rượu bia để "giải nhiệt".',
  'Không làm một mình ở chỗ rất nóng; có người kiểm tra nhau.'],
 ['Tôi phân biệt được hai mức nguy hiểm', 'Tôi biết 3 việc làm ngay khi sốc nhiệt', 'Tôi uống nước đều trong ngày nóng'],
 ['Tổ trưởng: để nước mát gần chỗ làm, cho nghỉ trong bóng mát, ghép đôi người mới với người quen việc.',
  'Ghi số 115 ở bảng thông báo của tổ.'],
 [lb('Đã xác nhận', f'WHO và WMO: năng suất người lao động giảm 2–3% cho mỗi độ trên 20°C; nóng gây say nắng, mất nước, tổn thương thận ({HEAT}).'),
  lb('Đã xác nhận', f'OSHA/NIOSH: khoảng 1 cốc mỗi 15–20 phút khi làm vừa sức trong nóng vừa; người mới cần tăng việc dần; dấu hiệu và sơ cứu kiệt sức vì nóng, sốc nhiệt ({HEATI}).'),
  lb('Suy luận', 'Hướng dẫn OSHA/NIOSH viết cho Hoa Kỳ; nguyên tắc sơ cứu dùng được ở Việt Nam, số cấp cứu là 115.')])

# ======================= TUẦN 2: AN TOÀN VÀ HỌC NGHỀ =======================
lesson('6', 'Khóa 15 phút mỗi ngày, bài 6: năm câu hỏi trước việc mới, săn sáu mối nguy thường gặp ở chỗ làm.',
 ['Hỏi đủ <strong>5 câu</strong> trước một việc mới.',
  'Tìm <strong>3 mối nguy</strong> ở chỗ làm của mình và cách phòng.'],
 [f'Sổ 15 phút, trang an toàn. Có thể học sâu hơn ở khóa <a href="{C4U}">Vững nghề</a>.'],
 ['<strong>Người lao động trẻ dễ bị tai nạn hơn.</strong> ILO cho biết người 15–24 tuổi bị tai nạn lao động không chết người cao hơn tới 40%.',
  '<strong>Lý do thường gặp:</strong> mới vào, chưa quen việc, ngại hỏi, muốn làm nhanh cho kịp.',
  '<strong>Năm câu hỏi trước việc mới:</strong> có thể bị thương ra sao? cần đồ bảo hộ gì? đã được hướng dẫn chưa? sự cố thì làm gì? hỏi ai?',
  '<strong>Sáu mối nguy hay gặp:</strong> trơn, vấp, ngã; vật rơi, vật đè; máy quay, cuốn; điện; hóa chất, bụi; ồn, nóng.',
  '<strong>Thấy nguy, báo ngay.</strong> Báo sớm rẻ hơn sửa sau tai nạn.'],
 '<p><strong>Săn mối nguy ở chỗ làm.</strong></p>'
 + table(['Mối nguy tôi thấy', 'Có thể gây ra gì?', 'Cách phòng', 'Đã báo ai?'], [['', '', '', ''] for _ in range(3)]),
 note3(['Câu hỏi nào trong 5 câu mình hay quên nhất?']),
 ['Chỉ dùng máy, dụng cụ đã được hướng dẫn và cho phép.', 'Không tháo che chắn máy, không chạm vào máy đang chạy để gỡ kẹt.'],
 ['Tôi hỏi đủ 5 câu trước việc mới', 'Tôi tìm được 3 mối nguy', 'Tôi đã báo ít nhất 1 mối nguy'],
 ['Tổ trưởng: khen người hỏi và người báo mối nguy, kể cả khi đó là báo nhầm.', 'Dành 5 phút đầu ca nói về một mối nguy.'],
 [lb('Đã xác nhận', f'ILO: người lao động 15–24 tuổi có tỉ lệ tai nạn lao động không chết người cao hơn tới 40% so với người lớn tuổi hơn ({ILO}).'),
  lb('Đánh giá chuyên môn', 'Năm câu hỏi và sáu nhóm mối nguy do daynentang.com tóm gọn từ thực hành an toàn lao động; không thay huấn luyện an toàn bắt buộc của chỗ làm.')])

lesson('7', 'Khóa 15 phút mỗi ngày, bài 7: đồ bảo hộ đúng việc, phép thử 1 mét cho tiếng ồn, chăm sóc đồ bảo hộ.',
 ['Liệt kê <strong>đồ bảo hộ</strong> cho từng việc mình làm.',
  'Dùng <strong>phép thử 1 mét</strong> để biết chỗ nào có thể quá ồn.',
  'Dùng đủ đồ bảo hộ <strong>5/5 ngày</strong>.'],
 ['Đồ bảo hộ bạn đang có.'],
 ['<strong>Đồ bảo hộ là lớp chắn cuối cùng.</strong> Trước đó, chỗ làm phải giảm nguy hiểm từ máy và cách làm.',
  '<strong>Đúng việc, đúng cỡ, còn tốt.</strong> Găng rách, kính trầy mờ, khẩu trang ướt bảo vệ kém.',
  '<strong>Tiếng ồn lớn kéo dài làm giảm thính lực</strong>, và mất rồi thì khó lấy lại.',
  '<strong>Phép thử 1 mét:</strong> phải nói to mới nghe được người cách khoảng 1 mét, thì chỗ đó có thể quá ồn. Đeo nút tai, báo tổ trưởng.',
  '<strong>Nút tai phải đeo đúng:</strong> vê nhỏ, kéo vành tai, nhét sâu, giữ vài giây cho nở ra.'],
 '<p><strong>Đồ bảo hộ của tôi.</strong></p>'
 + table(['Việc', 'Đồ bảo hộ cần', 'Tôi có?', 'Còn tốt?'], [['', '', '', ''] for _ in range(4)])
 + table(['Tuần 2'] + DAYS[:5], [['Đủ bảo hộ ✓'] + [''] * 5]),
 note3(['Đồ bảo hộ nào mình hay bỏ, vì sao?', 'Mình sẽ làm gì để đeo đều hơn?']),
 ['Ù tai, nghe kém sau ca: báo y tế cơ quan, đi khám tai.', 'Hóa chất bắn vào mắt: rửa nước sạch liên tục, báo ngay, đi khám.',
  'Thiếu đồ bảo hộ: báo tổ trưởng, chưa làm việc đó.'],
 ['Tôi biết đồ bảo hộ cho từng việc', 'Tôi dùng phép thử 1 mét', 'Tôi đeo đủ 5/5 ngày'],
 ['Tổ trưởng: kiểm tra đồ bảo hộ đầu ca; đổi ngay đồ hỏng.', 'Làm mẫu: tổ trưởng đeo đủ trước.'],
 [lb('Đã xác nhận', f'Tiếng ồn lớn ở nơi làm việc là một nguyên nhân gây giảm thính lực; WHO khuyến nghị chương trình bảo vệ thính lực nghề nghiệp ({WHOH}).'),
  lb('Đánh giá chuyên môn', 'Phép thử 1 mét là mẹo ước lượng dùng trong an toàn lao động, không thay máy đo tiếng ồn.'),
  lb('Cần kiểm chứng', 'Giới hạn tiếng ồn theo quy chuẩn Việt Nam: chúng tôi chưa đọc văn bản gốc nên không ghi con số.')])

lesson('8', 'Khóa 15 phút mỗi ngày, bài 8: quyền dừng việc khi thấy rõ nguy cơ đe dọa tính mạng, báo cáo ba phần, báo cả suýt tai nạn.',
 ['Nói được khi nào được <strong>dừng việc nguy hiểm</strong> và phải làm gì sau đó.',
  'Tập <strong>báo cáo ba phần</strong>: thấy gì, ở đâu, đã làm gì.',
  'Biết <strong>giới hạn giờ làm</strong> của người dưới 18 tuổi.'],
 ['Tên người phụ trách an toàn hoặc tổ trưởng của bạn.'],
 ['<strong>Bạn có quyền từ chối hoặc rời chỗ làm</strong> khi thấy rõ nguy cơ xảy ra tai nạn đe dọa nghiêm trọng tính mạng, sức khỏe.',
  '<strong>Kèm theo là trách nhiệm:</strong> phải báo ngay cho người quản lý trực tiếp. Chờ xử lý xong mới làm lại.',
  '<strong>Báo cáo ba phần:</strong> thấy gì, ở đâu, đã làm gì. Ví dụ: "Dây điện máy 3 bị hở, em đã tắt máy."',
  '<strong>Suýt tai nạn cũng báo.</strong> Mỗi lần suýt là một lời cảnh báo cho cả tổ.',
  '<strong>Người 15–17 tuổi:</strong> làm tối đa 8 giờ/ngày, 40 giờ/tuần; không được làm một số việc nặng nhọc, nguy hiểm.'],
 '<p><strong>Tập nói câu dừng việc và báo cáo.</strong></p>'
 + lines(['Câu dừng việc: "Em thấy … có thể gây … Em dừng lại và báo anh/chị."', 'Người tôi báo', 'Báo cáo ba phần (thấy gì – ở đâu – đã làm gì) cho một tình huống giả định'])
 + '<p class="small">Tình huống giả định: sàn trơn dầu gần máy cắt; bình gas rò mùi trong bếp; giàn giáo lung lay.</p>',
 note3(['Điều gì làm mình ngại báo? Mình sẽ nói câu gì?']),
 ['Dừng việc an toàn: tắt máy theo đúng cách đã học, không bỏ chạy để máy chạy một mình nếu tắt được an toàn.',
  'Bị la mắng, đe dọa vì báo nguy hiểm: ghi lại, báo công đoàn hoặc người có trách nhiệm.'],
 ['Tôi biết khi nào được dừng việc', 'Tôi nói được báo cáo ba phần', 'Tôi biết giới hạn giờ cho người dưới 18'],
 ['Tổ trưởng: cảm ơn người báo, xử lý nhanh, kể lại cho cả tổ.', 'Gia đình có con 15–17 tuổi đi làm: hỏi giờ làm thực tế mỗi tuần.'],
 [lb('Đã xác nhận', f'Người lao động được từ chối làm hoặc rời bỏ nơi làm việc khi thấy rõ nguy cơ đe dọa nghiêm trọng tính mạng, sức khỏe, và phải báo ngay người quản lý trực tiếp ({ATVS}).'),
  lb('Đã xác nhận', f'Người 15 đến dưới 18 tuổi làm không quá 8 giờ/ngày, 40 giờ/tuần; có danh mục việc cấm ({LDCTN}).'),
  lb('Cần kiểm chứng', 'Chúng tôi đọc các điều luật qua trang tóm tắt, chưa đối chiếu nguyên văn. Đây không phải tư vấn pháp lý.'),
  'Quyền lao động chuyên sâu sẽ có ở trang chị em trachnhiemxahoi.com.'])

lesson('9', 'Khóa 15 phút mỗi ngày, bài 9: học 15 phút để nhớ lâu bằng tự hỏi – tự trả lời và ôn giãn cách.',
 ['Làm <strong>5 thẻ hỏi – đáp</strong> về việc mình đang học.',
  'Ôn theo lịch <strong>giãn cách</strong>: ngày 1, 2, 4, 8.'],
 ['5 mảnh giấy nhỏ, hoặc một trang sổ chia đôi.', 'Một thứ bạn muốn nhớ: quy trình máy, nội quy an toàn, từ tiếng Anh, bài lý thuyết nghề.'],
 ['<strong>Đọc lại nhiều lần</strong> cho cảm giác đã biết, nhưng nhớ không lâu.',
  '<strong>Tự hỏi rồi tự trả lời</strong> (che đáp án) giúp nhớ lâu hơn. Sai cũng có ích: biết chỗ cần ôn.',
  '<strong>Ôn giãn cách:</strong> ôn lại sau 1 ngày, rồi để cách xa dần. Ví dụ lịch: ngày 1, 2, 4, 8.',
  '<strong>Thẻ hỏi – đáp:</strong> mặt trước một câu hỏi, mặt sau câu trả lời ngắn. Bỏ túi, ôn lúc chờ ca.',
  '<strong>15 phút đều đặn</strong> mỗi ngày tốt hơn học dồn 2 giờ một lần.'],
 '<p><strong>Năm thẻ hỏi – đáp của tôi.</strong></p>'
 + table(['Câu hỏi (mặt trước)', 'Trả lời (mặt sau)', 'Ngày 1', 'Ngày 2', 'Ngày 4', 'Ngày 8'], [['', '', '', '', '', ''] for _ in range(5)]),
 note3(['Thẻ nào mình trả lời sai? Lần sau ôn thế nào?']),
 ['Không học bằng điện thoại khi đang đi đường, đang đứng máy.'],
 ['Tôi làm được 5 thẻ', 'Tôi tự hỏi trước khi xem đáp án', 'Tôi ôn đúng lịch giãn cách'],
 ['Tổ trưởng: soạn sẵn thẻ hỏi – đáp về quy trình an toàn của tổ.', 'Gia đình: hỏi bài giúp người học bằng thẻ.'],
 [lb('Đã xác nhận', f'Tự kiểm tra và ôn giãn cách được xếp hữu ích cao; đọc lại và tô màu được xếp thấp ({DUN}).'),
  lb('Đã xác nhận', f'Tổng hợp 317 thí nghiệm: ôn giãn cách giúp nhớ lâu hơn học dồn ({CEP}).'),
  lb('Suy luận', 'Phần lớn nghiên cứu làm với học sinh, sinh viên. Áp dụng cho người đi làm tự học là suy luận hợp lý, chưa có thử nghiệm riêng.')])

lesson('10', 'Khóa 15 phút mỗi ngày, bài 10: chọn một kỹ năng kế tiếp để lên một bậc trong nghề, hỏi tổ trưởng ba câu, lập kế hoạch 4 tuần.',
 ['Chọn <strong>1 kỹ năng kế tiếp</strong> có ích cho việc làm.',
  'Hỏi tổ trưởng hoặc người giỏi <strong>3 câu</strong>.',
  'Có <strong>kế hoạch 4 tuần</strong>, mỗi tuần một bước nhỏ.'],
 [f'Nếu bạn đang học nghề, xem thêm khóa <a href="{C4U}">Vững nghề</a>.'],
 ['<strong>Thêm một kỹ năng</strong> có thể mở thêm việc mới, ca mới, bậc lương mới. Ví dụ: đọc bản vẽ, vận hành máy khác, kiểm hàng.',
  '<strong>Hỏi để học:</strong> kỹ năng nào tổ đang cần? ai có thể chỉ em? đạt chuẩn là thế nào?',
  '<strong>Chia nhỏ:</strong> mỗi tuần một bước. Tuần 1 xem làm; tuần 2 làm cùng; tuần 3 tự làm có người xem; tuần 4 tự kiểm.',
  '<strong>Một số việc bắt buộc chứng chỉ kỹ năng nghề quốc gia</strong> từ 01/01/2026, theo danh mục của Chính phủ.',
  '<strong>Ghi lại tiến bộ:</strong> ngày, việc làm được, ai xác nhận. Ghi chép này dùng được khi xin việc.'],
 '<p><strong>Kế hoạch lên một bậc.</strong></p>'
 + lines(['Kỹ năng kế tiếp', 'Vì sao có ích cho tôi', 'Người có thể chỉ tôi', 'Chuẩn đạt (theo lời người đó)'])
 + table(['Tuần', 'Bước nhỏ', 'Xong ✓'], [['1', 'Xem người giỏi làm', ''], ['2', 'Làm cùng', ''], ['3', 'Tự làm, có người xem', ''], ['4', 'Tự kiểm, nhờ xác nhận', '']]),
 note3(['Ai sẽ là người mình hỏi đầu tiên, khi nào?']),
 ['Không tự vận hành máy mới khi chưa được hướng dẫn và cho phép.', 'Việc cần chứng chỉ: chỉ làm khi đã có chứng chỉ.'],
 ['Tôi chọn được 1 kỹ năng kế tiếp', 'Tôi đã hỏi 3 câu', 'Tôi có kế hoạch 4 tuần'],
 ['Tổ trưởng: ghi danh sách kỹ năng tổ cần, ghép người học với người giỏi.', 'Xác nhận bằng chữ ký khi người học đạt chuẩn.'],
 [lb('Đã xác nhận', f'Luật Việc làm 74/2025/QH15 (hiệu lực 01/01/2026), Điều 26: người làm công việc ảnh hưởng trực tiếp an toàn, sức khỏe phải có chứng chỉ kỹ năng nghề quốc gia, theo danh mục của Chính phủ ({LVL}).'),
  lb('Cần kiểm chứng', 'Danh mục công việc bắt buộc chứng chỉ: chúng tôi chưa đọc văn bản hướng dẫn. Hỏi Sở phụ trách lao động nơi bạn ở.'),
  lb('Đánh giá chuyên môn', 'Bốn bước xem – làm cùng – tự làm – tự kiểm là cách dạy nghề phổ biến, do daynentang.com viết lại.')])

# ======================= TUẦN 3: TIỀN VÀ CHỮ TÍN =======================
lesson('11', 'Khóa 15 phút mỗi ngày, bài 11: ghi chi 7 ngày để thấy tiền đi đâu, phân biệt cần và muốn.',
 ['Ghi <strong>mọi khoản chi trong 7 ngày</strong>.',
  'Tìm <strong>khoản chi lớn nhất</strong> và 1 khoản có thể giảm.',
  'Dùng câu hỏi <strong>"cần hay muốn?"</strong> trước khi mua.'],
 [f'In <a href="{BTC}">Bảng thu chi</a> hoặc trang tiền trong Sổ 15 phút.'],
 ['<strong>Không ghi thì không biết tiền đi đâu.</strong> Nhiều khoản nhỏ (nước, thẻ cào, ăn vặt) cộng lại thành khoản lớn.',
  '<strong>Ghi ngay khi chi</strong>, không để cuối ngày. Ghi bằng sổ hay điện thoại đều được.',
  '<strong>Cần</strong> là thứ để sống và đi làm: ăn, ở, đi lại, thuốc, tiền gửi về nhà. <strong>Muốn</strong> là thứ thích, có cũng được.',
  '<strong>Với khoản muốn:</strong> chờ 1 ngày rồi quyết. Nhiều khi qua 1 ngày là hết muốn.',
  '<strong>Không cần cắt hết niềm vui.</strong> Mục tiêu là biết rõ và tự chọn.'],
 '<p><strong>Bảy ngày ghi chi.</strong></p>'
 + table(['Ngày', 'Chi gì', 'Bao nhiêu', 'Cần / Muốn'], [[d, '', '', ''] for d in DAYS]),
 note3(['Khoản chi lớn nhất tuần này', 'Một khoản mình có thể giảm']),
 ['Ghi chép tiền là của riêng bạn; cất sổ ở chỗ kín.'],
 ['Tôi ghi đủ 7 ngày', 'Tôi biết khoản chi lớn nhất', 'Tôi hỏi "cần hay muốn" trước khi mua'],
 [f'Gia đình: cùng xem bảng chi mỗi tuần, không trách. Học thêm ở khóa <a href="{G6U}">Tiền nhà mình</a>.'],
 [lb('Đánh giá chuyên môn', 'Ghi chi và phân biệt cần – muốn là cách dạy tài chính cơ bản phổ biến; chúng tôi chưa tìm được thử nghiệm riêng cho công nhân Việt Nam.'),
  lb('Suy luận', 'Hiệu quả của một khóa tự học tài chính ngắn như khóa này chưa được đo.')])

lesson('12', 'Khóa 15 phút mỗi ngày, bài 12: chia lương bốn phần ngay khi nhận, quỹ dự phòng, đọc phiếu lương và so với sổ giờ làm.',
 ['Chia lương tháng này thành <strong>4 phần</strong>.',
  'Bắt đầu <strong>quỹ dự phòng</strong>, dù nhỏ.',
  'Đọc <strong>phiếu lương</strong> và so với sổ giờ làm của mình.'],
 ['Phiếu lương gần nhất (nếu có).', 'Sổ ghi giờ làm, hoặc lịch ca bạn tự ghi.'],
 ['<strong>Chia ngay khi nhận lương:</strong> cố định (nhà, điện nước, gửi về nhà); ăn uống; dự phòng; phần còn lại.',
  '<strong>Dự phòng chuyển ra trước khi tiêu.</strong> Để riêng một chỗ, khó rút. Bắt đầu bằng số nhỏ cũng được.',
  '<strong>Quỹ dự phòng</strong> dùng khi ốm, mất việc, về quê gấp. Có quỹ thì đỡ phải vay nóng.',
  '<strong>Mỗi lần trả lương</strong>, chỗ làm phải cho bạn bảng kê: tiền lương, làm thêm giờ, làm đêm, khoản khấu trừ (nếu có).',
  '<strong>Tự ghi giờ làm</strong> và so với phiếu lương. Thấy chênh, hỏi phòng nhân sự lịch sự, có ghi chép kèm theo.'],
 '<p><strong>Chia lương tháng này.</strong></p>'
 + table(['Phần', 'Số tiền', 'Để ở đâu'], [['Cố định', '', ''], ['Ăn uống', '', ''], ['Dự phòng', '', ''], ['Còn lại', '', '']])
 + table(['Trên phiếu lương', 'Số trên phiếu', 'Theo sổ của tôi', 'Khớp?'], [['Ngày công', '', '', ''], ['Giờ làm thêm', '', '', ''], ['Giờ làm đêm', '', '', ''], ['Khấu trừ', '', '', '']]),
 note3(['Số tiền dự phòng tháng này', 'Mục nào trên phiếu lương mình chưa hiểu?']),
 ['Không cho người khác mượn thẻ ngân hàng, không đọc mã OTP cho ai.', 'Giữ phiếu lương, ảnh chụp lịch ca ở chỗ an toàn.'],
 ['Tôi chia lương 4 phần', 'Tôi đã bắt đầu quỹ dự phòng', 'Tôi đọc và so phiếu lương'],
 ['Gia đình: thống nhất số tiền gửi về mỗi tháng, để người đi làm giữ được phần dự phòng.'],
 [lb('Đã xác nhận', f'Mỗi lần trả lương, người sử dụng lao động phải thông báo bảng kê ghi rõ tiền lương, lương làm thêm giờ, làm đêm, nội dung và số tiền khấu trừ nếu có ({D95}).'),
  lb('Đánh giá chuyên môn', 'Chia lương bốn phần và tỉ lệ trong hình chỉ là minh họa, do daynentang.com soạn; mỗi người tự chọn tỉ lệ.'),
  'Thắc mắc về lương, làm thêm giờ, bảo hiểm: thông tin chuyên sâu sẽ có ở trang chị em trachnhiemxahoi.com.'])

lesson('13', 'Khóa 15 phút mỗi ngày, bài 13: nhận ra lừa đảo việc làm, không đặt cọc, không giao bản chính giấy tờ, tránh vay nóng.',
 ['Nhận ra <strong>4 dấu hiệu lừa đảo việc làm</strong>.',
  'Biết <strong>2 việc không làm</strong>: không đặt cọc, không giao bản chính giấy tờ.',
  'Có <strong>3 chỗ tìm tiền an toàn</strong> khi cần gấp.'],
 ['Nghĩ về một tin tuyển dụng hay một lời mời vay bạn từng thấy.'],
 ['<strong>Dấu hiệu lừa việc làm:</strong> thu phí trước; việc nhẹ lương cao; ép ký ngay; bắt nạp tiền "làm nhiệm vụ" hay mua dụng cụ.',
  '<strong>Kiểm tra trước khi nhận:</strong> tìm thông tin công ty ở nhiều nguồn; ưu tiên trung tâm dịch vụ việc làm, hội chợ việc làm chính thức.',
  '<strong>Không giao bản chính</strong> căn cước, bằng cấp cho chỗ làm giữ. Luật cấm chỗ làm giữ bản chính giấy tờ của người lao động.',
  '<strong>Vay nóng</strong> qua tờ rơi, ứng dụng lạ thường có lãi rất cao, đòi nợ kiểu đe dọa. Trần lãi vay dân sự là 20% một năm.',
  '<strong>Cần tiền gấp:</strong> dùng quỹ dự phòng; hỏi người thân; hỏi công đoàn; hỏi ngân hàng có giấy phép.'],
 '<p><strong>Kiểm tra một lời mời.</strong> Đánh dấu ✓ nếu có.</p>'
 + table(['Dấu hiệu', '✓'], [['Thu phí, đặt cọc trước', ''], ['Lương cao bất thường cho việc rất dễ', ''], ['Ép quyết trong ngày', ''], ['Bắt nạp tiền để nhận việc, rút tiền', ''], ['Đòi giữ bản chính giấy tờ', ''], ['Lãi tính theo ngày, theo tuần', '']])
 + '<p class="small">Có 1 dấu hiệu: dừng lại, hỏi người tin cậy trước khi làm gì tiếp.</p>',
 note3(['Ba chỗ tìm tiền an toàn của mình']),
 ['Bị đe dọa đòi nợ, bị lừa mất tiền: báo công an <strong>113</strong> hoặc công an nơi ở.', 'Không gửi ảnh căn cước, không đọc mã OTP cho người lạ.'],
 ['Tôi nhận ra 4 dấu hiệu', 'Tôi không đặt cọc, không giao bản chính giấy tờ', 'Tôi có 3 chỗ tìm tiền an toàn'],
 ['Tổ trưởng, công đoàn: dán dấu hiệu lừa việc làm ở bảng tin.', 'Gia đình: hỏi trước khi người thân nhận việc qua mạng.'],
 [lb('Đã xác nhận', f'Dấu hiệu lừa đảo việc làm: thu phí trước, mô tả mơ hồ, lương cao bất thường, ép quyết nhanh, đòi nạp tiền sau khi nhận ({LUA}).'),
  lb('Đã xác nhận', f'Chỗ làm không được giữ bản chính giấy tờ tùy thân, văn bằng của người lao động ({D17}).'),
  lb('Đã xác nhận', f'Lãi suất thỏa thuận trong vay dân sự không vượt quá 20%/năm ({BLDS}).')])

lesson('14', 'Khóa 15 phút mỗi ngày, bài 14: chữ tín ở chỗ làm qua bốn việc nhỏ: đúng giờ, giữ lời, nói thật, nhận lỗi bốn bước.',
 ['Đúng giờ <strong>5/5 ngày</strong>.',
  'Nói được <strong>4 bước nhận lỗi</strong>.',
  'Xử lý <strong>2 tình huống giả định</strong> theo hướng chính trực.'],
 ['Sổ 15 phút, trang chữ tín.'],
 ['<strong>Chữ tín là vốn của người làm.</strong> Người đúng giờ, giữ lời thường được giao việc mới, ca tốt.',
  '<strong>Giữ lời:</strong> chỉ hứa điều làm được. Không kịp thì báo sớm, không im lặng.',
  '<strong>Nói thật</strong> về việc mình làm: số lượng, lỗi, hàng hỏng. Giấu lỗi thường làm lỗi lớn hơn.',
  '<strong>Nhận lỗi 4 bước:</strong> việc gì xảy ra; hậu quả; cách sửa; cách tránh lần sau.',
  '<strong>Không ký thay, chấm công hộ, khai sai số liệu</strong>, dù được nhờ. Từ chối nhẹ nhàng: "Cái này em không làm được."'],
 '<p><strong>Tình huống giả định.</strong> Viết cách bạn sẽ nói.</p>'
 + lines(['1. Bạn làm hỏng 3 sản phẩm, chưa ai biết.', '2. Bạn của bạn nhờ quẹt thẻ chấm công hộ vì đến trễ.'])
 + table(['Tuần 3'] + DAYS[:5], [['Đúng giờ ✓'] + [''] * 5]),
 note3(['Một lời hứa nhỏ mình đã giữ tuần này']),
 ['Bị ép khai sai số liệu an toàn, chất lượng: ghi lại, báo người có trách nhiệm hoặc công đoàn.'],
 ['Tôi đúng giờ 5/5 ngày', 'Tôi nói được 4 bước nhận lỗi', 'Tôi xử lý 2 tình huống chính trực'],
 ['Tổ trưởng: cảm ơn người báo lỗi sớm; xử lý lỗi, không làm nhục người báo.'],
 [lb('Đánh giá chuyên môn', 'Bốn việc của chữ tín và nhận lỗi 4 bước do daynentang.com soạn, dựa trên thực hành quản lý chất lượng. Chưa có thử nghiệm riêng.'),
  lb('Suy luận', 'Liên hệ giữa chữ tín và cơ hội việc làm là nhận định thực tế, không phải kết quả nghiên cứu.')])

lesson('15', 'Khóa 15 phút mỗi ngày, bài 15: tử tế nơi làm việc, chỉ việc cho người mới, cảm ơn cụ thể, xử lý khi bị quấy rối.',
 ['Làm <strong>3 việc tử tế</strong> trong tuần.',
  'Biết <strong>3 bước</strong> khi bị quấy rối hoặc thấy người khác bị bắt nạt.'],
 ['Nghĩ về một người mới ở tổ bạn.'],
 ['<strong>Tử tế là việc nhỏ:</strong> chỉ việc cho người mới, nhường chỗ nghỉ, cảm ơn cụ thể.',
  '<strong>Cảm ơn cụ thể:</strong> "Cảm ơn chị chỉ em cách đổi chỉ, em làm nhanh hơn hẳn." Cụ thể thì người nghe tin.',
  '<strong>Không cười cợt, bêu xấu</strong> ngoại hình, quê quán, giọng nói của ai. Không chia sẻ ảnh người khác khi chưa được đồng ý.',
  '<strong>Quấy rối tình dục ở nơi làm việc bị luật cấm.</strong> Đó không phải lỗi của người bị quấy rối.',
  '<strong>Khi bị quấy rối:</strong> nói "Dừng lại" nếu an toàn; ghi ngày, giờ, người chứng kiến; báo người phụ trách, công đoàn.'],
 '<p><strong>Ba việc tử tế tuần này.</strong></p>'
 + table(['Ngày', 'Việc tử tế', 'Cho ai (không cần ghi tên)'], [['', '', ''] for _ in range(3)])
 + lines(['Người tôi sẽ báo nếu bị quấy rối hay thấy bắt nạt']),
 note3(['Một việc tử tế người khác làm cho mình gần đây']),
 ['Bị đe dọa, bị đánh: gọi <strong>113</strong>.', 'Dưới 18 tuổi bị quấy rối, xâm hại: gọi <strong>111</strong> (miễn phí, 24/7).',
  'Có thể nhờ người tin cậy đi cùng khi báo.'],
 ['Tôi làm 3 việc tử tế', 'Tôi cảm ơn cụ thể', 'Tôi biết 3 bước khi bị quấy rối'],
 ['Tổ trưởng: giới thiệu người mới với cả tổ, ghép một người kèm.', 'Xử lý nghiêm, kín đáo mọi báo cáo quấy rối.'],
 [lb('Đã xác nhận', f'Bộ luật Lao động 2019, Điều 8, liệt kê quấy rối tình dục tại nơi làm việc là hành vi bị nghiêm cấm ({D8}).'),
  lb('Đã xác nhận', f'Tổng đài 111 bảo vệ trẻ em, miễn phí, 24/7 ({T111}). Tra 28/10/2026.'),
  lb('Đánh giá chuyên môn', 'Ba bước khi bị quấy rối và các việc tử tế do daynentang.com soạn; chưa được luật sư hay chuyên gia duyệt.')])

# ======================= TUẦN 4: TÂM TRÍ VÀ GIA ĐÌNH =======================
lesson('16', 'Khóa 15 phút mỗi ngày, bài 16: dừng tay, gọi tên cảm xúc, thở chậm 1–3 phút trước khi nói hay làm.',
 ['Gọi tên <strong>cảm xúc</strong> của mình 1 lần mỗi ngày.',
  'Thở chậm <strong>1–3 phút</strong> khi bực hay lo.'],
 ['Một chỗ ngồi yên, hoặc đứng tựa tường.'],
 ['<strong>Cảm xúc nào cũng có lý do:</strong> bực, lo, buồn, mệt, vui. Cảm xúc không xấu; cách mình làm theo nó mới quan trọng.',
  '<strong>Gọi tên được thì dễ chọn cách làm.</strong> Nói thầm: "Mình đang bực vì bị nói nặng."',
  '<strong>Dừng – Gọi tên – Thở:</strong> dừng tay; gọi tên cảm xúc; thở chậm 1–3 phút; rồi mới nói hay làm.',
  '<strong>Thở chậm:</strong> hít vào đếm 4, thở ra đếm 6. Thấy dễ chịu là được, không cần đúng số.',
  f'<strong>Muốn đi sâu hơn</strong> về thiền, tĩnh tâm: xem trang chị em {THK}.'],
 '<p><strong>Thử ngay 1 phút thở chậm.</strong> Rồi ghi cảm xúc trong 5 ngày.</p>'
 + table(['Ngày', 'Cảm xúc mạnh nhất', 'Vì sao', 'Đã thở chậm?'], [[d, '', '', ''] for d in DAYS[:5]]),
 note3(['Sau khi thở chậm, mình khác gì so với trước?']),
 ['Chóng mặt khi thở chậm: dừng, thở bình thường.', 'Không tập thở khi đang lái xe, đứng máy.'],
 ['Tôi gọi tên được cảm xúc', 'Tôi thở chậm 1–3 phút khi bực', 'Tôi ghi cảm xúc 5 ngày'],
 ['Tổ trưởng: khi tổ căng thẳng, cho 1 phút im lặng thở trước khi họp.', 'Gia đình: hỏi "Hôm nay con/anh/em thấy thế nào?" và nghe hết.'],
 [lb('Đã xác nhận', f'WHO có sách minh họa về quản lý căng thẳng với bài tập vài phút mỗi ngày, có bản tiếng Việt ({DWM}).'),
  lb('Đánh giá chuyên môn', 'Nhịp thở 4–6 và chuỗi Dừng – Gọi tên – Thở do daynentang.com chọn; là kỹ năng ngắn, không phải điều trị.')])

lesson('17', 'Khóa 15 phút mỗi ngày, bài 17: nhận ra quá tải kéo dài, ba bậc tìm giúp, khi nào cần gọi ngay.',
 ['Nhận ra <strong>dấu hiệu quá tải</strong> kéo dài của mình.',
  'Ghi <strong>2 người</strong> có thể nói chuyện khi khó khăn.',
  'Biết <strong>số điện thoại</strong> cần gọi.'],
 ['Sổ 15 phút, trang số khẩn cấp.'],
 ['<strong>Mệt sau ca là bình thường.</strong> Quá tải là khi mệt, buồn, lo kéo dài nhiều tuần, không hồi lại sau nghỉ.',
  '<strong>Dấu hiệu:</strong> mất ngủ nhiều tuần; cáu gắt, buồn hầu hết các ngày; uống rượu nhiều hơn; muốn bỏ hết.',
  '<strong>Ba bậc tìm giúp:</strong> người thân, bạn; y tế, tư vấn; khi nguy hiểm thì gọi ngay.',
  '<strong>Nghĩ đến cái chết hay tự làm hại mình:</strong> nói với người tin cậy ngay hôm nay. Gọi 115 nếu nguy hiểm trước mắt.',
  '<strong>Tìm giúp là việc làm mạnh mẽ</strong>, không phải yếu đuối. Càng sớm càng dễ hồi phục.'],
 '<p><strong>Kế hoạch khi quá tải.</strong></p>'
 + lines(['3 dấu hiệu quá tải của tôi', 'Việc giúp tôi đỡ hơn (ngủ, đi bộ, gọi về nhà…)', 'Người 1 (không cần ghi tên thật)', 'Người 2', 'Nơi khám gần chỗ tôi ở']),
 note3(['Tuần này, mình ở mức nào: ổn, mệt, hay quá tải?']),
 ['Đường dây Ngày Mai <strong>096 306 1414</strong> (hỗ trợ người trầm cảm và người thân). Giờ làm việc xem ở trang Cần giúp ngay.',
  'Khóa này không thay thế khám và điều trị.'],
 ['Tôi biết dấu hiệu quá tải của mình', 'Tôi có 2 người có thể nói chuyện', 'Tôi biết số cần gọi'],
 ['Tổ trưởng: để ý người đổi tính, hay vắng, uống nhiều; hỏi riêng, nhẹ nhàng.', 'Gia đình: nghe nhiều hơn khuyên; đi cùng người thân đi khám.'],
 [lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}). Tra 28/10/2026, kiểm tra lại mỗi quý.'),
  lb('Đã xác nhận', f'WHO có tài liệu tự giúp khi căng thẳng, có bản tiếng Việt ({DWM}).'),
  lb('Đánh giá chuyên môn', 'Danh sách dấu hiệu và ba bậc tìm giúp do daynentang.com soạn, không dùng để chẩn đoán.')])

lesson('18', 'Khóa 15 phút mỗi ngày, bài 18: gần con khi ở xa, cuộc gọi 10 phút với câu hỏi mở, giờ gọi cố định, nhờ người chăm con đồng hành.',
 ['Có <strong>giờ gọi cố định</strong> với con.',
  'Hỏi <strong>1 câu mở</strong> mỗi cuộc gọi và nghe con kể.',
  'Thống nhất <strong>1 việc</strong> với người đang chăm con.'],
 ['Nghĩ 3 câu hỏi mở hợp với tuổi con.', 'Bạn chưa có con: dùng bài này cho cha mẹ, em nhỏ ở quê.'],
 ['<strong>Giờ gọi cố định</strong> giúp con có cái để chờ. Ví dụ: tối thứ Ba, thứ Năm, Chủ nhật, 10 phút.',
  '<strong>Câu hỏi mở</strong> mời con kể: "Hôm nay chuyện gì làm con cười?" Câu hỏi đóng chỉ được "Dạ có".',
  '<strong>Nghe nhiều hơn nói.</strong> Nhắc lại lời con: "À, con được cô khen vẽ đẹp." Con biết mình được nghe.',
  '<strong>Kể việc của mình</strong> bằng lời đơn giản. Với bé nhỏ: hát, làm mặt vui, chơi ú òa qua màn hình.',
  '<strong>Người chăm con là người đồng hành.</strong> Cảm ơn họ, hỏi họ cần gì, thống nhất một quy tắc chung.'],
 '<p><strong>Kế hoạch gọi về nhà.</strong></p>'
 + lines(['Giờ gọi cố định', 'Câu hỏi mở 1', 'Câu hỏi mở 2', 'Câu hỏi mở 3', 'Một việc thống nhất với người chăm con'])
 + table(['Tuần 4'] + DAYS[:5], [['Đã gọi ✓'] + [''] * 5]),
 note3(['Điều con kể làm mình nhớ nhất tuần này']),
 ['Không gọi khi đang lái xe, đang làm ca.', 'Con kể chuyện bị đánh, bị xâm hại, bị bỏ mặc: tin con, gọi 111 để được tư vấn.'],
 ['Tôi có giờ gọi cố định', 'Tôi hỏi câu mở và nghe hết', 'Tôi đã nói chuyện với người chăm con'],
 [f'Học thêm cho bố mẹ: <a href="{G2U}">Gia đình 0–2 – Giao và Đáp</a>, <a href="{G4U}">Gia đình có con 10–14</a>.',
  'Ông bà, người chăm con: kể cho bố mẹ ở xa một việc tốt con làm trong tuần.'],
 [lb('Đã xác nhận', f'Harvard: tương tác qua lại "giao và đáp" giữa trẻ và người lớn giúp xây nền phát triển não bộ ({HARV}).'),
  lb('Suy luận', 'Áp dụng ý "giao và đáp" cho cuộc gọi điện từ xa là suy luận của chúng tôi; chưa có nghiên cứu riêng về cuộc gọi.'),
  lb('Đánh giá chuyên môn', 'Giờ gọi cố định, câu hỏi mở, cuộc gọi 10 phút do daynentang.com soạn.')])

lesson('19', 'Khóa 15 phút mỗi ngày, bài 19: vòng người có thể nhờ, ghi 3 người, giữ quan hệ bằng việc nhỏ đều đặn.',
 ['Ghi tên <strong>3 người có thể nhờ</strong> khi khó.',
  'Làm <strong>2 việc nhỏ</strong> giữ quan hệ trong tuần.'],
 ['Nghĩ về người quanh bạn: gia đình, bạn cùng phòng trọ, đồng nghiệp, hàng xóm.'],
 ['<strong>Sống xa nhà dễ thấy một mình.</strong> Vài người có thể nhờ giúp bạn vững hơn khi ốm, mất việc, buồn.',
  '<strong>Người có quan hệ xã hội tốt</strong> có khả năng sống lâu hơn trong các nghiên cứu theo dõi. Đây là tương quan, không phải nhân quả.',
  '<strong>Ba vòng:</strong> gia đình; bạn bè, đồng nghiệp; hàng xóm, công đoàn, hội đồng hương.',
  '<strong>Giữ quan hệ bằng việc nhỏ:</strong> hỏi thăm, ăn chung, giúp một việc, rủ đi bộ.',
  '<strong>Giúp người cũng là xây vòng của mình.</strong> Người được giúp thường nhớ và giúp lại.'],
 '<p><strong>Vòng người có thể nhờ.</strong> Không cần ghi tên thật, ghi cách bạn gọi họ.</p>'
 + table(['Người', 'Nhờ được việc gì', 'Liên lạc lần cuối'], [['1.', '', ''], ['2.', '', ''], ['3.', '', '']])
 + lines(['Việc nhỏ 1 tuần này', 'Việc nhỏ 2 tuần này']),
 note3(['Ai là người mình muốn hỏi thăm nhất, vì sao chưa?']),
 ['Người mới quen hứa việc làm, cho vay, rủ đi xa: hỏi người tin cậy trước.', 'Không đưa giấy tờ, thẻ ngân hàng cho người mới quen.'],
 ['Tôi ghi được 3 người', 'Tôi làm 2 việc nhỏ giữ quan hệ', 'Tôi đã giúp một người'],
 ['Tổ trưởng, công đoàn: tạo dịp ăn chung, chơi thể thao cho người xa nhà.'],
 [lb('Đã xác nhận', f'Phân tích gộp 148 nghiên cứu: người có quan hệ xã hội mạnh có khả năng sống sót cao hơn khoảng 50% trong thời gian theo dõi; đây là tương quan ({HL}).'),
  lb('Đánh giá chuyên môn', 'Ba vòng và các việc nhỏ giữ quan hệ do daynentang.com soạn.')])

lesson('20', 'Khóa 15 phút mỗi ngày, bài 20: xem lại bốn tuần, chấm 0–1–2, chọn ba thói quen giữ trong 30 ngày tới.',
 ['Chấm lại <strong>10 mục tự đánh giá</strong> của khóa.',
  'Chọn <strong>3 thói quen</strong> giữ trong 30 ngày tới.',
  'Viết <strong>kế hoạch khi lỡ</strong> một ngày.'],
 [f'Trang tự đánh giá trong <a href="{TOOL}">Sổ 15 phút</a>.'],
 ['<strong>Bốn tuần, bốn nền:</strong> chăm thân, an toàn và học nghề, tiền và chữ tín, tâm trí và gia đình.',
  '<strong>Xem lại để biết mình đi được bao xa.</strong> So tuần 1 với tuần 4, không so với người khác.',
  '<strong>Giữ ít mà chắc:</strong> chọn 3 thói quen có ích nhất, đừng giữ hết cùng lúc.',
  '<strong>Lỡ một ngày là chuyện thường.</strong> Làm lại ngày hôm sau; đừng để lỡ hai ngày liền.',
  '<strong>Sau 30 ngày:</strong> xem lại, giữ thói quen đã chắc, thêm một thói quen mới.'],
 '<p><strong>Ba thói quen cho 30 ngày tới.</strong></p>'
 + lines(['Thói quen 1', 'Thói quen 2', 'Thói quen 3', 'Nếu lỡ một ngày thì …'])
 + f'<p>Theo dõi 30 ngày ở trang cuối của <a href="{TOOL}">Sổ 15 phút</a>.</p>',
 note3(['Điều mình tự hào nhất sau 4 tuần', 'Điều mình muốn học tiếp']),
 ['Nếu bài tự đánh giá cho thấy tâm trạng xấu kéo dài: xem lại bài 17 và tìm giúp sớm.'],
 ['Tôi chấm lại 10 mục', 'Tôi chọn 3 thói quen', 'Tôi có kế hoạch khi lỡ một ngày'],
 ['Tổ trưởng: cùng tổ chia sẻ thói quen giữ được, không chấm điểm ai.', 'Gia đình: chúc mừng người học đã đi hết 4 tuần.'],
 [lb('Đánh giá chuyên môn', 'Phiếu tự đánh giá 0–1–2 dùng để tự theo dõi, không phải công cụ đo đã kiểm định.'),
  lb('Suy luận', 'Chúng tôi chưa đo hiệu quả của khóa. Kết quả của bạn là thông tin quý để sửa khóa.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi có 15 phút cố định mỗi ngày', 'Tôi ngủ đủ, có chỗ ngủ tối, yên, mát', 'Tôi uống đủ nước, hộp cơm an toàn',
         'Tôi nghỉ ngắn, giãn cơ, vận động', 'Tôi biết dấu hiệu sốc nhiệt và cách xử lý', 'Tôi hỏi 5 câu và dùng đủ bảo hộ',
         'Tôi dám dừng việc nguy hiểm và báo cáo', 'Tôi ghi chi, chia lương, có quỹ dự phòng', 'Tôi giữ chữ tín, tử tế nơi làm',
         'Tôi gọi tên cảm xúc và biết khi nào cần giúp']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
grid30 = '<div class="table-wrap"><table><thead><tr><th>Thói quen</th>' + ''.join(f'<th>{i}</th>' for i in range(1, 16)) + '</tr></thead><tbody>' \
    + ''.join(f'<tr><td>{n}</td>' + '<td></td>' * 15 + '</tr>' for n in ['1.', '2.', '3.']) + '</tbody></table></div>'
grid30b = grid30.replace(''.join(f'<th>{i}</th>' for i in range(1, 16)), ''.join(f'<th>{i}</th>' for i in range(16, 31)))
page(TOOL, 'Sổ 15 phút', 'Trang in cho khóa 15 phút mỗi ngày: kế hoạch Nếu… thì…, giờ ngủ, nước, an toàn, chia lương, người có thể nhờ, số khẩn cấp, theo dõi 30 ngày.',
f'''
<h1>Sổ 15 phút</h1>
<p>Dùng cho khóa <a href="{U}">15 phút mỗi ngày</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Sổ là của riêng bạn.</p>
{PRINT_ROW}
<h2>1. 15 phút của tôi (bài 1)</h2>
{lines(['Giờ và chỗ', 'Nếu … thì …', 'Nếu bị cản thì …'])}
<h2>2. Giấc ngủ (bài 2)</h2>
{table(['Ngày', 'Ca', 'Lên giường', 'Dậy', 'Số giờ'], [['', '', '', '', ''] for _ in range(3)])}
<h2>3. Nước và hộp cơm (bài 3, 5)</h2>
<p>Chai nước: …… ml, đổ đầy …… lần/ca · Nước tiểu trong hoặc vàng nhạt = đủ nước.</p>
<p>Sốc nhiệt (lú lẫn, ngất, co giật): gọi <strong>115</strong>, đưa vào bóng mát, làm mát, ở cạnh.</p>
<h2>4. An toàn (bài 6–8)</h2>
<p>Năm câu hỏi: bị thương ra sao? · bảo hộ gì? · đã được hướng dẫn? · sự cố thì sao? · hỏi ai?</p>
{table(['Mối nguy', 'Cách phòng', 'Đồ bảo hộ', 'Đã báo'], [['', '', '', ''] for _ in range(3)])}
<p>Câu dừng việc: "Em thấy … có thể gây … Em dừng lại và báo anh/chị." · Dưới 18 tuổi: tối đa 8 giờ/ngày, 40 giờ/tuần.</p>
<h2>5. Lên một bậc (bài 10)</h2>
{lines(['Kỹ năng kế tiếp', 'Người chỉ tôi', 'Chuẩn đạt'])}
<h2>6. Tiền (bài 11–13)</h2>
{table(['Phần', 'Số tiền'], [['Cố định', ''], ['Ăn uống', ''], ['Dự phòng', ''], ['Còn lại', '']])}
<p>Không đặt cọc · Không giao bản chính giấy tờ · Không vay lãi theo ngày · Không đọc mã OTP cho ai.</p>
<h2>7. Người có thể nhờ (bài 17, 19)</h2>
{lines(['Người 1', 'Người 2', 'Người 3'])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">115</th><td>Cấp cứu y tế, tai nạn, sốc nhiệt</td></tr>
<tr><th>114</th><td>Cháy nổ, cứu nạn</td></tr>
<tr><th>113</th><td>Công an, khi bị đe dọa, ép buộc, lừa đảo</td></tr>
<tr><th>111</th><td>Bảo vệ trẻ em (dưới 18 tuổi), miễn phí, 24/7</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
</tbody></table></div>
<h2>8. Theo dõi 30 ngày (bài 20)</h2>
{grid30}
{grid30b}
<h2>Tự đánh giá (tuần 1 và tuần 4)</h2>
<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 4</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán hay đánh giá chính thức.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
wk = ''
for w in range(1, 5):
    items = ''.join(f'<li><a href="{url(w, L[k][2])}">{L[k][3]} – {L[k][4]}</a></li>' for k in ORDER if L[k][0] == w)
    wk += f'<h3>Tuần {w}: {WEEKS[w-1]}</h3><ol>{items}</ol>'
page(U, '15 phút mỗi ngày', 'Khóa tự học miễn phí cho người lao động: mỗi ngày 15 phút trong 4 tuần về giấc ngủ, nước, an toàn, học nghề, tiền lương, chữ tín, cảm xúc và gia đình.',
f'''
<p class="eyebrow">Cá nhân · Khóa C5 · Đang thử nghiệm</p>
<h1>15 phút mỗi ngày</h1>
<p class="lead">Làm ca dài, về nhà đã mệt. Khóa này chỉ xin bạn 15 phút mỗi ngày, để chăm sức khỏe, giữ an toàn, giữ tiền và giữ người thân.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn có thói quen nhỏ, đều đặn để ngủ đủ, làm việc an toàn, học thêm kỹ năng, quản lý lương, giữ chữ tín, chăm tâm trí và gần gia đình</td></tr>
<tr><th>Dành cho</th><td>Người lao động từ 15 tuổi: công nhân nhà máy, công trường, kho, bếp, dịch vụ; người làm ca, người sống xa nhà</td></tr>
<tr><th>Thời lượng</th><td>4 tuần × 5 ngày (thứ Hai đến thứ Sáu), mỗi bài 15 phút: đọc 5 phút, làm 7 phút, ghi lại 3 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút. Không cần máy tính; đọc trên điện thoại hoặc in ra đều được</td></tr>
<tr><th>Tình trạng</th><td>Đủ 20 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của tổ trưởng, cán bộ an toàn, công đoàn và người lao động</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn có 15 phút cố định mỗi ngày.</li><li>Bạn uống đủ nước, nghỉ ngắn, nhận ra sốc nhiệt.</li><li>Bạn biết tiền đi đâu trong 7 ngày.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: việc nhỏ làm đều thắng việc lớn làm một lần.</li><li>Kỹ năng: lập kế hoạch Nếu… thì…, báo cáo an toàn, chia lương, gọi tên cảm xúc.</li><li>Một vòng người có thể nhờ khi khó.</li></ul></div>
</div>
{figure_block('KHOAF')}

<h2 id="bon-tuan">Bốn tuần, hai mươi bài</h2>
{wk}

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ 15 phút</a>: kế hoạch Nếu… thì…, giấc ngủ, nước, an toàn, chia lương, người có thể nhờ, số khẩn cấp, theo dõi 30 ngày, tự đánh giá.</li>
<li><a href="{BTC}">Bảng thu chi</a>: ghi chi 7 ngày (bài 11).</li></ul>

<h2>Cho tổ trưởng, công đoàn, gia đình</h2>
<ul>
<li>Dùng mỗi bài như 15 phút sinh hoạt đầu ca hoặc giữa giờ nghỉ.</li>
<li>Khen người hỏi, người báo nguy hiểm, người báo lỗi sớm.</li>
<li>Không thu, không chấm sổ của người học. Sổ là của riêng họ.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{GS}</td><td>Kế hoạch Nếu… thì…</td><td><span class="label">[Đã xác nhận]</span> Tổng hợp nhiều nghiên cứu, chủ yếu ở phương Tây</td></tr>
<tr><td>{NSLEEP}; {AASMA}</td><td>Ngủ đủ khi làm ca</td><td><span class="label">[Đã xác nhận]</span> Khuyến nghị của NIOSH và đồng thuận chuyên gia</td></tr>
<tr><td>{HEAT}; {HEATI}</td><td>Làm việc khi nóng, sơ cứu</td><td><span class="label">[Đã xác nhận]</span> WHO/WMO 2025; hướng dẫn OSHA/NIOSH</td></tr>
<tr><td>{MICRO}; {WHOPA}</td><td>Nghỉ ngắn, vận động</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp 22 mẫu, tác dụng nhỏ; khuyến nghị WHO</td></tr>
<tr><td>{ILO}; {ATVS}; {LDCTN}</td><td>An toàn, quyền dừng việc, người dưới 18 tuổi</td><td><span class="label">[Đã xác nhận]</span> ILO; luật Việt Nam đọc qua trang tóm tắt</td></tr>
<tr><td>{DUN}; {CEP}</td><td>Học 15 phút để nhớ lâu</td><td><span class="label">[Đã xác nhận]</span> Tổng quan và phân tích gộp, chủ yếu với học sinh, sinh viên</td></tr>
<tr><td>{D95}; {D17}; {BLDS}; {LUA}</td><td>Phiếu lương, giấy tờ, vay, lừa việc làm</td><td><span class="label">[Đã xác nhận]</span> Văn bản pháp luật và cảnh báo chính thức</td></tr>
<tr><td>{DWM}; {HL}</td><td>Căng thẳng, người có thể nhờ</td><td><span class="label">[Đã xác nhận]</span> Tài liệu WHO; phân tích gộp (tương quan)</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Chúng tôi chưa tìm được thử nghiệm về một khóa tự học 15 phút cho công nhân như khóa này. Mỗi bài ghép các khuyến nghị đã có nguồn với cách làm do chúng tôi soạn, được ghi rõ là [Đánh giá chuyên môn].
  Khóa không thay thế huấn luyện an toàn bắt buộc của chỗ làm, khám chữa bệnh hay tư vấn pháp lý. Quyền lao động chuyên sâu sẽ có ở trang chị em trachnhiemxahoi.com.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C5 built')
