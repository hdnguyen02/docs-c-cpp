# [STL]. Các Hàm Thông Dụng Của Set Trong C++

Sau khi đã làm quen và có thể sử dụng set ở bài học trước thì mình sẽ tiếp tục hướng dẫn các bạn các hàm phổ biến trong set thông qua các ví dụ trực quan. Thông qua bài học này thì việc sử dụng set sẽ trở nên dễ dàng hơn bao giờ hết.

**NỘI DUNG :** 

- **Hàm find()**
- **Hàm count()**
- **Hàm erase()**
- **Hàm lower_bound()**
- **Hàm upper_bound()**

---

**1. Hàm find()**

Hàm **find()** có chức năng tìm kiếm một phần tử trong set, hàm này rất hiệu quả và dễ dùng.

Hàm này sẽ trả về iterator tới phần tử nếu tìm thấy, ngược lại sẽ trả về iterator **end()** của set

Độ phức tạp : O(logN)

Khi gặp bài toán cần tìm kiếm nhanh bạn có thể nghĩ tới set như một giải pháp tối ưu.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se = {3, 1, 2, 4, 5, 6}; // {1, 2, 3, 4, 5, 6}
    if(se.find(3) != se.end()){
        cout << "3 xuat hien trong set\n";
    }
    else{
        cout << "3 khong xuat hien trong set\n";
    }
    if(se.find(28) != se.end()){
        cout << "28 xuat hien trong set\n";
    }
    else{
        cout << "28 khong xuat hien trong set\n";
    }
}
```

Output :

```cpp
3 xuat hien trong set
28 khong xuat hien trong set
```

---

**2. Hàm count()**

Hàm **count()** trả về số lần xuất hiện của phần tử trong set, do đó hàm này sẽ có giá trị trả về là 0 hoặc 1 tùy theo giá trị đếm có xuất hiện trong set hay không.

Bạn có thể sử dụng hàm count() thay cho hàm find() vì độ phức tạp của chúng là như nhau.

Độ phức tạp : O(logN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se = {3, 1, 2, 4, 5, 6}; // {1, 2, 3, 4, 5, 6}
    if(se.count(3) != 0){
        cout << "3 xuat hien trong set\n";
    }
    else{
        cout << "3 khong xuat hien trong set\n";
    }
    if(se.count(28) != 0){
        cout << "28 xuat hien trong set\n";
    }
    else{
        cout << "28 khong xuat hien trong set\n";
    }
}
```

Output :

```cpp
3 xuat hien trong set
28 khong xuat hien trong set
```

---

**3. Hàm erase()**

Hàm **erase()** giúp bạn có thể xóa một giá trị ra khỏi set, ngoài ra bạn cũng có thể xóa thông qua iterator trỏ tới giá trị đó trong set.

Lưu ý nếu bạn cố xóa 1 phần tử không nằm trong set sẽ gây lỗi, nên trước khi xóa hãy đảm bảo giá trị bạn xóa có mặt trong set

Độ phức tạp : O(logN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se = {3, 1, 2, 4, 5, 6}; // {1, 2, 3, 4, 5, 6}
    //xoa thong qua gia tri
    se.erase(3);
    cout << "Set sau khi xoa 3 :\n";
    for(int x : se){
        cout << x << " ";
    }
    //xoa thong qua iterator
    set<int>::iterator it = se.find(5);
    if(it != se.end()){
        se.erase(it);
    }
    cout << "\nSet sau khi xoa 5 : \n";
    for(int x : se){
        cout << x << " ";
    }
}
```

Output :

```cpp
Set sau khi xoa 3 :
1 2 4 5 6 
Set sau khi xoa 5 : 
1 2 4 6
```

---

**4. Hàm lower_bound()**

Hàm **lower_bound()** trả về iterator tới phần tử có giá trị nhỏ nhất lớn hơn hoặc bằng giá trị cần tìm kiếm.

Trong trường hợp tất cả các phần tử trong set không có phần tử nào lớn hơn hoặc bằng giá trị mà bạn tìm kiếm thì hàm này trả về iterator end() của set.

Độ phức tạp : O(logN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se = {1, 2, 3, 5, 7, 9, 10};
    set<int>::iterator it1 = se.lower_bound(6);
    if(it1 == se.end()){
        cout << "Tat ca phan tu trong set < 6\n";
    }
    else{
        cout << *it1 << " la gia tri nho nhat >= 6\n";
    }
    set<int>::iterator it2 = se.lower_bound(28);
    if(it2 == se.end()){
        cout << "Tat ca phan tu trong set < 28\n";
    }
    else{
        cout << *it2 << " la gia tri nho nhat >= 28\n";
    }
}
```

Output :

```cpp
7 la gia tri nho nhat >= 6
Tat ca phan tu trong set < 28
```

---

**5. Hàm upper_bound()**

Tương tự như lower_bound(), hàm **upper_bound()** trả về iterator tới phần tử có giá trị nhỏ nhất lớn hơn giá trị cần tìm kiếm.

Trong trường hợp tất cả các phần tử trong set không có phần tử nào lớn hơn giá trị mà bạn tìm kiếm thì hàm này trả về iterator end() của set.

Độ phức tạp : O(logN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se = {1, 2, 3, 5, 7, 9, 10};
    set<int>::iterator it1 = se.upper_bound(5);
    if(it1 == se.end()){
        cout << "Tat ca phan tu trong set <= 5\n";
    }
    else{
        cout << *it1 << " la gia tri nho nhat > 5\n";
    }
    set<int>::iterator it2 = se.upper_bound(10);
    if(it2 == se.end()){
        cout << "Tat ca phan tu trong set <= 10\n";
    }
    else{
        cout << *it2 << " la gia tri nho nhat > 10\n";
    }
}
```

Output :

```cpp
7 la gia tri nho nhat > 5
Tat ca phan tu trong set <= 10
```

---

**Video tutorial :**
