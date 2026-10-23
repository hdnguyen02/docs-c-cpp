# Lời giải — [C]. Xây Dựng Hàm So Sánh Cho qsort

[← Quay lại bài học](../10-03-c-xay-dung-ham-so-sanh-cho-qsort.md)

> Hàm so sánh của `qsort` có dạng `int cmp(const void *a, const void *b)`: **ép kiểu** con trỏ về đúng kiểu phần tử, rồi trả **số âm** nếu `a` đứng trước, **số dương** nếu `a` đứng sau, **0** nếu tương đương.

---

### Bài 1.

```c
#include <stdio.h>
#include <stdlib.h>

int giamDan(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    if (x > y) return -1;       // x lon hon -> dung TRUOC
    if (x < y) return 1;        // x nho hon -> dung SAU
    return 0;
}

int main(void) {
    int a[] = {5, 2, 9, 1, 7, 3, 9};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), giamDan);     // truyen TEN ham, khong co ()

    for (int i = 0; i < n; i++) printf("%d ", a[i]);   // 9 9 7 5 3 2 1
    printf("\n");
    return 0;
}
```

⚠️ Truyền **tên hàm** (`giamDan`), **không** kèm dấu ngoặc — vì ta truyền chính hàm đó (một con trỏ hàm), không phải kết quả gọi hàm.

💡 Cách viết một dòng tương đương, cũng không dùng phép trừ giữa hai giá trị: `return (x < y) - (x > y);`

### Bài 2.

```c
#include <stdio.h>
#include <stdlib.h>

// SAI: hieu so thuc bi cat phan thap phan khi tra ve int
int cmpSai(const void *a, const void *b) {
    return (int)(*(const double *)a - *(const double *)b);
}

// DUNG
int cmpDouble(const void *a, const void *b) {
    double x = *(const double *)a;
    double y = *(const double *)b;
    if (x < y) return -1;
    if (x > y) return 1;
    return 0;
}

void inMang(const char *nhan, const double a[], int n) {
    printf("%s", nhan);
    for (int i = 0; i < n; i++) printf("%.2f ", a[i]);
    printf("\n");
}

int main(void) {
    double a[] = {0.75, 0.25, 0.5, 0.1, 0.9};
    double b[] = {0.75, 0.25, 0.5, 0.1, 0.9};
    int n = 5;

    qsort(a, n, sizeof(a[0]), cmpSai);
    qsort(b, n, sizeof(b[0]), cmpDouble);

    inMang("return x - y : ", a, n);
    inMang("so sanh if   : ", b, n);
    return 0;
}
```

Output (trên máy mình, dòng thứ nhất có thể khác trên máy bạn):

```
return x - y : 0.75 0.25 0.50 0.10 0.90 
so sanh if   : 0.10 0.25 0.50 0.75 0.90 
```

**Vì sao sai:** mọi hiệu giữa các số trong khoảng `(-1, 1)` khi đổi sang `int` đều thành **0** → `qsort` tưởng mọi phần tử bằng nhau → mảng giữ nguyên thứ tự lộn xộn.

⚠️ Không có `(int)` thì trình biên dịch cũng tự đổi `double` về `int` khi `return` — lỗi y hệt, chỉ là bị giấu đi.

### Bài 3.

```c
#include <stdio.h>
#include <limits.h>

int cmpTru(int x, int y)     { return x - y; }               // co the TRAN SO
int cmpAnToan(int x, int y)  { return (x > y) - (x < y); }   // luon dung

int main(void) {
    int cap[][2] = {{2000000000, -2000000000}, {INT_MIN, 1}, {5, 3}};

    for (int i = 0; i < 3; i++) {
        int x = cap[i][0], y = cap[i][1];
        printf("x = %11d, y = %11d | x - y -> %11d | an toan -> %2d\n",
               x, y, cmpTru(x, y), cmpAnToan(x, y));
    }
    return 0;
}
```

Output (trên máy dùng số bù 2, GCC):

```
x =  2000000000, y = -2000000000 | x - y ->  -294967296 | an toan ->  1
x = -2147483648, y =           1 | x - y ->  2147483647 | an toan -> -1
x =           5, y =           3 | x - y ->           2 | an toan ->  1
```

**Phân tích:**
- Cặp 1: `x > y` nhưng `x - y` = 4.000.000.000 vượt `INT_MAX` → quay vòng thành **số âm** → `qsort` hiểu `x` đứng trước `y`. **Sai.**
- Cặp 2: `x < y` nhưng `INT_MIN - 1` tràn thành `INT_MAX` → **số dương**. **Sai.**
- Cặp 3: số nhỏ, không tràn → đúng. Đây là lý do lỗi này **khó phát hiện**: chạy thử với dữ liệu nhỏ luôn thấy đúng.

⚠️ Tràn số `int` có dấu là **hành vi không xác định** trong C — kết quả trên chỉ là điều thường thấy, không được dựa vào. Với `-fsanitize=undefined`, GCC sẽ báo lỗi ngay khi chạy.

**Sửa:** dùng `(x > y) - (x < y)` hoặc cặp `if` như Bài 1.

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char ten[30];
    int  diem;
} HocSinh;

int theoDiemGiam(const void *a, const void *b) {
    const HocSinh *p = (const HocSinh *)a;
    const HocSinh *q = (const HocSinh *)b;
    return (p->diem < q->diem) - (p->diem > q->diem);    // diem cao truoc
}

int main(void) {
    HocSinh ds[] = {{"An", 85}, {"Binh", 92}, {"Chi", 78}, {"Dung", 95}, {"Em", 65}};
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), theoDiemGiam);

    printf("+----------+-------+\n");
    printf("| TEN      | DIEM  |\n");
    printf("+----------+-------+\n");
    for (int i = 0; i < n; i++)
        printf("| %-8s | %-5d |\n", ds[i].ten, ds[i].diem);
    printf("+----------+-------+\n");
    return 0;
}
```

Output:

```
+----------+-------+
| TEN      | DIEM  |
+----------+-------+
| Dung     | 95    |
| Binh     | 92    |
| An       | 85    |
| Chi      | 78    |
| Em       | 65    |
+----------+-------+
```

💡 `sizeof(ds[0])` là kích thước **cả một struct** (ở đây 36 byte). `qsort` sao chép nguyên khối struct khi đổi chỗ, nên tên đi cùng điểm, không bao giờ bị lệch.

### Bài 5.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char   ten[30];
    int    tuoi;
    double diem;
} SinhVien;

int cmpSV(const void *a, const void *b) {
    const SinhVien *p = (const SinhVien *)a;
    const SinhVien *q = (const SinhVien *)b;

    if (p->diem != q->diem)                                   // (1) diem GIAM
        return (p->diem < q->diem) - (p->diem > q->diem);
    if (p->tuoi != q->tuoi)                                   // (2) tuoi TANG
        return (p->tuoi > q->tuoi) - (p->tuoi < q->tuoi);
    return strcmp(p->ten, q->ten);                            // (3) ten A-Z
}

int main(void) {
    SinhVien ds[] = {
        {"Chi",   21, 9.0}, {"An",   20, 9.0}, {"Binh", 22, 9.0},
        {"Dung",  20, 8.5}, {"Em",   23, 8.5}, {"Phong", 19, 7.0},
        {"Anh",   21, 9.0}
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), cmpSV);

    printf("+------------+------+-------+\n");
    printf("| HO TEN     | TUOI | DIEM  |\n");
    printf("+------------+------+-------+\n");
    for (int i = 0; i < n; i++)
        printf("| %-10s | %4d | %5.1f |\n", ds[i].ten, ds[i].tuoi, ds[i].diem);
    printf("+------------+------+-------+\n");
    return 0;
}
```

Output:

```
+------------+------+-------+
| HO TEN     | TUOI | DIEM  |
+------------+------+-------+
| An         |   20 |   9.0 |
| Anh        |   21 |   9.0 |
| Chi        |   21 |   9.0 |
| Binh       |   22 |   9.0 |
| Dung       |   20 |   8.5 |
| Em         |   23 |   8.5 |
| Phong      |   19 |   7.0 |
+------------+------+-------+
```

💡 **Mẫu hàm so sánh nhiều tiêu chí:**

```c
if (tieuChi1(a) != tieuChi1(b)) return soSanh1(a, b);
if (tieuChi2(a) != tieuChi2(b)) return soSanh2(a, b);
return soSanh3(a, b);                  // tieu chi cuoi cung
```

Chỉ khi tiêu chí trước **bằng nhau** mới xét tiêu chí sau. `strcmp` đã trả về âm/0/dương đúng quy ước nên dùng thẳng được.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

int tongChuSo(int n) {
    long long m = n;                 // long long de abs(INT_MIN) khong tran
    if (m < 0) m = -m;
    int t = 0;
    while (m > 0) { t += (int)(m % 10); m /= 10; }
    return t;
}

int theoTongChuSo(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    int tx = tongChuSo(x), ty = tongChuSo(y);
    if (tx != ty) return (tx > ty) - (tx < ty);   // tong nho truoc
    return (x > y) - (x < y);                      // bang nhau: so nho truoc
}

int main(void) {
    int a[] = {123, -45, 900, 18, -9, 71, 0, 36};
    int n = sizeof(a) / sizeof(a[0]);

    qsort(a, n, sizeof(a[0]), theoTongChuSo);

    for (int i = 0; i < n; i++)
        printf("%5d  (tong chu so = %d)\n", a[i], tongChuSo(a[i]));
    return 0;
}
```

Output:

```
    0  (tong chu so = 0)
  123  (tong chu so = 6)
   71  (tong chu so = 8)
  -45  (tong chu so = 9)
   -9  (tong chu so = 9)
   18  (tong chu so = 9)
   36  (tong chu so = 9)
  900  (tong chu so = 9)
```

⚠️ Với số âm, `-45 % 10` trong C bằng **-5** → phải lấy trị tuyệt đối trước khi tách chữ số.

⚠️ **Vấn đề hiệu năng:** `tongChuSo` được gọi **rất nhiều lần** (mỗi lần so sánh gọi 2 lần, tổng O(n log n) lần). Với `n` lớn, nên **tính trước** tổng chữ số, lưu vào mảng struct `{int giaTri; int tong;}` rồi sắp mảng struct đó.

### Bài 7.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAXLEN 20

int demNguyenAm(const char *s) {
    int dem = 0;
    for (; *s; s++) {
        char t = (char)tolower((unsigned char)*s);
        if (t == 'a' || t == 'e' || t == 'i' || t == 'o' || t == 'u') dem++;
    }
    return dem;
}

int theoNguyenAm(const void *a, const void *b) {
    const char *s1 = (const char *)a;          // mang char[][MAXLEN]
    const char *s2 = (const char *)b;
    int n1 = demNguyenAm(s1), n2 = demNguyenAm(s2);
    if (n1 != n2) return (n1 < n2) - (n1 > n2);   // nhieu nguyen am truoc
    return strcmp(s1, s2);
}

int main(void) {
    char ds[][MAXLEN] = {"programming", "c", "algorithm", "data", "sequence", "xyz"};
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), theoNguyenAm);

    printf("Sap theo so nguyen am (giam dan):\n");
    for (int i = 0; i < n; i++)
        printf("  %s (%d nguyen am)\n", ds[i], demNguyenAm(ds[i]));
    return 0;
}
```

Output:

```
Sap theo so nguyen am (giam dan):
  sequence (4 nguyen am)
  algorithm (3 nguyen am)
  programming (3 nguyen am)
  data (2 nguyen am)
  c (0 nguyen am)
  xyz (0 nguyen am)
```

### Bài 8.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct { int x, y; } Diem;

// qsort KHONG cho truyen them tham so vao ham so sanh
// -> luu diem moc vao bien toan cuc
static Diem moc;

long long binhPhuongKC(Diem p) {
    long long dx = p.x - moc.x, dy = p.y - moc.y;
    return dx * dx + dy * dy;          // so sanh binh phuong, khoi can sqrt
}

int theoKhoangCach(const void *a, const void *b) {
    long long da = binhPhuongKC(*(const Diem *)a);
    long long db = binhPhuongKC(*(const Diem *)b);
    return (da > db) - (da < db);
}

int main(void) {
    Diem ds[] = {{1, 1}, {5, 5}, {-2, 3}, {0, 0}, {3, -1}, {4, 4}};
    int n = sizeof(ds) / sizeof(ds[0]);

    printf("Nhap diem moc (px py): ");
    if (scanf("%d %d", &moc.x, &moc.y) != 2) return 1;

    qsort(ds, n, sizeof(ds[0]), theoKhoangCach);

    printf("Tu gan den xa (%d, %d):\n", moc.x, moc.y);
    for (int i = 0; i < n; i++)
        printf("  (%2d, %2d)  kc^2 = %lld\n", ds[i].x, ds[i].y, binhPhuongKC(ds[i]));
    return 0;
}
```

Ví dụ chạy:

```
Nhap diem moc (px py): 4 4
Tu gan den xa (4, 4):
  ( 4,  4)  kc^2 = 0
  ( 5,  5)  kc^2 = 2
  ( 1,  1)  kc^2 = 18
  ( 3, -1)  kc^2 = 26
  ( 0,  0)  kc^2 = 32
  (-2,  3)  kc^2 = 37
```

💡 **Không cần `sqrt`:** so sánh khoảng cách tương đương so sánh **bình phương** khoảng cách, vừa nhanh vừa tránh sai số số thực.

⚠️ Dùng biến toàn cục nghĩa là hàm so sánh **không dùng song song** được ở nhiều luồng với các mốc khác nhau. Với chương trình học tập đây là cách đơn giản và phổ biến nhất trong C chuẩn.

### Bài 9.

```c
#include <stdio.h>
#include <stdlib.h>

#define LEN 11              // "dd/mm/yyyy" + '\0'

// Doi "dd/mm/yyyy" thanh so yyyymmdd de so sanh mot lan
long doiThanhSo(const char *s) {
    int d = 0, m = 0, y = 0;
    sscanf(s, "%d/%d/%d", &d, &m, &y);
    return (long)y * 10000 + m * 100 + d;
}

int theoThoiGian(const void *a, const void *b) {
    long x = doiThanhSo((const char *)a);
    long y = doiThanhSo((const char *)b);
    return (x > y) - (x < y);
}

int main(void) {
    char ds[][LEN] = {
        "17/09/2026", "01/01/2025", "25/12/2025",
        "17/09/2025", "03/09/2026", "17/03/2026"
    };
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), theoThoiGian);

    printf("Sap xep theo thoi gian:\n");
    for (int i = 0; i < n; i++) printf("  %s\n", ds[i]);
    return 0;
}
```

Output:

```
Sap xep theo thoi gian:
  01/01/2025
  17/09/2025
  25/12/2025
  17/03/2026
  03/09/2026
  17/09/2026
```

⚠️ **Sắp xếp chuỗi `"dd/mm/yyyy"` trực tiếp bằng `strcmp` sẽ SAI** — vì so sánh từ điển bắt đầu từ ngày. `"01/01/2026"` sẽ đứng trước `"25/12/2025"`.

💡 **Mẹo hay:** nếu định dạng là `"yyyy-mm-dd"` (chuẩn ISO 8601) thì **`strcmp` trực tiếp là đúng** — vì thứ tự từ điển trùng với thứ tự thời gian. Đây là lý do nên dùng định dạng này khi lưu trữ.

### Bài 10.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// So sanh chuoi khong phan biet hoa thuong (tu viet, vi strcasecmp khong thuoc C chuan)
int soSanhKhongHoa(const char *s1, const char *s2) {
    while (*s1 && *s2) {
        int c1 = tolower((unsigned char)*s1);
        int c2 = tolower((unsigned char)*s2);
        if (c1 != c2) return c1 - c2;       // ky tu 0..255: hieu khong tran
        s1++;
        s2++;
    }
    return tolower((unsigned char)*s1) - tolower((unsigned char)*s2);
}

// Phan tu cua mang la con tro char -> void* tro toi (const char *)
int cmpKhongHoa(const void *a, const void *b) {
    const char *s1 = *(const char * const *)a;
    const char *s2 = *(const char * const *)b;
    int kq = soSanhKhongHoa(s1, s2);
    if (kq != 0) return kq;
    return strcmp(s1, s2);                   // "Apple" vs "apple": giu thu tu co dinh
}

int main(void) {
    const char *ds[] = {"banana", "Apple", "cherry", "apple", "Banana", "date"};
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), cmpKhongHoa);

    for (int i = 0; i < n; i++) printf("%s ", ds[i]);
    printf("\n");
    return 0;
}
```

Output:

```
Apple apple Banana banana cherry date 
```

💡 Nếu chỉ dùng `strcmp`, mọi chữ **hoa** sẽ đứng trước mọi chữ **thường** (vì mã ASCII `'Z'` = 90 < `'a'` = 97): `Apple Banana apple banana cherry date`.

⚠️ Với mảng con trỏ `char *ds[]`, `void *` trỏ tới **một con trỏ** → phải ép `*(const char * const *)a`. Ép thẳng `(const char *)a` là lỗi hay gặp nhất (xem Bài 11, `c4`).

### Bài 11.

```c
int c1(const void *a, const void *b){ return *(const int *)a - *(const int *)b; }   // SAI (tran so)
int c2(const void *a, const void *b){ return *(const int *)a > *(const int *)b; }   // SAI
int c3(const void *a, const void *b){ int x = *(const int *)a, y = *(const int *)b;
                                      return (x > y) - (x < y); }                  // DUNG
int c4(const void *a, const void *b){ return strcmp((const char *)a, (const char *)b); } // SAI voi char *ds[]
```

**Phân tích từng hàm:**

| | Trả về | Vấn đề | Kết luận |
|---|---|---|---|
| `c1: x - y` | âm/0/dương | **Tràn số** khi `x`, `y` lớn và trái dấu | **SAI** (chỉ đúng với số nhỏ) |
| `c2: x > y` | chỉ **0 hoặc 1** | Không bao giờ trả **số âm** → khi `x < y` báo "bằng nhau" | **SAI** |
| `c3: (x>y)-(x<y)` | -1/0/1 | Không tràn, nhất quán | **ĐÚNG** |
| `c4: strcmp` ép thẳng | âm/0/dương | Với `char *ds[]`, `a` trỏ tới **con trỏ**, không phải chuỗi | **SAI** với mảng con trỏ |

**`c2` sai vì:** `c2(5, 1)` trả 1 (đúng: 5 đứng sau 1), nhưng `c2(1, 5)` trả 0 tức "1 và 5 bằng nhau" — lẽ ra phải trả **số âm**. Hàm so sánh **không nhất quán** → `qsort` sắp sai, kết quả tuỳ vào cách cài đặt thư viện. Đây là lỗi hay gặp khi chuyển thói quen viết "hàm trả về đúng/sai" sang `qsort`.

**`c4` sai vì:** `strcmp` đọc các byte của **địa chỉ** như thể đó là ký tự. Sửa thành:

```c
int c4(const void *a, const void *b){
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}
```

(`c4` gốc lại **đúng** nếu dùng cho mảng 2 chiều `char ds[][N]`.)

💡 **Cách kiểm tra nhanh một hàm so sánh:** thử `cmp(x, x)` phải bằng 0, và `cmp(x, y)`, `cmp(y, x)` phải **trái dấu** nhau.

### Bài 12.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAXTU 100

typedef struct {
    char tu[20];
    int  dem;
} TanSuat;

int cmpTanSuat(const void *a, const void *b) {
    const TanSuat *p = (const TanSuat *)a;
    const TanSuat *q = (const TanSuat *)b;
    if (p->dem != q->dem) return (p->dem < q->dem) - (p->dem > q->dem);  // dem GIAM
    return strcmp(p->tu, q->tu);                                         // tu A-Z
}

int main(void) {
    char cau[] = "the cat and the dog and the bird saw a cat";
    TanSuat ds[MAXTU];
    int n = 0;

    // Tach tu bang strtok (cau bi sua truc tiep)
    for (char *p = strtok(cau, " "); p != NULL; p = strtok(NULL, " ")) {
        int i;
        for (i = 0; i < n; i++)
            if (strcmp(ds[i].tu, p) == 0) break;
        if (i < n) {
            ds[i].dem++;                          // tu da co -> tang dem
        } else if (n < MAXTU) {
            strncpy(ds[n].tu, p, sizeof(ds[n].tu) - 1);
            ds[n].tu[sizeof(ds[n].tu) - 1] = '\0';
            ds[n].dem = 1;
            n++;
        }
    }

    qsort(ds, n, sizeof(ds[0]), cmpTanSuat);

    printf("Xep hang tan suat:\n");
    for (int i = 0; i < n; i++)
        printf("  %-5s : %d\n", ds[i].tu, ds[i].dem);
    return 0;
}
```

Output:

```
Xep hang tan suat:
  the   : 3
  and   : 2
  cat   : 2
  a     : 1
  bird  : 1
  dog   : 1
  saw   : 1
```

💡 Mẫu **"đếm vào mảng struct → qsort"** rất thường dùng trong các bài đếm tần suất rồi xếp hạng. Cách đếm trên là O(n·m); khi số từ lớn có thể sắp các từ trước rồi đếm các đoạn liên tiếp bằng nhau (như bài 10-02).

### Bài 13.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// Danh sach uu tien (bien toan cuc de ham so sanh doc duoc)
static const char *uuTien[] = {"cherry", "fig"};
static const int soUuTien = 2;

bool laUuTien(const char *s) {
    for (int i = 0; i < soUuTien; i++)
        if (strcmp(s, uuTien[i]) == 0) return true;
    return false;
}

int cmpUuTien(const void *a, const void *b) {
    const char *s1 = *(const char * const *)a;
    const char *s2 = *(const char * const *)b;
    bool u1 = laUuTien(s1), u2 = laUuTien(s2);

    if (u1 != u2) return u1 ? -1 : 1;      // nhom uu tien dung truoc
    return strcmp(s1, s2);                  // cung nhom -> A-Z
}

int main(void) {
    const char *ds[] = {"banana", "apple", "cherry", "date", "fig", "grape"};
    int n = sizeof(ds) / sizeof(ds[0]);

    qsort(ds, n, sizeof(ds[0]), cmpUuTien);

    printf("Sau khi sap xep uu tien:\n");
    for (int i = 0; i < n; i++)
        printf("  %s%s\n", ds[i], laUuTien(ds[i]) ? "  <- UU TIEN" : "");
    return 0;
}
```

Output:

```
Sau khi sap xep uu tien:
  cherry  <- UU TIEN
  fig  <- UU TIEN
  apple
  banana
  date
  grape
```

💡 **Kỹ thuật `if (u1 != u2) return u1 ? -1 : 1;`:** nếu hai phần tử khác nhóm, phần tử thuộc nhóm ưu tiên đứng trước; nếu cùng nhóm mới xét tiêu chí phụ.

**Mở rộng — nhiều mức ưu tiên:** thay `laUuTien` bằng hàm `mucUuTien(s)` trả về 1, 2, ... (không có trong danh sách thì trả 999), rồi so sánh mức trước, tên sau:

```c
int m1 = mucUuTien(s1), m2 = mucUuTien(s2);
if (m1 != m2) return (m1 > m2) - (m1 < m2);
return strcmp(s1, s2);
```

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>

// Con tro toan cuc tro toi mang goc de ham so sanh doc gia tri
static const int *giaTri;

int cmpChiSo(const void *a, const void *b) {
    int i = *(const int *)a, j = *(const int *)b;
    int x = giaTri[i], y = giaTri[j];
    if (x != y) return (x < y) - (x > y);   // gia tri LON truoc (xep hang)
    return (i > j) - (i < j);                // bang nhau: chi so nho truoc
}

int main(void) {
    int diem[] = {72, 95, 88, 95, 60, 81};
    int n = sizeof(diem) / sizeof(diem[0]);
    int idx[6];

    for (int i = 0; i < n; i++) idx[i] = i;  // idx = 0, 1, 2, ..., n-1

    giaTri = diem;
    qsort(idx, n, sizeof(idx[0]), cmpChiSo);

    printf("Hang | Chi so | Diem\n");
    for (int k = 0; k < n; k++)
        printf("%4d | %6d | %4d\n", k + 1, idx[k], diem[idx[k]]);

    printf("\nMang goc van giu nguyen: ");
    for (int i = 0; i < n; i++) printf("%d ", diem[i]);
    printf("\n");
    return 0;
}
```

Output:

```
Hang | Chi so | Diem
   1 |      1 |   95
   2 |      3 |   95
   3 |      2 |   88
   4 |      5 |   81
   5 |      0 |   72
   6 |      4 |   60

Mang goc van giu nguyen: 72 95 88 95 60 81 
```

💡 **Sắp xếp chỉ số (index sort)** hữu ích khi: mảng gốc không được thay đổi, phần tử là struct lớn (đổi chỗ `int` nhanh hơn đổi chỗ cả struct), hoặc cần biết phần tử **ban đầu** ở vị trí nào.

💡 Tiêu chí phụ "chỉ số nhỏ trước" giúp các giá trị bằng nhau giữ **thứ tự ban đầu** — một cách biến `qsort` (vốn không ổn định) thành sắp xếp ổn định. Xem thêm bài [10-04](../10-04-c-sap-xep-on-dinh-va-merge-sort.md).

### Bài 15.

Toàn bộ "bộ sưu tập" để trong một file cho dễ biên dịch. Khi làm dự án thật, phần hàm so sánh có thể tách ra `comparators.h` / `comparators.c`.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/* ================= BO SUU TAP HAM SO SANH ================= */

// ---- So nguyen (mang int) ----
int cmp_int_tang(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    return (x > y) - (x < y);
}
int cmp_int_giam(const void *a, const void *b) {
    return cmp_int_tang(b, a);                  // dao chieu = doi cho tham so
}
int cmp_int_tri_tuyet_doi(const void *a, const void *b) {
    long long x = *(const int *)a, y = *(const int *)b;
    long long ax = x < 0 ? -x : x, ay = y < 0 ? -y : y;
    if (ax != ay) return (ax > ay) - (ax < ay);
    return (x > y) - (x < y);
}
int cmp_int_chan_truoc(const void *a, const void *b) {
    int x = *(const int *)a, y = *(const int *)b;
    int cx = (x % 2 == 0), cy = (y % 2 == 0);
    if (cx != cy) return cy - cx;               // chan (1) truoc le (0)
    return (x > y) - (x < y);
}

// ---- So long long ----
int cmp_ll_tang(const void *a, const void *b) {
    long long x = *(const long long *)a, y = *(const long long *)b;
    return (x > y) - (x < y);
}

// ---- So thuc (mang double) ----
int cmp_double_tang(const void *a, const void *b) {
    double x = *(const double *)a, y = *(const double *)b;
    return (x > y) - (x < y);
}

// ---- Chuoi trong mang con tro: const char *ds[] ----
int cmp_str_tang(const void *a, const void *b) {
    return strcmp(*(const char * const *)a, *(const char * const *)b);
}
int cmp_str_do_dai(const void *a, const void *b) {
    const char *s1 = *(const char * const *)a, *s2 = *(const char * const *)b;
    size_t l1 = strlen(s1), l2 = strlen(s2);
    if (l1 != l2) return (l1 > l2) - (l1 < l2);   // size_t: KHONG dung l1 - l2
    return strcmp(s1, s2);
}
int cmp_str_khong_hoa(const void *a, const void *b) {
    const char *s1 = *(const char * const *)a, *s2 = *(const char * const *)b;
    const char *p = s1, *q = s2;
    while (*p && tolower((unsigned char)*p) == tolower((unsigned char)*q)) { p++; q++; }
    int kq = tolower((unsigned char)*p) - tolower((unsigned char)*q);
    return kq != 0 ? kq : strcmp(s1, s2);
}

/* ======================== DUNG THU ======================== */

void inInt(const char *nhan, const int a[], int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

void inStr(const char *nhan, const char *a[], int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("%s ", a[i]);
    printf("\n");
}

// Sao chep mang goc roi sap theo ham so sanh duoc truyen vao
void thuInt(const char *nhan, const int goc[], int n,
            int (*cmp)(const void *, const void *)) {
    int a[16];
    memcpy(a, goc, n * sizeof(int));
    qsort(a, n, sizeof(a[0]), cmp);
    inInt(nhan, a, n);
}

void thuStr(const char *nhan, const char *goc[], int n,
            int (*cmp)(const void *, const void *)) {
    const char *a[16];
    memcpy(a, goc, n * sizeof(goc[0]));
    qsort(a, n, sizeof(a[0]), cmp);
    inStr(nhan, a, n);
}

int main(void) {
    int so[] = {-5, 3, 12, -8, 7, 21, -1, 100};
    int n = sizeof(so) / sizeof(so[0]);

    thuInt("Tang dan      ", so, n, cmp_int_tang);
    thuInt("Giam dan      ", so, n, cmp_int_giam);
    thuInt("Tri tuyet doi ", so, n, cmp_int_tri_tuyet_doi);
    thuInt("Chan truoc    ", so, n, cmp_int_chan_truoc);

    long long lon[] = {5000000000LL, -3, 9000000000000LL, 0};
    qsort(lon, 4, sizeof(lon[0]), cmp_ll_tang);
    printf("long long     : %lld %lld %lld %lld\n", lon[0], lon[1], lon[2], lon[3]);

    double thuc[] = {2.5, -0.75, 3.25, 0.5};
    qsort(thuc, 4, sizeof(thuc[0]), cmp_double_tang);
    printf("double        : %.2f %.2f %.2f %.2f\n", thuc[0], thuc[1], thuc[2], thuc[3]);

    printf("\n");
    const char *chuoi[] = {"file10", "File2", "banana", "fig", "file1"};
    int m = sizeof(chuoi) / sizeof(chuoi[0]);

    thuStr("Tu dien       ", chuoi, m, cmp_str_tang);
    thuStr("Theo do dai   ", chuoi, m, cmp_str_do_dai);
    thuStr("Khong pb hoa  ", chuoi, m, cmp_str_khong_hoa);
    return 0;
}
```

Output:

```
Tang dan      : -8 -5 -1 3 7 12 21 100 
Giam dan      : 100 21 12 7 3 -1 -5 -8 
Tri tuyet doi : -1 3 -5 7 -8 12 21 100 
Chan truoc    : -8 12 100 -5 -1 3 7 21 
long long     : -3 0 5000000000 9000000000000
double        : -0.75 0.50 2.50 3.25

Tu dien       : File2 banana fig file1 file10 
Theo do dai   : fig File2 file1 banana file10 
Khong pb hoa  : banana fig file1 file10 File2 
```

💡 **Điểm thiết kế đáng học:**
1. **Đặt tên theo quy ước `cmp_<kieu>_<tieu chi>`** — nhìn tên là biết dùng cho mảng kiểu gì, tránh ép kiểu nhầm
2. **Đảo chiều bằng cách đổi chỗ tham số** — `cmp_int_giam` chỉ gọi `cmp_int_tang(b, a)`
3. **Không bao giờ `return x - y`** — mọi hàm dùng `(x > y) - (x < y)` hoặc so sánh riêng
4. **Hàm `thuInt`/`thuStr` nhận con trỏ hàm** `int (*cmp)(const void *, const void *)` — cùng kiểu với tham số thứ 4 của `qsort`, nên truyền được bất kỳ hàm nào trong bộ sưu tập
