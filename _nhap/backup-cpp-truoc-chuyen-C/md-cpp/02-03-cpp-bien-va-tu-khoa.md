# [C++]. Biến Và Từ Khóa

Trong bài học trước bạn đã học về kiểu dữ liệu trong C++, bài học này bạn sẽ học cách khai báo biến để lưu trữ giá trị trong bài toán của mình

**NỘI DUNG :** 

- **Khai Báo Biến** 
- **Các Quy Tắc Đặt Tên Biến**
- **Keywords** 
- **Video Tutorial**

---

**1. Khai Báo Biến**

Biến (variable) được sử dụng để lưu trữ giá trị cho bài toán của các bạn, ví dụ khi bài toán cho bạn chiều dài, chiều rộng của một hình chữ nhật bạn có thể khai báo 2 biến tương ứng để lưu lại giá trị này. Hầu như mọi chương trình của các bạn đều sử dụng đến các biến

Để hiển thị giá trị của biến ra màn hình bạn sử dụng cout tương tự như in ra giá trị của đoạn text mà đã học ở bài trước.

**Các chú ý khi khai báo biến :** 

- Kiểu dữ liệu của biến đó là gì ? Ví dụ : **int**,** long long**,** float**,** double**...
- Tên biến mà bạn muốn đặt cho nó là gì ? Ví dụ : chuVi, dienTich, salary, point...
- Giá trị mà bạn muốn khởi tạo cho nó là gì?
- Nếu bạn khai báo biến mà không khởi tạo giá trị thì nó sẽ có giá trị ngẫu nhiên

Cú pháp đặt tên biến : **[Kiểu dữ liệu] [Tên biến]**;

Ví dụ 1 : Khai báo biến và khởi tạo

```cpp
#include "iostream"

using namespace std;

int main(){
    int a = 28;
    long long b = 282828282828282;
    float c = 3.8912;
    double d = 10.8912781;
    char kitu = '@';
    bool check = true;
    cout << "Gia tri cua a : " << a << endl;
    cout << "Gia tri cua b : " << b << endl;
    cout << "Gia tri cua c : " << c << endl;
    cout << "Gia tri cua d : " << d << endl;
    cout << "Gia tri cua kitu : " << kitu << endl;
    cout << "Gia tri cua check : " << check << endl;
}
```

Output :

```cpp
Gia tri cua a : 28
Gia tri cua b : 282828282828282
Gia tri cua c : 3.8912
Gia tri cua d : 10.8913
Gia tri cua kitu : @
Gia tri cua check : 1
```

Ví dụ 2 : Bạn có thể khai báo các biến có cùng kiểu dữ liệu ở trên cùng 1 dòng

```cpp
#include "iostream"

using namespace std;

int main(){
    int a = 10, b = 20, c = 30;
    char x = '@', y = '#', z = '$';
    cout << a << ' ' << b << ' ' << c << endl;
    cout << x << ' ' << y << ' ' << z << endl;
    return 0;
}
```

Output :

```cpp
10 20 30
@ # $
```

---

**2. Các Quy Tắc Đặt Tên Biến**

C++ cũng như các ngôn ngữ lập trình khác cung cấp cho bạn bộ quy tắc để đặt tên biến sao cho hợp lệ, bạn có thể đặt tên biến Tiếng Anh, Tiếng Việt không dấu hay dài ngắn tùy bạn. Tuy nhiên nên đặt tên biến ngắn gọn, xúc tích và có thể hiện được ý nghĩa giá trị mà nó đang lưu trữ.

Các quy tắc :

| **Quy tắc** | **Ví dụ về cách đặt tên biến sai** |
| Tên biến không được bắt đầu bằng chữ số | codelab, 29tech, 300bankinh... |
| Tên biến không được chứa dấu cách hoặc các ký tự đặc biệt | ban kinh, ban#kinh, ban$kinh... |
| Tên biến không được trùng với các keyword có sẵn trong C++ | using, int, char, cout.... |
| Không được đặt 2 biến cùng tên, kể cả chúng khác kiểu dữ liệu | int a; float a; |
| Tên biến trong C có phân biệt chữ hoa và chữ thường | tech28 và Tech28 là 2 biến khác nhau |

Khi đặt tên biến nên đặt có ý nghĩa và tránh đặt tên biến quá dài, trong C++ thì không có quy chuẩn về cách đặt tên biến nào cả, bạn có thể lựa chọn đặt tên biến theo cách viết hoa chữ cái đầu của từng từ ví dụ **BanKinh**,** ChuVi**,** DienTich**,** ChieuRong**, hoặc các từ viết cách nhau một dấu gạch dưới ví dụ** ban_kinh**,** chu_vi**,** dien_tich**...

---

**3. Keywords**

Keywords - Từ khóa được định nghĩa sẵn trong ngôn ngữ lập trình C++, bạn sẽ gặp rất nhiều từ khóa như : cout, cin, int, float, using, for, while, try...

Ngày trước khi mình bắt đầu học lập trình thì mình cũng cố gắng học thuộc các keywords này nhưng sau rồi mới thấy việc học thuộc là không cần thiết, vì khi bạn học các kiến thức mới thì tự khắc bạn sẽ bắt gặp những từ khóa ở phần kiến thức đó

Bảng sau liệt kê các từ khóa trong ngôn ngữ lập trình C++

| **A-C** | **D-P** | **R-Z** |
| alignas (C++11)
alignof (C++11)
and
and_eq
asm
atomic_cancel
atomic_commit
atomic_noexcept
auto
bitand
bitor
bool
break
case
catch
char
char8_t (C++20)
char16_t (C++11)
char32_t (C++11)
class
compl
concept (C++20)
const
consteval (C++20)
constexpr (C++11)
constinit (C++20)
const_cast
continue
co_await (C++20)
co_return (C++20)
co_yield (C++20) | ecltype (C++11)
default
delete
do
double
dynamic_cast
else
enum
explicit
export
extern
false
float
for
friend
goto
if
inline
int
long
mutable
namespace
new
noexcept (C++11)
not
not_eq
nullptr (C++11)
operator
or
or_eq
private
protected
public | reflexpr (reflection TS)
register (2)
reinterpret_cast
requires (C++20)
return
short
signed
sizeof (1)
static
static_assert (C++11)
static_cast
struct (1)
switch
synchronized (TM TS)
template
this (4)
thread_local (C++11)
throw
true
try
typedef
typeid
typename
union
unsigned
using (1)
virtual
void
volatile
wchar_t
while
xor
xor_eq |

---

**Video hướng dẫn Kiểu Dữ Liệu và Biến trong C++ :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-03-cpp-bien-va-tu-khoa.md](solutions/02-03-cpp-bien-va-tu-khoa.md)

**Bài 1.** Khai báo và khởi tạo 5 biến lưu thông tin về một hình chữ nhật: chiều dài, chiều rộng, chu vi, diện tích, tên hình. In tất cả ra màn hình.

**Bài 2.** Trong các tên biến sau, tên nào **hợp lệ**, tên nào **không hợp lệ**? Giải thích từng trường hợp:

```
banKinh    2ban_kinh   ban kinh   _temp     int
Diem       diem-tb     $money     so1       class
tongSo     TONG_SO     ho&ten     __x       cout
```

**Bài 3.** Viết chương trình khai báo 2 biến `tech28` và `Tech28` với 2 giá trị khác nhau, in cả hai ra để chứng minh C++ phân biệt hoa thường.

**Bài 4.** Chương trình sau có lỗi gì? Hãy sửa lại:

```cpp
int main(){
    int a = 5;
    float a = 3.14;
    cout << a;
    return 0;
}
```

**Bài 5.** Viết chương trình khai báo 4 biến `a`, `b`, `c`, `d` kiểu `int` trên cùng một dòng với các giá trị lần lượt 10, 20, 30, 40, rồi in ra tổng của chúng.

**Bài 6.** Viết chương trình hoán đổi giá trị 2 biến `a` và `b` bằng cách dùng biến trung gian. In giá trị trước và sau khi hoán đổi.

**Bài 7.** Hoán đổi 2 biến `a`, `b` mà **không dùng** biến trung gian (dùng phép cộng trừ).

**Bài 8.** Viết chương trình nhập vào bán kính hình tròn, khai báo hằng số `PI = 3.14159`, tính và in ra chu vi và diện tích.

**Bài 9.** Tìm hiểu từ khoá `const`. Khai báo một biến `const` rồi thử gán lại giá trị cho nó. Chép lại thông báo lỗi.

**Bài 10.** Đặt lại tên các biến sau cho có ý nghĩa và đúng quy ước camelCase:

```cpp
int a;      // so luong hoc sinh
double x;   // diem trung binh
char k;     // xep loai
bool t;     // da nop hoc phi chua
int n1;     // tong so tien thu duoc
```

**Bài 11.** Viết cùng một chương trình 2 lần: lần 1 đặt tên biến theo kiểu `camelCase`, lần 2 theo kiểu `snake_case`. So sánh và cho biết bạn thích kiểu nào.

**Bài 12.** Tra bảng từ khoá trong bài học và cho biết các từ sau có phải keyword không: `main`, `cout`, `string`, `vector`, `true`, `nullptr`, `endl`, `size`.

**Bài 13.** Viết chương trình khai báo biến toàn cục và biến cục bộ cùng tên, in ra cả hai (gợi ý: dùng `::` để truy cập biến toàn cục).

**Bài 14.** Viết chương trình lưu thông tin một cuốn sách (tên, tác giả, số trang, giá, còn hàng hay không) bằng các biến có kiểu và tên phù hợp, rồi in ra dạng hoá đơn.

**Bài 15.** Tìm hiểu về phạm vi (scope) của biến. Dự đoán output của chương trình sau rồi chạy để kiểm chứng:

```cpp
#include <iostream>
using namespace std;

int main(){
    int x = 10;
    {
        int x = 20;
        cout << x << endl;
    }
    cout << x << endl;
    return 0;
}
```
