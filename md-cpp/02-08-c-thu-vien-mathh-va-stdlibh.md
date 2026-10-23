# [C]. Thư Viện math.h Và stdlib.h

Trong quá trình lập trình việc sử dụng các hàm toán học là rất phổ biến, ngôn ngữ C cung cấp cho bạn thư viện **math.h** chứa các hàm toán học và thư viện **stdlib.h** chứa nhiều hàm tiện ích như trị tuyệt đối của số nguyên, sinh số ngẫu nhiên... Bài viết này mình sẽ cung cấp cho bạn cách sử dụng và ví dụ minh họa cho các hàm toán học và tiện ích thông dụng, đồng thời hướng dẫn cách tự viết các hàm min, max, swap vốn không có sẵn trong C.

**NỘI DUNG :** 

- **Các Hàm Toán Học Phổ Biến**
- **Thư Viện stdlib.h**
- **Tự Viết Min, Max, Swap** 

---

**1. Các Hàm Toán Học Phổ Biến**

Các hàm toán học trong thư viện **math.h** đều có tham số là một số thuộc kiểu double và có kiểu trả về là double, bạn không cần phải nhớ hết mọi hàm mà chỉ cần nhớ cho mình một vài hàm quan trọng được sử dụng thường xuyên.

| **STT** | **Hàm** | **Chức năng** |
|---|---|---|
| 1 | pow(x, y) | Trả về x^y |
| 2 | sqrt(x) | Trả về căn bậc 2 của x |
| 3 | cbrt(x) | Trả về căn bậc 3 của x |
| 4 | ceil(x) | Trả về số nguyên nhỏ nhất lớn hơn hoặc bằng x, tương đương phép làm tròn lên |
| 5 | floor(x) | Trả về số nguyên lớn nhất nhỏ hơn hoặc bằng x, tương đương phép làm tròn xuống |
| 6 | round(x) | Trả về số nguyên gần x nhất phụ thuộc phần thập phân |
| 7 | fabs(x) | Trả về trị tuyệt đối của số x |
| 8 | exp(x) | Trả về e^x |
| 9 | fmod(x, y) | Trả về số dư khi chia x cho y |
| 10 | log(x) | Trả về logarit tự nhiên của x |
| 11 | log10(x) | Trả về logarit thập phân của x |
| 12 | cos(x) | Trả về giá trị hàm cos với x là radian |
| 13 | sin(x) | Trả về giá trị hàm sin với x là radian |
| 14 | tan(x) | Trả về giá trị hàm tan với x là radian |
| 15 | acos(x) | Trả về giá trị hàm arccos (kết quả tính bằng radian) |
| 16 | asin(x) | Trả về giá trị hàm arcsin (kết quả tính bằng radian) |
| 17 | atan(x) | Trả về giá trị hàm arctan (kết quả tính bằng radian) |

**Lưu ý khi biên dịch :** Trên Linux (gcc), các hàm của **math.h** nằm trong thư viện toán riêng, bạn cần thêm tuỳ chọn **-lm** ở cuối lệnh biên dịch, nếu không có thể gặp lỗi `undefined reference to 'sqrt'` :

```
gcc main.c -o main -lm
```

**Hàm pow(x,y)** : Trả về lũy thừa x^y, lưu ý là hàm này trả về số thực double nên nếu bạn muốn tính lũy thừa với x và y nguyên thì cần lưu kết quả dưới dạng số nguyên hoặc ép kiểu khi in ra.

Ví dụ 1:

```c
#include <stdio.h>
#include <math.h>

int main(){
    int a = 2, b = 10;
    printf("%d^%d = %d\n", a, b, (int)pow(a, b));
    //Tính căn bậc 5
    int n = 100;
    double res = pow(n, 1.0 / 5);
    printf("%.3f\n", res);
    return 0;
}
```

Output :

```
2^10 = 1024
2.512
```

**Hàm sqrt(x)** : Tính căn bậc 2 của x

Ví dụ 2 :

```c
#include <stdio.h>
#include <math.h>

int main(){
    int n = 100;
    int can = (int)sqrt(n);
    printf("%d\n", can);

    double res = sqrt(1000);
    printf("%.2f\n", res);
    return 0;
}
```

Output :

```
10
31.62
```

**Hàm cbrt(x)** : Trả về căn bậc 3 của x

Ví dụ 3 :

```c
#include <stdio.h>
#include <math.h>

int main(){
    int n = 27;
    int can = (int)cbrt(n);
    printf("%d\n", can);

    double res = cbrt(100);
    printf("%.2f\n", res);
    return 0;
}
```

Output :

```
3
4.64
```

**Hàm ceil(x)** : Trả về số nguyên khi làm tròn phần thập phân của x lên, ví dụ x là 2.3 hay 2.8 thì khi sử dụng hàm ceil ta sẽ thu được số 3.

Ví dụ 4 :

```c
#include <stdio.h>
#include <math.h>

int main(){
    double a = 3.14;
    double b = 3.8;
    printf("%d %d\n", (int)ceil(a), (int)ceil(b));
    return 0;
}
```

Output :

```
4 4
```

**Hàm floor(x)** : Trả về số nguyên khi làm tròn phần thập phân của x xuống, ví dụ x là 2.3 hay 2.8 thì khi sử dụng hàm floor ta sẽ thu được số 2.

Ví dụ 5 :

```c
#include <stdio.h>
#include <math.h>

int main(){
    double a = 3.14;
    double b = 3.8;
    printf("%d %d\n", (int)floor(a), (int)floor(b));
    return 0;
}
```

Output :

```
3 3
```

**Hàm round(x)** : Làm tròn dựa vào phần thập phân của x, nếu phần thập phân của x lớn hơn hoặc bằng 0.5 thì sẽ làm tròn lên, ngược lại sẽ làm tròn xuống

Ví dụ 6 :

```c
#include <stdio.h>
#include <math.h>

int main(){
    double a = 3.14;
    double b = 3.8;
    printf("%d %d\n", (int)round(a), (int)round(b));
    return 0;
}
```

Output :

```
3 4
```

**Hàm fabs(x)** : Trả về giá trị tuyệt đối của số thực x. Trong C, trị tuyệt đối của **số thực** phải dùng `fabs`, còn trị tuyệt đối của **số nguyên** dùng `abs` trong thư viện stdlib.h (xem phần 2).

Ví dụ 7 :

```c
#include <stdio.h>
#include <math.h>

int main(){
    printf("%.2f %.2f\n", fabs(3.5), fabs(-2.75));
    return 0;
}
```

Output :

```
3.50 2.75
```

---

**2. Thư Viện stdlib.h**

stdlib.h (standard library) là thư viện chứa nhiều hàm tiện ích chung của C. Hiện tại bạn sẽ làm quen với một vài hàm cơ bản trong thư viện này trước, sau khi học phần mảng và con trỏ thì mình sẽ giới thiệu các hàm khác như `qsort`, `malloc`, `free`.

Khi sử dụng thư viện này bạn cần include vào chương trình của mình: `#include <stdlib.h>`.

**Hàm abs, labs, llabs**

Các hàm này trả về giá trị tuyệt đối của số nguyên. C không hỗ trợ nạp chồng hàm (overload) nên mỗi kiểu dữ liệu có một hàm riêng :

| **Hàm** | **Kiểu tham số** | **Đặc tả in** |
|---|---|---|
| abs(x) | int | %d |
| labs(x) | long | %ld |
| llabs(x) | long long | %lld |

Ví dụ 8 :

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    printf("%d %d\n", abs(10), abs(-100));
    long long x = -9876543210LL;
    printf("%lld\n", llabs(x));
    return 0;
}
```

Output :

```
10 100
9876543210
```

**Chú ý :** Không dùng `abs` cho số thực, ví dụ `abs(-3.9)` sẽ ép tham số về int và trả về 3, muốn lấy trị tuyệt đối số thực hãy dùng `fabs`.

**Hàm rand và srand**

Hàm `rand()` trả về một số nguyên ngẫu nhiên trong đoạn từ 0 tới `RAND_MAX` (một hằng số được định nghĩa trong stdlib.h, tối thiểu là 32767). Để mỗi lần chạy chương trình thu được dãy số khác nhau, bạn gọi `srand(time(NULL))` một lần ở đầu chương trình, hàm `time` nằm trong thư viện **time.h**.

Muốn sinh số ngẫu nhiên trong đoạn [a, b] bạn dùng công thức : `a + rand() % (b - a + 1)`.

Ví dụ 9 :

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(NULL));
    for(int i = 0; i < 5; i++){
        int x = 1 + rand() % 100; // so ngau nhien trong doan [1, 100]
        printf("%d ", x);
    }
    printf("\n");
    return 0;
}
```

Output (mỗi lần chạy sẽ khác nhau) :

```
37 82 5 61 94
```

---

**3. Tự Viết Min, Max, Swap**

C không có sẵn các hàm min, max, swap như một số ngôn ngữ khác, bạn có thể tự viết hàm hoặc dùng macro `#define` (sẽ học kỹ ở bài sau).

**Hoán đổi giá trị 2 biến (swap)**

Cách phổ biến nhất là dùng thêm một biến tạm :

```c
#include <stdio.h>

int main(){
    int a = 100, b = 200;
    int temp = a;
    a = b;
    b = temp;
    printf("%d %d\n", a, b);

    char x = '@', y = '#';
    char tmp = x;
    x = y;
    y = tmp;
    printf("%c %c\n", x, y);
    return 0;
}
```

Output :

```
200 100
# @
```

Nếu muốn viết thành hàm swap thì trong C bạn phải truyền **địa chỉ** của 2 biến (con trỏ), phần này sẽ được giải thích chi tiết ở bài tham trị và con trỏ :

```c
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}
// Goi ham: swap(&a, &b);
```

**Hàm min và max**

Bạn có thể tự viết hàm trả về giá trị nhỏ hơn hoặc lớn hơn trong 2 số, muốn tìm min, max của nhiều số thì gọi lồng nhau.

```c
#include <stdio.h>

int min(int a, int b){
    return a < b ? a : b;
}

int max(int a, int b){
    return a > b ? a : b;
}

int main(){
    int a = 100, b = 200;
    printf("Min(%d, %d) = %d\n", a, b, min(a, b));
    printf("Max(%d, %d) = %d\n", a, b, max(a, b));
    printf("Min(10, 20, 15, 4) = %d\n", min(min(10, 20), min(15, 4)));
    printf("Max(10, 20, 15, 4) = %d\n", max(max(10, 20), max(15, 4)));
    return 0;
}
```

Output :

```
Min(100, 200) = 100
Max(100, 200) = 200
Min(10, 20, 15, 4) = 4
Max(10, 20, 15, 4) = 20
```

Ngoài ra bạn có thể dùng macro để min, max dùng được cho nhiều kiểu dữ liệu (int, double, char...) :

```c
#include <stdio.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))
#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main(){
    printf("%d\n", MIN(100, 200));
    printf("%.1f\n", MAX(2.5, 1.5));
    printf("%c\n", MAX('d', MAX('b', 'z')));
    return 0;
}
```

Output :

```
100
2.5
z
```

**Xem thêm bài giảng của mình về Hàm Toán Học trong C :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-08-c-thu-vien-mathh-va-stdlibh.md](solutions/02-08-c-thu-vien-mathh-va-stdlibh.md)

**Bài 1.** Nhập 2 số `x`, `y`. Tính và in ra `x^y`, `sqrt(x)`, `cbrt(x)`, `log(x)`, `log10(x)` với 4 chữ số thập phân.

**Bài 2.** Nhập một số thực `x`. In ra kết quả của `ceil(x)`, `floor(x)`, `round(x)` và giải thích sự khác nhau của 3 hàm.

**Bài 3.** Nhập 3 cạnh tam giác `a`, `b`, `c`. Dùng công thức Heron tính diện tích tam giác.

**Bài 4.** Nhập toạ độ 2 điểm, tính khoảng cách Euclid bằng `sqrt` và `pow`.

**Bài 5.** Giải phương trình bậc hai `ax² + bx + c = 0`, dùng `sqrt` để tính nghiệm.

**Bài 6.** Nhập một số nguyên `n`. Kiểm tra `n` có phải số chính phương không (dùng `sqrt`). Chú ý xử lý sai số số thực.

**Bài 7.** Chạy đoạn code sau và giải thích vì sao kết quả có thể **sai**:

```c
int n = 25;
int can = sqrt(n);
printf("%d\n", can * can == n);

int m = pow(10, 2);
printf("%d\n", m);
```

**Bài 8.** Nhập góc theo độ, chuyển sang radian rồi tính `sin`, `cos`, `tan` của góc đó.

**Bài 9.** Nhập 3 số nguyên, tự viết hàm `max` và `min` (nhận 2 số) để tìm số lớn nhất và nhỏ nhất trong 3 số.

**Bài 10.** Hoán đổi giá trị 2 biến kiểu `int`, 2 biến kiểu `char`, và 2 phần tử của mảng. Viết thêm hàm `swap(int *a, int *b)` dùng con trỏ.

**Bài 11.** Nhập 4 số, dùng macro `MAX(a, b)` và `MIN(a, b)` lồng nhau để tìm số lớn nhất và nhỏ nhất.

**Bài 12.** So sánh `abs`, `labs`, `llabs` và `fabs`. Viết chương trình minh hoạ sự khác nhau khi dùng với `int`, `long`, `long long`, `double`.

**Bài 13.** Viết chương trình làm tròn một số thực đến `k` chữ số thập phân (ví dụ `3.14159` với `k = 2` → `3.14`) bằng `round`.

**Bài 14.** Nhập số tiền gốc `P`, lãi suất `r` (%/năm), số năm `n`. Tính số tiền nhận được theo công thức lãi kép `A = P(1 + r/100)^n` dùng `pow`.

**Bài 15.** Viết chương trình tính tổng `S = 1 + 1/2 + 1/3 + ... + 1/n` và so sánh với `log(n) + 0.5772` (hằng số Euler–Mascheroni).
