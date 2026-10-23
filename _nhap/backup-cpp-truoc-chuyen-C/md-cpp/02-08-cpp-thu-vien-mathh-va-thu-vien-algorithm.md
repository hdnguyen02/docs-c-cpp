# [C++]. Thư Viện Math.h Và Thư Viện Algorithm

Trong quá trình lập trình việc sử dụng các hàm toán học là rất phổ biến, ngôn ngữ C++ cung cấp cho bạn một thư viện là **math.h** chứa các hàm toán học và thư viện **Algorithm** chứa các hàm thuật toán. Bài viết này mình sẽ cung cấp cho bạn cách sử dụng và ví dụ minh họa cho các hàm toán học và thuật toán thông dụng.

**NỘI DUNG :** 

- **Các Hàm Toán Học Phổ Biến**
- **Thư Viện Algorithm**
- **Ví Dụ** 

---

**1. Các Hàm Toán Học Phổ Biến**

Các hàm toán học trong thư viện **math.h** đều có tham số là một số thuộc kiểu double và có kiểu trả về là double, bạn không cần phải nhớ hết mọi hàm mà chỉ cần nhớ cho mình một vài hàm quan trọng được sử dụng thường xuyên.

| **STT** | **Hàm** | **Chức năng** |
| 1 | pow(x, y) | Trả về xy |
| 2 | sqrt(x) | Trả về căn bậc 2 của x |
| 3 | cbrt(x) | Trả về căn bậc 3 của x |
| 4 | ceil(x) | Trả về số nguyên nhỏ nhất lớn hơn hoặc bằng x, tương đương phép làm tròn lên |
| 5 | floor(x) | Trả về số nguyên lớn nhất nhỏ hơn hoặc bằng x, tương đương phép làm tròn xuống |
| 6 | round(x) | Trả về số nguyên gần x nhất phụ thuộc phần thập phân |
| 7 | fabs(x) | Trả về trị tuyệt đối của số x |
| 8 | exp(x) | Trả về ex |
| 9 | fmod(x, y) | Trả về số dư khi chia x cho y |
| 10 | log(x) | Trả về logarit tự nhiên của x |
| 11 | log10(x) | Trả về logarit thập phân của x |
| 12 | cos(x) | Trả về giá trị hàm cos với x là radian |
| 13 | sin(x) | Trả về giá trị hàm sin với x là radian |
| 14 | tan(x) | Trả về giá trị hàm tan với x là radian |
| 15 | acos(x) | Trả về giá trị hàm arccos với x là radian |
| 16 | asin(x) | Trả về giá trị hàm arcsin với x là radian |
| 17 | atan(x) | Trả về giá trị hàm arctan với x là radian |

**Hàm pow(x,y)** : Trả về lũy thừa xy, lưu ý là hàm này trả về số thực double nên nếu bạn muốn tính lũy thừa với x và y nguyên thì cần lưu kết quả dưới dạng số nguyên hoặc ép kiểu khi in ra.

Ví dụ 1:

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	int a = 2, b = 10;
    cout << a << "^" << b << " = " << (int)pow(a, b) << endl;
    //Tính căn bậc 5
    int n = 100;
    double res = pow(n, 1.0 / 5);
    cout << fixed << setprecision(3) << res << endl;
    return 0;
}
```

Output :

```cpp
2^10 = 1024
2.512
```

**Hàm sqrt(x)** : Tính căn bậc 2 của x

Ví dụ 2 :

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	int n = 100;
	int can = (int)sqrt(n);
	cout << can << endl;
	
	double res = sqrt(1000);
	cout << fixed << setprecision(2) << res << endl;
    return 0;
}
```

Output :

```cpp
10
31.62
```

**Hàm cbrt(x)** : Trả về căn bậc 3 của x

Ví dụ 3 :

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	int n = 27;
	int can = (int)cbrt(n);
	cout << can << endl;

	double res = cbrt(100);
	cout << fixed << setprecision(2) << res << endl;
    return 0;
}
```

Output :

```cpp
3
4.64
```

**Hàm ceil(x)** : Trả về số nguyên khi làm tròn phần thập phân của x lên, ví dụ x là 2.3 hay 2.8 thì khi sử dụng hàm ceil ta sẽ thu được số 3.

Ví dụ 4 :

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	double a = 3.14;
	double b = 3.8;
	cout << (int)ceil(a) << " " << (int)ceil(b) << endl;
    return 0;
}
```

Output :

```cpp
4 4
```

**Hàm floor(x)** : Trả về số nguyên khi làm tròn phần thập phân của x xuống, ví dụ x là 2.3 hay 2.8 thì khi sử dụng hàm ceil ta sẽ thu được số 2.

Ví dụ 5 :

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	double a = 3.14;
	double b = 3.8;
	cout << (int)floor(a) << " " << (int)floor(b) << endl;
    return 0;
}
```

Output :

```cpp
3 3
```

**Hàm round(x)** : Làm tròn dựa vào phần thập phân của x, nếu phần thập phân của x lớn hơn hoặc bằng 0.5 thì sẽ làm tròn lên, ngược lại sẽ làm tròn xuống

Ví dụ 6 :

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	double a = 3.14;
	double b = 3.8;
	cout << (int)round(a) << " " << (int)round(b) << endl;
    return 0;
}
```

Output :

```cpp
3 4
```

**Hàm abs(x)** : Trả về giá trị tuyệt đối của x, hàm này nằm trong thư viện stdlib.h

Ví dụ 7 :

```cpp
#include "iostream"
#include "math.h"
#include "iomanip"
using namespace std;

int main(){
	cout << abs(10) << " " << abs(-100) << endl;
    return 0;
}
```

Output :

```cpp
10 100
```

---

**2. Thư Viện Algorithm**

Algorithm là thư viện chứa các hàm thuật toán phổ biến, tuy nhiên các hàm này chủ yếu dùng cho dãy mảng. Hiện tại bạn sẽ làm quen với một vài hàm cơ bản trong thư viện này trước, sau khi học phần mảng thì mình sẽ giới thiệu các hàm khác trong thư viện này.

Khi sử dụng thư viện này bạn cần inlcude vào chương trình của mình.

**Hàm swap**

Hàm này sẽ hoán đổi giá trị của 2 biến, bạn có thể tự code hoán đổi giá trị 2 biến hoặc sử dụng hàm có sẵn.

```cpp
#include "iostream"
#include "algorithm"
#include "iomanip"
using namespace std;

int main(){
	int a = 100, b = 200;
	//Dùng hàm có sẵn
	swap(a, b);
	cout << a << " " << b << endl;
	//Tự code
	char x = '@', y = '#';
	char temp = x;
	x = y;
	y = temp;
	cout << x << ' ' << y << endl;
    return 0;
}
```

Output :

```cpp
200 100
# @
```

**Hàm min**

Hàm min sẽ trả về giá trị nhỏ hơn trong 2 hoặc nhiều số, trong trường hợp bạn áp dụng hàm min với nhiều số thì cần thêm ngoặc nhọn {}

```cpp
#include "iostream"
#include "algorithm"
#include "iomanip"
using namespace std;

int main(){
	int a = 100, b = 200;
	cout << "Min(" << a << ", " << b << ") = " << min(a, b) << endl;
	cout << "Min(10, 20, 15, 4) = " << min({10, 20, 15, 4}) << endl;
	cout << "Min('d', 'b', 'z',) = " << min({'d', 'b', 'z'}) << endl;
    return 0;
}
```

Output :

```cpp
Min(100, 200) = 100
Min(10, 20, 15, 4) = 4
Min('d', 'b', 'z',) = b
```

**Hàm max**

Hàm max sẽ trả về giá trị lớn hơn trong 2 hoặc nhiều số, trong trường hợp bạn áp dụng hàm max với nhiều số thì cần thêm ngoặc nhọn {}

```cpp
#include "iostream"
#include "algorithm"
#include "iomanip"
using namespace std;

int main(){
	int a = 100, b = 200;
	cout << "Max(" << a << ", " << b << ") = " << max(a, b) << endl;
	cout << "Max(10, 20, 15, 4) = " << max({10, 20, 15, 4}) << endl;
	cout << "Max('d', 'b', 'z',) = " << max({'d', 'b', 'z'}) << endl;
    return 0;
}
```

Output :

```cpp
Max(100, 200) = 200
Max(10, 20, 15, 4) = 20
Max('d', 'b', 'z',) = z
```

**Xem thêm bài giảng của mình về Hàm Toán Học trong C++ :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-08-cpp-thu-vien-mathh-va-thu-vien-algorithm.md](solutions/02-08-cpp-thu-vien-mathh-va-thu-vien-algorithm.md)

**Bài 1.** Nhập 2 số `x`, `y`. Tính và in ra `x^y`, `sqrt(x)`, `cbrt(x)`, `log(x)`, `log10(x)` với 4 chữ số thập phân.

**Bài 2.** Nhập một số thực `x`. In ra kết quả của `ceil(x)`, `floor(x)`, `round(x)` và giải thích sự khác nhau của 3 hàm.

**Bài 3.** Nhập 3 cạnh tam giác `a`, `b`, `c`. Dùng công thức Heron tính diện tích tam giác.

**Bài 4.** Nhập toạ độ 2 điểm, tính khoảng cách Euclid bằng `sqrt` và `pow`.

**Bài 5.** Giải phương trình bậc hai `ax² + bx + c = 0`, dùng `sqrt` để tính nghiệm.

**Bài 6.** Nhập một số nguyên `n`. Kiểm tra `n` có phải số chính phương không (dùng `sqrt`). Chú ý xử lý sai số số thực.

**Bài 7.** Chạy đoạn code sau và giải thích vì sao kết quả có thể **sai**:

```cpp
int n = 25;
int can = sqrt(n);
cout << (can * can == n) << endl;

int m = pow(10, 2);
cout << m << endl;
```

**Bài 8.** Nhập góc theo độ, chuyển sang radian rồi tính `sin`, `cos`, `tan` của góc đó.

**Bài 9.** Nhập 3 số nguyên, dùng hàm `max` và `min` của thư viện `algorithm` để tìm số lớn nhất và nhỏ nhất.

**Bài 10.** Dùng `swap` để hoán đổi giá trị 2 biến kiểu `int`, 2 biến kiểu `string`, và 2 phần tử của mảng.

**Bài 11.** Nhập 4 số, dùng `max({a,b,c,d})` (cú pháp C++11 với initializer list) để tìm số lớn nhất.

**Bài 12.** So sánh `abs`, `fabs`, và `labs`. Viết chương trình minh hoạ sự khác nhau khi dùng với `int`, `double`, `long`.

**Bài 13.** Viết chương trình làm tròn một số thực đến `k` chữ số thập phân (ví dụ `3.14159` với `k = 2` → `3.14`) bằng `round`.

**Bài 14.** Nhập số tiền gốc `P`, lãi suất `r` (%/năm), số năm `n`. Tính số tiền nhận được theo công thức lãi kép `A = P(1 + r/100)^n` dùng `pow`.

**Bài 15.** Viết chương trình tính tổng `S = 1 + 1/2 + 1/3 + ... + 1/n` và so sánh với `log(n) + 0.5772` (hằng số Euler–Mascheroni).
