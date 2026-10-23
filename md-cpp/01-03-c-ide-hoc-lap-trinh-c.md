# [C]. IDE Học Lập Trình C

Công cụ nào tốt nhất để có thể lập trình C? Để có thể lập trình bằng ngôn ngữ C bạn cần một công cụ để có thể soạn thảo code và chạy được code đó, trong bài viết này mình sẽ gợi ý cho các bạn một vài công cụ phổ biến mà các lập trình viên thường sử dụng khi lập trình C, đồng thời hướng dẫn cách biên dịch một file `.c` bằng trình biên dịch **gcc**

**NỘI DUNG** 

- **IDE Là Gì ?** 
- **Các IDE Và Text Editor Phổ Biến** 
- **Biên Dịch File .c Bằng gcc**

---

**1. IDE Là Gì ?** 

IDE viết tắt của Integrated Development Environment tạm dịch là môi trường phát triển tích hợp. IDE có rất nhiều chức năng như soạn thảo code, gỡ lỗi, biên dịch, kiểm thử ...

Nhìn chung IDE là một công cụ vừa giúp bạn soạn thảo code và vừa có thể biên dịch được code cũng như làm các chức năng khác. Một IDE sẽ có 2 phần chính đó là :

- Text Editor : Hỗ trợ soạn thảo code
- Compiler : Trình biên dịch giúp biên dịch code C của bạn sang mã máy

Bạn có thể hình dung việc biên dịch code như sơ đồ sau

```
 printf("codelab\n");   ───►   Compiler (gcc)   ───►   0101010101010101
  (mã nguồn C, file .c)        (trình biên dịch)       (mã máy, file thực thi)
```

Ngôn ngữ lập trình C bạn đang học là một ngôn ngữ lập trình bậc cao, máy tính không thể chạy được các câu lệnh bạn viết bằng mã nguồn C vì thế cần có một bước trước khi các câu lệnh có thể thực thi đó là biên dịch code. Nhiệm vụ biên dịch code được thực hiện bởi compiler - trình biên dịch, trình biên dịch sẽ giúp biên dịch mã nguồn mà bạn lập trình sang mã máy (file .exe trên Windows) có thể thực thi bởi máy tính.

Mã nguồn C được lưu trong file có đuôi **`.c`** (ví dụ `hello.c`), khác với file `.cpp` của C++. Đuôi file rất quan trọng : nhiều IDE và trình biên dịch dựa vào đuôi file để quyết định biên dịch theo ngôn ngữ C hay C++.

---

**2. Các IDE và Text Editor Phổ Biến**

Có nhiều IDE và Text Editor có thể sử dụng để lập trình C, phổ biến có thể kể đến : DevC++, Codeblock, Visual Studio Code, XCode (MacOS), Sublime text, VIM...

Nếu bạn là newbie thì mình khuyên bạn nên sử dụng công cụ nào dễ cài đặt, dễ làm quen trước. Sau này khi bạn thành thạo việc sử dụng công cụ đó rồi thì có thể chuyển sang các IDE khác đẹp hơn và mạnh mẽ hơn. IDE cũng chỉ là công cụ lập trình, kỹ năng code mới là quan trọng, tất nhiên là một IDE đẹp cũng sẽ làm bạn có nhiều hứng thú hơn với việc lập trình.

Lựa chọn số một của mình với newbie khi học lập trình C trên Windows đó là DevC++ với những lý do sau :

- Miễn phí
- Dễ dàng cài đặt như một phần mềm bình thường
- Đã bao gồm cả text editor và trình biên dịch (bộ MinGW có sẵn gcc)
- Dễ sử dụng, giao diện thân thiện
- Gọn nhẹ

Khi lưu file trong DevC++ bạn nhớ chọn kiểu file là **C source files (\*.c)** để chương trình được biên dịch theo ngôn ngữ C.

Bạn có thể tham khảo cách cài đặt và sử dụng DevC++ trên [video hướng dẫn của mình](https://www.youtube.com/watch?v=237q_8H7YI0), sau khi sử dụng DevC++ để lập trình C một cách thành thạo bạn có thể chuyển sang sử dụng VSCode hoặc Sublime Text để có thể có được nhiều hỗ trợ tốt hơn.

Trường hợp bạn sử dụng máy Mac thì bạn sẽ sử dụng công cụ là XCode hoặc cài luôn VSCode, Sublime text để học lập trình C vì DevC++ chỉ hỗ trợ hệ điều hành Window.

---

**3. Biên Dịch File .c Bằng gcc**

Bên dưới mọi IDE đều là một trình biên dịch. Trình biên dịch C phổ biến nhất là **gcc** (có sẵn trên Linux, đi kèm DevC++/MinGW trên Windows), trên macOS thường dùng **clang** (lệnh `gcc` trên macOS thực chất gọi tới clang). Bạn hoàn toàn có thể biên dịch và chạy chương trình chỉ bằng dòng lệnh.

Ví dụ bạn có file `hello.c` :

```c
#include <stdio.h>

int main(){
    printf("Hello codelab !\n");
    return 0;
}
```

Biên dịch và chạy :

```bash
gcc hello.c -o hello      # biên dịch hello.c thành file thực thi tên hello
./hello                   # chạy trên Linux / macOS (Windows: hello.exe)
```

Output :

```
Hello codelab !
```

Khi học, bạn nên biên dịch kèm theo chuẩn C và các tuỳ chọn bật cảnh báo để trình biên dịch giúp bạn phát hiện lỗi sớm :

```bash
gcc -std=c11 -Wall -Wextra hello.c -o hello
```

- `-std=c11` : biên dịch theo chuẩn C11
- `-Wall -Wextra` : bật hầu hết các cảnh báo hữu ích
- `-o hello` : đặt tên cho file thực thi, nếu bỏ đi thì gcc tạo file mặc định tên `a.out` (Windows là `a.exe`)

**KẾT LUẬN** : IDE và Text Editor chỉ là công cụ hỗ trợ lập trình nên nếu công cụ nào dễ dàng cài đặt và sử dụng cũng như đáp ứng đủ nhu cầu thì bạn nên sử dụng. Hãy nhớ lưu mã nguồn với đuôi `.c` và làm quen dần với việc biên dịch bằng `gcc`.

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/01-03-c-ide-hoc-lap-trinh-c.md](solutions/01-03-c-ide-hoc-lap-trinh-c.md)

**Bài 1.** IDE là viết tắt của cụm từ nào? Nêu 4 chức năng chính của một IDE.

**Bài 2.** Phân biệt Text Editor và Compiler. Notepad có phải là một IDE không? Vì sao?

**Bài 3.** Vẽ sơ đồ các bước từ file mã nguồn `main.c` cho tới khi chương trình chạy và in kết quả ra màn hình.

**Bài 4.** Cài đặt một IDE hoặc trình biên dịch C trên máy của bạn (DevC++, VSCode + gcc, XCode…).

**Bài 5.** Dùng terminal kiểm tra phiên bản trình biên dịch `gcc` đã cài trên máy.

**Bài 6.** Tạo file `hello.c` in ra dòng chữ `Xin chao C`, biên dịch và chạy bằng dòng lệnh.

**Bài 7.** Biên dịch lại file `hello.c` sao cho file thực thi có tên `chaythu`. Nếu không dùng tuỳ chọn `-o` thì file thực thi có tên gì?

**Bài 8.** Cố tình xoá dấu `;` ở một câu lệnh trong `hello.c`, biên dịch lại và giải thích thông báo lỗi.

**Bài 9.** Tìm hiểu ý nghĩa các tuỳ chọn biên dịch của gcc: `-o`, `-Wall`, `-Wextra`, `-std=c11`, `-g`, `-O2`, `-lm`.

**Bài 10.** So sánh DevC++ và Visual Studio Code theo các tiêu chí: dễ cài đặt, dung lượng, tính năng hỗ trợ, dùng lâu dài.

**Bài 11.** Lập bảng phím tắt biên dịch, chạy, lưu file, format code trong DevC++, VSCode và Code::Blocks.

**Bài 12.** Vì sao DevC++ không chạy được trên macOS/Linux? Trên các hệ điều hành này nên dùng công cụ gì?

**Bài 13.** Debug là gì? Thực hành đặt breakpoint và chạy từng dòng một chương trình C trong IDE của bạn (hoặc bằng `gdb`).

**Bài 14.** File `.exe` là gì? Trên Linux/macOS file thực thi có đuôi gì? Vì sao phải gõ `./hello` mà không gõ `hello`?

**Bài 15.** Viết một script (`.sh` hoặc `.bat`) nhận vào tên một file `.c`, tự động biên dịch và chạy file đó.
