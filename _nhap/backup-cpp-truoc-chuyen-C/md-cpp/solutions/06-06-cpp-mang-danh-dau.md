# Lời giải — [C++]. Mảng Đánh Dấu

[← Quay lại bài học](../06-06-cpp-mang-danh-dau.md)

> **Mảng đánh dấu (counting array / frequency array):** dùng **giá trị** của phần tử làm **chỉ số** của một mảng phụ. Đổi thời gian tra cứu từ O(n) xuống **O(1)**, với cái giá là bộ nhớ.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    int a[1000];
    int dem[101] = {};              // khoi tao TAT CA bang 0

    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] >= 0 && a[i] <= 100) dem[a[i]]++;    // dung GIA TRI lam CHI SO
    }

    cout << "Tan suat xuat hien:" << endl;
    for (int gt = 0; gt <= 100; gt++) {
        if (dem[gt] > 0) {
            cout << "  " << gt << " xuat hien " << dem[gt] << " lan" << endl;
        }
    }
    return 0;
}
```

⚠️ **Bắt buộc khởi tạo mảng đếm bằng 0:** `int dem[101] = {};`. Nếu không, giá trị rác sẽ làm kết quả sai hoàn toàn.

⚠️ **Luôn kiểm tra biên** `a[i] >= 0 && a[i] <= 100` trước khi dùng làm chỉ số — nếu người dùng nhập 500 hoặc −3 thì chương trình sẽ ghi ra ngoài mảng và crash.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    int dem[1001] = {};

    for (int i = 0; i < n; i++) { cin >> a[i]; dem[a[i]]++; }

    int giaTri = -1, soLanMax = 0;
    for (int gt = 0; gt <= 1000; gt++) {
        if (dem[gt] > soLanMax) { soLanMax = dem[gt]; giaTri = gt; }
    }

    cout << "Phan tu " << giaTri << " xuat hien nhieu nhat: "
         << soLanMax << " lan" << endl;
    return 0;
}
```

💡 **So sánh với cách O(n²)** ở bài [06-02](../06-02-cpp-bai-tap-mang-1-chieu-p1.md) bài 2: cách này chỉ **O(n + M)** với M là phạm vi giá trị. Với `n = 10⁵` và `M = 1000`, nhanh hơn hàng nghìn lần.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    int dem[1001] = {};

    for (int i = 0; i < n; i++) { cin >> a[i]; dem[a[i]]++; }

    cout << "Cac phan tu xuat hien dung 1 lan: ";
    bool co = false;
    for (int i = 0; i < n; i++) {
        if (dem[a[i]] == 1) { cout << a[i] << " "; co = true; }
    }
    if (!co) cout << "(khong co)";
    cout << endl;
    return 0;
}
```

💡 Duyệt theo mảng gốc `a[i]` giữ nguyên **thứ tự xuất hiện**; duyệt theo mảng `dem` sẽ cho thứ tự tăng dần theo giá trị.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    const int MAX = 1000001;
    static bool coMat[MAX] = {};        // static de dat tren vung nho tinh, khong tran stack

    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        if (x >= 0 && x < MAX) coMat[x] = true;
    }

    int nhoNhat = 0;
    while (nhoNhat < MAX && coMat[nhoNhat]) nhoNhat++;

    cout << "So nho nhat khong xuat hien: " << nhoNhat << endl;
    return 0;
}
```

💡 **Dùng `bool` thay `int`** khi chỉ cần biết "có/không" — tiết kiệm 4 lần bộ nhớ.

⚠️ **Từ khoá `static`** đặt mảng lớn vào vùng nhớ tĩnh thay vì stack. Mảng 1 triệu `bool` là 1 MB — nếu đặt trên stack (mặc định) có thể tràn.

Nếu chỉ quan tâm số **dương** nhỏ nhất không xuất hiện, đáp án luôn nằm trong `[1, n+1]`, nên mảng đánh dấu chỉ cần cỡ `n+2`.

### Bài 5.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    vector<bool> daGap(n + 1, false);
    bool laHoanVi = true;

    for (int i = 0; i < n; i++) {
        if (a[i] < 1 || a[i] > n)  { laHoanVi = false; break; }   // ngoai pham vi
        if (daGap[a[i]])           { laHoanVi = false; break; }   // trung lap
        daGap[a[i]] = true;
    }

    cout << "Mang " << (laHoanVi ? "LA" : "KHONG phai")
         << " hoan vi cua 1.." << n << endl;
    return 0;
}
```

Độ phức tạp **O(n)**, tốt hơn cách sắp xếp rồi so sánh (O(n log n)).

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    bool daGap[1001] = {};
    int m = 0;

    for (int i = 0; i < n; i++) {
        if (!daGap[a[i]]) {
            daGap[a[i]] = true;
            a[m++] = a[i];              // giu lai lan xuat hien DAU TIEN
        }
    }
    n = m;

    cout << "Sau khi loai trung lap: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

Độ phức tạp **O(n)** — tốt hơn hẳn cách O(n²) ở bài [06-05](../06-05-cpp-chen-va-xoa-phan-tu.md) bài 6.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cout << "So phan tu mang A: "; cin >> n;
    int a[1000];
    bool coTrongA[1001] = {};
    for (int i = 0; i < n; i++) { cin >> a[i]; coTrongA[a[i]] = true; }

    cout << "So phan tu mang B: "; cin >> m;
    int b[1000];
    for (int i = 0; i < m; i++) cin >> b[i];

    bool daIn[1001] = {};
    cout << "Cac phan tu chung: ";
    for (int i = 0; i < m; i++) {
        if (coTrongA[b[i]] && !daIn[b[i]]) {
            cout << b[i] << " ";
            daIn[b[i]] = true;          // tranh in trung
        }
    }
    cout << endl;
    return 0;
}
```

💡 Mảng `daIn` thứ hai đảm bảo mỗi giá trị chung chỉ in **một lần**, dù nó xuất hiện nhiều lần trong B.

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int dem[26] = {};

    for (char c : s) {
        if (isalpha((unsigned char)c)) {
            dem[tolower(c) - 'a']++;         // 'a' -> 0, 'b' -> 1, ...
        }
    }

    cout << "Tan suat cac chu cai:" << endl;
    for (int i = 0; i < 26; i++) {
        if (dem[i] > 0) {
            cout << "  " << (char)('a' + i) << ": " << dem[i] << endl;
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

```cpp
int chiSo = c - 'a';              // 'a'..'z'  ->  0..25
char kyTu = 'a' + chiSo;          // 0..25     ->  'a'..'z'
```

Áp dụng được vì các chữ cái nằm liên tiếp trong bảng ASCII.

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool laDaoChu(const string& s1, const string& s2) {
    int dem[26] = {};

    for (char c : s1) if (isalpha((unsigned char)c)) dem[tolower(c) - 'a']++;
    for (char c : s2) if (isalpha((unsigned char)c)) dem[tolower(c) - 'a']--;

    for (int i = 0; i < 26; i++) if (dem[i] != 0) return false;
    return true;
}

int main() {
    string s1, s2;
    cout << "Chuoi 1: "; getline(cin, s1);
    cout << "Chuoi 2: "; getline(cin, s2);

    cout << (laDaoChu(s1, s2) ? "LA dao chu" : "KHONG phai dao chu") << endl;
    return 0;
}
```

Ví dụ:
- `"listen"` và `"silent"` → **LÀ đảo chữ**
- `"Dormitory"` và `"Dirty Room"` → **LÀ đảo chữ**
- `"hello"` và `"world"` → không

💡 **Kỹ thuật thanh lịch:** dùng **một** mảng đếm, chuỗi 1 **cộng**, chuỗi 2 **trừ**. Nếu hai chuỗi là đảo chữ thì tất cả về 0. Chỉ cần O(n) thời gian và O(26) bộ nhớ.

Cách khác (chậm hơn): sắp xếp cả hai chuỗi rồi so sánh — O(n log n).

### Bài 10.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    vector<int> a(n);
    vector<int> dem(n + 1, 0);

    cout << "Nhap " << n << " phan tu (1.." << n << "): ";
    for (int i = 0; i < n; i++) { cin >> a[i]; dem[a[i]]++; }

    int lap = -1, thieu = -1;
    for (int gt = 1; gt <= n; gt++) {
        if (dem[gt] == 2) lap   = gt;
        if (dem[gt] == 0) thieu = gt;
    }

    cout << "So bi lap   : " << lap   << endl;
    cout << "So bi thieu : " << thieu << endl;
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

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void countingSort(vector<int>& a) {
    if (a.empty()) return;

    int mn = *min_element(a.begin(), a.end());
    int mx = *max_element(a.begin(), a.end());
    int phamVi = mx - mn + 1;

    vector<int> dem(phamVi, 0);
    for (int x : a) dem[x - mn]++;          // tru mn de chi so bat dau tu 0

    int k = 0;
    for (int i = 0; i < phamVi; i++) {
        for (int j = 0; j < dem[i]; j++) {
            a[k++] = i + mn;                // cong lai mn de tra ve gia tri goc
        }
    }
}

int main() {
    vector<int> a = {5, 2, 9, 2, 7, 1, 5, 2};

    cout << "Ban dau : ";
    for (int x : a) cout << x << " ";
    cout << endl;

    countingSort(a);

    cout << "Sau sort: ";
    for (int x : a) cout << x << " ";
    cout << endl;
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

⚠️ Với mảng 10 phần tử nhưng giá trị từ 1 đến 10⁹, cần mảng đếm 10⁹ phần tử — **hoàn toàn không khả thi**. Khi đó phải dùng `sort` thông thường.

**Ứng dụng thực tế:** sắp xếp điểm số (0–10), tuổi (0–150), tần suất ký tự, xếp hạng.

### Bài 12.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int N = 1000000;
    vector<bool> laNguyenTo(N + 1, true);
    laNguyenTo[0] = laNguyenTo[1] = false;

    for (int i = 2; (long long)i * i <= N; i++) {
        if (laNguyenTo[i]) {
            for (long long j = (long long)i * i; j <= N; j += i) {
                laNguyenTo[j] = false;          // DANH DAU la hop so
            }
        }
    }

    int dem = 0;
    for (int i = 2; i <= N; i++) if (laNguyenTo[i]) dem++;

    cout << "So luong so nguyen to <= " << N << ": " << dem << endl;

    cout << "20 so dau: ";
    int in = 0;
    for (int i = 2; i <= N && in < 20; i++)
        if (laNguyenTo[i]) { cout << i << " "; in++; }
    cout << endl;
    return 0;
}
```

**Sàng Eratosthenes chính là ứng dụng kinh điển nhất của mảng đánh dấu:** thay vì kiểm tra từng số một (O(n√n)), ta dùng một mảng `bool` để **gạch** bội của từng số nguyên tố — chỉ O(n log log n).

💡 `vector<bool>` được C++ nén thành bit, nên sàng 10⁶ chỉ tốn ~125 KB thay vì 1 MB.

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    const int MAX = 100001;
    static int soLuong[MAX] = {};         // luu SO LUONG thay vi bool

    int q;
    cout << "Nhap so thao tac: ";
    cin >> q;

    cout << "Cac thao tac (+x them, -x xoa, ?x truy van):" << endl;
    while (q--) {
        char op;
        int x;
        cin >> op >> x;

        if (x < 0 || x >= MAX) { cout << "  Gia tri ngoai pham vi!" << endl; continue; }

        if (op == '+') {
            soLuong[x]++;
            cout << "  Da them " << x << endl;
        } else if (op == '-') {
            if (soLuong[x] > 0) { soLuong[x]--; cout << "  Da xoa " << x << endl; }
            else cout << "  " << x << " khong co trong tap!" << endl;
        } else if (op == '?') {
            cout << "  " << x << ": " << (soLuong[x] > 0 ? "CO" : "KHONG")
                 << " (so luong = " << soLuong[x] << ")" << endl;
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

💡 **Dùng `int` (đếm số lượng) thay vì `bool`** cho phép xử lý đúng trường hợp thêm cùng một giá trị nhiều lần — giống `multiset`. Nếu chỉ cần tập hợp không trùng, `bool` là đủ.

Mọi thao tác đều **O(1)**.

### Bài 14.

| Tiêu chí | Mảng đánh dấu | `set` / `map` | `unordered_set` / `unordered_map` |
|---|---|---|---|
| **Thời gian tra cứu** | **O(1)** — nhanh nhất | O(log n) | O(1) trung bình |
| **Bộ nhớ** | O(phạm vi giá trị) | O(số phần tử) | O(số phần tử) |
| **Giới hạn giá trị** | ⚠️ Phải biết trước và hẹp | ✅ Không giới hạn | ✅ Không giới hạn |
| **Kiểu dữ liệu** | ⚠️ Chỉ số nguyên nhỏ | ✅ Mọi kiểu so sánh được | ✅ Mọi kiểu băm được |
| **Giá trị âm** | ⚠️ Phải dịch chỉ số | ✅ Được | ✅ Được |
| **Duyệt theo thứ tự** | ✅ Tự nhiên (tăng dần) | ✅ Có | ❌ Không |
| **Hằng số nhân** | Rất nhỏ | Lớn | Trung bình |

**✅ Dùng MẢNG ĐÁNH DẤU khi:**
- Giá trị là số nguyên trong phạm vi hẹp (≤ 10⁷)
- Cần tốc độ tối đa (lập trình thi đấu)
- Ví dụ: đếm tần suất chữ cái (26 ô), điểm số (0–10), sàng nguyên tố

**✅ Dùng `set`/`map` khi:**
- Giá trị rải rác hoặc rất lớn (`long long`, `string`)
- Cần duyệt theo thứ tự
- Số phần tử ít hơn nhiều so với phạm vi giá trị

**Ví dụ minh hoạ sự khác biệt:**

```cpp
// 5 phan tu: {1, 1000000000, 5, 999999999, 3}

int dem[1000000001];            // 4 GB -> KHONG KHA THI
map<int,int> dem;               // ~200 byte -> DUNG CACH NAY
```

```cpp
// 10^6 phan tu, gia tri trong [0, 100]

int dem[101];                   // 404 byte, O(1) -> TOI UU
map<int,int> dem;               // cham hon ~10 lan
```

💡 **Mẹo xử lý giá trị âm với mảng đánh dấu** — dịch chỉ số:

```cpp
const int OFFSET = 1000;        // gia tri tu -1000 den 1000
int dem[2001] = {};
dem[x + OFFSET]++;              // x = -5  ->  dem[995]++
```

### Bài 15.

```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, maxToaDo;
    cout << "Nhap so khoang va toa do lon nhat: ";
    cin >> n >> maxToaDo;

    vector<int> saiPhan(maxToaDo + 2, 0);

    cout << "Nhap " << n << " khoang [l, r]:" << endl;
    for (int i = 0; i < n; i++) {
        int l, r;
        cin >> l >> r;
        saiPhan[l]     += 1;          // bat dau bao phu tu l
        saiPhan[r + 1] -= 1;          // ket thuc bao phu sau r
    }

    // Tinh tong tien to de ra so lan bao phu thuc te
    cout << "\nSo lan bao phu tai moi diem:" << endl;
    int hienTai = 0, maxBaoPhu = 0, diemMax = 0;

    for (int i = 0; i <= maxToaDo; i++) {
        hienTai += saiPhan[i];
        cout << "  Diem " << i << ": " << hienTai << endl;
        if (hienTai > maxBaoPhu) { maxBaoPhu = hienTai; diemMax = i; }
    }

    cout << "\nDiem duoc bao phu nhieu nhat: " << diemMax
         << " (" << maxBaoPhu << " khoang)" << endl;
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
