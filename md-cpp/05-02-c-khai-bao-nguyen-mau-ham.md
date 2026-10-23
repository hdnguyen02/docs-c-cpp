# [C]. Khai Báo Nguyên Mẫu Hàm

Khai báo nguyên mẫu hàm - **Function Prototype** giúp người đọc code của bạn có thể nhanh chóng nhận biết số lượng hàm được xây dựng trong chương trình và các thông tin liên quan của hàm đó.

**NỘI DUNG :** 

- **Nguyên Mẫu Hàm**
- **Ví Dụ**

---

**Nguyên Mẫu Hàm**

Khai báo nguyên mẫu hàm nhằm cung cấp các thông tin của hàm cho trình biên dịch bao gồm

- Kiểu trả về của hàm
- Tên hàm
- Số lượng tham số của hàm
- Dánh sách kiểu dữ liệu của các tham số

Với hàm không có tham số, trong C bạn nên viết nguyên mẫu là `void greet(void);`. Nếu chỉ viết `void greet();` thì (trước chuẩn C23) trình biên dịch hiểu là "chưa nói gì về tham số" và sẽ không kiểm tra số đối số khi bạn gọi hàm.

Ví dụ 1 :

```c
#include <stdio.h>

//function prototype
void greet(void);
int tong(int, int, int);
long long solve(int, long long);

void greet(void){
    printf("codelab.dev\n");
}

int tong(int a, int b, int c){
    return a + b + c;
}

long long solve(int a, long long b){
    return 2 * a + 3 * b;
}

int main(void){
    greet();
    printf("%d\n", tong(10, 20, 30));
    printf("%lld\n", solve(10, 20));
    return 0;
}
```

Output :

```
codelab.dev
60
80
```

Ví dụ 2 : Chương trình bị lỗi biên dịch khi xây dựng hàm không đúng thứ tự

```c
#include <stdio.h>

void B(void){
    printf("codelab blog\n");
    A();
}

void A(void){
    printf("codelab\n");
}

int main(void){
    B();
    return 0;
}
```

Thông báo của trình biên dịch gcc (biên dịch theo đúng chuẩn với `gcc -std=c11 -pedantic-errors`) :

```
error: implicit declaration of function 'A' [-Wimplicit-function-declaration]
error: conflicting types for 'A'; have 'void(void)'
```

**Giải thích :** 

Ví dụ trong chương trình trên, hàm B() gọi hàm A() thì hàm A() cần xây dựng trước hàm B(). Nếu không thì chương trình sẽ bị lỗi biên dịch, điều tương tự xảy ra khi bạn gọi các hàm trong hàm main thì cần xây dựng các hàm này bên trên hàm main.

Từ chuẩn C99 trở đi, gọi một hàm chưa được khai báo là **không hợp lệ**. C đời cũ (C89) thì cho phép và tự "đoán" hàm đó trả về int, nên đến khi gặp định nghĩa thật `void A(void)` sẽ thấy kiểu không khớp (`conflicting types`). Vì lý do tương thích với code cũ, gcc 11 khi biên dịch mặc định chỉ báo 2 dòng trên dưới dạng **warning**, còn gcc 14 trở đi báo **error**. Dù trình biên dịch của bạn là loại nào, hãy coi cảnh báo `implicit declaration of function` là lỗi và sửa ngay.

Khi sử dụng khai báo nguyên mẫu hàm bạn có thể tùy ý gọi các hàm trong chương trình mà không cần xét đến thứ tự.

Ví dụ 3 :

```c
#include <stdio.h>

//function prototype
void A(void);
void B(void);

void B(void){
    printf("codelab blog\n");
    A();
}

void A(void){
    printf("codelab\n");
}

int main(void){
    B();
    return 0;
}
```

Output :

```
codelab blog
codelab
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-02-c-khai-bao-nguyen-mau-ham.md](solutions/05-02-c-khai-bao-nguyen-mau-ham.md)

**Bài 1.** Viết chương trình có hàm `tong` đặt **sau** `main`, dùng nguyên mẫu để chương trình biên dịch được.

**Bài 2.** Viết chương trình có 5 hàm, khai báo tất cả nguyên mẫu ở đầu file, định nghĩa ở cuối file.

**Bài 3.** Nguyên mẫu hàm có bắt buộc ghi tên tham số không? Thử bỏ tên tham số và biên dịch.

**Bài 4.** Chương trình sau có lỗi gì? Sửa lại:

```c
#include <stdio.h>

int tinhTong(int a, int b);
int main(void){ printf("%d\n", tinhTong(3, 5)); return 0; }
double tinhTong(int a, int b){ return a + b; }
```

**Bài 5.** Chương trình sau có lỗi gì? Sửa lại:

```c
#include <stdio.h>

int f(int x);
int main(void){ printf("%d\n", f(5)); return 0; }
```

**Bài 6.** Viết 2 hàm gọi lẫn nhau: `laChan(n)` gọi `laLe(n-1)` và ngược lại. Giải thích vì sao bắt buộc phải có nguyên mẫu.

**Bài 7.** Tách chương trình bài 6 thành 3 file: `hamso.h` (nguyên mẫu), `hamso.c` (định nghĩa), `main.c`. Biên dịch và chạy.

**Bài 8.** Tìm hiểu "header guard" (`#ifndef / #define / #endif`). Thêm vào file `.h` ở bài 7 và giải thích tác dụng.

**Bài 9.** Nguyên mẫu hàm khác định nghĩa hàm ở điểm nào? Lập bảng so sánh.

**Bài 10.** Viết chương trình có nguyên mẫu `void inBang(int n, char kyTu);` nhưng định nghĩa lại dùng tên tham số khác. Chương trình có chạy được không?

**Bài 11.** Viết thư viện nhỏ gồm 4 hàm toán học (`ucln`, `bcnn`, `laNguyenTo`, `giaiThua`) theo mô hình `.h` + `.c`.

**Bài 12.** Giải thích vì sao khi dùng `#include <stdio.h>` ta gọi được `printf` mà không cần khai báo gì thêm.

**Bài 13.** C không có nạp chồng hàm. Thử khai báo 2 nguyên mẫu cùng tên `dienTich` nhưng khác số tham số, biên dịch và đọc thông báo lỗi. Sau đó sửa thành 3 hàm tên khác nhau (`dienTichVuong`, `dienTichChuNhat`, `dienTichTamGiac`), khai báo đủ 3 nguyên mẫu ở đầu file.

**Bài 14.** Nếu nguyên mẫu ghi `int f(int);` nhưng định nghĩa ghi `int f(long x)` thì chuyện gì xảy ra? Thử và giải thích.

**Bài 15.** Viết chương trình lớn khoảng 100 dòng với ít nhất 6 hàm, tổ chức theo cấu trúc: header comment → `#include` → nguyên mẫu → `main` → định nghĩa hàm.
