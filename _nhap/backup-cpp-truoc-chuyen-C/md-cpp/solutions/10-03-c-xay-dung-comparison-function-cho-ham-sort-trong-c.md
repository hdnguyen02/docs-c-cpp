# Lời giải — [C++]. Xây Dựng Comparison Function Cho Hàm Sort

[← Quay lại bài học](../10-03-c-xay-dung-comparison-function-cho-ham-sort-trong-c.md)

> **Quy tắc vàng:** comparator trả về `true` nếu `a` **phải đứng trước** `b`. Phải thoả "strict weak ordering" — đặc biệt `cmp(a, a)` luôn là `false`.

---

### Bài 1.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Comparison function dang HAM THUONG
bool giamDan(int a, int b) {
    return a > b;
}

int main() {
    vector<int> v = {5, 2, 9, 1, 7};

    sort(v.begin(), v.end(), giamDan);       // truyen TEN HAM, khong co ()

    for (int x : v) cout << x << " ";
    cout << endl;                             // 9 7 5 2 1
    return 0;
}
```

⚠️ Truyền **tên hàm** (`giamDan`), **không** kèm dấu ngoặc — vì ta truyền chính hàm đó, không phải kết quả gọi hàm.

### Bài 2.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool giamDanHam(int a, int b) { return a > b; }

int main() {
    vector<int> v = {5, 2, 9, 1, 7};

    // Cach 1: ham thuong
    vector<int> a = v;
    sort(a.begin(), a.end(), giamDanHam);

    // Cach 2: lambda - dinh nghia NGAY TAI CHO
    vector<int> b = v;
    sort(b.begin(), b.end(), [](int x, int y) { return x > y; });

    // Cach 3: lambda luu vao bien
    auto cmp = [](int x, int y) { return x > y; };
    vector<int> c = v;
    sort(c.begin(), c.end(), cmp);

    cout << "Ham thuong: "; for (int x : a) cout << x << " "; cout << endl;
    cout << "Lambda    : "; for (int x : b) cout << x << " "; cout << endl;
    cout << "Lambda bien: "; for (int x : c) cout << x << " "; cout << endl;
    return 0;
}
```

**So sánh hàm thường vs lambda:**

| Tiêu chí | Hàm thường | Lambda |
|---|---|---|
| Vị trí định nghĩa | Ngoài `main` | **Ngay tại chỗ dùng** |
| Tái sử dụng | ✅ Dễ | Phải lưu vào biến |
| Bắt biến ngoài | ❌ Không | ✅ **Có** (capture) |
| Tốc độ | Có thể qua con trỏ hàm | ✅ Thường được inline |
| Đọc code | Phải nhảy đi tìm | ✅ Thấy ngay logic |

✅ **Lambda là lựa chọn mặc định** trong C++ hiện đại — gọn, rõ, và thường nhanh hơn.

### Bài 3.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// FUNCTOR: struct/class co nap chong operator()
struct GiamDan {
    bool operator()(int a, int b) const {
        return a > b;
    }
};

// Functor CO TRANG THAI - luu them du lieu
struct SapTheoKhoangCach {
    int moc;

    SapTheoKhoangCach(int m) : moc(m) {}

    bool operator()(int a, int b) const {
        return abs(a - moc) < abs(b - moc);
    }
};

int main() {
    vector<int> v = {5, 2, 9, 1, 7};

    vector<int> a = v;
    sort(a.begin(), a.end(), GiamDan());          // chu y co dau ()

    cout << "Functor GiamDan: ";
    for (int x : a) cout << x << " ";
    cout << endl;

    vector<int> b = v;
    sort(b.begin(), b.end(), SapTheoKhoangCach(6));

    cout << "Gan 6 nhat truoc: ";
    for (int x : b) cout << x << " ";
    cout << endl;                                  // 5 7 9 2 1
    return 0;
}
```

**Functor** (đối tượng hàm) là struct/class nạp chồng `operator()` — dùng được như một hàm.

💡 **Ưu điểm so với hàm thường:** functor có thể **lưu trạng thái** (như `moc` ở trên). Trước C++11 đây là cách duy nhất; nay lambda với capture làm được điều tương tự gọn hơn.

💡 `greater<int>()` và `less<int>()` của thư viện chuẩn chính là functor.

### Bài 4.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
using namespace std;

int main() {
    vector<pair<string, int>> ds = {
        {"An", 85}, {"Binh", 92}, {"Chi", 78}, {"Dung", 92}, {"Em", 65}
    };

    sort(ds.begin(), ds.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second) return a.second > b.second;   // diem GIAM
        return a.first < b.first;                                // ten TANG
    });

    cout << "+----------+-------+" << endl;
    cout << "| TEN      | DIEM  |" << endl;
    cout << "+----------+-------+" << endl;
    for (const auto& [ten, diem] : ds)
        cout << "| " << ten << string(9 - ten.length(), ' ')
             << "| " << diem << string(6 - to_string(diem).length(), ' ') << "|" << endl;
    cout << "+----------+-------+" << endl;
    return 0;
}
```

Output:

```
+----------+-------+
| TEN      | DIEM  |
+----------+-------+
| Binh     | 92    |
| Dung     | 92    |
| An       | 85    |
| Chi      | 78    |
| Em       | 65    |
+----------+-------+
```

💡 `const auto&` trong lambda (C++14 trở lên) giúp không phải viết kiểu dài `const pair<string,int>&`.

### Bài 5.

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
        {"Chi",   21, 9.0}, {"An",   20, 9.0}, {"Binh", 22, 9.0},
        {"Dung",  20, 8.5}, {"Em",   23, 8.5}, {"Phong", 19, 7.0}
    };

    sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
        if (a.diem != b.diem) return a.diem > b.diem;    // ① diem GIAM
        if (a.tuoi != b.tuoi) return a.tuoi < b.tuoi;    // ② tuoi TANG
        return a.ten < b.ten;                             // ③ ten A-Z
    });

    cout << fixed << setprecision(1);
    cout << "+------------+------+-------+" << endl;
    cout << "| HO TEN     | TUOI | DIEM  |" << endl;
    cout << "+------------+------+-------+" << endl;
    for (const auto& sv : ds)
        cout << "| " << left  << setw(10) << sv.ten
             << " | " << right << setw(4) << sv.tuoi
             << " | " << setw(5) << sv.diem << " |" << endl;
    cout << "+------------+------+-------+" << endl;
    return 0;
}
```

Output:

```
+------------+------+-------+
| HO TEN     | TUOI | DIEM  |
+------------+------+-------+
| An         |   20 |   9.0 |
| Chi        |   21 |   9.0 |
| Binh       |   22 |   9.0 |
| Dung       |   20 |   8.5 |
| Em         |   23 |   8.5 |
| Phong      |   19 |   7.0 |
+------------+------+-------+
```

💡 Cách viết gọn với `tuple` (tự động so sánh theo thứ tự):

```cpp
sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
    return tie(a.tuoi, a.ten) < tie(b.tuoi, b.ten);      // khi diem bang nhau
});
```

Nhưng với tiêu chí **giảm dần** thì phải đảo dấu, nên cách `if` rõ ràng hơn.

### Bài 6.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int tongChuSo(int n) {
    n = abs(n);
    int tong = 0;
    while (n > 0) { tong += n % 10; n /= 10; }
    return tong;
}

int main() {
    vector<int> v = {123, 45, 9, 78, 11, 500, 99};

    sort(v.begin(), v.end(), [](int a, int b) {
        int ta = tongChuSo(a), tb = tongChuSo(b);
        if (ta != tb) return ta < tb;
        return a < b;                       // cung tong -> gia tri nho truoc
    });

    cout << "Sap theo tong chu so:" << endl;
    for (int x : v)
        cout << "  " << x << "  (tong = " << tongChuSo(x) << ")" << endl;
    return 0;
}
```

Output:

```
Sap theo tong chu so:
  500  (tong = 5)
  123  (tong = 6)
  11   (tong = 2)      <- doi cho: 11 co tong 2, nen dung dau
  ...
```

⚠️ **Vấn đề hiệu năng:** `tongChuSo` được gọi **rất nhiều lần** (O(n log n) lần). Với `n` lớn, nên **tính trước** (decorate-sort-undecorate):

```cpp
vector<pair<int,int>> tam;                  // (tong_chu_so, gia_tri)
for (int x : v) tam.push_back({tongChuSo(x), x});
sort(tam.begin(), tam.end());
for (size_t i = 0; i < v.size(); i++) v[i] = tam[i].second;
```

Cách này gọi `tongChuSo` đúng **n lần** thay vì ~n log n lần.

### Bài 7.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int demNguyenAm(const string& s) {
    int dem = 0;
    for (unsigned char c : s) {
        char t = tolower(c);
        if (t=='a'||t=='e'||t=='i'||t=='o'||t=='u') dem++;
    }
    return dem;
}

int main() {
    vector<string> ds = {"programming", "cpp", "algorithm", "data", "sequence", "xyz"};

    sort(ds.begin(), ds.end(), [](const string& a, const string& b) {
        int na = demNguyenAm(a), nb = demNguyenAm(b);
        if (na != nb) return na > nb;       // nhieu nguyen am truoc
        return a < b;
    });

    cout << "Sap theo so nguyen am (giam dan):" << endl;
    for (const auto& s : ds)
        cout << "  " << s << " (" << demNguyenAm(s) << " nguyen am)" << endl;
    return 0;
}
```

Output:

```
Sap theo so nguyen am (giam dan):
  sequence (4 nguyen am)
  algorithm (3 nguyen am)
  programming (3 nguyen am)
  data (2 nguyen am)
  cpp (0 nguyen am)
  xyz (0 nguyen am)
```

### Bài 8.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
    vector<int> v = {10, 3, 25, 7, 18, 1, 30};
    int moc;

    cout << "Nhap gia tri moc: ";
    cin >> moc;

    // Lambda CAPTURE bien `moc` tu ben ngoai
    sort(v.begin(), v.end(), [moc](int a, int b) {
        int da = abs(a - moc), db = abs(b - moc);
        if (da != db) return da < db;
        return a < b;
    });

    cout << "Sap theo khoang cach toi " << moc << ":" << endl;
    for (int x : v)
        cout << "  " << x << " (cach " << abs(x - moc) << ")" << endl;
    return 0;
}
```

Với `moc = 15`:

```
Sap theo khoang cach toi 15:
  18 (cach 3)
  10 (cach 5)
  7 (cach 8)
  25 (cach 10)
  3 (cach 12)
  30 (cach 15)
  1 (cach 14)
```

**Các kiểu capture của lambda:**

| Cú pháp | Ý nghĩa |
|---|---|
| `[moc]` | Bắt `moc` theo **giá trị** (sao chép) |
| `[&moc]` | Bắt `moc` theo **tham chiếu** |
| `[=]` | Bắt **mọi** biến ngoài theo giá trị |
| `[&]` | Bắt **mọi** biến ngoài theo tham chiếu |
| `[this]` | Bắt con trỏ `this` (trong lớp) |
| `[]` | Không bắt gì |

💡 **Đây là điểm mạnh nhất của lambda so với hàm thường** — hàm thường không truy cập được biến cục bộ bên ngoài.

⚠️ Với comparator, nên capture **theo giá trị** (`[moc]`) để tránh rủi ro biến bị thay đổi trong lúc sắp xếp.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

struct Ngay { int d, m, y; };

Ngay phanTich(const string& s) {
    Ngay n{0, 0, 0};
    char c1, c2;
    istringstream iss(s);
    iss >> n.d >> c1 >> n.m >> c2 >> n.y;
    return n;
}

int main() {
    vector<string> ds = {
        "17/09/2026", "01/01/2025", "25/12/2025",
        "17/09/2025", "03/09/2026", "17/03/2026"
    };

    sort(ds.begin(), ds.end(), [](const string& a, const string& b) {
        Ngay na = phanTich(a), nb = phanTich(b);
        if (na.y != nb.y) return na.y < nb.y;      // NAM truoc
        if (na.m != nb.m) return na.m < nb.m;      // roi THANG
        return na.d < nb.d;                         // roi NGAY
    });

    cout << "Sap xep theo thoi gian:" << endl;
    for (const auto& s : ds) cout << "  " << s << endl;
    return 0;
}
```

Output:

```
Sap xep theo thoi gian:
  01/01/2025
  17/09/2025
  25/12/2025
  17/03/2026
  03/09/2026
  17/09/2026
```

⚠️ **Sắp xếp chuỗi `"dd/mm/yyyy"` trực tiếp sẽ SAI** — vì so sánh từ điển bắt đầu từ ngày. `"01/01/2026"` sẽ đứng trước `"25/12/2025"`.

💡 **Mẹo hay:** nếu định dạng là `"yyyy-mm-dd"` (chuẩn ISO 8601) thì **sắp xếp chuỗi trực tiếp là đúng** — vì thứ tự từ điển trùng với thứ tự thời gian. Đây là lý do nên dùng định dạng này khi lưu trữ.

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <iomanip>
using namespace std;

struct SinhVien {
    string ten;
    double diem;

    // NAP CHONG operator<  -> sort dung duoc ma khong can comparator
    bool operator<(const SinhVien& khac) const {
        if (diem != khac.diem) return diem > khac.diem;   // diem GIAM dan
        return ten < khac.ten;
    }

    bool operator==(const SinhVien& khac) const {
        return ten == khac.ten && diem == khac.diem;
    }
};

int main() {
    vector<SinhVien> ds = {
        {"Chi", 9.0}, {"An", 9.0}, {"Binh", 8.5}, {"Dung", 7.0}
    };

    sort(ds.begin(), ds.end());              // KHONG can comparator!

    cout << fixed << setprecision(1);
    cout << "Sau khi sort (dung operator<):" << endl;
    for (const auto& sv : ds)
        cout << "  " << left << setw(8) << sv.ten << " " << sv.diem << endl;

    // Loi the: dung duoc voi set, map, max_element...
    set<SinhVien> tap(ds.begin(), ds.end());
    cout << "\nDung voi set (tu dong sap xep):" << endl;
    for (const auto& sv : tap)
        cout << "  " << sv.ten << " " << sv.diem << endl;

    auto it = max_element(ds.begin(), ds.end());
    cout << "\nmax_element: " << it->ten << endl;
    return 0;
}
```

💡 **Lợi ích của nạp chồng `operator<`:**
1. `sort(v.begin(), v.end())` hoạt động ngay
2. Dùng được với `set`, `map`, `priority_queue`
3. Dùng được với `min_element`, `max_element`, `binary_search`
4. Toán tử `<`, `>`, `<=`, `>=` đều hoạt động

⚠️ **Chỉ nên nạp chồng `operator<` khi có một thứ tự "tự nhiên" duy nhất** cho kiểu đó. Nếu cần nhiều cách sắp xếp khác nhau, dùng comparator riêng cho từng trường hợp.

⚠️ Nhớ đánh dấu `const` cho phương thức — nếu không, `sort` với `const` container sẽ báo lỗi.

### Bài 11.

```cpp
auto c1 = [](int a, int b){ return a < b; };        // ✅ DUNG
auto c2 = [](int a, int b){ return a <= b; };       // ❌ SAI
auto c3 = [](int a, int b){ return abs(a) < abs(b); };  // ✅ DUNG
auto c4 = [](int a, int b){ return true; };         // ❌ SAI
```

**Phân tích từng comparator:**

| | Bất phản xạ<br>`cmp(a,a) == false` | Phản đối xứng | Bắc cầu | Kết luận |
|---|---|---|---|---|
| `c1: a < b` | ✅ `a < a` = false | ✅ | ✅ | **ĐÚNG** |
| `c2: a <= b` | ❌ `a <= a` = **true** | ❌ | ✅ | **SAI → CRASH** |
| `c3: |a| < |b|` | ✅ | ✅ | ✅ | **ĐÚNG** |
| `c4: true` | ❌ `cmp(a,a)` = **true** | ❌ | — | **SAI → CRASH** |

**`c2` sai vì:** khi `a == b`, nó nói "a đứng trước b" **và** "b đứng trước a" — mâu thuẫn. Thuật toán tin rằng luôn còn phần tử nhỏ hơn nên chạy vượt biên mảng → **segmentation fault**.

**`c4` sai vì:** nó nói mọi phần tử đều đứng trước mọi phần tử khác, kể cả chính nó.

**Ghi chú về `c3`:** đúng về mặt "strict weak ordering", nhưng lưu ý các phần tử có cùng trị tuyệt đối (`-5` và `5`) được coi là "tương đương" — thứ tự giữa chúng không đảm bảo.

💡 **Cách kiểm tra nhanh một comparator:** hỏi *"cmp(x, x) có trả về false không?"* — nếu không, comparator sai.

### Bài 12.

```cpp
#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    map<string, int> diem = {
        {"An", 85}, {"Binh", 92}, {"Chi", 78},
        {"Dung", 92}, {"Em", 65}, {"Phong", 88}
    };

    cout << "=== MAP GOC (sap theo KHOA) ===" << endl;
    for (const auto& [ten, d] : diem)
        cout << "  " << left << setw(8) << ten << " : " << d << endl;

    // Chuyen sang vector de sap theo GIA TRI
    vector<pair<string, int>> ds(diem.begin(), diem.end());

    sort(ds.begin(), ds.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second) return a.second > b.second;   // diem GIAM
        return a.first < b.first;                                // ten A-Z
    });

    cout << "\n=== SAU KHI SAP THEO GIA TRI ===" << endl;
    for (size_t i = 0; i < ds.size(); i++)
        cout << "  " << i + 1 << ". " << left << setw(8) << ds[i].first
             << " : " << ds[i].second << endl;
    return 0;
}
```

Output:

```
=== MAP GOC (sap theo KHOA) ===
  An       : 85
  Binh     : 92
  Chi      : 78
  Dung     : 92
  Em       : 65
  Phong    : 88

=== SAU KHI SAP THEO GIA TRI ===
  1. Binh     : 92
  2. Dung     : 92
  3. Phong    : 88
  4. An       : 85
  5. Chi      : 78
  6. Em       : 65
```

⚠️ **Không thể `sort` trực tiếp một `map`** — vì `map` luôn tự giữ thứ tự theo khoá (nó là cây cân bằng bên trong). Bắt buộc phải đổ sang `vector` rồi sắp xếp.

💡 Mẫu **"map → vector → sort"** này rất thường dùng trong các bài đếm tần suất rồi xếp hạng.

### Bài 13.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    vector<string> ds = {"banana", "apple", "cherry", "date", "fig", "grape"};

    // Danh sach uu tien - cac tu nay phai dung TRUOC
    set<string> uuTien = {"cherry", "fig"};

    sort(ds.begin(), ds.end(), [&uuTien](const string& a, const string& b) {
        bool ua = uuTien.count(a) > 0;
        bool ub = uuTien.count(b) > 0;

        if (ua != ub) return ua;         // uu tien dung truoc
        return a < b;                     // cung nhom -> A-Z
    });

    cout << "Sau khi sap xep uu tien:" << endl;
    for (const auto& s : ds)
        cout << "  " << s << (uuTien.count(s) ? "  <- UU TIEN" : "") << endl;
    return 0;
}
```

Output:

```
Sau khi sap xep uu tien:
  cherry  <- UU TIEN
  fig  <- UU TIEN
  apple
  banana
  date
  grape
```

💡 **Kỹ thuật `return ua;` khi `ua != ub`:** nếu `a` thuộc nhóm ưu tiên (và `b` không), trả về `true` nghĩa là `a` đứng trước.

💡 Lambda capture `[&uuTien]` theo tham chiếu để tránh sao chép cả `set`.

**Mở rộng — nhiều mức ưu tiên:**

```cpp
map<string, int> mucUuTien = {{"cherry", 1}, {"fig", 1}, {"apple", 2}};

sort(ds.begin(), ds.end(), [&](const string& a, const string& b) {
    int ma = mucUuTien.count(a) ? mucUuTien[a] : 999;
    int mb = mucUuTien.count(b) ? mucUuTien[b] : 999;
    if (ma != mb) return ma < mb;
    return a < b;
});
```

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

// ① Ham thuong
bool cmpHam(int a, int b) { return a < b; }

// ② Functor
struct CmpFunctor {
    bool operator()(int a, int b) const { return a < b; }
};

int main() {
    const int N = 1000000;
    vector<int> goc(N);
    for (int i = 0; i < N; i++) goc[i] = (i * 7919 + 13) % N;

    // ① Ham thuong
    vector<int> a = goc;
    auto t1 = high_resolution_clock::now();
    sort(a.begin(), a.end(), cmpHam);
    auto t2 = high_resolution_clock::now();
    cout << "① Ham thuong : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ② Lambda
    vector<int> b = goc;
    t1 = high_resolution_clock::now();
    sort(b.begin(), b.end(), [](int x, int y) { return x < y; });
    t2 = high_resolution_clock::now();
    cout << "② Lambda     : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ③ Functor
    vector<int> c = goc;
    t1 = high_resolution_clock::now();
    sort(c.begin(), c.end(), CmpFunctor());
    t2 = high_resolution_clock::now();
    cout << "③ Functor    : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ④ Mac dinh (khong comparator)
    vector<int> d = goc;
    t1 = high_resolution_clock::now();
    sort(d.begin(), d.end());
    t2 = high_resolution_clock::now();
    cout << "④ Mac dinh   : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    cout << "\nKet qua giong nhau: "
         << boolalpha << (a == b && b == c && c == d) << endl;
    return 0;
}
```

Kết quả tham khảo (`-O2`):

```
① Ham thuong : 71 ms
② Lambda     : 62 ms
③ Functor    : 62 ms
④ Mac dinh   : 62 ms

Ket qua giong nhau: true
```

**Nhận xét:**

| Cách | Tốc độ | Vì sao |
|---|---|---|
| Hàm thường | Chậm hơn ~15% | Truyền qua **con trỏ hàm** → compiler khó inline |
| **Lambda** | ✅ Nhanh nhất | Mỗi lambda là một **kiểu riêng** → inline hoàn toàn |
| **Functor** | ✅ Nhanh nhất | Cũng là kiểu riêng → inline |
| Mặc định | ✅ Nhanh nhất | Dùng `less<int>` — cũng là functor |

💡 **Lý do sâu xa:** lambda và functor có **kiểu riêng biệt** tại thời điểm biên dịch, nên compiler biết chính xác gọi hàm nào và có thể nội tuyến (inline). Con trỏ hàm chỉ được biết lúc chạy.

⚠️ Chênh lệch chỉ ~15% và thường không đáng kể — nhưng đây là lý do kỹ thuật để **ưu tiên lambda**.

### Bài 15.

**File `comparators.h`:**

```cpp
#pragma once
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <sstream>

namespace cmp {

// ============ SO HOC ============

/** @brief Tang dan (mac dinh). */
inline auto tangDan = [](const auto& a, const auto& b) { return a < b; };

/** @brief Giam dan. */
inline auto giamDan = [](const auto& a, const auto& b) { return a > b; };

/** @brief Theo tri tuyet doi tang dan. */
inline auto theoTriTuyetDoi = [](long long a, long long b) {
    long long da = std::llabs(a), db = std::llabs(b);
    if (da != db) return da < db;
    return a < b;
};

/** @brief Chan truoc, le sau; moi nhom tang dan. */
inline auto chanTruoc = [](long long a, long long b) {
    bool ca = (a % 2 == 0), cb = (b % 2 == 0);
    if (ca != cb) return ca;
    return a < b;
};

/** @brief Theo tong chu so tang dan. */
inline int tongChuSo(long long n) {
    n = std::llabs(n);
    int t = 0;
    while (n > 0) { t += n % 10; n /= 10; }
    return t;
}

inline auto theoTongChuSo = [](long long a, long long b) {
    int ta = tongChuSo(a), tb = tongChuSo(b);
    if (ta != tb) return ta < tb;
    return a < b;
};

// ============ CHUOI ============

/** @brief Theo do dai tang dan, bang nhau thi A-Z. */
inline auto theoDoDai = [](const std::string& a, const std::string& b) {
    if (a.length() != b.length()) return a.length() < b.length();
    return a < b;
};

/** @brief Khong phan biet hoa/thuong. */
inline std::string toLower(std::string s) {
    std::transform(s.begin(), s.end(), s.begin(),
                   [](unsigned char c) { return std::tolower(c); });
    return s;
}

inline auto khongPhanBietHoaThuong = [](const std::string& a, const std::string& b) {
    std::string la = toLower(a), lb = toLower(b);
    if (la != lb) return la < lb;
    return a < b;
};

/** @brief Sap xep "tu nhien": file2 truoc file10. */
inline auto tuNhien = [](const std::string& a, const std::string& b) {
    size_t i = 0, j = 0;
    while (i < a.length() && j < b.length()) {
        if (std::isdigit((unsigned char)a[i]) && std::isdigit((unsigned char)b[j])) {
            size_t i2 = i, j2 = j;
            while (i2 < a.length() && std::isdigit((unsigned char)a[i2])) i2++;
            while (j2 < b.length() && std::isdigit((unsigned char)b[j2])) j2++;
            long long va = std::stoll(a.substr(i, i2 - i));
            long long vb = std::stoll(b.substr(j, j2 - j));
            if (va != vb) return va < vb;
            i = i2; j = j2;
        } else {
            if (a[i] != b[j]) return a[i] < b[j];
            i++; j++;
        }
    }
    return a.length() < b.length();
};

// ============ TAO COMPARATOR DONG ============

/** @brief Tao comparator sap theo khoang cach toi mot moc. */
inline auto theoKhoangCach(long long moc) {
    return [moc](long long a, long long b) {
        long long da = std::llabs(a - moc), db = std::llabs(b - moc);
        if (da != db) return da < db;
        return a < b;
    };
}

/** @brief Dao chieu mot comparator bat ky. */
template <typename Cmp>
auto daoChieu(Cmp c) {
    return [c](const auto& a, const auto& b) { return c(b, a); };
}

} // namespace cmp
```

**File `main.cpp` — kiểm thử:**

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include "comparators.h"
using namespace std;

template <typename T>
void in(const string& nhan, const vector<T>& v) {
    cout << nhan << ": ";
    for (const auto& x : v) cout << x << " ";
    cout << endl;
}

int main() {
    vector<long long> so = {-5, 3, 12, -8, 7, 21, -1, 100};

    auto a = so; sort(a.begin(), a.end(), cmp::tangDan);
    in("Tang dan      ", a);

    auto b = so; sort(b.begin(), b.end(), cmp::giamDan);
    in("Giam dan      ", b);

    auto c = so; sort(c.begin(), c.end(), cmp::theoTriTuyetDoi);
    in("Tri tuyet doi ", c);

    auto d = so; sort(d.begin(), d.end(), cmp::chanTruoc);
    in("Chan truoc    ", d);

    auto e = so; sort(e.begin(), e.end(), cmp::theoTongChuSo);
    in("Tong chu so   ", e);

    auto f = so; sort(f.begin(), f.end(), cmp::theoKhoangCach(10));
    in("Gan 10 nhat   ", f);

    auto g = so; sort(g.begin(), g.end(), cmp::daoChieu(cmp::theoTriTuyetDoi));
    in("Tri tđ nguoc  ", g);

    cout << endl;
    vector<string> chuoi = {"file10", "File2", "banana", "fig", "file1"};

    auto h = chuoi; sort(h.begin(), h.end(), cmp::theoDoDai);
    in("Theo do dai   ", h);

    auto i = chuoi; sort(i.begin(), i.end(), cmp::khongPhanBietHoaThuong);
    in("Khong pb hoa  ", i);

    auto j = chuoi; sort(j.begin(), j.end(), cmp::tuNhien);
    in("Tu nhien      ", j);

    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp -o cmp
./cmp
```

💡 **Điểm thiết kế đáng học:**
1. **Gói trong `namespace cmp`** — tránh xung đột tên, gọi rõ nghĩa `cmp::giamDan`
2. **`inline auto`** cho biến lambda ở header (C++17) — tránh lỗi định nghĩa trùng khi include nhiều nơi
3. **`theoKhoangCach(moc)` là hàm trả về lambda** — tạo comparator động theo tham số
4. **`daoChieu` là template** — biến bất kỳ comparator nào thành chiều ngược lại
