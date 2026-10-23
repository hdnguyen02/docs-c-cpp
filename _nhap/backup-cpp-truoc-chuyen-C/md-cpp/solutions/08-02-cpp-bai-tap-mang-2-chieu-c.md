# Lời giải — [C++]. Bài Tập Mảng 2 Chiều C++

[← Quay lại bài học](../08-02-cpp-bai-tap-mang-2-chieu-c.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n;
    cout << "Nhap kich thuoc ma tran vuong: ";
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    long long cheoChinh = 0, cheoPhu = 0;
    for (int i = 0; i < n; i++) {
        cheoChinh += a[i][i];              // i == j
        cheoPhu   += a[i][n - 1 - i];      // i + j == n - 1
    }

    cout << "Tong duong cheo chinh = " << cheoChinh << endl;
    cout << "Tong duong cheo phu   = " << cheoPhu   << endl;
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

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n;
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    long long tren = 0, duoi = 0, cheo = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if      (j > i) tren += a[i][j];      // PHIA TREN duong cheo
            else if (j < i) duoi += a[i][j];      // PHIA DUOI
            else            cheo += a[i][j];      // TREN duong cheo
        }

    cout << "Tong phia tren duong cheo = " << tren << endl;
    cout << "Tong phia duoi duong cheo = " << duoi << endl;
    cout << "Tong tren duong cheo      = " << cheo << endl;
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

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n;
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    bool doiXung = true;
    for (int i = 0; i < n && doiXung; i++) {
        for (int j = i + 1; j < n; j++) {        // chi can xet NUA TREN
            if (a[i][j] != a[j][i]) { doiXung = false; break; }
        }
    }

    cout << "Ma tran " << (doiXung ? "DOI XUNG" : "KHONG doi xung")
         << " qua duong cheo chinh" << endl;
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

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

void inMT(int a[][100], int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    cout << endl;
}

int main() {
    int a[100][100] = {{1,2,3},{4,5,6},{7,8,9}};
    int n = 3, m = 3;

    cout << "Ban dau:" << endl;         inMT(a, n, m);

    // Hoan doi hang 0 va hang 2
    for (int j = 0; j < m; j++) swap(a[0][j], a[2][j]);
    cout << "Sau khi doi hang 0 va 2:" << endl;  inMT(a, n, m);

    // Hoan doi cot 0 va cot 1
    for (int i = 0; i < n; i++) swap(a[i][0], a[i][1]);
    cout << "Sau khi doi cot 0 va 1:" << endl;   inMT(a, n, m);

    return 0;
}
```

💡 **Đổi hàng** → duyệt qua các cột. **Đổi cột** → duyệt qua các hàng.

💡 Với `vector<vector<int>>`, đổi hàng chỉ cần `swap(a[0], a[2])` — cực nhanh vì chỉ tráo con trỏ nội bộ, không sao chép dữ liệu.

### Bài 5.

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    // ① Do ma tran ra mang 1 chieu
    int b[10000];
    int k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) b[k++] = a[i][j];

    // ② Sap xep
    sort(b, b + k);

    // ③ Do nguoc lai vao ma tran
    k = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) a[i][j] = b[k++];

    cout << "\nMa tran sau khi sap xep:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 **Mẹo hay:** vì ma trận được lưu liên tục trong bộ nhớ (xem bài [08-01](../08-01-c-ly-thuyet-mang-2-chieu-c.md) bài 8), với mảng tĩnh có **đúng** `n` hàng `m` cột có thể sort trực tiếp:

```cpp
sort(&a[0][0], &a[0][0] + n * m);     // chi dung khi ma tran KHIT (n = so hang khai bao)
```

⚠️ Cách này **sai** nếu bạn khai báo `a[100][100]` nhưng chỉ dùng `3×3` — vì các ô không dùng nằm xen giữa.

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    for (int i = 0; i < n; i++) {
        sort(a[i], a[i] + m);            // a[i] la mang 1 chieu (1 hang)
    }

    cout << "\nSau khi sap xep tung hang:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 **`a[i]` chính là một mảng 1 chiều** (hàng thứ `i`), nên dùng trực tiếp với `sort` được.

**Sắp xếp từng cột** khó hơn vì các phần tử không liền nhau — phải copy ra mảng tạm:

```cpp
for (int j = 0; j < m; j++) {
    int cot[100];
    for (int i = 0; i < n; i++) cot[i] = a[i][j];
    sort(cot, cot + n);
    for (int i = 0; i < n; i++) a[i][j] = cot[i];
}
```

### Bài 7.

```cpp
#include <iostream>
using namespace std;

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
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int hangTot = 0, demMax = -1;
    for (int i = 0; i < n; i++) {
        int dem = 0;
        for (int j = 0; j < m; j++)
            if (laNguyenTo(a[i][j])) dem++;

        cout << "Hang " << i << ": " << dem << " so nguyen to" << endl;
        if (dem > demMax) { demMax = dem; hangTot = i; }
    }

    cout << "\nHang " << hangTot << " co nhieu so nguyen to nhat ("
         << demMax << " so)" << endl;
    return 0;
}
```

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "Cac phan tu yen ngua:" << endl;
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
                cout << "  a[" << i << "][" << j << "] = " << a[i][j] << endl;
                dem++;
            }
        }
    }

    if (dem == 0) cout << "  (khong co)" << endl;
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

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

void inMT(int a[][100], int n, int m) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    cout << endl;
}

void xoaHang(int a[][100], int &n, int m, int k) {
    if (k < 0 || k >= n) return;
    for (int i = k; i < n - 1; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = a[i + 1][j];
    n--;
}

void xoaCot(int a[][100], int n, int &m, int k) {
    if (k < 0 || k >= m) return;
    for (int i = 0; i < n; i++)
        for (int j = k; j < m - 1; j++)
            a[i][j] = a[i][j + 1];
    m--;
}

int main() {
    int a[100][100] = {
        {1,2,3,4}, {5,6,7,8}, {9,10,11,12}, {13,14,15,16}
    };
    int n = 4, m = 4;

    cout << "Ban dau:" << endl;                inMT(a, n, m);

    xoaHang(a, n, m, 1);
    cout << "Sau khi xoa hang 1:" << endl;     inMT(a, n, m);

    xoaCot(a, n, m, 2);
    cout << "Sau khi xoa cot 2:" << endl;      inMT(a, n, m);

    return 0;
}
```

💡 Tương tự chèn/xoá mảng 1 chiều (bài [06-05](../06-05-cpp-chen-va-xoa-phan-tu.md)), chỉ khác là phải dịch **cả một hàng/cột**.

⚠️ `n` và `m` phải là **tham chiếu** để hàm cập nhật được kích thước.

### Bài 10.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

void chenHang(int a[][100], int &n, int m, int k, const int hangMoi[]) {
    if (k < 0 || k > n) return;

    // Dich cac hang tu k tro di XUONG DUOI (duyet tu cuoi)
    for (int i = n; i > k; i--)
        for (int j = 0; j < m; j++)
            a[i][j] = a[i - 1][j];

    for (int j = 0; j < m; j++) a[k][j] = hangMoi[j];
    n++;
}

int main() {
    int a[100][100] = {{1,2,3}, {4,5,6}, {7,8,9}};
    int n = 3, m = 3;
    int hangMoi[3] = {99, 98, 97};

    chenHang(a, n, m, 1, hangMoi);

    cout << "Sau khi chen hang tai vi tri 1:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

Output:

```
    1    2    3
   99   98   97
    4    5    6
    7    8    9
```

⚠️ **Duyệt từ cuối về đầu** khi dịch xuống — nếu duyệt xuôi sẽ ghi đè mất dữ liệu.

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n;
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> a[i][j];

    bool tamGiacTren = true, tamGiacDuoi = true;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            if (j < i && a[i][j] != 0) tamGiacTren = false;   // phia duoi phai = 0
            if (j > i && a[i][j] != 0) tamGiacDuoi = false;   // phia tren phai = 0
        }

    if (tamGiacTren && tamGiacDuoi) cout << "Ma tran DUONG CHEO" << endl;
    else if (tamGiacTren)           cout << "Ma tran TAM GIAC TREN" << endl;
    else if (tamGiacDuoi)           cout << "Ma tran TAM GIAC DUOI" << endl;
    else                            cout << "Khong phai ma tran tam giac" << endl;
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

```cpp
#include <iostream>
using namespace std;

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
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;
    cout << "Nhap ma tran 0/1:" << endl;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int soVung = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 1 && !daTham[i][j]) {
                soVung++;
                dfs(i, j);              // "to mau" toan bo vung nay
            }
        }

    cout << "So vung lien thong = " << soVung << endl;
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

```cpp
int dr[] = {-1,-1,-1, 0, 0, 1, 1, 1};
int dc[] = {-1, 0, 1,-1, 1,-1, 0, 1};
```

⚠️ Với ma trận lớn (> 1000×1000), DFS đệ quy có thể tràn stack — khi đó dùng BFS với `queue`.

### Bài 13.

```cpp
#include <iostream>
#include <climits>
using namespace std;

int main() {
    int a[55][55], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    // Tinh tong tien to 2 chieu: pre[i][j] = tong hinh chu nhat (0,0)-(i-1,j-1)
    long long pre[55][55] = {};
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

    cout << "Tong lon nhat = " << tongMax << endl;
    cout << "Hinh chu nhat tu (" << r1 << "," << c1 << ") den ("
         << r2 << "," << c2 << ")" << endl;
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

💡 Có thuật toán O(n²m) dùng Kadane (bài [06-02](../06-02-cpp-bai-tap-mang-1-chieu-p1.md) bài 6) cho từng cặp hàng.

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    long long dp[100][100];

    // Quy hoach dong: dp[i][j] = tong nho nhat de den o (i,j)
    dp[0][0] = a[0][0];

    for (int j = 1; j < m; j++) dp[0][j] = dp[0][j-1] + a[0][j];   // hang dau: chi di phai
    for (int i = 1; i < n; i++) dp[i][0] = dp[i-1][0] + a[i][0];   // cot dau: chi di xuong

    for (int i = 1; i < n; i++)
        for (int j = 1; j < m; j++)
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + a[i][j];

    cout << "Tong nho nhat = " << dp[n-1][m-1] << endl;

    // Truy vet duong di
    cout << "Duong di: ";
    int i = n - 1, j = m - 1;
    string duongDi = "";
    while (i > 0 || j > 0) {
        duongDi = "(" + to_string(i) + "," + to_string(j) + ") " + duongDi;
        if (i == 0)                        j--;
        else if (j == 0)                   i--;
        else if (dp[i-1][j] < dp[i][j-1])  i--;
        else                               j--;
    }
    cout << "(0,0) " << duongDi << endl;
    return 0;
}
```

Ví dụ với ma trận:

```
1 3 1
1 5 1
4 2 1
```

→ Tổng nhỏ nhất = **7**, đường đi: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)... thực ra là 1→1→4→2→1 hoặc 1→3→1→1→1 = 7.

**Quy hoạch động (dynamic programming):** để đến ô `(i,j)`, ta chỉ có thể đến từ ô **trên** `(i-1,j)` hoặc ô **trái** `(i,j-1)`. Chọn cái nhỏ hơn.

Độ phức tạp **O(n×m)** — tối ưu.

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap kich thuoc bang: ";
    cin >> n >> m;

    int bom[50][50];
    cout << "Nhap ma tran 0/1 (1 = co min):" << endl;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> bom[i][j];

    int dem[50][50] = {};

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

    cout << "\nBang do min:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (dem[i][j] == -1) cout << setw(3) << "*";
            else if (dem[i][j] == 0) cout << setw(3) << ".";
            else cout << setw(3) << dem[i][j];
        }
        cout << endl;
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
  *  1  1  1
  1  2  *  1
  1  2  1  1
  .  1  1  .
```

**Kỹ thuật cốt lõi:** với mỗi ô không có mìn, đếm số mìn trong 8 ô xung quanh.

⚠️ **Luôn kiểm tra biên** `r >= 0 && r < n && c >= 0 && c < m` trước khi truy cập — các ô ở viền không có đủ 8 hàng xóm.

💡 Cách viết gọn hơn không cần mảng `dr`/`dc`:

```cpp
for (int dr = -1; dr <= 1; dr++)
    for (int dc = -1; dc <= 1; dc++) {
        if (dr == 0 && dc == 0) continue;     // bo qua chinh no
        int r = i + dr, c = j + dc;
        if (r >= 0 && r < n && c >= 0 && c < m && bom[r][c]) dem[i][j]++;
    }
```
