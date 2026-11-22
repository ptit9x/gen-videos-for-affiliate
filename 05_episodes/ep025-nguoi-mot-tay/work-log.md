# Work log — ep025 Người Một Tay

## 2026-11-22 15:24 — Richard gửi link reel Jason Chen Music, nhờ tải kịch bản

- Link: https://www.facebook.com/share/r/1A9w48ULfp/?mibextid=wwXIfr (reel id 4522897961284657).
- Trình duyệt mở được reel: Jason Chen Music (verified), caption "UNO Reverse: explain yourself", 1,8 triệu like / 28,9 nghìn comment / 48 nghìn share. Trình duyệt nghe chép 2 lượt + đối chiếu phụ đề cháy và caption tự động — **reel gốc toàn thoại tiếng Anh, không có thoại Việt**.
- Facebook không có nút tải, trình duyệt không tải được qua menu. Bee kéo trực tiếp URL `og:video` bằng curl: file 360×640, 74,79s, 2.363.050 byte, sha256 `86a3a57e80d8fa93a1d52db6c1102b42ce631a239348a7a0f3ceb6c7a2f3d051`, verify bằng ffprobe. Metadata `og:video` ghi 1080×1920 nhưng file về thực tế là 360×640 (bản SD).
- File gốc lưu tại `input/references/source-reel-jason-chen-uno-reverse.mp4`. Transcript gốc lưu dạng tóm tắt tại `input/references/source-transcript.md` (không chép nguyên văn toàn bộ thoại tiếng Anh).

## 2026-11-22 15:31 — Viết draft ep025, 6 shot × 8s = 48s

- Viết `script.md` draft: phỏng theo reel gốc, viết lại hoàn toàn giọng Bắc, 6 shot. Beat dọa dọn đồ của gốc đã cắt để giữ 48s (phương án thêm lại → 7 shot / 56s đã ghi trong script).
- `episode.yaml` draft: 6 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả.
- Số tập: ep001–024 đều đã có tên nên tập mới là ep025 — slot trống tiếp theo.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip.

## 2026-11-22 15:34 — Richard sửa sh020: "shot2 phải là Anh tháo nhanh thế chứ"

- Bản draft đầu Bee viết nhầm vai: để Thảo (lúc đó là Nam) hỏi ngược My "Em tháo nhanh thế?". Richard sửa: sh020 PHẢI là My nói "Anh tháo nhanh thế chứ?" — người tháo vòng là Thảo, My mới là người cà khịa.
- Draft sửa toàn bộ theo: sh010 Thảo tháo vòng cho My (nhanh, hai tay); sh020 My cà khịa; sh030 Thảo lật ngược; sh040 My chối; sh050 Thảo gặng.

## 2026-11-22 15:35 — Richard đổi chàng trai: Nam → Thảo ep021

- Draft đầu đề xuất Nam ep008 (như ep023/ep024). Richard chọn "Đổi chàng trai khác" rồi gật "Dùng Thảo ep021".
- Thảo: tóc đen rối, râu nhẹ, sơ mi linen trắng mở cổ theo ảnh tạm ep021 (`thao-front-temp-v001.jpg`, sha `f9c75fe8…5f889`), CHƯA tạo nhân vật Flow. Trang phục ep025 giữ sơ mi linen trắng mở cổ theo ảnh ref, không lấy áo thun xám của reel gốc.
- Lưu ý: ep021 vẫn chưa duyệt kịch bản, nên nếu ep025 đi trước thì Thảo ra mắt khán giả ở ep025, không phải ep021.

## 2026-11-22 15:44 — Richard DUYỆT kịch bản, CHỐT Thảo ep021

- Richard gật widget "Duyệt, dùng Thảo ep021".
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 22/11, chàng trai chốt Thảo ep021; `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo.
- Trang phục My (áo hai dây kem + vòng cổ mảnh) + bối cảnh phòng khách buổi tối lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Lưu hồ sơ vào repo: bước này ban đầu bị chặn kiểm tra an toàn (repo có thể chạy code khi xử lý), Bee đã hỏi lại; **16:17 Richard gật "Lưu vào repo luôn"** → lưu scope ep025, chạy validator, commit + push riêng như ep023/ep024.
- Bước tiếp theo: làm 6 frame (project Flow riêng `CNTM · EP025 · Người Một Tay`, 0 credit) — tạo nhân vật Thảo trước, rồi mới làm frame — chờ Richard gật làm frame, hoặc đổi đồ/location trước.
