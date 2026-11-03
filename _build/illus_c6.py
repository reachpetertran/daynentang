# Hình minh họa và sơ đồ khóa C6 "Tự tin – an toàn" – tiền tố S / KHOAS
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười bài', 14)
items = [('1. Tự tin luyện được', SAND), ('2. Nói rõ ranh giới', PINK), ('3. Thoát ra, kêu cứu', YELLOW), ('4. Khi bị quấy rối', LBLUE),
         ('5. Đi lại an toàn', G), ('6. An toàn trên mạng', PURP), ('7. Quan hệ lành mạnh', PEACH), ('8. Bẫy việc làm', LGRAY),
         ('9. Tiền của mình', SAND), ('10. Kế hoạch an toàn', PINK)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 30 + (i // 2) * 33
    s += box(x, y, 142, 27, lab, c, 10.5)
add('KHOAS', 1, 'Mười bài', 'Mỗi bài 25 phút: đọc, làm ngay, rồi nói với người tin cậy hoặc tự viết.', s)

add('KHOAS', 2, 'Nhận ra – Nói rõ – Rời đi – Kêu cứu', 'Bốn bước dùng trong cả khóa. Phần lớn tình huống dừng ở bước nói rõ hoặc rời đi.',
    t(160, 28, 'Bốn bước an toàn', 14)
    + flow([['Nhận ra', 'dấu hiệu'], ['Nói rõ', '"Dừng lại"'], ['Rời đi', 'tới chỗ đông'], ['Kêu cứu,', 'báo người']], 56, 70, 8, 312, 10, 10.5, [YELLOW, PINK, LBLUE, G])
    + t(160, 160, 'Mục tiêu là thoát ra an toàn, không phải thắng', 10.5, GREEN))

# ================= BÀI 1 =================
s = t(160, 22, 'Tự tin là kỹ năng', 14)
for i, (lab, c) in enumerate([(['Bậc 1', 'tập một mình'], PINK), (['Bậc 2', 'tập với', 'người tin cậy'], YELLOW), (['Bậc 3', 'làm ở', 'ngoài đời'], G)]):
    s += box(14 + i * 102, 124 - i * 40, 88, 48, lab, c, 10.5)
    if i < 2:
        s += arrow(14 + i * 102 + 90, 140 - i * 40, 14 + (i + 1) * 102 - 2, 110 - i * 40, ORANGE, 3)
s += t(160, 190, 'Mỗi lần làm được, bạn thêm một bằng chứng', 10.5, GREEN)
add('S1', 1, 'Tự tin là kỹ năng', 'Tự tin lớn dần qua từng lần làm được, từ tập một mình tới làm ở ngoài đời.', s)

s = t(160, 22, 'Tư thế và giọng nói', 14)
s += box(14, 40, 140, 112, ['Đứng vững', 'hai chân rộng', 'bằng vai', '', 'Nhìn thẳng'], LBLUE, 10.5)
s += box(166, 40, 140, 112, ['Nói chậm,', 'rõ, đủ to', '', 'Câu ngắn,', 'không xin lỗi thừa'], YELLOW, 10.5)
s += t(160, 182, 'Tập trước gương 1 phút mỗi ngày', 10.5, GREEN)
add('S1', 2, 'Tư thế và giọng nói', 'Hai thứ tập được ngay: đứng vững, nhìn thẳng; nói chậm, rõ, câu ngắn.', s)

# ================= BÀI 2 =================
s = t(160, 22, 'Ba cách đáp lời', 14)
for i, (lab, c) in enumerate([(['Im lặng,', 'chịu đựng'], LGRAY), (['Quả quyết:', 'rõ, bình tĩnh,', 'tôn trọng'], G), (['Gây gổ,', 'xúc phạm'], PINK)]):
    s += box(14 + i * 102, 46, 88, 74, lab, c, 10.5)
s += check(160, 142)
s += t(160, 182, 'Chọn cách ở giữa: nói rõ mà không gây gổ', 10.5, GREEN)
add('S2', 1, 'Ba cách đáp lời', 'Im lặng thì người kia không biết bạn không đồng ý; gây gổ dễ làm tình hình căng. Quả quyết là nói rõ, bình tĩnh.', s)

add('S2', 2, 'Câu ranh giới ba phần', 'Một câu ranh giới có ba phần: việc gì, mình thấy sao, mình muốn gì. Nếu bị ép, nhắc lại câu ngắn.',
    t(160, 28, 'Câu ranh giới', 14)
    + flow([['Khi bạn…', '(việc gì)'], ['Mình thấy…', '(cảm xúc)'], ['Mình muốn…', '(đề nghị)']], 56, 70, 14, 306, 14, 11, [LBLUE, YELLOW, G])
    + box(40, 140, 240, 34, 'Bị ép? Nhắc lại: "Mình đã nói không."', PEACH, 10.5))

# ================= BÀI 3 =================
s = t(160, 22, 'Tin cảm giác "có gì đó sai"', 13)
s += box(14, 40, 292, 30, 'Tim đập nhanh, muốn rời đi, thấy bị ép', PINK, 10.5)
s += arrow(160, 72, 160, 88, ORANGE, 3)
s += box(14, 90, 292, 30, 'Không cần bằng chứng mới được rời đi', YELLOW, 10.5)
s += arrow(160, 122, 160, 138, ORANGE, 3)
s += box(14, 140, 292, 30, 'Rời đi sớm, tới chỗ đông người', G, 10.5)
add('S3', 1, 'Tin cảm giác', 'Cảm giác bất an là tín hiệu. Bạn được rời đi sớm mà không cần giải thích hay có bằng chứng.', s)

s = t(160, 20, 'Thoát khi bị nắm cổ tay', 13)
# cánh tay của mình (ngang)
s += f'<rect x="20" y="110" width="200" height="30" rx="14" fill="{PEACH}" stroke="{NAVY}" stroke-width="2.5"/>'
# bàn tay người nắm: 4 ngón ở dưới, ngón cái ở trên, có khe
s += f'<rect x="110" y="132" width="56" height="20" rx="8" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2.5"/>'
s += f'<rect x="110" y="96" width="22" height="18" rx="8" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2.5"/>'
s += t(138, 170, '4 ngón (chắc)', 10, NAVY, '600')
s += t(84, 98, 'ngón cái', 10, NAVY, '600')
s += t(158, 108, 'khe hở', 10, RED, '700', 'start')
s += arrow(150, 118, 150, 50, ORANGE, 4)
s += box(176, 30, 132, 44, ['Xoay cổ tay,', 'rút về phía khe'], YELLOW, 10)
s += t(160, 192, 'Rút mạnh về phía mình · lùi · chạy · hét', 10.5, GREEN)
add('S3', 2, 'Thoát khi bị nắm cổ tay', 'Chỗ yếu của tay nắm là khe giữa ngón cái và các ngón khác. Xoay cổ tay, rút mạnh qua khe đó, rồi chạy.', s)

s = t(160, 20, 'Giữ khoảng cách, nói to', 13)
s += person(70, 150, 1.0, PINK)
s += f'<line x1="92" y1="104" x2="132" y2="104" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>'
s += f'<line x1="92" y1="114" x2="132" y2="114" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>'
s += bubble(150, 48, 156, 40, '"DỪNG LẠI! LÙI RA!"', 11)
s += box(150, 108, 156, 46, ['Hai tay trước ngực,', 'lòng bàn tay mở'], LBLUE, 10)
s += t(160, 186, 'Nói to cho người xung quanh nghe thấy', 10.5, GREEN)
add('S3', 3, 'Giữ khoảng cách, nói to', 'Đưa hai tay mở ra trước ngực để giữ khoảng cách và nói thật to để người xung quanh chú ý.', s)

# ================= BÀI 4 =================
s = t(160, 22, 'Bị quấy rối: làm gì?', 14)
for i, (lab, c) in enumerate([('Nói rõ: "Dừng lại."', PINK), ('Rời đi, tới chỗ có người', YELLOW), ('Ghi lại: ngày, giờ, nơi, việc', LBLUE), ('Báo người tin cậy, nơi phụ trách', G)]):
    s += num(32, 46 + i * 34, i + 1)
    s += box(48, 34 + i * 34, 258, 26, lab, c, 10.5)
s += t(160, 186, 'Không phải lỗi của bạn', 11, GREEN)
add('S4', 1, 'Bị quấy rối: làm gì?', 'Bốn việc bạn có thể làm, theo thứ tự an toàn nhất trong lúc đó. Không bắt buộc làm đủ cả bốn.', s)

s = t(160, 22, 'Khi thấy người khác bị quấy rối', 13)
s += box(14, 38, 144, 60, ['Đánh lạc hướng', '"Chị ơi, mấy giờ', 'rồi ạ?"'], YELLOW, 10)
s += box(162, 38, 144, 60, ['Nhờ người khác', 'bảo vệ, tài xế,', 'quản lý'], LBLUE, 10)
s += box(14, 104, 144, 60, ['Ghi lại', 'nếu an toàn,', 'đưa cho nạn nhân'], G, 10)
s += box(162, 104, 144, 60, ['Hỏi han sau đó', '"Bạn ổn không?"'], PEACH, 10)
s += t(160, 188, 'Chọn việc an toàn cho chính bạn', 10.5, GREEN)
add('S4', 2, 'Khi thấy người khác bị quấy rối', 'Người chứng kiến không cần đối đầu. Có thể đánh lạc hướng, nhờ người khác, ghi lại hoặc hỏi han sau.', s)

# ================= BÀI 5 =================
add('S5', 1, 'Trước – Trong – Sau chuyến đi', 'Chia chuyến đi thành ba phần, mỗi phần có một việc an toàn.',
    t(160, 28, 'Mỗi chuyến đi', 14)
    + flow([['Trước:', 'báo nơi đến,', 'giờ về'], ['Trong:', 'xem biển số,', 'ngồi sau'], ['Sau:', 'nhắn', '"đã tới"']], 56, 76, 14, 306, 14, 10.5, [LBLUE, YELLOW, G])
    + t(160, 162, 'Không về đúng giờ? Người nhà gọi ngay', 10.5, GREEN))

s = t(160, 22, 'Xe công nghệ: kiểm 3 điều', 14)
for i, lab in enumerate(['Biển số trùng trên ứng dụng', 'Tên, ảnh tài xế trùng', 'Tài xế nói đúng tên bạn trước']):
    s += check(36, 56 + i * 36)
    s += box(56, 40 + i * 36, 250, 28, lab, WHITE, 10.5)
s += t(160, 186, 'Sai một điều: không lên xe', 11, RED)
add('S5', 2, 'Xe công nghệ: kiểm 3 điều', 'Trước khi lên xe đặt qua ứng dụng, kiểm biển số, tài xế và để tài xế nói tên bạn trước.', s)

# ================= BÀI 6 =================
s = t(160, 22, 'Bị dọa tung ảnh riêng tư', 14)
s += box(14, 38, 140, 66, ['KHÔNG', 'trả tiền', 'không gửi thêm'], PINK, 10.5)
s += box(166, 38, 140, 66, ['CÓ', 'chụp lại bằng chứng', 'rồi chặn'], G, 10.5)
s += box(14, 116, 292, 44, ['Báo người tin cậy, báo nền tảng,', 'báo công an; dưới 18 tuổi gọi 111'], YELLOW, 10.5)
s += t(160, 186, 'Bạn không có lỗi. Kẻ dọa mới vi phạm', 10.5, GREEN)
add('S6', 1, 'Bị dọa tung ảnh riêng tư', 'Không trả tiền, không gửi thêm; giữ bằng chứng, chặn, báo người tin cậy và nơi có thẩm quyền.', s)

s = t(160, 22, 'Gỡ ảnh: công cụ theo tuổi', 13)
s += box(14, 40, 140, 70, ['Ảnh chụp khi', 'dưới 18 tuổi', '→ Take It Down'], LBLUE, 10.5)
s += box(166, 40, 140, 70, ['Ảnh chụp khi', 'từ 18 tuổi', '→ StopNCII'], PURP, 10.5)
s += box(14, 122, 292, 36, 'Ảnh ở lại máy bạn; chỉ gửi "dấu vân tay số"', YELLOW, 10.5)
s += t(160, 186, 'Miễn phí; gỡ được trên các nền tảng tham gia', 10, GREEN)
add('S6', 2, 'Gỡ ảnh: công cụ theo tuổi', 'Hai công cụ miễn phí tạo dấu vân tay số của ảnh để các nền tảng tham gia tự tìm và gỡ.', s)

# ================= BÀI 7 =================
s = t(160, 22, 'Lành mạnh hay kiểm soát?', 14)
s += box(14, 36, 140, 132, ['Lành mạnh', '', 'Được nói "không"', 'Có bạn bè riêng', 'Giữ điện thoại riêng', 'Cãi nhau không sợ'], G, 10)
s += box(166, 36, 140, 132, ['Kiểm soát', '', 'Ghen, theo dõi', 'Cấm gặp bạn', 'Đòi mật khẩu', 'Giữ tiền, giấy tờ', 'Đe dọa, đánh'], PINK, 10)
s += t(160, 190, 'Nhiều dấu hiệu bên phải: hỏi người tin cậy', 10.5, NAVY)
add('S7', 1, 'Lành mạnh hay kiểm soát?', 'So sánh mối quan hệ lành mạnh với mối quan hệ kiểm soát. Các dấu hiệu bên phải thường tăng dần theo thời gian.', s)

s = t(160, 22, 'Nhờ ai khi bị bạo lực', 14)
for i, (lab, c) in enumerate([('117 · bạo lực gia đình (24/7)', PINK), ('111 · dưới 18 tuổi (miễn phí, 24/7)', YELLOW), ('113 · nguy hiểm ngay', LBLUE), ('115 · bị thương', G)]):
    s += box(30, 34 + i * 34, 260, 28, lab, c, 10.5)
s += t(160, 186, 'Bạo lực không bao giờ là lỗi của bạn', 10.5, GREEN)
add('S7', 2, 'Nhờ ai khi bị bạo lực', 'Các số gọi khi bị bạo lực. Kiểm tra lại mỗi quý vì số và giờ hoạt động có thể thay đổi.', s)

# ================= BÀI 8 =================
s = t(160, 22, 'Dấu hiệu bẫy việc làm', 14)
for i, (lab, c) in enumerate([('Việc nhẹ, lương cao bất thường', PINK), ('Đi xa, ra nước ngoài gấp, "lo hết"', YELLOW), ('Giữ căn cước, hộ chiếu của bạn', LBLUE), ('Bảo giấu gia đình, cắt liên lạc', LGRAY)]):
    s += box(30, 34 + i * 32, 260, 26, lab, c, 10.5)
s += t(160, 182, 'Một dấu hiệu: dừng lại, hỏi người thân', 10.5, GREEN)
add('S8', 1, 'Dấu hiệu bẫy việc làm', 'Bốn dấu hiệu hay gặp trong lừa việc làm và mua bán người. Gặp một dấu hiệu là dừng lại hỏi.', s)

add('S8', 2, 'Kiểm tra trước khi đi xa', 'Trước khi đi làm xa, để lại cho người thân đủ thông tin và thống nhất giờ liên lạc.',
    t(160, 28, 'Trước khi đi làm xa', 14)
    + flow([['Kiểm tra', 'nơi tuyển'], ['Để lại', 'bản sao', 'giấy tờ'], ['Hẹn giờ', 'gọi về'], ['Có số', '111, 113']], 56, 76, 8, 312, 10, 10.5, [LBLUE, YELLOW, G, PINK])
    + t(160, 160, 'Giấy tờ gốc luôn ở trong tay bạn', 10.5, GREEN))

# ================= BÀI 9 =================
s = t(160, 22, 'Tiền của mình', 14)
for i, (lab, c) in enumerate([(['Biết', 'mình có', 'bao nhiêu'], LBLUE), (['Có quỹ', 'dự phòng', 'riêng'], G), (['Giữ giấy tờ', 'và mật khẩu', 'của mình'], YELLOW)]):
    s += box(14 + i * 102, 46, 88, 74, lab, c, 10.5)
s += t(160, 150, 'Không đứng tên vay hộ, không cho mượn tài khoản', 10, RED)
s += t(160, 180, 'Có tiền riêng giúp bạn có lựa chọn', 10.5, GREEN)
add('S9', 1, 'Tiền của mình', 'Ba thói quen giữ quyền tự quyết: biết mình có bao nhiêu, có dự phòng riêng, tự giữ giấy tờ và mật khẩu.', s)

add('S9', 2, 'Quỹ dự phòng nhỏ', 'Bắt đầu nhỏ: để riêng một khoản cố định mỗi lần có tiền, đến khi đủ chi phí đi lại và vài ngày ăn ở.',
    t(160, 28, 'Quỹ dự phòng: bắt đầu nhỏ', 13)
    + flow([['Mỗi lần', 'có tiền'], ['Để riêng', 'một khoản', 'cố định'], ['Đủ tiền', 'xe, vài ngày', 'ăn ở']], 56, 76, 14, 306, 14, 10.5, [YELLOW, LBLUE, G])
    + t(160, 160, 'Số tiền là của bạn, mức nào cũng được', 10.5, GREEN))

# ================= BÀI 10 =================
s = t(160, 22, 'Kế hoạch an toàn của tôi', 14)
s += paper(40, 34, 240, 150, WHITE)
for i, lab in enumerate(['1. Ba người tôi có thể nhờ', '2. Mật mã gọi đón', '3. Số khẩn cấp đã lưu', '4. Giấy tờ, tiền dự phòng ở đâu', '5. Nơi an toàn gần nhà, chỗ làm']):
    s += t(58, 62 + i * 26, lab, 10.5, NAVY, '600', 'start')
add('S10', 1, 'Kế hoạch an toàn của tôi', 'Năm phần của kế hoạch an toàn một trang. Cập nhật khi đổi chỗ ở, chỗ làm hay mối quan hệ.', s)

s = t(160, 22, 'Ba người có thể nhờ', 14)
for i, (lab, c) in enumerate([(['Người', 'gọi lúc', 'nửa đêm'], PINK), (['Người', 'cho ở nhờ', 'vài ngày'], YELLOW), (['Người', 'biết luật,', 'thủ tục'], LBLUE)]):
    s += box(14 + i * 102, 46, 88, 74, lab, c, 10.5)
s += t(160, 150, 'Ba người khác nhau thì tốt hơn một người', 10.5, NAVY, '500')
s += t(160, 180, 'Nói trước với họ rằng bạn đã chọn họ', 10.5, GREEN)
add('S10', 2, 'Ba người có thể nhờ', 'Chọn ba người cho ba việc khác nhau và báo trước cho họ biết.', s)
