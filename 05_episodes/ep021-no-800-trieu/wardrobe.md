# ep021 — Nợ 800 Triệu — Wardrobe

Trạng thái: My CHỐT 21/11 (áo dài Thanh Nghi hồng đậm, mặc tiếp sau ep008). Chàng trai: mặt + đồ CHƯA chốt, chờ Richard cấp ảnh. Kịch bản rev2 (7 shot) đang chờ Richard duyệt lại.

## Thảo My — CHỐT 21/11

- **Áo dài Thanh Nghi — hồng đậm, quần hồng nhạt.** (Richard nhắn 21/11: mặc áo dài Thanh Nghi tiếp theo — tức mặc tiếp bộ đã chốt cho ep008.)
- Kiểu: áo dài truyền thống, cổ cao, tay dài, tà dài; hoa văn theo mẫu Thanh Nghi trong ảnh ref.
- Tóc: xõa tự nhiên, dài sóng nâu (chuẩn Thảo My). Bản búi nửa đầu đã có sẵn trong bộ hôm qua nếu muốn đổi.
- Son: **son đỏ**. Móng: **móng tự nhiên** (chuẩn ep006/ep007, theo luật QC 19/11) — ghi rõ trong mọi image prompt và kiểm tra lúc QC frame.
- Nốt ruồi cằm trái giữ nguyên.

### Ảnh tham chiếu (chỉ lấy áo + màu, không lấy phần còn lại)

1. Shop collage — `~/workspace/ao-dai-2011/outfit-thanh-nghi.jpg`
   - sha256 `0c5dcefffe4a23693e51f32ad5dc7188c20102fa53d31c5ed8d3328a3345b80c`
   - Chỉ lấy: kiểu áo dài Thanh Nghi, màu hồng đậm, quần hồng nhạt.
   - Không lấy: mặt/tóc/dáng người mẫu shop.
2. Thảo My mặc Thanh Nghi, tóc xõa (bản v3, 9:16) — `~/workspace/ao-dai-2011/media-generation-aodai-thanh-nghi-xoa-916-v3-0-efb70b1b-8c57-4de7-9336-33ae5b489511.jpg`
   - sha256 `3d262ba51cc4e82afc8350dab8a246c0fb345b949405a1667a5fc60912814b17`
   - Đây là ảnh My đã mặc đúng bộ này (đăng bộ 8 ảnh ngày 20/11) — dùng làm ref màu + form khi sửa frame.
3. Bản búi nửa đầu (dự phòng đổi tóc) — `~/workspace/ao-dai-2011/media-generation-aodai-thanh-nghi-bun-nua-dau-v-0-8ebf1be5-bfa1-4a14-8e8d-15f01b112e00.jpg`
   - sha256 `1636912bceacc58b2e270395202df058c2b1ada20f122936ae92f4674633f74c`

## Chàng trai — Nam (TẠM) — ảnh ref đã lưu 21/11, chưa tạo nhân vật Flow

- **Nam, khoảng 25–30 tuổi. TẠM THỜI dùng ảnh Richard gửi 21/11** — `input/references/nam-front-temp-v001.jpg` (1023×1537, sha256 `f9c75fe8ba0144f536bcc35cfd6dc9bfcdeebff8b2b6d8ec0d7901d491c5f889`) để sinh nhân vật trên Google Flow khi làm tới. **Chưa tạo nhân vật Flow — chỉ lưu ảnh lại theo lệnh "lưu lại vậy đã nhé" (21/11).**
- Ảnh ref: tóc đen rối, râu nhẹ, áo sơ mi linen trắng mở cổ, quần be, đứng ở biển. Chỉ lấy mặt/tóc/dáng — KHÔNG lấy nền biển, quần be.
- **LƯU Ý QUAN TRỌNG: mặt này KHÁC mặt Nam của ep008** (`02_characters/nam/approved/nam-front-v001.jpg` — không râu, tóc vuốt phồng, sơ mi trắng cài kín, nhân vật Flow đã tạo xong trong project `CNTM · EP008 · Con Nhỏ Đó`). Vì vậy ảnh mới lưu riêng trong thư mục tập ep021, KHÔNG ghi đè `nam-front-v001.jpg`, KHÔNG đưa vào `02_characters/nam/`. Nếu Richard muốn cùng 1 Nam xuyên 2 tập thì phải chọn 1 mặt duy nhất; còn không thì đây là Nam-bản-tạm chỉ dùng cho ep021.
- Trang phục trong tập: chưa chốt riêng — tạm giữ sơ mi trắng như ảnh ref; chờ Richard chốt.

## Bối cảnh

- Quán cà phê ngoài trời, ban ngày, bàn tròn gỗ, 2 ly nước đá, hoa giấy hồng, đèn thả vàng. Khóa này ghi vào mọi frame prompt.
- Location: `03_locations/` (café hẹn hò, date-cafe v001 đang chờ duyệt) hoặc tạo location mới cho quán sân vườn. Chưa chốt.

## Affiliate

- Áo dài Thanh Nghi của My không thuộc sản phẩm affiliate hiện có; chưa gắn link, chưa đăng. (aff-0001 là váy SANJOLI, không dùng cho tập này.)
