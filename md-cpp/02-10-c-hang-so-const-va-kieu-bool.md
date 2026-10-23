# [C]. Hằng Số const Và Kiểu bool

Trong chương trình có rất nhiều giá trị không bao giờ thay đổi như số PI, số ngày trong tuần, giá trị lớn nhất của một đại lượng... Ngôn ngữ C cung cấp cho bạn các **hằng số (literal)**, từ khóa **const** và chỉ thị **#define** để làm việc với những giá trị này. Bài viết này cũng sẽ giới thiệu kiểu dữ liệu **bool** trong thư viện **stdbool.h** dùng để biểu diễn giá trị đúng/sai.

**NỘI DUNG :**

- **Hằng Số Literal**
- **Từ Khóa const**
- **So Sánh #define Và const**
- **Kiểu bool Và Thư Viện stdbool.h**

---

**1. Hằng Số Literal** 

**Literal** là các giá trị được viết trực tiếp trong mã nguồn, ví dụ `100`, `3.14`, `'A'`, `"codelab"`. Mỗi literal đều có một kiểu dữ liệu xác định, trình biên dịch dựa vào cách viết để biết kiểu của nó.

**Hằng số nguyên** : có thể viết ở 3 hệ cơ số

| **Cách viết** | **Hệ cơ số** | **Ví dụ** | **Giá trị thập phân** |
|---|---|---|---|
| Bình thường | Thập phân (cơ số 10) | 28 | 28 |
| Bắt đầu bằng 0 | Bát phân (cơ số 8) | 034 | 28 |
| Bắt đầu bằng 0x | Thập lục phân (cơ số 16) | 0x1C | 28 |

Bạn có thể thêm **hậu tố** (suffix) để chỉ rõ kiểu của hằng số nguyên :

| **Hậu tố** | **Kiểu** | **Ví dụ** |
|---|---|---|
| Không có | int | 100 |
| U hoặc u | unsigned int | 100U |
| L hoặc l | long | 100L |
| LL hoặc ll | long long | 100LL |
| ULL | unsigned long long | 100ULL |

**Hằng số thực** : mặc định có kiểu **double**, thêm hậu tố **f** để có kiểu **float**. Bạn có thể viết dưới dạng khoa học với chữ **e**, ví dụ `1e9` là 1 x 10^9, `1e-9` là 1 x 10^-9.

**Hằng ký tự** : đặt trong cặp nháy đơn như `'A'`, `'@'`, `'\n'`. Lưu ý trong C hằng ký tự có kiểu **int** (khác với C++ là char).

**Hằng chuỗi** : đặt trong cặp nháy kép như `"codelab"`, là một mảng các ký tự kết thúc bởi ký tự `'\0'`.

**Ví dụ 1:** 

```c
#include <stdio.h>

int main(){
    printf("%d %d %d\n", 28, 034, 0x1C);
    printf("%u\n", 4000000000U);
    printf("%lld\n", 1000000000000000LL);
    printf("%f %f\n", 3.14, 2.5f);
    printf("%.0f %g\n", 1e9, 1e-9);
    printf("%c %d\n", 'A', 'A');
    printf("%s\n", "codelab");
    return 0;
}
```

Output :

```
28 28 28
4000000000
1000000000000000
3.140000 2.500000
1000000000 1e-09
A 65
codelab
```

**Ví dụ 2 :** Dùng toán tử **sizeof** để xem kích thước (byte) của các literal, kết quả của sizeof có kiểu **size_t** và được in bằng `%zu`.

```c
#include <stdio.h>

int main(){
    printf("sizeof(28)   = %zu\n", sizeof(28));
    printf("sizeof(28LL) = %zu\n", sizeof(28LL));
    printf("sizeof(3.14) = %zu\n", sizeof(3.14));
    printf("sizeof(3.14f)= %zu\n", sizeof(3.14f));
    printf("sizeof('A')  = %zu\n", sizeof('A'));
    return 0;
}
```

Output :

```
sizeof(28)   = 4
sizeof(28LL) = 8
sizeof(3.14) = 8
sizeof(3.14f)= 4
sizeof('A')  = 4
```

**Giải thích :** 

- `28` có kiểu int nên chiếm 4 byte, `28LL` có kiểu long long nên chiếm 8 byte
- `3.14` mặc định là double (8 byte), `3.14f` là float (4 byte)
- `'A'` trong C có kiểu int nên chiếm 4 byte chứ không phải 1 byte

**Chú ý** : Kích thước các kiểu có thể khác nhau tuỳ máy và trình biên dịch, kết quả trên là của gcc trên máy 64 bit phổ biến hiện nay.

---

**2. Từ Khóa const** 

Khi thêm từ khóa **const** vào trước kiểu dữ liệu, biến sẽ trở thành **biến chỉ đọc** (read-only) : bạn chỉ được gán giá trị cho nó một lần duy nhất lúc khai báo, sau đó mọi lệnh gán giá trị mới đều bị trình biên dịch báo lỗi.

Cú pháp : const kiểu_dữ_liệu tên_hằng = giá_trị;

Quy ước thông thường là đặt tên hằng bằng chữ **in hoa** để dễ phân biệt với biến thường.

**Ví dụ 1 :** 

```c
#include <stdio.h>

int main(){
    const double PI = 3.14159;
    const int SO_NGAY_TRONG_TUAN = 7;
    double r = 2.0;
    printf("Dien tich hinh tron : %.2f\n", PI * r * r);
    printf("So ngay trong tuan : %d\n", SO_NGAY_TRONG_TUAN);
    return 0;
}
```

Output :

```
Dien tich hinh tron : 12.57
So ngay trong tuan : 7
```

**Ví dụ 2 :** Thử thay đổi giá trị của hằng

```c
const int MAX = 100;
MAX = 200;   // Loi bien dich
```

Trình biên dịch gcc báo lỗi :

```
error: assignment of read-only variable 'MAX'
```

**Chú ý** : Bạn nên khởi tạo giá trị cho hằng ngay khi khai báo. Nếu viết `const int x;` thì trình biên dịch C vẫn chấp nhận nhưng biến x sẽ mang giá trị rác và bạn không thể gán lại cho nó được nữa, nên biến này trở nên vô dụng.

Việc sử dụng hằng thay cho các con số "trơ trọi" (magic number) giúp code dễ đọc hơn và khi cần thay đổi giá trị bạn chỉ cần sửa ở một chỗ duy nhất.

---

**3. So Sánh #define Và const** 

Ở bài trước bạn đã biết **#define** cũng có thể dùng để đặt tên cho giá trị. Vậy khi nào nên dùng #define, khi nào nên dùng const ?

**Ví dụ :** 

```c
#include <stdio.h>

#define PI_DEFINE 3.14159
#define N 5

const double PI_CONST = 3.14159;

int a[N];   // Dung : N la hang so bien dich

int main(){
    double r = 1.5;
    printf("%.4f\n", PI_DEFINE * r * r);
    printf("%.4f\n", PI_CONST * r * r);
    for(int i = 0; i < N; i++){
        a[i] = i * i;
        printf("%d ", a[i]);
    }
    return 0;
}
```

Output :

```
7.0686
7.0686
0 1 4 9 16
```

| **#define** | **const** |
|---|---|
| Được xử lý bởi preprocessor, thay thế văn bản trước khi biên dịch | Được xử lý bởi compiler, là một biến chỉ đọc |
| Không có kiểu dữ liệu, không được kiểm tra kiểu | Có kiểu dữ liệu rõ ràng, được kiểm tra kiểu |
| Có hiệu lực từ chỗ định nghĩa tới cuối file | Tuân theo phạm vi (scope) như biến thường |
| Là hằng số biên dịch : dùng được làm kích thước mảng toàn cục, nhãn case của switch | Trong C **không** phải hằng số biên dịch : không dùng làm kích thước mảng toàn cục hay nhãn case được |
| Không xem được giá trị khi debug | Xem được giá trị khi debug |

Nếu bạn viết `const int M = 5;` rồi khai báo mảng toàn cục `int b[M];` thì gcc sẽ báo lỗi `variably modified 'b' at file scope`. Vì vậy trong C :

- Dùng **const** cho các giá trị có kiểu cụ thể như số thực, số nguyên dùng trong tính toán
- Dùng **#define** (hoặc **enum**) khi cần hằng số biên dịch như kích thước mảng, nhãn case

---

**4. Kiểu bool Và Thư Viện stdbool.h**

Kiểu **bool** dùng để lưu giá trị logic : đúng (**true**) hoặc sai (**false**). Khác với nhiều ngôn ngữ khác, ở phiên bản đầu tiên C không có kiểu bool, người ta dùng số nguyên với quy ước **0 là sai, khác 0 là đúng**.

Từ chuẩn C99, C có kiểu **_Bool** và thư viện **stdbool.h** định nghĩa sẵn :

- `bool` là tên khác của `_Bool`
- `true` có giá trị là 1
- `false` có giá trị là 0

Vì vậy muốn dùng `bool`, `true`, `false` bạn cần `#include <stdbool.h>`.

**Ví dụ 1 :** 

```c
#include <stdio.h>
#include <stdbool.h>

int main(){
    bool a = true;
    bool b = false;
    printf("a = %d, b = %d\n", a, b);
    printf("sizeof(bool) = %zu\n", sizeof(bool));
    bool c = 10 > 5;
    bool d = 10 == 5;
    printf("c = %d, d = %d\n", c, d);
    printf("%s\n", c ? "true" : "false");
    return 0;
}
```

Output :

```
a = 1, b = 0
sizeof(bool) = 1
c = 1, d = 0
true
```

**Giải thích :** 

- printf không có đặc tả riêng cho bool, bạn in bằng `%d` sẽ được 1 hoặc 0
- Muốn in ra chữ "true"/"false" bạn dùng toán tử 3 ngôi như dòng cuối
- Các toán tử so sánh (`>`, `==`, ...) và logic (`&&`, `||`, `!`) trong C trả về giá trị **int** là 1 hoặc 0, có thể gán thẳng vào biến bool

**Ví dụ 2 :** Chuyển giá trị khác sang bool

```c
#include <stdio.h>
#include <stdbool.h>

int main(){
    bool x = 100;
    bool y = -5;
    bool z = 0;
    bool t = 0.5;
    printf("%d %d %d %d\n", x, y, z, t);
    return 0;
}
```

Output :

```
1 1 0 1
```

**Giải thích :** Khi gán một giá trị vào biến bool, mọi giá trị **khác 0** (kể cả số âm, số thực như 0.5) đều trở thành **1 (true)**, chỉ có giá trị **0** mới trở thành **0 (false)**. Đây là điểm khác biệt với kiểu int : `int t = 0.5;` sẽ cho t bằng 0.

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-10-c-hang-so-const-va-kieu-bool.md](solutions/02-10-c-hang-so-const-va-kieu-bool.md)

**Bài 1.** In ra giá trị thập phân của các hằng số `255`, `0377`, `0xFF`, `0x7FFFFFFF` bằng `printf("%d")`. Giải thích vì sao 3 hằng đầu bằng nhau.

**Bài 2.** Dùng `sizeof` in ra kích thước của các literal: `28`, `28L`, `28LL`, `28U`, `3.14`, `3.14f`, `'A'`, `"abc"`. Giải thích vì sao `sizeof('A')` là 4 và `sizeof("abc")` là 4.

**Bài 3.** Khai báo `const int MAX = 100;` rồi thử gán `MAX = 200;`. Ghi lại thông báo lỗi của gcc và giải thích.

**Bài 4.** Khai báo `const int x;` (không khởi tạo) rồi in ra. Biên dịch có lỗi không? Giải thích vì sao nên khởi tạo hằng ngay khi khai báo.

**Bài 5.** Nhập bán kính `r`, dùng `const double PI = 3.14159` tính chu vi và diện tích hình tròn, in với 2 chữ số thập phân.

**Bài 6.** Khai báo mảng toàn cục với kích thước là `#define N 5`, sau đó thử lại với `const int M = 5;`. Ghi lại lỗi và giải thích sự khác nhau.

**Bài 7.** Nhập nhiệt độ độ C, đổi sang độ F theo công thức `F = C * 9 / 5 + 32`, trong đó `9.0 / 5` và `32` được khai báo bằng các hằng `const` có tên rõ nghĩa.

**Bài 8.** Nhập 2 số nguyên `a`, `b`. Lưu kết quả của `a > b`, `a == b`, `a != b` vào 3 biến `bool` và in ra cả dạng số (`1/0`) và dạng chữ (`true/false`).

**Bài 9.** Nhập một số nguyên `n`, lưu vào biến `bool laChan` kết quả kiểm tra `n` chẵn, `bool laDuong` kết quả kiểm tra `n > 0`. In ra 2 kết quả.

**Bài 10.** In ra giá trị của các biến bool sau và giải thích: `bool a = 256;`, `bool b = -1;`, `bool c = 0.0001;`, `bool d = '0';`, `bool e = '\0';`.

**Bài 11.** Viết hàm `bool laNamNhuan(int nam)` trả về `true` nếu năm nhuận. Nhập một năm và in kết quả. (Năm nhuận: chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100.)

**Bài 12.** Viết chương trình dùng kiểu `_Bool` mà **không** include `stdbool.h`, tự định nghĩa `TRUE`, `FALSE` bằng `#define`. So sánh với cách dùng `stdbool.h`.

**Bài 13.** Chạy đoạn code sau và giải thích vì sao `a` và `c` cho kết quả khác nhau dù cùng được gán 256:

```c
bool a = 256;
unsigned char c = 256;
printf("%d %d\n", a, c);
```

**Bài 14.** Nhập số km đi taxi. Giá mở cửa `10000` đồng (cho km đầu tiên) và giá mỗi km tiếp theo `12000` đồng được khai báo bằng `const`. Tính số tiền phải trả (giả sử số km ≥ 1).

**Bài 15.** Tìm và sửa tất cả lỗi trong đoạn code sau:

```c
#include <stdio.h>
const int SIZE = 3;
int a[SIZE];
int main(){
    const double TI_LE = 0.1;
    TI_LE = 0.2;
    bool ok = true;
    printf("%d %f\n", ok, TI_LE);
    return 0;
}
```
