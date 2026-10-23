# [C]. Tách Chuỗi Với strtok Và sscanf

**strtok** và **sscanf** là hai công cụ rất hữu ích trong C với các bài toán xử lý chuỗi ký tự: `strtok` giúp tách chuỗi thành các từ theo ký tự phân cách, còn `sscanf` giúp đọc số và dữ liệu có định dạng ra khỏi một chuỗi. Bài học này mình sẽ hướng dẫn các bạn cách sử dụng hai hàm này để tách từ và đọc dữ liệu từ chuỗi.

**NỘI DUNG :** 

- **strtok và bài toán tách từ**
- **Tách từ theo nhiều ký tự khác nhau**
- **Đọc dữ liệu từ chuỗi với sscanf**
- **Bài tập áp dụng**
- **Video Tutorial** 

---

**1. strtok và bài toán tách từ**

Thông thường khi chuẩn hóa hay xử lý chuỗi ký tự thì bạn cần tách riêng lẻ các từ trong chuỗi theo dấu cách hoặc một ký tự khác ví dụ như dấu . , ! ...

Hàm **strtok** nằm trong thư viện **string.h**, có nguyên mẫu:

```c
char *strtok(char *str, const char *delim);
```

- `str` : chuỗi cần tách (chỉ truyền ở **lần gọi đầu tiên**, các lần sau truyền `NULL` để tách tiếp chuỗi cũ).
- `delim` : chuỗi chứa **các ký tự phân cách** (delimiter), mỗi ký tự trong `delim` đều được coi là dấu phân cách.
- Giá trị trả về : con trỏ tới từ (token) tiếp theo, hoặc `NULL` khi đã hết từ.

Ví dụ sau mình sẽ tách từng từ trong chuỗi ra, sau khi tách xong bạn có thể chuẩn hóa, đếm từ ... với từ bạn tách được.

**Mã nguồn 1:**

```c
#include <stdio.h>
#include <string.h>

int main(){
	char s[] = "codelab    hoc  lap trinh";
	int dem = 0;
	// Lan goi dau tien truyen s, cac lan sau truyen NULL
	char *word = strtok(s, " ");
	while(word != NULL){
		++dem;
		printf("Tu thu %d tach duoc : %s\n", dem, word);
		word = strtok(NULL, " ");
	}
	return 0;
}
```

Output :

```
Tu thu 1 tach duoc : codelab
Tu thu 2 tach duoc : hoc
Tu thu 3 tach duoc : lap
Tu thu 4 tach duoc : trinh
```

**Giải thích mã nguồn :** 

- Lần gọi đầu tiên `strtok(s, " ")` tìm từ đầu tiên trong `s`. Hàm ghi ký tự `'\0'` vào ngay sau từ đó và trả về con trỏ tới đầu từ, nên `word` là một chuỗi hoàn chỉnh.
- Các lần gọi sau `strtok(NULL, " ")` tiếp tục tách từ vị trí mà lần gọi trước dừng lại (hàm tự ghi nhớ vị trí này). Vòng lặp dừng khi `strtok` trả về `NULL`, tức là không còn từ nào nữa.
- Giữa các từ có nhiều dấu cách sẽ được bỏ qua hết, `strtok` không bao giờ trả về từ rỗng.

**Lưu ý quan trọng :**

- `strtok` **làm thay đổi chuỗi gốc** (thay các dấu phân cách bằng `'\0'`). Vì vậy phải dùng mảng `char s[] = "..."`, **không** được dùng `char *s = "..."` vì chuỗi hằng không sửa được. Nếu còn cần chuỗi gốc thì hãy chép ra một bản sao bằng `strcpy` trước khi tách.
- `strtok` chỉ ghi nhớ **một** vị trí tách, nên không thể tách lồng hai chuỗi cùng lúc bằng `strtok`.

Trong trường hợp bạn muốn tách theo 1 ký tự khác, ví dụ như là dấu - thay vì dấu cách, bạn chỉ cần đổi tham số `delim`.

**Mã nguồn 2:** 

```c
#include <stdio.h>
#include <string.h>

int main(){
	char s[] = "codelab-hoc-lap-trinh";
	int dem = 0;
	char *word = strtok(s, "-");
	while(word != NULL){
		++dem;
		printf("Tu thu %d tach duoc : %s\n", dem, word);
		word = strtok(NULL, "-");
	}
	return 0;
}
```

Output :

```
Tu thu 1 tach duoc : codelab
Tu thu 2 tach duoc : hoc
Tu thu 3 tach duoc : lap
Tu thu 4 tach duoc : trinh
```

---

**2. Tách từ theo nhiều ký tự khác nhau**

Giả sử bạn cần tách chuỗi theo 1 loạt ký tự khác nhau (delimiter), với `strtok` việc này rất đơn giản: bạn chỉ cần liệt kê **tất cả** các ký tự phân cách trong tham số `delim`.

Ví dụ muốn tách chuỗi theo các ký tự : dấu chấm '.', dấu phẩy ',', dấu cách ' ', dấu hỏi chấm '?', và dấu chấm than '!' ta triển khai như sau

**Mã nguồn :** 

```c
#include <stdio.h>
#include <string.h>

int main(){
	char s[] = "codelab,hoc.lap!!trinh???C dsa";
	// Moi ky tu trong chuoi nay deu la dau phan cach
	const char *delim = " .,?!";
	int dem = 0;
	char *word = strtok(s, delim);
	while(word != NULL){
		++dem;
		printf("Tu thu %d tach duoc : %s\n", dem, word);
		word = strtok(NULL, delim);
	}
	return 0;
}
```

Output :

```
Tu thu 1 tach duoc : codelab
Tu thu 2 tach duoc : hoc
Tu thu 3 tach duoc : lap
Tu thu 4 tach duoc : trinh
Tu thu 5 tach duoc : C
Tu thu 6 tach duoc : dsa
```

Nhiều ký tự phân cách đứng liền nhau như `"!!"` hay `"???"` cũng chỉ được tính là một chỗ ngắt, nên không sinh ra từ rỗng. Nếu muốn tách theo mọi loại khoảng trắng (dấu cách, tab, xuống dòng) bạn dùng `delim = " \t\n"`.

---

**3. Đọc dữ liệu từ chuỗi với sscanf**

Hàm **sscanf** nằm trong thư viện **stdio.h**, hoạt động giống hệt `scanf` nhưng thay vì đọc từ bàn phím, nó đọc từ **một chuỗi** có sẵn.

```c
int sscanf(const char *str, const char *format, ...);
```

Giá trị trả về là **số biến đọc thành công**, nhờ đó bạn biết được dữ liệu có đúng định dạng hay không. Khác với `strtok`, `sscanf` **không** làm thay đổi chuỗi nguồn.

**Mã nguồn :** 

```c
#include <stdio.h>

int main(){
	char s[] = "An 20 8.5";
	char ten[50];
	int tuoi;
	double diem;
	int n = sscanf(s, "%49s %d %lf", ten, &tuoi, &diem);
	printf("Doc duoc %d gia tri\n", n);
	printf("Ten : %s, Tuoi : %d, Diem : %.1f\n", ten, tuoi, diem);

	int ngay, thang, nam;
	if(sscanf("17/09/2026", "%d/%d/%d", &ngay, &thang, &nam) == 3){
		printf("Ngay %d, thang %d, nam %d\n", ngay, thang, nam);
	}
	return 0;
}
```

Output :

```
Doc duoc 3 gia tri
Ten : An, Tuoi : 20, Diem : 8.5
Ngay 17, thang 9, nam 2026
```

**Giải thích mã nguồn :** 

- `%49s` đọc một từ (dừng ở khoảng trắng) và giới hạn tối đa 49 ký tự để không tràn mảng `ten` 50 phần tử.
- Đọc `double` phải dùng `%lf`. Các ký tự thường trong chuỗi định dạng như `/` phải khớp đúng với chuỗi nguồn.
- Kiểm tra `sscanf(...) == 3` để chắc chắn đọc đủ cả 3 giá trị.

**Đọc lần lượt nhiều số với %n**

Nếu gọi `sscanf(s, "%d", &x)` nhiều lần thì lần nào nó cũng đọc lại từ **đầu** chuỗi. Để đọc tiếp, bạn dùng đặc tả **%n**: nó không đọc gì cả mà ghi vào biến `int` **số ký tự đã xử lý** tính tới thời điểm đó. Cộng con trỏ thêm số ký tự này là ta nhảy tới phần chưa đọc.

**Mã nguồn :** 

```c
#include <stdio.h>

int main(){
	char s[] = "10 20   30 -5 100";
	char *p = s;
	int x, dadoc;
	long long tong = 0;
	while(sscanf(p, "%d%n", &x, &dadoc) == 1){
		printf("Doc duoc : %d\n", x);
		tong += x;
		p += dadoc;    // nhay qua phan da doc
	}
	printf("Tong = %lld\n", tong);
	return 0;
}
```

Output :

```
Doc duoc : 10
Doc duoc : 20
Doc duoc : 30
Doc duoc : -5
Doc duoc : 100
Tong = 155
```

**Lưu ý :** `%n` không được tính vào giá trị trả về của `sscanf`, nên điều kiện vẫn là `== 1`. Vòng lặp dừng khi hết chuỗi (`sscanf` trả về `EOF`) hoặc gặp dữ liệu không phải số (trả về `0`).

---

**4. Bài tập áp dụng**

**Bài tập 1** : Đếm số lượng từ trong chuỗi ký tự, giữa các từ có thể có nhiều dấu cách

Đối với bài toán này bạn có thể xử lý chuỗi bằng cách gặp ký tự khác dấu cách thì đếm 1 từ và xử lý nốt các ký tự còn lại của từ đó hoặc dùng strtok

```c
#include <stdio.h>
#include <string.h>

int main(){
	char s[] = "codelab codelab com vn blog AI    python";
	int cnt = 0;
	char *word = strtok(s, " ");
	while(word != NULL){
		++cnt;
		word = strtok(NULL, " ");
	}
	printf("So luong tu trong chuoi : %d\n", cnt);
	return 0;
}
```

Output :

```
So luong tu trong chuoi : 7
```

Nếu bạn không muốn sử dụng strtok (ví dụ vì không được sửa chuỗi gốc) thì có thể cài đặt như sau :

```c
#include <stdio.h>
#include <string.h>

int main(){
	char s[] = "codelab codelab com vn blog AI    python";
	int cnt = 0;
	int n = (int)strlen(s);
	for(int i = 0; i < n; i++){
		if(s[i] != ' '){
			++cnt;
			//duyet not cac ki tu cua tu bat dau tu chi so i
			while(i < n && s[i] != ' '){
				++i;
			}
			--i;
		}
	}
	printf("So luong tu trong chuoi : %d\n", cnt);
	return 0;
}
```

**Bài tập 2** : Chuẩn hóa từ và loại bỏ dấu cách thừa giữa các từ trong chuỗi, ví dụ " ngUYEN VaN tech28" thì chuẩn hóa thành "Nguyen Van Tech28"

Cách làm là bạn hãy tách các từ ra, chuẩn hóa từng từ rồi nối chung lại với nhau để tạo thành chuỗi chuẩn hóa.

Thay vì bạn cứ loay hoay xét từ và xóa dấu cách thừa thì việc tách ra, chuẩn hóa và gộp lại sẽ dễ và nhanh hơn nhiều.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){
	char s[] = "   NgUYeN   vAN   tECH28  ";
	char res[100] = "";
	char *word = strtok(s, " ");
	while(word != NULL){
		//Ki tu dau tien cua tung tu thi viet hoa
		word[0] = (char)toupper((unsigned char)word[0]);
		//Cac ki tu con lai thi viet thuong
		for(int j = 1; word[j] != '\0'; j++){
			word[j] = (char)tolower((unsigned char)word[j]);
		}
		//Them dau cach giua cac tu (tru truoc tu dau tien)
		if(res[0] != '\0') strcat(res, " ");
		strcat(res, word);
		word = strtok(NULL, " ");
	}
	printf("Chuoi chuan hoa : %s\n", res);
	return 0;
}
```

Output :

```
Chuoi chuan hoa : Nguyen Van Tech28
```

Ở đây mình chỉ thêm dấu cách **trước** mỗi từ (trừ từ đầu tiên), nên chuỗi kết quả không bị thừa dấu cách ở cuối.

**Bài tập 3** : Tính tổng các số nguyên xuất hiện trong chuỗi, ví dụ "a12bc 5 -- 3x" có tổng 12 + 5 + 3 = 20

Chuỗi có lẫn chữ cái nên không thể đọc thẳng bằng `sscanf`. Cách làm là duyệt chuỗi, khi gặp chữ số thì dùng `sscanf` với `%n` đọc cả số đó rồi nhảy qua, gặp ký tự khác thì bỏ qua.

```c
#include <stdio.h>
#include <ctype.h>

int main(){
	char s[] = "a12bc 5 -- 3x";
	long long tong = 0;
	char *p = s;
	while(*p != '\0'){
		int x, dadoc;
		if(isdigit((unsigned char)*p) && sscanf(p, "%d%n", &x, &dadoc) == 1){
			tong += x;
			p += dadoc;
		}
		else{
			p++;
		}
	}
	printf("Tong cac so : %lld\n", tong);
	return 0;
}
```

Output :

```
Tong cac so : 20
```

---

**Video String :**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/09-07-c-tach-chuoi-voi-strtok-va-sscanf.md](solutions/09-07-c-tach-chuoi-voi-strtok-va-sscanf.md)

**Bài 1.** Dùng `strtok` tách một dòng chứa nhiều số (cách nhau bởi dấu cách) thành mảng `int`, in ra các số và tổng của chúng.

**Bài 2.** Dùng `strtok` đếm số từ trong một câu nhập từ bàn phím và in lại từng từ có đánh số thứ tự.

**Bài 3.** Tách chuỗi CSV `"Binh,,7.0,"` theo dấu phẩy. Chỉ ra vì sao `strtok` làm mất trường rỗng và tự viết hàm tách giữ lại trường rỗng (dùng `strchr`).

**Bài 4.** Dùng `sscanf` đọc một dòng `"An 20 8.5"` (tên, tuổi, điểm) vào 3 biến khác kiểu; báo lỗi nếu dòng sai định dạng như `"Binh abc 7.0"`.

**Bài 5.** Tách chuỗi ngày tháng `"17/09/2026"` thành 3 số nguyên bằng `sscanf`, kiểm tra ngày, tháng có hợp lệ không.

**Bài 6.** Dùng `sscanf` kết hợp `%n` đọc lần lượt các số thực trong chuỗi `"1.5 2.25 -3 4e1"` và tính trung bình cộng.

**Bài 7.** Dùng `strtok` lưu các từ vào mảng con trỏ `char *tu[100]`, sau đó in các từ theo thứ tự đảo ngược.

**Bài 8.** Tách đoạn văn theo nhiều dấu phân cách `" ,.;:!?"`, in ra từ dài nhất và từ ngắn nhất.

**Bài 9.** Đọc nhiều dòng dữ liệu dạng `"ten diem"` bằng `fgets` + `sscanf`, bỏ qua dòng sai định dạng, tính điểm trung bình.

**Bài 10.** Đọc thời gian `"12:30:45"` bằng `sscanf`, đổi ra tổng số giây; phát hiện chuỗi sai như `"12-30-45"` hoặc `"25:00:00"`.

**Bài 11.** Chứng minh `strtok` làm thay đổi chuỗi gốc bằng cách in từng byte của mảng sau khi tách. Viết lại chương trình để chuỗi gốc được giữ nguyên.

**Bài 12.** Tách chuỗi `"a=1;b=2;c=3"` thành các cặp tên = giá trị. Giải thích vì sao không lồng được hai vòng `strtok`, và dùng `sscanf` với `%[^=]` để thay thế.

**Bài 13.** Tự cài đặt hàm `int tachTu(const char *s, char tu[][50])` không dùng `strtok`, không sửa chuỗi gốc, trả về số từ tách được.

**Bài 14.** Phân tích dữ liệu CSV nhiều dòng (mỗi dòng: họ tên, tuổi, điểm, thành phố), in ra dạng bảng căn lề và tính điểm trung bình.

**Bài 15.** Viết chương trình tính biểu thức đơn giản dạng `"12 + 34 * 2"` (tính lần lượt từ trái sang phải, không ưu tiên toán tử) bằng `sscanf` và `%n`.
