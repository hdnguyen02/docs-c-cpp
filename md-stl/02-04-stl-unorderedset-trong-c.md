# [STL]. Unordered_set Trong C++

**Unordered_set** trong C++ là một container tương tự set nhưng không có thứ tự tăng dần như set, bài học này mình sẽ giới thiệu bạn một cấu trúc dữ liệu được xây dựng sẵn rất tối ưu cho việc truy xuất phần tử thông qua giá trị.

**NỘI DUNG :** 

- **Unordered_set trong C++**
- **Video tutorial** 

---

**1. Unordered_set trong C++** 

**Unordered_set** là một container trong thư viện STL và có thể sử dụng trong các chuẩn C++ 11 tới các phiên bản mới hơn.

Thư viện chứa unordered_set là "unordered_set", bạn cần thêm vào chương trình để có thể sử dụng.

Unordered_set được cài đặt bởi cấu trúc dữ liệu bảng băm - hash table vì thế rất tối ưu trong việc tìm kiếm giá trị của phần tử.

Sự khác biệt lớn nhất giữa Unordered_set và set chính là thứ tự các phần tử trong container.

Các tính chất của unordered_set :

- Các phần tử trong unordered_set đôi một khác nhau
- unordered_set không duy trì bất kỳ thứ tự nào giữa các phần tử mà nó chứa

Ngoài sự khác biệt về thứ tự, unordered_set khác với set và multiset ở độ phức tạp của các hàm tìm kiếm, chén, xóa..

- Các hàm find(), erase(), insert() của set và multiset có độ phức tạp là O(logN)
- Các hàm find(), erase(), insert() của unordered_set có độ phức tạp trong trường hợp trung bình là O(1) và trong trường hợp tệ nhất là O(N)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "unordered_set"

using namespace std;

int main(){
    unordered_set<int> se = {1, 3, 1, 1, 2, 3, 1, 4, 1};
    cout << "So phan tu trong set : " << se.size() << endl;
    cout << "Cac phan tu trong set :\n";
    for(int x : se){
        cout << x << " ";
    }
    cout << endl;
    if(se.find(3) == se.end()){
        cout << "NOT FOUND\n";
    }
    else{
        cout << "FOUND\n";
    }
}
```

Output :

```cpp
So phan tu trong set : 4
Cac phan tu trong set :
4 2 3 1 
FOUND
```

---

**Video tutorial :**
