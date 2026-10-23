# [C++]. Hàm binary_search, lower_bound, ...

Trong C++ cũng cung cấp sẵn thuật toán tìm kiếm nhị phân cũng như biến thể của nó là **lower_bound** & **upper_bound**. Đây là hai hàm mà nếu biết sử dụng và ứng dụng nó bạn sẽ giải quyết được rất nhiều bài toán về tìm kiếm một cách tối ưu.

**NỘI DUNG :** 

- **Hàm binary_search**
- **Hàm lower_bound**
- **Hàm upper_bound** 
- **Video tutorial**

**1. Hàm binary_search**

Hàm **binary_search()** được cài đặt bằng thuật toán tìm kiếm nhị phân, bạn có thể áp dụng hàm này trên mảng, vector, string đã được sắp xếp theo thứ tự tăng dần. Để sử dụng hàm này bạn cần thêm thư viện **"algorithm"** vào chương trình của mình.

**Giá trị trả về** : Hàm trả về true nếu giá trị tìm kiếm xuất hiện trong mảng, ngược lại trả về false.

Bạn có thể sử dụng hàm này luôn nếu đã code thành thạo thuật toán tìm kiếm nhị phân ở bài trước.

**Độ phức tạp** : O(logN)

**Cú pháp :** 

```cpp
//Cú pháp áp dụng với mảng a[] gồm n phần tử và giá trị tìm kiếm x
binary_search(a, a + n, x)

//Cú pháp áp dụng với vector, string và giá trị tìm kiếm x
binary_search(v.begin(), v.end(), x)
binary_search(s.begin(), s.end(), x)

```

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
using namespace std;

int main(){
    int a[10] = {1, 2, 3, 5, 5, 6, 8, 9, 14, 21};
    int n = 10, X = 5;
    if(binary_search(a, a + n, X)){
        cout << "FOUND\n";
    }
    else{
        cout << "NOT FOUND\n";
    }
    vector<int> v = {1, 2, 3, 4, 5, 6, 6, 6, 8, 9};
    if(binary_search(v.begin(), v.end(), X)){
        cout << "FOUND\n";
    }
    else{
        cout << "NOT FOUND\n";
    }
}
```

Output :

```cpp
FOUND
FOUND
```

Ngoài ra bạn cũng có thể tìm kiếm trên đoạn chỉ số [L, R] của mảng hoặc vector

**Cú pháp :** 

```cpp
//Cú pháp áp dụng với mảng a[] 
binary_search(a + L, a + R + 1, x)

//Cú pháp áp dụng với vector
binary_search(v.begin() + L, v.begin() + R + 1, x)
```

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"
using namespace std;

int main(){
    int a[10] = {1, 2, 3, 5, 5, 6, 8, 9, 14, 21};
    int n = 10, X = 5;
    if(binary_search(a + 5, a + 8, X)){
        cout << "FOUND\n";
    }
    else{
        cout << "NOT FOUND\n";
    }
    vector<int> v = {1, 2, 3, 4, 5, 6, 6, 6, 8, 9};
    if(binary_search(v.begin() + 2, v.begin() + 7, X)){
        cout << "FOUND\n";
    }
    else{
        cout << "NOT FOUND\n";
    }
}
```

Output :

```cpp
NOT FOUND
FOUND
```

**2. Hàm lower_bound**

Hàm **lower_bound()** được dùng để tìm giá trị nhỏ nhất lớn hơn hoặc bằng giá trị X mà bạn tìm kiếm trong mảng hoặc vector tăng dần, ngoài ra nó còn có thể áp dụng với set & map.

Hàm này tương đối khó dùng vì nó cần bạn thành thạo kiến thức về con trỏ và iterator.

**Giá trị trả về :** 

- Đối với mảng thì hàm này trả về con trỏ tới giá trị nhỏ nhất ≥ giá trị tìm kiếm, nếu không tìm thì hàm trả về con trỏ tới a + n
- Đối với vector thì hàm trả về iterator tới giá trị nhỏ nhất ≥ giá trị tìm kiếm, nếu không tìm thì hàm trả về iterator end()

**Độ phức tạp** : O(logN)

**Cú pháp :** 

```cpp
//Cú pháp áp dụng trên mảng a[] gồm n phần tử và giá trị tìm kiếm X
lower_bound(a, a + n, X)

//Cú pháp áp dụng trên vector và giá trị tìm kiếm X
lower_bound(v.begin(), v.end(), X)
```

**Mã nguồn 1** : Lower_bound áp dụng trên mảng đã tăng dần

```cpp
#include "iostream"
#include "algorithm"
using namespace std;

int main(){
    int a[10] = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int n = 10, X = 5, Y = 22;
    int *it1 = lower_bound(a, a + n, X);
    if(it1 == a + n){
        cout << "Khong tim duoc gia tri >= 5" << endl; 
    }
    else{
        cout << "Gia tri nho nhat >= 5 : " << *it1 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it1 - a << endl;
    }
    int *it2 = lower_bound(a, a + n, Y);
    if(it2 == a + n){
        cout << "Khong tim duoc gia tri >= 22" << endl; 
    }
    else{
        cout << "Gia tri nho nhat >= 22 : " << *it2 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it2 - a << endl;
    }
    
}
```

Output :

```cpp
Gia tri nho nhat >= 5 : 5
Chi so cua gia tri tim duoc : 3
Khong tim duoc gia tri >= 22
```

**Mã nguồn 2** : Lower_bound áp dụng trên vector đã tăng dần

```cpp
#include "iostream"
#include "algorithm"
using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int X = 5, Y = 22;
    vector<int>::iterator it1 = lower_bound(v.begin(), v.end(), X);
    if(it1 == v.end()){
        cout << "Khong tim duoc gia tri >= 5" << endl; 
    }
    else{
        cout << "Gia tri nho nhat >= 5 : " << *it1 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it1 - v.begin() << endl;
    }
    vector<int>::iterator it2 = lower_bound(v.begin(), v.end(), Y);
    if(it2 == v.end()){
        cout << "Khong tim duoc gia tri >= 22" << endl; 
    }
    else{
        cout << "Gia tri nho nhat >= 22 : " << *it2 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it2 - v.begin() << endl;
    }
}
```

Output :

```cpp
Gia tri nho nhat >= 5 : 5
Chi so cua gia tri tim duoc : 3
Khong tim duoc gia tri >= 22
```

**Chú ý** : Bạn cũng có thể áp dụng hàm lower_bound trên đoạn chỉ số [L, R], cú pháp tương tự như hàm binary_search

**3. Hàm upper_bound**

Hàm **upper_bound()** cách dùng, cú pháp, giá trị trả về, độ phức tạp đều giống hàm upper_bound chỉ khác duy nhất là hàm này tìm giá trị nhỏ nhất > giá trị X mà bạn tìm kiếm trong mảng tăng dần.

**Cú pháp :** 

```cpp
//Cú pháp áp dụng trên mảng a[] gồm n phần tử và giá trị tìm kiếm X
upper_bound(a, a + n, X)

//Cú pháp áp dụng trên vector và giá trị tìm kiếm X
upper_bound(v.begin(), v.end(), X)
```

**Mã nguồn 1** : upper_bound áp dụng trên mảng đã tăng dần

```cpp
#include "iostream"
#include "algorithm"
using namespace std;

int main(){
    int a[10] = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int n = 10, X = 5, Y = 22;
    int *it1 = upper_bound(a, a + n, X);
    if(it1 == a + n){
        cout << "Khong tim duoc gia tri > 5" << endl; 
    }
    else{
        cout << "Gia tri nho nhat > 5 : " << *it1 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it1 - a << endl;
    }
    int *it2 = upper_bound(a, a + n, Y);
    if(it2 == a + n){
        cout << "Khong tim duoc gia tri > 22" << endl; 
    }
    else{
        cout << "Gia tri nho nhat > 22 : " << *it2 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it2 - a << endl;
    }
    
}
```

Output :

```cpp
Gia tri nho nhat > 5 : 8
Chi so cua gia tri tim duoc : 6
Khong tim duoc gia tri > 22
```

**Mã nguồn 2** : upper_bound áp dụng trên vector đã tăng dần

```cpp
#include "iostream"
#include "algorithm"
using namespace std;

int main(){
    vector<int> v = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int X = 5, Y = 22;
    vector<int>::iterator it1 = upper_bound(v.begin(), v.end(), X);
    if(it1 == v.end()){
        cout << "Khong tim duoc gia tri > 5" << endl; 
    }
    else{
        cout << "Gia tri nho nhat > 5 : " << *it1 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it1 - v.begin() << endl;
    }
    vector<int>::iterator it2 = lower_bound(v.begin(), v.end(), Y);
    if(it2 == v.end()){
        cout << "Khong tim duoc gia tri > 22" << endl; 
    }
    else{
        cout << "Gia tri nho nhat > 22 : " << *it2 << endl;
        cout << "Chi so cua gia tri tim duoc : " << it2 - v.begin() << endl;
    }
}
```

Output :

```cpp
Gia tri nho nhat > 5 : 8
Chi so cua gia tri tim duoc : 6
Khong tim duoc gia tri > 22
```

**Video tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-06-c-ham-binarysearch-lowerbound-upperbound-trong-c.md](solutions/10-06-c-ham-binarysearch-lowerbound-upperbound-trong-c.md)

**Bài 1.** Dùng `binary_search` kiểm tra một giá trị có trong mảng đã sắp xếp hay không.

**Bài 2.** Dùng `lower_bound` tìm vị trí đầu tiên có giá trị ≥ `x`.

**Bài 3.** Dùng `upper_bound` tìm vị trí đầu tiên có giá trị > `x`.

**Bài 4.** Dùng `lower_bound` và `upper_bound` đếm số lần xuất hiện của `x`.

**Bài 5.** Dùng `equal_range` để làm việc của bài 4 chỉ bằng một lời gọi.

**Bài 6.** Tìm vị trí chèn `x` vào mảng đã sắp xếp mà vẫn giữ thứ tự.

**Bài 7.** Giải thích vì sao `binary_search` trả về `bool` chứ không phải vị trí. Làm sao lấy được vị trí?

**Bài 8.** Dùng `lower_bound` tìm phần tử gần `x` nhất trong mảng đã sắp xếp.

**Bài 9.** Dùng `lower_bound` với comparator tuỳ chỉnh trên mảng sắp xếp **giảm dần**.

**Bài 10.** Dùng `lower_bound` với `vector<pair<int,string>>` để tìm theo khoá.

**Bài 11.** Tìm số phần tử nằm trong khoảng `[a, b]` của một mảng đã sắp xếp.

**Bài 12.** Dùng `lower_bound` trên `set` và `map`. Vì sao nên dùng `s.lower_bound()` thay vì `std::lower_bound(s.begin(), ...)`?

**Bài 13.** Chương trình sau cho kết quả sai. Tìm lỗi:

```cpp
vector<int> v = {5, 2, 8, 1, 9};
cout << binary_search(v.begin(), v.end(), 8);
```

**Bài 14.** So sánh `binary_search`, `find`, và `set::count` về tốc độ với 10⁶ truy vấn.

**Bài 15.** Viết chương trình tra cứu bảng điểm: nhập điểm, dùng `upper_bound` để xác định xếp loại theo bảng ngưỡng.
