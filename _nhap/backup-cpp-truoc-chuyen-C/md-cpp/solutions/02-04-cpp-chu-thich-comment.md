# Lời giải — [C++]. Chú Thích - Comment

[← Quay lại bài học](../02-04-cpp-chu-thich-comment.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    double day, chieuCao;                  // khai bao 2 bien luu day va chieu cao

    cout << "Nhap do dai day: ";           // hien thi loi nhac nguoi dung
    cin >> day;                            // doc gia tri day tu ban phim

    cout << "Nhap chieu cao: ";
    cin >> chieuCao;

    double dienTich = 0.5 * day * chieuCao;  // cong thuc S = (day x cao) / 2

    cout << "Dien tich tam giac = " << dienTich << endl;
    return 0;
}
```

### Bài 2.

```cpp
/*
 * ============================================================
 * Ten file    : tinh_diem.cpp
 * Tac gia     : Nguyen Van A
 * Ngay viet   : 17/09/2026
 * Mo ta       : Chuong trinh nhap diem 3 mon (Toan, Ly, Hoa),
 *               tinh diem trung binh va xep loai hoc luc.
 * Bien dich   : g++ -std=c++17 -Wall tinh_diem.cpp -o tinh_diem
 * ============================================================
 */

#include <iostream>
using namespace std;

int main() {
    double toan, ly, hoa;

    cout << "Nhap diem Toan, Ly, Hoa: ";
    cin >> toan >> ly >> hoa;

    double dtb = (toan + ly + hoa) / 3;
    cout << "Diem trung binh: " << dtb << endl;

    return 0;
}
```

**Vì sao nên có header comment:** khi bạn có hàng trăm file bài tập, header giúp nhận ra ngay file này làm gì mà không cần đọc code. Nhiều trường/công ty cũng bắt buộc có phần này.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Dong 1" << endl;

    /*
    cout << "Dong 2" << endl;
    cout << "Dong 3" << endl;
    cout << "Dong 4" << endl;
    */

    cout << "Dong 5" << endl;
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

```cpp
cout << "A";  // cout << "B";     <- tu dau // toi HET DONG deu la chu thich
                                 //    -> "B" khong duoc in
/* cout << "C"; */               <- toan bo nam trong /* */ -> khong in "C"
cout << "D";                     <- lenh binh thuong -> in "D"
```

### Bài 5.

**Lỗi:** C++ **không hỗ trợ chú thích lồng nhau** (nested comment).

```cpp
/* Day la chu thich
   /* chu thich long nhau */   <- chu thich KET THUC tai day
   van con chu thich? */        <- day la CODE, khong hop le
```

Compiler đọc từ `/*` đầu tiên và kết thúc ở `*/` **đầu tiên** nó gặp. Phần `van con chu thich? */` bị coi là mã nguồn → lỗi:

```
error: 'van' does not name a type
warning: "/*" within comment
```

**Cách khắc phục:** dùng `//` cho từng dòng khi cần "chú thích chồng chú thích":

```cpp
// /* Day la chu thich
//    /* chu thich long nhau */
//    van con chu thich? */
```

Đây cũng là lý do nên dùng phím tắt `Ctrl + /` (comment từng dòng bằng `//`) thay vì bọc `/* */` khi tạm tắt code — vì đoạn code bạn tắt rất có thể đã chứa sẵn `/* */` bên trong.

### Bài 6.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    const double PI = 3.14159265358979;
    double r;

    cout << "Nhap ban kinh: ";
    cin >> r;

    // --- PHUONG AN 1 (dang dung): dung hang PI tu dinh nghia ---
    double chuVi = 2 * PI * r;

    /* --- PHUONG AN 2 (da thu, bo): dung acos(-1) de lay PI ---
       Uu diem : chinh xac toi da theo kieu double, khong phai go tay so PI
       Nhuoc diem: goi ham luong giac, cham hon mot chut, kho doc voi nguoi moi
       double chuVi = 2 * acos(-1.0) * r;
    */

    cout << "Chu vi = " << chuVi << endl;
    return 0;
}
```

**Lưu ý:** giữ lại phương án cũ dưới dạng chú thích chỉ nên làm **tạm thời** khi đang thử nghiệm. Trong dự án thật, code cũ nên được xoá và lưu lại bằng Git, vì "code chết" nằm trong chú thích lâu ngày sẽ lỗi thời và gây nhiễu.

### Bài 7.

**Chú thích KHÔNG được đưa vào file thực thi.** Chúng bị **tiền xử lý (preprocessor)** loại bỏ trước cả bước biên dịch.

Thí nghiệm chứng minh:

```cpp
// file a.cpp
#include <iostream>
using namespace std;
int main() { cout << "Hello"; return 0; }
```

```cpp
// file b.cpp  -- giong het a.cpp nhung them 100 dong chu thich
#include <iostream>
using namespace std;
// chu thich 1
// chu thich 2
// ... (den 100)
int main() { cout << "Hello"; return 0; }
```

```bash
g++ a.cpp -o a
g++ b.cpp -o b
ls -l a b
# -rwxr-xr-x 1 user user 17024 ... a
# -rwxr-xr-x 1 user user 17024 ... b     <- KICH THUOC Y HET NHAU
```

Xem trực tiếp kết quả sau bước tiền xử lý (chú thích đã biến mất):

```bash
g++ -E b.cpp | tail -5
```

**Kết luận:** viết chú thích **không làm chương trình chạy chậm hơn hay nặng hơn một byte nào**. Đừng bao giờ tiếc chú thích vì sợ "nặng file".

### Bài 8.

```cpp
#include <iostream>
using namespace std;

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

    cout << (t == n);     // in 1 neu la so Armstrong, 0 neu khong
    return 0;
}
```

**Hai kỹ thuật cần nhớ:**
- `x % 10` → lấy chữ số cuối cùng
- `x /= 10` → xoá chữ số cuối cùng

Kết hợp trong vòng `while (x > 0)` là cách duyệt qua từng chữ số của một số nguyên.

### Bài 9.

**① Chú thích giải thích *CÁI GÌ* (what)** — mô tả code đang làm gì. Thường **thừa** nếu code đã rõ ràng.

```cpp
i++;                          // tang i len 1     <- THUA, code da noi ro
int soHocSinh = 45;           // gan 45 cho bien  <- THUA
```

Dùng hợp lý khi đoạn code thực sự khó đọc:

```cpp
// Sap xep mang giam dan theo diem, neu bang diem thi theo ten tang dan
sort(ds.begin(), ds.end(), cmp);
```

**② Chú thích giải thích *TẠI SAO* (why)** — loại **giá trị nhất**, vì code không bao giờ tự nói được lý do.

```cpp
// Dung long long vi tong co the vuot 2 ty khi n > 65000
long long tong = 0;

// Cong 1e-9 de tranh loi lam tron khi so thuc sat nguong .5
int lamTron = (int)(x + 0.5 + 1e-9);

// Khong dung binary search o day vi mang chua chac da sap xep
```

**③ Ghi chú *VIỆC CẦN LÀM* (TODO / FIXME / HACK)**

```cpp
// TODO: them kiem tra n <= 0 truoc khi tinh
// FIXME: bi sai khi nhap so am, tam thoi chua xu ly
// HACK: hard-code 100 phan tu, se doi sang vector sau
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

```cpp
// Thay vi:
int d;    // so ngay con lai den han

// Hay viet:
int soNgayConLai;
```

Và nhớ: **chú thích sai còn tệ hơn không có chú thích**, vì nó đánh lừa người đọc. Khi sửa code, phải sửa cả chú thích.

### Bài 11.

```cpp
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
 *     cout << giaiThua(5);   // in ra 120
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

```cpp
#include <iostream>
using namespace std;

int main() {
    int a = 10, b = 3;
    int tong  = a + b;
    int hieu  = a - b;
    int tich  = a * b;
    int thuong = a / b;        // <- nghi ngo: chia nguyen, mat phan thap phan

    cout << "Tong   = " << tong   << endl;
    cout << "Hieu   = " << hieu   << endl;
    cout << "Tich   = " << tich   << endl;
    cout << "Thuong = " << thuong << endl;   // in ra 3 thay vi 3.333
    return 0;
}
```

Quy trình gỡ lỗi bằng chú thích ("chia đôi để tìm"):

```cpp
    cout << "Tong   = " << tong   << endl;
    // cout << "Hieu   = " << hieu   << endl;     <- tat thu
    // cout << "Tich   = " << tich   << endl;     <- tat thu
    cout << "Thuong = " << thuong << endl;        <- van sai -> loi nam o day
```

Khoanh vùng được rồi, in thêm biến trung gian để xác nhận:

```cpp
    cout << "DEBUG: a = " << a << ", b = " << b << endl;
    cout << "DEBUG: a / b = " << a / b << endl;         // 3  -> chia nguyen!
    cout << "DEBUG: (double)a / b = " << (double)a / b << endl;  // 3.33333
```

**Nguyên nhân:** `a` và `b` đều là `int` nên `a / b` là **phép chia nguyên**. Sửa:

```cpp
double thuong = (double)a / b;      // 3.33333
```

### Bài 15.

File mẫu `template.cpp`:

```cpp
/*
 * ============================================================
 *  Bai tap    : <so bai> - <ten bai tap>
 *  Chuong     : <so chuong> - <ten chuong>
 *  Tac gia    : <ten cua ban>
 *  Ngay        : dd/mm/yyyy
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
 *  Bien dich  : g++ -std=c++17 -Wall -Wextra -g main.cpp -o main
 * ============================================================
 */

#include <iostream>
using namespace std;

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
cp template.cpp bai01.cpp      # moi bai tap chi can copy ra
```

Trong VSCode, bạn còn có thể biến nó thành **User Snippet** (`File → Preferences → Configure User Snippets → cpp.json`) để gõ vài ký tự là sinh ra cả khung.

Phần **"Ý tưởng"** trong mẫu rất quan trọng: tập thói quen viết cách giải bằng tiếng Việt *trước khi* gõ code sẽ giúp bạn code nhanh và ít sai hơn nhiều.
