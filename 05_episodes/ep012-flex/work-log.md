# Work log — ep012 'Flex'

## 2026-11-25 — Rebuild hồ sơ r03 (review 06:30 → chốt → rebuild)

### Vấn đề (review 06:30 25/11, verdict CHƯA ĐỦ)
- script.md r02 (18/11) là tập Flex (Hùng ↔ My, café, chốt "Đồng hồ limited mà chia bill ly cà phê") nhưng episode.yaml rev 1 + cả 8 prompt trong input/prompts/ lại là một tập khác hẳn — My độc thoại solo ở phòng khách trang trí lễ hội, chốt "Là tôi." Lỗi cùng loại ep011 hôm qua; gần như chắc là file sót sau lần renumber. Theme lễ hội đã có nhà ở ep016 Last Christmas.
- Số từ trong script.md sai 3/4 shot (đếm lại: sh020 16 không phải 15, sh030 15 không phải 14, sh040 14 không phải 13).
- Cả 4 shot đều 2 câu — phạm luật "1 shot, 1 câu trọn ý".
- "Xe mấy tỷ" vô hình (cảnh café, không thấy xe).
- edit/manifest.yaml còn plan âm thanh của concept cũ (mute_veo_native true, VieNeu-TTS).

### Quyết định của Richard (25/11, chat review ep012)
- 06:57: chốt concept Flex; trang phục "áo dài Thanh Nghi tiếp".
- 07:06: đổi trang phục sang áo dài Mai Linh, link aff https://s.shopee.vn/30ppBKBi6L + 10 ảnh (9 tấm riêng, 1 tấm trùng).
- 07:07: "4 câu thoại sửa ok"; "Location kiếm nơi khác đi" (không dùng date-cafe).
- 07:07: "Xe mấy tỉ từ sh010 ok" (giữ câu khoe xe).
- 07:07: "Giọng Hùng giữ nguyên native ok".
- 07:11: "không phải xác minh" (dừng xác minh link Shopee aff-0007); hỏi nhà hàng tối nên mặc màu gì.
- 07:11: Bee đề xuất đỏ đô cho nhà hàng tối; Richard "Duyệt" (07:12) → màu đỏ đô chốt.

### Rebuild r03 (25/11, subagent)
- script.md → r03: thoại 1 câu/shot đã duyệt (7/15/15/9 từ), sửa số tiếng, thêm chìa khóa xe trên bàn sh010, đổi trang phục Mai Linh đỏ đô + aff-0007, đổi bối cảnh nhà hàng buổi tối (đã duyệt 19/11), sửa plan âm thanh.
- episode.yaml → revision 2, title "Flex", editorial_status draft, 4 shot với thoại đã duyệt; approved_for_generation false, first_frame null, takes [].
- input/prompts/ (8 file): viết lại toàn bộ theo Flex; không còn tên tập cũ hay cụm "Không phụ đề"/"Không chữ trên màn hình" trong bất kỳ prompt nào; son đỏ + móng tự nhiên ghi trong mọi image prompt của My; sh010 có chìa khóa xe trên bàn.
- edit/manifest.yaml → revision 2: audio_plan mới (mute_veo_native false; My native-nếu-Bắc else clone ThaoMy wordalign; Hùng giữ native, không preset, không lồng ThaoMy); bỏ plan VieNeu-TTS/mute-all cũ.
- wardrobe.md (mới): Mai Linh đỏ đô + 3 ref đỏ + sha, aff-0007, son đỏ, móng tự nhiên, tóc xõa.
- input/references/restaurant-bg-wood.jpg: copy byte-identical từ 03_locations/restaurant-evening/approved/ (sha c035ab8e…, duyệt 19/11).
- 04_products/affiliate-links.csv: hàng aff-0007 đã có từ trước (kiểm tra: chỉ 1 hàng, không trùng).
- 02_characters/thao-my/wardrobe/REGISTRY.md: hàng Mai Linh đã có từ trước; cập nhật màu thành đỏ đô (chốt 25/11).
- 00_docs/production-tracker.csv: hàng ep012 cập nhật sang Flex r03 (tên + nội dung cũ xem git history).
- Validator: `python3 06_automation/validate_episode.py 05_episodes/ep012-flex` — ĐẠT, exit 0 ("Episode structure valid"). Ghi chú kèm: 4 first frame missing (chưa làm frame — đúng giai đoạn này); "VieNeu voice pending user choice" là ghi chú chung của validator khi voice_status != locked, không phải lỗi (voice_status ở đây là decided_by_user theo quyết định của Richard).
- Commit: `8b1a80a` "rebuild ep012 Flex profile (r03): approved dialogue, Mai Linh red, restaurant-evening, fix Noel leftover" — 26 files, pushed, verified on origin/main (97848cd..8b1a80a).

### Còn chờ (sau rebuild)
- Richard review lại hồ sơ rebuild rồi mới làm frame Nano Banana (0 credit) → duyệt frame → gen clip Veo 3 Lite.
- Trang phục Hùng chưa chốt (chỉ thấy lưng/tay) — chốt trước khi làm frame sh010/sh030.
- aff-0007 UNVERIFIED theo lệnh Richard (không xác minh, không thử lại) — chỉ gắn vào bài khi Richard xác nhận màu/link trên điện thoại của cậu ấy, nếu cậu ấy yêu cầu.

## 2026-11-25 11:02 — Frames v1 (Nano Banana, 0 credit)

- Project Flow mới: CNTM · EP012 · Flex — https://flow.google.com/project/1cc7499d-86b9-44a0-b084-306ff4856f81 (acc huynhdn Pro; không cần xác minh thiết bị).
- Mỗi frame 1 edit trực tiếp từ master, không nối tiếp. Mặt ThaoMy002 lấy lại qua picker từ project EP003; nền nhà hàng lấy lại qua picker từ EP006; chỉ upload 3 ref áo dài đỏ mới; body ref đã có sẵn trong EP006 nên không upload.
- 4 frame về đủ, đã verify file trên disk (768×1376) + xem trực tiếp, map byte-identical vào input/frames/ (sha trong episode.yaml), frame_status pending_review, approved_for_generation vẫn false — chờ Richard duyệt frame.
  - sh010-frame-v1.jpg (ffb31434…, 132.233 B): Hùng lưng/tay, sơ mi trắng, đồng hồ trên cổ tay giơ cao, ly trong tay, chìa khóa xe trên bàn gỗ. Nit: sao Gemini nhỏ góc phải dưới (như ep011 đã duyệt).
  - sh020-frame-v1.jpg (f5673908…, 172.048 B): My áo dài đỏ đô thêu hạc + cúc tàu tua rua, son đỏ, nốt ruồi cằm trái (đã kiểm bằng crop zoom), móng tự nhiên, nâng ly cà phê. Nit: sao Gemini nhỏ góc phải dưới.
  - sh030-frame-v1.jpg (89d2bb5e…, 120.413 B): Hùng lưng/tay, sơ mi trắng, đồng hồ, đẩy bìa hóa đơn đen có hóa đơn trắng qua bàn. Nit: chữ trên hóa đơn mờ, khó đọc (chữ giả nhỏ); sao Gemini nhỏ góc phải dưới.
  - sh040-frame-v1.jpg (bd12340f…, 172.200 B): My deadpan, điện thoại cầm 2 tay trên bàn, áo dài đỏ đô. Nit: son đỏ nhạt hơn sh020 rõ (hồng đất thay vì đỏ tươi); nốt ruồi cằm trái không rõ ở khung này; sao Gemini nhỏ góc phải dưới.
- Validator sau khi map frame: đạt (exit 0).

## 2026-11-25 ~11:15 — Kiểm tra áo dài đỏ vs mẫu Mai Linh (Richard hỏi)

- So sánh trực tiếp frame v1 với 3 ảnh mẫu đỏ (flatlay + mặc ngoài trời + mặc trong nhà) + đo màu HLS.
- ĐÚNG: màu đỏ cùng họ (đỏ đô), cổ trụ, cúc tàu trắng + tua rua, thêu hạc tone-on-tone.
- SAI — TAY ÁO: mẫu thật tay lỡ RỘNG, vải ĐỤC không xuyên thấu, kết thúc ở khuỷu, cẳng tay để trần. Frame v1 tay áo là VOAN XUYÊN THẤU (thấy rõ da tay), ôm tay, kéo dài tới cổ tay. Ảnh đối chiếu: workspace/ep012-sleeve-check-frame-sh020.png vs workspace/ep012-sleeve-check-sample-mai-linh.png.
- MÀU: đo HLS vùng ngực đủ sáng — mẫu L39 S32 H354; sh020 L22 S49 H13, sh040 L24 S53 H2. Frame đỏ tối/đậm hơn mẫu; một phần do đèn vàng nhà hàng tối, nhưng tay áo mới là lỗi cấu trúc rõ ràng.
- Hướng sửa (chờ Richard gật): làm lại sh020/sh040 từ master với prompt ghi rõ "tay lỡ rộng, vải đục không xuyên thấu, tay áo kết thúc ở khuỷu, cẳng tay để trần" + lấy ảnh mặc trong nhà làm ref chính (thấy rõ tay áo nhất). Giữ v1 làm lịch sử, chỉ thay khi v2 được duyệt.

## 2026-11-25 11:31 — Frames v2 cho sh020/sh040 (sửa tay áo + son)

- Prompt sửa (đã cập nhật file + sha trong episode.yaml, validator đạt): tay lỡ RỘNG, vải đục không xuyên thấu, tay áo kết thúc ở khuỷu tay, cẳng tay để trần; ref chính ảnh mặc trong nhà; son đỏ đậm.
- Làm mới 1 edit từ master trong project EP012 (không sửa nối tiếp từ v1), 0 credit, mỗi shot 1 lượt.
- sh020-frame-v2.jpg (56ab98a3…, 175.109 B): tay áo SỬA ĐÚNG — rộng, vải đục, hết ở khuỷu, cẳng tay trần; son đỏ đậm; mặt khớp v002; thêu hạc cùng màu đỏ chìm; cúc tàu + tua rua. Nit: sao Gemini nhỏ góc phải dưới; trên bàn có 2 ly cà phê (cảnh hẹn hò 2 người nên hợp lý).
- sh040-frame-v2.jpg (f5a6995d…, 181.422 B): tay áo SỬA ĐÚNG; son đỏ đậm (đỏ hơn v1 rõ); mặt khớp v002, deadpan, nốt ruồi cằm trái thấy rõ khi crop zoom; điện thoại cầm 2 tay. Nit: thêu hạc bằng chỉ TRẮNG/bạc nổi bật — mẫu thật thêu cùng màu đỏ chìm (sh020 v2 thì đúng); sao Gemini nhỏ góc phải dưới.
- v1 giữ lại làm lịch sử trong input/frames/. episode.yaml đã trỏ sh020/sh040 sang v2, frame_status vẫn pending_review — chờ Richard duyệt.

## 2026-11-25 11:43 — Frame v3 cho sh040 (thêu hạc trắng → cùng màu đỏ)

- Prompt sửa (đã cập nhật file + sha trong episode.yaml, validator đạt): thêu hạc cùng màu đỏ chìm, không dùng chỉ trắng hay bạc.
- Làm mới 1 edit từ master trong project EP012 (không sửa nối tiếp từ v2), 0 credit, 1 lượt.
- sh040-frame-v3.jpg (0cb787c1…, 162.230 B): thêu hạc SỬA ĐÚNG — cùng màu đỏ chìm, không còn chỉ trắng/bạc; tay áo vẫn đúng (rộng, vải đục, hết ở khuỷu, cẳng tay trần); son đỏ đậm; mặt khớp v002, deadpan, nốt ruồi cằm trái thấy rõ khi crop zoom; điện thoại cầm 2 tay.
- Nit mới: cúc tàu ở v3 thành màu ĐỎ ĐẬM thay vì trắng như mẫu (v2 thì cúc trắng đúng) — tua rua vẫn đỏ đậm như mẫu; nền có thêm 2 khách bàn bên, người phụ nữ bàn bên nhìn về phía máy (hơi phân tâm). v2 giữ lại làm lịch sử.
- episode.yaml đã trỏ sh040 sang v3, frame_status vẫn pending_review — chờ Richard duyệt cả 4 frame.

## 2026-11-25 11:49 — Frame v4 cho sh040 (cúc trắng + thêu chìm cùng lúc)

- Prompt sửa (đã cập nhật file + sha trong episode.yaml, validator đạt): cúc tàu trắng, tua rua đỏ đậm; thêu chìm không chỉ trắng/bạc cho phần thêu; nền mờ không khách khác.
- Làm mới 1 edit từ master trong project EP012 (không sửa nối tiếp từ v3/v2), 0 credit, 1 lượt.
- sh040-frame-v4.jpg (d93117b0…, 167.283 B): CẢ 2 CHI TIẾT ĐÚNG CÙNG LÚC — cúc tàu trắng rõ, tua rua đỏ đậm; thêu hạc cùng màu đỏ chìm, không còn chỉ trắng/bạc; tay áo vẫn đúng (rộng, vải đục, hết ở khuỷu, cẳng tay trần); son đỏ đậm; mặt khớp v002, deadpan, nốt ruồi cằm trái thấy được; điện thoại cầm 2 tay; nền mờ không khách khác, chỉ có vai Hùng (áo trắng, mờ) ở tiền cảnh phải — hợp bố cục đối thoại, không lộ mặt.
- Nit còn lại: sao Gemini nhỏ góc phải dưới (như mọi frame). v3 giữ lại làm lịch sử.
- episode.yaml đã trỏ sh040 sang v4, frame_status vẫn pending_review — chờ Richard duyệt cả 4 frame (sh010 v1, sh020 v2, sh030 v1, sh040 v4).

## 2026-11-25 11:54 — So màu sh020 v2 vs sh040 v4 với mẫu (Richard hỏi)

- Đo HLS (median pixel đỏ đậm, đã kiểm chứng patch bằng mắt — patch tay/điện thoại/bàn bỏ qua): mẫu flatlay H342 L25 S57; mẫu mặc trong nhà H350 L29 S58; sh020 v2 H356 L19 S75; sh040 v4 H356 L16 S64.
- Kết luận: hue gần như nhau ở cả 2 frame (H356, lệch mẫu 6–14°). Lệch chính ở LIGHTNESS: cả 2 frame đều tối + đậm hơn mẫu do ánh sáng nhà hàng tối — sh020 (L19) gần mẫu (L25–29) hơn sh040 (L16); sh040 cũng đậm hơn (S64 vs mẫu 57, sh020 S75 còn đậm hơn nữa).
- Verdict: **sh020 v2 giống mẫu hơn** (sáng hơn, gần mẫu hơn). Hướng sửa nếu làm lại: ghi rõ "đỏ đô sáng như ảnh mẫu, không tối sẫm" + lấy ảnh mặc trong nhà (sáng nhất, L29) làm ref chính.

## 2026-11-25 12:45 — Áp dụng: sh040 dùng chung frame sh020 (script r04)

- Richard "Áp dụng luôn": sh040 dùng chung frame sh020-frame-v2.jpg (màu giống mẫu hơn theo đo HLS 11:54). episode.yaml sh040 first_frame đã trỏ sang sh020-frame-v2.jpg (sha 56ab98a3…); sh040-frame-v4.jpg giữ lại làm lịch sử trong input/frames/; sh040-image.txt giữ nguyên làm lịch sử (không dùng gen nữa).
- Hành động sh040 đổi: "Rút điện thoại ra" → "Đặt ly cà phê xuống, nụ cười tắt dần, mặt lạnh lại" (script.md r04 + sh040-motion.txt mới, sha fd868ba1…). Thoại giữ nguyên 9 từ: "Đồng hồ limited mà chia bill ly cà phê."
- Frame set hiện tại: sh010 v1, sh020 v2, sh030 v1, sh040 = sh020 v2. frame_status vẫn pending_review — chờ Richard duyệt bộ frame rồi mới gen 4 clip (40 credit).

## 2026-11-25 13:34 — Gen 4 clip thử (Veo 3.1 Lite, 70 credit)

- Richard "gen thử đi": 7 lượt gen (sh010 ×2, sh020 ×2, sh030 ×1, sh040 ×2), 70 credit, số dư còn 330 (reset 13:49 16/12). Frames trực tiếp, Agent OFF, 9:16, 8s, 1 output. Chỉ tải 1K về review, chưa upscale 2K.
- Takes (generated/, episode.yaml, status needs_review — chờ Richard nghe + duyệt):
  - sh010 take001 (bb0ae194…, sha c2025577…): Whisper base "Em biết sẽ ăn máy tầy không?" — "xe anh mấy tỷ" nghe thành "sẽ ăn máy tầy". Onset 0.3s. Visual: Hùng xoay sang profile LỘ MẶT (frame gốc chỉ lưng) — trái quyết định "Hùng không mặt"; đồng hồ + chìa khóa rõ; không chữ giả.
  - sh020 take002 (0db8954a…, sha 4965ae3d…): Whisper base "Dạ hay quá anh, em uống lý cả phê 30.000, anh đừng lo" — gần đủ, chỉ "ly"→"lý". Onset 0.0s. Visual: mặt khớp v002, nâng ly rồi hạ ly; không chữ giả. Take sạch nhất.
  - sh030 take001 (b7f71761…, sha 379a5720…): Whisper base "Biêu đây rồi nè, em chuyển khoảng phần em nhé, anh gọi số tài khoảng" — "Bill"→"Biêu", "khoản"→"khoảng" ×2, "gửi"→"gọi". Onset 0.4s. Visual: Hùng xoay sang profile lộ mặt (như sh010); đẩy hóa đơn rõ; không chữ giả.
  - sh040 take002 (1a6905e2…, sha 9563430b…): Whisper base "Đồng hồ lý mết thích mà chia bíu lý cà phê" — "limited"→"lý mết thích", "bill"→"bíu" (2 từ tiếng Anh là lõi câu chốt). Onset 3.5s (muộn). Visual: đặt ly xuống đĩa + nụ cười tắt dần thành mặt nghiêm ĐÚNG r04; không chữ giả. Đề xuất: lồng clone ThaoMy nếu "limited/bill" không rõ.
- Lưu ý QC: lỗi thanh điệu ("ly"→"lý", "khoản"→"khoảng") xuất hiện ở cả 4 clip — có thể là Whisper base nghe nhầm thanh, không chắc giọng sai; tai Richard quyết. faster-whisper đã mất khỏi VM sau restart, đã cài lại bằng pip --user (PYTHONNOUSERSITE=1 nên phải chạy với PYTHONPATH=~/.local/lib/python3.12/site-packages).

## 2026-11-25 13:42 — Richard bắt 2 lỗi take (chưa sửa)

- LỖI 1 — cốc xuất hiện 2 lần: frame sh020 v2 có 2 ly cà phê cam giống hệt nhau — 1 trên tay My, 1 trên đĩa ngay trước mặt My (Bee QC lúc đầu ghi "có thể là ly của Hùng" — SAI, ly nằm phía My, đọc thành trùng lặp). Lỗi này theo cả sh020 + sh040 (dùng chung frame). Sửa: edit frame xóa ly trên bàn, giữ đĩa trống (để sh040 đặt ly xuống), rồi gen lại sh020 + sh040.
- LỖI 2 — Hùng 2 mặt khác nhau: sh010 take001 mặt trẻ, dài, không râu; sh030 take001 mặt già hơn, nặng hơn. Nguyên nhân: Hùng chưa có mặt khóa — 2 frame gốc đều quay lưng, Veo tự bịa mặt mỗi lần quay sang nói. Sửa: khóa 1 mặt làm chuẩn, dựng lại cả 2 frame sh010/sh030 cùng mặt đó, gen lại 2 clip.
- CHỜ Richard chọn mặt chuẩn (sh010 hay sh030) rồi làm cả 2 sửa + gen lại 4 clip (40 credit).

## 2026-11-25 13:45 — Richard chốt mặt Hùng = sh010

- Face reference đã lưu: input/references/hung-face-sh010-ref.png (crop mặt sh010 take001 lúc 5s, sha 7ec42098…).
- Đã giao trình duyệt sửa 3 frame (0 credit, chưa gen clip): sh020-frame-v3 (xóa ly trên bàn, giữ đĩa trống), sh010-frame-v2 + sh030-frame-v2 (hiện mặt Hùng 3/4 profile, khớp đúng mặt ref sh010). Chờ frame về → Bee QC → gen lại 4 clip (40 credit).

## 2026-11-25 13:53 — 3 frame sửa xong, Bee QC đạt

- sh020-frame-v3.jpg (sha 4f07d758…, PNG gốc convert JPG q95): ly trùng trên bàn ĐÃ XÓA, chỉ còn đĩa trống; ly trên tay My, mặt, son, áo dài, nền giữ nguyên. Dùng chung cho sh020 + sh040.
- sh010-frame-v2.jpg (sha 934a6b37…) + sh030-frame-v2.jpg (sha 9095ae0a…): mặt Hùng 3/4 profile khớp đúng ref sh010 — Bee soi crop mặt 2 frame cạnh nhau: cùng kiểu tóc, cùng tuổi, không râu. Đồng hồ + chìa khóa (sh010), hóa đơn (sh030) giữ nguyên.
- episode.yaml: first_frame đã trỏ frame mới cả 4 shot; hung-face-sh010-ref.png thêm vào image_sources sh010/sh030. Validator đạt (sẽ chạy trước commit).

## 2026-11-25 14:19 — Gen lại 4 clip (50 credit, số dư 280)

- 5 lượt gen (sh010 ×2, còn lại ×1), 50 credit. Takes mới (status needs_review): sh010 take004 (cc8b1904), sh020 take003 (c0f602e8), sh030 take002 (70e75a4f), sh040 take003 (5758d0ff).
- Whisper base QC:
  - sh010 take004: "xe anh mấy tỷ" lỗi CÓ HỆ THỐNG (4/4 lượt gen đều nghe thành "sẽ ăn mấy tầy") + LẶP CÂU thật ("Một mấy tầy không?" ở 4.5–5.4s, xác nhận bằng năng lượng âm thanh). Visual: mặt khớp ref, đồng hồ + chìa khóa rõ; nit: giơ 2 nắm đấm lên gần mặt lúc nói. KHÔNG chốt như hiện tại.
  - sh020 take003: sạch nhất — chỉ 1 ly (đĩa trống suốt clip), thoại gần đủ. Đề xuất CHỐT.
  - sh030 take002: mặt khớp ref, giống sh010; thoại "Bill/khoản/gửi" nghe nhầm như round 1. Đề xuất CHỐT nếu Richard nghe giọng OK.
  - sh040 take003: hình đúng r04 (đặt ly + mặt lạnh), chỉ 1 ly; "limited"/"bill" vẫn không rõ (2/2 round). Đề xuất lồng clone ThaoMy.
- Đang chờ Richard chốt take + hướng xử lý sh010 (lồng Minh Quân / dùng lại trial take001 / quay lại) và sh040 (lồng clone ThaoMy / quay lại).

## 2026-11-25 16:41 — Richard: làm lại frame váy

- Đo HLS: váy clip sh020 take003 H354 L15 S83 vs mẫu trong nhà H349 L28 S59 / flatlay H343 L27 S58 — kiểu váy đúng mẫu (cúc/tua/tay/thêu khớp), chỉ màu tối hơn 13 điểm lightness + đậm hơn 24 saturation. "Giống mẫu hơn" trước đó chỉ là so sh020 vs sh040, không phải so với mẫu.
- Đã giao sửa frame sh020 v4 (1 edit từ v3, 0 credit, kèm ảnh mẫu mặc trong nhà làm ref màu): váy sáng lên gần mẫu, giữ nền tối; sau đó gen lại sh020 + sh040 (20 credit).

## 2026-11-25 16:47 — Frame sh020 v4 xong, Bee QC đạt

- Váy sáng lên rõ: thân váy H352 L24 S71 (clip cũ L15 S83; mẫu L28 S59) — chỉ còn lệch 4 điểm lightness ở thân váy; tay áo L19 (vẫn tối hơn do góc/bóng). Thêu hạc nhìn rõ hơn.
- Còn lại giữ nguyên: mặt, son, ly trên tay, đĩa trống (1 ly), cúc tàu + tua, tay loe 3/4, nền nhà hàng tối.
- episode.yaml: sh020 + sh040 đã trỏ frame v4 (sha 134fa566…). Validator đạt (sẽ chạy trước commit).

## 2026-11-25 17:02 — Gen lại sh020 + sh040 từ frame v4 (30 credit, số dư 250)

- Takes mới: sh020 take004 (d0d2bd40), sh040 take004 (f76426ba, attempt 1/2; attempt 2 clip 79332fa5 không tải về).
- Whisper base: sh020 take004 sạch như cũ (chỉ 'ly'→'lý'); sh040 take004 'limited' NGHE RÕ lần đầu (onset 2.4s), chỉ 'bill'→'bíu'.
- BÀI HỌC MÀU MỚI: frame v4 đo L24 nhưng Veo gen clip ra L17 — Veo tự làm tối váy lại trong cảnh nhà hàng tối; sửa frame chỉ cứu được một phần (clip cũ L15 → clip mới L17). Muốn clip chạm L28 thì phải làm frame sáng quá mức, hiệu quả chưa chắc.
- sh040 take004 KHÔNG chốt được cho hành động: cả 2 attempt đều không đặt ly xuống (cầm ly đến hết clip), nụ cười không tắt hẳn. Đề xuất: dùng lại take003 round 2 (đặt ly + mặt lạnh đúng) + lồng clone ThaoMy.
- Đang chờ Richard chốt toàn bộ take + hướng xử lý sh010/sh040.

## 2026-11-25 17:31 — Richard chốt take (dùng tạm) + lồng tiếng

- Takes CHỐT (accepted_editorial): sh010 take001 (trial), sh020 take004, sh030 take002, sh040 take003.
- Giọng Nam: Richard 17:32 "giọng Nam ko phải lồng 2 shot Nam đều ok" — sh010 + sh030 giữ nguyên tiếng Veo gốc, KHÔNG lồng Minh Quân.
- Lồng clone ThaoMy wordalign cho cả 2 shot My: sh020 take004 + sh040 take003 (Richard: "lồng ThaoMy cho cả hai sh nhé").
- Dub đang làm theo pipeline ep010/ep011 (Colab T4 VieNeu Turbo preset ThaoMyVeo + build_wordalign).

## 2026-11-25 ~17:45 — Lồng tiếng clone ThaoMy wordalign XONG, QC ĐẠT (sh020 + sh040)

- Colab T4 session ep012-dub: VieNeu v3 Turbo, preset ThaoMyVeo (enroll ref-clip2.wav). 2 run riêng: sh020 wav 5.36s (sha 17da182d…), sh040 wav 4.16s (sha 01d211da…) — lưu ở ~/workspace/colab-t4-test/ep012-dub/.
- Native windows (energy 48kHz stereo + fine 0.02s): sh020 P1 1.02–1.90 / P2 2.40–4.05 / P3 4.56–5.18; sh040 P1 3.14–4.48 / P2 5.14–6.70. Ghi ở edit/sh020-native-windows.md + edit/sh040-native-windows.md.
- Stretch: sh020 0.746x / 0.809x / 1.069x; sh040 1.288x / 0.696x — đều trong khoảng 0.60x–1.70x. Build edit/build_wordalign_sh020.py + edit/build_wordalign_sh040.py.
- Bản lồng: generated/sh020-take004-dubbed.mp4 (sha 82f3da86…), generated/sh040-take003-dubbed.mp4 (sha c317193c…) — video copy nguyên (framemd5 IDENTICAL), audio thay hoàn toàn bằng clone mono 48kHz AAC 192k; năng lượng ngoài cửa sổ = 0.000.
- QC Whisper base: sh020 14/15 từ đúng thứ tự/cửa sổ (chỉ nhầm đồng âm "uống"→"muốn", "lo"→"lắm" — wav gốc nghe đúng); sh040 9/9 từ đúng thứ tự/cửa sổ — LƯU Ý: "limited" Whisper nghe thành "lim tế" cả trên wav gốc lẫn bản lồng, KHÔNG xác minh được bằng Whisper, cần tai Richard. Chi tiết: edit/dub-qc-ep012-sh020.md + edit/dub-qc-ep012-sh040.md.
- KHÔNG commit (theo lệnh) — episode.yaml / manifest.yaml chưa cập nhật, chờ review.

## 2026-11-25 19:29 — Richard duyệt 2 bản lồng ("ok đó") + lệnh cắt đầu đít

- Đang dựng master 1K preview theo pipeline ep011 (concat filter, Boxed captions, SRT, Laugh Track 1 cuối, loudnorm -14 LUFS): cắt đoạn thừa đầu/đít mỗi shot, GIỮ hành động (đầu sh040 đặt ly 0–3.14s + đầu sh010 giơ đồng hồ không cắt).

## 2026-11-25 ~20:10 — Master 1K preview XONG (QC đạt, chờ Richard duyệt)

- File: `delivery/ep012-master-1k.mp4` (8.482.794 bytes, sha256 `58ebfb7e…`, 720×1280, 30fps, H.264 yuv420p, AAC 48kHz stereo, 22.53s) + `delivery/ep012-subtitles.srt` (4 cues, UTF-8, khớp script đúng từng chữ).
- Script dựng: `edit/build_master_1k.py` (theo đúng pipeline ep011: concat FILTER, Remotion Boxed accent #F59E0B, Laugh Track 1 cuối, loudnorm I=-15.5, KHÔNG title card). Báo cáo: `edit/build-report-1k.md` (+ bản gốc `edit/build1k/build-report-1k.md`).
- Trims (đo bằng Whisper base + energy envelope 48kHz + xem frame 1fps, cắt phần thừa đầu/đít theo lệnh Richard 19:29):
  - sh010 take001 native: 0–3.4s (thoại 1.08–2.62s; giơ đồng hồ giữ nguyên, tay hạ xuống bàn ~3.4s; uống nước ~6–7s là đuôi Veo, cắt).
  - sh020 take004-dubbed: 0–5.5s (dub 1.02–5.18s; giữ nụ cười; hạ ly ~6–7s là đuôi, cắt).
  - sh030 take002 native: 0–4.7s (thoại 0.90–4.34s; đẩy bill xong ~3s, tay đặt trên folder; 3.2s giữ hình tĩnh còn lại cắt).
  - sh040 take003-dubbed: 0–7.0s (dub 3.14–6.70s; ĐẦU 0–3.14s đặt ly + nụ cười tắt dần KHÔNG cắt — hard constraint).
  - Tổng video 20.6s + Laugh Track 1 (khởi 20.68s) + freeze-frame 1.82s = 22.53s.
- Crop: `crop=640:1138:40:0` + lanczos lên 720×1280 — icon Veo (sparkle + chữ "Veo") đã xác minh có ở góc dưới-phải CẢ 4 file 1K, mép trên icon cách đường crop ~22px.
- QC (đo trên file cuối, không tin filter chain):
  - Whisper base trên master cuối: nghe đủ 46 từ script theo đúng thứ tự (47 token do "limited" tách 3 + "ba mươi ngàn" tách 2 — artifact ASR đã biết, tai Richard chốt cuối).
  - Frame means 51.7–88.7 (không đoạn đen); xem contact sheet + 2 frame cắt sh040: không chữ giả, không icon Veo, cắt sạch.
  - Loudnorm đo trên file cuối: I=-15.44 LUFS, TP=-0.98, LRA 6.70 (ep011 đo -14.92, ep010 -14.99 — bản này êm hơn ~0.5 LU; cùng filter I=-15.5 theo pipeline ep011).
  - Laugh per-channel: RMS L=0.1551 R=0.1551 (tỉ lệ 1.00), L−R/L+R=0.000, envelope correlation 1.000 — không rò 1 kênh (mix bằng numpy, KHÔNG adelay).
  - Caption: SRT khớp script đúng từng chữ (assert trong script). Fix caption sh020: Whisper nghe "cà phê" thành 1 từ "café" và "phê ba mươi" thành "30" — chia span "30" thành 3 phần (phê/ba/mươi); đã kiểm chứng bằng frame t=7.0s (MƯỜI highlight đúng lúc) và t=7.45s (NGÀN, highlight đúng lúc). sh040 chỉ còn "phê." nội suy timing (Whisper nghe "limited" thành 1 từ "limite").
- Build chạy 2 lần (run 1 exit 0 nhưng caption sh020 lệch 7 từ cuối do mapping vị trí; đã sửa fix + chạy lại run 2 exit 0, sha mới 58ebfb7e…). Log: `edit/build1k/build_master_1k.log` (run 1) + `edit/build1k/build_master_1k-run2.log` (run 2, bản cuối).
- KHÔNG commit — episode.yaml / manifest.yaml chưa cập nhật, chờ review. Bước tiếp theo sau khi Richard duyệt preview 1K: tải 2K upscale của 4 take đã chốt, đối chiếu frame với take 1K, dựng lại master 2K theo cùng script.

## 2026-11-25 20:21 — Richard bắt lỗi thoại sh020 ở master ("nghe ảo")

- Câu cũ "Dạ hay quá anh, em uống ly cà phê ba mươi ngàn, anh đừng lo." không trả lời câu hỏi về xe — nhảy từ xe sang cà phê không cầu nối.
- Richard chốt câu mới (option 1): "Mấy tỷ thì kệ anh, em uống ly cà phê ba mươi ngàn, anh đừng lo." (16 từ).
- script.md → r05; episode.yaml sh020 dialogue đổi theo; manifest words 46 → 47, qc reset not_run (master 1K cũ STALE).
- Làm lại: lồng lại sh020 (clone ThaoMy wordalign, cửa sổ cũ) + dựng lại master 1K. sh010/sh030/sh040 không đổi.

## 2026-11-25 20:21 — Richard chốt câu sh020 mới (r05) + lồng lại + dựng lại master 1K

- Câu mới (Richard chọn): "Mấy tỷ thì kệ anh, em uống ly cà phê ba mươi ngàn, anh đừng lo." (16 từ, script r05, commit b5295b6). Câu cũ "Dạ hay quá anh..." bị bắt lỗi ở master v1: không trả lời câu hỏi về xe, nhảy từ xe sang cà phê không cầu nối.
- JOB 1 — Lồng lại sh020 (Colab T4 session ep012-dub-r05, VieNeu v3 Turbo preset ThaoMyVeo; wav mới 5.84s, sha a64baf42…): cửa sổ native đo lại khớp y hệt r03 (P1 1.02–1.90 / P2 2.40–4.05 / P3 4.56–5.18). Stretch 0.647x / 0.809x / 0.660x, đều trong khoảng 0.60–1.70x. LƯU Ý: P1 phải cắt pause nội cụm 0.30s trên wav TTS ("Mấy tỷ thì" | "kệ anh") mới vào khoảng — nếu lấy slice liền mạch thì stretch 0.553x, ngoài khoảng. QC đạt: Whisper 16/16 từ đúng thứ tự, đúng cửa sổ; năng lượng ngoài cửa sổ 0.000; video framemd5 identical với take gốc. File lồng mới ghi đè generated/sh020-take004-dubbed.mp4 (sha 963882b5…, bản r03 cũ 82f3da86… giữ trong git history). Build: edit/build_wordalign_sh020_r05.py; báo cáo: edit/wordalign-sh020-r05-report.md, edit/dub-qc-ep012-sh020-r05.md.
- JOB 2 — Dựng lại master 1K preview r05 (edit/build_master_1k_r05.py): cùng trims (sh010 0–3.4s / sh020 0–5.5s / sh030 0–4.7s / sh040 0–7.0s), crop, Boxed, Laugh Track 1 cuối; script 47 từ. QC đạt: Whisper cuối nghe đủ 47 từ theo đúng thứ tự (46 token — "cà phê" gộp "café", "ba mươi ngàn" thành "30"+".000", "limited" tách 3 — artifact ASR đã biết); SRT khớp script từng chữ; không đoạn đen (frame means 51.7–88.9); không chữ giả/icon Veo (xem contact sheet); Laugh Track 1 2 kênh cân bằng (RMS L/R 1.00, correlation 1.000); LUFS -15.42. Master mới ghi đè delivery/ep012-master-1k.mp4 (22.51s, sha 12c9b33e…; v1 cũ 22.53s, sha 58ebfb7e… giữ trong git history). Báo cáo: edit/build-report-1k-r05.md.
- LƯU Ý QC (đã sửa trong lần chạy 2, không còn là lỗi): lần chạy 1 của master r05 bị lệch timing caption — sh020 14 token (café + 30 + .000) và sh040 "limited" tách 3 token, các nhánh fix cũ không bắt được, khiến caption sh020 lệch muộn 1 từ từ 'ba' trở đi, caption sh040 lệch sớm 1 từ, và Laugh Track 1 audible 20.02s chồng lên đuôi từ "phê" (20.10–20.32s). Đã sửa nhánh fix (sh020: tách café + 30 + map .000; sh040: gộp mọi fragment giữa "hồ" và "mà" thành "limited") và chạy lại toàn bộ — lần 2: sh020 16/16 từ khớp, sh040 'limited' gộp đúng, từ cuối 'phê.' kết 20.52s, laugh audible 20.67s (sạch). Chỉ còn 'phê.' sh040 nội suy timing như bản v1 (chuẩn đã chấp nhận).

## 2026-11-26 06:53 — sh020 take005 (re-gen for lip-sync) — QC của Bee
- Lý do: Richard 06:30 26/11 bắt sh020 mồm không khớp câu mới — take004 quay cho câu cũ, lồng clone không sửa được khẩu hình. Gen lại với câu r05 trong prompt để Veo vẽ mồm theo câu mới.
- Motion prompt sh020 sửa sang câu r05 (sha 3187bea2…), commit 3d74d80.
- Gen: Flow project EP012, frame v4, Frames-direct, Veo 3.1 Lite, 10cr. 3 lần submit đầu lỗi "unusual activity", chờ cooldown 5 phút rồi gen lại thành công — clip 6b1f178f-af02-4dae-bccb-6e124d998766, 1K tải về sess-920868313. Số dư ~240.
- File: generated/sh020-take005.mp4 (sha d5fb896c…, 7.93s, 720×1280).
- QC Bee (Whisper base + energy 48kHz + 1fps frames): 16/16 từ đúng thứ tự, cụm P1 0.62–1.96 / P2 2.44–3.80 / P3 4.12–4.78, onset 0.9s. Mặt khớp v4, CHỈ 1 LY trong tay, đĩa trống, không chữ giả, watermark Veo góc phải dưới (crop master loại được). Mồm cử động theo câu mới (gen native, không lồng).
- Giọng: trình duyệt báo nữ miền Bắc — tai Richard chốt cuối. Nếu Bắc thì giữ native, thay take004, dựng lại master; nếu không Bắc thì cần quyết lồng-hay-quay-lại (lồng sẽ lệch mồm trở lại).
- Take ghi episode.yaml status needs_review.

## 2026-11-26 ~07:00 — sh020 take005 dub (clone ThaoMy) + master 1K r06
- Lý do: Richard 06:56 26/11 "ok đó, lồng giọng ThaoMy là đc" — take005 gen native
  với câu r05 nhưng chốt lồng clone (không giữ native).
- Dub: TÁI DÙNG wav clone r05 (sha a64baf42…, không chạy Colab mới). Cửa sổ native
  take005 đo lại bằng energy 48kHz: P1 0.91-1.99 / P2 2.41-3.99 / P3 4.29-4.91
  (take005 nói nhanh hơn take004 ~0.3s). Stretch 0.794x/0.786x/0.674x, trong
  khoảng 0.60-1.70. Output generated/sh020-take005-dubbed.mp4 (sha 60f66835…,
  7.93s). QC ĐẠT: Whisper 15 token cho 16 từ đúng thứ tự đúng cửa sổ (artifact
  quen thuộc: "ba mươi ngàn"→"30"+".000", "phê"→"xe", "lo"→"lâu"); năng lượng
  ngoài cửa sổ 0.000; framemd5 video identical take005 (4af9ba31…); peak 0.430.
  Script: edit/build_wordalign_sh020_take005.py; báo cáo:
  edit/wordalign-sh020-take005-report.md, edit/dub-qc-ep012-sh020-take005.md,
  edit/sh020-take005-native-windows.md. Take004 + take004-dubbed không động vào.
- Master 1K r06: pipeline như r05 (concat FILTER, Remotion Boxed #F59E0B, 3 chunk
  ≤287 frames concurrency 1, Laugh Track 1 cuối, loudnorm I=-15.5, crop
  640:1138:40:0). Takes: sh010 take001 native 0-3.4s / sh020 take005-DUBBED
  0-5.3s (thoại hết 4.91s, beat 0.39s, hạ ly ~6.0s là tail nên cắt) / sh030
  take002 native 0-4.7s / sh040 take003-dubbed 0-7.0s (giữ nguyên đầu đặt ly).
  Output GHI ĐÈ delivery/ep012-master-1k.mp4 (sha 7e39bea2…, 22.14s) +
  delivery/ep012-subtitles.srt (4 cue, khớp script r05 chính xác). Script:
  edit/build_master_1k_r06.py; báo cáo: edit/build-report-1k-r06.md.
- QC master ĐẠT: Whisper 46 token cho 47 từ đúng thứ tự (artifact quen thuộc:
  "cà phê"→"café", "ba mươi ngàn"→"30"+".000", "limited" tách 3 mảnh — đã merge);
  LUFS đo trên file cuối I=-15.41, TP=-1.00, LRA 6.60; không đoạn đen
  (frame mean 51.7-89); không chữ giả / không icon Veo (contact sheet đã xem);
  laugh 2 kênh cân bằng tuyệt đối (RMS L/R 1.00, L-R/L+R 0.000, envelope corr
  1.000), nghe rõ 20.30s sau từ cuối 20.15s; caption 47 từ, fix sh020/sh040
  đều chạy. Lưu ý (như r05): từ 'phê.' cuối sh040 timing nội suy
  (19.89-20.15 vs nói thật ~19.68-20.00), trễ ~0.2-0.3s trong lúc deadpan hold;
  caption "LO." giữ ~0.4s vào beat cười rồi biến đúng lúc cắt sang sh030 —
  hành vi của component Boxed, giống hệt r05, không phải lỗi.
- CHƯA làm: chưa commit, chưa sửa episode.yaml/manifest.yaml (Bee làm sau khi review).

## 2026-11-26 ~07:40 — master 1K r07 (title card "FLEX") — QC của Bee
- Chỉ thêm title card "FLEX" so với r06 (Richard 07:25 26/11 duyệt r06 + chốt "FLEX", bỏ "XE MẤY TỶ"). Style y hệt ep004/ep008: Remotion TitleCard (src/TitleCard.tsx, props accent #F59E0B + title "FLEX" + titleSeconds 2), chữ Inter 900 trắng viền đen + gạch accent cam dưới chữ, dải trên, 0–2s đầu sh010.
- Takes/trims/crop/captions/laugh/loudnorm y hệt r06. File: delivery/ep012-master-1k.mp4 (sha c2b0abec…, 22.14s) + copy tên riêng delivery/ep012-master-1k-r07.mp4 (sha khớp). SRT không đổi (sha 474d7177…, 4 cue).
- QC: frame 0.5s/1.5s — "FLEX" rõ, dải trên, KHÔNG che mặt Hùng, KHÔNG che đồng hồ/chìa khóa, không đè caption Boxed (caption "EM BIẾT XE" ở dưới, tách hẳn). Whisper 46 token cho 47 từ đúng thứ tự (artifact quen: "cà phê"→"café", "ba mươi ngàn"→"30"+".000", "limited"→3 mảnh). Không đoạn đen (mean 51.7–89.9). Không chữ giả / không icon Veo. Laugh 2 kênh cân bằng (RMS L/R 1.00, corr 1.000). LUFS I=-15.41, TP=-1.00, LRA 6.60.
- Script: edit/build_master_1k_r07.py; report: edit/build-report-1k-r07.md (bản trong edit/build1k/ giống hệt).
