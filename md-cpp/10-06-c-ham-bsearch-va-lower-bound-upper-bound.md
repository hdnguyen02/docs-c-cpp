# [C]. Hàm bsearch Và Tự Cài lower_bound, upper_bound

Thư viện chuẩn của C cung cấp sẵn hàm **bsearch()** để tìm kiếm nhị phân trên mảng đã sắp xếp. Tuy nhiên C không có sẵn hai biến thể rất hay dùng của tìm kiếm nhị phân là **lower_bound** & **upper_bound**, nên trong bài này mình sẽ hướng dẫn bạn tự cài đặt chúng. Đây là hai hàm mà nếu biết sử dụng và ứng dụng nó bạn sẽ giải quyết được rất nhiều bài toán về tìm kiếm một cách tối ưu.

**NỘI DUNG :** 

- **Hàm bsearch**
- **Tự cài đặt hàm lower_bound**
- **Tự cài đặt hàm upper_bound**
- **Đếm số lần xuất hiện bằng lower_bound & upper_bound**

**1. Hàm bsearch**

Hàm **bsearch()** được cài đặt bằng thuật toán tìm kiếm nhị phân, bạn có thể áp dụng hàm này trên mảng bất kỳ kiểu dữ liệu nào (int, double, struct, chuỗi...) miễn là mảng **đã được sắp xếp** theo đúng thứ tự mà hàm so sánh quy định. Để sử dụng hàm này bạn cần thêm thư viện **stdlib.h** vào chương trình của mình.

**Nguyên mẫu hàm :**

```c
void *bsearch(const void *key, const void *base, size_t n, size_t size,
              int (*cmp)(const void *, const void *));
```

Trong đó :

- **key** : con trỏ tới giá trị cần tìm
- **base** : con trỏ tới phần tử đầu tiên của mảng
- **n** : số phần tử của mảng
- **size** : kích thước 1 phần tử (dùng `sizeof`)
- **cmp** : hàm so sánh, viết giống hệt hàm so sánh của **qsort()** (trả về số âm, 0, số dương). bsearch() gọi `cmp(key, phần_tử)`, tham số thứ nhất luôn là con trỏ tới giá trị cần tìm

**Giá trị trả về** : Hàm trả về con trỏ tới một phần tử bằng giá trị cần tìm, nếu không tìm thấy thì trả về **NULL**. Từ con trỏ trả về bạn có thể lấy được chỉ số bằng phép trừ con trỏ `p - a`.

**Độ phức tạp** : O(logN)

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int main(){
    int a[10] = {1, 2, 3, 5, 5, 6, 8, 9, 14, 21};
    int n = 10, X = 6, Y = 4;
    int *p = (int*)bsearch(&X, a, n, sizeof(int), cmp);
    if(p != NULL){
        printf("FOUND %d tai chi so %d\n", *p, (int)(p - a));
    }
    else{
        printf("NOT FOUND\n");
    }
    int *q = (int*)bsearch(&Y, a, n, sizeof(int), cmp);
    if(q != NULL){
        printf("FOUND %d tai chi so %d\n", *q, (int)(q - a));
    }
    else{
        printf("NOT FOUND\n");
    }
    return 0;
}
```

Output :

```
FOUND 6 tai chi so 5
NOT FOUND
```

> ⚠️ Nếu trong mảng có **nhiều phần tử bằng** giá trị cần tìm (ví dụ số 5 ở chỉ số 3 và 4), chuẩn C **không quy định** bsearch() trả về phần tử nào trong số đó. Muốn lấy chính xác vị trí đầu tiên hay cuối cùng, bạn cần hàm lower_bound, upper_bound ở phần sau.

> 💡 Hàm so sánh viết `(x > y) - (x < y)` thay cho `x - y` để tránh tràn số khi x, y trái dấu và rất lớn.

Ngoài ra bạn cũng có thể tìm kiếm trên đoạn chỉ số [L, R] của mảng bằng cách truyền địa chỉ bắt đầu là `a + L` và số phần tử là `R - L + 1`

**Cú pháp :** 

```c
// Tim kiem X tren doan chi so [L, R] cua mang a[]
bsearch(&X, a + L, R - L + 1, sizeof(int), cmp)
```

**Mã nguồn :** 

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b){
    int x = *(const int*)a, y = *(const int*)b;
    return (x > y) - (x < y);
}

int main(){
    int a[10] = {1, 2, 3, 5, 5, 6, 8, 9, 14, 21};
    int X = 5;
    // Doan chi so [5, 7] : {6, 8, 9}
    if(bsearch(&X, a + 5, 3, sizeof(int), cmp) != NULL){
        printf("FOUND\n");
    }
    else{
        printf("NOT FOUND\n");
    }
    // Doan chi so [2, 6] : {3, 5, 5, 6, 8}
    if(bsearch(&X, a + 2, 5, sizeof(int), cmp) != NULL){
        printf("FOUND\n");
    }
    else{
        printf("NOT FOUND\n");
    }
    return 0;
}
```

Output :

```
NOT FOUND
FOUND
```

**2. Tự cài đặt hàm lower_bound**

Hàm **lower_bound** được dùng để tìm **chỉ số của phần tử đầu tiên có giá trị lớn hơn hoặc bằng X** trong mảng tăng dần, tức là giá trị nhỏ nhất ≥ X.

**Giá trị trả về :** 

- Chỉ số của phần tử đầu tiên ≥ X
- Nếu mọi phần tử đều nhỏ hơn X thì trả về **n** (chỉ số "ngay sau phần tử cuối cùng"), vì vậy trước khi truy cập `a[vị_trí]` bạn phải kiểm tra `vị_trí < n`

**Ý tưởng :** Dùng tìm kiếm nhị phân trên nửa khoảng `[l, r)` với l = 0, r = n. Xét phần tử giữa `a[m]` :

- Nếu `a[m] < X` thì đáp án chắc chắn nằm bên phải m, gán `l = m + 1`
- Ngược lại `a[m] >= X` thì a[m] có thể là đáp án, nhưng vẫn có thể còn phần tử ≥ X ở bên trái, gán `r = m`

Khi `l == r` thì l chính là đáp án.

**Độ phức tạp** : O(logN)

**Mã nguồn** : 

```c
#include <stdio.h>

// Tra ve chi so phan tu dau tien >= x, hoac n neu khong co
int lower_bound(int a[], int n, int x){
    int l = 0, r = n;
    while(l < r){
        int m = l + (r - l) / 2;
        if(a[m] < x) l = m + 1;
        else r = m;
    }
    return l;
}

int main(){
    int a[10] = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int n = 10, X = 5, Y = 22;
    int i1 = lower_bound(a, n, X);
    if(i1 == n){
        printf("Khong tim duoc gia tri >= %d\n", X);
    }
    else{
        printf("Gia tri nho nhat >= %d : %d\n", X, a[i1]);
        printf("Chi so cua gia tri tim duoc : %d\n", i1);
    }
    int i2 = lower_bound(a, n, Y);
    if(i2 == n){
        printf("Khong tim duoc gia tri >= %d\n", Y);
    }
    else{
        printf("Gia tri nho nhat >= %d : %d\n", Y, a[i2]);
        printf("Chi so cua gia tri tim duoc : %d\n", i2);
    }
    return 0;
}
```

Output :

```
Gia tri nho nhat >= 5 : 5
Chi so cua gia tri tim duoc : 3
Khong tim duoc gia tri >= 22
```

**Chú ý** : Muốn áp dụng hàm lower_bound trên đoạn chỉ số [L, R], bạn truyền `a + L` và `R - L + 1` giống như bsearch, kết quả trả về là chỉ số **tính từ L**, nên cộng thêm L để có chỉ số trong mảng gốc : `L + lower_bound(a + L, R - L + 1, X)`.

**3. Tự cài đặt hàm upper_bound**

Hàm **upper_bound** cách cài đặt, giá trị trả về, độ phức tạp đều giống hàm lower_bound, chỉ khác duy nhất là hàm này tìm **chỉ số của phần tử đầu tiên có giá trị lớn hơn X** (giá trị nhỏ nhất > X) trong mảng tăng dần.

Trong code, bạn chỉ cần đổi điều kiện `a[m] < x` thành `a[m] <= x`.

**Mã nguồn** : 

```c
#include <stdio.h>

// Tra ve chi so phan tu dau tien > x, hoac n neu khong co
int upper_bound(int a[], int n, int x){
    int l = 0, r = n;
    while(l < r){
        int m = l + (r - l) / 2;
        if(a[m] <= x) l = m + 1;
        else r = m;
    }
    return l;
}

int main(){
    int a[10] = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int n = 10, X = 5, Y = 22;
    int i1 = upper_bound(a, n, X);
    if(i1 == n){
        printf("Khong tim duoc gia tri > %d\n", X);
    }
    else{
        printf("Gia tri nho nhat > %d : %d\n", X, a[i1]);
        printf("Chi so cua gia tri tim duoc : %d\n", i1);
    }
    int i2 = upper_bound(a, n, Y);
    if(i2 == n){
        printf("Khong tim duoc gia tri > %d\n", Y);
    }
    else{
        printf("Gia tri nho nhat > %d : %d\n", Y, a[i2]);
        printf("Chi so cua gia tri tim duoc : %d\n", i2);
    }
    return 0;
}
```

Output :

```
Gia tri nho nhat > 5 : 8
Chi so cua gia tri tim duoc : 6
Khong tim duoc gia tri > 22
```

**4. Đếm số lần xuất hiện bằng lower_bound & upper_bound**

Trong mảng tăng dần, các phần tử bằng X luôn đứng liền nhau thành một đoạn. lower_bound cho biết **đầu đoạn**, còn upper_bound cho biết **vị trí ngay sau cuối đoạn**, do đó :

- Số lần xuất hiện của X = `upper_bound(X) - lower_bound(X)`
- X có xuất hiện trong mảng khi và chỉ khi `lower_bound(X) < n` và `a[lower_bound(X)] == X`

**Mã nguồn** :

```c
#include <stdio.h>

int lower_bound(int a[], int n, int x){
    int l = 0, r = n;
    while(l < r){
        int m = l + (r - l) / 2;
        if(a[m] < x) l = m + 1;
        else r = m;
    }
    return l;
}

int upper_bound(int a[], int n, int x){
    int l = 0, r = n;
    while(l < r){
        int m = l + (r - l) / 2;
        if(a[m] <= x) l = m + 1;
        else r = m;
    }
    return l;
}

int main(){
    int a[10] = {1, 2, 3, 5, 5, 5, 8, 9, 14, 21};
    int n = 10;
    int q[3] = {5, 8, 4};
    for(int i = 0; i < 3; i++){
        int x = q[i];
        int lb = lower_bound(a, n, x), ub = upper_bound(a, n, x);
        printf("So %d : lower_bound = %d, upper_bound = %d, xuat hien %d lan\n",
               x, lb, ub, ub - lb);
    }
    return 0;
}
```

Output :

```
So 5 : lower_bound = 3, upper_bound = 6, xuat hien 3 lan
So 8 : lower_bound = 6, upper_bound = 7, xuat hien 1 lan
So 4 : lower_bound = 3, upper_bound = 3, xuat hien 0 lan
```

**Nhận xét** : Khi X không xuất hiện trong mảng thì lower_bound và upper_bound trả về cùng một chỉ số, đó cũng chính là vị trí để chèn X vào mảng mà vẫn giữ được thứ tự tăng dần.

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-06-c-ham-bsearch-va-lower-bound-upper-bound.md](solutions/10-06-c-ham-bsearch-va-lower-bound-upper-bound.md)

**Bài 1.** Dùng `bsearch` kiểm tra một giá trị có trong mảng đã sắp xếp hay không, in ra chỉ số nếu tìm thấy.

**Bài 2.** Dùng hàm `lower_bound` tự viết tìm vị trí đầu tiên có giá trị ≥ `x`.

**Bài 3.** Dùng hàm `upper_bound` tự viết tìm vị trí đầu tiên có giá trị > `x`. Lập bảng so sánh kết quả với `lower_bound`.

**Bài 4.** Dùng `lower_bound` và `upper_bound` đếm số lần xuất hiện của `x`.

**Bài 5.** Viết hàm `equal_range(a, n, x, &dau, &cuoi)` trả về cả hai vị trí qua con trỏ, in ra đoạn các phần tử bằng `x`.

**Bài 6.** Tìm vị trí chèn `x` vào mảng đã sắp xếp mà vẫn giữ thứ tự, rồi thực hiện chèn (dịch các phần tử phía sau).

**Bài 7.** Vì sao `bsearch` trả về con trỏ (hoặc `NULL`) chứ không phải chỉ số? Khi có nhiều phần tử bằng nhau, làm sao lấy được vị trí **đầu tiên**?

**Bài 8.** Dùng `lower_bound` tìm phần tử gần `x` nhất trong mảng đã sắp xếp.

**Bài 9.** Viết `lower_bound`, `upper_bound` cho mảng sắp xếp **giảm dần**, và dùng `bsearch` với hàm so sánh giảm dần.

**Bài 10.** Dùng `bsearch` trên mảng struct sinh viên đã sắp xếp theo mã để tra cứu theo mã.

**Bài 11.** Đếm số phần tử nằm trong khoảng `[a, b]` của một mảng đã sắp xếp.

**Bài 12.** Dùng `bsearch` tra cứu một từ trong mảng chuỗi đã sắp xếp theo thứ tự từ điển (dùng `strcmp`).

**Bài 13.** Chương trình sau cho kết quả sai. Tìm lỗi:

```c
int a[] = {5, 2, 8, 1, 9};
int x = 1;
int *p = bsearch(&x, a, 5, sizeof(int), cmp);
printf("%s\n", p ? "FOUND" : "NOT FOUND");
```

**Bài 14.** So sánh tốc độ tìm kiếm tuyến tính, `bsearch` và `lower_bound` tự viết với 10⁶ truy vấn.

**Bài 15.** Viết chương trình tra cứu bảng điểm: nhập điểm, dùng `upper_bound` (trên mảng `double`) để xác định xếp loại theo bảng ngưỡng.
