# Lời giải — [C]. Lý Thuyết Con Trỏ

[← Quay lại bài học](../07-01-c-ly-thuyet-con-tro.md)

> **Con trỏ** là biến lưu **địa chỉ** của một biến khác.
> - `&x` — lấy **địa chỉ** của `x`
> - `*p` — lấy **giá trị** tại địa chỉ `p` (giải tham chiếu)
> - In địa chỉ bằng `printf("%p", (void *)p)`

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;              // p luu DIA CHI cua x

    printf("Gia tri cua x        : %d\n", x);
    printf("Dia chi cua x (&x)   : %p\n", (void *)&x);
    printf("Gia tri cua p        : %p\n", (void *)p);    // = &x
    printf("Gia tri p tro toi(*p): %d\n", *p);           // = x
    printf("Dia chi cua p (&p)   : %p\n", (void *)&p);
    return 0;
}
```

Output (địa chỉ thay đổi mỗi lần chạy):

```
Gia tri cua x        : 42
Dia chi cua x (&x)   : 0x7ffd5c3a1b4c
Gia tri cua p        : 0x7ffd5c3a1b4c      <- giong &x
Gia tri p tro toi(*p): 42                  <- giong x
Dia chi cua p (&p)   : 0x7ffd5c3a1b50      <- p cung co dia chi rieng
```

**Sơ đồ bộ nhớ:**

```
Dia chi         Bien      Gia tri
0x...b4c        x         42
0x...b50        p         0x...b4c   ---> tro toi x
```

💡 `%p` yêu cầu đối số kiểu `void *`, nên ta ép `(void *)` trước khi in.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;

    printf("Truoc: x = %d\n", x);       // 10

    *p = 99;                             // sua x THONG QUA con tro

    printf("Sau  : x = %d\n", x);       // 99
    printf("      *p = %d\n", *p);      // 99
    return 0;
}
```

💡 `*p = 99` và `x = 99` hoàn toàn tương đương — vì `*p` chính là `x`.

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int    *pi = NULL;
    double *pd = NULL;
    char   *pc = NULL;
    bool   *pb = NULL;

    printf("sizeof(int*)    = %zu byte\n", sizeof(pi));
    printf("sizeof(double*) = %zu byte\n", sizeof(pd));
    printf("sizeof(char*)   = %zu byte\n", sizeof(pc));
    printf("sizeof(bool*)   = %zu byte\n", sizeof(pb));

    printf("\nDe so sanh:\n");
    printf("sizeof(int)     = %zu byte\n", sizeof(int));
    printf("sizeof(double)  = %zu byte\n", sizeof(double));
    printf("sizeof(char)    = %zu byte\n", sizeof(char));
    return 0;
}
```

Output (máy 64-bit):

```
sizeof(int*)    = 8 byte
sizeof(double*) = 8 byte
sizeof(char*)   = 8 byte
sizeof(bool*)   = 8 byte
```

**Nhận xét: mọi con trỏ đều có CÙNG kích thước**, bất kể kiểu nó trỏ tới.

**Vì sao:** con trỏ chỉ lưu một **địa chỉ bộ nhớ** — và địa chỉ luôn có cùng độ dài trên một kiến trúc:
- Máy 64-bit → 8 byte (2⁶⁴ địa chỉ)
- Máy 32-bit → 4 byte (2³² địa chỉ ≈ 4 GB — đây là lý do Windows 32-bit không dùng được quá 4 GB RAM)

💡 `sizeof` trả về kiểu `size_t`, in bằng `%zu`.

**Vậy kiểu của con trỏ để làm gì?** Để compiler biết:
1. Khi giải tham chiếu `*p` thì đọc **bao nhiêu byte**
2. Khi làm số học `p + 1` thì nhảy **bao nhiêu byte**

```c
int *pi;     pi + 1  -> nhay 4 byte
double *pd;  pd + 1  -> nhay 8 byte
char *pc;    pc + 1  -> nhay 1 byte
```

### Bài 4.

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

    hoanDoi(&x, &y);                // truyen DIA CHI

    printf("Sau  : x = %d, y = %d\n", x, y);
    return 0;
}
```

So sánh 2 cách hoán đổi:

```c
void hoanDoi1(int a, int b)   { int t=a; a=b; b=t; }        // THAM TRI - khong hoat dong
void hoanDoi2(int *a, int *b) { int t=*a; *a=*b; *b=t; }    // CON TRO - goi: hoanDoi2(&x, &y)
```

Chỉ cách 2 đúng. C **không có tham chiếu** (khai báo `int &a` trong tham số là lỗi cú pháp), nên truyền **con trỏ** là cách duy nhất để hàm sửa được biến của hàm gọi.

### Bài 5.

```c
#include <stdio.h>

void tangGiaTri(int *p, int k) {
    if (p == NULL) return;        // LUON kiem tra con tro rong
    *p += k;
}

int main(void) {
    int x = 10;
    tangGiaTri(&x, 5);
    printf("x = %d\n", x);        // 15

    tangGiaTri(NULL, 5);          // an toan, khong crash
    printf("Khong crash\n");
    return 0;
}
```

✅ **Thói quen tốt: luôn kiểm tra `NULL` ở đầu hàm nhận con trỏ.**

### Bài 6.

```c
int *p;          // con tro CHUA duoc khoi tao -> chua dia chi RAC
*p = 10;         // ghi vao dia chi rac -> CRASH
printf("%d", *p);
```

**Lỗi:** con trỏ `p` chưa được gán địa chỉ nào, nên nó chứa **giá trị rác** — một địa chỉ ngẫu nhiên. Ghi vào đó là ghi vào vùng nhớ không thuộc chương trình.

Kết quả khi chạy:

```
Segmentation fault (core dumped)
```

**Sửa cách 1 — trỏ tới một biến có thật:**

```c
int x;
int *p = &x;
*p = 10;
printf("%d\n", *p);      // 10
```

**Sửa cách 2 — cấp phát bộ nhớ động (cần `<stdlib.h>`):**

```c
int *p = malloc(sizeof(int));
if (p != NULL) {
    *p = 10;
    printf("%d\n", *p);
    free(p);             // NHO giai phong
}
```

**Sửa cách 3 — khởi tạo `NULL` rồi kiểm tra:**

```c
int *p = NULL;
if (p != NULL) *p = 10;
else printf("Con tro rong!\n");
```

✅ **Quy tắc vàng: luôn khởi tạo con trỏ** — hoặc bằng địa chỉ thật, hoặc bằng `NULL`. Không bao giờ để nó "trống".

### Bài 7.

```c
#include <stdio.h>

void inGiaTri(int *p) {
    if (p == NULL) {
        printf("Con tro RONG, khong the truy cap!\n");
        return;
    }
    printf("Gia tri: %d\n", *p);
}

int main(void) {
    int x = 42;
    int *p1 = &x;
    int *p2 = NULL;

    inGiaTri(p1);         // Gia tri: 42
    inGiaTri(p2);         // Con tro RONG...

    // Cach viet ngan gon (con tro rong tuong duong false)
    if (p1) printf("p1 co gia tri\n");
    if (!p2) printf("p2 rong\n");

    return 0;
}
```

**`NULL`** là hằng con trỏ rỗng của C, được định nghĩa trong `<stdio.h>`, `<stdlib.h>`, `<string.h>`, `<stddef.h>`... Nó thường được định nghĩa là `((void *)0)` hoặc `0`.

💡 Con trỏ rỗng **không trỏ tới đối tượng nào**. Giải tham chiếu `*p` khi `p == NULL` là lỗi (thường là *Segmentation fault*), vì vậy luôn kiểm tra trước khi dùng. Các hàm thư viện như `malloc`, `fopen`, `strchr` đều trả về `NULL` để báo "thất bại / không tìm thấy".

### Bài 8.

```c
#include <stdio.h>

int *timMax(int *a, int *b) {
    if (a == NULL) return b;
    if (b == NULL) return a;
    return (*a > *b) ? a : b;
}

int main(void) {
    int x = 10, y = 20;

    int *p = timMax(&x, &y);
    printf("So lon hon = %d\n", *p);          // 20

    *p = 999;                                  // sua duoc qua con tro tra ve
    printf("x = %d, y = %d\n", x, y);         // x=10, y=999
    return 0;
}
```

⚠️ **An toàn vì:** hàm trả về con trỏ tới một trong hai **biến truyền địa chỉ vào** — chúng sống lâu hơn hàm.

⚠️ **KHÔNG BAO GIỜ** trả về con trỏ tới biến cục bộ:

```c
int *nguyHiem(void) {
    int x = 10;
    return &x;        // x bi huy khi ham ket thuc -> DANGLING POINTER
}
```

### Bài 9.

```c
#include <stdio.h>

int main(void) {
    int a = 10, b = 20;

    // (1) const int *p  -> KHONG sua duoc GIA TRI, sua duoc DIA CHI
    const int *p1 = &a;
    // *p1 = 99;          // LOI: assignment of read-only location
    p1 = &b;              // OK - doi sang tro vao b
    printf("p1 tro toi: %d\n", *p1);

    // (2) int * const p  -> sua duoc GIA TRI, KHONG doi duoc DIA CHI
    int * const p2 = &a;
    *p2 = 99;             // OK - sua gia tri cua a
    // p2 = &b;           // LOI: assignment of read-only variable 'p2'
    printf("a sau khi sua qua p2: %d\n", a);

    // (3) const int * const p -> KHONG sua duoc ca hai
    const int * const p3 = &b;
    // *p3 = 99;          // LOI
    // p3 = &a;           // LOI
    printf("p3 tro toi: %d\n", *p3);

    return 0;
}
```

**Bảng tổng hợp:**

| Khai báo | Sửa giá trị `*p`? | Đổi địa chỉ `p`? | Cách đọc |
|---|---|---|---|
| `int *p` | ✅ Có | ✅ Có | Con trỏ thường |
| `const int *p` | ❌ Không | ✅ Có | "Con trỏ tới **hằng** int" |
| `int * const p` | ✅ Có | ❌ Không | "**Hằng** con trỏ tới int" |
| `const int * const p` | ❌ Không | ❌ Không | Hằng con trỏ tới hằng int |

💡 **Mẹo đọc — đọc từ PHẢI sang TRÁI:**

```
const int  *  p      ->  p la con tro (*) toi int hang (const int)
int  * const  p      ->  p la con tro HANG (const *) toi int
```

Hoặc quy tắc đơn giản hơn: **`const` đứng trước `*` bảo vệ giá trị, `const` đứng sau `*` bảo vệ con trỏ.**

`const int *p` và `int const *p` là **giống hệt nhau**.

**Ứng dụng phổ biến nhất** — tham số hàm chỉ đọc (thư viện chuẩn dùng rất nhiều, ví dụ `size_t strlen(const char *s);`):

```c
void inMang(const int *a, int n);     // ham hua khong sua mang
```

### Bài 10.

```c
#include <stdio.h>

void inTheoKieu(void *p, char kieu) {
    switch (kieu) {
        case 'i': printf("int   : %d\n", *(int *)p);    break;
        case 'd': printf("double: %.2f\n", *(double *)p); break;
        case 'c': printf("char  : %c\n", *(char *)p);   break;
    }
}

int main(void) {
    int    a = 42;
    double b = 3.14;
    char   c = 'X';

    void *p;              // con tro "chung chung" - khong biet kieu

    p = &a;  inTheoKieu(p, 'i');
    p = &b;  inTheoKieu(p, 'd');
    p = &c;  inTheoKieu(p, 'c');

    // Khong the giai tham chieu truc tiep
    // printf("%d", *p);   // LOI: dereferencing 'void *' pointer

    return 0;
}
```

**`void *`** là con trỏ "vô kiểu" — nó lưu được địa chỉ của **bất kỳ** kiểu dữ liệu nào, nhưng compiler không biết đó là kiểu gì.

**Hạn chế:**
- Không giải tham chiếu trực tiếp (`*p` báo lỗi) — phải ép kiểu trước
- Không làm số học con trỏ theo chuẩn C (`p + 1` không biết nhảy bao nhiêu byte)

**Ứng dụng:** viết hàm tổng quát trong C, ví dụ `malloc` trả về `void *`, `qsort` và `memcpy` nhận `void *`.

💡 Trong C, `void *` **tự động chuyển** sang con trỏ kiểu khác khi gán, không cần ép:

```c
int *a = malloc(10 * sizeof(int));   // hop le trong C, khong can (int *)
```

### Bài 11.

```c
#include <stdio.h>

// Cach 1: truyen THAM TRI - ham nhan ban sao, tra ket qua qua return
int gapDoiThamTri(int x) {
    x *= 2;              // chi sua ban sao
    return x;
}

// Cach 2: truyen CON TRO - ham sua truc tiep bien goc
void gapDoiConTro(int *p) {
    if (p) *p *= 2;
}

int main(void) {
    int a = 5, b = 5;

    gapDoiThamTri(a);              // KHONG doi a (ket qua bi bo di)
    printf("a sau gapDoiThamTri(a)     = %d\n", a);   // 5
    a = gapDoiThamTri(a);          // phai gan lai
    printf("a = gapDoiThamTri(a)       = %d\n", a);   // 10

    gapDoiConTro(&b);              // phai co dau &
    printf("b sau gapDoiConTro(&b)     = %d\n", b);   // 10

    // Con tro co the RONG
    gapDoiConTro(NULL);            // an toan nho kiem tra
    return 0;
}
```

| | Tham trị `int x` | Con trỏ `int *p` |
|---|---|---|
| Cú pháp gọi hàm | `f(x)` | `f(&x)` |
| Trong hàm | `x` (bản sao) | `*p` (biến gốc) |
| Sửa được biến gốc | ❌ Không | ✅ Có |
| Trả về nhiều kết quả | ❌ Chỉ 1 qua `return` | ✅ Qua nhiều tham số con trỏ |
| Có thể rỗng | ❌ Không | ✅ Có (`NULL`) — phải kiểm tra |
| Chi phí khi truyền struct lớn | Sao chép toàn bộ | Chỉ sao chép 1 địa chỉ |

✅ **Trong C: dùng tham trị khi hàm chỉ cần đọc giá trị nhỏ; dùng con trỏ khi cần sửa biến gốc, trả về nhiều kết quả, hoặc truyền dữ liệu lớn** (khi đó thêm `const` nếu hàm không sửa). Đây chính là lý do `scanf("%d", &x)` cần dấu `&`.

### Bài 12.

```c
#include <stdio.h>

int binhPhuong(int x) { return x * x; }
int tangGapDoi(int x) { return x * 2; }
int doiDau(int x)     { return -x; }

// Ham nhan CON TRO HAM lam tham so
void apDung(int a[], int n, int (*f)(int)) {
    for (int i = 0; i < n; i++) {
        a[i] = f(a[i]);
    }
}

void inMang(const char *nhan, const int a[], int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[5] = {1, 2, 3, 4, 5};

    inMang("Ban dau     ", a, 5);

    apDung(a, 5, binhPhuong);
    inMang("Binh phuong ", a, 5);      // 1 4 9 16 25

    apDung(a, 5, tangGapDoi);
    inMang("Nhan doi    ", a, 5);      // 2 8 18 32 50

    apDung(a, 5, doiDau);
    inMang("Doi dau     ", a, 5);      // -2 -8 -18 -32 -50

    return 0;
}
```

**Cú pháp con trỏ hàm:** `kieu_tra_ve (*ten)(danh_sach_tham_so)`

```c
int (*f)(int);          // f la con tro toi ham nhan int, tra ve int
int *f(int);            // KHAC HAN: f la ham tra ve int*
```

💡 Dùng `typedef` cho dễ đọc:

```c
typedef int (*HamBienDoi)(int);
void apDung(int a[], int n, HamBienDoi f);
```

**Ứng dụng thực tế:** hàm so sánh cho `qsort`, callback, bảng phân phối lệnh (dispatch table).

### Bài 13.

```c
int x = 10;
int *p = &x;
int **q = &p;
printf("%d %d %d\n", x, *p, **q);
printf("%p %p %p\n", (void *)&x, (void *)p, (void *)*q);
```

**Output:**

```
10 10 10
0x7ffd... 0x7ffd... 0x7ffd...        (ba dia chi GIONG NHAU)
```

**Giải thích:**

```
Dia chi      Bien    Gia tri
0x1000        x       10
0x2000        p       0x1000    ---> tro toi x
0x3000        q       0x2000    ---> tro toi p
```

| Biểu thức | Kết quả | Giải thích |
|---|---|---|
| `x` | 10 | Giá trị của x |
| `*p` | 10 | Giá trị tại 0x1000 = x |
| `**q` | 10 | `*q` = 0x1000 (chính là p), rồi `*(0x1000)` = 10 |
| `&x` | 0x1000 | Địa chỉ của x |
| `p` | 0x1000 | Nội dung của p = địa chỉ x |
| `*q` | 0x1000 | Giá trị tại 0x2000 = nội dung p |
| `q` | 0x2000 | Địa chỉ của p |
| `&q` | 0x3000 | Địa chỉ của q |

💡 **Mẹo hiểu:** mỗi dấu `*` "đi thêm một bước" theo mũi tên. Xem thêm bài [07-02 — Con trỏ cấp 2](../07-02-c-con-tro-cap-2.md).

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>

int *taoConTroTreo(void) {
    int x = 42;
    int *p = &x;
    return p;               // x bi HUY khi ham ket thuc!
}

int main(void) {
    // --- TRUONG HOP 1: tro toi bien cuc bo da bi huy ---
    int *p1 = taoConTroTreo();
    // printf("%d", *p1);   // DANGLING POINTER - undefined behavior!
    (void)p1;

    // --- TRUONG HOP 2: dung con tro sau khi free ---
    int *p2 = malloc(sizeof(int));
    if (p2 == NULL) return 1;
    *p2 = 100;
    printf("Truoc free: %d\n", *p2);
    free(p2);
    // printf("%d", *p2);   // DANGLING POINTER - undefined behavior!

    p2 = NULL;              // <- PHONG TRANH: gan NULL ngay sau free
    if (p2) printf("%d\n", *p2);
    else printf("p2 da duoc giai phong an toan\n");

    // --- TRUONG HOP 3: tro vao vung nho cu sau khi realloc ---
    int *a = malloc(3 * sizeof(int));
    if (a == NULL) return 1;
    int *p3 = &a[0];
    int *tam = realloc(a, 1000 * sizeof(int));  // vung nho co the bi DOI CHO
    if (tam == NULL) { free(a); return 1; }
    a = tam;
    // printf("%d", *p3);   // NGUY HIEM: p3 van tro vao vung cu
    (void)p3;
    free(a);

    return 0;
}
```

**Dangling pointer (con trỏ treo)** là con trỏ trỏ tới vùng nhớ **đã bị giải phóng hoặc huỷ**.

**3 nguyên nhân chính:**

1. **Trả về địa chỉ biến cục bộ** — biến bị huỷ khi hàm kết thúc (gcc sẽ cảnh báo `function returns address of local variable` nếu bạn viết `return &x;` trực tiếp)
2. **Dùng con trỏ sau `free`** — vùng nhớ đã trả về hệ thống
3. **Vùng nhớ bị cấp phát lại** — `realloc` có thể chuyển dữ liệu sang vùng nhớ mới, mọi con trỏ cũ trỏ vào vùng cũ đều trở thành con trỏ treo

**Tính nguy hiểm:** chương trình thường **vẫn chạy** và có thể cho kết quả đúng trong lần thử đầu — vì vùng nhớ chưa bị ghi đè. Nhưng nó sẽ crash một cách ngẫu nhiên về sau, cực khó tìm nguyên nhân.

✅ **Cách phòng tránh:**

```c
// (1) Gan NULL ngay sau free
free(p);
p = NULL;

// (2) Khong tra ve con tro toi bien cuc bo
int taoSo(void) { int x = 42; return x; }     // tra ve GIA TRI

// (3) Neu can tra ve vung nho tu ham -> cap phat dong, nguoi goi free
int *taoMang(int n) { return malloc(n * sizeof(int)); }

// (4) Sau realloc, lay lai con tro tu con tro moi, khong dung con tro cu
```

💡 Phát hiện bằng công cụ:

```bash
gcc -fsanitize=address -g main.c -o main
./main
# AddressSanitizer: heap-use-after-free
```

### Bài 15.

| Toán tử | Tên | Ý nghĩa | Ví dụ |
|---|---|---|---|
| `&` | Lấy địa chỉ | Trả về địa chỉ của biến | `int *p = &x;` |
| `*` (khai báo) | Khai báo con trỏ | Báo đây là biến con trỏ | `int *p;` |
| `*` (dùng) | Giải tham chiếu | Lấy **giá trị** tại địa chỉ | `printf("%d", *p);` |
| `->` | Mũi tên | Truy cập thành viên struct qua con trỏ | `p->diem` (= `(*p).diem`) |
| `[]` | Chỉ số | Truy cập phần tử | `p[i]` (= `*(p + i)`) |
| `+`, `-` | Số học con trỏ | Dịch chuyển theo **số phần tử** | `p + 1` nhảy `sizeof(*p)` byte |
| `++`, `--` | Tăng/giảm | Chuyển sang phần tử kế/trước | `p++` |
| `==`, `!=`, `<` | So sánh | So sánh **địa chỉ** | `if (p == NULL)` |

**Chương trình minh hoạ đầy đủ:**

```c
#include <stdio.h>

struct SinhVien {
    char ten[50];
    int diem;
};

int main(void) {
    // (1) & va *
    int x = 42;
    int *p = &x;                    // & lay dia chi
    printf("*p = %d\n", *p);        // * lay gia tri

    // (2) -> voi struct
    struct SinhVien sv = {"An", 9};
    struct SinhVien *psv = &sv;
    printf("Ten: %s\n", psv->ten);        // cach ngan
    printf("Ten: %s\n", (*psv).ten);      // cach dai, tuong duong

    // (3) [] va so hoc con tro
    int a[5] = {10, 20, 30, 40, 50};
    int *pa = a;                     // ten mang = dia chi phan tu dau

    printf("pa[2]    = %d\n", pa[2]);        // 30
    printf("*(pa+2)  = %d\n", *(pa + 2));    // 30 - TUONG DUONG
    printf("a[2]     = %d\n", a[2]);         // 30

    // (4) ++ de duyet mang
    printf("Duyet bang con tro: ");
    for (int *q = a; q < a + 5; q++) {
        printf("%d ", *q);
    }
    printf("\n");

    // (5) Hieu 2 con tro = so phan tu giua chung (kieu ptrdiff_t, in bang %td)
    int *dau = &a[0], *cuoi = &a[4];
    printf("Khoang cach: %td phan tu\n", cuoi - dau);   // 4

    // (6) So sanh
    printf("p == &x? %d\n", p == &x);      // 1
    printf("p rong?  %d\n", p == NULL);    // 0

    return 0;
}
```

💡 **Điểm mấu chốt cần nhớ:** `a[i]` thực chất chỉ là cách viết tắt của `*(a + i)`. Đó là lý do mảng và con trỏ liên quan chặt chẽ với nhau — xem bài [07-03](../07-03-c-con-tro-va-mang-1-chieu.md).

Thú vị: vì `a[i] = *(a+i) = *(i+a) = i[a]`, nên `2[a]` cũng hợp lệ và bằng `a[2]`! (Tất nhiên đừng bao giờ viết như vậy.)
