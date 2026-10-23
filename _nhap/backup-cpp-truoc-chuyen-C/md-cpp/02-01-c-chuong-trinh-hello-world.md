# [C++]. Chương Trình Hello World

Hello World là chương trình đơn giản nhất mà một lập trình viên khi học các ngôn ngữ lập trình mới đều từng viết. Mục đích của chương trình này giúp bạn có thể biết được cấu trúc của một chương trình trong ngôn ngữ mà bạn đang học, bài viết này mình cũng giải thích chi tiết cho bạn những phần của một chương trình trong C++

**NỘI DUNG :** 

- **Chương Trình Hello World**
- **Cout Và Endl Trong C++** 
- **Câu Lệnh Return 0**

---

**1. Chương Trình Hello World** 

Bạn có thể code lại theo mã nguồn dưới đây và thử chạy chương trình này trong công cụ mà bạn sử dụng

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "Hello World !\n";
    cout << "codelab tutorial !" << endl;
    return 0;
}
```

Output :

```cpp
Hello World !
codelab tutorial !
```

Cấu trúc của một chương trình C++ gồm 3 phần chính như sau :

- **Thư viện** 

Trong chương trình trên thì câu lệnh #include "iostream" chính là câu lệnh bổ sung thư viện cần thiết vào chương trình của bạn, có thể hiểu đơn giản thì chương trình của bạn cần liên kết thêm với các thư viện có sẵn. Các thư viện có sẵn sẽ cung cấp cho bạn các công cụ như nhập, xuất, các hàm, thuật toán ...

Ở đây thư viện mà bạn thêm vào chương trình của mình là thư viện "iostream", đây là thư viện hỗ trợ nhập dữ liệu từ bàn phím và hiển thị dữ liệu ra màn hình, hầu hết các chương trình của bạn đều cần có thư viện này.

Ví dụ đối tượng cout bạn sử dụng để in ra nội dung text trong chương trình main của bạn thuộc thư viện nên bạn cần thêm thư viện này vào chương trình của mình để có thể sử dụng được nó.

- **Namespace** 

Namespace tạm dịch là không gian tên cung cấp không gian nơi chúng ta có thể định nghĩa hoặc khai báo mã định danh, tức là biến, hàm, lớp... Ví dụ như cout, endl, cin đều được định nghĩa trong namespace có tên là std. Khi bạn sử dụng câu lệnh using namespace std; ở đầu chương trình thì bạn sẽ có thể sử dụng cout thay vì phải khai báo là std::cout

Tương tự thì nếu không có câu lệnh này thì bạn sử dụng cout sẽ báo lỗi.

Nếu bạn không sử dụng câu lệnh thì bạn cần sử dụng cout và endl như sau :

```cpp
#include "iostream"

int main(){
    std::cout << "Hello codelab !\n";
    std::cout << "C++ tutorial" << std::endl;
    return 0;
}
```

- **Hàm main** 

Hàm main là nơi chứa các câu lệnh trong chương trình của bạn, các câu lệnh trong C++ được kết thúc bởi dấu ; tương tự như đa số các ngôn ngữ lập trình khác. Đây là nơi chương trình của bạn bắt đầu được thực thi, nếu không có hàm main thì chương trình sẽ không thể chạy được.

---

**2. Cout Và Endl Trong C++** 

**Cout** 

cout trong C++ là đối tượng thuộc thư viện được sử dụng để hiển thị nội dung ra màn hình. Trong chương trình Hello World thì bạn có thể in ra dòng chữ bất kỳ lên màn hình bằng cách sử dụng cout, nội dung đoạn text bạn muốn in ra màn hình được đặt trong dấu nháy kép, nếu nội dung có 1 ký tự bạn có thể dùng nháy đơn cũng được.

Ở cuối đoạn text trong câu lệnh cout nếu bạn muốn kết thúc và sang một dòng mới ở nội dung sau thì bạn thêm ký tự "\n", đây là ký tự giúp bạn ngắt dòng. Tổng quát thì bạn có thể xuống dòng bất cứ vị trí nào trong đoạn text chỉ cần thêm ký tự này vào vị trí bạn muốn xuống dòng

Ví dụ 1:

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "Hello\nWorld !\n";
    cout << "codelab\ntutorial !\nC++\nJava\n";
    return 0;
}
```

Output :

```cpp
Hello
World !
codelab
tutorial !
C++
Java
```

Bạn có thể sử dụng một cout để in ra nhiều đoạn text, mỗi đoạn text cần có 2 ký tự << trước nó.

Ví dụ 2:

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "Text1" << " @ " << "Text 2" << "-" << "Text3" << "." << "codelab!\n";
    return 0;
}
```

Output :

```cpp
Text1 @ Text 2-Text3.codelab!
```

**Endl** 

endl có chức năng tương tự như ký tự ngắt dòng ở trên, khi gặp đối tượng này thì cout sẽ kết thúc dòng và in ra ở một dòng mới. Muốn sử dụng endl thì bạn cũng cần thêm thư viện và namespace

Ví dụ 3 :

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "Hello" << endl << "codelab" << endl;
    cout << "@" << endl << "C++ tutorial" << endl;
    return 0;
}
```

Output :

```cpp
Hello
codelab
@
C++ tutorial
```

---

**3. Câu Lệnh Return 0**

Câu lệnh return 0; trong 2 chương trình đơn giản trên được đặt ở vị trí cuối cùng trong hàm main, đây là giá trị trả về của hàm main sau khi thực thi xong chương trình nếu chương trình hoạt động một cách chính xác.

Đôi khi những lỗi phát sinh trong chương trình của bạn lúc thực thi sẽ làm chương trình của bạn trả về giá trị khác 0, đó cũng là một cách để kiểm chứng rằng chương trình của bạn có phát sinh lỗi trong quá trình thực thi hay không.

Bạn cũng có thể trả về giá trị khác 0 tuy nhiên thông thường mọi người hay trả về giá trị 0, ví dụ bạn có thể trả về giá trị 1.

Bạn có thể thử copy mã nguồn sau và sẽ thấy rằng chương trình của bạn phát sinh lỗi lúc chạy dẫn tới giá trị trả về của hàm main sẽ là 3221225725

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "hello codelab !\n";
    int tech[1000000000];
    return 0;
}
```

Đừng lo việc bạn không thể hiểu những câu lệnh trên hay không hiểu vì sao nó sẽ gây ra lỗi, sau này bạn sẽ biết lý do còn thời điểm hiện tại mình chỉ cho các bạn các chương trình minh họa để hiểu rõ hơn câu lệnh return 0; thường được dùng ở cuối chương trình.

Chú ý rằng khi câu lệnh return 0; được thực thi, chương trình của bạn sẽ kết thúc ngay lập tức

Bạn thử chạy chương trình sau đây và sẽ thấy rằng khi câu lệnh return 0; được thực thi thì các câu lệnh bên dưới của nó sẽ không được thực thi vì chương trình của bạn đã kết thúc ngay tại thời điểm đó rồi.

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "hello codelab !\n";
    return 0;
    cout << "C++ tutorial !\n";
    return 0;
}
```

Output :

```cpp
hello codelab !
```

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-01-c-chuong-trinh-hello-world.md](solutions/02-01-c-chuong-trinh-hello-world.md)

**Bài 1.** Viết chương trình in ra màn hình dòng chữ `Xin chao, toi dang hoc C++`.

**Bài 2.** Viết chương trình in ra 3 dòng sau, mỗi dòng dùng **một** câu lệnh `cout` riêng:

```
Ho ten: Nguyen Van A
Lop: 12A1
So thich: Lap trinh
```

**Bài 3.** Làm lại bài 2 nhưng chỉ dùng **duy nhất một** câu lệnh `cout` (dùng `\n` để xuống dòng).

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

**Bài 7.** Viết lại chương trình Hello World **không dùng** `using namespace std;`.

**Bài 8.** In ra màn hình dòng chữ có chứa dấu nháy kép: `Toi thich ngon ngu "C++" nhat.`

**Bài 9.** In ra đường dẫn thư mục sau (chú ý dấu `\`): `C:\Users\Admin\Documents\cpp`

**Bài 10.** In ra bảng sau, dùng ký tự tab `\t` để căn cột:

```
STT	Ten		Diem
1	An		9.5
2	Binh	8.0
3	Chi		7.5
```

**Bài 11.** Cho chương trình dưới đây, hãy dự đoán output **trước khi chạy**, rồi chạy để kiểm tra:

```cpp
#include <iostream>
using namespace std;

int main(){
    cout << "A" << endl;
    return 0;
    cout << "B" << endl;
    return 0;
}
```

**Bài 12.** Chương trình sau có 4 lỗi. Hãy tìm và sửa tất cả:

```cpp
#include <iostream>

int main(){
    Cout << "Hello World"
    return 0
}
```

**Bài 13.** Viết chương trình có `return 1;` thay vì `return 0;`. Sau khi chạy, dùng lệnh terminal để in ra mã thoát (exit code) của chương trình và xác nhận nó bằng 1.

**Bài 14.** So sánh `endl` và `"\n"`. Viết một chương trình dùng cả hai và giải thích bằng comment sự khác nhau về mặt kỹ thuật.

**Bài 15.** Viết chương trình in ra "danh thiếp" của bạn trong một khung như sau (nội dung tự thay):

```
+----------------------------+
|                            |
|      NGUYEN VAN A          |
|      C++ Developer         |
|      nguyenvana@mail.com   |
|                            |
+----------------------------+
```
