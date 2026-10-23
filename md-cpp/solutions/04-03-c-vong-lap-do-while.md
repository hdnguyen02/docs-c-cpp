# Lời giải — [C]. Vòng Lặp Do-While

[← Quay lại bài học](../04-03-c-vong-lap-do-while.md)

> **Đặc trưng của `do while`:** thân vòng lặp chạy **ít nhất 1 lần** trước khi kiểm tra điều kiện. Phù hợp khi "làm rồi mới hỏi có làm tiếp không".

---

### Bài 1.

```c
#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int i = 1;
    do {
        printf("%d ", i);
        i++;
    } while (i <= n);

    printf("\n");
    return 0;
}
```

⚠️ Với `n = 0` hoặc `n` âm, chương trình **vẫn in ra số 1** — vì `do while` chạy trước rồi mới kiểm tra. Đây chính là điểm khác biệt cốt lõi so với `while`.

### Bài 2.

```c
#include <stdio.h>

int main(void) {
    int n;
    do {
        printf("Nhap mot so DUONG: ");
        scanf("%d", &n);
        if (n <= 0) printf("  -> Sai roi, phai la so duong!\n");
    } while (n <= 0);

    printf("Ban da nhap: %d\n", n);
    return 0;
}
```

**Đây là ứng dụng kinh điển nhất của `do while`** — kiểm tra dữ liệu đầu vào. Logic tự nhiên là "hỏi trước, kiểm tra sau", đúng thứ tự của `do while`.

Viết bằng `while` sẽ phải lặp code:

```c
printf("Nhap so duong: ");      // phai viet 2 lan
scanf("%d", &n);
while (n <= 0) {
    printf("Nhap so duong: ");  // lap lai
    scanf("%d", &n);
}
```

### Bài 3.

```c
#include <stdio.h>

int main(void) {
    double diem = -1;
    do {
        printf("Nhap diem (0 - 10): ");
        scanf("%lf", &diem);
        if (diem < 0 || diem > 10) {
            printf("  -> Diem phai tu 0 den 10!\n");
        }
    } while (diem < 0 || diem > 10);

    printf("Diem hop le: %g\n", diem);
    return 0;
}
```

💡 `%g` in số thực gọn (bỏ các số 0 thừa): `8.5` in ra `8.5`, `9` in ra `9`.

💡 **Xử lý khi người dùng nhập chữ thay vì số:** `scanf` trả về số biến đọc được; khi nhập chữ nó trả về 0 và **để nguyên** ký tự rác trong bộ đệm, nên vòng lặp sẽ thành vô hạn. Cách khắc phục:

```c
do {
    printf("Nhap diem (0 - 10): ");
    if (scanf("%lf", &diem) != 1) {
        int ch;
        while ((ch = getchar()) != '\n' && ch != EOF) { }   // bo du lieu rac
        diem = -1;                      // gan gia tri khong hop le de lap lai
        printf("  -> Phai nhap SO!\n");
    }
} while (diem < 0 || diem > 10);
```

### Bài 4.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    scanf("%d", &n);

    int tam = abs(n);
    int dem = 0;

    do {
        dem++;
        tam /= 10;
    } while (tam > 0);

    printf("%d co %d chu so\n", n, dem);
    return 0;
}
```

💡 **Ưu điểm so với `while`:** với `n = 0`, `do while` vẫn chạy 1 lần nên `dem = 1` — **đúng ngay mà không cần `if` đặc biệt**. Bản dùng `while` (bài [04-02](../04-02-c-vong-lap-while.md) bài 2) phải xử lý riêng trường hợp này.

Đây là ví dụ đẹp cho thấy chọn đúng loại vòng lặp giúp code ngắn và ít lỗi hơn.

### Bài 5.

```c
#include <stdio.h>

int main(void) {
    int chon;

    do {
        printf("\n========= MENU =========\n");
        printf("1. Them du lieu\n");
        printf("2. Xoa du lieu\n");
        printf("3. Hien thi danh sach\n");
        printf("4. Thoat\n");
        printf("========================\n");
        printf("Lua chon: ");
        if (scanf("%d", &chon) != 1) break;      // nhap sai kieu / het du lieu -> thoat

        switch (chon) {
            case 1: printf(">> Da THEM du lieu\n");    break;
            case 2: printf(">> Da XOA du lieu\n");     break;
            case 3: printf(">> Danh sach: (trong)\n"); break;
            case 4: printf(">> Tam biet!\n");          break;
            default: printf(">> Lua chon khong hop le!\n");
        }
    } while (chon != 4);

    return 0;
}
```

**Đây là mẫu chuẩn cho mọi chương trình quản lý** — kết hợp `do while` (hiện menu ít nhất 1 lần) với `switch case` (xử lý lựa chọn).

⚠️ Dòng `if (scanf(...) != 1) break;` đề phòng người dùng gõ chữ: nếu không có, `chon` giữ giá trị cũ và menu lặp vô hạn.

### Bài 6.

```c
#include <stdio.h>

int main(void) {
    char tiepTuc;

    do {
        double a, b;
        char pt;

        printf("\nNhap bieu thuc (vd: 5 + 3): ");
        scanf("%lf %c %lf", &a, &pt, &b);

        switch (pt) {
            case '+': printf("= %.4f\n", a + b); break;
            case '-': printf("= %.4f\n", a - b); break;
            case '*': printf("= %.4f\n", a * b); break;
            case '/':
                if (b == 0) printf("Loi: chia cho 0!\n");
                else        printf("= %.4f\n", a / b);
                break;
            default: printf("Phep toan khong hop le!\n");
        }

        printf("Tiep tuc? (y/n): ");
        scanf(" %c", &tiepTuc);        // dau cach truoc %c de bo qua '\n' con sot lai

    } while (tiepTuc == 'y' || tiepTuc == 'Y');

    printf("Tam biet!\n");
    return 0;
}
```

⚠️ **Bắt buộc có dấu cách trong `" %c"`.** Sau khi đọc số, phím Enter (`'\n'`) vẫn còn trong bộ đệm; nếu viết `"%c"` thì `tiepTuc` sẽ nhận ngay ký tự `'\n'` đó và vòng lặp kết thúc.

### Bài 7.

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
    srand((unsigned)time(NULL));
    int soBiMat = rand() % 100 + 1;
    int doan, soLan = 0;

    printf("=== DOAN SO (1-100) ===\n");

    do {
        printf("Doan cua ban: ");
        if (scanf("%d", &doan) != 1) return 1;
        soLan++;

        if      (doan < soBiMat) printf("  -> LON HON %d\n", doan);
        else if (doan > soBiMat) printf("  -> NHO HON %d\n", doan);
    } while (doan != soBiMat);

    printf("CHINH XAC! So lan doan: %d\n", soLan);
    return 0;
}
```

**So với bản `while(1) + break`** (bài [04-02](../04-02-c-vong-lap-while.md) bài 15): bản `do while` gọn hơn vì điều kiện dừng nằm tự nhiên ở cuối, không cần `break`.

### Bài 8.

```c
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void) {
    const char *MAT_KHAU_DUNG = "codelab2026";
    const int SO_LAN_TOI_DA = 3;

    char nhap[50];
    int soLan = 0;
    bool thanhCong = false;

    do {
        soLan++;
        printf("Lan %d/%d - Nhap mat khau: ", soLan, SO_LAN_TOI_DA);
        if (scanf("%49s", nhap) != 1) return 1;

        if (strcmp(nhap, MAT_KHAU_DUNG) == 0) {
            thanhCong = true;
        } else {
            printf("  -> Sai mat khau! Con %d lan thu.\n", SO_LAN_TOI_DA - soLan);
        }
    } while (!thanhCong && soLan < SO_LAN_TOI_DA);

    if (thanhCong) printf("\nDANG NHAP THANH CONG!\n");
    else           printf("\nTAI KHOAN BI KHOA (sai qua %d lan)\n", SO_LAN_TOI_DA);

    return 0;
}
```

**Điều kiện dừng kép:** `!thanhCong && soLan < SO_LAN_TOI_DA` — dừng khi **hoặc** đã đúng, **hoặc** hết lượt.

💡 **So sánh chuỗi trong C phải dùng `strcmp`** (trong `<string.h>`), trả về 0 khi 2 chuỗi giống nhau. Viết `nhap == MAT_KHAU_DUNG` chỉ so sánh **địa chỉ** hai mảng, luôn sai. `%49s` giới hạn đọc tối đa 49 ký tự để không tràn mảng 50 ô (chừa 1 ô cho `'\0'`).

⚠️ Trong ứng dụng thật, **không bao giờ** lưu mật khẩu dạng văn bản thuần trong code. Phải lưu **hash** (SHA-256, bcrypt) của mật khẩu.

### Bài 9.

**Với `n = 0`:**

| | Đoạn A (`while`) | Đoạn B (`do while`) |
|---|---|---|
| Output | *(không in gì)* | `0` |
| Số lần thân chạy | **0 lần** | **1 lần** |

**Giải thích:**

```c
// A: kiem tra TRUOC
int i = 0;
while (i > 0) { ... }        // 0 > 0 la SAI ngay -> khong chay lan nao

// B: chay TRUOC, kiem tra SAU
int i = 0;
do {
    printf("%d ", i);        // in 0
    i--;                     // i = -1
} while (i > 0);             // -1 > 0 SAI -> dung
```

**Đây là khác biệt duy nhất và cốt lõi giữa 2 loại vòng lặp:**

```
while:    KIEM TRA -> chay -> KIEM TRA -> chay -> ...   (co the chay 0 lan)
do while: chay -> KIEM TRA -> chay -> KIEM TRA -> ...   (chay it nhat 1 lan)
```

### Bài 10.

```c
#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int n;
    printf("Nhap n: ");
    scanf("%d", &n);

    bool am = (n < 0);
    long long tam = am ? -(long long)n : n;
    long long dao = 0;

    do {
        dao = dao * 10 + tam % 10;
        tam /= 10;
    } while (tam > 0);

    if (am) dao = -dao;
    printf("So dao nguoc = %lld\n", dao);
    return 0;
}
```

Với `n = 0`, `do while` cho kết quả `0` — đúng. Bản `while` cũng cho 0 (vì `dao` khởi tạo bằng 0), nên ở bài này cả hai đều được.

### Bài 11.

```c
#include <stdio.h>

int main(void) {
    int x, dem = 0;
    long long tong = 0;

    printf("Nhap cac so (dung khi tong > 100):\n");

    do {
        printf("  So thu %d: ", dem + 1);
        if (scanf("%d", &x) != 1) break;
        tong += x;
        dem++;
        printf("  Tong hien tai = %lld\n", tong);
    } while (tong <= 100);

    printf("\nDa nhap %d so, tong = %lld\n", dem, tong);
    return 0;
}
```

⚠️ Nếu người dùng nhập toàn số âm hoặc 0 thì vòng lặp chạy mãi. Nên thêm giới hạn an toàn:

```c
} while (tong <= 100 && dem < 1000);
```

### Bài 12.

```c
#include <stdio.h>

int main(void) {
    long long soDu = 1000000;
    int chon;

    do {
        printf("\n======== ATM CODELAB ========\n");
        printf("1. Xem so du\n");
        printf("2. Gui tien\n");
        printf("3. Rut tien\n");
        printf("4. Thoat\n");
        printf("=============================\n");
        printf("Chon chuc nang: ");
        if (scanf("%d", &chon) != 1) break;

        switch (chon) {
            case 1:
                printf(">> So du hien tai: %lld VND\n", soDu);
                break;

            case 2: {
                long long tien;
                printf(">> Nhap so tien gui: ");
                scanf("%lld", &tien);
                if (tien <= 0) {
                    printf("   Loi: so tien phai duong!\n");
                } else {
                    soDu += tien;
                    printf("   Da gui %lld VND. So du moi: %lld VND\n", tien, soDu);
                }
                break;
            }

            case 3: {
                long long tien;
                printf(">> Nhap so tien rut: ");
                scanf("%lld", &tien);
                if (tien <= 0) {
                    printf("   Loi: so tien phai duong!\n");
                } else if (tien % 50000 != 0) {
                    printf("   Loi: so tien phai la boi cua 50.000!\n");
                } else if (tien > soDu) {
                    printf("   Loi: so du khong du! (con %lld VND)\n", soDu);
                } else {
                    soDu -= tien;
                    printf("   Da rut %lld VND. So du con lai: %lld VND\n", tien, soDu);
                }
                break;
            }

            case 4:
                printf(">> Cam on quy khach. Tam biet!\n");
                break;

            default:
                printf(">> Chuc nang khong hop le!\n");
        }
    } while (chon != 4);

    return 0;
}
```

⚠️ Chú ý cặp `{ }` bọc quanh `case 2` và `case 3` — cần có khi khai báo biến mới bên trong `case` (xem bài [03-03](../03-03-c-switch-case.md) bài 3).

### Bài 13.

```c
int i = 1;
do {
    printf("%d ", i);
    i++;
} while (i <= 10)          // <- THIEU DAU CHAM PHAY
```

**Lỗi:** thiếu dấu `;` sau `while (i <= 10)`.

Thông báo lỗi (gcc):

```
error: expected ‘;’ before ‘return’
```

(Tên token sau chữ `before` tuỳ vào câu lệnh đứng ngay sau vòng lặp, ở đây là `return`.)

**Sửa:**

```c
} while (i <= 10);         // <- CO dau ;
```

**Ghi nhớ:** `do while` là loại vòng lặp **duy nhất** bắt buộc kết thúc bằng dấu `;`.

| Cấu trúc | Có `;` ở cuối? |
|---|---|
| `for (...) { }` | ❌ Không |
| `while (...) { }` | ❌ Không |
| `do { } while (...);` | ✅ **Có** |
| `if (...) { }` | ❌ Không |

Lý do: `do while` được coi là một **câu lệnh** hoàn chỉnh (giống `printf(...);`), còn `for`/`while` kết thúc bằng một khối `{ }`.

### Bài 14.

```c
#include <stdio.h>

int main(void) {
    int x;
    long long tong = 0;
    int dem = 0;

    printf("Nhap cac so nguyen (-1 de ket thuc):\n");

    do {
        if (scanf("%d", &x) != 1) break;
        if (x != -1) {
            tong += x;
            dem++;
        }
    } while (x != -1);

    printf("Da nhap %d so\n", dem);
    printf("Tong = %lld\n", tong);
    if (dem > 0) {
        printf("Trung binh = %.4f\n", (double)tong / dem);
    }
    return 0;
}
```

⚠️ Chú ý `if (x != -1)` bên trong — nếu không có, giá trị `-1` (giá trị đánh dấu kết thúc) cũng bị cộng vào tổng.

### Bài 15.

| Tiêu chí | `for` | `while` | `do while` |
|---|---|---|---|
| **Cú pháp** | `for (khoi_tao; dk; cap_nhat) { }` | `while (dk) { }` | `do { } while (dk);` |
| **Kiểm tra điều kiện** | Trước mỗi lần lặp | Trước mỗi lần lặp | **Sau** mỗi lần lặp |
| **Số lần chạy tối thiểu** | **0** | **0** | **1** |
| **Dấu `;` cuối** | Không | Không | ✅ **Có** |
| **Biết trước số lần lặp?** | ✅ Có | ❌ Thường không | ❌ Không |
| **Biến đếm** | Khai báo được ngay trong `for` (C99), tự huỷ sau vòng lặp | Phải khai báo bên ngoài | Phải khai báo bên ngoài |

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Duyệt mảng, lặp `n` lần đã biết | **`for`** |
| Đọc dữ liệu tới khi hết / gặp giá trị kết thúc | **`while`** |
| Lặp tới khi một điều kiện toán học thoả (chia tới khi bằng 0) | **`while`** |
| Menu chương trình | **`do while`** |
| Kiểm tra và bắt nhập lại dữ liệu | **`do while`** |
| Trò chơi "chơi tiếp không?" | **`do while`** |

**Về mặt kỹ thuật, cả 3 loại đều thay thế được nhau** — mọi `for` đều viết lại được bằng `while` và ngược lại. Việc chọn đúng loại chỉ để code **dễ đọc và ít lỗi hơn**, không ảnh hưởng tốc độ.

```c
// Cung mot viec, 3 cach viet
for (int i = 1; i <= 5; i++) printf("%d", i);

int i = 1;
while (i <= 5) { printf("%d", i); i++; }

int j = 1;
do { printf("%d", j); j++; } while (j <= 5);
```
