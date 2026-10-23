# Đặc tả: cô đọng bài giảng .md thành outline slide .json

## Mục tiêu
Biến một bài giảng dài (bê nguyên văn từ blog) thành **slide dạy học cô đọng**:
người xem nắm được logic bài học chỉ bằng slide, không cần đọc lại văn xuôi.

## Schema JSON (UTF-8, tiếng Việt)
```json
{
  "title": "Vòng Lặp For",
  "course": "C++ Cơ Bản · ",
  "source": "
  "slides": [
    { "title": "Tiêu đề slide", "bullets": ["ý 1", "ý 2"], "code": "...", "caption": "câu dẫn ngắn" }
  ]
}
```
- `title` của bài: bỏ tiền tố `[C++].` / `[STL].` trong tiêu đề md.
- `course`: đúng chuỗi được giao trong brief.
- `source`: lấy từ dòng `> Nguồn:` trong md.
- Mỗi slide: `title` bắt buộc; `bullets`, `code`, `caption` đều tuỳ chọn nhưng phải có ít nhất `bullets` hoặc `code`.

## Quy tắc cô đọng (bắt buộc)
1. **6–9 slide/bài**. Bài rất dài tối đa 12. Không bao giờ 1 slide cho 1 đoạn văn.
2. **Bullet ≤ 5 slide**, mỗi bullet **≤ 16 từ**, viết như gạch đầu dòng giảng bài, không phải câu văn xuôi cắt ra.
3. **Không chèn ảnh.** Bỏ mọi `![](...)`. Nếu ảnh là sơ đồ khối quan trọng, diễn đạt lại bằng 3–4 bullet.
4. **Code rút gọn**: giữ phần cốt lõi, bỏ `#include`, `using namespace std;`, `int main(){...return 0;}` khi không cần.
   Tối đa **14 dòng/slide**, dòng ≤ 80 ký tự. Gộp nhiều ví dụ cùng dạng vào 1 slide bằng comment ngăn cách.
5. **Output mẫu** chỉ giữ khi giúp hiểu bài; viết dạng comment trong code (`// 1 2 3 ... n`) thay vì slide riêng.
6. **Slide cuối luôn là "Ghi nhớ"**: 3–5 ý cốt lõi, gồm cả lỗi thường gặp nếu bài có nói.
7. Bỏ hẳn: mục "NỘI DUNG" liệt kê đầu bài, "Video Tutorial", lời chào, quảng cáo khoá học, link nội bộ.
8. **Không bịa kiến thức ngoài bài.** Chỉ cô đọng cái bài đã dạy. Được phép diễn đạt lại cho gọn.
9. Thuật ngữ kỹ thuật giữ nguyên tiếng Anh: `for`, `break`, `pointer`, `iterator`, `std::sort`... Phần giải thích viết tiếng Việt.
10. Đánh dấu trong bullet: `**đậm**` cho từ khoá, `` `code` `` cho tên hàm/biến. Trong `code` không dùng markdown.

## Tên file
JSON đặt cùng tên file md, đổi đuôi: `04-01-cpp-vong-lap-for.md` → `04-01-cpp-vong-lap-for.json`

## Kiểm tra trước khi nộp
- `python3 -c "import json;json.load(open('<file>.json'))"` chạy sạch cho từng file.
- Xuống dòng trong `code` là `\n` trong chuỗi JSON, không phải xuống dòng thật.
