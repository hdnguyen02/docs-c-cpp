# Lời giải — [C]. Define, Typedef Và Enum

[← Quay lại bài học](../02-09-c-define-typedef-va-enum.md)

---

### Bài 1.

```c
#include <stdio.h>

typedef long long          ll;
typedef unsigned long long ull;
typedef struct {
    int x;
    int y;
} Diem;

int main() {
    ll  n = 9123456789012345LL;
    ull u = 18446744073709551615ULL;     // gia tri lon nhat cua unsigned long long
    Diem p = {10, 20};

    printf("ll   : %lld\n", n);
    printf("ull  : %llu\n", u);
    printf("Diem : %d %d\n", p.x, p.y);
    return 0;
}
```

Output:

```
ll   : 9123456789012345
ull  : 18446744073709551615
Diem : 10 20
```

**So sánh có và không có typedef cho struct:**

```c
struct Diem2 { int x; int y; };
struct Diem2 a = {1, 2};       // khong typedef: phai viet ca "struct"

typedef struct { int x; int y; } Diem;
Diem b = {1, 2};               // co typedef: gon hon
```

💡 `typedef` còn giúp đọc dễ hơn với các kiểu phức tạp như con trỏ hàm:

```c
typedef int (*HamXuLy)(int, int);   // HamXuLy la kieu "con tro toi ham nhan 2 int, tra int"
HamXuLy f;                          // de doc hon: int (*f)(int, int);
```

### Bài 2.

```c
#include <stdio.h>

enum Ngay { THU2 = 2, THU3, THU4, THU5, THU6, THU7, CHUNHAT };

typedef enum { MUA_XUAN, MUA_HA, MUA_THU, MUA_DONG } Mua;

int main() {
    printf("THU2    = %d\n", THU2);
    printf("THU3    = %d\n", THU3);
    printf("THU4    = %d\n", THU4);
    printf("THU5    = %d\n", THU5);
    printf("THU6    = %d\n", THU6);
    printf("THU7    = %d\n", THU7);
    printf("CHUNHAT = %d\n", CHUNHAT);

    enum Ngay d = THU4;     // khong typedef: phai viet "enum Ngay"
    Mua m = MUA_THU;        // co typedef: chi can "Mua"
    printf("d = %d, m = %d\n", d, m);
    return 0;
}
```

Output:

```
THU2    = 2
THU3    = 3
THU4    = 4
THU5    = 5
THU6    = 6
THU7    = 7
CHUNHAT = 8
d = 4, m = 2
```

**Quy tắc đánh số của enum:**
- Không gán gì → hằng đầu tiên là `0`, các hằng sau tăng dần 1 (`MUA_XUAN = 0` ... `MUA_DONG = 3`).
- Gán `THU2 = 2` → các hằng sau tiếp tục `3, 4, 5...` nên `CHUNHAT = 8`.

⚠️ Trong C, biến enum thực chất là số nguyên: `enum Ngay d = 100;` vẫn biên dịch được, trình biên dịch **không** chặn giá trị ngoài danh sách.

### Bài 3.

```c
#include <stdio.h>

#define PI  3.14159
#define INF 1000000000
#define MOD 1000000007

int main() {
    printf("PI  = %.5f\n", PI);
    printf("INF = %d\n", INF);
    printf("MOD = %d\n", MOD);
    return 0;
}
```

Output:

```
PI  = 3.14159
INF = 1000000000
MOD = 1000000007
```

**Ý nghĩa thực tế:**
- `INF` = "vô cùng lớn" — dùng khi tìm giá trị nhỏ nhất: `int min = INF;`. Chọn 10⁹ vì nó nhỏ hơn giới hạn `int` (≈2,1×10⁹) nên an toàn khi so sánh; nhưng lưu ý `INF + INF` (2×10⁹) đã **vượt** giới hạn `int`.
- `MOD = 10⁹+7` — số nguyên tố hay dùng trong các bài đếm kết quả rất lớn, phải lấy dư.

⚠️ `PI` được thay bằng `3.14159` là hằng `double` nên in bằng `%f`; `INF`, `MOD` là hằng `int` nên in bằng `%d`. Dùng sai đặc tả (`%d` cho `PI`) sẽ in ra rác.

### Bài 4.

```c
#include <stdio.h>

#define PI_DEFINE 3.14159
const double PI_CONST = 3.14159;

int main() {
    double r = 5.0;
    printf("Dung #define : %f\n", PI_DEFINE * r * r);
    printf("Dung const   : %f\n", PI_CONST  * r * r);
    return 0;
}
```

Output:

```
Dung #define : 78.539750
Dung const   : 78.539750
```

**So sánh:**

| Tiêu chí | `#define PI 3.14159` | `const double PI = 3.14159;` |
|---|---|---|
| Ai xử lý | Preprocessor — **thay thế văn bản mù quáng** trước khi biên dịch | Compiler — là một biến thực sự |
| Có kiểu dữ liệu | ❌ Không. Chỉ là dãy ký tự | ✅ Có (`double`) |
| Kiểm tra kiểu | ❌ Không | ✅ Có |
| Debug được | ❌ Không. Debugger không biết `PI` là gì | ✅ Có, xem được giá trị |
| Tôn trọng phạm vi (scope) | ❌ Không — có hiệu lực tới cuối file, kể cả bên trong hàm khác | ✅ Có |
| Dùng làm kích thước mảng toàn cục, nhãn `case` | ✅ Được | ❌ **Không** — trong C, biến `const` không phải "hằng số biên dịch" |

Ví dụ `#define` gây lỗi khó hiểu:

```c
#define MAX 100
void thu(void) {
    int MAX = 5;        // -> bi thay thanh: int 100 = 5;
    // error: expected identifier or '(' before numeric constant
}
```

✅ **Kết luận:** trong C, dùng `const` khi cần một **giá trị có kiểu**, được kiểm tra và debug được. Dùng `#define` (hoặc `enum`) khi cần **hằng số biên dịch** như kích thước mảng toàn cục hay nhãn `case` của `switch`.

### Bài 5.

```c
#include <stdio.h>

#define FOR(i, a, b) for (int i = (a); i <= (b); i++)

int main() {
    FOR(i, 1, 10) {
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

Output: `1 2 3 4 5 6 7 8 9 10`

**Lưu ý quan trọng:** phải bọc `(a)` và `(b)` trong ngoặc. Nếu viết `for(int i = a; i <= b; i++)` thì khi gọi `FOR(i, 1, n-1)` sẽ thành `i <= n-1` — may mắn là đúng; nhưng `FOR(i, 1, n&1)` sẽ thành `i <= n&1`, tức `(i <= n) & 1` do `<=` có độ ưu tiên cao hơn `&` → sai.

⚠️ Vòng `for (int i = ...)` khai báo biến trong `for` cần chuẩn **C99 trở lên** (gcc mặc định đã bật chuẩn mới, hoặc thêm `-std=c11`).

### Bài 6.

```c
#include <stdio.h>

#define MAX(a, b) ((a) > (b) ? (a) : (b))

int main() {
    printf("%d\n", MAX(3, 7));        // 7
    printf("%d\n", MAX(2 + 3, 4));    // 5
    return 0;
}
```

Output:

```
7
5
```

**Vì sao phải bọc ngoặc khắp nơi:** nếu viết `#define MAX(a,b) a > b ? a : b` thì:

```c
int x = 10 - MAX(2, 3);
// bi thay thanh:  int x = 10 - 2 > 3 ? 2 : 3;
// -> (10 - 2) > 3 ? 2 : 3 -> x = 2   (ky vong 10 - 3 = 7)
```

✅ Muốn an toàn tuyệt đối (có kiểm tra kiểu, tham số chỉ tính 1 lần) thì viết **hàm**:

```c
int maxInt(int a, int b) { return a > b ? a : b; }
```

### Bài 7.

```c
#include <stdio.h>

#define BINH_PHUONG(x) x * x

int main() {
    printf("%d\n", BINH_PHUONG(2 + 3));
    return 0;
}
```

**Output: `11`** (kỳ vọng là 25)

**Giải thích:** macro hoạt động bằng **thay thế văn bản thuần tuý**, không hiểu gì về toán học:

```
BINH_PHUONG(2 + 3)
    -> thay x boi chuoi "2 + 3"
    -> 2 + 3 * 2 + 3
    -> 2 + 6 + 3          (nhan truoc cong sau!)
    -> 11
```

Đây là bẫy kinh điển nhất của macro.

### Bài 8.

**Sửa bằng cách bọc ngoặc đầy đủ:**

```c
#define BINH_PHUONG(x) ((x) * (x))

printf("%d\n", BINH_PHUONG(2 + 3));
// -> ((2 + 3) * (2 + 3)) -> 5 * 5 -> 25   ✔
```

**Nhưng vẫn còn vấn đề — tác dụng phụ (side effect):**

```c
int i = 3;
printf("%d\n", BINH_PHUONG(i++));
// -> ((i++) * (i++))
// -> i BI TANG HAI LAN! Ket qua co the la 3 * 4 = 12 (khong phai 9), va i = 5
```

Thực ra kết quả là *undefined behavior* (hành vi không xác định) vì `i` bị sửa 2 lần trong cùng một biểu thức — mỗi trình biên dịch có thể cho một kết quả khác. gcc với `-Wall` sẽ cảnh báo `operation on 'i' may be undefined`.

✅ **Giải pháp đúng trong C: dùng hàm** (có thể thêm `static inline` để gợi ý compiler chèn thẳng thân hàm, không chậm hơn macro):

```c
#include <stdio.h>

static inline int binhPhuong(int x) {
    return x * x;
}

int main() {
    int i = 3;
    printf("%d\n", binhPhuong(i++));   // 9 dung, i chi tang 1 lan
    printf("i = %d\n", i);             // 4
    return 0;
}
```

**Hàm có ưu điểm gì so với macro:** tham số chỉ được tính **một lần**, có kiểm tra kiểu, debug được, tôn trọng phạm vi, và compiler vẫn tối ưu (inline) nên không chậm hơn. Nhược điểm: C không có nạp chồng hàm, nên hàm `int` không dùng cho `double` được — phải viết thêm hàm riêng.

### Bài 9.

| Tiêu chí | `#define` | `typedef` | `enum` | `const` |
|---|---|---|---|---|
| **Ai xử lý** | Preprocessor (trước biên dịch) | Compiler | Compiler | Compiler |
| **Bản chất** | Thay thế văn bản | Tạo bí danh cho kiểu | Tạo nhóm hằng số nguyên có tên | Tạo biến chỉ đọc |
| **Kiểm tra kiểu** | ❌ Không | ✅ Có | ⚠️ Có nhưng lỏng (enum = int) | ✅ Có |
| **Kết thúc bằng `;`** | ❌ Không | ✅ Có | ✅ Có | ✅ Có |
| **Bắt đầu bằng `#`** | ✅ Có | ❌ Không | ❌ Không | ❌ Không |
| **Tôn trọng scope** | ❌ Không (tới cuối file) | ✅ Có | ✅ Có | ✅ Có |
| **Dùng cho hằng số** | ✅ Được (mọi kiểu) | ❌ Không | ✅ Chỉ hằng **nguyên** | ✅ Được (mọi kiểu) |
| **Là hằng số biên dịch** (kích thước mảng toàn cục, `case`) | ✅ Có | — | ✅ Có | ❌ Không |
| **Dùng cho kiểu dữ liệu** | ⚠️ Được nhưng không nên | ✅ **Nên dùng** | ✅ Tạo kiểu mới `enum X` | ❌ Không |
| **Dùng cho câu lệnh/macro hàm** | ✅ Được (cẩn thận!) | ❌ Không | ❌ Không | ❌ Không |
| **Debug được** | ❌ Không | ✅ Có | ✅ Có | ✅ Có |

**Tóm tắt nên dùng gì:**
- Nhóm hằng số nguyên có liên quan (trạng thái, ngày, màu...) → `enum`
- Giá trị hằng có kiểu (số thực, chuỗi...) → `const`, hoặc `#define` khi cần hằng biên dịch
- Bí danh kiểu → `typedef`
- Thay hàm ngắn → hàm `static inline`
- `#define` → hằng biên dịch, `#ifdef` (biên dịch có điều kiện) và header guard

**Minh hoạ sự khác nhau về `;` giữa `typedef` và `#define`:**

```c
#define PTR_INT int*
typedef int* PtrInt;

PTR_INT a, b;    // -> int* a, b;  => a la con tro, b chi la int!
PtrInt  c, d;    // c va d deu la con tro int
```

### Bài 10.

```c
#include <stdio.h>

#define ll            long long
#define FOR(i, a, b)  for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define SQR(x)        ((x) * (x))

int main() {
    FOR(i, 1, 5) printf("%d ", i);           // 1 2 3 4 5
    printf("\n");

    FORD(i, 5, 1) printf("%d ", i);          // 5 4 3 2 1
    printf("\n");

    ll tong = 0;
    FOR(i, 1, 100000) tong += SQR((ll)i);    // ep ll de tranh tran so
    printf("Tong binh phuong 1..100000 = %lld\n", tong);
    return 0;
}
```

Output:

```
1 2 3 4 5 
5 4 3 2 1 
Tong binh phuong 1..100000 = 333338333350000
```

⚠️ **Nhớ ép `(ll)i` trong `SQR`** — nếu viết `SQR(i)` thì `i * i` tính bằng `int`, với `i = 100000` được 10¹⁰ → tràn số.

⚠️ Đây là phong cách **chỉ dành cho lập trình thi đấu** — nơi bạn code một mình, code xong vứt, và mỗi giây gõ phím đều quý. **Tuyệt đối không dùng trong dự án thật hay bài tập nộp thầy cô**, vì người khác đọc sẽ rất khổ.

### Bài 11.

```c
typedef 3.14 PI;      // LOI BIEN DICH
```

Thông báo lỗi (gcc):

```
error: expected identifier or '(' before numeric constant
```

**Giải thích:** `typedef` **chỉ đặt bí danh cho KIỂU DỮ LIỆU**, không đặt tên cho giá trị. `3.14` là một giá trị (literal), không phải kiểu.

So sánh:

```c
typedef double SoThuc;        // DUNG: dat ten cho KIEU double
typedef 3.14 PI;              // SAI:  3.14 khong phai mot kieu

#define PI 3.14               // DUOC (define thay the van ban bat ky)
const double PI = 3.14;       // DUOC: bien chi doc co kieu
```

Đây chính là điểm khác biệt cốt lõi trong bảng ở bài 9: `#define` thay thế **bất kỳ chuỗi ký tự nào**, còn `typedef` chỉ làm việc với **kiểu**.

### Bài 12.

```c
#include <stdio.h>

typedef int Matrix[3][3];

int main() {
    Matrix m = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%4d", m[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

Output:

```
   1   2   3
   4   5   6
   7   8   9
```

**Cách đọc `typedef int Matrix[3][3];`:** viết như khai báo một biến `int Matrix[3][3];` rồi thêm `typedef` phía trước → `Matrix` trở thành **tên kiểu** "mảng 3×3 số nguyên".

**Lợi ích rõ nhất của bí danh kiểu** là khi viết hàm:

```c
// Khong co bi danh
void inMaTran(int m[3][3]);

// Co bi danh - ro rang hon
void inMaTran(Matrix m);
```

💡 `%4d` in số nguyên canh phải trong độ rộng 4 ký tự, giúp các cột thẳng hàng.

### Bài 13.

```c
#include <stdio.h>

#define DEBUG          // <- xoa hoac comment dong nay de TAT che do debug

#ifdef DEBUG
    #define LOG(x) printf("[DEBUG] %s = %d\n", #x, (x))
#else
    #define LOG(x)     // khi khong debug, LOG(x) bien thanh rong -> khong ton gi
#endif

int main() {
    int a = 10, b = 3;
    int tong = a + b;

    LOG(a);
    LOG(b);
    LOG(tong);
    LOG(a * b);

    printf("Ket qua: %d\n", tong);
    return 0;
}
```

Khi **có** `#define DEBUG`:

```
[DEBUG] a = 10
[DEBUG] b = 3
[DEBUG] tong = 13
[DEBUG] a * b = 30
Ket qua: 13
```

Khi **xoá** dòng `#define DEBUG`: chỉ in `Ket qua: 13`.

**Các chỉ thị tiền xử lý có điều kiện:**

| Chỉ thị | Ý nghĩa |
|---|---|
| `#ifdef X` | Biên dịch đoạn sau nếu `X` **đã** được define |
| `#ifndef X` | Biên dịch nếu `X` **chưa** được define |
| `#if <bieu thuc>` | Biên dịch nếu biểu thức khác 0 |
| `#else`, `#elif` | Nhánh thay thế |
| `#endif` | Kết thúc khối điều kiện |

**Toán tử `#x`** (stringize) biến tên biến thành chuỗi — nhờ nó mà `LOG(tong)` in ra được cả chữ `"tong"`. Macro `LOG` ở trên dùng `%d` nên chỉ in được giá trị kiểu `int`.

**Ứng dụng phổ biến nhất — header guard** (chống include trùng lặp):

```c
// file mylib.h
#ifndef MYLIB_H
#define MYLIB_H

// noi dung header...

#endif
```

Bạn cũng có thể bật/tắt DEBUG **từ dòng lệnh** mà không sửa code (khi đó xoá dòng `#define DEBUG` trong file):

```bash
gcc -DDEBUG main.c -o main      # bat debug
gcc main.c -o main              # tat debug
```

### Bài 14.

```c
/*
 * ============================================================
 *  Template thi dau (competitive programming) bang C
 *  Luu y: phong cach nay CHI dung khi code mot minh trong ky thi.
 * ============================================================
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdbool.h>

// ---------- Bi danh kieu ----------
typedef long long ll;              // so nguyen lon, tranh tran khi n^2 > 2 ty
typedef unsigned long long ull;
typedef long double ld;            // do chinh xac cao hon double

// ---------- Hang so ----------
#define INF  1000000007            // "vo cung" cho kieu int
#define LINF 1000000000000000000LL // "vo cung" cho kieu long long
#define MOD  1000000007LL          // so nguyen to hay dung de lay du
#define EPS  1e-9                  // sai so cho phep khi so sanh so thuc
#define MAXN 200005                // kich thuoc mang toan cuc

// ---------- Shortcut ----------
#define FOR(i, a, b)  for (int i = (a); i <= (b); i++)
#define FORD(i, a, b) for (int i = (a); i >= (b); i--)
#define MAX(a, b)     ((a) > (b) ? (a) : (b))
#define MIN(a, b)     ((a) < (b) ? (a) : (b))
#define SQR(x)        ((x) * (x))

ll a[MAXN];                        // mang lon dat toan cuc (tranh tran stack)

int main() {
    int n;
    if (scanf("%d", &n) != 1 || n < 1 || n >= MAXN) return 0;

    FOR(i, 0, n - 1) scanf("%lld", &a[i]);

    ll tong = 0, lonNhat = -LINF, nhoNhat = LINF;
    FOR(i, 0, n - 1) {
        tong += a[i];
        lonNhat = MAX(lonNhat, a[i]);
        nhoNhat = MIN(nhoNhat, a[i]);
    }

    printf("Tong = %lld\n", tong);
    printf("Nho nhat = %lld, Lon nhat = %lld\n", nhoNhat, lonNhat);
    return 0;
}
```

Ví dụ input `5` rồi `3 -1 7 2 9`:

```
Tong = 20
Nho nhat = -1, Lon nhat = 9
```

**Giải thích 3 dòng quan trọng nhất:**

1. `#define MAXN 200005` + mảng **toàn cục** `ll a[MAXN];` — mảng lớn khai báo trong `main` nằm trên stack (thường chỉ vài MB) dễ gây tràn stack. Mảng toàn cục nằm vùng nhớ tĩnh, không bị giới hạn này. Kích thước mảng toàn cục phải là hằng số biên dịch nên dùng `#define` chứ không dùng `const int`.

2. `scanf`/`printf` — trong C đây đã là cách nhập xuất nhanh. Điều kiện `scanf(...) != 1` giúp dừng an toàn khi input lỗi.

3. `#define LINF 1000000000000000000LL` — hậu tố `LL` bắt buộc để hằng có kiểu `long long`. `MAX`/`MIN` là macro nên dùng được cả với `long long`.

### Bài 15.

Code gốc viết lại thành C thông thường:

```c
#include <stdio.h>

int main() {
    long long binhPhuong[5];
    int n = 5;    // so phan tu cua mang

    // Tinh binh phuong cac so tu 1 den 5
    for (int i = 0; i < n; i++) {
        binhPhuong[i] = (long long)(i + 1) * (i + 1);
    }

    // In ket qua
    for (int i = 0; i < n; i++) {
        printf("%lld ", binhPhuong[i]);
    }
    printf("\n");

    return 0;
}
```

Output: `1 4 9 16 25`

**Bảng đối chiếu từng dòng:**

| Code thi đấu | Code thường |
|---|---|
| `ll` | `long long` |
| `SQR(i+1)` | `(i + 1) * (i + 1)` |
| `sz(a)` | `sizeof(a) / sizeof(a[0])` — ở đây ghi thẳng `n = 5` |
| `FOR(i,0,sz(a)-1)` | `for (int i = 0; i < n; i++)` |

⚠️ **Những điểm cần để ý trong code gốc:**
- `FOR` khai báo biến `ll i` rồi so sánh với `sz(a)-1` kiểu `int` — chạy được, nhưng code thường dùng `int i` cho rõ ràng.
- `main` thiếu `return 0;` — từ C99 `main` tự trả về 0 nên vẫn đúng, nhưng viết rõ vẫn tốt hơn.
- `SQR(i+1)` chỉ đúng vì macro đã bọc ngoặc `((x)*(x))`; nếu định nghĩa `x*x` sẽ ra `i+1*i+1` như bài 7.
- `sz(a)` dùng `sizeof` chỉ đúng với **mảng thật**. Nếu `a` là tham số hàm (thực chất là con trỏ), `sizeof(a)` trả kích thước con trỏ → sai số phần tử.

**Bài học:** macro giúp gõ nhanh, nhưng cũng **giấu đi các lỗi**. Đó là lý do chỉ nên dùng khi bạn đã hiểu rõ code bên dưới nó làm gì.
