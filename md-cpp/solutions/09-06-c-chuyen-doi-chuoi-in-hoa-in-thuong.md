# Lời giải — [C]. Chuyển Đổi Chuỗi In Hoa, In Thường

[← Quay lại bài học](../09-06-c-chuyen-doi-chuoi-in-hoa-in-thuong.md)

> **Nhắc lại:** `'A'` = 65, `'a'` = 97 — khoảng cách luôn là **32**. `toupper`/`tolower` nằm trong `<ctype.h>`. Nhập cả dòng bằng `fgets` rồi xoá ký tự `'\n'` ở cuối bằng `s[strcspn(s, "\n")] = '\0';`.

---

### Bài 1.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    char s[256], hoa[256];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';            // xoa '\n' do fgets doc vao

    strcpy(hoa, s);
    for (int i = 0; hoa[i] != '\0'; i++) {
        hoa[i] = (char)toupper((unsigned char)hoa[i]);
    }

    printf("Goc  : %s\n", s);
    printf("Hoa  : %s\n", hoa);
    return 0;
}
```

⚠️ **Nhớ xoá `'\n'` sau `fgets`** — `fgets` giữ lại ký tự xuống dòng trong chuỗi (xem bài [09-02](../09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi.md)).

⚠️ Ép `(unsigned char)` trước khi truyền vào `toupper` — tránh undefined behavior với ký tự có mã âm.

### Bài 2.

```c
#include <stdio.h>
#include <ctype.h>

// Ghi ban in thuong cua src vao dst, KHONG sua src
void chuyenThuong(const char *src, char *dst) {
    while (*src != '\0') {
        *dst = (char)tolower((unsigned char)*src);
        src++;
        dst++;
    }
    *dst = '\0';                           // dat ky tu ket thuc
}

int main(void) {
    const char *s = "LAP TRINH C CO BAN";
    char thuong[100];

    chuyenThuong(s, thuong);

    printf("Goc    : %s\n", s);
    printf("Thuong : %s\n", thuong);
    return 0;
}
```

**Mẫu duyệt chuỗi bằng con trỏ:**

```c
while (*src != '\0') { ...; src++; dst++; }
*dst = '\0';
```

Ở đây `s` có thể là `const char *` trỏ tới chuỗi hằng vì hàm **chỉ đọc** nó; kết quả được ghi vào mảng `thuong` có thể sửa.

⚠️ Mảng đích phải **đủ chỗ** (ít nhất `strlen(src) + 1` byte, tính cả `'\0'`).

### Bài 3.

```c
#include <stdio.h>
#include <string.h>

void toUpperASCII(char *s) {
    for (; *s; s++)
        if (*s >= 'a' && *s <= 'z') *s -= 32;
}

void toLowerASCII(char *s) {
    for (; *s; s++)
        if (*s >= 'A' && *s <= 'Z') *s += 32;
}

// Cach dung phep BIT - nhanh hon
void toUpperBit(char *s) {
    for (; *s; s++)
        if (*s >= 'a' && *s <= 'z') *s &= ~32;      // TAT bit thu 6
}

void toLowerBit(char *s) {
    for (; *s; s++)
        if (*s >= 'A' && *s <= 'Z') *s |= 32;       // BAT bit thu 6
}

int main(void) {
    const char *s = "Lap Trinh C 2026!";
    char t[100];

    printf("Goc         : %s\n", s);
    strcpy(t, s); toUpperASCII(t); printf("Hoa (+-32)  : %s\n", t);
    strcpy(t, s); toLowerASCII(t); printf("Thuong(+-32): %s\n", t);
    strcpy(t, s); toUpperBit(t);   printf("Hoa (bit)   : %s\n", t);
    strcpy(t, s); toLowerBit(t);   printf("Thuong(bit) : %s\n", t);
    return 0;
}
```

Output:

```
Goc         : Lap Trinh C 2026!
Hoa (+-32)  : LAP TRINH C 2026!
Thuong(+-32): lap trinh c 2026!
Hoa (bit)   : LAP TRINH C 2026!
Thuong(bit) : lap trinh c 2026!
```

**Cơ sở của phép bit:**

```
'A' = 65 = 0100 0001
'a' = 97 = 0110 0001
             ^
      chi khac bit thu 6 (gia tri 32)
```

⚠️ **BẮT BUỘC kiểm tra `if (c >= 'a' && c <= 'z')` trước.** Nếu áp dụng mù quáng lên chữ số hoặc ký tự đặc biệt sẽ ra rác:

```c
'5' - 32 = 53 - 32 = 21        // ky tu dieu khien NAK, khong in duoc
'!' + 32 = 33 + 32 = 65 = 'A'  // dau ! bien thanh chu A!
```

### Bài 4.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void daoHoaThuong(char *s) {
    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (islower(c))      *s = (char)toupper(c);
        else if (isupper(c)) *s = (char)tolower(c);
    }
}

// Cach dung phep XOR - rat gon
void daoHoaThuongXOR(char *s) {
    for (; *s; s++)
        if (isalpha((unsigned char)*s)) *s ^= 32;   // XOR dao bit thu 6
}

int main(void) {
    const char *s = "Lap Trinh C 2026!";
    char a[100], b[100];

    strcpy(a, s); daoHoaThuong(a);
    strcpy(b, s); daoHoaThuongXOR(b);

    printf("Goc     : %s\n", s);
    printf("Dao     : %s\n", a);
    printf("Dao(XOR): %s\n", b);

    // Dao 2 lan -> ve nhu cu
    daoHoaThuong(a);
    printf("Dao 2 lan: %s\n", a);
    return 0;
}
```

Output:

```
Goc     : Lap Trinh C 2026!
Dao     : lAP tRINH c 2026!
Dao(XOR): lAP tRINH c 2026!
Dao 2 lan: Lap Trinh C 2026!
```

💡 **Phép `c ^= 32`** đảo bit thứ 6 — biến hoa thành thường và ngược lại chỉ bằng **một phép toán**.

### Bài 5.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

void titleCase(char *s) {
    bool dauTu = true;                    // dang o dau mot tu

    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (isspace(c)) {
            dauTu = true;
        } else {
            *s = (char)(dauTu ? toupper(c) : tolower(c));
            dauTu = false;
        }
    }
}

int main(void) {
    const char *ds[] = {
        "lap trinh c co ban",
        "NGUYEN VAN AN",
        "hoc   lap   trinh",
        "  co khoang trang dau  "
    };
    int n = sizeof(ds) / sizeof(ds[0]);
    char t[100];

    for (int i = 0; i < n; i++) {
        strcpy(t, ds[i]);
        titleCase(t);
        printf("\"%s\"\n", ds[i]);
        printf("  -> \"%s\"\n", t);
    }
    return 0;
}
```

Output:

```
"lap trinh c co ban"
  -> "Lap Trinh C Co Ban"
"NGUYEN VAN AN"
  -> "Nguyen Van An"
"hoc   lap   trinh"
  -> "Hoc   Lap   Trinh"
"  co khoang trang dau  "
  -> "  Co Khoang Trang Dau  "
```

💡 **Biến cờ `dauTu`** là kỹ thuật chuẩn: bật khi gặp khoảng trắng, tắt ngay sau khi xử lý một ký tự.

💡 Mảng `ds` chứa các **chuỗi hằng** nên phải chép sang mảng `t` rồi mới sửa.

### Bài 6.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

void sentenceCase(char *s) {
    bool dauCau = true;

    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (dauCau && isalpha(c)) {
            *s = (char)toupper(c);
            dauCau = false;
        } else {
            *s = (char)tolower(c);
        }

        // Sau dau . ! ? la bat dau cau moi
        if (*s == '.' || *s == '!' || *s == '?') dauCau = true;
    }
}

int main(void) {
    char s[] = "day LA cau THU NHAT. day la CAU thu hai! con DAY la cau ba?  het.";

    printf("Goc : %s\n", s);
    sentenceCase(s);
    printf("Sau : %s\n", s);
    return 0;
}
```

Output:

```
Goc : day LA cau THU NHAT. day la CAU thu hai! con DAY la cau ba?  het.
Sau : Day la cau thu nhat. Day la cau thu hai! Con day la cau ba?  Het.
```

### Bài 7.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

// Ghi ket qua vao dst. pascal = true -> PascalCase, false -> camelCase
void toCase(const char *src, char *dst, bool pascal) {
    bool dauTu = true;       // ky tu tiep theo la chu dau cua mot tu
    bool tuDauTien = true;   // chua gap tu nao
    int k = 0;

    for (int i = 0; src[i] != '\0'; i++) {
        unsigned char c = (unsigned char)src[i];
        if (isspace(c)) {                     // bo dau cach, danh dau tu moi
            dauTu = true;
            continue;
        }
        if (dauTu && (pascal || !tuDauTien))
            dst[k++] = (char)toupper(c);      // chu dau cac tu sau: viet hoa
        else
            dst[k++] = (char)tolower(c);
        dauTu = false;
        tuDauTien = false;
    }
    dst[k] = '\0';
}

int main(void) {
    const char *ds[] = {"lap trinh c co ban", "HELLO WORLD", "tinh tong hai so"};
    char kq[100];

    for (int i = 0; i < 3; i++) {
        printf("\"%s\"\n", ds[i]);
        toCase(ds[i], kq, false);
        printf("  camelCase : %s\n", kq);
        toCase(ds[i], kq, true);
        printf("  PascalCase: %s\n", kq);
    }
    return 0;
}
```

Output:

```
"lap trinh c co ban"
  camelCase : lapTrinhCCoBan
  PascalCase: LapTrinhCCoBan
"HELLO WORLD"
  camelCase : helloWorld
  PascalCase: HelloWorld
"tinh tong hai so"
  camelCase : tinhTongHaiSo
  PascalCase: TinhTongHaiSo
```

💡 **Quy ước đặt tên trong lập trình:**

| Kiểu | Ví dụ | Thường dùng cho |
|---|---|---|
| `camelCase` | `soHocSinh` | Biến, hàm (Java, JavaScript) |
| `PascalCase` | `SinhVien` | Tên kiểu dữ liệu, struct |
| `snake_case` | `so_hoc_sinh` | Biến, hàm (Python, thư viện chuẩn C) |
| `SCREAMING_SNAKE` | `MAX_SIZE` | Hằng số, macro `#define` |
| `kebab-case` | `lap-trinh-c` | URL, tên file, CSS |

### Bài 8.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

// Noi cac tu bang ky tu noi (sep), tat ca viet thuong
void toSepCase(const char *src, char *dst, char sep) {
    int k = 0;
    bool dangTrongTu = false;

    for (int i = 0; src[i] != '\0'; i++) {
        unsigned char c = (unsigned char)src[i];
        if (isspace(c)) {
            dangTrongTu = false;
            continue;
        }
        if (!dangTrongTu && k > 0) dst[k++] = sep;   // bat dau tu moi
        dst[k++] = (char)tolower(c);
        dangTrongTu = true;
    }
    dst[k] = '\0';
}

// Chuyen camelCase -> snake_case
void camelToSnake(const char *src, char *dst) {
    int k = 0;
    for (int i = 0; src[i] != '\0'; i++) {
        unsigned char c = (unsigned char)src[i];
        if (isupper(c)) {
            if (i > 0) dst[k++] = '_';
            dst[k++] = (char)tolower(c);
        } else {
            dst[k++] = src[i];
        }
    }
    dst[k] = '\0';
}

int main(void) {
    const char *s = "Lap Trinh C Co Ban";
    char kq[100];

    printf("Goc         : %s\n", s);
    toSepCase(s, kq, '_');
    printf("snake_case  : %s\n", kq);
    toSepCase(s, kq, '-');
    printf("kebab-case  : %s\n", kq);

    printf("\ncamelToSnake:\n");
    const char *ds[] = {"soHocSinh", "tinhTongHaiSo", "maxValue"};
    for (int i = 0; i < 3; i++) {
        camelToSnake(ds[i], kq);
        printf("  %s -> %s\n", ds[i], kq);
    }
    return 0;
}
```

Output:

```
Goc         : Lap Trinh C Co Ban
snake_case  : lap_trinh_c_co_ban
kebab-case  : lap-trinh-c-co-ban

camelToSnake:
  soHocSinh -> so_hoc_sinh
  tinhTongHaiSo -> tinh_tong_hai_so
  maxValue -> max_value
```

### Bài 9.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    char s[256];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    int hoa = 0, thuong = 0, so = 0, khac = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if      (isupper(c)) hoa++;
        else if (islower(c)) thuong++;
        else if (isdigit(c)) so++;
        else                 khac++;
    }

    printf("Chu hoa   : %d\n", hoa);
    printf("Chu thuong: %d\n", thuong);
    printf("Chu so    : %d\n", so);
    printf("Khac      : %d\n", khac);
    printf("Tong      : %zu\n", strlen(s));

    if (hoa + thuong > 0) {
        printf("\nTy le chu hoa: %.2f%%\n", 100.0 * hoa / (hoa + thuong));
    }
    return 0;
}
```

💡 Muốn in ký tự `%` bằng `printf` phải viết `%%`. `strlen` trả về `size_t` nên in bằng `%zu`.

### Bài 10.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

bool toanHoa(const char *s) {
    bool coChuCai = false;
    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (isalpha(c)) {
            coChuCai = true;
            if (!isupper(c)) return false;
        }
    }
    return coChuCai;            // chuoi khong co chu cai -> false
}

bool toanThuong(const char *s) {
    bool coChuCai = false;
    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (isalpha(c)) {
            coChuCai = true;
            if (!islower(c)) return false;
        }
    }
    return coChuCai;
}

int main(void) {
    const char *ds[] = {"HELLO", "hello", "Hello", "HELLO 123!", "12345", ""};
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("Chuoi         | Toan hoa | Toan thuong\n");
    printf("--------------|----------|------------\n");
    for (int i = 0; i < n; i++) {
        char nhan[20];
        snprintf(nhan, sizeof nhan, "\"%s\"", ds[i]);
        printf("%-14s| %-8s | %s\n", nhan,
               toanHoa(ds[i]) ? "true" : "false",
               toanThuong(ds[i]) ? "true" : "false");
    }
    return 0;
}
```

Output:

```
Chuoi         | Toan hoa | Toan thuong
--------------|----------|------------
"HELLO"       | true     | false
"hello"       | false    | true
"Hello"       | false    | false
"HELLO 123!"  | true     | false
"12345"       | false    | false
""            | false    | false
```

⚠️ **Xử lý trường hợp đặc biệt:** chuỗi `"12345"` hoặc `""` không có chữ cái nào — nên trả về `false` (biến cờ `coChuCai` lo việc này).

💡 `bool`, `true`, `false` trong C cần `#include <stdbool.h>`. `printf` không có định dạng riêng cho `bool`, nên in bằng biểu thức `? "true" : "false"`.

### Bài 11.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void) {
    char s[256], a[256], b[256];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    // Vi tri CHAN -> hoa, vi tri LE -> thuong
    strcpy(a, s);
    for (size_t i = 0; a[i] != '\0'; i++) {
        unsigned char c = (unsigned char)a[i];
        a[i] = (char)((i % 2 == 0) ? toupper(c) : tolower(c));
    }

    printf("Goc      : %s\n", s);
    printf("Xen ke   : %s\n", a);

    // Chi tinh vi tri CUA CHU CAI (bo qua khoang trang)
    strcpy(b, s);
    int dem = 0;
    for (char *p = b; *p; p++) {
        unsigned char c = (unsigned char)*p;
        if (isalpha(c)) {
            *p = (char)((dem % 2 == 0) ? toupper(c) : tolower(c));
            dem++;
        }
    }
    printf("Xen ke 2 : %s\n", b);
    return 0;
}
```

Với input `lap trinh c`:

```
Goc      : lap trinh c
Xen ke   : LaP TrInH C
Xen ke 2 : LaP tRiNh C
```

### Bài 12.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char c = 'a';

    printf("--- SAI: in bang %%d ---\n");
    printf("toupper('a') = %d\n", toupper(c));            // 65 (so!)

    printf("\n--- DUNG: in bang %%c ---\n");
    printf("toupper('a') = %c\n", toupper(c));            // A

    printf("\nKieu tra ve cua toupper: int\n");
    printf("sizeof(toupper('a')) = %zu byte\n", sizeof(toupper(c)));  // 4
    printf("sizeof(char)         = %zu byte\n", sizeof(char));        // 1

    // Gan vao phan tu mang char: gia tri int duoc chuyen ve char
    char s[] = "abc";
    s[0] = (char)toupper((unsigned char)s[0]);
    printf("\nGan vao mang char thi OK: %s\n", s);
    return 0;
}
```

**Vì sao `toupper` trả về `int`:**

1. **Thiết kế của thư viện C:** tất cả hàm trong `<ctype.h>` đều nhận và trả `int`.

2. **Cần biểu diễn `EOF`:** các hàm này phải nhận được cả giá trị `EOF` (thường là −1, ví dụ kết quả của `getchar()`) bên cạnh mọi giá trị `unsigned char` hợp lệ. Nếu dùng `char`, không còn chỗ cho `EOF`.

3. **Tránh vấn đề `char` có dấu:** trên một số hệ thống `char` là có dấu (−128..127), dùng `int` tránh được nhập nhằng.

**Hệ quả thực tế:**

```c
printf("%d", toupper('a'));   // in ra 65 (SAI y muon)
printf("%c", toupper('a'));   // in ra A  (DUNG)

char c = toupper('a');        // OK - phep gan tu dong chuyen ve char
s[i] = toupper(s[i]);         // OK
```

⚠️ **Chỉ có vấn đề khi in ra** — `printf` in theo **đặc tả định dạng** bạn chọn: `%d` in con số, `%c` in ký tự. Hãy nhớ chọn đúng `%c`.

### Bài 13.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

int main(void) {
    const char *s = "Xin Chao! Toi 20 tuoi, email: an@gmail.com #2026";
    char hoa[100], thuong[100];

    strcpy(hoa, s);
    strcpy(thuong, s);
    for (char *p = hoa; *p; p++)    *p = (char)toupper((unsigned char)*p);
    for (char *p = thuong; *p; p++) *p = (char)tolower((unsigned char)*p);

    printf("Goc    : %s\n", s);
    printf("Hoa    : %s\n", hoa);
    printf("Thuong : %s\n", thuong);

    // Kiem tra: chu so va ky tu dac biet KHONG bi doi
    bool nguyenVen = true;
    for (size_t i = 0; s[i] != '\0'; i++) {
        if (!isalpha((unsigned char)s[i])) {
            if (hoa[i] != s[i] || thuong[i] != s[i]) {
                nguyenVen = false;
                printf("LOI tai vi tri %zu: '%c'\n", i, s[i]);
            }
        }
    }
    printf("\nKy tu khong phai chu cai giu nguyen: %s\n",
           nguyenVen ? "true" : "false");
    return 0;
}
```

Output:

```
Goc    : Xin Chao! Toi 20 tuoi, email: an@gmail.com #2026
Hoa    : XIN CHAO! TOI 20 TUOI, EMAIL: AN@GMAIL.COM #2026
Thuong : xin chao! toi 20 tuoi, email: an@gmail.com #2026

Ky tu khong phai chu cai giu nguyen: true
```

✅ **`toupper`/`tolower` an toàn với mọi ký tự** — nếu tham số không phải chữ cái, hàm trả về nguyên giá trị đó. Đây là ưu điểm lớn so với phép `±32` thủ công.

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

#define N 5000000

int main(void) {
    char *goc = malloc(N + 1);
    char *a = malloc(N + 1), *b = malloc(N + 1), *c = malloc(N + 1);
    if (!goc || !a || !b || !c) { printf("Khong du bo nho!\n"); return 1; }

    memset(goc, 'a', N);
    goc[N] = '\0';

    // (1) Vong lap chi so + toupper
    strcpy(a, goc);
    clock_t t1 = clock();
    for (size_t i = 0; a[i] != '\0'; i++) a[i] = (char)toupper((unsigned char)a[i]);
    clock_t t2 = clock();
    printf("(1) Chi so + toupper  : %.0f ms\n", 1000.0 * (t2 - t1) / CLOCKS_PER_SEC);

    // (2) Con tro + toupper
    strcpy(b, goc);
    t1 = clock();
    for (char *p = b; *p; p++) *p = (char)toupper((unsigned char)*p);
    t2 = clock();
    printf("(2) Con tro + toupper : %.0f ms\n", 1000.0 * (t2 - t1) / CLOCKS_PER_SEC);

    // (3) Phep bit
    strcpy(c, goc);
    t1 = clock();
    for (char *p = c; *p; p++) if (*p >= 'a' && *p <= 'z') *p &= ~32;
    t2 = clock();
    printf("(3) Phep bit (& ~32)  : %.0f ms\n", 1000.0 * (t2 - t1) / CLOCKS_PER_SEC);

    printf("\nKiem tra ket qua giong nhau: %s\n",
           (strcmp(a, b) == 0 && strcmp(b, c) == 0) ? "true" : "false");

    free(goc); free(a); free(b); free(c);
    return 0;
}
```

Kết quả tham khảo (biên dịch `-O2`, con số thay đổi theo máy):

```
(1) Chi so + toupper  : 18 ms
(2) Con tro + toupper : 18 ms
(3) Phep bit (& ~32)  : 4 ms

Kiem tra ket qua giong nhau: true
```

**Nhận xét:**

| Cách | Tốc độ | An toàn | Dễ đọc |
|---|---|---|---|
| Chỉ số + `toupper` | Trung bình | ✅ Cao | ✅ Cao |
| Con trỏ + `toupper` | Trung bình | ✅ Cao | Trung bình |
| Phép bit | ✅ **Nhanh nhất** | ⚠️ Chỉ đúng với ASCII | ⚠️ Thấp |

💡 Mảng 5 triệu ký tự quá lớn để đặt trên stack, nên cấp phát bằng `malloc` và nhớ `free`. Hàm `clock()` trong `<time.h>` đo thời gian CPU.

**Vì sao `toupper` chậm hơn:** nó phải tra bảng theo locale hiện tại, nên có thêm lần gọi hàm và truy cập bộ nhớ.

✅ **Khuyến nghị:** dùng `toupper`/`tolower` — chênh lệch vài ms trên 5 triệu ký tự hầu như không bao giờ quan trọng, mà tính đúng đắn và dễ đọc thì luôn quan trọng.

### Bài 15.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Chuan hoa ten tu src, ghi ket qua vao dst
void chuanHoaTen(const char *src, char *dst) {
    int k = 0;
    int i = 0;

    while (src[i] != '\0') {
        // (1) Bo qua moi khoang trang thua
        while (src[i] != '\0' && isspace((unsigned char)src[i])) i++;
        if (src[i] == '\0') break;

        // (4) Noi cac tu bang MOT dau cach
        if (k > 0) dst[k++] = ' ';

        // (3) Viet hoa chu cai dau
        dst[k++] = (char)toupper((unsigned char)src[i++]);

        // (2) Cac chu con lai cua tu ve chu thuong
        while (src[i] != '\0' && !isspace((unsigned char)src[i]))
            dst[k++] = (char)tolower((unsigned char)src[i++]);
    }
    dst[k] = '\0';
}

int main(void) {
    const char *ds[] = {
        "  nGuYen   vAN   an  ",
        "TRAN THI BINH",
        "le hoang    CUONG",
        "   ",
        "a"
    };
    int n = sizeof(ds) / sizeof(ds[0]);
    char kq[100], o1[128], o2[128];

    printf("+--------------------------+--------------------------+\n");
    printf("| GOC                      | CHUAN HOA                |\n");
    printf("+--------------------------+--------------------------+\n");
    for (int i = 0; i < n; i++) {
        chuanHoaTen(ds[i], kq);
        snprintf(o1, sizeof o1, "[%s]", ds[i]);
        snprintf(o2, sizeof o2, "[%s]", kq);
        printf("| %-24s | %-24s |\n", o1, o2);
    }
    printf("+--------------------------+--------------------------+\n");
    return 0;
}
```

Output:

```
+--------------------------+--------------------------+
| GOC                      | CHUAN HOA                |
+--------------------------+--------------------------+
| [  nGuYen   vAN   an  ]  | [Nguyen Van An]          |
| [TRAN THI BINH]          | [Tran Thi Binh]          |
| [le hoang    CUONG]      | [Le Hoang Cuong]         |
| [   ]                    | []                       |
| [a]                      | [A]                      |
+--------------------------+--------------------------+
```

**4 việc hàm này làm cùng lúc:**
1. **Xoá khoảng trắng thừa** ở đầu, cuối và giữa các từ
2. **Chuẩn hoá** mỗi từ về chữ thường
3. **Viết hoa** chữ cái đầu mỗi từ
4. **Nối lại** bằng đúng một dấu cách

💡 **Mẹo:** `%-24s` trong `printf` in chuỗi căn trái trong ô rộng 24 ký tự — cách kẻ bảng gọn nhất trong C. Ghép `[`, `]` vào chuỗi trước bằng `snprintf` để cả cụm được căn lề.

💡 Có thể tách từ bằng `strtok` thay cho vòng lặp tự viết — xem bài [09-07 — Tách chuỗi với strtok và sscanf](../09-07-c-tach-chuoi-voi-strtok-va-sscanf.md).

Xem thêm bài [09-09 — Chuẩn hoá tên và email](../09-09-c-chuan-hoa-ten-va-email.md).
