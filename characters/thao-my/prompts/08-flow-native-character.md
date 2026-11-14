# Prompt xây nhân vật Thảo My ngay trong Flow — bản váy maxi đen

Quyết định của Henry, 2026-11-14: nhân vật mặc **váy lụa 2 dây maxi suông màu ĐEN** (theo ảnh sản phẩm SANJOLI gửi kèm) làm trang phục cố định.
Ảnh tham chiếu trang phục (chỉ để con người đọc/mô tả, KHÔNG upload vào Flow làm Ingredients — tránh bộ lọc người thật):
`characters/thao-my/wardrobe/sanjoli-maxi-dress-black-reference.png`

## Nguồn nhận diện nhân vật (đã chốt)

Khuôn mặt, mái tóc, dáng người và thần thái của nhân vật vẫn dựng theo **bộ ảnh Thảo My gốc** — đặc biệt là ảnh toàn thân `thao-my-body-front-v002.png` và các ảnh biểu cảm đã duyệt. Ảnh người mẫu mặc váy chỉ là nguồn tham chiếu cho **chiếc váy**, không dùng mặt, tóc hay dáng của người mẫu trong ảnh sản phẩm.

Đặc điểm khóa theo ảnh Thảo My gốc: tóc dài thẳng màu nâu sáng, mái bằng phủ trán; lông mày đậm rõ nét; mắt nâu; son hồng tự nhiên; trang điểm nhẹ; biểu cảm dịu dàng, tự tin.

Lưu ý kỹ thuật: Flow đã từ chối việc dùng chính ảnh gốc làm Ingredients ở cả hai lượt thử. Vì vậy "dựa vào ảnh gốc" ở đây nghĩa là dùng ảnh gốc để rút đặc tả chi tiết và tái dựng nhân vật ngay trong Flow, sau đó khóa ảnh master do Flow sinh làm tham chiếu cho các shot sau. Không cam kết sao chép trùng khớp 100% khuôn mặt ảnh gốc.

## Đặc tả váy (khóa cứng trong mọi prompt)

Black satin silk slip maxi dress: two thin spaghetti straps, soft V neckline, loose straight flowing silhouette, smooth satin sheen, hem to the ankles. No patterns, no logos, no belt.

## Prompt sinh ảnh master nhân vật (text-to-image trong Flow, tiếng Anh)

Photorealistic full-body portrait of an original fictional Vietnamese woman, age 26, an AI-created character who is not a real person and does not resemble any celebrity. Recreate the established Thao My look from her approved character description: a soft oval face, warm fair skin, long straight light-brown hair with full blunt bangs, defined dark brows, brown eyes, soft natural pink lips, light natural makeup, gentle confident expression. She wears an elegant black satin silk slip maxi dress: two thin spaghetti straps, soft V neckline, loose straight flowing silhouette with a subtle satin sheen, hem to the ankles. Standing in a warm minimalist home interior, soft daylight from the left, plain off-white wall behind her. Natural body proportions, realistic skin texture, vertical composition. No text, no logos, no watermark, no other people.

## Sau khi có master

1. Henry duyệt mặt — mặt master phải tái dựng đúng các đặc điểm của Thảo My trong bộ ảnh gốc (tóc nâu thẳng mái bằng, mày đậm, mắt nâu, son hồng tự nhiên). Bộ ảnh gốc không upload trực tiếp được vì Flow chặn theo chính sách người nổi tiếng/người thật (2 lượt thử 14/11 đều bị từ chối và hoàn credit), nên master do Flow sinh sẽ là bản tái dựng theo đặc tả, không phải bản sao nguyên trạng.
2. Dùng chính ảnh master Flow sinh làm Ingredients cho các shot sau (asset sinh trong Flow), không quay lại ảnh upload bên ngoài.
3. ep001 cần revision 2: thay đặc tả trang phục áo thun trắng + short beige bằng váy maxi đen trong script.md, cả 2 prompt shot, rồi tính lại SHA-256 trong shots.json và chạy lại validator.

## Đã chốt

Tóc: **giữ tóc Thảo My hiện tại — nâu thẳng, mái bằng** (Henry chốt 2026-11-14). Không lấy tóc của người mẫu trong ảnh váy; ảnh đó chỉ dùng cho chiếc váy.
