# Lời giải — [C++]. If và Else If

[← Quay lại bài học](../03-02-cpp-if-va-else-if.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int thang;
    cout << "Nhap thang (1-12): ";
    cin >> thang;

    if      (thang >= 1  && thang <= 3)  cout << "Quy I"   << endl;
    else if (thang >= 4  && thang <= 6)  cout << "Quy II"  << endl;
    else if (thang >= 7  && thang <= 9)  cout << "Quy III" << endl;
    else if (thang >= 10 && thang <= 12) cout << "Quy IV"  << endl;
    else                                 cout << "Thang khong hop le!" << endl;

    return 0;
}
```

💡 Cách tính nhanh không cần `if`: `quy = (thang - 1) / 3 + 1`

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int m, y;
    cout << "Nhap thang va nam: ";
    cin >> m >> y;

    if (m < 1 || m > 12) {
        cout << "Thang khong hop le!" << endl;
    } else if (m == 1 || m == 3 || m == 5 || m == 7 ||
               m == 8 || m == 10 || m == 12) {
        cout << 31 << " ngay" << endl;
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        cout << 30 << " ngay" << endl;
    } else {    // m == 2
        bool nhuan = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
        cout << (nhuan ? 29 : 28) << " ngay" << endl;
    }
    return 0;
}
```

💡 **Mẹo nắm đấm:** nắm bàn tay lại, đếm các đốt xương và khe giữa chúng từ ngón trỏ — đốt nhô lên = 31 ngày, khe lõm = 30 ngày (trừ tháng 2). Tháng 8 quay lại đốt đầu tiên.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap thu (2-8): ";
    cin >> n;

    if      (n == 2) cout << "Thu Hai"  << endl;
    else if (n == 3) cout << "Thu Ba"   << endl;
    else if (n == 4) cout << "Thu Tu"   << endl;
    else if (n == 5) cout << "Thu Nam"  << endl;
    else if (n == 6) cout << "Thu Sau"  << endl;
    else if (n == 7) cout << "Thu Bay"  << endl;
    else if (n == 8) cout << "Chu Nhat" << endl;
    else             cout << "Khong hop le!" << endl;

    return 0;
}
```

Đây là trường hợp mà **`switch case` phù hợp hơn** — xem bài [03-03](../03-03-cpp-switch-case.md).

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int diem;
    cout << "Nhap diem (0-100): ";
    cin >> diem;

    if (diem < 0 || diem > 100) { cout << "Diem khong hop le!" << endl; return 1; }

    char xepLoai;
    if      (diem >= 90) xepLoai = 'A';
    else if (diem >= 80) xepLoai = 'B';
    else if (diem >= 70) xepLoai = 'C';
    else if (diem >= 60) xepLoai = 'D';
    else                 xepLoai = 'F';

    cout << "Diem " << diem << " -> Xep loai " << xepLoai << endl;
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    double bmi;
    cout << "Nhap chi so BMI: ";
    cin >> bmi;

    if      (bmi < 18.5) cout << "Thieu can"   << endl;
    else if (bmi < 25.0) cout << "Binh thuong" << endl;
    else if (bmi < 30.0) cout << "Thua can"    << endl;
    else                 cout << "Beo phi"     << endl;

    return 0;
}
```

**Lưu ý mốc:** dùng `bmi < 25.0` chứ không phải `bmi <= 24.9`. Với số thực, giá trị 24.95 sẽ bị **rơi ra ngoài mọi nhánh** nếu dùng 24.9. Các mốc phải **liền nhau** không có khe hở.

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double chieuCao, canNang;
    cout << "Nhap chieu cao (m)  : "; cin >> chieuCao;
    cout << "Nhap can nang (kg)  : "; cin >> canNang;

    if (chieuCao <= 0 || canNang <= 0) {
        cout << "Du lieu khong hop le!" << endl;
        return 1;
    }

    double bmi = canNang / (chieuCao * chieuCao);

    cout << fixed << setprecision(2);
    cout << "Chi so BMI = " << bmi << " -> ";

    if      (bmi < 18.5) cout << "Thieu can"   << endl;
    else if (bmi < 25.0) cout << "Binh thuong" << endl;
    else if (bmi < 30.0) cout << "Thua can"    << endl;
    else                 cout << "Beo phi"     << endl;

    return 0;
}
```

Ví dụ: cao 1.70 m, nặng 65 kg → BMI = 22.49 → Bình thường.

⚠️ Chiều cao phải nhập theo **mét** (1.70), không phải cm (170). Nếu người dùng nhập 170, BMI sẽ ra 0.00.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long a, b, c;
    cin >> a >> b >> c;

    if (a == b && b == c) {
        cout << 1 << endl;                                  // deu
    } else if (a == b || b == c || a == c) {
        cout << 2 << endl;                                  // can
    } else if (a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b) {
        cout << 3 << endl;                                  // vuong
    } else {
        cout << 4 << endl;                                  // thuong
    }
    return 0;
}
```

⚠️ Chú ý thứ tự: tam giác vuông cân thoả cả điều kiện "cân" lẫn "vuông". Với thứ tự trên nó sẽ được xếp là **cân** (in 2). Đề bài này không phân biệt vuông cân nên chấp nhận được; nếu cần thì thêm nhánh riêng như bài [03-01](../03-01-cpp-if-else.md) bài 8.

### Bài 8.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    char thuong = tolower(c);      // doi ve chu thuong de xet cho gon

    if (thuong == 'a' || thuong == 'e' || thuong == 'i' ||
        thuong == 'o' || thuong == 'u') {
        cout << "'" << c << "' la NGUYEN AM" << endl;
    } else if (isalpha(c)) {
        cout << "'" << c << "' la PHU AM" << endl;
    } else if (isdigit(c)) {
        cout << "'" << c << "' la CHU SO" << endl;
    } else {
        cout << "'" << c << "' la KY TU KHAC" << endl;
    }
    return 0;
}
```

Mẹo hay: dùng `tolower(c)` trước để không phải viết cả `'a'` lẫn `'A'` cho mỗi nguyên âm.

Cách gọn hơn nữa với `string::find`:

```cpp
#include <string>
if (string("aeiou").find(tolower(c)) != string::npos) { /* nguyen am */ }
```

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    double t;
    cout << "Nhap nhiet do (do C): ";
    cin >> t;

    if      (t < 0)  cout << "Bang gia"  << endl;
    else if (t <= 15) cout << "Lanh"     << endl;
    else if (t <= 25) cout << "Mat me"   << endl;
    else if (t <= 35) cout << "Nong"     << endl;
    else              cout << "Rat nong" << endl;

    return 0;
}
```

### Bài 10.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double tien;
    int loaiKhach;

    cout << "Nhap so tien: ";
    cin >> tien;
    cout << "Loai khach (1=Thuong, 2=Than thiet, 3=VIP): ";
    cin >> loaiKhach;

    double phanTram;
    string tenLoai;

    if (loaiKhach == 1)      { phanTram = 0;  tenLoai = "Thuong";     }
    else if (loaiKhach == 2) { phanTram = 10; tenLoai = "Than thiet"; }
    else if (loaiKhach == 3) { phanTram = 20; tenLoai = "VIP";        }
    else {
        cout << "Loai khach khong hop le!" << endl;
        return 1;
    }

    double giam    = tien * phanTram / 100;
    double phaiTra = tien - giam;

    cout << fixed << setprecision(0);
    cout << "Loai khach : " << tenLoai  << endl;
    cout << "Giam gia   : " << phanTram << "% (" << giam << " VND)" << endl;
    cout << "Phai tra   : " << phaiTra  << " VND" << endl;
    return 0;
}
```

Nhớ `#include <string>` khi dùng `string tenLoai`.

### Bài 11.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a, b;
    char pt;

    cout << "Nhap so thu nhat: ";  cin >> a;
    cout << "Nhap phep toan (+ - * / %): "; cin >> pt;
    cout << "Nhap so thu hai : ";  cin >> b;

    cout << fixed << setprecision(4);

    if (pt == '+') {
        cout << a << " + " << b << " = " << a + b << endl;
    } else if (pt == '-') {
        cout << a << " - " << b << " = " << a - b << endl;
    } else if (pt == '*') {
        cout << a << " * " << b << " = " << a * b << endl;
    } else if (pt == '/') {
        if (b == 0) cout << "Loi: khong the chia cho 0!" << endl;
        else        cout << a << " / " << b << " = " << a / b << endl;
    } else if (pt == '%') {
        if ((int)b == 0) cout << "Loi: khong the chia du cho 0!" << endl;
        else             cout << (int)a << " % " << (int)b << " = " << (int)a % (int)b << endl;
    } else {
        cout << "Phep toan khong hop le!" << endl;
    }
    return 0;
}
```

⚠️ Toán tử `%` **chỉ áp dụng cho số nguyên** — phải ép `(int)` trước.

⚠️ Luôn kiểm tra chia cho 0 trước khi chia, nếu không chương trình sẽ crash (với số nguyên) hoặc cho `inf`/`nan` (với số thực).

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n (1-999): ";
    cin >> n;

    if (n < 1 || n > 999) {
        cout << "Ngoai pham vi!" << endl;
    } else if (n < 10) {
        cout << n << " co 1 chu so" << endl;
    } else if (n < 100) {
        cout << n << " co 2 chu so" << endl;
    } else {
        cout << n << " co 3 chu so" << endl;
    }
    return 0;
}
```

Cách tổng quát cho số bất kỳ (dùng vòng lặp — chương 4):

```cpp
int demChuSo = 0;
int tam = abs(n);
if (tam == 0) demChuSo = 1;
while (tam > 0) { demChuSo++; tam /= 10; }
```

Hoặc dùng chuỗi: `to_string(n).length()`

### Bài 13.

```cpp
double d; cin >> d;
if (d >= 5.0) cout << "Trung binh";       // <- SAI THU TU
else if (d >= 7.0) cout << "Kha";
else if (d >= 8.5) cout << "Gioi";
```

**Lỗi:** thứ tự các điều kiện bị **ngược**. Với `d = 9.5`:
1. Kiểm tra `9.5 >= 5.0` → **đúng** → in "Trung binh"
2. Vì đã vào nhánh `if`, toàn bộ chuỗi `else if` phía sau **bị bỏ qua**

Điều kiện `d >= 5.0` "nuốt" hết mọi giá trị lớn hơn, nên 2 nhánh sau không bao giờ chạy tới — đó là **mã chết (dead code)**.

**Sửa — xếp từ điều kiện CHẶT NHẤT xuống LỎNG NHẤT:**

```cpp
if      (d >= 8.5) cout << "Gioi";
else if (d >= 7.0) cout << "Kha";
else if (d >= 5.0) cout << "Trung binh";
else               cout << "Yeu";
```

**Quy tắc chung:** với chuỗi `else if` dùng dấu `>=`, xếp mốc **giảm dần**; dùng dấu `<=`, xếp mốc **tăng dần**.

### Bài 14.

**Cách B (`else if`) hiệu quả hơn.**

Với `n = 100`:

| | Cách A (3 `if` riêng) | Cách B (`else if`) |
|---|---|---|
| Số lần kiểm tra | **4 phép so sánh** (`n<10`, `n>=10`, `n<100`, `n>=100`) | **2 phép so sánh** (`n<10` sai, `n<100` sai → vào `else`) |
| Có thể chạy nhiều nhánh | ⚠️ Có (nếu điều kiện chồng lấn) | ❌ Không — chỉ đúng 1 nhánh |
| Điều kiện phải viết đầy đủ | ✅ Phải viết `n >= 10 && n < 100` | ❌ Chỉ cần `n < 100` |

**Sự khác biệt bản chất:**

- **Cách A:** cả 3 điều kiện **đều được kiểm tra**, dù nhánh đầu đã đúng. Nếu các điều kiện chồng lấn, nhiều nhánh có thể cùng chạy — thường là lỗi.
- **Cách B:** khi một nhánh đúng, toàn bộ phần còn lại **bị bỏ qua**. Đảm bảo đúng một nhánh chạy.

Với 3 nhánh thì chênh lệch không đáng kể; nhưng với 50 nhánh thì `else if` tiết kiệm rõ rệt, và quan trọng hơn là **đảm bảo tính loại trừ lẫn nhau**.

✅ **Dùng `if` riêng biệt** chỉ khi các điều kiện **độc lập** và có thể cùng đúng:

```cpp
if (n % 2 == 0) cout << "Chia het 2\n";
if (n % 3 == 0) cout << "Chia het 3\n";     // ca hai cung co the in
```

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int gio, phut;
    cout << "Nhap gio (0-23) va phut: ";
    cin >> gio >> phut;

    if (gio < 0 || gio > 23 || phut < 0 || phut > 59) {
        cout << "Thoi gian khong hop le!" << endl;
        return 1;
    }

    // Xac dinh buoi va loi chao
    string buoi, loiChao;
    if (gio < 5) {
        buoi = "Dem";    loiChao = "Khuya roi, di ngu thoi!";
    } else if (gio < 11) {
        buoi = "Sang";   loiChao = "Chao buoi sang!";
    } else if (gio < 13) {
        buoi = "Trua";   loiChao = "Chao buoi trua!";
    } else if (gio < 18) {
        buoi = "Chieu";  loiChao = "Chao buoi chieu!";
    } else if (gio < 22) {
        buoi = "Toi";    loiChao = "Chao buoi toi!";
    } else {
        buoi = "Dem";    loiChao = "Khuya roi, di ngu thoi!";
    }

    // Doi sang dinh dang 12 gio
    int gio12;
    string amPm;
    if (gio == 0)       { gio12 = 12; amPm = "AM"; }   // 0h = 12 AM
    else if (gio < 12)  { gio12 = gio; amPm = "AM"; }
    else if (gio == 12) { gio12 = 12; amPm = "PM"; }   // 12h = 12 PM
    else                { gio12 = gio - 12; amPm = "PM"; }

    cout << "\n" << loiChao << endl;
    cout << "Gio 24h : " << setw(2) << setfill('0') << gio
         << ":" << setw(2) << gio << ":" << setw(2) << phut << endl;
    cout << setfill(' ');
    cout << "Gio 12h : " << gio12 << ":" << setw(2) << setfill('0') << phut
         << " " << amPm << endl;
    cout << setfill(' ');
    cout << "Buoi    : " << buoi << endl;
    return 0;
}
```

Ví dụ nhập `14 30`:

```
Chao buoi chieu!
Gio 24h : 14:30
Gio 12h : 2:30 PM
Buoi    : Chieu
```

**2 trường hợp đặc biệt hay sai khi đổi sang 12h:**
- `0:30` → **12:30 AM** (không phải 0:30 AM)
- `12:30` → **12:30 PM** (không phải 0:30 PM)
