# [STL]. Các Hàm Thông Dụng Của Map Trong C++

Bài viết này mình sẽ hướng dẫn các bạn cách sử dụng các hàm của map, các hàm của map đều rất tối ưu và dễ sử dụng.

**NỘI DUNG :** 

- **Hàm find()**
- **Hàm count()**
- **Hàm erase()**
- **Hàm lower_bound()**
- **Hàm upper_bound()**
- **Video Tutorial**

---

**1. Hàm find()**

Hàm **find()** được sử dụng để tìm giá trị key trong map, độ phức tạp của hàm này là **O(logN)**.

Giá trị trả về của hàm **find()** là iterator, nếu giá trị mà bạn tìm kiếm xuất hiện trong danh sách tập key của map thì hàm này sẽ trả về iterator tới cặp phần tử có key tương ứng, trường hợp key bạn tìm kiếm không xuất hiện trong map thì hàm trả về iterator end() của map.

Hàm này có độ phức tạp rất tốt nên bạn có thể sử dụng map trong các bài toán tìm kiếm nhanh.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    map<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(3, 5));
    map<int, int>::iterator it1 = mp.find(2);
    map<int, int>::iterator it2 = mp.find(5);
    if(it1 != mp.end()){
        cout << "FOUND\n";
    }
    else cout << "NOT FOUND\n";
    if(it2 != mp.end()){
        cout << "FOUND\n";
    }
    else cout << "NOT FOUND\n";
    return 0;
}
```

Output :

```cpp
FOUND
NOT FOUND
```

**2. Hàm count()**

Hàm **count()** trả về số lần xuất hiện của 1 giá trị mà bạn tìm kiếm trong tập các key. Và vì mỗi key trong map chỉ xuất hiện 1 lần nên hàm này trả về 1 nếu key bạn tìm kiếm xuất hiện trong map, ngược lại trả về 0.

Độ phức tạp là **O(logN)** và dễ dùng hơn hàm find() nên bạn có thể sử dụng hàm này để thay thế cho hàm find() trong việc tìm kiếm.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    map<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(3, 5));
    if(mp.count(2) != 0){
        cout << "FOUND\n";
    }
    else cout << "NOT FOUND\n";
    if(mp.count(4) == 1){
        cout << "FOUND\n";
    }
    else cout << "NOT FOUND\n";
    return 0;
}
```

Output :

```cpp
FOUND
NOT FOUND
```

**3. Hàm erase()**

Hàm **erase()** có chức năng xóa 1 cặp phần tử trong map thông qua key, có 2 cách sử dụng hàm này là xóa thông qua giá trị hoặc xóa thông qua iterator.

Độ phức tạp của hàm này là **O(logN)** nhưng khi sử dụng bạn cần hết sức lưu ý nếu bạn xóa 1 key không xuất hiện trong map sẽ gây lỗi.

**Mã nguồn 1 : Xóa thông qua giá trị**

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    map<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(3, 5));
    if(mp.count(2)){
        mp.erase(2);
    }
    cout << "Map sau khi xoa key 2 : \n";
    for(pair<int, int> it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Map sau khi xoa key 2 : 
1 2
3 5
```

**Mã nguồn 2 : Xóa thông qua iterator**

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    map<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(3, 5));
    map<int, int>::iterator it = mp.find(2);
    if(it != mp.end()){
        mp.erase(it);
    }
    cout << "Map sau khi xoa key 2 : \n";
    for(pair<int, int> it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Map sau khi xoa key 2 : 
1 2
3 5
```

**4. Hàm lower_bound()**

Hàm **lower_bound()** ngoài sử dụng với mảng hay vector đã được sắp xếp thì còn có thể áp dụng với set & map. Hàm này trả về iterator tới giá trị nhỏ nhất trong map có key lớn hơn hoặc bằng giá trị tìm kiếm.

Ví dụ map của bạn có tập key là {1, 3, 6, 8, 9, 12} và bạn tìm kiếm giá trị X = 7 thì hàm này sẽ trả về iterator tới phần tử có key là 8 trong map, tương tự nếu bạn tìm X = 3 thì sẽ trả về iterator tới phần tử có key là 3.

Nếu trong trường hợp map của bạn không có key nào lớn hơn hoặc bằng giá trị key tìm kiếm thì hàm trả về iterator end() của map.

Độ phức tạp là **O(logN)** 

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    map<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(3, 3));
    mp.insert(make_pair(5, 5));
    mp.insert(make_pair(6, 8));
    mp.insert(make_pair(10, 12));
    map<int, int>::iterator it1 = mp.lower_bound(4);
    if(it1 == mp.end()){
        cout << "Khong tim thay key >= 4" << endl;
    }
    else{
        cout << "Key nho nhat >= 4 la : " << (*it1).first << endl;
    }
    map<int, int>::iterator it2 = mp.lower_bound(14);
    if(it2 == mp.end()){
        cout << "Khong tim thay key >= 14" << endl;
    }
    else{
        cout << "Key nho nhat >= 14 la : " << (*it2).first << endl;
    }
    return 0;
}
```

Output :

```cpp
Key nho nhat >= 4 la : 5
Khong tim thay key >= 14
```

**5. Hàm upper_bound()**

Tương tự như hàm **lower_bound()** thì hàm** upper_bound() **được dùng để tìm giá trị nhỏ nhất lớn hơn giá trị key mà bạn tìm kiếm.

Ví dụ map của bạn có tập key là {1, 3, 6, 8, 9, 12} và bạn tìm kiếm giá trị X = 7 thì hàm này sẽ trả về iterator tới phần tử có key là 8 trong map, tương tự nếu bạn tìm X = 3 thì sẽ trả về iterator tới phần tử có key là 6.

Nếu trong trường hợp map của bạn không có key nào lớn hơn giá trị key tìm kiếm thì hàm trả về iterator end() của map.

Độ phức tạp là **O(logN)**

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    map<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(3, 3));
    mp.insert(make_pair(5, 5));
    mp.insert(make_pair(6, 8));
    mp.insert(make_pair(10, 12));
    map<int, int>::iterator it1 = mp.upper_bound(5);
    if(it1 == mp.end()){
        cout << "Khong tim thay key > 5" << endl;
    }
    else{
        cout << "Key nho nhat >= 5 la : " << (*it1).first << endl;
    }
    map<int, int>::iterator it2 = mp.upper_bound(14);
    if(it2 == mp.end()){
        cout << "Khong tim thay key > 14" << endl;
    }
    else{
        cout << "Key nho nhat >= 14 la : " << (*it2).first << endl;
    }
    return 0;
}
```

Output :

```cpp
Key nho nhat >= 5 la : 6
Khong tim thay key > 14
```

**Video Tutorial :**
