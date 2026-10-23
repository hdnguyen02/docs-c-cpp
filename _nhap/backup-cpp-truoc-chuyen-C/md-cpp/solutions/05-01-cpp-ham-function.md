# Lời giải — [C++]. Hàm

[← Quay lại bài học](../05-01-cpp-ham-function.md)

> **Cấu trúc hàm:** `kieu_tra_ve ten_ham(danh_sach_tham_so) { than_ham; return gia_tri; }`

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int tong(int a, int b) {
    return a + b;
}

int main() {
    int x, y;
    cout << "Nhap 2 so: ";
    cin >> x >> y;

    cout << x << " + " << y << " = " << tong(x, y) << endl;
    return 0;
}
```

**Thuật ngữ:**
- `a`, `b` trong định nghĩa hàm gọi là **tham số hình thức** (parameter)
- `x`, `y` khi gọi hàm gọi là **tham số thực** (argument)

### Bài 2.

```cpp
#include <iostream>
using namespace std;

void chao() {
    cout << "Xin chao C++" << endl;
}

int main() {
    chao();
    chao();
    chao();
    return 0;
}
```

**`void`** nghĩa là hàm **không trả về gì**. Hàm `void` không cần `return`, hoặc dùng `return;` trống để thoát sớm.

### Bài 3.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

const double PI = 3.14159265358979;

double dienTichChuNhat(double dai, double rong) {
    return dai * rong;
}

double dienTichTron(double r) {
    return PI * r * r;
}

double dienTichTamGiac(double day, double cao) {
    return 0.5 * day * cao;
}

int main() {
    cout << fixed << setprecision(2);
    cout << "Hinh chu nhat 5 x 3 : " << dienTichChuNhat(5, 3) << endl;
    cout << "Hinh tron r = 2     : " << dienTichTron(2)       << endl;
    cout << "Tam giac 6 x 4      : " << dienTichTamGiac(6, 4) << endl;
    return 0;
}
```

### Bài 4.

```cpp
#include <iostream>
using namespace std;

bool laSoChan(int n) {
    return n % 2 == 0;
}

int main() {
    int n;
    cin >> n;
    cout << n << (laSoChan(n) ? " la so CHAN" : " la so LE") << endl;
    return 0;
}
```

💡 Viết `return n % 2 == 0;` gọn hơn nhiều so với:

```cpp
if (n % 2 == 0) return true;
else return false;                  // DAI DONG khong can thiet
```

Biểu thức `n % 2 == 0` **đã** là một giá trị `bool` rồi.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int max3(int a, int b, int c) {
    int kq = a;
    if (b > kq) kq = b;
    if (c > kq) kq = c;
    return kq;
}

int main() {
    int a, b, c;
    cin >> a >> b >> c;
    cout << "Lon nhat = " << max3(a, b, c) << endl;
    return 0;
}
```

### Bài 6.

```cpp
#include <iostream>
using namespace std;

long long giaiThua(int n) {
    if (n < 0) return -1;              // gia tri bao loi

    long long kq = 1;
    for (int i = 2; i <= n; i++) {
        kq *= i;
    }
    return kq;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    long long kq = giaiThua(n);
    if (kq == -1) cout << "n phai khong am!" << endl;
    else          cout << n << "! = " << kq << endl;
    return 0;
}
```

⚠️ `long long` chỉ tính đúng tới `20!`. Từ `21!` trở đi sẽ tràn số.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

bool laNguyenTo(int n) {
    if (n < 2) return false;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) return false;      // return thay cho break + co
    }
    return true;
}

int main() {
    cout << "Cac so nguyen to tu 1 den 100:" << endl;
    int dem = 0;
    for (int i = 1; i <= 100; i++) {
        if (laNguyenTo(i)) {
            cout << i << " ";
            dem++;
        }
    }
    cout << "\nTong cong: " << dem << " so" << endl;
    return 0;
}
```

Output:

```
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Tong cong: 25 so
```

💡 **Lợi ích của việc tách hàm:** so sánh với việc viết vòng lặp kiểm tra nguyên tố **lồng bên trong** vòng lặp duyệt 1–100 — code sẽ khó đọc hơn nhiều, và cần biến cờ + `break`. Với hàm riêng, `return false` thoát luôn, code sạch.

### Bài 8.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int ucln(int a, int b) {
    a = abs(a);
    b = abs(b);
    while (b != 0) {
        int tam = a % b;
        a = b;
        b = tam;
    }
    return a;
}

long long bcnn(int a, int b) {
    if (a == 0 || b == 0) return 0;
    return (long long)abs(a) / ucln(a, b) * abs(b);   // CHIA truoc de tranh tran
}

int main() {
    int a, b;
    cout << "Nhap 2 so: ";
    cin >> a >> b;

    cout << "UCLN = " << ucln(a, b) << endl;
    cout << "BCNN = " << bcnn(a, b) << endl;
    return 0;
}
```

💡 **`bcnn` gọi lại `ucln`** — đây là điểm mạnh lớn nhất của hàm: xây dựng chức năng phức tạp từ những chức năng đơn giản đã có, không phải viết lại.

### Bài 9.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int demChuSo(int n) {
    if (n == 0) return 1;
    int tam = abs(n), dem = 0;
    while (tam > 0) { dem++; tam /= 10; }
    return dem;
}

int tongChuSo(int n) {
    int tam = abs(n), tong = 0;
    while (tam > 0) { tong += tam % 10; tam /= 10; }
    return tong;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << "So chu so   : " << demChuSo(n)  << endl;
    cout << "Tong chu so : " << tongChuSo(n) << endl;
    return 0;
}
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

long long daoNguoc(int n) {
    bool am = (n < 0);
    long long tam = am ? -(long long)n : n;
    long long dao = 0;

    while (tam > 0) {
        dao = dao * 10 + tam % 10;
        tam /= 10;
    }
    return am ? -dao : dao;
}

bool laDoiXung(int n) {
    if (n < 0) return false;
    return daoNguoc(n) == n;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << "So dao nguoc : " << daoNguoc(n) << endl;
    cout << n << (laDoiXung(n) ? " LA " : " KHONG ") << "so doi xung" << endl;
    return 0;
}
```

### Bài 11.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// Hinh vuong: 1 tham so
double dienTich(double canh) {
    return canh * canh;
}

// Hinh chu nhat: 2 tham so
double dienTich(double dai, double rong) {
    return dai * rong;
}

// Tam giac theo cong thuc Heron: 3 tham so
double dienTich(double a, double b, double c) {
    double p = (a + b + c) / 2;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}

int main() {
    cout << fixed << setprecision(4);
    cout << "Hinh vuong canh 5     : " << dienTich(5.0)          << endl;
    cout << "Chu nhat 5 x 3        : " << dienTich(5.0, 3.0)     << endl;
    cout << "Tam giac 3, 4, 5      : " << dienTich(3.0, 4.0, 5.0) << endl;
    return 0;
}
```

**Nạp chồng hàm (function overloading)** — nhiều hàm **cùng tên** nhưng **khác danh sách tham số**. Compiler tự chọn hàm phù hợp dựa vào số lượng và kiểu tham số khi bạn gọi.

**Điều kiện để nạp chồng hợp lệ — phải khác nhau về:**
- **Số lượng** tham số, hoặc
- **Kiểu** tham số

⚠️ **Chỉ khác kiểu trả về thì KHÔNG được:**

```cpp
int  f(int x);
double f(int x);     // LOI: cannot be overloaded
```

Vì khi gọi `f(5)`, compiler không có cách nào biết bạn muốn gọi cái nào.

⚠️ Coi chừng nhập nhằng:

```cpp
dienTich(5);          // 5 la int -> co the chuyen sang double, OK
dienTich(5, 3);       // OK
```

### Bài 12.

```cpp
#include <iostream>
using namespace std;

void inTamGiac(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

int main() {
    int n;
    cout << "Nhap so dong: ";
    cin >> n;
    inTamGiac(n);
    return 0;
}
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main(){
    cout << binhPhuong(5);         // <- LOI: ham chua duoc khai bao
    return 0;
}

int binhPhuong(int x){ return x * x; }
```

**Lỗi:** compiler đọc file **từ trên xuống dưới**. Khi tới dòng `cout << binhPhuong(5);`, nó chưa hề biết `binhPhuong` là gì.

Thông báo lỗi:

```
error: 'binhPhuong' was not declared in this scope
```

**Sửa cách 1 — đưa định nghĩa hàm lên trước `main`:**

```cpp
#include <iostream>
using namespace std;

int binhPhuong(int x) { return x * x; }

int main() {
    cout << binhPhuong(5);
    return 0;
}
```

**Sửa cách 2 — khai báo nguyên mẫu (prototype) trước `main`:**

```cpp
#include <iostream>
using namespace std;

int binhPhuong(int x);        // NGUYEN MAU - bao truoc cho compiler

int main() {
    cout << binhPhuong(5);
    return 0;
}

int binhPhuong(int x) { return x * x; }   // dinh nghia o duoi
```

Cách 2 tốt hơn khi có nhiều hàm — bạn thấy được danh sách hàm ngay ở đầu file. Chi tiết ở bài [05-02](../05-02-cpp-khai-bao-nguyen-mau-ham.md).

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

double trungBinh(int a[], int n) {
    if (n <= 0) return 0;

    long long tong = 0;
    for (int i = 0; i < n; i++) {
        tong += a[i];
    }
    return (double)tong / n;
}

int main() {
    int a[5] = {10, 20, 30, 40, 55};

    cout << "Mang: ";
    for (int i = 0; i < 5; i++) cout << a[i] << " ";
    cout << endl;

    cout << fixed << setprecision(2);
    cout << "Trung binh = " << trungBinh(a, 5) << endl;
    return 0;
}
```

Output: `Trung binh = 31.00`

⚠️ **Khi truyền mảng vào hàm, phải truyền kèm kích thước `n`.** Trong hàm, `a` thực chất chỉ là một **con trỏ** tới phần tử đầu — `sizeof(a)` bên trong hàm sẽ cho kích thước con trỏ (8 byte), không phải kích thước mảng.

⚠️ Mảng luôn được truyền theo kiểu **tham chiếu** (thực chất là con trỏ), nên sửa `a[i]` trong hàm **sẽ sửa mảng gốc**. Muốn bảo vệ, thêm `const`:

```cpp
double trungBinh(const int a[], int n) { ... }
```

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

const int MAX_SV = 100;

// ---------- Nhap diem cho n sinh vien ----------
void nhapDiem(string ten[], double toan[], double ly[], double hoa[], int n) {
    for (int i = 0; i < n; i++) {
        cout << "--- Sinh vien " << i + 1 << " ---" << endl;
        cout << "Ho ten (viet lien): ";
        cin >> ten[i];
        cout << "Diem Toan, Ly, Hoa: ";
        cin >> toan[i] >> ly[i] >> hoa[i];
    }
}

// ---------- Tinh diem trung binh ----------
double tinhTrungBinh(double toan, double ly, double hoa) {
    return (toan + ly + hoa) / 3.0;
}

// ---------- Xep loai theo diem trung binh ----------
string xepLoai(double dtb) {
    if (dtb >= 8.5) return "Gioi";
    if (dtb >= 7.0) return "Kha";
    if (dtb >= 5.0) return "Trung binh";
    return "Yeu";
}

// ---------- In bang ket qua ----------
void inKetQua(string ten[], double toan[], double ly[], double hoa[], int n) {
    cout << "\n+-----+----------------+-------+-------+-------+-------+------------+" << endl;
    cout << "| STT | HO TEN         |  TOAN |    LY |   HOA |   DTB | XEP LOAI   |" << endl;
    cout << "+-----+----------------+-------+-------+-------+-------+------------+" << endl;

    cout << fixed << setprecision(2);
    for (int i = 0; i < n; i++) {
        double dtb = tinhTrungBinh(toan[i], ly[i], hoa[i]);
        cout << "| " << left  << setw(3) << i + 1
             << " | " << setw(14) << ten[i]
             << " | " << right << setw(5) << toan[i]
             << " | " << setw(5) << ly[i]
             << " | " << setw(5) << hoa[i]
             << " | " << setw(5) << dtb
             << " | " << left << setw(10) << xepLoai(dtb) << " |" << endl;
    }
    cout << "+-----+----------------+-------+-------+-------+-------+------------+" << endl;
}

// ---------- Chuong trinh chinh ----------
int main() {
    int n;
    cout << "Nhap so sinh vien: ";
    cin >> n;

    if (n <= 0 || n > MAX_SV) {
        cout << "So sinh vien khong hop le!" << endl;
        return 1;
    }

    string ten[MAX_SV];
    double toan[MAX_SV], ly[MAX_SV], hoa[MAX_SV];

    nhapDiem(ten, toan, ly, hoa, n);
    inKetQua(ten, toan, ly, hoa, n);

    return 0;
}
```

Ví dụ output:

```
+-----+----------------+-------+-------+-------+-------+------------+
| STT | HO TEN         |  TOAN |    LY |   HOA |   DTB | XEP LOAI   |
+-----+----------------+-------+-------+-------+-------+------------+
| 1   | AnNguyen       |  9.00 |  8.50 |  8.00 |  8.50 | Gioi       |
| 2   | BinhTran       |  6.00 |  7.00 |  6.50 |  6.50 | Trung binh |
+-----+----------------+-------+-------+-------+-------+------------+
```

**Nguyên tắc thiết kế hàm tốt — mỗi hàm làm ĐÚNG MỘT việc:**

| Hàm | Việc duy nhất nó làm |
|---|---|
| `nhapDiem` | Đọc dữ liệu |
| `tinhTrungBinh` | Tính toán |
| `xepLoai` | Phân loại |
| `inKetQua` | Hiển thị |
| `main` | Điều phối |

**Lợi ích:**
1. **Dễ kiểm thử:** có thể test riêng `xepLoai(8.7)` mà không cần nhập liệu
2. **Dễ sửa:** đổi tiêu chí xếp loại chỉ cần sửa 1 hàm
3. **Tái sử dụng:** `tinhTrungBinh` dùng được ở mọi chỗ khác
4. **Dễ đọc:** đọc `main` là hiểu ngay chương trình làm gì

⚠️ Với nhiều trường dữ liệu như thế này, cách tốt hơn nữa là dùng `struct`:

```cpp
struct SinhVien {
    string ten;
    double toan, ly, hoa;
};
SinhVien ds[MAX_SV];      // chi 1 mang thay vi 4
```
