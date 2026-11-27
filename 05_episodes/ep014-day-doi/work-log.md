# Work log — ep014 'Dạy Đời'

## 2026-11-27 — Review + rebuild hồ sơ
- Review 06:30 27/11 verdict CHƯA ĐỦ: episode.yaml rev 1 + 8 prompt vẫn là tập "Mẹ gọi đêm Noel" (khác script r02); 4/4 motion prompt phạm luật cấm chữ; cả 4 shot đều 2 câu; số từ storyboard sai 2/4; Trí nói mà không thấy mặt; manifest mâu thuẫn script (mute_veo_native true + VieNeu-TTS); chưa có wardrobe.md/work-log.md.
- Richard duyệt 27/11 18:48 ("Duyệt") + lệnh gen ảnh trước, gen video sau ("gen hết ảnh các cảnh đưa tao duyệt xong mai chỉ việc gen video").
- Rebuild rev 2 theo script r02 + thoại gộp 1 câu/shot đã duyệt (15/12/15/14 từ): episode.yaml + 8 prompt mới, manifest theo r02 (My giữ native nếu Bắc else clone ThaoMy; Trí giữ native, không preset, không lồng ThaoMy), wardrobe.md + work-log.md mới. Location date-cafe v003-day (đã duyệt 21/11) + áo dài Vân Linh xanh nhạt lấy lại qua ref đã có, không upload mới.
- Trí: người mới (Bee chọn: 28t, tóc đen ngắn, polo xanh đậm + jean đen, quay ngang 3/4 nửa mặt) — Richard duyệt hướng này trong review; chưa có ảnh ref.
- My: áo dài Vân Linh xanh nhạt, son/móng tự nhiên (Bee chọn theo ep008/ep011) — Richard chưa chốt riêng, đổi thì sửa wardrobe.md + prompt sh020/sh040 trước khi làm lại frame.
- Validator: `python3 06_automation/validate_episode.py 05_episodes/ep014-day-doi` exit 0 — "Episode structure valid". Notes đúng giai đoạn: 4 frame missing + VieNeu voice pending (voice_status decided_by_user, chưa 'locked' — chỉ khóa ở khâu dựng).

## Frame v1 (đang làm)
- 4 frame Nano Banana, 0 credit, project Flow riêng `CNTM · EP014 · Dạy Đời` (tạo khi làm frame), mặt ThaoMy002 + café v003-day lấy lại qua picker.
- Trình Richard duyệt ảnh trước rồi mới gen clip (luật 26/11). Gen clip Veo 3.1 Lite 4 × 10cr = 40cr, làm ngày mai theo lệnh Richard.
