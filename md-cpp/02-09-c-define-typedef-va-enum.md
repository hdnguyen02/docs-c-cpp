# [C]. Define, Typedef Và Enum

Trong bài viết này mình sẽ giúp các bạn sử dụng thành thạo và phân biệt được 2 từ khóa **define** và **typedef** trong C, đồng thời làm quen với kiểu liệt kê **enum** dùng để đặt tên cho một nhóm hằng số nguyên.

**NỘI DUNG** 

- **Typedef**
- **Define**
- **Sự Khác Nhau Giữa Define Và Typedef**
- **Kiểu Liệt Kê Enum**

---

**1.Typedef**

**Typedef** giúp bạn tạo một tên mới cho các kiểu dữ liệu trong ngôn ngữ C

Sau khi tạo một bí danh mới cho các kiểu dữ liệu đó thì bạn có thể sử dụng tên mới hoặc tên cũ của kiểu dữ liệu đó đều được.

Cú pháp : typedef kiểu_dữ_liệu tên_mới;

Ví dụ 1:

```c
#include <stdio.h>
#include <stdbool.h>

typedef int songuyen;
typedef long long ll;
typedef double sothuc;
typedef bool dungsai;

int main(){
    songuyen a = 1000;
    ll b = 2828282828282;
    sothuc c = 3.1239;
    dungsai check = true;
    printf("%d %lld\n", a, b);
    printf("%.2f\n", c);
    printf("%d\n", check);
    return 0;
}
```

Output :

```
1000 2828282828282
3.12
1
```

**Chú ý :** Kiểu `bool` trong C nằm trong thư viện **stdbool.h**, khi in bằng `printf` thì `true` được in ra là `1` và `false` là `0`.

Ví dụ 2 : Định nghĩa tên cho kiểu struct

Typedef rất hay được dùng để đặt tên ngắn gọn cho kiểu **struct** (cấu trúc gồm nhiều thành phần, bạn sẽ học kỹ ở bài struct). Nếu không có typedef bạn phải viết `struct Diem` mỗi lần khai báo biến.

```c
#include <stdio.h>

typedef char kitu;
typedef struct {
    int x;
    int y;
} Diem;

int main(){
    kitu c = '@';
    printf("%c\n", c);
    Diem p = {100, 200};
    printf("%d %d\n", p.x, p.y);
    return 0;
}
```

Output :

```
@
100 200
```

---

**2.Define**

**Define** có 3 chức năng chính :

- Định nghĩa tên cho kiểu dữ liệu
- Định nghĩa tên cho giá trị
- Định nghĩa tên cho cấu trúc hoặc câu lệnh

**Định nghĩa tên cho kiểu dữ liệu** 

**Define** có thể sử dụng để làm công việc tương tự như **typedef** đó là định nghĩa tên mới cho kiểu dữ liệu

Cú pháp : #define tên_mới kiểu_dữ_liệu

Ví dụ 1 :

```c
#include <stdio.h>
#include <stdbool.h>

#define songuyen int
#define ll long long
#define sothuc double
#define dungsai bool

int main(){
    songuyen a = 1000;
    ll b = 2828282828282;
    sothuc c = 3.1239;
    dungsai check = true;
    printf("%d %lld\n", a, b);
    printf("%.2f\n", c);
    printf("%s\n", check ? "true" : "false");
    return 0;
}
```

Output :

```
1000 2828282828282
3.12
true
```

**Định nghĩa tên cho giá trị**

**Define** được sử dụng để đặt tên cho các giá trị được sử dụng trong chương trình nhằm mục đích truyền tải ý nghĩa tốt hơn

Cú pháp : #define tên_giá_trị giá_trị

Ví dụ 2 :

```c
#include <stdio.h>

#define PI 3.14
#define INF 1000000000
#define TRUE 1
#define FALSE 0
#define Tech28 "codelab.dev"
#define mod 1000000007

int main(){
    printf("%.2f\n", PI);
    printf("%d\n", INF);
    printf("%d\n", TRUE);
    printf("%d\n", FALSE);
    printf("%s\n", Tech28);
    printf("%d\n", mod);
    return 0;
}
```

Output :

```
3.14
1000000000
1
0
codelab.dev
1000000007
```

**Định nghĩa tên cho cấu trúc hoặc câu lệnh**

Việc sử dụng **define** để định nghĩa các câu lệnh hay cấu trúc thường được sử dụng bởi các bạn lập trình viên trong các cuộc thi về lập trình thi đấu hay thuật toán. Mục đích là có thể tiết kiệm thời gian code, tuy nhiên việc này sẽ dẫn tới khó khăn cho người khác khi cần tham khảo mã nguồn.

Hiện tại các bạn mới học lập trình thì chưa nên sử dụng **define** với mục đích này, sau này khi đã code tốt hơn các bạn có thể sử dụng nó để tiết kiệm thời gian code. Tuy nhiên mình nghĩ bạn chỉ nên sử dụng khi bạn code một mình và không cần chia sẻ mã nguồn cho người khác.

Ví dụ 3 :

```c
#include <stdio.h>

//Định nghĩa cấu trúc để in ra dòng chữ codelab.dev
#define greet printf("codelab.dev\n");

//Định nghĩa cấu trúc vòng lặp for
#define FOR(i, a, b) for(int i = a; i <= b; i++)

//Định nghĩa cấu trúc để in ra số lớn hơn trong 2 số
#define findMax(a, b) printf("%d\n", (a > b ? a : b));

int main(){
    greet;
    greet;
    findMax(10, 20);
    findMax(100, 50);
    FOR(i, 1, 5){
        printf("%d ", i);
    }
    return 0;
}
```

Output :

```
codelab.dev
codelab.dev
20
100
1 2 3 4 5
```

---

**3. Sự Khác Nhau Giữa Define Và Typedef**

| **Typedef** | **#Define** |
|---|---|
| Chỉ sử dụng để đặt tên thay thế cho kiểu dữ liệu | Có thể sử dụng để đặt tên cho kiểu dữ liệu, giá trị, cấu trúc, câu lệnh |
| Kết thúc bởi dấu ; | Không có kết thúc bằng dấu ; |
| Được xử lý bởi trình biên dịch (Compiler) | Được xử lý bởi preprocessor |
| Không có dấu # | Bắt đầu bởi dấu # |

---

**4. Kiểu Liệt Kê Enum**

**Enum** (enumeration - kiểu liệt kê) cho phép bạn đặt tên cho một nhóm các hằng số nguyên có liên quan với nhau, ví dụ các ngày trong tuần, các màu sắc, các trạng thái... Nhờ vậy code dễ đọc hơn rất nhiều so với việc dùng các con số 0, 1, 2 trực tiếp.

Cú pháp : enum tên_enum { HANG_1, HANG_2, ... };

- Mặc định hằng đầu tiên có giá trị **0**, các hằng tiếp theo lần lượt tăng thêm 1.
- Bạn có thể gán giá trị cụ thể cho một hằng, các hằng phía sau sẽ tăng dần từ giá trị đó.
- Các hằng của enum có kiểu **int**, in ra bằng `%d`.

Ví dụ 1 :

```c
#include <stdio.h>

enum Mau { DO, XANH, VANG };
enum Thang { THANG1 = 1, THANG2, THANG3 };
enum TrangThai { THANH_CONG = 200, KHONG_TIM_THAY = 404, LOI_SERVER = 500 };

int main(){
    enum Mau m = XANH;
    printf("%d %d %d\n", DO, XANH, VANG);
    printf("m = %d\n", m);
    printf("%d %d %d\n", THANG1, THANG2, THANG3);
    printf("%d\n", KHONG_TIM_THAY);
    return 0;
}
```

Output :

```
0 1 2
m = 1
1 2 3
404
```

Ví dụ 2 : Kết hợp **typedef** và **enum**

Khi khai báo biến kiểu enum bạn phải viết cả từ khóa `enum` (ví dụ `enum Mau m`). Kết hợp với typedef bạn có thể bỏ từ khóa này đi cho gọn :

```c
#include <stdio.h>

typedef enum { THU2 = 2, THU3, THU4, THU5, THU6, THU7, CHUNHAT = 8 } Ngay;

int main(){
    Ngay hom_nay = THU6;
    printf("Hom nay la thu %d\n", hom_nay);
    if(hom_nay == THU7 || hom_nay == CHUNHAT){
        printf("Cuoi tuan\n");
    }
    else{
        printf("Ngay lam viec\n");
    }
    return 0;
}
```

Output :

```
Hom nay la thu 6
Ngay lam viec
```

So với cách dùng `#define` để tạo nhiều hằng số, **enum** có ưu điểm là các giá trị được tự động đánh số, được nhóm lại dưới một tên kiểu và được xử lý bởi trình biên dịch.

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-09-c-define-typedef-va-enum.md](solutions/02-09-c-define-typedef-va-enum.md)

**Bài 1.** Dùng `typedef` đặt tên `ll` cho `long long`, `ull` cho `unsigned long long`, và `Diem` cho một struct gồm 2 số nguyên `x`, `y`. Viết chương trình sử dụng cả 3 bí danh này.

**Bài 2.** Dùng `enum` định nghĩa 7 ngày trong tuần (`THU2` đến `CHUNHAT`) với `THU2 = 2`. In giá trị số của từng hằng, rồi làm lại với `typedef enum`.

**Bài 3.** Dùng `#define` để định nghĩa các hằng: `PI = 3.14159`, `INF = 1000000000`, `MOD = 1000000007`. In cả 3 ra màn hình.

**Bài 4.** Viết chương trình tính diện tích hình tròn dùng `#define PI 3.14159`, sau đó viết lại bằng `const double PI`. So sánh 2 cách.

**Bài 5.** Định nghĩa macro `FOR(i, a, b)` tương đương vòng lặp `for(int i = a; i <= b; i++)`, rồi dùng nó để in các số từ 1 đến 10.

**Bài 6.** Định nghĩa macro `MAX(a, b)` trả về số lớn hơn. Thử với `MAX(3, 7)` và `MAX(2+3, 4)`.

**Bài 7.** Chạy đoạn code sau và giải thích vì sao kết quả **sai**:

```c
#define BINH_PHUONG(x) x * x
printf("%d\n", BINH_PHUONG(2 + 3));
```

**Bài 8.** Sửa macro ở bài 7 cho đúng. Sau đó thử với `BINH_PHUONG(i++)` và giải thích vì sao vẫn có vấn đề.

**Bài 9.** Lập bảng so sánh `#define`, `typedef`, `enum`, `const` theo các tiêu chí: ai xử lý (preprocessor hay compiler), có kiểm tra kiểu không, có dấu `;` không, dùng cho mục đích gì.

**Bài 10.** Dùng `#define` tạo shortcut cho các câu lệnh hay dùng trong lập trình thi đấu: `ll` (long long), `FOR(i, a, b)`, `FORD(i, a, b)` (lặp giảm dần), `SQR(x)` (bình phương). Viết chương trình minh hoạ.

**Bài 11.** `typedef` có làm được việc này không: `typedef 3.14 PI;`? Thử biên dịch và giải thích.

**Bài 12.** Dùng `typedef` tạo bí danh cho kiểu mảng 2 chiều `int[3][3]` tên là `Matrix`, rồi khai báo và in một ma trận 3×3.

**Bài 13.** Tìm hiểu `#define` có điều kiện (`#ifdef`, `#ifndef`, `#endif`). Viết chương trình có chế độ DEBUG bật/tắt được bằng một dòng `#define DEBUG`.

**Bài 14.** Viết một "template thi đấu" (competitive programming template) bằng C gồm các `typedef`/`define` mà bạn thấy tiện, kèm chú thích giải thích từng dòng.

**Bài 15.** Đọc đoạn code sau (viết theo phong cách thi đấu) và viết lại thành code C thông thường, dễ đọc, không dùng macro:

```c
#include <stdio.h>
#define ll long long
#define FOR(i,a,b) for(ll i=a;i<=b;i++)
#define SQR(x) ((x)*(x))
#define sz(a) (int)(sizeof(a)/sizeof(a[0]))
int main(){
    ll a[5];
    FOR(i,0,sz(a)-1) a[i] = SQR(i+1);
    FOR(i,0,sz(a)-1) printf("%lld ", a[i]);
}
```
