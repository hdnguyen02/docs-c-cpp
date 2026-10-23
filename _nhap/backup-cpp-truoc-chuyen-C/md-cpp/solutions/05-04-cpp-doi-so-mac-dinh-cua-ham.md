# Lời giải — [C++]. Đối Số Mặc Định Của Hàm

[← Quay lại bài học](../05-04-cpp-doi-so-mac-dinh-cua-ham.md)

> **3 quy tắc vàng:**
> 1. Đối số mặc định phải nằm ở **cuối** danh sách tham số
> 2. Chỉ khai báo giá trị mặc định **một lần** (ở nguyên mẫu, hoặc ở định nghĩa nếu không có nguyên mẫu)
> 3. Khi gọi hàm, chỉ được bỏ qua các tham số **từ phải sang trái**

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

void chao(string ten = "ban") {
    cout << "Xin chao " << ten << "!" << endl;
}

int main() {
    chao();              // Xin chao ban!
    chao("An");          // Xin chao An!
    chao("codelab");     // Xin chao codelab!
    return 0;
}
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

long long luyThua(int a, int n = 2) {
    long long kq = 1;
    for (int i = 0; i < n; i++) kq *= a;
    return kq;
}

int main() {
    cout << "luyThua(5)    = " << luyThua(5)    << endl;   // 25  (5^2)
    cout << "luyThua(2, 10)= " << luyThua(2, 10) << endl;  // 1024
    cout << "luyThua(3, 0) = " << luyThua(3, 0)  << endl;  // 1
    return 0;
}
```

### Bài 3.

```cpp
#include <iostream>
using namespace std;

void inDuongKe(int doDai = 30, char kyTu = '-') {
    for (int i = 0; i < doDai; i++) cout << kyTu;
    cout << endl;
}

int main() {
    inDuongKe();               // 30 dau '-'
    inDuongKe(50);             // 50 dau '-'
    inDuongKe(20, '=');        // 20 dau '='
    inDuongKe(40, '*');        // 40 dau '*'
    return 0;
}
```

Output:

```
------------------------------
--------------------------------------------------
====================
****************************************
```

💡 Không dùng vòng lặp cũng được: `cout << string(doDai, kyTu) << endl;`

### Bài 4.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

double tinhTien(double gia, int soLuong = 1, double giamGia = 0) {
    double tong = gia * soLuong;
    return tong * (1 - giamGia / 100.0);
}

int main() {
    cout << fixed << setprecision(0);
    cout << "1 mon, khong giam    : " << tinhTien(100000)          << endl;
    cout << "5 mon, khong giam    : " << tinhTien(100000, 5)       << endl;
    cout << "5 mon, giam 10%      : " << tinhTien(100000, 5, 10)   << endl;
    return 0;
}
```

Output:

```
1 mon, khong giam    : 100000
5 mon, khong giam    : 500000
5 mon, giam 10%      : 450000
```

💡 **Thứ tự tham số rất quan trọng:** đặt tham số **hay thay đổi nhất** lên trước, tham số **ít thay đổi nhất** (có mặc định) ở sau.

### Bài 5.

```cpp
void f(int a = 1, int b);       // LOI
```

**Lỗi:** tham số có giá trị mặc định phải nằm ở **cuối**, và mọi tham số sau nó cũng phải có mặc định.

Thông báo lỗi:

```
error: default argument missing for parameter 2 of 'void f(int, int)'
```

**Vì sao:** khi bạn gọi `f(5)`, compiler không có cách nào biết `5` là giá trị cho `a` hay cho `b`. Quy tắc "mặc định ở cuối" loại bỏ sự nhập nhằng đó.

**Sửa — chọn một trong hai:**

```cpp
void f(int a, int b = 1);           // dua mac dinh ve cuoi
void f(int a = 1, int b = 2);       // hoac cho ca hai deu co mac dinh
```

### Bài 6.

```cpp
int tong(int a, int b = 10);                    // nguyen mau
...
int tong(int a, int b = 10) { return a + b; }   // LOI: khai bao mac dinh 2 lan
```

**Lỗi:** giá trị mặc định chỉ được khai báo **một lần** trong toàn chương trình.

Thông báo lỗi:

```
error: default argument given for parameter 2 of 'int tong(int, int)'
note: previous specification in 'int tong(int, int)' here
```

**Sửa — đặt mặc định ở NGUYÊN MẪU, bỏ ở định nghĩa:**

```cpp
int tong(int a, int b = 10);          // <- mac dinh o day

int main() {
    cout << tong(5) << endl;          // 15
    return 0;
}

int tong(int a, int b) {              // <- KHONG lap lai mac dinh
    return a + b;
}
```

💡 **Quy ước chuẩn:** trong dự án nhiều file, giá trị mặc định luôn đặt ở **file `.h`** (nguyên mẫu), không đặt ở `.cpp`. Lý do: người dùng thư viện chỉ đọc file `.h`, nên phải thấy được giá trị mặc định ở đó.

### Bài 7.

```cpp
#include <iostream>
#include <string>
using namespace std;

void inMang(int a[], int n, string nhan = "Mang", char ngan = ' ') {
    cout << nhan << ": ";
    for (int i = 0; i < n; i++) {
        cout << a[i];
        if (i < n - 1) cout << ngan;
    }
    cout << endl;
}

int main() {
    int a[5] = {3, 1, 4, 1, 5};

    inMang(a, 5);                            // Mang: 3 1 4 1 5
    inMang(a, 5, "Day so");                  // Day so: 3 1 4 1 5
    inMang(a, 5, "Ket qua", ',');            // Ket qua: 3,1,4,1,5
    inMang(a, 5, "CSV", '|');                // CSV: 3|1|4|1|5
    return 0;
}
```

### Bài 8.

**KHÔNG thể bỏ qua tham số ở giữa.**

```cpp
void f(int a, int b = 2, int c = 3);

f(1);           // OK - b=2, c=3
f(1, 5);        // OK - b=5, c=3
f(1, 5, 7);     // OK
f(1, , 5);      // LOI CU PHAP!
```

Thông báo lỗi:

```
error: expected primary-expression before ',' token
```

**Vì sao:** C++ so khớp tham số theo **vị trí**, từ trái sang phải. Không có cú pháp nào để nói "bỏ qua tham số thứ 2".

**Hệ quả thiết kế:** phải xếp tham số theo thứ tự **giảm dần theo tần suất sử dụng**:

```cpp
// TOT: c it khi doi -> dat cuoi
void ve(int cao, int rong = 10, char kyTu = '*');

// KHONG TOT: neu muon doi kyTu, phai truyen ca rong
ve(5, 10, '#');      // phai lap lai gia tri mac dinh cua rong
```

**Các cách khắc phục khi cần bỏ tham số giữa:**

```cpp
// ① Truyen lai gia tri mac dinh
f(1, 2, 5);

// ② Dung struct tham so (C++20 co designated initializers)
struct ThamSo { int b = 2; int c = 3; };
void f(int a, ThamSo ts = {});
f(1, {.c = 5});          // C++20

// ③ Nap chong ham
void f(int a, int c);    // khong the - trung chu ky
```

Một số ngôn ngữ khác (Python, C#) hỗ trợ **named arguments** giải quyết vấn đề này: `f(1, c=5)`. C++ chưa có.

### Bài 9.

**Cách 1 — nạp chồng hàm:**

```cpp
#include <iostream>
#include <cmath>
using namespace std;

double dienTich(double canh)                         { return canh * canh; }
double dienTich(double dai, double rong)             { return dai * rong; }
double dienTich(double a, double b, double c) {
    double p = (a + b + c) / 2;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}
```

**Cách 2 — đối số mặc định:**

```cpp
double dienTich(double a, double b = 0) {
    if (b == 0) return a * a;      // hinh vuong
    return a * b;                   // hinh chu nhat
}
```

**So sánh:**

| | Nạp chồng | Đối số mặc định |
|---|---|---|
| **Số hàm phải viết** | Nhiều (mỗi trường hợp 1 hàm) | Một |
| **Logic bên trong** | Mỗi hàm một logic riêng, sạch | Phải có `if` phân nhánh |
| **Kiểu tham số khác nhau** | ✅ Được | ❌ Không |
| **Số lượng tham số khác nhau nhiều** | ✅ Phù hợp | ⚠️ Khó |
| **Dễ đọc khi logic khác nhau** | ✅ Rõ hơn | ❌ Rối |
| **Tránh lặp code khi logic giống nhau** | ❌ Phải lặp | ✅ Tốt |

⚠️ **Cách 2 có lỗ hổng:** dùng giá trị `0` làm "cờ đánh dấu" — nếu ai đó thực sự muốn hình chữ nhật rộng 0 thì sao? Đây gọi là **magic value**, một thiết kế không tốt.

✅ **Ở bài này, nạp chồng là lựa chọn đúng** vì 3 trường hợp có **công thức khác nhau hoàn toàn**.

### Bài 10.

```cpp
void f(int a);
void f(int a, int b = 5);
...
f(3);          // LOI: NHAP NHANG
```

**Lỗi:** lời gọi `f(3)` có **2 cách hiểu hợp lệ**:
1. Gọi `f(int a)` với `a = 3`
2. Gọi `f(int a, int b = 5)` với `a = 3`, `b` lấy mặc định = 5

Compiler không có cơ sở để chọn.

Thông báo lỗi:

```
error: call of overloaded 'f(int)' is ambiguous
note: candidate: 'void f(int)'
note: candidate: 'void f(int, int)'
```

**Sửa — chọn một trong hai cách:**

```cpp
// ① Bo doi so mac dinh
void f(int a);
void f(int a, int b);

// ② Bo ham nap chong 1 tham so
void f(int a, int b = 5);
```

⚠️ **Bài học: đừng trộn nạp chồng với đối số mặc định** trên cùng một tên hàm — rất dễ tạo ra nhập nhằng.

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
using namespace std;

string layNgay(int ngay, int thang, int nam = 2026, char ngan = '/') {
    ostringstream oss;
    oss << setfill('0')
        << setw(2) << ngay  << ngan
        << setw(2) << thang << ngan
        << setw(4) << nam;
    return oss.str();
}

int main() {
    cout << layNgay(5, 9)              << endl;   // 05/09/2026
    cout << layNgay(17, 12, 2025)      << endl;   // 17/12/2025
    cout << layNgay(1, 1, 2030, '-')   << endl;   // 01-01-2030
    cout << layNgay(25, 6, 1999, '.')  << endl;   // 25.06.1999
    return 0;
}
```

💡 `ostringstream` (trong `<sstream>`) cho phép dùng cú pháp `<<` quen thuộc để **xây dựng chuỗi** thay vì in ra màn hình. Rất tiện khi cần định dạng. Xem bài [09-07](../09-07-c-stringstream-trong-c-va-ung-dung.md).

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int demSoLanGoi = 0;

int tinhToan() {
    demSoLanGoi++;
    cout << "  [tinhToan() duoc goi lan " << demSoLanGoi << "]" << endl;
    return 42;
}

const int HANG_SO = 100;

void f(int x = 2 * 3)          { cout << "f: x = " << x << endl; }
void g(int x = tinhToan())     { cout << "g: x = " << x << endl; }
void h(int x = HANG_SO * 2)    { cout << "h: x = " << x << endl; }

int main() {
    f();             // x = 6
    g();             // goi tinhToan() -> x = 42
    g();             // goi tinhToan() LAN NUA -> x = 42
    g(99);           // KHONG goi tinhToan() vi da co gia tri
    h();             // x = 200
    return 0;
}
```

Output:

```
f: x = 6
  [tinhToan() duoc goi lan 1]
g: x = 42
  [tinhToan() duoc goi lan 2]
g: x = 42
g: x = 99
h: x = 200
```

**Kết luận:**

✅ Giá trị mặc định **có thể** là:
- Hằng số: `int x = 5`
- Biểu thức hằng: `int x = 2 * 3`
- Hằng số đã khai báo: `int x = HANG_SO * 2`
- **Lời gọi hàm**: `int x = tinhToan()`
- Biến toàn cục / `static`

❌ **Không thể** là biến cục bộ của hàm gọi (nó chưa tồn tại khi hàm được khai báo).

⚠️ **Điểm quan trọng:** nếu mặc định là lời gọi hàm, hàm đó được gọi **mỗi lần** bạn dùng giá trị mặc định (không phải một lần rồi nhớ). Nếu hàm đó có tác dụng phụ hoặc tốn thời gian, đây có thể là bẫy hiệu năng.

### Bài 13.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

void sapXep(int a[], int n, bool tangDan = true) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            bool caNDoiCho = tangDan ? (a[j] > a[j+1]) : (a[j] < a[j+1]);
            if (caNDoiCho) swap(a[j], a[j+1]);
        }
    }
}

void inMang(int a[], int n) {
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    cout << "Ban dau    : "; inMang(a, n);

    sapXep(a, n);              // mac dinh tang dan
    cout << "Tang dan   : "; inMang(a, n);

    sapXep(a, n, false);       // giam dan
    cout << "Giam dan   : "; inMang(a, n);
    return 0;
}
```

Output:

```
Ban dau    : 5 2 9 1 7 
Tang dan   : 1 2 5 7 9 
Giam dan   : 9 7 5 2 1 
```

💡 Với `std::sort`, cùng ý tưởng được thực hiện bằng comparator:

```cpp
sort(a, a + n);                     // tang dan
sort(a, a + n, greater<int>());     // giam dan
```

### Bài 14.

```cpp
#include <iostream>
using namespace std;

void veHCN(int cao, int rong = 0, char kyTu = '*') {
    if (rong <= 0) rong = cao;          // rong = 0 -> ve hinh VUONG

    for (int i = 0; i < cao; i++) {
        for (int j = 0; j < rong; j++) cout << kyTu;
        cout << endl;
    }
    cout << endl;
}

int main() {
    cout << "Hinh vuong 4x4:" << endl;
    veHCN(4);

    cout << "Hinh chu nhat 3x8:" << endl;
    veHCN(3, 8);

    cout << "Hinh chu nhat 3x6 bang dau #:" << endl;
    veHCN(3, 6, '#');
    return 0;
}
```

Output:

```
Hinh vuong 4x4:
****
****
****
****

Hinh chu nhat 3x8:
********
********
********

Hinh chu nhat 3x6 bang dau #:
######
######
######
```

⚠️ Kỹ thuật "dùng 0 làm cờ đánh dấu" ở đây chấp nhận được vì chiều rộng 0 không có ý nghĩa thực tế. Nhưng nói chung nên cẩn thận với **magic value** — nếu 0 là giá trị hợp lệ thì phải dùng cách khác (nạp chồng, hoặc `std::optional`).

### Bài 15.

| Tiêu chí | Đối số mặc định | Nạp chồng hàm |
|---|---|---|
| **Số hàm phải viết** | 1 | Nhiều |
| **Logic bên trong** | Giống nhau, chỉ khác giá trị | Có thể khác hoàn toàn |
| **Kiểu tham số** | Phải cùng kiểu | ✅ Khác kiểu được |
| **Số lượng tham số** | Chỉ thêm ở cuối | ✅ Tự do |
| **Rủi ro lặp code** | ❌ Không | ⚠️ Có |
| **Thay đổi giá trị mặc định** | Sửa 1 chỗ | — |

**✅ Dùng ĐỐI SỐ MẶC ĐỊNH khi:**

Logic **giống hệt nhau**, chỉ khác giá trị tham số:

```cpp
void log(string msg, string muc = "INFO");
void ketNoi(string host, int cong = 8080, int timeout = 30);
void inMang(int a[], int n, char ngan = ' ');
double lamTron(double x, int soChuSo = 2);
```

**✅ Dùng NẠP CHỒNG khi:**

① **Kiểu tham số khác nhau:**

```cpp
void in(int x);
void in(double x);
void in(const string& s);
```

② **Logic khác nhau hoàn toàn:**

```cpp
double dienTich(double canh);                    // canh^2
double dienTich(double dai, double rong);        // dai * rong
double dienTich(double a, double b, double c);   // Heron - khac han
```

③ **Ý nghĩa tham số khác nhau:**

```cpp
void veDuongTron(Point tam, double banKinh);
void veDuongTron(Point p1, Point p2, Point p3);   // 3 diem tren duong tron
```

**⚠️ KHÔNG dùng cả hai cùng lúc** cho một tên hàm — gây nhập nhằng (xem bài 10).

**Trường hợp kết hợp hợp lý** — nạp chồng theo kiểu, mỗi bản có mặc định riêng:

```cpp
void in(int x, int doRong = 5);
void in(const string& s, int doRong = 20);     // OK: khac KIEU tham so dau
```
