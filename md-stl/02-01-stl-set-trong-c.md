# [STL]. Set Trong C++

**Set** trong C++ là một container cực kỳ mạnh mẽ và hiệu quả, đây là là một kiến thức cơ bản trong C++ mà người học cần nắm vững. Bài viết này mình sẽ hướng dẫn các bạn cách sử dụng set trong C++, khi nắm được set trong C++ rồi thì việc học set trong Java, PHP, JS hay Python cũng rất dễ dàng và nhanh chóng.

**NỘI DUNG :** 

- **Tính chất của set trong C++**
- **Một số hàm cơ bản của set**
- **Duyệt set** 
- **Video tutorial** 

---

**1. Tính chất của set trong C++**

**Set** là một container được xây dựng sẵn, bạn cũng có thể gọi nó là cấu trúc dữ liệu hay thư viện cũng được.

Đây là một cấu trúc dữ liệu đã được xây dựng sẵn, để sử dụng bạn cần thêm thư viện set vào chương trình của mình.

Set được cài đặt bởi cấu trúc dữ liệu cây nhị phân tìm kiếm (binary search tree).

Sau đây là những tính chất quan trọng của set mà bạn cần ghi nhớ :

1. Các phần tử trong set có giá trị khác nhau, không có 2 phần tử có cùng giá trị
2. Các phần tử trong set được tự động sắp xếp theo thứ tự tăng dần
3. Tìm kiếm phần tử trong set chỉ mất độ phức tạp O(logN)
4. Set không thể truy cập phần tử thông qua chỉ số như mảng hay vector, string.

Set đặc biệt phù hợp với những bài toán liên quan tới việc loại bỏ giá trị trùng nhau hoặc tìm kiếm nhanh.

Cú pháp khai báo set trong C++ :

```cpp
#include "set"

set<data_type> set_name;
```

---

**2. Một số hàm cơ bản của set**

Mục này mình sẽ hướng dẫn các bạn cách sử dụng set thông qua một vài hàm cơ bản, các hàm quan trọng còn lại mình sẽ để ở bài tiếp theo.

| **Hàm** | **Chức năng** |
| size() | Số lượng phần tử trong set |
| insert() | Thêm phần tử vào trong set |
| empty() | Kiểm tra set rỗng, nếu đúng trả về true, ngược lại trả về false |
| clear() | Xóa toàn bộ phần tử trong set |

Để thêm 1 phần tử vào trong set bạn sử dụng hàm **insert()**, hàm này có độ phức tạp là O(logN) và lưu ý rằng nếu trong set của bạn đã tồn tại giá trị nào đó thì bạn không thể thêm nó vào nữa vì set không thể lưu giá trị trùng nhau.

**Ví dụ 1:** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se; // {}
    se.insert(3); // {3}
    se.insert(1); // {1, 3}
    se.insert(1); // {1, 3}
    se.insert(2); // {1, 2, 3}
    se.insert(3); // {1, 2, 3}
    se.insert(2); // {1, 2, 3}
    se.insert(4); // {1, 2, 3, 4}
    cout << "So luong phan tu trong set : \n";
    cout << se.size() << endl;
}
```

Output :

```cpp
So luong phan tu trong set : 
4
```

**Nhận xét** : Các phần tử trong set không trùng nhau và được sắp xếp theo thứ tự tăng dần

**Ví dụ 2 :**

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<string> se; // {}
    se.insert("tech28"); // {tech28}
    se.insert("c++"); // {c++, tech28}
    se.insert("c++"); // {c++, tech28}
    se.insert("tech28"); // {c++, tech28}
    se.insert("stl"); // {c++, stl, tech28}
    se.insert("stl"); // {c++, stl, tech28}
    se.insert("stl"); // {c++, stl, tech28}
    cout << "So luong phan tu trong set : \n";
    cout << se.size() << endl;
}
```

Output :

```cpp
So luong phan tu trong set : 
3
```

---

**3. Duyệt set**

Để duyệt set bạn có thể dụng range-based for loop hoặc duyệt thông qua iterator, tương tự như vector hay các container khác trong thư viện STL thì set cũng có [iterator](https://blog.codelab.dev/stl-iterator-trong-c)

Nếu bạn chưa rõ range-based for loop có thể tham khảo [tại đây](https://blog.codelab.dev/c-range-based-for-loop-trong-c)

**Ví dụ 1: Duyệt set** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se; // {}
    se.insert(3); // {3}
    se.insert(1); // {1, 3}
    se.insert(1); // {1, 3}
    se.insert(2); // {1, 2, 3}
    se.insert(3); // {1, 2, 3}
    se.insert(2); // {1, 2, 3}
    se.insert(4); // {1, 2, 3, 4}
    cout << "Duyet set bang range-based for loop : \n";
    for(int x : se){
        cout << x << ' ';
    }
    cout << "\nDuyet set bang iterator : \n";
    for(set<int>::iterator it = se.begin(); it != se.end(); ++it){
        cout << *it << " ";
    }
}
```

Output :

```cpp
Duyet set bang range-based for loop : 
1 2 3 4 
Duyet set bang iterator : 
1 2 3 4
```

Truy cập vào các giá trị đặc biệt (nhỏ nhất, lớn nhất) trong set thông qua iterator :

- begin() : Iterator trỏ tới phần tử đầu tiên trong set
- rbegin() : Iterator ngược trỏ tới phần tử cuối cùng trong set

**Ví dụ 2 :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    set<int> se; // {}
    se.insert(3); // {3}
    se.insert(1); // {1, 3}
    se.insert(1); // {1, 3}
    se.insert(2); // {1, 2, 3}
    se.insert(3); // {1, 2, 3}
    se.insert(2); // {1, 2, 3}
    se.insert(4); // {1, 2, 3, 4}
    cout << "Phan tu nho nhat : " << *se.begin() << endl;
    cout << "Phan tu lon nhat : " << *se.rbegin() << endl;
}
```

Output :

```cpp
Phan tu nho nhat : 1
Phan tu lon nhat : 4
```

**Chú ý** : Iterator trong set chỉ hỗ trợ toán tử ++ hoặc -- chứ không hỗ trợ toán tử += và -= như iterator của vector

---

**Video tutorial :**
