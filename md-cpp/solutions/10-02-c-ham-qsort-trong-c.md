# Lời giải — [C]. Hàm qsort Trong C

[← Quay lại bài học](../10-02-c-ham-qsort-trong-c.md)

> `qsort` nằm trong `<stdlib.h>`: `qsort(mang, so_phan_tu, sizeof(mang[0]), ham_so_sanh)`. Hàm so sánh trả về **số âm** nếu `a` đứng trước, **số dương** nếu `a` đứng sau, **0** nếu bằng nhau.

---

### Bài 1.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main(void) {
    int n;
    printf("Nhap n: ");
    if (scanf("%d", &n) != 1 || n <= 0) return 1;

    int *a = malloc(n * sizeof(int));
    if (a == NULL) return 1;

    printf("Nhap %d so: ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    qsort(a, n, sizeof(a[0]), cmpTang);

    printf("Mang tang dan: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    free(a);
    return 0;
}
```

Ví dụ chạy:

```
Nhap n: 6
Nhap 6 so: 5 2 9 1 7 3
Mang tang dan: 1 2 3 5 7 9 
```

💡 **4 tham số của `qsort`:** địa chỉ đầu mảng, số phần tử, kích thước **một** phần tử, tên hàm so sánh. Viết `sizeof(a[0])` thay vì `sizeof(int)` để khi đổi kiểu mảng không phải sửa lại.

### Bài 2.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int cmpGiam(const void *a, const void *b) {
    return cmpTang(b, a);            // doi cho 2 tham so -> dao nguoc thu tu
}

void daoNguoc(int a[], int n) {
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }
}

void inMang(const char *nhan, const int a[], int n) {
    printf("%s", nhan);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[] = {5, 2, 9, 1, 7, 3};
    int b[] = {5, 2, 9, 1, 7, 3};
    int n = 6;

    // Cach 1: ham so sanh giam dan
    qsort(a, n, sizeof(a[0]), cmpGiam);
    inMang("Ham so sanh giam dan : ", a, n);

    // Cach 2: sap tang dan roi dao nguoc mang
    qsort(b, n, sizeof(b[0]), cmpTang);
    daoNguoc(b, n);
    inMang("Sap tang + dao nguoc : ", b, n);
    return 0;
}
```

Output:

```
Ham so sanh giam dan : 9 7 5 3 2 1 
Sap tang + dao nguoc : 9 7 5 3 2 1 
```

💡 **Cách 1 gọn và nhanh hơn** — chỉ một lần sắp xếp. Mẹo `cmpTang(b, a)` giúp viết hàm giảm dần chỉ trong một dòng, không lặp lại logic.

### Bài 3.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main(void) {
    int a[] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    int n = 10, l, r;

    printf("Nhap l r (0 <= l <= r < %d): ", n);
    if (scanf("%d %d", &l, &r) != 2 || l < 0 || r >= n || l > r) {
        printf("Doan khong hop le!\n");
        return 1;
    }

    // Dia chi bat dau: a + l ; so phan tu: r - l + 1
    qsort(a + l, r - l + 1, sizeof(a[0]), cmpTang);

    printf("Ket qua: ");
    for (int i = 0; i < n; i++) {
        if (i == l) printf("| ");
        printf("%d ", a[i]);
        if (i == r) printf("| ");
    }
    printf("\n");
    return 0;
}
```

Ví dụ chạy:

```
Nhap l r (0 <= l <= r < 10): 2 7
Ket qua: 9 8 | 2 3 4 5 6 7 | 1 0 
```

⚠️ Tham số thứ hai là **số phần tử** của đoạn (`r - l + 1`), không phải chỉ số cuối. Viết nhầm `qsort(a + l, r, ...)` sẽ sắp lố ra ngoài đoạn, thậm chí vượt ra ngoài mảng.

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpDouble(const void *a, const void *b) {
    double x = *(const double *)a;
    double y = *(const double *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main(void) {
    double a[] = {3.14, -1.5, 2.718, 0.5, 1.414, -0.25};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), cmpDouble);

    printf("Mang double tang dan: ");
    for (int i = 0; i < n; i++) printf("%.2f ", a[i]);
    printf("\n");
    return 0;
}
```

Output:

```
Mang double tang dan: -1.50 -0.25 0.50 1.41 2.72 3.14 
```

⚠️ **Không viết `return x - y;` cho số thực.** Hiệu `0.5 - 0.25 = 0.25` khi đổi sang `int` thành `0` → `qsort` tưởng hai số bằng nhau → mảng sắp sai.

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmpChar(const void *a, const void *b) {
    char x = *(const char *)a;
    char y = *(const char *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main(void) {
    char s[101];
    printf("Nhap chuoi (khong dau cach): ");
    if (scanf("%100s", s) != 1) return 1;

    qsort(s, strlen(s), sizeof(s[0]), cmpChar);   // KHONG sap ky tu '\0'

    printf("Sau khi sap xep: %s\n", s);
    return 0;
}
```

Ví dụ chạy:

```
Nhap chuoi (khong dau cach): codelab
Sau khi sap xep: abcdelo
```

⚠️ Nếu dùng `sizeof(s)` (= 101) làm số phần tử, `qsort` sẽ sắp luôn cả `'\0'` và các byte rác phía sau. Vì `'\0'` có mã 0 nhỏ nhất, nó bị đưa lên **đầu** → chuỗi in ra rỗng.

💡 Sắp theo mã ASCII nên chữ số `'0'..'9'` < chữ hoa `'A'..'Z'` < chữ thường `'a'..'z'`.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpLL(const void *a, const void *b) {
    long long x = *(const long long *)a;
    long long y = *(const long long *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

int main(void) {
    long long a[] = {1000000000000000000LL, -5, 123456789012LL,
                     -900000000000000000LL, 0, 42};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), cmpLL);

    for (int i = 0; i < n; i++) printf("%lld\n", a[i]);
    return 0;
}
```

Output:

```
-900000000000000000
-5
0
42
123456789012
1000000000000000000
```

⚠️ **Hai lỗi hay gặp:**
- Ép kiểu về `int *` thay vì `long long *` → chỉ đọc 4 byte đầu của mỗi số → sắp sai.
- Viết `return x - y;` → hiệu kiểu `long long` bị cắt khi trả về `int`, dấu kết quả có thể bị đổi.

### Bài 7.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int cmpChar(const void *a, const void *b) {
    char x = *(const char *)a, y = *(const char *)b;
    return (x > y) - (x < y);       // -1, 0 hoac 1 ma khong tran so
}

bool laAnagram(const char *s1, const char *s2) {
    char a[101], b[101];
    size_t n = strlen(s1);
    if (n != strlen(s2) || n > 100) return false;

    strcpy(a, s1);                  // sap tren ban sao, giu nguyen chuoi goc
    strcpy(b, s2);
    qsort(a, n, 1, cmpChar);
    qsort(b, n, 1, cmpChar);
    return strcmp(a, b) == 0;
}

int main(void) {
    const char *cap[][2] = {{"listen", "silent"}, {"triangle", "integral"},
                            {"apple", "paple"}, {"hello", "world"}};

    for (int i = 0; i < 4; i++)
        printf("%-8s - %-8s : %s\n", cap[i][0], cap[i][1],
               laAnagram(cap[i][0], cap[i][1]) ? "ANAGRAM" : "khong");
    return 0;
}
```

Output:

```
listen   - silent   : ANAGRAM
triangle - integral : ANAGRAM
apple    - paple    : ANAGRAM
hello    - world    : khong
```

💡 Biểu thức `(x > y) - (x < y)` cho đúng `-1`, `0`, `1` — cách viết một dòng, an toàn, dùng được cho mọi kiểu so sánh được bằng `<`, `>`.

💡 Độ phức tạp **O(n log n)**. Nếu chỉ có chữ thường, cách đếm tần suất bằng mảng `dem[26]` còn nhanh hơn (O(n)).

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpGiam(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x < y) - (x > y);        // lon hon thi dung truoc
}

int main(void) {
    int a[] = {7, 3, 9, 9, 1, 5, 7, 2};
    int n = sizeof(a) / sizeof(a[0]);
    int k;

    printf("Nhap k: ");
    if (scanf("%d", &k) != 1 || k < 1 || k > n) {
        printf("k khong hop le\n");
        return 1;
    }

    qsort(a, n, sizeof(a[0]), cmpGiam);

    printf("Mang giam dan: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\nPhan tu lon thu %d (tinh ca trung lap): %d\n", k, a[k - 1]);

    // Lon thu k trong cac gia tri PHAN BIET
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || a[i] != a[i - 1]) dem++;
        if (dem == k) { printf("Gia tri phan biet lon thu %d: %d\n", k, a[i]); break; }
    }
    if (dem < k) printf("Khong co du %d gia tri phan biet\n", k);
    return 0;
}
```

Ví dụ chạy:

```
Nhap k: 2
Mang giam dan: 9 9 7 7 5 3 2 1 
Phan tu lon thu 2 (tinh ca trung lap): 9
Gia tri phan biet lon thu 2: 7
```

💡 Đề bài có trùng lặp thì phải hỏi rõ: "lớn thứ k" tính cả phần tử trùng hay chỉ tính **giá trị khác nhau** — hai cách cho kết quả khác nhau.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

// Loai phan tu trung trong mang DA SAP XEP, tra ve so phan tu con lai
int loaiTrung(int a[], int n) {
    if (n == 0) return 0;
    int m = 1;                          // a[0] luon duoc giu
    for (int i = 1; i < n; i++)
        if (a[i] != a[m - 1]) a[m++] = a[i];
    return m;
}

int main(void) {
    int a[] = {4, 1, 3, 3, 1, 4, 4, 2, 5, 1};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), cmpTang);
    int m = loaiTrung(a, n);

    printf("Cac gia tri phan biet (%d gia tri): ", m);
    for (int i = 0; i < m; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Output:

```
Cac gia tri phan biet (5 gia tri): 1 2 3 4 5 
```

💡 Kỹ thuật **hai con trỏ** trên mảng đã sắp xếp: `i` đọc, `m` ghi. Làm **tại chỗ**, O(n), không cần mảng phụ.

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpDouble(const void *a, const void *b) {
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

double trungVi(double a[], int n) {
    qsort(a, n, sizeof(a[0]), cmpDouble);
    if (n % 2 == 1) return a[n / 2];
    return (a[n / 2 - 1] + a[n / 2]) / 2.0;
}

int main(void) {
    double le[]  = {7.5, 1.0, 3.2, 9.8, 4.4};            // n = 5
    double chan[] = {6.0, 2.5, 8.0, 1.5, 4.0, 9.5};      // n = 6

    printf("Trung vi (n le)  : %.2f\n", trungVi(le, 5));
    printf("Trung vi (n chan): %.2f\n", trungVi(chan, 6));
    return 0;
}
```

Output:

```
Trung vi (n le)  : 4.40
Trung vi (n chan): 5.00
```

💡 Với `n` chẵn: mảng sắp xếp `1.5 2.5 4.0 6.0 8.0 9.5`, hai phần tử giữa là `4.0` và `6.0` → trung vị `5.00`.

⚠️ Hàm `trungVi` **làm thay đổi** mảng gốc (vì đã sắp xếp nó). Nếu cần giữ mảng gốc, hãy sao chép ra mảng phụ trước.

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

int cmpGiam(const void *a, const void *b) {
    return cmpTang(b, a);
}

int main(void) {
    int a[] = {8, 3, 5, 1, 9, 2, 7, 4, 6, 0};
    int n = sizeof(a) / sizeof(a[0]);
    int nua = n / 2;

    qsort(a, nua, sizeof(a[0]), cmpTang);             // a[0 .. nua-1]
    qsort(a + nua, n - nua, sizeof(a[0]), cmpGiam);   // a[nua .. n-1]

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Output:

```
1 3 5 8 9 7 6 4 2 0 
```

💡 Với `n` lẻ, nửa sau có nhiều hơn một phần tử — viết `n - nua` thay vì `nua` để không bỏ sót phần tử cuối.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

bool cungPhanTu(const int a[], const int b[], int n, int m) {
    if (n != m) return false;
    int *x = malloc(n * sizeof(int));
    int *y = malloc(n * sizeof(int));
    if (x == NULL || y == NULL) { free(x); free(y); return false; }

    memcpy(x, a, n * sizeof(int));      // sap tren ban sao
    memcpy(y, b, n * sizeof(int));
    qsort(x, n, sizeof(int), cmpTang);
    qsort(y, n, sizeof(int), cmpTang);

    bool kq = memcmp(x, y, n * sizeof(int)) == 0;
    free(x);
    free(y);
    return kq;
}

int main(void) {
    int a[] = {3, 1, 2, 2, 5};
    int b[] = {2, 5, 3, 1, 2};
    int c[] = {2, 5, 3, 1, 1};

    printf("a va b: %s\n", cungPhanTu(a, b, 5, 5) ? "GIONG" : "KHAC");
    printf("a va c: %s\n", cungPhanTu(a, c, 5, 5) ? "GIONG" : "KHAC");
    return 0;
}
```

Output:

```
a va b: GIONG
a va c: KHAC
```

💡 Sau khi sắp xếp, hai mảng có cùng các phần tử (kể cả số lần lặp) sẽ **giống hệt nhau** từng vị trí → so sánh một lần bằng `memcmp`.

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int cmpTang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}

void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int doiCho = 0;
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
                doiCho = 1;
            }
        if (!doiCho) break;
    }
}

int main(void) {
    const int N = 100000;
    int *goc = malloc(N * sizeof(int));
    int *a = malloc(N * sizeof(int));
    int *b = malloc(N * sizeof(int));
    if (!goc || !a || !b) return 1;

    for (int i = 0; i < N; i++) goc[i] = (int)((i * 7919LL + 13) % N);
    memcpy(a, goc, N * sizeof(int));
    memcpy(b, goc, N * sizeof(int));

    clock_t t1 = clock();
    qsort(a, N, sizeof(int), cmpTang);
    clock_t t2 = clock();
    double tQsort = (double)(t2 - t1) * 1000.0 / CLOCKS_PER_SEC;

    t1 = clock();
    bubbleSort(b, N);
    t2 = clock();
    double tBubble = (double)(t2 - t1) * 1000.0 / CLOCKS_PER_SEC;

    printf("Mang %d phan tu:\n", N);
    printf("  qsort       : %.1f ms\n", tQsort);
    printf("  Bubble Sort : %.1f ms\n", tBubble);
    if (tQsort > 0) printf("  Nhanh hon   : %.0f lan\n", tBubble / tQsort);
    printf("\nKet qua giong nhau: %s\n",
           memcmp(a, b, N * sizeof(int)) == 0 ? "OK" : "SAI");

    free(goc); free(a); free(b);
    return 0;
}
```

Kết quả tham khảo (biên dịch `-O2`, tuỳ máy):

```
Mang 100000 phan tu:
  qsort       : 4.5 ms
  Bubble Sort : 4335.2 ms
  Nhanh hon   : 956 lan

Ket qua giong nhau: OK
```

**Chênh lệch khổng lồ** — đúng như lý thuyết dự đoán:

| n | O(n²) — Bubble | O(n log n) — qsort | Tỉ lệ |
|---|---|---|---|
| 1.000 | 10⁶ | ~10⁴ | 100× |
| 100.000 | 10¹⁰ | ~1,7×10⁶ | ~6.000× |
| 1.000.000 | 10¹² | ~2×10⁷ | ~50.000× |

💡 `qsort` phải gọi hàm so sánh qua **con trỏ hàm** ở mỗi lần so sánh nên chậm hơn một chút so với hàm sắp xếp viết riêng cho `int`, nhưng vẫn nhanh hơn Bubble Sort hàng nghìn lần.

✅ **Luôn dùng `qsort`** (hoặc thuật toán O(n log n)) — chỉ học Bubble/Selection/Insertion để hiểu nguyên lý.

### Bài 14.

```c
double a[] = {3.5, 1.2, 2.8, 0.9};
int cmp(const void *x, const void *y){ return *(int *)x - *(int *)y; }   // SAI
qsort(a, 4, sizeof(int), cmp);                                             // SAI
```

**Có 3 lỗi:**

| # | Lỗi | Hậu quả |
|---|---|---|
| 1 | `sizeof(int)` (4 byte) thay vì `sizeof(double)` (8 byte) | `qsort` tưởng mảng có 4 phần tử **4 byte** → chỉ xáo trộn 16 byte đầu, cắt đôi các số `double` → dữ liệu hỏng |
| 2 | Ép về `int *` trong khi phần tử là `double` | Đọc 4 byte của số thực như số nguyên → giá trị vô nghĩa |
| 3 | `return x - y` | Với `double`, hiệu bị cắt phần thập phân; với `int` có thể **tràn số** |

**Sửa:**

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *x, const void *y) {
    double a = *(const double *)x;
    double b = *(const double *)y;
    if (a < b) return -1;
    if (a > b) return 1;
    return 0;
}

int main(void) {
    double a[] = {3.5, 1.2, 2.8, 0.9};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), cmp);

    for (int i = 0; i < n; i++) printf("%.1f ", a[i]);   // 0.9 1.2 2.8 3.5
    printf("\n");
    return 0;
}
```

💡 **Quy tắc vàng:** kiểu trong `sizeof(...)`, kiểu ép trong hàm so sánh và kiểu của mảng phải **cùng một kiểu**. Dùng `sizeof(a[0])` và `sizeof(a) / sizeof(a[0])` để trình biên dịch tự tính giúp.

⚠️ `qsort` nhận `void *` nên trình biên dịch **không phát hiện** được các lỗi này — chương trình vẫn biên dịch thành công, chỉ chạy ra kết quả sai.

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX 100

int cmpTang(const void *a, const void *b) {
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

int cmpGiam(const void *a, const void *b) {
    return cmpTang(b, a);
}

void hienThi(const double d[], int n, const char *tieuDe) {
    printf("\n=== %s ===\n", tieuDe);
    for (int i = 0; i < n; i++) printf("%6.2f", d[i]);
    printf("\n");
}

double trungVi(const double d[], int n) {
    double tam[MAX];
    for (int i = 0; i < n; i++) tam[i] = d[i];      // khong lam doi mang goc
    qsort(tam, n, sizeof(tam[0]), cmpTang);
    return n % 2 ? tam[n / 2] : (tam[n / 2 - 1] + tam[n / 2]) / 2.0;
}

int main(void) {
    double diem[MAX];
    int n;

    printf("Nhap so luong diem (1-%d): ", MAX);
    if (scanf("%d", &n) != 1 || n < 1 || n > MAX) {
        printf("So luong khong hop le!\n");
        return 1;
    }
    for (int i = 0; i < n; i++) {
        printf("Diem thu %d: ", i + 1);
        while (scanf("%lf", &diem[i]) != 1) {           // %lf khi scanf double
            int c;
            while ((c = getchar()) != '\n' && c != EOF) {}   // bo dong nhap sai
            printf("Nhap lai diem thu %d: ", i + 1);
        }
    }

    hienThi(diem, n, "DANH SACH BAN DAU");

    int chon;
    do {
        printf("\n====== MENU ======\n");
        printf("1. Sap xep tang dan\n");
        printf("2. Sap xep giam dan\n");
        printf("3. Diem cao nhat, thap nhat, trung vi\n");
        printf("0. Thoat\n");
        printf("Lua chon: ");

        if (scanf("%d", &chon) != 1) {
            int c;
            while ((c = getchar()) != '\n' && c != EOF) {}
            if (c == EOF) break;
            printf("Nhap khong hop le!\n");
            chon = -1;
            continue;
        }

        switch (chon) {
            case 1:
                qsort(diem, n, sizeof(diem[0]), cmpTang);
                hienThi(diem, n, "TANG DAN");
                break;
            case 2:
                qsort(diem, n, sizeof(diem[0]), cmpGiam);
                hienThi(diem, n, "GIAM DAN");
                break;
            case 3: {
                double lon = diem[0], nho = diem[0];
                for (int i = 1; i < n; i++) {
                    if (diem[i] > lon) lon = diem[i];
                    if (diem[i] < nho) nho = diem[i];
                }
                printf("Cao nhat: %.2f | Thap nhat: %.2f | Trung vi: %.2f\n",
                       lon, nho, trungVi(diem, n));
                break;
            }
            case 0:
                printf("Tam biet!\n");
                break;
            default:
                printf("Lua chon khong hop le!\n");
        }
    } while (chon != 0);

    return 0;
}
```

Ví dụ chạy:

```
Nhap so luong diem (1-100): 5
Diem thu 1: 7.5
Diem thu 2: 9
Diem thu 3: 6.25
Diem thu 4: 8
Diem thu 5: 5.5

=== DANH SACH BAN DAU ===
  7.50  9.00  6.25  8.00  5.50
...
Lua chon: 2

=== GIAM DAN ===
  9.00  8.00  7.50  6.25  5.50
...
Lua chon: 3
Cao nhat: 9.00 | Thap nhat: 5.50 | Trung vi: 7.50
```

💡 **Điểm thiết kế đáng học:**
1. **Hai hàm so sánh dùng chung logic** — `cmpGiam` chỉ gọi lại `cmpTang(b, a)`
2. **`trungVi` sắp trên bản sao** — không làm xáo trộn thứ tự mà người dùng đang xem
3. **`scanf("%lf", ...)`** cho `double` (còn `printf` dùng `%f` hay `%.2f`)
4. **Xử lý lỗi nhập** — kiểm tra giá trị trả về của `scanf`, đọc bỏ phần còn lại của dòng bằng `getchar()`
