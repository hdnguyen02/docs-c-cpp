# Lời giải — [C]. Con Trỏ Và Mảng 1 Chiều

[← Quay lại bài học](../07-03-c-con-tro-va-mang-1-chieu.md)

> **Điểm cốt lõi:** tên mảng chính là **địa chỉ của phần tử đầu tiên**, và `a[i]` chỉ là cách viết tắt của `*(a + i)`.

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;              // khong can &a[0] - ten mang DA LA dia chi

    printf("Cach 1 (con tro + chi so): ");
    for (int i = 0; i < 5; i++) printf("%d ", p[i]);
    printf("\n");

    printf("Cach 2 (so hoc con tro) : ");
    for (int i = 0; i < 5; i++) printf("%d ", *(p + i));
    printf("\n");

    printf("Cach 3 (dich con tro)   : ");
    for (int *q = a; q < a + 5; q++) printf("%d ", *q);
    printf("\n");

    return 0;
}
```

Cả 3 cách đều in: `10 20 30 40 50`

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;

    printf("i\ta[i]\t*(a+i)\tp[i]\t*(p+i)\n");
    printf("-----------------------------------------\n");
    for (int i = 0; i < 5; i++) {
        printf("%d\t%d\t%d\t%d\t%d\n", i, a[i], *(a + i), p[i], *(p + i));
    }

    // Kiem chung bang dia chi
    printf("\nTat ca deu cung dia chi:\n");
    printf("&a[2]    = %p\n", (void *)&a[2]);
    printf("a + 2    = %p\n", (void *)(a + 2));
    printf("&p[2]    = %p\n", (void *)&p[2]);
    printf("p + 2    = %p\n", (void *)(p + 2));
    return 0;
}
```

Output:

```
i	a[i]	*(a+i)	p[i]	*(p+i)
-----------------------------------------
0	10	10	10	10
1	20	20	20	20
...
```

**Quy tắc chuyển đổi của compiler:**

```
a[i]  ==  *(a + i)
p[i]  ==  *(p + i)
```

Vì phép cộng có tính giao hoán, `*(a+i) == *(i+a) == i[a]` — nên `2[a]` cũng hợp lệ và bằng `a[2]`! (Đương nhiên không nên viết như vậy.)

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    int    a[5] = {1, 2, 3, 4, 5};
    double b[5] = {1.1, 2.2, 3.3, 4.4, 5.5};
    char   c[5] = {'a', 'b', 'c', 'd', 'e'};

    printf("--- Mang int (4 byte/phan tu) ---\n");
    for (int i = 0; i < 5; i++) printf("&a[%d] = %p\n", i, (void *)&a[i]);

    printf("\n--- Mang double (8 byte/phan tu) ---\n");
    for (int i = 0; i < 5; i++) printf("&b[%d] = %p\n", i, (void *)&b[i]);

    printf("\n--- Mang char (1 byte/phan tu) ---\n");
    for (int i = 0; i < 5; i++) printf("&c[%d] = %p\n", i, (void *)&c[i]);

    printf("\n--- Khoang cach ---\n");
    printf("int    : %td byte\n", (char *)&a[1] - (char *)&a[0]);
    printf("double : %td byte\n", (char *)&b[1] - (char *)&b[0]);
    printf("char   : %td byte\n", (char *)&c[1] - (char *)&c[0]);
    return 0;
}
```

**Nhận xét:** các phần tử nằm **liên tiếp** trong bộ nhớ, cách nhau đúng `sizeof(kiểu)` byte.

```
int    a: 0x1000, 0x1004, 0x1008, 0x100c, 0x1010   (cach 4)
double b: 0x2000, 0x2008, 0x2010, 0x2018, 0x2020   (cach 8)
char   c: 0x3000, 0x3001, 0x3002, 0x3003, 0x3004   (cach 1)
```

⚠️ **Phải dùng `%p` (kèm ép `(void *)`) khi in địa chỉ** — nếu in `&c[i]` bằng `%s`, `printf` sẽ hiểu `char *` là **chuỗi** và in nội dung (thậm chí đọc tràn vì mảng `c` không có `'\0'`).

💡 Hiệu hai con trỏ có kiểu `ptrdiff_t`, in bằng `%td`. Ép về `char *` để đo khoảng cách theo **byte**.

💡 Đây chính là lý do `p + 1` nhảy khác nhau tuỳ kiểu: compiler tự nhân với `sizeof(kiểu)`.

### Bài 4.

```c
#include <stdio.h>

long long tongMang(const int *a, int n) {
    long long tong = 0;
    const int *ketThuc = a + n;

    for (const int *p = a; p < ketThuc; p++) {
        tong += *p;
    }
    return tong;
}

int main(void) {
    int a[6] = {10, 20, 30, 40, 50, 60};
    printf("Tong = %lld\n", tongMang(a, 6));    // 210
    return 0;
}
```

💡 Tính sẵn `ketThuc = a + n` ngoài vòng lặp, thay vì viết `p < a + n` (tính lại mỗi vòng). Compiler thường tự tối ưu, nhưng viết rõ vẫn tốt hơn.

### Bài 5.

```c
#include <stdio.h>

int *timMax(int *a, int n) {
    if (n <= 0) return NULL;

    int *max = a;
    for (int *p = a + 1; p < a + n; p++) {
        if (*p > *max) max = p;
    }
    return max;
}

int main(void) {
    int a[6] = {10, 45, 30, 90, 50, 20};

    int *p = timMax(a, 6);
    if (p) {
        printf("Gia tri lon nhat = %d\n", *p);          // 90
        printf("Tai vi tri       = %td\n", p - a);      // 3
        *p = 0;                                          // sua duoc qua con tro
        printf("Sau khi dat ve 0: a[3] = %d\n", a[3]);  // 0
    }
    return 0;
}
```

💡 **Lợi ích trả về con trỏ:** vừa biết giá trị (`*p`), vừa biết vị trí (`p - a`), lại **sửa được** phần tử đó.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};

    printf("Duyet nguoc: ");
    for (int *p = a + 4; p >= a; p--) {
        printf("%d ", *p);
    }
    printf("\n");                       // 50 40 30 20 10

    // Cach khac - an toan hon (tranh p < a la undefined behavior)
    printf("Cach 2     : ");
    for (int *p = a + 5; p > a; ) {
        p--;
        printf("%d ", *p);
    }
    printf("\n");
    return 0;
}
```

⚠️ **Lưu ý kỹ thuật:** khi `p = a` rồi `p--`, con trỏ trỏ vào vị trí **trước** mảng — về mặt chuẩn C đây là *undefined behavior* (dù thực tế hầu như luôn chạy đúng). Cách 2 an toàn hơn vì con trỏ không bao giờ đi trước `a`.

Chuẩn C cho phép con trỏ trỏ tới vị trí **ngay sau** phần tử cuối (`a + n`) — miễn là không giải tham chiếu nó. Nhờ vậy điều kiện `p < a + n` luôn hợp lệ.

### Bài 7.

```c
#include <stdio.h>

int main(void) {
    int a[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    int *p = &a[2];
    int *q = &a[7];

    printf("p tro toi a[2] = %d\n", *p);
    printf("q tro toi a[7] = %d\n", *q);

    printf("\nq - p = %td\n", q - p);        // 5 (SO PHAN TU, khong phai byte)
    printf("p - q = %td\n", p - q);          // -5

    printf("\nKhoang cach byte thuc te = %td byte\n",
           (char *)q - (char *)p);           // 20 = 5 * 4

    // Ung dung: tinh vi tri
    printf("\nVi tri cua p trong mang = %td\n", p - a);   // 2
    return 0;
}
```

**Điểm mấu chốt: hiệu 2 con trỏ cho SỐ PHẦN TỬ giữa chúng, không phải số byte.**

```
q - p = (dia chi q - dia chi p) / sizeof(int)
      = (0x101c - 0x1008) / 4
      = 20 / 4
      = 5
```

**Ứng dụng phổ biến nhất** — đổi con trỏ thành chỉ số:

```c
int *p = timKiem(a, n, x);         // xem bai 12
int viTri = (int)(p - a);          // doi con tro thanh chi so
```

⚠️ Hiệu 2 con trỏ **chỉ có ý nghĩa** khi chúng trỏ vào cùng một mảng.

### Bài 8.

```c
#include <stdio.h>

void daoNguoc(int *a, int n) {
    int *trai = a;
    int *phai = a + n - 1;

    while (trai < phai) {
        int tam = *trai;           // hoan doi 2 phan tu
        *trai = *phai;
        *phai = tam;
        trai++;
        phai--;
    }
}

void inMang(const int *a, int n) {
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[6] = {1, 2, 3, 4, 5, 6};

    printf("Truoc: ");
    inMang(a, 6);

    daoNguoc(a, 6);

    printf("Sau  : ");
    inMang(a, 6);                  // 6 5 4 3 2 1
    return 0;
}
```

**Kỹ thuật 2 con trỏ** — hai con trỏ tiến từ hai đầu vào giữa. Điều kiện `trai < phai` tự động dừng đúng chỗ với cả `n` chẵn và lẻ.

### Bài 9.

```c
int a[5] = {10,20,30,40,50};
int *p = a;
printf("%d %d %d\n", *p, *p++, *p);
printf("%d %d\n", *(a+2), *a+2);
```

**Dòng 1 — KHÔNG ĐOÁN TRƯỚC ĐƯỢC (undefined behavior).**

Lời gọi có `p++` (sửa `p`) và đồng thời đọc `*p` ở 2 đối số khác, mà **chuẩn C không quy định thứ tự tính các đối số của hàm**, cũng không có điểm tuần tự (sequence point) giữa chúng. Kết quả có thể là `10 10 20`, `20 10 20`, hoặc khác — tuỳ compiler. gcc với `-Wall` sẽ cảnh báo: `operation on 'p' may be undefined [-Wsequence-point]`.

✅ **Không bao giờ viết code kiểu này.** Tách ra:

```c
printf("%d ", *p);
printf("%d ", *p);
p++;
printf("%d\n", *p);
```

**Dòng 2 — kết quả rõ ràng: `30 12`**

| Biểu thức | Kết quả | Giải thích |
|---|---|---|
| `*(a+2)` | **30** | Cộng địa chỉ trước (`a+2` trỏ tới `a[2]`), rồi giải tham chiếu |
| `*a+2` | **12** | Giải tham chiếu trước (`*a` = `a[0]` = 10), rồi cộng 2 |

**Lý do:** toán tử `*` (giải tham chiếu) có **độ ưu tiên cao hơn** `+`.

✅ **Luôn đặt ngoặc cho rõ:** viết `*(a+2)` hoặc `a[2]`, đừng dựa vào độ ưu tiên.

### Bài 10.

```c
#include <stdio.h>

void trongHam(int a[]) {
    printf("Trong ham : sizeof(a) = %zu byte\n", sizeof(a));
}

int main(void) {
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int *p = a;

    printf("sizeof(a) = %zu byte\n", sizeof(a));   // 40
    printf("sizeof(p) = %zu byte\n", sizeof(p));   // 8

    printf("So phan tu = %zu\n", sizeof(a) / sizeof(a[0]));   // 10

    trongHam(a);                                    // 8

    printf("\nDia chi: a = %p, p = %p\n", (void *)a, (void *)p);   // GIONG NHAU
    return 0;
}
```

Output:

```
sizeof(a) = 40 byte
sizeof(p) = 8 byte
So phan tu = 10
Trong ham : sizeof(a) = 8 byte
Dia chi: a = 0x7ffd..., p = 0x7ffd...
```

💡 gcc sẽ cảnh báo ở hàm `trongHam`: `'sizeof' on array function parameter 'a' will return size of 'int *'` — chính là điều bài này muốn chứng minh.

**Giải thích:**

| | `a` (tên mảng) | `p` (con trỏ) |
|---|---|---|
| Kiểu thực sự | `int[10]` | `int*` |
| `sizeof` | 40 (= 10 × 4) — **toàn bộ mảng** | 8 — chỉ là một địa chỉ |
| Gán lại được? | ❌ Không (`a = p` báo lỗi) | ✅ Có |

**Tên mảng KHÔNG phải con trỏ** — nó là một *mảng*, chỉ **tự động chuyển** thành con trỏ khi cần (array-to-pointer decay). `sizeof` và `&` là những chỗ mà sự chuyển đổi này **không** xảy ra.

⚠️ **Hệ quả quan trọng:** khi truyền mảng vào hàm, nó **đã suy biến thành con trỏ** (tham số `int a[]` thực chất là `int *a`), nên `sizeof` bên trong hàm cho 8 chứ không phải 40. Đây là lý do **luôn phải truyền kèm kích thước `n`**.

Mẹo `sizeof(a)/sizeof(a[0])` **chỉ dùng được trong cùng phạm vi khai báo mảng**.

### Bài 11.

```c
#include <stdio.h>
#include <string.h>

// Phien ban tu viet cua memcpy cho mang int
void copyMang(int *dich, const int *nguon, int n) {
    for (int i = 0; i < n; i++) {
        *(dich + i) = *(nguon + i);
    }
}

// Phien ban dung con tro dich chuyen
void copyMang2(int *dich, const int *nguon, int n) {
    const int *ketThuc = nguon + n;
    while (nguon < ketThuc) {
        *dich++ = *nguon++;          // gan roi tang ca hai con tro
    }
}

void inMang(const char *nhan, const int *a, int n) {
    printf("%s: ", nhan);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
}

int main(void) {
    int a[5] = {10, 20, 30, 40, 50};
    int b[5], c[5], d[5];

    copyMang(b, a, 5);
    copyMang2(c, a, 5);
    memcpy(d, a, 5 * sizeof(int));   // Dung memcpy co san (lam viec theo BYTE)

    inMang("b", b, 5);
    inMang("c", c, 5);
    inMang("d", d, 5);
    return 0;
}
```

💡 `*dich++ = *nguon++` là thành ngữ kinh điển của C: gán giá trị rồi tăng cả hai con trỏ. Rất ngắn gọn nhưng khó đọc với người mới.

⚠️ **`memcpy` làm việc theo BYTE**, nên phải nhân với `sizeof(int)`. Nếu quên, chỉ copy được 5 byte thay vì 20.

⚠️ `memcpy` không dùng được khi vùng nguồn và vùng đích **chồng lấn** nhau — khi đó dùng `memmove`.

### Bài 12.

```c
#include <stdio.h>

int *timKiem(int *a, int n, int x) {
    for (int *p = a; p < a + n; p++) {
        if (*p == x) return p;
    }
    return NULL;                     // khong tim thay
}

int main(void) {
    int a[6] = {10, 25, 30, 45, 50, 25};

    int *p = timKiem(a, 6, 45);
    if (p) printf("Tim thay 45 tai vi tri %td\n", p - a);      // 3
    else   printf("Khong tim thay 45\n");

    p = timKiem(a, 6, 99);
    if (p) printf("Tim thay 99 tai vi tri %td\n", p - a);
    else   printf("Khong tim thay 99\n");

    return 0;
}
```

💡 So sánh 2 quy ước báo "không tìm thấy":
- Trả về **`NULL`** (con trỏ) — rõ ràng, không nhầm lẫn
- Trả về **`-1`** (chỉ số) — phổ biến, nhưng phải nhớ kiểm tra

Thư viện chuẩn C dùng quy ước `NULL`: `strchr`, `strstr`, `bsearch`, `memchr` đều trả về `NULL` khi không tìm thấy.

### Bài 13.

```c
#include <stdio.h>

void inDoan(const char *nhan, const int *batDau, const int *ketThuc) {
    printf("%s (%td phan tu): ", nhan, ketThuc - batDau);
    for (const int *p = batDau; p < ketThuc; p++) printf("%d ", *p);
    printf("\n");
}

int main(void) {
    int a[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = 9;
    int giua = n / 2;

    inDoan("Toan bo   ", a, a + n);
    inDoan("Nua dau   ", a, a + giua);
    inDoan("Nua sau   ", a + giua, a + n);

    // Chia lam 3 phan
    printf("\n");
    inDoan("Phan 1    ", a,     a + 3);
    inDoan("Phan 2    ", a + 3, a + 6);
    inDoan("Phan 3    ", a + 6, a + 9);
    return 0;
}
```

Output:

```
Toan bo    (9 phan tu): 1 2 3 4 5 6 7 8 9 
Nua dau    (4 phan tu): 1 2 3 4 
Nua sau    (5 phan tu): 5 6 7 8 9 

Phan 1     (3 phan tu): 1 2 3 
Phan 2     (3 phan tu): 4 5 6 
Phan 3     (3 phan tu): 7 8 9 
```

💡 **Cặp con trỏ `[batDau, ketThuc)`** — quy ước "bao gồm đầu, không bao gồm cuối", nhờ đó `ketThuc - batDau` cho ngay số phần tử và đoạn rỗng chỉ là `batDau == ketThuc`. Truyền `a + giua` cho hàm chính là truyền **mảng con** bắt đầu từ vị trí `giua` mà không cần sao chép.

### Bài 14.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    const int N = 10000000;
    int *a = malloc(N * sizeof(int));     // 40 MB -> cap phat dong (xem bai 07-04)
    if (a == NULL) { printf("Khong du bo nho!\n"); return 1; }
    for (int i = 0; i < N; i++) a[i] = i % 100;

    // (1) Duyet bang chi so
    clock_t t1 = clock();
    long long tong1 = 0;
    for (int i = 0; i < N; i++) tong1 += a[i];
    clock_t t2 = clock();
    printf("Chi so  : %.2f ms\n", 1000.0 * (t2 - t1) / CLOCKS_PER_SEC);

    // (2) Duyet bang con tro
    t1 = clock();
    long long tong2 = 0;
    for (int *p = a; p < a + N; p++) tong2 += *p;
    t2 = clock();
    printf("Con tro : %.2f ms\n", 1000.0 * (t2 - t1) / CLOCKS_PER_SEC);

    printf("\nKiem tra: %s (tong = %lld)\n", tong1 == tong2 ? "OK" : "SAI", tong1);
    free(a);
    return 0;
}
```

Kết quả tham khảo (biên dịch với `-O2`):

```
Chi so  : 8.00 ms
Con tro : 8.00 ms

Kiem tra: OK (tong = 495000000)
```

**Kết luận: TỐC ĐỘ GẦN NHƯ BẰNG NHAU.**

**Vì sao:** compiler hiện đại (với `-O2`) nhận ra `a[i]` và `*(a+i)` là **cùng một thứ** và sinh ra mã máy giống hệt nhau.

⚠️ Nếu biên dịch **không tối ưu** (`-O0`), kết quả có thể chênh lệch một chút — nhưng không ai chạy chương trình thật ở chế độ đó.

💡 **Bài học quan trọng:** đừng hy sinh tính dễ đọc để "tối ưu" những thứ compiler đã tự làm. Hãy viết `a[i]` khi nó rõ ràng hơn.

Kiểm chứng bằng cách so sánh assembly:

```bash
gcc -O2 -S main.c -o out.s
```

### Bài 15.

```c
#include <stdio.h>
#include <stddef.h>

// ===== strlen: dem so ky tu den truoc '\0' =====
size_t myStrlen(const char *s) {
    const char *p = s;
    while (*p != '\0') p++;
    return (size_t)(p - s);          // hieu 2 con tro = do dai
}

// ===== strcpy: sao chep chuoi (KE CA ky tu '\0') =====
char *myStrcpy(char *dich, const char *nguon) {
    char *batDau = dich;
    while ((*dich++ = *nguon++) != '\0');    // gan, roi kiem tra
    return batDau;
}

// ===== strcmp: so sanh 2 chuoi =====
int myStrcmp(const char *s1, const char *s2) {
    while (*s1 && (*s1 == *s2)) { s1++; s2++; }
    return (unsigned char)*s1 - (unsigned char)*s2;
}

// ===== strcat: noi chuoi =====
char *myStrcat(char *dich, const char *nguon) {
    char *batDau = dich;
    while (*dich) dich++;                     // di toi cuoi chuoi dich
    while ((*dich++ = *nguon++) != '\0');     // noi chuoi nguon vao
    return batDau;
}

int main(void) {
    const char *s = "codelab";
    printf("myStrlen(\"codelab\") = %zu\n", myStrlen(s));     // 7

    char buf[50];
    myStrcpy(buf, "Hello");
    printf("Sau myStrcpy: %s\n", buf);                        // Hello

    myStrcat(buf, " World");
    printf("Sau myStrcat: %s\n", buf);                        // Hello World

    printf("\nmyStrcmp:\n");
    printf("  (\"abc\", \"abc\") = %d\n", myStrcmp("abc", "abc"));   // 0
    printf("  (\"abc\", \"abd\") = %d\n", myStrcmp("abc", "abd"));   // am
    printf("  (\"abd\", \"abc\") = %d\n", myStrcmp("abd", "abc"));   // duong
    printf("  (\"abc\", \"ab\")  = %d\n", myStrcmp("abc", "ab"));    // duong
    return 0;
}
```

**Giải thích `myStrcpy`:**

```c
while ((*dich++ = *nguon++) != '\0');
//       └─ (1) gan ky tu
//          └─ (2) tang ca hai con tro
//             └─ (3) kiem tra ky tu vua gan co phai '\0' khong
```

Vòng lặp **cũng sao chép luôn ký tự `'\0'`** rồi mới dừng — đúng như hành vi của `strcpy` chuẩn.

**Giá trị trả về của `strcmp`:**
- `0` — hai chuỗi bằng nhau
- `< 0` — `s1` đứng trước `s2` theo thứ tự từ điển
- `> 0` — `s1` đứng sau `s2`

⚠️ **Những hàm này rất nguy hiểm nếu dùng bất cẩn:**

```c
char buf[5];
strcpy(buf, "Chuoi rat dai");     // TRAN BO DEM - ghi de bo nho, crash hoac lo hong bao mat
```

`strcpy`/`strcat` **không kiểm tra kích thước đích**. Đây là nguyên nhân của vô số lỗ hổng bảo mật "buffer overflow" trong lịch sử phần mềm.

✅ **Cách an toàn hơn trong C:** luôn biết kích thước bộ đệm và giới hạn số ký tự ghi vào:

```c
char buf[5];
snprintf(buf, sizeof(buf), "%s", "Chuoi rat dai");   // chi ghi toi da 4 ky tu + '\0'
printf("%s\n", buf);                                 // "Chuo"
```
