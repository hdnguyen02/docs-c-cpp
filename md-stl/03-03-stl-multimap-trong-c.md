# [STL]. Multimap Trong C++

Bài viết này mình sẽ hướng dẫn bạn sử dụng **multimap**, một container tương tự như map nhưng có thể lưu key trùng nhau.

**NỘI DUNG :** 

- **Multimap trong C++**
- **Hàm find(), erase(), find() trong multimap**
- **Video tutorial** 

---

**1. Multimap trong C++**

Tương tự như map thì **multimap** cũng lưu các phần tử là cặp key - value, nó có các hàm tương tự như **map** nhưng có 1 vài điểm khác biệt khi sử dụng.

Multimap vẫn lưu các phần tử theo thứ tự key tăng dần nhưng các key có thể trùng nhau. Và vì các key có thể trùng nhau nên multimap không hỗ trợ việc bạn truy cập value thông qua key bằng cú pháp map[key] như map.

Các tính chất của multimap :

- Các phần tử trong map có thể có key trùng nhau
- Multimap lưu các phần tử theo thứ tự tăng dần về key
- Multimap không hỗ trợ truy cập value thông qua key bằng cú pháp map[key]
- Multimap không hỗ trợ chỉ số như mảng hay vector mà chỉ số của multimap chính là key

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    multimap<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(1, 3));
    mp.insert(make_pair(1, 4));
    mp.insert(make_pair(2, 2));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(2, 4));
    mp.insert(make_pair(3, 1));
    mp.insert(make_pair(3, 1));
    cout << "Map size : " << mp.size() << endl;
    for(pair<int, int> it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Map size : 8
1 2
1 3
1 4
2 2
2 3
2 4
3 1
3 1
```

**2. Hàm find(), erase(), count() trong multimap**

Về độ phức tạp của 3 hàm **find()**,** erase()** và** count() **trong multimap thì tương tự như map là O(logN). Tuy nhiên có một vài điểm khác biệt các bạn cần lưu ý.

**Hàm find() :**

Do **multimap** có thể lưu trữ nhiều cặp phần tử có cùng key nên khi bạn tìm kiếm key sử dụng hàm **find()** thì sẽ trả về iterator tới cặp phần tử đầu tiên có key tương ứng trong map.

Ví dụ multimap đang lưu các cặp phần tử {(1, 2), (1, 3), (2, 3), (2, 1), (2, 4), (5, 6)) và bạn tìm kiếm key là 2 thì hàm find() sẽ trả về iterator tới cặp phần tử (2, 3) là cặp phần tử có key 2 xuất hiện đầu tiên trong map.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    multimap<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(1, 3));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(2, 1));
    mp.insert(make_pair(2, 4));
    mp.insert(make_pair(5, 6));
    multimap<int, int>::iterator it = mp.find(2);
    cout << (*it).first << " " << (*it).second << endl;
    return 0;
}
```

Output :

```cpp
2 3
```

**Hàm erase() :** 

Hàm **erase()** nếu bạn xóa thông qua giá trị của key sẽ xóa toàn bộ cặp phần tử có key tương ứng trong multimap. Để xóa đi 1 cặp phần tử duy nhất thì bạn nên xóa thông qua iterator.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    multimap<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(1, 3));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(2, 1));
    mp.insert(make_pair(2, 4));
    mp.insert(make_pair(5, 6));
    mp.erase(2);
    cout << "Map sau khi xoa : \n";
    for(pair<int, int> it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Map sau khi xoa : 
1 2
1 3
5 6
```

**Hàm count() :** 

Hàm **count()** trong multimap khi bạn sử dụng để đếm số lần xuất hiện của key trả về giá trị tương ứng với số cặp phần tử có key tương ứng. Nếu key bạn đếm không xuất hiện thì hàm này trả về 0.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    multimap<int, int> mp;
    mp.insert(make_pair(1, 2));
    mp.insert(make_pair(1, 3));
    mp.insert(make_pair(2, 3));
    mp.insert(make_pair(2, 1));
    mp.insert(make_pair(2, 4));
    mp.insert(make_pair(5, 6));
    cout << "Key 2 xuat hien : " << mp.count(2) << " lan\n";
    cout << "key 28 xuat hien : " << mp.count(28) << " lan\n";
    return 0;
}
```

Output :

```cpp
Key 2 xuat hien : 3 lan
key 28 xuat hien : 0 lan
```

**Video tutorial :**
