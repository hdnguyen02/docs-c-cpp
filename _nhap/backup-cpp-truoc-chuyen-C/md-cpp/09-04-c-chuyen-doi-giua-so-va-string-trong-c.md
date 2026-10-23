# [C++]. Chuyển Đổi Giữa Số Và String Trong C++

Để chuyển số thành string hay chuyển string thành số bạn có thể sử dụng hàm có sẵn hoặc tự cài đặt, bài viết này mình sẽ hướng dẫn các bạn những hàm thông dụng trong việc chuyển đổi số và xâu ký tự.

**NỘI DUNG :** 

- **Chuyển đổi xâu thành số**
- **Chuyển đổi số thành xâu**
- **Video tutorial** 

---

**1. Chuyển Đổi Xâu Thành Số**

Trong quá trình học lập trình đôi khi bạn sẽ cần chuyển đổi xâu string thành một số nguyên hoặc một số thực, C++ đã cung cấp sẵn cho bạn các hàm này và bạn có thể sử dụng ngay.

Lưu ý là các hàm này chỉ có từ chuẩn **C++11** trở lên tới các phiên bản sau này nên hãy đảm bảo việc bạn có thể sử dụng C++ khi đi thi, nếu không bạn cần dự trù việc tự cài đặt nó.

Tổng hợp các hàm thông dụng chuyển xâu thành số :

| **Hàm** | **Chức năng** |
| stoi() | Chuyển string thành số int |
| stoll() | Chuyển string thành số long long |
| stol() | Chuyển string thành số long (tương tự int) |
| stof() | Chuyển string thành số float |
| stod() | Chuyển string thành số double |
| stold() | Chuyển string thành số long double |
| stoul() | Chuyển string thành số long không dấu |
| stoull() | Chuyển string thành số long long không dấu |

Tuy nhiên chủ yếu bạn sử dụng 3 hàm : **stoi()**,** stoll() **và** stod()**

**stoi() : Chuyển string thành số int**

Lưu ý khi sử dụng stoi() :

- Dữ liệu cần đảm bảo có thể lưu trong giới hạn của int, nếu không sẽ gây ra ngoại lệ std::out_of_range. Tương tự nếu xâu rỗng cũng sẽ gây lỗi.
- Nếu xâu có thêm chữ cái hoặc ký tự đặc biệt không phải chữ số thì hàm sẽ convert tới kí tự đặc biệt đó mà thôi\

Ví dụ :

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
	string s1 = "282828";
	string s2 = "-292828";
	string s3 = "2828codelab.dev";
	int n1 = stoi(s1);
	int n2 = stoi(s2);
	int n3 = stoi(s3);
	cout << n1 << endl;
	cout << n2 << endl;
	cout << n3 << endl;
	return 0;
}
```

Output :

```cpp
282828
-292828
282828
```

**stoll() : Chuyển string thành số long long**

Ví dụ :

```cpp
#include "iostream"
#include "string"

using namespace std;

int main(){
	string s1 = "100000000000000000";
	string s2 = "-100000000000000000";
	string s3 = "28282828282828codelab.dev";
	long long n1 = stoll(s1);
	long long n2 = stoll(s2);
	long long n3 = stoll(s3);
	cout << n1 << endl;
	cout << n2 << endl;
	cout << n3 << endl;
	return 0;
}
```

Output :

```cpp
100000000000000000
-100000000000000000
2828282828282828
```

**stod() : Chuyển string thành số double**

Ví dụ :

```cpp
#include "iostream"
#include "string"
#include "iomanip"
using namespace std;

int main(){
	string s1 = "100.123";
	string s2 = "-100.456";
	string s3 = "28282.codelab.dev";
	double n1 = stod(s1);
	double n2 = stod(s2);
	double n3 = stod(s3);
	cout << fixed << setprecision(3) << n1 << endl;
	cout << fixed << setprecision(3) << n2 << endl;
	cout << fixed << setprecision(3) << n3 << endl;
	return 0;
}
```

Output :

```cpp
100.123
-100.456
28282.280
```

---

**2. Chuyển Đổi Số Thành Xâu**

Hàm **to_string()** trong C++ sẽ giúp bạn chuyển đối số thành xâu. Lưu ý hàm này chỉ hỗ trợ từ C++11 trở lên, nếu bạn làm việc với các chuẩn C++11 hoặc mới hơn hay làm bài trên các website chấm bài online thì có thể dùng hàm này một cách thoải mái.

Ví dụ :

```cpp
#include "iostream"
#include "string"
#include "iomanip"
using namespace std;

int main(){
	int n = 28282828;
	string s = to_string(n);
	cout << s << endl;
	return 0;
}
```

Output :

```cpp
28282828
```

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-04-c-chuyen-doi-giua-so-va-string-trong-c.md](solutions/09-04-c-chuyen-doi-giua-so-va-string-trong-c.md)

**Bài 1.** Dùng `to_string()` chuyển các kiểu `int`, `long long`, `float`, `double` sang chuỗi và in ra.

**Bài 2.** Dùng `stoi`, `stoll`, `stof`, `stod` chuyển chuỗi sang số.

**Bài 3.** Xử lý lỗi khi chuỗi không phải số: bắt `invalid_argument` và `out_of_range`.

**Bài 4.** Chuyển một số nguyên thành chuỗi **không dùng** `to_string` (tự viết bằng phép chia lấy dư).

**Bài 5.** Chuyển một chuỗi số thành số nguyên **không dùng** `stoi` (tự viết).

**Bài 6.** Dùng `stoi` với tham số cơ số: chuyển chuỗi nhị phân, bát phân, thập lục phân sang số thập phân.

**Bài 7.** Chuyển một số thập phân sang chuỗi nhị phân, bát phân, thập lục phân.

**Bài 8.** Dùng `stringstream` để chuyển đổi số ↔ chuỗi. So sánh với `to_string`/`stoi`.

**Bài 9.** Định dạng số thực thành chuỗi với đúng `k` chữ số thập phân.

**Bài 10.** Viết hàm định dạng số tiền có dấu chấm phân cách hàng nghìn: `1234567` → `1.234.567`.

**Bài 11.** Đọc một dòng chứa nhiều số cách nhau bởi dấu cách, chuyển tất cả thành `vector<int>`.

**Bài 12.** Kiểm tra một chuỗi có phải số hợp lệ không (có thể có dấu âm, phần thập phân).

**Bài 13.** Chuyển một chuỗi biểu thức đơn giản `"12+34"` thành 2 số rồi tính tổng.

**Bài 14.** Viết hàm chuyển số thành chữ tiếng Việt: `123` → `mot tram hai muoi ba`.

**Bài 15.** Viết một "thư viện chuyển đổi" với các hàm an toàn: `toInt`, `toDouble`, `toStr`, `isNumber`, `formatMoney`, `toBase`.
