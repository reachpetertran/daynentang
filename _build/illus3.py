# Hình minh họa và sơ đồ tuần 9–12
import math
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'

# ================= TUẦN 9 =================
s = t(160, 22, 'Cây cần gì – con cần gì', 14)
s += pot(70, 150) + t(70, 172, 'Cây', 12) + f'<circle cx="250" cy="96" r="16" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/><path d="M234 114 h32 l4 40 h-40z" fill="{GREEN}" stroke="{NAVY}" stroke-width="2.5"/>' + t(250, 172, 'Con', 12)
for i, (a, b) in enumerate([('Nước', 'Ăn uống'), ('Nắng', 'Vận động'), ('Đất tốt', 'Giấc ngủ')]):
    y = 56 + i*36
    s += box(108, y, 52, 26, a, LBLUE, 10.5) + arrow(162, y+13, 176, y+13, ORANGE, 2.5) + box(178, y, 58, 26, b, YELLOW, 10.5)
add('T9', 1, 'Cây cần gì – con cần gì', 'Cây cần nước, nắng, đất tốt. Con cần ăn uống, vận động và ngủ đủ.', s)
add('T9', 2, 'Nếp trước giờ ngủ', 'Bốn bước giống nhau mỗi tối giúp con dễ ngủ đúng giờ.',
    t(160, 30, 'Nếp trước giờ ngủ', 14) + flow([['Tắm,', 'thay đồ'], ['Đánh', 'răng'], ['Đọc', 'truyện'], ['Tắt đèn,', 'chúc ngủ', 'ngon']], 56, 74, 8, 312, 10, 10.5,
    [LBLUE, WHITE, YELLOW, '#c9b6e8']) + t(160, 160, 'Cùng giờ mỗi tối, kể cả cuối tuần', 12, GREEN))
s = t(160, 22, 'Ngủ bao lâu mỗi ngày?', 14)
for i, (age, hrs, h) in enumerate([('1–2 tuổi', '11–14 giờ', 120), ('3–5 tuổi', '10–13 giờ', 106), ('6–12 tuổi', '9–12 giờ', 94)]):
    x = 50 + i*90
    s += f'<rect x="{x}" y="{170-h}" width="50" height="{h}" rx="6" fill="#c9b6e8" stroke="{NAVY}" stroke-width="2"/>' + t(x+25, 186, age, 11) + t(x+25, 164-h, hrs, 11, NAVY, '700')
s += t(160, 198, 'Theo khuyến nghị AASM 2016 (có tính giấc trưa cho trẻ nhỏ)', 8.5, GRAY, '500')
add('T9', 3, 'Số giờ ngủ khuyến nghị theo tuổi', 'Khuyến nghị số giờ ngủ trong 24 giờ theo Học viện Y học Giấc ngủ Hoa Kỳ (AASM).', s)

add('K9', 1, 'Hóa thạch hình thành thế nào', 'Sơ đồ đơn giản: con vật được bùn phủ kín, rất lâu sau thành đá, rồi người tìm thấy.',
    t(160, 30, 'Hóa thạch (rất đơn giản)', 14) + flow([['Con vật', 'mất đi'], ['Bùn, cát', 'phủ kín'], ['Rất lâu', 'thành đá'], ['Người', 'đào thấy']], 60, 66, 8, 312, 10, 10.5,
    [G, SAND, LGRAY, YELLOW]) + t(160, 160, 'Mất hàng triệu năm, không phải vài ngày', 11.5, RED))
s = t(160, 22, 'Nhìn dấu – đoán vật', 14)
s += f'<ellipse cx="80" cy="110" rx="56" ry="40" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/>'
s += f'<path d="M64 96 l6 22 m10 -24 l2 24 m10 -22 l-4 22" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>' + arrow(144, 110, 186, 110, ORANGE, 3)
s += f'<rect x="196" y="74" width="100" height="72" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>' + t(246, 104, 'Dấu 3 ngón', 11) + t(246, 122, '→ chân chim?', 11, GREEN)
s += t(80, 170, 'đất nặn có dấu', 11)
add('K9', 2, 'Nhìn dấu đoán vật', 'Nhà khoa học nhìn dấu vết để đoán con vật. Con cũng làm như vậy với đất nặn.', s)
s = f'<ellipse cx="100" cy="110" rx="70" ry="52" fill="{SAND}" stroke="{NAVY}" stroke-width="3"/>'
s += f'<path d="M80 92 q-6 -16 6 -18 q10 2 6 18 M100 86 q0 -18 10 -18 q10 2 4 20 M118 96 q8 -14 16 -8 q4 8 -10 14" fill="none" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/><ellipse cx="102" cy="120" rx="20" ry="14" fill="none" stroke="{BROWN}" stroke-width="4"/>'
s += f'<ellipse cx="236" cy="110" rx="56" ry="44" fill="{SAND}" stroke="{NAVY}" stroke-width="3"/><path d="M216 130 q20 -50 40 0 M236 92 v40 M236 106 l-10 -8 M236 114 l10 -8" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"/>'
s += t(100, 182, 'dấu chân khủng long đồ chơi', 11) + t(236, 182, 'dấu chiếc lá', 11) + t(160, 26, 'In dấu trên đất nặn', 14)
add('K9', 3, 'Dấu chân và dấu lá', 'Ấn chân khủng long đồ chơi và chiếc lá lên đất nặn để tạo "hóa thạch".', s)

add('G9', 1, 'Năm bước ăn chậm', 'Ăn một miếng chuối thật chậm: nhìn, ngửi, sờ, cắn nhỏ, nhai và kể.',
    t(160, 30, 'Ăn chậm một miếng', 14) + flow([['Nhìn'], ['Ngửi'], ['Sờ'], ['Cắn', 'nhỏ'], ['Nhai,', 'kể lại']], 66, 56, 8, 312, 10, 11,
    [YELLOW, PINK, LBLUE, G, '#c9b6e8']) + t(160, 160, 'Không vội, không nói chuyện trong lúc nhai', 11.5, GREEN))
s = box(16, 62, 132, 76, ['Đi nhanh', 'thấy 1–2 điều'], LGRAY, 12) + box(172, 62, 132, 76, ['Đi chậm', 'thấy nhiều điều hơn'], G, 12)
s += t(160, 34, 'Chậm lại để nhận ra', 14) + t(160, 106, '→', 22, ORANGE) + t(160, 164, '"Con nghe thấy gì? Thấy gì? Chân cảm thấy gì?"', 11)
add('G9', 2, 'Chậm lại để nhận ra', 'Khi chậm lại, con nhận ra nhiều điều quanh mình hơn.', s)
s = f'<rect x="0" y="160" width="320" height="40" fill="{G}"/>' + dino(110, 160, 0.85) + ''.join(f'<ellipse cx="{170+k*30}" cy="{168+(k%2)*6}" rx="7" ry="4" fill="{GREEN}" opacity=".6"/>' for k in range(5))
s += sun(270, 46, 12) + t(110, 34, 'Tí đi thật chậm…', 13) + bubble(150, 60, 120, 32, '"Nghe chim hót!"', 11.5)
add('G9', 3, 'Tí đi bộ chậm', 'Tí đi thật chậm trong vườn và kể điều mình nghe, thấy.', s)

# ================= TUẦN 10 =================
s = f'<rect x="20" y="40" width="280" height="140" rx="12" fill="#f4ecff" stroke="{NAVY}" stroke-width="2.5"/>'
s += f'<ellipse cx="90" cy="150" rx="46" ry="18" fill="{PINK}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="160" cy="130" r="18" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>'
s += f'<rect x="200" y="70" width="80" height="54" rx="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>' + t(240, 92, 'Thở', 11) + t(240, 108, 'Ôm gối', 11)
s += face(70, 84, 18, 'vui') + face(120, 84, 18, 'gian') + t(160, 30, 'Góc bình tĩnh', 15)
add('T10', 1, 'Góc bình tĩnh', 'Một góc nhỏ có gối ôm, thẻ cảm xúc, thẻ cách bình tĩnh. Đây không phải chỗ phạt.', s)
add('T10', 2, 'Đường đi của cơn giận', 'Thấy giận → đến góc bình tĩnh → thở, ôm gối → quay lại nói → cùng giải quyết.',
    t(160, 30, 'Khi con giận', 14) + flow([['Thấy', 'giận'], ['Đến góc', 'bình tĩnh'], ['Thở,', 'ôm gối'], ['Quay lại', 'nói'], ['Cùng', 'giải quyết']], 60, 64, 6, 314, 8, 10,
    ['#f08a6b', '#f4ecff', LBLUE, YELLOW, G]) + t(160, 156, 'Bố mẹ có thể ngồi cùng con', 12, GREEN))
s = f'<rect x="140" y="30" width="40" height="140" rx="20" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><circle cx="160" cy="176" r="20" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>'
levels = [('5', 'Bùng nổ', RED), ('4', 'Rất giận', '#f08a6b'), ('3', 'Bực', ORANGE), ('2', 'Hơi khó chịu', YELLOW), ('1', 'Bình thường', G)]
for i, (n, lab, c) in enumerate(levels):
    y = 40 + i*26
    s += f'<rect x="146" y="{y}" width="28" height="22" fill="{c}"/>' + t(130, y+15, n, 12, NAVY, '800', 'end') + t(190, y+15, lab, 11, NAVY, '600', 'start')
s += t(60, 70, 'Mức 3 trở lên', 11) + t(60, 86, '→ đến góc', 11) + t(60, 102, 'bình tĩnh', 11)
add('T10', 3, 'Nhiệt kế cơn giận', 'Con chỉ mức giận của mình từ 1 đến 5. Từ mức 3 thì dùng góc bình tĩnh.', s)

add('K10', 1, 'Vòng thiết kế của kỹ sư nhí', 'Kỹ sư đi một vòng: hỏi vấn đề, nghĩ cách, làm, thử, rồi sửa cho tốt hơn.',
    t(160, 22, 'Kỹ sư nhí', 14) + cycle([['1. Hỏi'], ['2. Nghĩ', 'và vẽ'], ['3. Làm'], ['4. Thử'], ['5. Sửa']], 160, 112, 72, 70, 32, 11, [YELLOW, PINK, LBLUE, G, '#c9b6e8']))
s = t(160, 22, 'Thuyền nào chở được nhiều hơn?', 13)
for i, (w, wall, lab) in enumerate([(70, 10, 'đáy hẹp, thành thấp'), (110, 24, 'đáy rộng, thành cao')]):
    x = 30 + i*150
    s += f'<rect x="{x}" y="{120-wall}" width="{w}" height="{wall}" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2.5"/>' + f'<rect x="0" y="0" width="0" height="0"/>'
    s += f'<path d="M{x-6} 124 h{w+12}" stroke="{BLUE}" stroke-width="3"/>' + t(x+w/2, 150, lab, 10.5)
    s += ''.join(block(x+6+k*24, 120-wall-14, 20, 12, [RED, YELLOW, BLUE, LGREEN][k%4]) for k in range(2 if i == 0 else 4))
s += t(160, 182, 'Con tự thử để kiểm chứng', 11.5, GREEN)
add('K10', 2, 'Hình dạng thuyền', 'So sánh hai thiết kế. Con đoán trước, rồi thả khối vào để kiểm chứng.', s)
s = basin(60, 100, 200, 70) + f'<path d="M110 106 h80 l-10 16 h-60z" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2.5"/>'
s += block(124, 92, 20, 12, RED) + block(150, 92, 20, 12, BLUE) + t(160, 34, 'Thuyền giấy bạc chở khối', 14) + t(160, 60, 'Đếm: mấy khối thì chìm?', 12, GREEN)
add('K10', 3, 'Thuyền giấy bạc trong chậu', 'Gấp thuyền bằng giấy bạc, thả vào chậu nước nông, xếp khối từng cái.', s)

add('G10', 1, 'Vòng lời hứa', 'Hứa điều nhỏ, làm đúng, nhận ra mình giữ lời, nên mọi người tin nhau hơn.',
    t(160, 22, 'Giữ lời hứa', 14) + cycle([['Hứa', 'điều nhỏ'], ['Làm', 'đúng hẹn'], ['Đánh', 'dấu ✓'], ['Mọi người', 'tin nhau']], 160, 114, 64, 96, 36, 11, [YELLOW, G, LBLUE, PINK]))
s = box(20, 50, 130, 50, ['Bố mẹ giữ lời', '"Chơi xong 5 phút"'], G, 11) + box(170, 50, 130, 50, ['Con tin và chờ', 'được lâu hơn'], YELLOW, 11)
s += arrow(152, 75, 168, 75, ORANGE, 3) + t(160, 32, 'Người lớn giữ lời → con tin', 13)
s += box(20, 120, 130, 50, ['Bố mẹ hay quên', 'lời hứa'], LGRAY, 11) + box(170, 120, 130, 50, ['Con khó tin,', 'muốn có ngay'], LGRAY, 11) + arrow(152, 145, 168, 145, GRAY, 3)
add('G10', 2, 'Giữ lời và lòng tin', 'Khi người lớn giữ lời, trẻ tin hơn và chờ được lâu hơn (xem nguồn).', s)
s = f'<rect x="0" y="160" width="320" height="40" fill="{G}"/>' + dino(100, 160, 0.85) + cat(240, 168, 0.95) + f'<circle cx="170" cy="140" r="12" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>'
s += bubble(130, 26, 170, 36, '"Tớ trả bóng như đã hứa"', 11) + heart(200, 100, 1.3)
add('G10', 3, 'Tí trả bóng như đã hứa', 'Tí mượn bóng và trả đúng hẹn. Mướp tin Tí hơn.', s)

# ================= TUẦN 11 =================
add('T11', 1, 'Kế hoạch chậu rau gia đình', 'Dự án 4 tuần: chọn hạt, chuẩn bị chậu, gieo, chăm mỗi ngày, rồi thu hoạch.',
    t(160, 30, 'Chậu rau gia đình', 14) + flow([['Chọn', 'hạt'], ['Chuẩn bị', 'chậu,', 'đất'], ['Gieo'], ['Chăm', 'mỗi ngày'], ['Thu', 'hoạch']], 60, 64, 6, 314, 8, 10.5,
    [YELLOW, SAND, G, LBLUE, '#f08a6b']) + t(160, 158, 'Rau nhanh lớn: rau cải, rau muống (hỏi người bán hạt)', 10.5, GRAY))
s = t(160, 20, 'Cả bàn tay trong một dự án', 13)
for i, (f, role, c) in enumerate([('Ngón cái', 'Tự tưới cây', YELLOW), ('Ngón trỏ', 'Đặt ngày thu hoạch', LBLUE), ('Ngón giữa', 'Tưới trước, chơi sau', G), ('Áp út', 'Làm cùng em', PINK), ('Ngón út', 'Nghỉ ngơi khi mệt', '#c9b6e8')]):
    y = 32 + i*32
    s += box(20, y, 100, 26, f, c, 11) + arrow(124, y+13, 150, y+13, ORANGE, 2.5) + box(154, y, 150, 26, role, WHITE, 11)
add('T11', 2, 'Năm ngón trong một dự án', 'Mỗi ngón tay là một thói quen dùng trong dự án chậu rau.', s)
s = f'<path d="M100 130 h120 l-12 50 h-96z" fill="{BROWN}" stroke="{NAVY}" stroke-width="3"/><rect x="94" y="122" width="132" height="12" rx="4" fill="#8a5a33" stroke="{NAVY}" stroke-width="2"/>'
s += ''.join(sprout(118+k*21, 122, 30+(k%2)*10) for k in range(5)) + t(160, 34, 'Chậu rau của cả nhà', 14) + sun(270, 50, 12)
add('T11', 3, 'Chậu rau của cả nhà', 'Mỗi người trong nhà có một việc với chậu rau.', s)

add('K11', 1, 'Câu hỏi thử được', 'Biến câu "Vì sao…?" thành câu "Nếu… thì…?" để tự thử được.',
    t(160, 30, 'Câu hỏi thử được', 14) + box(16, 54, 130, 54, ['"Vì sao đá chìm?"', '(khó thử)'], LGRAY, 11) + arrow(150, 81, 170, 81, ORANGE, 3)
    + box(174, 54, 130, 54, ['"Nếu thả đá to và', 'đá nhỏ thì sao?"'], G, 11) + t(160, 140, 'Câu "Nếu… thì…" cho mình làm thí nghiệm', 11.5, GREEN))
add('K11', 2, 'Chu trình câu hỏi của con', 'Con tự hỏi, đoán, thử, kể lại, rồi nảy ra câu hỏi mới.',
    t(160, 22, 'Câu hỏi của con', 14) + cycle([['Con hỏi'], ['Con đoán'], ['Con thử'], ['Con kể'], ['Câu hỏi', 'mới']], 160, 112, 72, 70, 32, 11, [YELLOW, PINK, LBLUE, G, '#c9b6e8']))
s = dino(90, 166, 0.8) + bubble(130, 24, 150, 32, '"Nếu… thì sao?"', 12) + bubble(170, 72, 130, 32, '"Vì sao…?"', 12) + t(250, 140, '?', 40, ORANGE) + f'<rect x="0" y="166" width="320" height="34" fill="{G}"/>'
add('K11', 3, 'Tí đặt câu hỏi', 'Mỗi câu hỏi của con là một thí nghiệm có thể làm.', s)

s = bubble(14, 30, 140, 44, '"Bạn làm lại được mà!"', 11) + bubble(170, 30, 140, 44, '"Mình làm lại được mà!"', 11)
s += t(84, 100, 'Nói với bạn', 12) + t(240, 100, 'Nói với mình', 12) + t(160, 56, '=', 22, ORANGE)
s += t(160, 150, 'Nói với mình tử tế như nói với bạn thân', 12, GREEN) + heart(160, 120, 1.5)
add('G11', 1, 'Nói với mình như nói với bạn', 'Khi con thất bại, con nói với mình lời tử tế như với bạn thân.', s)
add('G11', 2, 'Ba bước tử tế với chính mình', 'Nhận ra mình đang buồn, nhớ ai cũng có lúc như vậy, rồi nói lời tử tế với mình.',
    t(160, 30, 'Tử tế với chính mình', 14) + flow([['Nhận ra', 'mình', 'đang buồn'], ['Nhớ rằng', 'ai cũng', 'có lúc thế'], ['Nói với', 'mình lời', 'tử tế']], 56, 78, 10, 310, 14, 10.5,
    [LBLUE, YELLOW, PINK]) + t(160, 164, 'Đặt tay lên ngực, thở một hơi', 12, GREEN))
s = f'<rect x="0" y="160" width="320" height="40" fill="{G}"/>' + dino(150, 160, 1.0) + heart(196, 100, 1.6) + bubble(196, 26, 110, 34, '"Không sao đâu"', 11.5)
s += f'<path d="M60 160 l10 -20 h24 l6 20z" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2"/>' + t(76, 186, 'tháp đổ', 11)
add('G11', 3, 'Tí tự an ủi', 'Tháp đổ, Tí đặt tay lên ngực và tự nói "Không sao đâu, mình làm lại".', s)

# ================= TUẦN 12 =================
s = hand_diagram() + ''.join(check(x, y) for x, y in [(30, 168), (30, 78), (210, 38), (290, 78), (290, 150)])
add('T12', 1, 'Ôn Bàn tay nền tảng', 'Con chỉ từng ngón và kể thói quen của ngón đó; đánh dấu ngón con làm tốt.', s)
add('T12', 2, 'Lễ Bàn tay nền tảng', 'Con kể, cả nhà khen cụ thể, con nhận "bằng" và chọn thói quen giữ tiếp.',
    t(160, 30, 'Lễ Bàn tay nền tảng', 14) + flow([['Con kể', '5 ngón'], ['Cả nhà', 'khen', 'cụ thể'], ['Nhận', '"bằng"'], ['Chọn 2', 'thói quen', 'giữ tiếp']], 56, 74, 8, 312, 10, 10.5,
    [YELLOW, PINK, G, LBLUE]))
s = f'<rect x="30" y="26" width="260" height="160" rx="10" fill="{WHITE}" stroke="{ORANGE}" stroke-width="5"/><rect x="40" y="36" width="240" height="140" rx="6" fill="none" stroke="{NAVY}" stroke-width="1.5"/>'
s += t(160, 70, 'BẰNG KHEN', 18, ORANGE, '800') + t(160, 96, 'Bàn tay nền tảng', 14) + t(160, 120, 'Con đã hoàn thành 12 tuần', 12) + star(100, 150, 12) + star(160, 152, 14) + star(220, 150, 12)
add('T12', 3, 'Bằng khen Bàn tay nền tảng', 'Bố mẹ tự vẽ bằng khen; không ghi tên con nếu đăng lên mạng.', s)

s = t(160, 20, 'Sơ đồ triển lãm trong nhà', 13)
for i, (lab, c) in enumerate([('Nổi – chìm', LBLUE), ('Hạt nảy mầm', G), ('Ánh sáng – bóng', YELLOW), ('Dốc – xe', SAND)]):
    x = 20 + (i % 2)*150; y = 34 + (i // 2)*70
    s += box(x, y, 130, 56, [f'Bàn {i+1}', lab], c, 11)
s += t(160, 190, 'Khách đi theo vòng, con làm hướng dẫn viên', 10.5, GREEN)
add('K12', 1, 'Sơ đồ triển lãm', 'Bốn bàn thí nghiệm con thích nhất. Con làm hướng dẫn viên cho khách.', s)
s = paper(70, 24, 180, 160)
for i, (lab, c) in enumerate([('Câu hỏi', YELLOW), ('Con đoán', PINK), ('Con thử', LBLUE), ('Kết quả', G)]):
    s += f'<rect x="84" y="{40+i*34}" width="152" height="28" rx="6" fill="{c}" stroke="{NAVY}" stroke-width="1.5"/>' + t(160, 59+i*34, lab, 11.5)
add('K12', 2, 'Mẫu áp phích thí nghiệm', 'Mỗi bàn có một tờ áp phích 4 ô: câu hỏi, con đoán, con thử, kết quả.', s)
s = basin(20, 120, 120, 50) + bottle(60, 100, 0.6) + f'<path d="M180 150 h40 l-6 26 h-28z" fill="#eef7fc" stroke="{NAVY}" stroke-width="2.5"/>' + sprout(200, 150, 30)
s += person(270, 186, 0.9, ORANGE) + t(160, 34, 'Triển lãm khoa học gia đình', 14) + bubble(200, 50, 110, 30, '"Mời bà xem!"', 11)
add('K12', 3, 'Ngày triển lãm', 'Con mời ông bà, hàng xóm xem và tự giải thích thí nghiệm.', s)

s = heart(160, 104, 7, PINK).replace('stroke-width="1.5"', 'stroke-width="0.4"') + box(122, 92, 76, 24, 'Gia đình', '#ffffff', 12)
for (x, y, lab, c) in [(60, 50, 'Trung thực', YELLOW), (260, 50, 'Biết ơn', G), (60, 170, 'Tử tế', LBLUE), (260, 170, 'Trách nhiệm', '#c9b6e8')]:
    s += box(x-50, y-16, 100, 32, lab, c, 11.5)
add('G12', 1, 'Bốn giá trị của nhà mình', 'Ôn bốn giá trị: trung thực, biết ơn, tử tế, trách nhiệm.', s)
add('G12', 2, 'Đánh giá cuối khóa', 'Chấm bảng quan sát tuần 12, so với tuần 0, chọn thói quen giữ tiếp và chia sẻ.',
    t(160, 30, 'Cuối khóa', 14) + flow([['Chấm bảng', 'tuần 12'], ['So với', 'tuần 0'], ['Chọn 2', 'thói quen', 'giữ tiếp'], ['Chia sẻ', 'trên web']], 60, 66, 8, 312, 10, 10.5,
    [YELLOW, LBLUE, G, PINK]) + t(160, 158, 'Tiến bộ nhỏ cũng đáng ghi nhận', 12, GREEN))
s = f'<path d="M160 180 v-60" stroke="{BROWN}" stroke-width="10" stroke-linecap="round"/><circle cx="160" cy="90" r="56" fill="{LGREEN}" stroke="{NAVY}" stroke-width="3"/>'
s += star(130, 70, 10) + star(186, 66, 10) + star(160, 108, 10) + star(116, 104, 8) + star(200, 100, 8) + t(160, 26, 'Cây ước nguyện', 14) + t(250, 160, 'Mỗi ngôi sao', 10.5) + t(250, 174, 'một ước nguyện', 10.5)
add('G12', 3, 'Cây ước nguyện', 'Mỗi người vẽ một ngôi sao ghi ước nguyện cho gia đình.', s)
