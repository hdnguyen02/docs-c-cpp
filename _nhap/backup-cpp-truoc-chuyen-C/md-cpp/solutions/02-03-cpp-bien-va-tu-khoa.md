# Lời giải — [C++]. Biến Và Từ Khóa

[← Quay lại bài học](../02-03-cpp-bien-va-tu-khoa.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    double chieuDai  = 8.5;
    double chieuRong = 4.2;
    double chuVi     = (chieuDai + chieuRong) * 2;
    double dienTich  = chieuDai * chieuRong;
    char   tenHinh   = 'A';

    cout << "Hinh chu nhat : " << tenHinh   << endl;
    cout << "Chieu dai     : " << chieuDai  << endl;
    cout << "Chieu rong    : " << chieuRong << endl;
    cout << "Chu vi        : " << chuVi     << endl;
    cout << "Dien tich     : " << dienTich  << endl;
    return 0;
}
```

Output:

```
Hinh chu nhat : A
Chieu dai     : 8.5
Chieu rong    : 4.2
Chu vi        : 25.4
Dien tich     : 35.7
```

### Bài 2.

| Tên biến | Hợp lệ? | Giải thích |
|---|---|---|
| `banKinh` | ✅ | Đúng chuẩn camelCase |
| `2ban_kinh` | ❌ | Bắt đầu bằng chữ số |
| `ban kinh` | ❌ | Chứa dấu cách |
| `_temp` | ✅ | Được phép bắt đầu bằng `_`, nhưng **không nên** (tên bắt đầu bằng `_` viết hoa hoặc `__` được dành riêng cho thư viện chuẩn) |
| `int` | ❌ | Trùng từ khoá |
| `Diem` | ✅ | Hợp lệ (kiểu PascalCase, thường dùng cho tên class) |
| `diem-tb` | ❌ | Dấu `-` là toán tử trừ, không được dùng trong tên |
| `$money` | ❌ | Ký tự đặc biệt `$` (một số compiler chấp nhận như phần mở rộng, nhưng không chuẩn) |
| `so1` | ✅ | Chữ số ở giữa/cuối thì được |
| `class` | ❌ | Trùng từ khoá |
| `tongSo` | ✅ | Hợp lệ |
| `TONG_SO` | ✅ | Hợp lệ (quy ước thường dùng cho hằng số) |
| `ho&ten` | ❌ | Ký tự `&` không hợp lệ |
| `__x` | ⚠️ | Về cú pháp là hợp lệ, nhưng tên chứa 2 dấu `_` liên tiếp được **dành riêng cho trình biên dịch** — không nên dùng |
| `cout` | ⚠️ | Không phải keyword nên **biên dịch được**, nhưng nó sẽ che mất `std::cout` khiến bạn không in được ra màn hình. Tuyệt đối tránh. |

**Tóm tắt quy tắc:** tên biến chỉ gồm **chữ cái, chữ số và dấu `_`**; **không bắt đầu bằng chữ số**; **không trùng từ khoá**; **phân biệt hoa thường**.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int tech28 = 100;
    int Tech28 = 200;
    int TECH28 = 300;

    cout << "tech28 = " << tech28 << endl;
    cout << "Tech28 = " << Tech28 << endl;
    cout << "TECH28 = " << TECH28 << endl;
    return 0;
}
```

Output:

```
tech28 = 100
Tech28 = 200
TECH28 = 300
```

**Kết luận:** C++ là ngôn ngữ **case-sensitive** — `tech28`, `Tech28`, `TECH28` là 3 biến hoàn toàn khác nhau. Đây là nguyên nhân rất nhiều lỗi `error: 'X' was not declared in this scope` của người mới (viết `Cout` thay vì `cout`, hoặc khai báo `soLuong` rồi dùng `soluong`).

### Bài 4.

**Lỗi:** khai báo 2 biến trùng tên `a` trong cùng một phạm vi (dù khác kiểu dữ liệu vẫn không được). Ngoài ra chương trình còn thiếu `#include <iostream>` và `using namespace std;`.

Thông báo lỗi:

```
error: conflicting declaration 'float a'
note: previous declaration as 'int a'
```

Sửa lại:

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5;
    float b = 3.14f;      // doi ten bien
    cout << a << " " << b << endl;
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20, c = 30, d = 40;
    cout << "Tong = " << a + b + c + d << endl;
    return 0;
}
```

Output: `Tong = 100`

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 9;
    cout << "Truoc khi hoan doi: a = " << a << ", b = " << b << endl;

    int tam = a;    // cat a vao bien tam
    a = b;          // chep b sang a
    b = tam;        // chep gia tri cu cua a sang b

    cout << "Sau khi hoan doi : a = " << a << ", b = " << b << endl;
    return 0;
}
```

Output:

```
Truoc khi hoan doi: a = 5, b = 9
Sau khi hoan doi : a = 9, b = 5
```

**Ghi chú:** C++ có sẵn hàm `swap` trong `<algorithm>` (hoặc `<utility>`):

```cpp
swap(a, b);     // ngan gon, an toan, nen dung trong thuc te
```

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 5, b = 9;
    cout << "Truoc: a = " << a << ", b = " << b << endl;

    a = a + b;      // a = 14
    b = a - b;      // b = 14 - 9 = 5  (gia tri cu cua a)
    a = a - b;      // a = 14 - 5 = 9  (gia tri cu cua b)

    cout << "Sau  : a = " << a << ", b = " << b << endl;
    return 0;
}
```

Cách dùng XOR (chỉ áp dụng cho số nguyên):

```cpp
a = a ^ b;
b = a ^ b;
a = a ^ b;
```

⚠️ **Cảnh báo:** cả 2 cách trên đều có nhược điểm:

- Cách cộng trừ có thể **tràn số** nếu `a + b` vượt phạm vi kiểu dữ liệu.
- Cả hai đều **sai** nếu `a` và `b` là cùng một biến (ví dụ `swap(x, x)` → kết quả thành 0).
- Khó đọc hơn nhiều so với dùng biến trung gian.

Trong thực tế hãy dùng `swap()` hoặc biến trung gian. Bài này chỉ mang tính rèn tư duy.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    const double PI = 3.14159;

    double banKinh;
    cout << "Nhap ban kinh: ";
    cin >> banKinh;

    double chuVi    = 2 * PI * banKinh;
    double dienTich = PI * banKinh * banKinh;

    cout << "Chu vi   = " << chuVi << endl;
    cout << "Dien tich = " << dienTich << endl;
    return 0;
}
```

Ví dụ chạy:

```
Nhap ban kinh: 5
Chu vi   = 31.4159
Dien tich = 78.5397
```

**Ghi chú:** C++20 có sẵn hằng `std::numbers::pi` trong `<numbers>`, chính xác hơn:

```cpp
#include <numbers>
double PI = std::numbers::pi;   // 3.14159265358979...
```

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX_HOC_SINH = 50;
    cout << MAX_HOC_SINH << endl;

    MAX_HOC_SINH = 60;      // <- DONG NAY GAY LOI

    return 0;
}
```

Thông báo lỗi:

```
error: assignment of read-only variable 'MAX_HOC_SINH'
   |     MAX_HOC_SINH = 60;
   |     ~~~~~~~~~~~~~^~~~
```

**`const` là gì:** từ khoá đánh dấu một biến **chỉ đọc** — giá trị được cố định ngay khi khai báo và không thể thay đổi về sau. Compiler sẽ chặn ngay lúc biên dịch nếu bạn lỡ gán lại.

**Lợi ích:**
1. Tránh sửa nhầm giá trị quan trọng.
2. Code dễ đọc: `PI`, `MAX_HOC_SINH` rõ nghĩa hơn số 3.14159 hay 50 rải rác khắp chương trình ("magic number").
3. Chỉ cần sửa một chỗ khi giá trị thay đổi.

⚠️ Biến `const` **bắt buộc phải khởi tạo ngay khi khai báo**:

```cpp
const int x;        // LOI: uninitialized 'const x'
const int y = 10;   // DUNG
```

### Bài 10.

| Tên cũ | Tên nên đặt | Kiểu |
|---|---|---|
| `int a` | `soLuongHocSinh` | `int` |
| `double x` | `diemTrungBinh` | `double` |
| `char k` | `xepLoai` | `char` |
| `bool t` | `daNopHocPhi` | `bool` |
| `int n1` | `tongSoTienThu` | `long long` (tiền có thể lớn) |

```cpp
int       soLuongHocSinh = 45;
double    diemTrungBinh  = 7.85;
char      xepLoai        = 'B';
bool      daNopHocPhi    = true;
long long tongSoTienThu  = 135000000;
```

**Nguyên tắc đặt tên tốt:**
- Tên nói lên **ý nghĩa** chứ không phải kiểu dữ liệu.
- Biến `bool` nên bắt đầu bằng `is`, `has`, `da`, `co` → `isValid`, `daNopHocPhi`.
- Biến đếm số lượng nên có tiền tố `so`, `count`, `num` → `soHocSinh`.
- Chỉ dùng tên một chữ cái (`i`, `j`, `k`) cho **biến đếm vòng lặp**.

### Bài 11.

**camelCase** (chữ đầu thường, các từ sau viết hoa chữ cái đầu):

```cpp
#include <iostream>
using namespace std;

int main() {
    int    soHocSinh    = 45;
    double diemTrungBinh = 7.85;
    double tongDiem      = soHocSinh * diemTrungBinh;
    cout << "Tong diem ca lop: " << tongDiem << endl;
    return 0;
}
```

**snake_case** (tất cả chữ thường, nối bằng `_`):

```cpp
#include <iostream>
using namespace std;

int main() {
    int    so_hoc_sinh     = 45;
    double diem_trung_binh = 7.85;
    double tong_diem       = so_hoc_sinh * diem_trung_binh;
    cout << "Tong diem ca lop: " << tong_diem << endl;
    return 0;
}
```

| | camelCase | snake_case |
|---|---|---|
| Ưu điểm | Ngắn hơn, phổ biến trong Java/JavaScript/C# | Dễ đọc hơn khi tên dài, phổ biến trong thư viện chuẩn C++ và Python |
| Thường dùng ở | Nhiều dự án C++ doanh nghiệp, Qt | Thư viện chuẩn C++ (`push_back`, `size`), Google C++ Style |

**Điều quan trọng nhất không phải chọn kiểu nào, mà là chọn một kiểu và dùng nhất quán trong toàn bộ dự án.**

### Bài 12.

| Từ | Có phải keyword? | Giải thích |
|---|---|---|
| `main` | ❌ Không | Là **tên hàm** đặc biệt (điểm bắt đầu chương trình), nhưng không phải từ khoá |
| `cout` | ❌ Không | Là một **đối tượng** trong namespace `std`, định nghĩa ở `<iostream>` |
| `string` | ❌ Không | Là một **lớp** (`std::string`) trong `<string>` |
| `vector` | ❌ Không | Là một **lớp template** (`std::vector`) trong `<vector>` |
| `true` | ✅ **Có** | Từ khoá, hằng logic |
| `nullptr` | ✅ **Có** | Từ khoá (từ C++11), con trỏ rỗng |
| `endl` | ❌ Không | Là một **hàm manipulator** trong `std` |
| `size` | ❌ Không | Là tên phương thức (`v.size()`), hoàn toàn có thể dùng làm tên biến |

**Điểm mấu chốt:** rất nhiều thứ bạn gõ hằng ngày (`cout`, `cin`, `endl`, `string`, `vector`, `sort`) **không phải từ khoá của ngôn ngữ** mà là các thành phần của **thư viện chuẩn**. Vì thế bạn *có thể* đặt biến tên `cout`, compiler không cấm — nhưng nó sẽ che mất `std::cout` và gây lỗi khó hiểu.

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int x = 100;        // bien TOAN CUC (global)

int main() {
    int x = 50;     // bien CUC BO (local), che mat bien toan cuc

    cout << "Bien cuc bo   x = " << x   << endl;   // 50
    cout << "Bien toan cuc x = " << ::x << endl;   // 100
    return 0;
}
```

Output:

```
Bien cuc bo   x = 50
Bien toan cuc x = 100
```

**Giải thích:**
- Khi có 2 biến trùng tên, biến ở **phạm vi gần nhất** (cục bộ) sẽ "che" (shadow) biến bên ngoài.
- Toán tử `::` không có gì đứng trước gọi là **toán tử phạm vi toàn cục**, dùng để truy cập biến toàn cục bị che.

⚠️ Trong thực tế nên **tránh** đặt trùng tên như vậy — nó gây nhầm lẫn và là nguồn lỗi phổ biến. Compiler có thể cảnh báo với `-Wshadow`.

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

int main() {
    string tenSach   = "Lap trinh C++ co ban";
    string tacGia    = "Nguyen Van A";
    int    soTrang   = 350;
    long long gia    = 185000;       // VND
    bool   conHang   = true;

    cout << "==================================" << endl;
    cout << "          HOA DON BAN SACH        " << endl;
    cout << "==================================" << endl;
    cout << left << setw(12) << "Ten sach"  << ": " << tenSach << endl;
    cout << left << setw(12) << "Tac gia"   << ": " << tacGia  << endl;
    cout << left << setw(12) << "So trang"  << ": " << soTrang << endl;
    cout << left << setw(12) << "Gia ban"   << ": " << gia << " VND" << endl;
    cout << left << setw(12) << "Tinh trang"<< ": "
         << (conHang ? "Con hang" : "Het hang") << endl;
    cout << "==================================" << endl;
    return 0;
}
```

Output:

```
==================================
          HOA DON BAN SACH        
==================================
Ten sach    : Lap trinh C++ co ban
Tac gia     : Nguyen Van A
So trang    : 350
Gia ban     : 185000 VND
Tinh trang  : Con hang
==================================
```

### Bài 15.

**Output:**

```
20
10
```

**Giải thích — Phạm vi (scope) của biến:**

```cpp
int main(){
    int x = 10;          // x thu nhat, song trong toan bo main
    {                    // <- mo mot KHOI (block) moi
        int x = 20;      // x thu hai, chi song trong khoi nay, CHE x ben ngoai
        cout << x << endl;   // -> 20 (x gan nhat)
    }                    // <- het khoi, x thu hai bi HUY
    cout << x << endl;   // -> 10 (x thu nhat van con nguyen)
    return 0;
}
```

**Các quy tắc cần nhớ:**

1. Biến chỉ tồn tại từ lúc khai báo đến dấu `}` đóng khối chứa nó.
2. Khi có nhiều biến trùng tên, biến ở khối **trong cùng** được ưu tiên (shadowing).
3. Ra khỏi khối, biến bị huỷ và bộ nhớ được thu hồi.

Lỗi thường gặp do không nắm scope:

```cpp
for (int i = 0; i < 5; i++) {
    int tong = 0;         // tong bi tao lai = 0 moi vong lap!
    tong += i;
}
cout << i;                // LOI: 'i' was not declared in this scope
```

Sửa lại:

```cpp
int tong = 0;             // khai bao NGOAI vong lap
for (int i = 0; i < 5; i++) {
    tong += i;
}
cout << tong;             // 10
```
