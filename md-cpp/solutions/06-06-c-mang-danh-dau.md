# Lời giải — [C]. Mảng Đánh Dấu

[← Quay lại bài học](../06-06-c-mang-danh-dau.md)

> **Mảng đánh dấu (counting array / frequency array):** dùng **giá trị** của phần tử làm **chỉ số** của một mảng phụ. Đổi thời gian tra cứu từ O(n) xuống **O(1)**, với cái giá là bộ nhớ.

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap so phan tu: ");
    scanf("%d", &n);

    int a[1000];
    int dem[101] = {0};             // khoi tao TAT CA bang 0

    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        if (a[i] >= 0 && a[i] <= 100) dem[a[i]]++;    // dung GIA TRI lam CHI SO
    }

    printf("Tan suat xuat hien:\n");
    for (int gt = 0; gt <= 100; gt++) {
        if (dem[gt] > 0) {
            printf("  %d xuat hien %d lan\n", gt, dem[gt]);
        }
    }
    return 0;
}
```

⚠️ **Bắt buộc khởi tạo mảng đếm bằng 0:** `int dem[101] = {0};`. Mảng cục bộ trong C **không** tự bằng 0 — nếu không khởi tạo, giá trị rác sẽ làm kết quả sai hoàn toàn. (Mảng toàn cục hoặc `static` thì tự được khởi tạo 0.)

⚠️ **Luôn kiểm tra biên** `a[i] >= 0 && a[i] <= 100` trước khi dùng làm chỉ số — nếu người dùng nhập 500 hoặc −3 thì chương trình sẽ ghi ra ngoài mảng và có thể crash.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    int dem[1001] = {0};            // gia tri trong [0, 1000]

    for (int i = 0; i < n; i++) { scanf("%d", &a[i]); dem[a[i]]++; }

    int giaTri = -1, soLanMax = 0;
    for (int gt = 0; gt <= 1000; gt++) {
        if (dem[gt] > soLanMax) { soLanMax = dem[gt]; giaTri = gt; }
    }

    printf("Phan tu %d xuat hien nhieu nhat: %d lan\n", giaTri, soLanMax);
    return 0;
}
```

💡 **So sánh với cách O(n²)** ở bài [06-02](../06-02-c-bai-tap-mang-1-chieu-p1.md) bài 2: cách này chỉ **O(n + M)** với M là phạm vi giá trị. Với `n = 10⁵` và `M = 1000`, nhanh hơn hàng nghìn lần.

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    int dem[1001] = {0};

    for (int i = 0; i < n; i++) { scanf("%d", &a[i]); dem[a[i]]++; }

    printf("Cac phan tu xuat hien dung 1 lan: ");
    bool co = false;
    for (int i = 0; i < n; i++) {
        if (dem[a[i]] == 1) { printf("%d ", a[i]); co = true; }
    }
    if (!co) printf("(khong co)");
    printf("\n");
    return 0;
}
```

💡 Duyệt theo mảng gốc `a[i]` giữ nguyên **thứ tự xuất hiện**; duyệt theo mảng `dem` sẽ cho thứ tự tăng dần theo giá trị.

### Bài 4.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAX 1000001

int main(void) {
    int n;
    scanf("%d", &n);
    static bool coMat[MAX];           // static: vung nho tinh, tu bang false, khong tran stack

    for (int i = 0; i < n; i++) {
        int x; scanf("%d", &x);
        if (x >= 0 && x < MAX) coMat[x] = true;
    }

    int nhoNhat = 0;
    while (nhoNhat < MAX && coMat[nhoNhat]) nhoNhat++;

    printf("So nho nhat khong xuat hien: %d\n", nhoNhat);
    return 0;
}
```

💡 **Dùng `bool` (từ `<stdbool.h>`) thay `int`** khi chỉ cần biết "có/không" — thường tiết kiệm 4 lần bộ nhớ (`bool` thường 1 byte, `int` thường 4 byte).

⚠️ **Từ khoá `static`** đặt mảng lớn vào vùng nhớ tĩnh thay vì stack. Mảng 1 triệu `bool` là khoảng 1 MB — nếu đặt trên stack (mặc định) có thể tràn.

Nếu chỉ quan tâm số **dương** nhỏ nhất không xuất hiện, đáp án luôn nằm trong `[1, n+1]`, nên mảng đánh dấu chỉ cần cỡ `n+2`.

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    bool daGap[1001] = {false};
    bool laHoanVi = true;

    for (int i = 0; i < n; i++) {
        if (a[i] < 1 || a[i] > n)  { laHoanVi = false; break; }   // ngoai pham vi
        if (daGap[a[i]])           { laHoanVi = false; break; }   // trung lap
        daGap[a[i]] = true;
    }

    printf("Mang %s hoan vi cua 1..%d\n", laHoanVi ? "LA" : "KHONG phai", n);
    return 0;
}
```

Độ phức tạp **O(n)**, tốt hơn cách sắp xếp rồi so sánh (O(n log n)).

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    bool daGap[1001] = {false};     // gia tri trong [0, 1000]
    int m = 0;

    for (int i = 0; i < n; i++) {
        if (!daGap[a[i]]) {
            daGap[a[i]] = true;
            a[m++] = a[i];              // giu lai lan xuat hien DAU TIEN
        }
    }
    n = m;

    printf("Sau khi loai trung lap: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Độ phức tạp **O(n)** — tốt hơn hẳn cách O(n²) ở bài [06-05](../06-05-c-chen-va-xoa-phan-tu.md) bài 6.

### Bài 7.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n, m;
    printf("So phan tu mang A: "); scanf("%d", &n);
    int a[1000];
    bool coTrongA[1001] = {false};
    for (int i = 0; i < n; i++) { scanf("%d", &a[i]); coTrongA[a[i]] = true; }

    printf("So phan tu mang B: "); scanf("%d", &m);
    int b[1000];
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    bool daIn[1001] = {false};
    printf("Cac phan tu chung: ");
    for (int i = 0; i < m; i++) {
        if (coTrongA[b[i]] && !daIn[b[i]]) {
            printf("%d ", b[i]);
            daIn[b[i]] = true;          // tranh in trung
        }
    }
    printf("\n");
    return 0;
}
```

💡 Mảng `daIn` thứ hai đảm bảo mỗi giá trị chung chỉ in **một lần**, dù nó xuất hiện nhiều lần trong B.

### Bài 8.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char s[1001];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof(s), stdin) == NULL) return 0;   // doc ca dong, co dau cach

    int dem[26] = {0};

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if (isalpha(c)) {
            dem[tolower(c) - 'a']++;         // 'a' -> 0, 'b' -> 1, ...
        }
    }

    printf("Tan suat cac chu cai:\n");
    for (int i = 0; i < 26; i++) {
        if (dem[i] > 0) {
            printf("  %c: %d\n", 'a' + i, dem[i]);
        }
    }
    return 0;
}
```

Với chuỗi `"Hello World"`:

```
  d: 1
  e: 1
  h: 1
  l: 3
  o: 2
  r: 1
  w: 1
```

💡 **Công thức chuyển đổi cốt lõi:**

```c
int chiSo = c - 'a';              // 'a'..'z'  ->  0..25
char kyTu = 'a' + chiSo;          // 0..25     ->  'a'..'z'
```

Áp dụng được vì các chữ cái nằm liên tiếp trong bảng ASCII.

⚠️ Ép sang `unsigned char` trước khi gọi `isalpha`/`tolower` — truyền `char` âm (ký tự ngoài ASCII) vào các hàm của `<ctype.h>` là hành vi không xác định.

### Bài 9.

```c
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

bool laDaoChu(const char s1[], const char s2[]) {
    int dem[26] = {0};

    for (int i = 0; s1[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s1[i];
        if (isalpha(c)) dem[tolower(c) - 'a']++;
    }
    for (int i = 0; s2[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s2[i];
        if (isalpha(c)) dem[tolower(c) - 'a']--;
    }

    for (int i = 0; i < 26; i++) if (dem[i] != 0) return false;
    return true;
}

int main(void) {
    char s1[1001], s2[1001];
    printf("Chuoi 1: ");
    if (fgets(s1, sizeof(s1), stdin) == NULL) return 0;
    printf("Chuoi 2: ");
    if (fgets(s2, sizeof(s2), stdin) == NULL) return 0;

    printf("%s\n", laDaoChu(s1, s2) ? "LA dao chu" : "KHONG phai dao chu");
    return 0;
}
```

Ví dụ:
- `"listen"` và `"silent"` → **LÀ đảo chữ**
- `"Dormitory"` và `"Dirty Room"` → **LÀ đảo chữ**
- `"hello"` và `"world"` → không

💡 **Kỹ thuật thanh lịch:** dùng **một** mảng đếm, chuỗi 1 **cộng**, chuỗi 2 **trừ**. Nếu hai chuỗi là đảo chữ thì tất cả về 0. Chỉ cần O(n) thời gian và O(26) bộ nhớ.

💡 `fgets` giữ lại ký tự `'\n'` cuối dòng, nhưng ở đây không ảnh hưởng vì ta chỉ đếm chữ cái.

Cách khác (chậm hơn): sắp xếp cả hai chuỗi rồi so sánh — O(n log n).

### Bài 10.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[1000];
    int dem[1001] = {0};

    printf("Nhap %d phan tu (1..%d): ", n, n);
    for (int i = 0; i < n; i++) { scanf("%d", &a[i]); dem[a[i]]++; }

    int lap = -1, thieu = -1;
    for (int gt = 1; gt <= n; gt++) {
        if (dem[gt] == 2) lap   = gt;
        if (dem[gt] == 0) thieu = gt;
    }

    printf("So bi lap   : %d\n", lap);
    printf("So bi thieu : %d\n", thieu);
    return 0;
}
```

Ví dụ `n = 5`, mảng `{1, 2, 2, 4, 5}` → lặp = 2, thiếu = 3.

💡 **Cách O(1) bộ nhớ** dùng công thức toán:

```
S  = tong thuc te - tong 1..n   = lap - thieu
S2 = tong binh phuong thuc te - tong binh phuong 1..n = lap² - thieu²
   = (lap - thieu)(lap + thieu) = S × (lap + thieu)
=> lap + thieu = S2 / S
=> giai he 2 phuong trinh
```

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>

void countingSort(int a[], int n) {
    if (n == 0) return;

    int mn = a[0], mx = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] < mn) mn = a[i];
        if (a[i] > mx) mx = a[i];
    }
    int phamVi = mx - mn + 1;

    int *dem = calloc(phamVi, sizeof(int));  // calloc: cap phat va gan toan 0
    if (dem == NULL) return;
    for (int i = 0; i < n; i++) dem[a[i] - mn]++;   // tru mn de chi so bat dau tu 0

    int k = 0;
    for (int i = 0; i < phamVi; i++) {
        for (int j = 0; j < dem[i]; j++) {
            a[k++] = i + mn;                // cong lai mn de tra ve gia tri goc
        }
    }
    free(dem);
}

int main(void) {
    int a[] = {5, 2, 9, 2, 7, 1, 5, 2};
    int n = sizeof(a) / sizeof(a[0]);

    printf("Ban dau : ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    countingSort(a, n);

    printf("Sau sort: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Output:

```
Ban dau : 5 2 9 2 7 1 5 2 
Sau sort: 1 2 2 2 5 5 7 9 
```

**Counting Sort — độ phức tạp O(n + k)** với `k` là phạm vi giá trị. Đây là thuật toán **nhanh hơn O(n log n)** — nhưng chỉ dùng được khi:

1. Dữ liệu là **số nguyên** (hoặc quy về số nguyên được)
2. **Phạm vi giá trị hẹp** so với `n`

⚠️ Với mảng 10 phần tử nhưng giá trị từ 1 đến 10⁹, cần mảng đếm 10⁹ phần tử — **hoàn toàn không khả thi**. Khi đó phải dùng `qsort` thông thường.

💡 Vì phạm vi giá trị chỉ biết lúc chạy, mảng đếm được cấp phát động bằng `calloc` và phải `free` sau khi dùng.

**Ứng dụng thực tế:** sắp xếp điểm số (0–10), tuổi (0–150), tần suất ký tự, xếp hạng.

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

#define N 1000000

bool laHopSo[N + 1];            // toan cuc: tu bang false, nghia la "chua bi gach"

int main(void) {
    laHopSo[0] = laHopSo[1] = true;     // 0 va 1 khong phai so nguyen to

    for (int i = 2; (long long)i * i <= N; i++) {
        if (!laHopSo[i]) {
            for (long long j = (long long)i * i; j <= N; j += i) {
                laHopSo[j] = true;          // DANH DAU la hop so
            }
        }
    }

    int dem = 0;
    for (int i = 2; i <= N; i++) if (!laHopSo[i]) dem++;

    printf("So luong so nguyen to <= %d: %d\n", N, dem);

    printf("20 so dau: ");
    int in = 0;
    for (int i = 2; i <= N && in < 20; i++)
        if (!laHopSo[i]) { printf("%d ", i); in++; }
    printf("\n");
    return 0;
}
```

Output:

```
So luong so nguyen to <= 1000000: 78498
20 so dau: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 
```

**Sàng Eratosthenes chính là ứng dụng kinh điển nhất của mảng đánh dấu:** thay vì kiểm tra từng số một (O(n√n)), ta dùng một mảng `bool` để **gạch** bội của từng số nguyên tố — chỉ O(n log log n).

💡 Đánh dấu **hợp số** (`laHopSo`) thay vì số nguyên tố giúp tận dụng việc mảng toàn cục tự khởi tạo bằng `false`, không cần vòng lặp gán `true` ban đầu. Mảng `bool` 10⁶ phần tử tốn khoảng 1 MB; muốn tiết kiệm hơn có thể tự nén mỗi phần tử thành 1 bit bằng các phép toán bit.

### Bài 13.

```c
#include <stdio.h>

#define MAX 100001

int main(void) {
    static int soLuong[MAX];          // luu SO LUONG thay vi bool, tu bang 0

    int q;
    printf("Nhap so thao tac: ");
    scanf("%d", &q);

    printf("Cac thao tac (+x them, -x xoa, ?x truy van):\n");
    while (q--) {
        char op;
        int x;
        scanf(" %c%d", &op, &x);      // dau cach truoc %c de bo qua ky tu trang

        if (x < 0 || x >= MAX) { printf("  Gia tri ngoai pham vi!\n"); continue; }

        if (op == '+') {
            soLuong[x]++;
            printf("  Da them %d\n", x);
        } else if (op == '-') {
            if (soLuong[x] > 0) { soLuong[x]--; printf("  Da xoa %d\n", x); }
            else printf("  %d khong co trong tap!\n", x);
        } else if (op == '?') {
            printf("  %d: %s (so luong = %d)\n", x,
                   soLuong[x] > 0 ? "CO" : "KHONG", soLuong[x]);
        }
    }
    return 0;
}
```

Ví dụ:

```
+5
+5
?5     ->  CO (so luong = 2)
-5
?5     ->  CO (so luong = 1)
-5
?5     ->  KHONG (so luong = 0)
```

💡 **Dùng `int` (đếm số lượng) thay vì `bool`** cho phép xử lý đúng trường hợp thêm cùng một giá trị nhiều lần (tập hợp cho phép trùng — multiset). Nếu chỉ cần tập hợp không trùng, `bool` là đủ.

⚠️ `scanf(" %c", ...)` có **dấu cách** trước `%c` để bỏ qua ký tự xuống dòng còn sót từ lần nhập trước.

Mọi thao tác đều **O(1)**.

### Bài 14.

| Tiêu chí | Mảng đánh dấu | 2 vòng lặp lồng nhau | Sắp xếp (`qsort`) rồi đếm |
|---|---|---|---|
| **Thời gian** | **O(n + M)** — nhanh nhất | O(n²) | O(n log n) |
| **Bộ nhớ thêm** | O(M) — phạm vi giá trị | O(1) | O(1) (sắp xếp tại chỗ) |
| **Giới hạn giá trị** | ⚠️ Phải biết trước và hẹp | ✅ Không giới hạn | ✅ Không giới hạn |
| **Kiểu dữ liệu** | ⚠️ Chỉ số nguyên nhỏ | ✅ Mọi kiểu so sánh bằng được | ✅ Mọi kiểu có hàm so sánh |
| **Giá trị âm** | ⚠️ Phải dịch chỉ số | ✅ Được | ✅ Được |
| **Giữ thứ tự xuất hiện** | ✅ Được (duyệt lại `a[]`) | ✅ Được | ❌ Mảng bị đổi thứ tự |
| **Độ khó cài đặt** | Dễ | Dễ nhất | Cần viết hàm so sánh |

(M là phạm vi giá trị, n là số phần tử.)

**✅ Dùng MẢNG ĐÁNH DẤU khi:**
- Giá trị là số nguyên trong phạm vi hẹp (≤ 10⁷)
- Cần tốc độ tối đa (lập trình thi đấu)
- Ví dụ: đếm tần suất chữ cái (26 ô), điểm số (0–10), sàng nguyên tố

**✅ Dùng SẮP XẾP rồi đếm khi:**
- Giá trị rải rác hoặc rất lớn (`long long`, số âm lớn)
- Số phần tử ít hơn nhiều so với phạm vi giá trị
- Không cần giữ thứ tự xuất hiện ban đầu

**✅ Dùng 2 VÒNG LẶP khi:** `n` nhỏ (vài nghìn) và muốn code đơn giản nhất.

**Ví dụ minh hoạ sự khác biệt:**

```c
// 5 phan tu: {1, 1000000000, 5, 999999999, 3}

int dem[1000000001];            // 4 GB -> KHONG KHA THI
qsort(a, 5, sizeof(int), cmp);  // sap xep 5 phan tu roi dem -> DUNG CACH NAY
```

```c
// 10^6 phan tu, gia tri trong [0, 100]

int dem[101];                   // 404 byte, O(n) -> TOI UU
// 2 vong lap: 10^12 phep so sanh -> khong kha thi
```

💡 **Mẹo xử lý giá trị âm với mảng đánh dấu** — dịch chỉ số:

```c
#define OFFSET 1000             // gia tri tu -1000 den 1000
int dem[2001] = {0};
dem[x + OFFSET]++;              // x = -5  ->  dem[995]++
```

### Bài 15.

```c
#include <stdio.h>

#define MAXTD 1000000

int saiPhan[MAXTD + 2];          // toan cuc: tu bang 0

int main(void) {
    int n, maxToaDo;
    printf("Nhap so khoang va toa do lon nhat: ");
    scanf("%d %d", &n, &maxToaDo);
    if (maxToaDo < 0 || maxToaDo > MAXTD) { printf("Toa do qua lon!\n"); return 1; }

    printf("Nhap %d khoang [l, r]:\n", n);
    for (int i = 0; i < n; i++) {
        int l, r;
        scanf("%d %d", &l, &r);
        if (l < 0 || r > maxToaDo || l > r) continue;   // bo qua khoang khong hop le
        saiPhan[l]     += 1;          // bat dau bao phu tu l
        saiPhan[r + 1] -= 1;          // ket thuc bao phu sau r
    }

    // Tinh tong tien to de ra so lan bao phu thuc te
    printf("\nSo lan bao phu tai moi diem:\n");
    int hienTai = 0, maxBaoPhu = 0, diemMax = 0;

    for (int i = 0; i <= maxToaDo; i++) {
        hienTai += saiPhan[i];
        printf("  Diem %d: %d\n", i, hienTai);
        if (hienTai > maxBaoPhu) { maxBaoPhu = hienTai; diemMax = i; }
    }

    printf("\nDiem duoc bao phu nhieu nhat: %d (%d khoang)\n", diemMax, maxBaoPhu);
    return 0;
}
```

Ví dụ với 3 khoảng `[1,4]`, `[2,6]`, `[5,7]`, `maxToaDo = 8`:

```
So lan bao phu tai moi diem:
  Diem 0: 0
  Diem 1: 1
  Diem 2: 2
  Diem 3: 2
  Diem 4: 2
  Diem 5: 2
  Diem 6: 2
  Diem 7: 1
  Diem 8: 0

Diem duoc bao phu nhieu nhat: 2 (2 khoang)
```

**Kỹ thuật mảng sai phân (difference array):**

Thay vì tăng từng phần tử trong khoảng `[l, r]` (tốn O(r−l+1) mỗi khoảng), ta chỉ đánh dấu **2 điểm**:

```
saiPhan[l]   += 1      <- "bat dau tang tu day"
saiPhan[r+1] -= 1      <- "ngung tang tu day"
```

Sau khi xử lý hết các khoảng, lấy **tổng tiền tố** một lần là có kết quả cuối.

**So sánh hiệu năng** với `n` khoảng trên trục dài `M`:

| Cách | Độ phức tạp |
|---|---|
| Tăng từng điểm trong mỗi khoảng | O(n × M) |
| **Mảng sai phân** | **O(n + M)** |

Với `n = 10⁵` khoảng trên trục dài 10⁶: cách đầu cần 10¹¹ bước (không khả thi), cách sai phân chỉ cần ~10⁶.

💡 **Ứng dụng thực tế:** đếm số người có mặt tại mỗi thời điểm (bài toán đặt phòng họp), tô màu đoạn, thống kê lưu lượng.
