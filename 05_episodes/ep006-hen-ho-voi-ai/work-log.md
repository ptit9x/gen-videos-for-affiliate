# ep006-hen-ho-voi-ai — work log

## 2026-11-19 — Sửa 3 lỗi review + frame sh010 (Bee)
- Pull remote mới nhất: HEAD `5d66365`, không có commit mới sau 14:44. Bản review là bản viết lại `bd77109`.
- Sửa lỗi 1 — thiếu motion prompt: tạo mới `sh010-motion.txt`, `sh030-motion.txt`, `sh040-motion.txt` (hành động + thoại nguyên văn + giọng nữ miền Bắc + camera tĩnh + không nhạc).
- Sửa lỗi 2 — cụm gây phụ đề giả: bỏ "không phụ đề, không chữ trên hình" khỏi `sh020-motion.txt` và khỏi `script.md` (giữ "không nhạc, camera tĩnh"). Lý do: đã chứng minh cụm nêu tên phụ đề khiến Veo vẽ phụ đề giả nhiều hơn (14/11, 16/11).
- Sửa lỗi 3 — "son đỏ" thoại nhắc mà frame không ghi: thêm "son đỏ" vào `sh010-image.txt`.
- Màu áo linen: Tím nhạt — tạm chốt theo ảnh mẫu để làm frame sh010, chưa chốt chính thức; đã ghi rõ "tạm chốt" trong `script.md` + `wardrobe.md`, và thêm "màu tím nhạt" vào cả 4 image prompt để khớp màu xuyên shot.
- Giọng (Richard 14:55): giữ tiếng Veo gốc nếu giọng Bắc; chỉ lồng clone ThaoMy khi giọng Veo không phải Bắc hoặc Richard chỉ định. Đã sửa mục Hậu kỳ trong `script.md` theo đúng quy tắc này.
- Frame sh010: `input/frames/sh010-first-frame.jpg` (1152×2048, sha256 `d48b7b8d2187b3995984268dfdf84722c8eb0ee37b7e18b0b2c223cd39055899`), gen bằng pipeline ảnh của Bee từ master v002 (`thao-my-body-front-v003-face-v002-review.png`, 1 lần sửa trực tiếp từ master gốc, 0 Flow credit) — KHÔNG phải Flow Nano Banana. Chờ Richard duyệt frame trước khi gen clip.
- Chưa làm: frame sh020/sh030/sh040, episode.yaml, manifest, gen clip.
