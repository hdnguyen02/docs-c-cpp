# Lời giải — [C]. Bài Tập Đệ Quy

[← Quay lại bài học](../05-07-c-bai-tap-de-quy.md)

---

### Bài 1.

```c
#include <stdio.h>

double tongNghichDao(int n) {
    if (n <= 0) return 0;
    return 1.0 / n + tongNghichDao(n - 1);      // chu y 1.0 chu khong phai 1
}

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);
    printf("S = %.10f\n", tongNghichDao(n));
    return 0;
}
```

⚠️ Viết `1 / n` (cả hai đều `int`) sẽ cho 0 với mọi `n > 1`. Phải là `1.0 / n`.

### Bài 2.

```c
#include <stdio.h>

long long tongBinhPhuong(int n) {
    if (n <= 0) return 0;
    return (long long)n * n + tongBinhPhuong(n - 1);
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("S = %lld\n", tongBinhPhuong(n));
    // Kiem chung bang cong thuc: n(n+1)(2n+1)/6
    printf("Cong thuc: %lld\n", (long long)n * (n + 1) * (2 * n + 1) / 6);
    return 0;
}
```

### Bài 3.

```c
#include <stdio.h>
#include <stdlib.h>

int demChuSoChan(int n) {
    n = abs(n);
    if (n == 0) return 0;
    int cuoi = n % 10;
    return (cuoi % 2 == 0 ? 1 : 0) + demChuSoChan(n / 10);
}

int main(void) {
    int n = 246813;
    printf("%d co %d chu so chan\n", n, demChuSoChan(n));   // 4
    return 0;
}
```

⚠️ Với `n = 0`, hàm trả về 0 — nhưng số 0 có 1 chữ số chẵn. Nếu cần xử lý đúng, thêm:

```c
int demChuSoChan(int n) {
    n = abs(n);
    if (n < 10) return (n % 2 == 0 ? 1 : 0);
    return (n % 10 % 2 == 0 ? 1 : 0) + demChuSoChan(n / 10);
}
```

### Bài 4.

```c
#include <stdio.h>
#include <stdbool.h>

// Ham de quy voi tham so phu i (uoc dang thu)
bool nguyenToDeQuy(int n, int i) {
    if (n < 2) return false;
    if ((long long)i * i > n) return true;      // da thu het -> la nguyen to
    if (n % i == 0) return false;               // tim thay uoc -> khong phai
    return nguyenToDeQuy(n, i + 1);
}

// Ham vo cho nguoi dung goi
bool laNguyenTo(int n) {
    return nguyenToDeQuy(n, 2);
}

int main(void) {
    int ds[] = {1, 2, 9, 17, 100, 97};
    for (int k = 0; k < 6; k++) {
        printf("%d -> %s\n", ds[k], laNguyenTo(ds[k]) ? "nguyen to" : "khong");
    }
    return 0;
}
```

💡 **Mẫu "hàm vỏ + hàm đệ quy có tham số phụ"** rất thường gặp: người dùng gọi `laNguyenTo(97)` đơn giản, còn tham số `i` là chi tiết nội bộ.

⚠️ C **không cho phép hai hàm trùng tên** (không có nạp chồng hàm), nên hàm đệ quy bên trong phải đặt tên khác (`nguyenToDeQuy`).

⚠️ Độ sâu đệ quy là O(√n) — với `n = 10¹⁸` cần 10⁹ tầng → tràn stack. Bài này nên dùng vòng lặp trong thực tế.

### Bài 5.

```c
#include <stdio.h>

long long tongMang(int a[], int n) {
    if (n <= 0) return 0;
    return a[n - 1] + tongMang(a, n - 1);       // cong phan tu CUOI + tong phan con lai
}

int main(void) {
    int a[] = {3, 7, -2, 8, 5};
    printf("Tong = %lld\n", tongMang(a, 5));   // 21
    return 0;
}
```

### Bài 6.

```c
#include <stdio.h>

int timTuViTri(int a[], int n, int x, int i) {
    if (i >= n) return -1;                  // het mang -> khong tim thay
    if (a[i] == x) return i;                // tim thay
    return timTuViTri(a, n, x, i + 1);      // xet phan tu ke tiep
}

// Ham vo: nguoi dung khong phai truyen tham so phu i
int timKiem(int a[], int n, int x) {
    return timTuViTri(a, n, x, 0);
}

int main(void) {
    int a[] = {5, 3, 8, 3, 1};
    printf("Tim 8: vi tri %d\n", timKiem(a, 5, 8));    // 2
    printf("Tim 3: vi tri %d\n", timKiem(a, 5, 3));    // 1 (dau tien)
    printf("Tim 9: vi tri %d\n", timKiem(a, 5, 9));    // -1
    return 0;
}
```

💡 C **không có đối số mặc định**, nên để người dùng không phải truyền tham số phụ `i`, ta viết thêm một **hàm vỏ** `timKiem` gọi `timTuViTri(..., 0)`.

### Bài 7.

```c
#include <stdio.h>

long long toHop(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;                    // C(n,0) = C(n,n) = 1
    return toHop(n - 1, k - 1) + toHop(n - 1, k);      // cong thuc Pascal
}

int main(void) {
    printf("C(5,2)  = %lld\n", toHop(5, 2));    // 10
    printf("C(10,5) = %lld\n", toHop(10, 5));   // 252
    return 0;
}
```

⚠️ **Rất chậm** — giống Fibonacci, cùng một `C(n,k)` bị tính lại nhiều lần. `C(30,15)` đã mất vài giây.

**Cải tiến bằng ghi nhớ:**

```c
long long bang[61][61];
bool daTinh[61][61];          // can #include <stdbool.h>

long long toHopMemo(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;
    if (daTinh[n][k]) return bang[n][k];
    daTinh[n][k] = true;
    bang[n][k] = toHopMemo(n - 1, k - 1) + toHopMemo(n - 1, k);
    return bang[n][k];
}
```

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

long long bang[35][35];
bool daTinh[35][35];

long long toHop(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;
    if (daTinh[n][k]) return bang[n][k];
    daTinh[n][k] = true;
    bang[n][k] = toHop(n - 1, k - 1) + toHop(n - 1, k);
    return bang[n][k];
}

int main(void) {
    int n;
    printf("Nhap so dong: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        // In dau cach de can giua
        printf("%*s", (n - i) * 3, "");
        for (int j = 0; j <= i; j++) {
            printf("%6lld", toHop(i, j));
        }
        printf("\n");
    }
    return 0;
}
```

Với `n = 6`:

```
                       1
                    1     1
                 1     2     1
              1     3     3     1
           1     4     6     4     1
        1     5    10    10     5     1
```

💡 `%6lld` in số chiếm đúng 6 ô (căn phải); `%*s` lấy độ rộng từ đối số đứng trước — ở đây dùng để in `(n - i) * 3` dấu cách.

💡 **Tam giác Pascal** — mỗi số bằng tổng 2 số ngay phía trên nó, chính là công thức `C(n,k) = C(n-1,k-1) + C(n-1,k)`.

### Bài 9.

```c
#include <stdio.h>

int day[20];
int demDay = 0;

void sinhNhiPhan(int viTri, int n) {
    if (viTri == n) {                       // da dien day du n vi tri
        demDay++;
        for (int i = 0; i < n; i++) printf("%d", day[i]);
        printf("\n");
        return;
    }

    for (int giaTri = 0; giaTri <= 1; giaTri++) {
        day[viTri] = giaTri;                // THU gia tri nay
        sinhNhiPhan(viTri + 1, n);          // sinh tiep phan con lai
    }
}

int main(void) {
    int n;
    printf("Nhap n (1..20): ");
    scanf("%d", &n);

    sinhNhiPhan(0, n);

    printf("Tong cong: %d day (= 2^%d)\n", demDay, n);
    return 0;
}
```

Với `n = 3`:

```
000
001
010
011
100
101
110
111
Tong cong: 8 day (= 2^3)
```

**Đây là mẫu SINH ĐỆ QUY cơ bản nhất:** tại mỗi vị trí, thử lần lượt mọi giá trị có thể, rồi đệ quy sang vị trí kế tiếp. Điều kiện dừng là khi đã điền đủ.

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

#define MAXN 10
int hv[MAXN];
bool daDung[MAXN + 1];
int demHoanVi = 0;

void sinhHoanVi(int viTri, int n) {
    if (viTri == n) {
        demHoanVi++;
        for (int i = 0; i < n; i++) printf("%d ", hv[i]);
        printf("\n");
        return;
    }

    for (int giaTri = 1; giaTri <= n; giaTri++) {
        if (daDung[giaTri]) continue;       // gia tri nay da dung roi

        hv[viTri] = giaTri;
        daDung[giaTri] = true;              // DANH DAU

        sinhHoanVi(viTri + 1, n);

        daDung[giaTri] = false;             // BO DANH DAU (quay lui!)
    }
}

int main(void) {
    int n;
    printf("Nhap n (1..10): ");
    scanf("%d", &n);

    sinhHoanVi(0, n);
    printf("Tong cong: %d hoan vi (= %d!)\n", demHoanVi, n);
    return 0;
}
```

Với `n = 3`:

```
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
Tong cong: 6 hoan vi (= 3!)
```

⚠️ **Dòng `daDung[giaTri] = false;` là linh hồn của thuật toán QUAY LUI (backtracking).** Sau khi thử xong một nhánh, phải **khôi phục trạng thái** để nhánh tiếp theo có thể dùng lại giá trị đó. Quên dòng này là thuật toán sai hoàn toàn.

💡 Thư viện chuẩn C không có hàm sinh hoán vị sẵn, nên cách đệ quy + quay lui ở trên chính là cách làm thông dụng.

### Bài 11.

```c
#include <stdio.h>

#define MAXN 91
long long bangNho[MAXN + 1];

long long demCach(int n) {
    if (n < 0) return 0;
    if (n == 0) return 1;                      // 1 cach: khong leo gi
    if (bangNho[n] != -1) return bangNho[n];

    // Buoc cuoi cung leo 1 bac HOAC 2 bac
    bangNho[n] = demCach(n - 1) + demCach(n - 2);
    return bangNho[n];
}

int main(void) {
    int n;
    printf("Nhap so bac thang (0..%d): ", MAXN);
    scanf("%d", &n);

    for (int i = 0; i <= MAXN; i++) bangNho[i] = -1;
    printf("So cach leo = %lld\n", demCach(n));
    return 0;
}
```

| n | Số cách |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 5 |
| 5 | 8 |
| 10 | 89 |

💡 **Đây chính là dãy Fibonacci!** Vì để lên bậc `n`, bạn phải đến từ bậc `n−1` (leo 1 bậc) hoặc bậc `n−2` (leo 2 bậc), nên `f(n) = f(n−1) + f(n−2)`.

### Bài 12.

```c
#include <stdio.h>

// Dem so cach viet n thanh tong cac so nguyen duong KHONG VUOT QUA max
// (khong phan biet thu tu, vd 4 = 3+1 = 2+2 = 2+1+1 = 1+1+1+1 = 4)
long long demPhanHoach(int n, int max) {
    if (n == 0) return 1;                   // da chia het -> 1 cach hop le
    if (n < 0 || max == 0) return 0;

    // Hoac DUNG so max, hoac KHONG dung so max nua
    return demPhanHoach(n - max, max) + demPhanHoach(n, max - 1);
}

int hienTai[100];      // cac so dang chon
int soPhanTu = 0;      // so luong so dang chon

void inPhanHoach(int n, int max) {
    if (n == 0) {
        for (int i = 0; i < soPhanTu; i++) {
            printf("%d", hienTai[i]);
            if (i + 1 < soPhanTu) printf(" + ");
        }
        printf("\n");
        return;
    }
    if (n < 0 || max == 0) return;

    hienTai[soPhanTu++] = max;          // them so max
    inPhanHoach(n - max, max);          // dung so max
    soPhanTu--;                         // quay lui

    inPhanHoach(n, max - 1);            // khong dung so max nua
}

int main(void) {
    int n;
    printf("Nhap n (1..100): ");
    scanf("%d", &n);

    printf("So cach phan hoach: %lld\n", demPhanHoach(n, n));
    printf("Chi tiet:\n");
    inPhanHoach(n, n);
    return 0;
}
```

Với `n = 5`:

```
So cach phan hoach: 7
Chi tiet:
5
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1
```

**Ý tưởng:** ràng buộc `max` (giá trị lớn nhất được dùng) đảm bảo mỗi phân hoạch chỉ được sinh **một lần** — vì các số luôn giảm dần.

💡 Mảng `hienTai` cùng biến đếm `soPhanTu` đóng vai trò một **ngăn xếp**: `hienTai[soPhanTu++] = x` là đẩy vào, `soPhanTu--` là lấy ra.

### Bài 13.

```c
#include <stdio.h>
#include <stdbool.h>

#define N 5
int meCung[N][N] = {
    {0, 1, 0, 0, 0},
    {0, 1, 0, 1, 0},
    {0, 0, 0, 1, 0},
    {1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0}
};
// 0 = di duoc, 1 = tuong

typedef struct {
    int hang, cot;
} O;

bool daTham[N][N];
O duongDi[N * N];
int doDai = 0;

bool timDuong(int r, int c) {
    // Ra ngoai bien, gap tuong, hoac da tham -> khong di duoc
    if (r < 0 || r >= N || c < 0 || c >= N) return false;
    if (meCung[r][c] == 1 || daTham[r][c])  return false;

    daTham[r][c] = true;
    duongDi[doDai].hang = r;
    duongDi[doDai].cot = c;
    doDai++;

    if (r == N - 1 && c == N - 1) return true;      // DEN DICH!

    // Thu 4 huong: xuong, phai, len, trai
    if (timDuong(r + 1, c)) return true;
    if (timDuong(r, c + 1)) return true;
    if (timDuong(r - 1, c)) return true;
    if (timDuong(r, c - 1)) return true;

    doDai--;                             // QUAY LUI: duong nay khong dan toi dich
    return false;
}

int main(void) {
    if (timDuong(0, 0)) {
        printf("Tim thay duong di (%d o):\n", doDai);
        for (int i = 0; i < doDai; i++) {
            printf("(%d,%d)", duongDi[i].hang, duongDi[i].cot);
            if (i + 1 < doDai) printf(" -> ");
        }
        printf("\n");
    } else {
        printf("Khong co duong di!\n");
    }
    return 0;
}
```

Output:

```
Tim thay duong di (9 o):
(0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) -> (3,2) -> (4,2) -> (4,3) -> (4,4)
```

**Đây là thuật toán DFS (tìm kiếm theo chiều sâu) + quay lui.** Mảng `daTham` ngăn việc đi lại ô cũ (nếu không sẽ lặp vô hạn).

💡 `struct` gom 2 giá trị hàng/cột của một ô thành một kiểu dữ liệu `O`, nhờ đó đường đi lưu gọn trong một mảng.

### Bài 14.

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

#define N 8
int viTriHau[N];          // viTriHau[i] = cot dat hau o hang i
int soNghiem = 0;
bool inNghiemDau = true;

bool anToan(int hang, int cot) {
    for (int i = 0; i < hang; i++) {
        // Cung cot?
        if (viTriHau[i] == cot) return false;
        // Cung duong cheo?
        if (abs(viTriHau[i] - cot) == abs(i - hang)) return false;
    }
    return true;
}

void inBanCo(void) {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%s", viTriHau[i] == j ? "Q " : ". ");
        }
        printf("\n");
    }
    printf("\n");
}

void datHau(int hang) {
    if (hang == N) {                    // da dat du 8 hau
        soNghiem++;
        if (inNghiemDau) { inBanCo(); inNghiemDau = false; }
        return;
    }

    for (int cot = 0; cot < N; cot++) {
        if (anToan(hang, cot)) {
            viTriHau[hang] = cot;       // DAT hau
            datHau(hang + 1);           // di tiep hang sau
            // Khong can "go hau" vi se bi ghi de o vong lap sau
        }
    }
}

int main(void) {
    datHau(0);
    printf("Tong so nghiem cua bai toan %d quan hau: %d\n", N, soNghiem);
    return 0;
}
```

Output:

```
Q . . . . . . . 
. . . . Q . . . 
. . . . . . . Q 
. . . . . Q . . 
. . Q . . . . . 
. . . . . . Q . 
. Q . . . . . . 
. . . Q . . . . 

Tong so nghiem cua bai toan 8 quan hau: 92
```

**Ý tưởng quay lui:**
1. Đặt hậu vào hàng 0, thử từng cột
2. Với mỗi vị trí an toàn, đệ quy sang hàng kế tiếp
3. Nếu hàng kế tiếp không có chỗ nào an toàn → quay lại thử cột khác ở hàng hiện tại
4. Đặt đủ 8 hậu → tìm được một nghiệm

**Số nghiệm theo N:**

| N | Số nghiệm |
|---|---|
| 4 | 2 |
| 6 | 4 |
| 8 | **92** |
| 10 | 724 |
| 12 | 14.200 |

💡 Nếu duyệt vét cạn mọi cách đặt 8 hậu trên 64 ô, sẽ có `C(64,8)` ≈ 4,4 tỷ trường hợp. Quay lui chỉ cần xét khoảng **15.000** vị trí nhờ cắt tỉa sớm các nhánh không hợp lệ.

### Bài 15.

```c
#include <stdio.h>

#define N 4
#define M 5
int a[N][M] = {
    { 1,  2,  3,  4,  5},
    { 6,  7,  8,  9, 10},
    {11, 12, 13, 14, 15},
    {16, 17, 18, 19, 20}
};

void xoanOc(int tren, int duoi, int trai, int phai) {
    if (tren > duoi || trai > phai) return;      // DIEU KIEN DUNG

    // (1) Di sang PHAI tren hang `tren`
    for (int j = trai; j <= phai; j++) printf("%4d", a[tren][j]);

    // (2) Di XUONG tren cot `phai`
    for (int i = tren + 1; i <= duoi; i++) printf("%4d", a[i][phai]);

    // (3) Di sang TRAI tren hang `duoi` (neu con hang)
    if (tren < duoi)
        for (int j = phai - 1; j >= trai; j--) printf("%4d", a[duoi][j]);

    // (4) Di LEN tren cot `trai` (neu con cot)
    if (trai < phai)
        for (int i = duoi - 1; i > tren; i--) printf("%4d", a[i][trai]);

    // DE QUY voi vong trong hon
    xoanOc(tren + 1, duoi - 1, trai + 1, phai - 1);
}

int main(void) {
    printf("Ma tran goc:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) printf("%4d", a[i][j]);
        printf("\n");
    }

    printf("\nDuyet xoan oc:\n");
    xoanOc(0, N - 1, 0, M - 1);
    printf("\n");
    return 0;
}
```

Output:

```
Ma tran goc:
   1   2   3   4   5
   6   7   8   9  10
  11  12  13  14  15
  16  17  18  19  20

Duyet xoan oc:
   1   2   3   4   5  10  15  20  19  18  17  16  11   6   7   8   9  14  13  12
```

**Ý tưởng:** mỗi lần đệ quy xử lý **một vòng ngoài cùng** (4 cạnh), rồi thu hẹp biên vào trong và gọi lại.

⚠️ **Hai câu `if` bảo vệ** rất quan trọng: khi vòng trong chỉ còn **một hàng** (`tren == duoi`) thì bước (3) sẽ in lại các phần tử đã in ở bước (1). Tương tự với một cột và bước (4).

Xem thêm bài [08-05 — Ma trận xoắn ốc](../08-05-c-ma-tran-xoan-oc.md) cho phiên bản dùng vòng lặp.
