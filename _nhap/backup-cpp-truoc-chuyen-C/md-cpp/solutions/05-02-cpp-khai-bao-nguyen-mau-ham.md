# Lời giải — [C++]. Khai Báo Nguyên Mẫu Hàm

[← Quay lại bài học](../05-02-cpp-khai-bao-nguyen-mau-ham.md)

> **Nguyên mẫu hàm (function prototype)** = lời "báo trước" cho compiler về tên hàm, kiểu trả về và danh sách tham số — chưa có phần thân.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int tong(int a, int b);        // NGUYEN MAU - ket thuc bang dau ;

int main() {
    cout << "3 + 5 = " << tong(3, 5) << endl;
    return 0;
}

int tong(int a, int b) {       // DINH NGHIA - co than ham
    return a + b;
}
```

**Vì sao cần:** compiler đọc file từ trên xuống. Nguyên mẫu cho nó biết "sẽ có một hàm tên `tong`, nhận 2 `int`, trả về `int`" — đủ để kiểm tra lời gọi ở `main` là hợp lệ. Phần thân hàm tìm sau cũng được (ở bước **liên kết**).

### Bài 2.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// ============ NGUYEN MAU ============
int    tong(int a, int b);
int    hieu(int a, int b);
int    tich(int a, int b);
double thuong(int a, int b);
void   inKetQua(int a, int b);

// ============ CHUONG TRINH CHINH ============
int main() {
    int x, y;
    cout << "Nhap 2 so: ";
    cin >> x >> y;
    inKetQua(x, y);
    return 0;
}

// ============ DINH NGHIA ============
int tong(int a, int b)    { return a + b; }
int hieu(int a, int b)    { return a - b; }
int tich(int a, int b)    { return a * b; }

double thuong(int a, int b) {
    if (b == 0) return 0;
    return (double)a / b;
}

void inKetQua(int a, int b) {
    cout << fixed << setprecision(4);
    cout << "Tong   = " << tong(a, b)   << endl;
    cout << "Hieu   = " << hieu(a, b)   << endl;
    cout << "Tich   = " << tich(a, b)   << endl;
    cout << "Thuong = " << thuong(a, b) << endl;
}
```

💡 **Đây là cách tổ chức file được khuyến nghị:** người đọc nhìn phần nguyên mẫu ở đầu là biết ngay chương trình có những chức năng gì, không phải cuộn xuống tìm.

### Bài 3.

**KHÔNG bắt buộc ghi tên tham số** trong nguyên mẫu — compiler chỉ cần biết **kiểu**.

```cpp
#include <iostream>
using namespace std;

int tong(int, int);              // HOP LE - khong co ten tham so
double dienTich(double, double);
void inBang(int, char);

int main() {
    cout << tong(3, 5) << endl;
    return 0;
}

int tong(int a, int b) { return a + b; }
```

Cả hai cách đều biên dịch được:

```cpp
int tong(int a, int b);     // co ten  <- NEN DUNG
int tong(int, int);         // khong ten
```

✅ **Nên ghi tên tham số** vì nó là tài liệu cho người đọc:

```cpp
void veHinhChuNhat(int, int);              // 2 so gi? dai rong? hay toa do?
void veHinhChuNhat(int dai, int rong);     // RO RANG
```

⚠️ Trong **định nghĩa** hàm thì **bắt buộc** phải có tên (trừ khi cố ý không dùng tham số đó).

### Bài 4.

```cpp
int tinhTong(int a, int b);                    // nguyen mau: tra ve int
int main(){ cout << tinhTong(3, 5); return 0; }
double tinhTong(int a, int b){ return a + b; } // dinh nghia: tra ve double
```

**Lỗi:** kiểu trả về trong nguyên mẫu (`int`) **không khớp** với định nghĩa (`double`).

Thông báo lỗi:

```
error: ambiguating new declaration of 'double tinhTong(int, int)'
note: old declaration 'int tinhTong(int, int)'
```

**Sửa:** cho khớp nhau (chọn một trong hai):

```cpp
int tinhTong(int a, int b);
...
int tinhTong(int a, int b) { return a + b; }
```

⚠️ Nhớ rằng **kiểu trả về không tham gia vào nạp chồng hàm** — hai hàm chỉ khác kiểu trả về thì không phải overload mà là **xung đột khai báo**.

Chương trình gốc còn thiếu `#include <iostream>` và `using namespace std;`.

### Bài 5.

```cpp
int f(int x);
int main(){ cout << f(5); return 0; }
// KHONG CO DINH NGHIA cua f
```

**Lỗi:** hàm được **khai báo** nhưng không được **định nghĩa** ở đâu cả.

Điều thú vị: lỗi này **không** xảy ra ở bước biên dịch (compiler tin lời hứa của nguyên mẫu), mà ở bước **liên kết (linking)**:

```
undefined reference to `f(int)'
collect2: error: ld returned 1 exit status
```

**Phân biệt 2 loại lỗi:**

| | Lỗi biên dịch (compile error) | Lỗi liên kết (link error) |
|---|---|---|
| Khi nào | Khi dịch từng file `.cpp` | Khi ghép các file `.o` lại |
| Ví dụ | Thiếu `;`, sai cú pháp, biến chưa khai báo | `undefined reference`, thiếu định nghĩa hàm |
| Thông báo | `error: expected ';'` | `undefined reference to ...` |

Thấy `undefined reference` thì kiểm tra: (1) đã viết định nghĩa hàm chưa, (2) có quên thêm file `.cpp` vào lệnh biên dịch không, (3) tên hàm có gõ sai không.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

// BAT BUOC co nguyen mau - vi 2 ham goi LAN NHAU
bool laChan(int n);
bool laLe(int n);

bool laChan(int n) {
    if (n == 0) return true;
    return laLe(n - 1);          // goi ham dinh nghia BEN DUOI
}

bool laLe(int n) {
    if (n == 0) return false;
    return laChan(n - 1);        // goi ham dinh nghia BEN TREN
}

int main() {
    for (int i = 0; i <= 6; i++) {
        cout << i << ": chan = " << boolalpha << laChan(i)
             << ", le = " << laLe(i) << endl;
    }
    return 0;
}
```

Output:

```
0: chan = true, le = false
1: chan = false, le = true
...
```

**Vì sao BẮT BUỘC phải có nguyên mẫu:** đây là **đệ quy tương hỗ (mutual recursion)** — `laChan` gọi `laLe`, `laLe` gọi `laChan`.

Dù bạn sắp xếp thế nào, cũng sẽ có một hàm gọi hàm được định nghĩa **phía dưới** nó. Không có nguyên mẫu thì không thể biên dịch được:

```
Neu dat laChan truoc  -> no goi laLe (chua biet)  -> LOI
Neu dat laLe truoc    -> no goi laChan (chua biet) -> LOI
```

Đây là trường hợp mà nguyên mẫu không phải "tuỳ chọn cho đẹp" mà là **bắt buộc kỹ thuật**.

### Bài 7.

**File `hamso.h`:**

```cpp
#ifndef HAMSO_H
#define HAMSO_H

bool laChan(int n);
bool laLe(int n);

#endif
```

**File `hamso.cpp`:**

```cpp
#include "hamso.h"

bool laChan(int n) {
    if (n == 0) return true;
    return laLe(n - 1);
}

bool laLe(int n) {
    if (n == 0) return false;
    return laChan(n - 1);
}
```

**File `main.cpp`:**

```cpp
#include <iostream>
#include "hamso.h"
using namespace std;

int main() {
    for (int i = 0; i <= 6; i++) {
        cout << i << ": chan = " << boolalpha << laChan(i) << endl;
    }
    return 0;
}
```

**Biên dịch — phải liệt kê TẤT CẢ file `.cpp`:**

```bash
g++ -std=c++17 main.cpp hamso.cpp -o chuongtrinh
./chuongtrinh
```

Hoặc biên dịch từng bước:

```bash
g++ -c hamso.cpp -o hamso.o        # dich rieng
g++ -c main.cpp  -o main.o
g++ hamso.o main.o -o chuongtrinh  # lien ket
```

⚠️ **Quên file `.cpp` trong lệnh biên dịch** là nguyên nhân số 1 của lỗi `undefined reference` khi làm dự án nhiều file.

**Lưu ý dấu ngoặc trong `#include`:**

| Cú pháp | Tìm ở đâu |
|---|---|
| `#include <iostream>` | Thư mục thư viện hệ thống |
| `#include "hamso.h"` | **Thư mục hiện tại trước**, rồi mới tới thư viện |

### Bài 8.

**Header guard** ngăn một file `.h` bị chèn vào nhiều lần trong cùng một đơn vị biên dịch.

```cpp
#ifndef HAMSO_H       // Neu chua dinh nghia HAMSO_H thi...
#define HAMSO_H       // ...dinh nghia no ngay (danh dau "da doc file nay")

bool laChan(int n);
bool laLe(int n);

#endif                // ket thuc khoi dieu kien
```

**Vấn đề nếu không có guard:**

```cpp
// file a.h
#include "hamso.h"

// file main.cpp
#include "hamso.h"
#include "a.h"            // a.h lai include hamso.h -> hamso.h duoc doc 2 LAN
```

Với chỉ là nguyên mẫu hàm thì khai báo lại 2 lần vẫn hợp lệ. Nhưng nếu file `.h` chứa `struct`, `class`, hoặc biến toàn cục thì sẽ lỗi:

```
error: redefinition of 'struct SinhVien'
```

**Cách hoạt động:**

```
Lan doc thu 1: HAMSO_H chua duoc dinh nghia -> vao trong, dinh nghia HAMSO_H, doc noi dung
Lan doc thu 2: HAMSO_H DA duoc dinh nghia   -> bo qua toan bo toi #endif
```

**Cách viết hiện đại hơn — `#pragma once`:**

```cpp
#pragma once

bool laChan(int n);
bool laLe(int n);
```

Ngắn gọn hơn và không cần nghĩ tên macro. Nó không nằm trong chuẩn C++ nhưng **mọi compiler phổ biến đều hỗ trợ** (GCC, Clang, MSVC).

💡 **Quy tắc đặt tên macro guard:** viết hoa tên file, thay `.` bằng `_`, thêm hậu tố nếu cần: `HAMSO_H`, `MYPROJECT_UTILS_MATH_H`.

### Bài 9.

| Tiêu chí | Nguyên mẫu (Declaration) | Định nghĩa (Definition) |
|---|---|---|
| **Có thân hàm `{ }`** | ❌ Không | ✅ Có |
| **Kết thúc bằng** | Dấu `;` | Dấu `}` |
| **Số lần được phép** | **Nhiều lần** (miễn giống nhau) | **Đúng một lần** trong toàn chương trình |
| **Tên tham số** | Tuỳ chọn | Bắt buộc (nếu có dùng) |
| **Đặt ở đâu** | Đầu file, hoặc file `.h` | File `.cpp` |
| **Cấp phát bộ nhớ** | ❌ Không | ✅ Có (mã máy của hàm) |
| **Nhiệm vụ** | Báo cho compiler biết hàm tồn tại | Cung cấp mã thực thi cho linker |

```cpp
int tong(int a, int b);          // NGUYEN MAU
int tong(int, int);              // duoc khai bao lai, khong sao
int tong(int a, int b);          // lai lan nua, van khong sao

int tong(int a, int b) {         // DINH NGHIA - chi duoc 1 lan
    return a + b;
}
```

Đây là **Quy tắc Một Định Nghĩa** (ODR — One Definition Rule) của C++.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

void inBang(int n, char kyTu);          // nguyen mau: n, kyTu

int main() {
    inBang(3, '*');
    return 0;
}

void inBang(int soDong, char ky) {      // dinh nghia: soDong, ky - TEN KHAC
    for (int i = 0; i < soDong; i++) {
        for (int j = 0; j < soDong; j++) cout << ky;
        cout << endl;
    }
}
```

**Chương trình CHẠY BÌNH THƯỜNG.** ✅

Output:

```
***
***
***
```

**Vì sao:** compiler chỉ so khớp **kiểu** tham số, không quan tâm tên. Tên tham số trong nguyên mẫu hoàn toàn mang tính tài liệu cho người đọc.

⚠️ Tuy chạy được, đây vẫn là **thói quen xấu** — người đọc nguyên mẫu thấy tên `kyTu` rồi đọc định nghĩa thấy `ky` sẽ bối rối. **Hãy đặt tên giống nhau.**

### Bài 11.

**File `mathlib.h`:**

```cpp
#pragma once

/**
 * @brief Tim uoc chung lon nhat cua 2 so nguyen.
 * @return UCLN (luon khong am). ucln(0,0) = 0.
 */
int ucln(int a, int b);

/**
 * @brief Tim boi chung nho nhat cua 2 so nguyen.
 * @return BCNN, hoac 0 neu mot trong hai so bang 0.
 */
long long bcnn(int a, int b);

/**
 * @brief Kiem tra mot so co phai so nguyen to.
 * @return true neu n la so nguyen to (n >= 2).
 */
bool laNguyenTo(int n);

/**
 * @brief Tinh giai thua n!
 * @return n! voi 0 <= n <= 20, tra ve -1 neu n am.
 */
long long giaiThua(int n);
```

**File `mathlib.cpp`:**

```cpp
#include "mathlib.h"
#include <cmath>

int ucln(int a, int b) {
    a = std::abs(a);
    b = std::abs(b);
    while (b != 0) {
        int tam = a % b;
        a = b;
        b = tam;
    }
    return a;
}

long long bcnn(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return (long long)std::abs(a) / ucln(a, b) * std::abs(b);
}

bool laNguyenTo(int n) {
    if (n < 2) return false;
    if (n < 4) return true;              // 2 va 3
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

long long giaiThua(int n) {
    if (n < 0) return -1;
    long long kq = 1;
    for (int i = 2; i <= n; i++) kq *= i;
    return kq;
}
```

**File `main.cpp`:**

```cpp
#include <iostream>
#include "mathlib.h"
using namespace std;

int main() {
    cout << "ucln(48, 18)   = " << ucln(48, 18)   << endl;   // 6
    cout << "bcnn(4, 6)     = " << bcnn(4, 6)     << endl;   // 12
    cout << "laNguyenTo(97) = " << boolalpha << laNguyenTo(97) << endl;  // true
    cout << "giaiThua(10)   = " << giaiThua(10)   << endl;   // 3628800
    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp mathlib.cpp -o chuongtrinh
```

💡 **Đây chính là cách mọi thư viện C++ được tổ chức:** file `.h` là **giao diện** (những gì người dùng cần biết), file `.cpp` là **cài đặt** (cách làm, người dùng không cần quan tâm).

### Bài 12.

Khi bạn viết `#include <iostream>`, **preprocessor chép toàn bộ nội dung file `iostream`** vào vị trí đó, trước khi biên dịch.

File `iostream` chứa (đơn giản hoá):

```cpp
namespace std {
    class ostream { ... };
    class istream { ... };
    extern ostream cout;         // KHAI BAO doi tuong cout
    extern istream cin;
    ostream& endl(ostream&);     // khai bao ham endl
    ...
}
```

Nói cách khác, **`#include` chính là cách C++ cung cấp "nguyên mẫu" cho toàn bộ thư viện chuẩn.**

Xem thử điều này thật sự xảy ra:

```bash
echo '#include <iostream>' > test.cpp
g++ -E test.cpp | wc -l
# Ket qua: ~30000 dong! (toan bo iostream va cac file no include)
```

**Phần định nghĩa (mã thực thi) ở đâu:** nằm trong thư viện đã biên dịch sẵn `libstdc++`, được linker tự động ghép vào khi bạn dùng `g++`. Đó là lý do bạn không phải làm gì thêm.

**Sơ đồ đầy đủ:**

```
#include <iostream>  ->  khai bao (nguyen mau) cua cout, cin
      +
libstdc++ (co san)   ->  dinh nghia (ma may) cua cout, cin
      =
Chuong trinh chay duoc
```

### Bài 13.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// ===== 3 NGUYEN MAU CUNG TEN, KHAC THAM SO =====
double dienTich(double canh);                            // hinh vuong
double dienTich(double dai, double rong);                // hinh chu nhat
double dienTich(double a, double b, double c);           // tam giac (Heron)

int main() {
    cout << fixed << setprecision(4);
    cout << "Vuong canh 5   : " << dienTich(5.0)            << endl;
    cout << "Chu nhat 5x3   : " << dienTich(5.0, 3.0)       << endl;
    cout << "Tam giac 3,4,5 : " << dienTich(3.0, 4.0, 5.0)  << endl;
    return 0;
}

// ===== DINH NGHIA =====
double dienTich(double canh) {
    return canh * canh;
}

double dienTich(double dai, double rong) {
    return dai * rong;
}

double dienTich(double a, double b, double c) {
    double p = (a + b + c) / 2;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}
```

Nạp chồng hoạt động hoàn toàn bình thường với nguyên mẫu — bạn chỉ cần khai báo đủ cả 3.

### Bài 14.

```cpp
#include <iostream>
using namespace std;

int f(int);                    // nguyen mau: nhan int

int main() {
    cout << f(5) << endl;
    return 0;
}

int f(long x) { return x * 2; }   // dinh nghia: nhan long
```

**Kết quả: lỗi LIÊN KẾT (không phải lỗi biên dịch).**

```
undefined reference to `f(int)'
```

**Giải thích:** C++ coi `f(int)` và `f(long)` là **hai hàm hoàn toàn khác nhau** (đây chính là nạp chồng hàm). Nên:

1. Compiler thấy nguyên mẫu `f(int)`, tin là có hàm này → lời gọi `f(5)` hợp lệ
2. Compiler thấy định nghĩa `f(long)` → đó là hàm khác, không liên quan
3. Linker đi tìm mã của `f(int)` → **không có** → báo lỗi

**Chứng minh C++ coi chúng là 2 hàm khác nhau** — xem tên đã "trang trí" (name mangling):

```bash
nm chuongtrinh.o | c++filt
# f(long)          <- co dinh nghia
# U f(int)         <- Undefined, chi co loi goi
```

**Sửa:** cho nguyên mẫu và định nghĩa **khớp hoàn toàn**:

```cpp
int f(int);
...
int f(int x) { return x * 2; }
```

💡 Đây là lý do thực tế người ta luôn đặt nguyên mẫu trong file `.h` và **`#include` chính file `.h` đó vào file `.cpp` định nghĩa** — nếu lệch nhau, compiler sẽ báo lỗi ngay thay vì để linker phát hiện muộn.

### Bài 15.

```cpp
/*
 * ============================================================
 *  Ten file  : quanly_sach.cpp
 *  Tac gia   : Nguyen Van A
 *  Ngay      : 17/09/2026
 *  Mo ta     : Chuong trinh quan ly danh sach sach don gian:
 *              nhap, hien thi, tim kiem, sap xep, thong ke.
 *  Bien dich : g++ -std=c++17 -Wall quanly_sach.cpp -o quanly
 * ============================================================
 */

// ==================== THU VIEN ====================
#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
using namespace std;

// ==================== HANG SO ====================
const int MAX_SACH = 100;

// ==================== NGUYEN MAU HAM ====================
void      hienMenu();
int       nhapSach(string ten[], string tacGia[], long long gia[], int soLuong);
void      hienThiTatCa(const string ten[], const string tacGia[],
                       const long long gia[], int n);
int       timTheoTen(const string ten[], int n, const string& canTim);
void      sapXepTheoGia(string ten[], string tacGia[], long long gia[], int n);
long long tongGiaTri(const long long gia[], int n);
double    giaTrungBinh(const long long gia[], int n);

// ==================== CHUONG TRINH CHINH ====================
int main() {
    string    ten[MAX_SACH];
    string    tacGia[MAX_SACH];
    long long gia[MAX_SACH];
    int n = 0;
    int chon;

    do {
        hienMenu();
        cin >> chon;

        switch (chon) {
            case 1: {
                int them;
                cout << "So sach muon them: ";
                cin >> them;
                n = nhapSach(ten, tacGia, gia, them);
                break;
            }
            case 2:
                hienThiTatCa(ten, tacGia, gia, n);
                break;
            case 3: {
                string canTim;
                cout << "Nhap ten sach can tim (viet lien): ";
                cin >> canTim;
                int vt = timTheoTen(ten, n, canTim);
                if (vt == -1) cout << ">> Khong tim thay!" << endl;
                else cout << ">> Tim thay tai vi tri " << vt + 1
                          << ": " << ten[vt] << " - " << gia[vt] << " VND" << endl;
                break;
            }
            case 4:
                sapXepTheoGia(ten, tacGia, gia, n);
                cout << ">> Da sap xep theo gia tang dan." << endl;
                hienThiTatCa(ten, tacGia, gia, n);
                break;
            case 5:
                cout << fixed << setprecision(0);
                cout << ">> Tong so sach   : " << n << endl;
                cout << ">> Tong gia tri   : " << tongGiaTri(gia, n) << " VND" << endl;
                cout << ">> Gia trung binh : " << giaTrungBinh(gia, n) << " VND" << endl;
                break;
            case 0:
                cout << ">> Tam biet!" << endl;
                break;
            default:
                cout << ">> Lua chon khong hop le!" << endl;
        }
    } while (chon != 0);

    return 0;
}

// ==================== DINH NGHIA HAM ====================

void hienMenu() {
    cout << "\n========= QUAN LY SACH =========" << endl;
    cout << "1. Nhap danh sach sach"             << endl;
    cout << "2. Hien thi tat ca"                 << endl;
    cout << "3. Tim sach theo ten"               << endl;
    cout << "4. Sap xep theo gia"                << endl;
    cout << "5. Thong ke"                        << endl;
    cout << "0. Thoat"                           << endl;
    cout << "================================"   << endl;
    cout << "Lua chon: ";
}

int nhapSach(string ten[], string tacGia[], long long gia[], int soLuong) {
    if (soLuong <= 0 || soLuong > MAX_SACH) {
        cout << "So luong khong hop le!" << endl;
        return 0;
    }
    for (int i = 0; i < soLuong; i++) {
        cout << "--- Sach " << i + 1 << " ---" << endl;
        cout << "Ten (viet lien)    : "; cin >> ten[i];
        cout << "Tac gia (viet lien): "; cin >> tacGia[i];
        cout << "Gia (VND)          : "; cin >> gia[i];
    }
    return soLuong;
}

void hienThiTatCa(const string ten[], const string tacGia[],
                  const long long gia[], int n) {
    if (n == 0) { cout << ">> Danh sach trong!" << endl; return; }

    cout << "\n+-----+--------------------+--------------------+--------------+" << endl;
    cout << "| STT | TEN SACH           | TAC GIA            |     GIA (VND)|" << endl;
    cout << "+-----+--------------------+--------------------+--------------+" << endl;
    for (int i = 0; i < n; i++) {
        cout << "| " << left  << setw(3) << i + 1
             << " | " << setw(18) << ten[i]
             << " | " << setw(18) << tacGia[i]
             << " | " << right << setw(12) << gia[i] << " |" << endl;
    }
    cout << "+-----+--------------------+--------------------+--------------+" << endl;
}

int timTheoTen(const string ten[], int n, const string& canTim) {
    for (int i = 0; i < n; i++) {
        if (ten[i] == canTim) return i;
    }
    return -1;                       // quy uoc: -1 = khong tim thay
}

void sapXepTheoGia(string ten[], string tacGia[], long long gia[], int n) {
    // Sap xep noi bot - khi doi cho gia, phai doi cho CA ten va tacGia
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (gia[j] > gia[j + 1]) {
                swap(gia[j],    gia[j + 1]);
                swap(ten[j],    ten[j + 1]);
                swap(tacGia[j], tacGia[j + 1]);
            }
        }
    }
}

long long tongGiaTri(const long long gia[], int n) {
    long long tong = 0;
    for (int i = 0; i < n; i++) tong += gia[i];
    return tong;
}

double giaTrungBinh(const long long gia[], int n) {
    if (n == 0) return 0;
    return (double)tongGiaTri(gia, n) / n;
}
```

**Các điểm đáng học trong chương trình này:**

1. **Cấu trúc file rõ ràng:** header comment → include → hằng số → nguyên mẫu → `main` → định nghĩa
2. **`const` cho tham số chỉ đọc:** `const string ten[]` báo cho người đọc (và compiler) biết hàm không sửa mảng
3. **`const string&` thay vì `string`:** tránh sao chép chuỗi khi truyền tham số
4. **Quy ước trả về `-1`** khi tìm không thấy — rất phổ biến trong C++
5. **`sapXepTheoGia` đổi chỗ cả 3 mảng** — lỗi kinh điển là chỉ đổi mảng giá, làm dữ liệu bị lệch

⚠️ Chương trình này dùng **3 mảng song song** — đây là thiết kế dễ sai. Cách đúng là dùng `struct`:

```cpp
struct Sach {
    string ten, tacGia;
    long long gia;
};
Sach ds[MAX_SACH];        // 1 mang, khong bao gio bi lech du lieu
```
