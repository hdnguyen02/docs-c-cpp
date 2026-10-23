# [STL]. Các Hàm Thông Dụng Của Lớp Vector

Bài viết này mình sẽ hướng dẫn các bạn sử dụng các hàm phổ biến của lớp vector, vector hỗ trợ các thao tác thêm, chèn, sửa xóa, thay đổi kích thước...

**NỘI DUNG :** 

- **Hàm front(), back(), at()...**
- **Hàm size(), max_size(), ...**
- **Hàm insert(), erase(), assign()...**
- **Video Tutorial** 

---

**1. Hàm Truy Cập Phần Tử**

Để truy cập vào các phần tử trong vector bạn có thể thông qua chỉ số, ngoài ra bạn có thể nhanh chóng truy cập vào phần tử ở đầu và cuối vector.

Tổng hợp các hàm truy cập phần tử trong vector :

| **Toán tử []** | Truy cập phần tử thông qua chỉ số |
| **at(index)** | Truy cập phần tử thông qua chỉ số |
| **front()** | Truy cập phần tử đầu tiên trong vector |
| **back()**
 | Truy cập phần tử cuối cùng trong vector |

**Ví dụ :** 

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v = {100, 200, 300, 400, 500};
    cout << "Duyet vector : \n";
    for(int i = 0; i < 5; i++){
        cout << v.at(i) << " ";
    }
    cout << "\nPhan tu dau tien : " << v.front() << endl;
    cout << "Phan tu cuoi cung : " << v.back() << endl;
}
```

Output :

```cpp
Duyet vector : 
100 200 300 400 500 
Phan tu dau tien : 100
Phan tu cuoi cung : 500
```

---

**2. Hàm Kích Thước**

Vector cung cấp các hàm kiểm tra số lượng phần tử, check rỗng, thay đổi kích thước của vector.

Tổng hợp các hàm liên quan tới kích thước phần tử trong vector :

| **size()** | Trả về kích thước của vector |
| **empty()** | Kiểm tra vector rỗng trả về true, ngược lại trả về false |
| **max_size()** | Trả về kích thước tối đa của vector |
| **resize()** | Thay đổi kích thước của vector |

**Ví dụ :** 

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v = {100, 200, 300, 400, 500};
    cout << "So luong phan tu : " << v.size() << endl;
    cout << "Max size : " << v.max_size() << endl;
    v.resize(3); // {100, 200, 300}
    cout << "So luong phan tu : " << v.size() << endl;
    v.resize(0);
    cout << "Vector rong : " << boolalpha << v.empty() << endl;
}
```

Output :

```cpp
So luong phan tu : 5
Max size : 4611686018427387903
So luong phan tu : 3
Vector rong : true
```

**Chú ý** : Theo kết quả trả về của hàm max_size() thì vector có thể lưu đến 4611686018427387903 phần tử, tuy nhiên đây chỉ là trên lý thuyết. Thông thường thì vector cũng chỉ lưu được số lượng phần tử tương tự như mảng 1 chiều (cỡ 107 phần tử) và còn phụ thuộc vào bộ nhớ cho phép.

---

**3. Hàm Thêm, Chèn, Xóa**

Vector cung cấp các hàm giúp bạn có thể thêm phần tử hoặc xóa phần tử khỏi vector, các hàm này sẽ làm kích thước của vector bị thay đổi theo.

Tổng hợp các hàm thay đổi vector :

| **push_back()** | Thêm phần tử vào cuối vector |
| **emplace_back()** | Thêm phần tử vào cuối vector |
| **pop_back()** | Xóa phần tử cuối cùng trong vector |
| **insert()** | Chèn phần tử vào vị trí bất kỳ trong vector |
| **erase()** | Xóa phần tử khỏi vị trí bất kỳ trong vector |
| **clear()** | Xóa toàn bộ phần tử trong vector |
| **assign()** | Gán giá trị cho phần tử trong vector |
| **swap()** | Hoán đổi 2 vector |

**Hàm push_back(), emplace_back(), pop_back() :** 

Để thêm phần tử vào cuối vector bạn có thể dùng push_back() hoặc emplace_back(), còn để xóa phần tử cuối trong vector bạn dùng pop_back(). Lưu ý rằng khi vector rỗng mà bạn cố tính pop_back() sẽ gây lỗi.

Độ phức tạp : O(1)

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v = {1, 2, 3};
    v.push_back(4);
    v.emplace_back(5);
    v.push_back(6);
    cout << "Duyet vector : \n";
    for(int x : v){
        cout << x << " ";
    }
    v.pop_back();
    cout << "\nDuyet vector : \n";
    for(int x : v){
        cout << x << " ";
    }
}
```

Output :

```cpp
Duyet vector : 
1 2 3 4 5 6 
Duyet vector : 
1 2 3 4 5
```

**Hàm insert() :** 

Hàm insert() giúp bạn chèn phần tử vào chỉ số bất kỳ trong mảng, tuy nhiên bạn phải insert thông qua iterator.

Ví dụ bạn chèn phần tử vào chỉ số 3 thì bạn cần insert thông qua iterator là v.begin() + 3

Độ phức tạp : O(N)

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 4, 5};
    //Chen vao chi so 3
    v.insert(v.begin() + 3, 28);
    cout << "Duyet vector : \n";
    for(int x : v){
        cout << x << " ";
    }
    //Chen vao dau : 
    v.insert(v.begin(), 1000);
    cout << "\nDuyet vector : \n";
    for(int x : v){
        cout << x << " ";
    }
}
```

Output :

```cpp
Duyet vector : 
1 2 3 28 4 5 
Duyet vector : 
1000 1 2 3 28 4 5
```

**Hàm erase() :** 

Tương tự như hàm insert() thì hàm erase() giúp bạn xóa 1 phần tử trong vector thông qua chỉ số của nó.

Bạn cũng cần truyền vào hàm erase() iterator đến phần tử mà bạn cần xóa.

Độ phức tạp : O(N)

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 4, 5};
    //xoa phan tu o chi so 3
    v.erase(v.begin() + 3);
    cout << "Duyet vector : \n";
    for(int x : v){
        cout << x << " ";
    }
    //xoa phan tu o dau
    v.erase(v.begin());
    cout << "\nDuyet vector : \n";
    for(int x : v){
        cout << x << " ";
    }
}
```

Output :

```cpp
Duyet vector : 
1 2 3 5 
Duyet vector : 
2 3 5
```

**Hàm clear() :** 

Hàm clear() giúp xóa toàn bộ phần tử khỏi vector và vector sẽ trở thành rỗng

Độ phức tạp O(N)

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 4, 5};
    v.clear();
    cout << "Vector size : " << v.size() << endl;
    cout << "Vector rong : " << boolalpha << v.empty() << endl;
}
```

Output :

```cpp
Vector size : 0
Vector rong : true
```

**Hàm assign() :**

Hàm assign() giúp bạn gán giá trị toàn bộ các phần tử trong vector hoặc 1 vài phần tử trong vector, bạn cũng có thể gán nội dung của mảng hay vector khác sang vector hiện tại. Hàm này sẽ làm thay đổi kích thước của vector.

Độ phức tạp : O(N)

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v1;
    //Gan 5 phan tu dau tien là 28
    v1.assign(5, 28);
    cout << "Vector v1 : ";
    for(int x : v1){
        cout << x << ' ';
    }
    vector<int> v2;
    //gan 3 phan tu dau tien trong v1 => v2
    v2.assign(v1.begin(), v1.begin() + 3);
    cout << "\nVector v2 : ";
    for(int x : v2){
        cout << x << ' ';
    }
}
```

Output :

```cpp
Vector v1 : 28 28 28 28 28 
Vector v2 : 28 28 28
```

**Hàm swap() :** 

Hàm swap() giúp bạn có thể hoán đổi nội dung của 2 vector.

Độ phức tạp : O(N)

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v1 = {1, 2, 3, 4, 5, 6};
    vector<int> v2 = {100, 200, 300, 400, 500};
    v1.swap(v2);
    cout << "Vector v1 : ";
    for(int x : v1){
        cout << x << " ";
    }
    cout << endl;
    cout << "Vector v2 : ";
    for(int x : v2){
        cout << x << " ";
    }
}
```

Output :

```cpp
Vector v1 : 100 200 300 400 500 
Vector v2 : 1 2 3 4 5 6
```

---

**Video Vector :**
