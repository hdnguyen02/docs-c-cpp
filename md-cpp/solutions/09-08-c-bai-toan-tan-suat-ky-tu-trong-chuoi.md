# Lời giải — [C]. Bài Toán Tần Suất Ký Tự Trong Chuỗi

[← Quay lại bài học](../09-08-c-bai-toan-tan-suat-ky-tu-trong-chuoi.md)

> **Kỹ thuật cốt lõi:** dùng **mảng đánh dấu** — lấy mã ký tự làm chỉ số. Mọi thao tác tra cứu và cập nhật đều **O(1)**. Nhớ ép `(unsigned char)` trước khi dùng ký tự làm chỉ số mảng.

---

### Bài 1.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;

    int dem[26] = {0};

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if (isalpha(c)) dem[tolower(c) - 'a']++;
    }

    printf("\nTan suat cac chu cai:\n");
    for (int i = 0; i < 26; i++)
        if (dem[i] > 0)
            printf("  '%c' : %d lan\n", 'a' + i, dem[i]);
    return 0;
}
```

**Công thức ánh xạ:** `'a'` → 0, `'b'` → 1, …, `'z'` → 25 nhờ `c - 'a'`.

`tolower` đưa mọi chữ cái về thường trước, nên `'A'` và `'a'` được đếm chung.

### Bài 2.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;

    int dem[256] = {0};

    for (int i = 0; s[i] != '\0'; i++)
        dem[(unsigned char)s[i]]++;          // dung TRUC TIEP ma ky tu lam chi so

    printf("\nTan suat moi ky tu:\n");
    for (int i = 0; i < 256; i++) {
        if (dem[i] > 0) {
            if (isprint(i)) printf("  '%c'  ", i);
            else            printf("  [%3d]", i);     // ky tu khong in duoc, vd '\n'
            printf(" (ma %3d) : %d lan\n", i, dem[i]);
        }
    }
    return 0;
}
```

⚠️ **Bắt buộc ép `(unsigned char)`** khi dùng ký tự làm chỉ số. Nếu `char` là kiểu có dấu (phổ biến trên GCC), ký tự có mã > 127 sẽ âm và `dem[c]` ghi ra **ngoài mảng** → crash hoặc hỏng dữ liệu.

💡 Mảng 256 phần tử phủ hết bảng mã 1 byte, nên đếm được **mọi** ký tự chứ không chỉ chữ cái. Ký tự `'\n'` do `fgets` đọc vào cũng được đếm (mã 10).

### Bài 3.

```c
#include <stdio.h>
#include <ctype.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;

    int dem[26] = {0};
    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if (isalpha(c)) dem[tolower(c) - 'a']++;
    }

    int viTriMax = -1, viTriMin = -1;
    for (int i = 0; i < 26; i++) {
        if (dem[i] == 0) continue;
        if (viTriMax == -1 || dem[i] > dem[viTriMax]) viTriMax = i;
        if (viTriMin == -1 || dem[i] < dem[viTriMin]) viTriMin = i;
    }

    if (viTriMax == -1) {
        printf("Chuoi khong co chu cai nao!\n");
        return 0;
    }

    printf("Nhieu nhat: '%c' - %d lan\n", 'a' + viTriMax, dem[viTriMax]);
    printf("It nhat   : '%c' - %d lan\n", 'a' + viTriMin, dem[viTriMin]);

    // Liet ke TAT CA ky tu co tan suat cao nhat (co the co nhieu)
    printf("\nTat ca ky tu xuat hien nhieu nhat: ");
    for (int i = 0; i < 26; i++)
        if (dem[i] == dem[viTriMax]) printf("'%c' ", 'a' + i);
    printf("\n");
    return 0;
}
```

⚠️ **Phải bỏ qua các ký tự có `dem[i] == 0`** khi tìm min — nếu không, kết quả luôn là một chữ cái không xuất hiện.

### Bài 4.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    int dem[256] = {0};
    for (int i = 0; s[i] != '\0'; i++)             // LUOT 1: dem
        dem[(unsigned char)s[i]]++;

    for (int i = 0; s[i] != '\0'; i++) {           // LUOT 2: tim theo THU TU chuoi
        if (dem[(unsigned char)s[i]] == 1) {
            printf("Ky tu dau tien khong lap: '%c'\n", s[i]);
            return 0;
        }
    }

    printf("Moi ky tu deu lap lai!\n");
    return 0;
}
```

Ví dụ:

```
"leetcode"     -> 'l'
"loveleetcode" -> 'v'
"aabb"         -> Moi ky tu deu lap lai!
```

💡 **Mẫu "2 lượt duyệt" rất quan trọng:**
- **Lượt 1** duyệt để đếm (thứ tự không quan trọng)
- **Lượt 2** duyệt **theo thứ tự chuỗi gốc** để tìm cái đầu tiên thoả điều kiện

Nếu duyệt mảng `dem` thay vì chuỗi, bạn sẽ được ký tự có mã nhỏ nhất, không phải ký tự **đầu tiên** trong chuỗi.

Độ phức tạp **O(n)** — tốt hơn hẳn cách so sánh mọi cặp O(n²).

⚠️ Phải xoá `'\n'` sau `fgets`, nếu không `'\n'` (xuất hiện đúng 1 lần) có thể bị báo là "ký tự không lặp".

### Bài 5.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    bool daGap[256] = {false};

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if (daGap[c]) {
            printf("Ky tu dau tien bi lap: '%c'\n", s[i]);
            return 0;
        }
        daGap[c] = true;
    }

    printf("Khong co ky tu nao lap lai!\n");
    return 0;
}
```

💡 **Chỉ cần MỘT lượt duyệt** — khác với bài 4 phải 2 lượt. Vì "bị lặp" nghĩa là "đã gặp trước đó", ta biết ngay khi gặp lần thứ hai.

### Bài 6.

```c
#include <stdio.h>
#include <ctype.h>

#define DO_RONG 40

void inLap(char c, int n) {
    for (int i = 0; i < n; i++) putchar(c);
}

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;

    int dem[26] = {0};
    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if (isalpha(c)) dem[tolower(c) - 'a']++;
    }

    // Tim tan suat lon nhat de chuan hoa do dai cot
    int maxDem = 0;
    for (int i = 0; i < 26; i++)
        if (dem[i] > maxDem) maxDem = dem[i];
    if (maxDem == 0) { printf("Khong co chu cai nao!\n"); return 0; }

    printf("\nBIEU DO TAN SUAT\n");
    inLap('=', DO_RONG + 12); printf("\n");

    for (int i = 0; i < 26; i++) {
        if (dem[i] == 0) continue;

        int doDai = dem[i] * DO_RONG / maxDem;
        if (doDai == 0) doDai = 1;

        printf(" '%c' | ", 'a' + i);
        inLap('*', doDai);
        printf("%*d\n", DO_RONG - doDai + 4, dem[i]);   // do rong dong
    }
    inLap('=', DO_RONG + 12); printf("\n");
    return 0;
}
```

Ví dụ với `"lap trinh c that thu vi"`:

```
BIEU DO TAN SUAT
====================================================
 'a' | ********************                       2
 'c' | **********                                 1
 'h' | ******************************             3
 'i' | ********************                       2
 'l' | **********                                 1
 'n' | **********                                 1
 'p' | **********                                 1
 'r' | **********                                 1
 't' | ****************************************   4
 'u' | **********                                 1
 'v' | **********                                 1
====================================================
```

💡 **Chuẩn hoá độ dài:** `doDai = dem[i] * DO_RONG / maxDem` — cột cao nhất luôn đúng `DO_RONG` ký tự, các cột khác tỉ lệ theo.

💡 **`%*d`** cho phép truyền độ rộng ô bằng một tham số `int` đứng trước giá trị cần in.

### Bài 7.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

bool laDaoChu(const char *a, const char *b) {
    int dem[26] = {0};

    for (; *a; a++) if (isalpha((unsigned char)*a)) dem[tolower((unsigned char)*a) - 'a']++;
    for (; *b; b++) if (isalpha((unsigned char)*b)) dem[tolower((unsigned char)*b) - 'a']--;

    for (int i = 0; i < 26; i++)
        if (dem[i] != 0) return false;

    return true;
}

int main(void) {
    struct { const char *a; const char *b; } bo[] = {
        {"listen",     "silent"},
        {"Dormitory",  "Dirty Room"},
        {"hello",      "world"},
        {"Astronomer", "Moon starer"},
        {"abc",        "abcd"}
    };
    int n = sizeof(bo) / sizeof(bo[0]);

    for (int i = 0; i < n; i++) {
        printf("\"%s\" vs \"%s\" -> %s\n", bo[i].a, bo[i].b,
               laDaoChu(bo[i].a, bo[i].b) ? "LA dao chu" : "khong");
    }
    return 0;
}
```

Output:

```
"listen" vs "silent" -> LA dao chu
"Dormitory" vs "Dirty Room" -> LA dao chu
"hello" vs "world" -> khong
"Astronomer" vs "Moon starer" -> LA dao chu
"abc" vs "abcd" -> khong
```

💡 **Kỹ thuật thanh lịch: một mảng, chuỗi đầu CỘNG, chuỗi sau TRỪ.** Nếu là đảo chữ thì mọi ô về 0.

Độ phức tạp **O(n)** — tốt hơn cách sắp xếp 2 chuỗi bằng `qsort` rồi so sánh (O(n log n)).

### Bài 8.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;

    bool coMat[26] = {false};
    int soChuKhacNhau = 0;

    for (int k = 0; s[k] != '\0'; k++) {
        unsigned char c = (unsigned char)s[k];
        if (isalpha(c)) {
            int i = tolower(c) - 'a';
            if (!coMat[i]) { coMat[i] = true; soChuKhacNhau++; }
        }
    }

    if (soChuKhacNhau == 26) {
        printf("LA PANGRAM! (co du 26 chu cai)\n");
    } else {
        printf("KHONG phai pangram (co %d/26 chu)\n", soChuKhacNhau);
        printf("Thieu cac chu: ");
        for (int i = 0; i < 26; i++)
            if (!coMat[i]) printf("%c ", 'a' + i);
        printf("\n");
    }
    return 0;
}
```

Thử với pangram tiếng Anh nổi tiếng:

```
Nhap chuoi: The quick brown fox jumps over the lazy dog
LA PANGRAM! (co du 26 chu cai)
```

💡 **Pangram** được dùng để kiểm tra font chữ, thử máy đánh chữ, và luyện gõ phím.

Một pangram ngắn khác: `"Pack my box with five dozen liquor jugs"`

### Bài 9.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_TU 500

typedef struct {
    char tu[50];
    int soLan;
} TanSuat;

// Bo dau cau o dau va cuoi tu, chuyen ve chu thuong (sua tai cho)
void chuanHoaTu(char *t) {
    int n = (int)strlen(t);
    while (n > 0 && !isalnum((unsigned char)t[n - 1])) t[--n] = '\0';   // cuoi
    int dau = 0;
    while (t[dau] != '\0' && !isalnum((unsigned char)t[dau])) dau++;    // dau
    memmove(t, t + dau, strlen(t + dau) + 1);
    for (int i = 0; t[i]; i++) t[i] = (char)tolower((unsigned char)t[i]);
}

// Tim tu trong mang, tra ve vi tri hoac -1
int timTu(TanSuat ds[], int n, const char *tu) {
    for (int i = 0; i < n; i++)
        if (strcmp(ds[i].tu, tu) == 0) return i;
    return -1;
}

int main(void) {
    char vanBan[1000];
    printf("Nhap doan van: ");
    if (fgets(vanBan, sizeof vanBan, stdin) == NULL) return 0;

    TanSuat ds[MAX_TU];
    int n = 0;

    for (char *t = strtok(vanBan, " \t\n"); t != NULL; t = strtok(NULL, " \t\n")) {
        chuanHoaTu(t);
        if (t[0] == '\0' || strlen(t) >= 50) continue;

        int vt = timTu(ds, n, t);
        if (vt >= 0) {
            ds[vt].soLan++;
        } else if (n < MAX_TU) {
            strcpy(ds[n].tu, t);
            ds[n].soLan = 1;
            n++;
        }
    }

    printf("\nTan suat cac tu (theo thu tu xuat hien):\n");
    for (int i = 0; i < n; i++)
        printf("  %s : %d\n", ds[i].tu, ds[i].soLan);

    printf("\nTong: %d tu khac nhau\n", n);
    return 0;
}
```

Ví dụ:

```
Nhap doan van: Toi hoc C. C rat hay, toi thich C!

Tan suat cac tu (theo thu tu xuat hien):
  toi : 2
  hoc : 1
  c : 3
  rat : 1
  hay : 1
  thich : 1

Tong: 6 tu khac nhau
```

💡 **C không có `map`**, nên ta tự quản lý một **mảng `struct`** gồm từ và số lần. Mỗi từ mới phải tìm tuyến tính trong mảng: độ phức tạp **O(n × k)** với `k` là số từ khác nhau — đủ nhanh cho văn bản vừa phải. Với dữ liệu lớn, cần bảng băm (hash table) tự cài đặt.

⚠️ **Chuẩn hoá từ rất quan trọng:** không chuẩn hoá thì `"C."`, `"C"`, `"c!"` bị đếm là 3 từ khác nhau.

💡 `memmove` (không phải `strcpy`) được dùng để dịch chuỗi sang trái vì vùng nguồn và vùng đích **chồng lên nhau**.

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TU 500

typedef struct {
    char tu[50];
    int soLan;
} TanSuat;

void chuanHoaTu(char *t) {
    int n = (int)strlen(t);
    while (n > 0 && !isalnum((unsigned char)t[n - 1])) t[--n] = '\0';
    int dau = 0;
    while (t[dau] != '\0' && !isalnum((unsigned char)t[dau])) dau++;
    memmove(t, t + dau, strlen(t + dau) + 1);
    for (int i = 0; t[i]; i++) t[i] = (char)tolower((unsigned char)t[i]);
}

// Tan suat GIAM dan, bang nhau thi theo tu dien A-Z
int soSanh(const void *a, const void *b) {
    const TanSuat *x = a, *y = b;
    if (x->soLan != y->soLan) return y->soLan - x->soLan;
    return strcmp(x->tu, y->tu);
}

int main(void) {
    char vanBan[] =
        "lap trinh C rat hay. Hoc lap trinh giup tu duy tot. "
        "C manh me, C nhanh. Lap trinh la ky nang quan trong. "
        "Hoc C de hoc cac ngon ngu khac.";

    TanSuat ds[MAX_TU];
    int n = 0;

    for (char *t = strtok(vanBan, " \t\n"); t != NULL; t = strtok(NULL, " \t\n")) {
        chuanHoaTu(t);
        if (t[0] == '\0' || strlen(t) >= 50) continue;

        int vt = -1;
        for (int i = 0; i < n; i++)
            if (strcmp(ds[i].tu, t) == 0) { vt = i; break; }

        if (vt >= 0) ds[vt].soLan++;
        else if (n < MAX_TU) { strcpy(ds[n].tu, t); ds[n].soLan = 1; n++; }
    }

    qsort(ds, n, sizeof(TanSuat), soSanh);

    printf("TOP 5 TU XUAT HIEN NHIEU NHAT:\n");
    printf("+------+----------------+---------+\n");
    printf("| HANG | TU             | SO LAN  |\n");
    printf("+------+----------------+---------+\n");
    for (int i = 0; i < n && i < 5; i++)
        printf("| %-4d | %-14s | %7d |\n", i + 1, ds[i].tu, ds[i].soLan);
    printf("+------+----------------+---------+\n");
    return 0;
}
```

Output:

```
TOP 5 TU XUAT HIEN NHIEU NHAT:
+------+----------------+---------+
| HANG | TU             | SO LAN  |
+------+----------------+---------+
| 1    | c              |       4 |
| 2    | hoc            |       3 |
| 3    | lap            |       3 |
| 4    | trinh          |       3 |
| 5    | cac            |       1 |
+------+----------------+---------+
```

💡 **Mẫu "đếm → qsort"** rất thường dùng: đếm vào mảng `struct`, sau đó `qsort` theo **số lần** với hàm so sánh tự viết. Hàm so sánh trả về số âm nếu `a` đứng trước `b`, dương nếu `a` đứng sau.

⚠️ `return y->soLan - x->soLan;` an toàn ở đây vì số lần là số nhỏ, không bị tràn khi trừ.

### Bài 11.

```c
#include <stdio.h>
#include <stdbool.h>

void xoaLap(const char *s, char *kq) {
    bool daGap[256] = {false};
    int k = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if (!daGap[c]) {
            daGap[c] = true;
            kq[k++] = s[i];
        }
    }
    kq[k] = '\0';
}

int main(void) {
    const char *ds[] = {"programming", "aabbcc", "hello world", "abcdef"};
    char kq[100];

    for (int i = 0; i < 4; i++) {
        xoaLap(ds[i], kq);
        printf("\"%s\" -> \"%s\"\n", ds[i], kq);
    }
    return 0;
}
```

Output:

```
"programming" -> "progamin"
"aabbcc" -> "abc"
"hello world" -> "helo wrd"
"abcdef" -> "abcdef"
```

Độ phức tạp **O(n)** thời gian, **O(1)** bộ nhớ phụ (mảng 256 phần tử cố định).

### Bài 12.

```c
#include <stdio.h>
#include <ctype.h>
#include <stdbool.h>

bool coTheThanhDoiXung(const char *s) {
    int dem[256] = {0};
    for (; *s; s++) {
        unsigned char c = (unsigned char)*s;
        if (isalnum(c)) dem[tolower(c)]++;
    }

    int soLe = 0;
    for (int i = 0; i < 256; i++)
        if (dem[i] % 2 == 1) soLe++;

    return soLe <= 1;                   // toi da MOT ky tu co tan suat le
}

int main(void) {
    const char *ds[] = {"aabb", "abcba", "abc", "racecar", "aabbc", "aabbcc"};

    for (int i = 0; i < 6; i++) {
        printf("\"%s\" -> %s\n", ds[i],
               coTheThanhDoiXung(ds[i]) ? "CO the sap xep thanh doi xung" : "khong the");
    }
    return 0;
}
```

Output:

```
"aabb" -> CO the sap xep thanh doi xung      (abba)
"abcba" -> CO the sap xep thanh doi xung     (da doi xung)
"abc" -> khong the
"racecar" -> CO the sap xep thanh doi xung
"aabbc" -> CO the sap xep thanh doi xung     (abcba)
"aabbcc" -> CO the sap xep thanh doi xung    (abccba)
```

**Chứng minh điều kiện:**

Trong một chuỗi đối xứng, mỗi ký tự ở vị trí `i` phải khớp với ký tự ở vị trí `n-1-i`. Nên:
- Với chuỗi **độ dài chẵn**: mọi ký tự phải xuất hiện **số lần chẵn**
- Với chuỗi **độ dài lẻ**: đúng **một** ký tự được phép xuất hiện số lần lẻ (nó nằm ở giữa)

→ Điều kiện: **số ký tự có tần suất lẻ ≤ 1**.

### Bài 13.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[500];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    int lanCuoi[256];
    for (int i = 0; i < 256; i++) lanCuoi[i] = -1;    // -1 = chua gap

    int doDaiMax = 0, batDauMax = 0;
    int trai = 0;
    int n = (int)strlen(s);

    for (int phai = 0; phai < n; phai++) {
        unsigned char c = (unsigned char)s[phai];

        // Neu ky tu nay da xuat hien TRONG cua so hien tai -> day bien trai
        if (lanCuoi[c] >= trai) {
            trai = lanCuoi[c] + 1;
        }

        lanCuoi[c] = phai;

        int doDai = phai - trai + 1;
        if (doDai > doDaiMax) {
            doDaiMax  = doDai;
            batDauMax = trai;
        }
    }

    // %.*s in dung doDaiMax ky tu bat dau tu s + batDauMax
    printf("Chuoi con dai nhat khong lap: \"%.*s\"\n", doDaiMax, s + batDauMax);
    printf("Do dai: %d\n", doDaiMax);
    return 0;
}
```

Ví dụ:

```
"abcabcbb"  -> "abc"  (do dai 3)
"bbbbb"     -> "b"    (do dai 1)
"pwwkew"    -> "wke"  (do dai 3)
"codelab"   -> "codelab" (do dai 7)
```

**Kỹ thuật cửa sổ trượt (sliding window):**
- `trai`, `phai` là 2 biên của cửa sổ đang xét
- Mở rộng `phai` mỗi bước
- Khi gặp ký tự đã có **trong cửa sổ**, đẩy `trai` qua vị trí cũ của nó

**Độ phức tạp O(n)** — mỗi ký tự chỉ được xét đúng một lần. So với cách vét cạn mọi chuỗi con là O(n³).

⚠️ Điều kiện `lanCuoi[c] >= trai` rất quan trọng — nó phân biệt "ký tự đã gặp **trong cửa sổ**" với "đã gặp nhưng **ngoài** cửa sổ".

### Bài 14.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Nen RLE: ghi ket qua vao kq
void nenRLE(const char *s, char *kq) {
    int k = 0, i = 0;
    while (s[i] != '\0') {
        char c = s[i];
        int dem = 0;
        while (s[i] == c) { dem++; i++; }
        k += sprintf(kq + k, "%c%d", c, dem);   // sprintf tra ve so ky tu da ghi
    }
    kq[k] = '\0';
}

void giaiNenRLE(const char *s, char *kq) {
    int k = 0, i = 0;
    while (s[i] != '\0') {
        char c = s[i++];
        int dem = 0;
        while (isdigit((unsigned char)s[i])) dem = dem * 10 + (s[i++] - '0');
        if (dem == 0) dem = 1;
        for (int j = 0; j < dem; j++) kq[k++] = c;
    }
    kq[k] = '\0';
}

int main(void) {
    const char *ds[] = {"aaabbc", "aabcccccaaa", "abcdef", "aaaaaaaaaaaa"};
    char nen[100], giai[100];

    printf("+----------------+----------------+-----------+\n");
    printf("| GOC            | NEN            | TI LE     |\n");
    printf("+----------------+----------------+-----------+\n");

    for (int i = 0; i < 4; i++) {
        nenRLE(ds[i], nen);
        int tiLe = (int)(100.0 * strlen(nen) / strlen(ds[i]));
        printf("| %-14s | %-14s | %4d%%     |\n", ds[i], nen, tiLe);

        // Kiem tra giai nen dung
        giaiNenRLE(nen, giai);
        if (strcmp(giai, ds[i]) != 0) printf("  !!! GIAI NEN SAI\n");
    }
    printf("+----------------+----------------+-----------+\n");
    return 0;
}
```

Output:

```
+----------------+----------------+-----------+
| GOC            | NEN            | TI LE     |
+----------------+----------------+-----------+
| aaabbc         | a3b2c1         |  100%     |
| aabcccccaaa    | a2b1c5a3       |   72%     |
| abcdef         | a1b1c1d1e1f1   |  200%     |
| aaaaaaaaaaaa   | a12            |   25%     |
+----------------+----------------+-----------+
```

⚠️ **RLE chỉ hiệu quả khi dữ liệu có nhiều đoạn lặp.** Với chuỗi không lặp (`"abcdef"`), nó **phình to gấp đôi**.

💡 **`sprintf` trả về số ký tự đã ghi** — cộng dồn vào `k` là cách gọn để nối nhiều mẩu vào cuối chuỗi kết quả.

💡 **Cải tiến thực tế:** so sánh kích thước rồi chọn bản nhỏ hơn:

```c
void nenThongMinh(const char *s, char *kq) {
    nenRLE(s, kq);
    if (strlen(kq) >= strlen(s)) strcpy(kq, s);
}
```

RLE được dùng trong định dạng ảnh BMP, fax, và là bước tiền xử lý trong nhiều thuật toán nén khác.

### Bài 15.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_TU 1000

typedef struct { char tu[50]; int soLan; } TanSuat;
typedef struct { char chu; int soLan; } DemChu;

void chuanHoaTu(char *t) {
    int n = (int)strlen(t);
    while (n > 0 && !isalnum((unsigned char)t[n - 1])) t[--n] = '\0';
    int dau = 0;
    while (t[dau] != '\0' && !isalnum((unsigned char)t[dau])) dau++;
    memmove(t, t + dau, strlen(t + dau) + 1);
    for (int i = 0; t[i]; i++) t[i] = (char)tolower((unsigned char)t[i]);
}

int soSanhTu(const void *a, const void *b) {
    const TanSuat *x = a, *y = b;
    if (x->soLan != y->soLan) return y->soLan - x->soLan;
    return strcmp(x->tu, y->tu);
}

int soSanhChu(const void *a, const void *b) {
    const DemChu *x = a, *y = b;
    return y->soLan - x->soLan;
}

void inLap(char c, int n) { for (int i = 0; i < n; i++) putchar(c); }

int main(void) {
    printf("Nhap van ban (dong trong de ket thuc):\n");

    static char vanBan[20000];          // static: tranh mang lon tren stack
    char dong[1000];
    int soDong = 0;
    vanBan[0] = '\0';
    while (fgets(dong, sizeof dong, stdin) != NULL && dong[0] != '\n') {
        if (strlen(vanBan) + strlen(dong) + 1 >= sizeof vanBan) break;
        strcat(vanBan, dong);           // dong con '\n' -> ngan cach cac dong
        soDong++;
    }

    if (vanBan[0] == '\0') { printf("Khong co du lieu!\n"); return 1; }

    // ===== THONG KE KY TU =====
    int demChu[26] = {0};
    int tongKyTu = 0, chuCai = 0, chuSo = 0, khoangTrang = 0, dacBiet = 0;

    for (int i = 0; vanBan[i] != '\0'; i++) {
        unsigned char c = (unsigned char)vanBan[i];
        tongKyTu++;
        if      (isalpha(c)) { chuCai++; demChu[tolower(c) - 'a']++; }
        else if (isdigit(c)) chuSo++;
        else if (isspace(c)) khoangTrang++;
        else                 dacBiet++;
    }

    // ===== THONG KE TU (strtok sua vanBan, nen lam SAU khi dem ky tu) =====
    static TanSuat dsTu[MAX_TU];
    int soTuKhac = 0, soTu = 0;
    long long tongDoDaiTu = 0;
    char tuDaiNhat[50] = "";

    for (char *t = strtok(vanBan, " \t\n"); t != NULL; t = strtok(NULL, " \t\n")) {
        chuanHoaTu(t);
        size_t len = strlen(t);
        if (len == 0 || len >= 50) continue;

        soTu++;
        tongDoDaiTu += (long long)len;
        if (len > strlen(tuDaiNhat)) strcpy(tuDaiNhat, t);

        int vt = -1;
        for (int i = 0; i < soTuKhac; i++)
            if (strcmp(dsTu[i].tu, t) == 0) { vt = i; break; }
        if (vt >= 0) dsTu[vt].soLan++;
        else if (soTuKhac < MAX_TU) {
            strcpy(dsTu[soTuKhac].tu, t);
            dsTu[soTuKhac].soLan = 1;
            soTuKhac++;
        }
    }

    // ===== IN BAO CAO =====
    printf("\n"); inLap('=', 50); printf("\n");
    printf("           BAO CAO PHAN TICH VAN BAN\n");
    inLap('=', 50); printf("\n");

    printf("\n--- THONG KE CHUNG ---\n");
    printf("%-28s: %d\n", "So dong",          soDong);
    printf("%-28s: %d\n", "Tong ky tu",       tongKyTu);
    printf("%-28s: %d\n", "  Chu cai",        chuCai);
    printf("%-28s: %d\n", "  Chu so",         chuSo);
    printf("%-28s: %d\n", "  Khoang trang",   khoangTrang);
    printf("%-28s: %d\n", "  Ky tu dac biet", dacBiet);
    printf("%-28s: %d\n", "So tu",            soTu);
    printf("%-28s: %d\n", "So tu khac nhau",  soTuKhac);
    if (soTu > 0)
        printf("%-28s: %.2f ky tu\n", "Do dai tu trung binh", (double)tongDoDaiTu / soTu);
    printf("%-28s: %s (%zu ky tu)\n", "Tu dai nhat", tuDaiNhat, strlen(tuDaiNhat));

    // ===== TOP 5 TU =====
    qsort(dsTu, soTuKhac, sizeof(TanSuat), soSanhTu);
    printf("\n--- TOP 5 TU PHO BIEN NHAT ---\n");
    for (int i = 0; i < soTuKhac && i < 5; i++)
        printf("  %d. %-20s : %d lan\n", i + 1, dsTu[i].tu, dsTu[i].soLan);

    // ===== TOP 5 CHU CAI =====
    DemChu dsChu[26];
    int nChu = 0;
    for (int i = 0; i < 26; i++)
        if (demChu[i] > 0) {
            dsChu[nChu].chu = (char)('a' + i);
            dsChu[nChu].soLan = demChu[i];
            nChu++;
        }
    qsort(dsChu, nChu, sizeof(DemChu), soSanhChu);

    printf("\n--- TOP 5 CHU CAI PHO BIEN NHAT ---\n");
    int maxChu = (nChu == 0) ? 1 : dsChu[0].soLan;
    for (int i = 0; i < nChu && i < 5; i++) {
        int doDai = dsChu[i].soLan * 30 / maxChu;
        if (doDai < 1) doDai = 1;
        printf("  '%c' ", dsChu[i].chu);
        inLap('*', doDai);
        printf(" %d\n", dsChu[i].soLan);
    }

    printf("\n"); inLap('=', 50); printf("\n");
    return 0;
}
```

Ví dụ với 3 dòng input:

```
Lap trinh C rat hay, hoc lap trinh C giup tu duy tot.
Nam 2026 minh hoc programming bang ngon ngu C!
Lap trinh that thu vi.
```

Output:

```
==================================================
           BAO CAO PHAN TICH VAN BAN
==================================================

--- THONG KE CHUNG ---
So dong                     : 3
Tong ky tu                  : 124
  Chu cai                   : 89
  Chu so                    : 4
  Khoang trang              : 27
  Ky tu dac biet            : 4
So tu                       : 27
So tu khac nhau             : 20
Do dai tu trung binh        : 3.44 ky tu
Tu dai nhat                 : programming (11 ky tu)

--- TOP 5 TU PHO BIEN NHAT ---
  1. c                    : 3 lan
  2. lap                  : 3 lan
  3. trinh                : 3 lan
  4. hoc                  : 2 lan
  5. 2026                 : 1 lan

--- TOP 5 CHU CAI PHO BIEN NHAT ---
  'n' ****************************** 10
  't' ****************************** 10
  'a' *************************** 9
  'h' *************************** 9
  'i' ********************* 7

==================================================
```

⚠️ **Thứ tự xử lý quan trọng:** `strtok` chèn `'\0'` vào `vanBan`, nên phải thống kê ký tự **trước** khi tách từ.

💡 Mảng lớn (`vanBan`, `dsTu`) được khai báo `static` để nằm ở vùng nhớ tĩnh thay vì stack, tránh tràn stack.
