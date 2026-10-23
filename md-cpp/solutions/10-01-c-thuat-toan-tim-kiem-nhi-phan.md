# Lời giải — [C]. Thuật Toán Tìm Kiếm Nhị Phân

[← Quay lại bài học](../10-01-c-thuat-toan-tim-kiem-nhi-phan.md)

> **Điều kiện bắt buộc: mảng phải ĐÃ SẮP XẾP.** Mỗi bước loại bỏ một nửa không gian tìm kiếm → **O(log n)**.

---

### Bài 1.

```c
#include <stdio.h>

int timNhiPhan(int a[], int n, int x) {
    int trai = 0, phai = n - 1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if      (a[giua] == x) return giua;        // tim thay
        else if (a[giua] <  x) trai = giua + 1;    // tim o NUA PHAI
        else                   phai = giua - 1;    // tim o NUA TRAI
    }
    return -1;                                      // khong tim thay
}

int main(void) {
    int a[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    int n = 10;
    int ds[] = {23, 2, 91, 50};

    for (int i = 0; i < 4; i++) {
        int x = ds[i];
        int vt = timNhiPhan(a, n, x);
        printf("Tim %d: ", x);
        if (vt != -1) printf("thay tai vi tri %d\n", vt);
        else          printf("khong tim thay\n");
    }
    return 0;
}
```

⚠️ Chú ý `trai <= phai` (có dấu `=`) — nếu viết `<` thì bỏ sót trường hợp khoảng còn đúng 1 phần tử.

### Bài 2.

```c
#include <stdio.h>

int timNhiPhanDeQuy(int a[], int trai, int phai, int x) {
    if (trai > phai) return -1;                     // DIEU KIEN DUNG

    int giua = trai + (phai - trai) / 2;

    if (a[giua] == x) return giua;
    if (a[giua] <  x) return timNhiPhanDeQuy(a, giua + 1, phai, x);
    return timNhiPhanDeQuy(a, trai, giua - 1, x);
}

// Ham vo cho de goi
int timNhiPhan(int a[], int n, int x) {
    return timNhiPhanDeQuy(a, 0, n - 1, x);
}

int main(void) {
    int a[] = {2, 5, 8, 12, 16, 23, 38, 56, 72, 91};
    printf("Tim 38: vi tri %d\n", timNhiPhan(a, 10, 38));   // 6
    printf("Tim 50: vi tri %d\n", timNhiPhan(a, 10, 50));   // -1
    return 0;
}
```

💡 Đây là **đệ quy đuôi** — compiler với `-O2` thường tối ưu thành vòng lặp, nên không lo tràn stack. Độ sâu tối đa cũng chỉ `log₂(n)` (~30 với n = 10⁹).

### Bài 3.

```c
#include <stdio.h>

int timNhiPhanChiTiet(int a[], int n, int x) {
    int trai = 0, phai = n - 1, buoc = 0;

    printf("Tim gia tri %d trong mang %d phan tu:\n", x, n);
    printf("+-------+-------+-------+-------+------------+\n");
    printf("| Buoc  | trai  | giua  | phai  | a[giua]    |\n");
    printf("+-------+-------+-------+-------+------------+\n");

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        buoc++;

        // %5d: in so nguyen canh phai trong o rong 5 ky tu
        printf("| %5d | %5d | %5d | %5d | %10d |", buoc, trai, giua, phai, a[giua]);

        if (a[giua] == x) {
            printf("  <- TIM THAY!\n");
            printf("+-------+-------+-------+-------+------------+\n");
            return giua;
        } else if (a[giua] < x) {
            printf("  (nho hon -> sang PHAI)\n");
            trai = giua + 1;
        } else {
            printf("  (lon hon -> sang TRAI)\n");
            phai = giua - 1;
        }
    }

    printf("+-------+-------+-------+-------+------------+\n");
    printf("Khong tim thay sau %d buoc\n", buoc);
    return -1;
}

int main(void) {
    int a[16];
    for (int i = 0; i < 16; i++) a[i] = (i + 1) * 5;    // 5, 10, 15, ..., 80

    timNhiPhanChiTiet(a, 16, 65);
    return 0;
}
```

Output:

```
Tim gia tri 65 trong mang 16 phan tu:
+-------+-------+-------+-------+------------+
| Buoc  | trai  | giua  | phai  | a[giua]    |
+-------+-------+-------+-------+------------+
|     1 |     0 |     7 |    15 |         40 |  (nho hon -> sang PHAI)
|     2 |     8 |    11 |    15 |         60 |  (nho hon -> sang PHAI)
|     3 |    12 |    13 |    15 |         70 |  (lon hon -> sang TRAI)
|     4 |    12 |    12 |    12 |         65 |  <- TIM THAY!
+-------+-------+-------+-------+------------+
```

💡 Chỉ **4 bước** để tìm trong 16 phần tử — đúng bằng `log₂(16) = 4`.

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int demBuoc(const int a[], int n, int x) {
    int trai = 0, phai = n - 1, buoc = 0;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        buoc++;
        if      (a[giua] == x) return buoc;
        else if (a[giua] <  x) trai = giua + 1;
        else                   phai = giua - 1;
    }
    return buoc;
}

int main(void) {
    int cacN[] = {10, 100, 1000, 10000, 100000, 1000000};

    printf("+-----------+-----------+-----------+\n");
    printf("|     n     |Buoc toi da|  log2(n)  |\n");
    printf("+-----------+-----------+-----------+\n");

    for (int k = 0; k < 6; k++) {
        int n = cacN[k];
        int *a = malloc(n * sizeof(int));     // mang dong, n co the rat lon
        if (a == NULL) return 1;
        for (int i = 0; i < n; i++) a[i] = i;

        // Tim buoc TOI DA (tim gia tri khong ton tai)
        int maxBuoc = demBuoc(a, n, -1);

        printf("| %9d | %9d | %9.1f |\n", n, maxBuoc, log2(n));
        free(a);
    }
    printf("+-----------+-----------+-----------+\n");
    return 0;
}
```

Biên dịch nhớ thêm `-lm` vì dùng `log2` của `<math.h>`: `gcc bai4.c -o bai4 -lm`.

Output:

```
+-----------+-----------+-----------+
|     n     |Buoc toi da|  log2(n)  |
+-----------+-----------+-----------+
|        10 |         3 |       3.3 |
|       100 |         6 |       6.6 |
|      1000 |         9 |      10.0 |
|     10000 |        13 |      13.3 |
|    100000 |        16 |      16.6 |
|   1000000 |        19 |      19.9 |
+-----------+-----------+-----------+
```

**Nhận xét: số bước ≈ `log₂(n)`, tối đa `⌊log₂(n)⌋ + 1`.** Mỗi khi `n` tăng **gấp đôi**, chỉ cần thêm **1 bước**.

Với 1 tỷ phần tử, chỉ cần khoảng **30 bước** — trong khi tìm tuyến tính cần tới 1 tỷ.

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int timTuyenTinh(const int a[], int n, int x) {
    for (int i = 0; i < n; i++)
        if (a[i] == x) return i;
    return -1;
}

int timNhiPhan(const int a[], int n, int x) {
    int trai = 0, phai = n - 1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        if      (a[giua] == x) return giua;
        else if (a[giua] <  x) trai = giua + 1;
        else                   phai = giua - 1;
    }
    return -1;
}

int main(void) {
    const int N = 10000000;
    const int SO_LAN = 1000;

    int *a = malloc((size_t)N * sizeof(int));   // 40 MB: phai cap phat dong
    if (a == NULL) { printf("Khong du bo nho\n"); return 1; }
    for (int i = 0; i < N; i++) a[i] = i * 2;   // mang da sap xep

    // (1) Tuyen tinh
    clock_t t1 = clock();
    long long tong1 = 0;
    for (int i = 0; i < SO_LAN; i++) tong1 += timTuyenTinh(a, N, (N - 1) * 2);
    clock_t t2 = clock();
    double tt = (double)(t2 - t1) * 1000.0 / CLOCKS_PER_SEC;     // ms

    // (2) Nhi phan
    t1 = clock();
    long long tong2 = 0;
    for (int i = 0; i < SO_LAN; i++) tong2 += timNhiPhan(a, N, (N - 1) * 2);
    t2 = clock();
    double tnp = (double)(t2 - t1) * 1000.0 / CLOCKS_PER_SEC;    // ms

    printf("Mang %d phan tu, tim %d lan:\n", N, SO_LAN);
    printf("  Tuyen tinh : %.0f ms\n", tt);
    printf("  Nhi phan   : %.3f ms\n", tnp);
    if (tnp > 0) printf("  Nhanh hon  : %.0f lan\n", tt / tnp);
    else         printf("  Nhanh hon  : qua nhanh, clock() do khong kip\n");
    printf("\nKiem tra ket qua giong nhau: %s\n", tong1 == tong2 ? "OK" : "SAI");

    free(a);
    return 0;
}
```

Kết quả tham khảo (tuỳ máy):

```
Mang 10000000 phan tu, tim 1000 lan:
  Tuyen tinh : 25591 ms
  Nhi phan   : 0.105 ms
  Nhanh hon  : 243722 lan
```

💡 `clock()` có độ phân giải khá thô (thường 1 micro giây). Phần nhị phân nhanh tới mức có thể đo ra 0 — khi đó hãy tăng `SO_LAN`.

⚠️ **Nhưng:** tìm kiếm nhị phân yêu cầu mảng **đã sắp xếp** — bản thân việc sắp xếp tốn O(n log n). Nên:

| Số lần tìm | Nên dùng |
|---|---|
| 1–2 lần | Tuyến tính (khỏi sắp xếp) |
| Nhiều lần | **Sắp xếp một lần + nhị phân** |

### Bài 6.

```c
int giua = (trai + phai) / 2;       // NGUY HIEM: co the TRAN SO
```

**Lỗi:** với mảng rất lớn, `trai + phai` có thể vượt giới hạn `int`.

Ví dụ: `trai = 1.500.000.000`, `phai = 2.000.000.000`
```
trai + phai = 3.500.000.000  >  INT_MAX (2.147.483.647)
-> tran so -> giua thanh SO AM
-> a[giua] truy cap ngoai bien -> CRASH
```

Trong C, tràn số với `int` có dấu là **hành vi không xác định** (undefined behavior) — chương trình có thể cho kết quả bất kỳ.

**Sửa — công thức an toàn:**

```c
int giua = trai + (phai - trai) / 2;
```

**Vì sao an toàn:** `phai - trai` luôn ≤ `phai` nên không bao giờ tràn. Kết quả **hoàn toàn tương đương** về mặt toán học:

```
trai + (phai - trai)/2 = trai + phai/2 - trai/2 = (trai + phai)/2  ✔
```

💡 **Đây là lỗi lịch sử nổi tiếng:** thư viện chuẩn Java chứa lỗi này suốt **9 năm** (1997–2006) trong `Arrays.binarySearch`, được Joshua Bloch công bố năm 2006. Nó cho thấy ngay cả thuật toán đơn giản nhất cũng có thể ẩn chứa lỗi tinh vi.

Cách khác (dùng phép bit hoặc số không dấu):

```c
int giua = (trai + phai) >> 1;                  // van tran neu trai+phai tran
int giua = ((unsigned)trai + (unsigned)phai) / 2;   // an toan khi trai, phai >= 0
```

### Bài 7.

```c
#include <stdio.h>

int timDauTien(const int a[], int n, int x) {
    int trai = 0, phai = n - 1;
    int kq = -1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (a[giua] == x) {
            kq = giua;              // luu lai, nhung VAN TIM TIEP ben trai
            phai = giua - 1;
        } else if (a[giua] < x) {
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }
    return kq;
}

int main(void) {
    int a[] = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int ds[] = {2, 5, 4, 9};

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d(%d) ", a[i], i);
    printf("\n\n");

    for (int i = 0; i < 4; i++) {
        int vt = timDauTien(a, n, ds[i]);
        printf("Vi tri DAU TIEN cua %d: ", ds[i]);
        if (vt == -1) printf("khong co\n");
        else          printf("%d\n", vt);
    }
    return 0;
}
```

Output:

```
Vi tri DAU TIEN cua 2: 1
Vi tri DAU TIEN cua 5: 7
Vi tri DAU TIEN cua 4: 5
Vi tri DAU TIEN cua 9: khong co
```

💡 **Điểm mấu chốt:** khi tìm thấy, **không dừng ngay** mà lưu kết quả rồi tiếp tục thu hẹp về **bên trái** để tìm vị trí sớm hơn.

### Bài 8.

```c
#include <stdio.h>

int timCuoiCung(const int a[], int n, int x) {
    int trai = 0, phai = n - 1;
    int kq = -1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (a[giua] == x) {
            kq = giua;
            trai = giua + 1;        // tim tiep ben PHAI
        } else if (a[giua] < x) {
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }
    return kq;
}

int main(void) {
    int a[] = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int ds[] = {2, 5, 4, 9};

    for (int i = 0; i < 4; i++) {
        int vt = timCuoiCung(a, n, ds[i]);
        printf("Vi tri CUOI CUNG cua %d: ", ds[i]);
        if (vt == -1) printf("khong co\n");
        else          printf("%d\n", vt);
    }
    return 0;
}
```

Output:

```
Vi tri CUOI CUNG cua 2: 3
Vi tri CUOI CUNG cua 5: 10
Vi tri CUOI CUNG cua 4: 6
Vi tri CUOI CUNG cua 9: khong co
```

💡 Chỉ khác bài 7 đúng **một dòng**: `trai = giua + 1` thay vì `phai = giua - 1`.

### Bài 9.

```c
#include <stdio.h>

int timDauTien(const int a[], int n, int x) {
    int trai = 0, phai = n - 1, kq = -1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        if (a[giua] == x) { kq = giua; phai = giua - 1; }
        else if (a[giua] < x) trai = giua + 1;
        else phai = giua - 1;
    }
    return kq;
}

int timCuoiCung(const int a[], int n, int x) {
    int trai = 0, phai = n - 1, kq = -1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        if (a[giua] == x) { kq = giua; trai = giua + 1; }
        else if (a[giua] < x) trai = giua + 1;
        else phai = giua - 1;
    }
    return kq;
}

int demSoLan(const int a[], int n, int x) {
    int dau = timDauTien(a, n, x);
    if (dau == -1) return 0;
    return timCuoiCung(a, n, x) - dau + 1;
}

// Dem kiem chung bang vong lap O(n)
int demTuyenTinh(const int a[], int n, int x) {
    int d = 0;
    for (int i = 0; i < n; i++) if (a[i] == x) d++;
    return d;
}

int main(void) {
    int a[] = {1, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int ds[] = {2, 5, 1, 9};

    for (int i = 0; i < 4; i++) {
        int x = ds[i];
        printf("So %d xuat hien %d lan", x, demSoLan(a, n, x));
        printf("  (kiem chung: %d)\n", demTuyenTinh(a, n, x));
    }
    return 0;
}
```

Output:

```
So 2 xuat hien 3 lan  (kiem chung: 3)
So 5 xuat hien 4 lan  (kiem chung: 4)
So 1 xuat hien 1 lan  (kiem chung: 1)
So 9 xuat hien 0 lan  (kiem chung: 0)
```

**Độ phức tạp O(log n)** — nhanh hơn hẳn cách đếm bằng vòng lặp (O(n)) khi mảng đã sắp xếp.

💡 Thư viện chuẩn C không có hàm đếm kiểu này, nên cặp hàm "vị trí đầu / vị trí cuối" tự viết là công cụ rất hay dùng.

### Bài 10.

```c
#include <stdio.h>

// Tim vi tri dau tien co a[i] >= x  (lower bound)
int lowerBound(const int a[], int n, int x) {
    int trai = 0, phai = n;               // chu y: phai = n, khong phai n-1

    while (trai < phai) {                  // chu y: dau < khong phai <=
        int giua = trai + (phai - trai) / 2;
        if (a[giua] < x) trai = giua + 1;
        else             phai = giua;
    }
    return trai;                            // co the = n neu moi phan tu < x
}

// Tim vi tri dau tien co a[i] > x  (upper bound)
int upperBound(const int a[], int n, int x) {
    int trai = 0, phai = n;
    while (trai < phai) {
        int giua = trai + (phai - trai) / 2;
        if (a[giua] <= x) trai = giua + 1;
        else              phai = giua;
    }
    return trai;
}

// Kiem chung bang cach duyet tuan tu
int lowerBoundCham(const int a[], int n, int x) {
    int i = 0;
    while (i < n && a[i] < x) i++;
    return i;
}

int main(void) {
    int a[] = {1, 3, 3, 5, 7, 7, 7, 9};
    int n = sizeof(a) / sizeof(a[0]);
    int ds[] = {3, 7, 4, 0, 10};

    printf("Mang: ");
    for (int i = 0; i < n; i++) printf("%d(%d) ", a[i], i);
    printf("\n\n");

    for (int i = 0; i < 5; i++) {
        int x = ds[i];
        int lb = lowerBound(a, n, x);
        int ub = upperBound(a, n, x);
        printf("x = %d: lower_bound = %d, upper_bound = %d, so lan xuat hien = %d\n",
               x, lb, ub, ub - lb);

        if (lb != lowerBoundCham(a, n, x)) printf("  !!! KHONG KHOP\n");
    }
    return 0;
}
```

Output:

```
x = 3: lower_bound = 1, upper_bound = 3, so lan xuat hien = 2
x = 7: lower_bound = 4, upper_bound = 7, so lan xuat hien = 3
x = 4: lower_bound = 3, upper_bound = 3, so lan xuat hien = 0
x = 0: lower_bound = 0, upper_bound = 0, so lan xuat hien = 0
x = 10: lower_bound = 8, upper_bound = 8, so lan xuat hien = 0
```

⚠️ **3 khác biệt so với tìm kiếm nhị phân thường:**
1. `phai = n` (không phải `n - 1`)
2. Điều kiện `trai < phai` (không phải `<=`)
3. `phai = giua` (không phải `giua - 1`)

Chi tiết xem bài [10-06](../10-06-c-ham-bsearch-va-lower-bound-upper-bound.md).

### Bài 11.

```c
#include <stdio.h>

// Tim can bac hai NGUYEN: so lon nhat k thoa k*k <= n
long long canBacHai(long long n) {
    if (n < 0) return -1;
    if (n < 2) return n;

    long long trai = 1, phai = n, kq = 0;

    while (trai <= phai) {
        long long giua = trai + (phai - trai) / 2;

        if (giua <= n / giua) {           // tranh tran: thay vi giua*giua <= n
            kq = giua;
            trai = giua + 1;
        } else {
            phai = giua - 1;
        }
    }
    return kq;
}

int main(void) {
    long long ds[] = {0, 1, 4, 8, 16, 100, 1000000000000LL};

    for (int i = 0; i < 7; i++) {
        long long n = ds[i];
        long long c = canBacHai(n);
        printf("canBacHai(%lld) = %lld  (%lld^2 = %lld)\n", n, c, c, c * c);
    }
    return 0;
}
```

Output:

```
canBacHai(0) = 0  (0^2 = 0)
canBacHai(1) = 1  (1^2 = 1)
canBacHai(4) = 2  (2^2 = 4)
canBacHai(8) = 2  (2^2 = 4)
canBacHai(16) = 4  (4^2 = 16)
canBacHai(100) = 10  (10^2 = 100)
canBacHai(1000000000000) = 1000000  (1000000^2 = 1000000000000)
```

💡 **Đây là "tìm kiếm nhị phân trên đáp án"** — không tìm trong mảng, mà tìm trong **khoảng giá trị có thể**. Điều kiện: hàm phải **đơn điệu** (ở đây `k²` tăng dần theo `k`).

⚠️ **Dùng `giua <= n / giua` thay vì `giua * giua <= n`** để tránh tràn số với `n` rất lớn.

### Bài 12.

```c
#include <stdio.h>

int timTrongMangXoay(const int a[], int n, int x) {
    int trai = 0, phai = n - 1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (a[giua] == x) return giua;

        // Xac dinh NUA NAO da sap xep
        if (a[trai] <= a[giua]) {
            // Nua TRAI da sap xep
            if (a[trai] <= x && x < a[giua]) phai = giua - 1;
            else                             trai = giua + 1;
        } else {
            // Nua PHAI da sap xep
            if (a[giua] < x && x <= a[phai]) trai = giua + 1;
            else                             phai = giua - 1;
        }
    }
    return -1;
}

int main(void) {
    int a[] = {4, 5, 6, 7, 0, 1, 2, 3};
    int n = sizeof(a) / sizeof(a[0]);
    int ds[] = {0, 4, 3, 8};

    printf("Mang xoay: ");
    for (int i = 0; i < n; i++) printf("%d(%d) ", a[i], i);
    printf("\n\n");

    for (int i = 0; i < 4; i++) {
        int vt = timTrongMangXoay(a, n, ds[i]);
        printf("Tim %d: ", ds[i]);
        if (vt == -1) printf("khong tim thay\n");
        else          printf("vi tri %d\n", vt);
    }
    return 0;
}
```

Output:

```
Tim 0: vi tri 4
Tim 4: vi tri 0
Tim 3: vi tri 7
Tim 8: khong tim thay
```

**Ý tưởng:** trong mảng xoay, **luôn có ít nhất một nửa đã sắp xếp**. Xác định nửa nào, rồi kiểm tra `x` có nằm trong khoảng đó không để quyết định đi hướng nào.

Vẫn giữ được **O(log n)** — đây là bài toán phỏng vấn kinh điển (LeetCode 33).

### Bài 13.

```c
#include <stdio.h>
#include <stdbool.h>

// BAI TOAN: co n bo keo, moi bo a[i] cai. Chia deu cho m em, moi em nhan
// dung k cai (co the bo thua keo). Tim k LON NHAT.

bool duChia(const int a[], int n, int m, int k) {
    if (k == 0) return true;
    long long soPhan = 0;
    for (int i = 0; i < n; i++) soPhan += a[i] / k;
    return soPhan >= m;
}

int timKLonNhat(const int a[], int n, int m) {
    int maxA = a[0];
    for (int i = 1; i < n; i++) if (a[i] > maxA) maxA = a[i];

    int trai = 1, phai = maxA;
    int kq = 0;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;

        if (duChia(a, n, m, giua)) {
            kq = giua;                // duoc -> thu gia tri LON HON
            trai = giua + 1;
        } else {
            phai = giua - 1;          // khong duoc -> thu NHO HON
        }
    }
    return kq;
}

int main(void) {
    int a[] = {5, 8, 11, 15};            // 4 bo keo
    int n = 4;
    int m = 10;                           // chia cho 10 em

    int k = timKLonNhat(a, n, m);
    printf("Cac bo keo: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\nSo em: %d\n", m);
    printf("Moi em nhan toi da: %d cai keo\n", k);

    // Kiem chung
    int tong = 0;
    for (int i = 0; i < n; i++) tong += a[i] / k;
    printf("Kiem chung: chia duoc %d phan (>= %d)\n", tong, m);
    return 0;
}
```

Output:

```
Cac bo keo: 5 8 11 15 
So em: 10
Moi em nhan toi da: 3 cai keo
Kiem chung: chia duoc 11 phan (>= 10)
```

**Mẫu "tìm kiếm nhị phân trên đáp án":**

```c
int trai = min_dap_an, phai = max_dap_an, kq = -1;
while (trai <= phai) {
    int giua = trai + (phai - trai) / 2;
    if (kiemTra(giua)) { kq = giua; /* thu tot hon */ }
    else               { /* thu te hon */ }
}
```

**Điều kiện áp dụng:** hàm `kiemTra` phải **đơn điệu** — nếu `k` thoả thì mọi `k' < k` cũng thoả (hoặc ngược lại).

💡 Đây là kỹ thuật cực kỳ mạnh trong lập trình thi đấu — biến bài toán tối ưu thành bài toán kiểm tra đơn giản hơn nhiều.

### Bài 14.

```c
#include <stdio.h>
#include <string.h>

int timChuoi(char ds[][20], int n, const char *x) {
    int trai = 0, phai = n - 1;

    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        int ss = strcmp(ds[giua], x);     // <0: ds[giua] dung truoc x

        if      (ss == 0) return giua;
        else if (ss <  0) trai = giua + 1;
        else              phai = giua - 1;
    }
    return -1;
}

int main(void) {
    // Mang chuoi DA SAP XEP theo thu tu tu dien
    char ds[][20] = {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"};
    int n = sizeof(ds) / sizeof(ds[0]);
    const char *canTim[] = {"cherry", "apple", "grape", "kiwi"};

    printf("Danh sach: ");
    for (int i = 0; i < n; i++) printf("%s ", ds[i]);
    printf("\n\n");

    for (int i = 0; i < 4; i++) {
        int vt = timChuoi(ds, n, canTim[i]);
        printf("Tim \"%s\": ", canTim[i]);
        if (vt == -1) printf("khong tim thay\n");
        else          printf("vi tri %d\n", vt);
    }
    return 0;
}
```

Output:

```
Danh sach: apple banana cherry date elderberry fig grape 

Tim "cherry": vi tri 2
Tim "apple": vi tri 0
Tim "grape": vi tri 6
Tim "kiwi": khong tim thay
```

💡 Trong C không so sánh chuỗi bằng `==` hay `<` (đó là so sánh **địa chỉ**). Phải dùng `strcmp`: trả về số âm, 0, hoặc số dương. Cùng một khung thuật toán, chỉ thay phép so sánh — áp dụng được cho mọi kiểu dữ liệu có thứ tự.

⚠️ **Nhớ sắp xếp trước!** Đây là lỗi phổ biến nhất — thuật toán không báo lỗi, chỉ cho kết quả sai. Cách sắp xếp mảng chuỗi bằng `qsort` xem bài [10-03](../10-03-c-xay-dung-ham-so-sanh-cho-qsort.md).

### Bài 15.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    const int MIN = 1, MAX = 1000;

    printf("============================================\n");
    printf("  MAY SE DOAN SO CUA BAN (tu %d den %d)\n", MIN, MAX);
    printf("============================================\n");
    printf("Hay nghi mot so, roi tra loi:\n");
    printf("  'l' neu so cua ban LON HON\n");
    printf("  'n' neu so cua ban NHO HON\n");
    printf("  'd' neu DUNG roi\n\n");

    int trai = MIN, phai = MAX, soLan = 0;

    while (trai <= phai) {
        int doan = trai + (phai - trai) / 2;
        soLan++;

        printf("Lan %d - May doan: %d  (con %d kha nang)\n", soLan, doan, phai - trai + 1);
        printf("  Tra loi (l/n/d): ");

        char tl;
        if (scanf(" %c", &tl) != 1) return 0;     // dau cach truoc %c: bo qua Enter
        tl = (char)tolower((unsigned char)tl);

        if (tl == 'd') {
            printf("\nMay doan dung sau %d lan!\n", soLan);
            printf("(Toi da can %d lan cho khoang 1-1000)\n", 10);
            return 0;
        } else if (tl == 'l') {
            trai = doan + 1;
        } else if (tl == 'n') {
            phai = doan - 1;
        } else {
            printf("  Cau tra loi khong hop le, thu lai!\n");
            soLan--;
        }
    }

    printf("\nBan da tra loi MAU THUAN! Khong co so nao thoa man.\n");
    return 0;
}
```

Ví dụ chạy (người chơi nghĩ số 777):

```
Lan 1 - May doan: 500  (con 1000 kha nang)
  Tra loi (l/n/d): l
Lan 2 - May doan: 750  (con 500 kha nang)
  Tra loi (l/n/d): l
Lan 3 - May doan: 875  (con 250 kha nang)
  Tra loi (l/n/d): n
Lan 4 - May doan: 812  (con 124 kha nang)
  Tra loi (l/n/d): n
Lan 5 - May doan: 781  (con 61 kha nang)
  Tra loi (l/n/d): n
Lan 6 - May doan: 765  (con 30 kha nang)
  Tra loi (l/n/d): l
Lan 7 - May doan: 773  (con 15 kha nang)
  Tra loi (l/n/d): l
Lan 8 - May doan: 777  (con 7 kha nang)
  Tra loi (l/n/d): d

May doan dung sau 8 lan!
(Toi da can 10 lan cho khoang 1-1000)
```

⚠️ Viết `scanf(" %c", &tl)` (có **dấu cách** trước `%c`) để bỏ qua ký tự Enter còn sót lại từ lần nhập trước — nếu không, vòng lặp sẽ đọc phải `'\n'` và báo "không hợp lệ".

💡 **Máy luôn thắng trong tối đa `⌈log₂(1000)⌉ = 10` lần đoán** — vì mỗi câu trả lời loại bỏ đúng một nửa khả năng.

Đây là minh hoạ trực quan nhất cho sức mạnh của tìm kiếm nhị phân:

| Khoảng số | Số lần đoán tối đa |
|---|---|
| 1–100 | 7 |
| 1–1.000 | 10 |
| 1–1.000.000 | 20 |
| 1–1 tỷ | 30 |
