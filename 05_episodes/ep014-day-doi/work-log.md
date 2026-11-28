# Work log — ep014 'Dạy Đời'

## 2026-11-27 — Review + rebuild hồ sơ
- Review 06:30 27/11 verdict CHƯA ĐỦ: episode.yaml rev 1 + 8 prompt vẫn là tập "Mẹ gọi đêm Noel" (khác script r02); 4/4 motion prompt phạm luật cấm chữ; cả 4 shot đều 2 câu; số từ storyboard sai 2/4; Trí nói mà không thấy mặt; manifest mâu thuẫn script (mute_veo_native true + VieNeu-TTS); chưa có wardrobe.md/work-log.md.
- Richard duyệt 27/11 18:48 ("Duyệt") + lệnh gen ảnh trước, gen video sau ("gen hết ảnh các cảnh đưa tao duyệt xong mai chỉ việc gen video").
- Rebuild rev 2 theo script r02 + thoại gộp 1 câu/shot đã duyệt (15/12/15/14 từ): episode.yaml + 8 prompt mới, manifest theo r02 (My giữ native nếu Bắc else clone ThaoMy; Trí giữ native, không preset, không lồng ThaoMy), wardrobe.md + work-log.md mới. Location date-cafe v003-day (đã duyệt 21/11) + áo dài Vân Linh xanh nhạt lấy lại qua ref đã có, không upload mới.
- Trí: người mới (Bee chọn: 28t, tóc đen ngắn, polo xanh đậm + jean đen, quay ngang 3/4 nửa mặt) — Richard duyệt hướng này trong review; chưa có ảnh ref.
- My: áo dài Vân Linh xanh nhạt, son/móng tự nhiên (Bee chọn theo ep008/ep011) — Richard chưa chốt riêng, đổi thì sửa wardrobe.md + prompt sh020/sh040 trước khi làm lại frame.
- **27/11 18:56 — Richard chốt áo polo Trí theo link cậu ấy gửi: polo Falcon xanh nhạt (aff-0008, https://s.shopee.vn/4B1qY76LTw; ảnh ref `input/references/polo-falcon.jpg` sha `cb2325e5…`; shop opaanlp; giá chưa xác minh). Prompt ảnh sh010/sh030 + episode.yaml + wardrobe.md + script.md đã sửa theo (polo xanh đậm → Falcon xanh nhạt).**
- Validator: `python3 06_automation/validate_episode.py 05_episodes/ep014-day-doi` exit 0 — "Episode structure valid". Notes đúng giai đoạn: 4 frame missing + VieNeu voice pending (voice_status decided_by_user, chưa 'locked' — chỉ khóa ở khâu dựng).

## Frame v1 (xong 19:20 27/11)
- 4 frame Nano Banana, 0 credit, project Flow `CNTM · EP014 · Dạy Đời` https://flow.google.com/project/a765ad21-a30f-4f9a-8bef-199e294d671f (acc tinphim PLUS; đăng nhập cần Richard xác minh trên iPhone, bấm Yes + số 60).
- Mặt ThaoMy002: KHÔNG có character ThaoMy002 trên acc tinphim (project ep013 chỉ có nhân vật Nam) — file mặt v002 đã có sẵn trong Images/Uploads của project ep013 nên dùng lại qua picker, không upload trùng. Café + áo dài chưa có trên acc này nên upload mới vào EP014; polo Falcon cũng upload mới.
- sh010 (asset b7955c85, round 1): Trí polo Falcon xanh nhạt + jean đen, 3/4 nửa mặt, ly cà phê đen thấy rõ trên bàn. Nit: vai/tay My lọt ở mép trái; trên bàn còn ly nước + chén kim loại nhỏ từ ảnh gốc.
- sh020 (asset 7b0d7352, round 2): round 1 bị loại (ly sáng màu, cà phê đen không rõ, cười quá to) — round 2 sửa từ mặt master, ly đen + cà phê đen thấy rõ. Nit: 2 vệt sao trắng nhỏ (Gemini star) ở dưới; vai mờ của Trí (màu be) ở tiền cảnh phải.
- sh030 (asset 9e02b6e9, round 2): lần gen đầu bị chặn "unusual activity", chờ 5 phút gen lại được. Framing rộng hơn sh010 (ghế trống nổi bật). **Lỗi: có badge "AI" ở góc phải dưới TRONG ảnh tải về (không phải nhãn viewer) — cần crop khi dựng hoặc gen lại.**
- sh040 (asset fe9a177e, round 1): My đặt ly xuống, nhìn thẳng Trí, mặt bình thản. Nit: ly màu sáng, cà phê trong ly đọc nâu nhạt chứ không đen hẳn; vai tiền cảnh của Trí màu be/kem chứ không phải polo xanh nhạt.
- 4 file đã lưu vào `input/frames/` (768×1376 PNG, sha ghi trong episode.yaml), frame_status pending_review. Trình Richard duyệt ảnh trước rồi mới gen clip (luật 26/11). Gen clip Veo 3.1 Lite 4 × 10cr = 40cr, làm ngày mai theo lệnh Richard.
- **27/11 20:13 — Richard đổi góc Trí: mặt chính diện như My, bỏ góc nghiêng 3/4.** Prompt ảnh sh010/sh030 + script + wardrobe đã sửa. Frame v1 của Trí (3/4) bỏ, làm lại v2 chính diện.
- **27/11 21:09 — Richard DUYỆT frame sh030 v2 cho CẢ HAI cảnh Trí (sh010 + sh030).** episode.yaml: sh010 dùng chung first_frame sh030-frame-v2.png (sha 4c57f2d1…), frame_status approved cả 2; file sh010-frame-v2.png giữ lại trong repo làm lịch sử. Frame My sh020/sh040 v1 vẫn chờ duyệt.
- **27/11 21:11 — Richard DUYỆT cả hai frame My (sh020 + sh040 v1).** Cả 4 frame đã duyệt. Mai gen 4 clip Veo 3.1 Lite (40cr, acc reset 50cr/ngày).

## Gen clip Veo 3.1 Lite (cron 06:00 28/11 — BLOCKED, 0 credit)
- Đăng nhập Flow acc tinphim2016@gmail.com (Richard Youtuber, PLUS) thành công, KHÔNG cần xác minh iPhone lần này. Project EP014 mở sẵn.
- Số dư credit: **0** — banner Flow: "Bạn đã dùng hết tín dụng Google Flow..." Reset theo panel: **09:32 ngày 3/12** (không phải reset hằng ngày như ghi chú trước — cần đính chính: 50cr/ngày đã hết và không làm mới hôm nay; thực tế chỉ còn reset tháng 3/12).
- Cần 40cr (4 clip × 10cr) → thiếu đủ 40cr. KHÔNG gen clip nào, không tải gì, đúng luật dừng khi < 40cr.
- Chờ Richard quyết: (a) nâng cấp gói lấy credit ngay, hoặc (b) chờ reset 09:32 3/12 rồi chạy lại cron gen 4 clip. 4 frame đã duyệt vẫn nguyên, không cần làm lại.

## Gen clip Veo 3.1 Lite (28/11 — 4 take001 XONG, cho Richard duyet)
- 06:04 28/11 cron ep014-gen-clips chay: so du Flow 0 credit, panel ghi reset 09:32 3/12 → dung theo luat <40cr, khong gen clip nao. (Ghi chu cu "50cr/ngay, 28/11 co lai" la sai.)
- 06:31 28/11 kiem tra goi nang cap (browser): Pro 489.000d/thang (1.000cr/thang + 50/ngay), Ultra tu 2.250.000d/thang (10.000cr/thang); mua le credit khong hien gia tren acc Plus (nut +Them dan sang trang nang cap). Upscale 1080p la tinh nang Plus, khong khoa sau Ultra. Trang Google One ghi credit "Lam moi vao ngay mai" (29/11) — kha nang cao co lai 50cr.
- 09:51 28/11 kiem chung live: so du DA VE 50 credit (panel Flow + Google One deu ghi 50) — refresh ngay xay ra trong khoang 06:04-09:42, khong phai cho den 29/11 hay 3/12. Gen luon 4 clip (40cr), so du con 10.
- Gen 28/11 09:52-10:05 (browser, Frames-direct, Agent OFF, Veo 3.1 Lite, 9:16, 8s, 1 output/shot, cach nhau >=1 phut, khong bi chan "unusual activity", khong upscale 2K):
  - sh010 take001 — clip a68ac8e1-d528-4980-acc0-c262307a8f12, file generated/sh010-take001.mp4, sha 30c9a71815e623f38cbf6e06f3c25cc14435fd36d33268b326d463a30031aa23, 7.93s, 720x1280, 24fps.
  - sh020 take001 — clip ab3ea55d-5461-47f3-8c1b-0cb2a8b6e3c9, file generated/sh020-take001.mp4, sha 0202760a6cddad3c4ceb96800d951f6663c6fd7536e98f6c4175ab5d5a387039.
  - sh030 take001 — clip da2a7b2d-a468-44b5-ae2e-a5026fab0c8e, file generated/sh030-take001.mp4, sha ea8cff4d2c0c9f41385151026dd44f3d07de1761f35fdaf70ba22639d9ab6581.
  - sh040 take001 — clip 123d9550-af61-432e-8268-51cee65c8858, file generated/sh040-take001.mp4, sha bce44a479e0d398a40878a96fb98aa0af899af1c7c4e44b484576f99bcef33a4.
- QC local (faster-whisper base + trich frame 1s/4s/7s so voi frame da duyet):
  - sh010: Whisper du 15 tu, cau ca phe/latte dung thu tu (lech thanh dieu ASR). Mat Tri + polo Falcon + ly den khop frame; khong chu gia.
  - sh020: Whisper du 12 tu, cau Parasite dung thu tu. Mat My + ao dai + ly den khop; nit: giua clip cam ly 2 tay (frame goc 1 tay); khong chu gia.
  - sh030: Whisper du 15 tu, dung cau truc cau dao dien. ASR trinh duyet nghe garbled + lan audio clip truoc — do la artifact trinh duyet, khong phai loi clip. Mat Tri + polo + ly den khop; badge AI trong frame goc chi hien nhu watermark AI/Veo chuan; khong chu gia.
  - sh040: Whisper du 14 tu, cau chot dung nguyen van. Mat My + ao dai khop, ly tren ban, ca phe den ro; nit: vai tien canh Tri doc xanh navy dam (khong phai polo xanh nhat), mo nhe; khong chu gia.
  - Ca 4 clip: chi co watermark AI/Veo nho goc phai duoi (crop luc dung theo quy tac repo); khong co phu de/chu gia. Giong: Tri nam Bac, My nu Bac theo browser — My giu tieng goc neu Richard nghe la Bac, Tri giu goc luon (theo manifest).
- Trang thai takes: needs_review ca 4 — CHO Richard duyet take. Chua dung master.
