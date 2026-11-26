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
