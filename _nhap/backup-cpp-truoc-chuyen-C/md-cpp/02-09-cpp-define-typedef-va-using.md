# [C++]. Define, Typedef Và Using

Trong bài viết này mình sẽ giúp các bạn sử dụng thành thạo và phân biệt được 2 từ khóa **define** và **typedef** trong C++

**NỘI DUNG** 

- **Typedef**
- **Define**
- **Sự Khác Nhau Giữa Define Và Typedef**
- **Từ Khóa Using**

---

**1.Typedef**

**Typedef** giúp bạn tạo một tên mới cho các kiểu dữ liệu trong ngôn ngữ C++

Sau khi tạo một bí danh mới cho các kiểu dữ liệu đó thì bạn có thể sử dụng tên mới hoặc tên cũ của kiểu dữ liệu đó đều được.

Cú pháp : typedef kiểu_dữ_liệu tên_mới;

Ví dụ 1:

```cpp
#include "iostream"
#include "iomanip"
using namespace std;

typedef int songuyen;
typedef long long ll;
typedef double sothuc;
typedef bool dungsai;

int main(){
	songuyen a = 1000;
	ll b = 2828282828282;
	sothuc c = 3.1239;
	dungsai check = true;
	cout << a << " " << b << endl;
	cout << fixed << setprecision(2) << c << endl;
    return 0;
}
```

Output :

```cpp
1000 2828282828282
3.12
true
```

Ví dụ 2 : Định nghĩa tên cho kiểu pair

```cpp
#include "iostream"
#include "iomanip"
using namespace std;

typedef char kitu;
typedef pair<int, int> ii;

int main(){
	kitu x = '@';
	cout << x << endl;
	ii p = {100, 200};
	cout << p.first << ' ' << p.second << endl;
    return 0;
}
```

Output :

```cpp
@
100 200
```

---

**2.Define**

**Define** có 3 chức năng chính :

- Định nghĩa tên cho kiểu dữ liệu
- Định nghĩa tên cho giá trị
- Định nghĩa tên cho cấu trúc hoặc câu lệnh

**Định nghĩa tên cho kiểu dữ liệu** 

**Define** có thể sử dụng để làm công việc tương tự như **typedef** đó là định nghĩa tên mới cho kiểu dữ liệu

Cú pháp : #define tên_mới kiểu_dữ_liệu

Ví dụ 1 :

```cpp
#include "iostream"
#include "iomanip"
using namespace std;

#define songuyen int
#define ll long long
#define sothuc double
#define dungsai bool
#define ii pair<int, int>

int main(){
	songuyen a = 1000;
	ll b = 2828282828282;
	sothuc c = 3.1239;
	dungsai check = true;
	ii p = {100, 200};
	cout << a << " " << b << endl;
	cout << fixed << setprecision(2) << c << endl;
	cout << boolalpha << check << endl;
	cout << p.first << " " << p.second << endl;
    return 0;
}
```

Output :

```cpp
1000 2828282828282
3.12
true
100 200
```

**Định nghĩa tên cho giá trị**

**Define** được sử dụng để đặt tên cho các giá trị được sử dụng trong chương trình nhằm mục đích truyền tải ý nghĩa tốt hơn

Cú pháp :  ****#define tên_giá_trị giá_trị

Ví dụ 2 :

```cpp
#include "iostream"
#include "iomanip"
using namespace std;

#define PI 3.14
#define INF 1000000000
#define TRUE 1
#define FALSE 0
#define Tech28 "codelab.dev"
#define mod 1000000007

int main(){
	cout << fixed << setprecision(2) << PI << endl;
	cout << INF << endl;
	cout << TRUE << endl;
	cout << FALSE << endl;
	cout << Tech28 << endl;
	cout << mod << endl;
    return 0;
}
```

Output :

```cpp
3.14
1000000000
1
0
codelab.dev
1000000007
```

**Định nghĩa tên cho cấu trúc hoặc câu lệnh**

Việc sử dụng **define** để định nghĩa các câu lệnh hay cấu trúc thường được sử dụng bởi các bạn lập trình viên trong các cuộc thi về lập trình thi đấu hay thuật toán. Mục đích là có thể tiết kiệm thời gian code, tuy nhiên việc này sẽ dẫn tới khó khăn cho người khác khi cần tham khảo mã nguồn.

Hiện tại các bạn mới học lập trình thì chưa nên sử dụng **define** với mục đích này, sau này khi đã code tốt hơn các bạn có thể sử dụng nó để tiết kiệm thời gian code. Tuy nhiên mình nghĩa bạn chỉ nên sử dụng khi bạn code một mình và không cần chia sẻ mã nguồn cho người khác.

Ví dụ 3 :

```cpp
#include "iostream"
#include "iomanip"
using namespace std;

//Định nghĩa cấu trúc để in ra dòng chữ codelab.dev
#define greet cout << "codelab.dev\n";

//Định nghĩa cấu trúc vòng lặp for
#define FOR(i, a, b) for(int i = a; i <= b; i++)

//Định nghĩa cấu trúc để in ra số lớn hơn trong 2 số
#define findMax(a, b) cout << (a > b ? a : b) << endl;

int main(){
	greet;
	greet;
	findMax(10, 20);
	findMax(100, 50);
	FOR(i, 1, 5){
		cout << i << " ";
	}
    return 0;
}
```

Output :

```cpp
codelab.dev
codelab.dev
20
100
1 2 3 4 5
```

---

**3. Sự Khác Nhau Giữa Define Và Typedef**

| **Typedef** | **#Define** |
| Chỉ sử dụng để đặt tên thay thế cho kiểu dữ liệu | Có thể sử dụng để đặt tên cho kiểu dữ liệu, giá trị, cấu trúc, câu lệnh |
| Kết thúc bởi dấu ; | Không có kết thúc bằng dấu ; |
| Được xử lý bới trình biên dịch (Compiler) | Được xử lý bởi preprocessor |
| Không có dấu # | Bắt đầu bởi dấu # |

---

**4. Từ Khóa Using**

Nếu bạn sử dụng chuẩn C++11 hoặc mới hơn thì bạn có thể sử dụng using để thay cho typedef

Ví dụ :

```cpp
#include "iostream"
#include "iomanip"
using namespace std;

using ll = long long;
using ii = pair<int, int>;
using kitu = char;

int main(){
	ll n = 1923919231345;
	cout << n << endl;
	ii p = {10, 20};
	cout << p.first << ' ' << p.second << endl;
	kitu x = '@';
	cout << x << endl;
    return 0;
}
```

Output :

```cpp
1923919231345
10 20
@
```

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-09-cpp-define-typedef-va-using.md](solutions/02-09-cpp-define-typedef-va-using.md)

**Bài 1.** Dùng `typedef` đặt tên `ll` cho `long long`, `ld` cho `long double`, `ii` cho `pair<int,int>`. Viết chương trình sử dụng cả 3 bí danh này.

**Bài 2.** Làm lại bài 1 nhưng dùng từ khoá `using` thay cho `typedef`.

**Bài 3.** Dùng `#define` để định nghĩa các hằng: `PI = 3.14159`, `INF = 1000000000`, `MOD = 1000000007`. In cả 3 ra màn hình.

**Bài 4.** Viết chương trình tính diện tích hình tròn dùng `#define PI 3.14159`, sau đó viết lại bằng `const double PI`. So sánh 2 cách.

**Bài 5.** Định nghĩa macro `FOR(i, a, b)` tương đương vòng lặp `for(int i = a; i <= b; i++)`, rồi dùng nó để in các số từ 1 đến 10.

**Bài 6.** Định nghĩa macro `MAX(a, b)` trả về số lớn hơn. Thử với `MAX(3, 7)` và `MAX(2+3, 4)`.

**Bài 7.** Chạy đoạn code sau và giải thích vì sao kết quả **sai**:

```cpp
#define BINH_PHUONG(x) x * x
cout << BINH_PHUONG(2 + 3) << endl;
```

**Bài 8.** Sửa macro ở bài 7 cho đúng. Sau đó thử với `BINH_PHUONG(i++)` và giải thích vì sao vẫn có vấn đề.

**Bài 9.** Lập bảng so sánh `#define`, `typedef`, `using`, `const` theo các tiêu chí: ai xử lý (preprocessor hay compiler), có kiểm tra kiểu không, có dấu `;` không, dùng cho mục đích gì.

**Bài 10.** Dùng `#define` tạo shortcut cho các câu lệnh hay dùng trong lập trình thi đấu: `pb` (push_back), `all(v)` (v.begin(), v.end()), `fi` (first), `se` (second). Viết chương trình minh hoạ.

**Bài 11.** `typedef` có làm được việc này không: `typedef 3.14 PI;`? Thử biên dịch và giải thích.

**Bài 12.** Dùng `using` tạo bí danh cho kiểu `vector<vector<int>>` tên là `Matrix`, rồi khai báo và in một ma trận 3×3.

**Bài 13.** Tìm hiểu `#define` có điều kiện (`#ifdef`, `#ifndef`, `#endif`). Viết chương trình có chế độ DEBUG bật/tắt được bằng một dòng `#define DEBUG`.

**Bài 14.** Viết một "template thi đấu" (competitive programming template) gồm các `typedef`/`define` mà bạn thấy tiện, kèm chú thích giải thích từng dòng.

**Bài 15.** Đọc đoạn code sau (viết theo phong cách thi đấu) và viết lại thành code C++ thông thường, dễ đọc, không dùng macro:

```cpp
#define ll long long
#define pb push_back
#define all(v) v.begin(), v.end()
#define FOR(i,a,b) for(ll i=a;i<=b;i++)
int main(){
    vector<ll> v;
    FOR(i,1,5) v.pb(i*i);
    sort(all(v));
    FOR(i,0,v.size()-1) cout << v[i] << " ";
}
```
