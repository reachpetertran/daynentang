# Hình minh họa và sơ đồ khóa G6 "Tiền nhà mình"
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; MINT = '#bfe3d0'
def kid(x, y, s=1, shirt=ORANGE): return person(x, y, s, shirt, False)

def note(x, y, label='', w=54, h=28, fill=MINT):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>'
            f'<circle cx="{x+w/2}" cy="{y+h/2}" r="{h/3.2}" fill="none" stroke="{GREEN}" stroke-width="1.5"/>' + (t(x+w/2, y+h/2+4, label, 9.5, NAVY, '700') if label else ''))

def jar(cx, base, w, h, label, fill_lvl=0.0, c=LBLUE, size=11):
    x = cx - w/2; top = base - h
    lvl = f'<rect x="{x+4}" y="{base - (h-12)*fill_lvl - 4}" width="{w-8}" height="{(h-12)*fill_lvl}" rx="4" fill="{c}"/>' if fill_lvl else ''
    return (f'<rect x="{x}" y="{top}" width="{w}" height="{h}" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>{lvl}'
            f'<rect x="{x-4}" y="{top-10}" width="{w+8}" height="12" rx="4" fill="{BROWN}" stroke="{NAVY}" stroke-width="2"/>'
            + t(cx, base + 18, label, size))

def bar(x, y, w, h, frac, c=GREEN, label=''):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
            f'<rect x="{x+3}" y="{y+3}" width="{(w-6)*frac}" height="{h-6}" rx="{(h-6)/2}" fill="{c}"/>' + (t(x + w/2, y + h + 16, label, 11) if label else ''))

# ================= TRANG KHÓA =================
add('KHOAM', 1, 'Sáu tuần, sáu bước', 'Biết tiền đi đâu, lập bảng thu chi, có quỹ khẩn cấp, tránh vay nặng lãi, đi chợ có kế hoạch, họp tiền mỗi tháng.',
    t(160, 24, 'Sáu tuần, sáu bước', 14)
    + flow([['1. Tiền', 'đi đâu?'], ['2. Bảng', 'thu chi'], ['3. Quỹ', 'khẩn cấp']], 40, 54, 10, 310, 16, 11, [SAND, YELLOW, LBLUE])
    + flow([['4. Vay', 'an toàn'], ['5. Đi chợ', 'có kế hoạch'], ['6. Họp', 'tiền tháng']], 112, 54, 10, 310, 16, 11, [PINK, G, PURP])
    + t(160, 190, 'Mỗi tuần: 1 buổi bố mẹ + 1 buổi cùng con', 11.5, GREEN))
s = t(160, 22, 'Ba khối nền về tiền của trẻ', 14)
for i, (age, lines, c) in enumerate([('3–5 tuổi', ['Chờ đợi,', 'tự kiểm soát'], LBLUE), ('6–12 tuổi', ['Thói quen', 'tiền bắt đầu', 'hình thành'], YELLOW), ('13–21 tuổi', ['Hiểu biết,', 'ra quyết định'], G)]):
    x = 14 + i*102; hgt = 50 + i*30
    s += box(x, 170 - hgt, 92, hgt, lines, c, 10.5, rx=6) + t(x + 46, 190, age, 11)
add('KHOAM', 2, 'Ba khối nền về tiền', 'Theo CFPB: trẻ nhỏ xây khả năng chờ đợi, trẻ tiểu học hình thành thói quen tiền, tuổi teen học ra quyết định.', s)

# ================= TUẦN 1 =================
s = t(160, 24, 'Ghi chi tiêu 7 ngày', 14) + paper(30, 36, 260, 150)
for i, (d, it, m) in enumerate([('T2', 'Chợ sáng', '120.000'), ('T2', 'Xăng', '70.000'), ('T3', 'Sữa con', '95.000'), ('T4', 'Cà phê', '25.000')]):
    y = 62 + i*28
    s += t(48, y, d, 11, GRAY, '600', 'start') + t(84, y, it, 11, NAVY, '600', 'start') + t(272, y, m, 11, NAVY, '700', 'end')
s += t(160, 176, 'Ghi ngay, ghi hết, không phán xét', 11.5, GREEN)
add('M1A', 1, 'Sổ ghi chi 7 ngày', 'Ghi mọi khoản chi trong 7 ngày, kể cả khoản nhỏ. Tuần sau mới phân loại.', s)
add('M1A', 2, 'Tiền vào – tiền ra', 'Đầu tiên chỉ cần biết hai con số: tiền vào mỗi tháng và tiền ra mỗi tháng.',
    t(160, 26, 'Tiền vào – tiền ra', 14) + flow([['Tiền vào', '(lương, bán', 'hàng…)'], ['Nhà', 'mình'], ['Tiền ra', '(chợ, điện,', 'học…)']], 50, 78, 10, 310, 18, 10.5, [G, SAND, PINK])
    + t(160, 160, 'Vào > ra: còn để dành. Ra > vào: phải sửa ngay', 11.5, NAVY, '600'))
s = t(160, 24, 'Tiền đổi lấy đồ', 14)
s += note(40, 70, '10k') + arrow(102, 84, 140, 84, ORANGE, 3)
s += f'<circle cx="176" cy="84" r="20" fill="{RED}" stroke="{NAVY}" stroke-width="2.5"/><path d="M176 64 q4 -10 12 -10" stroke="{GREEN}" stroke-width="3" fill="none"/>' + t(176, 124, 'quả táo', 11)
s += person(262, 150, 0.7, BLUE) + t(262, 170, 'người bán', 11)
s += t(160, 192, 'Tiền đến từ lao động của bố mẹ', 11.5, GREEN)
add('M1B', 1, 'Tiền đổi lấy đồ', 'Con hiểu: tiền dùng để đổi lấy đồ, và tiền đến từ công việc của bố mẹ.', s)
s = t(160, 24, 'Cửa hàng nhà mình', 14)
s += f'<rect x="30" y="110" width="260" height="20" rx="4" fill="{BROWN}" stroke="{NAVY}" stroke-width="2.5"/>'
s += cup(60, 70, 30, 40) + sock_ball(120, 96, 14) + block(160, 82, 30, 24, YELLOW) + f'<circle cx="230" cy="94" r="16" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/>'
for i, p in enumerate(['2k', '5k', '1k', '3k']):
    s += t(60 + i*57, 146, p, 11, GREEN, '700')
s += kid(100, 190, 0.5, ORANGE) + note(130, 160, '5k', 44, 24)
add('M1B', 2, 'Trò bán hàng', 'Dán giá lên đồ trong nhà. Con lớn trả bằng tiền giấy, con nhỏ đưa và nhận.', s)

# ================= TUẦN 2 =================
s = t(160, 22, 'Bảng thu chi tháng', 14)
for i, (lab, frac, c) in enumerate([('Cần thiết', 0.62, LBLUE), ('Tiết kiệm, trả nợ', 0.2, G), ('Mong muốn', 0.18, YELLOW)]):
    y = 44 + i*44
    s += t(18, y + 15, lab, 11, NAVY, '700', 'start') + bar(130, y, 176, 22, frac, c)
s += t(160, 180, 'Tỉ lệ chỉ là ví dụ, mỗi nhà một khác', 10, GRAY, '500')
add('M2A', 1, 'Ba nhóm chi', 'Chia tiền ra thành ba nhóm: cần thiết, tiết kiệm và trả nợ, mong muốn. Tỉ lệ trong hình chỉ là ví dụ.', s)
add('M2A', 2, 'Để dành trước, tiêu sau', 'Ngày nhận lương, chuyển ngay một khoản để dành. Phần còn lại mới dùng cho chi tiêu.',
    t(160, 28, 'Để dành trước, tiêu sau', 14) + flow([['Nhận', 'lương'], ['Chuyển', 'khoản', 'để dành'], ['Trả', 'chi cố', 'định'], ['Còn lại', 'mới tiêu']], 54, 78, 8, 312, 10, 10.5, [G, YELLOW, LBLUE, SAND])
    + t(160, 160, 'Khoản nhỏ mà đều tốt hơn khoản lớn mà thất thường', 11, GREEN))
s = t(160, 22, 'Cần hay muốn?', 14)
s += basket(40, 120, 100, 50, LBLUE) + t(90, 186, 'CẦN', 13, NAVY, '800') + basket(180, 120, 100, 50, YELLOW) + t(230, 186, 'MUỐN', 13, NAVY, '800')
s += t(90, 60, 'gạo · nước', 11) + t(90, 80, 'áo mặc đi học', 11) + t(230, 60, 'kẹo · đồ chơi', 11) + t(230, 80, 'áo siêu nhân', 11)
s += arrow(90, 88, 90, 112, ORANGE, 3) + arrow(230, 88, 230, 112, ORANGE, 3)
add('M2B', 1, 'Hai rổ: cần và muốn', 'Con xếp tranh vào hai rổ. Cần là thứ phải có để sống và đi học. Muốn là thứ thích nhưng có thể chờ.', s)
add('M2B', 2, 'Muốn thì chờ một chút', 'Món muốn mua: viết tên, chờ vài ngày, rồi hỏi lại "con còn muốn không?"',
    t(160, 28, 'Muốn thì chờ một chút', 14) + flow([['Con', 'muốn mua'], ['Viết tên', 'lên giấy'], ['Chờ', 'vài ngày'], ['Còn', 'muốn', 'không?']], 54, 78, 8, 312, 10, 10.5, [YELLOW, WHITE, LBLUE, G])
    + t(160, 160, 'Chờ được là một kỹ năng về tiền', 11.5, GREEN))

# ================= TUẦN 3 =================
s = t(160, 22, 'Quỹ khẩn cấp từng nấc', 14)
for i, (lab, c) in enumerate([(['Nấc 1:', 'khoản nhỏ'], YELLOW), (['Nấc 2:', '1 tháng chi', 'cần thiết'], LBLUE), (['Nấc 3:', '3 tháng', 'trở lên'], G)]):
    x = 20 + i*94; y = 140 - i*36
    s += box(x, y, 92, 186 - y, lab, c, 10, rx=4)
s += t(160, 44, 'Bắt đầu nhỏ, đi từng bậc', 11.5, GREEN)
add('M3A', 1, 'Quỹ khẩn cấp từng nấc', 'Bắt đầu bằng một khoản nhỏ, rồi lên dần. Các mốc là gợi ý, không phải quy định.', s)
add('M3A', 2, 'Khi nào dùng quỹ', 'Quỹ khẩn cấp dành cho việc bất ngờ và cần thiết. Dùng xong thì bù lại.',
    t(160, 28, 'Khi nào dùng quỹ?', 14) + flow([['Việc', 'bất ngờ?'], ['Thật sự', 'cần?'], ['Dùng', 'quỹ'], ['Bù lại', 'dần']], 54, 70, 8, 312, 10, 11, [SAND, YELLOW, LBLUE, G])
    + t(160, 150, 'Ốm đau, sửa xe đi làm: có', 11, GREEN) + t(160, 170, 'Giảm giá, đồ mới: không', 11, RED))
s = t(160, 22, 'Hũ ba ngăn', 14)
s += jar(70, 160, 70, 100, 'Tiết kiệm', 0.5, G) + jar(160, 160, 70, 100, 'Tiêu', 0.3, YELLOW) + jar(250, 160, 70, 100, 'Chia sẻ', 0.2, PINK)
add('M3B', 1, 'Hũ ba ngăn', 'Mỗi lần có tiền, con chia vào ba hũ: tiết kiệm, tiêu, chia sẻ.', s)
s = t(160, 22, 'Thanh mục tiêu của con', 14)
s += block(24, 52, 50, 40, ORANGE) + t(49, 110, 'món con muốn', 10)
s += bar(96, 62, 210, 26, 0.4, GREEN)
for i in range(5): s += f'<line x1="{99 + i*51}" y1="92" x2="{99 + i*51}" y2="100" stroke="{NAVY}" stroke-width="2"/>'
s += t(200, 120, 'Mỗi lần bỏ hũ, tô thêm một ô', 11.5, GREEN) + t(160, 170, 'Con nhỏ: bỏ tiền giấy vào hũ, không dùng tiền xu', 10.5, RED)
add('M3B', 2, 'Thanh mục tiêu', 'Con vẽ món mình muốn và tô thêm một ô mỗi lần bỏ tiền vào hũ tiết kiệm.', s)

# ================= TUẦN 4 =================
s = t(160, 22, 'Dấu hiệu tín dụng đen', 14)
for i, r in enumerate(['Lãi, phí không ghi rõ', 'Không có tên công ty, địa chỉ', 'Đòi quyền đọc danh bạ', 'Dọa, bôi nhọ khi trả chậm']):
    y = 38 + i*36
    s += f'<circle cx="28" cy="{y+14}" r="11" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>' + t(28, y+18, '!', 13, WHITE, '800') + box(46, y, 260, 28, r, WHITE, 11)
s += t(160, 190, 'Thấy một dấu hiệu: dừng lại', 11.5, RED)
add('M4A', 1, 'Dấu hiệu tín dụng đen', 'Bốn dấu hiệu theo cảnh báo của Bộ Công an về ứng dụng vay tiền biến tướng.', s)
s = t(160, 24, 'Trần lãi suất khi vay giữa người với người', 14)
s += bar(30, 60, 260, 26, 0.2, G) + t(56, 110, '20%/năm', 12, GREEN, '800') + t(56, 126, 'mức trần', 10)
s += f'<line x1="30" y1="140" x2="290" y2="140" stroke="{RED}" stroke-width="3" stroke-dasharray="6 5"/>' + t(160, 160, 'Gấp 5 lần mức trần: có thể bị xử lý hình sự', 11, RED, '700')
s += t(160, 184, 'Bộ luật Dân sự 2015 Điều 468; Bộ luật Hình sự Điều 201', 9, GRAY, '500')
add('M4A', 2, 'Trần lãi suất 20%/năm', 'Lãi suất thỏa thuận giữa các bên không vượt 20%/năm, trừ khi luật khác quy định khác. Cho vay gấp 5 lần mức trần có thể bị xử lý hình sự.', s)
add('M4B', 1, 'Mượn rồi trả', 'Mượn đồ của ai thì giữ cẩn thận và trả đúng hẹn. Đó cũng là cách người lớn vay tiền.',
    t(160, 20, 'Mượn rồi trả', 14) + cycle([['Hỏi', 'mượn'], ['Giữ', 'cẩn thận'], ['Trả', 'đúng hẹn'], ['Được tin,', 'mượn tiếp']], 160, 118, 64, 88, 34, 10.5, [YELLOW, LBLUE, G, PINK]))
s = t(160, 24, 'Vay thì phải trả thêm', 14)
s += f'<g>{"".join(star(30 + k*22, 74, 10) for k in range(5))}</g>' + t(74, 104, 'mượn 5 sao', 11)
s += arrow(150, 74, 182, 74, ORANGE, 3)
s += f'<g>{"".join(star(196 + k*20, 74, 9) for k in range(6))}</g>' + t(250, 104, 'trả 6 sao', 11)
s += box(40, 126, 240, 40, ['Sao thêm là "tiền lãi":', 'giá của việc dùng đồ người khác'], SAND, 11)
add('M4B', 2, 'Tiền lãi là gì', 'Trò chơi sao: mượn 5, trả 6. Sao thêm là tiền lãi.', s)

# ================= TUẦN 5 =================
add('M5A', 1, 'Đi chợ có kế hoạch', 'Lên thực đơn tuần, viết danh sách, đặt số tiền mang theo, rồi đi chợ một lần.',
    t(160, 28, 'Đi chợ có kế hoạch', 14) + flow([['Thực đơn', 'tuần'], ['Danh', 'sách'], ['Số tiền', 'mang', 'theo'], ['Đi chợ', 'một lần']], 54, 78, 8, 312, 10, 10.5, [SAND, YELLOW, G, LBLUE])
    + t(160, 160, 'Ngoài danh sách: ghi lại, tuần sau xét', 11.5, GREEN))
s = t(160, 24, 'So giá theo đơn vị', 14)
s += bottle(70, 70, 0.9) + t(70, 160, '500 ml · 10k', 11) + t(70, 178, '= 2k / 100 ml', 11, GREEN, '700')
s += bottle(220, 50, 1.2) + t(220, 160, '1 lít · 18k', 11) + t(220, 178, '= 1,8k / 100 ml', 11, GREEN, '700')
add('M5A', 2, 'So giá theo đơn vị', 'Chia giá cho số gam hoặc số ml để so. Hộp to thường rẻ hơn, nhưng không phải luôn luôn.', s)
s = t(160, 22, 'Danh sách tranh của con', 14) + paper(40, 32, 240, 156)
for i, (lab, ic) in enumerate([('Trứng', f'<ellipse cx="78" cy="62" rx="10" ry="13" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'),
                                ('Rau', sprout(78, 108, 26)), ('Chuối', f'<path d="M66 128 q12 18 28 0" stroke="{YELLOW}" stroke-width="8" fill="none" stroke-linecap="round"/>')]):
    y = 66 + i*44
    s += ic + t(110, y + 4, lab, 13, NAVY, '700', 'start') + f'<rect x="224" y="{y-10}" width="22" height="22" rx="4" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
s += check(228, 72)
add('M5B', 1, 'Danh sách tranh', 'Con nhỏ tìm món theo tranh. Con lớn đánh dấu khi đã mua.', s)
s = t(160, 22, 'Con giữ ngân sách nhỏ', 14)
s += note(30, 50, '20k', 70, 34) + t(65, 104, 'ngân sách', 11)
s += arrow(110, 66, 140, 66, ORANGE, 3) + box(146, 44, 160, 46, ['Mua 2 món cần', 'cho bữa tối'], G, 11)
s += box(146, 104, 160, 46, ['Còn dư: bỏ vào', 'hũ tiết kiệm'], YELLOW, 11) + arrow(226, 92, 226, 102, ORANGE, 3)
s += t(160, 182, 'Con tự đếm tiền, tự nhận tiền thừa', 11.5, GREEN)
add('M5B', 2, 'Ngân sách nhỏ', 'Con lớn giữ một khoản nhỏ, mua hai món cần và tự kiểm tra tiền thừa.', s)

# ================= TUẦN 6 =================
s = t(160, 22, 'Họp tiền mỗi tháng (20 phút)', 14)
parts = [('Xem', 'bảng', 5, LBLUE), ('Quỹ', '', 4, G), ('Nợ', '', 4, PINK), ('Tháng', 'tới', 4, YELLOW), ('Khen', '', 3, PURP)]
x = 12
for a, b, m, c in parts:
    w = 296 * m / 20
    s += box(x, 50, w - 4, 70, [a] + ([b] if b else []) + [f"{m}'"], c, 10.5, rx=6)
    x += w
s += t(160, 150, 'Ngày cố định, ví dụ sau ngày nhận lương', 11.5, GREEN) + t(160, 172, 'Nói về con số, không trách người', 11, NAVY, '500')
add('M6A', 1, 'Họp tiền mỗi tháng', 'Bố mẹ xem bảng thu chi, quỹ khẩn cấp, nợ, kế hoạch tháng tới, rồi khen nhau một điều.', s)
add('M6A', 2, 'Vòng một tháng', 'Ghi chép, để dành, xem lại, sửa một điều. Mỗi tháng tốt hơn một chút.',
    t(160, 22, 'Vòng một tháng', 14) + cycle([['Ghi', 'chép'], ['Để dành', 'trước'], ['Họp', 'cuối tháng'], ['Sửa', 'một điều']], 160, 112, 64, 88, 34, 10.5, [SAND, G, YELLOW, PINK]))
s = t(160, 22, 'Ngăn Chia sẻ dùng làm gì?', 14)
s += jar(70, 150, 70, 90, 'Chia sẻ', 0.6, PINK)
for i, r in enumerate(['Quà cho ông bà', 'Góp giúp bạn khó khăn', 'Mua sách tặng thư viện']):
    s += arrow(110, 104, 140, 62 + i*40, ORANGE, 2.5) + box(146, 46 + i*40, 160, 32, r, WHITE, 10.5)
add('M6B', 1, 'Ngăn Chia sẻ', 'Con tự chọn cách dùng tiền trong hũ Chia sẻ để giúp hoặc tặng người khác.', s)
s = t(160, 22, 'Con kể lại về tiền', 14)
s += kid(70, 170, 0.8, ORANGE) + bubble(110, 40, 196, 40, '"Tiền đến từ lao động."', 11)
s += bubble(110, 92, 196, 40, '"Cần trước, muốn sau."', 11) + bubble(110, 144, 196, 36, '"Chia ba hũ mỗi lần."', 11)
add('M6B', 2, 'Con kể lại', 'Cuối khóa, con kể lại ba điều đã học về tiền bằng lời của mình.', s)

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('M', 'KHOAM'))), 'hình G6')
