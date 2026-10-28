# Hình minh họa và sơ đồ tuần 5–8 + sơ đồ trang khóa học
import math
from illus import *  # noqa: F401,F403  (dùng chung hàm vẽ, add, FIGS)

# ---------- công cụ vẽ sơ đồ ----------
def box(x, y, w, h, lines, fill=WHITE, size=11.5, color=NAVY, rx=10, sw=2.5):
    if isinstance(lines, str): lines = [lines]
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{NAVY}" stroke-width="{sw}"/>'
    n = len(lines); lh = size + 3
    y0 = y + h/2 - (n-1)*lh/2 + size*0.36
    for i, ln in enumerate(lines):
        s += t(x + w/2, y0 + i*lh, ln, size, color)
    return s

def flow(steps, y=70, h=60, x0=12, x1=308, gap=14, size=11, fills=None):
    n = len(steps); w = (x1 - x0 - gap*(n-1)) / n
    s = ''
    for i, st in enumerate(steps):
        x = x0 + i*(w+gap)
        f = (fills[i] if fills else WHITE)
        s += box(x, y, w, h, st, f, size)
        if i < n-1:
            s += arrow(x+w+2, y+h/2, x+w+gap-2, y+h/2, ORANGE, 3)
    return s

def num(cx, cy, k, fill=ORANGE):
    return f'<circle cx="{cx}" cy="{cy}" r="10" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>' + t(cx, cy+4, str(k), 11, WHITE, '800')

def cycle(items, cx=160, cy=112, R=62, bw=92, bh=34, size=11, fills=None):
    n = len(items); s = f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="7 6"/>'
    for i in range(n):
        a1 = -math.pi/2 + (i+0.5)*2*math.pi/n
        ax, ay = cx + R*math.cos(a1), cy + R*math.sin(a1)
        # mũi tên nhỏ theo chiều kim đồng hồ
        tx, ty = -math.sin(a1), math.cos(a1)
        s += f'<polygon points="{ax+tx*8:.1f},{ay+ty*8:.1f} {ax-tx*2+math.cos(a1)*6:.1f},{ay-ty*2+math.sin(a1)*6:.1f} {ax-tx*2-math.cos(a1)*6:.1f},{ay-ty*2-math.sin(a1)*6:.1f}" fill="{ORANGE}"/>'
    for i, it in enumerate(items):
        a = -math.pi/2 + i*2*math.pi/n
        x, y = cx + R*math.cos(a), cy + R*math.sin(a)
        s += box(x-bw/2, y-bh/2, bw, bh, it, (fills[i] if fills else WHITE), size)
    return s

def lamp(x, y, s=1):
    return (f'<g transform="translate({x} {y}) scale({s})"><rect x="-26" y="-9" width="34" height="18" rx="4" fill="{GRAY}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<path d="M8 -12 h10 v24 h-10z" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/></g>')

def sun(cx, cy, r=14):
    rays = ''.join(f'<line x1="{cx+ (r+4)*math.cos(k*math.pi/4):.1f}" y1="{cy+(r+4)*math.sin(k*math.pi/4):.1f}" x2="{cx+(r+10)*math.cos(k*math.pi/4):.1f}" y2="{cy+(r+10)*math.sin(k*math.pi/4):.1f}" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>' for k in range(8))
    return rays + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/>'

def cloud(cx, cy, s=1, fill=WHITE):
    return (f'<g transform="translate({cx} {cy}) scale({s})"><path d="M-30 10 q-14 0 -14 -12 q0 -12 14 -12 q4 -16 22 -14 q12 -14 28 -2 q18 -2 20 14 q14 2 12 14 q-2 12 -14 12z" fill="{fill}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/></g>')

def drop(x, y, s=1):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0 -9 q7 8 0 13 q-7 -5 0 -13" fill="{BLUE}" stroke="{NAVY}" stroke-width="1"/>'

def bag(x, y):
    return (f'<path d="M{x} {y} q-6 70 10 80 h70 q16 -10 10 -80z" fill="{PINK}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M{x+4} {y+6} q42 14 82 0" fill="none" stroke="{NAVY}" stroke-width="2.5" stroke-dasharray="5 4"/>')

# ================= Sơ đồ trang khóa học =================
def hand_diagram():
    s = f'<path d="M110 120 q0 60 50 64 q54 2 58 -60 l2 -40" fill="{SAND}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
    fingers = [(96, 130, 26, 14, -40, 'Cái', 'Tự làm được'), (126, 56, 18, 60, -6, 'Trỏ', 'Nhìn đích rồi đi'),
               (152, 46, 18, 70, 0, 'Giữa', 'Việc quan trọng trước'), (178, 52, 18, 64, 6, 'Áp út', 'Nghe – hiểu – cùng vui'),
               (202, 70, 16, 50, 12, 'Út', 'Chăm cây của mình')]
    for x, y, w, h, r, nm, lab in fingers:
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{w/2}" fill="{SAND}" stroke="{NAVY}" stroke-width="3" transform="rotate({r} {x+w/2} {y+h})"/>'
    s += f'<rect x="114" y="104" width="104" height="40" fill="{SAND}"/>'
    labs = [(40, 150, 'Ngón cái', 'Tự làm được'), (40, 60, 'Ngón trỏ', 'Nhìn đích'), (160, 22, 'Ngón giữa', 'Việc quan trọng trước'),
            (270, 60, 'Áp út', 'Cùng vui'), (270, 132, 'Ngón út', 'Chăm cây')]
    for x, y, a, b in labs:
        s += t(x, y, a, 11, ORANGE, '800') + t(x, y+14, b, 10.5)
    return s
add('KHOA', 1, 'Bàn tay nền tảng', 'Năm ngón tay là năm thói quen. Con nhìn bàn tay mình là nhớ.', hand_diagram())
add('KHOA', 2, 'Chu trình Khoa học bằng tay', 'Mỗi bài khoa học đi một vòng: Quan sát → Đoán → Thử → Kể lại, rồi hỏi tiếp.',
    t(160, 22, 'Khoa học bằng tay', 14) + cycle([['1. Quan sát'], ['2. Đoán'], ['3. Thử'], ['4. Kể lại']], 160, 112, 62, 96, 32, 12, [LBLUE, YELLOW, '#cfe6c4', PINK]))
add('KHOA', 3, 'Một buổi 30 phút', 'Năm bước của một buổi học. Bé 2 tuổi tham gia 10–15 phút.',
    t(160, 34, 'Một buổi 30 phút', 14) + flow([['Kết nối', '3\''], ['Thở', '1\''], ['Hoạt động', '15\''], ['Kể lại', '5\''], ['Mang về', '5\'']], 72, 70, 8, 312, 8, 10.5,
    [SAND, LBLUE, '#cfe6c4', YELLOW, PINK]) + t(160, 172, 'Mệt thì dừng ở bước đang làm', 11.5, GREEN))

# ================= TUẦN 5 =================
# T5
s = t(160, 22, 'Đá to vào trước', 14)
for i, (ok, lab) in enumerate([(True, 'Đá to trước: vừa hết'), (False, 'Sỏi trước: đá không vừa')]):
    x = 40 + i*140
    s += f'<path d="M{x} 50 h100 v100 q0 14 -14 14 h-72 q-14 0 -14 -14z" fill="#eef7fc" stroke="{NAVY}" stroke-width="3"/>'
    if ok:
        s += ''.join(f'<circle cx="{x+cx}" cy="{cy}" r="17" fill="{GRAY}" stroke="{NAVY}" stroke-width="2"/>' for cx, cy in [(30, 140), (70, 140), (50, 108)])
        s += ''.join(f'<circle cx="{x+cx}" cy="{cy}" r="5" fill="{BROWN}"/>' for cx, cy in [(14,120),(86,118),(26,96),(76,92),(50,80),(16,150),(88,150)])
        s += check(x+40, 40)
    else:
        s += f'<rect x="{x+4}" y="100" width="92" height="60" fill="{BROWN}" opacity=".85"/>' + ''.join(f'<circle cx="{x+cx}" cy="{cy}" r="17" fill="{GRAY}" stroke="{NAVY}" stroke-width="2"/>' for cx, cy in [(30, 84), (70, 84), (50, 52)])
        s += t(x+50, 40, '✗', 20, RED)
    s += t(x+50, 186, lab, 10.5)
add('T5', 1, 'Nguyên lý đá to vào trước', 'Việc quan trọng như đá to: cho vào trước thì mọi thứ vừa. Để cuối thì không còn chỗ.', s)
add('T5', 2, 'Thứ tự trong ngày', 'Mỗi ngày: việc chính trước, việc nhà sau, rồi đến giờ chơi.',
    t(160, 34, 'Thứ tự của con hôm nay', 14) + flow([['1. Việc chính', '(bài, xếp cặp)'], ['2. Việc nhà', '(cất đồ)'], ['3. Chơi', '(thật vui!)']], 64, 72, 14, 306, 18, 11,
    [YELLOW, LBLUE, '#cfe6c4']) + num(30, 64, 1) + num(130, 64, 2) + num(228, 64, 3) + star(282, 160, 11))
s = f'<rect x="40" y="60" width="90" height="90" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' + f'<rect x="64" y="86" width="42" height="40" rx="8" fill="{BLUE}" stroke="{NAVY}" stroke-width="2.5"/><path d="M74 86 q11 -12 22 0" fill="none" stroke="{NAVY}" stroke-width="2.5"/>'
s += arrow(140, 105, 180, 105, GREEN) + f'<rect x="190" y="60" width="90" height="90" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
s += f'<rect x="208" y="96" width="56" height="24" rx="8" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="220" cy="122" r="7" fill="{NAVY}"/><circle cx="252" cy="122" r="7" fill="{NAVY}"/>'
s += t(85, 172, 'Đầu tiên: xếp cặp', 12) + t(235, 172, 'Rồi: chơi xe', 12) + t(160, 36, '"Đầu tiên… rồi…"', 14)
add('T5', 3, 'Đầu tiên – rồi', 'Với con nhỏ: một việc cần làm, rồi đến việc con thích.', s)

# K5
s = t(160, 20, 'Đèn càng gần, bóng càng to', 13)
for i, (lx, lab) in enumerate([(40, 'đèn gần'), (10, 'đèn xa')]):
    y0 = 40 + i*76
    s += lamp(lx+20, y0+30, 0.7) + f'<rect x="110" y="{y0+18}" width="14" height="24" rx="3" fill="{GREEN}" stroke="{NAVY}" stroke-width="2"/>'
    s += f'<line x1="280" y1="{y0}" x2="280" y2="{y0+62}" stroke="{NAVY}" stroke-width="3"/>'
    hh = 50 if i == 0 else 30
    s += f'<rect x="268" y="{y0+31-hh/2}" width="12" height="{hh}" fill="{NAVY}" opacity=".75"/>'
    s += f'<path d="M{lx+34} {y0+30} L268 {y0+31-hh/2} M{lx+34} {y0+30} L268 {y0+31+hh/2}" stroke="{YELLOW}" stroke-width="2" stroke-dasharray="4 4"/>'
    s += t(lx+20, y0+60, lab, 10.5) + t(250, y0+68, 'bóng to' if i == 0 else 'bóng nhỏ', 10.5)
add('K5', 1, 'Nguyên lý: đèn gần – bóng to', 'Vật chặn ánh sáng thì có bóng. Đèn càng gần vật, bóng trên tường càng to.', s)
s = f'<line x1="20" y1="160" x2="300" y2="160" stroke="{NAVY}" stroke-width="3"/>'
for x, sy, L, lab in [(60, 120, 60, 'Sáng sớm'), (160, 40, 14, 'Trưa'), (260, 120, 60, 'Chiều')]:
    s += sun(x, sy, 10) + f'<rect x="{x-4}" y="130" width="8" height="30" fill="{GREEN}" stroke="{NAVY}" stroke-width="1.5"/>'
    d = 1 if x < 160 else -1
    s += f'<path d="M{x} 160 l{d*L} 0 l0 4 l{-d*L} 0z" fill="{NAVY}" opacity=".7"/>' if x != 160 else f'<ellipse cx="{x}" cy="162" rx="9" ry="3" fill="{NAVY}" opacity=".7"/>'
    s += t(x, 186, lab, 11)
s += t(160, 20, 'Mặt trời thấp – bóng dài', 13)
add('K5', 2, 'Bóng ngoài trời trong ngày', 'Sáng sớm và chiều, mặt trời thấp nên bóng dài. Gần trưa bóng ngắn nhất.', s)
s = f'<rect x="200" y="20" width="100" height="160" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>' + lamp(46, 110, 1)
s += dino(130, 128, 0.45) + f'<g opacity=".8">' + dino(250, 140, 0.95, NAVY) + '</g>'
s += f'<path d="M72 110 L210 40 M72 110 L210 176" stroke="{YELLOW}" stroke-width="2" stroke-dasharray="5 4"/>' + t(100, 190, 'Rối bóng trên tường', 12)
add('K5', 3, 'Rối bóng khủng long', 'Dùng đèn pin và đồ chơi để tạo bóng trên tường; dịch đèn gần xa để thấy bóng đổi.', s)

# G5
s = t(160, 20, 'Việc nhà theo tuổi', 14)
s += box(14, 34, 140, 26, 'Con khoảng 2 tuổi', YELLOW, 11.5) + box(166, 34, 140, 26, 'Con khoảng 7 tuổi', '#cfe6c4', 11.5)
for i, it in enumerate(['Cất dép lên kệ', 'Bỏ đồ bẩn vào giỏ', 'Đưa thìa cho mẹ']):
    s += box(14, 68 + i*40, 140, 32, it, WHITE, 11)
for i, it in enumerate(['Tưới cây', 'Dọn bàn sau ăn', 'Gấp quần áo của mình']):
    s += box(166, 68 + i*40, 140, 32, it, WHITE, 11)
add('G5', 1, 'Bảng việc nhà theo tuổi', 'Gợi ý việc nhà vừa sức. Con chọn 1 việc làm mỗi ngày trong tuần.', s)
add('G5', 2, 'Vòng trách nhiệm', 'Trách nhiệm là một vòng: nhận việc, làm, tự kiểm tra, đánh dấu – rồi lặp lại mỗi ngày.',
    t(160, 22, 'Vòng trách nhiệm', 14) + cycle([['Nhận việc'], ['Làm'], ['Tự kiểm tra'], ['Đánh dấu ✓']], 160, 114, 64, 98, 32, 11.5, [YELLOW, '#cfe6c4', LBLUE, PINK]))
s = f'<rect x="0" y="160" width="320" height="40" fill="#cfe6c4"/>' + dino(110, 160, 0.9) + pot(230, 160)
s += f'<path d="M150 110 l30 10 l-6 8z" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>' + ''.join(drop(190+k*8, 120+k*6, 0.8) for k in range(3))
s += t(160, 30, 'Tí tưới cây mỗi sáng', 14)
add('G5', 3, 'Tí tưới cây', 'Việc nhà nhỏ, làm đều mỗi ngày, là cách con học trách nhiệm.', s)

# ================= TUẦN 6 =================
s = f'<rect x="120" y="26" width="80" height="150" rx="16" fill="{NAVY}" stroke="{NAVY}" stroke-width="2"/>'
for i, (c, lab) in enumerate([(RED, 'ĐỎ: đứng im'), (YELLOW, 'VÀNG: đi chậm'), (LGREEN, 'XANH: đi')]):
    s += f'<circle cx="160" cy="{56 + i*46}" r="18" fill="{c}" stroke="{WHITE}" stroke-width="2"/>' + t(228, 61 + i*46, lab, 12, NAVY, '600', 'start') + arrow(204, 56+i*46, 222, 56+i*46, GRAY, 2)
s += t(60, 100, 'Nghe hiệu', 12) + t(60, 116, 'lệnh rồi', 12) + t(60, 132, 'mới làm', 12)
add('T6', 1, 'Đèn đỏ – Đèn xanh', 'Ba màu, ba hành động. Con phải nghe và dừng đúng lúc: đó là tập tự kiểm soát.', s)
add('T6', 2, 'Vòng chờ lượt', 'Chờ lượt là một vòng: mình làm, bạn làm, mình chờ và xem.',
    t(160, 22, 'Chờ lượt', 14) + cycle([['Mình làm'], ['Mình chờ', 'và xem'], ['Bạn làm'], ['Bạn chờ', 'và xem']], 160, 114, 64, 98, 36, 11, [YELLOW, LBLUE, '#cfe6c4', PINK]))
s = person(70, 178, 1.0, BLUE) + person(150, 178, 0.95, GREEN, False) + person(230, 178, 0.95, ORANGE, False)
s += f'<circle cx="290" cy="50" r="16" fill="{RED}" stroke="{NAVY}" stroke-width="2.5"/>' + t(160, 32, 'Đèn đỏ! Cả nhà đứng im', 14)
add('T6', 3, 'Cả nhà đứng im', 'Người dẫn trò hô "Đèn đỏ!", mọi người đứng im như tượng.', s)

s = t(160, 20, 'Dốc càng cao, xe đi càng xa', 13)
for i, (h, d, lab) in enumerate([(26, 90, 'dốc thấp'), (52, 170, 'dốc cao')]):
    y = 90 + i*84
    s += f'<path d="M20 {y} l70 0 l-70 {-h}z" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>'
    s += f'<rect x="{28}" y="{y-h+2}" width="18" height="10" rx="3" fill="{ORANGE}" stroke="{NAVY}" stroke-width="1.5" transform="rotate({math.degrees(math.atan2(h,70)):.0f} 37 {y-h+7})"/>'
    s += f'<line x1="90" y1="{y}" x2="{90+d}" y2="{y}" stroke="{NAVY}" stroke-width="2" stroke-dasharray="5 4"/>' + f'<rect x="{90+d-10}" y="{y-10}" width="18" height="10" rx="3" fill="{ORANGE}" stroke="{NAVY}" stroke-width="1.5"/>'
    s += t(50, y+16, lab, 10.5) + t(90+d/2, y-6, f'{"ngắn" if i == 0 else "xa hơn"}', 10.5, GREEN)
add('K6', 1, 'Nguyên lý: dốc cao – xe đi xa', 'Thả xe ở dốc cao hơn, xe thường lăn xa hơn. Con tự đo để kiểm chứng.', s)
add('K6', 2, 'Thí nghiệm công bằng', 'Chỉ đổi một điều (độ cao dốc), giữ nguyên các điều khác, rồi đo và ghi.',
    t(160, 30, 'Thí nghiệm công bằng', 14) + flow([['Chỉ đổi', 'độ cao dốc'], ['Giữ nguyên', 'xe, vạch thả'], ['Đo bằng', 'bước chân'], ['Ghi và', 'so sánh']], 60, 70, 8, 312, 10, 10.5,
    [YELLOW, LBLUE, '#cfe6c4', PINK]) + t(160, 166, 'Đổi nhiều điều một lúc thì không biết vì sao', 11, RED))
s = ''.join(f'<rect x="30" y="{150-i*12}" width="60" height="12" fill="{c}" stroke="{NAVY}" stroke-width="1.5"/>' for i, c in enumerate([BLUE, RED, YELLOW]))
s += f'<path d="M90 114 L250 170" stroke="{BROWN}" stroke-width="10" stroke-linecap="round"/>' + f'<rect x="120" y="114" width="26" height="14" rx="4" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2" transform="rotate(19 133 121)"/>'
s += f'<line x1="250" y1="182" x2="310" y2="182" stroke="{NAVY}" stroke-width="2"/>' + ''.join(f'<line x1="{250+k*12}" y1="178" x2="{250+k*12}" y2="186" stroke="{NAVY}" stroke-width="2"/>' for k in range(6))
s += t(60, 186, '3 cuốn sách', 11) + t(170, 32, 'Ván nghiêng và xe đồ chơi', 13)
add('K6', 3, 'Ván nghiêng bằng sách', 'Kê tấm bìa cứng lên chồng sách để làm dốc; thêm sách là dốc cao hơn.', s)

add('G6', 1, 'Năm bước nhận lỗi – sửa lỗi', 'Lỡ làm sai: dừng, thở, nói thật, xin lỗi, rồi cùng sửa.',
    t(160, 30, 'Nhận lỗi – sửa lỗi', 14) + flow([['Dừng'], ['Thở'], ['Nói', 'thật'], ['Xin', 'lỗi'], ['Cùng', 'sửa']], 66, 60, 8, 312, 10, 11,
    [RED, LBLUE, YELLOW, PINK, '#cfe6c4']) + t(160, 160, '"Lỗi là để sửa, không phải để giấu"', 12, GREEN))
s = box(20, 60, 120, 70, ['Việc con làm', '(làm đổ nước)'], '#fde3cf', 12) + box(180, 60, 120, 70, ['Con là ai', '(con vẫn ngoan)'], '#cfe6c4', 12)
s += t(160, 102, '≠', 30, RED) + t(160, 34, 'Việc sai ≠ con người xấu', 14) + t(160, 166, 'Bố mẹ chê việc, không chê con', 12)
add('G6', 2, 'Việc sai khác với con người', 'Nói về việc con làm, không gắn nhãn con. "Nước đổ rồi, mình lau nhé" thay vì "Con hư quá".', s)
s = f'<rect x="0" y="160" width="320" height="40" fill="#cfe6c4"/>' + dino(90, 160, 0.85) + pot(200, 162) + dino(270, 162, 0.7, '#7fb069')
s += t(160, 30, 'Tí cùng bà trồng lại cây', 14) + heart(150, 80, 1.4)
add('G6', 3, 'Tí sửa lỗi', 'Sau khi nhận lỗi, Tí cùng bà thay chậu mới. Sửa lỗi làm lòng nhẹ hơn.', s)

# ================= TUẦN 7 =================
add('T7', 1, 'Vòng gậy nói chuyện', 'Ai cầm gậy thì nói; người khác nghe rồi nhắc lại ý trước khi đến lượt mình.',
    t(160, 22, 'Gậy nói chuyện', 14) + cycle([['Cầm gậy', 'thì nói'], ['Người khác', 'nghe'], ['Nhắc lại', 'ý bạn'], ['Chuyền', 'gậy']], 160, 114, 64, 96, 36, 11, [YELLOW, LBLUE, '#cfe6c4', PINK]))
s = person(160, 186, 1.3, GREEN)
for (y, side, lab) in [(70, 'L', 'Mắt nhìn người nói'), (76, 'R', 'Tai nghe'), (98, 'L', 'Miệng chờ'), (140, 'L', 'Tay yên'), (170, 'R', 'Chân đứng yên')]:
    if side == 'L':
        s += f'<line x1="122" y1="{y}" x2="146" y2="{y}" stroke="{ORANGE}" stroke-width="2"/>' + t(118, y+4, lab, 10.5, NAVY, '600', 'end')
    else:
        s += f'<line x1="176" y1="{y}" x2="200" y2="{y}" stroke="{ORANGE}" stroke-width="2"/>' + t(204, y+4, lab, 10.5, NAVY, '600', 'start')
s += t(160, 22, 'Nghe bằng cả cơ thể', 14)
add('T7', 2, 'Nghe bằng cả cơ thể', 'Năm dấu hiệu của người đang lắng nghe. Con tự kiểm tra từng dấu hiệu.', s)
s = person(70, 180, 1.0, BLUE) + person(160, 180, 0.8, GREEN, False) + person(250, 180, 1.0, ORANGE)
s += f'<rect x="80" y="104" width="44" height="7" rx="3" fill="{BROWN}" stroke="{NAVY}" stroke-width="2" transform="rotate(-25 102 108)"/>' + bubble(20, 22, 120, 34, '"Con nghĩ là…"', 12)
s += t(230, 40, 'Ai cầm gậy thì nói', 12)
add('T7', 3, 'Cả nhà ngồi vòng tròn', 'Dùng một chiếc thìa gỗ hoặc bút to làm "gậy nói chuyện".', s)

senses = [('Mắt', 'nhìn'), ('Tai', 'nghe'), ('Mũi', 'ngửi'), ('Tay', 'sờ'), ('Lưỡi', 'nếm')]
s = t(160, 22, 'Năm giác quan', 14) + f'<circle cx="160" cy="112" r="26" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>' + t(160, 116, 'Con', 12)
for i, (a, b) in enumerate(senses):
    ang = -math.pi/2 + i*2*math.pi/5; x, y = 160 + 92*math.cos(ang), 112 + 62*math.sin(ang)
    s += f'<line x1="{160+26*math.cos(ang):.1f}" y1="{112+26*math.sin(ang):.1f}" x2="{x - 30*math.cos(ang):.1f}" y2="{y - 20*math.sin(ang):.1f}" stroke="{ORANGE}" stroke-width="2.5"/>'
    s += box(x-36, y-16, 72, 32, [f'{a} – {b}'], [LBLUE, YELLOW, PINK, '#cfe6c4', LGRAY][i], 10.5)
add('K7', 1, 'Sơ đồ năm giác quan', 'Mỗi giác quan cho ta một loại thông tin. Bài này dùng tay, mũi, tai; không nếm.', s)
add('K7', 2, 'Quy trình túi bí ẩn', 'Sờ trong túi, đoán, lấy ra xem, rồi so với lời đoán.',
    t(160, 30, 'Túi bí ẩn', 14) + flow([['Sờ', 'không nhìn'], ['Nói', 'mềm, cứng?'], ['Đoán', 'là gì'], ['Lấy ra', 'so sánh']], 64, 64, 8, 312, 10, 10,
    [PINK, YELLOW, LBLUE, '#cfe6c4']))
s = bag(110, 70) + f'<path d="M150 40 q-6 20 0 40" stroke="{SAND}" stroke-width="18" stroke-linecap="round" fill="none"/>' + t(160, 30, '"Mềm… tròn… là gì nhỉ?"', 13)
s += bubble(220, 100, 90, 34, 'Quả bóng?', 12)
add('K7', 3, 'Tay sờ trong túi', 'Mỗi vật trong túi phải to, sạch, không sắc nhọn.', s)

add('G7', 1, 'Thám tử cảm xúc', 'Nhìn ba manh mối, đoán cảm xúc, hỏi han, rồi giúp.',
    t(160, 26, 'Thám tử cảm xúc', 14) + flow([['Nhìn', 'mặt'], ['Nhìn', 'cơ thể'], ['Nhìn', 'chuyện xảy ra']], 40, 50, 8, 312, 10, 10.5, [YELLOW, LBLUE, PINK])
    + arrow(160, 96, 160, 112, ORANGE, 3) + flow([['Đoán', 'cảm xúc'], ['Hỏi:', '"Bạn ổn không?"'], ['Giúp', 'một việc']], 118, 46, 8, 312, 10, 10.5, ['#cfe6c4', WHITE, '#cfe6c4']))
s = f'<rect x="0" y="160" width="320" height="40" fill="#cfe6c4"/>' + cat(80, 168, 0.95) + dino(220, 162, 0.8)
s += f'<circle cx="300" cy="150" r="10" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>' + bubble(150, 30, 150, 36, '"Mướp buồn à? Tớ giúp nhé"', 10.5)
s += t(70, 40, 'Bóng lăn mất…', 12, GRAY)
add('G7', 2, 'Tí nhận ra Mướp buồn', 'Tí nhìn Mướp, đoán bạn buồn vì mất bóng, rồi hỏi và giúp.', s)
s = t(160, 22, 'Thẻ manh mối', 14)
for i, (lab, ic) in enumerate([('Mặt', face(0, 0, 18, 'buon')), ('Cơ thể', f'<path d="M-10 -18 h20 l6 30 h-32z" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/><circle cx="0" cy="-26" r="8" fill="{SAND}" stroke="{NAVY}" stroke-width="2"/>'), ('Tình huống', pot(0, 20, True))]):
    x = 60 + i*100
    s += f'<rect x="{x-40}" y="40" width="80" height="110" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>' + f'<g transform="translate({x} 92)">{ic}</g>' + t(x, 140, lab, 11)
add('G7', 3, 'Ba thẻ manh mối', 'Vẽ ba thẻ để con nhớ nhìn manh mối nào khi đoán cảm xúc.', s)

# ================= TUẦN 8 =================
add('T8', 1, 'Bốn bước anh dạy em', 'Anh làm mẫu, làm cùng em, để em tự làm, rồi khen cụ thể.',
    t(160, 30, 'Anh dạy em', 14) + flow([['1. Anh', 'làm mẫu'], ['2. Làm', 'cùng em'], ['3. Em làm,', 'anh xem'], ['4. Khen', 'cụ thể']], 60, 66, 8, 312, 10, 10.5,
    [YELLOW, LBLUE, '#cfe6c4', PINK]) + t(160, 162, 'Anh không làm hộ em', 12, GREEN))
s = box(16, 60, 110, 70, ['Em học', 'cách làm'], YELLOW, 12) + box(194, 60, 110, 70, ['Anh học', 'kiên nhẫn, giải thích'], '#cfe6c4', 11)
s += arrow(130, 82, 190, 82, ORANGE, 3) + arrow(190, 112, 130, 112, ORANGE, 3) + t(160, 34, 'Cả hai cùng học', 14) + t(160, 166, 'Anh là trợ giảng, không phải người trông em', 11, NAVY)
add('T8', 2, 'Hai chiều cùng học', 'Khi anh dạy em, cả hai đều học. Anh chỉ hướng dẫn, người lớn vẫn trông em.', s)
s = dino(100, 162, 0.8) + dino(230, 166, 0.55, '#8fd16a') + block(150, 140, 26, 18, RED) + block(150, 120, 26, 18, YELLOW) + block(176, 140, 26, 18, BLUE)
s += f'<rect x="0" y="166" width="320" height="34" fill="#cfe6c4"/>' + bubble(30, 24, 130, 36, '"Đặt khối này lên"', 11.5)
add('T8', 3, 'Tí anh hướng dẫn Tí em', 'Anh nói từng bước ngắn và chờ em làm.', s)

s = t(160, 20, 'Bảng thời tiết tuần này', 13)
days = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
s += f'<rect x="12" y="32" width="296" height="150" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>'
for i, d in enumerate(days):
    x = 12 + i*296/7
    s += t(x + 21, 52, d, 11) + (f'<line x1="{x}" y1="32" x2="{x}" y2="182" stroke="{LGRAY}" stroke-width="1.5"/>' if i else '')
    ic = [sun(x+21, 100, 9), cloud(x+21, 100, 0.45), cloud(x+21, 92, 0.45, LGRAY) + drop(x+15, 120, 0.8) + drop(x+27, 124, 0.8), sun(x+21, 100, 9), cloud(x+21, 100, 0.45), '', ''][i]
    s += ic
s += f'<line x1="12" y1="60" x2="308" y2="60" stroke="{NAVY}" stroke-width="1.5"/>' + t(160, 170, 'Mỗi sáng con vẽ một ký hiệu', 11, GREEN)
add('K8', 1, 'Bảng thời tiết 7 ngày', 'Mỗi sáng con nhìn trời và vẽ ký hiệu: nắng, mây, mưa.', s)
add('K8', 2, 'Vòng tuần hoàn của nước (đơn giản)', 'Nước bốc hơi, thành mây, rơi xuống thành mưa, rồi lại bốc hơi.',
    t(160, 22, 'Nước đi một vòng', 14) + cycle([['Nước', 'ao, hồ'], ['Bốc hơi', 'khi nắng'], ['Thành', 'mây'], ['Rơi xuống', 'thành mưa']], 160, 114, 64, 96, 36, 10.5, [LBLUE, YELLOW, WHITE, BLUE]))
s = f'<path d="M120 70 h60 v100 h-60z" fill="#eef7fc" stroke="{NAVY}" stroke-width="3"/><path d="M114 70 l22 -18 h28 l22 18" fill="none" stroke="{NAVY}" stroke-width="3"/>'
s += f'<rect x="122" y="140" width="56" height="28" fill="{BLUE}" opacity=".7"/>' + ''.join(f'<line x1="180" y1="{150-k*15}" x2="190" y2="{150-k*15}" stroke="{NAVY}" stroke-width="2"/>' for k in range(5))
s += cloud(70, 50, 0.8, LGRAY) + ''.join(drop(56+k*14, 80+(k%2)*10) for k in range(4)) + t(250, 120, 'Người lớn cắt chai', 11) + t(250, 136, 'và dán băng dính', 11) + t(250, 152, 'vào mép cắt', 11)
add('K8', 3, 'Cốc đo mưa tự làm', 'Chai nhựa cắt đôi, úp phần miệng làm phễu. Người lớn cắt và dán kín mép.', s)

s = f'<path d="M130 90 l30 -26 l30 26 v40 h-60z" fill="{SAND}" stroke="{NAVY}" stroke-width="3"/>' + t(160, 116, 'Nhà mình', 11)
helpers = ['Bác thu gom rác', 'Cô bán rau', 'Chú bảo vệ', 'Người giao hàng', 'Cô giáo']
for i, h in enumerate(helpers):
    ang = -math.pi/2 + i*2*math.pi/5; x, y = 160 + 110*math.cos(ang), 110 + 68*math.sin(ang)
    s += f'<line x1="{160+40*math.cos(ang):.1f}" y1="{108+34*math.sin(ang):.1f}" x2="{x - 40*math.cos(ang):.1f}" y2="{y - 14*math.sin(ang):.1f}" stroke="{PINK}" stroke-width="2.5"/>'
    s += box(x-46, y-14, 92, 28, h, WHITE, 10)
add('G8', 1, 'Ai giúp nhà mình mỗi ngày?', 'Sơ đồ những người lao động quanh nhà. Con thêm người mình biết.', s)
add('G8', 2, 'Bốn bước biết ơn người lao động', 'Nhận ra người giúp mình, cảm ơn bằng lời, vẽ tặng, kể lại cho cả nhà.',
    t(160, 30, 'Biết ơn người lao động', 14) + flow([['Nhận ra', 'ai giúp'], ['Cảm ơn', 'bằng lời'], ['Vẽ', 'tặng'], ['Kể lại', 'cả nhà']], 60, 66, 8, 312, 10, 10.5,
    [YELLOW, PINK, LBLUE, '#cfe6c4']))
s = f'<rect x="70" y="36" width="180" height="130" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' + t(160, 62, 'Cảm ơn bác!', 16, ORANGE)
s += heart(110, 100, 1.6) + heart(210, 100, 1.6) + sun(160, 118, 12) + t(160, 152, 'Từ nhà số…', 11, GRAY)
add('G8', 3, 'Thiệp cảm ơn', 'Con vẽ thiệp cảm ơn tặng một người lao động quanh nhà.', s)
