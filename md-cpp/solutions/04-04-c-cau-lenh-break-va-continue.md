# Lời giải — [C]. Câu Lệnh Break Và Continue

[← Quay lại bài học](../04-04-c-cau-lenh-break-va-continue.md)

> **`break`** — thoát **hẳn** khỏi vòng lặp (hoặc `switch`).
> **`continue`** — bỏ qua phần còn lại của **lần lặp hiện tại**, nhảy sang lần lặp kế tiếp.

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 20; i++) {
        if (i % 7 == 0) {
            printf("\nGap so %d chia het cho 7 -> DUNG\n", i);
            break;
        }
        printf("%d ", i);
    }
    return 0;
}
```

Output:

```
1 2 3 4 5 6 
Gap so 7 chia het cho 7 -> DUNG
```

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) continue;      // bo qua, khong in
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

Output: `1 2 4 5 7 8 10 11 13 14 16 17 19 20`

### Bài 3.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    if (n < 2) {
        printf("%d KHONG phai so nguyen to\n", n);
        return 0;
    }

    bool nguyenTo = true;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) {
            nguyenTo = false;
            break;                      // tim thay uoc -> khong can duyet tiep
        }
    }

    printf("%d %s so nguyen to\n", n, nguyenTo ? "LA" : "KHONG phai");
    return 0;
}
```

💡 **Vì sao `break` quan trọng ở đây:** với `n = 1000000000` (số chẵn), không có `break` thì vòng lặp vẫn chạy hết ~31.623 bước; có `break` thì dừng ngay ở bước đầu tiên.

### Bài 4.

```c
#include <stdio.h>

int main(void) {
    long long tong = 0;
    int x, demDuong = 0;

    printf("Nhap cac so (0 de dung):\n");

    while (1) {
        if (scanf("%d", &x) != 1) break;   // het du lieu / nhap sai kieu

        if (x == 0) break;             // dieu kien DUNG
        if (x < 0)  continue;          // BO QUA so am

        tong += x;
        demDuong++;
    }

    printf("Co %d so duong, tong = %lld\n", demDuong, tong);
    return 0;
}
```

Ví dụ nhập `5 -3 10 -7 8 0`:

```
Co 3 so duong, tong = 23
```

**Mẫu code rất hay dùng:** `while (1)` + `break` cho điều kiện dừng + `continue` cho điều kiện bỏ qua. Cách này tách bạch 2 loại điều kiện rất rõ ràng.

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    for (int i = 100; i <= 1000; i++) {
        if (i % 7 == 0 && i % 11 == 0) {
            printf("So dau tien: %d\n", i);
            break;
        }
    }
    return 0;
}
```

Output: `So dau tien: 154`

💡 Chia hết cho cả 7 và 11 ⟺ chia hết cho 77. Số đầu tiên ≥ 100 là `77 × 2 = 154`.

### Bài 6.

```c
#include <stdio.h>
#include <stdbool.h>

bool laNguyenTo(int n) {
    if (n < 2) return false;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main(void) {
    int dem = 0;

    printf("10 so nguyen to dau tien: ");
    for (int n = 2; ; n++) {           // vong lap khong co dieu kien dung
        if (laNguyenTo(n)) {
            printf("%d ", n);
            dem++;
            if (dem == 10) break;      // du 10 so thi dung
        }
    }
    printf("\n");
    return 0;
}
```

Output: `2 3 5 7 11 13 17 19 23 29`

💡 `for (int n = 2; ; n++)` — bỏ trống phần điều kiện nghĩa là **luôn đúng**, vòng lặp chỉ dừng bằng `break`. Đây là cách xử lý bài toán "tìm đủ k phần tử" khi không biết cần duyệt tới đâu.

*(Hàm `laNguyenTo` sẽ được học kỹ ở bài [05-01](../05-01-c-ham-function.md).)*

### Bài 7.

**Output:**

```
1 2 4 5 
1 2 
```

**Giải thích:**

**Vòng 1 (`continue`):** khi `i == 3`, `continue` **bỏ qua `printf`** nhưng vòng lặp **vẫn tiếp tục** với `i = 4, 5`.

```
i=1 -> in 1
i=2 -> in 2
i=3 -> continue -> bo qua printf, nhay len i++
i=4 -> in 4
i=5 -> in 5
```

**Vòng 2 (`break`):** khi `i == 3`, `break` **thoát hẳn** vòng lặp, `i = 4, 5` không bao giờ chạy.

```
i=1 -> in 1
i=2 -> in 2
i=3 -> break -> THOAT
```

**Sơ đồ:**

```
continue:  [1] [2] [X] [4] [5]     <- nhay qua, roi tiep tuc
break:     [1] [2] [STOP]          <- dung han
```

### Bài 8.

```c
int i = 1;
while (i <= 10) {
    if (i % 2 == 0) continue;      // <- LOI: nhay qua ca i++
    printf("%d ", i);
    i++;
}
```

**Lỗi:** khi `i` chẵn (ví dụ `i = 2`), `continue` nhảy thẳng về đầu vòng lặp — **bỏ qua luôn câu `i++`**. Nên `i` mãi bằng 2, điều kiện `i <= 10` luôn đúng → lặp vô hạn.

**Sửa cách 1 — tăng `i` trước khi `continue`:**

```c
int i = 0;
while (i < 10) {
    i++;                           // tang TRUOC
    if (i % 2 == 0) continue;
    printf("%d ", i);
}
```

**Sửa cách 2 — dùng `for` (an toàn nhất):**

```c
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;
    printf("%d ", i);
}
```

⚠️ **Đây là lý do `continue` an toàn với `for` nhưng nguy hiểm với `while`.** Trong `for`, phần cập nhật `i++` nằm trong chính cấu trúc `for` nên **`continue` vẫn thực hiện nó**. Trong `while`, phần cập nhật nằm trong thân nên bị bỏ qua.

### Bài 9.

```c
#include <stdio.h>

int main(void) {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            if (i + j > 6) break;          // chi thoat vong TRONG
            printf("(%d,%d) ", i, j);
        }
        printf("\n");
    }
    return 0;
}
```

Output:

```
(1,1) (1,2) (1,3) (1,4) (1,5) 
(2,1) (2,2) (2,3) (2,4) 
(3,1) (3,2) (3,3) 
(4,1) (4,2) 
(5,1) 
```

Chú ý: sau `break`, vòng **ngoài** vẫn chạy tiếp sang `i` kế tiếp.

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    // --- CHUNG MINH: break chi thoat vong TRONG CUNG ---
    printf("=== break thuong ===\n");
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            if (j == 2) break;
            printf("%d-%d  ", i, j);
        }
    }
    printf("\n(Vong ngoai van chay du 3 lan)\n\n");

    // --- CACH 1: dung CO (flag) ---
    printf("=== Cach 1: dung co ===\n");
    bool thoat = false;
    for (int i = 1; i <= 3 && !thoat; i++) {
        for (int j = 1; j <= 3; j++) {
            if (i == 2 && j == 2) { thoat = true; break; }
            printf("%d-%d  ", i, j);
        }
    }
    printf("\n");

    // --- CACH 2: dung goto ---
    printf("=== Cach 2: goto ===\n");
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            if (i == 2 && j == 2) goto ketThuc;
            printf("%d-%d  ", i, j);
        }
    }
ketThuc:
    printf("\n");

    return 0;
}
```

**3 cách thoát nhiều vòng lặp cùng lúc:**

**① Dùng cờ (flag)** — phổ biến và an toàn nhất:

```c
bool timThay = false;
for (int i = 0; i < n && !timThay; i++) {
    for (int j = 0; j < m; j++) {
        if (dieuKien) { timThay = true; break; }
    }
}
```

**② Dùng `goto`** — ngắn gọn; trong C, thoát nhiều vòng lặp lồng nhau là một trong số ít trường hợp `goto` được chấp nhận rộng rãi (trường hợp còn lại hay gặp là nhảy tới đoạn dọn dẹp tài nguyên khi gặp lỗi):

```c
for (...) { for (...) { if (dk) goto xong; } }
xong:
```

**③ Tách thành hàm rồi `return`** — sạch nhất. C không trả về được 2 giá trị cùng lúc, nên ghi kết quả qua **con trỏ** (sẽ học ở chương 5 và 7):

```c
bool timKiem(int n, int m, int *ri, int *rj) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (dieuKien) { *ri = i; *rj = j; return true; }   // thoat CA HAI vong
    return false;
}
```

**Khuyến nghị:** ưu tiên cách ③ (tách hàm) vì code rõ ràng nhất; nếu không tiện thì dùng cách ①.

### Bài 11.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    const int MUC_TIEU = 2025;
    bool timThay = false;

    for (int a = 1; a <= 100 && !timThay; a++) {
        for (int b = 1; b <= 100; b++) {
            if (a * a + b * b == MUC_TIEU) {
                printf("Tim thay: a = %d, b = %d\n", a, b);
                printf("%d^2 + %d^2 = %d + %d = %d\n", a, b, a * a, b * b, MUC_TIEU);
                timThay = true;
                break;
            }
        }
    }

    if (!timThay) printf("Khong tim thay cap nao\n");
    return 0;
}
```

Output:

```
Tim thay: a = 27, b = 36
27^2 + 36^2 = 729 + 1296 = 2025
```

💡 Cách tối ưu hơn: chỉ cần vòng lặp **một** biến, tính `b` từ `a` (cần `#include <math.h>` và biên dịch thêm `-lm`):

```c
for (int a = 1; a * a < MUC_TIEU; a++) {
    int con = MUC_TIEU - a * a;
    int b = (int)(sqrt(con) + 0.5);
    if (b * b == con) { /* tim thay */ break; }
}
```

Giảm từ 10.000 phép thử xuống còn ~45.

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int x;
    int maxSo = 0;
    bool coSo = false;

    printf("Nhap cac so (so am de dung):\n");

    while (1) {
        if (scanf("%d", &x) != 1) break;

        if (x < 0)  break;            // DUNG khi gap so am
        if (x == 0) continue;         // BO QUA so 0

        if (!coSo || x > maxSo) {
            maxSo = x;
            coSo = true;
        }
    }

    if (coSo) printf("So lon nhat (khac 0) = %d\n", maxSo);
    else      printf("Khong co so nao hop le\n");

    return 0;
}
```

### Bài 13.

```c
#include <stdio.h>

int main(void) {
    long long tong = 0;

    for (int i = 1; i <= 100; i++) {
        if (i % 15 == 0) continue;         // bo qua boi cua ca 3 va 5

        printf("%d ", i);
        tong += i;

        if (tong > 1000) {
            printf("\n-> Tong = %lld > 1000, DUNG tai i = %d\n", tong, i);
            break;
        }
    }
    return 0;
}
```

Output:

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 21 22 23 24 25 26 27 28 29 31 32 33 34 35 36 37 38 39 40 41 42 43 44 46 47 
-> Tong = 1038 > 1000, DUNG tai i = 47
```

💡 Chia hết cho cả 3 và 5 ⟺ chia hết cho BCNN(3,5) = **15**.

### Bài 14.

```c
#include <stdio.h>

int main(void) {
    double diem, tong = 0;
    int dem = 0, soLoi = 0;

    printf("Nhap diem sinh vien (-1 de ket thuc):\n");

    while (1) {
        printf("  Diem: ");
        if (scanf("%lf", &diem) != 1) break;

        if (diem == -1) break;                    // KET THUC

        if (diem < 0 || diem > 10) {              // KHONG HOP LE -> bo qua
            printf("    -> Diem khong hop le (phai tu 0 den 10)!\n");
            soLoi++;
            continue;
        }

        tong += diem;
        dem++;
    }

    printf("\n--- KET QUA ---\n");
    printf("So diem hop le   : %d\n", dem);
    printf("So diem bi loi   : %d\n", soLoi);

    if (dem > 0) {
        printf("Tong diem        : %.2f\n", tong);
        printf("Diem trung binh  : %.2f\n", tong / dem);
    } else {
        printf("Khong co diem hop le nao.\n");
    }
    return 0;
}
```

### Bài 15.

| | `break` | `return` | `goto` |
|---|---|---|---|
| **Thoát khỏi** | Vòng lặp / `switch` gần nhất | Toàn bộ **hàm** | Nhảy tới **nhãn** bất kỳ trong cùng hàm |
| **Thoát nhiều vòng lặp** | ❌ Chỉ 1 vòng | ✅ Tất cả | ✅ Tất cả |
| **Trả về giá trị** | ❌ Không | ✅ Có | ❌ Không |
| **Dễ đọc** | ✅ Rất rõ | ✅ Rõ | ⚠️ Dễ gây rối |
| **Được khuyến nghị** | ✅ Có | ✅ Có | ⚠️ Chỉ trong vài trường hợp |

**① `break` — dùng khi:** thoát một vòng lặp, kết thúc `case` trong `switch`. Đây là lựa chọn mặc định.

```c
for (int i = 0; i < n; i++) {
    if (a[i] == target) { viTri = i; break; }
}
```

**② `return` — dùng khi:** đang trong một hàm và đã có kết quả. **Sạch nhất** khi cần thoát nhiều vòng lặp:

```c
int timKiem(int a[][100], int n, int m, int x) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (a[i][j] == x) return i * m + j;   // thoat CA HAI vong
    return -1;
}
```

**③ `goto` — chỉ dùng khi:** cần thoát nhiều vòng lặp lồng nhau mà không tiện tách hàm (hoặc nhảy tới đoạn dọn dẹp chung khi xử lý lỗi).

```c
for (...) {
    for (...) {
        for (...) {
            if (dieuKien) goto xong;
        }
    }
}
xong:
    printf("Da thoat ca 3 vong lap\n");
```

**Vì sao `goto` bị ghét:** nó cho phép nhảy **bất kỳ đâu** trong hàm, tạo ra code "mì spaghetti" — luồng thực thi rối như tơ vò, không thể lần theo. Bài báo nổi tiếng năm 1968 của Edsger Dijkstra, *"Go To Statement Considered Harmful"*, đã khiến nhiều ngôn ngữ ra đời sau loại bỏ nó (Java, Python không có `goto`).

⚠️ `goto` còn có bẫy kỹ thuật: nếu nhảy **qua** câu lệnh khai báo có khởi tạo, C vẫn biên dịch được (chỉ cấm nhảy vào phạm vi của mảng độ dài biến — VLA), nhưng biến đó sẽ **chưa được khởi tạo** khi dùng:

```c
goto nhan;
int x = 10;      // bi nhay qua: x ton tai nhung KHONG duoc gan 10
nhan:
printf("%d", x); // gia tri rac!
```

**Kết luận thực dụng:**
1. Mặc định dùng `break`
2. Trong hàm và đã có kết quả → `return`
3. Nhiều vòng lặp lồng nhau → **tách thành hàm** rồi `return` (tốt nhất), hoặc dùng cờ
4. `goto` — chỉ khi 3 cách trên đều bất tiện, và nhớ đặt nhãn ngay sau vòng lặp
