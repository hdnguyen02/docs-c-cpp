# Lời giải — [C++]. Toán Tử - Operator

[← Quay lại bài học](../02-07-cpp-toan-tu-operator.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Nhap a va b: ";
    cin >> a >> b;

    cout << "Tong        : " << a + b << endl;
    cout << "Hieu        : " << a - b << endl;
    cout << "Tich        : " << a * b << endl;
    cout << "Thuong nguyen: " << a / b << endl;
    cout << "So du       : " << a % b << endl;
    return 0;
}
```

Ví dụ với `a = 17, b = 5`:

```
Tong        : 22
Hieu        : 12
Tich        : 85
Thuong nguyen: 3
So du       : 2
```

⚠️ Nếu `b = 0` thì `a / b` và `a % b` gây lỗi chia cho 0 (chương trình crash). Nên kiểm tra trước:

```cpp
if (b != 0) { ... }
```

### Bài 2.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b;
    cout << "Nhap a va b: ";
    cin >> a >> b;

    cout << fixed << setprecision(3);
    cout << "Thuong = " << (double)a / b << endl;
    return 0;
}
```

Ví dụ `a = 17, b = 5` → `Thuong = 3.400`

**Điểm mấu chốt:** `a / b` với cả hai đều là `int` cho **phép chia nguyên**. Chỉ cần ép **một** toán hạng sang `double` là phép chia trở thành chia thực.

Các cách ép tương đương:

```cpp
(double)a / b        // ep a sang double
a / (double)b        // ep b sang double
1.0 * a / b          // nhan 1.0 -> tu dong nang kieu
static_cast<double>(a) / b   // cach chuan C++
```

⚠️ **SAI:** `(double)(a / b)` — phép chia nguyên đã xảy ra **trước**, ép kiểu sau cũng vô nghĩa (`(double)(17/5)` = `(double)3` = `3.0`).

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so co 3 chu so: ";
    cin >> n;

    int tram    = n / 100;          // 345 / 100 = 3
    int chuc    = (n / 10) % 10;    // 345 / 10 = 34, 34 % 10 = 4
    int donVi   = n % 10;           // 345 % 10 = 5

    cout << "Hang tram   : " << tram  << endl;
    cout << "Hang chuc   : " << chuc  << endl;
    cout << "Hang don vi : " << donVi << endl;
    cout << "Tong cac chu so: " << tram + chuc + donVi << endl;
    return 0;
}
```

Ví dụ `n = 345`:

```
Hang tram   : 3
Hang chuc   : 4
Hang don vi : 5
Tong cac chu so: 12
```

**2 kỹ thuật vàng cần thuộc lòng:**

| Thao tác | Công thức |
|---|---|
| Lấy chữ số cuối | `n % 10` |
| Xoá chữ số cuối | `n / 10` |
| Lấy chữ số thứ k từ phải (k bắt đầu từ 0) | `(n / pow(10,k)) % 10` |

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << " la so " << (n % 2 == 0 ? "CHAN" : "LE") << endl;
    return 0;
}
```

**Cú pháp toán tử 3 ngôi:** `dieu_kien ? gia_tri_neu_dung : gia_tri_neu_sai`

⚠️ **Lưu ý với số âm:** trong C++, `-7 % 2` cho kết quả **−1** chứ không phải 1. Vì thế điều kiện `n % 2 == 1` sẽ **sai** với số âm. Luôn dùng `n % 2 == 0` để kiểm tra chẵn (đúng với mọi số), hoặc `n % 2 != 0` để kiểm tra lẻ.

```cpp
cout << (-7 % 2) << endl;      // -1
cout << (-7 % 2 == 1) << endl; // 0 (SAI, -7 la so le!)
cout << (-7 % 2 != 0) << endl; // 1 (DUNG)
```

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int tongPhut;
    cout << "Nhap tong so phut: ";
    cin >> tongPhut;

    int gio  = tongPhut / 60;
    int phut = tongPhut % 60;

    cout << tongPhut << " phut = " << gio << " gio " << phut << " phut" << endl;
    return 0;
}
```

Ví dụ: `135` → `135 phut = 2 gio 15 phut`

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long sai  = 1000000 * 1000000;              // SAI
    long long dung1 = 1000000LL * 1000000;           // DUNG - hau to LL
    long long dung2 = (long long)1000000 * 1000000;  // DUNG - ep kieu
    long long a = 1000000;
    long long dung3 = a * 1000000;                   // DUNG - bien da la long long

    cout << "Sai   : " << sai   << endl;
    cout << "Dung 1: " << dung1 << endl;
    cout << "Dung 2: " << dung2 << endl;
    cout << "Dung 3: " << dung3 << endl;
    return 0;
}
```

Output:

```
Sai   : -727379968
Dung 1: 1000000000000
Dung 2: 1000000000000
Dung 3: 1000000000000
```

**Giải thích:** `1000000` và `1000000` đều là hằng kiểu `int`. C++ **tính vế phải trước**, bằng kiểu `int`:

```
1.000.000 × 1.000.000 = 1.000.000.000.000   (10^12)
Vuot gioi han int (2.147.483.647) -> tran so -> -727.379.968
Sau do moi gan gia tri DA SAI nay vao long long
```

✅ **Quy tắc vàng:** kiểu của biến nhận kết quả **không** ảnh hưởng tới cách tính vế phải. Muốn kết quả `long long`, phải có **ít nhất một toán hạng** là `long long` ngay trong biểu thức.

Đây là lỗi phổ biến nhất khiến bài tập/bài thi bị sai với dữ liệu lớn.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a;

    a = 5;  cout << a++ << " ";  cout << a << endl;   // 5 6
    a = 5;  cout << ++a << " ";  cout << a << endl;   // 6 6
    a = 5;  cout << a-- + 1 << endl;                  // 6
    return 0;
}
```

| Biểu thức | Kết quả in | Giá trị `a` sau đó | Giải thích |
|---|---|---|---|
| `a++` | **5** | 6 | **Hậu tố**: lấy giá trị cũ (5) để dùng, *rồi mới* tăng |
| `++a` | **6** | 6 | **Tiền tố**: tăng trước (thành 6), *rồi mới* lấy giá trị |
| `a-- + 1` | **6** | 4 | `a--` trả về 5, cộng 1 = 6; sau đó `a` giảm còn 4 |
| `--a + a++` | ⚠️ **Undefined** | ⚠️ | Xem bên dưới |

**Mẹo nhớ:** đọc từ trái sang phải theo đúng thứ tự viết.
- `a++` → "lấy `a` rồi tăng" (dấu `++` đứng sau = làm sau)
- `++a` → "tăng rồi lấy `a`" (dấu `++` đứng trước = làm trước)

⚠️ **Dòng cuối `--a + a++` là UNDEFINED BEHAVIOR.** Biến `a` bị sửa **2 lần** trong cùng một biểu thức mà không có điểm đồng bộ (sequence point). Chuẩn C++ không quy định thứ tự thực hiện, nên mỗi compiler có thể cho kết quả khác nhau — và về lý thuyết chương trình có quyền làm bất cứ điều gì.

✅ **Không bao giờ viết code kiểu này.** Tách ra cho rõ ràng:

```cpp
// Thay vi: cout << --a + a++;
--a;
int t = a;
a++;
cout << t + a;     // ro rang, chac chan dung
```

Trong thực tế, chỉ nên dùng `i++`/`++i` **một mình** trên một dòng hoặc trong phần cập nhật của vòng `for`.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 100;
    cout << "Ban dau : a = " << a << endl;

    a += 20;   cout << "a += 20 -> " << a << endl;   // 120
    a -= 50;   cout << "a -= 50 -> " << a << endl;   // 70
    a *= 3;    cout << "a *= 3  -> " << a << endl;   // 210
    a /= 4;    cout << "a /= 4  -> " << a << endl;   // 52 (chia nguyen!)
    a %= 10;   cout << "a %= 10 -> " << a << endl;   // 2

    return 0;
}
```

Output:

```
Ban dau : a = 100
a += 20 -> 120
a -= 50 -> 70
a *= 3  -> 210
a /= 4  -> 52
a %= 10 -> 2
```

**Lợi ích của toán tử gán rút gọn:**
1. Ngắn hơn: `a += 20` thay vì `a = a + 20`
2. Không bị viết nhầm tên biến: `tongDiemHocKy1 += x` an toàn hơn `tongDiemHocKy1 = tongDiemHocKy2 + x`
3. Với kiểu phức tạp (`string`, `vector`), phiên bản `+=` thường nhanh hơn

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Nhap 3 so: ";
    cin >> a >> b >> c;

    int lonNhat = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);

    cout << "So lon nhat = " << lonNhat << endl;
    return 0;
}
```

**Cách đọc biểu thức lồng nhau:**

```
(a > b) ? [ a lon hon b -> so a voi c ] : [ b lon hon a -> so b voi c ]
           (a > c) ? a : c                  (b > c) ? b : c
```

Cách viết dễ đọc hơn dùng `max`:

```cpp
#include <algorithm>
int lonNhat = max(a, max(b, c));
// hoac C++11:
int lonNhat = max({a, b, c});
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int tuoi;
    cout << "Nhap tuoi: ";
    cin >> tuoi;

    bool trongDoTuoiLaoDong = (tuoi >= 18 && tuoi <= 60);

    cout << "Trong do tuoi lao dong: "
         << (trongDoTuoiLaoDong ? "CO" : "KHONG") << endl;
    return 0;
}
```

⚠️ **Bẫy toán học:** trong C++ **không được** viết `18 <= tuoi <= 60` như trong toán học. Biểu thức đó vẫn biên dịch được nhưng cho kết quả sai:

```
18 <= tuoi <= 60
-> (18 <= tuoi) <= 60      (tinh tu trai sang phai)
-> (0 hoac 1) <= 60
-> LUON DUNG (vi 0 va 1 deu <= 60)
```

Bắt buộc phải tách ra và nối bằng `&&`.

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    int nam;
    cout << "Nhap nam: ";
    cin >> nam;

    bool laNamNhuan = (nam % 4 == 0 && nam % 100 != 0) || (nam % 400 == 0);

    cout << nam << (laNamNhuan ? " LA " : " KHONG LA ") << "nam nhuan" << endl;
    return 0;
}
```

Kiểm thử:

| Năm | Kết quả | Vì sao |
|---|---|---|
| 2024 | Nhuận | Chia hết 4, không chia hết 100 |
| 2023 | Không | Không chia hết 4 |
| 1900 | Không | Chia hết 4 **và** chia hết 100, nhưng không chia hết 400 |
| 2000 | Nhuận | Chia hết 400 |

**Quy tắc năm nhuận đầy đủ:** năm chia hết cho 4 là nhuận, **trừ** các năm chia hết cho 100, **nhưng** các năm chia hết cho 400 vẫn là nhuận.

⚠️ Dấu ngoặc ở đây rất quan trọng. `&&` có độ ưu tiên cao hơn `||`, nên về mặt kỹ thuật bỏ ngoặc vẫn đúng — nhưng **luôn nên đặt ngoặc** để người đọc không phải tra bảng ưu tiên.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int i = 0, j = 0;

    // && : neu ve TRAI SAI -> khong tinh ve phai nua
    if (false && (i++ > 0)) { }
    cout << "Sau &&: i = " << i << endl;      // i = 0, i++ KHONG chay

    // || : neu ve TRAI DUNG -> khong tinh ve phai nua
    if (true || (j++ > 0)) { }
    cout << "Sau ||: j = " << j << endl;      // j = 0, j++ KHONG chay

    int k = 0, m = 0;
    if (true && (k++ > -1)) { }
    cout << "k = " << k << endl;              // k = 1, CO chay
    if (false || (m++ > -1)) { }
    cout << "m = " << m << endl;              // m = 1, CO chay

    return 0;
}
```

Output:

```
Sau &&: i = 0
Sau ||: j = 0
k = 1
m = 1
```

**Short-circuit (đoản mạch)** là cơ chế: C++ **ngừng tính** ngay khi đã biết chắc kết quả.

| Toán tử | Ngừng khi | Lý do |
|---|---|---|
| `A && B` | `A` sai | Sai `&&` bất cứ gì đều sai → khỏi cần biết `B` |
| `A \|\| B` | `A` đúng | Đúng `\|\|` bất cứ gì đều đúng → khỏi cần biết `B` |

**Ứng dụng cực kỳ quan trọng — dùng để bảo vệ khỏi lỗi:**

```cpp
// Kiem tra chia het ma khong so chia cho 0
if (b != 0 && a % b == 0) { ... }
//  ^^^^^^^^ neu b == 0, ve phai KHONG bao gio chay -> khong crash

// Kiem tra phan tu mang ma khong vuot bien
if (i < n && a[i] > 0) { ... }
//  ^^^^^ neu i >= n, khong truy cap a[i] -> khong loi

// Kiem tra con tro truoc khi dung
if (p != nullptr && p->giaTri > 0) { ... }

// Kiem tra ky tu dau chuoi ma khong loi khi chuoi rong
if (!s.empty() && s[0] == 'A') { ... }
```

⚠️ **Thứ tự rất quan trọng** — viết ngược lại là crash:

```cpp
if (a % b == 0 && b != 0) { ... }    // SAI! chia cho 0 truoc khi kiem tra
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << 2 + 3 * 4 - 6 / 2 << endl;
    cout << (10 > 5) + (3 < 1) * 2 << endl;
    cout << 7 % 3 * 2 + 1 << endl;
    return 0;
}
```

Output:

```
11
1
3
```

**Giải thích từng biểu thức:**

**①** `2 + 3 * 4 - 6 / 2`
```
Uu tien: * va / truoc, + va - sau
= 2 + (3*4) - (6/2)
= 2 + 12 - 3
= 11
```

**②** `(10 > 5) + (3 < 1) * 2`
```
(10 > 5) -> true  -> 1
(3 < 1)  -> false -> 0
= 1 + 0 * 2
= 1 + 0
= 1
```
Điểm mấu chốt: kết quả so sánh trong C++ là **số** (1 hoặc 0), nên cộng/nhân được.

**③** `7 % 3 * 2 + 1`
```
% va * cung do uu tien, tinh TU TRAI SANG PHAI
= (7 % 3) * 2 + 1
= 1 * 2 + 1
= 3
```

**Bảng ưu tiên toán tử (từ cao xuống thấp) — phần hay dùng:**

| Mức | Toán tử | Chiều kết hợp |
|---|---|---|
| 1 | `()` `[]` `.` `->` | Trái → phải |
| 2 | `++` `--` (tiền tố), `!` `~`, `-` (dấu âm), ép kiểu | Phải → trái |
| 3 | `*` `/` `%` | Trái → phải |
| 4 | `+` `-` | Trái → phải |
| 5 | `<<` `>>` (dịch bit) | Trái → phải |
| 6 | `<` `<=` `>` `>=` | Trái → phải |
| 7 | `==` `!=` | Trái → phải |
| 8 | `&` → `^` → `\|` | Trái → phải |
| 9 | `&&` | Trái → phải |
| 10 | `\|\|` | Trái → phải |
| 11 | `?:` (3 ngôi) | Phải → trái |
| 12 | `=` `+=` `-=` … | Phải → trái |

✅ **Lời khuyên thực tế:** đừng học thuộc bảng này. **Cứ đặt ngoặc** cho rõ ràng — code dễ đọc hơn và không bao giờ sai:

```cpp
// Thay vi:  if (a & 1 == 0)      <- SAI! == uu tien hon &
// Hay viet: if ((a & 1) == 0)    <- dung va ro rang
```

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double x;
    cout << "Nhap so thuc: ";
    cin >> x;

    int    phanNguyen  = (int)x;        // ep kieu -> cat bo phan thap phan
    double phanThapPhan = x - phanNguyen;

    cout << fixed << setprecision(6);
    cout << "Phan nguyen    : " << phanNguyen   << endl;
    cout << "Phan thap phan : " << phanThapPhan << endl;
    return 0;
}
```

Ví dụ `x = 3.75`:

```
Phan nguyen    : 3
Phan thap phan : 0.750000
```

⚠️ **Với số âm:** `x = -3.75` → phần nguyên `-3`, phần thập phân `-0.75`. Ép `(int)` **cắt về phía 0** (truncate), không phải làm tròn xuống.

Muốn phần thập phân luôn dương:

```cpp
#include <cmath>
int phanNguyen = (int)floor(x);          // -4 voi x = -3.75
double phanThapPhan = x - phanNguyen;    // 0.25, luon >= 0
```

⚠️ Còn một điểm cần lưu ý: do sai số biểu diễn số thực, `0.1 + 0.2 - 0` có thể ra `0.30000000000000004`. Đừng ngạc nhiên nếu phần thập phân in ra hơi lệch ở chữ số cuối.

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a, b;
    cout << "Giai phuong trinh ax + b = 0" << endl;
    cout << "Nhap a va b: ";
    cin >> a >> b;

    cout << fixed << setprecision(4);

    // a = 0 : phuong trinh suy bien
    //   b = 0 -> 0 = 0 -> vo so nghiem
    //   b != 0 -> 0 = -b (vo ly) -> vo nghiem
    // a != 0 -> nghiem duy nhat x = -b/a

    const double EPS = 1e-9;

    if (fabs(a) < EPS) {
        cout << (fabs(b) < EPS ? "Phuong trinh co VO SO nghiem"
                               : "Phuong trinh VO NGHIEM") << endl;
    } else {
        cout << "Nghiem duy nhat: x = " << -b / a << endl;
    }

    return 0;
}
```

Phiên bản chỉ dùng toán tử 3 ngôi (như đề yêu cầu):

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double a, b;
    cin >> a >> b;
    const double EPS = 1e-9;

    fabs(a) < EPS
        ? (fabs(b) < EPS ? cout << "Vo so nghiem\n" : cout << "Vo nghiem\n")
        : cout << "x = " << -b / a << "\n";

    return 0;
}
```

Kiểm thử:

| a | b | Kết quả |
|---|---|---|
| 2 | −6 | x = 3.0000 |
| 0 | 0 | Vô số nghiệm |
| 0 | 5 | Vô nghiệm |
| −3 | 9 | x = 3.0000 |

⚠️ **Điểm quan trọng:** dùng `fabs(a) < EPS` chứ **không** dùng `a == 0`, vì `a` là số thực (xem bài [02-02](../02-02-cpp-kieu-du-lieu.md) bài 8). Đây là chi tiết mà rất nhiều lời giải trên mạng bỏ qua và bị sai khi chấm tự động.

**Bản dùng `if` bình thường dễ đọc hơn nhiều** — toán tử 3 ngôi lồng nhau chỉ nên dùng khi biểu thức rất ngắn.
