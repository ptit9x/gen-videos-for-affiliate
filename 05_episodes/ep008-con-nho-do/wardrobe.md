# ep008 — Con Nhỏ Đó — Wardrobe

Trạng thái: My CHỐT 21/11 (áo dài Vân Linh xanh nhạt — làm lại từ đầu, bỏ Thanh Nghi hồng đậm). Nam: ảnh tham chiếu v002 đã duyệt, đồ CHỐT (sơ mi trắng). Kịch bản rev4 (7 shot).

## Thảo My — CHỐT 21/11

- **Áo dài Vân Linh — xanh nhạt, quần xanh nhạt.** (Richard chốt 21/11 khi làm lại từ đầu, bỏ Thanh Nghi hồng đậm.)
- Kiểu: áo dài truyền thống, cổ cao, tay dài voan, tà dài; thêu hoa trắng theo mẫu Vân Linh trong ảnh ref.
- Tóc: xõa tự nhiên, dài sóng nâu (chuẩn Thảo My). Bản búi nửa đầu đã có sẵn trong bộ hôm qua nếu muốn đổi.
- Son: **son đỏ**. Móng: **móng tự nhiên** (chuẩn ep006/ep007, theo luật QC 19/11) — ghi rõ trong mọi image prompt và kiểm tra lúc QC frame.
- Nốt ruồi cằm trái giữ nguyên.

### Ảnh tham chiếu (chỉ lấy áo + màu, không lấy phần còn lại)

1. Shop collage — `~/workspace/ao-dai-2011/outfit-van-linh.jpg`
   - sha256 `3a46dd8b13e46dce367e2059446dd44e271a1bff22cefa6817735fd92986004b`
   - Chỉ lấy: kiểu áo dài Vân Linh, màu xanh nhạt, quần xanh nhạt.
   - Không lấy: mặt/tóc/dáng người mẫu shop.
2. Thảo My mặc Vân Linh, tóc xõa (bản v3, 9:16) — `05_episodes/ep008-con-nho-do/input/references/aodai-van-linh-xoa-v3.jpg`
   - sha256 `2f71722d20cf96e61242959197f25a99a8928f0143e06d2412f89024c98f3bb8`
   - Gen bằng Google Flow 21/11 từ ảnh Thanh Nghi xõa v3 (Flow asset 9a824890, Richard duyệt) — dùng làm ref màu + form khi sửa frame. Lưu ý: tay trái ảnh này cầm thêm vật vàng trang trí — frame phải để tay trống, không lấy vật đó.

## Nam — mặt đã có, đồ CHỐT 21/11: sơ mi trắng

- Mặt/tóc: `02_characters/nam/approved/nam-front-v002.jpg` (Richard duyệt 21/11, sha256 `340a246d…`, Flow asset 968c836f; gen lại kiểu ThaoMyv002 từ ảnh gốc `nam-front-v001.jpg` Richard gửi 21/11). Tóc đen dày vuốt ngược phồng, lông mày rậm. Nhân vật Nam trên Flow đã tạo xong (project `CNTM · EP008 · Con Nhỏ Đó`).
- **Đồ trong tập — CHỐT 21/11: áo sơ mi trắng dài tay, xắn tay áo, như ảnh ref** (Richard bấm widget chọn + nhắn "mặc áo sơ mi trắng luôn"). Quần: tối màu đơn giản (chưa chỉ định cụ thể — theo ảnh ref, quần không thấy trong khung nửa người).
- Không đeo kính (ảnh ref không có kính). Đồng hồ mặt tròn dây da nâu + vòng tay xích bạc trong ảnh ref: chỉ giữ nếu Richard chốt — mặc định KHÔNG đưa vào frame (tránh rối khung hình + tránh lấy phụ kiện của người mẫu).

## Bối cảnh

- Quán cà phê ngoài trời, ban ngày, bàn tròn phủ khăn trắng, **ghế gỗ tối CAO chuẩn tầm bàn, đệm be**, 2 ly nước cam trên bàn, cây xanh sau lưng. Khóa này ghi vào mọi frame prompt.
- Location: `03_locations/date-cafe/review/date-cafe-v003-day.png` (sha `1a66036e…`, Flow asset 5b80f134; Richard duyệt 21/11) — góc khác cùng quán v002-day, ghế cao hơn. v002-day bỏ (ghế thấp), v001 là ảnh tối, không dùng.

## Affiliate

- **Áo sơ mi trắng Nam — aff-0005 / prd-0005:** link Richard gửi 21/11: https://s.shopee.vn/9zzT7PVjWK — ghi `04_products/affiliate-links.csv`, trạng thái `unverified`, đang xác minh đích (browser.open fetch lỗi 21/11, đang kiểm tra lại bằng trình duyệt live). Chưa gắn vào bài.
- Áo dài Vân Linh của My không thuộc sản phẩm affiliate hiện có; chưa gắn link, chưa đăng. (aff-0001 là váy SANJOLI, không dùng cho tập này.)

## Ghi chú 21/11 — dáng áo dài (sau khi Richard chê ngực My bé quá ở frame v1)
- Áo dài Vân Linh phải **ôm vừa ở ngực, ngực đầy đặn nổi bật đúng tỷ lệ body v003 đã duyệt** — frame v1 áo rủ lỏng nên ngực đọc nhỏ, sai chuẩn nhân vật. Ghi rõ "tailored and fitted at the chest, bust full and prominent" trong mọi image prompt có My (cả shot Nam, vì My vẫn hiện diện đối diện bàn).
