# Lời giải — [C]. If Và Else If

[← Quay lại bài học](../03-02-c-if-va-else-if.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    int thang;
    printf("Nhap thang (1-12): ");
    scanf("%d", &thang);

    if      (thang >= 1  && thang <= 3)  printf("Quy I\n");
    else if (thang >= 4  && thang <= 6)  printf("Quy II\n");
    else if (thang >= 7  && thang <= 9)  printf("Quy III\n");
    else if (thang >= 10 && thang <= 12) printf("Quy IV\n");
    else                                 printf("Thang khong hop le!\n");

    return 0;
}
```

💡 Cách tính nhanh không cần `if`: `quy = (thang - 1) / 3 + 1`

### Bài 2.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int m, y;
    printf("Nhap thang va nam: ");
    scanf("%d %d", &m, &y);

    if (m < 1 || m > 12) {
        printf("Thang khong hop le!\n");
    } else if (m == 1 || m == 3 || m == 5 || m == 7 ||
               m == 8 || m == 10 || m == 12) {
        printf("31 ngay\n");
    } else if (m == 4 || m == 6 || m == 9 || m == 11) {
        printf("30 ngay\n");
    } else {    // m == 2
        bool nhuan = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
        printf("%d ngay\n", nhuan ? 29 : 28);
    }
    return 0;
}
```

💡 **Mẹo nắm đấm:** nắm bàn tay lại, đếm các đốt xương và khe giữa chúng từ ngón trỏ — đốt nhô lên = 31 ngày, khe lõm = 30 ngày (trừ tháng 2). Tháng 8 quay lại đốt đầu tiên.

### Bài 3.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap thu (2-8): ");
    scanf("%d", &n);

    if      (n == 2) printf("Thu Hai\n");
    else if (n == 3) printf("Thu Ba\n");
    else if (n == 4) printf("Thu Tu\n");
    else if (n == 5) printf("Thu Nam\n");
    else if (n == 6) printf("Thu Sau\n");
    else if (n == 7) printf("Thu Bay\n");
    else if (n == 8) printf("Chu Nhat\n");
    else             printf("Khong hop le!\n");

    return 0;
}
```

Đây là trường hợp mà **`switch case` phù hợp hơn** — xem bài [03-03](../03-03-c-switch-case.md).

### Bài 4.

```c
#include <stdio.h>

int main() {
    int diem;
    printf("Nhap diem (0-100): ");
    scanf("%d", &diem);

    if (diem < 0 || diem > 100) { printf("Diem khong hop le!\n"); return 1; }

    char xepLoai;
    if      (diem >= 90) xepLoai = 'A';
    else if (diem >= 80) xepLoai = 'B';
    else if (diem >= 70) xepLoai = 'C';
    else if (diem >= 60) xepLoai = 'D';
    else                 xepLoai = 'F';

    printf("Diem %d -> Xep loai %c\n", diem, xepLoai);
    return 0;
}
```

### Bài 5.

```c
#include <stdio.h>

int main() {
    double bmi;
    printf("Nhap chi so BMI: ");
    scanf("%lf", &bmi);

    if      (bmi < 18.5) printf("Thieu can\n");
    else if (bmi < 25.0) printf("Binh thuong\n");
    else if (bmi < 30.0) printf("Thua can\n");
    else                 printf("Beo phi\n");

    return 0;
}
```

**Lưu ý mốc:** dùng `bmi < 25.0` chứ không phải `bmi <= 24.9`. Với số thực, giá trị 24.95 sẽ bị **rơi ra ngoài mọi nhánh** nếu dùng 24.9. Các mốc phải **liền nhau** không có khe hở.

### Bài 6.

```c
#include <stdio.h>

int main() {
    double chieuCao, canNang;
    printf("Nhap chieu cao (m)  : "); scanf("%lf", &chieuCao);
    printf("Nhap can nang (kg)  : "); scanf("%lf", &canNang);

    if (chieuCao <= 0 || canNang <= 0) {
        printf("Du lieu khong hop le!\n");
        return 1;
    }

    double bmi = canNang / (chieuCao * chieuCao);

    printf("Chi so BMI = %.2f -> ", bmi);

    if      (bmi < 18.5) printf("Thieu can\n");
    else if (bmi < 25.0) printf("Binh thuong\n");
    else if (bmi < 30.0) printf("Thua can\n");
    else                 printf("Beo phi\n");

    return 0;
}
```

Ví dụ: cao 1.70 m, nặng 65 kg → BMI = 22.49 → Bình thường.

⚠️ Chiều cao phải nhập theo **mét** (1.70), không phải cm (170). Nếu người dùng nhập 170, BMI sẽ ra 0.00.

### Bài 7.

```c
#include <stdio.h>

int main() {
    long long a, b, c;
    scanf("%lld %lld %lld", &a, &b, &c);

    if (a == b && b == c) {
        printf("1\n");                                      // deu
    } else if (a == b || b == c || a == c) {
        printf("2\n");                                      // can
    } else if (a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b) {
        printf("3\n");                                      // vuong
    } else {
        printf("4\n");                                      // thuong
    }
    return 0;
}
```

⚠️ Chú ý thứ tự: tam giác vuông cân thoả cả điều kiện "cân" lẫn "vuông". Với thứ tự trên nó sẽ được xếp là **cân** (in 2). Đề bài này không phân biệt vuông cân nên chấp nhận được; nếu cần thì thêm nhánh riêng như bài [03-01](../03-01-c-if-else.md) bài 8.

💡 Dùng `long long` (nhập bằng `%lld`) để `a*a` không bị tràn khi cạnh lớn.

### Bài 8.

```c
#include <stdio.h>
#include <ctype.h>

int main() {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    char thuong = (char)tolower((unsigned char)c);   // doi ve chu thuong de xet cho gon

    if (thuong == 'a' || thuong == 'e' || thuong == 'i' ||
        thuong == 'o' || thuong == 'u') {
        printf("'%c' la NGUYEN AM\n", c);
    } else if (isalpha((unsigned char)c)) {
        printf("'%c' la PHU AM\n", c);
    } else if (isdigit((unsigned char)c)) {
        printf("'%c' la CHU SO\n", c);
    } else {
        printf("'%c' la KY TU KHAC\n", c);
    }
    return 0;
}
```

Mẹo hay: dùng `tolower(c)` trước để không phải viết cả `'a'` lẫn `'A'` cho mỗi nguyên âm.

💡 Các hàm của `<ctype.h>` nhận tham số `int` phải là giá trị của `unsigned char` (hoặc `EOF`), nên ép `(unsigned char)c` là cách viết an toàn.

Cách gọn hơn nữa với `strchr` của `<string.h>` (tìm ký tự trong chuỗi, trả về `NULL` nếu không có):

```c
#include <string.h>
if (thuong != '\0' && strchr("aeiou", thuong) != NULL) { /* nguyen am */ }
```

### Bài 9.

```c
#include <stdio.h>

int main() {
    double t;
    printf("Nhap nhiet do (do C): ");
    scanf("%lf", &t);

    if      (t < 0)   printf("Bang gia\n");
    else if (t <= 15) printf("Lanh\n");
    else if (t <= 25) printf("Mat me\n");
    else if (t <= 35) printf("Nong\n");
    else              printf("Rat nong\n");

    return 0;
}
```

### Bài 10.

```c
#include <stdio.h>

int main() {
    double tien;
    int loaiKhach;

    printf("Nhap so tien: ");
    scanf("%lf", &tien);
    printf("Loai khach (1=Thuong, 2=Than thiet, 3=VIP): ");
    scanf("%d", &loaiKhach);

    double phanTram;
    const char *tenLoai;

    if (loaiKhach == 1)      { phanTram = 0;  tenLoai = "Thuong";     }
    else if (loaiKhach == 2) { phanTram = 10; tenLoai = "Than thiet"; }
    else if (loaiKhach == 3) { phanTram = 20; tenLoai = "VIP";        }
    else {
        printf("Loai khach khong hop le!\n");
        return 1;
    }

    double giam    = tien * phanTram / 100;
    double phaiTra = tien - giam;

    printf("Loai khach : %s\n", tenLoai);
    printf("Giam gia   : %.0f%% (%.0f VND)\n", phanTram, giam);
    printf("Phai tra   : %.0f VND\n", phaiTra);
    return 0;
}
```

💡 C không có kiểu `string`. Ở đây `const char *tenLoai` là **con trỏ** trỏ tới một hằng chuỗi, gán `tenLoai = "VIP";` chỉ đổi chỗ nó trỏ tới, không sao chép chuỗi. Nếu dùng mảng `char tenLoai[20];` thì **không** gán bằng `=` được mà phải dùng `strcpy(tenLoai, "VIP");`.

### Bài 11.

```c
#include <stdio.h>

int main() {
    double a, b;
    char pt;

    printf("Nhap so thu nhat: ");  scanf("%lf", &a);
    printf("Nhap phep toan (+ - * / %%): "); scanf(" %c", &pt);
    printf("Nhap so thu hai : ");  scanf("%lf", &b);

    if (pt == '+') {
        printf("%.4f + %.4f = %.4f\n", a, b, a + b);
    } else if (pt == '-') {
        printf("%.4f - %.4f = %.4f\n", a, b, a - b);
    } else if (pt == '*') {
        printf("%.4f * %.4f = %.4f\n", a, b, a * b);
    } else if (pt == '/') {
        if (b == 0) printf("Loi: khong the chia cho 0!\n");
        else        printf("%.4f / %.4f = %.4f\n", a, b, a / b);
    } else if (pt == '%') {
        if ((int)b == 0) printf("Loi: khong the chia du cho 0!\n");
        else             printf("%d %% %d = %d\n", (int)a, (int)b, (int)a % (int)b);
    } else {
        printf("Phep toan khong hop le!\n");
    }
    return 0;
}
```

⚠️ Toán tử `%` **chỉ áp dụng cho số nguyên** — phải ép `(int)` trước. (Với số thực có hàm `fmod` trong `<math.h>`.)

⚠️ Luôn kiểm tra chia cho 0 trước khi chia, nếu không chương trình sẽ crash (với số nguyên) hoặc cho `inf`/`nan` (với số thực).

⚠️ Dấu cách trong `scanf(" %c", &pt)` rất quan trọng: nó bỏ qua ký tự xuống dòng còn sót lại sau lần nhập số trước. Thiếu dấu cách, `pt` sẽ nhận `'\n'`. Muốn in ký tự `%` bằng `printf` phải viết `%%`.

### Bài 12.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n (1-999): ");
    scanf("%d", &n);

    if (n < 1 || n > 999) {
        printf("Ngoai pham vi!\n");
    } else if (n < 10) {
        printf("%d co 1 chu so\n", n);
    } else if (n < 100) {
        printf("%d co 2 chu so\n", n);
    } else {
        printf("%d co 3 chu so\n", n);
    }
    return 0;
}
```

Cách tổng quát cho số bất kỳ (dùng vòng lặp — chương 4, `abs` trong `<stdlib.h>`):

```c
int demChuSo = 0;
int tam = abs(n);
if (tam == 0) demChuSo = 1;
while (tam > 0) { demChuSo++; tam /= 10; }
```

Hoặc dùng chuỗi: `char buf[20]; int len = sprintf(buf, "%d", n);` — `sprintf` trả về số ký tự đã ghi (tính cả dấu `-` nếu số âm).

### Bài 13.

```c
double d; scanf("%lf", &d);
if (d >= 5.0) printf("Trung binh");       // <- SAI THU TU
else if (d >= 7.0) printf("Kha");
else if (d >= 8.5) printf("Gioi");
```

**Lỗi:** thứ tự các điều kiện bị **ngược**. Với `d = 9.5`:
1. Kiểm tra `9.5 >= 5.0` → **đúng** → in "Trung binh"
2. Vì đã vào nhánh `if`, toàn bộ chuỗi `else if` phía sau **bị bỏ qua**

Điều kiện `d >= 5.0` "nuốt" hết mọi giá trị lớn hơn, nên 2 nhánh sau không bao giờ chạy tới — đó là **mã chết (dead code)**.

**Sửa — xếp từ điều kiện CHẶT NHẤT xuống LỎNG NHẤT:**

```c
if      (d >= 8.5) printf("Gioi");
else if (d >= 7.0) printf("Kha");
else if (d >= 5.0) printf("Trung binh");
else               printf("Yeu");
```

**Quy tắc chung:** với chuỗi `else if` dùng dấu `>=`, xếp mốc **giảm dần**; dùng dấu `<=`, xếp mốc **tăng dần**.

### Bài 14.

**Cách B (`else if`) hiệu quả hơn.**

Với `n = 100`:

| | Cách A (3 `if` riêng) | Cách B (`else if`) |
|---|---|---|
| Số lần kiểm tra | **4 phép so sánh** (`n<10`, `n>=10`, `n<100`, `n>=100`) | **2 phép so sánh** (`n<10` sai, `n<100` sai → vào `else`) |
| Có thể chạy nhiều nhánh | ⚠️ Có (nếu điều kiện chồng lấn) | ❌ Không — chỉ đúng 1 nhánh |
| Điều kiện phải viết đầy đủ | ✅ Phải viết `n >= 10 && n < 100` | ❌ Chỉ cần `n < 100` |

**Sự khác biệt bản chất:**

- **Cách A:** cả 3 điều kiện **đều được kiểm tra**, dù nhánh đầu đã đúng. Nếu các điều kiện chồng lấn, nhiều nhánh có thể cùng chạy — thường là lỗi.
- **Cách B:** khi một nhánh đúng, toàn bộ phần còn lại **bị bỏ qua**. Đảm bảo đúng một nhánh chạy.

Với 3 nhánh thì chênh lệch không đáng kể; nhưng với 50 nhánh thì `else if` tiết kiệm rõ rệt, và quan trọng hơn là **đảm bảo tính loại trừ lẫn nhau**.

✅ **Dùng `if` riêng biệt** chỉ khi các điều kiện **độc lập** và có thể cùng đúng:

```c
if (n % 2 == 0) printf("Chia het 2\n");
if (n % 3 == 0) printf("Chia het 3\n");     // ca hai cung co the in
```

### Bài 15.

```c
#include <stdio.h>

int main() {
    int gio, phut;
    printf("Nhap gio (0-23) va phut: ");
    scanf("%d %d", &gio, &phut);

    if (gio < 0 || gio > 23 || phut < 0 || phut > 59) {
        printf("Thoi gian khong hop le!\n");
        return 1;
    }

    // Xac dinh buoi va loi chao
    const char *buoi, *loiChao;
    if (gio < 5) {
        buoi = "Dem";    loiChao = "Khuya roi, di ngu thoi!";
    } else if (gio < 11) {
        buoi = "Sang";   loiChao = "Chao buoi sang!";
    } else if (gio < 13) {
        buoi = "Trua";   loiChao = "Chao buoi trua!";
    } else if (gio < 18) {
        buoi = "Chieu";  loiChao = "Chao buoi chieu!";
    } else if (gio < 22) {
        buoi = "Toi";    loiChao = "Chao buoi toi!";
    } else {
        buoi = "Dem";    loiChao = "Khuya roi, di ngu thoi!";
    }

    // Doi sang dinh dang 12 gio
    int gio12;
    const char *amPm;
    if (gio == 0)       { gio12 = 12; amPm = "AM"; }   // 0h = 12 AM
    else if (gio < 12)  { gio12 = gio; amPm = "AM"; }
    else if (gio == 12) { gio12 = 12; amPm = "PM"; }   // 12h = 12 PM
    else                { gio12 = gio - 12; amPm = "PM"; }

    printf("\n%s\n", loiChao);
    printf("Gio 24h : %02d:%02d\n", gio, phut);
    printf("Gio 12h : %d:%02d %s\n", gio12, phut, amPm);
    printf("Buoi    : %s\n", buoi);
    return 0;
}
```

Ví dụ nhập `14 30`:

```
Chao buoi chieu!
Gio 24h : 14:30
Gio 12h : 2:30 PM
Buoi    : Chieu
```

💡 `%02d` in số nguyên với độ rộng 2, thiếu thì **thêm số 0 ở đầu**: `5` → `05`. Nhờ vậy `9:5` được in đẹp thành `09:05`.

**2 trường hợp đặc biệt hay sai khi đổi sang 12h:**
- `0:30` → **12:30 AM** (không phải 0:30 AM)
- `12:30` → **12:30 PM** (không phải 0:30 PM)
