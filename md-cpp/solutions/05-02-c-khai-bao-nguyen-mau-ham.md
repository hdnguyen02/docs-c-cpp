# Lời giải — [C]. Khai Báo Nguyên Mẫu Hàm

[← Quay lại bài học](../05-02-c-khai-bao-nguyen-mau-ham.md)

> **Nguyên mẫu hàm (function prototype)** = lời "báo trước" cho compiler về tên hàm, kiểu trả về và danh sách tham số — chưa có phần thân.

---

### Bài 1.

```c
#include <stdio.h>

int tong(int a, int b);        // NGUYEN MAU - ket thuc bang dau ;

int main(void) {
    printf("3 + 5 = %d\n", tong(3, 5));
    return 0;
}

int tong(int a, int b) {       // DINH NGHIA - co than ham
    return a + b;
}
```

**Vì sao cần:** compiler đọc file từ trên xuống. Nguyên mẫu cho nó biết "sẽ có một hàm tên `tong`, nhận 2 `int`, trả về `int`" — đủ để kiểm tra lời gọi ở `main` là hợp lệ. Phần thân hàm tìm sau cũng được (ở bước **liên kết**).

### Bài 2.

```c
#include <stdio.h>

// ============ NGUYEN MAU ============
int    tong(int a, int b);
int    hieu(int a, int b);
int    tich(int a, int b);
double thuong(int a, int b);
void   inKetQua(int a, int b);

// ============ CHUONG TRINH CHINH ============
int main(void) {
    int x, y;
    printf("Nhap 2 so: ");
    scanf("%d %d", &x, &y);
    inKetQua(x, y);
    return 0;
}

// ============ DINH NGHIA ============
int tong(int a, int b)    { return a + b; }
int hieu(int a, int b)    { return a - b; }
int tich(int a, int b)    { return a * b; }

double thuong(int a, int b) {
    if (b == 0) return 0;
    return (double)a / b;
}

void inKetQua(int a, int b) {
    printf("Tong   = %d\n", tong(a, b));
    printf("Hieu   = %d\n", hieu(a, b));
    printf("Tich   = %d\n", tich(a, b));
    printf("Thuong = %.4f\n", thuong(a, b));
}
```

💡 **Đây là cách tổ chức file được khuyến nghị:** người đọc nhìn phần nguyên mẫu ở đầu là biết ngay chương trình có những chức năng gì, không phải cuộn xuống tìm.

### Bài 3.

**KHÔNG bắt buộc ghi tên tham số** trong nguyên mẫu — compiler chỉ cần biết **kiểu**.

```c
#include <stdio.h>

int tong(int, int);              // HOP LE - khong co ten tham so
double dienTich(double, double);
void inBang(int, char);

int main(void) {
    printf("%d\n", tong(3, 5));
    return 0;
}

int tong(int a, int b) { return a + b; }
```

Cả hai cách đều biên dịch được:

```c
int tong(int a, int b);     // co ten  <- NEN DUNG
int tong(int, int);         // khong ten
```

✅ **Nên ghi tên tham số** vì nó là tài liệu cho người đọc:

```c
void veHinhChuNhat(int, int);              // 2 so gi? dai rong? hay toa do?
void veHinhChuNhat(int dai, int rong);     // RO RANG
```

⚠️ Trong **định nghĩa** hàm của C (trước C23) thì **bắt buộc** phải có tên cho mọi tham số.

⚠️ Hàm không có tham số: nguyên mẫu nên viết `void f(void);` chứ không phải `void f();` — cặp ngoặc rỗng trong C (trước C23) nghĩa là "không nói gì về tham số", compiler sẽ không bắt lỗi khi gọi `f(1, 2, 3)`.

### Bài 4.

```c
#include <stdio.h>

int tinhTong(int a, int b);                                   // nguyen mau: tra ve int
int main(void){ printf("%d\n", tinhTong(3, 5)); return 0; }
double tinhTong(int a, int b){ return a + b; }                // dinh nghia: tra ve double
```

**Lỗi:** kiểu trả về trong nguyên mẫu (`int`) **không khớp** với định nghĩa (`double`).

Thông báo lỗi của gcc:

```
error: conflicting types for 'tinhTong'; have 'double(int,  int)'
note: previous declaration of 'tinhTong' with type 'int(int,  int)'
```

**Sửa:** cho khớp nhau (chọn một trong hai), ví dụ:

```c
#include <stdio.h>

int tinhTong(int a, int b);

int main(void) {
    printf("%d\n", tinhTong(3, 5));
    return 0;
}

int tinhTong(int a, int b) { return a + b; }
```

⚠️ Trong C, một tên hàm chỉ ứng với **đúng một** kiểu hàm. Mọi khai báo của cùng một tên phải giống nhau về kiểu trả về và kiểu tham số, nếu không là **xung đột khai báo** (`conflicting types`).

### Bài 5.

```c
#include <stdio.h>

int f(int x);
int main(void){ printf("%d\n", f(5)); return 0; }
// KHONG CO DINH NGHIA cua f
```

**Lỗi:** hàm được **khai báo** nhưng không được **định nghĩa** ở đâu cả.

Điều thú vị: lỗi này **không** xảy ra ở bước biên dịch (compiler tin lời hứa của nguyên mẫu), mà ở bước **liên kết (linking)**:

```
undefined reference to `f'
collect2: error: ld returned 1 exit status
```

**Sửa:** bổ sung định nghĩa hàm:

```c
#include <stdio.h>

int f(int x);

int main(void) {
    printf("%d\n", f(5));
    return 0;
}

int f(int x) { return x * 2; }
```

**Phân biệt 2 loại lỗi:**

| | Lỗi biên dịch (compile error) | Lỗi liên kết (link error) |
|---|---|---|
| Khi nào | Khi dịch từng file `.c` | Khi ghép các file `.o` lại |
| Ví dụ | Thiếu `;`, sai cú pháp, biến chưa khai báo | `undefined reference`, thiếu định nghĩa hàm |
| Thông báo | `error: expected ';'` | `undefined reference to ...` |

Thấy `undefined reference` thì kiểm tra: (1) đã viết định nghĩa hàm chưa, (2) có quên thêm file `.c` vào lệnh biên dịch không, (3) tên hàm có gõ sai không, (4) có quên `-lm` khi dùng hàm của `<math.h>` không.

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

// BAT BUOC co nguyen mau - vi 2 ham goi LAN NHAU
bool laChan(int n);
bool laLe(int n);

bool laChan(int n) {
    if (n == 0) return true;
    return laLe(n - 1);          // goi ham dinh nghia BEN DUOI
}

bool laLe(int n) {
    if (n == 0) return false;
    return laChan(n - 1);        // goi ham dinh nghia BEN TREN
}

int main(void) {
    for (int i = 0; i <= 6; i++) {
        printf("%d: chan = %s, le = %s\n", i,
               laChan(i) ? "true" : "false",
               laLe(i)   ? "true" : "false");
    }
    return 0;
}
```

Output:

```
0: chan = true, le = false
1: chan = false, le = true
...
```

💡 `printf` không có đặc tả riêng cho `bool`; in `%d` sẽ ra `1`/`0`, muốn in chữ thì dùng toán tử `?:` như trên.

**Vì sao BẮT BUỘC phải có nguyên mẫu:** đây là **đệ quy tương hỗ (mutual recursion)** — `laChan` gọi `laLe`, `laLe` gọi `laChan`.

Dù bạn sắp xếp thế nào, cũng sẽ có một hàm gọi hàm được định nghĩa **phía dưới** nó. Không có nguyên mẫu thì không thể biên dịch hợp lệ:

```
Neu dat laChan truoc  -> no goi laLe (chua biet)  -> LOI
Neu dat laLe truoc    -> no goi laChan (chua biet) -> LOI
```

Đây là trường hợp mà nguyên mẫu không phải "tuỳ chọn cho đẹp" mà là **bắt buộc kỹ thuật**.

### Bài 7.

**File `hamso.h`:**

```c
#ifndef HAMSO_H
#define HAMSO_H

#include <stdbool.h>

bool laChan(int n);
bool laLe(int n);

#endif
```

**File `hamso.c`:**

```c
#include "hamso.h"

bool laChan(int n) {
    if (n == 0) return true;
    return laLe(n - 1);
}

bool laLe(int n) {
    if (n == 0) return false;
    return laChan(n - 1);
}
```

**File `main.c`:**

```c
#include <stdio.h>
#include "hamso.h"

int main(void) {
    for (int i = 0; i <= 6; i++) {
        printf("%d: chan = %s\n", i, laChan(i) ? "true" : "false");
    }
    return 0;
}
```

**Biên dịch — phải liệt kê TẤT CẢ file `.c`:**

```bash
gcc -std=c11 -Wall main.c hamso.c -o chuongtrinh
./chuongtrinh
```

Hoặc biên dịch từng bước:

```bash
gcc -c hamso.c -o hamso.o          # dich rieng
gcc -c main.c  -o main.o
gcc hamso.o main.o -o chuongtrinh  # lien ket
```

⚠️ **Quên file `.c` trong lệnh biên dịch** là nguyên nhân số 1 của lỗi `undefined reference` khi làm dự án nhiều file.

💡 `hamso.h` tự `#include <stdbool.h>` vì nó dùng kiểu `bool` — file header nên tự đủ, không bắt người dùng nhớ include trước.

**Lưu ý dấu ngoặc trong `#include`:**

| Cú pháp | Tìm ở đâu |
|---|---|
| `#include <stdio.h>` | Thư mục thư viện hệ thống |
| `#include "hamso.h"` | **Thư mục hiện tại trước**, rồi mới tới thư viện |

### Bài 8.

**Header guard** ngăn một file `.h` bị chèn vào nhiều lần trong cùng một đơn vị biên dịch.

```c
#ifndef HAMSO_H       // Neu chua dinh nghia HAMSO_H thi...
#define HAMSO_H       // ...dinh nghia no ngay (danh dau "da doc file nay")

bool laChan(int n);
bool laLe(int n);

#endif                // ket thuc khoi dieu kien
```

**Vấn đề nếu không có guard:**

```c
// file a.h
#include "hamso.h"

// file main.c
#include "hamso.h"
#include "a.h"            // a.h lai include hamso.h -> hamso.h duoc doc 2 LAN
```

Với chỉ là nguyên mẫu hàm thì khai báo lại 2 lần vẫn hợp lệ. Nhưng nếu file `.h` chứa định nghĩa `struct` thì sẽ lỗi:

```
error: redefinition of 'struct SinhVien'
```

**Cách hoạt động:**

```
Lan doc thu 1: HAMSO_H chua duoc dinh nghia -> vao trong, dinh nghia HAMSO_H, doc noi dung
Lan doc thu 2: HAMSO_H DA duoc dinh nghia   -> bo qua toan bo toi #endif
```

**Cách viết ngắn hơn — `#pragma once`:**

```c
#pragma once

bool laChan(int n);
bool laLe(int n);
```

Ngắn gọn hơn và không cần nghĩ tên macro. Nó không nằm trong chuẩn C nhưng **mọi compiler phổ biến đều hỗ trợ** (GCC, Clang, MSVC).

💡 **Quy tắc đặt tên macro guard:** viết hoa tên file, thay `.` bằng `_`, thêm hậu tố nếu cần: `HAMSO_H`, `MYPROJECT_UTILS_MATH_H`.

### Bài 9.

| Tiêu chí | Nguyên mẫu (Declaration) | Định nghĩa (Definition) |
|---|---|---|
| **Có thân hàm `{ }`** | ❌ Không | ✅ Có |
| **Kết thúc bằng** | Dấu `;` | Dấu `}` |
| **Số lần được phép** | **Nhiều lần** (miễn giống nhau) | **Đúng một lần** trong toàn chương trình |
| **Tên tham số** | Tuỳ chọn | Bắt buộc (trước C23) |
| **Đặt ở đâu** | Đầu file, hoặc file `.h` | File `.c` |
| **Cấp phát bộ nhớ** | ❌ Không | ✅ Có (mã máy của hàm) |
| **Nhiệm vụ** | Báo cho compiler biết hàm tồn tại | Cung cấp mã thực thi cho linker |

```c
int tong(int a, int b);          // NGUYEN MAU
int tong(int, int);              // duoc khai bao lai, khong sao
int tong(int a, int b);          // lai lan nua, van khong sao

int tong(int a, int b) {         // DINH NGHIA - chi duoc 1 lan
    return a + b;
}
```

Định nghĩa cùng một hàm hai lần trong toàn chương trình sẽ bị lỗi: trong cùng một file là lỗi biên dịch `redefinition of 'tong'`, ở hai file `.c` khác nhau là lỗi liên kết `multiple definition of 'tong'`.

### Bài 10.

```c
#include <stdio.h>

void inBang(int n, char kyTu);          // nguyen mau: n, kyTu

int main(void) {
    inBang(3, '*');
    return 0;
}

void inBang(int soDong, char ky) {      // dinh nghia: soDong, ky - TEN KHAC
    for (int i = 0; i < soDong; i++) {
        for (int j = 0; j < soDong; j++) printf("%c", ky);
        printf("\n");
    }
}
```

**Chương trình CHẠY BÌNH THƯỜNG.** ✅

Output:

```
***
***
***
```

**Vì sao:** compiler chỉ so khớp **kiểu** tham số, không quan tâm tên. Tên tham số trong nguyên mẫu hoàn toàn mang tính tài liệu cho người đọc.

⚠️ Tuy chạy được, đây vẫn là **thói quen xấu** — người đọc nguyên mẫu thấy tên `kyTu` rồi đọc định nghĩa thấy `ky` sẽ bối rối. **Hãy đặt tên giống nhau.**

### Bài 11.

**File `mathlib.h`:**

```c
#ifndef MATHLIB_H
#define MATHLIB_H

#include <stdbool.h>

/**
 * @brief Tim uoc chung lon nhat cua 2 so nguyen.
 * @return UCLN (luon khong am). ucln(0,0) = 0.
 */
int ucln(int a, int b);

/**
 * @brief Tim boi chung nho nhat cua 2 so nguyen.
 * @return BCNN, hoac 0 neu mot trong hai so bang 0.
 */
long long bcnn(int a, int b);

/**
 * @brief Kiem tra mot so co phai so nguyen to.
 * @return true neu n la so nguyen to (n >= 2).
 */
bool laNguyenTo(int n);

/**
 * @brief Tinh giai thua n!
 * @return n! voi 0 <= n <= 20, tra ve -1 neu n am.
 */
long long giaiThua(int n);

#endif
```

**File `mathlib.c`:**

```c
#include "mathlib.h"
#include <stdlib.h>

int ucln(int a, int b) {
    a = abs(a);
    b = abs(b);
    while (b != 0) {
        int tam = a % b;
        a = b;
        b = tam;
    }
    return a;
}

long long bcnn(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return (long long)abs(a) / ucln(a, b) * abs(b);
}

bool laNguyenTo(int n) {
    if (n < 2) return false;
    if (n < 4) return true;              // 2 va 3
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

long long giaiThua(int n) {
    if (n < 0) return -1;
    long long kq = 1;
    for (int i = 2; i <= n; i++) kq *= i;
    return kq;
}
```

**File `main.c`:**

```c
#include <stdio.h>
#include "mathlib.h"

int main(void) {
    printf("ucln(48, 18)   = %d\n",   ucln(48, 18));                         // 6
    printf("bcnn(4, 6)     = %lld\n", bcnn(4, 6));                           // 12
    printf("laNguyenTo(97) = %s\n",   laNguyenTo(97) ? "true" : "false");    // true
    printf("giaiThua(10)   = %lld\n", giaiThua(10));                         // 3628800
    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall main.c mathlib.c -o chuongtrinh
```

💡 **Đây chính là cách mọi thư viện C được tổ chức:** file `.h` là **giao diện** (những gì người dùng cần biết), file `.c` là **cài đặt** (cách làm, người dùng không cần quan tâm).

### Bài 12.

Khi bạn viết `#include <stdio.h>`, **preprocessor chép toàn bộ nội dung file `stdio.h`** vào vị trí đó, trước khi biên dịch.

File `stdio.h` chứa (đơn giản hoá) các **nguyên mẫu** như:

```c
int printf(const char *format, ...);
int scanf(const char *format, ...);
int puts(const char *s);
int getchar(void);
...
```

Nói cách khác, **`#include` chính là cách C cung cấp "nguyên mẫu" cho toàn bộ thư viện chuẩn.** Dấu `...` nghĩa là hàm nhận **số lượng đối số thay đổi** — đó là lý do `printf` nhận được bao nhiêu đối số cũng được.

Xem thử điều này thật sự xảy ra:

```bash
echo '#include <stdio.h>' > test.c
gcc -E test.c | grep -w printf
# Ket qua: dong  extern int printf (const char *__restrict __format, ...);
gcc -E test.c | wc -l
# Vai tram dong (tuy he thong)
```

**Phần định nghĩa (mã thực thi) ở đâu:** nằm trong thư viện C chuẩn đã biên dịch sẵn (`libc`), được linker tự động ghép vào khi bạn dùng `gcc`. Đó là lý do bạn không phải làm gì thêm. Riêng các hàm toán học của `<math.h>` nằm ở thư viện `libm`, trên Linux thường phải thêm `-lm` khi biên dịch.

**Sơ đồ đầy đủ:**

```
#include <stdio.h>   ->  khai bao (nguyen mau) cua printf, scanf
      +
libc (co san)        ->  dinh nghia (ma may) cua printf, scanf
      =
Chuong trinh chay duoc
```

### Bài 13.

**Bước 1 — thử khai báo 2 nguyên mẫu cùng tên:**

```c
double dienTich(double canh);                  // hinh vuong
double dienTich(double dai, double rong);      // LOI
```

gcc báo:

```
error: conflicting types for 'dienTich'; have 'double(double,  double)'
note: previous declaration of 'dienTich' with type 'double(double)'
```

**C không có nạp chồng hàm (overload)**: mỗi tên hàm chỉ gắn với một kiểu hàm duy nhất.

**Bước 2 — sửa bằng cách đặt tên khác nhau:**

```c
#include <stdio.h>
#include <math.h>

// ===== 3 NGUYEN MAU, MOI HAM MOT TEN =====
double dienTichVuong(double canh);                        // hinh vuong
double dienTichChuNhat(double dai, double rong);          // hinh chu nhat
double dienTichTamGiac(double a, double b, double c);     // tam giac (Heron)

int main(void) {
    printf("Vuong canh 5   : %.4f\n", dienTichVuong(5.0));
    printf("Chu nhat 5x3   : %.4f\n", dienTichChuNhat(5.0, 3.0));
    printf("Tam giac 3,4,5 : %.4f\n", dienTichTamGiac(3.0, 4.0, 5.0));
    return 0;
}

// ===== DINH NGHIA =====
double dienTichVuong(double canh) {
    return canh * canh;
}

double dienTichChuNhat(double dai, double rong) {
    return dai * rong;
}

double dienTichTamGiac(double a, double b, double c) {
    double p = (a + b + c) / 2;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}
```

Biên dịch: `gcc -std=c11 -Wall main.c -o main -lm` (cần `-lm` vì dùng `sqrt`).

### Bài 14.

```c
#include <stdio.h>

int f(int);                    // nguyen mau: nhan int

int main(void) {
    printf("%d\n", f(5));
    return 0;
}

int f(long x) { return x * 2; }   // dinh nghia: nhan long
```

**Kết quả: lỗi BIÊN DỊCH.**

```
error: conflicting types for 'f'; have 'int(long int)'
note: previous declaration of 'f' with type 'int(int)'
```

**Giải thích:** trong C, tên `f` chỉ được phép ứng với **một** kiểu hàm. Nguyên mẫu nói `f` nhận `int`, định nghĩa lại nói `f` nhận `long` → hai khai báo mâu thuẫn nhau, compiler phát hiện ngay vì cả hai nằm trong cùng một file.

⚠️ **Trường hợp nguy hiểm hơn:** nếu nguyên mẫu `int f(int);` nằm trong `main.c`, còn định nghĩa `int f(long x)` nằm ở file khác `f.c`, thì mỗi file được biên dịch riêng nên compiler **không thấy** mâu thuẫn. Linker chỉ so khớp **tên** `f` (C không mã hoá kiểu tham số vào tên hàm), nên chương trình vẫn liên kết thành công — nhưng lời gọi truyền `int` trong khi hàm đọc `long`: đây là **undefined behavior**, kết quả có thể đúng "do may mắn" hoặc sai tuỳ máy.

**Sửa:** cho nguyên mẫu và định nghĩa **khớp hoàn toàn**:

```c
int f(int);
...
int f(int x) { return x * 2; }
```

💡 Đây là lý do thực tế người ta luôn đặt nguyên mẫu trong file `.h` và **`#include` chính file `.h` đó vào file `.c` định nghĩa** — nếu lệch nhau, compiler sẽ báo lỗi ngay thay vì để lỗi âm thầm lúc chạy.

### Bài 15.

```c
/*
 * ============================================================
 *  Ten file  : quanly_sach.c
 *  Tac gia   : Nguyen Van A
 *  Ngay      : 17/09/2026
 *  Mo ta     : Chuong trinh quan ly danh sach sach don gian:
 *              nhap, hien thi, tim kiem, sap xep, thong ke.
 *  Bien dich : gcc -std=c11 -Wall quanly_sach.c -o quanly
 * ============================================================
 */

// ==================== THU VIEN ====================
#include <stdio.h>
#include <string.h>

// ==================== HANG SO ====================
#define MAX_SACH 100
#define MAX_TEN  50

// ==================== NGUYEN MAU HAM ====================
void      hienMenu(void);
int       nhapSach(char ten[][MAX_TEN], char tacGia[][MAX_TEN],
                   long long gia[], int soLuong);
void      hienThiTatCa(char ten[][MAX_TEN], char tacGia[][MAX_TEN],
                       const long long gia[], int n);
int       timTheoTen(char ten[][MAX_TEN], int n, const char canTim[]);
void      sapXepTheoGia(char ten[][MAX_TEN], char tacGia[][MAX_TEN],
                        long long gia[], int n);
long long tongGiaTri(const long long gia[], int n);
double    giaTrungBinh(const long long gia[], int n);

// ==================== CHUONG TRINH CHINH ====================
int main(void) {
    char      ten[MAX_SACH][MAX_TEN];
    char      tacGia[MAX_SACH][MAX_TEN];
    long long gia[MAX_SACH];
    int n = 0;
    int chon;

    do {
        hienMenu();
        if (scanf("%d", &chon) != 1) break;      // nhap sai / het du lieu -> thoat

        switch (chon) {
            case 1: {
                int them;
                printf("So sach muon them: ");
                scanf("%d", &them);
                n = nhapSach(ten, tacGia, gia, them);
                break;
            }
            case 2:
                hienThiTatCa(ten, tacGia, gia, n);
                break;
            case 3: {
                char canTim[MAX_TEN];
                printf("Nhap ten sach can tim (viet lien): ");
                scanf("%49s", canTim);
                int vt = timTheoTen(ten, n, canTim);
                if (vt == -1) printf(">> Khong tim thay!\n");
                else printf(">> Tim thay tai vi tri %d: %s - %lld VND\n",
                            vt + 1, ten[vt], gia[vt]);
                break;
            }
            case 4:
                sapXepTheoGia(ten, tacGia, gia, n);
                printf(">> Da sap xep theo gia tang dan.\n");
                hienThiTatCa(ten, tacGia, gia, n);
                break;
            case 5:
                printf(">> Tong so sach   : %d\n", n);
                printf(">> Tong gia tri   : %lld VND\n", tongGiaTri(gia, n));
                printf(">> Gia trung binh : %.0f VND\n", giaTrungBinh(gia, n));
                break;
            case 0:
                printf(">> Tam biet!\n");
                break;
            default:
                printf(">> Lua chon khong hop le!\n");
        }
    } while (chon != 0);

    return 0;
}

// ==================== DINH NGHIA HAM ====================

void hienMenu(void) {
    printf("\n========= QUAN LY SACH =========\n");
    printf("1. Nhap danh sach sach\n");
    printf("2. Hien thi tat ca\n");
    printf("3. Tim sach theo ten\n");
    printf("4. Sap xep theo gia\n");
    printf("5. Thong ke\n");
    printf("0. Thoat\n");
    printf("================================\n");
    printf("Lua chon: ");
}

int nhapSach(char ten[][MAX_TEN], char tacGia[][MAX_TEN],
             long long gia[], int soLuong) {
    if (soLuong <= 0 || soLuong > MAX_SACH) {
        printf("So luong khong hop le!\n");
        return 0;
    }
    for (int i = 0; i < soLuong; i++) {
        printf("--- Sach %d ---\n", i + 1);
        printf("Ten (viet lien)    : "); scanf("%49s", ten[i]);
        printf("Tac gia (viet lien): "); scanf("%49s", tacGia[i]);
        printf("Gia (VND)          : "); scanf("%lld", &gia[i]);
    }
    return soLuong;
}

void hienThiTatCa(char ten[][MAX_TEN], char tacGia[][MAX_TEN],
                  const long long gia[], int n) {
    if (n == 0) { printf(">> Danh sach trong!\n"); return; }

    printf("\n+-----+--------------------+--------------------+--------------+\n");
    printf("| STT | TEN SACH           | TAC GIA            |     GIA (VND)|\n");
    printf("+-----+--------------------+--------------------+--------------+\n");
    for (int i = 0; i < n; i++) {
        printf("| %-3d | %-18s | %-18s | %12lld |\n",
               i + 1, ten[i], tacGia[i], gia[i]);
    }
    printf("+-----+--------------------+--------------------+--------------+\n");
}

int timTheoTen(char ten[][MAX_TEN], int n, const char canTim[]) {
    for (int i = 0; i < n; i++) {
        if (strcmp(ten[i], canTim) == 0) return i;
    }
    return -1;                       // quy uoc: -1 = khong tim thay
}

void sapXepTheoGia(char ten[][MAX_TEN], char tacGia[][MAX_TEN],
                   long long gia[], int n) {
    // Sap xep noi bot - khi doi cho gia, phai doi cho CA ten va tacGia
    char tamChuoi[MAX_TEN];
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (gia[j] > gia[j + 1]) {
                long long tamGia = gia[j];
                gia[j] = gia[j + 1];
                gia[j + 1] = tamGia;

                strcpy(tamChuoi, ten[j]);
                strcpy(ten[j], ten[j + 1]);
                strcpy(ten[j + 1], tamChuoi);

                strcpy(tamChuoi, tacGia[j]);
                strcpy(tacGia[j], tacGia[j + 1]);
                strcpy(tacGia[j + 1], tamChuoi);
            }
        }
    }
}

long long tongGiaTri(const long long gia[], int n) {
    long long tong = 0;
    for (int i = 0; i < n; i++) tong += gia[i];
    return tong;
}

double giaTrungBinh(const long long gia[], int n) {
    if (n == 0) return 0;
    return (double)tongGiaTri(gia, n) / n;
}
```

**Các điểm đáng học trong chương trình này:**

1. **Cấu trúc file rõ ràng:** header comment → include → hằng số → nguyên mẫu → `main` → định nghĩa
2. **`const` cho tham số chỉ đọc:** `const long long gia[]` báo cho người đọc (và compiler) biết hàm không sửa mảng
3. **So sánh chuỗi bằng `strcmp`**, không dùng `==` — với mảng `char`, `==` chỉ so sánh **địa chỉ**, không so sánh nội dung
4. **Quy ước trả về `-1`** khi tìm không thấy — rất phổ biến trong C
5. **`sapXepTheoGia` đổi chỗ cả 3 mảng** — lỗi kinh điển là chỉ đổi mảng giá, làm dữ liệu bị lệch. Chuỗi không gán được bằng `=` nên phải đổi chỗ bằng `strcpy`

⚠️ **Vì sao tham số mảng 2 chiều `char ten[][MAX_TEN]` không có `const`?** Trong C (trước C23), truyền mảng 2 chiều thường vào tham số `const char ten[][MAX_TEN]` bị coi là khác kiểu con trỏ, muốn đúng chuẩn phải ép kiểu rất rườm rà. Với mảng 1 chiều như `gia[]` thì thêm `const` thoải mái.

⚠️ Chương trình này dùng **3 mảng song song** — đây là thiết kế dễ sai. Cách tốt hơn là dùng `struct`:

```c
struct Sach {
    char ten[MAX_TEN], tacGia[MAX_TEN];
    long long gia;
};
struct Sach ds[MAX_SACH];        // 1 mang, khong bao gio bi lech du lieu
```

Khi đó đổi chỗ 2 cuốn sách chỉ cần gán struct: `struct Sach tam = ds[j]; ds[j] = ds[j + 1]; ds[j + 1] = tam;`.
