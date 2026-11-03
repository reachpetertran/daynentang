# Hình minh họa và sơ đồ khóa C8 "Chăm tâm trí cơ bản" – tiền tố P / KHOAP
# Không vẽ cách tự hại; chỉ vẽ kỹ năng, quy trình và nơi tìm giúp.
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười bài', 14)
items = [('1. Tâm trí cũng cần chăm', SAND), ('2. Gọi tên, thở chậm', PINK), ('3. Neo lại', YELLOW), ('4. Việc nhỏ có ý nghĩa', LBLUE),
         ('5. Giấc ngủ', G), ('6. Lo lắng vòng vo', PURP), ('7. Giải quyết vấn đề', PEACH), ('8. Kết nối', LGRAY),
         ('9. Rượu bia, màn hình', SAND), ('10. Kế hoạch giữ vững', PINK)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 30 + (i // 2) * 33
    s += box(x, y, 142, 27, lab, c, 10.5)
add('KHOAP', 1, 'Mười bài', 'Mỗi bài 25 phút: đọc 10 phút, làm 10 phút, ghi lại 5 phút.', s)

s = t(160, 22, 'Ba tầng chăm tâm trí', 14)
s += box(20, 40, 280, 40, ['Tự chăm mỗi ngày: ngủ, vận động,', 'kết nối, việc nhỏ có ý nghĩa'], G, 10.5)
s += box(40, 88, 240, 40, ['Nói với người tin cậy,', 'gặp nhân viên y tế'], YELLOW, 10.5)
s += box(60, 136, 200, 40, ['Nguy hiểm ngay:', 'gọi 115, tới cấp cứu'], PINK, 10.5)
s += t(160, 192, 'Khóa này dạy tầng 1 và chỉ đường tới tầng 2, 3', 10, GREEN)
add('KHOAP', 2, 'Ba tầng chăm tâm trí', 'Tự chăm mỗi ngày là tầng đầu. Khi không đủ, tìm người giúp. Khi nguy hiểm, gọi cấp cứu ngay.', s)

# ================= BÀI 1 =================
s = t(160, 22, 'Nhiệt kế tâm trí', 14)
for i in range(11):
    c = PINK if i < 4 else (YELLOW if i < 7 else G)
    s += f'<rect x="{18 + i * 26}" y="60" width="22" height="34" rx="5" fill="{c}" stroke="{NAVY}" stroke-width="2"/>' + t(29 + i * 26, 82, str(i), 11)
s += t(40, 116, 'Rất tệ', 10.5) + t(280, 116, 'Rất ổn', 10.5)
s += t(160, 150, 'Mỗi tối chấm 1 số cho: tâm trạng,', 10.5, GREEN) + t(160, 168, 'giấc ngủ, sức lực, kết nối', 10.5, GREEN)
add('P1', 1, 'Nhiệt kế tâm trí', 'Chấm từ 0 đến 10 mỗi tối cho bốn mục. Đây là cách tự theo dõi, không phải chẩn đoán.', s)

s = t(160, 22, 'Buồn bình thường hay cần đi khám?', 13)
s += box(14, 40, 140, 96, ['Buồn vài ngày,', 'vẫn ăn, ngủ,', 'vẫn làm việc', 'được'], G, 10.5)
s += box(166, 40, 140, 96, ['Buồn, mất hứng thú', 'gần như cả ngày,', 'hầu hết các ngày,', 'từ 2 tuần trở lên'], PINK, 10.5)
s += t(84, 158, 'Tự chăm, theo dõi', 10.5, GREEN) + t(236, 158, 'Gặp nhân viên y tế', 10.5, RED)
s += t(160, 186, 'Có ý nghĩ về cái chết: nói ngay với người tin cậy', 10, NAVY)
add('P1', 2, 'Khi nào cần đi khám', 'Buồn vài ngày là bình thường. Buồn, mất hứng thú gần như mỗi ngày từ hai tuần trở lên thì nên gặp nhân viên y tế.', s)

# ================= BÀI 2 =================
s = t(160, 22, 'Gọi tên cảm xúc', 14)
for i, (m, lab) in enumerate([('vui', 'Vui'), ('buon', 'Buồn'), ('gian', 'Giận'), ('so', 'Lo, sợ')]):
    cx = 46 + i * 76
    s += face(cx, 74, 24, m) + t(cx, 120, lab, 11)
s += box(30, 140, 260, 40, ['"Mình đang thấy… vì…"', 'Gọi tên giúp cảm xúc dịu hơn'], YELLOW, 10.5)
add('P2', 1, 'Gọi tên cảm xúc', 'Nói thầm một câu: "Mình đang thấy… vì…". Gọi đúng tên là bước đầu để biết mình cần gì.', s)

add('P2', 2, 'Thở chậm 1 phút', 'Hít vào bằng mũi khoảng 4 nhịp, thở ra chậm hơn khoảng 6 nhịp. Làm 5–6 lần.',
    t(160, 26, 'Thở chậm 1 phút', 14)
    + flow([['Ngồi', 'thả vai'], ['Hít vào', '~4 nhịp'], ['Thở ra', '~6 nhịp'], ['Lặp lại', '5–6 lần']], 56, 66, 10, 310, 10, 10.5, [LGRAY, LBLUE, G, YELLOW])
    + t(160, 160, 'Thở ra dài hơn hít vào', 10.5, GREEN)
    + t(160, 180, 'Chóng mặt thì dừng, thở bình thường', 10, NAVY))

# ================= BÀI 3 =================
add('P3', 1, 'Neo lại: Chậm – Để ý – Quay về', 'Khi cảm xúc dâng cao: chậm lại, để ý cơ thể và xung quanh, rồi quay về việc mình đang làm.',
    t(160, 26, 'Neo lại khi cảm xúc dâng cao', 13)
    + flow([['Chậm lại', 'ấn chân', 'xuống sàn'], ['Để ý', 'cơ thể và', 'xung quanh'], ['Quay về', 'việc đang', 'làm']], 56, 80, 12, 308, 14, 10.5, [LBLUE, YELLOW, G])
    + t(160, 168, 'Phỏng theo ý "neo lại" trong tài liệu tự giúp của WHO', 9.5, GRAY))

s = t(160, 22, 'Gọi tên 5 – 4 – 3 – 2 – 1', 14)
rows = [('5', 'thứ mình nhìn thấy', LBLUE), ('4', 'thứ mình chạm được', G), ('3', 'tiếng mình nghe', YELLOW), ('2', 'mùi mình ngửi', PEACH), ('1', 'hơi thở chậm', PINK)]
for i, (n, lab, c) in enumerate(rows):
    s += num(70, 46 + i * 30, n, ORANGE) + box(88, 34 + i * 30, 170, 24, lab, c, 10.5)
add('P3', 2, 'Gọi tên 5 – 4 – 3 – 2 – 1', 'Một cách neo lại bằng giác quan: gọi tên những gì mình thấy, chạm, nghe, ngửi, rồi thở chậm.', s)

# ================= BÀI 4 =================
add('P4', 1, 'Vòng buồn và vòng làm', 'Buồn làm mình bỏ việc; bỏ việc làm mình buồn hơn. Một việc nhỏ có ý nghĩa giúp bẻ vòng này.',
    t(160, 22, 'Bẻ vòng bằng một việc nhỏ', 13)
    + cycle([['Buồn,', 'mệt'], ['Bỏ việc,', 'nằm một chỗ'], ['Ít điều', 'vui, có ích'], ['Buồn', 'hơn']], 112, 112, 58, 80, 32, 9.5, [LBLUE, LGRAY, LGRAY, LBLUE])
    + arrow(214, 112, 234, 112, ORANGE, 3)
    + box(236, 82, 76, 60, ['1 việc', 'nhỏ,', '10 phút'], G, 10.5))

s = t(160, 22, 'Bốn loại việc nhỏ', 14)
for i, (lab, c) in enumerate([(['Chăm thân', 'tắm, đi bộ'], G), (['Có ích', 'dọn 1 góc'], YELLOW), (['Kết nối', 'nhắn 1 người'], LBLUE), (['Vui nhỏ', 'nghe 1 bài hát'], PEACH)]):
    s += box(14 + (i % 2) * 150, 38 + (i // 2) * 62, 142, 54, lab, c, 10.5)
s += t(160, 182, 'Làm trước, hứng thú thường đến sau', 10.5, GREEN)
add('P4', 2, 'Bốn loại việc nhỏ', 'Chọn mỗi ngày một việc nhỏ: chăm thân, có ích, kết nối, hoặc vui nhỏ. Làm theo kế hoạch, không chờ có hứng.', s)

# ================= BÀI 5 =================
add('P5', 1, 'Giường để ngủ', 'Chỉ lên giường khi buồn ngủ. Nằm mãi không ngủ được thì dậy làm việc nhẹ, buồn ngủ lại mới quay về.',
    t(160, 22, 'Giường là để ngủ', 14)
    + box(14, 40, 92, 54, ['Buồn ngủ', 'mới lên', 'giường'], LBLUE, 10)
    + arrow(108, 67, 122, 67, ORANGE, 3)
    + box(124, 40, 92, 54, ['Nằm lâu', 'không ngủ', 'được'], LGRAY, 10)
    + arrow(218, 67, 232, 67, ORANGE, 3)
    + box(234, 40, 76, 54, ['Dậy, làm', 'việc nhẹ,', 'ánh sáng dịu'], YELLOW, 9.5)
    + arrow(272, 98, 272, 120, ORANGE, 3)
    + box(134, 124, 176, 34, 'Buồn ngủ lại thì quay về', G, 10.5)
    + t(160, 184, 'Giờ dậy cố định, kể cả cuối tuần', 10.5, GREEN))

s = t(160, 22, 'Một ngày giúp giấc ngủ', 14)
for i, (lab, c) in enumerate([(['Sáng', 'dậy đúng giờ,', 'ra ánh sáng'], YELLOW), (['Chiều', 'vận động,', 'tránh cà phê'], G), (['Tối', 'tắt màn hình', 'trước khi ngủ'], LBLUE), (['Đêm', 'phòng tối,', 'yên, mát'], PURP)]):
    s += box(10 + i * 76, 44, 70, 92, lab, c, 10)
s += t(160, 168, 'Người lớn: ngủ từ 7 giờ mỗi đêm', 10.5, GREEN) + t(160, 186, 'Tuổi 15–17: 8–10 giờ', 10.5, GREEN)
add('P5', 2, 'Một ngày giúp giấc ngủ', 'Giấc ngủ bắt đầu từ buổi sáng: dậy đúng giờ, ra ánh sáng, vận động, tối bớt màn hình, phòng tối và mát.', s)

# ================= BÀI 6 =================
add('P6', 1, 'Lo được hay không?', 'Khi lo: hỏi việc này mình làm được gì không. Làm được thì lên kế hoạch; không làm được thì neo lại và để ý nghĩ trôi qua.',
    t(160, 22, 'Lo được hay không?', 14)
    + box(100, 34, 120, 34, 'Mình đang lo…', LGRAY, 11)
    + arrow(130, 70, 70, 94, ORANGE, 3) + arrow(190, 70, 250, 94, ORANGE, 3)
    + box(10, 96, 140, 52, ['Làm được gì đó', '→ lên kế hoạch', '(bài 7)'], G, 10.5)
    + box(170, 96, 140, 52, ['Không làm được', '→ neo lại, để ý', 'nghĩ trôi qua'], LBLUE, 10.5)
    + t(160, 178, 'Hỏi: "Việc này mình làm được gì không?"', 10.5, GREEN))

s = t(160, 22, 'Giờ lo 15 phút', 14)
s += box(14, 40, 140, 64, ['Ngoài giờ lo:', 'ghi ý lo vào giấy,', 'để dành'], LBLUE, 10.5)
s += arrow(156, 72, 170, 72, ORANGE, 3)
s += box(172, 40, 134, 64, ['Giờ lo (15 phút,', 'không sát giờ ngủ):', 'đọc lại, xử lý'], YELLOW, 10.5)
s += box(40, 122, 240, 40, ['Nhiều ý lo đã nhẹ đi', 'khi tới giờ đọc lại'], G, 10.5)
s += t(160, 186, 'Để dành, không phải cấm nghĩ', 10.5, GREEN)
add('P6', 2, 'Giờ lo 15 phút', 'Ghi ý lo ra giấy để dành tới một khung giờ cố định trong ngày, rồi mới đọc lại và xử lý.', s)

# ================= BÀI 7 =================
add('P7', 1, 'Giải quyết vấn đề 5 bước', 'Chọn một vấn đề nhỏ, nghĩ nhiều cách, chọn một cách, chia bước làm, rồi xem lại kết quả.',
    t(160, 26, 'Giải quyết vấn đề 5 bước', 14)
    + flow([['Chọn', '1 vấn đề', 'nhỏ'], ['Nghĩ', 'nhiều', 'cách'], ['Chọn', '1 cách'], ['Chia', 'bước,', 'làm'], ['Xem', 'lại']], 54, 76, 8, 312, 6, 9.5, [LGRAY, YELLOW, LBLUE, G, PEACH])
    + t(160, 162, 'Không chê ý nào ở bước 2', 10.5, GREEN))

s = t(160, 22, 'Tách vấn đề to', 14)
s += box(110, 36, 100, 34, 'Nợ, việc, nhà', PINK, 11)
for i, lab in enumerate(['Phần mình lo được', 'Phần cần người giúp', 'Phần để sau']):
    s += arrow(160, 72, 54 + i * 106, 100, ORANGE, 2.5)
    s += box(6 + i * 106, 102, 96, 46, lab.split(' ', 1), [G, YELLOW, LGRAY][i], 10)
s += t(160, 180, 'Làm phần nhỏ nhất trước', 10.5, GREEN)
add('P7', 2, 'Tách vấn đề to', 'Vấn đề to thì tách ra: phần mình tự lo được, phần cần người giúp, và phần để sau.', s)

# ================= BÀI 8 =================
s = t(160, 22, 'Vòng người mình có thể nhờ', 14)
for r, c in [(70, LGRAY), (50, LBLUE), (28, G)]:
    s += f'<circle cx="160" cy="104" r="{r}" fill="{c}" stroke="{NAVY}" stroke-width="2"/>'
s += t(160, 108, 'Mình', 11) + t(160, 68, 'Người rất tin', 9.5) + t(160, 46, 'Người quen tốt', 9.5)
s += t(160, 192, 'Ngoài vòng: nơi giúp chuyên môn', 10, GREEN)
add('P8', 1, 'Vòng người mình có thể nhờ', 'Vẽ ba vòng: người rất tin, người quen tốt, và nơi giúp chuyên môn. Ai cũng cần ít nhất vài người.', s)

add('P8', 2, 'Mở lời', 'Câu mở lời ngắn: "Dạo này mình không ổn. Bạn nghe mình 10 phút được không?"',
    t(160, 24, 'Mở lời', 14)
    + person(60, 176, 0.85, LBLUE) + person(262, 176, 0.85, G)
    + bubble(84, 36, 172, 52, '', 10.5)
    + t(170, 58, '"Mình không ổn,', 10.5) + t(170, 76, 'nghe mình 10 phút nhé?"', 10.5)
    + t(160, 190, 'Nói một câu là đủ để bắt đầu', 10.5, GREEN))

# ================= BÀI 9 =================
add('P9', 1, 'Dịu ngắn, nặng dài', 'Rượu bia, thuốc lá, lướt mạng có thể làm dịu trong chốc lát, nhưng hay làm giấc ngủ và tâm trạng tệ hơn về sau.',
    t(160, 22, 'Dịu ngắn, nặng dài', 14)
    + box(14, 44, 130, 50, ['Uống, lướt mạng', 'cho quên'], LGRAY, 10.5)
    + arrow(146, 69, 172, 69, ORANGE, 3)
    + box(176, 44, 130, 50, ['Dịu', 'trong chốc lát'], YELLOW, 10.5)
    + arrow(240, 98, 240, 118, ORANGE, 3)
    + box(100, 120, 206, 46, ['Ngủ kém, buồn hơn,', 'vấn đề vẫn còn'], PINK, 10.5)
    + t(160, 188, 'Đổi sang một cách dịu khác ở bài 2–4', 10, GREEN))

s = t(160, 22, 'Đổi một thói quen', 14)
s += box(14, 42, 292, 36, '"Nếu… (lúc buồn, lúc 10 giờ tối)"', LBLUE, 10.5)
s += arrow(160, 80, 160, 96, ORANGE, 3)
s += box(14, 98, 292, 36, '"thì… (thở chậm, gọi một người, đi bộ)"', G, 10.5)
s += t(160, 166, 'Giảm dần, có người cùng theo dõi', 10.5, GREEN)
add('P9', 2, 'Đổi một thói quen', 'Viết một câu "Nếu… thì…": khi điều gì xảy ra, mình sẽ làm việc gì thay cho thói quen cũ.', s)

# ================= BÀI 10 =================
s = t(160, 18, 'Kế hoạch giữ vững: 6 bước', 13)
steps = [('Dấu hiệu báo trước của mình', LGRAY), ('Việc tự làm để dịu xuống', G), ('Người, nơi giúp mình đổi không khí', LBLUE),
         ('Người mình nói thật được', YELLOW), ('Nơi giúp: 115, cấp cứu, đường dây', PINK), ('Làm chỗ ở an toàn hơn', PEACH)]
for i, (lab, c) in enumerate(steps):
    s += num(30, 40 + i * 27, i + 1) + box(46, 29 + i * 27, 262, 22, lab, c, 10)
add('P10', 1, 'Kế hoạch giữ vững', 'Sáu bước viết sẵn khi đang bình tĩnh, để dùng lúc khó khăn: từ việc tự làm tới gọi người và gọi cấp cứu.', s)

s = t(160, 22, 'Làm từ trên xuống', 14)
s += box(30, 38, 260, 30, 'Thử bước 2. Chưa đỡ?', G, 10.5)
s += arrow(160, 70, 160, 82, ORANGE, 3)
s += box(30, 84, 260, 30, 'Gọi người ở bước 3, 4. Chưa đỡ?', YELLOW, 10.5)
s += arrow(160, 116, 160, 128, ORANGE, 3)
s += box(30, 130, 260, 30, 'Gọi 115 hoặc tới cấp cứu', PINK, 10.5)
s += t(160, 184, 'Nguy hiểm ngay thì gọi 115 luôn', 10.5, RED)
add('P10', 2, 'Làm từ trên xuống', 'Dùng kế hoạch theo thứ tự. Nếu thấy nguy hiểm ngay, bỏ qua các bước và gọi 115 hoặc tới cấp cứu.', s)

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('P', 'KHOAP'))), 'hình C8')
