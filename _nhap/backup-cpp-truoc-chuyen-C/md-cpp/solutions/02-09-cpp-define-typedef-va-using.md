# Lời giải — [C++]. Define, Typedef Và Using

[← Quay lại bài học](../02-09-cpp-define-typedef-va-using.md)

---

### Bài 1.

```cpp
#include <iostream>
#include <utility>
#include <iomanip>
using namespace std;

typedef long long        ll;
typedef long double      ld;
typedef pair<int, int>   ii;

int main() {
    ll n = 9123456789012345LL;
    ld x = 3.141592653589793238L;
    ii p = {10, 20};

    cout << "ll : " << n << endl;
    cout << "ld : " << fixed << setprecision(15) << x << endl;
    cout << "ii : " << p.first << " " << p.second << endl;
    return 0;
}
```

Output:

```
ll : 9123456789012345
ld : 3.141592653589793
ii : 10 20
```

### Bài 2.

```cpp
#include <iostream>
#include <utility>
#include <iomanip>
using namespace std;

using ll = long long;
using ld = long double;
using ii = pair<int, int>;

int main() {
    ll n = 9123456789012345LL;
    ld x = 3.141592653589793238L;
    ii p = {10, 20};

    cout << "ll : " << n << endl;
    cout << "ld : " << fixed << setprecision(15) << x << endl;
    cout << "ii : " << p.first << " " << p.second << endl;
    return 0;
}
```

**So sánh cú pháp:**

```cpp
typedef long long ll;        // kieu_cu  ten_moi
using   ll = long long;      // ten_moi = kieu_cu   <- de doc hon, giong phep gan
```

`using` dễ đọc hơn rõ rệt khi kiểu phức tạp:

```cpp
typedef int (*HamXuLy)(int, int);          // <- ten nam GIUA, rat kho doc
using   HamXuLy = int (*)(int, int);       // <- ten nam dau, ro rang
```

**Từ C++11 trở đi nên dùng `using`** — nó làm được mọi việc `typedef` làm, và còn dùng được với template (`typedef` không làm được).

### Bài 3.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

#define PI  3.14159
#define INF 1000000000
#define MOD 1000000007

int main() {
    cout << fixed << setprecision(5);
    cout << "PI  = " << PI  << endl;
    cout << "INF = " << INF << endl;
    cout << "MOD = " << MOD << endl;
    return 0;
}
```

Output:

```
PI  = 3.14159
INF = 1000000000
MOD = 1000000007
```

**Ý nghĩa thực tế:**
- `INF` = "vô cùng lớn" — dùng khi tìm giá trị nhỏ nhất: `int min = INF;`. Chọn 10⁹ vì nó nhỏ hơn giới hạn `int` (≈2,1×10⁹) nên `INF + INF` chưa tràn.
- `MOD = 10⁹+7` — số nguyên tố hay dùng trong các bài đếm kết quả rất lớn, phải lấy dư.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

#define PI_DEFINE 3.14159
const double PI_CONST = 3.14159;

int main() {
    double r = 5.0;
    cout << "Dung #define : " << PI_DEFINE * r * r << endl;
    cout << "Dung const   : " << PI_CONST  * r * r << endl;
    return 0;
}
```

**So sánh — `const` tốt hơn hẳn:**

| Tiêu chí | `#define PI 3.14159` | `const double PI = 3.14159;` |
|---|---|---|
| Ai xử lý | Preprocessor — **thay thế văn bản mù quáng** trước khi biên dịch | Compiler — là một biến thực sự |
| Có kiểu dữ liệu | ❌ Không. Chỉ là dãy ký tự | ✅ Có (`double`) |
| Kiểm tra kiểu | ❌ Không | ✅ Có |
| Debug được | ❌ Không. Debugger không biết `PI` là gì | ✅ Có, xem được giá trị |
| Tôn trọng phạm vi (scope) | ❌ Không — có hiệu lực tới cuối file, kể cả bên trong hàm/lớp khác | ✅ Có |
| Thông báo lỗi | Khó hiểu (hiện giá trị thay vì tên) | Rõ ràng |

Ví dụ `#define` gây lỗi khó hiểu:

```cpp
#define MAX 100
int main() {
    int MAX = 5;        // -> bi thay thanh: int 100 = 5;
    // error: expected unqualified-id before numeric constant
}
```

✅ **Kết luận: trong C++ hiện đại, luôn dùng `const`/`constexpr` thay cho `#define` để định nghĩa hằng số.** `#define` chỉ nên dùng cho biên dịch có điều kiện (`#ifdef`) và header guard.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)

int main() {
    FOR(i, 1, 10) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```

Output: `1 2 3 4 5 6 7 8 9 10`

**Lưu ý quan trọng:** phải bọc `(a)` và `(b)` trong ngoặc. Nếu viết `for(int i = a; i <= b; i++)` thì khi gọi `FOR(i, 1, n-1)` sẽ thành `i <= n-1` — may mắn là đúng; nhưng `FOR(i, 1, n&1)` sẽ hỏng do thứ tự ưu tiên toán tử.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() {
    cout << MAX(3, 7)     << endl;     // 7
    cout << MAX(2 + 3, 4) << endl;     // 5
    return 0;
}
```

Output:

```
7
5
```

**Vì sao phải bọc ngoặc khắp nơi:** nếu viết `#define MAX(a,b) a > b ? a : b` thì:

```cpp
cout << MAX(2 + 3, 4) << endl;
// bi thay thanh:  cout << 2 + 3 > 4 ? 2 + 3 : 4 << endl;
// toan tu << co do uu tien CAO hon ?: -> bieu thuc bi hieu sai hoan toan
```

✅ **Trong C++ hiện đại, dùng `std::max` thay vì macro:**

```cpp
#include <algorithm>
cout << max(2 + 3, 4);      // an toan, co kiem tra kieu
```

### Bài 7.

```cpp
#include <iostream>
using namespace std;

#define BINH_PHUONG(x) x * x

int main() {
    cout << BINH_PHUONG(2 + 3) << endl;
    return 0;
}
```

**Output: `11`** (kỳ vọng là 25)

**Giải thích:** macro hoạt động bằng **thay thế văn bản thuần tuý**, không hiểu gì về toán học:

```
BINH_PHUONG(2 + 3)
    -> thay x boi chuoi "2 + 3"
    -> 2 + 3 * 2 + 3
    -> 2 + 6 + 3          (nhan truoc cong sau!)
    -> 11
```

Đây là bẫy kinh điển nhất của macro.

### Bài 8.

**Sửa bằng cách bọc ngoặc đầy đủ:**

```cpp
#define BINH_PHUONG(x) ((x) * (x))

cout << BINH_PHUONG(2 + 3) << endl;
// -> ((2 + 3) * (2 + 3)) -> 5 * 5 -> 25   ✔
```

**Nhưng vẫn còn vấn đề — tác dụng phụ (side effect):**

```cpp
int i = 3;
cout << BINH_PHUONG(i++) << endl;
// -> ((i++) * (i++))
// -> i BI TANG HAI LAN! Ket qua la 3 * 4 = 12 (khong phai 9), va i = 5
```

Ngoài ra kết quả còn là *undefined behavior* vì `i` bị sửa 2 lần trong cùng một biểu thức.

✅ **Giải pháp đúng trong C++: dùng hàm inline hoặc template**

```cpp
// Cach 1: ham thuong
int binhPhuong(int x) { return x * x; }

// Cach 2: template - dung duoc cho moi kieu so
template <typename T>
T binhPhuong(T x) { return x * x; }

// Cach 3: constexpr (C++11) - tinh luon luc bien dich neu co the
constexpr int binhPhuong(int x) { return x * x; }

int i = 3;
cout << binhPhuong(i++);   // 9 dung, i chi tang 1 lan
```

**Hàm có ưu điểm gì so với macro:** tham số chỉ được tính **một lần**, có kiểm tra kiểu, debug được, tôn trọng phạm vi, và compiler vẫn tối ưu (inline) nên không chậm hơn.

### Bài 9.

| Tiêu chí | `#define` | `typedef` | `using` (C++11) | `const` |
|---|---|---|---|---|
| **Ai xử lý** | Preprocessor (trước biên dịch) | Compiler | Compiler | Compiler |
| **Bản chất** | Thay thế văn bản | Tạo bí danh cho kiểu | Tạo bí danh cho kiểu | Tạo biến chỉ đọc |
| **Kiểm tra kiểu** | ❌ Không | ✅ Có | ✅ Có | ✅ Có |
| **Kết thúc bằng `;`** | ❌ Không | ✅ Có | ✅ Có | ✅ Có |
| **Bắt đầu bằng `#`** | ✅ Có | ❌ Không | ❌ Không | ❌ Không |
| **Tôn trọng scope** | ❌ Không (tới cuối file) | ✅ Có | ✅ Có | ✅ Có |
| **Dùng cho hằng số** | ⚠️ Được nhưng **không nên** | ❌ Không | ❌ Không | ✅ **Nên dùng** |
| **Dùng cho kiểu dữ liệu** | ⚠️ Được nhưng không nên | ✅ Được | ✅ **Nên dùng** | ❌ Không |
| **Dùng cho câu lệnh/macro hàm** | ✅ Được (cẩn thận!) | ❌ Không | ❌ Không | ❌ Không |
| **Dùng được với template** | — | ❌ Không | ✅ **Có** | — |
| **Debug được** | ❌ Không | ✅ Có | ✅ Có | ✅ Có |

**Tóm tắt nên dùng gì:**
- Hằng số → `const` / `constexpr`
- Bí danh kiểu → `using`
- Thay hàm ngắn → hàm `inline` / `template`
- `#define` → chỉ dùng cho `#ifdef` (biên dịch có điều kiện) và header guard

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

#define pb      push_back
#define all(v)  (v).begin(), (v).end()
#define fi      first
#define se      second

typedef pair<int, int> ii;

int main() {
    vector<int> v;
    v.pb(5);  v.pb(2);  v.pb(9);  v.pb(1);

    sort(all(v));                          // = sort(v.begin(), v.end())

    for (int x : v) cout << x << " ";
    cout << endl;

    ii p = {10, 20};
    cout << p.fi << " " << p.se << endl;   // = p.first, p.second
    return 0;
}
```

Output:

```
1 2 5 9
10 20
```

⚠️ **Nhớ bọc ngoặc `(v)` trong `all(v)`** — nếu không, `all(v1 + v2)` sẽ hỏng.

⚠️ Đây là phong cách **chỉ dành cho lập trình thi đấu** — nơi bạn code một mình, code xong vứt, và mỗi giây gõ phím đều quý. **Tuyệt đối không dùng trong dự án thật hay bài tập nộp thầy cô**, vì người khác đọc sẽ rất khổ.

### Bài 11.

```cpp
typedef 3.14 PI;      // LOI BIEN DICH
```

Thông báo lỗi:

```
error: expected unqualified-id before numeric constant
```

**Giải thích:** `typedef` **chỉ đặt bí danh cho KIỂU DỮ LIỆU**, không đặt tên cho giá trị. `3.14` là một giá trị (literal), không phải kiểu.

So sánh:

```cpp
typedef double SoThuc;        // DUNG: dat ten cho KIEU double
typedef 3.14 PI;              // SAI:  3.14 khong phai mot kieu

#define PI 3.14               // DUOC (define thay the van ban bat ky)
const double PI = 3.14;       // DUNG NHAT
```

Đây chính là điểm khác biệt cốt lõi trong bảng ở bài 9: `#define` thay thế **bất kỳ chuỗi ký tự nào**, còn `typedef`/`using` chỉ làm việc với **kiểu**.

### Bài 12.

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

using Matrix = vector<vector<int>>;

int main() {
    Matrix m = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    for (const auto& hang : m) {
        for (int x : hang) {
            cout << setw(4) << x;
        }
        cout << endl;
    }
    return 0;
}
```

Output:

```
   1   2   3
   4   5   6
   7   8   9
```

**Lợi ích rõ nhất của bí danh kiểu** chính là ở những kiểu dài như thế này:

```cpp
// Khong co bi danh - dai va kho doc
vector<vector<int>> nhanMaTran(const vector<vector<int>>& a,
                               const vector<vector<int>>& b);

// Co bi danh - ro rang
Matrix nhanMaTran(const Matrix& a, const Matrix& b);
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

#define DEBUG          // <- xoa hoac comment dong nay de TAT che do debug

#ifdef DEBUG
    #define LOG(x) cout << "[DEBUG] " << #x << " = " << (x) << endl
#else
    #define LOG(x)     // khi khong debug, LOG(x) bien thanh rong -> khong ton gi
#endif

int main() {
    int a = 10, b = 3;
    int tong = a + b;

    LOG(a);
    LOG(b);
    LOG(tong);
    LOG(a * b);

    cout << "Ket qua: " << tong << endl;
    return 0;
}
```

Khi **có** `#define DEBUG`:

```
[DEBUG] a = 10
[DEBUG] b = 3
[DEBUG] tong = 13
[DEBUG] a * b = 30
Ket qua: 13
```

Khi **xoá** dòng `#define DEBUG`: chỉ in `Ket qua: 13`.

**Các chỉ thị tiền xử lý có điều kiện:**

| Chỉ thị | Ý nghĩa |
|---|---|
| `#ifdef X` | Biên dịch đoạn sau nếu `X` **đã** được define |
| `#ifndef X` | Biên dịch nếu `X` **chưa** được define |
| `#if <bieu thuc>` | Biên dịch nếu biểu thức khác 0 |
| `#else`, `#elif` | Nhánh thay thế |
| `#endif` | Kết thúc khối điều kiện |

**Toán tử `#x`** (stringize) biến tên biến thành chuỗi — nhờ nó mà `LOG(tong)` in ra được cả chữ `"tong"`.

**Ứng dụng phổ biến nhất — header guard** (chống include trùng lặp):

```cpp
// file mylib.h
#ifndef MYLIB_H
#define MYLIB_H

// noi dung header...

#endif
```

Bạn cũng có thể bật/tắt DEBUG **từ dòng lệnh** mà không sửa code:

```bash
g++ -DDEBUG main.cpp -o main      # bat debug
g++ main.cpp -o main              # tat debug
```

### Bài 14.

```cpp
/*
 * ============================================================
 *  Template thi dau (competitive programming)
 *  Luu y: phong cach nay CHI dung khi code mot minh trong ky thi.
 * ============================================================
 */
#include <bits/stdc++.h>     // include TAT CA thu vien chuan (chi co tren GCC)
using namespace std;

// ---------- Bi danh kieu ----------
using ll  = long long;               // so nguyen lon, tranh tran khi n^2 > 2 ty
using ull = unsigned long long;
using ld  = long double;             // do chinh xac cao hon double
using ii  = pair<int, int>;          // cap so nguyen: toa do, canh do thi...
using vi  = vector<int>;
using vll = vector<ll>;

// ---------- Hang so ----------
const int  INF = 1e9 + 7;            // "vo cung" cho kieu int (khong tran khi cong 2 lan)
const ll   LINF = 1e18;              // "vo cung" cho kieu long long
const ll   MOD = 1e9 + 7;            // so nguyen to hay dung de lay du
const double EPS = 1e-9;             // sai so cho phep khi so sanh so thuc

// ---------- Shortcut ----------
#define pb        push_back
#define eb        emplace_back
#define fi        first
#define se        second
#define all(v)    (v).begin(), (v).end()
#define rall(v)   (v).rbegin(), (v).rend()      // duyet nguoc (sort giam dan)
#define sz(v)     (int)(v).size()               // ep ve int, tranh bay unsigned
#define FOR(i,a,b)  for (int i = (a); i <= (b); i++)
#define FORD(i,a,b) for (int i = (a); i >= (b); i--)

// ---------- Tang toc nhap xuat ----------
// Ngat lien ket giua cin/cout va scanf/printf -> nhanh hon nhieu lan
#define FAST_IO  ios_base::sync_with_stdio(false); cin.tie(nullptr)

int main() {
    FAST_IO;

    int n;
    cin >> n;

    vll a(n);
    FOR(i, 0, n - 1) cin >> a[i];

    sort(all(a));

    ll tong = 0;
    for (ll x : a) tong += x;

    cout << "Tong = " << tong << "\n";
    cout << "Nho nhat = " << a[0] << ", Lon nhat = " << a[n-1] << "\n";
    return 0;
}
```

**Giải thích 3 dòng quan trọng nhất:**

1. `#include <bits/stdc++.h>` — gộp toàn bộ thư viện chuẩn, khỏi phải nhớ `#include` nào. ⚠️ Đây là phần **mở rộng riêng của GCC**, không có trên MSVC/clang chuẩn, và làm biên dịch chậm hơn. Không dùng trong dự án thật.

2. `FAST_IO` — mặc định `cin`/`cout` được đồng bộ với `scanf`/`printf` của C để dùng lẫn được, gây chậm. Tắt đồng bộ giúp nhanh gấp 3–5 lần khi đọc hàng trăm nghìn số. ⚠️ Sau khi dùng thì **không được** dùng `scanf`/`printf` nữa.

3. `#define sz(v) (int)(v).size()` — `.size()` trả về kiểu **unsigned**, gây lỗi khi viết `i < v.size() - 1` với vector rỗng (xem bài [02-02](../02-02-cpp-kieu-du-lieu.md) bài 15). Ép về `int` để tránh bẫy này.

### Bài 15.

Code gốc viết lại thành C++ thông thường:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<long long> binhPhuong;

    // Tinh binh phuong cac so tu 1 den 5
    for (long long i = 1; i <= 5; i++) {
        binhPhuong.push_back(i * i);
    }

    // Sap xep tang dan
    sort(binhPhuong.begin(), binhPhuong.end());

    // In ket qua
    for (long long giaTri : binhPhuong) {
        cout << giaTri << " ";
    }
    cout << endl;

    return 0;
}
```

Output: `1 4 9 16 25`

**Bảng đối chiếu từng dòng:**

| Code thi đấu | Code thường |
|---|---|
| `ll` | `long long` |
| `v.pb(x)` | `v.push_back(x)` |
| `sort(all(v))` | `sort(v.begin(), v.end())` |
| `FOR(i,1,5)` | `for (long long i = 1; i <= 5; i++)` |
| `FOR(i,0,v.size()-1)` | `for (size_t i = 0; i < v.size(); i++)` |

⚠️ **Một lỗi tiềm ẩn trong code gốc:** `FOR(i, 0, v.size()-1)` — macro `FOR` khai báo `int i`, nhưng `v.size()` là **unsigned**. Nếu `v` rỗng thì `v.size() - 1` = số cực lớn → vòng lặp chạy ra ngoài biên và chương trình crash. Bản viết lại dùng range-based for nên không có vấn đề này.

**Bài học:** macro giúp gõ nhanh, nhưng cũng **giấu đi các lỗi**. Đó là lý do chỉ nên dùng khi bạn đã hiểu rõ code bên dưới nó làm gì.
