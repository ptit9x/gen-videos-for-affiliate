# Thảo My — body v003

- Ngày tạo: 2026-11-15, image_gen tích hợp.
- Trạng thái: đủ ba góc được người dùng duyệt ngày 2026-11-15. Chính diện: “Đẹp đó, gen các ảnh còn lại đi”; nghiêng trái và phía sau: “ổn đó”. Đã copy cả ba ảnh vào `../../approved/`, giữ nguyên tên file. Chưa kiểm chứng trong Flow.
- Ảnh mặt: `../../approved/thao-my-face-front-v001.png` (đã duyệt).
- Ảnh tỷ lệ cơ thể: ảnh váy đen người dùng đính kèm trong chat.
- Trang phục theo yêu cầu: áo thun trắng, quần short be như bộ cũ; thấy toàn bộ chân và bàn chân.
- Không suy ra số đo ba vòng chính xác từ ảnh.
- Đầu ra: `thao-my-body-front-v003.png`.

## Prompt

### Hai góc bổ sung — image_gen tích hợp

Ảnh đầu vào: body chính diện v003 và mặt chính diện đã duyệt. Đầu ra riêng từng ảnh: `thao-my-body-profile-screen-left-v003.png`, `thao-my-body-back-v003.png`.

Prompt nền: Use case: identity-preserve. Generate one photorealistic single full-body reference photograph of the EXACT SAME adult woman Thao My. Image 1 is approved body and wardrobe anchor; image 2 is approved facial identity. Preserve exact body volume, bust, waist, hips, leg length, shoulder width, skin tone and adult age from image 1. Same fitted opaque white crew-neck short-sleeve T-shirt tucked into same beige high-waisted ordinary shorts, bare feet. Same dark brown long hair and bangs, exact recognizable face from image 2 where visible. Entire head and both feet visible with margins, same scale, gray studio background, soft even light, level camera at torso height with no perspective distortion. Neutral relaxed upright stance, arms down naturally, no hip tilt, anatomically realistic. No text, collage, labels, or measurements. Change only viewing angle: 

Nghiêng: strict side profile facing SCREEN LEFT, head and torso and feet all in side profile, looking horizontally left, no turn toward camera. Maintain natural body thickness consistent with approved front view.

Sau: strict straight BACK VIEW, back of head, shoulders, torso and heels facing camera, head looking straight away, no face visible and no looking over shoulder. Long hair falls naturally down upper back. Same shorts with understated ordinary back pockets. Feet a little apart, arms relaxed slightly away from body.

### Chính diện

Use case: identity-preserve. Create ONE photorealistic full-body front-view character reference of the SAME adult woman Thao My. Image 1 (approved close-up portrait) is the authoritative facial identity and hair reference: preserve her exact facial geometry, eyes, nose, lips, beauty mark, bangs, dark brown long hair, skin tone, apparent adult age and neutral expression. Image 2 (black dress full-body photo) is the body silhouette, shoulder, neck, arm and overall proportion reference. Change clothing to her previous casual outfit: fitted opaque white crew-neck short-sleeve T-shirt, tucked into ordinary beige high-waisted shorts ending at upper-mid thigh, bare feet. Clothing follows the natural waist and hip shape without compression, transparent fabric or oversized folds. Tall slender balanced adult build, softly defined waist, natural gentle curves, long proportional legs; keep visible upper-body proportions faithful to image 2 and infer covered areas conservatively, no exaggerated bust or hips. Neutral straight standing posture, shoulders level, arms relaxed slightly separated from waist so silhouette is visible, legs straight and feet a little apart, no hip tilt, no sexual pose. Full head AND both feet fully visible with margin, camera at natural torso height, level camera, no wide-angle distortion. Simple light gray studio background, soft even daylight, realistic skin and anatomy. Single person, single front view, no collage, no labels, no measurements, no text. Highest priority: face must closely match approved image 1.

