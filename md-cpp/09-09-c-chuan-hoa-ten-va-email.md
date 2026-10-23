# [C]. Chuẩn Hóa Tên Và Email

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

Nếu bạn chưa học phương pháp tách từ trong chuỗi bằng hàm `strtok` thì bạn có thể tham khảo [tại đây](09-07-c-tach-chuoi-voi-strtok-va-sscanf.md)

**Mã nguồn :** 

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	char name[] = "tran  VAn  TeCH28";
	char res[100] = "";
	char *word = strtok(name, " ");
	while(word != NULL){
		word[0] = (char)toupper((unsigned char)word[0]);
		for(int j = 1; word[j] != '\0'; j++){
			word[j] = (char)tolower((unsigned char)word[j]);
		}
		if(res[0] != '\0') strcat(res, " ");
		strcat(res, word);
		word = strtok(NULL, " ");
	}
	printf("Ten chuan hoa : %s\n", res);
	return 0;
}
```

Output :

```
Ten chuan hoa : Tran Van Tech28
```

**Lưu ý :** `strtok` làm thay đổi chuỗi `name`, vì vậy `name` phải là mảng `char[]` chứ không phải con trỏ tới chuỗi hằng. Mảng `res` phải được khởi tạo rỗng (`""`) trước khi dùng `strcat` và đủ lớn để chứa kết quả.

---

**2. Bài toán chuẩn hóa tên 2**

Bài toán này yêu cần bạn in ra tên trước rồi mới tới họ và đệm

Ví dụ "tran VaN TeCH28" => "Tech28 Tran Van"

Để dễ dàng đưa ra các từ theo thứ tự mong muốn thì bạn nên lưu lại các từ vào trong 1 mảng. Trong C, danh sách các từ có thể lưu bằng **mảng 2 chiều** `char v[100][50]` (tối đa 100 từ, mỗi từ tối đa 49 ký tự), nếu bạn chưa biết mảng 2 chiều có thể tham khảo [tại đây](08-01-c-ly-thuyet-mang-2-chieu.md)

**Mã nguồn :** 

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//Ham nay chuan hoa 1 tu (sua truc tiep tren chuoi)
void convert(char s[]){
	s[0] = (char)toupper((unsigned char)s[0]);
	for(int i = 1; s[i] != '\0'; i++){
		s[i] = (char)tolower((unsigned char)s[i]);
	}
}

int main(){
	char name[] = "tran  VAn  TeCH28";
	char v[100][50];
	int n = 0;
	char *word = strtok(name, " ");
	while(word != NULL){
		strcpy(v[n], word);
		convert(v[n]);
		n++;
		word = strtok(NULL, " ");
	}
	printf("Ten sau khi chuan hoa : ");
	printf("%s ", v[n - 1]);
	for(int i = 0; i < n - 1; i++){
		printf("%s", v[i]);
		if(i != n - 2){
			printf(" ");
		}
	}
	printf("\n");
	return 0;
}
```

Output :

```
Ten sau khi chuan hoa : Tech28 Tran Van
```

Bằng cách lưu từng từ trong tên vào mảng thì bạn có thể chủ động trong việc in ra theo thứ tự mà đề bài yêu cầu. Biến `n` đếm số từ đã lưu, từ cuối cùng (tên) nằm ở `v[n - 1]`.

**3. Bài toán cấp email theo tên**

Bài toán cấp email thường gặp khi bạn cần cung cấp email cho các nhân viên trong 1 công ty hay các sinh viên trong trường đại học dựa trên tên của họ.

Ví dụ tên "Nguyen Van Nam" sẽ được cấp email là "namnv@codelab.dev" chẳng hạn

Tên email được cấp bằng cách lấy tên và ghép với các chữ cái đầu tiên của họ và đệm.

Có nhiều kiểu cấp email khác nhau nhưng bạn có thể làm tương tự kiểu chuẩn email này.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	char name[] = "tran  VAn  loNG";
	for(int i = 0; name[i] != '\0'; i++){
		name[i] = (char)tolower((unsigned char)name[i]);
	}
	char v[100][50];
	int n = 0;
	char *word = strtok(name, " ");
	while(word != NULL){
		strcpy(v[n++], word);
		word = strtok(NULL, " ");
	}
	char email[100];
	strcpy(email, v[n - 1]); // ten
	int len = (int)strlen(email);
	for(int i = 0; i < n - 1; i++){
		email[len++] = v[i][0]; // ki tu dau tien cua ho va dem
	}
	email[len] = '\0';
	strcat(email, "@codelab.dev");
	printf("Email duoc cap : %s\n", email);
	return 0;
}
```

Output :

```
Email duoc cap : longtv@codelab.dev
```

**Giải thích :** Để nối **một ký tự** vào cuối chuỗi, mình ghi ký tự đó vào vị trí `len` (vị trí của `'\0'` hiện tại), tăng `len` rồi đặt lại `'\0'` ở cuối. Hàm `strcat` chỉ nối được **chuỗi** với chuỗi, không nối trực tiếp một ký tự.

---

**Video giải bài tập string :**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/09-09-c-chuan-hoa-ten-va-email.md](solutions/09-09-c-chuan-hoa-ten-va-email.md)

**Bài 1.** Chuẩn hoá họ tên: xoá khoảng trắng thừa, viết hoa chữ cái đầu mỗi từ.

**Bài 2.** Tách họ tên thành 3 phần: họ, tên đệm, tên (lưu vào một `struct`).

**Bài 3.** Sinh email từ họ tên theo mẫu `ten.ho@domain.com`.

**Bài 4.** Kiểm tra email có hợp lệ không (có đúng một `@`, có dấu `.` sau `@`, không có khoảng trắng).

**Bài 5.** Tách email thành phần tên người dùng và tên miền.

**Bài 6.** Chuẩn hoá email: xoá khoảng trắng, chuyển toàn bộ về chữ thường.

**Bài 7.** Sinh tên đăng nhập từ họ tên: `"Nguyen Van An"` → `"annv"`.

**Bài 8.** Che một phần email để bảo mật: `"nguyenvanan@gmail.com"` → `"ngu******an@gmail.com"`.

**Bài 9.** Kiểm tra số điện thoại Việt Nam hợp lệ (10 số, bắt đầu bằng 0).

**Bài 10.** Chuẩn hoá số điện thoại: xoá dấu cách, dấu gạch, đổi `+84` thành `0`.

**Bài 11.** Định dạng số điện thoại thành `0xxx xxx xxx`.

**Bài 12.** Viết chương trình nhập danh sách sinh viên, tự động sinh email không trùng lặp (nếu trùng thì thêm số).

**Bài 13.** Kiểm tra mật khẩu mạnh: ít nhất 8 ký tự, có chữ hoa, chữ thường, chữ số, ký tự đặc biệt.

**Bài 14.** Chuẩn hoá địa chỉ: viết hoa chữ đầu, chuẩn hoá các từ viết tắt (`tp` → `TP`, `q.` → `Quan`).

**Bài 15.** Viết "thư viện chuẩn hoá dữ liệu" (file `.h` và `.c`) gồm: `chuanHoaTen`, `sinhEmail`, `kiemTraEmail`, `chuanHoaSDT`, `kiemTraMatKhau`.
