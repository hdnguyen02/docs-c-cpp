# [C]. Sắp Xếp Ổn Định Và Merge Sort

Ở bài học trước mình đã hướng dẫn các bạn cách sử dụng hàm **qsort()** và cách xây dựng hàm so sánh cho qsort(). Tiếp tục kiến thức về sắp xếp và tìm kiếm trong C, mình sẽ hướng dẫn bạn hiểu về tính chất ổn định (stable) của thuật toán sắp xếp, vì sao qsort() **không đảm bảo** tính ổn định và 2 cách để có được một phép sắp xếp ổn định trong C.

**NỘI DUNG :** 

- **Tính chất ổn định - stable của thuật toán sắp xếp**
- **Hàm qsort() không đảm bảo tính ổn định**
- **Cách 1 : Thêm chỉ số ban đầu làm tiêu chí phụ**
- **Cách 2 : Tự cài đặt thuật toán sắp xếp trộn Merge sort**

---

**1. Tính chất ổn định - stable của thuật toán sắp xếp**

Các thuật toán sắp xếp chia thành 2 loại là ổn định và không ổn định, các thuật toán sắp xếp không ổn định có thể kể đến như : sắp xếp nhanh quicksort, sắp xếp vun đống heap sort, sắp xếp chọn selection sort. Bên cạnh đó các thuật toán sắp xếp ổn định bao gồm : sắp xếp trộn merge sort, sắp xếp chèn insertion sort, tim sort, sắp xếp đếm phân phối counting sort.

Vậy tính ổn định của thuật toán sắp xếp là gì ?

Tính ổn định của thuật toán sắp xếp có thể hiểu đơn giản là khi bạn sắp xếp các phần tử trong mảng mà có cùng giá trị sắp xếp (ví dụ như giá trị về độ lớn, tổng chữ số ..) thì những phần tử này sẽ đứng cạnh nhau và duy trì thứ tự giống như thứ tự giữa chúng trong mảng ban đầu.

Ví dụ bạn có dãy số (111, 9, 3000, 18, 81, 1002, 2002) và muốn sắp xếp các phần tử này theo tổng chữ số tăng dần bằng thuật toán sắp xếp có tính chất stable thì mảng sẽ được sắp xếp theo thứ tự (111, 3000, 1002, 2002, 9, 18, 81) trong đó (111, 3000, 1002) có cùng tổng chữ số là 3 và chúng giữ đúng thứ tự ban đầu như thứ tự xuất hiện. Tương tự với cụm (9, 18, 81) có cùng tổng chữ số là 9.

Trong một số ngôn ngữ lập trình thì hàm sắp xếp có sẵn được cài đặt bởi các thuật toán sắp xếp có tính ổn định, ví dụ như Java (khi sắp xếp đối tượng), Python, JS. Còn trong C, thư viện chuẩn chỉ cung cấp duy nhất hàm **qsort()** và hàm này **không được đảm bảo** là ổn định.

---

**2. Hàm qsort() không đảm bảo tính ổn định**

Chuẩn C chỉ quy định qsort() sắp xếp mảng theo hàm so sánh mà bạn truyền vào, và nói rõ : nếu 2 phần tử được hàm so sánh coi là **bằng nhau** thì **thứ tự giữa chúng trong mảng kết quả là không xác định**.

Điều đó có nghĩa là mỗi thư viện C có thể cài đặt qsort() bằng một thuật toán khác nhau. Tuỳ thư viện và phiên bản, qsort() có thể dùng merge sort (thường cho kết quả ổn định), quicksort hoặc một thuật toán khác (không ổn định). Vì vậy bạn **không được dựa vào** việc qsort() "tình cờ" giữ đúng thứ tự trên máy của mình.

**Ví dụ** : Sắp xếp dãy số theo tổng chữ số tăng dần bằng qsort()

```c
#include <stdio.h>
#include <stdlib.h>

int tong(int n){
    int sum = 0;
    while(n){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int cmp(const void *a, const void *b){
    int x = *(const int*)a, y = *(const int*)b;
    return tong(x) - tong(y);
}

int main(){
    int a[] = {10002, 19, 3000, 111, 81, 45, 1002, 21, 10071, 203, 401};
    int n = 11;
    qsort(a, n, sizeof(int), cmp);
    printf("Mang sau khi sap xep : \n");
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    return 0;
}
```

Output (tuỳ thư viện C, có thể khác trên máy bạn) :

```
Mang sau khi sap xep : 
10002 3000 111 1002 21 203 401 81 45 10071 19
```

**Nhận xét** : Các số trong mảng đều được sắp theo tổng chữ số tăng dần, nhưng thứ tự giữa các số có **cùng tổng chữ số** (ví dụ 10002, 3000, 111, 1002, 21 cùng tổng là 3) thì chuẩn C không hứa hẹn gì. Trên một thư viện C khác, bạn có thể nhận được 3000 đứng trước 10002.

> 💡 Ở đây dùng `tong(x) - tong(y)` là an toàn vì tổng chữ số là số nhỏ, không thể tràn số.

Nếu đề bài có thêm yêu cầu : **khi các phần tử có cùng giá trị sắp xếp thì giữ nguyên thứ tự xuất hiện**, bạn có 2 cách làm dưới đây.

---

**3. Cách 1 : Thêm chỉ số ban đầu làm tiêu chí phụ**

Ý tưởng : lưu kèm mỗi phần tử **chỉ số của nó trong mảng ban đầu**. Trong hàm so sánh, nếu 2 phần tử có cùng giá trị sắp xếp thì so sánh tiếp theo chỉ số ban đầu, phần tử nào đứng trước thì xếp trước.

Khi đó không còn 2 phần tử nào bị hàm so sánh coi là "bằng nhau", nên thứ tự kết quả luôn xác định và giống hệt một phép sắp xếp ổn định, dù qsort() dùng thuật toán gì.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int giaTri;
    int viTriGoc;
} PhanTu;

int tong(int n){
    int sum = 0;
    while(n){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int cmp(const void *a, const void *b){
    const PhanTu *x = (const PhanTu*)a;
    const PhanTu *y = (const PhanTu*)b;
    int tx = tong(x->giaTri), ty = tong(y->giaTri);
    if(tx != ty) return tx - ty;          // tieu chi chinh : tong chu so
    return x->viTriGoc - y->viTriGoc;     // tieu chi phu : vi tri ban dau
}

int main(){
    int a[] = {10002, 19, 3000, 111, 81, 45, 1002, 21, 10071, 203, 401};
    int n = 11;
    PhanTu p[11];
    for(int i = 0; i < n; i++){
        p[i].giaTri = a[i];
        p[i].viTriGoc = i;
    }
    qsort(p, n, sizeof(PhanTu), cmp);
    printf("Mang sau khi sap xep : \n");
    for(int i = 0; i < n; i++){
        printf("%d ", p[i].giaTri);
    }
    printf("\n");
    return 0;
}
```

Output :

```
Mang sau khi sap xep : 
10002 3000 111 1002 21 203 401 81 45 10071 19
```

**Nhận xét** : Kết quả này luôn đúng trên mọi thư viện C. Cái giá phải trả là tốn thêm một trường `viTriGoc` cho mỗi phần tử.

---

**4. Cách 2 : Tự cài đặt thuật toán sắp xếp trộn Merge sort**

Merge sort là thuật toán sắp xếp ổn định, độ phức tạp **O(NlogN)** trong mọi trường hợp. Ý tưởng của thuật toán :

- Chia mảng thành 2 nửa trái và phải
- Sắp xếp đệ quy từng nửa
- **Trộn** 2 nửa đã sắp xếp thành một mảng đã sắp xếp

Tính ổn định nằm ở bước trộn : khi phần tử ở nửa trái và nửa phải **bằng nhau**, ta luôn lấy phần tử ở **nửa trái** trước (vì nó xuất hiện trước trong mảng ban đầu).

Merge sort cần một **mảng phụ** có kích thước bằng mảng cần sắp xếp để trộn, trong C ta cấp phát mảng phụ này bằng malloc() và giải phóng bằng free().

**Ví dụ** : Sắp xếp dãy số theo tổng chữ số tăng dần và giữ nguyên thứ tự xuất hiện giữa chúng nếu có cùng tổng chữ số

```c
#include <stdio.h>
#include <stdlib.h>

int tong(int n){
    int sum = 0;
    while(n){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

// Tron 2 doan da sap xep a[l..m] va a[m+1..r]
void tron(int a[], int tam[], int l, int m, int r){
    int i = l, j = m + 1, k = l;
    while(i <= m && j <= r){
        // Dau <= la mau chot : bang nhau thi lay tu nua TRAI truoc
        if(tong(a[i]) <= tong(a[j])) tam[k++] = a[i++];
        else tam[k++] = a[j++];
    }
    while(i <= m) tam[k++] = a[i++];
    while(j <= r) tam[k++] = a[j++];
    for(k = l; k <= r; k++) a[k] = tam[k];
}

void mergeSort(int a[], int tam[], int l, int r){
    if(l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(a, tam, l, m);
    mergeSort(a, tam, m + 1, r);
    tron(a, tam, l, m, r);
}

int main(){
    int a[] = {10002, 19, 3000, 111, 81, 45, 1002, 21, 10071, 203, 401};
    int n = 11;
    int *tam = (int*)malloc(n * sizeof(int));
    if(tam == NULL) return 1;
    mergeSort(a, tam, 0, n - 1);
    free(tam);
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
10002 3000 111 1002 21 203 401 81 45 10071 19
```

**Nhận xét** : Bạn chỉ cần sửa điều kiện so sánh trong hàm `tron()` để sắp xếp theo tiêu chí mong muốn, còn khi các số trong mảng có cùng tổng chữ số thì merge sort sẽ giữ thứ tự tương đối giữa chúng.

> ⚠️ Nếu đổi dấu `<=` trong hàm `tron()` thành `<`, khi 2 phần tử bằng nhau thuật toán sẽ lấy phần tử ở nửa phải trước và **mất tính ổn định**.

**So sánh 2 cách :**

| | qsort() + chỉ số ban đầu | Tự viết merge sort |
|---|---|---|
| Độ dài code | Ngắn, chỉ sửa hàm so sánh | Dài hơn |
| Bộ nhớ thêm | Thêm 1 trường chỉ số / phần tử | Mảng phụ O(N) |
| Tốc độ | Nhanh (dùng thư viện) | Nhanh, O(NlogN) mọi trường hợp |
| Đảm bảo ổn định | Có | Có |

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-04-c-sap-xep-on-dinh-va-merge-sort.md](solutions/10-04-c-sap-xep-on-dinh-va-merge-sort.md)

**Bài 1.** Cho mảng struct gồm 2 trường `khoa` (int) và `nhan` (char). Sắp xếp theo `khoa` bằng `qsort` và bằng merge sort tự viết. So sánh kết quả.

**Bài 2.** Viết chương trình kiểm tra `qsort` trên máy bạn có cho kết quả ổn định hay không với mảng lớn nhiều khoá trùng nhau. Sau đó tự cài quicksort và chứng minh nó **không** ổn định.

**Bài 3.** Sắp xếp danh sách sinh viên (tên là mảng `char`, điểm là `double`) theo điểm giảm dần, giữ nguyên thứ tự nhập ban đầu khi cùng điểm.

**Bài 4.** Sắp xếp nhiều tiêu chí bằng cách gọi một hàm sắp xếp ổn định **nhiều lần** (từ tiêu chí phụ đến chính).

**Bài 5.** So sánh tốc độ `qsort` và merge sort tự viết trên mảng 1 triệu phần tử (đo bằng `clock()`).

**Bài 6.** So sánh bộ nhớ phụ mà quicksort và merge sort cần dùng.

**Bài 7.** Khi nào bắt buộc phải dùng sắp xếp ổn định? Nêu 3 tình huống thực tế.

**Bài 8.** Làm cho `qsort` cho kết quả "ổn định" bằng cách thêm chỉ số ban đầu vào tiêu chí so sánh.

**Bài 9.** Sắp xếp bảng dữ liệu nhiều cột: sắp theo cột A, rồi trong mỗi nhóm sắp theo cột B — bằng sắp xếp ổn định.

**Bài 10.** Viết hàm `stableSort(void *base, size_t n, size_t size, int (*cmp)(const void*, const void*))` có cùng cách gọi như `qsort` nhưng cài bằng merge sort (ổn định).

**Bài 11.** Cài đặt Selection Sort và chứng minh nó **không** ổn định.

**Bài 12.** Tách mảng thành số chẵn đứng trước, số lẻ đứng sau, giữ nguyên thứ tự trong mỗi nhóm (phân hoạch ổn định).

**Bài 13.** Sắp xếp danh sách giao dịch theo ngày (chuỗi `"yyyy-mm-dd"`), cùng ngày thì giữ thứ tự thời gian nhập.

**Bài 14.** Lập bảng so sánh các thuật toán Bubble, Insertion, Selection, Merge, Quick, Heap sort về độ phức tạp, bộ nhớ phụ và tính ổn định.

**Bài 15.** Viết chương trình mô phỏng bảng xếp hạng nhiều vòng đấu: mỗi vòng sắp lại, người cùng điểm giữ thứ hạng vòng trước.
