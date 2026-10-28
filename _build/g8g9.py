# Khóa G8 "Nhà gọn, nhà an toàn" và G9 "Gia đình và cộng đồng" – 2 trang khóa, 8 bài, 2 công cụ in
import illus_g8g9  # noqa: F401  (tạo hình trước)
from common import page, HELP_BOX, PRINT_ROW
from illus import figure_block

def sec(n, title, body): return f'<section class="sec"><h2><span class="n">{n}.</span>{title}</h2>{body}</section>'
def ul(items): return '<ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul>'
def ol(items): return '<ol>' + ''.join(f'<li>{x}</li>' for x in items) + '</ol>'
def lb(label, text): return f'<span class="label">[{label}]</span> {text}'
def mom(need, steps, notes):
    li = ''.join(f'<li><strong>{a}</strong> {b}</li>' for a, b in steps)
    nt = ''.join(f'<p><strong>{a}</strong> {b}</p>' for a, b in notes)
    return f'<div class="mom"><p><em>{need}</em></p><ol>{li}</ol>{nt}</div>'
JOURNAL = ('<div class="table-wrap journal"><table><tbody>'
           '<tr><th class="w38">Cả nhà đã làm được gì</th><td></td></tr><tr><th>Con thích gì</th><td></td></tr>'
           '<tr><th>Cần sửa gì</th><td></td></tr></tbody></table></div>')
SMALL = 'Con dưới 3 tuổi: mọi đồ trong tầm với phải to hơn lõi giấy vệ sinh. Không pin cúc áo, nam châm nhỏ, túi nilon trong tầm với.'

def make_course(U, name, prefix, keyp, L, fig):
    ORDER = list(L)
    def url(k): return f'{U}tuan-{L[k][0]}/{L[k][1]}/'
    def link(k): return (url(k), f'{L[k][2]} – {L[k][3]}')
    def lesson(k, desc, sections):
        w, slug, code, title = L[k]; i = ORDER.index(k)
        prev = link(ORDER[i-1]) if i else (U, 'Về trang khóa học')
        nxt = link(ORDER[i+1]) if i < len(ORDER)-1 else (U, 'Về trang khóa học')
        key = f'{keyp}-{k}'
        note = ('<div class="box warn no-print"><p><strong>Bản chưa dạy thử.</strong> Bài này đã soạn theo khung của khóa nhưng chưa được dạy thử trong gia đình. '
                f'Nếu bạn dùng thử, hãy <a href="/chia-se/?bai={key}#gui">chia sẻ</a> điều bạn gặp để chúng tôi sửa bài.</p></div>')
        share = (f'<div class="box share-cta no-print"><h3>Bạn đã thử bài này?</h3><p>Chia sẻ khó khăn, ý tưởng hay kết quả. Ẩn danh hoặc công khai, tùy bạn.</p>'
                 f'<p><a class="btn primary" href="/chia-se/?bai={key}#gui">Chia sẻ về {code.lower()}</a></p></div>')
        meta = [f'Tuần {w}', 'Phần bố mẹ 30 phút', 'Phần cả nhà 15–20 phút']
        body = f'''<div class="lesson">
<p class="eyebrow no-print"><a href="{U}">{name}</a> · Tuần {w}</p>
<h1>{code}: {title}</h1>
<div class="lesson-meta">{''.join(f'<span>{m}</span>' for m in meta)}</div>
{note}
{PRINT_ROW}
{''.join(sections[:3])}
{figure_block(prefix + k)}
{''.join(sections[3:])}
{share}
<p class="print-only small">daynentang.com · CC BY-NC-SA 4.0 · Cập nhật 28/10/2026</p>
<nav class="lesson-nav no-print" aria-label="Bài trước, bài sau"><a href="{prev[0]}">← {prev[1]}</a><a href="{nxt[0]}">{nxt[1]} →</a></nav>
</div>'''
        page(url(k), f'{code} – {title}', desc, body, current='/gia-dinh/')
    return lesson, link, ORDER

# =====================================================================
# G8 NHÀ GỌN, NHÀ AN TOÀN
# =====================================================================
U8 = '/khoa-hoc/nha-gon-nha-an-toan/'
T8 = '/cong-cu/phieu-ra-soat-nha/'
WHOD = '<a href="https://www.who.int/vietnam/vi/news/feature-stories/item/in-viet-nam--low-cost-water-safety-actions-help-reduce-child-drowning-deaths">WHO Việt Nam (12/2023)</a>'
CPSCW = '<a href="https://www.cpsc.gov/Newsroom/News-Releases/2012/In-Home-Danger-CPSC-Warns-of-Children-Drowning-in-Bathtubs-Bath-Seats-and-Buckets-More-than-400-deaths-estimated-over-a-five-year-period/">CPSC, Hoa Kỳ</a>'
TIP = '<a href="https://www.cpsc.gov/Newsroom/News-Releases/2015/Anchor-It-CPSC-Launches-Nations-Largest-Campaign-to-Prevent-Furniture-and-TV-Tip-Over-Deaths-and-Injuries">CPSC 2015</a>'
PCCC = '<a href="https://luatvietnam.vn/dat-dai/luat-phong-chay-chua-chay-va-cuu-nan-cuu-ho-2024-so-55-2024-qh15-379071-d1.html">Luật Phòng cháy, chữa cháy và cứu nạn, cứu hộ số 55/2024/QH15</a>'
XEDIEN = '<a href="https://lsvn.vn/canh-bao-4-nguyen-nhan-chu-yeu-gay-chay-no-xe-dien-gia-tang-a165609.html">Phòng Cảnh sát PCCC và CNCH, Công an tỉnh Phú Thọ (11/2025)</a>'
FOOD = '<a href="https://www.paho.org/en/news/21-12-2015-pahowho-recommends-five-keys-safer-food-healthy-holiday-season">Năm chìa khóa an toàn thực phẩm của WHO</a>'
BURN = '<a href="https://www.schn.health.nsw.gov.au/kids-health-hub/safety-and-injury-prevention/burns-and-fire/first-aid-burns">Mạng lưới Bệnh viện Nhi Sydney</a>'
L8 = {
 '1': (1, 'ra-soat-an-toan', 'Bài 1', 'Rà soát an toàn từng phòng'),
 '2': (2, 'phong-chay-va-thoat-nan', 'Bài 2', 'Phòng cháy và kế hoạch thoát nạn'),
 '3': (3, 'nha-gon-bua-an-toan', 'Bài 3', 'Nhà gọn và bữa ăn an toàn'),
 '4': (4, 'bao-tri-va-so-cuu', 'Bài 4', 'Lịch bảo trì, tủ thuốc và sơ cứu'),
}
lesson8, link8, ORD8 = make_course(U8, 'Nhà gọn, nhà an toàn', 'N', 'g8', L8, 'N')

lesson8('1', 'Khóa Nhà gọn, nhà an toàn, bài 1: đi một vòng nhà ngang tầm mắt con, tìm và sửa nguy cơ về nước, ngã, bỏng, ngộ độc, đồ đổ.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> rà soát đủ các phòng theo phiếu, sửa ngay ít nhất 5 việc dễ, ghi việc cần mua hoặc cần thợ.', '<strong>Con lớn:</strong> chỉ ra được 3 chỗ nguy hiểm trong nhà và vì sao.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'In <a href="{T8}">Phiếu rà soát nhà</a>.', 'Băng dính, dây buộc, hộp có nắp để cất đồ nhỏ, hóa chất.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Nếu mình cao 1 mét, đi quanh nhà, mình với được những gì?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Ngồi xuống ngang tầm mắt con</strong> ở từng phòng. Nhìn những gì con với, trèo, mở được.',
   '<strong>Nước:</strong> đổ nước xô, chậu ngay sau khi dùng; đậy nắp bể, lu; khóa cửa phòng tắm; người lớn trong tầm tay khi trẻ gần nước.',
   '<strong>Ngã:</strong> chặn cầu thang; khóa cửa sổ, lan can ban công không có chỗ trèo; không kê ghế, tủ sát cửa sổ.',
   '<strong>Bỏng:</strong> quay cán chảo vào trong; ấm, phích nước nóng xa mép bàn; không bế con khi đang cầm đồ nóng.',
   '<strong>Ngộ độc, hóc:</strong> thuốc, hóa chất cất cao hoặc tủ có khóa, giữ chai gốc; đồ nhỏ, pin cúc áo, nam châm cất kín.',
   '<strong>Đồ đổ:</strong> bắt vít tivi, tủ, kệ vào tường; đồ nặng để ngăn dưới; điều khiển, đồ chơi không để trên nóc tủ.'])),
 sec(5, 'Phần cả nhà (15 phút)', ol([
   'Con lớn làm "thám tử an toàn": đi cùng bố mẹ, tìm 3 chỗ nguy hiểm, nói vì sao.',
   'Cả nhà dán nhãn đỏ (giấy màu) lên chỗ con không được tự đến: bếp ga, ổ điện, tủ thuốc.',
   'Con nhỏ: tập "đỏ là dừng" với nhãn đỏ.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Nguy cơ nào nhà mình đã quen đến mức không còn thấy?', 'Ai trông con khi mình nấu ăn?', 'Nhà ông bà, nhà người giúp việc có cần rà soát không?'])),
 sec(7, 'An toàn', ul([SMALL, 'Không để trẻ lớn trông trẻ nhỏ gần nước.', 'Nghi con nuốt pin cúc áo, hóa chất hay thuốc: gọi 115 ngay, mang theo vỏ chai, vỏ thuốc.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: phiếu rà soát, 30 phút chia 2 lần.', [
   ('Lần 1.', 'Bếp và phòng tắm.'), ('Lần 2.', 'Phòng ngủ, phòng khách, ban công.')], [
   ('Việc cần khoan, cần thợ:', 'ghi lại, để bố làm khi về hoặc nhờ thợ. Trong lúc chờ, dời đồ nặng xuống thấp.')])),
 sec(9, 'Ôn lại', ul(['<strong>Sau 1 tuần:</strong> làm xong việc cần mua, cần thợ.', '<strong>Mỗi khi con lớn thêm:</strong> rà soát lại, vì con với cao hơn, mở được nhiều hơn.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Mỗi năm khoảng 2.000 trẻ em Việt Nam tử vong do đuối nước ({WHOD}).'),
   lb('Đã xác nhận', f'Trẻ có thể đuối nước trong xô, chậu, bồn tắm ở nhà; giữ trẻ trong tầm tay, đổ nước sau khi dùng ({CPSCW}).'),
   lb('Đã xác nhận', f'Tại Mỹ, trung bình khoảng 2 tuần có một trẻ tử vong do tivi, đồ đạc đổ; khuyên bắt vít, để đồ nặng ở dưới, không để đồ hấp dẫn trên nóc ({TIP}).'),
   lb('Đánh giá chuyên môn', 'Phiếu rà soát theo phòng do daynentang.com soạn; không thay thế tư vấn của thợ điện, thợ xây.')]))
])

lesson8('2', 'Khóa Nhà gọn, nhà an toàn, bài 2: phòng cháy trong nhà, sạc xe điện an toàn, kế hoạch thoát nạn và tập cùng con.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> có sơ đồ thoát nạn, chỗ hẹn gặp ngoài nhà, và kiểm tra đủ 6 điểm phòng cháy.', '<strong>Cả nhà:</strong> tập thoát nạn một lần; con lớn nói được số 114.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 2 của <a href="{T8}">Phiếu rà soát nhà</a>.', 'Giấy vẽ sơ đồ nhà.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Nếu cháy ở tầng 1 lúc nửa đêm, cả nhà ra bằng đường nào?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Nguồn lửa:</strong> bếp không bỏ đi khi đang nấu; nơi thờ cúng, đốt vàng mã xa đồ dễ cháy; không câu điện, cắm quá nhiều thiết bị một ổ.',
   '<strong>Sạc xe điện, pin:</strong> không sạc qua đêm hay khi không có người; dùng sạc, pin chính hãng; không sạc gần đồ dễ cháy hay ở lối thoát; không tự độ pin, độ máy.',
   '<strong>Thiết bị:</strong> bình chữa cháy ở chỗ dễ lấy, người lớn biết dùng; nếu có thể, lắp thiết bị báo khói.',
   '<strong>Lối thoát:</strong> nhà ống có chuồng cọp, khung sắt: làm cửa mở được từ bên trong, chìa khóa để chỗ cố định.',
   '<strong>Kế hoạch thoát nạn:</strong> vẽ sơ đồ, mỗi phòng hai lối ra nếu có, chỗ hẹn gặp ngoài nhà. Thoát ra trước, gọi 114 sau, không quay lại lấy đồ.'])),
 sec(5, 'Phần cả nhà (20 phút)', ol([
   'Bố mẹ chỉ sơ đồ, đi một vòng hai lối ra cùng con.',
   'Tập: bò thấp dưới khói (giả vờ), sờ cửa trước khi mở, ra chỗ hẹn.',
   'Con lớn học số 114 và câu báo: tên đường, số nhà, cháy gì.',
   'Con nhỏ: tập "nắm tay bố mẹ, đi theo". Không trốn dưới gầm giường.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Chìa khóa cửa, khóa chuồng cọp để ở đâu? Ai cũng biết chưa?', 'Xe điện nhà mình đang sạc ở đâu, lúc nào?', 'Ai bế con nhỏ khi thoát nạn?'])),
 sec(7, 'An toàn', ul(['Tập thoát nạn không dùng lửa thật, không đốt thử.', 'Bật lửa, diêm cất ngoài tầm với của trẻ.', 'Khi có cháy: gọi 114. Có người bị thương: 115.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: sơ đồ, 20 phút tập.', [
   ('Trước khi bố đi.', 'Bố mẹ thống nhất ai bế con nhỏ, ai dắt con lớn; khi bố vắng, mẹ bế con nhỏ, con lớn nắm áo mẹ.'), ('Khi bố vắng.', 'Không sạc xe qua đêm; mẹ kiểm bếp, ổ điện trước khi ngủ.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tối:</strong> rút sạc, tắt bếp, kiểm gas.', '<strong>Hai lần mỗi năm:</strong> tập thoát nạn cả nhà.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{PCCC} (ban hành 29/11/2024, hiệu lực 01/07/2025): chủ hộ có trách nhiệm nhắc các thành viên tuân thủ, thường xuyên tự kiểm tra và khắc phục nguy cơ cháy, nổ. Nhà ở kết hợp kinh doanh có thêm yêu cầu về thiết bị điện, lối thoát nạn, ngăn cách khu kinh doanh. Tra cứu 28/10/2026; không phải tư vấn pháp lý.'),
   lb('Đã xác nhận', f'Khuyến cáo sạc xe điện: không sạc qua đêm, dùng sạc chính hãng, không độ chế, không sạc gần đồ dễ cháy, kiểm tra dây sạc, có bình chữa cháy ({XEDIEN}).'),
   lb('Đánh giá chuyên môn', 'Kế hoạch thoát nạn và cách tập với trẻ là thực hành phổ biến; cách viết do daynentang.com soạn.')]))
])

lesson8('3', 'Khóa Nhà gọn, nhà an toàn, bài 3: gọn nhà theo vòng "bỏ bớt – chọn chỗ – dán nhãn – cất lại", và năm chìa khóa an toàn thực phẩm.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> gọn xong 1 khu (tủ bếp, góc đồ chơi hay tủ quần áo con) và có giờ "cất lại 10 phút" mỗi ngày.', '<strong>Bố mẹ:</strong> áp dụng 5 chìa khóa an toàn thực phẩm; thớt sống và chín để riêng.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul(['3 thùng: Giữ, Cho, Bỏ.', 'Giấy dán nhãn, bút.', f'Trang 3 của <a href="{T8}">Phiếu rà soát nhà</a>.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Đồ nào trong nhà mình tìm mãi không thấy? Góc nào lúc nào cũng bừa?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Bỏ bớt:</strong> chọn một khu nhỏ. Đồ không dùng một năm: cho hoặc bỏ. Đồ hỏng: sửa trong tuần hoặc bỏ.',
   '<strong>Chọn chỗ:</strong> đồ hay dùng ở chỗ dễ lấy; đồ của con ở tầm con với; đồ nguy hiểm ở cao, có khóa.',
   '<strong>Dán nhãn:</strong> chữ cho người lớn, hình cho con nhỏ.',
   '<strong>Năm chìa khóa thực phẩm:</strong> giữ sạch tay, dao, thớt; để riêng đồ sống và chín; nấu kỹ; không để đồ chín ở nhiệt độ phòng quá 2 giờ; dùng nước và nguyên liệu an toàn.',
   '<strong>Thực đơn tuần:</strong> nếu nhà học khóa Tiền nhà mình, dùng thực đơn bài 5A, thêm cột "chuẩn bị trước".'])),
 sec(5, 'Phần cả nhà (15 phút)', ol([
   'Con lớn gọn góc đồ chơi: chọn đồ cho em hoặc cho bạn, dán nhãn hình lên rổ.',
   'Cả nhà "cất lại 10 phút" theo nhạc (như khóa Việc nhà chia đều).',
   'Con lớn rửa tay đúng cách trước bữa ăn; con nhỏ rửa tay cùng người lớn.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Mình giữ đồ vì cần hay vì tiếc?', 'Thức ăn thừa nhà mình để ngoài bao lâu?', 'Ai rửa thớt sau khi thái thịt sống?'])),
 sec(7, 'An toàn', ul([SMALL, 'Túi nilon, dây buộc khi dọn: cất ngay khỏi tầm với của con nhỏ.', 'Đồ cho đi: kiểm tra không có pin, đồ nhỏ vỡ.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 3 thùng, 30 phút cho một khu nhỏ.', [
   ('Khu đầu tiên.', 'Chọn khu nhỏ nhất, xong trong một buổi.'), ('Đồ lớn cần bỏ.', 'Để dành bố về cùng mang đi.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi ngày:</strong> cất lại 10 phút.', '<strong>Mỗi tuần:</strong> gọn thêm 1 khu nhỏ.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{FOOD}: dùng nước và nguyên liệu an toàn; giữ sạch tay, dụng cụ, bề mặt; nấu kỹ; giữ thực phẩm ở nhiệt độ an toàn, không để đồ chín ngoài quá 2 giờ; để riêng đồ sống và chín.'),
   lb('Đánh giá chuyên môn', 'Vòng "bỏ bớt – chọn chỗ – dán nhãn – cất lại" do daynentang.com soạn; chưa có nghiên cứu riêng về hiệu quả.')]))
])

lesson8('4', 'Khóa Nhà gọn, nhà an toàn, bài 4: lịch bảo trì nhà, tủ thuốc gia đình, sơ cứu bỏng và đánh giá cuối khóa.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> có lịch bảo trì dán tủ lạnh; tủ thuốc có khóa, đủ đồ sơ cứu cơ bản.', '<strong>Con lớn:</strong> nói lại 3 bước sơ cứu bỏng và các số 113, 114, 115.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 4 của <a href="{T8}">Phiếu rà soát nhà</a>.', 'Hộp có khóa làm tủ thuốc.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Thiết bị nào trong nhà đã lâu không ai kiểm tra?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Lịch bảo trì:</strong> mỗi tháng thử báo khói, xem bình chữa cháy; mỗi quý kiểm ổ cắm, dây điện, van gas; mỗi năm vệ sinh máy lạnh, bình nóng lạnh; trước mùa mưa xem mái, máng nước.',
   '<strong>Tủ thuốc:</strong> cất cao, có khóa; bỏ thuốc hết hạn; có gạc, băng, nhiệt kế, thuốc theo đơn bác sĩ. Thuốc cho con theo đúng nhãn và lời bác sĩ.',
   '<strong>Sơ cứu bỏng:</strong> làm mát bằng nước mát đang chảy 20 phút; tháo nhẫn, đồ quanh vết bỏng; không bôi đá, kem đánh răng, mỡ; đi khám nếu vết bỏng phồng rộp hay rộng.',
   '<strong>Số khẩn cấp:</strong> 113 công an, 114 cháy, 115 cấp cứu. Dán cạnh điện thoại bàn hoặc trên tủ lạnh.',
   '<strong>Đánh giá cuối khóa:</strong> chấm lại phiếu rà soát, so với tuần 1.'])),
 sec(5, 'Phần cả nhà (15 phút)', ol([
   'Đóng vai: "Em bị bỏng tay". Con lớn dẫn em ra vòi nước, nói "20 phút", gọi bố mẹ.',
   'Con lớn tập gọi giả: "Số 115. Nhà con ở … Em bị …"',
   'Cả nhà dán lịch bảo trì và số khẩn cấp lên tủ lạnh.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Mình có biết khóa van gas tổng ở đâu không?', 'Ai trong nhà biết sơ cứu?', 'Thuốc của ông bà có để trong tầm với của con không?'])),
 sec(7, 'An toàn', ul(['Không tự sửa điện, gas nếu không có chuyên môn; gọi thợ.', 'Thuốc người lớn, thuốc ông bà: cất có khóa như thuốc của con.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: lịch bảo trì, hộp thuốc, 30 phút.', [
   ('Trong buổi.', 'Mẹ sắp tủ thuốc, viết lịch bảo trì. Việc cần thợ, ghi lại.'), ('Với con.', 'Đóng vai sơ cứu bỏng, gọi số khẩn cấp.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> theo lịch bảo trì.', '<strong>Mỗi năm:</strong> rà soát lại cả nhà theo phiếu.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Sơ cứu bỏng: làm mát bằng nước mát đang chảy 20 phút, tháo quần áo, trang sức gần vết bỏng; không bôi đá, kem, gel, kem đánh răng, bơ ({BURN}).'),
   lb('Đánh giá chuyên môn', 'Lịch bảo trì là ví dụ; mỗi nhà điều chỉnh theo thiết bị và hướng dẫn của nhà sản xuất.'),
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước – sau 4 tuần; đây không phải bằng chứng hiệu quả.')]))
])

def course_page(U, title, eyebrow, lead, table_rows, giup, xay, figcode, tool_line, evidence, limit, extra_safe, link, ORDER, L, goals, desc):
    rows = ''.join(f'<tr><td>{L[k][0]}</td><td><a href="{link(k)[0]}">{L[k][3]}</a></td><td>{g}</td></tr>' for k, g in zip(ORDER, goals))
    page(U, title, desc, f'''
<p class="eyebrow">{eyebrow}</p>
<h1>{title}</h1>
<p class="lead">{lead}</p>
<div class="table-wrap"><table><tbody>{table_rows}</tbody></table></div>
<div class="two">
  <div class="card"><h3>Giúp ngay (1–2 tuần)</h3>{ul(giup)}</div>
  <div class="card"><h3>Xây lâu dài</h3>{ul(xay)}</div>
</div>
<h2>Bốn tuần</h2>
{figure_block(figcode)}
<div class="table-wrap"><table>
<thead><tr><th>Tuần</th><th>Bài</th><th>Mục tiêu đo được</th></tr></thead>
<tbody>{rows}</tbody></table></div>
<h2>Công cụ</h2>
<ul><li>{tool_line}</li></ul>
<h2>Căn cứ phương pháp</h2>
<div class="table-wrap"><table>
<thead><tr><th>Nguồn</th><th>Chúng tôi dùng gì</th><th>Bằng chứng</th></tr></thead>
<tbody>{evidence}</tbody></table></div>
<div class="box warn"><h3>Giới hạn, nói thật</h3><p><span class="label">[Suy luận]</span> {limit}</p></div>
<h2>Chia sẻ khi thực hành</h2>
<p>Gặp khó khăn hay nghĩ ra cách hay? <a href="/chia-se/?bai=chung#gui">Chia sẻ</a> ẩn danh hoặc công khai.</p>
<h2>An toàn cho mọi buổi</h2>
{ul(extra_safe)}
{HELP_BOX}
''', current='/gia-dinh/')

def ev(src, what, proof): return f'<tr><td>{src}</td><td>{what}</td><td><span class="label">[Đã xác nhận]</span> {proof}</td></tr>'
INFO = lambda purpose, who, dur, need: (f'<tr><th>Mục đích</th><td>{purpose}</td></tr><tr><th>Dành cho</th><td>{who}</td></tr>'
                                        f'<tr><th>Thời lượng</th><td>{dur}</td></tr><tr><th>Cần có</th><td>{need}</td></tr>'
                                        '<tr><th>Tình trạng</th><td>Đủ 4 tuần, bản chưa dạy thử, sẽ sửa theo nhật ký dạy thật</td></tr>')

course_page(U8, 'Nhà gọn, nhà an toàn', 'Gia đình · Khóa G8 · Đang thử nghiệm',
 'Một ngôi nhà an toàn cho trẻ nhỏ, có kế hoạch khi cháy, gọn để dễ sống, bữa ăn sạch, và lịch bảo trì để ít sự cố.',
 INFO('Giảm nguy cơ tai nạn trong nhà; cả nhà biết làm gì khi có sự cố', 'Bố mẹ, ông bà, người chăm trẻ; bài cả nhà có phần cho con lớn và con nhỏ',
      '4 tuần. Mỗi tuần phần bố mẹ 30 phút và phần cả nhà 15–20 phút', 'Phiếu rà soát in, băng dính, hộp có khóa, giấy màu'),
 ['Sửa ngay 5 nguy cơ dễ sửa trong nhà.', 'Có sơ đồ thoát nạn và chỗ hẹn gặp.', 'Không sạc xe điện qua đêm.'],
 ['Thói quen rà soát khi con lớn thêm.', 'Kỹ năng sơ cứu bỏng, gọi số khẩn cấp.', 'Lịch bảo trì và nếp cất lại mỗi ngày.'],
 'KHOAN', f'<a href="{T8}">Phiếu rà soát nhà</a>: rà soát từng phòng, 6 điểm phòng cháy, sơ đồ thoát nạn, gọn nhà, lịch bảo trì, tủ thuốc.',
 ev(WHOD, 'Mức độ nghiêm trọng của đuối nước ở trẻ', 'Khoảng 2.000 trẻ tử vong mỗi năm ở Việt Nam')
 + ev(f'{CPSCW}; {TIP}', 'Nước trong nhà; bắt vít đồ đạc, tivi', 'Cơ quan an toàn sản phẩm Hoa Kỳ')
 + ev(f'{PCCC}; {XEDIEN}', 'Trách nhiệm chủ hộ; sạc xe điện', 'Luật Việt Nam (hiệu lực 01/07/2025); khuyến cáo Cảnh sát PCCC')
 + ev(f'{FOOD}; {BURN}', 'An toàn thực phẩm; sơ cứu bỏng', 'Hướng dẫn WHO; hướng dẫn bệnh viện nhi'),
 'Khóa ghép từ hướng dẫn an toàn của cơ quan chuyên môn, không phải chương trình đã thử nghiệm. Khóa không thay thế kiểm tra của thợ điện, cảnh sát PCCC hay bác sĩ.',
 [SMALL, 'Trẻ gần nước: người lớn luôn trong tầm tay.', 'Khẩn cấp: 113 công an · 114 cháy · 115 cấp cứu.'], link8, ORD8, L8,
 ['Rà soát đủ phòng; sửa ≥5 việc dễ', 'Sơ đồ thoát nạn; tập 1 lần; không sạc qua đêm', 'Gọn 1 khu; thớt sống – chín riêng', 'Lịch bảo trì, tủ thuốc có khóa; chấm phiếu cuối'],
 'Khóa 4 tuần miễn phí: rà soát an toàn nhà cho trẻ, phòng cháy và sạc xe điện, nhà gọn, an toàn thực phẩm, lịch bảo trì, sơ cứu bỏng.')

ROOMS = [('Bếp', ['Cán chảo quay vào trong', 'Ấm, phích nóng xa mép bàn', 'Dao, kéo cất cao', 'Hóa chất tẩy rửa có khóa', 'Bật lửa, diêm cất cao']),
         ('Phòng tắm', ['Không để nước trong xô, chậu', 'Bể, lu có nắp', 'Thảm chống trơn', 'Dao cạo, thuốc cất cao']),
         ('Phòng ngủ, phòng khách', ['Tivi, tủ, kệ bắt vít vào tường', 'Ổ điện có nắp che', 'Dây rèm, dây điện ngoài tầm với', 'Đồ nhỏ, pin cúc áo cất kín']),
         ('Cầu thang, ban công, cửa sổ', ['Chặn cầu thang', 'Cửa sổ có khóa', 'Không kê ghế, tủ sát lan can', 'Lan can không có chỗ trèo'])]
rr = ''.join(f'<tr><th colspan="3">{r}</th></tr>' + ''.join(f'<tr><td>{x}</td><td></td><td></td></tr>' for x in items) for r, items in ROOMS)
FIRE = ['Không bỏ bếp khi đang nấu', 'Không cắm quá nhiều thiết bị một ổ', 'Không sạc xe điện qua đêm, gần đồ dễ cháy', 'Có bình chữa cháy, người lớn biết dùng', 'Cửa, khóa chuồng cọp mở được từ bên trong', 'Có sơ đồ thoát nạn, chỗ hẹn gặp']
fr = ''.join(f'<tr><td>{x}</td><td></td><td></td></tr>' for x in FIRE)
page(T8, 'Phiếu rà soát nhà', 'Phiếu in cho khóa Nhà gọn, nhà an toàn: rà soát từng phòng, phòng cháy, thoát nạn, gọn nhà, lịch bảo trì, tủ thuốc.',
f'''
<h1>Phiếu rà soát nhà</h1>
<p>Dùng cho khóa <a href="{U8}">Nhà gọn, nhà an toàn</a>. Đánh dấu ✓ khi đạt. Chấm ở tuần 1 và tuần 4.</p>
{PRINT_ROW}
<h2>1. Rà soát từng phòng (tuần 1)</h2>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 4</th></tr></thead><tbody>{rr}</tbody></table></div>
<h2>2. Phòng cháy (tuần 2)</h2>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 4</th></tr></thead><tbody>{fr}</tbody></table></div>
<p><strong>Sơ đồ thoát nạn:</strong> vẽ ở mặt sau tờ giấy. Chỗ hẹn gặp ngoài nhà: ……………………… Chìa khóa cửa để ở: ………………</p>
<h2>3. Gọn nhà (tuần 3)</h2>
<p>Khu gọn tuần này: ……………… · Giờ cất lại 10 phút: ……… · Thớt sống: màu ……… · Thớt chín: màu ………</p>
<h2>4. Lịch bảo trì và tủ thuốc (tuần 4)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Mỗi tháng</th><td>Thử báo khói · Xem bình chữa cháy</td></tr>
<tr><th>Mỗi quý</th><td>Ổ cắm, dây điện · Van, dây gas</td></tr>
<tr><th>Mỗi năm</th><td>Máy lạnh · Bình nóng lạnh · Thuốc hết hạn</td></tr>
<tr><th>Trước mùa mưa</th><td>Mái, máng nước · Đồ cần kê cao</td></tr>
<tr><th>Tủ thuốc</th><td>Có khóa · Gạc, băng · Nhiệt kế · Thuốc theo đơn</td></tr>
</tbody></table></div>
<p><strong>Số khẩn cấp:</strong> 113 công an · 114 cháy · 115 cấp cứu · 111 bảo vệ trẻ em</p>
<p class="small muted">Phiếu không thay thế kiểm tra của thợ điện, thợ gas hay cảnh sát PCCC.</p>
''', current='/cong-cu/')

# =====================================================================
# G9 GIA ĐÌNH VÀ CỘNG ĐỒNG
# =====================================================================
U9 = '/khoa-hoc/gia-dinh-va-cong-dong/'
T9 = '/cong-cu/so-tay-cong-dong/'
HL = '<a href="https://www.rti.org/publication/social-relationships-mortality-risk-meta-analytic-review">Holt-Lunstad et al. 2010, <em>PLoS Medicine</em></a>'
FIV = '<a href="https://www.medicalnewstoday.com/releases/31955">Fivush &amp; Duke, Đại học Emory</a>'
MEDIA = '<a href="https://healthychildren.org/English/family-life/Media/Pages/How-to-Make-a-Family-Media-Use-Plan.aspx">AAP – kế hoạch màn hình gia đình (cập nhật 1/2026)</a>'
WHO5 = '<a href="https://new.chconline.org/new-who-guidelines-on-physical-activity-sedentary-behaviour-and-sleep-for-children-under-5-years-of-age">WHO 2019</a>'
MCC = '<a href="https://mcc.gse.harvard.edu/reports/children-mean-raise">Making Caring Common, Harvard</a>'
WT = '<a href="https://scholars.duke.edu/publication/1458228">Warneken &amp; Tomasello 2008</a>'
L9 = {
 '1': (1, 'ong-ba-va-chuyen-gia-dinh', 'Bài 1', 'Ông bà và chuyện gia đình'),
 '2': (2, 'ho-hang-hang-xom', 'Bài 2', 'Họ hàng, hàng xóm: mạng lưới giúp nhau'),
 '3': (3, 'ke-hoach-man-hinh-gia-dinh', 'Bài 3', 'Kế hoạch màn hình gia đình'),
 '4': (4, 'giup-cong-dong', 'Bài 4', 'Cả nhà giúp cộng đồng'),
}
lesson9, link9, ORD9 = make_course(U9, 'Gia đình và cộng đồng', 'Q', 'g9', L9, 'Q')

lesson9('1', 'Khóa Gia đình và cộng đồng, bài 1: con phỏng vấn ông bà về chuyện gia đình; bố mẹ và ông bà thống nhất vài điều khi chăm cháu.', [
 sec(1, 'Mục tiêu', ul(['<strong>Con lớn:</strong> phỏng vấn ông hoặc bà 3 câu, kể lại 1 chuyện cho cả nhà.', '<strong>Bố mẹ:</strong> thống nhất với ông bà 3 điều khi chăm cháu, và cảm ơn ông bà cụ thể.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 1 của <a href="{T9}">Sổ tay cộng đồng</a>.', 'Hẹn ông bà một buổi, hoặc gọi video nếu ở xa.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Con mình biết gì về tuổi thơ của ông bà? Về lúc khó khăn của gia đình?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Chuyện gia đình:</strong> con biết chuyện ông bà, bố mẹ đã vượt khó thế nào giúp con thấy mình thuộc về một gia đình có gốc.',
   '<strong>Chuyện thật, cả vui và buồn:</strong> kể cả lúc khó và cách gia đình đứng dậy, không chỉ chuyện thành công.',
   '<strong>Thống nhất với ông bà:</strong> chọn 3 điều quan trọng nhất (giờ ngủ, đồ ngọt, không đánh). Hỏi ý ông bà trước, lắng nghe kinh nghiệm của ông bà.',
   '<strong>Cảm ơn cụ thể:</strong> "Con cảm ơn mẹ tuần này đón cháu 3 buổi, con làm thêm được việc."'])),
 sec(5, 'Phần cả nhà (20 phút)', ol([
   'Con lớn hỏi ông bà 3 câu: "Hồi nhỏ ông chơi gì?", "Ông bà gặp nhau thế nào?", "Lúc khó nhất, ông bà làm gì?"',
   'Con vẽ hoặc ghi lại một chuyện. Tối kể lại cho cả nhà.',
   'Con nhỏ: xem ảnh cũ cùng ông bà, gọi tên người trong ảnh.',
   'Vẽ cây gia đình đơn giản: ông bà nội, ngoại, bố mẹ, các con.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Điều gì ông bà làm khác mình mà thật ra không sao?', 'Điều gì mình cần ông bà giữ giống bố mẹ?', 'Lần cuối mình cảm ơn ông bà là khi nào?'])),
 sec(7, 'An toàn', ul(['Ảnh, tên, chuyện gia đình chỉ giữ trong nhà, không đăng mạng công khai.', 'Ông bà trông cháu: rà soát an toàn nhà ông bà như khóa Nhà gọn, nhà an toàn (thuốc của ông bà cất có khóa).'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: 20 phút gọi video với ông bà.', [
   ('Gọi video.', 'Con phỏng vấn ông bà qua điện thoại, mẹ giúp ghi.'), ('Ông bà bên nội.', 'Bố gọi video phần thống nhất 3 điều với ông bà bên nội.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> con hỏi ông bà 1 câu mới.', '<strong>Dịp lễ, Tết:</strong> cả nhà kể lại chuyện gia đình.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Nghiên cứu 40 gia đình có con 9–12 tuổi: trẻ biết nhiều về chuyện gia đình có lòng tự trọng cao hơn, quan hệ bạn bè tốt hơn. Đây là liên hệ, mẫu nhỏ ({FIV}).'),
   lb('Đánh giá chuyên môn', 'Câu hỏi phỏng vấn và cây gia đình do daynentang.com soạn.')]))
])

lesson9('2', 'Khóa Gia đình và cộng đồng, bài 2: lập danh sách người có thể nhờ, và giữ quan hệ cho – nhận với họ hàng, hàng xóm.', [
 sec(1, 'Mục tiêu', ul(['<strong>Bố mẹ:</strong> có danh sách ít nhất 5 người có thể nhờ, mỗi người cho một việc cụ thể.', '<strong>Cả nhà:</strong> làm 1 việc tốt nhỏ cho một hàng xóm trong tuần.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 2 của <a href="{T9}">Sổ tay cộng đồng</a>.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Nếu tối nay con sốt cao mà mình kẹt ở chỗ làm, ai có thể giúp?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Vì sao cần mạng lưới:</strong> người có quan hệ xã hội tốt sống khỏe hơn, theo phân tích gộp lớn. Gia đình có con nhỏ càng cần người đỡ lúc khó.',
   '<strong>Danh sách:</strong> việc cần giúp (đón con, trông con, chở đi viện, sửa điện, hỏi chuyện học) và người có thể nhờ.',
   '<strong>Cho trước:</strong> hỏi thăm, giúp việc nhỏ, mang đồ ăn khi nhà ai có chuyện. Quan hệ bền nhờ cho và nhận qua lại.',
   '<strong>Người đón con:</strong> thống nhất với trường, nhà trẻ danh sách người được đón con; dạy con chỉ đi với người trong danh sách.'])),
 sec(5, 'Phần cả nhà (15 phút)', ol([
   'Cả nhà chọn một hàng xóm để làm việc tốt: tặng ít trái cây, giúp mang đồ, hỏi thăm người già.',
   'Con lớn vẽ thiệp cảm ơn cho một người đã giúp nhà mình.',
   'Con lớn học thuộc số điện thoại của bố mẹ và tên 1 người lớn tin cậy gần nhà.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Mình ngại nhờ người khác vì sao?', 'Ai đang cần mình giúp mà mình chưa để ý?', 'Con có biết nhà ai gần nhất để chạy sang khi cần không?'])),
 sec(7, 'An toàn', ul(['Dạy con: chỉ đi với người trong danh sách đón; người lạ nói "bố mẹ nhờ đón" thì không đi, báo cô giáo.', 'Không để con một mình nhà người khác khi chưa quen biết kỹ.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: danh sách, 20 phút.', [
   ('Trước chuyến đi của bố.', 'Mẹ và bố cùng chọn 2 người có thể đỡ mẹ khi bố vắng; báo trước cho họ.')], [
   ('Mẹ ngại nhờ:', 'nhờ việc nhỏ, cụ thể, có giờ: "Chiều thứ Tư chị đón cháu giúp em được không?"')])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> một việc tốt cho hàng xóm.', '<strong>Mỗi năm học:</strong> cập nhật danh sách người đón con.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'Phân tích gộp 148 nghiên cứu, 308.849 người: người có quan hệ xã hội mạnh hơn có khả năng sống sót cao hơn (tỉ số chênh 1,50), tương đương các yếu tố nguy cơ đã biết ({HL}). Đây là nghiên cứu quan sát.'),
   lb('Đánh giá chuyên môn', 'Danh sách người có thể nhờ và quy tắc người đón con do daynentang.com soạn.')]))
])

lesson9('3', 'Khóa Gia đình và cộng đồng, bài 3: cả nhà làm kế hoạch màn hình gia đình theo tuổi từng con, bố mẹ làm gương.', [
 sec(1, 'Mục tiêu', ul(['<strong>Cả nhà:</strong> có kế hoạch màn hình 4 phần, ghi riêng cho từng tuổi, áp dụng cả bố mẹ.', '<strong>Bố mẹ:</strong> bữa ăn không điện thoại ít nhất 6/7 ngày.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 3 của <a href="{T9}">Sổ tay cộng đồng</a>.', 'Xem thời gian dùng màn hình hôm qua của mỗi người.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Con thấy mình cầm điện thoại bao nhiêu lần mỗi tối?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Theo tuổi:</strong> dưới 2 tuổi không xem màn hình (gọi video với người thân được); 2–4 tuổi tối đa 1 giờ mỗi ngày, ít hơn càng tốt.',
   '<strong>Từ 5 tuổi:</strong> theo kế hoạch gia đình; ngủ, vận động, bài tập, việc nhà làm trước.',
   '<strong>Bốn phần của kế hoạch:</strong> chỗ và giờ không màn hình (bàn ăn, trước ngủ); chọn nội dung tốt; tắt tự phát và thông báo; bố mẹ làm gương.',
   '<strong>Xem cùng con:</strong> khi con xem, ngồi cùng, hỏi về nội dung, nối với đời thật.',
   '<strong>Xem lại:</strong> mỗi đầu năm học hoặc dịp nghỉ dài.'])),
 sec(5, 'Phần cả nhà (20 phút)', ol([
   'Mỗi người nói thời gian dùng màn hình hôm qua. Bố mẹ nói trước.',
   'Cả nhà chọn chỗ và giờ không màn hình. Con lớn đề xuất một giờ cho bố mẹ.',
   'Liệt kê 5 việc vui không cần màn hình: đá bóng, xếp Lego, đọc truyện, vẽ, đi dạo.',
   'Con nhỏ: chọn "hộp chơi" không màn hình để dùng khi bố mẹ nấu cơm.'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Mình dùng màn hình để con ngồi yên lúc nào? Có cách khác không?', 'Ông bà, người giúp việc có theo kế hoạch không?', 'Thông báo nào trên máy mình nên tắt?'])),
 sec(7, 'An toàn', ul(['Con nhỏ không dùng máy một mình; nội dung trẻ em vẫn có quảng cáo, nội dung không hợp.', 'Không đăng ảnh, tên, trường của con lên mạng công khai.'])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: trang kế hoạch, 20 phút.', [
   ('Trong buổi.', 'Mẹ và con lớn viết kế hoạch; bố đồng ý qua video.'), ('Khi bố gọi video.', 'Bố cũng giữ giờ gọi cố định, không gọi vào giờ ăn, giờ ngủ của con.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tuần:</strong> nhắc kế hoạch trong buổi họp gia đình.', '<strong>Đầu năm học:</strong> xem lại kế hoạch.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{MEDIA}: chỗ không màn hình (bàn ăn, khi làm bài, trước ngủ), chọn nội dung chất lượng, tắt tự phát và thông báo, bố mẹ làm gương, áp dụng cho mọi người, xem lại đầu năm học.'),
   lb('Đã xác nhận', f'{WHO5}: không khuyến nghị màn hình cho trẻ dưới 2 tuổi; trẻ 2–4 tuổi tối đa 1 giờ mỗi ngày.'),
   lb('Đánh giá chuyên môn', 'Gọi video với người thân là ngoại lệ do daynentang.com chọn; chúng tôi chưa đọc nguồn gốc cho ngoại lệ này.')]))
])

lesson9('4', 'Khóa Gia đình và cộng đồng, bài 4: cả nhà chọn và làm một việc tốt cho cộng đồng, kể lại, và đánh giá cuối khóa.', [
 sec(1, 'Mục tiêu', ul(['<strong>Cả nhà:</strong> làm 1 việc tốt cho cộng đồng trong tháng, do con chọn.', '<strong>Bố mẹ:</strong> chấm phiếu tự đánh giá cuối khóa.'])),
 sec(2, 'Chuẩn bị (5 phút)', ul([f'Trang 4 của <a href="{T9}">Sổ tay cộng đồng</a>.', 'Tìm hiểu một hoạt động ở xóm, trường, nhà văn hóa.'])),
 sec(3, 'Mở đầu', '<p><strong>Bố mẹ tự hỏi:</strong> <em>"Con mình đã bao giờ thấy bố mẹ giúp người ngoài gia đình chưa?"</em></p>'),
 sec(4, 'Phần bố mẹ (30 phút)', ol([
   '<strong>Con học bằng cách làm:</strong> lòng tốt là kỹ năng, cần thực hành đều.',
   '<strong>Không thưởng vật chất:</strong> khen bằng lời, nói về niềm vui của người được giúp. Thưởng đồ có thể làm trẻ nhỏ giúp ít hơn về sau.',
   '<strong>Chọn việc hợp tuổi:</strong> nhặt rác ở xóm, tặng sách cũ, thăm người già neo đơn, góp quỹ lớp.',
   '<strong>Đánh giá cuối khóa:</strong> chấm phiếu, so với tuần 1.'])),
 sec(5, 'Phần cả nhà (20 phút + thời gian làm việc tốt)', ol([
   'Bố mẹ đưa 3–4 lựa chọn; con lớn chọn một việc.',
   'Cả nhà lên kế hoạch: ngày nào, mang gì, ai làm gì.',
   'Làm việc tốt cùng nhau. Con nhỏ làm phần nhỏ, an toàn.',
   'Tối đó kể lại: "Hôm nay mình đã giúp ai? Người đó thấy thế nào? Mình thấy thế nào?"'])),
 sec(6, 'Câu hỏi bố mẹ tự hỏi', ol(['Việc tốt nào có thể làm đều mỗi tháng?', 'Con có ý tưởng giúp ai mà mình chưa nghĩ ra?', 'Phần nào của khóa mình muốn giữ lâu dài?'])),
 sec(7, 'An toàn', ul(['Nhặt rác: đeo găng, không nhặt kim tiêm, mảnh vỡ; người lớn kiểm tra trước.', 'Góp tiền qua tổ chức quen biết, không qua lời kêu gọi lạ trên mạng.', SMALL])),
 sec(8, 'Khi chỉ một người làm (bố đi vắng)', mom('Mẹ chỉ cần: chọn một việc gần nhà, nhỏ.', [
   ('Trong tuần.', 'Mẹ và con làm việc tốt gần nhà, chụp ảnh tay hoặc đồ vật (không chụp mặt người được giúp).'), ('Khi bố gọi.', 'Con kể lại cho bố.')], [])),
 sec(9, 'Ôn lại', ul(['<strong>Mỗi tháng:</strong> một việc tốt cả nhà.', '<strong>Sau 3 tháng:</strong> chấm lại phiếu tự đánh giá.'])),
 sec(10, 'Nhật ký', JOURNAL),
 sec(11, 'Nguồn và nhãn', ul([
   lb('Đã xác nhận', f'{MCC} khuyên cho trẻ cơ hội thường xuyên để thực hành quan tâm người khác.'),
   lb('Đã xác nhận', f'Thí nghiệm với trẻ 20 tháng: trẻ được thưởng vật chất khi giúp thì về sau giúp ít hơn ({WT}).'),
   lb('Đánh giá chuyên môn', 'Một gia đình tự so sánh trước – sau 4 tuần; đây không phải bằng chứng hiệu quả.')]))
])

course_page(U9, 'Gia đình và cộng đồng', 'Gia đình · Khóa G9 · Đang thử nghiệm',
 'Con lớn lên trong nhiều vòng tròn: ông bà, họ hàng, hàng xóm, cộng đồng. Khóa giúp gia đình giữ gốc, có người giúp nhau, dùng màn hình có kế hoạch, và cùng làm việc tốt.',
 INFO('Gia đình gắn với ông bà và cộng đồng; con biết chuyện nhà và biết giúp người', 'Bố mẹ có con mọi tuổi; bài cả nhà có phần cho con lớn và con nhỏ',
      '4 tuần. Mỗi tuần phần bố mẹ 30 phút và phần cả nhà 15–20 phút', 'Giấy, bút, ảnh cũ của gia đình'),
 ['Con hỏi chuyện ông bà và kể lại.', 'Có danh sách người có thể nhờ khi khẩn cấp.', 'Bữa ăn không điện thoại.'],
 ['Con biết gốc gia đình và chuyện vượt khó.', 'Thói quen cho và nhận với hàng xóm, họ hàng.', 'Kế hoạch màn hình xem lại mỗi năm; việc tốt hằng tháng.'],
 'KHOAQ', f'<a href="{T9}">Sổ tay cộng đồng</a>: câu hỏi phỏng vấn ông bà, cây gia đình, danh sách người có thể nhờ, kế hoạch màn hình, việc tốt, phiếu tự đánh giá.',
 ev(FIV, 'Kể chuyện gia đình cho con', 'Nghiên cứu 40 gia đình; liên hệ')
 + ev(HL, 'Vì sao quan hệ xã hội quan trọng', 'Phân tích gộp 148 nghiên cứu; quan sát')
 + ev(f'{MEDIA}; {WHO5}', 'Kế hoạch màn hình; giới hạn theo tuổi', 'Hướng dẫn AAP; khuyến nghị WHO')
 + ev(f'{MCC}; {WT}', 'Thực hành lòng tốt, không thưởng vật chất', 'Khuyến nghị chuyên gia; thí nghiệm với trẻ nhỏ'),
 'Các nghiên cứu về chuyện gia đình và quan hệ xã hội là liên hệ, không chứng minh khóa này làm thay đổi kết quả. Khóa chưa được thử.',
 ['Không đăng ảnh, tên, trường của con khi chia sẻ chuyện gia đình hay việc tốt.', 'Con chỉ đi với người trong danh sách đón.', SMALL], link9, ORD9, L9,
 ['Con phỏng vấn ông bà 3 câu; thống nhất 3 điều', 'Danh sách ≥5 người có thể nhờ; 1 việc tốt cho hàng xóm', 'Kế hoạch màn hình 4 phần; bữa ăn không máy 6/7 ngày', '1 việc tốt cho cộng đồng; chấm phiếu cuối'],
 'Khóa 4 tuần miễn phí: ông bà và chuyện gia đình, mạng lưới giúp nhau với họ hàng, hàng xóm, kế hoạch màn hình gia đình, cả nhà giúp cộng đồng.')

SELF9 = ['Con biết ít nhất 1 chuyện về ông bà', 'Bố mẹ và ông bà thống nhất điều quan trọng khi chăm cháu', 'Cảm ơn ông bà cụ thể', 'Có danh sách người có thể nhờ',
         'Có danh sách người được đón con', 'Hỏi thăm, giúp hàng xóm', 'Có kế hoạch màn hình, cả bố mẹ theo', 'Bữa ăn không điện thoại', 'Cả nhà làm việc tốt cho cộng đồng']
s9 = ''.join(f'<tr><td>{x}</td><td></td><td></td></tr>' for x in SELF9)
need = ''.join(f'<tr><td>{x}</td><td class="tall"></td><td></td></tr>' for x in ['Đón con khi kẹt', 'Trông con một buổi', 'Chở đi viện ban đêm', 'Sửa điện, nước', 'Hỏi chuyện học', '……………'])
page(T9, 'Sổ tay cộng đồng', 'Trang in cho khóa Gia đình và cộng đồng: phỏng vấn ông bà, cây gia đình, người có thể nhờ, kế hoạch màn hình, việc tốt, phiếu tự đánh giá.',
f'''
<h1>Sổ tay cộng đồng</h1>
<p>Dùng cho khóa <a href="{U9}">Gia đình và cộng đồng</a>. Chỉ để in, trang không lưu dữ liệu của bạn. Giữ trong nhà, không đăng mạng.</p>
{PRINT_ROW}
<h2>1. Con phỏng vấn ông bà (tuần 1)</h2>
<ol><li>Hồi nhỏ ông / bà chơi gì? ……………………………………</li><li>Ông bà gặp nhau thế nào? ……………………………………</li>
<li>Lúc khó nhất, ông bà đã làm gì? ……………………………………</li><li>Câu hỏi con tự nghĩ: ……………………………………</li></ol>
<p><strong>Ba điều bố mẹ và ông bà thống nhất:</strong> 1. ……………… 2. ……………… 3. ………………</p>
<p><strong>Cây gia đình:</strong> vẽ ở mặt sau: ông bà nội, ông bà ngoại, bố mẹ, các con.</p>
<h2>2. Người có thể nhờ (tuần 2)</h2>
<div class="table-wrap"><table><thead><tr><th>Việc</th><th>Người có thể nhờ</th><th>Số điện thoại</th></tr></thead><tbody>{need}</tbody></table></div>
<p><strong>Người được đón con:</strong> …………………… · …………………… · ……………………</p>
<h2>3. Kế hoạch màn hình gia đình (tuần 3)</h2>
<div class="table-wrap"><table><tbody>
<tr><th class="w38">Chỗ, giờ không màn hình</th><td>Bàn ăn · Trước ngủ … giờ · ……………</td></tr>
<tr><th>Con dưới 2 tuổi</th><td>Không màn hình; gọi video với người thân được</td></tr>
<tr><th>Con 2–4 tuổi</th><td>Tối đa ……… phút mỗi ngày (≤ 1 giờ), có người lớn cùng xem</td></tr>
<tr><th>Con từ 5 tuổi</th><td>Ngày học: ……… · Cuối tuần: ……… · Sau khi: ngủ đủ, vận động, bài tập, việc nhà</td></tr>
<tr><th>Bố mẹ hứa</th><td></td></tr><tr><th>Năm việc vui không màn hình</th><td></td></tr>
</tbody></table></div>
<h2>4. Việc tốt cho cộng đồng (tuần 4)</h2>
<p>Việc con chọn: ……………………… · Ngày: ……… · Mang gì: ……………… · Ai làm gì: ………………</p>
<p>Sau khi làm: Mình đã giúp ai? Người đó thấy thế nào? Mình thấy thế nào? ……………………………</p>
<h2>5. Phiếu tự đánh giá (tuần 1 và tuần 4)</h2>
<p>0 = chưa có · 1 = có nhưng chưa đều · 2 = đều đặn.</p>
<div class="table-wrap"><table><thead><tr><th>Mục</th><th>Tuần 1</th><th>Tuần 4</th></tr></thead><tbody>{s9}</tbody></table></div>
''', current='/cong-cu/')
print('G8 + G9 built')
