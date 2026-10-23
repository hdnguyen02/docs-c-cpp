# Lời giải — [C++]. Tham Chiếu Và Tham Trị

[← Quay lại bài học](../05-03-c-tham-chieu-va-tham-tri.md)

> **Tham trị (pass by value):** hàm nhận một **bản sao** → sửa không ảnh hưởng biến gốc.
> **Tham chiếu (pass by reference, dấu `&`):** hàm làm việc trực tiếp trên **chính biến gốc**.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

void tangGapDoi(int x) {        // THAM TRI - nhan ban sao
    x = x * 2;
    cout << "  Trong ham (tham tri)    : x = " << x << endl;
}

void tangGapDoi2(int &x) {      // THAM CHIEU - lam viec tren bien goc
    x = x * 2;
    cout << "  Trong ham (tham chieu)  : x = " << x << endl;
}

int main() {
    int a = 5;
    cout << "Truoc khi goi : a = " << a << endl;
    tangGapDoi(a);
    cout << "Sau tham tri  : a = " << a << endl;

    cout << endl;
    int b = 5;
    cout << "Truoc khi goi : b = " << b << endl;
    tangGapDoi2(b);
    cout << "Sau tham chieu: b = " << b << endl;
    return 0;
}
```

Output:

```
Truoc khi goi : a = 5
  Trong ham (tham tri)    : x = 10
Sau tham tri  : a = 5          <- KHONG DOI

Truoc khi goi : b = 5
  Trong ham (tham chieu)  : x = 10
Sau tham chieu: b = 10         <- DA DOI
```

**Sơ đồ bộ nhớ:**

```
THAM TRI:
   main:  a [5]
             | sao chep
   ham:   x [5] -> [10]      (x la o nho KHAC, sua x khong anh huong a)

THAM CHIEU:
   main:  b [5]
             ^
   ham:   x --'                (x chi la TEN GOI KHAC cua b)
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

void hoanDoi(int &a, int &b) {
    int tam = a;
    a = b;
    b = tam;
}

int main() {
    int x = 10, y = 20;
    cout << "Truoc: x = " << x << ", y = " << y << endl;
    hoanDoi(x, y);
    cout << "Sau  : x = " << x << ", y = " << y << endl;
    return 0;
}
```

Output:

```
Truoc: x = 10, y = 20
Sau  : x = 20, y = 10
```

Đây chính là cách `std::swap` được cài đặt.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

void hoanDoiSai(int a, int b) {     // THAM TRI - khong hoat dong
    int tam = a;
    a = b;
    b = tam;
    cout << "  Trong ham: a = " << a << ", b = " << b << endl;
}

int main() {
    int x = 10, y = 20;
    cout << "Truoc: x = " << x << ", y = " << y << endl;
    hoanDoiSai(x, y);
    cout << "Sau  : x = " << x << ", y = " << y << endl;
    return 0;
}
```

Output:

```
Truoc: x = 10, y = 20
  Trong ham: a = 20, b = 10     <- hoan doi DUNG, nhung...
Sau  : x = 10, y = 20           <- ...x va y KHONG DOI
```

**Giải thích:** khi gọi `hoanDoiSai(x, y)`, C++ tạo **2 biến mới** `a` và `b`, sao chép giá trị của `x` và `y` vào. Hàm hoán đổi `a` với `b` — thành công, nhưng đó là 2 bản sao. Khi hàm kết thúc, `a` và `b` bị huỷ, `x` và `y` không hề bị đụng tới.

Đây là lý do **bắt buộc** phải dùng tham chiếu khi hàm cần sửa đối số.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

void tinhTongHieu(int a, int b, int &tong, int &hieu) {
    tong = a + b;
    hieu = a - b;
}

int main() {
    int a = 15, b = 4;
    int tong, hieu;

    tinhTongHieu(a, b, tong, hieu);

    cout << "Tong = " << tong << endl;    // 19
    cout << "Hieu = " << hieu << endl;    // 11
    return 0;
}
```

**Đây là cách kinh điển để hàm "trả về nhiều giá trị"** trong C/C++.

💡 Cách C++ hiện đại hơn — dùng `pair` hoặc `struct`:

```cpp
pair<int,int> tinhTongHieu(int a, int b) {
    return {a + b, a - b};
}
auto [tong, hieu] = tinhTongHieu(15, 4);   // C++17
```

Cách này rõ hơn vì nhìn vào **kiểu trả về** là biết hàm cho ra cái gì, thay vì phải đọc danh sách tham số.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

void nhapMang(int a[], int &n) {
    cout << "Nhap so phan tu: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        cout << "  a[" << i << "] = ";
        cin >> a[i];
    }
}

int main() {
    int a[100];
    int n;

    nhapMang(a, n);

    cout << "Mang vua nhap (" << n << " phan tu): ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

⚠️ **`n` BẮT BUỘC phải là tham chiếu.** Nếu viết `void nhapMang(int a[], int n)` thì `n` trong `main` sẽ không được cập nhật — giá trị rác, và vòng lặp in ra sẽ sai hoặc crash.

💡 Mảng `a` **không cần** dấu `&` vì mảng vốn đã được truyền theo kiểu địa chỉ (xem bài 10).

### Bài 6.

```cpp
#include <iostream>
using namespace std;

void timMinMax(int a[], int n, int &mn, int &mx) {
    if (n <= 0) return;

    mn = mx = a[0];                 // khoi tao bang phan tu DAU TIEN
    for (int i = 1; i < n; i++) {
        if (a[i] < mn) mn = a[i];
        if (a[i] > mx) mx = a[i];
    }
}

int main() {
    int a[] = {5, -3, 12, 0, 8, -7, 20};
    int n = 7;
    int mn, mx;

    timMinMax(a, n, mn, mx);

    cout << "Nho nhat = " << mn << endl;   // -7
    cout << "Lon nhat = " << mx << endl;   // 20
    return 0;
}
```

⚠️ **Khởi tạo bằng `a[0]`, không phải bằng 0.** Nếu khởi tạo `mn = 0` thì với mảng toàn số dương, kết quả sẽ sai (ra 0).

💡 Duyệt **một lần** tìm cả min lẫn max, thay vì duyệt 2 lần — nhanh gấp đôi.

### Bài 7.

**Output:**

```
1 11
```

**Giải thích:**

```cpp
void f(int x, int &y) { x += 10; y += 10; }
//       ^tham tri  ^tham chieu

int a = 1, b = 1;
f(a, b);
```

| Tham số | Kiểu truyền | Trong hàm | Sau khi hàm kết thúc |
|---|---|---|---|
| `x` ← `a` | Tham trị | `x` = 1 → 11 | `a` vẫn = **1** (bản sao bị huỷ) |
| `y` ← `b` | Tham chiếu | `y` chính là `b`, 1 → 11 | `b` = **11** |

Bài này cho thấy một hàm có thể **kết hợp** cả tham trị lẫn tham chiếu.

### Bài 8.

```cpp
#include <iostream>
#include <string>
using namespace std;

// ① Tham tri - SAO CHEP toan bo chuoi
void cach1(string s) {
    s += "!!!";                // sua ban sao, chuoi goc khong doi
    cout << "  Trong ham: " << s << endl;
}

// ② Tham chieu - KHONG sao chep, SUA DUOC chuoi goc
void cach2(string &s) {
    s += "!!!";                // sua THAT
}

// ③ Tham chieu hang - KHONG sao chep, KHONG sua duoc
void cach3(const string &s) {
    cout << "  Do dai: " << s.length() << endl;
    // s += "!";               // LOI bien dich neu bo comment
}

int main() {
    string s = "codelab";

    cach1(s);  cout << "Sau cach1: " << s << endl;   // codelab
    cach2(s);  cout << "Sau cach2: " << s << endl;   // codelab!!!
    cach3(s);
    return 0;
}
```

**Bảng so sánh:**

| Cách | Sao chép? | Sửa được gốc? | Nhận hằng số? | Dùng khi |
|---|---|---|---|---|
| `string s` | ✅ **Có** (tốn kém) | ❌ Không | ✅ Có | Cần một bản nháp để sửa mà không đụng gốc |
| `string &s` | ❌ Không | ✅ **Có** | ❌ **Không** | Cần **thay đổi** chuỗi gốc |
| `const string &s` | ❌ Không | ❌ Không | ✅ Có | **Chỉ đọc** — mặc định nên dùng cách này |

**Về hiệu năng:** với chuỗi 1 MB, `string s` phải sao chép 1 MB mỗi lần gọi hàm. `const string &s` chỉ truyền một địa chỉ (8 byte).

**Về tính an toàn:** `const` báo cho compiler *và người đọc* biết hàm không sửa dữ liệu. Nếu lỡ viết code sửa, compiler chặn ngay.

⚠️ **Tham chiếu không `const` không nhận được giá trị tạm thời:**

```cpp
cach2("codelab");          // LOI: cannot bind non-const lvalue reference
cach3("codelab");          // OK
```

✅ **Quy tắc vàng khi thiết kế tham số hàm:**
- Kiểu nhỏ (`int`, `double`, `char`, `bool`) → truyền **tham trị**
- Kiểu lớn (`string`, `vector`, struct) chỉ đọc → **`const T&`**
- Cần sửa → **`T&`**

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

void chuanHoa(string &s) {
    for (char &c : s) {                    // chu y dau & de sua duoc
        c = tolower((unsigned char)c);
    }
}

// Cach ngan gon dung <algorithm>
void chuanHoa2(string &s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
}

int main() {
    string s = "CodeLab DEV C++";
    cout << "Truoc: " << s << endl;

    chuanHoa(s);
    cout << "Sau  : " << s << endl;        // codelab dev c++
    return 0;
}
```

⚠️ **Hai dấu `&` khác nhau ở đây:**
- `string &s` — tham chiếu để sửa chuỗi gốc trong `main`
- `char &c : s` — tham chiếu để sửa từng ký tự trong chuỗi. Không có `&` thì `c` chỉ là bản sao, chuỗi không đổi (xem bài [02-10](../02-10-c-kieu-du-lieu-suy-luan-auto-trong-c.md) bài 9)

⚠️ Ép `(unsigned char)` trước khi gọi `tolower` là thói quen an toàn: `char` có thể âm trên một số hệ thống, và `tolower` với giá trị âm là undefined behavior.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

void thuSuaMang(int a[], int n) {         // KHONG co dau &
    a[0] = 999;
    cout << "  Trong ham: a[0] = " << a[0] << endl;
    cout << "  sizeof(a) trong ham = " << sizeof(a) << " byte" << endl;
}

void thuSuaSo(int x) {                     // tham tri
    x = 999;
}

int main() {
    int a[5] = {1, 2, 3, 4, 5};
    int x = 1;

    cout << "sizeof(a) trong main = " << sizeof(a) << " byte" << endl;

    thuSuaMang(a, 5);
    cout << "Sau khi goi: a[0] = " << a[0] << endl;

    thuSuaSo(x);
    cout << "Sau khi goi: x = " << x << endl;
    return 0;
}
```

Output (máy 64-bit):

```
sizeof(a) trong main = 20 byte
  Trong ham: a[0] = 999
  sizeof(a) trong ham = 8 byte
Sau khi goi: a[0] = 999          <- MANG BI SUA!
Sau khi goi: x = 1               <- SO KHONG BI SUA
```

**Kết luận: mảng luôn được truyền theo kiểu "tham chiếu"** (chính xác hơn: **truyền con trỏ tới phần tử đầu**), dù bạn không viết dấu `&`.

**Bằng chứng:** `sizeof(a)` trong `main` là 20 (5 × 4 byte), nhưng trong hàm chỉ còn **8 byte** — kích thước của một con trỏ. Hiện tượng này gọi là **array decay** (mảng suy biến thành con trỏ).

Ba cách viết sau **hoàn toàn tương đương**:

```cpp
void f(int a[5]);      // so 5 bi BO QUA hoan toan
void f(int a[]);
void f(int *a);        // day moi la ban chat that
```

⚠️ **Hệ quả quan trọng:**
1. Phải luôn truyền kèm kích thước `n` — trong hàm không tính được
2. Hàm có thể vô tình sửa mảng gốc. Muốn bảo vệ, dùng `const int a[]`

💡 Dùng `vector` thì không có vấn đề này: `vector` biết kích thước của chính nó, và mặc định truyền theo **tham trị** (sao chép). Nên với `vector` bạn phải chủ động viết `vector<int>&` khi muốn sửa.

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int& phanTu(int a[], int i) {        // tra ve THAM CHIEU
    return a[i];
}

int main() {
    int a[5] = {10, 20, 30, 40, 50};

    cout << "a[2] = " << phanTu(a, 2) << endl;   // doc: 30

    phanTu(a, 2) = 99;                            // GAN duoc!

    cout << "Sau khi gan, a[2] = " << a[2] << endl;   // 99

    phanTu(a, 0) += 5;                            // van hoat dong
    cout << "a[0] = " << a[0] << endl;            // 15
    return 0;
}
```

**Vì sao gán được:** hàm trả về `int&` nghĩa là nó trả về **chính ô nhớ** `a[i]`, không phải bản sao giá trị. Nên lời gọi hàm có thể đứng ở **vế trái** của phép gán (gọi là *lvalue*).

So sánh:

```cpp
int  phanTuSaoChep(int a[], int i) { return a[i]; }
int& phanTuThamChieu(int a[], int i) { return a[i]; }

phanTuSaoChep(a, 2) = 99;     // LOI: lvalue required as left operand
phanTuThamChieu(a, 2) = 99;   // OK
```

💡 **Đây chính là cách `operator[]` của `vector` và `string` hoạt động** — nhờ nó mà bạn viết được `v[0] = 5;`.

### Bài 12.

```cpp
int& taoSo() {
    int x = 10;
    return x;          // NGUY HIEM!
}
```

**Lỗi nghiêm trọng: trả về tham chiếu tới biến cục bộ (dangling reference).**

Biến `x` là biến **cục bộ**, nằm trên vùng nhớ ngăn xếp (stack) của hàm. Khi hàm kết thúc, vùng nhớ đó bị **thu hồi**. Tham chiếu trả về đang trỏ tới một ô nhớ đã bị huỷ.

```cpp
int main() {
    int y = taoSo();
    cout << y;              // gia tri RAC, hoac 10 do "may man"
    return 0;
}
```

⚠️ **Tính nguy hiểm đặc biệt:** chương trình thường **vẫn chạy** và có thể in ra `10` đúng như mong đợi — vì ô nhớ chưa bị ghi đè. Nhưng chỉ cần gọi thêm một hàm khác là giá trị thành rác. Đây là loại lỗi cực khó tìm.

May mắn là compiler có cảnh báo (với `-Wall`):

```
warning: reference to local variable 'x' returned [-Wreturn-local-addr]
```

**Các cách sửa:**

```cpp
// ① Tra ve theo GIA TRI (dung nhat cho truong hop nay)
int taoSo() { int x = 10; return x; }

// ② Tra ve tham chieu toi bien duoc truyen VAO
int& lay(int &x) { return x; }

// ③ Tra ve tham chieu toi bien static (ton tai suot chuong trinh)
int& taoSo() { static int x = 10; return x; }
```

**Quy tắc an toàn:** chỉ trả về tham chiếu tới thứ **sống lâu hơn** hàm — tham số truyền vào, biến thành viên của lớp, biến `static`, hoặc bộ nhớ động.

Lỗi tương tự với con trỏ:

```cpp
int* taoConTro() {
    int x = 10;
    return &x;          // CUNG NGUY HIEM
}
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

void demChanLe(int a[], int n, int &chan, int &le) {
    chan = le = 0;                       // BAT BUOC khoi tao ve 0
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) chan++;
        else               le++;
    }
}

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, -8, -9};
    int n = 9;
    int chan, le;

    demChanLe(a, n, chan, le);

    cout << "So phan tu chan: " << chan << endl;   // 4  (2,4,6,-8)
    cout << "So phan tu le  : " << le   << endl;   // 5
    return 0;
}
```

⚠️ **Phải khởi tạo `chan = le = 0` bên trong hàm.** Biến `chan`, `le` ở `main` không được khởi tạo — nếu hàm chỉ tăng mà không đặt về 0 trước, kết quả sẽ cộng dồn lên giá trị rác.

⚠️ Dùng `a[i] % 2 == 0` chứ **không** dùng `a[i] % 2 == 1` — vì `-9 % 2` trong C++ bằng `-1`, không phải `1` (xem bài [02-07](../02-07-cpp-toan-tu-operator.md) bài 4).

### Bài 14.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20;

    // THAM CHIEU
    int &ref = a;        // phai gan ngay, khong the doi sang b
    ref = 99;            // sua a
    cout << "a = " << a << endl;           // 99
    // int &ref2;        // LOI: phai khoi tao

    // CON TRO
    int *ptr = &a;       // co the khong gan ngay
    *ptr = 50;           // sua a (can dau *)
    ptr = &b;            // CO THE tro sang bien khac
    *ptr = 60;           // sua b
    cout << "a = " << a << ", b = " << b << endl;   // 50, 60

    int *null = nullptr; // CO THE la rong
    cout << "Con tro rong: " << (null == nullptr) << endl;

    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Tham chiếu `&` | Con trỏ `*` |
|---|---|---|
| **Cú pháp khai báo** | `int &r = a;` | `int *p = &a;` |
| **Truy cập giá trị** | `r` (dùng trực tiếp) | `*p` (phải giải tham chiếu) |
| **Bắt buộc khởi tạo** | ✅ **Có** | ❌ Không |
| **Gán lại cho biến khác** | ❌ **Không thể** | ✅ Có thể |
| **Có thể rỗng (null)** | ❌ Không | ✅ Có (`nullptr`) |
| **Số học (p+1, p++)** | ❌ Không | ✅ Có |
| **Cần kiểm tra null** | ❌ Không | ✅ **Nên kiểm tra** |
| **Dễ đọc** | ✅ Rất dễ | ⚠️ Khó hơn |

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Tham số hàm cần sửa đối số | **Tham chiếu** |
| Tham số lớn chỉ đọc | **`const` tham chiếu** |
| Duyệt mảng, số học địa chỉ | **Con trỏ** |
| Cấp phát động (`new`/`delete`) | **Con trỏ** |
| Giá trị "có thể không tồn tại" | **Con trỏ** (hoặc `std::optional`) |
| Cấu trúc dữ liệu liên kết (danh sách, cây) | **Con trỏ** |

**Bản chất:** tham chiếu thực chất được compiler cài đặt **bằng con trỏ**, nhưng với cú pháp an toàn hơn (không null, không gán lại, không cần `*`). Có thể coi tham chiếu là "con trỏ có kỷ luật".

✅ **Nguyên tắc C++ hiện đại:** *dùng tham chiếu khi có thể, dùng con trỏ khi buộc phải.*

### Bài 15.

```cpp
#include <iostream>
#include <vector>
#include <chrono>
#include <numeric>
using namespace std;
using namespace std::chrono;

// THAM TRI - sao chep toan bo vector moi lan goi
long long tongThamTri(vector<int> v) {
    long long tong = 0;
    for (int x : v) tong += x;
    return tong;
}

// CONST THAM CHIEU - khong sao chep gi
long long tongThamChieu(const vector<int> &v) {
    long long tong = 0;
    for (int x : v) tong += x;
    return tong;
}

int main() {
    const int N = 1000000;
    const int SO_LAN_GOI = 100;

    vector<int> v(N);
    iota(v.begin(), v.end(), 1);        // dien 1, 2, 3, ..., N

    // --- Do thoi gian THAM TRI ---
    auto batDau = high_resolution_clock::now();
    long long tong1 = 0;
    for (int i = 0; i < SO_LAN_GOI; i++) tong1 += tongThamTri(v);
    auto ketThuc = high_resolution_clock::now();
    auto thoiGian1 = duration_cast<milliseconds>(ketThuc - batDau).count();

    // --- Do thoi gian CONST THAM CHIEU ---
    batDau = high_resolution_clock::now();
    long long tong2 = 0;
    for (int i = 0; i < SO_LAN_GOI; i++) tong2 += tongThamChieu(v);
    ketThuc = high_resolution_clock::now();
    auto thoiGian2 = duration_cast<milliseconds>(ketThuc - batDau).count();

    cout << "Vector " << N << " phan tu, goi " << SO_LAN_GOI << " lan:" << endl;
    cout << "  Tham tri        : " << thoiGian1 << " ms" << endl;
    cout << "  Const tham chieu: " << thoiGian2 << " ms" << endl;
    if (thoiGian2 > 0)
        cout << "  Nhanh hon       : " << (double)thoiGian1 / thoiGian2 << " lan" << endl;

    cout << "\n(Kiem tra ket qua giong nhau: " << (tong1 == tong2 ? "OK" : "SAI") << ")" << endl;
    return 0;
}
```

Biên dịch và chạy:

```bash
g++ -std=c++17 -O2 main.cpp -o main
./main
```

Kết quả tham khảo:

```
Vector 1000000 phan tu, goi 100 lan:
  Tham tri        : 285 ms
  Const tham chieu: 62 ms
  Nhanh hon       : 4.6 lan
```

**Giải thích:** mỗi lần gọi `tongThamTri(v)`, C++ phải:
1. Cấp phát 4 MB bộ nhớ mới (1 triệu × 4 byte)
2. Sao chép toàn bộ 1 triệu phần tử
3. Tính tổng
4. Giải phóng 4 MB

Với `const vector<int>&`, bước 1, 2, 4 **biến mất hoàn toàn** — chỉ truyền một địa chỉ 8 byte.

✅ **Bài học thực tế:** đây là một trong những tối ưu **dễ nhất và hiệu quả nhất** trong C++. Chỉ cần thêm `const` và `&` vào tham số là code nhanh lên nhiều lần mà không phải thay đổi logic gì.
