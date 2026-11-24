# ep009 — Giỏ hàng — Work log

## 2026-11-22 — Bee (Muse), sửa hồ sơ theo review kịch bản 22/11 (verdict CẦN SỬA)

- Người dùng duyệt các sửa trong review 06:30 22/11 (widget) + chốt trang phục chọn 1 trong 5 váy SANJOLI có sẵn trong Flow (chưa chọn màu cụ thể — xem dưới).
- Motion prompt (cả 4): xóa "Không phụ đề. Không chữ trên màn hình." — ghi tên chữ vào prompt Veo khiến Veo vẽ phụ đề giả nhiều hơn (luật đã chứng minh 14/11, 16/11).
- Image prompt: tuổi 25 → 26 (theo bible); "ánh sáng tự nhiên" → "Ánh sáng xanh lạnh từ màn hình điện thoại, phòng tối."; sh010 thêm đồng hồ 00:00, sh020 thêm đồng hồ 00:30 + giỏ hàng 7 món trên màn hình, sh040 thêm tổng tiền 2.000.000đ trên màn hình (chữ/số trên điện thoại thêm ở hậu kỳ nếu Veo vẽ sai).
- sh020: CU mặt → "Medium CU, mặt + điện thoại trong tay đều thấy rõ" (khớp hành động ngón tay lướt). sh030: 3 động tác → "Thở dài, mắt nhắm lại, tay vẫn bấm tiếp" (image + motion + storyboard).
- Hậu kỳ (script.md + manifest.yaml): bỏ luật cũ "tắt tiếng Veo"; luật hiện hành: kiểm tra giọng native từng shot, giữ gốc nếu nữ miền Bắc, chỉ lồng clone ThaoMy cho shot không phải Bắc. Manifest chuyển sang cấu trúc speakers như ep003/ep004 (preset ThaoMyVeo, locked). SFX cuối tập đề xuất: Laugh Track 1 sau câu chốt sh040 (chờ chốt vị trí).
- SHA-256 8 prompt đồng bộ lại trong episode.yaml (revision giữ 1). Validator mặc định: đạt. Generation gate: chặn đúng (chưa frame/duyệt gen). Edit gate: chặn đúng (chưa take). Lưu ý: cổng edit của validator vẫn đòi mute_veo_native: true (luật cũ) — mâu thuẫn luật 18/11 và manifest ep003/ep004/ep005 đã đăng; cần cập nhật validator sau, không chặn bước hiện tại.
- Chờ: chọn 1 trong 5 váy SANJOLI (Đen/Kem/Trắng/Hồng/Xanh dương) + son/móng; có gắn affiliate không. Chưa làm frame (chưa wardrobe.md), chưa gen.

## 2026-11-22 — Trang phục chốt: váy trắng

- Richard chọn váy trắng (widget, 07:46). Đã ghi vào cả 4 image prompt: "Trang phục: váy hai dây maxi suông SANJOLI màu trắng. Son đỏ. Móng tự nhiên." + lập wardrobe.md (nguồn váy trắng: sanjoli-color-variants/vn-11134207-81ztc-mthrovmm4g02e7.webp, sha b16dae2e…).
- Lưu ý affiliate: aff-0001 đã xác minh chỉ có Đen + Be, không có Trắng — gắn link vào tập này thì không đúng màu váy (y hệt ep003, khi đó Richard chốt BỎ link). Chờ Richard quyết có gắn affiliate không.
- SHA-256 4 image prompt đồng bộ lại; validator mặc định vẫn đạt (exit 0).
- Tiếp theo: làm 4 frame trong Flow (1 edit từ master v002 mỗi shot, 0 credit) để Richard duyệt, rồi gen 4 clip Lite (40 credit).

## 2026-11-22 — Đổi váy trắng → be + commit

- Richard đổi sang váy be (07:51). Đã sửa cả 4 image prompt ("màu trắng" → "màu be") + viết lại wardrobe.md (nguồn váy be: ep002-sanjoli-kem/vn-11134207-81ztc-mthrovoch3ibe2.webp, sha 214c8c45…). Màu Be CÓ bán thật trong listing aff-0001 (chỉ Đen + Be) nên gắn link sẽ đúng màu váy.
- SHA-256 4 image prompt đồng bộ lại; validator mặc định vẫn đạt (exit 0).
- Richard lệnh "update git luôn" (07:51) → commit + push scope ep009 + tracker (không động ep008/locations/affiliate-links đang dở dang).

## 2026-11-22 — 4 frame xong (Flow, 0 credit), chờ duyệt

- Project Flow mới "CNTM · EP009 · Giỏ Hàng": https://flow.google.com/project/3de63f40-b914-4aea-b513-6433db75e874 (huynhdn Pro). Mỗi frame 1 edit Nano Banana 2.1 trực tiếp từ master v002 (chọn lại bản gốc trong history trước sh020/sh030/sh040, không sửa nối tiếp), mỗi shot 1 lượt duy nhất, 0 credit, không gen video. Cả 4 frame là các version trong history của 1 asset master: asset ID 51d8f90d-cbaf-46ad-94a8-324c3d0ccfc2 (ghi chú ở đây, flow_image_asset_id trong episode.yaml giữ null theo tiền lệ ep004).
- Tải về bản 2K (1536×2752), đã verify trên disk (kích thước khớp receipt): sh010 442.245 byte, sh020 436.803, sh030 517.585, sh040 521.501. Lưu byte-identical vào input/frames/ (sh010/sh020/sh030/sh040-first-frame.jpg); episode.yaml cập nhật flow_project + first_frame/sha + frame_status pending_review; validator mặc định đạt (exit 0, không còn NOTE thiếu frame). Lỗi nhỏ lúc cập nhật: script lần đầu sót first_frame do không nhận dạng dòng "- shot_id:" — đã sửa script, chạy lại và verify hash khớp hết.
- QC độc lập của Bee (so với master v002, xem full-res + crop mặt): mặt khớp cả 4 (tóc nâu sóng + mái thưa, son đỏ, nốt ruồi cằm trái CÓ ở cả 4, thấy rõ nhất ở sh040 chính diện); váy be hai dây đúng mẫu; móng tự nhiên; phòng tối + ánh sáng xanh lạnh nhất quán. Màn hình: sh010 "00:00" rõ, sh020 "00:30" + giỏ hàng badge đỏ "7" rõ (chỉ ~4-5 thumbnail phân biệt được, số món thể hiện qua badge), sh040 "2.000.000đ" to rõ.
- Lưu ý nhỏ (không chặn duyệt): (1) sh020/sh040 có vài dòng chữ nhỏ trên màn hình điện thoại bị nhòe/gibberish (giá "$51.90" v.v.) — chữ nhỏ, sửa ở hậu kỳ nếu Veo vẽ sai như đã chốt trong review; (2) sh030 nền có thêm đèn bàn + cửa sổ đèn thành phố, ghế sofa không thấy rõ — cùng căn hộ ban đêm nhưng góc khác, mood vẫn nhất quán; (3) cả 4 frame có dấu sao Gemini góc phải dưới (như mọi frame ep003/ep004) — cắt ở hậu kỳ như thường lệ.
- Chờ Richard duyệt 4 frame → gen 4 clip Veo 3.1 Lite Frames-direct (40 credit).

## 2026-11-22 — Ảnh tham chiếu váy be (gen riêng), chuẩn bị áp vào ThaoMy

- Richard hỏi váy trong frame lấy từ đâu (09:06) → Bee trả lời: ảnh sản phẩm váy kem ep002 (aff-0001), nhưng trong frame vải vẽ hơi nhăn/kiểu linen hơn ảnh gốc lụa bóng. Richard lệnh: gen ảnh tham chiếu cho váy, sau đó mới áp dụng vào ThaoMy.
- Ảnh tham chiếu gen bằng media pipeline từ ảnh sản phẩm gốc: `02_characters/thao-my/wardrobe/inbox/ep009-sanjoli-be/sanjoli-be-dress-reference-v001.jpg` (1120×2240, sha f77702d9…, ghost mannequin chính diện, lụa be bóng nhẹ, hai dây mảnh, cổ tròn, suông dài, không người mẫu/chữ/logo/watermark). Bee đã xem: đúng kiểu + màu mẫu be. Lưu ý nhỏ: bản gen có thêm xẻ tà nhỏ ở gấu bên phải — ảnh sản phẩm gốc không thấy rõ chi tiết này.
- 4 frame v1 (09:02) chờ làm lại với ảnh tham chiếu váy mới sau khi Richard ok ảnh này; frame_status vẫn pending_review, chưa gen clip.

## 2026-11-22 — 4 frame v2 (váy lụa đúng mẫu), chờ duyệt

- Richard ok ảnh tham chiếu váy (widget 09:15) → làm lại 4 frame v2 trong cùng project Flow (0 credit), mỗi shot 1 edit từ master v002 + gắn ảnh tham chiếu váy làm ingredient thứ 2. sh020 phải làm lại lần 2 (lần 1 giỏ hàng không đọc được) — tổng 5 lượt gen, 4 file tải về.
- Tải về bản 2K (1536×2752), đã verify trên disk: sh010 436.554 byte, sh020 381.015, sh030 362.771, sh040 423.469. Lưu byte-identical vào input/frames/ (sh010/sh020/sh030/sh040-first-frame-v2.jpg, v1 giữ nguyên); ảnh tham chiếu váy copy vào input/references/; episode.yaml cập nhật first_frame → v2 + image_sources thêm dress ref (3 nguồn/shot), frame_status pending_review; validator mặc định đạt (exit 0).
- QC độc lập của Bee (so với master v002 + ảnh tham chiếu váy, xem full-res + crop mặt): váy ĐÚNG lụa bóng cả 4 (mềm, có sheen, không còn nhăn linen); hai dây mảnh, cổ tròn, màu be đúng mẫu. Mặt khớp, nốt ruồi cằm trái có cả 4, son đỏ, móng tự nhiên. Màn hình: sh010 "00:00" rõ; sh020 tốt hơn v1 — tiêu đề "Shopping Cart (7 items)" + badge đỏ "7" + hàng sản phẩm rõ; sh040 "2.000.000đ" to rõ. Nền sh030 giờ là giường (cùng set với sh020), không còn đèn bàn/cửa sổ lệch như v1.
- Lưu ý nhỏ (không chặn duyệt): vài dòng chữ nhỏ trên màn hình sh020/sh040 vẫn hơi nhòe (giá/tên món gibberish) — chữ nhỏ, sửa ở hậu kỳ nếu Veo vẽ sai; cả 4 frame có dấu sao Gemini góc phải dưới (như mọi tập trước) — cắt ở hậu kỳ.
- Lỗi nhỏ lúc cập nhật: script thêm image_sources thụt lề sai làm YAML lỗi parse — đã sửa lề (6/8 khoảng trắng), verify hash khớp hết + validator đạt.
- Chờ Richard duyệt 4 frame v2 → gen 4 clip Veo 3.1 Lite Frames-direct (40 credit).

## 2026-11-22 — 4 frame v3 (body đúng ref + iPhone ốp Slimcase + sh020 cận màn hình), chờ duyệt

- Richard chê v2: ngực nhỏ quá, body không đúng; thêm yêu cầu điện thoại dùng iPhone có ốp affiliate; sh020 chỉ gen màn hình điện thoại thao tác.
- Sửa hồ sơ trước khi gen: 4 image prompt + motion sh020 + storyboard sh020 đều thêm "Điện thoại: iPhone trong ốp lưng trong suốt MagSafe Slimcase."; sh020 đổi khung thành cận cảnh màn hình thao tác (không mặt). Ảnh tham chiếu ốp: ảnh sản phẩm aff-0003 (-02, ốp trong + vòng MagSafe trắng), copy vào input/references/slimcase-phone-ref.jpg; episode.yaml đồng bộ hash + image_sources 4 nguồn/shot (mặt + body + váy + ốp); validator mặc định đạt (exit 0).
- Làm lại 4 frame v3 trong cùng project Flow (0 credit), mỗi shot 1 edit từ master v002 + 4 chip tham chiếu (mặt + váy + body + ốp). sh010 làm lại lần 2 (lần 1 điện thoại quay lưng, không thấy 00:00); sh020 làm 3 lượt đều giữ mặt trong khung (model neo theo ảnh master mặt) — lấy lượt 1 gần nhất.
- Tải về bản 2K (1536×2752), đã verify trên disk: sh010 439.615 byte, sh020 333.755, sh030 355.553, sh040 518.447. Lưu byte-identical vào input/frames/ dạng -v3 (v1/v2 giữ nguyên); episode.yaml cập nhật first_frame → v3, frame_status pending_review; validator đạt.
- QC độc lập của Bee (full-res + crop mặt): NGỰC ĐÃ ĐẦY — cả 4 đều có đường cong tự nhiên dưới váy lụa, khớp body ref, không còn phẳng như v2. Váy lụa bóng đúng cả 4. Mặt khớp, nốt ruồi cằm trái có (sh010/sh030/sh040, crop mặt), son đỏ, móng tự nhiên. Ốp Slimcase: sh010 viền ốp trong quanh mép máy; sh030 thấy rõ lưng máy — ốp trong + vòng MagSafe trắng + 3 camera, khớp ảnh sản phẩm; sh040 viền ốp quanh mép máy. Màn hình: sh010 "00:00" rõ; sh040 "2.000.000đ" to rõ.
- sh020: bản Flow v3 vẫn lọt mặt nghiêng ở mép phải (3/3 lượt đều vậy) + badge đỏ "7" nhỏ khó đọc (nhưng "Cart (7)" + "7 items" rõ). Bee crop hậu kỳ từ bản Flow: crop 864:1536:0:900 + upscale lanczos 1536:2752 → sh020-first-frame-v3-crop.jpg (sha 49fb1392…), chỉ còn điện thoại + tay lướt, không mặt; badge đỏ "7" trong bản crop đọc được. first_frame sh020 trỏ vào bản crop (bản Flow gốc giữ nguyên làm nguồn). Nếu Richard thích bản Flow gốc thì đổi lại 1 dòng.
- Lưu ý nhỏ: màn hình sh010 có thêm vòng tròn trắng lớn (vòng MagSafe lọt lên màn hình, trông như widget màn hình khóa) — "00:00" vẫn đọc rõ; vài chữ nhỏ trên màn hình sh020/sh040 vẫn hơi nhòe; dấu sao Gemini góc phải dưới — cắt ở hậu kỳ.
- Chờ Richard duyệt 4 frame v3 → gen 4 clip Veo 3.1 Lite Frames-direct (40 credit).

## 2026-11-22 — Richard DUYỆT 3 shot sau (sh020 crop, sh030, sh040); sh010 chưa duyệt vì điện thoại lạ

- Đã ghi approved_for_generation: true + frame_status: approved cho sh020 (bản crop), sh030, sh040; validator mặc định vẫn đạt (exit 0).
- sh010: Richard hỏi sao điện thoại shot đầu lạ — màn hình dính vòng tròn trắng lớn (vòng MagSafe từ ảnh tham chiếu ốp lọt lên màn hình, trông như widget màn hình khóa; "00:00" vẫn đọc rõ). Nguyên nhân: sh010 quay mặt trước điện thoại nên vòng MagSafe ở lưng ốp vốn không nhìn thấy — chip ốp là thừa ở shot này và chính nó làm vòng lọt lên màn hình.
- Hướng sửa sh010 v4 (chờ Richard gật): làm lại 1 edit từ master v002, KHÔNG gắn chip ốp (chỉ mặt + váy + body), prompt thêm "Màn hình chỉ hiện 00:00, không có vòng tròn hay hình vẽ nào khác trên màn hình." Viền ốp trong quanh mép máy vẫn giữ được vì máy vốn trong ốp.
- Richard sửa lại chẩn đoán của Bee (10:01): không phải chỉ vòng lọt lên màn hình — điện thoại v3 bị NGƯỢC ra sau (đặc điểm mặt lưng hiện lên phía màn hình nên máy đọc như bị lật ngược); vòng tròn thì đúng là từ ốp. Bee sửa prompt sh010 (bỏ "MagSafe" khỏi dòng điện thoại, màn hình chỉ hiện 00:00, không vòng tròn/hình vẽ khác), đồng bộ hash, validator đạt. Richard lệnh "gen lại đi" → đang làm lại sh010 v4 trong cùng project Flow (1 edit từ master, chỉ 3 chip mặt + váy + body, KHÔNG gắn chip ốp).

## 2026-11-22 — sh010 v4 THẤT BẠI (3 lượt đều quay lưng điện thoại), chờ Richard quyết hướng tiếp

- Làm lại sh010 v4 trong cùng project Flow (0 credit, 1 edit từ master, chỉ 3 chip mặt + váy + body, KHÔNG gắn chip ốp, prompt sửa: điện thoại chỉ "ốp lưng trong suốt", màn hình chỉ hiện 00:00 không vòng tròn/hình vẽ khác).
- Kết quả: cả 3 lượt đều quay LƯNG điện thoại về camera (ốp trong + 3 camera, không thấy màn hình, không có 00:00 ở đâu) — không đạt yêu cầu cứng nên không tải về lượt nào. Mọi thứ khác đều đạt (ngực đầy khớp body ref, váy lụa, mặt/son/móng, phòng tối + ánh sáng xanh). Vòng tròn đã hết (vì không thấy màn hình) nhưng 00:00 cũng mất luôn.
- Nguyên nhân có thể: bỏ chip ốp thì model không còn neo hướng màn hình, mặc định vẽ lưng máy. Hướng tiếp theo (chờ Richard): (a) thử thêm vài lượt v4 + thêm câu "màn hình hướng về phía camera" vào prompt — hướng mặt màn hình đã từng ra ở v2 và v3 lượt 2 nên có cơ may; (b) sửa thẳng frame v3 để xóa vòng tròn (phá luật 1 edit từ master, chỉ nên làm khi (a) vẫn trượt).

## 2026-11-22 — sh010 sửa vòng TRỰC TIẾP từ frame v3 (ringfix), XONG lượt 1, chờ duyệt

- Richard chốt hướng sửa thẳng frame v3 (ngoại lệ luật 1 edit từ master, do cậu ấy quyết sau khi v4 trượt 3/3 lượt quay lưng điện thoại).
- Sửa trong cùng project Flow (0 credit): 1 edit Nano Banana trực tiếp trên frame v3 sh010 (mở đúng version v3 trong history, kiểm tra thumbnail trước khi sửa), lệnh "xóa vòng tròn trắng trên màn hình, chỉ để 00:00, giữ nguyên mọi thứ khác", không gắn chip tham chiếu nào. Đạt ngay lượt 1.
- Tải về bản 2K (1536×2752, 526.148 byte, sha fe1dd27c…), đã verify trên disk. Lưu byte-identical vào input/frames/sh010-first-frame-v3-ringfix.jpg (bản v3 gốc giữ nguyên); episode.yaml cập nhật first_frame sh010 → ringfix, frame_status vẫn pending_review; validator đạt.
- QC độc lập của Bee (full-res + crop mặt): VÒNG ĐÃ HẾT — màn hình chỉ còn 00:00 trên nền xanh đậm, không vòng tròn/hình vẽ nào khác; điện thoại đọc như máy bình thường, không còn cảm giác ngược. Mặt KHÔNG drift (so trực tiếp với v3: cùng góc, cùng tóc/son; nốt ruồi cằm trái vẫn có, crop mặt), ngực vẫn đầy, váy lụa, tay, sofa, ánh sáng xanh giữ nguyên. Màn hình giờ sạch hẳn (cả chữ nhỏ/status bar cũ cũng hết — đúng prompt "chỉ hiện 00:00").
- Chờ Richard duyệt sh010 bản ringfix → đủ 4 frame duyệt → gen 4 clip Veo 3.1 Lite Frames-direct (40 credit).

## 2026-11-22 — sh010 dùng chung frame sh030, ĐỦ 4 FRAME DUYỆT

- Richard chê bản ringfix ("ko đúng rồi") và chốt: dùng frame sh030 cho cả sh010 + sh030.
- Bee đã nói rõ hệ quả trước khi cậu ấy chốt: frame sh030 quay lưng điện thoại (ốp + vòng MagSafe, không thấy màn hình) nên "00:00" sẽ KHÔNG hiện trong sh010 — câu "Mười hai giờ" mất bằng chứng trên hình. Richard chấp nhận ("cũng đc").
- episode.yaml: first_frame sh010 → input/frames/sh030-first-frame-v3.jpg (sha 6033f910…, khớp file sh030), frame_status sh010 → approved, approved_for_generation → true; editorial_status draft → generating (theo tiền lệ ep003); script.md đồng bộ (trạng thái + ghi chú frame chung ở storyboard sh010). Validator mặc định ĐẠT + cổng generation ĐẠT (exit 0 cả hai).
- Bản ringfix và bản v3 sh010 giữ nguyên trong input/frames/ (không dùng, không xóa).
- CHỜ: gen 4 clip Veo 3.1 Lite Frames-direct (40 credit).

## 2026-11-22 — Gen 4 clip Lite XONG (40cr, 470→430), take001 chờ duyệt

- Gen trong cùng project Flow, Frames-direct, Agent OFF, Veo 3.1 Lite, 9:16, 8s, 1 output/shot, 10cr/clip. Số dư 470 → 430. Không clip nào bị chặn chính sách.
- Clip ID: sh010 0cc83a3e…, sh020 6b19cfbe…, sh030 ef04d571…, sh040 26d94b78…. Tải về bản 720p gốc (7.93s, 720×1280, 24fps), đã verify trên disk, lưu vào generated/sh0X0-take001.mp4 (byte-identical); episode.yaml ghi take001 (status needs_review) + hash; validator mặc định đạt.
- SỰ CỐ MAP FILE — ĐÃ SỬA TRƯỚC KHI TRÌNH: lúc lưu take tao gán nhầm file theo thứ tự thời gian tải về (040953 → sh020, 040540 → sh030) trong khi receipt của trình duyệt liệt kê lệch thứ tự (f2 = sh020 = file 040540, f3 = sh030 = file 040953). Whisper base bắt được: file "sh020" nói thoại sh030 và ngược lại. Đã đổi lại đúng theo artifact ID + clip ID, chạy lại Whisper xác nhận. Bài học ghi vào AGENTS.md: map take theo receipt artifact ID, không theo giờ tải.
- QC độc lập của Bee (Whisper base + frame 0.5/4/7.5s): cả 4 clip đúng thoại, mỗi câu nghe đúng 1 lần, không lặp. sh010 "Mười hai giờ…" (nghe nhầm "một món"→"mục móng"); sh020 "Ba mươi phút sau…" (giỏ hàng cuộn thật, "Shopping Cart / 7 items / 00:30" rõ, không mặt); sh030 "Tôi xóa hết…" (mắt nhắm, thở dài, tay bấm); sh040 "Tiết kiệm bảy trăm ngàn…" (nghe nhầm đồng âm "trăm/chăm", "triệu/chiều"; "2.000.000đ" rõ 4–6s; điện thoại hạ xuống khỏi khung ~7s — cắt đuôi khi dựng, không cần quay lại). Không clip nào có phụ đề giả/chữ lạ trên màn hình; mặt khớp, không drift. Lưu ý nhỏ: sh030 t4.0 có chấm trắng thoáng qua ở đầu ngón tay (1 frame, mất ngay sau đó).
- CẢNH BÁO ASR CỦA TRÌNH DUYỆT SAI: báo cáo trình duyệt nói thoại sh040 là "tiếng Thái không hiểu được" (2 lần nghe đều ra chữ Thái) — Whisper base của Bee nghe ra đúng câu tiếng Việt (chỉ nhầm đồng âm). Đừng kết luận take hỏng thoại chỉ từ ASR của trình duyệt; kiểm chứng bằng Whisper base local trước.
- Giọng: Bee không tự kết luận Bắc/Nam bằng tai máy — Richard nghe và chốt khi duyệt take (theo luật giọng: giữ native nếu nữ Bắc, lồng clone ThaoMy nếu không).
- CHỜ: Richard duyệt 4 take → upscale 2K → dựng master (Boxed + SRT + Laugh Track 1 sau sh040 — vị trí SFX vẫn chờ chốt; affiliate chưa quyết).

## 2026-11-22 — Richard duyệt take: sh040 giữ native Bắc, sh010/sh020/sh030 lồng clone

- Richard chốt giọng sau khi xem 4 take: shot cuối (sh040) đúng giọng Bắc → giữ tiếng gốc; 3 shot còn lại lồng tiếng.
- episode.yaml: 4 take take001 needs_review → accepted_editorial; edit/manifest.yaml: selected_takes = 4 take001, audio_plan thao_my ghi rõ sh040 giữ gốc / sh010+sh020+sh030 tắt gốc lồng clone ThaoMyVeo. Validator mặc định đạt.
- Đang tải bản 2K (1080p upscale, 0 credit) của 4 take đã duyệt. Sau đó: lồng clone ThaoMy cho sh010/sh020/sh030 (VieNeu v3 Turbo trên Colab T4, tiền lệ ep008 wordalign) → dựng master Boxed + SRT + Laugh Track 1 (vị trí SFX vẫn chờ chốt; affiliate chưa quyết).

## 2026-11-22 — Upscale 2K 4 take XONG (0 credit), đã verify bằng frame-diff

- Tải về bản 1080p ("1080p Đã tăng độ phân giải") của 4 take đã duyệt, 0 credit, trong cùng project Flow. Số dư không đổi (430). Không gen thêm video.
- Verify độc lập của Bee trên disk (ffprobe + frame-diff @2.5s, không tin tên file/clip ID): cả 4 file đều 1080×1920, 24fps, 7.85s. Frame-diff MAD vs take 1K của chính nó ≈ 2.1 (sh010 2.13, sh020 2.17, sh030 2.10, sh040 2.17); vs các shot khác 41–61 — ĐÚNG take cả 4. Ngoại lệ đúng như kỳ vọng: sh010-2K vs sh030-1K = 8.14 và sh030-2K vs sh010-1K = 8.36 (hai clip chung frame đầu nên gần nhau hơn, nhưng vẫn tách biệt rõ với 2.1).
- File 2K lưu vào generated/sh0X0-take001-1080p.mp4 (byte-identical, sha: sh010 822a42b0…, sh020 3edb0f88…, sh030 69527177…, sh040 7d47915d…).
- Sự cố upscale sh010: lỗi "Không tăng được độ phân giải!" 2 lần (lần đầu bấm khi player chưa load xong, lần 2 sau chờ 3 phút); reload trang rồi làm lại thì được — đúng bài học 20/11 (upscale chạy thì để yên, đừng chạm giữa chừng; lỗi thì reload + chờ). 3 clip còn lại chờ player load hẳn (30s) rồi bấm thì 1 lần được ngay. Không có paywall Ultra lần này.
- TIẾP THEO: lồng clone ThaoMy cho sh010/sh020/sh030 (sh040 giữ native Bắc) → dựng master Boxed + SRT + Laugh Track 1 (vị trí SFX vẫn chờ chốt; affiliate chưa quyết).

## 2026-11-22 — Lồng clone ThaoMy xong 3 shot (wordalign, đã QC)

- Clone ThaoMyVeo, VieNeu v3 Turbo trên Colab T4 (session ep009-dub, enroll từ ref-clip2.wav; đã dừng session, không orphan). Script Colab: ~/workspace/colab-t4-test/ep009_dub_thaomy.py; wav gốc: ~/workspace/colab-t4-test/ep009-dub/thaomy-ep009-sh0{10,20,30}.wav; build: /tmp/ep009_build_wordalign.py.
- Phương pháp wordalign như ep008 đã duyệt: mỗi từ clone stretch đúng cửa sổ từ native (đo bằng energy envelope 48kHz stereo 0.1s; Whisper smear như thường lệ — sh010 'Mười' Whisper ghi 0.86s nhưng năng lượng chứng minh onset ~1.08s). Hệ số 0.60x–1.70x, không từ nào quá 1.8x.
- File lồng: generated/sh010/sh020/sh030-take001-dubbed.mp4 (1080×1920, 7.85s, video copy từ bản 2K, audio thay hoàn toàn bằng track clone mono 48kHz AAC 192k; tiếng gốc tắt hẳn, không bed nền, không rò). sh040 giữ nguyên native Bắc, không đụng. Take gốc không bị ghi đè.
- QC (Whisper base + energy envelope, file edit/dub-qc-ep009.md): cả 3 đều ĐẠT — Whisper nghe đủ từ (các nhầm 'nuôi'≈mua, 'nón'≈món, 'Mà 10'≈'Ba mươi', 'tụi'≈tôi, 'dồi'≈rồi là artifact đồng âm của Whisper; wav clone gốc nghe đúng chữ). Bee kiểm chứng độc lập năng lượng trên sh010/sh030: nóng đúng cửa sổ từ native, 0.0000 ngoài cửa sổ.
- 2 từ kéo nhiều nhất cần tai Richard kiểm tra: 'chỉ' ở sh010 (cửa sổ native chỉ 0.10s, stretch 1.60x) và 'xóa' cuối sh030 (1.70x).
- TIẾP THEO: Richard duyệt 3 bản lồng → dựng master (nối 4 clip 2K: 3 lồng + sh040 native; cắt đuôi sh040 trước ~7s; Boxed + SRT + Laugh Track 1 — vị trí SFX vẫn chờ chốt; affiliate chưa quyết).

## 2026-11-22 — Richard DUYỆT 3 bản lồng, lệnh dựng master

- Richard duyệt 3 bản lồng (widget, 12:42). Đang dựng master: nối 4 clip 2K (3 lồng + sh040 native), cắt đuôi sh040 trước ~7s, Boxed + SRT + Laugh Track 1 sau câu chốt sh040 (vị trí SFX theo đề xuất — trình master xong Richard nghe thử rồi chốt vị trí). Affiliate chưa quyết (không chặn dựng master).

## 2026-11-22 — Ngày đăng ep009: 24/11 (thứ Ba), 1 tập/ngày

- Richard chốt: mỗi ngày đăng 1 tập → ep009 đăng ngày kia 24/11 (sau ep007 22/11 và ep008 23/11). Giờ đăng theo khung chuẩn 19:00 (chưa nói khác).
- Sau khi master được duyệt: chuẩn bị bộ đăng (caption + link affiliate nếu chốt) rồi hẹn lịch 19:00 24/11 cả TikTok + Facebook.

## 2026-11-22 — Master 2K DONE (22.73s), đã QC — chờ Richard duyệt

- File: `delivery/ep009-master-2k.mp4` (sha 87f0eebe…, 1080×1920, 30fps, 22.73s, 21,859,783 B, -14.80 LUFS / TP -2.00) + `delivery/ep009-master-2k.srt` (4 cues: 1.11–4.85 / 5.62–9.15 / 10.41–15.15 / 16.10–20.74). Script dựng: `edit/build_master_2k.py`; script sửa captions: `edit/fix_captions_2k.py`; báo cáo: `edit/build2k/captions-fix-report.md`.
- Trim (đo bằng energy envelope + Whisper, không đoán): sh010 5.5s (lồng, thoại 1.11–4.85) / sh020 4.4s (lồng, thoại 0.11–3.65) / sh030 6.0s (lồng, thoại 0.50–5.25) / sh040 6.5s (gốc, 2 câu 0.2–1.86 + 3.16–4.84; điện thoại vẫn giơ "2.000.000đ" ở 6.5s, bắt đầu hạ ~6.8s). Crop watermark Veo 960:1707:60:0 + lanczos (icon góc phải dưới ~y1770, giống ep008). Concat FILTER (không demuxer+copy). Không title card.
- Captions: v1 (Whisper-only) SAI — Whisper gộp số thành digit nên lệch từ tới ~1.5s; đã sửa thành v2 bằng timings đo lường (Whisper trên wav clone + Whisper trên file lồng/gốc + energy envelope, đối chiếu ~0.1s), render lại Remotion Boxed (chunked ≤287 frame, concurrency=1, không đen frame). Contact sheet đã xem: mặt/váy/điện thoại đúng, phụ đề rõ, ô highlight đúng từ đang nói (sh040 mid: "CHỈ" sáng đúng lúc), watermark đã hết, không frame đứng ở điểm cắt.
- SFX: Laugh Track 1 sau câu chốt sh040, nghe từ ~20.89s, kèm freeze-frame tail 0.23s (ngắn vì câu chốt kết thúc muộn 20.74s) — VỊ TRÍ ĐỀ XUẤT, chưa chốt; Richard có thể yêu cầu dời.
- QC: ffprobe đúng chuẩn; frame means 46–60 khắp video, không frame đen (t=22.8s đọc -1.0 chỉ vì đã quá cuối video 22.73s); năng lượng từng shot khớp thoại; Whisper nghe đủ 4 câu (các nhầm đồng âm quen thuộc); loudness -14.80 LUFS / TP -2.00.
- Sự cố trong lúc dựng: service restart 1 lần giữa stage 1 (chỉ xong seg-sh010, không mất gì, chạy lại toàn bộ); script sửa captions chết ở bước cuối vì thiếu helper `sha` khi ghi báo cáo (master đã xong + QC xong trước đó) — báo cáo đã viết tay lại từ log, không chạy lại.
- CHỜ: Richard duyệt master → làm bộ đăng (caption + affiliate/SFX chốt) → hẹn giờ đăng.

## 2026-11-22 — Master 2K XONG, đã QC độc lập, chờ Richard duyệt

- Master: delivery/ep009-master-2k.mp4 (sha 87f0eebe…, 1080×1920, 30fps, 22.73s, 21.859.783 B) + delivery/ep009-master-2k.srt (4 cues: 1.11–4.85 / 5.62–9.15 / 10.41–15.15 / 16.10–20.74). Scripts: edit/build_master_2k.py, edit/fix_captions_2k.py; báo cáo: edit/build2k/captions-fix-report.md.
- Trim: sh010 5.5s / sh020 4.4s / sh030 6.0s / sh040 6.5s (cắt đuôi trước ~7s, điện thoại vẫn giơ 2.000.000đ ở 6.5s, bắt đầu hạ ~6.8s). Crop watermark Veo 960:1707:60:0 + lanczos. Concat FILTER. Loudnorm I=-15.5/TP=-1. Không title card. Boxed captions Remotion (#F59E0B), render chunked ≤287 frame, --concurrency=1 --muted.
- LỖI PHÁT HIỆN VÀ SỬA: bản dựng đầu (v1) dùng Whisper-only alignment nên sai thật — Whisper gộp số thành digit ("Mười hai"→"12", "Ba mươi"→"30", "bảy trăm ngàn"→"700.000"), lệch từ tới ~1.5s (sh020 "sau." timed 8.18s nhưng nói lúc ~6.5s; sh040 "Chỉ" hiện sớm 1.8s). Đã sửa thành v2 bằng timings đo lường (Whisper trên wav clone sạch + Whisper trên file lồng/gốc + energy envelope, đối chiếu ~0.1s), render lại Remotion + stage 3. Bản v1 đã ghi đè; chi tiết trong edit/build2k/captions-fix-report.md và captions-PROBLEMS.txt.
- QC độc lập của Bee trên bản final: ffprobe đúng chuẩn; 23 frame mẫu 1s/giây mean 45.8–63.1, KHÔNG frame đen; loudness đo lại -14.80 LUFS / TP -2.00 dB; SRT đúng 4 câu; 2 frame soi trực tiếp (sh040 giữa 18s: caption "TRĂM NGÀN." đúng từ đang nói, mặt/váy/điện thoại đúng, không watermark; đuôi 22s: freeze giữ nguyên nụ cười + điện thoại, không caption) — ĐẠT.
- Sự cố trong lúc dựng: service restart 1 lần giữa stage 1 (chạy lại từ đầu, không mất gì); script sửa captions chết bước cuối vì thiếu helper `sha` khi ghi báo cáo (master + QC đã xong trước đó, báo cáo viết tay từ log).
- CHƯA QUYẾT: vị trí SFX (Laugh Track 1 sau câu chốt sh040, nghe từ ~20.89s, freeze tail 0.23s — ngắn hơn ep004 0.48s vì câu chốt kết muộn 20.74s; dời được, chỉ làm lại stage 3); affiliate chưa quyết.
- TIẾP THEO: Richard duyệt master → chuẩn bị bộ đăng (caption + link affiliate nếu chốt) → hẹn lịch 19:00 thứ Ba 24/11 cả TikTok + Facebook.

- Validator (chạy lại từ repo root sau khi dựng): default exit 0; edit gate exit 1 — nhưng 2 lỗi đó là lỗi stale đã biết của validator (đòi mute blanket + key giọng flat), trái với luật giọng per-shot 18/11 và manifest ep003/ep004/ep005 đã ship; manifest ep009 ghi đúng speakers.thao_my (ThaoMyVeo, locked) + policy per-shot, dub đã làm bằng clone. Không phải lỗi thật của master.

## 2026-11-22 — Richard DUYỆT master, chuẩn bị bộ đăng

- Master duyệt (widget, 13:15). Vị trí SFX CHỐT theo master đã duyệt: Laugh Track 1 sau câu chốt sh040.
- Bìa: frame 19.5s của master (My cười toe, mắt mở, điện thoại giơ 2.000.000đ, caption 'CHỈ TỐN HAI') → delivery/ep009-cover-thaomy-sh040.jpg (1080×1920). Đã soi 3 ứng viên (17.5s há miệng quá, 18.5s nhắm mắt) — 19.5s tốt nhất.
- Bộ đăng: caption TikTok 'Tiết kiệm bảy trăm ngàn. Chỉ tốn hai triệu. 😌' + #chuyennhathaomy #phimnganai #haiviet + dòng CC BY Laugh Track 1; Facebook thêm link affiliate (chờ Richard chốt: đề xuất cả 2 — váy be là variant thật của aff-0001, ốp là product placement trong khung hình); comment ghim ngắn 3 dòng; hẹn 19:00 thứ Ba 24/11 cả 2 nền tảng, nhãn AI TikTok bật, bìa mặt Thảo My.

## 2026-11-22 — Affiliate CHỐT: chỉ link váy (Facebook); link ốp vào comment (Richard tự gắn)

- Richard chốt qua widget (13:30): chỉ link váy. Mô tả Facebook = caption + dòng link váy aff-0001 (https://s.shopee.vn/5LDVnTeC4f) + hashtags + dòng CC BY Laugh Track 1. TikTok giữ caption chốt (không link, link TikTok không bấm được).
- Link ốp aff-0003 KHÔNG vào mô tả — Richard tự gắn vào comment. Content comment đưa Richard: "Ốp lưng trong suốt MagSafe Slimcase Thảo My dùng trong video đây nhé: https://s.shopee.vn/AKcGpsTOV8".
- Đang hẹn lịch 19:00 thứ Ba 24/11 cả 2 nền tảng (master + bìa frame 19.5s). Cron xác minh 19:20 24/11 sẽ đặt sau khi có ID bài.

## 2026-11-22 — ĐÃ HẸN LỊCH 19:00 thứ Ba 24/11 cả 2 nền tảng

- TikTok @chuyennhathaomy: video ID 7710879994213322002 (https://www.tiktok.com/@chuyennhathaomy/video/7710879994213322002), hẹn 19:00 24/11, Everyone, nhãn AI BẬT, caption đúng y chữ, bìa = ảnh cover Thảo My (đã xác minh trong Studio > Posts). Video 00:22, 1080p.
- Facebook Page Chuyện Nhà Thảo My: post ID 2033685737320568, hẹn 19:00 24/11, Public, Reel, mô tả đúng y chữ gồm link váy aff-0001, bìa = ảnh cover Thảo My (đã xác minh trong Content > Scheduled + Planner). Không có tùy chọn nhãn AI trên Business Suite web (như đã biết). Facebook báo "Reel scheduled" + "No copyright issues were found".
- Không captcha, không xác minh thiết bị, không đăng sớm, không đụng bài khác.
- Cron xác minh 19:20 24/11 (ep009-record-publication) sẽ kiểm tra 2 bài đã lên sóng + ghi publications.csv + tracker + commit.

## 2026-11-24 — ĐÃ LÊN SÓNG 19:00 + ghi publication (cron ep009-record-publication)

- TikTok @chuyennhathaomy LIVE: https://www.tiktok.com/@chuyennhathaomy/video/7710879994213322002 — public (Everyone), caption đúng y chữ + hashtags + dòng CC BY Laugh Track 1, nhãn AI BẬT ("Creator labeled as AI-generated"), bìa mặt Thảo My cầm điện thoại. Studio 19:20: 5 views, 0 like, 0 comment.
- Facebook Page Chuyện Nhà Thảo My LIVE: https://www.facebook.com/reel/1017688074713810 — Public, mô tả đúng (caption + link váy aff-0001 https://s.shopee.vn/5LDVnTeC4f + hashtags + dòng CC BY), bìa mặt Thảo My (điện thoại hiện 2.000.000đ). LƯU Ý: ID hẹn giờ 2033685737320568 chỉ là ID lịch hẹn — reel công khai là 1017688074713810 (Business Suite content ID 1238208361871987). Không có nhãn AI trên web Business Suite (đã biết, không phải lỗi).
- Like + comment aff-0003: comment panel báo "No comments yet" trước đó nên KHÔNG trùng — Bee đăng mới 1 comment với tư cách Page 19:22, đúng câu đã duyệt ("Ốp lưng trong suốt MagSafe Slimcase Thảo My dùng trong video đây nhé: https://s.shopee.vn/AKcGpsTOV8"), comment ID 1663462468486188, URL https://www.facebook.com/reel/1017688074713810/?comment_id=1663462468486188. Like mới của Page cùng lúc (Reel có 1 reaction + 1 comment). Ghi plc-0011 vào affiliate-placements.csv.
- Ghi publication: 2 dòng mới vào 07_analytics/publications.csv, tracker ep009 → published, commit scope ep009.
