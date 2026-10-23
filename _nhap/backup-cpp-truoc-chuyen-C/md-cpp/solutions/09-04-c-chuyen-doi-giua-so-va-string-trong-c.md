# Lời giải — [C++]. Chuyển Đổi Giữa Số Và String Trong C++

[← Quay lại bài học](../09-04-c-chuyen-doi-giua-so-va-string-trong-c.md)

> **Từ C++11:** `to_string()` cho số → chuỗi, và họ hàm `sto*` cho chuỗi → số. Cần `#include <string>`.

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int       a = 42;
    long long b = 9123456789012345LL;
    float     c = 3.14f;
    double    d = 2.718281828459045;
    char      e = 'A';

    string sa = to_string(a);
    string sb = to_string(b);
    string sc = to_string(c);
    string sd = to_string(d);
    string se = string(1, e);            // char -> string

    cout << "int       -> \"" << sa << "\" (do dai " << sa.length() << ")" << endl;
    cout << "long long -> \"" << sb << "\"" << endl;
    cout << "float     -> \"" << sc << "\"" << endl;
    cout << "double    -> \"" << sd << "\"" << endl;
    cout << "char      -> \"" << se << "\"" << endl;

    // Ung dung: noi so vao chuoi
    cout << "\nKet qua: " << "Diem la " + to_string(9) + "/10" << endl;
    return 0;
}
```

Output:

```
int       -> "42" (do dai 2)
long long -> "9123456789012345"
float     -> "3.140000"
double    -> "2.718282"
char      -> "A"
```

⚠️ **`to_string` với số thực luôn cho 6 chữ số thập phân** và không kiểm soát được. Muốn định dạng khác phải dùng `ostringstream` (xem bài 9).

⚠️ `to_string('A')` cho `"65"` chứ không phải `"A"` — vì `char` được coi là số. Dùng `string(1, 'A')` để đổi một ký tự thành chuỗi.

### Bài 2.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s1 = "42";
    string s2 = "9123456789012345";
    string s3 = "3.14";
    string s4 = "2.718281828459045";

    int       a = stoi(s1);
    long long b = stoll(s2);
    float     c = stof(s3);
    double    d = stod(s4);

    cout << "stoi  : " << a << endl;
    cout << "stoll : " << b << endl;
    cout << "stof  : " << c << endl;
    cout << "stod  : " << d << endl;

    // stoi voi phan thua
    cout << "\nstoi(\"123abc\") = " << stoi("123abc") << endl;    // 123
    cout << "stoi(\"  45\")   = " << stoi("  45")   << endl;      // 45 (bo qua khoang trang dau)
    cout << "stoi(\"-7\")     = " << stoi("-7")     << endl;      // -7
    cout << "stod(\"1e3\")    = " << stod("1e3")    << endl;      // 1000
    return 0;
}
```

**Bảng các hàm chuyển đổi:**

| Hàm | Kiểu trả về |
|---|---|
| `stoi(s)` | `int` |
| `stol(s)` | `long` |
| `stoll(s)` | `long long` |
| `stoul(s)` | `unsigned long` |
| `stoull(s)` | `unsigned long long` |
| `stof(s)` | `float` |
| `stod(s)` | `double` |
| `stold(s)` | `long double` |

💡 Các hàm này **bỏ qua khoảng trắng ở đầu** và **dừng ở ký tự không hợp lệ đầu tiên**.

### Bài 3.

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

int chuyenSo(const string& s) {
    try {
        size_t viTri;
        int n = stoi(s, &viTri);

        if (viTri != s.length()) {
            cout << "  Canh bao: co ky tu thua sau so (\"" << s.substr(viTri) << "\")" << endl;
        }
        return n;

    } catch (const invalid_argument& e) {
        cout << "  Loi: \"" << s << "\" khong phai so hop le" << endl;
        return 0;
    } catch (const out_of_range& e) {
        cout << "  Loi: \"" << s << "\" vuot qua pham vi kieu int" << endl;
        return 0;
    }
}

int main() {
    string ds[] = {"42", "abc", "123abc", "99999999999999", "", "  7  ", "-15"};

    for (const string& s : ds) {
        cout << "stoi(\"" << s << "\"):" << endl;
        int kq = chuyenSo(s);
        cout << "  -> " << kq << endl << endl;
    }
    return 0;
}
```

**Hai loại ngoại lệ:**

| Ngoại lệ | Khi nào ném |
|---|---|
| `std::invalid_argument` | Chuỗi **không bắt đầu** bằng số hợp lệ (`"abc"`, `""`) |
| `std::out_of_range` | Số **vượt phạm vi** kiểu dữ liệu |

💡 **Tham số thứ hai `&viTri`** cho biết `stoi` đã đọc tới đâu — dùng để phát hiện ký tự thừa:

```cpp
size_t vt;
int n = stoi("123abc", &vt);
// n = 123, vt = 3  ->  con "abc" chua doc
```

⚠️ **`stoi` KHÔNG báo lỗi với `"123abc"`** — nó lặng lẽ nhận 123. Phải tự kiểm tra bằng `viTri`.

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string soThanhChuoi(long long n) {
    if (n == 0) return "0";

    bool am = (n < 0);
    unsigned long long tam = am ? -(unsigned long long)n : n;

    string kq = "";
    while (tam > 0) {
        kq += (char)('0' + tam % 10);     // lay chu so cuoi, doi thanh ky tu
        tam /= 10;
    }

    if (am) kq += '-';
    reverse(kq.begin(), kq.end());        // dao lai vi ta lay tu chu so thap
    return kq;
}

int main() {
    long long ds[] = {0, 7, 42, -123, 9123456789012345LL, -1};

    for (long long n : ds) {
        cout << n << " -> \"" << soThanhChuoi(n) << "\"" << endl;
    }

    // Kiem chung voi to_string
    cout << "\nKiem chung: " << (soThanhChuoi(-12345) == to_string(-12345) ? "DUNG" : "SAI") << endl;
    return 0;
}
```

**3 điểm cần chú ý:**
1. **Trường hợp `n = 0`** — vòng `while` không chạy, phải xử lý riêng
2. **Số âm** — tách dấu ra, xử lý phần trị tuyệt đối
3. **`reverse`** — vì ta lấy chữ số từ hàng đơn vị lên

⚠️ **Dùng `unsigned long long` cho `tam`:** giá trị `LLONG_MIN` (−9223372036854775808) không có số dương tương ứng trong `long long`, nên `-n` sẽ tràn.

### Bài 5.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

long long chuoiThanhSo(const string& s) {
    size_t i = 0;

    // Bo qua khoang trang dau
    while (i < s.length() && isspace((unsigned char)s[i])) i++;

    // Xu ly dau
    bool am = false;
    if (i < s.length() && (s[i] == '+' || s[i] == '-')) {
        am = (s[i] == '-');
        i++;
    }

    // Doc cac chu so
    long long kq = 0;
    while (i < s.length() && isdigit((unsigned char)s[i])) {
        kq = kq * 10 + (s[i] - '0');      // CONG THUC VANG
        i++;
    }

    return am ? -kq : kq;
}

int main() {
    string ds[] = {"42", "-123", "  +7  ", "0", "123abc", "abc"};

    for (const string& s : ds) {
        cout << "\"" << s << "\" -> " << chuoiThanhSo(s) << endl;
    }

    cout << "\nKiem chung: "
         << (chuoiThanhSo("-12345") == -12345 ? "DUNG" : "SAI") << endl;
    return 0;
}
```

**Công thức cốt lõi:** `kq = kq * 10 + (s[i] - '0')`

Quá trình với `"423"`:

```
kq = 0
'4': kq = 0*10 + 4 = 4
'2': kq = 4*10 + 2 = 42
'3': kq = 42*10 + 3 = 423  ✔
```

💡 `s[i] - '0'` đổi ký tự số thành giá trị số — nhờ các chữ số nằm liên tiếp trong bảng ASCII (xem bài [03-04](../03-04-cpp-bang-ma-ascii-va-thu-vien-ctype.md)).

### Bài 6.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // stoi(chuoi, &viTri, coSo)
    cout << "Nhi phan  \"1101\"   -> " << stoi("1101", nullptr, 2)  << endl;   // 13
    cout << "Bat phan  \"777\"    -> " << stoi("777",  nullptr, 8)  << endl;   // 511
    cout << "Thap luc  \"FF\"     -> " << stoi("FF",   nullptr, 16) << endl;   // 255
    cout << "Thap luc  \"1A2B\"   -> " << stoi("1A2B", nullptr, 16) << endl;   // 6699

    // Co so 0 = tu dong nhan dien theo tien to
    cout << "\n--- Tu dong nhan dien (co so 0) ---" << endl;
    cout << "\"0x1F\" -> " << stoi("0x1F", nullptr, 0) << endl;   // 31  (0x = he 16)
    cout << "\"017\"  -> " << stoi("017",  nullptr, 0) << endl;   // 15  (0  = he 8)
    cout << "\"42\"   -> " << stoi("42",   nullptr, 0) << endl;   // 42  (he 10)

    // Co so bat ky tu 2 den 36
    cout << "\nCo so 36 \"ZZ\"    -> " << stoi("ZZ", nullptr, 36) << endl;   // 1295
    return 0;
}
```

**Cơ số hỗ trợ: 2 đến 36** (dùng 0–9 rồi A–Z làm chữ số).

**Tiền tố khi dùng cơ số 0:**

| Tiền tố | Cơ số |
|---|---|
| `0x` hoặc `0X` | 16 |
| `0` (rồi chữ số) | 8 |
| Không có | 10 |

### Bài 7.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <bitset>
#include <algorithm>
using namespace std;

// Tu viet - ho tro co so bat ky
string doiCoSo(long long n, int coSo) {
    if (coSo < 2 || coSo > 36) return "";
    if (n == 0) return "0";

    const string KY_TU = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    bool am = (n < 0);
    unsigned long long tam = am ? -(unsigned long long)n : n;

    string kq = "";
    while (tam > 0) {
        kq += KY_TU[tam % coSo];
        tam /= coSo;
    }
    if (am) kq += '-';
    reverse(kq.begin(), kq.end());
    return kq;
}

int main() {
    int n = 255;

    cout << "So " << n << " trong cac he:" << endl;
    cout << "  He 2  : " << doiCoSo(n, 2)  << endl;      // 11111111
    cout << "  He 8  : " << doiCoSo(n, 8)  << endl;      // 377
    cout << "  He 16 : " << doiCoSo(n, 16) << endl;      // FF
    cout << "  He 36 : " << doiCoSo(n, 36) << endl;      // 73

    // Dung cong cu co san cua C++
    cout << "\n--- Dung cong cu C++ ---" << endl;
    cout << "  He 2  (bitset): " << bitset<8>(n) << endl;
    cout << "  He 8  (oct)   : " << oct << n << endl;
    cout << "  He 16 (hex)   : " << hex << uppercase << n << dec << endl;

    // Dung stringstream
    ostringstream oss;
    oss << hex << uppercase << n;
    cout << "  He 16 (sstream): " << oss.str() << endl;
    return 0;
}
```

**Các manipulator hệ đếm của `cout`:**

```cpp
cout << dec << n;          // he 10 (mac dinh)
cout << oct << n;          // he 8
cout << hex << n;          // he 16 (chu thuong)
cout << hex << uppercase << n;   // he 16 (chu HOA)
cout << showbase << hex << n;    // co tien to 0x
```

⚠️ Các manipulator này **có hiệu lực kéo dài** — nhớ `cout << dec` để quay lại hệ 10.

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    // ===== SO -> CHUOI =====
    int n = 42;
    double d = 3.14159;

    // Cach 1: to_string
    string s1 = to_string(n);

    // Cach 2: ostringstream - LINH HOAT HON
    ostringstream oss;
    oss << n;
    string s2 = oss.str();

    // Voi dinh dang
    ostringstream oss2;
    oss2 << fixed << setprecision(2) << d;
    string s3 = oss2.str();

    cout << "to_string     : " << s1 << endl;
    cout << "ostringstream : " << s2 << endl;
    cout << "Co dinh dang  : " << s3 << endl;      // 3.14

    // ===== CHUOI -> SO =====
    string s = "123";

    int a = stoi(s);                        // Cach 1

    istringstream iss(s);                   // Cach 2
    int b;
    iss >> b;

    cout << "\nstoi          : " << a << endl;
    cout << "istringstream : " << b << endl;

    // stringstream doc NHIEU gia tri cung luc
    string duLieu = "10 3.5 hello";
    istringstream iss2(duLieu);
    int x; double y; string z;
    iss2 >> x >> y >> z;
    cout << "\nDoc nhieu: x=" << x << ", y=" << y << ", z=" << z << endl;
    return 0;
}
```

**So sánh:**

| | `to_string`/`stoi` | `stringstream` |
|---|---|---|
| Cú pháp | ✅ Ngắn gọn | Dài hơn |
| Tốc độ | ✅ Nhanh hơn | Chậm hơn (tạo đối tượng luồng) |
| Định dạng số thực | ❌ Cố định 6 chữ số | ✅ Tuỳ ý (`setprecision`) |
| Đọc nhiều giá trị | ❌ Không | ✅ Được |
| Kiểu tự định nghĩa | ❌ Không | ✅ Được (nếu có `operator<<`) |
| Xử lý lỗi | Ném ngoại lệ | Kiểm tra cờ `fail()` |

✅ **Dùng `to_string`/`stoi`** cho việc chuyển đổi đơn giản; **dùng `stringstream`** khi cần định dạng hoặc đọc nhiều giá trị. Xem thêm bài [09-07](../09-07-c-stringstream-trong-c-va-ung-dung.md).

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
using namespace std;

string dinhDangSoThuc(double x, int soChuSo) {
    ostringstream oss;
    oss << fixed << setprecision(soChuSo) << x;
    return oss.str();
}

int main() {
    double pi = 3.14159265358979;

    for (int k = 0; k <= 8; k += 2) {
        cout << "k = " << k << " -> \"" << dinhDangSoThuc(pi, k) << "\"" << endl;
    }

    // So sanh voi to_string
    cout << "\nto_string(pi) = \"" << to_string(pi) << "\"" << endl;

    // Dinh dang khoa hoc
    ostringstream oss;
    oss << scientific << setprecision(3) << 123456.789;
    cout << "Khoa hoc      = \"" << oss.str() << "\"" << endl;
    return 0;
}
```

Output:

```
k = 0 -> "3"
k = 2 -> "3.14"
k = 4 -> "3.1416"
k = 6 -> "3.141593"
k = 8 -> "3.14159265"

to_string(pi) = "3.141593"
Khoa hoc      = "1.235e+05"
```

💡 **Từ C++20 có `std::format`** gọn hơn nhiều:

```cpp
#include <format>
string s = format("{:.2f}", pi);       // "3.14"
```

### Bài 10.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string dinhDangTien(long long n, char phanCach = '.') {
    bool am = (n < 0);
    string s = to_string(am ? -n : n);

    string kq = "";
    int dem = 0;

    // Duyet TU PHAI SANG TRAI, cu 3 chu so chen mot dau phan cach
    for (int i = s.length() - 1; i >= 0; i--) {
        kq += s[i];
        dem++;
        if (dem % 3 == 0 && i > 0) kq += phanCach;
    }

    if (am) kq += '-';
    reverse(kq.begin(), kq.end());
    return kq;
}

int main() {
    long long ds[] = {0, 7, 999, 1000, 1234567, 1000000000, -9876543};

    for (long long n : ds) {
        cout << n << "\t-> " << dinhDangTien(n) << " VND" << endl;
    }

    cout << "\nKieu My (dau phay): " << dinhDangTien(1234567, ',') << endl;
    return 0;
}
```

Output:

```
0	-> 0 VND
7	-> 7 VND
999	-> 999 VND
1000	-> 1.000 VND
1234567	-> 1.234.567 VND
1000000000	-> 1.000.000.000 VND
-9876543	-> -9.876.543 VND
```

💡 **Duyệt từ phải sang trái** vì việc nhóm 3 chữ số bắt đầu từ hàng đơn vị. Cuối cùng `reverse` lại.

⚠️ `if (dem % 3 == 0 && i > 0)` — điều kiện `i > 0` tránh thêm dấu phân cách thừa ở đầu (`".123"`).

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

vector<int> docCacSo(const string& dong) {
    vector<int> kq;
    istringstream iss(dong);
    int x;
    while (iss >> x) kq.push_back(x);
    return kq;
}

int main() {
    string dong;
    cout << "Nhap cac so cach nhau boi dau cach: ";
    getline(cin, dong);

    vector<int> ds = docCacSo(dong);

    cout << "Da doc " << ds.size() << " so: ";
    for (int x : ds) cout << x << " ";
    cout << endl;

    if (!ds.empty()) {
        long long tong = 0;
        int mx = ds[0], mn = ds[0];
        for (int x : ds) { tong += x; if (x > mx) mx = x; if (x < mn) mn = x; }

        cout << "Tong      = " << tong << endl;
        cout << "Lon nhat  = " << mx << endl;
        cout << "Nho nhat  = " << mn << endl;
        cout << "Trung binh= " << (double)tong / ds.size() << endl;
    }
    return 0;
}
```

💡 `while (iss >> x)` tự động dừng khi hết dữ liệu hoặc gặp ký tự không phải số — rất gọn.

Muốn tách theo dấu phẩy:

```cpp
istringstream iss(dong);
string phan;
while (getline(iss, phan, ',')) kq.push_back(stoi(phan));
```

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool laSoNguyen(const string& s) {
    if (s.empty()) return false;

    size_t i = 0;
    if (s[0] == '+' || s[0] == '-') i = 1;
    if (i >= s.length()) return false;          // chi co dau, khong co chu so

    for (; i < s.length(); i++)
        if (!isdigit((unsigned char)s[i])) return false;

    return true;
}

bool laSoThuc(const string& s) {
    if (s.empty()) return false;

    size_t i = 0;
    if (s[0] == '+' || s[0] == '-') i = 1;

    bool coChuSo = false, coChamThapPhan = false;

    for (; i < s.length(); i++) {
        if (isdigit((unsigned char)s[i])) {
            coChuSo = true;
        } else if (s[i] == '.') {
            if (coChamThapPhan) return false;   // co 2 dau cham -> sai
            coChamThapPhan = true;
        } else {
            return false;
        }
    }
    return coChuSo;                              // phai co it nhat 1 chu so
}

int main() {
    string ds[] = {"123", "-45", "+7", "3.14", "-0.5", ".5", "1.", "12a", "", "-", "1.2.3", "  5"};

    cout << left;
    cout << "Chuoi          | Nguyen | Thuc" << endl;
    cout << "---------------|--------|------" << endl;
    for (const string& s : ds) {
        cout << "\"" << s << "\"";
        for (size_t k = s.length(); k < 13; k++) cout << " ";
        cout << "| " << (laSoNguyen(s) ? "  CO  " : "  --  ")
             << " | " << (laSoThuc(s)  ? " CO"    : " --") << endl;
    }
    return 0;
}
```

💡 **Cách đơn giản hơn dùng `stod` + kiểm tra vị trí:**

```cpp
bool laSo(const string& s) {
    if (s.empty()) return false;
    try {
        size_t vt;
        stod(s, &vt);
        return vt == s.length();       // phai doc HET chuoi
    } catch (...) {
        return false;
    }
}
```

Cách này còn nhận được cả dạng khoa học (`"1e5"`).

### Bài 13.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string bieuThuc;
    cout << "Nhap bieu thuc (vd: 12+34): ";
    getline(cin, bieuThuc);

    // Tim vi tri toan tu (bo qua dau o dau)
    size_t vt = string::npos;
    for (size_t i = 1; i < bieuThuc.length(); i++) {
        char c = bieuThuc[i];
        if (c == '+' || c == '-' || c == '*' || c == '/' || c == '%') {
            vt = i;
            break;
        }
    }

    if (vt == string::npos) {
        cout << "Khong tim thay toan tu!" << endl;
        return 1;
    }

    try {
        double a = stod(bieuThuc.substr(0, vt));
        char   op = bieuThuc[vt];
        double b = stod(bieuThuc.substr(vt + 1));

        cout << a << " " << op << " " << b << " = ";
        switch (op) {
            case '+': cout << a + b; break;
            case '-': cout << a - b; break;
            case '*': cout << a * b; break;
            case '/':
                if (b == 0) cout << "Loi chia cho 0";
                else cout << a / b;
                break;
            case '%':
                if ((int)b == 0) cout << "Loi chia du cho 0";
                else cout << (int)a % (int)b;
                break;
        }
        cout << endl;

    } catch (const exception& e) {
        cout << "Loi: bieu thuc khong hop le!" << endl;
    }
    return 0;
}
```

Ví dụ:

```
Nhap bieu thuc (vd: 12+34): 12+34
12 + 34 = 46

Nhap bieu thuc: -5*3
-5 * 3 = -15
```

⚠️ Vòng lặp bắt đầu từ `i = 1` để **không nhầm dấu âm ở đầu** với toán tử trừ.

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const string CHU_SO[] = {"khong", "mot", "hai", "ba", "bon",
                          "nam", "sau", "bay", "tam", "chin"};

// Doc mot nhom 3 chu so (0-999)
string doc3ChuSo(int n, bool laNhomDau) {
    if (n == 0) return "";

    int tram = n / 100;
    int chuc = (n / 10) % 10;
    int donVi = n % 10;

    string kq = "";

    if (tram > 0) {
        kq += CHU_SO[tram] + " tram ";
    } else if (!laNhomDau && (chuc > 0 || donVi > 0)) {
        kq += "khong tram ";
    }

    if (chuc > 1) {
        kq += CHU_SO[chuc] + " muoi ";
        if (donVi == 1)      kq += "mot";
        else if (donVi == 5) kq += "lam";
        else if (donVi > 0)  kq += CHU_SO[donVi];
    } else if (chuc == 1) {
        kq += "muoi ";
        if (donVi == 5)      kq += "lam";
        else if (donVi > 0)  kq += CHU_SO[donVi];
    } else {
        if (donVi > 0) {
            if (tram > 0) kq += "le ";
            kq += CHU_SO[donVi];
        }
    }

    // Cat khoang trang thua
    while (!kq.empty() && kq.back() == ' ') kq.pop_back();
    return kq;
}

string docSo(long long n) {
    if (n == 0) return "khong";

    string kq = "";
    if (n < 0) { kq = "am "; n = -n; }

    const string DON_VI[] = {"", " nghin", " trieu", " ty", " nghin ty"};

    // Tach thanh cac nhom 3 chu so
    vector<int> nhom;
    while (n > 0) { nhom.push_back(n % 1000); n /= 1000; }

    for (int i = nhom.size() - 1; i >= 0; i--) {
        if (nhom[i] == 0) continue;
        string phan = doc3ChuSo(nhom[i], i == (int)nhom.size() - 1);
        kq += phan + DON_VI[i];
        if (i > 0) kq += " ";
    }

    // Cat khoang trang thua
    while (!kq.empty() && kq.back() == ' ') kq.pop_back();
    return kq;
}

int main() {
    long long ds[] = {0, 5, 10, 11, 15, 21, 25, 100, 101, 105, 123,
                      1000, 1234, 1000000, 123456789, -42};

    for (long long n : ds) {
        cout << n << "\t-> " << docSo(n) << endl;
    }
    return 0;
}
```

Output:

```
0	-> khong
5	-> nam
10	-> muoi
11	-> muoi mot
15	-> muoi lam
21	-> hai muoi mot
25	-> hai muoi lam
100	-> mot tram
101	-> mot tram le mot
105	-> mot tram le nam
123	-> mot tram hai muoi ba
1000	-> mot nghin
1234	-> mot nghin hai tram ba muoi bon
1000000	-> mot trieu
123456789	-> mot tram hai muoi ba trieu bon tram nam muoi sau nghin bay tram tam muoi chin
-42	-> am bon muoi hai
```

💡 **Các quy tắc đặc biệt của tiếng Việt** làm bài này khó hơn tưởng tượng:
- `15` → "mười **lăm**" (không phải "mười năm")
- `21` → "hai mươi **mốt**" (bản trên dùng "một" cho đơn giản)
- `101` → "một trăm **lẻ** một"
- `1234` → cần "không trăm" ở các nhóm giữa: `1.000.234` → "một triệu không trăm ba mươi tư nghìn..."

### Bài 15.

**File `chuyendoi.h`:**

```cpp
#pragma once
#include <string>
#include <vector>

/** @brief Chuyen chuoi sang int an toan. @param macDinh Gia tri tra ve neu that bai. */
int toInt(const std::string& s, int macDinh = 0);

/** @brief Chuyen chuoi sang long long an toan. */
long long toLongLong(const std::string& s, long long macDinh = 0);

/** @brief Chuyen chuoi sang double an toan. */
double toDouble(const std::string& s, double macDinh = 0.0);

/** @brief Chuyen so thuc thanh chuoi voi so chu so thap phan chi dinh. */
std::string toStr(double x, int soChuSo = 2);

/** @brief Chuyen so nguyen thanh chuoi. */
std::string toStr(long long n);

/** @brief Kiem tra chuoi co phai so nguyen hop le (cho phep dau +/-). */
bool isInteger(const std::string& s);

/** @brief Kiem tra chuoi co phai so (nguyen hoac thuc) hop le. */
bool isNumber(const std::string& s);

/** @brief Dinh dang so thanh tien te co dau phan cach hang nghin. */
std::string formatMoney(long long n, char phanCach = '.');

/** @brief Doi so nguyen sang chuoi theo co so (2-36). */
std::string toBase(long long n, int coSo);

/** @brief Doi chuoi theo co so ve so nguyen. Tra ve macDinh neu that bai. */
long long fromBase(const std::string& s, int coSo, long long macDinh = 0);

/** @brief Tach mot dong thanh cac so nguyen. */
std::vector<int> parseInts(const std::string& dong);
```

**File `chuyendoi.cpp`:**

```cpp
#include "chuyendoi.h"
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <cctype>
#include <stdexcept>
using namespace std;

int toInt(const string& s, int macDinh) {
    try { size_t vt; int n = stoi(s, &vt); return (vt == s.length()) ? n : macDinh; }
    catch (...) { return macDinh; }
}

long long toLongLong(const string& s, long long macDinh) {
    try { size_t vt; long long n = stoll(s, &vt); return (vt == s.length()) ? n : macDinh; }
    catch (...) { return macDinh; }
}

double toDouble(const string& s, double macDinh) {
    try { size_t vt; double x = stod(s, &vt); return (vt == s.length()) ? x : macDinh; }
    catch (...) { return macDinh; }
}

string toStr(double x, int soChuSo) {
    ostringstream oss;
    oss << fixed << setprecision(soChuSo) << x;
    return oss.str();
}

string toStr(long long n) { return to_string(n); }

bool isInteger(const string& s) {
    if (s.empty()) return false;
    size_t i = (s[0] == '+' || s[0] == '-') ? 1 : 0;
    if (i >= s.length()) return false;
    for (; i < s.length(); i++)
        if (!isdigit((unsigned char)s[i])) return false;
    return true;
}

bool isNumber(const string& s) {
    if (s.empty()) return false;
    try { size_t vt; stod(s, &vt); return vt == s.length(); }
    catch (...) { return false; }
}

string formatMoney(long long n, char phanCach) {
    bool am = (n < 0);
    string s = to_string(am ? -n : n);
    string kq;
    int dem = 0;
    for (int i = (int)s.length() - 1; i >= 0; i--) {
        kq += s[i];
        if (++dem % 3 == 0 && i > 0) kq += phanCach;
    }
    if (am) kq += '-';
    reverse(kq.begin(), kq.end());
    return kq;
}

string toBase(long long n, int coSo) {
    if (coSo < 2 || coSo > 36) return "";
    if (n == 0) return "0";

    static const string KY_TU = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    bool am = (n < 0);
    unsigned long long tam = am ? -(unsigned long long)n : n;

    string kq;
    while (tam > 0) { kq += KY_TU[tam % coSo]; tam /= coSo; }
    if (am) kq += '-';
    reverse(kq.begin(), kq.end());
    return kq;
}

long long fromBase(const string& s, int coSo, long long macDinh) {
    try { size_t vt; long long n = stoll(s, &vt, coSo); return (vt == s.length()) ? n : macDinh; }
    catch (...) { return macDinh; }
}

vector<int> parseInts(const string& dong) {
    vector<int> kq;
    istringstream iss(dong);
    int x;
    while (iss >> x) kq.push_back(x);
    return kq;
}
```

**File `main.cpp` — kiểm thử:**

```cpp
#include <iostream>
#include "chuyendoi.h"
using namespace std;

int main() {
    cout << "--- Chuyen doi an toan ---" << endl;
    cout << "toInt(\"42\")      = " << toInt("42")      << endl;   // 42
    cout << "toInt(\"abc\")     = " << toInt("abc", -1) << endl;   // -1
    cout << "toInt(\"12abc\")   = " << toInt("12abc", -1) << endl; // -1 (co rac)
    cout << "toDouble(\"3.14\") = " << toDouble("3.14") << endl;   // 3.14

    cout << "\n--- Kiem tra ---" << endl;
    cout << boolalpha;
    cout << "isInteger(\"-45\") = " << isInteger("-45")  << endl;  // true
    cout << "isInteger(\"3.14\")= " << isInteger("3.14") << endl;  // false
    cout << "isNumber(\"3.14\") = " << isNumber("3.14")  << endl;  // true
    cout << "isNumber(\"1e5\")  = " << isNumber("1e5")   << endl;  // true

    cout << "\n--- Dinh dang ---" << endl;
    cout << "toStr(3.14159, 3) = " << toStr(3.14159, 3)    << endl;  // 3.142
    cout << "formatMoney       = " << formatMoney(1234567) << " VND" << endl;

    cout << "\n--- He co so ---" << endl;
    cout << "toBase(255, 2)  = " << toBase(255, 2)  << endl;   // 11111111
    cout << "toBase(255, 16) = " << toBase(255, 16) << endl;   // FF
    cout << "fromBase(\"FF\", 16) = " << fromBase("FF", 16) << endl;  // 255

    cout << "\n--- Doc nhieu so ---" << endl;
    auto v = parseInts("10 20 30 40 50");
    cout << "parseInts: ";
    for (int x : v) cout << x << " ";
    cout << endl;
    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp chuyendoi.cpp -o chuyendoi
```

💡 **Điểm thiết kế quan trọng:** tất cả hàm chuyển đổi đều **không ném ngoại lệ** — chúng trả về giá trị mặc định khi thất bại. Điều này làm code gọi đơn giản hơn nhiều so với phải bọc `try/catch` khắp nơi.
