# [C]. Truyền Tham Trị Và Truyền Con Trỏ

Khi gọi hàm trong C, giá trị của đối số luôn được **sao chép** vào tham số. Vậy làm sao để một hàm có thể thay đổi giá trị của biến nằm bên ngoài nó, ví dụ hàm hoán đổi 2 biến? Câu trả lời là truyền cho hàm **địa chỉ** của biến thông qua con trỏ. Bài viết này mình sẽ giúp bạn phân biệt 2 cách truyền đối số trong C thông qua các ví dụ.

**NỘI DUNG :** 

- **Truyền Tham Trị**
- **Toán Tử & Và ***
- **Truyền Con Trỏ**
- **Trả Về Nhiều Giá Trị Qua Con Trỏ**
- **Video Tutorial** 

---

**1. Truyền Tham Trị** 

**Truyền tham trị** - Pass by value là hình thức xây dựng tham số phổ biến cho hàm, như trong bài học trước về hàm thì mình đã chú ý về việc giá trị của đối số sẽ được gán cho tham số khi lời gọi hàm được thực hiện.

Xem xét ví dụ sau bạn sẽ hiểu rõ hơn về tham số và đối số, từ đó sẽ nắm được logic khi gọi hàm với cách truyền tham trị

Ở đây mình dùng toán tử địa chỉ (&) để in ra địa chỉ của biến trong bộ nhớ máy tính, địa chỉ được in bằng đặc tả `%p` và thường hiển thị dưới dạng số hexa. Khi in bằng `%p` cần ép địa chỉ về kiểu `(void *)`.

**Mã nguồn :** 

```c
#include <stdio.h>

void thaydoi(int n){
    printf("Dia chi cua n trong bo nho may tinh : %p\n", (void *)&n);
    n += 100;
    printf("Gia tri cua n trong ham thay doi : %d\n", n);
}

int main(void){
    int m = 1000;
    printf("Dia chi cua m trong bo nho may tinh : %p\n", (void *)&m);
    thaydoi(m);
    printf("Gia tri cua m sau khi ham ket thuc : %d\n", m);
    return 0;
}
```

Output (địa chỉ sẽ khác nhau trên mỗi máy và mỗi lần chạy) :

```
Dia chi cua m trong bo nho may tinh : 0x7ffc8a3e1d4c
Dia chi cua n trong bo nho may tinh : 0x7ffc8a3e1d2c
Gia tri cua n trong ham thay doi : 1100
Gia tri cua m sau khi ham ket thuc : 1000
```

**Giải thích :** 

- n là tham số và m là đối số, giá trị của đối số m được gán cho n khi bạn gọi hàm thaydoi(m). Ở đây giá trị của m là 1000 sẽ được gán cho n và vì thế n cũng bằng 1000
- Địa chỉ của m trong máy tính là 0x7ffc8a3e1d4c, trong khi đó địa chỉ của n trong hàm thaydoi là 0x7ffc8a3e1d2c điều này chứng tỏ n và m là 2 biến khác nhau, không cùng quản lý 1 ô nhớ trong máy tính
- Trong hàm thaydoi giá trị của n được tăng lên 100, khi đó n thành 1100 và ô nhớ 0x7ffc8a3e1d2c (n đang quản lý) sẽ có giá trị là 1100
- Sau khi hàm thaydoi kết thúc thì giá trị của m vẫn sẽ là 1000, ô nhớ 0x7ffc8a3e1d4c không hề bị can thiệp gì khi hàm thay đổi thực thi

**Kết luận** : Khi hàm có tham số là tham trị thì đối số bạn truyền vào hàm và tham số của hàm là 2 biến khác nhau và việc bạn thay đổi tham số sẽ không ảnh hưởng gì tới đố số.

**Chú ý :** Trong C **mọi đối số đều được truyền theo tham trị**. C **không có** kiểu tham chiếu `int &n` (cú pháp này không hợp lệ trong C). Muốn hàm thay đổi được biến bên ngoài, bạn phải truyền **địa chỉ** của biến đó cho hàm, tức là truyền con trỏ.

---

**2. Toán Tử & Và ***

Để hiểu cách truyền con trỏ, bạn chỉ cần nắm 2 toán tử sau (kiến thức đầy đủ về con trỏ sẽ được học ở [chương con trỏ](07-01-c-ly-thuyet-con-tro.md)) :

- **Toán tử lấy địa chỉ `&`** : `&x` cho ra địa chỉ của biến x trong bộ nhớ. Bạn đã gặp nó khi dùng `scanf("%d", &x)`
- **Con trỏ** : là biến dùng để lưu địa chỉ. Khai báo `int *p;` nghĩa là p là con trỏ, lưu địa chỉ của một biến kiểu int
- **Toán tử giải tham chiếu `*`** : nếu p đang lưu địa chỉ của x thì `*p` chính là ô nhớ của x, đọc `*p` là đọc giá trị của x, gán `*p = ...` là gán giá trị cho x

Ví dụ :

```c
#include <stdio.h>

int main(void){
    int x = 10;
    int *p = &x;       // p luu dia chi cua x

    printf("x = %d\n", x);
    printf("*p = %d\n", *p);   // doc gia tri tai dia chi p dang giu

    *p = 28;           // gan gia tri 28 vao o nho cua x
    printf("x = %d\n", x);
    return 0;
}
```

Output :

```
x = 10
*p = 10
x = 28
```

**Giải thích :** 

- `p = &x` nên p giữ địa chỉ của x, ta nói "p trỏ tới x"
- `*p` truy cập đúng ô nhớ của x, vì thế khi gán `*p = 28` thì x cũng thành 28 dù ta không hề viết `x = 28`

**Chú ý :** Dấu `*` có 2 vai trò khác nhau. Trong **khai báo** `int *p` nó cho biết p là con trỏ, còn trong **biểu thức** `*p` nó là phép truy cập giá trị tại địa chỉ p đang giữ.

---

**3. Truyền Con Trỏ**

**Truyền con trỏ** - Pass by pointer (còn gọi là truyền địa chỉ) là cách thức xây dựng hàm với tham số là một con trỏ. Khi gọi hàm bạn truyền vào **địa chỉ** của biến bằng toán tử `&`.

Bản chất đây vẫn là truyền tham trị, chỉ có điều giá trị được sao chép lúc này là **địa chỉ** của biến. Có địa chỉ trong tay, hàm dùng toán tử `*` để truy cập trực tiếp vào ô nhớ của đối số và thay đổi giá trị tại ô nhớ đó, dẫn đến giá trị của đối số sẽ bị thay đổi theo.

Xem xét ví dụ sau đây bạn sẽ hiểu rõ hơn về truyền con trỏ trong C

**Mã nguồn :** 

```c
#include <stdio.h>

void thaydoi(int *n){
    printf("Gia tri con tro n (dia chi no giu) : %p\n", (void *)n);
    *n += 100;
}

int main(void){
    int m = 1000;
    printf("Dia chi cua m trong bo nho may tinh : %p\n", (void *)&m);
    thaydoi(&m);
    printf("Gia tri cua m sau khi ham ket thuc : %d\n", m);
    return 0;
}
```

Output :

```
Dia chi cua m trong bo nho may tinh : 0x7ffc8a3e1d4c
Gia tri con tro n (dia chi no giu) : 0x7ffc8a3e1d4c
Gia tri cua m sau khi ham ket thuc : 1100
```

**Giải thích :** 

- Lời gọi `thaydoi(&m)` truyền địa chỉ của m (0x7ffc8a3e1d4c) cho tham số con trỏ n, vì thế n đang trỏ tới ô nhớ của m
- `*n += 100` là tăng giá trị tại ô nhớ 0x7ffc8a3e1d4c, ban đầu ô nhớ này có giá trị 1000, sau đó lưu trữ giá trị 1100
- Ô nhớ 0x7ffc8a3e1d4c cũng chính là ô nhớ mà m đang quản lý, vì thế sau khi hàm kết thúc m có giá trị là 1100

**Chú ý :** 

- Khi gọi hàm phải truyền **địa chỉ** `thaydoi(&m)`, nếu viết `thaydoi(m)` thì trình biên dịch sẽ cảnh báo truyền số nguyên vào chỗ cần con trỏ và chương trình có thể bị crash khi chạy
- Bên trong hàm phải dùng `*n` để truy cập giá trị. Nếu viết `n += 100` thì bạn đang thay đổi địa chỉ mà con trỏ n giữ chứ không phải giá trị của m
- Bạn không thể truyền hằng số cho tham số con trỏ, ví dụ không thể gọi `thaydoi(&1000)` vì hằng số 1000 không có địa chỉ, bạn phải truyền địa chỉ của một biến
- Đây chính là lý do `scanf("%d", &x)` cần dấu `&` : scanf cần địa chỉ của x để ghi giá trị nhập vào ô nhớ của x

Ví dụ về việc hoán đổi giá trị của 2 biến thông qua hàm bằng tham trị và con trỏ :

```c
#include <stdio.h>

void swap1(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
}

void swap2(int *a, int *b){
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int main(void){
    int x = 100, y = 200;
    swap1(x, y);
    printf("%d %d\n", x, y);
    swap2(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```

Output :

```
100 200
200 100
```

**Giải thích :** 

- swap1 hoán đổi 2 bản sao a và b, khi hàm kết thúc 2 bản sao bị huỷ nên x, y không đổi
- swap2 nhận địa chỉ của x và y, việc hoán đổi `*a` và `*b` chính là hoán đổi giá trị trong ô nhớ của x và y

---

**4. Trả Về Nhiều Giá Trị Qua Con Trỏ**

Câu lệnh return chỉ trả về được **một** giá trị. Khi muốn hàm cho ra nhiều kết quả, bạn truyền thêm các tham số con trỏ để hàm ghi kết quả vào đó. Các tham số này thường được gọi là **tham số đầu ra** (output parameter).

Ví dụ : Hàm tính cả tổng và hiệu của 2 số

```c
#include <stdio.h>

void tongHieu(int a, int b, int *tong, int *hieu){
    *tong = a + b;
    *hieu = a - b;
}

int main(void){
    int t, h;
    tongHieu(28, 10, &t, &h);
    printf("Tong = %d\n", t);
    printf("Hieu = %d\n", h);
    return 0;
}
```

Output :

```
Tong = 38
Hieu = 18
```

**Giải thích :** 

- a, b là tham số đầu vào nên truyền theo tham trị như bình thường
- tong, hieu là tham số đầu ra, hàm nhận địa chỉ của t và h rồi ghi kết quả vào đó, vì thế sau lời gọi hàm t = 38 và h = 18

Bạn có thể kết hợp return với tham số đầu ra, ví dụ return một giá trị báo thành công hay thất bại và trả kết quả tính toán qua con trỏ :

```c
#include <stdio.h>

int chia(int a, int b, int *thuong, int *du){
    if(b == 0){
        return 0; // that bai, khong chia duoc
    }
    *thuong = a / b;
    *du = a % b;
    return 1; // thanh cong
}

int main(void){
    int q, r;
    if(chia(17, 5, &q, &r)){
        printf("17 = 5 * %d + %d\n", q, r);
    }
    if(!chia(17, 0, &q, &r)){
        printf("Khong the chia cho 0\n");
    }
    return 0;
}
```

Output :

```
17 = 5 * 3 + 2
Khong the chia cho 0
```

**Kết luận :** Khi bạn cần xây dựng hàm và muốn những thay đổi trong hàm sẽ được giữ nguyên với đối số sau khi hàm kết thúc, hoặc cần hàm trả về nhiều giá trị, thì sử dụng tham số con trỏ và truyền địa chỉ của biến khi gọi hàm. Kiến thức chi tiết về con trỏ bạn sẽ được học ở [chương con trỏ](07-01-c-ly-thuyet-con-tro.md).

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-03-c-truyen-tham-tri-va-truyen-con-tro.md](solutions/05-03-c-truyen-tham-tri-va-truyen-con-tro.md)

**Bài 1.** Viết hàm `void tangGapDoi(int x)` (tham trị) và `void tangGapDoi2(int *x)` (con trỏ). Gọi cả hai và so sánh kết quả.

**Bài 2.** Viết hàm `void hoanDoi(int *a, int *b)` hoán đổi 2 số. Chứng minh nó hoạt động.

**Bài 3.** Viết lại hàm `hoanDoi` dùng tham trị và giải thích vì sao nó **không** hoạt động.

**Bài 4.** Viết hàm `void tinhTongHieu(int a, int b, int *tong, int *hieu)` trả về 2 kết quả qua con trỏ.

**Bài 5.** Viết hàm `void nhapMang(int a[], int *n)` nhập mảng và cả số phần tử.

**Bài 6.** Viết hàm `void timMinMax(int a[], int n, int *mn, int *mx)` tìm cả min và max trong một lần duyệt.

**Bài 7.** Chương trình sau in ra gì? Giải thích:

```c
#include <stdio.h>

void f(int x, int *y) { x += 10; *y += 10; }
int main(void){
    int a = 1, b = 1;
    f(a, &b);
    printf("%d %d\n", a, b);
    return 0;
}
```

**Bài 8.** Vì sao `scanf("%d", &x)` cần dấu `&` còn `printf("%d", x)` thì không? Viết hàm `void nhapSoDuong(int *p)` nhập lại cho tới khi người dùng nhập một số dương, kết quả ghi vào biến của `main`.

**Bài 9.** Viết hàm `int giaiPTBac2(double a, double b, double c, double *x1, double *x2)` trả về số nghiệm của phương trình `ax² + bx + c = 0` (a khác 0) và ghi các nghiệm vào `*x1`, `*x2`.

**Bài 10.** Mảng được truyền vào hàm theo kiểu sao chép toàn bộ hay truyền địa chỉ? Viết chương trình chứng minh.

**Bài 11.** Viết hàm `void tachGioPhutGiay(int tongGiay, int *gio, int *phut, int *giay)` đổi tổng số giây ra giờ, phút, giây.

**Bài 12.** Chương trình sau có lỗi nguy hiểm gì? Giải thích:

```c
int *taoSo(void) {
    int x = 10;
    return &x;
}
```

**Bài 13.** Viết hàm `void demChanLe(int a[], int n, int *chan, int *le)` đếm số lượng phần tử chẵn và lẻ.

**Bài 14.** Chương trình sau có 2 lỗi khiến nó không hoán đổi được 2 số. Tìm và sửa:

```c
#include <stdio.h>

void hoanDoi(int *a, int *b){
    int *tmp = a;
    a = b;
    b = tmp;
}
int main(void){
    int x = 1, y = 2;
    hoanDoi(x, y);
    printf("%d %d\n", x, y);
    return 0;
}
```

**Bài 15.** Viết hàm `void sapXep3(int *a, int *b, int *c)` sắp xếp 3 biến theo thứ tự tăng dần bằng cách gọi lại hàm `hoanDoi` ở bài 2.
