# Khóa G2 "Gia đình 0–2 tuổi – Giao và Đáp" – trang khóa, 8 bài, 1 công cụ in
import illus_g2  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

U = '/khoa-hoc/gia-dinh-0-2/'
TOOL = '/cong-cu/nhat-ky-giao-dap/'
def url(w, slug): return f'{U}tuan-{w}/{slug}/'
def sec(n, title, body): return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'
def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>{need}</em></p><ol>{li}</ol>{nt}</div>'
def ages(a, b, c, sib):
    return (f'<h3>0–6 tháng</h3>{ol(a)}<h3>6–12 tháng</h3>{ol(b)}<h3>12–24 tháng (và đến gần 3 tuổi)</h3>{ol(c)}'
            f'<h3>Anh chị cùng chơi (5–8 tuổi)</h3>{ul(sib)}')
JOURNAL = ('<div class="table-wrap journal"><table><tbody>'
           '<tr><th class="w38">Con đã giao bằng cách nào</th><td></td></tr><tr><th>Mình đã đáp thế nào</th><td></td></tr>'
           '<tr><th>Tuần sau thử gì khác</th><td></td></tr></tbody></table></div>')

HARV = '<a href="https://developingchild.harvard.edu/resources/videos/how-to-5-steps-for-brain-building-serve-and-return/">Harvard Center on the Developing Child</a>'
HARV_PDF = '<a href="https://bettercarenetwork.org/sites/default/files/HCDC_ServeReturn_for_Parents_Caregivers_2019.pdf">Harvard – Serve and Return for Parents (2019)</a>'
JAM = '<a href="https://sciencedaily.com/releases/2014/05/140529142354.htm">Gertler et al. 2014, <em>Science</em></a>'
REACH = '<a href="https://reachupandlearn.com/resources/">Reach Up</a>'
SLEEP = '<a href="https://aap.org/en/news-room/news-releases/aap/2022/american-academy-of-pediatrics-updates-safe-sleep-recommendations-back-is-best">AAP 2022 – ngủ an toàn</a>'
WHO = '<a href="https://new.chconline.org/new-who-guidelines-on-physical-activity-sedentary-behaviour-and-sleep-for-children-under-5-years-of-age">WHO 2019 – vận động, ngồi, ngủ cho trẻ dưới 5 tuổi</a>'
READ = '<a href="https://www.physiciansweekly.com/aap-why-literacy-promotion-is-crucial-during-clinical-visits/">AAP 2024 – khuyến khích đọc sách</a>'
AHT = '<a href="https://webarchive.library.unt.edu/web/20201221232327/https://www.cdc.gov/violenceprevention/childabuseandneglect/Abusive-Head-Trauma.html">CDC – phòng chấn thương đầu do bạo hành</a>'
MILE = '<a href="https://www.cdc.gov/ncbddd/actearly/milestones/index.html">CDC – Learn the Signs. Act Early</a>'
MILE2 = '<a href="https://www.disabilityscoop.com/2022/02/10/cdc-revises-developmental-milestones-for-young-kids/29698/">bản sửa năm 2022</a>'
SMALL = 'Mọi đồ trong tầm với của con phải to hơn lõi giấy vệ sinh. Không pin cúc áo, nam châm nhỏ, túi nilon, dây dài hơn 30 cm.'
WATCH = 'Luôn có người lớn ngồi cạnh. Không để anh chị dưới 12 tuổi trông em một mình.'

L = {
 '1': (1, 'nhan-ra-loi-giao', 'Bài 1', 'Nhận ra lời "giao" của con'),
 '2': (2, 'dap-lai', 'Bài 2', 'Đáp lại'),
 '3': (3, 'goi-ten', 'Bài 3', 'Gọi tên'),
 '4': (4, 'thay-phien-va-cho', 'Bài 4', 'Thay phiên và chờ'),
 '5': (5, 'ket-thuc-va-bat-dau', 'Bài 5', 'Kết thúc và bắt đầu'),
 '6': (6, 'doc-sach-hat-ke', 'Bài 6', 'Đọc sách, hát, kể chuyện'),
 '7': (7, 'van-dong-do-choi-tu-lam', 'Bài 7', 'Vận động và đồ chơi tự làm'),
 '8': (8, 'khi-con-khoc-khi-bo-me-met', 'Bài 8', 'Khi con khóc, khi bố mẹ mệt'),
}
ORDER = list(L)
def link(k):
    w, slug, code, title = L[k]; return (url(w, slug), f'{code} – {title}')

def lesson(k, desc, sections):
    w, slug, code, title = L[k]; i = ORDER.index(k)
    prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
    nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
    key = 'g2-' + k
    note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này đã soạn theo khung của khóa nhưng chưa được dạy thử trong gia đình. '
            f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
    share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn.</p>'
             f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về {code.lower()}</a></p></div>')
    meta = [f'Tuần {w}', 'Bố mẹ đọc 10 phút', 'Chơi 5 phút mỗi ngày']
    body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">Gia đình 0–2 tuổi</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block('R' + k)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
    page(url(w, slug), f'{code} – {title}', desc, body, current='/gia-dinh/')

# ======================= BÀI 1 =======================
lesson('1', 'Khóa Gia đình 0–2 tuổi, bài 1: nhận ra lời "giao" của con qua ánh mắt, tiếng bập bẹ, chỉ tay, và cùng nhìn theo con.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> trong 5 phút quan sát, ghi được ít nhất 5 lần con "giao" và con giao bằng cách nào.',
   '<strong>Con:</strong> được người lớn chú ý theo điều con đang để ý, ít nhất 5 phút mỗi ngày.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul([f'In <a href="{TOOL}">Nhật ký giao và đáp</a>, hoặc dùng giấy và bút.', 'Chọn lúc con tỉnh táo, no, không buồn ngủ.', 'Úp điện thoại, tắt tivi.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Em bé chưa nói được vẫn luôn "giao": nhìn, bập bẹ, cười, chỉ tay, với lấy, khóc. '
   'Mỗi lần như vậy, con đang mời người lớn vào cuộc chơi. Tuần này chỉ tập một việc: <strong>nhận ra lời giao</strong> và <strong>cùng nhìn theo con</strong>.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày', ages(
   ['Bế con cách mặt mình khoảng 20–30 cm. Để ý con nhìn mắt mình, nhìn đi chỗ khác, hay cựa quậy.', 'Ghi lại: con nhìn bao lâu, con phát ra tiếng gì.'],
   ['Ngồi trên sàn cùng con. Con nhìn hay với đồ nào, bố mẹ nhìn theo đồ đó.', 'Đếm số lần con nhìn lên mặt bố mẹ để "kiểm tra".'],
   ['Để con dẫn: con chỉ đâu, bố mẹ nhìn đó. Con mang đồ đến, bố mẹ nhận và nhìn đồ đó cùng con.', 'Đừng đổi trò khi con đang mải mê.'],
   ['Anh chị làm "thám tử": "Em đang nhìn gì nhỉ?" Anh chị kể cho bố mẹ.', 'Anh chị ngồi ngang tầm em, không giành đồ chơi của em.'])),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Con hay giao bằng cách nào nhất?', 'Lúc nào trong ngày con giao nhiều nhất?', 'Mình đã lỡ lời giao nào vì đang bận điện thoại?'])),
 sec(6, 'An toàn', ul([SMALL, WATCH])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 5 phút, một tờ giấy.', [
   ('Phút 0–1.', 'Úp điện thoại, ngồi ngang tầm con.'), ('Phút 1–4.', 'Nhìn theo con nhìn. Đếm lời giao.'), ('Phút 4–5.', 'Ghi vào nhật ký.')], [
   ('Gọi video với bố:', 'bố cũng tập nhận ra lời giao qua màn hình: con nhìn camera, con cười, con với tay.'),
   ('Nhắn bố 1 câu:', 'cách con giao nhiều nhất hôm nay.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> 5 phút, ghi số lời giao.', '<strong>Cuối tuần:</strong> so ngày đầu và ngày cuối. Mình nhận ra nhiều hơn chưa?'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Bước 1 của "giao và đáp": nhận ra lời giao và cùng chú ý điều con đang chú ý ({HARV_PDF}).'),
   lb('Đã xác nhận', f'Trang của {HARV} dẫn các nghiên cứu liên hệ giữa tương tác qua lại và hoạt động não; đây phần lớn là nghiên cứu liên hệ, chưa chứng minh nhân quả.'),
   lb('Đánh giá chuyên môn', 'Gợi ý theo tháng tuổi và phần anh chị cùng chơi do daynentang.com soạn.')]))
])

# ======================= BÀI 2 =======================
lesson('2', 'Khóa Gia đình 0–2 tuổi, bài 2: đáp lại lời giao của con bằng nụ cười, cái chạm, lời nói, ngay và ấm áp.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> đáp lại ít nhất 10 lời giao trong 5 phút chơi, bằng ít nhất 3 cách khác nhau.', '<strong>Con:</strong> giao nhiều hơn khi thấy được đáp.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul(['Nhật ký giao và đáp.', 'Vài đồ chơi to, an toàn hoặc đồ dùng quen: thìa gỗ, nồi nhựa, khăn.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Khi con giao, bố mẹ <strong>đáp</strong>: cười, gật đầu, chạm nhẹ, nói, đưa đồ con đang với. '
   'Đáp không cần đúng, chỉ cần ấm áp và kịp lúc. Khi lời giao không được đáp, con có thể dần ít giao hơn.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày', ages(
   ['Con ê a: bố mẹ ê a lại, giọng cao và chậm. Con cười: bố mẹ cười lại.', 'Con nhìn đi chỗ khác: để con nghỉ, không ép con nhìn.'],
   ['Con đập tay xuống sàn: bố mẹ đập theo. Con đưa đồ: nhận và nói "Cảm ơn con".', 'Con với đồ xa: đưa đồ lại gần, để con tự cầm.'],
   ['Con chỉ: bố mẹ nhìn, gật đầu và nói. Con mang sách: ngồi xuống mở cùng.', 'Con nói một từ: nhắc lại từ đó và thêm một từ. "Bóng!" → "Bóng đỏ!"'],
   ['Anh chị bắt chước em: em vỗ tay, anh chị vỗ tay. Em cười là anh chị thắng.', 'Bố mẹ khen anh chị: "Con đáp em rất nhanh."'])),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Cách đáp nào làm con vui nhất?', 'Lúc mệt, mình đáp bằng cách nào ít tốn sức nhất? (nụ cười, cái gật đầu)', 'Có lúc nào mình đáp quá nhiều, làm con mệt không?'])),
 sec(6, 'An toàn', ul([SMALL, WATCH, 'Đồ bếp dùng chơi phải là đồ nhựa hoặc gỗ, không sắc, không nóng.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 5 phút, vài đồ quen.', [
   ('Phút 0–1.', 'Ngồi ngang tầm con.'), ('Phút 1–4.', 'Mỗi lời giao, mẹ đáp một cách. Thử đủ: cười, chạm, nói, đưa đồ.'), ('Phút 4–5.', 'Ghi cách đáp con thích nhất.')], [
   ('Khi đang làm việc nhà:', 'vẫn đáp được: nhìn con, cười, nói một câu, rồi làm tiếp.'), ('Nhắn bố 1 câu:', 'cách đáp con thích nhất.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> 5 phút đáp lại, đếm số lần.', '<strong>Cuối tuần:</strong> con có giao nhiều hơn không?'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Bước 2: đáp lại bằng sự hỗ trợ và khích lệ: an ủi, chơi, gật đầu, mỉm cười ({HARV_PDF}).'),
   lb('Suy luận', '"Lời giao không được đáp thì con ít giao hơn" là cách nói đơn giản của chúng tôi, không phải số liệu đo được.'),
   lb('Đánh giá chuyên môn', 'Cách "nhắc lại và thêm một từ" là kỹ thuật phổ biến trong hướng dẫn ngôn ngữ sớm; bài do daynentang.com soạn.')]))
])

# ======================= BÀI 3 =======================
lesson('3', 'Khóa Gia đình 0–2 tuổi, bài 3: gọi tên đồ vật, việc làm và cảm xúc của con; nói to việc mình đang làm.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> trong 5 phút, gọi tên ít nhất 10 lần: đồ vật, hành động, cảm xúc.', '<strong>Con 12–24 tháng:</strong> chỉ đúng hoặc nói được ít nhất 1 từ mới trong tuần.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul(['5 đồ quen trong nhà: cốc, thìa, khăn, quả cam, dép.', 'Nhật ký giao và đáp.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Khi con nhìn, chỉ hay làm gì, bố mẹ <strong>gọi tên</strong> điều đó bằng câu ngắn. '
   'Gọi tên cả cảm xúc: "Con vui", "Con bực vì rơi đồ". Con chưa nói được vẫn đang học. Dùng ngôn ngữ bố mẹ nói thạo và tự nhiên nhất.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày', ages(
   ['Thay tã, tắm: kể to việc đang làm. "Mẹ cởi áo. Nước ấm. Con đạp chân."', 'Giọng chậm, câu ngắn, nhìn mặt con.'],
   ['Con cầm đồ nào, gọi tên đồ đó. "Cái thìa. Thìa gõ cộc cộc."', 'Chỉ đồ và gọi tên khi đi quanh nhà.'],
   ['Hỏi "Cốc đâu?" và chờ con chỉ. Con chỉ đúng: "Đúng rồi, cái cốc."', 'Gọi tên cảm xúc khi con khóc, cười, bực. "Con buồn vì bố đi làm."'],
   ['Anh chị làm "người kể chuyện": kể to việc em đang làm. "Em đang xếp khối!"', 'Anh chị dạy em một từ mới mỗi ngày.'])),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Hôm nay mình đã gọi tên cảm xúc của con lần nào?', 'Từ nào con hiểu mà chưa nói?', 'Mình có đang nói quá nhanh, quá dài không?'])),
 sec(6, 'An toàn', ul([SMALL, 'Quả cam, quả to chỉ để chơi khi nguyên vỏ. Đồ ăn cho trẻ dưới 4 tuổi: cắt nhỏ, bỏ hạt; không cho ăn nho nguyên quả, hạt nguyên.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 5 đồ quen, 5 phút.', [
   ('Phút 0–3.', 'Đưa từng đồ, gọi tên 2 lần, để con cầm.'), ('Phút 3–5.', 'Hỏi "… đâu?", chờ con chỉ.')], [
   ('Trong ngày:', 'nói to việc mẹ đang làm khi nấu cơm, phơi đồ. Không cần thêm thời gian riêng.'), ('Nhắn bố 1 câu:', 'từ mới con hiểu hoặc nói.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> 5 phút gọi tên, cộng kể to việc mình làm.', '<strong>Cuối tuần:</strong> ghi các từ con đã hiểu hoặc nói.'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Bước 3: gọi tên điều con đang thấy, làm hay cảm thấy; gọi tên giúp xây kết nối ngôn ngữ ngay cả trước khi con biết nói ({HARV_PDF}).'),
   lb('Đã xác nhận', f'Chương trình ở Jamaica dạy mẹ nói chuyện với con, gọi tên đồ vật, hành động và khen con. Sau khoảng 20 năm, nhóm được can thiệp có thu nhập cao hơn 25% ({JAM}).'),
   lb('Đánh giá chuyên môn', '"Dùng ngôn ngữ bố mẹ nói thạo nhất" là khuyên của chúng tôi để lời nói tự nhiên, giàu từ.')]))
])

# ======================= BÀI 4 =======================
lesson('4', 'Khóa Gia đình 0–2 tuổi, bài 4: thay phiên và chờ: đến lượt con thì bố mẹ chờ đếm thầm 5–10, chơi ú òa.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> chờ đếm thầm đến 5–10 trước khi nói tiếp, ít nhất 5 lần trong 5 phút chơi.', '<strong>Con:</strong> có ít nhất 3 lượt qua lại liên tiếp trong một trò.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul(['Một chiếc khăn mỏng cho trò ú òa.', 'Một quả bóng mềm to hơn 4,4 cm (to hơn quả bóng bàn nhiều).'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Cuộc trò chuyện là chuyền qua lại. Bố mẹ hay nói liền, không chừa lượt cho con. '
   'Tuần này tập <strong>chờ</strong>: sau khi nói, đếm thầm 5 đến 10 để con kịp đáp bằng tiếng, cử chỉ hay ánh mắt.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày', ages(
   ['Bố mẹ ê a, rồi im lặng chờ. Con ê a lại thì đáp tiếp. Như một cuộc nói chuyện.', 'Lè lưỡi, chờ, xem con có bắt chước không.'],
   ['Ú òa với khăn: che mặt mình, chờ, rồi "ú òa". Sau vài lần, chờ lâu hơn để con kéo khăn.', 'Lăn bóng qua lại: lăn đi, chờ con đẩy lại.'],
   ['Hỏi một câu, chờ đếm đến 10. Con đáp bằng từ hay chỉ tay đều được.', 'Trò "đến lượt ai": xếp khối, mỗi người một khối.'],
   ['Anh chị chơi lăn bóng với em, đếm "1, 2, 3, đến lượt em".', 'Anh chị tập chờ em, không lấy lượt của em.'])),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Chờ 10 giây có khó không? Vì sao?', 'Khi mình chờ, con làm gì?', 'Trò nào con chơi được nhiều lượt nhất?'])),
 sec(6, 'An toàn', ul(['Khăn chỉ dùng khi chơi, không để trong giường ngủ của con.', 'Bóng to hơn 4,4 cm; không dùng bóng bay.', WATCH])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: khăn, bóng mềm, 5 phút.', [
   ('Phút 0–3.', 'Ú òa, chờ lâu dần.'), ('Phút 3–5.', 'Lăn bóng qua lại, đếm số lượt.')], [
   ('Gọi video với bố:', 'chơi ú òa qua màn hình: bố che mặt bằng tay, chờ, rồi "ú òa".'), ('Nhắn bố 1 câu:', 'số lượt qua lại dài nhất.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> 5 phút, đếm lượt qua lại dài nhất.', '<strong>Cuối tuần:</strong> chuỗi lượt dài hơn đầu tuần chưa?'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Bước 4: thay phiên và chờ; cho con thời gian đáp giúp con tập tự kiểm soát và tự tin ({HARV_PDF}).'),
   lb('Đánh giá chuyên môn', 'Con số "đếm thầm 5–10" là gợi ý thực hành của daynentang.com, không phải con số từ nghiên cứu.')]))
])

# ======================= BÀI 5 =======================
lesson('5', 'Khóa Gia đình 0–2 tuổi, bài 5: nhận ra khi con muốn dừng hay muốn đổi trò; để con dẫn; kèm hướng dẫn ngủ an toàn.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> nhận ra ít nhất 3 dấu hiệu con muốn dừng, và để con dẫn sang trò mới.', '<strong>Bố mẹ:</strong> chỗ ngủ của con đạt đủ 4 điều trong mục An toàn.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul(['Nhật ký giao và đáp.', 'Kiểm tra chỗ ngủ của con.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Mọi cuộc chơi đều có lúc kết thúc. Con quay mặt đi, ngáp, dụi mắt, cáu hay với đồ khác là con đang nói "đủ rồi". '
   'Bố mẹ dừng, đổi trò, hoặc cho con nghỉ. Để con dẫn sang việc mới giúp con thấy mình được hiểu.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày', ages(
   ['Khi con quay mặt đi, dừng nói, để con nghỉ. Con nhìn lại thì chơi tiếp.', 'Ghi các dấu hiệu buồn ngủ của con.'],
   ['Con bỏ đồ này, với đồ khác: đi theo con sang đồ mới.', 'Báo trước khi dừng: "Một lần nữa rồi đi tắm nhé."'],
   ['Báo trước và cho chọn: "Sắp ăn cơm. Con cất bóng hay cất khối trước?"', 'Có câu kết quen: "Chào khối, hẹn mai gặp."'],
   ['Anh chị hỏi em "Em muốn chơi nữa không?" và nhìn em trả lời.', 'Anh chị tập dừng khi em quay đi, không ép em chơi tiếp.'])),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Dấu hiệu "đủ rồi" của con là gì?', 'Mình có hay kéo dài trò chơi khi con đã mệt?', 'Câu kết quen của nhà mình là gì?'])),
 sec(6, 'An toàn – ngủ an toàn', ul(['Đặt con <strong>nằm ngửa</strong> cho mọi giấc ngủ.', 'Mặt nằm <strong>phẳng, cứng</strong>, không nghiêng. Không gối, chăn, thú bông, đệm mềm trong chỗ ngủ.',
   'Ngủ <strong>cùng phòng</strong> với bố mẹ, nhưng <strong>không chung giường</strong>, tốt nhất ít nhất 6 tháng đầu.',
   'Không cho con ngủ thường xuyên trong ghế ô tô, xe đẩy, võng. Không hút thuốc gần con.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 5 phút chơi, 5 phút kiểm chỗ ngủ.', [
   ('Phút 0–5.', 'Chơi, để ý dấu hiệu con muốn dừng, đi theo con.'), ('Sau đó.', 'Kiểm chỗ ngủ theo 4 điều.')], [
   ('Ngủ cùng giường là thói quen nhiều nhà:', 'nếu khó đổi ngay, hãy hỏi bác sĩ nhi cách làm an toàn nhất cho nhà mình.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> báo trước khi dừng trò.', '<strong>Cuối tuần:</strong> ghi 3 dấu hiệu "đủ rồi" của con.'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Bước 5: tập kết thúc và bắt đầu; nhận ra khi con xong và để con dẫn sang việc mới ({HARV_PDF}).'),
   lb('Đã xác nhận', f'Khuyến nghị ngủ an toàn: nằm ngửa, mặt phẳng cứng, không đồ mềm, ngủ cùng phòng không chung giường ít nhất 6 tháng đầu, không dùng ghế ngồi để ngủ thường xuyên ({SLEEP}).'),
   lb('Đánh giá chuyên môn', 'Câu kết quen và báo trước là kỹ thuật phổ biến; bài do daynentang.com soạn.')]))
])

# ======================= BÀI 6 =======================
lesson('6', 'Khóa Gia đình 0–2 tuổi, bài 6: đọc sách, hát, kể chuyện cùng con từ lúc mới sinh; làm sách tranh từ đồ trong nhà.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> đọc hoặc hát cùng con ít nhất 5 phút mỗi ngày, 6/7 ngày.', '<strong>Bố mẹ:</strong> làm 1 cuốn sách tranh tự làm 4–6 trang.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul(['1–2 cuốn sách tranh bìa cứng hoặc sách vải.', 'Bìa cứng, ảnh in hoặc tranh vẽ đồ quen, băng dính, dây buộc ngắn.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Đọc sách là giao và đáp có tranh. Không cần đọc hết chữ. Con chỉ, bố mẹ gọi tên; con lật trang, bố mẹ chờ. '
   'Hát ru, đồng dao, kể chuyện về ngày hôm nay cũng tính. Bắt đầu từ lúc mới sinh.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày', ages(
   ['Cho con nhìn tranh to, tương phản. Đọc bằng giọng vui, chậm.', 'Hát một bài ru quen mỗi tối.'],
   ['Để con cầm, sờ, gặm sách vải, sách bìa cứng. Gọi tên tranh con nhìn.', 'Đồng dao có động tác tay.'],
   ['Hỏi "… đâu?" và chờ con chỉ. Để con lật trang.', 'Kể lại chuyện trong ngày bằng 3 câu: "Sáng nay mình ra chợ. Mình mua cam. Con cầm cam."'],
   ['Anh chị "đọc" sách tranh cho em, kể bằng lời của mình.', 'Anh chị cùng làm sách tự làm: vẽ đồ em thích.'])) +
   '<h3>Làm sách tranh tự làm (15 phút, một lần)</h3>' + ol(['Cắt 4–6 tấm bìa cứng bằng nhau.', 'Dán ảnh hoặc vẽ đồ quen: cốc, mèo, ông bà, xe máy.', 'Dán băng dính trong phủ kín mặt để chống ướt.', 'Đục lỗ, buộc dây ngắn, thắt nút chặt.']),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Con thích trang nào nhất?', 'Giờ đọc nào hợp nhất với nhà mình?', 'Ai trong nhà có thể đọc thay khi mình bận?'])),
 sec(6, 'An toàn', ul([SMALL, 'Dây buộc sách thắt chặt, ngắn; kiểm tra sách tự làm mỗi tuần, bỏ trang bong tróc.', 'Ảnh gia đình trong sách: chỉ dùng ở nhà, không đăng lên mạng.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: 1 cuốn sách, 5 phút trước giờ ngủ.', [
   ('Phút 0–4.', 'Đọc theo kiểu giao và đáp: chỉ, gọi tên, chờ.'), ('Phút 4–5.', 'Hát bài ru quen.')], [
   ('Gọi video với bố:', 'bố đọc một trang sách qua điện thoại, mẹ cầm sách thật cho con xem.'), ('Nhắn bố 1 câu:', 'trang con thích nhất.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> 5 phút đọc hoặc hát.', '<strong>Cuối tuần:</strong> đếm số ngày đã đọc.'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Tuyên bố chính sách AAP (tạp chí <em>Pediatrics</em>, 2024) khuyến khích bố mẹ đọc to cho con bắt đầu từ lúc mới sinh ({READ}).'),
   lb('Đã xác nhận', f'WHO khuyến khích đọc và kể chuyện cùng người chăm sóc khi trẻ dưới 5 tuổi ngồi yên ({WHO}).'),
   lb('Đã xác nhận', f'{REACH} dùng sách và đồ chơi tự làm từ vật liệu sẵn có trong chương trình thăm nhà.'),
   lb('Đánh giá chuyên môn', 'Cách làm sách tự làm trong bài do daynentang.com soạn.')]))
])

# ======================= BÀI 7 =======================
lesson('7', 'Khóa Gia đình 0–2 tuổi, bài 7: vận động mỗi ngày theo tuổi và đồ chơi tự làm an toàn từ đồ có sẵn.', [
 sec(1, 'Mục tiêu', ul(['<strong>Con dưới 1 tuổi:</strong> nằm sấp khi thức, cộng lại ít nhất 30 phút mỗi ngày (khi con chưa bò).',
   '<strong>Con 1–2 tuổi:</strong> vận động cộng lại ít nhất 180 phút mỗi ngày.', '<strong>Bố mẹ:</strong> làm 2 đồ chơi tự làm đạt kiểm tra an toàn.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul(['Chai nhựa dày có nắp, hộp giấy, hộp sữa rỗng đã rửa sạch.', 'Băng dính khỏe, kéo (người lớn dùng).', 'Một tấm thảm hoặc chiếu sạch trên sàn.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Con học bằng cả cơ thể. Bố mẹ giao và đáp ngay trong lúc con lật, bò, đi. '
   'Đồ chơi tốt không cần mua: chai lắc, hộp thả đồ, hộp xếp chồng làm từ đồ có sẵn. Hạn chế để con ngồi lâu một chỗ.</p>'),
 sec(4, 'Chơi 5 phút mỗi ngày (cộng vận động cả ngày)', ages(
   ['Nằm sấp trên chiếu khi con thức, bố mẹ nằm đối diện, nói chuyện. Bắt đầu vài phút, nhiều lần trong ngày.', 'Đặt đồ chơi ngay trước mặt để con ngẩng đầu nhìn.'],
   ['Để đồ hơi xa, con bò đến lấy. Bố mẹ gọi tên đồ và khen.', 'Chai lắc: con lắc, bố mẹ lắc theo (giao và đáp).'],
   ['Hộp thả đồ: con thả khối vào lỗ, mở hộp, lấy ra, thả lại.', 'Đi dạo, leo bậc thấp có người lớn nắm tay, đá bóng to.'],
   ['Anh chị làm "huấn luyện viên": bò cùng em, đếm số bậc em leo.', 'Anh chị tự làm hộp xếp chồng tặng em.'])) +
   '<h3>Ba đồ chơi tự làm</h3>' + ul(['<strong>Chai lắc:</strong> chai nhựa dày, cho ít gạo hoặc nước màu; dán chặt nắp bằng băng dính, kiểm tra mỗi ngày.',
   '<strong>Hộp thả đồ:</strong> hộp giấy khoét lỗ tròn; đồ thả vào phải to hơn lõi giấy vệ sinh.',
   '<strong>Hộp xếp chồng:</strong> hộp sữa rỗng rửa sạch, dán kín miệng, bọc giấy màu.']),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Hôm nay con ngồi xe đẩy, ghế ăn liền bao lâu?', 'Lúc nào trong ngày con vận động nhiều nhất?', 'Đồ chơi nào con thích nhất? Vì sao?'])),
 sec(6, 'An toàn', ul(['Nằm sấp chỉ khi con thức và có người lớn ngồi cạnh. Ngủ luôn nằm ngửa.', SMALL,
   'Chai lắc: kiểm tra nắp mỗi ngày; nắp lỏng thì bỏ ngay. Không cho hạt, cúc, đồ nhỏ vào chai nếu chai có thể vỡ.', 'Cầu thang, mép bàn: chặn hoặc bọc. Không để con một mình gần nước.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: chiếu sạch, 1 đồ chơi tự làm.', [
   ('Mỗi lần con thức.', 'Vài phút nằm sấp hoặc bò, mẹ nằm đối diện nói chuyện.'), ('Một lần trong tuần.', 'Mẹ làm 1 đồ chơi; con lớn phụ dán giấy màu.')], [
   ('Ngày mưa, nhà chật:', 'trải chiếu giữa phòng, dọn đồ sắc, cho con bò quanh chiếu.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> ước thời gian con vận động.', '<strong>Cuối tuần:</strong> đồ chơi tự làm còn an toàn không?'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'WHO 2019: trẻ dưới 1 tuổi chưa bò cần ít nhất 30 phút nằm sấp khi thức, chia trong ngày; trẻ 1–2 tuổi vận động ít nhất 180 phút mỗi ngày; không ngồi xe đẩy, ghế ăn quá 1 giờ liền ({WHO}).'),
   lb('Đã xác nhận', f'AAP 2022 khuyến khích cho trẻ nằm sấp khi thức, có người giám sát ({SLEEP}).'),
   lb('Đã xác nhận', f'{REACH} dùng đồ chơi tự làm trong chương trình thăm nhà.'),
   lb('Đánh giá chuyên môn', 'Ba đồ chơi và các bước kiểm tra an toàn do daynentang.com soạn; mẹo lõi giấy vệ sinh không thay thế tiêu chuẩn đồ chơi.')]))
])

# ======================= BÀI 8 =======================
lesson('8', 'Khóa Gia đình 0–2 tuổi, bài 8: kế hoạch khi con khóc mãi, chăm sóc bố mẹ, mốc phát triển và đánh giá cuối khóa.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> có <strong>kế hoạch khi con khóc mãi</strong> viết ra, dán ở chỗ dễ thấy, kèm số người có thể gọi giúp.',
   '<strong>Bố mẹ:</strong> xem danh sách mốc phát triển theo tuổi con, chấm phiếu tự đánh giá cuối khóa.'])),
 sec(2, 'Chuẩn bị (2 phút)', ul([f'<a href="{TOOL}">Nhật ký giao và đáp</a>, trang "Kế hoạch khi con khóc".', f'Danh sách mốc theo tuổi con từ {MILE}.'])),
 sec(3, 'Bố mẹ đọc trước (10 phút)', '<p>Em bé khóc là bình thường, nhất là mấy tháng đầu. Có lúc dỗ mãi không nín. '
   'Khi ấy, người lớn mệt và bực là bình thường. Điều quan trọng là có kế hoạch trước, và <strong>không bao giờ lắc con</strong>.</p>'),
 sec(4, 'Làm kế hoạch và ôn khóa', '<h3>Kế hoạch khi con khóc mãi</h3>' + ol([
   '<strong>Kiểm tra:</strong> đói, ướt, nóng, lạnh, đau, sốt? Nghĩ con ốm thì gọi bác sĩ hoặc đưa đi khám.',
   '<strong>Dỗ:</strong> bế, ru nhẹ, hát nhỏ, cho ti giả, bế đi dạo.',
   '<strong>Mình bực:</strong> đặt con nằm ngửa ở chỗ an toàn (cũi, nôi), ra chỗ khác vài phút để bình tĩnh, quay lại xem con mỗi 5–10 phút.',
   '<strong>Gọi người giúp:</strong> viết sẵn tên và số của 2 người có thể gọi: vợ hoặc chồng, ông bà, hàng xóm thân.',
   '<strong>Chỉ giao con</strong> cho người bình tĩnh, không nóng tính.']) +
   '<h3>Ôn 5 bước (cả nhà)</h3>' + ul(['Mỗi người nói một lần mình đã giao và đáp với em bé tuần này.', 'Anh chị kể một trò mình chơi với em giỏi nhất.']) +
   '<h3>Mốc phát triển</h3>' + ul([f'Xem danh sách mốc theo tháng tuổi của con trên {MILE}. Danh sách {MILE2} ghi việc khoảng 75% trẻ cùng tuổi làm được.',
   'Con chưa làm được nhiều mốc, hay mất kỹ năng đã có: hỏi bác sĩ nhi sớm, đừng "chờ xem".', 'Danh sách mốc không thay thế khám sàng lọc của bác sĩ.'])),
 sec(5, 'Câu hỏi bố mẹ tự hỏi', ol(['Lúc nào trong ngày mình dễ bực nhất? Ai có thể đỡ mình lúc đó?', 'Mình ngủ đủ chưa? Mình có ai để tâm sự không?', 'Trong 5 bước, bước nào nhà mình làm tốt nhất?'])),
 sec(6, 'An toàn', ul(['<strong>Không bao giờ lắc, ném hay đánh em bé.</strong> Lắc có thể gây tổn thương não nặng hoặc tử vong.',
   'Mẹ hay bố buồn chán, lo âu kéo dài nhiều tuần sau sinh, hoặc có ý nghĩ làm hại mình hay con: gặp bác sĩ ngay. Gọi 115 khi khẩn cấp; tâm sự với Đường dây Ngày Mai 096 306 1414.',
   'Màn hình: trẻ dưới 2 tuổi không xem màn hình thụ động. Gọi video với bố được, coi như một cuộc giao và đáp.'])),
 sec(7, 'Cho mẹ dạy (khi bố đi vắng)', mom('Mẹ chỉ cần: một tờ giấy, 15 phút, và số điện thoại người giúp.', [
   ('Phút 0–8.', 'Mẹ viết kế hoạch khi con khóc, dán ở cửa tủ lạnh.'), ('Phút 8–15.', 'Mẹ xem danh sách mốc theo tuổi con, đánh dấu điều muốn hỏi bác sĩ.')], [
   ('Khi bố đi công tác dài ngày:', 'hẹn trước một người (ông bà, hàng xóm) có thể sang đỡ mẹ vào giờ con hay khóc.'),
   ('Mẹ cũng cần nghỉ:', 'mỗi ngày nhờ người trông con 30 phút để mẹ ngủ, tắm, ăn yên.')])),
 sec(8, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> xem lại danh sách mốc theo tuổi con.', '<strong>Sau 3 tháng:</strong> chấm lại phiếu tự đánh giá giao và đáp.'])),
 sec(9, 'Nhật ký trong tuần', JOURNAL),
 sec(10, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'CDC: khóc là nguyên nhân chính khiến người chăm sóc bực và lắc trẻ; trẻ dưới 1 tuổi có nguy cơ cao nhất. Lời khuyên: kiểm tra trẻ có ốm không, thử dỗ, đặt trẻ chỗ an toàn và tạm rời đi khi bực, gọi người giúp; không bao giờ lắc trẻ ({AHT}, bản lưu trữ).'),
   lb('Đã xác nhận', f'Danh sách mốc CDC sửa năm 2022 dùng ngưỡng 75% trẻ, thêm mốc 15 và 30 tháng; mục đích là để gia đình trao đổi với bác sĩ, không "chờ xem" ({MILE2}).'),
   lb('Đã xác nhận', f'WHO 2019: không khuyến nghị màn hình cho trẻ dưới 1 tuổi và 1 tuổi; trẻ 2 tuổi tối đa 1 giờ ({WHO}).'),
   lb('Đánh giá chuyên môn', 'Coi gọi video với bố là ngoại lệ của khóa vì đó là tương tác qua lại với người thân; chúng tôi chưa đọc nguồn gốc cho ngoại lệ này.')]))
])

# =============== TRANG KHÓA ===============
rows = ''.join(f'<tr><td>{L[k][0]}</td><td><a href="{link(k)[0]}">{L[k][3]}</a></td><td>{g}</td></tr>' for k, g in zip(ORDER, [
 '≥5 lời giao ghi được trong 5 phút', '≥10 lần đáp, 3 cách khác nhau', '≥10 lần gọi tên trong 5 phút', 'Chuỗi ≥3 lượt qua lại',
 'Nhận ra 3 dấu hiệu "đủ rồi"; chỗ ngủ an toàn', 'Đọc hoặc hát ≥5 phút, 6/7 ngày', 'Vận động theo khuyến nghị WHO; 2 đồ chơi tự làm', 'Kế hoạch khi con khóc; chấm phiếu cuối khóa']))
page(U, 'Gia đình 0–2 tuổi – Giao và Đáp',
 'Khóa 8 tuần miễn phí cho bố mẹ có con 0–2 tuổi: 5 phút giao và đáp mỗi ngày, đọc sách, vận động, ngủ an toàn, khi con khóc.',
f'''
<p class="eyebrow">Gia đình · Khóa G2 · Đang thử nghiệm</p>
<h1>Gia đình 0–2 tuổi – Giao và Đáp</h1>
<p class="lead">Mỗi ngày 5 phút chơi qua lại với con: con "giao" bằng ánh mắt, tiếng bập bẹ, chỉ tay; bố mẹ "đáp" lại. Việc nhỏ, làm đều, xây nền cho ngôn ngữ và gắn bó.</p>

<div class="table-wrap"><table><tbody>
<tr><th>Mục đích</th><td>Bố mẹ có thói quen giao và đáp hằng ngày; nhà an toàn cho em bé; có kế hoạch khi con khóc</td></tr>
<tr><th>Dành cho</th><td>Bố mẹ, ông bà, người chăm trẻ từ sơ sinh đến khoảng 3 tuổi. Mỗi bài có gợi ý cho anh chị 5–8 tuổi cùng chơi</td></tr>
<tr><th>Thời lượng</th><td>8 tuần. Mỗi tuần bố mẹ đọc 1 bài (10 phút), chơi với con 5 phút mỗi ngày</td></tr>
<tr><th>Cần có</th><td>Đồ có sẵn trong nhà, giấy bút. Con không cần màn hình</td></tr>
<tr><th>Tình trạng</th><td>Đủ 8 tuần, bản chưa dạy thử, sẽ sửa theo nhật ký dạy thật</td></tr>
</tbody></table></div>

<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>
    <ul><li>Bố mẹ nhận ra và đáp lại lời giao của con nhiều hơn.</li><li>Mỗi ngày có 5 phút chơi không điện thoại.</li><li>Chỗ ngủ của con an toàn.</li></ul></div>
  <div class="card"><h3>Xây lâu dài</h3>
    <ul><li>Cách nghĩ: em bé học qua tương tác với người thân.</li><li>Kỹ năng: 5 bước giao và đáp, đọc sách từ sớm.</li><li>Kế hoạch khi con khóc, biết khi nào hỏi bác sĩ.</li></ul></div>
</div>

<h2>Giao và đáp là gì?</h2>
{figure_block('KHOAR')}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<p class="small muted">Nhà có cả con 2 tuổi và con lớn hơn? Học song song với khóa <a href="/khoa-hoc/gia-dinh-2-8/">Gia đình 2–8 tuổi</a>; phần "Anh chị cùng chơi" giúp con lớn tham gia.</p>

<h2>Công cụ</h2>
<ul><li><a href="{TOOL}">Nhật ký giao và đáp</a>: bảng 5 phút mỗi ngày, kế hoạch khi con khóc, phiếu tự đánh giá.</li></ul>

<h2>Xem trước khi bắt đầu</h2>
<ul><li><a href="https://developingchild.harvard.edu/resources/videos/how-to-5-steps-for-brain-building-serve-and-return/">5 bước "Giao và đáp" – Harvard Center on the Developing Child</a> (video, tiếng Anh)</li>
<li>{HARV_PDF} (tài liệu PDF, tiếng Anh)</li></ul>

<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi mượn ý tưởng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>
<tr><td>{HARV}</td><td>5 bước giao và đáp, mỗi tuần một bước</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn chuyên gia; dựa trên nghiên cứu liên hệ về tương tác và phát triển não</td></tr>
<tr><td>{JAM}; {REACH}</td><td>Dạy bố mẹ chơi, nói chuyện, gọi tên, khen; đồ chơi và sách tự làm</td><td><span class="label">[Đã xác nhận]</span> Thử nghiệm ngẫu nhiên ở Jamaica, thăm nhà hằng tuần; theo dõi khoảng 20 năm, thu nhập cao hơn 25%</td></tr>
<tr><td>{SLEEP}; {WHO}; {READ}</td><td>Ngủ an toàn, vận động, màn hình, đọc sách từ lúc mới sinh</td><td><span class="label">[Đã xác nhận]</span> Khuyến nghị của AAP và WHO</td></tr>
<tr><td>{AHT}; {MILE}</td><td>Kế hoạch khi con khóc; mốc phát triển</td><td><span class="label">[Đã xác nhận]</span> Hướng dẫn của CDC</td></tr>
</tbody></table></div>
<div class="box warn">
  <h3>Giới hạn, nói thật</h3>
  <p><span class="label">[Suy luận]</span> Kết quả ở Jamaica đến từ thăm nhà hằng tuần do nhân viên y tế cộng đồng thực hiện, với trẻ có hoàn cảnh khó khăn.
  Bố mẹ tự học qua trang web chưa được chứng minh cho hiệu quả tương đương. Khóa không thay thế khám sức khỏe định kỳ và tiêm chủng.</p>
</div>

<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai. Xin đừng đăng ảnh hay tên em bé.</p>

<h2>An toàn cho mọi buổi</h2>
<ul><li>{SMALL}</li><li>{WATCH}</li><li>Ngủ: nằm ngửa, mặt phẳng cứng, không đồ mềm, cùng phòng không chung giường.</li><li><strong>Không bao giờ lắc em bé.</strong></li></ul>
{HELP_BOX}
''', current='/gia-dinh/')

# =============== CÔNG CỤ ===============
days = ''.join(f'<th>{d}</th>' for d in ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN'])
STEPS = ['1. Nhận ra lời giao', '2. Đáp lại', '3. Gọi tên', '4. Thay phiên và chờ', '5. Kết thúc và bắt đầu', 'Đọc sách hoặc hát', 'Vận động, nằm sấp']
trows = ''.join(f'<tr><td>{s}</td>' + '<td></td>' * 7 + '</tr>' for s in STEPS)
SELF = ['Mỗi ngày có 5 phút chơi không điện thoại', 'Nhận ra lời giao của con', 'Đáp lại nhanh, ấm áp', 'Gọi tên đồ vật, việc làm, cảm xúc',
        'Chờ con đáp trước khi nói tiếp', 'Nhận ra khi con muốn dừng', 'Đọc hoặc hát cùng con mỗi ngày', 'Chỗ ngủ an toàn', 'Có kế hoạch khi con khóc mãi']
srows = ''.join(f'<tr><td>{s}</td><td></td><td></td></tr>' for s in SELF)
page(TOOL, 'Nhật ký giao và đáp', 'Trang in cho khóa Gia đình 0–2 tuổi: bảng 5 phút giao và đáp mỗi ngày, kế hoạch khi con khóc, phiếu tự đánh giá.',
f'''
<h1>Nhật ký giao và đáp</h1>
<p>Dùng cho khóa <a href="{U}">Gia đình 0–2 tuổi – Giao và Đáp</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Không ghi tên hay ngày sinh của con lên mạng.</p>
{PRINT_ROW}
<h2>1. Bảng 5 phút mỗi ngày</h2>
<p>Đánh dấu bước mình đã làm trong ngày. Tuần nào học bước nào thì chú ý bước đó.</p>
<div class="table-wrap"><table><thead><tr><th>Việc</th>{days}</tr></thead><tbody>{trows}</tbody></table></div>
<p>Ghi chú tuần này (con giao bằng gì, từ mới, trò con thích): ………………………………………………</p>
<h2>2. Kế hoạch khi con khóc mãi</h2>
<ol>
<li><strong>Kiểm tra:</strong> đói? ướt? nóng, lạnh? đau, sốt? Nghĩ con ốm thì gọi bác sĩ.</li>
<li><strong>Dỗ:</strong> bế, ru, hát nhỏ, bế đi dạo.</li>
<li><strong>Mình bực:</strong> đặt con nằm ngửa trong cũi hoặc nôi, ra chỗ khác vài phút, quay lại xem con mỗi 5–10 phút.</li>
<li><strong>Gọi người giúp:</strong> 1. …………………… số ……………… &nbsp; 2. …………………… số ………………</li>
<li><strong>KHÔNG BAO GIỜ LẮC CON.</strong> Cấp cứu: 115.</li>
</ol>
<h2>3. Phiếu tự đánh giá (tuần 1 và tuần 8)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 8</th></tr></thead><tbody>{srows}</tbody></table></div>
<p class="small muted">Phiếu để bố mẹ tự theo dõi, không dùng để chẩn đoán. Lo lắng về sự phát triển của con, hãy hỏi bác sĩ nhi.</p>
''', current='/cong-cu/')
print('G2 built')
