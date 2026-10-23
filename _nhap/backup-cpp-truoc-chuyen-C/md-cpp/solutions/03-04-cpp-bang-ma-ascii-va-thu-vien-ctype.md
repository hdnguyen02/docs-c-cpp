# Lời giải — [C++]. Bảng Mã ASCII Và Thư Viện ctype

[← Quay lại bài học](../03-04-cpp-bang-ma-ascii-va-thu-vien-ctype.md)

> **3 mốc ASCII cần thuộc lòng:** `'0'` = **48**, `'A'` = **65**, `'a'` = **97**. Khoảng cách hoa–thường luôn là **32**.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    cout << "Ky tu '" << c << "' co ma ASCII = " << (int)c << endl;
    return 0;
}
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int ma;
    cout << "Nhap ma ASCII (0-127): ";
    cin >> ma;

    if (ma < 0 || ma > 127) {
        cout << "Ngoai pham vi ASCII chuan!" << endl;
        return 1;
    }

    cout << "Ma " << ma << " la ky tu: '" << (char)ma << "'" << endl;
    return 0;
}
```

⚠️ Mã 0–31 là các **ký tự điều khiển** (không in ra được): 7 = chuông, 9 = tab, 10 = xuống dòng, 13 = về đầu dòng. Chúng sẽ hiện ra lạ hoặc không hiện gì.

### Bài 3.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << "BANG MA ASCII (33 - 126)" << endl;
    cout << "------------------------------------------" << endl;

    for (int ma = 33; ma <= 126; ma++) {
        cout << setw(3) << ma << ":" << (char)ma << "   ";

        // Xuong dong sau moi 8 ky tu
        if ((ma - 32) % 8 == 0) cout << endl;
    }
    cout << endl;
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

**Vì sao bắt đầu từ 33:** mã 32 là dấu cách (in ra không thấy gì), mã 0–31 là ký tự điều khiển. Mã 127 là DEL.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    cout << "Ky tu '" << c << "' (ASCII " << (int)c << ") la: ";

    if (c >= 'A' && c <= 'Z') {
        cout << "CHU HOA" << endl;
    } else if (c >= 'a' && c <= 'z') {
        cout << "CHU THUONG" << endl;
    } else if (c >= '0' && c <= '9') {
        cout << "CHU SO" << endl;
    } else {
        cout << "KY TU DAC BIET" << endl;
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

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    cout << "Ky tu '" << c << "' la: ";

    if      (isupper(c)) cout << "CHU HOA"        << endl;
    else if (islower(c)) cout << "CHU THUONG"     << endl;
    else if (isdigit(c)) cout << "CHU SO"         << endl;
    else                 cout << "KY TU DAC BIET" << endl;

    return 0;
}
```

**So sánh 2 cách:**

| | So sánh ASCII thủ công | Dùng `<cctype>` |
|---|---|---|
| Dễ đọc | Trung bình | ✅ Rất rõ ràng |
| Dễ sai | ⚠️ Dễ nhầm `'Z'` với `'z'` | ✅ Khó sai |
| Đúng với mọi bảng mã | ❌ Chỉ đúng với ASCII | ✅ Đúng cả với locale khác |

✅ **Nên dùng `<cctype>`** trong code thật. Học cách so sánh ASCII để **hiểu bản chất**.

⚠️ Các hàm này trả về **`int`**, không phải `bool`. `isupper('A')` có thể trả về 1, 2, hay bất kỳ số khác 0 nào. Nên đừng viết `if (isupper(c) == 1)` — cứ viết `if (isupper(c))`.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot chu cai: ";
    cin >> c;

    if (c >= 'a' && c <= 'z') {
        cout << "Chu hoa: " << (char)(c - 32) << endl;
    } else if (c >= 'A' && c <= 'Z') {
        cout << "Chu thuong: " << (char)(c + 32) << endl;
    } else {
        cout << "'" << c << "' khong phai chu cai!" << endl;
    }
    return 0;
}
```

⚠️ **Bắt buộc ép `(char)`**. Nếu viết `cout << c - 32;` thì C++ nâng kết quả lên `int` và in ra **số** (ví dụ 65) thay vì ký tự.

### Bài 7.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot chu cai: ";
    cin >> c;

    if (islower(c)) {
        cout << "Chu hoa: " << (char)toupper(c) << endl;
    } else if (isupper(c)) {
        cout << "Chu thuong: " << (char)tolower(c) << endl;
    } else {
        cout << "'" << c << "' khong phai chu cai!" << endl;
    }
    return 0;
}
```

⚠️ **`toupper` và `tolower` trả về kiểu `int`** (mã ASCII), không phải `char`. Phải ép `(char)` khi in ra, nếu không sẽ thấy số.

```cpp
cout << toupper('a');           // in ra: 65
cout << (char)toupper('a');     // in ra: A
```

💡 **Ưu điểm của `toupper`/`tolower` so với `±32`:** chúng **an toàn** — nếu ký tự không phải chữ cái, hàm trả về nguyên ký tự đó. Trong khi `c - 32` áp dụng mù quáng lên `'5'` sẽ cho ký tự rác.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu so (0-9): ";
    cin >> c;

    if (c < '0' || c > '9') {
        cout << "Khong phai ky tu so!" << endl;
        return 1;
    }

    int so = c - '0';        // '7' - '0' = 55 - 48 = 7

    cout << "Ky tu '" << c << "' -> so " << so << endl;
    cout << so << "^2 = " << so * so << endl;
    return 0;
}
```

**Công thức vàng:**

```cpp
int so = kyTu - '0';          // doi ky tu so -> so nguyen
char kyTu = so + '0';         // doi so nguyen (0-9) -> ky tu so
```

Đây là kỹ thuật dùng **liên tục** khi xử lý chuỗi số ở chương 9.

⚠️ **Sai lầm phổ biến:** `int so = (int)c;` cho ra **55** (mã ASCII) chứ không phải 7. Phải **trừ đi `'0'`**.

### Bài 9.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot chu cai: ";
    cin >> c;

    if (!isalpha(c)) {
        cout << "Khong phai chu cai!" << endl;
        return 1;
    }

    int thuTu = tolower(c) - 'a' + 1;

    cout << "'" << c << "' la chu cai thu " << thuTu
         << " trong bang chu cai" << endl;
    return 0;
}
```

Ví dụ: `C` → 3, `z` → 26, `A` → 1.

**Giải thích công thức:** `tolower(c)` đưa về chữ thường, `- 'a'` cho khoảng cách từ `'a'` (0-based), `+ 1` để đánh số từ 1.

### Bài 10.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot chu cai: ";
    cin >> c;

    if (!isalpha(c)) {
        cout << "Khong phai chu cai!" << endl;
        return 1;
    }

    char doiXung;
    if (isupper(c)) {
        doiXung = 'Z' - (c - 'A');
    } else {
        doiXung = 'z' - (c - 'a');
    }

    cout << c << " <-> " << doiXung << endl;
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

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    int k;

    cout << "Nhap chu cai: ";       cin >> c;
    cout << "Nhap so buoc dich k: "; cin >> k;

    if (!isalpha(c)) {
        cout << "Khong phai chu cai!" << endl;
        return 1;
    }

    // Chuan hoa k ve khoang [0, 25], xu ly duoc ca k am va k rat lon
    k = ((k % 26) + 26) % 26;

    char goc = isupper(c) ? 'A' : 'a';
    char kq  = goc + (c - goc + k) % 26;

    cout << c << " dich " << k << " buoc -> " << kq << endl;
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

**Vì sao cần `((k % 26) + 26) % 26`:** nếu `k` âm (ví dụ −3), `k % 26` trong C++ cho **−3** chứ không phải 23. Cộng 26 rồi lấy dư lần nữa sẽ đưa về đúng khoảng dương.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "'A' = " << (int)'A' << endl;      // 65
    cout << "'a' = " << (int)'a' << endl;      // 97
    cout << "Khoang cach = " << (int)'a' - (int)'A' << endl;   // 32

    cout << "'A' + 32 = " << (char)('A' + 32) << endl;         // a
    cout << "So sanh: " << ('A' + 32 == 'a') << endl;          // 1 (true)

    // Kiem tra voi moi chu cai
    bool dungHet = true;
    for (char c = 'A'; c <= 'Z'; c++) {
        if (c + 32 != c - 'A' + 'a') dungHet = false;
    }
    cout << "Dung voi moi chu cai: " << boolalpha << dungHet << endl;
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

```cpp
c | 32     // doi sang chu THUONG (bat bit 6)
c & ~32    // doi sang chu HOA    (tat bit 6)
c ^ 32     // DAO hoa <-> thuong
```

```cpp
cout << (char)('A' | 32) << endl;    // a
cout << (char)('a' & ~32) << endl;   // A
cout << (char)('A' ^ 32) << endl;    // a
cout << (char)('a' ^ 32) << endl;    // A
```

⚠️ Các mẹo bit này chỉ đúng với **chữ cái**. Áp dụng lên ký tự khác sẽ cho kết quả rác — nên trong code thật vẫn nên dùng `toupper`/`tolower`.

### Bài 13.

```cpp
char c = 'A';
cout << c << endl;              // A
cout << c + 1 << endl;          // 66
cout << (char)(c + 1) << endl;  // B
cout << char(c + 32) << endl;   // a
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
| `cout << c` | `A` | `c` có kiểu `char` → `cout` in ra **ký tự** |
| `cout << c + 1` | `66` | Phép `+` **nâng kiểu** `char` lên `int` (integral promotion). Biểu thức có kiểu `int` → `cout` in ra **số** |
| `cout << (char)(c + 1)` | `B` | Ép ngược về `char` → in ra ký tự có mã 66 |
| `cout << char(c + 32)` | `a` | Tương tự, `char(...)` là cú pháp ép kiểu kiểu hàm |

**Nguyên tắc cốt lõi:** `cout` quyết định in số hay ký tự dựa vào **kiểu của biểu thức**, không phải kiểu của biến gốc.

**Integral promotion:** khi `char` tham gia phép toán số học, nó **tự động được nâng lên `int`**. Đây là quy tắc của C++ nhằm tránh tràn số với kiểu nhỏ.

### Bài 14.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    cout << boolalpha;

    // isspace: dau cach, tab, xuong dong, ...
    cout << "isspace(' ')  = " << (bool)isspace(' ')  << endl;   // true
    cout << "isspace('\\t') = " << (bool)isspace('\t') << endl;  // true
    cout << "isspace('A')  = " << (bool)isspace('A')  << endl;   // false

    // ispunct: dau cau va ky tu dac biet (khong phai chu, so, khoang trang)
    cout << "ispunct('!')  = " << (bool)ispunct('!')  << endl;   // true
    cout << "ispunct('@')  = " << (bool)ispunct('@')  << endl;   // true
    cout << "ispunct('A')  = " << (bool)ispunct('A')  << endl;   // false

    // isxdigit: chu so he 16 (0-9, a-f, A-F)
    cout << "isxdigit('7') = " << (bool)isxdigit('7') << endl;   // true
    cout << "isxdigit('F') = " << (bool)isxdigit('F') << endl;   // true
    cout << "isxdigit('G') = " << (bool)isxdigit('G') << endl;   // false

    // isprint: ky tu in ra duoc (bao gom ca dau cach)
    cout << "isprint('A')  = " << (bool)isprint('A')  << endl;   // true
    cout << "isprint(' ')  = " << (bool)isprint(' ')  << endl;   // true
    cout << "isprint('\\n') = " << (bool)isprint('\n') << endl;  // false

    return 0;
}
```

**Bảng đầy đủ các hàm `<cctype>`:**

| Hàm | Trả về true khi ký tự là |
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

```cpp
#include <iostream>
#include <iomanip>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    cout << "\n+---------------+---------+" << endl;
    cout << "| Ham kiem tra  | Ket qua |" << endl;
    cout << "+---------------+---------+" << endl;

    cout << boolalpha << left;
    cout << "| " << setw(13) << "isalpha" << " | " << setw(7) << (bool)isalpha(c) << " |" << endl;
    cout << "| " << setw(13) << "isdigit" << " | " << setw(7) << (bool)isdigit(c) << " |" << endl;
    cout << "| " << setw(13) << "isalnum" << " | " << setw(7) << (bool)isalnum(c) << " |" << endl;
    cout << "| " << setw(13) << "isupper" << " | " << setw(7) << (bool)isupper(c) << " |" << endl;
    cout << "| " << setw(13) << "islower" << " | " << setw(7) << (bool)islower(c) << " |" << endl;
    cout << "| " << setw(13) << "isspace" << " | " << setw(7) << (bool)isspace(c) << " |" << endl;
    cout << "| " << setw(13) << "ispunct" << " | " << setw(7) << (bool)ispunct(c) << " |" << endl;
    cout << "| " << setw(13) << "isprint" << " | " << setw(7) << (bool)isprint(c) << " |" << endl;
    cout << "+---------------+---------+" << endl;

    cout << "\nMa ASCII : " << (int)c << endl;
    if (isalpha(c)) {
        cout << "Chu hoa  : " << (char)toupper(c) << endl;
        cout << "Chu thuong: " << (char)tolower(c) << endl;
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

⚠️ Ép `(bool)` là cần thiết vì các hàm trả về `int`; không ép thì `boolalpha` không có tác dụng và bạn sẽ thấy số (ví dụ `1024`) thay vì `true`.

⚠️ Lưu ý: `cin >> c` **bỏ qua khoảng trắng**, nên bạn không thể nhập dấu cách để thử `isspace`. Muốn thử, dùng `c = cin.get();` hoặc gán trực tiếp trong code.
