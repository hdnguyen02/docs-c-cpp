# Lời giải — [C++]. Vòng Lặp While

[← Quay lại bài học](../04-02-cpp-vong-lap-while.md)

> **Khi nào dùng `while` thay vì `for`:** khi **không biết trước số lần lặp**, mà phụ thuộc vào một điều kiện (đọc tới khi hết dữ liệu, chia tới khi bằng 0, thử tới khi đúng).

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int i = 1;
    while (i <= n) {
        cout << i << " ";
        i++;                       // KHONG DUOC QUEN dong nay
    }
    cout << endl;
    return 0;
}
```

**Đối chiếu `for` ↔ `while`:**

```cpp
for (int i = 1; i <= n; i++) { ... }

// tuong duong:
int i = 1;              // khoi tao
while (i <= n) {        // dieu kien
    ...
    i++;                // cap nhat
}
```

`for` gom cả 3 phần lại một chỗ nên khó quên; `while` tách rời nên dễ quên phần cập nhật → lặp vô hạn.

### Bài 2.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    int tam = abs(n);
    int dem = 0;

    if (tam == 0) {
        dem = 1;                   // TRUONG HOP DAC BIET: so 0 co 1 chu so
    } else {
        while (tam > 0) {
            dem++;
            tam /= 10;
        }
    }

    cout << n << " co " << dem << " chu so" << endl;
    return 0;
}
```

⚠️ **2 trường hợp đặc biệt hay quên:**
- `n = 0`: vòng `while (tam > 0)` không chạy lần nào → `dem = 0` (sai, phải là 1)
- `n` âm: dấu `-` không phải chữ số → dùng `abs(n)`

### Bài 3.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    int tam = abs(n);
    int tong = 0;

    while (tam > 0) {
        tong += tam % 10;          // lay chu so cuoi
        tam /= 10;                 // bo chu so cuoi
    }

    cout << "Tong cac chu so = " << tong << endl;
    return 0;
}
```

### Bài 4.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    int tam = abs(n);
    if (tam == 0) {
        cout << "Chu so lon nhat = 0, nho nhat = 0" << endl;
        return 0;
    }

    int maxCs = 0, minCs = 9;
    while (tam > 0) {
        int cs = tam % 10;
        if (cs > maxCs) maxCs = cs;
        if (cs < minCs) minCs = cs;
        tam /= 10;
    }

    cout << "Chu so lon nhat  = " << maxCs << endl;
    cout << "Chu so nho nhat  = " << minCs << endl;
    return 0;
}
```

💡 **Mẹo khởi tạo:** vì chữ số chỉ từ 0 đến 9, khởi tạo `maxCs = 0` (nhỏ hơn mọi chữ số có thể) và `minCs = 9` (lớn hơn mọi chữ số) là an toàn.

Với bài toán tổng quát (mảng số bất kỳ), nên khởi tạo bằng **phần tử đầu tiên** thay vì một hằng số.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    bool am = (n < 0);
    long long tam = am ? -(long long)n : n;
    long long dao = 0;

    while (tam > 0) {
        dao = dao * 10 + tam % 10;    // day chu so cuoi cua tam vao cuoi dao
        tam /= 10;
    }

    if (am) dao = -dao;
    cout << "So dao nguoc = " << dao << endl;
    return 0;
}
```

**Cách hoạt động với `n = 1234`:**

```
tam=1234, dao=0    -> dao = 0*10 + 4 = 4,     tam=123
tam=123,  dao=4    -> dao = 4*10 + 3 = 43,    tam=12
tam=12,   dao=43   -> dao = 43*10 + 2 = 432,  tam=1
tam=1,    dao=432  -> dao = 432*10 + 1 = 4321, tam=0
```

⚠️ Dùng `long long` cho `dao` vì số đảo có thể tràn: `2147483647` đảo thành `7463847412` > giới hạn `int`.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n < 0) {
        cout << n << " KHONG doi xung (so am)" << endl;
        return 0;
    }

    long long tam = n, dao = 0;
    while (tam > 0) {
        dao = dao * 10 + tam % 10;
        tam /= 10;
    }

    cout << n << (dao == n ? " LA " : " KHONG ") << "so doi xung" << endl;
    return 0;
}
```

Kiểm thử: `12321` → đối xứng; `1234` → không; `7` → đối xứng; `10` → không.

### Bài 7.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    long long tong = 0;
    int dem = 0, x;

    cout << "Nhap cac so (nhap 0 de dung):" << endl;
    cin >> x;

    while (x != 0) {
        tong += x;
        dem++;
        cin >> x;
    }

    cout << "Da nhap " << dem << " so" << endl;
    cout << "Tong          = " << tong << endl;

    if (dem > 0) {
        cout << fixed << setprecision(4);
        cout << "Trung binh    = " << (double)tong / dem << endl;
    } else {
        cout << "Khong co so nao de tinh trung binh" << endl;
    }
    return 0;
}
```

**Mẫu code "đọc trước, kiểm tra sau"** (priming read): đọc giá trị đầu **trước** vòng lặp, rồi đọc giá trị tiếp ở **cuối** thân vòng lặp. Đây là mẫu chuẩn khi dùng `while` để đọc dữ liệu.

⚠️ Nhớ kiểm tra `dem > 0` trước khi chia — nếu người dùng nhập `0` ngay lần đầu thì sẽ chia cho 0.

Cách viết gọn hơn dùng `do while` (bài [04-03](../04-03-cpp-vong-lap-do-while.md)) hoặc:

```cpp
while (cin >> x && x != 0) { tong += x; dem++; }
```

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x;
    int maxSo = -1;               // chua co so duong nao
    bool coSoDuong = false;

    cout << "Nhap cac so (so am de dung):" << endl;
    cin >> x;

    while (x >= 0) {
        if (x > 0) {
            if (!coSoDuong || x > maxSo) {
                maxSo = x;
                coSoDuong = true;
            }
        }
        cin >> x;
    }

    if (coSoDuong) cout << "So duong lon nhat = " << maxSo << endl;
    else           cout << "Khong co so duong nao" << endl;

    return 0;
}
```

💡 **Cờ `coSoDuong`** xử lý trường hợp không có dữ liệu hợp lệ nào — rất hay bị bỏ sót.

### Bài 9.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int a, b;
    cout << "Nhap 2 so: ";
    cin >> a >> b;

    int x = abs(a), y = abs(b);

    while (y != 0) {
        int tam = x % y;
        x = y;
        y = tam;
    }

    cout << "UCLN(" << a << ", " << b << ") = " << x << endl;
    return 0;
}
```

**Thuật toán Euclid — nguyên lý:** `UCLN(a, b) = UCLN(b, a mod b)`, lặp tới khi `b = 0` thì `a` chính là UCLN.

Ví dụ `UCLN(48, 18)`:

```
x=48, y=18 -> tam = 48%18 = 12, x=18, y=12
x=18, y=12 -> tam = 18%12 = 6,  x=12, y=6
x=12, y=6  -> tam = 12%6  = 0,  x=6,  y=0
y=0 -> dung. UCLN = 6
```

Cực nhanh: với 2 số cỡ 10¹⁸ cũng chỉ mất vài chục bước.

💡 C++17 có sẵn `std::gcd(a, b)` trong `<numeric>`.

### Bài 10.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long a, b;
    cout << "Nhap 2 so: ";
    cin >> a >> b;

    if (a == 0 || b == 0) {
        cout << "BCNN khong xac dinh khi co so 0" << endl;
        return 1;
    }

    long long x = llabs(a), y = llabs(b);
    long long ta = x, tb = y;

    while (y != 0) {
        long long tam = x % y;
        x = y;
        y = tam;
    }
    long long ucln = x;

    // CHIA TRUOC roi moi NHAN - tranh tran so
    long long bcnn = ta / ucln * tb;

    cout << "UCLN = " << ucln << endl;
    cout << "BCNN = " << bcnn << endl;
    return 0;
}
```

**Công thức:** `BCNN(a, b) = a × b / UCLN(a, b)`

⚠️ **Rất quan trọng — viết `a / ucln * tb` chứ KHÔNG phải `a * tb / ucln`.** Với `a = b = 10⁹`, phép `a * b` = 10¹⁸ đã sát giới hạn `long long`, còn số lớn hơn sẽ tràn. Chia trước thì kết quả trung gian luôn nhỏ.

Phép chia này luôn chia hết, vì `ucln` là ước của `a`.

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cout << "Nhap so nguyen duong: ";
    cin >> n;

    if (n <= 0) { cout << "Phai la so duong!" << endl; return 1; }

    string nhiPhan = "";
    int tam = n;

    while (tam > 0) {
        nhiPhan += (char)('0' + tam % 2);   // lay bit cuoi
        tam /= 2;
    }

    reverse(nhiPhan.begin(), nhiPhan.end());  // dao lai vi ta lay tu bit thap

    cout << n << " (he 10) = " << nhiPhan << " (he 2)" << endl;
    return 0;
}
```

Ví dụ `n = 13`:

```
13 / 2 = 6  du 1
 6 / 2 = 3  du 0
 3 / 2 = 1  du 1
 1 / 2 = 0  du 1
Doc nguoc cac so du: 1101
```

💡 C++ có sẵn `bitset` để đổi nhanh:

```cpp
#include <bitset>
cout << bitset<8>(13) << endl;      // 00001101
```

Mở rộng cho hệ bất kỳ (2–16):

```cpp
const char* SO = "0123456789ABCDEF";
while (tam > 0) { kq += SO[tam % coSo]; tam /= coSo; }
```

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long x;
    cout << "Nhap x: ";
    cin >> x;

    long long a = 0, b = 1;
    int viTri = 0;

    while (a <= x) {
        long long tiep = a + b;
        a = b;
        b = tiep;
        viTri++;
    }

    cout << "So Fibonacci dau tien lon hon " << x << " la " << a
         << " (F" << viTri << ")" << endl;
    return 0;
}
```

Ví dụ `x = 100` → `144` (F₁₂)

Đây là ví dụ điển hình mà **`while` phù hợp hơn `for`** — ta không biết trước cần bao nhiêu vòng.

### Bài 13.

```cpp
int i = 1;
while (i <= 10) {
    cout << i << " ";
    // THIEU: i++;
}
```

**Lỗi:** thiếu câu lệnh cập nhật `i++`. Biến `i` luôn bằng 1, điều kiện `i <= 10` luôn đúng → **lặp vô hạn**, in số 1 mãi mãi.

**Sửa:**

```cpp
int i = 1;
while (i <= 10) {
    cout << i << " ";
    i++;                     // <- THEM VAO
}
```

**Đây là lỗi số 1 khi dùng `while`.** Danh sách kiểm tra mỗi khi viết `while`:

1. ✅ Biến điều kiện có được **cập nhật** trong thân vòng lặp không?
2. ✅ Cập nhật đó có làm điều kiện **tiến tới sai** không? (`i--` thay vì `i++` cũng gây lặp vô hạn)
3. ✅ Có nhánh `if` nào bỏ qua phần cập nhật không?

**Cách dừng chương trình bị treo:** bấm `Ctrl + C` trong terminal.

### Bài 14.

```cpp
int n = 5;
while (n--) cout << n << " ";
```

**Output:**

```
4 3 2 1 0
```

**Giải thích:** `n--` là toán tử hậu tố — nó **trả về giá trị cũ** rồi mới giảm.

| Lần | Giá trị `n--` trả về (dùng làm điều kiện) | `n` sau đó | Kết quả |
|---|---|---|---|
| 1 | 5 → true | 4 | in `4` |
| 2 | 4 → true | 3 | in `3` |
| 3 | 3 → true | 2 | in `2` |
| 4 | 2 → true | 1 | in `1` |
| 5 | 1 → true | 0 | in `0` |
| 6 | **0 → false** | −1 | dừng |

Nhớ: trong C++ **0 là `false`, khác 0 là `true`** — nên `while (n--)` nghĩa là "lặp khi `n` còn khác 0".

Nếu đổi thành `while (--n)` (tiền tố) thì giảm trước rồi mới kiểm tra → in `4 3 2 1` (không có 0).

⚠️ Kiểu viết này rất ngắn nhưng **khó đọc**. Trong code thật nên viết rõ: `while (n > 0) { n--; ... }`

### Bài 15.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    // Chon so ngau nhien tu 1 den 100
    srand(time(0));
    int soBiMat = rand() % 100 + 1;

    int doan, soLan = 0;

    cout << "=== TRO CHOI DOAN SO (1-100) ===" << endl;

    while (true) {
        cout << "Doan cua ban: ";
        cin >> doan;
        soLan++;

        if (doan == soBiMat) {
            cout << "CHINH XAC! Ban da doan dung sau " << soLan << " lan." << endl;
            break;
        } else if (doan < soBiMat) {
            cout << "  -> So bi mat LON HON " << doan << endl;
        } else {
            cout << "  -> So bi mat NHO HON " << doan << endl;
        }
    }

    // Danh gia
    if      (soLan <= 7)  cout << "Xuat sac! Ban dung chien luoc tim kiem nhi phan." << endl;
    else if (soLan <= 12) cout << "Kha tot!" << endl;
    else                  cout << "Thu tim hieu 'tim kiem nhi phan' nhe!" << endl;

    return 0;
}
```

**Về hàm ngẫu nhiên:**
- `srand(time(0))` — gieo hạt bằng thời gian hiện tại, để mỗi lần chạy cho số khác nhau. **Chỉ gọi MỘT LẦN** ở đầu chương trình.
- `rand() % 100 + 1` — sinh số trong khoảng 1–100.
- Cần `#include <cstdlib>` và `#include <ctime>`.

💡 **Chiến lược tối ưu để đoán:** luôn đoán vào **giữa khoảng còn lại** (bắt đầu 50, rồi 25 hoặc 75…). Cách này gọi là **tìm kiếm nhị phân** và đảm bảo tìm ra trong tối đa **7 lần** với dải 1–100 (vì 2⁷ = 128 > 100). Xem bài [10-01](../10-01-c-thuat-toan-tim-kiem-nhi-phan.md).

💡 `while (true)` kết hợp `break` là mẫu chuẩn khi điều kiện dừng nằm **giữa** thân vòng lặp chứ không phải ở đầu.
