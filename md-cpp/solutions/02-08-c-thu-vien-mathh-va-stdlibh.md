# Lời giải — [C]. Thư Viện math.h Và stdlib.h

[← Quay lại bài học](../02-08-c-thu-vien-mathh-va-stdlibh.md)

> **Ghi chú về biên dịch:** các hàm của `<math.h>` nằm trong thư viện toán `libm`. Với gcc trên Linux, luôn thêm `-lm` ở **cuối** lệnh: `gcc bai1.c -o bai1 -lm`. Thiếu nó có thể gặp lỗi `undefined reference to 'pow'`.

---

### Bài 1.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double x, y;
    printf("Nhap x va y: ");
    scanf("%lf %lf", &x, &y);

    printf("x^y      = %.4f\n", pow(x, y));
    printf("sqrt(x)  = %.4f\n", sqrt(x));
    printf("cbrt(x)  = %.4f\n", cbrt(x));
    printf("log(x)   = %.4f\n", log(x));     // logarit tu nhien (co so e)
    printf("log10(x) = %.4f\n", log10(x));   // logarit co so 10
    return 0;
}
```

Ví dụ `x = 8, y = 3`:

```
x^y      = 512.0000
sqrt(x)  = 2.8284
cbrt(x)  = 2.0000
log(x)   = 2.0794
log10(x) = 0.9031
```

⚠️ `sqrt` và `log` với tham số âm cho `NaN` (Not a Number, `printf` in ra `nan` hoặc `-nan`); `log(0)` cho `-inf`.

⚠️ Khi **nhập** `double` bằng `scanf` phải dùng `%lf`; khi **in** bằng `printf` thì `%f` hay `%lf` đều được.

### Bài 2.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double x;
    printf("Nhap so thuc: ");
    scanf("%lf", &x);

    printf("ceil(%g)  = %g\n", x, ceil(x));
    printf("floor(%g) = %g\n", x, floor(x));
    printf("round(%g) = %g\n", x, round(x));
    return 0;
}
```

💡 `%g` in số thực ở dạng gọn nhất (bỏ các số 0 thừa sau dấu chấm), tiện để in `3` thay vì `3.000000`.

**Bảng so sánh:**

| x | `ceil` (làm tròn lên) | `floor` (làm tròn xuống) | `round` (làm tròn gần nhất) | `(int)x` (cắt bỏ) |
|---|---|---|---|---|
| 2.3 | 3 | 2 | 2 | 2 |
| 2.5 | 3 | 2 | **3** | 2 |
| 2.8 | 3 | 2 | 3 | 2 |
| −2.3 | **−2** | **−3** | −2 | **−2** |
| −2.5 | −2 | −3 | **−3** | −2 |
| −2.8 | −2 | −3 | −3 | −2 |

**Điểm mấu chốt:**
- `ceil` luôn đi về phía **+∞**, `floor` luôn về phía **−∞**
- `round` làm tròn về số nguyên gần nhất, `.5` thì làm tròn **ra xa 0**
- `(int)` **cắt bỏ phần thập phân**, tức luôn đi về phía **0** — khác `floor` với số âm!

⚠️ Bẫy hay gặp: nhiều người tưởng `(int)x` = `floor(x)`, nhưng `(int)(-2.3)` = `-2` còn `floor(-2.3)` = `-3`.

### Bài 3.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c;
    printf("Nhap 3 canh tam giac: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    // Kiem tra dieu kien ton tai tam giac
    if (a <= 0 || b <= 0 || c <= 0 ||
        a + b <= c || a + c <= b || b + c <= a) {
        printf("Khong phai tam giac hop le!\n");
        return 1;
    }

    double p = (a + b + c) / 2;                         // nua chu vi
    double S = sqrt(p * (p - a) * (p - b) * (p - c));   // cong thuc Heron

    printf("Nua chu vi = %.4f\n", p);
    printf("Dien tich  = %.4f\n", S);
    return 0;
}
```

Ví dụ `3 4 5`:

```
Nua chu vi = 6.0000
Dien tich  = 6.0000
```

### Bài 4.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double x1, y1, x2, y2;
    printf("Nhap toa do diem A (x y): ");
    scanf("%lf %lf", &x1, &y1);
    printf("Nhap toa do diem B (x y): ");
    scanf("%lf %lf", &x2, &y2);

    double kc = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    printf("Khoang cach AB = %.4f\n", kc);
    return 0;
}
```

💡 **Mẹo hiệu năng:** `pow(x, 2)` chậm hơn nhiều so với `x * x`, vì `pow` là hàm tổng quát. Với luỹ thừa nhỏ, luôn viết trực tiếp:

```c
double dx = x2 - x1, dy = y2 - y1;
double kc = sqrt(dx * dx + dy * dy);      // nhanh hon va chinh xac hon
```

Từ C99, `<math.h>` còn có `hypot(dx, dy)` — tính đúng cả khi `dx`, `dy` rất lớn/rất nhỏ (tránh tràn số).

### Bài 5.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double a, b, c;
    printf("Giai ax^2 + bx + c = 0\n");
    printf("Nhap a, b, c: ");
    scanf("%lf %lf %lf", &a, &b, &c);

    const double EPS = 1e-9;

    if (fabs(a) < EPS) {                       // suy bien thanh bac nhat
        if (fabs(b) < EPS) {
            printf("%s\n", fabs(c) < EPS ? "Vo so nghiem" : "Vo nghiem");
        } else {
            printf("Nghiem duy nhat: x = %.4f\n", -c / b);
        }
        return 0;
    }

    double delta = b * b - 4 * a * c;

    if (delta < -EPS) {
        printf("Vo nghiem thuc (delta = %.4f < 0)\n", delta);
    } else if (fabs(delta) < EPS) {
        printf("Nghiem kep: x = %.4f\n", -b / (2 * a));
    } else {
        double canDelta = sqrt(delta);
        printf("x1 = %.4f\n", (-b + canDelta) / (2 * a));
        printf("x2 = %.4f\n", (-b - canDelta) / (2 * a));
    }
    return 0;
}
```

Kiểm thử:

| a | b | c | Kết quả |
|---|---|---|---|
| 1 | −3 | 2 | x1 = 2, x2 = 1 |
| 1 | −2 | 1 | Nghiệm kép x = 1 |
| 1 | 0 | 1 | Vô nghiệm thực |
| 0 | 2 | −4 | x = 2 |

### Bài 6.

```c
#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("%d khong phai so chinh phuong\n", n);
        return 0;
    }

    // Cong 0.5 truoc khi ep kieu de tranh sai so lam tron cua sqrt
    int can = (int)(sqrt((double)n) + 0.5);

    if ((long long)can * can == n) {
        printf("%d LA so chinh phuong (= %d^2)\n", n, can);
    } else {
        printf("%d KHONG phai so chinh phuong\n", n);
    }
    return 0;
}
```

**Vì sao phải `+ 0.5`:** `sqrt` trả về `double` có sai số. Với `n = 25`, máy có thể tính ra `4.999999999999999` thay vì `5.0`. Ép `(int)` sẽ **cắt bỏ** thành 4 → kết luận sai.

Cách viết an toàn tuyệt đối (không dùng số thực để kết luận):

```c
int can = (int)sqrt((double)n);
// Thu ca 3 gia tri lan can de chac chan
for (int k = (can > 0 ? can - 1 : 0); k <= can + 1; k++) {
    if ((long long)k * k == n) { /* la so chinh phuong */ }
}
```

### Bài 7.

```c
#include <stdio.h>
#include <math.h>

int main() {
    int n = 25;
    int can = sqrt(n);
    printf("%d\n", can * can == n);      // co the ra 0 thay vi 1!

    int m = pow(10, 2);
    printf("%d\n", m);                   // co the ra 99 thay vi 100!
    return 0;
}
```

**Giải thích — cả 2 dòng đều là bẫy nổi tiếng:**

**① `sqrt` trả về `double` có sai số.** Nếu tính `sqrt(25)` ra `4.999999999999999`, thì gán vào `int` sẽ cắt thành **4**, và `4*4 = 16 ≠ 25` → in ra `0`.

**② `pow(10, 2)` cũng trả về `double`.** Nếu kết quả là `99.99999999999999`, gán sang `int` cho **99**.

Trên máy hiện đại, hai ví dụ cụ thể này thường vẫn ra đúng (compiler tối ưu thành hằng số), nhưng với số lớn hơn thì **rất dễ sai**:

```c
printf("%lld\n", (long long)pow(10, 15));      // co the ra 999999999999999
```

✅ **Quy tắc: không dùng `pow` cho luỹ thừa số nguyên.** Tự viết hàm:

```c
long long luyThua(long long a, int n) {
    long long kq = 1;
    for (int i = 0; i < n; i++) kq *= a;
    return kq;
}
```

Hoặc dùng luỹ thừa nhanh (binary exponentiation) khi `n` lớn:

```c
long long luyThuaNhanh(long long a, long long n) {
    long long kq = 1;
    while (n > 0) {
        if (n & 1) kq *= a;
        a *= a;
        n >>= 1;
    }
    return kq;
}
```

### Bài 8.

```c
#include <stdio.h>
#include <math.h>

int main() {
    const double PI = acos(-1.0);      // cach lay PI chinh xac nhat

    double gocDo;
    printf("Nhap goc (do): ");
    scanf("%lf", &gocDo);

    double gocRad = gocDo * PI / 180.0;

    printf("Goc radian = %.6f\n", gocRad);
    printf("sin        = %.6f\n", sin(gocRad));
    printf("cos        = %.6f\n", cos(gocRad));
    printf("tan        = %.6f\n", tan(gocRad));
    return 0;
}
```

Ví dụ `goc = 30`:

```
Goc radian = 0.523599
sin        = 0.500000
cos        = 0.866025
tan        = 0.577350
```

⚠️ **Mọi hàm lượng giác trong C nhận tham số là RADIAN**, không phải độ. Công thức đổi: `rad = do × π / 180`.

⚠️ `tan(90°)` không cho "vô cùng" mà cho một số rất lớn (khoảng 1,6×10¹⁶), do `PI/2` không biểu diễn chính xác được.

💡 Nhiều trình biên dịch có sẵn hằng `M_PI` trong `<math.h>`, nhưng đó **không phải** chuẩn C11 (bị ẩn khi biên dịch với `-std=c11`), nên `acos(-1.0)` là cách an toàn hơn.

### Bài 9.

```c
#include <stdio.h>

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int main() {
    int a, b, c;
    printf("Nhap 3 so: ");
    scanf("%d %d %d", &a, &b, &c);

    printf("Lon nhat  = %d\n", max(a, max(b, c)));
    printf("Nho nhat  = %d\n", min(a, min(b, c)));
    return 0;
}
```

⚠️ **Bẫy kiểu dữ liệu:** C không hỗ trợ nạp chồng hàm, nên hàm `max(int, int)` ở trên **chỉ dành cho `int`**. Nếu truyền `long long` hoặc `double` vào, giá trị sẽ bị ép về `int` một cách âm thầm:

```c
long long x = 10000000000LL, y = 5;
max(x, y);                  // SAI: x bi cat ve int
// Can viet ham rieng cho long long:
long long maxLL(long long a, long long b) { return a > b ? a : b; }
```

### Bài 10.

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    // 1. Hoan doi 2 so nguyen bang bien tam
    int x = 10, y = 20;
    int t = x; x = y; y = t;
    printf("int    : %d %d\n", x, y);        // 20 10

    // 2. Hoan doi 2 ky tu
    char c1 = 'A', c2 = 'Z';
    char tc = c1; c1 = c2; c2 = tc;
    printf("char   : %c %c\n", c1, c2);      // Z A

    // 3. Hoan doi 2 phan tu cua mang bang ham swap
    int a[5] = {1, 2, 3, 4, 5};
    swap(&a[0], &a[4]);
    printf("mang   : ");
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);   // 5 2 3 4 1
    printf("\n");

    // 4. Dung ham swap voi 2 bien
    swap(&x, &y);
    printf("swap() : %d %d\n", x, y);        // 10 20
    return 0;
}
```

**Vì sao hàm `swap` phải nhận con trỏ:** C truyền tham số theo **giá trị** (tham trị). Nếu viết `void swap(int a, int b)`, hàm chỉ đổi 2 bản sao, biến gốc không thay đổi. Truyền địa chỉ `&x`, `&y` thì hàm mới sửa được biến gốc qua `*a`, `*b`.

💡 Hàm `swap` trên chỉ dùng cho `int`. Muốn đổi 2 chuỗi (mảng char) thì dùng mảng tạm và `strcpy` trong `<string.h>`.

### Bài 11.

```c
#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int main() {
    int a, b, c, d;
    printf("Nhap 4 so: ");
    scanf("%d %d %d %d", &a, &b, &c, &d);

    printf("Lon nhat = %d\n", MAX(MAX(a, b), MAX(c, d)));
    printf("Nho nhat = %d\n", MIN(MIN(a, b), MIN(c, d)));
    return 0;
}
```

**Macro `MAX(a, b)`** được bộ tiền xử lý thay thế thành biểu thức `((a) > (b) ? (a) : (b))` trước khi biên dịch, nên dùng được với mọi kiểu số (`int`, `double`, `char`...).

⚠️ Luôn bọc từng tham số và cả biểu thức trong ngoặc. Và **không** truyền biểu thức có tác dụng phụ như `MAX(i++, j)` vì `i++` có thể bị tính 2 lần.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>    // abs, labs, llabs cho so nguyen
#include <math.h>      // fabs cho so thuc

int main() {
    int       i = -42;
    long      l = -1234567890L;
    long long ll = -9876543210LL;
    double    d = -3.14159;

    printf("abs(int)      : %d\n", abs(i));        // 42
    printf("labs(long)    : %ld\n", labs(l));      // 1234567890
    printf("llabs(ll)     : %lld\n", llabs(ll));   // 9876543210
    printf("fabs(double)  : %f\n", fabs(d));       // 3.141590

    // BAY: dung abs voi so thuc, tham so bi ep ve int
    printf("abs(-3.9) sai : %d\n", abs((int)-3.9));  // 3
    return 0;
}
```

| Hàm | Thư viện | Dùng cho | Ghi chú |
|---|---|---|---|
| `abs` | `<stdlib.h>` | `int` | Cắt số thực về `int` nếu lỡ truyền số thực |
| `labs` | `<stdlib.h>` | `long` | In bằng `%ld` |
| `llabs` | `<stdlib.h>` | `long long` | In bằng `%lld` |
| `fabs` | `<math.h>` | `double` | **Luôn dùng cái này cho số thực** |

⚠️ **Bẫy kinh điển:** trong C, `abs(-3.9)` trả về **3** chứ không phải 3.9, vì tham số bị ép về `int`. gcc chỉ cảnh báo khi bật `-Wextra` (cảnh báo `-Wabsolute-value`), dễ bị bỏ qua. (Ví dụ trên ép `(int)` tường minh để minh hoạ mà không gây cảnh báo.)

✅ **Quy tắc:** C không có nạp chồng hàm nên phải chọn đúng hàm theo kiểu: `abs` cho `int`, `labs` cho `long`, `llabs` cho `long long`, `fabs` cho `double`.

### Bài 13.

```c
#include <stdio.h>
#include <math.h>

// Lam tron x den k chu so thap phan
double lamTron(double x, int k) {
    double heSo = pow(10, k);
    return round(x * heSo) / heSo;
}

int main() {
    double x;
    int k;
    printf("Nhap so thuc va so chu so thap phan: ");
    scanf("%lf %d", &x, &k);

    printf("Goc          : %.*f\n", k + 4, x);
    printf("Sau lam tron : %.*f\n", k + 4, lamTron(x, k));
    return 0;
}
```

Ví dụ `3.14159` và `k = 2`:

```
Goc          : 3.141590
Sau lam tron : 3.140000
```

💡 `%.*f` cho phép truyền số chữ số thập phân bằng một tham số `int` (ở đây là `k + 4`) đặt trước giá trị cần in.

**Nguyên lý:** nhân lên `10^k` → làm tròn về số nguyên → chia lại `10^k`.

```
3.14159 × 100 = 314.159
round(314.159) = 314
314 / 100 = 3.14
```

⚠️ Lưu ý phân biệt hai việc:
- **`%.2f`** chỉ thay đổi **cách hiển thị**, giá trị trong biến không đổi.
- **Hàm `lamTron` trên** thực sự **thay đổi giá trị** của số.

Nếu chỉ cần in đẹp thì dùng `%.2f`, đừng làm tròn thật (sẽ tích luỹ sai số qua các phép tính).

### Bài 14.

```c
#include <stdio.h>
#include <math.h>

int main() {
    double P, r;
    int n;

    printf("Nhap so tien goc (VND): ");  scanf("%lf", &P);
    printf("Nhap lai suat (%%/nam) : ");  scanf("%lf", &r);
    printf("Nhap so nam           : ");  scanf("%d", &n);

    double A = P * pow(1 + r / 100.0, n);

    printf("\n--- KET QUA ---\n");
    printf("So tien goc    : %.0f VND\n", P);
    printf("So tien nhan   : %.0f VND\n", A);
    printf("Tien lai       : %.0f VND\n", A - P);

    // Bang chi tiet tung nam
    printf("\nChi tiet tung nam:\n");
    for (int i = 1; i <= n; i++) {
        printf("  Nam %2d: %15.0f VND\n", i, P * pow(1 + r / 100.0, i));
    }
    return 0;
}
```

Ví dụ: `P = 100000000`, `r = 7`, `n = 5`

```
--- KET QUA ---
So tien goc    : 100000000 VND
So tien nhan   : 140255173 VND
Tien lai       : 40255173 VND

Chi tiet tung nam:
  Nam  1:       107000000 VND
  Nam  2:       114490000 VND
  Nam  3:       122504300 VND
  Nam  4:       131079601 VND
  Nam  5:       140255173 VND
```

💡 `%2d`, `%15.0f` canh phải số trong độ rộng 2 và 15 ký tự. Muốn in ký tự `%` trong `printf` phải viết `%%`.

⚠️ **Lưu ý `r / 100.0`** — phải có `.0`, nếu viết `r / 100` mà `r` là `int` thì sẽ bị chia nguyên và lãi suất 7% thành 0%.

### Bài 15.

```c
#include <stdio.h>
#include <math.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    double S = 0;
    for (int i = 1; i <= n; i++) {
        S += 1.0 / i;              // 1.0 chu khong phai 1 - de khong bi chia nguyen!
    }

    const double GAMMA = 0.5772156649;    // hang so Euler-Mascheroni
    double xapXi = log(n) + GAMMA;

    printf("S (tinh that)  = %.10f\n", S);
    printf("log(n) + gamma = %.10f\n", xapXi);
    printf("Sai lech       = %.10f\n", fabs(S - xapXi));
    return 0;
}
```

Ví dụ `n = 1000`:

```
S (tinh that)  = 7.4854708606
log(n) + gamma = 7.4849709439
Sai lech       = 0.0004999167
```

**Kiến thức toán học:** tổng `S = 1 + 1/2 + ... + 1/n` gọi là **chuỗi điều hoà** (harmonic series). Nó **phân kỳ** (tăng vô hạn khi n → ∞) nhưng tăng cực chậm, xấp xỉ `ln(n) + γ` với γ ≈ 0,5772. Sai lệch giảm dần khi `n` lớn (tỉ lệ `1/(2n)`).

⚠️ **Lỗi phổ biến nhất ở bài này:** viết `S += 1 / i;`. Vì `1` và `i` đều là `int`, phép chia là chia nguyên và cho **0** với mọi `i > 1` → kết quả luôn bằng 1. Phải viết `1.0 / i`.
