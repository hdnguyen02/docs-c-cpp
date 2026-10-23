# Lời giải — [C++]. Vòng Lặp Do-While

[← Quay lại bài học](../04-03-cpp-vong-lap-do-while.md)

> **Đặc trưng của `do while`:** thân vòng lặp chạy **ít nhất 1 lần** trước khi kiểm tra điều kiện. Phù hợp khi "làm rồi mới hỏi có làm tiếp không".

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    int i = 1;
    do {
        cout << i << " ";
        i++;
    } while (i <= n);

    cout << endl;
    return 0;
}
```

⚠️ Với `n = 0` hoặc `n` âm, chương trình **vẫn in ra số 1** — vì `do while` chạy trước rồi mới kiểm tra. Đây chính là điểm khác biệt cốt lõi so với `while`.

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    do {
        cout << "Nhap mot so DUONG: ";
        cin >> n;
        if (n <= 0) cout << "  -> Sai roi, phai la so duong!" << endl;
    } while (n <= 0);

    cout << "Ban da nhap: " << n << endl;
    return 0;
}
```

**Đây là ứng dụng kinh điển nhất của `do while`** — kiểm tra dữ liệu đầu vào. Logic tự nhiên là "hỏi trước, kiểm tra sau", đúng thứ tự của `do while`.

Viết bằng `while` sẽ phải lặp code:

```cpp
cout << "Nhap so duong: ";      // phai viet 2 lan
cin >> n;
while (n <= 0) {
    cout << "Nhap so duong: ";  // lap lai
    cin >> n;
}
```

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    double diem;
    do {
        cout << "Nhap diem (0 - 10): ";
        cin >> diem;
        if (diem < 0 || diem > 10) {
            cout << "  -> Diem phai tu 0 den 10!" << endl;
        }
    } while (diem < 0 || diem > 10);

    cout << "Diem hop le: " << diem << endl;
    return 0;
}
```

💡 **Xử lý khi người dùng nhập chữ thay vì số:** `cin` sẽ vào trạng thái lỗi và vòng lặp thành vô hạn. Cách khắc phục:

```cpp
do {
    cout << "Nhap diem (0 - 10): ";
    if (!(cin >> diem)) {
        cin.clear();                    // xoa trang thai loi
        cin.ignore(10000, '\n');        // bo qua du lieu rac
        diem = -1;                      // gan gia tri khong hop le de lap lai
        cout << "  -> Phai nhap SO!" << endl;
    }
} while (diem < 0 || diem > 10);
```

### Bài 4.

```cpp
#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    int tam = abs(n);
    int dem = 0;

    do {
        dem++;
        tam /= 10;
    } while (tam > 0);

    cout << n << " co " << dem << " chu so" << endl;
    return 0;
}
```

💡 **Ưu điểm so với `while`:** với `n = 0`, `do while` vẫn chạy 1 lần nên `dem = 1` — **đúng ngay mà không cần `if` đặc biệt**. Bản dùng `while` (bài [04-02](../04-02-cpp-vong-lap-while.md) bài 2) phải xử lý riêng trường hợp này.

Đây là ví dụ đẹp cho thấy chọn đúng loại vòng lặp giúp code ngắn và ít lỗi hơn.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    int chon;

    do {
        cout << "\n========= MENU =========" << endl;
        cout << "1. Them du lieu"            << endl;
        cout << "2. Xoa du lieu"             << endl;
        cout << "3. Hien thi danh sach"      << endl;
        cout << "4. Thoat"                   << endl;
        cout << "========================"   << endl;
        cout << "Lua chon: ";
        cin >> chon;

        switch (chon) {
            case 1: cout << ">> Da THEM du lieu"     << endl; break;
            case 2: cout << ">> Da XOA du lieu"      << endl; break;
            case 3: cout << ">> Danh sach: (trong)"  << endl; break;
            case 4: cout << ">> Tam biet!"           << endl; break;
            default: cout << ">> Lua chon khong hop le!" << endl;
        }
    } while (chon != 4);

    return 0;
}
```

**Đây là mẫu chuẩn cho mọi chương trình quản lý** — kết hợp `do while` (hiện menu ít nhất 1 lần) với `switch case` (xử lý lựa chọn).

### Bài 6.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    char tiepTuc;

    do {
        double a, b;
        char pt;

        cout << "\nNhap bieu thuc (vd: 5 + 3): ";
        cin >> a >> pt >> b;

        cout << fixed << setprecision(4);
        switch (pt) {
            case '+': cout << "= " << a + b << endl; break;
            case '-': cout << "= " << a - b << endl; break;
            case '*': cout << "= " << a * b << endl; break;
            case '/':
                if (b == 0) cout << "Loi: chia cho 0!" << endl;
                else        cout << "= " << a / b << endl;
                break;
            default: cout << "Phep toan khong hop le!" << endl;
        }

        cout << "Tiep tuc? (y/n): ";
        cin >> tiepTuc;

    } while (tiepTuc == 'y' || tiepTuc == 'Y');

    cout << "Tam biet!" << endl;
    return 0;
}
```

### Bài 7.

```cpp
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int soBiMat = rand() % 100 + 1;
    int doan, soLan = 0;

    cout << "=== DOAN SO (1-100) ===" << endl;

    do {
        cout << "Doan cua ban: ";
        cin >> doan;
        soLan++;

        if      (doan < soBiMat) cout << "  -> LON HON " << doan << endl;
        else if (doan > soBiMat) cout << "  -> NHO HON " << doan << endl;
    } while (doan != soBiMat);

    cout << "CHINH XAC! So lan doan: " << soLan << endl;
    return 0;
}
```

**So với bản `while(true) + break`** (bài [04-02](../04-02-cpp-vong-lap-while.md) bài 15): bản `do while` gọn hơn vì điều kiện dừng nằm tự nhiên ở cuối, không cần `break`.

### Bài 8.

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    const string MAT_KHAU_DUNG = "codelab2026";
    const int SO_LAN_TOI_DA = 3;

    string nhap;
    int soLan = 0;
    bool thanhCong = false;

    do {
        soLan++;
        cout << "Lan " << soLan << "/" << SO_LAN_TOI_DA << " - Nhap mat khau: ";
        cin >> nhap;

        if (nhap == MAT_KHAU_DUNG) {
            thanhCong = true;
        } else {
            cout << "  -> Sai mat khau! Con "
                 << SO_LAN_TOI_DA - soLan << " lan thu." << endl;
        }
    } while (!thanhCong && soLan < SO_LAN_TOI_DA);

    if (thanhCong) cout << "\nDANG NHAP THANH CONG!" << endl;
    else           cout << "\nTAI KHOAN BI KHOA (sai qua " << SO_LAN_TOI_DA << " lan)" << endl;

    return 0;
}
```

**Điều kiện dừng kép:** `!thanhCong && soLan < SO_LAN_TOI_DA` — dừng khi **hoặc** đã đúng, **hoặc** hết lượt.

⚠️ Trong ứng dụng thật, **không bao giờ** lưu mật khẩu dạng văn bản thuần trong code. Phải lưu **hash** (SHA-256, bcrypt) của mật khẩu.

### Bài 9.

**Với `n = 0`:**

| | Đoạn A (`while`) | Đoạn B (`do while`) |
|---|---|---|
| Output | *(không in gì)* | `0` |
| Số lần thân chạy | **0 lần** | **1 lần** |

**Giải thích:**

```cpp
// A: kiem tra TRUOC
int i = 0;
while (i > 0) { ... }        // 0 > 0 la SAI ngay -> khong chay lan nao

// B: chay TRUOC, kiem tra SAU
int i = 0;
do {
    cout << i << " ";        // in 0
    i--;                     // i = -1
} while (i > 0);             // -1 > 0 SAI -> dung
```

**Đây là khác biệt duy nhất và cốt lõi giữa 2 loại vòng lặp:**

```
while:    KIEM TRA -> chay -> KIEM TRA -> chay -> ...   (co the chay 0 lan)
do while: chay -> KIEM TRA -> chay -> KIEM TRA -> ...   (chay it nhat 1 lan)
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    bool am = (n < 0);
    long long tam = am ? -(long long)n : n;
    long long dao = 0;

    do {
        dao = dao * 10 + tam % 10;
        tam /= 10;
    } while (tam > 0);

    if (am) dao = -dao;
    cout << "So dao nguoc = " << dao << endl;
    return 0;
}
```

Với `n = 0`, `do while` cho kết quả `0` — đúng. Bản `while` cũng cho 0 (vì `dao` khởi tạo bằng 0), nên ở bài này cả hai đều được.

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x, dem = 0;
    long long tong = 0;

    cout << "Nhap cac so (dung khi tong > 100):" << endl;

    do {
        cout << "  So thu " << dem + 1 << ": ";
        cin >> x;
        tong += x;
        dem++;
        cout << "  Tong hien tai = " << tong << endl;
    } while (tong <= 100);

    cout << "\nDa nhap " << dem << " so, tong = " << tong << endl;
    return 0;
}
```

⚠️ Nếu người dùng nhập toàn số âm hoặc 0 thì vòng lặp chạy mãi. Nên thêm giới hạn an toàn:

```cpp
} while (tong <= 100 && dem < 1000);
```

### Bài 12.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    long long soDu = 1000000;
    int chon;

    do {
        cout << "\n======== ATM CODELAB ========" << endl;
        cout << "1. Xem so du"                    << endl;
        cout << "2. Gui tien"                     << endl;
        cout << "3. Rut tien"                     << endl;
        cout << "4. Thoat"                        << endl;
        cout << "=============================" << endl;
        cout << "Chon chuc nang: ";
        cin >> chon;

        switch (chon) {
            case 1:
                cout << ">> So du hien tai: " << soDu << " VND" << endl;
                break;

            case 2: {
                long long tien;
                cout << ">> Nhap so tien gui: ";
                cin >> tien;
                if (tien <= 0) {
                    cout << "   Loi: so tien phai duong!" << endl;
                } else {
                    soDu += tien;
                    cout << "   Da gui " << tien << " VND. So du moi: "
                         << soDu << " VND" << endl;
                }
                break;
            }

            case 3: {
                long long tien;
                cout << ">> Nhap so tien rut: ";
                cin >> tien;
                if (tien <= 0) {
                    cout << "   Loi: so tien phai duong!" << endl;
                } else if (tien % 50000 != 0) {
                    cout << "   Loi: so tien phai la boi cua 50.000!" << endl;
                } else if (tien > soDu) {
                    cout << "   Loi: so du khong du! (con " << soDu << " VND)" << endl;
                } else {
                    soDu -= tien;
                    cout << "   Da rut " << tien << " VND. So du con lai: "
                         << soDu << " VND" << endl;
                }
                break;
            }

            case 4:
                cout << ">> Cam on quy khach. Tam biet!" << endl;
                break;

            default:
                cout << ">> Chuc nang khong hop le!" << endl;
        }
    } while (chon != 4);

    return 0;
}
```

⚠️ Chú ý cặp `{ }` bọc quanh `case 2` và `case 3` — bắt buộc khi khai báo biến mới bên trong `case` (xem bài [03-03](../03-03-cpp-switch-case.md) bài 3).

### Bài 13.

```cpp
int i = 1;
do {
    cout << i << " ";
    i++;
} while (i <= 10)          // <- THIEU DAU CHAM PHAY
```

**Lỗi:** thiếu dấu `;` sau `while (i <= 10)`.

Thông báo lỗi:

```
error: expected ';' before '}' token
```

**Sửa:**

```cpp
} while (i <= 10);         // <- CO dau ;
```

**Ghi nhớ:** `do while` là loại vòng lặp **duy nhất** bắt buộc kết thúc bằng dấu `;`.

| Cấu trúc | Có `;` ở cuối? |
|---|---|
| `for (...) { }` | ❌ Không |
| `while (...) { }` | ❌ Không |
| `do { } while (...);` | ✅ **Có** |
| `if (...) { }` | ❌ Không |

Lý do: `do while` được coi là một **câu lệnh** hoàn chỉnh (giống `cout << ...;`), còn `for`/`while` kết thúc bằng một khối `{ }`.

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int x;
    long long tong = 0;
    int dem = 0;

    cout << "Nhap cac so nguyen (-1 de ket thuc):" << endl;

    do {
        cin >> x;
        if (x != -1) {
            tong += x;
            dem++;
        }
    } while (x != -1);

    cout << "Da nhap " << dem << " so" << endl;
    cout << "Tong = " << tong << endl;
    if (dem > 0) {
        cout << fixed << setprecision(4);
        cout << "Trung binh = " << (double)tong / dem << endl;
    }
    return 0;
}
```

⚠️ Chú ý `if (x != -1)` bên trong — nếu không có, giá trị `-1` (giá trị đánh dấu kết thúc) cũng bị cộng vào tổng.

### Bài 15.

| Tiêu chí | `for` | `while` | `do while` |
|---|---|---|---|
| **Cú pháp** | `for (khoi_tao; dk; cap_nhat) { }` | `while (dk) { }` | `do { } while (dk);` |
| **Kiểm tra điều kiện** | Trước mỗi lần lặp | Trước mỗi lần lặp | **Sau** mỗi lần lặp |
| **Số lần chạy tối thiểu** | **0** | **0** | **1** |
| **Dấu `;` cuối** | Không | Không | ✅ **Có** |
| **Biết trước số lần lặp?** | ✅ Có | ❌ Thường không | ❌ Không |
| **Biến đếm** | Gói gọn trong `for`, tự huỷ sau vòng lặp | Phải khai báo bên ngoài | Phải khai báo bên ngoài |

**Khi nào dùng cái nào:**

| Tình huống | Nên dùng |
|---|---|
| Duyệt mảng, lặp `n` lần đã biết | **`for`** |
| Đọc dữ liệu tới khi hết / gặp giá trị kết thúc | **`while`** |
| Lặp tới khi một điều kiện toán học thoả (chia tới khi bằng 0) | **`while`** |
| Menu chương trình | **`do while`** |
| Kiểm tra và bắt nhập lại dữ liệu | **`do while`** |
| Trò chơi "chơi tiếp không?" | **`do while`** |

**Về mặt kỹ thuật, cả 3 loại đều thay thế được nhau** — mọi `for` đều viết lại được bằng `while` và ngược lại. Việc chọn đúng loại chỉ để code **dễ đọc và ít lỗi hơn**, không ảnh hưởng tốc độ.

```cpp
// Cung mot viec, 3 cach viet
for (int i = 1; i <= 5; i++) cout << i;

int i = 1;
while (i <= 5) { cout << i; i++; }

int j = 1;
do { cout << j; j++; } while (j <= 5);
```
