# [STL]. Unordered_map Trong C++

**Unordered_map** là một associative container được bổ sung cho map và multimap với sự cải thiện về tốc độ của các hàm như find(), count(), erase().

**NỘI DUNG :** 

- **Unordered_map trong C++**
- **Các hàm find(), count(), erase()** 
- **Video tutorial** 

---

**1. Unordered_map trong C++**

Tương tự như map thì **unordered_map** được sử dụng để lưu trữ dữ liệu theo cặp key - value. Các hàm của map thì **unordered_map** đều có nhưng khác nhau về độ phức tạp.

**unordered_map** được cài đặt bởi cấu trúc dữ liệu bảng băm - hash table. Bạn cần thêm thư viện "unordered_map" vào để có thể sử dụng container này.

Các tính chất của unordered_map :

- unordered_map lưu trữ phần tử với các key là riêng biệt
- Các phần tử trong unordered_map không có thứ tự

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"
#include "unordered_map"

using namespace std;

int main(){
    unordered_map<string, string> mp;
    mp["codelab"] = "codelab.dev";
    mp["USA"] = "Trump";
    mp["Russia"] = "Putin";
    for(pair<string, string> it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Russia Putin
USA Trump
codelab codelab.dev
```

**2. Các hàm find(), count(), erase()**

Cách dùng 3 hàm phổ biến này của unordered_map tương tự như map, điều khác biệt duy nhất đó là vì unordered_map được cài đặt bởi bẳng băm thay vì cây đỏ đen Red-black tree như map nên sẽ có sự khác nhau về độ phức tạp.

Độ phức tạp trung bình của 3 hàm này là **O(1)**, tuy nhiên trong trường hợp tệ nhất (Worst case) thì nó có thể là** O(N)**.

Hàm insert trong unordered_map cũng tương tự như vậy về độ phức tạp.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"
#include "unordered_map"

using namespace std;

int main(){
    unordered_map<string, string> mp;
    mp["codelab"] = "codelab.dev";
    mp["USA"] = "Trump";
    mp["Russia"] = "Putin";
    mp.erase("USA");
    for(pair<string, string> it : mp){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Russia Putin
codelab codelab.dev
```

**Video tutorial :**
