# Lời giải — [C]. Bảng Mã ASCII Và Thư Viện ctype.h

[← Quay lại bài học](../03-04-c-bang-ma-ascii-va-thu-vien-ctypeh.md)

> **3 mốc ASCII cần thuộc lòng:** `'0'` = **48**, `'A'` = **65**, `'a'` = **97**. Khoảng cách hoa–thường luôn là **32**.

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    printf("Ky tu '%c' co ma ASCII = %d\n", c, c);
    return 0;
}
```

💡 Cùng một biến `c`: in bằng `%c` ra ký tự, in bằng `%d` ra mã ASCII.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int ma;
    printf("Nhap ma ASCII (0-127): ");
    scanf("%d", &ma);

    if (ma < 0 || ma > 127) {
        printf("Ngoai pham vi ASCII chuan!\n");
        return 1;
    }

    printf("Ma %d la ky tu: '%c'\n", ma, ma);
    return 0;
}
```

⚠️ Mã 0–31 là các **ký tự điều khiển** (không in ra được): 7 = chuông, 9 = tab, 10 = xuống dòng, 13 = về đầu dòng. Chúng sẽ hiện ra lạ hoặc không hiện gì.

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    printf("BANG MA ASCII (33 - 126)\n");
    printf("------------------------------------------\n");

    for (int ma = 33; ma <= 126; ma++) {
        printf("%3d:%c   ", ma, ma);

        // Xuong dong sau moi 8 ky tu
        if ((ma - 32) % 8 == 0) printf("\n");
    }
    printf("\n");
    return 0;
}
```

Output (một phần):

```
BANG MA ASCII (33 - 126)
------------------------------------------
 33:!    34:"    35:#    36:$    37:%    38:&    39:'    40:(   
 41:)    42:*    43:+    44:,    45:-    46:.    47:/    48:0   
 49:1    50:2    51:3    52:4    53:5    54:6    55:7    56:8   
...
```

💡 `%3d` in số chiếm đủ 3 ô, căn phải — giúp các cột thẳng hàng.

**Vì sao bắt đầu từ 33:** mã 32 là dấu cách (in ra không thấy gì), mã 0–31 là ký tự điều khiển. Mã 127 là DEL.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    printf("Ky tu '%c' (ASCII %d) la: ", c, c);

    if (c >= 'A' && c <= 'Z') {
        printf("CHU HOA\n");
    } else if (c >= 'a' && c <= 'z') {
        printf("CHU THUONG\n");
    } else if (c >= '0' && c <= '9') {
        printf("CHU SO\n");
    } else {
        printf("KY TU DAC BIET\n");
    }
    return 0;
}
```

**Cơ sở:** các nhóm ký tự nằm **liên tiếp** trong bảng ASCII, nên chỉ cần kiểm tra khoảng.

| Nhóm | Khoảng ASCII |
|---|---|
| `'0'`–`'9'` | 48–57 |
| `'A'`–`'Z'` | 65–90 |
| `'a'`–`'z'` | 97–122 |

💡 Viết `c >= 'A'` dễ đọc hơn `c >= 65` — kết quả như nhau vì `'A'` chính là hằng số 65.

### Bài 5.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("Nhap mot ky tu: ");
    scanf(" %c", &c);

    printf("Ky tu '%c' la: ", c);

    if      (isupper((unsigned char)c)) printf("CHU HOA\n");
    else if (islower((unsigned char)c)) printf("CHU THUONG\n");
    else if (isdigit((unsigned char)c)) printf("CHU SO\n");
    else                                printf("KY TU DAC BIET\n");

    return 0;
}
```

**So sánh 2 cách:**

| | So sánh ASCII thủ công | Dùng `<ctype.h>` |
|---|---|---|
| Dễ đọc | Trung bình | ✅ Rất rõ ràng |
| Dễ sai | ⚠️ Dễ nhầm `'Z'` với `'z'` | ✅ Khó sai |
| Đúng với mọi bảng mã | ❌ Chỉ đúng với ASCII | ✅ Đúng cả với locale khác |

✅ **Nên dùng `<ctype.h>`** trong code thật. Học cách so sánh ASCII để **hiểu bản chất**.

⚠️ Các hàm này trả về **`int`**, không phải `bool`. `isupper('A')` có thể trả về 1, 256, hay bất kỳ số khác 0 nào. Nên đừng viết `if (isupper(c) == 1)` — cứ viết `if (isupper(c))`.

💡 **Vì sao ép `(unsigned char)`:** tham số của các hàm `ctype.h` phải là giá trị trong khoảng của `unsigned char` (hoặc `EOF`). Trên nhiều máy `char` là có dấu, ký tự có mã > 127 sẽ thành số âm → hành vi không xác định. Với chữ cái, chữ số thông thường thì không sao, nhưng ép kiểu là thói quen an toàn.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    char c;
    printf("Nhap mot chu cai: ");
    scanf(" %c", &c);

    if (c >= 'a' && c <= 'z') {
        printf("Chu hoa: %c\n", c - 32);
    } else if (c >= 'A' && c <= 'Z') {
        printf("Chu thuong: %c\n", c + 32);
    } else {
        printf("'%c' khong phai chu cai!\n", c);
    }
    return 0;
}
```

⚠️ **Đặc tả quyết định cách in.** `c - 32` có kiểu `int`; nếu in bằng `%d` sẽ ra **số** (ví dụ 65), in bằng `%c` mới ra ký tự.

### Bài 7.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("Nhap mot chu cai: ");
    scanf(" %c", &c);

    if (islower((unsigned char)c)) {
        printf("Chu hoa: %c\n", toupper((unsigned char)c));
    } else if (isupper((unsigned char)c)) {
        printf("Chu thuong: %c\n", tolower((unsigned char)c));
    } else {
        printf("'%c' khong phai chu cai!\n", c);
    }
    return 0;
}
```

⚠️ **`toupper` và `tolower` trả về kiểu `int`** (mã ASCII), không phải `char`. In bằng `%c` để thấy ký tự; in bằng `%d` sẽ thấy số.

```c
printf("%d", toupper('a'));     // in ra: 65
printf("%c", toupper('a'));     // in ra: A
```

💡 **Ưu điểm của `toupper`/`tolower` so với `±32`:** chúng **an toàn** — nếu ký tự không phải chữ cái, hàm trả về nguyên ký tự đó. Trong khi `c - 32` áp dụng mù quáng lên `'5'` sẽ cho ký tự rác.

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    char c;
    printf("Nhap mot ky tu so (0-9): ");
    scanf(" %c", &c);

    if (c < '0' || c > '9') {
        printf("Khong phai ky tu so!\n");
        return 1;
    }

    int so = c - '0';        // '7' - '0' = 55 - 48 = 7

    printf("Ky tu '%c' -> so %d\n", c, so);
    printf("%d^2 = %d\n", so, so * so);
    return 0;
}
```

**Công thức vàng:**

```c
int so = kyTu - '0';          // doi ky tu so -> so nguyen
char kyTu = so + '0';         // doi so nguyen (0-9) -> ky tu so
```

Đây là kỹ thuật dùng **liên tục** khi xử lý chuỗi số ở chương 9.

⚠️ **Sai lầm phổ biến:** `int so = (int)c;` cho ra **55** (mã ASCII) chứ không phải 7. Phải **trừ đi `'0'`**.

### Bài 9.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("Nhap mot chu cai: ");
    scanf(" %c", &c);

    if (!isalpha((unsigned char)c)) {
        printf("Khong phai chu cai!\n");
        return 1;
    }

    int thuTu = tolower((unsigned char)c) - 'a' + 1;

    printf("'%c' la chu cai thu %d trong bang chu cai\n", c, thuTu);
    return 0;
}
```

Ví dụ: `C` → 3, `z` → 26, `A` → 1.

**Giải thích công thức:** `tolower(c)` đưa về chữ thường, `- 'a'` cho khoảng cách từ `'a'` (0-based), `+ 1` để đánh số từ 1.

### Bài 10.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    printf("Nhap mot chu cai: ");
    scanf(" %c", &c);

    if (!isalpha((unsigned char)c)) {
        printf("Khong phai chu cai!\n");
        return 1;
    }

    char doiXung;
    if (isupper((unsigned char)c)) {
        doiXung = 'Z' - (c - 'A');
    } else {
        doiXung = 'z' - (c - 'a');
    }

    printf("%c <-> %c\n", c, doiXung);
    return 0;
}
```

Kiểm thử: `A`→`Z`, `B`→`Y`, `M`→`N`, `z`→`a`

**Giải thích công thức `'Z' - (c - 'A')`:**

```
c = 'C':  c - 'A' = 2  (C la chu thu 2 tinh tu 0)
          'Z' - 2 = 'X' (lui 2 buoc tu cuoi bang)
```

Đây chính là phép mã hoá **Atbash** — một trong những mã cổ nhất, dùng trong tiếng Do Thái cổ.

### Bài 11.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c;
    int k;

    printf("Nhap chu cai: ");        scanf(" %c", &c);
    printf("Nhap so buoc dich k: "); scanf("%d", &k);

    if (!isalpha((unsigned char)c)) {
        printf("Khong phai chu cai!\n");
        return 1;
    }

    // Chuan hoa k ve khoang [0, 25], xu ly duoc ca k am va k rat lon
    k = ((k % 26) + 26) % 26;

    char goc = isupper((unsigned char)c) ? 'A' : 'a';
    char kq  = goc + (c - goc + k) % 26;

    printf("%c dich %d buoc -> %c\n", c, k, kq);
    return 0;
}
```

Kiểm thử:

| Ký tự | k | Kết quả |
|---|---|---|
| A | 3 | D |
| X | 3 | **A** (xoay vòng) |
| z | 1 | a |
| M | −1 | L |
| A | 29 | D (29 % 26 = 3) |

**Giải thích công thức `goc + (c - goc + k) % 26`:**

```
c - goc       : dua ve so thu tu 0-25  ('X' - 'A' = 23)
+ k           : dich k buoc            (23 + 3 = 26)
% 26          : xoay vong ve 0-25      (26 % 26 = 0)
+ goc         : doi nguoc lai thanh ky tu  ('A' + 0 = 'A')
```

**Vì sao cần `((k % 26) + 26) % 26`:** nếu `k` âm (ví dụ −3), `k % 26` trong C cho **−3** chứ không phải 23. Cộng 26 rồi lấy dư lần nữa sẽ đưa về đúng khoảng dương.

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    printf("'A' = %d\n", 'A');                          // 65
    printf("'a' = %d\n", 'a');                          // 97
    printf("Khoang cach = %d\n", 'a' - 'A');            // 32

    printf("'A' + 32 = %c\n", 'A' + 32);                // a
    printf("So sanh: %d\n", 'A' + 32 == 'a');           // 1 (true)

    // Kiem tra voi moi chu cai
    bool dungHet = true;
    for (char c = 'A'; c <= 'Z'; c++) {
        if (c + 32 != c - 'A' + 'a') dungHet = false;
    }
    printf("Dung voi moi chu cai: %s\n", dungHet ? "true" : "false");
    return 0;
}
```

**Con số 32 đến từ đâu:**

Trong bảng ASCII, khối chữ hoa bắt đầu ở **65** và khối chữ thường bắt đầu ở **97**. `97 − 65 = 32`.

Đây **không phải ngẫu nhiên** — người thiết kế ASCII (năm 1963) cố ý chọn như vậy, vì 32 = 2⁵, nghĩa là chữ hoa và chữ thường chỉ khác nhau đúng **một bit** (bit thứ 6):

```
'A' = 65  = 0100 0001
'a' = 97  = 0110 0001
                ↑
           chi khac bit nay
```

Nhờ vậy, việc đổi hoa ↔ thường có thể làm bằng phép toán bit cực nhanh:

```c
c | 32     // doi sang chu THUONG (bat bit 6)
c & ~32    // doi sang chu HOA    (tat bit 6)
c ^ 32     // DAO hoa <-> thuong
```

```c
printf("%c\n", 'A' | 32);    // a
printf("%c\n", 'a' & ~32);   // A
printf("%c\n", 'A' ^ 32);    // a
printf("%c\n", 'a' ^ 32);    // A
```

⚠️ Các mẹo bit này chỉ đúng với **chữ cái**. Áp dụng lên ký tự khác sẽ cho kết quả rác — nên trong code thật vẫn nên dùng `toupper`/`tolower`.

### Bài 13.

```c
char c = 'A';
printf("%c\n", c);              // A
printf("%d\n", c + 1);          // 66
printf("%c\n", c + 1);          // B
printf("%c\n", (char)(c + 32)); // a
```

**Output:**

```
A
66
B
a
```

**Giải thích từng dòng:**

| Dòng | Kết quả | Vì sao |
|---|---|---|
| `printf("%c", c)` | `A` | Đặc tả `%c` → in ra **ký tự** có mã 65 |
| `printf("%d", c + 1)` | `66` | Phép `+` **nâng kiểu** `char` lên `int` (integer promotion) → 66; `%d` in ra **số** |
| `printf("%c", c + 1)` | `B` | Vẫn là số 66, nhưng `%c` in ra ký tự có mã 66 |
| `printf("%c", (char)(c + 32))` | `a` | Ép về `char` (mã 97) rồi in ký tự; bỏ `(char)` kết quả cũng như vậy |

**Nguyên tắc cốt lõi:** `printf` quyết định in số hay ký tự dựa vào **đặc tả** (`%d` hay `%c`), không phải kiểu của biến. Vì vậy đặc tả phải khớp với ý định của bạn.

**Integer promotion:** khi `char` tham gia phép toán số học (hoặc được truyền vào `printf`), nó **tự động được nâng lên `int`**. Đây là quy tắc của C nhằm tránh tràn số với kiểu nhỏ.

💡 Trong C, hằng ký tự như `'A'` có sẵn kiểu **`int`** (khác với C++ là `char`), nên `sizeof('A')` bằng `sizeof(int)`.

### Bài 14.

```c
#include <stdio.h>
#include <ctype.h>

// In "true"/"false" tu gia tri tra ve cua ham ctype (khac 0 = true)
const char *tf(int x) { return x ? "true" : "false"; }

int main(void) {
    // isspace: dau cach, tab, xuong dong, ...
    printf("isspace(' ')  = %s\n", tf(isspace(' ')));    // true
    printf("isspace('\\t') = %s\n", tf(isspace('\t')));  // true
    printf("isspace('A')  = %s\n", tf(isspace('A')));    // false

    // ispunct: dau cau va ky tu dac biet (khong phai chu, so, khoang trang)
    printf("ispunct('!')  = %s\n", tf(ispunct('!')));    // true
    printf("ispunct('@')  = %s\n", tf(ispunct('@')));    // true
    printf("ispunct('A')  = %s\n", tf(ispunct('A')));    // false

    // isxdigit: chu so he 16 (0-9, a-f, A-F)
    printf("isxdigit('7') = %s\n", tf(isxdigit('7')));  // true
    printf("isxdigit('F') = %s\n", tf(isxdigit('F')));  // true
    printf("isxdigit('G') = %s\n", tf(isxdigit('G')));  // false

    // isprint: ky tu in ra duoc (bao gom ca dau cach)
    printf("isprint('A')  = %s\n", tf(isprint('A')));    // true
    printf("isprint(' ')  = %s\n", tf(isprint(' ')));    // true
    printf("isprint('\\n') = %s\n", tf(isprint('\n')));  // false

    return 0;
}
```

**Bảng đầy đủ các hàm `<ctype.h>`:**

| Hàm | Trả về true (khác 0) khi ký tự là |
|---|---|
| `isalpha(c)` | Chữ cái (a–z, A–Z) |
| `isdigit(c)` | Chữ số (0–9) |
| `isalnum(c)` | Chữ cái **hoặc** chữ số |
| `isupper(c)` | Chữ hoa |
| `islower(c)` | Chữ thường |
| `isspace(c)` | Khoảng trắng: `' '`, `'\t'`, `'\n'`, `'\v'`, `'\f'`, `'\r'` |
| `ispunct(c)` | Dấu câu / ký tự đặc biệt in được (không phải chữ, số, khoảng trắng) |
| `isxdigit(c)` | Chữ số hệ 16: 0–9, a–f, A–F |
| `isprint(c)` | Ký tự in ra được (mã 32–126) |
| `iscntrl(c)` | Ký tự điều khiển (mã 0–31 và 127) |
| `isgraph(c)` | Ký tự in được **trừ** dấu cách |
| `toupper(c)` | *(trả về)* mã ASCII chữ hoa tương ứng |
| `tolower(c)` | *(trả về)* mã ASCII chữ thường tương ứng |

### Bài 15.

```c
#include <stdio.h>
#include <ctype.h>

const char *tf(int x) { return x ? "true" : "false"; }

int main(void) {
    char c;
    printf("Nhap mot ky tu: ");
    scanf("%c", &c);            // khong co dau cach truoc %c -> doc duoc ca dau cach
    unsigned char u = (unsigned char)c;

    printf("\n+---------------+---------+\n");
    printf("| Ham kiem tra  | Ket qua |\n");
    printf("+---------------+---------+\n");

    printf("| %-13s | %-7s |\n", "isalpha", tf(isalpha(u)));
    printf("| %-13s | %-7s |\n", "isdigit", tf(isdigit(u)));
    printf("| %-13s | %-7s |\n", "isalnum", tf(isalnum(u)));
    printf("| %-13s | %-7s |\n", "isupper", tf(isupper(u)));
    printf("| %-13s | %-7s |\n", "islower", tf(islower(u)));
    printf("| %-13s | %-7s |\n", "isspace", tf(isspace(u)));
    printf("| %-13s | %-7s |\n", "ispunct", tf(ispunct(u)));
    printf("| %-13s | %-7s |\n", "isprint", tf(isprint(u)));
    printf("+---------------+---------+\n");

    printf("\nMa ASCII : %d\n", c);
    if (isalpha(u)) {
        printf("Chu hoa  : %c\n", toupper(u));
        printf("Chu thuong: %c\n", tolower(u));
    }
    return 0;
}
```

Ví dụ nhập `K`:

```
+---------------+---------+
| Ham kiem tra  | Ket qua |
+---------------+---------+
| isalpha       | true    |
| isdigit       | false   |
| isalnum       | true    |
| isupper       | true    |
| islower       | false   |
| isspace       | false   |
| ispunct       | false   |
| isprint       | true    |
+---------------+---------+

Ma ASCII : 75
Chu hoa  : K
Chu thuong: k
```

💡 `%-13s` in chuỗi chiếm 13 ô, **căn trái** (dấu `-`) — giúp bảng thẳng cột.

⚠️ Các hàm trả về `int` với giá trị khác 0 bất kỳ (ví dụ `1024`), nên phải tự đổi sang chữ `true`/`false` bằng toán tử `? :` (hàm `tf` ở trên). C không có sẵn cách in `bool` thành chữ.

⚠️ Lưu ý: `scanf(" %c", &c)` (có dấu cách trước `%c`) **bỏ qua khoảng trắng**, nên không thể nhập dấu cách để thử `isspace`. Vì vậy bài này dùng `scanf("%c", &c)` không có dấu cách (hoặc `c = getchar();`).
