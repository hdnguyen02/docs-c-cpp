# [C++]. Xây Dựng Comparison Function Cho Hàm ...

Để sử dụng hàm sort() trong C++ một cách linh hoạt thì bạn cần biết xây dựng hàm so sánh - **comparison function** cho nó. Hiểu đơn giản thì hàm so sánh sẽ quyết định thứ tự sắp xếp các phần tử.

**NỘI DUNG :** 

- **Xây dựng comparison function**
- **Sắp xếp mảng với nhiều hơn 2 tiêu chí**
- **Video tutorial** 

---

**1. Xây dựng comparison function** 

Hàm so sánh khi sử dụng hàm sort chính là tham số thứ 3 mà bạn sẽ truyền vào hàm khi sắp xếp mảng, vector.

Hàm này có kiểu trả về là true hoặc false và có 2 tham số với kiểu dữ liệu tương ứng với mảng mà bạn muốn sắp xếp.

Tên của hàm so sánh bạn tự đặt, thông thường mình hay đặt là cmp.

**Cú pháp hàm so sánh :** 

```cpp
bool cmp(data_type x, data_type  y){ 
     //logic
}
```

Logic khi trả về giá trị của hàm so sánh :

- Nếu muốn x đứng trước y sau khi sắp xếp thì trả về true
- Nếu muốn x đứng sau y sau khi sắp xếp thì trả về false

x và y ở đây bạn có thể coi như đó là 2 giá trị trong mảng mà bạn cần sắp xếp, khi sắp xếp thì hàm sort cần so sánh giá trị giữa 2 phần tử này. Bạn chỉ cần kiểm tra xem thứ tự của x và y có thỏa mãn x sẽ đứng trước y theo thứ tự sắp xếp của mảng không thì bạn trả về true, ngược lạ trả về false.

Ví dụ như bạn muốn sắp xếp mảng tăng dần, vậy thì x nhỏ hơn y sẽ đứng trước y, khi đó bạn kiểm tra nếu x < y thì bạn trả về true, ngược lại trả về false.

**Ví dụ 1** : Sắp xếp mảng giảm dần

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

bool cmp1(int a, int b){
	if(a > b)
		return true;
	else
		return false;
}

int main(){
	int a[] = {1, 3, 3, 3, 2, 1, 2, 4, 2, 4, 0, 2};
	int n = 12;
	sort(a, a + n, cmp1);
	cout << "Mang giam dan : ";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
}
```

Output :

```cpp
Mang giam dan : 4 4 3 3 3 2 2 2 2 1 1 0
```

**Ví dụ 2** : Sắp xếp mảng theo tổng chữ số tăng dần

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int tong(int n){
	int ans = 0;
	while(n){
		ans += n % 10;
		n /= 10;
	}
	return ans;
}

bool cmp1(int a, int b){
	if(tong(a) < tong(b))
		return true;
	else return false;
}

int main(){
	int a[] = {1000000, 212, 40, 9, 10001, 30, 449};
	int n = 7;
	sort(a, a + n, cmp1);
	cout << "Mang sap xep theo tong chu so tang dan : \n";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
}
```

Output :

```cpp
Mang sap xep theo tong chu so tang dan : 
1000000 10001 30 40 212 9 449
```

**Ví dụ 3** : Sắp xếp theo trị tuyệt đối giảm dần

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

bool cmp(int a, int b){
	if(abs(a) > abs(b))
		return true;
	else
		return false;
}

int main(){
	int a[] = {3, -5, -1, 4, -2, 6, -7};
	int n = 7;
	sort(a, a + n, cmp);
	cout << "Mang sap xep theo tri tuyet doi giam dan : \n";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
}
```

Output :

```cpp
Mang sap xep theo tri tuyet doi giam dan : 
-7 6 -5 4 3 -2 -1
```

---

**2. Sắp xếp mảng với nhiều hơn 2 tiêu chí**

Thông thường khi sắp xếp mảng sẽ có những giá trị có cùng thứ tự sắp xếp và khi đó họ sẽ yêu cầu bạn thêm 1 tiêu chí phụ nữa.

Ví dụ sắp xếp danh sách sinh viên theo gpa giảm dần, nếu 2 sinh viên có cùng gpa thì sinh viên nào có tên từ điển nhỏ hơn sẽ đứng trước.

Thậm chí đề bài có thể yêu cầu nhiều hơn 2 tiêu chí, tuy nhiên đối với đề bài yêu cầu kiểu này các bạn chỉ cần xét từ tiêu chí ưu tiên đầu tiên tới tiêu chí ưu tiên cuối cùng là được.

Nếu có thể sắp xếp theo tiêu chí chính thì không cần quan tâm tới tiêu chí phụ.

**Ví dụ 1** : Sắp xếp mảng theo tổng chữ số tăng dần, nếu 2 số có cùng tổng chữ số thì số lớn hơn sẽ đứng trước.

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int tong(int n){
	int ans = 0;
	while(n){
		ans += n % 10;
		n /= 10;
	}
	return ans;
}

bool cmp(int a, int b){
	if(tong(a) != tong(b)){
		return tong(a) < tong(b); // co the thay bang if else
	}
	else{
		return a > b; //co the thay bang if else
	}
}

int main(){
	int a[] = {111, 9, 3000, 20001, 18, 81, 405, 200, 1001};
	int n = 9;
	sort(a, a + n, cmp);
	cout << "Mang sau khi sap xep : \n";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
}
```

Output :

```cpp
Mang sau khi sap xep : 
1001 200 20001 3000 111 405 81 18 9
```

**Ví dụ 2** : Sắp xếp sao cho số chẵn đứng trước, lẻ đứng sau, chẵn giảm dần, lẻ tăng dần

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

bool cmp(int a, int b){
	int r1 = a % 2, r2 = b % 2;
	if(r1 == 0 && r2 == 1) return true;
	if(r1 == 1 && r2 == 0) return false;
	if(r1 == 0 && r2 == 0) return a > b;
	if(r1 == 1 && r2 == 1) return a < b;
}

int main(){
	int a[] = {1, 2, 10, 9, 6, 5, 8, 7, 4, 3};
	int n = 10;
	sort(a, a + n, cmp);
	cout << "Mang sau khi sap xep : \n";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
}
```

**Ví dụ 3** : Sắp xếp các điểm trong hệ tọa độ Oxy sao cho hoành độ tăng dần, nếu hoành độ bằng nhau thì sắp xếp theo tung độ giảm dần

Ở đây mình sẽ dùng pair để lưu điểm trong hệ tọa độ Oxy.

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

bool cmp(pair<int, int> x, pair<int, int> y){
	if(x.first != y.first)
		return x.first < y.first;
	else
		return x.second > y.second;
}

int main(){
	pair<int, int> a[] = {{3, 1}, {3, 2}, {1, 4}, {4, 3}, {3, 3}, {1, 1}, {4, 2}};
	int n = 7;
	sort(a, a + n, cmp);
	cout << "Mang sau khi sap xep : \n";
	for(pair<int, int> it : a){
		cout << it.first << " " << it.second << endl;
	}
}
```

Output :

```cpp
Mang sau khi sap xep : 
1 4
1 1
3 3
3 2
3 1
4 3
4 2
```

---

**Video tutorial:**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-03-c-xay-dung-comparison-function-cho-ham-sort-trong-c.md](solutions/10-03-c-xay-dung-comparison-function-cho-ham-sort-trong-c.md)

**Bài 1.** Viết comparison function dạng **hàm thường** để sắp xếp giảm dần.

**Bài 2.** Viết comparison function dạng **lambda**. So sánh với hàm thường.

**Bài 3.** Viết comparison function dạng **functor** (struct có `operator()`).

**Bài 4.** Sắp xếp `vector<pair<string,int>>` theo `second` giảm dần.

**Bài 5.** Sắp xếp struct sinh viên theo 3 tiêu chí: điểm giảm, tuổi tăng, tên A-Z.

**Bài 6.** Viết comparator sắp xếp số theo tổng chữ số.

**Bài 7.** Viết comparator sắp xếp chuỗi theo số nguyên âm trong chuỗi.

**Bài 8.** Viết comparator nhận tham số bên ngoài (dùng lambda capture) — sắp xếp theo khoảng cách tới một điểm cho trước.

**Bài 9.** Viết comparator cho `sort` mảng ngày tháng dạng `"dd/mm/yyyy"`.

**Bài 10.** Nạp chồng `operator<` cho struct để `sort` dùng được mà không cần comparator.

**Bài 11.** Comparator nào dưới đây sai? Giải thích:

```cpp
auto c1 = [](int a, int b){ return a < b; };
auto c2 = [](int a, int b){ return a <= b; };
auto c3 = [](int a, int b){ return abs(a) < abs(b); };
auto c4 = [](int a, int b){ return true; };
```

**Bài 12.** Dùng comparator để sắp xếp `map` theo giá trị (chuyển sang `vector` trước).

**Bài 13.** Viết comparator sắp xếp "ưu tiên": các phần tử trong danh sách ưu tiên đứng trước, còn lại xếp sau.

**Bài 14.** So sánh tốc độ 3 dạng comparator (hàm, lambda, functor) trên mảng 1 triệu phần tử.

**Bài 15.** Viết "bộ sưu tập comparator" tái sử dụng được cho các bài tập sắp xếp thường gặp.
