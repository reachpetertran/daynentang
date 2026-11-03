# Khóa C4 "Vững nghề" – trang khóa, 10 bài, công cụ "Sổ tay nghề của tôi".
# Người đọc gồm học viên 15–17 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c4  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/vung-nghe/'
TOOL = '/cong-cu/so-tay-nghe/'
C2V = '/khoa-hoc/hieu-minh/tuan-2/dieu-minh-coi-trong/'
C3 = '/khoa-hoc/tu-hoc-tu-quan/'
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
ILO = '<a href="https://www.ilo.org/node/653131">ILO – Improving the Safety and Health of Young Workers (soạn cho Ngày An toàn lao động thế giới 2018)</a>'
MAC = '<a href="https://www.sciencedaily.com/releases/2014/07/140716123835.htm">Macnamara, Hambrick &amp; Oswald 2014, <em>Psychological Science</em> (ScienceDaily đưa tin)</a>'
ATVS = '<a href="https://danchuphapluat.vn/quyen-tu-choi-lam-viec-khi-phat-hien-nguy-co-gay-chay-no-de-doa-tinh-mang-9563.html">Luật An toàn, vệ sinh lao động 84/2015/QH13, Điều 6 khoản 1 điểm đ (báo Dân chủ &amp; Pháp luật tóm tắt)</a>'
LDCTN = '<a href="https://lsvn.vn/quy-dinh-ve-su-dung-lao-dong-la-nguoi-chua-thanh-nien1666196792-a125368.html">Bộ luật Lao động 2019 về lao động chưa thành niên, Điều 143–147 (Báo Luật sư Việt Nam, 19/10/2022)</a>'
HN61 = '<a href="https://ketoananpha.vn/hoc-nghe-la-gi.html">Bộ luật Lao động 2019, Điều 61 (trang tóm tắt)</a>'
D17 = '<a href="https://hethongphapluat.com/bo-luat-lao-dong-2019/khoan-1-dieu-17">Bộ luật Lao động 2019, Điều 17 khoản 1</a>'
LVL = '<a href="https://luatvietnam.vn/lao-dong-tien-luong/diem-moi-cua-luat-viec-lam-2025-562-102940-article.html">Luật Việc làm 74/2025/QH15, Điều 26 (LuatVietnam tóm tắt)</a>'
WHOH = '<a href="https://www.who.int/news-room/fact-sheets/detail/deafness-and-hearing-loss">WHO – Điếc và giảm thính lực (3/3/2026)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
AASMA = '<a href="https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf">AASM và SRS 2015, <em>J Clin Sleep Med</em> 11(6)</a>'
WHOPA = '<a href="https://who.int/initiatives/behealthy/physical-activity">WHO – Be Healthy: vận động</a>'
PA = '<a href="https://knowledge-for-policy.ec.europa.eu/health-promotion-knowledge-gateway/physical-activity-sedentary-behaviour-table-2a_en">khuyến nghị WHO cho tuổi 5–17 (bảng tổng hợp của EU)</a>'
BLDS = '<a href="https://div.gov.vn/can-hieu-dung-ve-tran-lai-suat-cho-vay-20-nam">Bộ luật Dân sự 2015, Điều 468</a>'
VOH = '<a href="https://voh.com.vn/phap-luat/cong-an-canh-bao-3-chieu-bat-coc-online-nham-vao-hoc-sinh-sinh-vien-625691.html">Bộ Công an cảnh báo (VOH, 12/10/2025)</a>'
DWM = '<a href="https://who.int/publications/i/item/9789240003927">WHO – Doing What Matters in Times of Stress (29/4/2020, có bản tiếng Việt)</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài viết chưa được thầy dạy nghề, cán bộ an toàn lao động hay luật sư duyệt. Phần luật chỉ là thông tin chung, không phải tư vấn pháp lý.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Những gì bạn viết là của riêng bạn. '
           'Thầy dạy nghề, gia đình (từ 18 tuổi) có thể góp ý ở trang <a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên hay nơi làm.</p>')
TALK = ('Tai nạn, người bị thương nặng: gọi <strong>115</strong>. Cháy nổ: <strong>114</strong>. Bị đe dọa, ép buộc: <strong>113</strong>. '
        'Dưới 18 tuổi bị ép làm việc nguy hiểm, bị đánh: <strong>111</strong> (miễn phí, 24/7). Buồn, lo kéo dài: Ngày Mai <strong>096 306 1414</strong>.')

L = {
 '1': (1, 'bac-thang-ky-nang', 'Bài 1', 'Nghề mình chọn và bậc thang kỹ năng'),
 '2': (2, 'hoc-tay-nghe', 'Bài 2', 'Học tay nghề: xem – làm cùng – tự làm – tự kiểm'),
 '3': (3, 'an-toan-truoc-het', 'Bài 3', 'An toàn trước hết'),
 '4': (4, 'lam-dung-lan-dau', 'Bài 4', 'Làm đúng ngay lần đầu'),
 '5': (5, 'chinh-truc-trong-nghe', 'Bài 5', 'Chính trực trong nghề'),
 '6': (6, 'hoi-bao-cao-gop-y', 'Bài 6', 'Hỏi, báo cáo, nhận góp ý'),
 '7': (7, 'quyen-co-ban', 'Bài 7', 'Học nghề, thực tập, làm thêm: quyền cơ bản'),
 '8': (8, 'suc-khoe-nghe', 'Bài 8', 'Giữ sức khỏe khi làm nghề'),
 '9': (9, 'dong-luong-dau-tien', 'Bài 9', 'Đồng lương đầu tiên'),
 '10': (10, 'ho-so-ky-nang', 'Bài 10', 'Hồ sơ kỹ năng và bước tiếp theo'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn có bậc thang 6 kỹ năng của nghề và 1 kỹ năng luyện tháng này, có mức đạt đo được.'),
 (2, 'Bạn ghi nhật ký luyện ít nhất 5 buổi, mỗi buổi sửa 1 lỗi cụ thể.'),
 (3, 'Bạn rà soát 1 chỗ làm, ghi ít nhất 3 mối nguy và cách phòng.'),
 (4, 'Bạn có danh sách tự kiểm 5 mục và làm 5S chỗ làm 5 ngày.'),
 (5, 'Bạn đúng giờ 5/5 ngày và xử lý 3 tình huống giả định theo hướng chính trực.'),
 (6, 'Bạn gửi 3 báo cáo ba phần và nhắc lại lệnh trước khi làm.'),
 (7, 'Bạn kiểm tra 1 việc học nghề hoặc làm thêm theo 6 câu hỏi.'),
 (8, 'Bạn dùng đủ đồ bảo hộ 5/5 ngày và ghi giờ ngủ 7 ngày.'),
 (9, 'Bạn ghi chi 7 ngày và chia tiền tháng theo 4 phần.'),
 (10, 'Bạn có hồ sơ kỹ năng 1 trang và kế hoạch khi quá tải.'),
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
        sec(5, 'Xem lại với thầy, bạn cùng lớp hoặc tự viết (5 phút)', talk),
        sec(6, 'An toàn', ul(safety + [TALK])),
        sec(7, 'Tự đánh giá', selftab(selfq)),
        sec(8, 'Cho thầy dạy nghề, người kèm cặp, gia đình', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Vững nghề</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('E' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Vững nghề, bài 1: chia nghề thành các kỹ năng nhỏ, xếp thành bậc thang, chọn một kỹ năng luyện tháng này với mức đạt đo được.',
 ['Viết <strong>1 câu</strong> vì sao mình học nghề này.',
  'Liệt kê <strong>6 kỹ năng</strong> của nghề, xếp từ dễ đến khó.',
  'Chọn <strong>1 kỹ năng</strong> luyện tháng này, có <strong>mức đạt đo được</strong>.'],
 [f'In trang 1 của <a href="{TOOL}">Sổ tay nghề của tôi</a>, hoặc lấy một tờ giấy.', 'Chương trình học hoặc danh sách bài thực hành của lớp nghề.'],
 ['<strong>Nghề nào cũng là chuỗi kỹ năng nhỏ.</strong> Thợ điện: đọc sơ đồ, đi dây, đấu nối, đo kiểm. Thợ may: đo, cắt, may thẳng, may cong, hoàn thiện.',
  '<strong>Biết lý do mình học</strong> giúp bạn đi tiếp lúc khó. Lý do có thể là thu nhập, sở thích, gia đình, hay muốn làm ra thứ có ích.',
  '<strong>Bậc thang kỹ năng</strong> có ba bậc: bậc 1 làm khi thầy cầm tay; bậc 2 làm khi thầy đứng xem; bậc 3 tự làm đạt chuẩn.',
  '<strong>Mức đạt phải đo được:</strong> làm gì, sai số bao nhiêu, trong bao lâu. "May cho đẹp" chưa đo được.',
  '<strong>Ví dụ minh họa</strong> (không phải chuẩn của nghề): "may 1 mét đường thẳng, lệch không quá 2 mm, trong 3 phút". Hỏi thầy chuẩn thật của nghề bạn.',
  '<strong>Hỏi thầy chuẩn đầu ra</strong> của khóa học và tiêu chuẩn kỹ năng nghề quốc gia của nghề bạn, nếu có.',
  '<strong>Một số nghề bắt buộc chứng chỉ.</strong> Từ 01/01/2026, người làm việc ảnh hưởng trực tiếp an toàn, sức khỏe phải có chứng chỉ kỹ năng nghề quốc gia, theo danh mục của Chính phủ.'],
 '<p><strong>Bài 1: lý do của tôi.</strong> Mình học nghề này vì …………………………………………</p>'
 + '<p><strong>Bài 2: bậc thang kỹ năng.</strong> Đánh dấu ✓ vào bậc bạn đang đứng.</p>'
 + table(['Kỹ năng (từ dễ đến khó)', 'Bậc 1: thầy cầm tay', 'Bậc 2: thầy đứng xem', 'Bậc 3: tự làm đạt'], [[f'{n}.', '', '', ''] for n in range(1, 7)])
 + '<p><strong>Bài 3: kỹ năng tháng này.</strong></p>'
 + lines(['Kỹ năng', 'Mức đạt đo được (làm gì, sai số, thời gian)', 'Hỏi thầy chuẩn này vào ngày']),
 ol(['Đưa bậc thang cho thầy xem. Hỏi: "Em xếp vậy đúng chưa? Em đang ở bậc nào?"', 'Sửa bậc thang theo góp ý của thầy.',
     'Hoặc viết: "Một năm nữa, mình muốn tự làm được…"']),
 ['Kỹ năng bạn chưa được hướng dẫn: đặt ở bậc 1, chưa tự làm một mình.',
  'Mỗi kỹ năng ghi kèm đồ bảo hộ cần có (xem bài 3).'],
 ['Tôi viết được lý do học nghề', 'Tôi có bậc thang 6 kỹ năng', 'Tôi có 1 kỹ năng tháng này với mức đạt đo được'],
 ['Cho học viên xem sản phẩm đạt chuẩn và sản phẩm chưa đạt. So sánh giúp họ hiểu "đạt" là gì.',
  'Nói rõ chuẩn bằng số đo, thời gian khi có thể.', 'Gia đình: hỏi con đang ở bậc nào, không hỏi "học xong chưa".'],
 [lb('Đã xác nhận', f'Luật Việc làm 74/2025/QH15 (thông qua 16/6/2025, hiệu lực 01/01/2026), Điều 26: người làm công việc ảnh hưởng trực tiếp an toàn, sức khỏe của mình hay cộng đồng phải có chứng chỉ kỹ năng nghề quốc gia; Chính phủ ban hành danh mục ({LVL}).'),
  lb('Cần kiểm chứng', 'Danh mục nghề bắt buộc chứng chỉ theo văn bản hướng dẫn Luật Việc làm 2025: chúng tôi chưa đọc nguyên văn. Hỏi trường nghề hoặc Sở phụ trách lao động nơi bạn ở.'),
  lb('Đánh giá chuyên môn', 'Bậc thang ba bậc và mẫu mức đạt đo được do daynentang.com soạn. Con số trong ví dụ may là minh họa, không phải chuẩn nghề.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Vững nghề, bài 2: học kỹ năng tay theo bốn bước, luyện có chủ đích, ghi nhật ký luyện, biết lúc nào phải dừng để hỏi.',
 ['Nói được <strong>4 bước</strong> học một kỹ năng tay.',
  'Ghi <strong>nhật ký luyện</strong> ít nhất 5 buổi.',
  'Mỗi buổi chọn <strong>1 lỗi</strong> để sửa.'],
 [f'In trang 2 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Kỹ năng tháng này (từ bài 1).'],
 ['<strong>Bốn bước học kỹ năng tay:</strong> (1) xem người giỏi làm, nghe giải thích; (2) làm cùng, được chỉnh ngay; (3) tự làm, thầy xem; (4) tự kiểm, sửa lỗi.',
  '<strong>Đừng nhảy cóc.</strong> Tự làm khi chưa qua bước 2 dễ hỏng vật liệu, dễ bị thương, và dễ quen tay sai.',
  '<strong>Luyện có chủ đích:</strong> chọn một phần khó, làm lại nhiều lần, có người góp ý ngay, mỗi lần sửa một điểm.',
  '<strong>Luyện nhiều có ích, nhưng không phải tất cả.</strong> Tổng hợp 88 nghiên cứu: luyện tập giải thích khoảng 26% chênh lệch ở trò chơi, 18% ở thể thao.',
  '<strong>Ở công việc, con số này dưới 1%.</strong> Nghĩa là cách luyện, góp ý, hiểu biết, sức khỏe, môi trường làm việc cũng rất quan trọng. Đừng chỉ đếm giờ.',
  '<strong>Nhật ký luyện</strong> ghi: ngày, phần luyện, số lần, lỗi chính, lần sau sửa gì. Sau 2 tuần, bạn sẽ thấy lỗi nào đã hết.',
  '<strong>Dừng để hỏi</strong> khi: không chắc cách làm, máy kêu lạ, sắp cắt hay khoan vào vật liệu đắt. Hỏi một câu rẻ hơn làm hỏng một lần.'],
 '<p><strong>Nhật ký luyện 5 buổi.</strong></p>'
 + table(['Ngày', 'Phần luyện', 'Số lần', 'Lỗi chính', 'Lần sau sửa gì'], [['', '', '', '', ''] for _ in range(5)])
 + '<p class="small">Mẹo: viết lỗi cụ thể, ví dụ "mối hàn lệch sang trái", không viết "làm chưa đẹp".</p>',
 ol(['Nhờ thầy hoặc thợ giỏi xem bạn làm 5 phút và chỉ 1 điểm cần sửa.', 'Ghi điểm đó vào nhật ký, buổi sau chỉ tập trung sửa điểm này.',
     'Hoặc viết: "Lỗi mình đã sửa được trong tuần là…"']),
 ['Chỉ dùng máy, dụng cụ đã được hướng dẫn và cho phép.', 'Luyện lâu một động tác: nghỉ ngắn, đổi tư thế, nhất là cổ tay, lưng.',
  'Mệt, buồn ngủ: dừng luyện với máy móc, dao, lửa, điện.'],
 ['Tôi nói được 4 bước học kỹ năng tay', 'Tôi ghi nhật ký luyện 5 buổi', 'Mỗi buổi tôi sửa 1 lỗi cụ thể'],
 ['Làm mẫu chậm, nói to từng bước. Rồi làm lại ở tốc độ thật.', 'Góp ý từng điểm một, nói cụ thể, kèm cách sửa.',
  'Khen việc học viên tự phát hiện và sửa lỗi của mình.'],
 [lb('Đã xác nhận', f'Tổng hợp 88 nghiên cứu, hơn 11.000 người: luyện tập có chủ đích giải thích khoảng 26% chênh lệch thành tích ở trò chơi, 21% âm nhạc, 18% thể thao, 4% học tập, dưới 1% nghề nghiệp ({MAC}).'),
  lb('Suy luận', 'Nghiên cứu ở nhóm nghề nghiệp đo thành tích theo nhiều kiểu khác nhau. Con số "dưới 1%" không có nghĩa luyện tập vô ích; luyện vẫn cần nhưng chưa đủ.'),
  lb('Đánh giá chuyên môn', 'Bốn bước học kỹ năng tay và mẫu nhật ký luyện là cách dạy nghề phổ biến, do daynentang.com viết lại. Chưa có thử nghiệm riêng.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Vững nghề, bài 3: năm câu hỏi trước việc mới, đồ bảo hộ, rà soát mối nguy, quyền dừng việc khi thấy rõ nguy hiểm.',
 ['Hỏi đủ <strong>5 câu</strong> trước một việc mới.',
  'Rà soát <strong>1 chỗ làm</strong>, ghi ít nhất <strong>3 mối nguy</strong> và cách phòng.',
  'Nói được <strong>quyền dừng việc</strong> và việc phải làm ngay sau đó.'],
 [f'In trang 3 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Chọn chỗ làm để rà soát: xưởng thực hành, bếp, tiệm sửa xe, nơi làm thêm.'],
 ['<strong>Người mới vào nghề dễ bị tai nạn hơn.</strong> Theo ILO, người lao động trẻ bị tai nạn lao động không chết người cao hơn tới 40% so với người trên 25 tuổi.',
  '<strong>Vì sao?</strong> Chưa biết mối nguy, ngại hỏi, muốn làm nhanh để được khen, chưa quen máy. Biết vậy để tự nhắc mình.',
  '<strong>Năm câu hỏi trước việc mới:</strong> có thể bị thương ra sao? Cần đồ bảo hộ gì? Đã được hướng dẫn chưa? Sự cố thì làm gì? Hỏi ai?',
  '<strong>Đồ bảo hộ đúng việc:</strong> kính, mặt nạ hàn, găng, giày, nút tai, khẩu trang. Không tháo tấm che của máy cho nhanh.',
  '<strong>Quyền dừng việc:</strong> thấy rõ nguy cơ tai nạn nghiêm trọng đe dọa tính mạng, sức khỏe, bạn có quyền từ chối làm hoặc rời chỗ làm.',
  '<strong>Sau khi dừng, phải báo ngay</strong> người quản lý trực tiếp. Làm tiếp khi mối nguy đã được xử lý. Dừng việc như vậy không bị coi là vi phạm kỷ luật.',
  '<strong>Dưới 18 tuổi</strong> không được làm một số việc: mang vác quá sức, hàn cắt kim loại, sửa máy, hóa chất, công trường… Luật có danh mục cấm.'],
 '<p><strong>Bài 1: rà soát chỗ làm.</strong> Chỗ làm: ……………</p>'
 + table(['Mối nguy (thấy gì?)', 'Có thể gây ra gì?', 'Cách phòng', 'Đồ bảo hộ'], [['', '', '', ''] for _ in range(4)])
 + '<p><strong>Bài 2: câu dừng việc mẫu.</strong> <em>"Em thấy … có thể gây … Em dừng lại và báo anh/chị. Xử lý xong em làm tiếp."</em></p>'
 + lines(['Câu dừng việc của tôi', 'Người tôi báo khi có nguy hiểm']),
 ol(['Đưa phiếu rà soát cho thầy hoặc người phụ trách. Hỏi: "Em còn thiếu mối nguy nào?"', 'Hỏi vị trí bình chữa cháy, tủ sơ cứu, cầu dao tổng, lối thoát.',
     'Hoặc viết: "Việc làm mình sợ nhất ở chỗ làm là… Mình sẽ hỏi…"']),
 ['Người bị điện giật: không chạm vào người đó khi chưa ngắt điện. Ngắt cầu dao, rồi gọi 115.',
  'Báo cả lần "suýt bị tai nạn". Đó là lời nhắc miễn phí trước khi có tai nạn thật.',
  'Bỏng: làm mát vết bỏng dưới nước sạch mát, rồi đi khám nếu bỏng rộng hay sâu.'],
 ['Tôi hỏi đủ 5 câu trước việc mới', 'Tôi rà soát 1 chỗ làm, ghi 3 mối nguy', 'Tôi biết quyền dừng việc và phải báo ngay'],
 ['Hướng dẫn an toàn trước khi giao việc mới, kể cả việc "đơn giản". Hỏi lại để chắc học viên hiểu.',
  'Khen học viên dừng lại hỏi. Không chê "nhát" hay "chậm".', 'Gia đình: hỏi con chỗ làm có đồ bảo hộ không, có ai hướng dẫn không.'],
 [lb('Đã xác nhận', f'Người lao động trẻ (15–24 tuổi) bị tai nạn lao động không chết người cao hơn tới 40% so với người trên 25 tuổi ({ILO}).'),
  lb('Đã xác nhận', f'Người lao động có quyền từ chối làm hoặc rời nơi làm việc khi thấy rõ nguy cơ tai nạn nghiêm trọng, phải báo ngay người quản lý trực tiếp; không bị coi là vi phạm kỷ luật ({ATVS}).'),
  lb('Đã xác nhận', f'Người 15 đến dưới 18 tuổi không được làm một số việc và ở một số nơi, như mang vác quá sức, hàn kim loại, sửa máy, hóa chất, công trường ({LDCTN}).'),
  lb('Cần kiểm chứng', 'Chúng tôi chưa đọc nguyên văn Luật ATVSLĐ và Thông tư danh mục việc cấm. Danh sách trên là tóm tắt, chưa đầy đủ.'),
  lb('Đánh giá chuyên môn', 'Năm câu hỏi trước việc mới, phiếu rà soát và câu dừng việc mẫu do daynentang.com soạn.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Vững nghề, bài 4: hiểu yêu cầu trước khi làm, làm mẫu đầu, tự kiểm theo danh sách, giữ chỗ làm gọn theo 5S.',
 ['Viết <strong>danh sách tự kiểm 5 mục</strong> cho 1 việc của nghề.',
  'Làm <strong>mẫu đầu</strong> và tự kiểm trước khi làm loạt.',
  'Làm <strong>5S chỗ làm</strong> 10 phút, 5 ngày.'],
 [f'In trang 4 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Bản vẽ, đơn hàng hoặc yêu cầu của một việc bạn sắp làm.'],
 ['<strong>Hiểu yêu cầu trước khi làm.</strong> Đọc bản vẽ, đơn hàng. Không rõ số đo, vật liệu, màu: hỏi trước, không đoán.',
  '<strong>Làm mẫu đầu.</strong> Làm một sản phẩm, tự kiểm, nhờ thầy xem. Đạt rồi mới làm tiếp nhiều cái.',
  '<strong>Danh sách tự kiểm</strong> 5 mục: đúng kích thước, đúng số lượng, đúng hình thức, chắc chắn, sạch và an toàn. Đánh dấu từng mục.',
  '<strong>Thấy lỗi thì báo sớm.</strong> Giấu một lỗi nhỏ có thể thành lỗi lớn ở khách hàng.',
  '<strong>Tìm nguyên nhân,</strong> không tìm người để trách. Hỏi "vì sao" vài lần: lệch vì đo sai, đo sai vì thước mòn…',
  '<strong>5S giữ chỗ làm gọn:</strong> Sàng lọc (bỏ đồ thừa), Sắp xếp (đúng chỗ), Sạch sẽ, Săn sóc (giữ nề nếp), Sẵn sàng (thành thói quen).',
  '<strong>Chỗ làm gọn</strong> giúp tìm dụng cụ nhanh, ít vấp ngã, dễ thấy hỏng hóc.'],
 '<p><strong>Bài 1: danh sách tự kiểm.</strong> Việc: ……………</p>'
 + table(['Mục kiểm', 'Chuẩn', 'Mẫu đầu ✓/✗', 'Sửa gì?'], [['1. Kích thước', '', '', ''], ['2. Số lượng', '', '', ''], ['3. Hình thức', '', '', ''],
                                                    ['4. Chắc chắn', '', '', ''], ['5. Sạch, an toàn', '', '', '']])
 + '<p><strong>Bài 2: 5S trong 5 ngày.</strong> Mỗi ngày 10 phút cuối giờ.</p>'
 + table(['5S'] + DAYS[:5], [[x] + [''] * 5 for x in ['Sàng lọc', 'Sắp xếp', 'Sạch sẽ', 'Săn sóc', 'Sẵn sàng']]),
 ol(['Nhờ thầy xem mẫu đầu và danh sách tự kiểm. Hỏi: "Em còn thiếu mục nào?"', 'Sau 5 ngày, so chỗ làm trước và sau.',
     'Hoặc viết: "Lỗi mình hay mắc nhất là… Nguyên nhân là…"']),
 ['Dọn chỗ làm: tắt máy, ngắt điện trước khi lau. Không dùng tay gạt mạt kim loại.',
  'Hóa chất lau chùi: dùng đúng loại, đọc nhãn, đeo găng.'],
 ['Tôi có danh sách tự kiểm 5 mục', 'Tôi làm mẫu đầu rồi mới làm loạt', 'Tôi làm 5S 5 ngày'],
 ['Cho học viên tự kiểm trước khi thầy kiểm. So hai kết quả.', 'Khi học viên báo lỗi, cảm ơn trước rồi mới sửa.',
  'Giữ xưởng thực hành gọn để học viên thấy chuẩn hằng ngày.'],
 [lb('Đánh giá chuyên môn', '5S, làm mẫu đầu và danh sách tự kiểm là cách làm phổ biến trong quản lý chất lượng, do daynentang.com viết lại cho người học nghề.'),
  lb('Cần kiểm chứng', 'Chúng tôi chưa tìm được thử nghiệm đo hiệu quả của 5S hay danh sách tự kiểm với người học nghề. Bài không hứa con số cụ thể.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Vững nghề, bài 5: đúng giờ, nói thật về việc mình làm, không làm dối, nhận lỗi bốn bước, khi bị bảo làm sai.',
 ['Đúng giờ <strong>5/5 ngày</strong>, báo trước khi trễ.',
  'Xử lý <strong>3 tình huống giả định</strong> theo hướng chính trực.',
  'Dùng <strong>nhận lỗi 4 bước</strong> khi làm hỏng.'],
 [f'In trang 5 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', f'Nếu đã có, xem lại điều bạn coi trọng ở <a href="{C2V}">bài 2 khóa Hiểu mình</a>.'],
 ['<strong>Chữ tín là vốn của người thợ.</strong> Người ta giao việc khó, việc lương cao cho người tin được.',
  '<strong>Giờ giấc:</strong> đến trước giờ làm, báo trước khi trễ hoặc nghỉ, xong việc mới về.',
  '<strong>Nói thật về việc mình làm:</strong> báo lỗi, không ghi khống số lượng, không ký thay, không ký phiếu kiểm khi chưa kiểm.',
  '<strong>Làm thật:</strong> không bỏ bước kiểm, không thay vật liệu kém hơn, không làm ẩu khi không ai nhìn.',
  '<strong>Tài sản chỗ làm:</strong> dụng cụ, vật tư thừa không mang về khi chưa được phép.',
  '<strong>Nhận lỗi 4 bước:</strong> nói việc gì xảy ra; nói hậu quả; đề xuất cách sửa; nói cách tránh lần sau.',
  '<strong>Bị bảo làm sai:</strong> hỏi lại cho rõ, đề nghị cách khác, nếu vẫn sai thì báo người có trách nhiệm cao hơn. Nguy hiểm thì dừng (bài 3).'],
 '<p><strong>Bài 1: ba tình huống giả định.</strong> Các tình huống dưới đây do chúng tôi đặt ra, không có thật.</p>'
 + table(['Tình huống (giả định)', 'Tôi sẽ nói, sẽ làm'],
         [['Bạn làm hỏng một chi tiết. Chưa ai thấy.', ''],
          ['Tổ trưởng bảo bạn ký phiếu "đã kiểm" dù chưa kiểm.', ''],
          ['Bạn cùng tổ rủ mang vật tư thừa về nhà.', '']])
 + '<p><strong>Bài 2: đúng giờ 5 ngày.</strong></p>'
 + table(['Ngày'] + DAYS[:5], [['Đến đúng giờ ✓'] + [''] * 5, ['Báo trước khi trễ (nếu có)'] + [''] * 5]),
 ol(['Kể cách bạn xử lý tình huống 2 cho thầy hoặc người thân. Hỏi họ sẽ làm gì.', 'Tập nói to câu nhận lỗi 4 bước một lần.',
     'Hoặc viết: "Một người thợ mình tin được là người…"']),
 ['Bị ép làm sai gây nguy hiểm cho người khác (bỏ kiểm phanh, điện, gas): dừng, báo người phụ trách cao hơn.',
  'Bị đe dọa vì không làm sai: báo thầy, gia đình; nguy hiểm gọi 113.'],
 ['Tôi đúng giờ 5/5 ngày', 'Tôi xử lý 3 tình huống giả định', 'Tôi dùng nhận lỗi 4 bước'],
 ['Phản ứng bình tĩnh khi học viên báo lỗi. Nếu báo lỗi bị la mắng nặng, lần sau họ sẽ giấu.',
  'Kể một lần bạn từng nhận lỗi trong nghề và điều bạn học được.', 'Không giao học viên ký giấy tờ họ chưa kiểm.'],
 [lb('Đánh giá chuyên môn', 'Nội dung bài là chuẩn mực nghề nghiệp chung, do daynentang.com soạn. Ba tình huống là giả định.'),
  lb('Suy luận', 'Chúng tôi chưa trích nghiên cứu nào cho bài này. Bài không hứa kết quả đo được, chỉ đưa thói quen để tự theo dõi.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Vững nghề, bài 6: hỏi có chuẩn bị, nhắc lại lệnh, báo cáo ba phần, nhận góp ý, khi bị xúc phạm hay quấy rối.',
 ['Gửi <strong>3 báo cáo ba phần</strong>: đã xong, đang vướng, cần gì.',
  'Nhắc lại lệnh <strong>trước khi làm</strong>.',
  'Nhận góp ý theo <strong>4 bước</strong>.'],
 [f'In trang 6 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Nghĩ tới một việc bạn đang làm dở.'],
 ['<strong>Hỏi có chuẩn bị:</strong> nói mình đã thử gì, vướng ở đâu, rồi mới hỏi. "Em đã đo hai lần, vẫn lệch 3 mm, em nên kiểm gì?"',
  '<strong>Nhắc lại lệnh:</strong> "Em nhắc lại: cắt 20 tấm, dài 50 cm, xong trước 11 giờ, đúng không ạ?" Cách này tránh hiểu sai.',
  '<strong>Báo cáo ba phần:</strong> đã xong gì; đang vướng gì; cần gì. Ngắn, đúng lúc, có số liệu.',
  '<strong>Báo trước khi trễ hạn,</strong> không đợi tới hạn mới nói. Người quản lý cần thời gian xoay xở.',
  '<strong>Nhận góp ý:</strong> nghe hết, không cãi ngay; cảm ơn và hỏi một điểm cụ thể; sửa; báo lại đã sửa.',
  '<strong>Góp ý khác xúc phạm.</strong> "Mối hàn này lệch" là góp ý. Chửi bới, nói về gia đình, ngoại hình là xúc phạm.',
  '<strong>Bị xúc phạm, quấy rối, đánh:</strong> không phải "chịu cho quen nghề". Ghi lại ngày giờ, việc xảy ra, báo thầy hoặc người phụ trách.'],
 '<p><strong>Bài 1: ba báo cáo ba phần.</strong></p>'
 + table(['Ngày', 'Đã xong', 'Đang vướng', 'Cần gì'], [['', '', '', ''] for _ in range(3)])
 + '<p><strong>Bài 2: câu nhắc lại lệnh.</strong> <em>"Em nhắc lại: … , … , xong trước … , đúng không ạ?"</em></p>'
 + lines(['Câu nhắc lại lệnh của tôi', 'Một góp ý tôi nhận tuần này', 'Tôi đã sửa thế nào']),
 ol(['Gửi một báo cáo ba phần cho thầy hoặc người kèm cặp. Hỏi họ có dễ hiểu không.', 'Tập câu hỏi có chuẩn bị với một bạn cùng lớp.',
     'Hoặc viết: "Góp ý khó nghe nhất mình từng nhận là… Nó giúp mình…"']),
 ['Bị quấy rối tình dục, bị đánh, bị đe dọa: rời chỗ đó, báo người tin cậy. Nguy hiểm gọi 113.',
  'Dưới 18 tuổi bị bạo lực, bị ép làm việc: gọi 111 (miễn phí, 24/7).'],
 ['Tôi gửi 3 báo cáo ba phần', 'Tôi nhắc lại lệnh trước khi làm', 'Tôi nhận góp ý theo 4 bước'],
 ['Giao việc rõ: làm gì, bao nhiêu, xong khi nào, chuẩn ra sao. Mời học viên nhắc lại.',
  'Góp ý về việc, không về người. Góp ý riêng khi có thể.', 'Có một cách để học viên báo bị xúc phạm mà không sợ bị trả đũa.'],
 [lb('Đánh giá chuyên môn', 'Báo cáo ba phần, nhắc lại lệnh và nhận góp ý 4 bước là kỹ năng giao tiếp nơi làm việc phổ biến, do daynentang.com soạn.'),
  lb('Cần kiểm chứng', 'Chúng tôi chưa trích nghiên cứu về hiệu quả của các mẫu câu này với người học nghề ở Việt Nam.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Vững nghề, bài 7: hỏi rõ trước khi nhận học nghề, tập nghề, làm thêm; không đặt cọc, không giao giấy tờ gốc; quy định cho người dưới 18 tuổi.',
 ['Kiểm tra <strong>1 việc</strong> học nghề, thực tập hoặc làm thêm theo <strong>6 câu hỏi</strong>.',
  'Nói được <strong>3 điều</strong> chỗ làm không được đòi bạn.',
  'Biết <strong>giờ làm tối đa</strong> nếu bạn dưới 18 tuổi.'],
 [f'In trang 7 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Thông tin một chỗ học nghề, thực tập hay làm thêm bạn đang làm hoặc định nhận.'],
 ['<strong>Bài này là thông tin chung, không phải tư vấn pháp lý.</strong> Phần quyền lao động chuyên sâu sẽ có ở trang chị em trachnhiemxahoi.com.',
  '<strong>Sáu câu hỏi trước khi nhận:</strong> làm việc gì? ở đâu? giờ làm? tiền công bao nhiêu, trả khi nào? có hợp đồng, giấy tờ gì? ai hướng dẫn an toàn?',
  '<strong>Học nghề, tập nghề tại doanh nghiệp:</strong> người sử dụng lao động không được thu phí của bạn. Tập nghề tối đa 3 tháng. Người học nghề từ đủ 14 tuổi.',
  '<strong>Chỗ làm không được giữ bản chính</strong> căn cước, bằng cấp, chứng chỉ của bạn. Đưa bản sao khi cần.',
  '<strong>Không đặt cọc</strong> hay nộp "phí hồ sơ" để được nhận việc. Đây cũng là dấu hiệu lừa đảo hay gặp (bài 9).',
  '<strong>Dưới 18 tuổi:</strong> từ 15 đến dưới 18 tuổi làm tối đa 8 giờ một ngày, 40 giờ một tuần. Không làm việc trong danh mục cấm (bài 3).',
  '<strong>Giữ giấy tờ:</strong> chụp hoặc giữ bản hợp đồng, phiếu lương, lịch làm. Khi có tranh chấp, giấy tờ giúp bạn nhiều.'],
 '<p><strong>Bài 1: kiểm tra một việc.</strong> Việc: ……………</p>'
 + table(['Câu hỏi', 'Câu trả lời', 'Đủ rõ? ✓/✗'],
         [['1. Làm việc gì?', '', ''], ['2. Ở đâu?', '', ''], ['3. Giờ làm?', '', ''], ['4. Tiền công, trả khi nào?', '', ''],
          ['5. Hợp đồng, giấy tờ?', '', ''], ['6. Ai hướng dẫn an toàn?', '', '']])
 + '<p><strong>Bài 2: ba điều chỗ làm không được đòi.</strong></p>'
 + lines(['1.', '2.', '3.']),
 ol(['Cùng gia đình hoặc thầy đọc bảng 6 câu hỏi. Câu nào chưa rõ thì hỏi lại chỗ làm.', 'Lưu số điện thoại một người lớn tin cậy để hỏi trước khi ký giấy.',
     'Hoặc viết: "Điều mình cần hỏi rõ thêm là…"']),
 ['Chưa hiểu giấy tờ thì chưa ký. Mang về hỏi gia đình, thầy.',
  'Bị dụ đi làm xa, bị giữ giấy tờ, không cho liên lạc gia đình: gọi người thân và 113 ngay.'],
 ['Tôi kiểm tra 1 việc theo 6 câu hỏi', 'Tôi nói được 3 điều chỗ làm không được đòi', 'Tôi biết giờ làm tối đa nếu dưới 18 tuổi'],
 ['Cùng con đọc hợp đồng, thỏa thuận học nghề trước khi ký.', 'Hỏi con giờ làm thực tế mỗi tuần, nhất là khi con dưới 18 tuổi.',
  'Thầy: giới thiệu học viên tới chỗ thực tập có hướng dẫn an toàn rõ.'],
 [lb('Đã xác nhận', f'Người sử dụng lao động không được giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động ({D17}).'),
  lb('Đã xác nhận', f'Người 15 đến dưới 18 tuổi làm việc không quá 8 giờ một ngày và 40 giờ một tuần ({LDCTN}).'),
  lb('Đã xác nhận', f'Học nghề, tập nghề tại doanh nghiệp: không được thu phí của người học; tập nghề tối đa 3 tháng; người học nghề từ đủ 14 tuổi ({HN61}).'),
  lb('Cần kiểm chứng', 'Nguyên văn Điều 61 Bộ luật Lao động 2019 về tiền lương khi người học nghề trực tiếp làm ra sản phẩm: chúng tôi mới đọc trang tóm tắt.'),
  lb('Cần kiểm chứng', 'Điều khoản cụ thể cấm buộc người lao động đặt cọc: chúng tôi chưa đọc nguyên văn. Lời khuyên "không đặt cọc" là lời khuyên an toàn chung.'),
  lb('Đánh giá chuyên môn', 'Sáu câu hỏi trước khi nhận việc do daynentang.com soạn.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Vững nghề, bài 8: nâng vật đúng cách, đổi tư thế, bảo vệ mắt, tai, phổi, tay chân, ngủ đủ và vận động khi làm nghề.',
 ['Nâng vật theo <strong>4 bước</strong>.',
  'Dùng đủ <strong>đồ bảo hộ 5/5 ngày</strong>.',
  'Ghi <strong>giờ ngủ 7 ngày</strong>.'],
 [f'In trang 8 của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Liệt kê đồ bảo hộ bạn đang có.'],
 ['<strong>Sức khỏe là dụng cụ dùng cả đời.</strong> Đau lưng, giảm thính lực, hại mắt thường đến từ từ, khó chữa khi đã nặng.',
  '<strong>Nâng vật 4 bước:</strong> ước lượng vật; đứng gần, gập gối; giữ lưng thẳng, không vặn người; nặng quá thì nhờ người hoặc dùng xe đẩy.',
  '<strong>Đứng hay ngồi lâu:</strong> đổi tư thế, nghỉ ngắn, giãn cổ, vai, cổ tay giữa các việc.',
  '<strong>Tai:</strong> tiếng ồn lớn ở nơi làm việc là một nguyên nhân gây giảm thính lực. Phải nói to mới nghe được cách 1 mét: nên đeo nút tai.',
  '<strong>Mắt, phổi, da:</strong> kính khi mài, cắt; mặt nạ khi hàn; khẩu trang đúng loại với bụi, sơn, hóa chất; rửa tay trước khi ăn.',
  '<strong>Ngủ:</strong> 13–18 tuổi cần 8–10 giờ; người lớn từ 7 giờ trở lên. Làm ca đêm: giữ giờ ngủ cố định, phòng tối, yên tĩnh.',
  '<strong>Vận động:</strong> 5–17 tuổi khoảng 60 phút mỗi ngày; người lớn 150–300 phút mỗi tuần và tập cơ ít nhất 2 ngày.'],
 '<p><strong>Bài 1: đồ bảo hộ 5 ngày.</strong> Đánh dấu ✓ khi dùng đủ.</p>'
 + table(['Đồ bảo hộ'] + DAYS[:5], [[x] + [''] * 5 for x in ['Kính, mặt nạ', 'Nút tai, chụp tai', 'Khẩu trang', 'Găng tay', 'Giày']])
 + '<p><strong>Bài 2: ngủ 7 ngày.</strong></p>'
 + table(['Ngày', 'Lên giường', 'Dậy', 'Số giờ ngủ', 'Ca làm'], [[d, '', '', '', ''] for d in DAYS]),
 ol(['Nhờ thầy xem bạn nâng một vật, chỉnh tư thế.', 'Hỏi chỗ làm: đồ bảo hộ hỏng thì xin đổi ở đâu?',
     'Hoặc viết: "Phần cơ thể mình cần giữ gìn nhất trong nghề này là…"']),
 ['Đau lưng, tê tay kéo dài, ù tai, mờ mắt: đi khám, kể rõ công việc của bạn.',
  'Hóa chất bắn vào mắt: rửa ngay dưới vòi nước sạch nhiều phút, rồi đi khám.',
  'Không dùng nước tăng lực hay chất kích thích để làm xuyên đêm.'],
 ['Tôi nâng vật theo 4 bước', 'Tôi dùng đủ đồ bảo hộ 5/5 ngày', 'Tôi ghi giờ ngủ 7 ngày'],
 ['Có đủ đồ bảo hộ đúng cỡ cho học viên. Thay khi hỏng.', 'Làm gương: thầy cũng đeo kính, nút tai khi làm.',
  'Gia đình: giữ giờ ăn, giờ ngủ cho con khi con làm ca.'],
 [lb('Đã xác nhận', f'Tiếng ồn lớn và hóa chất ở nơi làm việc là nguyên nhân gây giảm thính lực; WHO khuyến nghị chương trình bảo vệ thính lực nghề nghiệp ({WHOH}).'),
  lb('Đã xác nhận', f'Tuổi 13–18 cần ngủ 8–10 giờ ({AASM}); người lớn từ 7 giờ ({AASMA}).'),
  lb('Đã xác nhận', f'Người lớn 18–64 tuổi: 150–300 phút vận động vừa mỗi tuần, tập cơ ít nhất 2 ngày ({WHOPA}). Tuổi 5–17: khoảng 60 phút mỗi ngày ({PA}).'),
  lb('Cần kiểm chứng', 'Giới hạn tiếng ồn tại nơi làm việc theo quy chuẩn Việt Nam: chúng tôi chưa đọc văn bản gốc nên không ghi con số.'),
  lb('Đánh giá chuyên môn', 'Bốn bước nâng vật, mẹo "nói to mới nghe được cách 1 mét" và lời khuyên làm ca đêm là hướng dẫn an toàn chung, do daynentang.com viết lại.')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Vững nghề, bài 9: đọc phiếu lương, ghi chi 7 ngày, chia lương theo 4 phần, tránh vay nặng lãi, nhận ra lừa đảo việc làm.',
 ['Ghi <strong>mọi khoản chi trong 7 ngày</strong>.',
  'Chia tiền tháng theo <strong>4 phần</strong>.',
  'Nêu được <strong>4 dấu hiệu lừa đảo</strong> việc làm.'],
 [f'In trang 9 của <a href="{TOOL}">Sổ tay nghề của tôi</a>, hoặc dùng <a href="{BTC}">Bảng thu chi</a>.', 'Phiếu lương hoặc số tiền nhận mỗi tháng.'],
 ['<strong>Đọc phiếu lương:</strong> xem số giờ, số ngày công, các khoản cộng, các khoản trừ. Khoản nào không hiểu thì hỏi bộ phận trả lương.',
  '<strong>Ghi chi 7 ngày</strong> trước khi lập kế hoạch. Cà phê, thuốc, ăn vặt cộng lại có thể thành số lớn.',
  '<strong>Chia ngay khi nhận lương:</strong> (1) cố định: trọ, điện nước, đi lại, gửi nhà; (2) ăn uống; (3) dự phòng; (4) phần còn lại.',
  '<strong>Dự phòng trước, tiêu sau.</strong> Ốm, hỏng xe, mất việc là chuyện có thể xảy ra với người mới vào nghề.',
  '<strong>Tránh vay nặng lãi.</strong> Lãi suất vay theo thỏa thuận không vượt quá 20% một năm. Ứng dụng, người lạ cho vay dễ thường đòi lãi cao hơn nhiều.',
  '<strong>Dấu hiệu lừa đảo việc làm:</strong> việc nhẹ lương cao bất thường; đòi đặt cọc, "phí hồ sơ"; mượn tài khoản, căn cước; đe dọa và bắt giữ bí mật.',
  '<strong>Gặp dấu hiệu đó:</strong> dừng, không chuyển tiền, không đọc mã OTP cho ai, gọi gia đình hoặc người tin cậy.'],
 table(['Ngày', 'Khoản chi', 'Số tiền', 'Cần / Muốn'], [[d, '', '', ''] for d in DAYS])
 + '<p><strong>Chia tiền tháng.</strong> Tổng nhận: ……………</p>'
 + table(['Phần', 'Số tiền', 'Ghi chú'], [['1. Cố định', '', ''], ['2. Ăn uống', '', ''], ['3. Dự phòng', '', ''], ['4. Phần còn lại', '', '']]),
 ol(['Cùng gia đình xem bảng chi 7 ngày. Hỏi bố mẹ cách họ chia lương.', 'Thống nhất với gia đình khoản gửi về nhà mỗi tháng.',
     'Hoặc viết: "Khoản chi làm mình bất ngờ nhất là…"']),
 ['Không cho mượn, không bán tài khoản ngân hàng, thẻ, căn cước, số điện thoại.',
  f'Bị dụ đi gặp người lạ, bị yêu cầu cắt liên lạc gia đình: dừng và gọi người nhà ngay (xem khóa <a href="{C1}">Lớn lên an toàn</a>).',
  'Bị đòi nợ đe dọa: báo gia đình và công an (113).'],
 ['Tôi ghi chi 7 ngày', 'Tôi chia tiền tháng theo 4 phần', 'Tôi nêu được 4 dấu hiệu lừa đảo'],
 ['Gia đình: để con tự chia lương, hỏi về bảng chi, không chỉ trích từng khoản.',
  f'Bố mẹ xem thêm khóa <a href="{G6}">Tiền nhà mình</a>.', 'Thầy: nhắc học viên các chiêu lừa việc làm hay gặp ở địa phương.'],
 [lb('Đã xác nhận', f'Lãi suất vay theo thỏa thuận không vượt quá 20%/năm của khoản tiền vay, trừ luật khác quy định ({BLDS}).'),
  lb('Đã xác nhận', f'Bộ Công an cảnh báo các chiêu nhắm vào học sinh, sinh viên: giả danh đe dọa, làm thân lâu ngày, dụ bằng việc làm hay tiền ({VOH}).'),
  lb('Đánh giá chuyên môn', 'Cách chia lương 4 phần và các dấu hiệu lừa đảo là lời khuyên chung do daynentang.com soạn. Bài chỉ dạy thu chi cơ bản, không tư vấn vay hay đầu tư.')])

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Vững nghề, bài 10: hồ sơ kỹ năng một trang, kể chuyện khi phỏng vấn, chứng chỉ kỹ năng nghề, kế hoạch khi quá tải.',
 ['Làm <strong>hồ sơ kỹ năng 1 trang</strong>.',
  'Kể <strong>1 việc thật</strong> theo 3 phần: tình huống, việc mình làm, kết quả.',
  'Viết <strong>kế hoạch khi quá tải</strong> và tên <strong>2 người</strong> có thể nhờ.'],
 [f'In trang 10 và phần tự đánh giá của <a href="{TOOL}">Sổ tay nghề của tôi</a>.', 'Bậc thang kỹ năng (bài 1) và nhật ký luyện (bài 2).'],
 ['<strong>Hồ sơ kỹ năng</strong> cho người tuyển dụng thấy bạn làm được gì. Gồm: kỹ năng đạt bậc 3, sản phẩm đã làm, nhận xét của thầy, chứng chỉ nếu có.',
  '<strong>Ảnh sản phẩm:</strong> chụp sản phẩm, không chụp mặt người khác, không chụp bí mật của chỗ làm khi chưa được phép.',
  '<strong>Phỏng vấn:</strong> kể một việc thật theo 3 phần: tình huống; việc mình làm; kết quả và điều học được.',
  '<strong>Bài thử tay nghề:</strong> nhiều nơi cho làm thử. Hỏi trước dụng cụ, thời gian, chuẩn đạt. Nhớ 5 câu hỏi an toàn (bài 3).',
  '<strong>Chứng chỉ kỹ năng nghề quốc gia</strong> bắt buộc với một số nghề ảnh hưởng an toàn (bài 1). Hỏi trường hoặc trung tâm dịch vụ việc làm cách đăng ký đánh giá.',
  '<strong>Khi quá tải:</strong> mệt, buồn hay lo kéo dài nhiều tuần, mất ngủ, muốn bỏ hết: nói với người tin cậy sớm. Nghĩ đến cái chết: nói ngay.',
  f'<strong>Học tiếp:</strong> nhiều người vừa làm vừa học thêm. Xem khóa <a href="{C3}">Tự học – tự quản</a> để lập kế hoạch học.'],
 '<p><strong>Bài 1: hồ sơ kỹ năng.</strong></p>'
 + table(['Mục', 'Của tôi'], [['Nghề, trình độ đang học', ''], ['3 kỹ năng đạt bậc 3', ''], ['2 sản phẩm đã làm (mô tả ngắn)', ''],
                              ['Nhận xét của thầy, quản đốc', ''], ['Chứng chỉ (nếu có)', ''], ['Kỹ năng đang luyện', '']])
 + '<p><strong>Bài 2: kể một việc thật.</strong></p>'
 + lines(['Tình huống', 'Việc mình làm', 'Kết quả, điều học được'])
 + '<p><strong>Bài 3: khi quá tải.</strong></p>'
 + lines(['3 dấu hiệu của tôi', 'Việc 15 phút đầu tiên', 'Người 1', 'Người 2']),
 ol(['Tập kể việc thật với một bạn cùng lớp, bấm giờ 2 phút.', 'Nhờ thầy đọc hồ sơ kỹ năng và góp ý 1 điểm.',
     'Kể một điều bạn làm vững hơn sau 10 tuần.']),
 ['Bài này không dùng để chẩn đoán. Dấu hiệu kéo dài: gặp bác sĩ hoặc chuyên gia tâm lý.',
  'Nghĩ đến cái chết hay muốn làm đau bản thân: nói ngay với người ở gần, gọi 115 nếu nguy hiểm.'],
 ['Tôi có hồ sơ kỹ năng 1 trang', 'Tôi kể được 1 việc thật theo 3 phần', 'Tôi có kế hoạch khi quá tải và 2 người để nhờ'],
 ['Viết nhận xét cụ thể cho học viên: kỹ năng nào đạt, mức nào. Nhận xét này rất có ích khi xin việc.',
  'Học viên mở lời về khó khăn: dừng việc, nghe hết, cảm ơn họ đã nói, giúp tìm người hỗ trợ.',
  'Nói về cái chết hay làm đau bản thân: ở bên họ, không để họ một mình, gọi 115 hoặc đưa tới cơ sở y tế.'],
 [lb('Đã xác nhận', f'Luật Việc làm 74/2025/QH15, Điều 26: một số công việc bắt buộc có chứng chỉ kỹ năng nghề quốc gia ({LVL}).'),
  lb('Đã xác nhận', f'Sách minh họa của WHO về quản lý căng thẳng, bài tập vài phút mỗi ngày, có bản tiếng Việt ({DWM}).'),
  lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}). Tra 28/10/2026, kiểm tra lại mỗi quý.'),
  lb('Cần kiểm chứng', 'Thủ tục, nơi đánh giá và cấp chứng chỉ kỹ năng nghề quốc gia theo văn bản hướng dẫn mới: chúng tôi chưa đọc văn bản gốc.'),
  lb('Đánh giá chuyên môn', 'Mẫu hồ sơ kỹ năng, cách kể 3 phần và kế hoạch khi quá tải do daynentang.com soạn.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi có bậc thang kỹ năng của nghề', 'Tôi luyện có chủ đích, có nhật ký', 'Tôi hỏi 5 câu an toàn trước việc mới',
         'Tôi tự kiểm trước khi giao sản phẩm', 'Tôi đúng giờ và nói thật về việc mình làm', 'Tôi báo cáo ba phần, nhận góp ý bình tĩnh',
         'Tôi hỏi rõ trước khi nhận việc, không đặt cọc', 'Tôi dùng đủ đồ bảo hộ và ngủ đủ', 'Tôi chia lương và có tiền dự phòng',
         'Tôi có hồ sơ kỹ năng và biết nhờ giúp']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Sổ tay nghề của tôi', 'Trang in cho khóa Vững nghề: bậc thang kỹ năng, nhật ký luyện, rà soát an toàn, tự kiểm, giờ giấc, báo cáo, kiểm tra việc làm, đồ bảo hộ, chia lương, hồ sơ kỹ năng.',
f'''
<h1>Sổ tay nghề của tôi</h1>
<p>Dùng cho khóa <a href="{U}">Vững nghề</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Sổ là của riêng bạn.</p>
{PRINT_ROW}
<h2>1. Bậc thang kỹ năng (bài 1)</h2>
{table(['Kỹ năng', 'Bậc 1', 'Bậc 2', 'Bậc 3'], [[f'{n}.', '', '', ''] for n in range(1, 7)])}
<p>Kỹ năng tháng này: ……………… · Mức đạt đo được: ………………</p>
<h2>2. Nhật ký luyện (bài 2)</h2>
{table(['Ngày', 'Phần luyện', 'Số lần', 'Lỗi chính', 'Lần sau sửa gì'], [['', '', '', '', ''] for _ in range(5)])}
<h2>3. Rà soát an toàn (bài 3)</h2>
{table(['Mối nguy', 'Có thể gây ra gì?', 'Cách phòng', 'Đồ bảo hộ'], [['', '', '', ''] for _ in range(3)])}
<p>Câu dừng việc: "Em thấy … có thể gây … Em dừng lại và báo anh/chị." · Người tôi báo: ………………</p>
<h2>4. Tự kiểm và 5S (bài 4)</h2>
{table(['Mục kiểm', 'Chuẩn', '✓/✗'], [['Kích thước', '', ''], ['Số lượng', '', ''], ['Hình thức', '', ''], ['Chắc chắn', '', ''], ['Sạch, an toàn', '', '']])}
<h2>5. Chính trực (bài 5)</h2>
{table(['Ngày'] + DAYS[:5], [['Đúng giờ ✓'] + [''] * 5])}
<p>Nhận lỗi 4 bước: việc gì xảy ra → hậu quả → cách sửa → cách tránh lần sau.</p>
<h2>6. Báo cáo ba phần (bài 6)</h2>
{table(['Ngày', 'Đã xong', 'Đang vướng', 'Cần gì'], [['', '', '', ''] for _ in range(3)])}
<h2>7. Trước khi nhận việc (bài 7)</h2>
{table(['Câu hỏi', 'Trả lời'], [['Làm việc gì?', ''], ['Ở đâu?', ''], ['Giờ làm?', ''], ['Tiền công, trả khi nào?', ''], ['Hợp đồng, giấy tờ?', ''], ['Ai hướng dẫn an toàn?', '']])}
<p>Không đặt cọc · Không giao bản chính giấy tờ · Dưới 18 tuổi: tối đa 8 giờ/ngày, 40 giờ/tuần.</p>
<h2>8. Đồ bảo hộ và giấc ngủ (bài 8)</h2>
<p>Đồ bảo hộ của tôi: ……………… · Giờ lên giường: …… · Giờ dậy: …… · Phút vận động tuần này: ……</p>
<h2>9. Chia lương (bài 9)</h2>
{table(['Phần', 'Số tiền'], [['Cố định', ''], ['Ăn uống', ''], ['Dự phòng', ''], ['Phần còn lại', '']])}
<h2>10. Hồ sơ kỹ năng và khi quá tải (bài 10)</h2>
{lines(['3 kỹ năng đạt bậc 3', '2 sản phẩm đã làm', 'Nhận xét của thầy', '3 dấu hiệu quá tải của tôi', 'Người 1', 'Người 2'])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">115</th><td>Cấp cứu y tế, tai nạn</td></tr>
<tr><th>114</th><td>Cháy nổ, cứu nạn</td></tr>
<tr><th>113</th><td>Công an, khi bị đe dọa, ép buộc</td></tr>
<tr><th>111</th><td>Bảo vệ trẻ em (dưới 18 tuổi), miễn phí, 24/7</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
</tbody></table></div>
<h2>Tự đánh giá (tuần 1 và tuần 10)</h2>
<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 10</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán hay đánh giá tay nghề chính thức.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Vững nghề', 'Khóa tự học miễn phí cho người học nghề: bậc thang kỹ năng, luyện tay nghề, an toàn lao động, làm đúng lần đầu, chính trực, giao tiếp, quyền cơ bản, sức khỏe, đồng lương đầu, hồ sơ kỹ năng.',
f'''
<p class="eyebrow">Cá nhân · Khóa C4 · Đang thử nghiệm</p>
<h1>Vững nghề</h1>
<p class="lead">Tay nghề vững cần ba thứ: luyện đúng cách, làm an toàn, và giữ chữ tín. Khóa này giúp bạn tự xây cả ba từ tuần đầu học nghề.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn tự luyện tay nghề có kế hoạch, làm việc an toàn, làm đúng chuẩn, giữ chính trực, giao tiếp tốt với thầy và chỗ làm, biết quyền cơ bản, giữ sức khỏe và tiền bạc</td></tr>
<tr><th>Dành cho</th><td>Người học nghề 15–24 tuổi: học viên trung cấp, cao đẳng, học việc tại xưởng, thực tập. Ví dụ lấy từ điện – cơ khí, may, bếp và sửa xe</td></tr>
<tr><th>Thời lượng</th><td>10 tuần, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, xem lại 5 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút, chương trình học nghề, một chỗ làm để thực hành (xưởng, bếp, tiệm)</td></tr>
<tr><th>Tình trạng</th><td>Đủ 10 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của thầy dạy nghề, cán bộ an toàn và học viên</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn hỏi 5 câu an toàn trước mỗi việc mới.</li><li>Bạn tự kiểm sản phẩm theo danh sách trước khi giao.</li><li>Bạn ghi nhật ký luyện và sửa từng lỗi cụ thể.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: tay nghề leo từng bậc, an toàn trước, chữ tín là vốn.</li><li>Kỹ năng: luyện có chủ đích, tự kiểm, báo cáo, quản lý lương.</li><li>Biết quyền cơ bản và biết nhờ giúp sớm.</li></ul></div>
</div>
{figure_block('KHOAE')}

<h2 id="muoi-tuan">Mười tuần</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ tay nghề của tôi</a>: bậc thang kỹ năng, nhật ký luyện, rà soát an toàn, tự kiểm, báo cáo, kiểm tra việc làm, chia lương, hồ sơ kỹ năng, tự đánh giá.</li>
<li><a href="{BTC}">Bảng thu chi</a>: ghi chi 7 ngày (dùng ở bài 9).</li></ul>

<h2>Cho thầy dạy nghề, người kèm cặp, gia đình</h2>
<ul>
<li>Dùng mỗi bài như một buổi sinh hoạt 25 phút đầu tuần, rồi để học viên áp dụng ở xưởng.</li>
<li>Khen học viên dừng lại hỏi, báo lỗi sớm, dùng đủ đồ bảo hộ.</li>
<li>Nhận xét cụ thể bằng số đo, thời gian, chuẩn. Nhận xét đó dùng được khi học viên xin việc.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{MAC}</td><td>Luyện có chủ đích, nhưng không chỉ đếm giờ</td><td><span class="label">[Đã xác nhận]</span> Tổng hợp 88 nghiên cứu; ở nghề nghiệp, luyện tập giải thích dưới 1% chênh lệch</td></tr>
<tr><td>{ILO}</td><td>An toàn cho người lao động trẻ</td><td><span class="label">[Đã xác nhận]</span> Người lao động trẻ bị tai nạn không chết người cao hơn tới 40%</td></tr>
<tr><td>{ATVS}; {LDCTN}; {D17}; {HN61}</td><td>Quyền dừng việc, quy định cho người dưới 18 tuổi, học nghề, giấy tờ</td><td><span class="label">[Đã xác nhận]</span> Văn bản pháp luật Việt Nam, đọc qua trang tóm tắt; nguyên văn một số điều [Cần kiểm chứng]</td></tr>
<tr><td>{LVL}</td><td>Chứng chỉ kỹ năng nghề quốc gia</td><td><span class="label">[Đã xác nhận]</span> Luật Việc làm 2025, hiệu lực 01/01/2026</td></tr>
<tr><td>{WHOH}; {AASMA}; {WHOPA}</td><td>Thính lực, ngủ, vận động</td><td><span class="label">[Đã xác nhận]</span> Khuyến nghị của WHO và đồng thuận chuyên gia</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Chúng tôi chưa tìm được thử nghiệm về một khóa tự học kỹ năng nghề như khóa này. Nhiều bài dựa trên cách làm phổ biến trong nghề và quản lý chất lượng, được ghi rõ là [Đánh giá chuyên môn].
  Khóa không thay thế thầy dạy nghề, huấn luyện an toàn lao động bắt buộc của chỗ làm, hay tư vấn pháp lý. Quyền lao động chuyên sâu sẽ có ở trang chị em trachnhiemxahoi.com.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C4 built')
