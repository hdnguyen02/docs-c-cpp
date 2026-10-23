# Lời giải — [C++]. Bài Tập Mảng 1 Chiều P1

[← Quay lại bài học](../06-02-cpp-bai-tap-mang-1-chieu-p1.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i];
    double tb = (double)tong / n;

    long long tongLon = 0;
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] > tb) { tongLon += a[i]; dem++; }
    }

    cout << "Trung binh cong = " << tb << endl;
    cout << "Co " << dem << " phan tu lon hon TB, tong = " << tongLon << endl;
    return 0;
}
```

⚠️ Phải duyệt **2 lần**: lần đầu tính trung bình, lần sau mới so sánh. Không thể làm trong một lần vì chưa biết trung bình khi đang duyệt.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int giaTri = a[0], soLanMax = 0;

    for (int i = 0; i < n; i++) {
        int dem = 0;
        for (int j = 0; j < n; j++) {
            if (a[j] == a[i]) dem++;
        }
        if (dem > soLanMax) { soLanMax = dem; giaTri = a[i]; }
    }

    cout << "Phan tu " << giaTri << " xuat hien " << soLanMax << " lan" << endl;
    return 0;
}
```

Độ phức tạp **O(n²)**. Với `n` lớn, dùng `map` sẽ nhanh hơn:

```cpp
#include <map>
map<int, int> dem;
for (int i = 0; i < n; i++) dem[a[i]]++;

int giaTri = 0, soLanMax = 0;
for (auto [gt, sl] : dem) {
    if (sl > soLanMax) { soLanMax = sl; giaTri = gt; }
}
```

Cách này là **O(n log n)**.

### Bài 3.

```cpp
#include <iostream>
#include <set>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    // Cach 1: O(n^2) - duyet moi cap
    bool coTrung = false;
    for (int i = 0; i < n && !coTrung; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] == a[j]) {
                cout << "Trung lap: a[" << i << "] = a[" << j
                     << "] = " << a[i] << endl;
                coTrung = true;
                break;
            }
        }
    }
    if (!coTrung) cout << "Khong co phan tu trung lap" << endl;

    // Cach 2: O(n log n) dung set
    set<int> tapHop(a, a + n);
    cout << "Kiem tra bang set: "
         << (tapHop.size() < (size_t)n ? "CO trung" : "KHONG trung") << endl;
    return 0;
}
```

💡 **Mẹo dùng `set`:** `set` tự loại phần tử trùng. Nếu `set.size() < n` nghĩa là có ít nhất một phần tử bị loại → có trùng lặp. Đây là cách kiểm tra gọn và nhanh nhất.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int chan[1000], le[1000];
    int soChan = 0, soLe = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) chan[soChan++] = a[i];
        else               le[soLe++]     = a[i];
    }

    cout << "Mang chan (" << soChan << " phan tu): ";
    for (int i = 0; i < soChan; i++) cout << chan[i] << " ";
    cout << endl;

    cout << "Mang le   (" << soLe << " phan tu): ";
    for (int i = 0; i < soLe; i++) cout << le[i] << " ";
    cout << endl;
    return 0;
}
```

💡 Kỹ thuật `chan[soChan++] = a[i]` — gán rồi tăng chỉ số trong một dòng, rất hay dùng khi xây mảng mới.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

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

    cout << "Day con tang dai nhat co " << doDaiMax << " phan tu: ";
    for (int i = batDauMax; i < batDauMax + doDaiMax; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

Ví dụ `{5, 1, 2, 3, 7, 2, 4}` → dãy `1 2 3 7` (4 phần tử).

**Ý tưởng:** đếm độ dài dãy tăng hiện tại; gặp phần tử không tăng thì đặt lại về 1. Luôn cập nhật kỷ lục. Độ phức tạp **O(n)**.

### Bài 6.

```cpp
#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

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

    cout << "Tong lon nhat = " << tongMax << endl;
    cout << "Day con: ";
    for (int i = batDau; i <= ketThuc; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

Ví dụ `{-2, 1, -3, 4, -1, 2, 1, -5, 4}` → tổng lớn nhất **6**, dãy con `4 -1 2 1`.

**Thuật toán Kadane — ý tưởng cốt lõi:** nếu tổng tích luỹ đang **âm**, giữ lại nó chỉ làm kết quả tệ đi, nên vứt bỏ và bắt đầu lại từ phần tử hiện tại.

Độ phức tạp **O(n)** — so với cách duyệt mọi dãy con là O(n²) hoặc O(n³).

### Bài 7.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, k;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "Nhap k: ";
    cin >> k;

    k = ((k % n) + n) % n;              // chuan hoa k, xu ly ca k am va k > n

    // Ky thuat DAO 3 LAN - O(n) thoi gian, O(1) bo nho
    reverse(a, a + n);                  // dao toan bo
    reverse(a, a + k);                  // dao k phan tu dau
    reverse(a + k, a + n);              // dao phan con lai

    cout << "Sau khi xoay phai " << k << " vi tri: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
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

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap so phan tu mang A: "; cin >> n;
    int a[1000];
    cout << "Nhap " << n << " phan tu (da sap xep tang dan): ";
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Nhap so phan tu mang B: "; cin >> m;
    int b[1000];
    cout << "Nhap " << m << " phan tu (da sap xep tang dan): ";
    for (int i = 0; i < m; i++) cin >> b[i];

    int c[2000];
    int i = 0, j = 0, k = 0;

    // Gop bang 2 con tro - O(n + m)
    while (i < n && j < m) {
        if (a[i] <= b[j]) c[k++] = a[i++];
        else              c[k++] = b[j++];
    }
    while (i < n) c[k++] = a[i++];       // phan con lai cua A
    while (j < m) c[k++] = b[j++];       // phan con lai cua B

    cout << "Mang sau khi gop: ";
    for (int t = 0; t < k; t++) cout << c[t] << " ";
    cout << endl;
    return 0;
}
```

Ví dụ: `A = {1,3,5,7}`, `B = {2,4,6}` → `1 2 3 4 5 6 7`

**Kỹ thuật 2 con trỏ:** mỗi lần lấy phần tử nhỏ hơn trong 2 đầu và tiến con trỏ tương ứng. Độ phức tạp **O(n+m)** — tốt hơn hẳn việc nối rồi `sort` (O((n+m)log(n+m))).

Đây chính là bước "trộn" trong thuật toán **Merge Sort**.

### Bài 9.

```cpp
#include <iostream>
#include <algorithm>
#include <unordered_set>
using namespace std;

int main() {
    int n, x;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "Nhap x: ";
    cin >> x;

    // Cach 1: O(n^2) - duyet moi cap
    bool timThay = false;
    for (int i = 0; i < n && !timThay; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] + a[j] == x) {
                cout << "Cach 1: " << a[i] << " + " << a[j] << " = " << x
                     << " (vi tri " << i << ", " << j << ")" << endl;
                timThay = true;
                break;
            }
        }
    }

    // Cach 2: O(n) dung hash set
    unordered_set<int> daGap;
    for (int i = 0; i < n; i++) {
        int can = x - a[i];
        if (daGap.count(can)) {
            cout << "Cach 2: " << can << " + " << a[i] << " = " << x << endl;
            break;
        }
        daGap.insert(a[i]);
    }

    if (!timThay) cout << "Khong tim thay cap nao" << endl;
    return 0;
}
```

**Cách 2 — ý tưởng:** với mỗi phần tử `a[i]`, ta cần tìm `x - a[i]`. Thay vì duyệt lại mảng, ta lưu các phần tử đã gặp vào `unordered_set` và tra cứu trong **O(1)**.

Đây chính là bài **Two Sum** nổi tiếng trên LeetCode.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Cac phan tu dinh: ";
    int dem = 0;
    for (int i = 1; i < n - 1; i++) {        // bo qua 2 dau mut
        if (a[i] > a[i - 1] && a[i] > a[i + 1]) {
            cout << a[i] << "(vt " << i << ") ";
            dem++;
        }
    }
    if (dem == 0) cout << "(khong co)";
    cout << endl;
    return 0;
}
```

Ví dụ `{1, 5, 2, 8, 3, 9, 4}` → đỉnh là `5`, `8`, `9`.

⚠️ Vòng lặp chạy từ `1` tới `n-2` — phần tử đầu và cuối chỉ có 1 phần tử kề nên không xét (tuỳ định nghĩa bài toán).

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    // Ky thuat 2 con tro: j tro toi vi tri tiep theo can dat phan tu khac 0
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != 0) a[j++] = a[i];
    }
    while (j < n) a[j++] = 0;            // dien 0 vao phan con lai

    cout << "Sau khi dich chuyen: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

Ví dụ `{0, 1, 0, 3, 12}` → `1 3 12 0 0`

**Ý tưởng:** duyệt một lần, "dồn" mọi phần tử khác 0 về đầu mảng (giữ nguyên thứ tự), rồi điền 0 vào phần còn lại. Độ phức tạp **O(n)**, bộ nhớ **O(1)**.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

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
        cout << "Khong co 2 phan tu nao bang nhau" << endl;
    } else {
        cout << "Khoang cach lon nhat = " << kcMax
             << " giua a[" << vt1 << "] va a[" << vt2 << "] = " << a[vt1] << endl;
    }
    return 0;
}
```

Ví dụ `{1, 2, 3, 1, 4, 2}` → khoảng cách lớn nhất là 3 (giữa vị trí 0 và 3, giá trị 1).

💡 Cách tối ưu O(n) dùng `map` lưu **vị trí đầu tiên** của mỗi giá trị:

```cpp
map<int,int> lanDau;
int kcMax = -1;
for (int i = 0; i < n; i++) {
    if (lanDau.count(a[i])) kcMax = max(kcMax, i - lanDau[a[i]]);
    else lanDau[a[i]] = i;
}
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;      // day goc co n so tu 1..n, mang chi co n-1 phan tu
    cout << "Nhap n: ";
    cin >> n;

    int a[1000];
    cout << "Nhap " << n - 1 << " phan tu: ";
    for (int i = 0; i < n - 1; i++) cin >> a[i];

    // Cach 1: hieu cua tong
    long long tongDayDu = (long long)n * (n + 1) / 2;
    long long tongThucTe = 0;
    for (int i = 0; i < n - 1; i++) tongThucTe += a[i];
    cout << "Cach 1 (tong): so thieu = " << tongDayDu - tongThucTe << endl;

    // Cach 2: XOR - khong so tran so du n rat lon
    int xorTatCa = 0;
    for (int i = 1; i <= n; i++)    xorTatCa ^= i;
    for (int i = 0; i < n - 1; i++) xorTatCa ^= a[i];
    cout << "Cach 2 (XOR) : so thieu = " << xorTatCa << endl;

    return 0;
}
```

**Cách 1 — hiệu của tổng:** tổng `1+2+...+n = n(n+1)/2`. Trừ đi tổng thực tế là ra số thiếu. Đơn giản nhất.

**Cách 2 — XOR:** dựa vào tính chất `x ^ x = 0` và `x ^ 0 = x`. XOR tất cả số từ 1..n với tất cả phần tử trong mảng: mọi số xuất hiện 2 lần triệt tiêu nhau, chỉ còn lại số thiếu.

**Ưu điểm của XOR:** không bao giờ tràn số, kể cả khi `n` rất lớn.

Cả hai đều **O(n)** thời gian, **O(1)** bộ nhớ.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<bool> daGap(n + 1, false);
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

    cout << "Mang " << (laHoanVi ? "LA" : "KHONG phai")
         << " hoan vi cua 1.." << n << endl;
    return 0;
}
```

**Điều kiện để là hoán vị của `1..n`:**
1. Mọi phần tử nằm trong khoảng `[1, n]`
2. Không có phần tử nào trùng lặp

Dùng **mảng đánh dấu** `daGap` để kiểm tra điều kiện 2 trong O(n). Xem thêm bài [06-06 — Mảng đánh dấu](../06-06-cpp-mang-danh-dau.md).

### Bài 15.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    long long tongToanBo = 0;
    for (int i = 0; i < n; i++) tongToanBo += a[i];

    cout << "Cac diem can bang: ";
    int dem = 0;
    long long tongTrai = 0;

    for (int i = 0; i < n; i++) {
        long long tongPhai = tongToanBo - tongTrai - a[i];
        if (tongTrai == tongPhai) {
            cout << i << " ";
            dem++;
        }
        tongTrai += a[i];
    }

    if (dem == 0) cout << "(khong co)";
    cout << "\nTong cong: " << dem << " diem" << endl;
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
