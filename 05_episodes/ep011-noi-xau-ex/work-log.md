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
- Duyệt đề xuất sửa thoại sh020/sh030 (prompt đang giữ thoại gốc).
- Giọng Dũng (mặc định: kiểm tra native từng take lúc gen).
- Xác nhận aff-0006 khớp màu/giá trên Shopee trước khi gắn bài.
