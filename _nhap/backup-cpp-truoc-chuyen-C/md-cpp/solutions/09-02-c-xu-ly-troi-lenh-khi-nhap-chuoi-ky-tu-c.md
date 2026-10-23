# Lời giải — [C++]. Xử Lý Trôi Lệnh Khi Nhập Chuỗi Ký Tự C++

[← Quay lại bài học](../09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi-ky-tu-c.md)

> **Nguyên nhân gốc rễ:** `cin >> x` đọc giá trị nhưng **để lại ký tự Enter (`'\n'`)** trong bộ đệm. `getline` gặp ngay ký tự đó và kết thúc → trả về chuỗi rỗng.

---

### Bài 1.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int n;
    string s;

    cout << "Nhap so: ";
    cin >> n;

    cout << "Nhap chuoi: ";
    getline(cin, s);

    cout << "n = " << n << ", s = [" << s << "]" << endl;
    return 0;
}
```

**Hiện tượng:** chương trình **không dừng lại** để bạn nhập chuỗi. Nó in ngay:

```
Nhap so: 25
Nhap chuoi: n = 25, s = []
```

**Giải thích chi tiết — theo dõi bộ đệm bàn phím:**

```
Ban go: 2 5 Enter
Bo dem chua:  '2' '5' '\n'

cin >> n:
   - Doc '2', '5' -> n = 25
   - GAP '\n' -> DUNG, nhung KHONG LAY '\n' ra khoi bo dem
   Bo dem con lai:  '\n'

getline(cin, s):
   - Doc tu bo dem, GAP NGAY '\n' o ky tu dau tien
   - Ket luan: "day la dong rong" -> s = "" va lay '\n' ra
   Bo dem: (rong)
```

**Bản chất:** `cin >>` **bỏ qua khoảng trắng ở đầu** nhưng **không xoá khoảng trắng phía sau**. `getline` thì ngược lại — nó đọc mọi thứ tới `'\n'` đầu tiên.

### Bài 2.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main() {
    int n;
    string s;

    cout << "Nhap so: ";
    cin >> n;

    cin.ignore(numeric_limits<streamsize>::max(), '\n');   // XOA phan con lai cua dong

    cout << "Nhap chuoi: ";
    getline(cin, s);

    cout << "n = " << n << ", s = [" << s << "]" << endl;
    return 0;
}
```

Kết quả:

```
Nhap so: 25
Nhap chuoi: codelab dev
n = 25, s = [codelab dev]
```

Cần `#include <limits>` cho `numeric_limits`.

### Bài 3.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main() {
    int tuoi;
    string hoTen;

    cout << "Nhap tuoi: ";
    cin >> tuoi;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    cout << "Nhap ho ten day du: ";
    getline(cin, hoTen);

    cout << "\n--- THONG TIN ---" << endl;
    cout << "Ho ten: " << hoTen << endl;
    cout << "Tuoi  : " << tuoi << endl;
    return 0;
}
```

✅ **Quy tắc vàng: sau MỌI `cin >>` mà tiếp theo là `getline`, phải có `cin.ignore(...)`.**

### Bài 4.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <limits>
using namespace std;

int main() {
    int n;
    cout << "Nhap so nguoi: ";
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');    // <- BAT BUOC

    vector<string> ds(n);
    for (int i = 0; i < n; i++) {
        cout << "  Ho ten nguoi " << i + 1 << ": ";
        getline(cin, ds[i]);
    }

    cout << "\n--- DANH SACH ---" << endl;
    for (int i = 0; i < n; i++) {
        cout << i + 1 << ". " << ds[i] << endl;
    }
    return 0;
}
```

⚠️ Chỉ cần **một** lần `ignore` sau `cin >> n`. Các `getline` sau đó không cần thêm gì, vì `getline` **có lấy** ký tự `'\n'` ra khỏi bộ đệm.

### Bài 5.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main() {
    int n;
    string s;

    cin >> n;

    // ① cin.ignore()  -> chi bo 1 ky tu
    // cin.ignore();

    // ② cin.ignore(1000, '\n')  -> bo toi da 1000 ky tu hoac den khi gap '\n'
    // cin.ignore(1000, '\n');

    // ③ AN TOAN NHAT
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    getline(cin, s);
    cout << "n = " << n << ", s = [" << s << "]" << endl;
    return 0;
}
```

**So sánh:**

| Cách | Bỏ qua | Rủi ro |
|---|---|---|
| `cin.ignore()` | **Đúng 1 ký tự** | ⚠️ Hỏng nếu người dùng gõ `25 abc` rồi Enter — chỉ bỏ dấu cách, còn `abc` |
| `cin.ignore(1000, '\n')` | Tối đa 1000 ký tự, hoặc tới `'\n'` | ⚠️ Hỏng nếu dòng dài hơn 1000 ký tự |
| `cin.ignore(numeric_limits<streamsize>::max(), '\n')` | **Toàn bộ dòng, không giới hạn** | ✅ An toàn tuyệt đối |

**Thử nghiệm với input `25 rac rac rac`:**

```
cin >> n            -> n = 25, bo dem: " rac rac rac\n"
cin.ignore()        -> bo 1 ky tu (dau cach), bo dem: "rac rac rac\n"
getline(cin, s)     -> s = "rac rac rac"    <- SAI, khong phai cai ta muon
```

Với cách ③, toàn bộ phần rác bị xoá sạch.

✅ **Luôn dùng cách ③.** Có thể định nghĩa macro cho gọn:

```cpp
#define XOA_DEM cin.ignore(numeric_limits<streamsize>::max(), '\n')
```

### Bài 6.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

void xoaDem() {
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

int main() {
    int maSV;
    string hoTen;
    double diem;
    string ghiChu;

    cout << "Ma sinh vien : ";  cin >> maSV;   xoaDem();
    cout << "Ho ten       : ";  getline(cin, hoTen);
    cout << "Diem trung binh: "; cin >> diem;  xoaDem();
    cout << "Ghi chu      : ";  getline(cin, ghiChu);

    cout << "\n--- KET QUA ---" << endl;
    cout << "Ma SV  : " << maSV   << endl;
    cout << "Ho ten : " << hoTen  << endl;
    cout << "Diem   : " << diem   << endl;
    cout << "Ghi chu: " << ghiChu << endl;
    return 0;
}
```

💡 **Tách hàm `xoaDem()`** làm code sạch hơn nhiều so với viết lại dòng dài đó mỗi lần.

**Quy tắc đặt `xoaDem()`:** ngay sau **mọi** `cin >>`, nếu sau đó còn `getline`.

### Bài 7.

```cpp
string s1, s2;
getline(cin, s1);
cin.ignore();        // <- THUA! Day la nguyen nhan loi
getline(cin, s2);
```

**Lỗi:** `cin.ignore()` ở đây là **thừa** và gây hại.

**Vì sao:** `getline` **đã lấy** ký tự `'\n'` ra khỏi bộ đệm rồi (nó chỉ không đưa ký tự đó vào chuỗi kết quả). Nên sau `getline(cin, s1)`, bộ đệm đã sạch.

`cin.ignore()` tiếp theo sẽ **nuốt mất ký tự đầu tiên** của dòng thứ hai:

```
Ban go:
  dong mot
  dong hai

getline(cin, s1)  -> s1 = "dong mot", bo dem sach
cin.ignore()      -> CHO nguoi dung nhap, roi nuot ky tu 'd' dau tien
getline(cin, s2)  -> s2 = "ong hai"    <- MAT chu 'd'!
```

**Sửa:** bỏ dòng `cin.ignore()`.

```cpp
string s1, s2;
getline(cin, s1);
getline(cin, s2);     // khong can gi them
```

✅ **Quy tắc rõ ràng:**

| Tình huống | Cần `ignore`? |
|---|---|
| `cin >>` rồi `getline` | ✅ **CÓ** |
| `getline` rồi `getline` | ❌ Không |
| `cin >>` rồi `cin >>` | ❌ Không |
| `getline` rồi `cin >>` | ❌ Không |

### Bài 8.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

int nhapSo(const string& loiNhac) {
    int n;
    while (true) {
        cout << loiNhac;

        if (cin >> n) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return n;
        }

        // Nhap sai -> khoi phuc trang thai va xoa du lieu rac
        cin.clear();                                              // xoa co loi
        cin.ignore(numeric_limits<streamsize>::max(), '\n');      // xoa du lieu rac
        cout << "  -> Khong hop le! Vui long nhap mot SO NGUYEN." << endl;
    }
}

int main() {
    int tuoi = nhapSo("Nhap tuoi: ");
    int nam  = nhapSo("Nhap nam sinh: ");

    cout << "\nTuoi: " << tuoi << ", Nam sinh: " << nam << endl;
    return 0;
}
```

Ví dụ chạy:

```
Nhap tuoi: abc
  -> Khong hop le! Vui long nhap mot SO NGUYEN.
Nhap tuoi: 12.5
  -> (nhan 12, phan .5 bi xoa)
Nhap tuoi: 25
Nhap nam sinh: 2001
```

**2 bước bắt buộc khi `cin` bị lỗi:**
1. **`cin.clear()`** — xoá cờ lỗi, đưa `cin` về trạng thái dùng được
2. **`cin.ignore(...)`** — xoá dữ liệu rác còn trong bộ đệm

⚠️ Thiếu bước 1: mọi lệnh đọc sau đó đều thất bại → **vòng lặp vô hạn**.
⚠️ Thiếu bước 2: dữ liệu rác vẫn còn → lại lỗi ngay → **vòng lặp vô hạn**.

### Bài 9.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

string nhapChuoi(const string& loiNhac, bool choPhepRong = false) {
    string s;
    while (true) {
        cout << loiNhac;
        getline(cin, s);

        if (!s.empty() || choPhepRong) return s;
        cout << "  -> Khong duoc de trong!" << endl;
    }
}

int nhapSo(const string& loiNhac) {
    int n;
    while (true) {
        cout << loiNhac;
        if (cin >> n) {
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            return n;
        }
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "  -> Phai nhap so!" << endl;
    }
}

int main() {
    int tuoi     = nhapSo("Nhap tuoi: ");
    string hoTen = nhapChuoi("Nhap ho ten: ");
    string diaChi = nhapChuoi("Nhap dia chi (co the bo trong): ", true);

    cout << "\n--- KET QUA ---" << endl;
    cout << "Ho ten : " << hoTen << endl;
    cout << "Tuoi   : " << tuoi << endl;
    cout << "Dia chi: " << (diaChi.empty() ? "(khong co)" : diaChi) << endl;
    return 0;
}
```

💡 Nhờ `nhapSo` đã tự gọi `ignore` bên trong, hàm `nhapChuoi` không cần lo về trôi lệnh nữa.

### Bài 10.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

int main() {
    char luaChon;
    string noiDung;

    cout << "Chon chuc nang (a/b/c): ";
    cin >> luaChon;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');      // <- BAT BUOC

    cout << "Nhap noi dung: ";
    getline(cin, noiDung);

    cout << "\nLua chon : " << luaChon << endl;
    cout << "Noi dung : " << noiDung << endl;
    return 0;
}
```

⚠️ **`cin >> c` với `char` cũng để lại `'\n'`** giống như với số. Quy tắc giống hệt nhau.

### Bài 11.

```cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    // ===== cin.get() : doc MOT ky tu, KE CA khoang trang =====
    cout << "--- cin.get() ---" << endl;
    cout << "Nhap 3 ky tu (ke ca dau cach): ";
    char a = cin.get();
    char b = cin.get();
    char c = cin.get();
    cout << "Da doc: [" << a << "][" << b << "][" << c << "]" << endl;
    cin.ignore(10000, '\n');

    // ===== cin.peek() : XEM ky tu ke tiep ma KHONG lay ra =====
    cout << "\n--- cin.peek() ---" << endl;
    cout << "Nhap mot so hoac mot chu: ";
    char tiep = cin.peek();                // chi NHIN, khong lay
    if (isdigit((unsigned char)tiep)) {
        int n;
        cin >> n;
        cout << "Da doc mot SO: " << n << endl;
    } else {
        string s;
        cin >> s;
        cout << "Da doc mot CHUOI: " << s << endl;
    }
    cin.ignore(10000, '\n');

    // ===== cin.putback() : TRA LAI ky tu vao bo dem =====
    cout << "\n--- cin.putback() ---" << endl;
    cout << "Nhap mot tu: ";
    char d = cin.get();
    cout << "Ky tu dau: " << d << endl;
    cin.putback(d);                         // TRA LAI
    string tu;
    cin >> tu;
    cout << "Ca tu (ky tu dau van con): " << tu << endl;

    return 0;
}
```

**Bảng tổng hợp:**

| Hàm | Tác dụng | Có lấy ký tự ra không? |
|---|---|---|
| `cin.get()` | Đọc 1 ký tự, **kể cả khoảng trắng** | ✅ Có |
| `cin.get(c)` | Đọc 1 ký tự vào biến `c` | ✅ Có |
| `cin.peek()` | **Xem** ký tự kế tiếp | ❌ Không |
| `cin.putback(c)` | **Trả lại** ký tự vào bộ đệm | Ngược lại |
| `cin.unget()` | Trả lại ký tự vừa đọc | Ngược lại |
| `cin.ignore(n, c)` | Bỏ qua `n` ký tự hoặc tới khi gặp `c` | ✅ Có |

💡 **`peek()` rất hữu ích** khi cần quyết định đọc kiểu gì mà chưa biết trước dữ liệu là số hay chữ.

### Bài 12.

```cpp
#include <iostream>
#include <string>
#include <limits>
using namespace std;

void inTrangThai() {
    cout << "  good = " << cin.good()
         << ", fail = " << cin.fail()
         << ", eof = "  << cin.eof()
         << ", bad = "  << cin.bad() << endl;
}

int main() {
    int n;

    cout << "Nhap mot SO (thu nhap chu de xem loi): ";
    cin >> n;

    cout << "Trang thai sau khi doc:" << endl;
    inTrangThai();

    if (cin.fail()) {
        cout << "  -> cin bi LOI (failbit bat)" << endl;

        cin.clear();                                              // ① XOA co loi
        cout << "  Sau cin.clear():" << endl;
        inTrangThai();

        cin.ignore(numeric_limits<streamsize>::max(), '\n');      // ② XOA du lieu rac

        cout << "\nNhap lai (lan nay nhap so): ";
        cin >> n;
        cout << "Da doc: " << n << endl;
    } else {
        cout << "  -> Doc thanh cong: " << n << endl;
    }
    return 0;
}
```

**Các cờ trạng thái của `cin`:**

| Cờ | Ý nghĩa | Khi nào bật |
|---|---|---|
| `goodbit` | Mọi thứ bình thường | Mặc định |
| **`failbit`** | Thao tác đọc **thất bại** | Nhập chữ khi cần số; định dạng sai |
| `eofbit` | Đã đến **cuối dữ liệu** | Bấm `Ctrl+D`/`Ctrl+Z`, hoặc hết file |
| `badbit` | Lỗi **nghiêm trọng** ở luồng | Hỏng thiết bị, lỗi bộ nhớ |

**Kiểm tra:**

```cpp
cin.good()   // khong co co loi nao
cin.fail()   // failbit HOAC badbit bat
cin.eof()    // eofbit bat
cin.bad()    // badbit bat
if (cin >> n) { ... }        // tuong duong !cin.fail()
```

⚠️ **Khi `failbit` bật, MỌI thao tác đọc sau đó đều thất bại ngay lập tức** cho tới khi gọi `cin.clear()`. Đây là nguyên nhân của vòng lặp vô hạn kinh điển:

```cpp
int n;
while (true) {
    cout << "Nhap so: ";
    cin >> n;               // that bai, failbit bat
    if (n > 0) break;
    // THIEU cin.clear() -> lan sau cung that bai -> LAP VO HAN, in lien tuc
}
```

### Bài 13.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <limits>
using namespace std;

void xoaDem() {
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

int nhapSo(const string& nhac, int min = INT_MIN, int max = INT_MAX) {
    int n;
    while (true) {
        cout << nhac;
        if (cin >> n) {
            xoaDem();
            if (n >= min && n <= max) return n;
            cout << "  -> Phai trong khoang [" << min << ", " << max << "]" << endl;
        } else {
            cin.clear();
            xoaDem();
            cout << "  -> Phai nhap SO!" << endl;
        }
    }
}

string nhapChuoi(const string& nhac) {
    string s;
    while (true) {
        cout << nhac;
        getline(cin, s);
        if (!s.empty()) return s;
        cout << "  -> Khong duoc de trong!" << endl;
    }
}

struct SinhVien { string ten; int tuoi; double diem; };

int main() {
    vector<SinhVien> ds;
    int chon;

    do {
        cout << "\n====== QUAN LY SINH VIEN ======" << endl;
        cout << "1. Them sinh vien"                 << endl;
        cout << "2. Hien thi danh sach"             << endl;
        cout << "3. Tim theo ten"                   << endl;
        cout << "0. Thoat"                          << endl;
        cout << "===============================" << endl;

        chon = nhapSo("Lua chon: ", 0, 3);

        switch (chon) {
            case 1: {
                SinhVien sv;
                sv.ten  = nhapChuoi("  Ho ten: ");
                sv.tuoi = nhapSo("  Tuoi: ", 1, 150);
                cout << "  Diem TB: ";
                while (!(cin >> sv.diem) || sv.diem < 0 || sv.diem > 10) {
                    cin.clear(); xoaDem();
                    cout << "  -> Diem phai tu 0 den 10: ";
                }
                xoaDem();
                ds.push_back(sv);
                cout << ">> Da them!" << endl;
                break;
            }
            case 2:
                if (ds.empty()) { cout << ">> Danh sach rong!" << endl; break; }
                cout << "\n--- DANH SACH ---" << endl;
                for (size_t i = 0; i < ds.size(); i++)
                    cout << i+1 << ". " << ds[i].ten
                         << " - " << ds[i].tuoi << " tuoi - "
                         << ds[i].diem << " diem" << endl;
                break;
            case 3: {
                string canTim = nhapChuoi("  Nhap ten can tim: ");
                bool thay = false;
                for (const auto& sv : ds)
                    if (sv.ten == canTim) {
                        cout << ">> Tim thay: " << sv.ten << " - "
                             << sv.tuoi << " tuoi - " << sv.diem << endl;
                        thay = true;
                    }
                if (!thay) cout << ">> Khong tim thay!" << endl;
                break;
            }
            case 0:
                cout << ">> Tam biet!" << endl;
                break;
        }
    } while (chon != 0);

    return 0;
}
```

💡 Nhờ dùng các hàm `nhapSo`/`nhapChuoi` đã xử lý sẵn, chương trình **không bao giờ** bị trôi lệnh hay lặp vô hạn, dù người dùng nhập gì.

Nhớ `#include <climits>` cho `INT_MIN`/`INT_MAX`.

### Bài 14.

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
using namespace std;

int main() {
    string dong;
    int n;

    // ===== CACH 1: getline + stoi =====
    cout << "Nhap mot so: ";
    getline(cin, dong);

    try {
        n = stoi(dong);
        cout << "Da doc: " << n << endl;
    } catch (const invalid_argument&) {
        cout << "Loi: khong phai so!" << endl;
    } catch (const out_of_range&) {
        cout << "Loi: so qua lon!" << endl;
    }

    // ===== Doc chuoi tiep theo - KHONG CAN ignore =====
    string s;
    cout << "Nhap chuoi: ";
    getline(cin, s);
    cout << "Chuoi: [" << s << "]" << endl;

    return 0;
}
```

**So sánh 2 cách tiếp cận:**

| | `cin >> n` + `ignore` | `getline` + `stoi` |
|---|---|---|
| Trôi lệnh | ⚠️ Phải nhớ `ignore` mỗi lần | ✅ **Không bao giờ xảy ra** |
| Xử lý lỗi | `cin.clear()` + `cin.ignore()` | `try/catch` |
| Nhập `12abc` | Nhận **12**, để lại `abc` | ❌ `stoi` nhận 12, nhưng có thể kiểm tra thêm |
| Nhập `abc` | `failbit` bật | Ném `invalid_argument` |
| Nhất quán | Trộn 2 kiểu đọc | ✅ Luôn dùng `getline` |
| Dễ hiểu với người mới | Trung bình | ✅ Rõ ràng hơn |

✅ **Cách 2 (`getline` + `stoi`) được nhiều người khuyến nghị** vì nó giải quyết triệt để vấn đề: **mọi lệnh đọc đều là `getline`**, nên không có khái niệm "trôi lệnh" nữa.

**Kiểm tra chặt chẽ hơn với `stoi`:**

```cpp
size_t viTri;
int n = stoi(dong, &viTri);
if (viTri != dong.length()) cout << "Co ky tu thua sau so!" << endl;
```

### Bài 15.

**File `nhaplieu.h`:**

```cpp
#pragma once
#include <string>

/** @brief Xoa sach bo dem ban phim den het dong hien tai. */
void xoaBoDem();

/**
 * @brief Nhap so nguyen an toan, bat nhap lai neu sai.
 * @param nhac Loi nhac hien thi.
 * @param min,max Khoang gia tri hop le.
 */
int nhapSoNguyen(const std::string& nhac,
                 int min = -2147483647, int max = 2147483647);

/** @brief Nhap so thuc an toan trong khoang [min, max]. */
double nhapSoThuc(const std::string& nhac,
                  double min = -1e18, double max = 1e18);

/**
 * @brief Nhap mot dong van ban.
 * @param choPhepRong Neu false, bat nhap lai khi de trong.
 */
std::string nhapChuoi(const std::string& nhac, bool choPhepRong = false);

/**
 * @brief Nhap mot ky tu thuoc tap hop cho phep.
 * @param hopLe Chuoi chua cac ky tu duoc chap nhan. Rong = chap nhan moi ky tu.
 */
char nhapKyTu(const std::string& nhac, const std::string& hopLe = "");

/** @brief Hoi Co/Khong, tra ve true neu nguoi dung chon y/Y. */
bool nhapCoKhong(const std::string& nhac);
```

**File `nhaplieu.cpp`:**

```cpp
#include "nhaplieu.h"
#include <iostream>
#include <limits>
#include <cctype>
using namespace std;

void xoaBoDem() {
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

int nhapSoNguyen(const string& nhac, int min, int max) {
    int n;
    while (true) {
        cout << nhac;
        if (cin >> n) {
            xoaBoDem();
            if (n >= min && n <= max) return n;
            cout << "  -> Gia tri phai trong khoang ["
                 << min << ", " << max << "]" << endl;
        } else {
            cin.clear();
            xoaBoDem();
            cout << "  -> Vui long nhap mot SO NGUYEN!" << endl;
        }
    }
}

double nhapSoThuc(const string& nhac, double min, double max) {
    double x;
    while (true) {
        cout << nhac;
        if (cin >> x) {
            xoaBoDem();
            if (x >= min && x <= max) return x;
            cout << "  -> Gia tri phai trong khoang ["
                 << min << ", " << max << "]" << endl;
        } else {
            cin.clear();
            xoaBoDem();
            cout << "  -> Vui long nhap mot SO!" << endl;
        }
    }
}

string nhapChuoi(const string& nhac, bool choPhepRong) {
    string s;
    while (true) {
        cout << nhac;
        getline(cin, s);
        if (!s.empty() || choPhepRong) return s;
        cout << "  -> Khong duoc de trong!" << endl;
    }
}

char nhapKyTu(const string& nhac, const string& hopLe) {
    char c;
    while (true) {
        cout << nhac;
        if (cin >> c) {
            xoaBoDem();
            if (hopLe.empty() || hopLe.find(c) != string::npos) return c;
            cout << "  -> Chi chap nhan cac ky tu: " << hopLe << endl;
        } else {
            cin.clear();
            xoaBoDem();
            cout << "  -> Nhap khong hop le!" << endl;
        }
    }
}

bool nhapCoKhong(const string& nhac) {
    char c = nhapKyTu(nhac + " (y/n): ", "yYnN");
    return (c == 'y' || c == 'Y');
}
```

**File `main.cpp` — kiểm thử:**

```cpp
#include <iostream>
#include <iomanip>
#include "nhaplieu.h"
using namespace std;

int main() {
    cout << "===== DANG KY THONG TIN =====" << endl;

    string hoTen = nhapChuoi("Ho ten        : ");
    int    tuoi  = nhapSoNguyen("Tuoi          : ", 1, 150);
    double diem  = nhapSoThuc("Diem TB (0-10): ", 0, 10);
    char   gioi  = nhapKyTu("Gioi tinh (M/F): ", "MFmf");
    string email = nhapChuoi("Email (tuy chon): ", true);

    cout << "\n===== THONG TIN DA NHAP =====" << endl;
    cout << fixed << setprecision(2);
    cout << "Ho ten   : " << hoTen << endl;
    cout << "Tuoi     : " << tuoi  << endl;
    cout << "Diem TB  : " << diem  << endl;
    cout << "Gioi tinh: " << gioi  << endl;
    cout << "Email    : " << (email.empty() ? "(khong co)" : email) << endl;

    if (nhapCoKhong("\nBan co muon luu thong tin")) {
        cout << ">> Da luu!" << endl;
    } else {
        cout << ">> Da huy." << endl;
    }
    return 0;
}
```

**Biên dịch:**

```bash
g++ -std=c++17 -Wall main.cpp nhaplieu.cpp -o dangky
./dangky
```

💡 **Hãy giữ thư viện này** — mọi bài tập có nhập liệu về sau đều dùng được, và bạn sẽ không bao giờ gặp lỗi trôi lệnh nữa.
