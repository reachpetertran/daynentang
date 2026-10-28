# Hình minh họa và sơ đồ khóa G2 "Gia đình 0–2 tuổi – Giao và Đáp"
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'

def baby(x, y, s=1, fill=SAND):
    """Em bé ngồi, đơn giản, không có mặt chi tiết."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<ellipse cx="0" cy="-6" rx="18" ry="16" fill="{YELLOW}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<circle cx="0" cy="-34" r="14" fill="{fill}" stroke="{NAVY}" stroke-width="2.5"/>'
            f'<path d="M-6 -48 q6 -6 10 0" stroke="{NAVY}" stroke-width="2" fill="none"/></g>')

def ball_toss(x1, y1, x2, y2, c=ORANGE):
    mx, my = (x1 + x2) / 2, min(y1, y2) - 40
    return f'<path d="M{x1} {y1} Q{mx} {my} {x2} {y2}" fill="none" stroke="{c}" stroke-width="3" stroke-dasharray="6 5"/>'

# ================= TRANG KHÓA =================
add('KHOAR', 1, 'Giao và đáp', 'Con "giao" bằng ánh mắt, tiếng bập bẹ, chỉ tay. Bố mẹ "đáp" lại. Qua lại nhiều lần như chuyền bóng.',
    t(160, 24, 'Giao và đáp như chuyền bóng', 14) + baby(44, 150, 1.0) + person(282, 170, 0.85, BLUE)
    + ball_toss(64, 96, 260, 96) + ball_toss(260, 116, 64, 116, GREEN)
    + t(160, 70, 'Con giao: "a… a…" + chỉ tay', 11, ORANGE) + t(160, 160, 'Bố mẹ đáp: "À, con chim!"', 11, GREEN) + t(160, 190, 'Lặp lại nhiều lần mỗi ngày', 11.5, NAVY))
add('KHOAR', 2, 'Năm bước giao và đáp', 'Năm bước theo Harvard Center on the Developing Child: nhận ra, đáp lại, gọi tên, thay phiên và chờ, kết thúc và bắt đầu.',
    t(160, 24, 'Năm bước, mỗi tuần một bước', 14)
    + flow([['1. Nhận', 'ra lời', 'giao'], ['2. Đáp', 'lại'], ['3. Gọi', 'tên']], 38, 62, 10, 310, 16, 10.5, [SAND, YELLOW, LBLUE])
    + flow([['4. Thay', 'phiên', 'và chờ'], ['5. Kết thúc', 'và bắt', 'đầu']], 116, 62, 60, 260, 20, 10.5, [G, PURP])
    + t(160, 194, 'Tuần 6–8: đọc sách, vận động, khi con khóc', 10.5, GREEN))

# ================= TUẦN 1–5 (năm bước) =================
s = t(160, 22, 'Con giao bằng gì?', 14) + baby(160, 130, 1.2)
for (x, y, lab) in [(40, 60, 'Nhìn'), (280, 60, 'Bập bẹ'), (40, 150, 'Chỉ tay'), (280, 150, 'Với lấy'), (160, 190, 'Khóc, cười')]:
    s += box(x - 36, y - 14, 72, 28, lab, WHITE, 11) if y != 190 else t(x, y, lab, 11.5, ORANGE, '700')
s += arrow(80, 66, 130, 92, ORANGE, 2.5) + arrow(240, 66, 190, 92, ORANGE, 2.5) + arrow(80, 148, 130, 124, ORANGE, 2.5) + arrow(240, 148, 190, 124, ORANGE, 2.5)
add('R1', 1, 'Lời giao của con', 'Con "giao" bằng ánh mắt, tiếng bập bẹ, chỉ tay, với lấy, cười hay khóc.', s)
s = t(160, 22, 'Nhìn theo con nhìn', 14) + baby(80, 150, 1) + person(160, 172, 0.8, BLUE)
s += f'<circle cx="262" cy="70" r="20" fill="{RED}" stroke="{NAVY}" stroke-width="2.5"/>' + t(262, 106, 'quả bóng', 10.5)
s += f'<path d="M86 108 L240 74" stroke="{ORANGE}" stroke-width="2" stroke-dasharray="4 4"/><path d="M164 92 L240 76" stroke="{GREEN}" stroke-width="2" stroke-dasharray="4 4"/>'
s += t(160, 194, 'Con nhìn đâu, bố mẹ nhìn đó', 11.5, GREEN)
add('R1', 2, 'Cùng nhìn một chỗ', 'Bước 1: để ý con đang nhìn gì, rồi cùng nhìn theo.', s)

add('R2', 1, 'Cách đáp lại', 'Đáp lại bằng nụ cười, cái gật đầu, cái chạm, lời nói hay đưa đồ con đang với.',
    t(160, 28, 'Đáp lại bằng', 14) + flow([['Nụ', 'cười'], ['Gật', 'đầu'], ['Chạm,', 'ôm'], ['Lời', 'nói'], ['Đưa', 'đồ']], 50, 64, 8, 312, 8, 11,
    [YELLOW, LBLUE, PINK, G, SAND]) + t(160, 150, 'Đáp ngay, ấm áp, không cần hoàn hảo', 11.5, GREEN))
s = t(160, 22, 'Khi bố mẹ không đáp', 14)
s += box(14, 40, 140, 90, ['Con giao', '→ không ai đáp', '→ con thôi giao'], LGRAY, 11)
s += box(166, 40, 140, 90, ['Con giao', '→ được đáp', '→ con giao tiếp'], G, 11)
s += t(84, 154, 'Điện thoại, tivi', 10.5, RED) + t(84, 170, 'làm ta lỡ lời giao', 10.5, RED) + check(226, 150)
add('R2', 2, 'Đáp và không đáp', 'Khi lời giao không được đáp, con dần ít giao hơn. Điện thoại dễ làm bố mẹ lỡ lời giao.', s)

s = t(160, 22, 'Gọi tên điều con thấy', 14) + baby(70, 150, 1)
s += bubble(120, 40, 186, 34, '"Cái thìa. Thìa màu xanh."', 11) + bubble(120, 84, 186, 34, '"Con đang gõ: cộc cộc!"', 11) + bubble(120, 128, 186, 34, '"Con vui quá, con cười."', 11)
add('R3', 1, 'Gọi tên', 'Bước 3: gọi tên đồ vật, việc con làm và cảm xúc của con, bằng câu ngắn.', s)
s = t(160, 22, 'Nói to việc mình làm', 14)
for i, ln in enumerate(['"Mẹ rửa rau. Nước chảy róc rách."', '"Bố bế con. Mình đi ra sân."', '"Áo này ướt. Mình thay áo khô."']):
    s += box(14, 40 + i*44, 292, 34, ln, [LBLUE, YELLOW, G][i], 11)
s += t(160, 186, 'Như kể bình luận trận bóng', 11, GREEN)
add('R3', 2, 'Kể việc đang làm', 'Trong lúc làm việc nhà, bố mẹ nói to việc mình đang làm bằng câu ngắn.', s)

s = t(160, 22, 'Thay phiên và chờ', 14)
for i, (who, c) in enumerate([('Con', ORANGE), ('Bố mẹ', BLUE), ('Con', ORANGE), ('Bố mẹ', BLUE)]):
    x = 30 + i*72
    s += f'<circle cx="{x+20}" cy="80" r="22" fill="{c}" stroke="{NAVY}" stroke-width="2.5"/>' + t(x + 20, 84, who, 9.5, WHITE, '700')
    if i < 3: s += arrow(x + 44, 80, x + 70, 80, NAVY, 2.5)
s += box(40, 120, 240, 40, ['Chờ đếm thầm 5–10', 'trước khi nói tiếp'], YELLOW, 11.5)
add('R4', 1, 'Thay phiên', 'Bước 4: đến lượt con, bố mẹ chờ. Đếm thầm đến 5 hoặc 10 để con kịp đáp.', s)
s = t(160, 22, 'Trò ú òa', 14) + baby(90, 160, 1)
s += f'<rect x="196" y="60" width="70" height="60" rx="8" fill="{PINK}" stroke="{NAVY}" stroke-width="2.5"/>' + t(231, 94, 'khăn', 11)
s += t(231, 146, '"Bố đâu rồi?"', 11) + t(231, 164, '… chờ …', 11, GRAY) + t(231, 182, '"Ú òa!"', 12, ORANGE, '800')
add('R4', 2, 'Ú òa', 'Trò ú òa tập thay phiên: bố mẹ trốn, chờ con nhìn, rồi xuất hiện.', s)

add('R5', 1, 'Nhận ra con muốn dừng', 'Bước 5: con quay đi, cáu, ngáp, dụi mắt là dấu hiệu muốn dừng. Để con dẫn sang việc mới.',
    t(160, 26, 'Con muốn dừng khi', 14) + flow([['Quay', 'mặt đi'], ['Ngáp,', 'dụi mắt'], ['Cáu,', 'đẩy ra'], ['Với đồ', 'khác']], 46, 64, 8, 312, 10, 11,
    [LGRAY, LBLUE, PINK, YELLOW]) + arrow(160, 116, 160, 136, ORANGE, 3) + box(70, 140, 180, 34, 'Dừng, đổi việc, hoặc nghỉ', G, 11.5))
s = t(160, 22, 'Ngủ an toàn', 14)
s += f'<rect x="60" y="60" width="200" height="90" rx="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="3"/>'
s += f'<rect x="70" y="120" width="180" height="22" rx="4" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>'
s += f'<circle cx="110" cy="108" r="12" fill="{SAND}" stroke="{NAVY}" stroke-width="2"/><rect x="122" y="100" width="56" height="18" rx="8" fill="{LGREEN}" stroke="{NAVY}" stroke-width="2"/>'
s += t(160, 168, 'Nằm ngửa · mặt phẳng, cứng · không gối, chăn, thú bông', 10.5, GREEN) + t(160, 188, 'Ngủ cùng phòng, không chung giường', 10.5, NAVY, '700')
add('R5', 2, 'Ngủ an toàn', 'Theo AAP 2022: đặt con nằm ngửa, trên mặt phẳng cứng, không đồ mềm; ngủ cùng phòng nhưng không chung giường.', s)

# ================= TUẦN 6–8 =================
s = t(160, 22, 'Đọc sách theo tuổi', 14)
for i, (age, txt, c) in enumerate([('0–6 tháng', ['Nhìn tranh to,', 'nghe giọng', 'bố mẹ'], LBLUE), ('6–12 tháng', ['Sờ, cầm, gặm', 'sách vải,', 'bìa cứng'], YELLOW), ('12–24 tháng', ['Chỉ tranh,', 'gọi tên,', 'lật trang'], G)]):
    x = 14 + i*102
    s += box(x, 46, 94, 104, [age, ''] + txt, c, 10.5)
s += t(160, 170, 'Bắt đầu từ lúc mới sinh', 12, GREEN, '700')
add('R6', 1, 'Đọc sách theo tuổi', 'AAP khuyên đọc to cho con từ lúc mới sinh. Cách đọc thay đổi theo tuổi.', s)
s = t(160, 22, 'Sách tự làm', 14) + paper(40, 40, 110, 140) + paper(170, 40, 110, 140)
s += f'<circle cx="95" cy="96" r="24" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>' + t(95, 160, 'quả táo', 11)
s += cat(225, 120, 0.7) + t(225, 160, 'con mèo', 11)
add('R6', 2, 'Sách tự làm', 'Dán ảnh hoặc vẽ đồ quen trong nhà lên bìa cứng, đục lỗ, buộc lại thành sách.', s)
s = t(160, 22, 'Đồ chơi tự làm', 14)
s += bottle(60, 60, 1.1) + t(60, 170, 'chai lắc', 11) + t(60, 186, '(nắp dán chặt)', 9.5, RED)
s += f'<rect x="130" y="80" width="60" height="60" rx="6" fill="{SAND}" stroke="{NAVY}" stroke-width="2.5"/><circle cx="160" cy="80" r="10" fill="{WHITE}" stroke="{NAVY}" stroke-width="2"/>' + t(160, 170, 'hộp thả đồ', 11)
s += block(230, 110, 30, 30, BLUE) + block(240, 80, 30, 30, YELLOW) + t(255, 170, 'hộp xếp chồng', 11)
add('R7', 1, 'Đồ chơi tự làm', 'Chai lắc dán chặt nắp, hộp thả đồ, hộp xếp chồng: làm từ đồ có sẵn, mọi chi tiết to hơn lõi giấy vệ sinh.', s)
s = t(160, 22, 'Vận động mỗi ngày', 14)
s += box(14, 40, 140, 110, ['Dưới 1 tuổi', '', 'Nằm sấp khi thức,', 'ít nhất 30 phút', 'chia nhiều lần'], LBLUE, 10.5)
s += box(166, 40, 140, 110, ['1–2 tuổi', '', 'Vận động ít nhất', '180 phút', 'cả ngày cộng lại'], G, 10.5)
s += t(160, 176, 'Không ngồi xe đẩy, ghế ăn quá 1 giờ liền', 11, NAVY, '600') + t(160, 194, 'Theo WHO 2019', 9.5, GRAY, '500')
add('R7', 2, 'Vận động theo tuổi', 'Khuyến nghị WHO 2019 cho trẻ dưới 1 tuổi và 1–2 tuổi.', s)
add('R8', 1, 'Khi con khóc mãi', 'Kiểm tra nhu cầu, thử dỗ, nếu mình bực thì đặt con chỗ an toàn và nghỉ một chút. Không bao giờ lắc con.',
    t(160, 24, 'Khi con khóc mãi', 14) + flow([['Kiểm', 'tra: đói,', 'ướt, ốm?'], ['Dỗ: ru,', 'hát, bế', 'đi'], ['Bực quá:', 'đặt con', 'nơi an toàn'], ['Nghỉ,', 'gọi', 'người giúp']],
    40, 80, 8, 312, 10, 10.5, [SAND, LBLUE, YELLOW, G]) + box(40, 140, 240, 40, 'KHÔNG BAO GIỜ LẮC CON', '#f7c9c5', 13, RED))
s = t(160, 22, 'Mốc phát triển: để ý, không lo vội', 13.5)
s += box(14, 40, 292, 50, ['Mốc trong danh sách CDC là việc', 'khoảng 75% trẻ cùng tuổi làm được'], LBLUE, 11)
s += arrow(160, 92, 160, 108, ORANGE, 3) + box(14, 112, 292, 50, ['Con chưa làm được, hay mất kỹ năng đã có:', 'hỏi bác sĩ nhi, đừng chờ'], YELLOW, 11)
add('R8', 2, 'Mốc phát triển', 'Danh sách mốc CDC 2022 dùng ngưỡng 75% trẻ. Nếu lo, hỏi bác sĩ nhi sớm.', s)

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k.startswith(('R', 'KHOAR'))), 'hình G2')
