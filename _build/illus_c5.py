# Hình minh họa và sơ đồ khóa C5 "15 phút mỗi ngày" – tiền tố F / KHOAF
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'
C4 = [PINK, YELLOW, LBLUE, G]

def head(s, size=14): return t(160, 24, s, size)
def foot(s): return t(160, 188, s, 10.5, GREEN)

def steps(code, n, title, cap, heading, items, footer, size=10.5, fills=None):
    add(code, n, title, cap, head(heading) + flow(items, 64, 72, 10, 310, 10, size, fills or C4) + foot(footer))

def grid(code, n, title, cap, heading, items, footer, cols=2, size=10.5):
    s = head(heading); rows = (len(items) + cols - 1) // cols
    w = (300 - (cols - 1) * 10) / cols; h = min(34, (140 - (rows - 1) * 8) / rows)
    for i, (lab, c) in enumerate(items):
        x = 10 + (i % cols) * (w + 10); y = 38 + (i // cols) * (h + 8)
        s += box(x, y, w, h, lab, c, size)
    add(code, n, title, cap, s + foot(footer))

def compare(code, n, title, cap, heading, left, right, footer, lc=LGRAY, rc=G):
    s = head(heading) + box(12, 44, 132, 104, left, lc, 10.5) + arrow(148, 96, 172, 96, ORANGE, 3) + box(176, 44, 132, 104, right, rc, 10.5)
    add(code, n, title, cap, s + foot(footer))

def cyc(code, n, title, cap, heading, items, footer, fills=None):
    add(code, n, title, cap, head(heading) + cycle(items, 160, 104, 54, 96, 32, 10, fills or C4) + foot(footer))

# ================= TRANG KHÓA =================
s = head('Bốn tuần, mỗi ngày 15 phút')
weeks = [('Tuần 1', ['Chăm', 'thân'], PINK), ('Tuần 2', ['An toàn,', 'học nghề'], YELLOW), ('Tuần 3', ['Tiền và', 'chữ tín'], LBLUE), ('Tuần 4', ['Tâm trí,', 'gia đình'], G)]
for i, (a, b, c) in enumerate(weeks):
    s += box(10 + i * 76, 44, 70, 92, [a, ''] + b, c, 10)
s += foot('Thứ Hai đến thứ Sáu, mỗi ngày 1 bài')
add('KHOAF', 1, 'Bốn tuần', 'Bốn tuần, mỗi tuần 5 bài: chăm thân, an toàn và học nghề, tiền và chữ tín, tâm trí và gia đình.', s)
add('KHOAF', 2, 'Một bài 15 phút', 'Mỗi bài 15 phút: đọc 5 phút, làm 7 phút, ghi lại 3 phút.',
    head('Một bài 15 phút') + flow([['Đọc', '5 phút'], ['Làm', '7 phút'], ['Ghi lại', '3 phút']], 60, 70, 20, 300, 18, 12, [LBLUE, YELLOW, G])
    + foot('Ngắn, đều, làm được giữa hai ca'))

# ================= TUẦN 1 =================
steps('F1', 1, 'Nếu… thì…', 'Gắn 15 phút vào một việc có sẵn: nếu xong việc đó, thì làm việc mới ngay tại chỗ đó.',
      'Kế hoạch Nếu… thì…', [['Nếu', 'tắm xong', 'sau ca'], ['thì', 'ngồi bàn', '15 phút'], ['Đánh', 'dấu ✓', 'vào sổ']], 'Chọn giờ và chỗ cố định', 11)
compare('F1', 2, 'Ý định và kế hoạch', 'Ý định chung chung dễ quên. Kế hoạch có giờ, có chỗ, có việc cụ thể dễ làm hơn.',
        'Ý định khác kế hoạch', ['"Mình sẽ', 'cố gắng', 'tự học"'], ['"21 giờ, sau', 'khi tắm, ngồi', 'bàn 15 phút', 'đọc 1 bài"'], 'Càng cụ thể, càng dễ làm')

s = head('Ngủ sau ca đêm')
for i, (lab, c) in enumerate([('Tối', LGRAY), ('Yên', LBLUE), ('Mát', G)]):
    s += box(20 + i * 98, 44, 84, 40, lab, c, 13)
s += box(20, 98, 280, 40, ['Không ăn nặng, không rượu bia trước ngủ;', 'ngưng cà phê vài giờ trước'], YELLOW, 10)
add('F2', 1, 'Chỗ ngủ sau ca đêm', 'Ngủ ban ngày cần chỗ tối, yên, mát; tránh ăn nặng, rượu bia và cà phê sát giờ ngủ.', s + foot('Người lớn cần ít nhất 7 giờ'))
s = head('Một ngày làm ca đêm')
bar = [('Ca', 0, 120, NAVY), ('Về, tắm', 120, 30, PEACH), ('Ngủ ≥ 7 giờ', 150, 120, LBLUE), ('Việc nhà', 270, 30, G)]
for lab, x, w, c in bar:
    s += f'<rect x="{10 + x}" y="60" width="{w}" height="40" fill="{c}" stroke="{NAVY}" stroke-width="2"/>'
    s += t(10 + x + w / 2, 85, lab, 9.5, WHITE if c == NAVY else NAVY)
s += t(160, 130, 'Giữ giờ ngủ giống nhau trong các ngày làm ca', 10.5)
add('F2', 2, 'Một ngày làm ca đêm', 'Ví dụ minh họa: đi ngủ sớm sau ca, giữ đủ ít nhất 7 giờ, giờ ngủ giống nhau các ngày làm ca.', s + foot('Ví dụ minh họa, không phải lịch bắt buộc'))

grid('F3', 1, 'Năm chìa khóa cho hộp cơm', 'Năm chìa khóa an toàn thực phẩm của WHO, áp dụng cho hộp cơm mang đi làm.',
     'Hộp cơm an toàn', [('1. Giữ sạch', PINK), ('2. Tách sống – chín', YELLOW), ('3. Nấu chín kỹ', LBLUE), ('4. Giữ lạnh, hâm nóng kỹ', G), ('5. Nước, đồ ăn sạch', PURP)], 'Theo năm chìa khóa của WHO')
s = head('Màu nước tiểu')
for i, (lab, c) in enumerate([('Trong', '#f4f8fb'), ('Vàng nhạt', '#f8eeb0'), ('Vàng đậm', '#e8c24a'), ('Nâu', '#b8873a')]):
    s += f'<rect x="{20 + i * 72}" y="44" width="56" height="70" rx="8" fill="{c}" stroke="{NAVY}" stroke-width="2"/>' + t(48 + i * 72, 132, lab, 10)
s += t(84, 152, '✓ Đủ nước', 11, GREEN) + t(232, 152, 'Uống thêm', 11, RED)
add('F3', 2, 'Màu nước tiểu', 'Nước tiểu trong hoặc vàng nhạt là dấu hiệu đủ nước. Màu đậm: uống thêm.', s + foot('Uống ít một, nhiều lần, trước khi khát'))

grid('F4', 1, 'Giãn cơ 5 phút', 'Năm động tác chậm, nhẹ: cổ, vai, cổ tay, lưng, bắp chân. Đau thì dừng.',
     'Giãn cơ 5 phút', [('Cổ: nghiêng chậm', PINK), ('Vai: xoay vòng', YELLOW), ('Cổ tay: duỗi nhẹ', LBLUE), ('Lưng: vươn, ưỡn nhẹ', G), ('Bắp chân: kiễng gót', PURP), ('Đau: dừng ngay', LGRAY)], 'Chậm, nhẹ, thở đều')
s = head('Nghỉ ngắn giúp gì?')
for i, (lab, v, c) in enumerate([('Tỉnh táo hơn', 36, G), ('Bớt mệt', 35, G), ('Năng suất', 16, LGRAY)]):
    y = 46 + i * 36
    s += t(98, y + 16, lab, 10.5, NAVY, '600', 'end') + f'<rect x="106" y="{y}" width="{v * 4}" height="22" rx="4" fill="{c}" stroke="{NAVY}" stroke-width="1.5"/>'
    s += t(112 + v * 4, y + 16, f'd = 0,{v}' + (' (chưa rõ)' if v == 16 else ''), 10, NAVY, '600', 'start')
s += t(160, 168, 'Albulescu và cộng sự 2022, 22 mẫu, 2.335 người', 9.5, GRAY, '500')
add('F4', 2, 'Nghỉ ngắn giúp gì?', 'Nghỉ ngắn có tác dụng nhỏ: tỉnh táo hơn, bớt mệt. Năng suất chung chưa rõ.', s + foot('Tác dụng nhỏ nhưng có thật'))

s = head('Trời nóng: năng suất giảm')
for i in range(6):
    v = i * 2.5
    s += f'<rect x="{30 + i * 46}" y="{60 + v * 4}" width="30" height="{80 - v * 4}" fill="{LBLUE if i == 0 else PEACH}" stroke="{NAVY}" stroke-width="1.5"/>'
    s += t(45 + i * 46, 156, f'{20 + i * 2}°C', 9.5)
s += t(160, 48, 'Mỗi độ trên 20°C: giảm 2–3%', 11, RED)
add('F5', 1, 'Nóng và năng suất', 'WHO và WMO 2025: trên 20°C, mỗi độ tăng thêm làm năng suất giảm 2–3%. Cột chỉ minh họa xu hướng.', s + foot('Minh họa xu hướng, không phải số đo'))
compare('F5', 2, 'Kiệt sức hay sốc nhiệt', 'Kiệt sức vì nóng: đau đầu, chóng mặt, buồn nôn. Sốc nhiệt: lú lẫn, ngất, co giật, gọi 115 ngay.',
        'Hai mức nguy hiểm', ['Kiệt sức vì nóng', 'đau đầu, chóng', 'mặt, buồn nôn,', 'khát → nghỉ mát,', 'uống nước'], ['SỐC NHIỆT', 'lú lẫn, ngất,', 'co giật → gọi', '115, làm mát', 'ngay'], 'Lú lẫn là dấu hiệu cấp cứu', YELLOW, PINK)

# ================= TUẦN 2 =================
grid('F6', 1, 'Năm câu hỏi trước việc mới', 'Trước mỗi việc mới, hỏi: bị thương ra sao, bảo hộ gì, đã được hướng dẫn chưa, sự cố thì sao, hỏi ai.',
     'Trước việc mới, hỏi 5 câu', [('1. Có thể bị thương ra sao?', PINK), ('2. Cần đồ bảo hộ gì?', YELLOW), ('3. Đã được hướng dẫn?', LBLUE), ('4. Sự cố thì làm gì?', G), ('5. Hỏi ai?', PURP)], 'Chưa rõ câu nào thì chưa làm', size=10)
grid('F6', 2, 'Sáu mối nguy thường gặp', 'Sáu mối nguy hay gặp ở xưởng, công trường, bếp, kho.',
     'Săn mối nguy', [('Trơn, vấp, ngã', PINK), ('Vật rơi, vật đè', YELLOW), ('Máy quay, cuốn', LBLUE), ('Điện', G), ('Hóa chất, bụi', PURP), ('Ồn, nóng', PEACH)], 'Thấy nguy, báo ngay', cols=3, size=10)

grid('F7', 1, 'Đồ bảo hộ', 'Đồ bảo hộ đúng việc: mũ, kính, nút tai, khẩu trang, găng, giày. Đeo đúng cách mới có tác dụng.',
     'Đồ bảo hộ đúng việc', [('Mũ', LBLUE), ('Kính', YELLOW), ('Nút tai', PINK), ('Khẩu trang', G), ('Găng', PURP), ('Giày', PEACH)], 'Đúng việc, đúng cỡ, còn tốt', cols=3, size=11)
compare('F7', 2, 'Phép thử 1 mét', 'Phải nói to mới nghe được người cách khoảng 1 mét: chỗ đó có thể quá ồn, nên đeo nút tai.',
        'Ồn tới mức nào?', ['Nói bình thường,', 'cách 1 mét', 'vẫn nghe rõ'], ['Phải nói to', 'mới nghe được', '→ đeo nút tai,', 'báo tổ trưởng'], 'Mẹo ước lượng, không thay máy đo')

steps('F8', 1, 'Dừng – Báo – Chờ', 'Thấy rõ nguy cơ đe dọa tính mạng: dừng việc, báo ngay người phụ trách, chờ xử lý xong mới làm lại.',
      'Thấy rõ nguy hiểm', [['Dừng', 'việc'], ['Báo', 'ngay', 'tổ trưởng'], ['Chờ', 'xử lý', 'xong']], 'Quyền theo Luật ATVSLĐ 2015', 12)
steps('F8', 2, 'Báo cáo ba phần', 'Báo cáo ngắn ba phần: thấy gì, ở đâu, đã làm gì. Suýt tai nạn cũng nên báo.',
      'Báo cáo ba phần', [['Thấy', 'gì?'], ['Ở', 'đâu?'], ['Đã làm', 'gì?']], 'Suýt tai nạn cũng báo', 12)

compare('F9', 1, 'Đọc lại và tự hỏi', 'Tự hỏi rồi trả lời giúp nhớ lâu hơn đọc lại nhiều lần.',
        'Cách ôn nào nhớ lâu?', ['Đọc lại', 'nhiều lần,', 'tô màu'], ['Che đáp án,', 'tự trả lời,', 'rồi kiểm tra'], 'Tự hỏi nhớ lâu hơn')
s = head('Ôn giãn cách')
for i, (lab, x) in enumerate([('Ngày 1', 20), ('Ngày 2', 80), ('Ngày 4', 150), ('Ngày 8', 240)]):
    s += f'<circle cx="{x + 20}" cy="90" r="18" fill="{[PINK, YELLOW, LBLUE, G][i]}" stroke="{NAVY}" stroke-width="2"/>' + t(x + 20, 130, lab, 10)
    if i < 3:
        nx = [80, 150, 240][i]
        s += arrow(x + 40, 90, nx - 2, 90, ORANGE, 3)
add('F9', 2, 'Ôn giãn cách', 'Ôn lại sau 1 ngày, rồi giãn dần ra. Ví dụ lịch: ngày 1, 2, 4, 8.', s + foot('Ví dụ lịch, có thể điều chỉnh'))

s = head('Leo một bậc')
for i, (lab, c) in enumerate([(['Hiện tại', 'làm được'], PINK), (['Kỹ năng', 'kế tiếp'], YELLOW), (['Bậc mới,', 'việc mới'], G)]):
    s += box(14 + i * 102, 130 - i * 44, 88, 40, lab, c, 10.5)
    if i < 2:
        s += arrow(14 + i * 102 + 90, 140 - i * 44, 14 + (i + 1) * 102 - 2, 108 - i * 44, ORANGE, 3)
add('F10', 1, 'Leo một bậc', 'Chọn một kỹ năng kế tiếp, học 15 phút mỗi ngày, để lên một bậc việc làm.', s + foot('Mỗi lần một kỹ năng'))
steps('F10', 2, 'Hỏi để học', 'Hỏi tổ trưởng ba câu: kỹ năng nào cần, ai dạy, chuẩn đạt là gì.',
      'Ba câu hỏi tổ trưởng', [['Kỹ năng', 'nào cần?'], ['Ai', 'có thể', 'chỉ em?'], ['Đạt', 'chuẩn', 'là gì?']], 'Hỏi rõ, ghi lại', 11)

# ================= TUẦN 3 =================
s = head('Bảy ngày ghi chi')
for i, d in enumerate(['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']):
    s += box(12 + i * 43, 50, 38, 60, [d, '', '...đ'], [PINK, YELLOW, LBLUE, G, PURP, PEACH, LGRAY][i], 10)
s += box(60, 124, 200, 30, 'Cộng: tiền đi đâu nhiều nhất?', YELLOW, 10.5)
add('F11', 1, 'Bảy ngày ghi chi', 'Ghi mọi khoản chi trong 7 ngày, rồi cộng lại để thấy tiền đi đâu nhiều nhất.', s + foot('Ghi ngay, không để cuối ngày'))
compare('F11', 2, 'Cần hay muốn', 'Trước khi mua, hỏi: đây là cần (ăn, ở, đi làm) hay muốn (thích, có cũng được)?',
        'Cần hay muốn?', ['CẦN', 'ăn, ở, đi làm,', 'thuốc, tiền', 'gửi về nhà'], ['MUỐN', 'đồ thích,', 'ăn ngoài,', 'có cũng được'], 'Muốn thì chờ 1 ngày rồi quyết', LBLUE, PEACH)

s = head('Chia lương bốn phần')
for i, (lab, w, c) in enumerate([('Cố định', 90, PINK), ('Ăn uống', 80, YELLOW), ('Dự phòng', 50, G), ('Còn lại', 70, LBLUE)]):
    x = 10 + sum([90, 80, 50, 70][:i]) + i * 3
    s += f'<rect x="{x}" y="60" width="{w}" height="50" fill="{c}" stroke="{NAVY}" stroke-width="2"/>' + t(x + w / 2, 90, lab, 10)
s += t(160, 136, 'Tiền dự phòng chuyển ra trước khi tiêu', 10.5)
add('F12', 1, 'Chia lương bốn phần', 'Nhận lương thì chia ngay: cố định, ăn uống, dự phòng, còn lại. Tỉ lệ ở đây chỉ là minh họa.', s + foot('Tỉ lệ minh họa, tùy nhà'))
grid('F12', 2, 'Đọc phiếu lương', 'Phiếu lương ghi lương, làm thêm giờ, làm đêm, khoản khấu trừ. So với sổ chấm công của mình.',
     'Đọc phiếu lương', [('Lương', PINK), ('Làm thêm giờ', YELLOW), ('Làm đêm', LBLUE), ('Khấu trừ (nếu có)', G)], 'So với sổ giờ làm của mình')

grid('F13', 1, 'Dấu hiệu lừa việc làm', 'Dấu hiệu lừa đảo việc làm: thu phí trước, lương cao việc nhẹ, ép quyết nhanh, bắt nạp tiền làm nhiệm vụ.',
     'Dấu hiệu lừa việc làm', [('Thu phí trước', PINK), ('Việc nhẹ, lương cao', YELLOW), ('Ép ký ngay', LBLUE), ('Nạp tiền làm nhiệm vụ', G)], 'Có 1 dấu hiệu: dừng lại, hỏi người tin cậy')
compare('F13', 2, 'Vay ở đâu', 'Vay nóng ngoài đường dễ thành nợ lớn. Trần lãi vay dân sự là 20% một năm.',
        'Cần tiền gấp', ['Vay nóng', 'qua tờ rơi,', 'ứng dụng lạ,', 'lãi theo ngày'], ['Quỹ dự phòng,', 'người thân,', 'công đoàn,', 'ngân hàng'], 'Lãi theo ngày: dừng lại', PINK, G)

grid('F14', 1, 'Bốn việc của chữ tín', 'Chữ tín ở chỗ làm là bốn việc nhỏ: đúng giờ, giữ lời, nói thật, nhận lỗi.',
     'Chữ tín: bốn việc nhỏ', [('Đúng giờ', PINK), ('Giữ lời', YELLOW), ('Nói thật', LBLUE), ('Nhận lỗi, sửa lỗi', G)], 'Chữ tín là vốn của người làm')
steps('F14', 2, 'Nhận lỗi 4 bước', 'Nhận lỗi 4 bước: việc gì xảy ra, hậu quả, cách sửa, cách tránh lần sau.',
      'Nhận lỗi 4 bước', [['Việc gì', 'xảy ra'], ['Hậu', 'quả'], ['Cách', 'sửa'], ['Lần sau', 'tránh', 'thế nào']], 'Nói sớm, sửa sớm', 10.5)

grid('F15', 1, 'Tử tế nơi làm', 'Ba việc tử tế mỗi ngày: chỉ việc cho người mới, cảm ơn cụ thể, không cười cợt người khác.',
     'Tử tế nơi làm', [('Chỉ việc người mới', PINK), ('Cảm ơn cụ thể', YELLOW), ('Không cười cợt, bêu xấu', LBLUE), ('Thấy bắt nạt: báo', G)], 'Nhỏ, đều, ai cũng làm được')
steps('F15', 2, 'Khi bị quấy rối', 'Khi bị quấy rối: nói dừng nếu an toàn, ghi lại, báo người có trách nhiệm hoặc công đoàn.',
      'Khi bị quấy rối', [['Nói', '"Dừng lại"', '(nếu an toàn)'], ['Ghi', 'ngày, giờ,', 'người thấy'], ['Báo', 'người phụ', 'trách, CĐ']], 'Không phải lỗi của bạn', 10)

# ================= TUẦN 4 =================
steps('F16', 1, 'Dừng – Gọi tên – Thở', 'Khi bực hay lo: dừng tay, gọi tên cảm xúc, thở chậm 1–3 phút, rồi mới nói hay làm.',
      'Khi cảm xúc dâng lên', [['Dừng', 'tay'], ['Gọi tên', '"Mình', 'đang bực"'], ['Thở', 'chậm', '1–3 phút']], 'Gọi tên được thì dễ chọn cách làm', 11)
s = head('Thở chậm: hít 4, thở 6')
s += f'<path d="M30 130 Q90 50 150 130 Q230 50 290 130" fill="none" stroke="{BLUE}" stroke-width="4"/>'
s += t(90, 76, 'Hít 4', 12) + t(150, 150, 'Thở ra 6', 12) + t(230, 76, 'Hít 4', 12)
add('F16', 2, 'Thở chậm', 'Hít vào đếm 4, thở ra đếm 6, lặp lại 1–3 phút. Chóng mặt thì thở bình thường.', s + foot('Ví dụ nhịp, thấy dễ chịu là được'))

grid('F17', 1, 'Dấu hiệu quá tải', 'Dấu hiệu quá tải kéo dài nhiều tuần: mất ngủ, cáu gắt, buồn, uống nhiều hơn, muốn bỏ hết.',
     'Quá tải kéo dài?', [('Mất ngủ nhiều tuần', PINK), ('Cáu gắt, buồn', YELLOW), ('Uống rượu nhiều hơn', LBLUE), ('Muốn bỏ hết', G)], 'Có dấu hiệu: nói với người tin cậy sớm')
s = head('Ba bậc tìm giúp')
for i, (lab, c) in enumerate([(['Bậc 1', 'người thân, bạn'], G), (['Bậc 2', 'y tế, tư vấn'], YELLOW), (['Bậc 3', 'nguy hiểm: 115'], PINK)]):
    s += box(14 + i * 102, 130 - i * 44, 88, 40, lab, c, 10.5)
    if i < 2:
        s += arrow(14 + i * 102 + 90, 140 - i * 44, 14 + (i + 1) * 102 - 2, 108 - i * 44, ORANGE, 3)
add('F17', 2, 'Ba bậc tìm giúp', 'Bắt đầu từ người thân, bạn bè; cần thì tìm y tế, tư vấn; nguy hiểm thì gọi 115 ngay.', s + foot('Nghĩ đến cái chết: nói ngay hôm nay'))

cyc('F18', 1, 'Cuộc gọi 10 phút', 'Cuộc gọi 10 phút với con: hỏi một câu mở, nghe con kể, kể việc của mình, hẹn lần sau.',
    'Cuộc gọi 10 phút với con', [['Hỏi', '1 câu mở'], ['Nghe', 'con kể'], ['Kể', 'việc mình'], ['Hẹn', 'lần sau']], 'Giờ gọi cố định giúp con chờ')
compare('F18', 2, 'Câu hỏi mở', 'Câu hỏi đóng chỉ được "có" hay "không". Câu hỏi mở mời con kể chuyện.',
        'Hỏi sao cho con kể?', ['"Ở nhà', 'ngoan không?"', '→ "Dạ có"'], ['"Hôm nay', 'chuyện gì làm', 'con cười?"'], 'Hỏi mở, nghe nhiều hơn nói')

s = head('Vòng người có thể nhờ')
for r, c in [(70, LGRAY), (48, LBLUE), (26, G)]:
    s += f'<circle cx="110" cy="104" r="{r}" fill="{c}" stroke="{NAVY}" stroke-width="2"/>'
s += t(110, 108, 'Mình', 11) + t(110, 68, 'Gia đình', 9.5) + t(110, 44, 'Bạn, đồng nghiệp', 9.5)
s += box(196, 54, 114, 30, '3 người có thể nhờ', YELLOW, 10) + box(196, 96, 114, 30, 'Giữ liên lạc mỗi tuần', G, 10)
add('F19', 1, 'Vòng người có thể nhờ', 'Ghi tên 3 người có thể nhờ khi khó: trong gia đình, bạn bè, đồng nghiệp.', s + foot('Giúp người, người giúp mình'))
grid('F19', 2, 'Gặp người, giữ lửa', 'Bốn cách nhỏ giữ quan hệ: hỏi thăm, ăn chung, giúp một việc, rủ vận động.',
     'Giữ quan hệ, việc nhỏ', [('Hỏi thăm 1 người', PINK), ('Ăn chung bữa', YELLOW), ('Giúp 1 việc nhỏ', LBLUE), ('Rủ đi bộ, chơi thể thao', G)], 'Đều đặn hơn là nhiều')

s = head('Tuần 1 và tuần 4')
for i, (lab, a, b) in enumerate([('Ngủ', 1, 2), ('Nước', 0, 2), ('An toàn', 1, 2), ('Tiền', 0, 1), ('Tâm trí', 1, 2)]):
    x = 22 + i * 58
    s += f'<rect x="{x}" y="{140 - a * 40}" width="20" height="{a * 40 + 2}" fill="{LGRAY}" stroke="{NAVY}" stroke-width="1.5"/>'
    s += f'<rect x="{x + 22}" y="{140 - b * 40}" width="20" height="{b * 40 + 2}" fill="{G}" stroke="{NAVY}" stroke-width="1.5"/>'
    s += t(x + 21, 158, lab, 9.5)
s += t(100, 44, '■ Tuần 1', 10, GRAY) + t(200, 44, '■ Tuần 4', 10, GREEN)
add('F20', 1, 'Xem lại bốn tuần', 'Ví dụ minh họa: chấm 0–1–2 ở tuần 1 và tuần 4 để thấy mục nào đã tiến.', s + foot('Số liệu minh họa'))
steps('F20', 2, 'Giữ ba thói quen', 'Chọn 3 thói quen giữ trong 30 ngày tới, mỗi ngày đánh dấu vào sổ.',
      'Ba mươi ngày tới', [['Chọn', '3 thói', 'quen'], ['Đánh', 'dấu', 'mỗi ngày'], ['Sau', '30 ngày', 'xem lại']], 'Lỡ một ngày: làm lại ngày sau', 11)
