# Lời giải — [C++]. Switch Case

[← Quay lại bài học](../03-03-cpp-switch-case.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap thu (2-8): ";
    cin >> n;

    switch (n) {
        case 2: cout << "Thu Hai"  << endl; break;
        case 3: cout << "Thu Ba"   << endl; break;
        case 4: cout << "Thu Tu"   << endl; break;
        case 5: cout << "Thu Nam"  << endl; break;
        case 6: cout << "Thu Sau"  << endl; break;
        case 7: cout << "Thu Bay"  << endl; break;
        case 8: cout << "Chu Nhat" << endl; break;
        default: cout << "Khong hop le!" << endl;
    }
    return 0;
}
```

⚠️ **Không được quên `break`** — nếu thiếu, chương trình sẽ chạy tiếp xuống các `case` bên dưới (xem bài 7).

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int m;
    cout << "Nhap thang: ";
    cin >> m;

    switch (m) {
        case 1: case 3: case 5: case 7:
        case 8: case 10: case 12:
            cout << "31 ngay" << endl;
            break;
        case 4: case 6: case 9: case 11:
            cout << "30 ngay" << endl;
            break;
        case 2:
            cout << "28 ngay" << endl;
            break;
        default:
            cout << "Thang khong hop le!" << endl;
    }
    return 0;
}
```

**Kỹ thuật gộp case:** nhiều `case` liên tiếp không có lệnh giữa chúng sẽ **cùng dùng chung** một khối lệnh. Đây là ứng dụng hợp lệ và hữu ích nhất của "fall-through".

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int m, y;
    cout << "Nhap thang va nam: ";
    cin >> m >> y;

    switch (m) {
        case 1: case 3: case 5: case 7:
        case 8: case 10: case 12:
            cout << "31 ngay" << endl;
            break;
        case 4: case 6: case 9: case 11:
            cout << "30 ngay" << endl;
            break;
        case 2: {
            bool nhuan = (y % 400 == 0) || (y % 4 == 0 && y % 100 != 0);
            cout << (nhuan ? 29 : 28) << " ngay" << endl;
            break;
        }
        default:
            cout << "Thang khong hop le!" << endl;
    }
    return 0;
}
```

⚠️ **Chú ý cặp `{ }` quanh `case 2`:** khi cần **khai báo biến mới** bên trong một `case`, bắt buộc phải bọc nó trong khối `{ }`. Nếu không sẽ gặp lỗi:

```
error: jump to case label crosses initialization of 'bool nhuan'
```

Lý do: các `case` nằm chung một phạm vi, nên biến khai báo ở `case 2` vẫn "nhìn thấy được" ở `default` — nhưng có thể chưa được khởi tạo nếu nhảy thẳng tới đó.

### Bài 4.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double a, b;
    char pt;

    cout << "Nhap bieu thuc (vd: 5 + 3): ";
    cin >> a >> pt >> b;

    cout << fixed << setprecision(4);

    switch (pt) {
        case '+':
            cout << a << " + " << b << " = " << a + b << endl;
            break;
        case '-':
            cout << a << " - " << b << " = " << a - b << endl;
            break;
        case '*':
            cout << a << " * " << b << " = " << a * b << endl;
            break;
        case '/':
            if (b == 0) cout << "Loi: chia cho 0!" << endl;
            else        cout << a << " / " << b << " = " << a / b << endl;
            break;
        case '%':
            if ((int)b == 0) cout << "Loi: chia du cho 0!" << endl;
            else cout << (int)a << " % " << (int)b << " = " << (int)a % (int)b << endl;
            break;
        default:
            cout << "Phep toan '" << pt << "' khong hop le!" << endl;
    }
    return 0;
}
```

💡 `cin >> a >> pt >> b` đọc được cả `5+3` (không cần dấu cách) lẫn `5 + 3`, vì `>>` tự bỏ qua khoảng trắng.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot ky tu: ";
    cin >> c;

    switch (c) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
        case 'A': case 'E': case 'I': case 'O': case 'U':
            cout << "'" << c << "' la NGUYEN AM" << endl;
            break;
        default:
            cout << "'" << c << "' KHONG phai nguyen am" << endl;
    }
    return 0;
}
```

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    int thang;
    cout << "Nhap thang (1-12): ";
    cin >> thang;

    switch (thang) {
        case 1: case 2: case 3:
            cout << "Mua XUAN" << endl;  break;
        case 4: case 5: case 6:
            cout << "Mua HA" << endl;    break;
        case 7: case 8: case 9:
            cout << "Mua THU" << endl;   break;
        case 10: case 11: case 12:
            cout << "Mua DONG" << endl;  break;
        default:
            cout << "Thang khong hop le!" << endl;
    }
    return 0;
}
```

💡 Cách không cần `switch`: `switch ((thang - 1) / 3)` rồi xét 4 case 0,1,2,3.

### Bài 7.

**Với `n = 2`, output là:**

```
Hai Ba Khac
```

**Giải thích — hiện tượng "fall-through" (rơi xuyên qua):**

`switch` **không** chọn đúng một nhánh như `if else`. Nó hoạt động như sau:

1. Tìm nhãn `case` khớp với giá trị → đây chỉ là **điểm nhảy vào**
2. Từ điểm đó, **chạy liên tục mọi câu lệnh phía dưới** cho tới khi gặp `break` hoặc hết `switch`

Với `n = 2`:
```
case 1: bo qua (khong khop)
case 2: <- NHAY VAO DAY, in "Hai "
case 3: khong co break o tren -> chay tiep, in "Ba "
default: van chay tiep, in "Khac"
```

Đây là nguồn lỗi phổ biến nhất khi dùng `switch`. Biên dịch với `-Wimplicit-fallthrough` để được cảnh báo.

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    switch (n) {
        case 1: cout << "Mot";  break;
        case 2: cout << "Hai";  break;
        case 3: cout << "Ba";   break;
        default: cout << "Khac";
    }
    cout << endl;
    return 0;
}
```

Với `n = 2` → in `Hai`.

**Ghi chú:** `default` là nhánh cuối nên không bắt buộc có `break`. Tuy vậy nhiều người vẫn thêm vào, phòng khi sau này chèn thêm `case` xuống dưới.

Nếu bạn **cố ý** muốn fall-through, hãy ghi chú rõ để người đọc (và compiler) biết:

```cpp
case 1:
    lamViecA();
    [[fallthrough]];        // C++17: bao cho compiler biet la co y
case 2:
    lamViecB();
    break;
```

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    int chon;

    cout << "========= MENU =========" << endl;
    cout << "1. Them du lieu"          << endl;
    cout << "2. Xoa du lieu"           << endl;
    cout << "3. Sua du lieu"           << endl;
    cout << "4. Thoat"                 << endl;
    cout << "========================" << endl;
    cout << "Lua chon cua ban: ";
    cin >> chon;

    switch (chon) {
        case 1: cout << ">> Da chon: THEM du lieu" << endl; break;
        case 2: cout << ">> Da chon: XOA du lieu"  << endl; break;
        case 3: cout << ">> Da chon: SUA du lieu"  << endl; break;
        case 4: cout << ">> Tam biet!"             << endl; break;
        default: cout << ">> Lua chon khong hop le, vui long chon 1-4!" << endl;
    }
    return 0;
}
```

Đây là **ứng dụng điển hình nhất** của `switch` — xử lý menu. Trong chương trình thật, phần này được đặt trong vòng lặp `do while` để lặp lại menu cho tới khi người dùng chọn Thoát (xem bài [04-03](../04-03-cpp-vong-lap-do-while.md)).

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int diem;
    cout << "Nhap diem (0-10): ";
    cin >> diem;

    switch (diem) {
        case 9: case 10:
            cout << "GIOI" << endl;
            break;
        case 7: case 8:
            cout << "KHA" << endl;
            break;
        case 5: case 6:
            cout << "TRUNG BINH" << endl;
            break;
        case 0: case 1: case 2: case 3: case 4:
            cout << "YEU" << endl;
            break;
        default:
            cout << "Diem khong hop le!" << endl;
    }
    return 0;
}
```

💡 **Mẹo dùng `switch` cho khoảng giá trị:** chia cho một số để thu về ít case hơn.

```cpp
switch (diem / 2) {         // 0-1 -> 0, 2-3 -> 1, ...
    ...
}
```

Nhưng nói chung, **với khoảng giá trị thì `if else if` phù hợp hơn `switch`** — đặc biệt khi điểm là số thực.

### Bài 11.

```cpp
double d = 2.5;
switch (d) {                // LOI BIEN DICH
    case 2.5: cout << "Hai ruoi"; break;
}
```

Thông báo lỗi:

```
error: switch quantity not an integer
error: could not convert '2.5e+0' from 'double' to 'int'
```

**Vì sao `switch` không hỗ trợ số thực:**

1. **Cách hoạt động:** compiler thường chuyển `switch` thành một **bảng nhảy (jump table)** — một mảng địa chỉ được đánh chỉ số bằng chính giá trị. Việc này chỉ làm được với giá trị **rời rạc, đếm được**. Số thực là liên tục, không thể đánh chỉ số.

2. **Sai số biểu diễn:** `0.1 + 0.2 != 0.3` (xem bài [02-02](../02-02-cpp-kieu-du-lieu.md) bài 8). Nếu `switch` cho phép số thực, `case 0.3:` sẽ không bao giờ khớp khi giá trị được tính ra là `0.30000000000000004` — một nguồn lỗi âm thầm.

**Các kiểu `switch` chấp nhận:**

| ✅ Được | ❌ Không được |
|---|---|
| `int`, `short`, `long`, `long long` | `float`, `double`, `long double` |
| `char` (vì là số nguyên) | `string` |
| `bool` | Mảng, `vector`, `pair` |
| `enum` | Kiểu tự định nghĩa (trừ khi có toán tử chuyển sang số nguyên) |

**Với số thực hoặc chuỗi, dùng `if else if`:**

```cpp
if      (fabs(d - 2.5) < 1e-9) { ... }
else if (fabs(d - 3.0) < 1e-9) { ... }
```

### Bài 12.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    char donVi;
    double nhietDo;

    cout << "Nhap don vi (c = Celsius, f = Fahrenheit): ";
    cin >> donVi;
    cout << "Nhap nhiet do: ";
    cin >> nhietDo;

    cout << fixed << setprecision(2);

    switch (donVi) {
        case 'c': case 'C':
            cout << nhietDo << " do C = "
                 << nhietDo * 9.0 / 5.0 + 32 << " do F" << endl;
            break;
        case 'f': case 'F':
            cout << nhietDo << " do F = "
                 << (nhietDo - 32) * 5.0 / 9.0 << " do C" << endl;
            break;
        default:
            cout << "Don vi khong hop le!" << endl;
    }
    return 0;
}
```

Ví dụ: `c 100` → `100.00 do C = 212.00 do F`

⚠️ Phải viết `9.0 / 5.0` chứ không phải `9 / 5` — nếu không sẽ bị chia nguyên cho kết quả **1**, và mọi nhiệt độ đều sai.

### Bài 13.

| Tiêu chí | `switch case` | `if else if` |
|---|---|---|
| **Kiểu dữ liệu** | Chỉ số nguyên, `char`, `enum` | Mọi kiểu, mọi biểu thức |
| **Điều kiện** | Chỉ so sánh **bằng** với hằng số | So sánh tuỳ ý: `>`, `<`, `&&`, `\|\|`, gọi hàm… |
| **Nhãn `case`** | Bắt buộc là **hằng số biên dịch** | Có thể là biến, biểu thức |
| **Tốc độ** | Nhanh hơn khi nhiều nhánh (jump table, O(1)) | Kiểm tra tuần tự, O(n) nhánh |
| **Dễ đọc** | Rất rõ khi có nhiều giá trị rời rạc | Rõ khi là khoảng giá trị |
| **Rủi ro** | Quên `break` → fall-through | Sai thứ tự điều kiện |
| **Gộp nhiều giá trị** | Dễ: `case 1: case 2:` | Phải viết `n == 1 \|\| n == 2` |

**Khi nào dùng `switch`:**
- Menu chọn chức năng
- Xử lý mã trạng thái, mã lỗi, `enum`
- Phân loại theo ký tự (phép toán, phím bấm)
- Khi có ≥ 4 giá trị rời rạc cần so sánh bằng

**Khi nào dùng `if else if`:**
- Điều kiện là **khoảng giá trị** (`diem >= 8.5`)
- Điều kiện phức tạp có `&&`, `||`
- Làm việc với số thực hoặc `string`
- Chỉ có 2–3 nhánh

### Bài 14.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap mot chu cai: ";
    cin >> c;

    if (!isalpha(c)) {
        cout << "'" << c << "' khong phai chu cai!" << endl;
        return 1;
    }

    // Doi ve chu thuong -> chi can 5 case thay vi 10
    switch (tolower(c)) {
        case 'a': case 'e': case 'i': case 'o': case 'u':
            cout << "'" << c << "' la NGUYEN AM" << endl;
            break;
        default:
            cout << "'" << c << "' la PHU AM" << endl;
    }
    return 0;
}
```

**Kỹ thuật:** **chuẩn hoá dữ liệu trước khi phân nhánh**. `tolower(c)` đưa mọi chữ cái về chữ thường, nên chỉ cần viết 5 `case` thay vì 10.

Đây là nguyên tắc chung rất hữu ích: thay vì xử lý mọi biến thể của dữ liệu, hãy đưa chúng về một dạng chuẩn rồi mới xử lý.

`tolower` nằm trong `<cctype>`.

### Bài 15.

```cpp
#include <iostream>
#include <cctype>
using namespace std;

int main() {
    char c;
    cout << "Nhap ky tu La Ma (I V X L C D M): ";
    cin >> c;

    int giaTri;
    switch (toupper(c)) {
        case 'I': giaTri = 1;    break;
        case 'V': giaTri = 5;    break;
        case 'X': giaTri = 10;   break;
        case 'L': giaTri = 50;   break;
        case 'C': giaTri = 100;  break;
        case 'D': giaTri = 500;  break;
        case 'M': giaTri = 1000; break;
        default:
            cout << "'" << c << "' khong phai ky tu La Ma!" << endl;
            return 1;
    }

    cout << toupper(c) << " = " << giaTri << endl;
    return 0;
}
```

**Mẹo nhớ bảng số La Mã:** **I** V **X** L **C** D **M** — "**I** **V**alue **X**ylophones **L**ike **C**ows **D**o **M**ilk".

| Ký tự | Giá trị |
|---|---|
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

**Mở rộng — đổi cả chuỗi La Mã sang số** (dùng vòng lặp, chương 4):

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int giaTriLaMa(char c) {
    switch (toupper(c)) {
        case 'I': return 1;    case 'V': return 5;
        case 'X': return 10;   case 'L': return 50;
        case 'C': return 100;  case 'D': return 500;
        case 'M': return 1000;
        default:  return 0;
    }
}

int main() {
    string s;
    cout << "Nhap so La Ma: ";
    cin >> s;

    int kq = 0;
    for (size_t i = 0; i < s.length(); i++) {
        int hienTai = giaTriLaMa(s[i]);
        // Neu ky tu hien tai NHO HON ky tu ke tiep -> phep TRU (IV = 4, IX = 9)
        if (i + 1 < s.length() && hienTai < giaTriLaMa(s[i+1])) {
            kq -= hienTai;
        } else {
            kq += hienTai;
        }
    }

    cout << s << " = " << kq << endl;
    return 0;
}
```

Ví dụ: `MCMXCIV` = 1994, `XIV` = 14, `IX` = 9.
