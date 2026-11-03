# Hình minh họa và sơ đồ khóa C7 "Tự lập từng bước" – tiền tố J / KHOAJ
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười bài', 14)
items = [('1. Việc mình muốn tự làm', SAND), ('2. Chia thành bước nhỏ', PINK), ('3. Giúp vừa đủ', YELLOW), ('4. Tự chăm sóc', LBLUE),
         ('5. An toàn khi đi lại', G), ('6. Nói điều mình cần', PURP), ('7. Tiền và đi chợ', PEACH), ('8. Lịch hình ảnh', LGRAY),
         ('9. Quyền và hỗ trợ', SAND), ('10. Bước tiếp theo', PINK)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 30 + (i // 2) * 33
    s += box(x, y, 142, 27, lab, c, 10.5)
add('KHOAJ', 1, 'Mười bài', 'Mỗi bài 25 phút: đọc bản dễ đọc, làm ngay, rồi làm cùng người thân.', s)

add('KHOAJ', 2, 'Vòng tự lập', 'Bốn bước dùng trong cả khóa: chọn việc, chia bước, tập có hỗ trợ, giảm dần hỗ trợ.',
    t(160, 22, 'Vòng tự lập', 14)
    + cycle([['Chọn', '1 việc'], ['Chia', 'bước nhỏ'], ['Tập,', 'có hỗ trợ'], ['Giảm dần', 'hỗ trợ']], 160, 114, 62, 92, 34, 10.5, [YELLOW, PINK, LBLUE, G]))

# ================= BÀI 1 =================
s = t(160, 22, 'Chọn việc vừa sức', 14)
s += box(14, 42, 92, 70, ['Quan trọng', 'với mình'], YELLOW, 10.5)
s += box(114, 42, 92, 70, ['Làm hằng', 'ngày'], LBLUE, 10.5)
s += box(214, 42, 92, 70, ['Hơi khó,', 'chưa quá khó'], G, 10.5)
s += arrow(160, 116, 160, 136, ORANGE, 3)
s += box(70, 138, 180, 34, 'Mục tiêu tháng này', PEACH, 11)
add('J1', 1, 'Chọn việc vừa sức', 'Một việc tốt để tập: quan trọng với mình, làm hằng ngày, hơi khó nhưng chưa quá khó.', s)

s = t(160, 22, 'Mục tiêu đo được', 14)
s += box(14, 42, 292, 34, 'Chưa rõ: "Mình muốn tự lập hơn."', LGRAY, 10.5)
s += arrow(160, 80, 160, 96, ORANGE, 3)
s += box(14, 98, 292, 52, ['Rõ: "Sau 4 tuần, mình tự pha mì', 'gói, chỉ cần nhắc 1 lần."'], G, 10.5)
s += t(160, 180, 'Ai, làm gì, tới khi nào, giúp bao nhiêu', 10.5, GREEN)
add('J1', 2, 'Mục tiêu đo được', 'Viết mục tiêu sao cho cả mình và người thân đều biết lúc nào đã đạt.', s)

# ================= BÀI 2 =================
add('J2', 1, 'Chia việc thành bước nhỏ', 'Ví dụ rửa tay chia thành 5 bước. Mỗi bước là một việc nhìn thấy được.',
    t(160, 26, 'Rửa tay: 5 bước', 14)
    + flow([['Mở', 'nước'], ['Xoa', 'xà phòng'], ['Chà', 'tay'], ['Xả', 'sạch'], ['Lau', 'khô']], 58, 64, 8, 312, 6, 10, [LBLUE, YELLOW, PINK, LBLUE, G])
    + t(160, 160, 'Mỗi bước: một động từ, một việc', 10.5, GREEN))

s = t(160, 22, 'Tập từ bước cuối', 14)
for i, (lab, c) in enumerate([(['Người thân', 'làm bước 1–4'], LGRAY), (['Mình làm', 'bước 5'], G)]):
    s += box(30 + i * 140, 46, 120, 56, lab, c, 10.5)
s += arrow(152, 74, 168, 74, ORANGE, 3)
s += box(30, 120, 260, 40, 'Rồi mình làm bước 4–5, rồi 3–5…', YELLOW, 10.5)
s += t(160, 186, 'Lần nào cũng kết thúc bằng "mình làm xong"', 10.5, GREEN)
add('J2', 2, 'Tập từ bước cuối', 'Một cách tập: người thân làm các bước đầu, mình làm bước cuối, rồi lùi dần lên. Lần nào cũng tự hoàn thành.', s)

# ================= BÀI 3 =================
s = t(160, 20, 'Thang hỗ trợ', 14)
lv = [('Cầm tay làm cùng', PINK), ('Làm mẫu cho xem', PEACH), ('Chỉ tay, đưa hình', YELLOW), ('Nhắc bằng lời', LBLUE), ('Tự làm', G)]
for i, (lab, c) in enumerate(lv):
    s += box(20 + i * 26, 160 - i * 30, 180, 26, lab, c, 10.5)
s += arrow(250, 160, 290, 40, ORANGE, 3)
s += t(272, 186, 'Giảm dần', 10.5, GREEN)
add('J3', 1, 'Thang hỗ trợ', 'Năm mức giúp, từ nhiều tới ít. Chọn mức ít nhất mà mình vẫn làm được, rồi lùi dần.', s)

add('J3', 2, 'Chờ trước khi giúp', 'Người thân đợi vài giây trước khi nhắc. Khoảng chờ cho mình cơ hội tự làm.',
    t(160, 28, 'Đợi – Nhắc – Giúp', 14)
    + flow([['Đợi', 'vài giây'], ['Nhắc', 'nhẹ'], ['Giúp', 'vừa đủ']], 60, 64, 14, 306, 14, 11, [G, YELLOW, PINK])
    + t(160, 160, 'Giúp ít nhất có thể, khen việc mình tự làm', 10.5, GREEN))

# ================= BÀI 4 =================
s = t(160, 22, 'Tự chăm sóc mỗi ngày', 14)
for i, (lab, c) in enumerate([('Ăn, uống', YELLOW), ('Mặc đồ', LBLUE), ('Vệ sinh', G), ('Tắm', PEACH), ('Uống thuốc', PURP), ('Ngủ', LGRAY)]):
    x = 14 + (i % 3) * 100; y = 44 + (i // 3) * 64
    s += box(x, y, 92, 52, lab, c, 11)
s += t(160, 186, 'Chọn 1 việc, chia bước, tập 4 tuần', 10.5, GREEN)
add('J4', 1, 'Tự chăm sóc mỗi ngày', 'Sáu nhóm việc tự chăm sóc. Mỗi lần chỉ tập một việc.', s)

s = t(160, 22, 'Đồ hỗ trợ tự làm', 14)
s += box(14, 42, 140, 50, ['Thìa cán to,', 'cốc có quai'], YELLOW, 10.5)
s += box(166, 42, 140, 50, ['Áo cài dán,', 'quần lưng thun'], LBLUE, 10.5)
s += box(14, 102, 140, 50, ['Ghế tắm,', 'tay vịn'], G, 10.5)
s += box(166, 102, 140, 50, ['Hộp thuốc', 'chia ngày'], PEACH, 10.5)
s += t(160, 182, 'Đổi đồ vật dễ hơn đổi con người', 10.5, GREEN)
add('J4', 2, 'Đồ hỗ trợ tự làm', 'Một số đồ đơn giản giúp tự làm dễ hơn. Hỏi chuyên viên phục hồi chức năng trước khi mua.', s)

# ================= BÀI 5 =================
s = t(160, 22, 'Nhà ít nguy cơ té ngã', 14)
for i, (lab, c) in enumerate([(['Lối đi', 'thông thoáng'], G), (['Đủ sáng,', 'nhất là ban đêm'], YELLOW), (['Chống trơn', 'nhà tắm'], LBLUE), (['Tay vịn', 'chỗ cần'], PEACH)]):
    x = 14 + (i % 2) * 150; y = 40 + (i // 2) * 66
    s += box(x, y, 142, 56, lab, c, 10.5)
s += t(160, 186, 'Rà soát nhà 1 lần, sửa 1 chỗ mỗi tuần', 10.5, GREEN)
add('J5', 1, 'Nhà ít nguy cơ té ngã', 'Bốn chỗ cần xem trong nhà: lối đi, ánh sáng, nhà tắm, tay vịn.', s)

add('J5', 2, 'Đi một mình: Trước – Trong – Sau', 'Trước khi đi báo nơi đến; trong lúc đi giữ thẻ thông tin; tới nơi nhắn "đã tới".',
    t(160, 28, 'Đi một mình', 14)
    + flow([['Trước', 'báo nơi đến,', 'giờ về'], ['Trong', 'mang thẻ', 'thông tin'], ['Sau', 'nhắn', '"đã tới"']], 52, 80, 14, 306, 14, 10.5, [YELLOW, LBLUE, G])
    + t(160, 170, 'Tập đường ngắn có người đi cùng trước', 10.5, GREEN))

# ================= BÀI 6 =================
add('J6', 1, 'Nói điều mình cần', 'Ba phần: mình cần gì, vì sao, giúp thế nào. Dùng lời, chữ viết, hình hoặc cử chỉ.',
    t(160, 28, 'Câu nhờ giúp', 14)
    + flow([['Mình cần…', '(việc gì)'], ['Vì…', '(lý do)'], ['Bạn giúp', 'bằng cách…']], 56, 70, 14, 306, 14, 10.5, [LBLUE, YELLOW, G])
    + box(40, 144, 240, 34, 'Nói, viết, chỉ hình đều được', PEACH, 10.5))

s = t(160, 22, 'Chạm đúng, chạm sai', 14)
s += box(14, 42, 140, 108, ['Được hỏi trước', '', 'Giúp đúng việc', 'mình nhờ', '', 'Dừng khi mình nói dừng'], G, 10.5)
s += box(166, 42, 140, 108, ['Không hỏi', '', 'Giữ tiền, giấy tờ', 'của mình', '', 'Bắt giữ bí mật'], PINK, 10.5)
s += t(160, 182, 'Thấy sai: nói không, kể với người tin cậy', 10.5, GREEN)
add('J6', 2, 'Chạm đúng, chạm sai', 'Người giúp tốt hỏi trước và dừng khi mình nói dừng. Dấu hiệu sai thì kể ngay với người tin cậy.', s)

# ================= BÀI 7 =================
s = t(160, 22, 'Đi chợ có danh sách', 14)
s += paper(30, 40, 110, 130)
for i in range(4):
    s += f'<rect x="42" y="{58 + i * 26}" width="12" height="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
    s += f'<line x1="62" y1="{64 + i * 26}" x2="128" y2="{64 + i * 26}" stroke="{GRAY}" stroke-width="3"/>'
s += box(170, 50, 130, 46, ['Đếm tiền', 'trước khi đi'], YELLOW, 10.5)
s += box(170, 110, 130, 46, ['Kiểm tiền thừa', 'trước khi rời'], G, 10.5)
add('J7', 1, 'Đi chợ có danh sách', 'Danh sách có hình hoặc chữ, đếm tiền trước khi đi, kiểm tiền thừa trước khi rời quầy.', s)

s = t(160, 22, 'Giữ tiền an toàn', 14)
s += box(14, 42, 292, 30, 'Mã PIN, mã OTP: chỉ mình biết', PINK, 10.5)
s += box(14, 82, 292, 30, 'Ai đòi giữ thẻ, giữ tiền: hỏi người tin cậy', YELLOW, 10.5)
s += box(14, 122, 292, 30, 'Ghi tiền vào, tiền ra mỗi tuần', G, 10.5)
s += t(160, 182, 'Tiền của mình, mình quyết định', 10.5, GREEN)
add('J7', 2, 'Giữ tiền an toàn', 'Ba thói quen giữ tiền: giữ kín mã, hỏi người tin cậy khi bị đòi giữ tiền, ghi thu chi mỗi tuần.', s)

# ================= BÀI 8 =================
s = t(160, 20, 'Lịch hình ảnh buổi sáng', 14)
icons = ['Dậy', 'Vệ sinh', 'Mặc đồ', 'Ăn', 'Thuốc']
for i, lab in enumerate(icons):
    x = 16 + i * 60
    s += box(x, 44, 52, 52, lab, [YELLOW, LBLUE, PEACH, G, PURP][i], 10)
    s += f'<rect x="{x + 18}" y="108" width="16" height="16" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
    if i < 2: s += check(x + 26, 116)
s += t(160, 160, 'Xong việc nào, đánh dấu việc đó', 10.5, GREEN)
add('J8', 1, 'Lịch hình ảnh', 'Mỗi việc một ô có hình hoặc chữ. Làm xong thì đánh dấu, nhìn là biết việc tiếp theo.', s)

add('J8', 2, 'Gắn việc mới vào việc cũ', 'Thói quen mới dễ giữ hơn khi gắn sau một việc đã quen làm hằng ngày.',
    t(160, 28, 'Sau khi… thì mình…', 14)
    + flow([['Việc đã quen', '(đánh răng)'], ['Việc mới', '(uống thuốc)'], ['Đánh dấu', 'trên lịch']], 56, 70, 14, 306, 14, 10.5, [LGRAY, YELLOW, G])
    + t(160, 160, 'Cùng giờ, cùng chỗ mỗi ngày', 10.5, GREEN))

# ================= BÀI 9 =================
s = t(160, 22, 'Quyền của mình', 14)
for i, (lab, c) in enumerate([(['Sống độc lập,', 'hòa nhập'], G), (['Không bị', 'phân biệt'], YELLOW), (['Dùng dịch vụ', 'y tế, học, làm'], LBLUE), (['Tài sản, giấy', 'tờ của mình'], PEACH)]):
    x = 14 + (i % 2) * 150; y = 40 + (i // 2) * 66
    s += box(x, y, 142, 56, lab, c, 10.5)
s += t(160, 186, 'Luật Người khuyết tật 2010, Điều 4 và 14', 10.5, GREEN)
add('J9', 1, 'Quyền của mình', 'Một số quyền trong Luật Người khuyết tật 2010. Đây là thông tin chung, không phải tư vấn pháp lý.', s)

add('J9', 2, 'Hỏi hỗ trợ ở đâu', 'Bắt đầu từ Ủy ban nhân dân xã, phường nơi mình ở; mang giấy tờ; ghi tên người tiếp và ngày hẹn.',
    t(160, 28, 'Hỏi hỗ trợ', 14)
    + flow([['UBND xã,', 'phường'], ['Xác định', 'mức độ', 'khuyết tật'], ['Hỏi', 'chính sách', 'phù hợp']], 52, 80, 14, 306, 14, 10.5, [LBLUE, YELLOW, G])
    + t(160, 170, 'Ghi tên người tiếp, ngày hẹn', 10.5, GREEN))

# ================= BÀI 10 =================
s = t(160, 22, 'Nhìn lại 10 tuần', 14)
s += box(14, 42, 92, 92, ['Trước:', 'giúp', 'nhiều'], LGRAY, 10.5)
s += arrow(108, 88, 124, 88, ORANGE, 3)
s += box(126, 42, 92, 92, ['Bây giờ:', 'giúp', 'ít hơn'], YELLOW, 10.5)
s += arrow(220, 88, 236, 88, ORANGE, 3)
s += box(238, 42, 70, 92, ['Việc', 'tiếp', 'theo'], G, 10.5)
s += t(160, 168, 'So với chính mình, không so với người khác', 10.5, GREEN)
add('J10', 1, 'Nhìn lại 10 tuần', 'So mức hỗ trợ trước và sau khóa. Tiến bộ là so với chính mình.', s)

add('J10', 2, 'Vòng tiếp theo', 'Khi một việc đã tự làm được, chọn việc tiếp theo và lặp lại vòng tự lập.',
    t(160, 22, 'Vòng tiếp theo', 14)
    + cycle([['Việc 1', 'tự làm ✓'], ['Chọn', 'việc 2'], ['Chia', 'bước'], ['Tập,', 'giảm giúp']], 160, 114, 62, 92, 34, 10.5, [G, YELLOW, PINK, LBLUE]))

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('J', 'KHOAJ'))), 'hình C7')
