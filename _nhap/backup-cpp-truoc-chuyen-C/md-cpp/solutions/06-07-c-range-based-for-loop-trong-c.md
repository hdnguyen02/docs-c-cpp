# Lời giải — [C++]. Range-based for loop trong C++

[← Quay lại bài học](../06-07-c-range-based-for-loop-trong-c.md)

> **Cú pháp:** `for (kieu bien : container) { ... }` — duyệt qua **từng phần tử**, không cần chỉ số.
> Cần chuẩn **C++11** trở lên: `g++ -std=c++17 main.cpp -o main`

---

### Bài 1.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int a[5] = {10, 20, 30, 40, 50};
    vector<int> v = {1, 2, 3, 4, 5};

    cout << "Mang tinh : ";
    for (int x : a) cout << x << " ";
    cout << endl;

    cout << "Vector    : ";
    for (int x : v) cout << x << " ";
    cout << endl;

    cout << "Dung auto : ";
    for (auto x : v) cout << x << " ";
    cout << endl;

    return 0;
}
```

💡 Range-based for dùng được với **mảng tĩnh, `vector`, `string`, `set`, `map`, `array`, `list`** — mọi thứ có `begin()`/`end()`.

### Bài 2.

```cpp
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

int main() {
    vector<int> v = {10, 20, 30, 40, 50};

    long long tong = 0;
    for (int x : v) tong += x;

    cout << "Tong = " << tong << endl;

    // Cach dung STL
    cout << "Tong (accumulate) = "
         << accumulate(v.begin(), v.end(), 0LL) << endl;
    return 0;
}
```

⚠️ Tham số thứ 3 của `accumulate` phải là `0LL` (kiểu `long long`), nếu viết `0` thì kết quả tính bằng `int` và có thể tràn.

### Bài 3.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5};

    cout << "Truoc: ";
    for (int x : v) cout << x << " ";
    cout << endl;

    for (auto& x : v) {          // DAU & rat quan trong!
        x *= 2;
    }

    cout << "Sau  : ";
    for (int x : v) cout << x << " ";
    cout << endl;                // 2 4 6 8 10
    return 0;
}
```

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int demNguyenAm = 0;
    for (char c : s) {
        char t = tolower((unsigned char)c);
        if (t == 'a' || t == 'e' || t == 'i' || t == 'o' || t == 'u') {
            demNguyenAm++;
        }
    }

    cout << "So nguyen am: " << demNguyenAm << endl;
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> ds = {"C++", "Python", "Javascript", "Go", "Rust"};

    string daiNhat = "";
    for (const auto& s : ds) {          // const auto& - khong sao chep chuoi
        if (s.length() > daiNhat.length()) daiNhat = s;
    }

    cout << "Chuoi dai nhat: " << daiNhat
         << " (" << daiNhat.length() << " ky tu)" << endl;
    return 0;
}
```

💡 Dùng `const auto&` thay vì `auto` — tránh sao chép chuỗi ở mỗi vòng lặp.

### Bài 6.

```cpp
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> diem = {
        {"An", 9}, {"Binh", 8}, {"Chi", 10}, {"Dung", 7}
    };

    // Cach 1: dung .first / .second
    cout << "--- Cach 1 ---" << endl;
    for (const auto& muc : diem) {
        cout << muc.first << " : " << muc.second << endl;
    }

    // Cach 2: structured binding (C++17) - RO RANG NHAT
    cout << "--- Cach 2 ---" << endl;
    for (const auto& [ten, d] : diem) {
        cout << ten << " : " << d << endl;
    }

    // Cach 3: sua gia tri
    for (auto& [ten, d] : diem) {
        d += 1;                          // cong diem cho tat ca
    }

    cout << "--- Sau khi cong diem ---" << endl;
    for (const auto& [ten, d] : diem) cout << ten << " : " << d << endl;

    return 0;
}
```

Output:

```
--- Cach 1 ---
An : 9
Binh : 8
Chi : 10
Dung : 7
...
```

⚠️ `map` **tự động sắp xếp theo khoá** — kết quả in ra theo thứ tự alphabet, không theo thứ tự chèn.

⚠️ Với `auto& [ten, d]`, bạn **sửa được `d`** nhưng **không sửa được `ten`** — khoá của `map` là `const`, vì sửa khoá sẽ phá vỡ cấu trúc sắp xếp bên trong.

### Bài 7.

```cpp
vector<int> v = {1,2,3};
for (auto x : v) x = x * 2;      // KHONG CO TAC DUNG
```

**Lỗi:** `auto x` (không có `&`) tạo một **bản sao** của phần tử ở mỗi vòng lặp. Sửa bản sao không ảnh hưởng vector gốc; bản sao bị huỷ khi hết vòng lặp.

**Sửa:**

```cpp
for (auto& x : v) x = x * 2;     // them dau &
```

Đây là lỗi phổ biến nhất khi mới dùng range-based for. Xem thêm bài [02-10](../02-10-c-kieu-du-lieu-suy-luan-auto-trong-c.md) bài 9.

### Bài 8.

```cpp
#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    vector<vector<int>> m = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Duyet in ra
    cout << "Ma tran:" << endl;
    for (const auto& hang : m) {
        for (int x : hang) cout << setw(4) << x;
        cout << endl;
    }

    // Tinh tong
    long long tong = 0;
    for (const auto& hang : m)
        for (int x : hang) tong += x;
    cout << "Tong = " << tong << endl;

    // Sua gia tri: nhan doi tat ca
    for (auto& hang : m)               // & o CA HAI cap
        for (auto& x : hang) x *= 2;

    cout << "Sau khi nhan doi:" << endl;
    for (const auto& hang : m) {
        for (int x : hang) cout << setw(4) << x;
        cout << endl;
    }
    return 0;
}
```

⚠️ **Muốn sửa được, phải có `&` ở CẢ HAI cấp.** Thiếu ở cấp ngoài (`for (auto hang : m)`) sẽ sao chép cả một hàng, và mọi thay đổi bên trong đều mất.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 200000;
    vector<string> v(N, string(200, 'x'));    // 200k chuoi, moi chuoi 200 ky tu

    // ① auto x - SAO CHEP moi chuoi
    auto t1 = high_resolution_clock::now();
    size_t tong1 = 0;
    for (auto x : v) tong1 += x.length();
    auto t2 = high_resolution_clock::now();
    cout << "auto x       : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ② auto& x - khong sao chep
    t1 = high_resolution_clock::now();
    size_t tong2 = 0;
    for (auto& x : v) tong2 += x.length();
    t2 = high_resolution_clock::now();
    cout << "auto& x      : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ③ const auto& x - khong sao chep + an toan
    t1 = high_resolution_clock::now();
    size_t tong3 = 0;
    for (const auto& x : v) tong3 += x.length();
    t2 = high_resolution_clock::now();
    cout << "const auto& x: " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    cout << "(Kiem tra: " << (tong1 == tong2 && tong2 == tong3 ? "OK" : "SAI") << ")" << endl;
    return 0;
}
```

Kết quả tham khảo:

```
auto x       : 32 ms
auto& x      : 1 ms
const auto& x: 1 ms
(Kiem tra: OK)
```

| Cú pháp | Sao chép? | Sửa được? | Dùng khi |
|---|---|---|---|
| `auto x` | ✅ Có | ❌ Không | Kiểu nhỏ (`int`, `char`, `double`) và chỉ đọc |
| `auto& x` | ❌ Không | ✅ Có | Cần **thay đổi** phần tử |
| `const auto& x` | ❌ Không | ❌ Không | **Mặc định nên dùng** khi chỉ đọc |

✅ **Quy tắc thực dụng:**
- Kiểu cơ bản → `for (int x : v)` hoặc `for (auto x : v)`
- Mọi kiểu khác → `for (const auto& x : v)`
- Cần sửa → `for (auto& x : v)`

### Bài 10.

```cpp
#include <iostream>
using namespace std;

void thu(int a[], int n) {
    // for (int x : a) cout << x;      // LOI BIEN DICH
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};

    for (int x : a) cout << x << " ";   // OK trong main
    cout << endl;

    thu(a, 5);
    return 0;
}
```

**KHÔNG dùng được.** Thông báo lỗi:

```
error: 'begin' was not declared in this scope
error: 'end' was not declared in this scope
```

**Giải thích:** range-based for cần biết **điểm đầu và điểm cuối** của dãy. Với mảng tĩnh trong cùng phạm vi khai báo, compiler biết kích thước nên tự suy ra được.

Nhưng khi truyền vào hàm, mảng **suy biến thành con trỏ** (array decay — xem bài [05-03](../05-03-c-tham-chieu-va-tham-tri.md) bài 10). Con trỏ chỉ biết **địa chỉ bắt đầu**, không biết mảng dài bao nhiêu → không có `end()`.

**Các cách khắc phục:**

```cpp
// ① Dung vector (tot nhat)
void thu(const vector<int>& v) {
    for (int x : v) cout << x << " ";
}

// ② Dung std::array
void thu(const array<int,5>& a) {
    for (int x : a) cout << x << " ";
}

// ③ Dung template giu nguyen kich thuoc
template <size_t N>
void thu(int (&a)[N]) {
    for (int x : a) cout << x << " ";
}

// ④ Dung span (C++20)
void thu(span<int> s) {
    for (int x : s) cout << x << " ";
}
```

### Bài 11.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // Duyet truc tiep danh sach khoi tao
    for (int x : {1, 2, 3, 4, 5}) cout << x << " ";
    cout << endl;

    for (const string& s : {"C++", "Python", "Java"}) cout << s << " ";
    cout << endl;

    // Rat tien khi kiem thu nhieu gia tri
    for (int n : {0, 1, 2, 17, 100, 97}) {
        cout << n << ": " << (n % 2 == 0 ? "chan" : "le") << endl;
    }
    return 0;
}
```

💡 **Rất tiện khi kiểm thử** — thay vì viết nhiều dòng gọi hàm, gom hết vào một danh sách:

```cpp
for (int n : {-1, 0, 1, 2, 100, 999})
    cout << n << " -> " << laNguyenTo(n) << endl;
```

### Bài 12.

```cpp
#include <iostream>
#include <vector>
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
    vector<int> v = {4, 7, 12, 13, 20, 29, 33, 41, 100, 97};

    cout << "Cac so nguyen to: ";
    vector<int> kq;
    for (int x : v) {
        if (laNguyenTo(x)) { cout << x << " "; kq.push_back(x); }
    }
    cout << "\nCo " << kq.size() << " so nguyen to" << endl;

    long long tong = 0;
    for (int x : kq) tong += x;
    cout << "Tong = " << tong << endl;
    return 0;
}
```

### Bài 13.

```cpp
vector<int> v = {1,2,3,4,5};
for (auto x : v) {
    if (x % 2 == 0) v.push_back(x * 10);     // NGUY HIEM!
}
```

**Lỗi nghiêm trọng: thay đổi container trong khi đang duyệt nó.**

`push_back` có thể khiến `vector` **cấp phát lại bộ nhớ** (khi vượt sức chứa hiện tại). Khi đó toàn bộ dữ liệu được chuyển sang vùng nhớ mới, và **mọi iterator đang dùng bị vô hiệu hoá** (dangling iterator).

Range-based for bên trong thực chất là:

```cpp
auto __end = v.end();
for (auto __it = v.begin(); __it != __end; ++__it) {
    auto x = *__it;
    ...
}
```

`__it` và `__end` được lấy **một lần** ở đầu. Sau `push_back`, chúng có thể trỏ vào vùng nhớ đã bị giải phóng → **undefined behavior**: chương trình có thể crash, lặp vô hạn, hoặc cho kết quả rác.

**Các cách sửa:**

```cpp
// ① Thu thap vao vector phu roi noi sau
vector<int> them;
for (int x : v) if (x % 2 == 0) them.push_back(x * 10);
v.insert(v.end(), them.begin(), them.end());

// ② Dung chi so va luu kich thuoc ban dau
size_t n = v.size();
for (size_t i = 0; i < n; i++)
    if (v[i] % 2 == 0) v.push_back(v[i] * 10);

// ③ Du tru san suc chua (van rui ro, khong khuyen nghi)
v.reserve(100);
```

⚠️ **Quy tắc vàng: KHÔNG BAO GIỜ thêm/xoá phần tử của container trong khi đang duyệt nó bằng range-based for.** Điều này đúng với cả `set`, `map`, `list`.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <ranges>
#include <algorithm>
using namespace std;

int main() {
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // Loc so chan roi nhan doi
    cout << "So chan nhan doi: ";
    for (int x : v | views::filter([](int n){ return n % 2 == 0; })
                   | views::transform([](int n){ return n * 2; })) {
        cout << x << " ";
    }
    cout << endl;                          // 4 8 12 16 20

    // Lay 3 phan tu dau
    cout << "3 phan tu dau : ";
    for (int x : v | views::take(3)) cout << x << " ";
    cout << endl;                          // 1 2 3

    // Bo 7 phan tu dau
    cout << "Bo 7 dau      : ";
    for (int x : v | views::drop(7)) cout << x << " ";
    cout << endl;                          // 8 9 10

    // Dao nguoc
    cout << "Dao nguoc     : ";
    for (int x : v | views::reverse) cout << x << " ";
    cout << endl;

    // Ket hop nhieu phep
    cout << "Ket hop        : ";
    for (int x : v | views::filter([](int n){ return n % 3 == 0; })
                   | views::transform([](int n){ return n * n; })
                   | views::reverse) {
        cout << x << " ";
    }
    cout << endl;                          // 81 36 9
    return 0;
}
```

Biên dịch cần **C++20**:

```bash
g++ -std=c++20 main.cpp -o main
```

**Ranges (C++20)** cho phép nối các phép biến đổi bằng toán tử `|` giống pipeline trong shell.

**Ưu điểm lớn nhất — lười biếng (lazy evaluation):** các phép biến đổi **không tạo ra vector trung gian**. Chúng chỉ được tính khi bạn thực sự duyệt tới phần tử đó.

```cpp
// Cach cu: tao 2 vector trung gian
vector<int> chan;
for (int x : v) if (x % 2 == 0) chan.push_back(x);
vector<int> kq;
for (int x : chan) kq.push_back(x * 2);

// Ranges: khong tao vector nao ca
auto kq = v | views::filter(...) | views::transform(...);
```

**Các view thường dùng:**

| View | Tác dụng |
|---|---|
| `views::filter(f)` | Chỉ giữ phần tử thoả điều kiện |
| `views::transform(f)` | Biến đổi từng phần tử |
| `views::take(n)` | Lấy `n` phần tử đầu |
| `views::drop(n)` | Bỏ `n` phần tử đầu |
| `views::reverse` | Đảo ngược |
| `views::iota(a, b)` | Sinh dãy số từ `a` tới `b−1` |
| `views::join` | Làm phẳng container lồng nhau |

### Bài 15.

Dưới đây là 5 ví dụ viết lại:

**① Tính tổng mảng** (bài [06-01](../06-01-cpp-mang-1-chieu.md) bài 2):

```cpp
// Truoc
long long tong = 0;
for (int i = 0; i < n; i++) tong += a[i];

// Sau
long long tong = 0;
for (int x : a) tong += x;
```

**② Đếm số chẵn/lẻ** (bài [06-01](../06-01-cpp-mang-1-chieu.md) bài 5):

```cpp
// Truoc
int chan = 0, le = 0;
for (int i = 0; i < n; i++) { if (a[i] % 2 == 0) chan++; else le++; }

// Sau
int chan = 0, le = 0;
for (int x : a) (x % 2 == 0) ? chan++ : le++;
```

**③ Tìm max** (bài [06-01](../06-01-cpp-mang-1-chieu.md) bài 3):

```cpp
// Truoc
int mx = a[0];
for (int i = 1; i < n; i++) if (a[i] > mx) mx = a[i];

// Sau
int mx = a[0];
for (int x : a) if (x > mx) mx = x;

// STL - ngan nhat
int mx = *max_element(a.begin(), a.end());
```

**④ Nhân đôi mọi phần tử:**

```cpp
// Truoc
for (int i = 0; i < n; i++) a[i] *= 2;

// Sau
for (auto& x : a) x *= 2;
```

**⑤ Đếm tần suất ký tự** (bài [06-06](../06-06-cpp-mang-danh-dau.md) bài 8):

```cpp
// Truoc
for (int i = 0; i < s.length(); i++)
    if (isalpha(s[i])) dem[tolower(s[i]) - 'a']++;

// Sau
for (char c : s)
    if (isalpha((unsigned char)c)) dem[tolower(c) - 'a']++;
```

**Nhận xét chung:**

| | Vòng for chỉ số | Range-based for |
|---|---|---|
| Độ dài code | Dài hơn ~20–30% | Ngắn hơn |
| Rủi ro lỗi | ⚠️ Sai biên, quên `i++`, dùng nhầm `<=` | ✅ Không thể sai biên |
| Biết vị trí phần tử | ✅ Có | ❌ Không |
| Duyệt ngược | ✅ Dễ | ⚠️ Cần `views::reverse` hoặc rbegin/rend |
| Duyệt nhiều mảng song song | ✅ Được | ❌ Không |
| Bỏ qua phần tử (bước nhảy 2) | ✅ Được | ❌ Không |

✅ **Khi nào vẫn dùng vòng for chỉ số:**
- Cần biết **vị trí** của phần tử
- Duyệt **ngược**, hoặc bước nhảy khác 1
- Duyệt **nhiều mảng cùng lúc**: `for (int i = 0; i < n; i++) c[i] = a[i] + b[i];`
- Cần **thêm/xoá** phần tử trong lúc duyệt
