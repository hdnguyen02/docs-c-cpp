# Lời giải — [C]. If Else

[← Quay lại bài học](../03-01-c-if-else.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    if (n > 0)      printf("%d la so DUONG\n", n);
    else if (n < 0) printf("%d la so AM\n", n);
    else            printf("n BANG 0\n");

    return 0;
}
```

### Bài 2.

```c
#include <stdio.h>

int main() {
    int a, b;
    printf("Nhap a va b: ");
    scanf("%d %d", &a, &b);

    if (a > b)      printf("So lon hon la: %d\n", a);
    else if (b > a) printf("So lon hon la: %d\n", b);
    else            printf("Hai so bang nhau\n");

    return 0;
}
```

### Bài 3.

```c
#include <stdio.h>

int main() {
    int a, b, c;
    printf("Nhap 3 so: ");
    scanf("%d %d %d", &a, &b, &c);

    int lonNhat;
    if (a >= b) {
        if (a >= c) lonNhat = a;
        else        lonNhat = c;
    } else {
        if (b >= c) lonNhat = b;
        else        lonNhat = c;
    }

    printf("So lon nhat = %d\n", lonNhat);
    return 0;
}
```

**Cách khác — dùng biến tạm, dễ mở rộng cho n số:**

```c
int lonNhat = a;
if (b > lonNhat) lonNhat = b;
if (c > lonNhat) lonNhat = c;
```

Cách thứ hai ngắn hơn và mở rộng được cho 10, 100 số (chỉ cần thêm dòng), trong khi `if` lồng nhau sẽ bùng nổ số nhánh.

### Bài 4.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    if (n % 2 == 0 && n % 3 == 0 && n % 5 == 0) {
        printf("%d chia het cho ca 2, 3 va 5\n", n);
    } else {
        printf("%d KHONG chia het cho ca 2, 3 va 5\n", n);
    }
    return 0;
}
```

💡 **Mẹo:** chia hết cho cả 2, 3, 5 tương đương chia hết cho **BCNN(2,3,5) = 30**. Nên có thể viết gọn: `if (n % 30 == 0)`.

### Bài 5.

```c
#include <stdio.h>

int main() {
    double dtb;
    printf("Nhap diem trung binh: ");
    scanf("%lf", &dtb);

    if (dtb < 0 || dtb > 10) {
        printf("Diem khong hop le!\n");
        return 1;
    }

    if      (dtb >= 8.5) printf("Xep loai: GIOI\n");
    else if (dtb >= 7.0) printf("Xep loai: KHA\n");
    else if (dtb >= 5.0) printf("Xep loai: TRUNG BINH\n");
    else                 printf("Xep loai: YEU\n");

    return 0;
}
```

**Điểm quan trọng về thứ tự `else if`:** phải xếp từ điều kiện **chặt nhất xuống lỏng nhất**. Nếu viết ngược lại:

```c
if      (dtb >= 5.0) printf("TRUNG BINH");     // SAI!
else if (dtb >= 7.0) printf("KHA");            // khong bao gio chay toi
else if (dtb >= 8.5) printf("GIOI");           // khong bao gio chay toi
```

thì điểm 9.0 cũng bị xếp "TRUNG BÌNH", vì nó thoả điều kiện đầu tiên và `else if` sau không được xét nữa.

Nhờ cơ chế `else if`, ta **không cần** viết `dtb >= 7.0 && dtb < 8.5` — nếu chạy tới nhánh đó thì chắc chắn `dtb < 8.5` rồi.

⚠️ Nhập `double` bằng `scanf` phải dùng `%lf`.

### Bài 6.

```c
#include <stdio.h>

int main() {
    int tuoi;
    printf("Nhap tuoi: ");
    scanf("%d", &tuoi);

    if      (tuoi < 0)   printf("Tuoi khong hop le!\n");
    else if (tuoi < 6)   printf("Mam non\n");
    else if (tuoi <= 10) printf("Tieu hoc\n");
    else if (tuoi <= 14) printf("THCS\n");
    else if (tuoi <= 17) printf("THPT\n");
    else                 printf("Dai hoc / Di lam\n");

    return 0;
}
```

Ở đây thứ tự ngược lại bài 5: điều kiện xếp **từ nhỏ đến lớn**, vì ta dùng dấu `<`/`<=`.

### Bài 7.

```c
#include <stdio.h>

int main() {
    int a, b, c;
    printf("Nhap 3 canh: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a <= 0 || b <= 0 || c <= 0) {
        printf("Canh phai la so duong!\n");
    } else if (a + b > c && a + c > b && b + c > a) {
        printf("La tam giac HOP LE\n");
    } else {
        printf("KHONG phai tam giac\n");
    }
    return 0;
}
```

**Bất đẳng thức tam giác:** tổng 2 cạnh bất kỳ phải **lớn hơn** (không phải ≥) cạnh còn lại. Nếu bằng nhau (`a + b == c`) thì 3 điểm thẳng hàng, không tạo thành tam giác.

⚠️ Với cạnh là số lớn, `a + b` có thể tràn `int`. Khi đó dùng `long long` hoặc viết `a > c - b`.

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    long long a, b, c;
    printf("Nhap 3 canh tam giac: ");
    scanf("%lld %lld %lld", &a, &b, &c);

    bool deu   = (a == b && b == c);
    bool can   = (a == b || b == c || a == c);
    bool vuong = (a*a == b*b + c*c) || (b*b == a*a + c*c) || (c*c == a*a + b*b);

    if      (deu)          printf("Tam giac DEU\n");
    else if (vuong && can) printf("Tam giac VUONG CAN\n");
    else if (vuong)        printf("Tam giac VUONG\n");
    else if (can)          printf("Tam giac CAN\n");
    else                   printf("Tam giac THUONG\n");

    return 0;
}
```

**Thứ tự kiểm tra rất quan trọng:** phải xét **đều** trước (vì tam giác đều cũng là cân), rồi **vuông cân** trước **vuông** và **cân** (vì nó thoả cả hai).

Kiểm thử:

| a | b | c | Kết quả |
|---|---|---|---|
| 5 | 5 | 5 | Đều |
| 3 | 4 | 5 | Vuông |
| 1 | 1 | 1.414… | Vuông cân *(không nhập được với số nguyên)* |
| 5 | 5 | 8 | Cân |
| 4 | 5 | 6 | Thường |

⚠️ Với **số nguyên**, tam giác vuông cân thực tế không tồn tại (cạnh huyền `a√2` luôn vô tỉ). Muốn xử lý số thực, phải dùng `double` và so sánh bằng `fabs(x - y) < EPS` (`fabs` trong `<math.h>`).

💡 Kiểu `bool` cần `#include <stdbool.h>`; `long long` nhập bằng `%lld`.

### Bài 9.

```c
#include <stdio.h>

int main() {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    if (c >= 'A' && c <= 'Z') {
        printf("'%c' la CHU HOA (ASCII %d)\n", c, c);
    } else if (c >= 'a' && c <= 'z') {
        printf("'%c' la CHU THUONG (ASCII %d)\n", c, c);
    } else if (c >= '0' && c <= '9') {
        printf("'%c' la CHU SO, gia tri = %d\n", c, c - '0');
    } else {
        printf("'%c' la KY TU DAC BIET (ASCII %d)\n", c, c);
    }
    return 0;
}
```

**Cơ sở của cách kiểm tra:** trong bảng ASCII, các nhóm ký tự nằm **liên tiếp nhau**:

| Nhóm | Mã ASCII |
|---|---|
| `'0'` … `'9'` | 48 … 57 |
| `'A'` … `'Z'` | 65 … 90 |
| `'a'` … `'z'` | 97 … 122 |

Nên `c >= 'A' && c <= 'Z'` chính là kiểm tra `c` có nằm trong khoảng 65–90.

💡 `c - '0'` đổi ký tự số thành giá trị số: `'7' - '0'` = `55 - 48` = `7`. In mã ASCII chỉ cần in biến `char` bằng `%d`.

💡 Dấu cách trước `%c` trong `scanf(" %c", &c)` giúp bỏ qua các khoảng trắng/dấu xuống dòng còn sót lại trong bộ đệm.

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int nam;
    printf("Nhap nam: ");
    scanf("%d", &nam);

    bool nhuan;

    if (nam % 4 != 0) {
        nhuan = false;                  // khong chia het 4 -> chac chan khong nhuan
    } else {
        if (nam % 100 != 0) {
            nhuan = true;               // chia het 4, khong chia het 100 -> nhuan
        } else {
            if (nam % 400 == 0) {
                nhuan = true;           // chia het 400 -> nhuan
            } else {
                nhuan = false;          // chia het 100 nhung khong chia het 400
            }
        }
    }

    printf("%d %s nam nhuan\n", nam, nhuan ? "LA" : "KHONG LA");
    return 0;
}
```

So sánh với bản gộp bằng toán tử logic:

```c
bool nhuan = (nam % 4 == 0 && nam % 100 != 0) || (nam % 400 == 0);
```

Bản gộp ngắn hơn nhiều, nhưng bản `if` lồng thể hiện rõ **luồng suy nghĩ**. Với logic phức tạp hơn, bản lồng dễ debug hơn (đặt breakpoint được ở từng nhánh).

### Bài 11.

```c
#include <stdio.h>

int main() {
    double soKwh;
    printf("Nhap so dien tieu thu (kWh): ");
    scanf("%lf", &soKwh);

    double tien = 0;

    if (soKwh <= 50) {
        tien = soKwh * 1800;
    } else if (soKwh <= 100) {
        tien = 50 * 1800 + (soKwh - 50) * 1900;
    } else {
        tien = 50 * 1800 + 50 * 1900 + (soKwh - 100) * 2200;
    }

    printf("So dien : %.0f kWh\n", soKwh);
    printf("Tien dien: %.0f VND\n", tien);
    return 0;
}
```

Kiểm thử:

| kWh | Tính | Tiền |
|---|---|---|
| 30 | 30 × 1800 | 54.000 |
| 50 | 50 × 1800 | 90.000 |
| 80 | 50×1800 + 30×1900 | 147.000 |
| 150 | 50×1800 + 50×1900 + 50×2200 | 295.000 |

⚠️ **Lỗi phổ biến:** tính `soKwh * 1900` cho toàn bộ khi vượt 50 kWh. Giá bậc thang chỉ áp dụng cho **phần vượt**, nên phải trừ đi: `(soKwh - 50) * 1900`.

### Bài 12.

```c
#include <stdio.h>

int main() {
    double tien;
    printf("Nhap so tien mua hang (VND): ");
    scanf("%lf", &tien);

    double phanTramGiam;

    if      (tien >= 5000000) phanTramGiam = 15;
    else if (tien >= 2000000) phanTramGiam = 10;
    else if (tien >=  500000) phanTramGiam = 5;
    else                      phanTramGiam = 0;

    double tienGiam  = tien * phanTramGiam / 100;
    double phaiTra   = tien - tienGiam;

    printf("-----------------------------\n");
    printf("Tong tien hang : %12.0f VND\n", tien);
    printf("Muc giam gia   : %12.0f %%\n", phanTramGiam);
    printf("Duoc giam      : %12.0f VND\n", tienGiam);
    printf("PHAI TRA       : %12.0f VND\n", phaiTra);
    printf("-----------------------------\n");
    return 0;
}
```

💡 `%12.0f` in số thực không có phần thập phân, canh phải trong độ rộng 12 ký tự. Muốn in dấu `%` phải viết `%%`.

⚠️ Nhớ thứ tự **từ mức cao xuống thấp**, giống bài 5.

### Bài 13.

```c
int n;
scanf("%d", &n);
if (n = 0) printf("Bang khong");       // <- LOI!
else printf("Khac khong");
```

**Lỗi:** dùng toán tử **gán `=`** thay vì **so sánh `==`**.

Chuyện gì xảy ra:
1. `n = 0` **gán** 0 cho `n` (giá trị người dùng nhập bị xoá!)
2. Biểu thức gán trả về giá trị vừa gán, tức `0`
3. `0` được hiểu là **sai**
4. → **luôn** vào nhánh `else`, in "Khac khong" với mọi đầu vào

**Sửa:**

```c
if (n == 0) printf("Bang khong");
else printf("Khac khong");
```

**Cách phòng tránh:**

1. Biên dịch với `-Wall`, compiler sẽ cảnh báo:
```
warning: suggest parentheses around assignment used as truth value
```

2. Dùng **điều kiện Yoda** — đặt hằng số bên trái:
```c
if (0 == n) { ... }      // neu lo viet 0 = n thi LOI BIEN DICH ngay
```

Lỗi `=` thay `==` là lỗi kinh điển và nguy hiểm vì **chương trình vẫn chạy**, chỉ cho kết quả sai.

### Bài 14.

```c
int n; scanf("%d", &n);
if (n > 0);                      // <- dau ; THUA o day!
    printf("So duong\n");
```

**Với `n = 5`** in ra `So duong`. **Nhưng với `n = -3` cũng in ra `So duong`!**

**Giải thích:** dấu `;` ngay sau `if (n > 0)` tạo thành một **câu lệnh rỗng** — đó chính là thân của `if`. Compiler hiểu code này là:

```c
if (n > 0) {
    // khong lam gi ca
}
printf("So duong\n");      // <- LUON chay, khong thuoc if
```

Phần thụt lề chỉ đánh lừa mắt người, C **không quan tâm thụt lề** (khác Python).

**Sửa:** bỏ dấu `;`

```c
if (n > 0)
    printf("So duong\n");
```

✅ **Thói quen phòng tránh: LUÔN dùng dấu ngoặc nhọn `{}` cho thân `if`**, kể cả khi chỉ có 1 câu lệnh:

```c
if (n > 0) {
    printf("So duong\n");
}
```

Điều này cũng tránh được lỗi khác: sau này thêm dòng thứ hai vào mà quên thêm `{}`.

Biên dịch với `-Wall -Wextra` sẽ được cảnh báo `warning: suggest braces around empty body in an 'if' statement`.

### Bài 15.

```c
#include <stdio.h>

int main() {
    int a, b, c, d, t;
    printf("Nhap 4 so: ");
    scanf("%d %d %d %d", &a, &b, &c, &d);

    // Mang bot: moi lan so sanh 2 so ke nhau, so lon "noi" ve cuoi
    // Luot 1: dua so lon nhat ve vi tri d
    if (a > b) { t = a; a = b; b = t; }
    if (b > c) { t = b; b = c; c = t; }
    if (c > d) { t = c; c = d; d = t; }

    // Luot 2: dua so lon thu 2 ve vi tri c
    if (a > b) { t = a; a = b; b = t; }
    if (b > c) { t = b; b = c; c = t; }

    // Luot 3: sap xep 2 so con lai
    if (a > b) { t = a; a = b; b = t; }

    printf("Sap xep tang dan: %d %d %d %d\n", a, b, c, d);
    return 0;
}
```

Ví dụ nhập `9 3 7 1`:

```
Sap xep tang dan: 1 3 7 9
```

**Đây chính là thuật toán sắp xếp nổi bọt (Bubble Sort)** viết tay, không dùng vòng lặp:

```
Luot 1: 9 3 7 1 -> 3 9 7 1 -> 3 7 9 1 -> 3 7 1 9   (9 ve cuoi)
Luot 2: 3 7 1 9 -> 3 7 1 9 -> 3 1 7 9              (7 ve vi tri ap chot)
Luot 3: 3 1 7 9 -> 1 3 7 9                         (xong)
```

Với 4 số cần `3 + 2 + 1 = 6` phép so sánh. Với `n` số cần `n(n−1)/2` — đó là lý do phải dùng vòng lặp khi `n` lớn (xem chương 6).

⚠️ Mỗi lần hoán đổi phải bọc 3 lệnh trong `{}`. Nếu viết `if (a > b) t = a; a = b; b = t;` thì chỉ `t = a;` thuộc `if`, hai lệnh sau **luôn chạy** → sai.

Cách viết ngắn gọn hơn dùng mảng và hàm `qsort` của `<stdlib.h>` (sẽ học ở chương mảng):

```c
int soSanh(const void *x, const void *y) {
    return *(const int *)x - *(const int *)y;
}

int a[4];
for (int i = 0; i < 4; i++) scanf("%d", &a[i]);
qsort(a, 4, sizeof(int), soSanh);
for (int i = 0; i < 4; i++) printf("%d ", a[i]);
```
