# [C++]. So Sánh Xâu Ký Tự Theo Thứ Tự Từ Điển

Thứ tự từ điển là một kiến thức quan trọng khi học về xâu ký tự, bài viết này mình sẽ hướng dẫn các bạn cách xác định thứ tự từ điển giữa các xâu ký tự cũng như các hàm và toán tử trong string đã cung cấp sẵn

**NỘI DUNG :** 

- **Thứ Tự Từ Điển (Lexicographically) Là Gì ?** 
- **Toán Tử So Sánh String Và Hàm Compare()**
- **Video Tutorial** 

---

**1. Thứ Tự Từ Điển (Lexicographically) Là Gì ?** 

Thứ tự từ điển của xâu ký tự hiểu đơn giản là thứ tự abc trong bảng chữ cái, trong đó ký tự nào đứng trước trong bảng chữ cái sẽ có thứ tự từ điển nhỏ hơn.

Đối với chuỗi ký tự thì thứ tự từ điển của nó so với chuỗi ký tự khác được xác định bằng ký tự khác nhau đầu tiên của 2 xâu.

**Quy tắc so sánh 2 xâu theo thứ tự từ điển :** 

- Nếu 2 xâu có cùng độ dài và giống nhau mọi ký tự thì bằng nhau, ví dụ "codelab" và "codelab"
- Nếu 2 xâu khác nhau thì ký tự đầu tiên khác nhau của 2 xâu sẽ quy định xâu nào có từ điển lớn hơn, nhỏ hơn. Ví dụ "codelabzabc" và "codelabaz" thì chữ thứ 7 của 2 xâu này khác nhau và 'z' lớn hơn 'a' theo từ điển nên xâu "codelabzabc" lớn hơn "codelabaz" về mặt từ điển
- Nếu 2 xâu không có ký tự khác nhau đầu tiên thì xâu nào dài hơn sẽ có từ điển lớn hơn, ví dụ "codelab" và "codelabblog" thì "codelabblog" có từ điển lớn hơn
- Chữ cái in hoa và in thường có thứ tự từ điển khác nhau và thứ tự từ điển của ký tự được quy định bởi mã ASCII

Một vài ví dụ về thứ tự từ điển của 2 xâu ký tự :

1. "codelab" > "codelabzzz"
2. "1234" > "zzz"
3. "lan" < "lan di hoc lap trinh"
4. "codelab" > "27tech"
5. "codelab java" < "codelab@"

---

**2.Toán Tử So Sánh String Và Hàm Compare()**

Để so sánh 2 xâu trong C++ bạn có thể sử dụng luôn các toán tử so sánh như >, <, !=, ==...

Ngoài ra bạn có thể sử dụng hàm **compare()** hoặc tự cài đặt hàm này cho mình.

Ví dụ :

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
	cout << boolalpha << ("codelab" == "codelab") << endl;
	cout << boolalpha << ("codelab" != "codelab") << endl;
	cout << boolalpha << ("codelababc" < "codelabza") << endl;
	cout << boolalpha << ("codelab" < "codelab") << endl;
	cout << boolalpha << ("codelab" < "28@tech") << endl;
	return 0;
}
```

Output :

```cpp
true
false
true
true
true
```

Hàm **compare()** trong C++ được sử dụng để so sánh 2 xâu, hàm này sẽ trả về số nhỏ hơn, lớn hơn hoặc bằng 0 tùy vào từ điển của 2 xâu sử dụng. Khi hàm này trả về 0 nghĩa là 2 xâu này giống nhau.

Ví dụ :

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
	string s = "codelab", t = "codelab", p = "codelab";
	cout << s.compare(p) << endl;
	cout << s.compare(t) << endl;
	cout << t.compare(p) << endl;
	return 0;
}
```

Output :

```cpp
0
1
-1
```

Ngoài ra bạn cũng có thể tự cài đặt hàm này như là bài tập rèn luyện.

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-05-c-so-sanh-xau-ky-tu-theo-thu-tu-tu-dien.md](solutions/09-05-c-so-sanh-xau-ky-tu-theo-thu-tu-tu-dien.md)

**Bài 1.** So sánh 2 chuỗi nhập từ bàn phím bằng các toán tử `<`, `>`, `==` và in kết quả.

**Bài 2.** Giải thích vì sao `"Apple" < "apple"` trả về `true`. Chứng minh bằng mã ASCII.

**Bài 3.** Viết hàm so sánh 2 chuỗi **không phân biệt hoa thường**.

**Bài 4.** Nhập `n` chuỗi, sắp xếp chúng theo thứ tự từ điển tăng dần.

**Bài 5.** Sắp xếp danh sách tên không phân biệt hoa thường.

**Bài 6.** Tìm chuỗi lớn nhất và nhỏ nhất theo thứ tự từ điển trong một mảng.

**Bài 7.** So sánh `"abc"` với `"abcd"`, `"10"` với `"9"`, `"Z"` với `"a"`. Dự đoán rồi kiểm chứng.

**Bài 8.** Viết hàm so sánh tự cài đặt (không dùng toán tử `<`), trả về −1, 0, 1.

**Bài 9.** Sắp xếp danh sách tên theo **tên** (từ cuối cùng) thay vì theo họ.

**Bài 10.** Sắp xếp các chuỗi số `"10"`, `"9"`, `"100"` theo giá trị số thay vì theo từ điển.

**Bài 11.** Viết hàm so sánh "tự nhiên" (natural sort): `"file2"` đứng trước `"file10"`.

**Bài 12.** Kiểm tra một danh sách đã được sắp xếp theo thứ tự từ điển chưa.

**Bài 13.** Tìm tiền tố chung dài nhất của một mảng chuỗi.

**Bài 14.** Sắp xếp danh sách theo độ dài chuỗi, nếu bằng nhau thì theo từ điển.

**Bài 15.** Viết chương trình tra từ điển đơn giản: sắp xếp danh sách từ, tìm kiếm nhị phân theo thứ tự từ điển.
