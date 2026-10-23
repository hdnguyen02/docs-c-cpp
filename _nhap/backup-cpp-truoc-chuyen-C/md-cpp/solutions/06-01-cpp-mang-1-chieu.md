# Lời giải — [C++]. Mảng 1 Chiều

[← Quay lại bài học](../06-01-cpp-mang-1-chieu.md)

> **Nhớ:** chỉ số mảng trong C++ bắt đầu từ **0**. Mảng `n` phần tử có chỉ số hợp lệ từ `0` đến `n−1`.

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
    for (int i = 0; i < n; i++) {
        cout << "  a[" << i << "] = ";
        cin >> a[i];
    }

    cout << "Thu tu nhap  : ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;

    cout << "Thu tu nguoc : ";
    for (int i = n - 1; i >= 0; i--) cout << a[i] << " ";
    cout << endl;

    return 0;
}
```

### Bài 2.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    long long tong = 0;
    long long tich = 1;
    for (int i = 0; i < n; i++) {
        tong += a[i];
        tich *= a[i];
    }

    cout << "Tong        = " << tong << endl;
    cout << "Tich        = " << tich << endl;
    cout << fixed << setprecision(4);
    cout << "Trung binh  = " << (n > 0 ? (double)tong / n : 0) << endl;
    return 0;
}
```

⚠️ **Tích rất dễ tràn số** — chỉ cần 10 phần tử cỡ 100 là đã vượt `long long`. Trong bài toán thật thường phải lấy dư (`% 1000000007`).

⚠️ Nhớ `(double)tong / n` chứ không phải `tong / n` (chia nguyên).

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    if (n <= 0) { cout << "Mang rong!" << endl; return 1; }

    int vtMax = 0, vtMin = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[vtMax]) vtMax = i;
        if (a[i] < a[vtMin]) vtMin = i;
    }

    cout << "Lon nhat  = " << a[vtMax] << " tai vi tri " << vtMax << endl;
    cout << "Nho nhat  = " << a[vtMin] << " tai vi tri " << vtMin << endl;
    return 0;
}
```

⚠️ **Khởi tạo bằng `a[0]` (hoặc vị trí 0), KHÔNG phải bằng 0.** Nếu mảng toàn số âm và bạn khởi tạo `max = 0`, kết quả sẽ sai.

💡 Lưu **vị trí** thay vì giá trị giúp có được cả hai thông tin bằng một biến.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int duong = 0, am = 0, khong = 0;
    for (int i = 0; i < n; i++) {
        if      (a[i] > 0) duong++;
        else if (a[i] < 0) am++;
        else               khong++;
    }

    cout << "So duong  : " << duong << endl;
    cout << "So am     : " << am    << endl;
    cout << "So bang 0 : " << khong << endl;
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int demChan = 0, demLe = 0;
    long long tongChan = 0, tongLe = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) { demChan++; tongChan += a[i]; }
        else               { demLe++;   tongLe   += a[i]; }
    }

    cout << "So luong chan : " << demChan  << ", tong = " << tongChan << endl;
    cout << "So luong le   : " << demLe    << ", tong = " << tongLe   << endl;
    return 0;
}
```

⚠️ Dùng `a[i] % 2 == 0` để kiểm tra chẵn (đúng với cả số âm). Không dùng `a[i] % 2 == 1` vì `-3 % 2` bằng `-1`.

### Bài 6.

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
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Cac so nguyen to trong mang: ";
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (laNguyenTo(a[i])) { cout << a[i] << " "; dem++; }
    }
    if (dem == 0) cout << "(khong co)";
    cout << "\nSo luong: " << dem << endl;
    return 0;
}
```

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    bool tangDan = true;
    for (int i = 0; i < n - 1; i++) {
        if (a[i] > a[i + 1]) { tangDan = false; break; }
    }

    cout << "Mang " << (tangDan ? "DA" : "CHUA") << " sap xep tang dan" << endl;
    return 0;
}
```

⚠️ Vòng lặp chạy tới `n - 1` (không phải `n`), vì ta so sánh `a[i]` với `a[i+1]`. Nếu chạy tới `n` thì `a[n]` là truy cập ngoài biên.

💡 C++ có sẵn: `is_sorted(a, a + n)` trong `<algorithm>`.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    int x;
    cout << "Nhap gia tri can dem: ";
    cin >> x;

    int dem = 0;
    cout << "Xuat hien tai cac vi tri: ";
    for (int i = 0; i < n; i++) {
        if (a[i] == x) { cout << i << " "; dem++; }
    }
    cout << "\nSo lan xuat hien: " << dem << endl;
    return 0;
}
```

💡 C++ có sẵn: `count(a, a + n, x)` trong `<algorithm>`.

### Bài 9.

```cpp
#include <iostream>
#include <climits>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    if (n < 2) { cout << "Mang can it nhat 2 phan tu!" << endl; return 1; }

    long long nhat = LLONG_MIN, nhi = LLONG_MIN;
    for (int i = 0; i < n; i++) {
        if (a[i] > nhat) {
            nhi  = nhat;           // cai lon nhat cu tut xuong thanh nhi
            nhat = a[i];
        } else if (a[i] > nhi && a[i] != nhat) {
            nhi = a[i];
        }
    }

    if (nhi == LLONG_MIN) cout << "Khong co phan tu lon thu hai (tat ca bang nhau)" << endl;
    else cout << "Lon nhat = " << nhat << ", lon thu hai = " << nhi << endl;
    return 0;
}
```

Ví dụ với `{5, 2, 9, 9, 1}` → lớn nhất 9, lớn thứ hai 5.

⚠️ **Điều kiện `a[i] != nhat`** xử lý trường hợp có giá trị trùng lặp. Nếu bỏ đi, mảng `{9, 9, 1}` sẽ cho "lớn thứ hai = 9" — thường không phải ý đồ bài toán.

💡 Cách này duyệt **một lần** O(n), tốt hơn sắp xếp O(n log n).

### Bài 10.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    // Dao nguoc tai cho: doi cho phan tu dau <-> cuoi, roi tien vao giua
    for (int i = 0; i < n / 2; i++) {
        swap(a[i], a[n - 1 - i]);
    }

    cout << "Mang sau khi dao: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
    return 0;
}
```

⚠️ **Vòng lặp chỉ chạy tới `n / 2`.** Nếu chạy hết `n`, mảng sẽ bị đảo **2 lần** và trở về như cũ.

Với `n` lẻ, phần tử giữa không cần đổi (nó tự đổi với chính nó).

💡 C++ có sẵn: `reverse(a, a + n)`.

### Bài 11.

```cpp
int a[5];
for (int i = 0; i <= 5; i++) a[i] = i;      // LOI!
```

**Lỗi: truy cập ngoài biên mảng (out of bounds).**

Mảng `a[5]` có 5 phần tử với chỉ số hợp lệ là **0, 1, 2, 3, 4**. Vòng lặp chạy `i = 0..5` nên lần cuối ghi vào `a[5]` — **ô nhớ không thuộc mảng**.

**Tính nguy hiểm đặc biệt:** C++ **không kiểm tra** biên mảng. Chương trình:
- Có thể vẫn chạy bình thường (ghi vào ô nhớ trống)
- Có thể **ghi đè lên biến khác** → kết quả sai một cách khó hiểu
- Có thể crash với `Segmentation fault`

Kết quả không đoán trước được, và có thể khác nhau giữa các lần chạy.

**Sửa:**

```cpp
for (int i = 0; i < 5; i++) a[i] = i;      // dung dau < thay vi <=
```

✅ **Quy tắc vàng: với mảng `n` phần tử, luôn viết `for (int i = 0; i < n; i++)`.** Dùng `<` chứ không phải `<=`.

💡 **Công cụ phát hiện lỗi này:**

```bash
g++ -fsanitize=address -g main.cpp -o main
./main
# AddressSanitizer: stack-buffer-overflow ... WRITE of size 4
```

Hoặc dùng `vector` và truy cập qua `.at(i)` — nó sẽ ném ngoại lệ khi vượt biên.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    // ① Khai bao du phan tu
    int a[5] = {10, 20, 30, 40, 50};

    // ② Khai bao THIEU phan tu -> phan con lai tu dong bang 0
    int b[5] = {10, 20};

    // ③ Khong ghi kich thuoc -> compiler tu dem
    int c[] = {1, 2, 3, 4, 5, 6, 7};

    // ④ Khoi tao tat ca bang 0
    int d[5] = {};       // hoac int d[5] = {0};

    // ⑤ KHONG khoi tao -> gia tri RAC
    int e[5];

    auto inMang = [](const char* ten, int m[], int n) {
        cout << ten << ": ";
        for (int i = 0; i < n; i++) cout << m[i] << " ";
        cout << endl;
    };

    inMang("a (du)      ", a, 5);
    inMang("b (thieu)   ", b, 5);
    inMang("c (tu dem)  ", c, 7);
    inMang("d (toan 0)  ", d, 5);
    inMang("e (chua kt) ", e, 5);

    cout << "So phan tu cua c = " << sizeof(c) / sizeof(c[0]) << endl;
    return 0;
}
```

Output:

```
a (du)      : 10 20 30 40 50 
b (thieu)   : 10 20 0 0 0 
c (tu dem)  : 1 2 3 4 5 6 7 
d (toan 0)  : 0 0 0 0 0 
e (chua kt) : 21845 0 4198400 0 32764      <- RAC, moi lan chay moi khac
So phan tu cua c = 7
```

**Ghi nhớ:**
- Khởi tạo thiếu → phần còn lại tự động **bằng 0**
- `int d[5] = {}` là cách gọn nhất để khởi tạo mảng toàn 0
- **Không khởi tạo gì cả** → giá trị rác, cực kỳ nguy hiểm
- `sizeof(mang) / sizeof(mang[0])` cho số phần tử — **chỉ dùng được trong cùng hàm khai báo** (xem bài [05-03](../05-03-c-tham-chieu-va-tham-tri.md) bài 10)

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    long long tongViTriChan = 0, tongViTriLe = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) tongViTriChan += a[i];    // vi tri 0, 2, 4, ...
        else            tongViTriLe   += a[i];    // vi tri 1, 3, 5, ...
    }

    cout << "Tong cac phan tu o VI TRI chan: " << tongViTriChan << endl;
    cout << "Tong cac phan tu o VI TRI le  : " << tongViTriLe   << endl;
    return 0;
}
```

⚠️ **Phân biệt rõ:** "vị trí chẵn" (`i % 2 == 0`) khác với "giá trị chẵn" (`a[i] % 2 == 0`). Đề bài hay dùng cả hai cách nói — đọc kỹ.

### Bài 14.

```cpp
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++) cin >> a[i];

    if (n <= 0) return 1;

    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i];
    double tb = (double)tong / n;

    int viTriGan = 0;
    double khoangCachMin = fabs(a[0] - tb);
    for (int i = 1; i < n; i++) {
        double kc = fabs(a[i] - tb);
        if (kc < khoangCachMin) {
            khoangCachMin = kc;
            viTriGan = i;
        }
    }

    cout << fixed << setprecision(4);
    cout << "Trung binh cong = " << tb << endl;
    cout << "Phan tu gan nhat = " << a[viTriGan]
         << " (vi tri " << viTriGan << ", cach " << khoangCachMin << ")" << endl;
    return 0;
}
```

Ví dụ `{1, 5, 8, 12}` → TB = 6.5 → gần nhất là 5 hoặc 8 (cùng cách 1.5); code trả về **5** (gặp trước).

### Bài 15.

**Cách 1 — mảng tĩnh:**

```cpp
#include <iostream>
using namespace std;

const int MAX = 1000;

int main() {
    int a[MAX];
    int n;

    cout << "Nhap so phan tu (toi da " << MAX << "): ";
    cin >> n;

    if (n <= 0 || n > MAX) {                   // PHAI tu kiem tra
        cout << "Kich thuoc khong hop le!" << endl;
        return 1;
    }

    for (int i = 0; i < n; i++) cin >> a[i];

    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i];

    cout << "Tong = " << tong << endl;
    return 0;
}
```

**Cách 2 — `vector`:**

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    vector<int> a(n);                          // cap phat DUNG n phan tu
    for (int i = 0; i < n; i++) cin >> a[i];

    long long tong = accumulate(a.begin(), a.end(), 0LL);

    cout << "Tong        = " << tong << endl;
    cout << "So phan tu  = " << a.size() << endl;     // vector BIET kich thuoc
    cout << "Lon nhat    = " << *max_element(a.begin(), a.end()) << endl;

    a.push_back(999);                          // them phan tu -> tu dong mo rong
    cout << "Sau push_back, size = " << a.size() << endl;

    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Mảng tĩnh `int a[100]` | `vector<int>` |
|---|---|---|
| **Kích thước** | ⚠️ Cố định lúc biên dịch | ✅ Thay đổi được lúc chạy |
| **Biết kích thước của mình** | ❌ Không (phải truyền `n` kèm) | ✅ Có (`.size()`) |
| **Thêm/xoá phần tử** | ❌ Phải tự làm | ✅ `push_back`, `pop_back`, `insert`, `erase` |
| **Kiểm tra biên** | ❌ Không | ✅ Có (`.at(i)` ném ngoại lệ) |
| **Truyền vào hàm** | Suy biến thành con trỏ | ✅ Truyền như đối tượng bình thường |
| **Sao chép, gán** | ❌ Không gán được `b = a` | ✅ Được |
| **So sánh** | ❌ `a == b` so sánh địa chỉ | ✅ So sánh nội dung |
| **Bộ nhớ** | Stack (giới hạn ~8 MB) | Heap (gần như không giới hạn) |
| **Tốc độ** | Nhanh hơn một chút | Rất gần (chênh lệch không đáng kể) |
| **Cấp phát** | Ngay lập tức | Có chi phí cấp phát ban đầu |

**⚠️ Vấn đề của mảng tĩnh khi `n` lớn:**

```cpp
int main() {
    int a[10000000];       // 40 MB tren STACK -> Segmentation fault!
}
```

Stack thường chỉ 1–8 MB. Mảng lớn phải khai báo **toàn cục** (ngoài `main`) hoặc dùng `vector`.

**✅ Khuyến nghị:**
- **Học cơ bản / bài tập nhỏ / lập trình thi đấu:** mảng tĩnh vẫn ổn, đơn giản và nhanh
- **Mọi trường hợp khác:** dùng `vector` — an toàn hơn, linh hoạt hơn, và nhanh gần như tương đương

💡 Một số hàm STL rất hữu ích với `vector`:

```cpp
#include <algorithm>
#include <numeric>

sort(v.begin(), v.end());                       // sap xep
reverse(v.begin(), v.end());                    // dao nguoc
accumulate(v.begin(), v.end(), 0LL);            // tinh tong
*max_element(v.begin(), v.end());               // gia tri lon nhat
count(v.begin(), v.end(), x);                   // dem so lan xuat hien
find(v.begin(), v.end(), x);                    // tim kiem
is_sorted(v.begin(), v.end());                  // kiem tra da sap xep
```

Tất cả đều dùng được với mảng tĩnh bằng cách truyền `a, a + n` thay cho `v.begin(), v.end()`.
