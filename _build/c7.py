# Khóa C7 "Tự lập từng bước" – trang khóa, 10 bài, công cụ "Sổ tự lập từng bước".
# Người đọc: người khuyết tật từ 15 tuổi (vận động, nhìn, nghe, trí tuệ – chậm phát triển) và người thân.
# Có người đọc dưới 18 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c7  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/tu-lap-tung-buoc/'
TOOL = '/cong-cu/so-tu-lap/'
RSN = '/cong-cu/phieu-ra-soat-nha/'
BTC = '/cong-cu/bang-thu-chi/'
C1 = '/khoa-hoc/lon-len-an-toan/'
C6 = '/khoa-hoc/tu-tin-an-toan/'
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
    return ('<p>0 = chưa · 1 = làm được khi có giúp · 2 = tự làm được. Có thể dùng hình: ☹ = 0, 😐 = 1, ☺ = 2.</p>'
            f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>{a}</th><th>{b}</th></tr></thead><tbody>{rows}</tbody></table></div>')
def adapt(van_dong, nhin, nghe, tri_tue):
    return table(['Nếu bạn…', 'Cách làm cho hợp'],
                 [['Khó đi lại, khó cử động tay', van_dong], ['Nhìn kém hoặc không nhìn thấy', nhin],
                  ['Nghe kém hoặc không nghe được', nghe], ['Học chậm, khó nhớ, khó hiểu chữ', tri_tue]])

# ---------- Nguồn (đã tra 03/11/2026) ----------
LUAT = '<a href="https://thuvienphapluat.vn/van-ban/Van-hoa-Xa-hoi/Luat-nguoi-khuyet-tat-2010-108081.aspx">Luật Người khuyết tật số 51/2010/QH12</a>'
D4 = '<a href="https://hethongphapluat.com/law-no-51-2010-qh12-of-june-17-2010-on-persons-with-disabilities/dieu-4">Luật Người khuyết tật 2010, Điều 4</a>'
D14 = '<a href="https://hethongphapluat.com/law-no-51-2010-qh12-of-june-17-2010-on-persons-with-disabilities/dieu-14">Luật Người khuyết tật 2010, Điều 14</a>'
D16 = '<a href="https://hethongphapluat.com/law-no-51-2010-qh12-of-june-17-2010-on-persons-with-disabilities/dieu-16">Luật Người khuyết tật 2010, Điều 16</a>'
NQ84 = '<a href="https://hethongphapluat.com/resolution-no-84-2014-qh13-dated-november-28-2014.html">Nghị quyết 84/2014/QH13 phê chuẩn Công ước về quyền của người khuyết tật</a>'
TCXH = '<a href="https://luatvietnam.vn/legal-updates/standard-social-assistance-level-of-up-to-vnd-500000-applied-from-july-1-2024-892-98399-article.html">Nghị định 76/2024/NĐ-CP sửa Nghị định 20/2021/NĐ-CP (LuatVietnam tóm tắt)</a>'
WHOD = '<a href="https://www.who.int/europe/news-room/fact-sheets/item/disability">WHO – Khuyết tật (10/8/2026)</a>'
WHOAT = '<a href="https://www.who.int/news-room/fact-sheets/detail/assistive-technology">WHO – Công nghệ hỗ trợ (2/1/2024)</a>'
WHOF = '<a href="https://www.who.int/news-room/fact-sheets/detail/falls">WHO – Té ngã (21/10/2026)</a>'
NCAEP = '<a href="https://autismpdc.fpg.unc.edu/ebps/">NCAEP 2020 – 28 phương pháp có bằng chứng (AFIRM, Đại học North Carolina)</a>'
HUGH = '<a href="https://pubmed.ncbi.nlm.nih.gov/22377290/">Hughes et al. 2012, <em>The Lancet</em></a>'
VDS = '<a href="https://www.nso.gov.vn/tin-tuc-thong-ke/2024/11/thong-cao-bao-chi-ve-ket-qua-dieu-tra-nguoi-khuyet-tat-nam-2023/">Điều tra người khuyết tật 2023 (Cục Thống kê, 2/11/2024)</a>'
ETR = '<a href="https://www.inclusion-europe.eu/easy-to-read-standards-guidelines/">Inclusion Europe – Information for all (tiêu chuẩn văn bản dễ đọc)</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'
T111 = '<a href="https://tongdai111.vn/">tongdai111.vn</a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài chưa được chuyên viên phục hồi chức năng, giáo viên giáo dục đặc biệt hay hội người khuyết tật duyệt. '
          'Khóa không thay thế phục hồi chức năng có người hướng dẫn. Phần luật chỉ là thông tin chung, không phải tư vấn pháp lý.</p></div>')
HOW = ('<p class="small">Mỗi bài có hai phần: <strong>phần dễ đọc</strong> cho bạn (câu ngắn, mỗi câu một ý), '
       'và <strong>phần cho người đồng hành</strong>. Bạn có thể nghe bài bằng trình đọc màn hình, hoặc nhờ người thân đọc to.</p>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Người từ 18 tuổi có thể góp ý cho bài ở trang '
           '<a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên thật, nơi ở hay chẩn đoán.</p>')
TALK = ('Nguy hiểm ngay: <strong>113</strong>. Té ngã, bị thương: <strong>115</strong>. Dưới 18 tuổi bị xâm hại, bạo lực: <strong>111</strong> (24/7). '
        'Bạo lực trong gia đình: <strong>117</strong> (24/7). Buồn, lo kéo dài: Ngày Mai <strong>096 306 1414</strong>.')
TEEN = 'Nếu bạn 15–17 tuổi: học cùng bố mẹ hoặc một người lớn bạn tin.'

L = {
 '1': (1, 'viec-minh-muon-tu-lam', 'Bài 1', 'Việc mình muốn tự làm'),
 '2': (2, 'chia-thanh-buoc-nho', 'Bài 2', 'Chia việc thành bước nhỏ'),
 '3': (3, 'giup-vua-du', 'Bài 3', 'Giúp vừa đủ, rồi giảm dần'),
 '4': (4, 'tu-cham-soc', 'Bài 4', 'Tự chăm sóc: ăn, mặc, vệ sinh'),
 '5': (5, 'an-toan-di-lai', 'Bài 5', 'An toàn trong nhà và khi đi lại'),
 '6': (6, 'noi-dieu-minh-can', 'Bài 6', 'Nói điều mình cần, nói "không"'),
 '7': (7, 'tien-va-di-cho', 'Bài 7', 'Tiền và đi chợ'),
 '8': (8, 'lich-hinh-anh', 'Bài 8', 'Lịch hình ảnh, giữ thói quen'),
 '9': (9, 'quyen-va-ho-tro', 'Bài 9', 'Quyền cơ bản và nơi tìm hỗ trợ'),
 '10': (10, 'buoc-tiep-theo', 'Bài 10', 'Xem lại, chọn bước tiếp theo'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn chọn 1 việc muốn tự làm và viết mục tiêu đo được.'),
 (2, 'Bạn chia việc đó thành 4–8 bước, mỗi bước một động từ.'),
 (3, 'Bạn và người thân ghi mức hỗ trợ cho từng bước, 5 lần tập.'),
 (4, 'Bạn tập 1 việc tự chăm sóc 7 ngày, có ghi lại.'),
 (5, 'Bạn rà soát nhà, sửa 1 chỗ nguy cơ té ngã, có thẻ thông tin khi đi.'),
 (6, 'Bạn có 3 câu nhờ giúp và nói thật 1 lần.'),
 (7, 'Bạn đi chợ 1 lần có danh sách, đếm tiền, kiểm tiền thừa.'),
 (8, 'Bạn dùng lịch hình ảnh buổi sáng 7 ngày.'),
 (9, 'Bạn biết 4 quyền cơ bản và có phiếu hỏi hỗ trợ đã điền.'),
 (10, 'Bạn so mức hỗ trợ trước – sau và chọn việc tiếp theo.'),
]

def lesson(k, desc, goals, prep, read, do, together, adapt_tbl, safety, selfq, adult, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Bài {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Làm cùng người thân 5 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (5 phút)', ul(prep)),
        sec(3, 'Đọc – phần dễ đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Làm cùng người thân (5 phút)', together),
        sec(6, 'Làm cho hợp với mình', adapt_tbl),
        sec(7, 'An toàn', ul(safety + [TEEN, TALK])),
        sec(8, 'Tự đánh giá', selftab(selfq)),
        sec(9, 'Cho người đồng hành: người thân, người chăm sóc, thầy cô', ul(adult)),
        sec(10, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Tự lập từng bước</a> · Bài {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{HOW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('J' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
SUPPORT = 'C = cầm tay làm cùng · M = làm mẫu · H = chỉ tay, đưa hình · L = nhắc bằng lời · T = tự làm'

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Tự lập từng bước, bài 1: chọn một việc muốn tự làm, vừa sức, làm hằng ngày; viết mục tiêu đo được.',
 ['Nói hoặc viết <strong>3 việc</strong> bạn muốn tự làm.',
  'Chọn <strong>1 việc</strong> để tập trong 4 tuần tới.',
  'Viết <strong>1 mục tiêu đo được</strong> cùng người thân.'],
 [f'In trang 1 của <a href="{TOOL}">Sổ tự lập từng bước</a>, hoặc lấy một tờ giấy.', 'Một người thân ngồi cùng 5 phút cuối.'],
 ['<strong>Tự lập</strong> là được tự chọn và tự làm việc của mình.',
  'Tự lập <strong>không có nghĩa</strong> là làm mọi thứ một mình. Ai cũng cần giúp ở một vài việc.',
  'Bạn là người <strong>chọn</strong> việc muốn tập. Người thân giúp, nhưng không chọn thay bạn.',
  'Chọn việc <strong>quan trọng với bạn</strong>. Ví dụ: tự mặc áo, tự pha nước, tự đi tới chợ gần nhà.',
  'Chọn việc <strong>làm hằng ngày</strong>. Làm nhiều lần thì nhanh quen.',
  'Chọn việc <strong>hơi khó, chưa quá khó</strong>. Quá dễ thì không tiến, quá khó thì dễ nản.',
  '<strong>Mục tiêu đo được</strong> nói rõ: làm gì, tới khi nào, cần giúp bao nhiêu.',
  'Ví dụ: "Sau 4 tuần, mình tự pha mì gói, chỉ cần nhắc 1 lần."'],
 '<p><strong>Bài 1: ba việc tôi muốn tự làm.</strong> Viết, vẽ, hoặc nói để người thân ghi giúp.</p>'
 + table(['Việc', 'Quan trọng với tôi? (có/không)', 'Làm hằng ngày? (có/không)', 'Hơi khó, chưa quá khó? (có/không)'],
         [['1.', '', '', ''], ['2.', '', '', ''], ['3.', '', '', '']])
 + '<p><strong>Bài 2: chọn 1 việc</strong> có nhiều chữ "có" nhất.</p>'
 + lines(['Việc tôi chọn', 'Mục tiêu: sau … tuần, tôi …, cần giúp …']),
 ol(['Đọc mục tiêu cho người thân nghe, hoặc đưa họ xem.', 'Hỏi: "Mục tiêu này có rõ không? Lúc nào thì mình biết đã đạt?"',
     'Hai người cùng ký hoặc đánh dấu vào mục tiêu.']),
 adapt('Chọn việc theo sức tay, sức chân hiện tại. Có thể chọn "tự điều khiển" việc: bạn nói, người khác làm theo ý bạn.',
       'Nói mục tiêu để người thân ghi, hoặc ghi âm. Dùng trình đọc màn hình để nghe bài.',
       'Đọc bài, viết ra giấy để trao đổi. Người thân nói chậm, quay mặt về phía bạn.',
       'Chỉ chọn trong 2–3 việc có hình. Mục tiêu một câu ngắn, có hình minh họa.'),
 ['Không chọn việc có lửa, dao, điện, nước nóng ở bài đầu, trừ khi chuyên viên phục hồi chức năng đồng ý.',
  'Nếu có bệnh tim, động kinh, chóng mặt: hỏi bác sĩ trước khi tập việc cần sức.'],
 ['Tôi nói được 3 việc muốn tự làm', 'Tôi chọn được 1 việc', 'Tôi có 1 mục tiêu đo được'],
 ['Hỏi "Bạn muốn tự làm việc gì?" rồi chờ. Không chọn thay.', 'Nếu việc bạn ấy chọn có rủi ro, cùng bàn cách làm an toàn hơn, đừng cấm ngay.',
  'Viết mục tiêu theo lời của bạn ấy, không theo lời bạn.'],
 [lb('Đã xác nhận', f'Người khuyết tật có quyền sống độc lập và hòa nhập cộng đồng ({D4}).'),
  lb('Đã xác nhận', f'Ở Việt Nam, khoảng 6,11% người từ 2 tuổi trở lên có khuyết tật; tỷ lệ tham gia lao động là 23,9% so với 77,4% ở người không khuyết tật ({VDS}).'),
  lb('Đánh giá chuyên môn', 'Ba tiêu chí chọn việc và cách viết mục tiêu đo được do daynentang.com soạn, theo cách làm phổ biến trong phục hồi chức năng.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Tự lập từng bước, bài 2: chia một việc thành 4–8 bước nhỏ; mỗi bước một động từ; cách tập từ bước cuối.',
 ['Chia việc đã chọn thành <strong>4–8 bước</strong>.',
  'Mỗi bước có <strong>1 động từ</strong> và nhìn thấy được.',
  'Thử làm theo danh sách <strong>1 lần</strong> cùng người thân.'],
 [f'In trang 2 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Đồ dùng thật của việc đã chọn ở bài 1.'],
 ['Một việc lớn gồm <strong>nhiều bước nhỏ</strong>.',
  'Ví dụ rửa tay: mở nước, xoa xà phòng, chà tay, xả sạch, lau khô.',
  'Mỗi bước bắt đầu bằng <strong>một động từ</strong>: mở, lấy, đặt, cài, kéo.',
  'Bước phải <strong>nhìn thấy được</strong>. "Chuẩn bị" thì chưa rõ. "Lấy cốc ra bàn" thì rõ.',
  'Bước nào khó, <strong>chia nhỏ thêm</strong>.',
  'Một cách tập: người thân làm các bước đầu, <strong>bạn làm bước cuối</strong>. Rồi bạn làm thêm bước trước đó.',
  'Cách này giúp bạn <strong>lần nào cũng tự làm xong</strong> việc.',
  'Có thể <strong>chụp ảnh hoặc vẽ</strong> từng bước, dán ở chỗ làm việc đó.'],
 '<p><strong>Bài 1: danh sách bước.</strong> Cùng người thân làm thật việc đó thật chậm, ghi từng bước.</p>'
 + table(['Bước', 'Động từ + việc (ví dụ: "Lấy cốc ra bàn")', 'Hình hoặc ghi chú'], [[str(n), '', ''] for n in range(1, 9)])
 + '<p><strong>Bài 2: kiểm danh sách.</strong> Đánh dấu ✓ nếu đúng.</p>'
 + ul(['Mỗi bước có một động từ.', 'Người khác đọc là làm theo được.', 'Không thiếu bước nào khi làm thật.']),
 ol(['Bạn đọc từng bước, người thân làm đúng theo chữ, không làm thêm.', 'Chỗ nào người thân làm sai, sửa lại câu cho rõ.',
     'Chọn: tập từ bước đầu hay từ bước cuối.']),
 adapt('Ghi rõ tư thế, chỗ để đồ cho vừa tầm tay. Bước nào cần đồ hỗ trợ thì ghi vào cột ghi chú.',
       'Dùng danh sách nói (ghi âm từng bước). Đồ luôn để đúng một chỗ cố định.',
       'Dùng hình hoặc chữ cho từng bước. Người thân làm mẫu, không chỉ giải thích bằng lời.',
       'Dùng ảnh thật của đồ dùng nhà mình. Ít bước trước (3–4), thêm dần sau.'),
 ['Bước có nước nóng, dao, điện: ghi chữ "CẦN NGƯỜI LỚN" và tập cùng người thân tới khi an toàn.'],
 ['Tôi chia việc thành 4–8 bước', 'Mỗi bước có 1 động từ', 'Tôi làm theo danh sách 1 lần'],
 ['Làm thật việc đó trước, chậm, để không bỏ sót bước.', 'Dùng đúng lời và đồ dùng nhà mình, không dùng mẫu chung.',
  'Nếu chọn tập từ bước cuối: bạn làm các bước đầu, để bạn ấy làm bước cuối và tự hoàn thành.'],
 [lb('Đã xác nhận', f'Phân tích nhiệm vụ (chia việc thành bước nhỏ) có trong danh sách 28 phương pháp có bằng chứng của {NCAEP}.'),
  lb('Suy luận', 'Danh sách trên dựa vào nghiên cứu ở người tự kỷ. Cách chia bước cũng được dùng rộng rãi với người khuyết tật trí tuệ, nhưng bài chưa đọc tổng quan riêng.'),
  lb('Đánh giá chuyên môn', 'Ví dụ rửa tay 5 bước và mẫu danh sách do daynentang.com soạn.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Tự lập từng bước, bài 3: năm mức hỗ trợ, chờ trước khi giúp, giảm dần hỗ trợ, khen việc tự làm.',
 ['Nói được <strong>5 mức hỗ trợ</strong>, từ nhiều tới ít.',
  'Ghi mức hỗ trợ cho từng bước trong <strong>5 lần tập</strong>.',
  'Cùng người thân chọn <strong>1 bước</strong> để giảm hỗ trợ tuần này.'],
 [f'In trang 3 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Danh sách bước ở bài 2.'],
 ['Có <strong>5 mức hỗ trợ</strong>. Từ nhiều tới ít:',
  '<strong>C</strong> – cầm tay làm cùng. <strong>M</strong> – làm mẫu cho xem. <strong>H</strong> – chỉ tay hoặc đưa hình. <strong>L</strong> – nhắc bằng lời. <strong>T</strong> – tự làm.',
  'Chọn mức <strong>ít nhất</strong> mà bạn vẫn làm được.',
  'Người thân <strong>đợi vài giây</strong> trước khi nhắc. Khoảng chờ cho bạn cơ hội tự làm.',
  'Khi bạn làm được ở một mức nhiều lần, <strong>lùi xuống mức ít hơn</strong>.',
  'Giúp quá nhiều làm bạn khó tự lập. Giúp quá ít làm bạn nản. Cần <strong>vừa đủ</strong>.',
  'Khi bạn tự làm một bước, người thân <strong>khen đúng việc đó</strong>: "Bạn tự cài được nút rồi."',
  'Bạn được nói: "<strong>Để mình thử trước</strong>."'],
 f'<p><strong>Bài 1: ghi mức hỗ trợ.</strong> {SUPPORT}.</p>'
 + table(['Bước', 'Lần 1', 'Lần 2', 'Lần 3', 'Lần 4', 'Lần 5'], [[str(n), '', '', '', '', ''] for n in range(1, 7)])
 + '<p><strong>Bài 2: chọn bước để giảm hỗ trợ.</strong> Bước nào đã làm được 3 lần liên tiếp ở cùng một mức?</p>'
 + lines(['Bước tôi chọn', 'Mức cũ → mức mới']),
 ol(['Tập một lần, người thân ghi mức hỗ trợ.', 'Bạn nói: "Lần sau, bạn đợi mình … giây rồi mới nhắc."',
     'Hai người thống nhất một câu khen ngắn.']),
 adapt('Cầm tay chỉ khi bạn đồng ý. Có thể thay bằng đồ hỗ trợ (bài 4) để giảm phần người khác làm.',
       'Thay "chỉ tay, đưa hình" bằng chạm nhẹ vào đồ vật hoặc nói vị trí: "cốc ở bên phải tay bạn".',
       'Thay "nhắc bằng lời" bằng cử chỉ, thẻ chữ hoặc thẻ hình đã thống nhất.',
       'Giảm hỗ trợ chậm, mỗi lần một bước. Giữ cùng một người tập trong 1–2 tuần đầu nếu được.'),
 ['Giảm hỗ trợ ở bước an toàn trước. Bước có nguy cơ (nước nóng, cầu thang) giảm chậm hơn.',
  'Cầm tay, chạm người: luôn hỏi trước, dừng ngay khi bạn nói dừng.'],
 ['Tôi nói được 5 mức hỗ trợ', 'Tôi ghi mức hỗ trợ 5 lần tập', 'Tôi giảm hỗ trợ ở 1 bước'],
 ['Đếm thầm vài giây trước khi nhắc. Phần lớn người giúp nhắc quá sớm.', 'Khen việc tự làm, không khen chung chung.',
  'Ghi lại mức hỗ trợ thật, không ghi cao hơn để vui lòng nhau.'],
 [lb('Đã xác nhận', f'Gợi ý theo mức (prompting), chờ trước khi gợi ý (time delay) và củng cố (reinforcement) đều có trong {NCAEP}.'),
  lb('Suy luận', 'Năm mức C – M – H – L – T là cách sắp xếp gợi ý thường gặp; bằng chứng gốc chủ yếu ở người tự kỷ.'),
  lb('Cần kiểm chứng', 'Nên đợi bao nhiêu giây trước khi nhắc: tùy người, chưa có con số chung. Bài để người thân và bạn tự thống nhất.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Tự lập từng bước, bài 4: tập một việc tự chăm sóc trong 7 ngày; đồ hỗ trợ đơn giản; an toàn khi tắm và uống thuốc.',
 ['Chọn <strong>1 việc tự chăm sóc</strong>: ăn, mặc, vệ sinh, tắm, thuốc hoặc ngủ.',
  'Tập việc đó <strong>7 ngày</strong>, có ghi lại.',
  'Nói được <strong>2 đồ hỗ trợ</strong> có thể giúp việc đó dễ hơn.'],
 [f'In trang 4 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Danh sách bước (bài 2) và bảng mức hỗ trợ (bài 3).'],
 ['<strong>Tự chăm sóc</strong> là ăn, uống, mặc đồ, vệ sinh, tắm, uống thuốc, ngủ.',
  'Mỗi lần chỉ tập <strong>một việc</strong>. Tập cùng giờ mỗi ngày.',
  '<strong>Đổi đồ vật</strong> thường dễ hơn đổi cách làm. Ví dụ: áo cài dán thay nút nhỏ.',
  'Đồ hỗ trợ đơn giản: thìa cán to, cốc có quai, quần lưng thun, ghế tắm, tay vịn, hộp thuốc chia ngày.',
  'Hỏi <strong>chuyên viên phục hồi chức năng</strong> trước khi mua đồ đắt tiền như xe lăn, máy trợ thính.',
  '<strong>Tắm:</strong> thử nước trước khi dùng. Bạn chưa cảm nhận rõ nóng lạnh thì nhờ người thân thử.',
  '<strong>Thuốc:</strong> uống đúng thuốc, đúng liều, đúng giờ bác sĩ dặn. Không tự đổi.',
  '<strong>Riêng tư:</strong> khi tắm, vệ sinh, bạn được đóng cửa, được chọn người giúp.'],
 '<p><strong>Bài 1: việc tôi tập.</strong></p>' + lines(['Việc tự chăm sóc tôi chọn', 'Giờ tập mỗi ngày', 'Đồ hỗ trợ có thể dùng'])
 + f'<p><strong>Bài 2: theo dõi 7 ngày.</strong> Ghi mức hỗ trợ thấp nhất hôm đó ({SUPPORT}).</p>'
 + table(['Ngày'] + DAYS, [['Mức hỗ trợ'] + [''] * 7, ['Thấy thế nào? ☹ 😐 ☺'] + [''] * 7]),
 ol(['Người thân xem bảng 7 ngày cùng bạn.', 'Hỏi nhau: "Ngày nào dễ nhất? Vì sao?"', 'Chọn 1 thay đổi nhỏ cho tuần sau: đổi giờ, đổi chỗ để đồ, thêm 1 đồ hỗ trợ.']),
 adapt('Ngồi khi mặc quần, tắm. Để đồ ở tầm tay. Hỏi về ghế tắm, tay vịn, đồ cán to.',
       'Mỗi thứ một chỗ cố định. Đánh dấu hộp thuốc bằng chạm (dán nút nhựa, dây thun) theo cách bác sĩ hoặc dược sĩ đồng ý.',
       'Dùng chuông báo rung hoặc đèn nháy để nhớ giờ thuốc. Viết sẵn câu hỏi khi đi khám.',
       'Dùng ảnh từng bước dán ở nhà tắm. Hộp thuốc chia ngày do người thân chuẩn bị, bạn tự lấy đúng ô.'),
 ['Nhà tắm dễ trơn: dùng thảm chống trơn, có tay vịn nếu được.', 'Thử nhiệt độ nước trước khi tắm hoặc rửa.',
  'Không tự đổi liều thuốc. Uống nhầm thuốc: gọi 115 hoặc tới cơ sở y tế gần nhất.'],
 ['Tôi chọn 1 việc tự chăm sóc', 'Tôi tập và ghi lại 7 ngày', 'Tôi nói được 2 đồ hỗ trợ'],
 ['Giữ riêng tư: hỏi trước khi vào nhà tắm, che phần cơ thể không cần thấy.', 'Chuẩn bị đồ sẵn ở tầm tay bạn ấy, rồi lùi ra.',
  'Thuốc: người thân giữ đơn thuốc gốc, cùng bạn ấy chia hộp mỗi tuần.'],
 [lb('Đã xác nhận', f'Trên thế giới hơn 2,5 tỷ người cần ít nhất một đồ hỗ trợ; ở một số nước thu nhập thấp, chỉ khoảng 3% có được ({WHOAT}).'),
  lb('Đã xác nhận', f'Người khuyết tật có quyền dùng dịch vụ y tế, phục hồi chức năng phù hợp dạng và mức độ khuyết tật ({D4}).'),
  lb('Đánh giá chuyên môn', 'Danh sách đồ hỗ trợ đơn giản và bảng 7 ngày do daynentang.com soạn; cần chuyên viên phục hồi chức năng duyệt.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Tự lập từng bước, bài 5: rà soát nhà để giảm té ngã, thẻ thông tin khi đi, thói quen Trước – Trong – Sau.',
 ['Rà soát nhà theo <strong>4 chỗ</strong>: lối đi, ánh sáng, nhà tắm, tay vịn.',
  'Sửa <strong>1 chỗ</strong> có nguy cơ té ngã.',
  'Làm <strong>1 thẻ thông tin</strong> mang theo khi đi.'],
 [f'In trang 5 của <a href="{TOOL}">Sổ tự lập từng bước</a>. Có thể dùng thêm <a href="{RSN}">Phiếu rà soát nhà</a>.', 'Một người thân đi cùng khi rà soát.'],
 ['<strong>Té ngã</strong> là nguyên nhân tử vong do tai nạn đứng thứ hai trên thế giới, sau tai nạn giao thông.',
  'Xem <strong>4 chỗ</strong> trong nhà: lối đi có đồ vướng không; đủ sáng không; nhà tắm trơn không; chỗ cần có tay vịn không.',
  'Mỗi tuần <strong>sửa 1 chỗ</strong>. Ví dụ: dọn dây điện khỏi lối đi, thêm đèn ngủ.',
  '<strong>Đi một mình:</strong> tập đường ngắn, có người đi cùng vài lần trước.',
  '<strong>Trước khi đi:</strong> báo nơi đến, giờ về.',
  '<strong>Trong lúc đi:</strong> mang thẻ thông tin: tên, số người thân, điều người giúp cần biết.',
  '<strong>Tới nơi:</strong> nhắn hoặc gọi "đã tới".',
  'Lạc đường: đứng lại, tìm người bán hàng, bảo vệ, công an, đưa thẻ thông tin.'],
 '<p><strong>Bài 1: rà soát nhà.</strong></p>'
 + table(['Chỗ', 'Có nguy cơ? (có/không)', 'Sửa thế nào', 'Sửa xong ✓'],
         [['Lối đi', '', '', ''], ['Ánh sáng, nhất là ban đêm', '', '', ''], ['Nhà tắm', '', '', ''], ['Tay vịn, cầu thang', '', '', '']])
 + '<p><strong>Bài 2: thẻ thông tin.</strong> Viết tay hoặc nhờ người thân viết. Cất trong ví hoặc túi.</p>'
 + lines(['Tên gọi', 'Số người thân 1', 'Số người thân 2', 'Điều người giúp cần biết (ví dụ: "tôi không nghe được, xin viết ra giấy")']),
 ol(['Cùng đi một đoạn đường ngắn quen thuộc.', 'Lần sau, người thân đi sau một quãng, bạn đi trước.', 'Thống nhất: nếu không nhắn "đã tới" sau bao lâu thì người thân gọi.']),
 adapt('Lối đi đủ rộng cho xe lăn hoặc khung tập đi. Phanh xe lăn khi dừng. Hỏi chuyên viên về bài tập thăng bằng hợp sức.',
       'Giữ đồ đạc cố định, đóng hẳn cửa tủ, không để cửa mở hé. Học đi bằng gậy trắng với người hướng dẫn.',
       'Thẻ ghi rõ cách giao tiếp với bạn. Chú ý xe từ phía sau: nhìn gương, đi sát lề.',
       'Tập một đường cố định, có ảnh các mốc. Thẻ thông tin có ảnh người thân và số gọi.'),
 ['Không đổi thuốc hay tự bỏ thuốc gây chóng mặt; hỏi bác sĩ nếu hay chóng mặt khi đứng dậy.',
  'Té ngã, đau nhiều, không đứng dậy được: không cố đứng, gọi người giúp hoặc 115.',
  'Thẻ thông tin không ghi số giấy tờ tùy thân hay địa chỉ nhà chi tiết.'],
 ['Tôi rà soát 4 chỗ trong nhà', 'Tôi sửa 1 chỗ có nguy cơ', 'Tôi có thẻ thông tin khi đi'],
 ['Rà soát theo tầm nhìn và tầm tay của bạn ấy, không theo của bạn.', 'Đi sau một quãng thay vì đi cạnh, khi bạn ấy đã quen đường.',
  'Hỏi trước khi đổi chỗ đồ đạc trong phòng bạn ấy.'],
 [lb('Đã xác nhận', f'Năm 2023 có khoảng 842.000 người chết do té ngã; té ngã đứng thứ hai trong tử vong do tai nạn, sau giao thông ({WHOF}).'),
  lb('Đã xác nhận', f'Với người cao tuổi có nguy cơ cao, rà soát và sửa nhà giảm té ngã khoảng 38%; với người không chọn lọc thì chưa thấy lợi ích ({WHOF}).'),
  lb('Suy luận', 'Bằng chứng sửa nhà chủ yếu ở người cao tuổi; áp dụng cho người khuyết tật trẻ hơn là suy luận.'),
  lb('Đánh giá chuyên môn', 'Thẻ thông tin và thói quen Trước – Trong – Sau do daynentang.com soạn.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Tự lập từng bước, bài 6: câu nhờ giúp ba phần, nói "không", nhận ra người giúp tốt và dấu hiệu bị lợi dụng.',
 ['Viết hoặc chọn <strong>3 câu nhờ giúp</strong>.',
  'Nói được <strong>3 dấu hiệu</strong> người giúp tốt và <strong>3 dấu hiệu</strong> cần cảnh giác.',
  'Có <strong>2 người tin cậy</strong> để kể khi có chuyện.'],
 [f'In trang 6 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Bút, hoặc thẻ hình để chỉ.'],
 ['Bạn được <strong>nhờ giúp</strong>. Nhờ giúp là một kỹ năng, không phải điều đáng xấu hổ.',
  '<strong>Câu nhờ giúp ba phần:</strong> "Mình cần… Vì… Bạn giúp bằng cách…"',
  'Ví dụ: "Mình cần qua đường. Vì mình nhìn kém. Bạn cho mình nắm khuỷu tay nhé."',
  'Bạn được <strong>nói "không"</strong>, kể cả với người thân, người giúp.',
  '<strong>Người giúp tốt:</strong> hỏi trước khi chạm; giúp đúng việc bạn nhờ; dừng khi bạn nói dừng.',
  '<strong>Cần cảnh giác:</strong> chạm khi bạn không muốn; giữ tiền, giấy tờ của bạn; bắt giữ bí mật; dọa bỏ mặc bạn.',
  'Người khuyết tật dễ bị bạo lực hơn người khác. <strong>Đó không phải lỗi của bạn.</strong>',
  'Có chuyện sai: nói "không", rời đi nếu được, <strong>kể với người tin cậy</strong>.'],
 '<p><strong>Bài 1: ba câu nhờ giúp.</strong></p>'
 + table(['Tình huống (giả định)', 'Mình cần…', 'Vì…', 'Bạn giúp bằng cách…'],
         [['Ở chợ, cần lấy đồ trên cao', '', '', ''], ['Ở trạm y tế, không hiểu lời dặn', '', '', ''], ['Bạn tự chọn', '', '', '']])
 + '<p><strong>Bài 2: người tin cậy.</strong></p>' + lines(['Người tin cậy 1 (số gọi)', 'Người tin cậy 2 (số gọi)', 'Câu "không" của tôi']),
 ol(['Người thân đóng vai người ở chợ. Bạn nói câu nhờ giúp.', 'Đổi vai: người thân nhờ giúp, bạn nói "không" một cách lịch sự.',
     'Người thân hứa: "Bạn kể gì mình cũng nghe, không mắng."']),
 adapt('Nói rõ cách giúp: đẩy xe lăn ra sao, đỡ chỗ nào. Bạn được từ chối người đẩy xe mà không hỏi.',
       'Nói người giúp cách dẫn đường: bạn nắm khuỷu tay họ, họ đi trước nửa bước.',
       'Viết sẵn câu nhờ giúp vào điện thoại hoặc thẻ. Dùng ngôn ngữ ký hiệu nếu người nghe biết.',
       'Dùng thẻ hình: "giúp", "không", "dừng". Tập đóng vai nhiều lần với cùng một tình huống.'),
 ['Bị đánh, bị chạm vào vùng kín, bị giữ tiền: đó là bạo lực. Kể với người tin cậy, gọi 113 nếu nguy hiểm.',
  'Nếu người làm hại là người chăm sóc: vẫn kể với người tin cậy khác. Bạn không phải giữ bí mật.'],
 ['Tôi có 3 câu nhờ giúp', 'Tôi phân biệt người giúp tốt và dấu hiệu cảnh giác', 'Tôi có 2 người tin cậy'],
 ['Tôn trọng câu "không" của bạn ấy, kể cả khi bạn đang muốn giúp.', 'Hỏi định kỳ, riêng tư: "Có ai làm bạn khó chịu không?"',
  f'Bạn 15–17 tuổi: xem thêm khóa <a href="{C1}">Lớn lên an toàn</a>; bạn nữ: khóa <a href="{C6}">Tự tin – an toàn</a>.'],
 [lb('Đã xác nhận', f'Tổng quan 26 nghiên cứu, 21.557 người khuyết tật: nguy cơ bị bạo lực cao hơn người không khuyết tật (OR 1,50); với khuyết tật trí tuệ OR 1,60 ({HUGH}). Đây là số liệu quan sát, cho thấy tương quan.'),
  lb('Đã xác nhận', f'Luật cấm xâm phạm thân thể, nhân phẩm, tài sản của người khuyết tật; cấm lợi dụng họ để trục lợi; cấm người chăm sóc bỏ mặc ({D14}).'),
  lb('Đánh giá chuyên môn', 'Câu nhờ giúp ba phần và các dấu hiệu cảnh giác do daynentang.com soạn.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Tự lập từng bước, bài 7: đi chợ có danh sách, đếm tiền, kiểm tiền thừa, giữ mã PIN và OTP, ghi thu chi.',
 ['Đi chợ <strong>1 lần</strong> có danh sách.',
  'Đếm tiền trước khi đi và <strong>kiểm tiền thừa</strong> trước khi rời quầy.',
  'Nói được <strong>3 thói quen</strong> giữ tiền an toàn.'],
 [f'In trang 7 của <a href="{TOOL}">Sổ tự lập từng bước</a>. Có thể dùng thêm <a href="{BTC}">Bảng thu chi</a>.', 'Một ít tiền thật, túi đựng.'],
 ['<strong>Danh sách:</strong> viết, vẽ hoặc dán hình đồ cần mua. Chỉ mua đồ trong danh sách.',
  '<strong>Đếm tiền</strong> trước khi đi. Ghi số tiền mang theo.',
  'Đưa tiền <strong>mệnh giá lớn hơn giá</strong> nếu chưa quen tính. Rồi kiểm tiền thừa.',
  '<strong>Kiểm tiền thừa</strong> trước khi rời quầy. Không chắc thì hỏi lại.',
  '<strong>Mã PIN, mã OTP:</strong> chỉ mình bạn biết. Ngân hàng không bao giờ gọi xin mã.',
  'Ai đòi <strong>giữ thẻ, giữ tiền</strong> của bạn: hỏi người tin cậy trước.',
  'Tiền trợ cấp, tiền lương là <strong>tiền của bạn</strong>. Bạn được biết mình có bao nhiêu.',
  'Ghi <strong>tiền vào, tiền ra</strong> mỗi tuần.'],
 '<p><strong>Bài 1: danh sách đi chợ.</strong></p>'
 + table(['Đồ cần mua', 'Giá dự tính', 'Đã mua ✓', 'Giá thật'], [['', '', '', ''] for _ in range(5)])
 + lines(['Tiền mang theo', 'Tiền còn lại sau khi về', 'Khớp không? (có/không)']),
 ol(['Người thân đi cùng lần đầu, đứng xa một chút.', 'Về nhà, cùng đếm tiền còn lại.', 'Ghi vào bảng thu chi tuần.']),
 adapt('Chọn chỗ mua có lối vào dễ, hoặc nhờ người bán mang đồ ra. Dùng túi đeo chéo để rảnh tay.',
       'Xếp tiền theo mệnh giá vào các ngăn ví khác nhau. Gấp tiền theo cách riêng để nhận ra.',
       'Viết danh sách để đưa người bán. Xem số tiền trên máy tính tiền hoặc nhờ ghi ra giấy.',
       'Danh sách bằng hình. Mang đúng số tiền cho một món trước, rồi tăng dần.'),
 ['Không cho ai biết mã PIN, OTP, kể cả người tự xưng là ngân hàng, công an.', 'Đi chợ ban ngày, chỗ đông người khi mới tập.',
  'Bị lừa, mất tiền: kể với người tin cậy, báo ngân hàng và công an.'],
 ['Tôi đi chợ có danh sách', 'Tôi đếm tiền và kiểm tiền thừa', 'Tôi nói được 3 thói quen giữ tiền'],
 ['Để bạn ấy tự trả tiền, kể cả khi chậm. Đứng xa, không trả thay.', 'Nếu bạn quản lý tiền giúp, cho bạn ấy xem sổ mỗi tháng.',
  'Không mượn tiền trợ cấp của bạn ấy mà không hỏi.'],
 [lb('Đã xác nhận', f'Luật cấm lợi dụng người khuyết tật để trục lợi và cấm xâm phạm tài sản của họ ({D14}).'),
  lb('Đánh giá chuyên môn', 'Mẫu danh sách đi chợ và cách tập theo số tiền tăng dần do daynentang.com soạn.'),
  lb('Cần kiểm chứng', 'Hiệu quả của khóa tự học về tiền cho người khuyết tật trí tuệ: chưa tìm được nghiên cứu.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Tự lập từng bước, bài 8: lịch hình ảnh buổi sáng, gắn việc mới sau việc đã quen, giữ thói quen 7 ngày.',
 ['Làm <strong>1 lịch buổi sáng</strong> có 4–6 việc.',
  'Dùng lịch <strong>7 ngày</strong> và đánh dấu việc đã xong.',
  'Viết <strong>1 câu "Sau khi… thì mình…"</strong>.'],
 [f'In trang 8 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Bút màu, hoặc ảnh chụp đồ dùng thật.'],
 ['<strong>Lịch hình ảnh</strong> là dãy ô, mỗi ô một việc, theo thứ tự.',
  'Nhìn lịch là biết <strong>việc tiếp theo</strong>. Không cần ai nhắc.',
  'Mỗi ô có <strong>hình hoặc chữ</strong>, tùy cách bạn dễ hiểu.',
  'Làm xong việc nào, <strong>đánh dấu</strong> việc đó.',
  'Dán lịch ở <strong>chỗ dễ thấy</strong>: cửa phòng, gương, cạnh giường.',
  'Thói quen mới dễ giữ hơn khi <strong>gắn sau việc đã quen</strong>.',
  'Ví dụ: "Sau khi đánh răng, thì mình uống thuốc."',
  '<strong>Quên một ngày không sao.</strong> Hôm sau làm tiếp.'],
 '<p><strong>Bài 1: lịch buổi sáng.</strong> Viết hoặc vẽ mỗi ô một việc.</p>'
 + table(['Thứ tự', '1', '2', '3', '4', '5', '6'], [['Việc'] + [''] * 6])
 + '<p><strong>Bài 2: theo dõi 7 ngày.</strong> Đánh dấu ✓ khi làm đủ lịch.</p>'
 + table(['Ngày'] + DAYS, [['Đủ lịch ✓'] + [''] * 7])
 + lines(['Sau khi …, thì mình …']),
 ol(['Cùng người thân dán lịch ở chỗ đã chọn.', 'Sáng hôm sau, người thân không nhắc, chỉ chỉ vào lịch nếu cần.', 'Cuối tuần, đếm số ngày đủ lịch.']),
 adapt('Dán lịch ở tầm mắt khi ngồi xe lăn. Chọn việc có thể làm ở cùng một chỗ.',
       'Dùng lịch chạm: mỗi ô gắn một đồ vật nhỏ, an toàn. Hoặc lịch nói ghi âm theo thứ tự.',
       'Lịch hình là cách hợp nhất. Thêm chuông rung báo giờ.',
       'Bắt đầu với 3 ô có ảnh thật. Thêm ô khi đã làm đủ 3 ô trong 7 ngày.'),
 ['Ô uống thuốc: chỉ ghi "uống thuốc", không ghi liều; liều theo đơn bác sĩ.', 'Đồ vật trên lịch chạm không để vật nhỏ nếu nhà có trẻ dưới 3 tuổi.'],
 ['Tôi làm lịch buổi sáng', 'Tôi dùng lịch 7 ngày', 'Tôi có 1 câu "Sau khi… thì mình…"'],
 ['Chỉ vào lịch thay vì nhắc bằng lời.', 'Khen số ngày làm được, không nhắc ngày quên.', 'Đổi lịch khi bạn ấy muốn đổi thứ tự.'],
 [lb('Đã xác nhận', f'Hỗ trợ bằng hình ảnh (visual supports) và tự quản lý (self-management) có trong {NCAEP}.'),
  lb('Suy luận', 'Bằng chứng gốc ở người tự kỷ; áp dụng cho người khuyết tật trí tuệ và người khó nhớ là suy luận.'),
  lb('Đánh giá chuyên môn', 'Câu "Sau khi… thì mình…" và lịch chạm do daynentang.com soạn.')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Tự lập từng bước, bài 9: một số quyền trong Luật Người khuyết tật 2010, xác định mức độ khuyết tật ở xã, chuẩn bị đi hỏi hỗ trợ.',
 ['Nói được <strong>4 quyền</strong> của người khuyết tật.',
  'Biết nơi bắt đầu hỏi hỗ trợ: <strong>Ủy ban nhân dân xã, phường</strong> nơi mình ở.',
  'Điền <strong>phiếu hỏi hỗ trợ</strong> trước khi đi.'],
 [f'In trang 9 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Giấy tờ tùy thân, giấy tờ khám bệnh (để xem, không cần mang ở bài này).'],
 ['Việt Nam có <strong>Luật Người khuyết tật 2010</strong>, hiệu lực từ 01/01/2011.',
  'Bạn có quyền <strong>tham gia bình đẳng</strong> vào hoạt động xã hội.',
  'Bạn có quyền <strong>sống độc lập, hòa nhập</strong> cộng đồng.',
  'Bạn có quyền dùng dịch vụ <strong>y tế, phục hồi chức năng, học, học nghề, việc làm</strong> phù hợp.',
  'Luật <strong>cấm</strong> kỳ thị, phân biệt; cấm xâm phạm thân thể, tài sản; cấm cản trở kết hôn, nuôi con.',
  '<strong>Mức độ khuyết tật</strong> do Hội đồng ở xã, phường xác định. Chủ tịch Ủy ban nhân dân xã, phường lập Hội đồng.',
  'Người khuyết tật nặng và đặc biệt nặng có thể được <strong>trợ cấp xã hội hằng tháng</strong>. Hỏi ở xã, phường.',
  'Khi đi hỏi: mang giấy tờ, <strong>ghi tên người tiếp và ngày hẹn</strong>.'],
 '<p><strong>Bài 1: phiếu hỏi hỗ trợ.</strong></p>'
 + lines(['Tôi muốn hỏi về (giấy xác nhận khuyết tật, trợ cấp, học nghề, đồ hỗ trợ…)', 'Giấy tờ tôi mang', 'Câu hỏi 1', 'Câu hỏi 2',
          'Người tiếp (tên, chức vụ)', 'Ngày hẹn, việc tiếp theo'])
 + '<p><strong>Bài 2: bốn quyền tôi nhớ.</strong></p>' + lines(['Quyền 1', 'Quyền 2', 'Quyền 3', 'Quyền 4']),
 ol(['Đọc phiếu cho người thân nghe.', 'Người thân đóng vai cán bộ. Bạn hỏi câu 1, ghi câu trả lời.', 'Thống nhất ngày đi hỏi thật, ai đi cùng.']),
 adapt('Gọi điện trước, hỏi lối vào cho xe lăn. Hỏi có thể nộp giấy tờ qua người thân hoặc trực tuyến không.',
       'Nhờ cán bộ đọc to giấy tờ. Không ký giấy mình chưa được đọc cho nghe.',
       'Mang phiếu đã viết sẵn. Đề nghị cán bộ trả lời bằng chữ.',
       'Người thân đi cùng, nhưng để bạn tự nói câu đầu tiên. Mang phiếu có hình.'),
 ['Không đưa giấy tờ gốc cho người lạ hứa "làm hộ hồ sơ" lấy phí.', 'Không ký giấy chưa hiểu.',
  'Thông tin này là thông tin chung, không phải tư vấn pháp lý. Thủ tục có thể đã đổi sau sắp xếp bộ máy năm 2025.'],
 ['Tôi nói được 4 quyền', 'Tôi biết nơi bắt đầu hỏi hỗ trợ', 'Tôi điền phiếu hỏi hỗ trợ'],
 ['Đi cùng, nhưng để bạn ấy nói và quyết định.', 'Giữ bản sao mọi giấy tờ, ghi ngày nộp.',
  'Hỏi hội người khuyết tật ở địa phương nếu có; họ thường biết thủ tục thực tế.'],
 [lb('Đã xác nhận', f'Quyền tham gia bình đẳng, sống độc lập, hòa nhập, dùng dịch vụ phù hợp ({D4}). Luật hiệu lực 01/01/2011 ({LUAT}).'),
  lb('Đã xác nhận', f'Các hành vi bị nghiêm cấm, gồm kỳ thị, xâm phạm thân thể, tài sản, cản trở kết hôn, nuôi con ({D14}).'),
  lb('Đã xác nhận', f'Hội đồng xác định mức độ khuyết tật cấp xã do Chủ tịch UBND xã, phường, thị trấn thành lập ({D16}).'),
  lb('Đã xác nhận', f'Mức chuẩn trợ giúp xã hội 500.000 đồng/tháng từ 01/07/2024 ({TCXH}).'),
  lb('Đã xác nhận', f'Việt Nam phê chuẩn Công ước của Liên hợp quốc về quyền của người khuyết tật ngày 28/11/2014 ({NQ84}).'),
  lb('Cần kiểm chứng', 'Hệ số trợ cấp theo mức độ khuyết tật; cơ quan và thủ tục cụ thể sau khi sắp xếp bộ máy năm 2025. Bài chưa đọc văn bản gốc.')])

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Tự lập từng bước, bài 10: so mức hỗ trợ trước và sau, chọn việc tiếp theo, làm tự đánh giá cuối khóa.',
 ['So <strong>mức hỗ trợ</strong> của việc đã tập: trước và bây giờ.',
  'Chọn <strong>việc tiếp theo</strong> và viết mục tiêu mới.',
  'Làm <strong>tự đánh giá cuối khóa</strong>.'],
 [f'In trang 10 của <a href="{TOOL}">Sổ tự lập từng bước</a>.', 'Bảng ghi mức hỗ trợ từ bài 3 và bài 4.'],
 ['Nhìn lại bảng ghi từ bài 3. <strong>Mức hỗ trợ đã giảm chưa?</strong>',
  'Giảm một mức là <strong>tiến bộ thật</strong>. Ví dụ: từ "làm mẫu" xuống "nhắc bằng lời".',
  '<strong>So với chính mình</strong>, không so với người khác.',
  'Có việc chưa tiến cũng không sao. Hỏi: bước nào khó? Cần đồ hỗ trợ gì?',
  'Việc đã tự làm được thì <strong>giữ</strong> bằng cách làm mỗi ngày.',
  '<strong>Chọn việc tiếp theo</strong> theo 3 tiêu chí ở bài 1.',
  'Lặp lại vòng: <strong>chọn – chia bước – tập có hỗ trợ – giảm dần</strong>.',
  'Bạn đã học <strong>cách học một việc mới</strong>. Cách này dùng được nhiều năm.'],
 '<p><strong>Bài 1: trước và bây giờ.</strong></p>'
 + table(['Việc đã tập', 'Mức hỗ trợ lần đầu', 'Mức hỗ trợ bây giờ', 'Điều giúp mình nhất'], [['', '', '', ''], ['', '', '', '']])
 + '<p><strong>Bài 2: việc tiếp theo.</strong></p>' + lines(['Việc tiếp theo', 'Mục tiêu: sau … tuần, tôi …, cần giúp …']),
 ol(['Người thân nói một tiến bộ họ thấy ở bạn.', 'Bạn nói một điều muốn người thân giúp ít đi.', 'Hai người làm tự đánh giá cuối khóa ở Sổ tự lập.']),
 adapt('Ghi cả đồ hỗ trợ đã giúp. Đồ hỗ trợ cũng là tiến bộ.',
       'Ghi âm phần nhìn lại để nghe lại sau 1 tháng.',
       'Viết hoặc vẽ phần nhìn lại; người thân viết lời nhận xét.',
       'Dùng hình mặt cười cho tự đánh giá. Chọn việc tiếp theo trong 2 việc có hình.'),
 ['Việc tiếp theo có nguy cơ (nấu ăn, đi xa): tập cùng người thân, hỏi chuyên viên trước.',
  'Buồn, lo kéo dài nhiều tuần, khó ăn ngủ: nói với người tin cậy hoặc gọi Ngày Mai.'],
 ['Tôi so được mức hỗ trợ trước và sau', 'Tôi chọn việc tiếp theo', 'Tôi làm tự đánh giá cuối khóa'],
 ['Nói tiến bộ cụ thể bạn thấy.', 'Hỏi: "Bạn muốn mình giúp ít đi ở việc nào?" và làm theo.',
  'Nhắn góp ý cho daynentang.com ở trang Chia sẻ (người từ 18 tuổi), không ghi tên hay chẩn đoán.'],
 [lb('Đã xác nhận', f'Người khuyết tật có thể chết sớm hơn tới 20 năm, phần lớn do bệnh phòng được và khó tiếp cận chăm sóc ({WHOD}).'),
  lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}); Tổng đài 111 ({T111}). Tra 28/10/2026, kiểm tra lại mỗi quý.'),
  lb('Đánh giá chuyên môn', 'Vòng tự lập và bảng so trước – sau do daynentang.com soạn.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi chọn được việc mình muốn tự làm', 'Tôi chia việc thành bước nhỏ', 'Tôi biết 5 mức hỗ trợ', 'Tôi tự làm 1 việc chăm sóc',
         'Nhà tôi ít nguy cơ té ngã hơn; tôi có thẻ thông tin', 'Tôi nhờ giúp và nói "không" được', 'Tôi đi chợ, giữ tiền an toàn',
         'Tôi dùng lịch hình ảnh', 'Tôi biết quyền của mình và nơi hỏi hỗ trợ', 'Tôi có việc tiếp theo để tập']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Sổ tự lập từng bước', 'Trang in cho khóa Tự lập từng bước: mục tiêu, danh sách bước, bảng mức hỗ trợ, rà soát nhà, thẻ thông tin, câu nhờ giúp, đi chợ, lịch hình ảnh, phiếu hỏi hỗ trợ.',
f'''
<h1>Sổ tự lập từng bước</h1>
<p>Dùng cho khóa <a href="{U}">Tự lập từng bước</a>. Chỉ để in, trang không lưu dữ liệu của bạn. In chữ to nếu cần (chọn thu phóng 125–150% khi in).</p>
{PRINT_ROW}
<h2>1. Mục tiêu (bài 1)</h2>
{lines(['Việc tôi chọn', 'Mục tiêu: sau … tuần, tôi …, cần giúp …', 'Chữ ký hoặc dấu của tôi và người thân'])}
<h2>2. Danh sách bước (bài 2)</h2>
{table(['Bước', 'Động từ + việc', 'Hình hoặc ghi chú'], [[str(n), '', ''] for n in range(1, 9)])}
<h2>3. Mức hỗ trợ (bài 3)</h2>
<p>{SUPPORT}.</p>
{table(['Bước', 'Lần 1', 'Lần 2', 'Lần 3', 'Lần 4', 'Lần 5'], [[str(n), '', '', '', '', ''] for n in range(1, 9)])}
<h2>4. Tự chăm sóc 7 ngày (bài 4)</h2>
{table(['Ngày'] + DAYS, [['Mức hỗ trợ'] + [''] * 7])}
<h2>5. Rà soát nhà và thẻ thông tin (bài 5)</h2>
{table(['Chỗ', 'Nguy cơ', 'Sửa thế nào', '✓'], [['Lối đi', '', '', ''], ['Ánh sáng', '', '', ''], ['Nhà tắm', '', '', ''], ['Tay vịn', '', '', '']])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Tên gọi</th><td></td></tr><tr><th>Người thân 1</th><td></td></tr><tr><th>Người thân 2</th><td></td></tr><tr><th>Người giúp cần biết</th><td></td></tr>
</tbody></table></div>
<p class="small">Cắt phần trên làm thẻ. Không ghi số giấy tờ tùy thân hay địa chỉ chi tiết.</p>
<h2>6. Nhờ giúp và người tin cậy (bài 6)</h2>
<p>"Mình cần… Vì… Bạn giúp bằng cách…"</p>
{lines(['Câu nhờ giúp 1', 'Câu nhờ giúp 2', 'Người tin cậy 1 (số gọi)', 'Người tin cậy 2 (số gọi)'])}
<h2>7. Đi chợ (bài 7)</h2>
{table(['Đồ cần mua', 'Giá dự tính', '✓', 'Giá thật'], [['', '', '', ''] for _ in range(5)])}
<p>Mã PIN, mã OTP: chỉ mình tôi biết.</p>
<h2>8. Lịch hình ảnh (bài 8)</h2>
{table(['1', '2', '3', '4', '5', '6'], [[''] * 6, [''] * 6])}
<h2>9. Phiếu hỏi hỗ trợ (bài 9)</h2>
{lines(['Tôi muốn hỏi về', 'Giấy tờ mang theo', 'Câu hỏi', 'Người tiếp, ngày hẹn'])}
<h2>10. Trước và bây giờ (bài 10)</h2>
{table(['Việc', 'Hỗ trợ lần đầu', 'Hỗ trợ bây giờ'], [['', '', ''], ['', '', '']])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">113</th><td>Công an, khi nguy hiểm ngay</td></tr>
<tr><th>115</th><td>Cấp cứu y tế</td></tr>
<tr><th>111</th><td>Bảo vệ trẻ em dưới 18 tuổi (24/7)</td></tr>
<tr><th>117</th><td>Phòng, chống bạo lực gia đình (24/7)</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
</tbody></table></div>
<h2>Tự đánh giá (bài 1 và bài 10)</h2>
<p>0 = chưa · 1 = làm được khi có giúp · 2 = tự làm được. Có thể dùng ☹ 😐 ☺.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Bài 1</th><th>Bài 10</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán hay xác định mức độ khuyết tật.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Tự lập từng bước', 'Khóa tự học miễn phí cho người khuyết tật từ 15 tuổi và người thân: chọn việc, chia bước, giúp vừa đủ, tự chăm sóc, an toàn, nhờ giúp, tiền, lịch hình ảnh, quyền và hỗ trợ.',
f'''
<p class="eyebrow">Cá nhân · Khóa C7 · Đang thử nghiệm</p>
<h1>Tự lập từng bước</h1>
<p class="lead">Tự lập không có nghĩa là làm mọi thứ một mình. Đó là được tự chọn, tự làm phần mình làm được, và nhờ giúp đúng chỗ.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn tự làm thêm từng việc hằng ngày, với hỗ trợ giảm dần; giữ an toàn; biết nhờ giúp, giữ tiền và biết quyền của mình</td></tr>
<tr><th>Dành cho</th><td>Người khuyết tật từ 15 tuổi (vận động, nhìn, nghe, trí tuệ – chậm phát triển) và người thân, người chăm sóc. Bạn 15–17 tuổi học cùng người lớn tin cậy</td></tr>
<tr><th>Thời lượng</th><td>10 bài, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, làm cùng người thân 5 phút</td></tr>
<tr><th>Cách đọc</th><td>Mỗi bài có phần dễ đọc (câu ngắn, mỗi câu một ý), bảng "Làm cho hợp với mình" theo dạng khuyết tật, và phần cho người đồng hành. Trang đọc được bằng trình đọc màn hình; mọi hình có mô tả</td></tr>
<tr><th>Cần có</th><td>Giấy, bút hoặc ảnh; một người thân đồng hành</td></tr>
<tr><th>Tình trạng</th><td>Đủ 10 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của người khuyết tật, hội người khuyết tật, chuyên viên phục hồi chức năng, giáo viên giáo dục đặc biệt</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn có 1 việc muốn tự làm, đã chia bước và bắt đầu tập.</li><li>Người thân biết đợi vài giây trước khi giúp.</li><li>Bạn có thẻ thông tin và 2 người tin cậy.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: mình được chọn, được thử, được nhờ giúp và được nói "không".</li><li>Kỹ năng: chia việc thành bước và giảm dần hỗ trợ, dùng cho mọi việc mới.</li><li>Biết quyền và nơi hỏi hỗ trợ.</li></ul></div>
</div>
{figure_block('KHOAJ')}

<h2 id="muoi-bai">Mười bài</h2>
<div class="table-wrap"><table>
<thead><tr><th>Bài</th><th>Tên</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ tự lập từng bước</a>: mục tiêu, danh sách bước, bảng mức hỗ trợ, rà soát nhà, thẻ thông tin, câu nhờ giúp, đi chợ, lịch hình ảnh, phiếu hỏi hỗ trợ, tự đánh giá.</li>
<li><a href="{RSN}">Phiếu rà soát nhà</a> (bài 5) và <a href="{BTC}">Bảng thu chi</a> (bài 7).</li></ul>

<h2>Cho người đồng hành</h2>
<ul>
<li>Hỏi trước, chờ rồi mới giúp. Giúp ít nhất có thể.</li>
<li>Để bạn ấy chọn việc và nói câu đầu tiên. Không nói thay khi bạn ấy nói được.</li>
<li>Tôn trọng riêng tư khi tắm, vệ sinh; tôn trọng câu "không".</li>
<li>Ghi lại mức hỗ trợ thật; tiến bộ là so với chính bạn ấy.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{NCAEP}</td><td>Chia việc thành bước, gợi ý theo mức, chờ trước khi gợi ý, củng cố, hình ảnh, tự quản lý</td><td><span class="label">[Đã xác nhận]</span> 28 phương pháp đạt tiêu chí bằng chứng, tổng quan tài liệu 1990–2017; chủ yếu ở người tự kỷ. Áp dụng cho các dạng khuyết tật khác là <span class="label">[Suy luận]</span></td></tr>
<tr><td>{ETR}</td><td>Cách viết phần dễ đọc</td><td><span class="label">[Đã xác nhận]</span> Tiêu chuẩn châu Âu soạn năm 2010; bài chưa được người khuyết tật trí tuệ đọc thử</td></tr>
<tr><td>{WHOF}; {WHOAT}</td><td>Phòng té ngã, đồ hỗ trợ</td><td><span class="label">[Đã xác nhận]</span> Tờ thông tin WHO; bằng chứng sửa nhà chủ yếu ở người cao tuổi</td></tr>
<tr><td>{HUGH}</td><td>Lý do có bài nhờ giúp, nói "không", giữ tiền</td><td><span class="label">[Đã xác nhận]</span> 26 nghiên cứu quan sát; nguy cơ bị bạo lực cao hơn (tương quan)</td></tr>
<tr><td>{LUAT}; {NQ84}; {TCXH}</td><td>Quyền, hành vi bị cấm, xác định mức độ khuyết tật, trợ cấp</td><td><span class="label">[Đã xác nhận]</span> Văn bản pháp luật, đọc qua trang tra cứu và tóm tắt; thủ tục sau 2025 <span class="label">[Cần kiểm chứng]</span></td></tr>
<tr><td>{VDS}; {WHOD}</td><td>Bối cảnh Việt Nam và thế giới</td><td><span class="label">[Đã xác nhận]</span> Số liệu điều tra và tờ thông tin</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các phương pháp trong khóa có bằng chứng khi do người được đào tạo dùng, chủ yếu với người tự kỷ. Khóa tự học này chưa được thử nghiệm, nên chúng tôi không hứa kết quả.</p>
  <p>Mỗi người khuyết tật một khác. Khóa không thay thế khám bệnh, phục hồi chức năng, giáo dục đặc biệt hay tư vấn pháp lý. Phần thủ tục có thể đã đổi; hãy hỏi Ủy ban nhân dân xã, phường nơi bạn ở.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C7 built')
