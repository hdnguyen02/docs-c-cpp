# Lời giải — [C++]. Cấp Phát Mảng Động

[← Quay lại bài học](../07-04-c-cap-phat-mang-dong.md)

> **Quy tắc vàng:** mỗi `new` phải có đúng một `delete`, mỗi `new[]` phải có đúng một `delete[]`.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    if (n <= 0) { cout << "n phai duong!" << endl; return 1; }

    int *a = new int[n];             // CAP PHAT

    for (int i = 0; i < n; i++) {
        cout << "  a[" << i << "] = ";
        cin >> a[i];
    }

    cout << "Mang vua nhap: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;

    delete[] a;                      // GIAI PHONG
    a = nullptr;                     // tranh dangling pointer

    return 0;
}
```

💡 **Ưu điểm lớn nhất của mảng động:** kích thước được quyết định **lúc chạy**, không phải lúc biên dịch. Không còn phải khai báo `int a[1000]` rồi chỉ dùng 5 phần tử.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int *p = new int;             // cap phat 1 int, gia tri RAC
    *p = 42;
    cout << "*p = " << *p << endl;
    delete p;                      // KHONG co []

    int *q = new int(100);         // cap phat VA khoi tao = 100
    cout << "*q = " << *q << endl;
    delete q;

    int *r = new int();            // cap phat VA khoi tao = 0
    cout << "*r = " << *r << endl;
    delete r;

    return 0;
}
```

| Cú pháp | Kết quả |
|---|---|
| `new int` | Cấp phát, giá trị **rác** |
| `new int()` | Cấp phát, khởi tạo **0** |
| `new int(100)` | Cấp phát, khởi tạo **100** |
| `new int[5]` | Mảng 5 phần tử, giá trị **rác** |
| `new int[5]()` | Mảng 5 phần tử, tất cả **0** |
| `new int[5]{1,2,3}` | Mảng 5 phần tử: 1, 2, 3, 0, 0 |

⚠️ **`delete` và `delete[]` KHÔNG thay thế cho nhau được** — xem bài 7.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n = 5;

    // Cach 1: dung () de khoi tao 0
    int *a = new int[n]();
    cout << "Cach 1: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;                     // 0 0 0 0 0

    // Cach 2: danh sach khoi tao {} (C++11)
    int *b = new int[n]{};
    cout << "Cach 2: ";
    for (int i = 0; i < n; i++) cout << b[i] << " ";
    cout << endl;

    // Cach 3: khoi tao mot so phan tu dau, con lai tu dong 0
    int *c = new int[n]{10, 20, 30};
    cout << "Cach 3: ";
    for (int i = 0; i < n; i++) cout << c[i] << " ";
    cout << endl;                     // 10 20 30 0 0

    // Cach 4: dung vong lap hoac fill
    int *d = new int[n];
    fill(d, d + n, 0);                // can <algorithm>

    delete[] a; delete[] b; delete[] c; delete[] d;
    return 0;
}
```

⚠️ **`new int[n]` (không có `()`) cho giá trị RÁC**, không phải 0. Đây là khác biệt so với mảng toàn cục (tự động 0).

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int* taoMang(int n) {
    if (n <= 0) return nullptr;

    int *a = new int[n];
    for (int i = 0; i < n; i++) a[i] = i;
    return a;                        // tra ve con tro toi vung nho HEAP
}

int main() {
    int n = 5;
    int *a = taoMang(n);

    if (a) {
        for (int i = 0; i < n; i++) cout << a[i] << " ";
        cout << endl;                // 0 1 2 3 4

        delete[] a;                  // NGUOI GOI phai giai phong
        a = nullptr;
    }
    return 0;
}
```

⚠️ **Trả về con trỏ tới bộ nhớ heap là HỢP LỆ** (khác với trả về địa chỉ biến cục bộ) — vì bộ nhớ heap tồn tại tới khi bạn `delete`.

⚠️ **Nhưng nó tạo ra vấn đề trách nhiệm:** ai phải gọi `delete[]`? Nếu người gọi quên → rò rỉ bộ nhớ. Đây là lý do C++ hiện đại tránh kiểu API này.

✅ **Cách tốt hơn:**

```cpp
vector<int> taoMang(int n) {
    vector<int> a(n);
    for (int i = 0; i < n; i++) a[i] = i;
    return a;              // tu dong giai phong, khong the ro ri
}

// Hoac dung smart pointer
unique_ptr<int[]> taoMang(int n) {
    auto a = make_unique<int[]>(n);
    for (int i = 0; i < n; i++) a[i] = i;
    return a;
}
```

### Bài 5.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

void moRong(int *&a, int &sucChua, int sucChuaMoi) {
    if (sucChuaMoi <= sucChua) return;

    int *moi = new int[sucChuaMoi]();            // ① cap phat vung moi
    copy(a, a + sucChua, moi);                   // ② copy du lieu cu sang
    delete[] a;                                  // ③ giai phong vung cu
    a = moi;                                     // ④ tro sang vung moi
    sucChua = sucChuaMoi;
}

int main() {
    int sucChua = 3;
    int *a = new int[sucChua]{10, 20, 30};

    cout << "Truoc (suc chua " << sucChua << "): ";
    for (int i = 0; i < sucChua; i++) cout << a[i] << " ";
    cout << endl;

    moRong(a, sucChua, 6);

    a[3] = 40; a[4] = 50; a[5] = 60;

    cout << "Sau  (suc chua " << sucChua << "): ";
    for (int i = 0; i < sucChua; i++) cout << a[i] << " ";
    cout << endl;

    delete[] a;
    return 0;
}
```

Output:

```
Truoc (suc chua 3): 10 20 30 
Sau  (suc chua 6): 10 20 30 40 50 60 
```

💡 **Đây chính xác là cách `vector` hoạt động bên trong** khi `push_back` làm đầy sức chứa. Lưu ý thứ tự 4 bước — làm sai thứ tự sẽ mất dữ liệu hoặc rò rỉ bộ nhớ.

💡 `int *&a` là **tham chiếu tới con trỏ** — cho phép hàm thay đổi chính con trỏ `a` ở hàm gọi.

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    cout << "Nhap so hang va so cot: ";
    cin >> n >> m;

    // ① Cap phat mang con tro
    int **a = new int*[n];
    for (int i = 0; i < n; i++) a[i] = new int[m];

    // ② Dien du lieu
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            a[i][j] = (i + 1) * (j + 1);

    // ③ In ra
    cout << "Ma tran:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) cout << setw(5) << a[i][j];
        cout << endl;
    }

    // ④ Tinh tong
    long long tong = 0;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            tong += a[i][j];
    cout << "Tong = " << tong << endl;

    // ⑤ Giai phong - NGUOC THU TU cap phat
    for (int i = 0; i < n; i++) delete[] a[i];
    delete[] a;
    a = nullptr;

    return 0;
}
```

💡 **Cách cấp phát khối liền — nhanh hơn, giải phóng dễ hơn:**

```cpp
int *duLieu = new int[n * m];                    // 1 khoi lien tuc
// Truy cap: duLieu[i * m + j] thay cho a[i][j]

delete[] duLieu;                                  // chi 1 lenh delete
```

Cách này còn nhanh hơn khi duyệt vì dữ liệu nằm liền nhau trong bộ nhớ (tốt cho cache CPU).

### Bài 7.

```cpp
int *a = new int[10];
delete a;                // LOI: phai la delete[]
```

**Lỗi:** dùng `delete` cho bộ nhớ được cấp phát bằng `new[]`.

**Hậu quả:** đây là **undefined behavior**. Với kiểu cơ bản như `int`, thực tế thường không crash (vì `int` không có destructor), nhưng:
- Có thể chỉ giải phóng một phần bộ nhớ → **rò rỉ**
- Với kiểu có destructor (`string`, class), **chỉ destructor của phần tử đầu được gọi** → rò rỉ nghiêm trọng
- Một số hệ thống phát hiện và crash ngay

**Sửa:**

```cpp
int *a = new int[10];
delete[] a;              // CO dau []
a = nullptr;
```

**Quy tắc ghép đôi:**

| Cấp phát | Giải phóng |
|---|---|
| `new T` | `delete p` |
| `new T[n]` | `delete[] p` |
| `malloc()` (C) | `free()` |

⚠️ **Không được trộn lẫn:** `malloc` + `delete`, hay `new` + `free` đều là undefined behavior.

### Bài 8.

```cpp
for (int i = 0; i < 1000; i++) {
    int *p = new int[1000];
    // ... xu ly ...
    // THIEU: delete[] p;
}
```

**Lỗi: rò rỉ bộ nhớ (memory leak).** Mỗi vòng lặp cấp phát 4000 byte mới nhưng không bao giờ giải phóng. Sau 1000 vòng, chương trình chiếm **4 MB** bộ nhớ vô ích, và con trỏ `p` bị ghi đè nên không còn cách nào lấy lại địa chỉ cũ để giải phóng.

**Sửa cách 1 — giải phóng trong vòng lặp:**

```cpp
for (int i = 0; i < 1000; i++) {
    int *p = new int[1000];
    // ... xu ly ...
    delete[] p;                  // <- THEM VAO
}
```

**Sửa cách 2 — cấp phát MỘT LẦN ngoài vòng lặp (tốt hơn nhiều):**

```cpp
int *p = new int[1000];
for (int i = 0; i < 1000; i++) {
    // ... xu ly, dung lai cung vung nho ...
}
delete[] p;
```

**Sửa cách 3 — dùng `vector` (không thể rò rỉ):**

```cpp
for (int i = 0; i < 1000; i++) {
    vector<int> v(1000);
    // ... xu ly ...
}   // tu dong giai phong o day
```

⚠️ **Rò rỉ bộ nhớ nguy hiểm vì:** chương trình chạy bình thường lúc đầu, nhưng càng chạy lâu càng chiếm nhiều RAM, cuối cùng làm chậm cả máy hoặc bị hệ điều hành giết. Với server chạy 24/7, đây là lỗi nghiêm trọng.

### Bài 9.

```cpp
int *p = new int(5);
delete p;
cout << *p;          // LOI 1: use-after-free
delete p;            // LOI 2: double free
```

**Hai lỗi nghiêm trọng:**

**① Use-after-free (dùng sau khi giải phóng):** sau `delete p`, vùng nhớ đã trả về hệ thống. `*p` đọc vào vùng nhớ không còn thuộc chương trình.
- Có thể in ra `5` (nếu chưa bị ghi đè) → **đánh lừa** người lập trình
- Có thể in ra rác
- Có thể crash

**② Double free (giải phóng 2 lần):** gọi `delete` lần thứ hai trên cùng một con trỏ.

```
free(): double free detected in tcache 2
Aborted (core dumped)
```

Đây là lỗi nghiêm trọng, có thể phá hỏng cấu trúc quản lý bộ nhớ của hệ thống, và là nguồn của nhiều lỗ hổng bảo mật.

**Sửa:**

```cpp
int *p = new int(5);
cout << *p << endl;           // dung TRUOC khi delete
delete p;
p = nullptr;                  // <- MAU CHOT

if (p) cout << *p;            // an toan, khong chay
delete p;                     // an toan! delete nullptr KHONG lam gi ca
```

✅ **Quy tắc: luôn gán `nullptr` ngay sau `delete`.** Chuẩn C++ đảm bảo `delete nullptr` là hợp lệ và không làm gì — nhờ đó `delete` nhiều lần cũng vô hại.

💡 Phát hiện bằng công cụ:

```bash
g++ -fsanitize=address -g main.cpp -o main && ./main
# AddressSanitizer: heap-use-after-free
# AddressSanitizer: attempting double-free
```

### Bài 10.

| Tiêu chí | Mảng tĩnh `int a[100]` | Mảng động `new int[n]` |
|---|---|---|
| **Kích thước xác định lúc** | Biên dịch (phải là hằng) | **Chạy** (có thể là biến) |
| **Vùng nhớ** | Stack (hoặc vùng tĩnh nếu toàn cục) | **Heap** |
| **Giới hạn kích thước** | ⚠️ Stack ~1–8 MB | Gần như toàn bộ RAM |
| **Cấp phát** | Tự động, rất nhanh | Có chi phí (gọi hệ thống) |
| **Giải phóng** | ✅ Tự động khi ra khỏi phạm vi | ⚠️ **Phải tự gọi `delete[]`** |
| **Rủi ro rò rỉ bộ nhớ** | ❌ Không | ✅ **Có** |
| **Thay đổi kích thước** | ❌ Không | ✅ Được (cấp phát lại) |
| **Tốc độ truy cập** | Rất nhanh (gần CPU cache) | Nhanh, nhưng hơi kém hơn |

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Kích thước nhỏ, biết trước | Mảng tĩnh |
| Kích thước lớn (> 1 MB) | Động, hoặc mảng toàn cục |
| Kích thước do người dùng nhập | Động |
| Cần thay đổi kích thước | Động |
| **Mọi trường hợp trong C++ hiện đại** | ✅ **`vector`** |

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    // int a[10000000];                  // 40 MB tren STACK -> CRASH
    int *b = new int[10000000];          // 40 MB tren HEAP -> OK

    b[0] = 1;
    b[9999999] = 100;
    cout << "OK: " << b[0] << " " << b[9999999] << endl;

    delete[] b;
    return 0;
}
```

**Stack vs Heap:**

| | Stack (ngăn xếp) | Heap (vùng nhớ động) |
|---|---|---|
| **Kích thước** | ⚠️ Nhỏ, cố định (1–8 MB) | Lớn (gần bằng RAM + swap) |
| **Cấp phát** | Tự động, chỉ dịch con trỏ stack — **cực nhanh** | Phải tìm vùng trống phù hợp — chậm hơn |
| **Giải phóng** | Tự động khi ra khỏi hàm | Thủ công (`delete`) |
| **Chứa gì** | Biến cục bộ, tham số hàm, địa chỉ quay về | Dữ liệu cấp phát bằng `new`/`malloc` |
| **Phân mảnh** | Không | Có thể bị |
| **Lỗi đặc trưng** | Stack overflow | Memory leak, dangling pointer |

**Sơ đồ bộ nhớ một chương trình:**

```
Dia chi cao
+------------------+
|      STACK       |  <- bien cuc bo, tham so (tang XUONG)
|        |         |
|        v         |
|                  |
|        ^         |
|        |         |
|      HEAP        |  <- new/malloc (tang LEN)
+------------------+
|   Du lieu tinh   |  <- bien toan cuc, static
+------------------+
|    Ma chuong     |  <- ma may
|      trinh       |
+------------------+
Dia chi thap
```

**Xem và tăng giới hạn stack trên Linux:**

```bash
ulimit -s              # xem gioi han (KB), thuong la 8192 = 8 MB
ulimit -s unlimited    # tang len (chi cho phien lam viec hien tai)
```

💡 **Cách khác để có mảng lớn mà không dùng heap:** khai báo **toàn cục** (ngoài `main`) — nó sẽ nằm ở vùng dữ liệu tĩnh, không giới hạn bởi stack:

```cpp
int a[10000000];        // TOAN CUC -> OK, va tu dong khoi tao 0
int main() { ... }
```

Đây là mẹo rất hay dùng trong lập trình thi đấu.

### Bài 12.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

class MyVector {
private:
    int *duLieu;
    int soLuong;        // so phan tu hien co
    int sucChua;        // suc chua toi da hien tai

    void moRong(int sucChuaMoi) {
        int *moi = new int[sucChuaMoi];
        copy(duLieu, duLieu + soLuong, moi);
        delete[] duLieu;
        duLieu = moi;
        sucChua = sucChuaMoi;
        cout << "  [Da mo rong suc chua len " << sucChua << "]" << endl;
    }

public:
    MyVector() : duLieu(new int[1]), soLuong(0), sucChua(1) {}

    ~MyVector() { delete[] duLieu; }     // DESTRUCTOR - tu dong giai phong

    void push_back(int x) {
        if (soLuong == sucChua) moRong(sucChua * 2);    // DAY -> gap doi
        duLieu[soLuong++] = x;
    }

    void pop_back() { if (soLuong > 0) soLuong--; }

    int& operator[](int i) { return duLieu[i]; }

    int size()     const { return soLuong; }
    int capacity() const { return sucChua; }

    void in() const {
        cout << "  [ ";
        for (int i = 0; i < soLuong; i++) cout << duLieu[i] << " ";
        cout << "]  size=" << soLuong << ", capacity=" << sucChua << endl;
    }
};

int main() {
    MyVector v;

    for (int i = 1; i <= 10; i++) {
        v.push_back(i * 10);
        v.in();
    }

    v[0] = 999;
    cout << "\nSau khi sua v[0]:" << endl;
    v.in();

    return 0;
}
```

Output:

```
  [ 10 ]  size=1, capacity=1
  [Da mo rong suc chua len 2]
  [ 10 20 ]  size=2, capacity=2
  [Da mo rong suc chua len 4]
  [ 10 20 30 ]  size=3, capacity=4
  [ 10 20 30 40 ]  size=4, capacity=4
  [Da mo rong suc chua len 8]
  [ 10 20 30 40 50 ]  size=5, capacity=8
  ...
```

💡 **Vì sao mở rộng GẤP ĐÔI thay vì cộng thêm 1:**

| Chiến lược | Số lần cấp phát khi thêm n phần tử | Chi phí trung bình mỗi `push_back` |
|---|---|---|
| Cộng thêm 1 mỗi lần | n lần | **O(n)** — rất chậm |
| **Gấp đôi** | log₂(n) lần | **O(1)** trung bình |

Đây gọi là **độ phức tạp khấu hao (amortized complexity)** — tuy có vài lần `push_back` tốn O(n), nhưng chia trung bình ra thì mỗi lần chỉ O(1).

💡 Destructor `~MyVector()` là cách C++ tự động giải phóng tài nguyên — nguyên tắc **RAII** (Resource Acquisition Is Initialization).

### Bài 13.

```cpp
#include <iostream>
#include <memory>
using namespace std;

int main() {
    int n;
    cout << "Nhap so phan tu: ";
    cin >> n;

    // unique_ptr cho MANG
    auto a = make_unique<int[]>(n);      // tu dong khoi tao 0

    for (int i = 0; i < n; i++) {
        cout << "  a[" << i << "] = ";
        cin >> a[i];                      // dung nhu mang binh thuong
    }

    cout << "Mang: ";
    for (int i = 0; i < n; i++) cout << a[i] << " ";
    cout << endl;

    // KHONG CAN delete[] - tu dong giai phong khi ra khoi pham vi
    return 0;
}
```

**Smart pointer** tự động giải phóng bộ nhớ khi ra khỏi phạm vi — **không thể rò rỉ, không thể quên `delete`**.

```cpp
#include <memory>

// ① unique_ptr - so huu DOC QUYEN, khong copy duoc
auto p = make_unique<int>(42);           // 1 gia tri
auto a = make_unique<int[]>(100);        // mang 100 phan tu
// delete tu dong

// ② shared_ptr - nhieu con tro cung so huu, dem so tham chieu
auto q = make_shared<int>(42);
auto r = q;                               // ca hai cung tro toi, dem = 2
// giai phong khi dem ve 0

// ③ weak_ptr - tham chieu "yeu", khong tang dem (tranh chu trinh)
```

**So sánh:**

| | Con trỏ thô | `unique_ptr` | `vector` |
|---|---|---|---|
| Phải tự `delete` | ✅ Có | ❌ Không | ❌ Không |
| Có thể rò rỉ | ✅ Có | ❌ Không | ❌ Không |
| Biết kích thước | ❌ Không | ❌ Không | ✅ Có |
| Thay đổi kích thước | Thủ công | ❌ Không | ✅ Có |
| Chi phí lúc chạy | 0 | **0** (bằng con trỏ thô) | Rất nhỏ |

✅ **Thứ tự ưu tiên trong C++ hiện đại:**
1. **`vector`/`string`** — cho dữ liệu dạng mảng (99% trường hợp)
2. **`unique_ptr`** — cho một đối tượng động
3. **`shared_ptr`** — khi cần chia sẻ quyền sở hữu
4. **Con trỏ thô** — chỉ để *quan sát*, không sở hữu; hoặc khi làm việc với API C

### Bài 14.

**Chương trình có rò rỉ:**

```cpp
// leak.cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 1000; i++) {
        int *p = new int[1000];
        p[0] = i;
        // thieu delete[] p;
    }
    cout << "Xong" << endl;
    return 0;
}
```

**Cách 1 — AddressSanitizer (dễ dùng nhất):**

```bash
g++ -fsanitize=address -g leak.cpp -o leak
./leak
```

Kết quả:

```
Xong

=================================================================
==12345==ERROR: LeakSanitizer: detected memory leaks

Direct leak of 4000000 byte(s) in 1000 object(s) allocated from:
    #0 0x7f... in operator new[](unsigned long)
    #1 0x5555... in main leak.cpp:7

SUMMARY: AddressSanitizer: 4000000 byte(s) leaked in 1000 allocation(s).
```

Thông báo chỉ rõ: **4 MB rò rỉ**, ở **dòng 7** của `leak.cpp`.

**Cách 2 — Valgrind (chi tiết hơn, không cần biên dịch lại đặc biệt):**

```bash
sudo apt install valgrind          # cai dat tren Ubuntu
g++ -g leak.cpp -o leak
valgrind --leak-check=full ./leak
```

Kết quả:

```
==12345== HEAP SUMMARY:
==12345==     in use at exit: 4,000,000 bytes in 1,000 blocks
==12345==   total heap usage: 1,001 allocs, 1 frees, 4,072,704 bytes allocated
==12345== 
==12345== 4,000,000 bytes in 1,000 blocks are definitely lost in loss record 1 of 1
==12345==    at 0x...: operator new[](unsigned long)
==12345==    by 0x...: main (leak.cpp:7)
==12345== 
==12345== LEAK SUMMARY:
==12345==    definitely lost: 4,000,000 bytes in 1,000 blocks
```

**Sau khi sửa** (thêm `delete[] p;`):

```
==12345== All heap blocks were freed -- no leaks are possible
```

💡 **Các loại rò rỉ trong báo cáo Valgrind:**

| Loại | Ý nghĩa |
|---|---|
| **definitely lost** | Chắc chắn rò rỉ — không còn con trỏ nào tới vùng nhớ |
| **indirectly lost** | Rò rỉ gián tiếp (do cấu trúc cha bị rò rỉ) |
| **possibly lost** | Có thể rò rỉ (con trỏ trỏ vào giữa vùng nhớ) |
| **still reachable** | Chưa giải phóng nhưng vẫn có con trỏ tới — thường không nghiêm trọng |

✅ **Thói quen tốt:** chạy `-fsanitize=address` khi phát triển. Nó phát hiện cả rò rỉ lẫn truy cập ngoài biên, use-after-free, double-free.

### Bài 15.

```cpp
#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

struct SinhVien {
    string ten;
    int    tuoi;
    double diemTB;
};

SinhVien* nhapDanhSach(int n) {
    SinhVien *ds = new SinhVien[n];
    for (int i = 0; i < n; i++) {
        cout << "--- Sinh vien " << i + 1 << " ---" << endl;
        cout << "Ho ten (viet lien): "; cin >> ds[i].ten;
        cout << "Tuoi              : "; cin >> ds[i].tuoi;
        cout << "Diem trung binh   : "; cin >> ds[i].diemTB;
    }
    return ds;
}

void inDanhSach(const SinhVien *ds, int n) {
    cout << "\n+-----+--------------------+-------+--------+------------+" << endl;
    cout << "| STT | HO TEN             | TUOI  | DIEM   | XEP LOAI   |" << endl;
    cout << "+-----+--------------------+-------+--------+------------+" << endl;

    cout << fixed << setprecision(2);
    for (int i = 0; i < n; i++) {
        string xl;
        if      (ds[i].diemTB >= 8.5) xl = "Gioi";
        else if (ds[i].diemTB >= 7.0) xl = "Kha";
        else if (ds[i].diemTB >= 5.0) xl = "Trung binh";
        else                          xl = "Yeu";

        cout << "| " << left  << setw(3) << i + 1
             << " | " << setw(18) << ds[i].ten
             << " | " << right << setw(5) << ds[i].tuoi
             << " | " << setw(6) << ds[i].diemTB
             << " | " << left << setw(10) << xl << " |" << endl;
    }
    cout << "+-----+--------------------+-------+--------+------------+" << endl;
}

double diemTrungBinhLop(const SinhVien *ds, int n) {
    if (n <= 0) return 0;
    double tong = 0;
    for (int i = 0; i < n; i++) tong += ds[i].diemTB;
    return tong / n;
}

int main() {
    int n;
    cout << "Nhap so sinh vien: ";
    cin >> n;

    if (n <= 0) { cout << "So luong khong hop le!" << endl; return 1; }

    SinhVien *ds = nhapDanhSach(n);

    inDanhSach(ds, n);
    cout << fixed << setprecision(2);
    cout << "Diem trung binh ca lop: " << diemTrungBinhLop(ds, n) << endl;

    delete[] ds;                 // GIAI PHONG
    ds = nullptr;

    return 0;
}
```

💡 **`delete[]` với mảng `struct` sẽ tự động gọi destructor của từng phần tử** — nhờ đó `string ten` bên trong cũng được giải phóng đúng cách. Đây chính là lý do **bắt buộc phải dùng `delete[]` chứ không phải `delete`** cho mảng.

✅ **Cách C++ hiện đại cho cùng chương trình:**

```cpp
#include <vector>

vector<SinhVien> nhapDanhSach(int n) {
    vector<SinhVien> ds(n);
    for (auto& sv : ds) { cin >> sv.ten >> sv.tuoi >> sv.diemTB; }
    return ds;
}

int main() {
    int n; cin >> n;
    auto ds = nhapDanhSach(n);
    inDanhSach(ds);
    // Khong can delete - khong the ro ri
}
```
