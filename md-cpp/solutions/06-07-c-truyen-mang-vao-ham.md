# Lời giải — [C]. Truyền Mảng Vào Hàm

[← Quay lại bài học](../06-07-c-truyen-mang-vao-ham.md)

> **Nguyên lý cốt lõi:**
> - Truyền mảng vào hàm thực chất là truyền **địa chỉ phần tử đầu tiên** → hàm sửa được mảng gốc
> - Luôn truyền kèm **số phần tử `n`**, không dùng `sizeof` bên trong hàm
> - Hàm chỉ đọc mảng thì khai báo `const int a[]`

---

### Bài 1.

```c
#include <stdio.h>

void xuatMang(const int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int tongMang(const int a[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5};
    int b[] = {10, -3, 7};
    int na = sizeof(a) / sizeof(a[0]);     // tinh o noi khai bao mang
    int nb = sizeof(b) / sizeof(b[0]);

    printf("Mang a: "); xuatMang(a, na);
    printf("Tong a = %d\n", tongMang(a, na));
    printf("Mang b: "); xuatMang(b, nb);
    printf("Tong b = %d\n", tongMang(b, nb));
    return 0;
}
```

Output:

```
Mang a: 1 2 3 4 5 
Tong a = 15
Mang b: 10 -3 7 
Tong b = 14
```

💡 Cả hai hàm chỉ **đọc** mảng nên dùng `const int a[]`. Số phần tử được tính bằng `sizeof` ở `main` — nơi `a` còn là mảng thật — rồi truyền vào hàm.

### Bài 2.

```c
#include <stdio.h>

#define MAX 1000

void nhapMang(int a[], int *n) {
    do {
        printf("Nhap so phan tu (1..%d): ", MAX);
        if (scanf("%d", n) != 1) { *n = 0; return; }   // nhap sai kieu
    } while (*n < 1 || *n > MAX);

    for (int i = 0; i < *n; i++) {
        printf("a[%d] = ", i);
        scanf("%d", &a[i]);
    }
}

void xuatMang(const int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[MAX], n;
    nhapMang(a, &n);
    printf("\nMang vua nhap: ");
    xuatMang(a, n);
    return 0;
}
```

⚠️ `n` trong hàm là **con trỏ** nên `scanf("%d", n)` không có dấu `&`, còn khi dùng giá trị phải viết `*n`.

💡 Vòng `do...while` ép người dùng nhập `n` trong khoảng hợp lệ — tránh ghi ra ngoài mảng `a[MAX]`.

### Bài 3.

```c
#include <stdio.h>

int timMax(const int a[], int n) {
    int res = a[0];
    for (int i = 1; i < n; i++)
        if (a[i] > res) res = a[i];
    return res;
}

int viTriMin(const int a[], int n) {
    int vt = 0;
    for (int i = 1; i < n; i++)
        if (a[i] < a[vt]) vt = i;
    return vt;
}

int main(void) {
    int a[] = {4, 9, -2, 7, -2, 5};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Gia tri lon nhat : %d\n", timMax(a, n));
    int vt = viTriMin(a, n);
    printf("Phan tu nho nhat : a[%d] = %d\n", vt, a[vt]);
    return 0;
}
```

Output:

```
Gia tri lon nhat : 9
Phan tu nho nhat : a[2] = -2
```

💡 Trả về **chỉ số** thay vì giá trị linh hoạt hơn: từ chỉ số bạn lấy được cả vị trí lẫn giá trị. Dùng `<` (không phải `<=`) để lấy vị trí xuất hiện **đầu tiên**.

⚠️ Cả hai hàm giả định `n >= 1`. Gọi với mảng rỗng sẽ đọc `a[0]` không hợp lệ.

### Bài 4.

```c
#include <stdio.h>

double trungBinh(const int a[], int n) {
    if (n <= 0) return 0.0;               // tranh chia cho 0
    long long s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return (double)s / n;
}

int main(void) {
    int a[] = {7, 8, 10, 6};
    int n = sizeof(a) / sizeof(a[0]);
    printf("Trung binh = %.2f\n", trungBinh(a, n));
    printf("Mang rong  = %.2f\n", trungBinh(a, 0));
    return 0;
}
```

Output:

```
Trung binh = 7.75
Mang rong  = 0.00
```

⚠️ Phải ép kiểu `(double)s / n`. Nếu viết `s / n` thì đó là **chia nguyên**, kết quả là 7 chứ không phải 7.75.

💡 Dùng `long long` cho tổng để tránh tràn số khi mảng lớn.

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(int x) {
    if (x < 2) return false;
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

int demNguyenTo(const int a[], int n) {
    int dem = 0;
    for (int i = 0; i < n; i++)
        if (laNguyenTo(a[i])) dem++;
    return dem;
}

int main(void) {
    int a[] = {2, 4, 7, 9, 11, 1, 13, 15};
    int n = sizeof(a) / sizeof(a[0]);
    printf("So luong so nguyen to: %d\n", demNguyenTo(a, n));   // 2 7 11 13 -> 4
    return 0;
}
```

💡 Chia nhỏ bài toán: hàm `laNguyenTo` xử lý **một số**, hàm `demNguyenTo` xử lý **cả mảng**. Mỗi hàm làm đúng một việc, dễ kiểm tra riêng.

### Bài 6.

```c
#include <stdio.h>

void daoNguoc(int a[], int n) {
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
}

void xuatMang(const int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5, 6};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Truoc: "); xuatMang(a, n);
    daoNguoc(a, n);
    printf("Sau  : "); xuatMang(a, n);
    return 0;
}
```

Output:

```
Truoc: 1 2 3 4 5 6 
Sau  : 6 5 4 3 2 1 
```

💡 Hàm `daoNguoc` không trả về gì (`void`) nhưng mảng `a` trong `main` vẫn bị đảo — bằng chứng hàm làm việc trên **mảng gốc** chứ không phải bản sao. Hàm này sửa mảng nên **không** được khai báo `const`.

### Bài 7.

```c
#include <stdio.h>

int timKiem(const int a[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i;          // gap la tra ve ngay
    return -1;                            // duyet het khong thay
}

int main(void) {
    int a[] = {5, 3, 8, 3, 1};
    int n = sizeof(a) / sizeof(a[0]);

    int x;
    printf("Nhap x: ");
    scanf("%d", &x);

    int vt = timKiem(a, n, x);
    if (vt == -1) printf("Khong tim thay %d\n", x);
    else          printf("%d xuat hien dau tien tai chi so %d\n", x, vt);
    return 0;
}
```

Với `x = 3`: `3 xuat hien dau tien tai chi so 1`. Với `x = 7`: `Khong tim thay 7`.

💡 Giá trị `-1` được chọn làm "không tìm thấy" vì chỉ số hợp lệ của mảng không bao giờ âm.

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

bool laTangDan(const int a[], int n) {
    for (int i = 1; i < n; i++)
        if (a[i] < a[i - 1]) return false;   // 1 cap sai la du ket luan
    return true;
}

int main(void) {
    int a[] = {1, 2, 2, 5, 9};
    int b[] = {1, 3, 2, 4};
    printf("a: %s\n", laTangDan(a, 5) ? "tang dan" : "khong tang dan");
    printf("b: %s\n", laTangDan(b, 4) ? "tang dan" : "khong tang dan");
    return 0;
}
```

Output:

```
a: tang dan
b: khong tang dan
```

💡 Mảng có 0 hoặc 1 phần tử được coi là tăng dần: vòng lặp không chạy lần nào và hàm trả về `true`.

### Bài 9.

```c
#include <stdio.h>

void cong2Mang(const int a[], const int b[], int c[], int n) {
    for (int i = 0; i < n; i++) c[i] = a[i] + b[i];
}

int main(void) {
    int a[] = {1, 2, 3, 4};
    int b[] = {10, 20, 30, 40};
    int c[4];                              // mang ket qua khai bao o noi goi

    cong2Mang(a, b, c, 4);

    printf("c = ");
    for (int i = 0; i < 4; i++) printf("%d ", c[i]);
    printf("\n");                          // c = 11 22 33 44
    return 0;
}
```

💡 C không cho hàm trả về mảng, nên mảng kết quả `c` được **truyền vào** để hàm ghi lên. `a` và `b` là đầu vào nên có `const`, còn `c` là đầu ra nên không có `const` — nhìn nguyên mẫu hàm là biết mảng nào bị ghi.

### Bài 10.

```c
void inMang(int a[]){
    int n = sizeof(a) / sizeof(a[0]);     // LOI: a o day la con tro
    for(int i = 0; i < n; i++) printf("%d ", a[i]);
}
```

**Lỗi:** bên trong hàm, tham số `a` là con trỏ `int *`. `sizeof(a)` là kích thước con trỏ (8 byte trên máy 64-bit) chứ không phải kích thước mảng, nên `n = 8 / 4 = 2` với mọi mảng. gcc với `-Wall` cảnh báo: `'sizeof' on array function parameter 'a' will return size of 'int *'`.

**Sửa:** tính số phần tử ở nơi khai báo mảng và truyền vào hàm.

```c
#include <stdio.h>

void inMang(const int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5, 6, 7};
    inMang(a, sizeof(a) / sizeof(a[0]));   // 1 2 3 4 5 6 7
    return 0;
}
```

💡 Một cách phổ biến để không phải gõ lại công thức là dùng macro, nhưng **chỉ được dùng với mảng thật**, không dùng với tham số hàm:

```c
#define SO_PHAN_TU(arr) (sizeof(arr) / sizeof((arr)[0]))
```

### Bài 11.

```c
#include <stdio.h>

void tachChanLe(const int a[], int n, int chan[], int *nc, int le[], int *nl) {
    *nc = *nl = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) chan[(*nc)++] = a[i];
        else               le[(*nl)++]   = a[i];
    }
}

void xuatMang(const int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[] = {5, 8, -3, 2, 7, 0, 4};
    int n = sizeof(a) / sizeof(a[0]);
    int chan[7], le[7], nc, nl;

    tachChanLe(a, n, chan, &nc, le, &nl);

    printf("So chan (%d): ", nc); xuatMang(chan, nc);
    printf("So le   (%d): ", nl); xuatMang(le, nl);
    return 0;
}
```

Output:

```
So chan (4): 8 2 0 4 
So le   (3): 5 -3 7 
```

💡 Hàm cần "trả về" 4 thứ: 2 mảng và 2 số lượng. Mảng thì tự sửa được, còn số lượng phải truyền **con trỏ** `int *nc`, `int *nl`. Viết `(*nc)++` có ngoặc để tăng giá trị chứ không tăng con trỏ.

⚠️ `-3 % 2` trong C bằng `-1` (không phải 1), nên kiểm tra số lẻ phải dùng `a[i] % 2 != 0` chứ không dùng `a[i] % 2 == 1`. Ở trên dùng `== 0` cho số chẵn và `else` cho số lẻ nên đúng với cả số âm.

### Bài 12.

```c
int *taoMang(void){
    int a[5] = {1, 2, 3, 4, 5};
    return a;                  // LOI: tra ve dia chi bien cuc bo
}
```

**Lỗi:** mảng `a` là **biến cục bộ**, nằm trên stack của hàm `taoMang`. Khi hàm kết thúc, vùng nhớ này bị giải phóng, con trỏ trả về trỏ tới vùng nhớ **không còn hợp lệ** (dangling pointer). Dùng nó là hành vi không xác định: có lúc in ra đúng, có lúc ra rác, có lúc crash. gcc cảnh báo: `function returns address of local variable`.

**Cách sửa 1 — truyền mảng vào hàm (khuyên dùng):**

```c
#include <stdio.h>

void taoMang(int a[], int n) {
    for (int i = 0; i < n; i++) a[i] = i + 1;
}

int main(void) {
    int a[5];
    taoMang(a, 5);
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);   // 1 2 3 4 5
    printf("\n");
    return 0;
}
```

**Cách sửa 2 — cấp phát động bằng `malloc`** (người gọi phải `free`):

```c
#include <stdio.h>
#include <stdlib.h>

int *taoMang(int n) {
    int *a = malloc(n * sizeof(int));
    if (a == NULL) return NULL;
    for (int i = 0; i < n; i++) a[i] = i + 1;
    return a;                      // vung nho heap van ton tai sau khi ham ket thuc
}

int main(void) {
    int *a = taoMang(5);
    if (a == NULL) return 1;
    for (int i = 0; i < 5; i++) printf("%d ", a[i]);   // 1 2 3 4 5
    printf("\n");
    free(a);                       // bat buoc giai phong
    return 0;
}
```

💡 Cách thứ 3 là khai báo `static int a[5]` trong hàm — vùng nhớ tồn tại suốt chương trình — nhưng mọi lần gọi đều dùng **chung một mảng**, dễ gây lỗi khó thấy. Chi tiết về `malloc` xem bài [07-04](../07-04-c-cap-phat-mang-dong.md).

### Bài 13.

```c
#include <stdio.h>

void daoDoan(int a[], int l, int r) {          // dao nguoc a[l..r]
    while (l < r) {
        int t = a[l]; a[l] = a[r]; a[r] = t;
        l++; r--;
    }
}

void xoayTrai(int a[], int n, int k) {
    if (n == 0) return;
    k %= n;                                    // xoay n vi tri = khong doi
    if (k < 0) k += n;
    daoDoan(a, 0, k - 1);
    daoDoan(a, k, n - 1);
    daoDoan(a, 0, n - 1);
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);

    xoayTrai(a, n, 2);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                              // 3 4 5 1 2
    return 0;
}
```

**Thuật toán 3 lần đảo:**

```
Ban dau        : 1 2 | 3 4 5
Dao doan dau   : 2 1 | 3 4 5
Dao doan sau   : 2 1 | 5 4 3
Dao ca mang    : 3 4 5 1 2   ✔
```

💡 Độ phức tạp **O(n)**, không cần mảng phụ. Cách "xoay 1 vị trí, lặp `k` lần" tốn O(n·k).

### Bài 14.

```c
#include <stdio.h>

int tongMang(const int a[], int n) {
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

int main(void) {
    int a[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int l = 2, r = 5;

    // a + l la dia chi cua a[l]; doan a[l..r] co r - l + 1 phan tu
    printf("Tong a[%d..%d] = %d\n", l, r, tongMang(a + l, r - l + 1));
    return 0;
}
```

Output:

```
Tong a[2..5] = 19
```

(4 + 1 + 5 + 9 = 19)

💡 Vì hàm chỉ nhận **địa chỉ bắt đầu**, `tongMang` "nhìn thấy" `a + l` như một mảng mới bắt đầu từ `a[l]`: bên trong hàm, `a[0]` chính là `a[l]` của `main`. Có thể viết tương đương `&a[l]` thay cho `a + l`.

⚠️ Phải đảm bảo `0 <= l <= r < n`, nếu không hàm sẽ đọc ra ngoài mảng.

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 1000

void nhapMang(int a[], int *n) {
    printf("Nhap so phan tu (0..%d): ", MAX);
    if (scanf("%d", n) != 1 || *n < 0 || *n > MAX) { *n = 0; return; }
    for (int i = 0; i < *n; i++) scanf("%d", &a[i]);
}

void xuatMang(const int a[], int n) {
    if (n == 0) { printf(">> Mang rong\n"); return; }
    printf(">> Mang (%d phan tu): ", n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int themCuoi(int a[], int *n, int x) {
    if (*n >= MAX) return 0;          // day
    a[(*n)++] = x;
    return 1;
}

int xoaTai(int a[], int *n, int k) {
    if (k < 0 || k >= *n) return 0;   // vi tri sai
    for (int i = k; i < *n - 1; i++) a[i] = a[i + 1];
    (*n)--;
    return 1;
}

int soSanhTang(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    return (x > y) - (x < y);
}

void sapXep(int a[], int n) {
    qsort(a, n, sizeof(int), soSanhTang);
}

int timKiem(const int a[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i;
    return -1;
}

int main(void) {
    int a[MAX], n = 0, chon, x, k;

    do {
        printf("\n1.Nhap 2.Xuat 3.Them cuoi 4.Xoa tai vi tri 5.Sap xep 6.Tim kiem 0.Thoat\n");
        printf("Lua chon: ");
        if (scanf("%d", &chon) != 1) break;

        switch (chon) {
            case 1: nhapMang(a, &n); break;
            case 2: xuatMang(a, n); break;
            case 3:
                printf("Nhap x: "); scanf("%d", &x);
                printf(themCuoi(a, &n, x) ? ">> Da them\n" : ">> Mang da day!\n");
                break;
            case 4:
                printf("Nhap vi tri: "); scanf("%d", &k);
                printf(xoaTai(a, &n, k) ? ">> Da xoa\n" : ">> Vi tri khong hop le!\n");
                break;
            case 5: sapXep(a, n); xuatMang(a, n); break;
            case 6:
                printf("Nhap x: "); scanf("%d", &x);
                k = timKiem(a, n, x);
                if (k == -1) printf(">> Khong tim thay\n");
                else         printf(">> Tim thay tai chi so %d\n", k);
                break;
            case 0: printf(">> Tam biet!\n"); break;
            default: printf(">> Lua chon khong hop le!\n");
        }
    } while (chon != 0);
    return 0;
}
```

**Các điểm đáng học:**

1. Hàm **thay đổi số phần tử** (`nhapMang`, `themCuoi`, `xoaTai`) nhận `int *n`; hàm **chỉ đọc** (`xuatMang`, `timKiem`) nhận `const int a[]` và `int n`
2. Hàm có thể thất bại thì **trả về 0/1** để `main` báo lỗi cho người dùng, thay vì in thông báo lẫn lộn bên trong
3. `main` chỉ còn điều phối menu — mỗi chức năng nằm gọn trong một hàm, dễ đọc và dễ sửa
4. Luôn kiểm tra biên (`MAX`, vị trí `k`) trước khi ghi vào mảng
