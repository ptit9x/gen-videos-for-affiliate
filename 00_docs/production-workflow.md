# Quy trình vận hành hiện hành

Cập nhật 2026-11-15. Áp dụng cho Chuyện Nhà Thảo My. Bản nghiên cứu 01 được giữ nguyên; hướng dẫn này triển khai cấu trúc phù hợp quy trình ảnh cảnh → Frames hiện hành.

## Cấu trúc

```text
02_characters/<nhan-vat>/     # source, approved, review, wardrobe, hồ sơ và prompt
03_locations/<boi-canh>/      # source, review, approved, README.md, location.json
04_products/                 # hồ sơ SKU và tư liệu xác thực khi có sản phẩm
05_episodes/epNNN-ten-tap/
  script.md
  episode.yaml
  input/references/
  input/frames/
  input/prompts/
  generated/<shot>/
  edit/manifest.yaml
  delivery/
07_analytics/                # kết quả từng tập và từng nền tảng
00_docs/                     # vận hành, kế hoạch và bản nghiên cứu
```

Kịch bản, clip và bản giao ở cùng tập để truy nguồn shot/take. Không chuyển sang các kho scripts/Flow outputs/final videos chung. Không đổi schema hoặc đường dẫn validator chỉ để thêm location. Bản nháp ý tưởng có thể chỉ có script.md; trước sản xuất phải tạo episode.yaml và manifest bằng `$thao-my-episode`.

## Nền sản xuất đã duyệt

Mặt `thao-my-face-front-v001.png`; body chính diện, nghiêng trái và phía sau v003. Danh mục/hash ở `02_characters/thao-my/references.json`. Chỉ dùng bộ mới cho sản xuất mới. Ảnh body áo trắng/quần short be khóa tỷ lệ; trang phục từng tập phải ghi riêng. Trang phục chọn theo từng tập trong `wardrobe.md`; nguồn người dùng gửi qua chat hoặc `02_characters/<nhân-vật>/wardrobe/inbox/`. Không mặc định váy SANJOLI đen cho toàn series; giữ nguyên bộ của ep001–002 đang gen. Bộ location mới còn chờ duyệt; My dùng preset Đoan Trang theo character.yaml, Vy chưa chốt giọng.

## Từ kịch bản tới video

1. Viết kịch bản: mỗi clip khoảng 8 giây, một người nói, câu ngắn và một hành động chính. Ghi thoại, góc máy, hành động, nguồn mặt/body/location và trang phục. Người dùng duyệt hướng/kịch bản.
2. Copy các nguồn đã duyệt thực sự cần vào input/references, giữ tên file; khai báo từng file/hash trong episode.yaml. Asset không dùng chung giữa các project Flow.
3. Sửa ảnh cảnh trong project Flow từ ảnh đơn nhân vật và location đã duyệt. Giữ mặt/tóc, bố cục và đạo cụ nhất quán. Tải frame đã duyệt vào input/frames, hash và ánh xạ shot; không ghi đè frame đã dùng. Mặt lệch thì sửa frame trước.
4. Chỉ khi được yêu cầu gen shot: Frames trực tiếp, Agent tắt, một frame đầu, không frame cuối hay ảnh kèm. Video 9:16, 8 giây, một output. Kiểm tra model/credit/quota thực tế trên UI trước mỗi lượt. Prompt chuyển động ngắn, thoại nguyên văn, máy tĩnh, không nhạc/chữ/phụ đề. Ghi take và ID Flow.
5. Đọc skill sitcom-flow-assembly trước hậu kỳ. Giữ clip nguồn; tắt tiếng Veo, lồng cùng preset VieNeu đã chốt; hard cut, SRT riêng, QC hình/âm thanh/khớp môi. Manifest ghi take, lệnh dựng, thông số và kết quả QC. Chỉ bản đạt QC vào delivery.
6. Đăng chỉ khi có yêu cầu cụ thể. Ghi số liệu thật vào analytics; lịch và mục tiêu vẫn là giả thuyết thử nghiệm.

Validator chỉ kiểm tra offline, không gen hoặc chứng nhận media. Không lưu secret/session. Đổi mặt/frame/prompt sau gen phải tăng revision và giữ lịch sử take; không gọi take cũ là đầu ra của revision mới.

## Tình trạng ep001

Rev3 dùng mặt mới/body v003; chưa gen frame/video mới. ID clip rev2 giữ để truy nguồn, hai đường dẫn clip local cũ không tìm thấy khi kiểm tra 2026-11-15. Cần duyệt kịch bản/frame và chốt giọng trước các bước tương ứng.
