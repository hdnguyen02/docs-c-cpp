# Lời giải — [C]. Tài Liệu Học Lập Trình C

[← Quay lại bài học](../01-02-c-tai-lieu-hoc-lap-trinh-c.md)

> Nhiều bài trong bài học này là **việc cần làm thực tế** (đăng ký tài khoản, tạo thư mục…). Phần dưới là hướng dẫn và đáp án tham khảo.

---

### Bài 1.

4 nhược điểm được nêu trong bài:

1. Nội dung quá cũ, không tái bản/chỉnh sửa theo kiến thức hiện hành
2. Không có bài tập hoặc rất ít bài tập
3. Không trực quan
4. Ít hướng dẫn cách tự cài đặt cấu trúc dữ liệu và thuật toán cơ bản bằng C

**Vì sao "nội dung quá cũ" nguy hiểm với người mới:** người mới chưa đủ kiến thức để biết cái gì sai, nên sẽ học và hình thành thói quen xấu, rất khó sửa về sau. Ví dụ các sách cũ (viết cho Turbo C, chuẩn C89) thường dạy:

| Cách cũ trong sách | Cách nên dùng hiện nay |
|---|---|
| `void main()` | `int main(void)` hoặc `int main()` (chuẩn C quy định `main` trả về `int`) |
| `#include <conio.h>`, `clrscr()`, `getch()` | Không dùng — `conio.h` không thuộc chuẩn C, chỉ có trên một số trình biên dịch Windows cũ |
| `gets(s)` để nhập chuỗi | `fgets(s, sizeof(s), stdin)` (`gets` đã bị **xoá khỏi chuẩn C11** vì gây tràn bộ đệm) |
| `fflush(stdin)` để xoá bộ đệm nhập | Đọc bỏ các ký tự thừa bằng `getchar()` — `fflush(stdin)` là hành vi không xác định theo chuẩn |
| Khai báo mọi biến ở đầu hàm, `int i; for (i = 0; ...)` | Từ C99 được khai báo ngay chỗ dùng: `for (int i = 0; ...)` |
| Chỉ dùng comment `/* ... */` | Từ C99 có thêm comment một dòng `// ...` |

### Bài 2.

Đường dẫn tham khảo:

- Geeksforgeeks: https://www.geeksforgeeks.org/c-for-loop/
- Programiz: https://www.programiz.com/c-programming/c-for-loop
- cppreference: https://en.cppreference.com/w/c/language/for

**Nhận xét chung:**

| Trang | Ưu điểm | Nhược điểm |
|---|---|---|
| Programiz | Giao diện sạch, ví dụ ngắn, có output kèm theo — dễ nhất với người mới | Nội dung không sâu |
| Geeksforgeeks | Rất nhiều bài, nhiều biến thể, có bài tập | Quảng cáo nhiều, trình bày hơi rối |
| cppreference (phần C) | Chính xác nhất, đúng chuẩn, ghi rõ tính năng có từ chuẩn nào — dùng để **tra cứu** | Khô khan, khó với người mới |

⚠️ Trên cppreference, phần C nằm ở `en.cppreference.com/w/c`, phần C++ ở `/w/cpp`. Khi tra cứu nhớ chọn đúng phần **C**, vì nhiều hàm cùng tên nhưng cách dùng khác nhau.

Lời khuyên: học khái niệm ở Programiz/Geeksforgeeks, **tra cứu** chi tiết hàm ở cppreference.

### Bài 3.

Hàm `sqrt` — tính căn bậc hai:

| Mục | Nội dung |
|---|---|
| Thư viện | `<math.h>` |
| Tham số | Một số `double`. Truyền số nguyên cũng được, sẽ tự chuyển về `double`. Có thêm `sqrtf` cho `float` và `sqrtl` cho `long double` |
| Trả về | `double` |
| Lưu ý | Truyền số âm → kết quả là `NaN` (không phải số). Trên Linux khi biên dịch với gcc có thể cần thêm `-lm` để liên kết thư viện toán học |

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    printf("%f\n", sqrt(16));    // 4.000000
    printf("%f\n", sqrt(2.0));   // 1.414214
    return 0;
}
```

Biên dịch:

```bash
gcc -std=c11 main.c -o main -lm
```

### Bài 4.

Trên Linux/macOS, tạo bằng terminal:

```bash
mkdir -p c-learning/{chuong-01,chuong-02,chuong-03,chuong-04,chuong-05,chuong-06,chuong-07,chuong-08,chuong-09,chuong-10,ghi-chu}
tree c-learning      # hoặc: ls -R c-learning
```

Trên Windows (Command Prompt):

```bat
mkdir c-learning
cd c-learning
mkdir chuong-01 chuong-02 chuong-03 chuong-04 chuong-05 ghi-chu
```

**Vì sao nên làm:** chia thư mục theo chương giúp bạn tìm lại code cũ nhanh, và khi ôn tập chỉ cần mở đúng thư mục chương đó.

### Bài 5 & Bài 6.

Đây là việc thực hành cá nhân. Gợi ý bài đầu tiên nên nộp:

| Trang | Bài gợi ý |
|---|---|
| Codeforces | Problem **4A — Watermelon** |
| Hackerrank | **"Hello World!" in C** (mục C → Introduction) |
| VNOI | Bài **HELLO** hoặc **A+B** |
| LeetCode | **1. Two Sum** (hơi khó hơn) |

Code mẫu cho bài "A + B":

```c
#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n", a + b);
    return 0;
}
```

**Lưu ý khi nộp bài trên web chấm tự động:**

- Không in thêm bất cứ chữ gì ngoài đáp án. Câu `printf("Nhap a, b: ");` sẽ làm bài bị chấm **sai** vì output không khớp.
- Chọn đúng ngôn ngữ **C** (ví dụ "GNU GCC C11") khi nộp, không chọn nhầm C++.

### Bài 7.

| Trang | Mục đích chính | Phù hợp với |
|---|---|---|
| **Hackerrank** | Luyện tập theo chủ đề, có lộ trình từ dễ tới khó, có riêng mục **C** | **Người mới** — nên bắt đầu ở đây |
| **LeetCode** | Luyện bài phỏng vấn công ty công nghệ | Người đã biết cấu trúc dữ liệu cơ bản |
| **Codeforces** | Thi đấu lập trình (contest) có xếp hạng, độ khó cao | Người đã code vững, muốn thi đấu |
| **VNOI** | Bài tập tiếng Việt, bám sát đề thi HSG/Olympic Việt Nam | Học sinh thi HSG, sinh viên ôn thuật toán |

**Với trình độ mới bắt đầu:** nên khởi đầu bằng **Hackerrank** (mục C → Introduction) hoặc các bài dễ trên **VNOI**, vì đề tiếng Việt và có phân loại rõ ràng.

### Bài 8.

Câu này tuỳ sở thích. Tiêu chí chọn kênh tốt:

- Có lộ trình rõ ràng (playlist theo thứ tự), không phải video rời rạc
- Có code trực tiếp trên màn hình, không chỉ đọc slide
- Có bài tập kèm theo mỗi bài
- Dạy đúng ngôn ngữ **C** (dùng `printf`/`scanf`), không lẫn với C++ (`cout`/`cin`)
- Không dạy các thói quen cũ như `void main()`, `conio.h`, `gets`

### Bài 9.

| Lời khuyên | Hành động cụ thể trong tuần này |
|---|---|
| **Kiên trì** | Học đủ 7/7 ngày, kể cả ngày chỉ học được 30 phút. Đánh dấu ✅ vào lịch mỗi ngày học. |
| **Chăm chỉ** | Đặt báo thức 20h–22h mỗi tối là "giờ code", tắt thông báo điện thoại trong khung giờ đó. |
| **Chủ động** | Khi gặp lỗi, tự Google trước 15 phút rồi mới đi hỏi. Tự tìm thêm 5 bài tập ngoài giáo trình. |
| **Thực hành** | Làm tối thiểu 15 bài tập, gõ lại code bằng tay chứ không copy-paste. |

### Bài 10.

**"Chủ động" trong học lập trình** nghĩa là: tự tìm tài liệu thay vì chờ người khác gửi; tự đọc thông báo lỗi thay vì chụp màn hình gửi đi hỏi ngay; tự thử nghiệm sửa code để hiểu vì sao sai; tự tìm thêm bài tập khi đã làm hết bài được giao.

Ví dụ chuyển câu hỏi thành truy vấn tìm kiếm:

| Câu định đi hỏi | Truy vấn nên gõ |
|---|---|
| "Code em báo lỗi expected ';' là sao ạ?" | `c error expected ';' before '}' token` |
| "Sao nhập chuỗi bằng fgets nó bị bỏ qua ạ?" | `c fgets skipped after scanf` |
| "Làm sao in số thực 2 chữ số thập phân?" | `c printf double 2 decimal places` |
| "Mảng bị lỗi khi chạy" | `c array index out of bounds segmentation fault` |
| "printf báo warning format" | `c warning format '%d' expects argument of type 'int'` |

**Nguyên tắc viết truy vấn tốt:** tiếng Anh + tên ngôn ngữ (`c`, hoặc `c language` cho rõ) + nguyên văn thông báo lỗi (bỏ tên file, bỏ số dòng cụ thể).

### Bài 11.

Quy trình 4 bước trước khi đi hỏi:

1. **Đọc kỹ thông báo lỗi** — lấy đúng số dòng và nội dung lỗi. Luôn sửa lỗi **đầu tiên** trước, vì một lỗi thường kéo theo hàng loạt lỗi giả phía sau.
2. **Kiểm tra dòng đó và dòng ngay trên nó** — 80% lỗi biên dịch của người mới là: thiếu `;`, thiếu `}`, sai chính tả tên biến/hàm, quên `#include` (ví dụ quên `#include <stdio.h>` sẽ bị báo `implicit declaration of function 'printf'`), dùng biến chưa khai báo.
3. **Google nguyên văn thông báo lỗi** (bỏ tên file và số dòng), thêm từ khoá `c`.
4. **Thu nhỏ chương trình** — tạo một file mới chỉ giữ lại đoạn code gây lỗi, chạy thử. Cách này thường giúp bạn tự tìm ra nguyên nhân.

Nếu vẫn không được, khi đi hỏi hãy đưa đủ: **code (dạng text, không phải ảnh) + thông báo lỗi đầy đủ + những gì bạn đã thử**.

### Bài 12.

Mẫu file `ghi-chu/nhat-ky-hoc.md`:

```markdown
# Nhật ký học C

## 2026-09-17
- **Nội dung học:** Bài 02-05 — Nhập xuất với scanf và printf
- **Làm được:** Bài 1–12 (%d, %lld, %.2f, độ rộng %5d)
- **Chưa làm được:** Bài 14 (căn lề bảng) — chưa rõ cách căn trái bằng %-10s
- **Chưa hiểu:** vì sao scanf double phải dùng %lf mà printf lại dùng %f
- **Cần làm tiếp:** đọc lại phần đặc tả định dạng, làm lại bài 14
```

**Vì sao nên ghi nhật ký:** mục "Chưa hiểu" chính là danh sách việc cần làm cho buổi học sau; sau 1 tháng đọc lại bạn sẽ thấy rõ mình tiến bộ tới đâu.

### Bài 13.

| | Đọc hết lý thuyết rồi làm bài tập | Học tới đâu làm bài tập tới đó |
|---|---|---|
| Ưu điểm | Thấy được bức tranh tổng thể, biết cái gì liên quan cái gì | Nhớ lâu, phát hiện ngay chỗ chưa hiểu, có cảm giác tiến bộ mỗi ngày |
| Nhược điểm | Quên gần hết khi bắt đầu làm bài; dễ ảo tưởng "mình hiểu rồi" | Đôi khi không hiểu vì sao cần học phần này |

**Khuyến nghị:** với người mới, cách thứ hai (**học tới đâu làm tới đó**) hiệu quả hơn hẳn. Lập trình là **kỹ năng vận động**, giống học đàn hay học bơi — đọc hiểu không đồng nghĩa với làm được. Hãy áp dụng quy tắc: *đọc xong một mục → gõ lại ví dụ → sửa ví dụ đó theo ý mình → làm 2–3 bài tập của mục đó → mới đọc mục tiếp theo.*

### Bài 14 & Bài 15.

Việc thực hành cá nhân. Mẫu "cam kết học tập":

```
CAM KẾT HỌC C — từ 17/09/2026
1. Học 2 giờ mỗi ngày, tối thiểu 6 ngày/tuần.
2. Khung giờ cố định: 20h00 - 22h00.
3. Tối thiểu 25 bài tập mỗi tuần, gõ tay 100%, không copy-paste.
4. Đủ chỉ tiêu cả tuần -> chủ nhật được nghỉ trọn ngày.
5. Không đủ chỉ tiêu -> học bù vào chủ nhật cho đủ mới được nghỉ.
```
