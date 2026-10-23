# Lời giải — [C]. Truyền Tham Trị Và Truyền Con Trỏ

[← Quay lại bài học](../05-03-c-truyen-tham-tri-va-truyen-con-tro.md)

> **Tham trị (pass by value):** hàm nhận một **bản sao** → sửa không ảnh hưởng biến gốc.
> **Truyền con trỏ (pass by pointer):** hàm nhận **địa chỉ** của biến gốc (`&x`), dùng `*p` để đọc/ghi thẳng vào ô nhớ đó.

---

### Bài 1.

```c
#include <stdio.h>

void tangGapDoi(int x) {        // THAM TRI - nhan ban sao
    x = x * 2;
    printf("  Trong ham (tham tri)  : x = %d\n", x);
}

void tangGapDoi2(int *x) {      // CON TRO - nhan dia chi cua bien goc
    *x = *x * 2;
    printf("  Trong ham (con tro)   : *x = %d\n", *x);
}

int main(void) {
    int a = 5;
    printf("Truoc khi goi : a = %d\n", a);
    tangGapDoi(a);
    printf("Sau tham tri  : a = %d\n", a);

    printf("\n");
    int b = 5;
    printf("Truoc khi goi : b = %d\n", b);
    tangGapDoi2(&b);            // truyen DIA CHI cua b
    printf("Sau con tro   : b = %d\n", b);
    return 0;
}
```

Output:

```
Truoc khi goi : a = 5
  Trong ham (tham tri)  : x = 10
Sau tham tri  : a = 5          <- KHONG DOI

Truoc khi goi : b = 5
  Trong ham (con tro)   : *x = 10
Sau con tro   : b = 10         <- DA DOI
```

**Sơ đồ bộ nhớ:**

```
THAM TRI:
   main:  a [5]
             | sao chep GIA TRI
   ham:   x [5] -> [10]      (x la o nho KHAC, sua x khong anh huong a)

CON TRO:
   main:  b [5] -> [10]
             ^
             | x giu DIA CHI cua b
   ham:   x [&b]             (*x chinh la o nho cua b)
```

### Bài 2.

```c
#include <stdio.h>

void hoanDoi(int *a, int *b) {
    int tam = *a;
    *a = *b;
    *b = tam;
}

int main(void) {
    int x = 10, y = 20;
    printf("Truoc: x = %d, y = %d\n", x, y);
    hoanDoi(&x, &y);
    printf("Sau  : x = %d, y = %d\n", x, y);
    return 0;
}
```

Output:

```
Truoc: x = 10, y = 20
Sau  : x = 20, y = 10
```

💡 Biến `tam` là `int` (không phải `int *`) vì ta cần giữ tạm **giá trị** `*a`, không phải địa chỉ.

### Bài 3.

```c
#include <stdio.h>

void hoanDoiSai(int a, int b) {     // THAM TRI - khong hoat dong
    int tam = a;
    a = b;
    b = tam;
    printf("  Trong ham: a = %d, b = %d\n", a, b);
}

int main(void) {
    int x = 10, y = 20;
    printf("Truoc: x = %d, y = %d\n", x, y);
    hoanDoiSai(x, y);
    printf("Sau  : x = %d, y = %d\n", x, y);
    return 0;
}
```

Output:

```
Truoc: x = 10, y = 20
  Trong ham: a = 20, b = 10     <- hoan doi DUNG, nhung...
Sau  : x = 10, y = 20           <- ...x va y KHONG DOI
```

**Giải thích:** khi gọi `hoanDoiSai(x, y)`, C tạo **2 biến mới** `a` và `b`, sao chép giá trị của `x` và `y` vào. Hàm hoán đổi `a` với `b` — thành công, nhưng đó là 2 bản sao. Khi hàm kết thúc, `a` và `b` bị huỷ, `x` và `y` không hề bị đụng tới.

Đây là lý do **bắt buộc** phải truyền địa chỉ (con trỏ) khi hàm cần sửa đối số.

### Bài 4.

```c
#include <stdio.h>

void tinhTongHieu(int a, int b, int *tong, int *hieu) {
    *tong = a + b;
    *hieu = a - b;
}

int main(void) {
    int a = 15, b = 4;
    int tong, hieu;

    tinhTongHieu(a, b, &tong, &hieu);

    printf("Tong = %d\n", tong);    // 19
    printf("Hieu = %d\n", hieu);    // 11
    return 0;
}
```

**Đây là cách kinh điển để hàm "trả về nhiều giá trị"** trong C: `a`, `b` là **đầu vào** (tham trị), `tong`, `hieu` là **đầu ra** (con trỏ).

💡 Một cách khác là gói các kết quả vào `struct` rồi `return` cả struct:

```c
struct KetQua { int tong, hieu; };

struct KetQua tinhTongHieu2(int a, int b) {
    struct KetQua kq = { a + b, a - b };
    return kq;
}
```

Cách này rõ hơn khi nhìn vào **kiểu trả về**, nhưng cách dùng con trỏ phổ biến hơn trong thư viện C (vd `scanf`, `strtol`).

### Bài 5.

```c
#include <stdio.h>

void nhapMang(int a[], int *n) {
    printf("Nhap so phan tu: ");
    scanf("%d", n);             // n DA la dia chi -> KHONG them &

    for (int i = 0; i < *n; i++) {
        printf("  a[%d] = ", i);
        scanf("%d", &a[i]);
    }
}

int main(void) {
    int a[100];
    int n;

    nhapMang(a, &n);

    printf("Mang vua nhap (%d phan tu): ", n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

⚠️ **`n` BẮT BUỘC phải là con trỏ.** Nếu viết `void nhapMang(int a[], int n)` thì `n` trong `main` sẽ không được cập nhật — giá trị rác, và vòng lặp in ra sẽ sai hoặc crash.

⚠️ Trong hàm, `n` đã là địa chỉ nên viết `scanf("%d", n)`, **không** phải `scanf("%d", &n)` (đó là địa chỉ của chính con trỏ → sai). Còn trong vòng lặp phải dùng `*n` để lấy số phần tử.

💡 Mảng `a` **không cần** dấu `&` vì tên mảng khi truyền vào hàm vốn đã là địa chỉ phần tử đầu (xem bài 10).

### Bài 6.

```c
#include <stdio.h>

void timMinMax(int a[], int n, int *mn, int *mx) {
    if (n <= 0) return;

    *mn = *mx = a[0];                 // khoi tao bang phan tu DAU TIEN
    for (int i = 1; i < n; i++) {
        if (a[i] < *mn) *mn = a[i];
        if (a[i] > *mx) *mx = a[i];
    }
}

int main(void) {
    int a[] = {5, -3, 12, 0, 8, -7, 20};
    int n = 7;
    int mn, mx;

    timMinMax(a, n, &mn, &mx);

    printf("Nho nhat = %d\n", mn);   // -7
    printf("Lon nhat = %d\n", mx);   // 20
    return 0;
}
```

⚠️ **Khởi tạo bằng `a[0]`, không phải bằng 0.** Nếu khởi tạo `*mn = 0` thì với mảng toàn số dương, kết quả sẽ sai (ra 0).

💡 Duyệt **một lần** tìm cả min lẫn max, thay vì viết 2 hàm duyệt 2 lần.

### Bài 7.

**Output:**

```
1 11
```

**Giải thích:**

```c
void f(int x, int *y) { x += 10; *y += 10; }
//       ^tham tri  ^con tro

int a = 1, b = 1;
f(a, &b);
```

| Tham số | Kiểu truyền | Trong hàm | Sau khi hàm kết thúc |
|---|---|---|---|
| `x` ← `a` | Tham trị | `x` = 1 → 11 | `a` vẫn = **1** (bản sao bị huỷ) |
| `y` ← `&b` | Con trỏ | `*y` chính là `b`, 1 → 11 | `b` = **11** |

Bài này cho thấy một hàm có thể **kết hợp** cả tham trị lẫn con trỏ.

### Bài 8.

**Vì sao `scanf` cần `&`:** `scanf` phải **ghi** giá trị nhập vào biến `x` của bạn. Vì C chỉ truyền tham trị, nếu truyền `x` thì `scanf` chỉ nhận được bản sao (thậm chí là giá trị rác) — không ghi vào đâu được. Truyền `&x` thì `scanf` biết địa chỉ ô nhớ của `x` để ghi vào. Còn `printf` chỉ cần **đọc** giá trị để in nên truyền bản sao `x` là đủ.

```c
#include <stdio.h>

void nhapSoDuong(int *p) {
    do {
        printf("Nhap mot so duong: ");
        if (scanf("%d", p) != 1) {      // p da la dia chi, khong them &
            *p = 0;
            int c;
            while ((c = getchar()) != '\n' && c != EOF) {}   // bo dong nhap sai
            if (c == EOF) return;       // het du lieu -> dung
        }
    } while (*p <= 0);
}

int main(void) {
    int x = 0;
    nhapSoDuong(&x);
    printf("Ban da nhap: %d\n", x);
    return 0;
}
```

Ví dụ chạy:

```
Nhap mot so duong: -5
Nhap mot so duong: 0
Nhap mot so duong: 28
Ban da nhap: 28
```

💡 Hàm `nhapSoDuong` hoạt động **y hệt** `scanf`: nhận địa chỉ, ghi kết quả vào địa chỉ đó. `scanf` trả về số giá trị đọc thành công, nên kiểm tra `!= 1` để bắt trường hợp người dùng gõ chữ.

### Bài 9.

```c
#include <stdio.h>
#include <math.h>

int giaiPTBac2(double a, double b, double c, double *x1, double *x2) {
    double delta = b * b - 4 * a * c;
    if (delta < 0) return 0;                  // vo nghiem
    if (delta == 0) {                         // nghiem kep
        *x1 = *x2 = -b / (2 * a);
        return 1;
    }
    *x1 = (-b - sqrt(delta)) / (2 * a);
    *x2 = (-b + sqrt(delta)) / (2 * a);
    return 2;
}

int main(void) {
    double a, b, c, x1, x2;
    printf("Nhap a, b, c (a khac 0): ");
    scanf("%lf %lf %lf", &a, &b, &c);

    int soNghiem = giaiPTBac2(a, b, c, &x1, &x2);
    if (soNghiem == 0)      printf("Phuong trinh vo nghiem\n");
    else if (soNghiem == 1) printf("Nghiem kep x = %.2f\n", x1);
    else                    printf("x1 = %.2f, x2 = %.2f\n", x1, x2);
    return 0;
}
```

Biên dịch: `gcc -std=c11 -Wall main.c -o main -lm` (cần `-lm` vì dùng `sqrt`).

Ví dụ: nhập `1 -3 2` → `x1 = 1.00, x2 = 2.00`.

💡 Mẫu thiết kế rất phổ biến trong C: **giá trị `return`** cho biết trạng thái (ở đây là số nghiệm), **tham số con trỏ** chứa kết quả. Khi vô nghiệm, hàm không ghi gì vào `*x1`, `*x2` — `main` cũng không đọc chúng.

⚠️ Đọc `double` bằng `scanf` phải dùng `%lf`, không phải `%f`.

### Bài 10.

```c
#include <stdio.h>

void thuSuaMang(int a[], int n) {         // KHONG co dau &
    a[0] = 999;
    printf("  Trong ham: a[0] = %d\n", a[0]);
    printf("  sizeof(a) trong ham = %zu byte\n", sizeof(a));
    (void)n;
}

void thuSuaSo(int x) {                     // tham tri
    x = 999;
    (void)x;
}

int main(void) {
    int a[5] = {1, 2, 3, 4, 5};
    int x = 1;

    printf("sizeof(a) trong main = %zu byte\n", sizeof(a));

    thuSuaMang(a, 5);
    printf("Sau khi goi: a[0] = %d\n", a[0]);

    thuSuaSo(x);
    printf("Sau khi goi: x = %d\n", x);
    return 0;
}
```

Output (máy 64-bit):

```
sizeof(a) trong main = 20 byte
  Trong ham: a[0] = 999
  sizeof(a) trong ham = 8 byte
Sau khi goi: a[0] = 999          <- MANG BI SUA!
Sau khi goi: x = 1               <- SO KHONG BI SUA
```

**Kết luận: mảng không bị sao chép khi truyền vào hàm — hàm nhận địa chỉ phần tử đầu tiên**, dù bạn không viết dấu `&`.

**Bằng chứng:** `sizeof(a)` trong `main` là 20 (5 × 4 byte), nhưng trong hàm chỉ còn **8 byte** — kích thước của một con trỏ. Hiện tượng này gọi là **array decay** (mảng suy biến thành con trỏ). gcc còn cảnh báo điều này với `-Wall` (`-Wsizeof-array-argument`).

Ba cách viết sau **hoàn toàn tương đương**:

```c
void f(int a[5]);      // so 5 bi BO QUA hoan toan
void f(int a[]);
void f(int *a);        // day moi la ban chat that
```

⚠️ **Hệ quả quan trọng:**
1. Phải luôn truyền kèm kích thước `n` — trong hàm không tính được
2. Hàm có thể vô tình sửa mảng gốc. Muốn bảo vệ, dùng `const int a[]`

💡 `(void)n;` và `(void)x;` chỉ để báo compiler "biết là biến này không dùng tới", tránh cảnh báo `unused parameter` / `set but not used`.

### Bài 11.

```c
#include <stdio.h>

void tachGioPhutGiay(int tongGiay, int *gio, int *phut, int *giay) {
    *gio  = tongGiay / 3600;
    *phut = tongGiay % 3600 / 60;
    *giay = tongGiay % 60;
}

int main(void) {
    int t, h, m, s;
    printf("Nhap tong so giay: ");
    scanf("%d", &t);

    tachGioPhutGiay(t, &h, &m, &s);
    printf("%d giay = %d gio %d phut %d giay\n", t, h, m, s);
    printf("Dinh dang dong ho: %02d:%02d:%02d\n", h, m, s);
    return 0;
}
```

Ví dụ: nhập `3725` →

```
3725 giay = 1 gio 2 phut 5 giay
Dinh dang dong ho: 01:02:05
```

💡 `%02d` in số nguyên đủ 2 chữ số, thiếu thì thêm `0` ở trước.

### Bài 12.

```c
int *taoSo(void) {
    int x = 10;
    return &x;          // NGUY HIEM!
}
```

**Lỗi nghiêm trọng: trả về địa chỉ của biến cục bộ (dangling pointer — con trỏ treo).**

Biến `x` là biến **cục bộ**, nằm trên vùng nhớ ngăn xếp (stack) của hàm. Khi hàm kết thúc, vùng nhớ đó bị **thu hồi**. Con trỏ trả về đang trỏ tới một ô nhớ không còn thuộc về `x`.

```c
int main(void) {
    int *p = taoSo();
    printf("%d\n", *p);      // UNDEFINED BEHAVIOR: rac, 10 do "may man", hoac crash
    return 0;
}
```

⚠️ **Tính nguy hiểm đặc biệt:** với một số compiler, chương trình **vẫn chạy** và có thể in ra `10` — vì ô nhớ chưa bị ghi đè. Nhưng chỉ cần gọi thêm một hàm khác là giá trị thành rác. gcc hiện đại còn cố tình trả về `NULL` trong trường hợp này, nên `*p` làm chương trình **crash** ngay (Segmentation fault).

Compiler có cảnh báo (mặc định, không cần `-Wall`):

```
warning: function returns address of local variable [-Wreturn-local-addr]
```

**Các cách sửa:**

```c
// (1) Tra ve theo GIA TRI (dung nhat cho truong hop nay)
int taoSo(void) { int x = 10; return x; }

// (2) De noi goi cap cho mot bien, ham ghi vao qua con tro
void taoSo2(int *kq) { *kq = 10; }

// (3) Tra ve dia chi bien static (ton tai suot chuong trinh)
int *taoSo3(void) { static int x = 10; return &x; }
```

**Quy tắc an toàn:** chỉ trả về địa chỉ của thứ **sống lâu hơn** hàm — biến do nơi gọi truyền vào, biến `static`, biến toàn cục, hoặc bộ nhớ cấp phát động bằng `malloc` (sẽ học ở chương con trỏ). Biến `static` được giải thích ở bài [05-04](../05-04-c-pham-vi-bien-va-lop-luu-tru.md).

### Bài 13.

```c
#include <stdio.h>

void demChanLe(int a[], int n, int *chan, int *le) {
    *chan = *le = 0;                     // BAT BUOC khoi tao ve 0
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) (*chan)++;
        else               (*le)++;
    }
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5, 6, 7, -8, -9};
    int n = 9;
    int chan, le;

    demChanLe(a, n, &chan, &le);

    printf("So phan tu chan: %d\n", chan);   // 4  (2,4,6,-8)
    printf("So phan tu le  : %d\n", le);     // 5
    return 0;
}
```

⚠️ **Phải khởi tạo `*chan = *le = 0` bên trong hàm.** Biến `chan`, `le` ở `main` không được khởi tạo — nếu hàm chỉ tăng mà không đặt về 0 trước, kết quả sẽ cộng dồn lên giá trị rác.

⚠️ **Phải có ngoặc `(*chan)++`.** Viết `*chan++` sẽ bị hiểu là `*(chan++)` — tăng **con trỏ** sang ô nhớ kế tiếp chứ không tăng giá trị. Đây là lỗi rất hay gặp.

⚠️ Dùng `a[i] % 2 == 0` chứ **không** dùng `a[i] % 2 == 1` — vì `-9 % 2` trong C bằng `-1`, không phải `1` (xem bài [02-07](../02-07-c-toan-tu-operator.md) bài 4).

### Bài 14.

```c
void hoanDoi(int *a, int *b){
    int *tmp = a;       // LOI 1: doi cho 2 CON TRO, khong phai 2 GIA TRI
    a = b;
    b = tmp;
}
...
hoanDoi(x, y);          // LOI 2: truyen GIA TRI x, y thay vi DIA CHI
```

**Lỗi 1 — trong hàm quên dấu `*`:** `a = b` chỉ làm con trỏ cục bộ `a` trỏ sang chỗ khác. Hai con trỏ `a`, `b` là **bản sao** địa chỉ, đổi chỗ chúng không đụng gì tới `x`, `y`. Phải đổi chỗ **giá trị** tại địa chỉ: `*a`, `*b`.

**Lỗi 2 — khi gọi quên dấu `&`:** `hoanDoi(x, y)` truyền số `1` và `2` vào chỗ cần địa chỉ. gcc cảnh báo:

```
warning: passing argument 1 of 'hoanDoi' makes pointer from integer without a cast [-Wint-conversion]
```

(gcc 14 trở đi báo **lỗi**.) Nếu chương trình vẫn được chạy và hàm có dùng `*a` thì nó sẽ truy cập địa chỉ `1` → crash.

**Bản sửa:**

```c
#include <stdio.h>

void hoanDoi(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(void){
    int x = 1, y = 2;
    hoanDoi(&x, &y);
    printf("%d %d\n", x, y);    // 2 1
    return 0;
}
```

💡 **Mẹo kiểm tra:** tham số khai báo `int *a` thì khi gọi truyền `&bien`, trong thân hàm dùng `*a`. Thiếu một trong hai là sai.

### Bài 15.

```c
#include <stdio.h>

void hoanDoi(int *a, int *b) {
    int tam = *a;
    *a = *b;
    *b = tam;
}

void sapXep3(int *a, int *b, int *c) {
    if (*a > *b) hoanDoi(a, b);     // a, b DA la dia chi -> KHONG them &
    if (*a > *c) hoanDoi(a, c);     // sau 2 buoc nay *a nho nhat
    if (*b > *c) hoanDoi(b, c);     // *b <= *c
}

int main(void) {
    int x, y, z;
    printf("Nhap 3 so: ");
    scanf("%d %d %d", &x, &y, &z);

    sapXep3(&x, &y, &z);
    printf("Tang dan: %d %d %d\n", x, y, z);
    return 0;
}
```

Ví dụ: nhập `9 -2 5` → `Tang dan: -2 5 9`.

💡 **Điểm mấu chốt:** trong `sapXep3`, `a`, `b`, `c` **đã là con trỏ** tới `x`, `y`, `z`. Khi chuyển tiếp cho `hoanDoi` chỉ cần truyền nguyên `a`, `b` — nếu viết `hoanDoi(&a, &b)` là truyền địa chỉ của **chính biến con trỏ** (kiểu `int **`), sai kiểu và compiler sẽ cảnh báo.

**Tổng kết các dấu `&` và `*`:**

| Vị trí | Viết | Nghĩa |
|---|---|---|
| Khai báo tham số | `int *a` | `a` là con trỏ, sẽ nhận một địa chỉ |
| Lời gọi từ `main` | `hoanDoi(&x, &y)` | Truyền địa chỉ của biến thường |
| Lời gọi từ hàm có sẵn con trỏ | `hoanDoi(a, b)` | Chuyển tiếp địa chỉ, không thêm `&` |
| Trong thân hàm | `*a = ...` | Đọc/ghi giá trị tại địa chỉ `a` giữ |
