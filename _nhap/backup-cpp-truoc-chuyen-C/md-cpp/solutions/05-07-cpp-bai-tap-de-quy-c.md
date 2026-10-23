# Lời giải — [C++]. Bài Tập Đệ Quy C++

[← Quay lại bài học](../05-07-cpp-bai-tap-de-quy-c.md)

---

### Bài 1.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

double tongNghichDao(int n) {
    if (n <= 0) return 0;
    return 1.0 / n + tongNghichDao(n - 1);      // chu y 1.0 chu khong phai 1
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;
    cout << fixed << setprecision(10);
    cout << "S = " << tongNghichDao(n) << endl;
    return 0;
}
```

⚠️ Viết `1 / n` (cả hai đều `int`) sẽ cho 0 với mọi `n > 1`. Phải là `1.0 / n`.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

long long tongBinhPhuong(int n) {
    if (n <= 0) return 0;
    return (long long)n * n + tongBinhPhuong(n - 1);
}

int main() {
    int n;
    cin >> n;
    cout << "S = " << tongBinhPhuong(n) << endl;
    // Kiem chung bang cong thuc: n(n+1)(2n+1)/6
    cout << "Cong thuc: " << (long long)n * (n + 1) * (2 * n + 1) / 6 << endl;
    return 0;
}
```

### Bài 3.

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int demChuSoChan(int n) {
    n = abs(n);
    if (n == 0) return 0;
    int cuoi = n % 10;
    return (cuoi % 2 == 0 ? 1 : 0) + demChuSoChan(n / 10);
}

int main() {
    int n = 246813;
    cout << n << " co " << demChuSoChan(n) << " chu so chan" << endl;   // 3
    return 0;
}
```

⚠️ Với `n = 0`, hàm trả về 0 — nhưng số 0 có 1 chữ số chẵn. Nếu cần xử lý đúng, thêm:

```cpp
int demChuSoChan(int n) {
    n = abs(n);
    if (n < 10) return (n % 2 == 0 ? 1 : 0);
    return (n % 10 % 2 == 0 ? 1 : 0) + demChuSoChan(n / 10);
}
```

### Bài 4.

```cpp
#include <iostream>
using namespace std;

// Ham de quy voi tham so phu i (uoc dang thu)
bool laNguyenTo(int n, int i) {
    if (n < 2) return false;
    if ((long long)i * i > n) return true;      // da thu het -> la nguyen to
    if (n % i == 0) return false;               // tim thay uoc -> khong phai
    return laNguyenTo(n, i + 1);
}

// Ham vo cho nguoi dung goi
bool laNguyenTo(int n) {
    return laNguyenTo(n, 2);
}

int main() {
    for (int n : {1, 2, 9, 17, 100, 97}) {
        cout << n << " -> " << (laNguyenTo(n) ? "nguyen to" : "khong") << endl;
    }
    return 0;
}
```

💡 **Mẫu "hàm vỏ + hàm đệ quy có tham số phụ"** rất thường gặp: người dùng gọi `laNguyenTo(97)` đơn giản, còn tham số `i` là chi tiết nội bộ.

⚠️ Độ sâu đệ quy là O(√n) — với `n = 10¹⁸` cần 10⁹ tầng → tràn stack. Bài này nên dùng vòng lặp trong thực tế.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

long long tongMang(int a[], int n) {
    if (n <= 0) return 0;
    return a[n - 1] + tongMang(a, n - 1);       // cong phan tu CUOI + tong phan con lai
}

int main() {
    int a[] = {3, 7, -2, 8, 5};
    cout << "Tong = " << tongMang(a, 5) << endl;   // 21
    return 0;
}
```

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int timKiem(int a[], int n, int x, int i = 0) {
    if (i >= n) return -1;                  // het mang -> khong tim thay
    if (a[i] == x) return i;                // tim thay
    return timKiem(a, n, x, i + 1);         // xet phan tu ke tiep
}

int main() {
    int a[] = {5, 3, 8, 3, 1};
    cout << "Tim 8: vi tri " << timKiem(a, 5, 8) << endl;    // 2
    cout << "Tim 3: vi tri " << timKiem(a, 5, 3) << endl;    // 1 (dau tien)
    cout << "Tim 9: vi tri " << timKiem(a, 5, 9) << endl;    // -1
    return 0;
}
```

💡 Dùng **đối số mặc định** `int i = 0` để người dùng không phải truyền tham số phụ.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

long long toHop(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;                    // C(n,0) = C(n,n) = 1
    return toHop(n - 1, k - 1) + toHop(n - 1, k);      // cong thuc Pascal
}

int main() {
    cout << "C(5,2)  = " << toHop(5, 2)  << endl;    // 10
    cout << "C(10,5) = " << toHop(10, 5) << endl;    // 252
    return 0;
}
```

⚠️ **Rất chậm** — giống Fibonacci, cùng một `C(n,k)` bị tính lại nhiều lần. `C(30,15)` đã mất vài giây.

**Cải tiến bằng ghi nhớ:**

```cpp
long long bang[61][61];
bool daTinh[61][61];

long long toHopMemo(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;
    if (daTinh[n][k]) return bang[n][k];
    daTinh[n][k] = true;
    return bang[n][k] = toHopMemo(n-1, k-1) + toHopMemo(n-1, k);
}
```

### Bài 8.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

long long bang[35][35];
bool daTinh[35][35];

long long toHop(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k == 0 || k == n) return 1;
    if (daTinh[n][k]) return bang[n][k];
    daTinh[n][k] = true;
    return bang[n][k] = toHop(n - 1, k - 1) + toHop(n - 1, k);
}

int main() {
    int n;
    cout << "Nhap so dong: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        // In dau cach de can giua
        cout << setw((n - i) * 3) << "";
        for (int j = 0; j <= i; j++) {
            cout << setw(6) << toHop(i, j);
        }
        cout << endl;
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

💡 **Tam giác Pascal** — mỗi số bằng tổng 2 số ngay phía trên nó, chính là công thức `C(n,k) = C(n-1,k-1) + C(n-1,k)`.

### Bài 9.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int demDay = 0;

void sinhNhiPhan(vector<int>& day, int viTri, int n) {
    if (viTri == n) {                       // da dien day du n vi tri
        demDay++;
        for (int x : day) cout << x;
        cout << endl;
        return;
    }

    for (int giaTri = 0; giaTri <= 1; giaTri++) {
        day[viTri] = giaTri;                // THU gia tri nay
        sinhNhiPhan(day, viTri + 1, n);     // sinh tiep phan con lai
    }
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    vector<int> day(n);
    sinhNhiPhan(day, 0, n);

    cout << "Tong cong: " << demDay << " day (= 2^" << n << ")" << endl;
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

```cpp
#include <iostream>
#include <vector>
using namespace std;

int demHoanVi = 0;

void sinhHoanVi(vector<int>& hv, vector<bool>& daDung, int viTri, int n) {
    if (viTri == n) {
        demHoanVi++;
        for (int x : hv) cout << x << " ";
        cout << endl;
        return;
    }

    for (int giaTri = 1; giaTri <= n; giaTri++) {
        if (daDung[giaTri]) continue;       // gia tri nay da dung roi

        hv[viTri] = giaTri;
        daDung[giaTri] = true;              // DANH DAU

        sinhHoanVi(hv, daDung, viTri + 1, n);

        daDung[giaTri] = false;             // BO DANH DAU (quay lui!)
    }
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    vector<int>  hv(n);
    vector<bool> daDung(n + 1, false);

    sinhHoanVi(hv, daDung, 0, n);
    cout << "Tong cong: " << demHoanVi << " hoan vi (= " << n << "!)" << endl;
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

💡 C++ có sẵn `next_permutation` trong `<algorithm>`:

```cpp
vector<int> v = {1, 2, 3};
do {
    for (int x : v) cout << x << " ";
    cout << endl;
} while (next_permutation(v.begin(), v.end()));
```

### Bài 11.

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<long long> bangNho;

long long demCach(int n) {
    if (n < 0) return 0;
    if (n == 0) return 1;                      // 1 cach: khong leo gi
    if (bangNho[n] != -1) return bangNho[n];

    // Buoc cuoi cung leo 1 bac HOAC 2 bac
    return bangNho[n] = demCach(n - 1) + demCach(n - 2);
}

int main() {
    int n;
    cout << "Nhap so bac thang: ";
    cin >> n;

    bangNho.assign(n + 1, -1);
    cout << "So cach leo = " << demCach(n) << endl;
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

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Dem so cach viet n thanh tong cac so nguyen duong KHONG VUOT QUA max
// (khong phan biet thu tu, vd 4 = 3+1 = 2+2 = 2+1+1 = 1+1+1+1 = 4)
long long demPhanHoach(int n, int max) {
    if (n == 0) return 1;                   // da chia het -> 1 cach hop le
    if (n < 0 || max == 0) return 0;

    // Hoac DUNG so max, hoac KHONG dung so max nua
    return demPhanHoach(n - max, max) + demPhanHoach(n, max - 1);
}

void inPhanHoach(int n, int max, vector<int>& hienTai) {
    if (n == 0) {
        for (size_t i = 0; i < hienTai.size(); i++) {
            cout << hienTai[i];
            if (i + 1 < hienTai.size()) cout << " + ";
        }
        cout << endl;
        return;
    }
    if (n < 0 || max == 0) return;

    hienTai.push_back(max);
    inPhanHoach(n - max, max, hienTai);      // dung so max
    hienTai.pop_back();                      // quay lui

    inPhanHoach(n, max - 1, hienTai);        // khong dung so max nua
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << "So cach phan hoach: " << demPhanHoach(n, n) << endl;
    cout << "Chi tiet:" << endl;
    vector<int> tam;
    inPhanHoach(n, n, tam);
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

### Bài 13.

```cpp
#include <iostream>
#include <vector>
using namespace std;

const int N = 5;
int meCung[N][N] = {
    {0, 1, 0, 0, 0},
    {0, 1, 0, 1, 0},
    {0, 0, 0, 1, 0},
    {1, 1, 0, 1, 0},
    {0, 0, 0, 0, 0}
};
// 0 = di duoc, 1 = tuong

bool daTham[N][N];
vector<pair<int,int>> duongDi;

bool timDuong(int r, int c) {
    // Ra ngoai bien, gap tuong, hoac da tham -> khong di duoc
    if (r < 0 || r >= N || c < 0 || c >= N) return false;
    if (meCung[r][c] == 1 || daTham[r][c])  return false;

    daTham[r][c] = true;
    duongDi.push_back({r, c});

    if (r == N - 1 && c == N - 1) return true;      // DEN DICH!

    // Thu 4 huong: xuong, phai, len, trai
    if (timDuong(r + 1, c)) return true;
    if (timDuong(r, c + 1)) return true;
    if (timDuong(r - 1, c)) return true;
    if (timDuong(r, c - 1)) return true;

    duongDi.pop_back();                             // QUAY LUI: duong nay khong dan toi dich
    return false;
}

int main() {
    if (timDuong(0, 0)) {
        cout << "Tim thay duong di (" << duongDi.size() << " o):" << endl;
        for (size_t i = 0; i < duongDi.size(); i++) {
            cout << "(" << duongDi[i].first << "," << duongDi[i].second << ")";
            if (i + 1 < duongDi.size()) cout << " -> ";
        }
        cout << endl;
    } else {
        cout << "Khong co duong di!" << endl;
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

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <cstdlib>
using namespace std;

const int N = 8;
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

void inBanCo() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cout << (viTriHau[i] == j ? "Q " : ". ");
        }
        cout << endl;
    }
    cout << endl;
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

int main() {
    datHau(0);
    cout << "Tong so nghiem cua bai toan " << N << " quan hau: " << soNghiem << endl;
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

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

const int N = 4, M = 5;
int a[N][M] = {
    { 1,  2,  3,  4,  5},
    { 6,  7,  8,  9, 10},
    {11, 12, 13, 14, 15},
    {16, 17, 18, 19, 20}
};

void xoanOc(int tren, int duoi, int trai, int phai) {
    if (tren > duoi || trai > phai) return;      // DIEU KIEN DUNG

    // ① Di sang PHAI tren hang `tren`
    for (int j = trai; j <= phai; j++) cout << setw(4) << a[tren][j];

    // ② Di XUONG tren cot `phai`
    for (int i = tren + 1; i <= duoi; i++) cout << setw(4) << a[i][phai];

    // ③ Di sang TRAI tren hang `duoi` (neu con hang)
    if (tren < duoi)
        for (int j = phai - 1; j >= trai; j--) cout << setw(4) << a[duoi][j];

    // ④ Di LEN tren cot `trai` (neu con cot)
    if (trai < phai)
        for (int i = duoi - 1; i > tren; i--) cout << setw(4) << a[i][trai];

    // DE QUY voi vong trong hon
    xoanOc(tren + 1, duoi - 1, trai + 1, phai - 1);
}

int main() {
    cout << "Ma tran goc:" << endl;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) cout << setw(4) << a[i][j];
        cout << endl;
    }

    cout << "\nDuyet xoan oc:" << endl;
    xoanOc(0, N - 1, 0, M - 1);
    cout << endl;
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

⚠️ **Hai câu `if` bảo vệ** rất quan trọng: khi vòng trong chỉ còn **một hàng** (`tren == duoi`) thì bước ③ sẽ in lại các phần tử đã in ở bước ①. Tương tự với một cột và bước ④.

Xem thêm bài [08-05 — Ma trận xoắn ốc](../08-05-c-ma-tran-xoan-oc-c.md) cho phiên bản dùng vòng lặp.
