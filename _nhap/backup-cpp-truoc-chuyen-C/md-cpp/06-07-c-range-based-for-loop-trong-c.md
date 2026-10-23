# [C++]. Range-based for loop trong C++

**Range-based for loop** là một vòng lặp tương tự như vòng lặp for truyền thống các bạn đã biết nhưng có phần ngắn gọn và tiện lợi hơn. Nó có thể dùng để duyệt qua các phần tử trong mảng hay các container như vector, set, map, ... trong C++

**NỘI DUNG :** 

- **Range-based for loop** 
- **Tham Chiếu Trong Range-based for loop** 

---

**1. Range-based for loop**

Từ C++ 11 tới các phiên bản C++ mới hơn thì đã có thêm vòng lặp Range-based for loop, đây là vòng lặp giúp bạn duyệt qua các phần tử trong mảng hay container tuần tự từ đầu tới cuối.

Đê có thể sử dụng được vòng lặp này thì bạn cần biên dịch code với chuẩn C++11 trở lên.

**Cú pháp :** 

```cpp
for ( range_declaration : range_expression ){
    //code
}
```

Các thành phần của range-based for loop :

**range_declaration** : Phần này bạn sẽ khai báo 1 biến tạm và kiểu dữ liệu tương ứng của biến đó, biến này có vai trò được gán giá trị của từng phần tử trong mảng hay container ở mỗi lần lặp.

**range_expression** : Đây là biểu thức, container, mảng... hỗ trợ việc duyệt từng phần tử.

**code** : Các câu lệnh của vòng for

**Ví dụ 1** : Duyệt mảng

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
    int a[5] = {10, 20, 30, 40, 50};
    cout << "Duyet mang int :\n";
    for(int x : a){
        cout << x << " ";
    }
    char b[6] = {'2', '8', 't', 'e', 'c', 'h'};
    cout << "\nDuyet mang char :\n";
    for(char x : b){
        cout << x << " ";
    }
    pair<int, int> c[3] = {{1, 2}, {2, 3}, {3, 4}};
    cout << "\nDuyet mang pair :\n";
    for(pair<int, int> it : c){
        cout << it.first << " " << it.second << endl;
    }
    return 0;
}
```

Output :

```cpp
Duyet mang int :
10 20 30 40 50 
Duyet mang char :
2 8 t e c h 
Duyet mang pair :
1 2
2 3
3 4
```

**Ví dụ 2** : Duyệt vector

Nếu bạn chưa biết về vector thì có thể học kiến thức này [tại đây](https://blog.codelab.dev/stl-vector-trong-c)

```cpp
#include "iostream"
#include "string"
#include "vector"
using namespace std;

int main(){
    vector<int> v1 = {1, 2, 3, 4, 5};
    for(int x : v1){
        cout << x << " ";
    }
    cout << endl;
    vector<char> v2 = {'2', '8', 't', 'e', 'c', 'h'};
    for(char x : v2){
        cout << x << ' ';
    }
    return 0;
}
```

Output :

```cpp
1 2 3 4 5 
2 8 t e c h
```

Ngoài ra range-based for loop còn có thể dùng để duyệt string, map, set... Tuy nhiên ở thời điểm hiện tại các bạn chưa có những kiến thức về phần này nên mình chưa thêm vào ví dụ demo. Các bạn có thể tìm bài học về string, set, map trên blog của mình thì trong các phần đó mình sẽ có phần hướng dẫn duyệt bằng range-based for loop.

---

**2. Tham Chiếu Trong Range-based for loop**

Range-based for loop giúp bạn dễ dàng duyệt qua mảng hay container tuy nhiên nếu bạn muốn thay đổi các phần tử trong mảng (container) mà bạn đang duyệt qua thì bạn cần thêm tham chiếu vào trước biến tạm của vòng lặp.

Xem xét ví dụ sau đây khi mình cố thay đổi giá trị các phần tử trong mảng thông qua vòng lặp range-based for loop

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
    char a[6] = {'2', '8', 't', 'e', 'c', 'h'};
    for(char x : a){
        x = '@';
    }
    cout << "Sau khi thay doi : \n";
    for(char x : a){
        cout << x << ' ';
    }
    return 0;
}
```

Output :

```cpp
Sau khi thay doi : 
2 8 t e c h
```

**Giải thích :** 

Khi bạn duyệt qua mảng b bằng vòng lặp thì biến x chỉ có vai trò là biến tạm được gán giá trị các phần tử trong mảng ở mỗi vòng lặp. Khi đó nếu bạn thay đổi giá trị của biến x thì không ảnh hưởng gì tới các phần tử trong mảng ban đầu.

Việc này tương tự như bạn gọi hàm và việc thay đổi tham số của hàm không ảnh hưởng tới đối số mà bạn truyền cho hàm

Để những gì thay đổi với biến tạm ở trong vòng for ảnh hưởng tới các phần tử trong mảng thì bạn cần thêm tham chiếu trước biến tạm này.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
    char a[6] = {'2', '8', 't', 'e', 'c', 'h'};
    for(char &x : a){
        x = '@';
    }
    cout << "Sau khi thay doi : \n";
    for(char x : a){
        cout << x << ' ';
    }
    return 0;
}
```

Output :

```cpp
Sau khi thay doi : 
@ @ @ @ @ @
```

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/06-07-c-range-based-for-loop-trong-c.md](solutions/06-07-c-range-based-for-loop-trong-c.md)

**Bài 1.** Dùng range-based for in ra tất cả phần tử của một mảng tĩnh và một `vector`.

**Bài 2.** Tính tổng các phần tử của `vector<int>` bằng range-based for.

**Bài 3.** Dùng range-based for nhân đôi mọi phần tử của `vector` (chú ý dấu `&`).

**Bài 4.** Duyệt một `string` và đếm số nguyên âm bằng range-based for.

**Bài 5.** Duyệt `vector<string>` và in ra chuỗi dài nhất.

**Bài 6.** Duyệt `map<string,int>` in ra từng cặp khoá-giá trị bằng range-based for và structured binding.

**Bài 7.** Chương trình sau không làm thay đổi `v`. Tìm lỗi và sửa:

```cpp
vector<int> v = {1,2,3};
for (auto x : v) x = x * 2;
```

**Bài 8.** Duyệt `vector<vector<int>>` (ma trận) bằng range-based for lồng nhau.

**Bài 9.** So sánh 3 cách: `for (auto x : v)`, `for (auto& x : v)`, `for (const auto& x : v)`. Đo thời gian với `vector<string>` lớn.

**Bài 10.** Range-based for có dùng được với mảng đã truyền vào hàm không? Thử và giải thích.

**Bài 11.** Dùng range-based for với danh sách khởi tạo trực tiếp: `for (int x : {1,2,3,4,5})`.

**Bài 12.** Viết chương trình lọc và in ra các số nguyên tố trong `vector` bằng range-based for.

**Bài 13.** Chương trình sau có lỗi nguy hiểm gì?

```cpp
vector<int> v = {1,2,3,4,5};
for (auto x : v) {
    if (x % 2 == 0) v.push_back(x * 10);
}
```

**Bài 14.** Tìm hiểu `std::views` / ranges (C++20). Viết chương trình lọc số chẵn và nhân đôi bằng ranges.

**Bài 15.** Viết lại 5 chương trình bất kỳ của bạn ở các chương trước bằng range-based for và so sánh độ dài code.
