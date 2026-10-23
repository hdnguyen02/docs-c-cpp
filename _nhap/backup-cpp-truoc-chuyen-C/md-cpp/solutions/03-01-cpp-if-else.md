# Lời giải — [C++]. If Else

[← Quay lại bài học](../03-01-cpp-if-else.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n > 0)      cout << n << " la so DUONG" << endl;
    else if (n < 0) cout << n << " la so AM" << endl;
    else            cout << "n BANG 0" << endl;

    return 0;
}
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Nhap a va b: ";
    cin >> a >> b;

    if (a > b)      cout << "So lon hon la: " << a << endl;
    else if (b > a) cout << "So lon hon la: " << b << endl;
    else            cout << "Hai so bang nhau" << endl;

    return 0;
}
```

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Nhap 3 so: ";
    cin >> a >> b >> c;

    int lonNhat;
    if (a >= b) {
        if (a >= c) lonNhat = a;
        else        lonNhat = c;
    } else {
        if (b >= c) lonNhat = b;
        else        lonNhat = c;
    }

    cout << "So lon nhat = " << lonNhat << endl;
    return 0;
}
```

**Cách khác — dùng biến tạm, dễ mở rộng cho n số:**

```cpp
int lonNhat = a;
if (b > lonNhat) lonNhat = b;
if (c > lonNhat) lonNhat = c;
```

Cách thứ hai ngắn hơn và mở rộng được cho 10, 100 số (chỉ cần thêm dòng), trong khi `if` lồng nhau sẽ bùng nổ số nhánh.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n % 2 == 0 && n % 3 == 0 && n % 5 == 0) {
        cout << n << " chia het cho ca 2, 3 va 5" << endl;
    } else {
        cout << n << " KHONG chia het cho ca 2, 3 va 5" << endl;
    }
    return 0;
}
```

💡 **Mẹo:** chia hết cho cả 2, 3, 5 tương đương chia hết cho **BCNN(2,3,5) = 30**. Nên có thể viết gọn: `if (n % 30 == 0)`.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    double dtb;
    cout << "Nhap diem trung binh: ";
    cin >> dtb;

    if (dtb < 0 || dtb > 10) {
        cout << "Diem khong hop le!" << endl;
        return 1;
    }

    if      (dtb >= 8.5) cout << "Xep loai: GIOI" << endl;
    else if (dtb >= 7.0) cout << "Xep loai: KHA" << endl;
    else if (dtb >= 5.0) cout << "Xep loai: TRUNG BINH" << endl;
    else                 cout << "Xep loai: YEU" << endl;

    return 0;
}
```

**Điểm quan trọng về thứ tự `else if`:** phải xếp từ điều kiện **chặt nhất xuống lỏng nhất**. Nếu viết ngược lại:

```cpp
if      (dtb >= 5.0) cout << "TRUNG BINH";     // SAI!
else if (dtb >= 7.0) cout << "KHA";            // khong bao gio chay toi
else if (dtb >= 8.5) cout << "GIOI";           // khong bao gio chay toi
```

thì điểm 9.0 cũng bị xếp "TRUNG BÌNH", vì nó thoả điều kiện đầu tiên và `else if` sau không được xét nữa.

Nhờ cơ chế `else if`, ta **không cần** viết `dtb >= 7.0 && dtb < 8.5` — nếu chạy tới nhánh đó thì chắc chắn `dtb < 8.5` rồi.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int tuoi;
    cout << "Nhap tuoi: ";
    cin >> tuoi;

    if      (tuoi < 0)   cout << "Tuoi khong hop le!" << endl;
    else if (tuoi < 6)   cout << "Mam non" << endl;
    else if (tuoi <= 10) cout << "Tieu hoc" << endl;
    else if (tuoi <= 14) cout << "THCS" << endl;
    else if (tuoi <= 17) cout << "THPT" << endl;
    else                 cout << "Dai hoc / Di lam" << endl;

    return 0;
}
```

Ở đây thứ tự ngược lại bài 5: điều kiện xếp **từ nhỏ đến lớn**, vì ta dùng dấu `<`/`<=`.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    cout << "Nhap 3 canh: ";
    cin >> a >> b >> c;

    if (a <= 0 || b <= 0 || c <= 0) {
        cout << "Canh phai la so duong!" << endl;
    } else if (a + b > c && a + c > b && b + c > a) {
        cout << "La tam giac HOP LE" << endl;
    } else {
        cout << "KHONG phai tam giac" << endl;
    }
    return 0;
}
```

**Bất đẳng thức tam giác:** tổng 2 cạnh bất kỳ phải **lớn hơn** (không phải ≥) cạnh còn lại. Nếu bằng nhau (`a + b == c`) thì 3 điểm thẳng hàng, không tạo thành tam giác.

⚠️ Với cạnh là số lớn, `a + b` có thể tràn `int`. Khi đó dùng `long long` hoặc viết `a > c - b`.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long a, b, c;
    cout << "Nhap 3 canh tam giac: ";
    cin >> a >> b >> c;

    bool deu   = (a == b && b == c);
    bool can   = (a == b || b == c || a == c);
    bool vuong = (a*a == b*b + c*c) || (b*b == a*a + c*c) || (c*c == a*a + b*b);

    if      (deu)          cout << "Tam giac DEU" << endl;
    else if (vuong && can) cout << "Tam giac VUONG CAN" << endl;
    else if (vuong)        cout << "Tam giac VUONG" << endl;
    else if (can)          cout << "Tam giac CAN" << endl;
    else                   cout << "Tam giac THUONG" << endl;

    return 0;
}
```

**Thứ tự kiểm tra rất quan trọng:** phải xét **đều** trước (vì tam giác đều cũng là cân), rồi **vuông cân** trước **vuông** và **cân** (vì nó thoả cả hai).

Kiểm thử:

| a | b | c | Kết quả |
|---|---|---|---|
| 5 | 5 | 5 | Đều |
| 3 | 4 | 5 | Vuông |
| 1 | 1 | 1.414… | Vuông cân *(không chính xác với số nguyên)* |
| 5 | 5 | 8 | Cân |
| 4 | 5 | 6 | Thường |

⚠️ Với **số nguyên**, tam giác vuông cân thực tế không tồn tại (cạnh huyền `a√2` luôn vô tỉ). Muốn xử lý số thực, phải so sánh bằng `fabs(x - y) < EPS`.

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    if (c >= 'A' && c <= 'Z') {
        cout << "'" << c << "' la CHU HOA (ASCII " << (int)c << ")" << endl;
    } else if (c >= 'a' && c <= 'z') {
        cout << "'" << c << "' la CHU THUONG (ASCII " << (int)c << ")" << endl;
    } else if (c >= '0' && c <= '9') {
        cout << "'" << c << "' la CHU SO, gia tri = " << (c - '0') << endl;
    } else {
        cout << "'" << c << "' la KY TU DAC BIET (ASCII " << (int)c << ")" << endl;
    }
    return 0;
}
```

**Cơ sở của cách kiểm tra:** trong bảng ASCII, các nhóm ký tự nằm **liên tiếp nhau**:

| Nhóm | Mã ASCII |
|---|---|
| `'0'` … `'9'` | 48 … 57 |
| `'A'` … `'Z'` | 65 … 90 |
| `'a'` … `'z'` | 97 … 122 |

Nên `c >= 'A' && c <= 'Z'` chính là kiểm tra `c` có nằm trong khoảng 65–90.

💡 `c - '0'` đổi ký tự số thành giá trị số: `'7' - '0'` = `55 - 48` = `7`.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int nam;
    cout << "Nhap nam: ";
    cin >> nam;

    bool nhuan;

    if (nam % 4 != 0) {
        nhuan = false;                  // khong chia het 4 -> chac chan khong nhuan
    } else {
        if (nam % 100 != 0) {
            nhuan = true;               // chia het 4, khong chia het 100 -> nhuan
        } else {
            if (nam % 400 == 0) {
                nhuan = true;           // chia het 400 -> nhuan
            } else {
                nhuan = false;          // chia het 100 nhung khong chia het 400
            }
        }
    }

    cout << nam << (nhuan ? " LA " : " KHONG LA ") << "nam nhuan" << endl;
    return 0;
}
```

So sánh với bản gộp bằng toán tử logic:

```cpp
bool nhuan = (nam % 4 == 0 && nam % 100 != 0) || (nam % 400 == 0);
```

Bản gộp ngắn hơn nhiều, nhưng bản `if` lồng thể hiện rõ **luồng suy nghĩ**. Với logic phức tạp hơn, bản lồng dễ debug hơn (đặt breakpoint được ở từng nhánh).

### Bài 11.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double soKwh;
    cout << "Nhap so dien tieu thu (kWh): ";
    cin >> soKwh;

    double tien = 0;

    if (soKwh <= 50) {
        tien = soKwh * 1800;
    } else if (soKwh <= 100) {
        tien = 50 * 1800 + (soKwh - 50) * 1900;
    } else {
        tien = 50 * 1800 + 50 * 1900 + (soKwh - 100) * 2200;
    }

    cout << fixed << setprecision(0);
    cout << "So dien : " << soKwh << " kWh" << endl;
    cout << "Tien dien: " << tien << " VND" << endl;
    return 0;
}
```

Kiểm thử:

| kWh | Tính | Tiền |
|---|---|---|
| 30 | 30 × 1800 | 54.000 |
| 50 | 50 × 1800 | 90.000 |
| 80 | 50×1800 + 30×1900 | 147.000 |
| 150 | 50×1800 + 50×1900 + 50×2200 | 295.000 |

⚠️ **Lỗi phổ biến:** tính `soKwh * 1900` cho toàn bộ khi vượt 50 kWh. Giá bậc thang chỉ áp dụng cho **phần vượt**, nên phải trừ đi: `(soKwh - 50) * 1900`.

### Bài 12.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double tien;
    cout << "Nhap so tien mua hang (VND): ";
    cin >> tien;

    double phanTramGiam;

    if      (tien >= 5000000) phanTramGiam = 15;
    else if (tien >= 2000000) phanTramGiam = 10;
    else if (tien >=  500000) phanTramGiam = 5;
    else                      phanTramGiam = 0;

    double tienGiam  = tien * phanTramGiam / 100;
    double phaiTra   = tien - tienGiam;

    cout << fixed << setprecision(0);
    cout << "-----------------------------" << endl;
    cout << "Tong tien hang : " << setw(12) << tien     << " VND" << endl;
    cout << "Muc giam gia   : " << setw(12) << phanTramGiam << " %" << endl;
    cout << "Duoc giam      : " << setw(12) << tienGiam << " VND" << endl;
    cout << "PHAI TRA       : " << setw(12) << phaiTra  << " VND" << endl;
    cout << "-----------------------------" << endl;
    return 0;
}
```

⚠️ Nhớ thứ tự **từ mức cao xuống thấp**, giống bài 5.

### Bài 13.

```cpp
int n;
cin >> n;
if (n = 0) cout << "Bang khong";       // <- LOI!
else cout << "Khac khong";
```

**Lỗi:** dùng toán tử **gán `=`** thay vì **so sánh `==`**.

Chuyện gì xảy ra:
1. `n = 0` **gán** 0 cho `n` (giá trị người dùng nhập bị xoá!)
2. Biểu thức gán trả về giá trị vừa gán, tức `0`
3. `0` được hiểu là **`false`**
4. → **luôn** vào nhánh `else`, in "Khac khong" với mọi đầu vào

**Sửa:**

```cpp
if (n == 0) cout << "Bang khong";
else cout << "Khac khong";
```

**Cách phòng tránh:**

1. Biên dịch với `-Wall`, compiler sẽ cảnh báo:
```
warning: suggest parentheses around assignment used as truth value
```

2. Dùng **điều kiện Yoda** — đặt hằng số bên trái:
```cpp
if (0 == n) { ... }      // neu lo viet 0 = n thi LOI BIEN DICH ngay
```

Lỗi `=` thay `==` là lỗi kinh điển và nguy hiểm vì **chương trình vẫn chạy**, chỉ cho kết quả sai.

### Bài 14.

```cpp
int n; cin >> n;
if (n > 0);                      // <- dau ; THUA o day!
    cout << "So duong" << endl;
```

**Với `n = 5`** in ra `So duong`. **Nhưng với `n = -3` cũng in ra `So duong`!**

**Giải thích:** dấu `;` ngay sau `if (n > 0)` tạo thành một **câu lệnh rỗng** — đó chính là thân của `if`. Compiler hiểu code này là:

```cpp
if (n > 0) {
    // khong lam gi ca
}
cout << "So duong" << endl;      // <- LUON chay, khong thuoc if
```

Phần thụt lề chỉ đánh lừa mắt người, C++ **không quan tâm thụt lề** (khác Python).

**Sửa:** bỏ dấu `;`

```cpp
if (n > 0)
    cout << "So duong" << endl;
```

✅ **Thói quen phòng tránh: LUÔN dùng dấu ngoặc nhọn `{}` cho thân `if`**, kể cả khi chỉ có 1 câu lệnh:

```cpp
if (n > 0) {
    cout << "So duong" << endl;
}
```

Điều này cũng tránh được lỗi khác: sau này thêm dòng thứ hai vào mà quên thêm `{}`.

Biên dịch với `-Wall -Wextra` sẽ được cảnh báo `warning: suggest braces around empty body in an 'if' statement`.

### Bài 15.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c, d;
    cout << "Nhap 4 so: ";
    cin >> a >> b >> c >> d;

    // Mang bot: moi lan so sanh 2 so ke nhau, so lon "noi" ve cuoi
    // Luot 1: dua so lon nhat ve vi tri d
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);
    if (c > d) swap(c, d);

    // Luot 2: dua so lon thu 2 ve vi tri c
    if (a > b) swap(a, b);
    if (b > c) swap(b, c);

    // Luot 3: sap xep 2 so con lai
    if (a > b) swap(a, b);

    cout << "Sap xep tang dan: " << a << " " << b << " " << c << " " << d << endl;
    return 0;
}
```

Ví dụ nhập `9 3 7 1`:

```
Sap xep tang dan: 1 3 7 9
```

**Đây chính là thuật toán sắp xếp nổi bọt (Bubble Sort)** viết tay, không dùng vòng lặp:

```
Luot 1: 9 3 7 1 -> 3 9 7 1 -> 3 7 9 1 -> 3 7 1 9   (9 ve cuoi)
Luot 2: 3 7 1 9 -> 3 7 1 9 -> 3 1 7 9              (7 ve vi tri ap chot)
Luot 3: 3 1 7 9 -> 1 3 7 9                         (xong)
```

Với 4 số cần `3 + 2 + 1 = 6` phép so sánh. Với `n` số cần `n(n−1)/2` — đó là lý do phải dùng vòng lặp khi `n` lớn (xem chương 6).

Cách viết ngắn gọn hơn dùng mảng và `sort`:

```cpp
int a[4];
for (int i = 0; i < 4; i++) cin >> a[i];
sort(a, a + 4);
for (int i = 0; i < 4; i++) cout << a[i] << " ";
```
