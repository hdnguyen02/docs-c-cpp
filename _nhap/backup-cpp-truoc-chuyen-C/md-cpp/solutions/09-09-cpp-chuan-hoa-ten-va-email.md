# Lời giải — [C++]. Chuẩn Hóa Tên Và Email

[← Quay lại bài học](../09-09-cpp-chuan-hoa-ten-va-email.md)

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>
using namespace std;

string chuanHoaTen(const string& s) {
    istringstream iss(s);
    vector<string> tu;
    string t;

    while (iss >> t) {
        for (char& c : t) c = tolower((unsigned char)c);
        if (!t.empty()) t[0] = toupper((unsigned char)t[0]);
        tu.push_back(t);
    }

    string kq;
    for (size_t i = 0; i < tu.size(); i++) {
        if (i > 0) kq += " ";
        kq += tu[i];
    }
    return kq;
}

int main() {
    string ds[] = {
        "  nGuYen   vAN   an  ",
        "TRAN THI BINH",
        "le    hoang cuong"
    };

    for (const string& s : ds)
        cout << "[" << s << "] -> [" << chuanHoaTen(s) << "]" << endl;
    return 0;
}
```

💡 `istringstream` tự động xử lý mọi khoảng trắng thừa — không cần viết hàm `trim` riêng.

### Bài 2.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

struct HoTen { string ho, dem, ten; };

HoTen tachHoTen(const string& s) {
    istringstream iss(s);
    vector<string> tu;
    string t;
    while (iss >> t) tu.push_back(t);

    HoTen kq;
    if (tu.empty()) return kq;

    kq.ho  = tu.front();
    kq.ten = tu.back();

    if (tu.size() == 1) { kq.ho = ""; kq.ten = tu[0]; }

    for (size_t i = 1; i + 1 < tu.size(); i++) {
        if (!kq.dem.empty()) kq.dem += " ";
        kq.dem += tu[i];
    }
    return kq;
}

int main() {
    string ds[] = {
        "Nguyen Van An",
        "Tran Thi Minh Chau",
        "Le Cuong",
        "An"
    };

    for (const string& s : ds) {
        HoTen h = tachHoTen(s);
        cout << "\"" << s << "\"" << endl;
        cout << "  Ho  : " << (h.ho.empty()  ? "(khong co)" : h.ho)  << endl;
        cout << "  Dem : " << (h.dem.empty() ? "(khong co)" : h.dem) << endl;
        cout << "  Ten : " << h.ten << endl << endl;
    }
    return 0;
}
```

Output:

```
"Nguyen Van An"
  Ho  : Nguyen
  Dem : Van
  Ten : An

"Tran Thi Minh Chau"
  Ho  : Tran
  Dem : Thi Minh
  Ten : Chau
```

⚠️ **Quy ước Việt Nam:** họ đứng **đầu**, tên đứng **cuối** — ngược với phương Tây.

### Bài 3.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>
using namespace std;

string sinhEmail(const string& hoTen, const string& domain = "gmail.com") {
    istringstream iss(hoTen);
    vector<string> tu;
    string t;
    while (iss >> t) {
        for (char& c : t) c = tolower((unsigned char)c);
        tu.push_back(t);
    }

    if (tu.empty()) return "";
    if (tu.size() == 1) return tu[0] + "@" + domain;

    // Mau: ten.ho@domain
    return tu.back() + "." + tu.front() + "@" + domain;
}

int main() {
    string ds[] = {"Nguyen Van An", "TRAN THI BINH", "Le Hoang Cuong"};

    for (const string& s : ds)
        cout << s << "  ->  " << sinhEmail(s) << endl;

    cout << "\nVoi domain khac:" << endl;
    cout << sinhEmail("Nguyen Van An", "company.vn") << endl;
    return 0;
}
```

Output:

```
Nguyen Van An  ->  an.nguyen@gmail.com
TRAN THI BINH  ->  binh.tran@gmail.com
Le Hoang Cuong  ->  cuong.le@gmail.com
```

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool emailHopLe(const string& email) {
    if (email.empty()) return false;

    // ① Phai co dung MOT dau @
    size_t vtAt = email.find('@');
    if (vtAt == string::npos) return false;
    if (email.find('@', vtAt + 1) != string::npos) return false;

    // ② Phan truoc @ khong duoc rong
    if (vtAt == 0) return false;

    // ③ Phan sau @ phai co dau . va khong o dau/cuoi
    string tenMien = email.substr(vtAt + 1);
    size_t vtCham = tenMien.find('.');
    if (vtCham == string::npos) return false;
    if (vtCham == 0 || vtCham == tenMien.length() - 1) return false;

    // ④ Khong duoc co khoang trang
    for (unsigned char c : email)
        if (isspace(c)) return false;

    // ⑤ Chi cho phep chu, so va mot so ky tu dac biet
    for (unsigned char c : email)
        if (!isalnum(c) && c != '@' && c != '.' && c != '_' && c != '-' && c != '+')
            return false;

    return true;
}

int main() {
    string ds[] = {
        "an.nguyen@gmail.com",
        "user_123@company.vn",
        "khongcodauat.com",
        "hai@@dau.com",
        "@thieuten.com",
        "thieu@cham",
        "co khoang@trang.com",
        "cuoi@domain."
    };

    cout << boolalpha;
    for (const string& e : ds) {
        cout << (emailHopLe(e) ? "  HOP LE  " : "KHONG HOP LE")
             << " : " << e << endl;
    }
    return 0;
}
```

⚠️ **Đây chỉ là kiểm tra cơ bản.** Chuẩn email đầy đủ (RFC 5322) rất phức tạp. Trong ứng dụng thật, cách kiểm tra đáng tin cậy nhất là **gửi email xác nhận**.

💡 C++11 có `<regex>` để viết gọn hơn:

```cpp
#include <regex>
bool hopLe(const string& e) {
    static const regex mau(R"(^[\w.+-]+@[\w-]+\.[\w.-]+$)");
    return regex_match(e, mau);
}
```

### Bài 5.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string email;
    cout << "Nhap email: ";
    getline(cin, email);

    size_t vt = email.find('@');
    if (vt == string::npos) {
        cout << "Email khong hop le (thieu @)!" << endl;
        return 1;
    }

    string nguoiDung = email.substr(0, vt);
    string tenMien   = email.substr(vt + 1);

    cout << "Ten nguoi dung : " << nguoiDung << endl;
    cout << "Ten mien       : " << tenMien   << endl;

    // Tach tiep phan duoi cua ten mien
    size_t vtCham = tenMien.rfind('.');
    if (vtCham != string::npos) {
        cout << "  Domain       : " << tenMien.substr(0, vtCham)  << endl;
        cout << "  TLD          : " << tenMien.substr(vtCham + 1) << endl;
    }
    return 0;
}
```

Với `an.nguyen@mail.company.vn`:

```
Ten nguoi dung : an.nguyen
Ten mien       : mail.company.vn
  Domain       : mail.company
  TLD          : vn
```

### Bài 6.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

string chuanHoaEmail(string s) {
    // ① Xoa moi khoang trang
    s.erase(remove_if(s.begin(), s.end(),
                      [](unsigned char c) { return isspace(c); }),
            s.end());

    // ② Chuyen ve chu thuong
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });

    return s;
}

int main() {
    string ds[] = {
        "  An.Nguyen@GMAIL.com  ",
        "USER@Company.VN",
        "a b c@mail.com"
    };

    for (const string& s : ds)
        cout << "[" << s << "]\n  -> [" << chuanHoaEmail(s) << "]" << endl;
    return 0;
}
```

Output:

```
[  An.Nguyen@GMAIL.com  ]
  -> [an.nguyen@gmail.com]
```

💡 **Vì sao chuẩn hoá email quan trọng:** tên miền **không phân biệt hoa thường** theo chuẩn, nên `User@GMAIL.com` và `user@gmail.com` là **cùng một hộp thư**. Không chuẩn hoá sẽ tạo tài khoản trùng trong cơ sở dữ liệu.

💡 **Thành ngữ erase-remove:** `remove_if` chỉ dồn phần tử cần giữ về đầu; phải kết hợp `erase` mới thực sự xoá.

### Bài 7.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cctype>
using namespace std;

string sinhTenDangNhap(const string& hoTen) {
    istringstream iss(hoTen);
    vector<string> tu;
    string t;
    while (iss >> t) {
        for (char& c : t) c = tolower((unsigned char)c);
        tu.push_back(t);
    }

    if (tu.empty()) return "";
    if (tu.size() == 1) return tu[0];

    // Mau: TEN + chu cai dau cua cac tu con lai
    string kq = tu.back();
    for (size_t i = 0; i + 1 < tu.size(); i++)
        if (!tu[i].empty()) kq += tu[i][0];

    return kq;
}

int main() {
    string ds[] = {
        "Nguyen Van An",
        "Tran Thi Minh Chau",
        "Le Cuong",
        "Pham Hoang Minh Duc"
    };

    for (const string& s : ds)
        cout << s << "  ->  " << sinhTenDangNhap(s) << endl;
    return 0;
}
```

Output:

```
Nguyen Van An  ->  annv
Tran Thi Minh Chau  ->  chauttm
Le Cuong  ->  cuongl
Pham Hoang Minh Duc  ->  ducphm
```

💡 Đây là quy ước đặt tên đăng nhập phổ biến ở nhiều công ty Việt Nam.

### Bài 8.

```cpp
#include <iostream>
#include <string>
using namespace std;

string cheEmail(const string& email) {
    size_t vt = email.find('@');
    if (vt == string::npos) return email;

    string nguoiDung = email.substr(0, vt);
    string tenMien   = email.substr(vt);

    size_t n = nguoiDung.length();
    if (n <= 4) {
        // Qua ngan -> che gan het
        return string(1, nguoiDung[0]) + string(n - 1, '*') + tenMien;
    }

    // Giu 3 ky tu dau + 2 ky tu cuoi
    return nguoiDung.substr(0, 3)
         + string(n - 5, '*')
         + nguoiDung.substr(n - 2)
         + tenMien;
}

string cheSDT(const string& sdt) {
    if (sdt.length() < 4) return sdt;
    return sdt.substr(0, 3) + string(sdt.length() - 5, '*') + sdt.substr(sdt.length() - 2);
}

int main() {
    string ds[] = {
        "nguyenvanan@gmail.com",
        "abc@mail.com",
        "a@b.com",
        "verylongusername123@company.vn"
    };

    for (const string& e : ds)
        cout << e << "\n  -> " << cheEmail(e) << endl;

    cout << "\nChe SDT: 0912345678 -> " << cheSDT("0912345678") << endl;
    return 0;
}
```

Output:

```
nguyenvanan@gmail.com
  -> ngu******an@gmail.com
abc@mail.com
  -> a**@mail.com
verylongusername123@company.vn
  -> ver**************23@company.vn
```

💡 Kỹ thuật này gọi là **data masking**, dùng để hiển thị thông tin nhạy cảm trong giao diện hoặc log mà vẫn giữ được tính nhận diện.

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool sdtHopLe(const string& sdt) {
    // ① Phai dung 10 chu so
    if (sdt.length() != 10) return false;

    // ② Bat dau bang 0
    if (sdt[0] != '0') return false;

    // ③ Toan chu so
    for (unsigned char c : sdt)
        if (!isdigit(c)) return false;

    // ④ Dau so hop le (03, 05, 07, 08, 09)
    string dauSo = sdt.substr(0, 2);
    const string HOP_LE[] = {"03", "05", "07", "08", "09"};
    for (const string& d : HOP_LE)
        if (dauSo == d) return true;

    return false;
}

string nhaMang(const string& sdt) {
    if (!sdtHopLe(sdt)) return "Khong xac dinh";
    string d3 = sdt.substr(0, 3);

    if (d3=="032"||d3=="033"||d3=="034"||d3=="035"||d3=="036"||d3=="037"||d3=="038"||d3=="039"||d3=="086"||d3=="096"||d3=="097"||d3=="098") return "Viettel";
    if (d3=="070"||d3=="076"||d3=="077"||d3=="078"||d3=="079"||d3=="089"||d3=="090"||d3=="093") return "MobiFone";
    if (d3=="081"||d3=="082"||d3=="083"||d3=="084"||d3=="085"||d3=="088"||d3=="091"||d3=="094") return "VinaPhone";
    if (d3=="056"||d3=="058"||d3=="092") return "Vietnamobile";
    if (d3=="059"||d3=="099") return "Gmobile";
    return "Khac";
}

int main() {
    string ds[] = {"0912345678", "0387654321", "012345678", "09123456789", "1912345678", "091234567a"};

    cout << boolalpha;
    for (const string& s : ds) {
        cout << s << " -> " << (sdtHopLe(s) ? "HOP LE  " : "KHONG   ");
        if (sdtHopLe(s)) cout << " (" << nhaMang(s) << ")";
        cout << endl;
    }
    return 0;
}
```

### Bài 10.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string chuanHoaSDT(const string& s) {
    // ① Chi giu lai CHU SO va dau + o dau
    string so;
    bool coPlus = false;

    for (size_t i = 0; i < s.length(); i++) {
        if (i == 0 && s[i] == '+') { coPlus = true; continue; }
        if (isdigit((unsigned char)s[i])) so += s[i];
    }

    // ② Doi +84 hoac 84 o dau thanh 0
    if (coPlus && so.substr(0, 2) == "84") {
        so = "0" + so.substr(2);
    } else if (so.length() == 11 && so.substr(0, 2) == "84") {
        so = "0" + so.substr(2);
    }

    return so;
}

int main() {
    string ds[] = {
        "0912 345 678",
        "0912-345-678",
        "+84912345678",
        "84912345678",
        "(091) 234 5678",
        "0912.345.678"
    };

    for (const string& s : ds)
        cout << "[" << s << "]  ->  [" << chuanHoaSDT(s) << "]" << endl;
    return 0;
}
```

Output:

```
[0912 345 678]  ->  [0912345678]
[0912-345-678]  ->  [0912345678]
[+84912345678]  ->  [0912345678]
[84912345678]  ->  [0912345678]
[(091) 234 5678]  ->  [0912345678]
[0912.345.678]  ->  [0912345678]
```

💡 **Nguyên tắc chuẩn hoá:** lọc bỏ mọi ký tự trang trí, chỉ giữ dữ liệu thật, rồi đưa về **một định dạng chuẩn duy nhất**. Điều này rất quan trọng khi lưu vào cơ sở dữ liệu — nếu không, cùng một số điện thoại sẽ được lưu dưới nhiều dạng khác nhau.

### Bài 11.

```cpp
#include <iostream>
#include <string>
using namespace std;

string dinhDangSDT(const string& sdt) {
    if (sdt.length() != 10) return sdt;
    return sdt.substr(0, 4) + " " + sdt.substr(4, 3) + " " + sdt.substr(7, 3);
}

string dinhDangQuocTe(const string& sdt) {
    if (sdt.length() != 10 || sdt[0] != '0') return sdt;
    return "+84 " + sdt.substr(1, 3) + " " + sdt.substr(4, 3) + " " + sdt.substr(7, 3);
}

int main() {
    string ds[] = {"0912345678", "0387654321"};

    for (const string& s : ds) {
        cout << "Goc      : " << s                  << endl;
        cout << "Trong nuoc: " << dinhDangSDT(s)     << endl;
        cout << "Quoc te  : " << dinhDangQuocTe(s)   << endl << endl;
    }
    return 0;
}
```

Output:

```
Goc      : 0912345678
Trong nuoc: 0912 345 678
Quoc te  : +84 912 345 678
```

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <cctype>
using namespace std;

string taoEmailGoc(const string& hoTen) {
    istringstream iss(hoTen);
    vector<string> tu;
    string t;
    while (iss >> t) {
        for (char& c : t) c = tolower((unsigned char)c);
        tu.push_back(t);
    }
    if (tu.empty()) return "";
    if (tu.size() == 1) return tu[0];

    string kq = tu.back();
    for (size_t i = 0; i + 1 < tu.size(); i++)
        if (!tu[i].empty()) kq += tu[i][0];
    return kq;
}

int main() {
    vector<string> ds = {
        "Nguyen Van An",
        "Nguyen Van An",             // TRUNG
        "Nguyen Viet An",            // cung sinh ra "annv"
        "Tran Thi Binh",
        "Nguyen Van An"              // TRUNG lan 3
    };

    const string DOMAIN = "@company.vn";
    set<string> daDung;

    cout << "+----------------------+----------------------------+" << endl;
    cout << "| HO TEN               | EMAIL                      |" << endl;
    cout << "+----------------------+----------------------------+" << endl;

    for (const string& ten : ds) {
        string goc = taoEmailGoc(ten);
        string email = goc;
        int soThu = 1;

        // Neu trung -> them so vao cuoi
        while (daDung.count(email)) {
            soThu++;
            email = goc + to_string(soThu);
        }
        daDung.insert(email);

        cout << "| " << left;
        cout.width(20); cout << ten;
        cout << " | ";
        cout.width(26); cout << (email + DOMAIN);
        cout << " |" << endl;
    }
    cout << "+----------------------+----------------------------+" << endl;
    return 0;
}
```

Output:

```
+----------------------+----------------------------+
| HO TEN               | EMAIL                      |
+----------------------+----------------------------+
| Nguyen Van An        | annv@company.vn            |
| Nguyen Van An        | annv2@company.vn           |
| Nguyen Viet An       | anvn@company.vn            |
| Tran Thi Binh        | binhtt@company.vn          |
| Nguyen Van An        | annv3@company.vn           |
+----------------------+----------------------------+
```

💡 **`set<string> daDung`** cho phép kiểm tra trùng trong **O(log n)** — với danh sách lớn, đây là điểm mấu chốt về hiệu năng.

### Bài 13.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <cctype>
using namespace std;

struct KetQua {
    bool hopLe;
    vector<string> loi;
    int diemManh;                  // 0-5
};

KetQua kiemTraMatKhau(const string& mk) {
    KetQua kq;
    kq.hopLe = true;
    kq.diemManh = 0;

    if (mk.length() < 8) {
        kq.loi.push_back("Phai co it nhat 8 ky tu (hien co " + to_string(mk.length()) + ")");
        kq.hopLe = false;
    } else {
        kq.diemManh++;
        if (mk.length() >= 12) kq.diemManh++;      // diem thuong cho do dai
    }

    bool coHoa = false, coThuong = false, coSo = false, coDacBiet = false;
    for (unsigned char c : mk) {
        if      (isupper(c)) coHoa     = true;
        else if (islower(c)) coThuong  = true;
        else if (isdigit(c)) coSo      = true;
        else if (isprint(c)) coDacBiet = true;
    }

    if (!coHoa)     { kq.loi.push_back("Thieu chu HOA");        kq.hopLe = false; } else kq.diemManh++;
    if (!coThuong)  { kq.loi.push_back("Thieu chu thuong");     kq.hopLe = false; } else kq.diemManh++;
    if (!coSo)      { kq.loi.push_back("Thieu chu so");         kq.hopLe = false; } else kq.diemManh++;
    if (!coDacBiet) { kq.loi.push_back("Thieu ky tu dac biet"); kq.hopLe = false; }

    // Kiem tra mat khau pho bien
    const string YEU[] = {"password", "12345678", "qwerty", "admin123"};
    string thuong = mk;
    for (char& c : thuong) c = tolower((unsigned char)c);
    for (const string& y : YEU)
        if (thuong.find(y) != string::npos) {
            kq.loi.push_back("Chua chuoi pho bien de doan: \"" + y + "\"");
            kq.hopLe = false;
        }

    return kq;
}

int main() {
    string ds[] = {"abc", "abcdefgh", "Abcdefg1", "Abcdef1!", "MyP@ssw0rd2026", "Password123!"};

    for (const string& mk : ds) {
        KetQua kq = kiemTraMatKhau(mk);
        cout << "\"" << mk << "\"" << endl;
        cout << "  Do manh: [";
        for (int i = 0; i < 5; i++) cout << (i < kq.diemManh ? "#" : "-");
        cout << "] " << kq.diemManh << "/5" << endl;
        cout << "  Ket qua: " << (kq.hopLe ? "HOP LE" : "KHONG HOP LE") << endl;
        for (const string& l : kq.loi) cout << "    - " << l << endl;
        cout << endl;
    }
    return 0;
}
```

⚠️ **Trong ứng dụng thật, KHÔNG BAO GIỜ lưu mật khẩu dạng văn bản thuần.** Phải lưu **hash** với thuật toán chuyên dụng (bcrypt, argon2, scrypt) kèm salt.

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <cctype>
using namespace std;

string chuanHoaDiaChi(const string& s) {
    // Bang thay the cac tu viet tat
    static const map<string, string> VIET_TAT = {
        {"tp",   "TP"},   {"tp.",  "TP"},
        {"q",    "Quan"}, {"q.",   "Quan"},
        {"p",    "Phuong"},{"p.",  "Phuong"},
        {"h",    "Huyen"},{"h.",   "Huyen"},
        {"t",    "Tinh"}, {"t.",   "Tinh"},
        {"tx",   "Thi xa"},{"tx.", "Thi xa"},
        {"duong","Duong"},{"d.",   "Duong"},
        {"hcm",  "Ho Chi Minh"},
        {"hn",   "Ha Noi"}
    };

    istringstream iss(s);
    vector<string> tu;
    string t;

    while (iss >> t) {
        string thuong = t;
        for (char& c : thuong) c = tolower((unsigned char)c);

        auto it = VIET_TAT.find(thuong);
        if (it != VIET_TAT.end()) {
            tu.push_back(it->second);
        } else {
            // Viet hoa chu cai dau, con lai thuong
            for (char& c : t) c = tolower((unsigned char)c);
            if (!t.empty()) t[0] = toupper((unsigned char)t[0]);
            tu.push_back(t);
        }
    }

    string kq;
    for (size_t i = 0; i < tu.size(); i++) {
        if (i > 0) kq += " ";
        kq += tu[i];
    }
    return kq;
}

int main() {
    string ds[] = {
        "  123 nguyen trai, q.1, tp.hcm  ",
        "45 LE LOI, P.BEN NGHE, Q1, TPHCM",
        "so 7 duong lang, h. tu liem, hn"
    };

    for (const string& s : ds)
        cout << "[" << s << "]\n  -> [" << chuanHoaDiaChi(s) << "]\n" << endl;
    return 0;
}
```

⚠️ Chuẩn hoá địa chỉ thật sự rất phức tạp (phụ thuộc quy ước hành chính, dấu tiếng Việt, đơn vị hành chính thay đổi). Bản trên chỉ minh hoạ nguyên lý.

### Bài 15.

**File `chuanhoa.h`:**

```cpp
#pragma once
#include <string>
#include <vector>

/** @brief Chuan hoa ho ten: xoa khoang trang thua, viet hoa chu cai dau moi tu. */
std::string chuanHoaTen(const std::string& s);

/** @brief Sinh email tu ho ten theo mau ten.ho@domain. */
std::string sinhEmail(const std::string& hoTen,
                      const std::string& domain = "gmail.com");

/** @brief Sinh ten dang nhap tu ho ten theo mau: ten + chu cai dau cac tu con lai. */
std::string sinhTenDangNhap(const std::string& hoTen);

/** @brief Kiem tra email co dung dinh dang co ban khong. */
bool kiemTraEmail(const std::string& email);

/** @brief Chuan hoa email: xoa khoang trang, chuyen ve chu thuong. */
std::string chuanHoaEmail(std::string s);

/** @brief Che mot phan email de bao mat. */
std::string cheEmail(const std::string& email);

/** @brief Chuan hoa so dien thoai VN: bo ky tu trang tri, doi +84 thanh 0. */
std::string chuanHoaSDT(const std::string& s);

/** @brief Kiem tra so dien thoai VN hop le (10 so, dau so dung). */
bool kiemTraSDT(const std::string& sdt);

/** @brief Dinh dang so dien thoai thanh 0xxx xxx xxx. */
std::string dinhDangSDT(const std::string& sdt);

/** @brief Ket qua kiem tra mat khau. */
struct KetQuaMatKhau {
    bool hopLe;
    int  doManh;                          // 0-5
    std::vector<std::string> loi;
};

/** @brief Kiem tra do manh cua mat khau. */
KetQuaMatKhau kiemTraMatKhau(const std::string& mk);
```

**File `chuanhoa.cpp`:**

```cpp
#include "chuanhoa.h"
#include <sstream>
#include <algorithm>
#include <cctype>
using namespace std;

static vector<string> tachTu(const string& s, bool veThuong = true) {
    istringstream iss(s);
    vector<string> tu;
    string t;
    while (iss >> t) {
        if (veThuong)
            for (char& c : t) c = tolower((unsigned char)c);
        tu.push_back(t);
    }
    return tu;
}

string chuanHoaTen(const string& s) {
    auto tu = tachTu(s);
    string kq;
    for (size_t i = 0; i < tu.size(); i++) {
        if (i > 0) kq += " ";
        string t = tu[i];
        if (!t.empty()) t[0] = toupper((unsigned char)t[0]);
        kq += t;
    }
    return kq;
}

string sinhEmail(const string& hoTen, const string& domain) {
    auto tu = tachTu(hoTen);
    if (tu.empty()) return "";
    if (tu.size() == 1) return tu[0] + "@" + domain;
    return tu.back() + "." + tu.front() + "@" + domain;
}

string sinhTenDangNhap(const string& hoTen) {
    auto tu = tachTu(hoTen);
    if (tu.empty()) return "";
    if (tu.size() == 1) return tu[0];

    string kq = tu.back();
    for (size_t i = 0; i + 1 < tu.size(); i++)
        if (!tu[i].empty()) kq += tu[i][0];
    return kq;
}

bool kiemTraEmail(const string& email) {
    if (email.empty()) return false;

    size_t vtAt = email.find('@');
    if (vtAt == string::npos || vtAt == 0) return false;
    if (email.find('@', vtAt + 1) != string::npos) return false;

    string mien = email.substr(vtAt + 1);
    size_t vtCham = mien.find('.');
    if (vtCham == string::npos || vtCham == 0 || vtCham == mien.length() - 1)
        return false;

    for (unsigned char c : email) {
        if (isspace(c)) return false;
        if (!isalnum(c) && c != '@' && c != '.' && c != '_' && c != '-' && c != '+')
            return false;
    }
    return true;
}

string chuanHoaEmail(string s) {
    s.erase(remove_if(s.begin(), s.end(),
                      [](unsigned char c) { return isspace(c); }), s.end());
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
    return s;
}

string cheEmail(const string& email) {
    size_t vt = email.find('@');
    if (vt == string::npos) return email;

    string nd = email.substr(0, vt), mien = email.substr(vt);
    size_t n = nd.length();

    if (n <= 4) return string(1, nd[0]) + string(n - 1, '*') + mien;
    return nd.substr(0, 3) + string(n - 5, '*') + nd.substr(n - 2) + mien;
}

string chuanHoaSDT(const string& s) {
    string so;
    bool coPlus = (!s.empty() && s[0] == '+');

    for (unsigned char c : s)
        if (isdigit(c)) so += c;

    if ((coPlus || so.length() == 11) && so.substr(0, 2) == "84")
        so = "0" + so.substr(2);

    return so;
}

bool kiemTraSDT(const string& sdt) {
    if (sdt.length() != 10 || sdt[0] != '0') return false;
    for (unsigned char c : sdt) if (!isdigit(c)) return false;

    string d2 = sdt.substr(0, 2);
    return d2 == "03" || d2 == "05" || d2 == "07" || d2 == "08" || d2 == "09";
}

string dinhDangSDT(const string& sdt) {
    if (sdt.length() != 10) return sdt;
    return sdt.substr(0, 4) + " " + sdt.substr(4, 3) + " " + sdt.substr(7, 3);
}

KetQuaMatKhau kiemTraMatKhau(const string& mk) {
    KetQuaMatKhau kq{true, 0, {}};

    if (mk.length() < 8) {
        kq.loi.push_back("Phai co it nhat 8 ky tu");
        kq.hopLe = false;
    } else {
        kq.doManh++;
        if (mk.length() >= 12) kq.doManh++;
    }

    bool hoa = false, thuong = false, so = false, dacBiet = false;
    for (unsigned char c : mk) {
        if      (isupper(c)) hoa     = true;
        else if (islower(c)) thuong  = true;
        else if (isdigit(c)) so      = true;
        else if (isprint(c)) dacBiet = true;
    }

    if (!hoa)     { kq.loi.push_back("Thieu chu HOA");        kq.hopLe = false; } else kq.doManh++;
    if (!thuong)  { kq.loi.push_back("Thieu chu thuong");     kq.hopLe = false; } else kq.doManh++;
    if (!so)      { kq.loi.push_back("Thieu chu so");         kq.hopLe = false; } else kq.doManh++;
    if (!dacBiet) { kq.loi.push_back("Thieu ky tu dac biet"); kq.hopLe = false; }

    if (kq.doManh > 5) kq.doManh = 5;
    return kq;
}
```

**File `main.cpp` — kiểm thử:**

```cpp
#include <iostream>
#include <iomanip>
#include "chuanhoa.h"
using namespace std;

int main() {
    string ten = "  nGuYen   vAN   an  ";

    cout << "=== CHUAN HOA TEN ===" << endl;
    cout << "Goc          : [" << ten << "]" << endl;
    cout << "Chuan hoa    : [" << chuanHoaTen(ten) << "]" << endl;
    cout << "Email        : " << sinhEmail(chuanHoaTen(ten), "company.vn") << endl;
    cout << "Ten dang nhap: " << sinhTenDangNhap(ten) << endl;

    cout << "\n=== EMAIL ===" << endl;
    string e = "  An.Nguyen@GMAIL.com  ";
    string ec = chuanHoaEmail(e);
    cout << "Goc       : [" << e << "]" << endl;
    cout << "Chuan hoa : " << ec << endl;
    cout << "Hop le    : " << boolalpha << kiemTraEmail(ec) << endl;
    cout << "Che       : " << cheEmail(ec) << endl;

    cout << "\n=== SO DIEN THOAI ===" << endl;
    for (string s : {"0912 345 678", "+84912345678", "(091) 234-5678"}) {
        string c = chuanHoaSDT(s);
        cout << left << setw(18) << ("[" + s + "]") << " -> " << c
             << "  " << (kiemTraSDT(c) ? "HOP LE" : "KHONG") 
             << "  " << dinhDangSDT(c) << endl;
    }

    cout << "\n=== MAT KHAU ===" << endl;
    for (string mk : {"abc", "Abcdef1!", "MyP@ssw0rd2026"}) {
        auto kq = kiemTraMatKhau(mk);
        cout << left << setw(18) << ("\"" + mk + "\"") << " [";
        for (int i = 0; i < 5; i++) cout << (i < kq.doManh ? "#" : "-");
        cout << "] " << (kq.hopLe ? "HOP LE" : "YEU") << endl;
        for (const auto& l : kq.loi) cout << "      - " << l << endl;
    }
    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp chuanhoa.cpp -o chuanhoa
./chuanhoa
```
