# [C]. Chú Thích - Comment

Chú thích là một phần quan trọng khi viết code, chúng có chức năng ghi chú giúp làm sáng rõ ý tưởng chương trình của bạn.

**NỘI DUNG :**

- **Vì Sao Nên Chú Thích Khi Code**
- **Chú Thích Trên 1 Dòng**
- **Chú Thích Trên Nhiều Dòng**

---

**1.Vì Sao Chú Thích Khi Code**

Chú thích không được coi là mã nguồn và sẽ được loại bỏ bởi trình biên dịch khi biên dịch mã nguồn của bạn

Những chức năng chính của chú thích :

- Giải thích mã nguồn - Chú thích có thể được sử dụng như là mã giả với mục đích giải thích code của bạn sẽ thực hiện công việc gì. Khi một lập trình viên khác hay chính bạn đọc mã nguồn của bạn đã từng viết trước đó có thể nhanh chóng nắm bắt ý tưởng của mã nguồn.
- Mô tả thuật toán - Khi các thuật toán bạn cài đặt trở nên phức tạp, bạn cần mô tả và giải thích thuật toán này
- Metadata - Siêu dữ liệu cho chương trình, đôi khi chú thích được sử dụng để mô tả chức năng và các thông tin cần thiết về file mã nguồn
- Debugging - Gỡ lỗi bằng chú thích là một hành động mà mình sử dụng rất nhiều trong quá trình lập trình, khi bạn phát hiện ra những câu lệnh có thể gây lỗi bạn không nhất thiết phải xóa nó đi ngay mà có thể biến nó thành một dòng chú thích để tạm thời loại bỏ nó.

Nhìn chung chú thích có nhiều lợi ích và là một thói quen tốt của một lập trình viên

---

**2.Chú Thích Trên 1 Dòng**

Trong C để chú thích trên 1 dòng ta sử dụng 2 dấu gạch chéo **//,** những nội dung trên cùng một dòng sau 2 dấu gạch chéo này sẽ được coi là chú thích. Nếu muốn chú thích 1 loạt các câu lệnh, bạn có thể sử dụng tổ hợp phím **Ctrl + "/"** và khi muốn mở lại các câu lệnh đó bạn cũng làm tương tự với tổ hợp phím đó. Đây là cách mình hay sử dụng khi muốn tạm thời loại bỏ 1 số dòng code không mong muốn trong quá trình debug

*Ghi chú:* chú thích `//` có trong C từ chuẩn **C99** (trước đó C89 chỉ có `/* */`). Với các chuẩn hiện nay như C11 bạn dùng thoải mái.

Ví dụ :

```c
#include <stdio.h>

//Chu thich tren 1 dong

int main(){
    //Khai bao 3 bien int va khoi tao
    int a = 10, b = 20, c = 30;
    //Khai bao 3 bien char va khoi tao
    char x = '@', y = '#', z = '$';
    //Cau lenh nay in ra gia tri cua 3 bien a, b, c
    printf("%d %d %d\n", a, b, c);
    //Cau lenh nay in ra gia tri cua 3 bien x, y, z
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

**3. Chú Thích Trên Nhiều Dòng**

Để chú thích trên nhiều dòng bạn đặt nội dung cần chú thích vào giữa **/*** và */ .

Ví dụ :

```c
#include <stdio.h>

/*
đây là chú thích trên nhiều dòng
codelab.dev
lập trình C
*/

int main(){
    /*
    Chương trình này khai báo 3 biến int 
    và in ra giá trị của 3 biến lên màn hình
    */
    int a = 10, b = 20, c = 30;
    printf("%d %d %d\n", a, b, c);
    return 0;
}

```

Output :

```
10 20 30
```

---

**Video hướng dẫn Kiểu Dữ Liệu và Biến trong C :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-04-c-chu-thich-comment.md](solutions/02-04-c-chu-thich-comment.md)

**Bài 1.** Viết chương trình tính diện tích hình tam giác và thêm chú thích cho mỗi dòng lệnh giải thích nó làm gì.

**Bài 2.** Viết chương trình có phần **header comment** ở đầu file gồm: tên tác giả, ngày viết, mô tả chức năng chương trình.

**Bài 3.** Dùng chú thích nhiều dòng `/* */` để "tắt" tạm 3 câu lệnh trong một chương trình, chạy thử và quan sát sự khác biệt.

**Bài 4.** Chương trình sau in ra gì? Giải thích:

```c
#include <stdio.h>
int main(){
    printf("A");  // printf("B");
    /* printf("C"); */
    printf("D");
    return 0;
}
```

**Bài 5.** Chương trình sau có lỗi biên dịch. Tìm lỗi và giải thích:

```c
/* Day la chu thich
   /* chu thich long nhau */
   van con chu thich? */
int main(){ return 0; }
```

**Bài 6.** Viết chương trình tính chu vi hình tròn, sau đó dùng chú thích để ghi lại 2 phương án cài đặt khác nhau (giữ lại phương án cũ dưới dạng chú thích).

**Bài 7.** Chú thích có bị đưa vào file thực thi không? Hãy chứng minh bằng cách so sánh kích thước file thực thi của 2 chương trình giống hệt nhau, một cái có 100 dòng chú thích.

**Bài 8.** Viết lại đoạn code sau kèm chú thích để người khác hiểu được ý tưởng:

```c
int n = 153, t = 0, x = n;
while(x > 0){ int d = x % 10; t += d*d*d; x /= 10; }
printf("%d", t == n);
```

**Bài 9.** Phân biệt 3 loại chú thích: giải thích *cái gì*, giải thích *tại sao*, và ghi chú *việc cần làm* (TODO). Viết 1 ví dụ cho mỗi loại.

**Bài 10.** Chú thích nào dưới đây là **chú thích tồi**? Vì sao?

```c
i++;                    // tang i len 1
tong += a[i];           // cong a[i] vao tong
x = x ^ (x >> 16);      // tron bit de giam va cham hash
delay(100);             // cho 100ms
```

**Bài 11.** Tìm hiểu về chú thích kiểu Doxygen (`/** ... */`). Viết chú thích Doxygen cho một hàm tính giai thừa (mô tả hàm, tham số, giá trị trả về).

**Bài 12.** Viết một chương trình khoảng 20 dòng, sau đó xoá hết chú thích và đưa cho bạn bè đọc. Ghi lại họ mất bao lâu để hiểu. Lặp lại với bản có chú thích.

**Bài 13.** Trong IDE bạn dùng, tìm phím tắt để comment/uncomment nhiều dòng cùng lúc. Ghi lại.

**Bài 14.** Viết chương trình có chứa một đoạn code sai, dùng chú thích để "gỡ lỗi từng bước" — comment dần từng phần cho tới khi tìm ra dòng gây lỗi.

**Bài 15.** Viết một "bản mẫu" (template) file C có sẵn phần chú thích chuẩn ở đầu để bạn dùng lại cho mọi bài tập sau này.
