# [C]. Truyền Mảng Vào Hàm

Khi chương trình lớn dần, các thao tác như nhập mảng, in mảng, tính tổng, tìm max... nên được tách thành hàm riêng để dễ đọc và dùng lại. Tuy nhiên truyền mảng vào hàm trong C có một số điểm **rất khác** so với truyền một biến `int` thông thường. Trong bài này mình sẽ hướng dẫn các bạn cách truyền mảng vào hàm và những cái bẫy hay gặp.

**NỘI DUNG :** 

- **Cú Pháp Truyền Mảng Vào Hàm**
- **Mảng Suy Biến Thành Con Trỏ**
- **Bẫy sizeof Bên Trong Hàm**
- **Tham Số const int a[]**
- **Hàm Nhập Và Xuất Mảng**

---

**1. Cú Pháp Truyền Mảng Vào Hàm**

Trong C, khi truyền mảng vào hàm bạn luôn cần truyền thêm **số lượng phần tử** của mảng, vì hàm không có cách nào tự biết mảng dài bao nhiêu (lý do sẽ được giải thích ở mục 3).

**Cú pháp :** 

```c
kieu_tra_ve ten_ham(kieu_du_lieu ten_mang[], int n){
    //code
}
```

Khi gọi hàm, bạn chỉ ghi **tên mảng**, không kèm dấu `[]`:

```c
ten_ham(a, n);
```

**Ví dụ 1** : Hàm tính tổng các phần tử trong mảng

```c
#include <stdio.h>

int tong(int a[], int n){
    int s = 0;
    for(int i = 0; i < n; i++){
        s += a[i];
    }
    return s;
}

int main(){
    int a[5] = {10, 20, 30, 40, 50};
    int b[3] = {1, 2, 3};
    printf("Tong mang a : %d\n", tong(a, 5));
    printf("Tong mang b : %d\n", tong(b, 3));
    return 0;
}
```

Output :

```
Tong mang a : 150
Tong mang b : 6
```

**Giải thích :** 

Cùng một hàm `tong` dùng được cho mọi mảng `int` có độ dài bất kỳ, chỉ cần truyền đúng số lượng phần tử `n`.

**Chú ý** : 3 cách khai báo tham số sau là **hoàn toàn tương đương** trong C:

```c
int tong(int a[], int n);
int tong(int a[100], int n);   // so 100 bi trinh bien dich BO QUA
int tong(int *a, int n);       // viet duoi dang con tro
```

Con số ghi trong `[]` của tham số không có tác dụng gì, hàm vẫn nhận được mảng có độ dài bất kỳ. Vì vậy cách viết `int a[]` kèm tham số `n` là rõ ràng nhất.

---

**2. Mảng Suy Biến Thành Con Trỏ**

Ở bài [Truyền Tham Trị Và Truyền Con Trỏ](05-03-c-truyen-tham-tri-va-truyen-con-tro.md) các bạn đã biết: khi truyền một biến `int` vào hàm, hàm nhận một **bản sao**, thay đổi bản sao không ảnh hưởng tới biến gốc.

Với mảng thì khác. Khi truyền mảng vào hàm, C **không sao chép** toàn bộ mảng mà chỉ truyền **địa chỉ của phần tử đầu tiên**. Hiện tượng này gọi là **mảng suy biến thành con trỏ** (array decay). Hệ quả là hàm thao tác **trực tiếp** trên mảng gốc.

**Ví dụ 2** : So sánh truyền biến và truyền mảng

```c
#include <stdio.h>

void doiBien(int x){
    x = 100;
    printf("x trong ham : %d\n", x);
}

void doiMang(int a[], int n){
    for(int i = 0; i < n; i++){
        a[i] = a[i] * 2;
    }
}

int main(){
    int x = 5;
    int a[4] = {1, 2, 3, 4};
    doiBien(x);
    doiMang(a, 4);
    printf("x sau khi goi ham : %d\n", x);
    printf("Mang a sau khi goi ham : ");
    for(int i = 0; i < 4; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}
```

Output :

```
x trong ham : 100
x sau khi goi ham : 5
Mang a sau khi goi ham : 2 4 6 8 
```

**Giải thích :** 

- Biến `x` được truyền theo tham trị: hàm `doiBien` sửa bản sao (bên trong hàm `x` là 100) nhưng `x` ở `main` vẫn là 5.
- Mảng `a` được truyền dưới dạng địa chỉ: hàm `doiMang` sửa thẳng vào vùng nhớ của mảng `a` trong `main`, nên các phần tử đều bị nhân đôi.

Bạn có thể kiểm chứng bằng cách in địa chỉ của mảng ở cả hai nơi:

```c
#include <stdio.h>

void inDiaChi(int a[]){
    printf("Dia chi trong ham : %p\n", (void *)a);
}

int main(){
    int a[4] = {1, 2, 3, 4};
    printf("Dia chi trong main: %p\n", (void *)a);
    inDiaChi(a);
    return 0;
}
```

Output (địa chỉ cụ thể thay đổi mỗi lần chạy) :

```
Dia chi trong main: 0x7ffd5c3a1e40
Dia chi trong ham : 0x7ffd5c3a1e40
```

Hai địa chỉ **giống hệt nhau**, chứng tỏ hàm đang làm việc trên chính mảng gốc.

**Chú ý** : Vì hàm chỉ nhận địa chỉ, bạn có thể truyền **một phần** của mảng bằng cách truyền địa chỉ phần tử bắt đầu. Biểu thức `a + k` là địa chỉ của `a[k]` (chi tiết ở bài [Con Trỏ Và Mảng 1 Chiều](07-03-c-con-tro-va-mang-1-chieu.md)):

```c
tong(a + 1, 3);   // tong 3 phan tu a[1], a[2], a[3]
```

---

**3. Bẫy sizeof Bên Trong Hàm**

Trong hàm khai báo mảng, bạn có thể tính số phần tử bằng `sizeof(a) / sizeof(a[0])`. Nhưng **bên trong hàm nhận mảng làm tham số**, cách này cho kết quả **sai**, vì lúc đó `a` chỉ là một con trỏ.

**Ví dụ 3** : 

```c
#include <stdio.h>

void kiemTra(int a[]){
    printf("Trong ham : sizeof(a) = %zu, so phan tu tinh duoc = %zu\n",
           sizeof(a), sizeof(a) / sizeof(a[0]));
}

int main(){
    int a[5] = {1, 2, 3, 4, 5};
    printf("Trong main: sizeof(a) = %zu, so phan tu tinh duoc = %zu\n",
           sizeof(a), sizeof(a) / sizeof(a[0]));
    kiemTra(a);
    return 0;
}
```

Output (trên máy 64-bit) :

```
Trong main: sizeof(a) = 20, so phan tu tinh duoc = 5
Trong ham : sizeof(a) = 8, so phan tu tinh duoc = 2
```

**Giải thích :** 

- Trong `main`, `a` là mảng thật gồm 5 phần tử `int`, `sizeof(a)` = 5 × 4 = 20 byte.
- Trong hàm `kiemTra`, `a` là **con trỏ** `int *`, `sizeof(a)` chỉ là kích thước của một con trỏ (8 byte trên máy 64-bit), nên phép chia cho ra con số 2 vô nghĩa.

Trình biên dịch gcc với `-Wall` cũng cảnh báo lỗi này:

```
warning: 'sizeof' on array function parameter 'a' will return size of 'int *'
```

**Quy tắc** : Chỉ dùng `sizeof(a) / sizeof(a[0])` ở **nơi khai báo mảng**, rồi truyền kết quả đó vào hàm dưới dạng tham số `n`.

```c
int a[] = {3, 1, 4, 1, 5, 9, 2, 6};
int n = sizeof(a) / sizeof(a[0]);   // dung: tinh o noi khai bao
printf("%d\n", tong(a, n));         // truyen n vao ham
```

---

**4. Tham Số const int a[]**

Vì hàm có thể sửa mảng gốc, đôi khi bạn vô tình thay đổi dữ liệu trong một hàm vốn chỉ cần **đọc** mảng. Để ngăn điều này, khai báo tham số với từ khoá `const`: trình biên dịch sẽ báo lỗi nếu hàm cố gán giá trị cho phần tử của mảng.

**Ví dụ 4** : Hàm tìm giá trị lớn nhất chỉ đọc mảng

```c
#include <stdio.h>

int timMax(const int a[], int n){
    int res = a[0];
    for(int i = 1; i < n; i++){
        if(a[i] > res){
            res = a[i];
        }
    }
    return res;
}

int main(){
    int a[6] = {3, 8, 1, 9, 4, 7};
    printf("Gia tri lon nhat : %d\n", timMax(a, 6));
    return 0;
}
```

Output :

```
Gia tri lon nhat : 9
```

Nếu bên trong `timMax` bạn lỡ viết `a[0] = 0;` thì chương trình sẽ **không biên dịch được**:

```
error: assignment of read-only location '*a'
```

**Chú ý** : 

- Hàm chỉ đọc mảng (in, tính tổng, tìm kiếm, đếm...) nên khai báo `const int a[]`.
- Hàm cần sửa mảng (nhập, sắp xếp, đảo ngược...) thì khai báo `int a[]` như bình thường.
- Nhìn vào nguyên mẫu hàm, người đọc biết ngay hàm có thay đổi mảng hay không.

---

**5. Hàm Nhập Và Xuất Mảng**

Đây là 2 hàm bạn sẽ viết đi viết lại rất nhiều lần. Hàm nhập cần thay đổi **cả mảng lẫn số lượng phần tử `n`**. Mảng thì tự động được sửa trực tiếp, còn `n` là biến `int` nên phải truyền **con trỏ** `int *n` thì hàm mới cập nhật được giá trị cho `main`.

**Ví dụ 5** : 

```c
#include <stdio.h>

void nhapMang(int a[], int *n){
    printf("Nhap so phan tu : ");
    scanf("%d", n);          // n da la dia chi nen khong can &
    for(int i = 0; i < *n; i++){
        printf("a[%d] = ", i);
        scanf("%d", &a[i]);
    }
}

void xuatMang(const int a[], int n){
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
}

int main(){
    int a[1000], n;
    nhapMang(a, &n);
    printf("Mang vua nhap : ");
    xuatMang(a, n);
    return 0;
}
```

Input :

```
4
7 2 9 5
```

Output :

```
Nhap so phan tu : a[0] = a[1] = a[2] = a[3] = Mang vua nhap : 7 2 9 5 
```

**Giải thích :** 

- Trong `nhapMang`, `n` là con trỏ trỏ tới biến `n` của `main`, nên `scanf("%d", n)` ghi thẳng vào biến đó, và `*n` là giá trị số phần tử.
- `xuatMang` chỉ đọc nên dùng `const int a[]` và nhận `n` theo tham trị.

**Chú ý** : Hàm trong C **không thể trả về một mảng**. Muốn hàm "tạo ra" một mảng kết quả, bạn khai báo mảng kết quả ở nơi gọi rồi truyền nó vào hàm làm tham số:

```c
// Ghi binh phuong cac phan tu cua a vao mang kq
void binhPhuong(const int a[], int kq[], int n){
    for(int i = 0; i < n; i++){
        kq[i] = a[i] * a[i];
    }
}
```

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/06-07-c-truyen-mang-vao-ham.md](solutions/06-07-c-truyen-mang-vao-ham.md)

**Bài 1.** Viết hàm `void xuatMang(const int a[], int n)` và hàm `int tongMang(const int a[], int n)`, gọi thử trong `main` với 2 mảng khác nhau.

**Bài 2.** Viết hàm `void nhapMang(int a[], int *n)` nhập số phần tử và các phần tử của mảng từ bàn phím.

**Bài 3.** Viết hàm `int timMax(const int a[], int n)` trả về giá trị lớn nhất và hàm `int viTriMin(const int a[], int n)` trả về chỉ số của phần tử nhỏ nhất.

**Bài 4.** Viết hàm `double trungBinh(const int a[], int n)` trả về trung bình cộng các phần tử (xử lý trường hợp `n = 0`).

**Bài 5.** Viết hàm `int demNguyenTo(const int a[], int n)` đếm số phần tử là số nguyên tố, có dùng thêm hàm `bool laNguyenTo(int x)`.

**Bài 6.** Viết hàm `void daoNguoc(int a[], int n)` đảo ngược mảng tại chỗ. In mảng trước và sau khi gọi hàm để thấy mảng gốc bị thay đổi.

**Bài 7.** Viết hàm `int timKiem(const int a[], int n, int x)` trả về chỉ số đầu tiên của `x` trong mảng, hoặc `-1` nếu không có.

**Bài 8.** Viết hàm `bool laTangDan(const int a[], int n)` kiểm tra mảng có tăng dần (không giảm) hay không.

**Bài 9.** Viết hàm `void cong2Mang(const int a[], const int b[], int c[], int n)` ghi tổng từng cặp phần tử `a[i] + b[i]` vào mảng `c`.

**Bài 10.** Chương trình sau in ra số phần tử sai. Tìm lỗi và sửa:

```c
void inMang(int a[]){
    int n = sizeof(a) / sizeof(a[0]);
    for(int i = 0; i < n; i++) printf("%d ", a[i]);
}
```

**Bài 11.** Viết hàm `void tachChanLe(const int a[], int n, int chan[], int *nc, int le[], int *nl)` tách mảng thành mảng số chẵn và mảng số lẻ.

**Bài 12.** Hàm sau có lỗi nguy hiểm gì? Giải thích và đưa ra cách sửa:

```c
int *taoMang(void){
    int a[5] = {1, 2, 3, 4, 5};
    return a;
}
```

**Bài 13.** Viết hàm `void xoayTrai(int a[], int n, int k)` xoay mảng sang trái `k` vị trí. Ví dụ `{1,2,3,4,5}`, `k = 2` → `{3,4,5,1,2}`.

**Bài 14.** Dùng lại hàm `tongMang` ở bài 1 để tính tổng đoạn `a[l..r]` bằng cách truyền `a + l` và `r - l + 1`, không viết hàm mới.

**Bài 15.** Viết chương trình menu quản lý mảng số nguyên, mỗi chức năng là một hàm riêng: nhập mảng, xuất mảng, thêm vào cuối, xoá tại vị trí, sắp xếp tăng dần, tìm kiếm.
