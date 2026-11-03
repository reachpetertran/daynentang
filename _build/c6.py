# Khóa C6 "Tự tin – an toàn" – trang khóa, 10 bài, công cụ "Kế hoạch an toàn của tôi".
# Người đọc gồm bạn nữ 13–17 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c6  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/tu-tin-an-toan/'
TOOL = '/cong-cu/ke-hoach-an-toan/'
C1 = '/khoa-hoc/lon-len-an-toan/'
C2 = '/khoa-hoc/hieu-minh/'
C5 = '/khoa-hoc/15-phut-moi-ngay/'
G5 = '/khoa-hoc/vo-chong-dong-long/'
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
SENN = '<a href="https://ojp.gov/ncjrs/virtual-library/abstracts/efficacy-sexual-assault-resistance-program-university-women">Senn et al. 2015, <em>New England Journal of Medicine</em> (tóm tắt trên NCJRS)</a>'
SAR14 = '<a href="https://med.stanford.edu/news/all-news/2014/04/empowerment-program-greatly-decreases-incidence-of-rape-study-finds.html">Sarnquist et al. 2014, <em>Pediatrics</em> (Đại học Stanford đưa tin)</a>'
SAR23 = '<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11111490">Sarnquist et al. 2023, <em>Prevention Science</em></a>'
WHOV = '<a href="https://www.who.int/news-room/fact-sheets/detail/violence-against-women">WHO – Bạo lực đối với phụ nữ (18/6/2026)</a>'
SURV = '<a href="https://www.sggp.org.vn/gan-63-phu-nu-o-nuoc-ta-tung-chiu-bao-luc-50-khong-ke-voi-ai-post620554.html">Nghiên cứu quốc gia về bạo lực đối với phụ nữ 2019 (SGGP đưa tin)</a>'
LUAT = '<a href="https://luatvietnam.vn/hon-nhan-gia-dinh/luat-phong-chong-bao-luc-gia-dinh-so-13-2022-qh15-238397-d1.html">Luật Phòng, chống bạo lực gia đình số 13/2022/QH15</a>'
T117 = '<a href="https://thuonghieucongluan.com.vn/tong-dai-117-hoat-dong-24-7-tiep-nhan-tin-bao-bao-luc-gia-dinh-tren-toan-quoc-a333505.html">Tổng đài 117</a>'
D8 = '<a href="https://daibieunhandan.vn/nhung-hanh-vi-nao-bi-nghiem-cam-trong-linh-vuc-lao-dong-nam-2024-10338504.html">Bộ luật Lao động 2019, Điều 8 (báo Đại biểu Nhân dân tóm tắt, 3/6/2024)</a>'
D17 = '<a href="https://hethongphapluat.com/bo-luat-lao-dong-2019/khoan-1-dieu-17">Bộ luật Lao động 2019, Điều 17 khoản 1</a>'
LUA = '<a href="https://hatinh.gov.vn/vi/bai-viet/nhung-dau-hieu-canh-bao-lua-dao-viec-lam-nguoi-lao-dong-can-biet">Dấu hiệu lừa đảo việc làm (VOV, đăng lại trên Cổng TTĐT Hà Tĩnh, 1/2/2025)</a>'
VOH = '<a href="https://voh.com.vn/phap-luat/cong-an-canh-bao-3-chieu-bat-coc-online-nham-vao-hoc-sinh-sinh-vien-625691.html">Bộ Công an cảnh báo (VOH, 12/10/2025)</a>'
PCMBN = '<a href="https://hethongphapluat.com/law-no-53-2024-qh15-dated-november-28-2024-on-prevention-and-combat-of-human-trafficking/dieu-63">Luật Phòng, chống mua bán người 53/2024/QH15 (trang tra cứu văn bản)</a>'
T111M = '<a href="https://baophapluat.vn/to-giac-bao-tin-ve-hanh-vi-mua-ban-nguoi-hay-goi-den-tong-dai-111.html">Tổng đài 111 nhận tin báo mua bán người (Báo Pháp luật Việt Nam, 2/7/2025)</a>'
TID = '<a href="https://takeitdown.ncmec.org/">Take It Down (NCMEC)</a>'
STOP = '<a href="https://stopncii.org/">StopNCII.org</a>'
BLDS = '<a href="https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam">Bộ luật Dân sự 2015, Điều 468</a>'
DWM = '<a href="https://who.int/publications/i/item/9789240003927">WHO – Doing What Matters in Times of Stress (2020, có bản tiếng Việt)</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'
T111 = '<a href="https://tongdai111.vn/">tongdai111.vn</a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài chưa được nhân viên công tác xã hội, chuyên gia phòng chống bạo lực hay huấn luyện viên tự vệ duyệt. Phần luật chỉ là thông tin chung, không phải tư vấn pháp lý.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Những gì bạn viết là của riêng bạn; hãy cất phiếu ở chỗ chỉ bạn biết. '
           'Người từ 18 tuổi có thể góp ý cho bài ở trang <a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên thật hay nơi ở.</p>')
TALK = ('Nguy hiểm ngay: <strong>113</strong>. Bị thương: <strong>115</strong>. Bạo lực gia đình: <strong>117</strong> (24/7). '
        'Dưới 18 tuổi bị xâm hại, bạo lực, hoặc nghi bị mua bán người ở mọi tuổi: <strong>111</strong> (24/7). Buồn, lo kéo dài: Ngày Mai <strong>096 306 1414</strong>.')
TEEN = 'Nếu bạn 13–17 tuổi: làm phần Làm cùng bố mẹ, thầy cô hoặc một người lớn bạn tin. Bạn không phải tự xử lý một mình.'

L = {
 '1': (1, 'tu-tin-luyen-duoc', 'Bài 1', 'Tự tin là kỹ năng luyện được'),
 '2': (2, 'noi-ro-ranh-gioi', 'Bài 2', 'Nói rõ, giữ ranh giới'),
 '3': (3, 'thoat-ra-keu-cuu', 'Bài 3', 'Tin cảm giác, thoát ra và kêu cứu'),
 '4': (4, 'khi-bi-quay-roi', 'Bài 4', 'Khi bị quấy rối ở nơi công cộng và chỗ làm'),
 '5': (5, 'di-lai-an-toan', 'Bài 5', 'Đi lại an toàn'),
 '6': (6, 'an-toan-tren-mang', 'Bài 6', 'An toàn trên mạng và ảnh riêng tư'),
 '7': (7, 'quan-he-lanh-manh', 'Bài 7', 'Mối quan hệ lành mạnh'),
 '8': (8, 'bay-viec-lam', 'Bài 8', 'Bẫy việc làm và mua bán người'),
 '9': (9, 'tien-cua-minh', 'Bài 9', 'Tiền của mình'),
 '10': (10, 'ke-hoach-an-toan', 'Bài 10', 'Kế hoạch an toàn của tôi'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn viết 3 điểm mạnh có bằng chứng và tập tư thế, giọng nói 5 ngày.'),
 (2, 'Bạn viết 3 câu ranh giới và nói thật 1 câu với một người.'),
 (3, 'Bạn tập 2 cách thoát ra với người tin cậy, đúng luật tập an toàn.'),
 (4, 'Bạn nói được 4 việc làm khi bị quấy rối và 4 cách giúp người khác.'),
 (5, 'Bạn có thói quen Trước – Trong – Sau cho 5 chuyến đi.'),
 (6, 'Bạn kiểm tra 4 cài đặt riêng tư và biết 4 việc làm khi bị dọa tung ảnh.'),
 (7, 'Bạn so sánh một mối quan hệ với 10 dấu hiệu và lưu số 117, 111.'),
 (8, 'Bạn kiểm tra 1 lời mời việc làm theo 6 câu hỏi.'),
 (9, 'Bạn ghi chi 7 ngày và bắt đầu quỹ dự phòng riêng.'),
 (10, 'Bạn có kế hoạch an toàn 1 trang và đã báo trước cho 3 người.'),
]

def lesson(k, desc, goals, prep, read, do, talk, safety, selfq, adult, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Bài {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Nói hoặc viết 5 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (5 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Nói với người tin cậy hoặc tự viết (5 phút)', talk),
        sec(6, 'An toàn', ul(safety + [TEEN, TALK])),
        sec(7, 'Tự đánh giá', selftab(selfq)),
        sec(8, 'Cho người đồng hành: bố mẹ, thầy cô, chị em, bạn bè', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Tự tin – an toàn</a> · Bài {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('S' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Tự tin – an toàn, bài 1: tự tin lớn lên qua từng lần làm được; tìm điểm mạnh có bằng chứng, tập tư thế và giọng nói.',
 ['Viết <strong>3 điểm mạnh</strong>, mỗi điểm kèm <strong>1 việc thật</strong> chứng minh.',
  'Tập <strong>tư thế và giọng nói</strong> 1 phút mỗi ngày, <strong>5 ngày</strong>.',
  'Đổi <strong>1 câu tự chê</strong> thành câu nói công bằng hơn.'],
 [f'In trang 1 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>, hoặc lấy một tờ giấy.', 'Một chỗ có gương, hoặc một người bạn tin.'],
 ['<strong>Tự tin không phải tính bẩm sinh.</strong> Nó lớn lên mỗi lần bạn làm được một việc hơi khó: hỏi đường, từ chối, nói ý kiến.',
  '<strong>Tự tin cần bằng chứng.</strong> "Mình giỏi" dễ lung lay. "Mình đã tự đi xe buýt tới chỗ lạ" thì vững hơn.',
  '<strong>Ba bậc luyện:</strong> tập một mình; tập với người tin cậy; làm ở ngoài đời. Đi từng bậc, không cần nhảy cóc.',
  '<strong>Tư thế:</strong> đứng vững, hai chân rộng bằng vai, nhìn thẳng. Tư thế này giúp người khác thấy bạn nghiêm túc.',
  '<strong>Giọng nói:</strong> nói chậm, rõ, đủ to, câu ngắn. Bỏ những câu xin lỗi thừa như "em xin lỗi, chắc em sai…".',
  '<strong>Câu tự chê</strong> như "mình kém lắm" làm bạn khó nói "không". Thử nói với mình như nói với một người bạn thân.',
  f'<strong>Tự tin khác coi thường người khác.</strong> Bạn có thể vững vàng mà vẫn lịch sự. Muốn tìm hiểu thêm về bản thân, xem khóa <a href="{C2}">Hiểu mình</a>.'],
 '<p><strong>Bài 1: ba điểm mạnh có bằng chứng.</strong></p>'
 + table(['Điểm mạnh', 'Việc thật chứng minh (khi nào, làm gì)'], [['1.', ''], ['2.', ''], ['3.', '']])
 + '<p><strong>Bài 2: tập 1 phút mỗi ngày.</strong> Đứng vững, nhìn thẳng, nói to: <em>"Tôi tên là… Tôi cần…"</em></p>'
 + table(['Ngày'] + DAYS[:5], [['Đã tập ✓'] + [''] * 5])
 + '<p><strong>Bài 3: đổi câu tự chê.</strong></p>'
 + lines(['Câu tôi hay tự chê', 'Câu công bằng hơn']),
 ol(['Đọc 3 điểm mạnh cho một người bạn tin. Hỏi họ: "Bạn thấy mình còn mạnh ở điểm nào?"', 'Thêm điểm họ nói vào danh sách nếu bạn thấy đúng.',
     'Hoặc viết: "Việc hơi khó mình sẽ thử tuần này là…"']),
 ['Bài này không yêu cầu bạn làm việc nguy hiểm để "chứng minh" tự tin.',
  'Nếu buồn, tự ti kéo dài nhiều tuần, khó ăn ngủ: nói với người tin cậy hoặc gọi Ngày Mai.'],
 ['Tôi viết 3 điểm mạnh có bằng chứng', 'Tôi tập tư thế, giọng nói 5 ngày', 'Tôi đổi được 1 câu tự chê'],
 ['Khen việc cụ thể bạn ấy đã làm, không khen chung chung hay khen ngoại hình.', 'Để bạn ấy tự nói ý kiến, không nói thay.',
  'Không so sánh với chị em, bạn bè khác.'],
 [lb('Đánh giá chuyên môn', 'Ba bậc luyện, mẫu điểm mạnh có bằng chứng và cách đổi câu tự chê do daynentang.com soạn.'),
  lb('Đã xác nhận', f'Các chương trình tự vệ có kết quả tốt đều dạy cả niềm tin vào bản thân và ranh giới, không chỉ kỹ thuật ({SAR14}; {SENN}).'),
  lb('Cần kiểm chứng', 'Tác dụng riêng của tư thế "đứng vững" lên cảm giác tự tin: các nghiên cứu cho kết quả không đồng nhất. Bài chỉ dùng nó để người khác hiểu bạn nghiêm túc.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Tự tin – an toàn, bài 2: ba cách đáp lời, câu ranh giới ba phần, nhắc lại khi bị ép, nói "không" mà vẫn lịch sự.',
 ['Phân biệt <strong>3 cách đáp lời</strong>: im lặng, gây gổ, quả quyết.',
  'Viết <strong>3 câu ranh giới</strong> cho 3 tình huống.',
  'Nói thật <strong>1 câu ranh giới</strong> với một người trong tuần.'],
 [f'In trang 2 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Nghĩ tới một việc nhỏ bạn từng muốn từ chối mà chưa nói.'],
 ['<strong>Ranh giới</strong> là điều bạn đồng ý và không đồng ý: về cơ thể, đồ dùng, thời gian, điện thoại, tiền, ảnh của bạn.',
  '<strong>Im lặng, chịu đựng:</strong> người kia có thể không biết bạn không đồng ý. Việc khó chịu dễ lặp lại.',
  '<strong>Gây gổ, xúc phạm:</strong> dễ làm tình hình căng hơn, nhất là với người lạ hay người đang say.',
  '<strong>Quả quyết:</strong> nói rõ, bình tĩnh, tôn trọng. Đây là cách các chương trình tự vệ dạy nhiều nhất.',
  '<strong>Câu ranh giới ba phần:</strong> "Khi bạn… (việc gì), mình thấy… (cảm xúc). Mình muốn… (đề nghị)."',
  '<strong>Khi bị ép:</strong> không cần giải thích thêm. Nhắc lại câu ngắn: "Mình đã nói không." Nói vài lần, giọng đều.',
  '<strong>Nói "không" mà vẫn giữ quan hệ:</strong> có thể thêm việc bạn đồng ý. "Mình không cho mượn xe, nhưng mình chở bạn ra bến được."'],
 '<p><strong>Bài 1: ba câu ranh giới.</strong> Các tình huống dưới đây là giả định.</p>'
 + table(['Tình huống (giả định)', 'Câu ranh giới của tôi'],
         [['Một người quen cứ chạm vai, khoác tay bạn dù bạn né.', ''],
          ['Bạn bè đòi xem tin nhắn trong điện thoại của bạn.', ''],
          ['Đồng nghiệp nhờ bạn làm hộ việc của họ nhiều lần.', '']])
 + '<p><strong>Bài 2: câu nhắc lại khi bị ép.</strong> <em>"Mình đã nói không."</em> Tập nói 3 lần, giọng đều, không cười.</p>'
 + lines(['Câu nhắc lại của tôi', 'Người tôi sẽ nói một câu ranh giới tuần này']),
 ol(['Nhờ người tin cậy đóng vai người ép. Bạn tập câu ranh giới và câu nhắc lại.', 'Đổi vai: bạn làm người ép, xem họ trả lời ra sao.',
     'Hoặc viết: "Lần mình nói được không, mình thấy…"']),
 ['Với người đang giận dữ, say rượu hay có vũ khí: an toàn trước, có thể tạm đồng ý để rời đi, rồi báo người khác.',
  'Nói rõ không có nghĩa phải ở lại tranh cãi. Nói xong, bạn được rời đi.'],
 ['Tôi phân biệt được 3 cách đáp lời', 'Tôi viết 3 câu ranh giới', 'Tôi nói thật 1 câu ranh giới'],
 ['Khi bạn ấy nói "không" với bạn, hãy tôn trọng. Đó là cách bạn ấy tập.', 'Đóng vai người ép ở mức nhẹ, không nói lời xúc phạm thật.',
  'Bố mẹ: đừng ép con ôm, hôn người lớn khi con không muốn.'],
 [lb('Đã xác nhận', f'Trong chương trình ở Nairobi, phần lớn lần các bạn nữ chặn được tấn công là nhờ kỹ năng lời nói, riêng hoặc kèm thân thể ({SAR14}).'),
  lb('Đánh giá chuyên môn', 'Ba cách đáp lời, câu ranh giới ba phần và câu nhắc lại là kỹ năng giao tiếp phổ biến, do daynentang.com viết lại.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Tự tin – an toàn, bài 3: tin cảm giác bất an, rời đi sớm, kêu cứu đúng cách, ba động tác thoát ra và luật tập an toàn.',
 ['Nói được <strong>3 dấu hiệu</strong> cơ thể báo "có gì đó sai".',
  'Tập <strong>2 trong 3 cách thoát ra</strong> với người tin cậy, đúng luật tập.',
  'Có <strong>1 câu kêu cứu</strong> chỉ đích danh người giúp.'],
 [f'In trang 3 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Một người tin cậy đồng ý tập cùng, một chỗ rộng, nền không trơn.'],
 ['<strong>Tin cảm giác của mình.</strong> Tim đập nhanh, muốn rời đi, thấy bị dồn ép: đó là tín hiệu. Bạn không cần bằng chứng mới được rời đi.',
  '<strong>Kẻ xấu thường là người quen,</strong> không chỉ người lạ. Họ hay thử ranh giới nhỏ trước: rủ đi riêng, ép uống, chạm "vô tình".',
  '<strong>Rời đi sớm</strong> là cách an toàn nhất. Viện cớ cũng được: "Mình phải về, mẹ đang đợi."',
  '<strong>Kêu cứu chỉ đích danh:</strong> "Chị áo xanh ơi, gọi giúp em 113!" Người được gọi đích danh dễ ra tay hơn đám đông.',
  '<strong>Cách 1, giữ khoảng cách và nói to:</strong> hai tay mở ra trước ngực, lùi lại, hét "DỪNG LẠI! LÙI RA!" để người xung quanh nghe.',
  '<strong>Cách 2, thoát khi bị nắm cổ tay:</strong> chỗ yếu là khe giữa ngón cái và các ngón kia. Xoay cổ tay, rút mạnh qua khe đó về phía mình, rồi chạy.',
  '<strong>Cách 3, khi bị kéo đi:</strong> hạ thấp người, ngồi xuống, la to "Tôi không quen người này!". Mục tiêu là thoát ra, không phải đánh thắng.'],
 '<p><strong>Bài 1: dấu hiệu của tôi.</strong> Khi thấy không an toàn, cơ thể tôi thường:</p>'
 + lines(['Dấu hiệu 1', 'Dấu hiệu 2', 'Dấu hiệu 3', 'Câu viện cớ để rời đi', 'Câu kêu cứu chỉ đích danh'])
 + '<p><strong>Bài 2: tập 2 cách thoát ra.</strong> Đọc luật tập ở mục An toàn trước. Tập chậm, mỗi cách 5 lần.</p>'
 + table(['Cách', 'Đã tập chậm ✓', 'Nói to được ✓', 'Ghi chú'],
         [['1. Giữ khoảng cách, nói to', '', '', ''], ['2. Thoát nắm cổ tay', '', '', ''], ['3. Hạ thấp người khi bị kéo', '', '', '']]),
 ol(['Cùng người tin cậy nhắc lại luật tập, thống nhất từ "Dừng" chung.', 'Sau khi tập, mỗi người nói một điều làm tốt, một điều cần tập thêm.',
     'Hoặc viết: "Nơi mình hay thấy bất an là… Mình sẽ…"']),
 ['<strong>Luật tập:</strong> chỉ tập với người đồng ý; tập chậm, lực nhẹ; ai nói "Dừng" thì dừng ngay; không tập đùa với người không biết.',
  'Không tập khi đang đau tay, cổ tay, vai hay đang mang thai. Không xoay khớp của bạn tập quá tầm.',
  'Người tấn công có dao, vũ khí, đòi tiền hay đồ: đưa đồ, ưu tiên mạng sống, rồi báo 113.',
  'Ba cách trên không thay thế một lớp tự vệ có người hướng dẫn. Nếu có điều kiện, hãy học trực tiếp.'],
 ['Tôi nói được 3 dấu hiệu "có gì đó sai"', 'Tôi tập 2 cách thoát ra đúng luật', 'Tôi có câu kêu cứu chỉ đích danh'],
 ['Tập cùng bạn ấy theo đúng luật. Bạn ấy dẫn, bạn theo.', 'Không chê "làm quá" khi bạn ấy rời đi vì thấy bất an.',
  'Nhắc: nếu có lần không thoát được, đó không phải lỗi của bạn ấy.'],
 [lb('Đã xác nhận', f'Chương trình 4 buổi × 3 giờ cho 893 nữ sinh viên năm nhất ở Canada, có nhận diện nguy cơ và tự vệ lời nói, thân thể: sau 1 năm, bị hiếp dâm 5,2% so với 9,8% ở nhóm chỉ nhận tờ rơi ({SENN}).'),
  lb('Đã xác nhận', f'Ở Nairobi, 12 giờ học gồm ranh giới, lời nói quả quyết, xoa dịu và kỹ năng thân thể để thoát ra; tỷ lệ bị hiếp dâm trong nhóm học giảm sau khoảng 10 tháng ({SAR14}).'),
  lb('Đã xác nhận', f'Một thử nghiệm lớn hơn sau đó với 3.263 nữ sinh 10–14 tuổi ở Nairobi không thấy giảm hiếp dâm sau 24 tháng ({SAR23}).'),
  lb('Suy luận', 'Các chương trình trên dạy trực tiếp, nhiều giờ, có người hướng dẫn. Bài tự học này ngắn hơn nhiều, nên không thể hứa kết quả tương tự.'),
  lb('Đánh giá chuyên môn', 'Ba động tác thoát ra là kỹ thuật cơ bản phổ biến trong các lớp tự vệ, do daynentang.com mô tả lại. Chưa có huấn luyện viên duyệt.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Tự tin – an toàn, bài 4: nhận ra quấy rối, bốn việc làm khi bị quấy rối, ghi lại để báo, bốn cách giúp khi thấy người khác bị quấy rối.',
 ['Nói được <strong>4 việc</strong> có thể làm khi bị quấy rối.',
  'Biết <strong>ghi lại</strong> một việc theo 5 ô: ngày, giờ, nơi, ai, việc gì.',
  'Nói được <strong>4 cách giúp</strong> khi thấy người khác bị quấy rối.'],
 [f'In trang 4 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Tìm hiểu nơi bạn học, làm việc có ai phụ trách nhận phản ánh.'],
 ['<strong>Quấy rối</strong> là lời nói, cử chỉ, tin nhắn, động chạm mang tính tình dục mà bạn không muốn: trêu ghẹo về cơ thể, huýt sáo theo, chụp lén, sờ soạng.',
  '<strong>Không phải lỗi của bạn.</strong> Quần áo, giờ giấc, nụ cười của bạn không phải lý do. Người quấy rối mới là người làm sai.',
  '<strong>Bốn việc có thể làm:</strong> nói rõ "Dừng lại"; rời đi tới chỗ có người; ghi lại; báo người tin cậy hoặc nơi phụ trách. Chọn việc an toàn nhất lúc đó.',
  '<strong>Ghi lại sớm:</strong> ngày, giờ, nơi, ai, việc gì, ai chứng kiến. Chụp lại tin nhắn. Ghi chép giúp khi báo cáo.',
  '<strong>Ở chỗ làm:</strong> quấy rối tình dục tại nơi làm việc bị pháp luật nghiêm cấm. Báo quản lý, công đoàn hoặc bộ phận nhân sự.',
  '<strong>Khi thấy người khác bị quấy rối:</strong> đánh lạc hướng ("Chị ơi, mấy giờ rồi?"); nhờ bảo vệ, tài xế; ghi lại nếu an toàn; hỏi han sau đó.',
  '<strong>Người chứng kiến không cần đối đầu.</strong> Một câu hỏi bình thường cũng có thể cắt ngang tình huống.'],
 '<p><strong>Bài 1: mẫu ghi lại.</strong> Giữ mẫu này trong điện thoại hoặc sổ.</p>'
 + table(['Ngày', 'Giờ', 'Nơi', 'Ai (tả ngoại hình nếu không biết tên)', 'Việc gì xảy ra', 'Ai chứng kiến'], [['', '', '', '', '', '']])
 + '<p><strong>Bài 2: tôi sẽ báo ai?</strong></p>'
 + lines(['Ở trường hoặc chỗ học', 'Ở chỗ làm', 'Trên xe buýt, nơi công cộng', 'Câu đánh lạc hướng của tôi khi thấy người khác bị quấy rối']),
 ol(['Hỏi người tin cậy: "Nếu em bị quấy rối ở…, em nên báo ai?"', 'Thống nhất họ sẽ làm gì khi bạn báo: nghe trước, không trách.',
     'Hoặc viết: "Một lần mình thấy người khác bị trêu ghẹo, mình đã… Lần sau mình sẽ…"']),
 ['Người quấy rối đi theo bạn: vào cửa hàng, quán đông người, gọi người thân, gọi 113.',
  'Bị chụp lén, quay lén: báo bảo vệ hoặc công an, giữ thông tin thời gian, địa điểm.'],
 ['Tôi nói được 4 việc khi bị quấy rối', 'Tôi có mẫu ghi lại 5 ô', 'Tôi nói được 4 cách giúp người khác'],
 ['Khi bạn ấy kể, hãy nghe hết, tin bạn ấy, không hỏi "mặc gì", "đi đâu khuya thế".', 'Cùng bạn ấy quyết định có báo hay không, báo ai.',
  'Ở chỗ làm: có cách để người lao động báo quấy rối mà không sợ bị trả đũa.'],
 [lb('Đã xác nhận', f'Quấy rối tình dục tại nơi làm việc là hành vi bị nghiêm cấm ({D8}).'),
  lb('Cần kiểm chứng', 'Mức xử phạt hành chính cho hành vi quấy rối nơi công cộng theo nghị định hiện hành: chúng tôi chưa đọc văn bản gốc nên không ghi con số.'),
  lb('Đánh giá chuyên môn', 'Bốn việc khi bị quấy rối, mẫu ghi lại và bốn cách giúp của người chứng kiến là cách làm phổ biến, do daynentang.com viết lại.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Tự tin – an toàn, bài 5: thói quen Trước – Trong – Sau mỗi chuyến đi, kiểm tra xe công nghệ, đi đêm, mật mã gọi đón.',
 ['Dùng thói quen <strong>Trước – Trong – Sau</strong> cho <strong>5 chuyến đi</strong>.',
  'Kiểm <strong>3 điều</strong> trước khi lên xe đặt qua ứng dụng.',
  'Có <strong>mật mã gọi đón</strong> với 1 người thân.'],
 [f'In trang 5 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Điện thoại đã sạc, lưu sẵn số người thân và 113.'],
 ['<strong>Trước khi đi:</strong> báo một người nơi đến, đi với ai, giờ về. Sạc pin, mang ít tiền mặt dự phòng.',
  '<strong>Trong khi đi:</strong> ngồi ghế sau, giữ túi, điện thoại trong tay. Hạn chế đeo tai nghe hai bên khi đi bộ đường vắng.',
  '<strong>Sau khi đến:</strong> nhắn "đã tới". Người thân không nhận được tin đúng giờ thì gọi ngay.',
  '<strong>Xe công nghệ, kiểm 3 điều:</strong> biển số trùng ứng dụng; tên, ảnh tài xế trùng; để tài xế nói tên bạn trước. Sai một điều: không lên xe.',
  '<strong>Chia sẻ hành trình</strong> trong ứng dụng cho người thân nếu ứng dụng có tính năng này.',
  '<strong>Mật mã gọi đón:</strong> một câu bình thường, ví dụ "Mẹ ơi, con quên mang áo mưa". Nghe câu này, người thân gọi lại và tới đón, không hỏi nhiều.',
  '<strong>Đi chơi, tiệc tùng:</strong> đi về cùng bạn, tự giữ ly nước của mình, đừng để ai một mình về với người vừa quen.'],
 '<p><strong>Bài 1: năm chuyến đi.</strong> Đánh dấu ✓ từng phần.</p>'
 + table(['Chuyến đi', 'Trước: đã báo', 'Trong: đã kiểm xe', 'Sau: đã nhắn "tới"'], [[f'{n}.', '', '', ''] for n in range(1, 6)])
 + '<p><strong>Bài 2: mật mã gọi đón.</strong></p>'
 + lines(['Mật mã của tôi', 'Người tôi thống nhất mật mã', 'Họ sẽ làm gì khi nghe mật mã']),
 ol(['Thống nhất mật mã với người thân. Tập một lần qua điện thoại.', 'Hỏi người thân: "Nếu em không nhắn đúng giờ, anh/chị sẽ làm gì?"',
     'Hoặc viết: "Đoạn đường mình thấy lo nhất là… Mình sẽ đổi…"']),
 ['Tài xế đổi đường lạ, khóa cửa, có hành vi khó chịu: yêu cầu dừng ở chỗ đông người, gọi người thân, gọi 113 nếu bị đe dọa.',
  'Bị đi theo: vào cửa hàng, nhà hàng, đồn công an gần nhất; không đi về nhà ngay.'],
 ['Tôi dùng Trước – Trong – Sau cho 5 chuyến', 'Tôi kiểm 3 điều trước khi lên xe', 'Tôi có mật mã gọi đón'],
 ['Khi nghe mật mã: tới đón, không mắng, không hỏi nhiều lúc đó.', 'Giữ máy mở vào giờ bạn ấy hay đi về.',
  f'Bố mẹ có con 10–14 tuổi xem thêm khóa <a href="{C1}">Lớn lên an toàn</a>.'],
 [lb('Đánh giá chuyên môn', 'Thói quen Trước – Trong – Sau, ba điều kiểm xe và mật mã gọi đón là lời khuyên an toàn chung, do daynentang.com soạn.'),
  lb('Cần kiểm chứng', 'Chúng tôi chưa tìm được nghiên cứu đo hiệu quả riêng của các thói quen đi lại này. Bài không hứa con số.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Tự tin – an toàn, bài 6: cài đặt riêng tư, lừa tình qua mạng, bị dọa tung ảnh riêng tư: không trả tiền, giữ bằng chứng, báo, gỡ ảnh.',
 ['Kiểm tra <strong>4 cài đặt riêng tư</strong> trên tài khoản của bạn.',
  'Nêu <strong>4 dấu hiệu</strong> lừa tình, lừa tiền qua mạng.',
  'Nói được <strong>4 việc làm</strong> khi bị dọa tung ảnh.'],
 [f'In trang 6 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Điện thoại và tài khoản mạng xã hội bạn dùng nhiều nhất.'],
 ['<strong>Bốn cài đặt nên kiểm:</strong> ai xem được bài đăng; ai nhắn tin được; tắt chia sẻ vị trí; bật xác thực hai lớp.',
  '<strong>Dấu hiệu lừa qua mạng:</strong> người lạ làm thân rất nhanh, khen nhiều; xin ảnh riêng; rủ gặp riêng; vay tiền hay nhờ chuyển tiền.',
  '<strong>Bộ Công an cảnh báo</strong> các chiêu làm thân lâu ngày, giả danh đe dọa, dụ bằng tiền nhắm vào học sinh, sinh viên.',
  '<strong>Ảnh riêng tư</strong> đã gửi đi thì bạn không còn kiểm soát được. Nghĩ kỹ trước khi gửi, kể cả cho người yêu.',
  '<strong>Bị dọa tung ảnh:</strong> không trả tiền, không gửi thêm ảnh. Chụp lại tin nhắn, tài khoản kẻ dọa. Rồi chặn và báo nền tảng.',
  '<strong>Báo người tin cậy và công an.</strong> Dưới 18 tuổi gọi 111. Bạn không có lỗi; người đe dọa mới là người vi phạm.',
  '<strong>Gỡ ảnh:</strong> ảnh chụp khi dưới 18 tuổi dùng Take It Down; từ 18 tuổi dùng StopNCII. Ảnh ở lại máy bạn, chỉ gửi "dấu vân tay số".'],
 '<p><strong>Bài 1: kiểm tra cài đặt.</strong></p>'
 + table(['Cài đặt', 'Trước', 'Sau khi chỉnh'],
         [['Ai xem được bài đăng', '', ''], ['Ai nhắn tin được cho tôi', '', ''], ['Chia sẻ vị trí', '', ''], ['Xác thực hai lớp', '', '']])
 + '<p><strong>Bài 2: nếu bị dọa tung ảnh, tôi sẽ:</strong></p>'
 + lines(['1. Không…', '2. Chụp lại…', '3. Chặn và báo…', '4. Nói với…']),
 ol(['Cùng người tin cậy kiểm tra cài đặt riêng tư của cả hai người.', 'Hỏi họ: "Nếu em bị dọa, em có thể nói với anh/chị mà không bị mắng không?"',
     'Hoặc viết: "Một tài khoản lạ mình nên chặn là…"']),
 ['Không đọc mã OTP, mật khẩu cho bất kỳ ai, kể cả người tự xưng là công an, ngân hàng.',
  'Không đi gặp một mình người chỉ quen qua mạng. Nếu gặp: chỗ đông người, báo trước người thân.',
  'Bị dọa hại bản thân hay người thân: gọi 113 ngay.'],
 ['Tôi kiểm tra 4 cài đặt riêng tư', 'Tôi nêu được 4 dấu hiệu lừa qua mạng', 'Tôi biết 4 việc làm khi bị dọa tung ảnh'],
 ['Nói trước với bạn ấy: "Dù chuyện gì xảy ra trên mạng, em cứ kể, chị không mắng."',
  'Khi bạn ấy kể, giúp giữ bằng chứng và báo; không đòi xem hết ảnh riêng.', 'Không tự liên lạc với kẻ dọa để thương lượng.'],
 [lb('Đã xác nhận', f'Take It Down là dịch vụ miễn phí cho ảnh, video riêng tư chụp khi dưới 18 tuổi; ảnh ở lại máy người dùng, chỉ gửi mã băm; ảnh chụp từ 18 tuổi được chuyển sang {STOP} ({TID}).'),
  lb('Đã xác nhận', f'Bộ Công an cảnh báo các chiêu nhắm vào học sinh, sinh viên: làm thân lâu ngày, giả danh đe dọa, dụ bằng tiền ({VOH}).'),
  lb('Cần kiểm chứng', 'Điều khoản pháp luật Việt Nam xử lý hành vi đe dọa, phát tán ảnh riêng tư: chúng tôi chưa đọc văn bản gốc nên không trích điều luật.'),
  lb('Đánh giá chuyên môn', 'Bốn cài đặt, bốn dấu hiệu và bốn việc làm khi bị dọa do daynentang.com tổng hợp.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Tự tin – an toàn, bài 7: dấu hiệu mối quan hệ lành mạnh và kiểm soát, bạo lực không phải lỗi của bạn, ai có thể giúp.',
 ['So sánh một mối quan hệ với <strong>10 dấu hiệu</strong>.',
  'Lưu số <strong>117, 111, 113</strong> trong điện thoại.',
  'Viết tên <strong>1 người</strong> bạn sẽ kể nếu thấy không ổn.'],
 [f'In trang 7 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>. Cất phiếu ở chỗ chỉ bạn biết.', 'Nghĩ tới một mối quan hệ: người yêu, bạn bè, người trong nhà.'],
 ['<strong>Lành mạnh:</strong> bạn được nói "không"; có bạn bè riêng; giữ điện thoại, tiền, giấy tờ của mình; cãi nhau mà không sợ.',
  '<strong>Kiểm soát:</strong> ghen tuông, theo dõi; cấm gặp bạn bè, gia đình; đòi mật khẩu; giữ tiền, giấy tờ; dọa, đánh, ép quan hệ.',
  '<strong>Kiểm soát thường tăng dần.</strong> Lúc đầu có thể giống "quan tâm": hỏi đang ở đâu, đòi đón đưa, không muốn bạn đi chơi với ai.',
  '<strong>Bạo lực khá phổ biến.</strong> Theo WHO, khoảng 1 trong 3 phụ nữ trên thế giới từng bị bạo lực thể chất hoặc tình dục.',
  '<strong>Ở Việt Nam,</strong> nghiên cứu quốc gia 2019 cho thấy gần 63% phụ nữ từng chịu ít nhất một hình thức bạo lực của chồng, và khoảng một nửa chưa từng kể với ai.',
  '<strong>Bạo lực không bao giờ là lỗi của người bị hại.</strong> Không có lời nói, món ăn hay bộ quần áo nào là lý do để bị đánh.',
  f'<strong>Nhờ giúp:</strong> 117 nhận tin bạo lực gia đình (24/7); 111 cho người dưới 18 tuổi; 113 khi nguy hiểm ngay. Vợ chồng xem thêm khóa <a href="{G5}">Vợ chồng đồng lòng</a>.'],
 '<p><strong>Bài 1: mười dấu hiệu.</strong> Nghĩ về một mối quan hệ. Đánh dấu ✓ nếu đúng.</p>'
 + table(['Dấu hiệu', '✓'],
         [['Người đó kiểm tra điện thoại, tin nhắn của tôi', ''], ['Tôi phải báo đang ở đâu mọi lúc', ''], ['Người đó cấm tôi gặp bạn bè, gia đình', ''],
          ['Người đó giữ tiền, giấy tờ của tôi', ''], ['Người đó chê bai, làm nhục tôi trước người khác', ''], ['Tôi sợ khi người đó giận', ''],
          ['Người đó đe dọa bỏ đi, tự hại nếu tôi không nghe', ''], ['Người đó ép tôi làm việc tôi không muốn', ''],
          ['Người đó đã đẩy, tát, đánh tôi', ''], ['Tôi thấy mình phải giấu chuyện này', '']])
 + '<p class="small">Có nhiều dấu ✓ không phải để bạn tự trách. Đó là lý do để nói với một người tin cậy.</p>'
 + lines(['Người tôi sẽ kể', 'Số đã lưu: 117 · 111 · 113 ✓']),
 ol(['Nếu thấy an toàn, kể với người tin cậy một dấu hiệu bạn thấy.', 'Nếu chưa sẵn sàng kể, chỉ cần lưu số và cất phiếu ở chỗ kín.',
     'Hoặc viết: "Mình xứng đáng được đối xử…"']),
 ['Nếu người kiểm soát hay xem điện thoại của bạn: xóa lịch sử duyệt web, không để phiếu này ở chỗ họ thấy.',
  'Đang nguy hiểm ngay: rời đi tới nhà hàng xóm, chỗ đông người, gọi 113.',
  'Bị thương, bị ép quan hệ: đi khám sớm, kể cả khi chưa muốn báo công an.'],
 ['Tôi so sánh được với 10 dấu hiệu', 'Tôi lưu số 117, 111, 113', 'Tôi có 1 người sẽ kể'],
 ['Khi bạn ấy kể: tin, nghe, không trách, không ép bỏ đi ngay. Hỏi "Mình giúp được gì?".',
  'Giúp bạn ấy lập kế hoạch an toàn (bài 10). Rời đi là quyết định của bạn ấy, có thể cần nhiều thời gian.',
  'Không tự đối đầu người gây bạo lực; việc đó có thể làm bạn ấy nguy hiểm hơn.'],
 [lb('Đã xác nhận', f'Khoảng 1 trong 3 phụ nữ (31,6%) trên thế giới từng bị bạo lực thể chất hoặc tình dục từ bạn tình, hoặc bạo lực tình dục từ người khác; hơn 1 trong 5 bạn gái 15–19 tuổi đã có bạn đời từng bị bạn đời bạo lực ({WHOV}).'),
  lb('Đã xác nhận', f'Nghiên cứu quốc gia 2019: 62,9% phụ nữ từng chịu ít nhất một hình thức bạo lực của chồng; khoảng 50% không kể với ai ({SURV}).'),
  lb('Đã xác nhận', f'{LUAT}, hiệu lực 01/07/2023. {T117} nhận tin bạo lực gia đình 24/7 từ 9/2026.'),
  lb('Cần kiểm chứng', 'Tổng đài 117 có miễn phí cước gọi hay không: chúng tôi chưa xác nhận.'),
  lb('Đánh giá chuyên môn', 'Bảng mười dấu hiệu do daynentang.com soạn để tự suy nghĩ, không phải công cụ đánh giá nguy cơ.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Tự tin – an toàn, bài 8: dấu hiệu lừa việc làm và mua bán người, sáu câu hỏi trước khi nhận việc xa, giữ giấy tờ gốc, gọi 111.',
 ['Nêu <strong>4 dấu hiệu</strong> bẫy việc làm, mua bán người.',
  'Kiểm tra <strong>1 lời mời</strong> việc làm theo <strong>6 câu hỏi</strong>.',
  'Biết <strong>111</strong> nhận tin báo mua bán người ở mọi tuổi.'],
 [f'In trang 8 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Một tin tuyển dụng, lời mời đi làm xa hay đi nước ngoài bạn từng thấy.'],
 ['<strong>Bẫy việc làm</strong> thường nhắm vào người cần tiền, người trẻ, người sắp đi làm xa. Kẻ dụ có thể là người quen, họ hàng, "người yêu" qua mạng.',
  '<strong>Dấu hiệu 1:</strong> việc nhẹ, lương cao bất thường, không cần kinh nghiệm.',
  '<strong>Dấu hiệu 2:</strong> phải đi xa, ra nước ngoài gấp; được "lo hết" vé, giấy tờ; đi bằng đường không chính thức.',
  '<strong>Dấu hiệu 3:</strong> đòi giữ căn cước, hộ chiếu; đòi đặt cọc, "phí hồ sơ". Chỗ làm không được giữ bản chính giấy tờ của bạn.',
  '<strong>Dấu hiệu 4:</strong> bảo bạn giấu gia đình, cắt liên lạc, đổi số điện thoại. Đây là dấu hiệu rất nguy hiểm.',
  '<strong>Sáu câu hỏi trước khi nhận:</strong> việc gì? ở đâu, địa chỉ thật? giờ làm? lương, trả khi nào? hợp đồng? ai tuyển, có giấy phép không?',
  '<strong>Trước khi đi xa:</strong> để lại bản sao giấy tờ, địa chỉ nơi làm, số người tuyển cho người thân. Hẹn giờ gọi về. Giấy tờ gốc luôn ở trong tay bạn.'],
 '<p><strong>Bài 1: kiểm tra một lời mời.</strong> Lời mời: ……………</p>'
 + table(['Câu hỏi', 'Câu trả lời', 'Rõ ràng? ✓/✗'],
         [['1. Việc gì?', '', ''], ['2. Ở đâu, địa chỉ thật?', '', ''], ['3. Giờ làm?', '', ''], ['4. Lương, trả khi nào?', '', ''],
          ['5. Hợp đồng?', '', ''], ['6. Ai tuyển, có giấy phép?', '', '']])
 + '<p><strong>Bài 2: dấu hiệu tôi thấy.</strong></p>'
 + lines(['Dấu hiệu trong lời mời này', 'Người tôi sẽ hỏi trước khi quyết định']),
 ol(['Đưa lời mời cho gia đình hoặc thầy cô cùng xem. Hỏi họ thấy gì lạ.', 'Lưu số 111 và 113. Nói với người thân: "Nếu em mất liên lạc quá… giờ, hãy gọi 111."',
     'Hoặc viết: "Nếu có người hứa việc lương cao, mình sẽ hỏi…"']),
 ['Đang ở nơi lạ, bị giữ giấy tờ, không được về, không được liên lạc: tìm cách gọi 113, 111, hoặc nhờ người lạ gọi giúp.',
  'Biết người khác đang bị dụ, bị giữ: báo 111 hoặc công an nơi gần nhất.'],
 ['Tôi nêu được 4 dấu hiệu bẫy việc làm', 'Tôi kiểm tra 1 lời mời theo 6 câu hỏi', 'Tôi biết 111 nhận tin mua bán người'],
 ['Hỏi con, em về các lời mời việc làm, nhất là việc ở xa hay ở nước ngoài.', 'Giữ bản sao giấy tờ và địa chỉ nơi làm của người thân đi xa.',
  'Hẹn giờ gọi cố định; mất liên lạc bất thường thì báo ngay.'],
 [lb('Đã xác nhận', f'{PCMBN}, thông qua 28/11/2024, hiệu lực 01/07/2025 theo trang tra cứu.'),
  lb('Đã xác nhận', f'Tổng đài 111 là tổng đài quốc gia nhận tố giác, tin báo về mua bán người, hoạt động 24 giờ, theo Nghị định 162/2025/NĐ-CP ({T111M}).'),
  lb('Đã xác nhận', f'Chỗ làm không được giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động ({D17}).'),
  lb('Đã xác nhận', f'Các dấu hiệu lừa đảo việc làm hay gặp: việc nhẹ lương cao, đòi đặt cọc, phí hồ sơ ({LUA}).'),
  lb('Cần kiểm chứng', 'Cuộc gọi 111 về mua bán người có miễn phí cho người từ 18 tuổi không: bài báo chưa nói rõ. Nguyên văn điều khoản hiệu lực của Luật 53/2024/QH15 chưa đọc.'),
  lb('Đánh giá chuyên môn', 'Sáu câu hỏi trước khi nhận việc và việc chuẩn bị trước khi đi xa do daynentang.com soạn.')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Tự tin – an toàn, bài 9: biết mình có bao nhiêu, quỹ dự phòng riêng, giữ giấy tờ và mật khẩu, không đứng tên vay hộ.',
 ['Ghi <strong>mọi khoản chi 7 ngày</strong>.',
  'Bắt đầu <strong>quỹ dự phòng riêng</strong>, mức nào cũng được.',
  'Kiểm tra <strong>4 điều</strong> về giấy tờ, tài khoản của mình.'],
 [f'In trang 9 của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>, hoặc dùng <a href="{BTC}">Bảng thu chi</a>.', 'Một phong bì, hộp nhỏ hoặc tài khoản riêng để đựng quỹ.'],
 ['<strong>Có tiền riêng giúp bạn có lựa chọn:</strong> rời một chỗ không an toàn, đi khám, gọi xe về lúc khuya.',
  '<strong>Biết mình có bao nhiêu:</strong> thu nhập, khoản chi, nợ (nếu có). Ghi chi 7 ngày là bước đầu.',
  '<strong>Quỹ dự phòng riêng:</strong> mỗi lần có tiền, để riêng một khoản cố định. Mục tiêu đầu: đủ tiền xe và vài ngày ăn ở.',
  '<strong>Giữ giấy tờ của mình:</strong> căn cước, giấy khai sinh, bằng cấp, thẻ ngân hàng. Biết chúng ở đâu.',
  '<strong>Giữ mật khẩu, mã OTP</strong> của mình. Không đưa cho người yêu, bạn bè hay người lạ.',
  '<strong>Không đứng tên vay hộ,</strong> không cho mượn tài khoản ngân hàng. Khoản nợ hay việc phạm pháp có thể rơi vào bạn.',
  f'<strong>Vay:</strong> lãi suất thỏa thuận không được vượt 20% một năm. Ứng dụng cho vay dễ thường đòi cao hơn nhiều. Bài không tư vấn vay hay đầu tư; cả nhà xem khóa <a href="{G6}">Tiền nhà mình</a>.'],
 '<p><strong>Bài 1: chi 7 ngày.</strong></p>'
 + table(['Ngày', 'Khoản chi', 'Số tiền', 'Cần / Muốn'], [[d, '', '', ''] for d in DAYS])
 + '<p><strong>Bài 2: bốn điều của tôi.</strong></p>'
 + table(['Điều', '✓'],
         [['Tôi biết giấy tờ gốc của mình ở đâu', ''], ['Chỉ tôi biết mật khẩu, mã OTP của mình', ''],
          ['Tôi không đứng tên vay hộ, không cho mượn tài khoản', ''], ['Tôi có quỹ dự phòng riêng, mức: ……', '']]),
 ol(['Hỏi người tin cậy cách họ để dành tiền dự phòng.', 'Nếu bạn dưới 18 tuổi: cùng bố mẹ chọn chỗ cất quỹ nhỏ của bạn.',
     'Hoặc viết: "Nếu cần rời đi ngay, mình cần khoảng … tiền cho…"']),
 ['Bị người khác giữ tiền, giấy tờ, ép đưa lương: đây là dấu hiệu kiểm soát (bài 7). Kể với người tin cậy.',
  'Bị đòi nợ đe dọa: báo gia đình và công an (113).'],
 ['Tôi ghi chi 7 ngày', 'Tôi có quỹ dự phòng riêng', 'Tôi kiểm tra 4 điều về giấy tờ, tài khoản'],
 ['Để bạn ấy tự giữ và tự quyết khoản tiền riêng, kể cả khi số nhỏ.', 'Không hỏi mật khẩu của bạn ấy.',
  'Chỉ cách đọc hợp đồng vay, nhưng không ép vay hay đứng tên hộ.'],
 [lb('Đã xác nhận', f'Lãi suất vay theo thỏa thuận không vượt quá 20%/năm của khoản tiền vay, trừ luật khác quy định ({BLDS}).'),
  lb('Đánh giá chuyên môn', 'Quỹ dự phòng riêng và bốn điều về giấy tờ, tài khoản là lời khuyên an toàn chung do daynentang.com soạn. Bài chỉ dạy thu chi cơ bản.')])

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Tự tin – an toàn, bài 10: kế hoạch an toàn một trang, ba người có thể nhờ, khi buồn lo kéo dài, tự đánh giá cuối khóa.',
 ['Làm <strong>kế hoạch an toàn 1 trang</strong> gồm 5 phần.',
  'Chọn <strong>3 người</strong> có thể nhờ và <strong>báo trước</strong> cho họ.',
  'Làm <strong>tự đánh giá</strong> cuối khóa.'],
 [f'In trang 10 và phần tự đánh giá của <a href="{TOOL}">Kế hoạch an toàn của tôi</a>.', 'Các phiếu đã làm ở bài 1–9.'],
 ['<strong>Kế hoạch an toàn</strong> giúp bạn không phải nghĩ lúc hoảng sợ. Mọi thứ đã viết sẵn.',
  '<strong>Năm phần:</strong> ba người có thể nhờ; mật mã gọi đón; số khẩn cấp đã lưu; giấy tờ, tiền dự phòng ở đâu; nơi an toàn gần nhà, chỗ làm.',
  '<strong>Ba người cho ba việc:</strong> người gọi được lúc nửa đêm; người cho ở nhờ vài ngày; người hiểu luật, thủ tục.',
  '<strong>Báo trước cho họ.</strong> "Em ghi anh/chị là người em có thể gọi khi cần. Anh/chị đồng ý không?"',
  '<strong>Cập nhật</strong> khi đổi chỗ ở, chỗ làm, số điện thoại hay mối quan hệ.',
  '<strong>Khi buồn, lo kéo dài:</strong> sau chuyện khó, có thể khó ngủ, giật mình, buồn nhiều tuần. Đó là phản ứng thường gặp; bạn nên được giúp.',
  f'<strong>Kỹ năng ngắn:</strong> WHO có sách minh họa quản lý căng thẳng, có bản tiếng Việt. Thiền, tinh thần chuyên sâu có ở trang chị em tamhonkhoe.com.'],
 '<p><strong>Bài 1: kế hoạch an toàn của tôi.</strong></p>'
 + lines(['Người 1 (gọi lúc nửa đêm)', 'Người 2 (cho ở nhờ)', 'Người 3 (hiểu luật, thủ tục)', 'Mật mã gọi đón',
          'Số đã lưu: 113 · 115 · 117 · 111 · 096 306 1414', 'Giấy tờ gốc, tiền dự phòng ở', 'Nơi an toàn gần nhà, chỗ làm'])
 + '<p><strong>Bài 2: đã báo trước?</strong></p>'
 + table(['Người', 'Đã báo ✓', 'Họ nói gì'], [['1.', '', ''], ['2.', '', ''], ['3.', '', '']]),
 ol(['Gọi hoặc gặp từng người, báo bạn đã chọn họ.', 'Làm tự đánh giá cuối khóa ở công cụ, so với bài 1.',
     'Hoặc viết: "Một năm nữa, mình muốn tự tin hơn ở…"']),
 ['Cất kế hoạch ở chỗ an toàn. Có thể chụp ảnh lưu ở nơi người khác không xem được.',
  'Buồn, lo kéo dài, có ý nghĩ làm hại bản thân: nói ngay với người tin cậy, gọi Ngày Mai hoặc 115.'],
 ['Tôi có kế hoạch an toàn 5 phần', 'Tôi đã báo trước cho 3 người', 'Tôi làm tự đánh giá cuối khóa'],
 ['Khi được chọn là người có thể nhờ: đồng ý thật lòng, lưu số, giữ máy.', 'Không cần hỏi lý do khi bạn ấy gọi nhờ. Giúp trước, hỏi sau.',
  'Hỏi thăm sau khóa: "Có điều gì em muốn tập thêm không?"'],
 [lb('Đã xác nhận', f'Sách minh họa của WHO về quản lý căng thẳng, bài tập vài phút mỗi ngày, có bản tiếng Việt ({DWM}).'),
  lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}); Tổng đài 111 ({T111}). Tra 28/10/2026, kiểm tra lại mỗi quý.'),
  lb('Đánh giá chuyên môn', 'Mẫu kế hoạch an toàn năm phần do daynentang.com soạn, dựa trên cách làm phổ biến của các tổ chức hỗ trợ người bị bạo lực.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi biết điểm mạnh của mình, có bằng chứng', 'Tôi nói câu ranh giới rõ, bình tĩnh', 'Tôi rời đi khi thấy bất an, biết kêu cứu',
         'Tôi biết làm gì khi bị quấy rối', 'Tôi dùng Trước – Trong – Sau khi đi lại', 'Tôi giữ riêng tư trên mạng, biết làm gì khi bị dọa',
         'Tôi nhận ra dấu hiệu kiểm soát, biết số 117, 111', 'Tôi kiểm tra lời mời việc làm trước khi nhận', 'Tôi có quỹ dự phòng, tự giữ giấy tờ',
         'Tôi có kế hoạch an toàn và 3 người có thể nhờ']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Kế hoạch an toàn của tôi', 'Trang in cho khóa Tự tin – an toàn: điểm mạnh, câu ranh giới, cách thoát ra, ghi lại quấy rối, đi lại, mạng, dấu hiệu kiểm soát, lời mời việc làm, quỹ dự phòng, kế hoạch an toàn.',
f'''
<h1>Kế hoạch an toàn của tôi</h1>
<p>Dùng cho khóa <a href="{U}">Tự tin – an toàn</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Cất phiếu ở chỗ chỉ bạn biết.</p>
{PRINT_ROW}
<h2>1. Điểm mạnh (bài 1)</h2>
{table(['Điểm mạnh', 'Việc thật chứng minh'], [['1.', ''], ['2.', ''], ['3.', '']])}
<h2>2. Câu ranh giới (bài 2)</h2>
<p>"Khi bạn … , mình thấy … . Mình muốn … ." · Khi bị ép: "Mình đã nói không."</p>
{lines(['Câu ranh giới của tôi'])}
<h2>3. Thoát ra và kêu cứu (bài 3)</h2>
<p>Nhận ra → Nói rõ → Rời đi → Kêu cứu. Kêu cứu chỉ đích danh: "Chị áo xanh ơi, gọi giúp em 113!"</p>
{lines(['Câu viện cớ để rời đi', 'Câu kêu cứu của tôi'])}
<h2>4. Ghi lại khi bị quấy rối (bài 4)</h2>
{table(['Ngày', 'Giờ', 'Nơi', 'Ai', 'Việc gì', 'Chứng kiến'], [['', '', '', '', '', ''], ['', '', '', '', '', '']])}
<h2>5. Đi lại (bài 5)</h2>
<p>Trước: báo nơi đến, giờ về · Trong: kiểm biển số, tài xế, tên · Sau: nhắn "đã tới".</p>
{lines(['Mật mã gọi đón', 'Người biết mật mã'])}
<h2>6. Mạng (bài 6)</h2>
<p>Bị dọa tung ảnh: không trả tiền, không gửi thêm · chụp lại bằng chứng · chặn, báo nền tảng · nói với người tin cậy, báo công an. Gỡ ảnh: Take It Down (ảnh khi dưới 18 tuổi), StopNCII (từ 18 tuổi).</p>
<h2>7. Dấu hiệu kiểm soát (bài 7)</h2>
<p>Kiểm tra điện thoại · cấm gặp bạn bè · giữ tiền, giấy tờ · làm nhục · đe dọa · ép buộc · đánh. Bạo lực không phải lỗi của bạn.</p>
<h2>8. Trước khi nhận việc xa (bài 8)</h2>
{table(['Câu hỏi', 'Trả lời'], [['Việc gì?', ''], ['Ở đâu, địa chỉ thật?', ''], ['Giờ làm?', ''], ['Lương, trả khi nào?', ''], ['Hợp đồng?', ''], ['Ai tuyển, có giấy phép?', '']])}
<p>Giấy tờ gốc luôn ở trong tay bạn · để lại bản sao cho người thân · hẹn giờ gọi về.</p>
<h2>9. Tiền và giấy tờ (bài 9)</h2>
<p>Quỹ dự phòng: …………… · Giấy tờ gốc ở: …………… · Mật khẩu, OTP: chỉ mình tôi biết.</p>
<h2>10. Kế hoạch an toàn (bài 10)</h2>
{lines(['Người 1 (gọi lúc nửa đêm)', 'Người 2 (cho ở nhờ)', 'Người 3 (hiểu luật, thủ tục)', 'Nơi an toàn gần nhà', 'Nơi an toàn gần chỗ làm, chỗ học'])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">113</th><td>Công an, khi nguy hiểm ngay</td></tr>
<tr><th>115</th><td>Cấp cứu y tế</td></tr>
<tr><th>117</th><td>Phòng, chống bạo lực gia đình (24/7)</td></tr>
<tr><th>111</th><td>Bảo vệ trẻ em dưới 18 tuổi; nhận tin báo mua bán người (24/7)</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
</tbody></table></div>
<h2>Tự đánh giá (bài 1 và bài 10)</h2>
<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Bài 1</th><th>Bài 10</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán hay đánh giá nguy cơ.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Tự tin – an toàn', 'Khóa tự học miễn phí cho bạn nữ từ 13 tuổi và phụ nữ: tự tin, ranh giới, thoát ra và kêu cứu, quấy rối, đi lại, an toàn mạng, quan hệ lành mạnh, bẫy việc làm, tiền riêng, kế hoạch an toàn.',
f'''
<p class="eyebrow">Cá nhân · Khóa C6 · Đang thử nghiệm</p>
<h1>Tự tin – an toàn</h1>
<p class="lead">An toàn bắt đầu từ việc biết mình được nói "không", được rời đi và được nhờ giúp. Khóa này giúp bạn tập ba điều đó, từng bước nhỏ.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn nói rõ ranh giới, nhận ra nguy cơ sớm, biết rời đi và kêu cứu, giữ an toàn khi đi lại, trên mạng, khi nhận việc, và có kế hoạch an toàn của riêng mình</td></tr>
<tr><th>Dành cho</th><td>Bạn nữ từ 13 tuổi và phụ nữ. Bạn 13–17 tuổi nên học cùng một người lớn tin cậy</td></tr>
<tr><th>Thời lượng</th><td>10 bài, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, nói hoặc viết 5 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút, điện thoại; một người tin cậy để tập bài 2–3</td></tr>
<tr><th>Tình trạng</th><td>Đủ 10 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của chị em phụ nữ, nhân viên công tác xã hội, huấn luyện viên tự vệ</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn có câu ranh giới và câu kêu cứu đã tập.</li><li>Bạn kiểm xe, báo nơi đến, có mật mã gọi đón.</li><li>Bạn đã lưu 113, 117, 111 và có 3 người có thể nhờ.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: mình được nói "không", được rời đi, và bị hại không phải lỗi của mình.</li><li>Kỹ năng: giao tiếp quả quyết, nhận ra kiểm soát, giữ tiền và giấy tờ riêng.</li><li>Biết nhờ giúp sớm.</li></ul></div>
</div>
{figure_block('KHOAS')}

<h2 id="muoi-bai">Mười bài</h2>
<div class="table-wrap"><table>
<thead><tr><th>Bài</th><th>Tên</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Kế hoạch an toàn của tôi</a>: điểm mạnh, câu ranh giới, ghi lại quấy rối, mật mã gọi đón, dấu hiệu kiểm soát, lời mời việc làm, quỹ dự phòng, số khẩn cấp, tự đánh giá.</li>
<li><a href="{BTC}">Bảng thu chi</a>: ghi chi 7 ngày (dùng ở bài 9).</li></ul>

<h2>Cho người đồng hành</h2>
<ul>
<li>Bố mẹ, thầy cô của bạn 13–17 tuổi: học cùng, nhất là bài 3, 6, 7, 8. Hứa trước rằng con kể gì cũng không bị mắng.</li>
<li>Tập bài 2–3 cùng bạn ấy theo đúng luật tập an toàn.</li>
<li>Khi bạn ấy kể chuyện khó: tin, nghe, không trách, cùng quyết định bước tiếp theo.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{SENN}</td><td>Nhận diện nguy cơ, vượt rào cản cảm xúc, tự vệ lời nói và thân thể</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên, 893 nữ sinh viên; bị hiếp dâm sau 1 năm 5,2% so với 9,8%</td></tr>
<tr><td>{SAR14}</td><td>Ranh giới, lời nói quả quyết, kỹ năng thoát ra</td><td><span class="label">[Đã xác nhận]</span> 2.406 nữ sinh ở Nairobi; tỷ lệ bị hiếp dâm trong nhóm học giảm sau khoảng 10 tháng</td></tr>
<tr><td>{SAR23}</td><td>Lý do thận trọng</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm lớn hơn, 3.263 nữ sinh 10–14 tuổi: không thấy giảm sau 24 tháng</td></tr>
<tr><td>{WHOV}; {SURV}</td><td>Mức độ phổ biến của bạo lực</td><td><span class="label">[Đã xác nhận]</span> Số liệu thế giới và Việt Nam</td></tr>
<tr><td>{D8}; {D17}; {PCMBN}; {T111M}</td><td>Quấy rối nơi làm việc, giấy tờ, mua bán người, tổng đài 111</td><td><span class="label">[Đã xác nhận]</span> Văn bản pháp luật Việt Nam, đọc qua trang tóm tắt; nguyên văn một số điều [Cần kiểm chứng]</td></tr>
<tr><td>{TID}</td><td>Gỡ ảnh riêng tư</td><td><span class="label">[Đã xác nhận]</span> Dịch vụ miễn phí, ảnh không rời máy người dùng</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các chương trình có kết quả tốt đều dạy trực tiếp, nhiều giờ, có huấn luyện viên. Kết quả lại không đồng nhất: một thử nghiệm lớn ở Kenya không thấy hiệu quả. Khóa tự học này chưa được thử nghiệm, nên chúng tôi không hứa giảm nguy cơ.</p>
  <p>An toàn của bạn không chỉ phụ thuộc vào bạn. Người gây hại mới là người phải chịu trách nhiệm. Khóa không thay thế lớp tự vệ có người hướng dẫn, hỗ trợ của công an, y tế, luật sư hay nhân viên công tác xã hội.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C6 built')
