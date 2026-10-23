# Lời giải — [C]. Ma Trận Và Mảng 2 Chiều

[← Quay lại bài học](../08-03-c-ma-tran-va-mang-2-chieu.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[100][100] = {0};
    for (int i = 0; i < n; i++) a[i][i] = 1;

    printf("Ma tran don vi %dx%d:\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%4d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

Với `n = 4`:

```
   1   0   0   0
   0   1   0   0
   0   0   1   0
   0   0   0   1
```

💡 `int a[100][100] = {0};` đưa **toàn bộ** mảng về 0 — phần tử đầu được gán 0, các phần tử còn lại C tự điền 0.

### Bài 2.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[100][100] = {0};
    printf("Nhap %d gia tri tren duong cheo: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i][i]);

    printf("\nMa tran duong cheo:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

💡 **Ma trận đường chéo** có tính chất đặc biệt: nhân 2 ma trận đường chéo chỉ cần nhân từng cặp phần tử trên đường chéo — O(n) thay vì O(n³).

### Bài 3.

```c
#include <stdio.h>

int main() {
    int a[100][100], b[100][100], n, m;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    // Chuyen vi: b[j][i] = a[i][j]
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            b[j][i] = a[i][j];

    printf("\nMa tran goc (%dx%d):\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }

    printf("\nMa tran chuyen vi (%dx%d):\n", m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) printf("%5d", b[i][j]);
        printf("\n");
    }
    return 0;
}
```

Ví dụ:

```
Goc (2x3):        Chuyen vi (3x2):
1 2 3             1 4
4 5 6             2 5
                  3 6
```

⚠️ **Ma trận `n×m` chuyển vị thành `m×n`** — kích thước đổi chỗ.

### Bài 4.

```c
#include <stdio.h>

void swap(int *x, int *y) {
    int t = *x; *x = *y; *y = t;
}

int main() {
    int n;
    scanf("%d", &n);
    int a[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    // Chuyen vi TAI CHO: chi doi cho nua tren voi nua duoi
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)      // j bat dau tu i+1
            swap(&a[i][j], &a[j][i]);

    printf("\nSau khi chuyen vi tai cho:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

⚠️ **`j` PHẢI bắt đầu từ `i + 1`.** Nếu bắt đầu từ 0, mỗi cặp bị đổi chỗ **2 lần** → ma trận trở về như cũ.

```
j = i+1  ->  chi duyet NUA TREN duong cheo
             . X X
             . . X
             . . .
```

⚠️ Cách này **chỉ áp dụng cho ma trận VUÔNG**. Ma trận chữ nhật phải dùng ma trận phụ (bài 3).

💡 C không có `swap` sẵn, ta tự viết hàm nhận **2 con trỏ** và truyền địa chỉ `&a[i][j]`.

### Bài 5.

```c
#include <stdio.h>

void swap(int *x, int *y) {
    int t = *x; *x = *y; *y = t;
}

void inMT(const char *nhan, int a[][100], int n) {
    printf("%s\n", nhan);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    int n = 3;
    int a[100][100] = {{1,2,3},{4,5,6},{7,8,9}};

    inMT("Ban dau:", a, n);

    // XOAY 90 DO THEO CHIEU KIM DONG HO = CHUYEN VI + LAT NGANG
    // Buoc 1: chuyen vi
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            swap(&a[i][j], &a[j][i]);

    // Buoc 2: lat theo chieu ngang (dao nguoc tung hang)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n / 2; j++)
            swap(&a[i][j], &a[i][n - 1 - j]);

    inMT("Sau khi xoay 90 do (chieu kim dong ho):", a, n);
    return 0;
}
```

Output:

```
Ban dau:
    1    2    3
    4    5    6
    7    8    9

Sau khi xoay 90 do (chieu kim dong ho):
    7    4    1
    8    5    2
    9    6    3
```

**Công thức nhớ:**

```
Xoay 90 do CUNG chieu kim dong ho = Chuyen vi + Lat NGANG
Xoay 90 do NGUOC chieu kim dong ho = Chuyen vi + Lat DOC
```

💡 Cách trực tiếp (dùng ma trận phụ): `b[j][n-1-i] = a[i][j]`

### Bài 6.

```c
#include <stdio.h>

#define N 100

void swap(int *x, int *y) {
    int t = *x; *x = *y; *y = t;
}

void chuyenVi(int a[][N], int n) {
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) swap(&a[i][j], &a[j][i]);
}

void latNgang(int a[][N], int n) {         // dao nguoc tung HANG
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n / 2; j++) swap(&a[i][j], &a[i][n-1-j]);
}

void latDoc(int a[][N], int n) {           // dao nguoc tung COT
    for (int i = 0; i < n / 2; i++)
        for (int j = 0; j < n; j++) swap(&a[i][j], &a[n-1-i][j]);
}

void xoay90(int a[][N], int n)  { chuyenVi(a, n); latNgang(a, n); }
void xoay270(int a[][N], int n) { chuyenVi(a, n); latDoc(a, n); }
void xoay180(int a[][N], int n) { latNgang(a, n); latDoc(a, n); }

void inMT(const char *nhan, int a[][N], int n) {
    printf("%s\n", nhan);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    printf("\n");
}

// Chep ma tran goc vao a truoc moi phep xoay
void saoChep(int a[][N], int goc[][N], int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) a[i][j] = goc[i][j];
}

int main() {
    int n = 3;
    int goc[N][N] = {{1,2,3},{4,5,6},{7,8,9}};
    int a[N][N];

    saoChep(a, goc, n); inMT("Ban dau:", a, n);
    saoChep(a, goc, n); xoay90(a, n);  inMT("Xoay 90 do (kim dong ho):", a, n);
    saoChep(a, goc, n); xoay180(a, n); inMT("Xoay 180 do:", a, n);
    saoChep(a, goc, n); xoay270(a, n); inMT("Xoay 270 do (= 90 nguoc kim):", a, n);

    return 0;
}
```

**Bảng tổng hợp:**

| Phép xoay | Cách thực hiện | Công thức trực tiếp |
|---|---|---|
| 90° cùng kim | Chuyển vị + Lật ngang | `b[j][n-1-i] = a[i][j]` |
| 180° | Lật ngang + Lật dọc | `b[n-1-i][n-1-j] = a[i][j]` |
| 270° (= 90° ngược) | Chuyển vị + Lật dọc | `b[n-1-j][i] = a[i][j]` |

💡 Dùng `#define N 100` làm số cột cố định cho mọi hàm — khi truyền mảng 2 chiều vào hàm, C bắt buộc phải biết **số cột**.

### Bài 7.

```c
#include <stdio.h>

void swap(int *x, int *y) {
    int t = *x; *x = *y; *y = t;
}

void inMT(const char *nhan, int a[][100], int n, int m) {
    printf("%s\n", nhan);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    int n = 3, m = 4;
    int a[100][100] = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};

    inMT("Ban dau:", a, n, m);

    // LAT NGANG: dao nguoc tung hang (trai <-> phai)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m / 2; j++)
            swap(&a[i][j], &a[i][m - 1 - j]);
    inMT("Lat NGANG (guong trai-phai):", a, n, m);

    // LAT DOC: dao nguoc thu tu cac hang (tren <-> duoi)
    for (int i = 0; i < n / 2; i++)
        for (int j = 0; j < m; j++)
            swap(&a[i][j], &a[n - 1 - i][j]);
    inMT("Lat DOC (guong tren-duoi):", a, n, m);

    return 0;
}
```

Output:

```
Ban dau:
    1    2    3    4
    5    6    7    8
    9   10   11   12

Lat NGANG (guong trai-phai):
    4    3    2    1
    8    7    6    5
   12   11   10    9

Lat DOC (guong tren-duoi):
   12   11   10    9
    8    7    6    5
    4    3    2    1
```

⚠️ Chú ý điều kiện vòng lặp: lật ngang chạy `j < m/2`, lật dọc chạy `i < n/2` — chỉ một nửa để không đảo 2 lần.

### Bài 8.

```c
#include <stdio.h>

long long vet(int a[][100], int n) {
    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i][i];
    return tong;
}

int main() {
    int n;
    scanf("%d", &n);
    int a[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    printf("Vet (trace) = %lld\n", vet(a, n));
    return 0;
}
```

💡 **Vết (trace)** là một bất biến quan trọng trong đại số tuyến tính:
- `trace(A + B) = trace(A) + trace(B)`
- `trace(AB) = trace(BA)` (dù `AB ≠ BA`)
- Vết bằng **tổng các giá trị riêng** của ma trận

### Bài 9.

```c
#include <stdio.h>
#include <stdbool.h>

bool bangNhau(int a[][100], int b[][100], int n, int m) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (a[i][j] != b[i][j]) return false;
    return true;
}

int main() {
    int n = 2, m = 3;
    int a[100][100] = {{1,2,3},{4,5,6}};
    int b[100][100] = {{1,2,3},{4,5,6}};
    int c[100][100] = {{1,2,3},{4,5,9}};

    printf("a == b? %s\n", bangNhau(a, b, n, m) ? "true" : "false");   // true
    printf("a == c? %s\n", bangNhau(a, c, n, m) ? "true" : "false");   // false
    return 0;
}
```

⚠️ **Hai ma trận chỉ bằng nhau khi CÙNG kích thước** và mọi phần tử tương ứng bằng nhau. Trong chương trình thật nên kiểm tra kích thước trước.

⚠️ Trong C **không thể** viết `if (a == b)` để so sánh 2 mảng — biểu thức đó chỉ so sánh **địa chỉ** của 2 mảng (luôn khác nhau). Phải so sánh từng phần tử như hàm `bangNhau`.

### Bài 10.

```c
#include <stdio.h>

int main() {
    int n = 3, m = 3;
    int a[100][100] = {{1,2,3},{4,5,6},{7,8,9}};
    int k;

    printf("Nhap so vo huong k: ");
    scanf("%d", &k);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] *= k;

    printf("Ma tran sau khi nhan %d:\n", k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%6d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

💡 Nhân vô hướng đơn giản hơn nhiều so với nhân 2 ma trận: chỉ O(n×m) thay vì O(n³).

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n, m, a, b;
    printf("Nhap so hang, cot: ");        scanf("%d %d", &n, &m);
    printf("Nhap khoang gia tri [a, b]: "); scanf("%d %d", &a, &b);

    if (a > b) { int t = a; a = b; b = t; }

    srand((unsigned)time(NULL));          // khoi tao hat giong 1 lan duy nhat

    int mt[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mt[i][j] = rand() % (b - a + 1) + a;

    printf("\nMa tran ngau nhien:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%6d", mt[i][j]);
        printf("\n");
    }
    return 0;
}
```

💡 `rand()` (trong `<stdlib.h>`) trả về số nguyên trong `[0, RAND_MAX]`; `rand() % (b - a + 1) + a` đưa về đoạn `[a, b]`. `srand(time(NULL))` (cần `<time.h>`) làm mỗi lần chạy ra dãy khác nhau.

⚠️ Chỉ gọi `srand` **một lần** ở đầu chương trình. Phép `%` làm phân bố **không đều hoàn toàn** khi `b - a + 1` không chia hết `RAND_MAX + 1` — đủ dùng cho bài tập, không dùng cho mật mã.

### Bài 12.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap so dong: ");
    scanf("%d", &n);

    long long pascal[35][35] = {0};

    for (int i = 0; i < n; i++) {
        pascal[i][0] = 1;                                    // cot dau luon = 1
        for (int j = 1; j <= i; j++) {
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];  // cong 2 so phia tren
        }
    }

    // In dang tam giac can
    printf("\nTam giac Pascal:\n");
    for (int i = 0; i < n; i++) {
        printf("%*s", (n - i) * 3, "");                      // canh le trai
        for (int j = 0; j <= i; j++) printf("%6lld", pascal[i][j]);
        printf("\n");
    }
    return 0;
}
```

Với `n = 6`:

```
                       1
                    1     1
                 1     2     1
              1     3     3     1
           1     4     6     4     1
        1     5    10    10     5     1
```

💡 **Công thức:** `C(i,j) = C(i-1,j-1) + C(i-1,j)`. Phần tử `pascal[i][j]` chính là tổ hợp chập `j` của `i`, cũng là hệ số của `x^j` trong khai triển `(a+b)^i`.

💡 `printf("%*s", w, "")` in một chuỗi rỗng với độ rộng `w` lấy từ tham số — tức là in `w` dấu cách.

⚠️ Dùng `long long` (in bằng `%lld`) — `C(60,30)` đã vượt `int`. Mảng khai báo `35×35` nên chỉ nhập `n ≤ 35`.

### Bài 13.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[100][100];
    printf("Nhap ma tran %dx%d:\n", n, n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    // Tinh tong hang dau lam moc
    long long tongChuan = 0;
    for (int j = 0; j < n; j++) tongChuan += a[0][j];

    bool laMaPhuong = true;

    // Kiem tra cac hang
    for (int i = 1; i < n && laMaPhuong; i++) {
        long long t = 0;
        for (int j = 0; j < n; j++) t += a[i][j];
        if (t != tongChuan) laMaPhuong = false;
    }

    // Kiem tra cac cot
    for (int j = 0; j < n && laMaPhuong; j++) {
        long long t = 0;
        for (int i = 0; i < n; i++) t += a[i][j];
        if (t != tongChuan) laMaPhuong = false;
    }

    // Kiem tra 2 duong cheo
    if (laMaPhuong) {
        long long c1 = 0, c2 = 0;
        for (int i = 0; i < n; i++) { c1 += a[i][i]; c2 += a[i][n-1-i]; }
        if (c1 != tongChuan || c2 != tongChuan) laMaPhuong = false;
    }

    printf("\nTong chuan = %lld\n", tongChuan);
    printf("Ma tran %s ma phuong\n", laMaPhuong ? "LA" : "KHONG phai");
    return 0;
}
```

Ví dụ ma phương bậc 3:

```
8 1 6
3 5 7      <- moi hang, cot, cheo deu co tong = 15
4 9 2
```

💡 **Tổng chuẩn của ma phương bậc n** chứa các số 1..n²: `M = n(n²+1)/2`.

| n | Tổng chuẩn |
|---|---|
| 3 | 15 |
| 4 | 34 |
| 5 | 65 |

### Bài 14.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n (phai LE): ");
    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("Phuong phap Siamese chi ap dung cho n LE!\n");
        return 1;
    }

    int a[100][100] = {0};

    // Bat dau: so 1 dat o GIUA hang DAU TIEN
    int i = 0, j = n / 2;

    for (int so = 1; so <= n * n; so++) {
        a[i][j] = so;

        // Di chuyen: LEN 1, PHAI 1 (vong quanh neu ra ngoai)
        int i2 = (i - 1 + n) % n;
        int j2 = (j + 1) % n;

        if (a[i2][j2] != 0) {
            i = (i + 1) % n;          // o do da co so -> di XUONG 1
        } else {
            i = i2; j = j2;
        }
    }

    printf("\nMa phuong bac %d:\n", n);
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) printf("%5d", a[r][c]);
        printf("\n");
    }

    printf("\nTong chuan = %d\n", n * (n * n + 1) / 2);
    return 0;
}
```

Với `n = 5`:

```
   17   24    1    8   15
   23    5    7   14   16
    4    6   13   20   22
   10   12   19   21    3
   11   18   25    2    9

Tong chuan = 65
```

**Phương pháp Siamese (De la Loubère):**
1. Đặt số 1 ở **giữa hàng đầu tiên**
2. Số kế tiếp đặt ở ô **lên 1, phải 1** (đi vòng qua biên nếu ra ngoài)
3. Nếu ô đó **đã có số**, đặt xuống **ngay dưới** ô hiện tại
4. Lặp tới khi hết `n²` số

💡 Phép `(i - 1 + n) % n` xử lý việc "vòng qua biên" — cộng `n` trước để tránh số âm (trong C, `-1 % n` cho kết quả **âm**).

⚠️ Chỉ áp dụng cho `n` **lẻ**. Ma phương bậc chẵn cần phương pháp khác (LUX, Strachey).

### Bài 15.

Để một biến mang theo cả kích thước lẫn dữ liệu, ta gói ma trận vào một **`struct`** gồm kích thước và mảng dữ liệu cố định. Hàm nhận **con trỏ tới `const MaTran`** cho tham số chỉ đọc (không sao chép), và trả về `MaTran` theo giá trị cho các phép tạo ma trận mới.

**File `matran.h`:**

```c
#ifndef MATRAN_H
#define MATRAN_H

#include <stdbool.h>

#define MAX 20

typedef struct {
    int n, m;              /* so hang, so cot */
    long long a[MAX][MAX];
} MaTran;

/** Tao ma tran n x m, moi phan tu = giaTri. */
MaTran taoMaTran(int n, int m, long long giaTri);

/** Tao ma tran don vi n x n. */
MaTran taoDonVi(int n);

/** In ma tran ra man hinh voi nhan (co the NULL) va do rong cot. */
void inMaTran(const MaTran *x, const char *nhan, int doRong);

/** Tra ve ma tran chuyen vi (n x m -> m x n). */
MaTran chuyenVi(const MaTran *x);

/** Xoay ma tran VUONG 90 do theo chieu kim dong ho. */
MaTran xoay90(const MaTran *x);

/** So sanh 2 ma tran co bang nhau khong (ca kich thuoc). */
bool bangNhau(const MaTran *x, const MaTran *y);

/** Vet (trace) - tong duong cheo chinh. Ma tran phai vuong. */
long long vet(const MaTran *x);

/** Nhan ma tran voi so vo huong. */
MaTran nhanVoHuong(const MaTran *x, int k);

/** Kiem tra co phai ma tran vuong. */
bool laVuong(const MaTran *x);

#endif
```

**File `matran.c`:**

```c
#include "matran.h"
#include <stdio.h>

MaTran taoMaTran(int n, int m, long long giaTri) {
    MaTran x;
    x.n = n; x.m = m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) x.a[i][j] = giaTri;
    return x;
}

MaTran taoDonVi(int n) {
    MaTran x = taoMaTran(n, n, 0);
    for (int i = 0; i < n; i++) x.a[i][i] = 1;
    return x;
}

void inMaTran(const MaTran *x, const char *nhan, int doRong) {
    if (nhan != NULL) printf("%s\n", nhan);
    for (int i = 0; i < x->n; i++) {
        for (int j = 0; j < x->m; j++) printf("%*lld", doRong, x->a[i][j]);
        printf("\n");
    }
    printf("\n");
}

MaTran chuyenVi(const MaTran *x) {
    MaTran y = taoMaTran(x->m, x->n, 0);
    for (int i = 0; i < x->n; i++)
        for (int j = 0; j < x->m; j++)
            y.a[j][i] = x->a[i][j];
    return y;
}

MaTran xoay90(const MaTran *x) {
    if (!laVuong(x)) return *x;
    int n = x->n;
    MaTran y = taoMaTran(n, n, 0);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            y.a[j][n - 1 - i] = x->a[i][j];
    return y;
}

bool bangNhau(const MaTran *x, const MaTran *y) {
    if (x->n != y->n || x->m != y->m) return false;
    for (int i = 0; i < x->n; i++)
        for (int j = 0; j < x->m; j++)
            if (x->a[i][j] != y->a[i][j]) return false;
    return true;
}

long long vet(const MaTran *x) {
    if (!laVuong(x)) return 0;
    long long tong = 0;
    for (int i = 0; i < x->n; i++) tong += x->a[i][i];
    return tong;
}

MaTran nhanVoHuong(const MaTran *x, int k) {
    MaTran y = *x;                        /* gan struct = sao chep toan bo */
    for (int i = 0; i < y.n; i++)
        for (int j = 0; j < y.m; j++) y.a[i][j] *= k;
    return y;
}

bool laVuong(const MaTran *x) {
    return x->n > 0 && x->n == x->m;
}
```

**File `main.c`:**

```c
#include <stdio.h>
#include "matran.h"

int main() {
    MaTran a = {3, 3, {{1,2,3}, {4,5,6}, {7,8,9}}};

    inMaTran(&a, "Ma tran goc:", 6);

    MaTran t = chuyenVi(&a);          inMaTran(&t, "Chuyen vi:", 6);
    MaTran x = xoay90(&a);            inMaTran(&x, "Xoay 90 do:", 6);
    MaTran k2 = nhanVoHuong(&a, 2);   inMaTran(&k2, "Nhan voi 2:", 6);
    MaTran dv = taoDonVi(4);          inMaTran(&dv, "Ma tran don vi 4x4:", 6);

    printf("Vet cua a     = %lld\n", vet(&a));                        // 15
    printf("a == a?       %s\n", bangNhau(&a, &a) ? "true" : "false");
    printf("a la vuong?   %s\n", laVuong(&a) ? "true" : "false");

    MaTran b = {2, 3, {{1,2,3}, {4,5,6}}};
    printf("b la vuong?   %s\n", laVuong(&b) ? "true" : "false");
    MaTran tb = chuyenVi(&b);
    inMaTran(&tb, "Chuyen vi cua b (2x3 -> 3x2):", 6);

    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall main.c matran.c -o matran
./matran
```

**Các điểm thiết kế đáng học:**

1. **`typedef struct {...} MaTran`** — gói kích thước và dữ liệu vào một kiểu, code ngắn và rõ hơn nhiều. Phần tử kiểu `long long` (in bằng `%lld`) để các phép nhân ở bài 08-04 ít bị tràn số
2. **`const MaTran *`** cho tham số chỉ đọc — chỉ truyền địa chỉ, không sao chép cả khối dữ liệu, và trình biên dịch chặn việc sửa nhầm
3. **Trả về `MaTran` theo giá trị** thay vì sửa tại chỗ — hàm thuần khiết, dễ kiểm thử. Struct trong C được sao chép khi gán/trả về (khác với mảng thuần)
4. **Kiểm tra `laVuong` trước** các phép chỉ áp dụng cho ma trận vuông
5. **Include guard** `#ifndef MATRAN_H ... #endif` chống include header 2 lần; C không có đối số mặc định nên mọi tham số (`nhan`, `doRong`) phải truyền đủ

⚠️ Kích thước tối đa bị giới hạn bởi `MAX` (ở đây 20). Muốn ma trận lớn tuỳ ý thì cấp phát động bằng `malloc` (bài [07-04](../07-04-c-cap-phat-mang-dong.md)).

💡 Hãy giữ thư viện này và mở rộng thêm ở bài [08-04](../08-04-c-cong-tru-nhan-2-ma-tran.md) (cộng, trừ, nhân ma trận).
