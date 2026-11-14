# Chuyện Nhà Thảo My

Workspace sản xuất sitcom AI và thử nghiệm affiliate. Nhân vật chính: Thảo My; chưa xây nhân vật khác. Video giới thiệu AI đã có: https://www.facebook.com/share/r/18EVd1BLCM/

| Thư mục | Nội dung |
|---|---|
| `brand/` | Avatar/banner hiện đang dùng |
| `characters/thao-my/` | Ảnh nguồn, prompt, ảnh duyệt và hồ sơ nhân vật |
| `products/` | Hồ sơ SKU và tư liệu sản phẩm khi chọn được sản phẩm |
| `episodes/` | Mỗi tập một thư mục: kịch bản, input, clip, bản dựng, delivery |
| `templates/episode/` | Mẫu để tạo tập; chưa đủ điều kiện chạy |
| `automation/` | Hợp đồng dữ liệu, schema, validator và cấu hình mẫu; chưa có runner Flow |
| `runs/` | Trạng thái và nhật ký theo từng lần chạy |
| `docs/research/` | Hội thoại nghiên cứu gốc |
| `docs/production-plan.md` | Lộ trình affiliate đề xuất |

Đọc [AGENTS.md](AGENTS.md), [hướng dẫn tập](episodes/README.md) và [hợp đồng automation](automation/README.md).

Tạo tập nháp từ thư mục gốc:

```sh
cp -R templates/episode episodes/ep001-don-ban
```

Điền ID nhất quán trong `episode.yaml` và `input/shots.json`, viết kịch bản, tách prompt đầy đủ và copy ảnh đơn đã duyệt vào `input/references/`. Điền SHA-256, kiểm tra rồi mới bật `approved_for_generation`.

```sh
uv run --with jsonschema --with pyyaml python automation/validate_episode.py episodes/ep001-don-ban
```

Validator chạy offline, không gửi dữ liệu sang Flow. Cấu trúc này chuẩn bị cho tích hợp; chưa xác nhận tương thích với công cụ automation cụ thể.
