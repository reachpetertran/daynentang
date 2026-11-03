# Khóa C3 "Tự học – tự quản" – trang khóa, 10 bài, công cụ "Sổ tự quản học kỳ".
# Người đọc gồm học sinh lớp 12 (có thể dưới 18 tuổi): KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c3  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/tu-hoc-tu-quan/'
TOOL = '/cong-cu/so-tu-quan-hoc-ky/'
C2 = '/khoa-hoc/hieu-minh/'
C2G = '/khoa-hoc/hieu-minh/tuan-7/muc-tieu-va-tro-ngai/'
C2E = '/khoa-hoc/hieu-minh/tuan-3/cam-xuc-tuoi-moi-lon/'
C1 = '/khoa-hoc/lon-len-an-toan/'
G6 = '/khoa-hoc/tien-nha-minh/'
BTC = '/cong-cu/bang-thu-chi/'
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

# ---------- Nguồn (đã tra 03/11/2026) ----------
EEF = '<a href="https://educationendowmentfoundation.org.uk/news/latest-updates-to-the-toolkit/">EEF – Teaching and Learning Toolkit, mục siêu nhận thức và tự điều chỉnh</a>'
DUN = '<a href="https://www.psychologicalscience.org/news/releases/which-study-strategies-make-the-grade.html">Dunlosky et al. 2013, <em>Psychological Science in the Public Interest</em> (thông cáo của APS)</a>'
CEP = '<a href="https://pubmed.ncbi.nlm.nih.gov/16719566/">Cepeda et al. 2006, <em>Psychological Bulletin</em> 132</a>'
AGA = '<a href="https://profiles.wustl.edu/en/publications/classroom-based-programs-of-retrieval-practice-reduce-middle-scho/">Agarwal et al. 2014, <em>JARMAC</em> 3</a>'
AEON = '<a href="https://sciencedaily.com/releases/2021/02/210204131413.htm">Aeon, Faber &amp; Panaccio 2021, <em>PLOS ONE</em> (ScienceDaily đưa tin)</a>'
BUE = '<a href="https://bear.warrington.ufl.edu/brenner/mar7588/Papers/buehler-et-al-1994.pdf">Buehler, Griffin &amp; Ross 1994, <em>JPSP</em> 67</a>'
GK = '<a href="https://www.rutgers.edu/news/cellphone-distraction-classroom-can-lead-lower-grades-rutgers-study-finds">Glass &amp; Kang, <em>Educational Psychology</em> (Rutgers đưa tin 27/7/2018)</a>'
KYN = '<a href="https://www.clearinghouse.edu.tum.de/wp-content/uploads/2023/12/CHU_KR4_ENG_Kyndt_2013.pdf">Kyndt et al. 2013, <em>Educational Research Review</em> 10 (tóm tắt của Clearing House TUM)</a>'
GS = '<a href="https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f">Gollwitzer &amp; Sheeran 2006</a>'
DUCK = '<a href="https://www.socmot.uni-konstanz.de/node/94">Duckworth et al. 2011</a>'
QC = '<a href="https://lsvn.vn/cac-hinh-thuc-xu-ly-vi-pham-quy-che-thi-tot-nghiep-thpt-thi-sinh-can-luu-y-a159467.html">Thông tư 24/2024/TT-BGDĐT, Điều 57 (Báo Luật sư Việt Nam tóm tắt, 26/6/2025)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
AASMA = '<a href="https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf">AASM và SRS 2015, <em>J Clin Sleep Med</em> 11(6)</a>'
NIMH = '<a href="https://www.nimh.nih.gov/health/publications/the-teen-brain-7-things-to-know">NIMH – The Teen Brain</a>'
WHOPA = '<a href="https://who.int/initiatives/behealthy/physical-activity">WHO – Be Healthy: vận động</a>'
PA = '<a href="https://knowledge-for-policy.ec.europa.eu/health-promotion-knowledge-gateway/physical-activity-sedentary-behaviour-table-2a_en">khuyến nghị WHO cho tuổi 5–17 (bảng tổng hợp của EU)</a>'
VOH = '<a href="https://voh.com.vn/phap-luat/cong-an-canh-bao-3-chieu-bat-coc-online-nham-vao-hoc-sinh-sinh-vien-625691.html">Bộ Công an cảnh báo (VOH, 12/10/2025)</a>'
DWM = '<a href="https://who.int/publications/i/item/9789240003927">WHO – Doing What Matters in Times of Stress (29/4/2020, có bản tiếng Việt)</a>'
WHOA = '<a href="https://www.who.int/news-room/fact-sheets/detail/mental-health-of-adolescents">WHO – Sức khỏe tâm thần vị thành niên (1/9/2025)</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài viết dựa trên nghiên cứu về cách học, nhưng chưa được thầy cô hay chuyên viên tư vấn học đường duyệt.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Những gì bạn viết là của riêng bạn. '
           'Bố mẹ, thầy cô (từ 18 tuổi) có thể góp ý ở trang <a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên hay trường.</p>')
TALK = ('Đang nghĩ đến cái chết hay muốn làm đau bản thân: nói ngay với người ở gần, gọi <strong>115</strong> nếu nguy hiểm. '
        'Đường dây Ngày Mai <strong>096 306 1414</strong>. Tổng đài <strong>111</strong> bảo vệ trẻ em, miễn phí, 24/7.')

L = {
 '1': (1, 'muc-tieu-hoc-ky', 'Bài 1', 'Mục tiêu học kỳ và vòng tự học'),
 '2': (2, 'lich-tuan', 'Bài 2', 'Lịch tuần và ước lượng thời gian'),
 '3': (3, 'doc-va-ghi-chu', 'Bài 3', 'Đọc và ghi chú chủ động'),
 '4': (4, 'on-tap-nho-lau', 'Bài 4', 'Ôn tập để nhớ lâu'),
 '5': (5, 'tap-trung-va-dien-thoai', 'Bài 5', 'Tập trung và điện thoại'),
 '6': (6, 'lam-viec-nhom', 'Bài 6', 'Làm việc nhóm'),
 '7': (7, 'thi-cu', 'Bài 7', 'Thi cử: ôn sớm, thi bình tĩnh, thi trung thực'),
 '8': (8, 'ngu-an-van-dong', 'Bài 8', 'Ngủ, ăn, vận động mùa học'),
 '9': (9, 'tien-hoc-sinh-sinh-vien', 'Bài 9', 'Tiền học sinh – sinh viên'),
 '10': (10, 'khi-qua-tai', 'Bài 10', 'Khi quá tải, xem lại học kỳ'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn viết 1 mục tiêu học kỳ đo được, chia thành 3 mốc và 1 việc tuần này.'),
 (2, 'Bạn xếp lịch tuần và so sánh thời gian ước lượng với thực tế cho 3 việc.'),
 (3, 'Bạn ghi chú 1 bài theo trang hai cột và tóm tắt bằng lời mình.'),
 (4, 'Bạn làm 10 thẻ tự kiểm tra và ôn theo lịch giãn cách ít nhất 3 lần.'),
 (5, 'Bạn làm ít nhất 5 khối tập trung trong tuần, điện thoại để xa.'),
 (6, 'Bạn lập bảng phân công cho 1 việc nhóm và họp nhóm đầu tiên.'),
 (7, 'Bạn làm 1 đề bấm giờ và phân loại mọi lỗi theo 4 loại.'),
 (8, 'Bạn ghi giờ ngủ 7 ngày và vận động đủ mức khuyến nghị cho tuổi mình.'),
 (9, 'Bạn ghi chi 7 ngày và chia tiền tháng theo 4 phần.'),
 (10, 'Bạn có kế hoạch khi quá tải và hoàn thành phiếu xem lại học kỳ.'),
]

def lesson(k, desc, goals, prep, read, do, talk, safety, selfq, adult, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Tuần {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Xem lại 5 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (5 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Xem lại với bạn học, người thân hoặc tự viết (5 phút)', talk),
        sec(6, 'An toàn', ul(safety + [TALK])),
        sec(7, 'Tự đánh giá', selftab(selfq)),
        sec(8, 'Cho bố mẹ, thầy cô (nếu có)', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Tự học – tự quản</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('D' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Tự học – tự quản, bài 1: viết mục tiêu học kỳ đo được, chia ngược thành mốc và việc tuần này, làm quen vòng tự học.',
 ['Viết <strong>1 mục tiêu học kỳ</strong> đo được, có hạn.',
  'Chia mục tiêu thành <strong>3 mốc</strong> và <strong>1 việc làm tuần này</strong>.',
  'Nói được <strong>3 bước</strong> của vòng tự học: lên kế hoạch, làm và tự theo dõi, xem lại.'],
 [f'In trang 1 của <a href="{TOOL}">Sổ tự quản học kỳ</a>, hoặc lấy một tờ giấy.', 'Lịch học kỳ: ngày thi giữa kỳ, cuối kỳ, hạn nộp bài lớn.'],
 ['<strong>Tự học là tự quản ba việc:</strong> lên kế hoạch trước khi học, tự theo dõi khi đang học, xem lại sau khi học.',
  '<strong>Lên đại học, ít ai nhắc bạn.</strong> Lịch, hạn nộp, cách học do bạn tự lo. Lớp 12 là lúc tập trước.',
  '<strong>Kỹ năng này dạy được.</strong> Ở trường học, dạy học sinh tự lên kế hoạch, theo dõi và xem lại việc học giúp tiến bộ thêm khoảng 7 tháng trong một năm (trung bình).',
  '<strong>Mục tiêu đo được</strong> nói rõ làm gì, bao nhiêu, khi nào. "Học Toán chăm hơn" chưa đo được. "Mỗi tuần làm 3 đề, giữa kỳ đạt 7,5" thì đo được.',
  '<strong>Ghi cả việc mình làm,</strong> không chỉ điểm số. Điểm còn phụ thuộc đề thi. Số đề, số giờ luyện thì do bạn quyết định.',
  '<strong>Chia ngược:</strong> mục tiêu cuối kỳ → mốc giữa kỳ → mốc tháng này → việc tuần này. Việc tuần này phải nhỏ đủ để bắt đầu ngay.',
  f'<strong>Trở ngại và câu Nếu… thì…</strong> bạn có thể học ở <a href="{C2G}">bài 7 khóa Hiểu mình</a>. Ở đây dùng lại cho mục tiêu học kỳ.'],
 '<p><strong>Bài 1: mục tiêu và mốc.</strong></p>'
 + table(['Mục', 'Của tôi'], [['Môn hoặc việc chọn', ''], ['Mục tiêu cuối kỳ (đo được, có hạn)', ''], ['Mốc giữa kỳ', ''],
                              ['Mốc tháng này', ''], ['Việc tuần này', ''], ['Câu Nếu… thì… cho trở ngại lớn nhất', 'Nếu ……………… thì ………………']])
 + '<p><strong>Bài 2: vòng tự học trong 1 buổi.</strong> Trước khi học, viết 1 câu: "Buổi này mình sẽ…". Học xong, viết: "Mình làm được… Lần sau sẽ chỉnh…".</p>'
 + lines(['Kế hoạch buổi học', 'Làm được', 'Lần sau sẽ chỉnh']),
 ol(['Kể mục tiêu và việc tuần này cho một bạn học hoặc người thân.', 'Hẹn họ hỏi thăm bạn vào cuối tuần.',
     'Hoặc viết: "Nếu đạt mục tiêu này, điều thay đổi với mình là…"']),
 ['Không đặt mục tiêu học bằng cách bỏ ngủ, bỏ ăn.',
  'Mục tiêu do bạn chọn. Áp lực điểm số làm bạn mất ngủ nhiều tuần: nói với người tin cậy (xem bài 10).'],
 ['Tôi có 1 mục tiêu học kỳ đo được', 'Tôi chia được 3 mốc và 1 việc tuần này', 'Tôi dùng vòng tự học cho ít nhất 1 buổi'],
 ['Hỏi con chọn mục tiêu gì và vì sao, trước khi góp ý.', 'Khen việc con làm đều (số buổi, số đề), không chỉ khen điểm.',
  'Thầy cô có thể dành 5 phút đầu giờ để học sinh viết kế hoạch buổi học.'],
 [lb('Đã xác nhận', f'Dạy siêu nhận thức và tự điều chỉnh việc học: trung bình khoảng +7 tháng tiến bộ trong một năm ({EEF}). Bằng chứng chủ yếu từ trường học, có thầy cô dạy.'),
  lb('Đã xác nhận', f'Câu Nếu… thì… giúp đạt mục tiêu tốt hơn (tổng hợp 94 nghiên cứu, {GS}); thử nghiệm nhỏ với học sinh THPT cho kết quả tương tự ({DUCK}).'),
  lb('Suy luận', 'Khóa tự học này chưa được thử nghiệm. Mức +7 tháng là của chương trình ở trường, không phải của khóa này.'),
  lb('Đánh giá chuyên môn', 'Bảng chia ngược mục tiêu và mẫu kế hoạch buổi học do daynentang.com soạn.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Tự học – tự quản, bài 2: xếp lịch tuần theo thứ tự việc cố định – khối học chính – chỗ trống, sửa thói quen đoán thiếu thời gian.',
 ['Xếp <strong>lịch tuần</strong> theo 3 bước: việc cố định, khối học chính, chỗ trống.',
  'Ghi thời gian <strong>ước lượng và thực tế</strong> cho 3 việc học.',
  'Mỗi ngày chọn <strong>1–3 việc quan trọng nhất</strong>.'],
 [f'In trang 2 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Thời khóa biểu, giờ làm thêm (nếu có), danh sách hạn nộp.'],
 ['<strong>Quản lý thời gian có ích, nhưng không thần kỳ.</strong> Tổng hợp 158 nghiên cứu: liên quan tích cực với kết quả học, rõ hơn với hài lòng cuộc sống và bớt căng thẳng.',
  '<strong>Đó là mối liên quan,</strong> chưa chứng minh lập lịch làm điểm cao hơn. Nhưng lịch rõ giúp bạn bớt quên hạn và bớt lo.',
  '<strong>Ai cũng hay đoán thiếu thời gian.</strong> Một nghiên cứu: sinh viên đoán làm xong luận văn trong khoảng 34 ngày, thực tế mất khoảng 55 ngày.',
  '<strong>Cách sửa:</strong> xem lần trước việc tương tự mất bao lâu. Không biết thì ước lượng rồi cộng thêm một nửa.',
  '<strong>Xếp lịch theo thứ tự:</strong> (1) việc cố định: lớp học, đi lại, ngủ, ăn, làm thêm; (2) khối học chính 45–90 phút cho việc khó; (3) chỗ trống.',
  '<strong>Việc lớn chia nhỏ,</strong> mỗi phần có hạn riêng. "Viết tiểu luận" thành "tìm 5 tài liệu", "lập dàn ý", "viết phần 1"…',
  '<strong>Chừa chỗ trống.</strong> Lịch kín 100% sẽ vỡ khi có việc phát sinh. Chỗ trống cũng là lúc nghỉ thật.'],
 '<p><strong>Bài 1: lịch tuần.</strong> Viết việc cố định trước, rồi khối học chính, cuối cùng đánh dấu chỗ trống.</p>'
 + table(['Buổi'] + DAYS, [['Sáng'] + [''] * 7, ['Chiều'] + [''] * 7, ['Tối'] + [''] * 7])
 + '<p><strong>Bài 2: ước lượng và thực tế.</strong></p>'
 + table(['Việc', 'Ước lượng', 'Thực tế', 'Lệch bao nhiêu?'], [['1.', '', '', ''], ['2.', '', '', ''], ['3.', '', '', '']]),
 ol(['So lịch tuần với một bạn học. Mỗi người góp ý 1 điểm.', 'Cuối tuần xem lại: khối học nào giữ được, khối nào vỡ, vì sao?',
     'Hoặc viết: "Việc mình hay đoán thiếu thời gian nhất là…"']),
 ['Lịch có giờ ngủ trước, rồi mới đến giờ học. Không lấy giờ ngủ bù cho việc học.',
  'Đi làm thêm buổi tối: tính cả thời gian đi lại an toàn về nhà.'],
 ['Tôi xếp lịch tuần theo 3 bước', 'Tôi ghi ước lượng và thực tế cho 3 việc', 'Tôi chọn 1–3 việc quan trọng mỗi ngày'],
 ['Giúp con thấy toàn bộ lịch: việc nhà, giờ ăn chung, giờ ngủ. Thống nhất trước khi con xếp giờ học.',
  'Không xếp thêm lớp học thêm kín lịch khi chưa hỏi con.', 'Kể cách bố mẹ lên kế hoạch cho một việc lớn ở cơ quan.'],
 [lb('Đã xác nhận', f'Tổng hợp 158 nghiên cứu, hơn 53.000 người: quản lý thời gian liên quan tích cực với kết quả học (yếu hơn với công việc), liên quan rõ hơn với hài lòng cuộc sống và ít căng thẳng ({AEON}).'),
  lb('Đã xác nhận', f'Sinh viên đoán làm luận văn khoảng 33,9 ngày, thực tế khoảng 55,5 ngày; chỉ khoảng 30% xong đúng dự đoán ({BUE}).'),
  lb('Đánh giá chuyên môn', 'Thứ tự xếp lịch, khối học 45–90 phút và mẹo "cộng thêm một nửa" là lời khuyên chung do daynentang.com soạn, chưa có thử nghiệm riêng.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Tự học – tự quản, bài 3: đọc chủ động bằng câu hỏi, gấp sách nói lại, ghi chú hai cột, tóm tắt bằng lời mình.',
 ['Đọc 1 bài theo <strong>4 bước</strong>: lướt, đặt câu hỏi, đọc từng đoạn, gấp sách nói lại.',
  'Ghi chú 1 bài theo <strong>trang hai cột</strong> và tóm tắt <strong>2–3 câu</strong>.',
  'Ghi rõ <strong>nguồn</strong> khi dùng ý của người khác.'],
 [f'In trang 3 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Một bài đọc hoặc chương sách của môn bạn đang học.'],
 ['<strong>Đọc lại và tô màu dễ làm, cảm giác như đang học.</strong> Một tổng quan lớn xếp đọc lại, tô màu, gạch chân vào nhóm ít hữu ích.',
  '<strong>Đọc chủ động</strong> nghĩa là đọc để trả lời câu hỏi. Trước khi đọc, lướt tiêu đề, hình, câu in đậm. Viết 2–3 câu hỏi.',
  '<strong>Đọc từng đoạn,</strong> rồi gấp sách và nói lại ý chính bằng lời mình. Nói không được? Đọc lại đúng đoạn đó.',
  '<strong>Tự hỏi "vì sao điều này đúng?"</strong> và tự giải thích từng bước. Cách này giúp nối kiến thức mới với điều bạn đã biết.',
  '<strong>Trang ghi chú hai cột:</strong> cột phải ghi ý chính, ví dụ, sơ đồ. Cột trái ghi câu hỏi, từ khóa. Cuối trang tóm tắt 2–3 câu.',
  '<strong>Viết tay hay gõ máy đều được.</strong> Điều quan trọng là ghi bằng lời mình, không chép nguyên văn lời giảng viên.',
  '<strong>Ghi nguồn</strong> mỗi khi chép ý của sách, bài báo, trang web. Dùng ý người khác mà không ghi nguồn là đạo văn.'],
 '<p><strong>Bài 1: câu hỏi trước khi đọc.</strong></p>'
 + lines(['Câu hỏi 1', 'Câu hỏi 2', 'Câu hỏi 3'])
 + '<p><strong>Bài 2: ghi chú hai cột.</strong></p>'
 + table(['Câu hỏi, từ khóa', 'Ý chính bằng lời mình'], [['', ''], ['', ''], ['', ''], ['', '']])
 + '<p><strong>Tóm tắt 2–3 câu:</strong> ………………………………………… · <strong>Nguồn:</strong> tác giả, tên sách/bài, năm, trang.</p>',
 ol(['Đổi trang ghi chú với một bạn học. Mỗi người dùng cột trái để hỏi bạn kia.', 'Hỏi thầy cô 1 câu bạn chưa trả lời được.',
     'Hoặc viết: "Điều mới nhất mình hiểu hôm nay là…"']),
 ['Đọc lâu trên màn hình: cứ 20–30 phút nhìn ra xa một lúc, giữ đủ sáng.', 'Không chụp đăng tài liệu có bản quyền lên mạng.'],
 ['Tôi đọc theo 4 bước', 'Tôi ghi chú hai cột và tóm tắt', 'Tôi ghi nguồn khi dùng ý người khác'],
 ['Hỏi con "con đọc để trả lời câu hỏi gì?" thay vì "con học bao lâu rồi?".', 'Thầy cô có thể cho học sinh viết câu hỏi trước bài đọc.',
  'Nhắc con: ghi nguồn là trung thực, không phải thủ tục.'],
 [lb('Đã xác nhận', f'Đọc lại, tô màu và gạch chân, tóm tắt được xếp mức hữu ích thấp trong tổng quan 10 cách học ({DUN}).'),
  lb('Cần kiểm chứng', 'Mức xếp hạng cụ thể của "tự hỏi vì sao" và "tự giải thích" trong tổng quan trên: chúng tôi mới đọc thông cáo, chưa đọc toàn văn.'),
  lb('Đánh giá chuyên môn', 'So sánh viết tay và gõ máy: các nghiên cứu cho kết quả chưa thống nhất. Bài này chỉ khuyên ghi bằng lời mình.'),
  lb('Đánh giá chuyên môn', 'Bốn bước đọc và trang ghi chú hai cột do daynentang.com soạn, dựa trên cách ghi chú phổ biến.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Tự học – tự quản, bài 4: tự kiểm tra bằng thẻ hỏi – đáp và ôn giãn cách thay vì đọc lại và học dồn.',
 ['Làm <strong>10 thẻ tự kiểm tra</strong> cho 1 môn.',
  'Ôn theo lịch giãn cách <strong>ít nhất 3 lần</strong> trong 2 tuần.',
  'Giải thích được vì sao <strong>"thấy khó khi nhớ ra"</strong> là dấu hiệu tốt.'],
 [f'In trang 4 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Giấy cắt thành thẻ nhỏ, hoặc gấp đôi tờ giấy: một bên câu hỏi, một bên đáp án.'],
 ['<strong>Hai cách học được xếp hữu ích nhất:</strong> tự kiểm tra (gấp sách, tự nhớ ra) và ôn giãn cách (chia nhỏ việc ôn ra nhiều lần).',
  '<strong>Tự kiểm tra không phải thi.</strong> Đó là bất kỳ lúc nào bạn tự nhớ ra mà không nhìn: trả lời thẻ, làm đề, giảng lại cho bạn.',
  '<strong>Thẻ hỏi – đáp:</strong> mặt trước một câu hỏi, mặt sau đáp án. Trả lời ra miệng hoặc ra giấy trước, rồi mới lật.',
  '<strong>Thấy khó là đang học.</strong> Đọc lại cho cảm giác quen, nên dễ tưởng mình đã nhớ. Cố nhớ ra mới làm trí nhớ bền hơn.',
  '<strong>Ôn giãn cách:</strong> 4 lần ôn 30 phút cách nhau vài ngày tốt hơn một buổi 2 giờ trước hôm thi.',
  '<strong>Khoảng cách bao nhiêu?</strong> Muốn nhớ càng lâu, khoảng ôn càng dài. Gợi ý: sau 1 ngày, 3 ngày, 1 tuần, 3 tuần.',
  '<strong>Bớt hồi hộp:</strong> trong một khảo sát, nhiều học sinh nói tự kiểm tra thường xuyên làm các em bớt lo trước bài thi.'],
 '<p><strong>Bài 1: 10 thẻ.</strong> Viết 10 câu hỏi từ trang ghi chú bài 3. Mỗi câu một thẻ.</p>'
 + table(['Thẻ', 'Câu hỏi', 'Lần 1 ✓/✗', 'Lần 2', 'Lần 3'], [[str(n), '', '', '', ''] for n in range(1, 11)])
 + '<p><strong>Bài 2: lịch ôn.</strong> Ngày học: …… · +1 ngày: …… · +3 ngày: …… · +1 tuần: …… · +3 tuần: ……</p>'
 + '<p class="small">Thẻ trả lời đúng 3 lần liên tiếp: chuyển sang chồng "ôn thưa". Thẻ sai: giữ ở chồng "ôn sớm".</p>',
 ol(['Đổi thẻ với một bạn học và hỏi nhau 10 phút.', 'Giảng lại một ý khó cho người trong nhà bằng lời đơn giản.',
     'Hoặc viết: "Thẻ khó nhất của mình là… vì…"']),
 ['Ôn giãn cách giúp tránh thức khuya học dồn đêm trước khi thi.', 'Thấy mình sai nhiều thẻ là bình thường lúc đầu. Không tự chê.'],
 ['Tôi làm 10 thẻ tự kiểm tra', 'Tôi ôn ít nhất 3 lần theo lịch', 'Tôi trả lời trước rồi mới lật thẻ'],
 ['Khi con ôn, hỏi con bằng thẻ thay vì bảo con "đọc lại đi".', 'Thầy cô có thể cho bài kiểm tra ngắn không tính điểm để học sinh tự nhớ ra.',
  'Khen con khi con nhận ra mình chưa nhớ, vì đó là lúc con biết cần ôn gì.'],
 [lb('Đã xác nhận', f'Tự kiểm tra và ôn giãn cách được xếp mức hữu ích cao nhất trong 10 cách học ({DUN}).'),
  lb('Đã xác nhận', f'Tổng hợp 317 thí nghiệm: khoảng cách ôn cho kết quả tốt nhất tăng dần khi thời gian cần nhớ dài ra ({CEP}).'),
  lb('Đã xác nhận', f'Khảo sát 1.408 học sinh THCS, THPT ở Mỹ: 72% nói tự kiểm tra giúp bớt lo trước bài kiểm tra ({AGA}). Đây là tự báo cáo.'),
  lb('Đánh giá chuyên môn', 'Lịch +1 ngày, +3 ngày, +1 tuần, +3 tuần và cách chia hai chồng thẻ là gợi ý, không phải con số nghiên cứu đưa ra.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Tự học – tự quản, bài 5: khối tập trung 25–50 phút, cất điện thoại xa, tắt thông báo, ghi ý chen ngang ra giấy.',
 ['Làm <strong>ít nhất 5 khối tập trung</strong> trong tuần, điện thoại để xa.',
  'Đếm <strong>số lần muốn cầm máy</strong> trong mỗi khối.',
  'Chọn <strong>1 chỗ học</strong> cố định và dọn gọn.'],
 [f'In trang 5 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Đồng hồ hoặc hẹn giờ không phải điện thoại (nếu có). Một tờ giấy nháp để ghi ý chen ngang.'],
 ['<strong>"Làm nhiều việc cùng lúc"</strong> thường là chuyển qua lại giữa các việc. Mỗi lần chuyển, bạn mất thêm thời gian để quay lại mạch.',
  '<strong>Một thử nghiệm trong lớp:</strong> 118 sinh viên. Buổi cho dùng thiết bị, điểm thi cuối kỳ thấp hơn ít nhất 5%. Cả bạn không dùng cũng bị ảnh hưởng.',
  '<strong>Khối tập trung:</strong> chọn 1 việc, cất máy ở phòng khác hoặc trong túi, tắt thông báo, học 25–50 phút, nghỉ 5–10 phút.',
  '<strong>Chưa có con số "chuẩn"</strong> cho độ dài khối học. Hãy thử 25 phút trước, rồi tăng dần nếu bạn giữ được.',
  '<strong>Ý chen ngang</strong> ("phải nhắn bạn", "tra cái này"): ghi ra giấy nháp, làm sau khối học.',
  '<strong>Chỗ học cố định:</strong> bàn gọn, đủ sáng, chỉ để đồ của môn đang học. Ở ký túc xá ồn thì thử thư viện.',
  '<strong>Dùng điện thoại có mục đích.</strong> Cần tra từ điển hay xem bài giảng? Mở đúng ứng dụng đó, xong thì cất.'],
 '<p><strong>Ghi 5 khối tập trung.</strong></p>'
 + table(['Khối', 'Việc', 'Số phút', 'Số lần muốn cầm máy', 'Làm được bao nhiêu?'], [[str(n), '', '', '', ''] for n in range(1, 6)])
 + '<p><strong>Chỗ học của tôi:</strong> …………… · <strong>Điện thoại để ở:</strong> …………… · <strong>Thông báo tắt:</strong> ☐</p>',
 ol(['Rủ một bạn học cùng làm khối tập trung, mỗi người một việc, cùng cất máy.', 'So số lần muốn cầm máy ở khối đầu và khối cuối.',
     'Hoặc viết: "Thứ làm mình mất tập trung nhất là… Mình sẽ…"']),
 ['Đi đường không nhìn điện thoại. Không dùng điện thoại khi đi xe máy, xe đạp.', 'Ngồi lâu: đứng dậy giữa các khối, nhìn ra xa.'],
 ['Tôi làm ít nhất 5 khối tập trung', 'Tôi để điện thoại xa khi học', 'Tôi có chỗ học cố định'],
 ['Cả nhà có giờ yên tĩnh chung: bố mẹ cũng cất máy.', 'Thầy cô có thể thống nhất quy tắc thiết bị trong lớp và giải thích lý do.',
  'Không lấy máy của con để phạt. Cùng con thống nhất chỗ để máy khi học.'],
 [lb('Đã xác nhận', f'Thử nghiệm với 118 sinh viên: buổi cho dùng thiết bị, điểm thi cuối kỳ thấp hơn ít nhất 5% (khoảng nửa bậc điểm), kể cả người không dùng ({GK}).'),
  lb('Suy luận', 'Thử nghiệm làm ở một lớp đại học ở Mỹ. Kết quả có thể khác ở lớp khác hay khi tự học ở nhà.'),
  lb('Đánh giá chuyên môn', 'Khối 25–50 phút, ghi ý chen ngang và chỗ học cố định là lời khuyên chung, chưa có thử nghiệm riêng cho từng mẹo.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Tự học – tự quản, bài 6: họp nhóm đầu tiên, bảng phân công, xử lý bất đồng và khi bạn chưa làm phần mình.',
 ['Lập <strong>bảng phân công</strong> cho 1 việc nhóm: việc – người – hạn – trạng thái.',
  'Dẫn hoặc tham gia <strong>buổi họp nhóm đầu</strong> theo 4 mục.',
  'Viết sẵn <strong>1 câu nhắc</strong> khi bạn cùng nhóm chậm phần mình.'],
 [f'In trang 6 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Đề bài nhóm và hạn nộp. Nếu chưa có việc nhóm, chọn một việc chung trong nhà.'],
 ['<strong>Học hợp tác có tác dụng.</strong> Tổng hợp 59 nghiên cứu: kết quả học tốt hơn mức trung bình so với chỉ nghe giảng cả lớp.',
  '<strong>Nhóm tốt cần ba điều:</strong> mục tiêu chung, mỗi người có phần rõ ràng, ai cũng chịu trách nhiệm phần mình.',
  '<strong>Buổi họp đầu có 4 mục:</strong> mục tiêu chung, chia việc, hạn từng phần, cách liên lạc và quy tắc (trả lời tin trong bao lâu).',
  '<strong>Bảng phân công</strong> giúp ai cũng thấy việc của mình và của nhóm. Cập nhật trạng thái mỗi tuần.',
  '<strong>Khi bất đồng:</strong> nói về việc, không nói về người. "Phần này thiếu số liệu" thay vì "bạn làm ẩu". Đưa ra 2 lựa chọn rồi cùng chọn.',
  '<strong>Khi bạn chưa làm phần mình:</strong> nhắc riêng, sớm, kèm hạn mới. Hỏi bạn cần giúp gì. Vẫn không được thì báo giảng viên kèm bảng phân công.',
  '<strong>Trung thực trong nhóm:</strong> không đứng tên phần mình không làm, không làm hộ người khác rồi ghi tên họ.'],
 '<p><strong>Bài 1: bảng phân công.</strong></p>'
 + table(['Việc', 'Người làm', 'Hạn', 'Trạng thái'], [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']])
 + '<p><strong>Bài 2: quy tắc nhóm.</strong> Trả lời tin nhắn trong …… giờ · Họp mỗi …… · Khi trễ hạn thì ……</p>'
 + '<p><strong>Bài 3: câu nhắc của tôi.</strong> Ví dụ: <em>"Phần của bạn hạn hôm qua. Bạn gửi được trước tối thứ Năm không? Cần mình giúp gì thì nói nhé."</em></p>'
 + lines(['Câu nhắc của tôi']),
 ol(['Sau buổi họp đầu, gửi bảng phân công cho cả nhóm.', 'Cuối tuần, mỗi người nói 1 việc đã xong và 1 việc vướng.',
     'Hoặc viết: "Vai trò mình làm tốt trong nhóm là…"']),
 ['Họp nhóm với người lạ: chọn nơi công cộng như thư viện, quán ăn. Báo người nhà nơi bạn đến.',
  'Không chia sẻ mật khẩu tài khoản học tập cho bạn cùng nhóm.'],
 ['Tôi lập bảng phân công', 'Tôi họp nhóm theo 4 mục', 'Tôi có câu nhắc lịch sự khi bạn chậm'],
 ['Hỏi con nhóm đang chia việc thế nào, ai vướng gì, trước khi hỏi điểm.', 'Thầy cô có thể chấm cả phần cá nhân để ai cũng chịu trách nhiệm.',
  'Họp gia đình là chỗ con tập dẫn họp (xem Biên bản họp gia đình ở mục Công cụ).'],
 [lb('Đã xác nhận', f'Tổng hợp 59 nghiên cứu: học hợp tác có tác dụng mức trung bình lên kết quả học (ES = 0,54) so với dạy cả lớp thông thường; tác dụng lên thái độ nhỏ (ES = 0,15) ({KYN}).'),
  lb('Suy luận', 'Các nghiên cứu này là học nhóm có thầy cô tổ chức trong lớp. Nhóm tự lập của sinh viên có thể cho kết quả khác.'),
  lb('Đánh giá chuyên môn', 'Bốn mục họp đầu, bảng phân công và câu nhắc mẫu do daynentang.com soạn.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Tự học – tự quản, bài 7: lịch ôn ba tuần, làm đề bấm giờ, phân loại lỗi, bình tĩnh trong phòng thi, tuân thủ quy chế.',
 ['Lập <strong>lịch ôn ba tuần</strong> ngược từ ngày thi.',
  'Làm <strong>1 đề bấm giờ</strong> và phân loại mọi lỗi theo <strong>4 loại</strong>.',
  'Nói được <strong>quy định về vật dụng cấm</strong> trong phòng thi.'],
 [f'In trang 7 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Một đề thi cũ hoặc đề luyện, đồng hồ bấm giờ.'],
 ['<strong>Ôn ngược từ ngày thi,</strong> bắt đầu sớm 3–4 tuần. Tuần 1 hệ thống kiến thức, tuần 2 làm đề, tuần 3 sửa lỗi và ôn phần yếu.',
  '<strong>Làm đề như thi thật:</strong> bấm giờ, không xem đáp án, không cầm điện thoại. Đây cũng là tự kiểm tra (bài 4).',
  '<strong>Phân loại lỗi sau mỗi đề:</strong> chưa biết, nhầm hay ẩu, đọc sai đề, hết giờ. Mỗi loại cần cách sửa khác.',
  '<strong>Trộn dạng bài khi luyện.</strong> Làm xen nhiều dạng giúp bạn tập nhận ra dạng nào dùng cách nào, như lúc thi thật.',
  '<strong>Đêm trước khi thi:</strong> ôn nhẹ phần tóm tắt, chuẩn bị giấy tờ, ngủ đủ. Không thức trắng.',
  f'<strong>Trong phòng thi:</strong> đọc hết đề, làm câu chắc trước, đánh dấu câu khó để quay lại. Hồi hộp thì thở chậm 1 phút (xem <a href="{C2E}">bài 3 khóa Hiểu mình</a>).',
  '<strong>Thi trung thực.</strong> Quy chế thi tốt nghiệp THPT cấm mang thiết bị thu phát, ghi âm, ghi hình vào phòng thi. Vi phạm có thể bị đình chỉ, hủy kết quả cả kỳ.'],
 '<p><strong>Bài 1: lịch ôn ba tuần.</strong> Ngày thi: ……………</p>'
 + table(['Tuần', 'Việc chính', 'Môn, chương', 'Xong? ✓'], [['1', 'Hệ thống kiến thức', '', ''], ['2', 'Làm đề bấm giờ', '', ''], ['3', 'Sửa lỗi, ôn phần yếu', '', '']])
 + '<p><strong>Bài 2: bảng lỗi sau đề.</strong></p>'
 + table(['Loại lỗi', 'Số câu', 'Cách sửa'], [['Chưa biết', '', 'Học lại phần đó, làm thêm thẻ'], ['Nhầm, ẩu', '', 'Soát lại, viết rõ từng bước'],
                                         ['Đọc sai đề', '', 'Gạch chân từ khóa trước khi làm'], ['Hết giờ', '', 'Làm câu chắc trước, chia giờ theo điểm']]),
 ol(['Kể lịch ôn cho người trong nhà để cả nhà biết tuần nào bạn cần yên tĩnh.', 'Cùng bạn học chấm đề cho nhau.',
     'Hoặc viết: "Loại lỗi mình gặp nhiều nhất là… Mình sẽ…"']),
 ['Không dùng thuốc "tăng trí nhớ", thuốc ngủ hay chất kích thích để ôn thi.',
  'Lo âu thi cử làm bạn mất ngủ, bỏ ăn nhiều ngày: nói với người tin cậy (xem bài 10).',
  'Để điện thoại, đồng hồ thông minh ở nơi quy định trước khi vào phòng thi.'],
 ['Tôi có lịch ôn ba tuần', 'Tôi làm 1 đề bấm giờ và phân loại lỗi', 'Tôi biết quy định vật dụng cấm'],
 ['Không so điểm của con với con người khác. Hỏi "loại lỗi nào con gặp nhiều nhất?".', 'Lo bữa ăn, giấc ngủ, đưa đón cho con mùa thi. Đó là phần bố mẹ giúp được nhiều nhất.',
  'Trước ngày thi, kiểm tra cùng con giấy tờ, đồ dùng được phép mang.'],
 [lb('Đã xác nhận', f'Thông tư 24/2024/TT-BGDĐT (quy chế thi tốt nghiệp THPT, ban hành 24/12/2024), Điều 57: mang vật dụng cấm vào phòng thi bị đình chỉ thi; bị 0 điểm môn đó và hủy kết quả cả kỳ ({QC}).'),
  lb('Suy luận', 'Điện thoại thuộc nhóm "thiết bị thu, phát thông tin" nên thuộc vật dụng cấm. Chúng tôi chưa đọc nguyên văn Điều 21 của Thông tư.'),
  lb('Cần kiểm chứng', 'Có văn bản sửa đổi quy chế thi áp dụng cho kỳ thi 2027 hay không. Thí sinh xem hướng dẫn chính thức của Bộ GD&amp;ĐT và trường mỗi năm.'),
  lb('Cần kiểm chứng', 'Mức xếp hạng của "học xen kẽ dạng bài" trong tổng quan Dunlosky 2013: chúng tôi chưa đọc toàn văn.'),
  lb('Đánh giá chuyên môn', 'Lịch ôn ba tuần và bảng 4 loại lỗi do daynentang.com soạn.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Tự học – tự quản, bài 8: ngủ đủ theo tuổi, vận động mỗi tuần, ăn đủ bữa, không thức trắng mùa thi.',
 ['Nói được <strong>số giờ ngủ</strong> và <strong>mức vận động</strong> khuyến nghị cho tuổi mình.',
  'Ghi <strong>giờ ngủ 7 ngày</strong>.',
  'Vận động đủ mức khuyến nghị trong <strong>1 tuần</strong>.'],
 [f'In trang 8 của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Chọn giờ lên giường và giờ dậy cố định cho tuần này.'],
 ['<strong>Ngủ theo tuổi:</strong> 13–18 tuổi cần 8–10 giờ mỗi đêm. Người lớn từ 18 tuổi cần từ 7 giờ trở lên. Người trẻ có thể cần hơn 9 giờ.',
  '<strong>Thức trắng ôn thi</strong> làm khó tập trung và học kém đi. Ngủ đủ là một phần của việc ôn, không phải thời gian bỏ phí.',
  '<strong>Vận động:</strong> 5–17 tuổi khoảng 60 phút mỗi ngày. 18–64 tuổi 150–300 phút mỗi tuần mức vừa, và tập cơ ít nhất 2 ngày mỗi tuần.',
  '<strong>150 phút mỗi tuần</strong> là khoảng 30 phút đi bộ nhanh, 5 ngày. Đi bộ đến lớp, đạp xe đều tính.',
  '<strong>Xen vận động vào giờ học:</strong> sau 1–2 khối học, đi bộ 5–10 phút, giãn cơ, uống nước.',
  '<strong>Ăn đủ bữa, mang nước.</strong> Bỏ bữa sáng, ăn vặt thay cơm làm bạn mệt và dễ cáu.',
  '<strong>Ở trọ, ký túc xá ồn:</strong> thử nút bịt tai, rèm che sáng, thống nhất giờ yên tĩnh với bạn cùng phòng.'],
 table(['Ngày', 'Lên giường', 'Dậy', 'Số giờ ngủ', 'Phút vận động'], [[d, '', '', '', ''] for d in DAYS])
 + '<p>Tổng phút vận động trong tuần: …… · Số ngày tập cơ: …… · Đạt khuyến nghị? ☐</p>',
 ol(['Rủ bạn cùng phòng hoặc người trong nhà đi bộ cùng 3 lần trong tuần.', 'Thống nhất giờ yên tĩnh buổi tối với người ở cùng.',
     'Hoặc viết: "Điều làm mình ngủ muộn nhất là… Mình sẽ thử…"']),
 ['Mất ngủ kéo dài nhiều tuần, ngáy to, ngừng thở khi ngủ: đi khám.',
  'Không dùng nước tăng lực hay cà phê để thức xuyên đêm. Không dùng thuốc ngủ khi không có bác sĩ kê đơn.',
  'Vận động mới: tăng dần, uống đủ nước, dừng khi đau ngực, choáng, khó thở.'],
 ['Tôi biết giờ ngủ và vận động khuyến nghị', 'Tôi ghi giờ ngủ 7 ngày', 'Tôi vận động đủ mức trong tuần'],
 ['Mùa thi, giữ giờ ăn tối và giờ ngủ chung của cả nhà.', 'Không khen con "thức khuya học giỏi". Khen con ngủ đủ và học đều.',
  'Rủ con đi bộ buổi tối, không nói chuyện điểm số.'],
 [lb('Đã xác nhận', f'Tuổi 13–18 cần ngủ 8–10 giờ mỗi 24 giờ ({AASM}).'),
  lb('Đã xác nhận', f'Người lớn 18–60 tuổi nên ngủ từ 7 giờ mỗi đêm; ngủ hơn 9 giờ có thể phù hợp với người trẻ ({AASMA}).'),
  lb('Đã xác nhận', f'Thiếu ngủ ảnh hưởng chú ý, kiềm chế và việc học ở tuổi teen ({NIMH}).'),
  lb('Đã xác nhận', f'Người lớn 18–64 tuổi: ít nhất 150 phút vận động vừa (hoặc 75 phút mạnh) mỗi tuần, tốt hơn nữa là 300 phút; tập cơ ít nhất 2 ngày ({WHOPA}). Tuổi 5–17: khoảng 60 phút mỗi ngày ({PA}).'),
  lb('Đánh giá chuyên môn', 'Mẹo xen vận động giữa giờ học, nút bịt tai, giờ yên tĩnh chung là lời khuyên chung do daynentang.com soạn.')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Tự học – tự quản, bài 9: ghi chi 7 ngày, chia tiền tháng theo 4 phần, cần và muốn, nhận ra lừa đảo nhắm vào học sinh, sinh viên.',
 ['Ghi <strong>mọi khoản chi trong 7 ngày</strong>.',
  'Chia tiền tháng theo <strong>4 phần</strong>: cố định, ăn uống, dự phòng, phần còn lại.',
  'Nêu được <strong>4 dấu hiệu lừa đảo</strong> và việc cần làm ngay.'],
 [f'In trang 9 của <a href="{TOOL}">Sổ tự quản học kỳ</a>, hoặc dùng <a href="{BTC}">Bảng thu chi</a>.', 'Số tiền nhận mỗi tháng (gia đình gửi, học bổng, làm thêm).'],
 ['<strong>Biết tiền vào, tiền ra.</strong> Tiền vào: gia đình gửi, học bổng, làm thêm. Tiền ra cố định: trọ, điện nước, đi lại. Tiền ra thay đổi: ăn, mua sắm, giải trí.',
  '<strong>Ghi chi 7 ngày</strong> trước khi lập kế hoạch. Nhiều khoản nhỏ như trà sữa, phí giao hàng cộng lại thành số lớn.',
  '<strong>Chia ngay khi nhận tiền:</strong> (1) khoản cố định; (2) ăn uống; (3) dự phòng nhỏ cho ốm đau, hỏng xe; (4) phần còn lại.',
  '<strong>Cần hay muốn?</strong> Muốn mua thứ không cần: chờ 24 giờ rồi quyết. Nhiều lần bạn sẽ không mua nữa.',
  '<strong>Làm thêm:</strong> chọn giờ không lấn giờ học chính và giờ ngủ. Hỏi rõ công việc, giờ làm, tiền công, cách trả trước khi nhận.',
  '<strong>Dấu hiệu lừa đảo:</strong> việc nhẹ lương cao, đòi đặt cọc hay "phí hồ sơ", mượn tài khoản ngân hàng hay căn cước, đe dọa và bắt giữ bí mật.',
  '<strong>Gặp dấu hiệu đó:</strong> dừng, không chuyển tiền, không gửi mã OTP, gọi cho gia đình hoặc người tin cậy. Bị đe dọa thì báo công an (113).'],
 table(['Ngày', 'Khoản chi', 'Số tiền', 'Cần / Muốn'], [[d, '', '', ''] for d in DAYS])
 + '<p><strong>Chia tiền tháng.</strong> Tổng nhận: ……………</p>'
 + table(['Phần', 'Số tiền', 'Ghi chú'], [['1. Cố định', '', ''], ['2. Ăn uống', '', ''], ['3. Dự phòng', '', ''], ['4. Phần còn lại', '', '']]),
 ol(['Cùng gia đình xem bảng chi 7 ngày. Hỏi bố mẹ cách họ chia tiền tháng.', 'Lưu số điện thoại một người lớn để gọi ngay khi nghi lừa đảo.',
     'Hoặc viết: "Khoản chi làm mình bất ngờ nhất là…"']),
 ['Không cho mượn, không bán tài khoản ngân hàng, thẻ, căn cước, số điện thoại.',
  'Không vay qua ứng dụng hay người lạ trên mạng. Khó khăn tiền bạc: nói với gia đình, thầy cô chủ nhiệm hoặc phòng công tác sinh viên.',
  f'Bị dụ đi gặp người lạ, bị yêu cầu "cách ly" khỏi gia đình: dừng và gọi người nhà ngay (xem khóa <a href="{C1}">Lớn lên an toàn</a>).'],
 ['Tôi ghi chi 7 ngày', 'Tôi chia tiền tháng theo 4 phần', 'Tôi nêu được 4 dấu hiệu lừa đảo'],
 ['Thống nhất với con số tiền mỗi tháng và để con tự chia. Hỏi con về bảng chi, không chỉ trích từng khoản.',
  f'Bố mẹ xem thêm khóa <a href="{G6}">Tiền nhà mình</a>.', 'Dặn con: ai gọi báo con bị bắt, cần chuyển tiền gấp, gia đình sẽ gọi lại kiểm tra trước.'],
 [lb('Đã xác nhận', f'Bộ Công an cảnh báo các chiêu "bắt cóc online" nhắm vào học sinh, sinh viên: giả danh đe dọa, làm thân lâu ngày, dụ bằng việc làm hay tiền ({VOH}).'),
  lb('Đánh giá chuyên môn', 'Cách chia tiền 4 phần, chờ 24 giờ và các dấu hiệu lừa đảo là lời khuyên chung do daynentang.com soạn. Bài chỉ dạy thu chi cơ bản, không tư vấn vay hay đầu tư.'),
  lb('Cần kiểm chứng', 'Hiệu quả của khóa tự học về quản lý tiền cho sinh viên: chúng tôi chưa tìm được thử nghiệm phù hợp.')])

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Tự học – tự quản, bài 10: dấu hiệu quá tải, cách giảm tải, xin gia hạn, tìm người giúp, xem lại học kỳ.',
 ['Viết <strong>3 dấu hiệu quá tải</strong> của mình và <strong>kế hoạch 3 bước</strong> khi gặp.',
  'Viết tên <strong>3 người hoặc nơi</strong> có thể nhờ giúp.',
  'Hoàn thành <strong>phiếu xem lại học kỳ</strong> và tự đánh giá cuối khóa.'],
 [f'In trang 10 và phần tự đánh giá của <a href="{TOOL}">Sổ tự quản học kỳ</a>.', 'Danh sách mọi việc đang phải làm.'],
 ['<strong>Mệt vài ngày mùa thi là bình thường.</strong> Nghỉ ngơi, ngủ đủ thì hồi lại.',
  '<strong>Nên nói sớm khi:</strong> mệt, buồn hay lo kéo dài nhiều tuần; mất ngủ, bỏ ăn; trì hoãn mọi việc; bỏ học; không muốn gặp ai; tự chê mình nặng nề.',
  '<strong>Nói ngay khi:</strong> bạn nghĩ đến cái chết, muốn làm đau bản thân, hoặc bạn bè nói với bạn điều đó.',
  '<strong>Giảm tải 3 bước:</strong> (1) viết hết việc ra giấy; (2) gạch việc có thể bỏ, hoãn, nhờ; (3) chọn 1 việc làm 15 phút ngay.',
  '<strong>Xin gia hạn sớm,</strong> trước hạn nộp, kèm lý do ngắn và ngày bạn sẽ nộp. Xin muộn sau hạn thường khó hơn nhiều.',
  '<strong>Kỹ năng ngắn khi căng thẳng:</strong> WHO có sách minh họa miễn phí, có bản tiếng Việt, mỗi bài tập chỉ vài phút một ngày.',
  '<strong>Người có thể giúp:</strong> gia đình, thầy cô chủ nhiệm, cố vấn học tập, phòng tư vấn tâm lý của trường (nếu trường có), bác sĩ.',
  '<strong>Xem lại học kỳ:</strong> điều nên giữ, điều nên bỏ, một cách mới sẽ thử, mục tiêu kỳ tới. Rồi quay lại bài 1.'],
 '<p><strong>Bài 1: kế hoạch khi quá tải.</strong></p>'
 + lines(['3 dấu hiệu của tôi', 'Bước 1: viết hết việc', 'Bước 2: bỏ, hoãn, nhờ việc gì?', 'Bước 3: việc 15 phút đầu tiên', 'Người 1', 'Người 2', 'Nơi giúp ở trường'])
 + '<p><strong>Bài 2: xem lại học kỳ.</strong></p>'
 + table(['Câu hỏi', 'Của tôi'], [['Cách học nên giữ', ''], ['Thói quen nên bỏ', ''], ['Một cách mới sẽ thử', ''], ['Mục tiêu kỳ tới', '']]),
 ol(['Cùng người tin cậy đọc lại Sổ tự quản. Chỉ đọc phần bạn muốn chia sẻ.', 'Cùng lưu các số khẩn cấp vào điện thoại.',
     'Kể một điều bạn tự quản tốt hơn sau 10 tuần.']),
 ['Bài này không dùng để chẩn đoán. Dấu hiệu kéo dài: gặp bác sĩ hoặc chuyên gia tâm lý.'],
 ['Tôi có kế hoạch 3 bước khi quá tải', 'Tôi có 3 người hoặc nơi để nhờ giúp', 'Tôi hoàn thành phiếu xem lại học kỳ'],
 ['Con mở lời: dừng việc đang làm, nghe hết, cảm ơn con đã nói. Không so sánh, không trách.',
  'Con nói về cái chết hay làm đau bản thân: ở bên con, không để con một mình, gọi 115 hoặc đưa con đến cơ sở y tế.',
  'Thầy cô thấy học sinh bỏ học, sa sút kéo dài: hỏi riêng và báo gia đình hoặc bộ phận tư vấn.'],
 [lb('Đã xác nhận', f'Khoảng 1 trong 7 người 10–19 tuổi có rối loạn tâm thần; lo âu, trầm cảm hay gặp nhất ({WHOA}).'),
  lb('Đã xác nhận', f'Sách minh họa của WHO về quản lý căng thẳng, bài tập vài phút mỗi ngày, có bản tiếng Việt ({DWM}).'),
  lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}). Tra 28/10/2026, kiểm tra lại mỗi quý.'),
  lb('Cần kiểm chứng', 'Không phải trường nào ở Việt Nam cũng có phòng tư vấn tâm lý. Hỏi phòng công tác học sinh, sinh viên của trường bạn.'),
  lb('Đánh giá chuyên môn', 'Danh sách dấu hiệu là tóm tắt chung. Kế hoạch giảm tải 3 bước và phiếu xem lại học kỳ do daynentang.com soạn.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi có mục tiêu học kỳ đo được', 'Tôi xếp lịch tuần và giữ được phần lớn', 'Tôi đọc chủ động và ghi chú bằng lời mình',
         'Tôi ôn bằng tự kiểm tra và giãn cách', 'Tôi học với điện thoại để xa', 'Tôi làm việc nhóm có bảng phân công',
         'Tôi ôn thi sớm và phân loại lỗi', 'Tôi ngủ đủ theo tuổi ít nhất 5/7 đêm', 'Tôi biết mình chi tiền vào đâu',
         'Tôi biết khi nào và với ai để nhờ giúp']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Sổ tự quản học kỳ', 'Trang in cho khóa Tự học – tự quản: mục tiêu, lịch tuần, ghi chú, thẻ ôn, tập trung, phân công nhóm, ôn thi, giấc ngủ, chi tiêu, kế hoạch khi quá tải.',
f'''
<h1>Sổ tự quản học kỳ</h1>
<p>Dùng cho khóa <a href="{U}">Tự học – tự quản</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Sổ là của riêng bạn.</p>
{PRINT_ROW}
<h2>1. Mục tiêu học kỳ (bài 1)</h2>
{table(['Mục', 'Của tôi'], [['Mục tiêu cuối kỳ', ''], ['Mốc giữa kỳ', ''], ['Mốc tháng này', ''], ['Việc tuần này', ''], ['Nếu… thì…', '']])}
<h2>2. Lịch tuần (bài 2)</h2>
{table(['Buổi'] + DAYS, [['Sáng'] + [''] * 7, ['Chiều'] + [''] * 7, ['Tối'] + [''] * 7])}
{table(['Việc', 'Ước lượng', 'Thực tế'], [['1.', '', ''], ['2.', '', ''], ['3.', '', '']])}
<h2>3. Ghi chú hai cột (bài 3)</h2>
{table(['Câu hỏi, từ khóa', 'Ý chính bằng lời mình'], [['', ''], ['', ''], ['', '']])}
<p>Tóm tắt: ……………………………………… · Nguồn: ………………………</p>
<h2>4. Thẻ ôn và lịch giãn cách (bài 4)</h2>
<p>Ngày học: …… · +1 ngày: …… · +3 ngày: …… · +1 tuần: …… · +3 tuần: ……</p>
<h2>5. Khối tập trung (bài 5)</h2>
{table(['Khối', 'Việc', 'Phút', 'Lần muốn cầm máy'], [[str(n), '', '', ''] for n in range(1, 6)])}
<h2>6. Phân công nhóm (bài 6)</h2>
{table(['Việc', 'Người', 'Hạn', 'Trạng thái'], [['', '', '', ''], ['', '', '', ''], ['', '', '', '']])}
<h2>7. Ôn thi (bài 7)</h2>
{table(['Loại lỗi', 'Số câu', 'Cách sửa'], [['Chưa biết', '', ''], ['Nhầm, ẩu', '', ''], ['Đọc sai đề', '', ''], ['Hết giờ', '', '']])}
<h2>8. Ngủ và vận động (bài 8)</h2>
<p>Giờ lên giường: …… · Giờ dậy: …… · Phút vận động tuần này: …… · Số ngày tập cơ: ……</p>
<h2>9. Tiền tháng (bài 9)</h2>
{table(['Phần', 'Số tiền'], [['Cố định', ''], ['Ăn uống', ''], ['Dự phòng', ''], ['Phần còn lại', '']])}
<h2>10. Khi quá tải (bài 10)</h2>
{lines(['3 dấu hiệu của tôi', 'Việc 15 phút đầu tiên', 'Người 1', 'Người 2', 'Nơi giúp ở trường'])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">115</th><td>Cấp cứu y tế</td></tr>
<tr><th>113</th><td>Công an, khi nguy hiểm ngay lúc đó</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
<tr><th>111</th><td>Bảo vệ trẻ em, miễn phí, 24/7</td></tr>
</tbody></table></div>
<h2>Xem lại học kỳ</h2>
{table(['Câu hỏi', 'Của tôi'], [['Nên giữ', ''], ['Nên bỏ', ''], ['Sẽ thử', ''], ['Mục tiêu kỳ tới', '']])}
<h2>Tự đánh giá (tuần 1 và tuần 10)</h2>
<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 10</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Tự học – tự quản', 'Khóa tự học miễn phí cho học sinh lớp 12 và sinh viên: mục tiêu, lịch tuần, đọc và ghi chú, ôn tập, tập trung, làm việc nhóm, thi cử, sức khỏe, tiền, khi quá tải.',
f'''
<p class="eyebrow">Cá nhân · Khóa C3 · Đang thử nghiệm</p>
<h1>Tự học – tự quản</h1>
<p class="lead">Lên đại học, không ai nhắc bạn học nữa. Khóa này giúp bạn tự đặt mục tiêu, tự xếp lịch, học theo cách có bằng chứng, và tự chăm mình.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn tự quản việc học: đặt mục tiêu, xếp lịch, học và ôn hiệu quả, làm việc nhóm, thi trung thực, chăm sức khỏe và tiền bạc, biết nhờ giúp sớm</td></tr>
<tr><th>Dành cho</th><td>Học sinh lớp 12 và sinh viên tự học. Bạn 13–17 tuổi nên xem khóa <a href="{C2}">Hiểu mình</a> trước</td></tr>
<tr><th>Thời lượng</th><td>10 tuần, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, xem lại 5 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút, lịch học kỳ, tài liệu của một môn đang học</td></tr>
<tr><th>Tình trạng</th><td>Đủ 10 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của học sinh, sinh viên và thầy cô</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn có mục tiêu học kỳ và lịch tuần rõ ràng.</li><li>Bạn ôn bằng thẻ tự kiểm tra thay vì đọc lại.</li><li>Bạn học với điện thoại để xa.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: lên kế hoạch, làm và tự theo dõi, xem lại rồi chỉnh.</li><li>Kỹ năng: học có bằng chứng, làm việc nhóm, quản lý tiền cơ bản.</li><li>Biết giảm tải và nhờ giúp sớm.</li></ul></div>
</div>
{figure_block('KHOAD')}

<h2 id="muoi-tuan">Mười tuần</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ tự quản học kỳ</a>: mục tiêu, lịch tuần, ghi chú, thẻ ôn, khối tập trung, phân công nhóm, ôn thi, ngủ, tiền, kế hoạch khi quá tải, tự đánh giá.</li>
<li><a href="{BTC}">Bảng thu chi</a>: ghi chi 7 ngày (dùng ở bài 9).</li></ul>

<h2>Cho bố mẹ, thầy cô (nếu có)</h2>
<ul>
<li>Để con tự chọn mục tiêu và tự xếp lịch. Hỏi "con định làm thế nào?" trước khi góp ý.</li>
<li>Khen việc làm đều: số buổi ôn, số đề, giờ ngủ. Không chỉ khen điểm.</li>
<li>Mùa thi, phần bố mẹ giúp được nhiều nhất là bữa ăn, giấc ngủ, sự yên tĩnh và lắng nghe.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{EEF}</td><td>Vòng tự học: lên kế hoạch, theo dõi, xem lại</td><td><span class="label">[Đã xác nhận]</span> Trung bình khoảng +7 tháng tiến bộ; chủ yếu chương trình ở trường, có thầy cô</td></tr>
<tr><td>{DUN}; {CEP}</td><td>Tự kiểm tra, ôn giãn cách; tránh đọc lại, tô màu</td><td><span class="label">[Đã xác nhận]</span> Tổng quan lớn về 10 cách học; tổng hợp 317 thí nghiệm về giãn cách</td></tr>
<tr><td>{AEON}; {BUE}</td><td>Lịch tuần, ước lượng thời gian</td><td><span class="label">[Đã xác nhận]</span> Tổng hợp 158 nghiên cứu (tương quan); nghiên cứu kinh điển về đoán thiếu thời gian</td></tr>
<tr><td>{GK}</td><td>Tập trung, điện thoại</td><td><span class="label">[Đã xác nhận]</span> Một thử nghiệm trong lớp, 118 sinh viên</td></tr>
<tr><td>{KYN}</td><td>Làm việc nhóm</td><td><span class="label">[Đã xác nhận]</span> Tổng hợp 59 nghiên cứu, tác dụng mức trung bình lên kết quả học</td></tr>
<tr><td>{AASMA}; {WHOPA}</td><td>Ngủ, vận động</td><td><span class="label">[Đã xác nhận]</span> Đồng thuận chuyên gia và khuyến nghị của WHO</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Phần lớn bằng chứng đến từ trường học ở nước ngoài, có thầy cô tổ chức. Khóa tự học này chưa được thử nghiệm và chưa có chuyên gia duyệt.
  Khóa không thay thế thầy cô, cố vấn học tập, bác sĩ hay nhà tâm lý. Phần tinh thần chuyên sâu (thiền, Khắc kỷ) sẽ có ở trang chị em tamhonkhoe.com.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C3 built')
