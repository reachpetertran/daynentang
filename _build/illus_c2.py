# Hình minh họa và sơ đồ khóa C2 "Hiểu mình (13–17)" – tiền tố B / KHOAB
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 22, 'Tám tuần', 14)
items = [('1. Mình là ai', SAND), ('2. Điều mình coi trọng', PINK), ('3. Cảm xúc', LBLUE), ('4. Não đang lớn', YELLOW),
         ('5. Chăm cơ thể', G), ('6. Mạng và hình ảnh', PURP), ('7. Mục tiêu', PEACH), ('8. Khi cần giúp', LGRAY)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 34 + (i // 2) * 40
    s += box(x, y, 142, 32, lab, c, 11)
add('KHOAB', 1, 'Tám tuần', 'Mỗi tuần một bài 25 phút: đọc, làm, rồi nói với người tin cậy hoặc viết cho chính mình.', s)

add('KHOAB', 2, 'Quan sát – Gọi tên – Chọn – Xem lại', 'Cách học chung của khóa: quan sát mình, gọi tên điều thấy, chọn một việc nhỏ, rồi xem lại sau một tuần.',
    t(160, 28, 'Vòng hiểu mình', 14)
    + cycle([['Quan sát'], ['Gọi tên'], ['Chọn 1 việc'], ['Xem lại']], 160, 112, 58, 90, 30, 11, [LBLUE, YELLOW, G, PINK]))

# ================= BÀI 1 =================
s = t(160, 22, 'Điểm mạnh có bằng chứng', 14)
s += box(14, 40, 92, 56, ['Điểm mạnh', '"kiên nhẫn"'], YELLOW, 10.5)
s += arrow(108, 68, 128, 68, ORANGE, 3)
s += box(130, 40, 176, 56, ['Bằng chứng', 'tự sửa xe đạp 2 tiếng', 'không bỏ cuộc'], G, 10.5)
s += box(14, 112, 92, 56, ['Người khác', 'thấy gì?'], LBLUE, 10.5)
s += arrow(108, 140, 128, 140, ORANGE, 3)
s += box(130, 112, 176, 56, ['Hỏi 2 người:', '"3 từ tả mình là gì?"'], PEACH, 10.5)
s += t(160, 190, 'Điểm mạnh thấy được qua việc làm', 11, GREEN)
add('B1', 1, 'Điểm mạnh có bằng chứng', 'Mỗi điểm mạnh đi kèm một việc bạn đã làm. Hỏi thêm người khác thấy gì ở bạn.', s)

s = t(160, 22, 'Ba vòng của mình', 14)
s += f'<circle cx="120" cy="100" r="52" fill="{YELLOW}" fill-opacity=".7" stroke="{NAVY}" stroke-width="2"/>'
s += f'<circle cx="200" cy="100" r="52" fill="{LBLUE}" fill-opacity=".7" stroke="{NAVY}" stroke-width="2"/>'
s += f'<circle cx="160" cy="146" r="40" fill="{G}" fill-opacity=".8" stroke="{NAVY}" stroke-width="2"/>'
s += t(96, 86, 'Mình', 11) + t(96, 100, 'giỏi', 11) + t(224, 86, 'Mình', 11) + t(224, 100, 'thích', 11)
s += t(160, 166, 'Có ích', 10.5) + t(160, 178, 'cho người khác', 10.5)
s += t(160, 120, '★', 16, ORANGE)
add('B1', 2, 'Ba vòng của mình', 'Chỗ giao nhau giữa việc mình giỏi, mình thích và có ích cho người khác là gợi ý để thử thêm.', s)

# ================= BÀI 2 =================
add('B2', 1, 'Từ giá trị đến việc làm', 'Chọn 3 giá trị, viết vì sao, rồi chọn 1 việc làm trong tuần này.',
    t(160, 28, 'Từ giá trị đến việc làm', 14)
    + flow([['Chọn', '3 giá trị'], ['Viết', 'vì sao', 'quan trọng'], ['Chọn', '1 việc', 'tuần này'], ['Xem lại', 'sau', '7 ngày']], 56, 76, 8, 312, 10, 10.5, [PINK, YELLOW, G, LBLUE])
    + t(160, 160, 'Giá trị thấy được qua việc làm, không qua lời nói', 10.5, GREEN))

s = t(160, 22, 'Khi hai giá trị kéo hai phía', 14)
s += box(14, 44, 120, 50, ['Trung thực', 'nói thật điểm kém'], LBLUE, 10.5)
s += box(186, 44, 120, 50, ['Giữ hòa khí', 'sợ bố mẹ buồn'], PINK, 10.5)
s += arrow(136, 69, 184, 69, ORANGE, 3) + arrow(184, 75, 136, 75, ORANGE, 3)
s += box(60, 118, 200, 44, ['Cách giữ cả hai:', 'nói thật, kèm kế hoạch sửa'], G, 10.5)
s += t(160, 186, 'Không có đáp án hoàn hảo, chỉ có cách tốt hơn', 10.5, GREEN)
add('B2', 2, 'Khi hai giá trị kéo hai phía', 'Đôi khi hai điều mình coi trọng mâu thuẫn. Tìm cách giữ được phần lớn của cả hai.', s)

# ================= BÀI 3 =================
s = t(160, 22, 'Nhiệt kế cảm xúc', 14)
lv = [('5', 'Bùng nổ', PINK), ('4', 'Rất mạnh', PEACH), ('3', 'Rõ ràng', YELLOW), ('2', 'Hơi có', G), ('1', 'Bình yên', LBLUE)]
for i, (n, lab, c) in enumerate(lv):
    y = 36 + i * 28
    s += box(110, y, 100, 24, f'{n} · {lab}', c, 10.5)
s += t(260, 56, 'Mức 4–5:', 10.5, NAVY, '700') + t(260, 72, 'dừng lại,', 10.5) + t(260, 88, 'thở trước', 10.5)
s += t(60, 140, 'Mức 1–3:', 10.5, NAVY, '700') + t(60, 156, 'nói ra,', 10.5) + t(60, 172, 'giải quyết', 10.5)
s += t(160, 192, 'Gọi số giúp mình chọn việc tiếp theo', 10.5, GREEN)
add('B3', 1, 'Nhiệt kế cảm xúc', 'Chấm cảm xúc từ 1 đến 5. Mức 4–5 thì dừng và thở trước khi nói hay làm.', s)

add('B3', 2, 'Chuyện – Nghĩ – Cảm – Làm', 'Cùng một chuyện, cách mình nghĩ ảnh hưởng đến cảm xúc và việc mình làm.',
    t(160, 28, 'Chuỗi cảm xúc', 14)
    + flow([['Chuyện', 'xảy ra'], ['Mình', 'nghĩ gì?'], ['Mình', 'cảm thấy'], ['Mình', 'làm gì?']], 56, 70, 8, 312, 10, 10.5, [LGRAY, YELLOW, PINK, G])
    + t(160, 150, 'Đổi một câu nghĩ có thể đổi cả chuỗi', 11, GREEN)
    + t(160, 170, 'Ví dụ: "Bạn ấy ghét mình" → "Có thể bạn ấy đang mệt"', 10, NAVY, '500'))

s = t(160, 22, 'Cơ thể báo trước', 14)
for i, (lab, c) in enumerate([(['Tim', 'đập nhanh'], PINK), (['Mặt', 'nóng'], PEACH), (['Tay', 'nắm chặt'], YELLOW), (['Bụng', 'thắt lại'], LBLUE)]):
    s += box(14 + i * 75, 44, 67, 56, lab, c, 10.5)
s += arrow(160, 108, 160, 128, ORANGE, 3)
s += box(60, 132, 200, 36, 'Thở chậm 1 phút: hít 4 – thở ra 6', G, 10.5)
s += t(160, 190, 'Nhận ra sớm thì dễ bình tĩnh hơn', 11, GREEN)
add('B3', 3, 'Cơ thể báo trước', 'Tim nhanh, mặt nóng, tay nắm chặt là tín hiệu sớm. Thở chậm một phút trước khi nói.', s)

# ================= BÀI 4 =================
s = t(160, 22, 'Não tuổi teen', 14)
s += box(14, 40, 140, 104, ['Vùng cảm xúc', 'và phần thưởng', '', 'phản ứng nhanh,', 'mạnh ở tuổi teen'], PINK, 10.5)
s += box(166, 40, 140, 104, ['Vùng lập kế hoạch', '(trước trán)', '', 'còn hoàn thiện đến', 'khoảng 25 tuổi'], LBLUE, 10.5)
s += t(160, 168, 'Não thay đổi theo việc mình luyện tập', 11, NAVY, '600') + t(160, 186, 'Theo NIMH', 9.5, GRAY, '500')
add('B4', 1, 'Não tuổi teen', 'Vùng cảm xúc phản ứng mạnh; vùng lập kế hoạch còn phát triển đến khoảng giữa tuổi 20. Não thay đổi theo luyện tập.', s)

add('B4', 2, 'Học từ một lần chưa được', 'Không chỉ "cố hơn". Xem lại chuyện gì xảy ra, đổi cách, và hỏi người giỏi hơn.',
    t(160, 28, 'Học từ một lần chưa được', 14)
    + flow([['Chuyện', 'gì xảy ra?'], ['Cách cũ', 'thiếu gì?'], ['Thử', 'cách mới'], ['Hỏi', 'người', 'giỏi hơn']], 56, 76, 8, 312, 10, 10.5, [LGRAY, YELLOW, G, LBLUE])
    + t(160, 160, '"Cố hơn" chưa đủ, cần đổi cách', 11.5, GREEN))

# ================= BÀI 5 =================
s = t(160, 22, 'Ba nền của cơ thể', 14)
s += box(14, 44, 92, 90, ['Ngủ', '8–10 giờ', 'mỗi đêm'], PURP, 11)
s += box(114, 44, 92, 90, ['Vận động', 'khoảng 60', 'phút/ngày'], G, 11)
s += box(214, 44, 92, 90, ['Ăn đều', 'đủ bữa,', 'uống nước'], PEACH, 11)
s += t(160, 160, 'Thiếu một nền, cảm xúc và việc học đều khó hơn', 10.5, GREEN)
s += t(160, 180, 'Theo AASM 2016, WHO', 9.5, GRAY, '500')
add('B5', 1, 'Ba nền của cơ thể', 'Tuổi 13–18 cần ngủ 8–10 giờ; tuổi 5–17 nên vận động khoảng 60 phút mỗi ngày; ăn đủ bữa.', s)

add('B5', 2, 'Một giờ trước khi ngủ', 'Đặt giờ tắt máy, sạc điện thoại ngoài phòng ngủ, làm việc nhẹ rồi lên giường đúng giờ.',
    t(160, 28, 'Một giờ trước khi ngủ', 14)
    + flow([['Giờ', 'tắt máy'], ['Sạc', 'ngoài', 'phòng ngủ'], ['Việc', 'nhẹ: đọc,', 'tắm'], ['Lên', 'giường', 'đúng giờ']], 56, 76, 8, 312, 10, 10.5, [PURP, YELLOW, LBLUE, G])
    + t(160, 160, 'Sáng dậy cùng giờ, kể cả cuối tuần', 11.5, GREEN))

# ================= BÀI 6 =================
s = t(160, 22, 'Ảnh trên mạng và người thật', 14)
s += paper(30, 40, 110, 110, WHITE) + t(85, 64, 'Ảnh đăng', 11, NAVY, '700')
s += t(85, 86, 'chọn góc đẹp', 10, NAVY, '500') + t(85, 102, 'lọc màu, chỉnh', 10, NAVY, '500') + t(85, 118, '1 khoảnh khắc', 10, NAVY, '500')
s += paper(180, 40, 110, 110, G) + t(235, 64, 'Đời thật', 11, NAVY, '700')
s += t(235, 86, 'có ngày mệt', 10, NAVY, '500') + t(235, 102, 'có mụn, có lỗi', 10, NAVY, '500') + t(235, 118, 'cả 24 giờ', 10, NAVY, '500')
s += t(160, 100, '≠', 26, ORANGE, '800')
s += t(160, 180, 'Đừng so cả đời mình với ảnh đẹp nhất của người khác', 10, GREEN)
add('B6', 1, 'Ảnh trên mạng và người thật', 'Ảnh đăng lên thường đã chọn và chỉnh. So mình với ảnh đó là so không công bằng.', s)

add('B6', 2, 'Kiểm tra sau khi lướt', 'Sau mỗi lần lướt, hỏi: mình thấy tốt hơn hay tệ hơn? Bỏ theo dõi nguồn làm mình tệ hơn.',
    t(160, 28, 'Kiểm tra sau khi lướt', 14)
    + flow([['Lướt', 'xong'], ['Hỏi:', 'tốt hơn hay', 'tệ hơn?'], ['Ghi', 'nguồn', 'gây tệ'], ['Bỏ theo', 'dõi, tắt', 'thông báo']], 56, 76, 8, 312, 10, 10.5, [LBLUE, YELLOW, PINK, G])
    + t(160, 160, 'Bạn chọn được mình xem gì', 11.5, GREEN))

# ================= BÀI 7 =================
add('B7', 1, 'Mong – Tốt nhất – Trở ngại – Nếu thì', 'Nghĩ về điều mong muốn, kết quả tốt nhất, trở ngại bên trong mình, rồi viết kế hoạch Nếu… thì….',
    t(160, 28, 'Bốn bước đặt mục tiêu', 14)
    + flow([['Mong', 'muốn'], ['Kết quả', 'tốt nhất'], ['Trở ngại', 'bên trong', 'mình'], ['Nếu…', 'thì…']], 56, 76, 8, 312, 10, 10.5, [YELLOW, G, PINK, LBLUE])
    + t(160, 160, 'Nhìn thẳng vào trở ngại, rồi lập kế hoạch cho nó', 10.5, GREEN))

s = t(160, 22, 'Câu Nếu… thì…', 14)
s += box(14, 42, 292, 40, ['Nếu 20 giờ tối mà mình đang cầm điện thoại', 'thì mình để máy ngoài phòng và mở sách'], YELLOW, 10.5)
s += box(14, 92, 292, 40, ['Nếu bài khó làm mình muốn bỏ', 'thì mình làm 1 câu dễ nhất trước'], G, 10.5)
s += t(160, 160, 'Gắn việc cần làm với một tình huống cụ thể', 11, NAVY, '600') + t(160, 178, 'Theo Gollwitzer &amp; Sheeran 2006', 9.5, GRAY, '500')
add('B7', 2, 'Câu Nếu… thì…', 'Gắn việc cần làm với một tình huống cụ thể giúp dễ làm theo hơn.', s)

# ================= BÀI 8 =================
s = t(160, 22, 'Khi nào cần nhờ giúp?', 14)
s += box(14, 38, 92, 112, ['Bình thường', '', 'buồn, lo', 'vài ngày', 'rồi qua'], G, 10.5)
s += box(114, 38, 92, 112, ['Nên nói sớm', '', 'kéo dài', 'nhiều tuần,', 'bỏ ăn, mất ngủ'], YELLOW, 10.5)
s += box(214, 38, 92, 112, ['Nói ngay', '', 'muốn làm đau', 'bản thân,', 'nghĩ đến cái chết'], PINK, 10.5)
s += t(160, 176, 'Nhờ giúp là dũng cảm, không phải yếu đuối', 11, GREEN)
add('B8', 1, 'Khi nào cần nhờ giúp', 'Buồn vài ngày là bình thường. Kéo dài nhiều tuần thì nói sớm. Có ý làm đau bản thân thì nói ngay.', s)

add('B8', 2, 'Cách mở lời', 'Chọn người, chọn lúc, nói câu đầu tiên, và nói điều mình cần.',
    t(160, 28, 'Cách mở lời', 14)
    + flow([['Chọn', 'người', 'tin cậy'], ['Chọn', 'lúc riêng'], ['Câu đầu:', '"Con cần', 'nói chuyện"'], ['Nói điều', 'mình cần']], 56, 76, 8, 312, 10, 10.5, [LBLUE, YELLOW, PINK, G])
    + t(160, 160, 'Người đầu chưa hiểu? Nói với người thứ hai', 11, GREEN))
