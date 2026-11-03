# Bộ sinh trang

Các trang HTML được sinh từ những tệp Python này. Sửa nội dung trong .py rồi chạy lại (đúng thứ tự):

    cd _build && for f in pages.py course.py lessons.py lessons_w2_4.py lessons_w5_8.py lessons_w9_12.py g1.py g6.py g7.py g2.py g4.py g5.py g8g9.py c1.py c2.py c3.py c4.py c5.py c6.py c7.py community.py en.py extras.py; do python3 $f; done

`en.py` sinh bản tiếng Anh (/en/…) và hình tiếng Anh (assets/minh-hoa/en/). Chạy trước `extras.py` để sitemap có trang /en/.
Thêm trang tiếng Anh mới: viết trang trong `en.py`, rồi thêm cặp đường dẫn vào `EN_PAGES` trong `common.py` (để có hreflang và nút English).

ROOT trong common.py trỏ tới thư mục gốc của kho; đổi nếu chạy ở máy khác.
