# [C]. Chuyển Đổi Giữa Số Và Chuỗi

Để chuyển số thành xâu hay chuyển xâu thành số bạn có thể sử dụng hàm có sẵn hoặc tự cài đặt, bài viết này mình sẽ hướng dẫn các bạn những hàm thông dụng trong việc chuyển đổi số và xâu ký tự trong C.

**NỘI DUNG :** 

- **Chuyển đổi xâu thành số**
- **Chuyển đổi số thành xâu**
- **Video tutorial** 

---

**1. Chuyển Đổi Xâu Thành Số**

Trong quá trình học lập trình đôi khi bạn sẽ cần chuyển đổi xâu ký tự thành một số nguyên hoặc một số thực, thư viện chuẩn của C đã cung cấp sẵn cho bạn các hàm này trong **`<stdlib.h>`** và bạn có thể sử dụng ngay.

Tổng hợp các hàm thông dụng chuyển xâu thành số :

| **Hàm** | **Chức năng** |
|---|---|
| atoi() | Chuyển xâu thành số int |
| atol() | Chuyển xâu thành số long |
| atoll() | Chuyển xâu thành số long long (từ C99) |
| atof() | Chuyển xâu thành số double |
| strtol() | Chuyển xâu thành số long, có báo lỗi và chọn được cơ số |
| strtoll() | Chuyển xâu thành số long long, có báo lỗi và chọn được cơ số |
| strtoul() | Chuyển xâu thành số long không dấu |
| strtoull() | Chuyển xâu thành số long long không dấu |
| strtod() | Chuyển xâu thành số double, có báo lỗi |

Tuy nhiên chủ yếu bạn sử dụng các hàm : **atoi()**, **atoll()**, **atof()** cho trường hợp đơn giản và **strtol()**, **strtod()** khi cần kiểm tra lỗi.

**atoi() : Chuyển xâu thành số int**

Lưu ý khi sử dụng atoi() :

- Hàm bỏ qua các khoảng trắng ở đầu xâu.
- Nếu xâu có thêm chữ cái hoặc ký tự đặc biệt không phải chữ số thì hàm sẽ chuyển đổi tới trước kí tự đặc biệt đó mà thôi.
- Hàm **không báo lỗi**: nếu xâu không bắt đầu bằng số (hoặc xâu rỗng) thì trả về 0, còn nếu giá trị vượt quá giới hạn của int thì kết quả là **hành vi không xác định**. Khi cần kiểm tra lỗi hãy dùng strtol().

Ví dụ :

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *s1 = "282828";
    const char *s2 = "-292828";
    const char *s3 = "2828codelab.dev";
    int n1 = atoi(s1);
    int n2 = atoi(s2);
    int n3 = atoi(s3);
    printf("%d\n", n1);
    printf("%d\n", n2);
    printf("%d\n", n3);
    return 0;
}
```

Output :

```
282828
-292828
2828
```

**atoll() : Chuyển xâu thành số long long**

Ví dụ :

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *s1 = "100000000000000000";
    const char *s2 = "-100000000000000000";
    const char *s3 = "28282828282828codelab.dev";
    long long n1 = atoll(s1);
    long long n2 = atoll(s2);
    long long n3 = atoll(s3);
    printf("%lld\n", n1);
    printf("%lld\n", n2);
    printf("%lld\n", n3);
    return 0;
}
```

Output :

```
100000000000000000
-100000000000000000
28282828282828
```

**atof() và strtod() : Chuyển xâu thành số double**

Lưu ý là mặc dù tên là atof nhưng hàm này trả về kiểu **double**.

Ví dụ :

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *s1 = "100.123";
    const char *s2 = "-100.456";
    const char *s3 = "28282.codelab.dev";
    double n1 = atof(s1);
    double n2 = atof(s2);
    double n3 = strtod(s3, NULL);
    printf("%.3f\n", n1);
    printf("%.3f\n", n2);
    printf("%.3f\n", n3);
    return 0;
}
```

Output :

```
100.123
-100.456
28282.000
```

**strtol() : Chuyển đổi có kiểm tra lỗi**

**Cú pháp :** long strtol(const char *s, char **end, int base);

- s : xâu cần chuyển
- end : địa chỉ một con trỏ, sau khi gọi hàm con trỏ này sẽ trỏ tới **ký tự đầu tiên chưa được đọc**. Có thể truyền NULL nếu không cần
- base : cơ số (2 tới 36, hoặc 0 để tự nhận diện theo tiền tố `0x`, `0`)

Nếu không đọc được chữ số nào thì `end` sẽ trỏ về đầu xâu s. Nếu giá trị vượt quá giới hạn của long thì biến **`errno`** (thư viện `<errno.h>`) được gán bằng `ERANGE`.

Ví dụ :

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(void) {
    const char *s = "2828codelab.dev";
    char *end;
    errno = 0;
    long n = strtol(s, &end, 10);
    if (end == s) {
        printf("Khong phai so\n");
    } else if (errno == ERANGE) {
        printf("So qua lon\n");
    } else {
        printf("So doc duoc : %ld\n", n);
        printf("Phan con lai : %s\n", end);
    }
    printf("%ld\n", strtol("FF", NULL, 16));   // co so 16
    return 0;
}
```

Output :

```
So doc duoc : 2828
Phan con lai : codelab.dev
255
```

Ngoài ra bạn cũng có thể dùng hàm **sscanf()** của `<stdio.h>`: hàm này hoạt động giống scanf nhưng đọc dữ liệu từ một xâu thay vì từ bàn phím, và trả về số biến đọc thành công.

```c
int n;
if (sscanf("  123", "%d", &n) == 1) printf("%d\n", n);   // 123
```

---

**2. Chuyển Đổi Số Thành Xâu**

Hàm **sprintf()** trong C sẽ giúp bạn chuyển đổi số thành xâu. Hàm này hoạt động giống printf nhưng thay vì in ra màn hình thì nó **ghi kết quả vào một mảng char**, vì vậy bạn dùng được mọi đặc tả định dạng quen thuộc như `%d`, `%lld`, `%.2f`...

Nên dùng **snprintf()** (từ C99) thay cho sprintf() vì snprintf() nhận thêm kích thước mảng đích và **không bao giờ ghi vượt** quá kích thước đó.

**Cú pháp :** snprintf(s, kich_thuoc, "dinh dang", cac_gia_tri...);

Ví dụ :

```c
#include <stdio.h>

int main(void) {
    int n = 28282828;
    char s[50];
    snprintf(s, sizeof(s), "%d", n);
    printf("%s\n", s);

    double x = 3.14159;
    char t[50];
    snprintf(t, sizeof(t), "%.2f", x);     // lay 2 chu so thap phan
    printf("%s\n", t);
    return 0;
}
```

Output :

```
28282828
3.14
```

Lưu ý: C không có hàm chuẩn itoa() (một số trình biên dịch có nhưng không phải chuẩn), vì vậy hãy dùng snprintf() để code chạy được ở mọi nơi.

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-04-c-chuyen-doi-giua-so-va-chuoi.md](solutions/09-04-c-chuyen-doi-giua-so-va-chuoi.md)

**Bài 1.** Dùng `snprintf()` chuyển các kiểu `int`, `long long`, `float`, `double`, `char` sang chuỗi và in ra.

**Bài 2.** Dùng `atoi`, `atoll`, `atof`, `strtod` chuyển chuỗi sang số.

**Bài 3.** Xử lý lỗi khi chuỗi không phải số bằng `strtol`: kiểm tra con trỏ `end` và `errno == ERANGE`.

**Bài 4.** Chuyển một số nguyên thành chuỗi **không dùng** `sprintf` (tự viết bằng phép chia lấy dư).

**Bài 5.** Chuyển một chuỗi số thành số nguyên **không dùng** `atoi` (tự viết).

**Bài 6.** Dùng `strtol` với tham số cơ số: chuyển chuỗi nhị phân, bát phân, thập lục phân sang số thập phân.

**Bài 7.** Chuyển một số thập phân sang chuỗi nhị phân, bát phân, thập lục phân.

**Bài 8.** Dùng `sscanf`/`sprintf` để chuyển đổi số ↔ chuỗi. So sánh với `atoi`/`strtol`.

**Bài 9.** Định dạng số thực thành chuỗi với đúng `k` chữ số thập phân.

**Bài 10.** Viết hàm định dạng số tiền có dấu chấm phân cách hàng nghìn: `1234567` → `1.234.567`.

**Bài 11.** Đọc một dòng chứa nhiều số cách nhau bởi dấu cách, chuyển tất cả vào một mảng `int`.

**Bài 12.** Kiểm tra một chuỗi có phải số hợp lệ không (có thể có dấu âm, phần thập phân).

**Bài 13.** Chuyển một chuỗi biểu thức đơn giản `"12+34"` thành 2 số rồi tính tổng.

**Bài 14.** Viết hàm chuyển số thành chữ tiếng Việt: `123` → `mot tram hai muoi ba`.

**Bài 15.** Viết một "thư viện chuyển đổi" với các hàm an toàn: `toInt`, `toDouble`, `toStr`, `isNumber`, `formatMoney`, `toBase`.
