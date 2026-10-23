# Lời giải — [C]. Bài Tập Mảng 1 Chiều P1

[← Quay lại bài học](../06-02-c-bai-tap-mang-1-chieu-p1.md)

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n <= 0) return 0;
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i];
    double tb = (double)tong / n;

    long long tongLon = 0;
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] > tb) { tongLon += a[i]; dem++; }
    }

    printf("Trung binh cong = %.2f\n", tb);
    printf("Co %d phan tu lon hon TB, tong = %lld\n", dem, tongLon);
    return 0;
}
```

⚠️ Phải duyệt **2 lần**: lần đầu tính trung bình, lần sau mới so sánh. Không thể làm trong một lần vì chưa biết trung bình khi đang duyệt.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    if (n <= 0) return 0;
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int giaTri = a[0], soLanMax = 0;

    for (int i = 0; i < n; i++) {
        int dem = 0;
        for (int j = 0; j < n; j++) {
            if (a[j] == a[i]) dem++;
        }
        if (dem > soLanMax) { soLanMax = dem; giaTri = a[i]; }
    }

    printf("Phan tu %d xuat hien %d lan\n", giaTri, soLanMax);
    return 0;
}
```

Độ phức tạp **O(n²)**. Với `n` lớn, **sắp xếp trước** bằng `qsort` rồi đếm các đoạn giá trị bằng nhau liên tiếp sẽ nhanh hơn:

```c
#include <stdlib.h>

int soSanh(const void *x, const void *y) {
    int a = *(const int *)x, b = *(const int *)y;
    return (a > b) - (a < b);          // am / 0 / duong
}

// trong main, sau khi nhap mang:
qsort(a, n, sizeof(int), soSanh);
int giaTri = a[0], soLanMax = 0, dem = 0;
for (int i = 0; i < n; i++) {
    dem = (i > 0 && a[i] == a[i - 1]) ? dem + 1 : 1;   // do dai doan bang nhau
    if (dem > soLanMax) { soLanMax = dem; giaTri = a[i]; }
}
```

Cách này là **O(n log n)**. Sau khi sắp xếp, các giá trị bằng nhau đứng liền nhau nên chỉ cần duyệt một lần.

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int soSanh(const void *x, const void *y) {
    int a = *(const int *)x, b = *(const int *)y;
    return (a > b) - (a < b);
}

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    // Cach 1: O(n^2) - duyet moi cap
    bool coTrung = false;
    for (int i = 0; i < n && !coTrung; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] == a[j]) {
                printf("Trung lap: a[%d] = a[%d] = %d\n", i, j, a[i]);
                coTrung = true;
                break;
            }
        }
    }
    if (!coTrung) printf("Khong co phan tu trung lap\n");

    // Cach 2: O(n log n) - sap xep ban sao roi so sanh 2 phan tu ke nhau
    int b[1000];
    for (int i = 0; i < n; i++) b[i] = a[i];
    qsort(b, n, sizeof(int), soSanh);
    bool trung2 = false;
    for (int i = 1; i < n; i++) {
        if (b[i] == b[i - 1]) { trung2 = true; break; }
    }
    printf("Kiem tra bang sap xep: %s\n", trung2 ? "CO trung" : "KHONG trung");
    return 0;
}
```

💡 **Mẹo sắp xếp:** sau khi sắp xếp, các phần tử bằng nhau luôn **đứng cạnh nhau**, nên chỉ cần so sánh `b[i]` với `b[i-1]`. Sắp xếp trên **bản sao** `b` để không làm mất thứ tự của mảng gốc.

💡 Hàm so sánh cho `qsort` trả về số âm / 0 / số dương. Viết `(a > b) - (a < b)` thay cho `a - b` để tránh tràn số khi `a`, `b` trái dấu và rất lớn.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int chan[1000], le[1000];
    int soChan = 0, soLe = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) chan[soChan++] = a[i];
        else               le[soLe++]     = a[i];
    }

    printf("Mang chan (%d phan tu): ", soChan);
    for (int i = 0; i < soChan; i++) printf("%d ", chan[i]);
    printf("\n");

    printf("Mang le   (%d phan tu): ", soLe);
    for (int i = 0; i < soLe; i++) printf("%d ", le[i]);
    printf("\n");
    return 0;
}
```

💡 Kỹ thuật `chan[soChan++] = a[i]` — gán rồi tăng chỉ số trong một dòng, rất hay dùng khi xây mảng mới.

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    if (n == 0) return 0;

    int doDaiMax = 1, batDauMax = 0;
    int doDaiHienTai = 1, batDauHienTai = 0;

    for (int i = 1; i < n; i++) {
        if (a[i] > a[i - 1]) {
            doDaiHienTai++;
        } else {
            doDaiHienTai = 1;
            batDauHienTai = i;
        }

        if (doDaiHienTai > doDaiMax) {
            doDaiMax  = doDaiHienTai;
            batDauMax = batDauHienTai;
        }
    }

    printf("Day con tang dai nhat co %d phan tu: ", doDaiMax);
    for (int i = batDauMax; i < batDauMax + doDaiMax; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Ví dụ `{5, 1, 2, 3, 7, 2, 4}` → dãy `1 2 3 7` (4 phần tử).

**Ý tưởng:** đếm độ dài dãy tăng hiện tại; gặp phần tử không tăng thì đặt lại về 1. Luôn cập nhật kỷ lục. Độ phức tạp **O(n)**.

### Bài 6.

```c
#include <stdio.h>
#include <limits.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tongMax = LLONG_MIN, tongHienTai = 0;
    int batDau = 0, ketThuc = 0, batDauTam = 0;

    for (int i = 0; i < n; i++) {
        if (tongHienTai <= 0) {          // tong am -> bo di, bat dau lai
            tongHienTai = a[i];
            batDauTam = i;
        } else {
            tongHienTai += a[i];
        }

        if (tongHienTai > tongMax) {
            tongMax  = tongHienTai;
            batDau   = batDauTam;
            ketThuc  = i;
        }
    }

    printf("Tong lon nhat = %lld\n", tongMax);
    printf("Day con: ");
    for (int i = batDau; i <= ketThuc; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Ví dụ `{-2, 1, -3, 4, -1, 2, 1, -5, 4}` → tổng lớn nhất **6**, dãy con `4 -1 2 1`.

**Thuật toán Kadane — ý tưởng cốt lõi:** nếu tổng tích luỹ đang **âm**, giữ lại nó chỉ làm kết quả tệ đi, nên vứt bỏ và bắt đầu lại từ phần tử hiện tại.

Độ phức tạp **O(n)** — so với cách duyệt mọi dãy con là O(n²) hoặc O(n³).

### Bài 7.

```c
#include <stdio.h>

// Dao nguoc doan a[trai..phai]
void daoDoan(int a[], int trai, int phai) {
    while (trai < phai) {
        int tam = a[trai];
        a[trai] = a[phai];
        a[phai] = tam;
        trai++;
        phai--;
    }
}

int main(void) {
    int n, k;
    scanf("%d", &n);
    if (n <= 0) return 0;
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Nhap k: ");
    scanf("%d", &k);

    k = ((k % n) + n) % n;              // chuan hoa k, xu ly ca k am va k > n

    // Ky thuat DAO 3 LAN - O(n) thoi gian, O(1) bo nho
    daoDoan(a, 0, n - 1);               // dao toan bo
    daoDoan(a, 0, k - 1);               // dao k phan tu dau
    daoDoan(a, k, n - 1);               // dao phan con lai

    printf("Sau khi xoay phai %d vi tri: ", k);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Ví dụ `{1,2,3,4,5}` với `k = 2`:

```
Ban dau       : 1 2 3 4 5
Dao toan bo   : 5 4 3 2 1
Dao 2 dau     : 4 5 3 2 1
Dao phan sau  : 4 5 1 2 3   ✔
```

💡 **Kỹ thuật đảo 3 lần** rất thanh lịch: O(n) thời gian, O(1) bộ nhớ. Cách ngây thơ (dịch từng phần tử `k` lần) là O(n×k), còn cách dùng mảng phụ tốn O(n) bộ nhớ.

💡 C không có hàm đảo mảng dựng sẵn nên ta tự viết `daoDoan` — nhận chỉ số **đầu và cuối** của đoạn cần đảo.

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    int n, m;
    printf("Nhap so phan tu mang A: "); scanf("%d", &n);
    int a[1000];
    printf("Nhap %d phan tu (da sap xep tang dan): ", n);
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Nhap so phan tu mang B: "); scanf("%d", &m);
    int b[1000];
    printf("Nhap %d phan tu (da sap xep tang dan): ", m);
    for (int i = 0; i < m; i++) scanf("%d", &b[i]);

    int c[2000];
    int i = 0, j = 0, k = 0;

    // Gop bang 2 con tro - O(n + m)
    while (i < n && j < m) {
        if (a[i] <= b[j]) c[k++] = a[i++];
        else              c[k++] = b[j++];
    }
    while (i < n) c[k++] = a[i++];       // phan con lai cua A
    while (j < m) c[k++] = b[j++];       // phan con lai cua B

    printf("Mang sau khi gop: ");
    for (int t = 0; t < k; t++) printf("%d ", c[t]);
    printf("\n");
    return 0;
}
```

Ví dụ: `A = {1,3,5,7}`, `B = {2,4,6}` → `1 2 3 4 5 6 7`

**Kỹ thuật 2 con trỏ:** mỗi lần lấy phần tử nhỏ hơn trong 2 đầu và tiến con trỏ tương ứng. Độ phức tạp **O(n+m)** — tốt hơn hẳn việc nối rồi sắp xếp bằng `qsort` (O((n+m)log(n+m))).

Đây chính là bước "trộn" trong thuật toán **Merge Sort**.

### Bài 9.

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int soSanh(const void *x, const void *y) {
    int a = *(const int *)x, b = *(const int *)y;
    return (a > b) - (a < b);
}

int main(void) {
    int n, x;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);
    printf("Nhap x: ");
    scanf("%d", &x);

    // Cach 1: O(n^2) - duyet moi cap
    bool timThay = false;
    for (int i = 0; i < n && !timThay; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == x) {
                printf("Cach 1: %d + %d = %d (vi tri %d, %d)\n", a[i], a[j], x, i, j);
                timThay = true;
                break;
            }
        }
    }

    // Cach 2: O(n log n) - sap xep ban sao + 2 con tro
    int b[1000];
    for (int i = 0; i < n; i++) b[i] = a[i];
    qsort(b, n, sizeof(int), soSanh);
    int trai = 0, phai = n - 1;
    while (trai < phai) {
        long long tong = (long long)b[trai] + b[phai];
        if (tong == x) {
            printf("Cach 2: %d + %d = %d\n", b[trai], b[phai], x);
            break;
        }
        if (tong < x) trai++;            // tong nho qua -> tang ben trai
        else          phai--;            // tong lon qua -> giam ben phai
    }

    if (!timThay) printf("Khong tim thay cap nao\n");
    return 0;
}
```

**Cách 2 — ý tưởng:** sau khi sắp xếp, đặt một con trỏ ở đầu và một ở cuối. Nếu tổng nhỏ hơn `x` thì tiến con trỏ trái (tăng tổng); lớn hơn thì lùi con trỏ phải (giảm tổng). Mỗi bước loại bỏ được một phần tử, nên sau khi sắp xếp chỉ mất **O(n)**.

Đây chính là bài **Two Sum** nổi tiếng trên LeetCode.

⚠️ Cách 2 cho biết **giá trị** của 2 phần tử, còn vị trí trong mảng gốc đã thay đổi do sắp xếp. Nếu cần vị trí gốc, phải lưu kèm chỉ số (ví dụ dùng mảng `struct { int giaTri, viTri; }`).

### Bài 10.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Cac phan tu dinh: ");
    int dem = 0;
    for (int i = 1; i < n - 1; i++) {        // bo qua 2 dau mut
        if (a[i] > a[i - 1] && a[i] > a[i + 1]) {
            printf("%d(vt %d) ", a[i], i);
            dem++;
        }
    }
    if (dem == 0) printf("(khong co)");
    printf("\n");
    return 0;
}
```

Ví dụ `{1, 5, 2, 8, 3, 9, 4}` → đỉnh là `5`, `8`, `9`.

⚠️ Vòng lặp chạy từ `1` tới `n-2` — phần tử đầu và cuối chỉ có 1 phần tử kề nên không xét (tuỳ định nghĩa bài toán).

### Bài 11.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    // Ky thuat 2 con tro: j tro toi vi tri tiep theo can dat phan tu khac 0
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != 0) a[j++] = a[i];
    }
    while (j < n) a[j++] = 0;            // dien 0 vao phan con lai

    printf("Sau khi dich chuyen: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Ví dụ `{0, 1, 0, 3, 12}` → `1 3 12 0 0`

**Ý tưởng:** duyệt một lần, "dồn" mọi phần tử khác 0 về đầu mảng (giữ nguyên thứ tự), rồi điền 0 vào phần còn lại. Độ phức tạp **O(n)**, bộ nhớ **O(1)**.

### Bài 12.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int kcMax = -1, vt1 = -1, vt2 = -1;

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] == a[j] && j - i > kcMax) {
                kcMax = j - i;
                vt1 = i; vt2 = j;
            }
        }
    }

    if (kcMax == -1) {
        printf("Khong co 2 phan tu nao bang nhau\n");
    } else {
        printf("Khoang cach lon nhat = %d giua a[%d] va a[%d] = %d\n",
               kcMax, vt1, vt2, a[vt1]);
    }
    return 0;
}
```

Ví dụ `{1, 2, 3, 1, 4, 2}` → khoảng cách lớn nhất là 4 (giữa vị trí 1 và 5, giá trị 2); cặp giá trị 1 chỉ cách nhau 3.

💡 Cách tối ưu O(n) khi các giá trị nằm trong khoảng nhỏ (ví dụ `0 ≤ a[i] ≤ 10⁶`): dùng mảng `lanDau` lưu **vị trí đầu tiên** của mỗi giá trị:

```c
#define MAXV 1000000
int lanDau[MAXV + 1];                        // mang toan cuc

// trong main:
for (int v = 0; v <= MAXV; v++) lanDau[v] = -1;   // -1 = chua gap
int kcMax = -1;
for (int i = 0; i < n; i++) {
    if (lanDau[a[i]] != -1) {
        if (i - lanDau[a[i]] > kcMax) kcMax = i - lanDau[a[i]];
    } else {
        lanDau[a[i]] = i;
    }
}
```

### Bài 13.

```c
#include <stdio.h>

int main(void) {
    int n;      // day goc co n so tu 1..n, mang chi co n-1 phan tu
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[1000];
    printf("Nhap %d phan tu: ", n - 1);
    for (int i = 0; i < n - 1; i++) scanf("%d", &a[i]);

    // Cach 1: hieu cua tong
    long long tongDayDu = (long long)n * (n + 1) / 2;
    long long tongThucTe = 0;
    for (int i = 0; i < n - 1; i++) tongThucTe += a[i];
    printf("Cach 1 (tong): so thieu = %lld\n", tongDayDu - tongThucTe);

    // Cach 2: XOR - khong so tran so du n rat lon
    int xorTatCa = 0;
    for (int i = 1; i <= n; i++)    xorTatCa ^= i;
    for (int i = 0; i < n - 1; i++) xorTatCa ^= a[i];
    printf("Cach 2 (XOR) : so thieu = %d\n", xorTatCa);

    return 0;
}
```

**Cách 1 — hiệu của tổng:** tổng `1+2+...+n = n(n+1)/2`. Trừ đi tổng thực tế là ra số thiếu. Đơn giản nhất.

**Cách 2 — XOR:** dựa vào tính chất `x ^ x = 0` và `x ^ 0 = x`. XOR tất cả số từ 1..n với tất cả phần tử trong mảng: mọi số xuất hiện 2 lần triệt tiêu nhau, chỉ còn lại số thiếu.

**Ưu điểm của XOR:** không bao giờ tràn số, kể cả khi `n` rất lớn.

Cả hai đều **O(n)** thời gian, **O(1)** bộ nhớ.

### Bài 14.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    bool daGap[1001] = {false};          // danh dau cac gia tri 1..n (n <= 1000)
    bool laHoanVi = true;

    for (int i = 0; i < n; i++) {
        if (a[i] < 1 || a[i] > n) {          // ngoai pham vi 1..n
            laHoanVi = false;
            break;
        }
        if (daGap[a[i]]) {                   // gia tri bi trung
            laHoanVi = false;
            break;
        }
        daGap[a[i]] = true;
    }

    printf("Mang %s hoan vi cua 1..%d\n", laHoanVi ? "LA" : "KHONG phai", n);
    return 0;
}
```

**Điều kiện để là hoán vị của `1..n`:**
1. Mọi phần tử nằm trong khoảng `[1, n]`
2. Không có phần tử nào trùng lặp

Dùng **mảng đánh dấu** `daGap` để kiểm tra điều kiện 2 trong O(n). Xem thêm bài [06-06 — Mảng đánh dấu](../06-06-c-mang-danh-dau.md).

### Bài 15.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tongToanBo = 0;
    for (int i = 0; i < n; i++) tongToanBo += a[i];

    printf("Cac diem can bang: ");
    int dem = 0;
    long long tongTrai = 0;

    for (int i = 0; i < n; i++) {
        long long tongPhai = tongToanBo - tongTrai - a[i];
        if (tongTrai == tongPhai) {
            printf("%d ", i);
            dem++;
        }
        tongTrai += a[i];
    }

    if (dem == 0) printf("(khong co)");
    printf("\nTong cong: %d diem\n", dem);
    return 0;
}
```

Ví dụ `{1, 7, 3, 6, 5, 6}`:
- Tại vị trí 3 (giá trị 6): trái = 1+7+3 = 11, phải = 5+6 = 11 ✔

**Ý tưởng tối ưu:** thay vì với mỗi vị trí lại tính lại tổng 2 bên (O(n²)), ta:
1. Tính tổng toàn bộ **một lần**
2. Duy trì `tongTrai` tăng dần khi duyệt
3. `tongPhai = tongToanBo − tongTrai − a[i]`

Độ phức tạp **O(n)**. Đây là kỹ thuật **tổng tiền tố (prefix sum)** ở dạng đơn giản nhất.
