# Work log — ep005 "Mẹ Anh Bảo"

## 2026-11-18 — review + rewrite (rev2)
- script.md r02 (4 shot, đối thoại My ↔ Khôi) lệch hẳn episode.yaml/prompts r01 (monologue 3 shot "Chưa"). Viết lại hồ sơ rev2: 4 shot r02, 8 prompt EN mới, validator cấu trúc đạt.
- Richard chốt: váy SANJOLI xanh dương; Khôi dùng mặt chính diện; câu chốt sh040: "Thế sao mẹ anh không đi hẹn hò thay anh luôn đi?" (12 từ).
- 4 frame dựng trong Flow project "CNTM · EP005 · Mẹ Anh Bảo" (0 credit): sh010, sh020 v1 (váy navy, lệch tông), sh030 (đếm 2 tay), sh040.
- sh020 v2: sửa mới từ master gốc + ảnh mẫu váy, khớp tông dusty medium-blue với sh040 nhưng lòi dây chuyền chép từ ảnh mẫu.
- sh020 v3: sửa mới từ master gốc, prompt thêm "no jewelry", hết vòng cổ, giữ tông dusty medium-blue. Prompt sh020-image.txt cập nhật "No text, no logos, no jewelry." + hash yaml.

## 2026-11-19 06:28 — duyệt frame, gen take 1
- Richard duyệt cả 4 frame (sh010, sh020 v3, sh030, sh040). Ghi frame vào input/frames/ (sh020 giữ cả v1/v2/v3, first_frame trỏ v3), approved_for_generation true, editorial_status generating, validator đạt cả --stage generation, tracker → generating.
- Gen 4 clip Veo 3.1 Lite Frames-direct, prompt nguyên văn, mỗi clip 1 lần, không chặn. Flow ID: sh010 04cdb21d, sh020 380c484d, sh030 0bff7bd9, sh040 dcc6dff4. File local ~/workspace/ep005-me-anh-bao-clips/ep005-sh0X0-take1.mp4 (720×1280, 24fps, 7,93s).
- QC local: cả 4 đúng người/khung, không phụ đề giả, đuôi sạch; thoại Whisper base sh010 + sh030 đúng từng chữ, sh020 + sh040 đúng nội dung (nghe nhầm đồng âm); F0: Khôi ~150/156Hz, My ~264/264Hz.
- Số dư Flow sau gen hiện 880, không khớp 870−40=830 (chưa rõ lý do).
- Chưa ghi take vào yaml, chưa dựng.

## 2026-11-19 07:57 — gen lại sh040 take 2
- Richard: sh040 take 1 hiền quá (mặt bình thản, cuối clip nhắm mắt cười dịu). Lệnh gen lại sắc hơn.
- Sửa sh040-motion.txt: "says coolly" → "says sharply with a teasing smirk" (1 biểu cảm, giữ nguyên thoại + hành động đặt ly), cập nhật hash yaml, validator --stage generation đạt.
- Đang gen lại đúng sh040 take 2, Frames-direct, Veo Lite, 10 credit, frame sh040-first-frame.jpg.

## 2026-11-19 07:58 — chốt giọng
- Richard nghe 4 clip take 1: giọng OK cả 4. Giữ nguyên tiếng Veo gốc cả 4 shot, KHÔNG lồng clone. Manifest audio_plan: mute_veo_native false, voice_by veo_native.

## 2026-11-19 08:00 — sh040 take 2 QC
- Gen xong take 2 (Flow ID b72ae899), 10 credit, số dư 880 → 870. File ~/workspace/ep005-me-anh-bao-clips/ep005-sh040-take2.mp4 (720×1280, 24fps, 7,93s).
- QC local: mặt sắc hơn hẳn take 1 — lúc nói nhướng mày, miệng mở lộ răng, kiểu cà khịa; đuôi 7,5s mắt MỞ, nhếch mép nhẹ, không còn nhắm mắt cười dịu. Không phụ đề giả, đuôi sạch. F0 ~263Hz, cùng giọng take 1.
- CẢNH BÁO: Whisper base nghe "mẹ anh" thành "mấy anh" ở take 2 ("Thế sao mấy anh không đi hẹn họ thấy anh luôn đi") — take 1 máy nghe đúng "mẹ anh". Chưa kết luận được là máy nghe sai hay Veo đọc sai; cần Richard nghe tai thật trước khi chốt take 2.

## 2026-11-19 08:09 — chốt take, chuẩn bị dựng
- Richard duyệt sh040 take 2 (đã nghe tai thật: "mẹ anh" đúng, Whisper nghe nhầm "mấy anh"). Bộ take chốt: sh010 take1, sh020 take1, sh030 take1, sh040 take2. Cả 4 giữ tiếng Veo gốc, không lồng.
- Ghi take vào episode.yaml + selected_takes vào manifest.
- Tải bản 2K (1080p upscale, 0 credit) của 4 take đã chốt rồi mới dựng, theo luật 1K review / 2K dựng.

## 2026-11-19 08:28 — thêm Laugh Track 1 sau sh020
- Richard: cuối sh020 khi My nói xong ("...nước sôi.") chèn Laugh Track 1 nữa, chỗ đó cũng hài.
- Cách làm: Laugh Track 1 (2,1s, CC BY) đặt thêm 1 lần ngay sau câu sh020, video freeze ở frame cuối sh020 trong lúc cười rồi mới sang sh030; Laugh cuối tập (stage 3) vẫn giữ. Chèn từ stage 1 (trước caption) để caption/SRT khớp timeline cuối; bounds mới ghi vào build/bounds.json.

## 2026-11-19 08:52 — sửa vị trí laugh giữa (stage 1 chạy lại)
- Stage 1 lần 1 XONG (assembly 30,54s, loudnorm input -15,84 LUFS, crop watermark sạch, cắt đúng người, mid-freeze MSE 0.0). Nhưng vị trí laugh giữa SAI: đặt theo energy span (2K đọc 0-7,85s) nên laugh nghe được từ 14,50s, trong khi Whisper word-level cho thấy câu sh020 kết thúc 12,97s — trễ 1,53s.
- Sửa: sh020_end lấy từ Whisper (12,97s), stem_start = 12,86s, laugh nghe 13,12-14,96s, freeze 14,0-15,16s (1,16s), tổng mới ~29,16s. Chạy lại stage 1 + build_captions.
- Caption lần 1: 56/56 từ khớp; sh040 Whisper thừa 16 từ do lặp ảo ở đuôi (30,00s+) — đã loại, chỉ lấy 12 từ đầu đúng thứ tự. Câu sh040 nói từ 26,66-29,49s (mở đầu ~3,6s im, đúng nhịp take đã duyệt).

## 2026-11-19 09:21 — master XONG, chờ duyệt
- Master: `ep005-me-anh-bao-boxed-laughtrack1.mp4` (30,08s, 1080x1920, 24fps, -15,45 LUFS/TP -0,78), tai ~/workspace/ep005-me-anh-bao-clips/. SRT kem: `ep005-me-anh-bao-subtitles.srt` (4 cue).
- Caption Boxed #F59E0B, 56/56 từ khớp kịch bản, không lỗi căn chỉnh (lần chạy 2; lần 1 Whisper lặp ảo 16 từ ở đuôi sh040 đã loại).
- Laugh Track 1 hai lần: sau sh020 nghe 13,12-14,96s + freeze 1,16s trên nụ cười của My (đã sửa vị trí từ 14,50s sai do đo năng lượng trên file 2K); cuối tập nghe 28,24-30,08s + freeze 0,87s. Peak 0,871, không clip.
- QC hình: caption đúng từ/đúng lúc cả 4 shot, 2 frame freeze sạch chữ, crop watermark sạch, váy xanh khớp cả tập, mặt sh040 take 2 sắc (nhếch mép lúc chốt câu).
- Remotion render lần 1 fail OOM ở frame 678/701 (concurrency 2), lần 2 chết do VM restart giữa chừng, lần 3 concurrency 1 chạy đạt (9,7 phút).
- Ghi manifest (locked 30,08s, build_notes, qc passed), episode.yaml editorial_status → built, tracker → draft. Chưa đăng, chờ Richard duyệt master.

## 2026-11-19 09:53 — hẹn giờ đăng 19:00 ngày 20/11
- Richard lệnh đăng (09:37), hẹn giờ 19h ngày mai 20/11; đồng thời chốt quy tắc mới: frame/thumbnail của mọi bài luôn là mặt Thảo My (vì mở đầu video là mặt Khôi — mặt lạ — sợ bóp tương tác).
- Ảnh bìa: `ep005-cover-thaomy-sh040.jpg` (frame 27.5s của master, mặt My lúc chốt câu, 1080x1920) — dùng làm custom cover/thumbnail cả 2 nền tảng.
- TikTok @chuyennhathaomy: hẹn Nov 20, 7:00 PM (GMT+7), video 7709707638719778066, Everyone, nhãn AI bật (preview + trang video đều hiện "Creator labeled as AI-generated"), caption đúng câu chốt + hashtag + dòng CC BY. Studio hiện badge "Nov 20, 7:00 PM (GMT+7) Saigon". Bài ep004 hẹn tối nay 19/11 không đụng.
- Facebook Page: hẹn Nov 20, 7:00 PM (Asia/Jakarta GMT+7 — cùng giờ VN, không có lựa chọn Asia/Saigon), post 1121844250750225, Public, description đúng bản chốt CÓ link aff-0001. Richard quyết gắn link (09:46), nói trong shop vẫn chọn được màu xanh — lưu ý: Bee check shop ngày 18/11 chỉ thấy 2 màu Đen/Be, không thấy xanh; quyết định gắn link là của Richard. Nhãn AI không bật được trên web Business Suite (như mọi lần). Thumbnail custom đã upload + chọn (dấu check xanh), dòng Scheduled hiện mặt Thảo My.
- Caption chốt cả 2 bên: "Em muốn hẹn hò với anh. Không phải hẹn hò với mẹ anh." + #chuyennhathaomy #phimnganai #haiviet + dòng CC BY Laugh Track 1; Facebook thêm dòng link váy.
- Ghi hồ sơ: episode.yaml editorial_status → ready_to_publish, manifest thêm build_notes hẹn giờ, tracker dòng ep005 → draft + trạng thái hẹn giờ. Chưa commit (Richard chưa lệnh). Cron ep005-record-publication hẹn 19:20 ngày 20/11 để xác minh lên sóng thật rồi mới ghi published.
