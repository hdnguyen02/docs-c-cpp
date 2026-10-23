# Lời giải — [C++]. Hàm Sort Trong C++

[← Quay lại bài học](../10-02-c-ham-sort-trong-c.md)

> `sort` nằm trong `<algorithm>`, độ phức tạp **O(n log n)** đảm bảo trong mọi trường hợp.

---

### Bài 1.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Mang tinh
    int a[] = {5, 2, 9, 1, 7, 3};
    int n = 6;
    sort(a, a + n);

    cout << "Mang tinh : ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;

    // Vector
    vector<int> v = {5, 2, 9, 1, 7, 3};
    sort(v.begin(), v.end());

    cout << "Vector    : ";
    for (int x : v) cout << x << " ";
    cout << endl;

    // string cung sap xep duoc (theo ky tu)
    string s = "codelab";
    sort(s.begin(), s.end());
    cout << "String    : " << s << endl;      // abcdelo
    return 0;
}
```

💡 **Cú pháp:** `sort(bat_dau, ket_thuc)` — khoảng `[bắt_đầu, kết_thúc)`, **không bao gồm** phần tử cuối.

Với mảng tĩnh: `sort(a, a + n)`. Với container: `sort(v.begin(), v.end())`.

### Bài 2.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
    vector<int> v = {5, 2, 9, 1, 7, 3};

    // Cach 1: greater<int>()
    vector<int> a = v;
    sort(a.begin(), a.end(), greater<int>());
    cout << "greater<int>() : ";
    for (int x : a) cout << x << " ";
    cout << endl;

    // Cach 2: lambda
    vector<int> b = v;
    sort(b.begin(), b.end(), [](int x, int y) { return x > y; });
    cout << "lambda         : ";
    for (int x : b) cout << x << " ";
    cout << endl;

    // Cach 3: sap tang roi dao nguoc iterator
    vector<int> c = v;
    sort(c.rbegin(), c.rend());
    cout << "rbegin/rend    : ";
    for (int x : c) cout << x << " ";
    cout << endl;

    // Cach 4: sap tang roi reverse
    vector<int> d = v;
    sort(d.begin(), d.end());
    reverse(d.begin(), d.end());
    cout << "sort + reverse : ";
    for (int x : d) cout << x << " ";
    cout << endl;
    return 0;
}
```

Tất cả đều cho: `9 7 5 3 2 1`

💡 **Cách 3 (`rbegin/rend`) nhanh nhất** — chỉ một lần duyệt, không cần đảo lại. `greater<int>()` cần `#include <functional>`.

### Bài 3.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};

    cout << "Ban dau       : ";
    for (int x : v) cout << x << " ";
    cout << endl;

    // Chi sap xep tu vi tri 2 den 7 (khong bao gom 8)
    sort(v.begin() + 2, v.begin() + 8);

    cout << "Sap [2, 8)    : ";
    for (size_t i = 0; i < v.size(); i++) {
        if (i == 2 || i == 8) cout << "| ";
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}
```

Output:

```
Ban dau       : 9 8 7 6 5 4 3 2 1 0 
Sap [2, 8)    : 9 8 | 2 3 4 5 6 7 | 1 0 
```

💡 `sort` nhận **hai iterator bất kỳ** — nên sắp xếp được bất kỳ đoạn nào.

### Bài 4.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    vector<string> ds = {"banana", "kiwi", "apple", "fig", "cherry", "date"};

    // Theo thu tu tu dien
    vector<string> a = ds;
    sort(a.begin(), a.end());
    cout << "Tu dien      : ";
    for (const auto& s : a) cout << s << " ";
    cout << endl;

    // Theo DO DAI
    vector<string> b = ds;
    sort(b.begin(), b.end(), [](const string& x, const string& y) {
        return x.length() < y.length();
    });
    cout << "Do dai       : ";
    for (const auto& s : b) cout << s << "(" << s.length() << ") ";
    cout << endl;

    // Do dai, bang nhau thi tu dien
    vector<string> c = ds;
    sort(c.begin(), c.end(), [](const string& x, const string& y) {
        if (x.length() != y.length()) return x.length() < y.length();
        return x < y;
    });
    cout << "Do dai + A-Z : ";
    for (const auto& s : c) cout << s << " ";
    cout << endl;
    return 0;
}
```

Output:

```
Tu dien      : apple banana cherry date fig kiwi 
Do dai       : fig kiwi date apple cherry banana 
Do dai + A-Z : fig date kiwi apple banana cherry 
```

### Bài 5.

```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<int, int>> v = {{3, 1}, {1, 5}, {2, 8}, {1, 2}, {3, 0}};

    sort(v.begin(), v.end());

    cout << "Sap xep mac dinh:" << endl;
    for (const auto& [a, b] : v)
        cout << "  (" << a << ", " << b << ")" << endl;

    // Sap theo phan tu THU HAI
    sort(v.begin(), v.end(), [](const auto& x, const auto& y) {
        return x.second < y.second;
    });
    cout << "\nSap theo second:" << endl;
    for (const auto& [a, b] : v)
        cout << "  (" << a << ", " << b << ")" << endl;
    return 0;
}
```

Output:

```
Sap xep mac dinh:
  (1, 2)
  (1, 5)
  (2, 8)
  (3, 0)
  (3, 1)
```

💡 **`pair` được so sánh theo thứ tự từ điển:** so `first` trước, bằng nhau mới so `second`. Nhờ đó `sort` mặc định đã cho kết quả sắp xếp 2 tiêu chí — không cần comparator.

**Mẹo rất hay dùng:** nếu muốn sắp theo điểm rồi theo tên, hãy để `pair<diem, ten>` thay vì `pair<ten, diem>`.

### Bài 6.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct SinhVien {
    string ten;
    int    tuoi;
    double diem;
};

int main() {
    vector<SinhVien> ds = {
        {"An",    20, 8.5},
        {"Binh",  22, 9.0},
        {"Chi",   21, 7.5},
        {"Dung",  20, 9.0},
        {"Em",    23, 6.5}
    };

    sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
        return a.diem > b.diem;               // GIAM dan theo diem
    });

    cout << fixed << setprecision(2);
    cout << "+------+----------+------+--------+" << endl;
    cout << "| HANG | HO TEN   | TUOI |  DIEM  |" << endl;
    cout << "+------+----------+------+--------+" << endl;
    for (size_t i = 0; i < ds.size(); i++)
        cout << "| " << left  << setw(4) << i + 1
             << " | " << setw(8) << ds[i].ten
             << " | " << right << setw(4) << ds[i].tuoi
             << " | " << setw(6) << ds[i].diem << " |" << endl;
    cout << "+------+----------+------+--------+" << endl;
    return 0;
}
```

### Bài 7.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct SinhVien { string ten; double diem; };

int main() {
    vector<SinhVien> ds = {
        {"Chi",   9.0}, {"An",  9.0}, {"Binh", 8.5},
        {"Dung",  9.0}, {"Em",  8.5}, {"Phong", 7.0}
    };

    sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
        if (a.diem != b.diem) return a.diem > b.diem;    // ① diem GIAM dan
        return a.ten < b.ten;                             // ② ten TANG dan
    });

    cout << fixed << setprecision(1);
    for (const auto& sv : ds)
        cout << left << setw(8) << sv.ten << " : " << sv.diem << endl;
    return 0;
}
```

Output:

```
An       : 9.0
Chi      : 9.0
Dung     : 9.0
Binh     : 8.5
Em       : 8.5
Phong    : 7.0
```

💡 **Mẫu comparator nhiều tiêu chí:**

```cpp
if (tieuChi1(a) != tieuChi1(b)) return tieuChi1(a) < tieuChi1(b);
if (tieuChi2(a) != tieuChi2(b)) return tieuChi2(a) < tieuChi2(b);
return tieuChi3(a) < tieuChi3(b);
```

**Luôn kiểm tra `!=` trước** khi so sánh — nếu không, comparator sẽ sai logic.

💡 Cách viết gọn dùng `tuple`:

```cpp
sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
    return make_tuple(-a.diem, a.ten) < make_tuple(-b.diem, b.ten);
});
```

Dấu `-` để đảo chiều điểm (giảm dần).

### Bài 8.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
    vector<int> v = {-5, 3, -1, 8, -9, 2, -7};

    sort(v.begin(), v.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });

    cout << "Sap theo tri tuyet doi: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    // Bang nhau thi so am truoc
    vector<int> w = {-5, 5, -3, 3, -1, 1};
    sort(w.begin(), w.end(), [](int a, int b) {
        if (abs(a) != abs(b)) return abs(a) < abs(b);
        return a < b;                       // -3 truoc 3
    });
    cout << "Co tieu chi phu       : ";
    for (int x : w) cout << x << " ";
    cout << endl;
    return 0;
}
```

Output:

```
Sap theo tri tuyet doi: -1 2 3 -5 -7 8 -9 
Co tieu chi phu       : -1 1 -3 3 -5 5 
```

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {5, 2, 9, 4, 7, 6, 1, 8, 3};

    sort(v.begin(), v.end(), [](int a, int b) {
        bool chanA = (a % 2 == 0);
        bool chanB = (b % 2 == 0);

        if (chanA != chanB) return chanA;    // chan dung TRUOC le
        return a < b;                         // cung loai -> tang dan
    });

    cout << "Chan truoc, le sau: ";
    for (int x : v) cout << x << " ";
    cout << endl;
    return 0;
}
```

Output:

```
Chan truoc, le sau: 2 4 6 8 1 3 5 7 9 
```

💡 `return chanA;` khi `chanA != chanB` nghĩa là: nếu `a` chẵn (và `b` lẻ) thì `a` đứng trước → trả về `true`.

💡 Cách khác dùng `stable_partition` (chỉ phân nhóm, giữ thứ tự):

```cpp
auto it = stable_partition(v.begin(), v.end(), [](int x){ return x % 2 == 0; });
sort(v.begin(), it);      // sap nhom chan
sort(it, v.end());        // sap nhom le
```

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 1000000;
    const int K = 5;

    vector<int> goc(N);
    for (int i = 0; i < N; i++) goc[i] = (i * 7919 + 13) % N;   // tron ngau nhien

    // ① sort toan bo
    vector<int> a = goc;
    auto t1 = high_resolution_clock::now();
    sort(a.begin(), a.end());
    auto t2 = high_resolution_clock::now();
    cout << "sort toan bo  : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ② partial_sort - chi sap K phan tu dau
    vector<int> b = goc;
    t1 = high_resolution_clock::now();
    partial_sort(b.begin(), b.begin() + K, b.end());
    t2 = high_resolution_clock::now();
    cout << "partial_sort  : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    cout << "\n" << K << " phan tu nho nhat: ";
    for (int i = 0; i < K; i++) cout << b[i] << " ";
    cout << endl;

    cout << "Kiem tra khop voi sort toan bo: ";
    cout << (equal(a.begin(), a.begin() + K, b.begin()) ? "OK" : "SAI") << endl;
    return 0;
}
```

Kết quả tham khảo:

```
sort toan bo  : 62 ms
partial_sort  : 11 ms

5 phan tu nho nhat: 0 1 2 3 4 
Kiem tra khop voi sort toan bo: OK
```

💡 **`partial_sort(first, middle, last)`** chỉ đảm bảo `[first, middle)` được sắp xếp đúng; phần còn lại thứ tự bất kỳ. Độ phức tạp **O(n log k)** thay vì O(n log n).

**Ứng dụng:** bảng xếp hạng top 10 trong hàng triệu người chơi.

### Bài 11.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<int> goc = {7, 10, 4, 3, 20, 15, 8, 1};
    int k = 3;                              // tim phan tu lon THU 3

    // nth_element dat dung phan tu thu k vao vi tri, khong sap xep toan bo
    vector<int> v = goc;
    nth_element(v.begin(), v.begin() + k - 1, v.end(), greater<int>());

    cout << "Mang goc: ";
    for (int x : goc) cout << x << " ";
    cout << endl;

    cout << "Phan tu lon thu " << k << " = " << v[k - 1] << endl;

    cout << "Mang sau nth_element: ";
    for (int x : v) cout << x << " ";
    cout << "  (chi dam bao vi tri " << k-1 << " dung)" << endl;

    // Kiem chung
    vector<int> w = goc;
    sort(w.begin(), w.end(), greater<int>());
    cout << "Kiem chung bang sort: " << w[k - 1] << endl;
    return 0;
}
```

Output:

```
Mang goc: 7 10 4 3 20 15 8 1 
Phan tu lon thu 3 = 10
Mang sau nth_element: 20 15 10 3 4 7 8 1   (chi dam bao vi tri 2 dung)
Kiem chung bang sort: 10
```

💡 **`nth_element` có độ phức tạp O(n) trung bình** — nhanh hơn `sort` (O(n log n)) khi chỉ cần biết phần tử thứ `k`.

**Đảm bảo:** phần tử tại vị trí `k` đúng chỗ; mọi phần tử trước nó ≥ nó, mọi phần tử sau nó ≤ nó (với `greater`).

### Bài 12.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

void bubbleSort(vector<int>& v) {
    int n = v.size();
    for (int i = 0; i < n - 1; i++) {
        bool doiCho = false;
        for (int j = 0; j < n - 1 - i; j++)
            if (v[j] > v[j+1]) { swap(v[j], v[j+1]); doiCho = true; }
        if (!doiCho) break;
    }
}

int main() {
    const int N = 100000;

    vector<int> goc(N);
    for (int i = 0; i < N; i++) goc[i] = (i * 7919 + 13) % N;

    // std::sort
    vector<int> a = goc;
    auto t1 = high_resolution_clock::now();
    sort(a.begin(), a.end());
    auto t2 = high_resolution_clock::now();
    auto tSort = duration_cast<milliseconds>(t2 - t1).count();

    // Bubble Sort
    vector<int> b = goc;
    t1 = high_resolution_clock::now();
    bubbleSort(b);
    t2 = high_resolution_clock::now();
    auto tBubble = duration_cast<milliseconds>(t2 - t1).count();

    cout << "Mang " << N << " phan tu:" << endl;
    cout << "  std::sort   : " << tSort   << " ms" << endl;
    cout << "  Bubble Sort : " << tBubble << " ms" << endl;
    cout << "  Nhanh hon   : " << (double)tBubble / max(1LL, tSort) << " lan" << endl;
    cout << "\nKet qua giong nhau: " << (a == b ? "OK" : "SAI") << endl;
    return 0;
}
```

Kết quả tham khảo (biên dịch `-O2`):

```
Mang 100000 phan tu:
  std::sort   : 6 ms
  Bubble Sort : 8500 ms
  Nhanh hon   : 1416 lan

Ket qua giong nhau: OK
```

**Chênh lệch khổng lồ** — đúng như lý thuyết dự đoán:

| n | O(n²) — Bubble | O(n log n) — sort | Tỉ lệ |
|---|---|---|---|
| 1.000 | 10⁶ | ~10⁴ | 100× |
| 100.000 | 10¹⁰ | ~1,7×10⁶ | ~6.000× |
| 1.000.000 | 10¹² | ~2×10⁷ | ~50.000× |

✅ **Luôn dùng `std::sort`** — chỉ học Bubble/Selection/Insertion để hiểu nguyên lý.

### Bài 13.

**`std::sort` dùng thuật toán INTROSORT** (Introspective Sort) — thuật toán lai kết hợp 3 thuật toán:

```
① QUICKSORT (mac dinh)
      |
      | Neu do sau de quy vuot 2*log2(n)  (dau hieu quicksort bi suy bien)
      v
② HEAPSORT (dam bao O(n log n))

③ INSERTION SORT cho cac doan NHO (< 16 phan tu)
```

| Giai đoạn | Thuật toán | Vì sao |
|---|---|---|
| Chính | **Quicksort** | Nhanh nhất trong thực tế (hằng số nhỏ, tận dụng cache tốt) |
| Dự phòng | **Heapsort** | Quicksort có thể suy biến thành O(n²) với dữ liệu xấu; heapsort **đảm bảo** O(n log n) |
| Đoạn nhỏ | **Insertion Sort** | Với n < 16, insertion sort nhanh hơn quicksort do ít chi phí |

**Đặc điểm của `std::sort`:**

| Tiêu chí | Giá trị |
|---|---|
| Độ phức tạp trung bình | O(n log n) |
| Độ phức tạp xấu nhất | **O(n log n)** (đảm bảo) |
| Bộ nhớ phụ | O(log n) — cho stack đệ quy |
| **Ổn định (stable)?** | ❌ **KHÔNG** |
| Tại chỗ (in-place)? | ✅ Có |

⚠️ **`sort` KHÔNG ổn định** — các phần tử bằng nhau có thể bị đổi thứ tự. Nếu cần giữ thứ tự ban đầu, dùng **`stable_sort`** (xem bài [10-04](../10-04-c-ham-stablesort-trong-c.md)).

**Lịch sử:** Introsort do David Musser đề xuất năm 1997, giải quyết điểm yếu chí mạng của quicksort thuần (có thể bị tấn công bằng dữ liệu cố ý gây suy biến).

### Bài 14.

```cpp
sort(v.begin(), v.end(), [](int a, int b){ return a <= b; });   // CRASH!
```

**Lỗi: comparator không thoả điều kiện "strict weak ordering".**

`sort` yêu cầu hàm so sánh phải là **thứ tự yếu nghiêm ngặt**, trong đó quan trọng nhất là tính **bất phản xạ**:

> `cmp(a, a)` phải luôn trả về **`false`**

Với `a <= b`, khi `a == b` thì `cmp(a, a)` trả về **`true`** → vi phạm.

**Hậu quả:** thuật toán tin rằng luôn có phần tử "nhỏ hơn", nên con trỏ chạy **vượt ra ngoài biên mảng** → truy cập bộ nhớ trái phép → crash hoặc hỏng dữ liệu.

```
Loi thuong gap:
  Segmentation fault (core dumped)
  free(): invalid pointer
```

**Sửa:** bỏ dấu `=`

```cpp
sort(v.begin(), v.end(), [](int a, int b){ return a < b; });    // DUNG
```

**Các lỗi comparator thường gặp khác:**

```cpp
// ❌ SAI: dung <= hoac >=
return a <= b;
return a >= b;

// ❌ SAI: quen kiem tra != o tieu chi dau
if (a.diem < b.diem) return true;
return a.ten < b.ten;              // sai khi diem bang nhau theo huong nguoc

// ✅ DUNG
if (a.diem != b.diem) return a.diem < b.diem;
return a.ten < b.ten;
```

💡 **Cách kiểm tra comparator đúng:** phải thoả 3 tính chất:
1. **Bất phản xạ:** `cmp(a, a) == false`
2. **Phản đối xứng:** nếu `cmp(a,b)` thì `!cmp(b,a)`
3. **Bắc cầu:** nếu `cmp(a,b)` và `cmp(b,c)` thì `cmp(a,c)`

💡 Biên dịch với `-D_GLIBCXX_DEBUG` (GCC) sẽ phát hiện comparator sai:

```bash
g++ -D_GLIBCXX_DEBUG -g main.cpp -o main
# Error: comparison doesn't meet irreflexive requirements
```

### Bài 15.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <limits>
using namespace std;

struct SinhVien {
    string ten;
    int    tuoi;
    double toan, ly, hoa;

    double dtb() const { return (toan + ly + hoa) / 3.0; }
};

void hienThi(const vector<SinhVien>& ds, const string& tieuDe) {
    cout << "\n=== " << tieuDe << " ===" << endl;
    cout << "+-----+------------+------+-------+-------+-------+-------+" << endl;
    cout << "| STT | HO TEN     | TUOI |  TOAN |    LY |   HOA |   DTB |" << endl;
    cout << "+-----+------------+------+-------+-------+-------+-------+" << endl;

    cout << fixed << setprecision(2);
    for (size_t i = 0; i < ds.size(); i++)
        cout << "| " << left  << setw(3) << i + 1
             << " | " << setw(10) << ds[i].ten
             << " | " << right << setw(4) << ds[i].tuoi
             << " | " << setw(5) << ds[i].toan
             << " | " << setw(5) << ds[i].ly
             << " | " << setw(5) << ds[i].hoa
             << " | " << setw(5) << ds[i].dtb() << " |" << endl;
    cout << "+-----+------------+------+-------+-------+-------+-------+" << endl;
}

int main() {
    vector<SinhVien> ds = {
        {"An",    20, 9.0, 8.5, 8.0},
        {"Binh",  22, 7.0, 7.5, 8.0},
        {"Chi",   21, 9.5, 9.0, 9.0},
        {"Dung",  20, 8.0, 8.0, 8.5},
        {"Em",    23, 6.5, 7.0, 6.0},
        {"Phong", 21, 9.0, 8.5, 8.0}
    };

    hienThi(ds, "DANH SACH BAN DAU");

    int chon;
    do {
        cout << "\n====== SAP XEP THEO ======" << endl;
        cout << "1. Ten (A-Z)"                << endl;
        cout << "2. Ten (Z-A)"                << endl;
        cout << "3. Tuoi tang dan"            << endl;
        cout << "4. Diem TB giam dan"         << endl;
        cout << "5. Diem Toan giam dan"       << endl;
        cout << "6. DTB giam, bang thi ten A-Z" << endl;
        cout << "0. Thoat"                    << endl;
        cout << "Lua chon: ";

        if (!(cin >> chon)) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            cout << "Nhap khong hop le!" << endl;
            continue;
        }

        switch (chon) {
            case 1:
                sort(ds.begin(), ds.end(),
                     [](const SinhVien& a, const SinhVien& b){ return a.ten < b.ten; });
                hienThi(ds, "SAP THEO TEN A-Z");
                break;
            case 2:
                sort(ds.begin(), ds.end(),
                     [](const SinhVien& a, const SinhVien& b){ return a.ten > b.ten; });
                hienThi(ds, "SAP THEO TEN Z-A");
                break;
            case 3:
                sort(ds.begin(), ds.end(),
                     [](const SinhVien& a, const SinhVien& b){ return a.tuoi < b.tuoi; });
                hienThi(ds, "SAP THEO TUOI TANG DAN");
                break;
            case 4:
                sort(ds.begin(), ds.end(),
                     [](const SinhVien& a, const SinhVien& b){ return a.dtb() > b.dtb(); });
                hienThi(ds, "SAP THEO DTB GIAM DAN");
                break;
            case 5:
                sort(ds.begin(), ds.end(),
                     [](const SinhVien& a, const SinhVien& b){ return a.toan > b.toan; });
                hienThi(ds, "SAP THEO DIEM TOAN GIAM DAN");
                break;
            case 6:
                sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
                    if (a.dtb() != b.dtb()) return a.dtb() > b.dtb();
                    return a.ten < b.ten;
                });
                hienThi(ds, "DTB GIAM, BANG THI TEN A-Z");
                break;
            case 0:
                cout << "Tam biet!" << endl;
                break;
            default:
                cout << "Lua chon khong hop le!" << endl;
        }
    } while (chon != 0);

    return 0;
}
```

💡 **Điểm thiết kế đáng học:**
1. **Phương thức `dtb()` trong struct** — tính toán gọn, dùng lại được khắp nơi
2. **Mỗi lựa chọn là một lambda riêng** — dễ thêm tiêu chí mới
3. **`const SinhVien&`** trong comparator — tránh sao chép struct mỗi lần so sánh
4. **Xử lý lỗi nhập** với `cin.clear()` + `cin.ignore()`
