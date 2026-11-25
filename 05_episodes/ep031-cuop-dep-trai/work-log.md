# Work log — ep031 Cướp Đẹp Trai

## 2026-11-25 20:27 — Richard gửi link Facebook, "update kịch bản ... thêm kịch bản này"

- Link: https://www.facebook.com/share/r/1Ctg73UQ9Q/?mibextid=wwXIfr → reel https://www.facebook.com/reel/1655734339670095 (Táo Đen Shop, verified, caption "POV: Bị cướp nhưng cướp đẹp trai cao 1m8 😭", ~53s ước chừng, 13,6K reactions / 101 comment / 97 share lúc xem 25/11).
- Facebook connector chưa kết nối nên không decode được bằng facebook-cli (lỗi "not connected"); mở bằng trình duyệt cloud, không cần đăng nhập, không post/like/comment/share/download gì. Tóm tắt nguồn lưu tại `input/references/source-facebook.md`.
- Transcript gốc KHÔNG chắc từng chữ: reel không có phụ đề, thoại nhanh + chồng lấn + ồn đường phố, trình duyệt nghe lại nhiều lần vẫn đánh dấu nhiều câu "wording uncertain" (nhất là đoạn giữa đưa đồ). Draft không chép nguyên văn — chỉ giữ cấu trúc + ý thoại, viết lại hoàn toàn sang giọng Bắc.

## 2026-11-25 20:35 — Viết draft ep031, 6 shot × 8s = 48s

- Viết `script.md` draft: chuyển thể cấu trúc gốc (hỏi lịch sự → có người yêu chưa → khen trai cao 1m8 → đưa điện thoại + chìa khóa xe → chốt "Còn em nữa, anh lấy em đi!"), giữ nguyên ý thoại gốc, viết lại theo giọng Bắc Thảo My.
- `episode.yaml` draft: 6 shot, chưa prompt, chưa frame, `approved_for_generation: false` tất cả, `editorial_status: draft`.
- `wardrobe.md` draft: My áo thun xanh nhạt ôm + chân váy sáng màu theo reel gốc, móng đỏ đậm (khác chuẩn móng tự nhiên — cần Richard chốt); đạo cụ túi hồng + iPhone + chìa khóa xe; location đường phố ban ngày là mới, chưa có master.
- `edit/manifest.yaml`: placeholder copy theo ep013 (chưa tới bước dựng) — tới bước edit sẽ rebuild theo plan giọng trong script (My native-nếu-Bắc không thì clone ThaoMy, cướp sh030 giữ native).
- Số tập: ep026–ep028 đã giữ cho 3 draft Ghost (script-only, chưa lưu repo); ep029, ep030 đã có trong repo nên tập mới là ep031.
- Chàng trai CHƯA CHỐT lúc draft: đề xuất A giữ POV không mặt (khuyến nghị — không cần khóa mặt nam mới, đúng góc reel gốc); phương án B dùng Nam ep008 làm cướp (lệch continuity, chỉ khi Richard muốn thấy mặt). Chờ Richard chọn.
- Chưa làm gì thêm: chưa duyệt kịch bản, chưa làm frame, chưa gen clip, chưa commit repo.

## 2026-11-25 20:38 — Richard DUYỆT kịch bản, CHỐT cướp POV không mặt

- Richard gật widget "Duyệt draft, giữ POV không mặt".
- Cập nhật hồ sơ: `script.md` trạng thái → kịch bản đã duyệt 25/11, chàng trai chốt POV không lộ mặt (phương án B dùng Nam ep008 đã bỏ); `episode.yaml` editorial_status `draft` → `script_approved`; `wardrobe.md` cập nhật theo (không cần mặt/trang phục nam).
- Trang phục My (áo thun xanh nhạt + chân váy sáng, móng đỏ đậm theo reel gốc) + bối cảnh đường phố lấy theo đề xuất trong draft đã duyệt — đổi được trước khi làm frame nếu Richard nói.
- Đối chiếu script ↔ episode.yaml (profile check): 6 shot, thoại khớp từng chữ, số tiếng đếm tay 14/6/1/13/14/7, mỗi shot đúng 1 câu, đều trong ngân sách 8s. Không có prompt ảnh/motion hay manifest âm thanh để đối chiếu (chưa tới bước đó). Validator đạt (exit 0; chỉ note thiếu frame 6/6 shot + voice pending — đúng trạng thái draft đã duyệt, như ep013/ep029).
- Lưu hồ sơ vào repo: commit riêng scope ep031, chạy validator trước, push lên main.
- Bước tiếp theo: làm 6 frame (project Flow riêng `CNTM · EP031 · Cướp Đẹp Trai`, 0 credit) — cần ảnh nền đường phố ban ngày đồng bộ 6 shot (location mới, chưa có master) + tay cướp POV vào khung từ mép/trên cao. CHỜ Richard gật làm frame — không tự gen, vì ep012 master r05 vẫn đang làm dở ở chat khác và quy tắc không chạy 2 task Flow song song.

## 2026-11-25 20:39 — Richard thêm 2 điểm sau khi duyệt: ốp iPhone + áo dài

- "còn điểm nữa là ốp iphone như mọi khi nhé, sản phẩm ấy" → điện thoại My là iPhone trong ốp lưng trong suốt MagSafe Slimcase aff-0003 (https://s.shopee.vn/AKcGpsTOV8, active, đích đã xác minh 19/11) như ep006/ep009. Ảnh sản phẩm 02 đã copy vào `input/references/slimcase-phone-ref.jpg` (sha `e492d33a…`, byte-identical với `04_products/prd-0003/`, đúng ảnh ep009 đã dùng). Khi làm frame: dùng ảnh này làm ref ốp + ghi dòng ốp Slimcase vào image prompt từng shot như ep009. Link ốp gắn bằng comment Page sau khi đăng (mẫu ep009 plc-0011), không vào mô tả.
- "áo dài nữa" → My mặc áo dài thay áo thun + chân váy của reel gốc. Tao chọn **Vân Linh xanh nhạt** (đã dùng ep008/ep011, có sẵn trong Flow project ep008 asset `9a824890`, lấy lại qua picker — không upload mới) vì đó là áo dài đã chứng minh trong Flow; Mai Linh đỏ đô (aff-0007, ep012) và Thanh Nghi hồng đậm là phương án đổi, đã ghi trong wardrobe.md để Richard đổi trước khi làm frame nếu muốn. Ảnh ref đã copy vào `input/references/aodai-van-linh-xoa-v3.jpg` (sha `2f71722d…`, đúng file ep008). Lưu ý: tay trái ảnh này cầm vật vàng — frame phải để tay trống.
- Cập nhật: `script.md` (trạng thái + trang phục My + đạo cụ + affiliate), `wardrobe.md` (áo dài Vân Linh + ốp Slimcase + cách gắn aff-0003). Thoại 6 shot KHÔNG đổi nên không cần duyệt lại thoại; đối chiếu lại script ↔ episode.yaml vẫn khớp (validator chạy lại trước commit).
- Commit lần này gộp cả duyệt draft 20:38 + 2 điểm thêm 20:39 (chưa commit riêng lúc duyệt vì 2 tin nhắn tới liền nhau) — xem commit message.

## 2026-11-25 20:42 — Richard "ok" = chốt móng đỏ đậm + gật làm frame

- Bee hỏi "móng đỏ đậm hay về tự nhiên?" + "bước tiếp theo là làm 6 frame, đang chờ mày gật"; Richard đáp "ok" → hiểu là: giữ móng đỏ đậm theo draft + bắt đầu làm 6 frame.
- Cập nhật: móng đỏ đậm CHỐT trong `script.md` + `wardrobe.md`.
- Kiểm tra trước khi giao frame: không có task Flow nào khác đang chạy (browser windows chỉ còn task Facebook reel đã completed) — ep012 ở chat khác đang làm master r05 local (dub + dựng), không phải task Flow, nên không vi phạm quy tắc không chạy 2 task Flow song song.
- Giao trình duyệt làm 6 frame (project Flow riêng `CNTM · EP031 · Cướp Đẹp Trai`, sửa ảnh Nano Banana 0 credit): mặt lấy lại ThaoMy002 qua picker (project EP003), áo dài Vân Linh xanh nhạt lấy lại qua picker từ project ep008 (asset `9a824890`), ốp Slimcase + mặt chuẩn local làm ref dự phòng, nền đường phố ban ngày đồng bộ 6 shot, tay cướp POV chỉ tay/cánh tay không mặt.

## 2026-11-25 20:45 — Task frame tạm dừng ở xác minh thiết bị Google

- Trình duyệt đăng nhập acc huynhdn.developer@gmail.com (email + mật khẩu đều được chấp nhận), Google hiện "Verify it's you" và gửi thông báo tới iPhone 13 Pro Max + iPhone 12 của Richard. Chưa tạo project, chưa làm frame nào.
- Cần Richard: mở thông báo Google trên iPhone, bấm "Yes", rồi bấm số **98** hiện trên trang đăng nhập. Xong báo tao để tao cho task chạy tiếp.

## 2026-11-25 21:23 — 6 frame v1 XONG, Bee QC đạt, chờ Richard duyệt frame

- Project Flow: `CNTM · EP031 · Cướp Đẹp Trai` — https://flow.google.com/project/77341ed7-c79a-47de-9d3d-7d29c311c25a (acc huynhdn Pro). Đăng nhập xong sau khi Richard xác minh iPhone (Yes + số 98). 0 credit video, chỉ sửa ảnh Nano Banana 2.1, mỗi frame 1 edit trực tiếp từ master, không nối tiếp.
- Tái dùng qua picker, không upload mới: mặt ThaoMy002 (character_id `801850a3-2913-47e0-8fba-6fadef05f045`, project EP003); áo dài Vân Linh từ project ep008 (asset `9a824890`). Ốp Slimcase upload 1 lần làm asset project, chỉ dùng cho sh050.
- Map take theo artifact ID (f1–f6) + Flow asset ID, kiểm chứng file trên disk bằng find + ffprobe (768×1376, đúng 9:16), không tin toast:

| Shot | Frame local | sha256 (đầu) | Flow asset ID |
|---|---|---|---|
| sh010 | sh010-frame-v1.jpg (PNG→JPG) | 7edc1df3… | 8f7d583a-20a3-4529-83c3-ab9ba2941ab0 |
| sh020 | sh020-frame-v1.jpg (PNG→JPG) | 9aa2e0d4… | ed060d72-4434-4971-9f46-114c87de1328 |
| sh030 | sh030-frame-v1.jpg (PNG→JPG) | 4b45541a… | 5f7273b6-ae30-4c12-b2a6-57bd94cbdc9b |
| sh040 | sh040-frame-v1.jpg | c191b2c7… | a48d6db5-106e-4d2f-bd21-fdc3e898b17c |
| sh050 | sh050-frame-v1.jpg | 5a046ee2… | 9ed9d4de-a798-46c0-8efb-d36840a4aa24 |
| sh060 | sh060-frame-v1.jpg | 5763b3f9… | 97b9f72f-52cc-4aaa-a5b8-d7c1ea1ed171 |

- Bee QC tự soi cả 6 ảnh, ĐẠT: mặt khớp master, áo dài Vân Linh xanh nhạt hoa chìm, túi hồng 1 cái, móng đỏ đậm, son đỏ, tay cướp chỉ tay/cánh tay không mặt (sh010 tay áo đen, sh030/sh060 tay trần từ trên cao, sh050 tay áo xám), phố HN ban ngày (cây, xe máy đậu, ô tô trắng, cửa hàng) đồng bộ. sh050 tốt nhất: vòng MagSafe trắng + 3 camera thấy rõ, chìa khóa xe treo ở túi hồng.
- Nits đã ghi (không chặn duyệt, Richard quyết): (1) sao Gemini nhỏ góc phải dưới mọi frame (như ep011); (2) nốt ruồi cằm trái nhỏ, không thấy rõ mọi frame (thấy mờ ở sh010); (3) sh040 có bóng người mờ xa gần cửa hàng, không thấy mặt; (4) ốp sh050 đọc hơi tối (màu máy) nhưng vòng MagSafe rõ; (5) góc phố hơi khác nhau giữa các shot (không có background master khóa cứng) nhưng cùng đoạn phố, cùng đạo cụ.
- Sự cố giữa chừng: sh050 Flow chặn 2 lần "unusual activity" (không tính phí); reload + chờ 5 phút thì hết, gen lại được. Bot-challenge agent test thêm 2 ảnh sh060 dự phòng (asset `89a88b67…`, `784d21f7…`) + 1 ảnh phone nữa trong project — KHÔNG dùng, không tải về, không ghi vào hồ sơ.
- `episode.yaml`: flow_project đã ghi, 6 shot `first_frame` + sha + `flow_image_asset_id`, `frame_status: pending_review`. Validator đạt (exit 0; chỉ note voice pending — đúng trạng thái).
- CHỜ: Richard duyệt 6 frame → gen 6 clip Veo 3.1 Lite (60 credit).
