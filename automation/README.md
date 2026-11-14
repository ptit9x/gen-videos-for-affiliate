# Hợp đồng dữ liệu automation — v1

Đây là lớp chuẩn bị dữ liệu, **chưa có runner Google Flow**. Runner cụ thể sẽ được tích hợp sau; không mặc định giao diện/công cụ nào đã hỗ trợ hợp đồng này.

## Đầu vào

Đưa cho runner đường dẫn một thư mục `episodes/<episode>/`. Chỉ thư mục `input/` là payload cho tạo clip; không đưa tài liệu nghiên cứu, output, tài khoản hoặc giấy tờ xác minh vào payload.

`input/shots.json` theo [schema](schemas/shots.schema.json). Đường dẫn prompt/ảnh tính từ `input/`, dùng `/`, không tuyệt đối, không `..`, không symlink thoát khỏi input. `episode.yaml` mô tả bản dựng, phải khớp ID, revision và thứ tự shot.

- Mỗi shot một prompt text đầy đủ, không placeholder.
- Ảnh tham chiếu là file đơn từ tạo hình đã chọn; không gửi sheet nhiều mặt. Theo thử nghiệm người dùng, Flow nhận tối đa 3 ảnh; schema giới hạn 1–3 ảnh/shot. Đây là giới hạn cấu hình hiện tại, không khẳng định mọi chế độ Flow đều giống nhau.
- `prompt_sha256` là hash byte của prompt, `reference_sha256` ánh xạ từng đường dẫn ảnh sang hash byte của file.
- `approved_for_generation: false` trong mẫu; chỉ đổi thành true khi kịch bản, prompt, ảnh và thông số đã sẵn sàng. Đây là trạng thái dữ liệu, không phải yêu cầu xác nhận lại mỗi lần chạy đã được người dùng cho phép.
- Schema chỉ mô tả yêu cầu thời lượng/model input; runner phải đối chiếu các lựa chọn thực sự có trong Flow, không tự thay thông số nếu không hỗ trợ.

Kiểm tra offline (dùng môi trường riêng do uv quản lý):

```sh
uv run --with jsonschema --with pyyaml python automation/validate_episode.py episodes/ep001-don-ban
```

Nếu đã cài `jsonschema`, `PyYAML`, có thể dùng `python3` trực tiếp. Validator thành công trả 0, lỗi trả 1. Mẫu gốc phải bị từ chối vì còn draft và chưa có ảnh. Validator không chứng minh chất lượng nội dung hoặc quyền sử dụng hình; người biên tập xác nhận các phần đó.

Tính hash cho từng file bằng `shasum -a 256 <path>` sau khi hoàn thiện input. Không có lệnh tự bật cờ duyệt.

## Hợp đồng runner cần thực hiện khi tích hợp

1. Validate, lấy lock nguyên tử ở cấp episode/revision và snapshot input trước khi gửi. Không chạy đồng thời hai runner trên cùng revision; lưu đường dẫn output đúng episode. Snapshot không bị sửa sau khi bắt đầu.
2. Mỗi take có job key `episode_id:r<revision>:shot_id:takeNNN`. Gắn hash input vào job; cùng key khác hash là lỗi, cần revision mới. Job key hỗ trợ chống trùng ở phía runner, không đảm bảo Flow hỗ trợ idempotency.
3. Lưu trạng thái `pending → submitting → submitted → downloaded → needs_review → accepted` hoặc `failed`. Ghi `submitting` xuống đĩa **trước** thao tác gửi tạo video. Lưu remote ID/URL nếu giao diện cung cấp.
4. Timeout/crash sau khi có thể đã gửi: chuyển `needs_reconciliation`; tra kết quả đã có trước khi quyết định gửi lại. Không tự đưa job về pending.
5. Giới hạn lượt theo config. Không tự lặp khi hết quota, hết phiên, CAPTCHA hoặc trạng thái gửi không rõ; ghi lý do và chờ xử lý phù hợp.
6. Tải file vào tên tạm, kiểm tra đọc được bằng ffprobe rồi hoàn tất bằng cơ chế không ghi đè file đã có. `generated/sh010/take001.mp4` là clip nguồn; clip có file chưa đồng nghĩa đã đạt QC.
7. Lưu `runs/<run-id>/state.json`, `events.jsonl` và snapshot input; log không chứa cookie/token. Chỉ chụp màn hình cần cho chẩn đoán.
8. Sau tạo clip chuyển sang review/hậu kỳ. Tạo video không bao gồm quyền đăng Facebook/TikTok.

Mỗi job state tối thiểu: job_key, input_hash, status, submitted_at, remote_reference (nếu có), output_path, error, updated_at. Timestamp ISO 8601 có timezone. Log append-only; state ghi nguyên tử.

`config.example.yaml` là giới hạn đề xuất ban đầu, runner chưa sử dụng cho tới khi triển khai. `migration-map.json` ghi đường dẫn cũ → mới khi tái tổ chức dự án.
