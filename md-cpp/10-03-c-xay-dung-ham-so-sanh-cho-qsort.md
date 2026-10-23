# [C]. Xây Dựng Hàm So Sánh Cho qsort

Để sử dụng hàm qsort() trong C một cách linh hoạt thì bạn cần biết xây dựng hàm so sánh - **comparison function** cho nó. Hiểu đơn giản thì hàm so sánh sẽ quyết định thứ tự sắp xếp các phần tử.

**NỘI DUNG :** 

- **Xây dựng hàm so sánh**
- **Bẫy tràn số khi viết return a - b**
- **Sắp xếp mảng với nhiều hơn 2 tiêu chí**
- **Sắp xếp mảng chuỗi**
- **Video tutorial** 

---

**1. Xây dựng hàm so sánh** 

Hàm so sánh khi sử dụng hàm qsort chính là tham số thứ 4 mà bạn sẽ truyền vào hàm khi sắp xếp mảng.

Hàm này có kiểu trả về là **int** và có 2 tham số kiểu **const void \***. qsort() dùng chung một hàm cho mọi kiểu mảng nên nó không biết phần tử của bạn là int, double hay struct, vì vậy nó chỉ truyền cho bạn **địa chỉ** của 2 phần tử cần so sánh dưới dạng con trỏ void.

Tên của hàm so sánh bạn tự đặt, thông thường mình hay đặt là cmp.

**Cú pháp hàm so sánh :** 

```c
int cmp(const void *a, const void *b){
     //B1: ep kieu con tro void ve con tro toi kieu phan tu
     const data_type *x = (const data_type *)a;
     const data_type *y = (const data_type *)b;
     //B2: logic so sanh *x va *y
}
```

Con trỏ void không thể dùng toán tử `*` để lấy giá trị, vì vậy bước đầu tiên luôn là **ép kiểu** về con trỏ tới đúng kiểu phần tử của mảng. Từ khoá `const` cho biết hàm so sánh chỉ đọc chứ không được thay đổi phần tử.

Logic khi trả về giá trị của hàm so sánh :

- Nếu muốn x đứng trước y sau khi sắp xếp thì trả về **số âm** (thường là -1)
- Nếu muốn x đứng sau y sau khi sắp xếp thì trả về **số dương** (thường là 1)
- Nếu x và y tương đương nhau về thứ tự thì trả về **0**

x và y ở đây bạn có thể coi như đó là 2 giá trị trong mảng mà bạn cần sắp xếp, khi sắp xếp thì hàm qsort cần so sánh giá trị giữa 2 phần tử này. Bạn chỉ cần kiểm tra xem thứ tự của x và y có thỏa mãn x sẽ đứng trước y theo thứ tự sắp xếp của mảng không thì bạn trả về số âm, nếu x phải đứng sau y thì trả về số dương.

Ví dụ như bạn muốn sắp xếp mảng tăng dần, vậy thì x nhỏ hơn y sẽ đứng trước y, khi đó bạn kiểm tra nếu x < y thì bạn trả về -1, nếu x > y thì trả về 1, còn lại trả về 0.

⚠️ Hàm so sánh phải **nhất quán** : nếu cmp(x, y) âm thì cmp(y, x) phải dương, và cmp(x, x) phải bằng 0. Hàm so sánh trả về kết quả mâu thuẫn sẽ làm qsort() sắp sai, thậm chí có thể gây lỗi chương trình.

**Ví dụ 1** : Sắp xếp mảng giảm dần

```c
#include <stdio.h>
#include <stdlib.h>

int cmp1(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(x > y)
		return -1; // x lon hon thi dung truoc
	else if(x < y)
		return 1;
	else
		return 0;
}

int main(){
	int a[] = {1, 3, 3, 3, 2, 1, 2, 4, 2, 4, 0, 2};
	int n = 12;
	qsort(a, n, sizeof(a[0]), cmp1);
	printf("Mang giam dan : ");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang giam dan : 4 4 3 3 3 2 2 2 2 1 1 0 
```

**Ví dụ 2** : Sắp xếp mảng theo tổng chữ số tăng dần

```c
#include <stdio.h>
#include <stdlib.h>

int tong(int n){
	int ans = 0;
	while(n){
		ans += n % 10;
		n /= 10;
	}
	return ans;
}

int cmp1(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	if(tong(x) < tong(y))
		return -1;
	else if(tong(x) > tong(y))
		return 1;
	else return 0;
}

int main(){
	int a[] = {1000000, 212, 40, 9, 10001, 30, 449};
	int n = 7;
	qsort(a, n, sizeof(a[0]), cmp1);
	printf("Mang sap xep theo tong chu so tang dan : \n");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang sap xep theo tong chu so tang dan : 
1000000 10001 30 40 212 9 449 
```

**Ví dụ 3** : Sắp xếp theo trị tuyệt đối giảm dần

Hàm `abs()` lấy trị tuyệt đối của số nguyên nằm trong thư viện **stdlib.h**.

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
	int x = abs(*(const int *)a);
	int y = abs(*(const int *)b);
	if(x > y)
		return -1;
	else if(x < y)
		return 1;
	else
		return 0;
}

int main(){
	int a[] = {3, -5, -1, 4, -2, 6, -7};
	int n = 7;
	qsort(a, n, sizeof(a[0]), cmp);
	printf("Mang sap xep theo tri tuyet doi giam dan : \n");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang sap xep theo tri tuyet doi giam dan : 
-7 6 -5 4 3 -2 -1 
```

---

**2. Bẫy tràn số khi viết return a - b**

Trên mạng bạn sẽ thường gặp cách viết hàm so sánh rất ngắn gọn cho mảng int như sau :

```c
int cmpNgan(const void *a, const void *b){
	return *(const int *)a - *(const int *)b; // NGUY HIEM
}
```

Ý tưởng là : nếu x < y thì x - y âm, nếu x > y thì x - y dương, nếu bằng nhau thì bằng 0. Cách này chạy đúng khi các số nhỏ, nhưng khi x và y **lớn và trái dấu** thì phép trừ x - y vượt quá giới hạn của kiểu int (khoảng ±2,1 tỷ) và bị **tràn số**. Trong C, tràn số với số nguyên có dấu là hành vi không xác định, trên thực tế kết quả thường bị "quay vòng" sang dấu ngược lại và qsort() nhận được thông tin so sánh sai.

**Ví dụ** : Sắp xếp mảng có các số rất lớn và rất nhỏ

```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int cmpNgan(const void *a, const void *b){
	return *(const int *)a - *(const int *)b; // co the tran so
}

int cmpAnToan(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	return (x > y) - (x < y); // chi tra ve -1, 0 hoac 1
}

int main(){
	int a[] = {2000000000, -2000000000, 5, INT_MIN, INT_MAX, 0};
	int b[] = {2000000000, -2000000000, 5, INT_MIN, INT_MAX, 0};
	int n = 6;
	qsort(a, n, sizeof(a[0]), cmpNgan);
	qsort(b, n, sizeof(b[0]), cmpAnToan);
	printf("Dung a - b     : ");
	for(int i = 0; i < n; i++) printf("%d ", a[i]);
	printf("\nDung so sanh   : ");
	for(int i = 0; i < n; i++) printf("%d ", b[i]);
	printf("\n");
	return 0;
}
```

Output (trên máy mình, dòng thứ nhất có thể khác trên máy bạn) :

```
Dung a - b     : 2000000000 -2147483648 -2000000000 0 5 2147483647 
Dung so sanh   : -2147483648 -2000000000 0 5 2000000000 2147483647 
```

Dòng thứ nhất hoàn toàn sai thứ tự : ví dụ `2000000000 - (-2000000000) = 4000000000` vượt quá INT_MAX nên bị tràn thành số âm, qsort() hiểu nhầm là 2000000000 nhỏ hơn -2000000000.

Biểu thức `(x > y) - (x < y)` chỉ gồm 2 phép so sánh, mỗi phép cho kết quả 0 hoặc 1, nên kết quả chỉ có thể là -1, 0 hoặc 1 và **không bao giờ tràn số**. Bạn cũng có thể dùng cách viết bằng if else như các ví dụ ở phần 1. Với mảng double hay long long cũng không được dùng `return x - y` vì kết quả trả về bị ép về int, phần thập phân hoặc phần bit cao sẽ bị mất.

---

**3. Sắp xếp mảng với nhiều hơn 2 tiêu chí**

Thông thường khi sắp xếp mảng sẽ có những giá trị có cùng thứ tự sắp xếp và khi đó họ sẽ yêu cầu bạn thêm 1 tiêu chí phụ nữa.

Ví dụ sắp xếp danh sách sinh viên theo gpa giảm dần, nếu 2 sinh viên có cùng gpa thì sinh viên nào có tên từ điển nhỏ hơn sẽ đứng trước.

Thậm chí đề bài có thể yêu cầu nhiều hơn 2 tiêu chí, tuy nhiên đối với đề bài yêu cầu kiểu này các bạn chỉ cần xét từ tiêu chí ưu tiên đầu tiên tới tiêu chí ưu tiên cuối cùng là được.

Nếu có thể sắp xếp theo tiêu chí chính thì không cần quan tâm tới tiêu chí phụ.

**Ví dụ 1** : Sắp xếp mảng theo tổng chữ số tăng dần, nếu 2 số có cùng tổng chữ số thì số lớn hơn sẽ đứng trước.

```c
#include <stdio.h>
#include <stdlib.h>

int tong(int n){
	int ans = 0;
	while(n){
		ans += n % 10;
		n /= 10;
	}
	return ans;
}

int cmp(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	int tx = tong(x), ty = tong(y);
	if(tx != ty){
		return (tx > ty) - (tx < ty); // tong nho hon dung truoc
	}
	else{
		return (x < y) - (x > y);     // so lon hon dung truoc
	}
}

int main(){
	int a[] = {111, 9, 3000, 20001, 18, 81, 405, 200, 1001};
	int n = 9;
	qsort(a, n, sizeof(a[0]), cmp);
	printf("Mang sau khi sap xep : \n");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang sau khi sap xep : 
1001 200 20001 3000 111 405 81 18 9 
```

Để ý rằng để sắp giảm dần theo tiêu chí phụ, mình chỉ cần đổi chỗ 2 vế của biểu thức : `(x < y) - (x > y)`.

**Ví dụ 2** : Sắp xếp sao cho số chẵn đứng trước, lẻ đứng sau, chẵn giảm dần, lẻ tăng dần

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
	int x = *(const int *)a;
	int y = *(const int *)b;
	int r1 = x % 2, r2 = y % 2;
	if(r1 == 0 && r2 == 1) return -1;       // x chan, y le: x truoc
	if(r1 == 1 && r2 == 0) return 1;        // x le, y chan: x sau
	if(r1 == 0) return (x < y) - (x > y);   // cung chan: giam dan
	return (x > y) - (x < y);               // cung le: tang dan
}

int main(){
	int a[] = {1, 2, 10, 9, 6, 5, 8, 7, 4, 3};
	int n = 10;
	qsort(a, n, sizeof(a[0]), cmp);
	printf("Mang sau khi sap xep : \n");
	for(int i = 0; i < n; i++){
		printf("%d ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Mang sau khi sap xep : 
10 8 6 4 2 1 3 5 7 9 
```

Lưu ý : với số âm lẻ thì phép `x % 2` trong C cho kết quả -1 chứ không phải 1, nếu mảng có số âm bạn nên kiểm tra chẵn lẻ bằng `x % 2 == 0`.

**Ví dụ 3** : Sắp xếp các điểm trong hệ tọa độ Oxy sao cho hoành độ tăng dần, nếu hoành độ bằng nhau thì sắp xếp theo tung độ giảm dần

Ở đây mình sẽ dùng struct để lưu điểm trong hệ tọa độ Oxy. Hàm so sánh ép kiểu con trỏ void về con trỏ struct `const Point *` rồi truy cập các trường bằng toán tử `->`.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int x, y;
} Point;

int cmp(const void *a, const void *b){
	const Point *p = (const Point *)a;
	const Point *q = (const Point *)b;
	if(p->x != q->x)
		return (p->x > q->x) - (p->x < q->x); // hoanh do tang dan
	else
		return (p->y < q->y) - (p->y > q->y); // tung do giam dan
}

int main(){
	Point a[] = {{3, 1}, {3, 2}, {1, 4}, {4, 3}, {3, 3}, {1, 1}, {4, 2}};
	int n = 7;
	qsort(a, n, sizeof(a[0]), cmp);
	printf("Mang sau khi sap xep : \n");
	for(int i = 0; i < n; i++){
		printf("%d %d\n", a[i].x, a[i].y);
	}
	return 0;
}
```

Output :

```
Mang sau khi sap xep : 
1 4
1 1
3 3
3 2
3 1
4 3
4 2
```

**Ví dụ 4** : Sắp xếp danh sách sinh viên theo gpa giảm dần, nếu 2 sinh viên có cùng gpa thì sinh viên có tên từ điển nhỏ hơn đứng trước

Tên sinh viên là chuỗi nên để so sánh bạn dùng hàm `strcmp()` trong thư viện **string.h**, hàm này đã trả về số âm, 0 hoặc số dương đúng theo quy ước của qsort() nên bạn có thể trả về trực tiếp kết quả của nó.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	char ten[30];
	double gpa;
} SinhVien;

int cmp(const void *a, const void *b){
	const SinhVien *s1 = (const SinhVien *)a;
	const SinhVien *s2 = (const SinhVien *)b;
	if(s1->gpa != s2->gpa){
		return (s1->gpa < s2->gpa) - (s1->gpa > s2->gpa); // gpa giam dan
	}
	return strcmp(s1->ten, s2->ten); // ten tang dan theo tu dien
}

int main(){
	SinhVien ds[] = {{"Nam", 3.2}, {"Hoa", 3.6}, {"Binh", 3.2},
	                 {"An", 3.6}, {"Tuan", 2.9}};
	int n = 5;
	qsort(ds, n, sizeof(ds[0]), cmp);
	printf("Danh sach sau khi sap xep : \n");
	for(int i = 0; i < n; i++){
		printf("%-6s %.1f\n", ds[i].ten, ds[i].gpa);
	}
	return 0;
}
```

Output :

```
Danh sach sau khi sap xep : 
An     3.6
Hoa    3.6
Binh   3.2
Nam    3.2
Tuan   2.9
```

Với struct, tham số size của qsort() là `sizeof(ds[0])`, tức kích thước của cả một struct. qsort() sẽ hoán đổi nguyên cả struct khi sắp xếp.

---

**4. Sắp xếp mảng chuỗi**

Trong C có 2 cách lưu một danh sách chuỗi, và hàm so sánh của 2 cách này **khác nhau** ở bước ép kiểu. Đây là chỗ rất nhiều bạn viết sai.

**Cách 1 : Mảng 2 chiều `char a[n][MAX]`**

Mỗi phần tử của mảng là một mảng char dài MAX byte, nên size là `sizeof(a[0])` (bằng MAX) và con trỏ void trỏ thẳng vào ký tự đầu của chuỗi. Bạn chỉ cần ép về `const char *` rồi gọi strcmp.

**Cách 2 : Mảng con trỏ `char *a[n]`**

Mỗi phần tử của mảng là một **con trỏ** char, nên size là `sizeof(char *)` và con trỏ void trỏ tới **con trỏ** char. Bạn phải ép về `const char * const *` (con trỏ tới con trỏ) rồi dùng `*` để lấy ra chuỗi.

**Ví dụ 1** : Sắp xếp danh sách tên theo thứ tự từ điển bằng cả 2 cách

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Cach 1: phan tu la mang char
int cmpMang2Chieu(const void *a, const void *b){
	return strcmp((const char *)a, (const char *)b);
}

// Cach 2: phan tu la con tro char
int cmpMangConTro(const void *a, const void *b){
	const char *s1 = *(const char * const *)a;
	const char *s2 = *(const char * const *)b;
	return strcmp(s1, s2);
}

int main(){
	char a[][20] = {"lan", "hoa", "cuc", "mai", "dao"};
	const char *b[] = {"lan", "hoa", "cuc", "mai", "dao"};
	int n = 5;
	qsort(a, n, sizeof(a[0]), cmpMang2Chieu);
	qsort(b, n, sizeof(b[0]), cmpMangConTro);
	printf("Mang 2 chieu : ");
	for(int i = 0; i < n; i++) printf("%s ", a[i]);
	printf("\nMang con tro : ");
	for(int i = 0; i < n; i++) printf("%s ", b[i]);
	printf("\n");
	return 0;
}
```

Output :

```
Mang 2 chieu : cuc dao hoa lan mai 
Mang con tro : cuc dao hoa lan mai 
```

Với mảng con trỏ, qsort() chỉ hoán đổi các **con trỏ** (8 byte) chứ không sao chép nội dung chuỗi nên sắp xếp nhanh hơn khi chuỗi dài. Nếu bạn dùng nhầm hàm `cmpMang2Chieu` cho mảng con trỏ, strcmp sẽ đọc các byte của địa chỉ như thể đó là ký tự và cho kết quả sai.

**Ví dụ 2** : Sắp xếp các từ theo độ dài tăng dần, nếu cùng độ dài thì sắp theo thứ tự từ điển

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void *a, const void *b){
	const char *s1 = (const char *)a;
	const char *s2 = (const char *)b;
	size_t l1 = strlen(s1), l2 = strlen(s2);
	if(l1 != l2)
		return (l1 > l2) - (l1 < l2); // ngan hon dung truoc
	return strcmp(s1, s2);
}

int main(){
	char a[][20] = {"python", "c", "java", "go", "rust", "cpp", "kotlin"};
	int n = 7;
	qsort(a, n, sizeof(a[0]), cmp);
	printf("Sap xep theo do dai : ");
	for(int i = 0; i < n; i++){
		printf("%s ", a[i]);
	}
	printf("\n");
	return 0;
}
```

Output :

```
Sap xep theo do dai : c go cpp java rust kotlin python 
```

`strlen()` trả về kiểu `size_t` là số không dấu, vì vậy càng không được viết `return l1 - l2;` : hiệu của 2 số không dấu không bao giờ âm, khi l1 < l2 kết quả sẽ là một số dương rất lớn.

---

**Video tutorial:**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-03-c-xay-dung-ham-so-sanh-cho-qsort.md](solutions/10-03-c-xay-dung-ham-so-sanh-cho-qsort.md)

**Bài 1.** Viết hàm so sánh sắp xếp mảng int **giảm dần** mà không dùng phép trừ.

**Bài 2.** Viết hàm so sánh cho mảng `double`. Giải thích vì sao `return x - y;` sai với số thực.

**Bài 3.** Tìm một cặp số `int` khiến hàm `return x - y;` trả về kết quả **sai dấu**. In ra để chứng minh, rồi sửa.

**Bài 4.** Sắp xếp mảng struct `{char ten[30]; int diem;}` theo điểm giảm dần.

**Bài 5.** Sắp xếp struct sinh viên theo 3 tiêu chí: điểm giảm, tuổi tăng, tên A-Z.

**Bài 6.** Viết hàm so sánh sắp xếp số theo tổng chữ số (xử lý được cả số âm).

**Bài 7.** Viết hàm so sánh sắp xếp mảng chuỗi theo số nguyên âm trong chuỗi.

**Bài 8.** Sắp xếp các điểm theo khoảng cách tới một điểm `(px, py)` nhập từ bàn phím. Hàm so sánh của `qsort` không nhận thêm tham số — hãy dùng biến toàn cục.

**Bài 9.** Viết hàm so sánh để sắp xếp mảng ngày tháng dạng chuỗi `"dd/mm/yyyy"` theo thời gian.

**Bài 10.** Sắp xếp một mảng con trỏ `char *ds[]` theo thứ tự từ điển **không phân biệt hoa thường**.

**Bài 11.** Hàm so sánh nào dưới đây sai? Giải thích:

```c
int c1(const void *a, const void *b){ return *(const int *)a - *(const int *)b; }
int c2(const void *a, const void *b){ return *(const int *)a > *(const int *)b; }
int c3(const void *a, const void *b){ int x = *(const int *)a, y = *(const int *)b; return (x > y) - (x < y); }
int c4(const void *a, const void *b){ return strcmp((const char *)a, (const char *)b); } // dung cho char *ds[]
```

**Bài 12.** Đếm tần suất các từ trong một câu (lưu vào mảng struct `{char tu[20]; int dem;}`), rồi in theo tần suất giảm dần, cùng tần suất thì theo từ A-Z.

**Bài 13.** Viết hàm so sánh sắp xếp "ưu tiên": các từ nằm trong danh sách ưu tiên đứng trước, còn lại xếp sau, mỗi nhóm theo A-Z.

**Bài 14.** Sắp xếp **mảng chỉ số** `idx[]` theo giá trị `a[idx[i]]` để in thứ hạng mà **không làm thay đổi** mảng gốc `a[]`.

**Bài 15.** Viết "bộ sưu tập hàm so sánh" tái sử dụng được (int tăng/giảm, double, chuỗi, chuỗi theo độ dài) và một chương trình dùng thử.
