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
