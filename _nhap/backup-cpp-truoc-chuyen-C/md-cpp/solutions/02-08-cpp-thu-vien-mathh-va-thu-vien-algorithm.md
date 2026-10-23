# Lời giải — [C++]. Thư Viện Math.h Và Thư Viện Algorithm

[← Quay lại bài học](../02-08-cpp-thu-vien-mathh-va-thu-vien-algorithm.md)

> **Ghi chú về thư viện:** trong C++ nên viết `#include <cmath>` thay vì `#include <math.h>`, và `#include <cstdlib>` thay vì `<stdlib.h>`. Hai cách đều chạy, nhưng bản `<cXXX>` đặt các hàm vào namespace `std` đúng chuẩn C++.

---

### Bài 1.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double x, y;
    cout << "Nhap x va y: ";
    cin >> x >> y;

    cout << fixed << setprecision(4);
    cout << "x^y      = " << pow(x, y)  << endl;
    cout << "sqrt(x)  = " << sqrt(x)    << endl;
    cout << "cbrt(x)  = " << cbrt(x)    << endl;
    cout << "log(x)   = " << log(x)     << endl;   // logarit tu nhien (co so e)
    cout << "log10(x) = " << log10(x)   << endl;   // logarit co so 10
    return 0;
}
```

Ví dụ `x = 8, y = 3`:

```
x^y      = 512.0000
sqrt(x)  = 2.8284
cbrt(x)  = 2.0000
log(x)   = 2.0794
log10(x) = 0.9031
```

⚠️ `sqrt` và `log` với tham số âm cho `NaN` (Not a Number); `log(0)` cho `-inf`.

### Bài 2.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    double x;
    cout << "Nhap so thuc: ";
    cin >> x;

    cout << "ceil(" << x << ")  = " << ceil(x)  << endl;
    cout << "floor(" << x << ") = " << floor(x) << endl;
    cout << "round(" << x << ") = " << round(x) << endl;
    return 0;
}
```

**Bảng so sánh:**

| x | `ceil` (làm tròn lên) | `floor` (làm tròn xuống) | `round` (làm tròn gần nhất) | `(int)x` (cắt bỏ) |
|---|---|---|---|---|
| 2.3 | 3 | 2 | 2 | 2 |
| 2.5 | 3 | 2 | **3** | 2 |
| 2.8 | 3 | 2 | 3 | 2 |
| −2.3 | **−2** | **−3** | −2 | **−2** |
| −2.5 | −2 | −3 | **−3** | −2 |
| −2.8 | −2 | −3 | −3 | −2 |

**Điểm mấu chốt:**
- `ceil` luôn đi về phía **+∞**, `floor` luôn về phía **−∞**
- `round` làm tròn về số nguyên gần nhất, `.5` thì làm tròn **ra xa 0**
- `(int)` **cắt bỏ phần thập phân**, tức luôn đi về phía **0** — khác `floor` với số âm!

⚠️ Bẫy hay gặp: nhiều người tưởng `(int)x` = `floor(x)`, nhưng `(int)(-2.3)` = `-2` còn `floor(-2.3)` = `-3`.

### Bài 3.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double a, b, c;
    cout << "Nhap 3 canh tam giac: ";
    cin >> a >> b >> c;

    // Kiem tra dieu kien ton tai tam giac
    if (a <= 0 || b <= 0 || c <= 0 ||
        a + b <= c || a + c <= b || b + c <= a) {
        cout << "Khong phai tam giac hop le!" << endl;
        return 1;
    }

    double p = (a + b + c) / 2;                         // nua chu vi
    double S = sqrt(p * (p - a) * (p - b) * (p - c));   // cong thuc Heron

    cout << fixed << setprecision(4);
    cout << "Nua chu vi = " << p << endl;
    cout << "Dien tich  = " << S << endl;
    return 0;
}
```

Ví dụ `3 4 5`:

```
Nua chu vi = 6.0000
Dien tich  = 6.0000
```

### Bài 4.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double x1, y1, x2, y2;
    cout << "Nhap toa do diem A (x y): ";  cin >> x1 >> y1;
    cout << "Nhap toa do diem B (x y): ";  cin >> x2 >> y2;

    double kc = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    cout << fixed << setprecision(4);
    cout << "Khoang cach AB = " << kc << endl;
    return 0;
}
```

💡 **Mẹo hiệu năng:** `pow(x, 2)` chậm hơn nhiều so với `x * x`, vì `pow` là hàm tổng quát dùng logarit. Với luỹ thừa nhỏ, luôn viết trực tiếp:

```cpp
double dx = x2 - x1, dy = y2 - y1;
double kc = sqrt(dx * dx + dy * dy);      // nhanh hon va chinh xac hon
```

C++17 còn có `std::hypot(dx, dy)` — tính đúng cả khi `dx`, `dy` rất lớn/rất nhỏ (tránh tràn số).

### Bài 5.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double a, b, c;
    cout << "Giai ax^2 + bx + c = 0" << endl;
    cout << "Nhap a, b, c: ";
    cin >> a >> b >> c;

    const double EPS = 1e-9;
    cout << fixed << setprecision(4);

    if (fabs(a) < EPS) {                       // suy bien thanh bac nhat
        if (fabs(b) < EPS) {
            cout << (fabs(c) < EPS ? "Vo so nghiem" : "Vo nghiem") << endl;
        } else {
            cout << "Nghiem duy nhat: x = " << -c / b << endl;
        }
        return 0;
    }

    double delta = b * b - 4 * a * c;

    if (delta < -EPS) {
        cout << "Vo nghiem thuc (delta = " << delta << " < 0)" << endl;
    } else if (fabs(delta) < EPS) {
        cout << "Nghiem kep: x = " << -b / (2 * a) << endl;
    } else {
        double canDelta = sqrt(delta);
        cout << "x1 = " << (-b + canDelta) / (2 * a) << endl;
        cout << "x2 = " << (-b - canDelta) / (2 * a) << endl;
    }
    return 0;
}
```

Kiểm thử:

| a | b | c | Kết quả |
|---|---|---|---|
| 1 | −3 | 2 | x1 = 2, x2 = 1 |
| 1 | −2 | 1 | Nghiệm kép x = 1 |
| 1 | 0 | 1 | Vô nghiệm thực |
| 0 | 2 | −4 | x = 2 |

### Bài 6.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n < 0) {
        cout << n << " khong phai so chinh phuong" << endl;
        return 0;
    }

    // Cong 0.5 truoc khi ep kieu de tranh sai so lam tron cua sqrt
    int can = (int)(sqrt((double)n) + 0.5);

    if (can * can == n) {
        cout << n << " LA so chinh phuong (= " << can << "^2)" << endl;
    } else {
        cout << n << " KHONG phai so chinh phuong" << endl;
    }
    return 0;
}
```

**Vì sao phải `+ 0.5`:** `sqrt` trả về `double` có sai số. Với `n = 25`, máy có thể tính ra `4.999999999999999` thay vì `5.0`. Ép `(int)` sẽ **cắt bỏ** thành 4 → kết luận sai.

Cách viết an toàn tuyệt đối (không dùng số thực để kết luận):

```cpp
int can = (int)sqrt((double)n);
// Thu ca 3 gia tri lan can de chac chan
for (int k = max(0, can - 1); k <= can + 1; k++) {
    if ((long long)k * k == n) { /* la so chinh phuong */ }
}
```

### Bài 7.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n = 25;
    int can = sqrt(n);
    cout << (can * can == n) << endl;      // co the ra 0 thay vi 1!

    int m = pow(10, 2);
    cout << m << endl;                      // co the ra 99 thay vi 100!
    return 0;
}
```

**Giải thích — cả 2 dòng đều là bẫy nổi tiếng:**

**① `sqrt` trả về `double` có sai số.** Nếu compiler tính `sqrt(25)` ra `4.999999999999999`, thì `(int)` cắt thành **4**, và `4*4 = 16 ≠ 25` → in ra `0`.

**② `pow(10, 2)` cũng trả về `double`.** Nếu kết quả là `99.99999999999999`, ép sang `int` cho **99**.

Trên máy hiện đại, hai ví dụ cụ thể này thường vẫn ra đúng (compiler tối ưu thành hằng số), nhưng với số lớn hơn thì **chắc chắn sai**:

```cpp
cout << (int)pow(10, 15) << endl;      // co the ra 999999999999999
```

✅ **Quy tắc: không dùng `pow` cho luỹ thừa số nguyên.** Tự viết hàm:

```cpp
long long luyThua(long long a, int n) {
    long long kq = 1;
    for (int i = 0; i < n; i++) kq *= a;
    return kq;
}
```

Hoặc dùng luỹ thừa nhanh (binary exponentiation) khi `n` lớn:

```cpp
long long luyThuaNhanh(long long a, long long n) {
    long long kq = 1;
    while (n > 0) {
        if (n & 1) kq *= a;
        a *= a;
        n >>= 1;
    }
    return kq;
}
```

### Bài 8.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    const double PI = acos(-1.0);      // cach lay PI chinh xac nhat

    double gocDo;
    cout << "Nhap goc (do): ";
    cin >> gocDo;

    double gocRad = gocDo * PI / 180.0;

    cout << fixed << setprecision(6);
    cout << "Goc radian = " << gocRad      << endl;
    cout << "sin        = " << sin(gocRad) << endl;
    cout << "cos        = " << cos(gocRad) << endl;
    cout << "tan        = " << tan(gocRad) << endl;
    return 0;
}
```

Ví dụ `goc = 30`:

```
Goc radian = 0.523599
sin        = 0.500000
cos        = 0.866025
tan        = 0.577350
```

⚠️ **Mọi hàm lượng giác trong C++ nhận tham số là RADIAN**, không phải độ. Công thức đổi: `rad = do × π / 180`.

⚠️ `tan(90°)` không cho "vô cùng" mà cho một số rất lớn (khoảng 1,6×10¹⁶), do `PI/2` không biểu diễn chính xác được.

### Bài 9.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c;
    cout << "Nhap 3 so: ";
    cin >> a >> b >> c;

    cout << "Lon nhat  = " << max(a, max(b, c)) << endl;
    cout << "Nho nhat  = " << min(a, min(b, c)) << endl;

    // C++11: dung initializer list, ro rang hon
    cout << "Lon nhat  = " << max({a, b, c}) << endl;
    cout << "Nho nhat  = " << min({a, b, c}) << endl;
    return 0;
}
```

⚠️ **Bẫy kiểu dữ liệu:** `max` yêu cầu 2 tham số **cùng kiểu**:

```cpp
int a = 5;
long long b = 10;
max(a, b);                      // LOI: no matching function
max((long long)a, b);           // DUNG
max<long long>(a, b);           // DUNG - chi ro kieu
```

### Bài 10.

```cpp
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
    // 1. Hoan doi 2 so nguyen
    int x = 10, y = 20;
    swap(x, y);
    cout << "int    : " << x << " " << y << endl;      // 20 10

    // 2. Hoan doi 2 chuoi
    string s1 = "codelab", s2 = "cpp";
    swap(s1, s2);
    cout << "string : " << s1 << " " << s2 << endl;    // cpp codelab

    // 3. Hoan doi 2 phan tu cua mang
    int a[5] = {1, 2, 3, 4, 5};
    swap(a[0], a[4]);
    cout << "mang   : ";
    for (int i = 0; i < 5; i++) cout << a[i] << " ";   // 5 2 3 4 1
    cout << endl;
    return 0;
}
```

`swap` là **template**, hoạt động với mọi kiểu — kể cả `vector`, `pair`, hay struct tự định nghĩa.

💡 Với `vector`, `swap` cực nhanh: nó chỉ tráo con trỏ nội bộ chứ không sao chép từng phần tử, nên `swap` hai vector triệu phần tử vẫn tức thì.

### Bài 11.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a, b, c, d;
    cout << "Nhap 4 so: ";
    cin >> a >> b >> c >> d;

    cout << "Lon nhat = " << max({a, b, c, d}) << endl;
    cout << "Nho nhat = " << min({a, b, c, d}) << endl;
    return 0;
}
```

**Cú pháp `max({...})`** (từ C++11) nhận một danh sách khởi tạo, gọn hơn nhiều so với lồng `max(max(max(a,b),c),d)`.

Cần biên dịch với chuẩn C++11 trở lên:

```bash
g++ -std=c++11 main.cpp -o main
```

### Bài 12.

```cpp
#include <iostream>
#include <cmath>       // fabs, abs cho so thuc
#include <cstdlib>     // abs, labs, llabs cho so nguyen
using namespace std;

int main() {
    int       i = -42;
    long      l = -1234567890L;
    long long ll = -9876543210LL;
    double    d = -3.14159;

    cout << "abs(int)      : " << abs(i)    << endl;   // 42
    cout << "labs(long)    : " << labs(l)   << endl;   // 1234567890
    cout << "llabs(ll)     : " << llabs(ll) << endl;   // 9876543210
    cout << "fabs(double)  : " << fabs(d)   << endl;   // 3.14159

    // BAY: dung abs voi so thuc trong C (khong co namespace std)
    cout << "abs(-3.9) sai : " << abs(-3.9) << endl;
    return 0;
}
```

| Hàm | Thư viện | Dùng cho | Ghi chú |
|---|---|---|---|
| `abs` | `<cstdlib>` | `int` | Bản C gốc — cắt số thực về `int` |
| `labs` | `<cstdlib>` | `long` | |
| `llabs` | `<cstdlib>` | `long long` | |
| `fabs` | `<cmath>` | `double`, `float` | **Luôn dùng cái này cho số thực** |
| `std::abs` | `<cmath>` | Mọi kiểu số | Nạp chồng đầy đủ — an toàn nhất trong C++ |

⚠️ **Bẫy kinh điển:** trong C (và trong C++ nếu lỡ dùng bản C của `abs`), `abs(-3.9)` trả về **3** chứ không phải 3.9, vì tham số bị ép về `int`. Đây là lỗi âm thầm, không có cảnh báo.

✅ **Quy tắc:** trong C++, cứ `#include <cmath>` và dùng `std::abs` cho mọi kiểu — nó tự chọn đúng phiên bản. Hoặc dùng `fabs` cho số thực để chắc chắn.

### Bài 13.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

// Lam tron x den k chu so thap phan
double lamTron(double x, int k) {
    double heSo = pow(10, k);
    return round(x * heSo) / heSo;
}

int main() {
    double x;
    int k;
    cout << "Nhap so thuc va so chu so thap phan: ";
    cin >> x >> k;

    cout << fixed << setprecision(k + 4);
    cout << "Goc          : " << x              << endl;
    cout << "Sau lam tron : " << lamTron(x, k)  << endl;
    return 0;
}
```

Ví dụ `3.14159` và `k = 2`:

```
Goc          : 3.141590
Sau lam tron : 3.140000
```

**Nguyên lý:** nhân lên `10^k` → làm tròn về số nguyên → chia lại `10^k`.

```
3.14159 × 100 = 314.159
round(314.159) = 314
314 / 100 = 3.14
```

⚠️ Lưu ý phân biệt hai việc:
- **`setprecision(2)`** chỉ thay đổi **cách hiển thị**, giá trị trong biến không đổi.
- **Hàm `lamTron` trên** thực sự **thay đổi giá trị** của số.

Nếu chỉ cần in đẹp thì dùng `setprecision`, đừng làm tròn thật (sẽ tích luỹ sai số qua các phép tính).

### Bài 14.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double P, r;
    int n;

    cout << "Nhap so tien goc (VND): ";  cin >> P;
    cout << "Nhap lai suat (%/nam) : ";  cin >> r;
    cout << "Nhap so nam           : ";  cin >> n;

    double A = P * pow(1 + r / 100.0, n);

    cout << fixed << setprecision(0);
    cout << "\n--- KET QUA ---" << endl;
    cout << "So tien goc    : " << P     << " VND" << endl;
    cout << "So tien nhan   : " << A     << " VND" << endl;
    cout << "Tien lai       : " << A - P << " VND" << endl;

    // Bang chi tiet tung nam
    cout << "\nChi tiet tung nam:" << endl;
    for (int i = 1; i <= n; i++) {
        cout << "  Nam " << setw(2) << i << ": "
             << setw(15) << P * pow(1 + r / 100.0, i) << " VND" << endl;
    }
    return 0;
}
```

Ví dụ: `P = 100000000`, `r = 7`, `n = 5`

```
--- KET QUA ---
So tien goc    : 100000000 VND
So tien nhan   : 140255173 VND
Tien lai       : 40255173 VND

Chi tiet tung nam:
  Nam  1:       107000000 VND
  Nam  2:       114490000 VND
  Nam  3:       122504300 VND
  Nam  4:       131079601 VND
  Nam  5:       140255173 VND
```

⚠️ **Lưu ý `r / 100.0`** — phải có `.0`, nếu viết `r / 100` mà `r` là `int` thì sẽ bị chia nguyên và lãi suất 7% thành 0%.

### Bài 15.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    double S = 0;
    for (int i = 1; i <= n; i++) {
        S += 1.0 / i;              // 1.0 chu khong phai 1 - de khong bi chia nguyen!
    }

    const double GAMMA = 0.5772156649;    // hang so Euler-Mascheroni
    double xapXi = log(n) + GAMMA;

    cout << fixed << setprecision(10);
    cout << "S (tinh that)  = " << S      << endl;
    cout << "log(n) + gamma = " << xapXi  << endl;
    cout << "Sai lech       = " << fabs(S - xapXi) << endl;
    return 0;
}
```

Ví dụ `n = 1000`:

```
S (tinh that)  = 7.4854708606
log(n) + gamma = 7.4849729965
Sai lech       = 0.0004978641
```

**Kiến thức toán học:** tổng `S = 1 + 1/2 + ... + 1/n` gọi là **chuỗi điều hoà** (harmonic series). Nó **phân kỳ** (tăng vô hạn khi n → ∞) nhưng tăng cực chậm, xấp xỉ `ln(n) + γ` với γ ≈ 0,5772. Sai lệch giảm dần khi `n` lớn (tỉ lệ `1/(2n)`).

⚠️ **Lỗi phổ biến nhất ở bài này:** viết `S += 1 / i;`. Vì `1` và `i` đều là `int`, phép chia là chia nguyên và cho **0** với mọi `i > 1` → kết quả luôn bằng 1. Phải viết `1.0 / i`.
