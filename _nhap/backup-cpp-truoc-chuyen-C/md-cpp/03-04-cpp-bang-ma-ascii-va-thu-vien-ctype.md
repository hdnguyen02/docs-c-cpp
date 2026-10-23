# [C++]. Bảng Mã ASCII Và Thư Viện ctype

**Bảng mã ASCII** là một kiến thức quan trọng mà các bạn cần nắm được để có thể hiểu bản chất về kiểu dữ liệu char trong C++.

**NỘI DUNG :**

- **Bảng Mã ASCII**
- **Các Câu Lệnh Kiểm Tra Loại Ký Tự**
- **Thư Viện Ctype.h**
- **Video Tutorial**

**1.Bảng Mã ASCII**

Bảng mã ASCII chứa 256 ký tự được đánh số từ 0 tới 255 bao gồm các ký tự thường gặp như :

- Chữ cái in hoa, in thường : 'a', 'b', 'c', 'Z', 'X', 'Y'
- Chữ số : '0', '1', '2'...
- Các ký tự đặc biệt : #, @, dấu cách, enter...

![](../images/8e6263ea47af2a4d.png)

Các cụm mã ASCII cần nhớ :

| **Cụm ký tự** | **Mã ASCII** |
| a - z | 97 -> 122 |
| A - Z | 65 -> 90 |
| '0' - '9' | 48 -> 57 |

**Chú ý** : Trong lập trình C++, char được sử dụng để lưu ký tự tuy nhiên nó cũng thể dùng để lưu số nguyên.

Khi tham gia vào các phép toán số học hay sử dụng kiểu char như một số nguyên thì khi đó mã ASCII của kí tự đó sẽ được sử dụng. Xem ví dụ sau bạn sẽ hiểu rõ hơn

Ví dụ 1 : In ra kiểu kí tự char với đặc tả số nguyên, bạn sẽ thu được mã ASCII của kí tự đó

```cpp
#include "iostream"

using namespace std;

int main(){
    char kitu1 = 'A', kitu2 = 'a', kitu3 = '0';
    cout << (int)kitu1 << " " << (int)kitu2 << " " << (int)kitu3 << endl;
    int n = kitu1; // 65
    cout << n << endl;
    cout << kitu1 + 100 << endl;
    return 0;
}
Output : 
65 97 48
65
165
```

Ví dụ 2 : Sử dụng kiểu char với phép toán số học

```cpp
#include "iostream"

using namespace std;

int main(){
    char kitu1 = 'A';
    int n = kitu1 + 10; // 65 + 10 = 75
    cout << n << endl;
    ++kitu1; // 66 => 'B'
    cout << (int)kitu1 << endl;
    cout << kitu1 << endl;
    return 0;
}
Output : 
75
66
B
```

---

**2. Các Câu Lệnh Kiểm Tra Loại Ký Tự**

Khi làm việc với ký tự hay chuỗi ký tự bạn thường xuyên phải kiểm tra loại ký tự xem nó là in hoa, in thường, chữ số hay chuyển đổi qua lại giữa chữ hoa và chữ thường.

Trong C++ đã có các hàm xử lý các yêu cầu này nhưng để hiểu bản chất của vấn đề các bạn nên tự viết được câu lệnh kiểm tra loại ký tự cho riêng mình.

**Kiểm tra kí tự in thường :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = 'u';
    //Cách 1
    if(c >= 'a' && c <= 'z'){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    //Cách 2 
    if(c >= 97 && c <= 122){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    return 0;
}

```

**Kiểm tra kí tự in hoa :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = 'u';
    //Cách 1
    if(c >= 'A' && c <= 'Z'){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    //Cách 2 
    if(c >= 65 && c <= 90){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    return 0;
}
```

**Kiểm tra chữ cái :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = 'Z';
    if((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    return 0;
}
```

**Kiểm tra chữ số :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = '5';
    //Cách 1
    if(c >= '0' && c <= '9'){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    if(c >= 48 && c <= 57){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    return 0;
}
```

**Chuyển đổi in hoa, in thường :** 

Chữ cái in hoa có mã ASCII nhỏ hơn chữ cái in thường tương ứng với nó 32 đơn vị, ví dụ 'A' - 65 và 'a' - 97. Vì thế muốn chuyển in hoa thành in thường bạn chỉ cần cộng thêm 32 đơn vị vào ký tự in thường.

Ngược lại nếu bạn có ký tự in thường và muốn chuyển thành in hoa bạn sẽ trừ đi 32 đơn vị.

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = 'A';
    c += 32;
   	cout << c << endl;
    char kitu = 'z';
    kitu -= 32;
    cout << kitu << endl;
    return 0;
}
Output : 
a
Z
```

**3. Thư Viện Ctype.h**

Ngôn ngữ C++ đã cung cấp cho bạn các hàm có sẵn với mục đích kiểm tra loại ký tự, bạn có thể sử dụng hàm có sẵn nếu đã thành thạo các câu lệnh ở mục 2.

Các hàm này nằm trong thư viện

| **Hàm** | **Chức năng** |
| int islower(char c) | Trả về 1 (true) nếu c là chữ cái in thường, ngược lại trả về 0 (false) |
| int isupper(char c)  | Trả về 1 (true) nếu c là chữ cái in hoa, ngược lại trả về 0 (false) |
| int isalpha(char c) | Trả về 1 (true) nếu c là chữ cái, ngược lại trả về 0 (false) |
| int isdigit(char c) | Trả về 1 (true) nếu c là chữ số, ngược lại trả về 0 (false) |
| int isalnum(char c) | Trả về 1 (true) nếu c là chữ số hoặc chữ cái, ngược lại trả về 0 (false) |
| int tolower(char c) | Trả về mã ascii tương ứng của kí tự in thường của c |
| int toupper(char c) | Trả về mã ascii tương ứng của kí tự in hoa của c |

Ví dụ 1 : Kiểm tra chữ in hoa in thường

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = 'A', d = 'z';
    if(isupper(c)){ // bạn viết là isupper(c) == 1 cũng được
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    if(islower(d)){
        cout << "YES\n";
    }
    else{
        cout << "NO\n";
    }
    return 0;
}
Output :
YES
YES
```

Ví dụ 2 : Chuyển đổi in hoa, thường

```cpp
#include "iostream"

using namespace std;

int main(){
    char c = 'A', d = 'z';
    c = tolower(c);
    d = toupper(d);
    cout << c << " " << d << endl;
    return 0;
}
Output : 
a Z
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/03-04-cpp-bang-ma-ascii-va-thu-vien-ctype.md](solutions/03-04-cpp-bang-ma-ascii-va-thu-vien-ctype.md)

**Bài 1.** Nhập một ký tự, in ra mã ASCII của nó.

**Bài 2.** Nhập một số nguyên từ 0–127, in ra ký tự tương ứng trong bảng ASCII.

**Bài 3.** In ra bảng ASCII từ mã 33 đến 126, mỗi dòng 8 ký tự theo dạng `ma:kytu`.

**Bài 4.** Nhập một ký tự, dùng **so sánh mã ASCII** (không dùng thư viện `ctype`) để kiểm tra nó là chữ hoa, chữ thường, chữ số hay ký tự đặc biệt.

**Bài 5.** Làm lại bài 4 nhưng dùng các hàm `isupper`, `islower`, `isdigit`, `isalpha` của `ctype`.

**Bài 6.** Nhập một chữ cái, chuyển nó thành chữ hoa (nếu đang thường) hoặc chữ thường (nếu đang hoa), bằng **phép toán với mã ASCII** (cộng/trừ 32).

**Bài 7.** Làm lại bài 6 bằng `toupper` và `tolower`.

**Bài 8.** Nhập một ký tự số (`'0'`–`'9'`), đổi nó thành giá trị số nguyên tương ứng rồi in ra bình phương của nó.

**Bài 9.** Nhập một chữ cái, in ra nó là chữ cái thứ mấy trong bảng chữ cái tiếng Anh (A/a = 1, …, Z/z = 26).

**Bài 10.** Nhập một ký tự chữ cái, in ra ký tự đối xứng của nó trong bảng chữ cái (A↔Z, B↔Y, C↔X…).

**Bài 11.** Viết chương trình mã hoá Caesar cho **một ký tự**: nhập một chữ cái và số bước dịch `k`, in ra ký tự sau khi dịch (có xoay vòng Z→A).

**Bài 12.** Giải thích vì sao `'A' + 32 == 'a'`. Con số 32 đến từ đâu? Viết chương trình chứng minh.

**Bài 13.** Chương trình sau in ra gì? Giải thích:

```cpp
char c = 'A';
cout << c << endl;
cout << c + 1 << endl;
cout << (char)(c + 1) << endl;
cout << char(c + 32) << endl;
```

**Bài 14.** Tìm hiểu các hàm `isspace`, `ispunct`, `isxdigit`, `isprint` của `ctype`. Viết chương trình minh hoạ từng hàm.

**Bài 15.** Nhập một ký tự, in ra một bảng đầy đủ kết quả của 8 hàm kiểm tra `ctype` (`isalpha`, `isdigit`, `isalnum`, `isupper`, `islower`, `isspace`, `ispunct`, `isprint`) dưới dạng `true`/`false`.
