# Hình minh họa và sơ đồ khóa G1 "Giá trị nhà mình"
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'

def house(cx, base, w, roof_txt, cols, floor_txt, size=10.5):
    """Mái nhà giá trị: mái = giá trị, cột = việc làm, nền = nội quy + họp."""
    x0 = cx - w/2
    s = f'<path d="M{x0-10} {base-100} L{cx} {base-150} L{x0+w+10} {base-100} Z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
    s += t(cx, base-112, roof_txt, size+1, WHITE, '700')
    n = len(cols); cw = (w - 8*(n+1)) / n
    for i, c in enumerate(cols):
        x = x0 + 8 + i*(cw+8)
        s += box(x, base-96, cw, 70, c, YELLOW if i % 2 == 0 else LBLUE, size-1, rx=4)
    s += box(x0-10, base-22, w+20, 24, floor_txt, G, size, rx=4)
    return s

def kid(x, y, s=1, shirt=ORANGE): return person(x, y, s, shirt, False)

# ================= TRANG KHÓA =================
add('KHOAV', 1, 'Lộ trình 4 tuần', 'Mỗi tuần một bước: chọn giá trị, biến thành việc làm, đặt nội quy, rồi họp gia đình thành nếp.',
    t(160, 30, 'Bốn tuần, bốn bước', 14) + flow([['Tuần 1', 'Chọn', 'giá trị'], ['Tuần 2', 'Thành', 'việc làm'], ['Tuần 3', 'Nội quy', 'nhà mình'], ['Tuần 4', 'Họp gia', 'đình 15\'']],
    58, 80, 8, 312, 10, 10.5, [YELLOW, LBLUE, G, PURP]) + t(160, 166, 'Mỗi tuần: 1 buổi bố mẹ + 1 buổi cả nhà', 12, GREEN))
add('KHOAV', 2, 'Mái nhà giá trị', 'Giá trị là mái che. Việc làm hằng ngày là cột. Nội quy và họp gia đình là nền giữ cho nhà vững.',
    house(160, 186, 220, 'Giá trị nhà mình', [['Việc', 'con', 'làm'], ['Việc', 'bố mẹ', 'làm'], ['Lời', 'khen', 'đúng lúc']], 'Nội quy + họp gia đình mỗi tuần'))

# ================= TUẦN 1 =================
add('V1A', 1, 'Bốn bước chọn giá trị', 'Mỗi người tự nhớ và tự chọn trước, rồi mới so sánh và chốt 3–5 giá trị chung.',
    t(160, 30, 'Chọn giá trị trong 30 phút', 14) + flow([['Nhớ lại', 'lúc tự hào'], ['Mỗi người', 'chọn 5', 'thẻ'], ['So sánh,', 'hỏi', '"vì sao?"'], ['Chốt', '3–5', 'giá trị']],
    60, 78, 8, 312, 10, 10.5, [SAND, YELLOW, LBLUE, G]) + t(160, 166, 'Tự chọn trước khi bàn, để ai cũng có tiếng nói', 11.5, GREEN))
s = t(160, 24, 'Bố chọn – Mẹ chọn – Chung', 14)
s += f'<circle cx="132" cy="112" r="78" fill="{LBLUE}" fill-opacity="0.55" stroke="{NAVY}" stroke-width="2.5"/>'
s += f'<circle cx="188" cy="112" r="78" fill="{PINK}" fill-opacity="0.55" stroke="{NAVY}" stroke-width="2.5"/>'
s += t(80, 104, 'Chăm chỉ', 10) + t(80, 126, 'Tiết kiệm', 10) + t(240, 104, 'Vui vẻ', 10) + t(240, 126, 'Sáng tạo', 10)
s += t(160, 92, 'Trung thực', 10.5, NAVY, '700') + t(160, 112, 'Tử tế', 10.5, NAVY, '700') + t(160, 132, 'Trách nhiệm', 10.5, NAVY, '700')
s += t(36, 52, 'Bố', 13) + t(284, 52, 'Mẹ', 13)
add('V1A', 2, 'Phần chung của hai người', 'Giá trị cả hai cùng chọn là điểm bắt đầu. Giá trị khác nhau thì hỏi nhau "vì sao điều này quan trọng?"', s)
s = t(160, 26, 'Đổi từ khó thành lời con hiểu', 14)
for i, (a, b) in enumerate([('Trách nhiệm', 'Việc của mình, mình làm'), ('Trung thực', 'Nói thật, kể cả khi lỡ sai'), ('Tử tế', 'Nhẹ tay, nhẹ lời với nhau')]):
    y = 48 + i*48
    s += box(14, y, 96, 34, a, YELLOW, 11) + arrow(114, y+17, 136, y+17, ORANGE, 3) + box(140, y, 166, 34, b, WHITE, 11)
add('V1A', 3, 'Lời con hiểu', 'Mỗi giá trị có một câu ngắn mà con 7 tuổi nói lại được.', s)

add('V1B', 1, 'Mái nhà giá trị của con', 'Con lớn vẽ ngôi nhà, ghi hoặc vẽ mỗi giá trị lên mái. Cả nhà dán ở chỗ dễ thấy.',
    house(160, 186, 220, 'Nhà mình', [['Nói', 'thật'], ['Nhẹ', 'tay'], ['Tự', 'làm'], ['Cảm', 'ơn']], 'Cả nhà cùng giữ') )
s = t(160, 24, 'Mỗi giá trị một động tác', 14)
for i, (lab, g) in enumerate([('Nói thật', f'<path d="M-10 -4 C-22 -16 -20 -26 -10 -20 L0 -12 L10 -20 C20 -26 22 -16 10 -4 L0 6Z" fill="{PINK}" stroke="{NAVY}" stroke-width="2"/><path d="M-22 8 q22 -6 44 0" stroke="{BROWN}" stroke-width="7" stroke-linecap="round" fill="none"/>'),
                              ('Nhẹ tay', f'<path d="M-24 0 q12 -18 24 -4 q12 -14 24 4" stroke="{BROWN}" stroke-width="7" stroke-linecap="round" fill="none"/><circle cx="0" cy="-22" r="8" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2"/>'),
                              ('Tự làm', f'<rect x="-8" y="-24" width="16" height="30" rx="7" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/><rect x="-14" y="2" width="28" height="16" rx="6" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>')]):
    cx = 60 + i*100
    s += f'<circle cx="{cx}" cy="100" r="40" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/><g transform="translate({cx} 108)">{g}</g>' + t(cx, 162, lab, 12)
s += t(160, 188, 'Con nhỏ làm động tác thay cho lời', 11, GREEN)
add('V1B', 2, 'Động tác cho con nhỏ', 'Con 2 tuổi chưa nói được từ khó. Mỗi giá trị gắn một động tác: tay đặt lên ngực, vuốt nhẹ, giơ ngón cái.', s)
add('V1B', 3, 'Buổi cả nhà 15 phút', 'Bố mẹ kể một chuyện thật, con vẽ, cả nhà dán lên tường và hỏi nhau.',
    t(160, 30, 'Buổi cả nhà 15 phút', 14) + flow([['Kể', 'chuyện', 'thật'], ['Con', 'vẽ nhà'], ['Dán', 'lên', 'tường'], ['"Ai đã', 'làm điều', 'này?"']],
    60, 78, 8, 312, 10, 10.5, [SAND, YELLOW, G, LBLUE]) + t(160, 166, 'Không giảng giải dài. Chuyện thật dễ nhớ hơn', 11.5, GREEN))

# ================= TUẦN 2 =================
s = t(160, 22, 'Từ giá trị đến việc thấy được', 14)
s += box(110, 36, 100, 30, 'Trung thực', YELLOW, 12)
s += arrow(140, 68, 90, 92, ORANGE, 3) + arrow(180, 68, 230, 92, ORANGE, 3)
s += box(14, 96, 140, 58, ['Con: tự nói khi', 'làm đổ, làm hỏng'], LBLUE, 10.5)
s += box(166, 96, 140, 58, ['Bố mẹ: nhận khi', 'mình nói sai'], PINK, 10.5)
s += t(160, 180, 'Ai cũng nhìn thấy, ai cũng đếm được', 11.5, GREEN)
add('V2A', 1, 'Giá trị thành hành vi', 'Mỗi giá trị viết 2 việc con làm và 2 việc bố mẹ làm. Việc phải nhìn thấy được.', s)
s = t(160, 26, 'Kế hoạch "Nếu… thì…"', 14)
s += box(14, 46, 292, 44, ['Nếu con làm đổ nước và nói thật,'], LBLUE, 12)
s += arrow(160, 92, 160, 110, ORANGE, 3)
s += box(14, 114, 292, 44, ['thì bố mẹ nói: "Cảm ơn con đã nói thật.', 'Mình lau cùng nhé."'], G, 11.5)
s += t(160, 182, 'Nghĩ trước câu nói, lúc bực vẫn nói đúng', 11.5, GREEN)
add('V2A', 2, 'Nếu… thì…', 'Viết trước câu sẽ nói trong tình huống hay gặp. Lúc bực, mình đã có sẵn câu đúng.', s)
add('V2A', 3, 'Con nhận giá trị thế nào', 'Theo một mô hình lý thuyết: con cần hiểu đúng điều bố mẹ muốn, rồi thấy điều đó hợp lý, mới tự làm theo.',
    t(160, 30, 'Con nhận giá trị thế nào', 14) + flow([['Con hiểu', 'đúng điều', 'bố mẹ muốn'], ['Con thấy', 'hợp lý,', 'công bằng'], ['Con tự', 'làm theo']],
    58, 80, 10, 310, 16, 10.5, [LBLUE, YELLOW, G]) + t(160, 160, 'Giải thích "vì sao" + làm gương', 12, GREEN) + t(160, 182, 'Mô hình lý thuyết, đơn giản hóa', 9.5, GRAY, '500'))

s = t(160, 24, 'Thám tử giá trị', 14)
s += f'<circle cx="96" cy="104" r="40" fill="{LBLUE}" fill-opacity="0.5" stroke="{NAVY}" stroke-width="5"/><path d="M124 132 l36 36" stroke="{BROWN}" stroke-width="12" stroke-linecap="round"/>'
s += kid(96, 132, 0.62, ORANGE) + bubble(176, 48, 130, 34, '"Con thấy em cất dép!"', 10.5)
s += dino(250, 166, 0.7)
add('V2B', 1, 'Thám tử giá trị', 'Cả tuần, ai thấy người khác làm đúng giá trị thì kể ra. Không ai đi "bắt lỗi".', s)
s = t(160, 24, 'Bảng "Nhà mình đã thấy"', 14)
s += paper(30, 36, 260, 150)
for i, (v, c) in enumerate([('Nói thật', 3), ('Nhẹ tay', 2), ('Tự làm', 4), ('Cảm ơn', 5)]):
    y = 60 + i*32
    s += t(56, y+5, v, 11, NAVY, '700', 'start')
    for k in range(c): s += star(150 + k*26, y, 9)
add('V2B', 2, 'Bảng ghi nhận', 'Mỗi lần thấy một việc tốt, vẽ một ngôi sao vào dòng của giá trị đó.', s)
s = t(160, 24, 'Đóng vai: con chọn cách nào?', 14)
s += box(14, 40, 292, 32, 'Con lỡ làm vỡ cốc của mẹ', SAND, 12)
s += arrow(100, 74, 80, 94, ORANGE, 3) + arrow(220, 74, 240, 94, ORANGE, 3)
s += box(14, 98, 140, 52, ['Giấu đi,', 'không nói'], LGRAY, 11) + box(166, 98, 140, 52, ['Nói thật,', 'cùng dọn'], G, 11)
s += check(236, 164) + t(160, 190, 'Hỏi con: cách nào giống nhà mình?', 11.5, GREEN)
add('V2B', 3, 'Tình huống đóng vai', 'Kể một tình huống, con chọn cách làm hợp với giá trị nhà mình.', s)

# ================= TUẦN 3 =================
add('V3A', 1, 'Công thức một nội quy', 'Mỗi nội quy đi ra từ một giá trị, nói điều cần làm, có lời khen và một hậu quả nhỏ báo trước.',
    t(160, 28, 'Công thức một nội quy', 14) + flow([['Giá trị'], ['Luật nói', 'điều', 'cần làm'], ['Khen khi', 'làm đúng'], ['Hậu quả', 'nhỏ, báo', 'trước']],
    54, 80, 8, 312, 10, 10.5, [YELLOW, LBLUE, G, SAND]) + t(160, 160, 'Con nhỏ: 2–3 luật một lúc', 12, GREEN) + t(160, 180, 'Theo hướng dẫn CDC cho trẻ 2–4 tuổi', 9.5, GRAY, '500'))
s = t(160, 26, 'Nói điều cần làm', 14)
for i, (a, b) in enumerate([('Không đánh em', 'Tay nhẹ nhàng với em'), ('Không bừa bộn', 'Chơi xong, cất về rổ'), ('Không la hét', 'Trong nhà nói nhỏ')]):
    y = 46 + i*48
    s += box(14, y, 110, 34, a, LGRAY, 11) + arrow(128, y+17, 150, y+17, ORANGE, 3) + box(154, y, 152, 34, b, G, 11)
add('V3A', 2, 'Đổi "Không…" thành điều cần làm', 'Câu "không…" chỉ nói điều cấm. Con cần biết phải làm gì thay vào.', s)
s = t(160, 24, 'Mọi người lớn, cùng một luật', 14)
for i, (sh, lab) in enumerate([(BLUE, 'Bố'), (PINK, 'Mẹ'), (PURP, 'Ông bà')]):
    x = 70 + i*90
    s += person(x, 150, 0.8, sh) + t(x, 172, lab, 12)
s += box(40, 30, 240, 28, '"Chơi xong, cất về rổ"', YELLOW, 11.5)
s += t(160, 192, 'Luật giống nhau, con không bị rối', 11.5, GREEN)
add('V3A', 3, 'Người lớn thống nhất', 'Bố, mẹ, ông bà và người chăm con dùng cùng một luật và cùng cách nhắc.', s)

s = t(160, 22, 'Nội quy nhà mình', 14) + paper(40, 32, 240, 160)
for i, (rule, icon) in enumerate([('Tay nhẹ nhàng', heart(80, 66, 1.2)), ('Chơi xong, cất về rổ', f'<path d="M66 98 h28 l-4 20 h-20z" fill="{BROWN}" stroke="{NAVY}" stroke-width="2"/><circle cx="80" cy="94" r="6" fill="{RED}" stroke="{NAVY}" stroke-width="1.5"/>'), ('Nói thật khi lỡ sai', face(80, 150, 12, 'vui'))]):
    y = 66 + i*42
    s += icon + t(108, y+5, rule, 12, NAVY, '700', 'start')
add('V3B', 1, 'Bảng nội quy có tranh', 'Mỗi luật có một hình nhỏ để con chưa biết đọc vẫn nhớ.', s)
s = t(160, 24, 'Cả nhà in dấu tay', 14) + paper(50, 36, 220, 150)
for i, (x, sc, c) in enumerate([(100, 1.0, BLUE), (160, 1.0, PINK), (220, 0.8, ORANGE), (130, 0.6, LGREEN)]):
    y = 100 if i < 3 else 152
    s += f'<g transform="translate({x} {y}) scale({sc})"><ellipse cx="0" cy="8" rx="16" ry="18" fill="{c}" stroke="{NAVY}" stroke-width="1.5"/>' + ''.join(f'<rect x="{-17+k*8}" y="-24" width="7" height="20" rx="3.5" fill="{c}" stroke="{NAVY}" stroke-width="1.5"/>' for k in range(4)) + f'<rect x="12" y="0" width="7" height="16" rx="3.5" fill="{c}" stroke="{NAVY}" stroke-width="1.5" transform="rotate(-30 15 8)"/></g>'
s += t(190, 160, 'Cả nhà đồng ý', 11.5, GREEN)
add('V3B', 2, 'In dấu tay đồng ý', 'Mỗi người in dấu tay bằng màu nước rửa được. Con nhỏ cũng tham gia.', s)
add('V3B', 3, 'Nhắc luật bằng một câu', 'Khi con quên luật, bố mẹ nhắc bằng một câu ngắn, giọng bình tĩnh, rồi chờ.',
    t(160, 30, 'Khi con quên luật', 14) + flow([['Lại gần,', 'nhìn con'], ['Một câu:', '"Luật nhà', 'mình là…"'], ['Chờ', '5 giây'], ['Con làm:', 'khen', 'ngay']],
    56, 82, 8, 312, 10, 10.5, [SAND, YELLOW, LBLUE, G]) + t(160, 166, 'Không giảng, không dọa, không đánh', 12, RED))

# ================= TUẦN 4 =================
s = t(160, 22, 'Họp gia đình 15 phút', 14)
parts = [('Cảm ơn', '3\'', PINK), ('Nhìn lại', '3\'', LBLUE), ('1 chuyện', '4\'', YELLOW), ('Kế hoạch', '3\'', G), ('Vui', '2\'', PURP)]
x = 12
for lab, m, c in parts:
    w = 296 * int(m[0]) / 15
    s += box(x, 50, w - 4, 70, [lab, m], c, 10.5, rx=6)
    x += w
s += t(160, 150, 'Giờ cố định, ví dụ tối Chủ nhật', 12, GREEN) + t(160, 172, 'Ngắn và đều quan trọng hơn dài', 11, NAVY, '500')
add('V4A', 1, 'Năm phần của cuộc họp', 'Cảm ơn, nhìn lại tuần, giải quyết một chuyện, lên kế hoạch, rồi kết thúc bằng một trò vui.', s)
s = t(160, 24, 'Luật của cuộc họp', 14)
for i, r in enumerate(['Một người nói, cả nhà nghe', 'Không chê, không trách', 'Chuyện khó: bố mẹ bàn riêng trước', 'Hết giờ là dừng']):
    y = 42 + i*36
    s += num(28, y+14, i+1) + box(46, y, 260, 28, r, WHITE, 11)
add('V4A', 2, 'Bốn luật họp', 'Luật ngắn để cuộc họp an toàn và vui, không thành buổi xử phạt.', s)
add('V4A', 3, 'Vòng một tuần', 'Họp, làm cả tuần, ghi nhận việc tốt, rồi họp lại. Mỗi vòng giỏi hơn một chút.',
    t(160, 22, 'Vòng một tuần', 14) + cycle([['Họp', 'Chủ nhật'], ['Làm cả', 'tuần'], ['Ghi nhận', 'việc tốt'], ['Sửa', 'một điều']], 160, 112, 64, 88, 34, 10.5, [YELLOW, LBLUE, G, PINK]))

s = t(160, 22, 'Cả nhà ngồi vòng tròn', 14)
s += f'<ellipse cx="160" cy="130" rx="100" ry="34" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>'
s += person(80, 120, 0.7, BLUE) + person(240, 120, 0.7, PINK) + kid(130, 116, 0.75, ORANGE) + kid(190, 112, 0.6, LGREEN)
s += f'<rect x="124" y="70" width="6" height="40" rx="3" fill="{BROWN}" transform="rotate(20 127 90)"/>' + t(160, 186, 'Ai cầm gậy thì nói', 11.5, GREEN)
add('V4B', 1, 'Cuộc họp đầu tiên', 'Cả nhà ngồi ngang tầm nhau. Ai cầm gậy nói chuyện thì nói, người khác nghe.', s)
s = t(160, 22, 'Biên bản họp', 14) + paper(50, 32, 220, 160)
for i, r in enumerate(['Cảm ơn: ……………', 'Tuần qua: ……………', 'Chuyện cần giải quyết: ……', 'Kế hoạch tuần: ……………', 'Trò vui: ……………']):
    s += t(68, 60 + i*28, r, 11, NAVY, '600', 'start')
add('V4B', 2, 'Biên bản họp gia đình', 'Con lớn làm "thư ký": ghi hoặc vẽ một dòng cho mỗi phần.', s)
add('V4B', 3, 'Mái nhà hoàn thành', 'Sau 4 tuần, nhà mình có đủ giá trị, việc làm, nội quy và nếp họp.',
    house(160, 186, 220, 'Giá trị nhà mình', [['Tuần 2', 'Việc', 'làm'], ['Tuần 3', 'Nội', 'quy'], ['Tuần 4', 'Họp', 'tuần']], 'Giữ đều mỗi tuần') + star(286, 42, 12) + star(34, 52, 10))

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('V', 'KHOAV'))), 'hình G1')
