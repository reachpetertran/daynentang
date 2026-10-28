# Hình minh họa và sơ đồ khóa G8 "Nhà gọn, nhà an toàn" (N) và G9 "Gia đình và cộng đồng" (Q)
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'
def kid(x, y, s=1, shirt=ORANGE): return person(x, y, s, shirt, False)
def warn_list(title, items, foot, foot_c=RED):
    s = t(160, 22, title, 14)
    for i, r in enumerate(items):
        y = 38 + i * 34
        s += f'<circle cx="28" cy="{y+13}" r="11" fill="{RED}" stroke="{NAVY}" stroke-width="2"/>' + t(28, y + 17, '!', 13, WHITE, '800') + box(46, y, 260, 26, r, WHITE, 10.5)
    return s + t(160, 192, foot, 11, foot_c)
def grid4(title, items, foot, size=11):
    s = t(160, 22, title, 14)
    for i, (lab, c) in enumerate(items):
        x = 14 + (i % 2) * 150; y = 38 + (i // 2) * 70
        s += box(x, y, 142, 62, lab if isinstance(lab, list) else [lab], c, size)
    return s + t(160, 190, foot, 11.5, GREEN)

# ===================== G8 =====================
add('KHOAN', 1, 'Bốn tuần', 'Rà soát an toàn, phòng cháy, nhà gọn và bữa ăn an toàn, lịch bảo trì và sơ cứu.',
    t(160, 30, 'Bốn tuần, bốn việc', 14) + flow([['Tuần 1', 'Rà soát', 'an toàn'], ['Tuần 2', 'Phòng', 'cháy'], ['Tuần 3', 'Nhà gọn,', 'bữa an toàn'], ['Tuần 4', 'Bảo trì,', 'sơ cứu']],
    56, 82, 8, 312, 10, 10.5, [LBLUE, PINK, G, YELLOW]) + t(160, 166, 'Mỗi tuần: 1 buổi bố mẹ + việc cùng con', 12, GREEN))
add('KHOAN', 2, 'Năm nguy cơ trong nhà', 'Năm nguy cơ thường gặp với trẻ trong nhà: nước, ngã, bỏng và lửa, ngộ độc, hóc và đồ đổ.',
    grid4('Năm nguy cơ trong nhà', [(['Nước', 'xô, chậu, bể'], LBLUE), (['Ngã', 'cầu thang, ban công'], YELLOW), (['Bỏng, lửa', 'bếp, nước sôi, sạc'], PINK), (['Ngộ độc, hóc', 'hóa chất, thuốc, đồ nhỏ'], G)],
    '+ tủ, tivi đổ: bắt vít vào tường'))
add('N1', 1, 'Đi một vòng nhà', 'Đi từng phòng, ngồi xuống ngang tầm mắt con, tìm nguy cơ và sửa ngay việc dễ.',
    t(160, 28, 'Đi một vòng nhà', 14) + flow([['Ngồi', 'ngang', 'tầm con'], ['Tìm', 'nguy cơ'], ['Sửa ngay', 'việc dễ'], ['Ghi việc', 'cần mua,', 'cần thợ']], 52, 80, 8, 312, 10, 10.5,
    [SAND, YELLOW, G, LBLUE]) + t(160, 160, 'Mỗi phòng 5 phút', 12, GREEN))
s = t(160, 22, 'Nước: một ít cũng nguy hiểm', 14)
s += basin(40, 110, 110, 50) + f'<path d="M48 126 h94" stroke="{BLUE}" stroke-width="6"/>' + t(95, 182, 'đổ nước ngay', 11, GREEN, '700')
s += f'<rect x="190" y="80" width="90" height="80" rx="6" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2.5"/><path d="M186 80 h98" stroke="{BROWN}" stroke-width="8"/>' + t(235, 182, 'bể, lu: có nắp', 11, GREEN, '700')
s += t(160, 50, 'Người lớn trong tầm tay, không để trẻ lớn trông trẻ nhỏ', 10.5, RED)
add('N1', 2, 'Nước', 'Đổ nước xô chậu ngay sau khi dùng, đậy nắp bể và lu, người lớn luôn trong tầm tay khi trẻ ở gần nước.', s)
add('N2', 1, 'Kế hoạch thoát nạn', 'Vẽ sơ đồ nhà, hai lối ra mỗi phòng nếu có, chỗ hẹn gặp ngoài nhà, tập mỗi năm hai lần.',
    t(160, 28, 'Kế hoạch thoát nạn', 14) + flow([['Vẽ', 'sơ đồ', 'nhà'], ['Hai', 'lối ra'], ['Chỗ hẹn', 'ngoài', 'nhà'], ['Tập', 'cả nhà']], 52, 80, 8, 312, 10, 10.5,
    [SAND, YELLOW, G, LBLUE]) + t(160, 158, 'Thoát ra trước, gọi 114 sau', 12, RED, '700') + t(160, 178, 'Không quay lại lấy đồ', 11, NAVY, '600'))
add('N2', 2, 'Sạc xe điện an toàn', 'Không sạc qua đêm hay khi không có người; dùng sạc chính hãng; không sạc trong phòng kín gần đồ dễ cháy.',
    warn_list('Sạc xe điện, điện thoại an toàn', ['Không sạc qua đêm, khi vắng người', 'Dùng sạc, pin chính hãng', 'Không sạc gần đồ dễ cháy, lối thoát', 'Không tự độ pin, độ máy'], 'Có bình chữa cháy ở chỗ dễ lấy'))
add('N3', 1, 'Mỗi đồ một chỗ', 'Gọn nhà theo vòng: bỏ bớt, chọn chỗ, dán nhãn, cất lại 10 phút mỗi ngày.',
    t(160, 22, 'Gọn nhà theo vòng', 14) + cycle([['Bỏ', 'bớt'], ['Chọn', 'chỗ'], ['Dán', 'nhãn'], ['Cất lại', '10 phút']], 160, 118, 64, 88, 34, 10.5, [PINK, YELLOW, LBLUE, G]))
add('N3', 2, 'Năm chìa khóa an toàn thực phẩm', 'Theo WHO: sạch sẽ; để riêng sống và chín; nấu kỹ; giữ nhiệt độ an toàn; nước và nguyên liệu an toàn.',
    t(160, 26, 'Năm chìa khóa thực phẩm an toàn', 13.5) + flow([['Sạch', 'tay, dao,', 'thớt'], ['Sống', 'riêng', 'chín'], ['Nấu', 'kỹ'], ['Không để', 'ngoài', 'quá 2 giờ'], ['Nước,', 'đồ tươi', 'an toàn']],
    46, 84, 6, 314, 6, 10, [LBLUE, PINK, YELLOW, G, SAND]) + t(160, 160, 'Theo WHO', 10, GRAY, '500'))
s = t(160, 22, 'Lịch bảo trì', 14) + paper(24, 32, 272, 158)
for i, (when, what) in enumerate([('Mỗi tháng', 'Thử báo khói, xem bình chữa cháy'), ('Mỗi quý', 'Kiểm ổ cắm, dây điện, van gas'), ('Mỗi năm', 'Vệ sinh máy lạnh, bình nóng'), ('Trước mùa mưa', 'Mái, máng nước, đồ cần kê cao')]):
    y = 60 + i * 34
    s += t(40, y, when, 11, ORANGE, '800', 'start') + t(126, y, what, 10, NAVY, '600', 'start')
add('N4', 1, 'Lịch bảo trì', 'Việc kiểm tra theo tháng, quý, năm và trước mùa mưa. Ví dụ; mỗi nhà điều chỉnh.', s)
add('N4', 2, 'Sơ cứu bỏng', 'Làm mát bằng nước mát đang chảy 20 phút; tháo nhẫn, đồ quanh vết bỏng; không bôi đá, kem đánh răng, mỡ; đi khám khi cần.',
    t(160, 26, 'Sơ cứu bỏng', 14) + flow([['Nước mát', 'đang chảy', '20 phút'], ['Tháo', 'nhẫn,', 'đồ quanh'], ['Không đá,', 'không kem', 'đánh răng'], ['Đi khám', 'nếu phồng,', 'rộng']],
    46, 84, 8, 312, 10, 10.5, [LBLUE, YELLOW, '#f7c9c5', G]) + t(160, 162, 'Khẩn cấp: 115', 13, RED, '800'))

# ===================== G9 =====================
add('KHOAQ', 1, 'Vòng tròn gia đình', 'Từ nhà mình ra ông bà, họ hàng, hàng xóm, rồi cộng đồng. Mỗi vòng là một nguồn hỗ trợ.',
    t(52, 20, 'Vòng tròn', 13) + t(52, 36, 'quanh con', 13)
    + ''.join(f'<circle cx="190" cy="104" r="{r}" fill="{c}" stroke="{NAVY}" stroke-width="2"/>' for r, c in [(92, SAND), (68, LBLUE), (44, YELLOW), (20, PINK)])
    + t(190, 108, 'Nhà', 10, NAVY, '700') + t(190, 74, 'Ông bà', 10) + t(190, 51, 'Họ hàng, hàng xóm', 10) + t(190, 27, 'Cộng đồng', 10))
add('KHOAQ', 2, 'Bốn tuần', 'Ông bà và chuyện gia đình, mạng lưới giúp nhau, kế hoạch màn hình, giúp cộng đồng.',
    t(160, 30, 'Bốn tuần', 14) + flow([['Tuần 1', 'Ông bà,', 'chuyện nhà'], ['Tuần 2', 'Họ hàng,', 'hàng xóm'], ['Tuần 3', 'Màn hình', 'gia đình'], ['Tuần 4', 'Giúp', 'cộng đồng']],
    56, 82, 8, 312, 10, 10.5, [SAND, LBLUE, PURP, G]) + t(160, 166, 'Mỗi tuần: 1 buổi bố mẹ + việc cả nhà', 12, GREEN))
s = t(160, 22, 'Con phỏng vấn ông bà', 14) + person(44, 170, 0.8, PURP) + kid(100, 170, 0.8)
for i, q in enumerate(['"Hồi nhỏ ông chơi gì?"', '"Bà gặp ông thế nào?"', '"Lúc khó nhất, ông bà làm gì?"']):
    s += bubble(132, 34 + i * 40, 178, 30, q, 10.5)
add('Q1', 1, 'Phỏng vấn ông bà', 'Con hỏi ông bà về tuổi thơ, gia đình, và cách vượt qua lúc khó.', s)
s = t(160, 22, 'Cùng một lời với ông bà', 14) + person(70, 160, 0.8, BLUE) + person(120, 160, 0.8, PINK) + person(230, 164, 0.8, PURP) + person(278, 164, 0.8, LGREEN)
s += box(80, 34, 160, 34, '3 điều cả nhà giống nhau', YELLOW, 11) + t(160, 192, 'Hỏi ý ông bà trước, cảm ơn công trông cháu', 10.5, GREEN)
add('Q1', 2, 'Thống nhất với ông bà', 'Bố mẹ và ông bà thống nhất vài điều quan trọng khi chăm cháu. Hỏi ý và cảm ơn ông bà.', s)
s = t(160, 22, 'Danh sách người có thể nhờ', 14) + paper(30, 32, 260, 158)
for i, (need, who) in enumerate([('Đón con khi kẹt', 'Cô Hoa (hàng xóm)'), ('Trông con 1 buổi', 'Bà nội'), ('Sửa điện', 'Chú Nam'), ('Hỏi chuyện học', 'Cô giáo chủ nhiệm')]):
    y = 62 + i * 32
    s += t(46, y, need, 11, NAVY, '700', 'start') + t(274, y, who, 10.5, GREEN, '600', 'end')
s += t(160, 184, 'Tên trong hình là ví dụ', 9.5, GRAY, '500')
add('Q2', 1, 'Mạng lưới giúp nhau', 'Mỗi việc cần giúp có ít nhất một người có thể nhờ. Mình cũng là người giúp được cho họ.', s)
add('Q2', 2, 'Cho và nhận', 'Quan hệ bền nhờ cho và nhận qua lại: hỏi thăm, giúp việc nhỏ, cảm ơn, rồi được giúp khi cần.',
    t(160, 22, 'Cho và nhận', 14) + cycle([['Hỏi', 'thăm'], ['Giúp', 'việc nhỏ'], ['Cảm ơn', 'khi nhận'], ['Nhờ', 'khi cần']], 160, 118, 64, 88, 34, 10.5, [YELLOW, G, PINK, LBLUE]))
add('Q3', 1, 'Kế hoạch màn hình gia đình', 'Chỗ và giờ không màn hình, chọn nội dung tốt, tắt tự phát và thông báo, bố mẹ làm gương.',
    grid4('Kế hoạch màn hình gia đình', [(['Chỗ, giờ', 'không màn hình'], LBLUE), (['Chọn nội', 'dung tốt'], YELLOW), (['Tắt tự phát,', 'thông báo'], G), (['Bố mẹ', 'làm gương'], PINK)], 'Xem lại mỗi đầu năm học'))
s = t(160, 22, 'Màn hình theo tuổi', 14)
for i, (age, txt, c) in enumerate([('Dưới 2 tuổi', ['Không màn hình', '(gọi video', 'với người thân)'], LBLUE), ('2–4 tuổi', ['Tối đa 1 giờ', 'mỗi ngày,', 'ít hơn càng tốt'], YELLOW), ('Từ 5 tuổi', ['Theo kế hoạch', 'gia đình, ngủ', 'và vận động trước'], G)]):
    x = 14 + i * 102
    s += box(x, 44, 94, 110, [age, ''] + txt, c, 10)
s += t(160, 180, 'Theo WHO 2019 và AAP', 9.5, GRAY, '500')
add('Q3', 2, 'Màn hình theo tuổi', 'Khuyến nghị WHO cho trẻ dưới 5 tuổi; từ 5 tuổi theo kế hoạch gia đình.', s)
s = t(160, 22, 'Việc tốt cho cộng đồng', 14)
for i, (lab, c) in enumerate([('Nhặt rác ở xóm', G), ('Tặng sách cũ', YELLOW), ('Thăm người già neo đơn', PINK), ('Góp quỹ lớp, quỹ xóm', LBLUE)]):
    x = 14 + (i % 2) * 150; y = 40 + (i // 2) * 66
    s += box(x, y, 142, 56, lab, c, 11)
s += t(160, 186, 'Con chọn việc, bố mẹ làm cùng', 11.5, GREEN)
add('Q4', 1, 'Việc tốt cho cộng đồng', 'Vài việc tốt nhỏ cả nhà làm cùng nhau. Con chọn việc.', s)
add('Q4', 2, 'Vòng giúp đỡ', 'Thấy một nhu cầu, chọn việc nhỏ, làm cùng nhau, rồi kể lại điều mình học được.',
    t(160, 28, 'Một việc tốt', 14) + flow([['Thấy', 'nhu cầu'], ['Chọn', 'việc nhỏ'], ['Làm', 'cùng nhau'], ['Kể lại,', 'cảm ơn']], 54, 70, 8, 312, 10, 11, [SAND, YELLOW, G, PINK])
    + t(160, 150, 'Không cần tiền, chỉ cần đều đặn', 11.5, GREEN))

if __name__ == '__main__':
    print(sum(len(v) for k, v in FIGS.items() if k[0] in 'NQ' or k in ('KHOAN', 'KHOAQ')), 'hình G8+G9')
