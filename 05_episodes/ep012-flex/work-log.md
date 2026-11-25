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
