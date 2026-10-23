# Lời giải — [C++]. So Sánh Xâu Ký Tự Theo Thứ Tự Từ Điển

[← Quay lại bài học](../09-05-c-so-sanh-xau-ky-tu-theo-thu-tu-tu-dien.md)

> **Quy tắc so sánh từ điển (lexicographical):** so sánh **từng ký tự từ trái sang phải** theo **mã ASCII**. Gặp cặp khác nhau đầu tiên thì kết luận ngay. Nếu một chuỗi là tiền tố của chuỗi kia, chuỗi **ngắn hơn** nhỏ hơn.

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a, b;
    cout << "Nhap chuoi 1: "; getline(cin, a);
    cout << "Nhap chuoi 2: "; getline(cin, b);

    cout << boolalpha;
    cout << "\na == b : " << (a == b) << endl;
    cout << "a != b : " << (a != b) << endl;
    cout << "a <  b : " << (a <  b) << endl;
    cout << "a >  b : " << (a >  b) << endl;
    cout << "a <= b : " << (a <= b) << endl;

    cout << "\nKet luan: ";
    if      (a < b) cout << "\"" << a << "\" dung TRUOC \"" << b << "\"" << endl;
    else if (a > b) cout << "\"" << a << "\" dung SAU \""   << b << "\"" << endl;
    else            cout << "Hai chuoi GIONG NHAU" << endl;
    return 0;
}
```

### Bài 2.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string a = "Apple", b = "apple";

    cout << boolalpha << "\"Apple\" < \"apple\" : " << (a < b) << endl;   // true

    cout << "\n--- Phan tich tung ky tu ---" << endl;
    for (size_t i = 0; i < min(a.length(), b.length()); i++) {
        cout << "Vi tri " << i << ": '" << a[i] << "' (" << (int)a[i] << ")"
             << " vs '" << b[i] << "' (" << (int)b[i] << ")";
        if (a[i] != b[i]) { cout << "  <-- KHAC NHAU, ket luan ngay!"; break; }
        cout << "  (bang nhau, xet tiep)";
        cout << endl;
    }
    cout << endl;

    cout << "\n--- Cac moc ASCII ---" << endl;
    cout << "'A' = " << (int)'A' << ", 'Z' = " << (int)'Z' << endl;   // 65, 90
    cout << "'a' = " << (int)'a' << ", 'z' = " << (int)'z' << endl;   // 97, 122
    cout << "'0' = " << (int)'0' << ", '9' = " << (int)'9' << endl;   // 48, 57
    return 0;
}
```

Output:

```
"Apple" < "apple" : true

--- Phan tich tung ky tu ---
Vi tri 0: 'A' (65) vs 'a' (97)  <-- KHAC NHAU, ket luan ngay!
```

**Giải thích:** ngay ký tự đầu tiên đã khác. `'A'` = 65 < `'a'` = 97, nên `"Apple" < "apple"`.

⚠️ **Hệ quả quan trọng: TOÀN BỘ chữ hoa đứng trước TOÀN BỘ chữ thường.**

```
'Z' (90) < 'a' (97)
```

Nên `"Zebra" < "apple"` — điều này thường **không phải** ý người dùng muốn khi sắp xếp tên!

Thứ tự ASCII đầy đủ: `' '` (32) < chữ số (48–57) < chữ hoa (65–90) < `'_'` (95) < chữ thường (97–122)

### Bài 3.

```cpp
#include <iostream>
#include <string>
#include <cctype>
#include <algorithm>
using namespace std;

// Tra ve: <0 neu a < b, 0 neu bang, >0 neu a > b
int soSanhKhongPhanBiet(const string& a, const string& b) {
    size_t n = min(a.length(), b.length());

    for (size_t i = 0; i < n; i++) {
        int ca = tolower((unsigned char)a[i]);
        int cb = tolower((unsigned char)b[i]);
        if (ca != cb) return ca - cb;
    }
    // Moi ky tu chung deu bang nhau -> chuoi ngan hon thi nho hon
    return (int)a.length() - (int)b.length();
}

bool bangNhauKhongPhanBiet(const string& a, const string& b) {
    return soSanhKhongPhanBiet(a, b) == 0;
}

int main() {
    cout << boolalpha;
    cout << "\"Apple\" vs \"apple\" : " << soSanhKhongPhanBiet("Apple", "apple") << " (bang)" << endl;
    cout << "\"Apple\" vs \"Banana\": " << soSanhKhongPhanBiet("Apple", "Banana") << " (am)" << endl;
    cout << "\"Zebra\" vs \"apple\" : " << soSanhKhongPhanBiet("Zebra", "apple") << " (duong)" << endl;

    cout << "\nSo sanh binh thuong: \"Zebra\" < \"apple\" = " << (string("Zebra") < "apple") << endl;
    cout << "Khong phan biet    : \"Zebra\" < \"apple\" = "
         << (soSanhKhongPhanBiet("Zebra", "apple") < 0) << endl;
    return 0;
}
```

Output:

```
"Apple" vs "apple" : 0 (bang)
"Apple" vs "Banana": -1 (am)
"Zebra" vs "apple" : 25 (duong)

So sanh binh thuong: "Zebra" < "apple" = true
Khong phan biet    : "Zebra" < "apple" = false
```

💡 **Đây mới là thứ tự người dùng mong đợi:** `apple` đứng trước `Zebra`.

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cout << "Nhap so chuoi: ";
    cin >> n;
    cin.ignore();

    vector<string> ds(n);
    for (int i = 0; i < n; i++) {
        cout << "  Chuoi " << i + 1 << ": ";
        getline(cin, ds[i]);
    }

    sort(ds.begin(), ds.end());             // sap xep theo thu tu tu dien

    cout << "\n--- Sau khi sap xep ---" << endl;
    for (size_t i = 0; i < ds.size(); i++)
        cout << i + 1 << ". " << ds[i] << endl;

    // Sap xep giam dan
    sort(ds.rbegin(), ds.rend());
    cout << "\n--- Giam dan ---" << endl;
    for (const auto& s : ds) cout << s << endl;
    return 0;
}
```

💡 `sort` mặc định dùng `operator<` của `string`, tức so sánh từ điển — không cần viết thêm gì.

💡 `sort(v.rbegin(), v.rend())` sắp xếp **giảm dần** bằng cách dùng iterator ngược.

### Bài 5.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;

string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
    return s;
}

int main() {
    vector<string> ds = {"Zebra", "apple", "Banana", "cherry", "Apple", "date"};

    cout << "--- Sap xep THONG THUONG (phan biet hoa/thuong) ---" << endl;
    vector<string> a = ds;
    sort(a.begin(), a.end());
    for (const auto& s : a) cout << s << " ";
    cout << endl;

    cout << "\n--- Sap xep KHONG phan biet hoa/thuong ---" << endl;
    vector<string> b = ds;
    sort(b.begin(), b.end(), [](const string& x, const string& y) {
        return toLower(x) < toLower(y);
    });
    for (const auto& s : b) cout << s << " ";
    cout << endl;
    return 0;
}
```

Output:

```
--- Sap xep THONG THUONG (phan biet hoa/thuong) ---
Apple Banana Zebra apple cherry date 

--- Sap xep KHONG phan biet hoa/thuong ---
apple Apple Banana cherry date Zebra 
```

⚠️ Cách trên tạo chuỗi thường mới ở **mỗi lần so sánh** — chậm với danh sách lớn. Cách tối ưu (**decorate-sort-undecorate**):

```cpp
vector<pair<string,string>> tam;              // (khoa_thuong, gia_tri_goc)
for (const auto& s : ds) tam.push_back({toLower(s), s});
sort(tam.begin(), tam.end());
for (const auto& [k, v] : tam) cout << v << " ";
```

### Bài 6.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<string> ds = {"cherry", "apple", "banana", "date", "elderberry"};

    // Cach 1: tu duyet
    string mn = ds[0], mx = ds[0];
    for (const auto& s : ds) {
        if (s < mn) mn = s;
        if (s > mx) mx = s;
    }
    cout << "Cach 1 - Nho nhat: " << mn << ", Lon nhat: " << mx << endl;

    // Cach 2: dung STL
    auto itMin = min_element(ds.begin(), ds.end());
    auto itMax = max_element(ds.begin(), ds.end());
    cout << "Cach 2 - Nho nhat: " << *itMin << ", Lon nhat: " << *itMax << endl;

    // Cach 3: minmax_element (mot lan duyet, nhanh hon)
    auto [p1, p2] = minmax_element(ds.begin(), ds.end());
    cout << "Cach 3 - Nho nhat: " << *p1 << ", Lon nhat: " << *p2 << endl;
    return 0;
}
```

Output:

```
Cach 1 - Nho nhat: apple, Lon nhat: elderberry
```

💡 `minmax_element` tìm cả hai trong **một lần duyệt** với ~1.5n phép so sánh, thay vì 2n khi gọi riêng.

### Bài 7.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << boolalpha;

    cout << "\"abc\" < \"abcd\"  = " << (string("abc") < "abcd") << endl;   // true
    cout << "\"10\"  < \"9\"     = " << (string("10")  < "9")    << endl;   // true !!
    cout << "\"Z\"   < \"a\"     = " << (string("Z")   < "a")    << endl;   // true
    cout << "\"\"    < \"a\"     = " << (string("")    < "a")    << endl;   // true
    cout << "\"abc\" < \"abd\"   = " << (string("abc") < "abd")  << endl;   // true
    return 0;
}
```

**Giải thích từng trường hợp:**

| So sánh | Kết quả | Lý do |
|---|---|---|
| `"abc" < "abcd"` | ✅ true | `"abc"` là **tiền tố** của `"abcd"` → chuỗi ngắn hơn nhỏ hơn |
| `"10" < "9"` | ✅ **true** | So sánh ký tự đầu: `'1'` (49) < `'9'` (57). **Không so sánh giá trị số!** |
| `"Z" < "a"` | ✅ true | `'Z'` (90) < `'a'` (97) |
| `""  < "a"` | ✅ true | Chuỗi rỗng luôn nhỏ nhất |
| `"abc" < "abd"` | ✅ true | Khác ở vị trí 2: `'c'` (99) < `'d'` (100) |

⚠️ **Trường hợp `"10" < "9"` là bẫy kinh điển.** Khi sắp xếp danh sách chuỗi số:

```
Thu tu tu dien:  "1", "10", "100", "2", "20", "3"
Thu tu so hoc:   "1", "2", "3", "10", "20", "100"
```

Đây là lý do tên file trong máy tính hay sắp xếp "lộn xộn": `file1, file10, file2` — xem bài 11 để khắc phục.

### Bài 8.

```cpp
#include <iostream>
#include <string>
using namespace std;

int soSanh(const string& a, const string& b) {
    size_t i = 0;

    // So sanh tung ky tu cho toi khi khac nhau hoac het mot chuoi
    while (i < a.length() && i < b.length()) {
        if (a[i] < b[i]) return -1;
        if (a[i] > b[i]) return  1;
        i++;
    }

    // Moi ky tu chung deu bang nhau -> so sanh DO DAI
    if (a.length() < b.length()) return -1;
    if (a.length() > b.length()) return  1;
    return 0;
}

int main() {
    struct { const char* a; const char* b; } bo[] = {
        {"abc", "abd"}, {"abc", "abc"}, {"abcd", "abc"},
        {"Apple", "apple"}, {"", "a"}, {"10", "9"}
    };

    for (auto& t : bo) {
        int kq = soSanh(t.a, t.b);
        cout << "soSanh(\"" << t.a << "\", \"" << t.b << "\") = " << kq
             << "  -> " << (kq < 0 ? "a < b" : (kq > 0 ? "a > b" : "a == b")) << endl;

        // Kiem chung voi toan tu co san
        int chuan = (string(t.a) < t.b) ? -1 : (string(t.a) > t.b ? 1 : 0);
        if (kq != chuan) cout << "  !!! KHONG KHOP voi toan tu chuan" << endl;
    }
    return 0;
}
```

💡 Đây chính là cách `std::string::compare` và `strcmp` hoạt động bên trong.

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

// Lay TU CUOI CUNG cua ho ten (thuong la ten)
string layTen(const string& hoTen) {
    size_t vt = hoTen.rfind(' ');
    return (vt == string::npos) ? hoTen : hoTen.substr(vt + 1);
}

int main() {
    vector<string> ds = {
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Hoang Cuong",
        "Pham Minh An",
        "Hoang Thi Dung"
    };

    cout << "--- Sap xep theo HO (mac dinh) ---" << endl;
    vector<string> a = ds;
    sort(a.begin(), a.end());
    for (const auto& s : a) cout << "  " << s << endl;

    cout << "\n--- Sap xep theo TEN ---" << endl;
    vector<string> b = ds;
    sort(b.begin(), b.end(), [](const string& x, const string& y) {
        string tx = layTen(x), ty = layTen(y);
        if (tx != ty) return tx < ty;
        return x < y;                   // cung ten -> sap theo ho ten day du
    });
    for (const auto& s : b) cout << "  " << s << " (ten: " << layTen(s) << ")" << endl;
    return 0;
}
```

Output:

```
--- Sap xep theo TEN ---
  Nguyen Van An (ten: An)
  Pham Minh An (ten: An)
  Tran Thi Binh (ten: Binh)
  Le Hoang Cuong (ten: Cuong)
  Hoang Thi Dung (ten: Dung)
```

💡 **Tiêu chí phụ `return x < y;`** đảm bảo kết quả ổn định khi 2 người trùng tên — đây là thói quen tốt khi viết comparator.

### Bài 10.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<string> ds = {"10", "9", "100", "2", "20", "1", "3"};

    cout << "--- Sap xep TU DIEN (mac dinh) ---" << endl;
    vector<string> a = ds;
    sort(a.begin(), a.end());
    for (const auto& s : a) cout << s << " ";
    cout << endl;

    cout << "\n--- Sap xep theo GIA TRI SO ---" << endl;
    vector<string> b = ds;
    sort(b.begin(), b.end(), [](const string& x, const string& y) {
        return stoll(x) < stoll(y);
    });
    for (const auto& s : b) cout << s << " ";
    cout << endl;
    return 0;
}
```

Output:

```
--- Sap xep TU DIEN (mac dinh) ---
1 10 100 2 20 3 9 

--- Sap xep theo GIA TRI SO ---
1 2 3 9 10 20 100 
```

⚠️ `stoll` được gọi **rất nhiều lần** trong quá trình sắp xếp (O(n log n) lần). Với danh sách lớn, nên chuyển đổi trước:

```cpp
vector<pair<long long, string>> tam;
for (const auto& s : ds) tam.push_back({stoll(s), s});
sort(tam.begin(), tam.end());
```

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;

// So sanh "tu nhien": tach cac cum SO ra so sanh theo gia tri
bool soSanhTuNhien(const string& a, const string& b) {
    size_t i = 0, j = 0;

    while (i < a.length() && j < b.length()) {
        if (isdigit((unsigned char)a[i]) && isdigit((unsigned char)b[j])) {
            // Ca hai deu la chu so -> doc nguyen cum so va so sanh gia tri
            size_t i2 = i, j2 = j;
            while (i2 < a.length() && isdigit((unsigned char)a[i2])) i2++;
            while (j2 < b.length() && isdigit((unsigned char)b[j2])) j2++;

            string sa = a.substr(i, i2 - i);
            string sb = b.substr(j, j2 - j);

            // Bo so 0 o dau
            size_t pa = sa.find_first_not_of('0');
            size_t pb = sb.find_first_not_of('0');
            sa = (pa == string::npos) ? "0" : sa.substr(pa);
            sb = (pb == string::npos) ? "0" : sb.substr(pb);

            if (sa.length() != sb.length()) return sa.length() < sb.length();
            if (sa != sb) return sa < sb;

            i = i2; j = j2;
        } else {
            if (a[i] != b[j]) return a[i] < b[j];
            i++; j++;
        }
    }
    return a.length() < b.length();
}

int main() {
    vector<string> ds = {"file10", "file2", "file1", "file20", "file3", "img100", "img9"};

    cout << "--- Sap xep TU DIEN ---" << endl;
    vector<string> a = ds;
    sort(a.begin(), a.end());
    for (const auto& s : a) cout << s << " ";
    cout << endl;

    cout << "\n--- Sap xep TU NHIEN ---" << endl;
    vector<string> b = ds;
    sort(b.begin(), b.end(), soSanhTuNhien);
    for (const auto& s : b) cout << s << " ";
    cout << endl;
    return 0;
}
```

Output:

```
--- Sap xep TU DIEN ---
file1 file10 file2 file20 file3 img100 img9 

--- Sap xep TU NHIEN ---
file1 file2 file3 file10 file20 img9 img100 
```

💡 **Natural sort** là cách Windows Explorer và macOS Finder sắp xếp tên file — đúng với trực giác con người hơn nhiều.

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool daSapXep(const vector<string>& ds) {
    for (size_t i = 0; i + 1 < ds.size(); i++)
        if (ds[i] > ds[i + 1]) return false;
    return true;
}

int main() {
    vector<string> a = {"apple", "banana", "cherry"};
    vector<string> b = {"banana", "apple", "cherry"};

    cout << boolalpha;
    cout << "a da sap xep? " << daSapXep(a) << endl;    // true
    cout << "b da sap xep? " << daSapXep(b) << endl;    // false

    // Dung STL
    cout << "\nDung is_sorted:" << endl;
    cout << "a: " << is_sorted(a.begin(), a.end()) << endl;
    cout << "b: " << is_sorted(b.begin(), b.end()) << endl;

    // Tim vi tri dau tien sai thu tu
    auto it = is_sorted_until(b.begin(), b.end());
    if (it != b.end())
        cout << "Phan tu dau tien sai thu tu: \"" << *it
             << "\" tai vi tri " << (it - b.begin()) << endl;
    return 0;
}
```

💡 `is_sorted_until` trả về iterator tới phần tử **đầu tiên phá vỡ** thứ tự — rất hữu ích khi debug.

### Bài 13.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string tienToChung(const vector<string>& ds) {
    if (ds.empty()) return "";

    string kq = ds[0];

    for (size_t i = 1; i < ds.size(); i++) {
        size_t j = 0;
        while (j < kq.length() && j < ds[i].length() && kq[j] == ds[i][j]) j++;
        kq = kq.substr(0, j);
        if (kq.empty()) break;              // khong con tien to chung
    }
    return kq;
}

// Cach toi uu: chi can so sanh chuoi NHO NHAT va LON NHAT
string tienToChung2(vector<string> ds) {
    if (ds.empty()) return "";
    sort(ds.begin(), ds.end());

    const string& dau  = ds.front();
    const string& cuoi = ds.back();

    size_t j = 0;
    while (j < dau.length() && j < cuoi.length() && dau[j] == cuoi[j]) j++;
    return dau.substr(0, j);
}

int main() {
    vector<vector<string>> boTest = {
        {"flower", "flow", "flight"},
        {"interspecies", "interstellar", "interstate"},
        {"dog", "racecar", "car"},
        {"abc"},
        {}
    };

    for (const auto& ds : boTest) {
        cout << "{ ";
        for (const auto& s : ds) cout << "\"" << s << "\" ";
        cout << "} -> \"" << tienToChung(ds) << "\"" << endl;
    }
    return 0;
}
```

Output:

```
{ "flower" "flow" "flight" } -> "fl"
{ "interspecies" "interstellar" "interstate" } -> "inters"
{ "dog" "racecar" "car" } -> ""
{ "abc" } -> "abc"
{ } -> ""
```

💡 **Cách 2 rất thông minh:** sau khi sắp xếp, tiền tố chung của **toàn bộ** danh sách chính là tiền tố chung của chuỗi **nhỏ nhất** và **lớn nhất** — vì mọi chuỗi ở giữa đều "kẹp" giữa chúng.

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    vector<string> ds = {"banana", "kiwi", "apple", "fig", "date", "cherry", "plum"};

    sort(ds.begin(), ds.end(), [](const string& a, const string& b) {
        if (a.length() != b.length()) return a.length() < b.length();  // tieu chi CHINH
        return a < b;                                                   // tieu chi PHU
    });

    cout << "--- Sap xep theo do dai, roi tu dien ---" << endl;
    for (const auto& s : ds)
        cout << "  " << s << " (" << s.length() << " ky tu)" << endl;
    return 0;
}
```

Output:

```
  fig (3 ky tu)
  date (4 ky tu)
  kiwi (4 ky tu)
  plum (4 ky tu)
  apple (5 ky tu)
  banana (6 ky tu)
  cherry (6 ky tu)
```

💡 **Mẫu comparator nhiều tiêu chí:**

```cpp
if (tieuChi1(a) != tieuChi1(b)) return tieuChi1(a) < tieuChi1(b);
if (tieuChi2(a) != tieuChi2(b)) return tieuChi2(a) < tieuChi2(b);
return tieuChi3(a) < tieuChi3(b);
```

Luôn kiểm tra **khác nhau** trước rồi mới so sánh — nếu không, comparator sẽ sai.

💡 Cách viết gọn dùng `tuple` (tự động so sánh theo thứ tự):

```cpp
sort(ds.begin(), ds.end(), [](const string& a, const string& b) {
    return make_tuple(a.length(), a) < make_tuple(b.length(), b);
});
```

### Bài 15.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;

string toLower(string s) {
    transform(s.begin(), s.end(), s.begin(),
              [](unsigned char c) { return tolower(c); });
    return s;
}

struct MucTu {
    string tu;
    string nghia;
};

class TuDien {
private:
    vector<MucTu> ds;

public:
    void them(const string& tu, const string& nghia) {
        ds.push_back({tu, nghia});
    }

    void sapXep() {
        sort(ds.begin(), ds.end(), [](const MucTu& a, const MucTu& b) {
            return toLower(a.tu) < toLower(b.tu);
        });
    }

    // Tim kiem NHI PHAN - O(log n)
    const MucTu* tim(const string& tu) const {
        string can = toLower(tu);
        int trai = 0, phai = ds.size() - 1;

        while (trai <= phai) {
            int giua = trai + (phai - trai) / 2;
            string gt = toLower(ds[giua].tu);

            if (gt == can)      return &ds[giua];
            else if (gt < can)  trai = giua + 1;
            else                phai = giua - 1;
        }
        return nullptr;
    }

    // Tim cac tu bat dau bang tien to
    vector<const MucTu*> timTienTo(const string& tienTo) const {
        vector<const MucTu*> kq;
        string tt = toLower(tienTo);
        for (const auto& m : ds)
            if (toLower(m.tu).compare(0, tt.length(), tt) == 0)
                kq.push_back(&m);
        return kq;
    }

    void hienThi() const {
        for (const auto& m : ds)
            cout << "  " << m.tu << " : " << m.nghia << endl;
    }

    size_t size() const { return ds.size(); }
};

int main() {
    TuDien td;
    td.them("apple",    "qua tao");
    td.them("banana",   "qua chuoi");
    td.them("cat",      "con meo");
    td.them("dog",      "con cho");
    td.them("elephant", "con voi");
    td.them("car",      "o to");
    td.them("cake",     "banh ngot");

    td.sapXep();

    cout << "=== TU DIEN (" << td.size() << " tu) ===" << endl;
    td.hienThi();

    // Tim kiem chinh xac
    cout << "\n=== TIM KIEM ===" << endl;
    for (string t : {"cat", "Dog", "xyz"}) {
        const MucTu* m = td.tim(t);
        if (m) cout << "  \"" << t << "\" -> " << m->nghia << endl;
        else   cout << "  \"" << t << "\" -> khong tim thay" << endl;
    }

    // Tim theo tien to
    cout << "\n=== GOI Y VOI TIEN TO \"ca\" ===" << endl;
    for (const MucTu* m : td.timTienTo("ca"))
        cout << "  " << m->tu << " : " << m->nghia << endl;

    return 0;
}
```

Output:

```
=== TU DIEN (7 tu) ===
  apple : qua tao
  banana : qua chuoi
  cake : banh ngot
  car : o to
  cat : con meo
  dog : con cho
  elephant : con voi

=== TIM KIEM ===
  "cat" -> con meo
  "Dog" -> con cho
  "xyz" -> khong tim thay

=== GOI Y VOI TIEN TO "ca" ===
  cake : banh ngot
  car : o to
  cat : con meo
```

**Vì sao từ điển phải sắp xếp:** tìm kiếm nhị phân yêu cầu dữ liệu **đã sắp xếp**. Với 100.000 từ:

| Cách tìm | Số phép so sánh |
|---|---|
| Tuyến tính | tối đa 100.000 |
| **Nhị phân** | tối đa **17** |

Xem chi tiết ở bài [10-01 — Tìm kiếm nhị phân](../10-01-c-thuat-toan-tim-kiem-nhi-phan.md).

💡 Trong thực tế, dùng `std::map<string, string>` hoặc `unordered_map` sẽ đơn giản hơn nhiều — nhưng cài đặt tay giúp bạn hiểu cơ chế bên dưới.
