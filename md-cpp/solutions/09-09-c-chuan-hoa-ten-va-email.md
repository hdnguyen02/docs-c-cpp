# Lời giải — [C]. Chuẩn Hóa Tên Và Email

[← Quay lại bài học](../09-09-c-chuan-hoa-ten-va-email.md)

> **Mẫu chung của các bài chuẩn hoá:** chép chuỗi vào một mảng tạm → tách từ bằng `strtok` → xử lý từng từ → ghép lại bằng `strcat`/`snprintf`. Nhớ rằng `strtok` sửa chuỗi, nên đừng tách trực tiếp trên chuỗi hằng.

---

### Bài 1.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Chuan hoa ho ten tu src, ghi ket qua vao kq
void chuanHoaTen(const char *src, char *kq) {
    char tam[200];
    strncpy(tam, src, sizeof tam - 1);
    tam[sizeof tam - 1] = '\0';

    kq[0] = '\0';
    for (char *t = strtok(tam, " \t\n"); t != NULL; t = strtok(NULL, " \t\n")) {
        t[0] = (char)toupper((unsigned char)t[0]);
        for (int i = 1; t[i]; i++) t[i] = (char)tolower((unsigned char)t[i]);

        if (kq[0] != '\0') strcat(kq, " ");
        strcat(kq, t);
    }
}

int main(void) {
    const char *ds[] = {
        "  nGuYen   vAN   an  ",
        "TRAN THI BINH",
        "le    hoang cuong"
    };
    char kq[200];

    for (int i = 0; i < 3; i++) {
        chuanHoaTen(ds[i], kq);
        printf("[%s] -> [%s]\n", ds[i], kq);
    }
    return 0;
}
```

Output:

```
[  nGuYen   vAN   an  ] -> [Nguyen Van An]
[TRAN THI BINH] -> [Tran Thi Binh]
[le    hoang cuong] -> [Le Hoang Cuong]
```

💡 `strtok` tự động bỏ qua mọi khoảng trắng thừa — không cần viết hàm `trim` riêng.

💡 Hàm nhận `const char *src` và chép sang mảng `tam` trước khi tách, nên gọi được với cả chuỗi hằng.

### Bài 2.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char ho[50];
    char dem[100];
    char ten[50];
} HoTen;

HoTen tachHoTen(const char *s) {
    HoTen kq = {"", "", ""};
    char tam[200];
    strncpy(tam, s, sizeof tam - 1);
    tam[sizeof tam - 1] = '\0';

    char *tu[20];
    int n = 0;
    for (char *t = strtok(tam, " \t\n"); t != NULL && n < 20; t = strtok(NULL, " \t\n"))
        tu[n++] = t;

    if (n == 0) return kq;
    if (n == 1) { strcpy(kq.ten, tu[0]); return kq; }    // chi co ten

    strcpy(kq.ho, tu[0]);
    strcpy(kq.ten, tu[n - 1]);
    for (int i = 1; i < n - 1; i++) {
        if (kq.dem[0] != '\0') strcat(kq.dem, " ");
        strcat(kq.dem, tu[i]);
    }
    return kq;
}

int main(void) {
    const char *ds[] = {
        "Nguyen Van An",
        "Tran Thi Minh Chau",
        "Le Cuong",
        "An"
    };

    for (int i = 0; i < 4; i++) {
        HoTen h = tachHoTen(ds[i]);
        printf("\"%s\"\n", ds[i]);
        printf("  Ho  : %s\n", h.ho[0]  ? h.ho  : "(khong co)");
        printf("  Dem : %s\n", h.dem[0] ? h.dem : "(khong co)");
        printf("  Ten : %s\n\n", h.ten);
    }
    return 0;
}
```

Output:

```
"Nguyen Van An"
  Ho  : Nguyen
  Dem : Van
  Ten : An

"Tran Thi Minh Chau"
  Ho  : Tran
  Dem : Thi Minh
  Ten : Chau

"Le Cuong"
  Ho  : Le
  Dem : (khong co)
  Ten : Cuong

"An"
  Ho  : (khong co)
  Dem : (khong co)
  Ten : An
```

⚠️ **Quy ước Việt Nam:** họ đứng **đầu**, tên đứng **cuối** — ngược với phương Tây.

💡 Hàm trả về cả một `struct` được — C cho phép trả `struct` theo giá trị (khác với mảng). Điều kiện `h.ho[0]` đúng khi chuỗi **không rỗng**.

### Bài 3.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Mau: ten.ho@domain
void sinhEmail(const char *hoTen, const char *domain, char *email) {
    char tam[200];
    strncpy(tam, hoTen, sizeof tam - 1);
    tam[sizeof tam - 1] = '\0';
    for (int i = 0; tam[i]; i++) tam[i] = (char)tolower((unsigned char)tam[i]);

    char *tu[20];
    int n = 0;
    for (char *t = strtok(tam, " \t\n"); t != NULL && n < 20; t = strtok(NULL, " \t\n"))
        tu[n++] = t;

    if (n == 0)      email[0] = '\0';
    else if (n == 1) sprintf(email, "%s@%s", tu[0], domain);
    else             sprintf(email, "%s.%s@%s", tu[n - 1], tu[0], domain);
}

int main(void) {
    const char *ds[] = {"Nguyen Van An", "TRAN THI BINH", "Le Hoang Cuong"};
    char email[200];

    for (int i = 0; i < 3; i++) {
        sinhEmail(ds[i], "gmail.com", email);
        printf("%s  ->  %s\n", ds[i], email);
    }

    printf("\nVoi domain khac:\n");
    sinhEmail("Nguyen Van An", "company.vn", email);
    printf("%s\n", email);
    return 0;
}
```

Output:

```
Nguyen Van An  ->  an.nguyen@gmail.com
TRAN THI BINH  ->  binh.tran@gmail.com
Le Hoang Cuong  ->  cuong.le@gmail.com

Voi domain khac:
an.nguyen@company.vn
```

💡 C không có đối số mặc định, nên `domain` phải được truyền ở mọi lần gọi. `sprintf` giúp ghép nhiều mẩu chuỗi theo mẫu chỉ trong một lệnh.

### Bài 4.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool emailHopLe(const char *email) {
    if (email[0] == '\0') return false;

    // (1) Phai co dung MOT dau @
    const char *at = strchr(email, '@');
    if (at == NULL) return false;
    if (strchr(at + 1, '@') != NULL) return false;

    // (2) Phan truoc @ khong duoc rong
    if (at == email) return false;

    // (3) Phan sau @ phai co dau . va khong o dau/cuoi
    const char *tenMien = at + 1;
    const char *cham = strchr(tenMien, '.');
    if (cham == NULL) return false;
    if (cham == tenMien || tenMien[strlen(tenMien) - 1] == '.') return false;

    // (4) Khong co khoang trang, chi cho phep chu, so va mot so ky tu dac biet
    for (const char *p = email; *p; p++) {
        unsigned char c = (unsigned char)*p;
        if (isspace(c)) return false;
        if (!isalnum(c) && c != '@' && c != '.' && c != '_' && c != '-' && c != '+')
            return false;
    }
    return true;
}

int main(void) {
    const char *ds[] = {
        "an.nguyen@gmail.com",
        "user_123@company.vn",
        "khongcodauat.com",
        "hai@@dau.com",
        "@thieuten.com",
        "thieu@cham",
        "co khoang@trang.com",
        "cuoi@domain."
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    for (int i = 0; i < n; i++)
        printf("%-12s : %s\n", emailHopLe(ds[i]) ? "HOP LE" : "KHONG HOP LE", ds[i]);
    return 0;
}
```

Output:

```
HOP LE       : an.nguyen@gmail.com
HOP LE       : user_123@company.vn
KHONG HOP LE : khongcodauat.com
KHONG HOP LE : hai@@dau.com
KHONG HOP LE : @thieuten.com
KHONG HOP LE : thieu@cham
KHONG HOP LE : co khoang@trang.com
KHONG HOP LE : cuoi@domain.
```

⚠️ **Đây chỉ là kiểm tra cơ bản.** Chuẩn email đầy đủ (RFC 5322) rất phức tạp. Trong ứng dụng thật, cách kiểm tra đáng tin cậy nhất là **gửi email xác nhận**.

💡 `strchr(s, c)` trả về con trỏ tới lần xuất hiện **đầu tiên** của `c`, hoặc `NULL` nếu không có. Tìm tiếp từ `at + 1` để phát hiện dấu `@` thứ hai.

### Bài 5.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char email[200];
    printf("Nhap email: ");
    if (fgets(email, sizeof email, stdin) == NULL) return 0;
    email[strcspn(email, "\n")] = '\0';

    char *at = strchr(email, '@');
    if (at == NULL) {
        printf("Email khong hop le (thieu @)!\n");
        return 1;
    }

    int doDaiTen = (int)(at - email);          // so ky tu truoc @
    const char *tenMien = at + 1;

    printf("Ten nguoi dung : %.*s\n", doDaiTen, email);
    printf("Ten mien       : %s\n", tenMien);

    // Tach tiep phan duoi cua ten mien theo dau . CUOI CUNG
    const char *cham = strrchr(tenMien, '.');
    if (cham != NULL) {
        printf("  Domain       : %.*s\n", (int)(cham - tenMien), tenMien);
        printf("  TLD          : %s\n", cham + 1);
    }
    return 0;
}
```

Với `an.nguyen@mail.company.vn`:

```
Ten nguoi dung : an.nguyen
Ten mien       : mail.company.vn
  Domain       : mail.company
  TLD          : vn
```

💡 **Hiệu hai con trỏ** `at - email` cho biết vị trí của `@`, cũng là độ dài phần tên. `strrchr` tìm lần xuất hiện **cuối cùng** của ký tự.

### Bài 6.

```c
#include <stdio.h>
#include <ctype.h>

// Sua tai cho: xoa moi khoang trang va chuyen ve chu thuong
void chuanHoaEmail(char *s) {
    int k = 0;                              // vi tri ghi
    for (int i = 0; s[i] != '\0'; i++) {    // vi tri doc
        unsigned char c = (unsigned char)s[i];
        if (!isspace(c)) s[k++] = (char)tolower(c);
    }
    s[k] = '\0';
}

int main(void) {
    char ds[][50] = {
        "  An.Nguyen@GMAIL.com  ",
        "USER@Company.VN",
        "a b c@mail.com"
    };

    for (int i = 0; i < 3; i++) {
        printf("[%s]\n", ds[i]);
        chuanHoaEmail(ds[i]);
        printf("  -> [%s]\n", ds[i]);
    }
    return 0;
}
```

Output:

```
[  An.Nguyen@GMAIL.com  ]
  -> [an.nguyen@gmail.com]
[USER@Company.VN]
  -> [user@company.vn]
[a b c@mail.com]
  -> [abc@mail.com]
```

💡 **Vì sao chuẩn hoá email quan trọng:** tên miền **không phân biệt hoa thường** theo chuẩn, nên `User@GMAIL.com` và `user@gmail.com` là **cùng một hộp thư**. Không chuẩn hoá sẽ tạo tài khoản trùng trong cơ sở dữ liệu.

💡 **Kỹ thuật hai chỉ số (đọc `i`, ghi `k`):** chỉ chép lại các ký tự cần giữ về đầu mảng, rồi đặt `'\0'` tại `k`. Xoá ký tự trong O(n) mà không cần mảng phụ.

💡 Mảng `char ds[][50]` chứa bản sao **sửa được** của các chuỗi, khác với mảng con trỏ `const char *ds[]` trỏ tới chuỗi hằng.

### Bài 7.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Mau: TEN + chu cai dau cua cac tu con lai
void sinhTenDangNhap(const char *hoTen, char *kq) {
    char tam[200];
    strncpy(tam, hoTen, sizeof tam - 1);
    tam[sizeof tam - 1] = '\0';
    for (int i = 0; tam[i]; i++) tam[i] = (char)tolower((unsigned char)tam[i]);

    char *tu[20];
    int n = 0;
    for (char *t = strtok(tam, " \t\n"); t != NULL && n < 20; t = strtok(NULL, " \t\n"))
        tu[n++] = t;

    kq[0] = '\0';
    if (n == 0) return;

    strcpy(kq, tu[n - 1]);
    int len = (int)strlen(kq);
    for (int i = 0; i < n - 1; i++) kq[len++] = tu[i][0];
    kq[len] = '\0';
}

int main(void) {
    const char *ds[] = {
        "Nguyen Van An",
        "Tran Thi Minh Chau",
        "Le Cuong",
        "Pham Hoang Minh Duc"
    };
    char kq[100];

    for (int i = 0; i < 4; i++) {
        sinhTenDangNhap(ds[i], kq);
        printf("%s  ->  %s\n", ds[i], kq);
    }
    return 0;
}
```

Output:

```
Nguyen Van An  ->  annv
Tran Thi Minh Chau  ->  chauttm
Le Cuong  ->  cuongl
Pham Hoang Minh Duc  ->  ducphm
```

💡 Đây là quy ước đặt tên đăng nhập phổ biến ở nhiều công ty Việt Nam.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>

void cheEmail(const char *email, char *kq) {
    const char *at = strchr(email, '@');
    if (at == NULL) { strcpy(kq, email); return; }

    int n = (int)(at - email);              // do dai phan ten nguoi dung
    int k = 0;

    if (n <= 4) {
        // Qua ngan -> giu 1 ky tu dau, che phan con lai
        kq[k++] = email[0];
        for (int i = 1; i < n; i++) kq[k++] = '*';
    } else {
        // Giu 3 ky tu dau + 2 ky tu cuoi
        for (int i = 0; i < n; i++)
            kq[k++] = (i < 3 || i >= n - 2) ? email[i] : '*';
    }
    strcpy(kq + k, at);                     // noi phan "@ten-mien"
}

void cheSDT(const char *sdt, char *kq) {
    int n = (int)strlen(sdt);
    strcpy(kq, sdt);
    if (n < 6) return;
    for (int i = 3; i < n - 2; i++) kq[i] = '*';
}

int main(void) {
    const char *ds[] = {
        "nguyenvanan@gmail.com",
        "abc@mail.com",
        "a@b.com",
        "verylongusername123@company.vn"
    };
    char kq[100];

    for (int i = 0; i < 4; i++) {
        cheEmail(ds[i], kq);
        printf("%s\n  -> %s\n", ds[i], kq);
    }

    cheSDT("0912345678", kq);
    printf("\nChe SDT: 0912345678 -> %s\n", kq);
    return 0;
}
```

Output:

```
nguyenvanan@gmail.com
  -> ngu******an@gmail.com
abc@mail.com
  -> a**@mail.com
a@b.com
  -> a@b.com
verylongusername123@company.vn
  -> ver**************23@company.vn

Che SDT: 0912345678 -> 091*****78
```

💡 Kỹ thuật này gọi là **data masking**, dùng để hiển thị thông tin nhạy cảm trong giao diện hoặc log mà vẫn giữ được tính nhận diện.

### Bài 9.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

bool sdtHopLe(const char *sdt) {
    // (1) Phai dung 10 ky tu, bat dau bang 0
    if (strlen(sdt) != 10 || sdt[0] != '0') return false;

    // (2) Toan chu so
    for (int i = 0; sdt[i]; i++)
        if (!isdigit((unsigned char)sdt[i])) return false;

    // (3) Dau so hop le (03, 05, 07, 08, 09)
    return strchr("35789", sdt[1]) != NULL;
}

// Kiem tra 3 so dau co nam trong danh sach "032 033 ..." khong
bool coDauSo(const char *sdt, const char *danhSach) {
    char d3[4];
    strncpy(d3, sdt, 3);
    d3[3] = '\0';
    return strstr(danhSach, d3) != NULL;
}

const char *nhaMang(const char *sdt) {
    if (!sdtHopLe(sdt)) return "Khong xac dinh";
    if (coDauSo(sdt, "032 033 034 035 036 037 038 039 086 096 097 098")) return "Viettel";
    if (coDauSo(sdt, "070 076 077 078 079 089 090 093"))                 return "MobiFone";
    if (coDauSo(sdt, "081 082 083 084 085 088 091 094"))                 return "VinaPhone";
    if (coDauSo(sdt, "056 058 092"))                                     return "Vietnamobile";
    if (coDauSo(sdt, "059 099"))                                         return "Gmobile";
    return "Khac";
}

int main(void) {
    const char *ds[] = {"0912345678", "0387654321", "012345678",
                        "09123456789", "1912345678", "091234567a"};

    for (int i = 0; i < 6; i++) {
        printf("%-12s -> %s", ds[i], sdtHopLe(ds[i]) ? "HOP LE  " : "KHONG   ");
        if (sdtHopLe(ds[i])) printf(" (%s)", nhaMang(ds[i]));
        printf("\n");
    }
    return 0;
}
```

Output:

```
0912345678   -> HOP LE   (VinaPhone)
0387654321   -> HOP LE   (Viettel)
012345678    -> KHONG   
09123456789  -> KHONG   
1912345678   -> KHONG   
091234567a   -> KHONG   
```

💡 **Mẹo `strchr("35789", c)`:** kiểm tra `c` có thuộc một tập ký tự hay không chỉ bằng một lệnh. Tương tự, `strstr` tìm đầu số 3 chữ số trong một chuỗi danh sách — gọn hơn chuỗi dài các phép so sánh `strcmp`.

⚠️ Danh sách đầu số nhà mạng có thể thay đổi theo thời gian, chỉ mang tính minh hoạ.

### Bài 10.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

void chuanHoaSDT(const char *s, char *kq) {
    // (1) Chi giu lai CHU SO
    char so[50];
    int k = 0;
    int coPlus = (s[0] == '+');
    for (int i = 0; s[i] != '\0' && k < 49; i++)
        if (isdigit((unsigned char)s[i])) so[k++] = s[i];
    so[k] = '\0';

    // (2) Doi +84 hoac 84 o dau (so 11 chu so) thanh 0
    if ((coPlus || k == 11) && strncmp(so, "84", 2) == 0)
        sprintf(kq, "0%s", so + 2);
    else
        strcpy(kq, so);
}

int main(void) {
    const char *ds[] = {
        "0912 345 678",
        "0912-345-678",
        "+84912345678",
        "84912345678",
        "(091) 234 5678",
        "0912.345.678"
    };
    char kq[50];

    for (int i = 0; i < 6; i++) {
        chuanHoaSDT(ds[i], kq);
        printf("[%s]  ->  [%s]\n", ds[i], kq);
    }
    return 0;
}
```

Output:

```
[0912 345 678]  ->  [0912345678]
[0912-345-678]  ->  [0912345678]
[+84912345678]  ->  [0912345678]
[84912345678]  ->  [0912345678]
[(091) 234 5678]  ->  [0912345678]
[0912.345.678]  ->  [0912345678]
```

💡 **Nguyên tắc chuẩn hoá:** lọc bỏ mọi ký tự trang trí, chỉ giữ dữ liệu thật, rồi đưa về **một định dạng chuẩn duy nhất**. Điều này rất quan trọng khi lưu vào cơ sở dữ liệu — nếu không, cùng một số điện thoại sẽ được lưu dưới nhiều dạng khác nhau.

💡 `strncmp(so, "84", 2)` so sánh đúng **2 ký tự đầu**. `so + 2` là con trỏ tới phần chuỗi bỏ đi 2 ký tự đầu.

### Bài 11.

```c
#include <stdio.h>
#include <string.h>

void dinhDangSDT(const char *sdt, char *kq) {
    if (strlen(sdt) != 10) { strcpy(kq, sdt); return; }
    // %.4s in toi da 4 ky tu dau cua chuoi
    sprintf(kq, "%.4s %.3s %.3s", sdt, sdt + 4, sdt + 7);
}

void dinhDangQuocTe(const char *sdt, char *kq) {
    if (strlen(sdt) != 10 || sdt[0] != '0') { strcpy(kq, sdt); return; }
    sprintf(kq, "+84 %.3s %.3s %.3s", sdt + 1, sdt + 4, sdt + 7);
}

int main(void) {
    const char *ds[] = {"0912345678", "0387654321"};
    char a[30], b[30];

    for (int i = 0; i < 2; i++) {
        dinhDangSDT(ds[i], a);
        dinhDangQuocTe(ds[i], b);
        printf("Goc       : %s\n", ds[i]);
        printf("Trong nuoc: %s\n", a);
        printf("Quoc te   : %s\n\n", b);
    }
    return 0;
}
```

Output:

```
Goc       : 0912345678
Trong nuoc: 0912 345 678
Quoc te   : +84 912 345 678

Goc       : 0387654321
Trong nuoc: 0387 654 321
Quoc te   : +84 387 654 321
```

💡 **`%.Ns` với con trỏ dịch chuyển** (`sdt + 4`) là cách lấy chuỗi con trong C mà không cần chép ra mảng riêng.

### Bài 12.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

#define MAX_SV 100

void taoEmailGoc(const char *hoTen, char *kq) {
    char tam[200];
    strncpy(tam, hoTen, sizeof tam - 1);
    tam[sizeof tam - 1] = '\0';
    for (int i = 0; tam[i]; i++) tam[i] = (char)tolower((unsigned char)tam[i]);

    char *tu[20];
    int n = 0;
    for (char *t = strtok(tam, " \t\n"); t != NULL && n < 20; t = strtok(NULL, " \t\n"))
        tu[n++] = t;

    kq[0] = '\0';
    if (n == 0) return;
    strcpy(kq, tu[n - 1]);
    int len = (int)strlen(kq);
    for (int i = 0; i < n - 1; i++) kq[len++] = tu[i][0];
    kq[len] = '\0';
}

bool daDung(char ds[][60], int n, const char *email) {
    for (int i = 0; i < n; i++)
        if (strcmp(ds[i], email) == 0) return true;
    return false;
}

int main(void) {
    const char *ds[] = {
        "Nguyen Van An",
        "Nguyen Van An",             // TRUNG
        "Nguyen Viet An",            // cung sinh ra "annv"
        "Tran Thi Binh",
        "Nguyen Van An"              // TRUNG lan 3
    };
    int soSV = sizeof(ds) / sizeof(ds[0]);

    const char *DOMAIN = "@company.vn";
    char daCap[MAX_SV][60];          // cac email da cap
    int soDaCap = 0;

    printf("+----------------------+----------------------------+\n");
    printf("| HO TEN               | EMAIL                      |\n");
    printf("+----------------------+----------------------------+\n");

    for (int i = 0; i < soSV; i++) {
        char goc[50], email[60], day[80];
        taoEmailGoc(ds[i], goc);
        strcpy(email, goc);

        // Neu trung -> them so vao cuoi
        int soThu = 1;
        while (daDung(daCap, soDaCap, email)) {
            soThu++;
            snprintf(email, sizeof email, "%s%d", goc, soThu);
        }
        if (soDaCap < MAX_SV) strcpy(daCap[soDaCap++], email);

        snprintf(day, sizeof day, "%s%s", email, DOMAIN);
        printf("| %-20s | %-26s |\n", ds[i], day);
    }
    printf("+----------------------+----------------------------+\n");
    return 0;
}
```

Output:

```
+----------------------+----------------------------+
| HO TEN               | EMAIL                      |
+----------------------+----------------------------+
| Nguyen Van An        | annv@company.vn            |
| Nguyen Van An        | annv2@company.vn           |
| Nguyen Viet An       | annv3@company.vn           |
| Tran Thi Binh        | binhtt@company.vn          |
| Nguyen Van An        | annv4@company.vn           |
+----------------------+----------------------------+
```

💡 **"Nguyen Viet An" cũng sinh ra `annv`** (chữ đầu của "Viet" cũng là `v`), nên bị đánh số `annv3`. Đây là lý do mọi hệ thống cấp email tự động đều phải kiểm tra trùng.

💡 C không có `set`, nên ở đây kiểm tra trùng bằng **tìm kiếm tuyến tính** trong mảng `daCap` — O(n) mỗi lần. Với danh sách lớn, có thể sắp xếp mảng và dùng tìm kiếm nhị phân (`bsearch`) hoặc bảng băm.

### Bài 13.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdbool.h>

typedef struct {
    bool hopLe;
    int diemManh;                  // 0-5
    char loi[6][80];               // toi da 6 thong bao loi
    int soLoi;
} KetQua;

void themLoi(KetQua *kq, const char *thongBao) {
    if (kq->soLoi < 6) {
        strncpy(kq->loi[kq->soLoi], thongBao, 79);
        kq->loi[kq->soLoi][79] = '\0';
        kq->soLoi++;
    }
    kq->hopLe = false;
}

KetQua kiemTraMatKhau(const char *mk) {
    KetQua kq = {true, 0, {{0}}, 0};
    size_t len = strlen(mk);

    if (len < 8) {
        char tb[80];
        snprintf(tb, sizeof tb, "Phai co it nhat 8 ky tu (hien co %zu)", len);
        themLoi(&kq, tb);
    } else {
        kq.diemManh++;
        if (len >= 12) kq.diemManh++;          // diem thuong cho do dai
    }

    bool coHoa = false, coThuong = false, coSo = false, coDacBiet = false;
    for (size_t i = 0; i < len; i++) {
        unsigned char c = (unsigned char)mk[i];
        if      (isupper(c)) coHoa     = true;
        else if (islower(c)) coThuong  = true;
        else if (isdigit(c)) coSo      = true;
        else if (isprint(c)) coDacBiet = true;
    }

    if (!coHoa)     themLoi(&kq, "Thieu chu HOA");        else kq.diemManh++;
    if (!coThuong)  themLoi(&kq, "Thieu chu thuong");     else kq.diemManh++;
    if (!coSo)      themLoi(&kq, "Thieu chu so");         else kq.diemManh++;
    if (!coDacBiet) themLoi(&kq, "Thieu ky tu dac biet");

    // Kiem tra mat khau pho bien
    const char *YEU[] = {"password", "12345678", "qwerty", "admin123"};
    char thuong[200];
    strncpy(thuong, mk, sizeof thuong - 1);
    thuong[sizeof thuong - 1] = '\0';
    for (int i = 0; thuong[i]; i++) thuong[i] = (char)tolower((unsigned char)thuong[i]);
    for (int i = 0; i < 4; i++)
        if (strstr(thuong, YEU[i]) != NULL) {
            char tb[80];
            snprintf(tb, sizeof tb, "Chua chuoi pho bien de doan: \"%s\"", YEU[i]);
            themLoi(&kq, tb);
        }

    if (kq.diemManh > 5) kq.diemManh = 5;
    return kq;
}

int main(void) {
    const char *ds[] = {"abc", "abcdefgh", "Abcdefg1", "Abcdef1!", "MyP@ssw0rd2026", "Password123!"};

    for (int i = 0; i < 6; i++) {
        KetQua kq = kiemTraMatKhau(ds[i]);
        printf("\"%s\"\n", ds[i]);
        printf("  Do manh: [");
        for (int j = 0; j < 5; j++) printf("%c", j < kq.diemManh ? '#' : '-');
        printf("] %d/5\n", kq.diemManh);
        printf("  Ket qua: %s\n", kq.hopLe ? "HOP LE" : "KHONG HOP LE");
        for (int j = 0; j < kq.soLoi; j++) printf("    - %s\n", kq.loi[j]);
        printf("\n");
    }
    return 0;
}
```

💡 Hàm `themLoi` nhận **con trỏ** `KetQua *kq` để sửa được struct của hàm gọi; truy cập trường qua con trỏ bằng toán tử `->`.

⚠️ **Trong ứng dụng thật, KHÔNG BAO GIỜ lưu mật khẩu dạng văn bản thuần.** Phải lưu **hash** với thuật toán chuyên dụng (bcrypt, argon2, scrypt) kèm salt.

### Bài 14.

```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

typedef struct { const char *vietTat; const char *dayDu; } CapTu;

// Bang thay the cac tu viet tat (so sanh voi ban chu thuong cua tu)
static const CapTu VIET_TAT[] = {
    {"tp",    "TP"},     {"tp.",  "TP"},
    {"q",     "Quan"},   {"q.",   "Quan"},
    {"p",     "Phuong"}, {"p.",   "Phuong"},
    {"h",     "Huyen"},  {"h.",   "Huyen"},
    {"t",     "Tinh"},   {"t.",   "Tinh"},
    {"tx",    "Thi xa"}, {"tx.",  "Thi xa"},
    {"d.",    "Duong"},
    {"hcm",   "Ho Chi Minh"},
    {"hn",    "Ha Noi"}
};
static const int SO_CAP = sizeof(VIET_TAT) / sizeof(VIET_TAT[0]);

void chuanHoaDiaChi(const char *s, char *kq) {
    char tam[300];
    strncpy(tam, s, sizeof tam - 1);
    tam[sizeof tam - 1] = '\0';

    kq[0] = '\0';
    for (char *t = strtok(tam, " \t\n"); t != NULL; t = strtok(NULL, " \t\n")) {
        for (int i = 0; t[i]; i++) t[i] = (char)tolower((unsigned char)t[i]);

        const char *thay = NULL;
        for (int i = 0; i < SO_CAP; i++)
            if (strcmp(t, VIET_TAT[i].vietTat) == 0) { thay = VIET_TAT[i].dayDu; break; }

        if (kq[0] != '\0') strcat(kq, " ");
        if (thay != NULL) {
            strcat(kq, thay);
        } else {
            // Viet hoa chu cai dau, con lai thuong
            t[0] = (char)toupper((unsigned char)t[0]);
            strcat(kq, t);
        }
    }
}

int main(void) {
    const char *ds[] = {
        "  123 nguyen trai, q. 1, tp. hcm  ",
        "45 LE LOI, P. BEN NGHE, Q 1, TP HCM",
        "so 7 duong lang, h. tu liem, hn"
    };
    char kq[300];

    for (int i = 0; i < 3; i++) {
        chuanHoaDiaChi(ds[i], kq);
        printf("[%s]\n  -> [%s]\n\n", ds[i], kq);
    }
    return 0;
}
```

Output:

```
[  123 nguyen trai, q. 1, tp. hcm  ]
  -> [123 Nguyen Trai, Quan 1, TP Ho Chi Minh]

[45 LE LOI, P. BEN NGHE, Q 1, TP HCM]
  -> [45 Le Loi, Phuong Ben Nghe, Quan 1, TP Ho Chi Minh]

[so 7 duong lang, h. tu liem, hn]
  -> [So 7 Duong Lang, Huyen Tu Liem, Ha Noi]
```

💡 **Bảng tra cứu bằng mảng `struct`** (C không có kiểu `map` dựng sẵn): mỗi phần tử là một cặp (viết tắt, đầy đủ), tìm bằng vòng lặp + `strcmp`.

⚠️ Bản trên chỉ nhận dạng từ viết tắt **đứng riêng** (cách nhau bởi dấu cách). Dạng dính liền như `"q.1"`, `"tp.hcm"` cần tách thêm theo dấu `.`. Chuẩn hoá địa chỉ thật sự rất phức tạp (phụ thuộc quy ước hành chính, dấu tiếng Việt, đơn vị hành chính thay đổi) — đây chỉ minh hoạ nguyên lý.

### Bài 15.

**File `chuanhoa.h`:**

```c
#ifndef CHUANHOA_H
#define CHUANHOA_H

#include <stdbool.h>

/* Cac ham ghi ket qua vao mang kq do nguoi goi cap (du lon, vd 200 byte). */

/** Chuan hoa ho ten: xoa khoang trang thua, viet hoa chu cai dau moi tu. */
void chuanHoaTen(const char *s, char *kq);

/** Sinh email tu ho ten theo mau ten.ho@domain. */
void sinhEmail(const char *hoTen, const char *domain, char *kq);

/** Sinh ten dang nhap: ten + chu cai dau cac tu con lai. */
void sinhTenDangNhap(const char *hoTen, char *kq);

/** Kiem tra email co dung dinh dang co ban khong. */
bool kiemTraEmail(const char *email);

/** Chuan hoa email tai cho: xoa khoang trang, chuyen ve chu thuong. */
void chuanHoaEmail(char *s);

/** Che mot phan email de bao mat. */
void cheEmail(const char *email, char *kq);

/** Chuan hoa so dien thoai VN: bo ky tu trang tri, doi +84 thanh 0. */
void chuanHoaSDT(const char *s, char *kq);

/** Kiem tra so dien thoai VN hop le (10 so, dau so dung). */
bool kiemTraSDT(const char *sdt);

/** Dinh dang so dien thoai thanh 0xxx xxx xxx. */
void dinhDangSDT(const char *sdt, char *kq);

/** Ket qua kiem tra mat khau. */
typedef struct {
    bool hopLe;
    int  doManh;                  /* 0-5 */
    char loi[5][40];
    int  soLoi;
} KetQuaMatKhau;

/** Kiem tra do manh cua mat khau. */
KetQuaMatKhau kiemTraMatKhau(const char *mk);

#endif
```

**File `chuanhoa.c`:**

```c
#include "chuanhoa.h"
#include <stdio.h>
#include <string.h>
#include <ctype.h>

/* Tach tu vao mang con tro tu[], tro vao ben trong mang tam. Tra ve so tu. */
static int tachTu(const char *s, char *tam, size_t kichThuoc, char *tu[], int toiDa) {
    strncpy(tam, s, kichThuoc - 1);
    tam[kichThuoc - 1] = '\0';
    for (int i = 0; tam[i]; i++) tam[i] = (char)tolower((unsigned char)tam[i]);

    int n = 0;
    for (char *t = strtok(tam, " \t\n"); t != NULL && n < toiDa; t = strtok(NULL, " \t\n"))
        tu[n++] = t;
    return n;
}

void chuanHoaTen(const char *s, char *kq) {
    char tam[200], *tu[20];
    int n = tachTu(s, tam, sizeof tam, tu, 20);
    kq[0] = '\0';
    for (int i = 0; i < n; i++) {
        tu[i][0] = (char)toupper((unsigned char)tu[i][0]);
        if (i > 0) strcat(kq, " ");
        strcat(kq, tu[i]);
    }
}

void sinhEmail(const char *hoTen, const char *domain, char *kq) {
    char tam[200], *tu[20];
    int n = tachTu(hoTen, tam, sizeof tam, tu, 20);
    if (n == 0)      kq[0] = '\0';
    else if (n == 1) sprintf(kq, "%s@%s", tu[0], domain);
    else             sprintf(kq, "%s.%s@%s", tu[n - 1], tu[0], domain);
}

void sinhTenDangNhap(const char *hoTen, char *kq) {
    char tam[200], *tu[20];
    int n = tachTu(hoTen, tam, sizeof tam, tu, 20);
    kq[0] = '\0';
    if (n == 0) return;
    strcpy(kq, tu[n - 1]);
    int len = (int)strlen(kq);
    for (int i = 0; i < n - 1; i++) kq[len++] = tu[i][0];
    kq[len] = '\0';
}

bool kiemTraEmail(const char *email) {
    const char *at = strchr(email, '@');
    if (at == NULL || at == email || strchr(at + 1, '@') != NULL) return false;

    const char *mien = at + 1;
    const char *cham = strchr(mien, '.');
    if (cham == NULL || cham == mien || mien[strlen(mien) - 1] == '.') return false;

    for (const char *p = email; *p; p++) {
        unsigned char c = (unsigned char)*p;
        if (!isalnum(c) && c != '@' && c != '.' && c != '_' && c != '-' && c != '+')
            return false;                   /* bao gom ca khoang trang */
    }
    return true;
}

void chuanHoaEmail(char *s) {
    int k = 0;
    for (int i = 0; s[i]; i++) {
        unsigned char c = (unsigned char)s[i];
        if (!isspace(c)) s[k++] = (char)tolower(c);
    }
    s[k] = '\0';
}

void cheEmail(const char *email, char *kq) {
    const char *at = strchr(email, '@');
    if (at == NULL) { strcpy(kq, email); return; }

    int n = (int)(at - email), k = 0;
    for (int i = 0; i < n; i++) {
        bool giu = (n <= 4) ? (i == 0) : (i < 3 || i >= n - 2);
        kq[k++] = giu ? email[i] : '*';
    }
    strcpy(kq + k, at);
}

void chuanHoaSDT(const char *s, char *kq) {
    char so[50];
    int k = 0;
    for (int i = 0; s[i] && k < 49; i++)
        if (isdigit((unsigned char)s[i])) so[k++] = s[i];
    so[k] = '\0';

    if ((s[0] == '+' || k == 11) && strncmp(so, "84", 2) == 0)
        sprintf(kq, "0%s", so + 2);
    else
        strcpy(kq, so);
}

bool kiemTraSDT(const char *sdt) {
    if (strlen(sdt) != 10 || sdt[0] != '0') return false;
    for (int i = 0; sdt[i]; i++)
        if (!isdigit((unsigned char)sdt[i])) return false;
    return strchr("35789", sdt[1]) != NULL;
}

void dinhDangSDT(const char *sdt, char *kq) {
    if (strlen(sdt) != 10) { strcpy(kq, sdt); return; }
    sprintf(kq, "%.4s %.3s %.3s", sdt, sdt + 4, sdt + 7);
}

static void themLoi(KetQuaMatKhau *kq, const char *tb) {
    if (kq->soLoi < 5) {
        strncpy(kq->loi[kq->soLoi], tb, 39);
        kq->loi[kq->soLoi][39] = '\0';
        kq->soLoi++;
    }
    kq->hopLe = false;
}

KetQuaMatKhau kiemTraMatKhau(const char *mk) {
    KetQuaMatKhau kq = {true, 0, {{0}}, 0};
    size_t len = strlen(mk);

    if (len < 8) themLoi(&kq, "Phai co it nhat 8 ky tu");
    else {
        kq.doManh++;
        if (len >= 12) kq.doManh++;
    }

    bool hoa = false, thuong = false, so = false, dacBiet = false;
    for (size_t i = 0; i < len; i++) {
        unsigned char c = (unsigned char)mk[i];
        if      (isupper(c)) hoa     = true;
        else if (islower(c)) thuong  = true;
        else if (isdigit(c)) so      = true;
        else if (isprint(c)) dacBiet = true;
    }

    if (!hoa)     themLoi(&kq, "Thieu chu HOA");        else kq.doManh++;
    if (!thuong)  themLoi(&kq, "Thieu chu thuong");     else kq.doManh++;
    if (!so)      themLoi(&kq, "Thieu chu so");         else kq.doManh++;
    if (!dacBiet) themLoi(&kq, "Thieu ky tu dac biet");

    if (kq.doManh > 5) kq.doManh = 5;
    return kq;
}
```

**File `main.c` — kiểm thử:**

```c
#include <stdio.h>
#include "chuanhoa.h"

int main(void) {
    const char *ten = "  nGuYen   vAN   an  ";
    char kq[200], kq2[200];

    printf("=== CHUAN HOA TEN ===\n");
    chuanHoaTen(ten, kq);
    printf("Goc          : [%s]\n", ten);
    printf("Chuan hoa    : [%s]\n", kq);
    sinhEmail(kq, "company.vn", kq2);
    printf("Email        : %s\n", kq2);
    sinhTenDangNhap(ten, kq2);
    printf("Ten dang nhap: %s\n", kq2);

    printf("\n=== EMAIL ===\n");
    char e[] = "  An.Nguyen@GMAIL.com  ";
    printf("Goc       : [%s]\n", e);
    chuanHoaEmail(e);
    printf("Chuan hoa : %s\n", e);
    printf("Hop le    : %s\n", kiemTraEmail(e) ? "true" : "false");
    cheEmail(e, kq);
    printf("Che       : %s\n", kq);

    printf("\n=== SO DIEN THOAI ===\n");
    const char *dsSDT[] = {"0912 345 678", "+84912345678", "(091) 234-5678"};
    for (int i = 0; i < 3; i++) {
        char nhan[40];
        chuanHoaSDT(dsSDT[i], kq);
        dinhDangSDT(kq, kq2);
        snprintf(nhan, sizeof nhan, "[%s]", dsSDT[i]);
        printf("%-18s -> %s  %s  %s\n", nhan, kq,
               kiemTraSDT(kq) ? "HOP LE" : "KHONG", kq2);
    }

    printf("\n=== MAT KHAU ===\n");
    const char *dsMK[] = {"abc", "Abcdef1!", "MyP@ssw0rd2026"};
    for (int i = 0; i < 3; i++) {
        KetQuaMatKhau r = kiemTraMatKhau(dsMK[i]);
        char nhan[40];
        snprintf(nhan, sizeof nhan, "\"%s\"", dsMK[i]);
        printf("%-18s [", nhan);
        for (int j = 0; j < 5; j++) printf("%c", j < r.doManh ? '#' : '-');
        printf("] %s\n", r.hopLe ? "HOP LE" : "YEU");
        for (int j = 0; j < r.soLoi; j++) printf("      - %s\n", r.loi[j]);
    }
    return 0;
}
```

**Biên dịch:**

```bash
gcc -std=c11 -Wall main.c chuanhoa.c -o chuanhoa
./chuanhoa
```

Output:

```
=== CHUAN HOA TEN ===
Goc          : [  nGuYen   vAN   an  ]
Chuan hoa    : [Nguyen Van An]
Email        : an.nguyen@company.vn
Ten dang nhap: annv

=== EMAIL ===
Goc       : [  An.Nguyen@GMAIL.com  ]
Chuan hoa : an.nguyen@gmail.com
Hop le    : true
Che       : an.****en@gmail.com

=== SO DIEN THOAI ===
[0912 345 678]     -> 0912345678  HOP LE  0912 345 678
[+84912345678]     -> 0912345678  HOP LE  0912 345 678
[(091) 234-5678]   -> 0912345678  HOP LE  0912 345 678

=== MAT KHAU ===
"abc"              [#----] YEU
      - Phai co it nhat 8 ky tu
      - Thieu chu HOA
      - Thieu chu so
      - Thieu ky tu dac biet
"Abcdef1!"         [####-] HOP LE
"MyP@ssw0rd2026"   [#####] HOP LE
```

💡 **Tách thư viện thành `.h` + `.c`:** file `.h` chỉ chứa **khai báo** (nguyên mẫu hàm, kiểu `struct`) được bảo vệ bằng include guard `#ifndef ... #define ... #endif`; file `.c` chứa phần cài đặt. Hàm `static` (như `tachTu`, `themLoi`) chỉ dùng được **bên trong** file `chuanhoa.c`.
