# Theo dõi kết quả

Chỉ ghi số liệu quan sát thật, không điền số minh họa thành kết quả. Mỗi tập có thể lưu file `epNNN.md`, tách Facebook/TikTok và ngày giờ đo theo Việt Nam.

Ghi link bài, ngày đăng, revision/master đã đăng, thời lượng, số liệu 24h/72h nếu có: views, thời lượng xem trung bình, tỷ lệ xem hết, share, comment, follow. Ghi thời gian/chi phí sản xuất. Nếu có affiliate, tách click, đơn tạo, đơn hoàn tất và hoa hồng thực nhận; chỉ ghi khi có báo cáo. Không lưu thông tin đăng nhập hay dữ liệu thanh toán.

## Sổ đăng và Schedule Muse Spark

- [publications.csv](publications.csv): một dòng cho mỗi bài/nền tảng; `unknown` là chưa xác minh. Đăng lại tạo dòng riêng. Video công bố AI đã được ghi theo xác nhận người dùng; chưa suy ra ngày đăng hoặc bản TikTok.
- [Hướng dẫn Schedule hằng tuần](weekly-review-instructions.md): bắt buộc lưu snapshot, báo cáo, nhật ký lần chạy và cập nhật ngược repository; không chỉ báo trong chat.
- `weekly/`: báo cáo theo ngày; `snapshots/`: số liệu quan sát giữ lịch sử; `review-runs.csv`: dấu vết các lần Schedule thực chạy (chỉ tạo dòng khi có lần chạy thật).
- [Tracker phân công Muse](../00_docs/production-tracker.csv): tài khoản nào làm tập nào và tiến độ; tách khỏi trạng thái đăng.
