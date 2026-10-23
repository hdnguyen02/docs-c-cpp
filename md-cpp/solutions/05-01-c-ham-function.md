# Lời giải — [C]. Hàm - Function

[← Quay lại bài học](../05-01-c-ham-function.md)

> **Cấu trúc hàm:** `kieu_tra_ve ten_ham(danh_sach_tham_so) { than_ham; return gia_tri; }`

---

### Bài 1.

```c
#include <stdio.h>

int tong(int a, int b) {
    return a + b;
}

int main(void) {
    int x, y;
    printf("Nhap 2 so: ");
    scanf("%d %d", &x, &y);

    printf("%d + %d = %d\n", x, y, tong(x, y));
    return 0;
}
```

**Thuật ngữ:**
- `a`, `b` trong định nghĩa hàm gọi là **tham số hình thức** (parameter)
- `x`, `y` khi gọi hàm gọi là **tham số thực** (argument)

### Bài 2.

```c
#include <stdio.h>

void chao(void) {
    printf("Xin chao C\n");
}

int main(void) {
    chao();
    chao();
    chao();
    return 0;
}
```

**`void`** ở kiểu trả về nghĩa là hàm **không trả về gì**. Hàm `void` không cần `return`, hoặc dùng `return;` trống để thoát sớm.

💡 `void` trong cặp ngoặc `chao(void)` nghĩa là hàm **không nhận tham số nào**. Trong C (trước C23), viết `void chao()` lại có nghĩa là "số tham số chưa xác định" — compiler sẽ không bắt lỗi nếu bạn lỡ gọi `chao(5)`. Vì vậy trong C nên viết rõ `(void)`.

### Bài 3.

```c
#include <stdio.h>

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

int main(void) {
    printf("Hinh chu nhat 5 x 3 : %.2f\n", dienTichChuNhat(5, 3));
    printf("Hinh tron r = 2     : %.2f\n", dienTichTron(2));
    printf("Tam giac 6 x 4      : %.2f\n", dienTichTamGiac(6, 4));
    return 0;
}
```

💡 Gọi `dienTichChuNhat(5, 3)` với đối số `int` vẫn đúng: vì hàm đã được khai báo trước với tham số `double`, compiler tự chuyển `5` thành `5.0`.

### Bài 4.

```c
#include <stdio.h>
#include <stdbool.h>

bool laSoChan(int n) {
    return n % 2 == 0;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d %s\n", n, laSoChan(n) ? "la so CHAN" : "la so LE");
    return 0;
}
```

💡 Viết `return n % 2 == 0;` gọn hơn nhiều so với:

```c
if (n % 2 == 0) return true;
else return false;                  // DAI DONG khong can thiet
```

Biểu thức `n % 2 == 0` **đã** là một giá trị đúng/sai rồi (trong C nó có giá trị `1` hoặc `0`).

⚠️ Kiểu `bool` và các từ `true`, `false` chỉ dùng được khi có `#include <stdbool.h>` (trước C23).

### Bài 5.

```c
#include <stdio.h>

int max3(int a, int b, int c) {
    int kq = a;
    if (b > kq) kq = b;
    if (c > kq) kq = c;
    return kq;
}

int main(void) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    printf("Lon nhat = %d\n", max3(a, b, c));
    return 0;
}
```

### Bài 6.

```c
#include <stdio.h>

long long giaiThua(int n) {
    if (n < 0) return -1;              // gia tri bao loi

    long long kq = 1;
    for (int i = 2; i <= n; i++) {
        kq *= i;
    }
    return kq;
}

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    long long kq = giaiThua(n);
    if (kq == -1) printf("n phai khong am!\n");
    else          printf("%d! = %lld\n", n, kq);
    return 0;
}
```

⚠️ `long long` chỉ tính đúng tới `20!`. Từ `21!` trở đi sẽ tràn số.

⚠️ In `long long` phải dùng `%lld`; dùng `%d` sẽ in sai.

### Bài 7.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(int n) {
    if (n < 2) return false;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) return false;      // return thay cho break + co
    }
    return true;
}

int main(void) {
    printf("Cac so nguyen to tu 1 den 100:\n");
    int dem = 0;
    for (int i = 1; i <= 100; i++) {
        if (laNguyenTo(i)) {
            printf("%d ", i);
            dem++;
        }
    }
    printf("\nTong cong: %d so\n", dem);
    return 0;
}
```

Output:

```
Cac so nguyen to tu 1 den 100:
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 
Tong cong: 25 so
```

💡 **Lợi ích của việc tách hàm:** so sánh với việc viết vòng lặp kiểm tra nguyên tố **lồng bên trong** vòng lặp duyệt 1–100 — code sẽ khó đọc hơn nhiều, và cần biến cờ + `break`. Với hàm riêng, `return false` thoát luôn, code sạch.

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

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

int main(void) {
    int a, b;
    printf("Nhap 2 so: ");
    scanf("%d %d", &a, &b);

    printf("UCLN = %d\n", ucln(a, b));
    printf("BCNN = %lld\n", bcnn(a, b));
    return 0;
}
```

💡 **`bcnn` gọi lại `ucln`** — đây là điểm mạnh lớn nhất của hàm: xây dựng chức năng phức tạp từ những chức năng đơn giản đã có, không phải viết lại.

💡 Hàm `abs` cho số nguyên nằm trong `<stdlib.h>` (không phải `<math.h>`). Đề bài gợi ý kiểu `int` cho `bcnn`, ở đây dùng `long long` để tránh tràn khi hai số lớn.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>

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

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    printf("So chu so   : %d\n", demChuSo(n));
    printf("Tong chu so : %d\n", tongChuSo(n));
    return 0;
}
```

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

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

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    printf("So dao nguoc : %lld\n", daoNguoc(n));
    printf("%d %s so doi xung\n", n, laDoiXung(n) ? "LA" : "KHONG");
    return 0;
}
```

💡 Hàm trả về `long long` thay vì `int` như đề gợi ý: số đảo của một `int` lớn (vd `1999999999` → `9999999991`) có thể vượt phạm vi `int`.

### Bài 11.

```c
#include <stdio.h>
#include <math.h>

// Hinh vuong: 1 tham so
double dienTichVuong(double canh) {
    return canh * canh;
}

// Hinh chu nhat: 2 tham so
double dienTichChuNhat(double dai, double rong) {
    return dai * rong;
}

// Tam giac theo cong thuc Heron: 3 tham so
double dienTichTamGiac(double a, double b, double c) {
    double p = (a + b + c) / 2;
    return sqrt(p * (p - a) * (p - b) * (p - c));
}

int main(void) {
    printf("Hinh vuong canh 5     : %.4f\n", dienTichVuong(5.0));
    printf("Chu nhat 5 x 3        : %.4f\n", dienTichChuNhat(5.0, 3.0));
    printf("Tam giac 3, 4, 5      : %.4f\n", dienTichTamGiac(3.0, 4.0, 5.0));
    return 0;
}
```

Biên dịch (cần `-lm` để liên kết thư viện toán vì dùng `sqrt`):

```bash
gcc -std=c11 -Wall main.c -o main -lm
```

**C KHÔNG có nạp chồng hàm (function overloading).** Trong một chương trình C, mỗi tên hàm chỉ ứng với **đúng một** hàm. Nếu thử đặt cả 3 hàm cùng tên `dienTich`:

```c
double dienTich(double canh);
double dienTich(double dai, double rong);     // LOI
```

gcc báo:

```
error: conflicting types for 'dienTich'
```

**Cách làm trong C:** đặt tên khác nhau, thường gắn thêm hậu tố mô tả — đúng như thư viện chuẩn C làm: `abs` (int), `labs` (long), `llabs` (long long), `fabs` (double); hay `sqrt` (double), `sqrtf` (float).

💡 Tên riêng cho từng hàm cũng có cái lợi: đọc lời gọi `dienTichTamGiac(3, 4, 5)` là biết ngay đang tính gì, không phải đếm số tham số.

### Bài 12.

```c
#include <stdio.h>

void inTamGiac(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("*");
        }
        printf("\n");
    }
}

int main(void) {
    int n;
    printf("Nhap so dong: ");
    scanf("%d", &n);
    inTamGiac(n);
    return 0;
}
```

### Bài 13.

```c
#include <stdio.h>

int main(void){
    printf("%d\n", binhPhuong(5));   // <- LOI: ham chua duoc khai bao
    return 0;
}

int binhPhuong(int x){ return x * x; }
```

**Lỗi:** compiler đọc file **từ trên xuống dưới**. Khi tới dòng gọi `binhPhuong(5)`, nó chưa hề biết `binhPhuong` là gì.

Thông báo của gcc:

```
warning: implicit declaration of function 'binhPhuong' [-Wimplicit-function-declaration]
```

⚠️ **Đừng coi thường cảnh báo này.** C đời cũ (C89) cho phép gọi hàm chưa khai báo và tự "đoán" hàm trả về `int`. Từ C99 trở đi, việc này **không còn hợp lệ**; gcc 11 vẫn chỉ cảnh báo để tương thích code cũ, gcc 14 trở đi báo **lỗi**. Nếu hàm thật trả về kiểu khác `int` (vd `double`), chương trình sẽ còn lỗi `conflicting types` hoặc in ra kết quả sai. Luôn biên dịch với `-Wall` và sửa hết cảnh báo loại này.

**Sửa cách 1 — đưa định nghĩa hàm lên trước `main`:**

```c
#include <stdio.h>

int binhPhuong(int x) { return x * x; }

int main(void) {
    printf("%d\n", binhPhuong(5));
    return 0;
}
```

**Sửa cách 2 — khai báo nguyên mẫu (prototype) trước `main`:**

```c
#include <stdio.h>

int binhPhuong(int x);        // NGUYEN MAU - bao truoc cho compiler

int main(void) {
    printf("%d\n", binhPhuong(5));
    return 0;
}

int binhPhuong(int x) { return x * x; }   // dinh nghia o duoi
```

Cách 2 tốt hơn khi có nhiều hàm — bạn thấy được danh sách hàm ngay ở đầu file. Chi tiết ở bài [05-02](../05-02-c-khai-bao-nguyen-mau-ham.md).

### Bài 14.

```c
#include <stdio.h>

double trungBinh(int a[], int n) {
    if (n <= 0) return 0;

    long long tong = 0;
    for (int i = 0; i < n; i++) {
        tong += a[i];
    }
    return (double)tong / n;
}

int main(void) {
    int a[5] = {10, 20, 30, 40, 55};

    printf("Mang: ");
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\n");

    printf("Trung binh = %.2f\n", trungBinh(a, 5));
    return 0;
}
```

Output: `Trung binh = 31.00`

⚠️ **Khi truyền mảng vào hàm, phải truyền kèm kích thước `n`.** Trong hàm, `a` thực chất chỉ là một **con trỏ** tới phần tử đầu — `sizeof(a)` bên trong hàm sẽ cho kích thước con trỏ (8 byte trên máy 64-bit), không phải kích thước mảng.

⚠️ Vì hàm nhận **địa chỉ** của mảng (không phải bản sao), sửa `a[i]` trong hàm **sẽ sửa mảng gốc**. Muốn bảo vệ, thêm `const`:

```c
double trungBinh(const int a[], int n) { ... }
```

### Bài 15.

```c
#include <stdio.h>

#define MAX_SV  100
#define MAX_TEN 50

// ---------- Nhap diem cho n sinh vien ----------
void nhapDiem(char ten[][MAX_TEN], double toan[], double ly[], double hoa[], int n) {
    for (int i = 0; i < n; i++) {
        printf("--- Sinh vien %d ---\n", i + 1);
        printf("Ho ten (viet lien): ");
        scanf("%49s", ten[i]);
        printf("Diem Toan, Ly, Hoa: ");
        scanf("%lf %lf %lf", &toan[i], &ly[i], &hoa[i]);
    }
}

// ---------- Tinh diem trung binh ----------
double tinhTrungBinh(double toan, double ly, double hoa) {
    return (toan + ly + hoa) / 3.0;
}

// ---------- Xep loai theo diem trung binh ----------
const char *xepLoai(double dtb) {
    if (dtb >= 8.5) return "Gioi";
    if (dtb >= 7.0) return "Kha";
    if (dtb >= 5.0) return "Trung binh";
    return "Yeu";
}

// ---------- In bang ket qua ----------
void inKetQua(char ten[][MAX_TEN], double toan[], double ly[], double hoa[], int n) {
    printf("\n+-----+----------------+-------+-------+-------+-------+------------+\n");
    printf("| STT | HO TEN         |  TOAN |    LY |   HOA |   DTB | XEP LOAI   |\n");
    printf("+-----+----------------+-------+-------+-------+-------+------------+\n");

    for (int i = 0; i < n; i++) {
        double dtb = tinhTrungBinh(toan[i], ly[i], hoa[i]);
        printf("| %-3d | %-14s | %5.2f | %5.2f | %5.2f | %5.2f | %-10s |\n",
               i + 1, ten[i], toan[i], ly[i], hoa[i], dtb, xepLoai(dtb));
    }
    printf("+-----+----------------+-------+-------+-------+-------+------------+\n");
}

// ---------- Chuong trinh chinh ----------
int main(void) {
    int n;
    printf("Nhap so sinh vien: ");
    scanf("%d", &n);

    if (n <= 0 || n > MAX_SV) {
        printf("So sinh vien khong hop le!\n");
        return 1;
    }

    char ten[MAX_SV][MAX_TEN];
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

💡 **Một vài điểm riêng của C trong bài này:**
- Tên sinh viên là **mảng 2 chiều ký tự** `char ten[MAX_SV][MAX_TEN]` — mỗi dòng là một chuỗi. Khi truyền vào hàm phải ghi rõ số cột: `char ten[][MAX_TEN]`.
- `scanf("%49s", ten[i])` giới hạn tối đa 49 ký tự (chừa 1 chỗ cho `'\0'`) để không tràn mảng; `ten[i]` đã là địa chỉ nên **không** có dấu `&`.
- Đọc `double` bằng `scanf` phải dùng `%lf`; in bằng `printf` dùng `%f` / `%.2f`.
- `xepLoai` trả về `const char *` — con trỏ tới chuỗi hằng như `"Gioi"`. Chuỗi hằng tồn tại suốt chương trình nên trả về như vậy là an toàn.
- Căn cột bằng độ rộng trong đặc tả: `%-14s` (căn trái 14 ô), `%5.2f` (căn phải 5 ô, 2 chữ số thập phân).

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

```c
struct SinhVien {
    char ten[MAX_TEN];
    double toan, ly, hoa;
};
struct SinhVien ds[MAX_SV];      // chi 1 mang thay vi 4
```
