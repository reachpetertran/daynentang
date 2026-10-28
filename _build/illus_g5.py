# Hình minh họa và sơ đồ khóa G5 "Vợ chồng đồng lòng"
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'

# ================= TRANG KHÓA =================
s = t(160, 22, 'Bốn phần của đồng nuôi dạy', 14)
for i, (lab, txt, c) in enumerate([('Đồng thuận', ['cùng hướng', 'nuôi dạy con'], LBLUE), ('Chia việc', ['công bằng,', 'cả hai thấy ổn'], YELLOW),
                                     ('Ủng hộ', ['không phá nhau', 'trước con'], G), ('Cùng xử lý', ['bất đồng,', 'không kéo con vào'], PINK)]):
    x = 14 + (i % 2) * 150; y = 34 + (i // 2) * 72
    s += box(x, y, 142, 64, [lab] + txt, c, 10.5)
s += t(160, 192, 'Hai người, một đội', 12, GREEN, '700')
add('KHOAW', 1, 'Bốn phần của đồng nuôi dạy', 'Đồng thuận về cách nuôi con, chia việc, ủng hộ nhau, và cùng xử lý bất đồng mà không kéo con vào.', s)
add('KHOAW', 2, 'Sáu tuần', 'Mỗi tuần một kỹ năng, mỗi ngày một việc nhỏ.',
    t(160, 24, 'Sáu tuần', 14)
    + flow([['1. Một', 'đội'], ['2. Cảm ơn', 'nhau'], ['3. Nói khi', 'bất đồng']], 40, 58, 10, 310, 16, 11, [SAND, YELLOW, LBLUE])
    + flow([['4. Khi', 'nóng giận'], ['5. Trước', 'mặt con'], ['6. Họp', 'vợ chồng']], 112, 58, 10, 310, 16, 11, [PINK, G, PURP])
    + t(160, 192, 'Mỗi tuần 30 phút + việc nhỏ mỗi ngày', 11.5, GREEN))

# ================= BÀI 1 =================
s = t(160, 22, 'Giống và khác về nuôi con', 14)
s += f'<circle cx="122" cy="110" r="72" fill="{LBLUE}" fill-opacity="0.55" stroke="{NAVY}" stroke-width="2.5"/>'
s += f'<circle cx="198" cy="110" r="72" fill="{PINK}" fill-opacity="0.55" stroke="{NAVY}" stroke-width="2.5"/>'
s += t(84, 104, 'Giờ ngủ', 10) + t(84, 124, 'Điện thoại', 10) + t(236, 104, 'Đồ ngọt', 10) + t(236, 124, 'Đi học thêm', 10)
s += t(160, 96, 'Không đánh', 10, NAVY, '700') + t(160, 114, 'Đọc sách', 10, NAVY, '700') + t(160, 132, 'Trung thực', 10, NAVY, '700')
s += t(36, 50, 'Chồng', 12) + t(284, 50, 'Vợ', 12)
add('W1', 1, 'Giống và khác', 'Mỗi người viết điều mình coi trọng khi nuôi con. Phần chung là nền; phần khác cần bàn.', s)
s = t(160, 22, 'Một đội, không phải hai đội', 14)
s += person(80, 160, 0.85, BLUE) + person(130, 160, 0.85, PINK) + person(250, 168, 0.6, ORANGE, False)
s += f'<path d="M60 70 h90" stroke="{GREEN}" stroke-width="4" stroke-linecap="round"/>' + t(105, 60, 'cùng phía', 11, GREEN, '700')
s += arrow(160, 120, 220, 120, ORANGE, 3) + t(190, 108, 'cùng một lời', 10.5) + t(160, 192, 'Bất đồng thì bàn riêng, nói với con một lời', 11, NAVY, '600')
add('W1', 2, 'Một đội', 'Bố mẹ đứng cùng phía. Bất đồng thì bàn riêng, khi nói với con thì nói một lời.', s)

# ================= BÀI 2 =================
s = t(160, 22, 'Đáp lại lời mời nhỏ', 14)
s += bubble(20, 44, 150, 34, '"Anh xem này…"', 11)
s += arrow(96, 84, 60, 112, GREEN, 3) + arrow(96, 84, 230, 112, RED, 3)
s += box(14, 116, 130, 50, ['Quay sang:', '"Gì thế em?"'], G, 11) + box(176, 116, 130, 50, ['Lờ đi, mắt', 'vẫn nhìn máy'], LGRAY, 11)
s += check(72, 182)
add('W2', 1, 'Đáp lại lời mời nhỏ', 'Mỗi ngày có nhiều lời mời nhỏ: "Anh xem này", một cái nhìn. Quay sang đáp lại là cách giữ gần gũi.', s)
s = t(160, 22, 'Cảm ơn cụ thể', 14)
s += box(14, 40, 292, 40, '"Cảm ơn em."', LGRAY, 12) + t(160, 98, 'thành', 11, GRAY)
s += box(14, 108, 292, 56, ['"Cảm ơn em tối qua dậy cho con bú', 'để anh ngủ. Anh khỏe hẳn."'], G, 11.5)
s += t(160, 186, 'Việc cụ thể + điều nó giúp mình', 11.5, GREEN)
add('W2', 2, 'Cảm ơn cụ thể', 'Lời cảm ơn có việc cụ thể và điều nó giúp mình thì người nghe thấy được ghi nhận.', s)

# ================= BÀI 3 =================
add('W3', 1, 'Mở lời nhẹ', 'Khi muốn nói chuyện khó: nói về cảm xúc của mình, việc cụ thể, và điều mình cần. Không chê con người.',
    t(160, 26, 'Mở lời nhẹ', 14) + flow([['"Em', 'thấy…"'], ['"khi…"', '(việc cụ', 'thể)'], ['"vì…"'], ['"Em cần', '…"']], 46, 74, 8, 312, 10, 11, [PINK, YELLOW, LBLUE, G])
    + box(14, 140, 292, 40, ['"Em mệt khi tối nào cũng một mình tắm cho con.', 'Em cần anh lo tắm 3 tối một tuần."'], WHITE, 10.5))
s = t(160, 22, 'Người nói – người nghe', 14)
s += person(80, 170, 0.85, BLUE) + person(240, 170, 0.85, PINK)
s += f'<rect x="64" y="40" width="34" height="14" rx="4" fill="{BROWN}"/>' + t(80, 72, 'cầm "sàn"', 10, NAVY, '700')
s += bubble(116, 44, 110, 30, '"Anh thấy…"', 11) + bubble(150, 92, 120, 30, '"Ý anh là…?"', 11)
s += t(160, 194, 'Đổi vai sau mỗi lượt. Chưa giải quyết vội', 10.5, GREEN)
add('W3', 2, 'Người nói – người nghe', 'Một người cầm "sàn" và nói ngắn; người kia nhắc lại cho đúng ý rồi mới đổi vai.', s)

# ================= BÀI 4 =================
s = t(160, 22, 'Khi nóng giận: tạm dừng', 14)
for i, (lab, c) in enumerate([(['Nói', 'tín hiệu', 'dừng'], YELLOW), (['Rời đi', '20 phút'], LBLUE), (['Làm việc', 'dịu lại'], G), (['Hẹn giờ', 'quay lại'], PINK)]):
    x = 14 + i * 76
    s += box(x, 60, 70, 70, lab, c, 10.5)
    if i < 3: s += arrow(x + 71, 95, x + 75, 95, ORANGE, 2.5)
s += t(160, 160, 'Không đuổi theo, không nhắn tin cãi tiếp', 11, RED) + t(160, 180, 'Tạm dừng khác bỏ đi: luôn hẹn quay lại', 11, GREEN)
add('W4', 1, 'Tạm dừng', 'Thống nhất tín hiệu dừng, rời đi khoảng 20 phút, làm việc dịu lại, và luôn hẹn giờ quay lại nói tiếp.', s)
s = t(160, 22, 'Hàn gắn sau cãi nhau', 14)
for i, ln in enumerate(['"Lúc nãy anh to tiếng, anh xin lỗi."', '"Em hiểu anh đang lo chuyện tiền."', '"Mình thử lại từ đầu nhé?"']):
    s += box(14, 40 + i * 44, 292, 34, ln, [PINK, LBLUE, G][i], 11)
s += t(160, 186, 'Ai sửa trước cũng là thắng cho cả hai', 11, GREEN)
add('W4', 2, 'Hàn gắn', 'Câu hàn gắn ngắn: nhận phần mình, hiểu người kia, mời bắt đầu lại.', s)

# ================= BÀI 5 =================
s = t(160, 22, 'Trước mặt con', 14)
s += box(14, 40, 140, 120, ['Nên', '', 'Không đồng ý thì', 'bàn riêng', 'Con thấy làm lành', 'Nói một lời'], G, 10.5)
s += box(166, 40, 140, 120, ['Tránh', '', 'Chê bố/mẹ trước con', 'Bắt con chọn phe', 'Nhờ con nhắn lời', 'Phá luật người kia'], '#f7c9c5', 10.5)
s += t(160, 186, 'Con cảm thấy an toàn khi bố mẹ là một đội', 11, NAVY, '600')
add('W5', 1, 'Trước mặt con', 'Bàn bất đồng riêng, để con thấy bố mẹ làm lành, không kéo con về phe nào.', s)
s = t(160, 22, 'Câu nói khi con hỏi "Ai đúng?"', 13.5)
s += box(14, 44, 292, 44, ['"Bố mẹ đang nghĩ khác nhau. Bố mẹ sẽ bàn', 'và trả lời con sau bữa tối."'], LBLUE, 11)
s += arrow(160, 92, 160, 112, ORANGE, 3) + box(14, 116, 292, 44, ['Sau đó: cùng nói với con một quyết định'], G, 11)
s += t(160, 184, 'Không nói "Hỏi mẹ mày ấy"', 11, RED)
add('W5', 2, 'Khi con hỏi ai đúng', 'Câu nói mẫu khi bố mẹ chưa thống nhất mà con đang chờ câu trả lời.', s)

# ================= BÀI 6 =================
s = t(160, 22, 'Họp vợ chồng 20 phút mỗi tuần', 14)
parts = [('Cảm ơn', 4, PINK), ('Lịch tuần', 4, LBLUE), ('Con cái', 5, YELLOW), ('Một chuyện', 4, G), ('Hẹn hò', 3, PURP)]
x = 12
for lab, m, c in parts:
    w = 296 * m / 20
    s += box(x, 50, w - 4, 70, lab.split(' ') + [f"{m}'"], c, 10, rx=6)
    x += w
s += t(160, 150, 'Ví dụ tối Chủ nhật, sau khi con ngủ', 11.5, GREEN) + t(160, 170, 'Bố đi công tác: họp qua video', 11, NAVY, '500')
add('W6', 1, 'Họp vợ chồng', 'Cảm ơn, lịch tuần, chuyện con, một chuyện cần bàn, và hẹn một lúc riêng cho hai người.', s)
add('W6', 2, 'Vòng một tuần', 'Họp, làm cả tuần, đáp lại lời mời nhỏ, sửa một điều. Mỗi tuần gần nhau hơn một chút.',
    t(160, 20, 'Vòng một tuần', 14) + cycle([['Họp', '20 phút'], ['Làm cả', 'tuần'], ['Cảm ơn', 'mỗi ngày'], ['Sửa', 'một điều']], 160, 118, 64, 88, 34, 10.5, [YELLOW, LBLUE, PINK, G]))

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('W', 'KHOAW'))), 'hình G5')
