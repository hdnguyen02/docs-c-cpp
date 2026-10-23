# Lời giải — [C]. Chú Thích - Comment

[← Quay lại bài học](../02-04-c-chu-thich-comment.md)

---

### Bài 1.

```c
#include <stdio.h>

int main() {
    double day, chieuCao;                  // khai bao 2 bien luu day va chieu cao

    printf("Nhap do dai day: ");           // hien thi loi nhac nguoi dung
    scanf("%lf", &day);                    // doc gia tri day tu ban phim (double dung %lf)

    printf("Nhap chieu cao: ");
    scanf("%lf", &chieuCao);

    double dienTich = 0.5 * day * chieuCao;  // cong thuc S = (day x cao) / 2

    printf("Dien tich tam giac = %g\n", dienTich);  // %g in gon, bo so 0 thua
    return 0;
}
```

### Bài 2.

```c
/*
 * ============================================================
 * Ten file    : tinh_diem.c
 * Tac gia     : Nguyen Van A
 * Ngay viet   : 17/09/2026
 * Mo ta       : Chuong trinh nhap diem 3 mon (Toan, Ly, Hoa),
 *               tinh diem trung binh va xep loai hoc luc.
 * Bien dich   : gcc -std=c11 -Wall tinh_diem.c -o tinh_diem
 * ============================================================
 */

#include <stdio.h>

int main() {
    double toan, ly, hoa;

    printf("Nhap diem Toan, Ly, Hoa: ");
    scanf("%lf %lf %lf", &toan, &ly, &hoa);

    double dtb = (toan + ly + hoa) / 3;
    printf("Diem trung binh: %.2f\n", dtb);

    return 0;
}
```

**Vì sao nên có header comment:** khi bạn có hàng trăm file bài tập, header giúp nhận ra ngay file này làm gì mà không cần đọc code. Nhiều trường/công ty cũng bắt buộc có phần này.

### Bài 3.

```c
#include <stdio.h>

int main() {
    printf("Dong 1\n");

    /*
    printf("Dong 2\n");
    printf("Dong 3\n");
    printf("Dong 4\n");
    */

    printf("Dong 5\n");
    return 0;
}
```

Output:

```
Dong 1
Dong 5
```

**Ứng dụng thực tế:** đây là kỹ thuật debug cơ bản nhất — tạm "tắt" một đoạn code để xác định nó có phải nguyên nhân gây lỗi hay không, mà không phải xoá đi rồi gõ lại.

### Bài 4.

**Output:**

```
AD
```

**Giải thích từng dòng:**

```
printf("A");  // printf("B");     <- tu dau // toi HET DONG deu la chu thich
                                  //    -> "B" khong duoc in
/* printf("C"); */                <- toan bo nam trong /* */ -> khong in "C"
printf("D");                      <- lenh binh thuong -> in "D"
```

### Bài 5.

**Lỗi:** C **không hỗ trợ chú thích lồng nhau** (nested comment).

```
/* Day la chu thich
   /* chu thich long nhau */   <- chu thich KET THUC tai day
   van con chu thich? */        <- day la CODE, khong hop le
```

Compiler đọc từ `/*` đầu tiên và kết thúc ở `*/` **đầu tiên** nó gặp. Phần `van con chu thich? */` bị coi là mã nguồn → gcc báo lỗi (thông báo cụ thể tuỳ phiên bản), đại loại:

```
warning: "/*" within comment [-Wcomment]
error: unknown type name 'van'
```

**Cách khắc phục:** dùng `//` cho từng dòng khi cần "chú thích chồng chú thích":

```c
// /* Day la chu thich
//    /* chu thich long nhau */
//    van con chu thich? */
```

Đây cũng là lý do nên dùng phím tắt `Ctrl + /` (comment từng dòng bằng `//`) thay vì bọc `/* */` khi tạm tắt code — vì đoạn code bạn tắt rất có thể đã chứa sẵn `/* */` bên trong.

💡 Trong C còn một cách "tắt" cả khối code an toàn dù bên trong có `/* */`: bọc bằng `#if 0 ... #endif` (tiền xử lý bỏ qua toàn bộ phần giữa).

### Bài 6.

```c
#include <stdio.h>
#include <math.h>

int main() {
    const double PI = 3.14159265358979;
    double r;

    printf("Nhap ban kinh: ");
    scanf("%lf", &r);

    // --- PHUONG AN 1 (dang dung): dung hang PI tu dinh nghia ---
    double chuVi = 2 * PI * r;

    /* --- PHUONG AN 2 (da thu, bo): dung acos(-1) de lay PI ---
       Uu diem : chinh xac toi da theo kieu double, khong phai go tay so PI
       Nhuoc diem: goi ham luong giac, cham hon mot chut, kho doc voi nguoi moi
       double chuVi = 2 * acos(-1.0) * r;
    */

    printf("Chu vi = %g\n", chuVi);
    return 0;
}
```

*(Nếu bật lại phương án 2 thì cần `#include <math.h>` và thêm `-lm` khi biên dịch bằng gcc.)*

**Lưu ý:** giữ lại phương án cũ dưới dạng chú thích chỉ nên làm **tạm thời** khi đang thử nghiệm. Trong dự án thật, code cũ nên được xoá và lưu lại bằng Git, vì "code chết" nằm trong chú thích lâu ngày sẽ lỗi thời và gây nhiễu.

### Bài 7.

**Chú thích KHÔNG được đưa vào file thực thi.** Chúng bị loại bỏ ngay ở giai đoạn **tiền xử lý (preprocessing)**, trước cả bước biên dịch.

Thí nghiệm chứng minh:

```c
// file a.c
#include <stdio.h>
int main() { printf("Hello"); return 0; }
```

```c
// file b.c  -- giong het a.c nhung them 100 dong chu thich
#include <stdio.h>
// chu thich 1
// chu thich 2
// ... (den 100)
int main() { printf("Hello"); return 0; }
```

```bash
gcc a.c -o a
gcc b.c -o b
ls -l a b
# -rwxr-xr-x 1 user user 15960 ... a
# -rwxr-xr-x 1 user user 15960 ... b     <- KICH THUOC Y HET NHAU
```

Xem trực tiếp kết quả sau bước tiền xử lý (chú thích đã biến mất):

```bash
gcc -E b.c | tail -5
```

**Kết luận:** viết chú thích **không làm chương trình chạy chậm hơn hay nặng hơn một byte nào**. Đừng bao giờ tiếc chú thích vì sợ "nặng file".

### Bài 8.

```c
#include <stdio.h>

int main() {
    // Bai toan: kiem tra 153 co phai SO ARMSTRONG 3 chu so khong
    // (so Armstrong: tong lap phuong cac chu so bang chinh no, vd 153 = 1^3 + 5^3 + 3^3)

    int n = 153;    // so can kiem tra
    int t = 0;      // t = tong lap phuong cac chu so
    int x = n;      // x = ban sao cua n de "bao mon" dan, giu nguyen n de so sanh cuoi

    while (x > 0) {
        int d = x % 10;   // lay chu so HANG DON VI cua x
        t += d * d * d;   // cong lap phuong chu so do vao tong
        x /= 10;          // bo chu so vua xet (chia nguyen cho 10)
    }

    printf("%d\n", t == n);   // in 1 neu la so Armstrong, 0 neu khong
    return 0;
}
```

**Hai kỹ thuật cần nhớ:**
- `x % 10` → lấy chữ số cuối cùng
- `x /= 10` → xoá chữ số cuối cùng

Kết hợp trong vòng `while (x > 0)` là cách duyệt qua từng chữ số của một số nguyên.

### Bài 9.

**① Chú thích giải thích *CÁI GÌ* (what)** — mô tả code đang làm gì. Thường **thừa** nếu code đã rõ ràng.

```c
i++;                          // tang i len 1     <- THUA, code da noi ro
int soHocSinh = 45;           // gan 45 cho bien  <- THUA
```

Dùng hợp lý khi đoạn code thực sự khó đọc:

```c
// Sap xep mang giam dan theo diem, neu bang diem thi theo ten tang dan
qsort(ds, n, sizeof(ds[0]), cmp);
```

**② Chú thích giải thích *TẠI SAO* (why)** — loại **giá trị nhất**, vì code không bao giờ tự nói được lý do.

```c
// Dung long long vi tong co the vuot 2 ty khi n > 65000
long long tong = 0;

// Cong 1e-9 de tranh loi lam tron khi so thuc sat nguong .5
int lamTron = (int)(x + 0.5 + 1e-9);

// Khong dung binary search o day vi mang chua chac da sap xep
```

**③ Ghi chú *VIỆC CẦN LÀM* (TODO / FIXME / HACK)**

```c
// TODO: them kiem tra n <= 0 truoc khi tinh
// FIXME: bi sai khi nhap so am, tam thoi chua xu ly
// HACK: hard-code 100 phan tu, se doi sang cap phat dong (malloc) sau
// NOTE: thuat toan nay O(n^2), du dung voi n <= 1000
```

Hầu hết IDE đều tự động tô sáng và liệt kê được các từ khoá `TODO`, `FIXME`.

### Bài 10.

| Chú thích | Đánh giá | Lý do |
|---|---|---|
| `i++;  // tang i len 1` | ❌ **Tồi** | Chỉ đọc lại code bằng tiếng Việt, không thêm thông tin gì |
| `tong += a[i];  // cong a[i] vao tong` | ❌ **Tồi** | Tương tự — code đã tự nói rõ |
| `x = x ^ (x >> 16);  // tron bit de giam va cham hash` | ✅ **Tốt** | Code hoàn toàn không tự giải thích được; chú thích cho biết **mục đích** |
| `delay(100);  // cho 100ms` | ⚠️ **Nửa vời** | Đọc lại code. Nên viết **tại sao**: `// cho cam bien on dinh sau khi cap nguon` |

**Nguyên tắc:** *Code nói **cái gì**, chú thích nói **tại sao**.* Nếu phải viết chú thích để giải thích code đang làm gì, thường là dấu hiệu nên **đặt lại tên biến/hàm** cho rõ hơn:

```c
// Thay vi:
int d;    // so ngay con lai den han

// Hay viet:
int soNgayConLai;
```

Và nhớ: **chú thích sai còn tệ hơn không có chú thích**, vì nó đánh lừa người đọc. Khi sửa code, phải sửa cả chú thích.

### Bài 11.

```c
#include <stdio.h>

/**
 * @brief   Tinh giai thua cua mot so nguyen khong am.
 *
 * Ham su dung vong lap (khong de quy) de tranh tran stack voi n lon.
 * Ket qua kieu long long nen chi dung dung toi n = 20;
 * tu n = 21 tro di se bi tran so.
 *
 * @param n  So nguyen khong am can tinh giai thua (0 <= n <= 20).
 * @return   Gia tri n! ; tra ve -1 neu n am.
 *
 * @note     0! = 1 theo dinh nghia.
 * @warning  Khong kiem tra tran so voi n > 20.
 *
 * @code
 *     printf("%lld", giaiThua(5));   // in ra 120
 * @endcode
 */
long long giaiThua(int n) {
    if (n < 0) return -1;

    long long kq = 1;
    for (int i = 2; i <= n; i++) {
        kq *= i;
    }
    return kq;
}

int main() {
    printf("%lld\n", giaiThua(5));    // 120
    return 0;
}
```

**Doxygen là gì:** công cụ tự động sinh tài liệu (HTML/PDF) từ chú thích trong mã nguồn. Chú thích Doxygen bắt đầu bằng `/**` và dùng các thẻ `@brief`, `@param`, `@return`, `@note`, `@warning`.

Lợi ích ngay cả khi không chạy Doxygen: VSCode, CLion, Visual Studio đều **đọc được** định dạng này và hiện gợi ý mô tả hàm khi bạn gõ tên hàm.

### Bài 12.

Bài thực hành. Kết quả thường thấy: với cùng một đoạn code ~20 dòng, người đọc bản **không có chú thích** mất gấp 2–3 lần thời gian, và hay hiểu sai mục đích chương trình.

Nhưng lưu ý bài học ngược lại: nếu bạn phải viết **rất nhiều** chú thích để người khác hiểu, có thể code của bạn đang quá rối. Ưu tiên theo thứ tự:

1. Đặt tên biến/hàm rõ nghĩa
2. Tách hàm nhỏ, mỗi hàm làm một việc
3. *Rồi mới* thêm chú thích cho phần còn lại thực sự khó

### Bài 13.

| IDE | Comment/Uncomment nhiều dòng |
|---|---|
| VSCode | `Ctrl + /` (macOS: `Cmd + /`) — comment bằng `//`<br>`Shift + Alt + A` — comment khối `/* */` |
| DevC++ | `Ctrl + /` |
| Code::Blocks | `Ctrl + Shift + C` (comment), `Ctrl + Shift + X` (uncomment) |
| CLion / IntelliJ | `Ctrl + /` (dòng), `Ctrl + Shift + /` (khối) |
| Visual Studio | `Ctrl + K, Ctrl + C` (comment), `Ctrl + K, Ctrl + U` (uncomment) |
| Sublime Text | `Ctrl + /` |
| Vim | `gc` + phạm vi (với plugin commentary) |

**Cách dùng:** bôi đen nhiều dòng rồi bấm phím tắt. Bấm lần nữa để bỏ chú thích.

### Bài 14.

Chương trình có lỗi (kết quả sai, không báo lỗi biên dịch):

```c
#include <stdio.h>

int main() {
    int a = 10, b = 3;
    int tong   = a + b;
    int hieu   = a - b;
    int tich   = a * b;
    int thuong = a / b;        // <- nghi ngo: chia nguyen, mat phan thap phan

    printf("Tong   = %d\n", tong);
    printf("Hieu   = %d\n", hieu);
    printf("Tich   = %d\n", tich);
    printf("Thuong = %d\n", thuong);   // in ra 3 thay vi 3.333
    return 0;
}
```

Quy trình gỡ lỗi bằng chú thích ("chia đôi để tìm"):

```c
    printf("Tong   = %d\n", tong);
    // printf("Hieu   = %d\n", hieu);     <- tat thu
    // printf("Tich   = %d\n", tich);     <- tat thu
    printf("Thuong = %d\n", thuong);      // <- van sai -> loi nam o day
```

Khoanh vùng được rồi, in thêm biến trung gian để xác nhận:

```c
    printf("DEBUG: a = %d, b = %d\n", a, b);
    printf("DEBUG: a / b = %d\n", a / b);                  // 3  -> chia nguyen!
    printf("DEBUG: (double)a / b = %f\n", (double)a / b);  // 3.333333
```

**Nguyên nhân:** `a` và `b` đều là `int` nên `a / b` là **phép chia nguyên**. Sửa:

```c
double thuong = (double)a / b;      // 3.333333
printf("Thuong = %f\n", thuong);    // nho doi %d thanh %f
```

⚠️ Trong C còn một bẫy nữa khi debug: in số thực bằng `%d` (hoặc in `int` bằng `%f`) là **sai đặc tả**, kết quả rác. Bật `-Wall` để gcc cảnh báo những chỗ này.

### Bài 15.

File mẫu `template.c`:

```c
/*
 * ============================================================
 *  Bai tap    : <so bai> - <ten bai tap>
 *  Chuong     : <so chuong> - <ten chuong>
 *  Tac gia    : <ten cua ban>
 *  Ngay       : dd/mm/yyyy
 *
 *  De bai     : <chep tom tat de bai vao day>
 *
 *  Input      : <mo ta du lieu vao>
 *  Output     : <mo ta du lieu ra>
 *
 *  Vi du:
 *      Input : 5
 *      Output: 120
 *
 *  Y tuong    : <ghi ngan gon cach giai truoc khi code>
 *
 *  Bien dich  : gcc -std=c11 -Wall -Wextra -g main.c -o main -lm
 * ============================================================
 */

#include <stdio.h>

int main() {
    // ---------- Khai bao bien ----------

    // ---------- Nhap du lieu ----------

    // ---------- Xu ly ----------

    // ---------- Xuat ket qua ----------

    return 0;
}
```

**Mẹo dùng lại nhanh:**

```bash
cp template.c bai01.c      # moi bai tap chi can copy ra
```

Trong VSCode, bạn còn có thể biến nó thành **User Snippet** (`File → Preferences → Configure User Snippets → c.json`) để gõ vài ký tự là sinh ra cả khung.

Phần **"Ý tưởng"** trong mẫu rất quan trọng: tập thói quen viết cách giải bằng tiếng Việt *trước khi* gõ code sẽ giúp bạn code nhanh và ít sai hơn nhiều.
