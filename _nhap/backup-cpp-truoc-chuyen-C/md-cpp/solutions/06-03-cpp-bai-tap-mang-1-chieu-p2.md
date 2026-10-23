# Lời giải — [C++]. Bài Tập Mảng 1 Chiều P2

[← Quay lại bài học](../06-03-cpp-bai-tap-mang-1-chieu-p2.md)

---

### Bài 1.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

void inMang(int a[], int n) {
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    cout << "Ban dau : "; inMang(a, n);

    for (int i = 0; i < n - 1; i++) {
        bool coDoiCho = false;
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j + 1]);
                coDoiCho = true;
            }
        }
        cout << "Luot " << i + 1 << " : "; inMang(a, n);

        if (!coDoiCho) {              // TOI UU: khong doi cho nao -> da sap xep xong
            cout << "(Da sap xep xong, dung som)" << endl;
            break;
        }
    }
    return 0;
}
```

Output:

```
Ban dau : 5 2 9 1 7 
Luot 1 : 2 5 1 7 9 
Luot 2 : 2 1 5 7 9 
Luot 3 : 1 2 5 7 9 
Luot 4 : 1 2 5 7 9 
(Da sap xep xong, dung som)
```

**Bubble Sort — nguyên lý:** so sánh từng cặp kề nhau, đổi chỗ nếu sai thứ tự. Sau mỗi lượt, phần tử lớn nhất "nổi" về cuối.

**Tối ưu bằng cờ `coDoiCho`:** nếu một lượt không có phép đổi chỗ nào thì mảng đã sắp xếp xong. Nhờ đó, với mảng đã sắp sẵn, độ phức tạp là **O(n)** thay vì O(n²).

### Bài 2.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    for (int i = 0; i < n - 1; i++) {
        int viTriMin = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[viTriMin]) viTriMin = j;
        }
        if (viTriMin != i) swap(a[i], a[viTriMin]);

        cout << "Buoc " << i + 1 << ": ";
        for (int k = 0; k < n; k++) cout << a[k] << " ";
        cout << endl;
    }
    return 0;
}
```

**Selection Sort — nguyên lý:** ở bước thứ `i`, tìm phần tử **nhỏ nhất** trong phần chưa sắp xếp và đưa nó về vị trí `i`.

💡 **Ưu điểm lớn nhất:** số phép **đổi chỗ** chỉ tối đa `n−1` — ít nhất trong các thuật toán O(n²). Hữu ích khi việc đổi chỗ tốn kém (ví dụ phần tử là struct lớn).

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[] = {5, 2, 9, 1, 7};
    int n = 5;

    for (int i = 1; i < n; i++) {
        int khoa = a[i];
        int j = i - 1;

        // Day cac phan tu lon hon khoa sang phai
        while (j >= 0 && a[j] > khoa) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = khoa;              // chen khoa vao dung cho

        cout << "Buoc " << i << ": ";
        for (int k = 0; k < n; k++) cout << a[k] << " ";
        cout << endl;
    }
    return 0;
}
```

**Insertion Sort — nguyên lý:** giống cách bạn xếp bài trên tay. Lấy từng phần tử và **chèn** nó vào đúng vị trí trong phần đã sắp xếp phía trước.

💡 **Ưu điểm:** với mảng **gần như đã sắp xếp**, độ phức tạp chỉ **O(n)** — nhanh nhất trong 3 thuật toán. Đây là lý do `std::sort` dùng Insertion Sort cho các đoạn nhỏ.

### Bài 4.

```cpp
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 10;
int goc[N] = {5, 2, 9, 1, 7, 3, 8, 6, 4, 0};

void bubbleSort(int a[], int n, long long& soSanh, long long& doiCho) {
    soSanh = doiCho = 0;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++) {
            soSanh++;
            if (a[j] > a[j + 1]) { swap(a[j], a[j + 1]); doiCho++; }
        }
}

void selectionSort(int a[], int n, long long& soSanh, long long& doiCho) {
    soSanh = doiCho = 0;
    for (int i = 0; i < n - 1; i++) {
        int vtMin = i;
        for (int j = i + 1; j < n; j++) {
            soSanh++;
            if (a[j] < a[vtMin]) vtMin = j;
        }
        if (vtMin != i) { swap(a[i], a[vtMin]); doiCho++; }
    }
}

void insertionSort(int a[], int n, long long& soSanh, long long& doiCho) {
    soSanh = doiCho = 0;
    for (int i = 1; i < n; i++) {
        int khoa = a[i], j = i - 1;
        while (j >= 0) {
            soSanh++;
            if (a[j] <= khoa) break;
            a[j + 1] = a[j];
            doiCho++;
            j--;
        }
        a[j + 1] = khoa;
    }
}

int main() {
    int a[N];
    long long ss, dc;

    memcpy(a, goc, sizeof(goc));
    bubbleSort(a, N, ss, dc);
    cout << "Bubble Sort    : " << ss << " so sanh, " << dc << " doi cho" << endl;

    memcpy(a, goc, sizeof(goc));
    selectionSort(a, N, ss, dc);
    cout << "Selection Sort : " << ss << " so sanh, " << dc << " doi cho" << endl;

    memcpy(a, goc, sizeof(goc));
    insertionSort(a, N, ss, dc);
    cout << "Insertion Sort : " << ss << " so sanh, " << dc << " phep dich" << endl;
    return 0;
}
```

Kết quả tham khảo (n = 10, mảng ngẫu nhiên):

```
Bubble Sort    : 45 so sanh, 22 doi cho
Selection Sort : 45 so sanh, 8 doi cho
Insertion Sort : 31 so sanh, 22 phep dich
```

**Bảng tổng hợp:**

| Thuật toán | Tốt nhất | Trung bình | Xấu nhất | Đổi chỗ | Ổn định? |
|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | Nhiều | ✅ Có |
| Selection | O(n²) | O(n²) | O(n²) | **Ít nhất** (n−1) | ❌ Không |
| Insertion | **O(n)** | O(n²) | O(n²) | Nhiều | ✅ Có |
| `std::sort` | O(n log n) | O(n log n) | O(n log n) | — | ❌ Không |

✅ Trong thực tế **luôn dùng `std::sort`**. Học 3 thuật toán trên để hiểu nguyên lý và rèn tư duy.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int b[1000], m = 0;

    for (int i = 0; i < n; i++) {
        bool daCo = false;
        for (int j = 0; j < m; j++) {
            if (b[j] == a[i]) { daCo = true; break; }
        }
        if (!daCo) b[m++] = a[i];
    }

    cout << "Sau khi loai trung lap (" << m << " phan tu): ";
    for (int i = 0; i < m; i++) cout << b[i] << " ";
    cout << endl;
    return 0;
}
```

Ví dụ `{1, 3, 1, 5, 3, 7}` → `1 3 5 7`

💡 Cách nhanh hơn với `unordered_set` — **O(n)** thay vì O(n²):

```cpp
#include <unordered_set>
unordered_set<int> daGap;
int m = 0;
for (int i = 0; i < n; i++) {
    if (daGap.insert(a[i]).second) b[m++] = a[i];
}
```

`insert` trả về `pair<iterator, bool>`, phần `.second` là `true` nếu phần tử **chưa** có.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int kq = 0;
    for (int i = 0; i < n; i++) kq ^= a[i];

    cout << "Phan tu xuat hien 1 lan: " << kq << endl;
    return 0;
}
```

Ví dụ `{4, 1, 2, 1, 2}` → `4`

**Nguyên lý XOR:**

| Tính chất | Ý nghĩa |
|---|---|
| `x ^ x = 0` | Hai số giống nhau triệt tiêu |
| `x ^ 0 = x` | XOR với 0 giữ nguyên |
| `a ^ b = b ^ a` | Giao hoán — thứ tự không quan trọng |

Nên khi XOR tất cả phần tử: mọi cặp trùng nhau triệt tiêu về 0, chỉ còn lại phần tử đơn lẻ.

```
4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1^1) ^ (2^2)
= 4 ^ 0 ^ 0
= 4  ✔
```

💡 **O(n) thời gian, O(1) bộ nhớ** — tốt hơn hẳn dùng `map` đếm số lần (O(n) bộ nhớ).

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1001];
    for (int i = 1; i <= n; i++) cin >> a[i];       // danh so tu 1 cho tien

    // Xay mang tong tien to: pre[i] = a[1] + a[2] + ... + a[i]
    long long pre[1001];
    pre[0] = 0;
    for (int i = 1; i <= n; i++) pre[i] = pre[i - 1] + a[i];

    int q;
    cout << "So truy van: ";
    cin >> q;

    while (q--) {
        int l, r;
        cout << "Nhap l r: ";
        cin >> l >> r;
        // Tong tu l den r = pre[r] - pre[l-1]  -> O(1)
        cout << "  Tong tu " << l << " den " << r << " = "
             << pre[r] - pre[l - 1] << endl;
    }
    return 0;
}
```

**Kỹ thuật tổng tiền tố (prefix sum):**

```
a   :      3   1   4   1   5   9
pre : 0    3   4   8   9  14  23
       0   1   2   3   4   5   6

Tong tu 2 den 4 = pre[4] - pre[1] = 9 - 3 = 6   (= 1 + 4 + 1) ✔
```

**Hiệu quả:**

| | Tính trực tiếp | Prefix sum |
|---|---|---|
| Tiền xử lý | 0 | O(n), một lần |
| Mỗi truy vấn | O(n) | **O(1)** |
| 10⁵ truy vấn trên mảng 10⁵ | 10¹⁰ bước (quá chậm) | 2×10⁵ bước |

💡 **Mẹo đánh chỉ số từ 1** giúp công thức `pre[r] - pre[l-1]` hoạt động mà không cần xét trường hợp đặc biệt `l = 0`.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    long long S;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "Nhap S: ";
    cin >> S;

    // Ky thuat CUA SO TRUOT - chi dung cho mang toan so DUONG
    int trai = 0;
    long long tong = 0;
    bool timThay = false;

    for (int phai = 0; phai < n; phai++) {
        tong += a[phai];

        while (tong > S && trai <= phai) {
            tong -= a[trai];
            trai++;
        }

        if (tong == S) {
            cout << "Tim thay day con tu vi tri " << trai << " den " << phai << ": ";
            for (int i = trai; i <= phai; i++) cout << a[i] << " ";
            cout << endl;
            timThay = true;
            break;
        }
    }

    if (!timThay) cout << "Khong tim thay" << endl;
    return 0;
}
```

Ví dụ `{1, 4, 20, 3, 10, 5}` với `S = 33` → dãy `20 3 10` (vị trí 2–4).

**Kỹ thuật cửa sổ trượt (sliding window):** mở rộng cửa sổ bên phải khi tổng còn nhỏ, thu hẹp bên trái khi tổng quá lớn. Độ phức tạp **O(n)**.

⚠️ **Chỉ đúng với mảng toàn số dương.** Nếu có số âm, phải dùng prefix sum + `map`:

```cpp
map<long long,int> viTri;
viTri[0] = -1;
long long tong = 0;
for (int i = 0; i < n; i++) {
    tong += a[i];
    if (viTri.count(tong - S)) { /* tim thay tu viTri[tong-S]+1 den i */ }
    if (!viTri.count(tong)) viTri[tong] = i;
}
```

### Bài 9.

```cpp
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int n, k;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];
    cout << "Nhap k: ";
    cin >> k;

    if (k > n) k = n;

    // Cach 1: sap xep giam dan roi lay k dau - O(n log n)
    vector<int> b = a;
    sort(b.begin(), b.end(), greater<int>());
    cout << k << " phan tu lon nhat: ";
    for (int i = 0; i < k; i++) cout << b[i] << " ";
    cout << endl;

    // Cach 2: nth_element - O(n) trung binh, chi sap xep DU dung
    vector<int> c = a;
    nth_element(c.begin(), c.begin() + k, c.end(), greater<int>());
    cout << "Cach 2 (nth_element): ";
    for (int i = 0; i < k; i++) cout << c[i] << " ";
    cout << endl;

    return 0;
}
```

💡 **`nth_element`** sắp xếp "một phần": nó chỉ đảm bảo phần tử thứ `k` nằm đúng vị trí và mọi phần tử trước nó đều lớn hơn (với `greater`). Nhanh hơn `sort` khi `k` nhỏ so với `n`.

Với `k` rất nhỏ và `n` rất lớn, dùng `priority_queue` (heap) kích thước `k` là tối ưu nhất: **O(n log k)**.

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    sort(a.begin(), a.end());

    cout << "Mang sau sap xep: ";
    for (int x : a) cout << x << " ";
    cout << endl;

    cout << fixed << setprecision(2);
    if (n % 2 == 1) {
        cout << "Trung vi = " << a[n / 2] << endl;              // le: phan tu giua
    } else {
        cout << "Trung vi = " << (a[n/2 - 1] + a[n/2]) / 2.0 << endl;   // chan: TB 2 phan tu giua
    }
    return 0;
}
```

Ví dụ:
- `{1, 3, 5, 7, 9}` (n lẻ) → trung vị = **5**
- `{1, 3, 5, 7}` (n chẵn) → trung vị = (3+5)/2 = **4.00**

💡 **Trung vị vs Trung bình:** trung vị **không bị ảnh hưởng** bởi các giá trị ngoại lai. Với `{1, 2, 3, 4, 1000}`, trung bình là 202 (không đại diện được cho dữ liệu) nhưng trung vị là 3 (hợp lý hơn). Đây là lý do thống kê thu nhập thường dùng trung vị.

### Bài 11.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <random>
#include <chrono>
using namespace std;

int main() {
    vector<int> a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int n = a.size();

    // Bo sinh so ngau nhien chat luong tot (C++11)
    unsigned seed = chrono::steady_clock::now().time_since_epoch().count();
    mt19937 rng(seed);

    // Thuat toan Fisher-Yates
    for (int i = n - 1; i > 0; i--) {
        uniform_int_distribution<int> phanBo(0, i);
        int j = phanBo(rng);
        swap(a[i], a[j]);
    }

    cout << "Sau khi tron: ";
    for (int x : a) cout << x << " ";
    cout << endl;

    // C++ co san ham shuffle
    shuffle(a.begin(), a.end(), rng);
    cout << "Dung shuffle: ";
    for (int x : a) cout << x << " ";
    cout << endl;
    return 0;
}
```

**Thuật toán Fisher-Yates:** duyệt từ cuối về đầu, mỗi bước đổi chỗ phần tử `i` với một phần tử ngẫu nhiên trong khoảng `[0, i]`.

**Đây là thuật toán trộn ĐÚNG duy nhất** — mọi hoán vị đều có xác suất bằng nhau (1/n!).

⚠️ **Cách trộn SAI thường gặp:**

```cpp
for (int i = 0; i < n; i++) swap(a[i], a[rand() % n]);   // KHONG deu!
```

Cách này tạo ra nⁿ khả năng, không chia hết cho n! nên một số hoán vị xuất hiện nhiều hơn.

💡 Nên dùng `mt19937` thay `rand()` — `rand()` có chất lượng ngẫu nhiên kém.

### Bài 12.

```cpp
#include <iostream>
#include <cstdlib>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    long long tongAll = 0;
    for (int x : a) tongAll += x;

    long long hieuMin = tongAll;      // khoi tao bang truong hop xau nhat
    int maskTot = 0;

    // Vet can 2^n cach chia (chi dung voi n <= 20)
    for (int mask = 0; mask < (1 << n); mask++) {
        long long tong1 = 0;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) tong1 += a[i];
        }
        long long tong2 = tongAll - tong1;
        long long hieu = llabs(tong1 - tong2);

        if (hieu < hieuMin) { hieuMin = hieu; maskTot = mask; }
    }

    cout << "Nhom 1: ";
    long long t1 = 0;
    for (int i = 0; i < n; i++) if (maskTot & (1 << i))  { cout << a[i] << " "; t1 += a[i]; }
    cout << "(tong = " << t1 << ")" << endl;

    cout << "Nhom 2: ";
    for (int i = 0; i < n; i++) if (!(maskTot & (1 << i))) cout << a[i] << " ";
    cout << "(tong = " << tongAll - t1 << ")" << endl;
    cout << "Chenh lech = " << hieuMin << endl;
    return 0;
}
```

**Kỹ thuật duyệt tập con bằng bitmask:** mỗi số `mask` từ 0 đến 2ⁿ−1 đại diện cho một cách chọn. Bit thứ `i` bằng 1 nghĩa là phần tử `i` thuộc nhóm 1.

```
n = 3, mask = 5 = binary 101
-> chon phan tu 0 va 2
```

⚠️ Độ phức tạp **O(2ⁿ × n)** — chỉ dùng được với `n ≤ 20`. Với `n` lớn, đây là bài toán NP-khó, phải dùng quy hoạch động (bài toán **Partition Problem**).

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    long long dem = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (a[i] > a[j]) dem++;
        }
    }

    cout << "So cap nghich the = " << dem << endl;

    // So cap nghich the toi da (mang sap xep nguoc hoan toan)
    cout << "Toi da co the co  = " << (long long)n * (n - 1) / 2 << endl;
    return 0;
}
```

Ví dụ `{2, 4, 1, 3, 5}` → 3 cặp nghịch thế: `(2,1)`, `(4,1)`, `(4,3)`

💡 **Ý nghĩa:** số cặp nghịch thế đo mức độ "lộn xộn" của mảng.
- Mảng đã sắp xếp → 0 cặp
- Mảng sắp ngược hoàn toàn → `n(n−1)/2` cặp (tối đa)
- Đây cũng chính là **số phép đổi chỗ** mà Bubble Sort cần thực hiện

⚠️ Cách trên là O(n²). Có thể giảm xuống **O(n log n)** bằng cách cải tiến Merge Sort hoặc dùng Binary Indexed Tree.

### Bài 14.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    if (n == 0) return 0;

    cout << "Ma hoa RLE: ";
    int i = 0;
    while (i < n) {
        int giaTri = a[i];
        int dem = 0;
        while (i < n && a[i] == giaTri) { dem++; i++; }

        cout << giaTri << "x" << dem;
        if (i < n) cout << ", ";
    }
    cout << endl;
    return 0;
}
```

Ví dụ `{1,1,1,2,2,3}` → `1x3, 2x2, 3x1`

**Run-Length Encoding (RLE)** là thuật toán nén đơn giản nhất — thay vì lưu từng phần tử, ta lưu "giá trị × số lần lặp".

**Hiệu quả:**
- `{1,1,1,1,1,1,1,1}` → `1x8` — nén rất tốt
- `{1,2,3,4,5,6,7,8}` → `1x1, 2x1, ...` — **phình to hơn** bản gốc

RLE được dùng trong định dạng ảnh BMP, fax, và các dữ liệu có nhiều đoạn lặp lại.

### Bài 15.

```cpp
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cout << "So phan tu mang A: "; cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "So phan tu mang B: "; cin >> m;
    vector<int> b(m);
    for (int i = 0; i < m; i++) cin >> b[i];

    // Cach 1: dung set (tu dong loai trung + sap xep)
    set<int> tapA(a.begin(), a.end());
    set<int> tapB(b.begin(), b.end());

    cout << "Giao (A n B): ";
    for (int x : tapA) if (tapB.count(x)) cout << x << " ";
    cout << endl;

    cout << "Hop (A u B): ";
    set<int> hop = tapA;
    hop.insert(tapB.begin(), tapB.end());
    for (int x : hop) cout << x << " ";
    cout << endl;

    cout << "Hieu (A \\ B): ";
    for (int x : tapA) if (!tapB.count(x)) cout << x << " ";
    cout << endl;

    // Cach 2: dung ham STL co san (yeu cau mang DA SAP XEP)
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    vector<int> giao, hop2;

    set_intersection(a.begin(), a.end(), b.begin(), b.end(), back_inserter(giao));
    set_union(a.begin(), a.end(), b.begin(), b.end(), back_inserter(hop2));

    cout << "Giao (STL): ";
    for (int x : giao) cout << x << " ";
    cout << endl;

    return 0;
}
```

Ví dụ `A = {1,2,3,4}`, `B = {3,4,5,6}`:

```
Giao (A n B): 3 4 
Hop (A u B): 1 2 3 4 5 6 
Hieu (A \ B): 1 2 
```

💡 **Các hàm tập hợp trong `<algorithm>`** (đều yêu cầu dãy đã sắp xếp):

| Hàm | Ý nghĩa |
|---|---|
| `set_intersection` | Giao — phần tử có ở **cả hai** |
| `set_union` | Hợp — phần tử có ở **ít nhất một** |
| `set_difference` | Hiệu A\B — có ở A nhưng không ở B |
| `set_symmetric_difference` | Hiệu đối xứng — có ở đúng một trong hai |

`back_inserter` là một iterator đặc biệt, tự động gọi `push_back` thay vì ghi đè.
