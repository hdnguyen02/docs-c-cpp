# Lời giải — [C++]. Stringstream Trong C++ Và Ứng Dụng

[← Quay lại bài học](../09-07-c-stringstream-trong-c-va-ung-dung.md)

> **`stringstream` biến một chuỗi thành luồng dữ liệu** — dùng `>>` và `<<` giống `cin`/`cout`, nhưng đọc/ghi vào chuỗi. Cần `#include <sstream>`.

---

### Bài 1.

```cpp
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string dong;
    cout << "Nhap cac so cach nhau boi dau cach: ";
    getline(cin, dong);

    istringstream iss(dong);
    vector<int> ds;
    int x;

    while (iss >> x) ds.push_back(x);

    cout << "Da doc " << ds.size() << " so: ";
    for (int v : ds) cout << v << " ";
    cout << endl;

    long long tong = 0;
    for (int v : ds) tong += v;
    cout << "Tong = " << tong << endl;
    return 0;
}
```

💡 `while (iss >> x)` tự dừng khi hết dữ liệu hoặc gặp ký tự không đọc được — cực kỳ gọn so với tự tách chuỗi bằng `find`/`substr`.

### Bài 2.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string cau;
    cout << "Nhap mot cau: ";
    getline(cin, cau);

    istringstream iss(cau);
    string tu;
    int dem = 0;

    while (iss >> tu) dem++;

    cout << "So tu: " << dem << endl;

    // In lai tung tu
    istringstream iss2(cau);
    int i = 1;
    while (iss2 >> tu) cout << "  " << i++ << ". " << tu << endl;
    return 0;
}
```

💡 `>>` **tự động bỏ qua mọi khoảng trắng** (dấu cách, tab, nhiều dấu cách liên tiếp, xuống dòng) — nên đếm từ chính xác mà không cần xử lý gì thêm.

⚠️ Một `istringstream` chỉ đọc được **một lần**. Muốn đọc lại phải tạo mới hoặc reset (xem bài 12).

### Bài 3.

```cpp
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;

vector<string> tachCSV(const string& dong, char delim = ',') {
    vector<string> kq;
    istringstream iss(dong);
    string phan;

    while (getline(iss, phan, delim)) {
        kq.push_back(phan);
    }
    return kq;
}

int main() {
    string ds[] = {
        "An,20,8.5,Ha Noi",
        "Binh,,7.0,",                  // co truong rong
        "Chi,22,9.0,TP HCM"
    };

    for (const string& dong : ds) {
        auto cot = tachCSV(dong);
        cout << "Dong: " << dong << endl;
        cout << "  -> " << cot.size() << " cot: ";
        for (const auto& c : cot) cout << "[" << c << "] ";
        cout << endl;
    }

    // Tach theo dau khac
    auto ngay = tachCSV("17/09/2026", '/');
    cout << "\nNgay: ";
    for (const auto& p : ngay) cout << p << " ";
    cout << endl;
    return 0;
}
```

Output:

```
Dong: An,20,8.5,Ha Noi
  -> 4 cot: [An] [20] [8.5] [Ha Noi] 
Dong: Binh,,7.0,
  -> 4 cot: [Binh] [] [7.0] [] 
```

💡 **Khác biệt quan trọng giữa `>>` và `getline(ss, s, delim)`:**

| | `iss >> tu` | `getline(iss, phan, ',')` |
|---|---|---|
| Phân cách | Mọi khoảng trắng | Đúng ký tự chỉ định |
| Trường rỗng | Bỏ qua | ✅ **Giữ lại** |
| Chuỗi có dấu cách | ❌ Bị cắt | ✅ Giữ nguyên (`"Ha Noi"`) |

Với CSV phải dùng `getline` — vì trường rỗng và trường có dấu cách đều quan trọng.

### Bài 4.

```cpp
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
using namespace std;

string dinhDang(double x, int soChuSo = 2) {
    ostringstream oss;
    oss << fixed << setprecision(soChuSo) << x;
    return oss.str();
}

int main() {
    double pi = 3.14159265358979;

    cout << "2 chu so : " << dinhDang(pi, 2) << endl;   // 3.14
    cout << "4 chu so : " << dinhDang(pi, 4) << endl;   // 3.1416
    cout << "0 chu so : " << dinhDang(pi, 0) << endl;   // 3

    // So sanh voi to_string
    cout << "to_string: " << to_string(pi) << endl;     // 3.141593 (luon 6 chu so)

    // Ghep vao chuoi khac
    string bao = "Diem trung binh la " + dinhDang(8.456, 2) + "/10";
    cout << "\n" << bao << endl;
    return 0;
}
```

💡 **Đây là ưu điểm lớn nhất của `ostringstream` so với `to_string`:** kiểm soát được **định dạng** số thực.

### Bài 5.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    // ===== SO -> CHUOI =====
    ostringstream oss;
    oss << 42 << " " << 3.14 << " " << 'A' << " " << true;
    string s = oss.str();
    cout << "Chuoi tao ra: \"" << s << "\"" << endl;

    // ===== CHUOI -> SO =====
    istringstream iss("100 2.5 X 0");
    int a; double b; char c; bool d;
    iss >> a >> b >> c >> d;

    cout << "\nDoc ra: a=" << a << ", b=" << b
         << ", c=" << c << ", d=" << d << endl;

    // stringstream 2 CHIEU
    stringstream ss;
    ss << 12345;                 // ghi vao
    int n;
    ss >> n;                     // doc ra
    cout << "\nGhi roi doc: " << n << endl;
    return 0;
}
```

Output:

```
Chuoi tao ra: "42 3.14 A 1"

Doc ra: a=100, b=2.5, c=X, d=0

Ghi roi doc: 12345
```

### Bài 6.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string dong = "An 20 8.5";

    istringstream iss(dong);
    string ten;
    int tuoi;
    double diem;

    if (iss >> ten >> tuoi >> diem) {
        cout << "Ten  : " << ten  << endl;
        cout << "Tuoi : " << tuoi << endl;
        cout << "Diem : " << diem << endl;
    } else {
        cout << "Dinh dang khong hop le!" << endl;
    }

    // Truong hop du lieu sai
    istringstream iss2("Binh abc 7.0");
    string t; int tu; double d;
    if (!(iss2 >> t >> tu >> d))
        cout << "\nDong 2: loi doc (tuoi khong phai so)" << endl;
    return 0;
}
```

💡 **`stringstream` tự động chuyển kiểu** theo biến bạn đọc vào — đây là điểm mạnh nhất của nó. Không cần gọi `stoi`, `stod` thủ công.

💡 Kiểm tra `if (iss >> a >> b >> c)` để phát hiện dữ liệu sai định dạng.

### Bài 7.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string ngayThang;
    cout << "Nhap ngay (dd/mm/yyyy): ";
    getline(cin, ngayThang);

    // Cach 1: getline voi dau phan cach
    istringstream iss(ngayThang);
    string phan;
    int ngay, thang, nam;

    getline(iss, phan, '/'); ngay  = stoi(phan);
    getline(iss, phan, '/'); thang = stoi(phan);
    getline(iss, phan);      nam   = stoi(phan);

    cout << "Ngay : " << ngay  << endl;
    cout << "Thang: " << thang << endl;
    cout << "Nam  : " << nam   << endl;

    // Cach 2: doc so va bo qua dau '/' bang bien char
    istringstream iss2(ngayThang);
    int d, m, y;
    char c1, c2;
    if (iss2 >> d >> c1 >> m >> c2 >> y && c1 == '/' && c2 == '/') {
        cout << "\nCach 2: " << d << "-" << m << "-" << y << endl;
    }
    return 0;
}
```

💡 **Cách 2 rất gọn:** đọc `int char int char int` — các biến `char` "nuốt" dấu phân cách. Áp dụng được cho mọi định dạng cố định như `"12:30:45"`, `"1.2.3"`.

### Bài 8.

```cpp
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string cau;
    cout << "Nhap mot cau: ";
    getline(cin, cau);

    // Tach thanh cac tu
    istringstream iss(cau);
    vector<string> tu;
    string t;
    while (iss >> t) tu.push_back(t);

    // Dao thu tu
    reverse(tu.begin(), tu.end());

    // Noi lai
    ostringstream oss;
    for (size_t i = 0; i < tu.size(); i++) {
        if (i > 0) oss << " ";
        oss << tu[i];
    }

    cout << "Goc : " << cau << endl;
    cout << "Dao : " << oss.str() << endl;
    return 0;
}
```

Ví dụ:

```
Goc : toi hoc lap trinh C++
Dao : C++ trinh lap hoc toi
```

⚠️ **Phân biệt với đảo ngược chuỗi:** đảo từ giữ nguyên từng từ (`"toi"` vẫn là `"toi"`), còn đảo chuỗi thì `"toi"` thành `"iot"`.

### Bài 9.

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

struct SinhVien { string ten; double diem; };

int main() {
    // Du lieu nhieu dong (co the doc tu file)
    string duLieu =
        "An 8.5\n"
        "Binh 7.0\n"
        "Chi 9.5\n"
        "Dung 6.5\n"
        "Em 8.0";

    istringstream iss(duLieu);
    string dong;
    vector<SinhVien> ds;

    while (getline(iss, dong)) {
        if (dong.empty()) continue;

        istringstream dongSS(dong);
        SinhVien sv;
        if (dongSS >> sv.ten >> sv.diem) ds.push_back(sv);
    }

    cout << fixed << setprecision(2);
    cout << "+----------------+--------+" << endl;
    cout << "| HO TEN         |  DIEM  |" << endl;
    cout << "+----------------+--------+" << endl;

    double tong = 0;
    for (const auto& sv : ds) {
        cout << "| " << left << setw(14) << sv.ten
             << " | " << right << setw(6) << sv.diem << " |" << endl;
        tong += sv.diem;
    }
    cout << "+----------------+--------+" << endl;

    if (!ds.empty())
        cout << "Diem trung binh: " << tong / ds.size() << endl;
    return 0;
}
```

💡 **Mẫu "stringstream lồng nhau"** rất hay dùng:
- `stringstream` **ngoài** tách theo **dòng** (`getline`)
- `stringstream` **trong** tách từng dòng thành **các trường** (`>>`)

### Bài 10.

```cpp
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;

struct SanPham { string ten; int soLuong; double donGia; };

string taoBaoCao(const vector<SanPham>& ds) {
    ostringstream oss;

    oss << "+----------------------+------+------------+--------------+\n";
    oss << "| " << left  << setw(20) << "TEN HANG"
        << " | " << right << setw(4)  << "SL"
        << " | " << setw(10) << "DON GIA"
        << " | " << setw(12) << "THANH TIEN" << " |\n";
    oss << "+----------------------+------+------------+--------------+\n";

    oss << fixed << setprecision(0);
    double tongCong = 0;
    for (const auto& sp : ds) {
        double tt = sp.soLuong * sp.donGia;
        tongCong += tt;
        oss << "| " << left  << setw(20) << sp.ten
            << " | " << right << setw(4)  << sp.soLuong
            << " | " << setw(10) << sp.donGia
            << " | " << setw(12) << tt << " |\n";
    }

    oss << "+----------------------+------+------------+--------------+\n";
    oss << "| " << left << setw(38) << "TONG CONG"
        << " | " << right << setw(12) << tongCong << " |\n";
    oss << "+----------------------+------+------------+--------------+\n";

    return oss.str();
}

int main() {
    vector<SanPham> ds = {
        {"But bi",            10, 5000},
        {"Vo 200 trang",       5, 12000},
        {"Thuoc ke 30cm",      3, 8500}
    };

    string baoCao = taoBaoCao(ds);
    cout << baoCao;

    // Loi the: co the luu vao file, gui qua mang, hien trong GUI...
    cout << "\nDo dai bao cao: " << baoCao.length() << " ky tu" << endl;
    return 0;
}
```

💡 **Lợi thế của `ostringstream` so với `cout` trực tiếp:** kết quả là một **chuỗi** — bạn có thể lưu file, gửi qua mạng, hiển thị trong giao diện đồ hoạ, hoặc kiểm thử tự động bằng cách so sánh chuỗi.

### Bài 11.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    // ===== istringstream: chi DOC =====
    istringstream iss("10 20 30");
    int a, b, c;
    iss >> a >> b >> c;
    cout << "istringstream doc: " << a << " " << b << " " << c << endl;
    // iss << 40;           // LOI: khong ghi duoc

    // ===== ostringstream: chi GHI =====
    ostringstream oss;
    oss << "Ket qua: " << 42;
    cout << "ostringstream ghi: " << oss.str() << endl;
    // int x; oss >> x;     // LOI: khong doc duoc

    // ===== stringstream: CA HAI =====
    stringstream ss;
    ss << 100 << " " << 200;          // ghi
    int m, n;
    ss >> m >> n;                      // doc
    cout << "stringstream: " << m << " + " << n << " = " << m + n << endl;
    return 0;
}
```

**Bảng so sánh:**

| Lớp | Đọc (`>>`) | Ghi (`<<`) | Dùng khi |
|---|---|---|---|
| `istringstream` | ✅ | ❌ | **Phân tích** một chuỗi có sẵn |
| `ostringstream` | ❌ | ✅ | **Xây dựng** một chuỗi mới |
| `stringstream` | ✅ | ✅ | Cần cả hai |

✅ **Nên chọn loại hẹp nhất phù hợp** (`istringstream` khi chỉ đọc) — ý đồ rõ ràng hơn và compiler chặn được lỗi dùng sai chiều.

Tất cả đều nằm trong `<sstream>`.

### Bài 12.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    stringstream ss;

    // Lan 1
    ss << "100";
    int a;
    ss >> a;
    cout << "Lan 1: a = " << a << endl;

    // ===== SAI: khong reset =====
    ss << "200";
    int b = -1;
    ss >> b;
    cout << "SAI (khong reset): b = " << b << endl;       // -1, khong doc duoc!

    // ===== DUNG: reset ca HAI thu =====
    ss.clear();        // ① xoa CO TRANG THAI (eofbit, failbit)
    ss.str("");        // ② xoa NOI DUNG chuoi

    ss << "300";
    int c;
    ss >> c;
    cout << "DUNG (co reset): c = " << c << endl;         // 300
    return 0;
}
```

Output:

```
Lan 1: a = 100
SAI (khong reset): b = -1
DUNG (co reset): c = 300
```

**Vì sao cần CẢ HAI lệnh:**

| Lệnh | Xoá gì | Nếu thiếu |
|---|---|---|
| `ss.clear()` | **Cờ trạng thái** (`eofbit`, `failbit`) | Mọi lệnh đọc sau đó đều thất bại |
| `ss.str("")` | **Nội dung** chuỗi bên trong | Dữ liệu cũ vẫn còn, đọc ra sai |

**Giải thích:** sau khi đọc hết `"100"`, `eofbit` được bật. Khi `eofbit` còn bật, `ss >> b` **không làm gì cả** — nên `b` giữ nguyên giá trị cũ.

⚠️ **Thứ tự quan trọng:** gọi `clear()` **trước** `str("")`. Gọi ngược lại cũng được nhưng dễ nhầm.

💡 **Cách đơn giản hơn — tạo mới mỗi lần:**

```cpp
{
    istringstream iss("100");
    iss >> a;
}   // tu dong huy
{
    istringstream iss("200");
    iss >> b;
}
```

Tránh được hoàn toàn vấn đề reset.

### Bài 13.

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <stdexcept>
using namespace std;

// Chuyen chuoi sang kieu T bat ky
template <typename T>
T convert(const string& s) {
    istringstream iss(s);
    T kq;
    if (!(iss >> kq)) throw invalid_argument("Khong the chuyen doi: \"" + s + "\"");
    return kq;
}

// Phien ban an toan - tra ve gia tri mac dinh thay vi nem ngoai le
template <typename T>
T convertOr(const string& s, T macDinh) {
    istringstream iss(s);
    T kq;
    if (iss >> kq) return kq;
    return macDinh;
}

// Chuyen kieu T bat ky sang chuoi
template <typename T>
string toStr(const T& giaTri) {
    ostringstream oss;
    oss << giaTri;
    return oss.str();
}

int main() {
    cout << "convert<int>(\"42\")      = " << convert<int>("42")      << endl;
    cout << "convert<double>(\"3.14\") = " << convert<double>("3.14") << endl;
    cout << "convert<char>(\"A\")      = " << convert<char>("A")      << endl;

    cout << "\nconvertOr<int>(\"abc\", -1) = " << convertOr<int>("abc", -1) << endl;

    cout << "\ntoStr(42)     = \"" << toStr(42)     << "\"" << endl;
    cout << "toStr(3.14)   = \"" << toStr(3.14)   << "\"" << endl;
    cout << "toStr(true)   = \"" << toStr(true)   << "\"" << endl;

    try {
        convert<int>("xyz");
    } catch (const invalid_argument& e) {
        cout << "\nBat loi: " << e.what() << endl;
    }
    return 0;
}
```

Output:

```
convert<int>("42")      = 42
convert<double>("3.14") = 3.14
convert<char>("A")      = A

convertOr<int>("abc", -1) = -1

toStr(42)     = "42"
toStr(3.14)   = "3.14"
toStr(true)   = "1"

Bat loi: Khong the chuyen doi: "xyz"
```

💡 **Ưu điểm của template + stringstream:** hoạt động với **mọi kiểu** có định nghĩa `operator>>` / `operator<<`, kể cả kiểu tự viết:

```cpp
struct Diem { int x, y; };
istream& operator>>(istream& is, Diem& d) { return is >> d.x >> d.y; }

Diem p = convert<Diem>("10 20");     // hoat dong!
```

### Bài 14.

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

vector<string> tachDong(const string& dong, char delim = ',') {
    vector<string> kq;
    istringstream iss(dong);
    string phan;
    while (getline(iss, phan, delim)) kq.push_back(phan);
    return kq;
}

int main() {
    // Du lieu CSV (co the doc tu file bang ifstream)
    string csv =
        "Ho ten,Tuoi,Diem,Thanh pho\n"
        "Nguyen Van An,20,8.5,Ha Noi\n"
        "Tran Thi Binh,22,9.0,TP HCM\n"
        "Le Hoang Cuong,21,7.5,Da Nang\n"
        "Pham Minh Dung,23,8.0,Can Tho";

    istringstream iss(csv);
    string dong;
    vector<vector<string>> bang;

    while (getline(iss, dong)) {
        if (!dong.empty()) bang.push_back(tachDong(dong));
    }

    if (bang.empty()) { cout << "Khong co du lieu!" << endl; return 1; }

    // Tinh do rong toi da cua tung cot
    size_t soCot = bang[0].size();
    vector<size_t> doRong(soCot, 0);
    for (const auto& hang : bang)
        for (size_t j = 0; j < hang.size() && j < soCot; j++)
            doRong[j] = max(doRong[j], hang[j].length());

    // Ham ve duong ke
    auto veDuong = [&]() {
        cout << "+";
        for (size_t j = 0; j < soCot; j++) {
            for (size_t k = 0; k < doRong[j] + 2; k++) cout << "-";
            cout << "+";
        }
        cout << endl;
    };

    // In bang
    veDuong();
    for (size_t i = 0; i < bang.size(); i++) {
        cout << "|";
        for (size_t j = 0; j < soCot; j++) {
            string o = (j < bang[i].size()) ? bang[i][j] : "";
            cout << " " << left << setw(doRong[j]) << o << " |";
        }
        cout << endl;
        if (i == 0) veDuong();           // duong ke sau dong tieu de
    }
    veDuong();

    // Thong ke cot Diem (cot 2)
    double tong = 0;
    int dem = 0;
    for (size_t i = 1; i < bang.size(); i++) {
        if (bang[i].size() > 2) {
            try { tong += stod(bang[i][2]); dem++; } catch (...) {}
        }
    }
    if (dem > 0) {
        cout << fixed << setprecision(2);
        cout << "\nDiem trung binh: " << tong / dem << endl;
    }
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

```cpp
#include <fstream>
ifstream file("dulieu.csv");
string dong;
while (getline(file, dong)) { ... }
file.close();
```

⚠️ **CSV thật phức tạp hơn:** có thể có dấu phẩy trong ngoặc kép (`"Ha Noi, Viet Nam"`), có dấu nháy thoát. Với dữ liệu thật nên dùng thư viện CSV chuyên dụng.

### Bài 15.

```cpp
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string bieuThuc;
    cout << "Nhap bieu thuc (vd: 12 + 34 * 2): ";
    getline(cin, bieuThuc);

    istringstream iss(bieuThuc);

    double kq;
    if (!(iss >> kq)) {
        cout << "Bieu thuc khong hop le!" << endl;
        return 1;
    }

    char op;
    double so;

    // Tinh TUAN TU tu trai sang phai (khong uu tien toan tu)
    while (iss >> op >> so) {
        switch (op) {
            case '+': kq += so; break;
            case '-': kq -= so; break;
            case '*': kq *= so; break;
            case '/':
                if (so == 0) { cout << "Loi: chia cho 0!" << endl; return 1; }
                kq /= so;
                break;
            default:
                cout << "Toan tu '" << op << "' khong hop le!" << endl;
                return 1;
        }
    }

    cout << bieuThuc << " = " << kq << endl;
    cout << "(Tinh tuan tu tu trai sang phai, KHONG uu tien nhan/chia)" << endl;
    return 0;
}
```

Ví dụ:

```
Nhap bieu thuc: 12 + 34 * 2
12 + 34 * 2 = 92
(Tinh tuan tu tu trai sang phai, KHONG uu tien nhan/chia)
```

⚠️ Kết quả là **92** chứ không phải 80, vì chương trình tính `(12 + 34) * 2` thay vì `12 + (34 * 2)`.

💡 **Cải tiến — có ưu tiên toán tử** (thuật toán 2 lượt):

```cpp
#include <iostream>
#include <sstream>
#include <vector>
using namespace std;

int main() {
    string bt;
    getline(cin, bt);
    istringstream iss(bt);

    vector<double> so;
    vector<char>   op;

    double x;
    iss >> x;
    so.push_back(x);

    char c;
    while (iss >> c >> x) { op.push_back(c); so.push_back(x); }

    // LUOT 1: xu ly * va / truoc
    for (size_t i = 0; i < op.size(); ) {
        if (op[i] == '*' || op[i] == '/') {
            double kq = (op[i] == '*') ? so[i] * so[i+1] : so[i] / so[i+1];
            so[i] = kq;
            so.erase(so.begin() + i + 1);
            op.erase(op.begin() + i);
        } else i++;
    }

    // LUOT 2: xu ly + va -
    double kq = so[0];
    for (size_t i = 0; i < op.size(); i++) {
        kq = (op[i] == '+') ? kq + so[i+1] : kq - so[i+1];
    }

    cout << bt << " = " << kq << endl;     // 12 + 34 * 2 = 80  ✔
    return 0;
}
```

💡 Để xử lý cả dấu ngoặc, cần thuật toán **Shunting-yard** của Dijkstra hoặc phân tích đệ quy — vượt ngoài phạm vi bài này.
