# [C++]. Các Hàm String Xử Lý Xâu Trong C++

Các hàm xử lý xâu trong C++ bao gồm có chèn, xóa, nối xâu, tìm kiếm... Trong bài viết này mình sẽ hướng dẫn các bạn các hàm xử lý xâu thông dụng trong C++ thông qua ví dụ trực quan.

**NỘI DUNG :** 

- **Hàm push_back() và pop_back()**
- **Hàm append()**
- **Hàm insert()**
- **Hàm erase()**
- **Hàm substr()**
- **Hàm find()** 

---

**1. Hàm push_back() và pop_back()** 

Hàm **push_back()** sẽ thêm 1 ký tự vào cuối string và **pop_back()** sẽ xóa đi ký tự cuối cùng trong string.

Lưu ý là hàm này sẽ thêm 1 ký tự chứ không phải là thêm 1 chuỗi ký tự, nếu bạn cố tính push_back 1 chuỗi ký tự sẽ gây lỗi.

Độ phức tạp của 2 hàm này đều là O(1)

**Ví dụ :** 

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab";
    s.push_back('@');
    cout << s << endl;
    s.push_back('#');
    cout << s << endl;
    s.pop_back();
    cout << s << endl;
}
```

Output :

```cpp
codelab@
codelab@#
codelab@
```

---

**2. Hàm append()**

Hàm **append()** có chức năng nối chuỗi hoặc nối ký tự vào cuối của string. Bạn có thể lựa chọn nối toàn bộ chuỗi khác vào chuỗi hiện tại hoặc nối 1 vài ký tự liên tiếp của xâu khác vào xâu hiện tại.

Độ phức tạp : O(N)

**Ví dụ :** 

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab";
    //Nối toàn bộ xâu
    s.append("blog");
    cout << s << endl;
    string t = "0123456789";
    //Nối 5 kí tự tính từ chỉ số 1 của xâu t vào s
    s.append(t, 1, 5);
    cout << s << endl;
}
```

Output :

```cpp
codelabblog
codelabblog12345
```

Có một cách khác để nối chuỗi nhanh hơn trong string đó là sử dụng toán tử **+=**, toán tử này khi áp dụng với string sẽ tương đương phép nối xâu.

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab";
    //Nối toàn bộ xâu
    s += " blog";
    cout << s << endl;
    //Nối 1 ký tự
    s += '@';
    cout << s << endl;
    s += " C++";
    cout << s << endl;
}
```

Output :

```cpp
codelab blog
codelab blog@
codelab blog@ C++
```

---

**3. Hàm insert()**

Hàm **insert()** giúp bạn chèn một xâu khác vào vị trí bất kỳ trong xâu hiện tại thông qua chỉ số chèn.

**Cú pháp** : s.insert(index, string t);

Trong đó xâu t được chèn vào chỉ số index của xâu s, hàm này có tương đối nhiều cách dùng tuy nhiên chèn vào vị trí xác định trong xâu là phổ biến nhất.

Độ phức tạp : O(N)

**Ví dụ :** 

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab";
    //Chen vao chi so 2 cua xau s 
    s.insert(2, "####");
    cout << s << endl;
    //Chen vao dau xau s
    s.insert(0, "blog ");
    cout << s << endl;
}
```

Output :

```cpp
28####tech
blog 28####tech
```

---

**4. Hàm erase**

Hàm **erase()** giúp bạn có thể xóa đi 1 vài ký tự của xâu hiện tại thông qua chỉ số.

**Cú pháp :**

- s.erase(pos) : Xóa tất cả các ký tự trong xâu s từ chỉ số pos tới cuối xâu
- s.erase(pos, n) : Xóa n ký tự trong xâu s tính từ chỉ số pos

Độ phức tạp : O(N)

**Ví dụ :** 

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab.dev";
    //Xoa tu chi so 6 toi het xau
    s.erase(6);
    cout << s << endl;
    string t = "codelab.dev";
    //Xoa 4 ki tu tinh tu chi so 2
    t.erase(2, 4);
    cout << t << endl;
}
```

Output :

```cpp
codelab
28.com.vn
```

---

**5. Hàm substr()**

Hàm **substr()** giúp bạn có thể tách xâu con của xâu hiện tại, hàm này trả về xâu con tách được.

**Cú pháp :** 

- s.substr(pos) : Trả về xâu con của xâu s tính từ chỉ số pos
- s.substr(pos, n) : Trả về xâu con gồm n ký tự tính từ chỉ số pos của xâu s

Độ phức tạp : O(N)

**Ví dụ :** 

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab.dev";
    //Xau con tu chi so 2 toi het xau
    string sub1 = s.substr(2);
    cout << sub1 << endl;
    string t = "codelab.dev";
    //Xau con tu chi so 0 co do dai 6
    string sub2 = t.substr(0, 6);
    cout << sub2 << endl;
}
```

Output :

```cpp
tech.com.vn
codelab
```

---

**6. Hàm find()**

Hàm **find()** giúp bạn tìm kiếm sự xuất hiện của xâu con trong xâu hiện tại.

Hàm này sẽ trả về chỉ số đầu tiên của xâu con nếu xâu này tồn tại trong xâu đang tìm kiếm, ngược lại sẽ trả về giá trị là **string::npos** 

Độ phức tạp : O(N)

**Ví dụ :** 

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
    string s = "codelab.dev codelab";
    if(s.find("codelab") == string::npos){
        cout << "NOT FOUND\n";
    }
    else{
        cout << "FOUND\n";
        cout << s.find("codelab");
    }
}
```

Output :

```cpp
FOUND
0
```

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-03-c-cac-ham-string-xu-ly-xau-trong-c.md](solutions/09-03-c-cac-ham-string-xu-ly-xau-trong-c.md)

**Bài 1.** Dùng `length()`, `empty()`, `clear()`, `size()` trên một chuỗi và in kết quả từng bước.

**Bài 2.** Dùng `find()` tìm vị trí xuất hiện đầu tiên của một chuỗi con. Xử lý trường hợp không tìm thấy.

**Bài 3.** Đếm số lần xuất hiện của một chuỗi con trong chuỗi mẹ.

**Bài 4.** Tìm tất cả vị trí xuất hiện của một ký tự trong chuỗi.

**Bài 5.** Dùng `replace()` thay thế một đoạn chuỗi. Viết hàm thay thế **tất cả** các lần xuất hiện.

**Bài 6.** Dùng `insert()` chèn chuỗi vào giữa, đầu, cuối chuỗi khác.

**Bài 7.** Dùng `erase()` xoá một đoạn chuỗi, xoá một ký tự, xoá từ vị trí đến hết.

**Bài 8.** Dùng `substr()` tách họ, tên đệm, tên từ chuỗi họ tên đầy đủ.

**Bài 9.** Dùng `rfind()` tìm vị trí xuất hiện **cuối cùng**. Áp dụng để lấy phần mở rộng của tên file.

**Bài 10.** Dùng `find_first_of()`, `find_last_of()`, `find_first_not_of()` và giải thích khác biệt.

**Bài 11.** Viết hàm tách chuỗi theo dấu phân cách (split) trả về `vector<string>`.

**Bài 12.** Viết hàm nối một `vector<string>` thành chuỗi với dấu phân cách (join).

**Bài 13.** Dùng `compare()` so sánh 2 chuỗi. So sánh với toán tử `==`, `<`.

**Bài 14.** Viết hàm kiểm tra chuỗi có bắt đầu / kết thúc bằng một chuỗi con cho trước.

**Bài 15.** Viết một "thư viện xử lý chuỗi" gồm: `trim`, `split`, `join`, `replaceAll`, `toUpper`, `toLower`, `startsWith`, `endsWith`, `contains`.
