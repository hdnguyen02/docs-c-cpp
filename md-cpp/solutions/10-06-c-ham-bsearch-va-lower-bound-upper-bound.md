# Lời giải — [C]. Hàm bsearch Và Tự Cài lower_bound, upper_bound

[← Quay lại bài học](../10-06-c-ham-bsearch-va-lower-bound-upper-bound.md)

> **Cả 3 hàm đều yêu cầu mảng ĐÃ SẮP XẾP** (theo đúng thứ tự mà hàm so sánh quy định) và có độ phức tạp **O(log n)**. `bsearch` nằm trong `<stdlib.h>`; `lower_bound`, `upper_bound` ta tự viết.

| Hàm | Trả về |
|---|---|
| `bsearch(&x, a, n, size, cmp)` | Con trỏ tới **một** phần tử bằng `x`, hoặc `NULL` |
| `lower_bound(a, n, x)` | Chỉ số phần tử **đầu tiên ≥ x**, hoặc `n` |
| `upper_bound(a, n, x)` | Chỉ số phần tử **đầu tiên > x**, hoặc `n` |

Hai hàm tự viết dùng trong hầu hết lời giải bên dưới:

```c
int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;                     // tim tren nua khoang [l, r)
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int upper_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] <= x) l = m + 1; else r = m;
    }
    return l;
}
```

---

### Bài 1.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int main(void) {
    int v[] = {1, 3, 5, 7, 9, 11, 13};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);
    printf("\n\n");

    int canTim[] = {7, 1, 13, 8, 100};
    for (int k = 0; k < 5; k++) {
        int x = canTim[k];
        int *p = bsearch(&x, v, n, sizeof(int), cmpInt);
        if (p != NULL) printf("bsearch(%d) -> tim thay tai chi so %d\n", x, (int)(p - v));
        else           printf("bsearch(%d) -> NULL (khong co)\n", x);
    }
    return 0;
}
```

Output:

```
Mang: 1 3 5 7 9 11 13 

bsearch(7) -> tim thay tai chi so 3
bsearch(1) -> tim thay tai chi so 0
bsearch(13) -> tim thay tai chi so 6
bsearch(8) -> NULL (khong co)
bsearch(100) -> NULL (khong co)
```

💡 Tham số đầu của `bsearch` là **địa chỉ** của giá trị cần tìm (`&x`), không phải `x`.

💡 Trong C, `void *` tự chuyển sang `int *` khi gán nên không bắt buộc ép kiểu `(int *)` — viết thêm cũng không sai.

### Bài 2.

```c
#include <stdio.h>

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int main(void) {
    int v[] = {1, 3, 3, 5, 7, 7, 7, 9};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d(%d) ", v[i], i);
    printf("\n\n");

    int canTim[] = {3, 7, 4, 0, 10};
    for (int k = 0; k < 5; k++) {
        int x = canTim[k];
        int vt = lower_bound(v, n, x);
        printf("lower_bound(%d) -> vi tri %d", x, vt);
        if (vt < n) printf(", gia tri %d\n", v[vt]);
        else        printf(" (= n, moi phan tu deu < %d)\n", x);
    }
    return 0;
}
```

Output:

```
lower_bound(3) -> vi tri 1, gia tri 3
lower_bound(7) -> vi tri 4, gia tri 7
lower_bound(4) -> vi tri 3, gia tri 5
lower_bound(0) -> vi tri 0, gia tri 1
lower_bound(10) -> vi tri 8 (= n, moi phan tu deu < 10)
```

⚠️ **Luôn kiểm tra `vt < n`** trước khi truy cập `v[vt]` — `v[n]` nằm ngoài mảng.

💡 `lower_bound` trả về **vị trí chèn** đúng chỗ để giữ thứ tự sắp xếp — kể cả khi `x` không có trong mảng.

### Bài 3.

```c
#include <stdio.h>

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int upper_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] <= x) l = m + 1; else r = m;
    }
    return l;
}

int main(void) {
    int v[] = {1, 3, 3, 5, 7, 7, 7, 9};
    int n = sizeof(v) / sizeof(v[0]);

    printf("+-----+-------------+-------------+\n");
    printf("|  x  | lower_bound | upper_bound |\n");
    printf("+-----+-------------+-------------+\n");

    int canTim[] = {1, 3, 4, 7, 9, 10};
    for (int k = 0; k < 6; k++) {
        int x = canTim[k];
        printf("| %-3d |      %d      |      %d      |\n",
               x, lower_bound(v, n, x), upper_bound(v, n, x));
    }
    printf("+-----+-------------+-------------+\n");
    return 0;
}
```

Output:

```
+-----+-------------+-------------+
|  x  | lower_bound | upper_bound |
+-----+-------------+-------------+
| 1   |      0      |      1      |
| 3   |      1      |      3      |
| 4   |      3      |      3      |
| 7   |      4      |      7      |
| 9   |      7      |      8      |
| 10  |      8      |      8      |
+-----+-------------+-------------+
```

**Phân biệt cốt lõi:**

```
Mang:   1   3   3   5   7   7   7   9
Index:  0   1   2   3   4   5   6   7

x = 3:
        lower_bound = 1  (phan tu DAU TIEN >= 3)
        upper_bound = 3  (phan tu DAU TIEN > 3)

        1  [3   3]  5   7   7   7   9
            ^       ^
            1       3
```

💡 Khi `x` **không tồn tại**, `lower_bound == upper_bound`.

💡 Hai hàm chỉ khác nhau đúng **một ký tự**: `a[m] < x` và `a[m] <= x`.

### Bài 4.

```c
#include <stdio.h>

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int upper_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] <= x) l = m + 1; else r = m;
    }
    return l;
}

int demSoLan(const int a[], int n, int x) {
    return upper_bound(a, n, x) - lower_bound(a, n, x);
}

// Dem tuyen tinh de kiem chung
int demTuyenTinh(const int a[], int n, int x) {
    int dem = 0;
    for (int i = 0; i < n; i++) if (a[i] == x) dem++;
    return dem;
}

int main(void) {
    int v[] = {1, 3, 3, 5, 7, 7, 7, 9, 9};
    int n = sizeof(v) / sizeof(v[0]);

    int canTim[] = {3, 7, 9, 1, 4};
    for (int k = 0; k < 5; k++) {
        int x = canTim[k];
        printf("So %d xuat hien %d lan  (kiem chung: %d)\n",
               x, demSoLan(v, n, x), demTuyenTinh(v, n, x));
    }
    return 0;
}
```

Output:

```
So 3 xuat hien 2 lan  (kiem chung: 2)
So 7 xuat hien 3 lan  (kiem chung: 3)
So 9 xuat hien 2 lan  (kiem chung: 2)
So 1 xuat hien 1 lan  (kiem chung: 1)
So 4 xuat hien 0 lan  (kiem chung: 0)
```

💡 **Độ phức tạp O(log n)** — nhanh hơn hẳn đếm tuyến tính (O(n)) khi mảng đã sắp xếp.

### Bài 5.

```c
#include <stdio.h>

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

// Doan cac phan tu bang x la [*dau, *cuoi)
void equal_range(const int a[], int n, int x, int *dau, int *cuoi) {
    *dau = lower_bound(a, n, x);
    // upper_bound chi can tim tu *dau tro di
    int l = *dau, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] <= x) l = m + 1; else r = m;
    }
    *cuoi = l;
}

int main(void) {
    int v[] = {1, 3, 3, 5, 7, 7, 7, 9};
    int n = sizeof(v) / sizeof(v[0]);

    int canTim[] = {3, 7, 4};
    for (int k = 0; k < 3; k++) {
        int x = canTim[k], dau, cuoi;
        equal_range(v, n, x, &dau, &cuoi);

        printf("equal_range(%d):\n", x);
        printf("  Vi tri  : [%d, %d)\n", dau, cuoi);
        printf("  So luong: %d\n", cuoi - dau);
        printf("  Cac phan tu: ");
        for (int i = dau; i < cuoi; i++) printf("%d ", v[i]);
        if (dau == cuoi) printf("(khong co)");
        printf("\n\n");
    }
    return 0;
}
```

Output:

```
equal_range(3):
  Vi tri  : [1, 3)
  So luong: 2
  Cac phan tu: 3 3 

equal_range(7):
  Vi tri  : [4, 7)
  So luong: 3
  Cac phan tu: 7 7 7 

equal_range(4):
  Vi tri  : [3, 3)
  So luong: 0
  Cac phan tu: (khong co)
```

💡 C không trả về được 2 giá trị, nên hàm ghi kết quả qua **2 con trỏ** `dau`, `cuoi`.

💡 Tìm `cuoi` bắt đầu từ `*dau` thay vì từ 0 — tiết kiệm được một ít phép so sánh vì `upper_bound` chắc chắn ≥ `lower_bound`.

### Bài 6.

```c
#include <stdio.h>

#define MAX 20

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

// Chen x vao mang tang dan a[] (dang co *n phan tu), giu thu tu. Tra ve vi tri chen
int chenCoThuTu(int a[], int *n, int x) {
    int vt = lower_bound(a, *n, x);
    for (int i = *n; i > vt; i--) a[i] = a[i - 1];   // dich sang phai 1 o
    a[vt] = x;
    (*n)++;
    return vt;
}

void in(const int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int goc[] = {1, 3, 5, 7, 9};

    printf("Mang ban dau: ");
    in(goc, 5);

    int canChen[] = {4, 0, 10, 5};
    for (int k = 0; k < 4; k++) {
        int tam[MAX], n = 5;
        for (int i = 0; i < n; i++) tam[i] = goc[i];
        int vt = chenCoThuTu(tam, &n, canChen[k]);
        printf("Chen %d vao vi tri %d: ", canChen[k], vt);
        in(tam, n);
    }

    // Duy tri mang luon sap xep khi them nhieu phan tu
    int v[MAX] = {1, 3, 5, 7, 9}, n = 5;
    int them[] = {6, 2, 8};
    printf("\nThem lien tiep 6, 2, 8 vao mang goc:\n");
    for (int k = 0; k < 3; k++) {
        if (n == MAX) break;                  // het cho
        chenCoThuTu(v, &n, them[k]);
        printf("  Sau khi them %d: ", them[k]);
        in(v, n);
    }
    return 0;
}
```

Output:

```
Mang ban dau: 1 3 5 7 9 
Chen 4 vao vi tri 2: 1 3 4 5 7 9 
Chen 0 vao vi tri 0: 0 1 3 5 7 9 
Chen 10 vao vi tri 5: 1 3 5 7 9 10 
Chen 5 vao vi tri 2: 1 3 5 5 7 9 

Them lien tiep 6, 2, 8 vao mang goc:
  Sau khi them 6: 1 3 5 6 7 9 
  Sau khi them 2: 1 2 3 5 6 7 9 
  Sau khi them 8: 1 2 3 5 6 7 8 9 
```

💡 **Đây là ứng dụng quan trọng của `lower_bound`:** duy trì một mảng **luôn được sắp xếp** khi thêm phần tử, mà không phải sắp xếp lại toàn bộ.

⚠️ Tuy việc **tìm vị trí** là O(log n), nhưng việc **dịch các phần tử** phía sau vẫn là O(n). Mảng cũng phải được khai báo **đủ chỗ trống** (`MAX`) — kiểm tra trước khi chèn để không ghi ra ngoài mảng.

### Bài 7.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

// Tra ve chi so DAU TIEN cua x, hoac -1
int timViTriDau(const int a[], int n, int x) {
    int vt = lower_bound(a, n, x);
    if (vt < n && a[vt] == x) return vt;
    return -1;
}

int main(void) {
    int v[] = {1, 5, 5, 5, 5, 5, 9};
    int n = sizeof(v) / sizeof(v[0]);
    int x = 5;

    // bsearch: tim thay MOT phan tu bang 5, nhung khong biet la phan tu nao
    int *p = bsearch(&x, v, n, sizeof(int), cmpInt);
    if (p != NULL) printf("bsearch(5)     -> chi so %d\n", (int)(p - v));

    // lower_bound + kiem tra: chac chan la vi tri DAU TIEN
    printf("timViTriDau(5) -> chi so %d\n", timViTriDau(v, n, 5));
    printf("timViTriDau(6) -> chi so %d\n", timViTriDau(v, n, 6));
    return 0;
}
```

Kết quả tham khảo:

```
bsearch(5)     -> chi so 3
timViTriDau(5) -> chi so 1
timViTriDau(6) -> chi so -1
```

**Vì sao `bsearch` trả về con trỏ:**

- `bsearch` là hàm **tổng quát**, làm việc với mảng **mọi kiểu dữ liệu** qua `void *`. Trả về con trỏ tới chính phần tử tìm được cho phép bạn **đọc/sửa ngay** phần tử đó (ví dụ cả một struct), không cần biết kiểu của mảng.
- Con trỏ có một giá trị đặc biệt là **`NULL`** để báo "không tìm thấy" — rất tự nhiên trong C.
- Cần chỉ số thì chỉ việc trừ con trỏ: `p - a`.

**Khi có nhiều phần tử bằng nhau:** chuẩn C chỉ nói `bsearch` trả về **một** phần tử khớp, **không quy định** là phần tử nào. Ở ví dụ trên nó trả về chỉ số 3 (phần tử giữa mảng được xét đầu tiên), nhưng thư viện khác có thể trả về chỉ số khác.

**Công thức lấy vị trí đầu tiên:**

```c
int vt = lower_bound(a, n, x);
int timThay = (vt < n && a[vt] == x);
int viTri = timThay ? vt : -1;
```

⚠️ **Bắt buộc kiểm tra CẢ HAI điều kiện:** `vt < n` (không vượt biên) **và** `a[vt] == x` (đúng giá trị cần tìm).

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int timGanNhat(const int v[], int n, int x) {
    if (n == 0) return -1;

    int vt = lower_bound(v, n, x);

    // Truong hop 1: x lon hon moi phan tu
    if (vt == n) return n - 1;

    // Truong hop 2: x nho hon hoac bang phan tu dau
    if (vt == 0) return 0;

    // Truong hop 3: so sanh phan tu tai vt va phan tu TRUOC no
    long long kcSau   = llabs((long long)v[vt] - x);
    long long kcTruoc = llabs((long long)v[vt - 1] - x);

    return (kcTruoc <= kcSau) ? vt - 1 : vt;
}

int main(void) {
    int v[] = {1, 5, 10, 15, 20, 30};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);
    printf("\n\n");

    int canTim[] = {0, 3, 7, 12, 25, 100};
    for (int k = 0; k < 6; k++) {
        int x = canTim[k];
        int vt = timGanNhat(v, n, x);
        printf("Gan %d nhat: %d (vi tri %d, cach %d)\n", x, v[vt], vt, abs(v[vt] - x));
    }
    return 0;
}
```

Output:

```
Gan 0 nhat: 1 (vi tri 0, cach 1)
Gan 3 nhat: 1 (vi tri 0, cach 2)
Gan 7 nhat: 5 (vi tri 1, cach 2)
Gan 12 nhat: 10 (vi tri 2, cach 2)
Gan 25 nhat: 20 (vi tri 4, cach 5)
Gan 100 nhat: 30 (vi tri 5, cach 70)
```

💡 **Độ phức tạp O(log n)** — tốt hơn nhiều so với duyệt tuyến tính O(n).

**Ý tưởng:** `lower_bound` cho ta ranh giới — phần tử gần nhất chỉ có thể là phần tử **tại ranh giới** hoặc **ngay trước nó**.

⚠️ Phải xử lý 2 trường hợp biên: `vt == n` và `vt == 0`.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>

// Mang GIAM DAN: "dung truoc" nghia la LON hon
// lower_bound giam: chi so dau tien co a[i] <= x
int lower_bound_giam(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] > x) l = m + 1; else r = m;
    }
    return l;
}

// upper_bound giam: chi so dau tien co a[i] < x
int upper_bound_giam(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] >= x) l = m + 1; else r = m;
    }
    return l;
}

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int cmpGiam(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x < y) - (x > y);
}

int main(void) {
    int v[] = {9, 7, 7, 5, 3, 3, 1};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Mang (giam dan): ");
    for (int i = 0; i < n; i++) printf("%d(%d) ", v[i], i);
    printf("\n\n");

    int canTim[] = {7, 5, 4};
    for (int k = 0; k < 3; k++) {
        int x = canTim[k];
        int lb = lower_bound_giam(v, n, x), ub = upper_bound_giam(v, n, x);
        printf("x = %d: lower_bound = %d, upper_bound = %d, so luong = %d\n",
               x, lb, ub, ub - lb);
    }

    // bsearch cung PHAI dung ham so sanh giam dan
    int x = 1;
    printf("\nbsearch(1, cmpGiam) = %s\n",
           bsearch(&x, v, n, sizeof(int), cmpGiam) ? "FOUND" : "NOT FOUND");
    printf("bsearch(1, cmpTang) = %s  <- SAI!\n",
           bsearch(&x, v, n, sizeof(int), cmpTang) ? "FOUND" : "NOT FOUND");
    return 0;
}
```

Output:

```
x = 7: lower_bound = 1, upper_bound = 3, so luong = 2
x = 5: lower_bound = 3, upper_bound = 4, so luong = 1
x = 4: lower_bound = 4, upper_bound = 4, so luong = 0

bsearch(1, cmpGiam) = FOUND
bsearch(1, cmpTang) = NOT FOUND  <- SAI!
```

⚠️ **Quy tắc bắt buộc: hàm so sánh dùng cho `bsearch` phải GIỐNG HỆT hàm so sánh đã dùng khi `qsort`.** Nếu mảng được sắp giảm dần bằng `cmpGiam` thì `bsearch` cũng phải dùng `cmpGiam`.

**Ý nghĩa với thứ tự giảm dần:**
- `lower_bound_giam` → phần tử đầu tiên **không lớn hơn** `x` (tức ≤ `x`)
- `upper_bound_giam` → phần tử đầu tiên **nhỏ hơn** `x`

💡 Chỉ cần **đảo dấu so sánh** trong thân vòng lặp: `<` thành `>`, `<=` thành `>=`.

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int  ma;
    char ten[20];
} SinhVien;

// So sanh theo MA - dung cho ca qsort va bsearch
int cmpMa(const void *a, const void *b) {
    const SinhVien *x = a, *y = b;
    return (x->ma > y->ma) - (x->ma < y->ma);
}

int main(void) {
    SinhVien ds[] = {
        {107, "Dung"}, {101, "An"}, {109, "Em"},
        {103, "Binh"}, {105, "Chi"}
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(SinhVien), cmpMa);      // sap xep theo ma truoc

    int canTim[] = {105, 104};
    for (int k = 0; k < 2; k++) {
        SinhVien khoa = { .ma = canTim[k] };    // chi can dien truong ma
        SinhVien *p = bsearch(&khoa, ds, n, sizeof(SinhVien), cmpMa);
        if (p != NULL) printf("Ma %d: %s (chi so %d)\n", p->ma, p->ten, (int)(p - ds));
        else           printf("Ma %d: khong tim thay\n", canTim[k]);
    }
    return 0;
}
```

Output:

```
Ma 105: Chi (chi so 2)
Ma 104: khong tim thay
```

💡 **Mẹo tạo "khoá":** tạo một biến struct tạm chỉ điền trường `ma`, để dùng **chung một hàm so sánh** cho cả `qsort` lẫn `bsearch`.

💡 Cách khác: truyền thẳng `&ma` (kiểu `int *`) làm `key` và viết hàm so sánh riêng cho `bsearch` với tham số đầu là `int *`, tham số sau là `SinhVien *` — vì `bsearch` luôn gọi `cmp(key, phần_tử)`:

```c
int cmpKhoaMa(const void *key, const void *elem) {
    int ma = *(const int *)key;
    const SinhVien *sv = elem;
    return (ma > sv->ma) - (ma < sv->ma);
}
// bsearch(&ma, ds, n, sizeof(SinhVien), cmpKhoaMa);
```

### Bài 11.

```c
#include <stdio.h>

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int upper_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] <= x) l = m + 1; else r = m;
    }
    return l;
}

int demTrongKhoang(const int v[], int n, int a, int b) {
    if (a > b) return 0;
    return upper_bound(v, n, b) - lower_bound(v, n, a);
}

int main(void) {
    int v[] = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
    int n = sizeof(v) / sizeof(v[0]);

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d ", v[i]);
    printf("\n\n");

    struct { int a, b; } bo[] = {{5, 11}, {1, 19}, {6, 8}, {20, 30}, {0, 4}};

    for (int k = 0; k < 5; k++) {
        int a = bo[k].a, b = bo[k].b;
        int dem = demTrongKhoang(v, n, a, b);
        printf("Trong khoang [%d, %d]: %d phan tu", a, b, dem);
        if (dem > 0) {
            printf("  ->  ");
            for (int i = lower_bound(v, n, a); i < upper_bound(v, n, b); i++)
                printf("%d ", v[i]);
        }
        printf("\n");
    }
    return 0;
}
```

Output:

```
Trong khoang [5, 11]: 4 phan tu  ->  5 7 9 11 
Trong khoang [1, 19]: 10 phan tu  ->  1 3 5 7 9 11 13 15 17 19 
Trong khoang [6, 8]: 1 phan tu  ->  7 
Trong khoang [20, 30]: 0 phan tu
Trong khoang [0, 4]: 2 phan tu  ->  1 3 
```

💡 **Công thức vàng:** số phần tử trong `[a, b]` = `upper_bound(b) - lower_bound(a)`

Độ phức tạp **O(log n)** — cực kỳ hữu ích khi có nhiều truy vấn khoảng.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Mang cac CON TRO chuoi: moi phan tu co kieu const char *
// -> tham so cua ham so sanh la con tro TOI con tro chuoi (const char * const *)
int cmpChuoi(const void *a, const void *b) {
    const char *x = *(const char * const *)a;
    const char *y = *(const char * const *)b;
    return strcmp(x, y);
}

int main(void) {
    const char *tuDien[] = {
        "banana", "apple", "mango", "cherry", "grape", "kiwi", "orange"
    };
    int n = sizeof(tuDien) / sizeof(tuDien[0]);

    qsort(tuDien, n, sizeof(tuDien[0]), cmpChuoi);   // sap theo tu dien

    printf("Tu dien: ");
    for (int i = 0; i < n; i++) printf("%s ", tuDien[i]);
    printf("\n\n");

    const char *canTim[] = {"kiwi", "lemon", "apple"};
    for (int k = 0; k < 3; k++) {
        const char *key = canTim[k];
        const char **p = bsearch(&key, tuDien, n, sizeof(tuDien[0]), cmpChuoi);
        if (p != NULL) printf("\"%s\" : co, chi so %d\n", key, (int)(p - tuDien));
        else           printf("\"%s\" : khong co\n", key);
    }
    return 0;
}
```

Output:

```
Tu dien: apple banana cherry grape kiwi mango orange 

"kiwi" : co, chi so 4
"lemon" : khong co
"apple" : co, chi so 0
```

⚠️ **Lỗi rất hay gặp:** phần tử của mảng là `const char *`, nên `qsort`/`bsearch` truyền vào hàm so sánh **địa chỉ của phần tử**, tức là `const char **`. Phải giải tham chiếu một lần (`*(const char * const *)a`) mới được chuỗi. Viết `strcmp(a, b)` trực tiếp là **sai**.

⚠️ Vì thế `key` cũng phải là **địa chỉ của một con trỏ chuỗi** (`&key`), cùng dạng với phần tử trong mảng.

### Bài 13.

```c
int a[] = {5, 2, 8, 1, 9};              // CHUA SAP XEP!
int x = 1;
int *p = bsearch(&x, a, 5, sizeof(int), cmp);
printf("%s\n", p ? "FOUND" : "NOT FOUND");
```

**Lỗi: mảng CHƯA được sắp xếp.**

`bsearch` (cũng như `lower_bound`, `upper_bound`) **giả định** mảng đã sắp xếp. Với mảng chưa sắp, kết quả là **không xác định** — có thể trả về `NULL` dù phần tử thực sự tồn tại, và **không có cảnh báo nào**.

**Quá trình tìm nhị phân với `{5, 2, 8, 1, 9}` tìm `1`** (một cách cài đặt điển hình):

```
trai=0, phai=4 -> giua=2, a[2]=8 > 1 -> sang trai
trai=0, phai=1 -> giua=0, a[0]=5 > 1 -> sang trai
Het -> NULL  <- SAI! So 1 co trong mang (chi so 3)
```

**Sửa:**

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int main(void) {
    int a[] = {5, 2, 8, 1, 9};
    int n = 5;

    qsort(a, n, sizeof(int), cmp);          // <- SAP XEP TRUOC, cung ham cmp

    printf("Mang sau sap xep: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    int canTim[] = {1, 8, 3};
    for (int k = 0; k < 3; k++) {
        int x = canTim[k];
        int *p = bsearch(&x, a, n, sizeof(int), cmp);
        printf("bsearch(%d) = %s\n", x, p ? "FOUND" : "NOT FOUND");
    }
    return 0;
}
```

Output:

```
Mang sau sap xep: 1 2 5 8 9 
bsearch(1) = FOUND
bsearch(8) = FOUND
bsearch(3) = NOT FOUND
```

💡 **Cách phòng tránh: kiểm tra mảng đã sắp xếp trước khi tìm** (ít nhất trong lúc phát triển):

```c
#include <assert.h>

int daSapXep(const int a[], int n) {
    for (int i = 1; i < n; i++) if (a[i - 1] > a[i]) return 0;
    return 1;
}
// assert(daSapXep(a, n));
```

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100000
#define SO_TRUY_VAN 1000000

int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int lower_bound(const int a[], int n, int x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] < x) l = m + 1; else r = m;
    }
    return l;
}

int timTuyenTinh(const int a[], int n, int x) {
    for (int i = 0; i < n; i++) if (a[i] == x) return 1;
    return 0;
}

double msTu(clock_t t) { return (double)(clock() - t) * 1000 / CLOCKS_PER_SEC; }

int main(void) {
    static int v[N];
    for (int i = 0; i < N; i++) v[i] = i * 2;           // mang tang dan

    long long dem;
    clock_t t;

    // (1) Tuyen tinh - O(n): chi chay 1/100 so truy van vi qua cham
    dem = 0; t = clock();
    for (int k = 0; k < SO_TRUY_VAN / 100; k++)
        dem += timTuyenTinh(v, N, (int)(k * 7LL % (2 * N)));
    printf("Tuyen tinh (uoc luong): %8.0f ms  (dem %lld)\n", msTu(t) * 100, dem);

    // (2) bsearch - O(log n)
    dem = 0; t = clock();
    for (int k = 0; k < SO_TRUY_VAN; k++) {
        int x = (int)(k * 7LL % (2 * N));
        if (bsearch(&x, v, N, sizeof(int), cmpInt) != NULL) dem++;
    }
    printf("bsearch               : %8.0f ms  (dem %lld)\n", msTu(t), dem);

    // (3) lower_bound tu viet - O(log n)
    dem = 0; t = clock();
    for (int k = 0; k < SO_TRUY_VAN; k++) {
        int x = (int)(k * 7LL % (2 * N));
        int vt = lower_bound(v, N, x);
        if (vt < N && v[vt] == x) dem++;
    }
    printf("lower_bound tu viet   : %8.0f ms  (dem %lld)\n", msTu(t), dem);
    return 0;
}
```

Kết quả tham khảo (biên dịch với `-O2`):

```
Tuyen tinh (uoc luong):    15304 ms  (dem 5000)
bsearch               :       53 ms  (dem 500000)
lower_bound tu viet   :       57 ms  (dem 500000)
```

**Bảng so sánh:**

| Phương pháp | Độ phức tạp | Cần sắp xếp | Kết quả | Ghi chú |
|---|---|---|---|---|
| Tuyến tính | O(n) | ❌ Không | Có / không, vị trí | Chỉ dùng khi n nhỏ hoặc tìm ít lần |
| **`bsearch`** | O(log n) | ✅ **Có** | Con trỏ hoặc `NULL` | Có sẵn, dùng cho **mọi kiểu** qua `void *` |
| **`lower_bound` tự viết** | O(log n) | ✅ **Có** | Chỉ số đầu tiên ≥ x | Trả về **vị trí**, dùng được để đếm, tìm khoảng |

💡 `bsearch` và `lower_bound` tự viết có tốc độ **tương đương** (cùng O(log n), khoảng 17 bước với n = 10⁵): `bsearch` phải gọi hàm so sánh qua **con trỏ hàm** ở mỗi bước, còn `lower_bound` luôn đi đủ log n bước mà không dừng sớm khi gặp phần tử bằng. Con số cụ thể phụ thuộc máy và trình biên dịch. Còn tìm tuyến tính chậm hơn **hàng trăm lần**.

✅ **Khuyến nghị:**
- Dữ liệu **cố định**, tra cứu nhiều → sắp xếp **một lần** bằng `qsort` + tìm nhị phân
- Chỉ cần biết **có/không** trên mảng bất kỳ kiểu nào → `bsearch`
- Cần **vị trí đầu/cuối**, **đếm**, **đếm trong khoảng** → `lower_bound` / `upper_bound`

### Bài 15.

```c
#include <stdio.h>

#define SO_MUC 6

// upper_bound tren mang double: chi so dau tien co a[i] > x
int upper_bound_d(const double a[], int n, double x) {
    int l = 0, r = n;
    while (l < r) {
        int m = l + (r - l) / 2;
        if (a[m] <= x) l = m + 1; else r = m;
    }
    return l;
}

void xoaBoDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}

int main(void) {
    // Bang nguong xep loai (PHAI sap xep TANG DAN)
    const double nguong[SO_MUC]  = {0.0, 3.5, 5.0, 6.5, 8.0, 9.0};
    const char  *xepLoai[SO_MUC] = {"Kem", "Yeu", "Trung binh", "Kha", "Gioi", "Xuat sac"};

    // Hien bang quy dinh
    printf("=== BANG QUY DOI XEP LOAI ===\n");
    printf("+----------------+---------------+\n");
    printf("| KHOANG DIEM    | XEP LOAI      |\n");
    printf("+----------------+---------------+\n");
    for (int i = 0; i < SO_MUC; i++) {
        double tren = (i + 1 < SO_MUC) ? nguong[i + 1] : 10.0;
        printf("| %4.1f - %-7.1f | %-13s |\n", nguong[i], tren, xepLoai[i]);
    }
    printf("+----------------+---------------+\n");

    // Tra cuu
    printf("\nNhap diem de tra cuu (nhap -1 de thoat):\n");
    double diem;

    while (1) {
        printf("\nDiem: ");
        int kq = scanf("%lf", &diem);
        if (kq == EOF) break;
        if (kq != 1) {
            xoaBoDem();
            printf("  -> Nhap khong hop le!\n");
            continue;
        }

        if (diem < 0) break;
        if (diem > 10) { printf("  -> Diem phai tu 0 den 10!\n"); continue; }

        // upper_bound tra ve nguong DAU TIEN > diem
        // Lui lai 1 buoc -> nguong lon nhat <= diem
        int chiSo = upper_bound_d(nguong, SO_MUC, diem) - 1;
        if (chiSo < 0) chiSo = 0;

        printf("  -> Diem %.2f xep loai: %s\n", diem, xepLoai[chiSo]);
    }

    printf("\nTam biet!\n");
    return 0;
}
```

Ví dụ chạy:

```
Diem: 8.5
  -> Diem 8.50 xep loai: Gioi

Diem: 9.0
  -> Diem 9.00 xep loai: Xuat sac

Diem: 6.4
  -> Diem 6.40 xep loai: Trung binh

Diem: 0
  -> Diem 0.00 xep loai: Kem
```

**Kỹ thuật "tra bảng ngưỡng" bằng `upper_bound`:**

```
nguong:  0.0   3.5   5.0   6.5   8.0   9.0
index:    0     1     2     3     4     5
loai:   Kem   Yeu   TB    Kha  Gioi  Xuat sac

diem = 8.5:
  upper_bound(8.5) -> tro toi 9.0 (index 5)
  lui 1 buoc -> index 4 -> "Gioi"
```

💡 **Ưu điểm so với chuỗi `if else if`:**
1. **Độ phức tạp O(log n)** thay vì O(n) — quan trọng khi có hàng trăm mức
2. **Dễ thay đổi:** chỉ cần sửa 2 mảng, không phải sửa logic
3. **Dữ liệu tách khỏi logic** — có thể đọc bảng ngưỡng từ file cấu hình

⚠️ `scanf` đọc `double` phải dùng `%lf` (còn `printf` in `double` dùng `%f`/`%.2f`).

Kỹ thuật này dùng rất nhiều trong thực tế: tính thuế thu nhập bậc thang, tính cước điện/nước, quy đổi điểm, phân loại BMI…
