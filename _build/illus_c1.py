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

if __name__ == '__main__':
    print('C1 hình xong')
