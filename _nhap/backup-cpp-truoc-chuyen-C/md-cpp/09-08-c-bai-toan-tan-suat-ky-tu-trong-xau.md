# [C++]. Bài Toán Tần Suất Ký Tự Trong Xâu

Đếm tần suất ký tự trong xâu và các bài toán liên quan tới sự xuất hiện của ký tự trong xâu các bạn có thể sử dụng mảng đánh dấu hoặc map. Trong bài viết này mình sẽ hướng dẫn các bạn dạng bài tập này và một vài bài tập ví dụ minh họa

**NỘI DUNG :** 

- **Đếm tần suất ký tự bằng mảng đánh dấu**
- **Đếm tần suất ký tự bằng map**
- **Bài tập áp dụng**
- **Video tutorial** 

---

**1. Đếm tần suất ký tự bằng mảng đánh dấu**

Để đếm xem mỗi ký tự trong xâu xuất hiện bao nhiêu lần bạn có thể sử dụng kỹ thuật mảng đánh dấu, nếu bạn chưa biết kỹ thuật này có thể tham khảo [tại đây](https://blog.codelab.dev/cpp-mang-danh-dau)

Ý tưởng là mình sẽ sử dụng mã ASCII của các ký tự để đếm tần suất tương ứng của ký tự đó, các ký tự trong bảng mã ASCII có thứ tự từ 0 tới 255 nên bạn chỉ cần sử dụng một mảng đánh dấu có 256 phần tử là có thể đếm được tần suất.

Ví dụ khi gặp kí tự 'a' trong xâu ký tự thì bạn sẽ đếm tần suất của nó thông qua phần tử có chỉ số 97 của mảng đánh dấu, vì 'a' có mã ASCII là 97

Sau khi bạn tìm được tần suất của từng ký tự bạn có thể triển khai nhiều bài toán mở rộng khác.

Độ phức tạp : O(N)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
	string s = "codelab codelab aaa";
	int cnt[256] = {0};
	for(int i = 0; i < s.size(); i++){
		cnt[s[i]]++;
	}
	for(int i = 0; i < 256; i++){
		if(cnt[i] != 0){
			cout << (char)i << " xuat hien " << cnt[i] << "lan\n";
		}
	}
}
```

Output :

```cpp
  xuat hien 2lan
2 xuat hien 2lan
8 xuat hien 2lan
a xuat hien 3lan
c xuat hien 2lan
e xuat hien 2lan
h xuat hien 2lan
t xuat hien 2lan
```

---

**2. Đếm tần suất ký tự bằng map**

Ngoài cách sử dụng mảng đánh dấu bạn có thể sử dụng map, nếu bạn chưa biết cách dùng map thì có thể tham khảo tại blog của mình bài viết về map nhé.

Ý tưởng là mình sẽ dùng một map<char,int> trong đó key của map sẽ lưu ký tự và value sẽ lưu tần suất tương ứng.

Cách này thì ngắn gọn tuy nhiên độ phức tạp tệ hơn so với mảng đánh dấu

Độ phức tạp : O(NlogN)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
#include "map"
using namespace std;

int main(){
	string s = "codelab codelab aaa";
	map<char, int> mp;
	for(int i = 0; i < s.size(); i++){
		mp[s[i]]++;
	}
	for(pair<char, int> it : mp){
		cout << it.first << " xuat hien " << it.second << " lan\n";
	}
}
```

Output :

```cpp
  xuat hien 2 lan
2 xuat hien 2 lan
8 xuat hien 2 lan
a xuat hien 3 lan
c xuat hien 2 lan
e xuat hien 2 lan
h xuat hien 2 lan
t xuat hien 2 lan
```

---

**3. Bài tập áp dụng**

**Bài tập 1** : Đếm số lượng ký tự khác nhau trong xâu

Bài này mình sẽ sử dụng mảng đánh dấu để đánh dấu sự xuất hiện của ký tự trong xâu sau đó đếm số lần xuất hiện của các ký tự khác nhau.

```cpp
#include "iostream"
#include "string"
#include "map"
using namespace std;

int main(){
	string s = "codelab codelab aaa";
	int cnt[256] = {0};
	for(int i = 0; i < s.size(); i++){
		cnt[s[i]] = 1;
	}
	int dem = 0;
	for(int i = 0; i < 256; i++){
		dem += cnt[i];
	}
	cout << "So luong ki tu khac nhau : " << dem << endl;
}
```

Output :

```cpp
So luong ki tu khac nhau : 8
```

**Bài tập 2** : Liệt kê các ký tự trong xâu và tần suất của nó theo thứ tự xuất hiện trong xâu

Trong mục 1 mình đã hướng dẫn các bạn cách duyệt theo thứ tự từ điển abc, nếu yêu cầu duyệt theo thứ tự xuất hiện trong xâu thì bạn duyệt xâu và in ra tần suất tương ứng.

Để tránh việc in 1 ký tự nhiều lần thì bạn sẽ cho tần suất của nó về 0 sau khi đã in trước đó.

```cpp
#include "iostream"
#include "string"
#include "map"
using namespace std;

int main(){
	string s = "codelab codelab aaa";
	int cnt[256] = {0};
	for(int i = 0; i < s.size(); i++){
		cnt[s[i]]++;
	}
	for(int i = 0; i < s.size(); i++){
		if(cnt[s[i]] != 0){
			cout << s[i] << " xuat hien " << cnt[s[i]] << " lan\n";
			//Lan sau gap s[i] se ko in nua
			cnt[s[i]] = 0;
		}
	}
}
```

Output :

```cpp
2 xuat hien 2 lan
8 xuat hien 2 lan
t xuat hien 2 lan
e xuat hien 2 lan
c xuat hien 2 lan
h xuat hien 2 lan
  xuat hien 2 lan
a xuat hien 3 lan
```

**Bài tập 3** : Kiểm tra xâu pangram

Xâu pangram là xâu mà chứa đầy đủ tất cả các chữ cái từ a tới z không phân biệt hoa thường.

```cpp
#include "iostream"
#include "string"
#include "ctype.h"
using namespace std;

int main(){
	string s = "codelabABCDefghijklmnopqrstuvWXYZ";
	int cnt[256] = {0};
	for(int i = 0; i < s.size(); i++){
		cnt[tolower(s[i])]++;
	}
	bool ok = true;
	for(int i = 'a'; i <= 'z'; i++){
		if(cnt[i] == 0){
			ok = false;
			break;
		}
	}
	if(ok) cout << "YES\n";
	else cout << "NO\n";
}
```

Output :

```cpp
YES
```

---

**Video String :**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/09-08-c-bai-toan-tan-suat-ky-tu-trong-xau.md](solutions/09-08-c-bai-toan-tan-suat-ky-tu-trong-xau.md)

**Bài 1.** Đếm tần suất từng chữ cái trong chuỗi bằng mảng 26 phần tử.

**Bài 2.** Đếm tần suất mọi ký tự (kể cả số, dấu) bằng mảng 256 phần tử.

**Bài 3.** Tìm ký tự xuất hiện nhiều nhất và ít nhất trong chuỗi.

**Bài 4.** Tìm ký tự đầu tiên **không lặp lại** trong chuỗi.

**Bài 5.** Tìm ký tự đầu tiên **bị lặp** trong chuỗi.

**Bài 6.** In biểu đồ cột (histogram) tần suất ký tự bằng dấu `*`.

**Bài 7.** Kiểm tra 2 chuỗi có phải đảo chữ (anagram) của nhau không.

**Bài 8.** Kiểm tra chuỗi có phải "pangram" không — chứa đủ 26 chữ cái.

**Bài 9.** Đếm tần suất **từ** trong một đoạn văn (dùng `map<string,int>`).

**Bài 10.** In ra 5 từ xuất hiện nhiều nhất trong đoạn văn.

**Bài 11.** Xoá các ký tự lặp lại, giữ lại lần xuất hiện đầu tiên.

**Bài 12.** Kiểm tra chuỗi có thể sắp xếp lại thành chuỗi đối xứng không.

**Bài 13.** Tìm chuỗi con dài nhất không có ký tự lặp lại.

**Bài 14.** Nén chuỗi kiểu RLE: `"aaabbc"` → `"a3b2c1"`.

**Bài 15.** Viết chương trình phân tích văn bản: số ký tự, số từ, tần suất chữ cái, từ dài nhất, từ phổ biến nhất.
