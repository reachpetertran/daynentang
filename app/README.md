# App Dạy Nền Tảng (Android, Capacitor)

- `build_www.py`: sinh `www/` từ `../public/` (nội dung đóng gói trong app, đọc khi mất mạng).
- `shell/`: khung app (thanh trên, 4 tab, Đã lưu, cỡ chữ, màu nền). Dữ liệu chỉ lưu trên máy.
- `android/`: dự án Android do Capacitor tạo. appId `com.daynentang.app` (không đổi sau khi lên Play Store).
- Build: GitHub Actions `.github/workflows/app-android.yml` tạo APK bản thử (artifact của lần chạy).
- Trong app không có quảng cáo, không tracking, không tài khoản, không nút quyên góp.

## Cập nhật 12/11/2026 (lần 2)
- Tên trên cửa hàng: "Dạy Nền Tảng: Truyện, Khóa học". Tên dưới icon: "Dạy Nền Tảng".
- `stories/`: 19 truyện (đoạn HTML + tranh WebP) sinh bằng `tools/gen_stories.py` từ bộ nguồn sách. Truyện C7 trong app đặt ở Bhutan.
- `www/app/index.js` (sinh khi build): danh mục khóa – bài – truyện cho lộ trình và tìm kiếm.
- Tính năng: tiến độ từng khóa, bài tiếp theo, ghi chú riêng, tìm kiếm không dấu, ngày có học trong tuần, chuyển Việt/Anh, cổng cảnh báo phần cam.
