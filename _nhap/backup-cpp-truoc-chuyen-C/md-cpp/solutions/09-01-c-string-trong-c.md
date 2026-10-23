# Lời giải — [C++]. String Trong C++

[← Quay lại bài học](../09-01-c-string-trong-c.md)

> Nhớ `#include <string>` khi dùng `std::string` (dù thường `<iostream>` đã kéo theo).

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    // ① Khoi tao truc tiep
    string s1 = "codelab";

    // ② Goi ham khoi tao
    string s2("C++ programming");

    // ③ Sao chep tu chuoi khac
    string s3 = s1;

    // ④ Tao chuoi gom n ky tu giong nhau
    string s4(5, '*');

    // ⑤ Chuoi rong
    string s5;

    // ⑥ Tu mot phan chuoi khac
    string s6(s2, 0, 3);            // 3 ky tu bat dau tu vi tri 0

    cout << "s1 = \"" << s1 << "\"" << endl;
    cout << "s2 = \"" << s2 << "\"" << endl;
    cout << "s3 = \"" << s3 << "\"" << endl;
    cout << "s4 = \"" << s4 << "\"" << endl;     // *****
    cout << "s5 = \"" << s5 << "\" (rong, length = " << s5.length() << ")" << endl;
    cout << "s6 = \"" << s6 << "\"" << endl;     // C++
    return 0;
}
```

💡 `string(n, c)` rất tiện để in đường kẻ: `cout << string(50, '-') << endl;`

### Bài 2.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string hoTen;

    cout << "Nhap ho ten day du: ";
    getline(cin, hoTen);

    cout << "Ho ten   : " << hoTen << endl;
    cout << "Do dai   : " << hoTen.length() << " ky tu" << endl;
    cout << "Do dai   : " << hoTen.size()   << " (size() giong length())" << endl;
    cout << "Rong?    : " << boolalpha << hoTen.empty() << endl;
    return 0;
}
```

⚠️ **`cin >>` chỉ đọc tới khoảng trắng đầu tiên.** Muốn đọc cả dòng phải dùng `getline(cin, s)`.

⚠️ **`length()` và `size()` hoàn toàn giống nhau** — `length()` hợp ngữ nghĩa với chuỗi, `size()` nhất quán với các container khác.

### Bài 3.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "codelab";

    cout << "Cach 1 (chi so)   : ";
    for (size_t i = 0; i < s.length(); i++) cout << s[i] << " ";
    cout << endl;

    cout << "Cach 2 (at)       : ";
    for (size_t i = 0; i < s.length(); i++) cout << s.at(i) << " ";
    cout << endl;

    cout << "Cach 3 (range-for): ";
    for (char c : s) cout << c << " ";
    cout << endl;

    cout << "Cach 4 (iterator) : ";
    for (auto it = s.begin(); it != s.end(); ++it) cout << *it << " ";
    cout << endl;
    return 0;
}
```

| Cách | Kiểm tra biên | Tốc độ | Dùng khi |
|---|---|---|---|
| `s[i]` | ❌ Không | Nhanh nhất | Chắc chắn chỉ số hợp lệ |
| `s.at(i)` | ✅ Có (ném ngoại lệ) | Chậm hơn chút | Chỉ số từ nguồn không tin cậy |
| Range-based for | — | Nhanh | Duyệt toàn bộ, không cần vị trí |

⚠️ Dùng `size_t` cho biến đếm để tránh cảnh báo so sánh signed/unsigned. Hoặc ép `(int)s.length()`.

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int chuCai = 0, chuSo = 0, dauCach = 0, dacBiet = 0;

    for (unsigned char c : s) {
        if      (isalpha(c)) chuCai++;
        else if (isdigit(c)) chuSo++;
        else if (isspace(c)) dauCach++;
        else                 dacBiet++;
    }

    cout << "Chu cai       : " << chuCai  << endl;
    cout << "Chu so        : " << chuSo   << endl;
    cout << "Dau cach      : " << dauCach << endl;
    cout << "Ky tu dac biet: " << dacBiet << endl;
    cout << "Tong          : " << s.length() << endl;
    return 0;
}
```

💡 Dùng `unsigned char c` trong vòng lặp để tránh undefined behavior khi truyền ký tự âm vào `isalpha`/`isdigit`.

### Bài 5.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a = "code", b = "lab";

    // ① Toan tu +
    string s1 = a + b;

    // ② Toan tu +=
    string s2 = a;
    s2 += b;

    // ③ Ham append
    string s3 = a;
    s3.append(b);

    // ④ Noi nhieu thu cung luc
    string s4 = a + b + ".dev" + " - " + to_string(2026);

    cout << "s1 = " << s1 << endl;
    cout << "s2 = " << s2 << endl;
    cout << "s3 = " << s3 << endl;
    cout << "s4 = " << s4 << endl;

    // append con noi duoc mot PHAN chuoi
    string s5 = "abc";
    s5.append("xyz123", 3);          // chi lay 3 ky tu dau
    cout << "s5 = " << s5 << endl;   // abcxyz
    return 0;
}
```

**So sánh:**

| Cách | Tạo chuỗi tạm? | Tốc độ | Ghi chú |
|---|---|---|---|
| `a + b` | ✅ Có | Chậm hơn | Tạo chuỗi mới rồi gán |
| `a += b` | ❌ Không | ✅ Nhanh | Nối trực tiếp vào `a` |
| `a.append(b)` | ❌ Không | ✅ Nhanh | Linh hoạt hơn (nối một phần) |

⚠️ **Nối chuỗi trong vòng lặp:** luôn dùng `+=`, không dùng `s = s + x`:

```cpp
// CHAM: moi vong tao chuoi moi, O(n^2)
for (int i = 0; i < n; i++) s = s + "x";

// NHANH: O(n)
for (int i = 0; i < n; i++) s += "x";
```

⚠️ `"abc" + "def"` **không hợp lệ** — đó là cộng 2 con trỏ `const char*`. Phải có ít nhất một vế là `string`.

### Bài 6.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

// Cach 1: vong lap
string daoNguoc1(string s) {
    int n = s.length();
    for (int i = 0; i < n / 2; i++) swap(s[i], s[n - 1 - i]);
    return s;
}

// Cach 2: dung reverse cua <algorithm>
string daoNguoc2(string s) {
    reverse(s.begin(), s.end());
    return s;
}

// Cach 3: de quy
void daoNguoc3(string& s, int trai, int phai) {
    if (trai >= phai) return;
    swap(s[trai], s[phai]);
    daoNguoc3(s, trai + 1, phai - 1);
}

int main() {
    string s = "codelab";

    cout << "Goc      : " << s << endl;
    cout << "Cach 1   : " << daoNguoc1(s) << endl;
    cout << "Cach 2   : " << daoNguoc2(s) << endl;

    string t = s;
    daoNguoc3(t, 0, t.length() - 1);
    cout << "Cach 3   : " << t << endl;

    // Cach 4: dung iterator nguoc
    string u(s.rbegin(), s.rend());
    cout << "Cach 4   : " << u << endl;
    return 0;
}
```

💡 Cách 4 (`string(s.rbegin(), s.rend())`) ngắn nhất — dùng **reverse iterator** để tạo chuỗi mới theo thứ tự ngược.

### Bài 7.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool laDoiXung(const string& s) {
    int trai = 0, phai = s.length() - 1;

    while (trai < phai) {
        // Bo qua ky tu khong phai chu/so o ben trai
        while (trai < phai && !isalnum((unsigned char)s[trai])) trai++;
        // Bo qua o ben phai
        while (trai < phai && !isalnum((unsigned char)s[phai])) phai--;

        if (tolower((unsigned char)s[trai]) != tolower((unsigned char)s[phai]))
            return false;

        trai++;
        phai--;
    }
    return true;
}

int main() {
    string ds[] = {
        "aba",
        "A man, a plan, a canal: Panama",
        "Race Car",
        "hello",
        ""
    };

    for (const string& s : ds) {
        cout << "\"" << s << "\" -> "
             << (laDoiXung(s) ? "DOI XUNG" : "khong") << endl;
    }
    return 0;
}
```

Output:

```
"aba" -> DOI XUNG
"A man, a plan, a canal: Panama" -> DOI XUNG
"Race Car" -> DOI XUNG
"hello" -> khong
"" -> DOI XUNG
```

**Kỹ thuật 2 con trỏ** với 2 vòng `while` bên trong để **nhảy qua** các ký tự không phải chữ/số.

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap mot cau: ";
    getline(cin, s);

    // Cach 1: dem thu cong
    int dem = 0;
    bool trongTu = false;
    for (unsigned char c : s) {
        if (isspace(c)) {
            trongTu = false;
        } else if (!trongTu) {
            trongTu = true;
            dem++;                    // bat dau mot tu moi
        }
    }
    cout << "Cach 1: " << dem << " tu" << endl;

    // Cach 2: dung stringstream (DON GIAN NHAT)
    stringstream ss(s);
    string tu;
    int dem2 = 0;
    while (ss >> tu) dem2++;
    cout << "Cach 2: " << dem2 << " tu" << endl;

    return 0;
}
```

💡 **Cách 2 với `stringstream`** tự động xử lý mọi trường hợp: nhiều dấu cách liên tiếp, dấu cách ở đầu/cuối, tab. Xem bài [09-07](../09-07-c-stringstream-trong-c-va-ung-dung.md).

💡 Biến cờ `trongTu` trong cách 1 là kỹ thuật kinh điển: chỉ đếm khi **chuyển từ khoảng trắng sang ký tự**.

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string s;
    cout << "Nhap mot cau: ";
    getline(cin, s);

    stringstream ss(s);
    string tu, daiNhat = "", nganNhat = "";

    while (ss >> tu) {
        if (daiNhat.empty() || tu.length() > daiNhat.length())  daiNhat = tu;
        if (nganNhat.empty() || tu.length() < nganNhat.length()) nganNhat = tu;
    }

    if (daiNhat.empty()) {
        cout << "Chuoi khong co tu nao!" << endl;
    } else {
        cout << "Tu dai nhat : \"" << daiNhat  << "\" (" << daiNhat.length()  << " ky tu)" << endl;
        cout << "Tu ngan nhat: \"" << nganNhat << "\" (" << nganNhat.length() << " ky tu)" << endl;
    }
    return 0;
}
```

### Bài 10.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s = "Lap trinh C++ co ban";

    cout << "Chuoi goc : \"" << s << "\" (" << s.length() << " ky tu)" << endl;

    // substr(vi_tri, so_luong)
    cout << "5 ky tu dau : \"" << s.substr(0, 5) << "\"" << endl;
    cout << "5 ky tu cuoi: \"" << s.substr(s.length() - 5) << "\"" << endl;
    cout << "Ky tu 3-7   : \"" << s.substr(3, 5) << "\"" << endl;   // tu vi tri 3, lay 5
    cout << "Tu vi tri 10: \"" << s.substr(10) << "\"" << endl;      // den het chuoi

    // substr an toan
    size_t bd = 100;
    if (bd < s.length()) cout << s.substr(bd) << endl;
    else cout << "Vi tri vuot qua do dai chuoi" << endl;

    return 0;
}
```

**Cú pháp `substr(pos, len)`:**
- `pos` — vị trí bắt đầu (bắt buộc)
- `len` — số ký tự lấy (tuỳ chọn; bỏ qua → lấy đến hết)

⚠️ Nếu `pos > length()` → ném ngoại lệ `std::out_of_range`. Nếu `pos + len` vượt quá độ dài, nó tự cắt tới cuối (không lỗi).

### Bài 11.

```cpp
string s = "codelab";      // do dai 7, chi so hop le 0..6
cout << s[10];             // LOI 1: undefined behavior, KHONG bao loi
cout << s.at(10);          // LOI 2: nem ngoai le out_of_range
```

**Khác biệt cốt lõi:**

| | `s[i]` | `s.at(i)` |
|---|---|---|
| Kiểm tra biên | ❌ Không | ✅ Có |
| Vượt biên | **Undefined behavior** — giá trị rác hoặc crash | Ném `std::out_of_range` |
| Tốc độ | Nhanh hơn | Chậm hơn một chút |

`s[10]` **không báo lỗi gì** — nó đọc vào bộ nhớ ngoài chuỗi. Đây là loại lỗi nguy hiểm vì chương trình có vẻ vẫn chạy.

**Sửa:**

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

int main() {
    string s = "codelab";
    size_t i = 10;

    // Cach 1: kiem tra truoc
    if (i < s.length()) cout << s[i] << endl;
    else cout << "Chi so " << i << " vuot qua do dai " << s.length() << endl;

    // Cach 2: bat ngoai le
    try {
        cout << s.at(i) << endl;
    } catch (const out_of_range& e) {
        cout << "Loi: " << e.what() << endl;
    }
    return 0;
}
```

✅ **Nguyên tắc:** dùng `s[i]` khi bạn **chắc chắn** chỉ số hợp lệ (ví dụ trong vòng `for i < s.length()`); dùng `s.at(i)` khi chỉ số đến từ người dùng hoặc tính toán phức tạp.

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
    // ===== char[] cua C =====
    char c1[50] = "code";
    char c2[50] = "lab";
    char kq[100];

    strcpy(kq, c1);
    strcat(kq, c2);
    cout << "char[] : " << kq << " (do dai " << strlen(kq) << ")" << endl;
    cout << "So sanh: " << (strcmp(c1, c2) == 0 ? "bang" : "khac") << endl;

    // ===== string cua C++ =====
    string s1 = "code";
    string s2 = "lab";
    string s3 = s1 + s2;
    cout << "string : " << s3 << " (do dai " << s3.length() << ")" << endl;
    cout << "So sanh: " << (s1 == s2 ? "bang" : "khac") << endl;

    // Chuyen doi qua lai
    const char* p = s3.c_str();          // string -> const char*
    string s4(c1);                        // char[] -> string
    cout << "c_str(): " << p << endl;
    cout << "tu char[]: " << s4 << endl;
    return 0;
}
```

**Bảng so sánh:**

| Tiêu chí | `char[]` (C) | `std::string` (C++) |
|---|---|---|
| **Kích thước** | ⚠️ Cố định lúc khai báo | ✅ Tự động thay đổi |
| **Tràn bộ đệm** | ⚠️ **Rất dễ** (`strcpy` không kiểm tra) | ✅ Không thể |
| **Nối chuỗi** | `strcat(a, b)` | `a + b` hoặc `a += b` |
| **So sánh** | `strcmp(a, b) == 0` | `a == b` |
| **Độ dài** | `strlen(a)` — **O(n)** mỗi lần gọi | `a.length()` — **O(1)** |
| **Gán** | `strcpy(a, b)` | `a = b` |
| **Sao chép** | ⚠️ Phải tự cấp phát đủ | ✅ Tự động |
| **Ký tự kết thúc** | ⚠️ Phải có `'\0'` | Tự quản lý |
| **Bộ nhớ** | Ít hơn một chút | Có overhead nhỏ |
| **Truyền vào hàm** | Suy biến thành con trỏ | Truyền như đối tượng |

**Ví dụ về nguy hiểm của `char[]`:**

```cpp
char buf[5];
strcpy(buf, "Chuoi rat dai qua muc");   // TRAN BO DEM -> crash hoac lo hong bao mat
```

✅ **Trong C++ luôn dùng `std::string`.** Chỉ dùng `char[]` khi:
- Làm việc với API C (`fopen`, các thư viện C)
- Lập trình nhúng, nơi không có STL
- Cần tối ưu bộ nhớ đến từng byte

Chuyển đổi khi cần: `s.c_str()` cho `string → const char*`, và `string s(p)` cho chiều ngược lại.

### Bài 13.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string dong;
    int soDong = 0;
    long long tongKyTu = 0;

    cout << "Nhap van ban (dong trong de ket thuc):" << endl;

    while (getline(cin, dong)) {
        if (dong.empty()) break;          // dong trong -> dung

        soDong++;
        tongKyTu += dong.length();
    }

    cout << "\nSo dong    : " << soDong << endl;
    cout << "Tong ky tu : " << tongKyTu << endl;
    if (soDong > 0)
        cout << "TB moi dong: " << (double)tongKyTu / soDong << " ky tu" << endl;
    return 0;
}
```

💡 `while (getline(cin, dong))` tự dừng khi gặp **cuối file** (bấm `Ctrl+D` trên Linux/macOS, `Ctrl+Z` trên Windows).

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

// Cat khoang trang o DAU
string trimTrai(const string& s) {
    size_t i = 0;
    while (i < s.length() && isspace((unsigned char)s[i])) i++;
    return s.substr(i);
}

// Cat khoang trang o CUOI
string trimPhai(const string& s) {
    if (s.empty()) return s;
    size_t i = s.length();
    while (i > 0 && isspace((unsigned char)s[i - 1])) i--;
    return s.substr(0, i);
}

// Cat ca hai dau
string trim(const string& s) {
    return trimPhai(trimTrai(s));
}

int main() {
    string s = "   codelab dev   ";

    cout << "Goc      : [" << s           << "]" << endl;
    cout << "trimTrai : [" << trimTrai(s) << "]" << endl;
    cout << "trimPhai : [" << trimPhai(s) << "]" << endl;
    cout << "trim     : [" << trim(s)     << "]" << endl;

    cout << "\nChuoi toan khoang trang: [" << trim("     ") << "]" << endl;
    cout << "Chuoi rong: [" << trim("") << "]" << endl;
    return 0;
}
```

Output:

```
Goc      : [   codelab dev   ]
trimTrai : [codelab dev   ]
trimPhai : [   codelab dev]
trim     : [codelab dev]

Chuoi toan khoang trang: []
Chuoi rong: []
```

💡 Cách viết gọn hơn dùng `find_first_not_of` / `find_last_not_of`:

```cpp
string trim(const string& s) {
    size_t dau = s.find_first_not_of(" \t\n\r\f\v");
    if (dau == string::npos) return "";          // toan khoang trang
    size_t cuoi = s.find_last_not_of(" \t\n\r\f\v");
    return s.substr(dau, cuoi - dau + 1);
}
```

⚠️ Luôn xử lý 2 trường hợp đặc biệt: **chuỗi rỗng** và **chuỗi toàn khoảng trắng**.

### Bài 15.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cctype>
using namespace std;

int main() {
    string dong;
    long long soDong = 0, soTu = 0, soKyTu = 0, soKyTuKhongTrang = 0;

    cout << "Nhap van ban (Ctrl+D de ket thuc tren Linux/macOS, Ctrl+Z tren Windows):" << endl;
    cout << "-----------------------------------------------------------" << endl;

    while (getline(cin, dong)) {
        soDong++;
        soKyTu += dong.length() + 1;          // +1 cho ky tu xuong dong

        for (unsigned char c : dong)
            if (!isspace(c)) soKyTuKhongTrang++;

        // Dem tu bang stringstream
        stringstream ss(dong);
        string tu;
        while (ss >> tu) soTu++;
    }

    cout << "-----------------------------------------------------------" << endl;
    cout << "+-----------------------------+------------+" << endl;
    cout << "| " << left << setw(27) << "THONG KE"
         << " | " << right << setw(10) << "SO LUONG" << " |" << endl;
    cout << "+-----------------------------+------------+" << endl;
    cout << "| " << left << setw(27) << "So dong"
         << " | " << right << setw(10) << soDong << " |" << endl;
    cout << "| " << left << setw(27) << "So tu"
         << " | " << right << setw(10) << soTu << " |" << endl;
    cout << "| " << left << setw(27) << "So ky tu (ke ca trang)"
         << " | " << right << setw(10) << soKyTu << " |" << endl;
    cout << "| " << left << setw(27) << "So ky tu (khong trang)"
         << " | " << right << setw(10) << soKyTuKhongTrang << " |" << endl;
    cout << "+-----------------------------+------------+" << endl;

    if (soDong > 0) {
        cout << fixed << setprecision(2);
        cout << "\nTrung binh " << (double)soTu / soDong << " tu/dong" << endl;
    }
    if (soTu > 0) {
        cout << "Trung binh " << (double)soKyTuKhongTrang / soTu << " ky tu/tu" << endl;
    }
    return 0;
}
```

Chạy thử với file:

```bash
g++ -std=c++17 wc.cpp -o wc
./wc < vanban.txt
```

So sánh với lệnh `wc` của Linux:

```bash
wc vanban.txt          # in ra: so dong, so tu, so byte
```

💡 Đây là bản mô phỏng đơn giản của lệnh `wc` (word count) — một trong những tiện ích Unix cổ điển nhất.
