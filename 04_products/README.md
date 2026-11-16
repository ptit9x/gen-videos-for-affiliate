# Sản phẩm và link affiliate

## Phạm vi hiện tại — chốt 2026-11-16

Người dùng hiện chưa thêm được link Shopee. Trước mắt chỉ lưu link affiliate được cung cấp và gợi ý tập phù hợp để dùng sau; không yêu cầu gắn link hoặc đo chuyển đổi ở giai đoạn này. Chưa suy ra nguyên nhân hoặc điều kiện mở quyền.

- Lưu URL thật vào `affiliate-links.csv` khi người dùng cung cấp.
- Ghi đề xuất vào `affiliate-suggestions.csv`: mã gợi ý, link_id, tập phù hợp, lý do, ngữ cảnh lồng sản phẩm, trạng thái và ngày cập nhật. Một link có thể được đề xuất cho nhiều tập, mỗi tập một dòng. `link_id` phải có trong sổ link; chưa biết tập cụ thể thì để episode trống và mô tả hướng nội dung trong suggested_context.
- Trạng thái gợi ý: `proposed`, `accepted`, `rejected`, `deferred`. Chỉ accepted khi người dùng duyệt rõ. Gợi ý không tự sửa kịch bản, duyệt sản phẩm hoặc cho phép gen media.
- Khi nhận link, Muse lưu nguồn rồi đọc kịch bản để đề xuất tập có ngữ cảnh tự nhiên, nêu lý do; nếu chưa có tập phù hợp thì ghi rõ, không ép sản phẩm vào tập. Không coi ảnh người mẫu là nhận diện nhân vật.
- `affiliate-placements.csv` giữ cho giai đoạn thực sự gắn link; hiện không cần tạo placement chỉ vì đã lưu link hoặc đề xuất tập. Schedule chỉ đối soát kho link/gợi ý, không yêu cầu click/đơn/hoa hồng khi chưa triển khai.

## Sổ link dùng chung

- `affiliate-links.csv`: một dòng cho mỗi link affiliate thực tế. Lưu `link_id` ổn định, mã/tên sản phẩm, nền tảng (ví dụ shopee), shop, URL sản phẩm gốc, URL affiliate nguyên vẹn, nhãn tracking nếu có, trạng thái, nguồn và ngày kiểm tra.
- `affiliate-placements.csv`: ánh xạ link với tập/bài đăng và vị trí thực dùng (caption, bình luận ghim, bio…). Một link có thể dùng ở nhiều bài; mỗi vị trí dùng có dòng riêng. `post_url` trỏ đến bài cụ thể, `link_id` phải tồn tại trong sổ link.
- Chưa có link người dùng cung cấp: hai sổ chỉ có header, không có link minh họa hoặc link tự tạo.

## Quy tắc cập nhật cho Muse Spark

1. Lưu đúng URL affiliate được cung cấp hoặc tạo qua công cụ chính chủ đã được người dùng cho phép; không tự chế mã tracking hay sửa query của URL. Lưu cả URL sản phẩm gốc nếu xác minh được; thiếu để trống và ghi chú.
2. Dùng mã như `aff-0001`, `prd-0001`, `place-0001`; kiểm tra trùng trên bản mới nhất trước khi cấp mã. Không lưu mật khẩu, cookie, token API hoặc dữ liệu thanh toán; URL affiliate công khai được lưu đầy đủ để bảo toàn tracking.
3. Trạng thái link: `unverified`, `active`, `inactive`, `replaced`. Chỉ `active` sau khi kiểm tra dẫn đúng sản phẩm; kiểm tra đích không chứng minh có hoa hồng hoặc còn quyền affiliate. Đổi link tạo dòng/link_id mới và giữ lịch sử dòng cũ, không ghi đè link đã dùng.
4. Trạng thái placement: `planned`, `confirmed`, `removed`, `unknown`. Chỉ `confirmed` khi có bằng chứng link đã được đặt ở bài/vị trí đó. Có video đã đăng không có nghĩa đã gắn link. Chưa có bài thì để post_url trống và dùng planned.
5. Mỗi sản phẩm có thể có thư mục `<product_id>/` chứa nguồn, tư liệu xác thực và README. Chỉ ghi giá/hoa hồng/ưu đãi khi có nguồn và thời điểm kiểm tra; không coi là thông số cố định.
6. Cập nhật repository theo quy tắc phối hợp trong production-workflow.md. Việc lưu link không phải ủy quyền đăng, gắn link, mua hàng hoặc bật affiliate.

## Đo lường

Schedule hằng tuần đọc hai sổ, đối soát link/vị trí trong phạm vi truy cập. Chỉ cập nhật trạng thái khi có bằng chứng; không mở được do thiếu quyền thì ghi hạn chế, không kết luận link hỏng.

Snapshot affiliate cần kỳ báo cáo, thời điểm lấy, nguồn, link_id/tracking_label nếu nền tảng có phân tách: click, đơn tạo, đơn hoàn tất, đơn hủy/hoàn và hoa hồng thực nhận. Không gán doanh thu cho từng video khi báo cáo chỉ có tổng toàn tài khoản hoặc nhiều video dùng cùng link không có tracking riêng. Thiếu dữ liệu ghi thiếu, không điền 0. Lưu dữ liệu đo tại `07_analytics/` theo hướng dẫn Schedule.
