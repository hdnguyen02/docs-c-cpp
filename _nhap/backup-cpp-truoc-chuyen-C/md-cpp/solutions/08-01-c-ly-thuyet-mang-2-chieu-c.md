# Lời giải — [C++]. Lý Thuyết Mảng 2 Chiều C++

[← Quay lại bài học](../08-01-c-ly-thuyet-mang-2-chieu-c.md)

> **Khai báo:** `int a[n][m]` — `n` hàng, `m` cột. Truy cập `a[i][j]` với `i` là **hàng**, `j` là **cột**.

---

### Bài 1.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

const int MAX = 100;

int main() {
    int a[MAX][MAX], n, m;

    cout << "Nhap so hang va so cot: ";
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            cout << "  a[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }

    cout << "\nMa tran " << n << " x " << m << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(6) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 **Mẫu chuẩn duyệt ma trận:** vòng ngoài cho **hàng** (`i`), vòng trong cho **cột** (`j`).

### Bài 2.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    long long tong = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) tong += a[i][j];

    cout << "Tong       = " << tong << endl;
    cout << fixed << setprecision(4);
    cout << "Trung binh = " << (double)tong / (n * m) << endl;
    return 0;
}
```

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int maxI = 0, maxJ = 0, minI = 0, minJ = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (a[i][j] > a[maxI][maxJ]) { maxI = i; maxJ = j; }
            if (a[i][j] < a[minI][minJ]) { minI = i; minJ = j; }
        }

    cout << "Lon nhat  = " << a[maxI][maxJ]
         << " tai (" << maxI << ", " << maxJ << ")" << endl;
    cout << "Nho nhat  = " << a[minI][minJ]
         << " tai (" << minI << ", " << minJ << ")" << endl;
    return 0;
}
```

⚠️ Khởi tạo bằng **vị trí (0,0)**, không phải bằng 0 — nếu ma trận toàn số âm, khởi tạo `max = 0` sẽ sai.

### Bài 4.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    long long tongHang[100] = {}, tongCot[100] = {};

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            tongHang[i] += a[i][j];
            tongCot[j]  += a[i][j];
        }

    // In ma tran kem tong hang
    cout << "\nMa tran va tong:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(6) << a[i][j];
        cout << "  |" << setw(7) << tongHang[i] << endl;
    }

    // Duong ke
    for (int j = 0; j < m; j++) cout << "------";
    cout << "--+" << endl;

    // Dong tong cot
    for (int j = 0; j < m; j++) cout << setw(6) << tongCot[j];
    cout << endl;
    return 0;
}
```

Ví dụ:

```
     1     2     3  |     6
     4     5     6  |    15
     7     8     9  |    24
------------------+
    12    15    18
```

💡 **Tính cả 2 tổng trong MỘT lần duyệt** — không cần duyệt 2 lần.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int duong = 0, am = 0, khong = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if      (a[i][j] > 0) duong++;
            else if (a[i][j] < 0) am++;
            else                  khong++;
        }

    cout << "So duong  : " << duong << endl;
    cout << "So am     : " << am    << endl;
    cout << "So bang 0 : " << khong << endl;
    return 0;
}
```

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "Cac phan tu o vien: ";
    long long tongVien = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (i == 0 || i == n - 1 || j == 0 || j == m - 1) {
                cout << a[i][j] << " ";
                tongVien += a[i][j];
            }
        }
    cout << "\nTong vien = " << tongVien << endl;

    // In truc quan: vien giu nguyen, ben trong thay bang dau .
    cout << "\nHinh anh truc quan:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i == 0 || i == n - 1 || j == 0 || j == m - 1)
                cout << setw(5) << a[i][j];
            else
                cout << setw(5) << ".";
        }
        cout << endl;
    }
    return 0;
}
```

**Điều kiện viền:** `i == 0` (hàng đầu) **hoặc** `i == n-1` (hàng cuối) **hoặc** `j == 0` (cột đầu) **hoặc** `j == m-1` (cột cuối).

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

void inMT(const char* nhan, int a[][4], int n) {
    cout << nhan << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    cout << endl;
}

int main() {
    // ① Khoi tao day du
    int a[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };

    // ② Khoi tao THIEU -> phan con lai tu dong = 0
    int b[3][4] = {
        {1, 2},
        {3}
    };

    // ③ Khoi tao TOAN 0
    int c[3][4] = {};

    // ④ Khoi tao phang (khong co ngoac trong) - van hop le
    int d[3][4] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

    inMT("① Day du   ", a, 3);
    inMT("② Thieu    ", b, 3);
    inMT("③ Toan 0   ", c, 3);
    inMT("④ Phang    ", d, 3);
    return 0;
}
```

Output của ② :

```
② Thieu    :
    1    2    0    0
    3    0    0    0
    0    0    0    0
```

⚠️ **Không khởi tạo gì cả** (`int e[3][4];`) → toàn giá trị **rác**.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[3][4];

    cout << "Dia chi tung phan tu:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << "a[" << i << "][" << j << "] = " << &a[i][j];
            if (!(i == 0 && j == 0))
                cout << "  (+" << (char*)&a[i][j] - (char*)&a[0][0] << " byte)";
            cout << endl;
        }
    }

    cout << "\nsizeof(a)    = " << sizeof(a)    << " byte" << endl;   // 48
    cout << "sizeof(a[0]) = " << sizeof(a[0]) << " byte" << endl;   // 16
    cout << "sizeof(a[0][0]) = " << sizeof(a[0][0]) << " byte" << endl; // 4

    // Truy cap nhu mang 1 chieu
    int *p = &a[0][0];
    for (int i = 0; i < 12; i++) p[i] = i;

    cout << "\nMa tran sau khi dien qua con tro 1 chieu:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) cout << a[i][j] << "\t";
        cout << endl;
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

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

const int SO_COT = 4;

// PHAI chi ro so COT (co the bo so hang)
void inMT(int a[][SO_COT], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < SO_COT; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
}

// Cach 2: dung con tro toi mang
void inMT2(int (*a)[SO_COT], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < SO_COT; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
}

int main() {
    int a[3][SO_COT] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    inMT(a, 3);
    cout << endl;
    inMT2(a, 3);
    return 0;
}
```

**Vì sao PHẢI chỉ rõ số cột:**

Compiler cần biết số cột để tính địa chỉ của `a[i][j]`:

```
dia chi a[i][j] = dia chi goc + (i * SO_COT + j) * sizeof(int)
                                     ^^^^^^^
                            BAT BUOC phai biet
```

Nếu viết `void f(int a[][])` → lỗi:

```
error: declaration of 'a' as multidimensional array must have bounds
       for all dimensions except the first
```

**Số hàng thì không cần** vì nó không tham gia vào công thức tính địa chỉ.

⚠️ **Hạn chế lớn:** hàm chỉ dùng được với ma trận có **đúng** số cột đó. Muốn tổng quát, phải dùng:

```cpp
// ① Template (C++)
template <size_t N, size_t M>
void inMT(int (&a)[N][M]) { ... }

// ② Mang 1 chieu + tu tinh chi so
void inMT(int *a, int n, int m) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cout << a[i * m + j];
}

// ③ vector<vector<int>> - DE NHAT
void inMT(const vector<vector<int>>& a) {
    for (const auto& hang : a) { ... }
}
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

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

    cout << "Hang " << hangMax << " co tong lon nhat = " << tongHangMax << endl;
    cout << "Cot  " << cotMin  << " co tong nho nhat = " << tongCotMin  << endl;
    return 0;
}
```

Nhớ `#include <climits>` cho `LLONG_MIN`/`LLONG_MAX`.

### Bài 11.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const int N = 3, M = 4;
    int a[N][M] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    int b[N * M];

    // ① Ma tran -> mang 1 chieu
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            b[i * M + j] = a[i][j];          // CONG THUC CHUYEN DOI

    cout << "Mang 1 chieu: ";
    for (int k = 0; k < N * M; k++) cout << b[k] << " ";
    cout << endl;

    // ② Mang 1 chieu -> ma tran
    int c[N][M];
    for (int k = 0; k < N * M; k++) {
        int i = k / M;                        // CHI SO HANG
        int j = k % M;                        // CHI SO COT
        c[i][j] = b[k] * 10;
    }

    cout << "\nMa tran khoi phuc (x10):" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) cout << setw(5) << c[i][j];
        cout << endl;
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

💡 **Ứng dụng:** lưu ma trận trong một khối nhớ liền, truyền hàm dễ hơn, và nhanh hơn (tốt cho cache).

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n;
    cout << "Nhap kich thuoc ma tran vuong: ";
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    bool laDonVi = true;
    for (int i = 0; i < n && laDonVi; i++) {
        for (int j = 0; j < n; j++) {
            int canCo = (i == j) ? 1 : 0;      // duong cheo chinh = 1, con lai = 0
            if (a[i][j] != canCo) { laDonVi = false; break; }
        }
    }

    cout << "Ma tran " << (laDonVi ? "LA" : "KHONG phai") << " ma tran don vi" << endl;
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

```cpp
#include <iostream>
using namespace std;

bool laNguyenTo(int n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int dem = 0;
    long long tong = 0;

    cout << "Cac so nguyen to: ";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (laNguyenTo(a[i][j])) {
                cout << a[i][j] << "(" << i << "," << j << ") ";
                dem++;
                tong += a[i][j];
            }

    cout << "\nSo luong: " << dem << ", tong = " << tong << endl;
    return 0;
}
```

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "\nDuyet theo HANG: ";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cout << a[i][j] << " ";
    cout << endl;

    cout << "Duyet theo COT: ";
    for (int j = 0; j < m; j++)             // COT o vong NGOAI
        for (int i = 0; i < n; i++)         // HANG o vong TRONG
            cout << a[i][j] << " ";
    cout << endl;
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

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    int n = 3, m = 4;

    // ========== ① MANG TINH 2 CHIEU ==========
    int a[3][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    cout << "① Mang tinh:" << endl;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }

    // ========== ② int** DONG ==========
    int **b = new int*[n];
    for (int i = 0; i < n; i++) b[i] = new int[m];
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) b[i][j] = (i + 1) * (j + 1);

    cout << "\n② int** dong:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << b[i][j];
        cout << endl;
    }
    for (int i = 0; i < n; i++) delete[] b[i];
    delete[] b;

    // ========== ③ vector<vector<int>> ==========
    vector<vector<int>> c(n, vector<int>(m, 0));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) c[i][j] = i * m + j;

    cout << "\n③ vector<vector<int>>:" << endl;
    for (const auto& hang : c) {
        for (int x : hang) cout << setw(5) << x;
        cout << endl;
    }

    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Mảng tĩnh `int a[3][4]` | `int**` động | `vector<vector<int>>` |
|---|---|---|---|
| **Kích thước** | ⚠️ Cố định lúc biên dịch | ✅ Lúc chạy | ✅ Lúc chạy, đổi được |
| **Bộ nhớ** | Stack (giới hạn 1–8 MB) | Heap | Heap |
| **Liên tục trong bộ nhớ** | ✅ Có (nhanh nhất) | ❌ Không (mỗi hàng một chỗ) | ❌ Không |
| **Tốc độ truy cập** | Nhanh nhất | Chậm hơn (2 lần giải tham chiếu) | Gần bằng `int**` |
| **Cấp phát/giải phóng** | Tự động | ⚠️ Thủ công, dễ rò rỉ | ✅ Tự động |
| **Truyền vào hàm** | ⚠️ Phải cố định số cột | ✅ Linh hoạt | ✅ Linh hoạt nhất |
| **Biết kích thước** | ❌ Phải truyền kèm | ❌ Phải truyền kèm | ✅ `.size()` |
| **Hàng có độ dài khác nhau** | ❌ Không | ✅ Được | ✅ Được |
| **An toàn** | ⚠️ Không kiểm tra biên | ⚠️ Nguy hiểm nhất | ✅ An toàn nhất (`.at()`) |

**✅ Khuyến nghị:**

| Tình huống | Nên dùng |
|---|---|
| Kích thước nhỏ, biết trước, cần tốc độ tối đa | **Mảng tĩnh** |
| Lập trình thi đấu | **Mảng tĩnh toàn cục** (`int a[1005][1005];` ngoài `main`) |
| Code ứng dụng thật | **`vector<vector<int>>`** |
| Cần tốc độ + kích thước động | **Mảng 1 chiều `vector<int>` cỡ `n*m`**, truy cập `v[i*m+j]` |
| Học C, làm việc với API C | `int**` |

💡 **Mẹo tối ưu tốt nhất** — kết hợp ưu điểm của cả hai:

```cpp
vector<int> mt(n * m);                    // 1 khoi lien tuc -> cache tot
auto at = [&](int i, int j) -> int& { return mt[i * m + j]; };

at(1, 2) = 99;                            // dung nhu ma tran
cout << at(1, 2);
```

Cách này vừa nhanh như mảng tĩnh, vừa linh hoạt như `vector`.
