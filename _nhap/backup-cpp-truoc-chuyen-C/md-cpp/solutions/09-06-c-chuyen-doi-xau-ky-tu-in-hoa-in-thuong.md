# Lời giải — [C++]. Chuyển Đổi Xâu Ký Tự In Hoa, In Thường

[← Quay lại bài học](../09-06-c-chuyen-doi-xau-ky-tu-in-hoa-in-thuong.md)

> **Nhắc lại:** `'A'` = 65, `'a'` = 97 — khoảng cách luôn là **32**. `toupper`/`tolower` nằm trong `<cctype>`.

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    string hoa = s;
    for (char& c : hoa) {                // dau & de sua truc tiep
        c = toupper((unsigned char)c);
    }

    cout << "Goc  : " << s   << endl;
    cout << "Hoa  : " << hoa << endl;
    return 0;
}
```

⚠️ **Nhớ dấu `&` trong `for (char& c : hoa)`** — không có nó, `c` chỉ là bản sao và chuỗi không đổi (xem bài [02-10](../02-10-c-kieu-du-lieu-suy-luan-auto-trong-c.md) bài 9).

⚠️ Ép `(unsigned char)` trước khi truyền vào `toupper` — tránh undefined behavior với ký tự có mã âm.

### Bài 2.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
using namespace std;

int main() {
    string s = "LAP TRINH C++ CO BAN";

    string thuong = s;
    transform(thuong.begin(), thuong.end(), thuong.begin(),
              [](unsigned char c) { return tolower(c); });

    cout << "Goc    : " << s      << endl;
    cout << "Thuong : " << thuong << endl;

    // transform vao chuoi KHAC (khong sua chuoi goc)
    string kq(s.length(), ' ');
    transform(s.begin(), s.end(), kq.begin(),
              [](unsigned char c) { return tolower(c); });
    cout << "Kq moi : " << kq << endl;
    return 0;
}
```

**Cú pháp `transform`:**

```cpp
transform(nguon_bat_dau, nguon_ket_thuc, dich_bat_dau, ham_bien_doi);
```

Tham số thứ 3 là **nơi ghi kết quả** — trỏ vào chính chuỗi gốc thì sửa tại chỗ.

⚠️ Nếu ghi vào chuỗi khác, chuỗi đích phải **đủ chỗ** trước (như `string kq(s.length(), ' ')`).

### Bài 3.

```cpp
#include <iostream>
#include <string>
using namespace std;

string toUpperASCII(string s) {
    for (char& c : s)
        if (c >= 'a' && c <= 'z') c -= 32;
    return s;
}

string toLowerASCII(string s) {
    for (char& c : s)
        if (c >= 'A' && c <= 'Z') c += 32;
    return s;
}

// Cach dung phep BIT - nhanh hon
string toUpperBit(string s) {
    for (char& c : s)
        if (c >= 'a' && c <= 'z') c &= ~32;      // TAT bit thu 6
    return s;
}

string toLowerBit(string s) {
    for (char& c : s)
        if (c >= 'A' && c <= 'Z') c |= 32;       // BAT bit thu 6
    return s;
}

int main() {
    string s = "Lap Trinh C++ 2026!";

    cout << "Goc         : " << s               << endl;
    cout << "Hoa (+-32)  : " << toUpperASCII(s) << endl;
    cout << "Thuong(+-32): " << toLowerASCII(s) << endl;
    cout << "Hoa (bit)   : " << toUpperBit(s)   << endl;
    cout << "Thuong(bit) : " << toLowerBit(s)   << endl;
    return 0;
}
```

Output:

```
Goc         : Lap Trinh C++ 2026!
Hoa (+-32)  : LAP TRINH C++ 2026!
Thuong(+-32): lap trinh c++ 2026!
```

**Cơ sở của phép bit:**

```
'A' = 65 = 0100 0001
'a' = 97 = 0110 0001
                ^
         chi khac bit thu 6 (gia tri 32)
```

⚠️ **BẮT BUỘC kiểm tra `if (c >= 'a' && c <= 'z')` trước.** Nếu áp dụng mù quáng lên chữ số hoặc ký tự đặc biệt sẽ ra rác:

```cpp
'5' - 32 = 53 - 32 = 21   // ky tu dieu khien NAK, khong in duoc
'!' + 32 = 33 + 32 = 65 = 'A'   // dau ! bien thanh chu A!
```

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string daoHoaThuong(string s) {
    for (char& c : s) {
        if (islower((unsigned char)c))      c = toupper((unsigned char)c);
        else if (isupper((unsigned char)c)) c = tolower((unsigned char)c);
    }
    return s;
}

// Cach dung phep XOR - rat gon
string daoHoaThuongXOR(string s) {
    for (char& c : s)
        if (isalpha((unsigned char)c)) c ^= 32;     // XOR dao bit thu 6
    return s;
}

int main() {
    string s = "Lap Trinh C++ 2026!";

    cout << "Goc     : " << s                  << endl;
    cout << "Dao     : " << daoHoaThuong(s)    << endl;
    cout << "Dao(XOR): " << daoHoaThuongXOR(s) << endl;

    // Dao 2 lan -> ve nhu cu
    cout << "Dao 2 lan: " << daoHoaThuong(daoHoaThuong(s)) << endl;
    return 0;
}
```

Output:

```
Goc     : Lap Trinh C++ 2026!
Dao     : lAP tRINH c++ 2026!
Dao(XOR): lAP tRINH c++ 2026!
```

💡 **Phép `c ^= 32`** đảo bit thứ 6 — biến hoa thành thường và ngược lại chỉ bằng **một phép toán**.

### Bài 5.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string titleCase(string s) {
    bool dauTu = true;                    // dang o dau mot tu

    for (char& c : s) {
        if (isspace((unsigned char)c)) {
            dauTu = true;
        } else {
            c = dauTu ? toupper((unsigned char)c) : tolower((unsigned char)c);
            dauTu = false;
        }
    }
    return s;
}

int main() {
    string ds[] = {
        "lap trinh c++ co ban",
        "NGUYEN VAN AN",
        "hoc   lap   trinh",
        "  co khoang trang dau  "
    };

    for (const string& s : ds) {
        cout << "\"" << s << "\"" << endl;
        cout << "  -> \"" << titleCase(s) << "\"" << endl;
    }
    return 0;
}
```

Output:

```
"lap trinh c++ co ban"
  -> "Lap Trinh C++ Co Ban"
"NGUYEN VAN AN"
  -> "Nguyen Van An"
"hoc   lap   trinh"
  -> "Hoc   Lap   Trinh"
```

💡 **Biến cờ `dauTu`** là kỹ thuật chuẩn: bật khi gặp khoảng trắng, tắt ngay sau khi xử lý một ký tự.

### Bài 6.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string sentenceCase(string s) {
    bool dauCau = true;

    for (char& c : s) {
        if (dauCau && isalpha((unsigned char)c)) {
            c = toupper((unsigned char)c);
            dauCau = false;
        } else {
            c = tolower((unsigned char)c);
        }

        // Sau dau . ! ? la bat dau cau moi
        if (c == '.' || c == '!' || c == '?') dauCau = true;
    }
    return s;
}

int main() {
    string s = "day LA cau THU NHAT. day la CAU thu hai! con DAY la cau ba?  het.";

    cout << "Goc : " << s << endl;
    cout << "Sau : " << sentenceCase(s) << endl;
    return 0;
}
```

Output:

```
Goc : day LA cau THU NHAT. day la CAU thu hai! con DAY la cau ba?  het.
Sau : Day la cau thu nhat. Day la cau thu hai! Con day la cau ba?  Het.
```

### Bài 7.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
using namespace std;

string toCamelCase(const string& s) {
    istringstream iss(s);
    string tu, kq = "";
    bool dauTien = true;

    while (iss >> tu) {
        for (char& c : tu) c = tolower((unsigned char)c);

        if (dauTien) {
            dauTien = false;                        // tu dau tien: giu thuong
        } else if (!tu.empty()) {
            tu[0] = toupper((unsigned char)tu[0]);  // cac tu sau: viet hoa chu dau
        }
        kq += tu;
    }
    return kq;
}

string toPascalCase(const string& s) {
    istringstream iss(s);
    string tu, kq = "";

    while (iss >> tu) {
        for (char& c : tu) c = tolower((unsigned char)c);
        if (!tu.empty()) tu[0] = toupper((unsigned char)tu[0]);
        kq += tu;
    }
    return kq;
}

int main() {
    string ds[] = {"lap trinh c++", "HELLO WORLD", "tinh tong hai so"};

    for (const string& s : ds) {
        cout << "\"" << s << "\"" << endl;
        cout << "  camelCase : " << toCamelCase(s)  << endl;
        cout << "  PascalCase: " << toPascalCase(s) << endl;
    }
    return 0;
}
```

Output:

```
"lap trinh c++"
  camelCase : lapTrinhC++
  PascalCase: LapTrinhC++
"tinh tong hai so"
  camelCase : tinhTongHaiSo
  PascalCase: TinhTongHaiSo
```

💡 **Quy ước đặt tên trong lập trình:**

| Kiểu | Ví dụ | Thường dùng cho |
|---|---|---|
| `camelCase` | `soHocSinh` | Biến, hàm (Java, JavaScript, C++) |
| `PascalCase` | `SinhVien` | Tên lớp, kiểu dữ liệu |
| `snake_case` | `so_hoc_sinh` | Biến (Python, thư viện chuẩn C++) |
| `SCREAMING_SNAKE` | `MAX_SIZE` | Hằng số |
| `kebab-case` | `lap-trinh-cpp` | URL, tên file, CSS |

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
using namespace std;

string toSnakeCase(const string& s) {
    istringstream iss(s);
    string tu, kq = "";
    bool dauTien = true;

    while (iss >> tu) {
        for (char& c : tu) c = tolower((unsigned char)c);
        if (!dauTien) kq += "_";
        kq += tu;
        dauTien = false;
    }
    return kq;
}

string toKebabCase(const string& s) {
    string kq = toSnakeCase(s);
    for (char& c : kq) if (c == '_') c = '-';
    return kq;
}

// Chuyen camelCase -> snake_case
string camelToSnake(const string& s) {
    string kq = "";
    for (size_t i = 0; i < s.length(); i++) {
        if (isupper((unsigned char)s[i])) {
            if (i > 0) kq += '_';
            kq += tolower((unsigned char)s[i]);
        } else {
            kq += s[i];
        }
    }
    return kq;
}

int main() {
    string s = "Lap Trinh C Plus Plus";
    cout << "Goc         : " << s                << endl;
    cout << "snake_case  : " << toSnakeCase(s)   << endl;
    cout << "kebab-case  : " << toKebabCase(s)   << endl;

    cout << "\ncamelToSnake:" << endl;
    for (string t : {"soHocSinh", "tinhTongHaiSo", "maxValue"})
        cout << "  " << t << " -> " << camelToSnake(t) << endl;
    return 0;
}
```

Output:

```
Goc         : Lap Trinh C Plus Plus
snake_case  : lap_trinh_c_plus_plus
kebab-case  : lap-trinh-c-plus-plus

camelToSnake:
  soHocSinh -> so_hoc_sinh
  tinhTongHaiSo -> tinh_tong_hai_so
  maxValue -> max_value
```

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int hoa = 0, thuong = 0, so = 0, khac = 0;

    for (unsigned char c : s) {
        if      (isupper(c)) hoa++;
        else if (islower(c)) thuong++;
        else if (isdigit(c)) so++;
        else                 khac++;
    }

    cout << "Chu hoa   : " << hoa    << endl;
    cout << "Chu thuong: " << thuong << endl;
    cout << "Chu so    : " << so     << endl;
    cout << "Khac      : " << khac   << endl;
    cout << "Tong      : " << s.length() << endl;

    if (hoa + thuong > 0) {
        cout << "\nTy le chu hoa: "
             << (100.0 * hoa / (hoa + thuong)) << "%" << endl;
    }
    return 0;
}
```

### Bài 10.

```cpp
#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

bool toanHoa(const string& s) {
    bool coChuCai = false;
    for (unsigned char c : s) {
        if (isalpha(c)) {
            coChuCai = true;
            if (!isupper(c)) return false;
        }
    }
    return coChuCai;            // chuoi khong co chu cai -> false
}

bool toanThuong(const string& s) {
    bool coChuCai = false;
    for (unsigned char c : s) {
        if (isalpha(c)) {
            coChuCai = true;
            if (!islower(c)) return false;
        }
    }
    return coChuCai;
}

int main() {
    string ds[] = {"HELLO", "hello", "Hello", "HELLO 123!", "12345", ""};

    cout << boolalpha;
    cout << "Chuoi         | Toan hoa | Toan thuong" << endl;
    cout << "--------------|----------|------------" << endl;
    for (const string& s : ds) {
        cout << "\"" << s << "\"";
        for (size_t k = s.length(); k < 12; k++) cout << " ";
        cout << "| " << (toanHoa(s) ? "  true  " : "  false ")
             << " | " << toanThuong(s) << endl;
    }

    // Cach dung all_of cua <algorithm>
    string t = "HELLO";
    bool kq = all_of(t.begin(), t.end(),
                     [](unsigned char c) { return !isalpha(c) || isupper(c); });
    cout << "\nDung all_of: " << kq << endl;
    return 0;
}
```

⚠️ **Xử lý trường hợp đặc biệt:** chuỗi `"12345"` hoặc `""` không có chữ cái nào — nên trả về `false` (biến cờ `coChuCai` lo việc này).

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    // Vi tri CHAN -> hoa, vi tri LE -> thuong
    string a = s;
    for (size_t i = 0; i < a.length(); i++)
        a[i] = (i % 2 == 0) ? toupper((unsigned char)a[i])
                            : tolower((unsigned char)a[i]);

    cout << "Goc      : " << s << endl;
    cout << "Xen ke   : " << a << endl;

    // Chi tinh vi tri CUA CHU CAI (bo qua khoang trang)
    string b = s;
    int dem = 0;
    for (char& c : b) {
        if (isalpha((unsigned char)c)) {
            c = (dem % 2 == 0) ? toupper((unsigned char)c)
                               : tolower((unsigned char)c);
            dem++;
        }
    }
    cout << "Xen ke 2 : " << b << endl;
    return 0;
}
```

Với input `lap trinh c++`:

```
Goc      : lap trinh c++
Xen ke   : LaP TrInH C++
Xen ke 2 : LaP TrInH C++
```

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    char c = 'a';

    cout << "--- SAI: quen ep kieu ---" << endl;
    cout << "toupper('a') = " << toupper(c) << endl;         // 65 (so!)

    cout << "\n--- DUNG: co ep kieu ---" << endl;
    cout << "(char)toupper('a') = " << (char)toupper(c) << endl;   // A

    cout << "\nKieu tra ve cua toupper: int" << endl;
    cout << "sizeof(toupper('a')) = " << sizeof(toupper(c)) << " byte" << endl;  // 4
    cout << "sizeof(char)         = " << sizeof(char)       << " byte" << endl;  // 1

    // Loi nghiem trong hon: gan truc tiep vao string
    string s = "abc";
    // s[0] = toupper(s[0]);      // OK - tu dong ep ve char khi gan
    cout << "\nGan vao string thi OK: ";
    s[0] = toupper((unsigned char)s[0]);
    cout << s << endl;
    return 0;
}
```

**Vì sao `toupper` trả về `int`:**

1. **Kế thừa từ C:** hàm này có từ thư viện C, nơi tất cả hàm `<ctype.h>` đều nhận và trả `int`.

2. **Cần biểu diễn `EOF`:** các hàm liên quan phải phân biệt được giá trị `EOF` (thường là −1) với mọi giá trị `char` hợp lệ. Nếu trả về `char`, không còn chỗ cho `EOF`.

3. **Tránh vấn đề `char` có dấu:** trên một số hệ thống `char` là có dấu (−128..127), dùng `int` tránh được nhập nhằng.

**Hệ quả thực tế:**

```cpp
cout << toupper('a');              // in ra 65 (SAI y muon)
cout << (char)toupper('a');        // in ra A  (DUNG)

char c = toupper('a');             // OK - phep gan tu dong ep kieu
s[i] = toupper(s[i]);              // OK
```

⚠️ **Chỉ có vấn đề khi truyền thẳng vào `cout`** — vì `cout` chọn cách in dựa trên kiểu của biểu thức.

### Bài 13.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s = "Xin Chao! Toi 20 tuoi, email: an@gmail.com #2026";

    string hoa = s, thuong = s;
    for (char& c : hoa)    c = toupper((unsigned char)c);
    for (char& c : thuong) c = tolower((unsigned char)c);

    cout << "Goc    : " << s      << endl;
    cout << "Hoa    : " << hoa    << endl;
    cout << "Thuong : " << thuong << endl;

    // Kiem tra: chu so va ky tu dac biet KHONG bi doi
    bool nguyenVen = true;
    for (size_t i = 0; i < s.length(); i++) {
        if (!isalpha((unsigned char)s[i])) {
            if (hoa[i] != s[i] || thuong[i] != s[i]) {
                nguyenVen = false;
                cout << "LOI tai vi tri " << i << ": '" << s[i] << "'" << endl;
            }
        }
    }
    cout << "\nKy tu khong phai chu cai giu nguyen: "
         << boolalpha << nguyenVen << endl;
    return 0;
}
```

Output:

```
Goc    : Xin Chao! Toi 20 tuoi, email: an@gmail.com #2026
Hoa    : XIN CHAO! TOI 20 TUOI, EMAIL: AN@GMAIL.COM #2026
Thuong : xin chao! toi 20 tuoi, email: an@gmail.com #2026

Ky tu khong phai chu cai giu nguyen: true
```

✅ **`toupper`/`tolower` an toàn với mọi ký tự** — nếu tham số không phải chữ cái, hàm trả về nguyên giá trị đó. Đây là ưu điểm lớn so với phép `±32` thủ công.

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 5000000;
    string goc(N, 'a');

    // ① Vong lap + toupper
    string a = goc;
    auto t1 = high_resolution_clock::now();
    for (char& c : a) c = toupper((unsigned char)c);
    auto t2 = high_resolution_clock::now();
    cout << "① Vong lap + toupper : "
         << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ② transform
    string b = goc;
    t1 = high_resolution_clock::now();
    transform(b.begin(), b.end(), b.begin(),
              [](unsigned char c) { return toupper(c); });
    t2 = high_resolution_clock::now();
    cout << "② transform          : "
         << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    // ③ Phep bit
    string c = goc;
    t1 = high_resolution_clock::now();
    for (char& ch : c) if (ch >= 'a' && ch <= 'z') ch &= ~32;
    t2 = high_resolution_clock::now();
    cout << "③ Phep bit (& ~32)   : "
         << duration_cast<milliseconds>(t2-t1).count() << " ms" << endl;

    cout << "\nKiem tra ket qua giong nhau: "
         << boolalpha << (a == b && b == c) << endl;
    return 0;
}
```

Kết quả tham khảo (biên dịch `-O2`):

```
① Vong lap + toupper : 18 ms
② transform          : 18 ms
③ Phep bit (& ~32)   : 4 ms

Kiem tra ket qua giong nhau: true
```

**Nhận xét:**

| Cách | Tốc độ | An toàn | Dễ đọc |
|---|---|---|---|
| Vòng lặp + `toupper` | Trung bình | ✅ Cao | ✅ Cao |
| `transform` | Trung bình | ✅ Cao | Trung bình |
| Phép bit | ✅ **Nhanh nhất** (~4×) | ⚠️ Chỉ đúng với ASCII | ⚠️ Thấp |

**Vì sao `toupper` chậm hơn:** nó phải tra bảng locale (để hỗ trợ đa ngôn ngữ), nên có thêm một lần truy cập bộ nhớ.

✅ **Khuyến nghị:** dùng `toupper`/`tolower` — chênh lệch 14 ms trên 5 triệu ký tự hầu như không bao giờ quan trọng, mà tính đúng đắn và dễ đọc thì luôn quan trọng.

### Bài 15.

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

    // ① Tach tu (tu dong bo qua moi khoang trang thua)
    while (iss >> t) {
        // ② Chuyen ca tu ve chu thuong
        for (char& c : t) c = tolower((unsigned char)c);
        // ③ Viet hoa chu cai dau
        if (!t.empty()) t[0] = toupper((unsigned char)t[0]);
        tu.push_back(t);
    }

    // ④ Noi lai bang MOT dau cach
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
        "le hoang    CUONG",
        "   ",
        "a"
    };

    cout << "+--------------------------+--------------------------+" << endl;
    cout << "| GOC                      | CHUAN HOA                |" << endl;
    cout << "+--------------------------+--------------------------+" << endl;
    for (const string& s : ds) {
        string kq = chuanHoaTen(s);
        cout << "| " << left;
        cout.width(24); cout << ("[" + s + "]");
        cout << " | ";
        cout.width(24); cout << ("[" + kq + "]");
        cout << " |" << endl;
    }
    cout << "+--------------------------+--------------------------+" << endl;
    return 0;
}
```

Output:

```
+--------------------------+--------------------------+
| GOC                      | CHUAN HOA                |
+--------------------------+--------------------------+
| [  nGuYen   vAN   an  ]  | [Nguyen Van An]          |
| [TRAN THI BINH]          | [Tran Thi Binh]          |
| [le hoang    CUONG]      | [Le Hoang Cuong]         |
| [   ]                    | []                       |
| [a]                      | [A]                      |
+--------------------------+--------------------------+
```

**4 việc hàm này làm cùng lúc:**
1. **Xoá khoảng trắng thừa** ở đầu, cuối và giữa các từ
2. **Chuẩn hoá** mỗi từ về chữ thường
3. **Viết hoa** chữ cái đầu mỗi từ
4. **Nối lại** bằng đúng một dấu cách

💡 **Mẹo hay nhất:** dùng `istringstream` để tách từ — nó **tự động** xử lý mọi khoảng trắng thừa (dấu cách, tab, nhiều dấu cách liên tiếp), nên không cần viết hàm `trim` riêng.

Xem thêm bài [09-09 — Chuẩn hoá tên và email](../09-09-cpp-chuan-hoa-ten-va-email.md).
