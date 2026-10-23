# Lời giải — [C]. Cấp Phát Mảng Động

[← Quay lại bài học](../07-04-c-cap-phat-mang-dong.md)

> **Quy tắc vàng:** mỗi `malloc`/`calloc`/`realloc` thành công phải có đúng một `free`, và **luôn kiểm tra `NULL`** sau khi cấp phát.

---

### Bài 1.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Nhap so phan tu: ");
    if (scanf("%d", &n) != 1 || n <= 0) { printf("n phai duong!\n"); return 1; }

    int *a = malloc(n * sizeof(int));      // CAP PHAT
    if (a == NULL) { printf("Khong du bo nho!\n"); return 1; }

    for (int i = 0; i < n; i++) {
        printf("  a[%d] = ", i);
        scanf("%d", &a[i]);
    }

    printf("Mang vua nhap: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    free(a);                               // GIAI PHONG
    a = NULL;                              // tranh dangling pointer

    return 0;
}
```

💡 **Ưu điểm lớn nhất của mảng động:** kích thước được quyết định **lúc chạy**, không phải lúc biên dịch. Không còn phải khai báo `int a[1000]` rồi chỉ dùng 5 phần tử.

### Bài 2.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *p = malloc(sizeof(int));     // cap phat 1 int, gia tri RAC
    if (p == NULL) return 1;
    *p = 42;
    printf("*p = %d\n", *p);
    free(p);

    int *r = calloc(1, sizeof(int));  // cap phat VA khoi tao = 0
    if (r == NULL) return 1;
    printf("*r = %d\n", *r);
    free(r);

    return 0;
}
```

| Cú pháp | Kết quả |
|---|---|
| `malloc(sizeof(int))` | 1 phần tử, giá trị **rác** |
| `calloc(1, sizeof(int))` | 1 phần tử, khởi tạo **0** |
| `malloc(5 * sizeof(int))` | Mảng 5 phần tử, giá trị **rác** |
| `calloc(5, sizeof(int))` | Mảng 5 phần tử, tất cả **0** |
| `realloc(p, 10 * sizeof(int))` | Đổi kích thước thành 10, giữ dữ liệu cũ |

💡 Cách viết `malloc(sizeof *p)` (lấy kích thước của **thứ mà `p` trỏ tới**) giúp không phải sửa khi đổi kiểu của `p`.

### Bài 3.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void inMang(const char *nhan, const int *a, int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int n = 5;

    // Cach 1: calloc - tu dong khoi tao 0
    int *a = calloc(n, sizeof(int));

    // Cach 2: malloc + memset (dat moi BYTE = 0)
    int *b = malloc(n * sizeof(int));
    if (b != NULL) memset(b, 0, n * sizeof(int));

    // Cach 3: malloc + vong lap
    int *c = malloc(n * sizeof(int));
    if (c != NULL) for (int i = 0; i < n; i++) c[i] = 0;

    if (a == NULL || b == NULL || c == NULL) {
        printf("Khong du bo nho!\n");
        free(a); free(b); free(c);        // free(NULL) an toan
        return 1;
    }

    inMang("Cach 1", a, n);               // 0 0 0 0 0
    inMang("Cach 2", b, n);
    inMang("Cach 3", c, n);

    free(a); free(b); free(c);
    return 0;
}
```

⚠️ **`malloc` (không có `memset`) cho giá trị RÁC**, không phải 0. Đây là khác biệt so với mảng toàn cục (tự động 0).

⚠️ `memset` đặt giá trị **theo từng byte**, nên chỉ dùng an toàn với 0 (hoặc -1). `memset(b, 1, ...)` **không** cho mảng toàn số 1 mà cho `16843009` (= 0x01010101).

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>

int *taoMang(int n) {
    if (n <= 0) return NULL;

    int *a = malloc(n * sizeof(int));
    if (a == NULL) return NULL;
    for (int i = 0; i < n; i++) a[i] = i;
    return a;                        // tra ve con tro toi vung nho HEAP
}

int main(void) {
    int n = 5;
    int *a = taoMang(n);

    if (a) {
        for (int i = 0; i < n; i++) printf("%d ", a[i]);
        printf("\n");                // 0 1 2 3 4

        free(a);                     // NGUOI GOI phai giai phong
        a = NULL;
    }
    return 0;
}
```

⚠️ **Trả về con trỏ tới bộ nhớ heap là HỢP LỆ** (khác với trả về địa chỉ biến cục bộ) — vì bộ nhớ heap tồn tại tới khi bạn `free`.

⚠️ **Nhưng nó tạo ra vấn đề trách nhiệm:** ai phải gọi `free`? Nếu người gọi quên → rò rỉ bộ nhớ. Vì vậy hãy **ghi rõ trong chú thích** của hàm rằng người gọi phải `free`, hoặc cung cấp kèm một hàm giải phóng tương ứng (ví dụ `taoMang` / `huyMang`).

✅ **Cách khác:** để người gọi tự cấp phát, hàm chỉ điền dữ liệu:

```c
void dienMang(int *a, int n) {
    for (int i = 0; i < n; i++) a[i] = i;
}
// int a[5]; dienMang(a, 5);   -> khong can free
```

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Cach 1: tu lam bang tay (4 buoc)
int moRong(int **a, int *sucChua, int sucChuaMoi) {
    if (sucChuaMoi <= *sucChua) return 1;

    int *moi = calloc(sucChuaMoi, sizeof(int));   // (1) cap phat vung moi
    if (moi == NULL) return 0;                     //     that bai: giu nguyen vung cu
    memcpy(moi, *a, *sucChua * sizeof(int));       // (2) copy du lieu cu sang
    free(*a);                                      // (3) giai phong vung cu
    *a = moi;                                      // (4) tro sang vung moi
    *sucChua = sucChuaMoi;
    return 1;
}

// Cach 2: dung realloc (lam ca 4 buoc tren)
int moRongRealloc(int **a, int *sucChua, int sucChuaMoi) {
    int *moi = realloc(*a, sucChuaMoi * sizeof(int));
    if (moi == NULL) return 0;                     // vung cu VAN CON, khong mat du lieu
    *a = moi;
    *sucChua = sucChuaMoi;
    return 1;
}

void inMang(const char *nhan, const int *a, int n) {
    printf("%s (suc chua %d): ", nhan, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int sucChua = 3;
    int *a = malloc(sucChua * sizeof(int));
    if (a == NULL) return 1;
    a[0] = 10; a[1] = 20; a[2] = 30;
    inMang("Truoc      ", a, sucChua);

    if (!moRong(&a, &sucChua, 6)) { free(a); return 1; }
    a[3] = 40; a[4] = 50; a[5] = 60;
    inMang("Sau moRong ", a, sucChua);

    if (!moRongRealloc(&a, &sucChua, 8)) { free(a); return 1; }
    a[6] = 70; a[7] = 80;
    inMang("Sau realloc", a, sucChua);

    free(a);
    return 0;
}
```

Output:

```
Truoc       (suc chua 3): 10 20 30 
Sau moRong  (suc chua 6): 10 20 30 40 50 60 
Sau realloc (suc chua 8): 10 20 30 40 50 60 70 80 
```

💡 Lưu ý thứ tự 4 bước — làm sai thứ tự sẽ mất dữ liệu hoặc rò rỉ bộ nhớ.

💡 `int **a` là **con trỏ tới con trỏ** — cho phép hàm thay đổi chính con trỏ `a` ở hàm gọi (xem [07-02](../07-02-c-con-tro-cap-2.md)). `int *sucChua` để hàm cập nhật được sức chứa.

| | Tự làm | `realloc` |
|---|---|---|
| Số dòng code | Nhiều | Ít |
| Có thể mở rộng **tại chỗ** (không copy) | ❌ Luôn copy | ✅ Nếu phía sau còn trống |
| Khi thất bại | Vùng cũ còn nguyên | Vùng cũ còn nguyên (trả về `NULL`) |

⚠️ **Sai lầm kinh điển:** `a = realloc(a, ...);` — nếu thất bại, `a` bị gán `NULL` và **mất luôn địa chỉ vùng cũ** → rò rỉ. Luôn dùng con trỏ tạm như trên.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n, m;
    printf("Nhap so hang va so cot: ");
    if (scanf("%d %d", &n, &m) != 2 || n <= 0 || m <= 0) return 1;

    // (1) Cap phat mang con tro, roi tung hang
    int **a = malloc(n * sizeof(int *));
    if (a == NULL) return 1;
    for (int i = 0; i < n; i++) {
        a[i] = malloc(m * sizeof(int));
        if (a[i] == NULL) {
            for (int k = 0; k < i; k++) free(a[k]);
            free(a);
            return 1;
        }
    }

    // (2) Dien du lieu
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = (i + 1) * (j + 1);

    // (3) In ra
    printf("Ma tran:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }

    // (4) Tinh tong
    long long tong = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            tong += a[i][j];
    printf("Tong = %lld\n", tong);

    // (5) Giai phong - NGUOC THU TU cap phat
    for (int i = 0; i < n; i++) free(a[i]);
    free(a);
    a = NULL;

    return 0;
}
```

💡 **Cách cấp phát khối liền — nhanh hơn, giải phóng dễ hơn:**

```c
int *duLieu = malloc(n * m * sizeof(int));     // 1 khoi lien tuc
// Truy cap: duLieu[i * m + j] thay cho a[i][j]

free(duLieu);                                   // chi 1 lenh free
```

Cách này còn nhanh hơn khi duyệt vì dữ liệu nằm liền nhau trong bộ nhớ (tốt cho cache CPU).

### Bài 7.

```c
int *a = malloc(10);                        // LOI: chi xin 10 BYTE
for (int i = 0; i < 10; i++) a[i] = i;      // ghi 10 * 4 = 40 byte -> TRAN
free(a);
```

**Lỗi:** tham số của `malloc` là **số byte**, không phải số phần tử. `malloc(10)` chỉ cấp 10 byte — đủ cho 2 số `int` rưỡi. Vòng lặp ghi 40 byte → **ghi tràn vùng heap** (heap buffer overflow). Ngoài ra chương trình **không kiểm tra `NULL`**.

**Hậu quả:** đây là **undefined behavior**. Thường chương trình vẫn chạy "bình thường" lúc đầu, nhưng đã phá hỏng dữ liệu quản lý heap, dẫn tới crash ở một lệnh `malloc`/`free` về sau, ví dụ:

```
free(): invalid next size (fast)
Aborted (core dumped)
```

**Sửa:**

```c
int *a = malloc(10 * sizeof(int));          // 10 PHAN TU int
if (a != NULL) {
    for (int i = 0; i < 10; i++) a[i] = i;
    free(a);
    a = NULL;
}
```

**Quy tắc ghép đôi:**

| Cấp phát | Giải phóng |
|---|---|
| `malloc(n * sizeof(T))` | `free(p)` |
| `calloc(n, sizeof(T))` | `free(p)` |
| `realloc(p, k)` | `free(p_moi)` (chỉ free con trỏ mới) |
| Mảng tĩnh / biến cục bộ | ❌ **KHÔNG** được `free` |

💡 `-fsanitize=address` bắt được lỗi này ngay: `heap-buffer-overflow`.

### Bài 8.

```c
for (int i = 0; i < 1000; i++) {
    int *p = malloc(1000 * sizeof(int));
    // ... xu ly ...
    // THIEU: free(p);
}
```

**Lỗi: rò rỉ bộ nhớ (memory leak).** Mỗi vòng lặp cấp phát 4000 byte mới nhưng không bao giờ giải phóng. Sau 1000 vòng, chương trình chiếm **4 MB** bộ nhớ vô ích, và con trỏ `p` bị ghi đè nên không còn cách nào lấy lại địa chỉ cũ để giải phóng.

**Sửa cách 1 — giải phóng trong vòng lặp:**

```c
for (int i = 0; i < 1000; i++) {
    int *p = malloc(1000 * sizeof(int));
    if (p == NULL) break;
    // ... xu ly ...
    free(p);                      // <- THEM VAO
}
```

**Sửa cách 2 — cấp phát MỘT LẦN ngoài vòng lặp (tốt hơn nhiều):**

```c
int *p = malloc(1000 * sizeof(int));
if (p != NULL) {
    for (int i = 0; i < 1000; i++) {
        // ... xu ly, dung lai cung vung nho ...
    }
    free(p);
}
```

**Sửa cách 3 — kích thước cố định nhỏ thì dùng mảng cục bộ (tự giải phóng):**

```c
for (int i = 0; i < 1000; i++) {
    int p[1000];                  // 4 KB tren stack, tu dong thu hoi
    // ... xu ly ...
}
```

⚠️ **Rò rỉ bộ nhớ nguy hiểm vì:** chương trình chạy bình thường lúc đầu, nhưng càng chạy lâu càng chiếm nhiều RAM, cuối cùng làm chậm cả máy hoặc bị hệ điều hành giết. Với server chạy 24/7, đây là lỗi nghiêm trọng.

### Bài 9.

```c
int *p = malloc(sizeof(int));
*p = 5;
free(p);
printf("%d", *p);    // LOI 1: use-after-free
free(p);             // LOI 2: double free
```

**Hai lỗi nghiêm trọng** (thêm một lỗi nhỏ: không kiểm tra `NULL` sau `malloc`):

**① Use-after-free (dùng sau khi giải phóng):** sau `free(p)`, vùng nhớ đã trả về hệ thống. `*p` đọc vào vùng nhớ không còn thuộc chương trình.
- Có thể in ra `5` (nếu chưa bị ghi đè) → **đánh lừa** người lập trình
- Có thể in ra rác
- Có thể crash

**② Double free (giải phóng 2 lần):** gọi `free` lần thứ hai trên cùng một con trỏ.

```
free(): double free detected in tcache 2
Aborted (core dumped)
```

Đây là lỗi nghiêm trọng, có thể phá hỏng cấu trúc quản lý bộ nhớ của hệ thống, và là nguồn của nhiều lỗ hổng bảo mật.

**Sửa:**

```c
int *p = malloc(sizeof(int));
if (p != NULL) {
    *p = 5;
    printf("%d\n", *p);       // dung TRUOC khi free
    free(p);
    p = NULL;                 // <- MAU CHOT
}

if (p) printf("%d", *p);      // an toan, khong chay
free(p);                      // an toan! free(NULL) KHONG lam gi ca
```

✅ **Quy tắc: luôn gán `NULL` ngay sau `free`.** Chuẩn C đảm bảo `free(NULL)` là hợp lệ và không làm gì — nhờ đó `free` nhiều lần cũng vô hại.

💡 Phát hiện bằng công cụ:

```bash
gcc -fsanitize=address -g main.c -o main && ./main
# AddressSanitizer: heap-use-after-free
# AddressSanitizer: attempting double-free
```

### Bài 10.

| Tiêu chí | Mảng tĩnh `int a[100]` | Mảng động `malloc(n * sizeof(int))` |
|---|---|---|
| **Kích thước xác định lúc** | Biên dịch (phải là hằng) | **Chạy** (có thể là biến) |
| **Vùng nhớ** | Stack (hoặc vùng tĩnh nếu toàn cục/`static`) | **Heap** |
| **Giới hạn kích thước** | ⚠️ Stack ~1–8 MB | Gần như toàn bộ RAM |
| **Cấp phát** | Tự động, rất nhanh | Có chi phí (gọi hàm cấp phát) |
| **Giải phóng** | ✅ Tự động khi ra khỏi phạm vi | ⚠️ **Phải tự gọi `free`** |
| **Rủi ro rò rỉ bộ nhớ** | ❌ Không | ✅ **Có** |
| **Thay đổi kích thước** | ❌ Không | ✅ Được (`realloc`) |
| **Báo lỗi khi thiếu bộ nhớ** | ❌ Không (crash stack overflow) | ✅ Trả về `NULL` |
| **`sizeof` cho cả mảng** | ✅ Có | ❌ Chỉ cho kích thước con trỏ |

💡 C99 còn có **mảng độ dài biến (VLA)** `int a[n];` với `n` là biến — kích thước xác định lúc chạy nhưng vẫn nằm trên **stack**, nên cũng bị giới hạn stack và không báo lỗi khi thiếu bộ nhớ (trong C11 VLA là tính năng tuỳ chọn, gcc hỗ trợ).

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Kích thước nhỏ, biết trước | Mảng tĩnh |
| Kích thước lớn (> 1 MB) | Động, hoặc mảng toàn cục |
| Kích thước do người dùng nhập | Động |
| Cần thay đổi kích thước | Động + `realloc` |
| Dữ liệu cần tồn tại sau khi hàm kết thúc | Động |

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // int a[10000000];                  // 40 MB tren STACK -> CRASH
    int *b = malloc(10000000 * sizeof(int));   // 40 MB tren HEAP -> OK
    if (b == NULL) { printf("Khong du bo nho!\n"); return 1; }

    b[0] = 1;
    b[9999999] = 100;
    printf("OK: %d %d\n", b[0], b[9999999]);

    free(b);
    return 0;
}
```

**Stack vs Heap:**

| | Stack (ngăn xếp) | Heap (vùng nhớ động) |
|---|---|---|
| **Kích thước** | ⚠️ Nhỏ, cố định (1–8 MB) | Lớn (gần bằng RAM + swap) |
| **Cấp phát** | Tự động, chỉ dịch con trỏ stack — **cực nhanh** | Phải tìm vùng trống phù hợp — chậm hơn |
| **Giải phóng** | Tự động khi ra khỏi hàm | Thủ công (`free`) |
| **Chứa gì** | Biến cục bộ, tham số hàm, địa chỉ quay về | Dữ liệu cấp phát bằng `malloc`/`calloc`/`realloc` |
| **Phân mảnh** | Không | Có thể bị |
| **Lỗi đặc trưng** | Stack overflow | Memory leak, dangling pointer |

**Sơ đồ bộ nhớ một chương trình:**

```
Dia chi cao
+------------------+
|      STACK       |  <- bien cuc bo, tham so (tang XUONG)
|        |         |
|        v         |
|                  |
|        ^         |
|        |         |
|      HEAP        |  <- malloc/calloc/realloc (tang LEN)
+------------------+
|   Du lieu tinh   |  <- bien toan cuc, static
+------------------+
|    Ma chuong     |  <- ma may
|      trinh       |
+------------------+
Dia chi thap
```

**Xem và tăng giới hạn stack trên Linux:**

```bash
ulimit -s              # xem gioi han (KB), thuong la 8192 = 8 MB
ulimit -s unlimited    # tang len (chi cho phien lam viec hien tai)
```

💡 **Cách khác để có mảng lớn mà không dùng heap:** khai báo **toàn cục** (ngoài `main`) hoặc `static` — nó sẽ nằm ở vùng dữ liệu tĩnh, không giới hạn bởi stack:

```c
int a[10000000];        // TOAN CUC -> OK, va tu dong khoi tao 0
int main(void) { /* ... */ return 0; }
```

Đây là mẹo rất hay dùng trong lập trình thi đấu.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *duLieu;
    int soLuong;        // so phan tu hien co
    int sucChua;        // suc chua toi da hien tai
} MangDong;

int khoiTao(MangDong *v) {
    v->duLieu = malloc(1 * sizeof(int));
    v->soLuong = 0;
    v->sucChua = (v->duLieu != NULL) ? 1 : 0;
    return v->duLieu != NULL;
}

void huy(MangDong *v) {                       // thay cho destructor
    free(v->duLieu);
    v->duLieu = NULL;
    v->soLuong = v->sucChua = 0;
}

int push_back(MangDong *v, int x) {
    if (v->soLuong == v->sucChua) {           // DAY -> gap doi
        int sucChuaMoi = v->sucChua * 2;
        int *moi = realloc(v->duLieu, sucChuaMoi * sizeof(int));
        if (moi == NULL) return 0;            // that bai, du lieu cu con nguyen
        v->duLieu = moi;
        v->sucChua = sucChuaMoi;
        printf("  [Da mo rong suc chua len %d]\n", v->sucChua);
    }
    v->duLieu[v->soLuong++] = x;
    return 1;
}

void pop_back(MangDong *v) { if (v->soLuong > 0) v->soLuong--; }

void in(const MangDong *v) {
    printf("  [ ");
    for (int i = 0; i < v->soLuong; i++) printf("%d ", v->duLieu[i]);
    printf("]  size=%d, capacity=%d\n", v->soLuong, v->sucChua);
}

int main(void) {
    MangDong v;
    if (!khoiTao(&v)) return 1;

    for (int i = 1; i <= 10; i++) {
        if (!push_back(&v, i * 10)) break;
        in(&v);
    }

    v.duLieu[0] = 999;
    printf("\nSau khi sua v.duLieu[0]:\n");
    in(&v);

    huy(&v);                                  // PHAI goi thu cong
    return 0;
}
```

Output:

```
  [ 10 ]  size=1, capacity=1
  [Da mo rong suc chua len 2]
  [ 10 20 ]  size=2, capacity=2
  [Da mo rong suc chua len 4]
  [ 10 20 30 ]  size=3, capacity=4
  [ 10 20 30 40 ]  size=4, capacity=4
  [Da mo rong suc chua len 8]
  [ 10 20 30 40 50 ]  size=5, capacity=8
  ...
```

💡 **Vì sao mở rộng GẤP ĐÔI thay vì cộng thêm 1:**

| Chiến lược | Số lần cấp phát khi thêm n phần tử | Chi phí trung bình mỗi `push_back` |
|---|---|---|
| Cộng thêm 1 mỗi lần | n lần | **O(n)** — rất chậm |
| **Gấp đôi** | log₂(n) lần | **O(1)** trung bình |

Đây gọi là **độ phức tạp khấu hao (amortized complexity)** — tuy có vài lần `push_back` tốn O(n), nhưng chia trung bình ra thì mỗi lần chỉ O(1).

⚠️ C không tự gọi hàm dọn dẹp khi biến ra khỏi phạm vi, nên bạn **phải tự gọi `huy(&v)`** — quên là rò rỉ bộ nhớ.

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *a = NULL;
    int n = 0, sucChua = 0, x;

    printf("Nhap day so, ket thuc bang 0:\n");
    while (scanf("%d", &x) == 1 && x != 0) {
        if (n == sucChua) {
            int sucChuaMoi = (sucChua == 0) ? 4 : sucChua * 2;
            // realloc(NULL, k) tuong duong malloc(k)
            int *moi = realloc(a, sucChuaMoi * sizeof(int));
            if (moi == NULL) { printf("Het bo nho!\n"); break; }
            a = moi;
            sucChua = sucChuaMoi;
        }
        a[n++] = x;
    }

    printf("Da nhap %d so (suc chua %d): ", n, sucChua);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    free(a);
    return 0;
}
```

Input / Output:

```
Nhap day so, ket thuc bang 0:
5 8 1 9 3 7 0
Da nhap 6 so (suc chua 8): 5 8 1 9 3 7 
```

💡 **`realloc(NULL, k)` hoạt động như `malloc(k)`** — nhờ đó không cần xử lý riêng lần cấp phát đầu tiên.

💡 Vòng lặp cũng dừng khi `scanf` không đọc được số (hết dữ liệu / EOF), nên chương trình vẫn đúng nếu người dùng quên nhập số 0.

### Bài 14.

**Chương trình có rò rỉ:**

```c
// leak.c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    for (int i = 0; i < 1000; i++) {
        int *p = malloc(1000 * sizeof(int));
        if (p == NULL) return 1;
        p[0] = i;
        // thieu free(p);
    }
    printf("Xong\n");
    return 0;
}
```

**Cách 1 — AddressSanitizer (dễ dùng nhất):**

```bash
gcc -fsanitize=address -g leak.c -o leak
./leak
```

Kết quả:

```
Xong

=================================================================
==12345==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 4000000 byte(s) in 1000 object(s) allocated from:
    #0 0x7f... in malloc
    #1 0x5555... in main leak.c:7

SUMMARY: AddressSanitizer: 4000000 byte(s) leaked in 1000 allocation(s).
```

Thông báo chỉ rõ: **4 MB rò rỉ**, ở **dòng 7** của `leak.c`.

**Cách 2 — Valgrind (chi tiết hơn, không cần biên dịch lại đặc biệt):**

```bash
sudo apt install valgrind          # cai dat tren Ubuntu
gcc -g leak.c -o leak
valgrind --leak-check=full ./leak
```

Kết quả:

```
==12345== HEAP SUMMARY:
==12345==     in use at exit: 4,000,000 bytes in 1,000 blocks
==12345==   total heap usage: 1,001 allocs, 1 frees, 4,001,024 bytes allocated
==12345== 
==12345== 4,000,000 bytes in 1,000 blocks are definitely lost in loss record 1 of 1
==12345==    at 0x...: malloc (vg_replace_malloc.c:...)
==12345==    by 0x...: main (leak.c:7)
==12345== 
==12345== LEAK SUMMARY:
==12345==    definitely lost: 4,000,000 bytes in 1,000 blocks
```

**Sau khi sửa** (thêm `free(p);`):

```
==12345== All heap blocks were freed -- no leaks are possible
```

💡 **Các loại rò rỉ trong báo cáo Valgrind:**

| Loại | Ý nghĩa |
|---|---|
| **definitely lost** | Chắc chắn rò rỉ — không còn con trỏ nào tới vùng nhớ |
| **indirectly lost** | Rò rỉ gián tiếp (do cấu trúc cha bị rò rỉ) |
| **possibly lost** | Có thể rò rỉ (con trỏ trỏ vào giữa vùng nhớ) |
| **still reachable** | Chưa giải phóng nhưng vẫn có con trỏ tới — thường không nghiêm trọng |

✅ **Thói quen tốt:** chạy `-fsanitize=address` khi phát triển. Nó phát hiện cả rò rỉ lẫn truy cập ngoài biên, use-after-free, double-free.

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char   ten[50];
    int    tuoi;
    double diemTB;
} SinhVien;

// Doc 1 dong vao s (toi da n-1 ky tu), bo ky tu '\n' o cuoi
void docDong(char *s, int n) {
    if (fgets(s, n, stdin) == NULL) { s[0] = '\0'; return; }
    s[strcspn(s, "\n")] = '\0';
}

SinhVien *nhapDanhSach(int n) {
    SinhVien *ds = malloc(n * sizeof(SinhVien));
    if (ds == NULL) return NULL;
    for (int i = 0; i < n; i++) {
        printf("--- Sinh vien %d ---\n", i + 1);
        printf("Ho ten            : "); docDong(ds[i].ten, sizeof(ds[i].ten));
        printf("Tuoi              : "); scanf("%d", &ds[i].tuoi);
        printf("Diem trung binh   : "); scanf("%lf", &ds[i].diemTB);
        while (getchar() != '\n' && !feof(stdin));   // bo '\n' con lai
    }
    return ds;
}

const char *xepLoai(double d) {
    if (d >= 8.5) return "Gioi";
    if (d >= 7.0) return "Kha";
    if (d >= 5.0) return "Trung binh";
    return "Yeu";
}

void inDanhSach(const SinhVien *ds, int n) {
    printf("\n+-----+--------------------+-------+--------+------------+\n");
    printf("| STT | HO TEN             | TUOI  | DIEM   | XEP LOAI   |\n");
    printf("+-----+--------------------+-------+--------+------------+\n");
    for (int i = 0; i < n; i++) {
        printf("| %-3d | %-18s | %5d | %6.2f | %-10s |\n",
               i + 1, ds[i].ten, ds[i].tuoi, ds[i].diemTB, xepLoai(ds[i].diemTB));
    }
    printf("+-----+--------------------+-------+--------+------------+\n");
}

double diemTrungBinhLop(const SinhVien *ds, int n) {
    if (n <= 0) return 0;
    double tong = 0;
    for (int i = 0; i < n; i++) tong += ds[i].diemTB;
    return tong / n;
}

int main(void) {
    int n;
    printf("Nhap so sinh vien: ");
    if (scanf("%d", &n) != 1 || n <= 0) { printf("So luong khong hop le!\n"); return 1; }
    while (getchar() != '\n' && !feof(stdin));       // bo '\n' sau so n

    SinhVien *ds = nhapDanhSach(n);
    if (ds == NULL) { printf("Khong du bo nho!\n"); return 1; }

    inDanhSach(ds, n);
    printf("Diem trung binh ca lop: %.2f\n", diemTrungBinhLop(ds, n));

    free(ds);                    // GIAI PHONG
    ds = NULL;

    return 0;
}
```

Input mẫu:

```
2
Nguyen Van An
20
8.75
Tran Thi Binh
19
6.5
```

Output (phần bảng):

```
+-----+--------------------+-------+--------+------------+
| STT | HO TEN             | TUOI  | DIEM   | XEP LOAI   |
+-----+--------------------+-------+--------+------------+
| 1   | Nguyen Van An      |    20 |   8.75 | Gioi       |
| 2   | Tran Thi Binh      |    19 |   6.50 | Trung binh |
+-----+--------------------+-------+--------+------------+
Diem trung binh ca lop: 7.62
```

💡 Vì `ten` là **mảng `char` nằm ngay trong struct**, chỉ cần **một lệnh `free(ds)`** là giải phóng toàn bộ. Nếu `ten` là `char *` được cấp phát riêng bằng `malloc`, bạn phải `free` từng `ds[i].ten` trước rồi mới `free(ds)`.

💡 Dùng `fgets` để đọc họ tên có dấu cách (không dùng `gets` vì không kiểm tra kích thước); `scanf("%lf", ...)` để đọc `double`.
