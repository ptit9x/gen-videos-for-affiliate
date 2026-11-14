# Validator hồ sơ tập — schema v2

Công cụ offline, không lái Flow, không gửi job, không tự xác nhận QC media. Quy trình UI đã thành công được ghi trong [AGENTS.md](../AGENTS.md); chưa triển khai runner tự động.

Hồ sơ duy nhất là `episode.yaml`, theo [schema](schemas/episode.schema.json). Các đường dẫn tính từ thư mục tập, không tuyệt đối, không `..`, không symlink thoát khỏi tập. Tài sản có cấu trúc `{path, sha256}`; null nghĩa là chưa có. Hash tính bằng `shasum -a 256 <file>`.

```sh
uv run --with jsonschema --with pyyaml python 06_automation/validate_episode.py 05_episodes/ep001-don-ban
uv run --with jsonschema --with pyyaml python 06_automation/validate_episode.py 05_episodes/ep001-don-ban --stage generation
uv run --with jsonschema --with pyyaml python 06_automation/validate_episode.py 05_episodes/ep001-don-ban --stage edit
uv run --with jsonschema --with pyyaml python -m unittest discover -s 06_automation/tests
```

- Mặc định: schema, đường dẫn/file/hash, prompt UTF-8 không placeholder, shot/take duy nhất, manifest khớp ID/revision/thứ tự và tham chiếu take. In ghi chú frame/clip/giọng thiếu; không kết luận sẵn sàng sản xuất.
- `generation`: mọi shot được duyệt, prompt ảnh/video tách riêng, nguồn sửa ảnh và frame cảnh local đã duyệt; project có khai báo. Frames trực tiếp, Agent off, Veo 3.1 Lite, 8s, 9:16, một output, không frame cuối. Video chỉ dùng `first_frame`; `image_sources` dành cho sửa ảnh. Schema không chấp nhận trường payload ảnh kiểu cũ.
- `edit`: mỗi shot có đúng một take được chọn, có file local; kế hoạch tắt tiếng Veo, VieNeu-TTS và preset đã chốt. Theo dõi QC khớp môi; cổng offline không tự chấm khớp môi.

Exit 0 khi phạm vi kiểm tra được yêu cầu hợp lệ; exit 1 khi lỗi. ep001 phải qua kiểm tra cấu trúc, nhưng generation bị chặn do thiếu frame/duyệt gen mới, edit bị chặn do giọng chưa chốt. Bộ fixture draft tại `tests/fixtures/draft-episode/` chỉ dùng kiểm tra validator, không phải nơi khởi tạo tập sản xuất.

Schema v1 và JSON shot cũ đã được thay bằng YAML v2, không đọc fallback. Chuyển schema không làm tăng revision nội dung. Giá/quota/model trên UI phải kiểm tra trước lần gen tiếp theo; validator không xác minh tài khoản, quyền ảnh hoặc lựa chọn thật trên Flow.
