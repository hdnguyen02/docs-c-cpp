# [STL]. Bài Tập Thực Hành Map Trong C++

Sau khi học xong các tính chất quan trọng và sử dụng **map** bạn hãy vận dụng nó để giải quyết các bài toán đặc trưng. Map rất mạnh trong các bài toán tìm kiếm nhanh, đánh dấu và đếm tần suất.

**NỘI DUNG :** 

- **Bài toán đếm giá trị khác nhau trong mảng**
- **Bài toán đếm tần suất của phần tử trong mảng 1**
- **Bài toán đếm tần suất của phần tử trong mảng 2**
- **Bài toán đếm tần suất của từ trong xâu ký tự**
- **Bài toán tìm tập hợp của 2 mảng**
- **Bài toán tìm tập giao của 2 mảng**
- Video tutorial

**1. Bài toán đếm giá trị khác nhau trong mảng**

**Đề bài** : Cho mảng A[] gồm N (1≤N≤106) các số nguyên 32 bit, hãy đếm xem trong mảng có bao nhiêu giá trị khác nhau.

**Thuật toán** : Đưa các giá trị trong mảng vào làm key của map, value thì bạn có thể tự chọn giá trị mình muốn. Khi đưa các phần tử trong mảng A[] vào làm key cho map thì nó sẽ tự loại đi các giá trị trùng nhau, khi đó số lượng phần tử trong map chính là số giá trị khác nhau trong mảng A[]

**Độ phức tạp** : O(NlogN) nếu bạn sử dụng map hoặc O(N) nếu bạn sử dụng unordered_map

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    int a[12] = {1, 3, 2, 1, 2, 3, 4, 1, 5, 8, 10, 2};
    int n = 12;
    map<int, int> mp; 
    for(int i = 0; i < n; i++){
        mp[a[i]] = 1; // value minh chon la 1
    }
    cout << "So luong phan tu khac nhau trong mang : " << mp.size() << endl;
    return 0; 
}
```

Output :

```cpp
So luong phan tu khac nhau trong mang : 7
```

**2. Bài toán đếm tần suất của phần tử trong mảng 1**

**Đề bài** : Cho mảng A[] gồm N (1≤N≤106) các số nguyên 32 bit, hãy đếm xem mỗi giá trị trong mảng xuất hiện bao nhiêu lần và in ra theo thứ tự giá trị tăng dần

**Thuật toán** : Sử dụng map với key tương ứng là giá trị trong mảng và value của key chính là lưu tần suất xuất hiện. Duyệt qua mảng A[] và key gặp giá trị x bạn chỉ cần cho mp[x]++ để tăng value của key x lên 1 đơn vị. Vì map đã lưu các giá trị key tăng dần nên bạn chỉ cần duyệt từng cặp phần tử trong map là có thể in theo thứ tự đề bài yêu cầu.

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    int a[12] = {1, 3, 2, 1, 2, 3, 4, 1, 5, 8, 10, 2};
    int n = 12;
    map<int, int> mp; 
    for(int i = 0; i < n; i++){
        mp[a[i]]++;
    }
    for(pair<int, int> it : mp){
        cout << it.first << " xuat hien " << it.second << " lan\n";
    }
    return 0; 
}
```

Output :

```cpp
1 xuat hien 3 lan
2 xuat hien 3 lan
3 xuat hien 2 lan
4 xuat hien 1 lan
5 xuat hien 1 lan
8 xuat hien 1 lan
10 xuat hien 1 lan
```

**3. Bài toán đếm tần suất của phần tử trong mảng 2**

**Đề bài** : Cho mảng A[] gồm N (1≤N≤106) các số nguyên 32 bit, hãy đếm xem mỗi giá trị trong mảng xuất hiện bao nhiêu lần và in ra theo thứ tự xuất hiện trong mảng, mỗi giá trị chỉ liệt kê 1 lần.

**Thuật toán** : Sử dụng map với key tương ứng là giá trị trong mảng và value của key chính là lưu tần suất xuất hiện. Duyệt qua mảng A[] và key gặp giá trị x bạn chỉ cần cho mp[x]++ để tăng value của key x lên 1 đơn vị. Để liệt kê theo thứ tự xuất hiện trong mảng thì bạn cần duyệt mảng, sau khi in xong bạn cần cho tần suất của giá trị đã in về 0 để tránh in trùng.

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    int a[12] = {1, 3, 2, 10, 2, 5, 4, 1, 5, 8, 10, 2};
    int n = 12;
    map<int, int> mp; 
    for(int i = 0; i < n; i++){
        mp[a[i]]++;
    }
    for(int i = 0; i < n; i++){
        if(mp[a[i]] != 0){
            cout << a[i] << " xuat hien " << mp[a[i]] << " lan\n";
            mp[a[i]] = 0;
        }
    }
    return 0; 
}
```

Output :

```cpp
1 xuat hien 2 lan
3 xuat hien 1 lan
2 xuat hien 3 lan
10 xuat hien 2 lan
5 xuat hien 2 lan
4 xuat hien 1 lan
8 xuat hien 1 lan
```

**4. Bài toán đếm tần suất của từ trong xâu ký tự**

**Đề bài** : Cho một xâu ký tự gồm nhiều từ, hãy đếm xem mỗi từ xuất hiện bao nhiêu lần và liệt kê theo thứ tự từ điển tăng dần

**Thuật toán** : Sử dụng map với key tương ứng là một string lưu một từ trong xâu và value của key chính là lưu tần suất xuất hiện của từ đó. Tách các từ trong xâu ra bằng stringstream, mỗi lần tách được 1 từ thì bạn tăng tần suất của nó lên, duyệt map và in ra từng cặp phần tử trong map.

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"
#include "sstream"

using namespace std;

int main(){
    string s = "codelab lap trinh C++ codelab tech thuat toan codelab lap trinh C++";
    stringstream ss(s);
    string word;
    map<string, int> mp;
    while(ss >> word){
        mp[word]++;
    }
    for(pair<string, int> it : mp){
        cout << it.first << " xuat hien " << it.second << " lan" << endl;
    }
    return 0; 
}
```

Output :

```cpp
codelab xuat hien 3 lan
C++ xuat hien 2 lan
lap xuat hien 2 lan
tech xuat hien 1 lan
thuat xuat hien 1 lan
toan xuat hien 1 lan
trinh xuat hien 2 lan
```

**5. Bài toán tìm tập hợp của 2 mảng**

**Đề bài** : Cho mảng A[] và B[] gồm N, M (1≤N, M≤106) các số nguyên 32 bit, hãy tìm những giá trị xuất hiện ít nhất ở 1 trong 2 mảng và liệt kê theo thứ tự tăng dần.

**Thuật toán** : Sử dụng map với key tương ứng là giá trị trong mảng, đưa tất cả các giá trị trong mảng A[] và B[] vào làm key của map thì map sẽ tự loại bỏ trùng những giá trị xuất hiện ở cả 2 mảng hay những giá trị xuất hiện nhiều lần trong 1 mảng. Khi đó các giá trị key trong map chính là tập hợp (Union), các giá trị mà xuất hiện ít nhất ở 1 trong 2 mảng.

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    int a[5] = {1, 2, 3, 4, 5};
    int b[5] = {4, 5, 6, 7, 8};
    map<int, int> mp;
    for(int i = 0; i < 5; i++){
        mp[a[i]] = 1;
    }
    for(int i = 0; i < 5; i++){
        mp[b[i]] = 1;
    }
    cout << "Tap hop cua a & b : ";
    for(pair<int, int> it : mp){
        cout << it.first << " ";
    }
    return 0; 
}
```

Output :

```cpp
Tap hop cua a & b : 1 2 3 4 5 6 7 8
```

**6. Bài toán tìm tập giao của 2 mảng**

**Đề bài** : Cho mảng A[] và B[] gồm N, M (1≤N, M≤106) các số nguyên 32 bit, hãy tìm những giá trị xuất hiện ở cả 2 mảng và liệt kê theo thứ tự tăng dần.

**Thuật toán** : Sử dụng map với key tương ứng là giá trị trong mảng và value có mục đích đánh dấu, đưa tất cả các giá trị trong mảng A[] vào map làm key với value tương ứng là 1. Thể hiện giá trị này xuất hiện trong mảng A[], duyệt tiếp mảng B[] và khi bạn gặp giá trị trong mảng B[] hãy check xem value của nó nếu là 1 tức là đã xuất hiện trong mảng A[] thì bạn thay value cho nó thành 2. Duyệt map và in ra những key có value là 2. Lưu ý bài này bạn không được đếm tần suất và in ra những giá trị có value là 2, vì có thể có 1 giá trị xuất hiện 2 lần trong mảng A[] nhưng không xuất hiện trong mảng B[].

**Độ phức tạp** : O(NlogN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "map"

using namespace std;

int main(){
    int a[5] = {1, 2, 3, 4, 5};
    int b[5] = {4, 5, 6, 7, 8};
    map<int, int> mp;
    for(int i = 0; i < 5; i++){
        mp[a[i]] = 1;
    }
    for(int i = 0; i < 5; i++){
        if(mp[b[i]] == 1){
            mp[b[i]] = 2;
        }
    }
    cout << "Tap giao cua a & b : ";
    for(pair<int, int> it : mp){
        if(it.second == 2)
            cout << it.first << " ";
    }
    return 0; 
}
```

Output :

```cpp
Tap giao cua a & b : 4 5
```

**Video tutorial :**
