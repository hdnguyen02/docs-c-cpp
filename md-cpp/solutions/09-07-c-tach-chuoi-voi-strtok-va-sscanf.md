# Lời giải — [C]. Tách Chuỗi Với strtok Và sscanf

[← Quay lại bài học](../09-07-c-tach-chuoi-voi-strtok-va-sscanf.md)

> **`strtok` (thư viện `<string.h>`) tách chuỗi thành các từ** — gọi lần đầu với chuỗi, các lần sau với `NULL`, và nó **sửa chuỗi gốc**. **`sscanf` (thư viện `<stdio.h>`) đọc dữ liệu có định dạng từ chuỗi** giống `scanf`, không sửa chuỗi, trả về số biến đọc thành công.

---

### Bài 1.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char dong[1000];
    printf("Nhap cac so cach nhau boi dau cach: ");
    if (fgets(dong, sizeof dong, stdin) == NULL) return 0;

    int ds[500];
    int n = 0;

    // Tach theo dau cach, tab va ky tu xuong dong do fgets de lai
    char *tok = strtok(dong, " \t\n");
    while (tok != NULL && n < 500) {
        ds[n++] = atoi(tok);
        tok = strtok(NULL, " \t\n");
    }

    printf("Da doc %d so: ", n);
    long long tong = 0;
    for (int i = 0; i < n; i++) {
        printf("%d ", ds[i]);
        tong += ds[i];
    }
    printf("\nTong = %lld\n", tong);
    return 0;
}
```

💡 Đưa `'\n'` vào danh sách phân cách là cách gọn để khỏi phải xoá ký tự xuống dòng mà `fgets` để lại.

⚠️ `atoi` trả về `0` khi gặp chữ, không báo lỗi. Muốn kiểm tra chặt hơn thì dùng `strtol` hoặc `sscanf` (xem bài 4).

### Bài 2.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char cau[500];
    printf("Nhap mot cau: ");
    if (fgets(cau, sizeof cau, stdin) == NULL) return 0;

    int dem = 0;
    char *tu = strtok(cau, " \t\n");
    while (tu != NULL) {
        dem++;
        printf("  %d. %s\n", dem, tu);
        tu = strtok(NULL, " \t\n");
    }

    printf("So tu: %d\n", dem);
    return 0;
}
```

💡 `strtok` **bỏ qua mọi dấu phân cách liên tiếp** (nhiều dấu cách, tab...) — nên đếm từ chính xác mà không cần xử lý gì thêm.

⚠️ Sau khi tách, mảng `cau` đã bị chèn các ký tự `'\0'`. Muốn dùng lại câu gốc phải chép ra bản sao **trước** khi tách (xem bài 11).

### Bài 3.

```c
#include <stdio.h>
#include <string.h>

// Tach bang strtok: MAT truong rong
void tachStrtok(const char *dong) {
    char s[200];
    strcpy(s, dong);
    int dem = 0;
    printf("  strtok : ");
    for (char *p = strtok(s, ","); p != NULL; p = strtok(NULL, ",")) {
        printf("[%s] ", p);
        dem++;
    }
    printf("-> %d cot\n", dem);
}

// Tu tach bang strchr: GIU truong rong
void tachGiuRong(const char *dong) {
    int dem = 0;
    const char *batDau = dong;
    printf("  strchr : ");
    while (1) {
        const char *phay = strchr(batDau, ',');
        int doDai = phay ? (int)(phay - batDau) : (int)strlen(batDau);
        printf("[%.*s] ", doDai, batDau);     // in doDai ky tu tu batDau
        dem++;
        if (phay == NULL) break;
        batDau = phay + 1;
    }
    printf("-> %d cot\n", dem);
}

int main(void) {
    const char *ds[] = {"An,20,8.5,Ha Noi", "Binh,,7.0,"};

    for (int i = 0; i < 2; i++) {
        printf("Dong: %s\n", ds[i]);
        tachStrtok(ds[i]);
        tachGiuRong(ds[i]);
    }
    return 0;
}
```

Output:

```
Dong: An,20,8.5,Ha Noi
  strtok : [An] [20] [8.5] [Ha Noi] -> 4 cot
  strchr : [An] [20] [8.5] [Ha Noi] -> 4 cot
Dong: Binh,,7.0,
  strtok : [Binh] [7.0] -> 2 cot
  strchr : [Binh] [] [7.0] [] -> 4 cot
```

💡 **Khác biệt quan trọng giữa hai cách:**

| | `strtok` | Tự tách bằng `strchr` |
|---|---|---|
| Nhiều dấu phân cách liền nhau | Gộp làm một | Mỗi dấu là một ranh giới |
| Trường rỗng | ❌ Bị bỏ qua | ✅ **Giữ lại** |
| Sửa chuỗi gốc | Có | Không |

Với CSV, trường rỗng có ý nghĩa (thiếu dữ liệu) nên không nên dùng `strtok`.

💡 `%.*s` in đúng `doDai` ký tự đầu của chuỗi — tiện để in một đoạn con mà không phải chép ra mảng khác.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    const char *dong = "An 20 8.5";
    char ten[50];
    int tuoi;
    double diem;

    if (sscanf(dong, "%49s %d %lf", ten, &tuoi, &diem) == 3) {
        printf("Ten  : %s\n", ten);
        printf("Tuoi : %d\n", tuoi);
        printf("Diem : %.1f\n", diem);
    } else {
        printf("Dinh dang khong hop le!\n");
    }

    // Truong hop du lieu sai
    const char *dong2 = "Binh abc 7.0";
    int n = sscanf(dong2, "%49s %d %lf", ten, &tuoi, &diem);
    if (n != 3)
        printf("\nDong 2: loi doc, chi doc duoc %d gia tri (tuoi khong phai so)\n", n);
    return 0;
}
```

Output:

```
Ten  : An
Tuoi : 20
Diem : 8.5

Dong 2: loi doc, chi doc duoc 1 gia tri (tuoi khong phai so)
```

💡 **`sscanf` tự chuyển kiểu** theo đặc tả `%d`, `%lf`, `%s` — không cần gọi `atoi`, `atof` thủ công.

💡 Luôn so sánh giá trị trả về với **số biến mong đợi** để phát hiện dữ liệu sai định dạng.

### Bài 5.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool ngayHopLe(int d, int m, int y) {
    int soNgay[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (y < 1 || m < 1 || m > 12 || d < 1) return false;
    bool nhuan = (y % 4 == 0 && y % 100 != 0) || y % 400 == 0;
    if (m == 2 && nhuan) return d <= 29;
    return d <= soNgay[m];
}

int main(void) {
    char s[50];
    printf("Nhap ngay (dd/mm/yyyy): ");
    if (fgets(s, sizeof s, stdin) == NULL) return 0;
    s[strcspn(s, "\n")] = '\0';

    int ngay, thang, nam;
    if (sscanf(s, "%d/%d/%d", &ngay, &thang, &nam) != 3) {
        printf("Sai dinh dang!\n");
        return 1;
    }

    printf("Ngay : %d\n", ngay);
    printf("Thang: %d\n", thang);
    printf("Nam  : %d\n", nam);
    printf("%s\n", ngayHopLe(ngay, thang, nam) ? "Ngay hop le" : "Ngay KHONG hop le");
    return 0;
}
```

Với input `17/09/2026`:

```
Ngay : 17
Thang: 9
Nam  : 2026
Ngay hop le
```

💡 Ký tự `/` trong chuỗi định dạng phải **khớp đúng** với chuỗi nguồn. Cách này dùng được cho mọi định dạng cố định như `"12:30:45"`, `"1.2.3"`.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    const char *s = "1.5 2.25 -3 4e1";
    const char *p = s;
    double x, tong = 0;
    int dadoc, dem = 0;

    while (sscanf(p, "%lf%n", &x, &dadoc) == 1) {
        printf("Doc duoc: %g\n", x);
        tong += x;
        dem++;
        p += dadoc;                    // nhay qua phan da doc
    }

    if (dem > 0)
        printf("Co %d so, trung binh = %.4f\n", dem, tong / dem);
    return 0;
}
```

Output:

```
Doc duoc: 1.5
Doc duoc: 2.25
Doc duoc: -3
Doc duoc: 40
Co 4 so, trung binh = 10.1875
```

💡 `%n` ghi **số ký tự đã xử lý** vào `dadoc` và **không** được tính vào giá trị trả về. Không có `%n`, mỗi lần gọi `sscanf(p, ...)` sẽ lại đọc từ đầu chuỗi.

💡 `%lf` hiểu cả dạng khoa học `4e1` = 40. `%g` in số thực ở dạng gọn nhất.

### Bài 7.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char cau[500];
    printf("Nhap mot cau: ");
    if (fgets(cau, sizeof cau, stdin) == NULL) return 0;

    // Luu con tro toi tung tu (cac tu van nam trong mang cau)
    char *tu[100];
    int n = 0;
    for (char *p = strtok(cau, " \t\n"); p != NULL && n < 100; p = strtok(NULL, " \t\n"))
        tu[n++] = p;

    printf("Dao : ");
    for (int i = n - 1; i >= 0; i--) {
        printf("%s", tu[i]);
        if (i > 0) printf(" ");
    }
    printf("\n");
    return 0;
}
```

Ví dụ:

```
Nhap mot cau: toi hoc lap trinh C
Dao : C trinh lap hoc toi
```

💡 Không cần chép từng từ: mỗi `tu[i]` là con trỏ trỏ vào **bên trong** mảng `cau`, vì `strtok` đã đặt `'\0'` sau mỗi từ. Nhưng vì vậy, mảng `cau` phải còn tồn tại khi dùng `tu[i]`.

⚠️ **Phân biệt với đảo ngược chuỗi:** đảo từ giữ nguyên từng từ (`"toi"` vẫn là `"toi"`), còn đảo chuỗi thì `"toi"` thành `"iot"`.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "Hoc lap trinh C: that thu vi! Ban co dong y, khong? Co; chac chan.";
    const char *delim = " ,.;:!?";

    char *dai = NULL, *ngan = NULL;
    for (char *t = strtok(s, delim); t != NULL; t = strtok(NULL, delim)) {
        size_t len = strlen(t);
        if (dai == NULL  || len > strlen(dai))  dai = t;
        if (ngan == NULL || len < strlen(ngan)) ngan = t;
    }

    if (dai != NULL) {
        printf("Tu dai nhat : %s (%zu ky tu)\n", dai, strlen(dai));
        printf("Tu ngan nhat: %s (%zu ky tu)\n", ngan, strlen(ngan));
    }
    return 0;
}
```

Output:

```
Tu dai nhat : trinh (5 ky tu)
Tu ngan nhat: C (1 ky tu)
```

💡 Khi có nhiều từ dài bằng nhau, điều kiện `>` (không phải `>=`) giữ lại từ **xuất hiện đầu tiên**.

### Bài 9.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    // Du lieu nhieu dong (thuc te co the doc tu ban phim hoac file bang fgets)
    const char *duLieu[] = {
        "An 8.5",
        "Binh 7.0",
        "dong loi",
        "Chi 9.5",
        "",
        "Dung 6.5",
        "Em 8.0"
    };
    int soDong = sizeof(duLieu) / sizeof(duLieu[0]);

    double tong = 0;
    int dem = 0;

    printf("+----------------+--------+\n");
    printf("| HO TEN         |  DIEM  |\n");
    printf("+----------------+--------+\n");
    for (int i = 0; i < soDong; i++) {
        char ten[50];
        double diem;
        if (sscanf(duLieu[i], "%49s %lf", ten, &diem) != 2) continue;   // bo dong sai
        printf("| %-14s | %6.2f |\n", ten, diem);
        tong += diem;
        dem++;
    }
    printf("+----------------+--------+\n");

    if (dem > 0)
        printf("Diem trung binh: %.2f\n", tong / dem);
    return 0;
}
```

Output:

```
+----------------+--------+
| HO TEN         |  DIEM  |
+----------------+--------+
| An             |   8.50 |
| Binh           |   7.00 |
| Chi            |   9.50 |
| Dung           |   6.50 |
| Em             |   8.00 |
+----------------+--------+
Diem trung binh: 7.90
```

💡 **Mẫu "fgets + sscanf"** rất hay dùng khi đọc dữ liệu nhiều dòng:
- `fgets` đọc **cả dòng** vào mảng (an toàn, không tràn)
- `sscanf` tách dòng đó thành **các trường** và báo lỗi nếu sai định dạng

Đọc từ bàn phím chỉ cần thay mảng `duLieu` bằng vòng `while (fgets(dong, sizeof dong, stdin) != NULL)`.

### Bài 10.

```c
#include <stdio.h>

// Tra ve so giay, hoac -1 neu sai dinh dang/gia tri
long chuyenGiay(const char *s) {
    int h, m, sec, dadoc;
    if (sscanf(s, "%d:%d:%d%n", &h, &m, &sec, &dadoc) != 3) return -1;
    if (s[dadoc] != '\0') return -1;                 // con ky tu thua phia sau
    if (h < 0 || h > 23 || m < 0 || m > 59 || sec < 0 || sec > 59) return -1;
    return h * 3600L + m * 60L + sec;
}

int main(void) {
    const char *ds[] = {"12:30:45", "00:00:00", "23:59:59", "12-30-45", "25:00:00", "1:2:3abc"};

    for (int i = 0; i < 6; i++) {
        long giay = chuyenGiay(ds[i]);
        if (giay < 0) printf("%-10s -> KHONG hop le\n", ds[i]);
        else          printf("%-10s -> %ld giay\n", ds[i], giay);
    }
    return 0;
}
```

Output:

```
12:30:45   -> 45045 giay
00:00:00   -> 0 giay
23:59:59   -> 86399 giay
12-30-45   -> KHONG hop le
25:00:00   -> KHONG hop le
1:2:3abc   -> KHONG hop le
```

💡 **Mẹo `%n` ở cuối định dạng:** nếu `s[dadoc]` chưa phải `'\0'` thì chuỗi còn ký tự thừa — `sscanf` bình thường không báo lỗi trường hợp này.

### Bài 11.

```c
#include <stdio.h>
#include <string.h>

void inTungByte(const char *s, int n) {
    for (int i = 0; i < n; i++) {
        if (s[i] == '\0') printf("\\0 ");
        else              printf("%c ", s[i]);
    }
    printf("\n");
}

int main(void) {
    char s[] = "an,binh,chi";
    int n = (int)sizeof(s);                  // 12 byte, tinh ca '\0' cuoi

    printf("Truoc khi tach: ");
    inTungByte(s, n);

    for (char *t = strtok(s, ","); t != NULL; t = strtok(NULL, ","))
        ;                                    // chi tach, khong lam gi

    printf("Sau khi tach  : ");
    inTungByte(s, n);
    printf("printf(\"%%s\", s) bay gio in: %s\n", s);

    // ===== Cach giu chuoi goc: tach tren BAN SAO =====
    char goc[] = "an,binh,chi";
    char banSao[sizeof goc];
    strcpy(banSao, goc);
    for (char *t = strtok(banSao, ","); t != NULL; t = strtok(NULL, ","))
        printf("  tu: %s\n", t);
    printf("Chuoi goc van con: %s\n", goc);
    return 0;
}
```

Output:

```
Truoc khi tach: a n , b i n h , c h i \0 
Sau khi tach  : a n \0 b i n h \0 c h i \0 
printf("%s", s) bay gio in: an
  tu: an
  tu: binh
  tu: chi
Chuoi goc van con: an,binh,chi
```

**Giải thích:** `strtok` ghi đè mỗi dấu phân cách vừa gặp bằng `'\0'`. Vì vậy sau khi tách, `printf("%s", s)` dừng ngay ở `'\0'` đầu tiên và chỉ in `an`.

⚠️ Cũng vì lý do này, gọi `strtok` trên chuỗi hằng (`char *s = "an,binh"`) là **lỗi** — chương trình thường bị crash do ghi vào vùng nhớ chỉ đọc.

### Bài 12.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s[] = "a=1;b=2;c=3";

    // ===== SAI: long hai vong strtok =====
    // for (char *cap = strtok(s, ";"); cap; cap = strtok(NULL, ";")) {
    //     char *ten = strtok(cap, "=");   // strtok quen vi tri cua vong ngoai!
    //     ...
    // }
    // -> strtok(NULL, ";") tiep tuc tach chuoi cap, khong bao gio toi b=2, c=3

    // ===== DUNG: strtok cho ';' + sscanf cho tung cap =====
    for (char *cap = strtok(s, ";"); cap != NULL; cap = strtok(NULL, ";")) {
        char ten[20];
        int giaTri;
        if (sscanf(cap, "%19[^=]=%d", ten, &giaTri) == 2)
            printf("Ten: %-3s Gia tri: %d\n", ten, giaTri);
        else
            printf("Cap sai dinh dang: %s\n", cap);
    }
    return 0;
}
```

Output:

```
Ten: a   Gia tri: 1
Ten: b   Gia tri: 2
Ten: c   Gia tri: 3
```

**Vì sao không lồng được hai vòng `strtok`:** `strtok` chỉ có **một** biến nội bộ ghi nhớ vị trí đang tách. Khi vòng trong gọi `strtok(cap, "=")`, vị trí cũ của vòng ngoài bị ghi đè; lần gọi `strtok(NULL, ";")` tiếp theo sẽ tách tiếp chuỗi `cap` chứ không quay lại chuỗi `s`. Chạy thử bản sai, vòng ngoài chỉ nhận được `"a"` rồi `"1"` và dừng — hai cặp `b=2`, `c=3` bị bỏ sót.

💡 **Đặc tả `%[^=]`** đọc mọi ký tự **cho tới khi gặp `=`** (không bao gồm `=`). `%19[^=]` giới hạn tối đa 19 ký tự để không tràn mảng `ten`.

💡 Một số hệ thống có `strtok_r` (POSIX) hoặc `strtok_s` (tuỳ chọn trong C11) cho phép tách lồng nhau, nhưng đây **không** phải hàm có ở mọi trình biên dịch.

### Bài 13.

```c
#include <stdio.h>
#include <ctype.h>

// Tach tu vao mang 2 chieu, KHONG sua chuoi goc. Tra ve so tu.
int tachTu(const char *s, char tu[][50]) {
    int soTu = 0;
    int i = 0;
    while (s[i] != '\0') {
        while (s[i] != '\0' && isspace((unsigned char)s[i])) i++;   // bo khoang trang
        if (s[i] == '\0') break;

        int k = 0;
        while (s[i] != '\0' && !isspace((unsigned char)s[i])) {
            if (k < 49) tu[soTu][k++] = s[i];                        // chong tran
            i++;
        }
        tu[soTu][k] = '\0';
        soTu++;
    }
    return soTu;
}

int main(void) {
    const char *s = "  hoc   lap\ttrinh  C  co ban ";
    char tu[100][50];

    int n = tachTu(s, tu);
    printf("Tach duoc %d tu:\n", n);
    for (int i = 0; i < n; i++)
        printf("  tu[%d] = \"%s\"\n", i, tu[i]);
    printf("Chuoi goc: \"%s\"\n", s);
    return 0;
}
```

Output:

```
Tach duoc 6 tu:
  tu[0] = "hoc"
  tu[1] = "lap"
  tu[2] = "trinh"
  tu[3] = "C"
  tu[4] = "co"
  tu[5] = "ban"
Chuoi goc: "  hoc   lap	trinh  C  co ban "
```

💡 Tham số `char tu[][50]` là mảng 2 chiều: số hàng tuỳ ý, **mỗi hàng 50 ký tự** — số cột bắt buộc phải ghi rõ.

⚠️ Hàm tin rằng mảng `tu` có đủ hàng; khi dùng thật nên truyền thêm số hàng tối đa để kiểm tra.

### Bài 14.

```c
#include <stdio.h>
#include <string.h>

typedef struct {
    char ten[50];
    int tuoi;
    double diem;
    char thanhPho[30];
} SinhVien;

int main(void) {
    // Du lieu CSV (thuc te doc tu file bang fopen + fgets)
    const char *csv[] = {
        "Ho ten,Tuoi,Diem,Thanh pho",
        "Nguyen Van An,20,8.5,Ha Noi",
        "Tran Thi Binh,22,9.0,TP HCM",
        "Le Hoang Cuong,21,7.5,Da Nang",
        "Pham Minh Dung,23,8.0,Can Tho"
    };
    int soDong = sizeof(csv) / sizeof(csv[0]);

    SinhVien ds[100];
    int n = 0;
    for (int i = 1; i < soDong; i++) {                 // bo dong tieu de
        SinhVien sv;
        // %[^,] doc toi dau phay -> giu duoc ca dau cach trong ten
        if (sscanf(csv[i], "%49[^,],%d,%lf,%29[^\n]",
                   sv.ten, &sv.tuoi, &sv.diem, sv.thanhPho) == 4)
            ds[n++] = sv;
    }

    printf("+----------------+------+------+-----------+\n");
    printf("| %-14s | %-4s | %-4s | %-9s |\n", "Ho ten", "Tuoi", "Diem", "Thanh pho");
    printf("+----------------+------+------+-----------+\n");
    double tong = 0;
    for (int i = 0; i < n; i++) {
        printf("| %-14s | %-4d | %-4.1f | %-9s |\n",
               ds[i].ten, ds[i].tuoi, ds[i].diem, ds[i].thanhPho);
        tong += ds[i].diem;
    }
    printf("+----------------+------+------+-----------+\n");

    if (n > 0) printf("\nDiem trung binh: %.2f\n", tong / n);
    return 0;
}
```

Output:

```
+----------------+------+------+-----------+
| Ho ten         | Tuoi | Diem | Thanh pho |
+----------------+------+------+-----------+
| Nguyen Van An  | 20   | 8.5  | Ha Noi    |
| Tran Thi Binh  | 22   | 9.0  | TP HCM    |
| Le Hoang Cuong | 21   | 7.5  | Da Nang   |
| Pham Minh Dung | 23   | 8.0  | Can Tho   |
+----------------+------+------+-----------+

Diem trung binh: 8.25
```

💡 **Đọc từ file thật:**

```c
FILE *f = fopen("dulieu.csv", "r");
char dong[256];
while (f != NULL && fgets(dong, sizeof dong, f) != NULL) { ... }
if (f != NULL) fclose(f);
```

⚠️ **CSV thật phức tạp hơn:** có thể có dấu phẩy trong ngoặc kép (`"Ha Noi, Viet Nam"`), có dấu nháy thoát. Với dữ liệu thật nên dùng thư viện CSV chuyên dụng.

### Bài 15.

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char bieuThuc[200];
    printf("Nhap bieu thuc (vd: 12 + 34 * 2): ");
    if (fgets(bieuThuc, sizeof bieuThuc, stdin) == NULL) return 0;
    bieuThuc[strcspn(bieuThuc, "\n")] = '\0';

    const char *p = bieuThuc;
    double kq, so;
    char op;
    int dadoc;

    if (sscanf(p, "%lf%n", &kq, &dadoc) != 1) {
        printf("Bieu thuc khong hop le!\n");
        return 1;
    }
    p += dadoc;

    // Tinh TUAN TU tu trai sang phai (khong uu tien toan tu)
    // Dau cach truoc %c de bo qua khoang trang truoc toan tu
    while (sscanf(p, " %c%lf%n", &op, &so, &dadoc) == 2) {
        p += dadoc;
        switch (op) {
            case '+': kq += so; break;
            case '-': kq -= so; break;
            case '*': kq *= so; break;
            case '/':
                if (so == 0) { printf("Loi: chia cho 0!\n"); return 1; }
                kq /= so;
                break;
            default:
                printf("Toan tu '%c' khong hop le!\n", op);
                return 1;
        }
    }

    printf("%s = %g\n", bieuThuc, kq);
    printf("(Tinh tuan tu tu trai sang phai, KHONG uu tien nhan/chia)\n");
    return 0;
}
```

Ví dụ:

```
Nhap bieu thuc (vd: 12 + 34 * 2): 12 + 34 * 2
12 + 34 * 2 = 92
(Tinh tuan tu tu trai sang phai, KHONG uu tien nhan/chia)
```

⚠️ Kết quả là **92** chứ không phải 80, vì chương trình tính `(12 + 34) * 2` thay vì `12 + (34 * 2)`.

💡 **Khác với `%d`, `%lf`, `%s`, đặc tả `%c` không tự bỏ qua khoảng trắng** — phải đặt một dấu cách trước nó (`" %c"`) để bỏ qua các dấu cách trước toán tử.

💡 **Cải tiến — có ưu tiên toán tử** (thuật toán 2 lượt, dùng mảng):

```c
#include <stdio.h>

int main(void) {
    const char *bt = "12 + 34 * 2";
    const char *p = bt;
    double so[100];
    char op[100];
    int nSo = 0, nOp = 0, dadoc;

    if (sscanf(p, "%lf%n", &so[nSo], &dadoc) != 1) return 1;
    nSo++;
    p += dadoc;
    while (nOp < 99 && sscanf(p, " %c%lf%n", &op[nOp], &so[nSo], &dadoc) == 2) {
        nOp++; nSo++; p += dadoc;
    }

    // LUOT 1: xu ly * va / truoc, don mang ve ben trai
    int k = 0;                        // so phep +,- con lai
    double cacSo[100];
    char cacOp[100];
    cacSo[0] = so[0];
    for (int i = 0; i < nOp; i++) {
        if (op[i] == '*')      cacSo[k] *= so[i + 1];
        else if (op[i] == '/') cacSo[k] /= so[i + 1];
        else { cacOp[k] = op[i]; cacSo[++k] = so[i + 1]; }
    }

    // LUOT 2: xu ly + va -
    double kq = cacSo[0];
    for (int i = 0; i < k; i++)
        kq = (cacOp[i] == '+') ? kq + cacSo[i + 1] : kq - cacSo[i + 1];

    printf("%s = %g\n", bt, kq);      // 12 + 34 * 2 = 80
    return 0;
}
```

💡 Để xử lý cả dấu ngoặc, cần thuật toán **Shunting-yard** của Dijkstra hoặc phân tích đệ quy — vượt ngoài phạm vi bài này.
