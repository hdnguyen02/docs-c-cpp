# [C++]. Hàm Sort Trong C++

Hàm **sort()** trong thư viện algorithm của ngôn ngữ lập trình C++ là một hàm thuật toán rất hiệu quả và được sử dụng thường xuyên trong lập trình. Bài học này sẽ hướng dẫn các bạn cách sử dụng hàm sort() để sắp xếp với mảng, vector, string..

**NỘI DUNG :** 

- **Hàm sort() trong C++**
- **Một số bài tập áp dụng hàm sort()**
- **Video tutorial** 

---

**1. Hàm sort() trong C++**

Hàm **sort()** trong C++ là hàm thuật toán thuộc thư viện algorithm, bạn có thể sử dụng ngay hàm này khi cần sắp xếp mà không cần cài đặt lại từ đầu.

Hàm sort() được cài đặt trong C++ là hàm **intro - sort**, đây là sự kết hợp của 2 thuật toán sắp xếp rất hiệu quả là** quick sort **và** heap sort **

Độ phức tạp của hàm sort() là O(NlogN). Bạn có thể sử dụng hàm này để sắp xếp mảng, vector, string.

Mặc định thì hàm này sẽ sắp xếp mảng của bạn tăng dần về giá trị số hoặc từ điển, nếu muốn sắp xếp giảm dần bạn cần thêm tham số **greater()**

**Cú pháp sort mảng :** 

```cpp
//Sắp xếp toàn bộ mảng a có n phần tử
sort(a, a + n);
//Sắp xếp mảng a từ chỉ số x tới chỉ số y
sort(a + x, a + y + 1);
//Sắp xếp mảng giảm dần
sort(a, a + n, greater<data_type>());
```

**Ví dụ 1 :** 

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
	int a[] = {3, 1, 2, 5, 6, 4, 8, 9, 10, 7};
	int n = 10;
	sort(a, a + n);
	cout << "Mang a sau khi sap xep tang dan : ";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
	sort(a, a + n, greater<int>());
	cout << "\nMang a sau khi sap xep giam dan : ";
	for(int i = 0; i < n; i++){
		cout << a[i] << " ";
	}
}
```

Output :

```cpp
Mang a sau khi sap xep tang dan : 1 2 3 4 5 6 7 8 9 10 
Mang a sau khi sap xep giam dan : 10 9 8 7 6 5 4 3 2 1
```

Nếu bạn có mảng string hay mảng char thì hàm sort() sẽ sắp xếp mặc định theo thứ tự từ điển tăng dần.

**Ví dụ 2 :** 

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
	char a[] = {'2', '8', 't', 'e', 'c', 'h', 'a', 'z'};
	int n = 8;
	sort(a, a + n);
	cout << "Mang char sap tang dan : ";
	for(int i = 0; i < n; i++){
		cout << a[i] << ' ';
	}
	sort(a, a + n, greater<char>());
	cout << "\nMang char sap giam dan : ";
	for(int i = 0; i < n; i++){
		cout << a[i] << ' ';
	}
}
```

Output :

```cpp
Mang char sap tang dan : 2 8 a c e h t z 
Mang char sap giam dan : z t h e c a 8 2
```

**Cú pháp sắp xếp vector :** 

```cpp
//Sắp xếp toàn bộ vector a có n phần tử
sort(a.begin(), a.end());
//Sắp xếp vector a từ chỉ số x tới chỉ số y
sort(a.begin() + x, a.begin() + y + 1);
//Sắp xếp vector giảm dần
sort(a.begin(), a.end(), greater<data_type>());
```

**Ví dụ 3 :** 

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
	vector<int> v = {3, 1, 2, 5, 4};
	sort(v.begin(), v.end());
	cout << "Vector sap tang dan : ";
	for(int i = 0; i < v.size(); i++){
		cout << v[i] << " ";
	}
	sort(v.begin(), v.end(), greater<int>());
	cout << "\nVector sap giam dan : ";
	for(int i = 0; i < v.size(); i++){
		cout << v[i] << " ";
	}
}
```

Output :

```cpp
Vector sap tang dan : 1 2 3 4 5 
Vector sap giam dan : 5 4 3 2 1
```

---

**2. Một số bài tập áp dụng hàm sort()**

Có nhiều bài toán mà bạn có thể sử dụng bước sắp xếp trước khi xử lý, phần này mình sẽ hướng dẫn các bạn 3 ví dụ để luyện tập với hàm sort.

**Bài 1**. Đếm số lượng giá trị khác nhau trong mảng

**Thuật toán** : Sắp xếp mảng tăng dần để các giá trị giống nhau sẽ đứng cạnh nhau, khi đó bạn chỉ cần so sánh 2 phần tử kề nhau trong mảng để đếm số giá trị khác nhau. Nếu 2 phần tử đứng cạnh nhau mà bằng nhau thì bạn không cần tăng số giá trị khác nhau lên.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
	int a[] = {1, 3, 3, 3, 2, 1, 2, 2, 2, 4, 0, 2};
	int n = 12;
	sort(a, a + n);
	int dem = 1; // a[0]
	for(int i = 1; i < n; i++){
		if(a[i] != a[i - 1]){
			++dem;
		}
	}
	cout << "So gia tri khac nhau : " << dem << endl;
}
```

Output :

```cpp
So gia tri khac nhau : 5
```

**Bài 2** : Tìm độ chênh lệch nhỏ nhất giữa 2 phần tử trong mảng

**Thuật toán** : Sắp xếp mảng tăng dần (hoặc giảm dần) để những giá trị gần nhau sẽ đứng cạnh nhau khi đó bạn chỉ cần xét độ chênh lệch giữa 2 phần tử đứng cạnh nhau và tìm giá trị nhỏ nhất.

Độ phức tạp sẽ là O(NlogN) thay vì O(N2) nếu bạn dùng 2 for lồng nhau để xét mọi cặp phần tử trong mảng

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
	int a[] = {3, 8, 10, 4, 12, 21, 1};
	int n = 7;
	sort(a, a + n);
	int max_diff = 1000000000;
	for(int i = 1; i < n; i++){
		if(a[i] - a[i - 1] < max_diff){
			max_diff = a[i] - a[i - 1];
		}
	}
	cout << "Do chenh lech nho nhat : " << max_diff << endl;
}
```

Output :

```cpp
Do chenh lech nho nhat : 1
```

**Bài 3**. Đếm tần suất xuất hiện của từng giá trị trong mảng và liệt kê theo thứ tự từ nhỏ tới lớn

**Thuật toán** : Sắp xếp mảng tăng dần sau đó xét các cặp phần tử đứng cạnh nhau để đếm tần suất xuất hiện, vì khi sắp tăng dần thì các giá trị giống nhau sẽ đứng cạnh nhau.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
	int a[] = {1, 3, 3, 3, 2, 1, 2, 4, 2, 4, 0, 2};
	int n = 12;
	sort(a, a + n);
	int dem = 1; // a[0];
	for(int i = 1; i < n; i++){
		if(a[i] == a[i - 1]){
			++dem;
		}
		else{
			cout << a[i - 1] << " xuat hien " << dem << " lan\n";
			dem = 1;
		}
	}
	cout << a[n - 1] << " xuat hien " << dem << " lan\n";
}
```

Output :

```cpp
0 xuat hien 1 lan
1 xuat hien 2 lan
2 xuat hien 4 lan
3 xuat hien 3 lan
4 xuat hien 2 lan
```

---

**Video tutorial:**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/10-02-c-ham-sort-trong-c.md](solutions/10-02-c-ham-sort-trong-c.md)

**Bài 1.** Sắp xếp mảng tĩnh và `vector` tăng dần bằng `sort`.

**Bài 2.** Sắp xếp giảm dần bằng 3 cách: `greater<int>()`, lambda, và `rbegin/rend`.

**Bài 3.** Sắp xếp chỉ một **phần** của mảng (từ vị trí 2 đến 7).

**Bài 4.** Sắp xếp `vector<string>` theo thứ tự từ điển và theo độ dài.

**Bài 5.** Sắp xếp `vector<pair<int,int>>` — quan sát thứ tự mặc định.

**Bài 6.** Sắp xếp mảng struct sinh viên theo điểm giảm dần.

**Bài 7.** Sắp xếp theo nhiều tiêu chí: điểm giảm dần, cùng điểm thì tên tăng dần.

**Bài 8.** Sắp xếp số theo trị tuyệt đối.

**Bài 9.** Sắp xếp sao cho số chẵn đứng trước số lẻ, mỗi nhóm tăng dần.

**Bài 10.** Dùng `partial_sort` để lấy 5 phần tử nhỏ nhất mà không sắp xếp toàn mảng.

**Bài 11.** Dùng `nth_element` tìm phần tử lớn thứ `k`.

**Bài 12.** So sánh tốc độ `sort` với Bubble Sort tự viết trên mảng 100.000 phần tử.

**Bài 13.** Tìm hiểu `sort` dùng thuật toán gì. Giải thích Introsort.

**Bài 14.** Chương trình sau bị crash. Tìm lỗi trong hàm so sánh:

```cpp
sort(v.begin(), v.end(), [](int a, int b){ return a <= b; });
```

**Bài 15.** Viết chương trình quản lý điểm: nhập danh sách, cho phép sắp xếp theo nhiều tiêu chí do người dùng chọn.
