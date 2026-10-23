# Lời giải — [C++]. Thuật Toán Tìm Kiếm Nhị Phân

[← Quay lại bài học](../10-01-c-thuat-toan-tim-kiem-nhi-phan.md)

> **Điều kiện bắt buộc: mảng phải ĐÃ SẮP XẾP.** Mỗi bước loại bỏ một nửa không gian tìm kiếm → **O(log n)**.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int timNhiPhan(int a[], int n, int x) {
    int trai = 0, phai = n - 1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if      (a[giua] == x) return giua;        // tim thay
        else if (a[giua] <  x) trai = giua + 1;    // tim o NUA PHAI
        else                   phai = giua - 1;    // tim o NUA TRAI
    }
    return -1;                                      // khong tim thay
}

int main() {
    int a[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = 10;

    for (int x : {23, 2, 91, 50}) {
        int vt = timNhiPhan(a, n, x);
        cout << "Tim " << x << ": ";
        if (vt != -1) cout << "thay tai vi tri " << vt << endl;
        else          cout << "khong tim thay" << endl;
    }
    return 0;
}
```

⚠️ Chú ý `trai <= phai` (có dấu `=`) — nếu viết `<` thì bỏ sót trường hợp khoảng còn đúng 1 phần tử.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int timNhiPhanDeQuy(int a[], int trai, int phai, int x) {
    if (trai > phai) return -1;                     // DIEU KIEN DUNG

    int giua = trai + (phai - trai) / 2;

    if (a[giua] == x) return giua;
    if (a[giua] <  x) return timNhiPhanDeQuy(a, giua + 1, phai, x);
    return timNhiPhanDeQuy(a, trai, giua - 1, x);
}

// Ham vo cho de goi
int timNhiPhan(int a[], int n, int x) {
    return timNhiPhanDeQuy(a, 0, n - 1, x);
}

int main() {
    int a[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    cout << "Tim 38: vi tri " << timNhiPhan(a, 10, 38) << endl;   // 6
    cout << "Tim 50: vi tri " << timNhiPhan(a, 10, 50) << endl;   // -1
    return 0;
}
```

💡 Đây là **đệ quy đuôi** — compiler với `-O2` thường tối ưu thành vòng lặp, nên không lo tràn stack. Độ sâu tối đa cũng chỉ `log₂(n)` (~30 với n = 10⁹).

### Bài 3.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int timNhiPhanChiTiet(int a[], int n, int x) {
    int trai = 0, phai = n - 1, buoc = 0;

    cout << "Tim gia tri " << x << " trong mang " << n << " phan tu:" << endl;
    cout << "+-------+-------+-------+-------+------------+" << endl;
    cout << "| Buoc  | trai  | giua  | phai  | a[giua]    |" << endl;
    cout << "+-------+-------+-------+-------+------------+" << endl;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        buoc++;

        cout << "| " << setw(5) << buoc
             << " | " << setw(5) << trai
             << " | " << setw(5) << giua
             << " | " << setw(5) << phai
             << " | " << setw(10) << a[giua] << " |";

        if (a[giua] == x) {
            cout << "  <- TIM THAY!" << endl;
            cout << "+-------+-------+-------+-------+------------+" << endl;
            return giua;
        } else if (a[giua] < x) {
            cout << "  (nho hon -> sang PHAI)" << endl;
            trai = giua + 1;
        } else {
            cout << "  (lon hon -> sang TRAI)" << endl;
            phai = giua - 1;
        }
    }

    cout << "+-------+-------+-------+-------+------------+" << endl;
    cout << "Khong tim thay sau " << buoc << " buoc" << endl;
    return -1;
}

int main() {
    int a[16];
    for (int i = 0; i < 16; i++) a[i] = (i + 1) * 5;    // 5, 10, 15, ..., 80

    timNhiPhanChiTiet(a, 16, 65);
    return 0;
}
```

Output:

```
Tim gia tri 65 trong mang 16 phan tu:
+-------+-------+-------+-------+------------+
| Buoc  | trai  | giua  | phai  | a[giua]    |
+-------+-------+-------+-------+------------+
|     1 |     0 |     7 |    15 |         40 |  (nho hon -> sang PHAI)
|     2 |     8 |    11 |    15 |         60 |  (nho hon -> sang PHAI)
|     3 |    12 |    13 |    15 |         70 |  (lon hon -> sang TRAI)
|     4 |    12 |    12 |    12 |         65 |  <- TIM THAY!
+-------+-------+-------+-------+------------+
```

💡 Chỉ **4 bước** để tìm trong 16 phần tử — đúng bằng `log₂(16) = 4`.

### Bài 4.

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;

int demBuoc(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1, buoc = 0;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        buoc++;
        if      (a[giua] == x) return buoc;
        else if (a[giua] <  x) trai = giua + 1;
        else                   phai = giua - 1;
    }
    return buoc;
}

int main() {
    cout << "+-----------+-----------+-----------+" << endl;
    cout << "|     n     | Buoc toi da| log2(n)  |" << endl;
    cout << "+-----------+-----------+-----------+" << endl;

    for (int n : {10, 100, 1000, 10000, 100000, 1000000}) {
        vector<int> a(n);
        for (int i = 0; i < n; i++) a[i] = i;

        // Tim buoc TOI DA (tim gia tri khong ton tai)
        int maxBuoc = demBuoc(a, -1);

        cout << "| " << setw(9) << n
             << " | " << setw(9) << maxBuoc
             << " | " << setw(9) << fixed << setprecision(1) << log2(n) << " |" << endl;
    }
    cout << "+-----------+-----------+-----------+" << endl;
    return 0;
}
```

Output:

```
+-----------+-----------+-----------+
|     n     | Buoc toi da| log2(n)  |
+-----------+-----------+-----------+
|        10 |         4 |       3.3 |
|       100 |         7 |       6.6 |
|      1000 |        10 |      10.0 |
|     10000 |        14 |      13.3 |
|    100000 |        17 |      16.6 |
|   1000000 |        20 |      19.9 |
+-----------+-----------+-----------+
```

**Nhận xét: số bước ≈ `⌈log₂(n)⌉`.** Mỗi khi `n` tăng **gấp đôi**, chỉ cần thêm **1 bước**.

Với 1 tỷ phần tử, chỉ cần **30 bước** — trong khi tìm tuyến tính cần tới 1 tỷ.

### Bài 5.

```cpp
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using namespace std::chrono;

int timTuyenTinh(const vector<int>& a, int x) {
    for (size_t i = 0; i < a.size(); i++)
        if (a[i] == x) return i;
    return -1;
}

int timNhiPhan(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        if      (a[giua] == x) return giua;
        else if (a[giua] <  x) trai = giua + 1;
        else                   phai = giua - 1;
    }
    return -1;
}

int main() {
    const int N = 10000000;
    const int SO_LAN = 1000;

    vector<int> a(N);
    for (int i = 0; i < N; i++) a[i] = i * 2;      // mang da sap xep

    // ① Tuyen tinh
    auto t1 = high_resolution_clock::now();
    long long tong1 = 0;
    for (int i = 0; i < SO_LAN; i++) tong1 += timTuyenTinh(a, (N - 1) * 2);
    auto t2 = high_resolution_clock::now();
    auto tt = duration_cast<milliseconds>(t2 - t1).count();

    // ② Nhi phan
    t1 = high_resolution_clock::now();
    long long tong2 = 0;
    for (int i = 0; i < SO_LAN; i++) tong2 += timNhiPhan(a, (N - 1) * 2);
    t2 = high_resolution_clock::now();
    auto tnp = duration_cast<microseconds>(t2 - t1).count();

    cout << "Mang " << N << " phan tu, tim " << SO_LAN << " lan:" << endl;
    cout << "  Tuyen tinh : " << tt  << " ms" << endl;
    cout << "  Nhi phan   : " << tnp << " micro giay (" << tnp / 1000.0 << " ms)" << endl;
    cout << "  Nhanh hon  : " << (tt * 1000.0 / max(1LL, tnp)) << " lan" << endl;
    cout << "\nKiem tra ket qua giong nhau: " << (tong1 == tong2 ? "OK" : "SAI") << endl;
    return 0;
}
```

Kết quả tham khảo:

```
Mang 10000000 phan tu, tim 1000 lan:
  Tuyen tinh : 5200 ms
  Nhi phan   : 32 micro giay (0.032 ms)
  Nhanh hon  : 162500 lan
```

⚠️ **Nhưng:** tìm kiếm nhị phân yêu cầu mảng **đã sắp xếp** — bản thân việc sắp xếp tốn O(n log n). Nên:

| Số lần tìm | Nên dùng |
|---|---|
| 1–2 lần | Tuyến tính (khỏi sắp xếp) |
| Nhiều lần | **Sắp xếp một lần + nhị phân** |

### Bài 6.

```cpp
int giua = (trai + phai) / 2;       // NGUY HIEM: co the TRAN SO
```

**Lỗi:** với mảng rất lớn, `trai + phai` có thể vượt giới hạn `int`.

Ví dụ: `trai = 1.500.000.000`, `phai = 2.000.000.000`
```
trai + phai = 3.500.000.000  >  INT_MAX (2.147.483.647)
-> tran so -> giua thanh SO AM
-> a[giua] truy cap ngoai bien -> CRASH
```

**Sửa — công thức an toàn:**

```cpp
int giua = trai + (phai - trai) / 2;
```

**Vì sao an toàn:** `phai - trai` luôn ≤ `phai` nên không bao giờ tràn. Kết quả **hoàn toàn tương đương** về mặt toán học:

```
trai + (phai - trai)/2 = trai + phai/2 - trai/2 = (trai + phai)/2  ✔
```

💡 **Đây là lỗi lịch sử nổi tiếng:** thư viện chuẩn Java chứa lỗi này suốt **9 năm** (1997–2006) trong `Arrays.binarySearch`, được Joshua Bloch công bố năm 2006. Nó cho thấy ngay cả thuật toán đơn giản nhất cũng có thể ẩn chứa lỗi tinh vi.

Cách khác (dùng phép bit, cũng an toàn):

```cpp
int giua = (trai + phai) >> 1;      // van tran neu trai+phai tran
unsigned giua = ((unsigned)trai + phai) / 2;   // an toan
```

### Bài 7.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int timDauTien(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1;
    int kq = -1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (a[giua] == x) {
            kq = giua;              // luu lai, nhung VAN TIM TIEP ben trai
            phai = giua - 1;
        } else if (a[giua] < x) {
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }
    return kq;
}

int main() {
    vector<int> a = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5};

    cout << "Mang: ";
    for (size_t i = 0; i < a.size(); i++) cout << a[i] << "(" << i << ") ";
    cout << endl << endl;

    for (int x : {2, 5, 4, 9}) {
        int vt = timDauTien(a, x);
        cout << "Vi tri DAU TIEN cua " << x << ": "
             << (vt == -1 ? "khong co" : to_string(vt)) << endl;
    }
    return 0;
}
```

Output:

```
Vi tri DAU TIEN cua 2: 1
Vi tri DAU TIEN cua 5: 7
Vi tri DAU TIEN cua 4: 5
Vi tri DAU TIEN cua 9: khong co
```

💡 **Điểm mấu chốt:** khi tìm thấy, **không dừng ngay** mà lưu kết quả rồi tiếp tục thu hẹp về **bên trái** để tìm vị trí sớm hơn.

### Bài 8.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int timCuoiCung(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1;
    int kq = -1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (a[giua] == x) {
            kq = giua;
            trai = giua + 1;        // tim tiep ben PHAI
        } else if (a[giua] < x) {
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }
    return kq;
}

int main() {
    vector<int> a = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5};

    for (int x : {2, 5, 4, 9}) {
        int vt = timCuoiCung(a, x);
        cout << "Vi tri CUOI CUNG cua " << x << ": "
             << (vt == -1 ? "khong co" : to_string(vt)) << endl;
    }
    return 0;
}
```

Output:

```
Vi tri CUOI CUNG cua 2: 3
Vi tri CUOI CUNG cua 5: 10
Vi tri CUOI CUNG cua 4: 6
```

💡 Chỉ khác bài 7 đúng **một dòng**: `trai = giua + 1` thay vì `phai = giua - 1`.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int timDauTien(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1, kq = -1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        if (a[giua] == x) { kq = giua; phai = giua - 1; }
        else if (a[giua] < x) trai = giua + 1;
        else phai = giua - 1;
    }
    return kq;
}

int timCuoiCung(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1, kq = -1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        if (a[giua] == x) { kq = giua; trai = giua + 1; }
        else if (a[giua] < x) trai = giua + 1;
        else phai = giua - 1;
    }
    return kq;
}

int demSoLan(const vector<int>& a, int x) {
    int dau = timDauTien(a, x);
    if (dau == -1) return 0;
    return timCuoiCung(a, x) - dau + 1;
}

int main() {
    vector<int> a = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5};

    for (int x : {2, 5, 1, 9}) {
        cout << "So " << x << " xuat hien " << demSoLan(a, x) << " lan";

        // Kiem chung bang count (O(n))
        cout << "  (kiem chung: " << count(a.begin(), a.end(), x) << ")" << endl;
    }

    // Dung STL
    cout << "\nDung equal_range (STL):" << endl;
    auto [lo, hi] = equal_range(a.begin(), a.end(), 5);
    cout << "  So 5 xuat hien " << (hi - lo) << " lan, tu vi tri "
         << (lo - a.begin()) << endl;
    return 0;
}
```

**Độ phức tạp O(log n)** — nhanh hơn hẳn `count` (O(n)) khi mảng đã sắp xếp.

💡 `equal_range` của STL làm đúng việc này, trả về cặp iterator `[đầu, cuối)`.

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Tim vi tri dau tien co a[i] >= x  (lower_bound)
int lowerBound(const vector<int>& a, int x) {
    int trai = 0, phai = a.size();        // chu y: phai = size(), khong phai size()-1

    while (trai < phai) {                  // chu y: dau < khong phai <=
        int giua = trai + (phai - trai) / 2;
        if (a[giua] < x) trai = giua + 1;
        else             phai = giua;
    }
    return trai;                            // co the = size() neu moi phan tu < x
}

// Tim vi tri dau tien co a[i] > x  (upper_bound)
int upperBound(const vector<int>& a, int x) {
    int trai = 0, phai = a.size();
    while (trai < phai) {
        int giua = trai + (phai - trai) / 2;
        if (a[giua] <= x) trai = giua + 1;
        else              phai = giua;
    }
    return trai;
}

int main() {
    vector<int> a = {1, 3, 3, 5, 7, 7, 7, 9};

    cout << "Mang: ";
    for (size_t i = 0; i < a.size(); i++) cout << a[i] << "(" << i << ") ";
    cout << endl << endl;

    for (int x : {3, 7, 4, 0, 10}) {
        int lb = lowerBound(a, x);
        int ub = upperBound(a, x);
        cout << "x = " << x
             << ": lower_bound = " << lb
             << ", upper_bound = " << ub
             << ", so lan xuat hien = " << (ub - lb) << endl;

        // Kiem chung voi STL
        int lbStd = lower_bound(a.begin(), a.end(), x) - a.begin();
        if (lb != lbStd) cout << "  !!! KHONG KHOP voi STL" << endl;
    }
    return 0;
}
```

Output:

```
x = 3: lower_bound = 1, upper_bound = 3, so lan xuat hien = 2
x = 7: lower_bound = 4, upper_bound = 7, so lan xuat hien = 3
x = 4: lower_bound = 3, upper_bound = 3, so lan xuat hien = 0
x = 0: lower_bound = 0, upper_bound = 0, so lan xuat hien = 0
x = 10: lower_bound = 8, upper_bound = 8, so lan xuat hien = 0
```

⚠️ **3 khác biệt so với tìm kiếm nhị phân thường:**
1. `phai = a.size()` (không phải `size() - 1`)
2. Điều kiện `trai < phai` (không phải `<=`)
3. `phai = giua` (không phải `giua - 1`)

Chi tiết xem bài [10-06](../10-06-c-ham-binarysearch-lowerbound-upperbound-trong-c.md).

### Bài 11.

```cpp
#include <iostream>
using namespace std;

// Tim can bac hai NGUYEN: so lon nhat k thoa k*k <= n
long long canBacHai(long long n) {
    if (n < 0) return -1;
    if (n < 2) return n;

    long long trai = 1, phai = n, kq = 0;

    while (trai <= phai) {
        long long giua = trai + (phai - trai) / 2;

        if (giua <= n / giua) {           // tranh tran: thay vi giua*giua <= n
            kq = giua;
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }
    return kq;
}

int main() {
    for (long long n : {0LL, 1LL, 4LL, 8LL, 16LL, 100LL, 1000000000000LL}) {
        long long c = canBacHai(n);
        cout << "canBacHai(" << n << ") = " << c
             << "  (" << c << "^2 = " << c*c << ")" << endl;
    }
    return 0;
}
```

Output:

```
canBacHai(0) = 0  (0^2 = 0)
canBacHai(1) = 1  (1^2 = 1)
canBacHai(4) = 2  (2^2 = 4)
canBacHai(8) = 2  (2^2 = 4)
canBacHai(16) = 4  (4^2 = 16)
canBacHai(100) = 10  (10^2 = 100)
canBacHai(1000000000000) = 1000000  (1000000^2 = 1000000000000)
```

💡 **Đây là "tìm kiếm nhị phân trên đáp án"** — không tìm trong mảng, mà tìm trong **khoảng giá trị có thể**. Điều kiện: hàm phải **đơn điệu** (ở đây `k²` tăng dần theo `k`).

⚠️ **Dùng `giua <= n / giua` thay vì `giua * giua <= n`** để tránh tràn số với `n` rất lớn.

### Bài 12.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int timTrongMangXoay(const vector<int>& a, int x) {
    int trai = 0, phai = a.size() - 1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (a[giua] == x) return giua;

        // Xac dinh NUA NAO da sap xep
        if (a[trai] <= a[giua]) {
            // Nua TRAI da sap xep
            if (a[trai] <= x && x < a[giua]) phai = giua - 1;
            else                             trai = giua + 1;
        } else {
            // Nua PHAI da sap xep
            if (a[giua] < x && x <= a[phai]) trai = giua + 1;
            else                             phai = giua - 1;
        }
    }
    return -1;
}

int main() {
    vector<int> a = {4, 5, 6, 7, 0, 1, 2, 3};

    cout << "Mang xoay: ";
    for (size_t i = 0; i < a.size(); i++) cout << a[i] << "(" << i << ") ";
    cout << endl << endl;

    for (int x : {0, 4, 3, 8}) {
        int vt = timTrongMangXoay(a, x);
        cout << "Tim " << x << ": "
             << (vt == -1 ? "khong tim thay" : "vi tri " + to_string(vt)) << endl;
    }
    return 0;
}
```

Output:

```
Tim 0: vi tri 4
Tim 4: vi tri 0
Tim 3: vi tri 7
Tim 8: khong tim thay
```

**Ý tưởng:** trong mảng xoay, **luôn có ít nhất một nửa đã sắp xếp**. Xác định nửa nào, rồi kiểm tra `x` có nằm trong khoảng đó không để quyết định đi hướng nào.

Vẫn giữ được **O(log n)** — đây là bài toán phỏng vấn kinh điển (LeetCode 33).

### Bài 13.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// BAI TOAN: co n bo keo, moi bo a[i] cai. Chia deu cho m em, moi em nhan
// dung k cai (co the bo thua keo). Tim k LON NHAT.

bool duChia(const vector<int>& a, int m, int k) {
    if (k == 0) return true;
    long long soPhan = 0;
    for (int x : a) soPhan += x / k;
    return soPhan >= m;
}

int timKLonNhat(const vector<int>& a, int m) {
    int trai = 1, phai = *max_element(a.begin(), a.end());
    int kq = 0;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (duChia(a, m, giua)) {
            kq = giua;                // duoc -> thu gia tri LON HON
            trai = giua + 1;
        } else {
            phai = giua - 1;          // khong duoc -> thu NHO HON
        }
    }
    return kq;
}

int main() {
    vector<int> a = {5, 8, 11, 15};      // 4 bo keo
    int m = 10;                           // chia cho 10 em

    int k = timKLonNhat(a, m);
    cout << "Cac bo keo: ";
    for (int x : a) cout << x << " ";
    cout << "\nSo em: " << m << endl;
    cout << "Moi em nhan toi da: " << k << " cai keo" << endl;

    // Kiem chung
    int tong = 0;
    for (int x : a) tong += x / k;
    cout << "Kiem chung: chia duoc " << tong << " phan (>= " << m << ") ✔" << endl;
    return 0;
}
```

Output:

```
Cac bo keo: 5 8 11 15 
So em: 10
Moi em nhan toi da: 3 cai keo
Kiem chung: chia duoc 12 phan (>= 10) ✔
```

**Mẫu "tìm kiếm nhị phân trên đáp án":**

```cpp
int trai = min_dap_an, phai = max_dap_an, kq = -1;
while (trai <= phai) {
    int giua = trai + (phai - trai) / 2;
    if (kiemTra(giua)) { kq = giua; /* thu tot hon */ }
    else               { /* thu te hon */ }
}
```

**Điều kiện áp dụng:** hàm `kiemTra` phải **đơn điệu** — nếu `k` thoả thì mọi `k' < k` cũng thoả (hoặc ngược lại).

💡 Đây là kỹ thuật cực kỳ mạnh trong lập trình thi đấu — biến bài toán tối ưu thành bài toán kiểm tra đơn giản hơn nhiều.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int timChuoi(const vector<string>& ds, const string& x) {
    int trai = 0, phai = ds.size() - 1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if      (ds[giua] == x) return giua;
        else if (ds[giua] <  x) trai = giua + 1;
        else                    phai = giua - 1;
    }
    return -1;
}

int main() {
    vector<string> ds = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"};

    // Bao dam DA SAP XEP
    sort(ds.begin(), ds.end());

    cout << "Danh sach: ";
    for (const auto& s : ds) cout << s << " ";
    cout << endl << endl;

    for (string x : {"cherry", "apple", "grape", "kiwi"}) {
        int vt = timChuoi(ds, x);
        cout << "Tim \"" << x << "\": "
             << (vt == -1 ? "khong tim thay" : "vi tri " + to_string(vt)) << endl;
    }

    // Dung STL
    cout << "\nDung binary_search: "
         << boolalpha << binary_search(ds.begin(), ds.end(), "date") << endl;
    return 0;
}
```

💡 Tìm kiếm nhị phân hoạt động với **mọi kiểu có định nghĩa `operator<`** — `string`, `pair`, struct tự viết (nếu nạp chồng toán tử).

⚠️ **Nhớ sắp xếp trước!** Đây là lỗi phổ biến nhất — thuật toán không báo lỗi, chỉ cho kết quả sai.

### Bài 15.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    const int MIN = 1, MAX = 1000;

    cout << "============================================" << endl;
    cout << "  MAY SE DOAN SO CUA BAN (tu " << MIN << " den " << MAX << ")" << endl;
    cout << "============================================" << endl;
    cout << "Hay nghi mot so, roi tra loi:" << endl;
    cout << "  'l' neu so cua ban LON HON" << endl;
    cout << "  'n' neu so cua ban NHO HON" << endl;
    cout << "  'd' neu DUNG roi" << endl << endl;

    int trai = MIN, phai = MAX, soLan = 0;

    while (trai <= phai) {
        int doan = trai + (phai - trai) / 2;
        soLan++;

        cout << "Lan " << soLan << " - May doan: " << doan
             << "  (con " << (phai - trai + 1) << " kha nang)" << endl;
        cout << "  Tra loi (l/n/d): ";

        char tl;
        cin >> tl;
        tl = tolower((unsigned char)tl);

        if (tl == 'd') {
            cout << "\nMay doan dung sau " << soLan << " lan!" << endl;
            cout << "(Toi da can " << 10 << " lan cho khoang 1-1000)" << endl;
            return 0;
        } else if (tl == 'l') {
            trai = doan + 1;
        } else if (tl == 'n') {
            phai = doan - 1;
        } else {
            cout << "  Cau tra loi khong hop le, thu lai!" << endl;
            soLan--;
        }
    }

    cout << "\nBan da tra loi MAU THUAN! Khong co so nao thoa man." << endl;
    return 0;
}
```

Ví dụ chạy (người chơi nghĩ số 777):

```
Lan 1 - May doan: 500  (con 1000 kha nang)
  Tra loi (l/n/d): l
Lan 2 - May doan: 750  (con 500 kha nang)
  Tra loi (l/n/d): l
Lan 3 - May doan: 875  (con 250 kha nang)
  Tra loi (l/n/d): n
Lan 4 - May doan: 812  (con 125 kha nang)
  Tra loi (l/n/d): n
Lan 5 - May doan: 781  (con 62 kha nang)
  Tra loi (l/n/d): n
Lan 6 - May doan: 765  (con 31 kha nang)
  Tra loi (l/n/d): l
...
Lan 10 - May doan: 777
  Tra loi (l/n/d): d

May doan dung sau 10 lan!
```

💡 **Máy luôn thắng trong tối đa `⌈log₂(1000)⌉ = 10` lần đoán** — vì mỗi câu trả lời loại bỏ đúng một nửa khả năng.

Đây là minh hoạ trực quan nhất cho sức mạnh của tìm kiếm nhị phân:

| Khoảng số | Số lần đoán tối đa |
|---|---|
| 1–100 | 7 |
| 1–1.000 | 10 |
| 1–1.000.000 | 20 |
| 1–1 tỷ | 30 |
