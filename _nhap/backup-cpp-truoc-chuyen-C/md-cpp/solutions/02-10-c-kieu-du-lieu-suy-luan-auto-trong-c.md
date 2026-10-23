# Lời giải — [C++]. Kiểu Dữ Liệu Suy Luận Auto Trong C++

[← Quay lại bài học](../02-10-c-kieu-du-lieu-suy-luan-auto-trong-c.md)

> `auto` là tính năng từ **C++11**. Biên dịch với `g++ -std=c++11` trở lên (nên dùng `-std=c++17`).

---

### Bài 1.

```cpp
#include <iostream>
#include <typeinfo>
#include <string>
using namespace std;

int main() {
    auto a = 28;          // int
    auto b = 3.14;        // double
    auto c = 'A';         // char
    auto d = true;        // bool
    auto e = "codelab";   // const char*  (KHONG phai string!)
    auto f = 28LL;        // long long
    auto g = 3.14f;       // float
    auto h = string("codelab");   // string

    cout << "a = " << a << " -> " << typeid(a).name() << endl;
    cout << "b = " << b << " -> " << typeid(b).name() << endl;
    cout << "c = " << c << " -> " << typeid(c).name() << endl;
    cout << "d = " << d << " -> " << typeid(d).name() << endl;
    cout << "e = " << e << " -> " << typeid(e).name() << endl;
    cout << "f = " << f << " -> " << typeid(f).name() << endl;
    cout << "g = " << g << " -> " << typeid(g).name() << endl;
    cout << "h = " << h << " -> " << typeid(h).name() << endl;
    return 0;
}
```

Output (trên g++):

```
a = 28 -> i
b = 3.14 -> d
c = A -> c
d = 1 -> b
e = codelab -> PKc
f = 28 -> x
g = 3.14 -> f
h = codelab -> NSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
```

**Bảng ký hiệu của `typeid().name()` trên GCC:**

| Ký hiệu | Kiểu |
|---|---|
| `i` | `int` |
| `d` | `double` |
| `f` | `float` |
| `c` | `char` |
| `b` | `bool` |
| `x` | `long long` |
| `l` | `long` |
| `PKc` | `const char*` (Pointer to Konst char) |
| `Ss` / chuỗi dài | `std::string` |

⚠️ **Điểm quan trọng:** `auto e = "codelab";` cho kiểu `const char*` chứ **không phải** `std::string`. Vì thế `e.length()` sẽ báo lỗi. Muốn có `string`:

```cpp
auto e = string("codelab");        // hoac
auto e = "codelab"s;               // C++14, can: using namespace std::string_literals;
string e = "codelab";              // don gian nhat
```

Để xem tên kiểu dễ đọc, có thể dùng lệnh:

```bash
./chuongtrinh | c++filt -t
```

### Bài 2.

```cpp
auto x;        // LOI BIEN DICH
```

Thông báo lỗi:

```
error: declaration of 'auto x' has no initializer
```

**Giải thích:** `auto` không phải là "kiểu dữ liệu tự do" — nó là lệnh yêu cầu compiler **suy luận kiểu từ giá trị khởi tạo**. Không có giá trị khởi tạo thì không có gì để suy luận.

Nói cách khác, `auto` được giải quyết **hoàn toàn lúc biên dịch**; sau khi compiler suy ra kiểu, biến đó là kiểu cố định như mọi biến khác. Nó **không** giống `var` của JavaScript hay biến động trong Python.

```cpp
auto x = 10;     // x la int, MAI MAI la int
x = 3.14;        // x = 3 (bi cat thanh int), khong doi thanh double
```

### Bài 3.

```cpp
#include <iostream>
#include <typeinfo>
using namespace std;

int main() {
    auto a = 5 / 2;        // ca hai la int -> chia nguyen -> a la int = 2
    auto b = 5.0 / 2;      // co double -> chia thuc -> b la double = 2.5
    auto c = 5 / 2.0;      // tuong tu -> double = 2.5
    auto d = 5.0f / 2;     // float = 2.5

    cout << "a = " << a << " (" << typeid(a).name() << ")" << endl;
    cout << "b = " << b << " (" << typeid(b).name() << ")" << endl;
    cout << "c = " << c << " (" << typeid(c).name() << ")" << endl;
    cout << "d = " << d << " (" << typeid(d).name() << ")" << endl;
    return 0;
}
```

Output:

```
a = 2 (i)
b = 2.5 (d)
c = 2.5 (d)
d = 2.5 (f)
```

**Bài học quan trọng:** `auto` **không cứu** bạn khỏi bẫy chia nguyên. Nó chỉ suy ra kiểu từ biểu thức — mà biểu thức `5 / 2` vốn đã là phép chia nguyên cho kết quả `int`.

⚠️ Đây là lý do `auto` đôi khi **nguy hiểm** với người mới: bạn không thấy rõ kiểu nên khó phát hiện lỗi này.

### Bài 4.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30, 40, 50};

    // Cach 1: vong for voi chi so
    cout << "Cach 1: ";
    for (int i = 0; i < (int)v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;

    // Cach 2: iterator voi auto
    cout << "Cach 2: ";
    for (auto it = v.begin(); it != v.end(); ++it) {
        cout << *it << " ";        // *it lay GIA TRI ma iterator dang tro toi
    }
    cout << endl;

    // Cach 3: range-based for (NGAN NHAT, NEN DUNG)
    cout << "Cach 3: ";
    for (auto x : v) {
        cout << x << " ";
    }
    cout << endl;

    return 0;
}
```

Cả 3 cách đều in: `10 20 30 40 50`

**So sánh:**

| Cách | Khi nào dùng |
|---|---|
| Chỉ số `v[i]` | Khi cần biết **vị trí** phần tử, hoặc truy cập nhiều mảng song song |
| Iterator | Khi cần dùng với các hàm STL (`insert`, `erase`, `find`), hoặc với container không có chỉ số (`set`, `map`, `list`) |
| Range-based for | **Mặc định** — khi chỉ cần duyệt qua từng phần tử |

Không có `auto`, cách 2 phải viết:

```cpp
for (vector<int>::iterator it = v.begin(); it != v.end(); ++it)
```

Đây chính là lý do `auto` ra đời.

### Bài 5.

```cpp
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main() {
    auto p = make_pair(string("An"), 20);     // pair<string, int>

    cout << "Ten : " << p.first  << endl;
    cout << "Tuoi: " << p.second << endl;

    // Sua gia tri
    p.second = 21;
    cout << "Tuoi moi: " << p.second << endl;

    return 0;
}
```

⚠️ `make_pair("An", 20)` cho kiểu `pair<const char*, int>` chứ không phải `pair<string, int>`. Cần `make_pair(string("An"), 20)` hoặc chỉ rõ kiểu:

```cpp
pair<string, int> p = {"An", 20};        // ro rang nhat
```

### Bài 6.

```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> diem;
    diem["An"]   = 9;
    diem["Binh"] = 8;
    diem["Chi"]  = 10;
    diem["Dung"] = 7;

    // Cach 1: auto voi .first / .second
    cout << "--- Cach 1 ---" << endl;
    for (auto it : diem) {
        cout << it.first << " : " << it.second << endl;
    }

    // Cach 2: structured binding (C++17) - RO RANG NHAT
    cout << "--- Cach 2 (C++17) ---" << endl;
    for (auto [ten, d] : diem) {
        cout << ten << " : " << d << endl;
    }

    // Cach 3: iterator - luu y dung -> thay vi .
    cout << "--- Cach 3 ---" << endl;
    for (auto it = diem.begin(); it != diem.end(); ++it) {
        cout << it->first << " : " << it->second << endl;
    }

    return 0;
}
```

Output (cả 3 cách giống nhau):

```
An : 9
Binh : 8
Chi : 10
Dung : 7
```

**Lưu ý:** `map` **tự động sắp xếp theo khoá tăng dần**, nên kết quả in ra theo thứ tự alphabet chứ không theo thứ tự bạn chèn vào.

Mỗi phần tử của `map` chính là một `pair<const Key, Value>` — đó là lý do dùng được `.first`/`.second`.

### Bài 7.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> v = {"codelab", "cpp", "lap trinh"};

    // ① auto x : v      -> SAO CHEP moi phan tu
    for (auto x : v) {
        x += "!!!";            // chi sua BAN SAO, v khong doi
    }

    // ② auto& x : v     -> THAM CHIEU, khong sao chep, SUA DUOC
    for (auto& x : v) {
        x += "!!!";            // sua THAT vao v
    }

    // ③ const auto& x : v -> THAM CHIEU HANG, khong sao chep, KHONG sua duoc
    for (const auto& x : v) {
        cout << x << endl;     // chi doc
        // x += "?";           // LOI bien dich neu bo comment
    }

    return 0;
}
```

**Bảng so sánh:**

| Cú pháp | Sao chép? | Sửa được `v`? | Dùng khi |
|---|---|---|---|
| `for (auto x : v)` | ✅ **Có** (tốn kém với kiểu lớn) | ❌ Không | Kiểu nhỏ (`int`, `char`, `double`) và chỉ cần đọc |
| `for (auto& x : v)` | ❌ Không | ✅ **Có** | Cần **thay đổi** phần tử |
| `for (const auto& x : v)` | ❌ Không | ❌ Không | Chỉ **đọc** — **an toàn và hiệu quả nhất** |

**Chi phí thực tế:** với `vector<string>` 1 triệu phần tử, mỗi chuỗi dài 100 ký tự:
- `auto x` → sao chép 100 MB dữ liệu → rất chậm
- `const auto&` → không sao chép gì → tức thì

✅ **Quy tắc thực dụng:**
- Kiểu cơ bản (`int`, `double`, `char`, `bool`) → `for (auto x : v)` là được
- Mọi kiểu khác (`string`, `vector`, `pair`, struct) → `for (const auto& x : v)`
- Cần sửa → `for (auto& x : v)`

### Bài 8.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5};

    cout << "Truoc: ";
    for (const auto& x : v) cout << x << " ";
    cout << endl;

    for (auto& x : v) {        // dau & rat quan trong!
        x *= 2;
    }

    cout << "Sau  : ";
    for (const auto& x : v) cout << x << " ";
    cout << endl;

    return 0;
}
```

Output:

```
Truoc: 1 2 3 4 5 
Sau  : 2 4 6 8 10 
```

### Bài 9.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3};
    for (auto x : v) x *= 10;              // KHONG CO TAC DUNG
    for (auto x : v) cout << x << " ";     // in ra: 1 2 3
    return 0;
}
```

**Output: `1 2 3`** — vector không hề thay đổi.

**Giải thích:** `auto x` (không có `&`) tạo ra một **bản sao** của phần tử tại mỗi vòng lặp.

```
Vong 1: x la ban sao cua v[0] -> x = 1, roi x *= 10 -> x = 10
        Het vong lap, x bi huy. v[0] van = 1.
Vong 2: x la ban sao cua v[1] -> x = 2, roi x = 20
        x bi huy. v[1] van = 2.
...
```

**Sửa:** thêm dấu `&` để `x` trở thành **tham chiếu** (một cái tên khác của chính phần tử trong vector):

```cpp
for (auto& x : v) x *= 10;      // v tro thanh {10, 20, 30}
```

Đây là một trong những lỗi phổ biến nhất khi mới dùng range-based for.

### Bài 10.

```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    set<int> s;
    s.insert(50);
    s.insert(10);
    s.insert(30);
    s.insert(10);      // TRUNG -> khong duoc them vao
    s.insert(20);

    cout << "So phan tu: " << s.size() << endl;    // 4 (khong phai 5)

    cout << "Cac phan tu: ";
    for (const auto& x : s) {
        cout << x << " ";
    }
    cout << endl;

    // Kiem tra ton tai
    cout << "Co 30 khong? " << (s.count(30) ? "Co" : "Khong") << endl;
    cout << "Co 99 khong? " << (s.count(99) ? "Co" : "Khong") << endl;

    return 0;
}
```

Output:

```
So phan tu: 4
Cac phan tu: 10 20 30 50 
Co 30 khong? Co
Co 99 khong? Khong
```

**2 đặc điểm cốt lõi của `set`:**
1. **Không chứa phần tử trùng** — chèn giá trị đã có sẽ bị bỏ qua.
2. **Tự động sắp xếp tăng dần** — dù bạn chèn vào theo thứ tự nào.

`set` không truy cập được bằng chỉ số (`s[0]` báo lỗi), nên `auto` với range-based for là cách duyệt tự nhiên nhất.

### Bài 11.

```cpp
#include <iostream>
#include <utility>
#include <vector>
using namespace std;

// Tra ve ca gia tri nho nhat va lon nhat
pair<int, int> timMinMax(const vector<int>& v) {
    int mn = v[0], mx = v[0];
    for (int x : v) {
        if (x < mn) mn = x;
        if (x > mx) mx = x;
    }
    return {mn, mx};
}

int main() {
    vector<int> v = {5, 2, 9, 1, 7};

    // Cach 1: auto
    auto kq = timMinMax(v);
    cout << "Min = " << kq.first << ", Max = " << kq.second << endl;

    // Cach 2: structured binding (C++17) - RO RANG HON HAN
    auto [nhoNhat, lonNhat] = timMinMax(v);
    cout << "Min = " << nhoNhat << ", Max = " << lonNhat << endl;

    return 0;
}
```

Output:

```
Min = 1, Max = 9
Min = 1, Max = 9
```

**Vì sao structured binding tốt hơn:** `kq.first` không nói lên điều gì — người đọc phải quay lại xem hàm trả về gì. `nhoNhat` thì tự giải thích.

Cần biên dịch chuẩn C++17: `g++ -std=c++17 main.cpp -o main`

### Bài 12.

**`auto` KHÔNG làm chương trình chạy chậm hơn một chút nào.**

`auto` được xử lý **hoàn toàn ở giai đoạn biên dịch (compile time)**. Compiler nhìn vào giá trị khởi tạo, suy ra kiểu, rồi thay thế `auto` bằng kiểu cụ thể đó. Sau bước này, hai đoạn code sau tạo ra **mã máy giống hệt nhau**:

```cpp
auto x = 10;        // compiler bien thanh:  int x = 10;
int  x = 10;
```

Chứng minh bằng cách so sánh mã assembly:

```bash
g++ -S -O2 dung_auto.cpp -o dung_auto.s
g++ -S -O2 khong_auto.cpp -o khong_auto.s
diff dung_auto.s khong_auto.s        # khong co khac biet
```

**Phân biệt với các ngôn ngữ khác:**

| | C++ `auto` | Python / JavaScript |
|---|---|---|
| Khi nào xác định kiểu | Lúc **biên dịch** | Lúc **chạy** |
| Kiểu có đổi được không | ❌ Không, cố định vĩnh viễn | ✅ Có |
| Chi phí lúc chạy | **Không có** | Có (phải kiểm tra kiểu mỗi lần) |

Thậm chí `auto` đôi khi còn **nhanh hơn**, vì tránh được ép kiểu ngầm ngoài ý muốn:

```cpp
map<string, int> m;
// Sai: pair<string,int> khac voi pair<const string,int>
//      -> moi vong lap phai TAO BAN SAO va chuyen kieu!
for (const pair<string, int>& p : m) { ... }

// Dung: khong sao chep gi ca
for (const auto& p : m) { ... }
```

### Bài 13.

**✅ 3 trường hợp NÊN dùng `auto`:**

**① Kiểu iterator dài dòng:**

```cpp
// Khong auto:
for (map<string, vector<pair<int,int>>>::const_iterator it = m.begin();
     it != m.end(); ++it) { ... }

// Co auto:
for (auto it = m.begin(); it != m.end(); ++it) { ... }
```

**② Range-based for:**

```cpp
for (const auto& sv : danhSachSinhVien) { ... }
```

**③ Kiểu do thư viện trả về mà bạn không quan tâm tên chính xác:**

```cpp
auto kq = m.insert({"An", 9});       // pair<iterator, bool> - dai dong
auto lambda = [](int x) { return x * x; };   // kieu lambda KHONG THE viet ra
```

**❌ 2 trường hợp KHÔNG nên dùng `auto`:**

**① Khi kiểu là thông tin quan trọng người đọc cần biết:**

```cpp
auto tong = 0;              // int hay long long? -> nguy hiem, de tran so
long long tong = 0;         // RO RANG

auto diem = getDiem();      // int hay double? doc code kho hieu
double diem = getDiem();    // RO RANG
```

**② Khi dễ suy ra kiểu ngoài ý muốn:**

```cpp
auto x = 5 / 2;             // x la int = 2, KHONG phai 2.5!
auto s = "codelab";         // const char*, KHONG phai string -> s.size() loi
auto n = v.size();          // unsigned! -> n - 1 voi v rong = so cuc lon

vector<bool> vb = {true, false};
auto b = vb[0];             // KHONG phai bool ma la mot kieu proxy dac biet!
```

**Nguyên tắc chung:** dùng `auto` khi kiểu **dài và hiển nhiên**; viết rõ kiểu khi kiểu **ngắn và quan trọng**.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <typeinfo>
using namespace std;

int main() {
    int    a = 10;
    double b = 3.14;
    vector<int> v = {1, 2, 3};

    decltype(a) x = 20;          // x co kieu int (giong a)
    decltype(b) y = 2.71;        // y co kieu double
    decltype(v) w = {4, 5, 6};   // w co kieu vector<int>

    // decltype voi BIEU THUC (khong tinh gia tri, chi lay kieu)
    decltype(a + b) z = 0;       // int + double -> double

    cout << "x = " << x << " (" << typeid(x).name() << ")" << endl;
    cout << "y = " << y << " (" << typeid(y).name() << ")" << endl;
    cout << "z = " << z << " (" << typeid(z).name() << ")" << endl;
    cout << "w[0] = " << w[0] << endl;

    return 0;
}
```

**`auto` khác `decltype` thế nào:**

| | `auto` | `decltype` |
|---|---|---|
| Suy kiểu từ | **Giá trị khởi tạo** | **Một biểu thức bất kỳ** |
| Bắt buộc khởi tạo | ✅ Có | ❌ Không |
| Giữ `const`, tham chiếu `&` | ❌ Bỏ đi | ✅ Giữ nguyên |

```cpp
const int  ci = 10;
int&       ri = const_cast<int&>(ci);

auto      a1 = ci;       // int       (mat const)
decltype(ci) d1 = 20;    // const int (giu const)
```

**Ứng dụng chính của `decltype`:** viết template khi chưa biết kiểu trả về:

```cpp
template <typename A, typename B>
auto cong(A a, B b) -> decltype(a + b) {
    return a + b;
}
// cong(1, 2)     -> int
// cong(1, 2.5)   -> double
```

Từ C++14 có thể viết gọn hơn: `auto cong(A a, B b) { return a + b; }`

Với người mới, `decltype` ít dùng — chỉ cần biết nó tồn tại.

### Bài 15.

**Code gốc:**

```cpp
vector<pair<string, vector<int>>> data;
for (vector<pair<string, vector<int>>>::iterator it = data.begin();
     it != data.end(); ++it) {
    cout << it->first << endl;
}
```

**Viết lại từng bước:**

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <utility>
using namespace std;

int main() {
    vector<pair<string, vector<int>>> data = {
        {"An",   {9, 8, 10}},
        {"Binh", {7, 8, 6}},
        {"Chi",  {10, 9, 9}}
    };

    // ① Dung auto cho iterator - da ngan hon nhieu
    for (auto it = data.begin(); it != data.end(); ++it) {
        cout << it->first << endl;
    }

    // ② Range-based for + const auto& - GON VA NHANH NHAT
    for (const auto& muc : data) {
        cout << muc.first << endl;
    }

    // ③ Structured binding (C++17) - RO NGHIA NHAT
    for (const auto& [ten, dsDiem] : data) {
        cout << ten << ": ";
        for (int d : dsDiem) cout << d << " ";
        cout << endl;
    }

    return 0;
}
```

Output của cách ③:

```
An: 9 8 10 
Binh: 7 8 6 
Chi: 10 9 9 
```

**Tiến trình rút gọn:**

```
vector<pair<string, vector<int>>>::iterator it = data.begin()   (60 ky tu)
auto it = data.begin()                                          (22 ky tu)
const auto& muc : data                                          (22 ky tu, ro hon)
const auto& [ten, dsDiem] : data                                (ro nghia nhat)
```

Ngoài chuyện ngắn gọn, cách ② và ③ còn **nhanh hơn** (không sao chép) và **an toàn hơn** (không thể viết sai kiểu iterator, không thể quên `++it` gây lặp vô hạn). Nếu bạn dùng bí danh kiểu thì còn gọn nữa:

```cpp
using SinhVien = pair<string, vector<int>>;
vector<SinhVien> data;
```
