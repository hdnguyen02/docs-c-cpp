# [C++]. Chuyển Đổi Xâu Ký Tự In Hoa, In Thường

Chuyển đổi xâu ký tự thành in hoa hoặc in thường là một công việc thường gặp khi làm việc với xâu ký tự, bài viết này mình sẽ hướng dẫn các bạn các cách phổ biến để chuyển 1 xâu ký tự thành dạng in thường hoặc in hoa.

**NỘI DUNG :** 

- **Cài Đặt Hàm Chuyển Đổi Hoa Thường**
- **Chuyển Đổi Hoa Thường Bằng Hàm transform()**
- **Video Tutorial**

---

**1.Cài Đặt Hàm Chuyển Đổi Hoa Thường**

Để tự cài đặt hàm chuyển đổi in hoa, in thường bạn cần sử dụng các hàm chuyển đổi loại ký tự như **tolower()**,** toupper()** hoặc tự viết các câu lệnh để chuyển đổi.

Bạn có thể ôn lại các hàm kiểm tra loại ký tự trong C/C++ [tại đây](https://blog.codelab.dev/c-cac-ham-kiem-tra-loai-ky-tu)

**Lưu ý** : Nếu bạn muốn thay đổi string thông qua hàm bạn cần sử dụng tham chiếu.

**Mã nguồn 1:** 

```cpp
#include "iostream"
#include "string"
#include "ctype.h"

using namespace std;

void to_lower(string &s){
	for(int i = 0; i < s.size(); i++){
		s[i] = tolower(s[i]);
	}
}

void to_upper(string &s){
	for(int i = 0; i < s.size(); i++){
		s[i] = toupper(s[i]);
	}
}

int main(){
	string s = "codelab BLOG";
	to_lower(s);
	cout << s << endl;
	to_upper(s);
	cout << s << endl;
}
```

Output :

```cpp
codelab blog
CODELAB BLOG
```

Bạn cũng có thể viết hàm để trả về string ở dạng in thường hoặc in hoa.

**Mã nguồn 2 :**

```cpp
#include "iostream"
#include "string"
#include "ctype.h"

using namespace std;

string to_lower(string s){
	for(int i = 0; i < s.size(); i++){
		if(s[i] >= 'A' && s[i] <= 'Z'){
			s[i] += 32;
		}
	}
	return s;
}

string to_upper(string s){
	for(int i = 0; i < s.size(); i++){
		if(s[i] >= 'a' && s[i] <= 'z'){
			s[i] -= 32;
		}
	}
	return s;
}

int main(){
	string s = "codelab BLOG";
	cout << to_lower(s) << endl;
	cout << to_upper(s) << endl;
}
```

Output :

```cpp
codelab blog
CODELAB BLOG
```

---

**2. Chuyển Đổi Hoa Thường Bằng Hàm transform()**

Trong C++ thì bạn có thể sử dụng hàm có sẵn transform() để chuyển đổi xâu thành in hoa hoặc in thường.

Tuy nhiên cú pháp của nó hơi dài dòng và khó nhớ, thông thường mình sẽ dùng range-based for loop và hàm toupper(), tolower() để chuyển xâu thành in hoa hoặc in thường.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
#include "algorithm"

using namespace std;

int main(){
	string s = "codelab BLOG strING";
	transform(s.begin(), s.end(), s.begin(), ::tolower);
	cout << "Lowercase : " << s << endl;
	transform(s.begin(), s.end(), s.begin(), ::toupper);
	cout << "Uppercase : " << s << endl;
}
```

Output :

```cpp
Lowercase : codelab blog string
Uppercase : CODELAB BLOG STRING
```

Chuyển đổi xâu thành in hoa, in thường bằng range-based for loop kết hợp tham chiếu

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
#include "algorithm"

using namespace std;

int main(){
	string s = "codelab BLOG strING";
	for(char &x : s) 
		x = tolower(x);
	cout << "Lowercase : " << s << endl;
	for(char &x : s)
		x = toupper(x);
	cout << "Uppercase : " << s << endl;
}
```

Output :

```cpp
Lowercase : codelab blog string
Uppercase : CODELAB BLOG STRING
```

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-06-c-chuyen-doi-xau-ky-tu-in-hoa-in-thuong.md](solutions/09-06-c-chuyen-doi-xau-ky-tu-in-hoa-in-thuong.md)

**Bài 1.** Chuyển toàn bộ chuỗi sang chữ hoa bằng vòng lặp và `toupper()`.

**Bài 2.** Chuyển toàn bộ chuỗi sang chữ thường bằng `transform()` của `<algorithm>`.

**Bài 3.** Chuyển hoa ↔ thường bằng phép toán `±32` với mã ASCII, không dùng thư viện.

**Bài 4.** Đảo hoa/thường: chữ hoa thành thường và ngược lại.

**Bài 5.** Viết hoa chữ cái đầu của mỗi từ trong câu (Title Case).

**Bài 6.** Viết hoa chữ cái đầu câu, còn lại viết thường (Sentence case).

**Bài 7.** Chuyển chuỗi sang định dạng `camelCase`: `"lap trinh c++"` → `"lapTrinhC++"`.

**Bài 8.** Chuyển chuỗi sang `snake_case` và `kebab-case`.

**Bài 9.** Đếm số chữ hoa, chữ thường trong chuỗi.

**Bài 10.** Kiểm tra chuỗi có toàn chữ hoa / toàn chữ thường không.

**Bài 11.** Chuyển đổi chỉ các chữ cái ở vị trí chẵn thành hoa.

**Bài 12.** Giải thích vì sao `toupper` trả về `int` chứ không phải `char`. Viết ví dụ minh hoạ lỗi nếu quên ép kiểu.

**Bài 13.** Chuyển hoa/thường cho chuỗi có ký tự đặc biệt và chữ số — kiểm tra kết quả không bị hỏng.

**Bài 14.** So sánh tốc độ 3 cách chuyển hoa: vòng lặp + `toupper`, `transform`, và phép bit `& ~32`.

**Bài 15.** Viết chương trình chuẩn hoá tên người: `"  nGuYen   vAN   an  "` → `"Nguyen Van An"`.
