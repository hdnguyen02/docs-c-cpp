# Lời giải — [C]. Switch Case

[← Quay lại bài học](../03-03-c-switch-case.md)

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap thu (2-8): ");
    scanf("%d", &n);

    switch (n) {
        case 2: printf("Thu Hai\n");  break;
        case 3: printf("Thu Ba\n");   break;
        case 4: printf("Thu Tu\n");   break;
        case 5: printf("Thu Nam\n");  break;
        case 6: printf("Thu Sau\n");  break;
        case 7: printf("Thu Bay\n");  break;
        case 8: printf("Chu Nhat\n"); break;
        default: printf("Khong hop le!\n");
    }
    return 0;
}
```

⚠️ **Không được quên `break`** — nếu thiếu, chương trình sẽ chạy tiếp xuống các `case` bên dưới (xem bài 7).

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int m;
    printf("Nhap thang: ");
    scanf("%d", &m);

    switch (m) {
        case 1: case 3: case 5: case 7:
        case 8: case 10: case 12:
            printf("31 ngay\n");
            break;
        case 4: case 6: case 9: case 11:
            printf("30 ngay\n");
            break;
        case 2:
            printf("28 ngay\n");
            break;
        default:
            printf("Thang khong hop le!\n");
    }
    return 0;
}
```

**Kỹ thuật gộp case:** nhiều `case` liên tiếp không có lệnh giữa chúng sẽ **cùng dùng chung** một khối lệnh. Đây là ứng dụng hợp lệ và hữu ích nhất của "fall-through".

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int m, y;
    printf("Nhap thang va nam: ");
    scanf("%d %d", &m, &y);

    switch (m) {
        case 1: case 3: case 5: case 7:
        case 8: case 10: case 12:
            printf("31 ngay\n");
            break;
        case 4: case 6: case 9: case 11:
            printf("30 ngay\n");
            break;
        case 2: {
            bool nhuan = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
            printf("%d ngay\n", nhuan ? 29 : 28);
            break;
        }
        default:
            printf("Thang khong hop le!\n");
    }
    return 0;
}
```

⚠️ **Chú ý cặp `{ }` quanh `case 2`:** khi cần **khai báo biến mới** bên trong một `case`, hãy bọc nó trong khối `{ }`. Theo chuẩn C11, ngay sau nhãn `case` phải là một **câu lệnh**, còn khai báo biến thì không phải câu lệnh. Tuỳ phiên bản, trình biên dịch sẽ báo lỗi hoặc cảnh báo (với `-pedantic`):

```
error: a label can only be part of a statement and a declaration is not a statement
```

Ngoài ra, các `case` nằm chung một phạm vi, nên biến khai báo ở `case 2` vẫn "nhìn thấy được" ở `default` — nhưng chưa được khởi tạo nếu nhảy thẳng tới đó. Khối `{ }` giới hạn biến trong đúng `case 2`.

💡 `bool` trong C cần `#include <stdbool.h>`.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    double a, b;
    char pt;

    printf("Nhap bieu thuc (vd: 5 + 3): ");
    scanf("%lf %c %lf", &a, &pt, &b);

    switch (pt) {
        case '+':
            printf("%.4f + %.4f = %.4f\n", a, b, a + b);
            break;
        case '-':
            printf("%.4f - %.4f = %.4f\n", a, b, a - b);
            break;
        case '*':
            printf("%.4f * %.4f = %.4f\n", a, b, a * b);
            break;
        case '/':
            if (b == 0) printf("Loi: chia cho 0!\n");
            else        printf("%.4f / %.4f = %.4f\n", a, b, a / b);
            break;
        case '%':
            if ((int)b == 0) printf("Loi: chia du cho 0!\n");
            else printf("%d %% %d = %d\n", (int)a, (int)b, (int)a % (int)b);
            break;
        default:
            printf("Phep toan '%c' khong hop le!\n", pt);
    }
    return 0;
}
```

💡 Chuỗi định dạng `"%lf %c %lf"` đọc được cả `5+3` (không cần dấu cách) lẫn `5 + 3`: dấu cách trong chuỗi định dạng bỏ qua mọi khoảng trắng (kể cả không có khoảng trắng nào), và `%lf` tự dừng khi gặp ký tự không phải số.

⚠️ Muốn in ký tự `%` bằng `printf` phải viết `%%`.

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    switch (c) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
        case 'A': case 'E': case 'I': case 'O': case 'U':
            printf("'%c' la NGUYEN AM\n", c);
            break;
        default:
            printf("'%c' KHONG phai nguyen am\n", c);
    }
    return 0;
}
```

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int thang;
    printf("Nhap thang (1-12): ");
    scanf("%d", &thang);

    switch (thang) {
        case 1: case 2: case 3:
            printf("Mua XUAN\n");  break;
        case 4: case 5: case 6:
            printf("Mua HA\n");    break;
        case 7: case 8: case 9:
            printf("Mua THU\n");   break;
        case 10: case 11: case 12:
            printf("Mua DONG\n");  break;
        default:
            printf("Thang khong hop le!\n");
    }
    return 0;
}
```

💡 Cách gọn hơn: `switch ((thang - 1) / 3)` rồi xét 4 case 0,1,2,3 (nhớ kiểm tra `thang` trong khoảng 1–12 trước).

### Bài 7.

**Với `n = 2`, output là:**

```
Hai Ba Khac
```

**Giải thích — hiện tượng "fall-through" (rơi xuyên qua):**

`switch` **không** chọn đúng một nhánh như `if else`. Nó hoạt động như sau:

1. Tìm nhãn `case` khớp với giá trị → đây chỉ là **điểm nhảy vào**
2. Từ điểm đó, **chạy liên tục mọi câu lệnh phía dưới** cho tới khi gặp `break` hoặc hết `switch`

Với `n = 2`:
```
case 1: bo qua (khong khop)
case 2: <- NHAY VAO DAY, in "Hai "
case 3: khong co break o tren -> chay tiep, in "Ba "
default: van chay tiep, in "Khac"
```

Đây là nguồn lỗi phổ biến nhất khi dùng `switch`. Biên dịch với `-Wimplicit-fallthrough` (gcc) để được cảnh báo.

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    switch (n) {
        case 1: printf("Mot");  break;
        case 2: printf("Hai");  break;
        case 3: printf("Ba");   break;
        default: printf("Khac");
    }
    printf("\n");
    return 0;
}
```

Với `n = 2` → in `Hai`.

**Ghi chú:** `default` là nhánh cuối nên không bắt buộc có `break`. Tuy vậy nhiều người vẫn thêm vào, phòng khi sau này chèn thêm `case` xuống dưới.

Nếu bạn **cố ý** muốn fall-through, hãy ghi chú rõ để người đọc (và compiler) biết. Trong C11, gcc nhận diện comment `/* fall through */` và sẽ không cảnh báo:

```c
case 1:
    lamViecA();
    /* fall through */      // bao cho nguoi doc va gcc biet la co y
case 2:
    lamViecB();
    break;
```

(Chuẩn C23 có thêm cú pháp `[[fallthrough]];` cho mục đích này.)

### Bài 9.

```c
#include <stdio.h>

int main(void) {
    int chon;

    printf("========= MENU =========\n");
    printf("1. Them du lieu\n");
    printf("2. Xoa du lieu\n");
    printf("3. Sua du lieu\n");
    printf("4. Thoat\n");
    printf("========================\n");
    printf("Lua chon cua ban: ");
    scanf("%d", &chon);

    switch (chon) {
        case 1: printf(">> Da chon: THEM du lieu\n"); break;
        case 2: printf(">> Da chon: XOA du lieu\n");  break;
        case 3: printf(">> Da chon: SUA du lieu\n");  break;
        case 4: printf(">> Tam biet!\n");             break;
        default: printf(">> Lua chon khong hop le, vui long chon 1-4!\n");
    }
    return 0;
}
```

Đây là **ứng dụng điển hình nhất** của `switch` — xử lý menu. Trong chương trình thật, phần này được đặt trong vòng lặp `do while` để lặp lại menu cho tới khi người dùng chọn Thoát (xem bài [04-03](../04-03-c-vong-lap-do-while.md)).

### Bài 10.

```c
#include <stdio.h>

int main(void) {
    int diem;
    printf("Nhap diem (0-10): ");
    scanf("%d", &diem);

    switch (diem) {
        case 9: case 10:
            printf("GIOI\n");
            break;
        case 7: case 8:
            printf("KHA\n");
            break;
        case 5: case 6:
            printf("TRUNG BINH\n");
            break;
        case 0: case 1: case 2: case 3: case 4:
            printf("YEU\n");
            break;
        default:
            printf("Diem khong hop le!\n");
    }
    return 0;
}
```

💡 **Mẹo dùng `switch` cho khoảng giá trị:** chia cho một số để thu về ít case hơn.

```c
switch (diem / 2) {         // 0-1 -> 0, 2-3 -> 1, ...
    ...
}
```

Nhưng nói chung, **với khoảng giá trị thì `if else if` phù hợp hơn `switch`** — đặc biệt khi điểm là số thực.

### Bài 11.

```c
double d = 2.5;
switch (d) {                // LOI BIEN DICH
    case 2.5: printf("Hai ruoi"); break;
}
```

Thông báo lỗi (gcc):

```
error: switch quantity not an integer
error: case label does not reduce to an integer constant
```

**Vì sao `switch` không hỗ trợ số thực:**

1. **Cách hoạt động:** compiler thường chuyển `switch` thành một **bảng nhảy (jump table)** — một mảng địa chỉ được đánh chỉ số bằng chính giá trị. Việc này chỉ làm được với giá trị **rời rạc, đếm được**. Số thực là liên tục, không thể đánh chỉ số.

2. **Sai số biểu diễn:** `0.1 + 0.2 != 0.3` (xem bài [02-02](../02-02-c-kieu-du-lieu.md) bài 8). Nếu `switch` cho phép số thực, `case 0.3:` sẽ không bao giờ khớp khi giá trị được tính ra là `0.30000000000000004` — một nguồn lỗi âm thầm.

**Các kiểu `switch` chấp nhận:**

| ✅ Được | ❌ Không được |
|---|---|
| `int`, `short`, `long`, `long long` | `float`, `double`, `long double` |
| `char` (vì là số nguyên) | Chuỗi ký tự (`char[]`, `char *`) |
| `bool` (`_Bool`) | Mảng, con trỏ |
| `enum` | `struct`, `union` |

**Với số thực hoặc chuỗi, dùng `if else if`** (so sánh chuỗi bằng `strcmp` trong `<string.h>`):

```c
if      (fabs(d - 2.5) < 1e-9) { ... }     // fabs trong <math.h>
else if (fabs(d - 3.0) < 1e-9) { ... }
```

### Bài 12.

```c
#include <stdio.h>

int main(void) {
    char donVi;
    double nhietDo;

    printf("Nhap don vi (c = Celsius, f = Fahrenheit): ");
    scanf(" %c", &donVi);
    printf("Nhap nhiet do: ");
    scanf("%lf", &nhietDo);

    switch (donVi) {
        case 'c': case 'C':
            printf("%.2f do C = %.2f do F\n", nhietDo, nhietDo * 9.0 / 5.0 + 32);
            break;
        case 'f': case 'F':
            printf("%.2f do F = %.2f do C\n", nhietDo, (nhietDo - 32) * 5.0 / 9.0);
            break;
        default:
            printf("Don vi khong hop le!\n");
    }
    return 0;
}
```

Ví dụ: `c 100` → `100.00 do C = 212.00 do F`

⚠️ Phải viết `9.0 / 5.0` chứ không phải `9 / 5` — nếu không sẽ bị chia nguyên cho kết quả **1**, và mọi nhiệt độ đều sai.

⚠️ `scanf` đọc `double` phải dùng `%lf` (không phải `%f`).

### Bài 13.

| Tiêu chí | `switch case` | `if else if` |
|---|---|---|
| **Kiểu dữ liệu** | Chỉ số nguyên, `char`, `enum` | Mọi kiểu, mọi biểu thức |
| **Điều kiện** | Chỉ so sánh **bằng** với hằng số | So sánh tuỳ ý: `>`, `<`, `&&`, `\|\|`, gọi hàm… |
| **Nhãn `case`** | Bắt buộc là **hằng số nguyên** lúc biên dịch | Có thể là biến, biểu thức |
| **Tốc độ** | Nhanh hơn khi nhiều nhánh (jump table, O(1)) | Kiểm tra tuần tự, O(n) nhánh |
| **Dễ đọc** | Rất rõ khi có nhiều giá trị rời rạc | Rõ khi là khoảng giá trị |
| **Rủi ro** | Quên `break` → fall-through | Sai thứ tự điều kiện |
| **Gộp nhiều giá trị** | Dễ: `case 1: case 2:` | Phải viết `n == 1 \|\| n == 2` |

**Khi nào dùng `switch`:**
- Menu chọn chức năng
- Xử lý mã trạng thái, mã lỗi, `enum`
- Phân loại theo ký tự (phép toán, phím bấm)
- Khi có ≥ 4 giá trị rời rạc cần so sánh bằng

**Khi nào dùng `if else if`:**
- Điều kiện là **khoảng giá trị** (`diem >= 8.5`)
- Điều kiện phức tạp có `&&`, `||`
- Làm việc với số thực hoặc chuỗi ký tự
- Chỉ có 2–3 nhánh

### Bài 14.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("Nhap mot chu cai: ");
    scanf(" %c", &c);

    if (!isalpha((unsigned char)c)) {
        printf("'%c' khong phai chu cai!\n", c);
        return 1;
    }

    // Doi ve chu thuong -> chi can 5 case thay vi 10
    switch (tolower((unsigned char)c)) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
            printf("'%c' la NGUYEN AM\n", c);
            break;
        default:
            printf("'%c' la PHU AM\n", c);
    }
    return 0;
}
```

**Kỹ thuật:** **chuẩn hoá dữ liệu trước khi phân nhánh**. `tolower(c)` đưa mọi chữ cái về chữ thường, nên chỉ cần viết 5 `case` thay vì 10.

Đây là nguyên tắc chung rất hữu ích: thay vì xử lý mọi biến thể của dữ liệu, hãy đưa chúng về một dạng chuẩn rồi mới xử lý.

`tolower`, `isalpha` nằm trong `<ctype.h>` (xem bài [03-04](../03-04-c-bang-ma-ascii-va-thu-vien-ctypeh.md)).

### Bài 15.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("Nhap ky tu La Ma (I V X L C D M): ");
    scanf(" %c", &c);

    int giaTri;
    switch (toupper((unsigned char)c)) {
        case 'I': giaTri = 1;    break;
        case 'V': giaTri = 5;    break;
        case 'X': giaTri = 10;   break;
        case 'L': giaTri = 50;   break;
        case 'C': giaTri = 100;  break;
        case 'D': giaTri = 500;  break;
        case 'M': giaTri = 1000; break;
        default:
            printf("'%c' khong phai ky tu La Ma!\n", c);
            return 1;
    }

    printf("%c = %d\n", toupper((unsigned char)c), giaTri);
    return 0;
}
```

💡 `toupper` trả về `int`; in bằng `%c` để thấy ký tự thay vì mã số.

**Mẹo nhớ bảng số La Mã:** **I** V **X** L **C** D **M** — "**I** **V**alue **X**ylophones **L**ike **C**ows **D**o **M**ilk".

| Ký tự | Giá trị |
|---|---|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

**Mở rộng — đổi cả chuỗi La Mã sang số** (dùng vòng lặp, chương 4):

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int giaTriLaMa(char c) {
    switch (toupper((unsigned char)c)) {
        case 'I': return 1;    case 'V': return 5;
        case 'X': return 10;   case 'L': return 50;
        case 'C': return 100;  case 'D': return 500;
        case 'M': return 1000;
        default:  return 0;
    }
}

int main(void) {
    char s[100];
    printf("Nhap so La Ma: ");
    scanf("%99s", s);

    size_t len = strlen(s);
    int kq = 0;
    for (size_t i = 0; i < len; i++) {
        int hienTai = giaTriLaMa(s[i]);
        // Neu ky tu hien tai NHO HON ky tu ke tiep -> phep TRU (IV = 4, IX = 9)
        if (i + 1 < len && hienTai < giaTriLaMa(s[i + 1])) {
            kq -= hienTai;
        } else {
            kq += hienTai;
        }
    }

    printf("%s = %d\n", s, kq);
    return 0;
}
```

Ví dụ: `MCMXCIV` = 1994, `XIV` = 14, `IX` = 9.
