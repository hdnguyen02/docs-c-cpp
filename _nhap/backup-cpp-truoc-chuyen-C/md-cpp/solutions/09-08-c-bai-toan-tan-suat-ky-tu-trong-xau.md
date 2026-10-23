# Lời giải — [C++]. Bài Toán Tần Suất Ký Tự Trong Xâu

[← Quay lại bài học](../09-08-c-bai-toan-tan-suat-ky-tu-trong-xau.md)

> **Kỹ thuật cốt lõi:** dùng **mảng đánh dấu** — lấy mã ký tự làm chỉ số. Mọi thao tác tra cứu và cập nhật đều **O(1)**.

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

    int dem[26] = {};

    for (unsigned char c : s)
        if (isalpha(c)) dem[tolower(c) - 'a']++;

    cout << "\nTan suat cac chu cai:" << endl;
    for (int i = 0; i < 26; i++)
        if (dem[i] > 0)
            cout << "  '" << (char)('a' + i) << "' : " << dem[i] << " lan" << endl;
    return 0;
}
```

**Công thức ánh xạ:** `'a'` → 0, `'b'` → 1, …, `'z'` → 25 nhờ `c - 'a'`.

`tolower` đưa mọi chữ cái về thường trước, nên `'A'` và `'a'` được đếm chung.

### Bài 2.

```cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int dem[256] = {};

    for (unsigned char c : s) dem[c]++;      // dung TRUC TIEP ma ASCII lam chi so

    cout << "\nTan suat moi ky tu:" << endl;
    for (int i = 0; i < 256; i++) {
        if (dem[i] > 0) {
            cout << "  ";
            if (isprint(i)) cout << "'" << (char)i << "'";
            else            cout << "[" << i << "]";
            cout << setw(6) << " (ma " << i << ") : " << dem[i] << " lan" << endl;
        }
    }
    return 0;
}
```

⚠️ **Bắt buộc dùng `unsigned char`** trong vòng lặp. Nếu dùng `char` (có thể âm trên một số hệ thống), `dem[c]` với `c` âm sẽ ghi ra **ngoài mảng** → crash hoặc hỏng dữ liệu.

💡 Mảng 256 phần tử phủ hết bảng mã 1 byte, nên đếm được **mọi** ký tự chứ không chỉ chữ cái.

### Bài 3.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int dem[26] = {};
    for (unsigned char c : s)
        if (isalpha(c)) dem[tolower(c) - 'a']++;

    int viTriMax = -1, viTriMin = -1;
    for (int i = 0; i < 26; i++) {
        if (dem[i] == 0) continue;
        if (viTriMax == -1 || dem[i] > dem[viTriMax]) viTriMax = i;
        if (viTriMin == -1 || dem[i] < dem[viTriMin]) viTriMin = i;
    }

    if (viTriMax == -1) {
        cout << "Chuoi khong co chu cai nao!" << endl;
        return 0;
    }

    cout << "Nhieu nhat: '" << (char)('a' + viTriMax)
         << "' - " << dem[viTriMax] << " lan" << endl;
    cout << "It nhat   : '" << (char)('a' + viTriMin)
         << "' - " << dem[viTriMin] << " lan" << endl;

    // Liet ke TAT CA ky tu co tan suat cao nhat (co the co nhieu)
    cout << "\nTat ca ky tu xuat hien nhieu nhat: ";
    for (int i = 0; i < 26; i++)
        if (dem[i] == dem[viTriMax]) cout << "'" << (char)('a' + i) << "' ";
    cout << endl;
    return 0;
}
```

⚠️ **Phải bỏ qua các ký tự có `dem[i] == 0`** khi tìm min — nếu không, kết quả luôn là một chữ cái không xuất hiện.

### Bài 4.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int dem[256] = {};
    for (unsigned char c : s) dem[c]++;           // LUOT 1: dem

    for (unsigned char c : s) {                   // LUOT 2: tim theo THU TU chuoi
        if (dem[c] == 1) {
            cout << "Ky tu dau tien khong lap: '" << c << "'" << endl;
            return 0;
        }
    }

    cout << "Moi ky tu deu lap lai!" << endl;
    return 0;
}
```

Ví dụ:

```
"leetcode"   -> 'l'
"loveleetcode" -> 'v'
"aabb"       -> Moi ky tu deu lap lai!
```

💡 **Mẫu "2 lượt duyệt" rất quan trọng:**
- **Lượt 1** duyệt để đếm (thứ tự không quan trọng)
- **Lượt 2** duyệt **theo thứ tự chuỗi gốc** để tìm cái đầu tiên thoả điều kiện

Nếu duyệt mảng `dem` thay vì chuỗi, bạn sẽ được ký tự nhỏ nhất theo bảng chữ cái, không phải ký tự **đầu tiên** trong chuỗi.

Độ phức tạp **O(n)** — tốt hơn hẳn cách so sánh mọi cặp O(n²).

### Bài 5.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    bool daGap[256] = {};

    for (unsigned char c : s) {
        if (daGap[c]) {
            cout << "Ky tu dau tien bi lap: '" << c << "'" << endl;
            return 0;
        }
        daGap[c] = true;
    }

    cout << "Khong co ky tu nao lap lai!" << endl;
    return 0;
}
```

💡 **Chỉ cần MỘT lượt duyệt** — khác với bài 4 phải 2 lượt. Vì "bị lặp" nghĩa là "đã gặp trước đó", ta biết ngay khi gặp lần thứ hai.

### Bài 6.

```cpp
#include <iostream>
#include <string>
#include <iomanip>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int dem[26] = {};
    for (unsigned char c : s)
        if (isalpha(c)) dem[tolower(c) - 'a']++;

    // Tim tan suat lon nhat de chuan hoa do dai cot
    int maxDem = 0;
    for (int i = 0; i < 26; i++) maxDem = max(maxDem, dem[i]);
    if (maxDem == 0) { cout << "Khong co chu cai nao!" << endl; return 0; }

    const int DO_RONG = 40;

    cout << "\nBIEU DO TAN SUAT" << endl;
    cout << string(DO_RONG + 12, '=') << endl;

    for (int i = 0; i < 26; i++) {
        if (dem[i] == 0) continue;

        int doDai = dem[i] * DO_RONG / maxDem;
        if (doDai == 0) doDai = 1;

        cout << " '" << (char)('a' + i) << "' | "
             << string(doDai, '*')
             << setw(DO_RONG - doDai + 4) << right << dem[i] << endl;
    }
    cout << string(DO_RONG + 12, '=') << endl;
    return 0;
}
```

Ví dụ với `"lap trinh c++ that thu vi"`:

```
BIEU DO TAN SUAT
====================================================
 'a' | ****************                           2
 'c' | ********                                   1
 'h' | ************************                   3
 'i' | ****************                           2
 'l' | ********                                   1
 'n' | ********                                   1
 'p' | ********                                   1
 'r' | ********                                   1
 't' | ****************************************   5
 'u' | ********                                   1
 'v' | ********                                   1
====================================================
```

💡 **Chuẩn hoá độ dài:** `doDai = dem[i] * DO_RONG / maxDem` — cột cao nhất luôn đúng `DO_RONG` ký tự, các cột khác tỉ lệ theo.

💡 `string(n, '*')` tạo chuỗi `n` dấu sao — gọn hơn vòng lặp.

### Bài 7.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool laDaoChu(const string& a, const string& b) {
    int dem[26] = {};

    for (unsigned char c : a) if (isalpha(c)) dem[tolower(c) - 'a']++;
    for (unsigned char c : b) if (isalpha(c)) dem[tolower(c) - 'a']--;

    for (int i = 0; i < 26; i++)
        if (dem[i] != 0) return false;

    return true;
}

int main() {
    struct { const char* a; const char* b; } bo[] = {
        {"listen",    "silent"},
        {"Dormitory", "Dirty Room"},
        {"hello",     "world"},
        {"Astronomer","Moon starer"},
        {"abc",       "abcd"}
    };

    cout << boolalpha;
    for (auto& t : bo) {
        cout << "\"" << t.a << "\" vs \"" << t.b << "\" -> "
             << (laDaoChu(t.a, t.b) ? "LA dao chu" : "khong") << endl;
    }
    return 0;
}
```

Output:

```
"listen" vs "silent" -> LA dao chu
"Dormitory" vs "Dirty Room" -> LA dao chu
"hello" vs "world" -> khong
"Astronomer" vs "Moon starer" -> LA dao chu
"abc" vs "abcd" -> khong
```

💡 **Kỹ thuật thanh lịch: một mảng, chuỗi đầu CỘNG, chuỗi sau TRỪ.** Nếu là đảo chữ thì mọi ô về 0.

Độ phức tạp **O(n)** — tốt hơn cách sắp xếp 2 chuỗi rồi so sánh (O(n log n)).

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    bool coMat[26] = {};
    int soChuKhacNhau = 0;

    for (unsigned char c : s) {
        if (isalpha(c)) {
            int i = tolower(c) - 'a';
            if (!coMat[i]) { coMat[i] = true; soChuKhacNhau++; }
        }
    }

    if (soChuKhacNhau == 26) {
        cout << "LA PANGRAM! (co du 26 chu cai)" << endl;
    } else {
        cout << "KHONG phai pangram (co " << soChuKhacNhau << "/26 chu)" << endl;
        cout << "Thieu cac chu: ";
        for (int i = 0; i < 26; i++)
            if (!coMat[i]) cout << (char)('a' + i) << " ";
        cout << endl;
    }
    return 0;
}
```

Thử với pangram tiếng Anh nổi tiếng:

```
Nhap chuoi: The quick brown fox jumps over the lazy dog
LA PANGRAM! (co du 26 chu cai)
```

💡 **Pangram** được dùng để kiểm tra font chữ, thử máy đánh chữ, và luyện gõ phím.

Một pangram ngắn khác: `"Pack my box with five dozen liquor jugs"`

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <cctype>
#include <algorithm>
using namespace std;

string chuanHoaTu(string t) {
    // Bo dau cau o dau va cuoi, chuyen ve chu thuong
    while (!t.empty() && !isalnum((unsigned char)t.front())) t.erase(t.begin());
    while (!t.empty() && !isalnum((unsigned char)t.back()))  t.pop_back();
    transform(t.begin(), t.end(), t.begin(),
              [](unsigned char c) { return tolower(c); });
    return t;
}

int main() {
    string vanBan;
    cout << "Nhap doan van: ";
    getline(cin, vanBan);

    map<string, int> dem;
    istringstream iss(vanBan);
    string tu;

    while (iss >> tu) {
        tu = chuanHoaTu(tu);
        if (!tu.empty()) dem[tu]++;
    }

    cout << "\nTan suat cac tu (theo thu tu bang chu cai):" << endl;
    for (const auto& [t, sl] : dem)
        cout << "  " << t << " : " << sl << endl;

    cout << "\nTong: " << dem.size() << " tu khac nhau" << endl;
    return 0;
}
```

Ví dụ:

```
Nhap doan van: Toi hoc C++. C++ rat hay, toi thich C++!

Tan suat cac tu (theo thu tu bang chu cai):
  c++ : 3
  hay : 1
  hoc : 1
  rat : 1
  thich : 1
  toi : 2
```

💡 **`map<string,int>` tự động sắp xếp theo khoá** và tự khởi tạo giá trị 0 khi truy cập khoá mới — nên `dem[tu]++` hoạt động ngay cả với từ chưa có.

⚠️ **Chuẩn hoá từ rất quan trọng:** không chuẩn hoá thì `"C++."`, `"C++"`, `"c++"` bị đếm là 3 từ khác nhau.

### Bài 10.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <cctype>
using namespace std;

string chuanHoaTu(string t) {
    while (!t.empty() && !isalnum((unsigned char)t.front())) t.erase(t.begin());
    while (!t.empty() && !isalnum((unsigned char)t.back()))  t.pop_back();
    transform(t.begin(), t.end(), t.begin(),
              [](unsigned char c) { return tolower(c); });
    return t;
}

int main() {
    string vanBan =
        "lap trinh C++ rat hay. Hoc lap trinh giup tu duy tot. "
        "C++ manh me, C++ nhanh. Lap trinh la ky nang quan trong. "
        "Hoc C++ de hoc cac ngon ngu khac.";

    map<string, int> dem;
    istringstream iss(vanBan);
    string tu;
    while (iss >> tu) {
        tu = chuanHoaTu(tu);
        if (!tu.empty()) dem[tu]++;
    }

    // Chuyen map sang vector de sap xep theo TAN SUAT
    vector<pair<string, int>> ds(dem.begin(), dem.end());

    sort(ds.begin(), ds.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second) return a.second > b.second;   // tan suat GIAM dan
        return a.first < b.first;                                // bang nhau -> A-Z
    });

    cout << "TOP 5 TU XUAT HIEN NHIEU NHAT:" << endl;
    cout << "+------+----------------+---------+" << endl;
    cout << "| HANG | TU             | SO LAN  |" << endl;
    cout << "+------+----------------+---------+" << endl;

    for (size_t i = 0; i < ds.size() && i < 5; i++) {
        cout << "| " << left  << setw(4) << i + 1
             << " | " << setw(14) << ds[i].first
             << " | " << right << setw(7) << ds[i].second << " |" << endl;
    }
    cout << "+------+----------------+---------+" << endl;
    return 0;
}
```

Nhớ `#include <iomanip>` cho `setw`.

Output:

```
TOP 5 TU XUAT HIEN NHIEU NHAT:
+------+----------------+---------+
| HANG | TU             | SO LAN  |
+------+----------------+---------+
| 1    | c++            |       4 |
| 2    | hoc            |       3 |
| 3    | lap            |       3 |
| 4    | trinh          |       3 |
| 5    | cac            |       1 |
+------+----------------+---------+
```

💡 **Mẫu "map → vector → sort"** rất thường dùng: `map` tiện để đếm, nhưng muốn sắp xếp theo **giá trị** (không phải khoá) thì phải đổ sang `vector` rồi `sort`.

### Bài 11.

```cpp
#include <iostream>
#include <string>
using namespace std;

string xoaLap(const string& s) {
    bool daGap[256] = {};
    string kq;

    for (unsigned char c : s) {
        if (!daGap[c]) {
            daGap[c] = true;
            kq += c;
        }
    }
    return kq;
}

int main() {
    string ds[] = {"programming", "aabbcc", "hello world", "abcdef"};

    for (const string& s : ds) {
        cout << "\"" << s << "\" -> \"" << xoaLap(s) << "\"" << endl;
    }
    return 0;
}
```

Output:

```
"programming" -> "progamin"
"aabbcc" -> "abc"
"hello world" -> "helo wrd"
"abcdef" -> "abcdef"
```

Độ phức tạp **O(n)** thời gian, **O(1)** bộ nhớ phụ (mảng 256 phần tử cố định).

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

bool coTheThanhDoiXung(const string& s) {
    int dem[256] = {};
    for (unsigned char c : s)
        if (isalnum(c)) dem[tolower(c)]++;

    int soLe = 0;
    for (int i = 0; i < 256; i++)
        if (dem[i] % 2 == 1) soLe++;

    return soLe <= 1;                   // toi da MOT ky tu co tan suat le
}

int main() {
    string ds[] = {"aabb", "abcba", "abc", "racecar", "aabbc", "aabbcc"};

    cout << boolalpha;
    for (const string& s : ds) {
        cout << "\"" << s << "\" -> "
             << (coTheThanhDoiXung(s) ? "CO the" : "khong the")
             << " sap xep thanh doi xung" << endl;
    }
    return 0;
}
```

Output:

```
"aabb" -> CO the sap xep thanh doi xung      (abba)
"abcba" -> CO the sap xep thanh doi xung     (da doi xung)
"abc" -> khong the
"racecar" -> CO the sap xep thanh doi xung
"aabbc" -> CO the sap xep thanh doi xung     (abcba)
"aabbcc" -> CO the sap xep thanh doi xung    (abccba)
```

**Chứng minh điều kiện:**

Trong một chuỗi đối xứng, mỗi ký tự ở vị trí `i` phải khớp với ký tự ở vị trí `n-1-i`. Nên:
- Với chuỗi **độ dài chẵn**: mọi ký tự phải xuất hiện **số lần chẵn**
- Với chuỗi **độ dài lẻ**: đúng **một** ký tự được phép xuất hiện số lần lẻ (nó nằm ở giữa)

→ Điều kiện: **số ký tự có tần suất lẻ ≤ 1**.

### Bài 13.

```cpp
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);

    int lanCuoi[256];
    fill(lanCuoi, lanCuoi + 256, -1);        // -1 = chua gap

    int doDaiMax = 0, batDauMax = 0;
    int trai = 0;

    for (int phai = 0; phai < (int)s.length(); phai++) {
        unsigned char c = s[phai];

        // Neu ky tu nay da xuat hien TRONG cua so hien tai -> day bien trai
        if (lanCuoi[c] >= trai) {
            trai = lanCuoi[c] + 1;
        }

        lanCuoi[c] = phai;

        int doDai = phai - trai + 1;
        if (doDai > doDaiMax) {
            doDaiMax  = doDai;
            batDauMax = trai;
        }
    }

    cout << "Chuoi con dai nhat khong lap: \""
         << s.substr(batDauMax, doDaiMax) << "\"" << endl;
    cout << "Do dai: " << doDaiMax << endl;
    return 0;
}
```

Ví dụ:

```
"abcabcbb"  -> "abc"  (do dai 3)
"bbbbb"     -> "b"    (do dai 1)
"pwwkew"    -> "wke"  (do dai 3)
"codelab"   -> "codelab" (do dai 7)
```

**Kỹ thuật cửa sổ trượt (sliding window):**
- `trai`, `phai` là 2 biên của cửa sổ đang xét
- Mở rộng `phai` mỗi bước
- Khi gặp ký tự đã có **trong cửa sổ**, đẩy `trai` qua vị trí cũ của nó

**Độ phức tạp O(n)** — mỗi ký tự chỉ được xét đúng một lần. So với cách vét cạn mọi chuỗi con là O(n³).

⚠️ Điều kiện `lanCuoi[c] >= trai` rất quan trọng — nó phân biệt "ký tự đã gặp **trong cửa sổ**" với "đã gặp nhưng **ngoài** cửa sổ".

### Bài 14.

```cpp
#include <iostream>
#include <string>
using namespace std;

string nenRLE(const string& s) {
    if (s.empty()) return "";

    string kq;
    size_t i = 0;

    while (i < s.length()) {
        char c = s[i];
        int dem = 0;
        while (i < s.length() && s[i] == c) { dem++; i++; }

        kq += c;
        kq += to_string(dem);
    }
    return kq;
}

string giaiNenRLE(const string& s) {
    string kq;
    size_t i = 0;

    while (i < s.length()) {
        char c = s[i++];
        string soStr;
        while (i < s.length() && isdigit((unsigned char)s[i])) soStr += s[i++];

        int dem = soStr.empty() ? 1 : stoi(soStr);
        kq += string(dem, c);
    }
    return kq;
}

int main() {
    string ds[] = {"aaabbc", "aabcccccaaa", "abcdef", "aaaaaaaaaaaa"};

    cout << "+----------------+----------------+-----------+" << endl;
    cout << "| GOC            | NEN            | TI LE     |" << endl;
    cout << "+----------------+----------------+-----------+" << endl;

    for (const string& s : ds) {
        string nen = nenRLE(s);
        double tiLe = 100.0 * nen.length() / s.length();

        cout << "| " << s;
        for (size_t k = s.length(); k < 14; k++) cout << " ";
        cout << " | " << nen;
        for (size_t k = nen.length(); k < 14; k++) cout << " ";
        cout << " | " << (tiLe <= 100 ? "" : "+") << (int)tiLe << "%";
        for (int k = 0; k < 6; k++) cout << " ";
        cout << "|" << endl;

        // Kiem tra giai nen dung
        if (giaiNenRLE(nen) != s) cout << "  !!! GIAI NEN SAI" << endl;
    }
    cout << "+----------------+----------------+-----------+" << endl;
    return 0;
}
```

Output:

```
+----------------+----------------+-----------+
| GOC            | NEN            | TI LE     |
+----------------+----------------+-----------+
| aaabbc         | a3b2c1         | 100%      |
| aabcccccaaa    | a2b1c5a3       | 72%       |
| abcdef         | a1b1c1d1e1f1   | 200%      |
| aaaaaaaaaaaa   | a12            | 25%       |
+----------------+----------------+-----------+
```

⚠️ **RLE chỉ hiệu quả khi dữ liệu có nhiều đoạn lặp.** Với chuỗi không lặp (`"abcdef"`), nó **phình to gấp đôi**.

💡 **Cải tiến thực tế:** chỉ nén khi `dem > 1`, và so sánh kích thước rồi chọn bản nhỏ hơn:

```cpp
string nenThongMinh(const string& s) {
    string nen = nenRLE(s);
    return (nen.length() < s.length()) ? nen : s;
}
```

RLE được dùng trong định dạng ảnh BMP, fax, và là bước tiền xử lý trong nhiều thuật toán nén khác.

### Bài 15.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cctype>
using namespace std;

string chuanHoaTu(string t) {
    while (!t.empty() && !isalnum((unsigned char)t.front())) t.erase(t.begin());
    while (!t.empty() && !isalnum((unsigned char)t.back()))  t.pop_back();
    transform(t.begin(), t.end(), t.begin(),
              [](unsigned char c) { return tolower(c); });
    return t;
}

int main() {
    cout << "Nhap van ban (dong trong de ket thuc):" << endl;

    string vanBan, dong;
    int soDong = 0;
    while (getline(cin, dong) && !dong.empty()) {
        vanBan += dong + " ";
        soDong++;
    }

    if (vanBan.empty()) { cout << "Khong co du lieu!" << endl; return 1; }

    // ===== THONG KE KY TU =====
    int demChu[26] = {};
    int tongKyTu = 0, chuCai = 0, chuSo = 0, khoangTrang = 0, dacBiet = 0;

    for (unsigned char c : vanBan) {
        tongKyTu++;
        if      (isalpha(c)) { chuCai++; demChu[tolower(c) - 'a']++; }
        else if (isdigit(c)) chuSo++;
        else if (isspace(c)) khoangTrang++;
        else                 dacBiet++;
    }

    // ===== THONG KE TU =====
    map<string, int> demTu;
    string tuDaiNhat;
    int soTu = 0;
    long long tongDoDaiTu = 0;

    istringstream iss(vanBan);
    string t;
    while (iss >> t) {
        string tu = chuanHoaTu(t);
        if (tu.empty()) continue;

        soTu++;
        demTu[tu]++;
        tongDoDaiTu += tu.length();
        if (tu.length() > tuDaiNhat.length()) tuDaiNhat = tu;
    }

    // ===== IN BAO CAO =====
    cout << "\n" << string(50, '=') << endl;
    cout << "           BAO CAO PHAN TICH VAN BAN" << endl;
    cout << string(50, '=') << endl;

    cout << fixed << setprecision(2);
    cout << "\n--- THONG KE CHUNG ---" << endl;
    cout << left << setw(28) << "So dong"            << ": " << soDong      << endl;
    cout << left << setw(28) << "Tong ky tu"         << ": " << tongKyTu    << endl;
    cout << left << setw(28) << "  Chu cai"          << ": " << chuCai      << endl;
    cout << left << setw(28) << "  Chu so"           << ": " << chuSo       << endl;
    cout << left << setw(28) << "  Khoang trang"     << ": " << khoangTrang << endl;
    cout << left << setw(28) << "  Ky tu dac biet"   << ": " << dacBiet     << endl;
    cout << left << setw(28) << "So tu"              << ": " << soTu        << endl;
    cout << left << setw(28) << "So tu khac nhau"    << ": " << demTu.size() << endl;
    if (soTu > 0)
        cout << left << setw(28) << "Do dai tu trung binh" << ": "
             << (double)tongDoDaiTu / soTu << " ky tu" << endl;
    cout << left << setw(28) << "Tu dai nhat"        << ": " << tuDaiNhat
         << " (" << tuDaiNhat.length() << " ky tu)" << endl;

    // ===== TOP 5 TU =====
    vector<pair<string,int>> dsTu(demTu.begin(), demTu.end());
    sort(dsTu.begin(), dsTu.end(), [](const auto& a, const auto& b) {
        if (a.second != b.second) return a.second > b.second;
        return a.first < b.first;
    });

    cout << "\n--- TOP 5 TU PHO BIEN NHAT ---" << endl;
    for (size_t i = 0; i < dsTu.size() && i < 5; i++)
        cout << "  " << i + 1 << ". " << left << setw(20) << dsTu[i].first
             << " : " << dsTu[i].second << " lan" << endl;

    // ===== TOP 5 CHU CAI =====
    vector<pair<char,int>> dsChu;
    for (int i = 0; i < 26; i++)
        if (demChu[i] > 0) dsChu.push_back({(char)('a' + i), demChu[i]});
    sort(dsChu.begin(), dsChu.end(), [](const auto& a, const auto& b) {
        return a.second > b.second;
    });

    cout << "\n--- TOP 5 CHU CAI PHO BIEN NHAT ---" << endl;
    int maxChu = dsChu.empty() ? 1 : dsChu[0].second;
    for (size_t i = 0; i < dsChu.size() && i < 5; i++) {
        int doDai = dsChu[i].second * 30 / maxChu;
        cout << "  '" << dsChu[i].first << "' " << string(max(1, doDai), '*')
             << " " << dsChu[i].second << endl;
    }

    cout << "\n" << string(50, '=') << endl;
    return 0;
}
```

Ví dụ output:

```
==================================================
           BAO CAO PHAN TICH VAN BAN
==================================================

--- THONG KE CHUNG ---
So dong                     : 3
Tong ky tu                  : 142
  Chu cai                   : 110
  Chu so                    : 3
  Khoang trang              : 25
  Ky tu dac biet            : 4
So tu                       : 25
So tu khac nhau             : 19
Do dai tu trung binh        : 4.40 ky tu
Tu dai nhat                 : programming (11 ky tu)

--- TOP 5 TU PHO BIEN NHAT ---
  1. lap                  : 3 lan
  2. trinh                : 3 lan
  ...

--- TOP 5 CHU CAI PHO BIEN NHAT ---
  'n' ****************************** 14
  'a' ************************ 11
  ...
```
