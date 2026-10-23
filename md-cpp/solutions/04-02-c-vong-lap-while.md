# Lời giải — [C]. Vòng Lặp While

[← Quay lại bài học](../04-02-c-vong-lap-while.md)

> **Khi nào dùng `while` thay vì `for`:** khi **không biết trước số lần lặp**, mà phụ thuộc vào một điều kiện (đọc tới khi hết dữ liệu, chia tới khi bằng 0, thử tới khi đúng).

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int i = 1;
    while (i <= n) {
        printf("%d ", i);
        i++;                       // KHONG DUOC QUEN dong nay
    }
    printf("\n");
    return 0;
}
```

**Đối chiếu `for` ↔ `while`:**

```c
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

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

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

    printf("%d co %d chu so\n", n, dem);
    return 0;
}
```

⚠️ **2 trường hợp đặc biệt hay quên:**
- `n = 0`: vòng `while (tam > 0)` không chạy lần nào → `dem = 0` (sai, phải là 1)
- `n` âm: dấu `-` không phải chữ số → dùng `abs(n)` (trong `<stdlib.h>`)

### Bài 3.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int tam = abs(n);
    int tong = 0;

    while (tam > 0) {
        tong += tam % 10;          // lay chu so cuoi
        tam /= 10;                 // bo chu so cuoi
    }

    printf("Tong cac chu so = %d\n", tong);
    return 0;
}
```

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int tam = abs(n);
    if (tam == 0) {
        printf("Chu so lon nhat = 0, nho nhat = 0\n");
        return 0;
    }

    int maxCs = 0, minCs = 9;
    while (tam > 0) {
        int cs = tam % 10;
        if (cs > maxCs) maxCs = cs;
        if (cs < minCs) minCs = cs;
        tam /= 10;
    }

    printf("Chu so lon nhat  = %d\n", maxCs);
    printf("Chu so nho nhat  = %d\n", minCs);
    return 0;
}
```

💡 **Mẹo khởi tạo:** vì chữ số chỉ từ 0 đến 9, khởi tạo `maxCs = 0` (nhỏ hơn mọi chữ số có thể) và `minCs = 9` (lớn hơn mọi chữ số) là an toàn.

Với bài toán tổng quát (mảng số bất kỳ), nên khởi tạo bằng **phần tử đầu tiên** thay vì một hằng số.

### Bài 5.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    bool am = (n < 0);
    long long tam = am ? -(long long)n : n;
    long long dao = 0;

    while (tam > 0) {
        dao = dao * 10 + tam % 10;    // day chu so cuoi cua tam vao cuoi dao
        tam /= 10;
    }

    if (am) dao = -dao;
    printf("So dao nguoc = %lld\n", dao);
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

⚠️ Dùng `long long` cho `dao` (in bằng `%lld`) vì số đảo có thể tràn: `2147483647` đảo thành `7463847412` > giới hạn `int`.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    if (n < 0) {
        printf("%d KHONG doi xung (so am)\n", n);
        return 0;
    }

    long long tam = n, dao = 0;
    while (tam > 0) {
        dao = dao * 10 + tam % 10;
        tam /= 10;
    }

    printf("%d %s so doi xung\n", n, dao == n ? "LA" : "KHONG");
    return 0;
}
```

Kiểm thử: `12321` → đối xứng; `1234` → không; `7` → đối xứng; `10` → không.

### Bài 7.

```c
#include <stdio.h>

int main(void) {
    long long tong = 0;
    int dem = 0, x;

    printf("Nhap cac so (nhap 0 de dung):\n");
    scanf("%d", &x);

    while (x != 0) {
        tong += x;
        dem++;
        scanf("%d", &x);
    }

    printf("Da nhap %d so\n", dem);
    printf("Tong          = %lld\n", tong);

    if (dem > 0) {
        printf("Trung binh    = %.4f\n", (double)tong / dem);
    } else {
        printf("Khong co so nao de tinh trung binh\n");
    }
    return 0;
}
```

**Mẫu code "đọc trước, kiểm tra sau"** (priming read): đọc giá trị đầu **trước** vòng lặp, rồi đọc giá trị tiếp ở **cuối** thân vòng lặp. Đây là mẫu chuẩn khi dùng `while` để đọc dữ liệu.

⚠️ Nhớ kiểm tra `dem > 0` trước khi chia — nếu người dùng nhập `0` ngay lần đầu thì sẽ chia cho 0.

Cách viết gọn hơn dùng `do while` (bài [04-03](../04-03-c-vong-lap-do-while.md)) hoặc tận dụng giá trị trả về của `scanf` (số biến đọc thành công):

```c
while (scanf("%d", &x) == 1 && x != 0) { tong += x; dem++; }
```

### Bài 8.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int x;
    int maxSo = -1;               // chua co so duong nao
    bool coSoDuong = false;

    printf("Nhap cac so (so am de dung):\n");
    scanf("%d", &x);

    while (x >= 0) {
        if (x > 0) {
            if (!coSoDuong || x > maxSo) {
                maxSo = x;
                coSoDuong = true;
            }
        }
        scanf("%d", &x);
    }

    if (coSoDuong) printf("So duong lon nhat = %d\n", maxSo);
    else           printf("Khong co so duong nao\n");

    return 0;
}
```

💡 **Cờ `coSoDuong`** xử lý trường hợp không có dữ liệu hợp lệ nào — rất hay bị bỏ sót.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int a, b;
    printf("Nhap 2 so: ");
    scanf("%d %d", &a, &b);

    int x = abs(a), y = abs(b);

    while (y != 0) {
        int tam = x % y;
        x = y;
        y = tam;
    }

    printf("UCLN(%d, %d) = %d\n", a, b, x);
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

💡 Thư viện chuẩn C **không có** sẵn hàm UCLN, nên bạn cần tự viết như trên (sau này sẽ gói lại thành hàm `gcd` ở chương 5).

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    long long a, b;
    printf("Nhap 2 so: ");
    scanf("%lld %lld", &a, &b);

    if (a == 0 || b == 0) {
        printf("BCNN khong xac dinh khi co so 0\n");
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

    printf("UCLN = %lld\n", ucln);
    printf("BCNN = %lld\n", bcnn);
    return 0;
}
```

**Công thức:** `BCNN(a, b) = a × b / UCLN(a, b)`

⚠️ **Rất quan trọng — viết `a / ucln * tb` chứ KHÔNG phải `a * tb / ucln`.** Với `a = b = 10⁹`, phép `a * b` = 10¹⁸ đã sát giới hạn `long long`, còn số lớn hơn sẽ tràn. Chia trước thì kết quả trung gian luôn nhỏ.

Phép chia này luôn chia hết, vì `ucln` là ước của `a`.

💡 `llabs` (trị tuyệt đối cho `long long`) nằm trong `<stdlib.h>`; đọc/in `long long` bằng `%lld`.

### Bài 11.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap so nguyen duong: ");
    scanf("%d", &n);

    if (n <= 0) { printf("Phai la so duong!\n"); return 1; }

    char nhiPhan[40];              // int toi da 32 bit -> 40 o la du
    int len = 0;
    int tam = n;

    while (tam > 0) {
        nhiPhan[len++] = (char)('0' + tam % 2);   // lay bit cuoi
        tam /= 2;
    }

    printf("%d (he 10) = ", n);
    int i = len - 1;
    while (i >= 0) {               // in nguoc lai vi ta lay tu bit thap
        printf("%c", nhiPhan[i]);
        i--;
    }
    printf(" (he 2)\n");
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

💡 C không có sẵn hàm in số dạng nhị phân (`printf` chỉ có `%o` hệ 8 và `%x`/`%X` hệ 16):

```c
printf("%o %x %X\n", 255, 255, 255);   // 377 ff FF
```

Mở rộng cho hệ bất kỳ (2–16):

```c
const char *SO = "0123456789ABCDEF";
while (tam > 0) { kq[len++] = SO[tam % coSo]; tam /= coSo; }
```

### Bài 12.

```c
#include <stdio.h>

int main(void) {
    long long x;
    printf("Nhap x: ");
    scanf("%lld", &x);

    long long a = 0, b = 1;
    int viTri = 0;

    while (a <= x) {
        long long tiep = a + b;
        a = b;
        b = tiep;
        viTri++;
    }

    printf("So Fibonacci dau tien lon hon %lld la %lld (F%d)\n", x, a, viTri);
    return 0;
}
```

Ví dụ `x = 100` → `144` (F₁₂)

Đây là ví dụ điển hình mà **`while` phù hợp hơn `for`** — ta không biết trước cần bao nhiêu vòng.

### Bài 13.

```c
int i = 1;
while (i <= 10) {
    printf("%d ", i);
    // THIEU: i++;
}
```

**Lỗi:** thiếu câu lệnh cập nhật `i++`. Biến `i` luôn bằng 1, điều kiện `i <= 10` luôn đúng → **lặp vô hạn**, in số 1 mãi mãi.

**Sửa:**

```c
int i = 1;
while (i <= 10) {
    printf("%d ", i);
    i++;                     // <- THEM VAO
}
```

**Đây là lỗi số 1 khi dùng `while`.** Danh sách kiểm tra mỗi khi viết `while`:

1. ✅ Biến điều kiện có được **cập nhật** trong thân vòng lặp không?
2. ✅ Cập nhật đó có làm điều kiện **tiến tới sai** không? (`i--` thay vì `i++` cũng gây lặp vô hạn)
3. ✅ Có nhánh `if` nào bỏ qua phần cập nhật không?

**Cách dừng chương trình bị treo:** bấm `Ctrl + C` trong terminal.

### Bài 14.

```c
int n = 5;
while (n--) printf("%d ", n);
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

Nhớ: trong C **0 là sai (false), khác 0 là đúng (true)** — nên `while (n--)` nghĩa là "lặp khi `n` còn khác 0".

Nếu đổi thành `while (--n)` (tiền tố) thì giảm trước rồi mới kiểm tra → in `4 3 2 1` (không có 0).

⚠️ Kiểu viết này rất ngắn nhưng **khó đọc**. Trong code thật nên viết rõ: `while (n > 0) { n--; ... }`

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    // Chon so ngau nhien tu 1 den 100 (hoac gan co dinh, vd: int soBiMat = 37;)
    srand((unsigned)time(NULL));
    int soBiMat = rand() % 100 + 1;

    int doan, soLan = 0;

    printf("=== TRO CHOI DOAN SO (1-100) ===\n");

    while (1) {
        printf("Doan cua ban: ");
        if (scanf("%d", &doan) != 1) return 1;   // nhap sai kieu -> thoat
        soLan++;

        if (doan == soBiMat) {
            printf("CHINH XAC! Ban da doan dung sau %d lan.\n", soLan);
            break;
        } else if (doan < soBiMat) {
            printf("  -> So bi mat LON HON %d\n", doan);
        } else {
            printf("  -> So bi mat NHO HON %d\n", doan);
        }
    }

    // Danh gia
    if      (soLan <= 7)  printf("Xuat sac! Ban dung chien luoc tim kiem nhi phan.\n");
    else if (soLan <= 12) printf("Kha tot!\n");
    else                  printf("Thu tim hieu 'tim kiem nhi phan' nhe!\n");

    return 0;
}
```

**Về hàm ngẫu nhiên:**
- `srand(time(NULL))` — gieo hạt bằng thời gian hiện tại, để mỗi lần chạy cho số khác nhau. **Chỉ gọi MỘT LẦN** ở đầu chương trình.
- `rand() % 100 + 1` — sinh số trong khoảng 1–100.
- Cần `#include <stdlib.h>` và `#include <time.h>`.

💡 **Chiến lược tối ưu để đoán:** luôn đoán vào **giữa khoảng còn lại** (bắt đầu 50, rồi 25 hoặc 75…). Cách này gọi là **tìm kiếm nhị phân** và đảm bảo tìm ra trong tối đa **7 lần** với dải 1–100 (vì 2⁷ = 128 > 100). Xem bài [10-01](../10-01-c-thuat-toan-tim-kiem-nhi-phan.md).

💡 `while (1)` kết hợp `break` (học ở bài [04-04](../04-04-c-cau-lenh-break-va-continue.md)) là mẫu chuẩn khi điều kiện dừng nằm **giữa** thân vòng lặp chứ không phải ở đầu.
