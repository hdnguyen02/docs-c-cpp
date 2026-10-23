# [C]. Biến Và Từ Khóa

Trong bài học trước bạn đã học về kiểu dữ liệu trong C, bài học này bạn sẽ học cách khai báo biến để lưu trữ giá trị trong bài toán của mình

**NỘI DUNG :** 

- **Khai Báo Biến** 
- **Các Quy Tắc Đặt Tên Biến**
- **Keywords** 
- **Video Tutorial**

---

**1. Khai Báo Biến**

Biến (variable) được sử dụng để lưu trữ giá trị cho bài toán của các bạn, ví dụ khi bài toán cho bạn chiều dài, chiều rộng của một hình chữ nhật bạn có thể khai báo 2 biến tương ứng để lưu lại giá trị này. Hầu như mọi chương trình của các bạn đều sử dụng đến các biến

Để hiển thị giá trị của biến ra màn hình bạn sử dụng printf tương tự như in ra đoạn text mà đã học ở bài trước, tuy nhiên trong chuỗi định dạng bạn cần đặt một **đặc tả** tương ứng với kiểu dữ liệu của biến tại vị trí muốn in giá trị, sau đó truyền biến vào phía sau, ngăn cách bởi dấu phẩy. Một số đặc tả thường dùng :

| **Kiểu dữ liệu** | **Đặc tả** |
|---|---|
| int | %d |
| long long | %lld |
| float, double | %f |
| char | %c |
| bool | %d (in ra 1 hoặc 0) |

Bạn sẽ học kỹ về các đặc tả này trong bài [nhập xuất với scanf và printf](02-05-c-nhap-xuat-voi-scanf-va-printf.md).

**Các chú ý khi khai báo biến :** 

- Kiểu dữ liệu của biến đó là gì ? Ví dụ : **int**, **long long**, **float**, **double**...
- Tên biến mà bạn muốn đặt cho nó là gì ? Ví dụ : chuVi, dienTich, salary, point...
- Giá trị mà bạn muốn khởi tạo cho nó là gì?
- Nếu bạn khai báo biến (bên trong hàm) mà không khởi tạo giá trị thì nó sẽ có giá trị ngẫu nhiên

Cú pháp khai báo biến : **[Kiểu dữ liệu] [Tên biến]**;

Ví dụ 1 : Khai báo biến và khởi tạo

```c
#include <stdio.h>
#include <stdbool.h>

int main(){
    int a = 28;
    long long b = 282828282828282;
    float c = 3.8912;
    double d = 10.8912781;
    char kitu = '@';
    bool check = true;
    printf("Gia tri cua a : %d\n", a);
    printf("Gia tri cua b : %lld\n", b);
    printf("Gia tri cua c : %f\n", c);
    printf("Gia tri cua d : %f\n", d);
    printf("Gia tri cua kitu : %c\n", kitu);
    printf("Gia tri cua check : %d\n", check);
    return 0;
}
```

Output :

```
Gia tri cua a : 28
Gia tri cua b : 282828282828282
Gia tri cua c : 3.891200
Gia tri cua d : 10.891278
Gia tri cua kitu : @
Gia tri cua check : 1
```

Đặc tả `%f` mặc định in ra 6 chữ số sau dấu phẩy (làm tròn), vì thế giá trị của d được in ra là 10.891278. Kiểu `bool` cần thư viện `<stdbool.h>` và khi in bằng `%d` giá trị true sẽ hiển thị là 1.

Ví dụ 2 : Bạn có thể khai báo các biến có cùng kiểu dữ liệu ở trên cùng 1 dòng

```c
#include <stdio.h>

int main(){
    int a = 10, b = 20, c = 30;
    char x = '@', y = '#', z = '$';
    printf("%d %d %d\n", a, b, c);
    printf("%c %c %c\n", x, y, z);
    return 0;
}
```

Output :

```
10 20 30
@ # $
```

---

**2. Các Quy Tắc Đặt Tên Biến**

C cũng như các ngôn ngữ lập trình khác cung cấp cho bạn bộ quy tắc để đặt tên biến sao cho hợp lệ, bạn có thể đặt tên biến Tiếng Anh, Tiếng Việt không dấu hay dài ngắn tùy bạn. Tuy nhiên nên đặt tên biến ngắn gọn, xúc tích và có thể hiện được ý nghĩa giá trị mà nó đang lưu trữ.

Các quy tắc :

| **Quy tắc** | **Ví dụ về cách đặt tên biến sai** |
|---|---|
| Tên biến không được bắt đầu bằng chữ số | 28abc, 29tech, 300bankinh... |
| Tên biến không được chứa dấu cách hoặc các ký tự đặc biệt | ban kinh, ban#kinh, ban$kinh... |
| Tên biến không được trùng với các keyword có sẵn trong C | int, char, for, return.... |
| Không được đặt 2 biến cùng tên trong cùng một phạm vi, kể cả chúng khác kiểu dữ liệu | int a; float a; |
| Tên biến trong C có phân biệt chữ hoa và chữ thường | tech28 và Tech28 là 2 biến khác nhau |

Tên biến chỉ được gồm các chữ cái, chữ số và dấu gạch dưới `_`. Ngoài ra bạn cũng nên tránh đặt tên biến trùng với tên các hàm có sẵn của thư viện như `printf`, `scanf`, `sqrt`... vì dù không phải keyword nhưng điều đó sẽ gây nhầm lẫn và lỗi khó hiểu.

Khi đặt tên biến nên đặt có ý nghĩa và tránh đặt tên biến quá dài, trong C thì không có quy chuẩn về cách đặt tên biến nào cả, bạn có thể lựa chọn đặt tên biến theo cách viết hoa chữ cái đầu của từng từ ví dụ **BanKinh**, **ChuVi**, **DienTich**, **ChieuRong**, hoặc các từ viết cách nhau một dấu gạch dưới ví dụ **ban_kinh**, **chu_vi**, **dien_tich**...

---

**3. Keywords**

Keywords - Từ khóa được định nghĩa sẵn trong ngôn ngữ lập trình C, bạn sẽ gặp rất nhiều từ khóa như : int, float, char, if, else, for, while, return...

Ngày trước khi mình bắt đầu học lập trình thì mình cũng cố gắng học thuộc các keywords này nhưng sau rồi mới thấy việc học thuộc là không cần thiết, vì khi bạn học các kiến thức mới thì tự khắc bạn sẽ bắt gặp những từ khóa ở phần kiến thức đó

Chú ý rằng `printf`, `scanf`, `main` **không phải từ khoá**, đó là tên hàm. So với C++ thì C có ít từ khoá hơn rất nhiều. Bảng sau liệt kê các từ khóa trong ngôn ngữ lập trình C theo chuẩn C11

| **A-E** | **F-R** | **S-Z và từ khoá bắt đầu bằng _** |
|---|---|---|
| auto<br>break<br>case<br>char<br>const<br>continue<br>default<br>do<br>double<br>else<br>enum<br>extern | float<br>for<br>goto<br>if<br>inline (C99)<br>int<br>long<br>register<br>restrict (C99)<br>return | short<br>signed<br>sizeof<br>static<br>struct<br>switch<br>typedef<br>union<br>unsigned<br>void<br>volatile<br>while<br>_Alignas (C11)<br>_Alignof (C11)<br>_Atomic (C11)<br>_Bool (C99)<br>_Complex (C99)<br>_Generic (C11)<br>_Imaginary (C99)<br>_Noreturn (C11)<br>_Static_assert (C11)<br>_Thread_local (C11) |

Các từ `bool`, `true`, `false` bạn dùng ở bài trước trong chuẩn C11 không phải là từ khoá mà được định nghĩa trong thư viện `<stdbool.h>` (từ chuẩn C23 chúng mới trở thành từ khoá).

---

**Video hướng dẫn Kiểu Dữ Liệu và Biến trong C :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-03-c-bien-va-tu-khoa.md](solutions/02-03-c-bien-va-tu-khoa.md)

**Bài 1.** Khai báo và khởi tạo 5 biến lưu thông tin về một hình chữ nhật: chiều dài, chiều rộng, chu vi, diện tích, tên hình (một ký tự). In tất cả ra màn hình.

**Bài 2.** Trong các tên biến sau, tên nào **hợp lệ**, tên nào **không hợp lệ**? Giải thích từng trường hợp:

```
banKinh    2ban_kinh   ban kinh   _temp     int
Diem       diem-tb     $money     so1       struct
tongSo     TONG_SO     ho&ten     __x       printf
```

**Bài 3.** Viết chương trình khai báo 2 biến `tech28` và `Tech28` với 2 giá trị khác nhau, in cả hai ra để chứng minh C phân biệt hoa thường.

**Bài 4.** Chương trình sau có lỗi gì? Hãy sửa lại:

```c
int main(){
    int a = 5;
    float a = 3.14;
    printf("%d", a);
    return 0;
}
```

**Bài 5.** Viết chương trình khai báo 4 biến `a`, `b`, `c`, `d` kiểu `int` trên cùng một dòng với các giá trị lần lượt 10, 20, 30, 40, rồi in ra tổng của chúng.

**Bài 6.** Viết chương trình hoán đổi giá trị 2 biến `a` và `b` bằng cách dùng biến trung gian. In giá trị trước và sau khi hoán đổi.

**Bài 7.** Hoán đổi 2 biến `a`, `b` mà **không dùng** biến trung gian (dùng phép cộng trừ).

**Bài 8.** Viết chương trình nhập vào bán kính hình tròn (dùng `scanf`), khai báo hằng số `PI = 3.14159`, tính và in ra chu vi và diện tích.

**Bài 9.** Tìm hiểu từ khoá `const`. Khai báo một biến `const` rồi thử gán lại giá trị cho nó. Chép lại thông báo lỗi.

**Bài 10.** Đặt lại tên các biến sau cho có ý nghĩa và đúng quy ước camelCase:

```c
int a;      // so luong hoc sinh
double x;   // diem trung binh
char k;     // xep loai
bool t;     // da nop hoc phi chua
int n1;     // tong so tien thu duoc
```

**Bài 11.** Viết cùng một chương trình 2 lần: lần 1 đặt tên biến theo kiểu `camelCase`, lần 2 theo kiểu `snake_case`. So sánh và cho biết bạn thích kiểu nào.

**Bài 12.** Tra bảng từ khoá trong bài học và cho biết các từ sau có phải keyword của C11 không: `main`, `printf`, `bool`, `_Bool`, `true`, `sizeof`, `NULL`, `size`.

**Bài 13.** Viết chương trình khai báo biến toàn cục và biến cục bộ cùng tên, in ra cả hai. (Gợi ý: C không có toán tử `::` như C++, hãy tìm hiểu cách dùng khai báo `extern` trong một khối lệnh.)

**Bài 14.** Viết chương trình lưu thông tin một cuốn sách (tên, tác giả, số trang, giá, còn hàng hay không) bằng các biến có kiểu và tên phù hợp, rồi in ra dạng hoá đơn. (Gợi ý: tên sách, tác giả lưu bằng mảng ký tự `char tenSach[] = "...";` và in bằng `%s`.)

**Bài 15.** Tìm hiểu về phạm vi (scope) của biến. Dự đoán output của chương trình sau rồi chạy để kiểm chứng:

```c
#include <stdio.h>

int main(){
    int x = 10;
    {
        int x = 20;
        printf("%d\n", x);
    }
    printf("%d\n", x);
    return 0;
}
```
