# Lời giải — [C]. Ma Trận Xoắn Ốc

[← Quay lại bài học](../08-05-c-ma-tran-xoan-oc.md)

> **Ý tưởng chung:** giữ 4 biên `tren`, `duoi`, `trai`, `phai`. Mỗi vòng đi 4 cạnh rồi thu hẹp biên vào trong.

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    int a[100][100], n, m;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;

    printf("\nXoan oc (cung chieu kim dong ho): ");
    while (tren <= duoi && trai <= phai) {
        // (1) Sang PHAI tren hang `tren`
        for (int j = trai; j <= phai; j++) printf("%d ", a[tren][j]);
        tren++;

        // (2) XUONG tren cot `phai`
        for (int i = tren; i <= duoi; i++) printf("%d ", a[i][phai]);
        phai--;

        // (3) Sang TRAI tren hang `duoi` (neu con hang)
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) printf("%d ", a[duoi][j]);
            duoi--;
        }

        // (4) LEN tren cot `trai` (neu con cot)
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) printf("%d ", a[i][trai]);
            trai++;
        }
    }
    printf("\n");
    return 0;
}
```

Với ma trận 3×4:

```
 1  2  3  4
 5  6  7  8
 9 10 11 12
```

Output: `1 2 3 4 8 12 11 10 9 5 6 7`

**Sơ đồ đường đi:**

```
→ → → →
        ↓
↑ ← ← ← ↓
```

⚠️ **Hai câu `if` bảo vệ rất quan trọng.** Khi vòng trong chỉ còn **một hàng**, bước ③ sẽ in lại các phần tử đã in ở bước ①. Tương tự với một cột và bước ④.

Thử bỏ 2 câu `if` và chạy với ma trận 1×5 — bạn sẽ thấy phần tử bị in 2 lần.

### Bài 2.

```c
#include <stdio.h>

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;

    printf("\nXoan oc (NGUOC chieu kim dong ho): ");
    while (tren <= duoi && trai <= phai) {
        // (1) XUONG tren cot `trai`
        for (int i = tren; i <= duoi; i++) printf("%d ", a[i][trai]);
        trai++;

        // (2) Sang PHAI tren hang `duoi`
        for (int j = trai; j <= phai; j++) printf("%d ", a[duoi][j]);
        duoi--;

        // (3) LEN tren cot `phai`
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) printf("%d ", a[i][phai]);
            phai--;
        }

        // (4) Sang TRAI tren hang `tren`
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) printf("%d ", a[tren][j]);
            tren++;
        }
    }
    printf("\n");
    return 0;
}
```

Với ma trận 3×4 ở trên: `1 5 9 10 11 12 8 4 3 2 6 7`

**Sơ đồ:**

```
↓ ← ← ←
↓     ↑
→ → → ↑
```

### Bài 3.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[100][100] = {0};
    int tren = 0, duoi = n - 1, trai = 0, phai = n - 1;
    int so = 1;

    while (tren <= duoi && trai <= phai) {
        for (int j = trai; j <= phai; j++) a[tren][j] = so++;
        tren++;

        for (int i = tren; i <= duoi; i++) a[i][phai] = so++;
        phai--;

        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) a[duoi][j] = so++;
            duoi--;
        }

        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) a[i][trai] = so++;
            trai++;
        }
    }

    printf("\nMa tran xoan oc %dx%d:\n", n, n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

Với `n = 5`:

```
    1    2    3    4    5
   16   17   18   19    6
   15   24   25   20    7
   14   23   22   21    8
   13   12   11   10    9
```

💡 **Code y hệt bài 1**, chỉ thay `printf("%d ", a[...])` bằng `a[...] = so++`.

### Bài 4.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    int a[100][100] = {0};
    int tren = 0, duoi = n - 1, trai = 0, phai = n - 1;
    int so = n * n;                       // BAT DAU TU SO LON NHAT

    while (tren <= duoi && trai <= phai) {
        for (int j = trai; j <= phai; j++) a[tren][j] = so--;
        tren++;
        for (int i = tren; i <= duoi; i++) a[i][phai] = so--;
        phai--;
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) a[duoi][j] = so--;
            duoi--;
        }
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) a[i][trai] = so--;
            trai++;
        }
    }

    printf("\nXoan oc tu TRONG RA NGOAI:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

Với `n = 4`:

```
   16   15   14   13
    5    4    3   12
    6    1    2   11
    7    8    9   10
```

💡 **Mẹo đơn giản:** điền như bình thường nhưng **đếm ngược** từ `n²` về 1.

### Bài 5.

```c
#include <stdio.h>

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("\nZigzag: ");
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {                          // hang CHAN: trai -> phai
            for (int j = 0; j < m; j++) printf("%d ", a[i][j]);
        } else {                                   // hang LE: phai -> trai
            for (int j = m - 1; j >= 0; j--) printf("%d ", a[i][j]);
        }
    }
    printf("\n");
    return 0;
}
```

Với ma trận 3×4:

```
 1  2  3  4
 5  6  7  8
 9 10 11 12
```

Output: `1 2 3 4 8 7 6 5 9 10 11 12`

**Sơ đồ:**

```
→ → → →
        ↓
← ← ← ←
↓
→ → → →
```

💡 **Ứng dụng thực tế:** đây là cách máy in phun và máy CNC di chuyển đầu in — tiết kiệm quãng đường so với quay về đầu dòng mỗi lần.

### Bài 6.

```c
#include <stdio.h>

int main() {
    int a[100][100], n, m;
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("\nTheo duong cheo (i + j tang dan):\n");
    for (int s = 0; s <= n + m - 2; s++) {         // s = i + j
        printf("  Cheo %d: ", s);
        for (int i = 0; i < n; i++) {
            int j = s - i;
            if (j >= 0 && j < m) printf("%d ", a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

Với ma trận 3×3:

```
1 2 3
4 5 6
7 8 9
```

Output:

```
  Cheo 0: 1 
  Cheo 1: 2 4 
  Cheo 2: 3 5 7 
  Cheo 3: 6 8 
  Cheo 4: 9 
```

**Ý tưởng:** tất cả phần tử trên cùng một đường chéo (hướng ↗) có **tổng `i + j` bằng nhau**.

💡 Đây chính là thứ tự quét **zigzag của JPEG** (kết hợp với đảo chiều xen kẽ) — dùng để nén ảnh hiệu quả.

### Bài 7.

```c
#include <stdio.h>

int main() {
    int n, m;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);

    static int day[10000];
    printf("Nhap %d so: ", n * m);
    for (int i = 0; i < n * m; i++) scanf("%d", &day[i]);

    int a[100][100] = {0};
    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;
    int k = 0;

    while (tren <= duoi && trai <= phai) {
        for (int j = trai; j <= phai; j++) a[tren][j] = day[k++];
        tren++;
        for (int i = tren; i <= duoi; i++) a[i][phai] = day[k++];
        phai--;
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) a[duoi][j] = day[k++];
            duoi--;
        }
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) a[i][trai] = day[k++];
            trai++;
        }
    }

    printf("\nMa tran ket qua:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

💡 Đây là **phép biến đổi ngược** của bài 1. Kết hợp cả hai, bạn có thể "mã hoá" một dãy số thành ma trận và giải mã ngược lại.

💡 Dãy được lưu trong mảng tĩnh `static int day[10000]` (đủ cho ma trận `100×100`).

### Bài 8.

```c
#include <stdio.h>

int main() {
    int n = 4, k;
    int a[100][100] = {
        {1,2,3,4}, {5,6,7,8}, {9,10,11,12}, {13,14,15,16}
    };
    int m = 4;

    printf("Nhap so buoc dich k: ");
    scanf("%d", &k);

    // (1) Doc ma tran theo xoan oc vao mang 1 chieu, luu kem vi tri (hang, cot)
    int day[10000], viR[10000], viC[10000];
    int tong = 0;
    int tren = 0, duoi = n-1, trai = 0, phai = m-1;

    while (tren <= duoi && trai <= phai) {
        for (int j = trai; j <= phai; j++) {
            day[tong] = a[tren][j]; viR[tong] = tren; viC[tong] = j; tong++;
        }
        tren++;
        for (int i = tren; i <= duoi; i++) {
            day[tong] = a[i][phai]; viR[tong] = i; viC[tong] = phai; tong++;
        }
        phai--;
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) {
                day[tong] = a[duoi][j]; viR[tong] = duoi; viC[tong] = j; tong++;
            }
            duoi--;
        }
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) {
                day[tong] = a[i][trai]; viR[tong] = i; viC[tong] = trai; tong++;
            }
            trai++;
        }
    }

    // (2) Dich vong mang 1 chieu
    k = ((k % tong) + tong) % tong;

    // (3) Ghi nguoc lai vao ma tran
    for (int i = 0; i < tong; i++) {
        int t = (i + k) % tong;
        a[viR[t]][viC[t]] = day[i];
    }

    printf("\nSau khi dich %d buoc theo xoan oc:\n", k);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

**Kỹ thuật:** thay vì cố dịch trực tiếp trên ma trận (rất rối), ta:
1. "Trải phẳng" đường xoắn ốc thành mảng 1 chiều + lưu kèm vị trí (2 mảng song song `viR`, `viC`)
2. Dịch vòng mảng 1 chiều (dễ)
3. Ghi ngược lại vào ma trận theo danh sách vị trí đã lưu

💡 Đây là mẫu tư duy chung: **đưa bài toán khó về bài toán dễ đã biết cách giải.**

⚠️ `k = ((k % tong) + tong) % tong` đưa `k` âm về dương — trong C, `%` với số âm cho kết quả âm.

### Bài 9.

```c
#include <stdio.h>

int minInt(int x, int y) { return x < y ? x : y; }

int main() {
    int n, m;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);

    int soVong = (minInt(n, m) + 1) / 2;

    printf("Ma tran %dx%d co %d vong xoan\n", n, m, soVong);

    // Kiem chung bang cach dem thuc te
    int dem = 0;
    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;
    while (tren <= duoi && trai <= phai) {
        dem++;
        tren++; duoi--; trai++; phai--;
    }
    printf("Dem thuc te: %d vong\n", dem);
    return 0;
}
```

**Công thức:** `soVong = ⌈min(n, m) / 2⌉ = (min(n,m) + 1) / 2`

| n × m | min | Số vòng |
|---|---|---|
| 3 × 3 | 3 | 2 |
| 4 × 4 | 4 | 2 |
| 5 × 5 | 5 | 3 |
| 3 × 7 | 3 | 2 |
| 1 × 10 | 1 | 1 |

**Lý do:** mỗi vòng "ăn" 1 hàng ở trên, 1 hàng ở dưới (và 1 cột trái, 1 cột phải). Nên số vòng bị giới hạn bởi chiều **nhỏ hơn**, chia đôi và làm tròn lên.

💡 C không có hàm `min` cho số nguyên, ta tự viết `minInt`.

### Bài 10.

```c
#include <stdio.h>

int minInt(int x, int y) { return x < y ? x : y; }

int main() {
    int a[100][100], n, m, k;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("Nhap vong can in (bat dau tu 0): ");
    scanf("%d", &k);

    int soVong = (minInt(n, m) + 1) / 2;
    if (k < 0 || k >= soVong) {
        printf("Vong khong hop le! (co %d vong)\n", soVong);
        return 1;
    }

    // Bien cua vong thu k
    int tren = k, duoi = n - 1 - k, trai = k, phai = m - 1 - k;

    printf("\nVong %d: ", k);
    for (int j = trai; j <= phai; j++) printf("%d ", a[tren][j]);
    for (int i = tren + 1; i <= duoi; i++) printf("%d ", a[i][phai]);
    if (tren < duoi)
        for (int j = phai - 1; j >= trai; j--) printf("%d ", a[duoi][j]);
    if (trai < phai)
        for (int i = duoi - 1; i > tren; i--) printf("%d ", a[i][trai]);
    printf("\n");
    return 0;
}
```

💡 **Công thức biên của vòng thứ `k`:**

```
tren = k
duoi = n - 1 - k
trai = k
phai = m - 1 - k
```

Nhờ công thức này, ta truy cập trực tiếp vòng bất kỳ mà không cần lặp từ vòng 0.

### Bài 11.

```c
#include <stdio.h>

int a[100][100];
int n, m;

void xoanOc(int tren, int duoi, int trai, int phai) {
    if (tren > duoi || trai > phai) return;          // DIEU KIEN DUNG

    for (int j = trai; j <= phai; j++) printf("%5d", a[tren][j]);
    for (int i = tren + 1; i <= duoi; i++) printf("%5d", a[i][phai]);

    if (tren < duoi)
        for (int j = phai - 1; j >= trai; j--) printf("%5d", a[duoi][j]);
    if (trai < phai)
        for (int i = duoi - 1; i > tren; i--) printf("%5d", a[i][trai]);

    // DE QUY voi vong trong hon
    xoanOc(tren + 1, duoi - 1, trai + 1, phai - 1);
}

int main() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) scanf("%d", &a[i][j]);

    printf("\nXoan oc (de quy):\n");
    xoanOc(0, n - 1, 0, m - 1);
    printf("\n");
    return 0;
}
```

💡 Bản đệ quy **ngắn gọn và tự nhiên hơn**: mỗi lời gọi xử lý đúng một vòng, rồi giao phần còn lại cho lời gọi kế tiếp.

Độ sâu đệ quy chỉ `O(min(n,m)/2)` nên không lo tràn stack.

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

int main() {
    int n, m;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);

    int a[100][100] = {0};
    bool daTham[100][100] = {{false}};

    // 4 huong theo thu tu: PHAI, XUONG, TRAI, LEN
    int dr[] = {0, 1, 0, -1};
    int dc[] = {1, 0, -1, 0};

    int r = 0, c = 0, huong = 0;

    for (int so = 1; so <= n * m; so++) {
        a[r][c] = so;
        daTham[r][c] = true;

        // Thu di tiep theo huong hien tai
        int r2 = r + dr[huong];
        int c2 = c + dc[huong];

        // Neu ra ngoai bien hoac o da tham -> DOI HUONG
        if (r2 < 0 || r2 >= n || c2 < 0 || c2 >= m || daTham[r2][c2]) {
            huong = (huong + 1) % 4;             // xoay sang huong ke tiep
            r2 = r + dr[huong];
            c2 = c + dc[huong];
        }

        r = r2; c = c2;
    }

    printf("\nMa tran xoan oc (mo phong buoc di):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

**So sánh 2 cách tiếp cận:**

| | Quản lý 4 biên | Mô phỏng bước đi |
|---|---|---|
| Code | Dài hơn, 4 vòng lặp | Ngắn hơn, 1 vòng lặp |
| Bộ nhớ phụ | Không cần | Cần mảng `daTham` |
| Dễ hiểu | Trung bình | ✅ Rất trực quan |
| Mở rộng (8 hướng, hình khác) | Khó | ✅ Dễ |

💡 Cách mô phỏng dễ mở rộng hơn — chỉ cần đổi mảng `dr`/`dc` là được hình dạng khác.

⚠️ Sau khi điền số cuối cùng, `(r, c)` có thể bước ra một ô "ảo" nhưng vòng lặp đã kết thúc nên không ghi vào đó. Nếu sửa code, đừng truy cập `a[r][c]` sau vòng lặp.

### Bài 13.

```c
#include <stdio.h>

typedef struct {
    int i, j;
} ViTri;

// Tim vi tri cua so k trong ma tran xoan oc n x n (dien tu 1)
ViTri timViTri(int n, int k) {
    ViTri khongCo = {-1, -1};
    if (k < 1 || k > n * n) return khongCo;

    int tren = 0, duoi = n - 1, trai = 0, phai = n - 1;
    int so = 1;

    while (tren <= duoi && trai <= phai) {
        // Canh tren
        int doDai = phai - trai + 1;
        if (k < so + doDai) return (ViTri){tren, trai + (k - so)};
        so += doDai;
        tren++;

        // Canh phai
        doDai = duoi - tren + 1;
        if (doDai > 0) {
            if (k < so + doDai) return (ViTri){tren + (k - so), phai};
            so += doDai;
        }
        phai--;

        // Canh duoi
        if (tren <= duoi) {
            doDai = phai - trai + 1;
            if (doDai > 0) {
                if (k < so + doDai) return (ViTri){duoi, phai - (k - so)};
                so += doDai;
            }
            duoi--;
        }

        // Canh trai
        if (trai <= phai) {
            doDai = duoi - tren + 1;
            if (doDai > 0) {
                if (k < so + doDai) return (ViTri){duoi - (k - so), trai};
                so += doDai;
            }
            trai++;
        }
    }
    return khongCo;
}

int main() {
    int n = 5;
    int ds[] = {1, 5, 6, 13, 25};
    for (int t = 0; t < 5; t++) {
        ViTri p = timViTri(n, ds[t]);
        printf("So %d nam tai (%d, %d)\n", ds[t], p.i, p.j);
    }
    return 0;
}
```

Với `n = 5` (ma trận xoắn ốc ở bài 3):

```
So 1 nam tai (0, 0)
So 5 nam tai (0, 4)
So 6 nam tai (1, 4)
So 13 nam tai (4, 0)
So 25 nam tai (2, 2)
```

**Ý tưởng:** thay vì điền cả ma trận rồi tìm (O(n²)), ta **nhảy qua từng cạnh** — mỗi cạnh biết trước độ dài, nên chỉ cần kiểm tra `k` có rơi vào cạnh này không.

**Độ phức tạp: O(n)** thay vì O(n²), và **không tốn bộ nhớ** cho ma trận.

💡 Hàm C chỉ trả về được **một** giá trị, nên ta gói 2 toạ độ vào `struct ViTri`. Cú pháp `(ViTri){x, y}` (compound literal của C99) tạo nhanh một struct tạm để trả về.

### Bài 14.

```c
#include <stdio.h>

int minInt(int x, int y) { return x < y ? x : y; }

int main() {
    int n, m;
    printf("Nhap so hang, cot: ");
    scanf("%d %d", &n, &m);

    int a[100][100] = {0};
    int so = 1;
    int soVong = (minInt(n, m) + 1) / 2;

    for (int k = 0; k < soVong; k++) {
        int tren = k, duoi = n - 1 - k, trai = k, phai = m - 1 - k;

        if (k % 2 == 0) {
            // Vong CHAN: cung chieu kim dong ho
            for (int j = trai; j <= phai; j++) a[tren][j] = so++;
            for (int i = tren + 1; i <= duoi; i++) a[i][phai] = so++;
            if (tren < duoi) for (int j = phai - 1; j >= trai; j--) a[duoi][j] = so++;
            if (trai < phai) for (int i = duoi - 1; i > tren; i--) a[i][trai] = so++;
        } else {
            // Vong LE: NGUOC chieu kim dong ho
            for (int i = tren; i <= duoi; i++) a[i][trai] = so++;
            for (int j = trai + 1; j <= phai; j++) a[duoi][j] = so++;
            if (trai < phai) for (int i = duoi - 1; i >= tren; i--) a[i][phai] = so++;
            if (tren < duoi) for (int j = phai - 1; j > trai; j--) a[tren][j] = so++;
        }
    }

    printf("\nMa tran boustrophedon (moi vong doi chieu):\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) printf("%5d", a[i][j]);
        printf("\n");
    }
    return 0;
}
```

Với `n = m = 5`:

```
    1    2    3    4    5
   16   17   24   23    6
   15   18   25   22    7
   14   19   20   21    8
   13   12   11   10    9
```

💡 **"Boustrophedon"** là từ Hy Lạp cổ nghĩa là "như đường cày của con bò" — đi hết một luống rồi quay lại luống kế. Một số văn bản Hy Lạp cổ được viết theo kiểu này.

### Bài 15.

```c
#include <stdio.h>

int main() {
    int n;
    printf("Nhap kich thuoc (nen le, vd 21): ");
    scanf("%d", &n);

    static char hinh[101][101];

    // (1) Tao ma tran xoan oc dang so
    static int a[101][101];
    int tren = 0, duoi = n - 1, trai = 0, phai = n - 1;
    int so = 0;

    while (tren <= duoi && trai <= phai) {
        for (int j = trai; j <= phai; j++) a[tren][j] = so++;
        tren++;
        for (int i = tren; i <= duoi; i++) a[i][phai] = so++;
        phai--;
        if (tren <= duoi) { for (int j = phai; j >= trai; j--) a[duoi][j] = so++; duoi--; }
        if (trai <= phai) { for (int i = duoi; i >= tren; i--) a[i][trai] = so++; trai++; }
    }

    // (2) Dua so ve ky tu: xen ke * va khoang trang theo chu ky
    const int CHU_KY = 6;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            hinh[i][j] = (a[i][j] % CHU_KY < CHU_KY / 2) ? '*' : ' ';

    printf("\nHoa van xoan oc:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%c%c", hinh[i][j], hinh[i][j]);  // in doi de vuong hon
        printf("\n");
    }

    // (3) Bien the: ve xoan oc bang duong lien tuc
    printf("\nDuong xoan oc lien tuc:\n");
    static int b[101][101];
    tren = 0; duoi = n - 1; trai = 0; phai = n - 1;
    int vong = 0;

    while (tren <= duoi && trai <= phai) {
        if (vong % 2 == 0) {                 // chi to mau cac vong chan
            for (int j = trai; j <= phai; j++) b[tren][j] = 1;
            for (int i = tren; i <= duoi; i++) b[i][phai] = 1;
            for (int j = phai; j >= trai; j--) b[duoi][j] = 1;
            for (int i = duoi; i >= tren + 1; i--) b[i][trai] = 1;
            b[tren][trai] = 0;                // ho mot lo de tao duong xoan
        }
        tren++; duoi--; trai++; phai--;
        vong++;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("%s", b[i][j] ? "##" : "  ");
        printf("\n");
    }
    return 0;
}
```

Ví dụ output (rút gọn, `n = 15`):

```
Duong xoan oc lien tuc:
  ############################
##                          ##
##    ####################  ##
##  ##                  ##  ##
##  ##    ############  ##  ##
##  ##  ##          ##  ##  ##
##  ##  ##    ####  ##  ##  ##
  ...
```

💡 **Kỹ thuật chung để vẽ hoa văn:** tính một **giá trị số** cho mỗi ô (ở đây là thứ tự xoắn ốc), rồi ánh xạ giá trị đó thành ký tự theo một quy tắc. Đổi quy tắc ánh xạ là được hoa văn khác.

Một số ý tưởng ánh xạ khác:
```c
hinh[i][j] = (a[i][j] % 2) ? '#' : '.';                  // soc xen ke
hinh[i][j] = "....:::;;;***###@@@"[a[i][j] * 18 / (n*n)]; // do dam tang dan
hinh[i][j] = (int)sqrt(a[i][j]) % 2 ? '*' : ' ';          // vong tron dong tam (can <math.h>, -lm)
```

**In mỗi ký tự 2 lần** (`printf("%c%c", hinh[i][j], hinh[i][j])`) vì ký tự trong terminal cao gấp đôi chiều rộng — làm vậy hình sẽ vuông hơn.

💡 Các mảng `101×101` được khai báo `static` để tự khởi tạo toàn 0 và không chiếm stack.
