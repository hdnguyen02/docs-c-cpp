# Lời giải — [C++]. Các Hàm String Xử Lý Xâu Trong C++

[← Quay lại bài học](../09-03-c-cac-ham-string-xu-ly-xau-trong-c.md)

> **Quy ước quan trọng:** các hàm tìm kiếm trả về `string::npos` (một giá trị rất lớn) khi **không tìm thấy** — luôn phải kiểm tra.

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "codelab dev";

    cout << "Chuoi    : \"" << s << "\"" << endl;
    cout << "length() : " << s.length()  << endl;      // 11
    cout << "size()   : " << s.size()    << endl;      // 11 (giong length)
    cout << "empty()  : " << boolalpha << s.empty() << endl;   // false

    s.clear();

    cout << "\nSau clear():" << endl;
    cout << "Chuoi    : \"" << s << "\"" << endl;
    cout << "length() : " << s.length()  << endl;      // 0
    cout << "empty()  : " << s.empty()   << endl;      // true

    return 0;
}
```

💡 Dùng `s.empty()` thay vì `s.length() == 0` — rõ nghĩa hơn và với một số container còn nhanh hơn.

### Bài 2.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Lap trinh C++ rat thu vi, C++ manh me";
    string canTim = "C++";

    size_t vt = s.find(canTim);

    if (vt != string::npos) {
        cout << "Tim thay \"" << canTim << "\" tai vi tri " << vt << endl;
        cout << "Doan quanh: \"" << s.substr(vt, 20) << "\"" << endl;
    } else {
        cout << "Khong tim thay!" << endl;
    }

    // Tim tu vi tri chi dinh
    size_t vt2 = s.find(canTim, vt + 1);
    if (vt2 != string::npos)
        cout << "Lan xuat hien thu 2 tai vi tri " << vt2 << endl;

    // Tim chuoi khong ton tai
    if (s.find("Python") == string::npos)
        cout << "Khong tim thay \"Python\"" << endl;
    return 0;
}
```

⚠️ **`string::npos` là một giá trị unsigned RẤT LỚN** (thường là 18446744073709551615). Đừng bao giờ so sánh kiểu:

```cpp
if (s.find("x") < 0)        // SAI! npos la unsigned, khong bao gio < 0
if (s.find("x") == -1)      // SAI (tuy tinh co van dung tren mot so he thong)
if (s.find("x") == string::npos)   // DUNG
```

### Bài 3.

```cpp
#include <iostream>
#include <string>
using namespace std;

int demSoLan(const string& s, const string& can) {
    if (can.empty()) return 0;

    int dem = 0;
    size_t vt = 0;

    while ((vt = s.find(can, vt)) != string::npos) {
        dem++;
        vt += can.length();          // nhay qua doan vua tim thay
    }
    return dem;
}

int main() {
    string s = "aaa bbb aaa ccc aaa";

    cout << "\"aaa\" xuat hien " << demSoLan(s, "aaa") << " lan" << endl;   // 3
    cout << "\"a\"   xuat hien " << demSoLan(s, "a")   << " lan" << endl;   // 9
    cout << "\"xyz\" xuat hien " << demSoLan(s, "xyz") << " lan" << endl;   // 0

    // Dem CHONG LAP (vd "aa" trong "aaa" -> 2 lan)
    cout << "\n--- Dem chong lap ---" << endl;
    int demCL = 0;
    size_t v = 0;
    while ((v = s.find("aa", v)) != string::npos) { demCL++; v++; }   // chi +1
    cout << "\"aa\" (chong lap) xuat hien " << demCL << " lan" << endl;
    return 0;
}
```

💡 **Điểm mấu chốt — `vt += can.length()` hay `vt++`:**
- `vt += can.length()` → **không chồng lấp**: `"aa"` trong `"aaa"` đếm được **1**
- `vt++` → **có chồng lấp**: `"aa"` trong `"aaa"` đếm được **2**

Chọn cách nào tuỳ yêu cầu bài toán.

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<size_t> timTatCa(const string& s, char c) {
    vector<size_t> viTri;
    for (size_t i = 0; i < s.length(); i++)
        if (s[i] == c) viTri.push_back(i);
    return viTri;
}

int main() {
    string s = "codelab.dev/cpp/co-ban";
    char c = '/';

    auto ds = timTatCa(s, c);

    cout << "Chuoi: " << s << endl;
    cout << "Ky tu '" << c << "' xuat hien " << ds.size() << " lan tai: ";
    for (size_t v : ds) cout << v << " ";
    cout << endl;

    // Cach dung find
    cout << "Dung find: ";
    size_t vt = s.find(c);
    while (vt != string::npos) {
        cout << vt << " ";
        vt = s.find(c, vt + 1);
    }
    cout << endl;
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Thay the TAT CA cac lan xuat hien
string thayTatCa(string s, const string& cu, const string& moi) {
    if (cu.empty()) return s;

    size_t vt = 0;
    while ((vt = s.find(cu, vt)) != string::npos) {
        s.replace(vt, cu.length(), moi);
        vt += moi.length();              // nhay qua phan MOI, tranh lap vo han
    }
    return s;
}

int main() {
    string s = "Toi hoc Java, Java rat hay, Java manh me";

    // ① replace mot lan tai vi tri cu the
    string s1 = s;
    s1.replace(8, 4, "C++");             // tu vi tri 8, thay 4 ky tu
    cout << "replace 1 lan : " << s1 << endl;

    // ② Thay the tat ca
    cout << "Thay tat ca   : " << thayTatCa(s, "Java", "C++") << endl;

    // ③ Truong hop nguy hiem: thay "a" bang "aa"
    cout << "a -> aa       : " << thayTatCa("abc", "a", "aa") << endl;   // aabc
    return 0;
}
```

⚠️ **Dòng `vt += moi.length()` cực kỳ quan trọng.** Nếu viết `vt++` hoặc không tăng, khi thay `"a"` bằng `"aa"` chương trình sẽ **lặp vô hạn** (liên tục tìm thấy `"a"` trong phần vừa thay).

### Bài 6.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Lap trinh";

    string a = s;
    a.insert(0, ">>> ");                 // chen vao DAU
    cout << "Chen dau  : " << a << endl;

    string b = s;
    b.insert(b.length(), " C++");         // chen vao CUOI
    cout << "Chen cuoi : " << b << endl;

    string c = s;
    c.insert(4, "hoc ");                  // chen vao GIUA (vi tri 4)
    cout << "Chen giua : " << c << endl;

    string d = s;
    d.insert(3, 5, '*');                  // chen 5 ky tu '*' tai vi tri 3
    cout << "Chen ky tu: " << d << endl;

    return 0;
}
```

Output:

```
Chen dau  : >>> Lap trinh
Chen cuoi : Lap trinh C++
Chen giua : Lap hoc trinh
Chen ky tu: Lap***** trinh
```

💡 Chèn vào cuối thì dùng `s += " C++"` gọn hơn.

### Bài 7.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string goc = "Lap trinh C++ co ban";

    string a = goc;
    a.erase(4, 6);                       // tu vi tri 4, xoa 6 ky tu
    cout << "erase(4, 6)  : " << a << endl;

    string b = goc;
    b.erase(0, 1);                       // xoa 1 ky tu dau
    cout << "Xoa 1 ky tu  : " << b << endl;

    string c = goc;
    c.erase(10);                         // tu vi tri 10 den HET
    cout << "erase(10)    : " << c << endl;

    string d = goc;
    d.erase(d.begin() + 3);              // xoa ky tu tai iterator
    cout << "Xoa vi tri 3 : " << d << endl;

    string e = goc;
    e.erase(e.begin() + 3, e.begin() + 9);  // xoa doan [3, 9)
    cout << "Xoa doan 3-9 : " << e << endl;

    string f = goc;
    f.erase();                           // xoa TAT CA (giong clear())
    cout << "erase()      : [" << f << "]" << endl;
    return 0;
}
```

Output:

```
erase(4, 6)  : Lap C++ co ban
Xoa 1 ky tu  : ap trinh C++ co ban
erase(10)    : Lap trinh
Xoa vi tri 3 : Laptrinh C++ co ban
Xoa doan 3-9 : Lap C++ co ban
erase()      : []
```

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    string hoTen;
    cout << "Nhap ho ten day du: ";
    getline(cin, hoTen);

    // Tach thanh cac tu
    vector<string> tu;
    stringstream ss(hoTen);
    string t;
    while (ss >> t) tu.push_back(t);

    if (tu.empty()) {
        cout << "Chuoi rong!" << endl;
        return 1;
    }

    cout << "\n--- PHAN TICH ---" << endl;
    cout << "Ho       : " << tu.front() << endl;
    cout << "Ten      : " << tu.back()  << endl;

    cout << "Ten dem  : ";
    if (tu.size() <= 2) cout << "(khong co)";
    else for (size_t i = 1; i + 1 < tu.size(); i++) cout << tu[i] << " ";
    cout << endl;

    // Cach dung find/substr truc tiep
    cout << "\n--- Cach dung find/substr ---" << endl;
    size_t vtDau  = hoTen.find(' ');
    size_t vtCuoi = hoTen.rfind(' ');

    if (vtDau != string::npos) {
        cout << "Ho  : " << hoTen.substr(0, vtDau) << endl;
        cout << "Ten : " << hoTen.substr(vtCuoi + 1) << endl;
        if (vtDau != vtCuoi)
            cout << "Dem : " << hoTen.substr(vtDau + 1, vtCuoi - vtDau - 1) << endl;
    }
    return 0;
}
```

Với input `Nguyen Van Minh Anh`:

```
Ho       : Nguyen
Ten      : Anh
Ten dem  : Van Minh 
```

### Bài 9.

```cpp
#include <iostream>
#include <string>
using namespace std;

string layPhanMoRong(const string& tenFile) {
    size_t vt = tenFile.rfind('.');
    if (vt == string::npos) return "";           // khong co duoi
    if (vt == 0) return "";                      // file an kieu .gitignore
    return tenFile.substr(vt + 1);
}

string layTenKhongDuoi(const string& tenFile) {
    size_t vt = tenFile.rfind('.');
    if (vt == string::npos || vt == 0) return tenFile;
    return tenFile.substr(0, vt);
}

string layTenFile(const string& duongDan) {
    size_t vt = duongDan.find_last_of("/\\");    // ho tro ca / va \
    if (vt == string::npos) return duongDan;
    return duongDan.substr(vt + 1);
}

int main() {
    string ds[] = {
        "baitap.cpp",
        "/home/user/docs/bao-cao.final.pdf",
        "C:\\Users\\Admin\\anh.png",
        "README",
        ".gitignore"
    };

    for (const string& f : ds) {
        cout << "Duong dan : " << f << endl;
        cout << "  Ten file: " << layTenFile(f) << endl;
        cout << "  Ten     : " << layTenKhongDuoi(layTenFile(f)) << endl;
        cout << "  Duoi    : " << layPhanMoRong(layTenFile(f)) << endl;
        cout << endl;
    }
    return 0;
}
```

**`find` vs `rfind`:**

| | `find` | `rfind` |
|---|---|---|
| Tìm từ | Trái sang phải | **Phải sang trái** |
| Trả về | Vị trí **đầu tiên** | Vị trí **cuối cùng** |

⚠️ Với `bao-cao.final.pdf`, phải dùng `rfind('.')` để lấy `pdf`. Nếu dùng `find('.')` sẽ ra `final.pdf`.

### Bài 10.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "  codelab-dev_2026!  ";

    cout << "Chuoi: [" << s << "]" << endl;

    // find(chuoi) - tim CA CUM
    cout << "\nfind(\"dev\")            = " << s.find("dev") << endl;

    // find_first_of(tap) - tim ky tu DAU TIEN thuoc tap
    cout << "find_first_of(\"-_\")     = " << s.find_first_of("-_") << endl;

    // find_last_of(tap) - tim ky tu CUOI CUNG thuoc tap
    cout << "find_last_of(\"-_\")      = " << s.find_last_of("-_") << endl;

    // find_first_not_of(tap) - tim ky tu dau tien KHONG thuoc tap
    cout << "find_first_not_of(\" \")  = " << s.find_first_not_of(" ") << endl;

    // find_last_not_of(tap)
    cout << "find_last_not_of(\" \")   = " << s.find_last_not_of(" ") << endl;

    // Ung dung: trim bang find_first/last_not_of
    size_t dau  = s.find_first_not_of(" \t\n");
    size_t cuoi = s.find_last_not_of(" \t\n");
    cout << "\nSau trim: [" << s.substr(dau, cuoi - dau + 1) << "]" << endl;
    return 0;
}
```

**Bảng phân biệt:**

| Hàm | Tìm gì | Ví dụ với `"abc123"` |
|---|---|---|
| `find("bc")` | **Cả cụm** `"bc"` | 1 |
| `find_first_of("321")` | Ký tự đầu tiên thuộc `{3,2,1}` | 3 (ký tự `'1'`) |
| `find_last_of("321")` | Ký tự cuối cùng thuộc tập | 5 (ký tự `'3'`) |
| `find_first_not_of("abc")` | Ký tự đầu tiên **không** thuộc tập | 3 (ký tự `'1'`) |
| `find_last_not_of("321")` | Ký tự cuối cùng **không** thuộc tập | 2 (ký tự `'c'`) |

⚠️ **Nhầm lẫn phổ biến:** `find("abc")` tìm **chuỗi con** `"abc"`, còn `find_first_of("abc")` tìm **bất kỳ ký tự nào** trong `{a, b, c}`.

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

// Tach theo mot KY TU phan cach
vector<string> split(const string& s, char phanCach) {
    vector<string> kq;
    stringstream ss(s);
    string phan;
    while (getline(ss, phan, phanCach)) {
        kq.push_back(phan);
    }
    return kq;
}

// Tach theo mot CHUOI phan cach
vector<string> splitChuoi(const string& s, const string& phanCach) {
    vector<string> kq;
    if (phanCach.empty()) { kq.push_back(s); return kq; }

    size_t batDau = 0, vt;
    while ((vt = s.find(phanCach, batDau)) != string::npos) {
        kq.push_back(s.substr(batDau, vt - batDau));
        batDau = vt + phanCach.length();
    }
    kq.push_back(s.substr(batDau));
    return kq;
}

// Tach theo khoang trang (bo qua nhieu dau cach lien tiep)
vector<string> splitTrang(const string& s) {
    vector<string> kq;
    stringstream ss(s);
    string tu;
    while (ss >> tu) kq.push_back(tu);
    return kq;
}

void in(const string& nhan, const vector<string>& v) {
    cout << nhan << " (" << v.size() << " phan): ";
    for (const auto& x : v) cout << "[" << x << "] ";
    cout << endl;
}

int main() {
    in("split(',')    ", split("An,Binh,Chi,Dung", ','));
    in("split('-')    ", split("2026-09-17", '-'));
    in("splitChuoi    ", splitChuoi("a::b::c", "::"));
    in("splitTrang    ", splitTrang("  nhieu    dau    cach  "));
    in("Co phan rong  ", split("a,,b,", ','));
    return 0;
}
```

Output:

```
split(',')     (4 phan): [An] [Binh] [Chi] [Dung] 
split('-')     (3 phan): [2026] [09] [17] 
splitChuoi     (3 phan): [a] [b] [c] 
splitTrang     (3 phan): [nhieu] [dau] [cach] 
Co phan rong   (4 phan): [a] [] [b] [] 
```

💡 **Khác biệt quan trọng:** `getline` với dấu phân cách **giữ lại phần rỗng** (`"a,,b"` → 3 phần), còn `ss >> tu` **bỏ qua** khoảng trắng liên tiếp. Chọn cách phù hợp với bài toán.

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

string join(const vector<string>& v, const string& phanCach) {
    if (v.empty()) return "";

    string kq = v[0];
    for (size_t i = 1; i < v.size(); i++) {
        kq += phanCach;
        kq += v[i];
    }
    return kq;
}

// Cach dung ostringstream (nhanh hon voi vector lon)
string join2(const vector<string>& v, const string& phanCach) {
    ostringstream oss;
    for (size_t i = 0; i < v.size(); i++) {
        if (i > 0) oss << phanCach;
        oss << v[i];
    }
    return oss.str();
}

int main() {
    vector<string> v = {"C++", "Python", "Java", "Go"};

    cout << "join(\", \")  : " << join(v, ", ")   << endl;
    cout << "join(\" | \") : " << join(v, " | ")  << endl;
    cout << "join(\"\")    : " << join(v, "")     << endl;
    cout << "join2        : " << join2(v, " -> ") << endl;

    vector<string> rong;
    cout << "Vector rong  : [" << join(rong, ",") << "]" << endl;
    return 0;
}
```

Output:

```
join(", ")  : C++, Python, Java, Go
join(" | ") : C++ | Python | Java | Go
join("")    : C++PythonJavaGo
join2        : C++ -> Python -> Java -> Go
Vector rong  : []
```

💡 **Mẹo tránh dấu phân cách thừa:** thêm phần tử **đầu tiên** trước vòng lặp, rồi từ phần tử thứ 2 mới thêm dấu phân cách trước. Cách này gọn hơn việc xoá dấu thừa ở cuối.

### Bài 13.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a = "apple", b = "banana", c = "apple";

    cout << "--- compare() ---" << endl;
    cout << "a.compare(b) = " << a.compare(b) << endl;   // am (a < b)
    cout << "b.compare(a) = " << b.compare(a) << endl;   // duong
    cout << "a.compare(c) = " << a.compare(c) << endl;   // 0

    cout << "\n--- Toan tu ---" << endl;
    cout << boolalpha;
    cout << "a == c : " << (a == c) << endl;
    cout << "a < b  : " << (a < b)  << endl;
    cout << "a > b  : " << (a > b)  << endl;
    cout << "a != b : " << (a != b) << endl;

    // compare mot PHAN chuoi
    string s = "Lap trinh C++";
    cout << "\n--- compare mot phan ---" << endl;
    cout << "s.compare(0, 3, \"Lap\") = " << s.compare(0, 3, "Lap") << endl;  // 0
    cout << "s.compare(10, 3, \"C++\") = " << s.compare(10, 3, "C++") << endl; // 0
    return 0;
}
```

**`compare()` trả về:**

| Giá trị | Ý nghĩa |
|---|---|
| `0` | Hai chuỗi **bằng nhau** |
| `< 0` | Chuỗi gọi hàm **nhỏ hơn** (đứng trước theo từ điển) |
| `> 0` | Chuỗi gọi hàm **lớn hơn** |

✅ **Trong C++ nên dùng toán tử `==`, `<`, `>`** — dễ đọc hơn nhiều so với `compare(x) == 0`.

`compare()` chỉ hữu ích khi:
- So sánh **một phần** chuỗi: `s.compare(pos, len, other)`
- Cần biết mức độ khác biệt (dùng trong hàm sắp xếp tuỳ chỉnh)

### Bài 14.

```cpp
#include <iostream>
#include <string>
using namespace std;

bool batDauBang(const string& s, const string& tienTo) {
    if (tienTo.length() > s.length()) return false;
    return s.compare(0, tienTo.length(), tienTo) == 0;
}

bool ketThucBang(const string& s, const string& hauTo) {
    if (hauTo.length() > s.length()) return false;
    return s.compare(s.length() - hauTo.length(), hauTo.length(), hauTo) == 0;
}

bool chua(const string& s, const string& can) {
    return s.find(can) != string::npos;
}

int main() {
    string s = "baitap01.cpp";

    cout << boolalpha;
    cout << "Bat dau bang \"bai\"  : " << batDauBang(s, "bai")  << endl;   // true
    cout << "Bat dau bang \"tap\"  : " << batDauBang(s, "tap")  << endl;   // false
    cout << "Ket thuc bang \".cpp\": " << ketThucBang(s, ".cpp") << endl;  // true
    cout << "Ket thuc bang \".py\" : " << ketThucBang(s, ".py")  << endl;  // false
    cout << "Chua \"tap0\"         : " << chua(s, "tap0")        << endl;  // true

    // Ung dung: loc file theo duoi
    string ds[] = {"a.cpp", "b.py", "c.cpp", "d.txt"};
    cout << "\nCac file .cpp: ";
    for (const string& f : ds)
        if (ketThucBang(f, ".cpp")) cout << f << " ";
    cout << endl;
    return 0;
}
```

💡 **Từ C++20 có sẵn:**

```cpp
s.starts_with("bai")    // true
s.ends_with(".cpp")     // true
s.contains("tap")       // C++23
```

Biên dịch với `-std=c++20`.

### Bài 15.

**File `chuoi.h`:**

```cpp
#pragma once
#include <string>
#include <vector>

/** @brief Cat khoang trang o dau va cuoi chuoi. */
std::string trim(const std::string& s);

/** @brief Cat khoang trang o dau chuoi. */
std::string trimTrai(const std::string& s);

/** @brief Cat khoang trang o cuoi chuoi. */
std::string trimPhai(const std::string& s);

/** @brief Tach chuoi theo mot ky tu phan cach. */
std::vector<std::string> split(const std::string& s, char phanCach);

/** @brief Tach chuoi theo khoang trang, bo qua cac khoang trang lien tiep. */
std::vector<std::string> splitTrang(const std::string& s);

/** @brief Noi cac phan tu thanh mot chuoi voi dau phan cach. */
std::string join(const std::vector<std::string>& v, const std::string& phanCach);

/** @brief Thay the TAT CA cac lan xuat hien cua `cu` bang `moi`. */
std::string replaceAll(std::string s, const std::string& cu, const std::string& moi);

/** @brief Chuyen toan bo chuoi sang chu HOA. */
std::string toUpper(std::string s);

/** @brief Chuyen toan bo chuoi sang chu thuong. */
std::string toLower(std::string s);

/** @brief Kiem tra chuoi co bat dau bang tien to cho truoc. */
bool startsWith(const std::string& s, const std::string& tienTo);

/** @brief Kiem tra chuoi co ket thuc bang hau to cho truoc. */
bool endsWith(const std::string& s, const std::string& hauTo);

/** @brief Kiem tra chuoi co chua chuoi con cho truoc. */
bool contains(const std::string& s, const std::string& can);

/** @brief Dem so lan xuat hien cua chuoi con (khong chong lap). */
int countOccurrences(const std::string& s, const std::string& can);

/** @brief Dao nguoc chuoi. */
std::string reverseStr(std::string s);

/** @brief Lap lai chuoi n lan. */
std::string repeat(const std::string& s, int n);
```

**File `chuoi.cpp`:**

```cpp
#include "chuoi.h"
#include <sstream>
#include <algorithm>
#include <cctype>
using namespace std;

static const string KHOANG_TRANG = " \t\n\r\f\v";

string trimTrai(const string& s) {
    size_t dau = s.find_first_not_of(KHOANG_TRANG);
    return (dau == string::npos) ? "" : s.substr(dau);
}

string trimPhai(const string& s) {
    size_t cuoi = s.find_last_not_of(KHOANG_TRANG);
    return (cuoi == string::npos) ? "" : s.substr(0, cuoi + 1);
}

string trim(const string& s) {
    return trimPhai(trimTrai(s));
}

vector<string> split(const string& s, char phanCach) {
    vector<string> kq;
    stringstream ss(s);
    string phan;
    while (getline(ss, phan, phanCach)) kq.push_back(phan);
    return kq;
}

vector<string> splitTrang(const string& s) {
    vector<string> kq;
    stringstream ss(s);
    string tu;
    while (ss >> tu) kq.push_back(tu);
    return kq;
}

string join(const vector<string>& v, const string& phanCach) {
    ostringstream oss;
    for (size_t i = 0; i < v.size(); i++) {
        if (i > 0) oss << phanCach;
        oss << v[i];
    }
    return oss.str();
}

string replaceAll(string s, const string& cu, const string& moi) {
    if (cu.empty()) return s;
    size_t vt = 0;
    while ((vt = s.find(cu, vt)) != string::npos) {
        s.replace(vt, cu.length(), moi);
        vt += moi.length();
    }
    return s;
}

string toUpper(string s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return toupper(c); });
    return s;
}

string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
    return s;
}

bool startsWith(const string& s, const string& tienTo) {
    return s.length() >= tienTo.length() &&
           s.compare(0, tienTo.length(), tienTo) == 0;
}

bool endsWith(const string& s, const string& hauTo) {
    return s.length() >= hauTo.length() &&
           s.compare(s.length() - hauTo.length(), hauTo.length(), hauTo) == 0;
}

bool contains(const string& s, const string& can) {
    return s.find(can) != string::npos;
}

int countOccurrences(const string& s, const string& can) {
    if (can.empty()) return 0;
    int dem = 0;
    size_t vt = 0;
    while ((vt = s.find(can, vt)) != string::npos) { dem++; vt += can.length(); }
    return dem;
}

string reverseStr(string s) {
    reverse(s.begin(), s.end());
    return s;
}

string repeat(const string& s, int n) {
    string kq;
    kq.reserve(s.length() * max(0, n));
    for (int i = 0; i < n; i++) kq += s;
    return kq;
}
```

**File `main.cpp` — kiểm thử:**

```cpp
#include <iostream>
#include "chuoi.h"
using namespace std;

int main() {
    cout << "trim          : [" << trim("   codelab   ") << "]" << endl;
    cout << "toUpper       : " << toUpper("Lap trinh C++") << endl;
    cout << "toLower       : " << toLower("LAP TRINH C++") << endl;
    cout << "replaceAll    : " << replaceAll("Java rat hay, Java manh", "Java", "C++") << endl;
    cout << "reverseStr    : " << reverseStr("codelab") << endl;
    cout << "repeat        : " << repeat("-=", 10) << endl;

    cout << boolalpha;
    cout << "startsWith    : " << startsWith("baitap.cpp", "bai")  << endl;
    cout << "endsWith      : " << endsWith("baitap.cpp", ".cpp")   << endl;
    cout << "contains      : " << contains("baitap.cpp", "tap")    << endl;
    cout << "countOccur    : " << countOccurrences("aaa bbb aaa", "aaa") << endl;

    auto v = split("An,Binh,Chi", ',');
    cout << "split + join  : " << join(v, " | ") << endl;

    auto w = splitTrang("  nhieu    dau   cach  ");
    cout << "splitTrang    : " << join(w, "/") << endl;
    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp chuoi.cpp -o chuoi
./chuoi
```

Output:

```
trim          : [codelab]
toUpper       : LAP TRINH C++
toLower       : lap trinh c++
replaceAll    : C++ rat hay, C++ manh
reverseStr    : baledoc
repeat        : -=-=-=-=-=-=-=-=-=-=
startsWith    : true
endsWith      : true
contains      : true
countOccur    : 2
split + join  : An | Binh | Chi
splitTrang    : nhieu/dau/cach
```

💡 **Vì sao một số hàm nhận `string s` (tham trị) thay vì `const string&`:** những hàm như `toUpper`, `replaceAll`, `reverseStr` **cần một bản sao để sửa** rồi trả về. Nhận tham trị là cách gọn nhất — compiler còn tối ưu được bằng move semantics.
