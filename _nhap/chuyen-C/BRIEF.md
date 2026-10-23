# Brief: chuyển khoá "C++ Cơ Bản" thành khoá "C Cơ Bản"

Thư mục gốc: /home/devnguyenho/Desktop/docs-cpp
Bảng đổi tên: _nhap/chuyen-C/mapping.tsv (old_stem, new_stem, new_title, ghi_chu)
Bản gốc đã sao lưu ở _nhap/backup-cpp-truoc-chuyen-C/ (đọc từ đây nếu file gốc đã bị đổi tên).

## Với MỖI bài được giao, làm 3 file:
1. `md-cpp/<old>.md`  → viết `md-cpp/<new>.md`, rồi xoá file cũ (nếu tên khác).
2. `md-cpp/solutions/<old>.md` → viết `md-cpp/solutions/<new>.md`, xoá file cũ.
3. `slides-cpp/<old>.json` → viết `slides-cpp/<new>.json`, xoá file cũ.
KHÔNG đụng tới file của bài khác, README.md, toc.json, ppt-cpp/ (người điều phối lo).

## Quy tắc nội dung
- Ngôn ngữ là **C chuẩn (C11)**, KHÔNG còn bất kỳ thứ gì của C++: iostream, cin/cout, endl, using namespace std,
  std::string, bits/stdc++.h, vector, map, pair, auto (kiểu suy luận), tham chiếu `int &x`, đối số mặc định,
  nạp chồng hàm, new/delete, nullptr, bool không include, `sort`, `__gcd`, `max/min/swap` của algorithm, getline, cin.ignore, stringstream, range-based for, class, template.
- Thay bằng: `#include <stdio.h>`, printf/scanf (đúng đặc tả: %d, %lld, %u, %f, %.2f, %lf khi scanf double, %c, %s, %zu cho size_t),
  `<stdbool.h>`, `<string.h>`, `<ctype.h>`, `<math.h>`, `<stdlib.h>`, mảng char, con trỏ, malloc/free, qsort, tự viết max/min/swap/gcd khi cần.
- Mọi chữ "C++" chỉ ngôn ngữ đổi thành "C". Tiêu đề H1 là `# <new_title>`. Khối code dùng ```c thay ```cpp.
- Bài bình thường: giữ nguyên cấu trúc, giọng văn, ví dụ, giải thích; chỉ chuyển cú pháp và sửa những câu giải thích
  chỉ đúng với C++ (vd: "C++ hỗ trợ overload" → "C không hỗ trợ overload"). Không thêm thông tin sai.
- Bài có ghi_chu "THAY": viết lại nội dung bài theo chủ đề mới, dài và chi tiết tương đương bài cũ, cùng phong cách
  (mục đánh số in đậm, ví dụ code + Output + Giải thích). Có thể tái dùng phần nào của bài cũ còn đúng với C.
- Ảnh `![](../images/...)`: xem ảnh bằng tool Read. Ảnh chỉ sơ đồ chung (sơ đồ khối, minh hoạ bộ nhớ) thì giữ.
  Ảnh chụp code/output/IDE mang tính C++ (cout, .cpp, iostream...) thì bỏ, thay bằng khối code/đoạn text tương đương nếu cần.
- Mục "## 🎯 BÀI TẬP": giữ 15 bài; chỉnh đề cho hợp C (bài dùng string/vector/pair → mảng char/mảng/struct).
  Bài "THAY" thì viết 15 bài tập mới theo chủ đề mới. Dòng link lời giải trỏ tới `solutions/<new>.md`.
- Link giữa các bài: đổi mọi `<old>.md` thành `<new>.md` theo mapping.tsv (kể cả bài khác được nhắc tới).

## Lời giải (solutions/<new>.md)
- Tiêu đề: `# Lời giải — <new_title>`; dòng `[← Quay lại bài học](../<new>.md)`.
- Mỗi bài 1 chương trình C đầy đủ (có #include, int main). Giữ các ghi chú 💡 ⚠️ bảng biểu, sửa cho đúng với C.
- **BẮT BUỘC kiểm tra biên dịch**: tách từng khối ```c đầy đủ (có main) ra file trong scratchpad của bạn và chạy
  `gcc -std=c11 -Wall -Wextra -Werror=implicit-function-declaration -c file.c -o /dev/null` (thêm `-lm` khi link nếu có).
  Khối không có main (đoạn code minh hoạ) thì không cần. Sửa hết lỗi; cảnh báo nên sửa. Chạy thử vài chương trình với input mẫu.
- Không để mã bị lỗi. Không dùng gets. Dùng `%lld` cho long long.

## Outline slide (slides-cpp/<new>.json)
- Theo đúng SLIDE-SPEC.md ở thư mục gốc (đọc file đó). `"course": "C Cơ Bản"`, `title` = new_title bỏ tiền tố "[C]. ".
- Cô đọng từ bài md MỚI. Code trong slide cũng là C (printf thay cout...).
- Kiểm tra: `python3 check_slides.py` chấp nhận (có thể chạy `python3 -c "import json;json.load(open('...'))"`).

## Báo cáo cuối
Trả về ngắn gọn: danh sách file đã tạo/xoá, số khối code đã biên dịch thành công / tổng, bất cứ chỗ nào bạn còn nghi ngờ.
