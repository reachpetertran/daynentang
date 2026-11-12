# App Dạy Nền Tảng (Android, Capacitor)

- `build_www.py`: sinh `www/` từ `../public/` (nội dung đóng gói trong app, đọc khi mất mạng).
- `shell/`: khung app (thanh trên, 4 tab, Đã lưu, cỡ chữ, màu nền). Dữ liệu chỉ lưu trên máy.
- `android/`: dự án Android do Capacitor tạo. appId `com.daynentang.app` (không đổi sau khi lên Play Store).
- Build: GitHub Actions `.github/workflows/app-android.yml` tạo APK bản thử (artifact của lần chạy).
- Trong app không có quảng cáo, không tracking, không tài khoản, không nút quyên góp.
