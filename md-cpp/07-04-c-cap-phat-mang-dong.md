# [C]. Cấp Phát Mảng Động

Cấp phát mảng động trong C được thực hiện thông qua các hàm **malloc**, **calloc**, **realloc** và **free** của thư viện `<stdlib.h>`. Đây là thao tác quan trọng khi xây dựng các cấu trúc dữ liệu như danh sách liên kết hay cây nhị phân.

**NỘI DUNG :** 

- **Cấp Phát Động Là Gì ?** 
- **Hàm Malloc, Calloc, Realloc Và Free**
- **Video Tutorial**

---

**1. Cấp Phát Động Là Gì?**

**Cấp phát động** - Dynamic memory allocation trong C là hình thức xin cấp phát vùng nhớ bởi lập trình viên.

Khi cấp phát động thì người lập trình sẽ chủ động xin cấp phát vùng nhớ khi cần và giải phóng vùng nhớ khi cần thu hồi.

Một số đặc điểm về cấp phát động bạn cần nhớ :

- Vùng nhớ sử dụng khi cấp phát động là vùng nhớ **heap** 
- Lập trình viên cần giải phóng vùng nhớ để tránh rò rỉ bộ nhớ (leak memory)
- Cấp phát động là thao tác chính để tạo nên các cấu trúc dữ liệu như cây nhị phân hay danh sách liên kết

Các hàm cấp phát động đều nằm trong thư viện **`<stdlib.h>`**, vì vậy bạn cần `#include <stdlib.h>` trước khi sử dụng.

---

**2. Hàm Malloc, Calloc, Realloc Và Free** 

**Hàm malloc :** 

Vùng nhớ cấp phát động được xin cấp phát thông qua hàm **malloc** (memory allocation). Tham số của malloc là **số byte** cần cấp phát, vì vậy khi xin cấp phát một mảng bạn cần nhân số lượng phần tử với kích thước mỗi phần tử (dùng toán tử `sizeof`).

Hàm malloc sẽ trả về con trỏ kiểu `void *` tới ô nhớ đầu tiên của vùng nhớ được cấp phát hoặc sẽ trả về con trỏ **NULL** nếu không cấp phát đủ bộ nhớ. Trong C, con trỏ `void *` được tự động chuyển sang kiểu con trỏ mà bạn gán nên không cần ép kiểu.

**Cú pháp :** 

```c
pointer = malloc(sizeof(data_type));
pointer = malloc(num_of_elements * sizeof(data_type));
```

Cú pháp thứ nhất sẽ xin cấp phát 1 phần tử còn cú pháp thứ 2 xin cấp phát 1 khối (tương tự như 1 mảng các phần tử).

Sau khi xin cấp phát 1 mảng động thì bạn có thể sử dụng mảng động thông qua con trỏ pointer tương tự như mảng 1 chiều.

**Chú ý** : Vùng nhớ do malloc cấp phát **chưa được khởi tạo**, các phần tử mang giá trị rác cho tới khi bạn gán giá trị cho chúng.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int *ptr = malloc(5 * sizeof(int));
    if(ptr == NULL){
        return 1;
    }
    printf("Gia tri cua ptr : %p\n", (void *)ptr);
    ptr[0] = 1;
    ptr[1] = 2;
    ptr[2] = 3;
    ptr[3] = 4;
    ptr[4] = 5;
    for(int i = 0; i < 5; i++){
        printf("%d ", ptr[i]); // hoac *(ptr + i)
    }
    free(ptr);
    return 0;
}
```

Output :

```
Gia tri cua ptr : 0xca1510
1 2 3 4 5
```

Trong trường hợp vùng nhớ heap không đủ cấp phát thì hàm malloc sẽ trả về con trỏ NULL (C không có cơ chế ngoại lệ). Vì vậy bạn **luôn phải kiểm tra** việc cấp phát có thành công hay không trước khi sử dụng con trỏ, trong ví dụ dưới đây mình sẽ xin cấp phát vùng nhớ có cỡ 10<sup>13</sup> phần tử int để việc cấp phát không thành công.

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int *ptr = malloc(10000000000000LL * sizeof(int));
    if(ptr == NULL){
        printf("Khong du bo nho cap phat !\n");
    }
    free(ptr); // free(NULL) hop le, khong lam gi ca
    return 0;
}
```

Output :

```
Khong du bo nho cap phat !
```

Nếu bạn quên kiểm tra NULL mà truy cập luôn `ptr[0]`, chương trình sẽ bị lỗi **Segmentation fault** khi chạy.

---

**Hàm calloc :** 

Hàm **calloc** (contiguous allocation) cũng dùng để cấp phát một mảng, nhưng có 2 điểm khác so với malloc:

- Nhận **2 tham số**: số lượng phần tử và kích thước mỗi phần tử
- Tất cả các byte trong vùng nhớ được **khởi tạo bằng 0**

**Cú pháp :** 

```c
pointer = calloc(num_of_elements, sizeof(data_type));
```

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int n = 5;
    int *ptr = calloc(n, sizeof(int));
    if(ptr == NULL){
        printf("Khong du bo nho cap phat !\n");
        return 1;
    }
    for(int i = 0; i < n; i++){
        printf("%d ", ptr[i]);
    }
    free(ptr);
    return 0;
}
```

Output :

```
0 0 0 0 0
```

---

**Hàm realloc :** 

Hàm **realloc** (re-allocation) dùng để **thay đổi kích thước** vùng nhớ đã được cấp phát trước đó bởi malloc, calloc hoặc realloc. Dữ liệu cũ (trong phạm vi kích thước nhỏ hơn giữa cũ và mới) được giữ nguyên, phần mới mở rộng thêm mang giá trị rác.

**Cú pháp :** 

```c
new_pointer = realloc(pointer, new_size_in_bytes);
```

Khi không đủ bộ nhớ, realloc trả về NULL và **vùng nhớ cũ vẫn còn nguyên**. Vì vậy bạn nên gán kết quả vào một con trỏ tạm, kiểm tra NULL rồi mới gán lại cho con trỏ chính, tránh việc mất địa chỉ vùng nhớ cũ.

Lưu ý realloc có thể chuyển dữ liệu sang một vùng nhớ khác, khi đó địa chỉ cũ không còn dùng được nữa.

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int n = 3;
    int *ptr = malloc(n * sizeof(int));
    if(ptr == NULL) return 1;
    for(int i = 0; i < n; i++){
        ptr[i] = i + 1; // 1 2 3
    }
    // Mo rong mang len 6 phan tu
    int *tmp = realloc(ptr, 6 * sizeof(int));
    if(tmp == NULL){
        printf("Khong du bo nho cap phat !\n");
        free(ptr);
        return 1;
    }
    ptr = tmp;
    for(int i = n; i < 6; i++){
        ptr[i] = (i + 1) * 10;
    }
    for(int i = 0; i < 6; i++){
        printf("%d ", ptr[i]);
    }
    free(ptr);
    return 0;
}
```

Output :

```
1 2 3 40 50 60
```

---

**Hàm free :** 

Hàm **free** được sử dụng để giải phóng vùng nhớ đã xin cấp phát trước đó bởi malloc, calloc hoặc realloc.

Việc này là cần thiết để tránh việc leak memory

**Cú pháp :** 

```c
free(pointer);
```

Trong C chỉ có một hàm free dùng cho cả vùng nhớ 1 phần tử lẫn vùng nhớ là một mảng. Một số lưu ý khi dùng free:

- Chỉ free con trỏ nhận được từ malloc, calloc, realloc; không free mảng tĩnh hay biến thường
- Không free một vùng nhớ 2 lần
- Sau khi free nên gán con trỏ bằng NULL để tránh dùng lại vùng nhớ đã giải phóng
- `free(NULL)` hợp lệ và không làm gì cả

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int n; printf("Nhap so luong phan tu xin cap phat : ");
    scanf("%d", &n);
    int *ptr = malloc(n * sizeof(int));
    if(ptr == NULL){
        printf("Khong du bo nho cap phat !\n");
    }
    else{
        printf("Nhap cac phan tu trong day : ");
        for(int i = 0; i < n; i++){
            scanf("%d", &ptr[i]);
        }
        printf("Cac phan tu vua nhap : ");
        for(int i = 0; i < n; i++){
            printf("%d ", ptr[i]);
        }
        free(ptr);
        ptr = NULL;
    }
    return 0;
}
```

---

**Xem thêm bài giảng về Con Trỏ của mình :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/07-04-c-cap-phat-mang-dong.md](solutions/07-04-c-cap-phat-mang-dong.md)

**Bài 1.** Nhập `n` từ bàn phím, cấp phát mảng động `n` phần tử bằng `malloc`, nhập giá trị, in ra rồi giải phóng.

**Bài 2.** Cấp phát một biến `int` động bằng `malloc`, gán giá trị, in ra rồi `free`.

**Bài 3.** Cấp phát mảng động và khởi tạo tất cả phần tử bằng 0 (ít nhất 2 cách).

**Bài 4.** Viết hàm `int *taoMang(int n)` cấp phát và trả về mảng động đã điền giá trị `0..n-1`.

**Bài 5.** Viết hàm mở rộng mảng động: cấp phát mảng mới lớn hơn, copy dữ liệu cũ sang, giải phóng mảng cũ. So sánh với cách dùng `realloc`.

**Bài 6.** Cấp phát mảng 2 chiều động `n × m` và tính tổng các phần tử.

**Bài 7.** Chương trình sau có lỗi gì? Sửa lại:

```c
int *a = malloc(10);
for (int i = 0; i < 10; i++) a[i] = i;
free(a);
```

**Bài 8.** Chương trình sau bị rò rỉ bộ nhớ (memory leak). Tìm và sửa:

```c
for (int i = 0; i < 1000; i++) {
    int *p = malloc(1000 * sizeof(int));
    // ... xu ly ...
}
```

**Bài 9.** Chương trình sau có lỗi gì? Giải thích:

```c
int *p = malloc(sizeof(int));
*p = 5;
free(p);
printf("%d", *p);
free(p);
```

**Bài 10.** So sánh mảng tĩnh và mảng động: lập bảng về kích thước, thời điểm xác định, vùng nhớ, giới hạn.

**Bài 11.** Tại sao mảng cục bộ `int a[10000000]` bị crash nhưng `malloc(10000000 * sizeof(int))` thì không? Giải thích stack vs heap.

**Bài 12.** Viết chương trình mô phỏng mảng động tự giãn: dùng `struct` gồm con trỏ dữ liệu, số lượng, sức chứa; hàm `push_back` tự mở rộng gấp đôi bằng `realloc` khi đầy.

**Bài 13.** Nhập một dãy số nguyên kết thúc bằng số `0` mà không biết trước số lượng, lưu vào mảng động dùng `realloc` để mở rộng, rồi in dãy vừa nhập.

**Bài 14.** Dùng công cụ phát hiện rò rỉ bộ nhớ (`valgrind` hoặc `-fsanitize=address`) kiểm tra chương trình ở bài 8.

**Bài 15.** Viết chương trình quản lý danh sách sinh viên (`struct` gồm họ tên, tuổi, điểm) với số lượng do người dùng nhập, dùng cấp phát động và giải phóng đúng cách.
