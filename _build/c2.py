# Khóa C2 "Hiểu mình (13–17)" – trang khóa, 8 bài, công cụ "Hồ sơ hiểu mình".
# Người đọc chính dưới 18 tuổi: KHÔNG có nút Chia sẻ, KHÔNG thu dữ liệu.
import illus_c2  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/hieu-minh/'
TOOL = '/cong-cu/ho-so-hieu-minh/'
C1 = '/khoa-hoc/lon-len-an-toan/'
G4 = '/khoa-hoc/gia-dinh-10-14/'
VAL = '/cong-cu/phieu-gia-tri/'
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

# ---------- Nguồn ----------
CASEL = '<a href="https://casel.org/casel-sel-framework-11-2020/?view=1">CASEL – khung năng lực cảm xúc xã hội (2020)</a>'
NIMH = '<a href="https://www.nimh.nih.gov/health/publications/the-teen-brain-7-things-to-know">NIMH – The Teen Brain: 7 Things to Know</a>'
WHOA = '<a href="https://www.who.int/news-room/fact-sheets/detail/mental-health-of-adolescents">WHO – Sức khỏe tâm thần vị thành niên (1/9/2025)</a>'
YEAGER = '<a href="https://www.hks.harvard.edu/publications/national-experiment-reveals-where-growth-mindset-improves-achievement">Yeager et al. 2019, <em>Nature</em> 573</a>'
MB = '<a href="https://artscimedia.case.edu/wp-content/uploads/sites/141/2020/06/26110416/Macnamara-Burgoyne-2023.pdf">Macnamara &amp; Burgoyne 2023</a>'
GS = '<a href="https://kops.uni-konstanz.de/entities/publication/2e749bfb-8533-437c-8203-7e788c910c5f">Gollwitzer &amp; Sheeran 2006</a>'
DUCK = '<a href="https://www.socmot.uni-konstanz.de/node/94">Duckworth et al. 2011, <em>Educational Psychology</em> 31</a>'
SG = '<a href="https://www.gpb.org/news/2023/05/23/social-media-can-put-young-people-in-danger-us-surgeon-general-warns">khuyến cáo của Tổng Y sĩ Hoa Kỳ 2023 (NPR đưa tin)</a>'
AASM = '<a href="https://www.sciencedaily.com/releases/2016/06/160613122419.htm">AASM 2016</a>'
PA = '<a href="https://knowledge-for-policy.ec.europa.eu/health-promotion-knowledge-gateway/physical-activity-sedentary-behaviour-table-2a_en">khuyến nghị WHO (bảng tổng hợp của EU)</a>'
AAP = '<a href="https://healthychildren.org/English/family-life/Media/Pages/How-to-Make-a-Family-Media-Use-Plan.aspx">AAP – Kế hoạch dùng thiết bị gia đình</a>'
NM = '<a href="https://duongdaynongngaymai.vn/">duongdaynongngaymai.vn</a>'
T111 = '<a href="https://tongdai111.vn/">tongdai111.vn</a>'

REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài viết dựa trên nguồn giáo dục và y khoa, nhưng chưa được thầy cô hay chuyên viên tâm lý duyệt. Bài không thay thế bác sĩ hay nhà tâm lý.</p></div>')
PRIVATE = ('<p class="small muted">Trang này không có ô gửi bài và không lưu gì về bạn. Những gì bạn viết là của riêng bạn. '
           'Người lớn đồng hành (từ 18 tuổi) có thể góp ý ở trang <a href="/chia-se/?bai=chung#gui">Chia sẻ</a>, xin không ghi tên hay trường.</p>')
TALK = ('Đang nghĩ đến cái chết hay muốn làm đau bản thân: nói ngay với người lớn ở gần, gọi <strong>115</strong> nếu nguy hiểm. '
        'Tổng đài <strong>111</strong> hỗ trợ trẻ em, miễn phí, 24/7.')

L = {
 '1': (1, 'minh-la-ai', 'Bài 1', 'Mình là ai'),
 '2': (2, 'dieu-minh-coi-trong', 'Bài 2', 'Điều mình coi trọng'),
 '3': (3, 'cam-xuc-tuoi-moi-lon', 'Bài 3', 'Cảm xúc tuổi mới lớn'),
 '4': (4, 'nao-dang-lon-minh-dang-hoc', 'Bài 4', 'Não đang lớn, mình đang học'),
 '5': (5, 'cham-co-the-minh', 'Bài 5', 'Chăm cơ thể mình'),
 '6': (6, 'mang-xa-hoi-va-hinh-anh-ban-than', 'Bài 6', 'Mạng xã hội và hình ảnh bản thân'),
 '7': (7, 'muc-tieu-va-tro-ngai', 'Bài 7', 'Mục tiêu và trở ngại'),
 '8': (8, 'khi-nao-can-giup', 'Bài 8', 'Khi nào cần giúp, mình một năm tới'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn ghi được 3 điểm mạnh, mỗi điểm có 1 bằng chứng từ việc đã làm.'),
 (2, 'Bạn chọn 3 giá trị và làm 1 việc theo giá trị đó trong tuần.'),
 (3, 'Bạn ghi nhật ký cảm xúc 3 ngày và dùng thở chậm 1 phút ít nhất 1 lần.'),
 (4, 'Bạn phân tích 1 lần chưa được theo 4 câu hỏi và thử 1 cách mới.'),
 (5, 'Bạn ghi giờ ngủ 7 ngày và giữ giờ tắt máy ít nhất 5/7 tối.'),
 (6, 'Bạn đếm giờ dùng mạng 3 ngày và bỏ theo dõi ít nhất 1 nguồn làm mình thấy tệ hơn.'),
 (7, 'Bạn viết 1 mục tiêu theo 4 bước và 2 câu Nếu… thì….'),
 (8, 'Bạn viết 3 dấu hiệu cần nhờ giúp, 3 người tin cậy và thư gửi mình một năm sau.'),
]

def lesson(k, desc, goals, prep, read, do, talk, safety, selfq, adult, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    meta = [f'Tuần {w}', 'Đọc 10 phút', 'Làm 10 phút', 'Nói hoặc viết 5 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (5 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Làm (10 phút)', do),
        sec(5, 'Nói với người tin cậy hoặc viết (5 phút)', talk),
        sec(6, 'An toàn', ul(safety + [TALK])),
        sec(7, 'Tự đánh giá', selftab(selfq)),
        sec(8, 'Cho người lớn đồng hành (nếu có)', ul(adult)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Hiểu mình (13–17)</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('B' + k)}
{''.join(sections[figs_after:])}
{HELP_BOX}
{PRIVATE}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

# ======================= BÀI 1 =======================
STRENGTHS = ['chăm chỉ', 'trung thực', 'tử tế', 'hài hước', 'tò mò', 'kiên nhẫn', 'sáng tạo', 'công bằng', 'can đảm', 'biết ơn',
             'cẩn thận', 'biết lắng nghe', 'dẫn dắt nhóm', 'tự kiềm chế', 'giữ lời hứa', 'biết tha thứ', 'thích học hỏi', 'khéo tay',
             'bền bỉ', 'biết giúp người']
lesson('1', 'Khóa Hiểu mình, bài 1: tìm điểm mạnh của mình bằng bằng chứng từ việc đã làm và hỏi người khác thấy gì.',
 ['Ghi được <strong>3 điểm mạnh</strong>, mỗi điểm có <strong>1 bằng chứng</strong> từ việc bạn đã làm.',
  'Hỏi <strong>2 người</strong> "3 từ tả mình là gì?" và ghi lại.',
  'Chọn <strong>1 việc</strong> trong tuần để dùng một điểm mạnh.'],
 [f'In trang 1 của <a href="{TOOL}">Hồ sơ hiểu mình</a>, hoặc lấy một tờ giấy.', 'Một cây bút. 15 phút yên tĩnh.'],
 ['<strong>Hiểu mình là một kỹ năng.</strong> Nó gồm biết mình cảm thấy gì, coi trọng điều gì, mạnh ở đâu, còn thiếu gì.',
  '<strong>Điểm mạnh tính cách</strong> là cách bạn hay cư xử, như kiên nhẫn, tử tế, tò mò. Nó khác điểm số hay năng khiếu.',
  '<strong>Điểm mạnh cần bằng chứng.</strong> "Mình kiên nhẫn" chưa đủ. "Mình tự sửa xe đạp 2 tiếng không bỏ cuộc" mới là bằng chứng.',
  '<strong>Người khác thấy điều mình không thấy.</strong> Hỏi bạn thân, anh chị em, thầy cô: "3 từ tả mình là gì?"',
  '<strong>Điểm yếu cũng là thông tin,</strong> không phải bản án. Ai cũng có. Biết nó giúp bạn chọn cách học, cách làm hợp hơn.',
  '<strong>Bạn đang thay đổi.</strong> Tuổi 13–17 là lúc thử nhiều thứ. Điểm mạnh hôm nay có thể khác năm sau. Điều đó bình thường.',
  '<strong>Ba vòng của mình:</strong> việc mình giỏi, việc mình thích, việc có ích cho người khác. Chỗ giao nhau là gợi ý để thử thêm.'],
 '<p><strong>Bài 1: chọn điểm mạnh.</strong> Khoanh 3–5 từ đúng với bạn nhất. Thiếu thì tự thêm.</p>'
 '<p class="small">' + ' · '.join(STRENGTHS) + '</p>'
 + table(['Điểm mạnh', 'Bằng chứng: một lần mình đã làm', 'Dùng ở đâu tuần này?'], [['1. ', '', ''], ['2. ', '', ''], ['3. ', '', '']])
 + '<p><strong>Bài 2: hỏi người khác.</strong> Nhắn hoặc hỏi trực tiếp 2 người: <em>"Mình đang làm bài tập hiểu mình. Bạn tả mình bằng 3 từ được không?"</em></p>'
 + lines(['Người 1 nói', 'Người 2 nói', 'Điều làm mình bất ngờ']),
 ol(['Kể cho một người tin cậy 3 điểm mạnh và bằng chứng của bạn.', 'Hỏi họ: "Bố/mẹ thấy con mạnh nhất ở đâu?"',
     'Không có ai để nói hôm nay? Viết 3 câu: "Mình tự hào vì…".']),
 ['Chỉ hỏi người bạn tin. Không đăng bài "hãy nhận xét về mình" lên mạng công khai.',
  'Nghe được nhận xét làm bạn buồn? Ghi lại, để một ngày rồi mới nghĩ tiếp. Bạn có quyền không đồng ý.'],
 ['Tôi ghi được 3 điểm mạnh có bằng chứng', 'Tôi đã hỏi 2 người', 'Tôi dùng 1 điểm mạnh trong tuần'],
 ['Khi con kể điểm mạnh, hãy nhắc lại bằng chứng cụ thể con đã nêu. Tránh khen chung chung.',
  'Kể một điểm mạnh của con mà con chưa nhận ra, kèm một việc con đã làm.',
  f'Bố mẹ có con 10–14 tuổi xem thêm khóa <a href="{G4}">Gia đình có con 10–14</a>.'],
 [lb('Đã xác nhận', f'Tự nhận thức gồm hiểu cảm xúc, suy nghĩ, giá trị của mình và nhận ra điểm mạnh, giới hạn ({CASEL}).'),
  lb('Suy luận', 'Hỏi người khác giúp thấy điểm mạnh mình chưa nhận ra. Chúng tôi chưa tìm được thử nghiệm đo riêng bài tập này.'),
  lb('Đánh giá chuyên môn', 'Danh sách 20 điểm mạnh, bảng bằng chứng và "ba vòng của mình" do daynentang.com soạn, chỉ mượn ý tưởng chung.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Hiểu mình, bài 2: chọn 3 giá trị của mình, biến giá trị thành việc làm, xử lý khi hai giá trị mâu thuẫn.',
 ['Chọn <strong>3 giá trị</strong> quan trọng nhất và viết vì sao.',
  'Làm <strong>1 việc</strong> theo một giá trị trong 7 ngày.',
  'Nghĩ được cách xử lý <strong>1 tình huống</strong> hai giá trị kéo hai phía.'],
 [f'In hoặc mở <a href="{VAL}">Phiếu giá trị</a> (20 thẻ giá trị) và trang 2 của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Kéo hoặc bút chì để đánh dấu.'],
 ['<strong>Giá trị</strong> là điều bạn coi trọng, dùng để chọn khi khó. Ví dụ: trung thực, gia đình, công bằng, học hỏi.',
  '<strong>Giá trị khác sở thích.</strong> Thích bóng đá là sở thích. Chơi đẹp, không ăn gian là giá trị.',
  '<strong>Giá trị của mình</strong> có thể giống hoặc khác bố mẹ một phần. Lớn lên là lúc tự xem lại, không phải chép lại.',
  '<strong>Giá trị thấy qua việc làm.</strong> Nói "mình trung thực" dễ. Nhận lỗi khi không ai biết mới khó.',
  '<strong>Hai giá trị có thể kéo hai phía.</strong> Muốn trung thực về điểm kém, nhưng sợ bố mẹ buồn.',
  '<strong>Cách giữ cả hai:</strong> nói thật, chọn lúc phù hợp, và mang theo kế hoạch sửa. Không có đáp án hoàn hảo.',
  '<strong>Áp lực nhóm</strong> thử giá trị của bạn rõ nhất. Biết trước mình coi trọng gì giúp bạn chọn nhanh hơn khi bị rủ rê.'],
 '<p><strong>Bài 1: lọc giá trị.</strong> Từ 20 thẻ, chọn 8. Từ 8, chọn 3. Viết vào bảng.</p>'
 + table(['Giá trị', 'Vì sao quan trọng với mình (1–2 câu)', 'Một việc làm tuần này'], [['1. ', '', ''], ['2. ', '', ''], ['3. ', '', '']])
 + '<p><strong>Bài 2: tình huống (giả định).</strong> Bạn thân nhờ cho chép bài kiểm tra. Giá trị nào kéo hai phía? Bạn sẽ nói gì?</p>'
 + lines(['Giá trị A', 'Giá trị B', 'Câu mình sẽ nói']),
 ol(['Kể cho người tin cậy 3 giá trị và vì sao bạn chọn.', 'Hỏi: "Hồi bằng tuổi con, bố/mẹ coi trọng điều gì? Giờ còn giữ không?"',
     'Hoặc viết: "Một lần mình đã sống đúng giá trị là…"']),
 ['Không ai được ép bạn làm việc sai với giá trị và pháp luật, kể cả bạn thân hay người lớn.',
  f'Bị đe dọa hay ép buộc: dừng, rời đi, kể người lớn. Xem bài 4 và 6 khóa <a href="{C1}">Lớn lên an toàn</a>.'],
 ['Tôi chọn được 3 giá trị và viết vì sao', 'Tôi làm 1 việc theo giá trị', 'Tôi có câu trả lời cho tình huống mâu thuẫn'],
 ['Nghe con kể giá trị trước, chưa sửa ngay. Hỏi "vì sao con chọn?"',
  'Kể một lần bố mẹ phải chọn giữa hai giá trị, và mình đã chọn thế nào.',
  'Giá trị con khác bố mẹ một phần là bình thường ở tuổi này.'],
 [lb('Đã xác nhận', f'Kết nối cảm xúc, giá trị và suy nghĩ; trung thực và có nguyên tắc là một phần của tự nhận thức ({CASEL}).'),
  lb('Cần kiểm chứng', 'Hiệu quả của bài viết "khẳng định giá trị" cho học sinh: kết quả các nghiên cứu không đồng nhất. Bài này không hứa kết quả học tập.'),
  lb('Đánh giá chuyên môn', 'Cách lọc 20 → 8 → 3 và tình huống mâu thuẫn do daynentang.com soạn, dùng lại Phiếu giá trị của khóa Giá trị nhà mình.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Hiểu mình, bài 3: gọi tên cảm xúc, nhiệt kế cảm xúc 1–5, chuỗi Chuyện – Nghĩ – Cảm – Làm, thở chậm 1 phút.',
 ['Gọi tên cảm xúc và chấm mức <strong>1–5</strong> trên nhiệt kế cảm xúc.',
  'Ghi <strong>nhật ký cảm xúc 3 ngày</strong> theo chuỗi Chuyện – Nghĩ – Cảm – Làm.',
  'Dùng <strong>thở chậm 1 phút</strong> ít nhất 1 lần khi cảm xúc ở mức 4–5.'],
 [f'In trang 3 của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Đồng hồ hoặc đếm nhẩm để thở 1 phút.'],
 ['<strong>Cảm xúc nào cũng bình thường:</strong> vui, buồn, giận, sợ, lo, xấu hổ, ghen tị, cô đơn. Việc mình làm với nó mới quan trọng.',
  '<strong>Tuổi teen cảm xúc mạnh hơn.</strong> Não đang thay đổi. Tuổi này cũng có thể phản ứng với căng thẳng khác người lớn.',
  '<strong>Gọi đúng tên</strong> giúp bạn hiểu mình. "Mình đang thất vọng" rõ hơn "mình bực".',
  '<strong>Nhiệt kế 1–5:</strong> 1 bình yên, 3 rõ ràng, 5 bùng nổ. Mức 4–5 thì chưa nên nói hay nhắn gì quan trọng.',
  '<strong>Cơ thể báo trước:</strong> tim nhanh, mặt nóng, tay nắm chặt, bụng thắt lại. Nhận ra sớm thì dễ bình tĩnh hơn.',
  '<strong>Chuỗi cảm xúc:</strong> Chuyện xảy ra → Mình nghĩ gì → Mình cảm thấy → Mình làm gì. Đổi một câu nghĩ có thể đổi cả chuỗi.',
  '<strong>Thở chậm 1 phút:</strong> hít vào đếm 4, thở ra đếm 6. Làm 5–6 lần. Đây là kỹ năng ngắn, không phải chữa bệnh.',
  '<strong>Muốn đi sâu</strong> về thiền và rèn tâm? Phần chuyên sâu sẽ có ở trang chị em tamhonkhoe.com.'],
 '<p><strong>Nhật ký cảm xúc 3 ngày.</strong> Mỗi tối ghi một chuyện làm cảm xúc mạnh nhất.</p>'
 + table(['Ngày', 'Chuyện', 'Mình nghĩ', 'Cảm xúc, mức 1–5', 'Mình làm', 'Câu nghĩ khác có thể'],
         [['1', '', '', '', '', ''], ['2', '', '', '', '', ''], ['3', '', '', '', '', '']])
 + '<p><strong>Tập ngay:</strong> thở chậm 1 phút. Ghi mức cảm xúc trước: …… sau: ……</p>',
 ol(['Kể cho người tin cậy một chuyện trong nhật ký, chỉ chuyện bạn muốn kể.', 'Hỏi: "Khi giận, bố/mẹ làm gì để bình tĩnh?"',
     'Hoặc viết: "Lần tới gặp chuyện giống vậy, mình sẽ…"']),
 ['Nhật ký là của riêng bạn. Cất ở chỗ riêng. Không chụp đăng lên mạng.',
  'Cảm xúc mạnh kéo dài nhiều tuần, hoặc bạn khó làm việc hằng ngày: nói với người lớn tin cậy. Xem bài 8.'],
 ['Tôi gọi tên và chấm mức cảm xúc được', 'Tôi ghi nhật ký 3 ngày', 'Tôi đã thử thở chậm 1 phút'],
 ['Khi con đang ở mức 4–5, chưa giảng giải. Đợi con bình tĩnh rồi mới nói chuyện.',
  'Nói tên cảm xúc của chính mình trước con: "Bố đang lo vì…". Con học từ cách bố mẹ làm.',
  'Không đòi đọc nhật ký của con. Con kể thì nghe, không phán xét.'],
 [lb('Đã xác nhận', f'Gọi tên cảm xúc và nối cảm xúc với suy nghĩ là một phần của tự nhận thức ({CASEL}).'),
  lb('Đã xác nhận', f'Tuổi teen có thể phản ứng với căng thẳng khác người lớn; nhận ra tác nhân và dùng cách ứng phó có ích ({NIMH}).'),
  lb('Đã xác nhận', f'WHO khuyến nghị xây kỹ năng ứng phó, giải quyết vấn đề và quản lý cảm xúc cho vị thành niên ({WHOA}).'),
  lb('Đánh giá chuyên môn', 'Nhiệt kế 1–5, chuỗi Chuyện – Nghĩ – Cảm – Làm và nhịp thở 4–6 do daynentang.com soạn. Đây là kỹ năng ngắn, không phải liệu pháp.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Hiểu mình, bài 4: não tuổi teen đang thay đổi, học từ một lần chưa được bằng 4 câu hỏi và đổi cách làm.',
 ['Nói được <strong>2 điều</strong> về não tuổi teen.',
  'Phân tích <strong>1 lần chưa được</strong> bằng 4 câu hỏi.',
  'Thử <strong>1 cách mới</strong> trong 7 ngày và ghi kết quả.'],
 [f'In trang 4 của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Nghĩ trước một lần gần đây bạn làm chưa được: bài kiểm tra, trận đấu, việc nhà.'],
 ['<strong>Não tuổi teen đang được "tinh chỉnh".</strong> Não không lớn thêm về kích thước, nhưng đang sắp xếp lại cách làm việc.',
  '<strong>Vùng trước trán</strong> lo lập kế hoạch, cân nhắc, ra quyết định. Vùng này hoàn thiện muộn, khoảng giữa đến cuối tuổi 20.',
  '<strong>Vì vậy</strong> tuổi teen dễ bị bạn bè và cảm giác hào hứng kéo đi. Biết điều này giúp bạn dừng lại một nhịp trước khi chọn.',
  '<strong>Não thay đổi theo việc bạn luyện.</strong> Học khó, vận động, làm việc sáng tạo đều làm các mạch não mạnh hơn.',
  '<strong>Chỉ nghĩ "mình có thể tiến bộ" là chưa đủ.</strong> Nghiên cứu cho thấy niềm tin đó một mình có tác dụng nhỏ.',
  '<strong>Điều giúp thật:</strong> đổi cách làm, luyện đều, và hỏi người giỏi hơn. "Cố hơn" mà vẫn làm cách cũ thường không đủ.',
  '<strong>Bốn câu hỏi sau một lần chưa được:</strong> Chuyện gì xảy ra? Cách cũ thiếu gì? Lần tới thử cách nào? Hỏi ai?'],
 '<p><strong>Phân tích một lần chưa được.</strong></p>'
 + lines(['Chuyện gì xảy ra?', 'Cách cũ thiếu gì? (thời gian, cách học, ngủ, hỏi bài…)', 'Lần tới thử cách nào?', 'Hỏi ai? Hỏi câu gì?'])
 + '<p><strong>Thử 7 ngày.</strong> Ghi cách mới bạn thử và kết quả.</p>'
 + table(['Ngày', 'Mình đã thử', 'Kết quả, điều học được'], [['', '', ''], ['', '', ''], ['', '', '']]),
 ol(['Kể cho người tin cậy lần chưa được và cách mới bạn sẽ thử.', 'Hỏi: "Có lần nào bố/mẹ thất bại rồi tìm ra cách khác không?"',
     'Hoặc viết: "Điều mình học được từ lần đó là…"']),
 ['Thất bại một lần không nói lên bạn là ai. Nhưng nếu bạn tự chê mình nặng nề nhiều ngày, hãy nói với người tin cậy.',
  'Không thức khuya quá giờ ngủ để "cố hơn". Thiếu ngủ làm việc học khó hơn (xem bài 5).'],
 ['Tôi nói được 2 điều về não tuổi teen', 'Tôi phân tích 1 lần chưa được', 'Tôi thử 1 cách mới trong 7 ngày'],
 ['Khen cách con làm và cách con đổi chiến lược, không chỉ khen "con thông minh".',
  'Khi con chưa được, hỏi "con sẽ thử cách nào?" trước khi góp ý.',
  'Kể một lần bố mẹ thất bại và học được gì.'],
 [lb('Đã xác nhận', f'Tuổi teen là giai đoạn não tinh chỉnh; vùng trước trán hoàn thiện ở khoảng giữa đến cuối tuổi 20; não thích nghi theo luyện tập ({NIMH}).'),
  lb('Đã xác nhận', f'Một bài học trực tuyến dưới 1 giờ về tư duy phát triển tăng điểm cho học sinh THPT học lực thấp hơn ở Mỹ ({YEAGER}). Mức tăng nhỏ.'),
  lb('Đã xác nhận', f'Tổng hợp các nghiên cứu: can thiệp tư duy phát triển có hiệu quả trung bình rất nhỏ ({MB}). Vì vậy bài này dạy đổi cách làm cụ thể.'),
  lb('Đánh giá chuyên môn', 'Bốn câu hỏi sau một lần chưa được và bảng thử 7 ngày do daynentang.com soạn.')])

# ======================= BÀI 5 =======================
DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
sleep_rows = [[d, '', '', '', ''] for d in DAYS]
lesson('5', 'Khóa Hiểu mình, bài 5: ngủ 8–10 giờ, vận động 60 phút, giờ tắt máy, nhật ký ngủ 7 ngày.',
 ['Nói được <strong>giờ ngủ</strong> và <strong>giờ vận động</strong> khuyến nghị cho tuổi mình.',
  'Ghi <strong>nhật ký ngủ 7 ngày</strong>.',
  'Giữ <strong>giờ tắt máy</strong> đã chọn ít nhất <strong>5/7 tối</strong>.'],
 [f'In trang 5 của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Chọn sẵn giờ lên giường và giờ tắt máy (trước giờ lên giường khoảng 1 giờ).'],
 ['<strong>Tuổi 13–18 cần ngủ 8–10 giờ</strong> mỗi đêm. Nhiều bạn ngủ ít hơn thế.',
  '<strong>Vì sao tuổi teen hay khó ngủ sớm?</strong> Chất gây buồn ngủ (melatonin) tăng muộn hơn vào buổi tối. Bạn không lười, cơ thể đang đổi nhịp.',
  '<strong>Thiếu ngủ</strong> làm khó tập trung, khó kiềm chế, và học kém đi.',
  '<strong>Vận động khoảng 60 phút mỗi ngày</strong> cho tuổi 5–17: đi bộ nhanh, đạp xe, chơi bóng, nhảy, làm việc nhà nặng.',
  '<strong>Ăn đều, đủ bữa, uống nước.</strong> Bỏ bữa làm bạn mệt và dễ cáu.',
  '<strong>Điện thoại và giấc ngủ:</strong> đặt giờ tắt máy, sạc máy ngoài phòng ngủ. Bố mẹ cũng có thể làm cùng.',
  '<strong>Giữ giờ dậy đều</strong>, kể cả cuối tuần. Lệch quá nhiều làm thứ Hai khó dậy hơn.'],
 f'<p>Giờ lên giường của tôi: …… · Giờ tắt máy: …… · Giờ dậy: ……</p>'
 + table(['Ngày', 'Lên giường', 'Dậy', 'Số giờ ngủ', 'Giữ giờ tắt máy? ✓'], sleep_rows)
 + '<p><strong>Vận động:</strong> ghi số phút mỗi ngày. Tổng 7 ngày: ……</p>',
 ol(['Cùng người lớn thống nhất chỗ sạc điện thoại ban đêm ngoài phòng ngủ.', 'Rủ một người trong nhà vận động cùng 3 lần trong tuần.',
     'Hoặc viết: "Điều làm mình khó ngủ sớm nhất là… Mình sẽ thử…"']),
 ['Ngáy to, ngừng thở khi ngủ, mất ngủ kéo dài nhiều tuần: nhờ bố mẹ đưa đi khám.',
  'Không tự dùng thuốc ngủ, nước tăng lực hay chất kích thích để thức học.',
  'Vận động mới: tăng dần, uống đủ nước, dừng khi đau ngực, choáng, khó thở.'],
 ['Tôi biết giờ ngủ và vận động khuyến nghị', 'Tôi ghi nhật ký ngủ 7 ngày', 'Tôi giữ giờ tắt máy ít nhất 5/7 tối'],
 ['Cả nhà cùng có giờ tắt máy và chỗ sạc chung ngoài phòng ngủ. Con dễ làm hơn khi bố mẹ làm cùng.',
  f'Làm kế hoạch dùng thiết bị cả nhà ({AAP}).', 'Không mắng con "lười" khi con khó dậy sớm. Cùng con chỉnh giờ dần, mỗi lần 15 phút.'],
 [lb('Đã xác nhận', f'Tuổi 13–18 cần ngủ 8–10 giờ mỗi 24 giờ ({AASM}).'),
  lb('Đã xác nhận', f'Melatonin ở tuổi teen tăng muộn hơn buổi tối; thiếu ngủ ảnh hưởng chú ý, kiềm chế và việc học ({NIMH}).'),
  lb('Đã xác nhận', f'Tuổi 5–17 nên vận động vừa đến mạnh trung bình khoảng 60 phút mỗi ngày ({PA}).'),
  lb('Đánh giá chuyên môn', 'Sạc máy ngoài phòng ngủ, giờ tắt máy trước khi ngủ khoảng 1 giờ, chỉnh giờ dần 15 phút là lời khuyên chung do daynentang.com soạn.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Hiểu mình, bài 6: mạng xã hội, so sánh, ảnh đã chỉnh, đếm giờ dùng và dọn nguồn theo dõi.',
 ['Đếm <strong>giờ dùng mạng xã hội</strong> trong 3 ngày.',
  'Tự hỏi <strong>"tốt hơn hay tệ hơn?"</strong> sau mỗi lần lướt, ghi lại.',
  'Bỏ theo dõi hoặc tắt thông báo <strong>ít nhất 1 nguồn</strong> làm mình thấy tệ hơn.'],
 [f'In trang 6 của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Nếu có điện thoại: tìm mục xem thời gian dùng ứng dụng trong phần cài đặt.'],
 ['<strong>Mạng xã hội có mặt tốt:</strong> giữ liên lạc, học điều mới, tìm bạn cùng sở thích.',
  '<strong>Và có rủi ro.</strong> Ở Mỹ, khoảng 95% bạn 13–17 tuổi dùng mạng xã hội; hơn một phần ba nói dùng "gần như liên tục".',
  '<strong>Dùng hơn 3 giờ mỗi ngày</strong> đi kèm nguy cơ có triệu chứng trầm cảm, lo âu cao gấp đôi. Đây là mối liên quan, chưa chứng minh là nguyên nhân.',
  '<strong>Ảnh đăng lên đã được chọn.</strong> Góc đẹp nhất, ánh sáng tốt, lọc màu, chỉnh sửa. Một khoảnh khắc, không phải cả ngày.',
  '<strong>So cả đời mình với ảnh đẹp nhất của người khác</strong> là so không công bằng. Cơ thể thật có mụn, có mệt, có thay đổi.',
  '<strong>Thuật toán đưa thêm thứ bạn hay xem.</strong> Xem nhiều nội dung làm bạn tự ti, bạn sẽ thấy nhiều hơn. Bạn chọn lại được.',
  '<strong>Bạn chọn được:</strong> bỏ theo dõi, tắt thông báo, đặt giờ, để máy xa khi học và khi ngủ.'],
 '<p><strong>Đếm 3 ngày.</strong> Ghi tổng giờ dùng mạng xã hội và cảm giác sau khi lướt.</p>'
 + table(['Ngày', 'Tổng giờ', 'Sau khi lướt: tốt hơn / như cũ / tệ hơn', 'Nguồn làm mình thấy tệ hơn'],
         [['1', '', '', ''], ['2', '', '', ''], ['3', '', '', '']])
 + '<p><strong>Dọn nguồn theo dõi:</strong> bỏ theo dõi 1 nguồn: …………… · Giữ lại 1 nguồn làm mình học được điều tốt: ……………</p>'
 + '<p><strong>Giới hạn của tôi:</strong> tối đa …… giờ mỗi ngày · không dùng khi: …………</p>',
 ol(['Kể cho người tin cậy con số 3 ngày và giới hạn bạn chọn.', 'Rủ người lớn cùng đếm giờ dùng của họ. So sánh vui, không trách nhau.',
     'Hoặc viết: "Nội dung làm mình thấy tốt là… Nội dung làm mình thấy tệ là…"']),
 ['Không gửi ảnh riêng tư cho ai. Bị đe dọa tung ảnh: không trả tiền, chụp lại, chặn, kể người lớn ngay.',
  'Bị bình luận chê bai cơ thể: không đáp trả, chặn, báo cáo, kể người lớn.',
  'Lo lắng nhiều về cân nặng, ăn uống hay ngoại hình: nói với người lớn tin cậy và nhờ đưa đi gặp bác sĩ.'],
 ['Tôi đếm giờ dùng 3 ngày', 'Tôi hỏi "tốt hơn hay tệ hơn" sau khi lướt', 'Tôi bỏ theo dõi ít nhất 1 nguồn'],
 ['Hỏi con thích gì trên mạng trước khi hỏi về giờ dùng.', 'Đặt giờ không máy chung: bữa cơm, trước khi ngủ. Bố mẹ làm gương.',
  'Không bình luận về cân nặng, ngoại hình của con hay người khác trước mặt con.'],
 [lb('Đã xác nhận', f'Khoảng 95% thiếu niên 13–17 ở Mỹ dùng mạng xã hội; dùng hơn 3 giờ/ngày đi kèm nguy cơ triệu chứng trầm cảm, lo âu gấp đôi ({SG}).'),
  lb('Suy luận', 'Số liệu trên là từ Mỹ và là mối liên quan, không chứng minh mạng xã hội gây ra trầm cảm. Chưa có số liệu tương đương cho Việt Nam mà chúng tôi kiểm chứng được.'),
  lb('Đã xác nhận', f'Khuyến cáo cũng nêu mạng xã hội có thể làm tăng bất mãn với cơ thể, nhất là ở bạn gái ({SG}).'),
  lb('Đánh giá chuyên môn', 'Bảng đếm 3 ngày, câu hỏi "tốt hơn hay tệ hơn" và dọn nguồn theo dõi do daynentang.com soạn.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Hiểu mình, bài 7: đặt mục tiêu theo 4 bước Mong muốn – Kết quả tốt nhất – Trở ngại – Nếu… thì….',
 ['Viết <strong>1 mục tiêu</strong> cho 4 tuần tới theo 4 bước.',
  'Viết <strong>2 câu Nếu… thì…</strong> cho trở ngại của mình.',
  'Làm theo kế hoạch và chấm <strong>số ngày làm được</strong> trong 7 ngày.'],
 [f'In trang 7 của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Nghĩ trước một điều bạn muốn trong 4 tuần tới: học, sức khỏe, gia đình, bạn bè.'],
 ['<strong>Mục tiêu tốt</strong> do chính bạn chọn, nhỏ đủ để làm được, và nói rõ làm gì, khi nào.',
  '<strong>Chỉ tưởng tượng thành công là chưa đủ.</strong> Cần nhìn thẳng vào trở ngại.',
  '<strong>Bốn bước:</strong> (1) Mong muốn. (2) Kết quả tốt nhất nếu đạt. (3) Trở ngại bên trong mình. (4) Kế hoạch Nếu… thì….',
  '<strong>Trở ngại bên trong</strong> là thứ thuộc về bạn: lười bắt đầu, dễ xem điện thoại, ngại hỏi. Không phải lỗi người khác.',
  '<strong>Câu Nếu… thì…</strong> gắn việc cần làm với một tình huống cụ thể. Ví dụ: "Nếu 20 giờ mà mình đang cầm điện thoại, thì mình để máy ngoài phòng và mở sách."',
  '<strong>Có bằng chứng:</strong> câu Nếu… thì… giúp người ta làm theo dự định tốt hơn. Một thử nghiệm nhỏ với học sinh THPT cho kết quả tương tự.',
  '<strong>Chậm nhưng đều</strong> tốt hơn làm nhiều rồi bỏ. Trượt một ngày thì làm lại ngày hôm sau.'],
 table(['Bước', 'Của tôi'], [['1. Mong muốn (4 tuần)', ''], ['2. Kết quả tốt nhất nếu đạt', ''], ['3. Trở ngại bên trong mình', ''],
                              ['4a. Nếu… thì…', 'Nếu ……………… thì ………………'], ['4b. Nếu… thì…', 'Nếu ……………… thì ………………']])
 + '<p><strong>Theo dõi 7 ngày:</strong> T2 ☐ · T3 ☐ · T4 ☐ · T5 ☐ · T6 ☐ · T7 ☐ · CN ☐</p>',
 ol(['Kể mục tiêu và câu Nếu… thì… cho người tin cậy.', 'Nhờ họ hỏi thăm bạn một lần vào cuối tuần.',
     'Hoặc viết: "Sau 7 ngày, điều giúp mình nhất là…"']),
 ['Không đặt mục tiêu ăn kiêng, nhịn ăn hay giảm cân nhanh. Lo về cân nặng thì hỏi bác sĩ cùng bố mẹ.',
  'Không đặt mục tiêu học bằng cách bỏ ngủ.'],
 ['Tôi viết 1 mục tiêu theo 4 bước', 'Tôi có 2 câu Nếu… thì…', 'Tôi làm theo ít nhất 4/7 ngày'],
 ['Để con tự chọn mục tiêu. Hỏi "điều gì có thể cản con?" thay vì đưa ra mục tiêu cho con.',
  'Hỏi thăm một lần mỗi tuần, ngắn. Khen việc làm đều, không chỉ kết quả.', 'Chia sẻ một mục tiêu của chính bố mẹ và câu Nếu… thì… của mình.'],
 [lb('Đã xác nhận', f'Kế hoạch Nếu… thì… có tác dụng từ vừa đến lớn lên việc đạt mục tiêu (tổng hợp 94 nghiên cứu, {GS}).'),
  lb('Đã xác nhận', f'66 học sinh THPT chuẩn bị kỳ thi: nhóm viết 30 phút về mục tiêu, trở ngại và câu Nếu… thì… làm nhiều bài luyện hơn nhóm chứng ({DUCK}).'),
  lb('Suy luận', 'Thử nghiệm học sinh là mẫu nhỏ ở Mỹ. Chưa có bằng chứng cho khóa tự học bằng tiếng Việt.'),
  lb('Đánh giá chuyên môn', 'Bảng 4 bước và bảng theo dõi 7 ngày do daynentang.com soạn, chỉ mượn ý tưởng từ nghiên cứu.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Hiểu mình, bài 8: dấu hiệu cần nhờ giúp, cách mở lời, người tin cậy, thư gửi mình một năm sau.',
 ['Viết <strong>3 dấu hiệu</strong> cho thấy mình nên nhờ giúp.',
  'Viết tên <strong>3 người tin cậy</strong> và một câu mở lời.',
  'Viết <strong>thư gửi mình một năm sau</strong> và chấm tự đánh giá cuối khóa.'],
 [f'In trang 8 và phần tự đánh giá của <a href="{TOOL}">Hồ sơ hiểu mình</a>.', 'Một phong bì hoặc tờ giấy gấp lại để cất thư.'],
 ['<strong>Khó khăn tâm lý khá phổ biến.</strong> Trên thế giới, khoảng 1 trong 7 người 10–19 tuổi có một rối loạn tâm thần. Lo âu và trầm cảm hay gặp nhất.',
  '<strong>Nhiều vấn đề bắt đầu ở tuổi teen.</strong> Phát hiện sớm thì dễ giúp hơn.',
  '<strong>Bình thường:</strong> buồn, lo, giận vài ngày rồi qua. Ai cũng có.',
  '<strong>Nên nói sớm khi:</strong> buồn hay lo kéo dài nhiều tuần; mất ngủ, bỏ ăn; không muốn gặp ai; không muốn đi học; tự chê mình nặng nề.',
  '<strong>Nói ngay khi:</strong> bạn nghĩ đến cái chết, muốn làm đau bản thân, hoặc bạn bè nói với bạn điều đó.',
  '<strong>Bạn bè kể với bạn ý muốn làm đau bản thân:</strong> đây là bí mật phải kể. Nói ngay với người lớn, kể cả khi bạn ấy dặn đừng kể.',
  '<strong>Cách mở lời:</strong> chọn người tin cậy, chọn lúc riêng, nói câu đầu: "Con cần nói chuyện, chuyện quan trọng." Rồi nói điều mình cần.',
  '<strong>Nhờ giúp là dũng cảm.</strong> Người đầu chưa hiểu? Nói với người thứ hai. Thầy cô, y tế trường, bác sĩ đều có thể giúp.'],
 '<p><strong>Bài 1: dấu hiệu của tôi.</strong> Ba dấu hiệu cho thấy tôi nên nhờ giúp:</p>'
 + lines(['Dấu hiệu 1', 'Dấu hiệu 2', 'Dấu hiệu 3'])
 + '<p><strong>Bài 2: người tin cậy và câu mở lời.</strong></p>'
 + lines(['Người 1', 'Người 2', 'Người 3 (ngoài nhà: thầy cô, y tế trường…)', 'Câu mở lời của tôi'])
 + '<p><strong>Bài 3: thư gửi mình một năm sau.</strong> Viết 5–8 câu: điểm mạnh, 3 giá trị, một điều đang lo, một mong muốn. Gấp lại, ghi ngày mở.</p>',
 ol(['Cùng người tin cậy đọc lại Hồ sơ hiểu mình. Chỉ đọc phần bạn muốn chia sẻ.', 'Cùng lưu các số khẩn cấp vào điện thoại.',
     'Kể một điều bạn hiểu thêm về mình sau 8 tuần.']),
 ['Đường dây Ngày Mai 096 306 1414 hỗ trợ người đang trầm cảm và người thân.'],
 ['Tôi viết 3 dấu hiệu cần nhờ giúp', 'Tôi có 3 người tin cậy và câu mở lời', 'Tôi viết thư gửi mình một năm sau'],
 ['Con mở lời: dừng việc đang làm, nghe hết, cảm ơn con đã nói. Không trách, không so sánh.',
  'Con nói về cái chết hay làm đau bản thân: ở bên con, không để con một mình, gọi 115 hoặc đưa con đến cơ sở y tế.',
  'Dấu hiệu kéo dài nhiều tuần: đưa con gặp bác sĩ hoặc chuyên gia tâm lý.'],
 [lb('Đã xác nhận', f'Khoảng 1 trong 7 người 10–19 tuổi có rối loạn tâm thần; lo âu, trầm cảm hay gặp ({WHOA}).'),
  lb('Đã xác nhận', f'Nhiều bệnh tâm thần như lo âu, trầm cảm có thể xuất hiện ở tuổi teen ({NIMH}).'),
  lb('Đã xác nhận', f'Đường dây Ngày Mai 096 306 1414 ({NM}). Tổng đài 111 bảo vệ trẻ em, miễn phí, 24/7 ({T111}). Tra 28/10/2026, kiểm tra lại mỗi quý.'),
  lb('Đánh giá chuyên môn', 'Danh sách dấu hiệu là tóm tắt chung, không dùng để chẩn đoán. Thư gửi mình và câu mở lời do daynentang.com soạn.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi biết 3 điểm mạnh có bằng chứng', 'Tôi biết 3 giá trị của mình', 'Tôi gọi tên và chấm mức cảm xúc được',
         'Tôi có 2 cách tự bình tĩnh', 'Khi chưa được, tôi đổi cách làm', 'Tôi ngủ đủ 8–10 giờ ít nhất 5/7 đêm',
         'Tôi tự chọn giờ dùng mạng xã hội', 'Tôi có 1 mục tiêu và câu Nếu… thì…', 'Tôi biết khi nào và với ai để nhờ giúp']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Hồ sơ hiểu mình', 'Trang in cho khóa Hiểu mình (13–17): điểm mạnh, giá trị, cảm xúc, giấc ngủ, mạng xã hội, mục tiêu, người tin cậy, tự đánh giá.',
f'''
<h1>Hồ sơ hiểu mình</h1>
<p>Dùng cho khóa <a href="{U}">Hiểu mình (13–17)</a>. Chỉ để in, trang không lưu dữ liệu của bạn.
Hồ sơ là của riêng bạn. Bạn chọn cho ai xem. Không chụp đăng lên mạng.</p>
{PRINT_ROW}
<h2>1. Điểm mạnh (bài 1)</h2>
{table(['Điểm mạnh', 'Bằng chứng'], [['1.', ''], ['2.', ''], ['3.', '']])}
<p>Người khác tả tôi bằng 3 từ: ……………………………………</p>
<h2>2. Giá trị (bài 2)</h2>
{table(['Giá trị', 'Vì sao', 'Việc làm'], [['1.', '', ''], ['2.', '', ''], ['3.', '', '']])}
<h2>3. Cảm xúc (bài 3)</h2>
<p>Nhiệt kế: 1 bình yên · 2 hơi có · 3 rõ ràng · 4 rất mạnh · 5 bùng nổ. Mức 4–5: dừng, thở trước.</p>
<p>Cơ thể tôi báo trước bằng: ……………………… · Hai cách tự bình tĩnh: 1. ……………… 2. ………………</p>
<h2>4. Một lần chưa được (bài 4)</h2>
{lines(['Chuyện gì xảy ra?', 'Cách cũ thiếu gì?', 'Cách mới', 'Hỏi ai?'])}
<h2>5. Kế hoạch ngủ (bài 5)</h2>
<p>Giờ tắt máy: …… · Lên giường: …… · Dậy: …… · Chỗ sạc điện thoại ban đêm: ……………</p>
<h2>6. Mạng xã hội (bài 6)</h2>
<p>Giới hạn mỗi ngày: …… giờ · Không dùng khi: ……………… · Đã bỏ theo dõi: ………………</p>
<h2>7. Mục tiêu (bài 7)</h2>
{table(['Bước', 'Của tôi'], [['Mong muốn', ''], ['Kết quả tốt nhất', ''], ['Trở ngại bên trong', ''], ['Nếu… thì…', '']])}
<h2>8. Khi cần giúp (bài 8)</h2>
{lines(['3 dấu hiệu của tôi', 'Người tin cậy 1', 'Người tin cậy 2', 'Người tin cậy 3', 'Câu mở lời'])}
<div class="table-wrap"><table><tbody>
<tr><th class="w38">111</th><td>Bảo vệ trẻ em, miễn phí, 24/7</td></tr>
<tr><th>115</th><td>Cấp cứu y tế</td></tr>
<tr><th>113</th><td>Công an, khi nguy hiểm ngay lúc đó</td></tr>
<tr><th>096 306 1414</th><td>Đường dây Ngày Mai, hỗ trợ người trầm cảm và người thân</td></tr>
</tbody></table></div>
<h2>9. Tự đánh giá (tuần 1 và tuần 8)</h2>
<p>0 = chưa · 1 = làm được một phần · 2 = làm được.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 8</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Phiếu để tự theo dõi, không dùng để chẩn đoán.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Hiểu mình (13–17)', 'Khóa tự học miễn phí cho bạn 13–17 tuổi: điểm mạnh, giá trị, cảm xúc, não tuổi teen, giấc ngủ, mạng xã hội, mục tiêu, khi nào cần giúp.',
f'''
<p class="eyebrow">Cá nhân · Khóa C2 · Đang thử nghiệm</p>
<h1>Hiểu mình (13–17)</h1>
<p class="lead">Bạn đang thay đổi nhanh. Khóa này giúp bạn biết mình mạnh ở đâu, coi trọng điều gì, cảm xúc vận hành ra sao, và tự chọn hướng đi.</p>
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn hiểu điểm mạnh, giá trị, cảm xúc của mình; chăm cơ thể; đặt mục tiêu có kế hoạch; biết nhờ giúp sớm</td></tr>
<tr><th>Dành cho</th><td>Bạn 13–17 tuổi tự học. Người lớn đồng hành là tùy chọn. Bạn 10–14 xem khóa <a href="{C1}">Lớn lên an toàn</a> trước</td></tr>
<tr><th>Thời lượng</th><td>8 tuần, mỗi tuần 1 bài 25 phút: đọc 10 phút, làm 10 phút, nói hoặc viết 5 phút</td></tr>
<tr><th>Cần có</th><td>Giấy, bút. Bài 6 có thể dùng điện thoại để xem giờ dùng ứng dụng</td></tr>
<tr><th>Tình trạng</th><td>Đủ 8 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của các bạn, gia đình và thầy cô</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn gọi tên được 3 điểm mạnh và 3 giá trị.</li><li>Bạn có giờ tắt máy và ngủ đủ hơn.</li><li>Bạn có một cách thở để bình tĩnh khi cảm xúc lên cao.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: quan sát mình, gọi tên, chọn một việc nhỏ, rồi xem lại.</li><li>Kỹ năng: đặt mục tiêu có kế hoạch vượt trở ngại.</li><li>Biết nhờ giúp sớm. Nhờ giúp là dũng cảm.</li></ul></div>
</div>
{figure_block('KHOAB')}

<h2 id="tam-tuan">Tám tuần</h2>
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Hồ sơ hiểu mình</a>: điểm mạnh, giá trị, cảm xúc, kế hoạch ngủ, mục tiêu, người tin cậy, tự đánh giá.</li>
<li><a href="{VAL}">Phiếu giá trị</a>: 20 thẻ giá trị (dùng ở bài 2).</li></ul>

<h2>Cho người lớn đồng hành (nếu có)</h2>
<ul>
<li>Tuổi này cần riêng tư. Không đòi đọc hồ sơ hay nhật ký của con. Con kể thì nghe.</li>
<li>Hỏi con học được gì, không kiểm tra bài như bài tập về nhà.</li>
<li>Làm cùng con các bài về giấc ngủ, mạng xã hội, mục tiêu. Con học từ cách bố mẹ làm.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{CASEL}</td><td>Tự nhận thức: cảm xúc, giá trị, điểm mạnh, mục đích</td><td><span class="label">[Đã xác nhận]</span> Khung năng lực dùng rộng ở trường học. Bằng chứng hiệu quả chủ yếu từ chương trình ở trường, có thầy cô dạy</td></tr>
<tr><td>{NIMH}</td><td>Kiến thức não tuổi teen, giấc ngủ, căng thẳng</td><td><span class="label">[Đã xác nhận]</span> Tài liệu của viện nghiên cứu nhà nước Mỹ</td></tr>
<tr><td>{GS}; {DUCK}</td><td>Mục tiêu, trở ngại, câu Nếu… thì…</td><td><span class="label">[Đã xác nhận]</span> Tổng hợp 94 nghiên cứu: tác dụng vừa đến lớn. Một thử nghiệm nhỏ với học sinh THPT</td></tr>
<tr><td>{YEAGER}; {MB}</td><td>Học từ sai lầm, đổi cách làm</td><td><span class="label">[Đã xác nhận]</span> Tác dụng nhỏ, rõ hơn ở học sinh học lực thấp hơn</td></tr>
<tr><td>{SG}</td><td>Mạng xã hội, hình ảnh bản thân</td><td><span class="label">[Đã xác nhận]</span> Khuyến cáo dựa trên nghiên cứu tương quan</td></tr>
<tr><td>{WHOA}; {AASM}</td><td>Dấu hiệu cần giúp, giấc ngủ, vận động</td><td><span class="label">[Đã xác nhận]</span> Tài liệu của WHO và đồng thuận chuyên gia</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Các chương trình có bằng chứng thường dạy ở trường, có thầy cô hướng dẫn. Khóa tự học này chưa được thử nghiệm và chưa có chuyên gia duyệt.
  Khóa không thay thế bác sĩ, nhà tâm lý hay điều trị. Phần tinh thần chuyên sâu (thiền, Khắc kỷ, Phật giáo) sẽ có ở trang chị em tamhonkhoe.com.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{TALK}</li><li>Trang này không có ô gửi bài và không lưu dữ liệu của bạn.</li></ul>
{HELP_BOX}
''', current='/ca-nhan/')
print('C2 built')
