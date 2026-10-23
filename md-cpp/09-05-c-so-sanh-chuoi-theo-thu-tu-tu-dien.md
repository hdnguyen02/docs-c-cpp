# [C]. So Sánh Chuỗi Theo Thứ Tự Từ Điển

Thứ tự từ điển là một kiến thức quan trọng khi học về xâu ký tự, bài viết này mình sẽ hướng dẫn các bạn cách xác định thứ tự từ điển giữa các xâu ký tự cũng như các hàm mà thư viện `<string.h>` của C đã cung cấp sẵn

**NỘI DUNG :**

- **Thứ Tự Từ Điển (Lexicographically) Là Gì ?** 
- **Hàm strcmp() Và strncmp()**
- **Video Tutorial** 

---

**1. Thứ Tự Từ Điển (Lexicographically) Là Gì ?** 

Thứ tự từ điển của xâu ký tự hiểu đơn giản là thứ tự abc trong bảng chữ cái, trong đó ký tự nào đứng trước trong bảng chữ cái sẽ có thứ tự từ điển nhỏ hơn.

Đối với chuỗi ký tự thì thứ tự từ điển của nó so với chuỗi ký tự khác được xác định bằng ký tự khác nhau đầu tiên của 2 xâu.

**Quy tắc so sánh 2 xâu theo thứ tự từ điển :** 

- Nếu 2 xâu có cùng độ dài và giống nhau mọi ký tự thì bằng nhau, ví dụ "codelab" và "codelab"
- Nếu 2 xâu khác nhau thì ký tự đầu tiên khác nhau của 2 xâu sẽ quy định xâu nào có từ điển lớn hơn, nhỏ hơn. Ví dụ "codelabzabc" và "codelabaz" thì chữ thứ 8 (chỉ số 7) của 2 xâu này khác nhau và 'z' lớn hơn 'a' theo từ điển nên xâu "codelabzabc" lớn hơn "codelabaz" về mặt từ điển
- Nếu 2 xâu không có ký tự khác nhau đầu tiên thì xâu nào dài hơn sẽ có từ điển lớn hơn, ví dụ "codelab" và "codelabblog" thì "codelabblog" có từ điển lớn hơn
- Chữ cái in hoa và in thường có thứ tự từ điển khác nhau và thứ tự từ điển của ký tự được quy định bởi mã ASCII

Một vài ví dụ về thứ tự từ điển của 2 xâu ký tự :

1. "codelab" < "codelabzzz"
2. "1234" < "zzz"
3. "lan" < "lan di hoc lap trinh"
4. "codelab" > "27tech"
5. "codelab java" < "codelab@"

Ở ví dụ 2, ký tự '1' có mã ASCII là 49 nhỏ hơn 'z' là 122. Ở ví dụ 5, dấu cách có mã 32 nhỏ hơn '@' có mã 64.

---

**2. Hàm strcmp() Và strncmp()**

Trong C, xâu là mảng char nên bạn **không thể dùng các toán tử so sánh** như >, <, !=, == để so sánh nội dung 2 xâu. Khi viết `a == b` hay `a < b` với 2 xâu, C sẽ so sánh **địa chỉ** của chúng trong bộ nhớ chứ không so sánh các ký tự, vì vậy kết quả không có ý nghĩa về mặt từ điển.

Để so sánh 2 xâu theo thứ tự từ điển bạn sử dụng hàm **strcmp()** trong thư viện `<string.h>`, hoặc tự cài đặt hàm này cho mình.

Hàm **strcmp(a, b)** sẽ trả về :

- Số **nhỏ hơn 0** nếu xâu a có thứ tự từ điển nhỏ hơn xâu b
- Số **bằng 0** nếu 2 xâu giống nhau
- Số **lớn hơn 0** nếu xâu a có thứ tự từ điển lớn hơn xâu b

Lưu ý chuẩn C chỉ quy định **dấu** của giá trị trả về, không quy định giá trị cụ thể, vì vậy hãy so sánh kết quả với 0 (`strcmp(a, b) < 0`) chứ đừng so sánh với -1 hay 1.

Ví dụ :

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    printf("%s\n", strcmp("codelab", "codelab") == 0 ? "true" : "false");
    printf("%s\n", strcmp("codelab", "codelab") != 0 ? "true" : "false");
    printf("%s\n", strcmp("codelababc", "codelabza") < 0 ? "true" : "false");
    printf("%s\n", strcmp("codelab", "codelab") < 0 ? "true" : "false");
    printf("%s\n", strcmp("codelab", "28@tech") < 0 ? "true" : "false");
    return 0;
}
```

Output :

```
true
false
true
false
false
```

Ở dòng thứ 5, ký tự 'c' (99) lớn hơn '2' (50) nên "codelab" **lớn hơn** "28@tech".

Tương tự ví dụ trên nhưng in trực tiếp dấu của giá trị trả về :

```c
#include <stdio.h>
#include <string.h>

int dau(int x) { return (x > 0) - (x < 0); }   // tra ve -1, 0 hoac 1

int main(void) {
    char s[] = "codelab", t[] = "codeblog", p[] = "codelab";
    printf("%d\n", dau(strcmp(s, p)));
    printf("%d\n", dau(strcmp(s, t)));
    printf("%d\n", dau(strcmp(t, p)));
    return 0;
}
```

Output :

```
0
1
-1
```

Hàm **strncmp(a, b, n)** hoạt động giống strcmp() nhưng chỉ so sánh **tối đa n ký tự đầu tiên** của 2 xâu. Hàm này thường dùng để kiểm tra một xâu có bắt đầu bằng một xâu khác hay không.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    printf("%d\n", strncmp("codelab.dev", "codelab.vn", 7) == 0);   // 7 ky tu dau giong nhau
    printf("%d\n", strncmp("codelab.dev", "codelab.vn", 9) == 0);   // ky tu thu 9 khac nhau
    return 0;
}
```

Output :

```
1
0
```

Hàm strcmp() phân biệt chữ hoa và chữ thường vì so sánh theo mã ASCII. Thư viện chuẩn C không có hàm so sánh không phân biệt hoa thường (hàm `strcasecmp()` chỉ có trên Linux/macOS, Windows dùng `_stricmp()`), nên thông thường bạn sẽ tự cài đặt bằng cách so sánh `tolower()` của từng ký tự.

Ngoài ra bạn cũng có thể tự cài đặt hàm strcmp() như là bài tập rèn luyện.

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-05-c-so-sanh-chuoi-theo-thu-tu-tu-dien.md](solutions/09-05-c-so-sanh-chuoi-theo-thu-tu-tu-dien.md)

**Bài 1.** So sánh 2 chuỗi nhập từ bàn phím bằng `strcmp()` và in kết quả (bằng, nhỏ hơn, lớn hơn).

**Bài 2.** Giải thích vì sao `strcmp("Apple", "apple") < 0`. Chứng minh bằng mã ASCII.

**Bài 3.** Viết hàm so sánh 2 chuỗi **không phân biệt hoa thường**.

**Bài 4.** Nhập `n` chuỗi, sắp xếp chúng theo thứ tự từ điển tăng dần (dùng `qsort` với hàm so sánh gọi `strcmp`).

**Bài 5.** Sắp xếp danh sách tên không phân biệt hoa thường.

**Bài 6.** Tìm chuỗi lớn nhất và nhỏ nhất theo thứ tự từ điển trong một mảng.

**Bài 7.** So sánh `"abc"` với `"abcd"`, `"10"` với `"9"`, `"Z"` với `"a"`. Dự đoán rồi kiểm chứng bằng `strcmp`.

**Bài 8.** Viết hàm so sánh tự cài đặt (không dùng `strcmp`), trả về −1, 0, 1.

**Bài 9.** Sắp xếp danh sách tên theo **tên** (từ cuối cùng) thay vì theo họ.

**Bài 10.** Sắp xếp các chuỗi số `"10"`, `"9"`, `"100"` theo giá trị số thay vì theo từ điển.

**Bài 11.** Viết hàm so sánh "tự nhiên" (natural sort): `"file2"` đứng trước `"file10"`.

**Bài 12.** Kiểm tra một danh sách đã được sắp xếp theo thứ tự từ điển chưa.

**Bài 13.** Tìm tiền tố chung dài nhất của một mảng chuỗi.

**Bài 14.** Sắp xếp danh sách theo độ dài chuỗi, nếu bằng nhau thì theo từ điển.

**Bài 15.** Viết chương trình tra từ điển đơn giản: sắp xếp danh sách từ, tìm kiếm nhị phân theo thứ tự từ điển.
