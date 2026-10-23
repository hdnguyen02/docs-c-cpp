# [STL]. Bài Tập Thực Hành Set Trong C++

Bài viết này sẽ hướng dẫn các bạn sử dụng container set trong C++ để giải quyết một số bài tập thường gặp một cách tối ưu hơn.

**NỘI DUNG :** 

- **Bài toán số lượng phần tử riêng biệt trong mảng**
- **Bài toán truy vấn phần tử trong mảng**
- **Bài toán liệt kê giá trị trong mảng theo thứ tự xuất hiện**
- **Bài toán liệt kê giá trị trong mảng theo thứ tự từ nhỏ tới lớn** 

---

**1. Bài toán số lượng phần tử riêng biệt trong mảng**

**Đề bài** : Cho mảng A[] gồm N (1 ≤ N ≤ 106) phần tử, hãy đếm xem trong mảng có bao nhiêu giá trị khác nhau ?

**Giải thuật** : Đưa tất cả các phần tử trong mảng vào set và in ra kích thước của set

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include 
#include 
#include 

using namespace std;

int main(){
    int a[10] = {1, 2, 1, 2, 3, 1, 2, 5, 1, 8};
    set<int> se;
    for(int i = 0; i < 10; i++){
        se.insert(a[i]);
    }
    cout << se.size() << endl;
}

```

**2. Bài toán truy vấn phần tử trong mảng**

**Đề bài** : Cho mảng A[] gồm N (1 ≤ N ≤ 106) phần tử, có Q truy vấn mỗi truy vấn yêu cầu bạn kiểm tra xem giá trị X có xuất hiện trong mảng hay không?

**Giải thuật** : Đưa tất cả các phần tử trong mảng vào set khi đó mỗi truy vấn bạn có thể áp dụng hàm tìm kiếm của set (O(logN)) để tối ưu cho mỗi truy vấn thay vì dùng thuật toán tìm kiếm tuyến tính O(N)

**Độ phức tạp** : O(logN) cho mỗi truy vấn

**Mã nguồn :** 

```cpp
#include 
#include 
#include 

using namespace std;

int main(){
    int a[10] = {1, 2, 1, 2, 3, 1, 2, 5, 1, 8};
    int X[5] = {1, 6, 8, 9, 10};
    int Q = 5, n = 10;
    set<int> se;
    for(int i = 0; i < 10; i++){
        se.insert(a[i]);
    }
    for(int i = 0; i < Q; i++){
        if(se.find(X[i]) != se.end()){
            cout << "TIM THAY " << X[i] << endl;
        }
        else{
            cout << "KHONG TIM THAY " << X[i] << endl;
        }
    }
}
```

**3. Bài toán liệt kê giá trị khác nhau trong mảng theo thứ tự xuất hiện**

**Đề bài** : Cho mảng A[] gồm N (1 ≤ N ≤ 106) phần tử, hãy liệt kê các giá trị khác nhau trong mảng theo thứ tự xuất hiện, mỗi giá trị chỉ liệt kê 1 lần.

**Giải thuật** : Duyệt qua mảng và duy trì set như 1 tập hợp các giá trị đã được in ra trước đó, khi gặp phần tử trong mảng bạn kiểm tra nếu chưa xuất hiện trong set thì sẽ in ra và đưa giá trị này vào set. Việc dùng set sẽ giúp bạn tìm kiếm nhanh hơn những giá trị đã được in ra.

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include 
#include 
#include 

using namespace std;

int main(){
    int a[10] = {1, 8, 2, 1, 2, 3, 2, 5, 5, 8};
    set<int> se;
    for(int i = 0; i < 10; i++){
        //Kiem tra xem a[i] da duoc in ra chua?
        if(se.find(a[i]) == se.end()){
            cout << a[i] << " ";
            se.insert(a[i]);
        }
    }
}

//Output : 1 8 2 3 5
```

**4. Bài toán liệt kê giá trị khác nhau trong mảng theo thứ tự từ nhỏ tới lớn**

**Đề bài** : Cho mảng A[] gồm N (1 ≤ N ≤ 106) phần tử, hãy liệt kê các giá trị khác nhau trong mảng theo thứ tự xuất hiện, mỗi giá trị chỉ liệt kê 1 lần.

**Giải thuật** : Đưa tất cả các giá trị trong mảng vào set, set sẽ chỉ giữ lại các giá trị khác nhau và lưu theo thứ tự tăng dần nên bạn chỉ cần duyệt set là có thể in ra được theo thứ tự đề bài yêu cầu.

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

int main(){
    int a[10] = {1, 8, 2, 1, 2, 3, 2, 5, 5, 8};
    set<int> se;
    for(int i = 0; i < 10; i++){
        se.insert(a[i]);
    }
    for(int x : se){
        cout << x << " ";
    }
}

//Output : 1 2 3 5 8
```
