# Lời giải — [C]. Nhập Xuất Với scanf Và printf

[← Quay lại bài học](../02-05-c-nhap-xuat-voi-scanf-va-printf.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    char ten[50];
    int tuoi;
    double diemTB;

    printf("Nhap ho ten (viet lien): ");
    scanf("%49s", ten);             // mang char: KHONG co &
    printf("Nhap tuoi: ");
    scanf("%d", &tuoi);
    printf("Nhap diem TB: ");
    scanf("%lf", &diemTB);          // double: %lf khi nhap

    printf("Sinh vien %s, %d tuoi, diem TB: %.2f\n", ten, tuoi, diemTB);
    return 0;
}
```

Ví dụ chạy:

```
Nhap ho ten (viet lien): NguyenVanA
Nhap tuoi: 19
Nhap diem TB: 8.25
Sinh vien NguyenVanA, 19 tuoi, diem TB: 8.25
```

*(Mảng `char` và chuỗi ký tự sẽ được học kỹ ở chương 9.)*

### Bài 2.

```c
#include <stdio.h>

int main() {
    int a, b;
    printf("Nhap a va b: ");
    scanf("%d%d", &a, &b);

    printf("Tong   = %d\n", a + b);
    printf("Hieu   = %d\n", a - b);
    printf("Tich   = %d\n", a * b);
    printf("Thuong = %f\n", (double)a / b);   // ep kieu de co phan thap phan
    return 0;
}
```

Ví dụ chạy:

```
Nhap a va b: 10 3
Tong   = 13
Hieu   = 7
Tich   = 30
Thuong = 3.333333
```

⚠️ Nếu viết `a / b` (cả hai đều `int`) thì được **3** chứ không phải 3.333333 — đây là phép chia nguyên. Và khi đó phải in bằng `%d`; in một biểu thức `int` bằng `%f` là sai đặc tả, cho ra số rác.

### Bài 3.

```c
#include <stdio.h>

int main() {
    const double PI = 3.14159265358979;
    double r;

    printf("Nhap ban kinh: ");
    scanf("%lf", &r);

    printf("Chu vi    = %.2f\n", 2 * PI * r);
    printf("Dien tich = %.2f\n", PI * r * r);
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

```c
#include <stdio.h>

int main() {
    double x;
    printf("Nhap so thuc: ");
    scanf("%lf", &x);

    printf("0  chu so : %.0f\n", x);
    printf("3  chu so : %.3f\n", x);
    printf("6  chu so : %.6f\n", x);
    printf("10 chu so : %.10f\n", x);
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

**Lưu ý:** `%.kf` **làm tròn**, không cắt bỏ.

💡 Số chữ số thập phân cũng có thể truyền bằng biến: `printf("%.*f", k, x);` — dấu `*` sẽ lấy giá trị `k` làm độ chính xác.

### Bài 5.

```c
#include <stdio.h>

int main() {
    int a, b, c;
    printf("Nhap 3 so nguyen: ");
    scanf("%d%d%d", &a, &b, &c);

    printf("%10d\n", a);
    printf("%10d\n", b);
    printf("%10d\n", c);
    return 0;
}
```

Ví dụ với `12 345 6789`:

```
        12
       345
      6789
```

**Giải thích:** `%10d` đặt độ rộng tối thiểu 10 ký tự cho **giá trị ứng với đặc tả đó**. Mặc định căn phải nên phần thiếu được đệm dấu cách ở bên trái.

⚠️ Nếu giá trị dài hơn độ rộng (ví dụ số có 12 chữ số với `%10d`) thì printf **không cắt** mà in đủ, chỉ là cột bị lệch.

### Bài 6.

printf chỉ tự đệm được bằng dấu cách hoặc số `0`. Muốn đệm bằng `*`, ta tự tính số ký tự còn thiếu rồi in đúng bấy nhiêu dấu `*`:

```c
#include <stdio.h>

int main() {
    int a, b, c;
    const char *sao = "**********";      // 10 dau *
    printf("Nhap 3 so nguyen: ");
    scanf("%d%d%d", &a, &b, &c);

    // snprintf(NULL, 0, ...) khong in gi, chi tra ve so ky tu SE in ra
    int la = snprintf(NULL, 0, "%d", a);
    int lb = snprintf(NULL, 0, "%d", b);
    int lc = snprintf(NULL, 0, "%d", c);

    // %.*s : in toi da (10 - do dai) ky tu dau cua chuoi sao
    printf("%.*s%d\n", 10 - la, sao, a);
    printf("%.*s%d\n", 10 - lb, sao, b);
    printf("%.*s%d\n", 10 - lc, sao, c);
    return 0;
}
```

Output:

```
********12
*******345
******6789
```

**Giải thích:**
- `snprintf(NULL, 0, "%d", a)` trả về số ký tự cần để in `a` (ví dụ `345` → 3) mà không in gì ra màn hình.
- `%.*s` với chuỗi: độ chính xác là **số ký tự tối đa** được in. Dấu `*` lấy giá trị đó từ tham số `10 - la`.
- Khi học vòng lặp (chương 4) bạn có thể thay bằng cách đơn giản hơn: lặp in `'*'` đúng `10 - la` lần.

### Bài 7.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap so nguyen: ");
    scanf("%d", &n);

    printf("%08d\n", n);
    return 0;
}
```

Ví dụ: nhập `123` → `00000123`

**Ứng dụng:** định dạng mã đơn hàng, mã sinh viên, số hoá đơn — những thứ cần cố định độ dài.

### Bài 8.

```c
#include <stdio.h>

int main() {
    int n = 5;
    for (int i = 1; i <= 10; i++) {
        printf("%2d x %2d = %2d\n", n, i, n * i);
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

*(Nếu chưa học vòng lặp, bạn có thể viết 10 dòng `printf` riêng.)*

### Bài 9.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int x;
    printf("Nhap 0 hoac 1: ");
    scanf("%d", &x);        // scanf khong co dac ta cho bool -> nhap vao int

    bool b = x;             // khac 0 -> true, bang 0 -> false

    printf("Dang so   : %d\n", b);
    printf("Dang chu  : %s\n", b ? "true" : "false");
    return 0;
}
```

Ví dụ nhập `1`:

```
Dang so   : 1
Dang chu  : true
```

**Lưu ý:** không được viết `scanf("%d", &b);` với `b` là `bool` — `%d` cần địa chỉ một `int` (4 byte) trong khi `bool` chỉ có 1 byte, ghi đè sai vùng nhớ. Hãy nhập vào `int` rồi gán sang.

### Bài 10.

```c
#include <stdio.h>

int main() {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    printf("Ky tu        : %c\n", c);
    printf("Ma ASCII     : %d\n", c);
    printf("Ky tu ke tiep: %c\n", c + 1);
    return 0;
}
```

Ví dụ nhập `A`:

```
Ky tu        : A
Ma ASCII     : 65
Ky tu ke tiep: B
```

💡 Trong C, **đặc tả quyết định cách in**: cùng giá trị `c + 1` (bằng 66), in bằng `%c` ra `B`, in bằng `%d` ra `66`. Không cần ép kiểu như khi dùng các cơ chế in tự nhận kiểu.

### Bài 11.

```c
#include <stdio.h>

int main() {
    const char *ten[3]  = {"But bi", "Vo o ly 200 trang", "Thuoc ke 30cm"};
    int    soLuong[3]   = {10, 5, 3};
    double donGia[3]    = {5000, 12000, 8500};

    printf("=========================================================\n");
    printf("%-22s%8s%12s%14s\n", "TEN HANG", "SL", "DON GIA", "THANH TIEN");
    printf("---------------------------------------------------------\n");

    double tongCong = 0;
    for (int i = 0; i < 3; i++) {
        double thanhTien = soLuong[i] * donGia[i];
        tongCong += thanhTien;
        printf("%-22s%8d%12.0f%14.0f\n", ten[i], soLuong[i], donGia[i], thanhTien);
    }

    printf("---------------------------------------------------------\n");
    printf("%-42s%14.0f\n", "TONG CONG", tongCong);
    printf("=========================================================\n");
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
TONG CONG                                         135500
=========================================================
```

**Điểm mấu chốt:** `%-22s` căn trái (dùng cho cột chữ), `%8d`, `%12.0f` căn phải (dùng cho cột số). Mỗi đặc tả chỉ áp dụng cho **đúng một** giá trị, nên phải ghi lại độ rộng ở mỗi cột, mỗi dòng.

### Bài 12.

```c
#include <stdio.h>

int main() {
    int tongGiay;
    printf("Nhap tong so giay: ");
    scanf("%d", &tongGiay);

    int gio   = tongGiay / 3600;
    int phut  = (tongGiay % 3600) / 60;
    int giay  = tongGiay % 60;

    printf("%02d:%02d:%02d\n", gio, phut, giay);
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

`%02d` = độ rộng 2, đệm số `0` phía trước.

### Bài 13.

**Output:**

```
1.235
9.876540
```

**Giải thích:** trong C, **mỗi lệnh printf hoàn toàn độc lập**. Độ chính xác `.3` nằm bên trong đặc tả `%.3f` nên chỉ áp dụng cho đúng giá trị `1.23456`. Lệnh thứ hai dùng `%f` không ghi độ chính xác, nên lấy mặc định là **6 chữ số thập phân** (và làm tròn `9.87654` thành `9.876540`).

| Muốn | Viết |
|---|---|
| Mặc định 6 chữ số | `%f` |
| k chữ số cố định | `%.kf`, ví dụ `%.3f` |
| k lấy từ biến | `%.*f` kèm tham số `k` |
| Độ rộng w, k chữ số | `%w.kf`, ví dụ `%8.3f` |

Muốn mọi số đều in 3 chữ số thì phải viết `%.3f` ở **mọi** chỗ cần in.

### Bài 14.

```c
#include <stdio.h>

int main() {
    char ten[50];

    // CACH SAI
    printf("Nhap ho ten: ");
    scanf("%49s", ten);
    printf("Ket qua voi scanf %%s : [%s]\n", ten);

    return 0;
}
```

Nhập `Nguyen Van A` → in ra:

```
Ket qua voi scanf %s : [Nguyen]
```

**Nguyên nhân:** `%s` **dừng lại ở khoảng trắng đầu tiên** (dấu cách, tab, xuống dòng). Nó chỉ đọc được một "từ". Phần ` Van A` vẫn còn nằm lại trong bộ đệm bàn phím.

**Cách đúng — dùng `fgets` đọc cả dòng:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char ten[50];
    printf("Nhap ho ten: ");
    fgets(ten, sizeof(ten), stdin);        // doc CA DONG, ke ca dau cach
    ten[strcspn(ten, "\n")] = '\0';        // xoa ky tu '\n' ma fgets giu lai
    printf("Xin chao, %s!\n", ten);
    return 0;
}
```

⚠️ **Bẫy trôi lệnh:** nếu trước đó có `scanf("%d", &n);` thì ký tự Enter còn sót lại sẽ khiến `fgets` ngay sau đó đọc được chuỗi rỗng:

```c
int tuoi;
char ten[50];
scanf("%d", &tuoi);
getchar();                         // <- BAT BUOC: bo ky tu Enter con sot lai
fgets(ten, sizeof(ten), stdin);
```

⚠️ Tuyệt đối **không dùng `gets`** — hàm này không giới hạn độ dài, dễ tràn mảng và đã bị loại khỏi chuẩn C11.

Chủ đề này được nói kỹ ở bài [09-02 — Xử lý trôi lệnh khi nhập chuỗi](../09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi.md).

### Bài 15.

```c
#include <stdio.h>

#define N 3

int main() {
    char ten[N][21];
    double toan[N], ly[N], hoa[N];

    for (int i = 0; i < N; i++) {
        printf("--- Sinh vien %d ---\n", i + 1);
        printf("Ten (viet lien): ");
        scanf("%20s", ten[i]);
        printf("Diem Toan, Ly, Hoa: ");
        scanf("%lf%lf%lf", &toan[i], &ly[i], &hoa[i]);
    }

    printf("\n");
    printf("+------+----------------------+--------+--------+--------+--------+\n");
    printf("| %-4s | %-20s | %6s | %6s | %6s | %6s |\n",
           "STT", "HO TEN", "TOAN", "LY", "HOA", "DTB");
    printf("+------+----------------------+--------+--------+--------+--------+\n");

    for (int i = 0; i < N; i++) {
        double dtb = (toan[i] + ly[i] + hoa[i]) / 3;
        printf("| %-4d | %-20s | %6.2f | %6.2f | %6.2f | %6.2f |\n",
               i + 1, ten[i], toan[i], ly[i], hoa[i], dtb);
    }
    printf("+------+----------------------+--------+--------+--------+--------+\n");
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

💡 `char ten[N][21]` là mảng 3 chuỗi, mỗi chuỗi tối đa 20 ký tự (mảng 2 chiều sẽ học ở chương 8). `%20s` giới hạn số ký tự đọc để không tràn.
