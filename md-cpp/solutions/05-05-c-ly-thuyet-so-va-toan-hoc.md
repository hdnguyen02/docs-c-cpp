# Lời giải — [C]. Lý Thuyết Số Và Toán Học

[← Quay lại bài học](../05-05-c-ly-thuyet-so-va-toan-hoc.md)

---

### Bài 1.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(long long n) {
    if (n < 2) return false;
    if (n < 4) return true;              // 2, 3
    if (n % 2 == 0) return false;        // loai het so chan

    // Chi can kiem tra cac so LE tu 3 den sqrt(n)
    for (long long i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

int main(void) {
    long long n;
    printf("Nhap n: ");
    scanf("%lld", &n);
    printf("%lld%sso nguyen to\n", n, laNguyenTo(n) ? " LA " : " KHONG phai ");
    return 0;
}
```

**2 tối ưu so với bản cơ bản:**
1. Loại số chẵn trước → chỉ duyệt số lẻ → **nhanh gấp đôi**
2. Điều kiện `i * i <= n` thay vì `i <= sqrt(n)` → tránh gọi hàm `sqrt` mỗi vòng và tránh sai số số thực

**Độ phức tạp: O(√n)**. Với `n = 10¹⁸`, chỉ cần ~5×10⁸ bước — vẫn hơi chậm, khi đó phải dùng thuật toán Miller-Rabin.

💡 Kiểu `bool` cùng hai giá trị `true`/`false` trong C nằm ở thư viện `<stdbool.h>` — thiếu dòng include này thì chương trình không biên dịch được.

### Bài 2.

```c
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

bool laChinhPhuong(long long n) {
    if (n < 0) return false;

    long long can = (long long)sqrtl((long double)n);

    // Kiem tra cac gia tri lan can de chac chan khong bi sai so
    long long batDau = can - 2 > 0 ? can - 2 : 0;
    for (long long k = batDau; k <= can + 2; k++) {
        if (k * k == n) return true;
    }
    return false;
}

int main(void) {
    long long ds[] = {0, 1, 16, 25, 26, 1000000000000LL};
    int soLuong = sizeof(ds) / sizeof(ds[0]);
    for (int i = 0; i < soLuong; i++) {
        printf("%lld -> %s\n", ds[i], laChinhPhuong(ds[i]) ? "chinh phuong" : "khong");
    }
    return 0;
}
```

⚠️ **Vì sao phải kiểm tra các giá trị lân cận:** `sqrt` trả về `double` có sai số. Với `n` lớn (> 10¹⁵), `sqrt(n)` có thể lệch 1–2 đơn vị, khiến kết luận sai. Duyệt vài giá trị quanh đó là cách chắc chắn nhất.

💡 Dùng `sqrtl` (long double) thay `sqrt` cho độ chính xác cao hơn với `long long`. Khi biên dịch bằng gcc nhớ thêm `-lm` để liên kết thư viện toán: `gcc bai2.c -o bai2 -lm`.

💡 C không có hàm `max` dựng sẵn, nên ở đây dùng toán tử ba ngôi `can - 2 > 0 ? can - 2 : 0`.

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>

bool laThuanNghich(long long n) {
    if (n < 0) return false;

    long long tam = n, dao = 0;
    while (tam > 0) {
        dao = dao * 10 + tam % 10;
        tam /= 10;
    }
    return dao == n;
}

int main(void) {
    printf("Cac so thuan nghich tu 100 den 200:\n");
    for (int i = 100; i <= 200; i++) {
        if (laThuanNghich(i)) printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

Output: `101 111 121 131 141 151 161 171 181 191`

### Bài 4.

```c
#include <stdio.h>

int demUoc(long long n) {
    if (n <= 0) return 0;
    int dem = 0;
    for (long long i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            dem++;                          // uoc i
            if (i != n / i) dem++;          // uoc n/i (neu khac i)
        }
    }
    return dem;
}

long long tongUoc(long long n) {
    if (n <= 0) return 0;
    long long tong = 0;
    for (long long i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            tong += i;
            if (i != n / i) tong += n / i;
        }
    }
    return tong;
}

int main(void) {
    long long n;
    printf("Nhap n: ");
    scanf("%lld", &n);
    printf("So luong uoc : %d\n", demUoc(n));
    printf("Tong cac uoc : %lld\n", tongUoc(n));
    return 0;
}
```

**Nguyên lý O(√n):** các ước luôn đi theo **cặp** `(i, n/i)`. Ví dụ với `n = 36`:

```
1 x 36    <- duyet i=1, tim duoc ca 1 va 36
2 x 18
3 x 12
4 x 9
6 x 6     <- i = n/i, chi dem MOT lan
```

Chỉ cần duyệt `i` tới √n là thu được tất cả.

⚠️ **Điều kiện `i != n / i`** xử lý số chính phương: với `n = 36`, `i = 6` cho `n/i = 6` — không được đếm 2 lần.

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

long long tongUocThatSu(long long n) {      // tong cac uoc, KHONG tinh chinh no
    if (n <= 1) return 0;
    long long tong = 1;                      // 1 luon la uoc
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            tong += i;
            if (i != n / i) tong += n / i;
        }
    }
    return tong;
}

bool laHoanHao(long long n) {
    return n > 1 && tongUocThatSu(n) == n;
}

int main(void) {
    printf("Cac so hoan hao < 10000:\n");
    for (long long n = 2; n < 10000; n++) {
        if (laHoanHao(n)) {
            printf("%lld = 1", n);
            for (long long i = 2; i <= n / 2; i++)
                if (n % i == 0) printf(" + %lld", i);
            printf("\n");
        }
    }
    return 0;
}
```

Output:

```
Cac so hoan hao < 10000:
6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14
496 = 1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248
8128 = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 127 + 254 + 508 + 1016 + 2032 + 4064
```

💡 **Số hoàn hảo** là số bằng tổng các ước thật sự của nó. Chỉ có 4 số hoàn hảo < 10.000: **6, 28, 496, 8128**. Tất cả số hoàn hảo đã biết đều là số chẵn — chưa ai tìm được số hoàn hảo lẻ, và cũng chưa ai chứng minh được là không tồn tại.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

long long ucln(long long a, long long b) {
    a = llabs(a);
    b = llabs(b);
    while (b != 0) {
        long long tam = a % b;
        a = b;
        b = tam;
    }
    return a;
}

long long bcnn(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    // CHIA TRUOC roi moi NHAN de tranh tran so
    return llabs(a) / ucln(a, b) * llabs(b);
}

int main(void) {
    long long a, b;
    printf("Nhap 2 so: ");
    scanf("%lld %lld", &a, &b);
    printf("UCLN = %lld\n", ucln(a, b));
    printf("BCNN = %lld\n", bcnn(a, b));
    return 0;
}
```

💡 C **không có** hàm tính UCLN dựng sẵn, nên ta tự viết bằng thuật toán Euclid như trên. Hàm `llabs` (trị tuyệt đối cho `long long`) nằm trong `<stdlib.h>`.

⚠️ **`a / ucln * b` chứ không phải `a * b / ucln`.** Với `a = b = 10⁹`, phép `a * b = 10¹⁸` sát giới hạn `long long`; với số lớn hơn sẽ tràn. Chia trước thì kết quả trung gian luôn nhỏ, và phép chia luôn chia hết vì `ucln` là ước của `a`.

### Bài 7.

```c
#include <stdio.h>

long long fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;

    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        long long tiep = a + b;
        a = b;
        b = tiep;
    }
    return b;
}

int main(void) {
    printf("30 so Fibonacci dau tien:\n");
    for (int i = 0; i < 30; i++) {
        printf("%lld ", fibonacci(i));
    }
    printf("\n");
    return 0;
}
```

Output:

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 
```

⚠️ **Giới hạn:** `F(92) = 7.540.113.804.746.346.429` là số Fibonacci lớn nhất vừa `long long`. `F(93)` tràn.

⚠️ Code trên gọi `fibonacci(i)` 30 lần, mỗi lần tính lại từ đầu → O(n²). Để in dãy, tốt hơn là tính một lần:

```c
long long a = 0, b = 1;
for (int i = 0; i < 30; i++) {
    printf("%lld ", a);
    long long t = a + b; a = b; b = t;
}
```

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

void phanTichThuaSo(long long n) {
    if (n < 2) { printf("%lld khong phan tich duoc\n", n); return; }

    printf("%lld = ", n);
    bool dauTien = true;

    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            int soMu = 0;
            while (n % i == 0) { n /= i; soMu++; }

            if (!dauTien) printf(" * ");
            printf("%lld", i);
            if (soMu > 1) printf("^%d", soMu);
            dauTien = false;
        }
    }

    // Neu con lai > 1 thi day chinh la mot thua so nguyen to
    if (n > 1) {
        if (!dauTien) printf(" * ");
        printf("%lld", n);
    }
    printf("\n");
}

int main(void) {
    phanTichThuaSo(360);          // 360 = 2^3 * 3^2 * 5
    phanTichThuaSo(97);           // 97 = 97
    phanTichThuaSo(1024);         // 1024 = 2^10
    phanTichThuaSo(999999937);    // so nguyen to lon
    return 0;
}
```

Output:

```
360 = 2^3 * 3^2 * 5
97 = 97
1024 = 2^10
999999937 = 999999937
```

**Vì sao cần dòng `if (n > 1)` ở cuối:** sau vòng lặp, nếu `n` vẫn còn lớn hơn 1, đó là **một thừa số nguyên tố lớn hơn √n gốc**. Ví dụ với `n = 14`: vòng lặp chỉ chạy tới `i = 3`, tách được thừa số 2, còn lại `n = 7` — phải in ra.

### Bài 9.

```c
#include <stdio.h>
#include <stdbool.h>

#define N 1000000

bool laNguyenTo[N + 1];     // mang toan cuc: khong lo tran stack

void sangEratosthenes(int n) {
    for (int i = 0; i <= n; i++) laNguyenTo[i] = true;
    laNguyenTo[0] = laNguyenTo[1] = false;

    for (int i = 2; (long long)i * i <= n; i++) {
        if (laNguyenTo[i]) {
            // Bat dau tu i*i, vi cac boi nho hon da bi danh dau boi so nho hon
            for (long long j = (long long)i * i; j <= n; j += i) {
                laNguyenTo[j] = false;
            }
        }
    }
}

int main(void) {
    sangEratosthenes(N);

    int dem = 0;
    for (int i = 2; i <= N; i++) if (laNguyenTo[i]) dem++;

    printf("So luong so nguyen to <= %d la: %d\n", N, dem);

    printf("10 so dau  : ");
    int daIn = 0;
    for (int i = 2; i <= N && daIn < 10; i++)
        if (laNguyenTo[i]) { printf("%d ", i); daIn++; }
    printf("\n");
    return 0;
}
```

Output:

```
So luong so nguyen to <= 1000000 la: 78498
10 so dau  : 2 3 5 7 11 13 17 19 23 29 
```

**Cách hoạt động của sàng:**

```
Ban dau : 2 3 4 5 6 7 8 9 10 11 12 ...  (tat ca deu "co the la nguyen to")
i = 2   : gach 4, 6, 8, 10, 12, ...
i = 3   : gach 9, 12, 15, 18, ...
i = 5   : gach 25, 30, 35, ...
Con lai : 2 3 5 7 11 13 ...  <- cac so nguyen to
```

**2 tối ưu trong code:**
1. Vòng ngoài chỉ chạy tới √n — vì mọi hợp số ≤ n đều có ước nguyên tố ≤ √n
2. Vòng trong bắt đầu từ `i*i` — vì `2i, 3i, ..., (i−1)i` đã bị gạch bởi các số nhỏ hơn

**Độ phức tạp: O(n log log n)** — gần như tuyến tính.

⚠️ Mảng 10⁶ phần tử nên khai báo **toàn cục** (ngoài `main`). Khai báo trong `main` là biến cục bộ nằm trên stack, mảng quá lớn có thể làm chương trình bị crash.

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 1000000

bool nt[MAX + 1];

int main(void) {
    for (int i = 0; i <= MAX; i++) nt[i] = true;
    nt[0] = nt[1] = false;

    // Xay sang MOT LAN - O(n log log n)
    for (int i = 2; (long long)i * i <= MAX; i++) {
        if (nt[i]) {
            for (long long j = (long long)i * i; j <= MAX; j += i) nt[j] = false;
        }
    }

    int q;
    printf("So truy van: ");
    scanf("%d", &q);

    // Moi truy van chi ton O(1)
    while (q--) {
        int n;
        scanf("%d", &n);
        if (n < 0 || n > MAX) printf("Ngoai pham vi\n");
        else printf("%d: %s\n", n, nt[n] ? "YES" : "NO");
    }
    return 0;
}
```

**So sánh hiệu năng với 1000 truy vấn, mỗi số cỡ 10⁶:**

| Cách | Chi phí | Tổng bước |
|---|---|---|
| Kiểm tra từng số O(√n) | 1000 × 1000 | ~10⁶ |
| Sàng một lần + tra O(1) | 3×10⁶ (dựng sàng) + 1000 | ~3×10⁶ |

Với ít truy vấn thì cách 1 nhanh hơn; nhưng với **10⁵ truy vấn trở lên**, sàng vượt trội hoàn toàn. Đây là kỹ thuật **tiền xử lý (preprocessing)** — bỏ công sức một lần để mọi truy vấn sau đều tức thì.

⚠️ Trong C, mỗi phần tử `bool` chiếm 1 byte, nên sàng 10⁶ tốn khoảng 1 MB bộ nhớ. Muốn tiết kiệm hơn có thể nén mỗi số vào 1 bit bằng các phép toán bit, nhưng code sẽ phức tạp hơn.

### Bài 11.

```c
#include <stdio.h>

long long luyThuaNhanh(long long a, long long n, long long mod) {
    long long kq = 1;
    a %= mod;

    while (n > 0) {
        if (n & 1) kq = kq * a % mod;     // neu bit cuoi cua n la 1
        a = a * a % mod;                   // binh phuong co so
        n >>= 1;                           // dich phai 1 bit (chia 2)
    }
    return kq;
}

int main(void) {
    const long long MOD = 1000000007;
    printf("2^10 mod 1e9+7  = %lld\n", luyThuaNhanh(2, 10, MOD));   // 1024
    printf("3^5  mod 1e9+7  = %lld\n", luyThuaNhanh(3, 5, MOD));    // 243
    printf("2^100 mod 1e9+7 = %lld\n", luyThuaNhanh(2, 100, MOD));
    return 0;
}
```

**Nguyên lý:** dựa vào biểu diễn nhị phân của số mũ.

```
a^13 = a^(1101 he 2) = a^8 × a^4 × a^1
```

Thay vì nhân 13 lần, chỉ cần 4 lần bình phương + 3 lần nhân.

**Độ phức tạp: O(log n)** thay vì O(n). Với `n = 10¹⁸`, chỉ cần ~60 bước thay vì 10¹⁸.

⚠️ **Lấy dư sau mỗi phép nhân** để tránh tràn số. Với `mod` tới 10⁹, phép `kq * a` có thể tới 10¹⁸ — vừa đủ `long long`. Nếu `mod` lớn hơn, phải dùng kiểu mở rộng `__int128` của gcc (không thuộc C chuẩn).

### Bài 12.

```c
#include <stdio.h>

long long luyThuaNhanh(long long a, long long n, long long mod) {
    long long kq = 1;
    a %= mod;
    while (n > 0) {
        if (n & 1) kq = kq * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return kq;
}

int main(void) {
    const long long MOD = 1000000007;
    printf("2^1000 mod (10^9+7) = %lld\n", luyThuaNhanh(2, 1000, MOD));
    return 0;
}
```

Output:

```
2^1000 mod (10^9+7) = 688423210
```

💡 Số `2^1000` có hơn 300 chữ số — không kiểu dữ liệu nào lưu nổi. Nhưng nhờ tính chất của phép đồng dư `(a × b) mod m = ((a mod m) × (b mod m)) mod m`, ta luôn giữ được giá trị trung gian nhỏ và vẫn tính đúng kết quả cuối.

Chỉ mất **10 vòng lặp** (vì 1000 < 2¹⁰).

### Bài 13.

```c
#include <stdio.h>

// Dem so chu so 0 o CUOI cua n!
int demSoKhongCuoi(long long n) {
    int dem = 0;
    for (long long p = 5; p <= n; p *= 5) {
        dem += n / p;
    }
    return dem;
}

int main(void) {
    long long ds[] = {5, 10, 25, 100, 1000};
    for (int i = 0; i < 5; i++) {
        printf("%lld! co %d chu so 0 o cuoi\n", ds[i], demSoKhongCuoi(ds[i]));
    }
    return 0;
}
```

Output:

```
5! co 1 chu so 0 o cuoi
10! co 2 chu so 0 o cuoi
25! co 6 chu so 0 o cuoi
100! co 24 chu so 0 o cuoi
1000! co 249 chu so 0 o cuoi
```

**Giải thích công thức (Legendre):**

Mỗi chữ số 0 ở cuối sinh ra từ một thừa số **10 = 2 × 5**. Trong `n!`, số lượng thừa số 2 luôn **nhiều hơn** số lượng thừa số 5. Vậy số chữ số 0 = **số thừa số 5** trong `n!`.

Công thức Legendre đếm số mũ của số nguyên tố `p` trong `n!`:

```
⌊n/p⌋ + ⌊n/p²⌋ + ⌊n/p³⌋ + ...
```

Ví dụ `n = 100`:
```
⌊100/5⌋  = 20   (cac so 5, 10, 15, ..., 100)
⌊100/25⌋ = 4    (cac so 25, 50, 75, 100 dong gop THEM mot thua so 5)
⌊100/125⌋= 0
Tong = 24 ✔
```

**Độ phức tạp O(log₅ n)** — tính được cho `n` tới 10¹⁸ trong tích tắc, dù `n!` là số khổng lồ.

### Bài 14.

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

long long ucln(long long a, long long b) {
    while (b != 0) { long long t = a % b; a = b; b = t; }
    return llabs(a);
}

bool nguyenToCungNhau(long long a, long long b) {
    return ucln(a, b) == 1;
}

int main(void) {
    const int M = 60;
    int dem = 0;

    printf("Cac so trong 1..100 nguyen to cung nhau voi %d:\n", M);
    for (int i = 1; i <= 100; i++) {
        if (nguyenToCungNhau(i, M)) {
            printf("%d ", i);
            dem++;
        }
    }
    printf("\nTong cong: %d so\n", dem);
    return 0;
}
```

Output:

```
Cac so trong 1..100 nguyen to cung nhau voi 60:
1 7 11 13 17 19 23 29 31 37 41 43 47 49 53 59 61 67 71 73 77 79 83 89 91 97 
Tong cong: 26 so
```

💡 **Liên hệ với hàm Euler φ(n):** số lượng số trong `1..n` nguyên tố cùng nhau với `n`. Với `n = 60 = 2²×3×5`:

```
φ(60) = 60 × (1 − 1/2) × (1 − 1/3) × (1 − 1/5) = 60 × 1/2 × 2/3 × 4/5 = 16
```

Trong `1..100` thì nhiều hơn 16 vì có thêm các số từ 61 đến 100.

### Bài 15.

**File `sohoc.h`:**

```c
#ifndef SOHOC_H
#define SOHOC_H

#include <stdbool.h>

/** @brief Kiem tra n co phai so nguyen to. @return true neu n >= 2 va la nguyen to. */
bool laNguyenTo(long long n);

/** @brief Kiem tra n co phai so chinh phuong (xu ly dung sai so sqrt). */
bool laChinhPhuong(long long n);

/** @brief Kiem tra n co phai so thuan nghich (doi xung). */
bool laThuanNghich(long long n);

/** @brief Dem so luong uoc duong cua n. Do phuc tap O(sqrt(n)). */
int demUoc(long long n);

/** @brief Tong tat ca uoc duong cua n (bao gom chinh n). */
long long tongUoc(long long n);

/** @brief Kiem tra n co phai so hoan hao (tong uoc that su = n). */
bool laHoanHao(long long n);

/** @brief Uoc chung lon nhat (thuat toan Euclid). Luon tra ve gia tri khong am. */
long long ucln(long long a, long long b);

/** @brief Boi chung nho nhat. Tra ve 0 neu mot trong hai so bang 0. */
long long bcnn(long long a, long long b);

/** @brief So Fibonacci thu n (F0 = 0, F1 = 1). Dung toi n = 92. */
long long fibonacci(int n);

/** @brief Phan tich n ra thua so nguyen to, in ra man hinh dang 360 = 2^3 * 3^2 * 5 */
void phanTichThuaSo(long long n);

/**
 * @brief Sang Eratosthenes.
 * @param nt Mang co it nhat n+1 phan tu, do nguoi goi cap phat.
 * @param n  Gioi han tren.
 * Sau khi goi: nt[i] = true neu i la so nguyen to.
 */
void sangNguyenTo(bool nt[], int n);

/** @brief Tinh (a^n) mod m bang luy thua nhi phan. Do phuc tap O(log n). */
long long luyThuaNhanh(long long a, long long n, long long mod);

/** @brief Dem so chu so 0 o cuoi cua n! (cong thuc Legendre voi co so 5). */
int demSoKhongCuoiGiaiThua(long long n);

/** @brief Kiem tra 2 so co nguyen to cung nhau (UCLN = 1). */
bool nguyenToCungNhau(long long a, long long b);

#endif
```

**File `sohoc.c`:**

```c
#include "sohoc.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

bool laNguyenTo(long long n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0) return false;
    for (long long i = 3; i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

bool laChinhPhuong(long long n) {
    if (n < 0) return false;
    long long can = (long long)sqrtl((long double)n);
    long long batDau = can - 2 > 0 ? can - 2 : 0;
    for (long long k = batDau; k <= can + 2; k++)
        if (k * k == n) return true;
    return false;
}

bool laThuanNghich(long long n) {
    if (n < 0) return false;
    long long tam = n, dao = 0;
    while (tam > 0) { dao = dao * 10 + tam % 10; tam /= 10; }
    return dao == n;
}

int demUoc(long long n) {
    if (n <= 0) return 0;
    int dem = 0;
    for (long long i = 1; i * i <= n; i++)
        if (n % i == 0) { dem++; if (i != n / i) dem++; }
    return dem;
}

long long tongUoc(long long n) {
    if (n <= 0) return 0;
    long long tong = 0;
    for (long long i = 1; i * i <= n; i++)
        if (n % i == 0) { tong += i; if (i != n / i) tong += n / i; }
    return tong;
}

bool laHoanHao(long long n) {
    return n > 1 && tongUoc(n) - n == n;
}

long long ucln(long long a, long long b) {
    a = llabs(a); b = llabs(b);
    while (b != 0) { long long t = a % b; a = b; b = t; }
    return a;
}

long long bcnn(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return llabs(a) / ucln(a, b) * llabs(b);
}

long long fibonacci(int n) {
    if (n <= 0) return 0;
    if (n == 1) return 1;
    long long a = 0, b = 1;
    for (int i = 2; i <= n; i++) { long long t = a + b; a = b; b = t; }
    return b;
}

void phanTichThuaSo(long long n) {
    if (n < 2) { printf("%lld khong phan tich duoc\n", n); return; }
    printf("%lld = ", n);
    bool dauTien = true;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            int soMu = 0;
            while (n % i == 0) { n /= i; soMu++; }
            if (!dauTien) printf(" * ");
            printf("%lld", i);
            if (soMu > 1) printf("^%d", soMu);
            dauTien = false;
        }
    }
    if (n > 1) { if (!dauTien) printf(" * "); printf("%lld", n); }
    printf("\n");
}

void sangNguyenTo(bool nt[], int n) {
    for (int i = 0; i <= n; i++) nt[i] = true;
    if (n >= 0) nt[0] = false;
    if (n >= 1) nt[1] = false;
    for (int i = 2; (long long)i * i <= n; i++)
        if (nt[i])
            for (long long j = (long long)i * i; j <= n; j += i) nt[j] = false;
}

long long luyThuaNhanh(long long a, long long n, long long mod) {
    long long kq = 1;
    a %= mod;
    while (n > 0) {
        if (n & 1) kq = kq * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return kq;
}

int demSoKhongCuoiGiaiThua(long long n) {
    int dem = 0;
    for (long long p = 5; p <= n; p *= 5) dem += n / p;
    return dem;
}

bool nguyenToCungNhau(long long a, long long b) {
    return ucln(a, b) == 1;
}
```

**File `main.c` — kiểm thử:**

```c
#include <stdio.h>
#include "sohoc.h"

const char *tf(bool b) { return b ? "true" : "false"; }

int main(void) {
    printf("laNguyenTo(97)          : %s\n", tf(laNguyenTo(97)));
    printf("laChinhPhuong(144)      : %s\n", tf(laChinhPhuong(144)));
    printf("laThuanNghich(12321)    : %s\n", tf(laThuanNghich(12321)));
    printf("demUoc(36)              : %d\n", demUoc(36));
    printf("tongUoc(28)             : %lld\n", tongUoc(28));
    printf("laHoanHao(496)          : %s\n", tf(laHoanHao(496)));
    printf("ucln(48, 18)            : %lld\n", ucln(48, 18));
    printf("bcnn(4, 6)              : %lld\n", bcnn(4, 6));
    printf("fibonacci(50)           : %lld\n", fibonacci(50));
    printf("luyThuaNhanh(2,1000,1e9+7): %lld\n", luyThuaNhanh(2, 1000, 1000000007));
    printf("demSoKhongCuoi(100!)    : %d\n", demSoKhongCuoiGiaiThua(100));
    printf("nguyenToCungNhau(7, 60) : %s\n", tf(nguyenToCungNhau(7, 60)));

    printf("\nPhan tich thua so:\n");
    phanTichThuaSo(360);
    phanTichThuaSo(1024);

    bool nt[101];
    sangNguyenTo(nt, 100);
    printf("\nSo nguyen to <= 100: ");
    for (int i = 2; i <= 100; i++) if (nt[i]) printf("%d ", i);
    printf("\n");
    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall -O2 main.c sohoc.c -o sohoc -lm
./sohoc
```

💡 **Header guard** `#ifndef SOHOC_H / #define SOHOC_H / #endif` giúp file `.h` không bị nạp hai lần khi nhiều file cùng `#include` nó. Nhiều trình biên dịch cũng hỗ trợ `#pragma once`, nhưng đó không phải C chuẩn.

💡 Trong C, hàm không thể trả về cả một mảng, nên `sangNguyenTo` nhận mảng do người gọi chuẩn bị sẵn và điền kết quả vào đó.

💡 **Hãy giữ thư viện này lại** — bạn sẽ dùng các hàm trong đó cho rất nhiều bài tập ở các chương sau, và cả khi đi thi lập trình.
