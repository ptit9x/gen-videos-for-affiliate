# ep010-love-bombing — work log

## 2026-11-19 — Áo linen chuyển sang ep010 (Bee)
- Richard chốt: áo linen LAHSTORE (aff-0002) bỏ khỏi ep006, để vào ep010 Love Bombing — solo ở nhà, sofa ban ngày, đúng bối cảnh áo.
- Ghi vào `script.md` (khóa trang phục + bảng sản phẩm lồng ghép) và `wardrobe.md` mới; sug-0007 chuyển episode ep006 → ep010; ghi chú aff-0002 cập nhật.
- Màu áo chưa chốt; ảnh mẫu màu Tím — dùng Tím khi làm frame nếu Richard không đổi.
- Chưa làm: episode.yaml + prompts ep010 vẫn là bản "Mở hộp" cũ (4 shot unboxing), chưa đồng bộ với kịch bản Love Bombing 3 shot — cần đồng bộ trước khi làm frame/gen clip. Script còn cụm "không nhạc/chữ/phụ đề" ở mục Tài sản và prompt, cần bỏ trước khi gen (bài học phụ đề giả 14/11).

## 2026-11-19 — Đồng bộ episode.yaml + prompts sang Love Bombing (Bee)
- Viết lại 6 prompt theo kịch bản Love Bombing 3 shot (sofa phòng khách ban ngày, áo linen tím); xóa prompt sh040 cũ (unboxing). Bỏ cụm nêu tên phụ đề/chữ khỏi mọi prompt + script; hậu kỳ sửa theo quy tắc giữ tiếng Veo nếu giọng Bắc.
- Viết lại `episode.yaml`: title "Love Bombing", target 24s, 3 shot, dialogue + sha256 prompt mới, image_sources giữ nguyên (hash khớp). Revision giữ 1, manifest khớp.
- Validator default chạy sau bước này; generation gate chặn đúng như kỳ vọng (chưa có frame duyệt / flow_project).
- Kết quả validator 19/11: default exit 0 ("Episode structure valid", chỉ note frame thiếu + giọng VieNeu pending); generation exit 1 đúng kỳ vọng (shot chưa duyệt, chưa có frame, chưa có Flow project, draft).

## 2026-11-23 — Sửa thoại sh010 theo phương án A (Richard chốt) + sửa số từ (Bee)
- Richard chốt phương án A cho sh010: "Tuần đầu, năm mươi tin một ngày. 'Anh chưa gặp ai như em.'" — 13 từ, thay bản cũ 20 từ/3 câu (script ghi sai 18 từ).
- Sửa số từ trong script.md cho khớp đếm thật: sh010 18 → 13; sh030 13 → 16 (thoại sh030 chưa đổi, bản gọn 14 từ vẫn chờ Richard quyết).
- Hook 3 giây sửa theo thoại mới: "Tuần đầu, năm mươi tin một ngày."
- Thêm điện thoại vào tay My ở sh010 (script + sh010-image): cầm/lướt điện thoại trong lúc kể, để con số "năm mươi tin" có bằng chứng trên hình; chữ trên màn hình thêm ở hậu kỳ, không đưa vào prompt video.
- Cập nhật dialogue + sha256 prompt mới vào episode.yaml (sh010-image 54dbbbbd…, sh010-motion a46fe310…).
- Chưa chốt: màu áo linen (Richard không nhớ — ảnh mẫu màu Tím vẫn là mặc định trong prompt); location phòng khách (v001 chưa duyệt); son/móng; thoại sh030 giữ 16 từ hay gọn 14 từ. Chưa commit.

## 2026-11-23 — Chốt màu/bối cảnh/son-móng + sh030 14 từ (Richard)
- Màu áo linen CHỐT: Tím như ảnh mẫu (Richard: "như ảnh nhé").
- Bối cảnh ĐỔI từ phòng khách sang quán café: date-cafe v003-day (Richard duyệt 21/11 cho ep008, sha 1a66036e…, bàn tròn khăn trắng, ghế gỗ tối cao đệm be, 2 ly nước cam, cây xanh). Phòng khách v001 không hợp. Script + wardrobe + cả 3 image prompt + sh010-motion đã đổi sang café; sh020/sh030-image thêm "phối quần short trắng" khóa continuity với sh010.
- Son tự nhiên, móng tự nhiên CHỐT 23/11 (theo luật series).
- sh030 gọn 14 từ theo quyết Richard: "Dội bom xong rút quân. Chiến thuật quân sự đem áp vào hẹn hò." (bản 16 từ cũ bỏ).
- Cập nhật dialogue + sha256 prompt mới vào episode.yaml (sh010-image 66a31aed…, sh010-motion 93d224b6…, sh020-image bb41ca66…, sh030-image 074a6141…, sh030-motion 005bfcc7…).
- sug-0007 + tracker đồng bộ sang café; tracker đổi key ep010-mo-hop → ep010-love-bombing.
- location.json date-cafe đã sửa (23/11): status approved, master_reference = v003-day (file giữ ở review/ để khỏi vỡ ref ep008); README location ghi chú v003-day.
- Chưa trả lời: áo dài Hồng Sen là cái nào (hồ sơ ep021 đang ghi hồng đậm). Chưa commit.

## 2026-11-23 — Làm 3 frame v1 (Richard gật, Flow huynhdn Pro, 0 credit)
- Project Flow mới: CNTM · EP010 · Love Bombing — https://flow.google.com/project/7162f595-d11b-49d7-aab5-47eae89dc6c9. Acc huynhdn Pro, không cần xác minh thiết bị, 470 credit nguyên (sửa ảnh 0 credit).
- Mỗi frame = 1 edit Nano Banana từ nền café v003-day khóa + mặt v002 làm ref phụ, prompt nguyên văn. sh010 đạt lượt 1, sh020 đạt lượt 2 (lượt 1 thiếu 1 ly nước cam), sh030 đạt lượt 1. Không gen video.
- File lưu byte-identical vào input/frames/: sh010-first-frame-v1.jpg = sh010-first-frame.jpg (sha cc0e7886…, 768×1376), sh020 (sha cd44e603…, 768×1376), sh030 (sha ca20fcb0…, 768×1376). Nền v003-day copy vào input/references/ + khai báo image_sources cả 3 shot. episode.yaml: flow_project + first_frame + frame_status pending_review (chờ Richard duyệt).
- QC của Bee trên file local: 3 frame cùng 1 người, cùng áo tím + short trắng, cùng quán/bàn/ghế — continuity tốt. sh010 có điện thoại trong tay + 2 ly nước cam; sh020 2 tay cầm điện thoại + 2 ly; sh030 nhìn thẳng camera deadpan, tay đặt bàn. Son/móng tự nhiên. Lưu ý trình Richard: (1) nốt ruồi cằm trái không thấy rõ ở cả 3 frame; (2) sh020/sh030 khung rộng hơn prompt yêu cầu (trung cảnh thay vì cận vừa/cận mặt); (3) dấu sao watermark Flow mờ ở mép khăn trải bàn cả 3 frame (watermark bắt buộc theo vùng, đã khóa bật, không gỡ bằng sửa lại được — như dấu sao Gemini ở ep008, lúc gen video sẽ crop).
- Chưa commit.

## 2026-11-23 — Frame v1 KHÔNG duyệt: áo tím lệch màu + 2 ly nước cam (Richard 07:27)
- Richard: "Cái áo tím này ở đâu vậy?? màu lạ thế" + "mà 1 cốc nước cam thôi, đi 1 người mà". Cả 2 đều đúng.
- Đo màu HLS (đừng tin mắt): áo mẫu LAHSTORE Tím H294 L81 S19 (tím oải hương rất nhạt); frame v1: sh010 H281 L50 S27, sh020 H287 L44 S25, sh030 H283 L45 S27 — hue gần đúng nhưng lightness lệch ~31-37 điểm, tím đậm + bão hòa hơn hẳn ảnh mẫu. Nguồn: cùng áo aff-0002 màu Tím, Flow render "màu tím" thành tím vừa thay vì tím nhạt pastel.
- Sửa prompt ảnh cả 3: "màu tím" → "màu tím nhạt pastel như ảnh mẫu" + thêm ảnh sản phẩm làm ref màu; "2 ly nước cam" → "1 ly nước cam" (sh010/sh020), sh030 thêm "1 ly nước cam". script.md + wardrobe.md cũng sửa "Tím" → "Tím nhạt". episode.yaml cập nhật SHA 3 prompt ảnh (sh010-image 5f07f3b4…, sh020-image 1e020f65…, sh030-image f4d44477…). Validator đạt.
- Làm lại frame v2 từ gốc (nền v003-day + mặt v002, KHÔNG sửa nối tiếp từ v1), 0 credit, trong cùng project EP010.

## 2026-11-23 — Frame v2 xong (sửa theo ý Richard, 0 credit)
- Làm lại từ gốc trong cùng project EP010, kèm ảnh sản phẩm làm ref màu. sh010 đạt lượt 1, sh020 đạt lượt 2 (lượt 1 model tự thêm kính tròn — loại, làm lại từ gốc + dặn không kính), sh030 đạt lượt 1.
- Đo lại màu HLS: v2 sh010 H286 L79 S15, sh020 H289 L76 S14, sh030 H287 L77 S16 — so với mẫu L81 S19 chỉ còn lệch 2-5 điểm lightness (v1 lệch 31-37). 1 ly nước cam cả 3 frame (đã đếm tay). File lưu byte-identical: sh010-first-frame-v2.jpg (sha b2601774…), sh020 (sha c25b905b…), sh030 (sha 357709a8…), 768×1376; file không phiên bản trỏ sang v2. episode.yaml cập nhật first_frame SHA v2, frame_status vẫn pending_review.
- QC của Bee: áo tím nhạt đúng mẫu; mặt/tóc khớp v002; son/móng tự nhiên; short trắng có. Lưu ý trình Richard: (1) sh010 My cầm điện thoại nhưng nhìn thẳng camera thay vì cúi lướt tin nhắn (khung kể chuyện, vẫn hợp); (2) nốt ruồi cằm trái vẫn không thấy rõ; (3) sh030 khung ngực trở lên, chưa cận mặt hẳn; (4) dấu sao watermark Flow còn mờ ở sh010/sh020 (sh030 không có).
- Chưa commit.

## 2026-11-23 — Richard DUYỆT cả 3 frame v2, lệnh gen 3 clip (07:57)
- episode.yaml: frame_status cả 3 → approved, approved_for_generation → true, editorial_status draft → script_approved. Validator --stage generation đạt.
- Gen: Frames trực tiếp từ frame v2 đã duyệt, Agent OFF, Veo 3.1 Lite 10cr/clip × 3 = 30 credit, 9:16, 8s, 1 output/shot, prompt motion nguyên văn.
- Ghi chú: sh020 CÓ thoại ("Tuần hai. Một tin. 'Dạo này bận quá.' Rồi im.", 10 từ) — script.md + episode.yaml + motion prompt đều khớp; không phải shot câm.
- Chưa commit.

## 2026-11-23 — Gen 3 clip take001 xong (30 credit Lite), QC Whisper base
- Frames-direct từ frame v2, Agent OFF, Veo 3.1 Lite 10cr/clip, 9:16, 8s (thực 7.93s), 1 output/shot. Clip ID: sh010 393a8d92…, sh020 e560258e…, sh030 ece56c2b…. Tải 1K về disk, lưu byte-identical vào generated/sh0{10,20,30}-take001.mp4.
- QC của Bee (không tin ASR trình duyệt): frame-diff + xem frame t=0.5s — cả 3 đúng take, mặt/quán/áo khớp frame v2, 1 ly nước cam; logo Veo góc dưới phải (crop lúc ghép). Whisper base (vi, prob 1.00): cả 3 câu ĐẦY ĐỦ đúng kịch bản — sh010 12 từ 0.1-4.7s, sh020 10 từ 0.0-6.4s (nghỉ 1.3s trước "Rồi im"), sh030 14 từ 0.6-6.3s (onset thật ~0.6s theo năng lượng 48k, Whisper smear về 0.00). Các lỗi nghe của Whisper đều là đồng âm/gộp số (Tuần→Toàn, năm mươi tin→50 tiên, Dạo→giáo, bận→bộn, im→em, áp→ác) — không phải thiếu từ hay nói sai. Giọng nữ, đúng hướng Bắc (tai Richard quyết cuối).
- episode.yaml: takes take001 cả 3 shot, status needs_review, file + SHA + note. Validator đạt.
- Chưa commit.

## 2026-11-23 — sh010 take001 REJECTED (mặt không giống), re-roll take002
- Richard 08:39: "shot01 mặt có vẻ không giống". Bee soi frame t=0.5/2/4/6s: đầu clip mặt còn giống frame v2, nhưng giữa clip Veo diễn quá đà — t~2s quay đầu cười lớn, t~4s cười phá lên nhắm tịt mắt + giơ cả 2 tay + đặt điện thoại xuống bàn. Lệch cả mặt lẫn hành động so với prompt (cầm điện thoại lướt tin, kể lại, bối rối nhưng hơi vui). take001 → rejected_editorial.
- sh020/sh030 soi thêm frame t=4s: mặt vẫn giữ, không trôi như sh010 — giữ nguyên take001 chờ duyệt.
- Re-roll sh010 take002 từ đúng frame v2 + prompt motion nguyên văn, Veo 3.1 Lite 10cr.

## 2026-11-23 — sh010 take002 xong, thoại OK nhưng vẫn cười lớn
- Re-roll từ frame v2 + prompt nguyên văn, Veo 3.1 Lite 10cr, clip ID 0eddbd03…. Tải 1K, lưu generated/sh010-take002.mp4 (sha 37575e50…).
- QC Bee: thoại ĐẦY ĐỦ (Whisper base: "tuần đầu 50 tiên 1 ngày" + "Anh chưa gặp ai như em", 12 từ, 0.0-2.0s + 2.8-4.5s) — ASR trình duyệt nghe nhầm "năm 2019" là sai, Whisper base khẳng định đủ chữ. Bình tĩnh hơn take001 (không giơ tay, không đặt điện thoại xuống bàn) NHƯNG vẫn cười lớn nhắm mắt ở ~2-4s, điện thoại rời khỏi tay từ ~4s — mặt vẫn lệch lúc cười. take002 needs_review, chưa duyệt.
- Richard 08:44 hỏi: phần chat nhiều có nên để màn hình điện thoại chỉ chat, không cần mặt? Đề xuất của Bee: CÓ — làm insert màn hình chat ở hậu kỳ (chữ thật, 0 credit, Veo vẽ chữ sẽ nhầm), chèn ~2s đầu sh010 trong lúc thoại "Tuần đầu, năm mươi tin một ngày", rồi cắt về mặt My lúc câu quote. Kèm quay take003 với prompt siết ("mỉm cười nhẹ, không cười lớn, tay cầm điện thoại suốt clip") để phần quote cũng bình tĩnh.

## 2026-11-23 — Richard CHỐT: làm màn hình chat + quay take003 (08:49)
- Insert màn hình chat: làm ở hậu kỳ bằng PIL (chữ thật, 0 credit), file edit/chat-insert-sh010.png (1080×1920): giao diện Messenger, tên "Anh ấy", pill xanh "50 tin nhắn mới", 10 bong bóng từ 06:12-06:31, câu cuối "Anh chưa gặp ai như em". Chèn ~2s đầu sh010 trong lúc thoại "Tuần đầu, năm mươi tin một ngày", rồi cắt về mặt My lúc câu quote. Chưa dùng — chờ take003 + duyệt take rồi mới ghép.
- take003: siết prompt motion sh010 — "mặt bối rối nhưng hơi vui" → "mặt bối rối, mỉm cười nhẹ nhàng, mắt mở, bình tĩnh, tay cầm điện thoại lướt tin nhắn suốt clip, không đặt điện thoại xuống". SHA mới d005095f… (take001/002 dùng prompt cũ 93d224b6…, ghi trong note từng take). Gen Veo 3.1 Lite 10cr từ frame v2.
- Insert chat: Richard 👍 08:56 (duyệt thiết kế, chờ ghép cùng take003).

## 2026-11-23 — sh010 take003 xong (prompt siết, bình tĩnh nhất)
- Gen từ frame v2 + prompt siết d005095f, Veo 3.1 Lite 10cr, clip ID 76b3a29a…. Tải 1K, lưu generated/sh010-take003.mp4 (sha 8ce3e34f…).
- QC Bee: thoại ĐẦY ĐỦ (Whisper base: "tuần đầu 50 tên 1 ngày" + "Anh chưa gặp ai như em", 12 từ, 0.0-2.4s + 3.0-5.6s; ASR trình duyệt nghe nhầm "Tình đầu năng ngơi" là sai). Bình tĩnh nhất 3 take: cầm điện thoại 2 tay suốt clip, không cười lớn, không giơ tay; mặt giữ ở t=2/6s; chỉ 1 khoảnh khắc mỉm cười nhắm mắt nhẹ ở ~4s lúc cúi xuống nhìn điện thoại. Đề xuất dùng take này. Trình Richard duyệt cả 3 take (sh010 take003 + sh020/sh030 take001).

## 2026-11-23 — Richard DUYỆT sh010 take003, chê sh030 chưa đủ hài (09:16)
- sh010 take003 → accepted ("Shot này ok").
- sh030 take001: Richard thấy đoạn cuối chưa đủ hài. Bee soi frame t=2/4/6s: hướng deadpan + gật đầu chậm trong prompt KHÔNG lên hình — mặt mở to kiểu ngạc nhiên ở ~6s, không có cái nhếch mép cười khẩy, không thấy gật đầu. Cái hài của câu chốt nằm ở độ tỉnh bơ tương phản với ẩn dụ quân sự, mà take này diễn như đang ngạc nhiên. Đề xuất: quay take002 siết prompt (mặt tỉnh bơ, nói chậm, xong nhếch mép cười khẩy + gật đầu chậm một cái), 10cr. Laugh Track 1 ở cuối vẫn giữ như kế hoạch, nhưng không cứu được diễn xuất phẳng — phải sửa ở take.

## 2026-11-23 — Richard CHỐT quay sh030 take002 (09:18)
- Siết prompt motion sh030 — "nhìn camera, gật đầu chậm, deadpan" → "nhìn thẳng camera, mặt tỉnh bơ, nói chậm rãi… Nói xong nhếch mép cười khẩy, gật đầu chậm một cái". SHA mới a485a3ee… (take001 dùng prompt cũ 005bfcc7…). Gen Veo 3.1 Lite 10cr từ frame v2.

## 2026-11-23 — sh030 take002 xong (deadpan lên hình, coda mềm)
- Gen từ frame v2 + prompt siết a485a3ee, Veo 3.1 Lite 10cr, clip ID 32d9d536…. Tải 1K, lưu generated/sh030-take002.mp4 (sha 8688d27b…).
- QC Bee: thoại ĐẦY ĐỦ (Whisper base: "dội bóng xong rút quân" + "chiến thuật quân sự đêm ác vào hẹn hò", 14 từ, 0.0-1.84s + 2.72-6.04s; bom→bóng, đem áp→đêm ác là lỗi đồng âm). DEADPAN LÊN HÌNH: mặt bình tĩnh xuyên câu, không còn miệng há to ngạc nhiên; cuối clip ~7.5s có nhịp khép — mỉm cười nhẹ, nhắm mắt, cúi đầu xuống — mềm hơn cái nhếch mép + gật đầu sắc nét trong prompt, nhưng là cái kết có ý. Đề xuất dùng take này kèm Laugh Track 1 ở cuối. Trình Richard duyệt cả 3 take (sh010 take003 + sh020 take001 + sh030 take002).

## 2026-11-23 — Richard DUYỆT CẢ 3 TAKE, GHÉP MASTER (09:25)
- Selected: sh010 take003 (accepted_editorial), sh020 take001 (accepted_editorial), sh030 take002 (accepted_editorial).
- Assembly: tải 2K upscale 3 take đã duyệt (browser) → crop logo Veo trước caption → chèn insert màn hình chat ~2.5s đầu sh010 (audio gốc giữ nguyên) → concat filter → giữ tiếng gốc cả 3 shot (nữ Bắc) → Remotion BasicCaptions boxed + SRT UTF-8 → Laugh Track 1 ở cuối sh030 → preview → render → QC → delivery/.

## 2026-11-23 — Richard: sh020 lồng clone ThaoMy (09:33)
- Richard nghe lại: chỉ sh010 + sh030 là giọng Bắc, sh020 không phải Bắc → lồng clone ThaoMy cho sh020 (wordalign như ep009, Richard duyệt 21/11). sh010/sh030 giữ tiếng gốc.
- Build script đổi sh020 source → generated/sh020-take001-dubbed.mp4 (video copy từ 2K + audio clone mono 48kHz, tiếng gốc tắt hẳn). Dub xây sau khi file 2K sh020 về; bản 2K đang tải (browser) vẫn cần cho cả 3 take.

## 2026-11-23 — Giọng clone sh020 gen xong trên Colab T4 (09:37)
- VieNeu v3 Turbo, preset ThaoMyVeo (enroll ref-clip2.wav), session ep010-dub, đã dừng sạch (không orphan). File: ~/workspace/colab-t4-test/ep010-dub/thaomy-ep010-sh020.wav (PCM 48kHz mono, 4.48s). Whisper base: đủ 10 từ đúng thứ tự ("Trần hai, một tin, dạo này bận quá." 0.00-2.74s + "Sửi im." 3.44-4.24s; Trần/Sửi là đồng âm). Script: ~/workspace/colab-t4-test/ep010_dub_thaomy.py.
- Lưu ý: `colab exec -f` đọc script ở LOCAL (không phải /content/ như tiền lệ ep009 ghi) — lần đầu lỗi FileNotFoundError, chạy lại bằng path local thì xong.
- Còn lại: wordalign (cần file 2K sh020 về) → generated/sh020-take001-dubbed.mp4.

## 2026-11-23 — File 2K về + lồng sh020 xong (09:49-09:52)
- 2K tải về 09:49 (browser, 3 upscale ~7 phút/clip, không paywall): sh010 take003 (6.8MB, sha 1a0dfe95…), sh020 take001 (6.1MB, sha 7a196f5a…), sh030 take002 (4.9MB, sha c542b146…), đều 1080×1920, 7.85s. Frame-diff 2K-vs-1K: 4.6-5.4 (đúng take; control sai take 15.13). Lưu generated/*-1080p.mp4.
- Icon Veo đo trên 2K (vùng góc phải dưới x720-1080/y1560-1920): sh010 + sh020 CÓ sparkle (~y1770) + chữ "Veo" (~y1880, x1020+); sh030 KHÔNG có icon ở vùng đó (khung toàn cảnh t=2.5/6 cũng không thấy). Crop thống nhất 960:1707:60:0 như ep008/ep009 — cắt icon ở sh010/sh020, chỉ mất khăn trải bàn trống ở sh030, giữ framing/scale đồng nhất qua hard cut.
- Dub sh020 wordalign xong: generated/sh020-take001-dubbed.mp4 (sha 526e7080…, 1080×1920, 7.85s, mono AAC 48kHz). 4 cụm stretch P1 1.346x / P2 1.667x / P3 1.170x / P4 0.875x. QC (edit/dub-qc-ep010.md): Whisper đủ 10 từ đúng cửa sổ, năng lượng ngoài cửa sổ = 0.000 tuyệt đối. ĐẠT theo chuẩn ep009.

## 2026-11-23 — Master 2K xong + QC đạt (11:13-11:30)
- Build lần 1 chết ~09:53: VM replacement giết job nền giữa chừng, assembly-raw.mp4 corrupt (thiếu moov). Build lại từ đầu 11:13-11:24 bằng `python3 -u edit/build_master_2k.py` (log unbuffered), exit 0.
- Master: delivery/ep010-master-2k.mp4 sha256 780df2bf9fcd57bd008f8f0e5978ca2512ccca20aed32954a037e4a8dfc2378f, 21.44s, 1080×1920 30fps, H.264, AAC 48kHz stereo, -14.99 LUFS (TP -1.00, LRA 5.80). SRT 3 cue theo shot. Chat insert 0-2.5s, cuts 6.3s / 13.4s, Laugh Track 1 từ ~19.6s + freeze tail.
- QC (edit/build2k/build-report.md): ffprobe đạt; frame means không có đoạn đen; energy đủ 3 shot, sh020 có khoảng lặng giữa cụm đúng wordalign; Whisper transcript đủ 3 thoại đúng cửa sổ (sai đồng âm quen thuộc); soi contact sheet + frame 1.0/3.0/6.5/13.6/21.3s — caption Boxed hiển thị đúng, cắt sạch, đuôi freeze giữ nụ cười nhắm mắt.
- WART đã báo Richard: caption Boxed đè lên khung chat 0-2.5s, che một phần bubble "Em rep anh đi mà". Fix nếu Richard muốn: tắt caption 0-2.5s, render lại chunk 0.
- build-report.md bản đầu còn text template ep009 (sh040, dubbed takes, "PROPOSED") — đã sửa tay 11:30, file master KHÔNG build lại. manifest.yaml: locked_duration_seconds 21.44, qc passed.
- Validator: --stage generation đạt. --stage edit báo 2 lỗi (mute_veo_native / voice preset) — DRIFT CŨ của validator, ep009 đã đăng cũng báo y hệt 2 lỗi này. Manifest giữ schema thật speakers.thao_my + policy theo shot (Richard chốt 09:33), KHÔNG ghi sai `mute_veo_native: true` chỉ để qua validator.

## 2026-11-23 — Richard DUYỆT master 11:29 + bìa
- Master duyệt ("không sao, duyệt được") — caption đè khung chat 0-2.5s được chấp nhận, không sửa.
- Bìa: frame 17.0s của master (My nhìn thẳng camera, mặt tỉnh bơ, mắt mở, caption 'CHIẾN THUẬT QUÂN' ngang ngực, không che mặt) → delivery/ep010-cover-thaomy.jpg (1080×1920). Đã soi 3 ứng viên: 5.5s nhắm mắt, 17.0s tốt nhất, 21.3s nhắm mắt cười nhẹ.
- Bộ đăng nháp đã trình Richard: TikTok caption "Dội bom xong rút quân. 😌" + #chuyennhathaomy #phimnganai #haiviet + dòng CC BY Laugh Track 1; Facebook thêm link aff-0002 áo linen https://s.shopee.vn/70LoresCVa (đích đã xác minh 19/11, chưa gắn bài nào). Đề xuất hẹn 19:00 thứ Tư 25/11 (nối ep008 23/11 + ep009 24/11). Chờ Richard chốt lịch + có commit hồ sơ ep010 không.

## 2026-11-23 — Đã hẹn đăng 19:00 thứ Tư 25/11 (13:00)
- TikTok @chuyennhathaomy: video ID 7711241440021531910 (https://www.tiktok.com/@chuyennhathaomy/video/7711241440021531910), hẹn "Nov 25, 7:00 PM (GMT+7)", Everyone, caption đúng 113 ký tự, nhãn AI bật ("Creator labeled as AI-generated"), bìa là ảnh cover JPG frame 17s đã upload (frame-picker không có đúng khung đó nên dùng file JPG). Không có scheduled-post ID riêng hiển thị.
- Facebook Page: scheduled post ID 1143610121744333, hẹn "Wed Nov 25, 7:00pm", Public, mô tả đúng (có link aff-0002 https://s.shopee.vn/70LoresCVa), thumbnail là ảnh cover JPG frame 17s (Upload image), có trong Scheduled + Planner. Không đọc được public reel ID lúc hẹn (chỉ có "Copy reel ID") — lấy lúc xác minh sau khi đăng.
- Nhãn AI Facebook: Business Suite web không có tùy chọn nhãn AI cho Reels (giới hạn đã biết, không tính là lỗi).
- 2 bài kia không đụng: TikTok/Facebook vẫn còn ep009 24/11 ("Tiết kiệm bảy trăm ngàn…") + ep008 23/11 ("Chia tay đi, yêu khổ quá…") nguyên vẹn. Lưu ý: lúc xác minh Facebook, bấm nhầm card Planner Wed 25 mở ra composer "Create post" trống — đã hủy không lưu, không tạo bài thừa (Wed 25 vẫn chỉ có 1 Reel).
- Cron xác minh `ep010-record-publication` đặt 19:20 25/11: kiểm tra lên sóng thật + ghi publications.csv (chỉ ghi khi có URL thật + bằng chứng).

## 2026-11-25 — ĐÃ LÊN SÓNG 19:00 + XÁC MINH (19:20-19:26)
- TikTok @chuyennhathaomy: ĐÃ ĐĂNG, public (Everyone), video ID 7711241440021531910 (https://www.tiktok.com/@chuyennhathaomy/video/7711241440021531910), create_time 19:00:00 +07 đúng giờ hẹn. Caption đúng 113 ký tự, nhãn AI bật ("Creator labeled as AI-generated", xác minh qua TikTok Studio). 6 views, 0 like, 0 comment lúc 19:21-19:26. Không lệch so với bản hẹn.
- Facebook Page: ĐÃ ĐĂNG, Public, reel thật ID 2185475262044414 — https://www.facebook.com/reel/2185475262044414/ (ID hẹn giờ 1143610121744333 chỉ là ID lịch hẹn; Business Suite content ID 1239287131764110). Mô tả đúng, có dòng link aff-0002 https://s.shopee.vn/70LoresCVa. 3 views (Business Suite Insights), 2 reactions lúc xác minh 19:25. Đã rời khỏi Scheduled (chỉ còn bài ep011 hẹn 26/11). Không lệch so với bản hẹn; nhãn AI không có trên web Business Suite (giới hạn đã biết, không tính lỗi).
- Like + comment aff-0002 với tư cách Page: kiểm tra trước — panel comment "No comments yet", chưa có comment nào nên không trùng. Đăng MỚI 1 comment 19:25 đúng câu duyệt "Áo sơ mi linen My mặc: https://s.shopee.vn/70LoresCVa" (comment ID 1162831226235299; URL https://www.facebook.com/reel/2185475262044414/?comment_id=1162831226235299). Like MỚI của Page cùng lúc (reactions 2 → 3, comment count 0 → 1). Ghi plc-0012 vào affiliate-placements.csv.
- Ghi publications.csv: 2 dòng tiktok + facebook (URL thật + bằng chứng trên).
