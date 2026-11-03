# Hình minh họa và sơ đồ khóa C3 "Tự học – tự quản" – tiền tố D / KHOAD
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười tuần', 14)
items = [('1. Mục tiêu học kỳ', SAND), ('2. Lịch tuần', PINK), ('3. Đọc, ghi chú', LBLUE), ('4. Ôn tập', YELLOW),
         ('5. Tập trung', G), ('6. Làm việc nhóm', PURP), ('7. Thi cử', PEACH), ('8. Ngủ, ăn, vận động', LGRAY),
         ('9. Tiền', SAND), ('10. Khi quá tải', PINK)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 30 + (i // 2) * 33
    s += box(x, y, 142, 27, lab, c, 10.5)
add('KHOAD', 1, 'Mười tuần', 'Mỗi tuần một bài 25 phút: đọc, làm, rồi xem lại với bạn học hoặc tự viết.', s)

add('KHOAD', 2, 'Lên kế hoạch – Làm – Xem lại', 'Vòng tự học dùng trong cả khóa: lên kế hoạch, làm và tự theo dõi, rồi xem lại để chỉnh cách học.',
    t(160, 28, 'Vòng tự học', 14)
    + cycle([['Lên', 'kế hoạch'], ['Làm và', 'tự theo dõi'], ['Xem lại'], ['Chỉnh', 'cách học']], 160, 112, 58, 90, 34, 10.5, [YELLOW, G, LBLUE, PINK]))

# ================= BÀI 1 =================
add('D1', 1, 'Chia ngược mục tiêu', 'Từ mục tiêu cuối học kỳ, chia thành mốc giữa kỳ, mốc tháng, rồi việc làm tuần này.',
    t(160, 28, 'Chia ngược mục tiêu', 14)
    + flow([['Mục tiêu', 'cuối kỳ'], ['Mốc', 'giữa kỳ'], ['Mốc', 'tháng này'], ['Việc', 'tuần này']], 56, 76, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
    + t(160, 160, 'Nghĩ từ đích về, làm từ hôm nay', 11.5, GREEN))

s = t(160, 22, 'Mục tiêu đo được', 14)
s += box(14, 40, 140, 62, ['Chưa rõ', '"Học Toán', 'chăm hơn"'], LGRAY, 10.5)
s += arrow(156, 71, 172, 71, ORANGE, 3)
s += box(174, 40, 132, 62, ['Đo được', '"Làm 3 đề/tuần,', 'giữa kỳ 7,5"'], G, 10.5)
s += box(14, 118, 292, 40, ['Có cả việc mình làm (số đề, số giờ)', 'và kết quả mong muốn (điểm số)'], YELLOW, 10.5)
s += t(160, 184, 'Điểm còn phụ thuộc đề; việc làm thì do mình', 10.5, GREEN)
add('D1', 2, 'Mục tiêu đo được', 'Mục tiêu tốt nói rõ làm gì, bao nhiêu, khi nào; có cả việc mình làm được và kết quả mong muốn.', s)

# ================= BÀI 2 =================
s = t(160, 22, 'Xếp lịch tuần', 14)
s += box(14, 38, 92, 96, ['1. Việc', 'cố định', '', 'lớp, ngủ,', 'ăn, đi lại'], LGRAY, 10.5)
s += box(114, 38, 92, 96, ['2. Khối', 'học chính', '', '45–90 phút', 'việc khó'], YELLOW, 10.5)
s += box(214, 38, 92, 96, ['3. Chỗ', 'trống', '', 'nghỉ, việc', 'phát sinh'], G, 10.5)
s += t(160, 160, 'Xếp theo thứ tự 1 → 2 → 3', 11, NAVY, '600')
s += t(160, 180, 'Lịch kín 100% sẽ vỡ', 10.5, GREEN)
add('D2', 1, 'Xếp lịch tuần', 'Điền việc cố định trước, rồi khối học chính, và chừa chỗ trống cho việc phát sinh.', s)

s = t(160, 22, 'Mình hay đoán thiếu thời gian', 14)
s += f'<rect x="40" y="60" width="122" height="30" rx="6" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>'
s += t(101, 80, 'Dự đoán: 34 ngày', 10.5)
s += f'<rect x="40" y="104" width="200" height="30" rx="6" fill="{PINK}" stroke="{NAVY}" stroke-width="2"/>'
s += t(140, 124, 'Thực tế: 55 ngày', 10.5)
s += t(160, 158, 'Cách sửa: ước lượng rồi cộng thêm một nửa', 10.5, GREEN)
s += t(160, 180, 'Theo Buehler, Griffin &amp; Ross 1994', 9.5, GRAY, '500')
add('D2', 2, 'Mình hay đoán thiếu thời gian', 'Sinh viên đoán làm xong luận văn trong khoảng 34 ngày, thực tế mất khoảng 55 ngày.', s)

# ================= BÀI 3 =================
add('D3', 1, 'Đọc chủ động', 'Lướt trước, đặt câu hỏi, đọc từng đoạn, gấp sách nói lại bằng lời mình.',
    t(160, 28, 'Đọc chủ động', 14)
    + flow([['Lướt', 'tiêu đề'], ['Đặt', '2–3', 'câu hỏi'], ['Đọc', 'từng', 'đoạn'], ['Gấp sách,', 'nói lại']], 56, 76, 8, 312, 10, 10.5, [LGRAY, YELLOW, LBLUE, G])
    + t(160, 160, 'Đọc lại và tô màu cho cảm giác quen, ít giúp nhớ', 10.5, GREEN))

s = t(160, 20, 'Trang ghi chú hai cột', 14)
s += paper(40, 32, 240, 150, WHITE)
s += f'<line x1="110" y1="40" x2="110" y2="140" stroke="{NAVY}" stroke-width="2"/>'
s += f'<line x1="48" y1="140" x2="272" y2="140" stroke="{NAVY}" stroke-width="2"/>'
s += t(76, 62, 'Câu hỏi', 10.5, NAVY, '700') + t(76, 80, 'từ khóa', 10, NAVY, '500')
s += t(190, 62, 'Ý chính', 10.5, NAVY, '700') + t(190, 80, 'bằng lời mình', 10, NAVY, '500') + t(190, 98, 'ví dụ, sơ đồ', 10, NAVY, '500')
s += t(160, 160, 'Tóm tắt 2–3 câu', 10.5, NAVY, '700')
add('D3', 2, 'Trang ghi chú hai cột', 'Bên phải ghi ý chính bằng lời mình, bên trái ghi câu hỏi; cuối trang tóm tắt 2–3 câu.', s)

# ================= BÀI 4 =================
s = t(160, 22, 'Tự kiểm tra', 14)
s += box(14, 42, 130, 70, ['Đọc lại', '', 'thấy quen,', 'tưởng đã nhớ'], LGRAY, 10.5)
s += box(176, 42, 130, 70, ['Tự kiểm tra', '', 'gấp sách,', 'tự nhớ ra'], G, 10.5)
s += t(160, 82, 'vs', 13, ORANGE, '800')
s += t(160, 140, 'Nhớ ra thấy khó là đang học', 11, NAVY, '600')
s += t(160, 160, 'Mức hữu ích cao (Dunlosky et al. 2013)', 9.5, GRAY, '500')
add('D4', 1, 'Tự kiểm tra thay vì đọc lại', 'Gấp sách và tự nhớ ra giúp nhớ lâu hơn đọc lại. Thấy khó là dấu hiệu đang học.', s)

s = t(160, 22, 'Ôn giãn cách', 14)
s += f'<line x1="20" y1="100" x2="300" y2="100" stroke="{NAVY}" stroke-width="3"/>'
for x, lab in [(30, 'Học'), (80, '+1 ngày'), (140, '+3 ngày'), (210, '+1 tuần'), (285, '+3 tuần')]:
    s += f'<circle cx="{x}" cy="100" r="9" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2"/>'
    s += t(x, 80, lab, 10, NAVY, '600')
s += t(160, 140, 'Khoảng cách giãn dần', 11, NAVY, '600')
s += t(160, 160, 'Muốn nhớ càng lâu, khoảng ôn càng dài', 10.5, GREEN)
s += t(160, 180, 'Lịch gợi ý, không phải con số cố định', 9.5, GRAY, '500')
add('D4', 2, 'Ôn giãn cách', 'Chia việc ôn ra nhiều lần, khoảng cách giãn dần, thay vì học dồn một buổi.', s)

# ================= BÀI 5 =================
add('D5', 1, 'Một khối tập trung', 'Chọn một việc, cất điện thoại xa, học 25–50 phút, rồi nghỉ ngắn.',
    t(160, 28, 'Một khối tập trung', 14)
    + flow([['Chọn', '1 việc'], ['Cất máy', 'xa, tắt', 'báo'], ['Học', '25–50', 'phút'], ['Nghỉ', '5–10', 'phút']], 56, 76, 8, 312, 10, 10.5, [YELLOW, PINK, G, LBLUE])
    + t(160, 160, 'Ý chen ngang? Ghi ra giấy rồi quay lại', 11, GREEN))

s = t(160, 22, 'Khi lớp cho dùng thiết bị', 14)
s += box(14, 42, 140, 80, ['Buổi cấm', 'thiết bị', '', 'điểm thi cuối kỳ', 'cao hơn'], G, 10.5)
s += box(166, 42, 140, 80, ['Buổi cho', 'dùng thiết bị', '', 'điểm thi cuối kỳ', 'thấp hơn ≥ 5%'], PINK, 10.5)
s += t(160, 146, 'Kể cả bạn không dùng cũng bị ảnh hưởng', 10.5, NAVY, '600')
s += t(160, 166, '118 sinh viên, Glass &amp; Kang (Educational Psychology)', 9.5, GRAY, '500')
add('D5', 2, 'Khi lớp cho dùng thiết bị', 'Trong một thử nghiệm với 118 sinh viên, buổi được dùng thiết bị cho điểm thi cuối kỳ thấp hơn.', s)

# ================= BÀI 6 =================
add('D6', 1, 'Buổi họp nhóm đầu tiên', 'Thống nhất mục tiêu, chia việc, đặt hạn và quy tắc liên lạc ngay từ buổi đầu.',
    t(160, 28, 'Buổi họp nhóm đầu tiên', 14)
    + flow([['Mục tiêu', 'chung'], ['Chia', 'việc rõ', 'người'], ['Hạn', 'từng', 'phần'], ['Quy tắc', 'liên lạc']], 56, 76, 8, 312, 10, 10.5, [YELLOW, G, PINK, LBLUE])
    + t(160, 160, 'Ai cũng có phần, ai cũng chịu trách nhiệm', 11, GREEN))

s = t(160, 22, 'Khi bạn chưa làm phần mình', 14)
s += box(14, 40, 92, 84, ['1. Nhắc', 'riêng, sớm', '', 'kèm hạn mới'], G, 10.5)
s += box(114, 40, 92, 84, ['2. Hỏi', 'cần giúp gì', '', 'chia lại', 'nếu cần'], YELLOW, 10.5)
s += box(214, 40, 92, 84, ['3. Báo', 'giảng viên', '', 'kèm bảng', 'phân công'], PEACH, 10.5)
s += t(160, 150, 'Nói về việc, không nói về người', 11, NAVY, '600')
s += t(160, 170, 'Không làm thay, không đứng tên phần không làm', 10, GREEN)
add('D6', 2, 'Khi bạn chưa làm phần mình', 'Nhắc riêng và sớm, hỏi cần giúp gì, rồi mới báo giảng viên kèm bằng chứng.', s)

# ================= BÀI 7 =================
add('D7', 1, 'Ba tuần trước kỳ thi', 'Lập lịch ôn ngược từ ngày thi, làm đề như thi thật, phân loại lỗi, rồi ôn lại phần yếu.',
    t(160, 28, 'Ôn thi ba tuần', 14)
    + flow([['Tuần 1', 'hệ thống', 'kiến thức'], ['Tuần 2', 'làm đề', 'bấm giờ'], ['Tuần 3', 'sửa lỗi,', 'ôn phần yếu'], ['Đêm', 'trước:', 'ngủ đủ']], 56, 76, 8, 312, 10, 10.5, [LBLUE, YELLOW, PINK, PURP])
    + t(160, 160, 'Không thức trắng đêm trước khi thi', 11, GREEN))

s = t(160, 22, 'Phân loại lỗi sau mỗi đề', 14)
for i, (lab, c) in enumerate([(['Chưa', 'biết'], PINK), (['Nhầm,', 'ẩu'], PEACH), (['Đọc', 'sai đề'], YELLOW), (['Hết', 'giờ'], LBLUE)]):
    s += box(14 + i * 75, 44, 67, 56, lab, c, 10.5)
s += t(160, 126, 'Mỗi loại lỗi một cách sửa khác nhau', 11, NAVY, '600')
s += t(160, 146, 'Chưa biết → học lại · Nhầm → soát lại', 10, NAVY, '500')
s += t(160, 164, 'Sai đề → gạch từ khóa · Hết giờ → làm câu chắc trước', 10, NAVY, '500')
add('D7', 2, 'Phân loại lỗi sau mỗi đề', 'Chia lỗi thành bốn loại để biết cần học lại, soát lại, đọc kỹ đề hay chia giờ.', s)

# ================= BÀI 8 =================
s = t(160, 22, 'Ba nền khi đi học', 14)
s += box(14, 40, 92, 100, ['Ngủ', '13–18 tuổi:', '8–10 giờ', '18+: từ', '7 giờ'], PURP, 10.5)
s += box(114, 40, 92, 100, ['Vận động', '18–64 tuổi:', '150–300', 'phút/tuần'], G, 10.5)
s += box(214, 40, 92, 100, ['Ăn', 'đủ bữa,', 'mang nước,', 'không bỏ', 'bữa sáng'], PEACH, 10.5)
s += t(160, 164, 'Thức trắng ôn thi làm khó tập trung', 10.5, GREEN)
s += t(160, 184, 'Theo AASM, WHO', 9.5, GRAY, '500')
add('D8', 1, 'Ba nền khi đi học', 'Ngủ đủ theo tuổi, vận động đều trong tuần, ăn đủ bữa. Thiếu một nền thì việc học khó hơn.', s)

add('D8', 2, 'Vận động xen giờ học', 'Sau mỗi một đến hai khối học, đứng dậy đi bộ, giãn cơ, uống nước rồi quay lại.',
    t(160, 28, 'Xen vận động vào giờ học', 14)
    + flow([['Khối', 'học 1'], ['Đi bộ', '5–10', 'phút'], ['Khối', 'học 2'], ['Uống', 'nước,', 'giãn cơ']], 56, 76, 8, 312, 10, 10.5, [YELLOW, G, YELLOW, LBLUE])
    + t(160, 160, 'Ngồi lâu thì đứng dậy, kể cả mùa thi', 11, GREEN))

# ================= BÀI 9 =================
s = t(160, 22, 'Chia tiền tháng', 14)
s += box(14, 40, 70, 90, ['1', 'Cố định', 'trọ, điện,', 'đi lại'], LGRAY, 10)
s += box(90, 40, 70, 90, ['2', 'Ăn', 'uống'], YELLOW, 10)
s += box(166, 40, 70, 90, ['3', 'Dự', 'phòng', 'nhỏ'], G, 10)
s += box(242, 40, 64, 90, ['4', 'Phần', 'còn lại'], PEACH, 10)
s += t(160, 156, 'Chia theo thứ tự 1 → 4 ngay khi nhận tiền', 10.5, NAVY, '600')
s += t(160, 176, 'Muốn mua thứ không cần? Chờ 24 giờ', 10.5, GREEN)
add('D9', 1, 'Chia tiền tháng', 'Nhận tiền xong, chia ngay cho khoản cố định, ăn uống, dự phòng, rồi mới đến phần còn lại.', s)

s = t(160, 22, 'Dấu hiệu lừa đảo', 14)
for i, (lab, c) in enumerate([(['Việc nhẹ', 'lương cao'], PINK), (['Đòi đặt', 'cọc trước'], PEACH), (['Mượn', 'tài khoản'], YELLOW), (['Đe dọa,', 'giữ bí mật'], LBLUE)]):
    s += box(14 + i * 75, 44, 67, 60, lab, c, 10)
s += arrow(160, 112, 160, 130, ORANGE, 3)
s += box(50, 134, 220, 34, 'Dừng · Không chuyển tiền · Hỏi người lớn', G, 10.5)
s += t(160, 188, 'Theo cảnh báo của Bộ Công an', 9.5, GRAY, '500')
add('D9', 2, 'Dấu hiệu lừa đảo', 'Việc nhẹ lương cao, đòi tiền cọc, mượn tài khoản hay giấy tờ, đe dọa và bắt giữ bí mật là dấu hiệu lừa đảo.', s)

# ================= BÀI 10 =================
s = t(160, 22, 'Khi quá tải', 14)
s += box(14, 38, 92, 112, ['Bình thường', '', 'mệt vài ngày', 'mùa thi,', 'rồi hồi lại'], G, 10.5)
s += box(114, 38, 92, 112, ['Nên nói sớm', '', 'kéo dài', 'nhiều tuần,', 'bỏ học, mất ngủ'], YELLOW, 10.5)
s += box(214, 38, 92, 112, ['Nói ngay', '', 'muốn làm đau', 'bản thân,', 'nghĩ đến cái chết'], PINK, 10.5)
s += t(160, 176, 'Nhờ giúp sớm là một kỹ năng tự quản', 11, GREEN)
add('D10', 1, 'Khi quá tải', 'Mệt vài ngày mùa thi là bình thường. Kéo dài nhiều tuần thì nói sớm. Có ý làm đau bản thân thì nói ngay.', s)

add('D10', 2, 'Xem lại học kỳ', 'Cuối học kỳ, ghi điều nên giữ, điều nên bỏ, điều sẽ thử, rồi đặt mục tiêu kỳ tới.',
    t(160, 28, 'Xem lại học kỳ', 14)
    + flow([['Giữ', 'điều', 'hiệu quả'], ['Bỏ', 'điều', 'vô ích'], ['Thử', '1 cách', 'mới'], ['Mục tiêu', 'kỳ tới']], 56, 76, 8, 312, 10, 10.5, [G, PINK, YELLOW, LBLUE])
    + t(160, 160, 'Mỗi học kỳ, cách học của mình tốt lên một chút', 10.5, GREEN))
