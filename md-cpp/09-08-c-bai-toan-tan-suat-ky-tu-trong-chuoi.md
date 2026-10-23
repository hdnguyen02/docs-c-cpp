# [C]. Bài Toán Tần Suất Ký Tự Trong Chuỗi

Đếm tần suất ký tự trong chuỗi và các bài toán liên quan tới sự xuất hiện của ký tự trong chuỗi các bạn có thể sử dụng mảng đánh dấu (mảng đếm). Trong bài viết này mình sẽ hướng dẫn các bạn dạng bài tập này và một vài bài tập ví dụ minh họa

**NỘI DUNG :** 

- **Đếm tần suất ký tự bằng mảng đánh dấu 256 phần tử**
- **Đếm tần suất chữ cái bằng mảng 26 phần tử**
- **Bài tập áp dụng**
- **Video tutorial** 

---

**1. Đếm tần suất ký tự bằng mảng đánh dấu 256 phần tử**

Để đếm xem mỗi ký tự trong chuỗi xuất hiện bao nhiêu lần bạn có thể sử dụng kỹ thuật mảng đánh dấu, nếu bạn chưa biết kỹ thuật này có thể tham khảo [tại đây](06-06-c-mang-danh-dau.md)

Ý tưởng là mình sẽ sử dụng mã ASCII của các ký tự để đếm tần suất tương ứng của ký tự đó, mỗi ký tự trong C chiếm 1 byte nên có mã từ 0 tới 255, vì vậy bạn chỉ cần sử dụng một mảng đánh dấu có 256 phần tử là có thể đếm được tần suất.

Ví dụ khi gặp kí tự 'a' trong chuỗi ký tự thì bạn sẽ đếm tần suất của nó thông qua phần tử có chỉ số 97 của mảng đánh dấu, vì 'a' có mã ASCII là 97

Sau khi bạn tìm được tần suất của từng ký tự bạn có thể triển khai nhiều bài toán mở rộng khác.

Độ phức tạp : O(N)

**Mã nguồn :** 

```c
#include <stdio.h>

int main(){
	char s[] = "codelab codelab aaa";
	int cnt[256] = {0};
	for(int i = 0; s[i] != '\0'; i++){
		cnt[(unsigned char)s[i]]++;
	}
	for(int i = 0; i < 256; i++){
		if(cnt[i] != 0){
			printf("%c xuat hien %d lan\n", i, cnt[i]);
		}
	}
	return 0;
}
```

Output :

```
  xuat hien 2 lan
a xuat hien 5 lan
b xuat hien 2 lan
c xuat hien 2 lan
d xuat hien 2 lan
e xuat hien 2 lan
l xuat hien 2 lan
o xuat hien 2 lan
```

**Lưu ý :** Kiểu `char` trong C có thể là kiểu **có dấu** (−128..127) tùy trình biên dịch. Với các ký tự có mã lớn hơn 127 (ví dụ chữ tiếng Việt có dấu), `s[i]` sẽ mang giá trị âm và `cnt[s[i]]` truy cập **ra ngoài mảng**. Vì vậy luôn ép kiểu `(unsigned char)s[i]` trước khi dùng làm chỉ số.

Vì duyệt mảng `cnt` theo chỉ số từ 0 tới 255, các ký tự được in ra theo **thứ tự mã ASCII** (dấu cách có mã 32 đứng trước, rồi tới các chữ cái).

---

**2. Đếm tần suất chữ cái bằng mảng 26 phần tử**

Nếu đề bài chỉ quan tâm tới các chữ cái (thường gặp nhất là chữ cái thường từ a tới z), bạn có thể dùng mảng đếm chỉ gồm **26 phần tử**, chỉ số `0` ứng với `'a'`, chỉ số `1` ứng với `'b'`, ..., chỉ số `25` ứng với `'z'`.

Công thức ánh xạ là `s[i] - 'a'`, ví dụ `'c' - 'a'` = 99 − 97 = 2. Khi in ra thì làm ngược lại: chỉ số `i` ứng với ký tự `'a' + i`.

Độ phức tạp : O(N)

**Mã nguồn :** 

```c
#include <stdio.h>

int main(){
	char s[] = "codelab codelab aaa";
	int cnt[26] = {0};
	for(int i = 0; s[i] != '\0'; i++){
		if(s[i] >= 'a' && s[i] <= 'z'){
			cnt[s[i] - 'a']++;
		}
	}
	for(int i = 0; i < 26; i++){
		if(cnt[i] != 0){
			printf("%c xuat hien %d lan\n", 'a' + i, cnt[i]);
		}
	}
	return 0;
}
```

Output :

```
a xuat hien 5 lan
b xuat hien 2 lan
c xuat hien 2 lan
d xuat hien 2 lan
e xuat hien 2 lan
l xuat hien 2 lan
o xuat hien 2 lan
```

Cách này tiết kiệm bộ nhớ hơn và bỏ qua được các ký tự không phải chữ cái, nhưng **bắt buộc** phải kiểm tra ký tự nằm trong đoạn `'a'`..`'z'` trước khi tăng biến đếm, nếu không chỉ số `s[i] - 'a'` sẽ âm hoặc vượt quá 25. Nếu muốn đếm không phân biệt hoa thường thì chuyển ký tự về chữ thường bằng `tolower()` trước.

---

**3. Bài tập áp dụng**

**Bài tập 1** : Đếm số lượng ký tự khác nhau trong chuỗi

Bài này mình sẽ sử dụng mảng đánh dấu để đánh dấu sự xuất hiện của ký tự trong chuỗi sau đó đếm số lần xuất hiện của các ký tự khác nhau.

```c
#include <stdio.h>

int main(){
	char s[] = "codelab codelab aaa";
	int cnt[256] = {0};
	for(int i = 0; s[i] != '\0'; i++){
		cnt[(unsigned char)s[i]] = 1;
	}
	int dem = 0;
	for(int i = 0; i < 256; i++){
		dem += cnt[i];
	}
	printf("So luong ki tu khac nhau : %d\n", dem);
	return 0;
}
```

Output :

```
So luong ki tu khac nhau : 8
```

**Bài tập 2** : Liệt kê các ký tự trong chuỗi và tần suất của nó theo thứ tự xuất hiện trong chuỗi

Trong mục 1 mình đã hướng dẫn các bạn cách duyệt theo thứ tự mã ASCII, nếu yêu cầu duyệt theo thứ tự xuất hiện trong chuỗi thì bạn duyệt chuỗi và in ra tần suất tương ứng.

Để tránh việc in 1 ký tự nhiều lần thì bạn sẽ cho tần suất của nó về 0 sau khi đã in trước đó.

```c
#include <stdio.h>

int main(){
	char s[] = "codelab codelab aaa";
	int cnt[256] = {0};
	for(int i = 0; s[i] != '\0'; i++){
		cnt[(unsigned char)s[i]]++;
	}
	for(int i = 0; s[i] != '\0'; i++){
		unsigned char c = (unsigned char)s[i];
		if(cnt[c] != 0){
			printf("%c xuat hien %d lan\n", s[i], cnt[c]);
			//Lan sau gap s[i] se ko in nua
			cnt[c] = 0;
		}
	}
	return 0;
}
```

Output :

```
c xuat hien 2 lan
o xuat hien 2 lan
d xuat hien 2 lan
e xuat hien 2 lan
l xuat hien 2 lan
a xuat hien 5 lan
b xuat hien 2 lan
  xuat hien 2 lan
```

**Bài tập 3** : Kiểm tra chuỗi pangram

Chuỗi pangram là chuỗi mà chứa đầy đủ tất cả các chữ cái từ a tới z không phân biệt hoa thường.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int main(){
	char s[] = "codelabABCDefghijklmnopqrstuvWXYZ";
	int cnt[256] = {0};
	for(int i = 0; s[i] != '\0'; i++){
		cnt[tolower((unsigned char)s[i])]++;
	}
	bool ok = true;
	for(int i = 'a'; i <= 'z'; i++){
		if(cnt[i] == 0){
			ok = false;
			break;
		}
	}
	if(ok) printf("YES\n");
	else printf("NO\n");
	return 0;
}
```

Output :

```
YES
```

---

**Video String :**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/09-08-c-bai-toan-tan-suat-ky-tu-trong-chuoi.md](solutions/09-08-c-bai-toan-tan-suat-ky-tu-trong-chuoi.md)

**Bài 1.** Đếm tần suất từng chữ cái trong chuỗi bằng mảng 26 phần tử.

**Bài 2.** Đếm tần suất mọi ký tự (kể cả số, dấu) bằng mảng 256 phần tử.

**Bài 3.** Tìm ký tự xuất hiện nhiều nhất và ít nhất trong chuỗi.

**Bài 4.** Tìm ký tự đầu tiên **không lặp lại** trong chuỗi.

**Bài 5.** Tìm ký tự đầu tiên **bị lặp** trong chuỗi.

**Bài 6.** In biểu đồ cột (histogram) tần suất ký tự bằng dấu `*`.

**Bài 7.** Kiểm tra 2 chuỗi có phải đảo chữ (anagram) của nhau không.

**Bài 8.** Kiểm tra chuỗi có phải "pangram" không — chứa đủ 26 chữ cái.

**Bài 9.** Đếm tần suất **từ** trong một đoạn văn (dùng mảng `struct` gồm từ và số lần xuất hiện).

**Bài 10.** In ra 5 từ xuất hiện nhiều nhất trong đoạn văn (sắp xếp bằng `qsort`).

**Bài 11.** Xoá các ký tự lặp lại, giữ lại lần xuất hiện đầu tiên.

**Bài 12.** Kiểm tra chuỗi có thể sắp xếp lại thành chuỗi đối xứng không.

**Bài 13.** Tìm chuỗi con dài nhất không có ký tự lặp lại.

**Bài 14.** Nén chuỗi kiểu RLE: `"aaabbc"` → `"a3b2c1"`.

**Bài 15.** Viết chương trình phân tích văn bản: số ký tự, số từ, tần suất chữ cái, từ dài nhất, từ phổ biến nhất.
