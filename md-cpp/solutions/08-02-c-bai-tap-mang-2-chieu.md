# Lời giải — [C]. Bài Tập Mảng 2 Chiều

[← Quay lại bài học](../08-02-c-bai-tap-mang-2-chieu.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    int a[100][100], n;
    printf("Nhap kich thuoc ma tran vuong: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    long long cheoChinh = 0, cheoPhu = 0;
    for (int i = 0; i < n; i++) {
        cheoChinh += a[i][i];              // i == j
        cheoPhu   += a[i][n - 1 - i];      // i + j == n - 1
    }

    printf("Tong duong cheo chinh = %lld\n", cheoChinh);
    printf("Tong duong cheo phu   = %lld\n", cheoPhu);
    return 0;
}
```

**Hai công thức cần nhớ:**

| Đường chéo | Điều kiện |
|---|---|
| Chính (\\) | `i == j` |
| Phụ (/) | `i + j == n - 1` |

```
Cheo chinh:  X . .        Cheo phu:  . . X
             . X .                   . X .
             . . X                   X . .
```

⚠️ Với `n` lẻ, phần tử giữa `a[n/2][n/2]` thuộc **cả hai** đường chéo.

### Bài 2.

```c
#include <stdio.h>

int main() {
    int a[100][100], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    long long tren = 0, duoi = 0, cheo = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if      (j > i) tren += a[i][j];      // PHIA TREN duong cheo
            else if (j < i) duoi += a[i][j];      // PHIA DUOI
            else            cheo += a[i][j];      // TREN duong cheo
        }

    printf("Tong phia tren duong cheo = %lld\n", tren);
    printf("Tong phia duoi duong cheo = %lld\n", duoi);
    printf("Tong tren duong cheo      = %lld\n", cheo);
    return 0;
}
```

**Điều kiện vùng:**

```
j > i  -> PHIA TREN      . X X
j < i  -> PHIA DUOI      . . X
j == i -> DUONG CHEO     . . .
```

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int a[100][100], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    bool doiXung = true;
    for (int i = 0; i < n && doiXung; i++) {
        for (int j = i + 1; j < n; j++) {        // chi can xet NUA TREN
            if (a[i][j] != a[j][i]) { doiXung = false; break; }
        }
    }

    printf("Ma tran %s qua duong cheo chinh\n",
           doiXung ? "DOI XUNG" : "KHONG doi xung");
    return 0;
}
```

**Ma trận đối xứng:** `a[i][j] == a[j][i]` với mọi `i`, `j`.

```
1 2 3
2 5 6      <- doi xung
3 6 9
```

💡 **Tối ưu:** chỉ cần duyệt **nửa trên** (`j` bắt đầu từ `i+1`) — vì so sánh `a[i][j]` với `a[j][i]` đã bao trùm cả nửa dưới. Giảm một nửa số phép so sánh.

### Bài 4.

```c
#include <stdio.h>

void swap(int *x, int *y) {
    int t = *x; *x = *y; *y = t;
}

void inMT(int a[][100], int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    printf("\n");
}

int main() {
    int a[100][100] = {{1,2,3},{4,5,6},{7,8,9}};
    int n = 3, m = 3;

    printf("Ban dau:\n");                     inMT(a, n, m);

    // Hoan doi hang 0 va hang 2
    for (int j = 0; j < m; j++) swap(&a[0][j], &a[2][j]);
    printf("Sau khi doi hang 0 va 2:\n");     inMT(a, n, m);

    // Hoan doi cot 0 va cot 1
    for (int i = 0; i < n; i++) swap(&a[i][0], &a[i][1]);
    printf("Sau khi doi cot 0 va 1:\n");      inMT(a, n, m);

    return 0;
}
```

💡 **Đổi hàng** → duyệt qua các cột. **Đổi cột** → duyệt qua các hàng.

💡 C không có hàm `swap` sẵn — tự viết hàm nhận **2 con trỏ** và gọi `swap(&a[0][j], &a[2][j])`. `%5d` trong `printf` in số chiếm đủ 5 ô, căn phải, giúp ma trận thẳng cột.

💡 Nếu ma trận cấp phát động dạng `int **a` (mảng các con trỏ hàng), đổi 2 hàng chỉ cần tráo 2 con trỏ `a[0]` và `a[2]` — không phải sao chép từng phần tử.

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *x, const void *y) {
    int u = *(const int *)x, v = *(const int *)y;
    return (u > v) - (u < v);
}

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    // (1) Do ma tran ra mang 1 chieu
    static int b[10000];
    int k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) b[k++] = a[i][j];

    // (2) Sap xep
    qsort(b, k, sizeof(int), cmp);

    // (3) Do nguoc lai vao ma tran
    k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) a[i][j] = b[k++];

    printf("\nMa tran sau khi sap xep:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

💡 **Mẹo hay:** vì ma trận được lưu liên tục trong bộ nhớ (xem bài [08-01](../08-01-c-ly-thuyet-mang-2-chieu.md) bài 8), với mảng tĩnh có **đúng** `n` hàng `m` cột (khai báo `int a[n][m]` khít) có thể sort trực tiếp:

```c
qsort(&a[0][0], n * m, sizeof(int), cmp);   // chi dung khi ma tran KHIT (so cot khai bao = m)
```

⚠️ Cách này **sai** nếu bạn khai báo `a[100][100]` nhưng chỉ dùng `3×3` — vì các ô không dùng nằm xen giữa.

💡 Hàm so sánh viết `(u > v) - (u < v)` thay vì `u - v` để tránh tràn số khi `u`, `v` rất lớn/nhỏ.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

int cmp(const void *x, const void *y) {
    int u = *(const int *)x, v = *(const int *)y;
    return (u > v) - (u < v);
}

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    for (int i = 0; i < n; i++) {
        qsort(a[i], m, sizeof(int), cmp);     // a[i] la mang 1 chieu (1 hang)
    }

    printf("\nSau khi sap xep tung hang:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

💡 **`a[i]` chính là một mảng 1 chiều** (hàng thứ `i`), nên truyền trực tiếp cho `qsort` được.

**Sắp xếp từng cột** khó hơn vì các phần tử không liền nhau — phải copy ra mảng tạm:

```c
for (int j = 0; j < m; j++) {
    int cot[100];
    for (int i = 0; i < n; i++) cot[i] = a[i][j];
    qsort(cot, n, sizeof(int), cmp);
    for (int i = 0; i < n; i++) a[i][j] = cot[i];
}
```

### Bài 7.

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

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int hangTot = 0, demMax = -1;
    for (int i = 0; i < n; i++) {
        int dem = 0;
        for (int j = 0; j < m; j++)
            if (laNguyenTo(a[i][j])) dem++;

        printf("Hang %d: %d so nguyen to\n", i, dem);
        if (dem > demMax) { demMax = dem; hangTot = i; }
    }

    printf("\nHang %d co nhieu so nguyen to nhat (%d so)\n", hangTot, demMax);
    return 0;
}
```

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("Cac phan tu yen ngua:\n");
    int dem = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            // Kiem tra: nho nhat tren HANG i?
            bool nhoNhatHang = true;
            for (int k = 0; k < m; k++)
                if (a[i][k] < a[i][j]) { nhoNhatHang = false; break; }

            if (!nhoNhatHang) continue;

            // Kiem tra: lon nhat tren COT j?
            bool lonNhatCot = true;
            for (int k = 0; k < n; k++)
                if (a[k][j] > a[i][j]) { lonNhatCot = false; break; }

            if (lonNhatCot) {
                printf("  a[%d][%d] = %d\n", i, j, a[i][j]);
                dem++;
            }
        }
    }

    if (dem == 0) printf("  (khong co)\n");
    return 0;
}
```

Ví dụ với ma trận:

```
 1  2  3
 4  5  6
 7  8  9
```

→ Phần tử yên ngựa là `a[2][0] = 7` (nhỏ nhất hàng 2, lớn nhất cột 0).

💡 **Ứng dụng trong lý thuyết trò chơi:** điểm yên ngựa (saddle point) là **điểm cân bằng** của một trò chơi tổng bằng 0 — cả hai người chơi đều không có lợi khi thay đổi chiến lược.

### Bài 9.

```c
#include <stdio.h>

void inMT(int a[][100], int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    printf("\n");
}

void xoaHang(int a[][100], int *n, int m, int k) {
    if (k < 0 || k >= *n) return;
    for (int i = k; i < *n - 1; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = a[i + 1][j];
    (*n)--;
}

void xoaCot(int a[][100], int n, int *m, int k) {
    if (k < 0 || k >= *m) return;
    for (int i = 0; i < n; i++)
        for (int j = k; j < *m - 1; j++)
            a[i][j] = a[i][j + 1];
    (*m)--;
}

int main() {
    int a[100][100] = {
        {1,2,3,4}, {5,6,7,8}, {9,10,11,12}, {13,14,15,16}
    };
    int n = 4, m = 4;

    printf("Ban dau:\n");                  inMT(a, n, m);

    xoaHang(a, &n, m, 1);
    printf("Sau khi xoa hang 1:\n");       inMT(a, n, m);

    xoaCot(a, n, &m, 2);
    printf("Sau khi xoa cot 2:\n");        inMT(a, n, m);

    return 0;
}
```

💡 Tương tự chèn/xoá mảng 1 chiều (bài [06-05](../06-05-c-chen-va-xoa-phan-tu.md)), chỉ khác là phải dịch **cả một hàng/cột**.

⚠️ C không có tham chiếu, nên để hàm cập nhật được kích thước thì phải truyền **con trỏ** `int *n`, `int *m` và gọi `xoaHang(a, &n, m, 1)`. Nhớ viết `(*n)--` có ngoặc — `*n--` sẽ giảm con trỏ chứ không giảm giá trị.

### Bài 10.

```c
#include <stdio.h>

void chenHang(int a[][100], int *n, int m, int k, const int hangMoi[]) {
    if (k < 0 || k > *n) return;

    // Dich cac hang tu k tro di XUONG DUOI (duyet tu cuoi)
    for (int i = *n; i > k; i--)
        for (int j = 0; j < m; j++)
            a[i][j] = a[i - 1][j];

    for (int j = 0; j < m; j++) a[k][j] = hangMoi[j];
    (*n)++;
}

int main() {
    int a[100][100] = {{1,2,3}, {4,5,6}, {7,8,9}};
    int n = 3, m = 3;
    int hangMoi[3] = {99, 98, 97};

    chenHang(a, &n, m, 1, hangMoi);

    printf("Sau khi chen hang tai vi tri 1:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

Output:

```
Sau khi chen hang tai vi tri 1:
    1    2    3
   99   98   97
    4    5    6
    7    8    9
```

⚠️ **Duyệt từ cuối về đầu** khi dịch xuống — nếu duyệt xuôi sẽ ghi đè mất dữ liệu.

### Bài 11.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int a[100][100], n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) scanf("%d", &a[i][j]);

    bool tamGiacTren = true, tamGiacDuoi = true;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (j < i && a[i][j] != 0) tamGiacTren = false;   // phia duoi phai = 0
            if (j > i && a[i][j] != 0) tamGiacDuoi = false;   // phia tren phai = 0
        }

    if (tamGiacTren && tamGiacDuoi) printf("Ma tran DUONG CHEO\n");
    else if (tamGiacTren)           printf("Ma tran TAM GIAC TREN\n");
    else if (tamGiacDuoi)           printf("Ma tran TAM GIAC DUOI\n");
    else                            printf("Khong phai ma tran tam giac\n");
    return 0;
}
```

**Định nghĩa:**

```
Tam giac TREN:     Tam giac DUOI:    Duong cheo:
1 2 3              1 0 0             1 0 0
0 5 6              4 5 0             0 5 0
0 0 9              7 8 9             0 0 9
(duoi cheo = 0)    (tren cheo = 0)   (ca hai = 0)
```

💡 **Ứng dụng:** ma trận tam giác giải hệ phương trình tuyến tính rất nhanh (phương pháp thế ngược), và là kết quả của phép khử Gauss.

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

int a[100][100];
bool daTham[100][100];
int n, m;

// 4 huong: xuong, len, phai, trai
int dr[] = {1, -1, 0, 0};
int dc[] = {0, 0, 1, -1};

void dfs(int r, int c) {
    if (r < 0 || r >= n || c < 0 || c >= m) return;   // ngoai bien
    if (daTham[r][c] || a[r][c] == 0) return;         // da tham hoac la o trong

    daTham[r][c] = true;

    for (int k = 0; k < 4; k++) {
        dfs(r + dr[k], c + dc[k]);
    }
}

int main() {
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);
    printf("Nhap ma tran 0/1:\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int soVung = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 1 && !daTham[i][j]) {
                soVung++;
                dfs(i, j);              // "to mau" toan bo vung nay
            }
        }

    printf("So vung lien thong = %d\n", soVung);
    return 0;
}
```

Ví dụ với ma trận:

```
1 1 0 0
1 0 0 1
0 0 1 1
0 0 1 0
```

→ **2 vùng** liên thông.

**Thuật toán "loang" (flood fill) bằng DFS:**
1. Duyệt mọi ô
2. Gặp ô `1` chưa thăm → tăng số vùng, rồi gọi DFS "tô màu" toàn bộ vùng nối liền với nó
3. Mỗi lần gọi DFS từ vòng lặp chính = một vùng mới

💡 **Mảng `dr`/`dc`** là kỹ thuật chuẩn để duyệt 4 (hoặc 8) hướng gọn gàng, thay vì viết 4 lệnh `dfs` riêng.

Muốn xét 8 hướng (kể cả chéo):

```c
int dr[] = {-1,-1,-1, 0, 0, 1, 1, 1};
int dc[] = {-1, 0, 1,-1, 1,-1, 0, 1};
```

⚠️ Với ma trận lớn (> 1000×1000), DFS đệ quy có thể tràn stack — khi đó dùng BFS với một hàng đợi (tự cài bằng mảng + 2 chỉ số đầu/cuối).

### Bài 13.

```c
#include <stdio.h>
#include <limits.h>

int main() {
    int a[55][55], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    // Tinh tong tien to 2 chieu: pre[i][j] = tong hinh chu nhat (0,0)-(i-1,j-1)
    long long pre[55][55] = {0};
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= m; j++)
            pre[i][j] = a[i-1][j-1] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1];

    long long tongMax = LLONG_MIN;
    int r1 = 0, c1 = 0, r2 = 0, c2 = 0;

    // Duyet moi hinh chu nhat con
    for (int i1 = 1; i1 <= n; i1++)
    for (int j1 = 1; j1 <= m; j1++)
    for (int i2 = i1; i2 <= n; i2++)
    for (int j2 = j1; j2 <= m; j2++) {
        long long tong = pre[i2][j2] - pre[i1-1][j2] - pre[i2][j1-1] + pre[i1-1][j1-1];
        if (tong > tongMax) {
            tongMax = tong;
            r1 = i1-1; c1 = j1-1; r2 = i2-1; c2 = j2-1;
        }
    }

    printf("Tong lon nhat = %lld\n", tongMax);
    printf("Hinh chu nhat tu (%d,%d) den (%d,%d)\n", r1, c1, r2, c2);
    return 0;
}
```

**Tổng tiền tố 2 chiều — công thức bao hàm-loại trừ:**

```
Xay dung:
pre[i][j] = a[i-1][j-1] + pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1]
                                                       ^^^^^^^^^^^
                                        tru vung bi cong 2 lan

Truy van tong hinh chu nhat (i1,j1)-(i2,j2):
tong = pre[i2][j2] - pre[i1-1][j2] - pre[i2][j1-1] + pre[i1-1][j1-1]
```

**Độ phức tạp:** O(n²m²) để duyệt mọi hình chữ nhật, mỗi cái O(1) nhờ prefix sum. Với `n = m = 50` là ~6 triệu bước — chấp nhận được.

💡 `LLONG_MIN` nằm trong `<limits.h>`. Khởi tạo `= {0}` đưa toàn bộ mảng về 0 (dạng `= {}` rỗng chỉ hợp lệ từ chuẩn C23, với C11 hãy viết `= {0}`).

💡 Có thuật toán O(n²m) dùng Kadane (bài [06-02](../06-02-c-bai-tap-mang-1-chieu-p1.md) bài 6) cho từng cặp hàng.

### Bài 14.

```c
#include <stdio.h>

long long minLL(long long x, long long y) { return x < y ? x : y; }

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    static long long dp[100][100];

    // Quy hoach dong: dp[i][j] = tong nho nhat de den o (i,j)
    dp[0][0] = a[0][0];

    for (int j = 1; j < m; j++) dp[0][j] = dp[0][j-1] + a[0][j];   // hang dau: chi di phai
    for (int i = 1; i < n; i++) dp[i][0] = dp[i-1][0] + a[i][0];   // cot dau: chi di xuong

    for (int i = 1; i < n; i++)
        for (int j = 1; j < m; j++)
            dp[i][j] = minLL(dp[i-1][j], dp[i][j-1]) + a[i][j];

    printf("Tong nho nhat = %lld\n", dp[n-1][m-1]);

    // Truy vet duong di (tu cuoi ve dau, luu vao mang roi in nguoc)
    int hang[200], cot[200], k = 0;
    int i = n - 1, j = m - 1;
    while (i > 0 || j > 0) {
        hang[k] = i; cot[k] = j; k++;
        if (i == 0)                        j--;
        else if (j == 0)                   i--;
        else if (dp[i-1][j] < dp[i][j-1])  i--;
        else                               j--;
    }
    printf("Duong di: (0,0)");
    for (int t = k - 1; t >= 0; t--) printf(" -> (%d,%d)", hang[t], cot[t]);
    printf("\n");
    return 0;
}
```

Ví dụ với ma trận:

```
1 3 1
1 5 1
4 2 1
```

Output:

```
Tong nho nhat = 7
Duong di: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2)
```

→ Tổng nhỏ nhất = **7** theo đường 1 → 3 → 1 → 1 → 1.

**Quy hoạch động (dynamic programming):** để đến ô `(i,j)`, ta chỉ có thể đến từ ô **trên** `(i-1,j)` hoặc ô **trái** `(i,j-1)`. Chọn cái nhỏ hơn.

💡 C không có `min` sẵn cho số nguyên và không có kiểu `string` để nối chuỗi, nên ta tự viết `minLL` và lưu toạ độ đường đi vào 2 mảng `hang[]`, `cot[]` rồi in ngược.

Độ phức tạp **O(n×m)** — tối ưu.

### Bài 15.

```c
#include <stdio.h>

int main() {
    int n, m;
    printf("Nhap kich thuoc bang: ");
    scanf("%d %d", &n, &m);

    int bom[50][50];
    printf("Nhap ma tran 0/1 (1 = co min):\n");
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &bom[i][j]);

    int dem[50][50] = {0};

    // 8 huong xung quanh
    int dr[] = {-1,-1,-1, 0, 0, 1, 1, 1};
    int dc[] = {-1, 0, 1,-1, 1,-1, 0, 1};

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (bom[i][j] == 1) { dem[i][j] = -1; continue; }   // -1 = co min

            for (int k = 0; k < 8; k++) {
                int r = i + dr[k], c = j + dc[k];
                if (r >= 0 && r < n && c >= 0 && c < m && bom[r][c] == 1)
                    dem[i][j]++;
            }
        }

    printf("\nBang do min:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dem[i][j] == -1)     printf("%3s", "*");
            else if (dem[i][j] == 0) printf("%3s", ".");
            else                     printf("%3d", dem[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

Ví dụ với bảng 4×4:

```
Input:
1 0 0 0
0 0 1 0
0 0 0 0
0 1 0 0

Output:
  *  2  1  1
  1  2  *  1
  1  2  2  1
  1  *  1  .
```

**Kỹ thuật cốt lõi:** với mỗi ô không có mìn, đếm số mìn trong 8 ô xung quanh.

⚠️ **Luôn kiểm tra biên** `r >= 0 && r < n && c >= 0 && c < m` trước khi truy cập — các ô ở viền không có đủ 8 hàng xóm.

💡 Cách viết gọn hơn không cần mảng `dr`/`dc`:

```c
for (int dr = -1; dr <= 1; dr++)
    for (int dc = -1; dc <= 1; dc++) {
        if (dr == 0 && dc == 0) continue;     // bo qua chinh no
        int r = i + dr, c = j + dc;
        if (r >= 0 && r < n && c >= 0 && c < m && bom[r][c]) dem[i][j]++;
    }
```
