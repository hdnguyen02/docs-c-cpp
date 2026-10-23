# Lời giải — [C++]. Cộng, Trừ, Nhân 2 Ma Trận C++

[← Quay lại bài học](../08-04-c-cong-tru-nhan-2-ma-tran-c.md)

> **Điều kiện:**
> - **Cộng/trừ:** hai ma trận phải **cùng kích thước** `n×m`
> - **Nhân `A×B`:** số **cột** của A phải bằng số **hàng** của B. Kết quả `A(n×m) × B(m×p) = C(n×p)`

---

### Bài 1.

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

MaTran cong(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size();
    MaTran c(n, vector<long long>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            c[i][j] = a[i][j] + b[i][j];
    return c;
}

void inMT(const MaTran& a, const string& nhan) {
    cout << nhan << endl;
    for (const auto& h : a) {
        for (long long x : h) cout << setw(6) << x;
        cout << endl;
    }
    cout << endl;
}

int main() {
    MaTran a = {{1,2,3},{4,5,6}};
    MaTran b = {{10,20,30},{40,50,60}};

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

### Bài 2.

```cpp
MaTran tru(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size();
    MaTran c(n, vector<long long>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            c[i][j] = a[i][j] - b[i][j];
    return c;
}
```

⚠️ Phép trừ **không giao hoán**: `A − B ≠ B − A`.

### Bài 3.

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size();          // so hang cua A
    int m = a[0].size();       // so cot cua A = so hang cua B
    int p = b[0].size();       // so cot cua B

    MaTran c(n, vector<long long>(p, 0));

    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c[i][j] += a[i][k] * b[k][j];

    return c;
}

void inMT(const MaTran& a, const string& nhan) {
    cout << nhan << endl;
    for (const auto& h : a) {
        for (long long x : h) cout << setw(8) << x;
        cout << endl;
    }
    cout << endl;
}

int main() {
    MaTran a = {{1,2,3},{4,5,6}};          // 2x3
    MaTran b = {{7,8},{9,10},{11,12}};     // 3x2

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

⚠️ **Bắt buộc khởi tạo `c` toàn 0** trước khi cộng dồn.

⚠️ Dùng `long long` — tích các phần tử rất dễ tràn `int`.

### Bài 4.

```cpp
#include <iostream>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

bool congDuoc(const MaTran& a, const MaTran& b) {
    if (a.empty() || b.empty()) return false;
    return a.size() == b.size() && a[0].size() == b[0].size();
}

bool nhanDuoc(const MaTran& a, const MaTran& b) {
    if (a.empty() || b.empty()) return false;
    return a[0].size() == b.size();        // so COT cua A == so HANG cua B
}

int main() {
    MaTran a = {{1,2,3},{4,5,6}};          // 2x3
    MaTran b = {{7,8,9},{10,11,12}};       // 2x3
    MaTran c = {{1,2},{3,4},{5,6}};        // 3x2

    cout << boolalpha;
    cout << "A(2x3) + B(2x3) duoc? " << congDuoc(a, b) << endl;   // true
    cout << "A(2x3) + C(3x2) duoc? " << congDuoc(a, c) << endl;   // false
    cout << "A(2x3) x C(3x2) duoc? " << nhanDuoc(a, c) << endl;   // true
    cout << "A(2x3) x B(2x3) duoc? " << nhanDuoc(a, b) << endl;   // false
    cout << "C(3x2) x A(2x3) duoc? " << nhanDuoc(c, a) << endl;   // true
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

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size(), p = b[0].size();
    MaTran c(n, vector<long long>(p, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c[i][j] += a[i][k] * b[k][j];
    return c;
}

void inMT(const MaTran& a, const string& nhan) {
    cout << nhan << endl;
    for (const auto& h : a) {
        for (long long x : h) cout << setw(6) << x;
        cout << endl;
    }
    cout << endl;
}

int main() {
    MaTran a = {{1, 2}, {3, 4}};
    MaTran b = {{5, 6}, {7, 8}};

    MaTran ab = nhan(a, b);
    MaTran ba = nhan(b, a);

    inMT(a, "A:");
    inMT(b, "B:");
    inMT(ab, "A x B:");
    inMT(ba, "B x A:");

    cout << "A x B == B x A ? " << boolalpha << (ab == ba) << endl;
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

**Nhưng phép nhân ma trận VẪN kết hợp:** `(A×B)×C = A×(B×C)` ✔

### Bài 6.

```cpp
#include <iostream>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size(), p = b[0].size();
    MaTran c(n, vector<long long>(p, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c[i][j] += a[i][k] * b[k][j];
    return c;
}

MaTran donVi(int n) {
    MaTran e(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) e[i][i] = 1;
    return e;
}

int main() {
    MaTran a = {{1,2,3},{4,5,6},{7,8,9}};
    MaTran I = donVi(3);

    cout << boolalpha;
    cout << "A x I == A ? " << (nhan(a, I) == a) << endl;    // true
    cout << "I x A == A ? " << (nhan(I, a) == a) << endl;    // true
    return 0;
}
```

**Ma trận đơn vị `I` là phần tử đơn vị của phép nhân ma trận** — giống vai trò của số 1 trong phép nhân số.

```
A × I = I × A = A
```

Đây cũng là **trường hợp hiếm hoi** mà phép nhân ma trận giao hoán.

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size(), p = b[0].size();
    MaTran c(n, vector<long long>(p, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c[i][j] += a[i][k] * b[k][j];
    return c;
}

MaTran donVi(int n) {
    MaTran e(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) e[i][i] = 1;
    return e;
}

// Luy thua CHAM: nhan k lan - O(k * n^3)
MaTran luyThua(MaTran a, int k) {
    MaTran kq = donVi(a.size());
    for (int i = 0; i < k; i++) kq = nhan(kq, a);
    return kq;
}

int main() {
    MaTran a = {{1, 1}, {1, 0}};

    for (int k = 1; k <= 5; k++) {
        MaTran kq = luyThua(a, k);
        cout << "A^" << k << " = [" << kq[0][0] << " " << kq[0][1]
             << "; " << kq[1][0] << " " << kq[1][1] << "]" << endl;
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

```cpp
#include <iostream>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;
const long long MOD = 1000000007;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size(), p = b[0].size();
    MaTran c(n, vector<long long>(p, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
    return c;
}

MaTran donVi(int n) {
    MaTran e(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) e[i][i] = 1;
    return e;
}

// Luy thua NHANH: O(log k * n^3)
MaTran luyThuaNhanh(MaTran a, long long k) {
    MaTran kq = donVi(a.size());
    while (k > 0) {
        if (k & 1) kq = nhan(kq, a);
        a = nhan(a, a);
        k >>= 1;
    }
    return kq;
}

int main() {
    MaTran a = {{1, 1}, {1, 0}};

    MaTran kq = luyThuaNhanh(a, 1000000);
    cout << "A^1000000 (mod 1e9+7):" << endl;
    cout << kq[0][0] << " " << kq[0][1] << endl;
    cout << kq[1][0] << " " << kq[1][1] << endl;
    return 0;
}
```

**So sánh số phép nhân ma trận:**

| k | Luỹ thừa chậm | Luỹ thừa nhanh |
|---|---|---|
| 10 | 10 | ~4 |
| 1.000 | 1.000 | ~10 |
| 10⁹ | 10⁹ (không khả thi) | **~30** |

Nguyên lý giống luỹ thừa nhị phân với số (bài [05-05](../05-05-cpp-ly-thuyet-so-va-toan-hoc.md) bài 11), chỉ thay phép nhân số bằng phép nhân ma trận.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;
const long long MOD = 1000000007;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size();
    MaTran c(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            for (int k = 0; k < n; k++)
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD;
    return c;
}

MaTran luyThuaNhanh(MaTran a, long long k) {
    int n = a.size();
    MaTran kq(n, vector<long long>(n, 0));
    for (int i = 0; i < n; i++) kq[i][i] = 1;

    while (k > 0) {
        if (k & 1) kq = nhan(kq, a);
        a = nhan(a, a);
        k >>= 1;
    }
    return kq;
}

long long fibonacci(long long n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    MaTran m = {{1, 1}, {1, 0}};
    MaTran kq = luyThuaNhanh(m, n - 1);
    return kq[0][0];
}

int main() {
    for (long long n : {1LL, 10LL, 50LL, 1000000LL, 1000000000000LL}) {
        cout << "F(" << n << ") = " << fibonacci(n) << endl;
    }
    return 0;
}
```

Output:

```
F(1) = 1
F(10) = 55
F(50) = 586268941        (da lay mod)
F(1000000) = 195023344
F(1000000000000) = 917056879
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

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    for (int n : {10, 50, 100, 200, 400}) {
        vector<vector<long long>> a(n, vector<long long>(n, 1));
        vector<vector<long long>> b(n, vector<long long>(n, 2));
        vector<vector<long long>> c(n, vector<long long>(n, 0));

        long long soPhepNhan = 0;

        auto t1 = high_resolution_clock::now();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++) {
                    c[i][j] += a[i][k] * b[k][j];
                    soPhepNhan++;
                }
        auto t2 = high_resolution_clock::now();

        cout << "n = " << n
             << ": " << soPhepNhan << " phep nhan"
             << " (n^3 = " << (long long)n*n*n << ")"
             << ", " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;
    }
    return 0;
}
```

Output:

```
n = 10: 1000 phep nhan (n^3 = 1000), 0 ms
n = 50: 125000 phep nhan (n^3 = 125000), 1 ms
n = 100: 1000000 phep nhan (n^3 = 1000000), 4 ms
n = 200: 8000000 phep nhan (n^3 = 8000000), 35 ms
n = 400: 64000000 phep nhan (n^3 = 64000000), 290 ms
```

**Kết luận: số phép nhân đúng bằng `n³`.**

Chú ý: khi `n` tăng **gấp đôi**, thời gian tăng **gấp 8** (2³).

💡 **Các thuật toán nhanh hơn O(n³):**

| Thuật toán | Độ phức tạp | Ghi chú |
|---|---|---|
| Ngây thơ | O(n³) | Đơn giản nhất |
| Strassen (1969) | O(n^2.807) | Thực tế nhanh hơn khi n > 100 |
| Coppersmith–Winograd | O(n^2.376) | Chỉ có ý nghĩa lý thuyết |
| Tốt nhất hiện nay | ~O(n^2.371) | Hằng số quá lớn, không dùng thực tế |

💡 **Tối ưu thực tế quan trọng nhất** — đổi thứ tự vòng lặp để thân thiện với cache:

```cpp
// Chậm: b[k][j] nhay lung tung trong bo nho
for (i) for (j) for (k) c[i][j] += a[i][k] * b[k][j];

// Nhanh hon 2-3 lan: truy cap b[k][j] tuan tu theo j
for (i) for (k) for (j) c[i][j] += a[i][k] * b[k][j];
```

### Bài 11.

```cpp
#include <iostream>
#include <vector>
using namespace std;

using MaTran = vector<vector<double>>;

// Dinh thuc 2x2: ad - bc
double dinhThuc2(const MaTran& a) {
    return a[0][0] * a[1][1] - a[0][1] * a[1][0];
}

// Dinh thuc 3x3: quy tac Sarrus
double dinhThuc3(const MaTran& a) {
    return a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
         - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
         + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]);
}

int main() {
    MaTran a = {{1, 2}, {3, 4}};
    cout << "det(2x2) = " << dinhThuc2(a) << endl;        // 1*4 - 2*3 = -2

    MaTran b = {{1,2,3}, {4,5,6}, {7,8,10}};
    cout << "det(3x3) = " << dinhThuc3(b) << endl;        // -3
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

💡 **Ý nghĩa của định thức:**
- `det = 0` → ma trận **suy biến** (không khả nghịch), hệ phương trình vô nghiệm hoặc vô số nghiệm
- `|det|` = **hệ số co giãn diện tích/thể tích** của phép biến đổi tuyến tính
- Dấu của `det` cho biết phép biến đổi có đảo hướng không

### Bài 12.

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

using MaTran = vector<vector<double>>;

double dinhThuc(MaTran a) {              // truyen BAN SAO vi se sua a
    int n = a.size();
    double det = 1.0;
    const double EPS = 1e-12;

    for (int i = 0; i < n; i++) {
        // Tim hang co phan tu tru lon nhat (pivoting - tang do chinh xac)
        int hangTot = i;
        for (int k = i + 1; k < n; k++)
            if (fabs(a[k][i]) > fabs(a[hangTot][i])) hangTot = k;

        if (fabs(a[hangTot][i]) < EPS) return 0.0;    // cot toan 0 -> det = 0

        if (hangTot != i) {
            swap(a[i], a[hangTot]);
            det = -det;                   // doi cho 2 hang -> doi dau dinh thuc
        }

        det *= a[i][i];

        // Khu cac hang phia duoi
        for (int k = i + 1; k < n; k++) {
            double heSo = a[k][i] / a[i][i];
            for (int j = i; j < n; j++)
                a[k][j] -= heSo * a[i][j];
        }
    }
    return det;
}

int main() {
    cout << fixed << setprecision(4);

    MaTran a = {{1, 2}, {3, 4}};
    cout << "det 2x2 = " << dinhThuc(a) << endl;             // -2

    MaTran b = {{1,2,3}, {4,5,6}, {7,8,10}};
    cout << "det 3x3 = " << dinhThuc(b) << endl;             // -3

    MaTran c = {{2,0,0,0}, {0,3,0,0}, {0,0,4,0}, {0,0,0,5}};
    cout << "det 4x4 (duong cheo) = " << dinhThuc(c) << endl;  // 120

    MaTran d = {{1,2}, {2,4}};             // 2 hang ti le -> suy bien
    cout << "det suy bien = " << dinhThuc(d) << endl;        // 0
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

### Bài 13.

```cpp
#include <iostream>
#include <vector>
using namespace std;

using MaTran = vector<vector<long long>>;

MaTran nhan(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size(), p = b[0].size();
    MaTran c(n, vector<long long>(p, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < p; j++)
            for (int k = 0; k < m; k++)
                c[i][j] += a[i][k] * b[k][j];
    return c;
}

MaTran cong(const MaTran& a, const MaTran& b) {
    int n = a.size(), m = a[0].size();
    MaTran c(n, vector<long long>(m));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) c[i][j] = a[i][j] + b[i][j];
    return c;
}

MaTran chuyenVi(const MaTran& a) {
    int n = a.size(), m = a[0].size();
    MaTran b(m, vector<long long>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) b[j][i] = a[i][j];
    return b;
}

int main() {
    MaTran a = {{1,2,3}, {4,5,6}};         // 2x3
    MaTran b = {{7,8,9}, {10,11,12}};      // 2x3
    MaTran c = {{1,2}, {3,4}, {5,6}};      // 3x2

    cout << boolalpha;

    // Tinh chat 1: (A + B)^T = A^T + B^T
    bool tc1 = (chuyenVi(cong(a, b)) == cong(chuyenVi(a), chuyenVi(b)));
    cout << "(A + B)^T == A^T + B^T ? " << tc1 << endl;      // true

    // Tinh chat 2: (A x C)^T = C^T x A^T   -- CHU Y THU TU BI DAO!
    bool tc2 = (chuyenVi(nhan(a, c)) == nhan(chuyenVi(c), chuyenVi(a)));
    cout << "(A x C)^T == C^T x A^T ? " << tc2 << endl;      // true

    // Kiem tra thu tu SAI
    // bool tc3 = (chuyenVi(nhan(a,c)) == nhan(chuyenVi(a), chuyenVi(c)));
    // -> Thuc ra khong nhan duoc: A^T la 3x2, C^T la 2x3 -> 3x2 x 2x3 = 3x3, sai kich thuoc

    // Tinh chat 3: (A^T)^T = A
    cout << "(A^T)^T == A ? " << (chuyenVi(chuyenVi(a)) == a) << endl;   // true
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

```cpp
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

using MaTran = vector<vector<double>>;

double det3(const MaTran& a) {
    return a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1])
         - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0])
         + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0]);
}

// Thay cot k cua a bang vector b
MaTran thayCot(MaTran a, const vector<double>& b, int k) {
    for (int i = 0; i < 3; i++) a[i][k] = b[i];
    return a;
}

int main() {
    cout << "Giai he:" << endl;
    cout << "  a1*x + b1*y + c1*z = d1" << endl;
    cout << "  a2*x + b2*y + c2*z = d2" << endl;
    cout << "  a3*x + b3*y + c3*z = d3" << endl;

    MaTran A(3, vector<double>(3));
    vector<double> B(3);

    for (int i = 0; i < 3; i++) {
        cout << "Nhap a" << i+1 << " b" << i+1 << " c" << i+1 << " d" << i+1 << ": ";
        cin >> A[i][0] >> A[i][1] >> A[i][2] >> B[i];
    }

    double D  = det3(A);
    double Dx = det3(thayCot(A, B, 0));
    double Dy = det3(thayCot(A, B, 1));
    double Dz = det3(thayCot(A, B, 2));

    const double EPS = 1e-9;
    cout << fixed << setprecision(4);
    cout << "\nD = " << D << ", Dx = " << Dx << ", Dy = " << Dy << ", Dz = " << Dz << endl;

    if (fabs(D) > EPS) {
        cout << "\nHe co nghiem duy nhat:" << endl;
        cout << "  x = " << Dx / D << endl;
        cout << "  y = " << Dy / D << endl;
        cout << "  z = " << Dz / D << endl;
    } else if (fabs(Dx) < EPS && fabs(Dy) < EPS && fabs(Dz) < EPS) {
        cout << "\nHe co VO SO nghiem" << endl;
    } else {
        cout << "\nHe VO NGHIEM" << endl;
    }
    return 0;
}
```

Ví dụ với hệ:

```
x + 2y + 3z = 14
2x + y + z  = 8
3x + 2y + z = 12
```

→ `x = 1, y = 2, z = 3`

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

### Bài 15.

**Bổ sung vào `matran.h`** (từ bài [08-03](../08-03-c-ma-tran-va-mang-2-chieu-c.md) bài 15):

```cpp
#pragma once
#include <vector>
#include <string>

using MaTran = std::vector<std::vector<long long>>;

// ---- Cac ham tu bai 08-03 ----
MaTran taoMaTran(int n, int m, long long giaTri = 0);
MaTran taoDonVi(int n);
void   inMaTran(const MaTran& a, const std::string& nhan = "", int doRong = 8);
MaTran chuyenVi(const MaTran& a);
bool   laVuong(const MaTran& a);
long long vet(const MaTran& a);

// ---- Cac ham moi ----

/** @brief Kiem tra 2 ma tran co cong duoc (cung kich thuoc). */
bool congDuoc(const MaTran& a, const MaTran& b);

/** @brief Kiem tra A x B co thuc hien duoc (cot A == hang B). */
bool nhanDuoc(const MaTran& a, const MaTran& b);

/** @brief Cong 2 ma tran. Tra ve ma tran rong neu khong hop le. */
MaTran cong(const MaTran& a, const MaTran& b);

/** @brief Tru 2 ma tran. */
MaTran tru(const MaTran& a, const MaTran& b);

/** @brief Nhan 2 ma tran. Do phuc tap O(n*m*p). */
MaTran nhan(const MaTran& a, const MaTran& b);

/**
 * @brief Tinh A^k bang luy thua nhi phan. Do phuc tap O(n^3 * log k).
 * @param mod Neu > 0, moi phep tinh se lay du cho mod.
 */
MaTran luyThua(MaTran a, long long k, long long mod = 0);

/** @brief Tinh dinh thuc bang khu Gauss. Do phuc tap O(n^3). */
double dinhThuc(const MaTran& a);
```

**Bổ sung vào `matran.cpp`:**

```cpp
#include "matran.h"
#include <cmath>
#include <algorithm>

bool congDuoc(const MaTran& a, const MaTran& b) {
    if (a.empty() || b.empty()) return false;
    return a.size() == b.size() && a[0].size() == b[0].size();
}

bool nhanDuoc(const MaTran& a, const MaTran& b) {
    if (a.empty() || b.empty()) return false;
    return a[0].size() == b.size();
}

MaTran cong(const MaTran& a, const MaTran& b) {
    if (!congDuoc(a, b)) return {};
    int n = a.size(), m = a[0].size();
    MaTran c = taoMaTran(n, m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) c[i][j] = a[i][j] + b[i][j];
    return c;
}

MaTran tru(const MaTran& a, const MaTran& b) {
    if (!congDuoc(a, b)) return {};
    int n = a.size(), m = a[0].size();
    MaTran c = taoMaTran(n, m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) c[i][j] = a[i][j] - b[i][j];
    return c;
}

MaTran nhan(const MaTran& a, const MaTran& b) {
    if (!nhanDuoc(a, b)) return {};
    int n = a.size(), m = a[0].size(), p = b[0].size();
    MaTran c = taoMaTran(n, p, 0);
    // Thu tu i-k-j: than thien voi CPU cache hon i-j-k
    for (int i = 0; i < n; i++)
        for (int k = 0; k < m; k++) {
            long long tam = a[i][k];
            for (int j = 0; j < p; j++) c[i][j] += tam * b[k][j];
        }
    return c;
}

MaTran luyThua(MaTran a, long long k, long long mod) {
    if (!laVuong(a) || k < 0) return {};
    int n = a.size();
    MaTran kq = taoDonVi(n);

    auto nhanMod = [&](const MaTran& x, const MaTran& y) {
        MaTran z = taoMaTran(n, n, 0);
        for (int i = 0; i < n; i++)
            for (int p = 0; p < n; p++) {
                long long t = x[i][p];
                if (t == 0) continue;
                for (int j = 0; j < n; j++) {
                    z[i][j] += t * y[p][j];
                    if (mod > 0) z[i][j] %= mod;
                }
            }
        return z;
    };

    while (k > 0) {
        if (k & 1) kq = nhanMod(kq, a);
        a = nhanMod(a, a);
        k >>= 1;
    }
    return kq;
}

double dinhThuc(const MaTran& a0) {
    if (!laVuong(a0)) return 0.0;
    int n = a0.size();

    std::vector<std::vector<double>> a(n, std::vector<double>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) a[i][j] = (double)a0[i][j];

    double det = 1.0;
    const double EPS = 1e-12;

    for (int i = 0; i < n; i++) {
        int tot = i;
        for (int k = i + 1; k < n; k++)
            if (std::fabs(a[k][i]) > std::fabs(a[tot][i])) tot = k;

        if (std::fabs(a[tot][i]) < EPS) return 0.0;
        if (tot != i) { std::swap(a[i], a[tot]); det = -det; }

        det *= a[i][i];
        for (int k = i + 1; k < n; k++) {
            double h = a[k][i] / a[i][i];
            for (int j = i; j < n; j++) a[k][j] -= h * a[i][j];
        }
    }
    return det;
}
```

**Kiểm thử `main.cpp`:**

```cpp
#include <iostream>
#include "matran.h"
using namespace std;

int main() {
    MaTran a = {{1,2},{3,4}};
    MaTran b = {{5,6},{7,8}};

    inMaTran(a, "A:");
    inMaTran(b, "B:");
    inMaTran(cong(a, b), "A + B:");
    inMaTran(tru(a, b),  "A - B:");
    inMaTran(nhan(a, b), "A x B:");
    inMaTran(nhan(b, a), "B x A (khac A x B!):");
    inMaTran(luyThua(a, 5), "A^5:");
    inMaTran(chuyenVi(a), "A^T:");

    cout << "det(A) = " << dinhThuc(a) << endl;         // -2
    cout << "vet(A) = " << vet(a)      << endl;         // 5

    // Fibonacci bang luy thua ma tran
    MaTran fib = {{1,1},{1,0}};
    cout << "\nF(50) = " << luyThua(fib, 49)[0][0] << endl;
    cout << "F(10^12) mod 1e9+7 = "
         << luyThua(fib, 999999999999LL, 1000000007)[0][0] << endl;

    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall -O2 main.cpp matran.cpp -o matran
```
