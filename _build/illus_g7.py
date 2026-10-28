# Hình minh họa và sơ đồ khóa G7 "Việc nhà chia đều"
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'
def kid(x, y, s=1, shirt=ORANGE): return person(x, y, s, shirt, False)

# ================= TRANG KHÓA =================
add('KHOAH', 1, 'Bốn tuần, bốn bước', 'Nhìn thấy mọi việc, chia lại cho công bằng, dạy con làm, rồi giữ đều.',
    t(160, 30, 'Bốn tuần, bốn bước', 14) + flow([['Tuần 1', 'Nhìn thấy', 'mọi việc'], ['Tuần 2', 'Chia lại', 'công bằng'], ['Tuần 3', 'Dạy con', 'làm'], ['Tuần 4', 'Giữ', 'đều']],
    58, 80, 8, 312, 10, 10.5, [SAND, YELLOW, G, PURP]) + t(160, 166, 'Mỗi tuần: 1 buổi bố mẹ + 1 buổi cả nhà', 12, GREEN))
s = t(160, 22, 'Một việc nhà có hai phần', 14)
s += box(14, 40, 140, 120, ['Phần làm', '', 'nấu, rửa, giặt,', 'quét, đưa đón'], LBLUE, 11)
s += box(166, 40, 140, 120, ['Phần nghĩ', '', 'nhớ, lên kế hoạch,', 'quyết định, theo dõi'], YELLOW, 11)
s += t(160, 186, 'Phần nghĩ thường bị bỏ quên', 11.5, RED)
add('KHOAH', 2, 'Phần làm và phần nghĩ', 'Mỗi việc nhà có phần làm bằng tay và phần nghĩ: nhớ, lên kế hoạch, quyết định, theo dõi.', s)

# ================= TUẦN 1 =================
add('H1A', 1, 'Bốn bước của phần nghĩ', 'Trước khi làm, có người phải nhận ra việc cần làm, nghĩ cách, chọn cách, rồi theo dõi.',
    t(160, 28, 'Phần nghĩ của một việc', 14) + flow([['Nhận ra', 'việc cần'], ['Nghĩ', 'các cách'], ['Chọn', 'một cách'], ['Theo dõi', 'xong chưa']],
    52, 70, 8, 312, 10, 10.5, [SAND, LBLUE, YELLOW, G]) + t(160, 146, 'Ví dụ: "Sắp hết sữa của con"', 11.5, NAVY, '600')
    + t(160, 168, '→ mua ở đâu → mua loại nào → đã mua chưa', 11, GRAY, '500'))
s = t(160, 22, 'Ai đang làm bao nhiêu giờ mỗi tuần?', 13.5)
for i, (lab, h, c) in enumerate([('Bố', 0.35, BLUE), ('Mẹ', 0.8, PINK), ('Con lớn', 0.1, ORANGE), ('Ông bà', 0.3, PURP)]):
    y = 44 + i*36
    s += t(66, y + 16, lab, 11.5, NAVY, '700', 'end') + f'<rect x="76" y="{y}" width="{220*h}" height="24" rx="6" fill="{c}" stroke="{NAVY}" stroke-width="2"/>'
s += t(160, 192, 'Số liệu trong hình chỉ là ví dụ', 10, GRAY, '500')
add('H1A', 2, 'Đếm giờ việc nhà', 'Mỗi người ước số giờ việc nhà mỗi tuần, gồm cả phần nghĩ. Hình chỉ là ví dụ.', s)
s = t(160, 22, 'Săn việc nhà', 14)
s += f'<circle cx="96" cy="100" r="40" fill="{LBLUE}" fill-opacity="0.5" stroke="{NAVY}" stroke-width="5"/><path d="M124 128 l36 36" stroke="{BROWN}" stroke-width="12" stroke-linecap="round"/>'
s += pot(80, 120) + bubble(170, 44, 136, 34, '"Ai nấu cơm tối qua?"', 10.5) + bubble(170, 96, 136, 34, '"Ai giặt áo của con?"', 10.5)
add('H1B', 1, 'Săn việc nhà', 'Con đi quanh nhà, tìm và kể các việc nhà ai đó đã làm cho cả nhà.', s)
s = t(160, 22, 'Con nhỏ cũng giúp được', 14)
s += basket(30, 110, 110, 60, BROWN) + f'<path d="M60 112 q14 -26 30 0" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>' + t(85, 190, 'Bỏ áo bẩn vào giỏ', 11)
s += kid(240, 170, 0.75, LGREEN) + t(240, 190, 'Con 2 tuổi', 11)
add('H1B', 2, 'Con nhỏ giúp việc', 'Trẻ 2 tuổi thường muốn giúp người lớn. Cho con làm phần nhỏ, an toàn.', s)

# ================= TUẦN 2 =================
s = t(160, 22, 'Người lo trọn việc', 14)
s += box(14, 40, 292, 34, 'Việc: sữa và đồ ăn sáng của con', SAND, 11.5)
for i, (st, c) in enumerate([('Nhận ra', LBLUE), ('Nghĩ', LBLUE), ('Chọn', LBLUE), ('Làm', G), ('Theo dõi', LBLUE)]):
    x = 14 + i*59
    s += box(x, 92, 54, 34, st, c, 10.5, rx=6)
s += f'<path d="M14 136 h292" stroke="{ORANGE}" stroke-width="3"/>' + t(160, 156, 'Một người lo cả 5 bước', 12, GREEN, '700') + t(160, 178, 'Không phải chờ người khác nhắc', 11, NAVY, '500')
add('H2A', 1, 'Người lo trọn việc', 'Chia việc theo "người lo trọn": người đó lo từ nhận ra đến theo dõi, không chỉ làm theo lời nhắc.', s)
s = t(160, 22, 'Công bằng không phải chia đôi', 14)
s += f'<path d="M160 50 v100" stroke="{NAVY}" stroke-width="4"/><path d="M80 70 h160" stroke="{NAVY}" stroke-width="4"/>'
s += f'<path d="M60 70 l-20 40 h40z M260 70 l-20 40 h40z" fill="{SAND}" stroke="{NAVY}" stroke-width="2"/>'
s += t(60, 130, 'giờ đi làm', 10.5) + t(260, 130, 'giờ việc nhà', 10.5) + f'<rect x="130" y="150" width="60" height="12" rx="4" fill="{BROWN}"/>'
s += t(160, 186, 'Tính cả giờ đi làm, sức khỏe, công tác', 11, GREEN)
add('H2A', 2, 'Công bằng không phải chia đôi', 'Công bằng là tổng công sức hợp lý, tính cả giờ đi làm, sức khỏe và những tuần đi công tác.', s)
add('H2B', 1, 'Dạy việc bốn bước', 'Bố mẹ làm mẫu, rồi làm cùng, rồi con làm có người xem, cuối cùng con tự làm.',
    t(160, 28, 'Dạy một việc mới', 14) + flow([['Bố mẹ', 'làm,', 'con xem'], ['Cùng', 'làm'], ['Con làm,', 'bố mẹ', 'xem'], ['Con tự', 'làm']],
    52, 80, 8, 312, 10, 10.5, [SAND, YELLOW, LBLUE, G]) + t(160, 160, 'Mỗi bước có thể mất vài ngày', 11.5, GREEN))
s = t(160, 22, 'Bảng việc của con', 14) + paper(30, 34, 260, 156)
for i, (job, n) in enumerate([('Dọn bàn sau bữa', 5), ('Tưới cây', 4), ('Cất đồ chơi (em)', 3)]):
    y = 66 + i*40
    s += t(46, y + 4, job, 11.5, NAVY, '700', 'start') + ''.join(star(170 + k*17, y, 7) for k in range(n)) + ''.join(f'<circle cx="{170 + k*17}" cy="{y}" r="6" fill="none" stroke="{LGRAY}" stroke-width="2"/>' for k in range(n, 7))
add('H2B', 2, 'Bảng việc của con', 'Mỗi con một vài việc hằng ngày. Làm xong thì tự vẽ ngôi sao.', s)

# ================= TUẦN 3 =================
s = t(160, 22, 'Khi con làm chưa khéo', 14)
s += box(14, 40, 140, 70, ['Làm lại trước', 'mặt con'], LGRAY, 11) + t(84, 128, 'Con nghĩ: "mình', 10.5, RED) + t(84, 144, 'làm cũng vô ích"', 10.5, RED)
s += box(166, 40, 140, 70, ['Khen phần làm được,', 'chỉ một bước'], G, 11) + check(226, 132) + t(236, 170, 'Lần sau con giỏi hơn', 10.5, GREEN)
add('H3A', 1, 'Chấp nhận chưa hoàn hảo', 'Không làm lại trước mặt con. Khen phần làm được và chỉ thêm một bước.', s)
s = t(160, 22, 'Việc nhà và tiền', 14)
s += box(14, 44, 140, 84, ['Việc chung', '(dọn bàn, cất đồ)', '', 'Không trả tiền'], LBLUE, 10.5)
s += box(166, 44, 140, 84, ['Việc thêm', '(rửa xe, nhổ cỏ)', '', 'Nhà tự quyết'], YELLOW, 10.5)
s += t(160, 160, 'Việc chung là phần của mỗi người trong nhà', 11, GREEN) + t(160, 182, 'Mỗi nhà một cách; bằng chứng chưa rõ', 9.5, GRAY, '500')
add('H3A', 2, 'Việc nhà và tiền', 'Gợi ý: việc chung không trả tiền vì là phần của mỗi người. Việc thêm thì mỗi nhà tự quyết.', s)
s = t(160, 22, 'Mười phút dọn nhà', 14)
s += f'<circle cx="80" cy="104" r="50" fill="{WHITE}" stroke="{NAVY}" stroke-width="4"/><path d="M80 104 L80 66 M80 104 L104 118" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/>'
s += t(80, 176, '10 phút', 13, NAVY, '800')
s += f'<path d="M180 60 q10 -14 20 0 v28" stroke="{NAVY}" stroke-width="3" fill="none"/><circle cx="196" cy="90" r="8" fill="{NAVY}"/><path d="M220 54 q10 -14 20 0 v28" stroke="{NAVY}" stroke-width="3" fill="none"/><circle cx="236" cy="84" r="8" fill="{NAVY}"/>'
s += t(220, 130, 'Bật nhạc, cả nhà', 11.5) + t(220, 148, 'cùng dọn đến khi', 11.5) + t(220, 166, 'hết bài', 11.5)
add('H3B', 1, 'Mười phút dọn nhà', 'Hẹn giờ 10 phút, bật một bài nhạc vui, cả nhà cùng dọn.', s)
s = t(160, 22, 'Mỗi người một khu', 14)
for i, (lab, c, who) in enumerate([('Phòng khách', LBLUE, 'Bố'), ('Bếp', YELLOW, 'Mẹ'), ('Góc đồ chơi', G, 'Con lớn'), ('Rổ dép', PINK, 'Con nhỏ')]):
    x = 14 + (i % 2)*150; y = 40 + (i // 2)*72
    s += box(x, y, 142, 62, [lab, who], c, 11)
add('H3B', 2, 'Mỗi người một khu', 'Chia nhà thành khu nhỏ, mỗi người một khu hợp sức mình.', s)

# ================= TUẦN 4 =================
add('H4A', 1, 'Xem lại phân công', 'Mỗi tháng xem lại: ai đang quá tải, việc nào bị quên, việc nào con đã tự làm được.',
    t(160, 22, 'Vòng một tháng', 14) + cycle([['Chia', 'việc'], ['Làm cả', 'tháng'], ['Xem lại', '10 phút'], ['Đổi', 'một việc']], 160, 118, 64, 88, 34, 10.5, [YELLOW, LBLUE, G, PINK]))
s = t(160, 22, 'Khi một người quá tải', 14)
for i, (q, c) in enumerate([('Việc nào bỏ được?', LGRAY), ('Việc nào làm đơn giản hơn?', LBLUE), ('Việc nào chuyển cho người khác?', YELLOW), ('Việc nào nhờ ngoài được?', G)]):
    y = 40 + i*36
    s += num(28, y + 14, i + 1) + box(46, y, 260, 28, q, c, 11)
add('H4A', 2, 'Khi một người quá tải', 'Bốn câu hỏi theo thứ tự: bỏ, làm đơn giản, chuyển, nhờ ngoài.', s)
s = t(160, 22, 'Thẻ cảm ơn', 14)
for i, (txt, c) in enumerate([('Cảm ơn mẹ nấu canh', PINK), ('Cảm ơn con dọn bàn', YELLOW), ('Cảm ơn bố sửa quạt', LBLUE)]):
    x = 18 + i*100
    s += f'<rect x="{x}" y="{50 + (i % 2)*20}" width="88" height="100" rx="8" fill="{c}" stroke="{NAVY}" stroke-width="2.5" transform="rotate({-5 + i*5} {x+44} 100)"/>'
    s += heart(x + 44, 80 + (i % 2)*20, 1.4) + t(x + 44, 118 + (i % 2)*20, txt.split(' ', 2)[0] + ' ' + txt.split(' ', 2)[1], 10) + t(x + 44, 134 + (i % 2)*20, txt.split(' ', 2)[2], 10)
add('H4B', 1, 'Thẻ cảm ơn', 'Mỗi người viết hoặc vẽ thẻ cảm ơn cho một việc nhà người khác đã làm.', s)
s = t(160, 22, 'Bảng "Ai lo việc gì" của nhà mình', 13.5) + paper(24, 34, 272, 156)
for i, (job, who) in enumerate([('Đi chợ, thực đơn', 'Mẹ'), ('Giặt, phơi đồ', 'Bố'), ('Đưa đón con', 'Bố + ông'), ('Dọn bàn', 'Con lớn'), ('Cất dép', 'Con nhỏ')]):
    y = 58 + i*26
    s += t(42, y, job, 11, NAVY, '600', 'start') + t(278, y, who, 11, GREEN, '700', 'end')
add('H4B', 2, 'Ai lo việc gì', 'Bảng phân công dán ở chỗ ai cũng thấy. Ví dụ trong hình, mỗi nhà một khác.', s)

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('H', 'KHOAH'))), 'hình G7')
