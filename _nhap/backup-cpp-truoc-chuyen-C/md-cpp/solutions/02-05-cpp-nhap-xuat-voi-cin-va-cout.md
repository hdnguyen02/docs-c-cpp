# Lời giải — [C++]. Nhập Xuất Với Cin và Cout

[← Quay lại bài học](../02-05-cpp-nhap-xuat-voi-cin-va-cout.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    char ten[50];
    int tuoi;
    double diemTB;

    cout << "Nhap ho ten (viet lien): ";
    cin >> ten;
    cout << "Nhap tuoi: ";
    cin >> tuoi;
    cout << "Nhap diem TB: ";
    cin >> diemTB;

    cout << "Sinh vien " << ten << ", " << tuoi
         << " tuoi, diem TB: " << diemTB << endl;
    return 0;
}
```

*(Sau khi học chương 9, bạn nên dùng `string ten;` thay cho mảng `char`.)*

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cout << "Nhap a va b: ";
    cin >> a >> b;

    cout << "Tong   = " << a + b << endl;
    cout << "Hieu   = " << a - b << endl;
    cout << "Tich   = " << a * b << endl;
    cout << "Thuong = " << (double)a / b << endl;   // ep kieu de co phan thap phan
    return 0;
}
```

Ví dụ chạy:

```
Nhap a va b: 10 3
Tong   = 13
Hieu   = 7
Tich   = 30
Thuong = 3.33333
```

⚠️ Nếu viết `a / b` (cả hai đều `int`) thì được **3** chứ không phải 3.33333 — đây là phép chia nguyên.

### Bài 3.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    const double PI = 3.14159265358979;
    double r;

    cout << "Nhap ban kinh: ";
    cin >> r;

    cout << fixed << setprecision(2);
    cout << "Chu vi    = " << 2 * PI * r << endl;
    cout << "Dien tich = " << PI * r * r << endl;
    return 0;
}
```

Ví dụ:

```
Nhap ban kinh: 3.5
Chu vi    = 21.99
Dien tich = 38.48
```

### Bài 4.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double x;
    cout << "Nhap so thuc: ";
    cin >> x;

    cout << fixed;
    cout << "0  chu so : " << setprecision(0)  << x << endl;
    cout << "3  chu so : " << setprecision(3)  << x << endl;
    cout << "6  chu so : " << setprecision(6)  << x << endl;
    cout << "10 chu so : " << setprecision(10) << x << endl;
    return 0;
}
```

Ví dụ với `x = 3.14159265358979`:

```
0  chu so : 3
3  chu so : 3.142
6  chu so : 3.141593
10 chu so : 3.1415926536
```

**Lưu ý:** `setprecision` **làm tròn**, không cắt bỏ.

### Bài 5.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b, c;
    cout << "Nhap 3 so nguyen: ";
    cin >> a >> b >> c;

    cout << setw(10) << a << endl;
    cout << setw(10) << b << endl;
    cout << setw(10) << c << endl;
    return 0;
}
```

Ví dụ với `12 345 6789`:

```
        12
       345
      6789
```

**Giải thích:** `setw(10)` đặt độ rộng tối thiểu 10 ký tự cho **giá trị ngay sau nó**. Mặc định căn phải nên phần thiếu được đệm dấu cách ở bên trái.

⚠️ `setw` chỉ có tác dụng cho **một** giá trị kế tiếp, khác với `setprecision` và `setfill` (có tác dụng kéo dài).

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b, c;
    cout << "Nhap 3 so nguyen: ";
    cin >> a >> b >> c;

    cout << setfill('*');          // dat ky tu dem, co hieu luc keo dai
    cout << setw(10) << a << endl;
    cout << setw(10) << b << endl;
    cout << setw(10) << c << endl;
    cout << setfill(' ');          // tra lai mac dinh
    return 0;
}
```

Output:

```
********12
*******345
******6789
```

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap so nguyen: ";
    cin >> n;

    cout << setw(8) << setfill('0') << n << endl;
    return 0;
}
```

Ví dụ: nhập `123` → `00000123`

**Ứng dụng:** định dạng mã đơn hàng, mã sinh viên, số hoá đơn — những thứ cần cố định độ dài.

### Bài 8.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n = 5;
    for (int i = 1; i <= 10; i++) {
        cout << setw(2) << n << " x " << setw(2) << i
             << " = " << setw(2) << n * i << endl;
    }
    return 0;
}
```

Output:

```
 5 x  1 =  5
 5 x  2 = 10
 5 x  3 = 15
 5 x  4 = 20
 5 x  5 = 25
 5 x  6 = 30
 5 x  7 = 35
 5 x  8 = 40
 5 x  9 = 45
 5 x 10 = 50
```

*(Nếu chưa học vòng lặp, bạn có thể viết 10 dòng `cout` riêng.)*

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    bool b;
    cout << "Nhap 0 hoac 1: ";
    cin >> b;

    cout << "Dang so   : " << b << endl;
    cout << "Dang chu  : " << boolalpha << b << endl;
    return 0;
}
```

Ví dụ nhập `1`:

```
Dang so   : 1
Dang chu  : true
```

**Lưu ý:** `boolalpha` cũng có hiệu lực kéo dài — mọi `bool` in sau đó đều hiện `true`/`false`. Tắt bằng `noboolalpha`.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    cout << "Ky tu       : " << c << endl;
    cout << "Ma ASCII    : " << (int)c << endl;
    cout << "Ky tu ke tiep: " << (char)(c + 1) << endl;
    return 0;
}
```

Ví dụ nhập `A`:

```
Ky tu       : A
Ma ASCII    : 65
Ky tu ke tiep: B
```

⚠️ Bắt buộc ép `(char)` ở dòng cuối. Nếu viết `c + 1` không ép kiểu, C++ tự nâng lên `int` và in ra **66** thay vì `B`.

### Bài 11.

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    string ten[3]  = {"But bi", "Vo o ly 200 trang", "Thuoc ke 30cm"};
    int    soLuong[3] = {10, 5, 3};
    double donGia[3]  = {5000, 12000, 8500};

    cout << "=========================================================" << endl;
    cout << left  << setw(22) << "TEN HANG"
         << right << setw(8)  << "SL"
         << right << setw(12) << "DON GIA"
         << right << setw(14) << "THANH TIEN" << endl;
    cout << "---------------------------------------------------------" << endl;

    cout << fixed << setprecision(0);
    double tongCong = 0;
    for (int i = 0; i < 3; i++) {
        double thanhTien = soLuong[i] * donGia[i];
        tongCong += thanhTien;
        cout << left  << setw(22) << ten[i]
             << right << setw(8)  << soLuong[i]
             << right << setw(12) << donGia[i]
             << right << setw(14) << thanhTien << endl;
    }

    cout << "---------------------------------------------------------" << endl;
    cout << left << setw(42) << "TONG CONG"
         << right << setw(14) << tongCong << endl;
    cout << "=========================================================" << endl;
    return 0;
}
```

Output:

```
=========================================================
TEN HANG                    SL     DON GIA    THANH TIEN
---------------------------------------------------------
But bi                      10        5000         50000
Vo o ly 200 trang            5       12000         60000
Thuoc ke 30cm                3        8500         25500
---------------------------------------------------------
TONG CONG                                        135500
=========================================================
```

**Điểm mấu chốt:** `left` căn trái (dùng cho cột chữ), `right` căn phải (dùng cho cột số) — cả hai đều có hiệu lực kéo dài cho tới khi bị đổi.

### Bài 12.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int tongGiay;
    cout << "Nhap tong so giay: ";
    cin >> tongGiay;

    int gio   = tongGiay / 3600;
    int phut  = (tongGiay % 3600) / 60;
    int giay  = tongGiay % 60;

    cout << setfill('0');
    cout << setw(2) << gio  << ":"
         << setw(2) << phut << ":"
         << setw(2) << giay << endl;
    return 0;
}
```

Ví dụ:

```
Nhap tong so giay: 3725
01:02:05
```

**Giải thích công thức:**
- `gio = tongGiay / 3600` — mỗi giờ có 3600 giây
- `phut = (tongGiay % 3600) / 60` — lấy phần dư sau khi trừ số giờ, chia 60
- `giay = tongGiay % 60` — phần dư khi chia 60

### Bài 13.

**Output:**

```
1.235
9.877
```

**Giải thích:** `fixed` và `setprecision` là các **sticky manipulator** (bộ điều khiển có hiệu lực kéo dài). Một khi đã đặt, chúng áp dụng cho **mọi lần xuất số thực sau đó** trên cùng luồng `cout`, cho tới khi bạn đổi sang giá trị khác.

Phân loại:

| Loại | Manipulator | Ghi chú |
|---|---|---|
| **Chỉ tác dụng 1 lần** | `setw()` | Phải đặt lại trước mỗi giá trị |
| **Có hiệu lực kéo dài** | `setprecision()`, `setfill()`, `fixed`, `scientific`, `left`, `right`, `boolalpha`, `hex`/`dec`/`oct` | Giữ nguyên cho tới khi đổi |

Muốn quay lại mặc định:

```cpp
cout.unsetf(ios::fixed);        // tat fixed
cout << setprecision(6);        // tra ve mac dinh
cout << defaultfloat;           // C++11: tra ve dinh dang mac dinh
```

### Bài 14.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string ten;

    // CACH SAI
    cout << "Nhap ho ten: ";
    cin >> ten;
    cout << "Ket qua voi cin >> : [" << ten << "]" << endl;

    return 0;
}
```

Nhập `Nguyen Van A` → in ra:

```
Ket qua voi cin >> : [Nguyen]
```

**Nguyên nhân:** toán tử `>>` **dừng lại ở khoảng trắng đầu tiên** (dấu cách, tab, xuống dòng). Nó chỉ đọc được một "từ". Phần `Van A` vẫn còn nằm lại trong bộ đệm bàn phím.

**Cách đúng — dùng `getline`:**

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string ten;
    cout << "Nhap ho ten: ";
    getline(cin, ten);              // doc CA DONG, ke ca dau cach
    cout << "Xin chao, " << ten << "!" << endl;
    return 0;
}
```

⚠️ **Bẫy trôi lệnh:** nếu trước đó có `cin >> n;` thì ký tự Enter còn sót lại sẽ khiến `getline` ngay sau đó đọc được chuỗi rỗng:

```cpp
int tuoi;
string ten;
cin >> tuoi;
cin.ignore();           // <- BAT BUOC: bo ky tu Enter con sot lai
getline(cin, ten);
```

Chủ đề này được nói kỹ ở bài [09-02 — Xử lý trôi lệnh khi nhập chuỗi ký tự](../09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi-ky-tu-c.md).

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
    const int N = 3;
    string ten[N];
    double toan[N], ly[N], hoa[N];

    for (int i = 0; i < N; i++) {
        cout << "--- Sinh vien " << i + 1 << " ---" << endl;
        cout << "Ten (viet lien): ";
        cin >> ten[i];
        cout << "Diem Toan, Ly, Hoa: ";
        cin >> toan[i] >> ly[i] >> hoa[i];
    }

    cout << endl;
    cout << "+------+----------------------+--------+--------+--------+--------+" << endl;
    cout << "| " << left << setw(4) << "STT"
         << " | " << setw(20) << "HO TEN"
         << " | " << right << setw(6) << "TOAN"
         << " | " << setw(6) << "LY"
         << " | " << setw(6) << "HOA"
         << " | " << setw(6) << "DTB" << " |" << endl;
    cout << "+------+----------------------+--------+--------+--------+--------+" << endl;

    cout << fixed << setprecision(2);
    for (int i = 0; i < N; i++) {
        double dtb = (toan[i] + ly[i] + hoa[i]) / 3;
        cout << "| " << left  << setw(4) << i + 1
             << " | " << setw(20) << ten[i]
             << " | " << right << setw(6) << toan[i]
             << " | " << setw(6) << ly[i]
             << " | " << setw(6) << hoa[i]
             << " | " << setw(6) << dtb << " |" << endl;
    }
    cout << "+------+----------------------+--------+--------+--------+--------+" << endl;
    return 0;
}
```

Ví dụ output:

```
+------+----------------------+--------+--------+--------+--------+
| STT  | HO TEN               |   TOAN |     LY |    HOA |    DTB |
+------+----------------------+--------+--------+--------+--------+
| 1    | AnNguyen             |   9.00 |   8.50 |   7.00 |   8.17 |
| 2    | BinhTran             |   6.50 |   7.00 |   8.00 |   7.17 |
| 3    | ChiLe                |   8.00 |   9.50 |   9.00 |   8.83 |
+------+----------------------+--------+--------+--------+--------+
```
