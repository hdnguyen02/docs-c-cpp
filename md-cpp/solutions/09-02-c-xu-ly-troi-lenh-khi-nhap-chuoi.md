# Lời giải — [C]. Xử Lý Trôi Lệnh Khi Nhập Chuỗi

[← Quay lại bài học](../09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi.md)

> **Nguyên nhân gốc rễ:** `scanf("%d", &x)` đọc giá trị nhưng **để lại ký tự Enter (`'\n'`)** trong bộ đệm `stdin`. `fgets` gặp ngay ký tự đó và kết thúc → xâu nhận được chỉ là `"\n"` (dòng rỗng).

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    char s[100];

    printf("Nhap so: ");
    scanf("%d", &n);

    printf("Nhap chuoi: ");
    fgets(s, sizeof(s), stdin);

    printf("n = %d, s = [%s]\n", n, s);
    return 0;
}
```

**Hiện tượng:** chương trình **không dừng lại** để bạn nhập chuỗi. Nó in ngay:

```
Nhap so: 25
Nhap chuoi: n = 25, s = [
]
```

Dấu `]` bị đẩy xuống dòng dưới vì trong `s` có đúng một ký tự `'\n'`.

**Giải thích chi tiết — theo dõi bộ đệm bàn phím:**

```
Ban go: 2 5 Enter
Bo dem chua:  '2' '5' '\n'

scanf("%d", &n):
   - Doc '2', '5' -> n = 25
   - GAP '\n' -> DUNG, nhung KHONG LAY '\n' ra khoi bo dem
   Bo dem con lai:  '\n'

fgets(s, 100, stdin):
   - Doc tu bo dem, GAP NGAY '\n' o ky tu dau tien
   - Luu '\n' vao s, them '\0' -> s = "\n"
   Bo dem: (rong)
```

**Bản chất:** `scanf("%d")` **bỏ qua khoảng trắng ở đầu** nhưng **không xoá khoảng trắng phía sau**. `fgets` thì ngược lại — nó đọc mọi thứ tới `'\n'` đầu tiên (và giữ luôn `'\n'` trong xâu).

### Bài 2.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    char s[100];

    printf("Nhap so: ");
    scanf("%d", &n);

    getchar();                       // BO ky tu '\n' con sot lai

    printf("Nhap chuoi: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';      // XOA '\n' o cuoi xau

    printf("n = %d, s = [%s]\n", n, s);
    return 0;
}
```

Kết quả:

```
Nhap so: 25
Nhap chuoi: codelab dev
n = 25, s = [codelab dev]
```

💡 `strcspn(s, "\n")` trả về vị trí của `'\n'` đầu tiên (hoặc `strlen(s)` nếu không có), nên dòng này an toàn cả khi xâu không chứa `'\n'`. Cần `#include <string.h>`.

### Bài 3.

```c
#include <stdio.h>
#include <string.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main(void) {
    int tuoi;
    char hoTen[100];

    printf("Nhap tuoi: ");
    scanf("%d", &tuoi);
    xoaDem();

    printf("Nhap ho ten day du: ");
    fgets(hoTen, sizeof(hoTen), stdin);
    hoTen[strcspn(hoTen, "\n")] = '\0';

    printf("\n--- THONG TIN ---\n");
    printf("Ho ten: %s\n", hoTen);
    printf("Tuoi  : %d\n", tuoi);
    return 0;
}
```

✅ **Quy tắc vàng: sau MỌI `scanf` mà tiếp theo là `fgets`, phải xoá bộ đệm.**

### Bài 4.

```c
#include <stdio.h>
#include <string.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main(void) {
    int n;
    char ds[100][51];

    printf("Nhap so nguoi (<= 100): ");
    scanf("%d", &n);
    xoaDem();                                  // <- BAT BUOC
    if (n < 0) n = 0;
    if (n > 100) n = 100;

    for (int i = 0; i < n; i++) {
        printf("  Ho ten nguoi %d: ", i + 1);
        if (fgets(ds[i], sizeof(ds[i]), stdin) == NULL) ds[i][0] = '\0';
        ds[i][strcspn(ds[i], "\n")] = '\0';
    }

    printf("\n--- DANH SACH ---\n");
    for (int i = 0; i < n; i++) {
        printf("%d. %s\n", i + 1, ds[i]);
    }
    return 0;
}
```

⚠️ Chỉ cần **một** lần xoá bộ đệm sau `scanf("%d", &n)`. Các `fgets` sau đó không cần thêm gì, vì `fgets` **có lấy** ký tự `'\n'` ra khỏi bộ đệm (miễn là dòng không dài hơn 50 ký tự).

### Bài 5.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    char s[100];

    scanf("%d", &n);

    // (1) getchar()  -> chi bo 1 ky tu
    // getchar();

    // (2) scanf("%*[^\n]"); getchar();  -> bo moi ky tu truoc '\n', roi bo '\n'
    // scanf("%*[^\n]");
    // getchar();

    // (3) AN TOAN NHAT
    int c;
    while ((c = getchar()) != '\n' && c != EOF);

    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';
    printf("n = %d, s = [%s]\n", n, s);
    return 0;
}
```

**So sánh:**

| Cách | Bỏ qua | Rủi ro |
|---|---|---|
| `getchar()` | **Đúng 1 ký tự** | ⚠️ Hỏng nếu người dùng gõ `25 abc` rồi Enter — chỉ bỏ dấu cách, còn `abc` |
| `scanf("%*[^\n]"); getchar();` | Toàn bộ phần còn lại của dòng | ✅ Chạy đúng, nhưng khó đọc và phải nhớ đủ 2 lệnh |
| `while ((c = getchar()) != '\n' && c != EOF);` | **Toàn bộ dòng, không giới hạn**, dừng cả khi hết dữ liệu | ✅ An toàn, rõ ràng |

**Thử nghiệm với input `25 rac rac rac`:**

```
scanf("%d", &n)     -> n = 25, bo dem: " rac rac rac\n"
getchar()           -> bo 1 ky tu (dau cach), bo dem: "rac rac rac\n"
fgets(s, ...)       -> s = "rac rac rac"    <- SAI, khong phai cai ta muon
```

Với cách (3), toàn bộ phần rác bị xoá sạch.

⚠️ Biến `c` phải có kiểu **`int`**, không phải `char`, để so sánh đúng được với `EOF`.

✅ **Luôn dùng cách (3).** Nên đóng gói thành hàm cho gọn:

```c
void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}
```

⚠️ Đừng dùng `fflush(stdin)`: chuẩn C **không định nghĩa** hành vi của `fflush` với luồng vào, có trình biên dịch chạy được, có cái không.

### Bài 6.

```c
#include <stdio.h>
#include <string.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void docDong(char *s, int size) {
    if (fgets(s, size, stdin) == NULL) s[0] = '\0';
    s[strcspn(s, "\n")] = '\0';
}

int main(void) {
    int maSV;
    char hoTen[100];
    double diem;
    char ghiChu[200];

    printf("Ma sinh vien   : ");  scanf("%d", &maSV);   xoaDem();
    printf("Ho ten         : ");  docDong(hoTen, sizeof(hoTen));
    printf("Diem trung binh: ");  scanf("%lf", &diem);  xoaDem();
    printf("Ghi chu        : ");  docDong(ghiChu, sizeof(ghiChu));

    printf("\n--- KET QUA ---\n");
    printf("Ma SV  : %d\n", maSV);
    printf("Ho ten : %s\n", hoTen);
    printf("Diem   : %.2f\n", diem);
    printf("Ghi chu: %s\n", ghiChu);
    return 0;
}
```

💡 **Tách hàm `xoaDem()` và `docDong()`** làm code sạch hơn nhiều so với viết lại vòng lặp và `strcspn` mỗi lần.

**Quy tắc đặt `xoaDem()`:** ngay sau **mọi** `scanf`, nếu sau đó còn `fgets`.

### Bài 7.

```c
char s1[100], s2[100];
fgets(s1, sizeof(s1), stdin);
getchar();        // <- THUA! Day la nguyen nhan loi
fgets(s2, sizeof(s2), stdin);
```

**Lỗi:** `getchar()` ở đây là **thừa** và gây hại.

**Vì sao:** `fgets` **đã lấy** ký tự `'\n'` ra khỏi bộ đệm rồi (và lưu nó vào `s1`). Nên sau `fgets(s1, ...)`, bộ đệm đã sạch.

`getchar()` tiếp theo sẽ **nuốt mất ký tự đầu tiên** của dòng thứ hai:

```
Ban go:
  dong mot
  dong hai

fgets(s1, ...)  -> s1 = "dong mot\n", bo dem sach
getchar()       -> CHO nguoi dung nhap, roi nuot ky tu 'd' dau tien
fgets(s2, ...)  -> s2 = "ong hai\n"    <- MAT chu 'd'!
```

**Sửa:** bỏ dòng `getchar()`.

```c
char s1[100], s2[100];
fgets(s1, sizeof(s1), stdin);
fgets(s2, sizeof(s2), stdin);     // khong can gi them
```

✅ **Quy tắc rõ ràng:**

| Tình huống | Cần xoá bộ đệm? |
|---|---|
| `scanf("%d")` rồi `fgets` | ✅ **CÓ** |
| `fgets` rồi `fgets` | ❌ Không (nếu dòng không dài hơn mảng) |
| `scanf("%d")` rồi `scanf("%d")` | ❌ Không (`%d` tự bỏ khoảng trắng đầu) |
| `fgets` rồi `scanf("%d")` | ❌ Không |
| `scanf("%d")` rồi `scanf("%c")` | ✅ **CÓ** — hoặc dùng `" %c"` |

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int nhapSo(const char *loiNhac) {
    int n;
    while (1) {
        printf("%s", loiNhac);
        int kq = scanf("%d", &n);

        if (kq == 1) {                // doc thanh cong 1 so
            xoaDem();
            return n;
        }
        if (kq == EOF) {              // het du lieu (Ctrl+D / Ctrl+Z)
            printf("\nKhong con du lieu vao!\n");
            exit(1);
        }
        // kq == 0: nhap sai -> xoa du lieu rac roi hoi lai
        xoaDem();
        printf("  -> Khong hop le! Vui long nhap mot SO NGUYEN.\n");
    }
}

int main(void) {
    int tuoi = nhapSo("Nhap tuoi: ");
    int nam  = nhapSo("Nhap nam sinh: ");

    printf("\nTuoi: %d, Nam sinh: %d\n", tuoi, nam);
    return 0;
}
```

Ví dụ chạy:

```
Nhap tuoi: abc
  -> Khong hop le! Vui long nhap mot SO NGUYEN.
Nhap tuoi: 12.5
  -> (nhan 12, phan .5 bi xoa)
Nhap nam sinh: 2001
```

**Giá trị trả về của `scanf` là chìa khoá:**
1. **`1`** — đọc được 1 biến, dữ liệu hợp lệ
2. **`0`** — ký tự đầu không phải số, **ký tự sai vẫn nằm lại trong bộ đệm**
3. **`EOF`** — hết dữ liệu vào

⚠️ Thiếu `xoaDem()` khi `kq == 0`: chữ `abc` vẫn còn trong bộ đệm → `scanf` lần sau lại thất bại ngay → **vòng lặp vô hạn**.
⚠️ Không xử lý `EOF`: khi người dùng bấm Ctrl+D, `scanf` trả `EOF` mãi mãi → **vòng lặp vô hạn**.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void nhapChuoi(const char *loiNhac, char *s, int size, bool choPhepRong) {
    while (1) {
        printf("%s", loiNhac);
        if (fgets(s, size, stdin) == NULL) {    // het du lieu
            s[0] = '\0';
            return;
        }
        if (strchr(s, '\n') == NULL) xoaDem();  // dong qua dai -> bo phan thua
        s[strcspn(s, "\n")] = '\0';

        if (s[0] != '\0' || choPhepRong) return;
        printf("  -> Khong duoc de trong!\n");
    }
}

int nhapSo(const char *loiNhac) {
    int n;
    while (1) {
        printf("%s", loiNhac);
        int kq = scanf("%d", &n);
        if (kq == 1) { xoaDem(); return n; }
        if (kq == EOF) exit(1);
        xoaDem();
        printf("  -> Phai nhap so!\n");
    }
}

int main(void) {
    char hoTen[100], diaChi[200];
    int tuoi = nhapSo("Nhap tuoi: ");
    nhapChuoi("Nhap ho ten: ", hoTen, sizeof(hoTen), false);
    nhapChuoi("Nhap dia chi (co the bo trong): ", diaChi, sizeof(diaChi), true);

    printf("\n--- KET QUA ---\n");
    printf("Ho ten : %s\n", hoTen);
    printf("Tuoi   : %d\n", tuoi);
    printf("Dia chi: %s\n", diaChi[0] == '\0' ? "(khong co)" : diaChi);
    return 0;
}
```

💡 Nhờ `nhapSo` đã tự xoá bộ đệm bên trong, hàm `nhapChuoi` không cần lo về trôi lệnh nữa.

⚠️ C **không có đối số mặc định**, nên tham số `choPhepRong` phải truyền rõ ở mọi lần gọi.

💡 Nếu dòng người dùng gõ dài hơn `size - 1` ký tự, `fgets` chỉ đọc một phần và **không có `'\n'`** trong xâu — phần còn lại vẫn nằm trong bộ đệm. Dòng `if (strchr(s, '\n') == NULL) xoaDem();` dọn phần thừa này để lần nhập sau không bị ảnh hưởng.

### Bài 10.

```c
#include <stdio.h>
#include <string.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main(void) {
    char luaChon;
    char noiDung[200];

    printf("Chon chuc nang (a/b/c): ");
    scanf(" %c", &luaChon);      // dau cach: bo qua khoang trang/enter phia truoc
    xoaDem();                    // <- BAT BUOC: bo '\n' phia sau

    printf("Nhap noi dung: ");
    fgets(noiDung, sizeof(noiDung), stdin);
    noiDung[strcspn(noiDung, "\n")] = '\0';

    printf("\nLua chon : %c\n", luaChon);
    printf("Noi dung : %s\n", noiDung);
    return 0;
}
```

⚠️ **`scanf(" %c")` với `char` cũng để lại `'\n'`** giống như với số. Dấu cách trước `%c` chỉ bỏ khoảng trắng **phía trước** ký tự, không bỏ phía sau.

⚠️ Nếu viết `scanf("%c", &c)` (không có dấu cách) ngay sau một `scanf("%d")`, biến `c` sẽ nhận luôn `'\n'` còn sót — đây là dạng trôi lệnh thứ hai rất hay gặp.

### Bài 11.

```c
#include <stdio.h>
#include <ctype.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main(void) {
    // ===== getchar() : doc MOT ky tu, KE CA khoang trang =====
    printf("--- getchar() ---\n");
    printf("Nhap 3 ky tu (ke ca dau cach): ");
    int a = getchar();
    int b = getchar();
    int c = getchar();
    printf("Da doc: [%c][%c][%c]\n", a, b, c);
    xoaDem();

    // ===== "peek": doc 1 ky tu roi TRA LAI bang ungetc =====
    printf("\n--- xem truoc (getchar + ungetc) ---\n");
    printf("Nhap mot so hoac mot chu: ");
    int tiep = getchar();
    ungetc(tiep, stdin);                 // tra lai -> bo dem nhu cu
    if (isdigit(tiep)) {
        int n;
        scanf("%d", &n);
        printf("Da doc mot SO: %d\n", n);
    } else {
        char s[100];
        scanf("%99s", s);
        printf("Da doc mot CHUOI: %s\n", s);
    }
    xoaDem();

    // ===== ungetc() : TRA LAI ky tu vao bo dem =====
    printf("\n--- ungetc() ---\n");
    printf("Nhap mot tu: ");
    int d = getchar();
    printf("Ky tu dau: %c\n", d);
    ungetc(d, stdin);                    // TRA LAI
    char tu[100];
    scanf("%99s", tu);
    printf("Ca tu (ky tu dau van con): %s\n", tu);

    return 0;
}
```

**Bảng tổng hợp:**

| Hàm / cách | Tác dụng | Có lấy ký tự ra không? |
|---|---|---|
| `getchar()` | Đọc 1 ký tự từ `stdin`, **kể cả khoảng trắng**; trả `EOF` khi hết | ✅ Có |
| `getc(stdin)`, `fgetc(stdin)` | Giống `getchar()` nhưng chỉ rõ luồng | ✅ Có |
| `c = getchar(); ungetc(c, stdin);` | **Xem** ký tự kế tiếp | ❌ Không (trả lại ngay) |
| `ungetc(c, stdin)` | **Trả lại** ký tự vào bộ đệm (chuẩn đảm bảo ít nhất 1 ký tự) | Ngược lại |
| `scanf("%*c")` | Bỏ qua 1 ký tự | ✅ Có |
| `scanf("%*[^\n]")` | Bỏ qua tới trước `'\n'` | ✅ Có |

💡 **Xem trước bằng `getchar` + `ungetc` rất hữu ích** khi cần quyết định đọc kiểu gì mà chưa biết trước dữ liệu là số hay chữ.

⚠️ Giá trị của `getchar()` là `int`; khi truyền cho `isdigit` thì giá trị đó đã nằm trong khoảng `unsigned char` hoặc là `EOF`, nên dùng trực tiếp được.

### Bài 12.

```c
#include <stdio.h>

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

void inTrangThai(int kq) {
    printf("  scanf tra ve = %d, feof = %d, ferror = %d\n",
           kq, feof(stdin) != 0, ferror(stdin) != 0);
}

int main(void) {
    int n;

    printf("Nhap mot SO (thu nhap chu de xem loi): ");
    int kq = scanf("%d", &n);

    printf("Trang thai sau khi doc:\n");
    inTrangThai(kq);

    if (kq == 0) {
        printf("  -> Nhap SAI dinh dang, du lieu rac con trong bo dem\n");
        xoaDem();                                    // XOA du lieu rac

        printf("\nNhap lai (lan nay nhap so): ");
        if (scanf("%d", &n) == 1) printf("Da doc: %d\n", n);
    } else if (kq == EOF) {
        printf("  -> Het du lieu (EOF)\n");
        clearerr(stdin);                             // XOA co EOF/loi
        printf("  Sau clearerr(stdin):\n");
        inTrangThai(0);
    } else {
        printf("  -> Doc thanh cong: %d\n", n);
    }
    return 0;
}
```

**Giá trị trả về của `scanf` và các hàm trạng thái:**

| Thứ cần kiểm tra | Ý nghĩa | Khi nào xảy ra |
|---|---|---|
| `scanf` trả **số biến đọc được** | Thành công (một phần hoặc toàn bộ) | Dữ liệu đúng định dạng |
| `scanf` trả **`0`** | Không đọc được biến nào | Nhập chữ khi cần số; định dạng sai |
| `scanf` trả **`EOF`** | Hết dữ liệu hoặc lỗi trước khi đọc được gì | Bấm `Ctrl+D`/`Ctrl+Z`, hoặc hết file |
| `feof(stdin)` khác 0 | Cờ **cuối dữ liệu** đã bật | Sau khi đọc chạm EOF |
| `ferror(stdin)` khác 0 | Cờ **lỗi** của luồng đã bật | Lỗi thiết bị, lỗi đọc |
| `clearerr(stdin)` | Xoá cả cờ EOF và cờ lỗi | Khi muốn đọc tiếp |

**Kiểm tra:**

```c
if (scanf("%d", &n) == 1) { /* ... */ }   // cach dung
if (feof(stdin))   { /* het du lieu */ }
if (ferror(stdin)) { /* loi doc */ }
```

⚠️ Khác với một số ngôn ngữ khác, `stdin` **không bị "khoá"** khi nhập sai định dạng: `scanf` chỉ trả `0` và để nguyên ký tự sai trong bộ đệm. Nguyên nhân của vòng lặp vô hạn kinh điển là **không dọn ký tự sai đó**:

```c
int n;
while (1) {
    printf("Nhap so: ");
    scanf("%d", &n);        // that bai, 'a' van nam trong bo dem
    if (n > 0) break;
    // THIEU xoaDem() -> lan sau doc lai dung 'a' -> LAP VO HAN, in lien tuc
}
```

⚠️ Còn một lỗi nữa: khi `scanf` thất bại, biến `n` **không được gán** — nếu `n` chưa khởi tạo thì `if (n > 0)` đọc giá trị rác.

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define MAX_SV 100

void xoaDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int nhapSo(const char *nhac, int min, int max) {
    int n;
    while (1) {
        printf("%s", nhac);
        int kq = scanf("%d", &n);
        if (kq == EOF) exit(1);
        xoaDem();
        if (kq == 1) {
            if (n >= min && n <= max) return n;
            printf("  -> Phai trong khoang [%d, %d]\n", min, max);
        } else {
            printf("  -> Phai nhap SO!\n");
        }
    }
}

double nhapSoThuc(const char *nhac, double min, double max) {
    double x;
    while (1) {
        printf("%s", nhac);
        int kq = scanf("%lf", &x);
        if (kq == EOF) exit(1);
        xoaDem();
        if (kq == 1 && x >= min && x <= max) return x;
        printf("  -> Phai la so tu %.0f den %.0f!\n", min, max);
    }
}

void nhapChuoi(const char *nhac, char *s, int size) {
    while (1) {
        printf("%s", nhac);
        if (fgets(s, size, stdin) == NULL) exit(1);
        if (strchr(s, '\n') == NULL) xoaDem();
        s[strcspn(s, "\n")] = '\0';
        if (s[0] != '\0') return;
        printf("  -> Khong duoc de trong!\n");
    }
}

typedef struct {
    char ten[51];
    int tuoi;
    double diem;
} SinhVien;

int main(void) {
    SinhVien ds[MAX_SV];
    int soSV = 0;
    int chon;

    do {
        printf("\n====== QUAN LY SINH VIEN ======\n");
        printf("1. Them sinh vien\n");
        printf("2. Hien thi danh sach\n");
        printf("3. Tim theo ten\n");
        printf("0. Thoat\n");
        printf("===============================\n");

        chon = nhapSo("Lua chon: ", 0, 3);

        switch (chon) {
            case 1: {
                if (soSV == MAX_SV) { printf(">> Danh sach da day!\n"); break; }
                SinhVien sv;
                nhapChuoi("  Ho ten: ", sv.ten, sizeof(sv.ten));
                sv.tuoi = nhapSo("  Tuoi: ", 1, 150);
                sv.diem = nhapSoThuc("  Diem TB: ", 0, 10);
                ds[soSV++] = sv;
                printf(">> Da them!\n");
                break;
            }
            case 2:
                if (soSV == 0) { printf(">> Danh sach rong!\n"); break; }
                printf("\n--- DANH SACH ---\n");
                for (int i = 0; i < soSV; i++)
                    printf("%d. %s - %d tuoi - %.2f diem\n",
                           i + 1, ds[i].ten, ds[i].tuoi, ds[i].diem);
                break;
            case 3: {
                char canTim[51];
                nhapChuoi("  Nhap ten can tim: ", canTim, sizeof(canTim));
                bool thay = false;
                for (int i = 0; i < soSV; i++)
                    if (strcmp(ds[i].ten, canTim) == 0) {
                        printf(">> Tim thay: %s - %d tuoi - %.2f\n",
                               ds[i].ten, ds[i].tuoi, ds[i].diem);
                        thay = true;
                    }
                if (!thay) printf(">> Khong tim thay!\n");
                break;
            }
            case 0:
                printf(">> Tam biet!\n");
                break;
        }
    } while (chon != 0);

    return 0;
}
```

💡 Nhờ dùng các hàm `nhapSo`/`nhapSoThuc`/`nhapChuoi` đã xử lý sẵn, chương trình **không bao giờ** bị trôi lệnh hay lặp vô hạn, dù người dùng nhập gì.

💡 So sánh hai xâu trong C phải dùng `strcmp(a, b) == 0`, **không** dùng `a == b` (phép đó chỉ so sánh địa chỉ).

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <limits.h>

int main(void) {
    char dong[100];
    int n;

    // ===== CACH 2: fgets + strtol =====
    printf("Nhap mot so: ");
    if (fgets(dong, sizeof(dong), stdin) == NULL) return 1;
    dong[strcspn(dong, "\n")] = '\0';

    char *het;
    errno = 0;
    long v = strtol(dong, &het, 10);

    if (het == dong) {
        printf("Loi: khong phai so!\n");
    } else if (errno == ERANGE || v < INT_MIN || v > INT_MAX) {
        printf("Loi: so qua lon!\n");
    } else {
        n = (int)v;
        printf("Da doc: %d\n", n);
        if (*het != '\0') printf("(Co ky tu thua sau so: \"%s\")\n", het);
    }

    // ===== Doc chuoi tiep theo - KHONG CAN xoa bo dem =====
    char s[100];
    printf("Nhap chuoi: ");
    if (fgets(s, sizeof(s), stdin) != NULL) {
        s[strcspn(s, "\n")] = '\0';
        printf("Chuoi: [%s]\n", s);
    }
    return 0;
}
```

**So sánh 2 cách tiếp cận:**

| | `scanf("%d")` + xoá bộ đệm | `fgets` + `strtol` |
|---|---|---|
| Trôi lệnh | ⚠️ Phải nhớ xoá bộ đệm mỗi lần | ✅ **Không bao giờ xảy ra** |
| Xử lý lỗi | Kiểm tra giá trị trả về + xoá rác | Kiểm tra `het`, `errno` |
| Nhập `12abc` | Nhận **12**, để lại `abc` | Nhận 12, `het` trỏ vào `"abc"` → **phát hiện được** |
| Nhập `abc` | `scanf` trả `0` | `het == dong` |
| Số quá lớn | Hành vi **không xác định** | `errno == ERANGE` |
| Nhất quán | Trộn 2 kiểu đọc | ✅ Luôn dùng `fgets` |

✅ **Cách 2 (`fgets` + `strtol`) được nhiều người khuyến nghị** vì nó giải quyết triệt để vấn đề: **mọi lệnh đọc đều là `fgets`**, nên không có khái niệm "trôi lệnh" nữa.

💡 Hàm `atoi(dong)` gọn hơn nhưng **không báo lỗi** (nhập `abc` trả về `0`, không phân biệt được với số 0 thật). Chi tiết `strtol`, `atoi` xem bài [09-04 — Chuyển đổi giữa số và chuỗi](../09-04-c-chuyen-doi-giua-so-va-chuoi.md).

### Bài 15.

**File `nhaplieu.h`:**

```c
// FILE: nhaplieu.h
#ifndef NHAPLIEU_H
#define NHAPLIEU_H

#include <stdbool.h>

/** @brief Xoa sach bo dem ban phim den het dong hien tai. */
void xoaBoDem(void);

/**
 * @brief Nhap so nguyen an toan, bat nhap lai neu sai.
 * @param nhac Loi nhac hien thi.
 * @param min,max Khoang gia tri hop le.
 */
int nhapSoNguyen(const char *nhac, int min, int max);

/** @brief Nhap so thuc an toan trong khoang [min, max]. */
double nhapSoThuc(const char *nhac, double min, double max);

/**
 * @brief Nhap mot dong van ban vao s (toi da size - 1 ky tu).
 * @param choPhepRong Neu false, bat nhap lai khi de trong.
 */
void nhapChuoi(const char *nhac, char *s, int size, bool choPhepRong);

/**
 * @brief Nhap mot ky tu thuoc tap hop cho phep.
 * @param hopLe Chuoi chua cac ky tu duoc chap nhan. "" = chap nhan moi ky tu.
 */
char nhapKyTu(const char *nhac, const char *hopLe);

/** @brief Hien menu cac lua chon 1..soMuc (va 0 = thoat), tra ve lua chon. */
int nhapLuaChon(const char *tieuDe, const char *cacMuc[], int soMuc);

/** @brief Hoi Co/Khong, tra ve true neu nguoi dung chon y/Y. */
bool nhapCoKhong(const char *nhac);

#endif
```

**File `nhaplieu.c`:**

```c
// FILE: nhaplieu.c
#include "nhaplieu.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void xoaBoDem(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int nhapSoNguyen(const char *nhac, int min, int max) {
    int n;
    while (1) {
        printf("%s", nhac);
        int kq = scanf("%d", &n);
        if (kq == EOF) exit(1);
        xoaBoDem();
        if (kq == 1) {
            if (n >= min && n <= max) return n;
            printf("  -> Gia tri phai trong khoang [%d, %d]\n", min, max);
        } else {
            printf("  -> Vui long nhap mot SO NGUYEN!\n");
        }
    }
}

double nhapSoThuc(const char *nhac, double min, double max) {
    double x;
    while (1) {
        printf("%s", nhac);
        int kq = scanf("%lf", &x);
        if (kq == EOF) exit(1);
        xoaBoDem();
        if (kq == 1) {
            if (x >= min && x <= max) return x;
            printf("  -> Gia tri phai trong khoang [%g, %g]\n", min, max);
        } else {
            printf("  -> Vui long nhap mot SO!\n");
        }
    }
}

void nhapChuoi(const char *nhac, char *s, int size, bool choPhepRong) {
    while (1) {
        printf("%s", nhac);
        if (fgets(s, size, stdin) == NULL) exit(1);
        if (strchr(s, '\n') == NULL) xoaBoDem();   // dong qua dai
        s[strcspn(s, "\n")] = '\0';
        if (s[0] != '\0' || choPhepRong) return;
        printf("  -> Khong duoc de trong!\n");
    }
}

char nhapKyTu(const char *nhac, const char *hopLe) {
    char c;
    while (1) {
        printf("%s", nhac);
        int kq = scanf(" %c", &c);
        if (kq == EOF) exit(1);
        xoaBoDem();
        if (hopLe[0] == '\0' || strchr(hopLe, c) != NULL) return c;
        printf("  -> Chi chap nhan cac ky tu: %s\n", hopLe);
    }
}

int nhapLuaChon(const char *tieuDe, const char *cacMuc[], int soMuc) {
    printf("\n===== %s =====\n", tieuDe);
    for (int i = 0; i < soMuc; i++) printf("%d. %s\n", i + 1, cacMuc[i]);
    printf("0. Thoat\n");
    return nhapSoNguyen("Lua chon: ", 0, soMuc);
}

bool nhapCoKhong(const char *nhac) {
    printf("%s (y/n)", nhac);
    char c = nhapKyTu(": ", "yYnN");
    return (c == 'y' || c == 'Y');
}
```

**File `main.c` — kiểm thử:**

```c
// FILE: main.c
#include <stdio.h>
#include "nhaplieu.h"

int main(void) {
    char hoTen[100], email[100];

    printf("===== DANG KY THONG TIN =====\n");

    nhapChuoi("Ho ten        : ", hoTen, sizeof(hoTen), false);
    int    tuoi = nhapSoNguyen("Tuoi          : ", 1, 150);
    double diem = nhapSoThuc("Diem TB (0-10): ", 0, 10);
    char   gioi = nhapKyTu("Gioi tinh (M/F): ", "MFmf");
    nhapChuoi("Email (tuy chon): ", email, sizeof(email), true);

    printf("\n===== THONG TIN DA NHAP =====\n");
    printf("Ho ten   : %s\n", hoTen);
    printf("Tuoi     : %d\n", tuoi);
    printf("Diem TB  : %.2f\n", diem);
    printf("Gioi tinh: %c\n", gioi);
    printf("Email    : %s\n", email[0] == '\0' ? "(khong co)" : email);

    const char *menu[] = { "Luu thong tin", "In lai thong tin" };
    int chon = nhapLuaChon("BAN MUON LAM GI", menu, 2);
    if (chon == 1 && nhapCoKhong("Ban chac chan muon luu")) {
        printf(">> Da luu!\n");
    } else if (chon == 2) {
        printf(">> %s, %d tuoi\n", hoTen, tuoi);
    } else {
        printf(">> Da huy.\n");
    }
    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall main.c nhaplieu.c -o dangky
./dangky
```

💡 C **không có đối số mặc định** như một số ngôn ngữ khác, nên mọi tham số (`min`, `max`, `choPhepRong`, `hopLe`) đều phải truyền rõ. Header dùng **include guard** `#ifndef ... #define ... #endif` để tránh bị include hai lần.

💡 **Hãy giữ thư viện này** — mọi bài tập có nhập liệu về sau đều dùng được, và bạn sẽ không bao giờ gặp lỗi trôi lệnh nữa.
