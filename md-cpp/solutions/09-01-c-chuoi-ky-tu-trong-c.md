# Lời giải — [C]. Chuỗi Ký Tự Trong C

[← Quay lại bài học](../09-01-c-chuoi-ky-tu-trong-c.md)

> Chuỗi trong C là **mảng `char` kết thúc bằng `'\0'`**. Nhớ `#include <string.h>` khi dùng `strlen`, `strcspn`… và `#include <ctype.h>` khi dùng `isalpha`, `isdigit`, `tolower`…

---

### Bài 1.

```c
#include <stdio.h>
#include <string.h>

int main() {
    // (1) Mang rong, co kich thuoc
    char s1[50] = "";

    // (2) Khong ghi kich thuoc: trinh bien dich tu tinh = so ky tu + 1
    char s2[] = "codelab";

    // (3) Co kich thuoc lon hon noi dung
    char s3[20] = "C programming";

    // (4) Khoi tao tung ky tu, TU THEM '\0'
    char s4[] = {'C', '1', '1', '\0'};

    printf("s1 = \"%s\"  strlen = %zu  sizeof = %zu\n", s1, strlen(s1), sizeof(s1));
    printf("s2 = \"%s\"  strlen = %zu  sizeof = %zu\n", s2, strlen(s2), sizeof(s2));
    printf("s3 = \"%s\"  strlen = %zu  sizeof = %zu\n", s3, strlen(s3), sizeof(s3));
    printf("s4 = \"%s\"  strlen = %zu  sizeof = %zu\n", s4, strlen(s4), sizeof(s4));
    return 0;
}
```

Output:

```
s1 = ""  strlen = 0  sizeof = 50
s2 = "codelab"  strlen = 7  sizeof = 8
s3 = "C programming"  strlen = 13  sizeof = 20
s4 = "C11"  strlen = 3  sizeof = 4
```

💡 `strlen` = số ký tự **trước** `'\0'`; `sizeof` = số byte của **cả mảng**. Với mảng không ghi kích thước, `sizeof = strlen + 1`.

⚠️ Nếu quên `'\0'` ở cách (4), `printf("%s")` và `strlen` sẽ đọc tràn sang vùng nhớ phía sau — kết quả rác, không đoán trước được.

### Bài 2.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char hoTen[100];

    printf("Nhap ho ten day du: ");
    if (fgets(hoTen, sizeof(hoTen), stdin) == NULL) return 0;

    hoTen[strcspn(hoTen, "\n")] = '\0';        // xoa '\n' cuoi chuoi (neu co)

    printf("Ho ten   : %s\n", hoTen);
    printf("Do dai   : %zu ky tu\n", strlen(hoTen));
    printf("Rong?    : %s\n", strlen(hoTen) == 0 ? "true" : "false");
    return 0;
}
```

Input: `Nguyen Van An` → Output:

```
Ho ten   : Nguyen Van An
Do dai   : 13 ky tu
Rong?    : false
```

⚠️ **`scanf("%s")` chỉ đọc tới khoảng trắng đầu tiên.** Muốn đọc cả dòng phải dùng `fgets`.

⚠️ `fgets` **giữ lại `'\n'`** ở cuối. Nếu không xoá, độ dài sẽ bị dư 1 và khi in sẽ xuống dòng thừa. `strcspn(s, "\n")` trả về vị trí của `'\n'` đầu tiên (hoặc `strlen(s)` nếu không có), nên dòng xoá trên an toàn trong mọi trường hợp.

### Bài 3.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[] = "codelab";

    printf("Cach 1 (chi so + strlen): ");
    int n = strlen(s);
    for (int i = 0; i < n; i++) printf("%c ", s[i]);
    printf("\n");

    printf("Cach 2 (toi '\\0')       : ");
    for (int i = 0; s[i] != '\0'; i++) printf("%c ", s[i]);
    printf("\n");

    printf("Cach 3 (con tro)        : ");
    for (const char *p = s; *p; p++) printf("%c ", *p);
    printf("\n");
    return 0;
}
```

Output:

```
Cach 1 (chi so + strlen): c o d e l a b 
Cach 2 (toi '\0')       : c o d e l a b 
Cach 3 (con tro)        : c o d e l a b 
```

| Cách | Cần biết độ dài trước? | Ghi chú |
|---|---|---|
| Chỉ số + `strlen` | ✅ Có | Tính `strlen` **một lần** trước vòng lặp |
| Chỉ số tới `'\0'` | ❌ Không | Cách tự nhiên nhất với chuỗi C |
| Con trỏ | ❌ Không | Gọn, hay gặp trong thư viện chuẩn |

⚠️ Trong chuỗi định dạng của `printf`, muốn in ra chữ `\0` phải viết `'\\0'` (dấu `\` phải nhân đôi).

### Bài 4.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[1000];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof(s), stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    int chuCai = 0, chuSo = 0, dauCach = 0, dacBiet = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        unsigned char c = (unsigned char)s[i];
        if      (isalpha(c)) chuCai++;
        else if (isdigit(c)) chuSo++;
        else if (isspace(c)) dauCach++;
        else                 dacBiet++;
    }

    printf("Chu cai       : %d\n", chuCai);
    printf("Chu so        : %d\n", chuSo);
    printf("Dau cach      : %d\n", dauCach);
    printf("Ky tu dac biet: %d\n", dacBiet);
    printf("Tong          : %zu\n", strlen(s));
    return 0;
}
```

Input: `Hello C11, 2026!` → Output:

```
Chu cai       : 6
Chu so        : 6
Dau cach      : 2
Ky tu dac biet: 2
Tong          : 16
```

💡 Ép sang `unsigned char` trước khi truyền vào `isalpha`/`isdigit` để tránh hành vi không xác định khi gặp ký tự có mã âm (ví dụ chữ có dấu tiếng Việt UTF-8).

### Bài 5.

```c
#include <stdio.h>
#include <string.h>

// Cach 1: dung chi so
int doDai1(const char s[]) {
    int n = 0;
    while (s[n] != '\0') n++;
    return n;
}

// Cach 2: dung con tro - lay hieu 2 dia chi
int doDai2(const char *s) {
    const char *p = s;
    while (*p) p++;
    return (int)(p - s);
}

int main() {
    const char *ds[] = {"", "a", "codelab", "lap trinh C co ban"};
    for (int i = 0; i < 4; i++) {
        printf("\"%s\": doDai1 = %d, doDai2 = %d, strlen = %zu\n",
               ds[i], doDai1(ds[i]), doDai2(ds[i]), strlen(ds[i]));
    }
    return 0;
}
```

Output:

```
"": doDai1 = 0, doDai2 = 0, strlen = 0
"a": doDai1 = 1, doDai2 = 1, strlen = 1
"codelab": doDai1 = 7, doDai2 = 7, strlen = 7
"lap trinh C co ban": doDai1 = 18, doDai2 = 18, strlen = 18
```

💡 Cách 2 dùng **phép trừ 2 con trỏ**: `p - s` là số phần tử nằm giữa 2 địa chỉ — chính là độ dài chuỗi.

💡 Tham số khai báo `const char` để hứa với trình biên dịch rằng hàm **không sửa** chuỗi, nhờ vậy truyền được cả hằng chuỗi.

### Bài 6.

```c
#include <stdio.h>
#include <string.h>

// Cach 1: vong lap, doi cho 2 dau
void daoNguoc1(char s[]) {
    int n = strlen(s);
    for (int i = 0; i < n / 2; i++) {
        char t = s[i];
        s[i] = s[n - 1 - i];
        s[n - 1 - i] = t;
    }
}

// Cach 2: de quy
void daoNguoc2(char s[], int trai, int phai) {
    if (trai >= phai) return;
    char t = s[trai]; s[trai] = s[phai]; s[phai] = t;
    daoNguoc2(s, trai + 1, phai - 1);
}

int main() {
    char s[] = "codelab";
    printf("Goc      : %s\n", s);

    daoNguoc1(s);
    printf("Cach 1   : %s\n", s);

    daoNguoc1(s);                      // dao lai de ve chuoi goc
    daoNguoc2(s, 0, (int)strlen(s) - 1);
    printf("Cach 2   : %s\n", s);
    return 0;
}
```

Output:

```
Goc      : codelab
Cach 1   : baledoc
Cach 2   : baledoc
```

💡 Hàm nhận mảng `char s[]` thực chất nhận **con trỏ** tới chuỗi gốc, nên đảo ngược **tại chỗ** — chuỗi ở `main` thay đổi theo.

⚠️ Không được gọi `daoNguoc1("codelab")` trực tiếp với hằng chuỗi — hằng chuỗi nằm ở vùng nhớ chỉ đọc, sửa vào sẽ crash. Phải chép vào mảng `char s[]` trước.

### Bài 7.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

bool laDoiXung(const char *s) {
    int trai = 0, phai = (int)strlen(s) - 1;

    while (trai < phai) {
        // Bo qua ky tu khong phai chu/so o ben trai
        while (trai < phai && !isalnum((unsigned char)s[trai])) trai++;
        // Bo qua o ben phai
        while (trai < phai && !isalnum((unsigned char)s[phai])) phai--;

        if (tolower((unsigned char)s[trai]) != tolower((unsigned char)s[phai]))
            return false;

        trai++;
        phai--;
    }
    return true;
}

int main() {
    const char *ds[] = {
        "aba",
        "A man, a plan, a canal: Panama",
        "Race Car",
        "hello",
        ""
    };

    for (int i = 0; i < 5; i++) {
        printf("\"%s\" -> %s\n", ds[i], laDoiXung(ds[i]) ? "DOI XUNG" : "khong");
    }
    return 0;
}
```

Output:

```
"aba" -> DOI XUNG
"A man, a plan, a canal: Panama" -> DOI XUNG
"Race Car" -> DOI XUNG
"hello" -> khong
"" -> DOI XUNG
```

**Kỹ thuật 2 con trỏ** với 2 vòng `while` bên trong để **nhảy qua** các ký tự không phải chữ/số.

⚠️ Với chuỗi rỗng, `strlen` trả về 0 kiểu `size_t` (không dấu); ép sang `int` trước khi trừ 1 để được `-1` chứ không phải một số không dấu cực lớn.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

int main() {
    char s[1000];
    printf("Nhap mot cau: ");
    if (fgets(s, sizeof(s), stdin) == NULL) return 0;

    int dem = 0;
    bool trongTu = false;
    for (int i = 0; s[i] != '\0'; i++) {
        if (isspace((unsigned char)s[i])) {
            trongTu = false;
        } else if (!trongTu) {
            trongTu = true;
            dem++;                    // bat dau mot tu moi
        }
    }
    printf("So tu: %d\n", dem);
    return 0;
}
```

Input: `   Hoc   lap trinh  C   ` → Output: `So tu: 4`

💡 Biến cờ `trongTu` là kỹ thuật kinh điển: chỉ đếm khi **chuyển từ khoảng trắng sang ký tự**. Cách này tự xử lý nhiều dấu cách liên tiếp, dấu cách đầu/cuối, tab và cả `'\n'` do `fgets` giữ lại (vì `isspace('\n')` đúng).

💡 Cách khác dùng hàm `strtok` để tách từ — xem bài [09-07](../09-07-c-tach-chuoi-voi-strtok-va-sscanf.md).

### Bài 9.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char s[1000];
    printf("Nhap mot cau: ");
    if (fgets(s, sizeof(s), stdin) == NULL) return 0;

    int bdDai = -1, lenDai = 0;       // vi tri bat dau va do dai tu dai nhat
    int bdNgan = -1, lenNgan = 0;     // ... tu ngan nhat

    int i = 0;
    while (s[i] != '\0') {
        while (s[i] != '\0' && isspace((unsigned char)s[i])) i++;   // bo khoang trang
        if (s[i] == '\0') break;

        int bd = i;                                                  // dau tu
        while (s[i] != '\0' && !isspace((unsigned char)s[i])) i++;   // chay het tu
        int len = i - bd;

        if (bdDai == -1 || len > lenDai)   { bdDai = bd;  lenDai = len; }
        if (bdNgan == -1 || len < lenNgan) { bdNgan = bd; lenNgan = len; }
    }

    if (bdDai == -1) {
        printf("Chuoi khong co tu nao!\n");
    } else {
        // %.*s: in dung lenDai ky tu bat dau tu s + bdDai
        printf("Tu dai nhat : \"%.*s\" (%d ky tu)\n", lenDai, s + bdDai, lenDai);
        printf("Tu ngan nhat: \"%.*s\" (%d ky tu)\n", lenNgan, s + bdNgan, lenNgan);
    }
    return 0;
}
```

Input: `Hoc lap trinh C that vui` → Output:

```
Tu dai nhat : "trinh" (5 ky tu)
Tu ngan nhat: "C" (1 ky tu)
```

💡 Thay vì chép từng từ ra mảng riêng, ta chỉ lưu **vị trí bắt đầu + độ dài**, rồi in bằng `printf("%.*s", len, s + bd)` — độ chính xác `.*` lấy từ tham số, giới hạn số ký tự in ra.

### Bài 10.

```c
#include <stdio.h>
#include <string.h>

// Chep toi da soKyTu ky tu cua s, bat dau tu viTri, vao kq. Tra ve kq.
char *layChuoiCon(const char *s, int viTri, int soKyTu, char kq[]) {
    int n = strlen(s);
    int k = 0;
    if (viTri >= 0 && viTri < n) {
        for (int i = viTri; i < n && k < soKyTu; i++) kq[k++] = s[i];
    }
    kq[k] = '\0';                       // BAT BUOC ket thuc chuoi
    return kq;
}

int main() {
    char s[] = "Lap trinh C co ban";
    char kq[100];
    int n = strlen(s);

    printf("Chuoi goc : \"%s\" (%d ky tu)\n", s, n);
    printf("5 ky tu dau : \"%s\"\n", layChuoiCon(s, 0, 5, kq));
    printf("5 ky tu cuoi: \"%s\"\n", layChuoiCon(s, n - 5, 5, kq));
    printf("Ky tu 3-7   : \"%s\"\n", layChuoiCon(s, 3, 5, kq));   // tu vi tri 3, lay 5
    printf("Tu vi tri 10: \"%s\"\n", layChuoiCon(s, 10, n, kq));  // den het chuoi
    printf("Vi tri 100  : \"%s\"\n", layChuoiCon(s, 100, 5, kq)); // vuot qua -> rong
    return 0;
}
```

Output:

```
Chuoi goc : "Lap trinh C co ban" (18 ky tu)
5 ky tu dau : "Lap t"
5 ky tu cuoi: "o ban"
Ky tu 3-7   : " trin"
Tu vi tri 10: "C co ban"
Vi tri 100  : ""
```

⚠️ Quên dòng `kq[k] = '\0'` là lỗi kinh điển: chuỗi kết quả sẽ dính rác phía sau.

⚠️ Mảng `kq` phải đủ chỗ cho `soKyTu + 1` ký tự. Hàm tự dừng ở cuối chuỗi nên `viTri + soKyTu` vượt quá độ dài cũng không lỗi.

💡 Với thư viện chuẩn có thể dùng `strncpy(kq, s + viTri, soKyTu); kq[soKyTu] = '\0';` — xem bài [09-03](../09-03-c-cac-ham-xu-ly-chuoi-trong-stringh.md).

### Bài 11.

```c
char s[7] = "codelab";                 // LOI 1: khong con cho cho '\0'
char t[20];
t = s;                                 // LOI 2: khong gan duoc mang bang '='
if (t == "codelab") printf("%s", t);   // LOI 3: '==' so sanh DIA CHI, khong so sanh noi dung
```

**Phân tích:**

| Dòng | Lỗi | Hậu quả |
|---|---|---|
| `char s[7] = "codelab";` | 7 ký tự vừa khít 7 ô, **mất `'\0'`** | C vẫn biên dịch; mọi hàm chuỗi đọc tràn |
| `t = s;` | Mảng không phải biến gán được | **Lỗi biên dịch** |
| `t == "codelab"` | So sánh 2 địa chỉ | Luôn sai (gcc còn cảnh báo) |

**Sửa:**

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s[] = "codelab";              // de trinh bien dich tu tinh: 8 byte
    char t[20];
    strcpy(t, s);                      // sao chep NOI DUNG
    if (strcmp(t, "codelab") == 0)     // so sanh NOI DUNG
        printf("%s\n", t);
    return 0;
}
```

Output: `codelab`

✅ **Nguyên tắc:** gán chuỗi dùng `strcpy`, so sánh chuỗi dùng `strcmp` — chi tiết ở bài [09-03](../09-03-c-cac-ham-xu-ly-chuoi-trong-stringh.md) và [09-05](../09-05-c-so-sanh-chuoi-theo-thu-tu-tu-dien.md).

### Bài 12.

```c
#include <stdio.h>

int main() {
    char s[] = "codelab";          // MANG: 8 byte rieng, noi dung duoc sao chep vao
    const char *p = "codelab";     // CON TRO: tro toi hang chuoi o vung nho chi doc

    printf("sizeof(s) = %zu\n", sizeof(s));    // 8  - kich thuoc ca mang
    printf("sizeof(p) = %zu\n", sizeof(p));    // 8 tren may 64-bit - kich thuoc CON TRO

    s[0] = 'C';                    // OK: mang cua minh
    printf("s = %s\n", s);

    // p[0] = 'C';                 // LOI BIEN DICH nho const (khong co const: crash luc chay)

    p = "hello";                   // OK: con tro tro sang chuoi khac
    printf("p = %s\n", p);

    // s = "hello";                // LOI BIEN DICH: ten mang khong gan lai duoc
    return 0;
}
```

Output (máy 64-bit):

```
sizeof(s) = 8
sizeof(p) = 8
s = Codelab
p = hello
```

**Bảng so sánh:**

| Tiêu chí | `char s[] = "codelab";` | `char *p = "codelab";` |
|---|---|---|
| **Bản chất** | Mảng riêng, chứa bản sao nội dung | Con trỏ tới hằng chuỗi |
| **`sizeof`** | Kích thước mảng (8) | Kích thước con trỏ (4 hoặc 8) |
| **Sửa ký tự `x[0] = 'C'`** | ✅ Được | ❌ Hành vi không xác định (thường crash) |
| **Trỏ/gán sang chuỗi khác** | ❌ Không (`s = ...` lỗi) | ✅ Được (`p = "hello"`) |
| **Vùng nhớ** | Stack (nếu là biến cục bộ) | Vùng hằng chỉ đọc |
| **Nên khai báo** | `char s[]` | `const char *p` |

⚠️ Ở ví dụ trên `sizeof(s)` và `sizeof(p)` tình cờ cùng bằng 8, hãy thử với `"lap trinh"` để thấy khác biệt: `sizeof(s)` thành 10 còn `sizeof(p)` vẫn là 8.

### Bài 13.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char dong[1000];
    int soDong = 0;
    long long tongKyTu = 0;

    printf("Nhap van ban (dong trong de ket thuc):\n");

    while (fgets(dong, sizeof(dong), stdin) != NULL) {
        dong[strcspn(dong, "\n")] = '\0';       // bo '\n'
        if (dong[0] == '\0') break;             // dong trong -> dung

        soDong++;
        tongKyTu += strlen(dong);
    }

    printf("\nSo dong    : %d\n", soDong);
    printf("Tong ky tu : %lld\n", tongKyTu);
    if (soDong > 0)
        printf("TB moi dong: %.2f ky tu\n", (double)tongKyTu / soDong);
    return 0;
}
```

Input:

```
Hoc lap trinh C
chuoi ky tu

```

Output:

```
So dong    : 2
Tong ky tu : 26
TB moi dong: 13.00 ky tu
```

💡 `fgets` trả về `NULL` khi gặp **cuối file** (bấm `Ctrl+D` trên Linux/macOS, `Ctrl+Z` rồi Enter trên Windows), nên vòng `while` cũng tự dừng nếu không có dòng trống.

⚠️ Dòng dài hơn 999 ký tự sẽ bị `fgets` cắt làm nhiều lần đọc — tăng kích thước mảng nếu cần.

### Bài 14.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Cat khoang trang o CUOI: dat '\0' ngay sau ky tu khong trang cuoi cung
void trimPhai(char s[]) {
    int n = strlen(s);
    while (n > 0 && isspace((unsigned char)s[n - 1])) n--;
    s[n] = '\0';
}

// Cat khoang trang o DAU: dich ca chuoi sang trai
void trimTrai(char s[]) {
    int i = 0;
    while (s[i] != '\0' && isspace((unsigned char)s[i])) i++;
    if (i > 0) memmove(s, s + i, strlen(s + i) + 1);   // +1 de chep ca '\0'
}

// Cat ca hai dau
void trim(char s[]) {
    trimPhai(s);
    trimTrai(s);
}

int main() {
    char a[] = "   codelab dev   ";
    char b[] = "   codelab dev   ";
    char c[] = "   codelab dev   ";
    char d[] = "     ";
    char e[] = "";

    printf("Goc      : [%s]\n", a);
    trimTrai(a); printf("trimTrai : [%s]\n", a);
    trimPhai(b); printf("trimPhai : [%s]\n", b);
    trim(c);     printf("trim     : [%s]\n", c);

    trim(d); printf("\nChuoi toan khoang trang: [%s]\n", d);
    trim(e); printf("Chuoi rong: [%s]\n", e);
    return 0;
}
```

Output:

```
Goc      : [   codelab dev   ]
trimTrai : [codelab dev   ]
trimPhai : [   codelab dev]
trim     : [codelab dev]

Chuoi toan khoang trang: []
Chuoi rong: []
```

💡 **Cắt cuối rất rẻ** — chỉ cần đặt `'\0'` sớm hơn. **Cắt đầu** phải dịch cả chuỗi sang trái; dùng `memmove` (không dùng `strcpy`) vì vùng nguồn và đích **chồng lên nhau**.

💡 Nên `trimPhai` trước rồi mới `trimTrai` — để lượng dữ liệu phải dịch ít hơn.

⚠️ Luôn xử lý 2 trường hợp đặc biệt: **chuỗi rỗng** và **chuỗi toàn khoảng trắng**.

### Bài 15.

```c
#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>

int main() {
    long long soDong = 0, soTu = 0, soKyTu = 0, soKyTuKhongTrang = 0;
    bool trongTu = false;
    int c;                                     // int, KHONG phai char, de nhan duoc EOF

    printf("Nhap van ban (Ctrl+D de ket thuc tren Linux/macOS, Ctrl+Z tren Windows):\n");
    printf("-----------------------------------------------------------\n");

    while ((c = getchar()) != EOF) {
        soKyTu++;
        if (c == '\n') soDong++;

        if (isspace(c)) {
            trongTu = false;
        } else {
            soKyTuKhongTrang++;
            if (!trongTu) { trongTu = true; soTu++; }
        }
    }

    printf("-----------------------------------------------------------\n");
    printf("+-----------------------------+------------+\n");
    printf("| %-27s | %10s |\n", "THONG KE", "SO LUONG");
    printf("+-----------------------------+------------+\n");
    printf("| %-27s | %10lld |\n", "So dong", soDong);
    printf("| %-27s | %10lld |\n", "So tu", soTu);
    printf("| %-27s | %10lld |\n", "So ky tu (ke ca trang)", soKyTu);
    printf("| %-27s | %10lld |\n", "So ky tu (khong trang)", soKyTuKhongTrang);
    printf("+-----------------------------+------------+\n");

    if (soDong > 0)
        printf("\nTrung binh %.2f tu/dong\n", (double)soTu / soDong);
    if (soTu > 0)
        printf("Trung binh %.2f ky tu/tu\n", (double)soKyTuKhongTrang / soTu);
    return 0;
}
```

Chạy thử với file:

```bash
gcc -std=c11 -Wall wc.c -o wc
./wc < vanban.txt
```

So sánh với lệnh `wc` của Linux:

```bash
wc vanban.txt          # in ra: so dong, so tu, so byte
```

💡 Đọc **từng ký tự** bằng `getchar()` thay vì từng dòng giúp không phải lo dòng dài hơn mảng — giống cách lệnh `wc` thật hoạt động. Số dòng được đếm bằng số ký tự `'\n'`, đúng quy ước của `wc`.

⚠️ Biến `c` phải khai báo **`int`**: `getchar()` trả về `EOF` (thường là -1), giá trị không nằm trong phạm vi `unsigned char`. Khai báo `char c` có thể làm vòng lặp không bao giờ dừng hoặc dừng sai.

💡 `%-27s` in chuỗi căn trái trong 27 ô, `%10lld` in số `long long` căn phải trong 10 ô.
