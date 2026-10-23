# [C]. Phạm Vi Biến Và Lớp Lưu Trữ

Khi chương trình có nhiều hàm, bạn sẽ gặp những câu hỏi như: biến khai báo trong hàm này có dùng được ở hàm khác không, biến có còn giữ giá trị sau khi hàm kết thúc không. Bài viết này mình sẽ giúp bạn tìm hiểu về **phạm vi của biến** (scope) và **lớp lưu trữ** (storage class) trong C thông qua các ví dụ.

**NỘI DUNG :** 

- **Khối Lệnh Và Phạm Vi Của Biến**
- **Biến Cục Bộ Và Biến Toàn Cục**
- **Lớp Lưu Trữ auto Và register**
- **Biến static**
- **Từ Khóa extern**
- **Video Tutorial**

---

**1. Khối Lệnh Và Phạm Vi Của Biến**

**Khối lệnh** (block) là các câu lệnh được đặt trong cặp ngoặc nhọn `{ }`. Thân hàm, thân của if, for, while... đều là các khối lệnh.

**Phạm vi** (scope) của một biến là vùng code mà bạn có thể sử dụng tên biến đó. Biến khai báo bên trong một khối lệnh chỉ có phạm vi từ vị trí khai báo tới dấu `}` đóng khối lệnh đó.

Ví dụ 1 :

```c
#include <stdio.h>

int main(void){
    int a = 10;
    {
        int b = 20;
        printf("Trong khoi : a = %d, b = %d\n", a, b);
    }
    printf("Ngoai khoi : a = %d\n", a);
    // printf("%d\n", b); // LOI : b khong ton tai o day
    return 0;
}
```

Output :

```
Trong khoi : a = 10, b = 20
Ngoai khoi : a = 10
```

**Giải thích :** 

- Biến a khai báo trong thân hàm main nên dùng được ở mọi chỗ bên dưới nó trong main, kể cả trong khối lệnh con
- Biến b khai báo trong khối lệnh con nên chỉ tồn tại bên trong khối lệnh đó, nếu bỏ comment dòng in ra b thì chương trình sẽ bị lỗi biên dịch `'b' undeclared`

Biến khai báo trong phần khởi tạo của vòng lặp for cũng chỉ có phạm vi trong vòng lặp :

```c
#include <stdio.h>

int main(void){
    for(int i = 1; i <= 3; i++){
        printf("%d ", i);
    }
    // printf("%d\n", i); // LOI : i chi ton tai trong vong for
    printf("\n");
    return 0;
}
```

Output :

```
1 2 3 
```

**Chú ý :** Nếu cần dùng giá trị của i sau vòng lặp, bạn phải khai báo i bên ngoài vòng for.

**Che khuất tên biến** (shadowing) : Khi khối lệnh con khai báo một biến trùng tên với biến ở khối lệnh cha, bên trong khối lệnh con tên đó sẽ chỉ biến mới, biến ở khối cha tạm thời bị che khuất.

Ví dụ 2 :

```c
#include <stdio.h>

int main(void){
    int x = 1;
    {
        int x = 2; // bien x moi, che khuat x ben ngoai
        x += 10;
        printf("x trong khoi = %d\n", x);
    }
    printf("x ngoai khoi = %d\n", x);
    return 0;
}
```

Output :

```
x trong khoi = 12
x ngoai khoi = 1
```

Bạn nên tránh đặt tên trùng như vậy vì code rất dễ gây nhầm lẫn.

---

**2. Biến Cục Bộ Và Biến Toàn Cục**

**Biến cục bộ** (local variable) là biến được khai báo bên trong một hàm hoặc một khối lệnh. Tham số của hàm cũng là biến cục bộ của hàm đó.

- Biến cục bộ chỉ dùng được trong hàm (khối lệnh) khai báo nó
- Biến cục bộ được tạo ra khi hàm bắt đầu chạy và bị hủy khi hàm kết thúc, mỗi lần gọi hàm là một biến mới
- Hai hàm khác nhau có thể có biến cục bộ trùng tên, chúng là 2 biến hoàn toàn độc lập
- Biến cục bộ **không được khởi tạo** sẽ chứa **giá trị rác**

**Biến toàn cục** (global variable) là biến được khai báo bên ngoài mọi hàm, thường ở đầu file.

- Biến toàn cục dùng được ở mọi hàm nằm bên dưới vị trí khai báo nó
- Biến toàn cục tồn tại suốt thời gian chạy chương trình
- Biến toàn cục không được khởi tạo sẽ tự động có giá trị **0**

Ví dụ :

```c
#include <stdio.h>

int dem = 0; // bien toan cuc

void tang(void){
    int k = 5; // bien cuc bo cua ham tang
    dem++;
    printf("tang : dem = %d, k = %d\n", dem, k);
}

int main(void){
    int k = 100; // bien cuc bo cua main, khong lien quan toi k trong ham tang
    tang();
    tang();
    printf("main : dem = %d, k = %d\n", dem, k);
    return 0;
}
```

Output :

```
tang : dem = 1, k = 5
tang : dem = 2, k = 5
main : dem = 2, k = 100
```

**Giải thích :** 

- Biến dem là biến toàn cục nên cả hàm tang và hàm main đều dùng chung 1 biến dem, mỗi lần gọi tang() thì dem tăng thêm 1
- Biến k trong hàm tang và biến k trong main là 2 biến cục bộ khác nhau, thay đổi biến này không ảnh hưởng tới biến kia

**Chú ý :** 

- Nếu biến cục bộ trùng tên với biến toàn cục thì bên trong hàm đó tên biến sẽ chỉ biến cục bộ (biến toàn cục bị che khuất)
- Biến toàn cục tiện lợi nhưng mọi hàm đều có thể thay đổi nó, khi chương trình lớn sẽ rất khó biết hàm nào đã làm thay đổi giá trị. Bạn nên ưu tiên truyền dữ liệu qua tham số và giá trị trả về, chỉ dùng biến toàn cục khi thật sự cần (ví dụ mảng rất lớn, hằng số dùng chung)

---

**3. Lớp Lưu Trữ auto Và register**

**Lớp lưu trữ** (storage class) quyết định biến được lưu ở đâu, tồn tại trong bao lâu và phạm vi liên kết của nó. C có các từ khóa lớp lưu trữ : `auto`, `register`, `static`, `extern`.

**auto** : Là lớp lưu trữ mặc định của mọi biến cục bộ. Hai khai báo sau là hoàn toàn giống nhau, vì thế trong thực tế gần như không ai viết từ khóa auto.

```c
int x = 10;
auto int y = 10; // giong het int y = 10;
```

**Chú ý :** Trong C, `auto` chỉ là lớp lưu trữ, **không** có nghĩa là tự suy luận kiểu dữ liệu. Viết `auto x = 10;` mà không có kiểu dữ liệu là cách viết không hợp lệ trong C11.

**register** : Gợi ý cho trình biên dịch lưu biến trong thanh ghi của CPU để truy cập nhanh hơn. Trình biên dịch có quyền bỏ qua gợi ý này, và các trình biên dịch hiện đại tự tối ưu tốt hơn nên từ khóa này hiếm khi được dùng. Điểm cần nhớ là bạn **không thể lấy địa chỉ** của biến register.

```c
register int i = 0;
// int *p = &i; // LOI : address of register variable requested
```

---

**4. Biến static**

**Biến static cục bộ** là biến khai báo trong hàm với từ khóa `static`. Nó có phạm vi như biến cục bộ (chỉ dùng được trong hàm đó) nhưng lại **tồn tại suốt chương trình** như biến toàn cục.

- Biến static chỉ được khởi tạo **một lần duy nhất**, trước khi chương trình chạy
- Khi hàm kết thúc, biến static không bị hủy mà **giữ nguyên giá trị** cho lần gọi hàm tiếp theo
- Biến static không được khởi tạo sẽ tự động có giá trị 0
- Giá trị khởi tạo của biến static phải là hằng số, ví dụ `static int x = 5;` hợp lệ còn `static int x = n;` (n là biến) sẽ bị lỗi biên dịch

Ví dụ : So sánh biến cục bộ thường và biến static

```c
#include <stdio.h>

void thuong(void){
    int dem = 0;
    dem++;
    printf("%d ", dem);
}

void tinh(void){
    static int dem = 0; // chi khoi tao 1 lan
    dem++;
    printf("%d ", dem);
}

int main(void){
    for(int i = 0; i < 3; i++){
        thuong();
    }
    printf("\n");
    for(int i = 0; i < 3; i++){
        tinh();
    }
    printf("\n");
    return 0;
}
```

Output :

```
1 1 1 
1 2 3 
```

**Giải thích :** 

- Trong hàm thuong, mỗi lần gọi hàm thì biến dem được tạo mới và gán lại bằng 0, tăng lên 1 rồi bị hủy khi hàm kết thúc, vì thế lần nào cũng in ra 1
- Trong hàm tinh, biến static dem chỉ được khởi tạo bằng 0 một lần, lần gọi thứ nhất tăng lên 1, lần gọi thứ hai tiếp tục từ 1 tăng lên 2, lần thứ ba tăng lên 3

**Biến và hàm static toàn cục** : Khi đặt `static` trước biến toàn cục hoặc trước một hàm, biến (hàm) đó chỉ dùng được trong **file hiện tại**, các file khác trong cùng chương trình không thể truy cập tới. Cách này giúp "giấu" những biến, hàm chỉ dùng nội bộ khi chương trình được chia thành nhiều file.

```c
static int soLanGoi = 0;        // chi dung duoc trong file nay
static void hamNoiBo(void){ }   // chi goi duoc trong file nay
```

---

**5. Từ Khóa extern**

Khi chương trình được chia thành nhiều file `.c`, từ khóa `extern` dùng để **khai báo** rằng một biến toàn cục đã được **định nghĩa ở file khác**. Khai báo extern không tạo ra biến mới, nó giống như nguyên mẫu hàm nhưng dành cho biến.

File `dem.c` :

```c
int tongSo = 0; // DINH NGHIA bien toan cuc (cap phat bo nho)

void cong(int x){
    tongSo += x;
}
```

File `main.c` :

```c
#include <stdio.h>

extern int tongSo; // KHAI BAO : tongSo nam o file khac
void cong(int x);  // nguyen mau ham nam o file khac

int main(void){
    cong(10);
    cong(18);
    printf("tongSo = %d\n", tongSo);
    return 0;
}
```

Biên dịch cả 2 file :

```
gcc -std=c11 main.c dem.c -o main
```

Output :

```
tongSo = 28
```

**Giải thích :** 

- Biến tongSo được định nghĩa một lần duy nhất trong dem.c
- Trong main.c, dòng `extern int tongSo;` báo cho trình biên dịch biết tongSo là biến int nằm ở file khác, đến bước liên kết thì main.c và dem.c dùng chung đúng một biến tongSo
- Nếu trong dem.c khai báo `static int tongSo = 0;` thì main.c không thể dùng được và chương trình bị lỗi liên kết `undefined reference to 'tongSo'`

**Tổng kết :**

| Loại biến | Phạm vi | Thời gian tồn tại | Giá trị mặc định |
|---|---|---|---|
| Cục bộ (auto) | Trong khối lệnh khai báo nó | Từ lúc khai báo tới hết khối lệnh | Giá trị rác |
| Cục bộ static | Trong khối lệnh khai báo nó | Suốt chương trình | 0 |
| Toàn cục | Toàn bộ file (và file khác qua extern) | Suốt chương trình | 0 |
| Toàn cục static | Chỉ trong file khai báo nó | Suốt chương trình | 0 |

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-04-c-pham-vi-bien-va-lop-luu-tru.md](solutions/05-04-c-pham-vi-bien-va-lop-luu-tru.md)

**Bài 1.** Chương trình sau in ra gì? Giải thích:

```c
#include <stdio.h>

int main(void){
    int a = 1;
    {
        int a = 2;
        {
            a = 3;
            int a = 4;
            printf("%d ", a);
        }
        printf("%d ", a);
    }
    printf("%d\n", a);
    return 0;
}
```

**Bài 2.** Chương trình sau có lỗi gì? Sửa lại để in ra số nguyên dương nhỏ nhất có bình phương lớn hơn 1000:

```c
#include <stdio.h>

int main(void){
    for(int i = 1; i * i <= 1000; i++){ }
    printf("%d\n", i);
    return 0;
}
```

**Bài 3.** Viết hàm `void goiHam(void)` mỗi lần được gọi in ra `Ham duoc goi lan thu k`, dùng biến `static`.

**Bài 4.** Viết lại bài 3 nhưng bỏ từ khóa `static`. Chương trình in ra gì? Giải thích vì sao.

**Bài 5.** Dùng một biến toàn cục `long long soDu` và 2 hàm `void napTien(long long x)`, `int rutTien(long long x)` (trả về 0 nếu không đủ tiền). Viết `main` thử nạp, rút vài lần và in số dư.

**Bài 6.** In ra giá trị của một biến toàn cục `int`, một biến `static int` cục bộ và một mảng toàn cục `int a[5]` khi không khởi tạo. Giải thích vì sao **không nên** in thử biến cục bộ thường chưa khởi tạo.

**Bài 7.** Chương trình sau in ra gì? Giải thích:

```c
#include <stdio.h>

int x = 10;

void f(void){
    int x = 20;
    x++;
    printf("%d ", x);
}

void g(void){
    x++;
    printf("%d ", x);
}

int main(void){
    f(); g(); f(); g();
    printf("%d\n", x);
    return 0;
}
```

**Bài 8.** Viết hàm `int sinhMa(void)` mỗi lần gọi trả về một mã mới tăng dần bắt đầu từ 1. Dùng nó để in ra mã sinh viên dạng `SV001`, `SV002`, ... cho 5 sinh viên.

**Bài 9.** Viết hàm `long long fiboTiepTheo(void)` mỗi lần gọi trả về số Fibonacci tiếp theo (0, 1, 1, 2, 3, 5, ...), chỉ dùng biến `static` bên trong hàm. In ra 15 số Fibonacci đầu tiên.

**Bài 10.** Chia chương trình thành 2 file `bodem.c` và `main.c`: biến toàn cục `int soLuong` định nghĩa trong `bodem.c` cùng hàm `void them(void)`; `main.c` dùng `extern` để đọc `soLuong`. Biên dịch và chạy.

**Bài 11.** Ở bài 10, đổi khai báo trong `bodem.c` thành `static int soLuong = 0;`. Biên dịch lại, đọc thông báo lỗi và giải thích. Làm thế nào để `main.c` vẫn biết được giá trị `soLuong` mà không bỏ `static`?

**Bài 12.** Khai báo `register int r = 5;` rồi thử in địa chỉ của `r` bằng `printf("%p", (void *)&r)`. Chuyện gì xảy ra? Giải thích.

**Bài 13.** Chương trình sau có lỗi gì? Sửa lại:

```c
#include <stdio.h>

void f(int n){
    static int tong = n;
    tong += n;
    printf("%d\n", tong);
}

int main(void){
    f(1); f(2); f(3);
    return 0;
}
```

**Bài 14.** Viết hàm `double themSo(double x)` trả về trung bình cộng của **tất cả** các số đã được truyền vào hàm từ trước tới giờ (dùng biến `static`). Nhập liên tục các số cho tới khi nhập 0 và in trung bình sau mỗi lần nhập.

**Bài 15.** Viết chương trình minh họa đủ 4 loại biến: cục bộ thường, cục bộ `static`, toàn cục, toàn cục `static`. Lập bảng so sánh về phạm vi, thời gian tồn tại, giá trị mặc định và nêu khi nào nên dùng loại nào.
