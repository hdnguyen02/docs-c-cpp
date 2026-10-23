# Lời giải — [C]. So Sánh Chuỗi Theo Thứ Tự Từ Điển

[← Quay lại bài học](../09-05-c-so-sanh-chuoi-theo-thu-tu-tu-dien.md)

> **Quy tắc so sánh từ điển (lexicographical):** so sánh **từng ký tự từ trái sang phải** theo **mã ASCII**. Gặp cặp khác nhau đầu tiên thì kết luận ngay. Nếu một chuỗi là tiền tố của chuỗi kia, chuỗi **ngắn hơn** nhỏ hơn. Trong C luôn dùng `strcmp`/`strncmp` — **không** dùng `==`, `<`, `>` với xâu.

---

### Bài 1.

```c
#include <stdio.h>
#include <string.h>

void docDong(char *s, int size) {
    if (fgets(s, size, stdin) == NULL) s[0] = '\0';
    s[strcspn(s, "\n")] = '\0';
}

int main(void) {
    char a[100], b[100];
    printf("Nhap chuoi 1: "); docDong(a, sizeof(a));
    printf("Nhap chuoi 2: "); docDong(b, sizeof(b));

    int kq = strcmp(a, b);

    printf("\nstrcmp(a, b)      = %d\n", kq);
    printf("a == b  (kq == 0) : %d\n", kq == 0);
    printf("a != b  (kq != 0) : %d\n", kq != 0);
    printf("a <  b  (kq <  0) : %d\n", kq < 0);
    printf("a >  b  (kq >  0) : %d\n", kq > 0);
    printf("a <= b  (kq <= 0) : %d\n", kq <= 0);

    printf("\nKet luan: ");
    if      (kq < 0) printf("\"%s\" dung TRUOC \"%s\"\n", a, b);
    else if (kq > 0) printf("\"%s\" dung SAU \"%s\"\n", a, b);
    else             printf("Hai chuoi GIONG NHAU\n");
    return 0;
}
```

💡 **Mẹo nhớ:** thay toán tử `op` giữa hai xâu bằng `strcmp(a, b) op 0`. Ví dụ `a < b` ⇔ `strcmp(a, b) < 0`, `a >= b` ⇔ `strcmp(a, b) >= 0`.

### Bài 2.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *a = "Apple", *b = "apple";

    printf("strcmp(\"Apple\", \"apple\") < 0 : %d\n", strcmp(a, b) < 0);   // 1

    printf("\n--- Phan tich tung ky tu ---\n");
    for (int i = 0; a[i] != '\0' && b[i] != '\0'; i++) {
        printf("Vi tri %d: '%c' (%d) vs '%c' (%d)", i, a[i], a[i], b[i], b[i]);
        if (a[i] != b[i]) { printf("  <-- KHAC NHAU, ket luan ngay!\n"); break; }
        printf("  (bang nhau, xet tiep)\n");
    }

    printf("\n--- Cac moc ASCII ---\n");
    printf("'A' = %d, 'Z' = %d\n", 'A', 'Z');   // 65, 90
    printf("'a' = %d, 'z' = %d\n", 'a', 'z');   // 97, 122
    printf("'0' = %d, '9' = %d\n", '0', '9');   // 48, 57
    return 0;
}
```

Output:

```
strcmp("Apple", "apple") < 0 : 1

--- Phan tich tung ky tu ---
Vi tri 0: 'A' (65) vs 'a' (97)  <-- KHAC NHAU, ket luan ngay!

--- Cac moc ASCII ---
'A' = 65, 'Z' = 90
'a' = 97, 'z' = 122
'0' = 48, '9' = 57
```

**Giải thích:** ngay ký tự đầu tiên đã khác. `'A'` = 65 < `'a'` = 97, nên `strcmp("Apple", "apple") < 0`.

⚠️ **Hệ quả quan trọng: TOÀN BỘ chữ hoa đứng trước TOÀN BỘ chữ thường.**

```
'Z' (90) < 'a' (97)
```

Nên `strcmp("Zebra", "apple") < 0` — điều này thường **không phải** ý người dùng muốn khi sắp xếp tên!

Thứ tự ASCII đầy đủ: `' '` (32) < chữ số (48–57) < chữ hoa (65–90) < `'_'` (95) < chữ thường (97–122)

### Bài 3.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Tra ve: <0 neu a < b, 0 neu bang, >0 neu a > b
int soSanhKhongPhanBiet(const char *a, const char *b) {
    int i = 0;
    while (a[i] != '\0' && b[i] != '\0') {
        int ca = tolower((unsigned char)a[i]);
        int cb = tolower((unsigned char)b[i]);
        if (ca != cb) return ca - cb;
        i++;
    }
    // Moi ky tu chung deu bang nhau -> chuoi ngan hon thi nho hon
    return (unsigned char)a[i] - (unsigned char)b[i];
}

int main(void) {
    printf("\"Apple\" vs \"apple\" : %d (bang)\n", soSanhKhongPhanBiet("Apple", "apple"));
    printf("\"Apple\" vs \"Banana\": %d (am)\n", soSanhKhongPhanBiet("Apple", "Banana"));
    printf("\"Zebra\" vs \"apple\" : %d (duong)\n", soSanhKhongPhanBiet("Zebra", "apple"));

    printf("\nSo sanh binh thuong: \"Zebra\" < \"apple\" = %d\n",
           strcmp("Zebra", "apple") < 0);
    printf("Khong phan biet    : \"Zebra\" < \"apple\" = %d\n",
           soSanhKhongPhanBiet("Zebra", "apple") < 0);
    return 0;
}
```

Output:

```
"Apple" vs "apple" : 0 (bang)
"Apple" vs "Banana": -1 (am)
"Zebra" vs "apple" : 25 (duong)

So sanh binh thuong: "Zebra" < "apple" = 1
Khong phan biet    : "Zebra" < "apple" = 0
```

💡 **Đây mới là thứ tự người dùng mong đợi:** `apple` đứng trước `Zebra`.

💡 Dòng cuối `a[i] - b[i]` xử lý trường hợp một xâu là tiền tố: ký tự `'\0'` (0) luôn nhỏ hơn mọi ký tự khác, nên xâu ngắn hơn cho kết quả âm.

💡 Trên Linux/macOS có sẵn `strcasecmp()` trong `<strings.h>` (POSIX, không thuộc chuẩn C); Windows dùng `_stricmp()`. Tự viết như trên thì chạy được ở mọi nơi.

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N   100
#define MAX_DAI 51

// Ham so sanh cho qsort: moi phan tu la mot mang char[MAX_DAI]
int soSanhTang(const void *a, const void *b) {
    return strcmp((const char *)a, (const char *)b);
}

int soSanhGiam(const void *a, const void *b) {
    return strcmp((const char *)b, (const char *)a);   // dao thu tu
}

int main(void) {
    int n;
    char ds[MAX_N][MAX_DAI];

    printf("Nhap so chuoi: ");
    if (scanf("%d", &n) != 1 || n < 0) return 1;
    if (n > MAX_N) n = MAX_N;
    int c;
    while ((c = getchar()) != '\n' && c != EOF);     // xoa '\n' con sot

    for (int i = 0; i < n; i++) {
        printf("  Chuoi %d: ", i + 1);
        if (fgets(ds[i], MAX_DAI, stdin) == NULL) ds[i][0] = '\0';
        ds[i][strcspn(ds[i], "\n")] = '\0';
    }

    qsort(ds, n, sizeof(ds[0]), soSanhTang);   // sap xep theo thu tu tu dien

    printf("\n--- Sau khi sap xep ---\n");
    for (int i = 0; i < n; i++) printf("%d. %s\n", i + 1, ds[i]);

    // Sap xep giam dan
    qsort(ds, n, sizeof(ds[0]), soSanhGiam);
    printf("\n--- Giam dan ---\n");
    for (int i = 0; i < n; i++) printf("%s\n", ds[i]);
    return 0;
}
```

💡 `qsort` (trong `<stdlib.h>`) truyền cho hàm so sánh **địa chỉ của hai phần tử**. Với mảng 2 chiều `char ds[][51]`, địa chỉ phần tử chính là địa chỉ đầu xâu, nên chỉ cần ép về `const char *` rồi gọi `strcmp`.

💡 Sắp xếp **giảm dần** chỉ cần đảo thứ tự hai tham số của `strcmp`. Chi tiết về `qsort` xem bài [10-02 — Hàm qsort trong C](../10-02-c-ham-qsort-trong-c.md).

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int soSanhKhongPhanBiet(const char *a, const char *b) {
    int i = 0;
    while (a[i] && b[i]) {
        int ca = tolower((unsigned char)a[i]), cb = tolower((unsigned char)b[i]);
        if (ca != cb) return ca - cb;
        i++;
    }
    return (unsigned char)a[i] - (unsigned char)b[i];
}

// Mang cac CON TRO toi xau: moi phan tu co kieu const char *
int soSanhThuong(const void *a, const void *b) {
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}

int soSanhKhongHoa(const void *a, const void *b) {
    return soSanhKhongPhanBiet(*(const char * const *)a, *(const char * const *)b);
}

void inMang(const char *ds[], int n) {
    for (int i = 0; i < n; i++) printf("%s ", ds[i]);
    printf("\n");
}

int main(void) {
    const char *ds[] = {"Zebra", "apple", "Banana", "cherry", "Apple", "date"};
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("--- Sap xep THONG THUONG (phan biet hoa/thuong) ---\n");
    qsort(ds, n, sizeof(ds[0]), soSanhThuong);
    inMang(ds, n);

    printf("\n--- Sap xep KHONG phan biet hoa/thuong ---\n");
    qsort(ds, n, sizeof(ds[0]), soSanhKhongHoa);
    inMang(ds, n);
    return 0;
}
```

Output (thứ tự của `apple`/`Apple` có thể khác vì `qsort` không ổn định):

```
--- Sap xep THONG THUONG (phan biet hoa/thuong) ---
Apple Banana Zebra apple cherry date 

--- Sap xep KHONG phan biet hoa/thuong ---
Apple apple Banana cherry date Zebra 
```

⚠️ **Khác biệt với bài 4:** ở đây mảng chứa **con trỏ** (`const char *ds[]`), nên `qsort` truyền vào **địa chỉ của con trỏ** (`const char **`). Phải **giải tham chiếu một lần** `*(const char * const *)a` mới ra xâu. Nhầm giữa hai dạng là lỗi rất hay gặp.

💡 Sắp xếp mảng con trỏ chỉ **hoán đổi con trỏ** (8 byte) chứ không sao chép cả xâu — nhanh hơn với xâu dài.

⚠️ `qsort` **không đảm bảo ổn định**: `"apple"` và `"Apple"` bằng nhau khi không phân biệt hoa thường nên thứ tự giữa chúng có thể bất kỳ. Muốn cố định, thêm tiêu chí phụ: nếu bằng nhau thì trả về `strcmp(x, y)`.

### Bài 6.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *ds[] = {"cherry", "apple", "banana", "date", "elderberry"};
    int n = sizeof(ds) / sizeof(ds[0]);

    // Luu CHI SO (hoac con tro) cua phan tu nho nhat / lon nhat
    int iMin = 0, iMax = 0;
    for (int i = 1; i < n; i++) {
        if (strcmp(ds[i], ds[iMin]) < 0) iMin = i;
        if (strcmp(ds[i], ds[iMax]) > 0) iMax = i;
    }
    printf("Nho nhat: %s (vi tri %d)\n", ds[iMin], iMin);
    printf("Lon nhat: %s (vi tri %d)\n", ds[iMax], iMax);

    // Neu can luu ban sao noi dung thi dung strcpy
    char mn[50], mx[50];
    strcpy(mn, ds[iMin]);
    strcpy(mx, ds[iMax]);
    printf("Ban sao : %s, %s\n", mn, mx);
    return 0;
}
```

Output:

```
Nho nhat: apple (vi tri 1)
Lon nhat: elderberry (vi tri 4)
Ban sao : apple, elderberry
```

💡 Lưu **chỉ số** thay vì sao chép xâu mỗi lần tìm được phần tử mới — vừa nhanh vừa biết luôn vị trí.

⚠️ Không viết `mn = ds[i];` nếu `mn` là **mảng** `char mn[50]` — mảng không gán được. Hoặc dùng con trỏ `const char *mn = ds[i];`, hoặc dùng `strcpy`.

### Bài 7.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    printf("\"abc\" < \"abcd\"  = %d\n", strcmp("abc", "abcd") < 0);   // 1
    printf("\"10\"  < \"9\"     = %d\n", strcmp("10", "9") < 0);       // 1 !!
    printf("\"Z\"   < \"a\"     = %d\n", strcmp("Z", "a") < 0);        // 1
    printf("\"\"    < \"a\"     = %d\n", strcmp("", "a") < 0);         // 1
    printf("\"abc\" < \"abd\"   = %d\n", strcmp("abc", "abd") < 0);    // 1
    return 0;
}
```

**Giải thích từng trường hợp:**

| So sánh | Kết quả | Lý do |
|---|---|---|
| `"abc"` < `"abcd"` | ✅ đúng | `"abc"` là **tiền tố** của `"abcd"` → chuỗi ngắn hơn nhỏ hơn (`'\0'` < `'d'`) |
| `"10"` < `"9"` | ✅ **đúng** | So sánh ký tự đầu: `'1'` (49) < `'9'` (57). **Không so sánh giá trị số!** |
| `"Z"` < `"a"` | ✅ đúng | `'Z'` (90) < `'a'` (97) |
| `""` < `"a"` | ✅ đúng | Chuỗi rỗng luôn nhỏ nhất |
| `"abc"` < `"abd"` | ✅ đúng | Khác ở vị trí 2: `'c'` (99) < `'d'` (100) |

⚠️ **Trường hợp `"10" < "9"` là bẫy kinh điển.** Khi sắp xếp danh sách chuỗi số:

```
Thu tu tu dien:  "1", "10", "100", "2", "20", "3"
Thu tu so hoc:   "1", "2", "3", "10", "20", "100"
```

Đây là lý do tên file trong máy tính hay sắp xếp "lộn xộn": `file1, file10, file2` — xem bài 11 để khắc phục.

⚠️ Nếu viết `"abc" < "abcd"` (không có `strcmp`), C so sánh **địa chỉ** của hai hằng xâu — kết quả tuỳ trình biên dịch, không liên quan gì tới thứ tự từ điển.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>

int soSanh(const char *a, const char *b) {
    int i = 0;

    // So sanh tung ky tu cho toi khi khac nhau hoac het mot chuoi
    while (a[i] != '\0' && b[i] != '\0') {
        if ((unsigned char)a[i] < (unsigned char)b[i]) return -1;
        if ((unsigned char)a[i] > (unsigned char)b[i]) return  1;
        i++;
    }

    // Moi ky tu chung deu bang nhau -> xau nao con ky tu thi dai hon
    if (a[i] == '\0' && b[i] != '\0') return -1;
    if (a[i] != '\0' && b[i] == '\0') return  1;
    return 0;
}

int dau(int x) { return (x > 0) - (x < 0); }

int main(void) {
    const char *bo[][2] = {
        {"abc", "abd"}, {"abc", "abc"}, {"abcd", "abc"},
        {"Apple", "apple"}, {"", "a"}, {"10", "9"}
    };
    int n = sizeof(bo) / sizeof(bo[0]);

    for (int k = 0; k < n; k++) {
        const char *a = bo[k][0], *b = bo[k][1];
        int kq = soSanh(a, b);
        printf("soSanh(\"%s\", \"%s\") = %2d  -> %s\n", a, b, kq,
               kq < 0 ? "a < b" : (kq > 0 ? "a > b" : "a == b"));

        // Kiem chung voi strcmp
        if (kq != dau(strcmp(a, b))) printf("  !!! KHONG KHOP voi strcmp\n");
    }
    return 0;
}
```

💡 Đây chính là cách `strcmp` hoạt động bên trong. Chuẩn C quy định `strcmp` so sánh các ký tự như **`unsigned char`**, nên bản tự viết cũng ép kiểu như vậy để đúng cả với ký tự ngoài bảng ASCII.

💡 Viết gọn hơn bằng con trỏ:

```c
int soSanh2(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }
    return (unsigned char)*a - (unsigned char)*b;
}
```

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Tra ve con tro toi TU CUOI CUNG cua ho ten (thuong la ten)
const char *layTen(const char *hoTen) {
    const char *p = strrchr(hoTen, ' ');
    return (p == NULL) ? hoTen : p + 1;
}

int theoHo(const void *a, const void *b) {
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}

int theoTen(const void *a, const void *b) {
    const char *x = *(const char * const *)a;
    const char *y = *(const char * const *)b;
    int kq = strcmp(layTen(x), layTen(y));
    if (kq != 0) return kq;
    return strcmp(x, y);             // cung ten -> sap theo ho ten day du
}

int main(void) {
    const char *ds[] = {
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Hoang Cuong",
        "Pham Minh An",
        "Hoang Thi Dung"
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("--- Sap xep theo HO (mac dinh) ---\n");
    qsort(ds, n, sizeof(ds[0]), theoHo);
    for (int i = 0; i < n; i++) printf("  %s\n", ds[i]);

    printf("\n--- Sap xep theo TEN ---\n");
    qsort(ds, n, sizeof(ds[0]), theoTen);
    for (int i = 0; i < n; i++) printf("  %s (ten: %s)\n", ds[i], layTen(ds[i]));
    return 0;
}
```

Output:

```
--- Sap xep theo HO (mac dinh) ---
  Hoang Thi Dung
  Le Hoang Cuong
  Nguyen Van An
  Pham Minh An
  Tran Thi Binh

--- Sap xep theo TEN ---
  Nguyen Van An (ten: An)
  Pham Minh An (ten: An)
  Tran Thi Binh (ten: Binh)
  Le Hoang Cuong (ten: Cuong)
  Hoang Thi Dung (ten: Dung)
```

💡 **Tiêu chí phụ `return strcmp(x, y);`** đảm bảo kết quả xác định khi 2 người trùng tên — đặc biệt quan trọng vì `qsort` không ổn định.

💡 `layTen` trả về **con trỏ vào giữa xâu gốc** (sau dấu cách cuối) — không cần sao chép, không cần mảng phụ.

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int theoTuDien(const void *a, const void *b) {
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}

int theoGiaTri(const void *a, const void *b) {
    long long x = atoll(*(const char * const *)a);
    long long y = atoll(*(const char * const *)b);
    return (x > y) - (x < y);          // KHONG dung x - y (co the tran)
}

void inMang(const char *ds[], int n) {
    for (int i = 0; i < n; i++) printf("%s ", ds[i]);
    printf("\n");
}

int main(void) {
    const char *ds[] = {"10", "9", "100", "2", "20", "1", "3"};
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("--- Sap xep TU DIEN (strcmp) ---\n");
    qsort(ds, n, sizeof(ds[0]), theoTuDien);
    inMang(ds, n);

    printf("\n--- Sap xep theo GIA TRI SO ---\n");
    qsort(ds, n, sizeof(ds[0]), theoGiaTri);
    inMang(ds, n);
    return 0;
}
```

Output:

```
--- Sap xep TU DIEN (strcmp) ---
1 10 100 2 20 3 9 

--- Sap xep theo GIA TRI SO ---
1 2 3 9 10 20 100 
```

⚠️ `atoll` được gọi **rất nhiều lần** trong quá trình sắp xếp (O(n log n) lần). Với danh sách lớn, nên chuyển đổi trước vào một mảng struct:

```c
typedef struct { long long giaTri; const char *s; } Muc;
// dien mang Muc, roi qsort theo truong giaTri
```

⚠️ Viết `return x - y;` trong hàm so sánh là lỗi hay gặp: với `long long` kết quả phải ép về `int` (mất dữ liệu), và phép trừ còn có thể **tràn số**. Dùng `(x > y) - (x < y)` luôn an toàn.

💡 Nếu các chuỗi số **không có số 0 ở đầu**, có thể so sánh không cần đổi: chuỗi **ngắn hơn** thì nhỏ hơn, cùng độ dài thì dùng `strcmp`. Cách này đúng cả với số rất lớn vượt `long long`.

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// So sanh "tu nhien": tach cac cum SO ra so sanh theo gia tri
int soSanhTuNhien(const char *a, const char *b) {
    while (*a && *b) {
        if (isdigit((unsigned char)*a) && isdigit((unsigned char)*b)) {
            // Bo so 0 o dau moi cum
            while (*a == '0' && isdigit((unsigned char)a[1])) a++;
            while (*b == '0' && isdigit((unsigned char)b[1])) b++;

            // Do dai moi cum so
            size_t la = 0, lb = 0;
            while (isdigit((unsigned char)a[la])) la++;
            while (isdigit((unsigned char)b[lb])) lb++;

            if (la != lb) return (la < lb) ? -1 : 1;   // cum ngan hon -> nho hon
            int kq = strncmp(a, b, la);                 // cung do dai -> so tung chu so
            if (kq != 0) return kq;

            a += la; b += lb;
        } else {
            if (*a != *b) return (unsigned char)*a - (unsigned char)*b;
            a++; b++;
        }
    }
    return (unsigned char)*a - (unsigned char)*b;
}

int cmpTuDien(const void *x, const void *y) {
    return strcmp(*(const char * const *)x, *(const char * const *)y);
}

int cmpTuNhien(const void *x, const void *y) {
    return soSanhTuNhien(*(const char * const *)x, *(const char * const *)y);
}

int main(void) {
    const char *ds[] = {"file10", "file2", "file1", "file20", "file3", "img100", "img9"};
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("--- Sap xep TU DIEN ---\n");
    qsort(ds, n, sizeof(ds[0]), cmpTuDien);
    for (int i = 0; i < n; i++) printf("%s ", ds[i]);
    printf("\n");

    printf("\n--- Sap xep TU NHIEN ---\n");
    qsort(ds, n, sizeof(ds[0]), cmpTuNhien);
    for (int i = 0; i < n; i++) printf("%s ", ds[i]);
    printf("\n");
    return 0;
}
```

Output:

```
--- Sap xep TU DIEN ---
file1 file10 file2 file20 file3 img100 img9 

--- Sap xep TU NHIEN ---
file1 file2 file3 file10 file20 img9 img100 
```

💡 **Natural sort** là cách Windows Explorer và macOS Finder sắp xếp tên file — đúng với trực giác con người hơn nhiều.

💡 So sánh cụm số bằng **độ dài trước, rồi `strncmp`** thay vì đổi sang số — không bao giờ tràn, dù cụm số dài bao nhiêu.

### Bài 12.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Tra ve -1 neu da sap xep, nguoc lai tra ve vi tri dau tien sai thu tu
int viTriSai(const char *ds[], int n) {
    for (int i = 0; i + 1 < n; i++)
        if (strcmp(ds[i], ds[i + 1]) > 0) return i + 1;
    return -1;
}

bool daSapXep(const char *ds[], int n) {
    return viTriSai(ds, n) == -1;
}

int main(void) {
    const char *a[] = {"apple", "banana", "cherry"};
    const char *b[] = {"banana", "apple", "cherry"};

    printf("a da sap xep? %s\n", daSapXep(a, 3) ? "true" : "false");   // true
    printf("b da sap xep? %s\n", daSapXep(b, 3) ? "true" : "false");   // false

    // Tim vi tri dau tien sai thu tu
    int vt = viTriSai(b, 3);
    if (vt != -1)
        printf("Phan tu dau tien sai thu tu: \"%s\" tai vi tri %d\n", b[vt], vt);
    return 0;
}
```

Output:

```
a da sap xep? true
b da sap xep? false
Phan tu dau tien sai thu tu: "apple" tai vi tri 1
```

💡 Hàm `viTriSai` trả về vị trí phần tử **đầu tiên phá vỡ** thứ tự — rất hữu ích khi debug. Chỉ cần so sánh các cặp **liền kề**, độ phức tạp O(n).

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Ghi tien to chung dai nhat vao kq
void tienToChung(const char *ds[], int n, char *kq) {
    kq[0] = '\0';
    if (n == 0) return;

    size_t len = strlen(ds[0]);            // do dai tien to hien tai
    for (int i = 1; i < n && len > 0; i++) {
        size_t j = 0;
        while (j < len && ds[i][j] == ds[0][j]) j++;   // dung o '\0' cua ds[i]
        len = j;
    }
    strncpy(kq, ds[0], len);
    kq[len] = '\0';
}

int cmp(const void *a, const void *b) {
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}

// Cach toi uu: chi can so sanh chuoi NHO NHAT va LON NHAT
void tienToChung2(const char *ds[], int n, char *kq) {
    kq[0] = '\0';
    if (n == 0) return;
    qsort(ds, n, sizeof(ds[0]), cmp);

    const char *dau = ds[0], *cuoi = ds[n - 1];
    size_t j = 0;
    while (dau[j] != '\0' && dau[j] == cuoi[j]) j++;
    strncpy(kq, dau, j);
    kq[j] = '\0';
}

void thu(const char *ds[], int n) {
    char kq1[100], kq2[100];
    tienToChung(ds, n, kq1);
    printf("{ ");
    for (int i = 0; i < n; i++) printf("\"%s\" ", ds[i]);
    printf("} -> \"%s\"", kq1);
    tienToChung2(ds, n, kq2);
    printf("  (cach 2: \"%s\")\n", kq2);
}

int main(void) {
    const char *t1[] = {"flower", "flow", "flight"};
    const char *t2[] = {"interspecies", "interstellar", "interstate"};
    const char *t3[] = {"dog", "racecar", "car"};
    const char *t4[] = {"abc"};

    thu(t1, 3);
    thu(t2, 3);
    thu(t3, 3);
    thu(t4, 1);
    thu(NULL, 0);
    return 0;
}
```

Output:

```
{ "flower" "flow" "flight" } -> "fl"  (cach 2: "fl")
{ "interspecies" "interstellar" "interstate" } -> "inters"  (cach 2: "inters")
{ "dog" "racecar" "car" } -> ""  (cach 2: "")
{ "abc" } -> "abc"  (cach 2: "abc")
{ } -> ""  (cach 2: "")
```

💡 **Cách 2 rất thông minh:** sau khi sắp xếp, tiền tố chung của **toàn bộ** danh sách chính là tiền tố chung của chuỗi **nhỏ nhất** và **lớn nhất** — vì mọi chuỗi ở giữa đều "kẹp" giữa chúng.

⚠️ Cách 2 **sắp xếp lại mảng của người gọi**. Nếu không muốn thay đổi thứ tự gốc, hãy sao chép mảng con trỏ trước khi gọi `qsort`.

💡 Vòng `while (j < len && ds[i][j] == ds[0][j])` tự dừng ở cuối `ds[i]`: khi `ds[i][j] == '\0'` thì nó khác `ds[0][j]` (vì `j < len`, ký tự đó của `ds[0]` khác `'\0'`).

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int theoDoDai(const void *a, const void *b) {
    const char *x = *(const char * const *)a;
    const char *y = *(const char * const *)b;
    size_t lx = strlen(x), ly = strlen(y);
    if (lx != ly) return (lx < ly) ? -1 : 1;   // tieu chi CHINH
    return strcmp(x, y);                        // tieu chi PHU
}

int main(void) {
    const char *ds[] = {"banana", "kiwi", "apple", "fig", "date", "cherry", "plum"};
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), theoDoDai);

    printf("--- Sap xep theo do dai, roi tu dien ---\n");
    for (int i = 0; i < n; i++)
        printf("  %s (%zu ky tu)\n", ds[i], strlen(ds[i]));
    return 0;
}
```

Output:

```
--- Sap xep theo do dai, roi tu dien ---
  fig (3 ky tu)
  date (4 ky tu)
  kiwi (4 ky tu)
  plum (4 ky tu)
  apple (5 ky tu)
  banana (6 ky tu)
  cherry (6 ky tu)
```

💡 **Mẫu hàm so sánh nhiều tiêu chí:**

```c
if (tieuChi1(a) != tieuChi1(b)) return tieuChi1(a) < tieuChi1(b) ? -1 : 1;
if (tieuChi2(a) != tieuChi2(b)) return tieuChi2(a) < tieuChi2(b) ? -1 : 1;
return soSanhTieuChi3(a, b);
```

Luôn kiểm tra **khác nhau** trước rồi mới so sánh — nếu không, hàm so sánh sẽ sai.

⚠️ Đừng viết `return lx - ly;` — `size_t` là **kiểu không dấu**, hiệu của hai số `size_t` không bao giờ âm, nên kết quả sai hoàn toàn.

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TU 100

typedef struct {
    char tu[30];
    char nghia[50];
} MucTu;

typedef struct {
    MucTu ds[MAX_TU];
    int soLuong;
} TuDien;

int soSanhKhongPhanBiet(const char *a, const char *b) {
    while (*a && tolower((unsigned char)*a) == tolower((unsigned char)*b)) { a++; b++; }
    return tolower((unsigned char)*a) - tolower((unsigned char)*b);
}

// So sanh n ky tu dau, khong phan biet hoa thuong
int soSanhNKyTu(const char *a, const char *b, size_t n) {
    for (size_t i = 0; i < n; i++) {
        int ca = tolower((unsigned char)a[i]), cb = tolower((unsigned char)b[i]);
        if (ca != cb || ca == '\0') return ca - cb;
    }
    return 0;
}

void them(TuDien *td, const char *tu, const char *nghia) {
    if (td->soLuong == MAX_TU) return;
    MucTu *m = &td->ds[td->soLuong++];
    snprintf(m->tu, sizeof(m->tu), "%s", tu);
    snprintf(m->nghia, sizeof(m->nghia), "%s", nghia);
}

int cmpMucTu(const void *a, const void *b) {
    return soSanhKhongPhanBiet(((const MucTu *)a)->tu, ((const MucTu *)b)->tu);
}

void sapXep(TuDien *td) {
    qsort(td->ds, td->soLuong, sizeof(MucTu), cmpMucTu);
}

// Tim kiem NHI PHAN - O(log n)
const MucTu *tim(const TuDien *td, const char *tu) {
    int trai = 0, phai = td->soLuong - 1;
    while (trai <= phai) {
        int giua = trai + (phai - trai) / 2;
        int kq = soSanhKhongPhanBiet(td->ds[giua].tu, tu);
        if (kq == 0)      return &td->ds[giua];
        else if (kq < 0)  trai = giua + 1;
        else              phai = giua - 1;
    }
    return NULL;
}

// In cac tu bat dau bang tien to
void timTienTo(const TuDien *td, const char *tienTo) {
    size_t n = strlen(tienTo);
    for (int i = 0; i < td->soLuong; i++)
        if (soSanhNKyTu(td->ds[i].tu, tienTo, n) == 0)
            printf("  %s : %s\n", td->ds[i].tu, td->ds[i].nghia);
}

void hienThi(const TuDien *td) {
    for (int i = 0; i < td->soLuong; i++)
        printf("  %s : %s\n", td->ds[i].tu, td->ds[i].nghia);
}

int main(void) {
    static TuDien td;              // static: tu dong khoi tao 0, khong chiem stack
    td.soLuong = 0;
    them(&td, "apple",    "qua tao");
    them(&td, "banana",   "qua chuoi");
    them(&td, "cat",      "con meo");
    them(&td, "dog",      "con cho");
    them(&td, "elephant", "con voi");
    them(&td, "car",      "o to");
    them(&td, "cake",     "banh ngot");

    sapXep(&td);

    printf("=== TU DIEN (%d tu) ===\n", td.soLuong);
    hienThi(&td);

    // Tim kiem chinh xac
    printf("\n=== TIM KIEM ===\n");
    const char *canTim[] = {"cat", "Dog", "xyz"};
    for (int i = 0; i < 3; i++) {
        const MucTu *m = tim(&td, canTim[i]);
        if (m) printf("  \"%s\" -> %s\n", canTim[i], m->nghia);
        else   printf("  \"%s\" -> khong tim thay\n", canTim[i]);
    }

    // Tim theo tien to
    printf("\n=== GOI Y VOI TIEN TO \"ca\" ===\n");
    timTienTo(&td, "ca");
    return 0;
}
```

Output:

```
=== TU DIEN (7 tu) ===
  apple : qua tao
  banana : qua chuoi
  cake : banh ngot
  car : o to
  cat : con meo
  dog : con cho
  elephant : con voi

=== TIM KIEM ===
  "cat" -> con meo
  "Dog" -> con cho
  "xyz" -> khong tim thay

=== GOI Y VOI TIEN TO "ca" ===
  cake : banh ngot
  car : o to
  cat : con meo
```

**Vì sao từ điển phải sắp xếp:** tìm kiếm nhị phân yêu cầu dữ liệu **đã sắp xếp** — và phải sắp xếp bằng **đúng hàm so sánh** dùng khi tìm (ở đây là không phân biệt hoa thường). Với 100.000 từ:

| Cách tìm | Số phép so sánh |
|---|---|
| Tuyến tính | tối đa 100.000 |
| **Nhị phân** | tối đa **17** |

Xem chi tiết ở bài [10-01 — Tìm kiếm nhị phân](../10-01-c-thuat-toan-tim-kiem-nhi-phan.md).

💡 C không có `class`, nên "đối tượng" từ điển được biểu diễn bằng `struct TuDien` và các hàm nhận **con trỏ** `TuDien *td` để thao tác. Thư viện chuẩn còn có hàm `bsearch()` trong `<stdlib.h>` làm sẵn việc tìm kiếm nhị phân — xem bài [10-06](../10-06-c-ham-bsearch-va-lower-bound-upper-bound.md).
