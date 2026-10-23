# [C]. Các Hàm Xử Lý Chuỗi Trong string.h

Các hàm xử lý xâu trong C bao gồm có tính độ dài, sao chép, nối xâu, so sánh, tìm kiếm... và hầu hết đều nằm trong thư viện **`<string.h>`**. Trong bài viết này mình sẽ hướng dẫn các bạn các hàm xử lý xâu thông dụng trong C thông qua ví dụ trực quan.

Nhắc lại: xâu trong C là **mảng `char` kết thúc bằng ký tự `'\0'`**. Các hàm trong `<string.h>` đều dựa vào ký tự `'\0'` này để biết xâu kết thúc ở đâu, và **không tự cấp phát thêm bộ nhớ** — bạn phải đảm bảo mảng đích đủ lớn.

**NỘI DUNG :** 

- **Hàm strlen()**
- **Hàm strcpy() và strncpy()**
- **Hàm strcat() và strncat()**
- **Hàm strcmp() và strncmp()**
- **Hàm strchr() và strrchr()**
- **Hàm strstr()**
- **Hàm memset(), memcpy() và memmove()**

---

**1. Hàm strlen()** 

Hàm **strlen(s)** trả về số ký tự của xâu s, **không tính** ký tự kết thúc `'\0'`. Giá trị trả về có kiểu `size_t` nên khi in ra dùng đặc tả `%zu`.

Lưu ý là strlen() phải đếm từng ký tự cho tới khi gặp `'\0'`, vì vậy nếu dùng trong điều kiện vòng lặp `for (i = 0; i < strlen(s); i++)` thì mỗi lần lặp lại phải đếm lại từ đầu. Nên lưu độ dài vào một biến trước vòng lặp.

Độ phức tạp : O(N)

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[100] = "codelab";
    printf("%zu\n", strlen(s));      // so ky tu thuc te
    printf("%zu\n", sizeof(s));      // kich thuoc ca mang
    s[0] = '\0';                     // "xoa" xau: bien thanh xau rong
    printf("%zu\n", strlen(s));
    if (s[0] == '\0') printf("Xau rong\n");
    return 0;
}
```

Output :

```
7
100
0
Xau rong
```

---

**2. Hàm strcpy() và strncpy()**

Trong C bạn **không thể gán xâu bằng toán tử `=`** (ví dụ `s = "abc";` sẽ báo lỗi vì s là mảng). Muốn gán nội dung xâu này cho xâu khác bạn dùng hàm **strcpy()**.

**Cú pháp :**

- strcpy(dest, src) : Sao chép toàn bộ xâu src (kể cả `'\0'`) vào dest
- strncpy(dest, src, n) : Sao chép tối đa n ký tự của src vào dest

Lưu ý với strncpy() : nếu src có từ n ký tự trở lên thì dest **sẽ không có** ký tự `'\0'` ở cuối, bạn phải tự thêm vào. Cách này thường dùng để **tách xâu con** (tương tự lấy n ký tự từ một vị trí).

Độ phức tạp : O(N)

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[100];
    strcpy(s, "codelab.dev");
    printf("%s\n", s);

    //Xau con tu chi so 2 toi het xau
    char sub1[100];
    strcpy(sub1, s + 2);
    printf("%s\n", sub1);

    //Xau con tu chi so 0 co do dai 4
    char sub2[100];
    strncpy(sub2, s, 4);
    sub2[4] = '\0';                  // tu them ky tu ket thuc
    printf("%s\n", sub2);
    return 0;
}
```

Output :

```
codelab.dev
delab.dev
code
```

Ở đây `s + 2` là con trỏ trỏ tới ký tự có chỉ số 2 của xâu s, nên strcpy sẽ sao chép từ vị trí đó tới hết xâu.

---

**3. Hàm strcat() và strncat()**

Hàm **strcat()** có chức năng nối xâu vào cuối của xâu hiện tại. Bạn có thể lựa chọn nối toàn bộ xâu khác vào xâu hiện tại hoặc nối vài ký tự đầu của xâu khác vào xâu hiện tại bằng **strncat()**.

**Cú pháp :**

- strcat(dest, src) : Nối toàn bộ src vào cuối dest
- strncat(dest, src, n) : Nối tối đa n ký tự đầu của src vào cuối dest, luôn tự thêm `'\0'`

Mảng dest phải đủ chỗ chứa cả xâu cũ, xâu được nối và ký tự `'\0'`, nếu không sẽ gây **tràn mảng**.

Độ phức tạp : O(N)

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[100] = "codelab";
    //Noi toan bo xau
    strcat(s, "blog");
    printf("%s\n", s);
    char t[] = "0123456789";
    //Noi 5 ki tu tinh tu chi so 1 cua xau t vao s
    strncat(s, t + 1, 5);
    printf("%s\n", s);
    return 0;
}
```

Output :

```
codelabblog
codelabblog12345
```

Nếu muốn thêm **1 ký tự** vào cuối xâu hoặc xoá đi ký tự cuối, bạn thao tác trực tiếp với ký tự `'\0'`:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[100] = "codelab";
    size_t n = strlen(s);
    s[n] = '@';                // them ky tu vao cuoi
    s[n + 1] = '\0';           // dat lai ky tu ket thuc
    printf("%s\n", s);
    s[strlen(s) - 1] = '\0';   // xoa ky tu cuoi cung
    printf("%s\n", s);
    return 0;
}
```

Output :

```
codelab@
codelab
```

---

**4. Hàm strcmp() và strncmp()**

Trong C bạn **không so sánh được nội dung 2 xâu bằng toán tử `==`**, vì khi đó bạn chỉ đang so sánh **địa chỉ** của 2 mảng. Muốn so sánh nội dung bạn dùng hàm **strcmp()**.

**Cú pháp :**

- strcmp(a, b) : trả về 0 nếu 2 xâu bằng nhau, số âm nếu a đứng trước b theo thứ tự từ điển, số dương nếu a đứng sau b
- strncmp(a, b, n) : giống strcmp nhưng chỉ so sánh tối đa n ký tự đầu

Độ phức tạp : O(N)

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char a[] = "codelab";
    char b[] = "codelab";
    if (strcmp(a, b) == 0) printf("Bang nhau\n");
    if (a != b) printf("Nhung dia chi khac nhau\n");
    if (strncmp("codelab.dev", "code", 4) == 0) printf("Bat dau bang code\n");
    return 0;
}
```

Output :

```
Bang nhau
Nhung dia chi khac nhau
Bat dau bang code
```

Chi tiết về so sánh xâu theo thứ tự từ điển mình sẽ trình bày ở bài [So sánh chuỗi theo thứ tự từ điển](09-05-c-so-sanh-chuoi-theo-thu-tu-tu-dien.md).

---

**5. Hàm strchr() và strrchr()**

Hàm **strchr(s, c)** tìm vị trí xuất hiện **đầu tiên** của ký tự c trong xâu s, còn **strrchr(s, c)** tìm vị trí xuất hiện **cuối cùng**.

Cả 2 hàm trả về **con trỏ** tới ký tự tìm được, hoặc **NULL** nếu không tìm thấy. Muốn đổi con trỏ thành chỉ số bạn lấy con trỏ đó trừ đi địa chỉ đầu xâu.

Độ phức tạp : O(N)

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "codelab.dev";
    char *p = strchr(s, 'e');
    if (p != NULL) printf("'e' dau tien tai chi so %d\n", (int)(p - s));
    char *q = strrchr(s, 'e');
    if (q != NULL) printf("'e' cuoi cung tai chi so %d\n", (int)(q - s));
    if (strchr(s, 'z') == NULL) printf("Khong co 'z'\n");
    return 0;
}
```

Output :

```
'e' dau tien tai chi so 3
'e' cuoi cung tai chi so 9
Khong co 'z'
```

---

**6. Hàm strstr()**

Hàm **strstr(s, t)** giúp bạn tìm kiếm sự xuất hiện của xâu con t trong xâu s.

Hàm này sẽ trả về con trỏ tới vị trí đầu tiên của xâu con nếu xâu này tồn tại trong xâu đang tìm kiếm, ngược lại sẽ trả về **NULL**.

Độ phức tạp : O(N * M) trong trường hợp xấu, với N, M là độ dài 2 xâu

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "codelab.dev codelab";
    char *p = strstr(s, "codelab");
    if (p == NULL) {
        printf("NOT FOUND\n");
    }
    else {
        printf("FOUND\n");
        printf("%d\n", (int)(p - s));
        //Tim lan xuat hien tiep theo, bat dau sau vi tri vua tim duoc
        p = strstr(p + 1, "codelab");
        if (p != NULL) printf("%d\n", (int)(p - s));
    }
    return 0;
}
```

Output :

```
FOUND
0
12
```

---

**7. Hàm memset(), memcpy() và memmove()**

Ba hàm này làm việc trên **từng byte** của vùng nhớ, không quan tâm tới ký tự `'\0'`:

- memset(p, c, n) : Gán giá trị c cho n byte đầu tiên tính từ p. Thường dùng để xoá trắng mảng hoặc gán cả mảng thành cùng 1 ký tự
- memcpy(dest, src, n) : Sao chép n byte từ src sang dest, **2 vùng nhớ không được chồng lên nhau**
- memmove(dest, src, n) : Giống memcpy nhưng **an toàn khi 2 vùng nhớ chồng lên nhau**

Nhờ memmove() bạn có thể dịch chuyển các ký tự trong cùng một xâu để **chèn** hoặc **xoá** một đoạn ký tự tại vị trí bất kỳ.

Độ phức tạp : O(N)

**Ví dụ :** 

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char a[10];
    memset(a, '*', 5);                 // 5 ky tu '*'
    a[5] = '\0';
    printf("%s\n", a);

    //Chen "####" vao chi so 2 cua xau s
    char s[100] = "codelab";
    size_t n = strlen(s);
    memmove(s + 2 + 4, s + 2, n - 2 + 1);   // doi phan sau (ca '\0') sang phai 4 o
    memcpy(s + 2, "####", 4);               // chep 4 ky tu vao cho trong
    printf("%s\n", s);

    //Xoa 4 ki tu tinh tu chi so 2
    char t[100] = "codelab.dev";
    n = strlen(t);
    memmove(t + 2, t + 2 + 4, n - 2 - 4 + 1);   // doi phan sau sang trai 4 o
    printf("%s\n", t);

    //Xoa tu chi so 3 toi het xau
    t[3] = '\0';
    printf("%s\n", t);
    return 0;
}
```

Output :

```
*****
co####delab
cob.dev
cob
```

Lưu ý memset() gán theo từng byte, nên với mảng số nguyên nó chỉ dùng đúng khi gán giá trị 0 (hoặc -1), ví dụ `memset(dem, 0, sizeof(dem));`.

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-03-c-cac-ham-xu-ly-chuoi-trong-stringh.md](solutions/09-03-c-cac-ham-xu-ly-chuoi-trong-stringh.md)

**Bài 1.** Dùng `strlen()`, `sizeof`, kiểm tra xâu rỗng và "xoá" xâu (`s[0] = '\0'`) trên một chuỗi và in kết quả từng bước.

**Bài 2.** Dùng `strstr()` tìm vị trí xuất hiện đầu tiên của một chuỗi con. Xử lý trường hợp không tìm thấy.

**Bài 3.** Đếm số lần xuất hiện của một chuỗi con trong chuỗi mẹ.

**Bài 4.** Tìm tất cả vị trí xuất hiện của một ký tự trong chuỗi (dùng `strchr()` trong vòng lặp).

**Bài 5.** Viết hàm thay thế một đoạn chuỗi tại vị trí cho trước. Viết hàm thay thế **tất cả** các lần xuất hiện của một chuỗi con.

**Bài 6.** Viết hàm `chenXau(s, viTri, t)` dùng `memmove()` chèn chuỗi vào giữa, đầu, cuối chuỗi khác.

**Bài 7.** Viết hàm `xoaDoan(s, viTri, n)` xoá một đoạn chuỗi; dùng nó để xoá một ký tự, xoá từ vị trí đến hết.

**Bài 8.** Dùng `strchr()`, `strrchr()` và `strncpy()` tách họ, tên đệm, tên từ chuỗi họ tên đầy đủ.

**Bài 9.** Dùng `strrchr()` tìm vị trí xuất hiện **cuối cùng**. Áp dụng để lấy phần mở rộng của tên file.

**Bài 10.** Dùng `strpbrk()`, `strspn()`, `strcspn()` và giải thích khác biệt với `strchr()`, `strstr()`.

**Bài 11.** Viết hàm tách chuỗi theo dấu phân cách (split) lưu các phần vào mảng 2 chiều `char kq[][50]`, trả về số phần.

**Bài 12.** Viết hàm nối một mảng các chuỗi thành một chuỗi với dấu phân cách (join).

**Bài 13.** Dùng `strcmp()`, `strncmp()` so sánh 2 chuỗi. Giải thích vì sao không dùng được toán tử `==`, `<`.

**Bài 14.** Viết hàm kiểm tra chuỗi có bắt đầu / kết thúc bằng một chuỗi con cho trước.

**Bài 15.** Viết một "thư viện xử lý chuỗi" gồm: `trim`, `split`, `join`, `replaceAll`, `toUpper`, `toLower`, `startsWith`, `endsWith`, `contains`.
