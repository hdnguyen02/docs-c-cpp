# Lời giải — [C]. Thuật Toán Tìm Kiếm Tuyến Tính

[← Quay lại bài học](../10-05-c-thuat-toan-tim-kiem-tuyen-tinh.md)

> **Tìm kiếm tuyến tính (linear search)** duyệt lần lượt từng phần tử. Độ phức tạp **O(n)**, nhưng **không yêu cầu mảng sắp xếp**.

---

### Bài 1.

```c
#include <stdio.h>

int timTuyenTinh(const int a[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i;
    return -1;
}

int main(void) {
    int a[] = {7, 3, 9, 1, 5, 3, 8};
    int n = sizeof(a) / sizeof(a[0]);
    int canTim[] = {9, 3, 100};

    for (int k = 0; k < 3; k++) {
        int x = canTim[k];
        int vt = timTuyenTinh(a, n, x);
        printf("Tim %d: ", x);
        if (vt != -1) printf("thay tai vi tri %d\n", vt);
        else          printf("khong tim thay\n");
    }
    return 0;
}
```

Output:

```
Tim 9: thay tai vi tri 2
Tim 3: thay tai vi tri 1
Tim 100: khong tim thay
```

💡 **Ưu điểm lớn nhất:** hoạt động với mảng **chưa sắp xếp** — đây là điều tìm kiếm nhị phân không làm được.

### Bài 2.

```c
#include <stdio.h>

int timCuoiCung(const int a[], int n, int x) {
    // Duyet NGUOC tu cuoi ve dau
    for (int i = n - 1; i >= 0; i--)
        if (a[i] == x) return i;
    return -1;
}

int main(void) {
    int a[] = {7, 3, 9, 1, 5, 3, 8, 3};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d(%d) ", a[i], i);
    printf("\n");

    printf("Vi tri CUOI CUNG cua 3: %d\n", timCuoiCung(a, n, 3));   // 7
    return 0;
}
```

💡 Chỉ cần **duyệt ngược** — tìm thấy đầu tiên khi đi ngược chính là vị trí cuối cùng.

⚠️ Biến chạy `i` phải là kiểu **có dấu** (`int`). Nếu dùng `size_t` (không dấu) thì điều kiện `i >= 0` **luôn đúng**, khi `i` giảm qua 0 sẽ quay vòng thành số cực lớn → vòng lặp vô hạn / truy cập ngoài mảng.

### Bài 3.

```c
#include <stdio.h>

// Ghi cac vi tri vao mang viTri[], tra ve so vi tri tim duoc
int timTatCa(const int a[], int n, int x, int viTri[]) {
    int dem = 0;
    for (int i = 0; i < n; i++)
        if (a[i] == x) viTri[dem++] = i;
    return dem;
}

int main(void) {
    int a[] = {3, 7, 3, 1, 3, 9, 3};
    int n = sizeof(a) / sizeof(a[0]);
    int viTri[7];                 // toi da n vi tri

    int soLuong = timTatCa(a, n, 3, viTri);

    printf("Gia tri 3 xuat hien tai cac vi tri: ");
    if (soLuong == 0) printf("(khong co)");
    for (int i = 0; i < soLuong; i++) printf("%d ", viTri[i]);
    printf("\nTong cong: %d lan\n", soLuong);
    return 0;
}
```

Output:

```
Gia tri 3 xuat hien tai cac vi tri: 0 2 4 6 
Tong cong: 4 lan
```

💡 C không có mảng động tự co giãn, nên người gọi chuẩn bị sẵn mảng kết quả **đủ lớn** (tối đa `n` phần tử) và hàm trả về **số phần tử đã ghi**.

### Bài 4.

```c
#include <stdio.h>

int demSoLan(const int a[], int n, int x) {
    int dem = 0;
    for (int i = 0; i < n; i++)
        if (a[i] == x) dem++;
    return dem;
}

int main(void) {
    int a[] = {3, 7, 3, 1, 3, 9, 3, 7};
    int n = sizeof(a) / sizeof(a[0]);

    printf("So 3 xuat hien: %d lan\n", demSoLan(a, n, 3));
    printf("So 7 xuat hien: %d lan\n", demSoLan(a, n, 7));
    printf("So 5 xuat hien: %d lan\n", demSoLan(a, n, 5));
    return 0;
}
```

Output:

```
So 3 xuat hien: 4 lan
So 7 xuat hien: 2 lan
So 5 xuat hien: 0 lan
```

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(int n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main(void) {
    int a[] = {4, 9, 15, 7, 12, 11, 20, 8};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n\n");

    // (1) So nguyen to dau tien
    for (int i = 0; i < n; i++)
        if (laNguyenTo(a[i])) {
            printf("So nguyen to dau tien : %d (vi tri %d)\n", a[i], i);
            break;
        }

    // (2) So chan dau tien
    for (int i = 0; i < n; i++)
        if (a[i] % 2 == 0) {
            printf("So chan dau tien      : %d (vi tri %d)\n", a[i], i);
            break;
        }

    // (3) Chia het cho k
    int k = 5, timThay = -1;
    for (int i = 0; i < n; i++)
        if (a[i] % k == 0) { timThay = i; break; }
    if (timThay != -1)
        printf("Chia het cho %d dau tien: %d\n", k, a[timThay]);
    else
        printf("Khong co so nao chia het cho %d\n", k);
    return 0;
}
```

Output:

```
Mang: 4 9 15 7 12 11 20 8 

So nguyen to dau tien : 7 (vi tri 3)
So chan dau tien      : 4 (vi tri 0)
Chia het cho 5 dau tien: 15
```

💡 `break` giúp dừng ngay khi gặp phần tử đầu tiên thoả mãn, không duyệt thừa phần còn lại.

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

typedef bool (*DieuKien)(int);

// (1) Vi tri dau tien thoa dieu kien, -1 neu khong co
int timDau(const int a[], int n, DieuKien dk) {
    for (int i = 0; i < n; i++) if (dk(a[i])) return i;
    return -1;
}

// (2) Dem so phan tu thoa dieu kien
int demNeu(const int a[], int n, DieuKien dk) {
    int dem = 0;
    for (int i = 0; i < n; i++) if (dk(a[i])) dem++;
    return dem;
}

// (3) Co it nhat mot / tat ca / khong phan tu nao thoa
bool coMot(const int a[], int n, DieuKien dk)   { return timDau(a, n, dk) != -1; }
bool tatCa(const int a[], int n, DieuKien dk)   { return demNeu(a, n, dk) == n; }
bool khongCo(const int a[], int n, DieuKien dk) { return !coMot(a, n, dk); }

bool lonHon5(int x) { return x > 5; }
bool laLe(int x)    { return x % 2 != 0; }
bool lonHon8(int x) { return x > 8; }
bool duong(int x)   { return x > 0; }
bool am(int x)      { return x < 0; }

int main(void) {
    int a[] = {3, 7, 3, 1, 9, 3, 8, 2};
    int n = sizeof(a) / sizeof(a[0]);

    int vt = timDau(a, n, lonHon5);
    printf("timDau(>5)  : %d tai vi tri %d\n", a[vt], vt);
    printf("demNeu(le)  : %d\n", demNeu(a, n, laLe));
    printf("coMot(>8)   : %s\n", coMot(a, n, lonHon8) ? "true" : "false");
    printf("tatCa(>0)   : %s\n", tatCa(a, n, duong)   ? "true" : "false");
    printf("khongCo(<0) : %s\n", khongCo(a, n, am)    ? "true" : "false");
    return 0;
}
```

Output:

```
timDau(>5)  : 7 tai vi tri 1
demNeu(le)  : 6
coMot(>8)   : true
tatCa(>0)   : true
khongCo(<0) : true
```

**Bảng các hàm tìm kiếm tổng quát vừa viết:**

| Hàm | Tác dụng | Trả về |
|---|---|---|
| `timDau(a, n, dk)` | Tìm phần tử đầu tiên thoả `dk` | Chỉ số, hoặc `-1` |
| `demNeu(a, n, dk)` | Đếm phần tử thoả `dk` | Số nguyên |
| `coMot(a, n, dk)` | Có **ít nhất một** phần tử thoả? | `bool` |
| `tatCa(a, n, dk)` | **Tất cả** đều thoả? | `bool` |
| `khongCo(a, n, dk)` | **Không** phần tử nào thoả? | `bool` |

💡 **Con trỏ hàm** (`bool (*)(int)`) cho phép truyền "điều kiện" như một tham số — cùng ý tưởng với hàm so sánh truyền vào `qsort`.

⚠️ **Luôn kiểm tra kết quả `!= -1`** trước khi dùng `a[vt]` — nếu không tìm thấy, `a[-1]` là truy cập ngoài mảng.

### Bài 7.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Chuyen chuoi src sang chu thuong, ghi vao dst
void toLower(char *dst, const char *src) {
    while (*src) *dst++ = (char)tolower((unsigned char)*src++);
    *dst = '\0';
}

int main(void) {
    char ds[][50] = {
        "Lap trinh C", "Hoc Python", "Thuat toan va CTDL",
        "Lap trinh Web", "Co so du lieu"
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    char canTim[50];
    printf("Nhap tu khoa tim kiem: ");
    if (fgets(canTim, sizeof(canTim), stdin) == NULL) return 0;
    canTim[strcspn(canTim, "\n")] = '\0';     // bo ky tu xuong dong

    char tk[50], tam[50];
    toLower(tk, canTim);

    int ketQua[5], soKQ = 0;
    for (int i = 0; i < n; i++) {
        toLower(tam, ds[i]);
        if (strstr(tam, tk) != NULL) ketQua[soKQ++] = i;
    }

    printf("\nTim thay %d ket qua:\n", soKQ);
    for (int k = 0; k < soKQ; k++)
        printf("  [%d] %s\n", ketQua[k], ds[ketQua[k]]);

    if (soKQ == 0) printf("  (khong co ket qua nao)\n");
    return 0;
}
```

Ví dụ với từ khoá `"lap trinh"`:

```
Tim thay 2 ket qua:
  [0] Lap trinh C
  [3] Lap trinh Web
```

💡 `strstr(s, t)` trả về con trỏ tới lần xuất hiện đầu tiên của `t` trong `s`, hoặc `NULL` nếu không có.

💡 Chuyển cả 2 vế về chữ thường để tìm kiếm **không phân biệt hoa/thường** — đúng như người dùng mong đợi.

⚠️ `fgets` giữ lại ký tự `'\n'` cuối chuỗi — phải xoá đi, nếu không `"lap trinh\n"` sẽ không khớp với chuỗi nào.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    int    maSV;
    char   ten[30];
    int    tuoi;
    double diem;
} SinhVien;

int main(void) {
    SinhVien ds[] = {
        {101, "An",    20, 8.5},
        {102, "Binh",  22, 9.0},
        {103, "Chi",   21, 7.5},
        {104, "Dung",  20, 9.0},
        {105, "Em",    23, 6.5}
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    // (1) Tim theo MA SV - tra ve con tro, NULL neu khong co
    int ma = 103;
    const SinhVien *p = NULL;
    for (int i = 0; i < n; i++)
        if (ds[i].maSV == ma) { p = &ds[i]; break; }
    if (p != NULL)
        printf("Ma %d: %s, %.1f diem\n", ma, p->ten, p->diem);

    // (2) Tim theo TEN - so sanh chuoi bang strcmp
    const char *ten = "Dung";
    for (int i = 0; i < n; i++)
        if (strcmp(ds[i].ten, ten) == 0) {
            printf("Ten %s: ma %d\n", ten, ds[i].maSV);
            break;
        }

    // (3) Tim TAT CA sinh vien diem >= 9.0
    printf("\nSinh vien diem >= 9.0:\n");
    for (int i = 0; i < n; i++)
        if (ds[i].diem >= 9.0)
            printf("  %s (%.1f)\n", ds[i].ten, ds[i].diem);

    // (4) Dem sinh vien 20 tuoi
    int dem = 0;
    for (int i = 0; i < n; i++) if (ds[i].tuoi == 20) dem++;
    printf("\nSo sinh vien 20 tuoi: %d\n", dem);
    return 0;
}
```

Output:

```
Ma 103: Chi, 7.5 diem
Ten Dung: ma 104

Sinh vien diem >= 9.0:
  Binh (9.0)
  Dung (9.0)

So sinh vien 20 tuoi: 2
```

💡 `p->ten` tương đương `(*p).ten` — toán tử `->` gọn hơn khi truy cập thành viên qua con trỏ.

⚠️ Không so sánh chuỗi bằng `ds[i].ten == ten` — phép đó so sánh **địa chỉ**, không phải nội dung. Phải dùng `strcmp`.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define N 1000000
#define SO_TRUY_VAN 1000

int cmpInt(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

bool timTuyenTinh(const int a[], int n, int x) {
    for (int i = 0; i < n; i++) if (a[i] == x) return true;
    return false;
}

bool timNhiPhan(const int a[], int n, int x) {
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (a[m] == x) return true;
        if (a[m] < x) l = m + 1; else r = m - 1;
    }
    return false;
}

double msTu(clock_t t) { return (double)(clock() - t) * 1000 / CLOCKS_PER_SEC; }

int main(void) {
    int *v = malloc(N * sizeof(int));
    int *w = malloc(N * sizeof(int));
    if (!v || !w) return 1;
    for (int i = 0; i < N; i++) v[i] = w[i] = (int)((i * 7919LL + 13) % N);

    long long dem = 0;              // dung ket qua de compiler khong bo vong lap

    // KICH BAN 1: sap xep truoc
    clock_t t = clock();
    qsort(w, N, sizeof(int), cmpInt);
    double tSort = msTu(t);
    printf("Thoi gian sap xep     : %.0f ms\n", tSort);

    // Tim tuyen tinh nhieu lan
    t = clock();
    for (int i = 0; i < SO_TRUY_VAN; i++) dem += timTuyenTinh(v, N, i);
    double tTT = msTu(t);

    // Tim nhi phan nhieu lan
    t = clock();
    for (int i = 0; i < SO_TRUY_VAN; i++) dem += timNhiPhan(w, N, i);
    double tNP = msTu(t);

    printf("\n%d truy van (tim thay %lld lan):\n", SO_TRUY_VAN, dem);
    printf("  Tuyen tinh        : %.0f ms\n", tTT);
    printf("  Nhi phan          : %.3f ms\n", tNP);
    printf("  Nhi phan + sap xep: %.0f ms\n", tSort + tNP);

    free(v); free(w);
    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Tuyến tính | Nhị phân |
|---|---|---|
| **Yêu cầu sắp xếp** | ❌ **Không** | ✅ **Bắt buộc** |
| Độ phức tạp | O(n) | **O(log n)** |
| Với n = 10⁶ | ~10⁶ phép so sánh | **~20** phép so sánh |
| Chi phí chuẩn bị | 0 | O(n log n) để sắp xếp |
| Hoạt động với danh sách liên kết | ✅ Có | ❌ Không (cần truy cập ngẫu nhiên theo chỉ số) |
| Code | ✅ Rất đơn giản | Phức tạp hơn |

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Tìm **1–2 lần**, mảng chưa sắp | **Tuyến tính** (khỏi tốn công sắp) |
| Tìm **nhiều lần** trên cùng dữ liệu | **Sắp xếp một lần + nhị phân** |
| Dữ liệu **thay đổi liên tục** | Tuyến tính, hoặc cấu trúc dữ liệu chuyên dụng (cây, bảng băm) |
| Mảng **đã sắp sẵn** | **Nhị phân** |
| Tìm theo **điều kiện phức tạp** (không phải so sánh giá trị) | **Tuyến tính** |

**Công thức quyết định:** với `q` truy vấn, tìm tuyến tính tốn khoảng `q × n`, còn sắp xếp rồi tìm nhị phân tốn khoảng `n log n + q × log n`. Bỏ qua số hạng nhỏ, cách thứ hai lợi hơn khi `q` lớn hơn cỡ `log n`. Với `n = 10⁶`, ngưỡng là khoảng **20 truy vấn** (thực tế còn phụ thuộc hằng số của từng cách cài đặt).

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 50000000

// Tim kiem THONG THUONG: moi vong 2 phep so sanh (i < n VA a[i] == x)
int timThuong(const int a[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i;
    return -1;
}

// Tim kiem voi LINH CANH: moi vong chi 1 phep so sanh
int timLinhCanh(int a[], int n, int x) {
    if (n == 0) return -1;

    int cuoiCung = a[n - 1];
    a[n - 1] = x;                        // dat "linh canh" o cuoi

    int i = 0;
    while (a[i] != x) i++;               // KHONG can kiem tra i < n!

    a[n - 1] = cuoiCung;                 // khoi phuc

    if (i < n - 1) return i;
    return (cuoiCung == x) ? n - 1 : -1;
}

int main(void) {
    int *v = malloc((size_t)N * sizeof(int));
    if (v == NULL) { printf("Khong du bo nho\n"); return 1; }
    for (int i = 0; i < N; i++) v[i] = i;

    int x = N - 1;                        // truong hop xau nhat

    clock_t t = clock();
    int r1 = timThuong(v, N, x);
    printf("Thong thuong: %.0f ms (ket qua %d)\n",
           (double)(clock() - t) * 1000 / CLOCKS_PER_SEC, r1);

    t = clock();
    int r2 = timLinhCanh(v, N, x);
    printf("Linh canh   : %.0f ms (ket qua %d)\n",
           (double)(clock() - t) * 1000 / CLOCKS_PER_SEC, r2);

    printf("\nKet qua giong nhau: %s\n", r1 == r2 ? "true" : "false");
    free(v);
    return 0;
}
```

**Kỹ thuật "lính canh" (sentinel):** đặt giá trị cần tìm vào **cuối mảng**, đảm bảo vòng lặp **chắc chắn dừng**. Nhờ đó bỏ được phép kiểm tra biên `i < n` mỗi vòng.

```
Thong thuong: kiem tra (i < n) VA (a[i] == x)   -> 2 phep so sanh
Linh canh   : chi kiem tra (a[i] == x)           -> 1 phep so sanh
```

⚠️ **Nhược điểm:** phải **sửa mảng** (rồi khôi phục) — không dùng được với mảng `const`, và không an toàn khi nhiều luồng cùng đọc mảng.

⚠️ Với compiler hiện đại và `-O2`, chênh lệch thường rất nhỏ (có khi không đo được) vì compiler đã tự tối ưu vòng lặp thường. Đây chủ yếu là kỹ thuật mang tính học thuật.

### Bài 11.

```c
#include <stdio.h>
#include <stdbool.h>

#define HANG 3
#define COT  4

// Tra ve true neu tim thay, vi tri ghi qua con tro *h, *c
bool timTrongMaTran(const int a[HANG][COT], int x, int *h, int *c) {
    for (int i = 0; i < HANG; i++)
        for (int j = 0; j < COT; j++)
            if (a[i][j] == x) { *h = i; *c = j; return true; }
    return false;
}

int main(void) {
    const int m[HANG][COT] = {
        {1, 5, 3, 7},
        {9, 2, 5, 4},
        {6, 8, 1, 5}
    };

    printf("Ma tran:\n");
    for (int i = 0; i < HANG; i++) {
        for (int j = 0; j < COT; j++) printf("%4d", m[i][j]);
        printf("\n");
    }

    int canTim[] = {5, 9, 100};
    for (int k = 0; k < 3; k++) {
        int x = canTim[k], i, j;
        printf("\nTim %d: ", x);
        if (timTrongMaTran(m, x, &i, &j)) printf("thay tai (%d, %d)\n", i, j);
        else                              printf("khong tim thay\n");

        // Tat ca vi tri
        int dem = 0;
        for (int r = 0; r < HANG; r++)
            for (int c = 0; c < COT; c++)
                if (m[r][c] == x) dem++;
        if (dem > 1) {
            printf("  Tat ca vi tri: ");
            for (int r = 0; r < HANG; r++)
                for (int c = 0; c < COT; c++)
                    if (m[r][c] == x) printf("(%d,%d) ", r, c);
            printf("\n");
        }
    }
    return 0;
}
```

Output:

```
Ma tran:
   1   5   3   7
   9   2   5   4
   6   8   1   5

Tim 5: thay tai (0, 1)
  Tat ca vi tri: (0,1) (1,2) (2,3) 

Tim 9: thay tai (1, 0)

Tim 100: khong tim thay
```

💡 C không trả về được 2 giá trị cùng lúc, nên ta trả `bool` báo tìm thấy hay không, còn **hàng, cột** được ghi qua **con trỏ** `int *h, int *c`.

Độ phức tạp **O(n×m)** — duyệt toàn bộ ma trận.

💡 Nếu ma trận **đã sắp xếp theo hàng và cột**, có thuật toán O(n+m): bắt đầu từ góc trên-phải, nếu giá trị lớn hơn thì sang trái, nhỏ hơn thì xuống dưới.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>

int timGanNhat(const int a[], int n, int x) {
    if (n == 0) return -1;

    int viTri = 0;
    long long kcMin = llabs((long long)a[0] - x);

    for (int i = 1; i < n; i++) {
        long long kc = llabs((long long)a[i] - x);
        if (kc < kcMin) { kcMin = kc; viTri = i; }
    }
    return viTri;
}

int main(void) {
    int a[] = {10, 3, 25, 7, 18, 1, 30};
    int n = sizeof(a) / sizeof(a[0]);
    int x;

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    printf("Nhap gia tri x: ");
    if (scanf("%d", &x) != 1) return 0;

    int vt = timGanNhat(a, n, x);
    printf("Phan tu gan %d nhat: %d (vi tri %d, cach %d)\n",
           x, a[vt], vt, abs(a[vt] - x));
    return 0;
}
```

Với `x = 15`: kết quả là `18` (cách 3).

💡 Dùng `llabs` với `long long` để hiệu `a[i] - x` không bị tràn số khi các giá trị gần giới hạn của `int`.

💡 Nếu mảng **đã sắp xếp**, dùng hàm `lower_bound` tự viết cho **O(log n)** thay vì O(n) — xem bài [10-06](../10-06-c-ham-bsearch-va-lower-bound-upper-bound.md).

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct { int giaTri; int viTri; } Muc;

// Cach 1: duyet moi cap - O(n^2)
int timCapNgayTho(const int a[], int n, int x, int *i1, int *j1) {
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (a[i] + a[j] == x) { *i1 = i; *j1 = j; return 1; }
    return 0;
}

int cmpMuc(const void *p, const void *q) {
    const Muc *a = p, *b = q;
    return (a->giaTri > b->giaTri) - (a->giaTri < b->giaTri);
}

// Cach 2: sap xep + hai con tro - O(n log n)
int timCapToiUu(const int a[], int n, int x, int *i1, int *j1) {
    Muc *m = malloc(n * sizeof(Muc));
    if (m == NULL) return 0;
    for (int i = 0; i < n; i++) { m[i].giaTri = a[i]; m[i].viTri = i; }
    qsort(m, n, sizeof(Muc), cmpMuc);

    int trai = 0, phai = n - 1, thay = 0;
    while (trai < phai) {
        long long tong = (long long)m[trai].giaTri + m[phai].giaTri;
        if (tong == x) { thay = 1; break; }
        if (tong < x) trai++;         // can tong LON hon -> dich trai sang phai
        else          phai--;         // can tong NHO hon -> dich phai sang trai
    }
    if (thay) {
        *i1 = m[trai].viTri; *j1 = m[phai].viTri;
        if (*i1 > *j1) { int t = *i1; *i1 = *j1; *j1 = t; }
    }
    free(m);
    return thay;
}

int main(void) {
    int a[] = {2, 7, 11, 15, 3, 6};
    int n = sizeof(a) / sizeof(a[0]);
    int x = 9, i, j;

    printf("Cach 1 O(n^2)    : ");
    if (timCapNgayTho(a, n, x, &i, &j))
        printf("%d + %d = %d (vi tri %d, %d)\n", a[i], a[j], x, i, j);
    else printf("khong tim thay\n");

    printf("Cach 2 O(n log n): ");
    if (timCapToiUu(a, n, x, &i, &j))
        printf("%d + %d = %d (vi tri %d, %d)\n", a[i], a[j], x, i, j);
    else printf("khong tim thay\n");

    // So sanh toc do voi mang lon
    const int M = 20000;
    int *b = malloc(M * sizeof(int));
    if (b == NULL) return 1;
    for (int k = 0; k < M; k++) b[k] = k;
    int target = 2 * M - 3;                      // 2 phan tu cuoi

    clock_t t = clock();
    timCapNgayTho(b, M, target, &i, &j);
    printf("\nN = %d:\n", M);
    printf("  O(n^2)    : %.0f ms\n", (double)(clock() - t) * 1000 / CLOCKS_PER_SEC);

    t = clock();
    timCapToiUu(b, M, target, &i, &j);
    printf("  O(n log n): %.0f ms\n", (double)(clock() - t) * 1000 / CLOCKS_PER_SEC);
    free(b);
    return 0;
}
```

Kết quả tham khảo:

```
Cach 1 O(n^2)    : 2 + 7 = 9 (vi tri 0, 1)
Cach 2 O(n log n): 2 + 7 = 9 (vi tri 0, 1)

N = 20000:
  O(n^2)    : 69 ms
  O(n log n): 1 ms
```

💡 **Bài toán Two Sum** — một trong những bài phỏng vấn phổ biến nhất. Khi có nhiều cặp thoả mãn (ở đây `2 + 7` và `3 + 6` đều bằng 9), hai cách **không nhất thiết** trả về cùng một cặp.

💡 **Kỹ thuật hai con trỏ:** sau khi sắp xếp, đặt `trai` ở đầu, `phai` ở cuối. Tổng nhỏ quá thì tăng `trai`, lớn quá thì giảm `phai` — mỗi bước loại được một phần tử nên chỉ tốn O(n). Tổng thể **O(n log n)** do bước sắp xếp.

⚠️ Phải lưu kèm **vị trí gốc** (`struct Muc`) trước khi sắp xếp, nếu không sẽ mất thông tin phần tử nằm ở đâu trong mảng ban đầu.

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 20000000
#define SO_LAN 20

int timTuyenTinh(const int a[], int n, int x) {
    for (int i = 0; i < n; i++) if (a[i] == x) return i;
    return -1;
}

int main(void) {
    int *v = malloc((size_t)N * sizeof(int));
    if (v == NULL) { printf("Khong du bo nho\n"); return 1; }
    for (int i = 0; i < N; i++) v[i] = i;

    struct { const char *nhan; int giaTri; } bo[] = {
        {"Phan tu DAU     ", 0},
        {"Phan tu 1/4     ", N / 4},
        {"Phan tu GIUA    ", N / 2},
        {"Phan tu 3/4     ", 3 * (N / 4)},
        {"Phan tu CUOI    ", N - 1},
        {"KHONG TON TAI   ", -1}
    };

    printf("Mang %d phan tu, moi truong hop tim %d lan:\n", N, SO_LAN);
    printf("+------------------+------------+\n");
    printf("| TRUONG HOP       | THOI GIAN  |\n");
    printf("+------------------+------------+\n");

    long long tongViTri = 0;          // dung ket qua de compiler khong bo vong lap
    for (int k = 0; k < 6; k++) {
        clock_t t = clock();
        for (int lan = 0; lan < SO_LAN; lan++)
            tongViTri += timTuyenTinh(v, N, bo[k].giaTri);
        double ms = (double)(clock() - t) * 1000 / CLOCKS_PER_SEC;
        printf("| %s | %7.0f ms |\n", bo[k].nhan, ms);
    }
    printf("+------------------+------------+\n");
    printf("(kiem tra: %lld)\n", tongViTri);
    free(v);
    return 0;
}
```

Kết quả tham khảo:

```
+------------------+------------+
| TRUONG HOP       | THOI GIAN  |
+------------------+------------+
| Phan tu DAU      |       0 ms |
| Phan tu 1/4      |      34 ms |
| Phan tu GIUA     |      70 ms |
| Phan tu 3/4      |     102 ms |
| Phan tu CUOI     |     135 ms |
| KHONG TON TAI    |     154 ms |
+------------------+------------+
(kiem tra: 999999960)
```

**Phân tích độ phức tạp:**

| Trường hợp | Số phép so sánh | Ký hiệu |
|---|---|---|
| **Tốt nhất** — phần tử ở đầu | 1 | **O(1)** |
| **Trung bình** — vị trí ngẫu nhiên | n/2 | **O(n)** |
| **Xấu nhất** — ở cuối hoặc không có | n | **O(n)** |

💡 Thời gian **tỉ lệ thuận** với vị trí phần tử — đúng như lý thuyết. Đây là bản chất của O(n).

⚠️ Cộng dồn kết quả vào `tongViTri` và in ra cuối chương trình: nếu bỏ đi, compiler với `-O2` có thể nhận ra kết quả không được dùng và xoá luôn vòng lặp, khiến thời gian đo được bằng 0.

### Bài 15.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_KQ 10

typedef struct {
    char ten[40];
    char sdt[15];
    char email[40];
} LienHe;

void toLower(char *dst, const char *src) {
    while (*src) *dst++ = (char)tolower((unsigned char)*src++);
    *dst = '\0';
}

// Doc 1 dong, bo ky tu '\n' cuoi
void docDong(char *s, int kichThuoc) {
    if (fgets(s, kichThuoc, stdin) == NULL) { s[0] = '\0'; return; }
    s[strcspn(s, "\n")] = '\0';
}

// Xoa phan con lai cua dong hien tai trong bo dem nhap
void xoaBoDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {}
}

void hienThi(const LienHe ds[], const int viTri[], int soKQ) {
    if (soKQ == 0) { printf(">> Khong tim thay ket qua nao!\n"); return; }

    printf("+-----+--------------------+--------------+------------------------+\n");
    printf("| STT | HO TEN             | SO DIEN THOAI| EMAIL                  |\n");
    printf("+-----+--------------------+--------------+------------------------+\n");
    for (int k = 0; k < soKQ; k++) {
        int i = viTri[k];
        printf("| %-3d | %-18s | %-12s | %-22s |\n", i + 1, ds[i].ten, ds[i].sdt, ds[i].email);
    }
    printf("+-----+--------------------+--------------+------------------------+\n");
    printf(">> Tim thay %d ket qua.\n", soKQ);
}

int main(void) {
    LienHe ds[] = {
        {"Nguyen Van An",   "0912345678", "an.nguyen@gmail.com"},
        {"Tran Thi Binh",   "0387654321", "binh.tran@gmail.com"},
        {"Le Hoang Cuong",  "0905112233", "cuong.le@company.vn"},
        {"Pham Minh An",    "0788990011", "an.pham@gmail.com"},
        {"Hoang Thi Dung",  "0356778899", "dung.hoang@company.vn"}
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    int chon;
    do {
        printf("\n====== DANH BA ======\n");
        printf("1. Hien thi tat ca\n");
        printf("2. Tim theo TEN chinh xac\n");
        printf("3. Tim theo MOT PHAN ten\n");
        printf("4. Tim theo SO DIEN THOAI\n");
        printf("5. Tim theo EMAIL (mot phan)\n");
        printf("0. Thoat\n");
        printf("=====================\n");
        printf("Lua chon: ");

        int kq = scanf("%d", &chon);
        if (kq == EOF) break;
        xoaBoDem();                         // bo '\n' con lai sau scanf
        if (kq != 1) {
            printf(">> Nhap khong hop le!\n");
            chon = -1;
            continue;
        }

        int viTri[MAX_KQ], soKQ = 0;
        char tk[40], tkThuong[40], tam[40];

        switch (chon) {
            case 1:
                for (int i = 0; i < n; i++) viTri[soKQ++] = i;
                hienThi(ds, viTri, soKQ);
                break;

            case 2:
                printf("Nhap ten chinh xac: ");
                docDong(tk, sizeof(tk));
                toLower(tkThuong, tk);
                for (int i = 0; i < n; i++) {
                    toLower(tam, ds[i].ten);
                    if (strcmp(tam, tkThuong) == 0) viTri[soKQ++] = i;
                }
                hienThi(ds, viTri, soKQ);
                break;

            case 3:
                printf("Nhap mot phan ten: ");
                docDong(tk, sizeof(tk));
                toLower(tkThuong, tk);
                for (int i = 0; i < n; i++) {
                    toLower(tam, ds[i].ten);
                    if (strstr(tam, tkThuong) != NULL) viTri[soKQ++] = i;
                }
                hienThi(ds, viTri, soKQ);
                break;

            case 4:
                printf("Nhap so dien thoai: ");
                docDong(tk, sizeof(tk));
                for (int i = 0; i < n; i++)
                    if (strstr(ds[i].sdt, tk) != NULL) viTri[soKQ++] = i;
                hienThi(ds, viTri, soKQ);
                break;

            case 5:
                printf("Nhap mot phan email: ");
                docDong(tk, sizeof(tk));
                toLower(tkThuong, tk);
                for (int i = 0; i < n; i++) {
                    toLower(tam, ds[i].email);
                    if (strstr(tam, tkThuong) != NULL) viTri[soKQ++] = i;
                }
                hienThi(ds, viTri, soKQ);
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

Ví dụ chọn `3` rồi nhập `hoang` (tìm theo một phần tên):

```
+-----+--------------------+--------------+------------------------+
| STT | HO TEN             | SO DIEN THOAI| EMAIL                  |
+-----+--------------------+--------------+------------------------+
| 3   | Le Hoang Cuong     | 0905112233   | cuong.le@company.vn    |
| 5   | Hoang Thi Dung     | 0356778899   | dung.hoang@company.vn  |
+-----+--------------------+--------------+------------------------+
>> Tim thay 2 ket qua.
```

⚠️ Từ khoá quá ngắn sẽ khớp rất nhiều: nhập `an` sẽ ra cả 5 liên hệ, vì `"an"` nằm trong `"Tran"`, `"Hoang"`...

💡 **Vì sao danh bạ dùng tìm kiếm tuyến tính:**
1. Cho phép tìm theo **một phần** chuỗi (`strstr`) — nhị phân không làm được
2. Cho phép tìm theo **nhiều trường** khác nhau
3. Dữ liệu **thay đổi liên tục** (thêm/xoá liên hệ) — sắp xếp lại mỗi lần sẽ tốn hơn
4. Số lượng liên hệ thường nhỏ (vài trăm đến vài nghìn) → O(n) hoàn toàn chấp nhận được

⚠️ Sau `scanf("%d", ...)` ký tự `'\n'` vẫn còn trong bộ đệm — phải gọi `xoaBoDem()` trước khi đọc chuỗi bằng `fgets`, nếu không `fgets` sẽ đọc ngay một dòng rỗng.
