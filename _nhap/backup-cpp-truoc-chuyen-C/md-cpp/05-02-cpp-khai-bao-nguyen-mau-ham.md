# [C++]. Khai Báo Nguyên Mẫu Hàm

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

Ví dụ 1 :

```cpp
#include "iostream"

using namespace std;

//function prototype
void greet();
int tong(int, int, int);
long long solve(int, long long);

void greet(){
    cout << "codelab.dev\n";
}

int tong(int a, int b, int c){
    return a + b + c;
}

long long solve(int a, long long b){
    return 2 * a + 3 * b;
}

int main(){
    greet();
    cout << tong(10, 20, 30) << endl;
    cout << solve(10, 20);
    return 0;
}
```

Output :

```cpp
codelab.dev
60
80
```

Ví dụ 2 : Chương trình bị lỗi biên dịch khi xây dựng hàm không đúng thứ tự

```cpp
#include "iostream"

using namespace std;

void B(){
    cout << "codelab blog\n";
    A();
}

void A(){
    cout << "codelab\n";
}

int main(){
    B();
    return 0;
}
```

**Giải thích :** 

Ví dụ trong chương trình dưới trên, hàm B() gọi hàm A() thì hàm A() cần xây dựng trước hàm B(). Nếu không thì chương trình sẽ bị lỗi biên dịch, điều tương tự xảy ra khi bạn gọi các hàm trong hàm main thì cần xây dựng các hàm này bên trên hàm main.

Khi sử dụng khai báo nguyên mẫu hàm bạn có thể tùy ý gọi các hàm trong chương trình mà không cần xét đến thứ tự.

Ví dụ 3 :

```cpp
#include "iostream"

using namespace std;

//function prototype
void A();
void B();

void B(){
    cout << "codelab blog\n";
    A();
}

void A(){
    cout << "codelab\n";
}

int main(){
    B();
    return 0;
}
```

Output :

```cpp
codelab blog
codelab
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-02-cpp-khai-bao-nguyen-mau-ham.md](solutions/05-02-cpp-khai-bao-nguyen-mau-ham.md)

**Bài 1.** Viết chương trình có hàm `tong` đặt **sau** `main`, dùng nguyên mẫu để chương trình biên dịch được.

**Bài 2.** Viết chương trình có 5 hàm, khai báo tất cả nguyên mẫu ở đầu file, định nghĩa ở cuối file.

**Bài 3.** Nguyên mẫu hàm có bắt buộc ghi tên tham số không? Thử bỏ tên tham số và biên dịch.

**Bài 4.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
int tinhTong(int a, int b);
int main(){ cout << tinhTong(3, 5); return 0; }
double tinhTong(int a, int b){ return a + b; }
```

**Bài 5.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
int f(int x);
int main(){ cout << f(5); return 0; }
```

**Bài 6.** Viết 2 hàm gọi lẫn nhau: `laChan(n)` gọi `laLe(n-1)` và ngược lại. Giải thích vì sao bắt buộc phải có nguyên mẫu.

**Bài 7.** Tách chương trình bài 6 thành 3 file: `hamso.h` (nguyên mẫu), `hamso.cpp` (định nghĩa), `main.cpp`. Biên dịch và chạy.

**Bài 8.** Tìm hiểu "header guard" (`#ifndef / #define / #endif`). Thêm vào file `.h` ở bài 7 và giải thích tác dụng.

**Bài 9.** Nguyên mẫu hàm khác định nghĩa hàm ở điểm nào? Lập bảng so sánh.

**Bài 10.** Viết chương trình có nguyên mẫu `void inBang(int n, char kyTu);` nhưng định nghĩa lại dùng tên tham số khác. Chương trình có chạy được không?

**Bài 11.** Viết thư viện nhỏ gồm 4 hàm toán học (`ucln`, `bcnn`, `laNguyenTo`, `giaiThua`) theo mô hình `.h` + `.cpp`.

**Bài 12.** Giải thích vì sao khi dùng `#include <iostream>` ta gọi được `cout` mà không cần khai báo gì thêm.

**Bài 13.** Viết chương trình có 3 hàm nạp chồng cùng tên, khai báo đủ 3 nguyên mẫu ở đầu file.

**Bài 14.** Nếu nguyên mẫu ghi `int f(int);` nhưng định nghĩa ghi `int f(long);` thì chuyện gì xảy ra? Thử và giải thích.

**Bài 15.** Viết chương trình lớn khoảng 100 dòng với ít nhất 6 hàm, tổ chức theo cấu trúc: header comment → `#include` → nguyên mẫu → `main` → định nghĩa hàm.
