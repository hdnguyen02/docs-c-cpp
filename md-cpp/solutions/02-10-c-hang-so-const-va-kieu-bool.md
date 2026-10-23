# Lời giải — [C]. Hằng Số const Và Kiểu bool

[← Quay lại bài học](../02-10-c-hang-so-const-va-kieu-bool.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    printf("255        = %d\n", 255);
    printf("0377       = %d\n", 0377);
    printf("0xFF       = %d\n", 0xFF);
    printf("0x7FFFFFFF = %d\n", 0x7FFFFFFF);
    return 0;
}
```

Output:

```
255        = 255
0377       = 255
0xFF       = 255
0x7FFFFFFF = 2147483647
```

**Giải thích:**
- `0377` bắt đầu bằng `0` → hệ **bát phân**: `3×8² + 7×8 + 7 = 192 + 56 + 7 = 255`
- `0xFF` bắt đầu bằng `0x` → hệ **thập lục phân**: `F×16 + F = 15×16 + 15 = 255`
- `0x7FFFFFFF` là giá trị lớn nhất của `int` 32 bit (`INT_MAX` trong `<limits.h>`)

⚠️ **Bẫy số 0 ở đầu:** viết `int ma = 010;` với ý định là "mười" thì thực ra được **8** (bát phân). Đừng thêm số 0 ở đầu số thập phân.

💡 Muốn **in** ra ở hệ khác thì dùng đặc tả `%o` (bát phân) và `%x` / `%X` (thập lục phân): `printf("%o %X", 255, 255);` → `377 FF`.

### Bài 2.

```c
#include <stdio.h>

int main() {
    printf("sizeof(28)    = %zu\n", sizeof(28));
    printf("sizeof(28L)   = %zu\n", sizeof(28L));
    printf("sizeof(28LL)  = %zu\n", sizeof(28LL));
    printf("sizeof(28U)   = %zu\n", sizeof(28U));
    printf("sizeof(3.14)  = %zu\n", sizeof(3.14));
    printf("sizeof(3.14f) = %zu\n", sizeof(3.14f));
    printf("sizeof('A')   = %zu\n", sizeof('A'));
    printf("sizeof(\"abc\") = %zu\n", sizeof("abc"));
    return 0;
}
```

Output (gcc, Linux 64 bit):

```
sizeof(28)    = 4
sizeof(28L)   = 8
sizeof(28LL)  = 8
sizeof(28U)   = 4
sizeof(3.14)  = 8
sizeof(3.14f) = 4
sizeof('A')   = 4
sizeof("abc") = 4
```

**Giải thích:**
- `'A'` trong C có kiểu **`int`**, không phải `char` → 4 byte. (Trong C++ thì `sizeof('A')` là 1.) Khi gán vào biến `char c = 'A';` thì biến `c` mới chiếm 1 byte.
- `"abc"` là mảng `char` gồm 3 ký tự **cộng ký tự kết thúc `'\0'`** → 4 byte.
- `long` là 8 byte trên Linux 64 bit, nhưng chỉ 4 byte trên Windows — vì vậy khi cần chắc chắn 8 byte hãy dùng `long long`.

⚠️ `sizeof` trả về kiểu `size_t` (số nguyên không dấu), đặc tả đúng là `%zu`. Dùng `%d` sẽ bị gcc cảnh báo `-Wformat`.

### Bài 3.

```c
#include <stdio.h>

int main() {
    const int MAX = 100;
    // MAX = 200;      // bo comment dong nay se bi loi bien dich
    printf("MAX = %d\n", MAX);
    return 0;
}
```

Khi bỏ comment dòng `MAX = 200;`, gcc báo:

```
error: assignment of read-only variable 'MAX'
```

**Giải thích:** `const` biến `MAX` thành **biến chỉ đọc**. Trình biên dịch kiểm tra mọi lệnh gán và từ chối biên dịch nếu có lệnh nào ghi vào `MAX`. Lỗi được phát hiện **lúc biên dịch**, chương trình không bao giờ chạy được với lệnh sai đó.

Các thao tác sau cũng bị lỗi vì đều là ghi vào `MAX`:

```c
MAX++;          // error: increment of read-only variable 'MAX'
MAX += 5;       // error: assignment of read-only variable 'MAX'
scanf("%d", &MAX);   // gcc canh bao: writing into constant object
```

### Bài 4.

```c
#include <stdio.h>

int main() {
    const int x;         // hop le trong C nhung vo dung
    printf("x = %d\n", x);
    return 0;
}
```

gcc **không báo lỗi**, chỉ cảnh báo (khi bật `-Wall`):

```
warning: 'x' is used uninitialized [-Wuninitialized]
```

Chương trình chạy và in ra một giá trị **rác** (có thể là 0, có thể là số bất kỳ).

**Giải thích:**
- Trong C, khai báo `const` không khởi tạo là **hợp lệ** (khác C++, nơi đây là lỗi biên dịch).
- Nhưng vì là `const`, bạn **không thể gán giá trị** cho `x` sau đó → `x` mang giá trị rác mãi mãi → vô dụng.

✅ **Quy tắc:** luôn khởi tạo hằng ngay khi khai báo: `const int x = 10;`

💡 Riêng hằng **toàn cục** (khai báo ngoài hàm) không khởi tạo thì được tự động gán `0`, nhưng cũng chẳng có ý nghĩa gì.

### Bài 5.

```c
#include <stdio.h>

int main() {
    const double PI = 3.14159;
    double r;

    printf("Nhap ban kinh: ");
    scanf("%lf", &r);

    double chuVi   = 2 * PI * r;
    double dienTich = PI * r * r;

    printf("Chu vi    = %.2f\n", chuVi);
    printf("Dien tich = %.2f\n", dienTich);
    return 0;
}
```

Ví dụ `r = 5`:

```
Chu vi    = 31.42
Dien tich = 78.54
```

⚠️ Nhập `double` bằng `scanf` phải dùng **`%lf`**, không phải `%f` (`%f` dành cho `float`). Dùng sai sẽ đọc ra giá trị rác.

💡 Muốn PI chính xác tối đa, có thể dùng `const double PI = acos(-1.0);` (cần `<math.h>` và `-lm`) như bài 02-08.

### Bài 6.

```c
#include <stdio.h>

#define N 5
int a[N];                 // DUNG: N duoc thay bang 5 truoc khi bien dich

// const int M = 5;
// int b[M];              // LOI: variably modified 'b' at file scope

int main() {
    for (int i = 0; i < N; i++) {
        a[i] = (i + 1) * 10;
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}
```

Output: `10 20 30 40 50`

Khi bỏ comment 2 dòng `const int M = 5; int b[M];`, gcc báo:

```
error: variably modified 'b' at file scope
```

**Giải thích:**
- Kích thước mảng **toàn cục** phải là **hằng số biên dịch** (compiler biết chính xác lúc biên dịch).
- `#define N 5` được preprocessor thay thành `int a[5];` → hợp lệ.
- `const int M` trong C chỉ là **biến chỉ đọc**, không được coi là hằng số biên dịch → không dùng làm kích thước mảng toàn cục được.

⚠️ Nếu khai báo `int b[M];` **bên trong hàm** thì gcc chấp nhận, nhưng khi đó `b` là **mảng có độ dài thay đổi** (VLA — variable length array) và **không** khởi tạo được bằng `= {...}`:

```c
void thu(void) {
    const int M = 5;
    int b[M];               // duoc: VLA
    // int c[M] = {1, 2};   // LOI: variable-sized object may not be initialized
    b[0] = 1;
    printf("%d\n", b[0]);
}
```

✅ Cách thay thế trong C: dùng `#define N 5` hoặc `enum { N = 5 };`.

### Bài 7.

```c
#include <stdio.h>

int main() {
    const double TI_LE = 9.0 / 5;     // 1.8
    const double DO_LECH = 32;

    double doC;
    printf("Nhap nhiet do (do C): ");
    scanf("%lf", &doC);

    double doF = doC * TI_LE + DO_LECH;
    printf("%.1f do C = %.1f do F\n", doC, doF);
    return 0;
}
```

Ví dụ:

| Input (°C) | Output (°F) |
|---|---|
| 0 | 32.0 |
| 100 | 212.0 |
| 37 | 98.6 |
| −40 | −40.0 |

⚠️ **Bẫy chia nguyên:** nếu viết `const double TI_LE = 9 / 5;` thì `9 / 5` là phép chia hai số `int` → được `1`, rồi mới chuyển thành `1.0`. Kết quả sai hoàn toàn. Phải viết `9.0 / 5`.

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int a, b;
    printf("Nhap a, b: ");
    scanf("%d %d", &a, &b);

    bool lonHon  = a > b;
    bool bangNhau = a == b;
    bool khacNhau = a != b;

    printf("a >  b : %d (%s)\n", lonHon,   lonHon   ? "true" : "false");
    printf("a == b : %d (%s)\n", bangNhau, bangNhau ? "true" : "false");
    printf("a != b : %d (%s)\n", khacNhau, khacNhau ? "true" : "false");
    return 0;
}
```

Ví dụ `a = 7, b = 3`:

```
a >  b : 1 (true)
a == b : 0 (false)
a != b : 1 (true)
```

💡 `printf` không có đặc tả riêng cho `bool`. Khi truyền vào `printf`, giá trị `bool` được **nâng lên `int`** nên in bằng `%d` là đúng chuẩn.

### Bài 9.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    bool laChan  = (n % 2 == 0);
    bool laDuong = (n > 0);

    printf("%d %s so chan\n", n, laChan ? "la" : "khong la");
    printf("%d %s so duong\n", n, laDuong ? "la" : "khong la");
    return 0;
}
```

Ví dụ `n = -4`:

```
-4 la so chan
-4 khong la so duong
```

⚠️ Kiểm tra số **lẻ** nên viết `n % 2 != 0` chứ **không** viết `n % 2 == 1`, vì trong C `-3 % 2` bằng `-1` (dấu của phép chia lấy dư theo số bị chia).

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool a = 256;
    bool b = -1;
    bool c = 0.0001;
    bool d = '0';
    bool e = '\0';

    printf("a = %d\n", a);
    printf("b = %d\n", b);
    printf("c = %d\n", c);
    printf("d = %d\n", d);
    printf("e = %d\n", e);
    return 0;
}
```

Output:

```
a = 1
b = 1
c = 1
d = 1
e = 0
```

**Giải thích — quy tắc duy nhất: khác 0 → `1`, bằng 0 → `0`.**
- `256`, `-1`: khác 0 → `true`
- `0.0001`: rất nhỏ nhưng vẫn khác 0 → `true` (trong khi `int x = 0.0001;` cho `0`)
- `'0'`: là **ký tự chữ số 0**, có mã ASCII **48** ≠ 0 → `true`. Đây là bẫy hay gặp!
- `'\0'`: là ký tự có mã **0** (ký tự kết thúc chuỗi) → `false`

### Bài 11.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNamNhuan(int nam) {
    return (nam % 400 == 0) || (nam % 4 == 0 && nam % 100 != 0);
}

int main() {
    int nam;
    printf("Nhap nam: ");
    scanf("%d", &nam);

    printf("Nam %d %s nam nhuan\n", nam, laNamNhuan(nam) ? "LA" : "KHONG phai");
    return 0;
}
```

Kiểm thử:

| Năm | Kết quả | Lý do |
|---|---|---|
| 2024 | Nhuận | chia hết cho 4, không chia hết cho 100 |
| 2023 | Không | không chia hết cho 4 |
| 1900 | Không | chia hết cho 100 nhưng không chia hết cho 400 |
| 2000 | Nhuận | chia hết cho 400 |

💡 Hàm trả về `bool` nên đặt tên dạng câu hỏi (`laNamNhuan`, `laSoNguyenTo`, `coTheMua`) để khi đọc `laNamNhuan(nam) ? ... : ...` giống như đọc câu tiếng Việt.

### Bài 12.

```c
#include <stdio.h>

// Khong include <stdbool.h>
#define TRUE  1
#define FALSE 0

int main() {
    _Bool daDangNhap = TRUE;
    _Bool coLoi = FALSE;
    _Bool x = 5;             // _Bool van tu dua ve 1

    printf("daDangNhap = %d\n", daDangNhap);
    printf("coLoi      = %d\n", coLoi);
    printf("x          = %d\n", x);
    printf("sizeof(_Bool) = %zu\n", sizeof(_Bool));
    return 0;
}
```

Output:

```
daDangNhap = 1
coLoi      = 0
x          = 1
sizeof(_Bool) = 1
```

**So sánh:**

| | `_Bool` + `#define TRUE/FALSE` | `<stdbool.h>` |
|---|---|---|
| Tên kiểu | `_Bool` (từ khoá gốc của C99) | `bool` (macro của `_Bool`) |
| Hằng đúng/sai | Tự định nghĩa `TRUE`, `FALSE` | Có sẵn `true`, `false` |
| Cần include | Không | Có |
| Dễ đọc | Kém hơn | ✅ Tốt hơn, giống các ngôn ngữ khác |

✅ Nên dùng `<stdbool.h>`. Cách `#define TRUE 1` hay gặp trong code C cũ (trước C99) — khi đó người ta dùng `int` thay cho `_Bool`, và `int x = 5;` **không** tự đưa về 1 như `_Bool`.

### Bài 13.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    bool a = 256;
    unsigned char c = (unsigned char)256;
    printf("%d %d\n", a, c);
    return 0;
}
```

Output: `1 0`

**Giải thích:**
- **`bool`**: quy tắc là "khác 0 → 1". `256 ≠ 0` → `a = 1`.
- **`unsigned char`** (1 byte, 0..255): giá trị bị **cắt bớt**, chỉ giữ 8 bit thấp. `256` ở hệ nhị phân là `1 0000 0000`, 8 bit thấp đều là 0 → `c = 0`. Nói cách khác `c = 256 % 256 = 0`.

⚠️ Với `unsigned char c = 256;` (không ép kiểu như đề bài), gcc sẽ cảnh báo `-Woverflow`: *unsigned conversion from 'int' to 'unsigned char' changes value from '256' to '0'*. Lời giải trên ép kiểu tường minh để biên dịch sạch.

**Bài học:** `bool` **không phải** một "số nguyên 1 byte" bình thường. Chuyển sang `bool` là phép so sánh với 0, còn chuyển sang kiểu nguyên nhỏ là phép cắt bit.

### Bài 14.

```c
#include <stdio.h>

int main() {
    const long long GIA_MO_CUA = 10000;     // km dau tien
    const long long GIA_MOI_KM = 12000;     // moi km tiep theo

    int soKm;
    printf("Nhap so km: ");
    scanf("%d", &soKm);

    long long tien = GIA_MO_CUA + (long long)(soKm - 1) * GIA_MOI_KM;

    printf("So tien phai tra: %lld dong\n", tien);
    return 0;
}
```

Ví dụ:

| Số km | Tiền |
|---|---|
| 1 | 10000 |
| 5 | 10000 + 4 × 12000 = 58000 |
| 30 | 10000 + 29 × 12000 = 358000 |

💡 Nếu sau này giá cước thay đổi, bạn chỉ cần sửa **1 dòng** khai báo hằng, không phải đi tìm từng con số `12000` rải rác trong code. Đó là lợi ích lớn nhất của việc đặt tên cho hằng số (tránh *magic number*).

### Bài 15.

Code gốc có **3 lỗi**:

| Dòng | Lỗi | Thông báo gcc |
|---|---|---|
| `int a[SIZE];` | `const int` không phải hằng số biên dịch, không làm kích thước mảng toàn cục được | `variably modified 'a' at file scope` |
| `TI_LE = 0.2;` | Gán giá trị cho hằng | `assignment of read-only variable 'TI_LE'` |
| `bool ok = true;` | Thiếu `#include <stdbool.h>` | `unknown type name 'bool'` và `'true' undeclared` |

Code đã sửa:

```c
#include <stdio.h>
#include <stdbool.h>       // sua loi 3: can cho bool, true, false

#define SIZE 3             // sua loi 1: dung #define thay cho const int
int a[SIZE];

int main() {
    double tiLe = 0.1;     // sua loi 2: muon thay doi thi khong dung const
    tiLe = 0.2;
    bool ok = true;
    printf("%d %f\n", ok, tiLe);
    printf("sizeof(a) = %zu\n", sizeof(a));
    return 0;
}
```

Output:

```
1 0.200000
sizeof(a) = 12
```

💡 Với lỗi 2 có 2 cách sửa tuỳ ý đồ: nếu tỉ lệ **thực sự không đổi** thì giữ `const` và **xoá** dòng gán; nếu cần thay đổi thì bỏ `const` (và đổi tên sang kiểu biến thường `tiLe` cho khỏi nhầm là hằng).
