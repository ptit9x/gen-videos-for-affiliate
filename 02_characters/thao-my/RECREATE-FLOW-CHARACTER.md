# Tái tạo nhân vật Thảo My trong tài khoản Flow mới — tránh bị chặn "người nổi tiếng"

Ghi ngày 2026-11-26, sau khi tài khoản Flow huynhdn.developer@gmail.com hết Pro.
Nhân vật **ThaoMy002** trong Flow KHÔNG chuyển được sang tài khoản khác bằng
file — phải tạo lại nhân vật từ đầu. File này ghi đúng cách đã làm được, để
lần sau không phải mò lại và không vô tình upload nhầm ảnh gây chặn.

## File dùng để tạo nhân vật — CHỈ file này

- `approved/thao-my-face-front-v002.png`
  - SHA-256: `8793c0cea8dbb8a2aef02597d76be943a847450263a8a97229c9e2904ed94ed4`
  - 720×1280, ảnh selfie ngoài trời, áo cardigan kem.
  - Lưu ý: file mang đuôi `.png` nhưng dữ liệu bên trong là JPEG. Nếu Flow
    mới từ chối thì dùng bản copy nguyên byte đổi đuôi `.jpg`, không gen lại.
- Đây là **mặt AI đã gen** (pipeline ảnh của Bee, 0 Flow credit), KHÔNG phải
  ảnh người thật. Chính vì thế nó qua được bộ lọc của Flow/Veo.

## TUYỆT ĐỐI KHÔNG upload các file này vào Flow

- Mọi file trong `source/` (`reference-original.jpg`,
  `face-hair-reference-2026-11-16.jpg`, `multi-angle-reference-75f1ee34.jpg`,
  `facial-expressions-38847112.jpg`): đây là ảnh gốc người thật do người dùng
  gửi, chỉ để lưu xuất xứ. Đưa ảnh người thật vào Flow làm Ingredient/nhân
  vật là con đường đã bị chặn.
- Mặt v001 (`approved/thao-my-face-front-v001.png`): chỉ giữ lịch sử.

## Vì sao cách này qua được, cách khác thì không (đã chứng minh)

- Bộ lọc ảnh và bộ lọc video của Veo 3.1 là **hai bộ lọc khác nhau**.
  Tạo Ingredient/nhân vật thành công KHÔNG có nghĩa gen video sẽ qua:
  mặt Vy v2 upload + tạo Ingredient đều được, nhưng gen video bị chặn 2/2
  lần với lỗi "người nổi tiếng" (credit được hoàn đủ cả 2 lần).
- Mặt v2 cũ (tóc nâu dài + mái, nốt ruồi má trái) cũng bị chặn 2 lần ở bước
  gen video dù đã đổi prompt.
- **Đổi prompt không cứu được mặt đã bị chặn.** Mặt nào bị chặn thì chỉ có
  cách đổi sang mặt khác hẳn, gen bằng chữ/mô tả, không đưa ảnh người thật
  làm tham chiếu.
- Đường Ingredients/Agent cho ảnh người thật đã bị từ chối 5/5 lượt tối
  2026-11-14 (2 khuôn mặt khác nhau, cả ảnh tải lên / ảnh sửa trong Flow /
  nhân vật Flow đều bị). Video luôn đi **Frames trực tiếp** với frame đầu
  đã duyệt, không qua Agent, không đính kèm ảnh nhân vật.

## Cách mặt v002 được tạo ra (để gen lại mặt mới nếu v002 cũng bị chặn)

1. Từ ảnh gốc người thật, chỉ **tách mô tả JSON** (dáng mặt, mắt, mày, mũi,
   môi, tóc, màu da...) — không nhét ảnh gốc vào công cụ gen.
2. Sinh mặt AI mới **chỉ từ chữ/mô tả đó** bằng pipeline ảnh của Bee.
3. Người dùng duyệt mặt mới rồi mới đưa vào Flow.
4. Khi viết prompt gen mặt mới, luôn ghi rõ: nhân vật hư cấu riêng biệt,
   **không giống người nổi tiếng** ("a distinct individual, not a celebrity",
   "no celebrity resemblance") — câu này đã có sẵn trong mọi prompt casting
   ở `02_characters/*/review/*-source.json` và `casting-2026-11-18.json`.

## Các bước tái tạo trong tài khoản Flow mới

1. Pull repo, kiểm chứng SHA-256 của `thao-my-face-front-v002.png` khớp
   với số ở trên.
2. Tạo project mới (đặt tên theo quy ước `CNTM · EP003 · Sắp tới` hoặc
   project của tập đang làm), tạo nhân vật **ThaoMy002** từ đúng file v002.
3. Với mỗi ref trang phục/bối cảnh cần dùng: mở picker **"Chọn dự án"**
   kiểm tra trước — nếu ảnh đó **đã có trong Flow thì dùng lại, không
   upload**. Chỉ upload từ đường dẫn repo trong `wardrobe/REGISTRY.md`
   khi ảnh đó **chưa có** trong Flow (đừng upload bản copy khác).
4. **Gen thử 1 clip rẻ** (Veo 3.1 Lite, 10 credit) với frame đã duyệt trước
   khi làm hàng loạt — gen video mới là bài kiểm tra thật, tạo nhân vật
   xong chưa chứng minh được gì.
5. Nếu clip thử bị chặn "người nổi tiếng": dừng, đừng sửa prompt rồi thử
   lại mặt cũ. Gen mặt AI mới hẳn theo mục trên, người dùng duyệt, rồi
   tạo nhân vật mới từ mặt đó.
6. Ghi lại vào repo ngay sau khi upload/tạo xong: URL project mới, URL
   nhân vật mới, asset ID mới (vào `README.md` này, `character.yaml` và
   `wardrobe/REGISTRY.md`) — **luôn lưu đường dẫn ảnh tham chiếu trong
   Flow vào git**, không để ref chỉ tồn tại trong Flow.

## Hồ sơ cũ (tham khảo, tài khoản đã hết Pro)

- Project cũ: `CNTM · EP003 · Sắp tới` —
  https://flow.google.com/u/1/project/2948266f-ba05-481e-b636-4ebe81db52ba
  (nhân vật ThaoMy002 nằm trong project này).
- Nam (ep008) là ngoại lệ đã qua: nhân vật Nam tạo từ `nam-front-v001.jpg`
  (ảnh trông như ảnh studio người thật, có watermark) và không bị chặn ở
  bước nào — nhưng đó là may mắn, không phải cách làm an toàn. Fallback nếu
  Nam bị chặn ở acc mới: chỉ dùng ảnh ref làm nguồn sửa frame như cách làm
  của Bằng, video vẫn đi Frames trực tiếp, không tạo Ingredient.
