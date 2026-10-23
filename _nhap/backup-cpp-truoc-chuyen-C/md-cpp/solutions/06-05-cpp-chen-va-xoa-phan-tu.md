# Lời giải — [C++]. Chèn Và Xóa Phần Tử

[← Quay lại bài học](../06-05-cpp-chen-va-xoa-phan-tu.md)

> **Nguyên lý cốt lõi:**
> - **Chèn** tại vị trí `k` → dịch các phần tử từ `k` trở đi **sang phải**, duyệt **từ cuối về `k`**
> - **Xoá** tại vị trí `k` → dịch các phần tử từ `k+1` trở đi **sang trái**, duyệt **từ `k` đến cuối**

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

void chen(int a[], int &n, int k, int x) {
    if (k < 0 || k > n) { cout << "Vi tri khong hop le!" << endl; return; }

    // Dich cac phan tu tu k tro di sang PHAI mot vi tri
    // Duyet TU CUOI VE DAU de khong ghi de du lieu
    for (int i = n; i > k; i--) {
        a[i] = a[i - 1];
    }
    a[k] = x;
    n++;
}

int main() {
    int a[100] = {10, 20, 30, 40, 50};
    int n = 5;

    chen(a, n, 2, 99);

    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                          // 10 20 99 30 40 50
    return 0;
}
```

⚠️ **Phải duyệt TỪ CUỐI VỀ ĐẦU.** Nếu duyệt xuôi:

```cpp
for (int i = k; i < n; i++) a[i + 1] = a[i];   // SAI!
// a[3] = a[2] -> 30 ghi de 40 (mat 40)
// a[4] = a[3] -> lai la 30, khong phai 40
// Ket qua: 10 20 30 30 30 30
```

⚠️ `n` phải là **tham chiếu** (`int &n`) để cập nhật được kích thước ở hàm gọi.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

void xoa(int a[], int &n, int k) {
    if (k < 0 || k >= n) { cout << "Vi tri khong hop le!" << endl; return; }

    // Dich cac phan tu tu k+1 tro di sang TRAI
    // Duyet TU DAU VE CUOI
    for (int i = k; i < n - 1; i++) {
        a[i] = a[i + 1];
    }
    n--;
}

int main() {
    int a[100] = {10, 20, 30, 40, 50};
    int n = 5;

    xoa(a, n, 1);

    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                          // 10 30 40 50
    return 0;
}
```

⚠️ **Vòng lặp dừng ở `n - 1`**, không phải `n`. Nếu chạy tới `n` thì `a[i+1]` = `a[n]` là truy cập ngoài biên.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

void chen(int a[], int &n, int k, int x) {
    for (int i = n; i > k; i--) a[i] = a[i - 1];
    a[k] = x;
    n++;
}

void inMang(int a[], int n) {
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;
}

int main() {
    int a[100] = {10, 20, 30};
    int n = 3;

    cout << "Ban dau   : "; inMang(a, n);

    chen(a, n, 0, 5);           // chen vao DAU
    cout << "Chen dau 5: "; inMang(a, n);

    chen(a, n, n, 99);          // chen vao CUOI
    cout << "Chen cuoi : "; inMang(a, n);
    return 0;
}
```

Output:

```
Ban dau   : 10 20 30 
Chen dau 5: 5 10 20 30 
Chen cuoi : 5 10 20 30 99 
```

💡 **Chèn cuối chỉ cần `a[n++] = x;`** — không phải dịch phần tử nào, O(1).
💡 **Chèn đầu phải dịch toàn bộ** — O(n), tốn kém nhất.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

void xoaTatCa(int a[], int &n, int x) {
    int j = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] != x) a[j++] = a[i];        // giu lai phan tu khac x
    }
    n = j;
}

int main() {
    int a[100] = {1, 3, 2, 3, 4, 3, 5};
    int n = 7;

    xoaTatCa(a, n, 3);

    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << " (n = " << n << ")" << endl;     // 1 2 4 5 (n = 4)
    return 0;
}
```

💡 **Kỹ thuật 2 con trỏ** — cách tối ưu nhất để xoá nhiều phần tử:
- `i` duyệt qua mọi phần tử
- `j` là vị trí tiếp theo để ghi phần tử được giữ lại

Độ phức tạp **O(n)** — duyệt đúng một lần. So với cách gọi hàm `xoa()` nhiều lần (O(n²)), đây là cải tiến rất lớn.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100] = {3, -1, 5, -7, 2, -4, 8};
    int n = 7;

    int j = 0;
    for (int i = 0; i < n; i++) {
        if (a[i] >= 0) a[j++] = a[i];
    }
    n = j;

    cout << "Sau khi xoa so am: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                                 // 3 5 2 8
    return 0;
}
```

💡 C++ có sẵn: `n = remove_if(a, a + n, [](int x){ return x < 0; }) - a;`

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100] = {1, 3, 1, 5, 3, 7, 5};
    int n = 7;

    int m = 0;
    for (int i = 0; i < n; i++) {
        bool daCo = false;
        for (int j = 0; j < m; j++) {
            if (a[j] == a[i]) { daCo = true; break; }
        }
        if (!daCo) a[m++] = a[i];
    }
    n = m;

    cout << "Sau khi xoa trung lap: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                                 // 1 3 5 7
    return 0;
}
```

Độ phức tạp O(n²). Cách O(n) dùng `unordered_set`:

```cpp
#include <unordered_set>
unordered_set<int> daGap;
int m = 0;
for (int i = 0; i < n; i++)
    if (daGap.insert(a[i]).second) a[m++] = a[i];
n = m;
```

⚠️ Nếu mảng **đã sắp xếp**, có thể dùng `unique`:

```cpp
n = unique(a, a + n) - a;      // chi xoa cac phan tu TRUNG KE NHAU
```

### Bài 7.

```cpp
#include <iostream>
using namespace std;

void chenGiuThuTu(int a[], int &n, int x) {
    // Tim vi tri chen: phan tu dau tien >= x
    int k = 0;
    while (k < n && a[k] < x) k++;

    // Dich sang phai roi chen
    for (int i = n; i > k; i--) a[i] = a[i - 1];
    a[k] = x;
    n++;
}

int main() {
    int a[100] = {1, 3, 5, 7, 9};
    int n = 5;

    chenGiuThuTu(a, n, 6);
    chenGiuThuTu(a, n, 0);
    chenGiuThuTu(a, n, 100);

    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                       // 0 1 3 5 6 7 9 100
    return 0;
}
```

💡 Có thể dùng **tìm kiếm nhị phân** để tìm vị trí chèn nhanh hơn (O(log n) thay vì O(n)):

```cpp
int k = lower_bound(a, a + n, x) - a;
```

Nhưng phần **dịch phần tử** vẫn là O(n), nên tổng thể vẫn O(n).

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100] = {1, 2, 3, 4, 5};
    int n = 5;

    // Duyet TU CUOI VE DAU de khong bi lap vo han
    for (int i = n - 1; i >= 0; i--) {
        if (a[i] % 2 == 0) {
            // Chen 0 vao vi tri i+1
            for (int j = n; j > i + 1; j--) a[j] = a[j - 1];
            a[i + 1] = 0;
            n++;
        }
    }

    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                       // 1 2 0 3 4 0 5
    return 0;
}
```

⚠️ **Phải duyệt từ cuối về đầu.** Nếu duyệt xuôi, sau khi chèn 0 thì các chỉ số phía sau bị dịch, vòng lặp sẽ xét lại phần tử đã xử lý và chèn lặp vô hạn (số 0 là số chẵn!).

Đây là quy tắc chung: **khi vừa duyệt vừa chèn, hãy duyệt ngược.**

### Bài 9.

```cpp
#include <iostream>
using namespace std;

void xoaNhieu(int a[], int &n, int p, int k) {
    if (p < 0 || p >= n || k <= 0) return;
    if (p + k > n) k = n - p;              // cat bot neu vuot qua

    for (int i = p; i < n - k; i++) {
        a[i] = a[i + k];
    }
    n -= k;
}

int main() {
    int a[100] = {10, 20, 30, 40, 50, 60, 70};
    int n = 7;

    xoaNhieu(a, n, 2, 3);                  // xoa 3 phan tu tu vi tri 2

    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                          // 10 20 60 70
    return 0;
}
```

💡 Xoá `k` phần tử cùng lúc chỉ cần **một lần duyệt** — nhanh hơn nhiều so với gọi hàm xoá 1 phần tử `k` lần.

### Bài 10.

```cpp
for (int i = k; i < n; i++) a[i] = a[i + 1];   // LOI: truy cap ngoai bien
n--;
```

**Lỗi:** khi `i = n - 1`, câu lệnh trở thành `a[n-1] = a[n]` — truy cập `a[n]` là **ngoài biên** mảng.

Với mảng tĩnh cỡ lớn (`int a[100]` mà `n = 5`), lỗi này thường **không gây crash** và giá trị đọc được là rác — nhưng nó bị ghi vào `a[n-1]` rồi lại bị `n--` bỏ đi, nên **kết quả tình cờ vẫn đúng**. Đây là loại lỗi nguy hiểm vì khó phát hiện.

Nếu `n` đúng bằng kích thước mảng, chương trình sẽ đọc vào vùng nhớ không thuộc mảng → có thể crash.

**Sửa:**

```cpp
for (int i = k; i < n - 1; i++) a[i] = a[i + 1];
n--;
```

💡 Biên dịch với `-fsanitize=address` sẽ phát hiện ngay lỗi này.

### Bài 11.

```cpp
for (int i = 0; i < n; i++) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
        // THIEU: i--;
    }
}
```

**Lỗi:** sau khi xoá phần tử tại vị trí `i`, phần tử kế tiếp **đã dịch vào chính vị trí `i`**. Nhưng vòng lặp vẫn tăng `i++`, nên phần tử mới này bị **bỏ qua**.

Ví dụ với `{-1, -2, 3}`:

```
i=0: a[0]=-1 am -> xoa -> mang thanh {-2, 3}, n=2
i=1: xet a[1]=3 (khong am)      <- BO SOT a[0] = -2!
Ket qua: {-2, 3}  -- con sot so am
```

**Sửa cách 1 — giảm `i` sau khi xoá:**

```cpp
for (int i = 0; i < n; i++) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
        i--;                     // <- lui lai de xet lai vi tri nay
    }
}
```

**Sửa cách 2 — duyệt ngược (không cần chỉnh `i`):**

```cpp
for (int i = n - 1; i >= 0; i--) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
    }
}
```

**Sửa cách 3 — kỹ thuật 2 con trỏ (TỐT NHẤT, O(n)):**

```cpp
int j = 0;
for (int i = 0; i < n; i++)
    if (a[i] >= 0) a[j++] = a[i];
n = j;
```

Cách 1 và 2 là **O(n²)**; cách 3 là **O(n)**.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[100] = {1, 2, 3};
    int n = 3;
    int b[] = {7, 8, 9, 10};
    int m = 4;

    // Cach don gian: noi B vao cuoi A
    for (int i = 0; i < m; i++) {
        a[n++] = b[i];
    }

    cout << "Sau khi gop: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                       // 1 2 3 7 8 9 10

    // Cach xen ke: chen tung phan tu cua B vao vi tri le cua A
    int c[100] = {1, 2, 3};
    int nc = 3;
    int d[] = {7, 8, 9};
    int md = 3;

    for (int i = 0; i < md; i++) {
        int vt = 2 * i + 1;
        if (vt > nc) vt = nc;
        for (int j = nc; j > vt; j--) c[j] = c[j - 1];
        c[vt] = d[i];
        nc++;
    }

    cout << "Gop xen ke : ";
    for (int i = 0; i < nc; i++) cout << c[i] << " ";
    cout << endl;                       // 1 7 2 8 3 9
    return 0;
}
```

### Bài 13.

| Thao tác | Độ phức tạp | Số phần tử phải dịch |
|---|---|---|
| **Chèn vào cuối** | **O(1)** | 0 |
| **Xoá ở cuối** | **O(1)** | 0 |
| Chèn vào giữa (vị trí `k`) | O(n−k) | n−k |
| Xoá ở giữa | O(n−k) | n−k−1 |
| **Chèn vào đầu** | **O(n)** | n (toàn bộ) |
| **Xoá ở đầu** | **O(n)** | n−1 (gần toàn bộ) |

**Vì sao có sự khác biệt:** mảng lưu các phần tử **liên tiếp nhau trong bộ nhớ**. Đây là lý do truy cập `a[i]` cực nhanh (O(1) — chỉ cần tính địa chỉ), nhưng cũng là lý do chèn/xoá ở giữa phải **dịch chuyển vật lý** mọi phần tử phía sau.

```
Chen vao dau:  [1][2][3][4][ ]
                 \  \  \  \      <- tat ca phai dich 1 o
               [x][1][2][3][4]

Chen vao cuoi: [1][2][3][4][ ]
                            |    <- chi ghi 1 o
               [1][2][3][4][x]
```

💡 **Hệ quả thiết kế:**
- Cần chèn/xoá **ở cuối** nhiều → dùng `vector` (`push_back` là O(1) trung bình)
- Cần chèn/xoá **ở đầu** nhiều → dùng `deque` (O(1) cả hai đầu)
- Cần chèn/xoá **ở giữa** nhiều → dùng `list` (danh sách liên kết, O(1) nếu đã có iterator)

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void inVector(const string& nhan, const vector<int>& v) {
    cout << nhan << ": ";
    for (int x : v) cout << x << " ";
    cout << "(size = " << v.size() << ")" << endl;
}

int main() {
    vector<int> v = {10, 20, 30, 40, 50};
    inVector("Ban dau        ", v);

    // Bai 1: chen 99 vao vi tri 2
    v.insert(v.begin() + 2, 99);
    inVector("Sau insert     ", v);

    // Bai 2: xoa phan tu tai vi tri 1
    v.erase(v.begin() + 1);
    inVector("Sau erase      ", v);

    // Bai 4: xoa tat ca gia tri 30
    v.erase(remove(v.begin(), v.end(), 30), v.end());
    inVector("Sau xoa gia tri", v);

    // Them vao cuoi / xoa cuoi
    v.push_back(777);
    inVector("Sau push_back  ", v);
    v.pop_back();
    inVector("Sau pop_back   ", v);

    return 0;
}
```

Output:

```
Ban dau        : 10 20 30 40 50 (size = 5)
Sau insert     : 10 20 99 30 40 50 (size = 6)
Sau erase      : 10 99 30 40 50 (size = 5)
Sau xoa gia tri: 10 99 40 50 (size = 4)
Sau push_back  : 10 99 40 50 777 (size = 5)
Sau pop_back   : 10 99 40 50 (size = 4)
```

**So sánh với mảng tĩnh:**

| Việc | Mảng tĩnh | `vector` |
|---|---|---|
| Chèn | Tự viết hàm ~8 dòng | `v.insert(v.begin()+k, x)` |
| Xoá | Tự viết hàm ~6 dòng | `v.erase(v.begin()+k)` |
| Xoá theo giá trị | Tự viết vòng lặp 2 con trỏ | `v.erase(remove(...), v.end())` |
| Theo dõi kích thước | Tự quản lý biến `n` | `v.size()` |
| Vượt sức chứa | ⚠️ Tràn bộ nhớ, crash | ✅ Tự động mở rộng |

⚠️ **Thành ngữ erase-remove:** `remove` **không thực sự xoá** — nó dồn các phần tử cần giữ về đầu và trả về iterator tới vị trí kết thúc phần hợp lệ. Phải kết hợp với `erase` mới thực sự thu nhỏ vector. Đây là điểm gây nhầm lẫn kinh điển trong C++.

💡 C++20 có `std::erase(v, 30)` gọn hơn.

### Bài 15.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void hienMenu() {
    cout << "\n====== QUAN LY DANH SACH ======" << endl;
    cout << "1. Them vao cuoi"                  << endl;
    cout << "2. Chen tai vi tri"                << endl;
    cout << "3. Xoa theo vi tri"                << endl;
    cout << "4. Xoa theo gia tri"               << endl;
    cout << "5. Hien thi danh sach"             << endl;
    cout << "6. Sap xep tang dan"               << endl;
    cout << "0. Thoat"                          << endl;
    cout << "==============================="   << endl;
    cout << "Lua chon: ";
}

void hienThi(const vector<int>& v) {
    if (v.empty()) { cout << ">> Danh sach RONG" << endl; return; }
    cout << ">> Danh sach (" << v.size() << " phan tu): ";
    for (size_t i = 0; i < v.size(); i++) {
        cout << "[" << i << "]=" << v[i] << " ";
    }
    cout << endl;
}

int main() {
    vector<int> v;
    int chon;

    do {
        hienMenu();
        cin >> chon;

        switch (chon) {
            case 1: {
                int x;
                cout << "Nhap gia tri: "; cin >> x;
                v.push_back(x);
                cout << ">> Da them " << x << " vao cuoi" << endl;
                break;
            }
            case 2: {
                int k, x;
                cout << "Nhap vi tri (0.." << v.size() << "): "; cin >> k;
                if (k < 0 || k > (int)v.size()) {
                    cout << ">> Vi tri khong hop le!" << endl;
                    break;
                }
                cout << "Nhap gia tri: "; cin >> x;
                v.insert(v.begin() + k, x);
                cout << ">> Da chen " << x << " vao vi tri " << k << endl;
                break;
            }
            case 3: {
                if (v.empty()) { cout << ">> Danh sach rong!" << endl; break; }
                int k;
                cout << "Nhap vi tri (0.." << v.size() - 1 << "): "; cin >> k;
                if (k < 0 || k >= (int)v.size()) {
                    cout << ">> Vi tri khong hop le!" << endl;
                    break;
                }
                cout << ">> Da xoa gia tri " << v[k] << endl;
                v.erase(v.begin() + k);
                break;
            }
            case 4: {
                int x;
                cout << "Nhap gia tri can xoa: "; cin >> x;
                size_t truoc = v.size();
                v.erase(remove(v.begin(), v.end(), x), v.end());
                cout << ">> Da xoa " << truoc - v.size() << " phan tu" << endl;
                break;
            }
            case 5:
                hienThi(v);
                break;
            case 6:
                sort(v.begin(), v.end());
                cout << ">> Da sap xep" << endl;
                hienThi(v);
                break;
            case 0:
                cout << ">> Tam biet!" << endl;
                break;
            default:
                cout << ">> Lua chon khong hop le!" << endl;
        }
    } while (chon != 0);

    return 0;
}
```

**Các điểm đáng học:**

1. **Luôn kiểm tra `v.empty()`** trước khi xoá — tránh crash
2. **Luôn kiểm tra biên** của vị trí người dùng nhập
3. **Ép `(int)v.size()`** khi so sánh với `int` — `size()` trả về unsigned, so sánh `k < v.size()` với `k` âm sẽ cho kết quả sai (xem bài [02-02](../02-02-cpp-kieu-du-lieu.md) bài 15)
4. Bọc `{ }` quanh các `case` có khai báo biến
