# Lời giải — [C++]. Con Trỏ Cấp 2

[← Quay lại bài học](../07-02-cpp-con-tro-cap-2.md)

> **Con trỏ cấp 2 (`int **q`)** là con trỏ trỏ tới **một con trỏ khác**.
> Dùng khi cần **thay đổi chính con trỏ** (chứ không chỉ giá trị nó trỏ tới).

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 42;
    int *p = &x;
    int **q = &p;

    cout << "--- GIA TRI ---" << endl;
    cout << "x   = " << x   << endl;      // 42
    cout << "*p  = " << *p  << endl;      // 42
    cout << "**q = " << **q << endl;      // 42

    cout << "\n--- DIA CHI ---" << endl;
    cout << "&x  = " << &x << endl;
    cout << "p   = " << p  << endl;       // = &x
    cout << "*q  = " << *q << endl;       // = p = &x

    cout << "&p  = " << &p << endl;
    cout << "q   = " << q  << endl;       // = &p

    cout << "&q  = " << &q << endl;
    return 0;
}
```

**Sơ đồ bộ nhớ:**

```
Dia chi      Bien    Gia tri
0x1000        x       42
0x2000        p       0x1000  -----> x
0x3000        q       0x2000  -----> p -----> x
```

**Quy tắc:** mỗi dấu `*` đi thêm một bước theo mũi tên.

```
q    = 0x2000    (dia chi cua p)
*q   = 0x1000    (noi dung p = dia chi cua x)
**q  = 42        (noi dung x)
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 10;
    int *p = &x;
    int **q = &p;

    cout << "Truoc: x = " << x << endl;    // 10

    **q = 99;                               // sua x qua 2 cap con tro

    cout << "Sau  : x = " << x << endl;    // 99
    return 0;
}
```

3 cách sau hoàn toàn tương đương: `x = 99`, `*p = 99`, `**q = 99`.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

void doiConTro(int **q, int *moi) {
    *q = moi;          // thay doi CHINH con tro ma q tro toi
}

int main() {
    int a = 10, b = 20;
    int *p = &a;

    cout << "Truoc: *p = " << *p << endl;   // 10

    doiConTro(&p, &b);                       // truyen DIA CHI cua p

    cout << "Sau  : *p = " << *p << endl;   // 20
    return 0;
}
```

💡 So sánh `*q = moi` với `**q = giaTri`:
- `*q = moi` → thay đổi **con trỏ** `p` (cho nó trỏ sang chỗ khác)
- `**q = giaTri` → thay đổi **giá trị** mà `p` đang trỏ tới

### Bài 4.

```cpp
#include <iostream>
using namespace std;

// SAI: nhan con tro CAP 1 - chi thay doi duoc BAN SAO cua con tro
void thuDoiSai(int *p, int *moi) {
    p = moi;                   // chi doi ban sao, khong anh huong ben ngoai
}

// DUNG: nhan con tro CAP 2
void thuDoiDung(int **q, int *moi) {
    *q = moi;
}

int main() {
    int a = 10, b = 20;
    int *p = &a;

    thuDoiSai(p, &b);
    cout << "Sau thuDoiSai : *p = " << *p << endl;    // van 10

    thuDoiDung(&p, &b);
    cout << "Sau thuDoiDung: *p = " << *p << endl;    // 20
    return 0;
}
```

**Giải thích — đây chính là quy tắc tham trị áp dụng cho con trỏ:**

```
thuDoiSai(p, &b):
   main:  p [0x1000]  ---> a
                |  sao chep
   ham:   p [0x1000]  ---> a
          p = moi  ->  ham: p [0x2000] ---> b
          Nhung main: p VAN LA [0x1000]

thuDoiDung(&p, &b):
   main:  p [0x1000]
              ^
   ham:   q --'  (q tro thang vao o nho cua p)
          *q = moi  ->  ghi thang vao o nho cua p
          main: p [0x2000] ---> b   ✔
```

**Nguyên tắc tổng quát:** muốn hàm thay đổi được thứ gì, phải truyền **địa chỉ** của thứ đó.
- Thay đổi `int` → truyền `int*` (hoặc `int&`)
- Thay đổi `int*` → truyền `int**` (hoặc `int*&`)

💡 **Trong C++, dùng tham chiếu tới con trỏ dễ đọc hơn nhiều:**

```cpp
void doiConTro(int *&p, int *moi) {    // tham chieu toi con tro
    p = moi;
}
doiConTro(p, &b);                       // goi binh thuong, khong can &
```

### Bài 5.

```cpp
#include <iostream>
using namespace std;

void capPhat(int **p, int n) {
    *p = new int[n];
    for (int i = 0; i < n; i++) (*p)[i] = i * 10;     // chu y dau ngoac!
}

void giaiPhong(int **p) {
    delete[] *p;
    *p = nullptr;                    // tranh dangling pointer
}

int main() {
    int *a = nullptr;
    int n = 5;

    capPhat(&a, n);

    cout << "Mang: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                    // 0 10 20 30 40

    giaiPhong(&a);
    cout << "Sau giai phong, a = " << (a == nullptr ? "nullptr" : "co gia tri") << endl;
    return 0;
}
```

⚠️ **Chú ý dấu ngoặc: `(*p)[i]` chứ không phải `*p[i]`.**

```
(*p)[i]  ->  lay con tro ma p tro toi, roi truy cap phan tu i   ✔
*p[i]    ->  p[i] truoc (do uu tien [] cao hon *), roi giai tham chieu  ✘
```

💡 Cách C++ hiện đại — dùng tham chiếu hoặc trả về:

```cpp
void capPhat(int *&p, int n) { p = new int[n]; }    // tham chieu toi con tro
int* capPhat(int n) { return new int[n]; }          // tra ve con tro
vector<int> taoMang(int n) { return vector<int>(n); }  // TOT NHAT
```

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 20, c = 30;

    int *arr[3] = {&a, &b, &c};      // MANG cac con tro

    cout << "Gia tri: ";
    for (int i = 0; i < 3; i++) cout << *arr[i] << " ";
    cout << endl;                     // 10 20 30

    // Sua gia tri qua mang con tro
    *arr[1] = 999;
    cout << "b sau khi sua = " << b << endl;    // 999

    // Ten mang chinh la con tro cap 2
    int **p = arr;
    cout << "Qua con tro cap 2: ";
    for (int i = 0; i < 3; i++) cout << **(p + i) << " ";
    cout << endl;                     // 10 999 30

    return 0;
}
```

💡 **Điểm liên hệ quan trọng:** tên mảng `arr` (kiểu `int*[3]`) suy biến thành `int**` khi dùng như con trỏ. Đây là lý do `char **argv` ở bài 8 hoạt động được.

**Ứng dụng thực tế:** sắp xếp mà không di chuyển dữ liệu gốc — chỉ sắp xếp mảng con trỏ.

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n = 3, m = 4;

    // ① Cap phat mang con tro (n hang)
    int **a = new int*[n];

    // ② Cap phat tung hang (moi hang m phan tu)
    for (int i = 0; i < n; i++) {
        a[i] = new int[m];
    }

    // ③ Su dung nhu mang 2 chieu binh thuong
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = i * m + j;

    cout << "Ma tran " << n << "x" << m << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(4) << a[i][j];
        cout << endl;
    }

    // ④ GIAI PHONG - phai lam NGUOC THU TU cap phat
    for (int i = 0; i < n; i++) delete[] a[i];    // giai phong tung hang truoc
    delete[] a;                                    // roi moi giai phong mang con tro
    a = nullptr;

    return 0;
}
```

**Sơ đồ bộ nhớ:**

```
a ---> [ptr0][ptr1][ptr2]          (mang con tro, n phan tu)
         |     |     |
         v     v     v
       [0][1][2][3]                (hang 0, m phan tu)
       [4][5][6][7]                (hang 1)
       [8][9][10][11]              (hang 2)
```

⚠️ **Phải giải phóng đúng thứ tự ngược lại.** Nếu `delete[] a` trước, bạn mất luôn địa chỉ các hàng → **rò rỉ bộ nhớ (memory leak)**.

✅ **Cách C++ hiện đại — đơn giản hơn nhiều:**

```cpp
#include <vector>
vector<vector<int>> a(n, vector<int>(m));
a[i][j] = ...;
// Khong can delete - tu dong giai phong
```

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main(int argc, char **argv) {
    cout << "So tham so (argc) = " << argc << endl;

    for (int i = 0; i < argc; i++) {
        cout << "argv[" << i << "] = " << argv[i] << endl;
    }

    // Tinh tong cac tham so so
    if (argc > 1) {
        long long tong = 0;
        for (int i = 1; i < argc; i++) {
            tong += atoll(argv[i]);      // can <cstdlib>
        }
        cout << "Tong cac tham so = " << tong << endl;
    }
    return 0;
}
```

Biên dịch và chạy:

```bash
g++ main.cpp -o chuongtrinh
./chuongtrinh 10 20 30
```

Output:

```
So tham so (argc) = 4
argv[0] = ./chuongtrinh
argv[1] = 10
argv[2] = 20
argv[3] = 30
Tong cac tham so = 60
```

**Giải thích:**
- `argc` (argument count) — số tham số, **luôn ≥ 1**
- `argv` (argument vector) — mảng các chuỗi
- `argv[0]` **luôn là tên chương trình**
- `argv[argc]` luôn là `nullptr`

`char **argv` chính là "con trỏ tới mảng các chuỗi". Có thể viết tương đương `char *argv[]`.

💡 Trong C++ nên chuyển ngay sang `string` để dễ xử lý:

```cpp
#include <string>
#include <vector>
int main(int argc, char **argv) {
    vector<string> thamSo(argv, argv + argc);
    for (const auto& s : thamSo) cout << s << endl;
}
```

### Bài 9.

```cpp
int a = 1, b = 2;
int *p = &a;
int **q = &p;
*q = &b;
cout << *p << " " << **q << " " << a << " " << b;
```

**Output:**

```
2 2 1 2
```

**Giải thích từng bước:**

```
Ban dau:
   a = 1, b = 2
   p ---> a
   q ---> p ---> a

Sau *q = &b:
   *q chinh la p, nen lenh nay = "p = &b"
   p ---> b
   q ---> p ---> b
   (a VAN BANG 1, khong bi dung toi)
```

| Biểu thức | Giá trị | Vì sao |
|---|---|---|
| `*p` | **2** | `p` giờ trỏ tới `b` = 2 |
| `**q` | **2** | `*q` = `p` → `**q` = `*p` = 2 |
| `a` | **1** | Không hề bị thay đổi |
| `b` | **2** | Không hề bị thay đổi |

⚠️ **Phân biệt rõ:**
- `*q = &b` → đổi **con trỏ** `p` sang trỏ vào `b`
- `**q = 5` → đổi **giá trị** mà `p` đang trỏ tới (tức `a = 5`)

### Bài 10.

```cpp
#include <iostream>
using namespace std;

// Hoan doi 2 CON TRO (khong doi gia tri chung tro toi)
void hoanDoiConTro(int **p1, int **p2) {
    int *tam = *p1;
    *p1 = *p2;
    *p2 = tam;
}

int main() {
    int a = 10, b = 20;
    int *p = &a;
    int *q = &b;

    cout << "Truoc: *p = " << *p << ", *q = " << *q << endl;   // 10, 20
    cout << "       a  = " << a  << ", b  = " << b  << endl;   // 10, 20

    hoanDoiConTro(&p, &q);

    cout << "Sau  : *p = " << *p << ", *q = " << *q << endl;   // 20, 10
    cout << "       a  = " << a  << ", b  = " << b  << endl;   // 10, 20 (KHONG DOI)
    return 0;
}
```

**Điểm mấu chốt:** hoán đổi con trỏ chỉ làm chúng trỏ sang chỗ khác — **giá trị `a` và `b` không hề thay đổi**.

Đối chiếu với hoán đổi giá trị:

```cpp
void hoanDoiGiaTri(int *p1, int *p2) {
    int tam = *p1;
    *p1 = *p2;
    *p2 = tam;
}
// Sau khi goi: a = 20, b = 10; con p va q van tro cho cu
```

💡 Cách C++ đơn giản hơn: `swap(p, q);` — `std::swap` hoạt động với mọi kiểu, kể cả con trỏ.

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x = 42;
    int *p = &x;
    int **q = &p;
    int ***r = &q;

    cout << "x     = " << x     << endl;   // 42
    cout << "*p    = " << *p    << endl;   // 42
    cout << "**q   = " << **q   << endl;   // 42
    cout << "***r  = " << ***r  << endl;   // 42

    ***r = 100;                             // sua x qua 3 cap
    cout << "x sau khi sua = " << x << endl;   // 100
    return 0;
}
```

**Sơ đồ bộ nhớ:**

```
Dia chi      Bien    Gia tri              Y nghia
0x1000        x       42                  gia tri thuc
0x2000        p       0x1000    --------> x
0x3000        q       0x2000    --------> p --------> x
0x4000        r       0x3000    --------> q --------> p --------> x
```

**Bảng giải tham chiếu:**

| Biểu thức | Giá trị | Kiểu |
|---|---|---|
| `r` | 0x3000 | `int***` |
| `*r` | 0x2000 | `int**` (= `q`) |
| `**r` | 0x1000 | `int*` (= `p`) |
| `***r` | 42 | `int` (= `x`) |

⚠️ Trong thực tế **hầu như không bao giờ** cần con trỏ cấp 3. Nếu code của bạn có `int***`, gần như chắc chắn thiết kế đang sai — hãy dùng `struct`, `vector`, hoặc `class` thay thế.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int** capPhatMaTran(int n, int m) {
    int **a = new int*[n];
    for (int i = 0; i < n; i++) a[i] = new int[m]();    // () de khoi tao 0
    return a;
}

void giaiPhongMaTran(int ***a, int n) {
    if (a == nullptr || *a == nullptr) return;

    for (int i = 0; i < n; i++) {
        delete[] (*a)[i];        // giai phong tung hang
        (*a)[i] = nullptr;
    }
    delete[] *a;                 // giai phong mang con tro
    *a = nullptr;                // dat con tro goc ve nullptr
}

int main() {
    int n = 3, m = 4;
    int **mt = capPhatMaTran(n, m);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mt[i][j] = i * m + j;

    cout << "Ma tran:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << mt[i][j] << "\t";
        cout << endl;
    }

    giaiPhongMaTran(&mt, n);

    cout << "Sau giai phong: mt = "
         << (mt == nullptr ? "nullptr (an toan)" : "con gia tri (nguy hiem)") << endl;
    return 0;
}
```

💡 **Vì sao cần con trỏ cấp 3 (`int ***a`) ở đây:** để hàm có thể đặt con trỏ `mt` ở `main` về `nullptr`. Nếu chỉ nhận `int **a`, hàm chỉ sửa được bản sao.

✅ **Cách C++ hiện đại giải quyết triệt để vấn đề này:**

```cpp
vector<vector<int>> mt(n, vector<int>(m, 0));
// Khong can cap phat, khong can giai phong, khong the ro ri bo nho
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    // ① int **p : con tro toi con tro
    int x = 1;
    int *tam = &x;
    int **p = &tam;
    cout << "**p = " << **p << endl;

    // ② int *q[3] : MANG 3 con tro
    int a = 10, b = 20, c = 30;
    int *q[3] = {&a, &b, &c};
    cout << "*q[1] = " << *q[1] << endl;      // 20
    cout << "sizeof(q) = " << sizeof(q) << " byte" << endl;   // 3 * 8 = 24

    // ③ int (*r)[3] : CON TRO toi mang 3 phan tu
    int m[2][3] = {{1,2,3}, {4,5,6}};
    int (*r)[3] = m;                          // r tro toi hang dau
    cout << "r[1][2] = " << r[1][2] << endl;  // 6
    cout << "sizeof(*r) = " << sizeof(*r) << " byte" << endl;  // 3 * 4 = 12

    return 0;
}
```

**Bảng phân biệt:**

| Khai báo | Là gì | Kích thước | Dùng cho |
|---|---|---|---|
| `int **p` | Con trỏ tới con trỏ | 8 byte | Mảng 2D động, `argv` |
| `int *q[3]` | **Mảng** 3 con trỏ | 24 byte (3×8) | Mảng chuỗi, mảng con trỏ hàm |
| `int (*r)[3]` | Con trỏ tới **mảng** 3 phần tử | 8 byte | Truyền mảng 2D tĩnh vào hàm |

💡 **Mẹo đọc — bắt đầu từ tên biến, đọc theo thứ tự ưu tiên toán tử:**

```
int *q[3]
    ^ q la...  [3] mang 3 phan tu...  * cua con tro...  int toi int
    -> "q la mang 3 con tro toi int"

int (*r)[3]
    ^ (*r) -> r la con tro...  [3] toi mang 3 phan tu...  int kieu int
    -> "r la con tro toi mang 3 int"
```

`[]` có độ ưu tiên **cao hơn** `*`, nên phải dùng ngoặc `(*r)` để ép `r` là con trỏ trước.

💡 Dùng `using` để làm rõ:

```cpp
using MangConTro = int*[3];      // rat kho doc neu viet truc tiep
using ConTroMang = int(*)[3];
```

### Bài 14.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

const int MAX = 100;

void themChuoi(char **ds, int &n, const char *s) {
    if (n >= MAX) { cout << "Danh sach day!" << endl; return; }
    ds[n] = new char[strlen(s) + 1];
    strcpy(ds[n], s);
    n++;
}

void xoaChuoi(char **ds, int &n, int k) {
    if (k < 0 || k >= n) { cout << "Vi tri khong hop le!" << endl; return; }
    delete[] ds[k];                          // giai phong chuoi bi xoa
    for (int i = k; i < n - 1; i++) ds[i] = ds[i + 1];
    n--;
}

void inDanhSach(char **ds, int n) {
    if (n == 0) { cout << "Danh sach rong" << endl; return; }
    for (int i = 0; i < n; i++) cout << "[" << i << "] " << ds[i] << endl;
}

void giaiPhongTatCa(char **ds, int &n) {
    for (int i = 0; i < n; i++) { delete[] ds[i]; ds[i] = nullptr; }
    n = 0;
}

int main() {
    char *ds[MAX];
    int n = 0;

    themChuoi(ds, n, "C++");
    themChuoi(ds, n, "Python");
    themChuoi(ds, n, "Java");
    themChuoi(ds, n, "Go");

    cout << "--- Danh sach ban dau ---" << endl;
    inDanhSach(ds, n);

    xoaChuoi(ds, n, 1);
    cout << "\n--- Sau khi xoa vi tri 1 ---" << endl;
    inDanhSach(ds, n);

    giaiPhongTatCa(ds, n);
    cout << "\nDa giai phong toan bo bo nho." << endl;
    return 0;
}
```

Output:

```
--- Danh sach ban dau ---
[0] C++
[1] Python
[2] Java
[3] Go

--- Sau khi xoa vi tri 1 ---
[0] C++
[1] Java
[2] Go

Da giai phong toan bo bo nho.
```

⚠️ Mỗi `new[]` phải có đúng một `delete[]` tương ứng. Chương trình trên rất dễ **rò rỉ bộ nhớ** nếu quên một chỗ.

✅ **Cách C++ hiện đại — chỉ 10 dòng, không thể rò rỉ:**

```cpp
#include <vector>
#include <string>

vector<string> ds = {"C++", "Python", "Java", "Go"};
ds.erase(ds.begin() + 1);
for (size_t i = 0; i < ds.size(); i++)
    cout << "[" << i << "] " << ds[i] << endl;
// Khong can giai phong gi ca
```

### Bài 15.

**Con trỏ cấp 2 trong C++ hiện đại: gần như KHÔNG cần thiết.**

| Trường hợp dùng `**` | Giải pháp C++ hiện đại |
|---|---|
| Hàm cần thay đổi một con trỏ | **Tham chiếu tới con trỏ** `int *&p`, hoặc **trả về** con trỏ |
| Mảng 2 chiều động | **`vector<vector<int>>`** |
| Mảng chuỗi (`char**`) | **`vector<string>`** |
| Cấp phát bộ nhớ trong hàm | **Trả về `vector`** hoặc `unique_ptr` |
| Tham số dòng lệnh `char **argv` | ⚠️ Vẫn cần (do chuẩn C), nhưng nên chuyển ngay sang `vector<string>` |
| Cấu trúc dữ liệu liên kết | **Smart pointer** (`unique_ptr`, `shared_ptr`) |

**Đối chiếu cụ thể:**

```cpp
// ========== CÁCH CŨ (C) ==========
void capPhat(int **p, int n) {
    *p = (int*)malloc(n * sizeof(int));
}
int *a;
capPhat(&a, 10);
free(a);

// ========== C++ VỚI THAM CHIẾU ==========
void capPhat(int *&p, int n) {
    p = new int[n];
}
int *a;
capPhat(a, 10);
delete[] a;

// ========== C++ HIỆN ĐẠI ==========
vector<int> taoMang(int n) {
    return vector<int>(n);
}
auto a = taoMang(10);
// tu dong giai phong
```

```cpp
// ========== Mảng 2D: cũ ==========
int **m = new int*[n];
for (int i = 0; i < n; i++) m[i] = new int[c];
// ... su dung ...
for (int i = 0; i < n; i++) delete[] m[i];
delete[] m;

// ========== Mảng 2D: hiện đại ==========
vector<vector<int>> m(n, vector<int>(c));
// het. khong can gi them.
```

**✅ Vẫn NÊN học con trỏ cấp 2 vì:**

1. **Đọc hiểu code cũ** — rất nhiều thư viện C và code legacy dùng nó
2. **Hiểu bản chất `argv`** trong hàm `main`
3. **Hiểu cơ chế bộ nhớ** — biết `vector<vector<int>>` thực sự làm gì bên dưới
4. **Phỏng vấn và bài thi** — vẫn là chủ đề được hỏi
5. **Lập trình nhúng / hệ thống** — nơi không dùng được STL

**❌ Nhưng KHÔNG nên dùng trong code mới**, vì:
- Dễ rò rỉ bộ nhớ (quên `delete`)
- Dễ tạo dangling pointer
- Khó đọc, khó bảo trì
- STL đã làm tốt hơn và an toàn hơn

💡 **Nguyên tắc C++ hiện đại:** *"Không bao giờ dùng `new`/`delete` thủ công trong code ứng dụng."* Dùng container (`vector`, `string`, `map`) hoặc smart pointer (`unique_ptr`, `shared_ptr`).
