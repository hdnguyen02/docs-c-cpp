# [C]. Hàm qsort Trong C

Hàm **qsort()** trong thư viện stdlib.h của ngôn ngữ lập trình C là hàm sắp xếp có sẵn, rất hiệu quả và được sử dụng thường xuyên trong lập trình. Bài học này sẽ hướng dẫn các bạn cách sử dụng hàm qsort() để sắp xếp mảng số nguyên, mảng số thực và mảng ký tự.

**NỘI DUNG :** 

- **Hàm qsort() trong C**
- **Hàm so sánh cơ bản cho qsort()**
- **Sắp xếp mảng int, double, char**
- **Một số bài tập áp dụng hàm qsort()**
- **Video tutorial** 

---

**1. Hàm qsort() trong C**

Hàm **qsort()** là hàm thuộc thư viện **stdlib.h**, bạn có thể sử dụng ngay hàm này khi cần sắp xếp mà không cần cài đặt lại thuật toán sắp xếp từ đầu.

Chuẩn C không quy định qsort() phải cài đặt bằng thuật toán nào, nhưng các thư viện C thông dụng đều cài đặt bằng những thuật toán hiệu quả, độ phức tạp trung bình là **O(NlogN)**, nhanh hơn rất nhiều so với các thuật toán O(N²) như sắp xếp nổi bọt hay chọn.

Khác với các hàm sắp xếp mà bạn tự viết chỉ dùng được cho một kiểu dữ liệu, qsort() sắp xếp được mảng thuộc **mọi kiểu**: int, long long, double, char, chuỗi, struct... Để làm được điều đó, bạn phải cho qsort() biết 4 thông tin.

**Nguyên mẫu hàm :** 

```c
void qsort(void *base, size_t nmemb, size_t size,
           int (*compar)(const void *, const void *));
```

Ý nghĩa 4 tham số :

1. **base** : địa chỉ phần tử đầu tiên của đoạn cần sắp xếp, thường là tên mảng `a`
2. **nmemb** : số phần tử cần sắp xếp, thường là `n`
3. **size** : kích thước (số byte) của **một** phần tử, viết `sizeof(a[0])` hoặc `sizeof(int)`
4. **compar** : tên hàm so sánh do bạn tự viết, hàm này quyết định thứ tự sắp xếp

Vì qsort() không biết mảng của bạn có kiểu gì nên nó chỉ nhìn mảng như một dãy byte, mỗi phần tử dài `size` byte. Mỗi khi cần so sánh 2 phần tử, qsort() sẽ gọi hàm so sánh của bạn và truyền vào **địa chỉ** của 2 phần tử đó.

**Cú pháp sắp xếp mảng :** 

```c
//Sắp xếp toàn bộ mảng a có n phần tử
qsort(a, n, sizeof(a[0]), cmp);
//Sắp xếp mảng a từ chỉ số x tới chỉ số y
qsort(a + x, y - x + 1, sizeof(a[0]), cmp);
```

Khi sắp xếp một đoạn, tham số đầu là `a + x` (địa chỉ của phần tử `a[x]`) và tham số thứ hai là **số phần tử** của đoạn, tức là `y - x + 1`, chứ không phải chỉ số cuối.

---

**2. Hàm so sánh cơ bản cho qsort()**

Hàm so sánh của qsort() luôn có dạng :

```c
int cmp(const void *a, const void *b){
    //logic
}
```

Hai tham số `a`, `b` là **con trỏ void** trỏ tới 2 phần tử cần so sánh. Vì con trỏ void không thể lấy giá trị trực tiếp, bạn phải **ép kiểu** về con trỏ tới kiểu phần tử của mảng rồi mới dùng toán tử `*` để lấy giá trị. Ví dụ với mảng int : `int x = *(const int *)a;`

Logic khi trả về giá trị của hàm so sánh :

- Trả về số **âm** nếu muốn a đứng **trước** b sau khi sắp xếp
- Trả về số **dương** nếu muốn a đứng **sau** b sau khi sắp xếp
- Trả về **0** nếu coi a và b bằng nhau về thứ tự

**Hàm so sánh sắp xếp tăng dần :** 

```c
int cmpTang(const void *a, const void *b){
    int x = *(const int *)a;
    int y = *(const int *)b;
    if(x < y) return -1; // x nho hon thi dung truoc
    if(x > y) return 1;  // x lon hon thi dung sau
    return 0;
}
```

**Hàm so sánh sắp xếp giảm dần :** chỉ cần đảo ngược kết quả, số lớn hơn sẽ đứng trước.

```c
int cmpGiam(const void *a, const void *b){
    int x = *(const int *)a;
    int y = *(const int *)b;
    if(x > y) return -1; // x lon hon thi dung truoc
    if(x < y) return 1;
    return 0;
}
```

Bạn có thể gặp cách viết ngắn gọn `return x - y;` cho sắp tăng dần. Cách này chạy đúng với số nhỏ nhưng **có thể bị tràn số** khi x, y rất lớn hoặc trái dấu, vì vậy nên dùng cách so sánh bằng if như trên. Chi tiết về lỗi này và cách viết hàm so sánh phức tạp hơn sẽ được trình bày trong bài [Xây Dựng Hàm So Sánh Cho qsort](10-03-c-xay-dung-ham-so-sanh-cho-qsort.md).

---

**3. Sắp xếp mảng int, double, char**

**Ví dụ 1 :** Sắp xếp mảng số nguyên tăng dần và giảm dần

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int cmpGiam(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x > y) return -1;
	if(x < y) return 1;
	return 0;
}

int main(){
	int a[] = {3, 1, 2, 5, 6, 4, 8, 9, 10, 7};
	int n = 10;
	qsort(a, n, sizeof(a[0]), cmpTang);
	printf("Mang a sau khi sap xep tang dan : ");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	qsort(a, n, sizeof(a[0]), cmpGiam);
	printf("\nMang a sau khi sap xep giam dan : ");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang a sau khi sap xep tang dan : 1 2 3 4 5 6 7 8 9 10 
Mang a sau khi sap xep giam dan : 10 9 8 7 6 5 4 3 2 1 
```

**Ví dụ 2 :** Sắp xếp mảng ký tự

Mỗi ký tự trong C thực chất là một số nguyên (mã ASCII), nên sắp xếp mảng char tăng dần chính là sắp theo mã ASCII : chữ số `'0'..'9'` đứng trước, sau đó tới chữ in hoa, cuối cùng là chữ in thường. Hàm so sánh ép kiểu về `const char *`.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpChar(const void *a, const void *b){
	char x = *(const char *)a;
	char y = *(const char *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int cmpCharGiam(const void *a, const void *b){
	return cmpChar(b, a); // doi cho a, b -> dao nguoc thu tu
}

int main(){
	char a[] = {'2', '8', 't', 'e', 'c', 'h', 'a', 'z'};
	int n = 8;
	qsort(a, n, sizeof(a[0]), cmpChar);
	printf("Mang char sap tang dan : ");
	for(int i = 0; i < n; i++){
		printf("%c ", a[i]);
	}
	qsort(a, n, sizeof(a[0]), cmpCharGiam);
	printf("\nMang char sap giam dan : ");
	for(int i = 0; i < n; i++){
		printf("%c ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang char sap tang dan : 2 8 a c e h t z 
Mang char sap giam dan : z t h e c a 8 2 
```

Mẹo : hàm `cmpCharGiam` chỉ cần gọi lại `cmpChar` với 2 tham số đổi chỗ cho nhau, khi đó kết quả so sánh bị đảo ngược và mảng được sắp giảm dần.

Nếu bạn muốn sắp xếp các ký tự của một **chuỗi**, hãy dùng `strlen(s)` làm số phần tử để không sắp luôn cả ký tự kết thúc `'\0'` :

```c
char s[] = "codelab";
qsort(s, strlen(s), sizeof(s[0]), cmpChar); // s = "abcdelo"
```

**Ví dụ 3 :** Sắp xếp mảng số thực

Với mảng double, hàm so sánh ép kiểu về `const double *` và tham số size là `sizeof(double)`. Tuyệt đối không viết `return x - y;` vì hiệu của 2 số thực là số thực, khi trả về kiểu int sẽ bị cắt phần thập phân : hiệu `0.5` bị biến thành `0` và qsort() hiểu nhầm 2 số bằng nhau.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpDouble(const void *a, const void *b){
	double x = *(const double *)a;
	double y = *(const double *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int main(){
	double a[] = {3.5, 1.25, 2.0, 5.75, 4.5};
	int n = 5;
	qsort(a, n, sizeof(a[0]), cmpDouble);
	printf("Mang double sap tang dan : ");
	for(int i = 0; i < n; i++){
		printf("%.2f ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang double sap tang dan : 1.25 2.00 3.50 4.50 5.75 
```

**Ví dụ 4 :** Sắp xếp một đoạn của mảng

Sắp xếp các phần tử từ chỉ số 2 tới chỉ số 6 của mảng, các phần tử còn lại giữ nguyên.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int main(){
	int a[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
	int n = 10;
	int x = 2, y = 6;
	qsort(a + x, y - x + 1, sizeof(a[0]), cmpTang);
	printf("Mang sau khi sap xep doan [2, 6] : ");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang sau khi sap xep doan [2, 6] : 9 8 3 4 5 6 7 2 1 0 
```

**Lưu ý khi dùng qsort() :** 

- Phải `#include <stdlib.h>`, nếu thiếu trình biên dịch sẽ báo lỗi hoặc cảnh báo khai báo ngầm hàm
- Tham số size phải đúng kích thước **một phần tử** của mảng, dùng `sizeof(a[0])` là an toàn nhất
- Kiểu ép trong hàm so sánh phải **khớp** với kiểu phần tử của mảng, mảng double mà ép về `int *` sẽ cho kết quả sai
- qsort() **không đảm bảo ổn định** : các phần tử bằng nhau có thể bị đổi thứ tự tương đối (xem bài [Sắp Xếp Ổn Định Và Merge Sort](10-04-c-sap-xep-on-dinh-va-merge-sort.md))

---

**4. Một số bài tập áp dụng hàm qsort()**

Có nhiều bài toán mà bạn có thể sử dụng bước sắp xếp trước khi xử lý, phần này mình sẽ hướng dẫn các bạn 3 ví dụ để luyện tập với hàm qsort. Cả 3 ví dụ đều dùng chung hàm so sánh `cmpTang` ở trên.

**Bài 1**. Đếm số lượng giá trị khác nhau trong mảng

**Thuật toán** : Sắp xếp mảng tăng dần để các giá trị giống nhau sẽ đứng cạnh nhau, khi đó bạn chỉ cần so sánh 2 phần tử kề nhau trong mảng để đếm số giá trị khác nhau. Nếu 2 phần tử đứng cạnh nhau mà bằng nhau thì bạn không cần tăng số giá trị khác nhau lên.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int main(){
	int a[] = {1, 3, 3, 3, 2, 1, 2, 2, 2, 4, 0, 2};
	int n = 12;
	qsort(a, n, sizeof(a[0]), cmpTang);
	int dem = 1; // a[0]
	for(int i = 1; i < n; i++){
		if(a[i] != a[i - 1]){
			++dem;
		}
	}
	printf("So gia tri khac nhau : %d\n", dem);
	return 0;
}
```

Output :

```
So gia tri khac nhau : 5
```

**Bài 2** : Tìm độ chênh lệch nhỏ nhất giữa 2 phần tử trong mảng

**Thuật toán** : Sắp xếp mảng tăng dần (hoặc giảm dần) để những giá trị gần nhau sẽ đứng cạnh nhau khi đó bạn chỉ cần xét độ chênh lệch giữa 2 phần tử đứng cạnh nhau và tìm giá trị nhỏ nhất.

Độ phức tạp sẽ là O(NlogN) thay vì O(N²) nếu bạn dùng 2 vòng for lồng nhau để xét mọi cặp phần tử trong mảng.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int main(){
	int a[] = {3, 8, 10, 4, 12, 21, 1};
	int n = 7;
	qsort(a, n, sizeof(a[0]), cmpTang);
	int min_diff = 1000000000;
	for(int i = 1; i < n; i++){
		if(a[i] - a[i - 1] < min_diff){
			min_diff = a[i] - a[i - 1];
		}
	}
	printf("Do chenh lech nho nhat : %d\n", min_diff);
	return 0;
}
```

Output :

```
Do chenh lech nho nhat : 1
```

**Bài 3**. Đếm tần suất xuất hiện của từng giá trị trong mảng và liệt kê theo thứ tự từ nhỏ tới lớn

**Thuật toán** : Sắp xếp mảng tăng dần sau đó xét các cặp phần tử đứng cạnh nhau để đếm tần suất xuất hiện, vì khi sắp tăng dần thì các giá trị giống nhau sẽ đứng cạnh nhau.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x < y) return -1;
	if(x > y) return 1;
	return 0;
}

int main(){
	int a[] = {1, 3, 3, 3, 2, 1, 2, 4, 2, 4, 0, 2};
	int n = 12;
	qsort(a, n, sizeof(a[0]), cmpTang);
	int dem = 1; // a[0];
	for(int i = 1; i < n; i++){
		if(a[i] == a[i - 1]){
			++dem;
		}
		else{
			printf("%d xuat hien %d lan\n", a[i - 1], dem);
			dem = 1;
		}
	}
	printf("%d xuat hien %d lan\n", a[n - 1], dem);
	return 0;
}
```

Output :

```
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

> 📘 Lời giải tham khảo: [solutions/10-02-c-ham-qsort-trong-c.md](solutions/10-02-c-ham-qsort-trong-c.md)

**Bài 1.** Nhập mảng `n` số nguyên từ bàn phím, dùng `qsort` sắp xếp tăng dần rồi in ra.

**Bài 2.** Sắp xếp mảng giảm dần bằng 2 cách: viết hàm so sánh giảm dần, và sắp tăng dần rồi đảo ngược mảng.

**Bài 3.** Nhập `l`, `r`, chỉ sắp xếp **đoạn** `a[l..r]` của mảng tăng dần, các phần tử khác giữ nguyên.

**Bài 4.** Sắp xếp mảng `double` tăng dần, in mỗi số với 2 chữ số sau dấu phẩy.

**Bài 5.** Nhập một chuỗi, sắp xếp các ký tự của chuỗi tăng dần (không sắp ký tự `'\0'`).

**Bài 6.** Sắp xếp mảng `long long` có các số tới 10¹⁸, viết hàm so sánh đúng kiểu.

**Bài 7.** Kiểm tra hai chuỗi có phải **anagram** của nhau không (cùng các ký tự, khác thứ tự) bằng cách sắp xếp ký tự.

**Bài 8.** Tìm phần tử lớn thứ `k` trong mảng (các phần tử có thể trùng nhau).

**Bài 9.** Sau khi sắp xếp, loại bỏ các phần tử trùng lặp và in mảng các giá trị phân biệt.

**Bài 10.** Tìm **trung vị** của một mảng số thực (phần tử đứng giữa sau khi sắp xếp; nếu `n` chẵn lấy trung bình 2 phần tử giữa).

**Bài 11.** Sắp xếp nửa đầu mảng tăng dần và nửa sau giảm dần.

**Bài 12.** Kiểm tra hai mảng có chứa **cùng các phần tử** không (kể cả số lần lặp lại).

**Bài 13.** So sánh tốc độ `qsort` với Bubble Sort tự viết trên mảng 100.000 phần tử (đo bằng `clock()`).

**Bài 14.** Chương trình sau in ra kết quả sai. Tìm tất cả các lỗi và sửa:

```c
double a[] = {3.5, 1.2, 2.8, 0.9};
int cmp(const void *x, const void *y){ return *(int *)x - *(int *)y; }
qsort(a, 4, sizeof(int), cmp);
```

**Bài 15.** Viết chương trình quản lý điểm: nhập `n` điểm số thực, có menu cho phép sắp xếp tăng/giảm, in điểm cao nhất, thấp nhất và trung vị.
