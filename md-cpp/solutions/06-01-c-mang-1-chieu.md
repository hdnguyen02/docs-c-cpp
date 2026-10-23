# Lời giải — [C]. Mảng 1 Chiều

[← Quay lại bài học](../06-01-c-mang-1-chieu.md)

> **Nhớ:** chỉ số mảng trong C bắt đầu từ **0**. Mảng `n` phần tử có chỉ số hợp lệ từ `0` đến `n−1`.

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap so phan tu: ");
    scanf("%d", &n);

    int a[1000];
    for (int i = 0; i < n; i++) {
        printf("  a[%d] = ", i);
        scanf("%d", &a[i]);
    }

    printf("Thu tu nhap  : ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");

    printf("Thu tu nguoc : ");
    for (int i = n - 1; i >= 0; i--) printf("%d ", a[i]);
    printf("\n");

    return 0;
}
```

⚠️ Với `scanf`, phải truyền **địa chỉ** của phần tử: `&a[i]`. Quên dấu `&` là lỗi rất hay gặp, chương trình sẽ crash hoặc cho kết quả sai.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tong = 0;
    long long tich = 1;
    for (int i = 0; i < n; i++) {
        tong += a[i];
        tich *= a[i];
    }

    printf("Tong        = %lld\n", tong);
    printf("Tich        = %lld\n", tich);
    printf("Trung binh  = %.4f\n", n > 0 ? (double)tong / n : 0.0);
    return 0;
}
```

⚠️ **Tích rất dễ tràn số** — chỉ cần 10 phần tử cỡ 100 là đã vượt `long long`. Trong bài toán thật thường phải lấy dư (`% 1000000007`).

⚠️ Nhớ `(double)tong / n` chứ không phải `tong / n` (chia nguyên). In `long long` bằng `%lld`, in số thực với 4 chữ số thập phân bằng `%.4f`.

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    if (n <= 0) { printf("Mang rong!\n"); return 1; }

    int vtMax = 0, vtMin = 0;
    for (int i = 1; i < n; i++) {
        if (a[i] > a[vtMax]) vtMax = i;
        if (a[i] < a[vtMin]) vtMin = i;
    }

    printf("Lon nhat  = %d tai vi tri %d\n", a[vtMax], vtMax);
    printf("Nho nhat  = %d tai vi tri %d\n", a[vtMin], vtMin);
    return 0;
}
```

⚠️ **Khởi tạo bằng `a[0]` (hoặc vị trí 0), KHÔNG phải bằng 0.** Nếu mảng toàn số âm và bạn khởi tạo `max = 0`, kết quả sẽ sai.

💡 Lưu **vị trí** thay vì giá trị giúp có được cả hai thông tin bằng một biến.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int duong = 0, am = 0, khong = 0;
    for (int i = 0; i < n; i++) {
        if      (a[i] > 0) duong++;
        else if (a[i] < 0) am++;
        else               khong++;
    }

    printf("So duong  : %d\n", duong);
    printf("So am     : %d\n", am);
    printf("So bang 0 : %d\n", khong);
    return 0;
}
```

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int demChan = 0, demLe = 0;
    long long tongChan = 0, tongLe = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] % 2 == 0) { demChan++; tongChan += a[i]; }
        else               { demLe++;   tongLe   += a[i]; }
    }

    printf("So luong chan : %d, tong = %lld\n", demChan, tongChan);
    printf("So luong le   : %d, tong = %lld\n", demLe, tongLe);
    return 0;
}
```

⚠️ Dùng `a[i] % 2 == 0` để kiểm tra chẵn (đúng với cả số âm). Không dùng `a[i] % 2 == 1` vì `-3 % 2` bằng `-1`.

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(int n) {
    if (n < 2) return false;
    if (n < 4) return true;
    if (n % 2 == 0) return false;
    for (int i = 3; (long long)i * i <= n; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    printf("Cac so nguyen to trong mang: ");
    int dem = 0;
    for (int i = 0; i < n; i++) {
        if (laNguyenTo(a[i])) { printf("%d ", a[i]); dem++; }
    }
    if (dem == 0) printf("(khong co)");
    printf("\nSo luong: %d\n", dem);
    return 0;
}
```

### Bài 7.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    bool tangDan = true;
    for (int i = 0; i < n - 1; i++) {
        if (a[i] > a[i + 1]) { tangDan = false; break; }
    }

    printf("Mang %s sap xep tang dan\n", tangDan ? "DA" : "CHUA");
    return 0;
}
```

⚠️ Vòng lặp chạy tới `n - 1` (không phải `n`), vì ta so sánh `a[i]` với `a[i+1]`. Nếu chạy tới `n` thì `a[n]` là truy cập ngoài biên.

💡 Thư viện chuẩn C không có hàm kiểm tra mảng đã sắp xếp — ta tự viết như trên, và nên đóng gói thành hàm `bool daSapXep(int a[], int n)` để dùng lại.

### Bài 8.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    int x;
    printf("Nhap gia tri can dem: ");
    scanf("%d", &x);

    int dem = 0;
    printf("Xuat hien tai cac vi tri: ");
    for (int i = 0; i < n; i++) {
        if (a[i] == x) { printf("%d ", i); dem++; }
    }
    printf("\nSo lan xuat hien: %d\n", dem);
    return 0;
}
```

💡 C không có hàm đếm có sẵn cho mảng; vòng lặp đếm như trên là cách làm chuẩn.

### Bài 9.

```c
#include <stdio.h>
#include <limits.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    if (n < 2) { printf("Mang can it nhat 2 phan tu!\n"); return 1; }

    long long nhat = LLONG_MIN, nhi = LLONG_MIN;
    for (int i = 0; i < n; i++) {
        if (a[i] > nhat) {
            nhi  = nhat;           // cai lon nhat cu tut xuong thanh nhi
            nhat = a[i];
        } else if (a[i] > nhi && a[i] != nhat) {
            nhi = a[i];
        }
    }

    if (nhi == LLONG_MIN) printf("Khong co phan tu lon thu hai (tat ca bang nhau)\n");
    else printf("Lon nhat = %lld, lon thu hai = %lld\n", nhat, nhi);
    return 0;
}
```

Ví dụ với `{5, 2, 9, 9, 1}` → lớn nhất 9, lớn thứ hai 5.

⚠️ **Điều kiện `a[i] != nhat`** xử lý trường hợp có giá trị trùng lặp. Nếu bỏ đi, mảng `{9, 9, 1}` sẽ cho "lớn thứ hai = 9" — thường không phải ý đồ bài toán.

💡 Cách này duyệt **một lần** O(n), tốt hơn sắp xếp O(n log n). Hằng `LLONG_MIN` (giá trị nhỏ nhất của `long long`) nằm trong `<limits.h>`.

### Bài 10.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    // Dao nguoc tai cho: doi cho phan tu dau <-> cuoi, roi tien vao giua
    for (int i = 0; i < n / 2; i++) {
        int tam = a[i];
        a[i] = a[n - 1 - i];
        a[n - 1 - i] = tam;
    }

    printf("Mang sau khi dao: ");
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

⚠️ **Vòng lặp chỉ chạy tới `n / 2`.** Nếu chạy hết `n`, mảng sẽ bị đảo **2 lần** và trở về như cũ.

Với `n` lẻ, phần tử giữa không cần đổi (nó tự đổi với chính nó).

💡 C không có hàm `swap` dựng sẵn, nên đổi chỗ 2 phần tử bằng một biến tạm `tam` như trên.

### Bài 11.

```c
int a[5];
for (int i = 0; i <= 5; i++) a[i] = i;      // LOI!
```

**Lỗi: truy cập ngoài biên mảng (out of bounds).**

Mảng `a[5]` có 5 phần tử với chỉ số hợp lệ là **0, 1, 2, 3, 4**. Vòng lặp chạy `i = 0..5` nên lần cuối ghi vào `a[5]` — **ô nhớ không thuộc mảng**.

**Tính nguy hiểm đặc biệt:** C **không kiểm tra** biên mảng. Chương trình:
- Có thể vẫn chạy bình thường (ghi vào ô nhớ trống)
- Có thể **ghi đè lên biến khác** → kết quả sai một cách khó hiểu
- Có thể crash với `Segmentation fault`

Kết quả không đoán trước được, và có thể khác nhau giữa các lần chạy.

**Sửa:**

```c
for (int i = 0; i < 5; i++) a[i] = i;      // dung dau < thay vi <=
```

✅ **Quy tắc vàng: với mảng `n` phần tử, luôn viết `for (int i = 0; i < n; i++)`.** Dùng `<` chứ không phải `<=`.

💡 **Công cụ phát hiện lỗi này:**

```bash
gcc -fsanitize=address -g main.c -o main
./main
# AddressSanitizer: stack-buffer-overflow ... WRITE of size 4
```

### Bài 12.

```c
#include <stdio.h>

void inMang(const char *ten, int m[], int n) {
    printf("%s: ", ten);
    for (int i = 0; i < n; i++) printf("%d ", m[i]);
    printf("\n");
}

int main(void) {
    // (1) Khai bao du phan tu
    int a[5] = {10, 20, 30, 40, 50};

    // (2) Khai bao THIEU phan tu -> phan con lai tu dong bang 0
    int b[5] = {10, 20};

    // (3) Khong ghi kich thuoc -> compiler tu dem
    int c[] = {1, 2, 3, 4, 5, 6, 7};

    // (4) Khoi tao tat ca bang 0
    int d[5] = {0};

    inMang("a (du)      ", a, 5);
    inMang("b (thieu)   ", b, 5);
    inMang("c (tu dem)  ", c, 7);
    inMang("d (toan 0)  ", d, 5);

    printf("So phan tu cua c = %zu\n", sizeof(c) / sizeof(c[0]));
    return 0;
}
```

Output:

```
a (du)      : 10 20 30 40 50 
b (thieu)   : 10 20 0 0 0 
c (tu dem)  : 1 2 3 4 5 6 7 
d (toan 0)  : 0 0 0 0 0 
So phan tu cua c = 7
```

**Ghi nhớ:**
- Khởi tạo thiếu → phần còn lại tự động **bằng 0**
- `int d[5] = {0}` là cách gọn nhất để khởi tạo mảng toàn 0 trong C (cách viết `{}` rỗng chỉ hợp lệ từ chuẩn C23)
- **Không khởi tạo gì cả** (`int e[5];` bên trong hàm) → các phần tử mang **giá trị rác**, mỗi lần chạy có thể khác nhau. Đọc giá trị rác là hành vi không xác định, vì vậy chương trình trên không in thử mảng như vậy
- `sizeof(mang) / sizeof(mang[0])` cho số phần tử (kiểu `size_t`, in bằng `%zu`) — **chỉ dùng được trong cùng hàm khai báo mảng** (xem bài [06-07 — Truyền mảng vào hàm](../06-07-c-truyen-mang-vao-ham.md))

### Bài 13.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tongViTriChan = 0, tongViTriLe = 0;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) tongViTriChan += a[i];    // vi tri 0, 2, 4, ...
        else            tongViTriLe   += a[i];    // vi tri 1, 3, 5, ...
    }

    printf("Tong cac phan tu o VI TRI chan: %lld\n", tongViTriChan);
    printf("Tong cac phan tu o VI TRI le  : %lld\n", tongViTriLe);
    return 0;
}
```

⚠️ **Phân biệt rõ:** "vị trí chẵn" (`i % 2 == 0`) khác với "giá trị chẵn" (`a[i] % 2 == 0`). Đề bài hay dùng cả hai cách nói — đọc kỹ.

### Bài 14.

```c
#include <stdio.h>
#include <math.h>

int main(void) {
    int n;
    scanf("%d", &n);
    int a[1000];
    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    if (n <= 0) return 1;

    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i];
    double tb = (double)tong / n;

    int viTriGan = 0;
    double khoangCachMin = fabs(a[0] - tb);
    for (int i = 1; i < n; i++) {
        double kc = fabs(a[i] - tb);
        if (kc < khoangCachMin) {
            khoangCachMin = kc;
            viTriGan = i;
        }
    }

    printf("Trung binh cong = %.4f\n", tb);
    printf("Phan tu gan nhat = %d (vi tri %d, cach %.4f)\n",
           a[viTriGan], viTriGan, khoangCachMin);
    return 0;
}
```

Ví dụ `{1, 5, 8, 12}` → TB = 6.5 → gần nhất là 5 hoặc 8 (cùng cách 1.5); code trả về **5** (gặp trước).

💡 `fabs` (trị tuyệt đối số thực) nằm trong `<math.h>`; nhớ thêm `-lm` khi biên dịch bằng gcc.

### Bài 15.

**Cách 1 — mảng tĩnh:**

```c
#include <stdio.h>

#define MAX 1000

int main(void) {
    int a[MAX];
    int n;

    printf("Nhap so phan tu (toi da %d): ", MAX);
    scanf("%d", &n);

    if (n <= 0 || n > MAX) {                   // PHAI tu kiem tra
        printf("Kich thuoc khong hop le!\n");
        return 1;
    }

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);

    long long tong = 0;
    for (int i = 0; i < n; i++) tong += a[i];

    printf("Tong = %lld\n", tong);
    return 0;
}
```

**Cách 2 — mảng cấp phát động bằng `malloc`:**

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    printf("Nhap so phan tu: ");
    scanf("%d", &n);
    if (n <= 0) { printf("Kich thuoc khong hop le!\n"); return 1; }

    int *a = malloc(n * sizeof(int));          // cap phat DUNG n phan tu tren HEAP
    if (a == NULL) {                           // het bo nho -> malloc tra ve NULL
        printf("Khong du bo nho!\n");
        return 1;
    }

    for (int i = 0; i < n; i++) scanf("%d", &a[i]);   // dung nhu mang binh thuong

    long long tong = 0;
    int lonNhat = a[0];
    for (int i = 0; i < n; i++) {
        tong += a[i];
        if (a[i] > lonNhat) lonNhat = a[i];
    }
    printf("Tong        = %lld\n", tong);
    printf("Lon nhat    = %d\n", lonNhat);

    // Muon them 1 phan tu: xin lai vung nho lon hon bang realloc
    int *moi = realloc(a, (n + 1) * sizeof(int));
    if (moi == NULL) { free(a); return 1; }
    a = moi;
    a[n] = 999;
    n++;
    printf("Sau khi them, so phan tu = %d, phan tu cuoi = %d\n", n, a[n - 1]);

    free(a);                                   // PHAI tu giai phong
    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | Mảng tĩnh `int a[100]` | Mảng động `malloc` |
|---|---|---|
| **Kích thước** | ⚠️ Cố định lúc biên dịch | ✅ Quyết định lúc chạy (theo `n` nhập vào) |
| **Biết kích thước của mình** | ❌ Không (phải truyền `n` kèm) | ❌ Không (cũng phải tự giữ `n`) |
| **Thêm phần tử** | ❌ Không vượt được `MAX` | ✅ Mở rộng bằng `realloc` |
| **Kiểm tra biên** | ❌ Không | ❌ Không |
| **Giải phóng** | ✅ Tự động khi ra khỏi hàm | ⚠️ Phải gọi `free`, quên là rò rỉ bộ nhớ |
| **Lỗi khi hết bộ nhớ** | Crash (tràn stack) | ✅ `malloc` trả về `NULL`, kiểm tra được |
| **Bộ nhớ** | Stack (giới hạn ~1–8 MB) nếu khai báo trong hàm | Heap (lớn hơn rất nhiều) |
| **Truy cập phần tử** | `a[i]` | `a[i]` — giống hệt |
| **Tốc độ** | Nhanh, không tốn chi phí cấp phát | Có chi phí cấp phát ban đầu, truy cập nhanh tương đương |

**⚠️ Vấn đề của mảng tĩnh khi `n` lớn:**

```c
#include <stdio.h>

int main(void) {
    int a[10000000];       // 40 MB tren STACK -> Segmentation fault!
    a[0] = 1;
    printf("%d\n", a[0]);
    return 0;
}
```

Stack thường chỉ 1–8 MB. Mảng lớn phải khai báo **toàn cục** (ngoài `main`) hoặc cấp phát động bằng `malloc`.

**✅ Khuyến nghị:**
- **Học cơ bản / bài tập nhỏ / lập trình thi đấu:** mảng tĩnh (hoặc mảng toàn cục) vẫn ổn, đơn giản và nhanh
- **Khi kích thước chỉ biết lúc chạy hoặc rất lớn:** dùng `malloc`, luôn kiểm tra `NULL` và nhớ `free`

💡 Chi tiết về `malloc`, `calloc`, `realloc`, `free` được học ở bài [07-04 — Cấp phát mảng động](../07-04-c-cap-phat-mang-dong.md).
