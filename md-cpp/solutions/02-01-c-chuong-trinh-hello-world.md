# Lời giải — [C]. Chương Trình Hello World

[← Quay lại bài học](../02-01-c-chuong-trinh-hello-world.md)

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    printf("Xin chao, toi dang hoc C\n");
    return 0;
}
```

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    printf("Ho ten: Nguyen Van A\n");
    printf("Lop: 12A1\n");
    printf("So thich: Lap trinh\n");
    return 0;
}
```

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    printf("Ho ten: Nguyen Van A\nLop: 12A1\nSo thich: Lap trinh\n");
    return 0;
}
```

**Giải thích:** `\n` là **ký tự** xuống dòng nằm ngay trong chuỗi, nên gộp được cả 3 dòng vào một lệnh `printf`.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    printf("**********\n");
    printf("**********\n");
    printf("**********\n");
    printf("**********\n");
    printf("**********\n");
    return 0;
}
```

Hoặc gọn hơn:

```c
#include <stdio.h>

int main(void) {
    printf("**********\n**********\n**********\n**********\n**********\n");
    return 0;
}
```

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    printf("*\n");
    printf("**\n");
    printf("***\n");
    printf("****\n");
    printf("*****\n");
    return 0;
}
```

*(Sau khi học vòng lặp `for` ở chương 4, bạn sẽ viết bài này chỉ bằng 3 dòng.)*

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    printf("  #####  \n");
    printf(" #     # \n");
    printf("#        \n");
    printf("#        \n");
    printf("#        \n");
    printf(" #     # \n");
    printf("  #####  \n");
    return 0;
}
```

### Bài 7.

```c
#include <stdio.h>

int main(void) {
    puts("Hello World !");
    puts("codelab tutorial !");
    return 0;
}
```

**Giải thích:** `puts` **tự động thêm ký tự xuống dòng** sau khi in, nên không cần `\n` ở cuối chuỗi. Nếu vẫn viết `puts("Hello World !\n");` thì sẽ bị xuống dòng **2 lần** (thừa một dòng trống).

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    printf("Toi thich ngon ngu \"C\" nhat.\n");
    return 0;
}
```

**Giải thích:** dấu `"` dùng để đánh dấu đầu/cuối chuỗi, nên muốn in chính dấu `"` phải **thoát ký tự** bằng `\"`.

Các ký tự thoát (escape sequence) thường gặp:

| Viết | Ý nghĩa |
|---|---|
| `\n` | Xuống dòng |
| `\t` | Dấu tab |
| `\\` | Dấu `\` |
| `\"` | Dấu nháy kép |
| `\'` | Dấu nháy đơn |
| `\0` | Ký tự null (kết thúc chuỗi trong C) |

⚠️ Riêng với `printf`, dấu `%` có ý nghĩa đặc biệt (bắt đầu một đặc tả như `%d`, `%s`). Muốn in chính dấu `%` phải viết `%%`: `printf("Giam gia 50%%\n");` → `Giam gia 50%`.

### Bài 9.

```c
#include <stdio.h>

int main(void) {
    printf("C:\\Users\\Admin\\Documents\\c\n");
    return 0;
}
```

**Giải thích:** `\` là ký tự mở đầu chuỗi thoát, nên muốn in một dấu `\` phải viết `\\`.

⚠️ Nếu viết `printf("C:\Users\Admin");` thì `\U` và `\A` không phải chuỗi thoát hợp lệ → compiler báo lỗi hoặc cảnh báo và kết quả sai.

*(Khác với C++, C không có "raw string literal" `R"(...)"`, nên cách duy nhất là nhân đôi dấu `\`.)*

### Bài 10.

```c
#include <stdio.h>

int main(void) {
    printf("STT\tTen\t\tDiem\n");
    printf("1\tAn\t\t9.5\n");
    printf("2\tBinh\t8.0\n");
    printf("3\tChi\t\t7.5\n");
    return 0;
}
```

**Giải thích:** `\t` nhảy tới mốc tab tiếp theo (thường cách nhau 8 ký tự). Vì "An" và "Chi" ngắn hơn "Binh", chúng cần **2 tab** mới sang được cột kế tiếp.

Đây chính là nhược điểm của `\t`: căn lề không ổn định. Cách chuẩn hơn là dùng **độ rộng** trong đặc tả của `printf` (xem bài [02-05](../02-05-c-nhap-xuat-voi-scanf-va-printf.md)): `%-6s` nghĩa là in chuỗi trong ô rộng 6 ký tự, căn trái.

```c
#include <stdio.h>

int main(void) {
    printf("%-6s%-10s%s\n", "STT", "Ten", "Diem");
    printf("%-6d%-10s%.1f\n", 1, "An",   9.5);
    printf("%-6d%-10s%.1f\n", 2, "Binh", 8.0);
    printf("%-6d%-10s%.1f\n", 3, "Chi",  7.5);
    return 0;
}
```

Output:

```
STT   Ten       Diem
1     An        9.5
2     Binh      8.0
3     Chi       7.5
```

### Bài 11.

**Output:**

```
A
```

**Giải thích:** `return 0;` trong `main` kết thúc hàm `main` ngay lập tức, tức là kết thúc chương trình. Mọi câu lệnh phía sau nó **không bao giờ được thực thi** — gọi là *dead code* (mã chết).

gcc hiện nay không cảnh báo về mã chết (tuỳ chọn `-Wunreachable-code` của gcc được giữ lại nhưng không còn tác dụng). Trình biên dịch clang thì có cảnh báo khi bật `-Wunreachable-code`:

```
warning: code will never be executed [-Wunreachable-code]
```

### Bài 12.

4 lỗi trong chương trình:

| # | Lỗi | Sửa |
|---|---|---|
| 1 | Thiếu `#include <stdio.h>` — không có thư viện thì không dùng được `printf` | thêm `#include <stdio.h>` |
| 2 | `Printf` viết hoa chữ P — C **phân biệt hoa thường** | `printf` |
| 3 | Thiếu `;` sau `printf("Hello World")` | thêm `;` |
| 4 | Thiếu `;` sau `return 0` | thêm `;` |

Chương trình sau khi sửa:

```c
#include <stdio.h>

int main(void) {
    printf("Hello World");
    return 0;
}
```

### Bài 13.

```c
#include <stdio.h>

int main(void) {
    printf("Chuong trinh ket thuc voi ma 1\n");
    return 1;
}
```

Kiểm tra mã thoát:

```bash
# Linux / macOS
gcc baitap13.c -o baitap13
./baitap13
echo $?        # in ra: 1
```

```bat
REM Windows (cmd)
gcc baitap13.c -o baitap13.exe
baitap13.exe
echo %errorlevel%     REM in ra: 1
```

**Giải thích:** giá trị `main` trả về chính là **mã thoát (exit code)** báo cho hệ điều hành biết chương trình kết thúc thế nào. Theo quy ước: `0` = thành công, khác `0` = có lỗi. Các script tự động (build script, CI) dựa vào mã này để biết bước trước có thành công hay không.

### Bài 14.

```c
#include <stdio.h>

int main(void) {
    // printf KHONG tu xuong dong, muon xuong dong phai tu them \n
    printf("Dong 1 dung printf");
    printf(" - van tren dong 1\n");

    // puts in chuoi roi TU DONG xuong dong
    puts("Dong 2 dung puts");

    // printf dinh dang duoc noi dung bang dac ta %s, %d...
    printf("Dong %d dung printf co dac ta %s\n", 3, "%d va %s");

    // puts in NGUYEN VAN chuoi, ky tu % khong co y nghia dac biet
    puts("Dong 4: puts in nguyen 100% va %d");
    return 0;
}
```

Output:

```
Dong 1 dung printf - van tren dong 1
Dong 2 dung puts
Dong 3 dung printf co dac ta %d va %s
Dong 4: puts in nguyen 100% va %d
```

| | `printf` | `puts` |
|---|---|---|
| Tự xuống dòng | Không, phải tự thêm `\n` | **Có**, luôn thêm `\n` sau chuỗi |
| Định dạng (`%d`, `%s`, `%f`…) | Có | Không, in nguyên văn |
| In được | Chuỗi, số, ký tự… (qua đặc tả) | Chỉ một chuỗi |
| Nên dùng khi | In kèm giá trị biến, cần căn lề | In một dòng chữ cố định |

**Lưu ý về bộ đệm (buffer):** `printf` và `puts` không ghi thẳng ra màn hình mà gom dữ liệu vào bộ nhớ đệm rồi mới đẩy ra. Khi in ra màn hình (terminal), bộ đệm thường được đẩy ra mỗi khi gặp ký tự xuống dòng. Nếu cần đẩy ngay lập tức (ví dụ trước khi chương trình có thể bị crash), dùng `fflush(stdout);`.

### Bài 15.

```c
#include <stdio.h>

int main(void) {
    printf("+----------------------------+\n");
    printf("|                            |\n");
    printf("|      NGUYEN VAN A          |\n");
    printf("|      C Developer           |\n");
    printf("|      nguyenvana@mail.com   |\n");
    printf("|                            |\n");
    printf("+----------------------------+\n");
    return 0;
}
```

**Mẹo căn khung:** đếm số ký tự của dòng viền trên (`+` + 28 dấu `-` + `+` = 30 ký tự). Mọi dòng bên trong cũng phải đúng 30 ký tự: `|` + 28 ký tự nội dung (đệm bằng dấu cách) + `|`.
