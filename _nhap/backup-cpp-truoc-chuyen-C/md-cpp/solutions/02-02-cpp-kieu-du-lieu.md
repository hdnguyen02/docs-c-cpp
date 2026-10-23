# Lời giải — [C++]. Kiểu Dữ Liệu

[← Quay lại bài học](../02-02-cpp-kieu-du-lieu.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "char        : " << sizeof(char)        << " byte" << endl;
    cout << "bool        : " << sizeof(bool)        << " byte" << endl;
    cout << "short       : " << sizeof(short)       << " byte" << endl;
    cout << "int         : " << sizeof(int)         << " byte" << endl;
    cout << "long long   : " << sizeof(long long)   << " byte" << endl;
    cout << "float       : " << sizeof(float)       << " byte" << endl;
    cout << "double      : " << sizeof(double)      << " byte" << endl;
    cout << "long double : " << sizeof(long double) << " byte" << endl;
    return 0;
}
```

Output (trên máy 64-bit Linux):

```
char        : 1 byte
bool        : 1 byte
short       : 2 byte
int         : 4 byte
long long   : 8 byte
float       : 4 byte
double      : 8 byte
long double : 16 byte
```

⚠️ **Lưu ý:** chuẩn C++ chỉ quy định *quan hệ* giữa các kiểu (`short` ≤ `int` ≤ `long` ≤ `long long`), không quy định số byte tuyệt đối. Ví dụ `long` là 8 byte trên Linux 64-bit nhưng chỉ 4 byte trên Windows.

### Bài 2.

```cpp
#include <iostream>
#include <limits>
using namespace std;

int main() {
    cout << "short              : " << numeric_limits<short>::min()
         << " -> " << numeric_limits<short>::max() << endl;
    cout << "unsigned short     : " << numeric_limits<unsigned short>::min()
         << " -> " << numeric_limits<unsigned short>::max() << endl;
    cout << "int                : " << numeric_limits<int>::min()
         << " -> " << numeric_limits<int>::max() << endl;
    cout << "unsigned int       : " << numeric_limits<unsigned int>::min()
         << " -> " << numeric_limits<unsigned int>::max() << endl;
    cout << "long long          : " << numeric_limits<long long>::min()
         << " -> " << numeric_limits<long long>::max() << endl;
    cout << "unsigned long long : " << numeric_limits<unsigned long long>::min()
         << " -> " << numeric_limits<unsigned long long>::max() << endl;
    return 0;
}
```

**Cách tự tính:**

| Kiểu | Byte | Bit (K) | Công thức | Phạm vi |
|---|---|---|---|---|
| `short` | 2 | 16 | −2^(K−1) → 2^(K−1)−1 | −32.768 → 32.767 |
| `unsigned short` | 2 | 16 | 0 → 2^K−1 | 0 → 65.535 |
| `int` | 4 | 32 | −2^31 → 2^31−1 | −2.147.483.648 → 2.147.483.647 |
| `unsigned int` | 4 | 32 | 0 → 2^32−1 | 0 → 4.294.967.295 |
| `long long` | 8 | 64 | −2^63 → 2^63−1 | ≈ −9,22×10^18 → 9,22×10^18 |
| `unsigned long long` | 8 | 64 | 0 → 2^64−1 | 0 → ≈1,84×10^19 |

**Mẹo nhớ nhanh:** `int` ≈ ±2×10⁹, `long long` ≈ ±9×10¹⁸.

### Bài 3.

| Giá trị | Kiểu nên dùng | Lý do |
|---|---|---|
| a) Tuổi một người | `unsigned char` hoặc `int` | Tuổi 0–150, `unsigned char` (0–255) là đủ. Thực tế nên dùng `int` cho dễ đọc và tránh lỗi khi tính toán. |
| b) Dân số Việt Nam | `int` | ≈ 100 triệu < 2,1 tỷ → `int` thừa sức. |
| c) Dân số thế giới | `long long` | ≈ 8 tỷ > 2,1 tỷ → tràn `int`. Có thể dùng `unsigned int` (tối đa 4,29 tỷ) nhưng `long long` an toàn hơn. |
| d) Điểm trung bình môn | `float` hoặc `double` | Có phần thập phân. `float` đủ (chỉ cần 1–2 chữ số thập phân), nhưng `double` là lựa chọn mặc định an toàn. |
| e) Giới tính (nam/nữ) | `bool` | Chỉ có 2 trạng thái. Ví dụ `bool isMale`. |
| f) Ký tự xếp loại A/B/C/D | `char` | Lưu đúng một ký tự. |
| g) Số tiền tài khoản (VNĐ) | `long long` | Số dư có thể lên hàng nghìn tỷ đồng, vượt xa `int`. **Tuyệt đối không dùng `float`/`double`** cho tiền vì có sai số làm tròn. |
| h) Số ngày trong tháng | `unsigned char` / `int` | Giá trị 28–31, rất nhỏ. |

**Nguyên tắc thực tế:** với người mới, chỉ cần nhớ **`int` cho số nguyên thường, `long long` khi quá 2 tỷ, `double` cho số thực, `char` cho ký tự, `bool` cho đúng/sai**. Tiết kiệm từng byte chỉ thực sự quan trọng khi lưu mảng hàng triệu phần tử.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 3000000000;
    cout << a << endl;
    return 0;
}
```

Output:

```
-1294967296
```

**Giải thích:** giá trị lớn nhất của `int` là 2.147.483.647. Số 3.000.000.000 vượt quá ngưỡng này nên bị **tràn số (overflow)**, giá trị "quay vòng" về phía âm.

Cách tính: 3.000.000.000 − 2^32 = 3.000.000.000 − 4.294.967.296 = **−1.294.967.296** ✔

Khi biên dịch với `-Wall`, compiler sẽ cảnh báo:

```
warning: overflow in conversion from 'long int' to 'int' changes value
```

**Cách sửa:** dùng `long long a = 3000000000;`

### Bài 5.

```cpp
#include <iostream>
#include <limits>
using namespace std;

int main() {
    short x = numeric_limits<short>::max();   // 32767
    cout << "Gia tri lon nhat cua short : " << x << endl;

    x = x + 1;
    cout << "Sau khi cong them 1        : " << x << endl;
    return 0;
}
```

Output:

```
Gia tri lon nhat cua short : 32767
Sau khi cong them 1        : -32768
```

**Giải thích:** `short` dùng 16 bit theo dạng **bù 2 (two's complement)**.

```
 32767 = 0111 1111 1111 1111
    +1
-32768 = 1000 0000 0000 0000   <- bit dau tien (bit dau) bat len -> thanh so am
```

Giống như đồng hồ đo quãng đường ô tô quay về 0 khi đạt số lớn nhất — số nguyên "quay vòng" từ max về min.

⚠️ Với **số nguyên có dấu**, tràn số là *undefined behavior* theo chuẩn C++ (kết quả không đảm bảo). Với **số không dấu**, chuẩn quy định rõ là quay vòng theo modulo.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 1;
    for (int i = 0; i < 31; i++) a = a * 2;

    long long b = 1;
    for (int i = 0; i < 31; i++) b = b * 2;

    cout << "Dung int       : " << a << endl;
    cout << "Dung long long : " << b << endl;
    return 0;
}
```

Output:

```
Dung int       : -2147483648
Dung long long : 2147483648
```

**Giải thích:** 2³¹ = 2.147.483.648, lớn hơn giá trị max của `int` đúng 1 đơn vị, nên bị tràn thành giá trị min (−2.147.483.648). `long long` (64 bit) lưu thoải mái.

⚠️ **Bẫy kinh điển:**

```cpp
long long kq = 1000000 * 1000000;       // SAI: -727379968
long long kq2 = 1000000LL * 1000000;    // DUNG: 1000000000000
```

Phép nhân bên phải được thực hiện **trước** với kiểu `int`, tràn rồi mới gán vào `long long`. Phải ép một toán hạng sang `long long` (bằng hậu tố `LL` hoặc `(long long)`).

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    float  f = 1.0f / 3.0f;
    double d = 1.0  / 3.0;

    cout << fixed << setprecision(20);
    cout << "float  : " << f << endl;
    cout << "double : " << d << endl;
    return 0;
}
```

Output:

```
float  : 0.33333334326744079590
double : 0.33333333333333331483
```

**Giải thích:**

| | `float` | `double` |
|---|---|---|
| Kích thước | 4 byte (32 bit) | 8 byte (64 bit) |
| Số bit phần định trị | 23 bit | 52 bit |
| Số chữ số thập phân đáng tin | ~7 | ~15–16 |

`float` chỉ đúng tới chữ số thứ 7 (`0.3333333`), từ chữ số thứ 8 trở đi (`4326744...`) là rác. `double` đúng tới khoảng chữ số thứ 16.

**Kết luận:** trong hầu hết bài toán nên dùng `double`, chỉ dùng `float` khi phải tiết kiệm bộ nhớ cho mảng cực lớn.

### Bài 8.

```cpp
#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
    double a = 0.1 + 0.2;
    cout << (a == 0.3) << endl;                       // 0 (false)
    cout << setprecision(20) << a << endl;            // 0.30000000000000004441
    cout << setprecision(20) << 0.3 << endl;          // 0.29999999999999998890

    // Cach so sanh DUNG voi so thuc:
    const double EPS = 1e-9;
    cout << (fabs(a - 0.3) < EPS) << endl;            // 1 (true)
    return 0;
}
```

**Giải thích:** máy tính lưu số thực ở **hệ nhị phân**. Giống như hệ thập phân không biểu diễn chính xác được 1/3 (= 0,3333…), hệ nhị phân **không biểu diễn chính xác được 0,1 và 0,2** — chúng là số thập phân vô hạn tuần hoàn trong hệ 2.

```
0.1 (thuc te luu) = 0.1000000000000000055511151231257827...
0.2 (thuc te luu) = 0.2000000000000000111022302462515654...
Cong lai          = 0.3000000000000000444089209850062616...
0.3 (thuc te luu) = 0.2999999999999999888977697537...
```

→ Hai số khác nhau ở chữ số thứ 17, nên `==` trả về `false`.

✅ **Quy tắc vàng: KHÔNG BAO GIỜ so sánh 2 số thực bằng `==`.** Luôn dùng:

```cpp
if (fabs(a - b) < 1e-9) { /* coi nhu bang nhau */ }
```

Đây là lỗi khiến rất nhiều bài tập bị sai kết quả mà người mới không hiểu vì sao.

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c = 'A';
    cout << "Dang ky tu   : " << c << endl;
    cout << "Dang so nguyen: " << (int)c << endl;
    return 0;
}
```

Output:

```
Dang ky tu   : A
Dang so nguyen: 65
```

**Giải thích:** `char` thực chất là một số nguyên 1 byte. Ký tự `'A'` được lưu dưới dạng **mã ASCII** của nó là 65. `cout` in ra ký tự hay số phụ thuộc vào **kiểu** của biểu thức: `(int)c` ép sang `int` nên in ra số.

Các cách ép kiểu tương đương:

```cpp
cout << (int)c;              // ep kieu kieu C
cout << int(c);              // ep kieu kieu ham
cout << static_cast<int>(c); // ep kieu chuan C++ (nen dung)
cout << c + 0;               // meo: cong 0 -> tu dong nang len int
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    char a = 65;
    char b = 97;
    char c = 48;
    cout << a << " " << b << " " << c << endl;
    return 0;
}
```

Output:

```
A a 0
```

**Nhận xét:** gán số nguyên cho `char` thì khi in ra, `cout` hiểu đó là **mã ASCII** và in ký tự tương ứng. `char` và số nguyên là **một** — chỉ khác cách hiển thị.

Ba mốc ASCII cần nhớ:

| Ký tự | Mã | Ghi nhớ |
|---|---|---|
| `'0'` | 48 | Chữ số `'0'`–`'9'` = 48–57 |
| `'A'` | 65 | Chữ hoa `'A'`–`'Z'` = 65–90 |
| `'a'` | 97 | Chữ thường `'a'`–`'z'` = 97–122 |

Khoảng cách giữa chữ hoa và chữ thường luôn là **32**.

Ứng dụng:

```cpp
char so = '7';
int giatri = so - '0';        // 55 - 48 = 7  -> doi ky tu so sang so
char hoa = 'a' - 32;          // 'A'          -> doi thuong sang hoa
```

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    bool b1 = 0;
    bool b2 = 1;
    bool b3 = 5;
    bool b4 = -3;
    bool b5 = 0.0;

    cout << boolalpha;
    cout << "bool b1 = 0    -> " << b1 << endl;
    cout << "bool b2 = 1    -> " << b2 << endl;
    cout << "bool b3 = 5    -> " << b3 << endl;
    cout << "bool b4 = -3   -> " << b4 << endl;
    cout << "bool b5 = 0.0  -> " << b5 << endl;
    return 0;
}
```

Output:

```
bool b1 = 0    -> false
bool b2 = 1    -> true
bool b3 = 5    -> true
bool b4 = -3   -> true
bool b5 = 0.0  -> false
```

**Kết luận quan trọng:**

> Trong C++, **0 là `false`, mọi giá trị khác 0 đều là `true`** — kể cả số âm.

Vì vậy các cách viết sau là hợp lệ và rất hay gặp:

```cpp
int n = 5;
if (n) { ... }          // tuong duong if (n != 0)
if (!n) { ... }         // tuong duong if (n == 0)
```

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a;              // KHONG khoi tao
    cout << a << endl;
    return 0;
}
```

Kết quả khi chạy 3 lần (ví dụ): `21845`, `0`, `32764` — **không đoán trước được**.

**Giải thích:** biến cục bộ không khởi tạo sẽ nhận giá trị "rác" — chính là dãy bit đang có sẵn tại ô nhớ mà biến được cấp phát (do chương trình khác hoặc chính chương trình bạn dùng trước đó để lại).

⚠️ Đây là **undefined behavior**. Nguy hiểm ở chỗ: chương trình có thể chạy đúng trên máy bạn và sai trên máy khác, hoặc đúng ở chế độ Debug và sai ở chế độ Release.

Biên dịch với `-Wall` để được cảnh báo:

```
warning: 'a' is used uninitialized [-Wuninitialized]
```

✅ **Thói quen tốt: luôn khởi tạo biến ngay khi khai báo.**

```cpp
int a = 0;
double d = 0.0;
char c = '\0';
bool flag = false;
```

Ghi chú: biến **toàn cục** (khai báo ngoài mọi hàm) thì ngược lại — luôn được tự động khởi tạo bằng 0.

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    int       maSV      = 20250001;      // ma sinh vien
    long long soCMND    = 001234567890;  // 12 chu so -> vuot int
    float     chieuCao  = 1.72f;         // met
    double    diemTB    = 8.75;
    char      xepLoai   = 'B';
    bool      daTotNghiep = false;

    cout << "Ma SV        : " << maSV << endl;
    cout << "So CMND      : " << soCMND << endl;
    cout << "Chieu cao    : " << chieuCao << " m" << endl;
    cout << "Diem TB      : " << diemTB << endl;
    cout << "Xep loai     : " << xepLoai << endl;
    cout << "Da tot nghiep: " << boolalpha << daTotNghiep << endl;
    return 0;
}
```

Output:

```
Ma SV        : 20250001
So CMND      : 1234567890
Chieu cao    : 1.72 m
Diem TB      : 8.75
Xep loai     : B
Da tot nghiep: false
```

⚠️ **Lưu ý thực tế:** số CMND/CCCD nên lưu bằng `string` chứ không phải số, vì nó có thể bắt đầu bằng số 0 (`001234567890`) — lưu bằng số sẽ mất các số 0 đầu, và ta cũng không bao giờ cần *tính toán* trên số CMND.

### Bài 14.

`int` và `unsigned int` đều dùng **32 bit**, tức 2³² = 4.294.967.296 tổ hợp bit khác nhau. Số lượng giá trị biểu diễn được là **như nhau** — cái khác là **các giá trị đó được diễn giải thế nào**.

| | `int` (có dấu) | `unsigned int` (không dấu) |
|---|---|---|
| Bit đầu tiên | Dùng làm bit dấu (0 = dương, 1 = âm) | Dùng làm bit giá trị bình thường |
| Số bit cho giá trị | 31 bit | 32 bit |
| Phạm vi | −2.147.483.648 → 2.147.483.647 | 0 → 4.294.967.295 |
| Tổng số giá trị | 4.294.967.296 | 4.294.967.296 |

Ví dụ cùng một dãy bit `1111 1111 1111 1111 1111 1111 1111 1111`:

- Hiểu là `int` → **−1**
- Hiểu là `unsigned int` → **4.294.967.295**

**Kết luận:** `unsigned` không "chứa được nhiều số hơn", nó chỉ **dịch toàn bộ phạm vi sang phía dương** bằng cách hy sinh khả năng lưu số âm. Giá trị dương lớn nhất tăng gấp đôi, đúng như bài học nêu.

### Bài 15.

```cpp
#include <iostream>
using namespace std;

int main() {
    unsigned int a = 0;
    a = a - 1;
    cout << a << endl;
    return 0;
}
```

Output:

```
4294967295
```

**Giải thích:** `unsigned int` không lưu được số âm. Khi kết quả là −1, giá trị bị **quay vòng (wrap around)** về giá trị lớn nhất: 2³² − 1 = 4.294.967.295.

Về mặt bit:
```
    0 = 0000 0000 0000 0000 0000 0000 0000 0000
   -1   (muon tru 1 -> muon tu bit cao nhat)
  kq  = 1111 1111 1111 1111 1111 1111 1111 1111  = 4294967295
```

⚠️ **Bẫy cực kỳ phổ biến** — vòng lặp dưới đây chạy **vô hạn**:

```cpp
for (unsigned int i = 5; i >= 0; i--) {   // SAI: i >= 0 LUON dung voi unsigned!
    cout << i << " ";
}
```

Khi `i = 0` giảm tiếp sẽ thành 4.294.967.295 chứ không phải −1, nên điều kiện `i >= 0` không bao giờ sai.

Một bẫy khác với `.size()` (trả về kiểu unsigned):

```cpp
vector<int> v;                      // vector rong
if (v.size() - 1 >= 0) { ... }      // LUON dung, vi 0 - 1 = so cuc lon!
for (int i = 0; i < v.size() - 1; i++) { ... }   // chay ra ngoai bien!
```

✅ **Lời khuyên: với người mới, cứ dùng `int` cho biến đếm và chỉ số, tránh `unsigned` trừ khi thật sự cần.**
