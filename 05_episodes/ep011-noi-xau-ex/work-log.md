# Work-log — ep011 'Nói Xấu Ex'

## 2026-11-24 06:32 — Review hằng ngày (chưa đủ điều kiện)
- episode.yaml + 6 prompt cũ mô tả tập khác ('Nấu cho một người', bếp, 3 shot, My độc thoại);
  script r02 là Dũng ↔ My ở café, 4 shot.
- Số từ ghi sai 3/4 shot (sh010 15, sh030 15, sh040 13 — đã sửa trong script.md).
- sh030 lộ twist 'Bốn mối' trước sh040; sh020 thừa câu đệm (đề xuất sửa thoại, CHƯA duyệt —
  prompt đang dùng thoại gốc r02).
- Dũng chưa có mặt/giọng; wardrobe My chưa chốt; affiliate chưa có.

## 2026-11-24 06:43–06:48 — Quyết định của Richard + rebuild hồ sơ (revision 2)
- Wardrobe My: áo dài, ngực to → giả định áo dài Vân Linh xanh nhạt (ep008) + son/móng tự nhiên
  (ep010), chờ frame duyệt làm xác nhận.
- Dũng: Richard gửi ảnh mới (1200×1986) → master v002, thay casting v001 (18/11, mặt khác hẳn,
  giữ làm lịch sử). File: `02_characters/dung/approved/dung-front-v002.jpg` (sha 5622b659…).
- episode.yaml viết lại rev 2: title 'Nói Xấu Ex', 4 shot, target 32s, thoại gốc r02,
  image_sources + prompt hash cập nhật. 8 prompt viết lại (motion chỉ 'Camera tĩnh. Không nhạc nền.'
  — không chữ phụ đề). wardrobe.md mới. manifest rev 2.
- Validator: exit 0 (note: first frame thiếu + VieNeu voice pending — đúng kỳ vọng).
- Affiliate aff-0006: link áo Dũng https://s.shopee.vn/3qOuYpE1Z6 → Aristino ALS618EDP01 kẻ xanh
  tím than (xác minh qua redirect + web search; Shopee chặn login nên chưa xác minh giá/màu trên
  Shopee — chờ Richard xác nhận).

## 2026-11-24 06:48 — Frame v1 bằng media pipeline (ĐÃ THAY THẾ, KHÔNG DÙNG)
- 4 frame 1152×2048 webp, 0 Flow credit. Richard hỏi nguồn → cậu ấy chốt làm lại bằng Google Flow.
- File cất tại `input/frames/media-pipeline-v1-superseded/` (giữ, không xóa).

## 2026-11-24 06:56–07:09 — Frame Flow (chờ duyệt)
- Project mới 'CNTM · EP011 · Nói Xấu Ex' — https://flow.google.com/project/ce074482-b99e-47c9-87e9-18cb86fa091a
  (huynhdn Pro). Nano Banana 2.1, mỗi frame 1 edit từ ảnh gốc, round 1, 0 credit.
  Không gen clip, không Agent.
- Quy tắc mới (Richard 24/11): lấy lại ref đã có trong Flow qua picker 'Chọn dự án', chỉ upload
  ảnh thật sự mới. sh010/sh020 dùng bản copy upload lúc đầu (lệnh sửa tới sau); sh030/sh040 dùng
  ref có sẵn (ThaoMyV002 từ EP003, áo dài + café từ EP008/EP010). Bản copy thừa KHÔNG xóa —
  frame nằm chồng version dưới asset gốc.
- File tải về (768×1376 JPEG, đã kiểm chứng trên disk): đường dẫn + sha đầy đủ ở
  `02_characters/thao-my/wardrobe/REGISTRY.md` mục 10.
- QC của Bee (xem trực tiếp 4 ảnh): mặt Dũng/My khớp, áo dài + café khớp, son/móng tự nhiên.
  Nit: sao Gemini nhỏ góc phải dưới cả 4 frame; sh020/sh040 khung rộng hơn medium shot;
  sh030 mất ly café đá của Dũng (chỉ còn ly cam của My); nốt ruồi cằm trái My nhìn không rõ.
- Trình Richard duyệt 07:09. CHỜ DUYỆT → mới map first_frame + SHA vào episode.yaml,
  gen 4 clip Veo 3.1 Lite (40 credit).
- Sổ đăng ký: `02_characters/thao-my/wardrobe/REGISTRY.md` cập nhật URL EP011 + mục frame ep011,
  commit 5bc2487 đã push (validator exit 0 trước commit). episode.yaml đã ghi flow_project
  (chưa commit — gộp vào commit hồ sơ sau duyệt frame).

## 2026-11-24 08:27 — Richard duyệt 4 frame → map + gen clip
- Richard: "duyệt" (4 frame Flow giữ nguyên, kể cả các nit đã báo: sao Gemini góc phải dưới,
  sh020/sh040 khung rộng, sh030 mất ly café đá, nốt ruồi chưa rõ).
- Map vào episode.yaml: 4 frame copy byte-identical vào `input/frames/sh0X0-frame-v1.jpg`
  (sha khớp bản tải về), `first_frame` + `frame_status: approved` + `approved_for_generation: true`
  từng shot; `flow_image_asset_id: null` (trình duyệt không báo asset ID; ep010 cũng null).
  `editorial_status: draft` → `script_approved` (thoại gốc r02 là bản sản xuất; đề xuất sửa
  sh020/sh030 vẫn chưa duyệt, không đưa vào prompt). `flow_project` đã ghi từ trước.
- Validator: default exit 0; `--stage generation` exit 0 (lưu ý: script sửa yaml bằng re.split
  từng chèn thừa `sh0X0` vào đầu dòng approved_for_generation — đã sửa bằng sed + parse lại
  + validator, lần sau dùng text replace theo từng shot hoặc kiểm tra diff ngay sau script).
- Commit hồ sơ ep011 (scope: ep011 + dung + affiliate-links.csv với aff-0006; KHÔNG gồm
  affiliate-placements.csv plc-0006–0010 của ep004–ep008 hay file bẩn ep009).
- Gen 4 clip Veo 3.1 Lite Frames-direct trong project EP011 (40 credit), tải 1K về review trước;
  2K chỉ sau khi duyệt take.

## Chờ Richard
- Duyệt frame — XONG 08:27.
- Duyệt 4 take take001 (trình 08:55): sh010 (giọng Dũng + diễn hoạt hơn thở dài), sh020 (giọng My nghiêng Nam — Whisper nghe "không xứng" thành "hổng sướng"), sh030 REJECT (chữ giả ~3.5–5.5s) → đề xuất quay take002 prompt y nguyên 10cr, sh040 (deadpan chưa rõ — mặt hiền/cười nhẹ).
- Duyệt đề xuất sửa thoại sh020/sh030 (prompt đang giữ thoại gốc).
- Giọng Dũng (mặc định: kiểm tra native từng take lúc gen).
- Xác nhận aff-0006 khớp màu/giá trên Shopee trước khi gắn bài.

## 2026-11-24 ~08:47 — 4 take Veo 3 Lite gen xong + QC của Bee (1K)
- Gen: browser task 08:29–08:47, huynhdn Pro, project EP011, Frames-direct, Veo 3.1 Lite, 9:16, 8s, 1 output/shot, 10cr/shot = 40cr, số dư 460 → 420 (xác minh trên panel). Không clip nào bị chặn policy. Player sh020/sh030/sh040 lúc đầu báo "Không tải được video" — reload 1 lần + chờ ~30s thì lên bình thường.
- Tải 1K (720p gốc, download-capture): sh010 e8c3b603 (2,9MB), sh020 8d950a41 (3,4MB), sh030 e8864056 (2,3MB), sh040 b03b7790 (2,5MB); ffprobe: 720×1280, video 7.92s / audio 7.93s. Map theo artifact ID + tên file tải về (f1=sh010, f2=sh020, f3=sh030, f4=sh040), khớp Flow clip ID.
- QC của Bee (frame ở 0.5/2.0/4.0/5.0/6.0/7.5s + Whisper base + năng lượng 48k): cả 4 thoại đủ từ (15/13/15/13). Lưu ý: báo cáo trình duyệt nói "không có chữ giả" là SAI — sh030 có chữ giả, Bee tự soi frame mới bắt được.
- sh010 take001: đủ 15 từ 0.5–5.7s. Mặt/đồ/café khớp; diễn hoạt hơn "thở dài" (2 tay giơ cao ~4s); đuôi cúi đầu ~7.5s (cắt lúc dựng). Giọng nam; hướng Bắc/Nam chờ Richard nghe (Whisper nghe "Ích kỷ"→"Bất kỳ", "tệ"→"tài").
- sh020 take001: đủ 13 từ 0.6–6.56s. Mặt/đồ khớp, 1 ly cam + điện thoại, không chữ giả. Whisper nghe "không xứng"→"hổng sướng" — nghiêng Nam (giống ep010 sh020); nếu Richard nghe không Bắc thì tắt tiếng gốc, lồng clone ThaoMy wordalign.
- sh030 take001: đủ 15 từ 0.0–5.28s; "Bốn mối" nghe thành "Vũng mỗi". LỖI: chữ giả "Rẹpatistépinéés fâilluurệrs." hiện ~3.5–5.5s (có ở 4.0/5.0, sạch ở 2.0/3.0/6.0/7.5), đè đúng câu "Bốn mối rồi" — không crop được. Đề xuất REJECT + quay take002 prompt y nguyên.
- sh040 take001: đủ 13 từ 0.62–6.3s. Mặt/đồ khớp, không chữ giả. Nhưng biểu cảm hiền/cười nhẹ ở 2.0/4.0/7.5s (nhắm mắt cười ở 7.5s), chưa rõ deadpan + gật đầu chậm có lên hình — chờ Richard quyết giữ hay quay take002 siết prompt.
- Chung: logo "Veo" góc dưới phải + sao Gemini ở cả 4 clip (crop logo lúc dựng, như mọi tập). Takes đã ghi vào episode.yaml (status needs_review) + copy vào generated/ (sha khớp bản tải), validator generation đạt.

## 2026-11-24 ~09:09 — Richard chốt take (sh020 lồng, sh040 giữ)
- sh020 take001: ACCEPTED — Richard: "giọng Bắc, cần lồng tiếng" → tắt tiếng gốc, lồng clone ThaoMy wordalign (như ep010 sh020). Đang làm dub (subagent, theo pipeline ep010: Colab T4 VieNeu Turbo preset ThaoMyVeo + build_wordalign).
- sh040 take001: ACCEPTED — Richard: "giữ nguyên đc" → giữ tiếng gốc.
- sh010 take001: chưa chốt (giọng Dũng chờ Richard nghe).
- sh030 take001: REJECTED (chữ giả) — take002 đang gen (browser task 221f0da1, 10cr).
- episode.yaml: statuses đã cập nhật (sh020/sh040 accepted_editorial, sh030 take001 rejected_editorial), validator generation đạt.

## 2026-11-24 ~09:15 — sh030 take002 gen xong + QC của Bee (1K)
- Re-roll theo lệnh Richard 09:08, prompt + frame y nguyên take001, Veo 3.1 Lite 10cr. Flow clip e6f4ee42-8aad-4a17-9d5d-9bbb21d9902c; tải 1K (2.387.007 byte, sha 01d7820e…, 720×1280, 7.92s).
- QC của Bee (frame 0.5/2.0/3.5/4.0/4.5/5.0/5.5/7.5s + Whisper base): SẠCH — không còn chữ giả ở bất cứ thời điểm nào, kể cả cửa sổ 3.5–5.5s (take001 dính chữ ở 4.0/5.0). Mặt/đồ/café khớp; diễn: lắc đầu buồn, 2 tay giơ lúc ~4.0s nói "Bốn mối rồi"; đuôi cúi đầu ~7.5s (cắt lúc dựng).
- Whisper base: đủ 15 từ 0.0–5.48s; "Bốn mối" lại nghe thành "Vũ cũng mỗi" (lỗi đồng âm ASR quen thuộc, giống take001) — giọng Dũng vẫn chờ Richard nghe.
- Takes: take002 ghi vào episode.yaml (needs_review) + copy vào generated/; validator generation đạt. Chờ Richard duyệt take002.

## 2026-11-24 ~09:15 — Lồng tiếng clone ThaoMy sh020 (wordalign) XONG, QC ĐẠT
- Lý do: Richard 09:24 chốt sh020 lồng clone (giọng native nghiêng Nam), sh040 giữ nguyên.
- TTS: VieNeu v3 Turbo trên Colab T4 (session ep011-dub, script `~/workspace/colab-t4-test/ep011_dub_thaomy.py`), preset ThaoMyVeo, enroll ref-clip2.wav. Wav `~/workspace/colab-t4-test/ep011-dub/thaomy-ep011-sh020.wav` (5.20s, 48kHz mono). Session đã stop, không orphan.
- Cửa sổ native đo lại bằng energy 48kHz 0.05s từng kênh (ghi `edit/sh020-native-windows.md`): 1.00-1.90 / 2.80-4.20 / 5.85-6.65. Whisper smear từ đầu cụm 1 sớm 0.4s ("Thương" 0.6s; energy: ambient tới 1.00s) — dub đặt theo energy, không theo Whisper.
- Stretch: P1 0.989x, P2 0.737x, P3 0.952x (đều trong khoảng ep009 0.60x–1.70x). Build `edit/build_wordalign_sh020.py`.
- Output: `generated/sh020-take001-dubbed.mp4` (video copy 1K 720x1280, audio clone mono 48kHz AAC 192k, 7.93s; sha ab4cd7f3...). Take gốc không ghi đè (sha vẫn 3bb1a1b8...).
- QC (`edit/dub-qc-ep011-sh020.md`): Whisper base nghe đủ 13/13 từ đúng 3 cửa sổ (nhầm đồng âm "của"≈cô, "sướng"≈xứng như mọi lần); năng lượng ngoài cửa sổ = 0.000 tuyệt đối (đuôi 0.1s). ĐẠT — chờ tai Richard chốt cuối.

## 2026-11-24 ~09:18 — Takes chốt hết, commit + bắt đầu tải 2K
- Richard 09:17: "2 video của Dũng là giọng miền nam nhưng ko sao, duyệt đc" → sh010 take001 + sh030 take002 ACCEPTED (giữ tiếng gốc Nam). Cả 4 shot đã chốt: sh010 take001 (Nam), sh020 take001 (lồng clone, QC đạt), sh030 take002 (Nam), sh040 take001 (giữ gốc).
- episode.yaml: statuses cập nhật (cả 4 accepted_editorial), validator generation đạt. Tracker ep011 cập nhật (nau-cho-mot-nguoi → noi-xau-ex, script_approved, URL project EP011).
- Commit 10e808e đã push (18 file: ep011 scope + tracker; KHÔNG gồm file bẩn ep008/ep009/ep010 hay affiliate-placements.csv của chat khác).
- Tải 2K: browser task đang chạy upscale + download-capture từng take (sh010 → sh020 → sh030 take002 → sh040); verify bằng frame-diff vs 1K đã duyệt sau khi file về. Dub sh020 sẽ rebuild trên video 2K sau.
- Chờ Richard nghe bản lồng sh020 (đã gửi 09:17).

## 2026-11-24 ~09:49 — 2K về đủ + verify đúng take + dub rebuild trên 2K
- Tải 2K xong 09:19–09:49 (browser, upscale mỗi clip ~7 phút, không chạm giữa chừng, không paywall; 4K khóa không dùng): sh010 10.314.763 byte sha 92ffac3d…; sh020 8.271.057 byte sha fe4d2622…; sh030 take002 6.929.729 byte sha 26336e41…; sh040 8.763.089 byte sha d2ca0202… — tất cả 1080×1920, video 7.83s / audio 7.85s.
- Verify bằng frame-diff vs 1K đã duyệt (t=2.5/4.0s, mean abs diff): sh010 4.66/5.05, sh020 3.38/3.58, sh030 take002 3.24/3.52, sh040 4.49/4.73 — ĐÚNG take cả 4. Control sh030 2K vs take001: 10.37/10.24 (khác rõ) → 2K đúng là take002, không phải take001.
- 2K copy vào generated/ theo quy ước ep010 (*-1080p.mp4).
- Dub sh020 rebuild trên video 2K: generated/sh020-take001-dubbed-1080p.mp4 (1080×1920, 7.83s, sha e4aa1b02…, video copy 2K + audio clone từ edit/wordalign/sh020-aligned.wav, -shortest). QC: Whisper đủ 13 từ đúng cửa sổ, năng lượng ngoài cửa sổ ≤0.001. ĐẠT.
- Chờ Richard nghe bản lồng (bản 2K) rồi dựng master.

## 2026-11-24 ~12:06–12:35 — Dựng master 2K XONG, QC ĐẠT (chờ Richard duyệt)
- Lệnh: Richard 12:05 "ok" (duyệt bản lồng sh020) → dựng master theo pipeline ep010 (`edit/build_master_2k.py`, adapt từ ep010, không ghi đè file ep010).
- Nguồn (2K, đã verify đúng take bằng frame-diff): sh010 take001-1080p (native Dũng Nam), sh020 take001-dubbed-1080p (clone ThaoMy wordalign, native thay hẳn), sh030 take002-1080p (native Dũng Nam), sh040 take001-1080p (native My Bắc).
- Đo lại trên 2K (Whisper base + energy 48kHz 0.1s): sh010 thoại 0.00–5.68s → trim 6.4s; sh020 dub 3 cụm 1.00–1.90 / 2.80–4.20 / 5.85–6.65 → trim 7.35s; sh030 take002 0.00–5.48s → trim 6.2s; sh040 0.66–3.58 + 5.16–6.30s → trim 7.7s (giữ nụ cười nhắm mắt tới 7.5s như ep010). Tổng video 27.65s.
- Crop: Veo + sao Gemini xác minh ở góc dưới phải trên file 2K (corner crop x900–1080/y1700–1920: sao ~y1735, chữ "Veo" ~y1855–1885) → crop `960:1707:60:0` + lanczos 1080×1920, giống ep010, một crop chung cả 4 shot.
- Caption: Remotion BasicCaptions Boxed (accent #F59E0B), 56 từ, Whisper base chạy lại trên assembly, align theo thứ tự + energy-refine. Fix biên: "Cũng" (13.20–13.92s) chuyển từ sh020 sang sh030. Lần này "Bốn mối" Whisper nghe 2 từ ("Bộ"+"mỗi") nên fix 3-cho-2 đã chuẩn bị không cần dùng. `captions-PROBLEMS.txt` chỉ có clamp cuối từ thường lệ. Render chunked ≤287 frame, concurrency 1, chrome-headless-shell 131: chunk0 287f/9.57s, chunk1 287f/9.57s, chunk2 257f/8.57s.
- SỰ CỐ GIỮA CHỪNG: lần chạy đầu bị SIGTERM kill ~phút 10, đúng lúc đang concat video-only (sau khi cả 3 chunk đã verify đạt) → `boxed-video-only.mp4` hỏng (thiếu moov). Resume bằng `edit/build2k/resume_build.py`: xóa file hỏng, dựng lại từ 3 chunk đã verify (27.70s, mean frame 100.3 @ 13.8s), tiếp tục mux + stage 3 + QC. Không render lại, không gen lại, không lồng lại, không tốn credit.
- SFX: Laugh Track 1 duy nhất sau punchline sh040 — mix bằng numpy (KHÔNG adelay), audible 26.46s (từ cuối "anh." 26.31s + 0.15s), stem_start 26.20s, kết 28.30s; đuôi freeze-frame 0.60s.
- Master: `delivery/ep011-master-2k.mp4` (28.30s, 1080×1920, 30fps, H.264 yuv420p, AAC 48kHz stereo; sha ebfdb8573e28e332b2f6a98c7e1c82f641380aed5c7554c81fe944d5e80d314b; 43.463.754 byte; loudness −14.92 LUFS, TP −0.97 — ngang ep010 −14.99). SRT: `delivery/ep011-master-2k.srt` (8 cue).
- Cover candidate: `delivery/ep011-cover-thaomy.jpg` (sh040 6.5s, master 26.45s; My mắt mở, cười nhẹ, nhìn camera; sha 011f463d…). LƯU Ý: bản đầu trích từ master đã caption nên dính chữ "ANH." trên đùi → đã trích lại từ assembly chưa caption (không chữ, không icon Veo). Đây là ỨNG VIÊN cho Richard chốt, không phải quyết định.
- QC ĐẠT (chi tiết `edit/build2k/build-report.md`): ffprobe đủ thông số; frame mean 100.6–120.0 khắp 0.5–28.2s, không đoạn đen; Whisper final đủ 56 từ đúng 4 câu theo thứ tự (chỉ nhầm đồng âm quen thuộc: "tệ"→"tài", "xứng"→"sướng", "Bốn mối"→"Bộ mỗi", "đấy"→"để"); energy đúng cửa sổ từng shot, sh020 có khoảng lặng đúng giữa 3 cụm dub; caption xem trực tiếp: 1.5s "ANH TỆ LẮM" (highlight "TỆ"), 8.0s "THƯƠNG ANH GHÊ." ("GHÊ."), 22.0s "LẦN NÀO CŨNG" ("LẦN"); cut 3 chỗ xem trực tiếp đều sạch (sh030→sh040: Dũng cúi đầu/nhắm mắt, caption đã tắt → My nhìn camera, chưa caption); laugh kiểm tra TỪNG KÊNH trên file đã build: RMS L=0.1291 R=0.1292 (tỉ lệ 1.00), L−R/L+R = 0.062, tương quan envelope L/R = 0.995 — không rò 1 kênh.
- Nit ghi nhận: contact sheet `edit/build2k/qc-contact.png` rộng 4 cột nhưng paste 6 frame cắt nên 2 frame cắt sh040 rơi khỏi sheet (2 frame đó đã xem riêng ở `edit/build2k/qc/final-cut-sh040-pre/post.png`).
- Manifest cập nhật rev 3 (takes đã khóa + sha đầy đủ, crop, trim, build commands, SFX nguồn/license, QC passed). KHÔNG commit, KHÔNG đăng/hẹn — master chờ Richard duyệt. episode.yaml editorial_status không đổi (để parent).

## 2026-11-24 ~13:46 — Bìa v1 bị chê, trích 3 bìa khác
- Richard: "Bìa nhìn hơi giả không giống mặt My lắm" — bìa v1 (sh040 6.5s, master 26.45s, My nhắm mắt cười nhẹ) KHÔNG dùng nữa.
- 3 bìa khác trích từ take 2K chưa caption (mắt mở, giống My hơn), crop Veo icon như master (crop=960:1707:60:0 + lanczos 1080×1920):
  - ep011-cover-alt-sh040-1p4.jpg — sh040 1.4s, My nhìn thẳng camera, mặt tỉnh (khoảnh khắc 22.0s của master).
  - ep011-cover-alt-sh020-1p6.jpg — sh020 1.6s, My chống cằm, mặt rõ, miệng mở ("Thương anh ghê").
  - ep011-cover-alt-sh020-3p0.jpg — sh020 3.0s, My chống cằm, miệng chữ o ngạc nhiên.
- Chờ Richard chốt bìa + duyệt master + lịch đăng.

## 2026-11-24 ~14:08 — Richard chốt bìa số 2
- Bìa CHỐT: ep011-cover-alt-sh020-1p6.jpg (sh020 1.6s, My chống cằm) → copy thành ep011-cover-thaomy.jpg (canonical).
- Bìa v1 đổi tên thành ep011-cover-v1-rejected.jpg (giữ lại làm lịch sử, không dùng).
- Chờ Richard duyệt master + lịch đăng (slot trống tiếp theo: 19:00 T4 26/11 — ep009 tối nay 24/11, ep010 tối mai 25/11).

## 2026-11-24 ~14:09 — Master DUYỆT, commit 1fe781c
- Richard DUYỆT master 2K (28.30s, -14.92 LUFS, sha ebfdb857…) + CHỐT bìa số 2 (sh020 1.6s, chống cằm).
- Validator: manifest rev 3→2 + `shot`/`take` → `shot_id`/`take_id` (theo schema ep010) rồi pass exit 0. editorial_status giữ `script_approved` (ep010 đã hẹn đăng vẫn `script_approved`).
- Commit 1fe781c đã push, origin/main xác nhận (72 files: toàn bộ ep011 + tracker 1 dòng).
- Publish kit đã soạn: delivery/ep011-publish-kit.md (chưa commit).
- Chờ Richard chốt giờ đăng 26/11 (17h hay 19h). Chưa hẹn đăng, chưa đăng.

## 2026-11-24 ~15:07 — Đã hẹn đăng 19:00 T4 26/11 cả 2 nền tảng
- Richard chốt 19h (widget 14:58).
- TikTok @chuyennhathaomy: post 7711645254763564295, https://www.tiktok.com/@chuyennhathaomy/video/7711645254763564295, Everyone, nhãn AI BẬT, cover Thảo My chống cằm (sh020 1.6s, bìa số 2), caption "Bốn mối mà lần nào cũng lỗi người ta. Hay thật đấy anh. 😌" + hashtags #chuyennhathaomy #phimnganai #haiviet #shorts.
- Facebook Page Chuyện Nhà Thảo My (273224542851642): post 4656304111293707, Public, cùng caption, KHÔNG gắn link aff-0006 (chưa xác nhận màu/giá Shopee), cover set qua Thumbnail upload.
- publications.csv: 2 dòng scheduled (ep011-noi-xau-ex, tiktok + facebook), master_revision ep011-master-2k.mp4, verified_at trống. Chưa ghi published — chỉ ghi sau khi xác minh lên sóng 19:20 26/11.
- Cron xác minh `ep011-record-publication` 19:20 26/11 — chỉ like Facebook, KHÔNG comment aff-0006 (chưa xác nhận Shopee).
