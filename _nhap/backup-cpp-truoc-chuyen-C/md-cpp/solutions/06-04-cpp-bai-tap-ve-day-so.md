# Lời giải — [C++]. Bài Tập Về Dãy Số

[← Quay lại bài học](../06-04-cpp-bai-tap-ve-day-so.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << "Day so: ";
    for (int i = 1; i <= n; i++) {
        cout << (long long)i * i + 1 << " ";
    }
    cout << endl;
    return 0;
}
```

Với `n = 6`: `2 5 10 17 26 37`

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long a = 1;
    cout << "Day so: ";
    for (int i = 1; i <= n; i++) {
        cout << a << " ";
        a = 2 * a + 3;               // cong thuc truy hoi
    }
    cout << endl;
    return 0;
}
```

Với `n = 8`: `1 5 13 29 61 125 253 509`

💡 Dãy này tăng theo cấp số nhân — chỉ cần `n = 63` là tràn `long long`. Công thức tổng quát: `a[i] = 2^i × 4 − 3`.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    long long t0 = 0, t1 = 0, t2 = 1;

    cout << "Tribonacci: ";
    for (int i = 0; i < n; i++) {
        if      (i == 0) cout << t0 << " ";
        else if (i == 1) cout << t1 << " ";
        else if (i == 2) cout << t2 << " ";
        else {
            long long tiep = t0 + t1 + t2;
            t0 = t1; t1 = t2; t2 = tiep;
            cout << t2 << " ";
        }
    }
    cout << endl;
    return 0;
}
```

Với `n = 12`: `0 0 1 1 2 4 7 13 24 44 81 149`

💡 Chỉ cần giữ **3 số gần nhất** — tương tự Fibonacci giữ 2 số.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    const int N = 15;
    long long C[N];
    C[0] = 1;

    for (int n = 1; n < N; n++) {
        C[n] = 0;
        for (int i = 0; i < n; i++) {
            C[n] += C[i] * C[n - 1 - i];
        }
    }

    cout << "15 so Catalan dau tien:" << endl;
    for (int i = 0; i < N; i++) cout << C[i] << " ";
    cout << endl;
    return 0;
}
```

Output:

```
1 1 2 5 14 42 132 429 1430 4862 16796 58786 208012 742900 2674440 
```

💡 **Số Catalan** xuất hiện ở rất nhiều bài toán đếm:
- Số cách đặt ngoặc hợp lệ với `n` cặp ngoặc
- Số cây nhị phân khác nhau có `n` nút
- Số cách chia đa giác `n+2` cạnh thành các tam giác
- Số đường đi trên lưới không vượt qua đường chéo

Công thức đóng: `C(n) = (2n)! / ((n+1)! × n!)`

### Bài 5.

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
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << n << " so nguyen to dau tien: ";
    int dem = 0;
    for (int so = 2; dem < n; so++) {
        if (laNguyenTo(so)) { cout << so << " "; dem++; }
    }
    cout << endl;
    return 0;
}
```

Với `n = 10`: `2 3 5 7 11 13 17 19 23 29`

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    long long tong = 0;
    cout << n << " so chinh phuong dau tien: ";
    for (int i = 1; i <= n; i++) {
        long long cp = (long long)i * i;
        cout << cp << " ";
        tong += cp;
    }
    cout << "\nTong = " << tong << endl;
    cout << "Cong thuc n(n+1)(2n+1)/6 = "
         << (long long)n * (n + 1) * (2 * n + 1) / 6 << endl;
    return 0;
}
```

Với `n = 5`: `1 4 9 16 25`, tổng = **55**

### Bài 7.

```cpp
#include <iostream>
using namespace std;

long long tongUocThatSu(long long n) {
    if (n <= 1) return 0;
    long long tong = 1;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            tong += i;
            if (i != n / i) tong += n / i;
        }
    }
    return tong;
}

int main() {
    int n;
    cout << "Nhap n (nen <= 4): ";
    cin >> n;

    cout << n << " so hoan hao dau tien: ";
    int dem = 0;
    for (long long so = 2; dem < n; so++) {
        if (tongUocThatSu(so) == so) { cout << so << " "; dem++; }
    }
    cout << endl;
    return 0;
}
```

4 số hoàn hảo đầu: `6 28 496 8128`

⚠️ Số hoàn hảo thứ 5 là **33.550.336** — chương trình sẽ chạy rất lâu nếu `n = 5`.

💡 **Định lý Euclid–Euler:** mọi số hoàn hảo chẵn đều có dạng `2^(p−1) × (2^p − 1)` với `2^p − 1` là số nguyên tố Mersenne. Dùng công thức này sinh nhanh hơn nhiều:

```cpp
// p = 2, 3, 5, 7, 13, 17, 19, 31, ...
// -> 6, 28, 496, 8128, 33550336, ...
```

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long n;
    cout << "Nhap n: ";
    cin >> n;

    if (n < 1) { cout << "n phai duong!" << endl; return 1; }

    long long goc = n;
    int doDai = 1;
    long long maxGiaTri = n;

    cout << "Day Collatz: " << n;
    while (n != 1) {
        n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
        cout << " -> " << n;
        doDai++;
        if (n > maxGiaTri) maxGiaTri = n;
    }

    cout << "\nSo hang dau : " << goc << endl;
    cout << "Do dai day  : " << doDai << endl;
    cout << "Gia tri max : " << maxGiaTri << endl;
    return 0;
}
```

Với `n = 27`, dãy dài **112** bước và đạt giá trị lớn nhất **9232**.

Với `n = 6`:

```
Day Collatz: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
Do dai day  : 9
```

💡 **Giả thuyết Collatz** (bài toán 3n+1) — một trong những bài toán chưa giải được nổi tiếng nhất của toán học: người ta tin rằng **mọi** số nguyên dương đều dẫn về 1, nhưng chưa ai chứng minh được. Đã kiểm chứng bằng máy tính tới 2⁶⁸.

⚠️ Dùng `long long` — giá trị trung gian có thể rất lớn (dù `n` ban đầu nhỏ).

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int doDaiCollatz(long long n) {
    int dem = 1;
    while (n != 1) {
        n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
        dem++;
    }
    return dem;
}

int main() {
    int soTot = 1, doDaiMax = 1;

    for (int n = 1; n <= 1000; n++) {
        int d = doDaiCollatz(n);
        if (d > doDaiMax) { doDaiMax = d; soTot = n; }
    }

    cout << "So co day Collatz dai nhat trong [1, 1000]: " << soTot << endl;
    cout << "Do dai: " << doDaiMax << endl;
    return 0;
}
```

Output:

```
So co day Collatz dai nhat trong [1, 1000]: 871
Do dai: 179
```

💡 **Tối ưu bằng ghi nhớ** — lưu độ dài đã tính để dùng lại:

```cpp
#include <map>
map<long long, int> daBiet;

int doDaiCollatz(long long n) {
    if (n == 1) return 1;
    if (daBiet.count(n)) return daBiet[n];
    long long tiep = (n % 2 == 0) ? n / 2 : 3 * n + 1;
    return daBiet[n] = 1 + doDaiCollatz(tiep);
}
```

Với khoảng [1, 10⁶], cách này nhanh hơn hàng chục lần.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n (toi da 18): ";
    cin >> n;

    long long a = 0;
    cout << "Day so: ";
    for (int i = 1; i <= n; i++) {
        a = a * 10 + 1;              // them chu so 1 vao cuoi
        cout << a << " ";
    }
    cout << endl;
    return 0;
}
```

Với `n = 6`: `1 11 111 1111 11111 111111`

⚠️ Số thứ 19 (`1111111111111111111`) đã vượt `long long`. Cần `string` hoặc số lớn nếu muốn đi xa hơn.

💡 Các số dạng này gọi là **repunit** (repeated unit). Công thức: `R(n) = (10ⁿ − 1)/9`.

### Bài 11.

```cpp
#include <iostream>
#include <string>
using namespace std;

string tiepTheo(const string& s) {
    string kq = "";
    size_t i = 0;
    while (i < s.length()) {
        char c = s[i];
        int dem = 0;
        while (i < s.length() && s[i] == c) { dem++; i++; }
        kq += to_string(dem);
        kq += c;
    }
    return kq;
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    string s = "1";
    for (int i = 1; i <= n; i++) {
        cout << "So hang " << i << ": " << s << endl;
        s = tiepTheo(s);
    }
    return 0;
}
```

Với `n = 7`:

```
So hang 1: 1
So hang 2: 11
So hang 3: 21
So hang 4: 1211
So hang 5: 111221
So hang 6: 312211
So hang 7: 13112221
```

**Cách đọc dãy Look-and-Say:** đọc số hạng trước rồi mô tả nó.

```
1        -> "mot so 1"       -> 11
11       -> "hai so 1"       -> 21
21       -> "mot so 2, mot so 1" -> 1211
1211     -> "mot so 1, mot so 2, hai so 1" -> 111221
```

💡 Độ dài dãy tăng theo hằng số **Conway** ≈ 1,303577. Thú vị: không bao giờ xuất hiện chữ số nào lớn hơn 3 (nếu bắt đầu từ 1, 2 hoặc 3).

### Bài 12.

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
    int n;
    cout << "Nhap n (so cap song sinh can tim): ";
    cin >> n;

    int dem = 0;
    for (int p = 2; dem < n; p++) {
        if (laNguyenTo(p) && laNguyenTo(p + 2)) {
            cout << "Cap " << ++dem << ": (" << p << ", " << p + 2 << ")" << endl;
        }
    }
    return 0;
}
```

Với `n = 8`:

```
Cap 1: (3, 5)
Cap 2: (5, 7)
Cap 3: (11, 13)
Cap 4: (17, 19)
Cap 5: (29, 31)
Cap 6: (41, 43)
Cap 7: (59, 61)
Cap 8: (71, 73)
```

💡 **Giả thuyết số nguyên tố sinh đôi:** có vô hạn cặp như vậy — cũng là một bài toán chưa giải được. Cặp lớn nhất tìm được có gần 400.000 chữ số.

### Bài 13.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;
    double a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    if (n < 3) { cout << "Can it nhat 3 phan tu!" << endl; return 1; }

    const double EPS = 1e-9;

    // Kiem tra cap so CONG: hieu khong doi
    double cong = a[1] - a[0];
    bool laCSC = true;
    for (int i = 2; i < n; i++) {
        if (fabs((a[i] - a[i-1]) - cong) > EPS) { laCSC = false; break; }
    }

    // Kiem tra cap so NHAN: ti so khong doi
    bool laCSN = true;
    if (fabs(a[0]) < EPS) laCSN = false;
    double nhan = 0;
    if (laCSN) {
        nhan = a[1] / a[0];
        for (int i = 2; i < n; i++) {
            if (fabs(a[i-1]) < EPS) { laCSN = false; break; }
            if (fabs((a[i] / a[i-1]) - nhan) > EPS) { laCSN = false; break; }
        }
    }

    if (laCSC) cout << "La CAP SO CONG voi cong sai d = " << cong << endl;
    if (laCSN) cout << "La CAP SO NHAN voi cong boi q = " << nhan << endl;
    if (!laCSC && !laCSN) cout << "Khong phai cap so cong hay cap so nhan" << endl;
    return 0;
}
```

Ví dụ:
- `2 5 8 11 14` → cấp số cộng, `d = 3`
- `3 6 12 24 48` → cấp số nhân, `q = 2`
- `5 5 5 5` → **cả hai** (`d = 0` và `q = 1`)

⚠️ Dùng `fabs(x - y) > EPS` để so sánh số thực, không dùng `!=`.

### Bài 14.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    double a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    if (n < 3) return 1;
    const double EPS = 1e-9;

    double d = a[1] - a[0];
    bool laCSC = true;
    for (int i = 2; i < n; i++)
        if (fabs((a[i] - a[i-1]) - d) > EPS) { laCSC = false; break; }

    cout << fixed << setprecision(4);

    if (laCSC) {
        cout << "Cap so cong: u(n) = " << a[0] << " + (n-1) * " << d << endl;
        cout << "So hang thu 10 = " << a[0] + 9 * d << endl;
        cout << "Tong 10 so hang dau = " << 10 * (2 * a[0] + 9 * d) / 2 << endl;
        return 0;
    }

    if (fabs(a[0]) > EPS) {
        double q = a[1] / a[0];
        bool laCSN = true;
        for (int i = 2; i < n; i++) {
            if (fabs(a[i-1]) < EPS || fabs((a[i]/a[i-1]) - q) > EPS) { laCSN = false; break; }
        }
        if (laCSN) {
            cout << "Cap so nhan: u(n) = " << a[0] << " * " << q << "^(n-1)" << endl;
            cout << "So hang thu 10 = " << a[0] * pow(q, 9) << endl;
            if (fabs(q - 1) > EPS)
                cout << "Tong 10 so hang dau = " << a[0] * (pow(q,10) - 1) / (q - 1) << endl;
            return 0;
        }
    }

    cout << "Khong xac dinh duoc cong thuc tong quat" << endl;
    return 0;
}
```

**Các công thức cần nhớ:**

| | Cấp số cộng | Cấp số nhân |
|---|---|---|
| Số hạng tổng quát | `u(n) = u₁ + (n−1)d` | `u(n) = u₁ · q^(n−1)` |
| Tổng n số hạng đầu | `Sₙ = n(2u₁ + (n−1)d)/2` | `Sₙ = u₁(qⁿ − 1)/(q − 1)`, với q ≠ 1 |

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap so dong: ";
    cin >> n;

    // ① Dong i chua cac so tu 1 den i
    cout << "\n--- Kieu 1 ---" << endl;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) cout << setw(4) << j;
        cout << endl;
    }

    // ② Dong i chua i so lien tiep, noi tiep tu dong truoc
    cout << "\n--- Kieu 2 ---" << endl;
    int so = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) cout << setw(4) << so++;
        cout << endl;
    }

    // ③ Tam giac can, dong i chua cac so tu 1 den i roi giam ve 1
    cout << "\n--- Kieu 3 ---" << endl;
    for (int i = 1; i <= n; i++) {
        cout << setw((n - i) * 2) << "";
        for (int j = 1; j <= i; j++)     cout << setw(2) << j;
        for (int j = i - 1; j >= 1; j--) cout << setw(2) << j;
        cout << endl;
    }

    return 0;
}
```

Với `n = 5`:

```
--- Kieu 1 ---
   1
   1   2
   1   2   3
   1   2   3   4
   1   2   3   4   5

--- Kieu 2 ---
   1
   2   3
   4   5   6
   7   8   9  10
  11  12  13  14  15

--- Kieu 3 ---
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
```

💡 Kiểu 2 chính là dãy **số tam giác**: dòng cuối của dòng thứ `i` là `i(i+1)/2`.
