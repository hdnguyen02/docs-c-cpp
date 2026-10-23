# Lời giải — [C]. Lý Thuyết Mảng 2 Chiều

[← Quay lại bài học](../08-01-c-ly-thuyet-mang-2-chieu.md)

> **Khai báo:** `int a[n][m]` — `n` hàng, `m` cột. Truy cập `a[i][j]` với `i` là **hàng**, `j` là **cột**.

---

### Bài 1.

```c
#include <stdio.h>

#define MAX 100

int main(void) {
    int a[MAX][MAX], n, m;

    printf("Nhap so hang va so cot: ");
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            printf("  a[%d][%d] = ", i, j);
            scanf("%d", &a[i][j]);
        }

    printf("\nMa tran %d x %d:\n", n, m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%6d", a[i][j]);   // can phai, rong 6
        printf("\n");
    }
    return 0;
}
```

💡 **Mẫu chuẩn duyệt ma trận:** vòng ngoài cho **hàng** (`i`), vòng trong cho **cột** (`j`).

💡 `%6d` in số căn phải trong ô rộng 6 ký tự; `%-6d` để căn trái.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    long long tong = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) tong += a[i][j];

    printf("Tong       = %lld\n", tong);
    printf("Trung binh = %.4f\n", (double)tong / (n * m));
    return 0;
}
```

⚠️ Phải ép `(double)` trước khi chia, nếu không `tong / (n * m)` là phép chia **nguyên**.

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int maxI = 0, maxJ = 0, minI = 0, minJ = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (a[i][j] > a[maxI][maxJ]) { maxI = i; maxJ = j; }
            if (a[i][j] < a[minI][minJ]) { minI = i; minJ = j; }
        }

    printf("Lon nhat  = %d tai (%d, %d)\n", a[maxI][maxJ], maxI, maxJ);
    printf("Nho nhat  = %d tai (%d, %d)\n", a[minI][minJ], minI, minJ);
    return 0;
}
```

⚠️ Khởi tạo bằng **vị trí (0,0)**, không phải bằng 0 — nếu ma trận toàn số âm, khởi tạo `max = 0` sẽ sai.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    long long tongHang[100] = {0}, tongCot[100] = {0};

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            tongHang[i] += a[i][j];
            tongCot[j]  += a[i][j];
        }

    // In ma tran kem tong hang
    printf("\nMa tran va tong:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%6d", a[i][j]);
        printf("  |%7lld\n", tongHang[i]);
    }

    // Duong ke
    for (int j = 0; j < m; j++) printf("------");
    printf("--+\n");

    // Dong tong cot
    for (int j = 0; j < m; j++) printf("%6lld", tongCot[j]);
    printf("\n");
    return 0;
}
```

Ví dụ:

```
     1     2     3  |      6
     4     5     6  |     15
     7     8     9  |     24
--------------------+
    12    15    18
```

💡 **Tính cả 2 tổng trong MỘT lần duyệt** — không cần duyệt 2 lần.

💡 `= {0}` khởi tạo toàn bộ mảng bằng 0 (các phần tử không ghi rõ tự động là 0).

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int duong = 0, am = 0, khong = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if      (a[i][j] > 0) duong++;
            else if (a[i][j] < 0) am++;
            else                  khong++;
        }

    printf("So duong  : %d\n", duong);
    printf("So am     : %d\n", am);
    printf("So bang 0 : %d\n", khong);
    return 0;
}
```

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("Cac phan tu o vien: ");
    long long tongVien = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                printf("%d ", a[i][j]);
                tongVien += a[i][j];
            }
        }
    printf("\nTong vien = %lld\n", tongVien);

    // In truc quan: vien giu nguyen, ben trong thay bang dau .
    printf("\nHinh anh truc quan:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 || i == n - 1 || j == 0 || j == m - 1)
                printf("%5d", a[i][j]);
            else
                printf("%5s", ".");
        }
        printf("\n");
    }
    return 0;
}
```

**Điều kiện viền:** `i == 0` (hàng đầu) **hoặc** `i == n-1` (hàng cuối) **hoặc** `j == 0` (cột đầu) **hoặc** `j == m-1` (cột cuối).

### Bài 7.

```c
#include <stdio.h>

void inMT(const char *nhan, int a[][4], int n) {
    printf("%s:\n", nhan);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main(void) {
    // (1) Khoi tao day du
    int a[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // (2) Khoi tao THIEU -> phan con lai tu dong = 0
    int b[3][4] = {
        {1, 2},
        {3}
    };

    // (3) Khoi tao TOAN 0
    int c[3][4] = {0};

    // (4) Khoi tao phang (khong co ngoac trong) - van hop le
    int d[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

    inMT("(1) Day du   ", a, 3);
    inMT("(2) Thieu    ", b, 3);
    inMT("(3) Toan 0   ", c, 3);
    inMT("(4) Phang    ", d, 3);
    return 0;
}
```

Output của (2) :

```
(2) Thieu    :
    1    2    0    0
    3    0    0    0
    0    0    0    0
```

💡 Cách (4) hợp lệ nhưng gcc với `-Wall` sẽ cảnh báo `missing braces around initializer` — nên viết có ngoặc từng hàng như cách (1) cho dễ đọc.

⚠️ **Không khởi tạo gì cả** (`int e[3][4];` bên trong hàm) → toàn giá trị **rác**. Mảng khai báo **toàn cục** hoặc `static` thì tự động là 0.

💡 Trong C, dùng `= {0}` để khởi tạo toàn 0. Cách viết `= {}` (ngoặc rỗng) chỉ hợp lệ từ chuẩn C23.

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    int a[3][4];

    printf("Dia chi tung phan tu:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            printf("a[%d][%d] = %p", i, j, (void *)&a[i][j]);
            if (!(i == 0 && j == 0))
                printf("  (+%td byte)", (char *)&a[i][j] - (char *)&a[0][0]);
            printf("\n");
        }
    }

    printf("\nsizeof(a)       = %zu byte\n", sizeof(a));        // 48
    printf("sizeof(a[0])    = %zu byte\n", sizeof(a[0]));       // 16
    printf("sizeof(a[0][0]) = %zu byte\n", sizeof(a[0][0]));    // 4

    // Truy cap nhu mang 1 chieu
    int *p = &a[0][0];
    for (int i = 0; i < 12; i++) p[i] = i;

    printf("\nMa tran sau khi dien qua con tro 1 chieu:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) printf("%d\t", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

Output (địa chỉ tăng đều 4 byte):

```
a[0][0] = 0x7ffd1000
a[0][1] = 0x7ffd1004  (+4 byte)
a[0][2] = 0x7ffd1008  (+8 byte)
a[0][3] = 0x7ffd100c  (+12 byte)
a[1][0] = 0x7ffd1010  (+16 byte)    <- tiep ngay sau a[0][3]
...
```

**Kết luận: mảng 2 chiều được lưu THEO HÀNG, liên tiếp trong bộ nhớ (row-major order).**

```
Bo nho: [a00][a01][a02][a03][a10][a11][a12][a13][a20][a21][a22][a23]
         <---- hang 0 ----> <---- hang 1 ----> <---- hang 2 ---->
```

**Công thức chuyển đổi:** `a[i][j]` nằm ở vị trí `i * m + j` trong bộ nhớ.

💡 **Hệ quả về hiệu năng:** duyệt **theo hàng** (`for i { for j }`) nhanh hơn duyệt **theo cột** đáng kể, vì CPU cache nạp các ô liền kề. Với ma trận lớn, chênh lệch có thể tới 5–10 lần.

### Bài 9.

```c
#include <stdio.h>

#define SO_COT 4

// Cach 1: PHAI chi ro so COT (co the bo so hang)
void inMT(int a[][SO_COT], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < SO_COT; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
}

// Cach 2: dung con tro toi mang (tuong duong cach 1)
void inMT2(int (*a)[SO_COT], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < SO_COT; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
}

// Cach 3 (C99): so cot la THAM SO - truyen n, m TRUOC mang
void inMT3(int n, int m, int a[n][m]) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
}

int main(void) {
    int a[3][SO_COT] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    inMT(a, 3);
    printf("\n");
    inMT2(a, 3);
    printf("\n");

    int b[2][3] = {{1, 2, 3}, {4, 5, 6}};   // so cot khac van dung duoc cach 3
    inMT3(3, SO_COT, a);
    printf("\n");
    inMT3(2, 3, b);
    return 0;
}
```

**Vì sao PHẢI chỉ rõ số cột:**

Compiler cần biết số cột để tính địa chỉ của `a[i][j]`:

```
dia chi a[i][j] = dia chi goc + (i * SO_COT + j) * sizeof(int)
                                     ^^^^^^
                            BAT BUOC phai biet
```

Nếu viết `void f(int a[][])` → lỗi:

```
error: array type has incomplete element type 'int[]'
note: declaration of 'a' as multidimensional array must have bounds for all dimensions except the first
```

**Số hàng thì không cần** vì nó không tham gia vào công thức tính địa chỉ.

⚠️ **Hạn chế của cách 1, 2:** hàm chỉ dùng được với ma trận có **đúng** số cột đó. Muốn tổng quát, có thể:

```c
// (1) C99: tham so VLA - so cot truyen vao luc chay (cach 3 o tren)
void inMT3(int n, int m, int a[n][m]);

// (2) Mang 1 chieu + tu tinh chi so
void inMT4(const int *a, int n, int m) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            printf("%d ", a[i * m + j]);
}
// goi: inMT4(&a[0][0], 3, 4);
```

### Bài 10.

```c
#include <stdio.h>
#include <limits.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    // Tong hang lon nhat
    int hangMax = 0;
    long long tongHangMax = LLONG_MIN;
    for (int i = 0; i < n; i++) {
        long long tong = 0;
        for (int j = 0; j < m; j++) tong += a[i][j];
        if (tong > tongHangMax) { tongHangMax = tong; hangMax = i; }
    }

    // Tong cot nho nhat
    int cotMin = 0;
    long long tongCotMin = LLONG_MAX;
    for (int j = 0; j < m; j++) {
        long long tong = 0;
        for (int i = 0; i < n; i++) tong += a[i][j];
        if (tong < tongCotMin) { tongCotMin = tong; cotMin = j; }
    }

    printf("Hang %d co tong lon nhat = %lld\n", hangMax, tongHangMax);
    printf("Cot  %d co tong nho nhat = %lld\n", cotMin, tongCotMin);
    return 0;
}
```

Nhớ `#include <limits.h>` cho `LLONG_MIN`/`LLONG_MAX`.

### Bài 11.

```c
#include <stdio.h>

#define N 3
#define M 4

int main(void) {
    int a[N][M] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    int b[N * M];

    // (1) Ma tran -> mang 1 chieu
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            b[i * M + j] = a[i][j];          // CONG THUC CHUYEN DOI

    printf("Mang 1 chieu: ");
    for (int k = 0; k < N * M; k++) printf("%d ", b[k]);
    printf("\n");

    // (2) Mang 1 chieu -> ma tran
    int c[N][M];
    for (int k = 0; k < N * M; k++) {
        int i = k / M;                        // CHI SO HANG
        int j = k % M;                        // CHI SO COT
        c[i][j] = b[k] * 10;
    }

    printf("\nMa tran khoi phuc (x10):\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) printf("%5d", c[i][j]);
        printf("\n");
    }
    return 0;
}
```

**Hai công thức cần thuộc:**

| Chiều | Công thức |
|---|---|
| 2D → 1D | `k = i * M + j` |
| 1D → 2D | `i = k / M`, `j = k % M` |

⚠️ Luôn dùng **số CỘT (`M`)** trong cả hai công thức, không phải số hàng.

💡 Dùng `#define` cho kích thước để có thể khai báo mảng thường và khởi tạo bằng `= {...}` (mảng VLA thì không khởi tạo được).

💡 **Ứng dụng:** lưu ma trận trong một khối nhớ liền, truyền hàm dễ hơn, và nhanh hơn (tốt cho cache).

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int a[100][100], n;
    printf("Nhap kich thuoc ma tran vuong: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    bool laDonVi = true;
    for (int i = 0; i < n && laDonVi; i++) {
        for (int j = 0; j < n; j++) {
            int canCo = (i == j) ? 1 : 0;      // duong cheo chinh = 1, con lai = 0
            if (a[i][j] != canCo) { laDonVi = false; break; }
        }
    }

    printf("Ma tran %s ma tran don vi\n", laDonVi ? "LA" : "KHONG phai");
    return 0;
}
```

**Ma trận đơn vị** (identity matrix) — ma trận vuông có đường chéo chính toàn 1, còn lại toàn 0:

```
1 0 0
0 1 0
0 0 1
```

### Bài 13.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(int n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int dem = 0;
    long long tong = 0;

    printf("Cac so nguyen to: ");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (laNguyenTo(a[i][j])) {
                printf("%d(%d,%d) ", a[i][j], i, j);
                dem++;
                tong += a[i][j];
            }

    printf("\nSo luong: %d, tong = %lld\n", dem, tong);
    return 0;
}
```

💡 Điều kiện `i * i <= n` thay cho `i <= sqrt(n)` giúp không cần `<math.h>` và tránh sai số số thực.

### Bài 14.

```c
#include <stdio.h>

int main(void) {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("\nDuyet theo HANG: ");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) printf("%d ", a[i][j]);
    printf("\n");

    printf("Duyet theo COT: ");
    for (int j = 0; j < m; j++)             // COT o vong NGOAI
        for (int i = 0; i < n; i++)         // HANG o vong TRONG
            printf("%d ", a[i][j]);
    printf("\n");
    return 0;
}
```

Với ma trận:

```
1 2 3
4 5 6
```

```
Duyet theo HANG: 1 2 3 4 5 6 
Duyet theo COT: 1 4 2 5 3 6 
```

💡 **Chỉ cần đổi chỗ 2 vòng lặp.** Nhưng nhớ rằng duyệt theo cột **chậm hơn** do không tận dụng được CPU cache (xem bài 8).

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 3, m = 4;

    // ========== (1) MANG TINH 2 CHIEU ==========
    int a[3][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
    printf("(1) Mang tinh:\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) printf("%5d", a[i][j]);
        printf("\n");
    }

    // ========== (2) int** CAP PHAT DONG ==========
    int **b = malloc(n * sizeof(int *));
    if (b == NULL) return 1;
    for (int i = 0; i < n; i++) {
        b[i] = malloc(m * sizeof(int));
        if (b[i] == NULL) return 1;          // don gian hoa
    }
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) b[i][j] = (i + 1) * (j + 1);

    printf("\n(2) int** dong:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", b[i][j]);
        printf("\n");
    }
    for (int i = 0; i < n; i++) free(b[i]);
    free(b);

    // ========== (3) MANG 1 CHIEU DONG CO n*m ==========
    int *c = malloc(n * m * sizeof(int));
    if (c == NULL) return 1;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) c[i * m + j] = i * m + j;

    printf("\n(3) Mang 1 chieu n*m:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", c[i * m + j]);
        printf("\n");
    }
    free(c);

    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Mảng tĩnh `int a[3][4]` | `int**` động | Mảng 1 chiều động `n*m` |
|---|---|---|---|
| **Kích thước** | ⚠️ Cố định lúc biên dịch | ✅ Lúc chạy | ✅ Lúc chạy, đổi được bằng `realloc` |
| **Bộ nhớ** | Stack (giới hạn 1–8 MB) hoặc vùng tĩnh nếu toàn cục | Heap | Heap |
| **Liên tục trong bộ nhớ** | ✅ Có (nhanh nhất) | ❌ Không (mỗi hàng một chỗ) | ✅ Có |
| **Tốc độ truy cập** | Nhanh nhất | Chậm hơn (2 lần giải tham chiếu) | Gần bằng mảng tĩnh |
| **Số lần cấp phát/giải phóng** | 0 (tự động) | ⚠️ `n + 1` lần, dễ rò rỉ | ✅ 1 lần |
| **Cú pháp truy cập** | ✅ `a[i][j]` | ✅ `b[i][j]` | ⚠️ `c[i*m + j]` |
| **Truyền vào hàm** | ⚠️ Phải cố định số cột (hoặc dùng tham số VLA) | ✅ Linh hoạt | ✅ Linh hoạt |
| **Biết kích thước** | ✅ `sizeof` (trong phạm vi khai báo) | ❌ Phải truyền kèm | ❌ Phải truyền kèm |
| **Hàng có độ dài khác nhau** | ❌ Không | ✅ Được | ❌ Không |
| **An toàn** | ⚠️ Không kiểm tra biên | ⚠️ Nguy hiểm nhất | ⚠️ Không kiểm tra biên |

**✅ Khuyến nghị:**

| Tình huống | Nên dùng |
|---|---|
| Kích thước nhỏ, biết trước, cần tốc độ tối đa | **Mảng tĩnh** |
| Lập trình thi đấu | **Mảng tĩnh toàn cục** (`int a[1005][1005];` ngoài `main`) |
| Kích thước lúc chạy, cần tốc độ | **Mảng 1 chiều động `n*m`** |
| Các hàng có độ dài khác nhau (ví dụ tam giác Pascal) | `int**` |

💡 **Mẹo kết hợp ưu điểm (C99)** — cấp phát 1 khối liền nhưng vẫn viết được `a[i][j]` bằng **con trỏ tới mảng**:

```c
int (*mt)[m] = malloc(n * sizeof *mt);    // n hang, moi hang m int, 1 khoi lien
mt[1][2] = 99;                            // dung nhu ma tran
printf("%d\n", mt[1][2]);
free(mt);                                 // chi 1 lenh free
```

Cách này vừa nhanh như mảng tĩnh, vừa có kích thước xác định lúc chạy.
