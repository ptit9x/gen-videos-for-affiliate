# ep000 — Tên tập

- Trạng thái: nháp, chưa duyệt/chưa tạo clip.
- Phiên bản/ngày:
- Mục tiêu: test hook / tình huống / click sản phẩm (chọn một mục tiêu chính).
- Khán giả và nhu cầu giả định:
- Ý tưởng một câu + mâu thuẫn gây cười:
- Nhân vật: Thảo My solo, trừ khi đã có quyết định khác.
- Tổng thời lượng dự kiến: 24–32s; chốt lại theo thoại, trim và chuyển cảnh.
- Canvas: dọc 9:16, xuất 1080×1920, 30 fps.

## Khóa tài nguyên cho tập

- Ảnh master đã duyệt: đường dẫn cụ thể, chưa điền = chưa chốt.
- Ảnh góc đơn từng clip: ghi đúng tên file từ `characters/thao-my/references.json`, ví dụ `thao-my-angle-front-v001.png`. Giữ nguyên tên khi copy vào `input/references/`; `shots.json` dùng đường dẫn `references/thao-my-angle-front-v001.png`.
- Trang phục/tóc/phụ kiện:
- Bối cảnh, ánh sáng, vị trí đồ:
- Giọng/accent và cách giữ nhất quán:
- Audio: giữ Flow / TTS / ambience; nguồn nhạc và quyền nếu có.

## Sản phẩm (ghi “không affiliate” nếu không dùng)

- Chương trình/quyền được kích hoạt và vị trí đặt link:
- URL listing, SKU, biến thể, người bán, ngày kiểm tra:
- Giá/hoa hồng tại ngày kiểm tra (không hứa giữ nguyên):
- Vai trò sản phẩm trong câu chuyện:
- Footage thật và quyền dùng:
- Claim được nói → bằng chứng tương ứng:
- Công bố AI/thương mại dự kiến:

## Storyboard

| Clip | Khoảng thời gian dự kiến | Vai trò | Thoại tiếng Việt | Một hành động chính | Góc máy/ảnh | Sản phẩm/footage |
|---|---|---|---|---|---|---|
| 01 | 0–8s | Hook | Điền câu ngắn | Điền | Điền | Điền |
| 02 | 8–16s | Tình huống | Điền hoặc không thoại | Điền | Điền | Điền |
| 03 | 16–24s | Phản ứng | Điền hoặc không thoại | Điền | Điền | Điền |
| 04 | 24–32s | Chốt | Điền câu ngắn | Điền | Điền | Điền |

Có thể bỏ/thêm clip theo nhịp kể. Đọc thoại thành tiếng; khoảng 12–18 từ/clip 8s chỉ là mức khởi đầu. Chừa thời gian cho phản ứng, không tăng tốc lời để nhét câu.

## Prompt Flow — bản nháp để review

Sau duyệt, lưu prompt tự đủ nội dung vào `input/prompts/sh010.txt` và các shot tương ứng. Automation đọc file text theo `input/shots.json`, không bóc prompt từ Markdown. Thứ tự và ID phải khớp `episode.yaml`.

### Cấu trúc prompt — lặp cho từng clip

### Clip 01

- File ảnh tham chiếu đính kèm (một góc đơn):
- Chế độ tạo/model và thời lượng thực sự có trong tài khoản:
- Prompt nháp; thay toàn bộ ngoặc vuông trước khi dùng:

```text
Create an approximately 8-second photorealistic Vietnamese sitcom shot, vertical 9:16.
Use the attached approved single-view Thao My reference to preserve her facial identity.
Wardrobe and hair: [exact approved outfit, hairstyle and accessories for this episode].
Location and lighting: [exact room, props, positions and lighting].
Camera: [one framing and camera angle; prefer static coverage].
One main action: [specific action with clear beginning and ending].
Thao My is the only speaker. She speaks Vietnamese in [approved voice/accent],
with natural pacing and [delivery/emotion]: “[exact short Vietnamese line]”.
After the line: [reaction and pause, if any].
No additional dialogue, no background music, no generated subtitles, no watermark.
Keep the same face, hairstyle, wardrobe and room layout throughout the shot.
```

- Nếu không thoại: thay đoạn người nói bằng “No dialogue. [specific reaction]”; vẫn kiểm tra audio vì có thể có âm thanh ngoài ý muốn.
- Nếu dùng TTS: ghi rõ thoại trên là thoại hậu kỳ; không mặc định audio Flow sẽ khớp WAV.
- Clip 02/03/04: tạo khối đầy đủ riêng, không chỉ ghi “giống trên”.

## Hậu kỳ và kiểm tra

- Take được chọn: ghi trong edit/manifest.yaml khi có clip thật.
- Điểm trim/cut, khoảng nghỉ và tổng thời lượng dự kiến:
- Audio giữ/bỏ/thay từng clip:
- Phụ đề theo lời thực tế đã duyệt; SRT canh bản dựng cuối:
- Cảnh sản phẩm thật, chữ/CTA thêm hậu kỳ:
- Kiểm tra mặt, tay, giọng, nói đủ câu, sản phẩm đúng biến thể:
- QC kỹ thuật và phần không đo được: ghi kết quả thật, không đánh dấu trước.

## Đăng và đo lường

- Caption TikTok / caption Facebook:
- CTA khớp đường mua thực tế, hoặc CTA bình luận nếu không affiliate:
- Nhãn AI, công bố thương mại, quyền âm nhạc:
- Link/tracking riêng từng nền tảng nếu được hỗ trợ:
- Người dùng đã yêu cầu đăng bài này: chưa / có (ghi bằng chứng).
- URL bài sau khi đăng:
- Số liệu 24h/72h; click, đơn và hoa hồng sau đối soát nếu có:
- Chi phí/thời gian thực; điều học được và biến thể tiếp theo:
