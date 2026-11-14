# Chuyện Nhà Thảo My

Workspace sitcom AI và thử nghiệm affiliate, nhân vật chính Thảo My. Quy trình sản xuất chính ở [AGENTS.md](AGENTS.md): sửa ảnh cảnh từ tạo hình gốc → duyệt frame → Flow Frames trực tiếp → lồng VieNeu → dựng và QC. Muse thao tác UI chính chủ; chưa có runner tự động.

Thư mục gốc đánh số theo thứ tự: `00_docs` → `01_brand` → `02_characters` → `03_locations` → `04_products` → `05_episodes` → `06_automation` → `07_analytics`. Phân tích kết quả nằm cuối luồng sản xuất.

- [Thư viện nhân vật](02_characters/thao-my/README.md): ảnh nguồn, ảnh đơn, váy và giọng đang chờ chốt.
- [Từng tập](05_episodes/README.md): kịch bản, một hồ sơ `episode.yaml`, prompt ảnh/video, frame, clip nguồn, manifest và delivery.
- Tạo kịch bản/hồ sơ tập bằng [skill thao-my-episode](/Users/richard/.codex/skills/thao-my-episode/SKILL.md).
- [Validator offline](06_automation/README.md): kiểm tra cấu trúc và cổng generation/edit.
- [Tài liệu](00_docs/README.md): nghiên cứu gốc và lộ trình đề xuất; `01_brand/` giữ nhận diện, `04_products/` giữ tư liệu sản phẩm.

Tạo tập mới bằng `$thao-my-episode`, điền hồ sơ rồi kiểm tra theo hướng dẫn validator. Không copy đè tập đã có.

Facebook: https://www.facebook.com/chuyennhathaomy · TikTok: https://www.tiktok.com/@chuyennhathaomy

Video công bố AI đã có: https://www.facebook.com/share/r/18EVd1BLCM/ . Không tự đăng bài.
