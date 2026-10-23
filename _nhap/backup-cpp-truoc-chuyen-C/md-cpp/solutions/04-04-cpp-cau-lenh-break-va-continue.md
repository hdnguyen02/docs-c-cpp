# Lời giải — [C++]. Câu Lệnh Break Và Continue

[← Quay lại bài học](../04-04-cpp-cau-lenh-break-va-continue.md)

> **`break`** — thoát **hẳn** khỏi vòng lặp (hoặc `switch`).
> **`continue`** — bỏ qua phần còn lại của **lần lặp hiện tại**, nhảy sang lần lặp kế tiếp.

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 20; i++) {
        if (i % 7 == 0) {
            cout << "\nGap so " << i << " chia het cho 7 -> DUNG" << endl;
            break;
        }
        cout << i << " ";
    }
    return 0;
}
```

Output:

```
1 2 3 4 5 6 
Gap so 7 chia het cho 7 -> DUNG
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 20; i++) {
        if (i % 3 == 0) continue;      // bo qua, khong in
        cout << i << " ";
    }
    cout << endl;
    return 0;
}
```

Output: `1 2 4 5 7 8 10 11 13 14 16 17 19 20`

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;

    if (n < 2) {
        cout << n << " KHONG phai so nguyen to" << endl;
        return 0;
    }

    bool nguyenTo = true;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) {
            nguyenTo = false;
            break;                      // tim thay uoc -> khong can duyet tiep
        }
    }

    cout << n << (nguyenTo ? " LA " : " KHONG phai ") << "so nguyen to" << endl;
    return 0;
}
```

💡 **Vì sao `break` quan trọng ở đây:** với `n = 1000000000` (số chẵn), không có `break` thì vòng lặp vẫn chạy hết ~31.623 bước; có `break` thì dừng ngay ở bước đầu tiên.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long tong = 0;
    int x, demDuong = 0;

    cout << "Nhap cac so (0 de dung):" << endl;

    while (true) {
        cin >> x;

        if (x == 0) break;             // dieu kien DUNG
        if (x < 0)  continue;          // BO QUA so am

        tong += x;
        demDuong++;
    }

    cout << "Co " << demDuong << " so duong, tong = " << tong << endl;
    return 0;
}
```

Ví dụ nhập `5 -3 10 -7 8 0`:

```
Co 3 so duong, tong = 23
```

**Mẫu code rất hay dùng:** `while (true)` + `break` cho điều kiện dừng + `continue` cho điều kiện bỏ qua. Cách này tách bạch 2 loại điều kiện rất rõ ràng.

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 100; i <= 1000; i++) {
        if (i % 7 == 0 && i % 11 == 0) {
            cout << "So dau tien: " << i << endl;
            break;
        }
    }
    return 0;
}
```

Output: `So dau tien: 154`

💡 Chia hết cho cả 7 và 11 ⟺ chia hết cho 77. Số đầu tiên ≥ 100 là `77 × 2 = 154`.

### Bài 6.

```cpp
#include <iostream>
using namespace std;

bool laNguyenTo(int n) {
    if (n < 2) return false;
    for (int i = 2; (long long)i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int dem = 0;

    cout << "10 so nguyen to dau tien: ";
    for (int n = 2; ; n++) {           // vong lap khong co dieu kien dung
        if (laNguyenTo(n)) {
            cout << n << " ";
            dem++;
            if (dem == 10) break;      // du 10 so thi dung
        }
    }
    cout << endl;
    return 0;
}
```

Output: `2 3 5 7 11 13 17 19 23 29`

💡 `for (int n = 2; ; n++)` — bỏ trống phần điều kiện nghĩa là **luôn đúng**, vòng lặp chỉ dừng bằng `break`. Đây là cách xử lý bài toán "tìm đủ k phần tử" khi không biết cần duyệt tới đâu.

### Bài 7.

**Output:**

```
1 2 4 5 
1 2 
```

**Giải thích:**

**Vòng 1 (`continue`):** khi `i == 3`, `continue` **bỏ qua `cout`** nhưng vòng lặp **vẫn tiếp tục** với `i = 4, 5`.

```
i=1 -> in 1
i=2 -> in 2
i=3 -> continue -> bo qua cout, nhay len i++
i=4 -> in 4
i=5 -> in 5
```

**Vòng 2 (`break`):** khi `i == 3`, `break` **thoát hẳn** vòng lặp, `i = 4, 5` không bao giờ chạy.

```
i=1 -> in 1
i=2 -> in 2
i=3 -> break -> THOAT
```

**Sơ đồ:**

```
continue:  [1] [2] [X] [4] [5]     <- nhay qua, roi tiep tuc
break:     [1] [2] [STOP]          <- dung han
```

### Bài 8.

```cpp
int i = 1;
while (i <= 10) {
    if (i % 2 == 0) continue;      // <- LOI: nhay qua ca i++
    cout << i << " ";
    i++;
}
```

**Lỗi:** khi `i` chẵn (ví dụ `i = 2`), `continue` nhảy thẳng về đầu vòng lặp — **bỏ qua luôn câu `i++`**. Nên `i` mãi bằng 2, điều kiện `i <= 10` luôn đúng → lặp vô hạn.

**Sửa cách 1 — tăng `i` trước khi `continue`:**

```cpp
int i = 0;
while (i < 10) {
    i++;                           // tang TRUOC
    if (i % 2 == 0) continue;
    cout << i << " ";
}
```

**Sửa cách 2 — dùng `for` (an toàn nhất):**

```cpp
for (int i = 1; i <= 10; i++) {
    if (i % 2 == 0) continue;
    cout << i << " ";
}
```

⚠️ **Đây là lý do `continue` an toàn với `for` nhưng nguy hiểm với `while`.** Trong `for`, phần cập nhật `i++` nằm trong chính cấu trúc `for` nên **`continue` vẫn thực hiện nó**. Trong `while`, phần cập nhật nằm trong thân nên bị bỏ qua.

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    for (int i = 1; i <= 5; i++) {
        for (int j = 1; j <= 5; j++) {
            if (i + j > 6) break;          // chi thoat vong TRONG
            cout << "(" << i << "," << j << ") ";
        }
        cout << endl;
    }
    return 0;
}
```

Output:

```
(1,1) (1,2) (1,3) (1,4) (1,5) 
(2,1) (2,2) (2,3) (2,4) 
(3,1) (3,2) (3,3) 
(4,1) (4,2) 
(5,1) 
```

Chú ý: sau `break`, vòng **ngoài** vẫn chạy tiếp sang `i` kế tiếp.

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    // --- CHUNG MINH: break chi thoat vong TRONG CUNG ---
    cout << "=== break thuong ===" << endl;
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            if (j == 2) break;
            cout << i << "-" << j << "  ";
        }
    }
    cout << "\n(Vong ngoai van chay du 3 lan)\n" << endl;

    // --- CACH 1: dung CO (flag) ---
    cout << "=== Cach 1: dung co ===" << endl;
    bool thoat = false;
    for (int i = 1; i <= 3 && !thoat; i++) {
        for (int j = 1; j <= 3; j++) {
            if (i == 2 && j == 2) { thoat = true; break; }
            cout << i << "-" << j << "  ";
        }
    }
    cout << endl;

    // --- CACH 2: dung goto ---
    cout << "=== Cach 2: goto ===" << endl;
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            if (i == 2 && j == 2) goto ketThuc;
            cout << i << "-" << j << "  ";
        }
    }
ketThuc:
    cout << endl;

    return 0;
}
```

**3 cách thoát nhiều vòng lặp cùng lúc:**

**① Dùng cờ (flag)** — phổ biến và an toàn nhất:

```cpp
bool timThay = false;
for (int i = 0; i < n && !timThay; i++) {
    for (int j = 0; j < m; j++) {
        if (dieuKien) { timThay = true; break; }
    }
}
```

**② Dùng `goto`** — ngắn gọn, đây là **trường hợp duy nhất** mà `goto` được chấp nhận trong C++ hiện đại:

```cpp
for (...) { for (...) { if (dk) goto xong; } }
xong:
```

**③ Tách thành hàm rồi `return`** — sạch nhất:

```cpp
pair<int,int> timKiem(...) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (dieuKien) return {i, j};    // thoat CA HAI vong
    return {-1, -1};
}
```

**Khuyến nghị:** ưu tiên cách ③ (tách hàm) vì code rõ ràng nhất; nếu không tiện thì dùng cách ①.

### Bài 11.

```cpp
#include <iostream>
using namespace std;

int main() {
    const int MUC_TIEU = 2025;
    bool timThay = false;

    for (int a = 1; a <= 100 && !timThay; a++) {
        for (int b = 1; b <= 100; b++) {
            if (a * a + b * b == MUC_TIEU) {
                cout << "Tim thay: a = " << a << ", b = " << b << endl;
                cout << a << "^2 + " << b << "^2 = "
                     << a*a << " + " << b*b << " = " << MUC_TIEU << endl;
                timThay = true;
                break;
            }
        }
    }

    if (!timThay) cout << "Khong tim thay cap nao" << endl;
    return 0;
}
```

Output:

```
Tim thay: a = 27, b = 36
27^2 + 36^2 = 729 + 1296 = 2025
```

💡 Cách tối ưu hơn: chỉ cần vòng lặp **một** biến, tính `b` từ `a`:

```cpp
for (int a = 1; a * a < MUC_TIEU; a++) {
    int con = MUC_TIEU - a * a;
    int b = (int)(sqrt(con) + 0.5);
    if (b * b == con) { /* tim thay */ break; }
}
```

Giảm từ 10.000 phép thử xuống còn ~45.

### Bài 12.

```cpp
#include <iostream>
using namespace std;

int main() {
    int x;
    int maxSo = 0;
    bool coSo = false;

    cout << "Nhap cac so (so am de dung):" << endl;

    while (true) {
        cin >> x;

        if (x < 0)  break;            // DUNG khi gap so am
        if (x == 0) continue;         // BO QUA so 0

        if (!coSo || x > maxSo) {
            maxSo = x;
            coSo = true;
        }
    }

    if (coSo) cout << "So lon nhat (khac 0) = " << maxSo << endl;
    else      cout << "Khong co so nao hop le" << endl;

    return 0;
}
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    long long tong = 0;

    for (int i = 1; i <= 100; i++) {
        if (i % 15 == 0) continue;         // bo qua boi cua ca 3 va 5

        cout << i << " ";
        tong += i;

        if (tong > 1000) {
            cout << "\n-> Tong = " << tong << " > 1000, DUNG tai i = " << i << endl;
            break;
        }
    }
    return 0;
}
```

Output:

```
1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 21 22 23 24 26 27 28 29 30 31 32 33 34 36 37 38 39 40 41 42 43 44 46 
-> Tong = 1035 > 1000, DUNG tai i = 46
```

💡 Chia hết cho cả 3 và 5 ⟺ chia hết cho BCNN(3,5) = **15**.

### Bài 14.

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double diem, tong = 0;
    int dem = 0, soLoi = 0;

    cout << "Nhap diem sinh vien (-1 de ket thuc):" << endl;

    while (true) {
        cout << "  Diem: ";
        cin >> diem;

        if (diem == -1) break;                    // KET THUC

        if (diem < 0 || diem > 10) {              // KHONG HOP LE -> bo qua
            cout << "    -> Diem khong hop le (phai tu 0 den 10)!" << endl;
            soLoi++;
            continue;
        }

        tong += diem;
        dem++;
    }

    cout << "\n--- KET QUA ---" << endl;
    cout << "So diem hop le   : " << dem   << endl;
    cout << "So diem bi loi   : " << soLoi << endl;

    if (dem > 0) {
        cout << fixed << setprecision(2);
        cout << "Tong diem        : " << tong << endl;
        cout << "Diem trung binh  : " << tong / dem << endl;
    } else {
        cout << "Khong co diem hop le nao." << endl;
    }
    return 0;
}
```

### Bài 15.

| | `break` | `return` | `goto` |
|---|---|---|---|
| **Thoát khỏi** | Vòng lặp / `switch` gần nhất | Toàn bộ **hàm** | Nhảy tới **nhãn** bất kỳ trong cùng hàm |
| **Thoát nhiều vòng lặp** | ❌ Chỉ 1 vòng | ✅ Tất cả | ✅ Tất cả |
| **Trả về giá trị** | ❌ Không | ✅ Có | ❌ Không |
| **Dễ đọc** | ✅ Rất rõ | ✅ Rõ | ⚠️ Dễ gây rối |
| **Được khuyến nghị** | ✅ Có | ✅ Có | ⚠️ Chỉ trong 1 trường hợp |

**① `break` — dùng khi:** thoát một vòng lặp, kết thúc `case` trong `switch`. Đây là lựa chọn mặc định.

```cpp
for (int i = 0; i < n; i++) {
    if (a[i] == target) { viTri = i; break; }
}
```

**② `return` — dùng khi:** đang trong một hàm và đã có kết quả. **Sạch nhất** khi cần thoát nhiều vòng lặp:

```cpp
int timKiem(int a[][100], int n, int m, int x) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (a[i][j] == x) return i * m + j;   // thoat CA HAI vong
    return -1;
}
```

**③ `goto` — chỉ dùng khi:** cần thoát nhiều vòng lặp lồng nhau mà không tiện tách hàm.

```cpp
for (...) {
    for (...) {
        for (...) {
            if (dieuKien) goto xong;
        }
    }
}
xong:
    cout << "Da thoat ca 3 vong lap";
```

**Vì sao `goto` bị ghét:** nó cho phép nhảy **bất kỳ đâu** trong hàm, tạo ra code "mì spaghetti" — luồng thực thi rối như tơ vò, không thể lần theo. Bài báo nổi tiếng năm 1968 của Edsger Dijkstra, *"Go To Statement Considered Harmful"*, đã khiến hầu hết ngôn ngữ hiện đại loại bỏ nó (Java, Python không có `goto`).

⚠️ `goto` còn có hạn chế kỹ thuật: **không được nhảy qua phần khởi tạo biến**.

```cpp
goto nhan;
int x = 10;      // error: jump to label 'nhan' crosses initialization of 'int x'
nhan:
```

**Kết luận thực dụng:**
1. Mặc định dùng `break`
2. Trong hàm và đã có kết quả → `return`
3. Nhiều vòng lặp lồng nhau → **tách thành hàm** rồi `return` (tốt nhất), hoặc dùng cờ
4. `goto` — chỉ khi 3 cách trên đều bất tiện, và nhớ đặt nhãn ngay sau vòng lặp
