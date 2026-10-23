# Lời giải — [C++]. Lý Thuyết Con Trỏ

[← Quay lại bài học](../07-01-cpp-ly-thuyet-con-tro-sub.md)

> **Con trỏ** là biến lưu **địa chỉ** của một biến khác.
> - `&x` — lấy **địa chỉ** của `x`
> - `*p` — lấy **giá trị** tại địa chỉ `p` (giải tham chiếu)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 42;
    int *p = &x;              // p luu DIA CHI cua x

    cout << "Gia tri cua x       : " << x  << endl;
    cout << "Dia chi cua x (&x)  : " << &x << endl;
    cout << "Gia tri cua p       : " << p  << endl;   // = &x
    cout << "Gia tri p tro toi(*p): " << *p << endl;   // = x
    cout << "Dia chi cua p (&p)  : " << &p << endl;
    return 0;
}
```

Output (địa chỉ thay đổi mỗi lần chạy):

```
Gia tri cua x       : 42
Dia chi cua x (&x)  : 0x7ffd5c3a1b4c
Gia tri cua p       : 0x7ffd5c3a1b4c      <- giong &x
Gia tri p tro toi(*p): 42                 <- giong x
Dia chi cua p (&p)  : 0x7ffd5c3a1b50      <- p cung co dia chi rieng
```

**Sơ đồ bộ nhớ:**

```
Dia chi         Bien      Gia tri
0x...b4c        x         42
0x...b50        p         0x...b4c   ---> tro toi x
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    int *p = &x;

    cout << "Truoc: x = " << x << endl;      // 10

    *p = 99;                                  // sua x THONG QUA con tro

    cout << "Sau  : x = " << x << endl;      // 99
    cout << "       *p = " << *p << endl;    // 99
    return 0;
}
```

💡 `*p = 99` và `x = 99` hoàn toàn tương đương — vì `*p` chính là `x`.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int    *pi = nullptr;
    double *pd = nullptr;
    char   *pc = nullptr;
    bool   *pb = nullptr;

    cout << "sizeof(int*)    = " << sizeof(pi) << " byte" << endl;
    cout << "sizeof(double*) = " << sizeof(pd) << " byte" << endl;
    cout << "sizeof(char*)   = " << sizeof(pc) << " byte" << endl;
    cout << "sizeof(bool*)   = " << sizeof(pb) << " byte" << endl;

    cout << "\nDe so sanh:" << endl;
    cout << "sizeof(int)     = " << sizeof(int)    << " byte" << endl;
    cout << "sizeof(double)  = " << sizeof(double) << " byte" << endl;
    cout << "sizeof(char)    = " << sizeof(char)   << " byte" << endl;
    return 0;
}
```

Output (máy 64-bit):

```
sizeof(int*)    = 8 byte
sizeof(double*) = 8 byte
sizeof(char*)   = 8 byte
sizeof(bool*)   = 8 byte
```

**Nhận xét: mọi con trỏ đều có CÙNG kích thước**, bất kể kiểu nó trỏ tới.

**Vì sao:** con trỏ chỉ lưu một **địa chỉ bộ nhớ** — và địa chỉ luôn có cùng độ dài trên một kiến trúc:
- Máy 64-bit → 8 byte (2⁶⁴ địa chỉ)
- Máy 32-bit → 4 byte (2³² địa chỉ ≈ 4 GB — đây là lý do Windows 32-bit không dùng được quá 4 GB RAM)

**Vậy kiểu của con trỏ để làm gì?** Để compiler biết:
1. Khi giải tham chiếu `*p` thì đọc **bao nhiêu byte**
2. Khi làm số học `p + 1` thì nhảy **bao nhiêu byte**

```cpp
int *pi;     pi + 1  -> nhay 4 byte
double *pd;  pd + 1  -> nhay 8 byte
char *pc;    pc + 1  -> nhay 1 byte
```

### Bài 4.

```cpp
#include <iostream>
using namespace std;

void hoanDoi(int *a, int *b) {
    int tam = *a;
    *a = *b;
    *b = tam;
}

int main() {
    int x = 10, y = 20;
    cout << "Truoc: x = " << x << ", y = " << y << endl;

    hoanDoi(&x, &y);                // truyen DIA CHI

    cout << "Sau  : x = " << x << ", y = " << y << endl;
    return 0;
}
```

So sánh 3 cách hoán đổi:

```cpp
void hoanDoi1(int a, int b)   { int t=a; a=b; b=t; }        // THAM TRI - khong hoat dong
void hoanDoi2(int &a, int &b) { int t=a; a=b; b=t; }        // THAM CHIEU - goi: hoanDoi2(x, y)
void hoanDoi3(int *a, int *b) { int t=*a; *a=*b; *b=t; }    // CON TRO - goi: hoanDoi3(&x, &y)
```

Cách 2 và 3 đều đúng. Cách 2 (**tham chiếu**) dễ đọc hơn và là lựa chọn ưu tiên trong C++; cách 3 (**con trỏ**) là cách duy nhất trong C.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

void tangGiaTri(int *p, int k) {
    if (p == nullptr) return;        // LUON kiem tra con tro rong
    *p += k;
}

int main() {
    int x = 10;
    tangGiaTri(&x, 5);
    cout << "x = " << x << endl;     // 15

    tangGiaTri(nullptr, 5);          // an toan, khong crash
    cout << "Khong crash" << endl;
    return 0;
}
```

✅ **Thói quen tốt: luôn kiểm tra `nullptr` ở đầu hàm nhận con trỏ.**

### Bài 6.

```cpp
int *p;          // con tro CHUA duoc khoi tao -> chua dia chi RAC
*p = 10;         // ghi vao dia chi rac -> CRASH
cout << *p;
```

**Lỗi:** con trỏ `p` chưa được gán địa chỉ nào, nên nó chứa **giá trị rác** — một địa chỉ ngẫu nhiên. Ghi vào đó là ghi vào vùng nhớ không thuộc chương trình.

Kết quả khi chạy:

```
Segmentation fault (core dumped)
```

**Sửa cách 1 — trỏ tới một biến có thật:**

```cpp
int x;
int *p = &x;
*p = 10;
cout << *p;      // 10
```

**Sửa cách 2 — cấp phát bộ nhớ động:**

```cpp
int *p = new int;
*p = 10;
cout << *p;
delete p;        // NHO giai phong
```

**Sửa cách 3 — khởi tạo `nullptr` rồi kiểm tra:**

```cpp
int *p = nullptr;
if (p != nullptr) *p = 10;
else cout << "Con tro rong!" << endl;
```

✅ **Quy tắc vàng: luôn khởi tạo con trỏ** — hoặc bằng địa chỉ thật, hoặc bằng `nullptr`. Không bao giờ để nó "trống".

### Bài 7.

```cpp
#include <iostream>
using namespace std;

void inGiaTri(int *p) {
    if (p == nullptr) {
        cout << "Con tro RONG, khong the truy cap!" << endl;
        return;
    }
    cout << "Gia tri: " << *p << endl;
}

int main() {
    int x = 42;
    int *p1 = &x;
    int *p2 = nullptr;

    inGiaTri(p1);         // Gia tri: 42
    inGiaTri(p2);         // Con tro RONG...

    // Cach viet ngan gon (con tro rong tuong duong false)
    if (p1) cout << "p1 co gia tri" << endl;
    if (!p2) cout << "p2 rong" << endl;

    return 0;
}
```

**`nullptr` (C++11)** là con trỏ rỗng chuẩn. Trước C++11 người ta dùng `NULL` hoặc `0`.

**Vì sao `nullptr` tốt hơn `NULL`:**

```cpp
void f(int x)    { cout << "f(int)"; }
void f(char* p)  { cout << "f(char*)"; }

f(NULL);        // NHAP NHANG - NULL thuc chat la so 0 -> goi f(int)!
f(nullptr);     // RO RANG - goi f(char*)
```

`NULL` được định nghĩa là `0` nên compiler coi nó là số nguyên. `nullptr` có kiểu riêng (`std::nullptr_t`) nên không bao giờ nhầm với số.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int* timMax(int *a, int *b) {
    if (a == nullptr) return b;
    if (b == nullptr) return a;
    return (*a > *b) ? a : b;
}

int main() {
    int x = 10, y = 20;

    int *p = timMax(&x, &y);
    cout << "So lon hon = " << *p << endl;      // 20

    *p = 999;                                    // sua duoc qua con tro tra ve
    cout << "x = " << x << ", y = " << y << endl;   // x=10, y=999
    return 0;
}
```

⚠️ **An toàn vì:** hàm trả về con trỏ tới một trong hai **tham số truyền vào** — chúng sống lâu hơn hàm.

⚠️ **KHÔNG BAO GIỜ** trả về con trỏ tới biến cục bộ:

```cpp
int* nguyHiem() {
    int x = 10;
    return &x;        // x bi huy khi ham ket thuc -> DANGLING POINTER
}
```

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;

    // ① const int *p  -> KHONG sua duoc GIA TRI, sua duoc DIA CHI
    const int *p1 = &a;
    // *p1 = 99;          // LOI: assignment of read-only location
    p1 = &b;              // OK - doi sang tro vao b
    cout << "p1 tro toi: " << *p1 << endl;

    // ② int * const p  -> sua duoc GIA TRI, KHONG doi duoc DIA CHI
    int * const p2 = &a;
    *p2 = 99;             // OK - sua gia tri cua a
    // p2 = &b;           // LOI: assignment of read-only variable 'p2'
    cout << "a sau khi sua qua p2: " << a << endl;

    // ③ const int * const p -> KHONG sua duoc ca hai
    const int * const p3 = &b;
    // *p3 = 99;          // LOI
    // p3 = &a;           // LOI
    cout << "p3 tro toi: " << *p3 << endl;

    return 0;
}
```

**Bảng tổng hợp:**

| Khai báo | Sửa giá trị `*p`? | Đổi địa chỉ `p`? | Cách đọc |
|---|---|---|---|
| `int *p` | ✅ Có | ✅ Có | Con trỏ thường |
| `const int *p` | ❌ Không | ✅ Có | "Con trỏ tới **hằng** int" |
| `int * const p` | ✅ Có | ❌ Không | "**Hằng** con trỏ tới int" |
| `const int * const p` | ❌ Không | ❌ Không | Hằng con trỏ tới hằng int |

💡 **Mẹo đọc — đọc từ PHẢI sang TRÁI:**

```
const int  *  p      ->  p la con tro (*) toi int hang (const int)
int  * const  p      ->  p la con tro HANG (const *) toi int
```

Hoặc quy tắc đơn giản hơn: **`const` đứng trước `*` bảo vệ giá trị, `const` đứng sau `*` bảo vệ con trỏ.**

`const int *p` và `int const *p` là **giống hệt nhau**.

**Ứng dụng phổ biến nhất** — tham số hàm chỉ đọc:

```cpp
void inMang(const int *a, int n);     // ham hua khong sua mang
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

void inTheoKieu(void *p, char kieu) {
    switch (kieu) {
        case 'i': cout << "int   : " << *(int*)p    << endl; break;
        case 'd': cout << "double: " << *(double*)p << endl; break;
        case 'c': cout << "char  : " << *(char*)p   << endl; break;
    }
}

int main() {
    int    a = 42;
    double b = 3.14;
    char   c = 'X';

    void *p;              // con tro "chung chung" - khong biet kieu

    p = &a;  inTheoKieu(p, 'i');
    p = &b;  inTheoKieu(p, 'd');
    p = &c;  inTheoKieu(p, 'c');

    // Khong the giai tham chieu truc tiep
    // cout << *p;        // LOI: 'void*' is not a pointer-to-object type

    return 0;
}
```

**`void*`** là con trỏ "vô kiểu" — nó lưu được địa chỉ của **bất kỳ** kiểu dữ liệu nào, nhưng compiler không biết đó là kiểu gì.

**Hạn chế:**
- Không giải tham chiếu trực tiếp (`*p` báo lỗi) — phải ép kiểu trước
- Không làm số học con trỏ (`p + 1` không biết nhảy bao nhiêu byte)

**Ứng dụng:** dùng trong C để viết hàm tổng quát, ví dụ `malloc` trả về `void*`, `qsort` nhận `void*`.

⚠️ **Trong C++ hiện đại, gần như không bao giờ dùng `void*`.** Thay vào đó dùng **template** (an toàn kiểu):

```cpp
template <typename T>
void in(T giaTri) { cout << giaTri << endl; }
```

### Bài 11.

```cpp
#include <iostream>
using namespace std;

// Cach 1: con tro
void tangGapDoiCT(int *p) {
    if (p) *p *= 2;
}

// Cach 2: tham chieu
void tangGapDoiTC(int &r) {
    r *= 2;
}

int main() {
    int a = 5, b = 5;

    tangGapDoiCT(&a);              // phai co dau &
    tangGapDoiTC(b);               // goi binh thuong

    cout << "a (con tro)   = " << a << endl;   // 10
    cout << "b (tham chieu)= " << b << endl;   // 10

    // Khac biet: con tro co the RONG, tham chieu thi khong
    tangGapDoiCT(nullptr);         // an toan
    // tangGapDoiTC(???);          // khong the truyen "khong co gi"

    // Khac biet: con tro co the tro sang bien khac
    int *p = &a;
    p = &b;                        // OK

    int &r = a;
    r = b;                         // KHONG phai "r tro sang b" ma la "a = b"!
    cout << "a sau r = b: " << a << endl;

    return 0;
}
```

| | Con trỏ `*` | Tham chiếu `&` |
|---|---|---|
| Cú pháp gọi hàm | `f(&x)` | `f(x)` |
| Trong hàm | `*p` | `r` (dùng trực tiếp) |
| Có thể rỗng | ✅ Có | ❌ Không |
| Gán lại cho biến khác | ✅ Có | ❌ Không |
| Bắt buộc khởi tạo | ❌ Không | ✅ Có |
| Dễ đọc | ⚠️ Khó hơn | ✅ Dễ |

✅ **Trong C++: dùng tham chiếu khi có thể, dùng con trỏ khi buộc phải** (cần biểu diễn "không có gì", cần trỏ sang chỗ khác, cần số học địa chỉ, làm việc với bộ nhớ động).

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int binhPhuong(int x) { return x * x; }
int tangGapDoi(int x) { return x * 2; }
int doiDau(int x)     { return -x; }

// Ham nhan CON TRO HAM lam tham so
void apDung(int a[], int n, int (*f)(int)) {
    for (int i = 0; i < n; i++) {
        a[i] = f(a[i]);
    }
}

void inMang(const char* nhan, int a[], int n) {
    cout << nhan << ": ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};

    inMang("Ban dau     ", a, 5);

    apDung(a, 5, binhPhuong);
    inMang("Binh phuong ", a, 5);      // 1 4 9 16 25

    apDung(a, 5, tangGapDoi);
    inMang("Nhan doi    ", a, 5);      // 2 8 18 32 50

    apDung(a, 5, doiDau);
    inMang("Doi dau     ", a, 5);      // -2 -8 -18 -32 -50

    return 0;
}
```

**Cú pháp con trỏ hàm:** `kieu_tra_ve (*ten)(danh_sach_tham_so)`

```cpp
int (*f)(int);          // f la con tro toi ham nhan int, tra ve int
int *f(int);            // KHAC HAN: f la ham tra ve int*
```

💡 **Cách viết C++ hiện đại** — dùng `std::function` hoặc template, nhận được cả lambda:

```cpp
#include <functional>
void apDung(int a[], int n, function<int(int)> f) { ... }

// Goi voi lambda
apDung(a, 5, [](int x) { return x * x + 1; });
```

**Ứng dụng thực tế:** hàm so sánh cho `sort`, callback, bảng phân phối lệnh (dispatch table).

### Bài 13.

```cpp
int x = 10;
int *p = &x;
int **q = &p;
cout << x << " " << *p << " " << **q << endl;
cout << &x << " " << p << " " << *q << endl;
```

**Output:**

```
10 10 10
0x7ffd... 0x7ffd... 0x7ffd...        (ba dia chi GIONG NHAU)
```

**Giải thích:**

```
Dia chi      Bien    Gia tri
0x1000        x       10
0x2000        p       0x1000    ---> tro toi x
0x3000        q       0x2000    ---> tro toi p
```

| Biểu thức | Kết quả | Giải thích |
|---|---|---|
| `x` | 10 | Giá trị của x |
| `*p` | 10 | Giá trị tại 0x1000 = x |
| `**q` | 10 | `*q` = 0x1000 (chính là p), rồi `*(0x1000)` = 10 |
| `&x` | 0x1000 | Địa chỉ của x |
| `p` | 0x1000 | Nội dung của p = địa chỉ x |
| `*q` | 0x1000 | Giá trị tại 0x2000 = nội dung p |
| `q` | 0x2000 | Địa chỉ của p |
| `&q` | 0x3000 | Địa chỉ của q |

💡 **Mẹo hiểu:** mỗi dấu `*` "đi thêm một bước" theo mũi tên. Xem thêm bài [07-02 — Con trỏ cấp 2](../07-02-cpp-con-tro-cap-2.md).

### Bài 14.

```cpp
#include <iostream>
using namespace std;

int* taoConTroTreo() {
    int x = 42;
    return &x;              // x bi HUY khi ham ket thuc!
}

int main() {
    // --- TRUONG HOP 1: tro toi bien cuc bo da bi huy ---
    int *p1 = taoConTroTreo();
    cout << "Gia tri rac: " << *p1 << endl;   // co the la 42, co the la rac

    // --- TRUONG HOP 2: dung con tro sau khi delete ---
    int *p2 = new int(100);
    cout << "Truoc delete: " << *p2 << endl;
    delete p2;
    // cout << *p2;         // DANGLING POINTER - undefined behavior!

    p2 = nullptr;           // <- PHONG TRANH: gan nullptr ngay sau delete
    if (p2) cout << *p2;
    else cout << "p2 da duoc giai phong an toan" << endl;

    // --- TRUONG HOP 3: tro toi phan tu vector sau khi vector mo rong ---
    // vector<int> v = {1,2,3};
    // int *p3 = &v[0];
    // v.push_back(4);      // vector co the cap phat lai -> p3 thanh dangling
    // cout << *p3;         // NGUY HIEM

    return 0;
}
```

**Dangling pointer (con trỏ treo)** là con trỏ trỏ tới vùng nhớ **đã bị giải phóng hoặc huỷ**.

**3 nguyên nhân chính:**

1. **Trả về địa chỉ biến cục bộ** — biến bị huỷ khi hàm kết thúc
2. **Dùng con trỏ sau `delete`** — vùng nhớ đã trả về hệ thống
3. **Container cấp phát lại** — `vector.push_back()` có thể chuyển dữ liệu sang vùng nhớ mới

**Tính nguy hiểm:** chương trình thường **vẫn chạy** và có thể cho kết quả đúng trong lần thử đầu — vì vùng nhớ chưa bị ghi đè. Nhưng nó sẽ crash một cách ngẫu nhiên về sau, cực khó tìm nguyên nhân.

✅ **Cách phòng tránh:**

```cpp
// ① Gan nullptr ngay sau delete
delete p;
p = nullptr;

// ② Khong tra ve con tro toi bien cuc bo
int taoSo() { int x = 42; return x; }       // tra ve GIA TRI

// ③ Dung smart pointer (C++11) - TOT NHAT
#include <memory>
unique_ptr<int> p = make_unique<int>(42);   // tu dong delete khi het pham vi
shared_ptr<int> q = make_shared<int>(42);   // dem so tham chieu

// ④ Dung vector/string thay vi cap phat thu cong
vector<int> v(100);                          // khong can new/delete
```

💡 Phát hiện bằng công cụ:

```bash
g++ -fsanitize=address -g main.cpp -o main
./main
# AddressSanitizer: heap-use-after-free
```

### Bài 15.

| Toán tử | Tên | Ý nghĩa | Ví dụ |
|---|---|---|---|
| `&` | Lấy địa chỉ | Trả về địa chỉ của biến | `int *p = &x;` |
| `*` (khai báo) | Khai báo con trỏ | Báo đây là biến con trỏ | `int *p;` |
| `*` (dùng) | Giải tham chiếu | Lấy **giá trị** tại địa chỉ | `cout << *p;` |
| `->` | Mũi tên | Truy cập thành viên qua con trỏ | `p->ten` (= `(*p).ten`) |
| `[]` | Chỉ số | Truy cập phần tử | `p[i]` (= `*(p + i)`) |
| `+`, `-` | Số học con trỏ | Dịch chuyển theo **số phần tử** | `p + 1` nhảy `sizeof(T)` byte |
| `++`, `--` | Tăng/giảm | Chuyển sang phần tử kế/trước | `p++` |
| `==`, `!=`, `<` | So sánh | So sánh **địa chỉ** | `if (p == nullptr)` |

**Chương trình minh hoạ đầy đủ:**

```cpp
#include <iostream>
#include <string>
using namespace std;

struct SinhVien {
    string ten;
    int diem;
};

int main() {
    // ① & va *
    int x = 42;
    int *p = &x;                    // & lay dia chi
    cout << "*p = " << *p << endl;  // * lay gia tri

    // ② -> voi struct
    SinhVien sv = {"An", 9};
    SinhVien *psv = &sv;
    cout << "Ten: " << psv->ten << endl;        // cach ngan
    cout << "Ten: " << (*psv).ten << endl;      // cach dai, tuong duong

    // ③ [] va so hoc con tro
    int a[5] = {10, 20, 30, 40, 50};
    int *pa = a;                     // ten mang = dia chi phan tu dau

    cout << "pa[2]    = " << pa[2]     << endl;   // 30
    cout << "*(pa+2)  = " << *(pa + 2) << endl;   // 30 - TUONG DUONG
    cout << "a[2]     = " << a[2]      << endl;   // 30

    // ④ ++ de duyet mang
    cout << "Duyet bang con tro: ";
    for (int *q = a; q < a + 5; q++) {
        cout << *q << " ";
    }
    cout << endl;

    // ⑤ Hieu 2 con tro = so phan tu giua chung
    int *dau = &a[0], *cuoi = &a[4];
    cout << "Khoang cach: " << cuoi - dau << " phan tu" << endl;   // 4

    // ⑥ So sanh
    cout << "p == &x? " << (p == &x) << endl;    // 1
    cout << "p rong?  " << (p == nullptr) << endl; // 0

    return 0;
}
```

💡 **Điểm mấu chốt cần nhớ:** `a[i]` thực chất chỉ là cách viết tắt của `*(a + i)`. Đó là lý do mảng và con trỏ liên quan chặt chẽ với nhau — xem bài [07-03](../07-03-cpp-con-tro-va-mang-1-chieu.md).

Thú vị: vì `a[i] = *(a+i) = *(i+a) = i[a]`, nên `2[a]` cũng hợp lệ và bằng `a[2]`! (Tất nhiên đừng bao giờ viết như vậy.)
