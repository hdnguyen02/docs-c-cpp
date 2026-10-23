# Lời giải — [C]. Con Trỏ Cấp 2

[← Quay lại bài học](../07-02-c-con-tro-cap-2.md)

> **Con trỏ cấp 2 (`int **q`)** là con trỏ trỏ tới **một con trỏ khác**.
> Dùng khi cần **thay đổi chính con trỏ** (chứ không chỉ giá trị nó trỏ tới).

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;
    int **q = &p;

    printf("--- GIA TRI ---\n");
    printf("x   = %d\n", x);            // 42
    printf("*p  = %d\n", *p);           // 42
    printf("**q = %d\n", **q);          // 42

    printf("\n--- DIA CHI ---\n");
    printf("&x  = %p\n", (void *)&x);
    printf("p   = %p\n", (void *)p);    // = &x
    printf("*q  = %p\n", (void *)*q);   // = p = &x

    printf("&p  = %p\n", (void *)&p);
    printf("q   = %p\n", (void *)q);    // = &p

    printf("&q  = %p\n", (void *)&q);
    return 0;
}
```

**Sơ đồ bộ nhớ:**

```
Dia chi      Bien    Gia tri
0x1000        x       42
0x2000        p       0x1000  -----> x
0x3000        q       0x2000  -----> p -----> x
```

**Quy tắc:** mỗi dấu `*` đi thêm một bước theo mũi tên.

```
q    = 0x2000    (dia chi cua p)
*q   = 0x1000    (noi dung p = dia chi cua x)
**q  = 42        (noi dung x)
```

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int x = 10;
    int *p = &x;
    int **q = &p;

    printf("Truoc: x = %d\n", x);    // 10

    **q = 99;                         // sua x qua 2 cap con tro

    printf("Sau  : x = %d\n", x);    // 99
    return 0;
}
```

3 cách sau hoàn toàn tương đương: `x = 99`, `*p = 99`, `**q = 99`.

### Bài 3.

```c
#include <stdio.h>

void doiConTro(int **q, int *moi) {
    *q = moi;          // thay doi CHINH con tro ma q tro toi
}

int main(void) {
    int a = 10, b = 20;
    int *p = &a;

    printf("Truoc: *p = %d\n", *p);   // 10

    doiConTro(&p, &b);                 // truyen DIA CHI cua p

    printf("Sau  : *p = %d\n", *p);   // 20
    return 0;
}
```

💡 So sánh `*q = moi` với `**q = giaTri`:
- `*q = moi` → thay đổi **con trỏ** `p` (cho nó trỏ sang chỗ khác)
- `**q = giaTri` → thay đổi **giá trị** mà `p` đang trỏ tới

### Bài 4.

```c
#include <stdio.h>

// SAI: nhan con tro CAP 1 - chi thay doi duoc BAN SAO cua con tro
void thuDoiSai(int *p, int *moi) {
    p = moi;                   // chi doi ban sao, khong anh huong ben ngoai
    (void)p;
}

// DUNG: nhan con tro CAP 2
void thuDoiDung(int **q, int *moi) {
    *q = moi;
}

int main(void) {
    int a = 10, b = 20;
    int *p = &a;

    thuDoiSai(p, &b);
    printf("Sau thuDoiSai : *p = %d\n", *p);    // van 10

    thuDoiDung(&p, &b);
    printf("Sau thuDoiDung: *p = %d\n", *p);    // 20
    return 0;
}
```

**Giải thích — đây chính là quy tắc tham trị áp dụng cho con trỏ:**

```
thuDoiSai(p, &b):
   main:  p [0x1000]  ---> a
                |  sao chep
   ham:   p [0x1000]  ---> a
          p = moi  ->  ham: p [0x2000] ---> b
          Nhung main: p VAN LA [0x1000]

thuDoiDung(&p, &b):
   main:  p [0x1000]
              ^
   ham:   q --'  (q tro thang vao o nho cua p)
          *q = moi  ->  ghi thang vao o nho cua p
          main: p [0x2000] ---> b   ✔
```

**Nguyên tắc tổng quát:** trong C mọi tham số đều truyền theo **tham trị**, nên muốn hàm thay đổi được thứ gì, phải truyền **địa chỉ** của thứ đó.
- Thay đổi `int` → truyền `int*`
- Thay đổi `int*` → truyền `int**`
- Thay đổi `int**` → truyền `int***`

💡 **Cách khác không cần `**`:** cho hàm **trả về** con trỏ mới rồi gán lại ở nơi gọi:

```c
int *chonConTro(int *moi) { return moi; }
p = chonConTro(&b);
```

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>

void capPhat(int **p, int n) {
    *p = malloc(n * sizeof(int));
    if (*p == NULL) return;                            // cap phat that bai
    for (int i = 0; i < n; i++) (*p)[i] = i * 10;     // chu y dau ngoac!
}

void giaiPhong(int **p) {
    free(*p);
    *p = NULL;                    // tranh dangling pointer
}

int main(void) {
    int *a = NULL;
    int n = 5;

    capPhat(&a, n);
    if (a == NULL) { printf("Khong du bo nho!\n"); return 1; }

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                 // 0 10 20 30 40

    giaiPhong(&a);
    printf("Sau giai phong, a = %s\n", a == NULL ? "NULL" : "co gia tri");
    return 0;
}
```

⚠️ **Chú ý dấu ngoặc: `(*p)[i]` chứ không phải `*p[i]`.**

```
(*p)[i]  ->  lay con tro ma p tro toi, roi truy cap phan tu i   ✔
*p[i]    ->  p[i] truoc (do uu tien [] cao hon *), roi giai tham chieu  ✘
```

💡 Cách viết khác — trả về con trỏ (chính là kiểu của `malloc`):

```c
int *capPhat2(int n) { return malloc(n * sizeof(int)); }
int *a = capPhat2(5);
```

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int a = 10, b = 20, c = 30;

    int *arr[3] = {&a, &b, &c};      // MANG cac con tro

    printf("Gia tri: ");
    for (int i = 0; i < 3; i++) printf("%d ", *arr[i]);
    printf("\n");                     // 10 20 30

    // Sua gia tri qua mang con tro
    *arr[1] = 999;
    printf("b sau khi sua = %d\n", b);    // 999

    // Ten mang chinh la con tro cap 2
    int **p = arr;
    printf("Qua con tro cap 2: ");
    for (int i = 0; i < 3; i++) printf("%d ", **(p + i));
    printf("\n");                     // 10 999 30

    return 0;
}
```

💡 **Điểm liên hệ quan trọng:** tên mảng `arr` (kiểu `int *[3]`) suy biến thành `int **` khi dùng như con trỏ. Đây là lý do `char **argv` ở bài 8 hoạt động được.

**Ứng dụng thực tế:** sắp xếp mà không di chuyển dữ liệu gốc — chỉ sắp xếp mảng con trỏ.

### Bài 7.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 3, m = 4;

    // (1) Cap phat mang con tro (n hang)
    int **a = malloc(n * sizeof(int *));
    if (a == NULL) return 1;

    // (2) Cap phat tung hang (moi hang m phan tu)
    for (int i = 0; i < n; i++) {
        a[i] = malloc(m * sizeof(int));
        if (a[i] == NULL) return 1;     // don gian hoa: bo qua giai phong khi loi
    }

    // (3) Su dung nhu mang 2 chieu binh thuong
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = i * m + j;

    printf("Ma tran %dx%d:\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%4d", a[i][j]);
        printf("\n");
    }

    // (4) GIAI PHONG - phai lam NGUOC THU TU cap phat
    for (int i = 0; i < n; i++) free(a[i]);    // giai phong tung hang truoc
    free(a);                                    // roi moi giai phong mang con tro
    a = NULL;

    return 0;
}
```

**Sơ đồ bộ nhớ:**

```
a ---> [ptr0][ptr1][ptr2]          (mang con tro, n phan tu)
         |     |     |
         v     v     v
       [0][1][2][3]                (hang 0, m phan tu)
       [4][5][6][7]                (hang 1)
       [8][9][10][11]              (hang 2)
```

⚠️ **Phải giải phóng đúng thứ tự ngược lại.** Nếu `free(a)` trước, bạn mất luôn địa chỉ các hàng → **rò rỉ bộ nhớ (memory leak)**.

💡 `sizeof(int *)` là kích thước **một con trỏ** (mỗi phần tử của mảng `a`), còn `sizeof(int)` là kích thước một số nguyên (mỗi phần tử của một hàng).

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    printf("So tham so (argc) = %d\n", argc);

    for (int i = 0; i < argc; i++) {
        printf("argv[%d] = %s\n", i, argv[i]);
    }

    // Tinh tong cac tham so so
    if (argc > 1) {
        long long tong = 0;
        for (int i = 1; i < argc; i++) {
            tong += atoll(argv[i]);      // can <stdlib.h>
        }
        printf("Tong cac tham so = %lld\n", tong);
    }
    return 0;
}
```

Biên dịch và chạy:

```bash
gcc main.c -o chuongtrinh
./chuongtrinh 10 20 30
```

Output:

```
So tham so (argc) = 4
argv[0] = ./chuongtrinh
argv[1] = 10
argv[2] = 20
argv[3] = 30
Tong cac tham so = 60
```

**Giải thích:**
- `argc` (argument count) — số tham số, **luôn ≥ 1**
- `argv` (argument vector) — mảng các chuỗi
- `argv[0]` **thường là tên chương trình**
- `argv[argc]` luôn là `NULL`

`char **argv` chính là "con trỏ tới mảng các chuỗi". Có thể viết tương đương `char *argv[]`.

💡 Nhờ `argv[argc] == NULL`, có thể duyệt mà không cần `argc`:

```c
for (char **p = argv; *p != NULL; p++) printf("%s\n", *p);
```

### Bài 9.

```c
int a = 1, b = 2;
int *p = &a;
int **q = &p;
*q = &b;
printf("%d %d %d %d", *p, **q, a, b);
```

**Output:**

```
2 2 1 2
```

**Giải thích từng bước:**

```
Ban dau:
   a = 1, b = 2
   p ---> a
   q ---> p ---> a

Sau *q = &b:
   *q chinh la p, nen lenh nay = "p = &b"
   p ---> b
   q ---> p ---> b
   (a VAN BANG 1, khong bi dung toi)
```

| Biểu thức | Giá trị | Vì sao |
|---|---|---|
| `*p` | **2** | `p` giờ trỏ tới `b` = 2 |
| `**q` | **2** | `*q` = `p` → `**q` = `*p` = 2 |
| `a` | **1** | Không hề bị thay đổi |
| `b` | **2** | Không hề bị thay đổi |

⚠️ **Phân biệt rõ:**
- `*q = &b` → đổi **con trỏ** `p` sang trỏ vào `b`
- `**q = 5` → đổi **giá trị** mà `p` đang trỏ tới (tức `a = 5`)

### Bài 10.

```c
#include <stdio.h>

// Hoan doi 2 CON TRO (khong doi gia tri chung tro toi)
void hoanDoiConTro(int **p1, int **p2) {
    int *tam = *p1;
    *p1 = *p2;
    *p2 = tam;
}

int main(void) {
    int a = 10, b = 20;
    int *p = &a;
    int *q = &b;

    printf("Truoc: *p = %d, *q = %d\n", *p, *q);   // 10, 20
    printf("       a  = %d, b  = %d\n", a, b);     // 10, 20

    hoanDoiConTro(&p, &q);

    printf("Sau  : *p = %d, *q = %d\n", *p, *q);   // 20, 10
    printf("       a  = %d, b  = %d\n", a, b);     // 10, 20 (KHONG DOI)
    return 0;
}
```

**Điểm mấu chốt:** hoán đổi con trỏ chỉ làm chúng trỏ sang chỗ khác — **giá trị `a` và `b` không hề thay đổi**.

Đối chiếu với hoán đổi giá trị:

```c
void hoanDoiGiaTri(int *p1, int *p2) {
    int tam = *p1;
    *p1 = *p2;
    *p2 = tam;
}
// Sau khi goi: a = 20, b = 10; con p va q van tro cho cu
```

💡 C không có hàm `swap` dùng chung cho mọi kiểu, nên mỗi kiểu cần tự viết một hàm hoán đổi riêng (`int`, `int *`, ...).

### Bài 11.

```c
#include <stdio.h>

int main(void) {
    int x = 42;
    int *p = &x;
    int **q = &p;
    int ***r = &q;

    printf("x     = %d\n", x);       // 42
    printf("*p    = %d\n", *p);      // 42
    printf("**q   = %d\n", **q);     // 42
    printf("***r  = %d\n", ***r);    // 42

    ***r = 100;                       // sua x qua 3 cap
    printf("x sau khi sua = %d\n", x);   // 100
    return 0;
}
```

**Sơ đồ bộ nhớ:**

```
Dia chi      Bien    Gia tri              Y nghia
0x1000        x       42                  gia tri thuc
0x2000        p       0x1000    --------> x
0x3000        q       0x2000    --------> p --------> x
0x4000        r       0x3000    --------> q --------> p --------> x
```

**Bảng giải tham chiếu:**

| Biểu thức | Giá trị | Kiểu |
|---|---|---|
| `r` | 0x3000 | `int***` |
| `*r` | 0x2000 | `int**` (= `q`) |
| `**r` | 0x1000 | `int*` (= `p`) |
| `***r` | 42 | `int` (= `x`) |

⚠️ Trong thực tế **rất hiếm khi** cần con trỏ cấp 3. Nếu code của bạn có nhiều `int***`, hãy cân nhắc gom dữ liệu vào một `struct` cho dễ đọc.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>

int **capPhatMaTran(int n, int m) {
    int **a = malloc(n * sizeof(int *));
    if (a == NULL) return NULL;
    for (int i = 0; i < n; i++) {
        a[i] = calloc(m, sizeof(int));        // calloc -> khoi tao 0
        if (a[i] == NULL) {                   // loi: giai phong phan da cap
            for (int k = 0; k < i; k++) free(a[k]);
            free(a);
            return NULL;
        }
    }
    return a;
}

void giaiPhongMaTran(int ***a, int n) {
    if (a == NULL || *a == NULL) return;

    for (int i = 0; i < n; i++) {
        free((*a)[i]);           // giai phong tung hang
        (*a)[i] = NULL;
    }
    free(*a);                    // giai phong mang con tro
    *a = NULL;                   // dat con tro goc ve NULL
}

int main(void) {
    int n = 3, m = 4;
    int **mt = capPhatMaTran(n, m);
    if (mt == NULL) return 1;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mt[i][j] = i * m + j;

    printf("Ma tran:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%d\t", mt[i][j]);
        printf("\n");
    }

    giaiPhongMaTran(&mt, n);

    printf("Sau giai phong: mt = %s\n",
           mt == NULL ? "NULL (an toan)" : "con gia tri (nguy hiem)");
    return 0;
}
```

💡 **Vì sao cần con trỏ cấp 3 (`int ***a`) ở đây:** để hàm có thể đặt con trỏ `mt` ở `main` về `NULL`. Nếu chỉ nhận `int **a`, hàm chỉ sửa được bản sao.

💡 **Cách đơn giản hơn:** hàm nhận `int **a` để giải phóng, rồi người gọi tự gán `mt = NULL;` ngay sau lời gọi.

### Bài 13.

```c
#include <stdio.h>

int main(void) {
    // (1) int **p : con tro toi con tro
    int x = 1;
    int *tam = &x;
    int **p = &tam;
    printf("**p = %d\n", **p);

    // (2) int *q[3] : MANG 3 con tro
    int a = 10, b = 20, c = 30;
    int *q[3] = {&a, &b, &c};
    printf("*q[1] = %d\n", *q[1]);                    // 20
    printf("sizeof(q) = %zu byte\n", sizeof(q));      // 3 * 8 = 24

    // (3) int (*r)[3] : CON TRO toi mang 3 phan tu
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int (*r)[3] = m;                                  // r tro toi hang dau
    printf("r[1][2] = %d\n", r[1][2]);                // 6
    printf("sizeof(*r) = %zu byte\n", sizeof(*r));    // 3 * 4 = 12

    return 0;
}
```

**Bảng phân biệt:**

| Khai báo | Là gì | Kích thước | Dùng cho |
|---|---|---|---|
| `int **p` | Con trỏ tới con trỏ | 8 byte | Mảng 2D động, `argv` |
| `int *q[3]` | **Mảng** 3 con trỏ | 24 byte (3×8) | Mảng chuỗi, mảng con trỏ hàm |
| `int (*r)[3]` | Con trỏ tới **mảng** 3 phần tử | 8 byte | Truyền mảng 2D tĩnh vào hàm |

💡 **Mẹo đọc — bắt đầu từ tên biến, đọc theo thứ tự ưu tiên toán tử:**

```
int *q[3]
    ^ q la...  [3] mang 3 phan tu...  * cua con tro...  int toi int
    -> "q la mang 3 con tro toi int"

int (*r)[3]
    ^ (*r) -> r la con tro...  [3] toi mang 3 phan tu...  int kieu int
    -> "r la con tro toi mang 3 int"
```

`[]` có độ ưu tiên **cao hơn** `*`, nên phải dùng ngoặc `(*r)` để ép `r` là con trỏ trước.

💡 Dùng `typedef` để làm rõ:

```c
typedef int *MangConTro[3];      // rat kho doc neu viet truc tiep
typedef int (*ConTroMang)[3];
```

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

void themChuoi(char **ds, int *n, const char *s) {
    if (*n >= MAX) { printf("Danh sach day!\n"); return; }
    ds[*n] = malloc(strlen(s) + 1);           // +1 cho ky tu '\0'
    if (ds[*n] == NULL) { printf("Het bo nho!\n"); return; }
    strcpy(ds[*n], s);
    (*n)++;
}

void xoaChuoi(char **ds, int *n, int k) {
    if (k < 0 || k >= *n) { printf("Vi tri khong hop le!\n"); return; }
    free(ds[k]);                              // giai phong chuoi bi xoa
    for (int i = k; i < *n - 1; i++) ds[i] = ds[i + 1];
    (*n)--;
}

void inDanhSach(char **ds, int n) {
    if (n == 0) { printf("Danh sach rong\n"); return; }
    for (int i = 0; i < n; i++) printf("[%d] %s\n", i, ds[i]);
}

void giaiPhongTatCa(char **ds, int *n) {
    for (int i = 0; i < *n; i++) { free(ds[i]); ds[i] = NULL; }
    *n = 0;
}

int main(void) {
    char *ds[MAX];
    int n = 0;

    themChuoi(ds, &n, "C");
    themChuoi(ds, &n, "Python");
    themChuoi(ds, &n, "Java");
    themChuoi(ds, &n, "Go");

    printf("--- Danh sach ban dau ---\n");
    inDanhSach(ds, n);

    xoaChuoi(ds, &n, 1);
    printf("\n--- Sau khi xoa vi tri 1 ---\n");
    inDanhSach(ds, n);

    giaiPhongTatCa(ds, &n);
    printf("\nDa giai phong toan bo bo nho.\n");
    return 0;
}
```

Output:

```
--- Danh sach ban dau ---
[0] C
[1] Python
[2] Java
[3] Go

--- Sau khi xoa vi tri 1 ---
[0] C
[1] Java
[2] Go

Da giai phong toan bo bo nho.
```

⚠️ Mỗi `malloc` phải có đúng một `free` tương ứng. Chương trình trên rất dễ **rò rỉ bộ nhớ** nếu quên một chỗ.

💡 Số lượng `n` được truyền bằng **con trỏ `int *n`** để các hàm thêm/xoá cập nhật được biến `n` ở `main`.

### Bài 15.

**Các tình huống dùng con trỏ cấp 2 trong C:**

| Trường hợp dùng `**` | Có thể tránh bằng | Ưu / nhược |
|---|---|---|
| Hàm cần thay đổi một con trỏ | **Trả về** con trỏ mới: `p = f(...)` | ✅ Dễ đọc; ❌ chỉ trả về được 1 giá trị, không còn chỗ trả mã lỗi |
| Mảng 2 chiều động | **Mảng 1 chiều** cỡ `n*m`, truy cập `a[i*m + j]` | ✅ 1 lần `malloc`/`free`, dữ liệu liền nhau; ❌ phải tự tính chỉ số |
| Mảng 2 chiều động (C99) | **Con trỏ tới mảng**: `int (*a)[m] = malloc(n * sizeof *a);` | ✅ Viết được `a[i][j]`, 1 lần `free`; ❌ cần VLA |
| Mảng chuỗi (`char**`) | Mảng 2 chiều `char ds[100][50]` | ✅ Không cần cấp phát; ❌ phí bộ nhớ, giới hạn độ dài |
| Tham số dòng lệnh `char **argv` | ❌ Không tránh được | Do chuẩn C quy định chữ ký `main` |
| Hàm cấp phát trả mã lỗi | ❌ Thường vẫn dùng `**` | Kiểu `int taoMang(int **out, int n)` — trả mã lỗi, kết quả qua `*out` |

**Đối chiếu cụ thể:**

```c
// ========== Dùng con trỏ cấp 2 ==========
void capPhat(int **p, int n) {
    *p = malloc(n * sizeof(int));
}
int *a;
capPhat(&a, 10);
free(a);

// ========== Trả về con trỏ ==========
int *capPhat2(int n) {
    return malloc(n * sizeof(int));
}
int *b = capPhat2(10);
free(b);
```

```c
// ========== Mảng 2D: int** (n + 1 lần malloc) ==========
int **m = malloc(n * sizeof(int *));
for (int i = 0; i < n; i++) m[i] = malloc(c * sizeof(int));
// ... su dung m[i][j] ...
for (int i = 0; i < n; i++) free(m[i]);
free(m);

// ========== Mảng 2D: 1 khối liền (1 lần malloc) ==========
int *k = malloc(n * c * sizeof(int));
// ... su dung k[i * c + j] ...
free(k);
```

**✅ Vẫn NÊN nắm vững con trỏ cấp 2 vì:**

1. **Đọc hiểu code C** — thư viện chuẩn và rất nhiều thư viện C dùng nó (`strtol(const char *s, char **endptr, int base)`...)
2. **Hiểu bản chất `argv`** trong hàm `main`
3. **Hiểu cơ chế bộ nhớ** — mảng con trỏ, mảng 2 chiều, danh sách liên kết (con trỏ tới con trỏ `next`)
4. **Phỏng vấn và bài thi** — vẫn là chủ đề được hỏi
5. **Lập trình nhúng / hệ thống** — nơi C được dùng nhiều nhất

⚠️ **Khi dùng thì cẩn thận vì:**
- Dễ rò rỉ bộ nhớ (quên `free`)
- Dễ tạo dangling pointer
- Khó đọc, khó bảo trì — nên đặt tên rõ ràng, dùng `typedef` khi kiểu phức tạp
