# Work log ep004

## 2026-11-18 — Codex, sửa kịch bản theo yêu cầu trong chat

- Sửa tình huống: chia tiền sốt theo lượt chấm 3/2; ba shot, lần lượt 14/11/11 tiếng (đếm theo khoảng trắng). Chưa thử giọng.
- Người dùng chốt váy affiliate màu hồng, aff-0001. Chưa duyệt frame/gen.
- Đồng bộ episode r02, prompt và manifest từ hồ sơ cũ “Không có anh”; giữ bản trước sửa trong prep/before-chia-bill-r02. Chưa có take, chưa nhận phân công tài khoản Muse hoặc thao tác Flow.

## 2026-11-18 — Duyệt ảnh Bằng

Người dùng duyệt bang-front-v001.jpg trong chat. File đã có ở approved trước thao tác; cập nhật hồ sơ nhân vật, SHA-256 và tham chiếu ep004; copy nguyên byte vào input/references cho sh010. Không đổi thoại, không duyệt frame/location hoặc gen video.

## 2026-11-18 — Sửa r03 thành đối thoại trực tiếp

Người dùng yêu cầu hai người nói với nhau. Đổi sang Bằng → My → Bằng → My, mỗi shot một người nói, bốn clip nguồn 8 giây. Giữ váy My hồng aff-0001 và ảnh Bằng đã duyệt; sửa lại tham chiếu cũ còn ghi review trong script. Đồng bộ prompt, nguồn theo người nói, episode và manifest r03. Giọng Bằng chưa chốt. Chưa thử giọng, gen frame/video hoặc render.

## 2026-11-18 — r04, gợi nhớ vụ Kenh14

Theo phản hồi người dùng, bỏ tình huống nước chấm. Tra cứu Kenh14 thấy bài 72k ngày 17/04/2026 (người dùng nhắc 62k); lưu nguồn trong script. Viết đối thoại hư cấu qua điện thoại gần 1h sáng, có chi tiết QR và Facebook; giữ My mặc váy hồng aff-0001. Bốn câu ngắn, chưa thử giọng. Đồng bộ prompt/episode/manifest r04; lưu r03. Chưa duyệt gen, chưa tạo media.

## 2026-11-18 — Chốt thoại cuộc gọi r05

Người dùng trả lời “ok đó” cho bản đối thoại kết “Rẻ hơn phí đi nhầm chồng.” Lưu đúng bốn câu đã duyệt, đồng bộ episode/prompt/manifest r05; giữ My mặc SANJOLI hồng aff-0001. Lưu r04 trong prep/before-approved-call-r05/. Chỉ duyệt kịch bản, chưa duyệt frame/gen; chưa thử giọng hoặc tạo media.

## 2026-11-18 — Bee (Muse), sửa prompt r05 trước gen theo review

- Viết lại 4 motion prompt sang tiếng Anh ngắn theo mẫu ep003 (một hành động + thoại nguyên văn + hướng giọng + máy tĩnh), bỏ toàn bộ phủ định "không nhạc, không phụ đề, không chữ" (đã chứng minh gây phụ đề giả trên Veo). Thoại không đổi chữ nào.
- Sửa mâu thuẫn frame/motion: hóa đơn để trên bàn, không cầm tay (sh010); sh030 thống nhất "tỉnh bơ" ở cả image và motion (bỏ "sốt ruột" ở image); sh020 bỏ "nhấc điện thoại" (frame đã áp tai). Đồng bộ 2 ô hành động tương ứng trong storyboard script.md.
- Viết lại 4 image prompt sang tiếng Anh theo mẫu ep003: khóa mặt/tóc/kính/đồ chi tiết (Bằng: kính gọng mảnh chữ nhật, tóc rẽ ngôi, sơ mi xanh nhạt; My: mặt/tóc/nốt ruồi cằm trái, váy hồng satin 2 dây), giữ "No text, no logos" như ep003; bỏ ghi chú "chưa duyệt frame/location" ra khỏi nội dung prompt.
- Đồng bộ lại SHA-256 của 8 prompt trong episode.yaml; revision giữ 5 (chưa gen). Validator cấu trúc đạt; generation gate vẫn chặn đúng (chưa duyệt frame/gen). Giọng Bằng vẫn chưa chốt.

## 2026-11-18 — Bee (Muse), duyệt frame v1

- Người dùng duyệt cả 4 frame v1 trong chat. Chép nguyên byte vào input/frames/ (sh010/sh020/sh030/sh040-first-frame.jpg), ghi first_frame + SHA-256 vào episode.yaml, frame_status approved, approved_for_generation true cả 4; flow_project ghi URL project 'CNTM · EP004 · Chia Bill' (b19785af). editorial_status giữ script_approved vì chưa có lệnh gen. Validator đạt cả default và generation gate. Giọng Bằng vẫn chưa chốt; gen chưa chạy.

## 2026-11-18 — Bee (Muse), lệnh gen 4 clip native

- Người dùng lệnh gen 4 clip với giọng native trước, chốt giọng lồng sau (2 giọng test Minh Quân/Thiện Minh đã gửi, chưa chốt). editorial_status script_approved → generating; tracker cập nhật. Gen trong Flow acc huynhdn Pro, project 'CNTM · EP004 · Chia Bill' (b19785af): Frames trực tiếp, Agent tắt, Veo 3.1 Lite, 9:16, 8s, 1 output, prompt motion nguyên văn, frame đầu = file local đã duyệt đính kèm trực tiếp. Dự kiến 40 credit (930→890). Chỉ tải bản 1K để review; chưa có clip.

## 2026-11-18 — Bee (Muse), gen 4 clip v1 + QC

- Gen xong 4 clip Frames trực tiếp, Veo 3.1 Lite, 40 credit (930→890), không clip nào bị chặn. Flow ID: sh010 85725ac7-5767-4ab0-8644-549b94136ae8, sh020 b6cd5b64-b945-4bb0-a127-945c58770dfd, sh030 fc8d53ff-2650-463b-9db1-65d5040f4dc2, sh040 7bc890b2-7466-44e9-806a-623ed05ae896. Lượt tải đầu chỉ hiện toast, không có file trên đĩa; tải lại trong cùng task thì đủ 4 file 720p/24fps/7,93s tại ~/workspace/ep004-chia-bill-clips/. SHA-256: sh010 6471701bc69fdcca68c4c6c1ac593501328e394f34926fe87a550f06e35fad70, sh020 6cc9dfe17af73fea40a3311b2b2214f7219485ff5ae3e6dcaa95dc4593974f29, sh030 ce4fe561d0707b5fd417dfc27625cab7cfa2428632cc0bf4bed73469451cf1eb, sh040 a10a93bf9cc9a7bec2f52f8da64dc89bdaea60ce2615fe5e81d7ff5f3cf92660.
- QC local (frame 0,5/2,5/5,0/7,0/7,85s + Whisper base + đo F0): cả 4 đúng người/khung frame, đủ thoại, không phụ đề giả, đuôi sạch không bóng ma; watermark Veo + sao Gemini góc dưới-phải (crop lúc dựng). Giọng native: sh010 nam F0 ~151Hz, sh030 nam F0 ~124Hz (2 take khác giọng nhau), sh020 nữ F0 ~234Hz, sh040 F0 ~199Hz dao động rộng; giọng miền Bắc/Nam chưa xác minh bằng máy — chờ người dùng nghe tai thật. Đang chờ duyệt clip; chưa lồng, chưa lấy 2K.

## 2026-11-18 — Bee (Muse), frame v2 của Bằng + lệnh gen lại 2 clip

- Người dùng nghe clip thấy Veo đọc "72k" thay vì "bảy mươi hai nghìn" (chưa rõ clip nào); đề xuất viết lại thoại kiểu chào hỏi rồi chốt GIỮ bản r05. Người dùng thấy mặt Bằng chưa hợp dạng keo kiệt; Bee gen 3 mặt mới (A sắc/lạnh, B gầy/khắc khổ, C nhạt/bình thường) — cả 3 đều không lấy; chốt GIỮ ảnh master cũ, chỉ sửa biểu cảm tốt hơn.
- Dựng lại 2 frame v2 trong Flow (0 credit), mỗi frame 1 lượt sửa duy nhất trực tiếp từ master gốc bang-front-v001.jpg, mặt/kính/tóc/đồ giữ nguyên: sh010 v2 biểu cảm tính toán (nheo mắt, môi mím, cau nhẹ, nhìn hóa đơn); sh030 v2 tỉnh bơ (mặt phẳng, mắt lim dim, môi khép). Prompt sửa ảnh thực tế dùng cho v2 (khác file image prompt trong repo ở câu biểu cảm): sh010 "…looking down at a bill lying flat on the table… Expression: calculating — slight squint at the bill, lips pressed closed, faint frown of concentration, cold and unbothered, no smile…"; sh030 "…right hand resting on a bill lying flat on the table, laptop and open notebook on the desk… Expression: deadpan — flat face, half-lidded tired eyes looking down at the bill, lips closed, completely unbothered, no smile…". Khung v2 hơi rộng hơn v1 (thấy nhiều bàn/kệ hơn) — đã báo người dùng khi trình duyệt.
- Người dùng DUYỆT cả 2 frame v2 trong chat. Chép nguyên byte vào input/frames/ dạng file riêng sh010-first-frame-v2.jpg (SHA-256 4bb095d2118c397d45304c87a0a760a0bbe44ff7b4fc19f750ca3cb1553fd4c7) và sh030-first-frame-v2.jpg (SHA-256 41085e811be1e91a9278677e1486c2186a6ce1f5c5a9b3148a90d3f24b5b70f1); file v1 giữ nguyên, không ghi đè. episode.yaml: first_frame của sh010/sh030 trỏ sang file v2 + SHA-256 mới; revision giữ 5 (thoại không đổi); motion prompt giữ nguyên văn, không sửa.
- Lệnh gen lại 2 clip sh010 + sh030 (clip của My giữ nguyên): Frames trực tiếp, Agent tắt, Veo 3.1 Lite, 9:16, 8s, 1 output, prompt motion nguyên văn, frame đầu = file v2 đính kèm trực tiếp. Dự kiến 20 credit (890→870). Chỉ tải bản 1K để review. Còn chờ: clip nào đọc "72k", chốt giọng Bằng (Minh Quân/Thiện Minh), xác minh giọng miền 4 clip.

## 2026-11-18 — Bee (Muse), gen lại 2 clip Bằng take 2 + QC

- Gen xong 2 clip từ frame v2, Frames trực tiếp, Veo 3.1 Lite, 20 credit (890→870), không chặn. Flow ID: sh010 b7d66917-1a02-4467-b3e7-4ee5826c3ff3, sh030 bb96136c-3c84-4c4a-8ac8-d7c9d649d702. File 720p/24fps/7,93s tại ~/workspace/ep004-chia-bill-clips/sh010-take002.mp4 (SHA-256 0f6b657bab83e565d6d41ebfc2f045442f89950a6a0a53d7f8986776b5807fb9) và sh030-take002.mp4 (SHA-256 8fa9237c080136c759067c28fc823e92a82b5ce40efb0493433b0f8b3531ba82). Ánh xạ file↔shot đã kiểm chứng bằng thoại trong clip, không tin tên file tải về (picker từng mặc định nhầm frame sh040/sh010 v2 lúc gen, nhưng preview đã kiểm tra trước khi bấm).
- QC local (contact sheet 0,5/2,5/5,0/7,0/7,85s + Whisper base + đo F0): cả 2 đúng người/khung v2, biểu cảm đạt (sh010 cau mày tính toán, sh030 tỉnh bơ), không phụ đề giả, đuôi sạch không bóng ma; watermark Veo + sao Gemini góc dưới-phải (crop lúc dựng). sh030 đủ thoại. sh010: máy nghe câu 2 rõ ("Anh gửi mã rồi") nhưng cụm số nghe rất nhảm ("7-2-2-2-1") — KHÔNG kết luận được bằng máy là Veo đọc đúng "bảy mươi hai nghìn" hay đọc sai, chờ người dùng nghe tai thật. Giọng native 2 take vẫn khác nhau (F0 ~169Hz vs ~130Hz) nên gần như chắc phải lồng 1 giọng thống nhất cho Bằng; giọng lồng vẫn chưa chốt. Đang chờ duyệt clip; chưa lồng, chưa lấy 2K.

## 2026-11-18 — Bee (Muse), duyệt take 2 + lồng giọng sh030 sang sh010

- Người dùng DUYỆT 2 clip take 2 và lệnh lấy giọng clip 2 (sh030 take 2) gán vào clip 1 (sh010 take 2). Giọng Bằng từ nay là giọng này; 2 giọng test Minh Quân/Thiện Minh không dùng nữa.
- Clone giọng: enroll "BangTake2" bằng VieNeu Turbo từ tiếng native sh030 take 2 (cắt 0–4,2s, 48kHz mono, file dub/ref-bang-sh030take2.wav). Gen 2 câu riêng: "Em chuyển anh bảy mươi hai nghìn nhé." (thoại thật 0,06–1,45s, F0 ~135Hz) và "Anh gửi mã rồi." (0,06–0,75s, F0 ~123Hz) — khớp giọng gốc sh030 (F0 ~130Hz), khác hẳn native sh010 (F0 ~169Hz).
- Lồng khô: tắt hẳn tiếng gốc sh010, đặt 2 câu clone theo đúng cửa sổ miệng native đo bằng năng lượng (câu 1 bắt đầu 0,85s, câu 2 bắt đầu 4,00s), track đệm silence dựng sẵn bằng numpy, chuẩn hoá âm lượng theo RMS thoại gốc. Kiểm chứng trên file đã mux: khoảng lặng 0 tuyệt đối (không rò tiếng gốc), thoại đúng 2 cửa sổ, Whisper nghe đúng 2 câu (số tự chuẩn hoá "72,000" như mọi khi — TTS đọc theo text chữ nên không đọc tắt). File: sh010-take002-dub-bangtake2.mp4 (7,93s, 720p). Đang chờ người dùng duyệt bản lồng. Clip của My (sh020/sh040 take 1) vẫn chưa duyệt.

## 2026-11-18 — Bee (Muse), duyệt bản lồng sh010

- Người dùng DUYỆT bản lồng sh010 take 2 (giọng clone BangTake2). Chốt xử lý tiếng cho Bằng: sh010 = take 2 lồng clone, sh030 = take 2 giữ tiếng Veo gốc. Còn chờ duyệt 2 clip của My (sh020/sh040 take 1) và xác minh sh040 đọc đúng "bảy mươi hai nghìn" + giọng miền Bắc/Nam của 2 clip My.

## 2026-11-18 — Bee (Muse), lồng sh040 bằng giọng ThaoMyVeo

- Người dùng lệnh lồng clip Thảo My cuối (sh040) bằng giọng ThaoMy đã train. Clone ThaoMyVeo (VieNeu Turbo, enroll ref-clip2.wav), gen 2 câu riêng: "Ừ, bảy mươi hai nghìn." (thoại 0,08–1,56s, F0 ~242Hz) và "Rẻ hơn phí đi nhầm chồng." (0,17–1,90s, F0 ~239Hz), đặt theo đúng cửa sổ miệng native đo bằng năng lượng (câu 1 bắt đầu 0,60s, câu 2 bắt đầu 2,90s).
- Khác bản lồng khô sh010: bản này GIỮ tiếng nền đầu clip (0–0,5s) và tiếng cười/tiếng nền đuôi clip (4,6s trở đi) của bản gốc, chỉ thay vùng có thoại (0,55–4,35s) bằng im lặng + clone, nối bằng fade 0,05s. Câu 2 dài hơn nhịp miệng gốc ~0,3s (kết thúc 4,63s so với miệng dừng ~4,3s), không tăng tốc để giữ nhịp đọc tự nhiên — đã báo người dùng khi trình duyệt. Kiểm chứng trên file đã mux: Whisper nghe đúng 2 câu, không rò tiếng gốc, khoảng lặng giữa 2 câu gần như tuyệt đối. File: sh040-take001-dub-thaomy.mp4 (7,93s, 720p). Đang chờ duyệt. Chỉ còn sh020 chưa duyệt.

## 2026-11-18 — Bee (Muse), duyệt bản lồng sh040

- Người dùng DUYỆT bản lồng sh040 take 1 (clone ThaoMyVeo, giữ tiếng cười đuôi clip). Đã chốt 3/4 shot: sh010 = take 2 lồng clone BangTake2, sh030 = take 2 giữ tiếng gốc, sh040 = take 1 lồng clone ThaoMyVeo. Chỉ còn sh020 (take 1, tiếng gốc) chưa duyệt và chưa xác minh giọng miền.

## 2026-11-18 — Bee (Muse), duyệt sh020, chốt đủ 4 shot

- Người dùng DUYỆT sh020 take 1 giữ tiếng Veo gốc (giọng Bắc). Chốt toàn bộ: sh010 = take 2 lồng clone BangTake2, sh020 = take 1 tiếng gốc, sh030 = take 2 tiếng gốc, sh040 = take 1 lồng clone ThaoMyVeo. Bước tiếp: lấy bản 1080p upscale của 4 take đã chốt rồi dựng (caption Boxed, crop watermark, 1 laugh SFX cuối). Hồ sơ ep004 vẫn chỉ ở máy local, chưa commit/push.

## 2026-11-18 — Bee (Muse), dựng master ep004

- Lấy bản 1080p upscale (0 credit) của đúng 4 take đã chốt; verify trực tiếp trên file: cả 4 đều 1080×1920/24fps/7,85s, thoại khớp shot, timing audio trùng bản 720p từng bucket nên track lồng chuyển sang không lệch. SHA-256 2K: sh010 f59d3acc…, sh020 0b15be48…, sh030 1ded2d25…, sh040 3276b517… (đủ trong log build).
- Stage 1: trim sh010 6,5s (lồng) / sh020 6,5s (gốc) / sh030 6,0s (gốc) / sh040 7,0s (lồng), crop 960:1707:60:0 + lanczos 1080×1920, concat filter, loudnorm. Lần chạy đầu bị restart service giữa chừng, chạy lại thì xong (EXIT 0).
- Title "CHIA TIỀN": thêm component TitleCard mới vào project Remotion (hiện 2s đầu, dải trên, chữ trắng viền đen + gạch hổ phách; tsc đạt). Người dùng dặn không được lấp đầu nhân vật — đã đo đầu thật trên frame 2K và soi frame render: chữ nằm trên đầu, hở ~100px, mờ dần ở 1,9s, hết ở 2,2s.
- Caption Boxed #F59E0B: 47 từ, Whisper base đếm khớp kịch bản từng shot (12/13/11/11), refine bằng năng lượng. Render Remotion 626 frame, EXIT 0.
- Stage 3: đuôi 7,0s của sh040 dài hơn stem Laugh Track 1 (2,10s) nên freeze âm — đã cắt đuôi bản Boxed còn 25,12s rồi mới gắn Laugh (nghe từ 23,76s) + freeze 0,48s + loudnorm. Master: ep004-chia-bill-boxed-laughtrack1.mp4 (25,62s, 1080×1920, -14,81 LUFS/TP -0,80); freeze MSE mid-vs-end = 0,0; SRT 4 cue. Bản Boxed chưa Laugh giữ riêng. Đang chờ duyệt; chưa đăng, chưa hẹn giờ.

## 2026-11-18 — Bee (Muse), duyệt master + lệnh hẹn giờ 19/11

- Người dùng DUYỆT bản dựng ("Tốt"), lệnh hẹn giờ ngày mai 19/11 tầm 19h, cả 2 nền tảng như ep003. Caption ep004 chưa có bản chốt — trình nháp để duyệt trước khi hẹn giờ. Facebook không gắn link aff-0001 (biến thể hồng chưa xác minh trong shop, như vụ trắng ở ep003).

## 2026-11-18 — Bee (Muse), caption chốt + hẹn giờ

- Caption chốt (người dùng duyệt qua widget 16:24): "1 giờ sáng gọi điện, tưởng hỏi thăm. Hóa ra đòi 72 nghìn. 😌" + #chuyennhathaomy #phimnganai #haiviet + 'Sound effects: "Laugh Track 1.mp3" by LittleRainySeasons, CC BY, via Freesound.org'. Dùng chung cả 2 nền tảng; Facebook không gắn link aff.
- Đang hẹn giờ 19h ngày 19/11 (GMT+7) cả TikTok (@chuyennhathaomy, nhãn AI bật, Everyone) và Facebook Page (nhãn AI không bật được trên web).

## 2026-11-18 — Bee (Muse), kiểm chứng biến thể hồng

- Người dùng lệnh gắn link Shopee vào description. Bee check link aff-0001 (https://s.shopee.vn/5LDVnTeC4f → váy SANJOLI VD010) 2 lần tải trang: mục "Màu Sắc" chỉ có Đen + Be, KHÔNG có Hồng (cũng không có Trắng). Link không dẫn tới đúng váy hồng My mặc trong tập. Đang chờ người dùng quyết gắn hay bỏ như ep003; chưa hẹn giờ Facebook.

## 2026-11-18 — Bee (Muse), TikTok đã hẹn giờ

- TikTok @chuyennhathaomy: video ID 7709443983012826386, hẹn 19:00 ngày 19/11 (GMT+7), Everyone, nhãn AI bật, caption đúng bản chốt; verify qua Studio (badge "Nov 19, 7:00 PM (GMT+7) Saigon") + trang video hiện "Scheduled for: 2026-11-19 19:00". Bài ep003 hẹn 19h tối nay không bị đụng. Chưa public — chỉ ghi published sau khi xác minh lên sóng thật.
- Facebook: chưa hẹn giờ, đang chờ quyết định gắn/bỏ link.

## 2026-11-18 — Bee (Muse), quyết gắn link + hẹn giờ Facebook

- Người dùng quyết vẫn gắn link aff-0001 dù đã biết shop chỉ có Đen/Be. Description Facebook: caption chốt + dòng "Váy Thảo My mặc ở đây nhé: https://s.shopee.vn/5LDVnTeC4f" (đặt ngay sau câu mở đầu, trước hashtag). Đang hẹn giờ 19:00 ngày 19/11 (GMT+7) qua Business Suite.

## 2026-11-18 — Bee (Muse), Facebook đã hẹn giờ

- Facebook Page Chuyện Nhà Thảo My: post ID 1585624176939181, hẹn 19:00 ngày 19/11 (Asia/Saigon GMT+7), Public, description có link Shopee (verify 2 lần: trong composer + preview bài hẹn giờ); nhãn AI không bật được trên web Business Suite. Bài ep003 hẹn 19h tối nay không bị đụng. Composer có spinner treo sau khi bấm Schedule nhưng lịch đã ăn server-side (hiện cả Scheduled list + Planner) nên không bấm lại, tránh trùng bài.
- Cả 2 nền tảng đã hẹn xong 19h 19/11. Chưa public — chỉ ghi published sau khi xác minh cả 2 bài lên sóng thật (~19:20 ngày 19/11).

## 2026-11-19 — Bee (Muse), quyết bìa ep004

- Bìa cả 2 bài hẹn giờ 19h tối nay đều là mặt Bằng (TikTok không cho sửa bài đã hẹn giờ; Facebook không có mục đổi thumbnail). Người dùng quyết 13:20: ĐỂ NGUYÊN bìa Bằng tập này, không xóa/đăng lại. Hai bài giữ nguyên lịch 19h; cron 19:20 xác minh lên sóng rồi ghi nhận.

## 2026-11-19 — Bee (Muse), đã đăng cả 2 nền tảng (xác minh 19:2x)

- TikTok @chuyennhathaomy: video 7709443983012826386 public (Everyone), 5 views lúc xác minh; caption đúng; nhãn "Creator labeled as AI-generated" bật. URL: https://www.tiktok.com/@chuyennhathaomy/video/7709443983012826386
- Facebook Page Chuyện Nhà Thảo My: reel 1950158259280138, Shared with Public, 0 views/lượt tương tác lúc xác minh; description có dòng link Shopee aff-0001. URL: https://www.facebook.com/reel/1950158259280138
- Lưu ý ID: ID hẹn giờ 1585624176939181 là ID lịch hẹn, không hiển thị dạng ID bài đã đăng; Business Suite item ID 1232202395805917; reel ID công khai 1950158259280138.
- Nhãn AI Facebook: không bật được trên web Business Suite (như ep003); chưa xác minh có hiển thị trên bài đã đăng hay không.
- Ghi nhận: editorial_status → published; publications.csv + production-tracker.csv + affiliate-placements.csv (plc-0001, aff-0001 trên bài Facebook).
