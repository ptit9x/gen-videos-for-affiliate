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
