# Hình minh họa và sơ đồ khóa C9 "Vận động an toàn" – tiền tố X / KHOAX
# Người que đơn giản, không mặt chi tiết; ưu tiên sơ đồ quy trình và nguyên lý.
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'
L = f'stroke="{NAVY}" stroke-width="3" stroke-linecap="round" fill="none"'

def chair(x, y, s=1, fill=BROWN):
    # ghế nhìn ngang, lưng ghế bên trái; (x, y) = góc trái mặt ghế
    w = 34 * s; h = 30 * s
    return (f'<path d="M{x} {y - 34*s} V{y + h}" {L.replace(NAVY, fill)}/>'
            f'<rect x="{x}" y="{y - 3*s}" width="{w}" height="{6*s}" rx="2" fill="{fill}" stroke="{NAVY}" stroke-width="2"/>'
            f'<path d="M{x + w - 2*s} {y} V{y + h}" {L.replace(NAVY, fill)}/>')

def head(cx, cy, r=8):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/>'

def stand(x, y, arms='down', lean=0, legs='both', shirt=GREEN):
    # người đứng; (x, y) = điểm giữa hai bàn chân
    hip = (x + lean * 0.4, y - 34); sh = (x + lean, y - 62)
    s = f'<path d="M{hip[0]} {hip[1]} L{sh[0]} {sh[1]}" stroke="{shirt}" stroke-width="7" stroke-linecap="round"/>'
    if legs == 'both':
        s += f'<path d="M{x-7} {y} L{hip[0]} {hip[1]} L{x+7} {y}" {L}/>'
    elif legs == 'one':
        s += f'<path d="M{x} {y} L{hip[0]} {hip[1]} L{x+12} {y-14}" {L}/>'
    elif legs == 'tandem':
        s += f'<path d="M{x-2} {y} L{hip[0]} {hip[1]} L{x+2} {y-2}" {L}/>'
    elif legs == 'toes':
        s += f'<path d="M{x-6} {y-6} L{hip[0]} {hip[1]} L{x+6} {y-6}" {L}/><path d="M{x-10} {y} l6 -6 M{x+2} {y} l6 -6" {L}/>'
    if arms == 'down':
        s += f'<path d="M{sh[0]-12} {sh[1]+28} L{sh[0]} {sh[1]+2} L{sh[0]+12} {sh[1]+28}" {L}/>'
    elif arms == 'hold':
        s += f'<path d="M{sh[0]} {sh[1]+2} L{sh[0]-18} {sh[1]+30}" {L}/>'
    elif arms == 'front':
        s += f'<path d="M{sh[0]} {sh[1]+2} L{sh[0]+28} {sh[1]+6}" {L}/>'
    elif arms == 'up':
        s += f'<path d="M{sh[0]-10} {sh[1]-26} L{sh[0]} {sh[1]+2} L{sh[0]+10} {sh[1]-26}" {L}/>'
    elif arms == 'curl':
        s += (f'<path d="M{sh[0]} {sh[1]+2} L{sh[0]+4} {sh[1]+22} L{sh[0]+10} {sh[1]+6}" {L}/>'
              f'<rect x="{sh[0]+6}" y="{sh[1]-8}" width="8" height="16" rx="3" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>')
    elif arms == 'cross':
        s += f'<path d="M{sh[0]-8} {sh[1]+4} L{sh[0]+8} {sh[1]+14} M{sh[0]+8} {sh[1]+4} L{sh[0]-8} {sh[1]+14}" {L}/>'
    s += head(sh[0] + lean * 0.2, sh[1] - 12)
    return s

def sit(x, y, arms='lap', leg='down', shirt=GREEN):
    # người ngồi trên ghế; (x, y) = mông trên mặt ghế (ghế vẽ riêng)
    sh = (x, y - 30)
    s = f'<path d="M{x} {y} L{sh[0]} {sh[1]}" stroke="{shirt}" stroke-width="7" stroke-linecap="round"/>'
    if leg == 'down':
        s += f'<path d="M{x} {y} L{x+24} {y} L{x+24} {y+30}" {L}/>'
    else:
        s += f'<path d="M{x} {y} L{x+24} {y} L{x+50} {y+8}" {L}/>'
    if arms == 'lap':
        s += f'<path d="M{sh[0]} {sh[1]+2} L{sh[0]+8} {sh[1]+22} L{sh[0]+20} {sh[1]+26}" {L}/>'
    elif arms == 'up':
        s += f'<path d="M{sh[0]-8} {sh[1]-26} L{sh[0]} {sh[1]+2} L{sh[0]+8} {sh[1]-26}" {L}/>'
    elif arms == 'cross':
        s += f'<path d="M{sh[0]-8} {sh[1]+4} L{sh[0]+8} {sh[1]+14} M{sh[0]+8} {sh[1]+4} L{sh[0]-8} {sh[1]+14}" {L}/>'
    s += head(sh[0], sh[1] - 12)
    return s

def floor(y=176):
    return f'<line x1="10" y1="{y}" x2="310" y2="{y}" stroke="{GRAY}" stroke-width="2"/>'

def tiny_chair_back(x, y):
    # lưng ghế để vịn khi đứng, nhìn ngang
    return (f'<path d="M{x} {y-58} V{y}" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>'
            f'<rect x="{x-2}" y="{y-34}" width="30" height="5" rx="2" fill="{BROWN}" stroke="{NAVY}" stroke-width="1.5"/>'
            f'<path d="M{x+26} {y-30} V{y}" stroke="{BROWN}" stroke-width="4" stroke-linecap="round"/>')

# ================= TRANG KHÓA =================
s = t(160, 20, 'Mười bài', 14)
items = [('1. Bắt đầu an toàn', PINK), ('2. Ngồi ít lại', SAND), ('3. Thở, khởi động', LBLUE), ('4. Sức chân', G),
         ('5. Thăng bằng', YELLOW), ('6. Sức tay', PEACH), ('7. Đi bộ tăng dần', G), ('8. Giãn cơ, khớp', PURP),
         ('9. Phòng té ngã', PINK), ('10. Kế hoạch tuần', LGRAY)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 30 + (i // 2) * 33
    s += box(x, y, 142, 27, lab, c, 10.5)
add('KHOAX', 1, 'Mười bài', 'Mỗi bài 25 phút: đọc 10 phút, tập 10 phút, ghi lại 5 phút. Các ngày khác tập ngắn ở nhà.', s)

s = t(160, 22, 'Bốn loại vận động', 14)
s += box(14, 36, 140, 52, ['Sức cơ', 'đứng lên, ngồi xuống'], G, 10.5)
s += box(166, 36, 140, 52, ['Thăng bằng', 'đứng vịn ghế'], YELLOW, 10.5)
s += box(14, 96, 140, 52, ['Đi lại', 'đi bộ, việc nhà'], LBLUE, 10.5)
s += box(166, 96, 140, 52, ['Linh hoạt', 'giãn cơ, xoay khớp'], PURP, 10.5)
s += t(160, 172, 'Và ngồi lì ít lại: mỗi giờ đứng dậy một lần', 10.5, GREEN)
add('KHOAX', 2, 'Bốn loại vận động', 'Khóa tập đủ bốn loại: sức cơ, thăng bằng, đi lại và linh hoạt; kèm thói quen ngồi lì ít lại.', s)

s = t(160, 22, 'Mỗi động tác có 3 mức', 14)
for i, (lab, sub, c) in enumerate([('Dễ', ['có vịn,', 'ít lần'], G), ('Vừa', ['vịn nhẹ,', 'thêm lần'], YELLOW), ('Khó', ['không vịn,', 'chậm hơn'], PEACH)]):
    x = 16 + i * 100; top = 120 - i * 36
    s += box(x, top, 92, 168 - top, [lab] + sub, c, 10.5)
s += t(160, 190, 'Lên mức khi làm dễ dàng khoảng 2 tuần', 10, NAVY)
add('KHOAX', 3, 'Ba mức dễ – vừa – khó', 'Bắt đầu ở mức dễ. Chỉ lên mức khi làm được nhẹ nhàng, không đau, trong khoảng hai tuần.', s)

# ================= BÀI 1 =================
s = t(160, 22, 'Đèn tập luyện', 14)
for i, (c, lab, sub) in enumerate([(LGREEN, 'Xanh', ['Thở nhanh hơn,', 'vẫn nói được câu']),
                                   (YELLOW, 'Vàng', ['Mỏi nhiều, đau cơ,', 'hụt hơi: chậm lại']),
                                   (RED, 'Đỏ', ['Đau ngực, khó thở,', 'chóng mặt: dừng'])]):
    y = 38 + i * 50
    s += f'<circle cx="40" cy="{y + 18}" r="16" fill="{c}" stroke="{NAVY}" stroke-width="2.5"/>' + t(40, y + 22, lab, 9.5, WHITE if i != 1 else NAVY, '800')
    s += box(66, y, 240, 38, sub, WHITE, 10.5)
add('X1', 1, 'Đèn tập luyện', 'Xanh: tập tiếp. Vàng: chậm lại, giảm mức. Đỏ: dừng ngay, ngồi xuống, gọi người giúp; nặng thì gọi 115.', s)

s = t(160, 22, 'Hỏi nhân viên y tế trước khi tập nếu', 12.5)
rows = ['Có bệnh tim, từng đau ngực khi gắng sức', 'Vừa mổ, vừa ốm nặng, gãy xương, đột quỵ', 'Hay chóng mặt, từng ngất, vừa bị ngã',
        'Huyết áp, đường huyết chưa ổn; tiêm insulin', 'Khớp mới sưng, nóng, đỏ']
for i, r in enumerate(rows):
    s += num(26, 46 + i * 28, i + 1, PINK) + t(44, 50 + i * 28, r, 10.5, NAVY, '600', 'start')
s += t(160, 190, 'Có 1 ý "Có" → hỏi trước, rồi tập ở mức dễ', 10, GREEN)
add('X1', 2, 'Khi nào hỏi trước', 'Có một trong năm điều này thì hỏi bác sĩ hoặc nhân viên y tế trước khi bắt đầu tập.', s)

# ================= BÀI 2 =================
s = t(160, 22, 'Mỗi giờ đứng dậy một lần', 14)
s += f'<circle cx="70" cy="100" r="40" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
s += f'<path d="M70 100 V72 M70 100 L90 108" {L}/>' + t(70, 160, 'Chuông nhắc', 10.5)
s += arrow(118, 100, 160, 100, ORANGE, 3)
s += chair(180, 150) + stand(240, 176, 'down') + floor(176)
s += t(240, 192, 'Đứng, đi vài bước', 10.5, GREEN)
add('X2', 1, 'Mỗi giờ đứng dậy', 'Đặt chuông nhắc. Mỗi giờ đứng dậy, đi vài bước, rót cốc nước rồi ngồi lại.', s)

s = t(160, 22, 'Cùng 8 giờ ngồi, hai cách', 13)
s += t(76, 48, 'Ngồi liền một mạch', 10.5) + f'<rect x="20" y="58" width="112" height="22" rx="4" fill="{PINK}" stroke="{NAVY}" stroke-width="2"/>'
s += t(240, 48, 'Chia nhỏ, đứng dậy', 10.5)
for i in range(8):
    s += f'<rect x="{184 + i * 14}" y="58" width="10" height="22" rx="2" fill="{G}" stroke="{NAVY}" stroke-width="1.5"/>'
s += box(20, 104, 280, 50, ['Việc nhỏ: đứng khi nghe điện thoại, tự đi lấy nước,', 'đứng dậy mỗi lần hết một tập phim'], YELLOW, 10.5)
s += t(160, 180, 'Ít ngồi lì hơn là bước đầu, ai cũng làm được', 10, GREEN)
add('X2', 2, 'Chia nhỏ thời gian ngồi', 'Ngồi liền nhiều giờ khác với ngồi rồi đứng dậy thường xuyên. Gắn việc đứng dậy với việc hằng ngày.', s)

# ================= BÀI 3 =================
add('X3', 1, 'Thở chậm trên ghế', 'Ngồi thẳng, thả vai. Hít vào bằng mũi, thở ra chậm hơn. Khi gắng sức, thở đều, không nín thở.',
    t(160, 26, 'Thở chậm 1 phút trên ghế', 14)
    + flow([['Ngồi thẳng', 'thả vai'], ['Hít vào', 'bằng mũi'], ['Thở ra', 'chậm, dài'], ['Lặp lại', '5–6 lần']], 50, 64, 10, 310, 10, 10.5, [LGRAY, LBLUE, G, YELLOW])
    + t(160, 146, 'Khi tập sức: đếm to, thở đều, không nín thở', 10.5, GREEN)
    + t(160, 168, 'Chóng mặt thì dừng, thở bình thường', 10, NAVY))

s = t(160, 22, 'Khởi động 5 phút', 14)
steps = [(['Xoay vai', '5 lần'], LBLUE), (['Xoay cổ tay', '5 lần'], YELLOW), (['Gót – mũi', 'chân, 10 lần'], G), (['Bước tại', 'chỗ 1–2 phút'], PEACH)]
for i, (lab, c) in enumerate(steps):
    x = 10 + i * 76
    s += box(x, 36, 70, 48, lab, c, 9.5)
    if i < 3: s += arrow(x + 71, 60, x + 75, 60, ORANGE, 3)
s += chair(70, 152) + sit(78, 149, 'up') + floor(182)
s += tiny_chair_back(190, 182) + stand(236, 182, 'hold', legs='toes')
s += t(160, 197, 'Sau buổi tập: đi chậm 2–3 phút cho thả lỏng', 9.5, GREEN)
add('X3', 2, 'Khởi động 5 phút', 'Bốn động tác nhẹ làm ấm cơ và khớp trước khi tập. Sau buổi tập, đi chậm vài phút cho thả lỏng.', s)

# ================= BÀI 4 =================
s = t(160, 20, 'Đứng lên – ngồi xuống', 14)
s += chair(14, 120, 0.9) + sit(22, 117)
s += chair(92, 120, 0.9) + f'<path d="M100 117 L100 87" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/><path d="M100 117 L120 117 L112 146" {L}/>' + head(100, 75)
s += chair(170, 120, 0.9) + f'<path d="M184 117 L200 90" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/><path d="M184 117 L200 120 L196 146" {L}/>' + head(206, 80)
s += stand(272, 146, 'cross') + floor(146)
for i, lab in enumerate([['Ngồi', 'mép ghế'], ['Chân', 'lùi sau'], ['Nghiêng', 'tới trước'], ['Đẩy', 'đứng thẳng']]):
    x = 40 + i * 78
    s += num(x - 26, 162, i + 1) + t(x + 10, 160, lab[0], 9.5) + t(x + 10, 172, lab[1], 9.5)
s += t(160, 192, 'Ngồi xuống chậm, đếm 1–2–3', 10.5, GREEN)
add('X4', 1, 'Đứng lên – ngồi xuống', 'Ngồi mép ghế, kéo bàn chân lùi về sau, nghiêng người tới trước rồi đẩy đứng lên. Ngồi xuống thật chậm.', s)

s = t(160, 22, 'Ba mức của động tác ghế', 14)
s += box(14, 40, 92, 110, ['Dễ', '', 'Chống tay', 'lên tay ghế', 'hoặc đùi;', 'ghế cao'], G, 10)
s += box(114, 40, 92, 110, ['Vừa', '', 'Khoanh tay', 'trước ngực;', 'ghế thường'], YELLOW, 10)
s += box(214, 40, 92, 110, ['Khó', '', 'Khoanh tay,', 'ngồi xuống', 'chậm 3 nhịp,', 'thêm lần'], PEACH, 10)
s += t(160, 176, 'Ghế chắc, dựa vào tường, không có bánh xe', 10.5, RED)
add('X4', 2, 'Ba mức động tác ghế', 'Dễ: chống tay, ghế cao. Vừa: khoanh tay. Khó: khoanh tay, ngồi xuống thật chậm và làm thêm lần.', s)

s = t(160, 22, 'Tự đo 30 giây: so mình với mình', 13)
s += f'<circle cx="64" cy="98" r="40" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>' + t(64, 104, '30 giây', 13, ORANGE, '800')
s += box(122, 46, 186, 104, ['Tuần 1: … lần', 'Tuần 5: … lần', 'Tuần 10: … lần', '(chỉ đo khi đứng lên', 'không cần chống tay)'], LGRAY, 10.5)
s += t(160, 178, 'Có người đứng cạnh khi đo', 10.5, GREEN)
add('X4', 3, 'Tự đo 30 giây', 'Đếm số lần đứng lên – ngồi xuống trong 30 giây, khoanh tay, có người đứng cạnh. Ghi lại để so ở tuần 5 và 10.', s)

# ================= BÀI 5 =================
s = t(160, 20, 'Thăng bằng: 4 bậc, luôn vịn ghế', 13)
for i, (lab, legs) in enumerate([('Hai chân sát', 'both'), ('Nửa nối gót', 'tandem'), ('Nối gót', 'tandem'), ('Một chân', 'one')]):
    x = 12 + i * 77
    s += tiny_chair_back(x, 150) + stand(x + 50, 150, 'hold', legs=legs)
    s += t(x + 36, 168, lab, 10)
s += floor(150)
s += t(160, 192, 'Mỗi bậc giữ 10 giây; dễ dàng mới lên bậc sau', 10, GREEN)
add('X5', 1, 'Bốn bậc thăng bằng', 'Hai chân sát, nửa nối gót, nối gót, rồi đứng một chân. Một tay luôn vịn lưng ghế chắc.', s)

s = t(160, 22, 'Chỗ tập thăng bằng an toàn', 13.5)
for i, r in enumerate(['Ghế nặng, dựa tường, hoặc bàn bếp chắc', 'Nền khô, không thảm trơn; đi giày hoặc chân trần', 'Có người ở gần lần đầu',
                       'Đứng cạnh góc tường để có chỗ vịn hai phía', 'Chóng mặt, mệt: không tập hôm nay']):
    s += check(22, 40 + i * 28) + t(44, 50 + i * 28, r, 10.5, NAVY, '600', 'start')
add('X5', 2, 'Chỗ tập thăng bằng', 'Tập thăng bằng ở chỗ có vật vịn chắc, nền khô, có người ở gần. Không tập khi đang chóng mặt.', s)

# ================= BÀI 6 =================
s = t(160, 22, 'Co tay với chai nước', 14)
s += stand(80, 170, 'curl', shirt=GREEN) + floor(170)
s += box(140, 40, 166, 100, ['Dễ: chai 0,5 lít', 'Vừa: chai 1 lít', 'Khó: chai 1,5 lít', '8–12 lần mỗi tay', 'ngồi hoặc đứng'], LBLUE, 10.5)
s += t(160, 190, 'Thở ra khi nâng, hạ xuống chậm', 10.5, GREEN)
add('X6', 1, 'Co tay với chai nước', 'Cầm chai nước, co khuỷu tay đưa chai lên, rồi hạ chậm. Chọn chai nhẹ trước.', s)

s = t(160, 22, 'Đẩy tường', 14)
s += f'<rect x="250" y="40" width="16" height="136" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2"/>'
s += f'<path d="M150 176 L196 92" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/>' + head(204, 80)
s += f'<path d="M196 96 L226 104 L250 98" {L}/><path d="M146 176 L160 140 L172 176" {L}/>' + floor(176)
s += box(14, 44, 120, 92, ['Dễ: đứng gần', 'Vừa: lùi xa hơn', 'Khó: chống', 'tay lên bàn', 'bếp chắc'], PEACH, 10.5)
s += t(160, 194, 'Người thẳng như tấm ván, không chùng lưng', 10, GREEN)
add('X6', 2, 'Đẩy tường', 'Chống hai tay lên tường ngang vai, gập khuỷu đưa người vào gần tường, rồi đẩy ra. Đứng xa hơn là khó hơn.', s)

# ================= BÀI 7 =================
s = t(160, 22, 'Phép thử nói chuyện', 14)
for i, (lab, sub, c) in enumerate([('Hát được', 'Nhẹ', G), ('Nói được câu,', 'không hát được: Vừa', YELLOW), ('Chỉ nói vài từ', 'Mạnh', PEACH)]):
    y = 38 + i * 46
    s += box(20, y, 280, 38, [lab, sub] if i != 1 else [lab, sub], c, 10.5)
s += t(160, 188, 'Người mới tập: nhẹ đến vừa là đủ', 10.5, GREEN)
add('X7', 1, 'Phép thử nói chuyện', 'Đi mà vẫn nói được câu nhưng không hát được là mức vừa. Chỉ nói được vài từ là quá sức với người mới tập.', s)

s = t(160, 22, 'Tăng dần, mỗi tuần thêm một chút', 13)
vals = [5, 7, 10, 12, 15, 20]
for i, v in enumerate(vals):
    h = v * 5; x = 30 + i * 46
    s += f'<rect x="{x}" y="{168 - h}" width="32" height="{h}" rx="4" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>'
    s += t(x + 16, 162 - h, f'{v}\'', 10.5) + t(x + 16, 184, f'T{i + 1}', 10)
s += t(160, 198, 'Ví dụ; ốm, mệt thì quay lại mức trước', 9.5, GRAY)
add('X7', 2, 'Tăng dần thời gian đi', 'Ví dụ: bắt đầu 5 phút, mỗi tuần thêm vài phút. Có thể chia thành nhiều lần ngắn trong ngày.', s)

# ================= BÀI 8 =================
s = t(160, 20, 'Giãn cơ nhẹ nhàng', 14)
s += chair(20, 140) + sit(28, 137, 'up') + t(52, 190, 'Với tay lên', 10)
s += f'<rect x="282" y="40" width="14" height="136" fill="{LGRAY}" stroke="{NAVY}" stroke-width="2"/>'
s += f'<path d="M236 136 L262 92" stroke="{GREEN}" stroke-width="7" stroke-linecap="round"/>' + head(268, 80)
s += f'<path d="M262 96 L282 98" {L}/><path d="M210 176 L236 136 L254 176" {L}/>' + t(244, 192, 'Giãn bắp chân', 10)
s += chair(110, 140) + sit(118, 137, 'lap', leg='out') + t(150, 190, 'Duỗi chân', 10)
s += floor(176)
add('X8', 1, 'Ba động tác giãn cơ', 'Với tay lên cao khi ngồi; duỗi một chân, nghiêng nhẹ người tới; tựa tường giãn bắp chân.', s)

s = t(160, 22, 'Giãn đúng cách', 14)
s += box(14, 40, 140, 110, ['Nên', '', 'Sau khi đi bộ,', 'cơ đã ấm', 'Căng nhẹ, chậm', 'Thở đều'], G, 10.5)
s += box(166, 40, 140, 110, ['Không', '', 'Nhún, giật', 'Cố tới đau', 'Nín thở', 'Ép khớp đang sưng'], PINK, 10.5)
s += t(160, 178, 'Giữ khoảng 3–5 hơi thở chậm, rồi thả', 10.5, NAVY)
add('X8', 2, 'Nên và không khi giãn cơ', 'Giãn khi cơ đã ấm, căng nhẹ và thở đều. Không nhún, không cố tới mức đau.', s)

# ================= BÀI 9 =================
s = t(160, 18, 'Khi bị ngã: đứng dậy từ từ', 13.5)
steps = ['Nằm yên, thở, tự kiểm tra đau', 'Lăn nghiêng người', 'Chống tay và gối', 'Bò tới ghế chắc', 'Một chân lên, vịn ghế đứng dậy', 'Ngồi nghỉ, báo người nhà']
for i, st in enumerate(steps):
    y = 30 + i * 26
    s += num(26, y + 8, i + 1) + t(44, y + 12, st, 10.5, NAVY, '600', 'start')
s += t(160, 190, 'Đau đầu, hông, lưng, cổ: không cố dậy, gọi 115', 10, RED)
add('X9', 1, 'Đứng dậy sau khi ngã', 'Làm từ từ theo sáu bước. Nếu đau ở đầu, hông, lưng, cổ hoặc không dậy được: nằm yên và gọi người giúp.', s)

s = t(160, 22, 'Không dậy được thì làm gì', 13.5)
s += box(14, 40, 92, 100, ['Gọi', '', 'Điện thoại,', 'gọi to, gõ', 'xuống sàn'], PINK, 10.5)
s += box(114, 40, 92, 100, ['Giữ ấm', '', 'Kéo khăn,', 'áo, chăn', 'đắp lên'], YELLOW, 10.5)
s += box(214, 40, 92, 100, ['Cử động', '', 'Co duỗi tay', 'chân; đổi', 'tư thế'], G, 10.5)
s += t(160, 166, 'Mang điện thoại theo người khi ở nhà một mình', 10.5, GREEN)
add('X9', 2, 'Khi không dậy được', 'Gọi người giúp, giữ ấm, cử động tay chân và đổi tư thế trong lúc chờ.', s)

s = t(160, 22, 'Ba cách giảm té ngã', 14)
s += box(14, 40, 92, 104, ['Tập sức', 'và thăng', 'bằng đều', '(bài 4–5)'], G, 10.5)
s += box(114, 40, 92, 104, ['Nhà an toàn', 'đèn, tay vịn,', 'nền khô'], LBLUE, 10.5)
s += box(214, 40, 92, 104, ['Hỏi thuốc,', 'khám mắt', 'khi hay', 'chóng mặt'], YELLOW, 10.5)
s += t(160, 170, 'Đã ngã một lần: nói với nhân viên y tế', 10.5, RED)
add('X9', 3, 'Ba cách giảm té ngã', 'Tập sức và thăng bằng đều; làm nhà an toàn hơn; hỏi về thuốc và khám mắt khi hay chóng mặt.', s)

# ================= BÀI 10 =================
s = t(160, 18, 'Tuần mẫu (mức dễ)', 13)
days = ['T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'CN']
plan = {'Sức': [1, 0, 1, 0, 1, 0, 0], 'Thăng bằng': [1, 1, 1, 0, 1, 1, 0], 'Đi bộ': [1, 1, 1, 1, 1, 1, 1], 'Giãn': [1, 0, 1, 0, 1, 0, 1]}
cols = [G, YELLOW, LBLUE, PURP]
for j, d in enumerate(days):
    s += t(104 + j * 30, 38, d, 10)
for i, (k, row) in enumerate(plan.items()):
    y = 48 + i * 30
    s += t(14, y + 16, k, 10.5, NAVY, '600', 'start')
    for j, v in enumerate(row):
        s += f'<rect x="{92 + j * 30}" y="{y}" width="24" height="22" rx="4" fill="{cols[i] if v else WHITE}" stroke="{NAVY}" stroke-width="1.5"/>'
s += t(160, 190, 'Mỗi ngày 10–20 phút, chia nhỏ cũng được', 10.5, GREEN)
add('X10', 1, 'Tuần mẫu', 'Một tuần mẫu: sức cơ 2–3 ngày, thăng bằng từ 3 ngày, đi bộ hằng ngày, giãn cơ sau đi bộ. Sửa cho hợp với mình.', s)

s = t(160, 22, 'Vòng giữ thói quen', 14)
s += cycle([['Chọn giờ', 'cố định'], ['Tập', 'mức hợp'], ['Ghi lại', 'vào sổ'], ['Xem lại', 'mỗi tuần']], 160, 110, 60, 92, 34, 10, [G, YELLOW, LBLUE, PEACH])
add('X10', 2, 'Vòng giữ thói quen', 'Chọn giờ cố định, tập ở mức hợp với mình, ghi lại, mỗi tuần xem lại và chỉnh mức.', s)

if __name__ == '__main__':
    print(sum(1 for k in FIGS if k.startswith('X') or k == 'KHOAX'), 'nhóm hình C9')
