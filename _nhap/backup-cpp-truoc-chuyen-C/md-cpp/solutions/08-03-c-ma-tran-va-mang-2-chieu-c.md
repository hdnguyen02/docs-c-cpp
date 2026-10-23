# Lời giải — [C++]. Ma Trận Và Mảng 2 Chiều C++

[← Quay lại bài học](../08-03-c-ma-tran-va-mang-2-chieu-c.md)

---

### Bài 1.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int a[100][100] = {};
    for (int i = 0; i < n; i++) a[i][i] = 1;

    cout << "Ma tran don vi " << n << "x" << n << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(4) << a[i][j];
        cout << endl;
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

### Bài 2.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int a[100][100] = {};
    cout << "Nhap " << n << " gia tri tren duong cheo: ";
    for (int i = 0; i < n; i++) cin >> a[i][i];

    cout << "\nMa tran duong cheo:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 **Ma trận đường chéo** có tính chất đặc biệt: nhân 2 ma trận đường chéo chỉ cần nhân từng cặp phần tử trên đường chéo — O(n) thay vì O(n³).

### Bài 3.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a[100][100], b[100][100], n, m;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    // Chuyen vi: b[j][i] = a[i][j]
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            b[j][i] = a[i][j];

    cout << "\nMa tran goc (" << n << "x" << m << "):" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }

    cout << "\nMa tran chuyen vi (" << m << "x" << n << "):" << endl;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << b[i][j];
        cout << endl;
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

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    // Chuyen vi TAI CHO: chi doi cho nua tren voi nua duoi
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)      // j bat dau tu i+1
            swap(a[i][j], a[j][i]);

    cout << "\nSau khi chuyen vi tai cho:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << a[i][j];
        cout << endl;
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

### Bài 5.

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

void inMT(const char* nhan, int a[][100], int n) {
    cout << nhan << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    cout << endl;
}

int main() {
    int n = 3;
    int a[100][100] = {{1,2,3},{4,5,6},{7,8,9}};

    inMT("Ban dau:", a, n);

    // XOAY 90 DO THEO CHIEU KIM DONG HO = CHUYEN VI + LAT NGANG
    // Buoc 1: chuyen vi
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            swap(a[i][j], a[j][i]);

    // Buoc 2: lat theo chieu ngang (dao nguoc tung hang)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n / 2; j++)
            swap(a[i][j], a[i][n - 1 - j]);

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

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

const int N = 100;

void chuyenVi(int a[][N], int n) {
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) swap(a[i][j], a[j][i]);
}

void latNgang(int a[][N], int n) {         // dao nguoc tung HANG
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n / 2; j++) swap(a[i][j], a[i][n-1-j]);
}

void latDoc(int a[][N], int n) {           // dao nguoc tung COT
    for (int i = 0; i < n / 2; i++)
        for (int j = 0; j < n; j++) swap(a[i][j], a[n-1-i][j]);
}

void xoay90(int a[][N], int n)  { chuyenVi(a, n); latNgang(a, n); }
void xoay270(int a[][N], int n) { chuyenVi(a, n); latDoc(a, n); }
void xoay180(int a[][N], int n) { latNgang(a, n); latDoc(a, n); }

void inMT(const char* nhan, int a[][N], int n) {
    cout << nhan << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    cout << endl;
}

int main() {
    int n = 3;
    int goc[N][N] = {{1,2,3},{4,5,6},{7,8,9}};
    int a[N][N];

    auto reset = [&]() {
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++) a[i][j] = goc[i][j];
    };

    reset(); inMT("Ban dau:", a, n);
    reset(); xoay90(a, n);  inMT("Xoay 90 do (kim dong ho):", a, n);
    reset(); xoay180(a, n); inMT("Xoay 180 do:", a, n);
    reset(); xoay270(a, n); inMT("Xoay 270 do (= 90 nguoc kim):", a, n);

    return 0;
}
```

**Bảng tổng hợp:**

| Phép xoay | Cách thực hiện | Công thức trực tiếp |
|---|---|---|
| 90° cùng kim | Chuyển vị + Lật ngang | `b[j][n-1-i] = a[i][j]` |
| 180° | Lật ngang + Lật dọc | `b[n-1-i][n-1-j] = a[i][j]` |
| 270° (= 90° ngược) | Chuyển vị + Lật dọc | `b[n-1-j][i] = a[i][j]` |

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int n = 3, m = 4;
    int a[100][100] = {{1,2,3,4},{5,6,7,8},{9,10,11,12}};

    auto inMT = [&](const char* nhan) {
        cout << nhan << endl;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
            cout << endl;
        }
        cout << endl;
    };

    inMT("Ban dau:");

    // LAT NGANG: dao nguoc tung hang (trai <-> phai)
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m / 2; j++)
            swap(a[i][j], a[i][m - 1 - j]);
    inMT("Lat NGANG (guong trai-phai):");

    // LAT DOC: dao nguoc thu tu cac hang (tren <-> duoi)
    for (int i = 0; i < n / 2; i++)
        for (int j = 0; j < m; j++)
            swap(a[i][j], a[n - 1 - i][j]);
    inMT("Lat DOC (guong tren-duoi):");

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

```cpp
#include <iostream>
using namespace std;

long long vet(int a[][100], int n) {
    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i][i];
    return tong;
}

int main() {
    int n;
    cin >> n;
    int a[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    cout << "Vet (trace) = " << vet(a, n) << endl;
    return 0;
}
```

💡 **Vết (trace)** là một bất biến quan trọng trong đại số tuyến tính:
- `trace(A + B) = trace(A) + trace(B)`
- `trace(AB) = trace(BA)` (dù `AB ≠ BA`)
- Vết bằng **tổng các giá trị riêng** của ma trận

### Bài 9.

```cpp
#include <iostream>
using namespace std;

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

    cout << boolalpha;
    cout << "a == b? " << bangNhau(a, b, n, m) << endl;    // true
    cout << "a == c? " << bangNhau(a, c, n, m) << endl;    // false
    return 0;
}
```

⚠️ **Hai ma trận chỉ bằng nhau khi CÙNG kích thước** và mọi phần tử tương ứng bằng nhau. Trong chương trình thật nên kiểm tra kích thước trước.

💡 Với `vector<vector<int>>` thì đơn giản: `if (a == b)` — `vector` đã nạp chồng `operator==`.

### Bài 10.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n = 3, m = 3;
    int a[100][100] = {{1,2,3},{4,5,6},{7,8,9}};
    int k;

    cout << "Nhap so vo huong k: ";
    cin >> k;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] *= k;

    cout << "Ma tran sau khi nhan " << k << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(6) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 Nhân vô hướng đơn giản hơn nhiều so với nhân 2 ma trận: chỉ O(n×m) thay vì O(n³).

### Bài 11.

```cpp
#include <iostream>
#include <iomanip>
#include <random>
#include <chrono>
using namespace std;

int main() {
    int n, m, a, b;
    cout << "Nhap so hang, cot: "; cin >> n >> m;
    cout << "Nhap khoang gia tri [a, b]: "; cin >> a >> b;

    if (a > b) swap(a, b);

    unsigned seed = chrono::steady_clock::now().time_since_epoch().count();
    mt19937 rng(seed);
    uniform_int_distribution<int> phanBo(a, b);

    int mt[100][100];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mt[i][j] = phanBo(rng);

    cout << "\nMa tran ngau nhien:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(6) << mt[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 `mt19937` (Mersenne Twister) cho chất lượng ngẫu nhiên tốt hơn nhiều so với `rand()`. Cách cũ:

```cpp
srand(time(0));
mt[i][j] = rand() % (b - a + 1) + a;      // phan bo khong deu hoan toan
```

### Bài 12.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap so dong: ";
    cin >> n;

    long long pascal[35][35] = {};

    for (int i = 0; i < n; i++) {
        pascal[i][0] = 1;                                    // cot dau luon = 1
        for (int j = 1; j <= i; j++) {
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];  // cong 2 so phia tren
        }
    }

    // In dang tam giac can
    cout << "\nTam giac Pascal:" << endl;
    for (int i = 0; i < n; i++) {
        cout << setw((n - i) * 3) << "";
        for (int j = 0; j <= i; j++) cout << setw(6) << pascal[i][j];
        cout << endl;
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

⚠️ Dùng `long long` — `C(60,30)` đã vượt `int`.

### Bài 13.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int a[100][100];
    cout << "Nhap ma tran " << n << "x" << n << ":" << endl;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

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

    cout << "\nTong chuan = " << tongChuan << endl;
    cout << "Ma tran " << (laMaPhuong ? "LA" : "KHONG phai") << " ma phuong" << endl;
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

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n (phai LE): ";
    cin >> n;

    if (n % 2 == 0) {
        cout << "Phuong phap Siamese chi ap dung cho n LE!" << endl;
        return 1;
    }

    int a[100][100] = {};

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

    cout << "\nMa phuong bac " << n << ":" << endl;
    for (int r = 0; r < n; r++) {
        for (int c = 0; c < n; c++) cout << setw(5) << a[r][c];
        cout << endl;
    }

    cout << "\nTong chuan = " << n * (n * n + 1) / 2 << endl;
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

💡 Phép `(i - 1 + n) % n` xử lý việc "vòng qua biên" — cộng `n` trước để tránh số âm.

⚠️ Chỉ áp dụng cho `n` **lẻ**. Ma phương bậc chẵn cần phương pháp khác (LUX, Strachey).

### Bài 15.

**File `matran.h`:**

```cpp
#pragma once
#include <vector>

using MaTran = std::vector<std::vector<int>>;

/** @brief Tao ma tran n x m voi gia tri khoi tao. */
MaTran taoMaTran(int n, int m, int giaTri = 0);

/** @brief Tao ma tran don vi n x n. */
MaTran taoDonVi(int n);

/** @brief In ma tran ra man hinh voi do rong cot tuy chon. */
void inMaTran(const MaTran& a, const std::string& nhan = "", int doRong = 6);

/** @brief Tra ve ma tran chuyen vi (n x m -> m x n). */
MaTran chuyenVi(const MaTran& a);

/** @brief Xoay ma tran VUONG 90 do theo chieu kim dong ho. */
MaTran xoay90(const MaTran& a);

/** @brief So sanh 2 ma tran co bang nhau khong. */
bool bangNhau(const MaTran& a, const MaTran& b);

/** @brief Vet (trace) - tong duong cheo chinh. Ma tran phai vuong. */
long long vet(const MaTran& a);

/** @brief Nhan ma tran voi so vo huong. */
MaTran nhanVoHuong(const MaTran& a, int k);

/** @brief Kiem tra co phai ma tran vuong. */
bool laVuong(const MaTran& a);
```

**File `matran.cpp`:**

```cpp
#include "matran.h"
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

MaTran taoMaTran(int n, int m, int giaTri) {
    return MaTran(n, vector<int>(m, giaTri));
}

MaTran taoDonVi(int n) {
    MaTran a = taoMaTran(n, n, 0);
    for (int i = 0; i < n; i++) a[i][i] = 1;
    return a;
}

void inMaTran(const MaTran& a, const string& nhan, int doRong) {
    if (!nhan.empty()) cout << nhan << endl;
    for (const auto& hang : a) {
        for (int x : hang) cout << setw(doRong) << x;
        cout << endl;
    }
    cout << endl;
}

MaTran chuyenVi(const MaTran& a) {
    if (a.empty()) return {};
    int n = a.size(), m = a[0].size();
    MaTran b = taoMaTran(m, n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            b[j][i] = a[i][j];
    return b;
}

MaTran xoay90(const MaTran& a) {
    if (!laVuong(a)) return a;
    int n = a.size();
    MaTran b = taoMaTran(n, n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            b[j][n - 1 - i] = a[i][j];
    return b;
}

bool bangNhau(const MaTran& a, const MaTran& b) {
    return a == b;                    // vector da nap chong operator==
}

long long vet(const MaTran& a) {
    if (!laVuong(a)) return 0;
    long long tong = 0;
    for (size_t i = 0; i < a.size(); i++) tong += a[i][i];
    return tong;
}

MaTran nhanVoHuong(const MaTran& a, int k) {
    MaTran b = a;
    for (auto& hang : b)
        for (int& x : hang) x *= k;
    return b;
}

bool laVuong(const MaTran& a) {
    return !a.empty() && a.size() == a[0].size();
}
```

**File `main.cpp`:**

```cpp
#include <iostream>
#include "matran.h"
using namespace std;

int main() {
    MaTran a = {{1,2,3}, {4,5,6}, {7,8,9}};

    inMaTran(a, "Ma tran goc:");
    inMaTran(chuyenVi(a), "Chuyen vi:");
    inMaTran(xoay90(a), "Xoay 90 do:");
    inMaTran(nhanVoHuong(a, 2), "Nhan voi 2:");
    inMaTran(taoDonVi(4), "Ma tran don vi 4x4:");

    cout << "Vet cua a     = " << vet(a) << endl;              // 15
    cout << "a == a?       " << boolalpha << bangNhau(a, a) << endl;
    cout << "a la vuong?   " << laVuong(a) << endl;

    MaTran b = {{1,2,3}, {4,5,6}};
    cout << "b la vuong?   " << laVuong(b) << endl;
    inMaTran(chuyenVi(b), "Chuyen vi cua b (2x3 -> 3x2):");

    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp matran.cpp -o matran
./matran
```

**Các điểm thiết kế đáng học:**

1. **`using MaTran = vector<vector<int>>`** — bí danh kiểu làm code ngắn và rõ hơn nhiều
2. **`const MaTran&`** cho tham số chỉ đọc — không sao chép, an toàn
3. **Trả về `MaTran`** thay vì sửa tại chỗ — hàm thuần khiết, dễ kiểm thử, dễ nối chuỗi: `xoay90(chuyenVi(a))`
4. **Kiểm tra `laVuong` trước** các phép chỉ áp dụng cho ma trận vuông
5. **Đối số mặc định** (`giaTri = 0`, `nhan = ""`) làm API dễ dùng

💡 Hãy giữ thư viện này và mở rộng thêm ở bài [08-04](../08-04-c-cong-tru-nhan-2-ma-tran-c.md) (cộng, trừ, nhân ma trận).
