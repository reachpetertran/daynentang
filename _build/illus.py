# Hình minh họa tự vẽ (SVG) cho các bài học – daynentang.com
# Phong cách phẳng, màu theo logo. Không vẽ trẻ em thật; nhân vật là con vật tự sáng tác.
import os, html
from common import ROOT

OUT = os.path.join(ROOT, 'assets', 'minh-hoa')
NAVY='#1b2a41'; ORANGE='#f47b2a'; GREEN='#2f7d4a'; LGREEN='#5cae4f'; CREAM='#fffdf8'
BLUE='#2f86c9'; LBLUE='#9fd0f0'; SAND='#f3e3c3'; BROWN='#a0673a'; PINK='#f2a7a0'
YELLOW='#f6c445'; GRAY='#8a8f98'; LGRAY='#d9dde3'; WHITE='#ffffff'; RED='#d9534f'
FONT='font-family="system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif"'

def svg(body, bg='#fbf3e4', title=''):
    title = html.escape(title)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 200" role="img" aria-label="{title}">'
            f'<title>{title}</title><rect width="320" height="200" rx="16" fill="{bg}"/>{body}</svg>')

def t(x, y, s, size=13, fill=NAVY, w='600', anchor='middle'):
    return f'<text x="{x}" y="{y}" {FONT} font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{s}</text>'

# ---------- vật dụng ----------
def cup(x, y, w=34, h=44, fill=LBLUE, water=None, stroke=NAVY):
    p = f'<path d="M{x} {y} L{x+w} {y} L{x+w-5} {y+h} L{x+5} {y+h} Z" fill="{fill}" stroke="{stroke}" stroke-width="2.5" stroke-linejoin="round"/>'
    if water:
        wy = y + h*(1-water)
        p += f'<path d="M{x+1+ (wy-y)*5/h} {wy} L{x+w-1-(wy-y)*5/h} {wy} L{x+w-5} {y+h-1} L{x+5} {y+h-1} Z" fill="{BLUE}" opacity=".75"/>'
    return p
def bottle(x, y, s=1, full=False):
    body = f'<rect x="{x}" y="{y+14*s}" width="{22*s}" height="{46*s}" rx="{7*s}" fill="{LBLUE if not full else BLUE}" stroke="{NAVY}" stroke-width="2.5"/>'
    neck = f'<rect x="{x+6*s}" y="{y}" width="{10*s}" height="{16*s}" rx="2" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/>'
    return body + neck
def basin(x, y, w=200, h=70):
    return (f'<path d="M{x} {y} L{x+w} {y} L{x+w-18} {y+h} L{x+18} {y+h} Z" fill="{LGRAY}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
            f'<path d="M{x+6} {y+14} L{x+w-6} {y+14} L{x+w-20} {y+h-3} L{x+20} {y+h-3} Z" fill="{LBLUE}"/>'
            f'<path d="M{x+20} {y+14} q10 -6 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="{WHITE}" stroke-width="2"/>')
def basket(x, y, w=80, h=44, fill=BROWN):
    return (f'<path d="M{x} {y} L{x+w} {y} L{x+w-8} {y+h} L{x+8} {y+h} Z" fill="{fill}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
            + ''.join(f'<line x1="{x+8+i*16}" y1="{y+4}" x2="{x+12+i*15}" y2="{y+h-3}" stroke="#7a4c28" stroke-width="2"/>' for i in range(5))
            + f'<rect x="{x-4}" y="{y-6}" width="{w+8}" height="8" rx="4" fill="#8a5a33" stroke="{NAVY}" stroke-width="2"/>')
def sock_ball(cx, cy, r=12, fill=ORANGE):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/><path d="M{cx-r+3} {cy} q{r-3} {-r/2} {2*r-6} 0" fill="none" stroke="{NAVY}" stroke-width="2"/>'
def block(x, y, w=26, h=18, fill=RED):
    studs = ''.join(f'<rect x="{x+4+i*10}" y="{y-5}" width="7" height="5" rx="1.5" fill="{fill}" stroke="{NAVY}" stroke-width="1.5"/>' for i in range(int(w//10)))
    return studs + f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>'
def sprout(x, y, h=30, leaves=2):
    s = f'<path d="M{x} {y} q-3 {-h/2} 0 {-h}" stroke="{LGREEN}" stroke-width="4" fill="none" stroke-linecap="round"/>'
    if leaves:
        s += f'<ellipse cx="{x-8}" cy="{y-h+2}" rx="9" ry="5" fill="{LGREEN}" stroke="{GREEN}" stroke-width="1.5" transform="rotate(-25 {x-8} {y-h+2})"/>'
        s += f'<ellipse cx="{x+8}" cy="{y-h+2}" rx="9" ry="5" fill="{LGREEN}" stroke="{GREEN}" stroke-width="1.5" transform="rotate(25 {x+8} {y-h+2})"/>'
    return s
def bean(cx, cy, rot=0):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="6" ry="4" fill="#4c8b3a" stroke="{NAVY}" stroke-width="1.2" transform="rotate({rot} {cx} {cy})"/>'
def paper(x, y, w=110, h=130, fill=WHITE):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/>'
def check(x, y, c=GREEN):
    return f'<path d="M{x} {y} l6 6 l12 -13" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
def star(cx, cy, r=9, fill=YELLOW):
    import math
    pts=[]
    for i in range(10):
        a = math.pi/2 + i*math.pi/5; rr = r if i%2==0 else r*0.45
        pts.append(f'{cx+rr*math.cos(a):.1f},{cy-rr*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{fill}" stroke="{NAVY}" stroke-width="1.5" stroke-linejoin="round"/>'
def heart(cx, cy, s=1, fill=PINK):
    return f'<path transform="translate({cx} {cy}) scale({s})" d="M0 6 C-10 -2 -8 -10 0 -5 C8 -10 10 -2 0 6Z" fill="{fill}" stroke="{NAVY}" stroke-width="1.5"/>'
def arrow(x1, y1, x2, y2, c=ORANGE, w=4):
    import math
    a = math.atan2(y2-y1, x2-x1); L=10
    hx1 = x2 - L*math.cos(a-0.5); hy1 = y2 - L*math.sin(a-0.5)
    hx2 = x2 - L*math.cos(a+0.5); hy2 = y2 - L*math.sin(a+0.5)
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polyline points="{hx1:.1f},{hy1:.1f} {x2},{y2} {hx2:.1f},{hy2:.1f}" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')
def bubble(x, y, w, h, s, size=12):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
            f'<path d="M{x+16} {y+h} l-4 10 l12 -10" fill="{WHITE}" stroke="{NAVY}" stroke-width="2" stroke-linejoin="round"/>'
            f'<rect x="{x+13}" y="{y+h-2}" width="14" height="4" fill="{WHITE}"/>' + t(x+w/2, y+h/2+4, s, size))
def face(cx, cy, r, mood, fill=YELLOW):
    eyes = f'<circle cx="{cx-r*0.35}" cy="{cy-r*0.2}" r="{r*0.09}" fill="{NAVY}"/><circle cx="{cx+r*0.35}" cy="{cy-r*0.2}" r="{r*0.09}" fill="{NAVY}"/>'
    m = {'vui': f'<path d="M{cx-r*0.45} {cy+r*0.15} q{r*0.45} {r*0.45} {r*0.9} 0" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>',
         'buon': f'<path d="M{cx-r*0.4} {cy+r*0.45} q{r*0.4} {-r*0.35} {r*0.8} 0" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>'
                 f'<path d="M{cx+r*0.38} {cy+r*0.02} q4 8 0 10 q-4 -2 0 -10" fill="{LBLUE}"/>',
         'gian': f'<path d="M{cx-r*0.4} {cy+r*0.4} h{r*0.8}" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>'
                 f'<path d="M{cx-r*0.55} {cy-r*0.5} l{r*0.35} {r*0.18} M{cx+r*0.55} {cy-r*0.5} l{-r*0.35} {r*0.18}" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>',
         'so': f'<ellipse cx="{cx}" cy="{cy+r*0.38}" rx="{r*0.18}" ry="{r*0.24}" fill="{NAVY}"/>'
               f'<path d="M{cx-r*0.55} {cy-r*0.55} q{r*0.2} {-r*0.15} {r*0.4} 0 M{cx+r*0.15} {cy-r*0.55} q{r*0.2} {-r*0.15} {r*0.4} 0" stroke="{NAVY}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'}
    fills = {'vui': YELLOW, 'buon': LBLUE, 'gian': '#f08a6b', 'so': '#c9b6e8'}
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fills.get(mood, fill)}" stroke="{NAVY}" stroke-width="2.5"/>' + eyes + m[mood]
def person(x, y, s=1, shirt=GREEN, big=True):
    # người lớn/trẻ dạng hình khối đơn giản, không có mặt chi tiết
    h = 1 if big else 0.72
    return (f'<g transform="translate({x} {y}) scale({s*h})">'
            f'<circle cx="0" cy="-78" r="14" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<path d="M-18 -60 h36 l4 44 h-44 z" fill="{shirt}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<rect x="-14" y="-16" width="11" height="16" rx="3" fill="{NAVY}"/><rect x="3" y="-16" width="11" height="16" rx="3" fill="{NAVY}"/></g>')
def dino(x, y, s=1, fill=LGREEN):
    # Khủng long Tí – nhân vật tự sáng tác
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-30 0 q-30 -2 -42 -14 q20 4 34 -4 z" fill="{fill}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<ellipse cx="0" cy="-14" rx="32" ry="22" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<path d="M14 -28 q10 -26 30 -26 q16 0 16 14 q0 12 -16 12 q-12 0 -18 8 z" fill="{fill}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<circle cx="48" cy="-44" r="3" fill="{NAVY}"/><path d="M52 -34 q4 2 6 -1" stroke="{NAVY}" stroke-width="2" fill="none" stroke-linecap="round"/>'
            f'<path d="M-20 -34 l6 -10 l6 9 l6 -11 l6 10 l6 -9 l4 8" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2" stroke-linejoin="round"/>'
            f'<rect x="-18" y="2" width="10" height="14" rx="4" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/><rect x="8" y="2" width="10" height="14" rx="4" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/></g>')
def cat(x, y, s=1, fill='#e9a24a'):
    # Mèo Mướp – nhân vật tự sáng tác
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M22 -10 q26 -6 20 -30" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/><path d="M22 -10 q26 -6 20 -30" fill="none" stroke="{fill}" stroke-width="4" stroke-linecap="round"/>'
            f'<ellipse cx="0" cy="-16" rx="26" ry="18" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<path d="M-22 -40 l4 -16 l10 10 h16 l10 -10 l4 16 q4 20 -22 22 q-26 -2 -22 -22z" fill="{fill}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>'
            f'<circle cx="-11" cy="-34" r="2.6" fill="{NAVY}"/><circle cx="7" cy="-34" r="2.6" fill="{NAVY}"/>'
            f'<path d="M-6 -28 q2 3 4 0" stroke="{NAVY}" stroke-width="2" fill="none"/>'
            f'<path d="M-10 -14 l-4 -3 M-4 -12 v-4 M2 -14 l4 -3" stroke="#b9772f" stroke-width="2.5" stroke-linecap="round"/>'
            f'<rect x="-18" y="-2" width="9" height="10" rx="4" fill="{fill}" stroke="{NAVY}" stroke-width="2"/><rect x="8" y="-2" width="9" height="10" rx="4" fill="{fill}" stroke="{NAVY}" stroke-width="2"/></g>')
def slipper(x, y, rot=0, fill=BLUE):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><ellipse cx="0" cy="0" rx="10" ry="22" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<path d="M-9 -6 q9 -8 18 0" fill="none" stroke="{NAVY}" stroke-width="4"/></g>')
def pot(x, y, broken=False):
    if not broken:
        return (f'<path d="M{x-20} {y-34} h40 l-6 34 h-28 z" fill="{BROWN}" stroke="{NAVY}" stroke-width="2.5"/>'
                + sprout(x, y-34, 22) + f'<circle cx="{x}" cy="{y-58}" r="7" fill="{PINK}" stroke="{NAVY}" stroke-width="2"/>')
    return (f'<path d="M{x-30} {y} l6 -26 h18 l-6 26 z" fill="{BROWN}" stroke="{NAVY}" stroke-width="2.5" transform="rotate(-12 {x-20} {y})"/>'
            f'<path d="M{x+2} {y} l2 -26 h18 l4 26 z" fill="{BROWN}" stroke="{NAVY}" stroke-width="2.5" transform="rotate(14 {x+12} {y})"/>'
            f'<ellipse cx="{x-4}" cy="{y+2}" rx="20" ry="5" fill="#6b4a2c"/>' + f'<circle cx="{x+30}" cy="{y-6}" r="7" fill="{PINK}" stroke="{NAVY}" stroke-width="2"/>')

# ---------- danh sách hình theo bài ----------
FIGS = {}
def add(code, n, title, cap, body, bg='#fbf3e4'):
    os.makedirs(OUT, exist_ok=True)
    fn = f'{code.lower()}-{n}.svg'
    open(os.path.join(OUT, fn), 'w', encoding='utf-8').write(svg(body, bg, title))
    FIGS.setdefault(code, []).append((fn, title, cap))

# ===== T1 =====
icons = [('Dậy', f'<circle cx="0" cy="0" r="11" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2"/>'),
         ('Đánh răng', f'<rect x="-14" y="-3" width="26" height="6" rx="3" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/><rect x="8" y="-9" width="7" height="8" rx="2" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'),
         ('Mặc đồ', f'<path d="M-12 -10 l7 -4 h10 l7 4 l-4 8 h-3 v14 h-10 v-14 h-3z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2" stroke-linejoin="round"/>'),
         ('Ăn sáng', f'<path d="M-14 -2 h28 q0 14 -14 14 q-14 0 -14 -14z" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/><path d="M-6 -6 q2 -6 0 -10 M2 -6 q2 -6 0 -10" stroke="{GRAY}" stroke-width="2" fill="none"/>'),
         ('Xếp cặp', f'<rect x="-12" y="-10" width="24" height="22" rx="5" fill="{BLUE}" stroke="{NAVY}" stroke-width="2"/><path d="M-6 -10 q6 -8 12 0" fill="none" stroke="{NAVY}" stroke-width="2"/>')]
b = t(160, 26, 'Bảng buổi sáng của con', 15)
for i, (lab, ic) in enumerate(icons):
    x = 22 + i*58
    b += f'<rect x="{x}" y="42" width="50" height="96" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>'
    b += f'<g transform="translate({x+25} 78)">{ic}</g>' + t(x+25, 120, lab, 9.5)
b += f'<ellipse cx="{22+3*58+25}" cy="90" rx="32" ry="52" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="6 4"/>'
b += t(160, 172, 'Con khoanh 1 việc sẽ tự làm tuần này', 12, GREEN)
add('T1', 1, 'Bảng buổi sáng', 'Con vẽ 4–5 việc buổi sáng, khoanh 1 việc sẽ tự làm.', b)
b = person(110, 176, 1.15, BLUE) + bubble(150, 30, 150, 40, '"Bố giơ tay trái lên!"', 12)
b += f'<rect x="230" y="104" width="24" height="44" rx="6" fill="{GREEN}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="242" cy="92" r="11" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>'
b += arrow(222, 120, 140, 110) + t(160, 190, 'Trò "Người máy": làm đúng từng lời con nói', 11.5)
add('T1', 2, 'Trò Người máy', 'Bố mẹ làm "người máy", con ra lệnh từng bước.', b)
b = basket(118, 120, 90, 50) + block(70, 150, 30, 20, RED) + sock_ball(240, 160, 14, YELLOW)
b += f'<rect x="140" y="80" width="40" height="34" rx="8" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="148" cy="116" r="7" fill="{NAVY}"/><circle cx="172" cy="116" r="7" fill="{NAVY}"/>'
b += arrow(95, 140, 120, 128) + arrow(228, 152, 205, 135)
b += t(70, 52, '♪', 26, ORANGE) + t(250, 60, '♪', 22, ORANGE) + t(160, 34, '"Đồ chơi về nhà…"', 14)
add('T1', 3, 'Cất đồ chơi vào rổ', 'Con nhỏ cất đồ chơi to vào rổ theo bài hát.', b)

# ===== K1 =====
b = basin(60, 96, 200, 74)
b += bottle(96, 80, 0.8) + f'<circle cx="160" cy="112" r="13" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/>'
b += f'<rect x="196" y="152" width="40" height="8" rx="4" fill="{GRAY}" stroke="{NAVY}" stroke-width="2"/><ellipse cx="236" cy="156" rx="9" ry="6" fill="{GRAY}" stroke="{NAVY}" stroke-width="2"/>'
b += f'<ellipse cx="128" cy="160" rx="13" ry="8" fill="#7c7f86" stroke="{NAVY}" stroke-width="2"/>'
b += t(160, 34, 'Nổi hay chìm?', 16) + t(104, 64, 'nổi', 12, GREEN) + t(220, 140, 'chìm', 12, RED)
add('K1', 1, 'Chậu nước thử nổi chìm', 'Thả từng vật vào chậu nước nông. Người lớn luôn ngồi sát.', b)
b = basin(60, 100, 200, 70) + bottle(100, 78, 0.85) + bottle(200, 120, 0.85, True)
b += t(112, 66, 'chai rỗng', 12, GREEN) + t(250, 192, 'chai đầy nước (nằm thấp)', 11.5, RED)
b += t(160, 30, 'Hai chai giống nhau – vì sao khác?', 14)
add('K1', 2, 'Chai rỗng và chai đầy nước', 'So sánh bất ngờ: chai rỗng nổi cao, chai đầy nước nằm thấp hơn hẳn.', b)
b = paper(40, 24, 240, 150)
b += t(90, 48, 'Vật', 12) + t(170, 48, 'Con đoán', 12) + t(240, 48, 'Kết quả', 12)
b += f'<line x1="40" y1="56" x2="280" y2="56" stroke="{NAVY}" stroke-width="1.5"/><line x1="130" y1="30" x2="130" y2="170" stroke="{LGRAY}" stroke-width="1.5"/><line x1="205" y1="30" x2="205" y2="170" stroke="{LGRAY}" stroke-width="1.5"/>'
rows = [('Thìa', 'C', 'C'), ('Chai rỗng', 'C', 'N'), ('Quả cam', 'C', '?'), ('Khối gỗ', 'N', 'N')]
for i, (v, d, k) in enumerate(rows):
    y = 80 + i*24
    b += t(90, y, v, 12, NAVY, '500') + t(170, y, d, 13, ORANGE) + t(240, y, k, 13, GREEN if k != '?' else GRAY)
add('K1', 3, 'Bảng ghi Vật – Đoán – Kết quả', 'Con ghi N (nổi) hay C (chìm) trước khi thả. Đoán sai thì vẽ dấu hỏi.', b)

# ===== G1 =====
b = f'<rect x="0" y="160" width="320" height="40" rx="0" fill="#cfe6c4"/>' + dino(120, 160, 1) + pot(240, 162, True)
b += t(160, 30, 'Tí lỡ quẫy đuôi làm vỡ chậu cây', 14)
add('G1', 1, 'Khủng long Tí làm vỡ chậu cây', 'Tí lỡ làm vỡ chậu cây của bà và định chạy đi.', b)
b = f'<rect x="0" y="160" width="320" height="40" fill="#cfe6c4"/>' + dino(90, 160, 0.85) + dino(230, 162, 1.15, '#7fb069')
b += bubble(14, 24, 140, 40, '"Bà ơi, cháu xin lỗi"', 11.5) + bubble(166, 18, 146, 40, '"Cảm ơn cháu nói thật"', 11.5)
b += heart(160, 110, 1.6)
add('G1', 2, 'Tí nói thật với bà', 'Bà ôm Tí và cảm ơn vì Tí đã nói thật.', b)
b = t(160, 30, 'Dừng – Thở – Nói', 16)
b += f'<circle cx="62" cy="100" r="38" fill="{RED}" stroke="{NAVY}" stroke-width="3"/>' + t(62, 106, 'DỪNG', 15, WHITE, '800')
b += f'<circle cx="160" cy="100" r="38" fill="{LBLUE}" stroke="{NAVY}" stroke-width="3"/><path d="M134 92 q14 -10 28 0 t24 0 M138 108 q12 -8 24 0 t20 0" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>'
b += f'<circle cx="258" cy="100" r="38" fill="{YELLOW}" stroke="{NAVY}" stroke-width="3"/>' + bubble(232, 84, 52, 28, '…', 16)
b += t(62, 160, '1. Dừng lại', 12) + t(160, 160, '2. Thở 1 hơi', 12) + t(258, 160, '3. Nói thật', 12)
add('G1', 3, 'Ba bước Dừng – Thở – Nói', 'Ba bước khi lỡ làm sai: dừng lại, thở một hơi, nói thật.', b)

# ===== T2 =====
b = f'<line x1="20" y1="170" x2="300" y2="170" stroke="{NAVY}" stroke-width="3"/>'
for i, hgt in enumerate([40, 70, 110]):
    x = 50 + i*95
    b += f'<rect x="{x}" y="{170-hgt}" width="44" height="{hgt}" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>'
    b += ''.join(f'<line x1="{x}" y1="{170-hgt+k*14}" x2="{x+44}" y2="{170-hgt+k*14}" stroke="{LGRAY}" stroke-width="2"/>' for k in range(1, hgt//14))
    b += t(x+22, 188, f'Cách {i+1}', 12)
b += star(258, 46, 12) + t(160, 32, 'Mỗi lần thử, tháp cao hơn', 14)
add('T2', 1, 'Tháp giấy qua 3 cách', 'Con thử 3 cách xây tháp giấy và so sánh.', b)
b = ''
for i, (cx, cy, r) in enumerate([(60,150,0),(80,130,25),(100,160,60)]):
    b += f'<g transform="rotate({r} {cx} {cy})">' + cup(cx-17, cy-22, 34, 30, ORANGE) + '</g>'
b += arrow(130, 130, 170, 130, GREEN)
for k in range(3):
    b += cup(205 + (k%2)*0 , 150 - k*32, 34, 30, [ORANGE, YELLOW, PINK][k])
b += t(80, 40, 'Đổ rồi…', 14, RED) + t(222, 40, 'Thử lại!', 14, GREEN)
add('T2', 2, 'Tháp cốc đổ và xây lại', 'Con nhỏ đẩy đổ tháp cốc rồi cùng bố mẹ xây lại.', b)
b = paper(30, 30, 260, 140)
for i in range(3):
    x = 40 + i*84
    b += f'<rect x="{x}" y="58" width="76" height="100" rx="6" fill="#fff7ec" stroke="{NAVY}" stroke-width="1.5"/>' + t(x+38, 76, f'Cách {i+1}', 12)
b += f'<path d="M62 140 v-30 h30 v30" fill="none" stroke="{GRAY}" stroke-width="3"/>' + f'<path d="M150 140 v-40 m16 40 v-40" stroke="{GRAY}" stroke-width="4"/>'
b += f'<path d="M226 140 v-50 m14 50 v-50 m14 50 v-50" stroke="{GREEN}" stroke-width="4"/>' + t(160, 48, '', 1)
add('T2', 3, 'Phiếu Cách 1 – 2 – 3', 'Con vẽ nhanh từng cách đã thử vào phiếu.', b)

# ===== K2 =====
b = cup(80, 50, 40, 110, LBLUE) + cup(190, 105, 80, 55, LBLUE)
b += t(160, 34, 'Cốc nào chứa nhiều nước hơn?', 14) + t(100, 186, 'cao, gầy', 12) + t(230, 186, 'thấp, rộng', 12) + t(160, 120, '?', 30, ORANGE)
add('K2', 1, 'Hai cốc khác dáng', 'Con đoán cốc cao gầy hay cốc thấp rộng chứa nhiều hơn, rồi đo.', b)
b = cup(70, 70, 30, 34, LBLUE, 0.8) 
b += f'<path d="M98 76 q18 8 30 30" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>'
b += cup(120, 96, 60, 74, LBLUE, 0.45)
b += t(250, 70, 'Đếm:', 13) + f'<path d="M222 90 v28 M232 90 v28 M242 90 v28 M252 90 v28 M216 112 l44 -16" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>' + t(250, 150, '= 5 cốc đo', 12, GREEN)
add('K2', 2, 'Rót bằng cốc đo và đếm', 'Dùng một cốc nhỏ làm "cốc đo", đếm số lần rót.', b)
items = [('bọt biển', f'<rect x="-24" y="-14" width="48" height="28" rx="6" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="-10" cy="-2" r="2.5" fill="#d6a32a"/><circle cx="6" cy="4" r="3" fill="#d6a32a"/><circle cx="12" cy="-6" r="2" fill="#d6a32a"/>', 4),
         ('khăn vải', f'<path d="M-24 -14 h48 v28 h-48z" fill="{PINK}" stroke="{NAVY}" stroke-width="2.5"/><path d="M-24 -4 h48 M-24 6 h48" stroke="{WHITE}" stroke-width="2"/>', 3),
         ('giấy ăn', f'<path d="M-22 -14 h44 l-4 28 h-36z" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>', 2),
         ('túi nilon', f'<path d="M-18 -16 h36 l4 30 h-44z" fill="#e8f1f8" stroke="{NAVY}" stroke-width="2.5" opacity=".9"/><path d="M-8 -16 q8 -10 16 0" fill="none" stroke="{NAVY}" stroke-width="2"/>', 0)]
b = t(160, 26, 'Vật nào thấm nhiều nước nhất?', 14)
for i, (lab, ic, drops) in enumerate(items):
    x = 44 + i*77
    b += f'<g transform="translate({x} 82)">{ic}</g>' + t(x, 122, lab, 11.5)
    b += ''.join(f'<path transform="translate({x-12+k*8} 148)" d="M0 -8 q5 6 0 10 q-5 -4 0 -10" fill="{BLUE}"/>' for k in range(drops))
add('K2', 3, 'Thử vật thấm nước', 'Nhúng từng vật, vắt vào cốc đo, đếm xem vật nào giữ nhiều nước nhất.', b)

# ===== G2 =====
b = f'<path d="M110 60 h100 v100 q0 16 -16 16 h-68 q-16 0 -16 -16z" fill="#e9f4fb" stroke="{NAVY}" stroke-width="3"/><rect x="104" y="48" width="112" height="16" rx="5" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/>'
for i, (x, y, r, c) in enumerate([(130,130,-10,YELLOW),(160,140,8,PINK),(186,124,-4,WHITE),(146,108,14,LBLUE),(178,100,-12,YELLOW)]):
    b += f'<rect x="{x-14}" y="{y-9}" width="28" height="18" rx="3" fill="{c}" stroke="{NAVY}" stroke-width="1.5" transform="rotate({r} {x} {y})"/>'
b += heart(70, 80, 1.8) + heart(255, 110, 1.4) + t(160, 30, 'Lọ cảm ơn', 16)
add('G2', 1, 'Lọ cảm ơn', 'Mỗi tối, viết hoặc vẽ điều cảm ơn, bỏ vào lọ nhựa.', b)
b = person(100, 180, 1.1, GREEN) + f'<circle cx="100" cy="118" r="14" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="4 3"/>'
b += f'<circle cx="230" cy="96" r="38" fill="{PINK}" stroke="{NAVY}" stroke-width="3"/><path d="M230 134 q-6 14 4 30" fill="none" stroke="{NAVY}" stroke-width="2"/>'
b += t(230, 102, 'thở ra', 13, NAVY) + t(160, 30, 'Thở bong bóng: tay trên bụng', 14) + arrow(132, 100, 186, 96, BLUE, 3)
add('G2', 2, 'Thở bong bóng', 'Đặt tay lên bụng, hít chậm, thở ra như thổi bong bóng. 3 hơi là đủ.', b)
b = person(70, 182, 1.0, GREEN, False) + person(250, 182, 1.1, BLUE)
b += f'<rect x="140" y="110" width="40" height="34" rx="8" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="148" cy="146" r="6" fill="{NAVY}"/><circle cx="172" cy="146" r="6" fill="{NAVY}"/>'
b += arrow(96, 118, 132, 118, GREEN, 3) + arrow(224, 136, 188, 136, GREEN, 3)
b += bubble(196, 30, 100, 36, '"Cảm ơn!"', 13) + bubble(20, 40, 100, 36, '"Cảm ơn!"', 13)
add('G2', 3, 'Trò đưa – cảm ơn', 'Con nhỏ học nói "cảm ơn" qua trò đưa đồ chơi qua lại.', b)

# ===== T3 =====
b = basket(220, 120, 70, 44) + f'<line x1="40" y1="176" x2="110" y2="176" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 5"/>'
b += sock_ball(70, 150, 13) + f'<path d="M84 140 q70 -90 150 -14" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-dasharray="6 5"/>'
b += f'<ellipse cx="80" cy="60" rx="20" ry="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="80" cy="60" r="6" fill="{NAVY}"/>' + arrow(104, 60, 210, 104, GREEN, 3)
b += t(160, 30, 'Nhìn đích trước rồi mới ném', 14)
add('T3', 1, 'Ném tất vào rổ', 'Lượt 1 nhắm mắt, lượt 2 nhìn rổ rồi ném. Lượt nào trúng nhiều hơn?', b)
b = ''.join(f'<circle cx="80" cy="96" r="{r}" fill="{c}" stroke="{NAVY}" stroke-width="2.5"/>' for r, c in [(54, WHITE), (40, ORANGE), (26, WHITE), (12, RED)])
b += t(80, 170, 'Đích: tự xếp cặp', 12)
b += f'<rect x="160" y="54" width="130" height="34" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>' + t(225, 76, 'Bước 1: để cặp cạnh bàn', 10.5)
b += f'<rect x="160" y="104" width="130" height="34" rx="8" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>' + t(225, 126, 'Bước 2: xếp theo thời khóa biểu', 9.5)
b += arrow(225, 160, 140, 110, GREEN, 3) + check(250, 170) + t(160, 30, 'Đích ngày mai', 15)
add('T3', 2, 'Bảng đích ngày mai', 'Con vẽ đích và 2 bước để tới đích; tối hôm sau tự đánh dấu.', b)
b = f'<rect x="50" y="44" width="90" height="110" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' + slipper(82, 100, -10) + slipper(108, 100, 10)
b += f'<rect x="180" y="44" width="90" height="110" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' + pot(225, 138)
b += t(95, 176, 'Cất dép', 13) + t(225, 176, 'Tưới cây', 13) + t(160, 30, 'Con chọn việc nào?', 14)
add('T3', 3, 'Hai tranh để con nhỏ chọn', 'Con nhỏ chọn 1 trong 2 tranh rồi làm việc đó ngay.', b)

# ===== K3 =====
def clear_cup(x, y, label, wet, sprouts):
    s = f'<path d="M{x} {y} h70 l-8 90 h-54 z" fill="#eef7fc" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round" opacity=".95"/>'
    s += f'<path d="M{x+6} {y+60} h58 l-3 28 h-52 z" fill="{WHITE if not wet else "#d9eef9"}" stroke="{GRAY}" stroke-width="1.5"/>'
    for k in range(4):
        s += bean(x+16+k*13, y+60, k*30)
    for k in range(sprouts):
        s += sprout(x+20+k*16, y+58, 24+k*6)
    s += f'<rect x="{x+8}" y="{y+18}" width="54" height="20" rx="4" fill="{YELLOW}" stroke="{NAVY}" stroke-width="1.5"/>' + t(x+35, y+32, label, 10.5)
    return s
b = clear_cup(40, 50, 'Có nước', True, 0) + clear_cup(210, 50, 'Không nước', False, 0)
b += t(160, 30, 'Ngày 0: gieo hạt, chỉ khác nước', 14) + t(160, 110, 'vs', 16, GRAY)
add('K3', 1, 'Hai cốc thí nghiệm ngày 0', 'Hai cốc giống nhau, chỉ khác một điều: có nước hay không nước.', b)
b = ''.join(bean(70+ (k%4)*28, 90 + (k//4)*26, k*25) for k in range(8))
b += f'<rect x="196" y="60" width="90" height="70" rx="12" fill="{WHITE}" stroke="{NAVY}" stroke-width="2.5"/>' + t(241, 90, 'Người lớn', 12) + t(241, 108, 'giữ túi hạt', 12)
b += t(160, 30, 'Đếm hạt trước và sau buổi', 14) + t(110, 168, '8 hạt mỗi cốc', 13, GREEN)
add('K3', 2, 'Đếm hạt đậu', 'Hạt khô là vật nhỏ: người lớn giữ túi hạt, đếm trước và sau buổi.', b)
b = ''
for d in range(5):
    x = 22 + d*58
    b += f'<rect x="{x}" y="50" width="50" height="100" rx="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>' + t(x+25, 68, f'Ngày {d}', 10.5)
    b += bean(x+25, 132, 0)
    if d >= 2: b += sprout(x+25, 130, 8 + (d-2)*14, 1 if d >= 3 else 0)
b += t(160, 30, 'Nhật ký mầm: mỗi ngày vẽ 1 hình', 14)
add('K3', 3, 'Nhật ký mầm', 'Mỗi ngày con vẽ một hình để thấy hạt thay đổi.', b)

# ===== G3 =====
b = f'<rect x="200" y="40" width="80" height="130" rx="4" fill="{BROWN}" stroke="{NAVY}" stroke-width="3"/><circle cx="268" cy="108" r="4" fill="{YELLOW}"/>'
b += f'<rect x="0" y="170" width="320" height="30" fill="#e7d3b0"/>' + slipper(160, 162, 90, BLUE) + slipper(160, 182, 90, BLUE)
b += cat(90, 176, 1.1) + t(110, 34, 'Mướp xếp dép cho ông', 14)
add('G3', 1, 'Mèo Mướp xếp dép', 'Mướp lặng lẽ xếp dép cho ông, không cần ai khen.', b)
b = f'<rect x="80" y="36" width="160" height="140" rx="8" fill="{ORANGE}" stroke="{NAVY}" stroke-width="3"/><rect x="92" y="46" width="140" height="120" rx="4" fill="{WHITE}"/>'
b += t(162, 68, 'Sổ bí mật', 14)
for i, s in enumerate(['Xếp dép cho ông', 'Gấp khăn cho mẹ', 'Rót nước cho bố']):
    b += check(104, 94 + i*26) + t(130, 98 + i*26, s, 11.5, NAVY, '500', 'start')
b += star(46, 70, 12) + star(276, 150, 10) + heart(278, 70, 1.4)
add('G3', 2, 'Sổ việc tốt bí mật', 'Con lớn ghi 3 việc tốt bí mật cho 3 ngày.', b)
b = person(220, 180, 1.1, ORANGE) + person(90, 180, 1.0, GREEN, False)
b += f'<rect x="104" y="112" width="34" height="22" rx="4" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>' + arrow(146, 120, 190, 120, GREEN, 3)
b += bubble(170, 24, 130, 38, '"Cảm ơn con đã giúp!"', 11.5)
add('G3', 3, 'Con nhỏ giúp mang khăn', 'Con nhỏ mang đồ nhẹ cho người khác và nhận lời cảm ơn.', b)

# ===== T4 =====
b = paper(20, 40, 280, 130)
for i, lab in enumerate(['Trước', 'Trong', 'Sau']):
    x = 20 + i*93
    b += t(x+46, 62, lab, 13, [ORANGE, BLUE, GREEN][i])
    if i: b += f'<line x1="{x}" y1="44" x2="{x}" y2="166" stroke="{LGRAY}" stroke-width="2"/>'
b += block(45, 110, 30, 20, RED) + block(60, 92, 20, 18, YELLOW) + f'<path d="M45 140 h40" stroke="{NAVY}" stroke-width="2"/>' + t(66, 158, 'vẽ kế hoạch', 10.5)
b += block(125, 130, 40, 20, RED) + block(130, 112, 30, 18, YELLOW) + block(138, 94, 16, 18, BLUE) + t(159, 158, 'đang ở bước 2', 10.5)
b += check(234, 120) + t(252, 158, 'giống – đổi gì?', 10.5) + t(160, 28, 'Trước – Trong – Sau', 15)
add('T4', 1, 'Bảng Trước – Trong – Sau', 'Con vẽ kế hoạch trước khi chơi, xem lại giữa chừng, so sánh sau khi chơi.', b)
b = f'<rect x="30" y="50" width="110" height="100" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
b += f'<path d="M64 100 q22 -24 44 0" fill="none" stroke="{SAND}" stroke-width="16" stroke-linecap="round"/>' + ''.join(f'<path transform="translate({70+k*14} {122})" d="M0 -8 q5 6 0 10 q-5 -4 0 -10" fill="{BLUE}"/>' for k in range(3))
b += f'<rect x="180" y="50" width="110" height="100" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/><circle cx="235" cy="100" r="26" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="226" cy="94" r="3" fill="{BROWN}"/><circle cx="242" cy="104" r="3" fill="{BROWN}"/>'
b += arrow(146, 100, 174, 100, GREEN) + t(85, 172, 'Đầu tiên: rửa tay', 12) + t(235, 172, 'Rồi: ăn bánh', 12) + t(160, 32, 'Đầu tiên… rồi…', 15)
add('T4', 2, 'Đầu tiên… rồi…', 'Con nhỏ làm 2 việc theo thứ tự với 2 tranh.', b)
b = paper(30, 50, 110, 110) + f'<path d="M50 130 v-36 l35 -26 l35 26 v36 z" fill="none" stroke="{GRAY}" stroke-width="3" stroke-dasharray="6 4"/>' + t(85, 150, 'bản vẽ', 11)
for r in range(3):
    for c in range(3 - (r == 2)):
        b += block(190 + c*30 + (15 if r == 2 else 0), 140 - r*20, 28, 18, [RED, YELLOW, BLUE][r])
b += f'<path d="M190 82 l45 -30 l45 30 z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>' + t(235, 182, 'nhà đã xây', 11) + t(160, 32, 'Kiến trúc sư giờ chơi', 15)
add('T4', 3, 'Từ bản vẽ đến nhà Lego', 'Kế hoạch giúp con biết mình định làm gì; đổi giữa chừng cũng được.', b)

# ===== K4 =====
b = f'<path d="M60 80 h70 l-8 90 h-54 z" fill="#eef7fc" stroke="{NAVY}" stroke-width="3"/>' + sprout(95, 140, 70)
for k in range(4):
    b += block(160, 150 - k*20, 26, 18, [RED, YELLOW, BLUE, LGREEN][k])
b += f'<line x1="104" y1="70" x2="186" y2="70" stroke="{ORANGE}" stroke-width="2.5" stroke-dasharray="5 4"/>' + t(250, 110, '≈ 4 khối', 16, GREEN) + t(160, 30, 'Mầm cao bằng mấy khối?', 14)
add('K4', 1, 'Đo mầm bằng khối', 'Dựng khối cạnh mầm để đo bằng đơn vị con hiểu được.', b)
b = f'<line x1="50" y1="160" x2="290" y2="160" stroke="{NAVY}" stroke-width="3"/><line x1="50" y1="160" x2="50" y2="40" stroke="{NAVY}" stroke-width="3"/>'
for i, (hgt, c) in enumerate([(80, LGREEN), (96, LGREEN), (64, LGREEN), (4, GRAY), (4, GRAY), (4, GRAY)]):
    x = 66 + i*36 + (20 if i >= 3 else 0)
    b += f'<rect x="{x}" y="{160-hgt}" width="24" height="{hgt}" fill="{c}" stroke="{NAVY}" stroke-width="2"/>'
b += t(120, 182, 'Có nước', 12) + t(232, 182, 'Không nước', 12) + t(160, 30, 'Biểu đồ cột đầu tiên', 14)
add('K4', 2, 'Biểu đồ cột hai cốc', 'Mỗi mầm một cột. Cốc chưa nảy mầm thì cột bằng 0.', b)
b = f'<rect x="40" y="110" width="240" height="30" rx="4" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/>'
b += ''.join(f'<line x1="{50+k*22}" y1="110" x2="{50+k*22}" y2="{124 if k%5 else 132}" stroke="{NAVY}" stroke-width="2"/>' for k in range(11))
b += ''.join(t(50+k*22, 156, str(k), 10, NAVY, '500') for k in range(0, 11, 5))
b += ''.join(block(50+k*30, 80, 26, 18, [RED, BLUE, LGREEN][k % 3]) for k in range(3))
b += t(160, 30, 'Khối trước, thước sau', 14) + t(240, 90, 'cách nào chính xác hơn?', 10.5, GRAY)
add('K4', 3, 'So sánh khối và thước', 'Đo bằng khối trước, rồi thử bằng thước để so sánh.', b)

# ===== G4 =====
b = ''.join(face(50 + i*74, 96, 28, m) + t(50 + i*74, 152, lab, 13) for i, (m, lab) in enumerate([('vui', 'Vui'), ('buon', 'Buồn'), ('gian', 'Giận'), ('so', 'Sợ')]))
b += t(160, 30, 'Bốn gương mặt cảm xúc', 15)
add('G4', 1, 'Bốn gương mặt cảm xúc', 'Vẽ 4 gương mặt to, đơn giản để chơi trò đoán mặt.', b)
b = f'<ellipse cx="200" cy="100" rx="58" ry="70" fill="#dfeef7" stroke="{NAVY}" stroke-width="4"/><rect x="190" y="168" width="20" height="24" fill="{BROWN}" stroke="{NAVY}" stroke-width="2.5"/>'
b += face(200, 96, 30, 'gian') + face(80, 96, 30, 'gian') + t(80, 152, 'mặt con', 12) + t(200, 30, 'gương', 12, GRAY) + t(80, 30, 'Soi gương làm mặt', 13)
add('G4', 2, 'Soi gương làm mặt', 'Con soi gương làm các gương mặt và gọi tên cảm xúc.', b)
b = face(60, 90, 30, 'gian') + arrow(98, 90, 130, 90, NAVY, 3)
b += f'<circle cx="160" cy="90" r="26" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2.5"/><path d="M144 86 q8 -6 16 0 t16 0 M146 96 q8 -6 16 0 t12 0" fill="none" stroke="{NAVY}" stroke-width="2.5" stroke-linecap="round"/>'
b += arrow(190, 90, 214, 90, NAVY, 3) + bubble(218, 60, 92, 52, '', 1) + t(264, 82, 'Con thấy giận', 11) + t(264, 98, 'vì…', 11)
b += t(160, 30, 'Dừng – Thở – Nói', 15) + t(60, 150, 'Dừng', 12) + t(160, 150, 'Thở', 12) + t(262, 150, 'Nói', 12)
add('G4', 3, 'Nói "Con thấy… vì…"', 'Sau khi dừng và thở, con nói rõ cảm xúc và lý do.', b)

def figure_block(code):
    figs = FIGS.get(code, [])
    if not figs: return ''
    items = ''.join(f'<figure><img src="/assets/minh-hoa/{fn}" alt="{html.escape(alt)}" width="320" height="200" loading="lazy"><figcaption>{cap}</figcaption></figure>' for fn, alt, cap in figs)
    return f'<div class="figs">{items}</div>'

if __name__ == '__main__':
    print(sum(len(v) for v in FIGS.values()), 'hình')
