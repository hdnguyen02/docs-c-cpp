# Lời giải — [C]. Biến Và Từ Khóa

[← Quay lại bài học](../02-03-c-bien-va-tu-khoa.md)

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    double chieuDai  = 8.5;
    double chieuRong = 4.2;
    double chuVi     = (chieuDai + chieuRong) * 2;
    double dienTich  = chieuDai * chieuRong;
    char   tenHinh   = 'A';

    printf("Hinh chu nhat : %c\n", tenHinh);
    printf("Chieu dai     : %.1f\n", chieuDai);
    printf("Chieu rong    : %.1f\n", chieuRong);
    printf("Chu vi        : %.1f\n", chuVi);
    printf("Dien tich     : %.1f\n", dienTich);
    return 0;
}
```

Output:

```
Hinh chu nhat : A
Chieu dai     : 8.5
Chieu rong    : 4.2
Chu vi        : 25.4
Dien tich     : 35.7
```

*(`%.1f` in số thực với 1 chữ số sau dấu phẩy. Nếu dùng `%f` sẽ in 6 chữ số: `8.500000`.)*

### Bài 2.

| Tên biến | Hợp lệ? | Giải thích |
|---|---|---|
| `banKinh` | ✅ | Đúng chuẩn camelCase |
| `2ban_kinh` | ❌ | Bắt đầu bằng chữ số |
| `ban kinh` | ❌ | Chứa dấu cách |
| `_temp` | ✅ | Được phép bắt đầu bằng `_`, nhưng **không nên** (tên bắt đầu bằng `_` + chữ hoa hoặc `__` được dành riêng cho trình biên dịch và thư viện chuẩn) |
| `int` | ❌ | Trùng từ khoá |
| `Diem` | ✅ | Hợp lệ (kiểu PascalCase) |
| `diem-tb` | ❌ | Dấu `-` là toán tử trừ, không được dùng trong tên |
| `$money` | ❌ | Ký tự đặc biệt `$` (gcc chấp nhận như phần mở rộng riêng, nhưng không thuộc chuẩn C) |
| `so1` | ✅ | Chữ số ở giữa/cuối thì được |
| `struct` | ❌ | Trùng từ khoá |
| `tongSo` | ✅ | Hợp lệ |
| `TONG_SO` | ✅ | Hợp lệ (quy ước thường dùng cho hằng số) |
| `ho&ten` | ❌ | Ký tự `&` không hợp lệ |
| `__x` | ⚠️ | Về cú pháp là hợp lệ, nhưng tên bắt đầu bằng 2 dấu `_` được **dành riêng cho trình biên dịch** — không nên dùng |
| `printf` | ⚠️ | Không phải keyword nên đặt tên biến cục bộ **vẫn biên dịch được**, nhưng biến đó sẽ che mất hàm `printf` khiến bạn không in được ra màn hình trong phạm vi đó. Tuyệt đối tránh. |

**Tóm tắt quy tắc:** tên biến chỉ gồm **chữ cái, chữ số và dấu `_`**; **không bắt đầu bằng chữ số**; **không trùng từ khoá**; **phân biệt hoa thường**.

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    int tech28 = 100;
    int Tech28 = 200;
    int TECH28 = 300;

    printf("tech28 = %d\n", tech28);
    printf("Tech28 = %d\n", Tech28);
    printf("TECH28 = %d\n", TECH28);
    return 0;
}
```

Output:

```
tech28 = 100
Tech28 = 200
TECH28 = 300
```

**Kết luận:** C là ngôn ngữ **case-sensitive** — `tech28`, `Tech28`, `TECH28` là 3 biến hoàn toàn khác nhau. Đây là nguyên nhân rất nhiều lỗi `error: 'X' undeclared` của người mới (viết `Printf` thay vì `printf`, hoặc khai báo `soLuong` rồi dùng `soluong`).

### Bài 4.

**Lỗi:** khai báo 2 biến trùng tên `a` trong cùng một phạm vi (dù khác kiểu dữ liệu vẫn không được). Ngoài ra chương trình còn thiếu `#include <stdio.h>` để dùng được `printf`.

Thông báo lỗi:

```
error: conflicting types for 'a'; have 'float'
note: previous definition of 'a' with type 'int'
```

Sửa lại:

```c
#include <stdio.h>

int main(void) {
    int a = 5;
    float b = 3.14f;      // doi ten bien
    printf("%d %.2f\n", a, b);
    return 0;
}
```

Output: `5 3.14`

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    int a = 10, b = 20, c = 30, d = 40;
    printf("Tong = %d\n", a + b + c + d);
    return 0;
}
```

Output: `Tong = 100`

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int a = 5, b = 9;
    printf("Truoc khi hoan doi: a = %d, b = %d\n", a, b);

    int tam = a;    // cat a vao bien tam
    a = b;          // chep b sang a
    b = tam;        // chep gia tri cu cua a sang b

    printf("Sau khi hoan doi : a = %d, b = %d\n", a, b);
    return 0;
}
```

Output:

```
Truoc khi hoan doi: a = 5, b = 9
Sau khi hoan doi : a = 9, b = 5
```

**Ghi chú:** khác với C++, C **không có sẵn hàm `swap`**. Muốn viết hàm hoán đổi dùng lại được, bạn cần truyền **địa chỉ** của biến vào hàm (con trỏ) — sẽ học ở bài [truyền tham trị và truyền con trỏ](../05-03-c-truyen-tham-tri-va-truyen-con-tro.md):

```c
void swap(int *x, int *y) {
    int tam = *x;
    *x = *y;
    *y = tam;
}
// goi: swap(&a, &b);
```

### Bài 7.

```c
#include <stdio.h>

int main(void) {
    int a = 5, b = 9;
    printf("Truoc: a = %d, b = %d\n", a, b);

    a = a + b;      // a = 14
    b = a - b;      // b = 14 - 9 = 5  (gia tri cu cua a)
    a = a - b;      // a = 14 - 5 = 9  (gia tri cu cua b)

    printf("Sau  : a = %d, b = %d\n", a, b);
    return 0;
}
```

Cách dùng XOR (chỉ áp dụng cho số nguyên):

```c
a = a ^ b;
b = a ^ b;
a = a ^ b;
```

⚠️ **Cảnh báo:** cả 2 cách trên đều có nhược điểm:

- Cách cộng trừ có thể **tràn số** nếu `a + b` vượt phạm vi kiểu dữ liệu.
- Cả hai đều **sai** nếu hoán đổi một biến với chính nó thông qua con trỏ (ví dụ `swap(&x, &x)` → kết quả thành 0).
- Khó đọc hơn nhiều so với dùng biến trung gian.

Trong thực tế hãy dùng biến trung gian. Bài này chỉ mang tính rèn tư duy.

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    const double PI = 3.14159;

    double banKinh;
    printf("Nhap ban kinh: ");
    scanf("%lf", &banKinh);

    double chuVi    = 2 * PI * banKinh;
    double dienTich = PI * banKinh * banKinh;

    printf("Chu vi    = %.4f\n", chuVi);
    printf("Dien tich = %.4f\n", dienTich);
    return 0;
}
```

Ví dụ chạy:

```
Nhap ban kinh: 5
Chu vi    = 31.4159
Dien tich = 78.5397
```

**Chú ý:** `scanf` đọc `double` phải dùng **`%lf`** (không phải `%f`) và phải có dấu **`&`** trước tên biến. Còn `printf` in `double` thì dùng `%f`.

**Ghi chú:** chuẩn C không có hằng số PI dựng sẵn. Nhiều trình biên dịch (gcc trên Linux) có `M_PI` trong `<math.h>` nhưng đó không phải chuẩn C. Cách chuẩn để lấy PI chính xác là dùng `acos(-1.0)` từ `<math.h>`:

```c
#include <math.h>
const double PI = acos(-1.0);   // 3.14159265358979... (can -lm khi bien dich tren Linux)
```

*(Cách này chỉ dùng được với biến `const` cục bộ trong hàm, vì biến toàn cục trong C phải được khởi tạo bằng hằng số.)*

### Bài 9.

```c
#include <stdio.h>

int main(void) {
    const int MAX_HOC_SINH = 50;
    printf("%d\n", MAX_HOC_SINH);

    MAX_HOC_SINH = 60;      // <- DONG NAY GAY LOI

    return 0;
}
```

Thông báo lỗi:

```
error: assignment of read-only variable 'MAX_HOC_SINH'
   |     MAX_HOC_SINH = 60;
   |                  ^
```

**`const` là gì:** từ khoá đánh dấu một biến **chỉ đọc** — giá trị được cố định ngay khi khai báo và không thể thay đổi về sau. Compiler sẽ chặn ngay lúc biên dịch nếu bạn lỡ gán lại.

**Lợi ích:**
1. Tránh sửa nhầm giá trị quan trọng.
2. Code dễ đọc: `PI`, `MAX_HOC_SINH` rõ nghĩa hơn số 3.14159 hay 50 rải rác khắp chương trình ("magic number").
3. Chỉ cần sửa một chỗ khi giá trị thay đổi.

⚠️ Biến `const` **phải được khởi tạo ngay khi khai báo**, vì sau đó không gán được nữa:

```c
const int x;        // khong khoi tao -> x mang gia tri rac mai mai
const int y = 10;   // DUNG
```

*(Khác với C++ báo lỗi, C vẫn cho biên dịch dòng `const int x;` — gcc thậm chí không cảnh báo — nhưng biến `x` trở nên vô dụng vì không bao giờ gán được giá trị.)*

### Bài 10.

| Tên cũ | Tên nên đặt | Kiểu |
|---|---|---|
| `int a` | `soLuongHocSinh` | `int` |
| `double x` | `diemTrungBinh` | `double` |
| `char k` | `xepLoai` | `char` |
| `bool t` | `daNopHocPhi` | `bool` (cần `<stdbool.h>`) |
| `int n1` | `tongSoTienThu` | `long long` (tiền có thể lớn) |

```c
int       soLuongHocSinh = 45;
double    diemTrungBinh  = 7.85;
char      xepLoai        = 'B';
bool      daNopHocPhi    = true;
long long tongSoTienThu  = 135000000;
```

**Nguyên tắc đặt tên tốt:**
- Tên nói lên **ý nghĩa** chứ không phải kiểu dữ liệu.
- Biến `bool` nên bắt đầu bằng `is`, `has`, `da`, `co` → `isValid`, `daNopHocPhi`.
- Biến đếm số lượng nên có tiền tố `so`, `count`, `num` → `soHocSinh`.
- Chỉ dùng tên một chữ cái (`i`, `j`, `k`) cho **biến đếm vòng lặp**.

### Bài 11.

**camelCase** (chữ đầu thường, các từ sau viết hoa chữ cái đầu):

```c
#include <stdio.h>

int main(void) {
    int    soHocSinh     = 45;
    double diemTrungBinh = 7.85;
    double tongDiem      = soHocSinh * diemTrungBinh;
    printf("Tong diem ca lop: %.2f\n", tongDiem);
    return 0;
}
```

**snake_case** (tất cả chữ thường, nối bằng `_`):

```c
#include <stdio.h>

int main(void) {
    int    so_hoc_sinh     = 45;
    double diem_trung_binh = 7.85;
    double tong_diem       = so_hoc_sinh * diem_trung_binh;
    printf("Tong diem ca lop: %.2f\n", tong_diem);
    return 0;
}
```

Output (cả hai): `Tong diem ca lop: 353.25`

| | camelCase | snake_case |
|---|---|---|
| Ưu điểm | Ngắn hơn, phổ biến trong Java/JavaScript/C# | Dễ đọc hơn khi tên dài |
| Thường dùng ở | Nhiều dự án ứng dụng, lập trình Windows | Rất phổ biến trong thế giới C: nhân Linux, Git, thư viện GNU; tên hàm chuẩn C cũng viết thường (`strlen`, `isdigit`) |

**Điều quan trọng nhất không phải chọn kiểu nào, mà là chọn một kiểu và dùng nhất quán trong toàn bộ dự án.**

### Bài 12.

| Từ | Có phải keyword (C11)? | Giải thích |
|---|---|---|
| `main` | ❌ Không | Là **tên hàm** đặc biệt (điểm bắt đầu chương trình), nhưng không phải từ khoá |
| `printf` | ❌ Không | Là một **hàm** của thư viện chuẩn, khai báo trong `<stdio.h>` |
| `bool` | ❌ Không | Là **macro** định nghĩa trong `<stdbool.h>`, thay cho `_Bool` (C23 mới là từ khoá) |
| `_Bool` | ✅ **Có** | Từ khoá (từ C99), kiểu đúng/sai gốc của C |
| `true` | ❌ Không | Là **macro** trong `<stdbool.h>`, có giá trị 1 (C23 mới là từ khoá) |
| `sizeof` | ✅ **Có** | Từ khoá, là toán tử lấy kích thước |
| `NULL` | ❌ Không | Là **macro** (con trỏ rỗng) định nghĩa trong `<stddef.h>`, `<stdio.h>`, `<stdlib.h>`… |
| `size` | ❌ Không | Tên bình thường, hoàn toàn có thể dùng làm tên biến |

**Điểm mấu chốt:** rất nhiều thứ bạn gõ hằng ngày (`printf`, `scanf`, `bool`, `true`, `NULL`) **không phải từ khoá của ngôn ngữ** mà là các thành phần của **thư viện chuẩn**. Vì thế bạn *có thể* đặt biến tên `printf`, compiler không cấm — nhưng nó sẽ che mất hàm `printf` và gây lỗi khó hiểu.

### Bài 13.

```c
#include <stdio.h>

int x = 100;        // bien TOAN CUC (global)

int main(void) {
    int x = 50;     // bien CUC BO (local), che mat bien toan cuc

    printf("Bien cuc bo   x = %d\n", x);       // 50
    {
        extern int x;   // trong khoi nay, x la bien toan cuc
        printf("Bien toan cuc x = %d\n", x);   // 100
    }
    return 0;
}
```

Output:

```
Bien cuc bo   x = 50
Bien toan cuc x = 100
```

**Giải thích:**
- Khi có 2 biến trùng tên, biến ở **phạm vi gần nhất** (cục bộ) sẽ "che" (shadow) biến bên ngoài.
- C **không có** toán tử `::` như C++. Khai báo `extern int x;` bên trong một khối mới báo cho compiler rằng "`x` ở đây là biến `x` được định nghĩa ở phạm vi toàn cục", nên trong khối đó ta truy cập được biến toàn cục.

⚠️ Trong thực tế nên **tránh** đặt trùng tên như vậy — nó gây nhầm lẫn và là nguồn lỗi phổ biến. Compiler có thể cảnh báo với `-Wshadow`. Cách đơn giản nhất là **đặt tên khác nhau** (ví dụ biến toàn cục có tiền tố `g_`: `g_x`).

### Bài 14.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    char      tenSach[] = "Lap trinh C co ban";
    char      tacGia[]  = "Nguyen Van A";
    int       soTrang   = 350;
    long long gia       = 185000;       // VND
    bool      conHang   = true;

    printf("==================================\n");
    printf("          HOA DON BAN SACH        \n");
    printf("==================================\n");
    printf("%-12s: %s\n",   "Ten sach",   tenSach);
    printf("%-12s: %s\n",   "Tac gia",    tacGia);
    printf("%-12s: %d\n",   "So trang",   soTrang);
    printf("%-12s: %lld VND\n", "Gia ban", gia);
    printf("%-12s: %s\n",   "Tinh trang", conHang ? "Con hang" : "Het hang");
    printf("==================================\n");
    return 0;
}
```

Output:

```
==================================
          HOA DON BAN SACH        
==================================
Ten sach    : Lap trinh C co ban
Tac gia     : Nguyen Van A
So trang    : 350
Gia ban     : 185000 VND
Tinh trang  : Con hang
==================================
```

**Giải thích:**
- C không có kiểu `string`, nên tên sách và tác giả được lưu bằng **mảng ký tự** `char tenSach[] = "...";` và in bằng đặc tả `%s`.
- `%-12s` in chuỗi trong ô rộng 12 ký tự, căn trái (dấu `-`), giúp các dấu `:` thẳng cột.

### Bài 15.

**Output:**

```
20
10
```

**Giải thích — Phạm vi (scope) của biến:**

```c
int main(){
    int x = 10;          // x thu nhat, song trong toan bo main
    {                    // <- mo mot KHOI (block) moi
        int x = 20;      // x thu hai, chi song trong khoi nay, CHE x ben ngoai
        printf("%d\n", x);   // -> 20 (x gan nhat)
    }                    // <- het khoi, x thu hai bi HUY
    printf("%d\n", x);   // -> 10 (x thu nhat van con nguyen)
    return 0;
}
```

**Các quy tắc cần nhớ:**

1. Biến chỉ tồn tại từ lúc khai báo đến dấu `}` đóng khối chứa nó.
2. Khi có nhiều biến trùng tên, biến ở khối **trong cùng** được ưu tiên (shadowing).
3. Ra khỏi khối, biến bị huỷ và bộ nhớ được thu hồi.

Lỗi thường gặp do không nắm scope:

```c
for (int i = 0; i < 5; i++) {
    int tong = 0;         // tong bi tao lai = 0 moi vong lap!
    tong += i;
}
printf("%d", i);          // LOI: 'i' undeclared
```

Sửa lại:

```c
int tong = 0;             // khai bao NGOAI vong lap
for (int i = 0; i < 5; i++) {
    tong += i;
}
printf("%d", tong);       // 10
```
