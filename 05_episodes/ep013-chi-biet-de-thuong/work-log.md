# Work log — ep013 Chỉ Biết Dễ Thương (lúc viết là ep030, đổi số 25/11)

## 2026-11-25 13:21 — Richard gửi link TikTok, hỏi "Cho kịch bản này vào [link]"

- Link: https://vt.tiktok.com/ZSsjMb2wg/ → redirect về https://www.tiktok.com/@alan.z9/video/7698272917985037575 (Thanh Điền - AI Thực Chiến, 35s, 864 like / 45 comment, đăng 19/10).
- Trình duyệt mở được không cần đăng nhập, đọc thoại từ phụ đề burned-in (ASR tự động của trình duyệt bị vỡ, không dùng). Tóm tắt nguồn lưu tại `input/references/source-tiktok.md`.

## 2026-11-25 13:2x — Viết draft ep030, 6 shot × 8s = 48s

- Viết `script.md` draft: chuyển thể cấu trúc gốc (3 bộ đồ → 3 lần "Dễ thương!" → gắt → ấp úng chốt), giữ nguyên ý thoại gốc, viết lại theo giọng Bắc Thảo My.
- `episode.yaml` draft: 6 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả, `editorial_status: draft`.
- `wardrobe.md` draft: My 3 váy SANJOLI khác màu (hồng / kem / trắng, aff-0001, ảnh ref đã có trong sổ đăng ký — lấy lại qua picker, không upload mới); Nam áo phông trắng + jean đen (đề xuất).
- `edit/manifest.yaml`: placeholder copy theo ep029 (chưa tới bước dựng) — tới bước edit sẽ rebuild theo plan giọng trong script (My native-nếu-Bắc không thì clone ThaoMy, Nam giữ native).
- Số tập: ep026–ep028 đã giữ cho 3 draft Ghost (script-only, chưa lưu repo); ep029 đã có trong repo nên tập mới là ep030.
- Chàng trai CHƯA CHỐT lúc draft: đề xuất Nam ep008 (mặt đã có sẵn trong Flow), Thảo ep021 là phương án đổi; chờ Richard chọn.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip, chưa commit repo.

## 2026-11-25 13:45 — Richard DUYỆT kịch bản, CHỐT Nam ep008

- Richard gật widget "Duyệt draft, chốt Nam ep008".
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 25/11, chàng trai chốt Nam ep008; `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo (Nam áo phông trắng + jean đen theo draft).
- Trang phục My (3 váy SANJOLI hồng/kem/trắng) + bối cảnh phòng khách lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Đối chiếu script ↔ episode.yaml: 6 shot, thoại khớp từng chữ, số tiếng đếm tay 8/2/4/3/15/6 (đều trong ngân sách 8s). Cờ vàng duy nhất: sh050 có 2 câu trong 1 shot (15 từ) — giữ nguyên theo bản đã duyệt; phương án dự phòng gộp thành 1 câu đã ghi trong script, chỉ dùng khi take 1 đọc vội và phải báo Richard trước khi đổi thoại.
- Lưu hồ sơ vào repo: commit riêng scope ep030, chạy validator trước, push lên main. Validator đạt (exit 0; chỉ note thiếu frame 6/6 shot + voice pending — đúng trạng thái draft, như ep029).
- Bước tiếp theo: làm 6 frame (project Flow riêng `CNTM · EP030 · Chỉ Biết Dễ Thương`, 0 credit) — lấy lại nhân vật Nam từ project ep008 qua picker, 3 váy SANJOLI lấy lại qua picker từ project ep004/ep002/ep003, nền phòng khách từ `03_locations/thao-my-apartment/living-room/` — chờ Richard gật làm frame, hoặc đổi đồ/location trước.

## 2026-11-25 16:37 — Richard chốt đổi số: ep030 → ep013 (làm sớm hơn, Gym lùi xuống ep030)

- Richard: "Cái này làm sớm hơn, đổi đánh thứ tự đi, mai làm luôn".
- Đổi số bằng `git mv` thư mục ep030-chi-biet-de-thuong → ep013-chi-biet-de-thuong; sửa `ep030` → `ep013` trong script.md, episode.yaml, wardrobe.md, manifest.yaml, source-tiktok.md (tham chiếu live). Các entry work-log cũ giữ nguyên số ep030 vì đó là lịch sử lúc viết (commit `3dc7244` vẫn mang scope ep030).
- Hồ sơ sau đổi số: đối chiếu lại script ↔ episode.yaml (6 shot, thoại khớp), chạy validator, commit riêng + push.
- Bước tiếp theo: làm 6 frame ngày mai 26/11 (project Flow riêng `CNTM · EP013 · Chỉ Biết Dễ Thương`, 0 credit) — lấy lại nhân vật Nam từ project ep008 qua picker, 3 váy SANJOLI lấy lại qua picker từ project ep004/ep002/ep003, nền phòng khách từ `03_locations/thao-my-apartment/living-room/`.

## 2026-11-26 06:5x — Chuẩn bị làm frame, chờ gen ep012 xong

- Viết xong 12 prompt ảnh/motion (`input/prompts/sh0X0-image.txt` + `sh0X0-motion.txt`), map sha vào episode.yaml, validator đạt (exit 0; chỉ note thiếu frame 6/6 + voice pending — đúng trạng thái).
- Prompt ảnh: khóa nền phòng khách buổi tối đèn vàng (sofa be trái, 2 tranh pastel, bàn trà gỗ nhạt, ban công tối) + son đỏ/móng tự nhiên/nốt ruồi cằm trái; màu váy ghi rõ từng bộ (hồng sh010 / kem sh030 / trắng sh050) để tránh lẫn dưới đèn vàng.
- Prompt motion: 1 hành động + thoại nguyên văn + hướng giọng, không ghi cấm phụ đề/chữ (theo verdict review ep009 22/11 — ghi cấm phụ đề vào prompt Veo làm Veo vẽ thêm chữ giả).
- Refs lấy lại qua picker, không upload mới: mặt My ThaoMy002 (project EP003), Nam từ project ep008, váy hồng từ project ep004, váy trắng từ project ep003. Váy kem: sổ đăng ký chưa ghi rõ project Flow — lấy file local `02_characters/thao-my/wardrobe/inbox/ep002-sanjoli-kem/vn-11134207-81ztc-mthrovoch3ibe2.webp` đưa vào project ep013 khi làm sh030.
- Nền phòng khách: ảnh review thao-my-living-room-v001.png (ban ngày) CHƯA duyệt, chưa có master — frame sh010 sẽ khóa nền buổi tối, trình Richard duyệt nền trước khi làm nốt 5 frame.
- CHỜ: gen lại sh020 ep012 đang chạy (bắt đầu 06:31, kẹt kiểm tra bot Flow) — KHÔNG mở task Flow song song. Gen ep012 xong mới tạo project 'CNTM · EP013 · Chỉ Biết Dễ Thương' + làm sh010.

## 2026-11-26 06:58 — Richard chốt đổi sh050 trắng → đen (3 váy hồng/kem/đen, xanh dự phòng)

- Richard tự rà lại: váy hồng ở tập Chia Bill (ep004), váy đen ở tập Hẹn Hò Một Mình (ep006), váy kem đúng; chốt dùng 3 váy, váy xanh ep005 (Hẹn Hò Với Mẹ Anh) làm dự phòng nếu cần thêm.
- Đổi sh050 trắng → đen trong wardrobe.md, script.md, prompt sh050 (image + motion), cập nhật sha vào episode.yaml; validator đạt (exit 0). Lợi thêm: đen tách rõ khỏi kem/hồng dưới đèn vàng, hết hẳn rủi ro kem–trắng lẫn như bản draft cũ.
- Gen sh020 ep012 đã xong 06:53 (take005, commit 6fba92f) — Flow rảnh, làm sh010 ngay sau commit này.
