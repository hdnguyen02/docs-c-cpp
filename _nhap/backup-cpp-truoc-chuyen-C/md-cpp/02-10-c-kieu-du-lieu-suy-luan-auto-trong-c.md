# [C++]. Kiểu Dữ Liệu Suy Luận Auto Trong C++

Từ khóa **auto** trong C++ giúp bạn có thể suy luận ra kiểu dữ liệu tương ứng phù hợp với một biến thông qua giá trị mà biến được gán. Từ C++11 trở về sau thì ta có sử dụng kiểu auto để thay cho các kiểu dữ liệu phức tạp trong C++

**NỘI DUNG :**

- **Từ Khóa auto**
- **Auto Và Vector**
- **Auto Và Set**
- **Auto Và Map**

---

**1. Từ Khóa auto** 

**Từ khóa auto** hay mình tạm gọi là kiểu auto là một tính năng mới từ C++11 tới các phiên bản mới hơn sau này, trước C++11 thì ngôn ngữ lập trình C++ khi khai báo biến bạn phải chỉ ra kiểu dữ liệu tương ứng của biến đó.

Từ khóa auto giúp tự suy luận ra kiểu dữ liệu phù hợp với biến thông qua giá trị bạn gán cho biến đó, đặc điểm này khá giống với các ngôn ngữ lập trình Dynamically Typed Languages như Python.

Nếu bạn đã từng học qua Python thì khi khai báo biến bạn không cần khai báo kiểu dữ liệu cho biến mà kiểu dữ liệu sẽ được tự động xác định dựa vào giá trị mà biến được khởi tạo

Sử dụng từ khóa auto, kiểu dữ liệu của biến sẽ được xác định lúc runtime thay vì compile-time như trước.

**Ví dụ 1:** 

```cpp
#include "iostream"
#include "typeinfo"

using namespace std;

int main(){
   auto x = 100;
   auto y = 30.5f;
   auto z = '@';
   auto t = 1000000000000000;
   auto p = make_pair(10, 20);
   auto l = 30.5d;
   cout << "Kieu du lieu cua x : " << typeid(x).name() << endl;
   cout << "Kieu du lieu cua y : " << typeid(y).name() << endl;
   cout << "Kieu du lieu cua z : " << typeid(z).name() << endl;
   cout << "Kieu du lieu cua t : " << typeid(t).name() << endl;
   cout << "Kieu du lieu cua p : " << typeid(p).name() << endl;
   cout << "Kieu du lieu cua l : " << typeid(l).name() << endl;
   return 0;
}
```

Output :

```cpp
Kieu du lieu cua x : i
Kieu du lieu cua y : f
Kieu du lieu cua z : c
Kieu du lieu cua t : x
Kieu du lieu cua p : St4pairIiiE
Kieu du lieu cua l : d
```

**Giải thích :** 

Ở đây mình sử dụng toán tử **typeid()** để có thể lấy về kiểu dữ liệu cho biến

- Biến x được gán giá trị 30 nên có kiểu là integer (i)
- Biến y được gán giá trị 30.5f nên có kiểu là float (f)
- Biến z được gán giá trị '@' nên có kiểu là char(c)
- Biến t được gán giá trị 1000000000000000 nên có kiểu là long long (x)
- Biến p được gán giá trị là một pair(10, 20) nên có kiểu là pair (St4pairIiiE)
- Biến l được gán giá trị là 30.5d nên có kiểu là double (d)

**Chú ý** : Bạn không thể khai báo biến có kiểu auto mà không khởi tạo giá trị cho nó

Thông thường mình chỉ dùng auto để thay cho các kiểu dữ liệu dài dòng như : pair, iterator, con trỏ... Nếu bạn chưa biết kiến thức về iterator và con trỏ thì có thể tạm thời bỏ qua ví dụ này nhé.

**Ví dụ 2 :** 

```cpp
#include "iostream"
#include "typeinfo"

using namespace std;

int main(){
   auto p = make_pair(10, 20);
   cout << p.first << ' ' << p.second << endl;
   int n = 100;
   auto ptr1 = &n;
   cout << "ptr1 la kieu con tro : " << typeid(ptr1).name() << endl;
   auto ptr2 = &ptr1;
   cout << "ptr2 la kieu con tro cap 2 : " << typeid(ptr2).name() << endl;
   return 0;
}
```

Output :

```cpp
10 20
ptr1 la kieu con tro : Pi
ptr2 la kieu con tro cap 2 : PPi
```

---

**2. Auto Và Vector** 

Kiến thức về **vector** nếu bạn chưa học có thể bỏ qua phần này và khi học xong vector có thể tiếp tục tham khảo.

Thông thường để duyệt qua vector bạn có thể dùng iterator, tuy nhiên đôi khi việc khai báo iterator quá dài dòng nên bạn có thể thay nó bằng kiểu auto

**Ví dụ :** 

```cpp
#include "iostream"
#include "vector"

using namespace std;

int main(){
   vector<int> v = {1, 2, 3, 4, 5};
   cout << "Duyet vector bang range-based for loop : \n";
   for(auto x : v){
      cout << x << ' ';
   }
   cout << endl;
   cout << "Duyet vector bang iterator : \n";
   for(auto it = v.begin(); it != v.end(); ++it){
      cout << *it << ' ';
   }
   return 0;
}
```

Output :

```cpp
Duyet vector bang range-based for loop : 
1 2 3 4 5 
Duyet vector bang iterator : 
1 2 3 4 5
```

**Giải thích :** 

- auto x khi dùng trong range-based for loop thì x đóng vai trò là int
- auto it = v.begin() thì it đóng vai trò là iterator nên khi truy xuất giá trị trong vector bạn cần giải tham chiếu

---

**3. Auto Và Set** 

Kiến thức về **set** nếu bạn chưa học có thể bỏ qua phần này và khi học xong vector có thể tiếp tục tham khảo.

Trong ví dụ này mình sẽ dùng kiểu auto để thay cho iterator, string... khi áp dụng với set

**Ví dụ :** 

```cpp
#include "iostream"
#include "set"

using namespace std;

int main(){
   set<string> se = {"codelab", "c++", "python", "c++", "java"};
   cout << "Duyet set bang range-based for loop : \n";
   for(auto x : se){
      cout << x << " ";
   }
   cout << endl;
   auto pos = se.find("codelab");
   if(pos == se.end()){
      cout << "NOT FOUND";
   }
   else{
      cout << "FOUND\n";
   }
}
```

Output :

```cpp
Duyet set bang range-based for loop : 
codelab c++ java python 
FOUND
```

**Giải thích :** 

- auto x khi duyệt set thì x có kiểu dữ liệu là string
- auto pos = se.find("codelab") được gán giá trị trả về của hàm find nên pos có kiểu là set::iterator

---

**4. Auto Và Map**

Kiến thức về **map** nếu bạn chưa học có thể bỏ qua phần này và khi học xong vector có thể tiếp tục tham khảo.

**Ví dụ :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
   map<string, string> mp;
   mp.insert({"codelab", "codelab.dev"});
   mp.insert({"Meta", "facebook.com"});
   mp.insert({"X", "twitter.com"});
   cout << "Duyet map bang range-based for loop : \n";
   for(auto p : mp){
      cout << p.first << ' ' << p.second << endl;
   }
   cout << "Duyet map bang iterator : \n";
   for(auto it = mp.begin(); it != mp.end(); ++it){
      cout << it->first << ' ' << it-> second << endl;
   }
}
```

Output :

```cpp
Duyet map bang range-based for loop : 
codelab codelab.dev
Meta facebook.com
X twitter.com
Duyet map bang iterator : 
codelab codelab.dev
Meta facebook.com
X twitter.com
```

**Giải thích :** 

- auto p thì p có kiểu dữ liệu là pair
- auto it = mp.begin() thì it có kiểu dữ liệu là map::iterator

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-10-c-kieu-du-lieu-suy-luan-auto-trong-c.md](solutions/02-10-c-kieu-du-lieu-suy-luan-auto-trong-c.md)

**Bài 1.** Khai báo bằng `auto` các biến với giá trị: `28`, `3.14`, `'A'`, `true`, `"codelab"`, `28LL`, `3.14f`. Dùng `typeid().name()` để in ra kiểu thật của mỗi biến.

**Bài 2.** Thử khai báo `auto x;` (không khởi tạo) và chép lại thông báo lỗi. Giải thích vì sao.

**Bài 3.** Dự đoán kiểu của `auto a = 5 / 2;` và `auto b = 5.0 / 2;`. In kết quả để kiểm chứng.

**Bài 4.** Khai báo một `vector<int>` gồm 5 phần tử và duyệt in ra bằng 3 cách: vòng `for` chỉ số, `auto` với iterator, và range-based for với `auto`.

**Bài 5.** Khai báo `pair<string, int>` và dùng `auto` để nhận giá trị trả về từ `make_pair`.

**Bài 6.** Duyệt một `map<string, int>` bằng `auto` và in ra từng cặp khoá — giá trị.

**Bài 7.** So sánh 3 cách viết vòng lặp sau, cho biết cách nào có sao chép dữ liệu (tốn kém) và cách nào không:

```cpp
for (auto x : v)        { ... }
for (auto& x : v)       { ... }
for (const auto& x : v) { ... }
```

**Bài 8.** Viết chương trình dùng `auto&` để thay đổi giá trị các phần tử trong `vector` (nhân đôi mỗi phần tử).

**Bài 9.** Chạy đoạn sau và giải thích vì sao `v` không bị thay đổi:

```cpp
vector<int> v = {1, 2, 3};
for (auto x : v) x *= 10;
for (auto x : v) cout << x << " ";
```

**Bài 10.** Dùng `auto` với `set<int>`: chèn vài số, duyệt in ra và quan sát thứ tự.

**Bài 11.** Viết một hàm trả về `pair<int,int>` rồi dùng `auto` để nhận kết quả. Sau đó viết lại bằng structured binding `auto [a, b]`.

**Bài 12.** `auto` có làm chương trình chạy chậm hơn không? Giải thích `auto` được xử lý ở giai đoạn nào (biên dịch hay chạy).

**Bài 13.** Nêu 3 trường hợp **nên** dùng `auto` và 2 trường hợp **không nên** dùng `auto`. Cho ví dụ cụ thể.

**Bài 14.** Tìm hiểu `decltype`. Viết chương trình dùng `decltype` để khai báo một biến có cùng kiểu với biến khác.

**Bài 15.** Viết lại đoạn code dài dòng sau bằng `auto` cho gọn:

```cpp
vector<pair<string, vector<int>>> data;
for (vector<pair<string, vector<int>>>::iterator it = data.begin();
     it != data.end(); ++it) {
    cout << it->first << endl;
}
```
