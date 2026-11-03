# Khóa C9 "Vận động an toàn" – trang khóa, 10 bài, công cụ "Sổ vận động an toàn".
# Người đọc: người cao tuổi, người mới ốm dậy, người có bệnh mạn tính đã ổn định, người lớn ít vận động (từ 18 tuổi).
# Người đọc đều từ 18 tuổi: CÓ nút Chia sẻ (khóa c9-n trong chia-se.js).
# An toàn: mỗi bài có khối "Dừng tập ngay khi" ở đầu trang; mỗi động tác có 3 mức dễ – vừa – khó.
import illus_c9  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/van-dong-an-toan/'
TOOL = '/cong-cu/so-van-dong-an-toan/'
C7B5 = '/khoa-hoc/tu-lap-tung-buoc/tuan-5/an-toan-di-lai/'
G8 = '/khoa-hoc/nha-gon-nha-an-toan/'
C5 = '/khoa-hoc/15-phut-moi-ngay/'
C8 = '/khoa-hoc/cham-tam-tri-co-ban/'
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
def levels(rows):
    return table(['Động tác', 'Dễ', 'Vừa', 'Khó'], rows)
def selftab(items, a='Tuần này', b='Sau 2 tuần'):
    rows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in items)
    return ('<p>0 = chưa làm · 1 = làm 1–2 ngày trong tuần · 2 = làm từ 3 ngày trở lên. Đây là tự theo dõi, không phải chấm điểm bản thân.</p>'
            f'<div class="table-wrap"><table><thead><tr><th>Mục</th><th>{a}</th><th>{b}</th></tr></thead><tbody>{rows}</tbody></table></div>')

# ---------- Nguồn (đã tra 03/11/2026) ----------
WHO20 = '<a href="https://www.sydney.edu.au/news-opinion/news/2020/11/26/new-global-guidelines-on-physical-activity-and-sedentary-behavio.html">WHO 2020 – Hướng dẫn về vận động và hành vi tĩnh tại (công bố 26/11/2020 trên <em>BJSM</em>; Đại học Sydney tóm tắt)</a>'
WHOFS = '<a href="https://www.who.int/news-room/fact-sheets/detail/physical-activity">WHO – Vận động thể lực (tờ thông tin, 26/6/2024)</a>'
WHOAGE = '<a href="https://www.who.int/health-topics/ageing/physical-activity">WHO – Vận động ở người cao tuổi (trang chủ đề, 2/2018)</a>'
BYT = '<a href="https://daidoanket.vn/bo-y-te-ban-hanh-cam-nang-huong-dan-hoat-dong-the-luc-cho-cong-dong.html">Cục Phòng bệnh, Bộ Y tế – Cẩm nang hướng dẫn hoạt động thể lực, Quyết định 103/QĐ-PB ngày 13/7/2026 (báo Đại Đoàn Kết, 31/7/2026)</a>'
BYT2 = '<a href="https://baophapluat.vn/bo-y-te-khuyen-nghi-thoi-luong-van-dong-phu-hop-cho-tung-nhom-tuoi.html">Báo Pháp luật Việt Nam, 31/7/2026 (tóm tắt Cẩm nang của Bộ Y tế)</a>'
SHER = '<a href="https://pubmed.ncbi.nlm.nih.gov/30703272/">Sherrington et al. 2019, <em>Cochrane</em> – Tập luyện phòng té ngã ở người cao tuổi sống tại cộng đồng</a>'
PRT = '<a href="https://www.cochrane.org/evidence/CD002759_progressive-resistance-strength-training-improving-physical-function-older-people">Liu &amp; Latham, <em>Cochrane</em> CD002759 – Tập sức cơ tăng dần ở người cao tuổi</a>'
STEADI = '<a href="https://www.nj.gov/humanservices/doas/forms/STEADI-Assessment-30Sec-508.pdf">CDC STEADI – Phép thử đứng lên ngồi xuống 30 giây (bản đăng lại của bang New Jersey)</a>'
TALKT = '<a href="https://www.cdc.gov/physical-activity-basics/measuring/">CDC – Đo mức gắng sức, phép thử nói chuyện (4/12/2025)</a>'
NHSF = '<a href="https://www.nhs.uk/conditions/falls/">NHS – Té ngã (duyệt 6/3/2025)</a>'
NIA = '<a href="https://webarchive.library.unt.edu/web/20121002052225/http://go4life.nia.nih.gov/sites/default/files/StayingSafe.pdf">NIA Go4Life – Staying Safe (Viện Lão hóa Hoa Kỳ, bản lưu trữ 2012)</a>'
BANNER = '<a href="https://www.bannerhealth.com/healthcareblog/teach-me/heart-health-warning-signs-active-seniors-should-not-ignore">Banner Health, 18/9/2026 (bác sĩ tim mạch giải thích dấu hiệu cảnh báo)</a>'
WHOF = '<a href="https://www.who.int/news-room/fact-sheets/detail/falls">WHO – Té ngã (21/10/2026)</a>'

STOP = ('<div class="box warn"><p><strong>Dừng tập ngay khi:</strong> đau, tức ngực; khó thở nhiều; chóng mặt, choáng; tim đập rất nhanh hoặc loạn nhịp; '
        'đau nhói ở khớp. Ngồi xuống, gọi người ở gần. <strong>Đau ngực không đỡ, ngất, yếu nửa người, méo miệng, nói khó: gọi 115 ngay.</strong></p></div>')
REVIEW = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử, chưa có chuyên gia duyệt.</strong> '
          'Bài chưa được bác sĩ, chuyên viên vật lý trị liệu hay phục hồi chức năng duyệt. '
          'Khóa không thay thế khám bệnh hay chương trình phục hồi do nhân viên y tế chỉ định.</p></div>')
ASK = 'Có bệnh tim, vừa mổ, vừa ốm nặng, gãy xương, đột quỵ, hay chóng mặt, đường huyết chưa ổn: hỏi nhân viên y tế trước (xem bài 1).'
EMERG = 'Cấp cứu: <strong>115</strong>. Bạo lực trong gia đình: <strong>117</strong>. Buồn, lo kéo dài: Ngày Mai <strong>096 306 1414</strong>.'

L = {
 '1': (1, 'bat-dau-an-toan', 'Bài 1', 'Bắt đầu an toàn'),
 '2': (2, 'ngoi-it-lai', 'Bài 2', 'Ngồi ít lại, đứng dậy thường hơn'),
 '3': (3, 'tho-va-khoi-dong', 'Bài 3', 'Thở chậm và khởi động nhẹ'),
 '4': (4, 'suc-chan', 'Bài 4', 'Sức chân: đứng lên, ngồi xuống'),
 '5': (5, 'thang-bang', 'Bài 5', 'Thăng bằng có vịn ghế'),
 '6': (6, 'suc-tay', 'Bài 6', 'Sức tay và sức nắm'),
 '7': (7, 'di-bo-tang-dan', 'Bài 7', 'Đi bộ an toàn, tăng dần'),
 '8': (8, 'gian-co-khop', 'Bài 8', 'Giãn cơ, giữ khớp dễ cử động'),
 '9': (9, 'phong-te-nga', 'Bài 9', 'Phòng té ngã, đứng dậy sau khi ngã'),
 '10': (10, 'ke-hoach-tuan', 'Bài 10', 'Kế hoạch tuần của tôi'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')
PLAN = [
 (1, 'Bạn trả lời xong phiếu "Trước khi tập" và tập thử 5 phút trên ghế.'),
 (2, 'Bạn đứng dậy ít nhất 6 lần mỗi ngày, trong 5 ngày.'),
 (3, 'Bạn khởi động 5 phút trước mỗi buổi tập, 3 buổi trong tuần.'),
 (4, 'Bạn tập đứng lên – ngồi xuống 2 ngày trong tuần và ghi số lần đo 30 giây.'),
 (5, 'Bạn tập thăng bằng có vịn 3 ngày trong tuần.'),
 (6, 'Bạn tập co tay và đẩy tường 2 ngày trong tuần.'),
 (7, 'Bạn đi bộ ở mức "vừa" 5 ngày, mỗi tuần thêm vài phút.'),
 (8, 'Bạn giãn cơ sau khi đi bộ 3 ngày trong tuần.'),
 (9, 'Bạn kể được 6 bước đứng dậy sau khi ngã và sửa 1 chỗ dễ trượt trong nhà.'),
 (10, 'Bạn viết xong lịch tuần và đo lại 30 giây.'),
]

def lesson(k, desc, goals, prep, read, do, note, safety, selfq, helper, src, figs_after=3):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'c9-' + k
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn. '
             f'Xin không ghi tên thật, nơi ở hay bệnh của người khác.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về {code.lower()}</a></p></div>')
    meta = [f'Bài {w}', 'Đọc 10 phút', 'Tập 10 phút', 'Ghi lại 5 phút']
    sections = [
        sec(1, 'Sau bài này, bạn sẽ', ul(goals)),
        sec(2, 'Chuẩn bị (2 phút)', ul(prep)),
        sec(3, 'Đọc (10 phút)', ol(read)),
        sec(4, 'Tập (10 phút)', do),
        sec(5, 'Ghi lại (5 phút)', note),
        sec(6, 'An toàn', ul(safety + [ASK, EMERG])),
        sec(7, 'Tự theo dõi', selftab(selfq)),
        sec(8, 'Cho người đồng hành: con cháu, người chăm sóc, bạn tập', ul(helper)),
        sec(9, 'Nguồn và nhãn', ul(src))]
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Vận động an toàn</a> · Bài {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{STOP}
{REVIEW}
{PRINT_ROW}
{''.join(sections[:figs_after])}
{figure_block('X' + k)}
{''.join(sections[figs_after:])}
{share}
{HELP_BOX}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 03/11/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/ca-nhan/')

DAYS = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
ASKLIST = ['Tôi có bệnh tim, hoặc từng đau, tức ngực khi gắng sức',
           'Tôi vừa mổ, vừa ốm nặng, vừa nằm viện, hoặc vừa gãy xương',
           'Tôi từng bị đột quỵ, hoặc đang tập phục hồi theo chỉ định',
           'Tôi hay chóng mặt, từng ngất, hoặc vừa bị ngã',
           'Huyết áp hoặc đường huyết của tôi chưa ổn; tôi tiêm insulin hoặc uống thuốc hạ đường huyết',
           'Tôi có khớp mới sưng, nóng, đỏ, hoặc đau tăng khi nghỉ',
           'Tôi khó thở khi đi lại nhẹ, hoặc phù chân mới xuất hiện']

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Vận động an toàn, bài 1: vì sao nên vận động khi sức yếu; phiếu Trước khi tập; đèn xanh – vàng – đỏ; tập thử 5 phút trên ghế.',
 ['Trả lời xong phiếu <strong>"Trước khi tập"</strong> 7 câu.',
  'Nói được <strong>3 đèn</strong>: xanh tập tiếp, vàng chậm lại, đỏ dừng ngay.',
  'Tập thử <strong>5 phút trên ghế</strong> mà không thấy đèn đỏ.'],
 [f'In trang 1–2 của <a href="{TOOL}">Sổ vận động an toàn</a>, hoặc lấy giấy bút.', 'Một ghế chắc có lưng tựa, đặt sát tường.', 'Một cốc nước. Quần áo rộng, giày đế bám hoặc chân trần.'],
 ['Vận động giúp giữ sức đứng dậy, đi lại, tự làm việc nhà. <strong>Một ít vẫn hơn không vận động</strong>.',
  'Người ít vận động nên <strong>bắt đầu nhỏ</strong>, rồi tăng dần thời gian, số ngày và độ gắng sức.',
  'Người có bệnh mạn tính đã ổn định, như huyết áp cao hay tiểu đường, vẫn nên vận động <strong>trong sức của mình</strong>.',
  'Có bệnh tim, vừa ốm nặng, vừa mổ, hay chóng mặt: <strong>hỏi nhân viên y tế trước</strong> khi bắt đầu chương trình mới.',
  '<strong>Đèn xanh:</strong> thở nhanh hơn nhưng vẫn nói được câu. Tập tiếp.',
  '<strong>Đèn vàng:</strong> mỏi nhiều, đau cơ, hụt hơi. Chậm lại, xuống mức dễ hơn, nghỉ.',
  '<strong>Đèn đỏ:</strong> đau ngực, khó thở nhiều, chóng mặt, choáng. Dừng ngay, ngồi xuống, gọi người. Nặng thì gọi 115.',
  'Khóa có 4 loại vận động: <strong>sức cơ, thăng bằng, đi lại, linh hoạt</strong>. Mỗi động tác có 3 mức dễ – vừa – khó.'],
 '<p><strong>Phần 1: phiếu "Trước khi tập".</strong> Đánh dấu Có hoặc Không.</p>'
 + table(['Câu hỏi', 'Có', 'Không'], [[q, '', ''] for q in ASKLIST])
 + '<p>Có từ 1 ý "Có": mang phiếu đi hỏi nhân viên y tế trước. Trong lúc chờ, chỉ tập bài 2 (đứng dậy thường hơn) và bài 3 (thở chậm).</p>'
 + '<p><strong>Phần 2: tập thử 5 phút trên ghế</strong> (nếu tất cả là "Không").</p>'
 + levels([['Xoay vai', 'Ngồi, xoay 5 lần', 'Xoay 10 lần', 'Thêm đưa tay lên cao 5 lần'],
           ['Nhấc gót – mũi chân', 'Ngồi, 10 lần', '15 lần', '20 lần, chậm'],
           ['Bước tại chỗ khi ngồi', '1 phút', '2 phút', '2 phút, nhấc gối cao hơn']]),
 lines(['Hôm nay tôi tập … phút', 'Đèn tôi thấy: xanh / vàng / đỏ', 'Giờ tập hợp với tôi', 'Người tôi muốn rủ tập cùng']),
 ['Tập lúc no vừa, không tập ngay sau bữa ăn no.', 'Uống nước trước và sau khi tập, kể cả khi chưa khát.',
  'Trời nóng: tập trong nhà, chỗ thoáng mát, hoặc sáng sớm.'],
 ['Tôi biết 3 đèn tập luyện', 'Tôi tập trên ghế 5 phút', 'Tôi uống nước trước và sau khi tập'],
 ['Cùng đọc phiếu "Trước khi tập". Nếu có ý "Có", giúp đặt lịch khám và mang phiếu theo.',
  'Ngồi cạnh trong buổi tập đầu. Hỏi: "Đèn gì rồi?" thay vì "Cố lên".',
  'Khen việc đã làm: "Hôm nay tập đủ 5 phút rồi."'],
 [lb('Đã xác nhận', f'Một ít vận động vẫn tốt hơn không; người ít vận động nên bắt đầu nhỏ rồi tăng dần; người cao tuổi vận động trong mức sức khỏe cho phép; người có bệnh tim có thể cần hỏi ý kiến y tế trước ({WHOAGE}; {WHOFS}).'),
  lb('Đã xác nhận', f'Cẩm nang của Bộ Y tế: người bệnh mạn tính hỏi nhân viên y tế trước khi bắt đầu chương trình mới; dừng tập khi đau ngực, khó thở, chóng mặt ({BYT}). Chưa đọc văn bản gốc.'),
  lb('Đã xác nhận', f'Đau ngực kéo dài, khó thở, ngất, yếu đột ngột, méo mặt, nói khó là dấu hiệu cần dừng và gọi cấp cứu ({BANNER}).'),
  lb('Đánh giá chuyên môn', 'Phiếu "Trước khi tập" 7 câu và ba đèn do daynentang.com soạn để người tự học dễ dùng; không phải công cụ sàng lọc đã được kiểm định.')])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Vận động an toàn, bài 2: ngồi lì ít lại; mỗi giờ đứng dậy một lần; gắn việc đứng dậy với việc hằng ngày; câu Nếu… thì….',
 ['Đếm số lần <strong>đứng dậy</strong> trong một ngày.', 'Viết <strong>1 câu "Nếu… thì…"</strong> để đứng dậy thường hơn.',
  'Đứng dậy ít nhất <strong>6 lần mỗi ngày</strong>, trong 5 ngày.'],
 [f'In trang 3 của <a href="{TOOL}">Sổ vận động an toàn</a>.', 'Đồng hồ hoặc điện thoại có chuông nhắc.'],
 ['WHO khuyên <strong>mọi lứa tuổi hạn chế thời gian ngồi lì</strong>, thay bằng vận động nhẹ bất kỳ.',
  'Ngồi liền nhiều giờ khác với ngồi rồi đứng dậy thường xuyên. Đứng dậy là bước đầu, ai cũng làm được.',
  'Mọi vận động đều tính: <strong>quét nhà, tưới cây, đi chợ, phơi đồ</strong>.',
  'Cách dễ nhất: <strong>gắn với việc có sẵn</strong>. Nghe điện thoại thì đứng. Hết một tập phim thì đứng dậy đi vài bước.',
  'Câu "Nếu… thì…" giúp nhớ: "Nếu chuông báo giờ, thì tôi đứng dậy rót nước."',
  'Người phải nằm hay ngồi nhiều: co duỗi tay chân, xoay cổ chân ngay trên giường hoặc ghế cũng là vận động.',
  'Đứng dậy từ từ. Ngồi một lát ở mép giường hoặc ghế rồi mới đứng, nhất là buổi sáng.'],
 '<p><strong>Đếm lần đứng dậy</strong> trong 3 ngày. Mỗi lần đứng, vạch một gạch.</p>'
 + table(['Ngày', 'Sáng', 'Chiều', 'Tối', 'Tổng'], [['Ngày 1', '', '', '', ''], ['Ngày 2', '', '', '', ''], ['Ngày 3', '', '', '', '']])
 + levels([['Đứng dậy', 'Vịn ghế, đứng 10 giây rồi ngồi', 'Đứng, đi vài bước trong phòng', 'Đi lấy nước, đi một vòng nhà'],
           ['Khi nằm, ngồi nhiều', 'Xoay cổ chân 10 lần', 'Co duỗi gối 10 lần', 'Thêm co duỗi tay 10 lần']]),
 lines(['Nếu …', 'thì tôi …', 'Việc nhà tôi sẽ tự làm thêm']),
 ['Đứng dậy chậm; chóng mặt khi đứng thì ngồi lại ngay và báo nhân viên y tế.', 'Bật đèn khi đứng dậy ban đêm.'],
 ['Tôi đứng dậy ít nhất 6 lần mỗi ngày', 'Tôi có câu Nếu… thì…', 'Tôi tự làm một việc nhà nhỏ'],
 ['Nhờ người thân tự làm việc nhỏ, đừng làm hộ hết: rót nước, phơi đồ, tưới cây.',
  'Đặt cốc nước, điều khiển TV ở chỗ phải đứng dậy mới lấy được, nếu an toàn.',
  'Đi cùng vài bước sau bữa ăn.'],
 [lb('Đã xác nhận', f'Mọi lứa tuổi nên hạn chế thời gian ngồi lì; mọi vận động đều có ích ({WHOFS}; {WHO20}).'),
  lb('Đã xác nhận', f'Cẩm nang của Bộ Y tế: người từ 60 tuổi có thể vận động qua việc hằng ngày như đi bộ, việc nhà, trong sức của mình ({BYT2}).'),
  lb('Đánh giá chuyên môn', 'Mốc "mỗi giờ đứng dậy một lần" và "6 lần mỗi ngày" là mục tiêu tập thói quen do daynentang.com đặt, không phải ngưỡng từ nghiên cứu.'),
  lb('Đánh giá chuyên môn', 'Ngồi một lát trước khi đứng để giảm chóng mặt khi đổi tư thế là lời khuyên thực hành phổ biến; chưa dẫn được nghiên cứu.')])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Vận động an toàn, bài 3: thở chậm trên ghế; không nín thở khi gắng sức; khởi động 5 phút trước khi tập, thả lỏng sau khi tập.',
 ['Thở chậm <strong>1 phút</strong> trên ghế.', 'Làm trọn chuỗi <strong>khởi động 5 phút</strong>.', 'Khởi động trước <strong>3 buổi tập</strong> trong tuần.'],
 ['Ghế chắc, sát tường.', 'Một khoảng trống quanh ghế, dọn thảm và dây điện.'],
 ['Thở chậm giúp bắt đầu buổi tập bình tĩnh. Hít vào bằng mũi, <strong>thở ra chậm và dài hơn</strong>.',
  'Khi tập sức, <strong>thở đều, không nín thở</strong>. Đếm to "một, hai" giúp không nín thở.',
  'Trong lúc tập, thở có thể nhanh hơn, nhưng <strong>bạn vẫn nói được</strong>.',
  '<strong>Khởi động</strong> 5 phút làm ấm cơ và khớp: xoay vai, xoay cổ tay, nhấc gót – mũi chân, bước tại chỗ.',
  'Sau buổi tập, <strong>đi chậm 2–3 phút</strong> cho người dịu xuống, rồi mới ngồi nghỉ.',
  'Ngày mệt, ngày ốm: chỉ thở chậm và khởi động là đủ. Nghỉ cũng là một phần của tập.'],
 levels([['Thở chậm', 'Ngồi, 5 hơi', '10 hơi', '1 phút, thêm đưa tay lên khi hít vào'],
         ['Xoay vai', 'Ngồi, 5 lần', 'Đứng vịn ghế, 5 lần', 'Đứng, 10 lần'],
         ['Xoay cổ tay', 'Mỗi bên 5 lần', 'Mỗi bên 10 lần', 'Thêm nắm – mở bàn tay 10 lần'],
         ['Nhấc gót – mũi chân', 'Ngồi, 10 lần', 'Đứng vịn ghế, 10 lần', 'Đứng vịn, 15 lần'],
         ['Bước tại chỗ', 'Ngồi, 1 phút', 'Đứng vịn ghế, 1 phút', 'Đứng vịn, 2 phút, gối cao hơn']]),
 lines(['Mức tôi chọn hôm nay', 'Sau khởi động tôi thấy (0–10)', 'Tôi có nín thở không? Lúc nào?']),
 ['Chóng mặt khi thở sâu: thở bình thường, nghỉ.', 'Đứng tập thì luôn có ghế hoặc bàn chắc để vịn.'],
 ['Tôi thở chậm 1 phút', 'Tôi khởi động trước khi tập', 'Tôi đi chậm sau khi tập'],
 ['Đếm nhịp cùng người tập. Nhắc nhẹ khi thấy nín thở.', 'Tập cùng. Người thân khỏe cũng cần khởi động.'],
 [lb('Đã xác nhận', f'Khởi động trước và thả lỏng sau khi tập; thở có thể nhanh hơn nhưng vẫn nói được; bắt đầu chậm với bài nhẹ ({NIA}).'),
  lb('Đánh giá chuyên môn', 'Lời khuyên không nín thở khi tập sức, đếm to để giữ nhịp thở, là thực hành thường dùng trong tập luyện; chưa dẫn được nguồn gốc cụ thể. [Cần kiểm chứng]'),
  lb('Đánh giá chuyên môn', 'Chuỗi khởi động 5 động tác và ba mức do daynentang.com soạn.')])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Vận động an toàn, bài 4: đứng lên – ngồi xuống ghế 4 bước; nhón gót vịn ghế; ba mức; tự đo 30 giây để so mình với mình.',
 ['Làm đúng <strong>4 bước</strong> đứng lên – ngồi xuống ghế.', 'Tập sức chân <strong>2 ngày</strong> trong tuần.',
  'Ghi số lần <strong>đo 30 giây</strong> lần đầu (nếu đứng lên được mà không chống tay).'],
 [f'In trang 4 của <a href="{TOOL}">Sổ vận động an toàn</a>.', 'Ghế chắc không tay vịn, không bánh xe, dựa tường. Gối hoặc nệm nếu ghế thấp.',
  'Đồng hồ có kim giây. Một người đứng cạnh khi đo.'],
 ['Sức chân giúp <strong>đứng dậy, lên bậc, đi lại</strong> và giữ người khi suýt ngã.',
  'Tập sức cơ tăng dần làm cơ khỏe hơn rõ rệt ở người cao tuổi, kể cả việc đứng dậy khỏi ghế.',
  'WHO khuyên tập sức cơ <strong>ít nhất 2 ngày mỗi tuần</strong>.',
  '<strong>Bốn bước:</strong> ngồi mép ghế · kéo bàn chân lùi về sau · nghiêng người tới trước · đẩy đứng thẳng.',
  '<strong>Ngồi xuống chậm</strong>, đếm 1–2–3. Phần ngồi xuống chậm cũng làm chân khỏe.',
  'Làm <strong>8–12 lần</strong> là một lượt. Mỏi vừa ở đùi là bình thường. Đau khớp nhói là đèn vàng.',
  'Đo 30 giây: khoanh tay, đếm số lần đứng lên – ngồi xuống. Ghi lại để <strong>so với chính mình</strong> ở tuần 5 và tuần 10.',
  'Cơ hơi mỏi 1–2 ngày sau tập là thường gặp. Nghỉ một ngày giữa hai buổi tập sức nếu cơ còn mỏi.'],
 levels([['Đứng lên – ngồi xuống', 'Chống tay lên đùi hoặc tay ghế; ghế cao hoặc kê gối; 5 lần', 'Khoanh tay; ghế thường; 8 lần', 'Khoanh tay; ngồi xuống chậm 3 nhịp; 12 lần'],
         ['Nhón gót', 'Vịn ghế hai tay, 5 lần', 'Vịn một tay, 10 lần', 'Vịn một ngón tay, 15 lần, hạ chậm']])
 + '<p><strong>Đo 30 giây</strong> (chỉ khi đứng lên được mà không chống tay): ghế cao khoảng 43 cm, khoanh tay trước ngực, có người đứng cạnh. Đếm số lần đứng thẳng hẳn trong 30 giây.</p>'
 + table(['Tuổi', 'Nam: dưới mức', 'Nữ: dưới mức'], [['60–64', '< 14', '< 12'], ['65–69', '< 12', '< 11'], ['70–74', '< 12', '< 10'], ['75–79', '< 11', '< 10'], ['80–84', '< 10', '< 9'], ['85–89', '< 8', '< 8'], ['90–94', '< 7', '< 4']])
 + '<p class="small">Bảng mức của CDC dùng để nhận ra nguy cơ té ngã. Thấp hơn mức: nói với nhân viên y tế. Bảng không dùng để tự chẩn đoán.</p>',
 lines(['Mức tôi tập', 'Số lần mỗi lượt', 'Đo 30 giây tuần 1: … lần', 'Tôi thấy (dễ / vừa / khó)']),
 ['Ghế phải chắc, dựa tường. Không dùng ghế xoay, ghế có bánh xe, ghế nhựa yếu.', 'Đau gối nhói: kê ghế cao hơn, giảm số lần, hỏi nhân viên y tế nếu đau kéo dài.',
  'Không làm phép đo 30 giây khi đứng lên phải chống tay; ghi "chống tay" là đủ.'],
 ['Tôi tập đứng lên – ngồi xuống', 'Tôi tập nhón gót', 'Tôi ngồi xuống chậm'],
 ['Đứng cạnh, phía trước hơi lệch một bên, khi người tập đứng lên. Không kéo tay họ.', 'Bấm giờ và đếm khi đo 30 giây.', 'Ghi số đo vào sổ, khen tiến bộ dù nhỏ.'],
 [lb('Đã xác nhận', f'Tổng quan 121 thử nghiệm, 6.700 người: tập sức cơ tăng dần làm sức cơ tăng nhiều, cải thiện việc đứng dậy khỏi ghế ở mức vừa đến lớn, cải thiện khả năng vận động chung ở mức nhỏ; biến cố nghiêm trọng hiếm gặp ({PRT}).'),
  lb('Đã xác nhận', f'WHO khuyên người lớn tập sức cơ từ 2 ngày mỗi tuần ({WHO20}).'),
  lb('Đã xác nhận', f'Phép thử 30 giây của CDC: ghế 17 inch (khoảng 43 cm), khoanh tay, có người đứng cạnh; bảng mức dưới trung bình theo tuổi và giới ({STEADI}).'),
  lb('Cần kiểm chứng', 'Bảng mức của CDC lấy từ người Hoa Kỳ; chưa rõ có hợp với người Việt Nam không.'),
  lb('Đánh giá chuyên môn', 'Ba mức, số lần mỗi lượt và lời khuyên nghỉ một ngày khi cơ còn mỏi do daynentang.com đặt.')])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Vận động an toàn, bài 5: bốn bậc thăng bằng luôn vịn ghế; đi nối gót dọc bàn bếp; chỗ tập an toàn; tập từ 3 ngày mỗi tuần.',
 ['Đứng vững ở <strong>bậc thăng bằng của mình</strong> trong 10 giây, có vịn.', 'Tập thăng bằng <strong>3 ngày</strong> trong tuần.',
  'Chọn được <strong>một chỗ tập an toàn</strong> trong nhà.'],
 [f'In trang 5 của <a href="{TOOL}">Sổ vận động an toàn</a>.', 'Ghế nặng dựa tường, hoặc bàn bếp chắc. Nền khô, không thảm trơn.', 'Lần đầu: có một người ở gần.'],
 ['Thăng bằng tốt giúp <strong>đứng vững khi xoay người, bước qua bậc, mặc quần</strong>.',
  'Tổng quan nhiều thử nghiệm: tập thăng bằng và động tác chức năng <strong>giảm số lần té ngã</strong> ở người cao tuổi.',
  'WHO khuyên người cao tuổi tập phối hợp thăng bằng và sức cơ <strong>từ 3 ngày mỗi tuần</strong>.',
  '<strong>Bốn bậc:</strong> hai chân sát nhau · nửa nối gót · nối gót (gót chân trước chạm mũi chân sau) · đứng một chân.',
  '<strong>Luôn vịn</strong> ghế hoặc bàn. Khi vững hơn, chuyển từ vịn hai tay xuống một tay, rồi một ngón tay.',
  'Mỗi bậc giữ khoảng 10 giây. Làm được dễ dàng nhiều lần mới lên bậc sau.',
  '<strong>Đi nối gót</strong> dọc bàn bếp, tay để trên mặt bàn: gót chân trước đặt sát mũi chân sau, 10 bước.',
  'Thái cực quyền cũng có bằng chứng giảm té ngã. Muốn học, tìm lớp có người hướng dẫn.'],
 levels([['Đứng thăng bằng', 'Hai chân sát, vịn hai tay', 'Nửa nối gót hoặc nối gót, vịn một tay', 'Đứng một chân, vịn một ngón tay'],
         ['Đi nối gót dọc bàn', 'Bước bình thường, tay trên bàn, 10 bước', 'Nửa nối gót, 10 bước', 'Nối gót, 10 bước, đi chậm'],
         ['Bước sang ngang', 'Vịn bàn, 5 bước mỗi bên', '10 bước mỗi bên', '10 bước, bước rộng hơn']]),
 lines(['Bậc của tôi hôm nay', 'Giữ được … giây', 'Chỗ tập trong nhà', 'Tuần sau thử bậc']),
 ['Không tập thăng bằng khi đang chóng mặt, mệt, vừa uống thuốc ngủ.', 'Đi giày đế bám hoặc chân trần; không đi dép lê, tất trơn.',
  'Đứng gần góc tường hoặc giữa bàn và tường để có chỗ vịn hai phía.'],
 ['Tôi tập thăng bằng có vịn', 'Tôi đi nối gót dọc bàn', 'Tôi tập ở chỗ an toàn'],
 ['Lần đầu, đứng sát bên, sẵn sàng đỡ ở hông, không nắm tay kéo.', 'Dọn chỗ tập: thảm, dây điện, đồ chơi.', 'Tập cùng như một trò chơi: ai đứng nối gót lâu hơn.'],
 [lb('Đã xác nhận', f'Tổng quan 108 thử nghiệm, 23.407 người cao tuổi sống tại cộng đồng: tập luyện giảm số lần té ngã 23%; tập thăng bằng và động tác chức năng giảm 24%; Thái cực quyền giảm số người bị ngã 20% ({SHER}).'),
  lb('Đã xác nhận', f'WHO 2020: người cao tuổi nên tập phối hợp thăng bằng, phối hợp động tác và sức cơ từ 3 ngày mỗi tuần để phòng té ngã ({WHO20}).'),
  lb('Đã xác nhận', f'Khi tập thăng bằng, để ghế chắc hoặc một người ở gần để vịn khi thấy chông chênh ({NIA}).'),
  lb('Đánh giá chuyên môn', 'Bốn bậc, mốc 10 giây và ba mức do daynentang.com soạn, phỏng theo ý tập thăng bằng tăng dần; không chép chương trình có bản quyền.')])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Vận động an toàn, bài 6: sức tay và sức nắm bằng đồ trong nhà: co tay với chai nước, đẩy tường, bóp khăn cuộn.',
 ['Tập <strong>co tay với chai nước</strong> và <strong>đẩy tường</strong>, mỗi động tác một lượt.', 'Tập sức tay <strong>2 ngày</strong> trong tuần.',
  'Nêu <strong>1 việc hằng ngày</strong> sẽ dễ hơn khi tay khỏe.'],
 ['Hai chai nước có nắp: 0,5 lít và 1 lít.', 'Một khăn mặt cuộn tròn.', 'Một bức tường trống, nền không trơn.'],
 ['Sức tay giúp <strong>xách giỏ, mở nắp lọ, chống tay đứng dậy, bám tay vịn</strong> khi suýt ngã.',
  'Tập sức cơ dùng sức nặng nhỏ, tăng dần. <strong>Chai nước</strong> là quả tạ có sẵn trong nhà.',
  '<strong>Co tay:</strong> khuỷu tay sát người, đưa chai lên vai, hạ xuống chậm. Thở ra khi nâng.',
  '<strong>Đẩy tường:</strong> chống hai tay lên tường ngang vai, gập khuỷu đưa người vào, rồi đẩy ra. Người thẳng như tấm ván.',
  '<strong>Bóp khăn cuộn:</strong> nắm chặt 3 giây, thả ra. Tốt cho sức nắm.',
  'Làm 8–12 lần là một lượt. Tăng mức khi lượt cuối vẫn thấy nhẹ.',
  'Thở đều, đếm to. Không nín thở khi đẩy hay nâng.'],
 levels([['Co tay với chai', 'Ngồi, chai 0,5 lít, 8 lần mỗi tay', 'Chai 1 lít, 10 lần', 'Chai 1,5 lít, 12 lần, hạ chậm'],
         ['Đẩy tường', 'Đứng gần tường, 5 lần', 'Lùi xa thêm nửa bước, 8 lần', 'Chống tay lên bàn bếp chắc, 10 lần'],
         ['Bóp khăn cuộn', '5 lần mỗi tay', '10 lần', '10 lần, giữ 5 giây'],
         ['Đưa tay lên cao', 'Ngồi, không cầm gì, 5 lần', 'Cầm chai 0,5 lít, 8 lần', 'Chai 0,5 lít, 12 lần']]),
 lines(['Mức tôi tập', 'Việc hằng ngày tôi muốn làm dễ hơn', 'Tôi thấy (dễ / vừa / khó)']),
 ['Đau vai nhói khi đưa tay lên: chỉ đưa tới ngang vai, hỏi nhân viên y tế nếu đau kéo dài.', 'Chai phải đậy kín nắp. Lau khô tay để khỏi trượt.',
  'Huyết áp cao: thở đều, không nín thở, không gồng quá sức.'],
 ['Tôi co tay với chai nước', 'Tôi đẩy tường', 'Tôi bóp khăn cuộn'],
 ['Chuẩn bị chai nước đúng cỡ.', 'Nhờ người tập tự mở nắp lọ, tự xách túi nhẹ: việc hằng ngày cũng là tập.'],
 [lb('Đã xác nhận', f'Tập sức cơ tăng dần ở người cao tuổi làm sức cơ tăng rõ; than phiền đau cơ, đau khớp hay gặp; biến cố nghiêm trọng hiếm ({PRT}).'),
  lb('Đã xác nhận', f'WHO: tập sức cơ có lợi cho mọi người; người lớn nên tập từ 2 ngày mỗi tuần ({WHOFS}; {WHO20}).'),
  lb('Đánh giá chuyên môn', 'Chọn chai nước, đẩy tường, bóp khăn cuộn và số lần mỗi lượt do daynentang.com đặt cho người tự tập ở nhà; chưa được thử nghiệm riêng.'),
  lb('Cần kiểm chứng', 'Mức tăng huyết áp khi nín thở lúc tập sức ở người có huyết áp cao: chưa tra nguồn gốc.')])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Vận động an toàn, bài 7: phép thử nói chuyện; đi bộ ở mức vừa, tăng dần mỗi tuần; chia nhỏ trong ngày; đi bộ an toàn khi trời nóng.',
 ['Dùng <strong>phép thử nói chuyện</strong> để biết mình đang đi ở mức nào.', 'Đi bộ <strong>5 ngày</strong> trong tuần ở mức vừa.',
  'Mỗi tuần <strong>thêm vài phút</strong>.'],
 [f'In trang 6 của <a href="{TOOL}">Sổ vận động an toàn</a>.', 'Giày đế bám, vừa chân. Nước uống. Mũ khi ra nắng. Điện thoại.',
  'Một đường đi bằng phẳng, có bóng mát, ít xe. Trong nhà cũng được.'],
 ['<strong>Phép thử nói chuyện:</strong> nói được câu nhưng không hát được là mức <strong>vừa</strong>. Chỉ nói được vài từ là mức <strong>mạnh</strong>.',
  'Người mới tập: mức nhẹ đến vừa là đủ. Không cần đi nhanh.',
  'Bắt đầu <strong>5–10 phút</strong>. Mỗi tuần thêm vài phút. Chia làm nhiều lần ngắn trong ngày cũng được.',
  'Mục tiêu xa của người lớn: <strong>150–300 phút mỗi tuần</strong> ở mức vừa. Người yếu sức làm trong sức mình, mỗi phút đều có ích.',
  'Đi bộ tốt cho tim phổi và sức bền. Để phòng té ngã, <strong>cần thêm bài thăng bằng và sức chân</strong> (bài 4–5).',
  'Trời nóng: đi sáng sớm hoặc chiều mát, mang nước, nghỉ trong bóng râm. Nắng gắt thì đi trong nhà.',
  'Dùng gậy hay khung tập đi: dùng đúng loại, đúng cách nhân viên y tế đã hướng dẫn.'],
 levels([['Đi bộ', '5 phút trong nhà hoặc sân, có người đi cùng', '10–15 phút, mức vừa', '20–30 phút, hoặc 2 lần 15 phút'],
         ['Lên bậc thang', 'Vịn tay vịn, 1 bậc lên xuống, 5 lần', '3 bậc, vịn tay vịn', '1 tầng, vịn tay vịn, đi chậm']])
 + '<p><strong>Kế hoạch đi bộ 4 tuần</strong> (điền số phút):</p>'
 + table(['Tuần'] + DAYS, [[f'Tuần {i}'] + [''] * 7 for i in range(1, 5)]),
 lines(['Tôi đi ở mức (nhẹ / vừa / mạnh)', 'Đường đi an toàn của tôi', 'Người đi cùng']),
 ['Đi đường bằng, đủ sáng; tránh đường trơn, ổ gà, giờ xe đông.', 'Mang điện thoại, nói người nhà mình đi đâu, khi nào về.',
  'Đèn đỏ khi đi: đứng lại, tìm chỗ ngồi, gọi người.', f'Làm việc ngoài trời nóng: xem thêm khóa <a href="{C5}">15 phút mỗi ngày</a>, bài làm việc khi trời nóng.'],
 ['Tôi đi bộ ở mức vừa', 'Tôi tăng thêm vài phút', 'Tôi mang nước khi đi'],
 ['Đi cùng, nói chuyện trong lúc đi: đó cũng là phép thử nói chuyện.', 'Chọn giờ đi cố định với người tập, ví dụ sau bữa tối.'],
 [lb('Đã xác nhận', f'Mức vừa: nói được nhưng không hát được; mức mạnh: chỉ nói được vài từ ({TALKT}).'),
  lb('Đã xác nhận', f'Người lớn: 150–300 phút mức vừa mỗi tuần ({WHO20}). Cẩm nang Bộ Y tế: người từ 60 tuổi giữ mức như người lớn, trong khả năng và thể trạng ({BYT2}).'),
  lb('Đã xác nhận', f'Chương trình chỉ đi bộ: tác dụng phòng té ngã chưa chắc chắn ({SHER}).'),
  lb('Đã xác nhận', f'Uống nước trước, trong và sau khi tập; tập trong nhà khi trời quá nóng hoặc lạnh ({NIA}).'),
  lb('Đánh giá chuyên môn', 'Mốc bắt đầu 5–10 phút và cách tăng vài phút mỗi tuần do daynentang.com đặt.')])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Vận động an toàn, bài 8: giãn cơ nhẹ sau khi đi bộ; với tay lên cao, duỗi chân, giãn bắp chân; xoay khớp; nên và không nên.',
 ['Làm <strong>3 động tác giãn cơ</strong> đúng cách.', 'Giãn cơ sau khi đi bộ <strong>3 ngày</strong> trong tuần.', 'Nói được <strong>2 điều không nên</strong> khi giãn cơ.'],
 ['Ghế chắc, một bức tường trống.', 'Làm sau khi đi bộ hoặc khởi động, lúc cơ đã ấm.'],
 ['Giãn cơ và xoay khớp giúp <strong>với lên kệ, cúi buộc dây giày, quay đầu nhìn xe</strong> dễ hơn.',
  'Giãn khi <strong>cơ đã ấm</strong>: sau đi bộ vài phút hoặc sau khởi động.',
  'Căng <strong>nhẹ</strong>, không đau. Giữ khoảng 3–5 hơi thở chậm, rồi thả.',
  '<strong>Không nhún, không giật</strong>, không cố tới mức đau, không nín thở.',
  '<strong>Với tay lên cao:</strong> ngồi thẳng, đưa hai tay lên, thở đều.',
  '<strong>Duỗi chân:</strong> ngồi mép ghế, duỗi thẳng một chân, gót chạm sàn, nghiêng nhẹ người tới trước.',
  '<strong>Giãn bắp chân:</strong> chống tay vào tường, một chân lùi sau, gót chân sau chạm sàn.',
  'Khớp đau lâu ngày: cử động nhẹ trong tầm không đau. Khớp mới sưng, nóng, đỏ: không tập khớp đó, đi khám.'],
 levels([['Với tay lên cao', 'Ngồi, đưa tới ngang vai', 'Ngồi, đưa lên cao', 'Đứng vịn, đưa lên cao, nghiêng nhẹ hai bên'],
         ['Duỗi chân', 'Ngồi, duỗi chân, không nghiêng', 'Nghiêng nhẹ tới trước', 'Giữ lâu hơn, đổi chân 2 lượt'],
         ['Giãn bắp chân', 'Chân sau lùi nửa bước', 'Lùi một bước', 'Lùi xa hơn, gót vẫn chạm sàn'],
         ['Xoay cổ chân', 'Ngồi, 5 vòng mỗi chiều', '10 vòng', '10 vòng, cả hai chân lần lượt']]),
 lines(['Động tác dễ chịu nhất', 'Chỗ còn cứng', 'Việc hằng ngày tôi muốn làm dễ hơn']),
 ['Mới thay khớp háng, gối: chỉ làm động tác nhân viên y tế cho phép.', 'Đứng giãn thì luôn có chỗ vịn.'],
 ['Tôi giãn cơ sau khi đi bộ', 'Tôi không nhún, không cố tới đau', 'Tôi xoay cổ chân'],
 ['Nhắc giãn nhẹ, không ấn, không kéo giúp.', 'Giãn cùng sau khi đi bộ chung.'],
 [lb('Đã xác nhận', f'Đi bộ vài phút trước khi giãn cơ; bắt đầu chậm; dùng ghế chắc ({NIA}).'),
  lb('Đã xác nhận', f'Cẩm nang Bộ Y tế: người cao tuổi nên chú ý bài tập giúp thăng bằng, sức cơ và giữ khớp linh hoạt ({BYT}).'),
  lb('Đã xác nhận', f'Tập linh hoạt chưa được nghiên cứu riêng về tác dụng phòng té ngã ({SHER}).'),
  lb('Đánh giá chuyên môn', 'Mốc 3–5 hơi thở, động tác và ba mức do daynentang.com đặt; chưa dẫn được nghiên cứu về thời gian giữ cho người yếu sức. [Cần kiểm chứng]')])

# ======================= BÀI 9 =======================
lesson('9', 'Khóa Vận động an toàn, bài 9: ba cách giảm té ngã; sáu bước đứng dậy sau khi ngã; làm gì khi không dậy được; khi nào gọi 115.',
 ['Kể được <strong>6 bước</strong> đứng dậy sau khi ngã.', 'Biết <strong>khi nào không cố dậy</strong> mà gọi 115.', 'Sửa <strong>1 chỗ dễ trượt, dễ vấp</strong> trong nhà.'],
 [f'In trang 7 của <a href="{TOOL}">Sổ vận động an toàn</a> (Kế hoạch khi ngã).', 'Điện thoại có lưu số người thân.', 'Tập phần lăn nghiêng trên giường, có người ở cạnh.'],
 ['Té ngã là nguyên nhân thương tích hay gặp ở người cao tuổi. <strong>Nhiều lần ngã có thể phòng được.</strong>',
  '<strong>Ba cách giảm té ngã:</strong> tập sức chân và thăng bằng đều (bài 4–5); nhà an toàn hơn; hỏi về thuốc và khám mắt.',
  f'Nhà an toàn: đủ đèn, nhất là lối đi ban đêm; nền khô; tay vịn ở nhà tắm, cầu thang. Xem <a href="{C7B5}">bài An toàn trong nhà</a> và khóa <a href="{G8}">Nhà gọn, nhà an toàn</a>.',
  'Một số thuốc gây chóng mặt, buồn ngủ. Hỏi bác sĩ hoặc dược sĩ khi hay chóng mặt.',
  '<strong>Khi bị ngã:</strong> nằm yên, thở, tự kiểm tra chỗ đau trước khi dậy.',
  '<strong>Sáu bước:</strong> nằm yên kiểm tra · lăn nghiêng · chống tay và gối · bò tới ghế chắc · một chân lên, vịn ghế đứng dậy · ngồi nghỉ, báo người nhà.',
  '<strong>Không cố dậy, gọi 115</strong> khi đau ở đầu, cổ, lưng, hông, hoặc không đứng lên được.',
  '<strong>Không dậy được:</strong> gọi điện, gọi to, gõ xuống sàn; kéo khăn, áo đắp cho ấm; co duỗi tay chân, đổi tư thế trong lúc chờ.',
  '<strong>Đã ngã một lần</strong>, kể cả không đau: nói với nhân viên y tế. Họ có thể tìm nguyên nhân.'],
 '<p><strong>Phần 1: tập lăn nghiêng trên giường</strong>, có người ở cạnh. Không tập ngã thật, không tập xuống sàn khi chưa có nhân viên y tế hướng dẫn.</p>'
 + levels([['Lăn nghiêng', 'Nằm ngửa, co gối, lăn sang một bên, 3 lần', 'Mỗi bên 3 lần', 'Lăn rồi chống tay ngồi dậy ở mép giường'],
           ['Chống tay và gối', 'Bỏ qua bậc này', 'Trên giường, giữ 5 hơi thở', 'Trên thảm dày, có người cạnh, giữ 5 hơi thở']])
 + '<p><strong>Phần 2: rà một vòng nhà</strong> (5 phút). Đánh dấu chỗ cần sửa:</p>'
 + table(['Chỗ', 'Ổn', 'Cần sửa'], [[x, '', ''] for x in ['Lối từ giường tới nhà vệ sinh có đèn ngủ', 'Nền nhà tắm khô, có thảm chống trơn', 'Không có dây điện, đồ vật trên lối đi',
                                                         'Cầu thang có tay vịn, đủ sáng', 'Dép trong nhà có đế bám, vừa chân', 'Đồ hay dùng để ngang tầm tay, không phải trèo']]),
 lines(['Chỗ tôi sửa tuần này', 'Người tôi gọi khi ngã (tên, số)', 'Thuốc tôi muốn hỏi bác sĩ, dược sĩ']),
 ['Không đứng lên ghế, thang để lấy đồ trên cao khi ở nhà một mình.', 'Ban đêm: ngồi ở mép giường một lát, bật đèn, rồi mới đứng.',
  'Mang điện thoại theo người, kể cả khi vào nhà tắm.'],
 ['Tôi biết 6 bước đứng dậy', 'Tôi sửa một chỗ trong nhà', 'Tôi mang điện thoại theo người'],
 ['Cùng rà một vòng nhà và sửa ngay chỗ dễ làm.', 'Thấy người thân ngã: không vội kéo dậy. Hỏi chỗ đau. Đau đầu, cổ, lưng, hông hoặc không dậy được: gọi 115, đắp ấm, ở cạnh.',
  'Hẹn gọi điện vào một giờ cố định mỗi ngày nếu người thân ở một mình.'],
 [lb('Đã xác nhận', f'Các bước đứng dậy sau khi ngã; khi không dậy được: gọi người, giữ ấm, cử động tay chân, đổi tư thế khoảng mỗi 30 phút; gọi cấp cứu khi có thể chấn thương đầu, lưng, cổ, hông; gặp bác sĩ sau khi ngã ({NHSF}).'),
  lb('Đã xác nhận', f'Tập luyện giảm số lần té ngã 23% ở người cao tuổi sống tại cộng đồng ({SHER}).'),
  lb('Đã xác nhận', f'Thông tin về té ngã và sửa nhà phòng ngã ở người cao tuổi nguy cơ cao ({WHOF}).'),
  lb('Đã xác nhận', f'Hỏi bác sĩ, dược sĩ về thuốc có thể ảnh hưởng thăng bằng; khám mắt đều ({NHSF}).'),
  lb('Đánh giá chuyên môn', 'Chỉ tập phần lăn nghiêng trên giường, không tập xuống sàn khi tự học: daynentang.com chọn để an toàn.')], figs_after=3)

# ======================= BÀI 10 =======================
lesson('10', 'Khóa Vận động an toàn, bài 10: viết lịch tuần đủ bốn loại vận động; đo lại 30 giây; khi nào giảm mức; giữ thói quen nhiều năm.',
 ['Viết xong <strong>lịch tuần</strong> có đủ 4 loại vận động.', '<strong>Đo lại 30 giây</strong> và so với tuần 1.', 'Chọn <strong>1 bước tiếp theo</strong> cho 3 tháng tới.'],
 [f'In trang 8–9 của <a href="{TOOL}">Sổ vận động an toàn</a>.', 'Sổ ghi chép các tuần trước.'],
 ['Một tuần nên có đủ: <strong>sức cơ</strong> từ 2 ngày, <strong>thăng bằng</strong> từ 3 ngày, <strong>đi lại</strong> hằng ngày, <strong>giãn cơ</strong> sau đi bộ.',
  'Đó là hướng tới, không phải bắt buộc ngay. Mỗi phút vận động đều có ích.',
  '<strong>Giờ cố định</strong> và <strong>tập cùng người khác</strong> giúp giữ thói quen.',
  '<strong>Giảm mức</strong> khi: vừa ốm, vừa ngã, đổi thuốc, mất ngủ, trời quá nóng. Quay lại mức dễ, rồi tăng lại dần.',
  '<strong>Tăng mức</strong> khi làm dễ dàng khoảng 2 tuần liền, không đau.',
  'So kết quả với <strong>chính mình</strong>, không so với người khác.',
  'Muốn đi xa hơn: tìm lớp thể dục người cao tuổi, câu lạc bộ đi bộ, lớp Thái cực quyền có người hướng dẫn.'],
 '<p><strong>Lịch tuần của tôi</strong> (đánh dấu và ghi số phút):</p>'
 + table(['Loại'] + DAYS, [[x] + [''] * 7 for x in ['Sức cơ (bài 4, 6)', 'Thăng bằng (bài 5)', 'Đi bộ (bài 7)', 'Giãn cơ (bài 8)', 'Đứng dậy mỗi giờ (bài 2)']])
 + table(['Đo lại', 'Tuần 1', 'Tuần 5', 'Tuần 10'], [['Đứng lên – ngồi xuống 30 giây', '', '', ''], ['Phút đi bộ liền một lần', '', '', ''], ['Bậc thăng bằng (1–4)', '', '', '']]),
 lines(['Giờ tập cố định', 'Người tập cùng', 'Bước tiếp theo trong 3 tháng', 'Khi ốm hay vừa ngã, tôi sẽ quay về mức']),
 ['Đo lại trong cùng điều kiện như tuần 1: cùng ghế, có người đứng cạnh.', 'Kết quả đi xuống hoặc ngã lại: nói với nhân viên y tế.'],
 ['Tôi có lịch tuần', 'Tôi đo lại 30 giây', 'Tôi có bước tiếp theo'],
 ['Cùng xem sổ, khen những tuần đã giữ được.', 'Hỏi người tập muốn tập tiếp với ai, ở đâu.', f'Người tập buồn, chán kéo dài: xem khóa <a href="{C8}">Chăm tâm trí cơ bản</a>.'],
 [lb('Đã xác nhận', f'WHO 2020: sức cơ từ 2 ngày; người cao tuổi tập phối hợp thăng bằng và sức cơ từ 3 ngày; hạn chế ngồi lì ({WHO20}).'),
  lb('Đã xác nhận', f'Khoảng 31% người lớn trên thế giới chưa vận động đủ; tỷ lệ này tăng sau 60 tuổi ({WHOFS}).'),
  lb('Đã xác nhận', f'Tập phối hợp nhiều loại (thường là thăng bằng, động tác chức năng và sức cơ) giảm số lần té ngã 34%, mức chắc chắn vừa ({SHER}).'),
  lb('Đánh giá chuyên môn', 'Tuần mẫu, mốc "2 tuần thì lên mức" và cách quay về mức dễ do daynentang.com đặt.')])

# ======================= CÔNG CỤ =======================
FINAL = ['Tôi biết 3 đèn tập luyện', 'Tôi đứng dậy mỗi giờ', 'Tôi khởi động trước khi tập', 'Tôi tập sức chân 2 ngày/tuần',
         'Tôi tập thăng bằng 3 ngày/tuần', 'Tôi tập sức tay 2 ngày/tuần', 'Tôi đi bộ ở mức vừa', 'Tôi giãn cơ sau đi bộ',
         'Tôi biết 6 bước đứng dậy sau khi ngã', 'Tôi có lịch tuần']
frows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in FINAL)
page(TOOL, 'Sổ vận động an toàn', 'Trang in cho khóa Vận động an toàn: phiếu Trước khi tập, thẻ dừng tập, đếm lần đứng dậy, động tác 3 mức, đo 30 giây, kế hoạch đi bộ, Kế hoạch khi ngã, lịch tuần.',
f'''
<h1>Sổ vận động an toàn</h1>
<p>Dùng cho khóa <a href="{U}">Vận động an toàn</a>. Chỉ để in, trang không lưu dữ liệu của bạn.</p>
{STOP}
{PRINT_ROW}
<h2>1. Phiếu "Trước khi tập" (bài 1)</h2>
{table(['Câu hỏi', 'Có', 'Không'], [[q, '', ''] for q in ASKLIST])}
<p>Có từ 1 ý "Có": mang phiếu đi hỏi nhân viên y tế trước khi tập.</p>
{lines(['Nhân viên y tế dặn tôi', 'Động tác tôi không nên làm'])}
<h2>2. Thẻ đèn tập luyện (cắt, dán cạnh chỗ tập)</h2>
<div class="table-wrap"><table><tbody>
<tr><th>Xanh</th><td>Thở nhanh hơn, vẫn nói được câu → tập tiếp</td></tr>
<tr><th>Vàng</th><td>Mỏi nhiều, đau cơ, hụt hơi → chậm lại, xuống mức dễ, nghỉ</td></tr>
<tr><th>Đỏ</th><td>Đau ngực, khó thở nhiều, chóng mặt, choáng → dừng, ngồi xuống, gọi người</td></tr>
<tr><th>115</th><td>Đau ngực không đỡ, ngất, yếu nửa người, méo miệng, nói khó</td></tr>
</tbody></table></div>
<h2>3. Đếm lần đứng dậy (bài 2)</h2>
{table(['Ngày'] + DAYS, [['Số lần'] + [''] * 7])}
{lines(['Nếu …', 'thì tôi …'])}
<h2>4. Động tác của tôi (bài 3–8)</h2>
<p>Ghi mức (D = dễ, V = vừa, K = khó) và số lần. Lên mức khi làm dễ dàng khoảng 2 tuần.</p>
{table(['Động tác', 'Tuần 1', 'Tuần 3', 'Tuần 5', 'Tuần 7', 'Tuần 9'], [[x, '', '', '', '', ''] for x in ['Khởi động 5 phút', 'Đứng lên – ngồi xuống', 'Nhón gót', 'Thăng bằng (bậc 1–4)', 'Đi nối gót dọc bàn', 'Co tay với chai nước', 'Đẩy tường', 'Bóp khăn cuộn', 'Giãn cơ']])}
<h2>5. Đo 30 giây (bài 4, 10)</h2>
<p>Chỉ đo khi đứng lên được mà không chống tay. Ghế chắc khoảng 43 cm, khoanh tay, có người đứng cạnh.</p>
{table(['Đo', 'Tuần 1', 'Tuần 5', 'Tuần 10'], [['Số lần trong 30 giây', '', '', ''], ['Phút đi bộ liền một lần', '', '', ''], ['Bậc thăng bằng', '', '', '']])}
<h2>6. Kế hoạch đi bộ (bài 7)</h2>
{table(['Tuần'] + DAYS, [[f'Tuần {i}'] + [''] * 7 for i in range(1, 7)])}
<p class="small">Ghi số phút. Mức vừa: nói được câu, không hát được.</p>
<h2>7. Kế hoạch khi ngã (bài 9)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">1</th><td>Nằm yên, thở, kiểm tra chỗ đau</td></tr>
<tr><th>2</th><td>Lăn nghiêng người</td></tr>
<tr><th>3</th><td>Chống tay và gối</td></tr>
<tr><th>4</th><td>Bò tới ghế chắc</td></tr>
<tr><th>5</th><td>Một chân lên, vịn ghế đứng dậy</td></tr>
<tr><th>6</th><td>Ngồi nghỉ, báo người nhà; đã ngã thì nói với nhân viên y tế</td></tr>
<tr><th>Gọi 115</th><td>Đau đầu, cổ, lưng, hông, hoặc không dậy được. Trong lúc chờ: gọi to, giữ ấm, cử động tay chân</td></tr>
</tbody></table></div>
{lines(['Người tôi gọi khi ngã (tên, số)', 'Người thứ hai (tên, số)', 'Giờ người thân gọi điện hỏi thăm mỗi ngày'])}
<h2>8. Lịch tuần (bài 10)</h2>
{table(['Loại'] + DAYS, [[x] + [''] * 7 for x in ['Sức cơ', 'Thăng bằng', 'Đi bộ', 'Giãn cơ', 'Đứng dậy mỗi giờ']])}
{lines(['Giờ tập cố định', 'Người tập cùng', 'Bước tiếp theo trong 3 tháng'])}
<h2>9. Tự theo dõi (bài 1 và bài 10)</h2>
<p>0 = chưa làm · 1 = làm 1–2 ngày trong tuần · 2 = làm từ 3 ngày trở lên.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Bài 1</th><th>Bài 10</th></tr></thead><tbody>{frows}</tbody></table></div>
<p class="small muted">Sổ để tự theo dõi, không dùng để chẩn đoán. Sổ không thay thế khám bệnh hay chương trình phục hồi do nhân viên y tế chỉ định.</p>
{HELP_BOX}
''', current='/cong-cu/')

# ======================= TRANG KHÓA =======================
rows = ''.join(f'<tr><td>{w}</td><td><a href="{url(w, L[str(w)][1])}">{L[str(w)][3]}</a></td><td>{goal}</td></tr>' for w, goal in PLAN)
page(U, 'Vận động an toàn', 'Khóa tự học miễn phí cho người cao tuổi, người mới ốm dậy, người có bệnh mạn tính đã ổn định và người ít vận động: ngồi ít lại, sức chân, thăng bằng, sức tay, đi bộ, giãn cơ, phòng té ngã.',
f'''
<p class="eyebrow">Cá nhân · Khóa C9 · Đang thử nghiệm</p>
<h1>Vận động an toàn</h1>
<p class="lead">Mười bài tập ở nhà, với một cái ghế, chai nước và bức tường. Bắt đầu nhỏ, tăng dần, biết lúc nào phải dừng.</p>
{STOP}
{PRINT_ROW}
<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bạn giữ và tăng sức đứng dậy, đi lại, thăng bằng; giảm nguy cơ té ngã; biết tập an toàn trong sức mình</td></tr>
<tr><th>Dành cho</th><td>Người cao tuổi; người mới ốm dậy; người có bệnh mạn tính đã ổn định (huyết áp, tiểu đường, đau khớp…); người lớn ít vận động. Có người thân đồng hành càng tốt</td></tr>
<tr><th>Không dành cho</th><td>Người đang đau ngực, khó thở khi nghỉ, đang sốt, vừa ngã chưa khám; người nằm liệt giường cần nhân viên phục hồi chức năng; thay thế chương trình phục hồi bác sĩ đã chỉ định</td></tr>
<tr><th>Thời lượng</th><td>10 bài, mỗi tuần 1 bài 25 phút: đọc 10 phút, tập 10 phút, ghi lại 5 phút. Các ngày khác tập ngắn 10–20 phút</td></tr>
<tr><th>Cần có</th><td>Ghế chắc có lưng tựa, chai nước 0,5–1,5 lít, một bức tường trống, giày đế bám; Sổ vận động an toàn in sẵn</td></tr>
<tr><th>Cách tập</th><td>Mỗi động tác có 3 mức dễ – vừa – khó. Luôn bắt đầu ở mức dễ</td></tr>
<tr><th>Tình trạng</th><td>Đủ 10 bài, bản chưa dạy thử, chưa có chuyên gia duyệt. Rất cần góp ý của bác sĩ, chuyên viên vật lý trị liệu, phục hồi chức năng</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bạn biết khi nào cần hỏi bác sĩ trước, và ba đèn tập luyện.</li><li>Bạn đứng dậy thường hơn, ngồi lì ít hơn.</li><li>Bạn tập được 5–10 phút mỗi ngày trên ghế, ở mức dễ.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: một ít vẫn hơn không; so với chính mình; nghỉ cũng là một phần của tập.</li><li>Kỹ năng: tự chọn mức, tự đo, tự tăng giảm; đứng dậy an toàn sau khi ngã.</li><li>Một lịch tuần dùng được nhiều năm.</li></ul></div>
</div>
{figure_block('KHOAX')}

<h2 id="muoi-bai">Mười bài</h2>
<div class="table-wrap"><table>
<thead><tr><th>Bài</th><th>Tên</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>

<h2>Đo đầu và cuối khóa</h2>
<ul><li>Tuần 1, 5, 10: số lần đứng lên – ngồi xuống trong 30 giây (nếu không cần chống tay), phút đi bộ liền một lần, bậc thăng bằng.</li>
<li>Bài 1 và bài 10: bảng tự theo dõi 0–1–2.</li>
<li>Đây là tự theo dõi, không phải bằng chứng khóa có hiệu quả.</li></ul>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Sổ vận động an toàn</a>: phiếu Trước khi tập, thẻ đèn tập luyện, đếm lần đứng dậy, động tác 3 mức, đo 30 giây, kế hoạch đi bộ, Kế hoạch khi ngã, lịch tuần.</li></ul>

<h2>Cho người đồng hành</h2>
<ul>
<li>Đọc phiếu Trước khi tập cùng nhau. Có ý "Có" thì giúp đặt lịch khám.</li>
<li>Đứng cạnh trong buổi đầu tập thăng bằng và khi đo 30 giây. Không kéo tay.</li>
<li>Để người tập tự làm việc nhỏ, đừng làm hộ hết.</li>
<li>Tập cùng: đi bộ chung, giãn cơ chung.</li>
</ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng ý gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{WHO20}; {WHOFS}; {WHOAGE}</td><td>Bốn loại vận động; số ngày tập sức và thăng bằng; ngồi ít lại; bắt đầu nhỏ, tăng dần</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn toàn cầu của WHO</td></tr>
<tr><td>{BYT}; {BYT2}</td><td>Khuyến nghị cho người từ 60 tuổi và người bệnh mạn tính; dấu hiệu dừng tập</td><td><span class="label">[Đã xác nhận]</span> Cẩm nang của Bộ Y tế, đọc qua báo; chưa đọc văn bản gốc</td></tr>
<tr><td>{SHER}</td><td>Tập thăng bằng, động tác chức năng và sức cơ để phòng té ngã</td><td><span class="label">[Đã xác nhận]</span> Tổng quan Cochrane 108 thử nghiệm, 23.407 người; giảm số lần ngã 23%, chắc chắn cao</td></tr>
<tr><td>{PRT}</td><td>Sức chân, sức tay, tăng dần</td><td><span class="label">[Đã xác nhận]</span> Tổng quan Cochrane 121 thử nghiệm, 6.700 người</td></tr>
<tr><td>{STEADI}; {TALKT}</td><td>Đo 30 giây; phép thử nói chuyện</td><td><span class="label">[Đã xác nhận]</span> Công cụ của CDC</td></tr>
<tr><td>{NHSF}; {NIA}; {BANNER}</td><td>Đứng dậy sau khi ngã; tập an toàn; dấu hiệu cần gọi cấp cứu</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn cho người dân của cơ quan y tế; bác sĩ tim mạch giải thích</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Phần lớn thử nghiệm trên có người hướng dẫn, nhiều buổi, nhiều tháng. Khóa tự học này chưa được thử nghiệm, nên chúng tôi không hứa kết quả.</p>
  <p>Chương trình chỉ đi bộ chưa chắc giảm té ngã; vì vậy khóa có bài thăng bằng và sức chân. Tác dụng của giãn cơ lên té ngã chưa được nghiên cứu riêng.</p>
  <p>Khóa không chẩn đoán, không thay thế khám bệnh hay phục hồi chức năng. Đang tập theo chỉ định của nhân viên y tế: làm theo họ trước, dùng khóa như phần tập thêm sau khi hỏi họ.</p>
</div>

<h2>An toàn cho mọi bài</h2>
<ul><li>{ASK}</li><li>{EMERG}</li><li>Người khuyết tật vận động, nhìn, nghe: xem thêm khóa <a href="/khoa-hoc/tu-lap-tung-buoc/">Tự lập từng bước</a>.</li></ul>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai. Xin không ghi tên, nơi ở hay bệnh của người khác.</p>
{HELP_BOX}
''', current='/ca-nhan/')
print('C9 built')
