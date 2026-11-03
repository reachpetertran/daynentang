# Hình minh họa và sơ đồ khóa C10 "Nền tảng không cần điện" – tiền tố Z / KHOAZ
# Hình đơn giản, in đen trắng vẫn đọc được (chữ to, viền đậm). Không vẽ trẻ em thật.
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười một bài', 14)
items = [('1. Học bằng giấy bút', SAND), ('2. Nước uống an toàn', LBLUE), ('3. Rửa tay, tiêu chảy', G), ('4. Ăn đủ, giữ đồ ăn', PEACH),
         ('5. Lửa, khói, đèn', YELLOW), ('6. Sơ cứu tay không', PINK), ('7. Chơi với con', PURP), ('8. Chữ và số cùng con', LGRAY),
         ('9. Sổ thu chi giấy', SAND), ('10. Bão lũ, mất điện', LBLUE)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 28 + (i // 2) * 29
    s += box(x, y, 142, 24, lab, c, 10.5)
s += box(89, 175, 142, 22, '11. Người có thể nhờ', G, 10.5)
add('KHOAZ', 1, 'Mười một bài', 'Mỗi bài 25 phút: đọc 10 phút, làm 10 phút, ghi lại 5 phút. Không cần điện, mạng hay màn hình.', s)

add('KHOAZ', 2, 'In một lần, dùng nhiều năm', 'Ai có điện, có máy in thì in giúp. Sau đó cả nhà học bằng giấy bút và đồ sẵn có.',
    t(160, 26, 'In một lần, dùng nhiều năm', 14)
    + flow([['Một người', 'in giúp', '(xã, trường)'], ['Đọc bài', 'bằng giấy'], ['Làm bằng', 'đồ sẵn có'], ['Ghi vào', 'Sổ nền tảng']], 56, 70, 10, 310, 10, 10.5, [LGRAY, SAND, G, YELLOW])
    + t(160, 160, 'Không cần điện, mạng hay màn hình', 11, GREEN)
    + t(160, 180, 'Giữ bài trong túi ni lông cho khỏi ướt', 10, NAVY))

# ================= BÀI 1 =================
add('Z1', 1, 'Vòng tự học bằng giấy bút', 'Đặt mục tiêu nhỏ, học, tự kiểm tra bằng thẻ giấy, rồi xem lại. Lặp lại mỗi tuần.',
    t(160, 22, 'Vòng tự học bằng giấy bút', 14)
    + cycle([['Đặt mục', 'tiêu nhỏ'], ['Học', '15 phút'], ['Tự kiểm', 'bằng thẻ'], ['Xem lại', 'cuối tuần']], 160, 112, 62, 88, 34, 10.5, [YELLOW, LBLUE, G, PEACH]))

s = t(160, 22, 'Thẻ hỏi – đáp tự làm', 14)
s += paper(30, 44, 120, 90) + t(90, 80, 'Mặt trước:', 11) + t(90, 98, 'câu hỏi', 12, ORANGE)
s += paper(170, 44, 120, 90) + t(230, 80, 'Mặt sau:', 11) + t(230, 98, 'câu trả lời', 12, GREEN)
s += t(160, 160, 'Tự hỏi mình, rồi lật thẻ xem', 10.5, NAVY) + t(160, 180, 'Sai thì để thẻ lên trên, hỏi lại ngày mai', 10, GREEN)
add('Z1', 2, 'Thẻ hỏi – đáp tự làm', 'Cắt giấy cũ thành thẻ. Viết câu hỏi một mặt, câu trả lời mặt kia. Tự hỏi mình trước khi lật thẻ.', s)

# ================= BÀI 2 =================
add('Z2', 1, 'Bốn bước có nước uống an toàn', 'Để lắng, lọc qua vải sạch, đun sôi sùng sục, rồi cất trong can có nắp.',
    t(160, 24, 'Bốn bước có nước uống an toàn', 13)
    + flow([['Để lắng', 'nước đục'], ['Lọc qua', 'vải sạch'], ['Đun sôi', 'sùng sục'], ['Cất can', 'có nắp']], 52, 72, 10, 310, 10, 10.5, [LGRAY, SAND, PEACH, LBLUE])
    + t(160, 152, 'Rót ra, không nhúng ca vào can', 11, GREEN)
    + t(160, 174, 'Đun sôi không khử được hóa chất, thuốc trừ sâu', 10, RED))

s = t(160, 22, 'Rót ra hay múc vào?', 14)
s += box(14, 40, 140, 100, ['Can có nắp,', 'rót qua vòi', 'hoặc miệng nhỏ'], G, 11)
s += box(166, 40, 140, 100, ['Chum mở nắp,', 'nhúng ca, tay', 'vào múc'], PINK, 11)
s += check(76, 160) + t(236, 166, 'Dễ bẩn lại', 11, RED) + t(84, 186, 'Giữ sạch lâu hơn', 10.5, GREEN)
add('Z2', 2, 'Cất nước đã đun', 'Nước đã đun dễ bẩn lại nếu nhúng tay hay ca vào. Cất trong can sạch, có nắp, rót ra khi dùng.', s)

# ================= BÀI 3 =================
add('Z3', 1, 'Năm lúc cần rửa tay với xà phòng', 'Sau khi đi vệ sinh, sau khi lau rửa cho bé, trước khi nấu, trước khi ăn, trước khi cho con ăn.',
    t(160, 22, 'Năm lúc rửa tay với xà phòng', 13)
    + box(14, 36, 140, 30, 'Sau khi đi vệ sinh', LBLUE, 10.5) + box(166, 36, 140, 30, 'Sau khi lau rửa cho bé', LBLUE, 10.5)
    + box(14, 74, 140, 30, 'Trước khi nấu', G, 10.5) + box(166, 74, 140, 30, 'Trước khi ăn', G, 10.5)
    + box(89, 112, 142, 30, 'Trước khi cho con ăn', YELLOW, 10.5)
    + t(160, 166, 'Xoa đủ lòng, mu, kẽ ngón, móng', 10.5, NAVY) + t(160, 186, 'Không có vòi: dùng can treo, nước chảy', 10, GREEN))

s = t(160, 22, 'Khi bị tiêu chảy', 14)
s += flow([['Uống', 'oresol', 'pha đúng gói'], ['Ăn tiếp,', 'bú mẹ', 'tiếp'], ['Theo dõi', 'dấu hiệu', 'mất nước']], 46, 70, 12, 308, 14, 10.5, [LBLUE, G, YELLOW])
s += box(20, 134, 280, 50, ['Đi trạm y tế ngay: mắt trũng, lả, uống kém,', 'có máu trong phân, sốt cao, hơn 14 ngày'], PINK, 10.5)
add('Z3', 2, 'Khi bị tiêu chảy', 'Uống oresol pha đúng hướng dẫn trên gói, ăn và bú tiếp. Có dấu hiệu nặng thì đi trạm y tế ngay.', s)

# ================= BÀI 4 =================
add('Z4', 1, 'Đĩa ăn đủ nhóm', 'Mỗi bữa cố có đủ: tinh bột, đạm, rau quả. Dùng thực phẩm địa phương, theo mùa.',
    t(160, 22, 'Một bữa đủ nhóm', 14)
    + '<circle cx="160" cy="108" r="66" fill="#ffffff" stroke="#1b2a41" stroke-width="3"/>'
    + '<path d="M160 108 L160 42 A66 66 0 0 1 217 141 Z" fill="#f6d9a8" stroke="#1b2a41" stroke-width="2"/>'
    + '<path d="M160 108 L217 141 A66 66 0 0 1 103 141 Z" fill="#f2a7a0" stroke="#1b2a41" stroke-width="2"/>'
    + '<path d="M160 108 L103 141 A66 66 0 0 1 160 42 Z" fill="#cfe6c4" stroke="#1b2a41" stroke-width="2"/>'
    + t(186, 92, 'Cơm, ngô,', 10) + t(186, 105, 'khoai', 10) + t(160, 150, 'Cá, trứng, đậu,', 10) + t(160, 163, 'thịt, tôm', 10)
    + t(132, 92, 'Rau,', 10) + t(132, 105, 'quả', 10)
    + t(160, 192, 'Uống nước sạch, ít muối, ít đường', 10, GREEN))

add('Z4', 2, 'Giữ đồ ăn khi không có tủ lạnh', 'Nấu vừa đủ ăn, ăn khi còn nóng. Đồ nấu chín không để quá 2 giờ ở nhiệt độ phòng.',
    t(160, 24, 'Không có tủ lạnh', 14)
    + flow([['Nấu vừa', 'đủ ăn'], ['Ăn khi', 'còn nóng'], ['Còn thừa:', 'đậy, để', 'chỗ mát'], ['Ăn lại:', 'đun sôi', 'kỹ']], 46, 76, 10, 310, 10, 10.5, [PEACH, YELLOW, LBLUE, G])
    + t(160, 150, 'Đồ chín không để quá 2 giờ ở nhiệt độ phòng', 10.5, RED)
    + t(160, 172, 'Ngửi, nhìn thấy lạ: bỏ đi', 10.5, NAVY))

# ================= BÀI 5 =================
s = t(160, 22, 'Bếp củi: bớt khói', 14)
s += box(14, 40, 140, 104, ['Nấu chỗ thoáng,', 'mở cửa, mở', 'lỗ thoát khói'], G, 11)
s += box(166, 40, 140, 104, ['Trẻ nhỏ', 'tránh xa khói', 'và bếp'], YELLOW, 11)
s += t(160, 168, 'Củi khô cháy ít khói hơn củi ướt', 10.5, NAVY) + t(160, 188, 'Khói trong nhà hại phổi, nhất là trẻ nhỏ', 10, RED)
add('Z5', 1, 'Bếp củi: bớt khói', 'Nấu ở chỗ thoáng, mở cửa và lỗ thoát khói, cho trẻ nhỏ tránh xa bếp và khói.', s)

s = t(160, 22, 'Dầu hỏa, nến, đèn', 14)
s += box(14, 38, 292, 34, 'Dầu hỏa: chai có nhãn, cất cao, khóa – không đựng chai nước', PINK, 10.5)
s += box(14, 80, 292, 34, 'Nến, đèn dầu: đặt trên đế vững, xa màn, mái lá', YELLOW, 10.5)
s += box(14, 122, 292, 34, 'Thổi tắt trước khi ngủ hoặc ra khỏi phòng', LBLUE, 10.5)
s += t(160, 182, 'Trẻ uống nhầm dầu: gọi 115, đi viện ngay', 10.5, RED)
add('Z5', 2, 'Dầu hỏa, nến, đèn an toàn', 'Dầu hỏa đựng chai có nhãn, cất cao. Nến đặt chỗ vững, xa vật dễ cháy, tắt trước khi ngủ.', s)

# ================= BÀI 6 =================
add('Z6', 1, 'Sơ cứu bỏng', 'Làm mát vết bỏng dưới nước mát đang chảy 20 phút, tháo nhẫn, vòng gần vết bỏng. Không bôi đá, kem đánh răng, mỡ.',
    t(160, 24, 'Sơ cứu bỏng', 14)
    + flow([['Nước mát', 'đang chảy', '20 phút'], ['Tháo nhẫn,', 'vòng, đồ', 'gần vết bỏng'], ['Phồng rộp', 'hoặc rộng:', 'đi khám']], 46, 76, 12, 308, 14, 10.5, [LBLUE, YELLOW, G])
    + t(160, 150, 'Không bôi đá, kem đánh răng, mỡ, bơ', 10.5, RED)
    + t(160, 172, 'Bỏng ở trẻ nhỏ: luôn cho đi khám', 10, NAVY))

s = t(160, 22, 'Khi nào phải chuyển viện ngay', 13)
for i, lab in enumerate(['Bất tỉnh, co giật', 'Khó thở, tím tái', 'Chảy máu ép chặt vẫn không cầm', 'Đuối nước, dù đã tỉnh', 'Bỏng rộng, phồng rộp nhiều']):
    s += box(30, 34 + i * 31, 260, 26, lab, PINK if i < 2 else YELLOW, 10.5)
add('Z6', 2, 'Khi nào phải chuyển viện ngay', 'Năm tình huống cần gọi 115 hoặc đưa đi viện ngay, không chờ.', s)

# ================= BÀI 7 =================
add('Z7', 1, 'Giao và đáp khi chơi', 'Con làm gì đó, bạn đáp lại: gọi tên, nói theo, chờ con đáp. Lặp lại như chơi bóng qua lại.',
    t(160, 22, 'Chơi là giao và đáp', 14)
    + cycle([['Con chỉ,', 'nói, nhìn'], ['Bạn đáp:', 'gọi tên'], ['Chờ con', 'đáp lại'], ['Đổi lượt,', 'chơi tiếp']], 160, 112, 62, 88, 34, 10.5, [YELLOW, G, LBLUE, PEACH]))

s = t(160, 22, 'Đồ chơi tự làm', 14)
s += box(14, 38, 140, 46, ['Chai nhựa có nắp,', 'đựng hạt to: xóc'], PEACH, 10.5)
s += box(166, 38, 140, 46, ['Hộp giấy:', 'xếp chồng, bỏ vào'], LBLUE, 10.5)
s += box(14, 92, 140, 46, ['Lá, que, đá to:', 'xếp hàng, đếm'], G, 10.5)
s += box(166, 92, 140, 46, ['Vải vụn:', 'trốn tìm, ú òa'], YELLOW, 10.5)
s += t(160, 164, 'Dưới 3 tuổi: không vật nhỏ lọt ống', 10.5, RED) + t(160, 184, 'giấy vệ sinh, dán chặt nắp chai', 10.5, RED)
add('Z7', 2, 'Đồ chơi tự làm', 'Chai, hộp, lá, vải vụn đều thành đồ chơi. Với trẻ dưới 3 tuổi, bỏ mọi vật nhỏ và dán chặt nắp chai.', s)

# ================= BÀI 8 =================
add('Z8', 1, 'Kể chuyện qua tranh', 'Không cần sách mua. Chỉ vào tranh, hỏi con, chờ con trả lời, khen và nói thêm một chút.',
    t(160, 22, 'Kể chuyện qua tranh, đổi lượt', 13)
    + flow([['Chỉ', 'vào tranh'], ['Hỏi:', '"Gì đây?"'], ['Chờ', 'con đáp'], ['Khen, nói', 'thêm 1 ý']], 50, 70, 10, 310, 10, 10.5, [SAND, YELLOW, LBLUE, G])
    + t(160, 150, 'Tranh lịch cũ, bao bì, báo, tranh tự vẽ', 10.5, NAVY)
    + t(160, 172, '10 phút mỗi ngày, cùng một giờ', 10.5, GREEN))

s = t(160, 22, 'Đếm bằng đồ thật', 14)
for i in range(5):
    s += f'<circle cx="{70 + i * 45}" cy="70" r="14" fill="{PEACH}" stroke="{NAVY}" stroke-width="2.5"/>' + t(70 + i * 45, 104, str(i + 1), 13, ORANGE)
s += box(30, 120, 260, 30, 'Chạm từng vật, đọc to một số', LBLUE, 11)
s += t(160, 172, 'Số cuối cùng là có bao nhiêu', 11, GREEN) + t(160, 190, 'Dùng quả, nắp to, đá to (không vật nhỏ)', 10, RED)
add('Z8', 2, 'Đếm bằng đồ thật', 'Chạm từng vật, đọc to một số. Số cuối cùng cho biết có bao nhiêu. Với trẻ nhỏ chỉ dùng vật to.', s)

# ================= BÀI 9 =================
add('Z9', 1, 'Sổ thu chi bằng giấy', 'Mỗi tối ghi tiền vào, tiền ra. Cuối tuần cộng lại, xem tiền đi đâu, chọn một khoản bớt.',
    t(160, 22, 'Sổ thu chi bằng giấy', 14)
    + paper(40, 38, 240, 120)
    + '<line x1="40" y1="64" x2="280" y2="64" stroke="#1b2a41" stroke-width="2"/><line x1="120" y1="38" x2="120" y2="158" stroke="#1b2a41" stroke-width="2"/><line x1="200" y1="38" x2="200" y2="158" stroke="#1b2a41" stroke-width="2"/>'
    + t(80, 56, 'Ngày', 11) + t(160, 56, 'Tiền vào', 11, GREEN) + t(240, 56, 'Tiền ra', 11, RED)
    + t(160, 182, 'Cuối tuần: cộng lại, chọn 1 khoản bớt', 10.5, GREEN))

add('Z9', 2, 'Để dành trước, tiêu sau', 'Có tiền vào thì để riêng một phần nhỏ trước, cho lúc ốm đau hay mất mùa.',
    t(160, 24, 'Để dành trước, tiêu sau', 14)
    + flow([['Có tiền', 'vào'], ['Để riêng', 'một phần', 'nhỏ'], ['Phần còn', 'lại mới', 'tiêu']], 46, 76, 12, 308, 14, 10.5, [LGRAY, G, PEACH])
    + t(160, 152, 'Quỹ để dành: cho ốm đau, mất mùa, bão lũ', 10.5, NAVY)
    + t(160, 174, 'Tránh vay nóng lãi cao', 10.5, RED))

# ================= BÀI 10 =================
s = t(160, 20, 'Túi khẩn cấp gia đình', 14)
for i, lab in enumerate(['Nước uống', 'Đồ ăn khô', 'Đèn pin, pin', 'Thuốc, sơ cứu', 'Giấy tờ (túi ni lông)', 'Áo mưa, áo ấm', 'Còi', 'Ít tiền lẻ']):
    x = 14 + (i % 2) * 150; y = 32 + (i // 2) * 34
    s += box(x, y, 142, 28, lab, [LBLUE, PEACH, YELLOW, PINK][i // 2], 10.5)
s += t(160, 182, 'Để chỗ dễ lấy, cả nhà biết chỗ để', 10.5, GREEN)
add('Z10', 1, 'Túi khẩn cấp gia đình', 'Chuẩn bị sẵn một túi: nước, đồ ăn khô, đèn, thuốc, giấy tờ bọc ni lông, áo mưa, còi, ít tiền.', s)

add('Z10', 2, 'Trước – trong – sau bão lũ', 'Trước: chuẩn bị túi, nghe tin. Trong: nghe chính quyền, sơ tán khi được báo. Sau: chờ nước rút, đun sôi nước, cẩn thận điện.',
    t(160, 22, 'Trước – Trong – Sau bão lũ', 13)
    + flow([['Trước:', 'túi khẩn cấp,', 'nghe tin, gia', 'cố nhà'], ['Trong:', 'nghe chính', 'quyền, sơ tán', 'khi được báo'], ['Sau:', 'chờ nước rút,', 'đun sôi nước,', 'tránh dây điện']], 40, 98, 12, 308, 14, 10, [YELLOW, LBLUE, G])
    + t(160, 164, 'Không lội, không bơi qua dòng nước chảy xiết', 10.5, RED)
    + t(160, 184, 'Trẻ em luôn trong tầm tay người lớn', 10.5, NAVY))

# ================= BÀI 11 =================
s = t(160, 20, 'Vòng người có thể nhờ', 14)
s += '<circle cx="160" cy="110" r="80" fill="#cfe6c4" stroke="#1b2a41" stroke-width="2.5"/>'
s += '<circle cx="160" cy="110" r="54" fill="#f6d9a8" stroke="#1b2a41" stroke-width="2.5"/>'
s += '<circle cx="160" cy="110" r="28" fill="#f6c445" stroke="#1b2a41" stroke-width="2.5"/>'
s += t(160, 114, 'Nhà mình', 10) + t(160, 74, 'Họ hàng, hàng xóm', 10) + t(160, 46, 'Trưởng thôn, trạm y tế', 10)
s += t(160, 182, 'Hội phụ nữ, trường, công an xã', 10)
add('Z11', 1, 'Vòng người có thể nhờ', 'Vòng trong là nhà mình, vòng giữa là họ hàng và hàng xóm, vòng ngoài là thôn, trạm y tế, trường, công an xã.', s)

add('Z11', 2, 'Kế hoạch gia đình một trang', 'Một trang ghi: ai lo việc gì, gặp nhau ở đâu khi có chuyện, số cần gọi, ai đón con.',
    t(160, 24, 'Kế hoạch gia đình một trang', 13)
    + box(20, 40, 280, 28, 'Khi có chuyện, cả nhà gặp nhau ở: ………', SAND, 10.5)
    + box(20, 74, 280, 28, 'Người đón con nếu bố mẹ vắng: ………', YELLOW, 10.5)
    + box(20, 108, 280, 28, 'Số gọi: 115 · 113 · 114 · 111 · trưởng thôn', PINK, 10.5)
    + box(20, 142, 280, 28, 'Ai lo người già, người ốm: ………', LBLUE, 10.5)
    + t(160, 190, 'Dán chỗ cả nhà thấy, xem lại mỗi năm', 10.5, GREEN))
