# Hình minh họa và sơ đồ khóa G4 "Gia đình có con 10–14"
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'
def teen(x, y, s=1, shirt=PURP): return person(x, y, s * 0.88, shirt, True)

def phone(x, y, w=34, h=58):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{NAVY}"/>'
            f'<rect x="{x+3}" y="{y+6}" width="{w-6}" height="{h-14}" rx="2" fill="{LBLUE}"/>')

# ================= TRANG KHÓA =================
add('KHOAY', 1, 'Yêu thương và giới hạn', 'Tuổi 10–14 cần cả hai: gần gũi, lắng nghe; và luật rõ, giới hạn nhất quán.',
    t(160, 24, 'Yêu thương + giới hạn', 14)
    + box(14, 44, 140, 110, ['Yêu thương', '', 'Thời gian riêng', 'Lắng nghe', 'Khen cụ thể'], PINK, 11)
    + box(166, 44, 140, 110, ['Giới hạn', '', 'Thỏa thuận rõ', 'Hậu quả nhất quán', 'Biết con ở đâu'], LBLUE, 11)
    + t(160, 104, '+', 26, NAVY, '800') + t(160, 184, 'Thiếu một bên, con dễ chênh vênh', 11.5, GREEN))
s = t(160, 22, 'Bảy tuần', 14)
items = [('1. Hiểu tuổi 10–14', SAND), ('2. Lắng nghe', YELLOW), ('3. Thỏa thuận', LBLUE), ('4. Giải quyết vấn đề', G),
         ('5. Điện thoại, mạng', PURP), ('6. Bạn bè, rượu bia', PINK), ('7. Cảm xúc, tương lai', '#f6d9a8')]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 36 + (i // 2) * 40
    if i == 6: x = 89
    s += box(x, y, 142, 32, lab, c, 11)
add('KHOAY', 2, 'Bảy tuần', 'Mỗi tuần một chủ đề, mỗi chủ đề có phần bố mẹ và phần cùng con.', s)

# ================= BÀI 1 =================
s = t(160, 22, 'Tuổi 10–14 đang thay đổi', 14)
for i, (lab, txt, c) in enumerate([('Cơ thể', ['dậy thì, lớn', 'nhanh, ngủ muộn'], LBLUE), ('Cảm xúc', ['mạnh, đổi', 'nhanh'], PINK), ('Bạn bè', ['quan trọng', 'hơn trước'], YELLOW), ('Tự lập', ['muốn tự', 'quyết định'], G)]):
    x = 14 + (i % 2) * 150; y = 40 + (i // 2) * 74
    s += box(x, y, 142, 64, [lab] + txt, c, 11)
s += t(160, 192, 'Bình thường, không phải "hư"', 11.5, GREEN)
add('Y1', 1, 'Tuổi 10–14 đang thay đổi', 'Cơ thể, cảm xúc, bạn bè, nhu cầu tự lập đều thay đổi. Đó là bình thường.', s)
s = t(160, 22, 'Thời gian riêng 15 phút', 14) + person(100, 170, 0.85, BLUE) + teen(200, 170, 0.95)
s += bubble(36, 34, 120, 32, '"Con chọn nhé"', 11) + bubble(186, 40, 120, 32, '"Chơi cờ đi bố"', 11)
s += t(160, 192, 'Con chọn việc, bố mẹ đi theo, không điện thoại', 10.5, GREEN)
add('Y1', 2, 'Thời gian riêng', 'Mỗi tuần vài lần, 15 phút một – một. Con chọn việc, bố mẹ đi theo, không giảng dạy.', s)

# ================= BÀI 2 =================
add('Y2', 1, 'Lắng nghe để con kể', 'Lắng nghe, nhắc lại, hỏi thêm, rồi mới nói ý mình. Con kể nhiều hơn khi không bị phán xét ngay.',
    t(160, 28, 'Lắng nghe để con muốn kể', 14) + flow([['Dừng', 'việc,', 'nhìn con'], ['Nghe', 'hết,', 'không ngắt'], ['Nhắc lại', '"Ý con', 'là…"'], ['Hỏi', '"Rồi sao', 'nữa?"']],
    52, 80, 8, 312, 10, 10.5, [SAND, YELLOW, LBLUE, G]) + t(160, 160, 'Khuyên sau, và chỉ khi con muốn nghe', 11.5, GREEN))
s = t(160, 22, 'Con tự kể hay bị hỏi tra?', 14)
s += box(14, 40, 140, 100, ['Hỏi tra, theo dõi', 'lén, mắng ngay', '', '→ con giấu'], LGRAY, 11)
s += box(166, 40, 140, 100, ['Lắng nghe, bình', 'tĩnh, tôn trọng', '', '→ con tự kể'], G, 11)
s += t(160, 168, 'Bố mẹ biết về con chủ yếu nhờ con kể', 11, NAVY, '600') + t(160, 186, 'Theo Kerr và Stattin 2000 (nghiên cứu liên hệ)', 9.5, GRAY, '500')
add('Y2', 2, 'Con tự kể', 'Nghiên cứu cho thấy hiểu biết của bố mẹ về con gắn với việc con tự kể nhiều hơn là với theo dõi.', s)

# ================= BÀI 3 =================
s = t(160, 22, 'Thỏa thuận nhà mình', 14) + paper(30, 32, 260, 158)
for i, (a, b) in enumerate([('Luật', 'Về nhà trước 18 giờ'), ('Đặc quyền', 'Chơi game 30 phút cuối tuần'), ('Hậu quả', 'Về trễ: tuần sau ở nhà'), ('Ký', 'Bố · Mẹ · Con')]):
    y = 60 + i * 34
    s += t(48, y, a, 11.5, ORANGE, '800', 'start') + t(130, y, b, 11, NAVY, '600', 'start')
add('Y3', 1, 'Thỏa thuận nhà mình', 'Luật rõ, đặc quyền đi kèm trách nhiệm, hậu quả nói trước. Con cùng viết và ký.', s)
add('Y3', 2, 'Luật tốt', 'Một luật tốt: ít, rõ, con hiểu lý do, có góp ý của con, áp dụng nhất quán.',
    t(160, 28, 'Một luật tốt', 14) + flow([['Ít', '(3–5)'], ['Rõ, đo', 'được'], ['Con hiểu', 'lý do'], ['Con góp', 'ý'], ['Giữ', 'đều']], 52, 70, 8, 312, 8, 10.5,
    [SAND, YELLOW, LBLUE, G, PURP]) + t(160, 152, 'Xem lại khi con lớn hơn', 11.5, GREEN))

# ================= BÀI 4 =================
add('Y4', 1, 'Năm bước giải quyết vấn đề', 'Gọi tên vấn đề, nghĩ nhiều cách, chọn một, thử, rồi xem lại.',
    t(160, 22, 'Giải quyết vấn đề cùng nhau', 14) + cycle([['Gọi tên', 'vấn đề'], ['Nghĩ', 'nhiều cách'], ['Chọn', 'một cách'], ['Thử', '1 tuần'], ['Xem', 'lại']], 160, 122, 72, 76, 30, 10.5,
    [SAND, YELLOW, LBLUE, G, PINK]))
s = t(160, 22, 'Hậu quả, không trừng phạt', 14)
s += box(14, 40, 140, 100, ['Liên quan', 'Ngắn', 'Nói trước', 'Tôn trọng'], G, 11.5)
s += box(166, 40, 140, 100, ['Không đánh', 'Không làm nhục', 'Không cấm', 'nhiều tuần'], '#f7c9c5', 11.5)
s += t(160, 170, 'Ví dụ: dùng máy quá giờ → mai không dùng', 11, NAVY, '600')
add('Y4', 2, 'Hậu quả hợp lý', 'Hậu quả nên liên quan đến việc sai, ngắn, nói trước. Không đánh, không làm con xấu hổ.', s)

# ================= BÀI 5 =================
s = t(160, 22, 'Kế hoạch dùng thiết bị gia đình', 13.5)
for i, (lab, c) in enumerate([('Giờ dùng', LBLUE), ('Chỗ không máy', YELLOW), ('Sạc ngoài phòng ngủ', G), ('Bố mẹ làm gương', PINK)]):
    x = 14 + (i % 2) * 150; y = 40 + (i // 2) * 64
    s += box(x, y, 142, 54, lab, c, 11.5)
s += t(160, 184, 'Cả nhà cùng theo, kể cả bố mẹ', 11.5, GREEN)
add('Y5', 1, 'Kế hoạch dùng thiết bị', 'Bốn phần của kế hoạch: giờ dùng, chỗ không máy, sạc ngoài phòng ngủ, bố mẹ làm gương.', s)
s = t(160, 22, 'Dấu hiệu người lạ trên mạng', 14)
for i, r in enumerate(['Khen quá mức, tặng quà', 'Đòi giữ bí mật với bố mẹ', 'Xin ảnh riêng tư', 'Rủ gặp riêng']):
    y = 38 + i * 36
    s += f'<circle cx="28" cy="{y+14}" r="11" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>' + t(28, y + 18, '!', 13, WHITE, '800') + box(46, y, 260, 28, r, WHITE, 11)
s += t(160, 190, 'Thấy một dấu hiệu: chặn, chụp lại, kể bố mẹ', 11, RED)
add('Y5', 2, 'An toàn trên mạng', 'Bốn dấu hiệu cần dừng lại và kể ngay với người lớn tin cậy.', s)

# ================= BÀI 6 =================
s = t(160, 22, 'Mật mã gọi đón', 14) + teen(70, 170, 0.9) + phone(130, 70)
s += bubble(176, 50, 130, 34, '"Bố ơi, con quên áo"', 11) + arrow(240, 92, 240, 116, ORANGE, 3)
s += box(176, 120, 130, 44, ['Bố đến đón ngay,', 'không hỏi lúc đó'], G, 10.5)
s += t(160, 192, 'Câu mật mã nghĩa là: "Con cần ra khỏi đây"', 10.5, NAVY, '600')
add('Y6', 1, 'Mật mã gọi đón', 'Cả nhà thống nhất một câu mật mã. Con nhắn câu đó, bố mẹ đến đón ngay, không tra hỏi lúc đó.', s)
add('Y6', 2, 'Cách nói không', 'Bốn cách từ chối khi bạn rủ làm điều nguy hiểm.',
    t(160, 28, 'Bốn cách nói không', 14) + flow([['"Không,', 'cảm ơn"'], ['Đưa lý', 'do: "Bố', 'mẹ đón"'], ['Đổi', 'chủ đề'], ['Bỏ đi', '/ gọi', 'mật mã']], 52, 80, 8, 312, 10, 10.5,
    [SAND, YELLOW, LBLUE, G]) + t(160, 158, 'Tập trước ở nhà, nói được thật dễ hơn', 11.5, GREEN)
    + t(160, 180, 'Bán rượu bia cho người dưới 18 tuổi là vi phạm luật', 10, RED))

# ================= BÀI 7 =================
s = t(160, 22, 'Bình tĩnh lại khi căng thẳng', 14)
for i, (lab, c) in enumerate([('Ngủ đủ giờ', LBLUE), ('Vận động 60 phút', G), ('Thở chậm 1 phút', YELLOW), ('Nói với người tin', PINK)]):
    x = 14 + (i % 2) * 150; y = 40 + (i // 2) * 64
    s += box(x, y, 142, 54, lab, c, 11.5)
s += t(160, 182, 'Ngủ, vận động là nền của cảm xúc', 11.5, GREEN)
add('Y7', 1, 'Nền của cảm xúc', 'Ngủ đủ, vận động mỗi ngày, thở chậm và có người để nói chuyện giúp con vững hơn khi căng thẳng.', s)
s = t(160, 22, 'Khi nào cần tìm giúp', 14)
s += box(14, 40, 292, 64, ['Buồn chán, cáu gắt kéo dài nhiều tuần', 'Bỏ ăn, mất ngủ, rút khỏi bạn bè, bỏ học', 'Nói về cái chết hay làm hại bản thân'], '#f7c9c5', 10.5)
s += arrow(160, 108, 160, 124, ORANGE, 3) + box(14, 128, 292, 50, ['Nói chuyện với con, ở bên con', 'Gặp bác sĩ, chuyên gia. Khẩn cấp: 115'], G, 11)
add('Y7', 2, 'Khi nào cần tìm giúp', 'Dấu hiệu cần đưa con gặp chuyên gia. Khẩn cấp gọi 115.', s)

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('Y', 'KHOAY'))), 'hình G4')
