# Hình minh họa và sơ đồ khóa C4 "Vững nghề" – tiền tố E / KHOAE
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười tuần', 14)
items = [('1. Bậc thang kỹ năng', SAND), ('2. Học tay nghề', PINK), ('3. An toàn trước hết', YELLOW), ('4. Làm đúng lần đầu', LBLUE),
         ('5. Chính trực', G), ('6. Hỏi, báo cáo', PURP), ('7. Quyền cơ bản', PEACH), ('8. Sức khỏe nghề', LGRAY),
         ('9. Đồng lương đầu', SAND), ('10. Hồ sơ kỹ năng', PINK)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 30 + (i // 2) * 33
    s += box(x, y, 142, 27, lab, c, 10.5)
add('KHOAE', 1, 'Mười tuần', 'Mỗi tuần một bài 25 phút: đọc, làm ngay ở xưởng hoặc ở nhà, rồi xem lại.', s)

add('KHOAE', 2, 'Xem – Làm cùng – Tự làm – Tự kiểm', 'Vòng học tay nghề dùng trong cả khóa: xem người giỏi làm, làm cùng, tự làm, tự kiểm rồi sửa.',
    t(160, 28, 'Vòng học tay nghề', 14)
    + cycle([['Xem', 'thầy làm'], ['Làm cùng,', 'thầy chỉnh'], ['Tự làm,', 'thầy xem'], ['Tự kiểm,', 'sửa lỗi']], 160, 112, 58, 90, 34, 10.5, [LBLUE, YELLOW, G, PINK]))

# ================= BÀI 1 =================
s = t(160, 22, 'Bậc thang kỹ năng', 14)
for i, (lab, c) in enumerate([(['Bậc 1', 'thầy cầm tay'], PINK), (['Bậc 2', 'thầy đứng xem'], YELLOW), (['Bậc 3', 'tự làm đạt'], G)]):
    s += box(14 + i * 102, 130 - i * 44, 88, 40, lab, c, 10.5)
    if i < 2:
        s += arrow(14 + i * 102 + 90, 140 - i * 44, 14 + (i + 1) * 102 - 2, 108 - i * 44, ORANGE, 3)
s += t(160, 190, 'Mỗi kỹ năng leo từng bậc', 10.5, GREEN)
add('E1', 1, 'Bậc thang kỹ năng', 'Mỗi kỹ năng đi qua ba bậc: làm khi thầy cầm tay, làm khi thầy đứng xem, tự làm đạt chuẩn.', s)

s = t(160, 22, 'Mức đạt đo được', 14)
s += box(14, 40, 140, 62, ['Chưa rõ', '"May cho', 'đẹp hơn"'], LGRAY, 10.5)
s += arrow(156, 71, 172, 71, ORANGE, 3)
s += box(174, 40, 132, 62, ['Đo được', '"1 mét đường thẳng,', 'lệch ≤ 2 mm"'], G, 10)
s += box(14, 118, 292, 40, ['Có việc làm, số đo, thời gian', '(ví dụ minh họa)'], YELLOW, 10.5)
s += t(160, 184, 'Đo được thì biết mình đã đạt chưa', 10.5, GREEN)
add('E1', 2, 'Mức đạt đo được', 'Mức đạt tốt nói rõ làm gì, sai số bao nhiêu, trong bao lâu. Con số ở đây chỉ là ví dụ.', s)

# ================= BÀI 2 =================
add('E2', 1, 'Luyện có chủ đích', 'Chọn một phần khó, làm lại nhiều lần, nhận góp ý ngay, mỗi lần sửa một điểm.',
    t(160, 28, 'Luyện có chủ đích', 14)
    + flow([['Chọn', '1 phần', 'khó'], ['Làm', 'lại', 'nhiều lần'], ['Nhận', 'góp ý', 'ngay'], ['Sửa', '1 điểm', 'mỗi lần']], 56, 76, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
    + t(160, 160, 'Đếm lỗi đã sửa, không chỉ đếm giờ', 11, GREEN))

s = t(160, 22, 'Luyện tập giải thích được bao nhiêu?', 13)
data = [('Trò chơi', 26), ('Âm nhạc', 21), ('Thể thao', 18), ('Học tập', 4), ('Nghề nghiệp', 1)]
for i, (lab, v) in enumerate(data):
    y = 40 + i * 26
    s += t(92, y + 14, lab, 10.5, NAVY, '600', 'end')
    s += f'<rect x="100" y="{y}" width="{max(v * 7, 3)}" height="18" rx="4" fill="{LBLUE}" stroke="{NAVY}" stroke-width="1.5"/>'
    s += t(108 + max(v * 7, 3), y + 14, ('dưới 1%' if v == 1 else f'{v}%'), 10, NAVY, '600', 'start')
s += t(160, 190, 'Macnamara và cộng sự 2014, 88 nghiên cứu', 9.5, GRAY, '500')
add('E2', 2, 'Luyện tập giải thích được bao nhiêu?', 'Phần chênh lệch về thành tích mà luyện tập giải thích được, theo lĩnh vực. Ở nghề nghiệp: dưới 1%.', s)

# ================= BÀI 3 =================
add('E3', 1, 'Năm câu hỏi trước việc mới', 'Trước mỗi việc mới, hỏi: nguy hiểm gì, bảo hộ gì, đã được hướng dẫn chưa, sự cố thì sao, hỏi ai.',
    t(160, 26, 'Trước việc mới, hỏi 5 câu', 14)
    + box(14, 40, 140, 30, '1. Có thể bị thương ra sao?', PINK, 10)
    + box(166, 40, 140, 30, '2. Cần đồ bảo hộ gì?', YELLOW, 10)
    + box(14, 80, 140, 30, '3. Đã được hướng dẫn?', LBLUE, 10)
    + box(166, 80, 140, 30, '4. Sự cố thì làm gì?', G, 10)
    + box(90, 120, 140, 30, '5. Hỏi ai?', PURP, 10)
    + t(160, 178, 'Chưa trả lời được thì chưa làm', 11, GREEN))

s = t(160, 22, 'Thấy rõ nguy hiểm: dừng – báo – chờ', 13)
s += flow([['Dừng', 'việc'], ['Báo ngay', 'quản lý'], ['Chờ', 'xử lý xong'], ['Làm', 'tiếp']], 50, 70, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
s += t(160, 148, 'Luật ATVSLĐ 2015: quyền từ chối khi thấy rõ', 10, NAVY, '500')
s += t(160, 164, 'nguy cơ tai nạn nghiêm trọng', 10, NAVY, '500')
s += t(160, 186, 'Không bị coi là vi phạm kỷ luật', 10.5, GREEN)
add('E3', 2, 'Dừng – báo – chờ', 'Khi thấy rõ nguy cơ tai nạn nghiêm trọng: dừng việc, báo ngay người quản lý trực tiếp, chờ khắc phục rồi mới làm tiếp.', s)

# ================= BÀI 4 =================
add('E4', 1, 'Làm mẫu đầu rồi mới làm loạt', 'Hiểu yêu cầu, làm một sản phẩm mẫu, tự kiểm theo danh sách, đạt rồi mới làm tiếp.',
    t(160, 28, 'Làm đúng ngay lần đầu', 14)
    + flow([['Hiểu', 'yêu cầu'], ['Làm', '1 mẫu'], ['Tự kiểm', 'theo danh', 'sách'], ['Đạt mới', 'làm loạt']], 56, 76, 8, 312, 10, 10.5, [LGRAY, YELLOW, LBLUE, G])
    + t(160, 160, 'Sai ở mẫu đầu rẻ hơn sai cả loạt', 11, GREEN))

s = t(160, 22, '5S cho chỗ làm', 14)
for i, (lab, c) in enumerate([('Sàng lọc', PINK), ('Sắp xếp', YELLOW), ('Sạch sẽ', LBLUE), ('Săn sóc', G), ('Sẵn sàng', PURP)]):
    s += box(12 + i * 60, 50, 56, 56, ['S' + str(i + 1), lab], c, 10)
s += t(160, 136, 'Bỏ đồ thừa · đúng chỗ · lau sạch', 10.5, NAVY, '500')
s += t(160, 154, 'giữ nề nếp · thành thói quen', 10.5, NAVY, '500')
s += t(160, 182, 'Chỗ làm gọn thì ít lỗi, ít tai nạn hơn', 10.5, GREEN)
add('E4', 2, '5S cho chỗ làm', 'Năm việc giữ chỗ làm gọn: sàng lọc, sắp xếp, sạch sẽ, săn sóc, sẵn sàng.', s)

# ================= BÀI 5 =================
s = t(160, 22, 'Chính trực trong nghề', 14)
s += box(14, 38, 92, 96, ['Giờ giấc', '', 'đến sớm,', 'báo trước', 'khi trễ'], YELLOW, 10.5)
s += box(114, 38, 92, 96, ['Nói thật', '', 'báo lỗi,', 'không ghi', 'khống'], LBLUE, 10.5)
s += box(214, 38, 92, 96, ['Làm thật', '', 'không bỏ', 'bước kiểm,', 'không lấy đồ'], G, 10.5)
s += t(160, 166, 'Người ta giao việc khó cho người tin được', 10.5, GREEN)
add('E5', 1, 'Chính trực trong nghề', 'Ba điều làm nên chữ tín: đúng giờ, nói thật về việc mình làm, làm đủ bước.', s)

add('E5', 2, 'Nhận lỗi bốn bước', 'Khi làm hỏng: nói việc gì xảy ra, nói hậu quả, đề xuất cách sửa, nói cách tránh lần sau.',
    t(160, 28, 'Nhận lỗi bốn bước', 14)
    + flow([['Nói', 'việc gì', 'xảy ra'], ['Nói', 'hậu quả'], ['Đề xuất', 'cách sửa'], ['Cách tránh', 'lần sau']], 56, 76, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
    + t(160, 160, 'Báo sớm thì sửa được nhiều hơn', 11, GREEN))

# ================= BÀI 6 =================
add('E6', 1, 'Báo cáo ba phần', 'Báo cáo ngắn gồm ba phần: đã xong gì, đang vướng gì, cần gì.',
    t(160, 28, 'Báo cáo ba phần', 14)
    + flow([['Đã xong', 'gì?'], ['Đang', 'vướng gì?'], ['Cần', 'gì?']], 56, 76, 20, 300, 16, 11.5, [G, YELLOW, LBLUE])
    + t(160, 160, 'Ngắn, đúng lúc, có số liệu', 11, GREEN))

s = t(160, 22, 'Nhận góp ý', 14)
s += cycle([['Nghe', 'hết'], ['Cảm ơn,', 'hỏi rõ'], ['Sửa'], ['Báo lại']], 160, 110, 56, 84, 32, 10.5, [LBLUE, YELLOW, G, PINK])
add('E6', 2, 'Nhận góp ý', 'Nghe hết, cảm ơn và hỏi một điểm cụ thể, sửa, rồi báo lại cho người góp ý.', s)

# ================= BÀI 7 =================
s = t(160, 22, 'Trước khi nhận việc, hỏi rõ', 14)
for i, (lab, c) in enumerate([('Làm việc gì?', PINK), ('Giờ làm?', YELLOW), ('Tiền công, trả khi nào?', LBLUE), ('Có giấy tờ, hợp đồng?', G)]):
    s += box(30, 36 + i * 32, 260, 26, lab, c, 10.5)
s += t(160, 184, 'Không nộp tiền, không giao giấy tờ gốc', 10.5, RED)
add('E7', 1, 'Trước khi nhận việc, hỏi rõ', 'Bốn câu hỏi trước khi nhận học nghề, thực tập hay làm thêm; không đặt cọc, không giao giấy tờ gốc.', s)

s = t(160, 22, 'Dưới 18 tuổi đi làm', 14)
s += box(14, 40, 140, 80, ['Tối đa', '8 giờ/ngày', '40 giờ/tuần'], LBLUE, 11)
s += box(166, 40, 140, 80, ['Không làm', 'việc nặng nhọc,', 'nguy hiểm theo', 'danh mục cấm'], PINK, 10.5)
s += t(160, 150, 'Bộ luật Lao động 2019', 10.5, NAVY, '500')
s += t(160, 176, 'Bị ép làm việc cấm: gọi 111', 10.5, GREEN)
add('E7', 2, 'Dưới 18 tuổi đi làm', 'Người 15 đến dưới 18 tuổi làm tối đa 8 giờ một ngày, 40 giờ một tuần, không làm việc thuộc danh mục cấm.', s)

# ================= BÀI 8 =================
s = t(160, 22, 'Nâng vật đúng cách', 14)
s += flow([['Xem', 'vật nặng', 'cỡ nào'], ['Đứng gần,', 'gập gối'], ['Lưng thẳng,', 'không vặn'], ['Nặng quá:', 'nhờ, dùng', 'xe đẩy']], 50, 80, 8, 312, 10, 10.5, [LGRAY, YELLOW, LBLUE, G])
s += t(160, 160, 'Đổi hướng bằng chân, không xoay lưng', 10.5, GREEN)
add('E8', 1, 'Nâng vật đúng cách', 'Ước lượng vật trước, đứng gần, gập gối, giữ lưng thẳng, quá nặng thì nhờ người hoặc dùng xe đẩy.', s)

s = t(160, 22, 'Bảo vệ cơ thể khi làm nghề', 14)
for i, (lab, c) in enumerate([(['Mắt', 'kính,', 'mặt nạ hàn'], LBLUE), (['Tai', 'nút tai,', 'chụp tai'], YELLOW), (['Phổi', 'khẩu trang', 'đúng loại'], G), (['Tay, chân', 'găng,', 'giày'], PINK)]):
    s += box(12 + i * 76, 44, 70, 84, lab, c, 10)
s += t(160, 160, 'Phải nói to mới nghe được cách 1 mét:', 10.5, NAVY, '500')
s += t(160, 178, 'cần bảo vệ tai', 10.5, GREEN)
add('E8', 2, 'Bảo vệ cơ thể khi làm nghề', 'Mắt, tai, phổi, tay chân: mỗi phần có đồ bảo hộ riêng, dùng đúng việc.', s)

# ================= BÀI 9 =================
s = t(160, 22, 'Chia lương ngay khi nhận', 14)
for i, (lab, c) in enumerate([(['1', 'Cố định'], LGRAY), (['2', 'Ăn uống'], YELLOW), (['3', 'Dự phòng'], G), (['4', 'Còn lại'], LBLUE)]):
    s += box(14 + i * 74, 50, 66, 66, lab, c, 11)
s += t(160, 150, 'Cố định: trọ, điện nước, đi lại, gửi nhà', 10.5, NAVY, '500')
s += t(160, 178, 'Dự phòng trước, tiêu sau', 11, GREEN)
add('E9', 1, 'Chia lương ngay khi nhận', 'Ngày nhận lương, chia ngay thành bốn phần: cố định, ăn uống, dự phòng, phần còn lại.', s)

s = t(160, 22, 'Dấu hiệu lừa đảo việc làm', 14)
for i, (lab, c) in enumerate([('Việc nhẹ, lương cao bất thường', PINK), ('Đòi đặt cọc, "phí hồ sơ"', YELLOW), ('Mượn tài khoản, căn cước', LBLUE), ('Đe dọa, bắt giữ bí mật', LGRAY)]):
    s += box(30, 34 + i * 32, 260, 26, lab, c, 10.5)
s += t(160, 182, 'Dừng · không chuyển tiền · gọi người thân', 10.5, GREEN)
add('E9', 2, 'Dấu hiệu lừa đảo việc làm', 'Bốn dấu hiệu thường gặp; gặp một dấu hiệu là dừng, không chuyển tiền, gọi người thân.', s)

# ================= BÀI 10 =================
s = t(160, 22, 'Hồ sơ kỹ năng', 14)
s += paper(40, 34, 240, 150, WHITE)
for i, lab in enumerate(['1. Kỹ năng đạt bậc 3', '2. Sản phẩm đã làm (mô tả, ảnh)', '3. Nhận xét của thầy, quản đốc', '4. Chứng chỉ (nếu có)']):
    s += t(60, 66 + i * 28, lab, 10.5, NAVY, '600', 'start')
add('E10', 1, 'Hồ sơ kỹ năng', 'Hồ sơ kỹ năng gồm kỹ năng đã đạt, sản phẩm đã làm, nhận xét và chứng chỉ nếu có.', s)

add('E10', 2, 'Kể chuyện khi phỏng vấn', 'Khi phỏng vấn, kể một việc thật theo ba phần: tình huống, việc mình làm, kết quả.',
    t(160, 28, 'Kể khi phỏng vấn', 14)
    + flow([['Tình', 'huống'], ['Việc', 'mình làm'], ['Kết quả,', 'học được gì']], 56, 76, 20, 300, 16, 11.5, [LBLUE, YELLOW, G])
    + t(160, 160, 'Kể việc thật, có con số nếu có', 11, GREEN))
