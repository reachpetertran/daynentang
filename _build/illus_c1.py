# Hình minh họa và sơ đồ khóa C1 "Lớn lên an toàn (10–14)" – tiền tố A / KHOAA
from illus2 import *  # noqa: F401,F403

G = '#cfe6c4'; PURP = '#c9b6e8'; PEACH = '#f6d9a8'
def teen(x, y, s=1, shirt=PURP): return person(x, y, s * 0.88, shirt, True)

# ================= TRANG KHÓA =================
s = t(160, 22, 'Tám tuần', 14)
items = [('1. Cơ thể đang lớn', SAND), ('2. Ranh giới cơ thể', PINK), ('3. An toàn trên mạng', LBLUE), ('4. Nhận ra lừa đảo', YELLOW),
         ('5. Bạn bè, bắt nạt', G), ('6. Nói "không"', PURP), ('7. Đường, nước, điện', PEACH), ('8. Bản đồ an toàn', LGRAY)]
for i, (lab, c) in enumerate(items):
    x = 14 + (i % 2) * 150; y = 34 + (i // 2) * 40
    s += box(x, y, 142, 32, lab, c, 11)
add('KHOAA', 1, 'Tám tuần', 'Mỗi tuần một bài 25 phút: đọc, làm, rồi nói với một người lớn tin cậy.', s)

add('KHOAA', 2, 'Dừng – Nghĩ – Chọn – Kể', 'Một cách làm dùng cho mọi tình huống khó: dừng lại, nghĩ, chọn việc an toàn, rồi kể cho người lớn tin cậy.',
    t(160, 28, 'Khi gặp chuyện lạ hay khó', 14)
    + flow([['Dừng', 'lại'], ['Nghĩ', 'điều gì', 'xảy ra?'], ['Chọn', 'việc an', 'toàn'], ['Kể', 'người lớn', 'tin cậy']],
           56, 76, 8, 312, 10, 10.5, [PINK, YELLOW, G, LBLUE])
    + t(160, 160, 'Kể ra không bao giờ là lỗi của bạn', 11.5, GREEN))

# ================= BÀI 1 =================
s = t(160, 22, 'Mỗi người một lịch lớn', 14)
s += t(40, 50, 'tuổi', 10, GRAY, '600')
for i, a in enumerate(range(8, 15)):
    x = 70 + i * 34
    s += t(x, 50, str(a), 11, NAVY, '700')
s += f'<rect x="60" y="62" width="{34*5+20}" height="26" rx="13" fill="{PINK}" stroke="{NAVY}" stroke-width="2"/>' + t(150, 79, 'bạn gái thường 8–13', 10.5)
s += f'<rect x="94" y="100" width="{34*5+20}" height="26" rx="13" fill="{LBLUE}" stroke="{NAVY}" stroke-width="2"/>' + t(184, 117, 'bạn trai thường 9–14', 10.5)
s += t(160, 152, 'Sớm hơn hay muộn hơn bạn bè', 11.5, NAVY, '600') + t(160, 170, 'thường vẫn là bình thường', 11.5, GREEN)
s += t(160, 190, 'Theo Nemours KidsHealth', 9.5, GRAY, '500')
add('A1', 1, 'Mỗi người một lịch lớn', 'Dậy thì thường bắt đầu từ 8–13 tuổi ở bạn gái và 9–14 tuổi ở bạn trai. Mỗi người một lịch.', s)

add('A1', 2, 'Năm việc chăm cơ thể mỗi ngày', 'Tắm, rửa mặt, đánh răng, thay đồ sạch, ngủ đủ và vận động. Làm đều quan trọng hơn làm nhiều.',
    t(160, 26, 'Năm việc chăm cơ thể mỗi ngày', 14)
    + flow([['Tắm,', 'rửa mặt'], ['Đánh', 'răng', '2 lần'], ['Đồ lót,', 'tất sạch'], ['Vận', 'động'], ['Ngủ', 'đủ giờ']],
           52, 74, 8, 312, 6, 10, [LBLUE, WHITE, SAND, G, PURP])
    + t(160, 154, 'Đánh dấu mỗi ngày trong 7 ngày', 11.5, GREEN) + check(150, 172))

s = t(160, 22, 'Câu hỏi nào cũng được hỏi', 14)
s += paper(20, 40, 110, 120) + t(75, 66, 'Hộp câu hỏi', 11.5, ORANGE, '800')
for i in range(3):
    s += f'<line x1="34" y1="{88+i*22}" x2="116" y2="{88+i*22}" stroke="{LGRAY}" stroke-width="2"/>'
s += arrow(136, 100, 176, 100, ORANGE, 3)
s += person(230, 172, 0.8, GREEN) + bubble(184, 36, 124, 34, '"Hỏi hay đấy!"', 11)
s += t(160, 192, 'Chọn một người lớn tin cậy để hỏi', 11, GREEN)
add('A1', 3, 'Câu hỏi nào cũng được hỏi', 'Viết câu hỏi vào hộp, rồi hỏi một người lớn tin cậy: bố mẹ, người thân, y tế trường, bác sĩ.', s)


# ================= BÀI 2 =================
s = t(160, 22, 'Bàn tay 5 người tin cậy', 14)
for i, (lab, c) in enumerate([(['Ngón 1', 'Bố hoặc', 'mẹ'], PINK), (['Ngón 2', 'Người', 'thân'], YELLOW), (['Ngón 3', 'Thầy', 'cô'], LBLUE), (['Ngón 4', 'Y tế,', 'bác sĩ'], G), (['Ngón 5', 'Người lớn', 'khác'], PURP)]):
    s += box(12 + i * 60, 44 + abs(2 - i) * 12, 56, 78, lab, c, 10)
s += t(160, 168, 'Kể người thứ nhất chưa được?', 11.5, NAVY, '600') + t(160, 186, 'Kể tiếp người thứ hai', 11.5, GREEN)
add('A2', 1, 'Bàn tay 5 người tin cậy', 'Mỗi ngón tay là một người lớn bạn có thể kể. Người này chưa nghe thì kể người tiếp theo.', s)
s = t(160, 22, 'Bí mật vui hay bí mật phải kể?', 14)
s += box(14, 40, 140, 112, ['Bí mật vui', '', 'làm người khác vui', 'sẽ được kể sớm', 'ví dụ: quà bất ngờ'], G, 10.5)
s += box(166, 40, 140, 112, ['Bí mật phải kể', '', 'làm bạn sợ, khó chịu', 'bị bảo "đừng kể"', 'liên quan cơ thể'], PINK, 10.5)
s += t(160, 180, 'Bí mật phải kể: kể ngay cho người lớn tin cậy', 11, GREEN)
add('A2', 2, 'Bí mật vui và bí mật phải kể', 'Bí mật vui làm người khác vui và sẽ được kể. Bí mật làm bạn sợ hay bị bảo đừng kể thì phải kể.', s)
add('A2', 3, 'Khi thấy khó chịu', 'Bạn có quyền nói dừng, rời đi và kể cho người lớn. Kể ra không phải lỗi của bạn.',
    t(160, 28, 'Khi thấy khó chịu', 14)
    + flow([['Nói', '"Dừng', 'lại"'], ['Rời', 'đi'], ['Kể', 'người lớn', 'tin cậy']], 56, 76, 14, 306, 16, 11, [PINK, YELLOW, LBLUE])
    + t(160, 160, 'Kể ra không bao giờ là lỗi của bạn', 11.5, GREEN))

# ================= BÀI 3 =================
s = t(160, 22, 'Giữ kín hay hỏi trước?', 14)
s += box(14, 38, 140, 124, ['Giữ kín', '', 'Địa chỉ nhà', 'Trường, lớp', 'Số điện thoại', 'Mật khẩu', 'Lịch đi lại'], PINK, 10.5)
s += box(166, 38, 140, 124, ['Hỏi người lớn trước', '', 'Ảnh có mặt mình', 'Ảnh đồng phục', 'Vị trí đang ở', 'Kết bạn mới', 'Tải ứng dụng'], YELLOW, 10.5)
s += t(160, 186, 'Đã đăng lên mạng thì rất khó lấy lại', 11, GREEN)
add('A3', 1, 'Giữ kín hay hỏi trước', 'Một số thông tin luôn giữ kín. Một số việc nên hỏi người lớn trước khi làm.', s)
add('A3', 2, 'Dừng – Chặn – Chụp – Kể', 'Gặp điều xấu trên mạng: dừng trả lời, chặn, chụp màn hình làm bằng chứng, kể cho người lớn.',
    t(160, 28, 'Gặp điều xấu trên mạng', 14)
    + flow([['Dừng', 'trả lời'], ['Chặn'], ['Chụp', 'màn hình'], ['Kể', 'người lớn']], 56, 70, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
    + t(160, 154, 'Bạn không bị phạt vì đã kể', 11.5, GREEN))

# ================= BÀI 4 =================
s = t(160, 22, 'Năm dấu hiệu lừa đảo', 14)
for i, (lab, c) in enumerate([(['1. Vội', 'phải làm ngay'], PINK), (['2. Dọa', 'làm bạn sợ'], YELLOW), (['3. Bí mật', 'đừng kể bố mẹ'], LBLUE),
                               (['4. Đòi', 'tiền, ảnh, mã'], G), (['5. Hời', 'quá mức'], PURP)]):
    x = 14 + (i % 3) * 100 if i < 3 else 64 + (i - 3) * 100; y = 40 if i < 3 else 104
    s += box(x, y, 92, 54, lab, c, 10.5)
s += t(160, 186, 'Thấy 1 dấu hiệu: dừng lại và hỏi người lớn', 11, GREEN)
add('A4', 1, 'Năm dấu hiệu lừa đảo', 'Vội, dọa, bắt giữ bí mật, đòi tiền hay ảnh, hứa quá hời. Một dấu hiệu là đủ để dừng lại.', s)
add('A4', 2, 'Dừng – Hỏi – Kể', 'Dù người kia nói họ là ai, hãy dừng lại, hỏi người lớn và kể lại.',
    t(160, 28, 'Quy tắc Dừng – Hỏi – Kể', 14)
    + flow([['Dừng', 'không làm', 'theo ngay'], ['Hỏi', 'người lớn', 'tin cậy'], ['Kể', 'dù đã lỡ', 'làm theo']], 56, 76, 14, 306, 16, 10.5, [PINK, YELLOW, G])
    + t(160, 160, 'Người thật sự giúp bạn không bắt bạn giấu bố mẹ', 10.5, GREEN))

# ================= BÀI 5 =================
s = t(160, 22, 'Bốn vai khi có bắt nạt', 14)
for i, (lab, c) in enumerate([(['Người bị', 'bắt nạt'], LBLUE), (['Người', 'bắt nạt'], LGRAY), (['Người', 'đứng xem'], YELLOW), (['Người', 'giúp'], G)]):
    s += box(14 + i * 75, 50, 67, 64, lab, c, 10.5)
s += arrow(186, 130, 232, 130, ORANGE, 3) + t(160, 156, 'Bạn có thể đổi từ đứng xem', 11, NAVY, '600') + t(160, 174, 'thành người giúp', 11, GREEN)
add('A5', 1, 'Bốn vai', 'Khi có bắt nạt, thường có bốn vai. Người đứng xem có thể trở thành người giúp.', s)
add('A5', 2, 'Ba câu nói', 'Một câu cho người bắt nạt, một câu cho bạn bị bắt nạt, một câu cho người lớn.',
    t(160, 24, 'Ba câu nói của người giúp', 14)
    + box(14, 38, 292, 36, '"Dừng lại, như vậy không vui."', PINK, 11)
    + box(14, 82, 292, 36, '"Mình ở đây. Mình đi cùng bạn nhé."', G, 11)
    + box(14, 126, 292, 36, '"Con thấy bạn bị bắt nạt. Con cần giúp."', LBLUE, 11)
    + t(160, 186, 'Không đánh trả, không chia sẻ, không cười theo', 10.5, GREEN))

# ================= BÀI 6 =================
add('A6', 1, 'Bốn cách nói không', 'Nói không cảm ơn, đưa lý do, đổi chủ đề, hoặc rời đi và gọi mật mã.',
    t(160, 28, 'Bốn cách nói không', 14)
    + flow([['"Không,', 'cảm ơn"'], ['Đưa', 'lý do'], ['Đổi', 'chủ đề'], ['Rời đi,', 'gọi', 'mật mã']], 52, 76, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
    + t(160, 156, 'Bạn thật sẽ tôn trọng lời "không"', 11.5, GREEN))
add('A6', 2, 'Mật mã gọi đón', 'Nhắn câu mật mã đã thống nhất. Người lớn đến đón ngay, nói chuyện sau.',
    t(160, 28, 'Mật mã gọi đón', 14)
    + flow([['Nhắn', 'câu', 'mật mã'], ['Người lớn', 'đến đón', 'ngay'], ['Nói chuyện', 'sau, khi', 'bình tĩnh']], 56, 76, 14, 306, 16, 10.5, [YELLOW, LBLUE, G])
    + t(160, 160, 'Thống nhất trước với bố mẹ', 11.5, GREEN))

# ================= BÀI 7 =================
add('A7', 1, 'Qua đường', 'Dừng ở mép đường, nhìn hai phía, nghe tiếng xe, rồi mới đi thẳng, không chạy.',
    t(160, 28, 'Qua đường an toàn', 14)
    + flow([['Dừng', 'ở mép'], ['Nhìn', 'hai phía'], ['Nghe', 'tiếng xe'], ['Đi', 'thẳng,', 'không chạy']], 56, 70, 8, 312, 10, 10.5, [PINK, YELLOW, LBLUE, G])
    + t(160, 156, 'Không vừa đi vừa xem điện thoại', 11.5, GREEN))
s = t(160, 22, 'Ba quy tắc ở gần nước', 14)
s += box(14, 38, 292, 36, '1. Không bơi một mình, luôn có người lớn', LBLUE, 11)
s += box(14, 82, 292, 36, '2. Không xuống ao, hồ, sông, suối lạ', YELLOW, 11)
s += box(14, 126, 292, 36, '3. Thấy người đuối nước: gọi to, ném vật nổi', PINK, 11)
s += t(160, 186, 'Không tự nhảy xuống cứu', 11, GREEN)
add('A7', 2, 'Ba quy tắc ở gần nước', 'Không bơi một mình, không xuống chỗ nước lạ, thấy người đuối nước thì gọi người lớn và ném vật nổi.', s)

# ================= BÀI 8 =================
s = t(160, 22, 'Gọi tên cảm xúc', 14)
for i, (lab, c) in enumerate([('Vui', YELLOW), ('Buồn', LBLUE), ('Giận', PINK), ('Sợ', PURP), ('Lo', SAND), ('Xấu hổ', G)]):
    s += box(14 + (i % 3) * 100, 40 + (i // 3) * 54, 92, 44, lab, c, 12)
s += t(160, 168, 'Cảm xúc nào cũng bình thường', 11.5, NAVY, '600') + t(160, 186, 'Việc mình làm với nó mới quan trọng', 11, GREEN)
add('A8', 1, 'Gọi tên cảm xúc', 'Gọi đúng tên cảm xúc là bước đầu để hiểu mình và nói với người khác.', s)
s = t(160, 22, 'Khi nào cần nhờ giúp?', 14)
s += box(14, 40, 140, 110, ['Vài ngày', '', 'buồn, giận rồi qua', '', 'tự bình tĩnh,', 'nói với bạn'], G, 10.5)
s += box(166, 40, 140, 110, ['Nhiều tuần', 'hoặc nguy hiểm', '', 'mất ngủ, bỏ ăn,', 'muốn làm đau', 'bản thân'], PINK, 10.5)
s += t(160, 178, 'Nói ngay với người lớn tin cậy', 11.5, GREEN)
add('A8', 2, 'Khi nào cần nhờ giúp', 'Buồn vài ngày là bình thường. Kéo dài nhiều tuần hay có ý làm đau bản thân thì nói ngay với người lớn.', s)
