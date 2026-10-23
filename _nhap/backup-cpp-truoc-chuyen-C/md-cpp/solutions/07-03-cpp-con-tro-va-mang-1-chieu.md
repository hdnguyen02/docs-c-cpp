# Lời giải — [C++]. Con Trỏ Và Mảng 1 Chiều

[← Quay lại bài học](../07-03-cpp-con-tro-va-mang-1-chieu.md)

> **Điểm cốt lõi:** tên mảng chính là **địa chỉ của phần tử đầu tiên**, và `a[i]` chỉ là cách viết tắt của `*(a + i)`.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;              // khong can &a[0] - ten mang DA LA dia chi

    cout << "Cach 1 (con tro + chi so): ";
    for (int i = 0; i < 5; i++) cout << p[i] << " ";
    cout << endl;

    cout << "Cach 2 (so hoc con tro) : ";
    for (int i = 0; i < 5; i++) cout << *(p + i) << " ";
    cout << endl;

    cout << "Cach 3 (dich con tro)   : ";
    for (int *q = a; q < a + 5; q++) cout << *q << " ";
    cout << endl;

    return 0;
}
```

Cả 3 cách đều in: `10 20 30 40 50`

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;

    cout << "i\ta[i]\t*(a+i)\tp[i]\t*(p+i)" << endl;
    cout << "-----------------------------------------" << endl;
    for (int i = 0; i < 5; i++) {
        cout << i << "\t" << a[i] << "\t" << *(a + i)
             << "\t" << p[i] << "\t" << *(p + i) << endl;
    }

    // Kiem chung bang dia chi
    cout << "\nTat ca deu cung dia chi:" << endl;
    cout << "&a[2]    = " << &a[2]    << endl;
    cout << "a + 2    = " << a + 2    << endl;
    cout << "&p[2]    = " << &p[2]    << endl;
    cout << "p + 2    = " << p + 2    << endl;
    return 0;
}
```

Output:

```
i	a[i]	*(a+i)	p[i]	*(p+i)
-----------------------------------------
0	10	10	10	10
1	20	20	20	20
...
```

**Quy tắc chuyển đổi của compiler:**

```
a[i]  ==  *(a + i)
p[i]  ==  *(p + i)
```

Vì phép cộng có tính giao hoán, `*(a+i) == *(i+a) == i[a]` — nên `2[a]` cũng hợp lệ và bằng `a[2]`! (Đương nhiên không nên viết như vậy.)

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int    a[5] = {1, 2, 3, 4, 5};
    double b[5] = {1.1, 2.2, 3.3, 4.4, 5.5};
    char   c[5] = {'a', 'b', 'c', 'd', 'e'};

    cout << "--- Mang int (4 byte/phan tu) ---" << endl;
    for (int i = 0; i < 5; i++) cout << "&a[" << i << "] = " << &a[i] << endl;

    cout << "\n--- Mang double (8 byte/phan tu) ---" << endl;
    for (int i = 0; i < 5; i++) cout << "&b[" << i << "] = " << &b[i] << endl;

    cout << "\n--- Mang char (1 byte/phan tu) ---" << endl;
    for (int i = 0; i < 5; i++) cout << "&c[" << i << "] = " << (void*)&c[i] << endl;

    cout << "\n--- Khoang cach ---" << endl;
    cout << "int    : " << (char*)&a[1] - (char*)&a[0] << " byte" << endl;
    cout << "double : " << (char*)&b[1] - (char*)&b[0] << " byte" << endl;
    cout << "char   : " << (char*)&c[1] - (char*)&c[0] << " byte" << endl;
    return 0;
}
```

**Nhận xét:** các phần tử nằm **liên tiếp** trong bộ nhớ, cách nhau đúng `sizeof(kiểu)` byte.

```
int    a: 0x1000, 0x1004, 0x1008, 0x100c, 0x1010   (cach 4)
double b: 0x2000, 0x2008, 0x2010, 0x2018, 0x2020   (cach 8)
char   c: 0x3000, 0x3001, 0x3002, 0x3003, 0x3004   (cach 1)
```

⚠️ **Phải ép `(void*)` khi in địa chỉ của `char`** — nếu không, `cout` hiểu `char*` là **chuỗi** và in nội dung chuỗi thay vì địa chỉ.

💡 Đây chính là lý do `p + 1` nhảy khác nhau tuỳ kiểu: compiler tự nhân với `sizeof(kiểu)`.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

long long tongMang(const int *a, int n) {
    long long tong = 0;
    const int *ketThuc = a + n;

    for (const int *p = a; p < ketThuc; p++) {
        tong += *p;
    }
    return tong;
}

int main() {
    int a[6] = {10, 20, 30, 40, 50, 60};
    cout << "Tong = " << tongMang(a, 6) << endl;    // 210
    return 0;
}
```

💡 Tính sẵn `ketThuc = a + n` ngoài vòng lặp, thay vì viết `p < a + n` (tính lại mỗi vòng). Compiler thường tự tối ưu, nhưng viết rõ vẫn tốt hơn.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int* timMax(int *a, int n) {
    if (n <= 0) return nullptr;

    int *max = a;
    for (int *p = a + 1; p < a + n; p++) {
        if (*p > *max) max = p;
    }
    return max;
}

int main() {
    int a[6] = {10, 45, 30, 90, 50, 20};

    int *p = timMax(a, 6);
    if (p) {
        cout << "Gia tri lon nhat = " << *p << endl;          // 90
        cout << "Tai vi tri       = " << p - a << endl;       // 3
        *p = 0;                                                // sua duoc qua con tro
        cout << "Sau khi dat ve 0: a[3] = " << a[3] << endl;  // 0
    }
    return 0;
}
```

💡 **Lợi ích trả về con trỏ:** vừa biết giá trị (`*p`), vừa biết vị trí (`p - a`), lại **sửa được** phần tử đó.

Đây chính là cách `std::max_element` hoạt động:

```cpp
#include <algorithm>
int *p = max_element(a, a + 6);
```

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[5] = {10, 20, 30, 40, 50};

    cout << "Duyet nguoc: ";
    for (int *p = a + 4; p >= a; p--) {
        cout << *p << " ";
    }
    cout << endl;                       // 50 40 30 20 10

    // Cach khac - an toan hon (tranh p < a la undefined behavior)
    cout << "Cach 2     : ";
    for (int *p = a + 5; p > a; ) {
        p--;
        cout << *p << " ";
    }
    cout << endl;
    return 0;
}
```

⚠️ **Lưu ý kỹ thuật:** khi `p = a` rồi `p--`, con trỏ trỏ vào vị trí **trước** mảng — về mặt chuẩn C++ đây là *undefined behavior* (dù thực tế hầu như luôn chạy đúng). Cách 2 an toàn hơn vì con trỏ không bao giờ đi trước `a`.

C++ cho phép con trỏ trỏ tới vị trí **ngay sau** phần tử cuối (`a + n`) — đó là lý do `end()` của mọi container đều hợp lệ.

### Bài 7.

```cpp
#include <iostream>
using namespace std;

int main() {
    int a[10] = {0,1,2,3,4,5,6,7,8,9};

    int *p = &a[2];
    int *q = &a[7];

    cout << "p tro toi a[2] = " << *p << endl;
    cout << "q tro toi a[7] = " << *q << endl;

    cout << "\nq - p = " << q - p << endl;        // 5 (SO PHAN TU, khong phai byte)
    cout << "p - q = " << p - q << endl;          // -5

    cout << "\nKhoang cach byte thuc te = "
         << (char*)q - (char*)p << " byte" << endl;   // 20 = 5 * 4

    // Ung dung: tinh vi tri
    cout << "\nVi tri cua p trong mang = " << p - a << endl;   // 2
    return 0;
}
```

**Điểm mấu chốt: hiệu 2 con trỏ cho SỐ PHẦN TỬ giữa chúng, không phải số byte.**

```
q - p = (dia chi q - dia chi p) / sizeof(int)
      = (0x101c - 0x1008) / 4
      = 20 / 4
      = 5
```

**Ứng dụng phổ biến nhất** — tìm vị trí của một phần tử:

```cpp
int *p = find(a, a + n, x);
int viTri = p - a;                 // doi con tro thanh chi so
```

⚠️ Hiệu 2 con trỏ **chỉ có ý nghĩa** khi chúng trỏ vào cùng một mảng.

### Bài 8.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

void daoNguoc(int *a, int n) {
    int *trai  = a;
    int *phai  = a + n - 1;

    while (trai < phai) {
        swap(*trai, *phai);
        trai++;
        phai--;
    }
}

int main() {
    int a[6] = {1, 2, 3, 4, 5, 6};

    cout << "Truoc: ";
    for (int x : a) cout << x << " ";
    cout << endl;

    daoNguoc(a, 6);

    cout << "Sau  : ";
    for (int x : a) cout << x << " ";
    cout << endl;                       // 6 5 4 3 2 1
    return 0;
}
```

**Kỹ thuật 2 con trỏ** — hai con trỏ tiến từ hai đầu vào giữa. Điều kiện `trai < phai` tự động dừng đúng chỗ với cả `n` chẵn và lẻ.

💡 C++ có sẵn: `reverse(a, a + n);`

### Bài 9.

```cpp
int a[5] = {10,20,30,40,50};
int *p = a;
cout << *p << " " << *p++ << " " << *p << endl;
cout << *(a+2) << " " << *a+2 << endl;
```

**Dòng 1 — KHÔNG ĐOÁN TRƯỚC ĐƯỢC (undefined behavior).**

Biểu thức có `p++` (sửa `p`) và đồng thời đọc `*p` ở 2 chỗ khác, mà **thứ tự tính các toán hạng của `<<` không được chuẩn quy định** (trước C++17). Kết quả có thể là `10 10 20`, `20 10 20`, hoặc khác — tuỳ compiler.

✅ **Không bao giờ viết code kiểu này.** Tách ra:

```cpp
cout << *p << " ";
cout << *p << " ";
p++;
cout << *p << endl;
```

**Dòng 2 — kết quả rõ ràng: `30 12`**

| Biểu thức | Kết quả | Giải thích |
|---|---|---|
| `*(a+2)` | **30** | Cộng địa chỉ trước (`a+2` trỏ tới `a[2]`), rồi giải tham chiếu |
| `*a+2` | **12** | Giải tham chiếu trước (`*a` = `a[0]` = 10), rồi cộng 2 |

**Lý do:** toán tử `*` (giải tham chiếu) có **độ ưu tiên cao hơn** `+`.

✅ **Luôn đặt ngoặc cho rõ:** viết `*(a+2)` hoặc `a[2]`, đừng dựa vào độ ưu tiên.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

void trongHam(int a[]) {
    cout << "Trong ham : sizeof(a) = " << sizeof(a) << " byte" << endl;
}

int main() {
    int a[10] = {1,2,3,4,5,6,7,8,9,10};
    int *p = a;

    cout << "sizeof(a) = " << sizeof(a) << " byte" << endl;   // 40
    cout << "sizeof(p) = " << sizeof(p) << " byte" << endl;   // 8

    cout << "So phan tu = " << sizeof(a) / sizeof(a[0]) << endl;   // 10

    trongHam(a);                                               // 8

    cout << "\nDia chi: a = " << a << ", p = " << p << endl;   // GIONG NHAU
    return 0;
}
```

Output:

```
sizeof(a) = 40 byte
sizeof(p) = 8 byte
So phan tu = 10
Trong ham : sizeof(a) = 8 byte
Dia chi: a = 0x7ffd..., p = 0x7ffd...
```

**Giải thích:**

| | `a` (tên mảng) | `p` (con trỏ) |
|---|---|---|
| Kiểu thực sự | `int[10]` | `int*` |
| `sizeof` | 40 (= 10 × 4) — **toàn bộ mảng** | 8 — chỉ là một địa chỉ |
| Gán lại được? | ❌ Không (`a = p` báo lỗi) | ✅ Có |

**Tên mảng KHÔNG phải con trỏ** — nó là một *mảng*, chỉ **tự động chuyển** thành con trỏ khi cần (array-to-pointer decay). `sizeof` là một trong những chỗ mà sự chuyển đổi này **không** xảy ra.

⚠️ **Hệ quả quan trọng:** khi truyền mảng vào hàm, nó **đã suy biến thành con trỏ**, nên `sizeof` bên trong hàm cho 8 chứ không phải 40. Đây là lý do **luôn phải truyền kèm kích thước `n`**.

Mẹo `sizeof(a)/sizeof(a[0])` **chỉ dùng được trong cùng phạm vi khai báo mảng**.

### Bài 11.

```cpp
#include <iostream>
#include <cstring>
using namespace std;

// Phien ban tu viet cua memcpy cho mang int
void copyMang(int *dich, const int *nguon, int n) {
    for (int i = 0; i < n; i++) {
        *(dich + i) = *(nguon + i);
    }
}

// Phien ban dung con tro dich chuyen
void copyMang2(int *dich, const int *nguon, int n) {
    const int *ketThuc = nguon + n;
    while (nguon < ketThuc) {
        *dich++ = *nguon++;          // gan roi tang ca hai con tro
    }
}

int main() {
    int a[5] = {10, 20, 30, 40, 50};
    int b[5], c[5];

    copyMang(b, a, 5);
    copyMang2(c, a, 5);

    cout << "b: "; for (int x : b) cout << x << " "; cout << endl;
    cout << "c: "; for (int x : c) cout << x << " "; cout << endl;

    // Dung memcpy co san (lam viec theo BYTE)
    int d[5];
    memcpy(d, a, 5 * sizeof(int));
    cout << "d: "; for (int x : d) cout << x << " "; cout << endl;

    return 0;
}
```

💡 `*dich++ = *nguon++` là thành ngữ kinh điển của C: gán giá trị rồi tăng cả hai con trỏ. Rất ngắn gọn nhưng khó đọc với người mới.

⚠️ **`memcpy` làm việc theo BYTE**, nên phải nhân với `sizeof(int)`. Nếu quên, chỉ copy được 5 byte thay vì 20.

✅ C++ có `std::copy` an toàn hơn: `copy(a, a + 5, b);`

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int* timKiem(int *a, int n, int x) {
    for (int *p = a; p < a + n; p++) {
        if (*p == x) return p;
    }
    return nullptr;                  // khong tim thay
}

int main() {
    int a[6] = {10, 25, 30, 45, 50, 25};

    int *p = timKiem(a, 6, 45);
    if (p) cout << "Tim thay 45 tai vi tri " << p - a << endl;      // 3
    else   cout << "Khong tim thay 45" << endl;

    p = timKiem(a, 6, 99);
    if (p) cout << "Tim thay 99 tai vi tri " << p - a << endl;
    else   cout << "Khong tim thay 99" << endl;

    return 0;
}
```

💡 So sánh 2 quy ước báo "không tìm thấy":
- Trả về **`nullptr`** (con trỏ) — rõ ràng, không nhầm lẫn
- Trả về **`-1`** (chỉ số) — phổ biến, nhưng phải nhớ kiểm tra

STL dùng quy ước thứ ba: trả về **`end()`** (vị trí ngay sau phần tử cuối):

```cpp
#include <algorithm>
int *p = find(a, a + 6, 45);
if (p != a + 6) cout << "Tim thay tai " << p - a;
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

void inDoan(const char *nhan, const int *batDau, const int *ketThuc) {
    cout << nhan << " (" << ketThuc - batDau << " phan tu): ";
    for (const int *p = batDau; p < ketThuc; p++) cout << *p << " ";
    cout << endl;
}

int main() {
    int a[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = 9;
    int giua = n / 2;

    inDoan("Toan bo   ", a, a + n);
    inDoan("Nua dau   ", a, a + giua);
    inDoan("Nua sau   ", a + giua, a + n);

    // Chia lam 3 phan
    cout << endl;
    inDoan("Phan 1    ", a,         a + 3);
    inDoan("Phan 2    ", a + 3,     a + 6);
    inDoan("Phan 3    ", a + 6,     a + 9);
    return 0;
}
```

Output:

```
Toan bo    (9 phan tu): 1 2 3 4 5 6 7 8 9 
Nua dau    (4 phan tu): 1 2 3 4 
Nua sau    (5 phan tu): 5 6 7 8 9 

Phan 1     (3 phan tu): 1 2 3 
Phan 2     (3 phan tu): 4 5 6 
Phan 3     (3 phan tu): 7 8 9 
```

💡 **Cặp con trỏ `[batDau, ketThuc)`** — đây chính là mô hình **iterator** mà toàn bộ STL sử dụng: `sort(v.begin(), v.end())`, `find(a, a+n, x)`. Quy ước là "bao gồm đầu, không bao gồm cuối", nhờ đó `ketThuc - batDau` cho ngay số phần tử.

### Bài 14.

```cpp
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 10000000;
    vector<int> v(N);
    for (int i = 0; i < N; i++) v[i] = i % 100;

    int *a = v.data();

    // ① Duyet bang chi so
    auto t1 = high_resolution_clock::now();
    long long tong1 = 0;
    for (int i = 0; i < N; i++) tong1 += a[i];
    auto t2 = high_resolution_clock::now();
    cout << "Chi so     : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ② Duyet bang con tro
    t1 = high_resolution_clock::now();
    long long tong2 = 0;
    for (int *p = a; p < a + N; p++) tong2 += *p;
    t2 = high_resolution_clock::now();
    cout << "Con tro    : " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ③ Range-based for
    t1 = high_resolution_clock::now();
    long long tong3 = 0;
    for (int x : v) tong3 += x;
    t2 = high_resolution_clock::now();
    cout << "Range-based: " << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    cout << "\nKiem tra: " << (tong1 == tong2 && tong2 == tong3 ? "OK" : "SAI") << endl;
    return 0;
}
```

Kết quả tham khảo (biên dịch với `-O2`):

```
Chi so     : 8 ms
Con tro    : 8 ms
Range-based: 8 ms

Kiem tra: OK
```

**Kết luận: TỐC ĐỘ GẦN NHƯ BẰNG NHAU.**

**Vì sao:** compiler hiện đại (với `-O2`) nhận ra `a[i]` và `*(a+i)` là **cùng một thứ** và sinh ra mã máy giống hệt nhau.

⚠️ Nếu biên dịch **không tối ưu** (`-O0`), duyệt bằng con trỏ có thể nhanh hơn 10–20% — nhưng không ai chạy chương trình thật ở chế độ đó.

💡 **Bài học quan trọng:** đừng hy sinh tính dễ đọc để "tối ưu" những thứ compiler đã tự làm. Hãy viết `for (int x : v)` — rõ ràng nhất và cũng nhanh nhất.

Kiểm chứng bằng cách so sánh assembly:

```bash
g++ -O2 -S main.cpp -o out.s
```

### Bài 15.

```cpp
#include <iostream>
using namespace std;

// ===== strlen: dem so ky tu den truoc '\0' =====
size_t myStrlen(const char *s) {
    const char *p = s;
    while (*p != '\0') p++;
    return p - s;                    // hieu 2 con tro = do dai
}

// ===== strcpy: sao chep chuoi (KE CA ky tu '\0') =====
char* myStrcpy(char *dich, const char *nguon) {
    char *batDau = dich;
    while ((*dich++ = *nguon++) != '\0');    // gan, roi kiem tra
    return batDau;
}

// ===== strcmp: so sanh 2 chuoi =====
int myStrcmp(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) { s1++; s2++; }
    return (unsigned char)*s1 - (unsigned char)*s2;
}

// ===== strcat: noi chuoi =====
char* myStrcat(char *dich, const char *nguon) {
    char *batDau = dich;
    while (*dich) dich++;                     // di toi cuoi chuoi dich
    while ((*dich++ = *nguon++) != '\0');     // noi chuoi nguon vao
    return batDau;
}

int main() {
    const char *s = "codelab";
    cout << "myStrlen(\"codelab\") = " << myStrlen(s) << endl;      // 7

    char buf[50];
    myStrcpy(buf, "Hello");
    cout << "Sau myStrcpy: " << buf << endl;                        // Hello

    myStrcat(buf, " World");
    cout << "Sau myStrcat: " << buf << endl;                        // Hello World

    cout << "\nmyStrcmp:" << endl;
    cout << "  (\"abc\", \"abc\") = " << myStrcmp("abc", "abc") << endl;   // 0
    cout << "  (\"abc\", \"abd\") = " << myStrcmp("abc", "abd") << endl;   // am
    cout << "  (\"abd\", \"abc\") = " << myStrcmp("abd", "abc") << endl;   // duong
    cout << "  (\"abc\", \"ab\")  = " << myStrcmp("abc", "ab")  << endl;   // duong
    return 0;
}
```

**Giải thích `myStrcpy`:**

```cpp
while ((*dich++ = *nguon++) != '\0');
//       └─ ① gan ky tu
//          └─ ② tang ca hai con tro
//             └─ ③ kiem tra ky tu vua gan co phai '\0' khong
```

Vòng lặp **cũng sao chép luôn ký tự `'\0'`** rồi mới dừng — đúng như hành vi của `strcpy` chuẩn.

**Giá trị trả về của `strcmp`:**
- `0` — hai chuỗi bằng nhau
- `< 0` — `s1` đứng trước `s2` theo thứ tự từ điển
- `> 0` — `s1` đứng sau `s2`

⚠️ **Những hàm này rất nguy hiểm trong thực tế:**

```cpp
char buf[5];
strcpy(buf, "Chuoi rat dai");     // TRAN BO DEM - ghi de bo nho, crash hoac lo hong bao mat
```

`strcpy` **không kiểm tra kích thước đích**. Đây là nguyên nhân của vô số lỗ hổng bảo mật "buffer overflow" trong lịch sử phần mềm.

✅ **Trong C++, luôn dùng `std::string`:**

```cpp
#include <string>
string s = "codelab";
cout << s.length();               // thay strlen
string t = s;                     // thay strcpy - tu quan ly bo nho
if (s == t) { ... }               // thay strcmp - doc hon nhieu
s += " dev";                      // thay strcat - tu mo rong
```

`std::string` **tự động cấp phát đủ bộ nhớ**, không bao giờ tràn bộ đệm.
