# Giao việc Schedule Muse Spark: review video hằng tuần

Đã được chủ dự án yêu cầu ngày 2026-11-16. Đây là nội dung giao việc; chưa phải Schedule đã được cài đặt. Lịch/giờ và quyền truy cập sẽ cấu hình trên tài khoản Muse Spark chạy Schedule.

## Đầu vào và phạm vi

- Đọc AGENTS.md, 00_docs/production-workflow.md, 00_docs/production-tracker.csv, 07_analytics/publications.csv và báo cáo tuần trước từ phiên bản repository mới nhất.
- Phạm vi hiện tại: người dùng chưa thêm được link Shopee; chỉ lưu link và gợi ý tập tại `04_products/affiliate-suggestions.csv`. Không yêu cầu số liệu chuyển đổi khi chưa gắn link, không coi đề xuất là placement thật.
- Đọc `04_products/affiliate-links.csv` và `04_products/affiliate-placements.csv`; đối soát link/vị trí đã dùng, cập nhật bằng chứng và trạng thái theo `04_products/README.md`. Đo affiliate theo kỳ báo cáo và link_id/tracking_label nếu có; không quy doanh thu cho từng video khi nguồn không phân tách.
- Kiểm tra đúng kênh Facebook https://www.facebook.com/chuyennhathaomy và TikTok https://www.tiktok.com/@chuyennhathaomy. Chỉ ánh xạ bài với tập khi có bằng chứng; bài chưa nhận diện được ghi riêng để đối soát, không đoán tập.
- Ghi mã tài khoản Muse thực hiện, khoảng thời gian đo, thời điểm quan sát theo Asia/Ho_Chi_Minh (ISO 8601 có +07:00), nguồn và giới hạn truy cập. Không lưu secret hoặc thông tin nhận diện không cần thiết của người bình luận.

## Việc phải làm trong mỗi lần chạy

1. Đối soát bài mới và các bài đã biết. Cập nhật publications.csv khi xác minh được đã đăng, bài bị gỡ hoặc không còn truy cập được. Không kết luận đã gỡ chỉ vì thiếu quyền truy cập. Giữ lịch sử và ghi bằng chứng; không thay ngày đăng chưa biết bằng ngày kiểm tra.
2. Thu thập snapshot từng bài có thể truy cập: views/reach, likes, comments, shares, saves, thời lượng xem trung bình, tỷ lệ xem hết, follower tăng và số liệu affiliate nếu có quyền/báo cáo. Chỉ ghi chỉ số thực có; thiếu ghi null/kèm lý do, không điền 0. Phân biệt views/reach và số tích lũy/số trong kỳ; ghi đơn vị, định nghĩa nền tảng và tuổi bài tại thời điểm đo.
3. Phân tích chất lượng nội dung và phản hồi: hook, nhịp hài, độ rõ thoại, giọng/khớp môi, hình ảnh/continuity và phản ứng với sản phẩm. Chỉ nhận xét trực tiếp hình/âm thanh khi thực sự xem/nghe được; tách quan sát, ý kiến khán giả và suy luận. Tóm tắt các chủ đề phản hồi cùng số bình luận thực đã đọc; không coi mẫu nhỏ là ý kiến toàn bộ khán giả.
4. So với snapshot trước và các bài cùng nền tảng/độ tuổi tương đương. Nêu hạn chế mẫu, số liệu thiếu và độ chắc chắn. Lượt đo hằng tuần không được gắn nhãn 24h/72h nếu không đúng mốc. Đưa đề xuất thử nghiệm tuần tới; không tự biến đề xuất thành quyết định đã duyệt.
5. Lưu báo cáo `07_analytics/weekly/YYYY-MM-DD.md`, snapshot thô có cấu trúc tại `07_analytics/snapshots/YYYY-MM-DD/` và cập nhật file phân tích từng tập `07_analytics/epNNN.md`. Giữ snapshot cũ. Cùng ngày chạy lại dùng hậu tố thời gian để không ghi đè dữ liệu trước. Mỗi số liệu có post_url, platform, observed_at, metric, value, unit, scope (lifetime/period và mốc kỳ), source, access_notes.
6. Ghi dấu lần chạy vào `07_analytics/review-runs.csv`: run_id, muse_account_id, started_at, finished_at, status (complete/partial/blocked), report_path, notes. Tạo header này nếu chưa có file. Chỉ complete khi đã xong phạm vi và lưu kết quả; thiếu quyền/số liệu cần nêu rõ partial/blocked. Không đánh dấu tập đã hoàn tất sản xuất chỉ vì đã đo lường.
7. Bắt buộc ghi ngược repository: cập nhật sổ đăng/báo cáo/snapshot và nhật ký lần chạy; xem diff, kiểm tra CSV/đường dẫn, commit và push theo quy tắc nhánh ở production-workflow.md nếu có remote và quyền. Đọc bản mới trước khi sửa, giữ cập nhật của tài khoản khác. Nếu push thất bại, báo chưa đồng bộ remote và cung cấp bản local/patch; không tuyên bố đã cập nhật repository từ xa.
8. Trả báo cáo ngắn: bài đã kiểm tra, phát hiện chính, dữ liệu thiếu, đề xuất, đường dẫn báo cáo và commit/nhánh đã push thực tế. Không tự đăng/sửa/xóa bài, trả lời bình luận hoặc thay đổi kịch bản/trạng thái duyệt.

## Mẫu báo cáo tuần

- Kỳ đo, tài khoản thực hiện, thời điểm quan sát, phạm vi truy cập.
- Bài mới và trạng thái đăng đã đối soát, liên kết bằng chứng.
- Bảng số liệu từng bài/nền tảng, tuổi bài, nguồn; thay đổi so với snapshot trước nếu có.
- Quan sát chất lượng video; chủ đề bình luận và cỡ mẫu đã đọc.
- Nhận định và giới hạn; đề xuất thử nghiệm cần chủ dự án chốt.
- Các file cập nhật, commit/nhánh và tình trạng đồng bộ; việc còn thiếu.
