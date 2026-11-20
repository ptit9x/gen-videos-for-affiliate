# ep019 — Khám Bệnh — Wardrobe: Thảo My

Trạng thái: ref đã nhận 20/11/2026 từ Richard, chưa làm lại frame. Frame sh010/sh030 hiện tại vẫn là áo len hồng đậm, dệt kim — KHÔNG khớp ref mới, xem mục "Khác với frame hiện tại" bên dưới.

## Áo Thảo My — chốt theo ref Richard gửi 20/11

- Sản phẩm: áo thun chiết eo có mút rời, KVK KIVIKA FITWEAR.
- Màu dùng trong tập: **Hồng Pastel** (chỉ màu này; listing có 4 màu: Đen, Trắng, Xám than, Hồng pastel).
- Kiểu: ngắn tay, cổ tròn, tay raglan, vải trơn mịn (không dệt kim), co giãn 4 chiều, thoáng mát, có mút rời bên trong.
- Độ ôm: **bó sát, chiết eo, tôn dáng — phải nhìn rõ là đang chật**. Đây là điểm mấu chốt của cú chốt sh040 ("mặc chật thế thở làm sao được"), nên độ bó sát không được làm nhẹ đi.
- Quần: quần dài tối màu đơn giản như kịch bản cũ. Ảnh mẫu mặc quần legging xám — KHÔNG dùng legging trong cảnh phòng khám, chỉ giữ quần tối màu.
- Son/tóc: giữ như frame đã duyệt — son hồng nhạt, tóc nâu dài buông tự nhiên, nốt ruồi cằm trái.

## Ảnh tham chiếu (chỉ lấy áo + độ ôm, không lấy phần còn lại)

1. Flat lay — `input/references/thao-my-pink-pastel-fitted-tee-reference.jpg`
   - sha256 `5e9012df90cd106c7572f97c3a3aedabf6292e6980aff1ff4e43ca0ae18d8f11`, 1024×1024.
   - Chỉ lấy: áo hồng pastel, cổ tròn, tay ngắn raglan, form bó sát.
   - Không lấy: chữ "Màu Hồng Pastel" / "Kèm mút", mút rời đặt bên cạnh, thảm yoga, tạ tay, bình nước.
2. Mẫu mặc — `input/references/thao-my-pink-pastel-fitted-tee-worn-reference.jpg`
   - sha256 `d415d5df4b965260a58a7974e5f6dd8693353561db1a2356c1031181c70127f8`, 1024×1024.
   - Chỉ lấy: độ bó sát + chiết eo khi mặc, màu hồng pastel.
   - Không lấy: chữ/logo KVK KIVIKA FITWEAR, các ô mô tả (Tôn dáng / Co giãn 4 chiều / Thoáng mát / Mút rời), ảnh nhỏ 3 màu còn lại, quần legging xám, mặt/tóc/dáng người mẫu (mặt Thảo My vẫn theo master v002, không lấy mặt mẫu).
- Bản gốc 2 ảnh lưu tại `02_characters/thao-my/wardrobe/inbox/ep019-pink-pastel-fitted-tee/` (cùng sha256).

## Khác với frame hiện tại — cần quyết trước khi gen clip

- Frame sh010/sh030 ngày 19/11: áo hồng ĐẬM hơn, vải dệt kim có vân, cổ tròn — nhìn vẫn ôm nhưng không phải áo pastel trơn trong ref mới.
- Nếu đổi sang ref mới thì phải làm lại frame sh010 + sh030 từ master v002 (Nano Banana, 0 credit video), cập nhật image prompt ("pink textured knit top" → "smooth pastel pink fitted tee, waist-cinched, visibly snug") + `image_sources` trong `episode.yaml`, rồi mới gen clip.
- Bác sĩ (sh020/sh040) không đổi.

## Affiliate

- Link Richard gửi 20/11: https://s.shopee.vn/8fU4QqQvWj — ghi aff-0004 / prd-0004, đang chờ xác minh đích (trình duyệt đang mở link để đối chiếu với 2 ảnh ref).
- Chưa gắn vào bài, chưa đăng.
