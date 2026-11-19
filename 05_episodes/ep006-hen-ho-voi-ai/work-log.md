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

## 2026-11-19 — Đổi sang váy đen, bỏ áo linen, frame sh010 v2 (Bee)
- Richard: áo linen không hợp bối cảnh nhà hàng tối; hỏi còn màu váy cũ nào chưa lên video. Kiểm kê: kem ep001/ep002, trắng ep003, hồng ep004, xanh dương ep005 đều đã lên video; chỉ còn Đen chưa có clip nào (từng định cho ep001, chỉ có frame tĩnh).
- Đổi ep006: váy hai dây maxi suông SANJOLI màu đen, không áo khoác ngoài — Richard chốt. Bỏ áo linen khỏi script/wardrobe/cả 4 image prompt; aff-0002 giữ trong `affiliate-links.csv` cho tập sau, không còn placement trong ep006.
- Frame sh010 v1 tím (commit `4dcc74d`) đổi tên thành `sh010-first-frame-v1-linen.jpg`, giữ lại làm lịch sử. Frame v2 váy đen làm MỚI 1 lần từ master v002 gốc (không sửa nối từ frame v1), pipeline ảnh Bee, 0 Flow credit: `sh010-first-frame.jpg` (1152×2048, sha256 `cc02928254f59aa10e4d99ce30eac52e99ba39bfdb5fbd28f97d95f1e4a039f5`). Chờ Richard duyệt frame v2 trước khi gen clip.

## 2026-11-19 — Frame sh010 v3: váy lụa đen cổ đổ đúng mẫu (Bee)
- Richard: váy đen v2 chưa giống váy mẫu. Soi ảnh mẫu: váy lụa 2 dây maxi suông, cổ đổ, dây mảnh, suông dài 111cm, vải lụa bóng; v2 cổ tròn, vải mờ như camisole, khung cắt ngang eo nên không thấy độ dài maxi.
- Sửa prompt cả 4 shot + script + wardrobe: "váy lụa ... màu đen, cổ đổ, dây mảnh, dáng suông dài, vải lụa bóng"; ghi nguồn mẫu kem vào wardrobe.md.
- Frame v2 đổi tên thành `sh010-first-frame-v2-black.jpg`, giữ lại. Frame v3 làm MỚI 1 lần từ master v002 gốc + ảnh mẫu kem ngồi làm tham chiếu váy (cùng mẫu đổi sang đen), pipeline ảnh Bee, 0 Flow credit: `sh010-first-frame.jpg` (1152×2048, sha256 `ce0387b144b35b8c778558ab3921828dd682b8b7c6c54e92c58eb008aeef32b4`). Cổ đổ + lụa bóng + tà dài thấy rõ tới gần sàn. Chờ Richard duyệt frame v3.
