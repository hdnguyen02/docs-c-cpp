# [C]. Chương Trình Hello World

Hello World là chương trình đơn giản nhất mà một lập trình viên khi học các ngôn ngữ lập trình mới đều từng viết. Mục đích của chương trình này giúp bạn có thể biết được cấu trúc của một chương trình trong ngôn ngữ mà bạn đang học, bài viết này mình cũng giải thích chi tiết cho bạn những phần của một chương trình trong C

**NỘI DUNG :** 

- **Chương Trình Hello World**
- **Hàm Printf Và Ký Tự Xuống Dòng Trong C** 
- **Câu Lệnh Return 0**

---

**1. Chương Trình Hello World** 

Bạn có thể code lại theo mã nguồn dưới đây, lưu vào file có đuôi `.c` (ví dụ `hello.c`) và thử chạy chương trình này trong công cụ mà bạn sử dụng

```c
#include <stdio.h>

int main(){
    printf("Hello World !\n");
    printf("codelab tutorial !\n");
    return 0;
}
```

Output :

```
Hello World !
codelab tutorial !
```

Cấu trúc của một chương trình C gồm 2 phần chính như sau :

- **Thư viện** 

Trong chương trình trên thì câu lệnh `#include <stdio.h>` chính là câu lệnh bổ sung thư viện cần thiết vào chương trình của bạn, có thể hiểu đơn giản thì chương trình của bạn cần liên kết thêm với các thư viện có sẵn. Các thư viện có sẵn sẽ cung cấp cho bạn các công cụ như nhập, xuất, các hàm toán học, xử lý chuỗi ...

Ở đây thư viện mà bạn thêm vào chương trình của mình là thư viện `stdio.h` (**st**andar**d** **i**nput **o**utput - nhập xuất chuẩn), đây là thư viện hỗ trợ nhập dữ liệu từ bàn phím và hiển thị dữ liệu ra màn hình, hầu hết các chương trình của bạn đều cần có thư viện này. File có đuôi `.h` được gọi là **file header**.

Ví dụ hàm `printf` bạn sử dụng để in ra nội dung text trong hàm main của bạn thuộc thư viện `stdio.h` nên bạn cần thêm thư viện này vào chương trình của mình để có thể sử dụng được nó. Nếu quên dòng `#include <stdio.h>`, trình biên dịch sẽ báo lỗi hoặc cảnh báo `implicit declaration of function 'printf'`.

Lưu ý : khác với C++, ngôn ngữ C **không có namespace**, vì vậy trong C không có câu lệnh `using namespace std;`, các hàm của thư viện như `printf`, `scanf` được dùng trực tiếp sau khi `#include`.

- **Hàm main** 

Hàm main là nơi chứa các câu lệnh trong chương trình của bạn, các câu lệnh trong C được kết thúc bởi dấu ; tương tự như đa số các ngôn ngữ lập trình khác. Đây là nơi chương trình của bạn bắt đầu được thực thi, nếu không có hàm main thì chương trình sẽ không thể chạy được.

Bạn cũng sẽ thường thấy hàm main được viết là `int main(void)`, cách viết này nói rõ hàm main không nhận tham số nào, trong các chương trình ở khoá học này thì `int main()` và `int main(void)` dùng như nhau.

---

**2. Hàm Printf Và Ký Tự Xuống Dòng Trong C** 

**Printf** 

`printf` trong C là hàm thuộc thư viện `stdio.h` được sử dụng để hiển thị nội dung ra màn hình. Trong chương trình Hello World thì bạn có thể in ra dòng chữ bất kỳ lên màn hình bằng cách sử dụng printf, nội dung đoạn text bạn muốn in ra màn hình được đặt trong dấu nháy kép `" "` và đặt trong cặp ngoặc tròn của hàm printf.

Ở cuối đoạn text trong câu lệnh printf nếu bạn muốn kết thúc và sang một dòng mới ở nội dung sau thì bạn thêm ký tự "\n", đây là ký tự giúp bạn ngắt dòng. Khác với một số ngôn ngữ khác, printf **không tự động xuống dòng**, nếu bạn không thêm "\n" thì nội dung của lần printf sau sẽ được in tiếp ngay trên cùng dòng. Tổng quát thì bạn có thể xuống dòng bất cứ vị trí nào trong đoạn text chỉ cần thêm ký tự này vào vị trí bạn muốn xuống dòng

Ví dụ 1:

```c
#include <stdio.h>

int main(){
    printf("Hello\nWorld !\n");
    printf("codelab\ntutorial !\nC\nJava\n");
    return 0;
}
```

Output :

```
Hello
World !
codelab
tutorial !
C
Java
```

Bạn có thể dùng nhiều câu lệnh printf liên tiếp để in nối tiếp nhiều đoạn text trên cùng một dòng, vì printf không tự xuống dòng. Ngoài ra printf còn có thể in các đoạn text thông qua **đặc tả** `%s` : mỗi `%s` trong chuỗi định dạng sẽ được thay bằng một đoạn text truyền vào phía sau, cách nhau bởi dấu phẩy. Bạn sẽ học kỹ về các đặc tả của printf trong bài [nhập xuất với scanf và printf](02-05-c-nhap-xuat-voi-scanf-va-printf.md).

Ví dụ 2:

```c
#include <stdio.h>

int main(){
    printf("Text1");
    printf(" @ ");
    printf("Text 2");
    printf("-Text3.codelab!\n");
    printf("%s @ %s-%s.%s\n", "Text1", "Text 2", "Text3", "codelab!");
    return 0;
}
```

Output :

```
Text1 @ Text 2-Text3.codelab!
Text1 @ Text 2-Text3.codelab!
```

**Hàm puts** 

Thư viện `stdio.h` còn có hàm `puts` dùng để in một đoạn text ra màn hình, điểm khác biệt là puts **tự động xuống dòng** sau khi in xong, nên bạn không cần thêm "\n" ở cuối. Hàm puts chỉ in được đúng một đoạn text, không dùng được các đặc tả như `%s` giống printf.

Ví dụ 3 :

```c
#include <stdio.h>

int main(){
    puts("Hello");
    puts("codelab");
    printf("@\n");
    puts("C tutorial");
    return 0;
}
```

Output :

```
Hello
codelab
@
C tutorial
```

---

**3. Câu Lệnh Return 0**

Câu lệnh return 0; trong các chương trình đơn giản trên được đặt ở vị trí cuối cùng trong hàm main, đây là giá trị trả về của hàm main sau khi thực thi xong chương trình nếu chương trình hoạt động một cách chính xác.

Đôi khi những lỗi phát sinh trong chương trình của bạn lúc thực thi sẽ làm chương trình của bạn trả về giá trị khác 0, đó cũng là một cách để kiểm chứng rằng chương trình của bạn có phát sinh lỗi trong quá trình thực thi hay không.

Bạn cũng có thể trả về giá trị khác 0 tuy nhiên thông thường mọi người hay trả về giá trị 0, ví dụ bạn có thể trả về giá trị 1.

Bạn có thể thử copy mã nguồn sau và sẽ thấy rằng chương trình của bạn phát sinh lỗi lúc chạy dẫn tới giá trị trả về của hàm main sẽ là 3221225725 (khi chạy trên Windows, trên Linux chương trình sẽ báo lỗi `Segmentation fault`)

```c
#include <stdio.h>

int main(){
    printf("hello codelab !\n");
    int tech[1000000000];
    tech[0] = 1;
    printf("%d\n", tech[0]);
    return 0;
}
```

Đừng lo việc bạn không thể hiểu những câu lệnh trên hay không hiểu vì sao nó sẽ gây ra lỗi, sau này bạn sẽ biết lý do còn thời điểm hiện tại mình chỉ cho các bạn các chương trình minh họa để hiểu rõ hơn câu lệnh return 0; thường được dùng ở cuối chương trình.

Chú ý rằng khi câu lệnh return 0; trong hàm main được thực thi, chương trình của bạn sẽ kết thúc ngay lập tức

Bạn thử chạy chương trình sau đây và sẽ thấy rằng khi câu lệnh return 0; được thực thi thì các câu lệnh bên dưới của nó sẽ không được thực thi vì chương trình của bạn đã kết thúc ngay tại thời điểm đó rồi.

```c
#include <stdio.h>

int main(){
    printf("hello codelab !\n");
    return 0;
    printf("C tutorial !\n");
    return 0;
}
```

Output :

```
hello codelab !
```

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-01-c-chuong-trinh-hello-world.md](solutions/02-01-c-chuong-trinh-hello-world.md)

**Bài 1.** Viết chương trình in ra màn hình dòng chữ `Xin chao, toi dang hoc C`.

**Bài 2.** Viết chương trình in ra 3 dòng sau, mỗi dòng dùng **một** câu lệnh `printf` riêng:

```
Ho ten: Nguyen Van A
Lop: 12A1
So thich: Lap trinh
```

**Bài 3.** Làm lại bài 2 nhưng chỉ dùng **duy nhất một** câu lệnh `printf` (dùng `\n` để xuống dòng).

**Bài 4.** Viết chương trình in ra hình chữ nhật bằng dấu `*` có kích thước 5 dòng × 10 cột.

**Bài 5.** In ra tam giác vuông bằng dấu `*` như sau (không dùng vòng lặp):

```
*
**
***
****
*****
```

**Bài 6.** Viết chương trình in ra chữ cái `C` khổ lớn bằng dấu `#`, cao 7 dòng.

**Bài 7.** Viết lại chương trình Hello World chỉ dùng hàm `puts` thay cho `printf`. Chương trình có cần thêm `\n` nữa không?

**Bài 8.** In ra màn hình dòng chữ có chứa dấu nháy kép: `Toi thich ngon ngu "C" nhat.`

**Bài 9.** In ra đường dẫn thư mục sau (chú ý dấu `\`): `C:\Users\Admin\Documents\c`

**Bài 10.** In ra bảng sau, dùng ký tự tab `\t` để căn cột:

```
STT	Ten		Diem
1	An		9.5
2	Binh	8.0
3	Chi		7.5
```

**Bài 11.** Cho chương trình dưới đây, hãy dự đoán output **trước khi chạy**, rồi chạy để kiểm tra:

```c
#include <stdio.h>

int main(){
    printf("A\n");
    return 0;
    printf("B\n");
    return 0;
}
```

**Bài 12.** Chương trình sau có 4 lỗi. Hãy tìm và sửa tất cả:

```c
int main(){
    Printf("Hello World")
    return 0
}
```

**Bài 13.** Viết chương trình có `return 1;` thay vì `return 0;`. Sau khi chạy, dùng lệnh terminal để in ra mã thoát (exit code) của chương trình và xác nhận nó bằng 1.

**Bài 14.** So sánh `printf` và `puts`. Viết một chương trình dùng cả hai và giải thích bằng comment sự khác nhau của chúng.

**Bài 15.** Viết chương trình in ra "danh thiếp" của bạn trong một khung như sau (nội dung tự thay):

```
+----------------------------+
|                            |
|      NGUYEN VAN A          |
|      C Developer           |
|      nguyenvana@mail.com   |
|                            |
+----------------------------+
```
