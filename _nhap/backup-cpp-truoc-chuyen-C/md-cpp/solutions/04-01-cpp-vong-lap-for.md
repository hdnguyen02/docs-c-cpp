# Lời giải — [C++]. Vòng Lặp For

[← Quay lại bài học](../04-01-cpp-vong-lap-for.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```

**Cấu trúc `for`:**

```
for (khoi_tao ; dieu_kien ; cap_nhat) { than_vong_lap }
      ↑ chay 1 lan   ↑ kiem tra     ↑ chay sau moi
      dau tien       truoc moi      lan lap
                     lan lap
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = n; i >= 1; i--) {
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    long long S = 0;              // dung long long de tranh tran voi n lon
    for (int i = 1; i <= n; i++) {
        S += i;
    }

    cout << "S = " << S << endl;
    // Kiem chung bang cong thuc Gauss
    cout << "Cong thuc: " << (long long)n * (n + 1) / 2 << endl;
    return 0;
}
```

💡 **Công thức Gauss:** `1 + 2 + ... + n = n(n+1)/2`. Với `n = 10⁶`, vòng lặp chạy 1 triệu bước còn công thức chỉ 1 phép tính.

⚠️ `S` phải là `long long`: với `n = 100000`, `S ≈ 5×10⁹` đã vượt `int`.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n < 0) { cout << "n phai khong am!" << endl; return 1; }

    unsigned long long gt = 1;
    for (int i = 2; i <= n; i++) {
        gt *= i;
    }

    cout << n << "! = " << gt << endl;
    return 0;
}
```

**Giới hạn kiểu dữ liệu với giai thừa:**

| Kiểu | Tính đúng tới |
|---|---|
| `int` (4 byte) | 12! = 479.001.600 |
| `long long` (8 byte) | **20!** = 2.432.902.008.176.640.000 |
| `unsigned long long` | 20! (21! vẫn tràn) |
| `double` | ~170! (mất độ chính xác) |

Từ `21!` trở đi phải dùng **số lớn** (big integer) — lưu từng chữ số vào mảng.

⚠️ `0! = 1` theo định nghĩa — vòng lặp trên xử lý đúng vì bắt đầu từ `i = 2` nên không chạy lần nào, `gt` giữ nguyên 1.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int dem = 0;
    // Cach 1: duyet tat ca, kiem tra chan
    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            cout << i << " ";
            dem++;
        }
    }
    cout << "\nCo " << dem << " so chan" << endl;

    // Cach 2: nhay 2 buoc - NHANH GAP DOI
    cout << "Cach 2: ";
    for (int i = 2; i <= n; i += 2) {
        cout << i << " ";
    }
    cout << "\nCo " << n / 2 << " so chan" << endl;
    return 0;
}
```

💡 **Cách 2 tốt hơn:** thay vì duyệt hết rồi lọc, hãy **chỉ duyệt đúng cái cần**. Bước nhảy `i += 2` giảm một nửa số vòng lặp.

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    cout << "--- BANG CUU CHUONG " << n << " ---" << endl;
    for (int i = 1; i <= 10; i++) {
        cout << setw(2) << n << " x " << setw(2) << i
             << " = " << setw(3) << n * i << endl;
    }
    return 0;
}
```

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    // In 2 bang cuu chuong tren mot hang cho gon
    for (int hang = 1; hang <= 10; hang++) {
        for (int bang = 2; bang <= 9; bang++) {
            cout << bang << "x" << setw(2) << hang
                 << "=" << setw(2) << bang * hang << "  ";
        }
        cout << endl;
    }
    return 0;
}
```

Output:

```
2x 1= 2  3x 1= 3  4x 1= 4  5x 1= 5  6x 1= 6  7x 1= 7  8x 1= 8  9x 1= 9  
2x 2= 4  3x 2= 6  4x 2= 8  5x 2=10  6x 2=12  7x 2=14  8x 2=16  9x 2=18  
...
```

**Nguyên lý vòng lặp lồng nhau:** với mỗi lần chạy của vòng **ngoài**, vòng **trong** chạy trọn vẹn từ đầu đến cuối. Tổng số lần thân trong chạy = (số vòng ngoài) × (số vòng trong) = 10 × 8 = 80.

### Bài 8.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int tam = abs(n);
    int tong = 0;

    for (; tam > 0; tam /= 10) {
        tong += tam % 10;
    }

    cout << "Tong cac chu so = " << tong << endl;
    return 0;
}
```

💡 Vòng `for` này bỏ trống phần khởi tạo (vì `tam` đã khai báo trước). Cả 3 phần của `for` đều có thể bỏ trống — `for (;;)` là vòng lặp vô hạn.

⚠️ **Trường hợp `n = 0`:** vòng lặp không chạy lần nào, `tong = 0` — vẫn đúng.

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n < 2) {
        cout << n << " KHONG phai so nguyen to" << endl;
        return 0;
    }

    bool nguyenTo = true;
    // Chi can kiem tra toi CAN BAC HAI cua n
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) {
            nguyenTo = false;
            break;                  // tim thay uoc -> dung ngay
        }
    }

    cout << n << (nguyenTo ? " LA " : " KHONG phai ") << "so nguyen to" << endl;
    return 0;
}
```

**Vì sao chỉ cần duyệt tới √n:** nếu `n = a × b` với `a ≤ b`, thì chắc chắn `a ≤ √n`. Nên nếu không tìm được ước nào ≤ √n thì `n` là số nguyên tố.

Với `n = 10⁹`: duyệt tới `n` cần 1 tỷ bước (~10 giây), duyệt tới `√n` chỉ cần ~31.623 bước (**tức thì**).

⚠️ Dùng `(long long)i * i <= n` thay vì `i <= sqrt(n)` để tránh sai số số thực và tránh gọi `sqrt` mỗi vòng lặp.

⚠️ Nhớ 2 trường hợp đặc biệt: `n < 2` không phải nguyên tố; **2 là số nguyên tố chẵn duy nhất**.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n <= 0) { cout << "n phai duong!" << endl; return 1; }

    cout << "Cac uoc cua " << n << ": ";
    long long tongUoc = 0;
    int demUoc = 0;

    for (int i = 1; i <= n; i++) {
        if (n % i == 0) {
            cout << i << " ";
            tongUoc += i;
            demUoc++;
        }
    }

    cout << "\nSo luong uoc : " << demUoc  << endl;
    cout << "Tong cac uoc : " << tongUoc << endl;

    // Kiem tra so hoan hao (tong cac uoc THAT SU = chinh no)
    if (tongUoc - n == n) cout << n << " la SO HOAN HAO!" << endl;
    return 0;
}
```

💡 **Cách tối ưu — chỉ duyệt tới √n:** các ước luôn đi thành cặp `(i, n/i)`:

```cpp
for (int i = 1; (long long)i * i <= n; i++) {
    if (n % i == 0) {
        tongUoc += i;
        if (i != n / i) tongUoc += n / i;    // tranh cong doi voi so chinh phuong
    }
}
```

Với `n = 10⁹` cách này nhanh hơn ~31.000 lần.

**Số hoàn hảo:** 6 (1+2+3), 28 (1+2+4+7+14), 496, 8128…

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    long long a = 0, b = 1;

    cout << "Day Fibonacci: ";
    for (int i = 1; i <= n; i++) {
        cout << a << " ";
        long long tiep = a + b;
        a = b;
        b = tiep;
    }
    cout << endl;
    return 0;
}
```

Với `n = 10`: `0 1 1 2 3 5 8 13 21 34`

**Cách hoạt động:** chỉ cần giữ **2 số gần nhất**, không cần mảng.

```
a=0, b=1  -> in 0, roi a=1, b=1
a=1, b=1  -> in 1, roi a=1, b=2
a=1, b=2  -> in 1, roi a=2, b=3
a=2, b=3  -> in 2, roi a=3, b=5
```

⚠️ Fibonacci tăng rất nhanh: `F(47)` đã vượt `int`, `F(93)` vượt `long long`. Nhớ dùng `long long`.

*(Cách đệ quy sẽ học ở bài [05-06](../05-06-cpp-ham-de-quy.md) — nhưng đệ quy thuần cho Fibonacci cực chậm.)*

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so dong: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
```

**Nguyên lý:** dòng thứ `i` có đúng `i` dấu `*`. Vòng ngoài điều khiển **dòng**, vòng trong điều khiển **số ký tự trên dòng đó**.

Biến thể — tam giác ngược:

```cpp
for (int i = n; i >= 1; i--) {
    for (int j = 1; j <= i; j++) cout << "*";
    cout << endl;
}
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so dong: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        // In (n - i) dau cach de can giua
        for (int j = 1; j <= n - i; j++) cout << " ";
        // In (2*i - 1) dau sao
        for (int j = 1; j <= 2 * i - 1; j++) cout << "*";
        cout << endl;
    }
    return 0;
}
```

Với `n = 4`:

```
   *
  ***
 *****
*******
```

**Phân tích công thức:**

| Dòng i | Số dấu cách | Số dấu `*` |
|---|---|---|
| 1 | n−1 = 3 | 2×1−1 = 1 |
| 2 | n−2 = 2 | 2×2−1 = 3 |
| 3 | n−3 = 1 | 2×3−1 = 5 |
| 4 | n−4 = 0 | 2×4−1 = 7 |

**Mẹo giải mọi bài vẽ hình:** lập bảng như trên cho 3–4 dòng đầu, tìm ra công thức theo `i`, rồi mới viết code.

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    double S = 0;
    for (int i = 1; i <= n; i++) {
        S += 1.0 / i;              // 1.0 chu khong phai 1!
    }

    cout << fixed << setprecision(10);
    cout << "S = " << S << endl;
    return 0;
}
```

⚠️ **Lỗi phổ biến nhất:** viết `S += 1 / i;`. Vì `1` và `i` đều là `int`, phép chia là **chia nguyên** → cho 0 với mọi `i > 1` → kết quả luôn bằng 1.

Sửa bằng một trong các cách: `1.0 / i`, `1 / (double)i`, `(double)1 / i`.

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    double S = 0;
    int dau = 1;                   // 1 hoac -1

    for (int i = 1; i <= n; i++) {
        S += dau * 1.0 / i;
        dau = -dau;                // dao dau moi vong
    }

    cout << fixed << setprecision(10);
    cout << "S = " << S << endl;
    cout << "ln(2) = " << 0.6931471805 << " (gia tri hoi tu)" << endl;
    return 0;
}
```

**Cách khác — dùng tính chẵn lẻ của `i`:**

```cpp
for (int i = 1; i <= n; i++) {
    if (i % 2 == 1) S += 1.0 / i;
    else            S -= 1.0 / i;
}
```

**Cách thứ ba — dùng `pow(-1, i+1)`:** đúng nhưng **chậm**, vì `pow` là hàm số thực nặng. Kỹ thuật `dau = -dau` nhanh hơn nhiều.

💡 **Kiến thức toán:** chuỗi này hội tụ về **ln(2) ≈ 0,693147** khi `n → ∞`. Với `n = 1000` bạn sẽ thấy `S ≈ 0,6926`.
