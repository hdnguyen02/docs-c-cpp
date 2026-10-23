# Lời giải — [C]. Chuyển Đổi Giữa Số Và Chuỗi

[← Quay lại bài học](../09-04-c-chuyen-doi-giua-so-va-chuoi.md)

> **Trong C:** `snprintf()` (`<stdio.h>`) cho số → chuỗi, và các hàm `atoi`/`atoll`/`atof`, `strtol`/`strtoll`/`strtod` (`<stdlib.h>`) cho chuỗi → số. Chỉ họ `strto*` mới **báo lỗi** được.

---

### Bài 1.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    int       a = 42;
    long long b = 9123456789012345LL;
    float     c = 3.14f;
    double    d = 2.718281828459045;
    char      e = 'A';

    char sa[32], sb[32], sc[32], sd[32], se[2];
    snprintf(sa, sizeof(sa), "%d", a);
    snprintf(sb, sizeof(sb), "%lld", b);
    snprintf(sc, sizeof(sc), "%f", c);      // float duoc nang len double
    snprintf(sd, sizeof(sd), "%f", d);
    se[0] = e; se[1] = '\0';                // char -> chuoi

    printf("int       -> \"%s\" (do dai %zu)\n", sa, strlen(sa));
    printf("long long -> \"%s\"\n", sb);
    printf("float     -> \"%s\"\n", sc);
    printf("double    -> \"%s\"\n", sd);
    printf("char      -> \"%s\"\n", se);

    // Ung dung: ghep so vao chuoi
    char kq[50];
    snprintf(kq, sizeof(kq), "Diem la %d/10", 9);
    printf("\nKet qua: %s\n", kq);
    return 0;
}
```

Output:

```
int       -> "42" (do dai 2)
long long -> "9123456789012345"
float     -> "3.140000"
double    -> "2.718282"
char      -> "A"

Ket qua: Diem la 9/10
```

💡 **`%f` mặc định in 6 chữ số thập phân.** Khác với việc chỉ đổi số, `snprintf` cho phép định dạng tuỳ ý: `"%.2f"`, `"%10d"`, `"%05d"`... (xem bài 9).

⚠️ `snprintf(s, n, "%d", 'A')` cho `"65"` chứ không phải `"A"` — vì `char` được coi là số. Dùng `"%c"` hoặc gán trực tiếp `s[0] = 'A'; s[1] = '\0';`.

💡 Giá trị trả về của `snprintf` là **số ký tự lẽ ra được ghi** (không tính `'\0'`). Nếu giá trị này `>= n` nghĩa là kết quả đã bị **cắt bớt**.

### Bài 2.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const char *s1 = "42";
    const char *s2 = "9123456789012345";
    const char *s3 = "3.14";
    const char *s4 = "2.718281828459045";

    int       a = atoi(s1);
    long long b = atoll(s2);
    float     c = (float)atof(s3);
    double    d = strtod(s4, NULL);

    printf("atoi   : %d\n", a);
    printf("atoll  : %lld\n", b);
    printf("atof   : %g\n", c);
    printf("strtod : %.15f\n", d);

    // atoi voi phan thua
    printf("\natoi(\"123abc\") = %d\n", atoi("123abc"));   // 123
    printf("atoi(\"  45\")   = %d\n", atoi("  45"));       // 45 (bo qua khoang trang dau)
    printf("atoi(\"-7\")     = %d\n", atoi("-7"));         // -7
    printf("atoi(\"abc\")    = %d\n", atoi("abc"));        // 0 (khong bao loi!)
    printf("atof(\"1e3\")    = %g\n", atof("1e3"));        // 1000
    return 0;
}
```

**Bảng các hàm chuyển đổi (`<stdlib.h>`):**

| Hàm | Kiểu trả về | Báo lỗi? |
|---|---|---|
| `atoi(s)` | `int` | ❌ |
| `atol(s)` | `long` | ❌ |
| `atoll(s)` | `long long` | ❌ |
| `atof(s)` | `double` | ❌ |
| `strtol(s, &end, base)` | `long` | ✅ |
| `strtoll(s, &end, base)` | `long long` | ✅ |
| `strtoul(s, &end, base)` | `unsigned long` | ✅ |
| `strtoull(s, &end, base)` | `unsigned long long` | ✅ |
| `strtof(s, &end)` | `float` | ✅ |
| `strtod(s, &end)` | `double` | ✅ |

💡 Các hàm này **bỏ qua khoảng trắng ở đầu** và **dừng ở ký tự không hợp lệ đầu tiên**.

### Bài 3.

```c
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int chuyenSo(const char *s) {
    char *end;
    errno = 0;
    long n = strtol(s, &end, 10);

    if (end == s) {
        printf("  Loi: \"%s\" khong phai so hop le\n", s);
        return 0;
    }
    if (errno == ERANGE || n < INT_MIN || n > INT_MAX) {
        printf("  Loi: \"%s\" vuot qua pham vi kieu int\n", s);
        return 0;
    }
    if (*end != '\0') {
        printf("  Canh bao: co ky tu thua sau so (\"%s\")\n", end);
    }
    return (int)n;
}

int main(void) {
    const char *ds[] = {"42", "abc", "123abc", "99999999999999999999", "", "  7  ", "-15"};
    int soLuong = sizeof(ds) / sizeof(ds[0]);

    for (int i = 0; i < soLuong; i++) {
        printf("strtol(\"%s\"):\n", ds[i]);
        int kq = chuyenSo(ds[i]);
        printf("  -> %d\n\n", kq);
    }
    return 0;
}
```

**Hai loại lỗi và cách phát hiện:**

| Lỗi | Cách phát hiện |
|---|---|
| Chuỗi **không bắt đầu** bằng số hợp lệ (`"abc"`, `""`) | `end == s` (không đọc được chữ số nào) |
| Số **vượt phạm vi** kiểu dữ liệu | `errno == ERANGE` (nhớ gán `errno = 0` trước khi gọi) |

💡 **Tham số thứ hai `&end`** cho biết `strtol` đã đọc tới đâu — dùng để phát hiện ký tự thừa:

```c
char *end;
long n = strtol("123abc", &end, 10);
// n = 123, end tro toi "abc"  ->  con "abc" chua doc
```

⚠️ **`strtol` KHÔNG báo lỗi với `"123abc"`** — nó lặng lẽ nhận 123. Phải tự kiểm tra `*end != '\0'`. Với `"  7  "` cũng sẽ có cảnh báo vì còn 2 dấu cách ở cuối.

⚠️ `long` trên Windows chỉ có 32 bit (bằng `int`), nên kiểm tra `n < INT_MIN || n > INT_MAX` giúp code đúng trên mọi hệ thống.

### Bài 4.

```c
#include <stdio.h>
#include <string.h>

// Ghi n duoi dang chuoi vao kq (kq can it nhat 21 ky tu)
void soThanhChuoi(long long n, char *kq) {
    if (n == 0) { strcpy(kq, "0"); return; }

    int am = (n < 0);
    unsigned long long tam = am ? -(unsigned long long)n : (unsigned long long)n;

    int len = 0;
    while (tam > 0) {
        kq[len++] = (char)('0' + tam % 10);   // lay chu so cuoi, doi thanh ky tu
        tam /= 10;
    }
    if (am) kq[len++] = '-';
    kq[len] = '\0';

    // dao lai vi ta lay tu chu so thap
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char t = kq[i]; kq[i] = kq[j]; kq[j] = t;
    }
}

int main(void) {
    long long ds[] = {0, 7, 42, -123, 9123456789012345LL, -1};
    char s[32], chuan[32];

    for (int i = 0; i < 6; i++) {
        soThanhChuoi(ds[i], s);
        printf("%lld -> \"%s\"\n", ds[i], s);
    }

    // Kiem chung voi snprintf
    soThanhChuoi(-12345, s);
    snprintf(chuan, sizeof(chuan), "%d", -12345);
    printf("\nKiem chung: %s\n", strcmp(s, chuan) == 0 ? "DUNG" : "SAI");
    return 0;
}
```

**3 điểm cần chú ý:**
1. **Trường hợp `n = 0`** — vòng `while` không chạy, phải xử lý riêng
2. **Số âm** — tách dấu ra, xử lý phần trị tuyệt đối
3. **Đảo xâu** — vì ta lấy chữ số từ hàng đơn vị lên

⚠️ **Dùng `unsigned long long` cho `tam`:** giá trị `LLONG_MIN` (−9223372036854775808) không có số dương tương ứng trong `long long`, nên `-n` sẽ tràn.

### Bài 5.

```c
#include <stdio.h>
#include <ctype.h>

long long chuoiThanhSo(const char *s) {
    int i = 0;

    // Bo qua khoang trang dau
    while (isspace((unsigned char)s[i])) i++;

    // Xu ly dau
    int am = 0;
    if (s[i] == '+' || s[i] == '-') {
        am = (s[i] == '-');
        i++;
    }

    // Doc cac chu so
    long long kq = 0;
    while (isdigit((unsigned char)s[i])) {
        kq = kq * 10 + (s[i] - '0');      // CONG THUC VANG
        i++;
    }

    return am ? -kq : kq;
}

int main(void) {
    const char *ds[] = {"42", "-123", "  +7  ", "0", "123abc", "abc"};

    for (int i = 0; i < 6; i++) {
        printf("\"%s\" -> %lld\n", ds[i], chuoiThanhSo(ds[i]));
    }

    printf("\nKiem chung: %s\n", chuoiThanhSo("-12345") == -12345 ? "DUNG" : "SAI");
    return 0;
}
```

**Công thức cốt lõi:** `kq = kq * 10 + (s[i] - '0')`

Quá trình với `"423"`:

```
kq = 0
'4': kq = 0*10 + 4 = 4
'2': kq = 4*10 + 2 = 42
'3': kq = 42*10 + 3 = 423  ✔
```

💡 `s[i] - '0'` đổi ký tự số thành giá trị số — nhờ các chữ số nằm liên tiếp trong bảng ASCII (xem bài [03-04](../03-04-c-bang-ma-ascii-va-thu-vien-ctypeh.md)).

💡 Vì xâu C kết thúc bằng `'\0'` (không phải chữ số, không phải khoảng trắng), các vòng `while` tự dừng ở cuối xâu mà không cần so sánh với độ dài.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // strtol(chuoi, &end, coSo)
    printf("Nhi phan  \"1101\"   -> %ld\n", strtol("1101", NULL, 2));    // 13
    printf("Bat phan  \"777\"    -> %ld\n", strtol("777",  NULL, 8));    // 511
    printf("Thap luc  \"FF\"     -> %ld\n", strtol("FF",   NULL, 16));   // 255
    printf("Thap luc  \"1A2B\"   -> %ld\n", strtol("1A2B", NULL, 16));   // 6699

    // Co so 0 = tu dong nhan dien theo tien to
    printf("\n--- Tu dong nhan dien (co so 0) ---\n");
    printf("\"0x1F\" -> %ld\n", strtol("0x1F", NULL, 0));   // 31  (0x = he 16)
    printf("\"017\"  -> %ld\n", strtol("017",  NULL, 0));   // 15  (0  = he 8)
    printf("\"42\"   -> %ld\n", strtol("42",   NULL, 0));   // 42  (he 10)

    // Co so bat ky tu 2 den 36
    printf("\nCo so 36 \"ZZ\"    -> %ld\n", strtol("ZZ", NULL, 36));   // 1295
    return 0;
}
```

**Cơ số hỗ trợ: 2 đến 36** (dùng 0–9 rồi A–Z làm chữ số, không phân biệt hoa thường).

**Tiền tố khi dùng cơ số 0:**

| Tiền tố | Cơ số |
|---|---|
| `0x` hoặc `0X` | 16 |
| `0` (rồi chữ số) | 8 |
| Không có | 10 |

💡 Truyền `NULL` cho tham số `end` khi không cần biết vị trí dừng.

### Bài 7.

```c
#include <stdio.h>

// Tu viet - ho tro co so bat ky, ghi ket qua vao kq (it nhat 66 ky tu)
void doiCoSo(long long n, int coSo, char *kq) {
    const char KY_TU[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (coSo < 2 || coSo > 36) { kq[0] = '\0'; return; }
    if (n == 0) { kq[0] = '0'; kq[1] = '\0'; return; }

    int am = (n < 0);
    unsigned long long tam = am ? -(unsigned long long)n : (unsigned long long)n;

    int len = 0;
    while (tam > 0) {
        kq[len++] = KY_TU[tam % coSo];
        tam /= coSo;
    }
    if (am) kq[len++] = '-';
    kq[len] = '\0';
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char t = kq[i]; kq[i] = kq[j]; kq[j] = t;
    }
}

int main(void) {
    int n = 255;
    char s[70];

    printf("So %d trong cac he:\n", n);
    doiCoSo(n, 2, s);  printf("  He 2  : %s\n", s);    // 11111111
    doiCoSo(n, 8, s);  printf("  He 8  : %s\n", s);    // 377
    doiCoSo(n, 16, s); printf("  He 16 : %s\n", s);    // FF
    doiCoSo(n, 36, s); printf("  He 36 : %s\n", s);    // 73

    // Dung dac ta co san cua printf
    printf("\n--- Dung printf ---\n");
    printf("  He 8  (%%o)  : %o\n", n);
    printf("  He 16 (%%x)  : %x\n", n);
    printf("  He 16 (%%X)  : %X\n", n);
    printf("  Co tien to  : %#x  %#o\n", n, n);

    // Ghi vao chuoi
    char hex[20];
    snprintf(hex, sizeof(hex), "%X", n);
    printf("  He 16 (snprintf): %s\n", hex);
    return 0;
}
```

**Các đặc tả hệ đếm của `printf`:**

```c
printf("%d", n);     // he 10
printf("%o", n);     // he 8
printf("%x", n);     // he 16 (chu thuong)
printf("%X", n);     // he 16 (chu HOA)
printf("%#x", n);    // co tien to 0x
```

⚠️ `printf` **không có** đặc tả cho hệ 2 (nhị phân) trong chuẩn C11 — phải tự viết như hàm `doiCoSo`. `%o`, `%x`, `%X` dùng cho số **không dấu** (`unsigned int`); với số âm hãy tự xử lý dấu.

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    // ===== SO -> CHUOI =====
    int n = 42;
    double d = 3.14159;

    char s1[32], s2[32];
    snprintf(s1, sizeof(s1), "%d", n);
    snprintf(s2, sizeof(s2), "%.2f", d);      // co dinh dang

    printf("snprintf %%d   : %s\n", s1);
    printf("snprintf %%.2f : %s\n", s2);      // 3.14

    // ===== CHUOI -> SO =====
    const char *s = "123";

    int a = atoi(s);                          // Cach 1

    int b;
    if (sscanf(s, "%d", &b) != 1) b = 0;      // Cach 2

    char *end;
    long c = strtol(s, &end, 10);             // Cach 3

    printf("\natoi   : %d\n", a);
    printf("sscanf : %d\n", b);
    printf("strtol : %ld\n", c);

    // sscanf doc NHIEU gia tri cung luc
    const char *duLieu = "10 3.5 hello";
    int x; double y; char z[20];
    int soDoc = sscanf(duLieu, "%d %lf %19s", &x, &y, z);
    printf("\nDoc nhieu (%d gia tri): x=%d, y=%.1f, z=%s\n", soDoc, x, y, z);
    return 0;
}
```

**So sánh:**

| | `atoi`/`atof` | `strtol`/`strtod` | `sscanf` |
|---|---|---|---|
| Cú pháp | ✅ Ngắn gọn nhất | Trung bình | Trung bình |
| Tốc độ | ✅ Nhanh | ✅ Nhanh | Chậm hơn (phải phân tích định dạng) |
| Báo lỗi | ❌ Không | ✅ `end`, `errno` | ✅ Số giá trị đọc được |
| Biết vị trí dừng | ❌ | ✅ | Có (qua `%n`) |
| Đọc nhiều giá trị | ❌ | Được (gọi lặp với `end`) | ✅ Một lệnh |
| Chọn cơ số | ❌ | ✅ 2–36 | `%x`, `%o` |

✅ **Dùng `atoi`** khi chắc chắn dữ liệu đúng; **dùng `strtol`** khi cần kiểm tra lỗi; **dùng `sscanf`** khi cần đọc nhiều giá trị theo mẫu. Chiều ngược lại luôn dùng **`snprintf`**. Xem thêm bài [09-07](../09-07-c-tach-chuoi-voi-strtok-va-sscanf.md).

⚠️ Khi `sscanf` đọc chuỗi bằng `%s`, luôn giới hạn độ dài (`%19s` với mảng 20 phần tử) để tránh tràn mảng.

### Bài 9.

```c
#include <stdio.h>

void dinhDangSoThuc(double x, int soChuSo, char *kq, size_t size) {
    snprintf(kq, size, "%.*f", soChuSo, x);    // * lay do chinh xac tu tham so
}

int main(void) {
    double pi = 3.14159265358979;
    char s[50];

    for (int k = 0; k <= 8; k += 2) {
        dinhDangSoThuc(pi, k, s, sizeof(s));
        printf("k = %d -> \"%s\"\n", k, s);
    }

    // Mac dinh cua %f
    snprintf(s, sizeof(s), "%f", pi);
    printf("\n%%f mac dinh  = \"%s\"\n", s);

    // Dinh dang khoa hoc
    snprintf(s, sizeof(s), "%.3e", 123456.789);
    printf("Khoa hoc      = \"%s\"\n", s);
    return 0;
}
```

Output:

```
k = 0 -> "3"
k = 2 -> "3.14"
k = 4 -> "3.1416"
k = 6 -> "3.141593"
k = 8 -> "3.14159265"

%f mac dinh  = "3.141593"
Khoa hoc      = "1.235e+05"
```

💡 **Dấu `*` trong `"%.*f"`** nghĩa là độ chính xác được truyền vào như một tham số `int` đứng trước giá trị — rất tiện khi `k` chỉ biết lúc chạy.

### Bài 10.

```c
#include <stdio.h>
#include <string.h>

// Ghi so tien da dinh dang vao kq (kq can it nhat 32 ky tu)
void dinhDangTien(long long n, char phanCach, char *kq) {
    int am = (n < 0);
    unsigned long long tri = am ? -(unsigned long long)n : (unsigned long long)n;
    char s[32];
    snprintf(s, sizeof(s), "%llu", tri);

    int len = (int)strlen(s), k = 0, dem = 0;

    // Duyet TU PHAI SANG TRAI, cu 3 chu so chen mot dau phan cach
    for (int i = len - 1; i >= 0; i--) {
        kq[k++] = s[i];
        dem++;
        if (dem % 3 == 0 && i > 0) kq[k++] = phanCach;
    }
    if (am) kq[k++] = '-';
    kq[k] = '\0';

    for (int i = 0, j = k - 1; i < j; i++, j--) {        // dao lai
        char t = kq[i]; kq[i] = kq[j]; kq[j] = t;
    }
}

int main(void) {
    long long ds[] = {0, 7, 999, 1000, 1234567, 1000000000, -9876543};
    char s[40];

    for (int i = 0; i < 7; i++) {
        dinhDangTien(ds[i], '.', s);
        printf("%lld\t-> %s VND\n", ds[i], s);
    }

    dinhDangTien(1234567, ',', s);
    printf("\nKieu My (dau phay): %s\n", s);
    return 0;
}
```

Output:

```
0	-> 0 VND
7	-> 7 VND
999	-> 999 VND
1000	-> 1.000 VND
1234567	-> 1.234.567 VND
1000000000	-> 1.000.000.000 VND
-9876543	-> -9.876.543 VND
```

💡 **Duyệt từ phải sang trái** vì việc nhóm 3 chữ số bắt đầu từ hàng đơn vị. Cuối cùng đảo lại.

⚠️ `if (dem % 3 == 0 && i > 0)` — điều kiện `i > 0` tránh thêm dấu phân cách thừa ở đầu (`".123"`).

💡 C không có đối số mặc định, nên dấu phân cách `phanCach` phải truyền rõ mỗi lần gọi.

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Doc cac so trong dong vao mang a, tra ve so luong
int docCacSo(const char *dong, int a[], int toiDa) {
    int n = 0;
    const char *p = dong;
    char *end;
    while (n < toiDa) {
        long x = strtol(p, &end, 10);
        if (end == p) break;            // khong doc duoc so nao nua
        a[n++] = (int)x;
        p = end;                        // tiep tuc tu cho vua dung
    }
    return n;
}

int main(void) {
    char dong[1000];
    printf("Nhap cac so cach nhau boi dau cach: ");
    if (fgets(dong, sizeof(dong), stdin) == NULL) return 1;

    int ds[500];
    int n = docCacSo(dong, ds, 500);

    printf("Da doc %d so: ", n);
    for (int i = 0; i < n; i++) printf("%d ", ds[i]);
    printf("\n");

    if (n > 0) {
        long long tong = 0;
        int mx = ds[0], mn = ds[0];
        for (int i = 0; i < n; i++) {
            tong += ds[i];
            if (ds[i] > mx) mx = ds[i];
            if (ds[i] < mn) mn = ds[i];
        }

        printf("Tong      = %lld\n", tong);
        printf("Lon nhat  = %d\n", mx);
        printf("Nho nhat  = %d\n", mn);
        printf("Trung binh= %.2f\n", (double)tong / n);
    }
    return 0;
}
```

💡 Vòng lặp với `strtol` tự động dừng khi hết dữ liệu hoặc gặp ký tự không phải số (`end == p`) — `strtol` tự bỏ qua khoảng trắng (kể cả `'\n'`) trước mỗi số.

Muốn tách theo dấu phẩy, sau mỗi số bỏ qua dấu phẩy:

```c
while (n < toiDa) {
    long x = strtol(p, &end, 10);
    if (end == p) break;
    a[n++] = (int)x;
    p = end;
    if (*p == ',') p++;
}
```

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool laSoNguyen(const char *s) {
    int i = 0;
    if (s[0] == '+' || s[0] == '-') i = 1;
    if (s[i] == '\0') return false;          // rong, hoac chi co dau

    for (; s[i] != '\0'; i++)
        if (!isdigit((unsigned char)s[i])) return false;

    return true;
}

bool laSoThuc(const char *s) {
    int i = 0;
    if (s[0] == '+' || s[0] == '-') i = 1;

    bool coChuSo = false, coChamThapPhan = false;

    for (; s[i] != '\0'; i++) {
        if (isdigit((unsigned char)s[i])) {
            coChuSo = true;
        } else if (s[i] == '.') {
            if (coChamThapPhan) return false;   // co 2 dau cham -> sai
            coChamThapPhan = true;
        } else {
            return false;
        }
    }
    return coChuSo;                              // phai co it nhat 1 chu so
}

int main(void) {
    const char *ds[] = {"123", "-45", "+7", "3.14", "-0.5", ".5", "1.",
                        "12a", "", "-", "1.2.3", "  5"};
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("Chuoi          | Nguyen | Thuc\n");
    printf("---------------|--------|------\n");
    for (int i = 0; i < n; i++) {
        char nhan[20];
        snprintf(nhan, sizeof(nhan), "\"%s\"", ds[i]);
        printf("%-15s| %s | %s\n", nhan,
               laSoNguyen(ds[i]) ? "  CO  " : "  --  ",
               laSoThuc(ds[i])   ? " CO"    : " --");
    }
    return 0;
}
```

💡 `"%-15s"` in xâu **căn trái** trong ô rộng 15 ký tự — gọn hơn nhiều so với tự in dấu cách.

💡 **Cách đơn giản hơn dùng `strtod` + kiểm tra vị trí:**

```c
bool laSo(const char *s) {
    if (s[0] == '\0') return false;
    char *end;
    strtod(s, &end);
    return end != s && *end == '\0';     // phai doc HET chuoi
}
```

Cách này còn nhận được cả dạng khoa học (`"1e5"`), nhưng cũng chấp nhận khoảng trắng ở đầu (`"  5"`) và các xâu như `"inf"`, `"nan"`.

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char bieuThuc[100];
    printf("Nhap bieu thuc (vd: 12+34): ");
    if (fgets(bieuThuc, sizeof(bieuThuc), stdin) == NULL) return 1;
    bieuThuc[strcspn(bieuThuc, "\n")] = '\0';

    // Doc so thu nhat (strtod tu xu ly dau am o dau)
    char *p;
    double a = strtod(bieuThuc, &p);
    if (p == bieuThuc) {
        printf("Loi: bieu thuc khong hop le!\n");
        return 1;
    }

    while (*p == ' ') p++;                       // bo khoang trang
    char op = *p;
    if (strchr("+-*/%", op) == NULL || op == '\0') {
        printf("Khong tim thay toan tu!\n");
        return 1;
    }
    p++;

    char *het;
    double b = strtod(p, &het);
    if (het == p) {
        printf("Loi: bieu thuc khong hop le!\n");
        return 1;
    }

    printf("%g %c %g = ", a, op, b);
    switch (op) {
        case '+': printf("%g", a + b); break;
        case '-': printf("%g", a - b); break;
        case '*': printf("%g", a * b); break;
        case '/':
            if (b == 0) printf("Loi chia cho 0");
            else printf("%g", a / b);
            break;
        case '%':
            if ((int)b == 0) printf("Loi chia du cho 0");
            else printf("%d", (int)a % (int)b);
            break;
    }
    printf("\n");
    return 0;
}
```

Ví dụ:

```
Nhap bieu thuc (vd: 12+34): 12+34
12 + 34 = 46

Nhap bieu thuc: -5*3
-5 * 3 = -15
```

💡 Đọc số thứ nhất bằng `strtod` trước, rồi mới tìm toán tử ở chỗ `strtod` dừng lại — nhờ vậy **không nhầm dấu âm ở đầu** với toán tử trừ.

💡 Cách gọn hơn nữa với `sscanf`: `if (sscanf(bieuThuc, "%lf %c %lf", &a, &op, &b) == 3) ...`.

### Bài 14.

```c
#include <stdio.h>
#include <string.h>

static const char *CHU_SO[] = {"khong", "mot", "hai", "ba", "bon",
                               "nam", "sau", "bay", "tam", "chin"};

// Noi them tu vao kq, tu dong them dau cach
static void them(char *kq, const char *tu) {
    if (kq[0] != '\0') strcat(kq, " ");
    strcat(kq, tu);
}

// Doc mot nhom 3 chu so (0-999), noi vao kq
static void doc3ChuSo(int n, int laNhomDau, char *kq) {
    int tram = n / 100;
    int chuc = (n / 10) % 10;
    int donVi = n % 10;

    if (tram > 0) {
        them(kq, CHU_SO[tram]); them(kq, "tram");
    } else if (!laNhomDau && (chuc > 0 || donVi > 0)) {
        them(kq, "khong tram");
    }

    if (chuc > 1) {
        them(kq, CHU_SO[chuc]); them(kq, "muoi");
        if (donVi == 1)      them(kq, "mot");
        else if (donVi == 5) them(kq, "lam");
        else if (donVi > 0)  them(kq, CHU_SO[donVi]);
    } else if (chuc == 1) {
        them(kq, "muoi");
        if (donVi == 5)      them(kq, "lam");
        else if (donVi > 0)  them(kq, CHU_SO[donVi]);
    } else if (donVi > 0) {
        if (tram > 0 || !laNhomDau) them(kq, "le");
        them(kq, CHU_SO[donVi]);
    }
}

// kq can du lon (khoang 300 ky tu)
void docSo(long long n, char *kq) {
    kq[0] = '\0';
    if (n == 0) { strcpy(kq, "khong"); return; }
    if (n < 0) { strcpy(kq, "am"); n = -n; }

    const char *DON_VI[] = {"", "nghin", "trieu", "ty", "nghin ty", "trieu ty"};

    // Tach thanh cac nhom 3 chu so
    int nhom[7], soNhom = 0;
    while (n > 0) { nhom[soNhom++] = (int)(n % 1000); n /= 1000; }

    for (int i = soNhom - 1; i >= 0; i--) {
        if (nhom[i] == 0) continue;
        doc3ChuSo(nhom[i], i == soNhom - 1, kq);
        if (i > 0) them(kq, DON_VI[i]);
    }
}

int main(void) {
    long long ds[] = {0, 5, 10, 11, 15, 21, 25, 100, 101, 105, 123,
                      1000, 1234, 1000000, 123456789, -42};
    int n = sizeof(ds) / sizeof(ds[0]);
    char s[300];

    for (int i = 0; i < n; i++) {
        docSo(ds[i], s);
        printf("%lld\t-> %s\n", ds[i], s);
    }
    return 0;
}
```

Output:

```
0	-> khong
5	-> nam
10	-> muoi
11	-> muoi mot
15	-> muoi lam
21	-> hai muoi mot
25	-> hai muoi lam
100	-> mot tram
101	-> mot tram le mot
105	-> mot tram le nam
123	-> mot tram hai muoi ba
1000	-> mot nghin
1234	-> mot nghin hai tram ba muoi bon
1000000	-> mot trieu
123456789	-> mot tram hai muoi ba trieu bon tram nam muoi sau nghin bay tram tam muoi chin
-42	-> am bon muoi hai
```

💡 **Các quy tắc đặc biệt của tiếng Việt** làm bài này khó hơn tưởng tượng:
- `15` → "mười **lăm**" (không phải "mười năm")
- `21` → "hai mươi **mốt**" (bản trên dùng "một" cho đơn giản)
- `101` → "một trăm **lẻ** một"
- Các nhóm giữa cần "không trăm": `1.000.234` → "một triệu không trăm ba mươi tư"...

💡 Hàm phụ `them()` lo việc chèn dấu cách giữa các từ, nhờ vậy không phải cắt khoảng trắng thừa ở cuối như khi tự ghép xâu.

### Bài 15.

**File `chuyendoi.h`:**

```c
// FILE: chuyendoi.h
#ifndef CHUYENDOI_H
#define CHUYENDOI_H

#include <stdbool.h>
#include <stddef.h>

/** @brief Chuyen chuoi sang int an toan. Tra ve true neu thanh cong, ket qua ghi vao *kq. */
bool toInt(const char *s, int *kq);

/** @brief Chuyen chuoi sang long long an toan. */
bool toLongLong(const char *s, long long *kq);

/** @brief Chuyen chuoi sang double an toan. */
bool toDouble(const char *s, double *kq);

/** @brief Chuyen so thuc thanh chuoi voi so chu so thap phan chi dinh. */
void toStr(double x, int soChuSo, char *kq, size_t size);

/** @brief Kiem tra chuoi co phai so nguyen hop le (cho phep dau +/-). */
bool isInteger(const char *s);

/** @brief Kiem tra chuoi co phai so (nguyen hoac thuc) hop le. */
bool isNumber(const char *s);

/** @brief Dinh dang so thanh tien te co dau phan cach hang nghin. kq >= 32 ky tu. */
void formatMoney(long long n, char phanCach, char *kq);

/** @brief Doi so nguyen sang chuoi theo co so (2-36). kq >= 66 ky tu. */
void toBase(long long n, int coSo, char *kq);

/** @brief Doi chuoi theo co so ve so nguyen. Tra ve true neu thanh cong. */
bool fromBase(const char *s, int coSo, long long *kq);

/** @brief Tach mot dong thanh cac so nguyen, tra ve so luong. */
int parseInts(const char *dong, int a[], int toiDa);

#endif
```

**File `chuyendoi.c`:**

```c
// FILE: chuyendoi.c
#include "chuyendoi.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <errno.h>
#include <limits.h>

bool toLongLong(const char *s, long long *kq) {
    char *end;
    errno = 0;
    long long n = strtoll(s, &end, 10);
    if (end == s || *end != '\0' || errno == ERANGE) return false;
    *kq = n;
    return true;
}

bool toInt(const char *s, int *kq) {
    long long n;
    if (!toLongLong(s, &n) || n < INT_MIN || n > INT_MAX) return false;
    *kq = (int)n;
    return true;
}

bool toDouble(const char *s, double *kq) {
    char *end;
    errno = 0;
    double x = strtod(s, &end);
    if (end == s || *end != '\0' || errno == ERANGE) return false;
    *kq = x;
    return true;
}

void toStr(double x, int soChuSo, char *kq, size_t size) {
    snprintf(kq, size, "%.*f", soChuSo, x);
}

bool isInteger(const char *s) {
    int i = (s[0] == '+' || s[0] == '-') ? 1 : 0;
    if (s[i] == '\0') return false;
    for (; s[i] != '\0'; i++)
        if (!isdigit((unsigned char)s[i])) return false;
    return true;
}

bool isNumber(const char *s) {
    double x;
    return toDouble(s, &x);
}

static void daoXau(char *s) {
    size_t len = strlen(s);
    if (len < 2) return;
    for (size_t i = 0, j = len - 1; i < j; i++, j--) {
        char t = s[i]; s[i] = s[j]; s[j] = t;
    }
}

void formatMoney(long long n, char phanCach, char *kq) {
    int am = (n < 0);
    unsigned long long tri = am ? -(unsigned long long)n : (unsigned long long)n;
    char s[32];
    snprintf(s, sizeof(s), "%llu", tri);
    int k = 0, dem = 0;
    for (int i = (int)strlen(s) - 1; i >= 0; i--) {
        kq[k++] = s[i];
        if (++dem % 3 == 0 && i > 0) kq[k++] = phanCach;
    }
    if (am) kq[k++] = '-';
    kq[k] = '\0';
    daoXau(kq);
}

void toBase(long long n, int coSo, char *kq) {
    static const char KY_TU[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if (coSo < 2 || coSo > 36) { kq[0] = '\0'; return; }
    if (n == 0) { strcpy(kq, "0"); return; }

    int am = (n < 0);
    unsigned long long tam = am ? -(unsigned long long)n : (unsigned long long)n;
    int k = 0;
    while (tam > 0) { kq[k++] = KY_TU[tam % coSo]; tam /= coSo; }
    if (am) kq[k++] = '-';
    kq[k] = '\0';
    daoXau(kq);
}

bool fromBase(const char *s, int coSo, long long *kq) {
    char *end;
    errno = 0;
    long long n = strtoll(s, &end, coSo);
    if (end == s || *end != '\0' || errno == ERANGE) return false;
    *kq = n;
    return true;
}

int parseInts(const char *dong, int a[], int toiDa) {
    int n = 0;
    char *end;
    while (n < toiDa) {
        long x = strtol(dong, &end, 10);
        if (end == dong) break;
        a[n++] = (int)x;
        dong = end;
    }
    return n;
}
```

**File `main.c` — kiểm thử:**

```c
// FILE: main.c
#include <stdio.h>
#include "chuyendoi.h"

int main(void) {
    int n; double x; long long v;
    char s[70];

    printf("--- Chuyen doi an toan ---\n");
    if (toInt("42", &n)) printf("toInt(\"42\")      = %d\n", n);          // 42
    if (!toInt("abc", &n)) printf("toInt(\"abc\")     = that bai\n");
    if (!toInt("12abc", &n)) printf("toInt(\"12abc\")   = that bai (co rac)\n");
    if (toDouble("3.14", &x)) printf("toDouble(\"3.14\") = %g\n", x);    // 3.14

    printf("\n--- Kiem tra ---\n");
    printf("isInteger(\"-45\") = %d\n", isInteger("-45"));   // 1
    printf("isInteger(\"3.14\")= %d\n", isInteger("3.14"));  // 0
    printf("isNumber(\"3.14\") = %d\n", isNumber("3.14"));   // 1
    printf("isNumber(\"1e5\")  = %d\n", isNumber("1e5"));    // 1

    printf("\n--- Dinh dang ---\n");
    toStr(3.14159, 3, s, sizeof(s));
    printf("toStr(3.14159, 3) = %s\n", s);                  // 3.142
    formatMoney(1234567, '.', s);
    printf("formatMoney       = %s VND\n", s);

    printf("\n--- He co so ---\n");
    toBase(255, 2, s);  printf("toBase(255, 2)  = %s\n", s);   // 11111111
    toBase(255, 16, s); printf("toBase(255, 16) = %s\n", s);   // FF
    if (fromBase("FF", 16, &v)) printf("fromBase(\"FF\", 16) = %lld\n", v);  // 255

    printf("\n--- Doc nhieu so ---\n");
    int a[10];
    int k = parseInts("10 20 30 40 50", a, 10);
    printf("parseInts: ");
    for (int i = 0; i < k; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall main.c chuyendoi.c -o chuyendoi
./chuyendoi
```

💡 **Điểm thiết kế quan trọng:** C không có ngoại lệ, nên các hàm chuyển đổi **trả về `bool` báo thành công/thất bại** và ghi kết quả qua **con trỏ** (`int *kq`). Người gọi chỉ cần `if (toInt(s, &n)) ...` — rõ ràng và không bao giờ nhầm giá trị `0` thật với lỗi như khi dùng `atoi`.
