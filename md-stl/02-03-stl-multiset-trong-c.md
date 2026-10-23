# [STL]. Multiset Trong C++

**Multiset** trong C++ là một container tương tự như set nhưng có thể lưu các giá trị trùng nhau, bài học này mình sẽ hướng dẫn các bạn sử dụng multiset cũng như một vài lưu ý khi sử dụng các hàm trong multiset.

**NỘI DUNG :** 

- **Multiset trong C++**
- **Hàm find(), count(), erase() trong multiset**
- **Video tutorial** 

---

**1. Multiset trong C++**

**Multiset** trong C++ cũng được cài đặt bằng cấu trúc dữ liệu cây nhị phân tìm kiếm (binary search tree) tương tự như set, đặc điểm khác biệt nhất so với set đó là nó có thể lưu trữ các giá trị trùng nhau.

Các tính chất của multiset :

- Các phần tử trong multiset có thứ tự mặc định theo thứ tự tăng dần
- Các phần tử trong multiset có thể trùng nhau
- Các phần tử trong multiset không thể thay đổi, chỉ có thể xóa hoặc thêm vào
- Multiset không hỗ trợ truy cập phần tử thông qua chỉ số

**Ví dụ :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    multiset<int> ms;
    ms.insert(3);
    ms.insert(1);
    ms.insert(3);
    ms.insert(2);
    ms.insert(2);
    ms.insert(3);
    ms.insert(4);
    cout << "So phan tu trong multiset : " << ms.size() << endl;
    cout << "Cac phan tu trong multiset :\n";
    for(int x : ms){
        cout << x << ' ';
    }
}
```

Output :

```cpp
So phan tu trong multiset : 7
Cac phan tu trong multiset :
1 2 2 3 3 3 4
```

---

**2. Hàm find(), count(), erase() trong multiset**

Các hàm của multiset tương tự như set tuy nhiên có sự khác nhau về 3 hàm là **find()**,** count() **và** erase()**.

**Hàm find() :** 

Hàm này sẽ trả về iterator tới vị trí đầu tiên của phần tử trong multiset nếu giá trị tìm kiếm xuất hiện, ngược lại sẽ trả về iterator end()

Ví dụ trong mã nguồn dưới đây bạn sẽ thấy hàm find() trả về vị trí đầu tiên của số 3 trong multiset.

**Ví dụ 1 :** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    multiset<int> ms = {1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4};
    multiset<int>::iterator it = ms.find(3);
    if(it != ms.end()){
        cout << "3 xuat hien trong multiset\n";
        cout << "Vi tri dau tien cua 3 trong multiset : " << distance(ms.begin(), it) << endl;
    }
    else{
        cout << "3 khong xuat hien trong multiset\n";
    }
}
```

Output :

```cpp
3 xuat hien trong multiset
Vi tri dau tien cua 3 trong multiset : 5
```

**Hàm count() :** 

Hàm count() trong set chỉ trả về giá trị là 0 hoặc 1 nhưng do multiset có thể lưu giá trị trùng nhau nên hàm count() trong multiset có thể trả về 0 hoặc 1 số khác 0, tương ứng số lần xuất hiện của giá trị đó trong multiset.

**Ví dụ 2:** 

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    multiset<int> ms = {1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4};
    cout << "So lan xuat hien cua 3 : " << ms.count(3) << endl;
    cout << "So lan xuat hien cua 28 : " << ms.count(28) << endl;
    cout << "So lan xuat hien cua 1 : " << ms.count(1) << endl;
}
```

Output :

```cpp
So lan xuat hien cua 3 : 5
So lan xuat hien cua 28 : 0
So lan xuat hien cua 1 : 3
```

**Hàm erase() :** 

Khi sử dụng hàm erase() bạn cần lưu ý nếu bạn xóa thông qua giá trị thì nó sẽ xóa hết mọi phần tử có cùng giá trị đó, ngược lại nếu bạn chỉ muốn xóa 1 phần tử có giá trị đó trong multiset thì bạn cần xóa thông qua iterator.

Tương tự như trong set bạn cần đảm bảo rằng giá trị bạn xóa tồn tại trong multiset

**Ví dụ 3** : Xóa phần tử thông qua giá trị

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    multiset<int> ms = {1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4};
    cout << "Multiset ban dau : \n";
    for(int x : ms){
        cout << x << " ";
    }
    ms.erase(3);
    cout << "\nMultiset sau khi xoa 3 : \n";
    for(int x : ms){
        cout << x << " ";
    }
}
```

Output :

```cpp
Multiset ban dau : 
1 1 1 2 2 3 3 3 3 3 4 
Multiset sau khi xoa 3 : 
1 1 1 2 2 4
```

**Ví dụ 4** : Xóa thông qua iterator

```cpp
#include "iostream"
#include "algorithm"
#include "set"

using namespace std;

int main(){
    multiset<int> ms = {1, 1, 1, 2, 2, 3, 3, 3, 3, 3, 4};
    cout << "Multiset ban dau : \n";
    for(int x : ms){
        cout << x << " ";
    }
    multiset<int>::iterator it = ms.find(3);
    ms.erase(it);
    cout << "\nMultiset sau khi xoa 3 : \n";
    for(int x : ms){
        cout << x << " ";
    }
}
```

Output :

```cpp
Multiset ban dau : 
1 1 1 2 2 3 3 3 3 3 4 
Multiset sau khi xoa 3 : 
1 1 1 2 2 3 3 3 3 4
```

---

**Video tutorial :**
