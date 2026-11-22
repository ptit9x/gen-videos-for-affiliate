# Transcript reel gốc — Chuyện đời daily, "Lý do vợ chọn chồng vì ngủ không ngáy"

- Nguồn: https://www.facebook.com/share/r/19bG9Zep7h/?mibextid=wwXIfr (reel id 1687774499562746, link gốc Richard gửi 22/11/2026)
- Tác giả: Chuyện đời daily. Caption: "Lý do vợ chọn chồng vì ngủ không ngáy 😂😂😂 #giaitri #chuyendoidaily #vochong #xuhuong #viral" — đăng 2026-11-20, 22 likes / 1 comment lúc xem qua Facebook (lúc trình duyệt xem lại: 10 reactions, 2 comments, 4 shares).
- Video: `source-reel-chuyen-doi-daily-ngu-khong-ngay.mp4`, 1440×2560, 29,95 giây, sha256 `a5c04b23d8766ba37abc8acc21474b3f28be4ef681a756d95bcec562a5d5cc16`. Lưu ý hash: file gốc tải bằng yt-dlp từ Facebook là 6.990.578 byte, sha256 `fc5caa7b416d4b043b257348ac5e1705b8d03e3d19a4cab6c57a0b4f1aa18dfe`; bản lưu trong repo này là bản hệ thống re-encode (12.890.778 byte) — đã kiểm chứng lại bằng faster-whisper base: transcript khớp từng câu với bản gốc, nội dung không đổi.
- Cách dựng transcript này: trình duyệt mở link nhưng không phát được video và không tải được file (Getfvid không vào được, FDOWN bị chặn, trình duyệt báo không hỗ trợ download). Bee tải trực tiếp bằng yt-dlp từ link reel Facebook (file trên) và từ bản repost YouTube Shorts https://www.youtube.com/watch?v=43cT_NWE90E (cùng 29,98s, đối chiếu khớp). Transcript bằng faster-whisper base local (model tại `~/MoneyPrinterTurbo/models/whisper-base`, đọc audio bằng numpy vì PyAV lỗi `metadata_errors`), đã sửa các lỗi nghe có hệ thống của Whisper (ngấy→ngáy, trọn trông→chọn chồng, xo sánh→so sánh, to mò mấy hỏi→tò mò mới hỏi, khắc biệt sao→khác biệt so) theo ngữ cảnh + chữ phụ đề cháy sẵn trong video (chữ hồng ở các frame 16s/19s/21s) + transcript indexed mà trình duyệt tìm được — cả 3 nguồn khớp nhau từng câu. Thời gian chỉ là gần đúng (Whisper hay bôi từ đầu câu).

## Toàn bộ thoại (theo thứ tự, giữ nguyên lời gốc)

| Thời gian | Người nói | Thoại (giữ nguyên lời gốc) |
|---|---|---|
| ~0:00–0:04 | Chồng | Vợ ơi, ngày xưa vợ nhiều người theo đuổi thế. Sao vợ lại chọn chồng? |
| ~0:04–0:06 | Vợ | Sao chồng lại so sánh mình với người ta thế? |
| ~0:07–0:09 | Chồng | Chồng tò mò mới hỏi mà. |
| ~0:10–0:12 | Vợ | Vì chồng khác biệt so với mọi người? |
| ~0:13–0:15 | Chồng | Khác biệt như nào hả vợ? |
| ~0:15–0:18 | Vợ | Chồng ngủ không ngáy, còn mấy ông kia ngủ ngáy to lắm. |
| ~0:18–0:22 | Vợ | (Bắt chước tiếng ngáy to — Whisper nghe thành lặp lại câu "Mấy ông kia ngủ ngáy to lắm" 2 lần; frame 19s/21s thấy vợ há miệng đang bắt chước, chữ trên màn hình vẫn là "mấy ông kia ngủ ngáy to".) |
| ~0:22–0:26 | — | Không thoại. Chồng bật dậy, hai tay ôm đầu, mặt sốc (frame 24s); vợ ngồi yên bình thản bên cạnh. |
| ~0:26–0:30 | Voiceover outro | Chuyện đời, muôn vẻ. Cười khỏe mỗi ngày. (Cảnh studio: hai người đứng cầm biển "Chuyện đời muôn vẻ" và "Cười khỏe mỗi ngày" — frame 27s.) |

## Bối cảnh hình ảnh

- Phòng khách hiện đại, đèn vàng ấm, sofa be. Vợ mặc váy lụa hai dây màu kem, tóc dài xõa; chồng mặc áo thun be, quần xám, nằm gối đầu lên đùi vợ, vợ vuốt tóc chồng. Tủ rượu gỗ + đèn led phía sau, rèm nâu, tranh treo tường.
- Video có phụ đề cháy sẵn màu hồng, kiểu chữ to ("chồng ngủ ko ngáy", "mấy ông kia ngủ ngáy to").
- Outro là cảnh studio khác hẳn bối cảnh chính (không phải phòng khách), chỉ là tagline kênh — khi chuyển thể thì bỏ outro này.
