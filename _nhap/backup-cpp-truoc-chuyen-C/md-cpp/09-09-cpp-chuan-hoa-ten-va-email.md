# [C++]. Chuẩn Hóa Tên Và Email

Chuẩn hóa tên là một công việc thường gặp khi xử lý chuỗi, trong bài viết này mình sẽ hướng dẫn các bạn phương pháp để bạn có thể chuẩn hóa tên theo nhiều yêu cầu khác nhau

**NỘI DUNG :** 

- **Bài toán chuẩn hóa tên 1**
- **Bài toán chuẩn hóa tên 2**
- **Bài toán cấp email theo tên**
- **Video tutorial** 

---

**1. Bài toán chuẩn hóa tên 1**

Bài toán này sẽ yêu cầu bạn chuẩn hóa tên bằng cách loại bỏ dấu cách thừa giữa các từ và viết hoa chữ cái đầu của từng từ.

Ví dụ " nguYEN Thuy linH" => "Nguyen Thuy Linh"

Phương pháp làm những bài toán chuẩn hóa tên đó là bạn nên tách từng từ ra sau đó xử lý từng từ và gộp lại

Nếu bạn chưa học phương pháp tách từ trong xâu thì bạn có thể tham khảo [tại đây](https://blog.codelab.dev/c-ham-strtok)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
#include "ctype.h"
#include "sstream"

using namespace std;

int main(){
	string name = "tran  VAn  TeCH28";
	stringstream ss(name);
	string res = "", word;
	while(ss >> word){
		res += toupper(word[0]);
		for(int j = 1; j < word.size(); j++){
			res += tolower(word[j]);
		}
		res += " ";
	}
	res.pop_back();
	cout << "Ten chuan hoa : " << res << endl;
}
```

Output :

```cpp
Ten chuan hoa : Tran Van Tech28
```

---

**2. Bài toán chuẩn hóa tên 2**

Bài toán này yêu cần bạn in ra tên trước rồi mới tới họ và đệm

Ví dụ "tran VaN TeCH28" => "Tech28 Tran Van"

Để dễ dàng đưa ra các từ theo thứ tự mong muốn thì bạn nên lưu lại các từ vào trong 1 vector hoặc mảng, nếu bạn chưa biết vector có thể tham khảo [tại đây](https://blog.codelab.dev/stl-vector-trong-c)

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
#include "ctype.h"
#include "sstream"
#include "vector"

using namespace std;

//Ham nay chuan hoa 1 tu 
string convert(string s){
	s[0] = toupper(s[0]);
	for(int i = 1; i < s.size(); i++){
		s[i] = tolower(s[i]);
	}
	return s;
}

int main(){
	string name = "tran  VAn  TeCH28";
	stringstream ss(name);
	vector<string> v;
	string word;
	while(ss >> word){
		v.push_back(convert(word));
	}
	cout << "Ten sau khi chuan hoa : ";
	cout << v[v.size() - 1] << " ";
	for(int i = 0; i < v.size() - 1; i++){
		cout << v[i];
		if(i != v.size() - 2){
			cout << " ";
		}
	}
}
```

Output :

```cpp
Ten sau khi chuan hoa : Tech28 Tran Van
```

Bằng cách lưu từng từ trong tên vào vector hoặc mảng thì bạn có thể chủ động trong việc in ra theo thứ tự mà đề bài yêu cầu.

**3. Bài toán cấp email theo tên**

Bài toán cấp email thường gặp khi bạn cần cung cấp email cho các nhân viên trong 1 công ty hay các sinh viên trong trường đại học dựa trên tên của họ.

Ví dụ tên "Nguyen Van Nam" sẽ được cấp email là "namnv@codelab.dev" chẳng hạn

Tên email được cấp bằng cách lấy tên và ghép với các chữ cái đầu tiên của họ và đệm.

Có nhiều kiểu cấp email khác nhau nhưng bạn có thể làm tương tự kiểu chuẩn email này.

**Mã nguồn :** 

```cpp
#include "iostream"
#include "string"
#include "ctype.h"
#include "sstream"
#include "vector"

using namespace std;

int main(){
	string name = "tran  VAn  loNG";
	for(int i = 0; i < name.size(); i++){
		name[i] = tolower(name[i]);
	}
	stringstream ss(name);
	vector<string> v;
	string word;
	while(ss >> word){
		v.push_back(word);
	}
	string email = v[v.size() - 1]; // ten
	for(int i = 0; i < v.size() - 1; i++){
		email += v[i][0]; // ki tu dau tien cua ho va dem
	}
	email += "@codelab.dev";
	cout << "Email duoc cap : " << email << endl;
}
```

Output :

```cpp
Email duoc cap : longtv@codelab.dev
```

---

**Video giải bài tập string :**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/09-09-cpp-chuan-hoa-ten-va-email.md](solutions/09-09-cpp-chuan-hoa-ten-va-email.md)

**Bài 1.** Chuẩn hoá họ tên: xoá khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ.

**Bài 2.** Tách họ tên thành 3 phần: họ, tên đệm, tên.

**Bài 3.** Sinh email từ họ tên theo mẫu `ten.ho@domain.com`.

**Bài 4.** Kiểm tra email có hợp lệ không (có đúng một `@`, có dấu `.` sau `@`, không có khoảng trắng).

**Bài 5.** Tách email thành phần tên người dùng và tên miền.

**Bài 6.** Chuẩn hoá email: xoá khoảng trắng, chuyển toàn bộ về chữ thường.

**Bài 7.** Sinh tên đăng nhập từ họ tên: `"Nguyen Van An"` → `"annv"`.

**Bài 8.** Che một phần email để bảo mật: `"nguyenvanan@gmail.com"` → `"ngu*******an@gmail.com"`.

**Bài 9.** Kiểm tra số điện thoại Việt Nam hợp lệ (10 số, bắt đầu bằng 0).

**Bài 10.** Chuẩn hoá số điện thoại: xoá dấu cách, dấu gạch, đổi `+84` thành `0`.

**Bài 11.** Định dạng số điện thoại thành `0xxx xxx xxx`.

**Bài 12.** Viết chương trình nhập danh sách sinh viên, tự động sinh email không trùng lặp (nếu trùng thì thêm số).

**Bài 13.** Kiểm tra mật khẩu mạnh: ít nhất 8 ký tự, có chữ hoa, chữ thường, chữ số, ký tự đặc biệt.

**Bài 14.** Chuẩn hoá địa chỉ: viết hoa chữ đầu, chuẩn hoá các từ viết tắt (`tp` → `TP`, `q.` → `Quan`).

**Bài 15.** Viết "thư viện chuẩn hoá dữ liệu" gồm: `chuanHoaTen`, `sinhEmail`, `kiemTraEmail`, `chuanHoaSDT`, `kiemTraMatKhau`.
