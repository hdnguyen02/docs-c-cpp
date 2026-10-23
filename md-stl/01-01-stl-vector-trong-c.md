# [STL]. Vector Trong C++

**Vector** trong C++ là một container kiểu mảng động, tương tự như mảng nhưng linh hoạt và hỗ trợ nhiều hàm có sẵn. Sử dụng thành thạo vector là kỹ năng cần thiết khi bạn học lập trình C++, bài viết này mình sẽ hướng dẫn bạn cách tạo và sử dụng một số hàm với vector để làm quen với container này.

**NỘI DUNG :** 

- **Vector Và Khai Báo Vector**
- **Hàm size(), length() và push_back()**
- **Vector Và Mảng 1 Chiều**
- **Vector Và Mảng 2 Chiều** 
- **Video Tutorial** 

---

**1. Vector Và Khai Báo Vector**

**Vector** là một container có tính chất tương tự như 1 mảng động, nó tự thay đổi kích thước khi bạn thêm hay xóa các phần tử trong mảng.

Ngoài ra nó hỗ trợ truy cập các phần tử trong mảng thông qua chỉ số như mảng 1 chiều.

Vector có thể lưu các kiểu dữ liệu như int, long long, float, char, pair, hoặc thậm chí là một vector khác. Khi sử dụng vector bạn cần thêm thư viện "vector" vào chương trình của mình.

**Cú pháp khai báo vector :** 

```cpp
vector<data_type> vector_name;
```

Sau đây là một vài cách khai báo vector thường gặp

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    //Khai báo vector rỗng
    vector<int> v1;
    //Khai báo vector với các phần tử
    vector<int> v2 = {1, 2, 3, 4, 5};
    //Khai báo vector có sẵn n phần tử
    int n = 20;
    vector<int> v3(n);
    //Khai báo vector có sẵn n phần tử có cùng giá trị val
    int val = 0;
    vector<int> v4(n, val);
    return 0;
}
```

---

**2. Hàm size(), length(), push_back() và pop_back()**

**size()** : Trả về số lượng phần tử trong vector. Độ phức tạp O(1)

**length()** : Trả về số lượng phần tử trong vector. Độ phức tạp O(1)

**push_back()** : Thêm phần tử vào cuối vector. Độ phức tạp O(1)

**pop_back()** : Xóa phần tử cuối cùng trong vector. Độ phức tạp O(1)

Để duyệt vector bạn có thể duyệt thông qua chỉ số, dùng ranged-base for loop.

**Ví dụ 1:** Tạo và duyệt vector

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v;
    v.push_back(1); // {1}
    v.push_back(2); // {1, 2}
    v.push_back(3); // {1, 2, 3}
    v.push_back(4); // {1, 2, 3, 4}
    cout << "Kich thuoc vector : " << v.size() << endl; // v.length()
    cout << "Duyet vector bang chi so : \n";
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << ' ';
    }  
    cout << "\nDuyet vector bang ranged-base for loop :\n";
    for(int x : v){
        cout << x << ' ';
    }
    return 0;
}
```

Output :

```cpp
Kich thuoc vector : 4
Duyet vector bang chi so : 
1 2 3 4 
Duyet vector bang ranged-base for loop :
1 2 3 4
```

**Ví dụ 2** : Vector string

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<string> v = {"codelab", "STL"};
    cout << "Kich thuoc vector : " << v.size() << endl;
    v.push_back("C++");
    v.push_back("Java");
    v.push_back("PHP");
    cout << "Kich thuoc vector : " << v.size() << endl;
    cout << "Duyet vector : ";
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    v.pop_back(); // Xoa PHP
    cout << "\nKich thuoc vector : " << v.size() << endl;
}
```

Output :

```cpp
Kich thuoc vector : 2
Kich thuoc vector : 5
Duyet vector : codelab STL C++ Java PHP 
Kich thuoc vector : 4
```

---

**3. Vector Và Mảng 1 Chiều**

Tất cả các bài toán sử dụng mảng 1 chiều bạn đều có thể sử dụng vector để thay thế, dưới đây mình sẽ hướng dẫn cách bạn nhập mảng 1 chiều từ bàn phím sử dụng vector.

**Cách 1 :**

Khai báo vector rỗng và thêm phần tử được nhập từ bàn phím vào cuối vector

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    vector<int> v;
    int n, tmp; cout << "Nhap so luong phan tu : ";
    cin >> n;
    for(int i = 0; i < n; i++){
        cout << "Nhap phan tu thu " << i + 1 << " : ";
        cin >> tmp;
        v.push_back(tmp);
    }
    cout << "Day so vua nhap : \n";
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    return 0;
}
```

**Cách 2 :** 

Khai báo vector có sẵn số lượng phần tử được nhập từ bàn phím

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    int n, tmp; cout << "Nhap so luong phan tu : ";
    cin >> n;
    vector<int> v(n);
    for(int i = 0; i < n; i++){
        cout << "Nhap phan tu thu " << i + 1 << " : ";
        cin >> v[i];
    }
    cout << "Day so vua nhap : \n";
    for(int i = 0; i < v.size(); i++){
        cout << v[i] << " ";
    }
    return 0;
}
```

---

**4. Vector Và Mảng 2 Chiều**

Mỗi vector có thể sử dụng như mảng 1 chiều, nếu muốn sử dụng vector như mảng 2 chiều bạn cần sử dụng vector các vector.

Mình sẽ hướng dẫn các bạn 2 cách để lưu mảng 2 chiều vào vector và bạn có thể lựa chọn cách mà mình thấy dễ tiếp cận hơn.

**Cách 1 :** 

Nhập từng dòng của mảng 2 chiều như 1 vector và thêm vào vector chính.

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    int n, m;
    cout << "Nhap hang, cot : ";
    cin >> n >> m;
    vector<vector<int>> v;
    for(int i = 0; i < n; i++){
        vector<int> row;
        for(int j = 0; j < m; j++){
            cout << "Nhap phan tu hang " << i + 1 << ", cot " << j + 1 << " : ";
            int tmp; cin >> tmp;
            row.push_back(tmp);
        }   
        v.push_back(row);
    }
    cout << "\nMang 2 chieu vua nhap : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

**Cách 2 :** 

Khai báo sẵn vector có kích thước với hàng, cột được nhập từ bàn phím

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
    int n, m;
    cout << "Nhap hang, cot : ";
    cin >> n >> m;
    vector<vector<int>> v(n, vector<int>(m));
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << "Nhap phan tu hang " << i + 1 << ", cot " << j + 1 << " : ";
            cin >> v[i][j];
        }   
    }
    cout << "\nMang 2 chieu vua nhap : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

---

**Video Vector :**
