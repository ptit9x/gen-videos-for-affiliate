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

## 2026-11-26 07:09 — Frame sh010 v1 XONG (Flow, 0 credit)

- Project mới 'CNTM · EP013 · Chỉ Biết Dễ Thương' https://flow.google.com/project/2eee36ea-3b8f-486c-a531-520cf34e242f; asset sh010 cea46e42-6641-4b1c-a869-48bf6ec1ece9; Nano Banana 1 edit trực tiếp từ master ThaoMy002 (mặt lấy lại từ EP003 qua picker, váy hồng lấy lại từ ep004 qua picker, nền phòng khách upload 1 lần file local thao-my-living-room-v001.png).
- File tải về: browser_downloads/sess-920868313/browser-download-20261126T000855.412967987Z-1-sh010_1c403fe4.png (768×1376, sha 1879d57e…).
- Bee QC: ĐẠT — mặt khớp ThaoMy002, váy hồng rõ, nền buổi tối đèn vàng ấm, ban công tối, sofa be trái + 2 tranh pastel + khăn len + bàn gỗ nhạt. Nits: sao Gemini nhỏ góc phải dưới (như 4 frame ep011 đã duyệt); khung toàn thân thay vì cận vừa (khoe trọn váy — Richard quyết).
- CHỜ: Richard duyệt nền + sofa + đèn vàng → làm nốt 5 frame.

## 2026-11-26 07:28 — Frame sh010 v2 (sửa theo ý Richard, 1 edit trực tiếp trên v1)

- Richard duyệt nền, bắt 2 lỗi: ngực cần to hơn, nốt ruồi sai vị trí. Sửa trực tiếp trên frame v1 bằng 1 edit Nano Banana (giữ nguyên nền đã duyệt), 0 credit.
- File tải về: browser_downloads/sess-920868313/browser-download-20261126T002743.104812894Z-2-sh010_376cedd0.png (768×1376, sha ba3ccc7e…).
- Bee QC: ĐẠT — ngực đầy đặn hơn rõ rệt, vẫn tự nhiên; nốt ruồi về đúng cằm trái (dưới môi trái); mặt/tóc/váy hồng/nền giữ nguyên; sao Gemini nhỏ góc phải dưới vẫn còn (nit cũ).
- CHỜ: Richard duyệt v2 → làm nốt 5 frame (dùng chung nền + chuẩn ngực/nốt ruồi của v2).

## 2026-11-26 07:29–07:54 — Nốt ruồi sh010: v2 bị bắt lỗi, v3 Flow không cứu được, v4 sửa bằng pixel-edit (CHỜ duyệt)

- Richard 07:29: nốt ruồi v2 "nhìn kinh thế, nó ở cằm bên kia mà" (sai bên + quá đậm); ngực thì ok. Ghi nhận: ngực + nền đã duyệt, chỉ còn nốt ruồi.
- Soi kỹ bằng crop phóng to + đo pixel: v2 thực tế có 2 chấm — 1 nốt to đậm dưới môi lệch phải + 1 nốt nhỏ trên má; master ThaoMy002 chỉ có đúng 1 nốt rất nhỏ, mờ, dưới môi lệch trái một chút so với giữa cằm.
- v3 (Flow, 6 edit Nano Banana trực tiếp trên v2, 0 credit): xóa được cả 2 nốt sai, còn đúng 1 nốt nhỏ — NHƯNG đo pixel thì nốt vẫn ở gần như chỗ cũ (x≈427, không dịch sang trái rõ), mặt mềm đi sau 6 lần sửa nối tiếp → KHÔNG dùng v3. File tải về: browser_downloads/sess-920868313/browser-download-20261126T004411.981150299Z-3-sh010_3c10afd3.png (sha cef4f9ab…).
- v4 (pixel-edit trực tiếp trên mặt v2 đã duyệt, KHÔNG qua Flow): file `~/workspace/ep013-source-check/sh010-v4-molefix.png` (768×1376, sha 03738f88…). Xóa nốt thừa trên má bằng Laplace inpaint; đặt đúng 1 nốt nhỏ mờ (Gaussian alpha, r≈1.8px) tại (412,516) — dưới môi, cằm trái theo hướng nhìn vào ảnh, khớp vị trí tương đối trên master. Mặt/ngực/nền giữ nguyên 100% v2 (diff chỉ quanh vùng sửa; detector xác nhận: má sạch, đúng 1 nốt mới, mọi cluster khác y hệt v2).
- Bài học đo được: "nốt to" dưới môi hóa ra là MÉP TÓC (vệt tối dọc x≈427, y 512–548, lum 3–27) chứ không phải nốt ruồi tròn — đừng xóa mép tóc; kiểm tra hình dạng bằng crop neighbor + profile độ sáng, đừng tin zoom Lanczos (nó biến mép tóc thành chấm tròn). Nano Banana KHÔNG dịch được chi tiết 2–3px (6 lần sửa vẫn về cùng chỗ) — sửa nốt ruồi thì làm pixel-edit trên frame đã duyệt.
- CHỜ: Richard duyệt v4 → làm nốt 5 frame (sh020–sh060), kiểm tra 3 váy cạnh nhau, map frame vào episode.yaml + validator + commit.

## 2026-11-26 08:09 — Richard: bỏ hẳn nốt ruồi (v5, mặt sạch)

- Richard: "chưa đúng, bỏ nốt ruồi đi vậy" → bỏ hẳn nốt ruồi khỏi frame sh010, không đặt lại.
- v5 (pixel-edit trên v4): xóa nốt v4 tại (412,516) bằng Laplace inpaint r=4; file `~/workspace/ep013-source-check/sh010-v5-nomole.png` (768×1376, sha a0d963f0…). Detector xác nhận vùng cằm/má sạch nốt (chỉ còn mép tóc + các chi tiết gốc của v2); mặt/ngực/nền giữ nguyên 100% v2.
- QUYẾT ĐỊNH ÁP CHO CẢ TẬP (để đồng nhất): 5 frame còn lại cũng bỏ nốt ruồi — khi làm frame mới, nếu Nano Banana vẽ nốt ruồi theo master thì xóa bằng pixel-edit trước khi trình. Nốt ruồi vẫn là đặc điểm của master ThaoMy002 trong hồ sơ nhân vật; riêng tập ep013 chốt mặt sạch không nốt.
- CHỜ: Richard duyệt v5 → làm nốt 5 frame (sh020–sh060), kiểm tra 3 váy cạnh nhau, map frame vào episode.yaml + validator + commit.

## 2026-11-26 08:10–08:35 — Richard: "chưa sạch" (v5 còn 2 nốt) → v9, mặt sạch

- Vấn đề thật của v5: còn 2 nốt — nốt cằm lớn (432,502) + chấm má nhỏ (421,479). Lỗi của tao: các bản v4/v5/v6 đo sai vị trí — đọc tọa độ bằng mắt trên crop phóng to lệch 10–30px, khoanh nhầm vào mép tóc (427,526) và chấm mờ trên hàm (380,522) thay vì nốt thật.
- Cách đo ĐÚNG (đã chứng minh): chạy detector trên crop mặt (không đọc bằng mắt) — nốt cằm lớn: cluster tròn 21×19px, minlum 4, tâm (431.6,502.0); chấm má: cluster 10×12, tâm (421.4,479.3).
- v6: khoanh đúng tâm nhưng Laplace thường bị môi kéo tối (mean 73) → v7: Laplace skin-only (chỉ lấy biên sáng) + chỉ ghi lại pixel trong mask (không ghi ring) → nốt sạch (min 132) nhưng vùng fill phẳng (std 1.8) lộ ở zoom 3x. v8: texture transfer từ patch má sai (std 33, có bóng tối) → rải chấm đen. v9 (bản trình): fill skin-only + texture từ patch trán sạch đã verify (x470,y340, std 3.2), detail clip ±10 → nốt cằm + chấm má đều sạch, detector xác nhận KHÔNG còn cluster nốt nào; các vệt tối còn lại quanh miệng/cằm là giải phẫu có sẵn từ v2 (bóng khóe miệng (436,488), miệng, mép tóc) — KHÔNG xóa, xóa sẽ hỏng miệng.
- File trình: `~/workspace/ep013-source-check/sh010-v9-clean.png` (768×1376, sha 0b643e8e…).
- BÀI HỌC: đừng bao giờ định vị nốt/chấm bằng mắt trên ảnh zoom — luôn chạy detector trên crop rồi mới khoanh; kiểm chứng bằng detector sau khi sửa, không tin mắt.
- CHỜ: Richard duyệt v9 → làm nốt 5 frame (sh020–sh060, cũng bỏ nốt ruồi), kiểm tra 3 váy cạnh nhau, map frame vào episode.yaml + validator + commit.

## 2026-11-26 08:29–08:55 — Flow xóa nốt (thất bại) + pixel v12–v16 (đạt)

- Flow: 1 edit Nano Banana từ v2, lệnh "Remove ALL dark moles..." — chỉ xóa được chấm má, NỐT CẰM LỚN VẪN CÒN NGUYÊN (detector: cluster 144px tại đúng (431.4,502.0), y hệt v5). Báo cáo trình duyệt nói "cả 2 đều sạch" là SAI — lại thêm 1 bằng chứng: Nano Banana KHÔNG xóa được nốt cằm (neo vào mặt master), và KHÔNG được tin báo cáo "đã sạch" của trình duyệt khi chưa đo pixel. File Flow: `~/workspace/ep013-source-check/sh010-flow-nomole.png` (sha 9c34a6b1) — KHÔNG DÙNG.
- Pixel v12–v16: v9 còn vệt đuôi nốt (trail) ở (428.6,509.3) — đó là cái Richard thấy ở v9 ("vẫn còn"). v12 xóa trail bằng capsule; v13 vá thêm đầu mút nốt (433,510); v14 chỉnh màu (vùng fill cũ đỏ/nâu do lấy tone từ môi); v15/v16 làm lại từ v5 bằng DIRECT FILL (không Laplace — Laplace hút màu tối từ môi/tóc xung quanh nên vùng fill tối và phẳng): lấy tone da cằm đo được [200,141,111], gradient dọc, ellipse hữu cơ + feather rộng + texture trán clip ±8.
- v16 (bản trình): detector xác nhận nốt cằm lớn + chấm má + vệt đuôi đều HẾT; điểm tối nhất vùng cằm còn lại là mép tóc (tự nhiên, có sẵn từ v2); điểm tao "thấy" ở crop (488,502) đo ra mean 122/min 107 = tone da, KHÔNG phải nốt — mắt tao đọc sai ở mức zoom này, tin số đo. File: `~/workspace/ep013-source-check/sh010-v16-clean.png` (768×1376, sha e4c0516d…).
- BÀI HỌC (ghi vào AGENTS.md sau khi duyệt): (1) Nano Banana không xóa được nốt ruồi trên cằm — đừng thử lại. (2) Nốt ruồi không phải 1 chấm tròn mà là cụm: nốt chính + vệt đuôi dưới nó — xóa phải hết cả cụm. (3) Laplace inpaint ở sát môi/miệng/tóc sẽ hút màu tối → vùng fill tối/phẳng/nâu — dùng direct fill bằng tone da đo được + gradient + feather rộng. (4) Đừng tin mắt mình ở zoom 3–4x — đo pixel (detector + patch stats) mới là chuẩn.
- CHỜ: Richard duyệt v16 → làm nốt 5 frame (sh020–sh060, cũng bỏ nốt ruồi), kiểm tra 3 váy cạnh nhau, map frame vào episode.yaml + validator + commit.

## 2026-11-26 08:36–08:44 — Frame sh010 MỚI gen từ đầu (Richard: "gen lại từ ảnh")
- Gốc rễ tìm ra: prompt sh010-image.txt ghi sẵn "nốt ruồi cằm trái" — nên mọi frame gen ra đều có nốt. Đã sửa prompt sh010/sh030/sh050 → "KHÔNG có nốt ruồi, da mặt sạch, cằm sạch", cập nhật episode.yaml shas, validator đạt, commit e3394fb đã push.
- Frame mới: 1 lần gen Nano Banana 2.1 từ refs (ThaoMy002 + váy hồng ep004 + phòng khách, qua picker, 0 credit), asset MỚI 568a427c-632d-4b79-b022-dbd415ac2662 (tách khỏi asset sh010 cũ cea46e42). File: `~/workspace/ep013-source-check/sh010-fresh.png` (768×1376, sha 4e3c4427…).
- Bee QC: mặt SẠCH, KHÔNG nốt ruồi (detector + xem crop mặt); váy hồng rõ; phòng khách buổi tối giống nền v2 đã duyệt (sofa be + 2 tranh + bàn gỗ + ban công tối); ngực đầy đặn tự nhiên; không chữ/logo. Khác v2: dáng đứng chính diện hơn, đầu quay phải, cười tươi lộ răng (v2 xoay 3/4). Sao Gemini nhỏ góc phải dưới (nit cũ).
- CHỜ: Richard duyệt frame mới → làm nốt 5 frame (sh020–sh060, prompt đã bỏ nốt), kiểm tra 3 váy cạnh nhau, map frame vào episode.yaml + validator + commit.

## 2026-11-26 09:01–09:06 — sh020 framing: Richard muốn sát mặt Nam hơn
- sh020 v1 (Nam ngồi sofa, medium shot) + v2 close-up (crop 480×854 tại x80,y400 + lanczos upscale → 768×1376, mặt giữ nguyên pixel) đã trình; Richard: "sát nữa vào, lấy nửa người và không góc nghiêng" + "thẳng mặt đi".
- Crop KHÔNG xoay được mặt (v1/v2 mặt Nam đang nghiêng 3/4 nhìn sang trái) → cần gen mới: Nam nhìn thẳng vào máy quay, nửa người (ngực trở lên), mặt lớn trong khung.
- Chuẩn bị ref: `~/workspace/ep013-source-check/nam-front-tight.jpg` — crop chặt mặt + vai từ master Nam frontal v002 (sha 340a246d, mặt chính diện, 2 mắt đối xứng) để neo cỡ mặt lớn.
- CHỜ: task Flow retry sh040/sh050/sh060 đang chạy — KHÔNG chạy 2 task Flow song song. Gen lại sh020 frontal ngay khi task kia xong, dùng ref Nam tight + Nam character qua picker + phòng khách, prompt sửa "nhìn thẳng vào máy quay, mặt chính diện".

## 2026-11-26 08:44–09:00 — Gen 5 frame còn lại: sh020 + sh030 xong, sh040/sh050/sh060 chặn "unusual activity"
- Batch 5 frame (1 lần gen/frame, 0 credit): sh020 Nam cười khoái (asset e469973a, file sh020-v1.png sha ebcac554…) + sh030 My váy kem (asset d8c7f1cd, file sh030-v1.png sha 4420c9c5…) XONG + tải về. Bee QC: sh020 mặt khớp Nam, áo trắng + jean đen, phòng khách y hệt; sh030 váy kem rõ khác hẳn hồng, mặt sạch không nốt (detector + xem trực tiếp), nit: đèn bàn lọt thêm vào nền.
- sh040/sh050/sh060: Flow chặn "Chúng tôi nhận thấy có hoạt động bất thường nào đó..." sau 2 lần gen liên tiếp, KHÔNG tốn credit, không retry trong lượt đó. Bài học: gen liên tiếp 2 frame là chạm ngưỡng — phải chờ + gen từng cái cách nhau.

## 2026-11-26 09:01–09:17 — Retry sh040/sh050/sh060: CẢ 3 XONG
- Chờ 5 phút + gen từng cái cách nhau ~1 phút → cả 3 đều qua, không bị chặn. sh040 Nam gãi đầu (asset d7cf4553, sh040-v1.png sha af781fed…); sh050 My váy đen chống nạnh (asset 713a3c42, sh050-v1.png sha 66ff37f2…, váy HLS L14 đen tuyền, mặt sạch không nốt); sh060 Nam cúi đầu vân vê gối (asset 24b59127, sh060-v1.png sha 8efc9def…). Bee QC đạt cả 3. Nit continuity: lọ hoa tulip trên bàn trà lúc có (sh020/sh040/sh060) lúc không (sh010/sh030/sh050).
- Đủ 6 frame. Dress check: hồng sh010 H8 L68 / kem sh030 ấm / đen sh050 L14 — 3 màu phân biệt rõ.

## 2026-11-26 09:05–09:21 — sh020 frontal: Richard muốn sát mặt, nửa người, mặt thẳng
- sh020 v2 close-up (crop 480×854 tại x80,y400 + lanczos upscale từ v1, mặt giữ nguyên pixel) đã trình; Richard: "sát nữa vào, lấy nửa người và không góc nghiêng" + "thẳng mặt đi". Crop không xoay được mặt → gen mới.
- Richard: "ok 10 phút sau hẵng làm lại cho chắc" → hẹn giờ sleep 600s (09:07–09:17), gen sau khi đủ 10 phút + task retry xong.
- Gen mới 09:18–09:21 (1 lần, 0 credit): ref Nam character qua picker + crop mặt chính diện `nam-front-tight.jpg` (640×940, từ master Nam frontal v002 sha 340a246d) + phòng khách. Asset MỚI ba0fd264, file `~/workspace/ep013-source-check/sh020-frontal-v1.png` (768×1376, sha de841d4e…). Bee QC: mặt Nam thẳng vào máy quay, nửa người ngực trở lên, mặt to trong khung, nền cắt gọn, mặt khớp Nam. Asset cũ e469973a vẫn nằm trong project (không xóa).
- CHỜ: Richard duyệt sh040/sh050/sh060 + sh020 frontal → map 4 frame vào episode.yaml (thay sh020 v1 bằng frontal v2) + validator + commit → kiểm tra continuity cả 6 frame cạnh nhau → gen 6 clip Veo 3.1 Lite (60 credit) sau khi đủ frame duyệt.

## 2026-11-26 09:36–09:49 — sh020 frontal v1/v2: Richard bắt sai vị trí — Nam phải đối diện My, phía cửa ra vào
- v1 frontal (asset ba0fd264, mặt thẳng, nửa người, giữa khung): Richard 09:36 "Nam ở góc khác đi, góc đó là ThaoMy đứng rồi mà, background sau ấy" — Nam ngồi giữa khung = đúng chỗ My đứng trong các shot của cô ấy, nền tranh + ban công y hệt.
- v2 (asset 411ad989, ngồi đầu phải sofa, người nghiêng, liếc máy): Richard 09:46 "ko đúng, ngồi đối diện ThaoMy chứ" — người Nam xoay ngang, không hướng về phía My. Bee hiểu sai 2 lần: "góc khác" không phải đổi góc trong khung mà là đổi VỊ TRÍ trong phòng.
- Richard 09:49 chốt: "Nam sẽ phải ngồi ở góc đối diện ThaoMy, tức là hướng cửa ra vào" — Nam ngồi góc đối diện My, phía cửa ra vào; mặt hướng thẳng về phía My; nền sau là cửa ra vào + tủ giày, KHÔNG sofa/tranh/ban công. Ghế: ghế bành đơn gần cửa (Bee tự chọn — sofa nằm phía My).
- v3 (ngồi trái khung, hướng thẳng máy quay) gửi 09:47: Flow CHẶN "unusual activity" 09:49 — gen thứ 3 trong ~11 phút, không tốn credit, không có asset mới, không retry trong lượt. Bài học: gen sh020 dồn dập 3 lượt/11 phút là chạm ngưỡng; lần sau chờ 5 phút giữa các lượt gen cùng 1 frame.
- ĐANG CHẠY: retry v4 với blocking cửa ra vào + chờ 5 phút trước khi submit (theo đúng mẫu retry sh040/50/60 đã thành công).

## 2026-11-26 09:50–09:58 — sh020 v4 (cửa ra vào): Flow chặn lần 2 — cứu bằng media pipeline
- Retry v4 (ghế bành gần cửa ra vào, mặt hướng My, nền cửa + tủ giày) sau 5 phút nghỉ: Flow CHẶN lần 2 liên tiếp ("unusual activity"), không tốn credit, không có asset mới. 5 phút nghỉ KHÔNG đủ lần này (khác đợt sh040/50/60). Bài học: sau 2 lần chặn liên tiếp thì đừng gen Flow dồn nữa — nghỉ dài hơn hoặc đổi đường.
- Fallback (tiền lệ ep008: Flow chặn 3 shot Nam → media pipeline cứu 3/3): gen bằng media pipeline của Bee từ ảnh mặt Nam (nam-front-tight.jpg) — file `~/workspace/ep013-source-check/sh020-door-v1.png` (sha befe23d6…). Bee QC: mặt khớp Nam, mặt thẳng vào máy, nửa người, mặt to; nền cửa gỗ + tủ giày có giày, KHÔNG sofa/tranh/ban công; áo trắng + jean đen; không chữ/logo/sao Gemini. Nit: ghế bành xám (khác sofa be — hợp lý vì góc cửa), ánh sáng sáng hơn các shot kia một chút.
- CHỜ: Richard duyệt frame cửa ra vào này (hoặc chọn retry Flow sau khi nghỉ dài).

## 2026-11-26 12:04 — sh020 CHỐT bản cửa ra vào, đã map vào hồ sơ
- Richard 👍 bản door-side (media pipeline) 12:04 → CHỐT làm sh020.
- Map: `input/frames/sh020-frame-v2.jpg` (1152×2048, sha 59752aa5…, từ sh020-door-v1.png sha befe23d6…); episode.yaml sh020 → first_frame v2, image_prompt + motion_prompt viết lại theo blocking cửa ra vào (ghế bành gần cửa, mặt hướng My), flow_image_asset_id: null (tiền lệ ep008: frame media pipeline ghi null). frame_status approved, approved_for_generation true. Frame rộng cũ sh020-frame-v1.jpg giữ nguyên trong thư mục (không xóa).
- CHỜ: Richard duyệt sh040/sh050/sh060 (đã trình 09:21, chưa gật) → map 3 frame → kiểm tra continuity cả 6 frame → gen 6 clip Veo 3.1 Lite (60 credit).

## 2026-11-26 12:05 — Map sh040/sh050/sh060 + kiểm tra continuity cả 6 frame: PASS
- Richard "ok" 12:05 → map 3 frame còn lại: sh040-frame-v1.jpg (sha 1e5f32f7…, asset d7cf4553), sh050-frame-v1.jpg (sha 856b2361…, asset 713a3c42), sh060-frame-v1.jpg (sha f6fa85da…, asset 24b59127). episode.yaml cả 3 → approved + approved_for_generation true.
- Cross-frame continuity (contact sheet 6 frame, so cạnh nhau + đo HLS):
  - VERDICT: PASS. Mặt My (sh010/030/050) và mặt Nam (sh020/040/060) nhất quán; son đỏ + móng tự nhiên đủ 3 shot My; KHÔNG nốt ruồi cả 6 frame; Nam áo trắng + jean đen đủ 3 shot; 3 váy phân biệt rõ (hồng H9-13 L67-69 / kem H26-27 L39-55 / đen L14-23).
  - Nits (không chặn): (1) lọ hoa tulip trên bàn trà: có ở sh040/sh060, không ở sh010/sh030/sh050; (2) đèn bàn lọt thêm ở sh030; (3) sách trên bàn trà ở sh040/sh060; (4) sh020 góc cửa ra vào sáng hơn + ghế xám — cố ý theo blocking Richard chốt, không tính lỗi continuity.
- CHỜ: Richard gật gen 6 clip Veo 3.1 Lite (60 credit, số dư ~100) → gen từng clip, QC take, dựng master.

## 2026-11-26 12:07–12:25 — Gen 6 clip: chỉ được 2/6, Flow chặn 4 clip + sh020 take001 CÂM
- Richard gật gen 6 clip 12:07 (60 credit). Task mới (Env 2): sh010 take001 (clip af4a540f, 7.93s) + sh020 take001 (clip 4d9a6a9e, 8.00s) XONG + tải 1K. sh030/sh040/sh050/sh060: Flow chặn "unusual activity" cả 4 (mỗi shot 1 lượt, cách nhau ~1 phút), không tốn credit, không retry.
- CREDIT — ĐÍNH CHÍNH: số dư đầu lượt là 40 (không phải ~100 như Bee ước), 2 clip tốn 20, còn 20. 5 clip còn lại (sh030/40/50/60 + sh020 take002) cần 50 credit — thiếu 30. Refresh hằng ngày lúc 23:07 (số credit refresh chưa rõ).
- QC take: sh010 take001 — Whisper base đủ 8 từ đúng thứ tự 0.00-1.96s, F0 median 230Hz (giọng nữ); hình mặt khớp, váy hồng, xoay người cười, không chữ giả → needs_review, đề xuất CHỐT nếu Richard nghe giọng Bắc. sh020 take001 — REJECT: clip KHÔNG CÓ ÂM THANH (Flow "Chưa tạo âm thanh nào", ffprobe không audio stream, năng lượng 0) + Nam cười há miệng suốt → cần gen lại take002. faster-whisper đã mất sau VM restart, cài lại bằng pip --ignore-installed (numpy lên 2.5.5, scipy vẫn import được, chỉ warning).
- CHỜ: Richard chọn — (A) chờ refresh 23:07 rồi gen cả 5, hoặc (B) gen 2 clip nữa sau khi nghỉ (sh030+sh040) rồi gen nốt sau refresh.

## 2026-11-26 13:57 — sh010 take001 REJECT: mặt không giống ThaoMy
- Richard xem frame clip 5s: "mặt này không giống ThaoMy". Bee soi frame đã duyệt vs clip cạnh nhau: mặt clip tròn/rộng hơn, mắt + nụ cười khác hẳn — Veo drift mặt dù gen từ đúng frame đã duyệt. Take001 → rejected_editorial.
- Fix: gen lại take002, prompt + frame y nguyên (10cr) — lỗi drift ngẫu nhiên thì re-roll. Tổng clip còn cần: 6 (sh010 take002 + sh020 take002 + sh030/40/50/60), cần 60cr, số dư 20, refresh 23:07.
- CHỜ: Richard chọn — (A) chờ refresh 23:07 rồi gen cả 6, hoặc (B) gen 2 clip nữa sau khi nghỉ.

## 2026-11-26 13:59–14:07 — Gen 2 clip (sh030 + sh040): cả 2 đều ra, không bị chặn
- Richard chọn "gen 2 clip nữa sau khi nghỉ" 13:58. Task mới Env 2: sh030 take001 (clip 92030214, 7.93s) + sh040 take001 (clip 14dd8966, 7.93s), nộp cách nhau ~3 phút, KHÔNG bị chặn. Cả 2 tải 1K về đĩa, đều có audio.
- QC: sh030 take001 — Whisper base đủ 4 từ "Thế còn bộ này" (onset thật ~0.4s), F0 215Hz nữ; hình mặt khớp ThaoMy, váy kem rõ → needs_review, đề xuất CHỐT nếu Richard nghe giọng Bắc. sh040 take001 — REJECT: Veo nói câu 2 LẦN (Whisper 0.00-1.30s + 2.12-4.20s; energy envelope xác nhận 2 burst thoại thật, không phải artifact ASR); hình thì đúng → cần gen lại take002.
- CREDIT: số dư giờ 0 (panel Flow). 4 clip còn lại (sh010 take002 + sh020 take002 + sh050 + sh060, 40cr) CHỜ refresh 23:07.
- NOTE: faster-whisper lại mất sau VM restart — cài lại bằng pip --ignore-installed (lần 2 trong ngày). Ghi nhớ: pip package ngoài ~ bị wipe khi restart, kiểm tra lại đầu mỗi lần QC.

## 2026-11-26 15:27 — Richard duyệt sh030 take001: CHỐT TẠM
- Richard xem video thật: "trông mặt cũng chưa giống lắm nhỉ, giọng thì Bắc rồi, tạm ổn" + "Dáng hơi lùn" → take001 accepted_editorial (chốt tạm, ghi nhận caveat: mặt chưa giống hẳn, dáng lùn hơn frame).
- Pattern drift của Veo ở ep013: sh010 mặt tròn/rộng hơn frame; sh030 mặt chưa giống hẳn + dáng lùn hơn frame. Veo có xu hướng làm My tròn/lùn hơn ảnh đầu — chấp nhận "tạm ổn" theo tai/mắt Richard từng take, không đốt credit re-roll chỉ vì drift nhẹ khi cậu ấy đã gật.
- Còn lại 4 clip (sh010 take002 + sh020 take002 + sh050 + sh060, 40cr) — CHỜ refresh 23:07, số dư 0.

## 2026-11-26 16:57–17:05 — Gen sh010 take002 trên acc tinphim (project mới)
- Richard lệnh chuyển Flow sang tinphim2016@gmail.com (huynhdn hết Pro). Mật khẩu vault sai (đã sai 2 lần 12/11 + 1 lần 16:55), Richard tự gõ pass 16:57 → Flow vào tinphim "Richard Youtuber" PLUS, 50cr, reset 09:32 3/12.
- ĐÍNH CHÍNH số clip còn thiếu: không phải 4 mà là **5** (sh010t2 + sh020t2 + sh040t2 + sh050 + sh060 = 50cr) — sh040 take001 cũng REJECT (nói 2 lần) nhưng work-log 13:59 đếm sót. Richard lệnh "gen từng cái 1 bắt đầu từ 010" → làm tuần tự, mỗi clip QC + trình riêng.
- Project ep013 cũ (huynhdn, 2eee36ea) không mở được từ tinphim → tạo project MỚI "CNTM · EP013 · Chỉ Biết Dễ Thương" https://flow.google.com/project/7ac61787-27b9-4022-ac91-fe3f15d02414, Frames-direct, upload frame sh010-frame-v1.jpg làm frame đầu, Veo 3.1 Lite 10cr, KHÔNG bị chặn "unusual activity", không lỗi celebrity.
- sh010 take002 (clip 00fb14d4, 7.93s, 720x1280, sha 0e4bdc03…): Whisper base đủ 8 từ 0.00-2.22s nhưng nghe "thế sao" thay "thấy sao" (browser ASR cũng nghe "thế" — có thể Veo phát âm gần giống, cần tai Richard); 1 burst thoại duy nhất, không lặp câu; F0 ~258Hz nữ. Hình: mặt khớp frame đã duyệt (không tròn/rộng như take001), váy hồng rõ, 4s quay lưng theo động tác xoay. Nit: watermark Veo + sao Gemini góc phải dưới. Số dư tinphim: 40cr. Trạng thái: needs_review.
- Lưu ý kỹ thuật: faster-whisper lại mất sau VM restart (lần 3 trong ngày) — cài lại `pip install --break-system-packages --ignore-installed faster-whisper`; av 19.0.2 không tương thích faster-whisper 1.2.1 (`metadata_errors` kwarg) → QC phải decode wav bằng ffmpeg + đọc bằng module wave, không qua scipy (scipy gãy do numpy 2.5.5). CẢNH BÁO: đừng dùng scipy trong QC khi numpy đã lên 2.x.
- flow_image_asset_id sh010 trong episode.yaml vẫn là asset cũ huynhdn (568a427c) — asset ID mới bên tinphim chưa được browser báo, cần bổ sung khi lấy được.

## 2026-11-26 18:38 — sh010 take002 REJECT: mặt không giống ThaoMy
- Richard xem video take002: "Mặt ổn cái con khỉ, mặt ko giống ThaoMy chút nào" → take002 rejected_editorial.
- Bee nhận sai: QC của Bee bảo "mặt khớp frame đã duyệt" là SAI — mắt Bee không đáng tin ở khâu soi mặt. Từ nay không trình nhận định "mặt khớp" như kết luận; chỉ trình video + số đo kỹ thuật, mặt do Richard quyết.
- LUẬT MỚI (Richard 18:39): lần tới gửi ẢNH cho Richard duyệt TRƯỚC mới được gen video. Áp dụng cho mọi clip tiếp theo, kể cả frame đã duyệt từ trước — gửi đúng ảnh frame sẽ dùng làm frame đầu, chờ gật rồi mới bấm gen.
- Hệ quả credit: số dư tinphim 40cr; 4 clip còn lại (sh020t2, sh040t2, sh050, sh060) cần đúng 40cr. Nếu sh010 cần take003 nữa thì tổng cần 50cr — thiếu 10, phải chờ reset 09:32 3/12 hoặc bỏ 1 clip. Chờ Richard chọn hướng.

## 2026-11-26 19:14–19:20 — Frame sh010 v2: Flow chặn, cứu bằng pipeline
- Flow (tinphim, project 7ac61787): sau khi Richard bấm Yes trên app Google, browser vào lại project, set Image mode Nano Banana 2.1, 9:16, 1 output, 0 credit, upload đủ 3 ref (mặt v002, body v003, frame v1) + nộp mô tả 1 lần → Flow báo "Không thành công — hoạt động bất thường", KHÔNG tốn credit, KHÔNG có ảnh. Browser dừng theo luật (không retry). Số dư vẫn 40cr.
- Đổi đường sang pipeline của Bee (tiền lệ cứu sh020 door-frame ep013 + 3 shot Nam ep008): edit từ frame v1 + ref mặt v002 + ref body v003, giữ nguyên phòng/váy/tư thế, mặt theo đúng ảnh chuẩn, dáng cao/gầy ~169cm. File `input/frames/sh010-frame-v2.jpg` (sha 24c74ae7…, từ media-generation-sh010-frame-v2-0-fa4b162a…). Nit tự soi: vòng cổ mảnh ở v1 không còn trong v2; lọ tulip trên bàn trà cũng không còn; không chữ/logo/sao Gemini. CHỜ Richard duyệt ảnh rồi mới gen take003 — KHÔNG gen trước.

## 2026-11-26 19:16 — Richard DUYỆT frame sh010 v2, lệnh gen take003
- Richard bấm "Duyệt frame v2, gen take003 luôn" → frame v2 (pipeline, sha 24c74ae7…) CHỐT làm first_frame sh010, thay v1; flow_image_asset_id → null (frame pipeline, upload lúc gen như sh020 v2). Asset huynhdn cũ 568a427c chỉ còn là lịch sử.
- Credit trước gen: 40cr. take003 tốn 10cr → còn 30cr; 4 clip còn lại sau đó (sh020t2, sh040t2, sh050, sh060) cần 40cr — THIẾU 10 so với số dư sau take003, phải chờ reset 09:32 3/12 hoặc bỏ 1 clip. Đã báo Richard từ 18:38.

## 2026-11-26 19:17–19:23 — sh010 take003 (frame v2 đã duyệt): GEN XONG, needs_review
- Phiên browser MỚI (phiên cũ bị flag unusual activity) — vào project tinphim 7ac61787 bình thường, Frames-direct, upload frame v2, Veo 3.1 Lite 10cr, 1 lần nộp, KHÔNG bị chặn. Clip 617855ff, 7.93s, 720x1280, sha be80a090…, tải 1K về đĩa. Số dư tinphim: 30cr.
- QC: Whisper base đủ 8 từ 4.24-6.16s, "thấy" nghe ĐÚNG (take002 nghe "thế"); từ đầu smeared ("ăn" thay "Anh", artifact onset — RMS im đến ~4.2s); 1 burst duy nhất, không lặp; F0 ~260Hz nữ. LƯU Ý: thoại bắt đầu MUỘN (~4.2s), nửa đầu clip chỉ xoay người không lời. Hình: váy hồng rõ, phòng khách khớp, dáng cao/gầy; watermark Veo góc phải dưới. faster-whisper lại mất sau VM restart (lần 4 trong ngày) — cài lại bằng pip --break-system-packages --ignore-installed; QC vẫn dùng script decode wav bằng ffmpeg + module wave (tránh av 19/scipy gãy).
- Trạng thái: needs_review — chờ Richard xem mặt/dáng + nghe giọng Bắc + chốt vụ thoại muộn.
- Credit: còn 30cr; 4 clip còn lại (sh020t2, sh040t2, sh050, sh060) cần 40cr — THIẾU 10, phải chờ reset 09:32 3/12 (hoặc bỏ 1 clip). Đã báo Richard từ 18:38.

## 2026-11-26 19:57 — Richard xem take003: "Mặt cảm giác vẫn không giống lắm" → REJECT (mặt)
- take003 → rejected_editorial. Đây là take sh010 thứ 3 liên tiếp trượt vì mặt (take001: mặt tròn/rộng hơn; take002: không giống chút nào; take003: vẫn không giống lắm) — mặt Veo gen ra từ cùng 1 frame v2 đã duyệt vẫn drift khác nhau mỗi lần, không ổn định.
- Số dư tinphim: 30cr. Chờ Richard chọn hướng: gen lại take004 từ frame v2 (10cr, hên xui mặt) / làm frame mới / tạm để sh010 lại, làm các shot khác trước (sh020t2, sh040t2, sh050, sh060 cần 40cr — đã thiếu 10 so với 30cr hiện có).

## 2026-11-26 20:00 — Frame sh010 v3 (mặt thẳng) làm xong, chờ Richard duyệt
- Richard lệnh 19:59: gen lại ảnh, ảnh trước nghiêng mặt, lần này thẳng mặt. Làm bằng pipeline (Flow image edit đang bị flag unusual activity): sửa từ frame v1, ref mặt v002 + body v003, giữ phòng khách/váy hồng/tư thế xoay — mặt THẲNG nhìn vào camera, cười, dáng cao gầy. Bình tulip + dây chuyền vàng có lại như v1; không chữ/logo/sao Gemini.
- Chưa map vào episode.yaml — chờ Richard duyệt ảnh TRƯỚC rồi mới gen take004 (luật 18:39).

## 2026-11-26 20:06 — Richard DUYỆT frame sh010 v3 (mặt thẳng), lệnh gen take004
- Frame v3 (pipeline, sha 88b40f5b…, 1168×2112) CHỐT làm first_frame sh010, thay v2; flow_image_asset_id vẫn null (frame pipeline, upload lúc gen). Credit trước gen: 30cr → take004 tốn 10cr, còn 20cr; 4 clip còn lại sau đó cần 40cr — thiếu 20, chờ reset 09:32 3/12 (đã báo Richard từ 18:38, nhắc lại lúc 19:57).

## 2026-11-26 20:07–20:13 — sh010 take004 (frame v3 mặt thẳng): GEN XONG, needs_review
- Phiên browser mới, vào project tinphim 7ac61787 bình thường (lần này browser tự vào acc qua chooser, KHÔNG cần Richard gõ pass — không rõ vault password đã đúng hay session cũ còn hạn; KHÔNG kết luận mật khẩu vault đã đúng, vẫn không tự thử lại khi cần đăng nhập mới). Frames-direct, upload frame v3, Veo 3.1 Lite 10cr, 1 lần nộp, KHÔNG bị chặn. Clip 380c71b4, 7.93s, 720x1280, sha 762e5773…, tải 1K về đĩa. Số dư tinphim: 20cr.
- QC: Whisper base đủ 8 từ 0.80-2.64s, "Anh" + "thấy" nghe ĐÚNG; từ thứ 3 mờ: Whisper nghe "dưới", ASR trình duyệt nghe "trước" (prompt "giúp") — cần tai Richard. Thoại SỚM (0.8s), 1 burst duy nhất, không lặp; F0 ~254Hz nữ. Hình: váy hồng rõ, phòng khách khớp, dáng cao/gầy; frame 5s quay 3/4 nhìn về camera cười; watermark Veo góc phải dưới. faster-whisper lại mất sau VM restart (lần 5 trong ngày) — cài lại pip; QC vẫn dùng script decode wav bằng ffmpeg + module wave.
- Trạng thái: needs_review — chờ Richard xem mặt/dáng + nghe giọng Bắc + nghe rõ từ "giúp".
- Credit: còn 20cr; 4 clip còn lại (sh020t2, sh040t2, sh050, sh060) cần 40cr — THIẾU 20, chờ reset 09:32 3/12 (hoặc bỏ 2 clip). Đã báo Richard từ 18:38, nhắc lại 19:57.

## 2026-11-26 20:19 — Richard CHỐT take004 ("ok đó") + lệnh lồng giọng clone ThaoMy
- take004 → accepted_editorial (mặt/dáng OK). Giọng Veo phải lồng lại bằng clone ThaoMy ("lồng ThaoMy ấy") — tắt tiếng Veo, dub wordalign bằng VieNeu v3 Turbo clone ThaoMyVeo (theo skill ai_sitcom_dubbing + precedent ep011/ep012).
- Dub làm riêng từng shot, trình video đã lồng cho Richard duyệt trước khi dựng master.

## 2026-11-26 20:19–20:28 — sh010 take004: CHỐT + lồng giọng clone ThaoMy XONG, chờ Richard nghe
- Richard: "ok đó" → take004 accepted_editorial; "giọng thì phải lồng rồi" + "lồng ThaoMy ấy" → dub clone ThaoMyVeo, tắt tiếng Veo.
- TTS: VieNeu v3 Turbo trên Colab T4 (session ep013-dub, script ep013_dub_thaomy_sh010.py, enroll ref-clip2.wav), wav 2.96s 48kHz mono → `~/workspace/colab-t4-test/ep013-dub/thaomy-ep013-sh010.wav`. Session đã stop, không còn session active. Whisper trên wav clone gốc: "Anh sẽ giúp em bộ này. Thế sao?" (8 từ; "xem"→"sẽ", "thấy"→"thế" là nhầm của Whisper — tai Richard quyết).
- Build wordalign (`edit/build_wordalign_sh010.py`): cửa sổ native đo bằng energy 48kHz stereo 0.05s — 2 burst tách bởi khoảng lặng 2.20s (dấu phẩy): P1 0.85-2.15, P2 2.25-2.75. A/B test: bản stretch (atempo 1.108/1.04, cửa sổ chặt) Whisper nghe sai 4 từ; bản NO-STRETCH (atempo 1.0, cửa sổ mở rộng P1 0.80-2.24 / P2 2.25-2.77) Whisper nghe đúng 7/8 từ ("xem" + "thấy sao?" đúng, chỉ "giúp"→"xúc" nhầm đồng âm) → GIỮ bản no-stretch. Peak 0.552, năng lượng ngoài cửa sổ = 0.0 (không rò tiếng gốc).
- Output: `generated/sh010-take004-dubbed.mp4` (sha c2289096…), 7.93s, 720x1280, audio mono 48kHz AAC 192k. QC chi tiết: `edit/dub-qc-ep013-sh010.md`. Chờ Richard nghe chốt bản lồng trước khi dựng master.

## 2026-11-26 20:31 — Richard nghe bản lồng sh010: "ok, chấp nhận đc" → DUB ACCEPTED, sh010 HOÀN THÀNH
- take004 (accepted_editorial) + dub clone ThaoMy (no-stretch wordalign, sha c2289096…) đã được Richard chốt. sh010 xong — không gen/lồng thêm cho shot này.
- Còn lại 4 clip: sh020 take002, sh040 take002, sh050 take001, sh060 take001 = 40cr; số dư tinphim 20cr → chỉ làm được 2 clip, 2 clip còn lại chờ reset 09:32 3/12. Mỗi clip vẫn theo luật 18:39: gửi ảnh frame duyệt trước khi gen.

## 2026-11-26 20:37–20:42 — sh020 take002: GEN LỖI, không có clip (không tốn credit)
- Richard duyệt frame sh020 v2 (20:37), gen take002 từ ảnh đó, Frames-direct, Veo 3.1 Lite. Flow báo lỗi: "Không thành công — Không tạo được âm thanh. Vui lòng thử một câu lệnh khác hoặc gửi ý kiến phản hồi." Không có clip, không có clip ID, không tải file. Browser không bấm Retry (theo lệnh dừng).
- Số dư tinphim: vẫn 20cr (Flow nói sẽ hoàn credit, "có thể mất vài phút" — lần này chưa thấy trừ, cần kiểm tra lại số dư ở lần gen sau).
- ĐIỂM ĐÁNG CHÚ Ý: sh020 take001 CÂM hoàn toàn (không có audio stream), take002 lỗi "không tạo được âm thanh" — shot này lỗi âm thanh 2 lần liên tiếp. Câu thoại chỉ có 2 từ "Dễ thương!" — có thể Veo khó tạo audio với câu quá ngắn, hoặc lỗi nhất thời. Flow gợi ý thử câu lệnh khác (đổi prompt, không đổi thoại) hoặc gen video không tiếng rồi lồng sau.
- Chờ Richard chọn: thử lại prompt sửa nhẹ / thử lại y nguyên sau / để sh020 lại làm shot khác trước.

## 2026-11-27 01:02 — Richard đổi thoại sh020: "Dễ thương!" → "Đáng yêu", gen lại take002
- Sau 2 lần lỗi âm thanh với câu "Dễ thương!" (take001 câm, take002 lỗi "không tạo được âm thanh"), Richard đổi câu sh020 thành "Đáng yêu". Cập nhật: episode.yaml dialogue + input/prompts/sh020-motion.txt (sha mới) + script.md hàng sh020 + ghi chú thay đổi (sh040/sh060 vẫn "dễ thương", chờ Richard chốt có đổi theo không).
- Gen lại take002 từ frame v2 đã duyệt, câu mới "Đáng yêu", Veo 3.1 Lite 10cr. Số dư tinphim: 20cr.

## 2026-11-27 01:03–01:09 — sh020 take002 retry với câu "Đáng yêu": LỖI LẠI, vẫn "không tạo được âm thanh"
- Gen lại 1 lần, câu mới "Đáng yêu", còn lại y nguyên (frame v2, Veo 3.1 Lite). Flow lại báo đúng lỗi cũ: "Không tạo được âm thanh. Vui lòng thử một câu lệnh khác hoặc gửi ý kiến phản hồi." Không có clip. Browser không bấm Retry.
- KẾT LUẬN: đổi câu thoại KHÔNG sửa được lỗi — nguyên nhân không phải chữ "Dễ thương!". Shot sh020 lỗi âm thanh 3 lần liên tiếp (take001 câm, take002 lần 1 + lần 2 lỗi audio). Nghi: Veo khó tạo audio cho shot này (nam cười khoái + câu ngắn?), hoặc lỗi nhất thời của Flow. Số dư: vẫn 20cr (không bị trừ / hoàn đã về).
- Hướng còn lại: (a) gen video KHÔNG tiếng rồi lồng sau — nhưng Nam chưa có giọng clone (chỉ có clone ThaoMy nữ + BangTake2 cho Bằng; lồng Nam bằng giọng TTS nam khác sẽ lệch giọng các shot Nam còn lại); (b) thử lại sau; (c) sửa prompt (bỏ cười khoái / đổi hướng giọng); (d) để sh020 lại làm shot khác trước. Chờ Richard chọn.

## 2026-11-27 06:39 — Richard chọn "thử lại sh020 với prompt sửa nhẹ"
- Sửa nhẹ motion prompt (thoại vẫn "Đáng yêu", frame v2 giữ nguyên): "cười khoái" → "mỉm cười vui vẻ", "Nam nói:" → "Nam nói rõ ràng:" — giả thuyết: cười khoái khiến Veo cố tạo tiếng cười thay vì thoại rõ, nên audio lỗi. Giữ nguyên cảnh, giọng nam hào hứng, camera tĩnh, không nhạc.
- Gen lại take002 (lần thử thứ 3 cho shot này, lần 1 với prompt sửa), Veo 3.1 Lite 10cr. Số dư tinphim: 20cr.

## 2026-11-27 06:39–06:46 — sh020 take002 retry prompt sửa: LỖI LẠI "không tạo được âm thanh"
- Phiên browser bị đăng xuất (06:40), Richard đăng nhập lại tinphim (06:42 "xong"), gen tiếp với prompt sửa (mỉm cười, nói rõ ràng, câu "Đáng yêu"). Kết quả: vẫn lỗi đúng "Không tạo được âm thanh", không có clip, không tốn credit (còn 20cr).
- KẾT LUẬN: sửa prompt cũng KHÔNG sửa được. Shot sh020 lỗi âm thanh 4 lần liên tiếp (take001 câm + take002 lỗi audio ×3, qua 2 câu thoại khác nhau và 2 prompt khác nhau). Khả năng cao vấn đề nằm ở shot/frame/giọng nam, không phải chữ hay hành động. Hướng còn lại: (a) gen video KHÔNG tiếng rồi lồng sau — Nam chưa có giọng clone, nhưng có thể clone từ audio gốc của sh040 take001 (Nam nói thật, dù bị lặp câu 2 lần — lấy 1 lần làm mẫu); (b) thử lại sau; (c) để sh020 lại làm shot khác trước. Chờ Richard chọn.

## 2026-11-27 06:55–07:00 — sh020 take002 gen KHÔNG tiếng: Flow chặn "unusual activity", không có clip
- Gen câm (prompt không thoại, không hướng giọng; Flow không có nút tắt audio riêng) — sau ~90s Flow báo lỗi: "Chúng tôi nhận thấy có hoạt động bất thường nào đó..." (unusual activity). Không có clip, không tốn credit (còn 20cr). Browser không bấm Retry.
- Đây là lần hỏng thứ 5 của sh020 (take001 câm + take002 lỗi audio ×3 + gen câm bị chặn unusual activity). Lần chặn này khác 4 lần trước: không phải lỗi audio mà là Flow nghi session tự động vì gen dồn dập (2 lần gen trong ~15 phút, 06:46 và 06:55). Tiền lệ ep013 ngày 26/11: sau chặn unusual activity thì nghỉ 5 phút + gen cách nhau thì chạy được.
- Chờ Richard chọn: nghỉ một lúc rồi thử lại gen câm / để sh020 lại làm sh050 trước / Richard tự bấm gen trên trình duyệt của mình.

## 2026-11-27 07:23–07:27 — Thử lại gen câm sau nghỉ 23 phút: LỖI LẠI "không tạo được âm thanh"
- Gen câm lần 2 (prompt không thoại, không hướng giọng) — Flow vẫn báo đúng lỗi cũ "Không tạo được âm thanh" sau ~1 phút, dù prompt không hề yêu cầu âm thanh. Không có clip, không tốn credit (còn 20cr).
- PHÁT HIỆN QUAN TRỌNG: lỗi audio KHÔNG liên quan tới thoại/prompt — Veo vẫn cố tạo audio cho shot này dù prompt không có thoại, và cứ lỗi. Shot sh020 hỏng 6 lần liên tiếp (take001 câm + take002 lỗi audio ×3 + gen câm bị chặn unusual activity ×1 + gen câm lỗi audio ×1).
- MANH MỐI MỚI: thông báo lỗi của Flow ghi "Bạn có thể cập nhật chế độ cài đặt để tạo video không có âm thanh" + link tới cài đặt — có vẻ Flow CÓ nút tắt tiếng thật trong phần cài đặt (trình duyệt chưa tìm thấy trong panel đã mở). Lần thử sau nên tìm và bật nút tắt tiếng đó thay vì chỉ ghi trong prompt.
- Chờ Richard chọn: thử lại với nút tắt tiếng trong cài đặt / để sh020 lại làm sh050 trước.

## 2026-11-27 08:17–08:22 — Thử giả thuyết của Richard: tạo nhân vật Nam rồi gen — nhân vật TẠO ĐƯỢC, gen VẪN LỖI audio
- Bước 1 THÀNH CÔNG: tạo nhân vật "Nam" từ ảnh sh020-frame-v2.jpg trong project tinphim, không bị chặn (ảnh AI, không phải ảnh người thật). Character ID 8608fd89-6ce9-4519-80c2-e65e14f9c547, URL https://flow.google.com/project/7ac61787-27b9-4022-ac91-fe3f15d02414/character/8608fd89-6ce9-4519-80c2-e65e14f9c547. Chân dung: Nam áo phông trắng, ngồi ghế bành gần cửa gỗ, mỉm cười — khớp frame. Nhân vật này giữ lại trong project, dùng được cho các shot Nam sau (sh040/sh060).
- Bước 2 THẤT BẠI: gen 1 clip với nhân vật Nam + frame v2 làm ingredients, Veo 3.1 Lite, prompt "Đáng yêu" — sau ~2 phút vẫn lỗi đúng "Không tạo được âm thanh". Không có clip, không tốn credit (còn 20cr).
- KẾT LUẬN: giả thuyết "thiếu nhân vật" KHÔNG đúng — lỗi audio tái hiện cả khi đã có nhân vật. Shot sh020 hỏng 7 lần liên tiếp. Hướng còn: (a) thử nút tắt tiếng thật trong cài đặt (manh mối từ thông báo lỗi Flow); (b) để sh020 lại làm sh050 trước; (c) thử lại sau.

## 2026-11-27 08:27 — Richard: đổi thoại sh020 VỀ LẠI "Dễ thương!", gen lại luôn với nhân vật Nam
- Lý do: đổi sang "Đáng yêu" không sửa được lỗi audio; lần gen với nhân vật Nam dùng câu "Đáng yêu" vẫn lỗi — tổ hợp chưa thử là nhân vật Nam + câu gốc "Dễ thương!". Không đi hướng tắt tiếng nữa.
- Cập nhật: episode.yaml dialogue → "Dễ thương!", input/prompts/sh020-motion.txt (giữ "mỉm cười vui vẻ, nói rõ ràng", chỉ đổi lại câu thoại), script.md hàng sh020 + ghi chú. Running gag 3 lần "dễ thương" khôi phục.
- Gen lại take002 với nhân vật Nam (8608fd89) + frame v2, Veo 3.1 Lite 10cr. Số dư tinphim: 20cr.

## 2026-11-27 08:28–08:31 — Gen lại nhân vật Nam + câu gốc "Dễ thương!": VẪN LỖI audio
- Tổ hợp chưa thử cuối cùng (nhân vật Nam + câu gốc) cũng lỗi đúng "Không tạo được âm thanh" sau ~2 phút. Không dùng hướng tắt tiếng (theo lệnh Richard). Không có clip.
- Shot sh020 hỏng 8 lần liên tiếp. Đã thử đủ ma trận: Frames-direct × 2 câu thoại × cười/mỉm cười; gen câm (prompt không thoại) ×2; nhân vật Nam + 2 câu thoại — tất cả đều lỗi audio (trừ 1 lần chặn unusual activity). Kết luận: lỗi không nằm ở thoại, prompt, nhân vật hay chế độ gen — có thể nằm ở chính frame v2 (Nam cười há miệng?) hoặc lỗi nhất thời của Flow với shot này.
- LƯU Ý SỐ DƯ: panel tài khoản hiện 50 credit (lúc bắt đầu lần này là 20) — không rõ lý do (có thể hoàn credit các lần lỗi dồn về, hoặc reset ngày mới); CẦN kiểm tra lại số dư ở lần gen sau trước khi tính toán. Nếu thật sự 50 thì đủ làm cả 4 clip còn lại (40cr).
- Chờ Richard chọn: làm frame mới cho sh020 (biểu cảm miệng khép, không cười há miệng) / để sh020 lại làm sh050 trước / thử lại sau.

## 2026-11-27 08:32 — Frame sh020 v3 (miệng khép) làm xong, đã trình Richard duyệt
- Richard chọn làm frame mới miệng khép (giả thuyết: frame v2 Nam cười há miệng làm Veo kẹt audio). Frame v3 làm bằng media pipeline, sửa từ v2: giữ nguyên người, áo trắng, ghế bành, cửa gỗ, tủ giày, góc máy, ánh sáng; chỉ đổi miệng thành khép, cười mỉm môi khép. File input/frames/sh020-frame-v3.jpg, 1184×2096, sha256 17423ea7ed440eb05e996b8a780d75a776664fec0bd6e14532ea8f9cd481ed7a.
- CHƯA ghi vào episode.yaml — chờ Richard duyệt ảnh trước rồi mới map + gen (luật 18:39).

## 2026-11-27 08:52 — Richard DUYỆT frame sh020 v3, gen take002 luôn
- Frame v3 (miệng khép, sha 17423ea7) đã map làm first_frame của sh020 trong episode.yaml (flow_image_asset_id null — frame pipeline, không phải asset Flow). Gen take002 từ frame v3 + nhân vật Nam (8608fd89), Veo 3.1 Lite, câu "Dễ thương!".

## 2026-11-27 08:53–09:00 — Gen take002 từ frame v3 + nhân vật Nam: VẪN LỖI audio
- Frame v3 (miệng khép) đã upload vào project, gen với nhân vật Nam + frame v3, Veo 3.1 Lite, câu "Dễ thương!" — sau ~2 phút vẫn lỗi đúng "Không tạo được âm thanh". Không có clip.
- KẾT LUẬN: miệng há cũng không phải nguyên nhân. Shot sh020 hỏng 9 lần liên tiếp. Số dư XÁC NHẬN 50 credit (trước gen 50, sau gen 50 — lần lỗi không bị trừ).
- Chi tiết kỹ thuật đáng ghi: khi đính frame trước, picker của Flow ẨN nhân vật Nam (tab Characters báo "No ingredients found", tìm "Nam" không ra); bỏ frame ra thì nhân vật hiện lại — phải đính nhân vật TRƯỚC rồi mới đính frame thì cả 2 mới cùng vào. (Quy tắc 1 reference mang mặt/lần — entity + portrait cùng lúc có thể xung đột.)
- Tổ hợp CHƯA thử: Frames-direct với frame v3 (không nhân vật) — mọi lần gen v3 đều qua Ingredients + nhân vật. Chờ Richard chọn: thử Frames-direct v3 / để sh020 lại làm sh050 trước / thử lại sau.

## 2026-11-27 09:10–09:13 — Frames-direct frame v3 (không nhân vật): VẪN LỖI audio — ma trận đã thử hết
- Tổ hợp cuối cùng chưa thử (Frames-direct + frame v3 miệng khép, không nhân vật, câu "Dễ thương!") cũng lỗi đúng "Không tạo được âm thanh" sau ~2 phút. Không có clip, số dư vẫn 50cr.
- Shot sh020 hỏng 10 lần liên tiếp. Ma trận ĐÃ THỬ HẾT: Frames-direct v2 × 2 câu; gen câm ×2; Ingredients + nhân vật Nam × v2/v3 × 2 câu; Frames-direct v3. Chế độ, frame, câu thoại, nhân vật — đổi hết vẫn lỗi y hệt. Kết luận: nguyên nhân không nằm trong các biến đã thử — có thể là lỗi nhất thời phía Flow với shot này, hoặc điều gì đó trong nội dung shot mà Veo không nói ra.
- Đề xuất: DỪNG thử sh020, làm sh050 trước — vừa tiến tập, vừa chẩn đoán: nếu sh050 gen có tiếng bình thường thì lỗi chỉ riêng sh020; nếu sh050 cũng lỗi audio thì vấn đề ở acc/Flow. Chờ Richard chọn.

## 2026-11-27 13:52 — Richard DUYỆT frame sh050 v1, gen take001 luôn
- Frame v1 đã map sẵn trong episode.yaml (sha 856b2361, flow asset 713a3c42), frame_status approved — không cần sửa yaml. Gen take001 Frames-direct từ frame v1, Veo 3.1 Lite, câu "Còn bộ cuối này thì sao? Anh chỉ biết nói mỗi dễ thương thôi hả?". Đây cũng là phép chẩn đoán: nếu sh050 có tiếng bình thường thì lỗi audio chỉ riêng sh020; nếu cũng lỗi thì vấn đề ở acc/Flow.

## 2026-11-27 13:52–14:04 — sh050 take001 THÀNH CÔNG, có tiếng (gen 1 lần)
- Frame v1 Richard duyệt 13:52. Cửa sổ mới chưa đăng nhập — Richard tự đăng nhập 13:56, tiếp tục gen; lần tiếp tục đầu chết giữa chừng (task slot missing, chưa gen, 0cr), mở cửa sổ mới thì lại chưa đăng nhập — Richard đăng nhập lại 13:59, gen 14:04 thành công ngay lần đầu.
- Clip f175fd88, 7.93s, 720x1280, AAC, sha c963afde. Whisper base nghe đúng cả 2 câu thoại. Số dư 50→40cr.
- CHẨN ĐOÁN QUAN TRỌNG: sh050 gen có tiếng bình thường → lỗi audio của sh020 là riêng shot sh020, KHÔNG phải acc/Flow.
- LƯU Ý: frame sh050 v1 KHÔNG có sẵn trong project dù yaml ghi flow_image_asset_id 713a3c42 — trình duyệt phải upload lại file. Asset ID đã ghi có thể không trỏ đúng asset trong project này; lần sau kiểm tra lại khi dùng.

## 2026-11-27 14:12 — sh050 take001 REJECTED (mặt lúc nói không giống ThaoMy)
- Richard xem video: "Mặt tự nhiên thấy lúc nói không giống nhỉ" / "ko giống ThaoMy" — mặt drift khi nói, giống lỗi sh010 take001–003. Thoại + tiếng vẫn đúng (Whisper đã verify). Gen lại take002 từ cùng frame v1 đã duyệt.

## 2026-11-27 14:12–14:15 — sh050 take002 gen xong (re-roll từ frame v1)
- Clip 235a3da1, 7.93s, 720x1280, AAC, sha 8e0d39e5. Whisper base nghe đúng cả 2 câu. Số dư 40→30cr. Chờ Richard duyệt mặt.

## 2026-11-27 14:21 — sh050 take002 REJECTED (mặt không giống ThaoMy tí nào)
- Richard: "đéo giống tí nào". Cả 2 take sh050 đều drift mặt lúc nói (take001 cũng reject vì mặt). Gen lại take003 từ cùng frame v1 — giống sh010 trước đây phải tới take004 mới giữ mặt.

## 2026-11-27 14:22–14:25 — sh050 take003 gen xong (re-roll từ frame v1)
- Clip 0f521d57, 7.93s, 720x1280, AAC, sha d0ed609f. Whisper base nghe đúng cả 2 câu ("thôi" đúng — ASR trình duyệt nghe nhầm thành "rồi"). Số dư 30→20cr. Chờ Richard duyệt mặt.

## 2026-11-27 14:29 — sh050 take003 ACCEPTED (cắt 2s cuối)
- Richard: "Cắt 2 giây cuối thì ok". Đã cắt đuôi: file gốc 7.93s → 6.04s (cắt ở keyframe gần nhất, ~1.9s), sha mới a328699f. Whisper trên bản đã cắt vẫn nghe đủ cả 2 câu (0.00-2.00s + 2.00-5.00s). Take003 = take chốt của sh050.

## 2026-11-27 14:32 — Richard DUYỆT frame sh040 v1, gen take002 luôn
- Frame v1 đã map sẵn trong episode.yaml (sha 1e5f32f7, flow asset d7cf4553), frame_status approved — không cần sửa yaml. Gen take002 Frames-direct từ frame v1, Veo 3.1 Lite, câu "Ừm... dễ thương!" (take001 hỏng vì Veo nói câu 2 lần).

## 2026-11-27 14:32 — sh050 take003 cắt thêm 1s cuối (theo Richard)
- Richard: "cái này cắt thêm 1 giây cuối nữa". Đã cắt: 6.04s → 5.17s (cắt ~0.87s, giới hạn packet). Đo energy envelope trước khi cắt: tiếng nói hết khoảng 5.05–5.1s nên cắt tới 5.17s vẫn giữ nguyên thoại — Whisper trên bản đã cắt vẫn nghe đủ cả 2 câu. Sha mới f5c8bfa3. Take003 chốt của sh050.

## 2026-11-27 14:32–14:39 — sh040 take002 gen xong (re-roll từ frame v1)
- Frame sh040 v1 KHÔNG có sẵn trong project dù yaml ghi asset d7cf4553 (giống vụ sh050) — phải cấp file cho trình duyệt upload lại. Gen 1 lần thành công, clip 4538e5a7, 7.93s, 720x1280, AAC, sha b0a508ec. Số dư 20→10cr.
- QC: Whisper base word-timestamps — câu "Ừ, dễ thương" nói ĐÚNG 1 LẦN (0.00–1.16s). Energy envelope: 1 burst thoại 0.0–1.2s + 1 burst ngắn không lời 4.7–4.9s (~0.3s, Whisper không dịch được — có thể là cười trừ/hơi thở, khớp prompt "cười trừ"). KHÔNG phải lỗi nói 2 lần như take001. ASR trình duyệt nghe loạn xạ 4 lần khác nhau — không đáng tin, đã bỏ qua. Chờ Richard duyệt (mặt + giọng Nam).

## 2026-11-27 14:40 — Richard DUYỆT sh040 take002
- Take002 chốt của sh040 (câu nói đúng 1 lần, Whisper + energy envelope đã kiểm). Status accepted_editorial, commit. Số dư 10cr — chỉ đủ 1 clip nữa trước reset 09:32 3/12; còn lại sh020 take002 + sh060 take001 (cần 20cr).

## 2026-11-27 14:41 — Richard DUYỆT frame sh060 v1, gen take001 luôn
- Frame v1 đã map sẵn trong episode.yaml (sha f6fa85da). Gen take001 Frames-direct từ frame v1, Veo 3.1 Lite, câu "...phối kiểu... dễ thương." Đây là clip cuối với số dư 10cr — sau đó sh020 take002 chờ reset 09:32 3/12.
