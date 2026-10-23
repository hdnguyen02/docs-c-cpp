# Lời giải — [C]. Cộng, Trừ, Nhân 2 Ma Trận

[← Quay lại bài học](../08-04-c-cong-tru-nhan-2-ma-tran.md)

> **Điều kiện:**
> - **Cộng/trừ:** hai ma trận phải **cùng kích thước** `n×m`
> - **Nhân `A×B`:** số **cột** của A phải bằng số **hàng** của B. Kết quả `A(n×m) × B(m×p) = C(n×p)`

> **Quy ước trong các lời giải:** Để mỗi ma trận mang theo cả kích thước, ta gói ma trận vào một `struct` gồm số hàng `n`, số cột `m` và mảng `a[MAX][MAX]`. Struct nhỏ (`MAX = 10`) nên các hàm nhận và trả về **theo giá trị** (C sao chép cả struct) — viết gọn như công thức toán, lồng được `chuyenVi(cong(a, b))`. Với ma trận lớn nên truyền con trỏ như thư viện ở bài 08-03.

---

### Bài 1.

```c
#include <stdio.h>

#define MAX 10

typedef struct {
    int n, m;                    // so hang, so cot
    long long a[MAX][MAX];
} MaTran;

MaTran cong(MaTran x, MaTran y) {
    MaTran c = {x.n, x.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++)
            c.a[i][j] = x.a[i][j] + y.a[i][j];
    return c;
}

void inMT(MaTran x, const char *nhan) {
    printf("%s\n", nhan);
    for (int i = 0; i < x.n; i++) {
        for (int j = 0; j < x.m; j++) printf("%6lld", x.a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    MaTran a = {2, 3, {{1,2,3},{4,5,6}}};
    MaTran b = {2, 3, {{10,20,30},{40,50,60}}};

    inMT(a, "A:");
    inMT(b, "B:");
    inMT(cong(a, b), "A + B:");
    return 0;
}
```

Output:

```
A + B:
    11    22    33
    44    55    66
```

**Cộng ma trận:** cộng từng cặp phần tử tương ứng. Độ phức tạp **O(n×m)**.

💡 `MaTran a = {2, 3, {{1,2,3},{4,5,6}}};` khởi tạo lần lượt `n = 2`, `m = 3`, rồi mảng `a`; các ô còn lại tự động bằng 0.

### Bài 2.

```c
MaTran tru(MaTran x, MaTran y) {
    MaTran c = {x.n, x.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++)
            c.a[i][j] = x.a[i][j] - y.a[i][j];
    return c;
}
```

⚠️ Phép trừ **không giao hoán**: `A − B ≠ B − A`.

### Bài 3.

```c
#include <stdio.h>

#define MAX 10

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    int n = x.n;          // so hang cua A
    int m = x.m;          // so cot cua A = so hang cua B
    int p = y.m;          // so cot cua B

    MaTran c = {n, p, {{0}}};          // toan bo phan tu = 0

    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c.a[i][j] += x.a[i][k] * y.a[k][j];

    return c;
}

void inMT(MaTran x, const char *nhan) {
    printf("%s\n", nhan);
    for (int i = 0; i < x.n; i++) {
        for (int j = 0; j < x.m; j++) printf("%8lld", x.a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    MaTran a = {2, 3, {{1,2,3},{4,5,6}}};          // 2x3
    MaTran b = {3, 2, {{7,8},{9,10},{11,12}}};     // 3x2

    inMT(a, "A (2x3):");
    inMT(b, "B (3x2):");
    inMT(nhan(a, b), "A x B (2x2):");
    return 0;
}
```

Output:

```
A x B (2x2):
      58      64
     139     154
```

**Công thức:** `C[i][j] = Σ(k=0..m-1) A[i][k] × B[k][j]`

Nghĩa là: phần tử `C[i][j]` = tích vô hướng của **hàng `i` của A** với **cột `j` của B**.

```
C[0][0] = 1×7 + 2×9 + 3×11 = 7 + 18 + 33 = 58  ✔
```

**Độ phức tạp O(n×m×p)** — với ma trận vuông `n×n` là **O(n³)**.

⚠️ **Bắt buộc khởi tạo `c` toàn 0** trước khi cộng dồn — biến cục bộ trong C không tự bằng 0, ở đây ta dùng `{{0}}`.

⚠️ Dùng `long long` (in bằng `%lld`) — tích các phần tử rất dễ tràn `int`.

### Bài 4.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 10

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

bool congDuoc(MaTran x, MaTran y) {
    if (x.n == 0 || y.n == 0) return false;
    return x.n == y.n && x.m == y.m;
}

bool nhanDuoc(MaTran x, MaTran y) {
    if (x.n == 0 || y.n == 0) return false;
    return x.m == y.n;                  // so COT cua A == so HANG cua B
}

const char *tf(bool b) { return b ? "true" : "false"; }

int main() {
    MaTran a = {2, 3, {{1,2,3},{4,5,6}}};          // 2x3
    MaTran b = {2, 3, {{7,8,9},{10,11,12}}};       // 2x3
    MaTran c = {3, 2, {{1,2},{3,4},{5,6}}};        // 3x2

    printf("A(2x3) + B(2x3) duoc? %s\n", tf(congDuoc(a, b)));   // true
    printf("A(2x3) + C(3x2) duoc? %s\n", tf(congDuoc(a, c)));   // false
    printf("A(2x3) x C(3x2) duoc? %s\n", tf(nhanDuoc(a, c)));   // true
    printf("A(2x3) x B(2x3) duoc? %s\n", tf(nhanDuoc(a, b)));   // false
    printf("C(3x2) x A(2x3) duoc? %s\n", tf(nhanDuoc(c, a)));   // true
    return 0;
}
```

**Quy tắc ghi nhớ:**

```
Cong:  A(n x m) + B(n x m) = C(n x m)      <- kich thuoc PHAI GIONG HET
                    ^^^^^

Nhan:  A(n x m) x B(m x p) = C(n x p)      <- so GIUA phai khop
              ^^^   ^^^
```

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 10

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    MaTran c = {x.n, y.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < y.m; j++)
            for (int k = 0; k < x.m; k++)
                c.a[i][j] += x.a[i][k] * y.a[k][j];
    return c;
}

bool bangNhau(MaTran x, MaTran y) {
    if (x.n != y.n || x.m != y.m) return false;
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++)
            if (x.a[i][j] != y.a[i][j]) return false;
    return true;
}

void inMT(MaTran x, const char *nhan) {
    printf("%s\n", nhan);
    for (int i = 0; i < x.n; i++) {
        for (int j = 0; j < x.m; j++) printf("%6lld", x.a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    MaTran a = {2, 2, {{1, 2}, {3, 4}}};
    MaTran b = {2, 2, {{5, 6}, {7, 8}}};

    MaTran ab = nhan(a, b);
    MaTran ba = nhan(b, a);

    inMT(a, "A:");
    inMT(b, "B:");
    inMT(ab, "A x B:");
    inMT(ba, "B x A:");

    printf("A x B == B x A ? %s\n", bangNhau(ab, ba) ? "true" : "false");
    return 0;
}
```

Output:

```
A x B:
    19    22
    43    50

B x A:
    23    34
    31    46

A x B == B x A ? false
```

**Kết luận: phép nhân ma trận KHÔNG GIAO HOÁN.**

Đây là điểm khác biệt quan trọng nhất so với phép nhân số. Ngay cả khi cả hai phép nhân đều thực hiện được, kết quả thường khác nhau.

💡 Thậm chí với ma trận chữ nhật, `A×B` tồn tại không có nghĩa là `B×A` tồn tại: `A(2×3) × B(3×4)` được, nhưng `B(3×4) × A(2×3)` thì không.

⚠️ C không cho so sánh 2 struct bằng `==`, nên phải tự viết hàm `bangNhau` so từng phần tử.

**Nhưng phép nhân ma trận VẪN kết hợp:** `(A×B)×C = A×(B×C)` ✔

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 10

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    MaTran c = {x.n, y.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < y.m; j++)
            for (int k = 0; k < x.m; k++)
                c.a[i][j] += x.a[i][k] * y.a[k][j];
    return c;
}

MaTran donVi(int n) {
    MaTran e = {n, n, {{0}}};
    for (int i = 0; i < n; i++) e.a[i][i] = 1;
    return e;
}

bool bangNhau(MaTran x, MaTran y) {
    if (x.n != y.n || x.m != y.m) return false;
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++)
            if (x.a[i][j] != y.a[i][j]) return false;
    return true;
}

int main() {
    MaTran a = {3, 3, {{1,2,3},{4,5,6},{7,8,9}}};
    MaTran I = donVi(3);

    printf("A x I == A ? %s\n", bangNhau(nhan(a, I), a) ? "true" : "false");  // true
    printf("I x A == A ? %s\n", bangNhau(nhan(I, a), a) ? "true" : "false");  // true
    return 0;
}
```

**Ma trận đơn vị `I` là phần tử đơn vị của phép nhân ma trận** — giống vai trò của số 1 trong phép nhân số.

```
A × I = I × A = A
```

Đây cũng là **trường hợp hiếm hoi** mà phép nhân ma trận giao hoán.

### Bài 7.

```c
#include <stdio.h>

#define MAX 10

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    MaTran c = {x.n, y.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < y.m; j++)
            for (int k = 0; k < x.m; k++)
                c.a[i][j] += x.a[i][k] * y.a[k][j];
    return c;
}

MaTran donVi(int n) {
    MaTran e = {n, n, {{0}}};
    for (int i = 0; i < n; i++) e.a[i][i] = 1;
    return e;
}

// Luy thua CHAM: nhan k lan - O(k * n^3)
MaTran luyThua(MaTran x, int k) {
    MaTran kq = donVi(x.n);
    for (int i = 0; i < k; i++) kq = nhan(kq, x);
    return kq;
}

int main() {
    MaTran a = {2, 2, {{1, 1}, {1, 0}}};

    for (int k = 1; k <= 5; k++) {
        MaTran kq = luyThua(a, k);
        printf("A^%d = [%lld %lld; %lld %lld]\n", k,
               kq.a[0][0], kq.a[0][1], kq.a[1][0], kq.a[1][1]);
    }
    return 0;
}
```

Output:

```
A^1 = [1 1; 1 0]
A^2 = [2 1; 1 1]
A^3 = [3 2; 2 1]
A^4 = [5 3; 3 2]
A^5 = [8 5; 5 3]
```

💡 Nhận ra dãy Fibonacci chưa? `1, 1, 2, 3, 5, 8...` — xem bài 9.

### Bài 8.

```c
#include <stdio.h>

#define MAX 10
#define MOD 1000000007LL

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    MaTran c = {x.n, y.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < y.m; j++)
            for (int k = 0; k < x.m; k++)
                c.a[i][j] = (c.a[i][j] + x.a[i][k] * y.a[k][j]) % MOD;
    return c;
}

MaTran donVi(int n) {
    MaTran e = {n, n, {{0}}};
    for (int i = 0; i < n; i++) e.a[i][i] = 1;
    return e;
}

// Luy thua NHANH: O(log k * n^3)
MaTran luyThuaNhanh(MaTran x, long long k) {
    MaTran kq = donVi(x.n);
    while (k > 0) {
        if (k & 1) kq = nhan(kq, x);
        x = nhan(x, x);
        k >>= 1;
    }
    return kq;
}

int main() {
    MaTran a = {2, 2, {{1, 1}, {1, 0}}};

    MaTran kq = luyThuaNhanh(a, 1000000);
    printf("A^1000000 (mod 1e9+7):\n");
    printf("%lld %lld\n", kq.a[0][0], kq.a[0][1]);
    printf("%lld %lld\n", kq.a[1][0], kq.a[1][1]);
    return 0;
}
```

**So sánh số phép nhân ma trận:**

| k | Luỹ thừa chậm | Luỹ thừa nhanh |
|---|---|---|
| 10 | 10 | ~4 |
| 1.000 | 1.000 | ~10 |
| 10⁹ | 10⁹ (không khả thi) | **~30** |

Nguyên lý giống luỹ thừa nhị phân với số (bài [05-05](../05-05-c-ly-thuyet-so-va-toan-hoc.md) bài 11), chỉ thay phép nhân số bằng phép nhân ma trận.

💡 Tham số `x` được truyền **theo giá trị** nên hàm tha hồ sửa `x = nhan(x, x)` mà không ảnh hưởng ma trận gốc ở `main`.

### Bài 9.

```c
#include <stdio.h>

#define MAX 10
#define MOD 1000000007LL

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    int n = x.n;
    MaTran c = {n, n, {{0}}};
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                c.a[i][j] = (c.a[i][j] + x.a[i][k] * y.a[k][j]) % MOD;
    return c;
}

MaTran luyThuaNhanh(MaTran x, long long k) {
    int n = x.n;
    MaTran kq = {n, n, {{0}}};
    for (int i = 0; i < n; i++) kq.a[i][i] = 1;

    while (k > 0) {
        if (k & 1) kq = nhan(kq, x);
        x = nhan(x, x);
        k >>= 1;
    }
    return kq;
}

long long fibonacci(long long n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    MaTran q = {2, 2, {{1, 1}, {1, 0}}};
    MaTran kq = luyThuaNhanh(q, n - 1);
    return kq.a[0][0];
}

int main() {
    long long ds[] = {1, 10, 50, 1000000, 1000000000000LL};
    int soLuong = sizeof(ds) / sizeof(ds[0]);
    for (int i = 0; i < soLuong; i++) {
        printf("F(%lld) = %lld\n", ds[i], fibonacci(ds[i]));
    }
    return 0;
}
```

Output:

```
F(1) = 1
F(10) = 55
F(50) = 586268941        (da lay mod)
F(1000000) = 918091266
F(1000000000000) = 730695249
```

**Nguyên lý:**

```
| F(n+1) |   | 1  1 |   | F(n)   |
|        | = |      | x |        |
| F(n)   |   | 1  0 |   | F(n-1) |
```

Áp dụng `n−1` lần:

```
| F(n)   |   | 1  1 |^(n-1)   | F(1) |
|        | = |      |       x |      |
| F(n-1) |   | 1  0 |         | F(0) |
```

**So sánh độ phức tạp:**

| Phương pháp | Độ phức tạp | F(10¹²) |
|---|---|---|
| Đệ quy thuần | O(2ⁿ) | Không bao giờ xong |
| Vòng lặp / ghi nhớ | O(n) | ~10¹² bước — quá chậm |
| **Luỹ thừa ma trận** | **O(log n)** | **~40 bước** — tức thì |

💡 Kỹ thuật này áp dụng được cho **mọi dãy truy hồi tuyến tính**: Tribonacci, dãy `a[n] = 3a[n-1] + 2a[n-2]`…

⚠️ Mỗi tích `x.a[i][k] * y.a[k][j]` < (10⁹+7)² ≈ 10¹⁸ vẫn nằm trong `long long` (tối đa ≈ 9,2×10¹⁸) — nên phải lấy `% MOD` **sau mỗi lần cộng**.

### Bài 10.

```c
#include <stdio.h>
#include <time.h>

#define NMAX 400

static long long a[NMAX][NMAX], b[NMAX][NMAX], c[NMAX][NMAX];

int main() {
    int ds[] = {10, 50, 100, 200, 400};
    for (int t = 0; t < 5; t++) {
        int n = ds[t];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) { a[i][j] = 1; b[i][j] = 2; c[i][j] = 0; }

        long long soPhepNhan = 0;

        clock_t t1 = clock();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                    soPhepNhan++;
                }
        clock_t t2 = clock();

        printf("n = %d: %lld phep nhan (n^3 = %lld), %.0f ms\n",
               n, soPhepNhan, (long long)n * n * n,
               (double)(t2 - t1) * 1000 / CLOCKS_PER_SEC);
    }
    return 0;
}
```

Output (thời gian phụ thuộc máy):

```
n = 10: 1000 phep nhan (n^3 = 1000), 0 ms
n = 50: 125000 phep nhan (n^3 = 125000), 1 ms
n = 100: 1000000 phep nhan (n^3 = 1000000), 4 ms
n = 200: 8000000 phep nhan (n^3 = 8000000), 35 ms
n = 400: 64000000 phep nhan (n^3 = 64000000), 290 ms
```

**Kết luận: số phép nhân đúng bằng `n³`.**

Chú ý: khi `n` tăng **gấp đôi**, thời gian tăng **gấp 8** (2³).

💡 Đo thời gian trong C bằng `clock()` của `<time.h>`: hiệu `t2 - t1` chia `CLOCKS_PER_SEC` ra số giây. 3 mảng `400×400` `long long` (~1,3 MB mỗi mảng) được khai báo `static` ngoài hàm để không tràn stack.

💡 **Các thuật toán nhanh hơn O(n³):**

| Thuật toán | Độ phức tạp | Ghi chú |
|---|---|---|
| Ngây thơ | O(n³) | Đơn giản nhất |
| Strassen (1969) | O(n^2.807) | Thực tế nhanh hơn khi n > 100 |
| Coppersmith–Winograd | O(n^2.376) | Chỉ có ý nghĩa lý thuyết |
| Tốt nhất hiện nay | ~O(n^2.371) | Hằng số quá lớn, không dùng thực tế |

💡 **Tối ưu thực tế quan trọng nhất** — đổi thứ tự vòng lặp để thân thiện với cache:

```c
// Cham: b[k][j] nhay lung tung trong bo nho
for (i) for (j) for (k) c[i][j] += a[i][k] * b[k][j];

// Nhanh hon 2-3 lan: truy cap b[k][j] tuan tu theo j
for (i) for (k) for (j) c[i][j] += a[i][k] * b[k][j];
```

### Bài 11.

```c
#include <stdio.h>

// Dinh thuc 2x2: ad - bc
double dinhThuc2(double a[2][2]) {
    return a[0][0] * a[1][1] - a[0][1] * a[1][0];
}

// Dinh thuc 3x3: khai trien theo hang dau
double dinhThuc3(double a[3][3]) {
    return a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
         - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
         + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]);
}

int main() {
    double a[2][2] = {{1, 2}, {3, 4}};
    printf("det(2x2) = %g\n", dinhThuc2(a));        // 1*4 - 2*3 = -2

    double b[3][3] = {{1,2,3}, {4,5,6}, {7,8,10}};
    printf("det(3x3) = %g\n", dinhThuc3(b));        // -3
    return 0;
}
```

**Công thức 2×2:**

```
| a b |
| c d |  =  ad - bc
```

**Công thức 3×3 (khai triển theo hàng đầu):**

```
| a b c |
| d e f |  =  a(ei - fh) - b(di - fg) + c(dh - eg)
| g h i |
```

💡 `%g` in số thực ở dạng gọn nhất (bỏ các số 0 thừa), nên `-2.000000` hiện ra là `-2`.

💡 **Ý nghĩa của định thức:**
- `det = 0` → ma trận **suy biến** (không khả nghịch), hệ phương trình vô nghiệm hoặc vô số nghiệm
- `|det|` = **hệ số co giãn diện tích/thể tích** của phép biến đổi tuyến tính
- Dấu của `det` cho biết phép biến đổi có đảo hướng không

### Bài 12.

```c
#include <stdio.h>
#include <math.h>

#define MAX 10

typedef struct {
    int n;
    double a[MAX][MAX];
} MaTranThuc;

double dinhThuc(MaTranThuc x) {          // struct truyen theo gia tri = BAN SAO, sua thoai mai
    int n = x.n;
    double det = 1.0;
    const double EPS = 1e-12;

    for (int i = 0; i < n; i++) {
        // Tim hang co phan tu tru lon nhat (pivoting - tang do chinh xac)
        int hangTot = i;
        for (int k = i + 1; k < n; k++)
            if (fabs(x.a[k][i]) > fabs(x.a[hangTot][i])) hangTot = k;

        if (fabs(x.a[hangTot][i]) < EPS) return 0.0;    // cot toan 0 -> det = 0

        if (hangTot != i) {
            for (int j = 0; j < n; j++) {               // doi cho 2 hang
                double t = x.a[i][j]; x.a[i][j] = x.a[hangTot][j]; x.a[hangTot][j] = t;
            }
            det = -det;                   // doi cho 2 hang -> doi dau dinh thuc
        }

        det *= x.a[i][i];

        // Khu cac hang phia duoi
        for (int k = i + 1; k < n; k++) {
            double heSo = x.a[k][i] / x.a[i][i];
            for (int j = i; j < n; j++)
                x.a[k][j] -= heSo * x.a[i][j];
        }
    }
    return det;
}

int main() {
    MaTranThuc a = {2, {{1, 2}, {3, 4}}};
    printf("det 2x2 = %.4f\n", dinhThuc(a));             // -2

    MaTranThuc b = {3, {{1,2,3}, {4,5,6}, {7,8,10}}};
    printf("det 3x3 = %.4f\n", dinhThuc(b));             // -3

    MaTranThuc c = {4, {{2,0,0,0}, {0,3,0,0}, {0,0,4,0}, {0,0,0,5}}};
    printf("det 4x4 (duong cheo) = %.4f\n", dinhThuc(c));  // 120

    MaTranThuc d = {2, {{1,2}, {2,4}}};    // 2 hang ti le -> suy bien
    printf("det suy bien = %.4f\n", dinhThuc(d));        // 0
    return 0;
}
```

**Khử Gauss — nguyên lý:** biến ma trận thành **tam giác trên** bằng các phép biến đổi sơ cấp, rồi định thức = tích các phần tử trên đường chéo.

**Ba quy tắc biến đổi:**
1. Đổi chỗ 2 hàng → định thức **đổi dấu**
2. Nhân một hàng với `k` → định thức **nhân `k`**
3. Cộng bội của hàng này vào hàng khác → định thức **không đổi**

**Độ phức tạp O(n³)** — so với khai triển Laplace là O(n!):

| n | Khai triển Laplace | Khử Gauss |
|---|---|---|
| 10 | 3.628.800 | 1.000 |
| 20 | 2,4×10¹⁸ (không khả thi) | 8.000 |

💡 **Pivoting** (chọn hàng có phần tử trụ lớn nhất) rất quan trọng: nó giảm sai số làm tròn khi làm việc với số thực.

⚠️ Dùng `fabs()` (của `<math.h>`) cho số thực, **không** dùng `abs()` — `abs` chỉ dành cho `int` và sẽ cắt mất phần thập phân. Nhớ biên dịch kèm `-lm`.

### Bài 13.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 10

typedef struct {
    int n, m;
    long long a[MAX][MAX];
} MaTran;

MaTran nhan(MaTran x, MaTran y) {
    MaTran c = {x.n, y.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < y.m; j++)
            for (int k = 0; k < x.m; k++)
                c.a[i][j] += x.a[i][k] * y.a[k][j];
    return c;
}

MaTran cong(MaTran x, MaTran y) {
    MaTran c = {x.n, x.m, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++) c.a[i][j] = x.a[i][j] + y.a[i][j];
    return c;
}

MaTran chuyenVi(MaTran x) {
    MaTran t = {x.m, x.n, {{0}}};
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++) t.a[j][i] = x.a[i][j];
    return t;
}

bool bangNhau(MaTran x, MaTran y) {
    if (x.n != y.n || x.m != y.m) return false;
    for (int i = 0; i < x.n; i++)
        for (int j = 0; j < x.m; j++)
            if (x.a[i][j] != y.a[i][j]) return false;
    return true;
}

const char *tf(bool b) { return b ? "true" : "false"; }

int main() {
    MaTran a = {2, 3, {{1,2,3}, {4,5,6}}};         // 2x3
    MaTran b = {2, 3, {{7,8,9}, {10,11,12}}};      // 2x3
    MaTran c = {3, 2, {{1,2}, {3,4}, {5,6}}};      // 3x2

    // Tinh chat 1: (A + B)^T = A^T + B^T
    bool tc1 = bangNhau(chuyenVi(cong(a, b)), cong(chuyenVi(a), chuyenVi(b)));
    printf("(A + B)^T == A^T + B^T ? %s\n", tf(tc1));      // true

    // Tinh chat 2: (A x C)^T = C^T x A^T   -- CHU Y THU TU BI DAO!
    bool tc2 = bangNhau(chuyenVi(nhan(a, c)), nhan(chuyenVi(c), chuyenVi(a)));
    printf("(A x C)^T == C^T x A^T ? %s\n", tf(tc2));      // true

    // Kiem tra thu tu SAI
    // nhan(chuyenVi(a), chuyenVi(c)): A^T la 3x2, C^T la 2x3 -> ra 3x3, sai kich thuoc

    // Tinh chat 3: (A^T)^T = A
    printf("(A^T)^T == A ? %s\n", tf(bangNhau(chuyenVi(chuyenVi(a)), a)));   // true
    return 0;
}
```

**Các tính chất của chuyển vị:**

| Tính chất | Công thức |
|---|---|
| Chuyển vị 2 lần | `(Aᵀ)ᵀ = A` |
| Cộng | `(A + B)ᵀ = Aᵀ + Bᵀ` |
| Nhân vô hướng | `(kA)ᵀ = kAᵀ` |
| **Nhân ma trận** | **`(A × B)ᵀ = Bᵀ × Aᵀ`** ⚠️ đảo thứ tự! |

⚠️ Tính chất cuối là điểm hay nhầm nhất: thứ tự bị **đảo ngược**, không phải `Aᵀ × Bᵀ`.

### Bài 14.

```c
#include <stdio.h>
#include <math.h>

double det3(double a[3][3]) {
    return a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
         - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
         + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]);
}

// Chep a vao kq, roi thay cot k bang vector b
void thayCot(double a[3][3], const double b[3], int k, double kq[3][3]) {
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) kq[i][j] = a[i][j];
    for (int i = 0; i < 3; i++) kq[i][k] = b[i];
}

int main() {
    printf("Giai he:\n");
    printf("  a1*x + b1*y + c1*z = d1\n");
    printf("  a2*x + b2*y + c2*z = d2\n");
    printf("  a3*x + b3*y + c3*z = d3\n");

    double A[3][3], B[3];

    for (int i = 0; i < 3; i++) {
        printf("Nhap a%d b%d c%d d%d: ", i + 1, i + 1, i + 1, i + 1);
        scanf("%lf %lf %lf %lf", &A[i][0], &A[i][1], &A[i][2], &B[i]);
    }

    double T[3][3];
    double D  = det3(A);
    thayCot(A, B, 0, T); double Dx = det3(T);
    thayCot(A, B, 1, T); double Dy = det3(T);
    thayCot(A, B, 2, T); double Dz = det3(T);

    const double EPS = 1e-9;
    printf("\nD = %.4f, Dx = %.4f, Dy = %.4f, Dz = %.4f\n", D, Dx, Dy, Dz);

    if (fabs(D) > EPS) {
        printf("\nHe co nghiem duy nhat:\n");
        printf("  x = %.4f\n", Dx / D);
        printf("  y = %.4f\n", Dy / D);
        printf("  z = %.4f\n", Dz / D);
    } else if (fabs(Dx) < EPS && fabs(Dy) < EPS && fabs(Dz) < EPS) {
        printf("\nHe co VO SO nghiem\n");
    } else {
        printf("\nHe VO NGHIEM\n");
    }
    return 0;
}
```

Ví dụ với hệ:

```
x + 2y + 3z = 14
2x + y + z  = 7
3x + 2y + z = 10
```

Input: `1 2 3 14`, `2 1 1 7`, `3 2 1 10` → `D = 4`, nghiệm `x = 1, y = 2, z = 3`

⚠️ `scanf` đọc `double` phải dùng **`%lf`** (còn `printf` in `double` dùng `%f` hoặc `%.4f`).

**Quy tắc Cramer:**
- `D` = định thức ma trận hệ số
- `Dx` = định thức khi thay **cột x** bằng cột vế phải
- Nghiệm: `x = Dx/D`, `y = Dy/D`, `z = Dz/D`

**Biện luận:**

| Điều kiện | Kết luận |
|---|---|
| `D ≠ 0` | Nghiệm duy nhất |
| `D = 0` và `Dx = Dy = Dz = 0` | Vô số nghiệm |
| `D = 0` và có `Dx`, `Dy` hoặc `Dz` ≠ 0 | Vô nghiệm |

⚠️ Cramer chỉ thực tế với hệ nhỏ (n ≤ 4). Với `n` lớn, độ phức tạp tính định thức khiến nó chậm hơn nhiều so với **khử Gauss** (O(n³)).

⚠️ Với `D = 0`, việc `Dx = Dy = Dz = 0` là điều kiện **cần** để có vô số nghiệm, trong một số trường hợp đặc biệt hệ vẫn có thể vô nghiệm — muốn biện luận chính xác tuyệt đối thì dùng khử Gauss.

### Bài 15.

Mở rộng thư viện `struct MaTran` ở bài [08-03](../08-03-c-ma-tran-va-mang-2-chieu.md) bài 15 (kiểu phần tử `long long`, hàm nhận `const MaTran *`).

**`matran.h` đầy đủ sau khi bổ sung:**

```c
#ifndef MATRAN_H
#define MATRAN_H

#include <stdbool.h>

#define MAX 20

typedef struct {
    int n, m;              /* so hang, so cot */
    long long a[MAX][MAX];
} MaTran;

/* ---- Cac ham tu bai 08-03 ---- */
MaTran taoMaTran(int n, int m, long long giaTri);
MaTran taoDonVi(int n);
void   inMaTran(const MaTran *x, const char *nhan, int doRong);
MaTran chuyenVi(const MaTran *x);
MaTran xoay90(const MaTran *x);
bool   bangNhau(const MaTran *x, const MaTran *y);
long long vet(const MaTran *x);
MaTran nhanVoHuong(const MaTran *x, int k);
bool   laVuong(const MaTran *x);

/* ---- Cac ham moi ---- */

/** Kiem tra 2 ma tran co cong duoc (cung kich thuoc). */
bool congDuoc(const MaTran *x, const MaTran *y);

/** Kiem tra A x B co thuc hien duoc (cot A == hang B). */
bool nhanDuoc(const MaTran *x, const MaTran *y);

/** Cong 2 ma tran. Tra ve ma tran rong (0 x 0) neu khong hop le. */
MaTran cong(const MaTran *x, const MaTran *y);

/** Tru 2 ma tran. */
MaTran tru(const MaTran *x, const MaTran *y);

/** Nhan 2 ma tran. Do phuc tap O(n*m*p). */
MaTran nhan(const MaTran *x, const MaTran *y);

/**
 * Tinh A^k bang luy thua nhi phan. Do phuc tap O(n^3 * log k).
 * mod > 0: moi phep tinh lay du cho mod; mod = 0: khong lay du.
 */
MaTran luyThua(const MaTran *x, long long k, long long mod);

/** Tinh dinh thuc bang khu Gauss. Do phuc tap O(n^3). */
double dinhThuc(const MaTran *x);

#endif
```

**Bổ sung vào cuối `matran.c`** (giữ nguyên các hàm của bài 08-03, thêm `#include <math.h>` ở đầu file):

```c
#include <math.h>

bool congDuoc(const MaTran *x, const MaTran *y) {
    if (x->n == 0 || y->n == 0) return false;
    return x->n == y->n && x->m == y->m;
}

bool nhanDuoc(const MaTran *x, const MaTran *y) {
    if (x->n == 0 || y->n == 0) return false;
    return x->m == y->n;
}

MaTran cong(const MaTran *x, const MaTran *y) {
    if (!congDuoc(x, y)) return taoMaTran(0, 0, 0);
    MaTran c = taoMaTran(x->n, x->m, 0);
    for (int i = 0; i < x->n; i++)
        for (int j = 0; j < x->m; j++) c.a[i][j] = x->a[i][j] + y->a[i][j];
    return c;
}

MaTran tru(const MaTran *x, const MaTran *y) {
    if (!congDuoc(x, y)) return taoMaTran(0, 0, 0);
    MaTran c = taoMaTran(x->n, x->m, 0);
    for (int i = 0; i < x->n; i++)
        for (int j = 0; j < x->m; j++) c.a[i][j] = x->a[i][j] - y->a[i][j];
    return c;
}

MaTran nhan(const MaTran *x, const MaTran *y) {
    if (!nhanDuoc(x, y)) return taoMaTran(0, 0, 0);
    int n = x->n, m = x->m, p = y->m;
    MaTran c = taoMaTran(n, p, 0);
    /* Thu tu i-k-j: than thien voi CPU cache hon i-j-k */
    for (int i = 0; i < n; i++)
        for (int k = 0; k < m; k++) {
            long long tam = x->a[i][k];
            for (int j = 0; j < p; j++) c.a[i][j] += tam * y->a[k][j];
        }
    return c;
}

/* Ham phu (static = chi dung trong file nay): nhan 2 ma tran vuong co lay du */
static MaTran nhanMod(const MaTran *x, const MaTran *y, long long mod) {
    int n = x->n;
    MaTran z = taoMaTran(n, n, 0);
    for (int i = 0; i < n; i++)
        for (int p = 0; p < n; p++) {
            long long t = x->a[i][p];
            if (t == 0) continue;
            for (int j = 0; j < n; j++) {
                z.a[i][j] += t * y->a[p][j];
                if (mod > 0) z.a[i][j] %= mod;
            }
        }
    return z;
}

MaTran luyThua(const MaTran *x, long long k, long long mod) {
    if (!laVuong(x) || k < 0) return taoMaTran(0, 0, 0);
    MaTran kq = taoDonVi(x->n);
    MaTran co = *x;                       /* ban sao de binh phuong dan */

    while (k > 0) {
        if (k & 1) kq = nhanMod(&kq, &co, mod);
        co = nhanMod(&co, &co, mod);
        k >>= 1;
    }
    return kq;
}

double dinhThuc(const MaTran *x) {
    if (!laVuong(x)) return 0.0;
    int n = x->n;

    double a[MAX][MAX];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) a[i][j] = (double)x->a[i][j];

    double det = 1.0;
    const double EPS = 1e-12;

    for (int i = 0; i < n; i++) {
        int tot = i;
        for (int k = i + 1; k < n; k++)
            if (fabs(a[k][i]) > fabs(a[tot][i])) tot = k;

        if (fabs(a[tot][i]) < EPS) return 0.0;
        if (tot != i) {
            for (int j = 0; j < n; j++) {
                double t = a[i][j]; a[i][j] = a[tot][j]; a[tot][j] = t;
            }
            det = -det;
        }

        det *= a[i][i];
        for (int k = i + 1; k < n; k++) {
            double h = a[k][i] / a[i][i];
            for (int j = i; j < n; j++) a[k][j] -= h * a[i][j];
        }
    }
    return det;
}
```

**Kiểm thử `main.c`:**

```c
#include <stdio.h>
#include "matran.h"

int main() {
    MaTran a = {2, 2, {{1,2},{3,4}}};
    MaTran b = {2, 2, {{5,6},{7,8}}};
    MaTran kq;

    inMaTran(&a, "A:", 8);
    inMaTran(&b, "B:", 8);
    kq = cong(&a, &b);        inMaTran(&kq, "A + B:", 8);
    kq = tru(&a, &b);         inMaTran(&kq, "A - B:", 8);
    kq = nhan(&a, &b);        inMaTran(&kq, "A x B:", 8);
    kq = nhan(&b, &a);        inMaTran(&kq, "B x A (khac A x B!):", 8);
    kq = luyThua(&a, 5, 0);   inMaTran(&kq, "A^5:", 8);
    kq = chuyenVi(&a);        inMaTran(&kq, "A^T:", 8);

    printf("det(A) = %g\n", dinhThuc(&a));          // -2
    printf("vet(A) = %lld\n", vet(&a));             // 5

    // Fibonacci bang luy thua ma tran
    MaTran fib = {2, 2, {{1,1},{1,0}}};
    kq = luyThua(&fib, 49, 0);
    printf("\nF(50) = %lld\n", kq.a[0][0]);
    kq = luyThua(&fib, 999999999999LL, 1000000007);
    printf("F(10^12) mod 1e9+7 = %lld\n", kq.a[0][0]);

    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall -O2 main.c matran.c -o matran -lm
```

💡 Hàm `nhanMod` được khai báo `static` — nó chỉ là hàm phụ nội bộ của `matran.c`, không đưa vào header nên file khác không gọi được.
