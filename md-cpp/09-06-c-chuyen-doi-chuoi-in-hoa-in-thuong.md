# [C]. Chuyển Đổi Chuỗi In Hoa, In Thường

Chuyển đổi chuỗi ký tự thành in hoa hoặc in thường là một công việc thường gặp khi làm việc với chuỗi ký tự, bài viết này mình sẽ hướng dẫn các bạn các cách phổ biến để chuyển 1 chuỗi ký tự thành dạng in thường hoặc in hoa trong C.

**NỘI DUNG :** 

- **Cài Đặt Hàm Chuyển Đổi Hoa Thường**
- **Chuyển Đổi Hoa Thường Bằng Con Trỏ**
- **Video Tutorial**

---

**1.Cài Đặt Hàm Chuyển Đổi Hoa Thường**

Để tự cài đặt hàm chuyển đổi in hoa, in thường bạn cần sử dụng các hàm chuyển đổi loại ký tự như **tolower()**, **toupper()** trong thư viện **ctype.h** hoặc tự viết các câu lệnh để chuyển đổi.

Bạn có thể ôn lại các hàm kiểm tra loại ký tự trong C [tại đây](03-04-c-bang-ma-ascii-va-thu-vien-ctypeh.md)

**Lưu ý** : Trong C, chuỗi là mảng `char` kết thúc bằng ký tự `'\0'`. Khi truyền mảng vào hàm, hàm nhận được **con trỏ** tới phần tử đầu tiên, vì vậy mọi thay đổi trong hàm sẽ tác động trực tiếp lên chuỗi gốc — C không có kiểu tham chiếu, mảng luôn được truyền qua con trỏ.

**Mã nguồn 1:** 

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void to_lower(char s[]){
	for(size_t i = 0; i < strlen(s); i++){
		s[i] = (char)tolower((unsigned char)s[i]);
	}
}

void to_upper(char s[]){
	for(size_t i = 0; i < strlen(s); i++){
		s[i] = (char)toupper((unsigned char)s[i]);
	}
}

int main(){
	char s[] = "codelab BLOG";
	to_lower(s);
	printf("%s\n", s);
	to_upper(s);
	printf("%s\n", s);
	return 0;
}
```

Output :

```
codelab blog
CODELAB BLOG
```

**Chú ý :**

- Phải khai báo `char s[] = "..."` (mảng có thể sửa) chứ **không** dùng `char *s = "..."`. Chuỗi hằng (string literal) nằm ở vùng nhớ chỉ đọc, sửa nó là hành vi không xác định (thường làm chương trình bị crash).
- Ép `(unsigned char)` trước khi truyền vào `tolower`/`toupper` để tránh lỗi với ký tự có mã âm.
- Gọi `strlen(s)` trong điều kiện vòng lặp sẽ tính lại độ dài ở mỗi bước. Với chuỗi dài, nên lưu `size_t n = strlen(s);` trước vòng lặp, hoặc duyệt tới khi gặp `'\0'`: `for(int i = 0; s[i] != '\0'; i++)`.

Trong C, hàm không thể trả về cả một mảng. Nếu muốn **giữ nguyên chuỗi gốc** và lấy kết quả ở chuỗi khác, bạn truyền thêm một mảng đích để hàm ghi kết quả vào. Ở cách này mình tự chuyển đổi bằng mã ASCII: chữ hoa và chữ thường tương ứng lệch nhau đúng **32** đơn vị (`'A'` = 65, `'a'` = 97).

**Mã nguồn 2 :**

```c
#include <stdio.h>

// Ghi ban in thuong cua src vao dst (dst phai du cho)
void to_lower(const char src[], char dst[]){
	int i = 0;
	for(; src[i] != '\0'; i++){
		dst[i] = src[i];
		if(src[i] >= 'A' && src[i] <= 'Z'){
			dst[i] += 32;
		}
	}
	dst[i] = '\0';
}

void to_upper(const char src[], char dst[]){
	int i = 0;
	for(; src[i] != '\0'; i++){
		dst[i] = src[i];
		if(src[i] >= 'a' && src[i] <= 'z'){
			dst[i] -= 32;
		}
	}
	dst[i] = '\0';
}

int main(){
	char s[] = "codelab BLOG";
	char kq[100];
	to_lower(s, kq);
	printf("%s\n", kq);
	to_upper(s, kq);
	printf("%s\n", kq);
	printf("%s\n", s);    // chuoi goc khong doi
	return 0;
}
```

Output :

```
codelab blog
CODELAB BLOG
codelab BLOG
```

**Lưu ý** : Đừng quên đặt ký tự kết thúc `'\0'` vào cuối chuỗi đích, nếu không `printf` sẽ in tràn ra các byte rác phía sau.

---

**2. Chuyển Đổi Hoa Thường Bằng Con Trỏ**

C không có hàm chuẩn nào chuyển cả chuỗi thành in hoa hoặc in thường. Một số trình biên dịch (như MSVC) có hàm `strupr()`, `strlwr()` nhưng đây **không phải** hàm chuẩn C, dùng với GCC sẽ báo lỗi, vì vậy bạn nên tự viết.

Cách viết gọn và phổ biến trong C là dùng một **con trỏ** chạy dọc chuỗi, đổi từng ký tự cho tới khi gặp `'\0'`.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <ctype.h>

int main(){
	char s[] = "codelab BLOG strING";
	for(char *p = s; *p != '\0'; p++)
		*p = (char)tolower((unsigned char)*p);
	printf("Lowercase : %s\n", s);
	for(char *p = s; *p != '\0'; p++)
		*p = (char)toupper((unsigned char)*p);
	printf("Uppercase : %s\n", s);
	return 0;
}
```

Output :

```
Lowercase : codelab blog string
Uppercase : CODELAB BLOG STRING
```

Bạn có thể đóng gói vòng lặp con trỏ thành hàm và cho hàm **trả về chính con trỏ tới chuỗi** — giống cách các hàm `strcpy`, `strcat` của `string.h` hoạt động — để có thể dùng ngay trong `printf`.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <ctype.h>

char *str_lower(char *s){
	for(char *p = s; *p; p++)
		*p = (char)tolower((unsigned char)*p);
	return s;
}

char *str_upper(char *s){
	for(char *p = s; *p; p++)
		*p = (char)toupper((unsigned char)*p);
	return s;
}

int main(){
	char s[] = "codelab BLOG strING";
	printf("Lowercase : %s\n", str_lower(s));
	printf("Uppercase : %s\n", str_upper(s));
	return 0;
}
```

Output :

```
Lowercase : codelab blog string
Uppercase : CODELAB BLOG STRING
```

**Giải thích :** Điều kiện `*p` tương đương `*p != '\0'`, vì ký tự `'\0'` có giá trị 0 (sai). Hàm sửa chuỗi tại chỗ rồi trả về địa chỉ đầu chuỗi, nên `printf` in được ngay kết quả.

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-06-c-chuyen-doi-chuoi-in-hoa-in-thuong.md](solutions/09-06-c-chuyen-doi-chuoi-in-hoa-in-thuong.md)

**Bài 1.** Chuyển toàn bộ chuỗi sang chữ hoa bằng vòng lặp và `toupper()`.

**Bài 2.** Chuyển toàn bộ chuỗi sang chữ thường bằng con trỏ duyệt tới `'\0'`, ghi kết quả vào một mảng khác (không sửa chuỗi gốc).

**Bài 3.** Chuyển hoa ↔ thường bằng phép toán `±32` với mã ASCII, không dùng thư viện.

**Bài 4.** Đảo hoa/thường: chữ hoa thành thường và ngược lại.

**Bài 5.** Viết hoa chữ cái đầu của mỗi từ trong câu (Title Case).

**Bài 6.** Viết hoa chữ cái đầu câu, còn lại viết thường (Sentence case).

**Bài 7.** Chuyển chuỗi sang định dạng `camelCase`: `"lap trinh c co ban"` → `"lapTrinhCCoBan"`.

**Bài 8.** Chuyển chuỗi sang `snake_case` và `kebab-case`.

**Bài 9.** Đếm số chữ hoa, chữ thường trong chuỗi.

**Bài 10.** Kiểm tra chuỗi có toàn chữ hoa / toàn chữ thường không.

**Bài 11.** Chuyển đổi chỉ các chữ cái ở vị trí chẵn thành hoa.

**Bài 12.** Giải thích vì sao `toupper` trả về `int` chứ không phải `char`. Viết ví dụ minh hoạ lỗi nếu in kết quả bằng `%d` thay vì `%c`.

**Bài 13.** Chuyển hoa/thường cho chuỗi có ký tự đặc biệt và chữ số — kiểm tra kết quả không bị hỏng.

**Bài 14.** So sánh tốc độ 3 cách chuyển hoa: vòng lặp chỉ số + `toupper`, con trỏ + `toupper`, và phép bit `& ~32`.

**Bài 15.** Viết chương trình chuẩn hoá tên người: `"  nGuYen   vAN   an  "` → `"Nguyen Van An"`.
