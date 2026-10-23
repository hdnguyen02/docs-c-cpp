# Lời giải — [C]. Phạm Vi Biến Và Lớp Lưu Trữ

[← Quay lại bài học](../05-04-c-pham-vi-bien-va-lop-luu-tru.md)

> **Phạm vi (scope):** tên biến dùng được ở **đâu** trong code.
> **Thời gian tồn tại (lifetime):** biến sống **bao lâu** khi chương trình chạy.
> Biến cục bộ thường: phạm vi hẹp, sống ngắn. Biến `static` cục bộ: phạm vi hẹp, sống suốt chương trình. Biến toàn cục: phạm vi rộng, sống suốt chương trình.

---

### Bài 1.

**Output:**

```
4 3 1
```

**Giải thích từng tầng:**

```c
int a = 1;                 // a#1 (tang ngoai)
{
    int a = 2;             // a#2 che khuat a#1
    {
        a = 3;             // chua co a moi -> gan vao a#2, a#2 = 3
        int a = 4;         // a#3 che khuat a#2 tu day tro xuong
        printf("%d ", a);  // a#3 -> 4
    }
    printf("%d ", a);      // a#2 -> 3
}
printf("%d\n", a);         // a#1 -> 1
```

💡 **Điểm dễ nhầm:** dòng `a = 3;` đứng **trước** `int a = 4;` nên lúc đó tên `a` vẫn chỉ biến `a#2` của khối giữa. Phạm vi của một biến bắt đầu **từ vị trí khai báo**, không phải từ đầu khối.

⚠️ Code thực tế đừng bao giờ đặt tên trùng kiểu này. Dùng `gcc -Wshadow` để compiler cảnh báo mỗi khi có biến che khuất biến khác.

### Bài 2.

**Lỗi:** biến `i` khai báo trong phần khởi tạo của `for` nên chỉ tồn tại **bên trong** vòng lặp. Ra khỏi vòng lặp, `i` không còn nữa:

```
error: 'i' undeclared (first use in this function)
```

**Sửa:** khai báo `i` **bên ngoài** vòng lặp:

```c
#include <stdio.h>

int main(void) {
    int i;
    for (i = 1; i * i <= 1000; i++) { }   // than rong, chi de tim i
    printf("%d\n", i);                     // 32  (32*32 = 1024 > 1000)
    return 0;
}
```

💡 Vòng lặp dừng ngay khi `i * i <= 1000` sai, tức là `i` đầu tiên có `i * i > 1000`. Giá trị này vẫn còn trong `i` sau vòng lặp vì giờ `i` thuộc phạm vi của `main`.

### Bài 3.

```c
#include <stdio.h>

void goiHam(void) {
    static int soLan = 0;      // khoi tao DUNG 1 LAN
    soLan++;
    printf("Ham duoc goi lan thu %d\n", soLan);
}

int main(void) {
    for (int i = 0; i < 4; i++) {
        goiHam();
    }
    return 0;
}
```

Output:

```
Ham duoc goi lan thu 1
Ham duoc goi lan thu 2
Ham duoc goi lan thu 3
Ham duoc goi lan thu 4
```

💡 `soLan` chỉ dùng được bên trong `goiHam` (không hàm nào khác sửa được nó), nhưng vẫn giữ giá trị giữa các lần gọi. Đây là ưu điểm của `static` cục bộ so với biến toàn cục.

### Bài 4.

```c
#include <stdio.h>

void goiHam(void) {
    int soLan = 0;             // KHONG static: tao moi moi lan goi
    soLan++;
    printf("Ham duoc goi lan thu %d\n", soLan);
}

int main(void) {
    for (int i = 0; i < 4; i++) {
        goiHam();
    }
    return 0;
}
```

Output:

```
Ham duoc goi lan thu 1
Ham duoc goi lan thu 1
Ham duoc goi lan thu 1
Ham duoc goi lan thu 1
```

**Giải thích:** không có `static`, `soLan` là biến cục bộ thường (lớp lưu trữ `auto`). Mỗi lần gọi hàm:

```
goi ham  -> tao bien soLan moi, gan = 0
soLan++  -> soLan = 1, in ra 1
het ham  -> soLan bi HUY
```

Lần gọi sau lại bắt đầu từ đầu, nên lúc nào cũng in `1`.

| | Có `static` | Không `static` |
|---|---|---|
| Dòng khởi tạo `= 0` chạy | **1 lần** duy nhất | **Mỗi lần** gọi hàm |
| Khi hàm kết thúc | Biến **vẫn còn** | Biến **bị huỷ** |
| Kết quả | 1 2 3 4 | 1 1 1 1 |

### Bài 5.

```c
#include <stdio.h>

long long soDu = 0;            // BIEN TOAN CUC - moi ham deu thay

void napTien(long long x) {
    if (x > 0) soDu += x;
}

int rutTien(long long x) {
    if (x <= 0 || x > soDu) return 0;   // khong hop le / khong du tien
    soDu -= x;
    return 1;
}

int main(void) {
    napTien(500000);
    printf("Nap 500000   -> so du: %lld\n", soDu);

    if (rutTien(200000)) printf("Rut 200000   -> so du: %lld\n", soDu);
    else                 printf("Rut 200000   -> THAT BAI\n");

    if (rutTien(1000000)) printf("Rut 1000000  -> so du: %lld\n", soDu);
    else                  printf("Rut 1000000  -> THAT BAI, khong du tien (so du %lld)\n", soDu);

    napTien(50000);
    printf("Nap 50000    -> so du: %lld\n", soDu);
    return 0;
}
```

Output:

```
Nap 500000   -> so du: 500000
Rut 200000   -> so du: 300000
Rut 1000000  -> THAT BAI, khong du tien (so du 300000)
Nap 50000    -> so du: 350000
```

⚠️ **Nhược điểm của biến toàn cục:** ở đây bất kỳ hàm nào cũng có thể viết `soDu = -999;` mà không qua kiểm tra. Chương trình càng lớn càng khó biết ai đã sửa `soDu`. Cách an toàn hơn là truyền con trỏ tới số dư vào hàm (`void napTien(long long *soDu, long long x)`, xem bài [05-03](../05-03-c-truyen-tham-tri-va-truyen-con-tro.md)), hoặc ít nhất đánh dấu `static` để chỉ file này truy cập được.

### Bài 6.

```c
#include <stdio.h>

int toanCuc;                   // toan cuc, khong khoi tao
int mangToanCuc[5];            // mang toan cuc, khong khoi tao

void inStatic(void) {
    static int s;              // static cuc bo, khong khoi tao
    printf("static cuc bo   = %d\n", s);
}

int main(void) {
    printf("toan cuc        = %d\n", toanCuc);
    inStatic();
    printf("mang toan cuc   = ");
    for (int i = 0; i < 5; i++) printf("%d ", mangToanCuc[i]);
    printf("\n");
    return 0;
}
```

Output:

```
toan cuc        = 0
static cuc bo   = 0
mang toan cuc   = 0 0 0 0 0 
```

**Quy tắc:** mọi biến có thời gian tồn tại suốt chương trình (toàn cục, `static`) mà không khởi tạo sẽ được **tự động gán 0** (với mảng: mọi phần tử là 0).

⚠️ **Vì sao không nên in thử biến cục bộ thường chưa khởi tạo:**

```c
#include <stdio.h>

int main(void) {
    int x;                 // cuc bo, KHONG khoi tao
    printf("%d\n", x);     // UNDEFINED BEHAVIOR
    return 0;
}
```

- `x` chứa **giá trị rác** — bất cứ thứ gì còn sót lại trong ô nhớ đó. Có lần in ra `0`, có lần in số lạ, đổi máy/đổi mức tối ưu là đổi kết quả.
- Theo chuẩn C, đọc biến này là **hành vi không xác định**, compiler được phép sinh ra code làm bất cứ điều gì.
- Nếu tình cờ thấy in ra `0`, bạn sẽ tưởng biến cục bộ cũng mặc định bằng 0 — một hiểu lầm rất nguy hiểm. `gcc -Wall` sẽ cảnh báo `'x' is used uninitialized`.

✅ **Luôn khởi tạo biến cục bộ** trước khi đọc: `int x = 0;`.

### Bài 7.

**Output:**

```
21 11 21 12 12
```

**Giải thích:**

| Lời gọi | `x` được dùng | Diễn biến | In ra |
|---|---|---|---|
| `f()` | `x` **cục bộ** của `f` | tạo mới = 20, tăng lên 21, huỷ khi hết hàm | `21` |
| `g()` | `x` **toàn cục** | 10 → 11 | `11` |
| `f()` | `x` cục bộ **mới** | lại tạo = 20 → 21 | `21` |
| `g()` | `x` toàn cục | 11 → 12 | `12` |
| `main` | `x` toàn cục | không đổi | `12` |

💡 Trong `f`, biến cục bộ `x` **che khuất** biến toàn cục cùng tên, nên `f` không hề đụng tới `x` toàn cục. `g` không có `x` riêng nên dùng `x` toàn cục.

### Bài 8.

```c
#include <stdio.h>

int sinhMa(void) {
    static int maHienTai = 0;
    maHienTai++;
    return maHienTai;
}

int main(void) {
    for (int i = 0; i < 5; i++) {
        printf("SV%03d\n", sinhMa());
    }
    return 0;
}
```

Output:

```
SV001
SV002
SV003
SV004
SV005
```

💡 `%03d` in số nguyên đủ 3 chữ số, thiếu thì thêm `0` phía trước.

💡 Đây là mẫu **bộ sinh mã tự tăng** rất hay gặp: người gọi không cần biết (và không thể sửa) biến đếm bên trong, chỉ việc gọi `sinhMa()` là có mã mới không trùng.

### Bài 9.

```c
#include <stdio.h>

long long fiboTiepTheo(void) {
    static long long a = 0, b = 1;   // 2 so Fibonacci lien tiep
    long long kq = a;
    long long tiep = a + b;
    a = b;
    b = tiep;
    return kq;
}

int main(void) {
    for (int i = 0; i < 15; i++) {
        printf("%lld ", fiboTiepTheo());
    }
    printf("\n");
    return 0;
}
```

Output:

```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
```

**Cách hoạt động:** hai biến `static` `a`, `b` luôn giữ "cặp số hiện tại". Mỗi lần gọi, hàm trả về `a` rồi dịch cặp số lên một bước:

```
lan 1: (a,b) = (0,1) -> tra 0, thanh (1,1)
lan 2: (a,b) = (1,1) -> tra 1, thanh (1,2)
lan 3: (a,b) = (1,2) -> tra 1, thanh (2,3)
...
```

⚠️ `long long` chỉ chứa được tới khoảng số Fibonacci thứ 92. Gọi nhiều hơn sẽ tràn số.

### Bài 10.

**File `bodem.c`:**

```c
int soLuong = 0;           // DINH NGHIA bien toan cuc

void them(void) {
    soLuong++;
}
```

**File `main.c`:**

```c
#include <stdio.h>

extern int soLuong;        // KHAI BAO: soLuong dinh nghia o bodem.c
void them(void);           // nguyen mau ham o bodem.c

int main(void) {
    for (int i = 0; i < 3; i++) them();
    printf("soLuong = %d\n", soLuong);
    return 0;
}
```

**Biên dịch và chạy:**

```bash
gcc -std=c11 -Wall main.c bodem.c -o main
./main
```

Output:

```
soLuong = 3
```

**Phân biệt định nghĩa và khai báo biến:**

| Dòng | Loại | Cấp phát bộ nhớ? | Số lần được phép |
|---|---|---|---|
| `int soLuong = 0;` | **Định nghĩa** | ✅ Có | Đúng 1 lần trong cả chương trình |
| `extern int soLuong;` | **Khai báo** | ❌ Không | Bao nhiêu lần cũng được |

💡 Trong dự án thật, dòng `extern int soLuong;` và nguyên mẫu `void them(void);` được đặt trong file `bodem.h`, `main.c` chỉ cần `#include "bodem.h"` — giống cách tổ chức ở bài [05-02](../05-02-c-khai-bao-nguyen-mau-ham.md).

### Bài 11.

Đổi `bodem.c` thành:

```c
static int soLuong = 0;    // chi thay duoc trong bodem.c

void them(void) {
    soLuong++;
}
```

Biên dịch lại cùng `main.c` của bài 10 → **lỗi liên kết**:

```
undefined reference to `soLuong'
collect2: error: ld returned 1 exit status
```

**Giải thích:** `static` ở mức file làm cho `soLuong` **không được "công bố" ra ngoài** file `bodem.c`. Từng file vẫn biên dịch được (`main.c` tin lời khai báo `extern`), nhưng tới bước liên kết, linker đi tìm biến `soLuong` công khai thì không có.

**Cách để `main.c` vẫn đọc được giá trị mà không bỏ `static`:** viết thêm một hàm "cửa ngõ" trong `bodem.c`:

**File `bodem.c`:**

```c
static int soLuong = 0;

void them(void) {
    soLuong++;
}

int laySoLuong(void) {     // ham cong khai, tra ve gia tri
    return soLuong;
}
```

**File `main.c`:**

```c
#include <stdio.h>

void them(void);
int laySoLuong(void);

int main(void) {
    for (int i = 0; i < 3; i++) them();
    printf("soLuong = %d\n", laySoLuong());
    return 0;
}
```

💡 Lúc này `main.c` **đọc** được `soLuong` nhưng **không sửa** trực tiếp được — chỉ có thể tăng qua `them()`. Đây là cách C "đóng gói" dữ liệu: giấu biến bằng `static`, chỉ cho truy cập qua hàm.

### Bài 12.

```c
#include <stdio.h>

int main(void) {
    register int r = 5;
    printf("%p\n", (void *)&r);    // LOI
    return 0;
}
```

**Kết quả: lỗi biên dịch.**

```
error: address of register variable 'r' requested
```

**Giải thích:** `register` gợi ý đặt biến trong **thanh ghi** của CPU. Thanh ghi không nằm trong bộ nhớ RAM nên **không có địa chỉ**. Vì vậy chuẩn C cấm dùng `&` với biến `register` — kể cả khi trình biên dịch thực tế vẫn để biến đó trong RAM.

💡 Hệ quả: biến `register` không thể truyền cho hàm cần con trỏ, ví dụ `scanf("%d", &r)` cũng lỗi.

💡 Ngày nay trình biên dịch tự quyết định biến nào nên nằm trong thanh ghi tốt hơn lập trình viên, nên `register` gần như không còn được dùng. Bạn chỉ cần biết để đọc hiểu code cũ.

### Bài 13.

**Lỗi:** giá trị khởi tạo của biến `static` phải là **hằng số** biết được lúc biên dịch. `n` là tham số, chỉ biết khi chạy:

```
error: initializer element is not constant
```

Lý do: biến `static` được khởi tạo **một lần trước khi chương trình chạy**, lúc đó chưa có lời gọi hàm nào nên chưa có `n`.

**Sửa:** khởi tạo bằng hằng số, rồi xử lý `n` bằng câu lệnh bình thường:

```c
#include <stdio.h>

void f(int n) {
    static int tong = 0;       // hang so -> hop le
    tong += n;
    printf("%d\n", tong);
}

int main(void) {
    f(1); f(2); f(3);
    return 0;
}
```

Output:

```
1
3
6
```

💡 Nếu thực sự muốn "lần gọi đầu tiên lấy `n` làm giá trị ban đầu", dùng thêm một biến cờ `static`:

```c
void f2(int n) {
    static int daKhoiTao = 0, giaTri = 0;
    if (!daKhoiTao) { giaTri = n; daKhoiTao = 1; }
    ...
}
```

### Bài 14.

```c
#include <stdio.h>

double themSo(double x) {
    static double tong = 0;
    static int dem = 0;
    tong += x;
    dem++;
    return tong / dem;
}

int main(void) {
    double x;
    printf("Nhap cac so (nhap 0 de dung):\n");
    while (scanf("%lf", &x) == 1 && x != 0) {
        printf("  -> Trung binh hien tai: %.2f\n", themSo(x));
    }
    return 0;
}
```

Ví dụ chạy:

```
Nhap cac so (nhap 0 de dung):
4
  -> Trung binh hien tai: 4.00
8
  -> Trung binh hien tai: 6.00
3
  -> Trung binh hien tai: 5.00
0
```

💡 `tong` và `dem` nhớ toàn bộ "lịch sử" các lần gọi, `main` không phải tự lưu gì cả. Đọc `double` bằng `%lf`, in bằng `%.2f`.

⚠️ Nhược điểm của cách dùng `static` này: hàm **không thể "làm lại từ đầu"** — muốn tính trung bình cho một dãy mới thì `tong`, `dem` vẫn còn giá trị cũ. Khi cần nhiều bộ đếm độc lập, tốt hơn là lưu `tong`, `dem` ở nơi gọi và truyền con trỏ vào hàm.

### Bài 15.

```c
#include <stdio.h>

int toanCuc = 0;              // (3) toan cuc: moi ham, moi file (qua extern)
static int toanCucFile = 0;   // (4) toan cuc static: moi ham, CHI file nay

void demo(void) {
    int cucBo = 0;            // (1) cuc bo thuong: tao moi moi lan goi
    static int cucBoTinh = 0; // (2) cuc bo static: giu gia tri giua cac lan goi

    cucBo++;
    cucBoTinh++;
    toanCuc++;
    toanCucFile += 10;

    printf("cucBo = %d | cucBoTinh = %d | toanCuc = %d | toanCucFile = %d\n",
           cucBo, cucBoTinh, toanCuc, toanCucFile);
}

int main(void) {
    for (int i = 0; i < 3; i++) demo();

    // printf("%d", cucBo);        // LOI: cucBo chi ton tai trong demo()
    // printf("%d", cucBoTinh);    // LOI: cucBoTinh cung chi thay trong demo()
    printf("Trong main: toanCuc = %d, toanCucFile = %d\n", toanCuc, toanCucFile);
    return 0;
}
```

Output:

```
cucBo = 1 | cucBoTinh = 1 | toanCuc = 1 | toanCucFile = 10
cucBo = 1 | cucBoTinh = 2 | toanCuc = 2 | toanCucFile = 20
cucBo = 1 | cucBoTinh = 3 | toanCuc = 3 | toanCucFile = 30
Trong main: toanCuc = 3, toanCucFile = 30
```

**Bảng so sánh:**

| Loại | Khai báo | Phạm vi | Thời gian tồn tại | Mặc định | Nên dùng khi |
|---|---|---|---|---|---|
| **Cục bộ thường** | `int x;` trong hàm | Trong khối lệnh | Tới hết khối lệnh | Rác | **Mặc định** cho mọi biến tạm |
| **Cục bộ `static`** | `static int x;` trong hàm | Trong khối lệnh | Suốt chương trình | 0 | Hàm cần "nhớ" giữa các lần gọi (bộ đếm, sinh mã) |
| **Toàn cục** | `int x;` ngoài hàm | Cả file + file khác qua `extern` | Suốt chương trình | 0 | Dữ liệu thật sự dùng chung, mảng rất lớn |
| **Toàn cục `static`** | `static int x;` ngoài hàm | Chỉ trong file | Suốt chương trình | 0 | Dữ liệu nội bộ của một file/module |

**Nguyên tắc chọn:**
1. **Ưu tiên biến cục bộ** + truyền qua tham số / giá trị trả về — dễ đọc, dễ kiểm thử.
2. Cần nhớ trạng thái giữa các lần gọi → **`static` cục bộ** (phạm vi vẫn hẹp).
3. Buộc phải dùng chung giữa nhiều hàm → **toàn cục**, và nếu chỉ trong một file thì thêm **`static`**.
4. Chỉ dùng `extern` khi thực sự chia sẻ biến giữa nhiều file, và đặt khai báo `extern` trong file `.h`.

⚠️ **Mảng rất lớn** (vd `int a[1000000]`) nên khai báo **toàn cục** hoặc `static`: biến cục bộ nằm trên stack vốn có kích thước giới hạn (thường vài MB), mảng quá lớn trên stack có thể làm chương trình crash (stack overflow).
