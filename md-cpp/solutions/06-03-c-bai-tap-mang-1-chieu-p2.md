# Lời giải — [C]. Bài Tập Mảng 1 Chiều P2

[← Quay lại bài học](../06-03-c-bai-tap-mang-1-chieu-p2.md)

---

### Bài 1.

```c
#include <stdio.h>
#include <stdbool.h>

void inMang(int a[], int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

void hoanDoi(int *x, int *y) {
    int t = *x; *x = *y; *y = t;
}

int main(void) {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    printf("Ban dau : "); inMang(a, n);

    for (int i = 0; i < n - 1; i++) {
        bool coDoiCho = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                hoanDoi(&a[j], &a[j + 1]);
                coDoiCho = true;
            }
        }
        printf("Luot %d : ", i + 1); inMang(a, n);

        if (!coDoiCho) {              // TOI UU: khong doi cho nao -> da sap xep xong
            printf("(Da sap xep xong, dung som)\n");
            break;
        }
    }
    return 0;
}
```

Output:

```
Ban dau : 5 2 9 1 7 
Luot 1 : 2 5 1 7 9 
Luot 2 : 2 1 5 7 9 
Luot 3 : 1 2 5 7 9 
Luot 4 : 1 2 5 7 9 
(Da sap xep xong, dung som)
```

**Bubble Sort — nguyên lý:** so sánh từng cặp kề nhau, đổi chỗ nếu sai thứ tự. Sau mỗi lượt, phần tử lớn nhất "nổi" về cuối.

**Tối ưu bằng cờ `coDoiCho`:** nếu một lượt không có phép đổi chỗ nào thì mảng đã sắp xếp xong. Nhờ đó, với mảng đã sắp sẵn, độ phức tạp là **O(n)** thay vì O(n²).

💡 C không có hàm `swap` có sẵn, ta tự viết `hoanDoi` nhận **con trỏ** tới 2 phần tử cần đổi.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    for (int i = 0; i < n - 1; i++) {
        int viTriMin = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[viTriMin]) viTriMin = j;
        }
        if (viTriMin != i) {
            int t = a[i]; a[i] = a[viTriMin]; a[viTriMin] = t;
        }

        printf("Buoc %d: ", i + 1);
        for (int k = 0; k < n; k++) printf("%d ", a[k]);
        printf("\n");
    }
    return 0;
}
```

**Selection Sort — nguyên lý:** ở bước thứ `i`, tìm phần tử **nhỏ nhất** trong phần chưa sắp xếp và đưa nó về vị trí `i`.

💡 **Ưu điểm lớn nhất:** số phép **đổi chỗ** chỉ tối đa `n−1` — ít nhất trong các thuật toán O(n²). Hữu ích khi việc đổi chỗ tốn kém (ví dụ phần tử là struct lớn).

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    for (int i = 1; i < n; i++) {
        int khoa = a[i];
        int j = i - 1;

        // Day cac phan tu lon hon khoa sang phai
        while (j >= 0 && a[j] > khoa) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = khoa;              // chen khoa vao dung cho

        printf("Buoc %d: ", i);
        for (int k = 0; k < n; k++) printf("%d ", a[k]);
        printf("\n");
    }
    return 0;
}
```

**Insertion Sort — nguyên lý:** giống cách bạn xếp bài trên tay. Lấy từng phần tử và **chèn** nó vào đúng vị trí trong phần đã sắp xếp phía trước.

💡 **Ưu điểm:** với mảng **gần như đã sắp xếp**, độ phức tạp chỉ **O(n)** — nhanh nhất trong 3 thuật toán. Đây là lý do nhiều thư viện sắp xếp thực tế dùng Insertion Sort cho các đoạn nhỏ.

### Bài 4.

```c
#include <stdio.h>
#include <string.h>

#define N 10
int goc[N] = {5, 2, 9, 1, 7, 3, 8, 6, 4, 0};

void hoanDoi(int *x, int *y) { int t = *x; *x = *y; *y = t; }

// C khong co tham chieu: dung con tro de tra ve 2 bo dem
void bubbleSort(int a[], int n, long long *soSanh, long long *doiCho) {
    *soSanh = *doiCho = 0;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++) {
            (*soSanh)++;
            if (a[j] > a[j + 1]) { hoanDoi(&a[j], &a[j + 1]); (*doiCho)++; }
        }
}

void selectionSort(int a[], int n, long long *soSanh, long long *doiCho) {
    *soSanh = *doiCho = 0;
    for (int i = 0; i < n - 1; i++) {
        int vtMin = i;
        for (int j = i + 1; j < n; j++) {
            (*soSanh)++;
            if (a[j] < a[vtMin]) vtMin = j;
        }
        if (vtMin != i) { hoanDoi(&a[i], &a[vtMin]); (*doiCho)++; }
    }
}

void insertionSort(int a[], int n, long long *soSanh, long long *doiCho) {
    *soSanh = *doiCho = 0;
    for (int i = 1; i < n; i++) {
        int khoa = a[i], j = i - 1;
        while (j >= 0) {
            (*soSanh)++;
            if (a[j] <= khoa) break;
            a[j + 1] = a[j];
            (*doiCho)++;
            j--;
        }
        a[j + 1] = khoa;
    }
}

int main(void) {
    int a[N];
    long long ss, dc;

    memcpy(a, goc, sizeof(goc));
    bubbleSort(a, N, &ss, &dc);
    printf("Bubble Sort    : %lld so sanh, %lld doi cho\n", ss, dc);

    memcpy(a, goc, sizeof(goc));
    selectionSort(a, N, &ss, &dc);
    printf("Selection Sort : %lld so sanh, %lld doi cho\n", ss, dc);

    memcpy(a, goc, sizeof(goc));
    insertionSort(a, N, &ss, &dc);
    printf("Insertion Sort : %lld so sanh, %lld phep dich\n", ss, dc);
    return 0;
}
```

Output (n = 10, mảng `goc` ở trên):

```
Bubble Sort    : 45 so sanh, 26 doi cho
Selection Sort : 45 so sanh, 8 doi cho
Insertion Sort : 32 so sanh, 26 phep dich
```

**Bảng tổng hợp:**

| Thuật toán | Tốt nhất | Trung bình | Xấu nhất | Đổi chỗ | Ổn định? |
|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | Nhiều | ✅ Có |
| Selection | O(n²) | O(n²) | O(n²) | **Ít nhất** (n−1) | ❌ Không |
| Insertion | **O(n)** | O(n²) | O(n²) | Nhiều | ✅ Có |
| `qsort` (`<stdlib.h>`) | O(n log n)* | O(n log n)* | O(n log n)* | — | ❌ Không đảm bảo |

\* Chuẩn C không quy định thuật toán bên trong `qsort`, nhưng các thư viện phổ biến đều đạt O(n log n).

✅ Trong thực tế **nên dùng `qsort`** của thư viện chuẩn. Học 3 thuật toán trên để hiểu nguyên lý và rèn tư duy.

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int b[1000], m = 0;

    for (int i = 0; i < n; i++) {
        bool daCo = false;
        for (int j = 0; j < m; j++) {
            if (b[j] == a[i]) { daCo = true; break; }
        }
        if (!daCo) b[m++] = a[i];
    }

    printf("Sau khi loai trung lap (%d phan tu): ", m);
    for (int i = 0; i < m; i++) printf("%d ", b[i]);
    printf("\n");
    return 0;
}
```

Ví dụ `{1, 3, 1, 5, 3, 7}` → `1 3 5 7`

💡 Cách nhanh hơn khi các giá trị là số nguyên không âm và không quá lớn — dùng **mảng đánh dấu**, **O(n)** thay vì O(n²):

```c
static bool daGap[1000001];      // gia tri a[i] trong [0, 10^6]
int m = 0;
for (int i = 0; i < n; i++) {
    if (!daGap[a[i]]) {
        daGap[a[i]] = true;
        b[m++] = a[i];
    }
}
```

Mảng khai báo `static` (hoặc toàn cục) được tự khởi tạo toàn `false` và không chiếm stack.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int kq = 0;
    for (int i = 0; i < n; i++) kq ^= a[i];

    printf("Phan tu xuat hien 1 lan: %d\n", kq);
    return 0;
}
```

Ví dụ `{4, 1, 2, 1, 2}` → `4`

**Nguyên lý XOR:**

| Tính chất | Ý nghĩa |
|---|---|
| `x ^ x = 0` | Hai số giống nhau triệt tiêu |
| `x ^ 0 = x` | XOR với 0 giữ nguyên |
| `a ^ b = b ^ a` | Giao hoán — thứ tự không quan trọng |

Nên khi XOR tất cả phần tử: mọi cặp trùng nhau triệt tiêu về 0, chỉ còn lại phần tử đơn lẻ.

```
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1^1) ^ (2^2)
= 4 ^ 0 ^ 0
= 4  ✔
```

💡 **O(n) thời gian, O(1) bộ nhớ** — tốt hơn hẳn dùng mảng đếm số lần xuất hiện (tốn bộ nhớ theo miền giá trị).

### Bài 7.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1001];
    for (int i = 1; i <= n; i++) scanf("%d", &a[i]);       // danh so tu 1 cho tien

    // Xay mang tong tien to: pre[i] = a[1] + a[2] + ... + a[i]
    long long pre[1001];
    pre[0] = 0;
    for (int i = 1; i <= n; i++) pre[i] = pre[i - 1] + a[i];

    int q;
    printf("So truy van: ");
    scanf("%d", &q);

    while (q--) {
        int l, r;
        printf("Nhap l r: ");
        scanf("%d %d", &l, &r);
        // Tong tu l den r = pre[r] - pre[l-1]  -> O(1)
        printf("  Tong tu %d den %d = %lld\n", l, r, pre[r] - pre[l - 1]);
    }
    return 0;
}
```

**Kỹ thuật tổng tiền tố (prefix sum):**

```
a   :      3   1   4   1   5   9
pre : 0    3   4   8   9  14  23
       0   1   2   3   4   5   6

Tong tu 2 den 4 = pre[4] - pre[1] = 9 - 3 = 6   (= 1 + 4 + 1) ✔
```

**Hiệu quả:**

| | Tính trực tiếp | Prefix sum |
|---|---|---|
| Tiền xử lý | 0 | O(n), một lần |
| Mỗi truy vấn | O(n) | **O(1)** |
| 10⁵ truy vấn trên mảng 10⁵ | 10¹⁰ bước (quá chậm) | 2×10⁵ bước |

💡 **Mẹo đánh chỉ số từ 1** giúp công thức `pre[r] - pre[l-1]` hoạt động mà không cần xét trường hợp đặc biệt `l = 0`.

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    long long S;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Nhap S: ");
    scanf("%lld", &S);

    // Ky thuat CUA SO TRUOT - chi dung cho mang toan so DUONG
    int trai = 0;
    long long tong = 0;
    bool timThay = false;

    for (int phai = 0; phai < n; phai++) {
        tong += a[phai];

        while (tong > S && trai <= phai) {
            tong -= a[trai];
            trai++;
        }

        if (tong == S) {
            printf("Tim thay day con tu vi tri %d den %d: ", trai, phai);
            for (int i = trai; i <= phai; i++) printf("%d ", a[i]);
            printf("\n");
            timThay = true;
            break;
        }
    }

    if (!timThay) printf("Khong tim thay\n");
    return 0;
}
```

Ví dụ `{1, 4, 20, 3, 10, 5}` với `S = 33` → dãy `20 3 10` (vị trí 2–4).

**Kỹ thuật cửa sổ trượt (sliding window):** mở rộng cửa sổ bên phải khi tổng còn nhỏ, thu hẹp bên trái khi tổng quá lớn. Độ phức tạp **O(n)**.

⚠️ **Chỉ đúng với mảng toàn số dương.** Nếu có số âm, cách đơn giản trong C là dùng prefix sum và xét mọi cặp `(l, r)` — **O(n²)**:

```c
long long pre[1001];
pre[0] = 0;
for (int i = 0; i < n; i++) pre[i + 1] = pre[i] + a[i];
for (int l = 0; l < n; l++)
    for (int r = l; r < n; r++)
        if (pre[r + 1] - pre[l] == S) { /* tim thay tu l den r */ }
```

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>

// Ham so sanh cho qsort: sap xep GIAM dan
int soSanhGiam(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    return (x < y) - (x > y);
}

int main(void) {
    int n, k;
    scanf("%d", &n);
    int a[1000], b[1000], c[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Nhap k: ");
    scanf("%d", &k);

    if (k > n) k = n;

    // Cach 1: sap xep giam dan roi lay k dau - O(n log n)
    for (int i = 0; i < n; i++) b[i] = a[i];
    qsort(b, n, sizeof(int), soSanhGiam);
    printf("%d phan tu lon nhat: ", k);
    for (int i = 0; i < k; i++) printf("%d ", b[i]);
    printf("\n");

    // Cach 2: chon k lan (giong Selection Sort dung som) - O(n * k)
    for (int i = 0; i < n; i++) c[i] = a[i];
    for (int i = 0; i < k; i++) {
        int vtMax = i;
        for (int j = i + 1; j < n; j++)
            if (c[j] > c[vtMax]) vtMax = j;
        int t = c[i]; c[i] = c[vtMax]; c[vtMax] = t;
    }
    printf("Cach 2 (chon k lan): ");
    for (int i = 0; i < k; i++) printf("%d ", c[i]);
    printf("\n");

    return 0;
}
```

💡 **`qsort`** nhận: địa chỉ mảng, số phần tử, kích thước mỗi phần tử, và **hàm so sánh**. Hàm so sánh trả về số âm / 0 / dương. Biểu thức `(x < y) - (x > y)` tránh tràn số so với cách viết `y - x`.

Cách 2 chỉ "sắp xếp một phần": dừng sau `k` bước chọn. Nhanh hơn `qsort` khi `k` rất nhỏ so với `n`.

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>

int soSanhTang(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    return (x > y) - (x < y);
}

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    qsort(a, n, sizeof(int), soSanhTang);

    printf("Mang sau sap xep: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    if (n % 2 == 1) {
        printf("Trung vi = %d\n", a[n / 2]);                        // le: phan tu giua
    } else {
        printf("Trung vi = %.2f\n", (a[n/2 - 1] + a[n/2]) / 2.0);   // chan: TB 2 phan tu giua
    }
    return 0;
}
```

Ví dụ:
- `{1, 3, 5, 7, 9}` (n lẻ) → trung vị = **5**
- `{1, 3, 5, 7}` (n chẵn) → trung vị = (3+5)/2 = **4.00**

💡 **Trung vị vs Trung bình:** trung vị **không bị ảnh hưởng** bởi các giá trị ngoại lai. Với `{1, 2, 3, 4, 1000}`, trung bình là 202 (không đại diện được cho dữ liệu) nhưng trung vị là 3 (hợp lý hơn). Đây là lý do thống kê thu nhập thường dùng trung vị.

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = sizeof(a) / sizeof(a[0]);

    srand((unsigned)time(NULL));     // khoi tao bo sinh so ngau nhien

    // Thuat toan Fisher-Yates
    for (int i = n - 1; i > 0; i--) {
        int j = rand() % (i + 1);    // j ngau nhien trong [0, i]
        int t = a[i]; a[i] = a[j]; a[j] = t;
    }

    printf("Sau khi tron: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

**Thuật toán Fisher-Yates:** duyệt từ cuối về đầu, mỗi bước đổi chỗ phần tử `i` với một phần tử ngẫu nhiên trong khoảng `[0, i]`.

**Đây là cách trộn chuẩn** — nếu nguồn ngẫu nhiên đều, mọi hoán vị đều có xác suất bằng nhau (1/n!).

⚠️ **Cách trộn SAI thường gặp:**

```c
for (int i = 0; i < n; i++) {
    int j = rand() % n;                          // KHONG deu!
    int t = a[i]; a[i] = a[j]; a[j] = t;
}
```

Cách này tạo ra nⁿ khả năng, không chia hết cho n! nên một số hoán vị xuất hiện nhiều hơn.

💡 `rand()` của thư viện chuẩn C có chất lượng ngẫu nhiên hạn chế và `rand() % m` hơi lệch khi `m` lớn — đủ dùng cho bài tập, nhưng không dùng cho mật mã hay mô phỏng nghiêm túc.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);                 // n <= 20
    int a[20];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tongAll = 0;
    for (int i = 0; i < n; i++) tongAll += a[i];

    long long hieuMin = llabs(tongAll);   // khoi tao bang truong hop xau nhat
    int maskTot = 0;

    // Vet can 2^n cach chia (chi dung voi n <= 20)
    for (int mask = 0; mask < (1 << n); mask++) {
        long long tong1 = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) tong1 += a[i];
        }
        long long tong2 = tongAll - tong1;
        long long hieu = llabs(tong1 - tong2);

        if (hieu < hieuMin) { hieuMin = hieu; maskTot = mask; }
    }

    printf("Nhom 1: ");
    long long t1 = 0;
    for (int i = 0; i < n; i++) if (maskTot & (1 << i))  { printf("%d ", a[i]); t1 += a[i]; }
    printf("(tong = %lld)\n", t1);

    printf("Nhom 2: ");
    for (int i = 0; i < n; i++) if (!(maskTot & (1 << i))) printf("%d ", a[i]);
    printf("(tong = %lld)\n", tongAll - t1);
    printf("Chenh lech = %lld\n", hieuMin);
    return 0;
}
```

**Kỹ thuật duyệt tập con bằng bitmask:** mỗi số `mask` từ 0 đến 2ⁿ−1 đại diện cho một cách chọn. Bit thứ `i` bằng 1 nghĩa là phần tử `i` thuộc nhóm 1.

```
n = 3, mask = 5 = binary 101
-> chon phan tu 0 va 2
```

⚠️ Độ phức tạp **O(2ⁿ × n)** — chỉ dùng được với `n ≤ 20`. Với `n` lớn, đây là bài toán NP-khó, phải dùng quy hoạch động (bài toán **Partition Problem**).

💡 `llabs` (trị tuyệt đối cho `long long`) nằm trong `<stdlib.h>`.

### Bài 13.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long dem = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] > a[j]) dem++;
        }
    }

    printf("So cap nghich the = %lld\n", dem);

    // So cap nghich the toi da (mang sap xep nguoc hoan toan)
    printf("Toi da co the co  = %lld\n", (long long)n * (n - 1) / 2);
    return 0;
}
```

Ví dụ `{2, 4, 1, 3, 5}` → 3 cặp nghịch thế: `(2,1)`, `(4,1)`, `(4,3)`

💡 **Ý nghĩa:** số cặp nghịch thế đo mức độ "lộn xộn" của mảng.
- Mảng đã sắp xếp → 0 cặp
- Mảng sắp ngược hoàn toàn → `n(n−1)/2` cặp (tối đa)
- Đây cũng chính là **số phép đổi chỗ** mà Bubble Sort cần thực hiện

⚠️ Cách trên là O(n²). Có thể giảm xuống **O(n log n)** bằng cách cải tiến Merge Sort hoặc dùng Binary Indexed Tree.

### Bài 14.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    if (n == 0) return 0;

    printf("Ma hoa RLE: ");
    int i = 0;
    while (i < n) {
        int giaTri = a[i];
        int dem = 0;
        while (i < n && a[i] == giaTri) { dem++; i++; }

        printf("%dx%d", giaTri, dem);
        if (i < n) printf(", ");
    }
    printf("\n");
    return 0;
}
```

Ví dụ `{1,1,1,2,2,3}` → `1x3, 2x2, 3x1`

**Run-Length Encoding (RLE)** là thuật toán nén đơn giản nhất — thay vì lưu từng phần tử, ta lưu "giá trị × số lần lặp".

**Hiệu quả:**
- `{1,1,1,1,1,1,1,1}` → `1x8` — nén rất tốt
- `{1,2,3,4,5,6,7,8}` → `1x1, 2x1, ...` — **phình to hơn** bản gốc

RLE được dùng trong định dạng ảnh BMP, fax, và các dữ liệu có nhiều đoạn lặp lại.

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>

int soSanhTang(const void *p, const void *q) {
    int x = *(const int *)p, y = *(const int *)q;
    return (x > y) - (x < y);
}

// Sap xep roi loai trung, tra ve so phan tu con lai
int chuanHoa(int a[], int n) {
    if (n == 0) return 0;
    qsort(a, n, sizeof(int), soSanhTang);
    int m = 1;
    for (int i = 1; i < n; i++)
        if (a[i] != a[m - 1]) a[m++] = a[i];
    return m;
}

int main(void) {
    int n, m;
    int a[1000], b[1000];
    printf("So phan tu mang A: "); scanf("%d", &n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("So phan tu mang B: "); scanf("%d", &m);
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    n = chuanHoa(a, n);
    m = chuanHoa(b, m);

    // Hai con tro chay song song tren 2 mang da sap xep
    int i, j;

    printf("Giao (A n B): ");
    i = j = 0;
    while (i < n && j < m) {
        if (a[i] < b[j]) i++;
        else if (a[i] > b[j]) j++;
        else { printf("%d ", a[i]); i++; j++; }
    }
    printf("\n");

    printf("Hop (A u B): ");
    i = j = 0;
    while (i < n || j < m) {
        if (j >= m || (i < n && a[i] < b[j])) printf("%d ", a[i++]);
        else if (i >= n || b[j] < a[i])      printf("%d ", b[j++]);
        else { printf("%d ", a[i]); i++; j++; }
    }
    printf("\n");

    printf("Hieu (A \\ B): ");
    i = j = 0;
    while (i < n) {
        if (j >= m || a[i] < b[j]) printf("%d ", a[i++]);
        else if (a[i] > b[j]) j++;
        else { i++; j++; }
    }
    printf("\n");

    return 0;
}
```

Ví dụ `A = {1,2,3,4}`, `B = {3,4,5,6}`:

```
Giao (A n B): 3 4 
Hop (A u B): 1 2 3 4 5 6 
Hieu (A \ B): 1 2 
```

💡 **Kỹ thuật hai con trỏ trên 2 mảng đã sắp xếp** (sau khi `qsort` và loại trùng):

| Phép | Khi `a[i] == b[j]` | Khi khác nhau |
|---|---|---|
| Giao | In ra, tăng cả hai | Tăng bên nhỏ hơn |
| Hợp | In 1 lần, tăng cả hai | In bên nhỏ hơn rồi tăng nó |
| Hiệu A\B | Bỏ qua, tăng cả hai | `a[i]` nhỏ hơn thì in `a[i]`; ngược lại tăng `j` |

Mỗi phép chỉ tốn **O(n + m)** sau khi sắp xếp.
