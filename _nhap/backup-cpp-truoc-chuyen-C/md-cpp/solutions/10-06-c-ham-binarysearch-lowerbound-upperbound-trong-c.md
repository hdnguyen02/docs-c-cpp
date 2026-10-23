# Lời giải — [C++]. Hàm binary_search, lower_bound, upper_bound Trong C++

[← Quay lại bài học](../10-06-c-ham-binarysearch-lowerbound-upperbound-trong-c.md)

> **Cả 3 hàm đều yêu cầu dãy ĐÃ SẮP XẾP.** Chúng nằm trong `<algorithm>` và có độ phức tạp **O(log n)**.

| Hàm | Trả về |
|---|---|
| `binary_search(b, e, x)` | `bool` — có tồn tại `x` không |
| `lower_bound(b, e, x)` | Iterator tới phần tử **đầu tiên ≥ x** |
| `upper_bound(b, e, x)` | Iterator tới phần tử **đầu tiên > x** |

---

### Bài 1.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 3, 5, 7, 9, 11, 13};

    cout << "Mang: ";
    for (int x : v) cout << x << " ";
    cout << endl << endl;

    cout << boolalpha;
    for (int x : {7, 1, 13, 8, 100}) {
        cout << "binary_search(" << x << ") = "
             << binary_search(v.begin(), v.end(), x) << endl;
    }

    // Voi mang tinh
    int a[] = {2, 4, 6, 8, 10};
    cout << "\nMang tinh, tim 6: " << binary_search(a, a + 5, 6) << endl;
    return 0;
}
```

Output:

```
binary_search(7) = true
binary_search(1) = true
binary_search(13) = true
binary_search(8) = false
binary_search(100) = false
```

### Bài 2.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 3, 3, 5, 7, 7, 7, 9};

    cout << "Mang: ";
    for (size_t i = 0; i < v.size(); i++) cout << v[i] << "(" << i << ") ";
    cout << endl << endl;

    for (int x : {3, 7, 4, 0, 10}) {
        auto it = lower_bound(v.begin(), v.end(), x);
        int vt = it - v.begin();

        cout << "lower_bound(" << x << ") -> vi tri " << vt;
        if (it != v.end()) cout << ", gia tri " << *it;
        else               cout << " (= end(), moi phan tu deu < " << x << ")";
        cout << endl;
    }
    return 0;
}
```

Output:

```
lower_bound(3) -> vi tri 1, gia tri 3
lower_bound(7) -> vi tri 4, gia tri 7
lower_bound(4) -> vi tri 3, gia tri 5
lower_bound(0) -> vi tri 0, gia tri 1
lower_bound(10) -> vi tri 8 (= end(), moi phan tu deu < 10)
```

⚠️ **Luôn kiểm tra `it != v.end()`** trước khi giải tham chiếu `*it`.

💡 `lower_bound` trả về **vị trí chèn** đúng chỗ để giữ thứ tự sắp xếp — kể cả khi `x` không có trong mảng.

### Bài 3.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 3, 3, 5, 7, 7, 7, 9};

    cout << "Mang: ";
    for (size_t i = 0; i < v.size(); i++) cout << v[i] << "(" << i << ") ";
    cout << endl << endl;

    cout << "+-----+-------------+-------------+" << endl;
    cout << "|  x  | lower_bound | upper_bound |" << endl;
    cout << "+-----+-------------+-------------+" << endl;

    for (int x : {1, 3, 4, 7, 9, 10}) {
        int lb = lower_bound(v.begin(), v.end(), x) - v.begin();
        int ub = upper_bound(v.begin(), v.end(), x) - v.begin();
        cout << "| " << x << "   |      " << lb
             << "      |      " << ub << "      |" << endl;
    }
    cout << "+-----+-------------+-------------+" << endl;
    return 0;
}
```

Output:

```
+-----+-------------+-------------+
|  x  | lower_bound | upper_bound |
+-----+-------------+-------------+
| 1   |      0      |      1      |
| 3   |      1      |      3      |
| 4   |      3      |      3      |
| 7   |      4      |      7      |
| 9   |      7      |      8      |
| 10  |      8      |      8      |
+-----+-------------+-------------+
```

**Phân biệt cốt lõi:**

```
Mang:   1   3   3   5   7   7   7   9
Index:  0   1   2   3   4   5   6   7

x = 3:
        lower_bound = 1  (phan tu DAU TIEN >= 3)
                      ↓
        1  [3   3]  5  7  7  7  9
                 ↑
        upper_bound = 3  (phan tu DAU TIEN > 3)
```

💡 Khi `x` **không tồn tại**, `lower_bound == upper_bound`.

### Bài 4.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int demSoLan(const vector<int>& v, int x) {
    auto lb = lower_bound(v.begin(), v.end(), x);
    auto ub = upper_bound(v.begin(), v.end(), x);
    return ub - lb;
}

int main() {
    vector<int> v = {1, 3, 3, 5, 7, 7, 7, 9, 9};

    for (int x : {3, 7, 9, 1, 4}) {
        cout << "So " << x << " xuat hien " << demSoLan(v, x) << " lan";
        cout << "  (kiem chung: " << count(v.begin(), v.end(), x) << ")" << endl;
    }
    return 0;
}
```

Output:

```
So 3 xuat hien 2 lan  (kiem chung: 2)
So 7 xuat hien 3 lan  (kiem chung: 3)
So 9 xuat hien 2 lan  (kiem chung: 2)
So 1 xuat hien 1 lan  (kiem chung: 1)
So 4 xuat hien 0 lan  (kiem chung: 0)
```

💡 **Độ phức tạp O(log n)** — nhanh hơn hẳn `count` (O(n)) khi mảng đã sắp xếp.

### Bài 5.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 3, 3, 5, 7, 7, 7, 9};

    for (int x : {3, 7, 4}) {
        auto [lb, ub] = equal_range(v.begin(), v.end(), x);

        cout << "equal_range(" << x << "):" << endl;
        cout << "  Vi tri : [" << (lb - v.begin()) << ", " << (ub - v.begin()) << ")" << endl;
        cout << "  So luong: " << (ub - lb) << endl;
        cout << "  Cac phan tu: ";
        for (auto it = lb; it != ub; ++it) cout << *it << " ";
        if (lb == ub) cout << "(khong co)";
        cout << endl << endl;
    }
    return 0;
}
```

Output:

```
equal_range(3):
  Vi tri : [1, 3)
  So luong: 2
  Cac phan tu: 3 3 

equal_range(7):
  Vi tri : [4, 7)
  So luong: 3
  Cac phan tu: 7 7 7 

equal_range(4):
  Vi tri : [3, 3)
  So luong: 0
  Cac phan tu: (khong co)
```

💡 **`equal_range` = `lower_bound` + `upper_bound` trong một lời gọi**, và cài đặt tối ưu hơn (không duyệt 2 lần độc lập).

`auto [lb, ub] = ...` là structured binding (C++17).

### Bài 6.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 3, 5, 7, 9};

    cout << "Mang ban dau: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    for (int x : {4, 0, 10, 5}) {
        vector<int> tam = v;
        auto it = lower_bound(tam.begin(), tam.end(), x);
        int vt = it - tam.begin();

        tam.insert(it, x);

        cout << "Chen " << x << " vao vi tri " << vt << ": ";
        for (int y : tam) cout << y << " ";
        cout << endl;
    }

    // Duy tri mang luon sap xep khi them nhieu phan tu
    cout << "\nThem lien tiep 6, 2, 8 vao mang goc:" << endl;
    for (int x : {6, 2, 8}) {
        v.insert(lower_bound(v.begin(), v.end(), x), x);
        cout << "  Sau khi them " << x << ": ";
        for (int y : v) cout << y << " ";
        cout << endl;
    }
    return 0;
}
```

Output:

```
Chen 4 vao vi tri 2: 1 3 4 5 7 9 
Chen 0 vao vi tri 0: 0 1 3 5 7 9 
Chen 10 vao vi tri 5: 1 3 5 7 9 10 
Chen 5 vao vi tri 2: 1 3 5 5 7 9 
```

💡 **Đây là ứng dụng quan trọng nhất của `lower_bound`:** duy trì một mảng **luôn được sắp xếp** khi thêm phần tử, mà không phải sắp xếp lại toàn bộ.

⚠️ Tuy việc **tìm vị trí** là O(log n), nhưng `vector::insert` vẫn phải **dịch các phần tử** phía sau — O(n). Nếu cần chèn thường xuyên, dùng `set` hoặc `multiset` (O(log n) hoàn toàn).

### Bài 7.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 3, 5, 7, 9};

    // binary_search chi tra ve BOOL
    bool co = binary_search(v.begin(), v.end(), 5);
    cout << "binary_search(5) = " << boolalpha << co << endl;
    // Khong biet 5 o vi tri nao!

    // Muon lay VI TRI -> dung lower_bound roi kiem tra
    int x = 5;
    auto it = lower_bound(v.begin(), v.end(), x);
    if (it != v.end() && *it == x) {
        cout << "Tim thay " << x << " tai vi tri " << (it - v.begin()) << endl;
    } else {
        cout << "Khong tim thay " << x << endl;
    }

    // Viet thanh ham tien dung
    auto timViTri = [](const vector<int>& v, int x) -> int {
        auto it = lower_bound(v.begin(), v.end(), x);
        if (it != v.end() && *it == x) return it - v.begin();
        return -1;
    };

    cout << "\ntimViTri(7)  = " << timViTri(v, 7) << endl;    // 3
    cout << "timViTri(6)  = " << timViTri(v, 6) << endl;      // -1
    return 0;
}
```

**Vì sao `binary_search` chỉ trả về `bool`:**

Thiết kế của STL tuân theo nguyên tắc **"mỗi hàm làm đúng một việc"**:
- Cần biết **có tồn tại** → `binary_search`
- Cần biết **ở đâu** → `lower_bound` / `upper_bound`
- Cần biết **khoảng** → `equal_range`

Nếu `binary_search` trả về iterator, nó sẽ trùng lặp chức năng với `lower_bound` — và phải quy định trả về vị trí nào khi có nhiều phần tử bằng nhau.

**Công thức lấy vị trí:**

```cpp
auto it = lower_bound(v.begin(), v.end(), x);
bool timThay = (it != v.end() && *it == x);
int viTri = timThay ? (it - v.begin()) : -1;
```

⚠️ **Bắt buộc kiểm tra CẢ HAI điều kiện:** `it != v.end()` (không vượt biên) **và** `*it == x` (đúng giá trị cần tìm).

### Bài 8.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int timGanNhat(const vector<int>& v, int x) {
    if (v.empty()) return -1;

    auto it = lower_bound(v.begin(), v.end(), x);

    // Truong hop 1: x lon hon moi phan tu
    if (it == v.end()) return v.size() - 1;

    // Truong hop 2: x nho hon hoac bang phan tu dau
    if (it == v.begin()) return 0;

    // Truong hop 3: so sanh phan tu tai `it` va phan tu TRUOC no
    int viTriSau  = it - v.begin();
    int viTriTruoc = viTriSau - 1;

    long long kcSau   = llabs((long long)v[viTriSau]  - x);
    long long kcTruoc = llabs((long long)v[viTriTruoc] - x);

    return (kcTruoc <= kcSau) ? viTriTruoc : viTriSau;
}

int main() {
    vector<int> v = {1, 5, 10, 15, 20, 30};

    cout << "Mang: ";
    for (int x : v) cout << x << " ";
    cout << endl << endl;

    for (int x : {0, 3, 7, 12, 25, 100}) {
        int vt = timGanNhat(v, x);
        cout << "Gan " << x << " nhat: " << v[vt]
             << " (vi tri " << vt << ", cach " << abs(v[vt] - x) << ")" << endl;
    }
    return 0;
}
```

Output:

```
Gan 0 nhat: 1 (vi tri 0, cach 1)
Gan 3 nhat: 1 (vi tri 0, cach 2)
Gan 7 nhat: 5 (vi tri 1, cach 2)
Gan 12 nhat: 10 (vi tri 2, cach 2)
Gan 25 nhat: 20 (vi tri 4, cach 5)
Gan 100 nhat: 30 (vi tri 5, cach 70)
```

💡 **Độ phức tạp O(log n)** — tốt hơn nhiều so với duyệt tuyến tính O(n).

**Ý tưởng:** `lower_bound` cho ta ranh giới — phần tử gần nhất chỉ có thể là phần tử **tại ranh giới** hoặc **ngay trước nó**.

⚠️ Phải xử lý 2 trường hợp biên: `it == end()` và `it == begin()`.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    // Mang sap xep GIAM DAN
    vector<int> v = {9, 7, 7, 5, 3, 3, 1};

    cout << "Mang (giam dan): ";
    for (size_t i = 0; i < v.size(); i++) cout << v[i] << "(" << i << ") ";
    cout << endl << endl;

    for (int x : {7, 5, 4}) {
        // PHAI truyen comparator greater<int>() giong luc sap xep
        auto lb = lower_bound(v.begin(), v.end(), x, greater<int>());
        auto ub = upper_bound(v.begin(), v.end(), x, greater<int>());

        cout << "x = " << x
             << ": lower_bound = " << (lb - v.begin())
             << ", upper_bound = " << (ub - v.begin())
             << ", so luong = "    << (ub - lb) << endl;
    }

    // binary_search cung can comparator
    cout << "\nbinary_search(7, greater) = " << boolalpha
         << binary_search(v.begin(), v.end(), 7, greater<int>()) << endl;

    // SAI: khong truyen comparator
    cout << "binary_search(7, khong cmp) = "
         << binary_search(v.begin(), v.end(), 7) << "  <- SAI!" << endl;
    return 0;
}
```

Output:

```
x = 7: lower_bound = 1, upper_bound = 3, so luong = 2
x = 5: lower_bound = 3, upper_bound = 4, so luong = 1
x = 4: lower_bound = 4, upper_bound = 4, so luong = 0

binary_search(7, greater) = true
binary_search(7, khong cmp) = false  <- SAI!
```

⚠️ **Quy tắc bắt buộc: comparator dùng cho `lower_bound`/`upper_bound`/`binary_search` phải GIỐNG HỆT comparator đã dùng khi `sort`.**

Nếu sắp xếp bằng `sort(v.begin(), v.end(), greater<int>())`, thì mọi hàm tìm kiếm cũng phải truyền `greater<int>()`.

**Ý nghĩa với thứ tự giảm dần:**
- `lower_bound` → phần tử đầu tiên **không lớn hơn** `x` (tức ≤ `x`)
- `upper_bound` → phần tử đầu tiên **nhỏ hơn** `x`

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
    // Mang da sap xep theo KHOA (first)
    vector<pair<int, string>> ds = {
        {101, "An"}, {103, "Binh"}, {105, "Chi"},
        {107, "Dung"}, {109, "Em"}
    };

    // Cach 1: tim bang pair day du (can biet ca gia tri second)
    auto it1 = lower_bound(ds.begin(), ds.end(), make_pair(105, string("")));
    cout << "Cach 1: ma " << it1->first << " - " << it1->second << endl;

    // Cach 2: dung comparator so sanh CHI KHOA - TOT HON
    int maCanTim = 105;
    auto it2 = lower_bound(ds.begin(), ds.end(), maCanTim,
        [](const pair<int,string>& p, int gt) { return p.first < gt; });

    if (it2 != ds.end() && it2->first == maCanTim)
        cout << "Cach 2: ma " << it2->first << " - " << it2->second << endl;
    else
        cout << "Cach 2: khong tim thay ma " << maCanTim << endl;

    // Tim ma khong ton tai
    int ma2 = 104;
    auto it3 = lower_bound(ds.begin(), ds.end(), ma2,
        [](const pair<int,string>& p, int gt) { return p.first < gt; });

    cout << "\nTim ma " << ma2 << ": ";
    if (it3 != ds.end() && it3->first == ma2) cout << it3->second << endl;
    else cout << "khong co (vi tri chen se la " << (it3 - ds.begin()) << ")" << endl;

    return 0;
}
```

⚠️ **Chú ý thứ tự tham số của comparator** trong `lower_bound`: tham số đầu là **phần tử trong dãy**, tham số sau là **giá trị cần tìm**.

```cpp
// lower_bound: cmp(phan_tu, gia_tri)
[](const pair<int,string>& p, int gt) { return p.first < gt; }

// upper_bound: cmp(gia_tri, phan_tu)  -- NGUOC LAI!
[](int gt, const pair<int,string>& p) { return gt < p.first; }
```

Đây là điểm rất dễ nhầm.

### Bài 11.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int demTrongKhoang(const vector<int>& v, int a, int b) {
    if (a > b) return 0;

    auto lb = lower_bound(v.begin(), v.end(), a);    // phan tu dau tien >= a
    auto ub = upper_bound(v.begin(), v.end(), b);    // phan tu dau tien > b

    return ub - lb;
}

int main() {
    vector<int> v = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};

    cout << "Mang: ";
    for (int x : v) cout << x << " ";
    cout << endl << endl;

    struct { int a, b; } bo[] = {{5, 11}, {1, 19}, {6, 8}, {20, 30}, {0, 4}};

    for (auto& t : bo) {
        int dem = demTrongKhoang(v, t.a, t.b);
        cout << "Trong khoang [" << t.a << ", " << t.b << "]: " << dem << " phan tu";

        if (dem > 0) {
            cout << "  ->  ";
            auto lb = lower_bound(v.begin(), v.end(), t.a);
            auto ub = upper_bound(v.begin(), v.end(), t.b);
            for (auto it = lb; it != ub; ++it) cout << *it << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output:

```
Trong khoang [5, 11]: 4 phan tu  ->  5 7 9 11 
Trong khoang [1, 19]: 10 phan tu  ->  1 3 5 7 9 11 13 15 17 19 
Trong khoang [6, 8]: 1 phan tu  ->  7 
Trong khoang [20, 30]: 0 phan tu
Trong khoang [0, 4]: 2 phan tu  ->  1 3 
```

💡 **Công thức vàng:** số phần tử trong `[a, b]` = `upper_bound(b) - lower_bound(a)`

Độ phức tạp **O(log n)** — cực kỳ hữu ích khi có nhiều truy vấn khoảng.

### Bài 12.

```cpp
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    set<int> s;
    for (int i = 0; i < 100000; i++) s.insert(i * 2);

    int x = 100000;

    // ① Dung PHUONG THUC cua set - O(log n)
    auto t1 = high_resolution_clock::now();
    for (int k = 0; k < 10000; k++) s.lower_bound(x);
    auto t2 = high_resolution_clock::now();
    cout << "s.lower_bound()          : "
         << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ② Dung HAM TU DO - O(n) voi set!
    t1 = high_resolution_clock::now();
    for (int k = 0; k < 10000; k++) lower_bound(s.begin(), s.end(), x);
    t2 = high_resolution_clock::now();
    cout << "std::lower_bound(s.begin()...) : "
         << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // Vi du su dung voi map
    map<string, int> m = {{"An", 90}, {"Binh", 85}, {"Chi", 95}, {"Dung", 80}};

    auto it = m.lower_bound("Bi");
    cout << "\nm.lower_bound(\"Bi\") -> " << it->first << " : " << it->second << endl;

    // Duyet cac khoa >= "C"
    cout << "Cac ten tu \"C\" tro di: ";
    for (auto i = m.lower_bound("C"); i != m.end(); ++i)
        cout << i->first << " ";
    cout << endl;
    return 0;
}
```

Kết quả tham khảo:

```
s.lower_bound()          : 4 ms
std::lower_bound(s.begin()...) : 8500 ms
```

**Chênh lệch hơn 2000 lần!**

**Vì sao:** `std::lower_bound` có độ phức tạp **O(log n) về số phép SO SÁNH**, nhưng nó cần **di chuyển iterator** tới vị trí giữa. Với `vector`, iterator là **random access** — nhảy tới giữa là O(1). Với `set`/`map`, iterator là **bidirectional** — chỉ đi được từng bước, nên việc "nhảy tới giữa" tốn **O(n)**.

**Phương thức `s.lower_bound()`** tận dụng được cấu trúc cây bên trong của `set` → thực sự **O(log n)**.

✅ **Quy tắc quan trọng:**

| Container | Dùng |
|---|---|
| `vector`, `array`, mảng tĩnh, `deque` | `std::lower_bound(v.begin(), v.end(), x)` |
| **`set`, `multiset`, `map`, `multimap`** | **`s.lower_bound(x)`** (phương thức) |
| `list`, `forward_list` | Cả hai đều chậm — nên dùng container khác |

### Bài 13.

```cpp
vector<int> v = {5, 2, 8, 1, 9};              // CHUA SAP XEP!
cout << binary_search(v.begin(), v.end(), 8);
```

**Lỗi: mảng CHƯA được sắp xếp.**

`binary_search` (cũng như `lower_bound`, `upper_bound`) **giả định** dãy đã sắp xếp. Với dãy chưa sắp, kết quả là **không xác định** — có thể trả về `false` dù phần tử thực sự tồn tại, và **không có cảnh báo nào**.

**Quá trình với `{5, 2, 8, 1, 9}` tìm `8`:**

```
trai=0, phai=5 -> giua=2, v[2]=8 == 8 -> tra ve true (may man dung)
```

Nhưng nếu tìm `2`:

```
trai=0, phai=5 -> giua=2, v[2]=8 > 2 -> tim ben TRAI
trai=0, phai=2 -> giua=1, v[1]=2 == 2 -> true (cung may man)
```

Với `{5, 2, 8, 1, 9}` tìm `1`:

```
giua=2, v[2]=8 > 1 -> sang trai
giua=1, v[1]=2 > 1 -> sang trai
giua=0, v[0]=5 > 1 -> sang trai
Het -> FALSE  <- SAI! So 1 co trong mang
```

**Sửa:**

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {5, 2, 8, 1, 9};

    sort(v.begin(), v.end());                 // <- SAP XEP TRUOC

    cout << "Mang sau sap xep: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    cout << boolalpha;
    for (int x : {1, 8, 3}) {
        cout << "binary_search(" << x << ") = "
             << binary_search(v.begin(), v.end(), x) << endl;
    }
    return 0;
}
```

💡 **Cách phòng tránh: luôn kiểm tra trước khi tìm** (ít nhất trong lúc phát triển):

```cpp
assert(is_sorted(v.begin(), v.end()));
```

Hoặc biên dịch với `-D_GLIBCXX_DEBUG` để thư viện tự kiểm tra.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 100000;
    const int SO_TRUY_VAN = 1000000;

    vector<int> v(N);
    for (int i = 0; i < N; i++) v[i] = i * 2;

    set<int>           s(v.begin(), v.end());
    unordered_set<int> us(v.begin(), v.end());

    long long dem;

    // ① find - O(n)
    auto t1 = high_resolution_clock::now();
    dem = 0;
    for (int k = 0; k < SO_TRUY_VAN / 100; k++)              // it hon 100 lan vi qua cham
        if (find(v.begin(), v.end(), k * 7 % (2*N)) != v.end()) dem++;
    auto t2 = high_resolution_clock::now();
    auto tFind = duration_cast<milliseconds>(t2-t1).count() * 100;
    cout << "find (uoc luong)   : " << tFind << " ms" << endl;

    // ② binary_search - O(log n)
    t1 = high_resolution_clock::now();
    dem = 0;
    for (int k = 0; k < SO_TRUY_VAN; k++)
        if (binary_search(v.begin(), v.end(), k * 7 % (2*N))) dem++;
    t2 = high_resolution_clock::now();
    cout << "binary_search      : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ③ set::count - O(log n)
    t1 = high_resolution_clock::now();
    dem = 0;
    for (int k = 0; k < SO_TRUY_VAN; k++)
        dem += s.count(k * 7 % (2*N));
    t2 = high_resolution_clock::now();
    cout << "set::count         : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ④ unordered_set::count - O(1)
    t1 = high_resolution_clock::now();
    dem = 0;
    for (int k = 0; k < SO_TRUY_VAN; k++)
        dem += us.count(k * 7 % (2*N));
    t2 = high_resolution_clock::now();
    cout << "unordered_set::count: " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    return 0;
}
```

Kết quả tham khảo:

```
find (uoc luong)   : 45000 ms
binary_search      : 62 ms
set::count         : 185 ms
unordered_set::count: 38 ms
```

**Bảng so sánh:**

| Phương pháp | Độ phức tạp | Cần sắp xếp | Bộ nhớ | Ghi chú |
|---|---|---|---|---|
| `find` (vector) | O(n) | ❌ Không | Thấp nhất | Chỉ dùng khi n nhỏ |
| **`binary_search`** | O(log n) | ✅ **Có** | Thấp | **Nhanh, tiết kiệm bộ nhớ** |
| `set::count` | O(log n) | Tự sắp | Cao (cây) | Cho phép thêm/xoá O(log n) |
| **`unordered_set::count`** | **O(1)** TB | ❌ Không | Cao (hash) | **Nhanh nhất** |

💡 **`binary_search` trên `vector` nhanh hơn `set::count`** dù cùng O(log n) — vì `vector` lưu dữ liệu **liên tục** (tốt cho CPU cache), còn `set` là cây với các nút rải rác trong bộ nhớ.

✅ **Khuyến nghị:**
- Dữ liệu **cố định**, tra cứu nhiều → `vector` đã sắp + `binary_search`
- Dữ liệu **thay đổi**, cần thứ tự → `set` / `map`
- Dữ liệu **thay đổi**, không cần thứ tự → `unordered_set` / `unordered_map`

### Bài 15.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <limits>
using namespace std;

int main() {
    // Bang nguong xep loai (PHAI sap xep TANG DAN)
    vector<double> nguong  = {0.0, 3.5, 5.0, 6.5, 8.0, 9.0};
    vector<string> xepLoai = {"Kem", "Yeu", "Trung binh", "Kha", "Gioi", "Xuat sac"};

    // Hien bang quy dinh
    cout << "=== BANG QUY DOI XEP LOAI ===" << endl;
    cout << "+----------------+---------------+" << endl;
    cout << "| KHOANG DIEM    | XEP LOAI      |" << endl;
    cout << "+----------------+---------------+" << endl;
    for (size_t i = 0; i < nguong.size(); i++) {
        string khoang;
        if (i + 1 < nguong.size())
            khoang = to_string(nguong[i]).substr(0,3) + " - " +
                     to_string(nguong[i+1]).substr(0,3);
        else
            khoang = to_string(nguong[i]).substr(0,3) + " - 10.0";

        cout << "| " << left << setw(14) << khoang
             << " | " << setw(13) << xepLoai[i] << " |" << endl;
    }
    cout << "+----------------+---------------+" << endl;

    // Tra cuu
    cout << "\nNhap diem de tra cuu (nhap -1 de thoat):" << endl;
    double diem;

    while (true) {
        cout << "\nDiem: ";
        if (!(cin >> diem)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "  -> Nhap khong hop le!" << endl;
            continue;
        }

        if (diem < 0) break;
        if (diem > 10) { cout << "  -> Diem phai tu 0 den 10!" << endl; continue; }

        // upper_bound tra ve nguong DAU TIEN > diem
        // Lui lai 1 buoc -> nguong lon nhat <= diem
        auto it = upper_bound(nguong.begin(), nguong.end(), diem);
        int chiSo = (it - nguong.begin()) - 1;

        if (chiSo < 0) chiSo = 0;

        cout << fixed << setprecision(2);
        cout << "  -> Diem " << diem << " xep loai: "
             << xepLoai[chiSo] << endl;
    }

    cout << "\nTam biet!" << endl;
    return 0;
}
```

Ví dụ chạy:

```
Diem: 8.5
  -> Diem 8.50 xep loai: Gioi

Diem: 9.0
  -> Diem 9.00 xep loai: Xuat sac

Diem: 6.4
  -> Diem 6.40 xep loai: Trung binh

Diem: 0
  -> Diem 0.00 xep loai: Kem
```

**Kỹ thuật "tra bảng ngưỡng" bằng `upper_bound`:**

```
nguong:  0.0   3.5   5.0   6.5   8.0   9.0
index:    0     1     2     3     4     5
loai:   Kem   Yeu   TB    Kha  Gioi  Xuat sac

diem = 8.5:
  upper_bound(8.5) -> tro toi 9.0 (index 5)
  lui 1 buoc -> index 4 -> "Gioi"  ✔
```

💡 **Ưu điểm so với chuỗi `if else if`:**
1. **Độ phức tạp O(log n)** thay vì O(n) — quan trọng khi có hàng trăm mức
2. **Dễ thay đổi:** chỉ cần sửa 2 mảng, không phải sửa logic
3. **Dữ liệu tách khỏi logic** — có thể đọc bảng ngưỡng từ file cấu hình

Kỹ thuật này dùng rất nhiều trong thực tế: tính thuế thu nhập bậc thang, tính cước điện/nước, quy đổi điểm, phân loại BMI…
