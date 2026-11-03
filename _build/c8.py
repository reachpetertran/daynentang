# Khóa C8 "Chăm tâm trí cơ bản" – trang khóa, 10 bài, công cụ "Sổ chăm tâm trí" (có Kế hoạch giữ vững).
# Người đọc: người từ 15 tuổi đang căng thẳng, buồn, lo kéo dài; bạn 15–17 học cùng người lớn tin cậy.
# Có người đọc dưới 18 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
# An toàn: không mô tả cách tự hại; mọi bài có khối khủng hoảng ở đầu và khối Cần giúp ngay ở cuối.
import illus_c8  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/cham-tam-tri-co-ban/'
TOOL = '/cong-cu/so-cham-tam-tri/'
C2 = '/khoa-hoc/hieu-minh/'
C5 = '/khoa-hoc/15-phut-moi-ngay/'
G5 = '/khoa-hoc/vo-chong-dong-long/'
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
def selftab(items, a='Tuần này', b='Sau 2 tuần'):
    rows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in items)
    return ('<p>0 = chưa làm · 1 = làm 1–3 ngày trong tuần · 2 = làm từ 4 ngày trở lên. Đây là tự theo dõi, không phải chấm điểm bản thân.</p>'
            f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>{a}</th><th>{b}</th></tr></thead><tbody>{rows}</tbody></table></div>')

# ---------- Nguồn (đã tra 03/11/2026) ----------
DWM = '<a href="https://www.who.int/publications/i/item/9789240003927">WHO – Doing What Matters in Times of Stress (29/4/2020, CC BY-NC-SA 3.0 IGO, có bản tiếng Việt)</a>'
WDEP = '<a href="https://www.who.int/news-room/fact-sheets/detail/depression">WHO – Trầm cảm (tờ thông tin, 11/9/2026)</a>'
WSUI = '<a href="https://www.who.int/news-room/fact-sheets/detail/suicide">WHO – Tự tử (tờ thông tin, 28/8/2026)</a>'
SHP = '<a href="https://doaj.org/article/955a816979774135adb958354d58830f">Thử nghiệm Self-Help Plus ở Uganda, <em>The Lancet Global Health</em> 2/2020</a>'
PMP = '<a href="https://www.elrha.org/news-blogs/results-r2hc-supported-trial-suggest-effectiveness-new-psychological-intervention">Thử nghiệm PM+ ở Peshawar, Pakistan (đăng trên <em>JAMA</em>, Elrha tóm tắt)</a>'
EKERS = '<a href="https://durham-repository.worktribe.com/output/1427994/behavioural-activation-for-depression-an-update-of-meta-analysis-of-effectiveness-and-sub-group-analysis">Ekers et al. 2014, <em>PLoS ONE</em></a>'
STAN = '<a href="https://www.npr.org/sections/health-shots/2018/07/11/628029412/a-simple-emergency-room-intervention-can-help-cut-future-suicide-risk">Stanley et al. 2018, <em>JAMA Psychiatry</em> (NPR tóm tắt)</a>'
DAZZI = '<a href="https://www.cambridge.org/core/product/FCAEE9E5BC840D76CF10AEBECD921AC9">Dazzi et al. 2014, <em>Psychological Medicine</em></a>'
AASMI = '<a href="https://aasm.org/new-guideline-supports-behavioral-psychological-treatments-for-insomnia/">AASM – hướng dẫn điều trị mất ngủ bằng hành vi (Edinger et al., <em>J Clin Sleep Med</em> 2021)</a>'
AASMA = '<a href="https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf">AASM và SRS 2015, <em>J Clin Sleep Med</em> 11(6)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
WHOPA = '<a href="https://who.int/initiatives/behealthy/physical-activity">WHO – Be Healthy: vận động</a>'
HL = '<a href="https://www.rti.org/publication/social-relationships-mortality-risk-meta-analytic-review">Holt-Lunstad et al. 2010, <em>PLoS Medicine</em></a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'
T111 = '<a href="https://tongdai111.vn/">tongdai111.vn</a>'

CRISIS = ('<div class="box warn"><p><strong>Nếu bạn đang nghĩ tới chuyện tự tử hoặc tự làm hại mình:</strong> đừng ở một mình. '
          'Nói ngay với một người ở gần. Gọi <strong>115</strong> hoặc tới khoa cấp cứu gần nhất. '
          'Dưới 18 tuổi: <strong>111</strong> (24/7). Muốn được nghe: Ngày Mai <strong>096 306 1414</strong> (13:00–20:30, thứ Tư – Chủ nhật).</p></div>')
REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài chưa được bác sĩ tâm thần, nhà tâm lý lâm sàng hay nhân viên công tác xã hội duyệt. '
          'Khóa dạy kỹ năng tự chăm sóc. Khóa không thay thế khám, điều trị hay tư vấn tâm lý.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Người từ 18 tuổi có thể góp ý cho bài ở trang '
           '<a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên thật, nơi ở hay chẩn đoán.</p>')
TALK = ('Nguy hiểm ngay: <strong>115</strong> (cấp cứu), <strong>113</strong> (công an). Dưới 18 tuổi: <strong>111</strong> (24/7). '
        'Bạo lực trong gia đình: <strong>117</strong> (24/7). Buồn, lo kéo dài: Ngày Mai <strong>096 306 1414</strong>.')
TEEN = 'Nếu bạn 15–17 tuổi: học cùng bố mẹ, thầy cô hoặc một người lớn bạn tin.'
DEEP = 'Muốn tập thiền hay tìm hiểu triết lý sống sâu hơn: xem trang chị em <strong>tamhonkhoe.com</strong>.'

L = {
 '1': (1, 'tam-tri-cung-can-cham', 'Bài 1', 'Tâm trí cũng cần chăm'),
 '2': (2, 'goi-ten-tho-cham', 'Bài 2', 'Gọi tên cảm xúc, thở chậm'),
 '3': (3, 'neo-lai', 'Bài 3', 'Neo lại khi cảm xúc dâng cao'),
 '4': (4, 'viec-nho-co-y-nghia', 'Bài 4', 'Một việc nhỏ có ý nghĩa mỗi ngày'),
 '5': (5, 'giac-ngu', 'Bài 5', 'Giấc ngủ khi lòng không yên'),
 '6': (6, 'lo-lang-vong-vo', 'Bài 6', 'Lo lắng và suy nghĩ vòng vo'),
 '7': (7, 'giai-quyet-van-de', 'Bài 7', 'Giải quyết vấn đề từng bước'),
 '8': (8, 'ket-noi', 'Bài 8', 'Kết nối, người mình có thể nhờ'),
 '9': (9, 'ruou-bia-man-hinh', 'Bài 9', 'Rượu bia, chất kích thích, màn hình khi buồn'),
 '10': (10, 'ke-hoach-giu-vung', 'Bài 10', 'Kế hoạch giữ vững và khi nào cần giúp'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn chấm nhiệt kế tâm trí 7 tối và biết dấu hiệu nên đi khám.'),
 (2, 'Bạn gọi tên cảm xúc 1 lần mỗi ngày và thở chậm 1 phút.'),
 (3, 'Bạn dùng cách neo lại ít nhất 2 lần khi cảm xúc dâng cao.'),
 (4, 'Bạn làm 1 việc nhỏ có ý nghĩa mỗi ngày, 5 ngày trong tuần.'),
 (5, 'Bạn giữ giờ dậy cố định 7 ngày và đổi 1 thói quen trước khi ngủ.'),
 (6, 'Bạn dùng "giờ lo 15 phút" 5 ngày.'),
 (7, 'Bạn giải quyết 1 vấn đề nhỏ theo 5 bước.'),
 (8, 'Bạn vẽ vòng người có thể nhờ và mở lời với 1 người.'),
 (9, 'Bạn viết 1 câu "Nếu… thì…" để thay một cách làm dịu có hại.'),
 (10, 'Bạn viết xong Kế hoạch giữ vững và đưa 1 người tin cậy xem.'),
]

def lesson(k, desc, goals, prep, read, do, note, safety, selfq, adult, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Bài {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Ghi lại 5 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (2 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Ghi lại (5 phút)', note),
        sec(6, 'An toàn', ul(safety + [TEEN, TALK])),
        sec(7, 'Tự theo dõi', selftab(selfq)),
        sec(8, 'Cho người đồng hành: người thân, bạn bè, thầy cô', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Chăm tâm trí cơ bản</a> · Bài {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{CRISIS}
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('P' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
THERMO = ['Tâm trạng', 'Giấc ngủ', 'Sức lực', 'Kết nối với người khác']

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Chăm tâm trí cơ bản, bài 1: tâm trí cũng cần chăm mỗi ngày; nhiệt kế tâm trí 0–10; dấu hiệu nên gặp nhân viên y tế.',
 ['Chấm <strong>nhiệt kế tâm trí</strong> 0–10 cho 4 mục mỗi tối, trong 7 ngày.',
  'Nói được <strong>3 dấu hiệu</strong> cho thấy nên gặp nhân viên y tế.',
  'Ghi <strong>1 điều</strong> đang giúp mình đứng vững.'],
 [f'In trang 1 của <a href="{TOOL}">Sổ chăm tâm trí</a>, hoặc lấy một tờ giấy.', 'Một chỗ ngồi yên 10 phút.'],
 ['Ai cũng có ngày buồn, ngày lo. Tâm trí cũng <strong>cần chăm</strong> như cơ thể.',
  'Chăm tâm trí gồm việc nhỏ mỗi ngày: <strong>ngủ, vận động, gặp người, làm việc có ý nghĩa</strong>.',
  'Buồn vài ngày rồi qua là bình thường. Vẫn ăn, ngủ, làm việc được.',
  '<strong>Nên gặp nhân viên y tế</strong> khi buồn, trống rỗng hoặc mất hứng thú gần như cả ngày, hầu hết các ngày, <strong>từ 2 tuần trở lên</strong>.',
  'Dấu hiệu đi kèm: khó tập trung, thấy mình vô dụng, mất hy vọng, ngủ hoặc ăn thay đổi nhiều, rất mệt.',
  '<strong>Ý nghĩ về cái chết hay tự tử</strong> cũng là một dấu hiệu. Khi có ý nghĩ đó, nói ngay với người tin cậy.',
  'Trầm cảm là <strong>bệnh chữa được</strong>. Có cách điều trị bằng trò chuyện, có khi kèm thuốc.',
  '<strong>Nhiệt kế tâm trí</strong> giúp bạn thấy mình thay đổi theo ngày. Nó không dùng để chẩn đoán.'],
 '<p><strong>Bài 1: nhiệt kế tâm trí 7 tối.</strong> Chấm 0 (rất tệ) đến 10 (rất ổn).</p>'
 + table(['Mục'] + DAYS, [[m] + [''] * 7 for m in THERMO])
 + '<p><strong>Bài 2: dấu hiệu của mình.</strong> Đánh dấu ✓ những điều đúng với bạn trong 2 tuần qua.</p>'
 + ul(['Buồn hoặc trống rỗng gần như mỗi ngày.', 'Không còn thích những việc trước đây thích.', 'Ngủ hoặc ăn thay đổi nhiều.',
       'Rất mệt, khó tập trung.', 'Thấy mình vô dụng, mất hy vọng.', 'Có ý nghĩ về cái chết.'])
 + '<p class="small">Có ✓ ở 2 dòng đầu từ 2 tuần trở lên, hoặc ✓ ở dòng cuối: hãy nói với người tin cậy và gặp nhân viên y tế. Danh sách này không phải bài kiểm tra chẩn đoán.</p>',
 lines(['Một điều đang giúp mình đứng vững', 'Một người mình có thể kể khi không ổn']),
 ['Có ý nghĩ về cái chết: không chờ hết khóa. Nói ngay với người tin cậy, gọi 115 nếu thấy nguy hiểm.',
  'Đang uống thuốc theo đơn: không tự ngừng. Hỏi bác sĩ trước khi đổi.'],
 ['Tôi chấm nhiệt kế 7 tối', 'Tôi nói được 3 dấu hiệu nên đi khám', 'Tôi ghi 1 điều giúp mình đứng vững'],
 ['Hỏi "Dạo này bạn thấy thế nào?" rồi nghe hết, không khuyên ngay.', 'Không nói "cố lên", "nghĩ tích cực đi". Nói "Mình ở đây, mình nghe."',
  'Nếu bạn ấy có dấu hiệu 2 tuần trở lên, cùng đi khám nếu bạn ấy đồng ý.'],
 [lb('Đã xác nhận', f'Khoảng 5,2% người lớn trên thế giới có trầm cảm năm 2023; giai đoạn trầm cảm kéo dài gần như cả ngày, hầu hết các ngày, ít nhất 2 tuần ({WDEP}).'),
  lb('Đã xác nhận', f'Dấu hiệu gồm khó tập trung, thấy có lỗi hoặc vô giá trị, mất hy vọng, ý nghĩ về cái chết hay tự tử, rối loạn ngủ, thay đổi ăn uống, rất mệt ({WDEP}).'),
  lb('Đã xác nhận', f'Có các liệu pháp trò chuyện hiệu quả: kích hoạt hành vi, giải quyết vấn đề, nhận thức – hành vi, liên cá nhân ({WDEP}).'),
  lb('Đánh giá chuyên môn', 'Nhiệt kế tâm trí 0–10 bốn mục do daynentang.com soạn; chưa được kiểm định, chỉ để tự theo dõi.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Chăm tâm trí cơ bản, bài 2: gọi tên cảm xúc bằng một câu ngắn và thở chậm một phút.',
 ['Gọi tên cảm xúc <strong>1 lần mỗi ngày</strong> bằng câu "Mình đang thấy… vì…".',
  'Thở chậm <strong>1 phút</strong>, thở ra dài hơn hít vào.',
  'Ghi lại cảm xúc 7 ngày.'],
 [f'In trang 2 của <a href="{TOOL}">Sổ chăm tâm trí</a>.', 'Đồng hồ hoặc đếm nhẩm.'],
 ['Cảm xúc <strong>không tốt, không xấu</strong>. Nó là tín hiệu cho biết điều gì đang xảy ra.',
  'Có nhiều tên: buồn, lo, sợ, giận, xấu hổ, cô đơn, mệt, nhẹ nhõm, vui.',
  'Gọi đúng tên giúp bạn <strong>biết mình cần gì</strong>. Cô đơn cần người. Mệt cần nghỉ.',
  'Câu mẫu: "<strong>Mình đang thấy</strong> lo <strong>vì</strong> mai phải nói chuyện với sếp."',
  'Một cảm xúc mạnh thường <strong>lên rồi xuống</strong>, như sóng. Nó không ở mãi.',
  '<strong>Thở chậm:</strong> ngồi, thả vai. Hít vào bằng mũi khoảng 4 nhịp.',
  'Thở ra chậm khoảng 6 nhịp, như thổi nguội cốc nước. Làm 5–6 lần, khoảng 1 phút.',
  'Thở chậm là <strong>kỹ năng ngắn</strong> để dịu xuống, không phải cách chữa bệnh.'],
 '<p><strong>Bài 1: thở chậm 1 phút ngay bây giờ.</strong> Trước và sau khi thở, chấm mức căng 0–10.</p>'
 + lines(['Mức căng trước khi thở (0–10)', 'Mức căng sau khi thở (0–10)'])
 + '<p><strong>Bài 2: hôm nay mình thấy gì?</strong></p>'
 + lines(['Mình đang thấy …', 'vì …', 'Mình cần …']),
 table(['Ngày'] + DAYS, [['Cảm xúc chính'] + [''] * 7, ['Thở chậm ✓'] + [''] * 7]),
 ['Thở chậm thấy chóng mặt, tê tay: dừng, thở bình thường.', 'Khó thở, đau ngực đột ngột: gọi 115, đừng nghĩ đó chỉ là lo.'],
 ['Tôi gọi tên cảm xúc mỗi ngày', 'Tôi thở chậm 1 phút', 'Tôi ghi lại 7 ngày'],
 ['Gọi tên cảm xúc cùng bạn ấy: "Nghe như bạn đang thất vọng?" Để bạn ấy sửa nếu chưa đúng.',
  'Đừng tranh cãi về cảm xúc ("không có gì phải buồn"). Cảm xúc là thật với người đang có nó.',
  f'Bạn 13–17 tuổi: xem thêm bài 3 khóa <a href="{C2}">Hiểu mình</a>.'],
 [lb('Đã xác nhận', f'Sách minh họa của WHO dạy kỹ năng quản lý căng thẳng vài phút mỗi ngày, có bản tiếng Việt ({DWM}).'),
  lb('Đánh giá chuyên môn', 'Câu "Mình đang thấy… vì… Mình cần…" và nhịp thở 4–6 do daynentang.com soạn. Đây là kỹ năng ngắn, chưa có thử nghiệm riêng.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Chăm tâm trí cơ bản, bài 3: neo lại khi cảm xúc dâng cao bằng ba bước Chậm – Để ý – Quay về và cách gọi tên 5–4–3–2–1.',
 ['Nói được <strong>3 bước neo lại</strong>: Chậm – Để ý – Quay về.',
  'Dùng cách neo lại <strong>ít nhất 2 lần</strong> trong tuần khi cảm xúc dâng cao.',
  'Ghi lại cảm xúc trước và sau khi neo lại.'],
 [f'In trang 3 của <a href="{TOOL}">Sổ chăm tâm trí</a>.'],
 ['Khi giận, sợ hay buồn dâng cao, ta dễ <strong>bị cuốn đi</strong>: nói, làm điều sau này hối tiếc.',
  '<strong>Neo lại</strong> giống thả neo cho thuyền khi có bão. Bão chưa tan, nhưng thuyền không trôi.',
  '<strong>Chậm lại:</strong> ấn chân xuống sàn, duỗi thẳng lưng, ép hai lòng bàn tay vào nhau.',
  '<strong>Để ý:</strong> nhận ra ý nghĩ, cảm giác trong người. Rồi để ý thứ xung quanh: màu, tiếng, mùi.',
  '<strong>Quay về:</strong> đưa sự chú ý về việc bạn đang làm, hoặc người đang ở trước mặt.',
  'Một cách để ý khác: gọi tên <strong>5</strong> thứ thấy, <strong>4</strong> thứ chạm, <strong>3</strong> tiếng nghe, <strong>2</strong> mùi, <strong>1</strong> hơi thở chậm.',
  'Neo lại <strong>không làm cảm xúc biến mất</strong>. Nó giúp bạn chọn việc làm tiếp theo.',
  'Tập khi đang bình tĩnh trước. Lúc khó mới dễ nhớ.'],
 '<p><strong>Bài 1: tập neo lại 2 phút</strong>, ngay khi đang bình tĩnh. Làm theo 3 bước.</p>'
 + '<p><strong>Bài 2: chuẩn bị trước.</strong> Lúc nào mình hay bị cuốn đi?</p>'
 + lines(['Lúc mình hay bị cuốn đi (ví dụ: khi bị chê, khi về nhà muộn)', 'Câu nhắc mình neo lại (ví dụ: "Chậm. Để ý. Quay về.")']),
 table(['Lần', 'Chuyện gì xảy ra', 'Cảm xúc trước (0–10)', 'Cảm xúc sau (0–10)'], [['1', '', '', ''], ['2', '', '', ''], ['3', '', '', '']]),
 ['Đang ở chỗ nguy hiểm (lái xe, đứng cạnh máy): dừng việc đó, ra chỗ an toàn rồi mới neo lại.',
  'Hay bị những ký ức đau ùa về, hoặc thấy mình như "không còn ở đây": nên gặp nhân viên y tế.'],
 ['Tôi nói được 3 bước neo lại', 'Tôi neo lại 2 lần khi cảm xúc dâng cao', 'Tôi ghi trước và sau'],
 ['Khi bạn ấy đang rất xúc động, nói ít, chậm: "Mình ở đây. Hai đứa mình thở chậm nhé."',
  'Đừng chạm người khi chưa hỏi. Có người dịu đi khi được nắm tay, có người không.',
  f'Vợ chồng hay cãi to: xem bài 4 khóa <a href="{G5}">Vợ chồng đồng lòng</a> (tạm dừng 20 phút).'],
 [lb('Đã xác nhận', f'Neo lại (grounding) là kỹ năng đầu tiên trong sách của WHO ({DWM}).'),
  lb('Đã xác nhận', f'Chương trình nhóm Self-Help Plus dựa trên sách này: 694 phụ nữ tị nạn ở Uganda; sau 3 tháng, căng thẳng giảm nhiều hơn nhóm chứng, mức tác dụng nhỏ (d = −0,26) ({SHP}).'),
  lb('Suy luận', 'Thử nghiệm trên có 5 buổi nhóm có người dẫn. Tự đọc một mình có thể có tác dụng ít hơn.'),
  lb('Đánh giá chuyên môn', 'Cách gọi tên 5–4–3–2–1 là cách làm phổ biến, chưa có thử nghiệm riêng; ba bước Chậm – Để ý – Quay về là lời viết lại của daynentang.com.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Chăm tâm trí cơ bản, bài 4: kích hoạt hành vi – làm một việc nhỏ có ý nghĩa mỗi ngày theo kế hoạch, không chờ có hứng.',
 ['Viết danh sách <strong>8 việc nhỏ</strong> thuộc 4 loại.',
  'Làm <strong>1 việc nhỏ mỗi ngày</strong>, 5 ngày trong tuần.',
  'Chấm mức <strong>vui</strong> và mức <strong>làm được</strong> sau mỗi việc.'],
 [f'In trang 4 của <a href="{TOOL}">Sổ chăm tâm trí</a>.'],
 ['Khi buồn, ta hay <strong>bỏ việc</strong>, nằm một chỗ, tránh gặp người.',
  'Bỏ việc làm cuộc sống <strong>ít điều vui, ít điều có ích</strong>. Thế là buồn hơn. Đó là một vòng.',
  'Cách bẻ vòng: <strong>làm trước, hứng thú đến sau</strong>. Không chờ có hứng mới làm.',
  'Chọn việc <strong>thật nhỏ</strong>, khoảng 10 phút. Nhỏ tới mức khó nói "không".',
  'Bốn loại việc: <strong>chăm thân</strong> (tắm, đi bộ), <strong>có ích</strong> (dọn một góc), <strong>kết nối</strong> (nhắn một người), <strong>vui nhỏ</strong> (nghe một bài hát).',
  'Chọn việc hợp với <strong>điều bạn coi trọng</strong>: gia đình, sức khỏe, học, giúp người.',
  'Ghi giờ cụ thể: "<strong>7 giờ tối, đi bộ quanh xóm 10 phút</strong>."',
  'Làm xong, ghi lại. Không vui ngay cũng <strong>vẫn tính là làm được</strong>.'],
 '<p><strong>Bài 1: tám việc nhỏ của mình.</strong></p>'
 + table(['Loại', 'Việc 1', 'Việc 2'], [['Chăm thân', '', ''], ['Có ích', '', ''], ['Kết nối', '', ''], ['Vui nhỏ', '', '']])
 + '<p><strong>Bài 2: chọn việc cho ngày mai.</strong></p>' + lines(['Việc', 'Giờ', 'Ở đâu']),
 table(['Ngày'] + DAYS, [['Việc đã làm'] + [''] * 7, ['Vui (0–10)'] + [''] * 7, ['Làm được (0–10)'] + [''] * 7]),
 ['Vận động: bắt đầu nhẹ. Có bệnh tim, huyết áp, đang mang thai: hỏi nhân viên y tế trước khi tập mạnh.',
  'Nằm cả ngày nhiều ngày liền, không ăn uống được: đây là lúc cần gặp nhân viên y tế, không chỉ tự tập.'],
 ['Tôi có danh sách 8 việc nhỏ', 'Tôi làm 1 việc nhỏ mỗi ngày', 'Tôi chấm vui và làm được'],
 ['Rủ cùng làm việc nhỏ: "Đi bộ với mình 10 phút nhé?"', 'Khen việc đã làm, không so với lúc khỏe.',
  'Không làm hết việc thay bạn ấy. Giúp bắt đầu, rồi để bạn ấy tự làm phần mình.'],
 [lb('Đã xác nhận', f'Phân tích gộp 26 thử nghiệm, 1.524 người; so với nhóm chứng (25 thử nghiệm), kích hoạt hành vi giảm trầm cảm nhiều hơn (SMD −0,74) ({EKERS}).'),
  lb('Đã xác nhận', f'WHO liệt kê kích hoạt hành vi là một liệu pháp trò chuyện hiệu quả; khuyên vận động đều, dù chỉ đi bộ ngắn ({WDEP}).'),
  lb('Suy luận', 'Các thử nghiệm trên phần lớn có người hướng dẫn. Tự học một mình có thể kém hiệu quả hơn.'),
  lb('Đánh giá chuyên môn', 'Bốn loại việc nhỏ và bảng chấm do daynentang.com soạn.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Chăm tâm trí cơ bản, bài 5: giờ dậy cố định, giường để ngủ, dậy khi nằm lâu không ngủ được, một ngày giúp giấc ngủ.',
 ['Giữ <strong>giờ dậy cố định</strong> 7 ngày, kể cả cuối tuần.',
  'Đổi <strong>1 thói quen</strong> trước khi ngủ.',
  'Ghi nhật ký ngủ 7 ngày.'],
 [f'In trang 5 của <a href="{TOOL}">Sổ chăm tâm trí</a>.', 'Đặt sổ và bút cạnh giường.'],
 ['Khi buồn, lo, ta hay <strong>ngủ khó, ngủ chập chờn</strong>, hoặc ngủ quá nhiều.',
  'Người lớn nên ngủ <strong>từ 7 giờ</strong> mỗi đêm. Tuổi 15–17 cần <strong>8–10 giờ</strong>.',
  '<strong>Giờ dậy cố định</strong> mỗi ngày giúp cơ thể giữ nhịp. Giờ dậy quan trọng hơn giờ đi ngủ.',
  '<strong>Giường để ngủ.</strong> Chỉ lên giường khi buồn ngủ. Không nằm lướt điện thoại trên giường.',
  'Nằm lâu không ngủ được: <strong>dậy</strong>, ra chỗ khác, làm việc nhẹ dưới ánh sáng dịu. Buồn ngủ lại mới quay về.',
  'Ban ngày: ra <strong>ánh sáng buổi sáng</strong>, vận động. Tránh cà phê, trà đặc từ chiều.',
  'Rượu làm dễ ngủ lúc đầu nhưng hay làm <strong>tỉnh giấc giữa đêm</strong>.',
  'Mất ngủ kéo dài nhiều tuần: có cách điều trị bằng trò chuyện. Hãy hỏi nhân viên y tế.'],
 '<p><strong>Bài 1: chọn giờ dậy.</strong></p>' + lines(['Giờ dậy cố định của mình', 'Một thói quen trước khi ngủ mình sẽ đổi'])
 + '<p><strong>Bài 2: nhật ký ngủ.</strong> Ghi mỗi sáng.</p>'
 + table(['Ngày'] + DAYS, [['Giờ lên giường'] + [''] * 7, ['Giờ dậy'] + [''] * 7, ['Ngủ ngon (0–10)'] + [''] * 7]),
 lines(['Sau 7 ngày, điều gì giúp mình ngủ tốt hơn?', 'Điều gì làm mình ngủ kém?']),
 ['Làm ca đêm: xem thêm bài 2 khóa <a href="' + C5 + '">15 phút mỗi ngày</a>.',
  'Ngáy to, ngừng thở khi ngủ, buồn ngủ khi lái xe: gặp nhân viên y tế.',
  'Không tự mua thuốc ngủ. Thuốc ngủ cần bác sĩ kê và theo dõi.'],
 ['Tôi giữ giờ dậy cố định', 'Tôi đổi 1 thói quen trước khi ngủ', 'Tôi ghi nhật ký ngủ 7 ngày'],
 ['Giữ nhà yên tĩnh, tối vào giờ ngủ của cả nhà.', 'Đừng chê "ngủ nướng". Rủ ra ngoài buổi sáng thay vì mắng.',
  'Bạn 15–17 tuổi: cùng thống nhất giờ cất điện thoại ra khỏi phòng ngủ.'],
 [lb('Đã xác nhận', f'Người lớn nên ngủ từ 7 giờ mỗi đêm ({AASMA}). Tuổi 13–18: 8–10 giờ mỗi 24 giờ ({AASM}).'),
  lb('Đã xác nhận', f'Hướng dẫn AASM: khuyến nghị mạnh điều trị mất ngủ bằng nhận thức – hành vi (CBT-I); kiểm soát kích thích (chỉ lên giường khi buồn ngủ) là gợi ý có điều kiện; vệ sinh giấc ngủ đơn thuần không đủ để điều trị ({AASMI}).'),
  lb('Đã xác nhận', f'WHO khuyên giữ giờ ăn, giờ ngủ đều đặn và giảm rượu khi bị trầm cảm ({WDEP}).'),
  lb('Suy luận', 'Hướng dẫn AASM dành cho người lớn mất ngủ mạn tính có người điều trị. Bài này chỉ mượn ý cho người tự học.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Chăm tâm trí cơ bản, bài 6: phân biệt lo làm được và lo không làm được; giờ lo 15 phút; để ý nghĩ trôi qua.',
 ['Hỏi được câu "<strong>Việc này mình làm được gì không?</strong>" khi lo.',
  'Dùng <strong>giờ lo 15 phút</strong> 5 ngày.',
  'Tập <strong>để ý một ý nghĩ</strong> mà không chạy theo nó.'],
 [f'In trang 6 của <a href="{TOOL}">Sổ chăm tâm trí</a>.', 'Một tờ giấy nhỏ mang theo người để ghi ý lo.'],
 ['Lo giúp ta chuẩn bị. Lo <strong>quá nhiều, vòng vo</strong> thì làm ta mệt mà không giải quyết gì.',
  'Khi lo, hỏi: "<strong>Việc này mình làm được gì không?</strong>"',
  'Làm được: <strong>lên kế hoạch</strong> nhỏ (bài 7). Không làm được: neo lại (bài 3), để ý nghĩ trôi qua.',
  '<strong>Để ý nghĩ trôi qua:</strong> thêm câu "Mình đang có ý nghĩ rằng…" trước ý lo.',
  'Ví dụ: "Mình sẽ mất việc" thành "<strong>Mình đang có ý nghĩ rằng</strong> mình sẽ mất việc."',
  'Ý nghĩ <strong>chưa chắc là sự thật</strong>. Nó chỉ là ý nghĩ.',
  '<strong>Giờ lo 15 phút:</strong> chọn một khung giờ cố định, không sát giờ ngủ.',
  'Ngoài giờ lo, ý lo đến thì ghi vào giấy, nói "để tới giờ lo". Tới giờ, đọc lại và xử lý.'],
 '<p><strong>Bài 1: phân loại ý lo.</strong></p>'
 + table(['Ý lo', 'Làm được gì không? (có/không)', 'Nếu có: việc nhỏ đầu tiên'], [['', '', ''], ['', '', ''], ['', '', '']])
 + '<p><strong>Bài 2: chọn giờ lo.</strong></p>' + lines(['Giờ lo của mình (15 phút)', 'Chỗ ngồi lo']),
 table(['Ngày'] + DAYS, [['Dùng giờ lo ✓'] + [''] * 7, ['Mức lo cuối ngày (0–10)'] + [''] * 7]),
 ['Lo kèm tim đập nhanh, khó thở, sợ chết đi được, lặp lại nhiều lần: gặp nhân viên y tế để kiểm tra.',
  'Lo làm bạn không dám ra khỏi nhà, không đi làm, đi học được: đây là lúc cần giúp chuyên môn.'],
 ['Tôi hỏi "làm được gì không?" khi lo', 'Tôi dùng giờ lo 15 phút', 'Tôi tập câu "Mình đang có ý nghĩ rằng…"'],
 ['Đừng nói "đừng lo nữa". Hỏi: "Phần nào mình cùng làm được?"', 'Không trấn an quá nhiều lần cho cùng một ý lo; cùng xem lại bài 7.',
  'Giúp bạn ấy giữ đúng giờ lo, không ép nói chuyện lo vào giờ ngủ.'],
 [lb('Đã xác nhận', f'"Gỡ khỏi ý nghĩ khó" (unhooking) là kỹ năng thứ hai trong sách của WHO ({DWM}).'),
  lb('Đánh giá chuyên môn', 'Giờ lo 15 phút là kỹ thuật thường dùng trong liệu pháp nhận thức – hành vi. Bài chưa đọc tổng quan về hiệu quả của riêng kỹ thuật này.'),
  lb('Cần kiểm chứng', 'Mức hiệu quả của "giờ lo" khi tự học, không có người hướng dẫn.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Chăm tâm trí cơ bản, bài 7: giải quyết một vấn đề nhỏ theo 5 bước; tách vấn đề to thành phần tự lo, phần cần giúp, phần để sau.',
 ['Giải quyết <strong>1 vấn đề nhỏ</strong> theo 5 bước.',
  'Tách <strong>1 vấn đề to</strong> thành 3 phần.',
  'Có <strong>1 việc làm được trong 48 giờ</strong>.'],
 [f'In trang 7 của <a href="{TOOL}">Sổ chăm tâm trí</a>.'],
 ['Nhiều nỗi buồn, nỗi lo đến từ <strong>vấn đề thật</strong>: tiền, việc làm, nhà cửa, quan hệ.',
  'Vấn đề to làm ta thấy <strong>bất lực</strong>. Chia nhỏ giúp ta thấy có chỗ để bắt đầu.',
  '<strong>Bước 1:</strong> chọn một vấn đề nhỏ, viết một câu cụ thể.',
  '<strong>Bước 2:</strong> nghĩ <strong>nhiều cách</strong>, kể cả cách nghe lạ. Chưa chê cách nào.',
  '<strong>Bước 3:</strong> chọn một cách: được nhiều, mất ít, làm được ngay.',
  '<strong>Bước 4:</strong> chia thành bước nhỏ, ghi ngày giờ làm.',
  '<strong>Bước 5:</strong> làm, rồi xem lại. Chưa được thì quay lại bước 2.',
  'Vấn đề to: tách ra <strong>phần mình lo được</strong>, <strong>phần cần người giúp</strong>, <strong>phần để sau</strong>.'],
 '<p><strong>Bài 1: năm bước.</strong></p>'
 + lines(['1. Vấn đề (một câu)', '2. Các cách (ít nhất 3)', '3. Cách mình chọn', '4. Các bước nhỏ, ngày giờ', '5. Kết quả, việc tiếp theo'])
 + '<p><strong>Bài 2: tách vấn đề to.</strong></p>'
 + table(['Phần mình lo được', 'Phần cần người giúp (ai?)', 'Phần để sau'], [['', '', ''], ['', '', '']]),
 lines(['Việc mình làm trong 48 giờ tới', 'Ai có thể cùng làm hoặc nhắc mình']),
 ['Vấn đề tiền, nợ nặng: không vay tín dụng đen, không nhận "việc nhẹ lương cao". Hỏi người tin cậy trước.',
  'Vấn đề bạo lực trong nhà: an toàn trước. Gọi 113 khi nguy hiểm, 117 để được tư vấn (24/7).'],
 ['Tôi giải quyết 1 vấn đề theo 5 bước', 'Tôi tách 1 vấn đề to', 'Tôi làm 1 việc trong 48 giờ'],
 ['Cùng nghĩ cách, nhưng để bạn ấy chọn.', 'Giúp phần "cần người giúp" bằng việc cụ thể: đi cùng, gọi điện cùng, trông con giúp.',
  'Khen việc đã thử, kể cả khi chưa thành.'],
 [lb('Đã xác nhận', f'WHO liệt kê liệu pháp giải quyết vấn đề là một liệu pháp hiệu quả; chương trình PM+ của WHO gồm giải quyết vấn đề, quản lý căng thẳng, kích hoạt hành vi, tăng hỗ trợ xã hội ({WDEP}).'),
  lb('Đã xác nhận', f'Thử nghiệm PM+ với 346 người ở Pakistan, do người không chuyên được đào tạo 8 ngày thực hiện: sau 3 tháng, lo âu và trầm cảm giảm nhiều hơn nhóm chứng ({PMP}).'),
  lb('Suy luận', 'PM+ có người hướng dẫn trực tiếp. Bài này chỉ mượn ý năm bước cho người tự học.'),
  lb('Đánh giá chuyên môn', 'Mẫu năm bước và bảng tách vấn đề do daynentang.com soạn, không chép tài liệu PM+.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Chăm tâm trí cơ bản, bài 8: vẽ vòng người có thể nhờ, câu mở lời ngắn, và cách nghe khi người khác kể.',
 ['Vẽ <strong>vòng người có thể nhờ</strong> với ít nhất 3 người hoặc nơi.',
  'Mở lời với <strong>1 người</strong> trong tuần này.',
  'Nói được <strong>3 việc</strong> người nghe tốt làm.'],
 [f'In trang 8 của <a href="{TOOL}">Sổ chăm tâm trí</a>.'],
 ['Khi buồn, ta hay <strong>thu mình</strong>. Ít gặp người làm ta buồn hơn.',
  'Kết nối không cần nhiều người. <strong>Một, hai người</strong> tin được đã có ích.',
  '<strong>Vòng trong:</strong> người rất tin. <strong>Vòng giữa:</strong> bạn, đồng nghiệp, hàng xóm tốt. <strong>Vòng ngoài:</strong> nơi giúp chuyên môn.',
  '<strong>Mở lời</strong> chỉ cần một câu: "Dạo này mình không ổn. Bạn nghe mình 10 phút được không?"',
  'Bạn được chọn <strong>kể bao nhiêu</strong>. Không cần kể hết.',
  '<strong>Người nghe tốt:</strong> nghe hết, không ngắt lời; không phán xét; hỏi "Mình giúp được gì?"',
  'Có người phản ứng chưa tốt. Đó không phải lỗi của bạn. <strong>Thử người khác.</strong>',
  'Sống xa nhà: gọi video, nhắn tin cũng là kết nối.'],
 '<p><strong>Bài 1: vòng người có thể nhờ.</strong></p>'
 + table(['Vòng', 'Người hoặc nơi', 'Số gọi'], [['Trong: người rất tin', '', ''], ['Giữa: người quen tốt', '', ''], ['Ngoài: nơi giúp chuyên môn', 'Trạm y tế, bệnh viện gần nhà; Ngày Mai 096 306 1414', '']])
 + '<p><strong>Bài 2: câu mở lời của mình.</strong></p>' + lines(['Mình sẽ mở lời với', 'Câu mở lời', 'Lúc nào, ở đâu']),
 lines(['Mình đã mở lời chưa? Người đó phản ứng thế nào?', 'Mình thấy thế nào sau khi nói?']),
 ['Người làm bạn đau, đe dọa bạn: không phải người để nhờ. Tìm người khác hoặc gọi 113, 117.',
  'Trên mạng: cẩn thận người lạ tỏ ra rất quan tâm rồi xin tiền, xin ảnh riêng.'],
 ['Tôi vẽ vòng người có thể nhờ', 'Tôi mở lời với 1 người', 'Tôi nói được 3 việc người nghe tốt làm'],
 ['Khi được kể: cảm ơn vì đã tin mình. Nghe hết rồi mới nói.', 'Hỏi "Bạn cần mình nghe, hay cần mình giúp việc gì?"',
  'Hẹn lần gặp sau. Một tin nhắn hỏi thăm sau 2–3 ngày có ý nghĩa.'],
 [lb('Đã xác nhận', f'WHO khuyên giữ liên lạc với bạn bè, gia đình khi bị trầm cảm ({WDEP}).'),
  lb('Đã xác nhận', f'Phân tích gộp 148 nghiên cứu: người có quan hệ xã hội mạnh có khả năng sống sót cao hơn khoảng 50% trong thời gian theo dõi; đây là tương quan ({HL}).'),
  lb('Đánh giá chuyên môn', 'Ba vòng người có thể nhờ và câu mở lời do daynentang.com soạn.')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Chăm tâm trí cơ bản, bài 9: rượu bia, thuốc lá, chất kích thích, lướt mạng khi buồn; dịu ngắn nặng dài; câu "Nếu… thì…" để đổi thói quen.',
 ['Nhận ra <strong>1 cách làm dịu</strong> có hại mình đang dùng.',
  'Viết <strong>1 câu "Nếu… thì…"</strong> để thay nó.',
  'Theo dõi <strong>7 ngày</strong>.'],
 [f'In trang 9 của <a href="{TOOL}">Sổ chăm tâm trí</a>.'],
 ['Khi buồn, ta hay tìm cách <strong>quên nhanh</strong>: uống rượu, hút thuốc, lướt mạng tới khuya, chơi game, ăn quá nhiều.',
  'Những cách này <strong>dịu trong chốc lát</strong>. Về sau hay làm ngủ kém, buồn hơn, tốn tiền.',
  'Rượu bia, chất kích thích có thể làm <strong>trầm cảm nặng hơn</strong>.',
  'Không cần bỏ hết một lần. Bắt đầu bằng <strong>một thay đổi nhỏ</strong>.',
  'Câu "<strong>Nếu… thì…</strong>": "Nếu 10 giờ tối thấy buồn, thì mình thở chậm rồi gọi cho anh trai."',
  'Để <strong>đồ làm dịu tốt</strong> ở chỗ dễ lấy: dép đi bộ, số điện thoại, sổ ghi.',
  'Để <strong>đồ có hại</strong> ở xa: không trữ rượu trong nhà, sạc điện thoại ngoài phòng ngủ.',
  'Uống rượu hay dùng chất để chịu được mỗi ngày: đó là lúc <strong>cần người giúp</strong>, không chỉ tự cố.'],
 '<p><strong>Bài 1: cách làm dịu của mình.</strong></p>'
 + table(['Cách mình hay làm khi buồn', 'Dịu bao lâu?', 'Sau đó thế nào?'], [['', '', ''], ['', '', '']])
 + '<p><strong>Bài 2: câu "Nếu… thì…".</strong></p>' + lines(['Nếu …', 'thì mình …', 'Đồ mình để xa / để gần']),
 table(['Ngày'] + DAYS, [['Làm theo câu "Nếu… thì…" ✓'] + [''] * 7]),
 ['Đang uống nhiều rượu mỗi ngày: không tự ngừng đột ngột. Hỏi nhân viên y tế, vì ngừng đột ngột có thể nguy hiểm.',
  'Đang buồn nặng: không uống rượu một mình, không lái xe sau khi uống.',
  'Bạn dưới 18 tuổi: pháp luật cấm bán rượu bia cho người chưa đủ 18 tuổi.'],
 ['Tôi nhận ra 1 cách làm dịu có hại', 'Tôi có câu "Nếu… thì…"', 'Tôi theo dõi 7 ngày'],
 ['Không mắng, không bêu. Hỏi: "Mình giúp bạn đổi một chút được không?"', 'Cả nhà cùng không trữ rượu, cùng cất điện thoại sau 10 giờ tối.',
  'Thấy uống nhiều, dùng chất mỗi ngày: cùng đi khám.'],
 [lb('Đã xác nhận', f'WHO khuyên tránh hoặc giảm rượu và tránh chất cấm khi bị trầm cảm, vì có thể làm bệnh nặng hơn ({WDEP}).'),
  lb('Đã xác nhận', 'Cấm bán rượu, bia cho người chưa đủ 18 tuổi (Luật Phòng, chống tác hại của rượu, bia 44/2019/QH14, Điều 5 khoản 3, dùng lại từ khóa G4).'),
  lb('Đánh giá chuyên môn', 'Câu "Nếu… thì…" dựa trên ý dự định thực hiện (Gollwitzer & Sheeran 2006, dùng ở khóa G1, C2). Hiệu quả với việc giảm rượu khi tự học: chưa đọc nghiên cứu riêng.'),
  lb('Cần kiểm chứng', 'Ngừng rượu đột ngột ở người uống nhiều có thể nguy hiểm: đây là kiến thức y khoa phổ biến, bài chưa ghi nguồn gốc.')])

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Chăm tâm trí cơ bản, bài 10: viết Kế hoạch giữ vững 6 bước lúc bình tĩnh; khi nào cần giúp ngay; cách hỏi thẳng và ở bên người đang khó.',
 ['Viết xong <strong>Kế hoạch giữ vững</strong> 6 bước.',
  'Đưa kế hoạch cho <strong>1 người tin cậy</strong> xem.',
  'Nói được <strong>khi nào cần gọi 115</strong> hoặc tới cấp cứu.'],
 [f'In trang 10 của <a href="{TOOL}">Sổ chăm tâm trí</a> (Kế hoạch giữ vững).', 'Viết lúc đang bình tĩnh. Có thể viết cùng người tin cậy.'],
 ['Khi quá đau, quá mệt, có người nghĩ tới cái chết. <strong>Nhiều người từng có ý nghĩ đó và đã đi qua được.</strong>',
  'Có ý nghĩ đó không có nghĩa là bạn yếu hay xấu. Đó là <strong>dấu hiệu cần thêm giúp đỡ</strong>.',
  '<strong>Kế hoạch giữ vững</strong> viết lúc bình tĩnh, để dùng lúc khó. Lúc khó, ta khó nghĩ ra cách.',
  '<strong>Bước 1:</strong> dấu hiệu báo trước của riêng mình (ý nghĩ, cảm giác, tình huống).',
  '<strong>Bước 2:</strong> việc tự làm để dịu xuống (bài 2–4). <strong>Bước 3:</strong> người, nơi giúp mình đổi không khí.',
  '<strong>Bước 4:</strong> người mình nói thật được. <strong>Bước 5:</strong> nơi giúp: 115, khoa cấp cứu, đường dây.',
  '<strong>Bước 6:</strong> làm chỗ ở an toàn hơn. Nhờ người tin cậy giữ hộ thuốc dự trữ, thuốc trừ sâu và đồ có thể gây hại.',
  '<strong>Nguy hiểm ngay</strong>, không giữ được an toàn: bỏ qua các bước, gọi 115 hoặc tới cấp cứu, ở cạnh một người.'],
 f'<p><strong>Viết Kế hoạch giữ vững</strong> ở trang 10 của <a href="{TOOL}">Sổ chăm tâm trí</a>. Viết bằng lời của bạn, ngắn, dễ đọc.</p>'
 + lines(['1. Dấu hiệu báo trước của mình', '2. Việc tự làm để dịu xuống', '3. Người, nơi giúp mình đổi không khí',
          '4. Người mình nói thật được (tên, số gọi)', '5. Nơi giúp: 115 · khoa cấp cứu gần nhất: … · Ngày Mai 096 306 1414 · dưới 18 tuổi: 111',
          '6. Làm chỗ ở an toàn hơn: nhờ ai giữ hộ gì', 'Điều quan trọng giúp mình đi tiếp']),
 ol(['Chụp ảnh kế hoạch lưu trong điện thoại. Để một bản giấy trong ví hoặc cạnh giường.',
     'Đưa kế hoạch cho 1 người tin cậy xem. Nói: "Nếu mình nhắn chữ … nghĩa là mình cần bạn gọi ngay."',
     'Lưu số 115 và số người tin cậy ở đầu danh bạ.']),
 ['Đang có ý nghĩ tự tử ngay lúc này: dừng đọc, gọi 115 hoặc nói với người ở gần.',
  'Không ở một mình khi thấy mình không an toàn. Đi tới chỗ có người.',
  'Kế hoạch không thay thế khám và điều trị. Hãy gặp nhân viên y tế sớm.'],
 ['Tôi viết xong Kế hoạch giữ vững', 'Tôi đưa 1 người tin cậy xem', 'Tôi lưu số 115 và số người tin cậy'],
 ['Lo bạn ấy có ý nghĩ tự tử: <strong>hỏi thẳng</strong> "Bạn có đang nghĩ tới chuyện tự tử không?" Hỏi thẳng không làm ý nghĩ đó tăng lên.',
  'Nghe, không phán xét, không hứa giữ bí mật nếu bạn ấy đang nguy hiểm.',
  'Đang nguy hiểm: ở cạnh bạn ấy, cất đồ có thể gây hại ra xa, gọi 115 hoặc đưa tới cấp cứu.',
  'Chăm cả bản thân bạn. Kể với một người khác, gọi Ngày Mai nếu bạn cần được nghe.'],
 [lb('Đã xác nhận', f'Nghiên cứu có nhóm so sánh ở 9 phòng cấp cứu (khoảng 1.200 người ở 5 nơi làm can thiệp): nhóm có kế hoạch an toàn kèm gọi điện theo dõi có hành vi tự tử ít hơn khoảng một nửa ({STAN}).'),
  lb('Đã xác nhận', f'WHO nêu hạn chế tiếp cận phương tiện tự tử, như thuốc trừ sâu và một số thuốc, là biện pháp hiệu quả; năm 2021 khoảng 727.000 người chết do tự tử ({WSUI}).'),
  lb('Đã xác nhận', f'Tổng quan 13 nghiên cứu: hỏi về ý nghĩ tự tử không làm ý nghĩ đó tăng lên ({DAZZI}).'),
  lb('Suy luận', 'Thử nghiệm trên có nhân viên y tế lập kế hoạch và gọi điện theo dõi. Tự viết kế hoạch một mình chưa được thử nghiệm.'),
  lb('Đánh giá chuyên môn', 'Kế hoạch giữ vững 6 bước do daynentang.com viết lại theo ý của các mẫu kế hoạch an toàn; không chép mẫu có bản quyền.'),
  lb('Đã xác nhận', f'Ngày Mai 096 306 1414 ({NM}); Tổng đài 111 ({T111}). Tra 28/10/2026, kiểm tra lại mỗi quý.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi chấm nhiệt kế tâm trí', 'Tôi gọi tên cảm xúc, thở chậm', 'Tôi neo lại khi cảm xúc dâng cao', 'Tôi làm việc nhỏ có ý nghĩa mỗi ngày',
         'Tôi giữ giờ dậy cố định', 'Tôi dùng giờ lo', 'Tôi giải quyết vấn đề theo bước', 'Tôi mở lời với người tin cậy',
         'Tôi đổi một cách làm dịu có hại', 'Tôi có Kế hoạch giữ vững']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
PLAN_ROWS = [('1. Dấu hiệu báo trước của tôi', 3), ('2. Việc tôi tự làm để dịu xuống', 3), ('3. Người, nơi giúp tôi đổi không khí', 2),
             ('4. Người tôi nói thật được (tên, số gọi)', 3), ('5. Nơi giúp', 0), ('6. Làm chỗ ở an toàn hơn (nhờ ai giữ hộ gì)', 2),
             ('Điều quan trọng giúp tôi đi tiếp', 2)]
def plan_block():
    out = ''
    for lab, n in PLAN_ROWS:
        if n == 0:
            out += ('<h3>5. Nơi giúp</h3><div class="table-wrap"><table><tbody>'
                    '<tr><th class="w38">115</th><td>Cấp cứu y tế – khi nguy hiểm ngay</td></tr>'
                    '<tr><th>Khoa cấp cứu gần nhất</th><td></td></tr>'
                    '<tr><th>096 306 1414</th><td>Đường dây Ngày Mai (13:00–20:30, thứ Tư – Chủ nhật)</td></tr>'
                    '<tr><th>111</th><td>Dưới 18 tuổi (24/7)</td></tr>'
                    '<tr><th>Nhân viên y tế của tôi</th><td></td></tr></tbody></table></div>')
        else:
            out += f'<h3>{lab}</h3>' + lines([str(i) for i in range(1, n + 1)])
    return out

page(TOOL, 'Sổ chăm tâm trí', 'Trang in cho khóa Chăm tâm trí cơ bản: nhiệt kế tâm trí, cảm xúc, neo lại, việc nhỏ, nhật ký ngủ, giờ lo, giải quyết vấn đề, vòng người có thể nhờ, câu Nếu… thì…, Kế hoạch giữ vững.',
f'''
<h1>Sổ chăm tâm trí</h1>
<p>Dùng cho khóa <a href="{U}">Chăm tâm trí cơ bản</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Giữ sổ ở chỗ riêng tư.</p>
{CRISIS}
{PRINT_ROW}
<h2>1. Nhiệt kế tâm trí 14 tối (bài 1)</h2>
<p>0 = rất tệ · 10 = rất ổn. Để tự theo dõi, không dùng để chẩn đoán.</p>
{table(['Mục'] + [str(d) for d in range(1, 15)], [[m] + [''] * 14 for m in THERMO])}
<h2>2. Cảm xúc và thở chậm (bài 2)</h2>
{table(['Ngày'] + DAYS, [['Mình đang thấy…'] + [''] * 7, ['Thở chậm ✓'] + [''] * 7])}
<h2>3. Neo lại (bài 3)</h2>
<p>Chậm lại – Để ý – Quay về. Hoặc gọi tên 5 thấy · 4 chạm · 3 nghe · 2 ngửi · 1 hơi thở.</p>
{table(['Lần', 'Chuyện gì', 'Trước (0–10)', 'Sau (0–10)'], [['1', '', '', ''], ['2', '', '', ''], ['3', '', '', '']])}
<h2>4. Việc nhỏ có ý nghĩa (bài 4)</h2>
{table(['Chăm thân', 'Có ích', 'Kết nối', 'Vui nhỏ'], [['', '', '', ''], ['', '', '', '']])}
{table(['Ngày'] + DAYS, [['Việc'] + [''] * 7, ['Vui (0–10)'] + [''] * 7, ['Làm được (0–10)'] + [''] * 7])}
<h2>5. Nhật ký ngủ (bài 5)</h2>
{lines(['Giờ dậy cố định'])}
{table(['Ngày'] + DAYS, [['Lên giường'] + [''] * 7, ['Dậy'] + [''] * 7, ['Ngủ ngon (0–10)'] + [''] * 7])}
<h2>6. Giờ lo 15 phút (bài 6)</h2>
{lines(['Giờ lo của tôi', 'Câu: "Mình đang có ý nghĩ rằng…"'])}
{table(['Ý lo', 'Làm được gì không?', 'Việc nhỏ đầu tiên'], [['', '', ''], ['', '', ''], ['', '', '']])}
<h2>7. Giải quyết vấn đề (bài 7)</h2>
{lines(['1. Vấn đề', '2. Các cách', '3. Cách chọn', '4. Bước nhỏ, ngày giờ', '5. Kết quả'])}
<h2>8. Vòng người có thể nhờ (bài 8)</h2>
{table(['Vòng', 'Người hoặc nơi', 'Số gọi'], [['Trong', '', ''], ['Giữa', '', ''], ['Ngoài', '', '']])}
<h2>9. Nếu… thì… (bài 9)</h2>
{lines(['Nếu …', 'thì tôi …'])}
<h2>10. Kế hoạch giữ vững (bài 10)</h2>
<p>Viết lúc bình tĩnh. Dùng từ trên xuống. <strong>Nguy hiểm ngay: gọi 115 hoặc tới cấp cứu, ở cạnh một người.</strong></p>
{plan_block()}
<p class="small">Chụp ảnh trang này lưu trong điện thoại. Đưa một người tin cậy xem.</p>
<h2>Tự theo dõi (bài 1 và bài 10)</h2>
<p>0 = chưa làm · 1 = làm 1–3 ngày trong tuần · 2 = làm từ 4 ngày trở lên.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Bài 1</th><th>Bài 10</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Sổ để tự theo dõi, không dùng để chẩn đoán. Kế hoạch giữ vững không thay thế khám và điều trị.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Chăm tâm trí cơ bản', 'Khóa tự học miễn phí cho người từ 15 tuổi đang căng thẳng, buồn, lo kéo dài: gọi tên cảm xúc, neo lại, việc nhỏ có ý nghĩa, giấc ngủ, lo lắng, giải quyết vấn đề, kết nối, Kế hoạch giữ vững.',
f'''
<p class="eyebrow">Cá nhân · Khóa C8 · Đang thử nghiệm</p>
<h1>Chăm tâm trí cơ bản</h1>
<p class="lead">Mười kỹ năng nhỏ để chăm tâm trí mỗi ngày, và biết lúc nào cần người giúp.</p>
{CRISIS}
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn có vài kỹ năng tự chăm tâm trí dùng được ngay; biết dấu hiệu cần đi khám; có người để nhờ và một Kế hoạch giữ vững</td></tr>
<tr><th>Dành cho</th><td>Người từ 15 tuổi đang căng thẳng, buồn hoặc lo kéo dài, và người thân của họ. Bạn 15–17 tuổi học cùng người lớn tin cậy</td></tr>
<tr><th>Không dành cho</th><td>Thay thế khám, điều trị. Đang có ý nghĩ tự tử, đang khủng hoảng: hãy gọi 115 hoặc tới cấp cứu trước</td></tr>
<tr><th>Thời lượng</th><td>10 bài, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, ghi lại 5 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút hoặc Sổ chăm tâm trí in sẵn; một người tin cậy nếu có</td></tr>
<tr><th>Tình trạng</th><td>Đủ 10 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của bác sĩ tâm thần, nhà tâm lý lâm sàng, nhân viên công tác xã hội</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn có 2 cách dịu xuống khi cảm xúc dâng cao: thở chậm và neo lại.</li><li>Mỗi ngày bạn làm 1 việc nhỏ có ý nghĩa.</li><li>Bạn biết dấu hiệu cần đi khám và số cần gọi.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: cảm xúc là tín hiệu; ý nghĩ chưa chắc là sự thật; nhờ giúp là mạnh, không phải yếu.</li><li>Kỹ năng: làm trước, hứng thú đến sau; giải quyết vấn đề từng bước.</li><li>Một Kế hoạch giữ vững dùng được nhiều năm.</li></ul></div>
</div>
{figure_block('KHOAP')}

<h2 id="muoi-bai">Mười bài</h2>
<div class="table-wrap"><table>
<thead><tr><th>Bài</th><th>Tên</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ chăm tâm trí</a>: nhiệt kế tâm trí 14 tối, cảm xúc, neo lại, việc nhỏ, nhật ký ngủ, giờ lo, giải quyết vấn đề, vòng người có thể nhờ, câu "Nếu… thì…", Kế hoạch giữ vững, tự theo dõi.</li></ul>

<h2>Cho người đồng hành</h2>
<ul>
<li>Nghe nhiều, khuyên ít. Không nói "cố lên", "nghĩ tích cực đi".</li>
<li>Rủ làm việc nhỏ cùng nhau; khen việc đã làm.</li>
<li>Lo người thân có ý nghĩ tự tử: hỏi thẳng, ở cạnh, gọi 115 khi nguy hiểm. Xem bài 10.</li>
<li>Chăm cả bản thân bạn.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{DWM}; {SHP}</td><td>Neo lại, gỡ khỏi ý nghĩ khó, sống theo điều mình coi trọng</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên theo cụm, 694 người, tác dụng nhỏ sau 3 tháng; có buổi nhóm có người dẫn</td></tr>
<tr><td>{EKERS}; {WDEP}</td><td>Việc nhỏ có ý nghĩa (kích hoạt hành vi)</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp 26 thử nghiệm; WHO liệt kê là liệu pháp hiệu quả</td></tr>
<tr><td>{PMP}</td><td>Giải quyết vấn đề, kết nối (chỉ mượn ý)</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên, 346 người, có người hướng dẫn</td></tr>
<tr><td>{AASMI}; {AASMA}; {AASM}</td><td>Giờ dậy cố định, giường để ngủ, thời lượng ngủ</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn lâm sàng và đồng thuận chuyên gia</td></tr>
<tr><td>{STAN}; {WSUI}; {DAZZI}</td><td>Kế hoạch giữ vững, làm chỗ ở an toàn hơn, hỏi thẳng</td><td><span class="label">[Đã xác nhận]</span> Nghiên cứu có nhóm so sánh ở phòng cấp cứu; tờ thông tin WHO; tổng quan 13 nghiên cứu</td></tr>
<tr><td>{HL}</td><td>Lý do có bài kết nối</td><td><span class="label">[Đã xác nhận]</span> Phân tích gộp 148 nghiên cứu (tương quan)</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các nghiên cứu trên phần lớn có người hướng dẫn: nhân viên y tế, người không chuyên được đào tạo, hoặc buổi nhóm. Khóa tự học này chưa được thử nghiệm, nên chúng tôi không hứa kết quả.</p>
  <p>Khóa không chẩn đoán, không điều trị, không thay thế bác sĩ hay nhà tâm lý. Nếu bạn đã đang điều trị, hãy dùng khóa như phần tập thêm và báo người điều trị.</p>
  <p>{DEEP}</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C8 built')
