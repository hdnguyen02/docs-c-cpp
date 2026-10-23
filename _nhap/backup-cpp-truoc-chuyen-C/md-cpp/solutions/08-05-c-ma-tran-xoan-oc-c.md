# Lời giải — [C++]. Ma Trận Xoắn Ốc C++

[← Quay lại bài học](../08-05-c-ma-tran-xoan-oc-c.md)

> **Ý tưởng chung:** giữ 4 biên `tren`, `duoi`, `trai`, `phai`. Mỗi vòng đi 4 cạnh rồi thu hẹp biên vào trong.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;

    cout << "\nXoan oc (cung chieu kim dong ho): ";
    while (tren <= duoi && trai <= phai) {
        // ① Sang PHAI tren hang `tren`
        for (int j = trai; j <= phai; j++) cout << a[tren][j] << " ";
        tren++;

        // ② XUONG tren cot `phai`
        for (int i = tren; i <= duoi; i++) cout << a[i][phai] << " ";
        phai--;

        // ③ Sang TRAI tren hang `duoi` (neu con hang)
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) cout << a[duoi][j] << " ";
            duoi--;
        }

        // ④ LEN tren cot `trai` (neu con cot)
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) cout << a[i][trai] << " ";
            trai++;
        }
    }
    cout << endl;
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

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;

    cout << "\nXoan oc (NGUOC chieu kim dong ho): ";
    while (tren <= duoi && trai <= phai) {
        // ① XUONG tren cot `trai`
        for (int i = tren; i <= duoi; i++) cout << a[i][trai] << " ";
        trai++;

        // ② Sang PHAI tren hang `duoi`
        for (int j = trai; j <= phai; j++) cout << a[duoi][j] << " ";
        duoi--;

        // ③ LEN tren cot `phai`
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) cout << a[i][phai] << " ";
            phai--;
        }

        // ④ Sang TRAI tren hang `tren`
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) cout << a[tren][j] << " ";
            tren++;
        }
    }
    cout << endl;
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

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int a[100][100] = {};
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

    cout << "\nMa tran xoan oc " << n << "x" << n << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << a[i][j];
        cout << endl;
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

💡 **Code y hệt bài 1**, chỉ thay `cout << a[...]` bằng `a[...] = so++`.

### Bài 4.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int a[100][100] = {};
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

    cout << "\nXoan oc tu TRONG RA NGOAI:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << setw(5) << a[i][j];
        cout << endl;
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

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "\nZigzag: ";
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {                          // hang CHAN: trai -> phai
            for (int j = 0; j < m; j++) cout << a[i][j] << " ";
        } else {                                   // hang LE: phai -> trai
            for (int j = m - 1; j >= 0; j--) cout << a[i][j] << " ";
        }
    }
    cout << endl;
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

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "\nTheo duong cheo (i + j tang dan):" << endl;
    for (int s = 0; s <= n + m - 2; s++) {         // s = i + j
        cout << "  Cheo " << s << ": ";
        for (int i = 0; i < n; i++) {
            int j = s - i;
            if (j >= 0 && j < m) cout << a[i][j] << " ";
        }
        cout << endl;
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

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;

    vector<int> day(n * m);
    cout << "Nhap " << n * m << " so: ";
    for (int i = 0; i < n * m; i++) cin >> day[i];

    int a[100][100] = {};
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

    cout << "\nMa tran ket qua:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

💡 Đây là **phép biến đổi ngược** của bài 1. Kết hợp cả hai, bạn có thể "mã hoá" một dãy số thành ma trận và giải mã ngược lại.

### Bài 8.

```cpp
#include <iostream>
#include <iomanip>
#include <vector>
using namespace std;

int main() {
    int n = 4, k;
    int a[100][100] = {
        {1,2,3,4}, {5,6,7,8}, {9,10,11,12}, {13,14,15,16}
    };
    int m = 4;

    cout << "Nhap so buoc dich k: ";
    cin >> k;

    // ① Doc ma tran theo xoan oc vao mang 1 chieu
    vector<int> day;
    vector<pair<int,int>> viTri;
    int tren = 0, duoi = n-1, trai = 0, phai = m-1;

    while (tren <= duoi && trai <= phai) {
        for (int j = trai; j <= phai; j++) { day.push_back(a[tren][j]); viTri.push_back({tren,j}); }
        tren++;
        for (int i = tren; i <= duoi; i++) { day.push_back(a[i][phai]); viTri.push_back({i,phai}); }
        phai--;
        if (tren <= duoi) {
            for (int j = phai; j >= trai; j--) { day.push_back(a[duoi][j]); viTri.push_back({duoi,j}); }
            duoi--;
        }
        if (trai <= phai) {
            for (int i = duoi; i >= tren; i--) { day.push_back(a[i][trai]); viTri.push_back({i,trai}); }
            trai++;
        }
    }

    // ② Dich vong mang 1 chieu
    int tong = day.size();
    k = ((k % tong) + tong) % tong;

    // ③ Ghi nguoc lai vao ma tran
    for (int i = 0; i < tong; i++) {
        auto [r, c] = viTri[(i + k) % tong];
        a[r][c] = day[i];
    }

    cout << "\nSau khi dich " << k << " buoc theo xoan oc:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

**Kỹ thuật:** thay vì cố dịch trực tiếp trên ma trận (rất rối), ta:
1. "Trải phẳng" đường xoắn ốc thành mảng 1 chiều + lưu kèm vị trí
2. Dịch vòng mảng 1 chiều (dễ)
3. Ghi ngược lại vào ma trận theo danh sách vị trí đã lưu

💡 Đây là mẫu tư duy chung: **đưa bài toán khó về bài toán dễ đã biết cách giải.**

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;

    int soVong = (min(n, m) + 1) / 2;

    cout << "Ma tran " << n << "x" << m << " co " << soVong << " vong xoan" << endl;

    // Kiem chung bang cach dem thuc te
    int dem = 0;
    int tren = 0, duoi = n - 1, trai = 0, phai = m - 1;
    while (tren <= duoi && trai <= phai) {
        dem++;
        tren++; duoi--; trai++; phai--;
    }
    cout << "Dem thuc te: " << dem << " vong" << endl;
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

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100][100], n, m, k;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "Nhap vong can in (bat dau tu 0): ";
    cin >> k;

    int soVong = (min(n, m) + 1) / 2;
    if (k < 0 || k >= soVong) {
        cout << "Vong khong hop le! (co " << soVong << " vong)" << endl;
        return 1;
    }

    // Bien cua vong thu k
    int tren = k, duoi = n - 1 - k, trai = k, phai = m - 1 - k;

    cout << "\nVong " << k << ": ";
    for (int j = trai; j <= phai; j++) cout << a[tren][j] << " ";
    for (int i = tren + 1; i <= duoi; i++) cout << a[i][phai] << " ";
    if (tren < duoi)
        for (int j = phai - 1; j >= trai; j--) cout << a[duoi][j] << " ";
    if (trai < phai)
        for (int i = duoi - 1; i > tren; i--) cout << a[i][trai] << " ";
    cout << endl;
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

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int a[100][100];
int n, m;

void xoanOc(int tren, int duoi, int trai, int phai) {
    if (tren > duoi || trai > phai) return;          // DIEU KIEN DUNG

    for (int j = trai; j <= phai; j++) cout << setw(5) << a[tren][j];
    for (int i = tren + 1; i <= duoi; i++) cout << setw(5) << a[i][phai];

    if (tren < duoi)
        for (int j = phai - 1; j >= trai; j--) cout << setw(5) << a[duoi][j];
    if (trai < phai)
        for (int i = duoi - 1; i > tren; i--) cout << setw(5) << a[i][trai];

    // DE QUY voi vong trong hon
    xoanOc(tren + 1, duoi - 1, trai + 1, phai - 1);
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++) cin >> a[i][j];

    cout << "\nXoan oc (de quy):" << endl;
    xoanOc(0, n - 1, 0, m - 1);
    cout << endl;
    return 0;
}
```

💡 Bản đệ quy **ngắn gọn và tự nhiên hơn**: mỗi lời gọi xử lý đúng một vòng, rồi giao phần còn lại cho lời gọi kế tiếp.

Độ sâu đệ quy chỉ `O(min(n,m)/2)` nên không lo tràn stack.

### Bài 12.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;

    int a[100][100] = {};
    bool daTham[100][100] = {};

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

    cout << "\nMa tran xoan oc (mo phong buoc di):" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
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

### Bài 13.

```cpp
#include <iostream>
using namespace std;

// Tim vi tri cua so k trong ma tran xoan oc n x n (dien tu 1)
pair<int,int> timViTri(int n, int k) {
    if (k < 1 || k > n * n) return {-1, -1};

    int tren = 0, duoi = n - 1, trai = 0, phai = n - 1;
    int so = 1;

    while (tren <= duoi && trai <= phai) {
        // Canh tren
        int doDai = phai - trai + 1;
        if (k < so + doDai) return {tren, trai + (k - so)};
        so += doDai;
        tren++;

        // Canh phai
        doDai = duoi - tren + 1;
        if (doDai > 0) {
            if (k < so + doDai) return {tren + (k - so), phai};
            so += doDai;
        }
        phai--;

        // Canh duoi
        if (tren <= duoi) {
            doDai = phai - trai + 1;
            if (doDai > 0) {
                if (k < so + doDai) return {duoi, phai - (k - so)};
                so += doDai;
            }
            duoi--;
        }

        // Canh trai
        if (trai <= phai) {
            doDai = duoi - tren + 1;
            if (doDai > 0) {
                if (k < so + doDai) return {duoi - (k - so), trai};
                so += doDai;
            }
            trai++;
        }
    }
    return {-1, -1};
}

int main() {
    int n = 5;
    for (int k : {1, 5, 6, 13, 25}) {
        auto [i, j] = timViTri(n, k);
        cout << "So " << k << " nam tai (" << i << ", " << j << ")" << endl;
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

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap so hang, cot: ";
    cin >> n >> m;

    int a[100][100] = {};
    int so = 1;
    int soVong = (min(n, m) + 1) / 2;

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

    cout << "\nMa tran boustrophedon (moi vong doi chieu):" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }
    return 0;
}
```

Với `n = m = 5`:

```
    1    2    3    4    5
   16   21   22   17    6
   15   20   25   18    7
   14   19   24   23    8
   13   12   11   10    9
```

💡 **"Boustrophedon"** là từ Hy Lạp cổ nghĩa là "như đường cày của con bò" — đi hết một luống rồi quay lại luống kế. Một số văn bản Hy Lạp cổ được viết theo kiểu này.

### Bài 15.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Nhap kich thuoc (nen le, vd 21): ";
    cin >> n;

    char hinh[101][101];

    // ① Tao ma tran xoan oc dang so
    int a[101][101] = {};
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

    // ② Dua so ve ky tu: xen ke * va khoang trang theo chu ky
    const int CHU_KY = 6;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            hinh[i][j] = (a[i][j] % CHU_KY < CHU_KY / 2) ? '*' : ' ';

    cout << "\nHoa van xoan oc:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) cout << hinh[i][j] << hinh[i][j];  // in doi de vuong hon
        cout << endl;
    }

    // ③ Bien the: ve xoan oc bang duong lien tuc
    cout << "\nDuong xoan oc lien tuc:" << endl;
    int b[101][101] = {};
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
        for (int j = 0; j < n; j++) cout << (b[i][j] ? "##" : "  ");
        cout << endl;
    }
    return 0;
}
```

Ví dụ output (rút gọn, `n = 15`):

```
Duong xoan oc lien tuc:
  ############################
  ##                        ##
  ##  ####################  ##
  ##  ##                ##  ##
  ##  ##  ############  ##  ##
  ##  ##  ##        ##  ##  ##
  ##  ##  ##  ####  ##  ##  ##
  ...
```

💡 **Kỹ thuật chung để vẽ hoa văn:** tính một **giá trị số** cho mỗi ô (ở đây là thứ tự xoắn ốc), rồi ánh xạ giá trị đó thành ký tự theo một quy tắc. Đổi quy tắc ánh xạ là được hoa văn khác.

Một số ý tưởng ánh xạ khác:
```cpp
hinh[i][j] = (a[i][j] % 2) ? '#' : '.';                  // soc xen ke
hinh[i][j] = "....:::;;;***###@@@"[a[i][j] * 18 / (n*n)]; // do dam tang dan
hinh[i][j] = (int)(sqrt(a[i][j])) % 2 ? '*' : ' ';        // vong tron dong tam
```

**In mỗi ký tự 2 lần** (`cout << hinh[i][j] << hinh[i][j]`) vì ký tự trong terminal cao gấp đôi chiều rộng — làm vậy hình sẽ vuông hơn.
