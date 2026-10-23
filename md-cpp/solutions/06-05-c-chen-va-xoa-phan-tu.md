# Lời giải — [C]. Chèn Và Xóa Phần Tử

[← Quay lại bài học](../06-05-c-chen-va-xoa-phan-tu.md)

> **Nguyên lý cốt lõi:**
> - **Chèn** tại vị trí `k` → dịch các phần tử từ `k` trở đi **sang phải**, duyệt **từ cuối về `k`**
> - **Xoá** tại vị trí `k` → dịch các phần tử từ `k+1` trở đi **sang trái**, duyệt **từ `k` đến cuối**

---

### Bài 1.

```c
#include <stdio.h>

void chen(int a[], int *n, int k, int x) {
    if (k < 0 || k > *n) { printf("Vi tri khong hop le!\n"); return; }

    // Dich cac phan tu tu k tro di sang PHAI mot vi tri
    // Duyet TU CUOI VE DAU de khong ghi de du lieu
    for (int i = *n; i > k; i--) {
        a[i] = a[i - 1];
    }
    a[k] = x;
    (*n)++;
}

int main(void) {
    int a[100] = {10, 20, 30, 40, 50};
    int n = 5;

    chen(a, &n, 2, 99);

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                          // 10 20 99 30 40 50
    return 0;
}
```

⚠️ **Phải duyệt TỪ CUỐI VỀ ĐẦU.** Nếu duyệt xuôi:

```c
for (int i = k; i < n; i++) a[i + 1] = a[i];   // SAI!
// a[3] = a[2] -> 30 ghi de 40 (mat 40)
// a[4] = a[3] -> lai la 30, khong phai 40
// Ket qua: 10 20 30 30 30 30
```

⚠️ C không có tham chiếu: muốn hàm cập nhật được kích thước `n` ở hàm gọi, phải truyền **con trỏ** `int *n` (gọi `chen(a, &n, ...)`) và dùng `*n` bên trong hàm. Chú ý viết `(*n)++`, không viết `*n++` (sẽ tăng con trỏ chứ không tăng giá trị).

### Bài 2.

```c
#include <stdio.h>

void xoa(int a[], int *n, int k) {
    if (k < 0 || k >= *n) { printf("Vi tri khong hop le!\n"); return; }

    // Dich cac phan tu tu k+1 tro di sang TRAI
    // Duyet TU DAU VE CUOI
    for (int i = k; i < *n - 1; i++) {
        a[i] = a[i + 1];
    }
    (*n)--;
}

int main(void) {
    int a[100] = {10, 20, 30, 40, 50};
    int n = 5;

    xoa(a, &n, 1);

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                          // 10 30 40 50
    return 0;
}
```

⚠️ **Vòng lặp dừng ở `n - 1`**, không phải `n`. Nếu chạy tới `n` thì `a[i+1]` = `a[n]` là truy cập ngoài biên.

### Bài 3.

```c
#include <stdio.h>

void chen(int a[], int *n, int k, int x) {
    for (int i = *n; i > k; i--) a[i] = a[i - 1];
    a[k] = x;
    (*n)++;
}

void inMang(int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[100] = {10, 20, 30};
    int n = 3;

    printf("Ban dau   : "); inMang(a, n);

    chen(a, &n, 0, 5);          // chen vao DAU
    printf("Chen dau 5: "); inMang(a, n);

    chen(a, &n, n, 99);         // chen vao CUOI
    printf("Chen cuoi : "); inMang(a, n);
    return 0;
}
```

Output:

```
Ban dau   : 10 20 30 
Chen dau 5: 5 10 20 30 
Chen cuoi : 5 10 20 30 99 
```

💡 **Chèn cuối chỉ cần `a[n++] = x;`** — không phải dịch phần tử nào, O(1).
💡 **Chèn đầu phải dịch toàn bộ** — O(n), tốn kém nhất.

### Bài 4.

```c
#include <stdio.h>

void xoaTatCa(int a[], int *n, int x) {
    int j = 0;
    for (int i = 0; i < *n; i++) {
        if (a[i] != x) a[j++] = a[i];        // giu lai phan tu khac x
    }
    *n = j;
}

int main(void) {
    int a[100] = {1, 3, 2, 3, 4, 3, 5};
    int n = 7;

    xoaTatCa(a, &n, 3);

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf(" (n = %d)\n", n);                   // 1 2 4 5  (n = 4)
    return 0;
}
```

💡 **Kỹ thuật 2 con trỏ** — cách tối ưu nhất để xoá nhiều phần tử:
- `i` duyệt qua mọi phần tử
- `j` là vị trí tiếp theo để ghi phần tử được giữ lại

Độ phức tạp **O(n)** — duyệt đúng một lần. So với cách gọi hàm `xoa()` nhiều lần (O(n²)), đây là cải tiến rất lớn.

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    int a[100] = {3, -1, 5, -7, 2, -4, 8};
    int n = 7;

    int j = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] >= 0) a[j++] = a[i];
    }
    n = j;

    printf("Sau khi xoa so am: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                                 // 3 5 2 8
    return 0;
}
```

💡 Thư viện chuẩn C không có hàm kiểu "xoá theo điều kiện" — kỹ thuật 2 con trỏ ở trên chính là cách làm chuẩn.

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int a[100] = {1, 3, 1, 5, 3, 7, 5};
    int n = 7;

    int m = 0;
    for (int i = 0; i < n; i++) {
        bool daCo = false;
        for (int j = 0; j < m; j++) {
            if (a[j] == a[i]) { daCo = true; break; }
        }
        if (!daCo) a[m++] = a[i];
    }
    n = m;

    printf("Sau khi xoa trung lap: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                                 // 1 3 5 7
    return 0;
}
```

Độ phức tạp O(n²). Nếu các giá trị là số nguyên không âm và nhỏ, có cách O(n) dùng **mảng đánh dấu** (xem bài [06-06](../06-06-c-mang-danh-dau.md)):

```c
static bool daGap[1000001];      // gia tri trong [0, 10^6]
int m = 0;
for (int i = 0; i < n; i++)
    if (!daGap[a[i]]) { daGap[a[i]] = true; a[m++] = a[i]; }
n = m;
```

⚠️ Nếu mảng **đã sắp xếp**, các phần tử trùng nằm **kề nhau**, chỉ cần so với phần tử vừa giữ lại:

```c
int m = 0;
for (int i = 0; i < n; i++)
    if (m == 0 || a[i] != a[m - 1]) a[m++] = a[i];   // chi xoa trung KE NHAU
n = m;
```

### Bài 7.

```c
#include <stdio.h>

void chenGiuThuTu(int a[], int *n, int x) {
    // Tim vi tri chen: phan tu dau tien >= x
    int k = 0;
    while (k < *n && a[k] < x) k++;

    // Dich sang phai roi chen
    for (int i = *n; i > k; i--) a[i] = a[i - 1];
    a[k] = x;
    (*n)++;
}

int main(void) {
    int a[100] = {1, 3, 5, 7, 9};
    int n = 5;

    chenGiuThuTu(a, &n, 6);
    chenGiuThuTu(a, &n, 0);
    chenGiuThuTu(a, &n, 100);

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                       // 0 1 3 5 6 7 9 100
    return 0;
}
```

💡 Có thể dùng **tìm kiếm nhị phân** để tìm vị trí chèn nhanh hơn (O(log n) thay vì O(n)):

```c
int lo = 0, hi = n;                 // tim phan tu dau tien >= x
while (lo < hi) {
    int mid = lo + (hi - lo) / 2;
    if (a[mid] < x) lo = mid + 1;
    else hi = mid;
}
int k = lo;
```

Nhưng phần **dịch phần tử** vẫn là O(n), nên tổng thể vẫn O(n).

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    int a[100] = {1, 2, 3, 4, 5};
    int n = 5;

    // Duyet TU CUOI VE DAU de khong bi lap vo han
    for (int i = n - 1; i >= 0; i--) {
        if (a[i] % 2 == 0) {
            // Chen 0 vao vi tri i+1
            for (int j = n; j > i + 1; j--) a[j] = a[j - 1];
            a[i + 1] = 0;
            n++;
        }
    }

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                       // 1 2 0 3 4 0 5
    return 0;
}
```

⚠️ **Phải duyệt từ cuối về đầu.** Nếu duyệt xuôi, sau khi chèn 0 thì các chỉ số phía sau bị dịch, vòng lặp sẽ xét lại phần tử đã xử lý và chèn lặp vô hạn (số 0 là số chẵn!).

Đây là quy tắc chung: **khi vừa duyệt vừa chèn, hãy duyệt ngược.**

### Bài 9.

```c
#include <stdio.h>

void xoaNhieu(int a[], int *n, int p, int k) {
    if (p < 0 || p >= *n || k <= 0) return;
    if (p + k > *n) k = *n - p;            // cat bot neu vuot qua

    for (int i = p; i < *n - k; i++) {
        a[i] = a[i + k];
    }
    *n -= k;
}

int main(void) {
    int a[100] = {10, 20, 30, 40, 50, 60, 70};
    int n = 7;

    xoaNhieu(a, &n, 2, 3);                 // xoa 3 phan tu tu vi tri 2

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                          // 10 20 60 70
    return 0;
}
```

💡 Xoá `k` phần tử cùng lúc chỉ cần **một lần duyệt** — nhanh hơn nhiều so với gọi hàm xoá 1 phần tử `k` lần.

### Bài 10.

```c
for (int i = k; i < n; i++) a[i] = a[i + 1];   // LOI: truy cap ngoai bien
n--;
```

**Lỗi:** khi `i = n - 1`, câu lệnh trở thành `a[n-1] = a[n]` — truy cập `a[n]` là **ngoài biên** mảng.

Với mảng tĩnh cỡ lớn (`int a[100]` mà `n = 5`), lỗi này thường **không gây crash** và giá trị đọc được là rác — nhưng nó bị ghi vào `a[n-1]` rồi lại bị `n--` bỏ đi, nên **kết quả tình cờ vẫn đúng**. Đây là loại lỗi nguy hiểm vì khó phát hiện.

Nếu `n` đúng bằng kích thước mảng, chương trình sẽ đọc vào vùng nhớ không thuộc mảng → hành vi không xác định (undefined behavior), có thể crash.

**Sửa:**

```c
for (int i = k; i < n - 1; i++) a[i] = a[i + 1];
n--;
```

💡 Biên dịch với `gcc -fsanitize=address` sẽ phát hiện ngay lỗi này.

### Bài 11.

```c
for (int i = 0; i < n; i++) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
        // THIEU: i--;
    }
}
```

**Lỗi:** sau khi xoá phần tử tại vị trí `i`, phần tử kế tiếp **đã dịch vào chính vị trí `i`**. Nhưng vòng lặp vẫn tăng `i++`, nên phần tử mới này bị **bỏ qua**.

Ví dụ với `{-1, -2, 3}`:

```
i=0: a[0]=-1 am -> xoa -> mang thanh {-2, 3}, n=2
i=1: xet a[1]=3 (khong am)      <- BO SOT a[0] = -2!
Ket qua: {-2, 3}  -- con sot so am
```

**Sửa cách 1 — giảm `i` sau khi xoá:**

```c
for (int i = 0; i < n; i++) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
        i--;                     // <- lui lai de xet lai vi tri nay
    }
}
```

**Sửa cách 2 — duyệt ngược (không cần chỉnh `i`):**

```c
for (int i = n - 1; i >= 0; i--) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
    }
}
```

**Sửa cách 3 — kỹ thuật 2 con trỏ (TỐT NHẤT, O(n)):**

```c
int j = 0;
for (int i = 0; i < n; i++)
    if (a[i] >= 0) a[j++] = a[i];
n = j;
```

Cách 1 và 2 là **O(n²)**; cách 3 là **O(n)**.

### Bài 12.

```c
#include <stdio.h>

int main(void) {
    int a[100] = {1, 2, 3};
    int n = 3;
    int b[] = {7, 8, 9, 10};
    int m = 4;

    // Cach don gian: noi B vao cuoi A
    for (int i = 0; i < m; i++) {
        a[n++] = b[i];
    }

    printf("Sau khi gop: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                       // 1 2 3 7 8 9 10

    // Cach xen ke: chen tung phan tu cua B vao vi tri le cua A
    int c[100] = {1, 2, 3};
    int nc = 3;
    int d[] = {7, 8, 9};
    int md = 3;

    for (int i = 0; i < md; i++) {
        int vt = 2 * i + 1;
        if (vt > nc) vt = nc;
        for (int j = nc; j > vt; j--) c[j] = c[j - 1];
        c[vt] = d[i];
        nc++;
    }

    printf("Gop xen ke : ");
    for (int i = 0; i < nc; i++) printf("%d ", c[i]);
    printf("\n");                       // 1 7 2 8 3 9
    return 0;
}
```

### Bài 13.

| Thao tác | Độ phức tạp | Số phần tử phải dịch |
|---|---|---|
| **Chèn vào cuối** | **O(1)** | 0 |
| **Xoá ở cuối** | **O(1)** | 0 |
| Chèn vào giữa (vị trí `k`) | O(n−k) | n−k |
| Xoá ở giữa | O(n−k) | n−k−1 |
| **Chèn vào đầu** | **O(n)** | n (toàn bộ) |
| **Xoá ở đầu** | **O(n)** | n−1 (gần toàn bộ) |

**Vì sao có sự khác biệt:** mảng lưu các phần tử **liên tiếp nhau trong bộ nhớ**. Đây là lý do truy cập `a[i]` cực nhanh (O(1) — chỉ cần tính địa chỉ), nhưng cũng là lý do chèn/xoá ở giữa phải **dịch chuyển vật lý** mọi phần tử phía sau.

```
Chen vao dau:  [1][2][3][4][ ]
                 \  \  \  \      <- tat ca phai dich 1 o
               [x][1][2][3][4]

Chen vao cuoi: [1][2][3][4][ ]
                            |    <- chi ghi 1 o
               [1][2][3][4][x]
```

💡 **Hệ quả thiết kế** (trong C bạn phải tự cài đặt các cấu trúc này):
- Cần chèn/xoá **ở cuối** nhiều → mảng động với `realloc` tăng gấp đôi sức chứa (O(1) trung bình)
- Cần chèn/xoá **ở cả hai đầu** nhiều → mảng vòng (circular buffer)
- Cần chèn/xoá **ở giữa** nhiều → danh sách liên kết (O(1) nếu đã có con trỏ tới nút)

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>

// Mang dong: con tro du lieu + so phan tu + suc chua
typedef struct {
    int *data;
    int n;
    int cap;
} MangDong;

// Dam bao con cho cho them 1 phan tu; tra ve 0 neu het bo nho
int damBaoSucChua(MangDong *m) {
    if (m->n < m->cap) return 1;
    int capMoi = (m->cap == 0) ? 4 : m->cap * 2;
    int *p = realloc(m->data, capMoi * sizeof(int));
    if (p == NULL) return 0;
    m->data = p;
    m->cap = capMoi;
    return 1;
}

// Bai 1: chen x vao vi tri k
int chen(MangDong *m, int k, int x) {
    if (k < 0 || k > m->n || !damBaoSucChua(m)) return 0;
    for (int i = m->n; i > k; i--) m->data[i] = m->data[i - 1];
    m->data[k] = x;
    m->n++;
    return 1;
}

// Bai 2: xoa phan tu tai vi tri k
void xoa(MangDong *m, int k) {
    if (k < 0 || k >= m->n) return;
    for (int i = k; i < m->n - 1; i++) m->data[i] = m->data[i + 1];
    m->n--;
}

// Bai 4: xoa tat ca gia tri x
void xoaGiaTri(MangDong *m, int x) {
    int j = 0;
    for (int i = 0; i < m->n; i++)
        if (m->data[i] != x) m->data[j++] = m->data[i];
    m->n = j;
}

void inMang(const char *nhan, const MangDong *m) {
    printf("%s: ", nhan);
    for (int i = 0; i < m->n; i++) printf("%d ", m->data[i]);
    printf("(n = %d, cap = %d)\n", m->n, m->cap);
}

int main(void) {
    MangDong m = {NULL, 0, 0};
    int banDau[] = {10, 20, 30, 40, 50};
    for (int i = 0; i < 5; i++) chen(&m, m.n, banDau[i]);   // them vao cuoi
    inMang("Ban dau        ", &m);

    chen(&m, 2, 99);
    inMang("Sau chen       ", &m);

    xoa(&m, 1);
    inMang("Sau xoa        ", &m);

    xoaGiaTri(&m, 30);
    inMang("Sau xoa gia tri", &m);

    free(m.data);                  // giai phong bo nho khi dung xong
    return 0;
}
```

Output:

```
Ban dau        : 10 20 30 40 50 (n = 5, cap = 8)
Sau chen       : 10 20 99 30 40 50 (n = 6, cap = 8)
Sau xoa        : 10 99 30 40 50 (n = 5, cap = 8)
Sau xoa gia tri: 10 99 40 50 (n = 4, cap = 8)
```

**So sánh với mảng tĩnh:**

| Việc | Mảng tĩnh `int a[100]` | Mảng động (`malloc`/`realloc`) |
|---|---|---|
| Kích thước tối đa | Cố định lúc biên dịch | Tăng dần khi chạy |
| Vượt sức chứa | ⚠️ Ghi ra ngoài mảng, hành vi không xác định | ✅ Gọi `realloc` mở rộng |
| Giải phóng | Tự động | ⚠️ Phải tự gọi `free` |
| Thao tác chèn/xoá | Dịch phần tử | Vẫn dịch phần tử y hệt |

⚠️ Luôn gán kết quả `realloc` vào **biến tạm** rồi kiểm tra `NULL`: nếu gán thẳng `m->data = realloc(m->data, ...)` mà thất bại thì mất con trỏ cũ → rò rỉ bộ nhớ.

💡 Tăng sức chứa **gấp đôi** mỗi lần giúp chi phí thêm vào cuối trung bình chỉ O(1). Chi tiết về cấp phát động xem bài [07-04](../07-04-c-cap-phat-mang-dong.md).

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

int soSanhTang(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    return (x > y) - (x < y);
}

void hienMenu(void) {
    printf("\n====== QUAN LY DANH SACH ======\n");
    printf("1. Them vao cuoi\n");
    printf("2. Chen tai vi tri\n");
    printf("3. Xoa theo vi tri\n");
    printf("4. Xoa theo gia tri\n");
    printf("5. Hien thi danh sach\n");
    printf("6. Sap xep tang dan\n");
    printf("0. Thoat\n");
    printf("===============================\n");
    printf("Lua chon: ");
}

void hienThi(const int a[], int n) {
    if (n == 0) { printf(">> Danh sach RONG\n"); return; }
    printf(">> Danh sach (%d phan tu): ", n);
    for (int i = 0; i < n; i++) {
        printf("[%d]=%d ", i, a[i]);
    }
    printf("\n");
}

int main(void) {
    int a[MAX];
    int n = 0;
    int chon;

    do {
        hienMenu();
        if (scanf("%d", &chon) != 1) break;      // nhap sai kieu -> thoat

        switch (chon) {
            case 1: {
                if (n == MAX) { printf(">> Danh sach da day!\n"); break; }
                int x;
                printf("Nhap gia tri: "); scanf("%d", &x);
                a[n++] = x;
                printf(">> Da them %d vao cuoi\n", x);
                break;
            }
            case 2: {
                if (n == MAX) { printf(">> Danh sach da day!\n"); break; }
                int k, x;
                printf("Nhap vi tri (0..%d): ", n); scanf("%d", &k);
                if (k < 0 || k > n) {
                    printf(">> Vi tri khong hop le!\n");
                    break;
                }
                printf("Nhap gia tri: "); scanf("%d", &x);
                for (int i = n; i > k; i--) a[i] = a[i - 1];
                a[k] = x;
                n++;
                printf(">> Da chen %d vao vi tri %d\n", x, k);
                break;
            }
            case 3: {
                if (n == 0) { printf(">> Danh sach rong!\n"); break; }
                int k;
                printf("Nhap vi tri (0..%d): ", n - 1); scanf("%d", &k);
                if (k < 0 || k >= n) {
                    printf(">> Vi tri khong hop le!\n");
                    break;
                }
                printf(">> Da xoa gia tri %d\n", a[k]);
                for (int i = k; i < n - 1; i++) a[i] = a[i + 1];
                n--;
                break;
            }
            case 4: {
                int x;
                printf("Nhap gia tri can xoa: "); scanf("%d", &x);
                int truoc = n, j = 0;
                for (int i = 0; i < n; i++)
                    if (a[i] != x) a[j++] = a[i];
                n = j;
                printf(">> Da xoa %d phan tu\n", truoc - n);
                break;
            }
            case 5:
                hienThi(a, n);
                break;
            case 6:
                qsort(a, n, sizeof(int), soSanhTang);
                printf(">> Da sap xep\n");
                hienThi(a, n);
                break;
            case 0:
                printf(">> Tam biet!\n");
                break;
            default:
                printf(">> Lua chon khong hop le!\n");
        }
    } while (chon != 0);

    return 0;
}
```

**Các điểm đáng học:**

1. **Luôn kiểm tra `n == 0`** trước khi xoá và `n == MAX` trước khi thêm — tránh truy cập ngoài mảng
2. **Luôn kiểm tra biên** của vị trí người dùng nhập
3. **Kiểm tra giá trị trả về của `scanf`** — nếu người dùng gõ chữ, `scanf("%d")` trả về 0 và `chon` không được gán, vòng lặp có thể chạy mãi
4. Bọc `{ }` quanh các `case` có khai báo biến
