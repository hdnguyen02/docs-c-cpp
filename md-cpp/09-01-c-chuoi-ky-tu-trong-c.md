# [C]. Chuỗi Ký Tự Trong C

Ngôn ngữ C không có kiểu dữ liệu chuỗi riêng như nhiều ngôn ngữ khác. **Chuỗi (xâu) ký tự** trong C thực chất là một **mảng char** mà ký tự cuối cùng là ký tự kết thúc chuỗi **`'\0'`**. Hiểu rõ quy ước này là chìa khoá để làm việc với chuỗi trong C mà không bị lỗi.

**NỘI DUNG :** 

- **Chuỗi Ký Tự Là Mảng Char Kết Thúc Bằng '\0'**
- **Khai Báo Và Khởi Tạo Chuỗi**
- **In Chuỗi Với %s**
- **Duyệt Chuỗi**
- **Độ Dài Chuỗi Với strlen()**
- **Nhập Chuỗi Từ Bàn Phím**
- **Những Lỗi Thường Gặp**
- **Video Tutorial** 

---

**1. Chuỗi Ký Tự Là Mảng Char Kết Thúc Bằng '\0'**

Một chuỗi trong C là một dãy các ký tự `char` nằm liên tiếp nhau trong bộ nhớ, và **luôn được kết thúc bằng ký tự null `'\0'`** (mã ASCII bằng 0).

Ký tự `'\0'` không được in ra màn hình, nó chỉ là "dấu mốc" để các hàm như `printf`, `strlen`... biết chuỗi kết thúc ở đâu. Không có `'\0'` thì các hàm này sẽ đọc tràn sang vùng nhớ phía sau.

Ví dụ chuỗi `"codelab"` gồm 7 ký tự nhìn thấy được nhưng chiếm **8 byte** trong bộ nhớ :

| **s[index]** | c | o | d | e | l | a | b | \0 |
|---|---|---|---|---|---|---|---|---|
| **index** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

Như vậy một mảng `char` có kích thước `N` chỉ lưu được chuỗi dài **tối đa `N - 1`** ký tự, vì phải dành 1 ô cho `'\0'`.

> 💡 Hằng chuỗi viết trong dấu nháy kép `"codelab"` được trình biên dịch **tự động thêm `'\0'`** ở cuối. Còn hằng ký tự viết trong dấu nháy đơn `'c'` chỉ là **một ký tự**, không phải chuỗi.

---

**2. Khai Báo Và Khởi Tạo Chuỗi**

**Cú pháp :** 

```c
//Khai báo mảng char đủ chứa chuỗi dài tối đa 99 ký tự
char name_string[100];

//Khai báo chuỗi rỗng (chỉ có '\0')
char name_string[100] = "";

//Khai báo chuỗi có nội dung, kích thước tự tính = số ký tự + 1
char name_string[] = "data";

//Khởi tạo từng ký tự, phải tự thêm '\0'
char name_string[] = {'d', 'a', 't', 'a', '\0'};
```

Ví dụ khai báo chuỗi, in nội dung, số ký tự (dùng hàm `strlen()` của thư viện `<string.h>`) và kích thước mảng (dùng `sizeof`) :

```c
#include <stdio.h>
#include <string.h>

int main(){
    char s1[100] = "";
    char s2[] = "codelab";
    char s3[20] = "codelab";
    char s4[] = {'c', 'o', 'd', 'e', '\0'};
    printf("Noi dung s1 : %s\n", s1);
    printf("So ky tu s1 : %zu, kich thuoc mang : %zu\n", strlen(s1), sizeof(s1));
    printf("Noi dung s2 : %s\n", s2);
    printf("So ky tu s2 : %zu, kich thuoc mang : %zu\n", strlen(s2), sizeof(s2));
    printf("Noi dung s3 : %s\n", s3);
    printf("So ky tu s3 : %zu, kich thuoc mang : %zu\n", strlen(s3), sizeof(s3));
    printf("Noi dung s4 : %s\n", s4);
    printf("So ky tu s4 : %zu, kich thuoc mang : %zu\n", strlen(s4), sizeof(s4));
    return 0;
}
```

Output :

```
Noi dung s1 : 
So ky tu s1 : 0, kich thuoc mang : 100
Noi dung s2 : codelab
So ky tu s2 : 7, kich thuoc mang : 8
Noi dung s3 : codelab
So ky tu s3 : 7, kich thuoc mang : 20
Noi dung s4 : code
So ky tu s4 : 4, kich thuoc mang : 5
```

**Giải thích :**

- `strlen()` đếm số ký tự **trước `'\0'`**, còn `sizeof` cho biết **kích thước cả mảng** tính bằng byte.
- `s2` không ghi kích thước nên trình biên dịch cấp đúng 7 + 1 = 8 byte.
- `s3` có 20 ô, chuỗi chỉ dùng 8 ô đầu (kể cả `'\0'`), các ô còn lại được tự điền `'\0'`.
- `strlen()` và `sizeof` trả về kiểu `size_t` nên in bằng đặc tả **`%zu`**.

---

**3. In Chuỗi Với %s**

Để in cả chuỗi ta dùng đặc tả **`%s`** trong `printf()` và truyền **tên mảng** (không có `&`, không có chỉ số). `printf` sẽ in lần lượt từng ký tự cho tới khi gặp `'\0'`.

Ngoài ra có thể dùng hàm `puts()` : in chuỗi và **tự xuống dòng**. Muốn in một ký tự thì dùng `%c` với `s[i]`.

```c
#include <stdio.h>

int main(){
    char s[] = "codelab";
    printf("%s\n", s);          // in ca chuoi
    puts(s);                    // in chuoi + tu xuong dong
    printf("[%10s]\n", s);      // canh phai trong 10 o
    printf("[%-10s]\n", s);     // canh trai trong 10 o
    printf("[%.4s]\n", s);      // chi in toi da 4 ky tu dau
    printf("Ky tu dau : %c\n", s[0]);
    return 0;
}
```

Output :

```
codelab
codelab
[   codelab]
[codelab   ]
[code]
Ky tu dau : c
```

---

**4. Duyệt Chuỗi**

Vì chuỗi là mảng char nên bạn truy xuất các ký tự thông qua chỉ số được đánh từ 0. Có 3 cách duyệt thường gặp :

- Duyệt theo chỉ số từ 0 tới `strlen(s) - 1`
- Duyệt theo chỉ số cho tới khi gặp `'\0'`
- Duyệt bằng con trỏ

Ví dụ `char s[] = "codelab!@#"` :

| **s[index]** | c | o | d | e | l | a | b | ! | @ | # | \0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **index** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |

**Duyệt chuỗi bằng chỉ số và strlen() :** 

```c
#include <stdio.h>
#include <string.h>

int main(){
    char s[] = "codelab!@#";
    int n = strlen(s);          // tinh do dai 1 lan truoc vong lap
    for(int i = 0; i < n; i++){
        printf("s[%d] = %c\n", i, s[i]);
    }
    return 0;
}
```

Output :

```
s[0] = c
s[1] = o
s[2] = d
s[3] = e
s[4] = l
s[5] = a
s[6] = b
s[7] = !
s[8] = @
s[9] = #
```

**Duyệt tới khi gặp '\0' :** 

Cách này không cần biết trước độ dài, đây là cách "tự nhiên" nhất với chuỗi C.

```c
#include <stdio.h>

int main(){
    char s[] = "codelab!@#";
    for(int i = 0; s[i] != '\0'; i++){
        printf("%c ", s[i]);
    }
    printf("\n");
    return 0;
}
```

Output :

```
c o d e l a b ! @ # 
```

**Duyệt bằng con trỏ**

Tên mảng `s` chính là địa chỉ phần tử đầu tiên, vì vậy bạn có thể dùng một con trỏ `char *p` chạy từ `s` cho tới khi `*p` là `'\0'`. Nếu chưa nắm vững con trỏ, bạn xem lại bài [Con Trỏ Và Mảng 1 Chiều](07-03-c-con-tro-va-mang-1-chieu.md).

```c
#include <stdio.h>

int main(){
    char s[] = "codelab!@#";
    for(char *p = s; *p != '\0'; p++){
        printf("%c ", *p);
    }
    printf("\n");
    return 0;
}
```

Output :

```
c o d e l a b ! @ # 
```

> 💡 Điều kiện `s[i] != '\0'` có thể viết gọn là `s[i]`, vì `'\0'` có giá trị 0 tương ứng với "sai".

---

**5. Độ Dài Chuỗi Với strlen()**

Hàm **`strlen()`** trong thư viện `<string.h>` trả về số ký tự của chuỗi, **không tính `'\0'`**.

**Cú pháp** :

```c
size_t strlen(const char *s);
```

Bên trong, `strlen()` chỉ đơn giản là đếm từ đầu chuỗi cho tới khi gặp `'\0'`, bạn hoàn toàn có thể tự viết lại :

```c
#include <stdio.h>
#include <string.h>

int doDai(const char s[]){
    int dem = 0;
    while(s[dem] != '\0'){
        ++dem;
    }
    return dem;
}

int main(){
    char s[] = "lap trinh C";
    printf("Tu viet : %d\n", doDai(s));
    printf("strlen  : %zu\n", strlen(s));
    return 0;
}
```

Output :

```
Tu viet : 11
strlen  : 11
```

> ⚠️ Vì `strlen()` phải đếm lại từ đầu mỗi lần gọi (độ phức tạp O(n)), **không nên** viết `for(int i = 0; i < strlen(s); i++)` — vòng lặp sẽ thành O(n²). Hãy tính `int n = strlen(s);` một lần trước vòng lặp như ví dụ ở mục 4.

---

**6. Nhập Chuỗi Từ Bàn Phím**

**Nhập chuỗi không có khoảng trắng bằng scanf("%s")**

Trong trường hợp chuỗi của bạn không chứa khoảng trắng (dấu cách, tab) thì có thể dùng `scanf()` với đặc tả `%s`. Chú ý **không có dấu `&`** trước tên mảng, vì tên mảng đã là địa chỉ.

```c
#include <stdio.h>

int main(){
    char s[100];
    printf("Nhap xau s : ");
    scanf("%99s", s);           // doc toi da 99 ky tu, chua 1 cho cho '\0'
    printf("Xau vua nhap : %s\n", s);
    return 0;
}
```

Input và output :

```
Nhap xau s : codelab C string
Xau vua nhap : codelab
```

`scanf("%s")` dừng lại ngay khi gặp khoảng trắng, nên chỉ đọc được từ đầu tiên. Số `99` trong `%99s` giới hạn số ký tự được đọc để **không tràn mảng**.

**Nhập cả dòng (có khoảng trắng) bằng fgets()**

Khi muốn đọc chuỗi tới hết dòng (đọc cả dấu cách, tab) thì bạn dùng hàm **`fgets()`** :

**Cú pháp** :

```c
fgets(ten_mang, kich_thuoc_toi_da, stdin);
```

```c
#include <stdio.h>
#include <string.h>

int main(){
    char s[100];
    printf("Nhap xau s : \n");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';     // xoa ky tu '\n' ma fgets giu lai
    printf("Xau vua nhap : %s\n", s);
    printf("Do dai : %zu\n", strlen(s));
    return 0;
}
```

Input và output :

```
input : 
codelab C string
Output : 
Xau vua nhap : codelab C string
Do dai : 16
```

`fgets()` đọc tối đa `kich_thuoc_toi_da - 1` ký tự và **giữ lại ký tự xuống dòng `'\n'`** trong chuỗi, vì vậy ta thường xoá nó đi. Chi tiết về `fgets()`, cách xoá `'\n'` và hiện tượng trôi lệnh khi nhập chuỗi sau khi nhập số sẽ được trình bày ở bài [Xử Lý Trôi Lệnh Khi Nhập Chuỗi](09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi.md).

> ⚠️ **Không bao giờ dùng hàm `gets()`**. Hàm này không giới hạn số ký tự đọc vào nên rất dễ tràn mảng, nó đã bị **loại bỏ khỏi chuẩn C11**.

---

**7. Những Lỗi Thường Gặp**

**Lỗi 1 : Quên chỗ cho '\0'**

```c
char s[7] = "codelab";   // 7 ky tu, KHONG con cho cho '\0'
printf("%s", s);         // printf doc tran sang vung nho phia sau!
```

C vẫn cho biên dịch dòng khai báo này (mảng vừa khít 7 ký tự, bỏ mất `'\0'`) nên lỗi rất khó phát hiện. Phải khai báo `char s[8]` hoặc `char s[] = "codelab"` để trình biên dịch tự tính.

**Lỗi 2 : Gán chuỗi bằng dấu =**

```c
char s[20];
s = "codelab";           // LOI BIEN DICH: khong gan duoc cho mang
```

Chỉ được dùng dấu `=` khi **khởi tạo** lúc khai báo. Sau đó muốn gán nội dung mới phải dùng hàm `strcpy()` (bài [Các Hàm Xử Lý Chuỗi Trong string.h](09-03-c-cac-ham-xu-ly-chuoi-trong-stringh.md)).

**Lỗi 3 : So sánh chuỗi bằng ==**

```c
char a[] = "abc", b[] = "abc";
if(a == b) { ... }       // so sanh DIA CHI 2 mang -> luon sai
```

Muốn so sánh nội dung phải dùng `strcmp()` (bài [So Sánh Chuỗi Theo Thứ Tự Từ Điển](09-05-c-so-sanh-chuoi-theo-thu-tu-tu-dien.md)).

**Lỗi 4 : Sửa hằng chuỗi qua con trỏ**

```c
char *p = "codelab";     // p tro toi hang chuoi, vung nho CHI DOC
p[0] = 'C';              // hanh vi khong xac dinh, thuong bi crash

char s[] = "codelab";    // s la mang RIENG, duoc sao chep noi dung
s[0] = 'C';              // OK
```

Nếu cần sửa chuỗi, hãy khai báo bằng mảng `char s[]`. Nếu dùng con trỏ tới hằng chuỗi, nên viết `const char *p = "codelab";` để trình biên dịch báo lỗi khi lỡ sửa.

---

**Video Chuỗi Ký Tự :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-01-c-chuoi-ky-tu-trong-c.md](solutions/09-01-c-chuoi-ky-tu-trong-c.md)

**Bài 1.** Khai báo chuỗi theo 4 cách khác nhau (mảng rỗng, không ghi kích thước, có kích thước, khởi tạo từng ký tự) và in ra nội dung, `strlen`, `sizeof` của từng chuỗi.

**Bài 2.** Nhập họ tên đầy đủ (có dấu cách) bằng `fgets`, xoá ký tự `'\n'` ở cuối rồi in ra độ dài chuỗi.

**Bài 3.** Duyệt và in từng ký tự của chuỗi theo 3 cách: chỉ số kết hợp `strlen`, chỉ số tới khi gặp `'\0'`, con trỏ.

**Bài 4.** Đếm số ký tự chữ cái, chữ số, dấu cách và ký tự đặc biệt trong chuỗi (dùng các hàm của `<ctype.h>`).

**Bài 5.** Tự viết hàm tính độ dài chuỗi theo 2 cách (dùng chỉ số, dùng con trỏ) và so sánh kết quả với `strlen`.

**Bài 6.** Đảo ngược chuỗi tại chỗ bằng 2 cách: vòng lặp đổi chỗ hai đầu, đệ quy.

**Bài 7.** Kiểm tra chuỗi có đối xứng (palindrome) không, bỏ qua hoa/thường và dấu cách.

**Bài 8.** Đếm số từ trong một câu (các từ cách nhau bằng một hoặc nhiều dấu cách).

**Bài 9.** In ra từ dài nhất và từ ngắn nhất trong câu.

**Bài 10.** Tự viết hàm lấy chuỗi con `layChuoiCon(s, viTri, soKyTu, kq)`: lấy 5 ký tự đầu, 5 ký tự cuối, và các ký tự từ vị trí 3 tới 7. Nhớ thêm `'\0'`.

**Bài 11.** Chương trình sau có lỗi gì? Sửa lại:

```c
char s[7] = "codelab";
char t[20];
t = s;
if (t == "codelab") printf("%s", t);
```

**Bài 12.** So sánh `char s[] = "codelab";` với `char *p = "codelab";`: kích thước `sizeof`, có sửa ký tự được không, có trỏ sang chuỗi khác được không. Lập bảng.

**Bài 13.** Đọc nhiều dòng văn bản bằng `fgets` tới khi gặp dòng trống, đếm tổng số ký tự (không tính `'\n'`).

**Bài 14.** Viết hàm cắt khoảng trắng thừa ở đầu và cuối chuỗi (trim) trực tiếp trên mảng.

**Bài 15.** Viết chương trình "đếm từ" đơn giản: đọc văn bản tới hết đầu vào (EOF), in ra số dòng, số từ, số ký tự (giống lệnh `wc` của Linux).
