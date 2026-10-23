# Lời giải — [C]. Các Hàm Xử Lý Chuỗi Trong string.h

[← Quay lại bài học](../09-03-c-cac-ham-xu-ly-chuoi-trong-stringh.md)

> **Quy ước quan trọng:** các hàm tìm kiếm `strchr`, `strrchr`, `strstr`, `strpbrk` trả về **`NULL`** khi **không tìm thấy** — luôn phải kiểm tra trước khi dùng con trỏ kết quả. Chỉ số = `con_tro - dau_xau`.

---

### Bài 1.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[50] = "codelab dev";

    printf("Chuoi    : \"%s\"\n", s);
    printf("strlen() : %zu\n", strlen(s));          // 11
    printf("sizeof   : %zu\n", sizeof(s));          // 50 (ca mang)
    printf("rong?    : %s\n", s[0] == '\0' ? "true" : "false");   // false

    s[0] = '\0';                                    // "xoa" xau

    printf("\nSau s[0] = '\\0':\n");
    printf("Chuoi    : \"%s\"\n", s);
    printf("strlen() : %zu\n", strlen(s));          // 0
    printf("rong?    : %s\n", s[0] == '\0' ? "true" : "false");   // true

    return 0;
}
```

💡 Kiểm tra rỗng bằng `s[0] == '\0'` thay vì `strlen(s) == 0` — rõ nghĩa và **O(1)**, còn `strlen` phải đếm cả xâu.

⚠️ **`sizeof` khác `strlen`:** `sizeof(s)` là kích thước **mảng** (50), `strlen(s)` là số ký tự **thực tế** trước `'\0'`. Nếu `s` là **con trỏ** (`char *s`) thì `sizeof(s)` chỉ là kích thước con trỏ (thường 8).

### Bài 2.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *s = "Lap trinh C rat thu vi, C manh me";
    const char *canTim = "C ";

    const char *p = strstr(s, canTim);

    if (p != NULL) {
        printf("Tim thay \"%s\" tai vi tri %d\n", canTim, (int)(p - s));
        printf("Doan quanh: \"%.20s\"\n", p);     // in toi da 20 ky tu
    } else {
        printf("Khong tim thay!\n");
    }

    // Tim tu vi tri chi dinh: tim tiep tu p + 1
    if (p != NULL) {
        const char *p2 = strstr(p + 1, canTim);
        if (p2 != NULL)
            printf("Lan xuat hien thu 2 tai vi tri %d\n", (int)(p2 - s));
    }

    // Tim chuoi khong ton tai
    if (strstr(s, "Python") == NULL)
        printf("Khong tim thay \"Python\"\n");
    return 0;
}
```

💡 Đặc tả `%.20s` in **tối đa 20 ký tự** của xâu — cách gọn để in một đoạn con mà không cần sao chép.

⚠️ **Không được dùng con trỏ `NULL`**. Đừng bao giờ viết:

```c
printf("%d", (int)(strstr(s, "x") - s));   // SAI neu khong tim thay: NULL - s
char *p = strstr(s, "x");
if (p != NULL) printf("%d", (int)(p - s)); // DUNG
```

### Bài 3.

```c
#include <stdio.h>
#include <string.h>

int demSoLan(const char *s, const char *can) {
    size_t lenCan = strlen(can);
    if (lenCan == 0) return 0;

    int dem = 0;
    const char *p = s;
    while ((p = strstr(p, can)) != NULL) {
        dem++;
        p += lenCan;                 // nhay qua doan vua tim thay
    }
    return dem;
}

int main(void) {
    const char *s = "aaa bbb aaa ccc aaa";

    printf("\"aaa\" xuat hien %d lan\n", demSoLan(s, "aaa"));   // 3
    printf("\"a\"   xuat hien %d lan\n", demSoLan(s, "a"));     // 9
    printf("\"xyz\" xuat hien %d lan\n", demSoLan(s, "xyz"));   // 0

    // Dem CHONG LAP (vd "aa" trong "aaa" -> 2 lan)
    printf("\n--- Dem chong lap ---\n");
    int demCL = 0;
    const char *p = s;
    while ((p = strstr(p, "aa")) != NULL) { demCL++; p++; }    // chi +1
    printf("\"aa\" (chong lap) xuat hien %d lan\n", demCL);
    return 0;
}
```

💡 **Điểm mấu chốt — `p += lenCan` hay `p++`:**
- `p += lenCan` → **không chồng lấp**: `"aa"` trong `"aaa"` đếm được **1**
- `p++` → **có chồng lấp**: `"aa"` trong `"aaa"` đếm được **2**

Chọn cách nào tuỳ yêu cầu bài toán.

### Bài 4.

```c
#include <stdio.h>
#include <string.h>

// Luu cac vi tri vao mang viTri, tra ve so vi tri tim duoc
int timTatCa(const char *s, char c, int viTri[], int toiDa) {
    int dem = 0;
    for (int i = 0; s[i] != '\0' && dem < toiDa; i++)
        if (s[i] == c) viTri[dem++] = i;
    return dem;
}

int main(void) {
    const char *s = "codelab.dev/c/co-ban";
    char c = '/';

    int ds[100];
    int n = timTatCa(s, c, ds, 100);

    printf("Chuoi: %s\n", s);
    printf("Ky tu '%c' xuat hien %d lan tai: ", c, n);
    for (int i = 0; i < n; i++) printf("%d ", ds[i]);
    printf("\n");

    // Cach dung strchr
    printf("Dung strchr: ");
    const char *p = strchr(s, c);
    while (p != NULL) {
        printf("%d ", (int)(p - s));
        p = strchr(p + 1, c);
    }
    printf("\n");
    return 0;
}
```

Output:

```
Chuoi: codelab.dev/c/co-ban
Ky tu '/' xuat hien 2 lan tai: 11 13 
Dung strchr: 11 13 
```

💡 C không có mảng động tự lớn lên, nên hàm nhận thêm tham số `toiDa` để **không ghi vượt** mảng kết quả.

### Bài 5.

```c
#include <stdio.h>
#include <string.h>

// Thay n ky tu tai vi tri pos bang xau moi (s phai du cho)
void thayDoan(char *s, size_t pos, size_t n, const char *moi) {
    size_t len = strlen(s), lenMoi = strlen(moi);
    if (pos > len) return;
    if (pos + n > len) n = len - pos;
    // doi phan phia sau (ca '\0') toi dung cho
    memmove(s + pos + lenMoi, s + pos + n, len - pos - n + 1);
    memcpy(s + pos, moi, lenMoi);
}

// Thay the TAT CA cac lan xuat hien, ghi ket qua vao kq (kich thuoc size)
void thayTatCa(const char *s, const char *cu, const char *moi,
               char *kq, size_t size) {
    size_t lenCu = strlen(cu);
    kq[0] = '\0';
    if (lenCu == 0) { strncat(kq, s, size - 1); return; }

    const char *p = s, *q;
    while ((q = strstr(p, cu)) != NULL) {
        size_t conLai = size - 1 - strlen(kq);   // so cho con trong
        size_t n = (size_t)(q - p);              // doan truoc chu cu
        strncat(kq, p, n < conLai ? n : conLai);
        strncat(kq, moi, size - 1 - strlen(kq));
        p = q + lenCu;                 // nhay qua phan CU, tranh lap vo han
    }
    strncat(kq, p, size - 1 - strlen(kq));
}

int main(void) {
    const char *s = "Toi hoc Java, Java rat hay, Java manh me";
    char kq[200];

    // (1) thay mot lan tai vi tri cu the
    char s1[200];
    strcpy(s1, s);
    thayDoan(s1, 8, 4, "C");              // tu vi tri 8, thay 4 ky tu
    printf("Thay 1 lan    : %s\n", s1);

    // (2) Thay the tat ca
    thayTatCa(s, "Java", "C", kq, sizeof(kq));
    printf("Thay tat ca   : %s\n", kq);

    // (3) Truong hop nguy hiem: thay "a" bang "aa"
    thayTatCa("abc", "a", "aa", kq, sizeof(kq));
    printf("a -> aa       : %s\n", kq);   // aabc
    return 0;
}
```

Output:

```
Thay 1 lan    : Toi hoc C, Java rat hay, Java manh me
Thay tat ca   : Toi hoc C, C rat hay, C manh me
a -> aa       : aabc
```

⚠️ **Tìm tiếp trong xâu GỐC, bắt đầu sau phần cũ (`p = q + lenCu`) là điểm quan trọng.** Nếu thay trực tiếp trên cùng một xâu rồi tìm lại từ đầu, khi thay `"a"` bằng `"aa"` chương trình sẽ **lặp vô hạn** (liên tục tìm thấy `"a"` trong phần vừa thay).

💡 Ghi kết quả sang một mảng `kq` riêng, mỗi lần nối đều giới hạn bằng `size - 1 - strlen(kq)` nên **không bao giờ tràn** mảng kết quả.

### Bài 6.

```c
#include <stdio.h>
#include <string.h>

// Chen xau t vao vi tri viTri cua s (s phai du cho)
void chenXau(char *s, size_t viTri, const char *t) {
    size_t len = strlen(s), lenT = strlen(t);
    if (viTri > len) viTri = len;
    memmove(s + viTri + lenT, s + viTri, len - viTri + 1);   // ca '\0'
    memcpy(s + viTri, t, lenT);
}

int main(void) {
    const char *s = "Lap trinh";
    char a[100], b[100], c[100], d[100];

    strcpy(a, s);
    chenXau(a, 0, ">>> ");                // chen vao DAU
    printf("Chen dau  : %s\n", a);

    strcpy(b, s);
    chenXau(b, strlen(b), " C");          // chen vao CUOI
    printf("Chen cuoi : %s\n", b);

    strcpy(c, s);
    chenXau(c, 4, "hoc ");                // chen vao GIUA (vi tri 4)
    printf("Chen giua : %s\n", c);

    strcpy(d, s);
    char sao[6];
    memset(sao, '*', 5);                  // tao xau 5 ky tu '*'
    sao[5] = '\0';
    chenXau(d, 3, sao);                   // chen 5 ky tu '*' tai vi tri 3
    printf("Chen ky tu: %s\n", d);

    return 0;
}
```

Output:

```
Chen dau  : >>> Lap trinh
Chen cuoi : Lap trinh C
Chen giua : Lap hoc trinh
Chen ky tu: Lap***** trinh
```

💡 Chèn vào cuối thì dùng `strcat(b, " C")` gọn hơn.

⚠️ **Phải dùng `memmove`, không dùng `memcpy`** để dịch phần sau, vì vùng nguồn và vùng đích **chồng lên nhau**.

### Bài 7.

```c
#include <stdio.h>
#include <string.h>

// Xoa n ky tu tu vi tri viTri
void xoaDoan(char *s, size_t viTri, size_t n) {
    size_t len = strlen(s);
    if (viTri >= len) return;
    if (viTri + n > len) n = len - viTri;
    memmove(s + viTri, s + viTri + n, len - viTri - n + 1);   // ca '\0'
}

int main(void) {
    const char *goc = "Lap trinh C co ban";
    char a[100], b[100], c[100], d[100], e[100];

    strcpy(a, goc);
    xoaDoan(a, 4, 6);                    // tu vi tri 4, xoa 6 ky tu
    printf("xoaDoan(4, 6) : %s\n", a);

    strcpy(b, goc);
    xoaDoan(b, 0, 1);                    // xoa 1 ky tu dau
    printf("Xoa 1 ky tu   : %s\n", b);

    strcpy(c, goc);
    c[10] = '\0';                        // tu vi tri 10 den HET
    printf("Cat tu 10     : %s\n", c);

    strcpy(d, goc);
    xoaDoan(d, 3, 1);                    // xoa ky tu tai vi tri 3
    printf("Xoa vi tri 3  : %s\n", d);

    strcpy(e, goc);
    e[0] = '\0';                         // xoa TAT CA
    printf("Xoa het       : [%s]\n", e);
    return 0;
}
```

Output:

```
xoaDoan(4, 6) : Lap C co ban
Xoa 1 ky tu   : ap trinh C co ban
Cat tu 10     : Lap trinh 
Xoa vi tri 3  : Laptrinh C co ban
Xoa het       : []
```

💡 **Xoá từ vị trí `k` tới hết** chỉ cần đặt `s[k] = '\0'` — không phải dịch chuyển gì cả, **O(1)**.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char hoTen[100];
    printf("Nhap ho ten day du: ");
    if (fgets(hoTen, sizeof(hoTen), stdin) == NULL) return 1;
    hoTen[strcspn(hoTen, "\n")] = '\0';

    if (hoTen[0] == '\0') {
        printf("Chuoi rong!\n");
        return 1;
    }

    char *dauCach1 = strchr(hoTen, ' ');     // dau cach DAU TIEN
    char *dauCachN = strrchr(hoTen, ' ');    // dau cach CUOI CUNG

    printf("\n--- PHAN TICH ---\n");
    if (dauCach1 == NULL) {                  // chi co 1 tu
        printf("Ten      : %s\n", hoTen);
        return 0;
    }

    char ho[100], ten[100], dem[100];

    size_t lenHo = dauCach1 - hoTen;
    strncpy(ho, hoTen, lenHo);
    ho[lenHo] = '\0';

    strcpy(ten, dauCachN + 1);

    if (dauCach1 == dauCachN) {
        strcpy(dem, "(khong co)");
    } else {
        size_t lenDem = dauCachN - dauCach1 - 1;
        strncpy(dem, dauCach1 + 1, lenDem);
        dem[lenDem] = '\0';
    }

    printf("Ho       : %s\n", ho);
    printf("Ten      : %s\n", ten);
    printf("Ten dem  : %s\n", dem);
    return 0;
}
```

Với input `Nguyen Van Minh Anh`:

```
Ho       : Nguyen
Ten      : Anh
Ten dem  : Van Minh
```

⚠️ Sau `strncpy(dich, nguon, n)` với `n` nhỏ hơn độ dài nguồn, **phải tự thêm `'\0'`** — `strncpy` không làm việc đó.

💡 Bài này giả sử các từ cách nhau đúng một dấu cách. Chuẩn hoá xâu trước (xoá khoảng trắng thừa) được bàn ở bài [09-09 — Chuẩn hoá tên và email](../09-09-c-chuan-hoa-ten-va-email.md).

### Bài 9.

```c
#include <stdio.h>
#include <string.h>

// Tra ve con tro toi phan ten file trong duong dan
const char *layTenFile(const char *duongDan) {
    const char *p1 = strrchr(duongDan, '/');
    const char *p2 = strrchr(duongDan, '\\');   // ho tro ca / va \ .
    const char *p;                              // dau phan cach cuoi cung
    if (p1 == NULL) p = p2;
    else if (p2 == NULL) p = p1;
    else p = (p1 > p2) ? p1 : p2;
    return p ? p + 1 : duongDan;
}

// Tra ve con tro toi phan duoi ("" neu khong co)
const char *layPhanMoRong(const char *tenFile) {
    const char *p = strrchr(tenFile, '.');
    if (p == NULL || p == tenFile) return "";   // khong co duoi / file an .gitignore
    return p + 1;
}

// Ghi ten khong duoi vao kq
void layTenKhongDuoi(const char *tenFile, char *kq) {
    const char *p = strrchr(tenFile, '.');
    if (p == NULL || p == tenFile) { strcpy(kq, tenFile); return; }
    size_t n = p - tenFile;
    strncpy(kq, tenFile, n);
    kq[n] = '\0';
}

int main(void) {
    const char *ds[] = {
        "baitap.c",
        "/home/user/docs/bao-cao.final.pdf",
        "C:\\Users\\Admin\\anh.png",
        "README",
        ".gitignore"
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    for (int i = 0; i < n; i++) {
        const char *ten = layTenFile(ds[i]);
        char khongDuoi[100];
        layTenKhongDuoi(ten, khongDuoi);
        printf("Duong dan : %s\n", ds[i]);
        printf("  Ten file: %s\n", ten);
        printf("  Ten     : %s\n", khongDuoi);
        printf("  Duoi    : %s\n\n", layPhanMoRong(ten));
    }
    return 0;
}
```

**`strchr` vs `strrchr`:**

| | `strchr` | `strrchr` |
|---|---|---|
| Tìm từ | Trái sang phải | **Phải sang trái** |
| Trả về | Con trỏ tới vị trí **đầu tiên** | Con trỏ tới vị trí **cuối cùng** |

⚠️ Với `bao-cao.final.pdf`, phải dùng `strrchr(s, '.')` để lấy `pdf`. Nếu dùng `strchr(s, '.')` sẽ ra `final.pdf`.

💡 Chỉ so sánh `p1 > p2` khi **cả hai khác `NULL`** — lúc đó chúng cùng trỏ vào một xâu nên phép so sánh con trỏ mới có nghĩa.

### Bài 10.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    const char *s = "  codelab-dev_2026!  ";

    printf("Chuoi: [%s]\n", s);

    // strstr(chuoi) - tim CA CUM
    printf("\nstrstr(\"dev\")         = %d\n", (int)(strstr(s, "dev") - s));

    // strpbrk(tap) - tim ky tu DAU TIEN thuoc tap
    printf("strpbrk(\"-_\")         = %d\n", (int)(strpbrk(s, "-_") - s));

    // strcspn(tap) - DO DAI doan dau KHONG chua ky tu nao cua tap
    printf("strcspn(\"-_\")         = %zu\n", strcspn(s, "-_"));

    // strspn(tap) - DO DAI doan dau CHI gom ky tu thuoc tap
    printf("strspn(\" \")           = %zu\n", strspn(s, " "));

    // Ung dung: trim bang strspn + duyet nguoc
    const char *dau = s + strspn(s, " \t\n");
    size_t len = strlen(dau);
    while (len > 0 && strchr(" \t\n", dau[len - 1]) != NULL) len--;
    printf("\nSau trim: [%.*s]\n", (int)len, dau);
    return 0;
}
```

Output:

```
Chuoi: [  codelab-dev_2026!  ]

strstr("dev")         = 10
strpbrk("-_")         = 9
strcspn("-_")         = 9
strspn(" ")           = 2

Sau trim: [codelab-dev_2026!]
```

**Bảng phân biệt:**

| Hàm | Tìm gì | Trả về | Ví dụ với `"abc123"` |
|---|---|---|---|
| `strstr(s, "bc")` | **Cả cụm** `"bc"` | Con trỏ / `NULL` | vị trí 1 |
| `strchr(s, '2')` | Đúng **một** ký tự | Con trỏ / `NULL` | vị trí 4 |
| `strpbrk(s, "321")` | Ký tự đầu tiên thuộc `{3,2,1}` | Con trỏ / `NULL` | vị trí 3 (ký tự `'1'`) |
| `strcspn(s, "321")` | Độ dài đoạn đầu **không** có ký tự thuộc tập | `size_t` | 3 |
| `strspn(s, "abc")` | Độ dài đoạn đầu **chỉ** gồm ký tự thuộc tập | `size_t` | 3 |

⚠️ **Nhầm lẫn phổ biến:** `strstr(s, "abc")` tìm **chuỗi con** `"abc"`, còn `strpbrk(s, "abc")` tìm **bất kỳ ký tự nào** trong `{a, b, c}`.

💡 `strcspn` và `strspn` **không bao giờ trả `NULL`**: nếu không gặp ký tự cần tìm, `strcspn` trả về `strlen(s)`. Đó là lý do `s[strcspn(s, "\n")] = '\0'` luôn an toàn.

💡 `%.*s` nhận độ dài từ tham số `int` đứng trước — in đúng `len` ký tự mà không cần sửa xâu gốc.

### Bài 11.

```c
#include <stdio.h>
#include <string.h>

#define MAX_PHAN 20
#define MAX_DAI  50

// Tach theo mot KY TU phan cach, GIU phan rong. Tra ve so phan.
int split(const char *s, char phanCach, char kq[][MAX_DAI], int toiDa) {
    int dem = 0;
    const char *dau = s;
    while (dem < toiDa) {
        const char *cuoi = strchr(dau, phanCach);
        size_t n = cuoi ? (size_t)(cuoi - dau) : strlen(dau);
        if (n >= MAX_DAI) n = MAX_DAI - 1;       // cat bot neu qua dai
        memcpy(kq[dem], dau, n);
        kq[dem][n] = '\0';
        dem++;
        if (cuoi == NULL) break;
        dau = cuoi + 1;
    }
    return dem;
}

// Tach theo khoang trang (bo qua nhieu dau cach lien tiep)
int splitTrang(const char *s, char kq[][MAX_DAI], int toiDa) {
    int dem = 0;
    const char *p = s;
    while (dem < toiDa) {
        p += strspn(p, " \t");                   // bo khoang trang
        if (*p == '\0') break;
        size_t n = strcspn(p, " \t");            // do dai tu
        size_t m = n < MAX_DAI ? n : MAX_DAI - 1;
        memcpy(kq[dem], p, m);
        kq[dem][m] = '\0';
        dem++;
        p += n;
    }
    return dem;
}

void in(const char *nhan, char v[][MAX_DAI], int n) {
    printf("%s (%d phan): ", nhan, n);
    for (int i = 0; i < n; i++) printf("[%s] ", v[i]);
    printf("\n");
}

int main(void) {
    char kq[MAX_PHAN][MAX_DAI];
    int n;

    n = split("An,Binh,Chi,Dung", ',', kq, MAX_PHAN);  in("split(',')    ", kq, n);
    n = split("2026-09-17", '-', kq, MAX_PHAN);        in("split('-')    ", kq, n);
    n = splitTrang("  nhieu    dau    cach  ", kq, MAX_PHAN);
    in("splitTrang    ", kq, n);
    n = split("a,,b,", ',', kq, MAX_PHAN);             in("Co phan rong  ", kq, n);
    return 0;
}
```

Output:

```
split(',')     (4 phan): [An] [Binh] [Chi] [Dung] 
split('-')     (3 phan): [2026] [09] [17] 
splitTrang     (3 phan): [nhieu] [dau] [cach] 
Co phan rong   (4 phan): [a] [] [b] [] 
```

💡 **Khác biệt quan trọng:** `split` **giữ lại phần rỗng** (`"a,,b,"` → 4 phần), còn `splitTrang` **bỏ qua** khoảng trắng liên tiếp. Chọn cách phù hợp với bài toán.

💡 Thư viện chuẩn có hàm `strtok` để tách xâu, nhưng nó **sửa xâu gốc** và **bỏ qua phần rỗng**. Xem bài [09-07 — Tách chuỗi với strtok và sscanf](../09-07-c-tach-chuoi-voi-strtok-va-sscanf.md).

### Bài 12.

```c
#include <stdio.h>
#include <string.h>

// Noi n xau voi dau phan cach, ghi vao kq (kich thuoc size)
void join(const char *v[], int n, const char *phanCach, char *kq, size_t size) {
    kq[0] = '\0';
    if (n == 0) return;

    strncat(kq, v[0], size - 1);
    for (int i = 1; i < n; i++) {
        strncat(kq, phanCach, size - 1 - strlen(kq));
        strncat(kq, v[i], size - 1 - strlen(kq));
    }
}

int main(void) {
    const char *v[] = {"C", "Python", "Java", "Go"};
    int n = 4;
    char kq[200];

    join(v, n, ", ", kq, sizeof(kq));   printf("join(\", \")  : %s\n", kq);
    join(v, n, " | ", kq, sizeof(kq));  printf("join(\" | \") : %s\n", kq);
    join(v, n, "", kq, sizeof(kq));     printf("join(\"\")    : %s\n", kq);
    join(v, n, " -> ", kq, sizeof(kq)); printf("join(\"->\")  : %s\n", kq);

    join(v, 0, ",", kq, sizeof(kq));    printf("Mang rong    : [%s]\n", kq);
    return 0;
}
```

Output:

```
join(", ")  : C, Python, Java, Go
join(" | ") : C | Python | Java | Go
join("")    : CPythonJavaGo
join("->")  : C -> Python -> Java -> Go
Mang rong    : []
```

💡 **Mẹo tránh dấu phân cách thừa:** thêm phần tử **đầu tiên** trước vòng lặp, rồi từ phần tử thứ 2 mới thêm dấu phân cách trước. Cách này gọn hơn việc xoá dấu thừa ở cuối.

⚠️ `strncat(dich, nguon, n)` nối **tối đa n ký tự** và luôn thêm `'\0'`, nên `n` phải là **số chỗ còn trống** `size - 1 - strlen(dich)`, không phải `size`.

### Bài 13.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char a[] = "apple", b[] = "banana", c[] = "apple";

    printf("--- strcmp() ---\n");
    printf("strcmp(a, b) < 0 : %d\n", strcmp(a, b) < 0);   // 1 (a < b)
    printf("strcmp(b, a) > 0 : %d\n", strcmp(b, a) > 0);   // 1
    printf("strcmp(a, c)     : %d\n", strcmp(a, c));       // 0

    printf("\n--- Toan tu == so sanh DIA CHI ---\n");
    printf("a == c           : %d\n", a == c);             // 0 (2 mang khac nhau)
    printf("strcmp(a,c) == 0 : %d\n", strcmp(a, c) == 0);  // 1

    // so sanh mot PHAN chuoi
    const char *s = "Lap trinh C";
    printf("\n--- strncmp mot phan ---\n");
    printf("strncmp(s, \"Lap\", 3)      = %d\n", strncmp(s, "Lap", 3));      // 0
    printf("strncmp(s + 10, \"C\", 1)   = %d\n", strncmp(s + 10, "C", 1));   // 0
    return 0;
}
```

**`strcmp()` trả về:**

| Giá trị | Ý nghĩa |
|---|---|
| `0` | Hai chuỗi **bằng nhau** |
| `< 0` | Chuỗi thứ nhất **nhỏ hơn** (đứng trước theo từ điển) |
| `> 0` | Chuỗi thứ nhất **lớn hơn** |

⚠️ Chuẩn C **chỉ đảm bảo dấu** (âm / 0 / dương), không đảm bảo giá trị cụ thể. Viết `strcmp(a, b) < 0`, **đừng** viết `strcmp(a, b) == -1`.

⚠️ **Trong C không dùng được `==`, `<`, `>` để so sánh nội dung xâu.** Tên mảng chuyển thành **địa chỉ** phần tử đầu, nên `a == c` chỉ hỏi "hai mảng có cùng địa chỉ không" — luôn sai với hai mảng khác nhau dù nội dung giống hệt.

`strncmp()` hữu ích khi:
- So sánh **một phần** chuỗi: `strncmp(s + pos, other, len)`
- Kiểm tra tiền tố (bài 14)

### Bài 14.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool batDauBang(const char *s, const char *tienTo) {
    return strncmp(s, tienTo, strlen(tienTo)) == 0;
}

bool ketThucBang(const char *s, const char *hauTo) {
    size_t ls = strlen(s), lh = strlen(hauTo);
    if (lh > ls) return false;
    return strcmp(s + ls - lh, hauTo) == 0;
}

bool chua(const char *s, const char *can) {
    return strstr(s, can) != NULL;
}

int main(void) {
    const char *s = "baitap01.c";

    printf("Bat dau bang \"bai\"  : %d\n", batDauBang(s, "bai"));   // 1
    printf("Bat dau bang \"tap\"  : %d\n", batDauBang(s, "tap"));   // 0
    printf("Ket thuc bang \".c\"  : %d\n", ketThucBang(s, ".c"));   // 1
    printf("Ket thuc bang \".py\" : %d\n", ketThucBang(s, ".py"));  // 0
    printf("Chua \"tap0\"         : %d\n", chua(s, "tap0"));        // 1

    // Ung dung: loc file theo duoi
    const char *ds[] = {"a.c", "b.py", "c.c", "d.txt"};
    printf("\nCac file .c: ");
    for (int i = 0; i < 4; i++)
        if (ketThucBang(ds[i], ".c")) printf("%s ", ds[i]);
    printf("\n");
    return 0;
}
```

💡 `batDauBang` không cần kiểm tra độ dài: nếu `s` ngắn hơn `tienTo`, `strncmp` sẽ gặp `'\0'` của `s` trước và trả về khác 0.

💡 `bool` trong C cần `#include <stdbool.h>`; khi in bằng `%d`, `true` là `1` và `false` là `0`.

### Bài 15.

**File `chuoi.h`:**

```c
// FILE: chuoi.h
#ifndef CHUOI_H
#define CHUOI_H

#include <stdbool.h>
#include <stddef.h>

#define CHUOI_MAX_DAI 50

/** @brief Cat khoang trang o dau va cuoi chuoi (sua truc tiep s). */
void trim(char *s);

/** @brief Cat khoang trang o dau chuoi. */
void trimTrai(char *s);

/** @brief Cat khoang trang o cuoi chuoi. */
void trimPhai(char *s);

/** @brief Tach chuoi theo mot ky tu phan cach, tra ve so phan. */
int split(const char *s, char phanCach, char kq[][CHUOI_MAX_DAI], int toiDa);

/** @brief Noi n phan tu thanh mot chuoi voi dau phan cach. */
void join(const char *v[], int n, const char *phanCach, char *kq, size_t size);

/** @brief Thay the TAT CA cac lan xuat hien cua cu bang moi, ghi vao kq. */
void replaceAll(const char *s, const char *cu, const char *moi,
                char *kq, size_t size);

/** @brief Chuyen toan bo chuoi sang chu HOA (sua truc tiep s). */
void toUpper(char *s);

/** @brief Chuyen toan bo chuoi sang chu thuong (sua truc tiep s). */
void toLower(char *s);

/** @brief Kiem tra chuoi co bat dau bang tien to cho truoc. */
bool startsWith(const char *s, const char *tienTo);

/** @brief Kiem tra chuoi co ket thuc bang hau to cho truoc. */
bool endsWith(const char *s, const char *hauTo);

/** @brief Kiem tra chuoi co chua chuoi con cho truoc. */
bool contains(const char *s, const char *can);

/** @brief Dem so lan xuat hien cua chuoi con (khong chong lap). */
int countOccurrences(const char *s, const char *can);

/** @brief Dao nguoc chuoi (sua truc tiep s). */
void reverseStr(char *s);

#endif
```

**File `chuoi.c`:**

```c
// FILE: chuoi.c
#include "chuoi.h"
#include <string.h>
#include <ctype.h>

static const char KHOANG_TRANG[] = " \t\n\r\f\v";

void trimTrai(char *s) {
    size_t dau = strspn(s, KHOANG_TRANG);
    memmove(s, s + dau, strlen(s + dau) + 1);
}

void trimPhai(char *s) {
    size_t len = strlen(s);
    while (len > 0 && strchr(KHOANG_TRANG, s[len - 1]) != NULL) len--;
    s[len] = '\0';
}

void trim(char *s) {
    trimPhai(s);
    trimTrai(s);
}

int split(const char *s, char phanCach, char kq[][CHUOI_MAX_DAI], int toiDa) {
    int dem = 0;
    const char *dau = s;
    while (dem < toiDa) {
        const char *cuoi = strchr(dau, phanCach);
        size_t n = cuoi ? (size_t)(cuoi - dau) : strlen(dau);
        if (n >= CHUOI_MAX_DAI) n = CHUOI_MAX_DAI - 1;
        memcpy(kq[dem], dau, n);
        kq[dem][n] = '\0';
        dem++;
        if (cuoi == NULL) break;
        dau = cuoi + 1;
    }
    return dem;
}

void join(const char *v[], int n, const char *phanCach, char *kq, size_t size) {
    kq[0] = '\0';
    for (int i = 0; i < n; i++) {
        if (i > 0) strncat(kq, phanCach, size - 1 - strlen(kq));
        strncat(kq, v[i], size - 1 - strlen(kq));
    }
}

void replaceAll(const char *s, const char *cu, const char *moi,
                char *kq, size_t size) {
    size_t lenCu = strlen(cu);
    kq[0] = '\0';
    if (lenCu == 0) { strncat(kq, s, size - 1); return; }

    const char *p = s, *q;
    while ((q = strstr(p, cu)) != NULL) {
        size_t conLai = size - 1 - strlen(kq);
        size_t n = (size_t)(q - p);
        strncat(kq, p, n < conLai ? n : conLai);
        strncat(kq, moi, size - 1 - strlen(kq));
        p = q + lenCu;
    }
    strncat(kq, p, size - 1 - strlen(kq));
}

void toUpper(char *s) {
    for (; *s; s++) *s = (char)toupper((unsigned char)*s);
}

void toLower(char *s) {
    for (; *s; s++) *s = (char)tolower((unsigned char)*s);
}

bool startsWith(const char *s, const char *tienTo) {
    return strncmp(s, tienTo, strlen(tienTo)) == 0;
}

bool endsWith(const char *s, const char *hauTo) {
    size_t ls = strlen(s), lh = strlen(hauTo);
    return lh <= ls && strcmp(s + ls - lh, hauTo) == 0;
}

bool contains(const char *s, const char *can) {
    return strstr(s, can) != NULL;
}

int countOccurrences(const char *s, const char *can) {
    size_t lenCan = strlen(can);
    if (lenCan == 0) return 0;
    int dem = 0;
    while ((s = strstr(s, can)) != NULL) { dem++; s += lenCan; }
    return dem;
}

void reverseStr(char *s) {
    size_t len = strlen(s);
    if (len < 2) return;
    for (size_t i = 0, j = len - 1; i < j; i++, j--) {
        char t = s[i]; s[i] = s[j]; s[j] = t;
    }
}
```

**File `main.c` — kiểm thử:**

```c
// FILE: main.c
#include <stdio.h>
#include <string.h>
#include "chuoi.h"

int main(void) {
    char s[200];
    char kq[200];

    strcpy(s, "   codelab   ");   trim(s);
    printf("trim          : [%s]\n", s);
    strcpy(s, "Lap trinh C");     toUpper(s);
    printf("toUpper       : %s\n", s);
    strcpy(s, "LAP TRINH C");     toLower(s);
    printf("toLower       : %s\n", s);
    replaceAll("Java rat hay, Java manh", "Java", "C", kq, sizeof(kq));
    printf("replaceAll    : %s\n", kq);
    strcpy(s, "codelab");         reverseStr(s);
    printf("reverseStr    : %s\n", s);

    printf("startsWith    : %d\n", startsWith("baitap.c", "bai"));
    printf("endsWith      : %d\n", endsWith("baitap.c", ".c"));
    printf("contains      : %d\n", contains("baitap.c", "tap"));
    printf("countOccur    : %d\n", countOccurrences("aaa bbb aaa", "aaa"));

    char phan[10][CHUOI_MAX_DAI];
    int n = split("An,Binh,Chi", ',', phan, 10);
    const char *v[10];
    for (int i = 0; i < n; i++) v[i] = phan[i];
    join(v, n, " | ", kq, sizeof(kq));
    printf("split + join  : %s\n", kq);
    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall main.c chuoi.c -o chuoi
./chuoi
```

Output:

```
trim          : [codelab]
toUpper       : LAP TRINH C
toLower       : lap trinh c
replaceAll    : C rat hay, C manh
reverseStr    : baledoc
startsWith    : 1
endsWith      : 1
contains      : 1
countOccur    : 2
split + join  : An | Binh | Chi
```

💡 **Hai kiểu thiết kế hàm xâu trong C:**
- Hàm **sửa trực tiếp** xâu truyền vào (`trim`, `toUpper`, `reverseStr`) — nhận `char *s`, không cần bộ nhớ thêm, nhưng **không dùng được với xâu hằng** như `"abc"`.
- Hàm **ghi kết quả vào mảng do người gọi cấp** (`replaceAll`, `join`) — nhận thêm `kq` và `size` để không bao giờ tràn mảng. Khi kết quả có thể dài hơn đầu vào, đây là cách an toàn.

⚠️ Luôn ép kiểu `(unsigned char)` trước khi truyền ký tự cho `toupper`/`tolower`/`isspace`..., vì `char` có thể âm với ký tự ngoài bảng ASCII.
