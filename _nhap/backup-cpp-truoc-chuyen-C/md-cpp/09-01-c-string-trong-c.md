# [C++]. String Trong C++

**String** trong C++ là một lớp chuyên được sử dụng để xử lý xâu ký tự thay cho mảng char, bạn vẫn có thể lưu xâu bằng mảng ký tự tuy nhiên nó không hỗ trợ nhiều hàm như string.

**NỘI DUNG :** 

- **String** 
- **Duyệt String**
- **Nhập Xâu Ký Tự Từ Bàn Phím**
- **Video Tutorial** 

---

**1. String**

**String** trong C++ được sử dụng để lưu chuỗi (xâu) ký tự, nó như một mảng char động, có thể thay đổi kích thước một cách linh hoạt cũng như hỗ trợ chèn, xóa, sửa đổi...

Khai báo string bạn có thể khai báo một xâu ký tự rỗng hoặc xâu có sẵn nội dung :

**Cú pháp :** 

```markup
//Khai báo xâu rỗng
string name_string; 

//Khai báo xâu rỗng
string name_string = "";

//Khai báo xâu có nội dung 
string name_string = "data";
```

Bạn có thể khai báo string, in ra màn hình nội dung string và sử dụng hàm size() để in ra số lượng ký tự trong string.

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s1;
    string s2 = "";
    string s3 = "codelab";
    cout << "Noi dung s1 : " << s1 << endl;
    cout << "So luong ky tu s1 : " << s1.size() << endl;
    cout << "Noi dung s2 : " << s2 << endl;
    cout << "So luong ky tu s2 : " << s2.size() << endl;
    cout << "Noi dung s3 : " << s3 << endl;
    cout << "So luong ky tu s3 : " << s3.size() << endl;
}
```

Output :

```cpp
Noi dung s1 : 
So luong ky tu s1 : 0
Noi dung s2 : 
So luong ky tu s2 : 0
Noi dung s3 : codelab
So luong ky tu s3 : 6
```

---

**2. Duyệt String**

String tương tự như 1 mảng động, bạn có thể truy xuất các phần tử (ký tự) trong xâu thông qua chỉ số được đánh từ 0.

Nếu bạn muốn duyệt từng ký tự trong string thì bạn có thể dùng 3 cách :

- Duyệt thông qua chỉ số
- Duyệt bằng ranged-base for loop
- Duyệt bằng Iterator

Ví dụ string s = "codelab!@#" :

| **s[index]** | 2 | 8 | t | e | c | h | ! | @ | # |
| **index** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |

**Duyệt string bằng chỉ số :** 

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s = "codelab!@#";
    for(int i = 0; i < (int)s.size(); i++){
        cout << "s[" << i << "] = " << s[i] << endl;
    }
}
```

Output :

```cpp
s[0] = 2
s[1] = 8
s[2] = t
s[3] = e
s[4] = c
s[5] = h
s[6] = !
s[7] = @
s[8] = #
```

**Duyệt bằng ranged-base for loop :** 

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s = "codelab!@#";
    for(char x : s){
        cout << x << ' ';
    }
}
```

Output :

```cpp
2 8 t e c h ! @ #
```

**Duyệt bằng iterator**

Tương tự vector như thì bạn cũng có thể dùng iterator để duyệt qua string. Nếu bạn chưa nắm rõ về iterator có thể tham khảo kiến thức này [tại đây](https://blog.codelab.dev/stl-iterator-trong-c)

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s = "codelab!@#";
    for(string::iterator it = s.begin(); it != s.end(); ++it){
        cout << *it << ' ';
    }
}
```

Output :

```cpp
2 8 t e c h ! @ #
```

---

**3. Nhập Xâu Ký Tự Từ Bàn Phím**

Trong trường hợp xâu ký tự của bạn không chứa khoảng trắng (dấu cách, tab) thì bạn có thể dùng cin.

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s;
    cout << "Nhap xau s : ";
    cin >> s;
    cout << "Xau vua nhap : " << s << endl;
    return 0;
}
```

Khi bạn muốn đọc xâu ký tự đến hết dòng (đọc hết cả dấu cách, tab) thì bạn cần dùng hàm **getline()**

**Cú pháp** :

```cpp
getline(cin, string, delimiter);
```

Nếu getline() không có tham số thứ 3 thì mặc định nó sẽ là dấu enter.

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s;
    cout << "Nhap xau s : \n";
    getline(cin, s);
    cout << "Xau vua nhap : " << s << endl;
    return 0;
}
```

Input và output :

```cpp
input : 
codelab C++ string
Output : 
Xau vua nhap : codelab C++ string
```

Trong trường hợp bạn thêm tham số thứ 3 cho getline() thì nó sẽ đọc từ luồng cin cho tới khi gặp kí tự là tham số thứ 3 mà bạn truyền vào hàm.

```cpp
#include "iostream"
#include "string"
using namespace std;

using ll = long long;

int main(){
    string s;
    cout << "Nhap xau s : \n";
    getline(cin, s, ',');
    cout << "Xau vua nhap : " << s << endl;
    return 0;
}
```

Input và output :

```cpp
input : 
codelab.C++,string
output : 
Xau vua nhap : codelab.C++
```

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-01-c-string-trong-c.md](solutions/09-01-c-string-trong-c.md)

**Bài 1.** Khai báo `string` theo 4 cách khác nhau và in ra.

**Bài 2.** Nhập họ tên đầy đủ (có dấu cách) bằng `getline` rồi in ra độ dài chuỗi.

**Bài 3.** Duyệt và in từng ký tự của chuỗi theo 3 cách: chỉ số, `at()`, range-based for.

**Bài 4.** Đếm số ký tự chữ cái, chữ số, dấu cách và ký tự đặc biệt trong chuỗi.

**Bài 5.** Nối 2 chuỗi bằng `+`, `+=` và `append()`. So sánh 3 cách.

**Bài 6.** Đảo ngược chuỗi bằng 3 cách: vòng lặp, `reverse()`, đệ quy.

**Bài 7.** Kiểm tra chuỗi có đối xứng (palindrome) không, bỏ qua hoa/thường và dấu cách.

**Bài 8.** Đếm số từ trong một câu (các từ cách nhau bằng dấu cách).

**Bài 9.** In ra từ dài nhất và từ ngắn nhất trong câu.

**Bài 10.** Cắt chuỗi con bằng `substr()`: lấy 5 ký tự đầu, 5 ký tự cuối, và ký tự thứ 3–7.

**Bài 11.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
string s = "codelab";
cout << s[10];
cout << s.at(10);
```

**Bài 12.** So sánh `string` của C++ với mảng `char[]` của C. Lập bảng ưu nhược điểm.

**Bài 13.** Đọc nhiều dòng văn bản tới khi gặp dòng trống, đếm tổng số ký tự.

**Bài 14.** Viết hàm cắt khoảng trắng thừa ở đầu và cuối chuỗi (trim).

**Bài 15.** Viết chương trình "đếm từ" đơn giản: nhập một đoạn văn, in ra số dòng, số từ, số ký tự (giống lệnh `wc` của Linux).
