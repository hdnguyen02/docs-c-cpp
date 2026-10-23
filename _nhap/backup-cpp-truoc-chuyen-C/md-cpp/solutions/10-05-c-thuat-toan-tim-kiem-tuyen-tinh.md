# Lời giải — [C++]. Thuật Toán Tìm Kiếm Tuyến Tính

[← Quay lại bài học](../10-05-c-thuat-toan-tim-kiem-tuyen-tinh.md)

> **Tìm kiếm tuyến tính (linear search)** duyệt lần lượt từng phần tử. Độ phức tạp **O(n)**, nhưng **không yêu cầu mảng sắp xếp**.

---

### Bài 1.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int timTuyenTinh(const vector<int>& a, int x) {
    for (size_t i = 0; i < a.size(); i++)
        if (a[i] == x) return i;
    return -1;
}

int main() {
    vector<int> a = {7, 3, 9, 1, 5, 3, 8};

    for (int x : {9, 3, 100}) {
        int vt = timTuyenTinh(a, x);
        cout << "Tim " << x << ": ";
        if (vt != -1) cout << "thay tai vi tri " << vt << endl;
        else          cout << "khong tim thay" << endl;
    }
    return 0;
}
```

💡 **Ưu điểm lớn nhất:** hoạt động với mảng **chưa sắp xếp** — đây là điều tìm kiếm nhị phân không làm được.

### Bài 2.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int timCuoiCung(const vector<int>& a, int x) {
    // Duyet NGUOC tu cuoi ve dau
    for (int i = (int)a.size() - 1; i >= 0; i--)
        if (a[i] == x) return i;
    return -1;
}

int main() {
    vector<int> a = {7, 3, 9, 1, 5, 3, 8, 3};

    cout << "Mang: ";
    for (size_t i = 0; i < a.size(); i++) cout << a[i] << "(" << i << ") ";
    cout << endl;

    cout << "Vi tri CUOI CUNG cua 3: " << timCuoiCung(a, 3) << endl;   // 7
    return 0;
}
```

💡 Chỉ cần **duyệt ngược** — tìm thấy đầu tiên khi đi ngược chính là vị trí cuối cùng.

⚠️ Dùng `(int)a.size() - 1` chứ không phải `a.size() - 1` — vì `size()` là **unsigned**, với vector rỗng sẽ cho số cực lớn.

### Bài 3.

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> timTatCa(const vector<int>& a, int x) {
    vector<int> viTri;
    for (size_t i = 0; i < a.size(); i++)
        if (a[i] == x) viTri.push_back(i);
    return viTri;
}

int main() {
    vector<int> a = {3, 7, 3, 1, 3, 9, 3};

    auto ds = timTatCa(a, 3);

    cout << "Gia tri 3 xuat hien tai cac vi tri: ";
    if (ds.empty()) cout << "(khong co)";
    for (int v : ds) cout << v << " ";
    cout << "\nTong cong: " << ds.size() << " lan" << endl;
    return 0;
}
```

### Bài 4.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int demSoLan(const vector<int>& a, int x) {
    int dem = 0;
    for (int v : a) if (v == x) dem++;
    return dem;
}

int main() {
    vector<int> a = {3, 7, 3, 1, 3, 9, 3, 7};

    cout << "So 3 xuat hien: " << demSoLan(a, 3) << " lan" << endl;
    cout << "So 7 xuat hien: " << demSoLan(a, 7) << " lan" << endl;

    // Dung STL
    cout << "\nDung count(): " << count(a.begin(), a.end(), 3) << endl;
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
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
    vector<int> a = {4, 9, 15, 7, 12, 11, 20, 8};

    cout << "Mang: ";
    for (int x : a) cout << x << " ";
    cout << endl << endl;

    // ① So nguyen to dau tien
    for (size_t i = 0; i < a.size(); i++)
        if (laNguyenTo(a[i])) {
            cout << "So nguyen to dau tien: " << a[i] << " (vi tri " << i << ")" << endl;
            break;
        }

    // ② So chan dau tien - dung find_if
    auto it = find_if(a.begin(), a.end(), [](int x) { return x % 2 == 0; });
    if (it != a.end())
        cout << "So chan dau tien     : " << *it << " (vi tri " << (it - a.begin()) << ")" << endl;

    // ③ Chia het cho 5
    int k = 5;
    auto it2 = find_if(a.begin(), a.end(), [k](int x) { return x % k == 0; });
    if (it2 != a.end())
        cout << "Chia het cho " << k << " dau tien: " << *it2 << endl;
    else
        cout << "Khong co so nao chia het cho " << k << endl;
    return 0;
}
```

### Bài 6.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> a = {3, 7, 3, 1, 9, 3, 8, 2};

    // ① find - tim GIA TRI cu the
    auto it = find(a.begin(), a.end(), 9);
    if (it != a.end())
        cout << "find(9)      : vi tri " << (it - a.begin()) << endl;
    else
        cout << "find(9)      : khong thay" << endl;

    // ② find_if - tim theo DIEU KIEN
    auto it2 = find_if(a.begin(), a.end(), [](int x) { return x > 5; });
    cout << "find_if(>5)  : " << *it2 << " tai vi tri " << (it2 - a.begin()) << endl;

    // ③ find_if_not - tim phan tu KHONG thoa dieu kien
    auto it3 = find_if_not(a.begin(), a.end(), [](int x) { return x < 5; });
    cout << "find_if_not  : " << *it3 << endl;

    // ④ count - dem so lan xuat hien
    cout << "count(3)     : " << count(a.begin(), a.end(), 3) << endl;

    // ⑤ count_if - dem theo dieu kien
    cout << "count_if(le) : " << count_if(a.begin(), a.end(),
                                          [](int x){ return x % 2 == 1; }) << endl;

    // ⑥ any_of / all_of / none_of
    cout << boolalpha;
    cout << "any_of(>8)   : " << any_of(a.begin(), a.end(), [](int x){return x>8;}) << endl;
    cout << "all_of(>0)   : " << all_of(a.begin(), a.end(), [](int x){return x>0;}) << endl;
    cout << "none_of(<0)  : " << none_of(a.begin(), a.end(), [](int x){return x<0;}) << endl;
    return 0;
}
```

**Bảng các hàm tìm kiếm tuyến tính trong `<algorithm>`:**

| Hàm | Tác dụng | Trả về |
|---|---|---|
| `find(b, e, x)` | Tìm giá trị `x` | Iterator, hoặc `e` nếu không thấy |
| `find_if(b, e, f)` | Tìm phần tử thoả `f` | Iterator |
| `find_if_not(b, e, f)` | Tìm phần tử **không** thoả `f` | Iterator |
| `count(b, e, x)` | Đếm số lần `x` xuất hiện | Số nguyên |
| `count_if(b, e, f)` | Đếm phần tử thoả `f` | Số nguyên |
| `any_of(b, e, f)` | Có **ít nhất một** phần tử thoả? | `bool` |
| `all_of(b, e, f)` | **Tất cả** đều thoả? | `bool` |
| `none_of(b, e, f)` | **Không** phần tử nào thoả? | `bool` |
| `search(b1,e1,b2,e2)` | Tìm một **dãy con** | Iterator |

⚠️ **Luôn kiểm tra `it != v.end()`** trước khi dùng `*it` — nếu không tìm thấy, `*it` là truy cập ngoài biên.

### Bài 7.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
    return s;
}

int main() {
    vector<string> ds = {
        "Lap trinh C++", "Hoc Python", "Thuat toan va CTDL",
        "Lap trinh Web", "Co so du lieu"
    };

    string canTim;
    cout << "Nhap tu khoa tim kiem: ";
    getline(cin, canTim);

    string tk = toLower(canTim);
    vector<int> ketQua;

    for (size_t i = 0; i < ds.size(); i++)
        if (toLower(ds[i]).find(tk) != string::npos)
            ketQua.push_back(i);

    cout << "\nTim thay " << ketQua.size() << " ket qua:" << endl;
    for (int i : ketQua)
        cout << "  [" << i << "] " << ds[i] << endl;

    if (ketQua.empty()) cout << "  (khong co ket qua nao)" << endl;
    return 0;
}
```

Ví dụ với từ khoá `"lap trinh"`:

```
Tim thay 2 ket qua:
  [0] Lap trinh C++
  [3] Lap trinh Web
```

💡 Chuyển cả 2 vế về chữ thường để tìm kiếm **không phân biệt hoa/thường** — đúng như người dùng mong đợi.

### Bài 8.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct SinhVien {
    int    maSV;
    string ten;
    int    tuoi;
    double diem;
};

int main() {
    vector<SinhVien> ds = {
        {101, "An",    20, 8.5},
        {102, "Binh",  22, 9.0},
        {103, "Chi",   21, 7.5},
        {104, "Dung",  20, 9.0},
        {105, "Em",    23, 6.5}
    };

    // ① Tim theo MA SV
    int ma = 103;
    auto it = find_if(ds.begin(), ds.end(),
                      [ma](const SinhVien& sv) { return sv.maSV == ma; });
    if (it != ds.end())
        cout << "Ma " << ma << ": " << it->ten << ", " << it->diem << " diem" << endl;

    // ② Tim theo TEN
    string ten = "Dung";
    auto it2 = find_if(ds.begin(), ds.end(),
                       [&ten](const SinhVien& sv) { return sv.ten == ten; });
    if (it2 != ds.end())
        cout << "Ten " << ten << ": ma " << it2->maSV << endl;

    // ③ Tim TAT CA sinh vien diem >= 9.0
    cout << "\nSinh vien diem >= 9.0:" << endl;
    for (const auto& sv : ds)
        if (sv.diem >= 9.0)
            cout << "  " << sv.ten << " (" << sv.diem << ")" << endl;

    // ④ Dem sinh vien 20 tuoi
    int dem = count_if(ds.begin(), ds.end(),
                       [](const SinhVien& sv) { return sv.tuoi == 20; });
    cout << "\nSo sinh vien 20 tuoi: " << dem << endl;
    return 0;
}
```

💡 `it->ten` tương đương `(*it).ten` — toán tử `->` gọn hơn khi truy cập thành viên qua iterator/con trỏ.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 1000000;
    const int SO_TRUY_VAN = 1000;

    vector<int> v(N);
    for (int i = 0; i < N; i++) v[i] = (i * 7919 + 13) % N;

    // === KICH BAN 1: mang CHUA sap xep, tim 1 lan ===
    auto t1 = high_resolution_clock::now();
    auto it = find(v.begin(), v.end(), N - 1);
    auto t2 = high_resolution_clock::now();
    cout << "Tim 1 lan (tuyen tinh): "
         << duration_cast<microseconds>(t2-t1).count() << " micro giay" << endl;

    // === KICH BAN 2: sap xep truoc roi tim nhieu lan ===
    vector<int> w = v;
    t1 = high_resolution_clock::now();
    sort(w.begin(), w.end());
    t2 = high_resolution_clock::now();
    auto tSort = duration_cast<milliseconds>(t2-t1).count();
    cout << "Thoi gian sap xep     : " << tSort << " ms" << endl;

    // Tim tuyen tinh nhieu lan
    t1 = high_resolution_clock::now();
    for (int i = 0; i < SO_TRUY_VAN; i++) find(v.begin(), v.end(), i);
    t2 = high_resolution_clock::now();
    auto tTT = duration_cast<milliseconds>(t2-t1).count();

    // Tim nhi phan nhieu lan
    t1 = high_resolution_clock::now();
    for (int i = 0; i < SO_TRUY_VAN; i++) binary_search(w.begin(), w.end(), i);
    t2 = high_resolution_clock::now();
    auto tNP = duration_cast<microseconds>(t2-t1).count();

    cout << "\n" << SO_TRUY_VAN << " truy van:" << endl;
    cout << "  Tuyen tinh        : " << tTT << " ms" << endl;
    cout << "  Nhi phan          : " << tNP/1000.0 << " ms" << endl;
    cout << "  Nhi phan + sap xep: " << tSort + tNP/1000.0 << " ms" << endl;
    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Tuyến tính | Nhị phân |
|---|---|---|
| **Yêu cầu sắp xếp** | ❌ **Không** | ✅ **Bắt buộc** |
| Độ phức tạp | O(n) | **O(log n)** |
| Với n = 10⁶ | ~10⁶ phép so sánh | **~20** phép so sánh |
| Chi phí chuẩn bị | 0 | O(n log n) để sắp xếp |
| Hoạt động với `list` | ✅ Có | ❌ Không (cần truy cập ngẫu nhiên) |
| Code | ✅ Rất đơn giản | Phức tạp hơn |

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Tìm **1–2 lần**, mảng chưa sắp | **Tuyến tính** (khỏi tốn công sắp) |
| Tìm **nhiều lần** trên cùng dữ liệu | **Sắp xếp một lần + nhị phân** |
| Dữ liệu **thay đổi liên tục** | Tuyến tính, hoặc dùng `set`/`map` |
| Mảng **đã sắp sẵn** | **Nhị phân** |
| Tìm theo **điều kiện phức tạp** (không phải so sánh giá trị) | **Tuyến tính** |

**Công thức quyết định:** nếu số truy vấn `q` thoả `q × n > n log n + q × log n`, tức `q > log n`, thì nên sắp xếp trước. Với `n = 10⁶`, ngưỡng là khoảng **20 truy vấn**.

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Tim kiem THONG THUONG: moi vong 2 phep so sanh (i < n VA a[i] == x)
int timThuong(vector<int>& a, int x) {
    for (size_t i = 0; i < a.size(); i++)
        if (a[i] == x) return i;
    return -1;
}

// Tim kiem voi LINH CANH: moi vong chi 1 phep so sanh
int timLinhCanh(vector<int>& a, int x) {
    if (a.empty()) return -1;

    size_t n = a.size();
    int cuoiCung = a[n - 1];
    a[n - 1] = x;                        // dat "linh canh" o cuoi

    size_t i = 0;
    while (a[i] != x) i++;               // KHONG can kiem tra i < n!

    a[n - 1] = cuoiCung;                 // khoi phuc

    if (i < n - 1) return i;
    return (cuoiCung == x) ? (int)(n - 1) : -1;
}

int main() {
    const int N = 50000000;
    vector<int> v(N);
    for (int i = 0; i < N; i++) v[i] = i;

    int x = N - 1;                        // truong hop xau nhat

    auto t1 = high_resolution_clock::now();
    int r1 = timThuong(v, x);
    auto t2 = high_resolution_clock::now();
    cout << "Thong thuong: " << duration_cast<milliseconds>(t2-t1).count()
         << " ms (ket qua " << r1 << ")" << endl;

    t1 = high_resolution_clock::now();
    int r2 = timLinhCanh(v, x);
    t2 = high_resolution_clock::now();
    cout << "Linh canh   : " << duration_cast<milliseconds>(t2-t1).count()
         << " ms (ket qua " << r2 << ")" << endl;

    cout << "\nKet qua giong nhau: " << boolalpha << (r1 == r2) << endl;
    return 0;
}
```

**Kỹ thuật "lính canh" (sentinel):** đặt giá trị cần tìm vào **cuối mảng**, đảm bảo vòng lặp **chắc chắn dừng**. Nhờ đó bỏ được phép kiểm tra biên `i < n` mỗi vòng.

```
Thong thuong: kiem tra (i < n) VA (a[i] == x)   -> 2 phep so sanh
Linh canh   : chi kiem tra (a[i] == x)           -> 1 phep so sanh
```

Kết quả tham khảo:

```
Thong thuong: 42 ms
Linh canh   : 31 ms
```

⚠️ **Nhược điểm:** phải **sửa mảng** (rồi khôi phục) — không dùng được với mảng `const`, và không an toàn khi lập trình đa luồng.

⚠️ Với compiler hiện đại và `-O2`, chênh lệch thường nhỏ hơn nhiều vì compiler đã tự tối ưu. Đây chủ yếu là kỹ thuật mang tính học thuật.

### Bài 11.

```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>
using namespace std;

pair<int,int> timTrongMaTran(const vector<vector<int>>& a, int x) {
    for (size_t i = 0; i < a.size(); i++)
        for (size_t j = 0; j < a[i].size(); j++)
            if (a[i][j] == x) return {(int)i, (int)j};
    return {-1, -1};
}

vector<pair<int,int>> timTatCa(const vector<vector<int>>& a, int x) {
    vector<pair<int,int>> kq;
    for (size_t i = 0; i < a.size(); i++)
        for (size_t j = 0; j < a[i].size(); j++)
            if (a[i][j] == x) kq.push_back({(int)i, (int)j});
    return kq;
}

int main() {
    vector<vector<int>> m = {
        {1, 5, 3, 7},
        {9, 2, 5, 4},
        {6, 8, 1, 5}
    };

    cout << "Ma tran:" << endl;
    for (const auto& hang : m) {
        for (int x : hang) cout << setw(4) << x;
        cout << endl;
    }

    for (int x : {5, 9, 100}) {
        auto [i, j] = timTrongMaTran(m, x);
        cout << "\nTim " << x << ": ";
        if (i != -1) cout << "thay tai (" << i << ", " << j << ")";
        else         cout << "khong tim thay";
        cout << endl;

        auto ds = timTatCa(m, x);
        if (ds.size() > 1) {
            cout << "  Tat ca vi tri: ";
            for (auto [r, c] : ds) cout << "(" << r << "," << c << ") ";
            cout << endl;
        }
    }
    return 0;
}
```

Độ phức tạp **O(n×m)** — duyệt toàn bộ ma trận.

💡 Nếu ma trận **đã sắp xếp theo hàng và cột**, có thuật toán O(n+m): bắt đầu từ góc trên-phải, nếu giá trị lớn hơn thì sang trái, nhỏ hơn thì xuống dưới.

### Bài 12.

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
#include <climits>
using namespace std;

int timGanNhat(const vector<int>& a, int x) {
    if (a.empty()) return -1;

    int viTri = 0;
    long long kcMin = llabs((long long)a[0] - x);

    for (size_t i = 1; i < a.size(); i++) {
        long long kc = llabs((long long)a[i] - x);
        if (kc < kcMin) { kcMin = kc; viTri = i; }
    }
    return viTri;
}

int main() {
    vector<int> a = {10, 3, 25, 7, 18, 1, 30};
    int x;

    cout << "Mang: ";
    for (int v : a) cout << v << " ";
    cout << endl;

    cout << "Nhap gia tri x: ";
    cin >> x;

    int vt = timGanNhat(a, x);
    cout << "Phan tu gan " << x << " nhat: " << a[vt]
         << " (vi tri " << vt << ", cach " << abs(a[vt] - x) << ")" << endl;
    return 0;
}
```

Với `x = 15`: kết quả là `18` (cách 3).

💡 Nếu mảng **đã sắp xếp**, dùng `lower_bound` cho **O(log n)** thay vì O(n) — xem bài [10-06](../10-06-c-ham-binarysearch-lowerbound-upperbound-trong-c.md).

### Bài 13.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>
#include <chrono>
using namespace std;
using namespace std::chrono;

// Cach 1: duyet moi cap - O(n^2)
pair<int,int> timCapNgayTho(const vector<int>& a, int x) {
    for (size_t i = 0; i < a.size(); i++)
        for (size_t j = i + 1; j < a.size(); j++)
            if (a[i] + a[j] == x) return {(int)i, (int)j};
    return {-1, -1};
}

// Cach 2: dung hash set - O(n)
pair<int,int> timCapToiUu(const vector<int>& a, int x) {
    unordered_set<int> daGap;
    for (size_t i = 0; i < a.size(); i++) {
        int can = x - a[i];
        if (daGap.count(can)) {
            // Tim lai vi tri cua `can`
            for (size_t j = 0; j < i; j++)
                if (a[j] == can) return {(int)j, (int)i};
        }
        daGap.insert(a[i]);
    }
    return {-1, -1};
}

int main() {
    vector<int> a = {2, 7, 11, 15, 3, 6};
    int x = 9;

    auto [i1, j1] = timCapNgayTho(a, x);
    cout << "Cach 1 O(n^2): ";
    if (i1 != -1) cout << a[i1] << " + " << a[j1] << " = " << x
                       << " (vi tri " << i1 << ", " << j1 << ")" << endl;
    else cout << "khong tim thay" << endl;

    auto [i2, j2] = timCapToiUu(a, x);
    cout << "Cach 2 O(n)  : ";
    if (i2 != -1) cout << a[i2] << " + " << a[j2] << " = " << x << endl;
    else cout << "khong tim thay" << endl;

    // So sanh toc do voi mang lon
    const int N = 20000;
    vector<int> b(N);
    for (int i = 0; i < N; i++) b[i] = i;
    int target = 2 * N - 3;                      // 2 phan tu cuoi

    auto t1 = high_resolution_clock::now();
    timCapNgayTho(b, target);
    auto t2 = high_resolution_clock::now();
    cout << "\nN = " << N << ":" << endl;
    cout << "  O(n^2): " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    t1 = high_resolution_clock::now();
    timCapToiUu(b, target);
    t2 = high_resolution_clock::now();
    cout << "  O(n)  : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;
    return 0;
}
```

💡 **Bài toán Two Sum** — một trong những bài phỏng vấn phổ biến nhất. Điểm mấu chốt: thay vì tìm cặp `(a, b)` với `a + b = x`, ta duyệt từng `a` và **tra cứu** xem `x − a` đã gặp chưa.

`unordered_set` cho tra cứu **O(1)** trung bình → tổng thể **O(n)**.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
#include <iomanip>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 20000000;
    const int SO_LAN = 20;

    vector<int> v(N);
    for (int i = 0; i < N; i++) v[i] = i;

    struct { const char* nhan; int giaTri; } bo[] = {
        {"Phan tu DAU     ", 0},
        {"Phan tu 1/4     ", N / 4},
        {"Phan tu GIUA    ", N / 2},
        {"Phan tu 3/4     ", 3 * N / 4},
        {"Phan tu CUOI    ", N - 1},
        {"KHONG TON TAI   ", -1}
    };

    cout << "Mang " << N << " phan tu, moi truong hop tim " << SO_LAN << " lan:" << endl;
    cout << "+------------------+------------+" << endl;
    cout << "| TRUONG HOP       | THOI GIAN  |" << endl;
    cout << "+------------------+------------+" << endl;

    for (auto& t : bo) {
        auto t1 = high_resolution_clock::now();
        for (int k = 0; k < SO_LAN; k++)
            find(v.begin(), v.end(), t.giaTri);
        auto t2 = high_resolution_clock::now();

        cout << "| " << t.nhan << " | "
             << setw(7) << duration_cast<milliseconds>(t2-t1).count() << " ms |" << endl;
    }
    cout << "+------------------+------------+" << endl;
    return 0;
}
```

Kết quả tham khảo:

```
+------------------+------------+
| TRUONG HOP       | THOI GIAN  |
+------------------+------------+
| Phan tu DAU      |       0 ms |
| Phan tu 1/4      |      62 ms |
| Phan tu GIUA     |     124 ms |
| Phan tu 3/4      |     186 ms |
| Phan tu CUOI     |     248 ms |
| KHONG TON TAI    |     249 ms |
+------------------+------------+
```

**Phân tích độ phức tạp:**

| Trường hợp | Số phép so sánh | Ký hiệu |
|---|---|---|
| **Tốt nhất** — phần tử ở đầu | 1 | **O(1)** |
| **Trung bình** — vị trí ngẫu nhiên | n/2 | **O(n)** |
| **Xấu nhất** — ở cuối hoặc không có | n | **O(n)** |

💡 Thời gian **tỉ lệ thuận** với vị trí phần tử — đúng như lý thuyết. Đây là bản chất của O(n).

### Bài 15.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <cctype>
#include <limits>
using namespace std;

struct LienHe {
    string ten;
    string sdt;
    string email;
};

string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
    return s;
}

void hienThi(const vector<LienHe>& ds, const vector<int>& viTri) {
    if (viTri.empty()) { cout << ">> Khong tim thay ket qua nao!" << endl; return; }

    cout << "+-----+--------------------+--------------+------------------------+" << endl;
    cout << "| STT | HO TEN             | SO DIEN THOAI| EMAIL                  |" << endl;
    cout << "+-----+--------------------+--------------+------------------------+" << endl;
    for (int i : viTri)
        cout << "| " << left  << setw(3) << i + 1
             << " | " << setw(18) << ds[i].ten
             << " | " << setw(12) << ds[i].sdt
             << " | " << setw(22) << ds[i].email << " |" << endl;
    cout << "+-----+--------------------+--------------+------------------------+" << endl;
    cout << ">> Tim thay " << viTri.size() << " ket qua." << endl;
}

int main() {
    vector<LienHe> ds = {
        {"Nguyen Van An",   "0912345678", "an.nguyen@gmail.com"},
        {"Tran Thi Binh",   "0387654321", "binh.tran@gmail.com"},
        {"Le Hoang Cuong",  "0905112233", "cuong.le@company.vn"},
        {"Pham Minh An",    "0788990011", "an.pham@gmail.com"},
        {"Hoang Thi Dung",  "0356778899", "dung.hoang@company.vn"}
    };

    int chon;
    do {
        cout << "\n====== DANH BA ======" << endl;
        cout << "1. Hien thi tat ca"      << endl;
        cout << "2. Tim theo TEN chinh xac" << endl;
        cout << "3. Tim theo MOT PHAN ten"  << endl;
        cout << "4. Tim theo SO DIEN THOAI" << endl;
        cout << "5. Tim theo EMAIL (mot phan)" << endl;
        cout << "0. Thoat"                 << endl;
        cout << "=====================" << endl;
        cout << "Lua chon: ";

        if (!(cin >> chon)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << ">> Nhap khong hop le!" << endl;
            continue;
        }
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        vector<int> kq;
        string tk;

        switch (chon) {
            case 1:
                for (size_t i = 0; i < ds.size(); i++) kq.push_back(i);
                hienThi(ds, kq);
                break;

            case 2:
                cout << "Nhap ten chinh xac: ";
                getline(cin, tk);
                for (size_t i = 0; i < ds.size(); i++)
                    if (toLower(ds[i].ten) == toLower(tk)) kq.push_back(i);
                hienThi(ds, kq);
                break;

            case 3:
                cout << "Nhap mot phan ten: ";
                getline(cin, tk);
                for (size_t i = 0; i < ds.size(); i++)
                    if (toLower(ds[i].ten).find(toLower(tk)) != string::npos)
                        kq.push_back(i);
                hienThi(ds, kq);
                break;

            case 4:
                cout << "Nhap so dien thoai: ";
                getline(cin, tk);
                for (size_t i = 0; i < ds.size(); i++)
                    if (ds[i].sdt.find(tk) != string::npos) kq.push_back(i);
                hienThi(ds, kq);
                break;

            case 5:
                cout << "Nhap mot phan email: ";
                getline(cin, tk);
                for (size_t i = 0; i < ds.size(); i++)
                    if (toLower(ds[i].email).find(toLower(tk)) != string::npos)
                        kq.push_back(i);
                hienThi(ds, kq);
                break;

            case 0:
                cout << ">> Tam biet!" << endl;
                break;

            default:
                cout << ">> Lua chon khong hop le!" << endl;
        }
    } while (chon != 0);

    return 0;
}
```

Ví dụ tìm "An" theo một phần tên:

```
+-----+--------------------+--------------+------------------------+
| STT | HO TEN             | SO DIEN THOAI| EMAIL                  |
+-----+--------------------+--------------+------------------------+
| 1   | Nguyen Van An      | 0912345678   | an.nguyen@gmail.com    |
| 4   | Pham Minh An       | 0788990011   | an.pham@gmail.com      |
+-----+--------------------+--------------+------------------------+
>> Tim thay 2 ket qua.
```

💡 **Vì sao danh bạ dùng tìm kiếm tuyến tính:**
1. Cho phép tìm theo **một phần** chuỗi — nhị phân không làm được
2. Cho phép tìm theo **nhiều trường** khác nhau
3. Dữ liệu **thay đổi liên tục** (thêm/xoá liên hệ) — sắp xếp lại mỗi lần sẽ tốn hơn
4. Số lượng liên hệ thường nhỏ (vài trăm đến vài nghìn) → O(n) hoàn toàn chấp nhận được
