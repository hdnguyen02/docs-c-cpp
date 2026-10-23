# Lời giải — [C]. Sắp Xếp Ổn Định Và Merge Sort

[← Quay lại bài học](../10-04-c-sap-xep-on-dinh-va-merge-sort.md)

> **Ổn định (stable)** nghĩa là: các phần tử **bằng nhau** (theo tiêu chí so sánh) giữ nguyên **thứ tự tương đối ban đầu**.
> `qsort` của C **không được đảm bảo** ổn định; merge sort, insertion sort **có**.

---

### Bài 1.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct { int khoa; char nhan; } Muc;

int cmpKhoa(const void *a, const void *b) {
    const Muc *x = a, *y = b;
    return (x->khoa > y->khoa) - (x->khoa < y->khoa);
}

// Merge sort on dinh theo khoa
void tron(Muc v[], Muc tam[], int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (v[i].khoa <= v[j].khoa) tam[k++] = v[i++];
        else                        tam[k++] = v[j++];
    }
    while (i <= m) tam[k++] = v[i++];
    while (j <= r) tam[k++] = v[j++];
    for (k = l; k <= r; k++) v[k] = tam[k];
}

void mergeSort(Muc v[], Muc tam[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(v, tam, l, m);
    mergeSort(v, tam, m + 1, r);
    tron(v, tam, l, m, r);
}

void in(const char *nhan, const Muc v[], int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("(%d,%c) ", v[i].khoa, v[i].nhan);
    printf("\n");
}

int main(void) {
    Muc goc[] = {
        {3,'a'}, {1,'b'}, {3,'c'}, {2,'d'}, {1,'e'}, {3,'f'}, {2,'g'}
    };
    int n = sizeof(goc) / sizeof(goc[0]);

    in("Ban dau   ", goc, n);

    Muc a[7], b[7], tam[7];
    memcpy(a, goc, sizeof(goc));
    qsort(a, n, sizeof(Muc), cmpKhoa);
    in("qsort     ", a, n);

    memcpy(b, goc, sizeof(goc));
    mergeSort(b, tam, 0, n - 1);
    in("merge sort", b, n);

    bool giong = true;
    for (int i = 0; i < n; i++)
        if (a[i].khoa != b[i].khoa || a[i].nhan != b[i].nhan) giong = false;
    printf("\nGiong nhau? %s\n", giong ? "true" : "false");
    return 0;
}
```

Kết quả tham khảo:

```
Ban dau   : (3,a) (1,b) (3,c) (2,d) (1,e) (3,f) (2,g) 
qsort     : (1,b) (1,e) (2,d) (2,g) (3,a) (3,c) (3,f) 
merge sort: (1,b) (1,e) (2,d) (2,g) (3,a) (3,c) (3,f) 

Giong nhau? true
```

**Nhận xét:** với merge sort, các cặp có `khoa = 1` **luôn** giữ nguyên thứ tự `b` trước `e` (đúng như trong mảng gốc). Với `qsort`, kết quả phụ thuộc vào thư viện C: trên glibc (Linux) bạn thường thấy kết quả giống merge sort, trên thư viện khác có thể thấy `e` đứng trước `b`.

⚠️ "Tình cờ ổn định trên máy mình" **không** có nghĩa là `qsort` ổn định — chuẩn C không hứa hẹn điều đó. Đó là lý do bài 2 tự cài quicksort để thấy rõ sự mất ổn định.

💡 `(x > y) - (x < y)` là cách viết hàm so sánh trả về `-1/0/1` mà không sợ tràn số như `x - y`.

### Bài 2.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 1000

typedef struct { int khoa; int thuTuGoc; } Muc;

int cmpKhoa(const void *a, const void *b) {
    const Muc *x = a, *y = b;
    return (x->khoa > y->khoa) - (x->khoa < y->khoa);
}

void hoanVi(Muc *x, Muc *y) { Muc t = *x; *x = *y; *y = t; }

// Quicksort phan hoach Lomuto - KHONG on dinh
void quickSort(Muc v[], int l, int r) {
    if (l >= r) return;
    int chot = v[r].khoa, i = l - 1;
    for (int j = l; j < r; j++)
        if (v[j].khoa < chot) hoanVi(&v[++i], &v[j]);
    hoanVi(&v[i + 1], &v[r]);
    quickSort(v, l, i);
    quickSort(v, i + 2, r);
}

// Kiem tra tinh on dinh: thuTuGoc trong moi nhom phai TANG DAN
bool kiemTraOnDinh(const Muc v[], int n) {
    for (int i = 1; i < n; i++)
        if (v[i].khoa == v[i-1].khoa && v[i].thuTuGoc < v[i-1].thuTuGoc)
            return false;
    return true;
}

int main(void) {
    static Muc a[N], b[N];
    for (int i = 0; i < N; i++) {
        a[i].khoa = i % 5;             // chi co 5 gia tri khoa khac nhau
        a[i].thuTuGoc = i;
        b[i] = a[i];
    }

    qsort(a, N, sizeof(Muc), cmpKhoa);   // (1) qsort cua thu vien
    quickSort(b, 0, N - 1);              // (2) quicksort tu viet

    printf("Mang %d phan tu, 5 gia tri khoa khac nhau\n", N);
    printf("qsort (thu vien)     on dinh? %s\n", kiemTraOnDinh(a, N) ? "true" : "false");
    printf("quicksort tu viet    on dinh? %s\n", kiemTraOnDinh(b, N) ? "true" : "false");

    printf("\n10 phan tu dau (qsort)    : ");
    for (int i = 0; i < 10; i++) printf("%d ", a[i].thuTuGoc);
    printf("\n10 phan tu dau (quicksort): ");
    for (int i = 0; i < 10; i++) printf("%d ", b[i].thuTuGoc);
    printf("\n");
    return 0;
}
```

Output (trên glibc):

```
Mang 1000 phan tu, 5 gia tri khoa khac nhau
qsort (thu vien)     on dinh? true
quicksort tu viet    on dinh? false

10 phan tu dau (qsort)    : 0 5 10 15 20 25 30 35 40 45 
10 phan tu dau (quicksort): 995 0 5 10 15 20 25 30 35 40 
```

**Nhận xét:**
- Dòng `qsort` có thể in `true` hoặc `false` tuỳ thư viện C. Trên glibc thường là `true` vì glibc dùng merge sort khi đủ bộ nhớ — nhưng đây là **chi tiết cài đặt**, không phải cam kết của chuẩn.
- Quicksort tự viết **chắc chắn** mất ổn định: phép `hoanVi` trong bước phân hoạch đưa phần tử nhảy xa, vượt qua các phần tử cùng khoá. Ngay ở 10 phần tử đầu đã thấy `995` (phần tử cuối mảng, được chọn làm chốt) nhảy lên trước `0, 5, 10...` dù cùng khoá 0.

### Bài 3.

```c
#include <stdio.h>
#include <string.h>

typedef struct { char ten[30]; double diem; } SinhVien;

// Merge sort theo diem GIAM DAN, on dinh
void tron(SinhVien v[], SinhVien tam[], int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        // lay ben trai khi diem trai >= diem phai -> giu thu tu nhap
        if (v[i].diem >= v[j].diem) tam[k++] = v[i++];
        else                        tam[k++] = v[j++];
    }
    while (i <= m) tam[k++] = v[i++];
    while (j <= r) tam[k++] = v[j++];
    for (k = l; k <= r; k++) v[k] = tam[k];
}

void mergeSort(SinhVien v[], SinhVien tam[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(v, tam, l, m);
    mergeSort(v, tam, m + 1, r);
    tron(v, tam, l, m, r);
}

int main(void) {
    // Thu tu nhap co y nghia (vi du: thu tu nop bai)
    SinhVien ds[] = {
        {"An",    9.0},
        {"Binh",  8.5},
        {"Chi",   9.0},
        {"Dung",  7.0},
        {"Em",    8.5},
        {"Phong", 9.0}
    };
    int n = sizeof(ds) / sizeof(ds[0]);
    SinhVien tam[6];

    printf("=== THU TU NHAP BAN DAU ===\n");
    for (int i = 0; i < n; i++)
        printf("  %d. %s - %.1f\n", i + 1, ds[i].ten, ds[i].diem);

    mergeSort(ds, tam, 0, n - 1);

    printf("\n=== SAU KHI SAP THEO DIEM (merge sort) ===\n");
    for (int i = 0; i < n; i++)
        printf("  %d. %-8s - %.1f\n", i + 1, ds[i].ten, ds[i].diem);
    return 0;
}
```

Output:

```
=== SAU KHI SAP THEO DIEM (merge sort) ===
  1. An       - 9.0
  2. Chi      - 9.0
  3. Phong    - 9.0
  4. Binh     - 8.5
  5. Em       - 8.5
  6. Dung     - 7.0
```

💡 An, Chi, Phong cùng 9.0 điểm và giữ nguyên thứ tự nhập — điều này **quan trọng** khi thứ tự nhập mang ý nghĩa (ai nộp bài trước).

💡 Sắp **giảm dần** mà vẫn ổn định: điều kiện lấy bên trái là `>=` (bằng nhau vẫn ưu tiên bên trái).

### Bài 4.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char   ten[20];
    char   phongBan[20];
    int    tuoi;
    double luong;
} NhanVien;

typedef int (*HamSoSanh)(const NhanVien *, const NhanVien *);

int theoTen(const NhanVien *a, const NhanVien *b)      { return strcmp(a->ten, b->ten); }
int theoTuoi(const NhanVien *a, const NhanVien *b)     { return (a->tuoi > b->tuoi) - (a->tuoi < b->tuoi); }
int theoPhongBan(const NhanVien *a, const NhanVien *b) { return strcmp(a->phongBan, b->phongBan); }

// Merge sort on dinh, nhan ham so sanh lam tham so
void tron(NhanVien v[], NhanVien tam[], int l, int m, int r, HamSoSanh cmp) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (cmp(&v[i], &v[j]) <= 0) tam[k++] = v[i++];
        else                        tam[k++] = v[j++];
    }
    while (i <= m) tam[k++] = v[i++];
    while (j <= r) tam[k++] = v[j++];
    for (k = l; k <= r; k++) v[k] = tam[k];
}

void mergeSort(NhanVien v[], NhanVien tam[], int l, int r, HamSoSanh cmp) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(v, tam, l, m, cmp);
    mergeSort(v, tam, m + 1, r, cmp);
    tron(v, tam, l, m, r, cmp);
}

int main(void) {
    NhanVien ds[] = {
        {"An",    "IT",     25, 20},
        {"Binh",  "HR",     30, 15},
        {"Chi",   "IT",     28, 25},
        {"Dung",  "Sales",  25, 18},
        {"Em",    "IT",     25, 22},
        {"Phong", "HR",     35, 15}
    };
    int n = sizeof(ds) / sizeof(ds[0]);
    NhanVien tam[6];

    // KY THUAT: sap xep on dinh NHIEU LAN, tu tieu chi PHU den tieu chi CHINH
    mergeSort(ds, tam, 0, n - 1, theoTen);        // (3) tieu chi phu nhat truoc
    mergeSort(ds, tam, 0, n - 1, theoTuoi);       // (2) tieu chi phu
    mergeSort(ds, tam, 0, n - 1, theoPhongBan);   // (1) tieu chi chinh CUOI CUNG

    printf("Sap theo: Phong ban -> Tuoi -> Ten\n");
    printf("+----------+----------+------+--------+\n");
    printf("| PHONG    | HO TEN   | TUOI | LUONG  |\n");
    printf("+----------+----------+------+--------+\n");
    for (int i = 0; i < n; i++)
        printf("| %-8s | %-8s | %4d | %6.0f |\n",
               ds[i].phongBan, ds[i].ten, ds[i].tuoi, ds[i].luong);
    printf("+----------+----------+------+--------+\n");
    return 0;
}
```

Output:

```
Sap theo: Phong ban -> Tuoi -> Ten
+----------+----------+------+--------+
| PHONG    | HO TEN   | TUOI | LUONG  |
+----------+----------+------+--------+
| HR       | Binh     |   30 |     15 |
| HR       | Phong    |   35 |     15 |
| IT       | An       |   25 |     20 |
| IT       | Em       |   25 |     22 |
| IT       | Chi      |   28 |     25 |
| Sales    | Dung     |   25 |     18 |
+----------+----------+------+--------+
```

💡 **Kỹ thuật rất hay:** thay vì viết một hàm so sánh phức tạp nhiều `if`, gọi hàm sắp xếp ổn định nhiều lần theo thứ tự **ngược** (tiêu chí phụ trước, chính sau).

**Ưu điểm:** dễ đọc, dễ thêm/bớt tiêu chí, và mỗi hàm so sánh đơn giản.
**Nhược điểm:** chạy `k` lần sắp xếp thay vì 1 lần.

⚠️ **Chỉ hoạt động với sắp xếp ổn định** — dùng `qsort` (không đảm bảo ổn định) có thể phá vỡ kết quả của các lượt trước.

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 1000000

int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

void tron(int a[], int tam[], int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) tam[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];
    while (i <= m) tam[k++] = a[i++];
    while (j <= r) tam[k++] = a[j++];
    memcpy(a + l, tam + l, (size_t)(r - l + 1) * sizeof(int));
}

void mergeSort(int a[], int tam[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(a, tam, l, m);
    mergeSort(a, tam, m + 1, r);
    tron(a, tam, l, m, r);
}

int main(void) {
    int *goc = malloc(N * sizeof(int));
    int *a   = malloc(N * sizeof(int));
    int *b   = malloc(N * sizeof(int));
    int *tam = malloc(N * sizeof(int));
    if (!goc || !a || !b || !tam) { printf("Khong du bo nho\n"); return 1; }

    for (int i = 0; i < N; i++) goc[i] = (int)((i * 7919LL + 13) % (N / 10));

    memcpy(a, goc, N * sizeof(int));
    clock_t t1 = clock();
    qsort(a, N, sizeof(int), cmpInt);
    double tQsort = (double)(clock() - t1) * 1000 / CLOCKS_PER_SEC;

    memcpy(b, goc, N * sizeof(int));
    t1 = clock();
    mergeSort(b, tam, 0, N - 1);
    double tMerge = (double)(clock() - t1) * 1000 / CLOCKS_PER_SEC;

    printf("Mang %d phan tu:\n", N);
    printf("  qsort      : %.0f ms\n", tQsort);
    printf("  merge sort : %.0f ms\n", tMerge);
    printf("\nKet qua giong nhau: %s\n",
           memcmp(a, b, N * sizeof(int)) == 0 ? "true" : "false");

    free(goc); free(a); free(b); free(tam);
    return 0;
}
```

Kết quả tham khảo (biên dịch với `-O2`):

```
Mang 1000000 phan tu:
  qsort      : 57 ms
  merge sort : 89 ms

Ket qua giong nhau: true
```

**Nhận xét:** thời gian cụ thể phụ thuộc máy, trình biên dịch và thư viện C. Cả hai đều là O(n log n) nên chênh lệch chỉ ở hằng số: `qsort` phải gọi hàm so sánh qua **con trỏ hàm** cho mỗi phép so sánh, nhưng bù lại được cài đặt rất kỹ; merge sort tự viết đơn giản hơn và tốn thêm thời gian sao chép qua mảng phụ. Cái giá chắc chắn của merge sort là **mảng phụ O(n)** — đổi lại ta được **tính ổn định**.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    printf("=== SO SANH BO NHO ===\n\n");

    printf("Quicksort:\n");
    printf("  Bo nho phu  : O(log n)  - chi cho stack de quy\n");
    printf("  Voi n = 10^6: khoang vai chuc muc stack ~ vai tram byte\n");

    printf("\nMerge sort:\n");
    printf("  Bo nho phu  : O(n)  - can mang tam bang kich thuoc du lieu\n");
    printf("  Voi n = 10^6 int: khoang 4 MB bo nho phu (malloc)\n");

    // Minh hoa thuc te
    const long N = 10000000;
    printf("\n--- Thuc te voi %ld int ---\n", N);
    printf("Du lieu goc          : %.2f MB\n", (double)N * sizeof(int) / (1024 * 1024));
    printf("Quicksort can them   : ~0 MB\n");
    printf("Merge sort can them  : ~%.2f MB\n", (double)N * sizeof(int) / (1024 * 1024));
    return 0;
}
```

**Bảng so sánh bộ nhớ:**

| | Quicksort | Merge sort |
|---|---|---|
| Bộ nhớ phụ | **O(log n)** (stack đệ quy) | **O(n)** (mảng tạm) |
| Với 10⁶ `int` | ~vài trăm byte | **~4 MB** |
| Với 10⁷ `int` | ~vài trăm byte | **~40 MB** |
| Ổn định | ❌ | ✅ |

⚠️ **Với dữ liệu rất lớn, merge sort có thể không cấp phát được mảng phụ** — luôn kiểm tra `malloc` trả về `NULL`.

💡 Bạn không biết chắc `qsort` dùng bao nhiêu bộ nhớ phụ vì chuẩn C không quy định thuật toán; glibc chẳng hạn sẽ cấp phát mảng tạm cho merge sort khi đủ bộ nhớ, ngược lại chuyển sang thuật toán tại chỗ.

### Bài 7.

**3 tình huống BẮT BUỘC cần sắp xếp ổn định:**

**① Sắp xếp nhiều tiêu chí bằng nhiều lượt** (như bài 4)

```c
mergeSort(ds, tam, 0, n - 1, theoTen);        // tieu chi phu
mergeSort(ds, tam, 0, n - 1, theoPhongBan);   // tieu chi chinh
// Dung qsort (khong on dinh) co the pha vo ket qua luot truoc
```

**② Thứ tự ban đầu mang ý nghĩa nghiệp vụ**

```c
// Danh sach giao dich theo thu tu THOI GIAN
// Sap theo so tien, nhung cung so tien thi giu thu tu thoi gian
mergeSort(giaoDich, tam, 0, n - 1, theoSoTien);
```

Ví dụ thực tế:
- Danh sách nộp bài (ai nộp trước được ưu tiên khi cùng điểm)
- Hàng đợi xử lý (FIFO trong cùng mức ưu tiên)
- Lịch sử giao dịch ngân hàng

**③ Giao diện người dùng — sắp xếp bảng theo cột**

```c
// Nguoi dung bam cot "Ten" -> sap theo ten
// Roi bam cot "Tuoi" -> sap theo tuoi, nhung cung tuoi van giu thu tu ten
```

Đây là hành vi người dùng **mong đợi** ở mọi bảng dữ liệu (Excel, Google Sheets đều làm vậy). Nếu dùng thuật toán không ổn định, mỗi lần bấm cột có thể xáo trộn các dòng bằng nhau.

**Khi nào KHÔNG cần sắp xếp ổn định:**
- Sắp xếp số nguyên thuần tuý (các phần tử bằng nhau không phân biệt được)
- Hàm so sánh đã bao gồm tiêu chí phá hoà hoàn toàn (không có 2 phần tử nào "bằng nhau")
- Ưu tiên bộ nhớ, chấp nhận dùng `qsort`

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char   ten[20];
    double diem;
    int    thuTuGoc;          // them truong nay
} SinhVien;

int cmp(const void *a, const void *b) {
    const SinhVien *x = a, *y = b;
    if (x->diem != y->diem) return (x->diem < y->diem) ? 1 : -1;  // diem giam dan
    return x->thuTuGoc - y->thuTuGoc;                             // <- BI QUYET
}

int main(void) {
    SinhVien ds[] = {
        {"An", 9.0, 0}, {"Binh", 8.5, 0}, {"Chi", 9.0, 0},
        {"Dung", 7.0, 0}, {"Em", 8.5, 0}, {"Phong", 9.0, 0}
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    // Gan thu tu goc
    for (int i = 0; i < n; i++) ds[i].thuTuGoc = i;

    // qsort THONG THUONG nhung them thuTuGoc lam tieu chi phu
    // -> ket qua GIONG HET mot phep sap xep on dinh
    qsort(ds, n, sizeof(SinhVien), cmp);

    printf("Ket qua (qsort + thuTuGoc = on dinh):\n");
    for (int i = 0; i < n; i++)
        printf("  %s - %g (goc: %d)\n", ds[i].ten, ds[i].diem, ds[i].thuTuGoc);
    return 0;
}
```

Output:

```
Ket qua (qsort + thuTuGoc = on dinh):
  An - 9 (goc: 0)
  Chi - 9 (goc: 2)
  Phong - 9 (goc: 5)
  Binh - 8.5 (goc: 1)
  Em - 8.5 (goc: 4)
  Dung - 7 (goc: 3)
```

💡 **Kỹ thuật này làm `qsort` cho kết quả "ổn định":** thêm chỉ số ban đầu làm tiêu chí phá hoà cuối cùng. Khi đó **không còn 2 phần tử nào "bằng nhau"** nên thứ tự luôn xác định, trên mọi thư viện C.

⚠️ Không viết `return (int)(x->diem - y->diem);` cho số thực — `8.5 - 9.0 = -0.5` ép sang `int` thành `0`, hai điểm khác nhau bị coi là bằng nhau.

**So sánh 2 cách:**

| | Merge sort tự viết | `qsort` + chỉ số |
|---|---|---|
| Bộ nhớ phụ | O(n) mảng tạm | Tuỳ thư viện |
| Bộ nhớ dữ liệu | Không thêm | ⚠️ Thêm 4 byte/phần tử |
| Code | Phải tự viết thuật toán | ✅ Chỉ sửa hàm so sánh |
| Đảm bảo ổn định | ✅ | ✅ |

### Bài 9.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char thanhPho[20];
    char quan[20];
    int  danSo;
} Dong;

typedef int (*HamSoSanh)(const Dong *, const Dong *);

int theoDanSoGiam(const Dong *a, const Dong *b) { return (a->danSo < b->danSo) - (a->danSo > b->danSo); }
int theoThanhPho(const Dong *a, const Dong *b)  { return strcmp(a->thanhPho, b->thanhPho); }

void tron(Dong v[], Dong tam[], int l, int m, int r, HamSoSanh cmp) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (cmp(&v[i], &v[j]) <= 0) tam[k++] = v[i++];
        else                        tam[k++] = v[j++];
    }
    while (i <= m) tam[k++] = v[i++];
    while (j <= r) tam[k++] = v[j++];
    for (k = l; k <= r; k++) v[k] = tam[k];
}

void mergeSort(Dong v[], Dong tam[], int l, int r, HamSoSanh cmp) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(v, tam, l, m, cmp);
    mergeSort(v, tam, m + 1, r, cmp);
    tron(v, tam, l, m, r, cmp);
}

int main(void) {
    Dong bang[] = {
        {"Ha Noi",   "Ba Dinh",    250},
        {"TP HCM",   "Quan 1",     180},
        {"Ha Noi",   "Cau Giay",   280},
        {"Da Nang",  "Hai Chau",   200},
        {"TP HCM",   "Quan 7",     360},
        {"Ha Noi",   "Dong Da",    400},
        {"TP HCM",   "Binh Thanh", 490}
    };
    int n = sizeof(bang) / sizeof(bang[0]);
    Dong tam[7];

    // (1) Sap theo DAN SO giam dan (tieu chi PHU)
    mergeSort(bang, tam, 0, n - 1, theoDanSoGiam);
    // (2) Sap theo THANH PHO (tieu chi CHINH) - sap xep on dinh giu nguyen ket qua (1)
    mergeSort(bang, tam, 0, n - 1, theoThanhPho);

    printf("Nhom theo thanh pho, trong nhom sap theo dan so giam dan:\n");
    printf("+------------+---------------+----------+\n");
    printf("| THANH PHO  | QUAN          | DAN SO   |\n");
    printf("+------------+---------------+----------+\n");

    const char *tpTruoc = "";
    for (int i = 0; i < n; i++) {
        int cungTP = strcmp(bang[i].thanhPho, tpTruoc) == 0;
        if (!cungTP && i > 0)
            printf("+------------+---------------+----------+\n");
        printf("| %-10s | %-13s | %8d |\n",
               cungTP ? "" : bang[i].thanhPho, bang[i].quan, bang[i].danSo);
        tpTruoc = bang[i].thanhPho;
    }
    printf("+------------+---------------+----------+\n");
    return 0;
}
```

Output:

```
Nhom theo thanh pho, trong nhom sap theo dan so giam dan:
+------------+---------------+----------+
| THANH PHO  | QUAN          | DAN SO   |
+------------+---------------+----------+
| Da Nang    | Hai Chau      |      200 |
+------------+---------------+----------+
| Ha Noi     | Dong Da       |      400 |
|            | Cau Giay      |      280 |
|            | Ba Dinh       |      250 |
+------------+---------------+----------+
| TP HCM     | Binh Thanh    |      490 |
|            | Quan 7        |      360 |
|            | Quan 1        |      180 |
+------------+---------------+----------+
```

💡 Đây chính là cách các phần mềm bảng tính thực hiện "sắp xếp nhiều cấp" (multi-level sort).

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Merge sort TONG QUAT, cach goi giong het qsort
static void tronByte(char *base, char *tam, size_t l, size_t m, size_t r,
                     size_t size, int (*cmp)(const void *, const void *)) {
    size_t i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        // <= 0 : bang nhau thi lay tu NUA TRAI truoc -> on dinh
        if (cmp(base + i * size, base + j * size) <= 0)
            memcpy(tam + (k++) * size, base + (i++) * size, size);
        else
            memcpy(tam + (k++) * size, base + (j++) * size, size);
    }
    while (i <= m) memcpy(tam + (k++) * size, base + (i++) * size, size);
    while (j <= r) memcpy(tam + (k++) * size, base + (j++) * size, size);
    memcpy(base + l * size, tam + l * size, (r - l + 1) * size);
}

static void chiaDoi(char *base, char *tam, size_t l, size_t r,
                    size_t size, int (*cmp)(const void *, const void *)) {
    if (l >= r) return;
    size_t m = l + (r - l) / 2;
    chiaDoi(base, tam, l, m, size, cmp);
    chiaDoi(base, tam, m + 1, r, size, cmp);
    tronByte(base, tam, l, m, r, size, cmp);
}

// Tra ve 0 neu thanh cong, -1 neu khong cap phat duoc bo nho
int stableSort(void *base, size_t n, size_t size,
               int (*cmp)(const void *, const void *)) {
    if (n < 2) return 0;
    char *tam = malloc(n * size);
    if (tam == NULL) return -1;
    chiaDoi((char *)base, tam, 0, n - 1, size, cmp);
    free(tam);
    return 0;
}

// ---- Thu nghiem ----
typedef struct { int khoa; char nhan; } Muc;

int cmpKhoa(const void *a, const void *b) {
    const Muc *x = a, *y = b;
    return (x->khoa > y->khoa) - (x->khoa < y->khoa);
}

int main(void) {
    Muc v[] = {
        {3,'a'}, {1,'b'}, {3,'c'}, {2,'d'}, {1,'e'}, {3,'f'}, {2,'g'}
    };
    size_t n = sizeof(v) / sizeof(v[0]);

    printf("Ban dau : ");
    for (size_t i = 0; i < n; i++) printf("(%d,%c) ", v[i].khoa, v[i].nhan);
    printf("\n");

    stableSort(v, n, sizeof(Muc), cmpKhoa);     // goi giong qsort

    printf("Sau sort: ");
    for (size_t i = 0; i < n; i++) printf("(%d,%c) ", v[i].khoa, v[i].nhan);
    printf("\n");

    // Kiem tra on dinh: cung khoa thi nhan phai tang dan (a < c < f ...)
    int onDinh = 1;
    for (size_t i = 1; i < n; i++)
        if (v[i].khoa == v[i-1].khoa && v[i].nhan < v[i-1].nhan) onDinh = 0;
    printf("\nOn dinh? %s\n", onDinh ? "true" : "false");
    return 0;
}
```

Output:

```
Ban dau : (3,a) (1,b) (3,c) (2,d) (1,e) (3,f) (2,g) 
Sau sort: (1,b) (1,e) (2,d) (2,g) (3,a) (3,c) (3,f) 

On dinh? true
```

💡 **Vì sao dùng `char *`:** không được làm phép cộng con trỏ trên `void *` trong C chuẩn. Ép về `char *` (mỗi phần tử 1 byte) rồi nhân chỉ số với `size` để nhảy tới phần tử thứ `i` — đây cũng là cách `qsort` làm bên trong.

💡 **Điểm mấu chốt tạo tính ổn định:** điều kiện `cmp(...) <= 0`. Khi 2 phần tử bằng nhau, ta ưu tiên lấy từ **nửa trái** (xuất hiện trước trong mảng gốc).

⚠️ Đổi thành `< 0` sẽ làm thuật toán **mất tính ổn định**.

### Bài 11.

```c
#include <stdio.h>

typedef struct { int khoa; char nhan; } Muc;

// Selection Sort - KHONG on dinh
void selectionSort(Muc v[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int viTriMin = i;
        for (int j = i + 1; j < n; j++)
            if (v[j].khoa < v[viTriMin].khoa) viTriMin = j;

        if (viTriMin != i) {                  // <- PHEP DOI CHO PHA VO TINH ON DINH
            Muc t = v[i]; v[i] = v[viTriMin]; v[viTriMin] = t;
        }
    }
}

void in(const char *nhan, const Muc v[], int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("(%d,%c) ", v[i].khoa, v[i].nhan);
    printf("\n");
}

int main(void) {
    Muc v[] = {{2,'a'}, {2,'b'}, {1,'c'}};
    int n = 3;

    in("Ban dau ", v, n);
    selectionSort(v, n);
    in("Sau sort", v, n);
    return 0;
}
```

Output:

```
Ban dau : (2,a) (2,b) (1,c) 
Sau sort: (1,c) (2,b) (2,a) 
```

**Phân tích vì sao mất ổn định:**

```
Buoc i=0: tim min trong [2a, 2b, 1c] -> la 1c (vi tri 2)
          doi cho v[0] va v[2]
          -> [1c, 2b, 2a]
          
          PHEP DOI CHO nay da NHAY 2a tu dau xuong cuoi,
          vuot qua 2b -> pha vo thu tu tuong doi!
```

Kết quả: `2b` đứng trước `2a`, trong khi ban đầu `2a` đứng trước.

**Tổng kết tính ổn định của các thuật toán:**

| Thuật toán | Ổn định? | Vì sao |
|---|---|---|
| Bubble Sort | ✅ Có | Chỉ đổi chỗ 2 phần tử **kề nhau** khi thực sự `>` |
| Insertion Sort | ✅ Có | Chèn vào **sau** các phần tử bằng nhau |
| Merge Sort | ✅ Có | Ưu tiên nửa trái khi bằng nhau |
| **Selection Sort** | ❌ **Không** | Phép đổi chỗ nhảy qua nhiều phần tử |
| **Quick Sort** | ❌ **Không** | Phân hoạch dùng đổi chỗ nhảy xa |
| **Heap Sort** | ❌ **Không** | Cấu trúc heap không giữ thứ tự |

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool laChan(int x) { return x % 2 == 0; }

// Phan hoach ON DINH: phan tu thoa dieu kien len truoc, giu nguyen thu tu
// Tra ve so phan tu thoa dieu kien (vi tri ranh gioi)
int phanHoachOnDinh(int a[], int n, bool (*dk)(int)) {
    int *tam = malloc(n * sizeof(int));
    if (tam == NULL) return -1;
    int k = 0;
    for (int i = 0; i < n; i++) if (dk(a[i]))  tam[k++] = a[i];   // nhom 1
    int ranhGioi = k;
    for (int i = 0; i < n; i++) if (!dk(a[i])) tam[k++] = a[i];   // nhom 2
    for (int i = 0; i < n; i++) a[i] = tam[i];
    free(tam);
    return ranhGioi;
}

// Phan hoach KHONG on dinh (kieu quicksort): doi cho 2 dau
int phanHoachThuong(int a[], int n, bool (*dk)(int)) {
    int i = 0, j = n - 1;
    while (i <= j) {
        if (dk(a[i])) i++;
        else { int t = a[i]; a[i] = a[j]; a[j] = t; j--; }
    }
    return i;
}

void in(const char *nhan, const int a[], int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int b[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = 10;

    in("Ban dau          ", a, n);

    int k1 = phanHoachThuong(a, n, laChan);
    in("Phan hoach thuong", a, n);
    printf("  (so chan: %d phan tu)\n", k1);

    int k2 = phanHoachOnDinh(b, n, laChan);
    in("Phan hoach on dinh", b, n);
    printf("  (so chan: %d phan tu)\n", k2);
    return 0;
}
```

Output:

```
Ban dau          : 1 2 3 4 5 6 7 8 9 10 
Phan hoach thuong: 10 2 8 4 6 7 5 9 3 1 
  (so chan: 5 phan tu)
Phan hoach on dinh: 2 4 6 8 10 1 3 5 7 9 
  (so chan: 5 phan tu)
```

**Phân hoạch** chia mảng thành **2 nhóm** theo một điều kiện và trả về **ranh giới** giữa 2 nhóm.

| | Phân hoạch thường | Phân hoạch ổn định |
|---|---|---|
| Giữ thứ tự | ❌ Không | ✅ **Có** |
| Độ phức tạp | O(n) | O(n) |
| Bộ nhớ phụ | O(1) | O(n) |

💡 **Nhanh hơn sắp xếp** khi chỉ cần phân nhóm (không cần sắp xếp trong nhóm).

### Bài 13.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char      ngay[11];       // "yyyy-mm-dd" de so sanh chuoi truc tiep
    char      moTa[30];
    long long soTien;
} GiaoDich;

void tron(GiaoDich v[], GiaoDich tam[], int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (strcmp(v[i].ngay, v[j].ngay) <= 0) tam[k++] = v[i++];
        else                                   tam[k++] = v[j++];
    }
    while (i <= m) tam[k++] = v[i++];
    while (j <= r) tam[k++] = v[j++];
    for (k = l; k <= r; k++) v[k] = tam[k];
}

void mergeSort(GiaoDich v[], GiaoDich tam[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(v, tam, l, m);
    mergeSort(v, tam, m + 1, r);
    tron(v, tam, l, m, r);
}

int main(void) {
    // Danh sach theo THU TU NHAP (thu tu thoi gian thuc)
    GiaoDich ds[] = {
        {"2026-09-17", "Mua sach",       -250000},
        {"2026-09-15", "Nhan luong",    15000000},
        {"2026-09-17", "An trua",         -85000},
        {"2026-09-16", "Do xang",        -200000},
        {"2026-09-17", "Ca phe",          -45000},
        {"2026-09-15", "Tra tien nha",  -5000000}
    };
    int n = sizeof(ds) / sizeof(ds[0]);
    GiaoDich tam[6];

    printf("=== THU TU NHAP (theo thoi gian thuc) ===\n");
    for (int i = 0; i < n; i++)
        printf("  %d. %s %s\n", i + 1, ds[i].ngay, ds[i].moTa);

    // Sap xep on dinh: cung ngay -> giu nguyen thu tu thoi gian nhap
    mergeSort(ds, tam, 0, n - 1);

    printf("\n=== SAU KHI SAP THEO NGAY ===\n");
    printf("+------------+-----------------+--------------+\n");
    printf("| NGAY       | MO TA           | SO TIEN      |\n");
    printf("+------------+-----------------+--------------+\n");

    long long soDu = 0;
    for (int i = 0; i < n; i++) {
        soDu += ds[i].soTien;
        int cungNgay = (i > 0 && strcmp(ds[i].ngay, ds[i-1].ngay) == 0);
        printf("| %-10s | %-15s | %12lld |\n",
               cungNgay ? "" : ds[i].ngay, ds[i].moTa, ds[i].soTien);
    }
    printf("+------------+-----------------+--------------+\n");
    printf("| %-28s | %12lld |\n", "SO DU CUOI KY", soDu);
    printf("+------------+-----------------+--------------+\n");
    return 0;
}
```

Output:

```
=== SAU KHI SAP THEO NGAY ===
+------------+-----------------+--------------+
| NGAY       | MO TA           | SO TIEN      |
+------------+-----------------+--------------+
| 2026-09-15 | Nhan luong      |     15000000 |
|            | Tra tien nha    |     -5000000 |
| 2026-09-16 | Do xang         |      -200000 |
| 2026-09-17 | Mua sach        |      -250000 |
|            | An trua         |       -85000 |
|            | Ca phe          |       -45000 |
+------------+-----------------+--------------+
| SO DU CUOI KY                |      9420000 |
+------------+-----------------+--------------+
```

💡 **Định dạng `"yyyy-mm-dd"` (ISO 8601)** cho phép so sánh chuỗi trực tiếp bằng `strcmp` mà vẫn đúng thứ tự thời gian — đây là lý do chuẩn này được dùng rộng rãi trong cơ sở dữ liệu và API.

💡 Trong cùng một ngày, thứ tự giao dịch **giữ nguyên như lúc nhập** — điều bắt buộc với sổ kế toán.

### Bài 14.

**Bảng so sánh đầy đủ:**

| Thuật toán | Tốt nhất | Trung bình | Xấu nhất | Bộ nhớ phụ | Ổn định |
|---|---|---|---|---|---|
| Bubble Sort | O(n) (có cờ dừng sớm) | O(n²) | O(n²) | O(1) | ✅ |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | ✅ |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | ❌ |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | **O(n)** | ✅ |
| **Quick Sort** | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ |
| `qsort` (thư viện C) | — | thường O(n log n) | tuỳ cài đặt | tuỳ cài đặt | **Không đảm bảo** |

**Chọn cách nào — theo nhu cầu:**

```
Can giu thu tu cac phan tu bang nhau?
├─ Khong -> qsort (it code nhat)
└─ Co ─ Duoc them truong chi so goc?
        ├─ Co    -> qsort + chi so goc lam tieu chi phu
        └─ Khong -> tu viet merge sort
                    (mang nho, gan sap xep san -> insertion sort)
```

💡 Chuẩn C không quy định thuật toán cho `qsort` — ngay cả độ phức tạp cũng không được hứa hẹn, dù trên thực tế các thư viện phổ biến đều cho O(n log n).

### Bài 15.

```c
#include <stdio.h>
#include <string.h>

#define SO_NGUOI 6

typedef struct {
    char ten[20];
    int  diem;
    int  hangTruoc;      // 0 = chua co hang
} NguoiChoi;

// Merge sort theo diem GIAM DAN, on dinh
void tron(NguoiChoi v[], NguoiChoi tam[], int l, int m, int r) {
    int i = l, j = m + 1, k = l;
    while (i <= m && j <= r) {
        if (v[i].diem >= v[j].diem) tam[k++] = v[i++];
        else                        tam[k++] = v[j++];
    }
    while (i <= m) tam[k++] = v[i++];
    while (j <= r) tam[k++] = v[j++];
    for (k = l; k <= r; k++) v[k] = tam[k];
}

void mergeSort(NguoiChoi v[], NguoiChoi tam[], int l, int r) {
    if (l >= r) return;
    int m = l + (r - l) / 2;
    mergeSort(v, tam, l, m);
    mergeSort(v, tam, m + 1, r);
    tron(v, tam, l, m, r);
}

void hienBang(const NguoiChoi ds[], int n, int vong) {
    printf("\n=== SAU VONG %d ===\n", vong);
    printf("+------+------------+-------+-----------+\n");
    printf("| HANG | NGUOI CHOI | DIEM  | THAY DOI  |\n");
    printf("+------+------------+-------+-----------+\n");
    for (int i = 0; i < n; i++) {
        int hangMoi = i + 1;
        int thayDoi = ds[i].hangTruoc - hangMoi;
        char mui[12];
        if      (ds[i].hangTruoc == 0) strcpy(mui, "moi");
        else if (thayDoi > 0)          sprintf(mui, "+%d", thayDoi);
        else if (thayDoi < 0)          sprintf(mui, "%d", thayDoi);
        else                           strcpy(mui, "--");

        printf("| %-4d | %-10s | %5d | %9s |\n", hangMoi, ds[i].ten, ds[i].diem, mui);
    }
    printf("+------+------------+-------+-----------+\n");
}

int main(void) {
    NguoiChoi ds[SO_NGUOI] = {
        {"An", 0, 0}, {"Binh", 0, 0}, {"Chi", 0, 0},
        {"Dung", 0, 0}, {"Em", 0, 0}, {"Phong", 0, 0}
    };
    NguoiChoi tam[SO_NGUOI];

    // Diem tung vong, theo thu tu ten: An, Binh, Chi, Dung, Em, Phong
    const char *thuTuTen[SO_NGUOI] = {"An", "Binh", "Chi", "Dung", "Em", "Phong"};
    int diemVong[3][SO_NGUOI] = {
        {10, 15, 10,  8, 15, 12},        // vong 1
        {12,  8, 15, 20, 10, 12},        // vong 2
        {15, 15,  5, 10, 12, 18}         // vong 3
    };

    for (int vong = 0; vong < 3; vong++) {
        for (int i = 0; i < SO_NGUOI; i++) {
            // Ghi lai hang hien tai (vong 1 chua co hang)
            ds[i].hangTruoc = (vong == 0) ? 0 : i + 1;
            // Cong diem theo ten
            for (int k = 0; k < SO_NGUOI; k++)
                if (strcmp(ds[i].ten, thuTuTen[k]) == 0)
                    ds[i].diem += diemVong[vong][k];
        }

        // SAP XEP ON DINH: diem giam dan, CUNG DIEM -> giu thu hang vong truoc
        mergeSort(ds, tam, 0, SO_NGUOI - 1);

        hienBang(ds, SO_NGUOI, vong + 1);
    }

    printf("\n*** NHA VO DICH: %s voi %d diem ***\n", ds[0].ten, ds[0].diem);
    return 0;
}
```

Output (rút gọn):

```
=== SAU VONG 1 ===
+------+------------+-------+-----------+
| HANG | NGUOI CHOI | DIEM  | THAY DOI  |
+------+------------+-------+-----------+
| 1    | Binh       |    15 |       moi |
| 2    | Em         |    15 |       moi |
| 3    | Phong      |    12 |       moi |
| 4    | An         |    10 |       moi |
| 5    | Chi        |    10 |       moi |
| 6    | Dung       |     8 |       moi |
+------+------------+-------+-----------+

...

=== SAU VONG 3 ===
+------+------------+-------+-----------+
| HANG | NGUOI CHOI | DIEM  | THAY DOI  |
+------+------------+-------+-----------+
| 1    | Phong      |    42 |        +3 |
| 2    | Dung       |    38 |        -1 |
| 3    | Binh       |    38 |        +2 |
| 4    | Em         |    37 |        -2 |
| 5    | An         |    37 |        +1 |
| 6    | Chi        |    30 |        -3 |
+------+------------+-------+-----------+

*** NHA VO DICH: Phong voi 42 diem ***
```

💡 **Vì sao phải dùng sắp xếp ổn định:** Binh và Em cùng 15 điểm ở vòng 1; ở vòng 3 Dung và Binh cùng 38 điểm — Dung đứng trên vì hạng vòng 2 cao hơn. Nhờ merge sort ổn định, thứ tự giữa những người cùng điểm được giữ theo thứ hạng vòng trước thay vì nhảy loạn xạ — đây chính là cách các giải đấu thật xử lý (ai đạt điểm đó trước thì xếp trên).
