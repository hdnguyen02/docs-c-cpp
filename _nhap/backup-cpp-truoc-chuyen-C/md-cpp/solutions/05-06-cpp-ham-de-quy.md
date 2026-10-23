# Lời giải — [C++]. Hàm Đệ Quy

[← Quay lại bài học](../05-06-cpp-ham-de-quy.md)

> **Mọi hàm đệ quy phải có 2 phần:**
> 1. **Điều kiện dừng (base case)** — trường hợp đơn giản nhất, trả kết quả ngay, không gọi lại chính nó
> 2. **Bước đệ quy** — gọi lại chính nó với bài toán **nhỏ hơn**, tiến dần về điều kiện dừng

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

long long giaiThua(int n) {
    if (n <= 1) return 1;              // DIEU KIEN DUNG: 0! = 1! = 1
    return (long long)n * giaiThua(n - 1);   // BUOC DE QUY
}

int main() {
    for (int n = 0; n <= 10; n++) {
        cout << n << "! = " << giaiThua(n) << endl;
    }
    return 0;
}
```

**Quá trình thực thi với `n = 4`:**

```
giaiThua(4) = 4 * giaiThua(3)
              4 * (3 * giaiThua(2))
              4 * (3 * (2 * giaiThua(1)))
              4 * (3 * (2 * 1))           <- cham day, bat dau quay ve
              4 * (3 * 2)
              4 * 6
              24
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

long long tong(int n) {
    if (n <= 0) return 0;
    return n + tong(n - 1);
}

int main() {
    int n;
    cout << "Nhap n: ";
    cin >> n;
    cout << "1 + 2 + ... + " << n << " = " << tong(n) << endl;
    return 0;
}
```

⚠️ Với `n` lớn (khoảng 10⁵ trở lên), chương trình sẽ bị **tràn ngăn xếp (stack overflow)** vì có tới `n` lời gọi hàm lồng nhau. Bài toán này nên dùng công thức `n(n+1)/2` hoặc vòng lặp.

### Bài 3.

```cpp
#include <iostream>
using namespace std;

void demXuoi(int n) {
    if (n <= 0) return;
    demXuoi(n - 1);          // GOI DE QUY TRUOC
    cout << n << " ";        // roi moi IN -> in tu nho den lon
}

void demNguoc(int n) {
    if (n <= 0) return;
    cout << n << " ";        // IN TRUOC
    demNguoc(n - 1);         // roi moi goi de quy -> in tu lon xuong nho
}

int main() {
    cout << "Dem xuoi : "; demXuoi(5);  cout << endl;   // 1 2 3 4 5
    cout << "Dem nguoc: "; demNguoc(5); cout << endl;   // 5 4 3 2 1
    return 0;
}
```

💡 **Điểm mấu chốt:** chỉ đổi **thứ tự** giữa lệnh `cout` và lời gọi đệ quy là được kết quả ngược lại.

- **In trước, gọi sau** → xử lý trên đường "đi xuống" → thứ tự **xuôi theo lời gọi**
- **Gọi trước, in sau** → xử lý trên đường "quay về" → thứ tự **ngược lại**

Đây là kỹ thuật quan trọng, dùng nhiều khi duyệt cây (tiền thứ tự / hậu thứ tự).

### Bài 4.

```cpp
#include <iostream>
using namespace std;

// Cach 1: de quy don gian - O(n)
long long luyThua(int a, int n) {
    if (n == 0) return 1;
    return (long long)a * luyThua(a, n - 1);
}

// Cach 2: de quy nhi phan - O(log n)
long long luyThuaNhanh(long long a, int n) {
    if (n == 0) return 1;
    long long nua = luyThuaNhanh(a, n / 2);
    if (n % 2 == 0) return nua * nua;
    return nua * nua * a;
}

int main() {
    cout << "2^10 = " << luyThua(2, 10)      << endl;   // 1024
    cout << "3^5  = " << luyThuaNhanh(3, 5)  << endl;   // 243
    cout << "2^40 = " << luyThuaNhanh(2, 40) << endl;
    return 0;
}
```

**So sánh số lời gọi để tính `a^1000`:**

| Cách | Số lời gọi |
|---|---|
| Đệ quy đơn giản | 1000 |
| Đệ quy nhị phân | ~10 |

**Nguyên lý luỹ thừa nhanh:** `a^n = (a^(n/2))² nếu n chẵn`, `= (a^(n/2))² × a nếu n lẻ`.

⚠️ Chú ý gọi `luyThuaNhanh(a, n/2)` **một lần** rồi lưu vào `nua`. Nếu viết `luyThuaNhanh(a,n/2) * luyThuaNhanh(a,n/2)` thì lại thành O(n) — mất hết ưu thế.

### Bài 5.

```cpp
#include <iostream>
#include <chrono>
using namespace std;
using namespace std::chrono;

long long fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    for (int n = 30; n <= 45; n += 5) {
        auto batDau = high_resolution_clock::now();
        long long kq = fibonacci(n);
        auto ketThuc = high_resolution_clock::now();
        auto ms = duration_cast<milliseconds>(ketThuc - batDau).count();

        cout << "F(" << n << ") = " << kq << "  (" << ms << " ms)" << endl;
    }
    return 0;
}
```

Kết quả tham khảo:

```
F(30) = 832040        (4 ms)
F(35) = 9227465       (45 ms)
F(40) = 102334155     (500 ms)
F(45) = 1134903170    (5500 ms)
```

**Nhận xét: cực kỳ chậm.** Mỗi khi `n` tăng thêm 5, thời gian tăng khoảng **11 lần**.

**Nguyên nhân — tính lại vô số lần:**

```
                    F(5)
              /            \
          F(4)              F(3)
        /     \            /    \
     F(3)     F(2)      F(2)    F(1)
    /   \     /  \      /  \
  F(2) F(1) F(1) F(0) F(1) F(0)
  /  \
F(1) F(0)
```

`F(3)` được tính **2 lần**, `F(2)` tính **3 lần**, `F(1)` tính **5 lần**… Độ phức tạp là **O(2ⁿ)** — tăng theo cấp số nhân.

Để tính `F(50)` cần khoảng **2 tỷ** lời gọi hàm.

### Bài 6.

```cpp
#include <iostream>
#include <vector>
#include <chrono>
using namespace std;
using namespace std::chrono;

const int MAX = 100;
vector<long long> bangNho(MAX, -1);       // -1 = chua tinh

long long fibMemo(int n) {
    if (n <= 1) return n;
    if (bangNho[n] != -1) return bangNho[n];      // DA TINH ROI -> lay ra dung
    return bangNho[n] = fibMemo(n - 1) + fibMemo(n - 2);   // tinh va LUU LAI
}

long long fibThuong(int n) {
    if (n <= 1) return n;
    return fibThuong(n - 1) + fibThuong(n - 2);
}

int main() {
    auto t1 = high_resolution_clock::now();
    cout << "fibThuong(40) = " << fibThuong(40) << endl;
    auto t2 = high_resolution_clock::now();
    cout << "  Thoi gian: " << duration_cast<milliseconds>(t2 - t1).count() << " ms\n\n";

    t1 = high_resolution_clock::now();
    cout << "fibMemo(90)   = " << fibMemo(90) << endl;
    t2 = high_resolution_clock::now();
    cout << "  Thoi gian: " << duration_cast<microseconds>(t2 - t1).count() << " micro giay\n";
    return 0;
}
```

Kết quả:

```
fibThuong(40) = 102334155
  Thoi gian: 498 ms

fibMemo(90)   = 2880067194370816120
  Thoi gian: 3 micro giay
```

**Ghi nhớ (memoization)** đưa độ phức tạp từ **O(2ⁿ)** xuống **O(n)** — mỗi giá trị `F(i)` chỉ được tính đúng **một lần**, các lần sau lấy từ bảng.

Đây là kỹ thuật nền tảng của **quy hoạch động (dynamic programming)**.

💡 Với Fibonacci, cách nhanh nhất vẫn là **vòng lặp** (O(n), không tốn stack):

```cpp
long long fib(int n) {
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) { long long t = a + b; a = b; b = t; }
    return a;
}
```

### Bài 7.

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int ucln(int a, int b) {
    if (b == 0) return abs(a);           // DIEU KIEN DUNG
    return ucln(b, a % b);               // BUOC DE QUY
}

int main() {
    cout << "ucln(48, 18) = " << ucln(48, 18) << endl;   // 6
    cout << "ucln(17, 5)  = " << ucln(17, 5)  << endl;   // 1
    cout << "ucln(0, 7)   = " << ucln(0, 7)   << endl;   // 7
    return 0;
}
```

**Đây là ví dụ đệ quy ĐẸP NHẤT** — công thức toán học `UCLN(a,b) = UCLN(b, a mod b)` chuyển thành code gần như nguyên văn, chỉ 2 dòng.

Quá trình với `ucln(48, 18)`:

```
ucln(48, 18) -> ucln(18, 48%18=12)
             -> ucln(12, 18%12=6)
             -> ucln(6,  12%6=0)
             -> b == 0 -> tra ve 6
```

Số lời gọi rất ít (tối đa ~90 với số cỡ 10¹⁸), nên không lo tràn stack.

### Bài 8.

```cpp
#include <iostream>
#include <cstdlib>
using namespace std;

int tongChuSo(int n) {
    n = abs(n);
    if (n == 0) return 0;
    return n % 10 + tongChuSo(n / 10);
}

int demChuSo(int n) {
    n = abs(n);
    if (n < 10) return 1;              // so co 1 chu so (ke ca so 0)
    return 1 + demChuSo(n / 10);
}

int main() {
    int n = 12345;
    cout << "n = " << n << endl;
    cout << "Tong chu so : " << tongChuSo(n) << endl;   // 15
    cout << "So chu so   : " << demChuSo(n)  << endl;   // 5
    cout << "demChuSo(0) : " << demChuSo(0)  << endl;   // 1
    return 0;
}
```

⚠️ Điều kiện dừng của `demChuSo` là `n < 10` (chứ không phải `n == 0`) — như vậy xử lý đúng luôn trường hợp `n = 0`.

### Bài 9.

```cpp
#include <iostream>
using namespace std;

const char* KY_TU_SO = "0123456789ABCDEF";

void doiCoSo(int n, int b) {
    if (n == 0) return;
    doiCoSo(n / b, b);                 // GOI TRUOC (de in tu chu so cao)
    cout << KY_TU_SO[n % b];           // IN SAU
}

int main() {
    int n = 255;
    cout << n << " he 2  = ";  doiCoSo(n, 2);  cout << endl;   // 11111111
    cout << n << " he 8  = ";  doiCoSo(n, 8);  cout << endl;   // 377
    cout << n << " he 16 = ";  doiCoSo(n, 16); cout << endl;   // FF

    cout << 1000 << " he 2 = "; doiCoSo(1000, 2); cout << endl;
    return 0;
}
```

💡 **Đệ quy giải bài này rất gọn.** Với vòng lặp, ta lấy được các chữ số **từ thấp lên cao** nên phải lưu vào chuỗi rồi đảo ngược. Với đệ quy, chỉ cần gọi đệ quy **trước** rồi in **sau** — thứ tự tự động đúng (giống bài 3).

⚠️ Hàm không in gì với `n = 0`. Cần xử lý riêng nếu muốn in `"0"`.

### Bài 10.

```cpp
#include <iostream>
#include <string>
using namespace std;

// Cach 1: tra ve chuoi moi
string daoNguoc(const string& s) {
    if (s.length() <= 1) return s;
    return daoNguoc(s.substr(1)) + s[0];
}

// Cach 2: dao tai cho bang 2 chi so (hieu qua hon)
void daoTaiCho(string& s, int trai, int phai) {
    if (trai >= phai) return;
    swap(s[trai], s[phai]);
    daoTaiCho(s, trai + 1, phai - 1);
}

int main() {
    string s = "codelab";
    cout << "Cach 1: " << daoNguoc(s) << endl;      // baledoc

    string t = "programming";
    daoTaiCho(t, 0, t.length() - 1);
    cout << "Cach 2: " << t << endl;                // gnimmargorp
    return 0;
}
```

**Cách 1 hoạt động với `"abc"`:**

```
daoNguoc("abc") = daoNguoc("bc") + 'a'
                = (daoNguoc("c") + 'b') + 'a'
                = ("c" + 'b') + 'a'
                = "cb" + 'a'
                = "cba"
```

⚠️ **Cách 1 tốn kém:** mỗi lần `s.substr(1)` tạo một chuỗi mới → độ phức tạp O(n²) về thời gian lẫn bộ nhớ. Cách 2 dùng 2 chỉ số, không sao chép gì → O(n).

💡 Trong thực tế: `reverse(s.begin(), s.end());`

### Bài 11.

```cpp
#include <iostream>
#include <string>
using namespace std;

bool laDoiXung(const string& s, int trai, int phai) {
    if (trai >= phai) return true;              // da gap nhau -> doi xung
    if (s[trai] != s[phai]) return false;       // khac nhau -> khong doi xung
    return laDoiXung(s, trai + 1, phai - 1);    // xet cap trong hon
}

bool laDoiXung(const string& s) {
    if (s.empty()) return true;
    return laDoiXung(s, 0, s.length() - 1);
}

int main() {
    for (string s : {"aba", "abba", "abc", "a", "", "racecar"}) {
        cout << "\"" << s << "\" -> "
             << (laDoiXung(s) ? "DOI XUNG" : "khong") << endl;
    }
    return 0;
}
```

💡 **Mẫu thiết kế thường gặp:** một hàm "vỏ" đơn giản cho người dùng gọi (`laDoiXung(s)`) và một hàm đệ quy có thêm tham số phụ (`laDoiXung(s, trai, phai)`). Người dùng không phải quan tâm tới chi tiết bên trong.

### Bài 12.

```cpp
int f(int n) { return n + f(n - 1); }     // KHONG CO DIEU KIEN DUNG!
int main(){ cout << f(5); }
```

**Lỗi: đệ quy vô hạn → tràn ngăn xếp (stack overflow) → chương trình crash.**

Thông báo lỗi khi chạy:

```
Segmentation fault (core dumped)
```

**Quá trình:**

```
f(5) -> f(4) -> f(3) -> f(2) -> f(1) -> f(0) -> f(-1) -> f(-2) -> ... mai mai
```

Không có điều kiện dừng nên `n` cứ giảm về âm vô hạn. Mỗi lời gọi hàm chiếm một **khung ngăn xếp (stack frame)** chứa tham số, biến cục bộ, địa chỉ quay về. Ngăn xếp có giới hạn (~1–8 MB), nên sau khoảng **vài chục nghìn lời gọi** thì hết bộ nhớ.

**Sửa:**

```cpp
int f(int n) {
    if (n <= 0) return 0;         // <- THEM DIEU KIEN DUNG
    return n + f(n - 1);
}
```

✅ **Danh sách kiểm tra mỗi khi viết hàm đệ quy:**
1. Có **điều kiện dừng** chưa?
2. Bước đệ quy có làm bài toán **nhỏ đi** không?
3. Mọi đường đi có **chắc chắn** tới được điều kiện dừng không? (kể cả đầu vào âm, 0, rất lớn)

⚠️ Ngay cả hàm đệ quy **đúng** cũng có thể tràn stack nếu độ sâu quá lớn. `tong(1000000)` ở bài 2 sẽ crash dù code không sai.

### Bài 13.

```cpp
#include <iostream>
#include <algorithm>
using namespace std;

// Cach 1: so sanh phan tu dau voi max cua phan con lai
int timMax(int a[], int n) {
    if (n == 1) return a[0];
    return max(a[0], timMax(a + 1, n - 1));
}

// Cach 2: chia doi (divide and conquer) - do sau de quy chi O(log n)
int timMax2(int a[], int trai, int phai) {
    if (trai == phai) return a[trai];
    int giua = (trai + phai) / 2;
    return max(timMax2(a, trai, giua), timMax2(a, giua + 1, phai));
}

int main() {
    int a[] = {5, -3, 12, 0, 8, -7, 20, 4};
    int n = 8;

    cout << "Cach 1: " << timMax(a, n)        << endl;   // 20
    cout << "Cach 2: " << timMax2(a, 0, n-1)  << endl;   // 20
    return 0;
}
```

**So sánh 2 cách:**

| | Cách 1 (tuyến tính) | Cách 2 (chia đôi) |
|---|---|---|
| Số phép so sánh | n−1 | n−1 |
| **Độ sâu đệ quy** | **O(n)** — dễ tràn stack | **O(log n)** — an toàn |

Với mảng 1 triệu phần tử, cách 1 crash còn cách 2 chỉ cần độ sâu 20.

💡 `a + 1` trong cách 1 là **số học con trỏ** — tạo một con trỏ trỏ tới phần tử thứ 2, tức "mảng con bắt đầu từ vị trí 1".

### Bài 14.

```cpp
#include <iostream>
using namespace std;

long long soBuoc = 0;

void thapHaNoi(int n, char nguon, char dich, char trungGian) {
    if (n == 1) {
        soBuoc++;
        cout << "Buoc " << soBuoc << ": Chuyen dia 1 tu " << nguon
             << " sang " << dich << endl;
        return;
    }

    // ① Chuyen n-1 dia tren cung tu NGUON sang TRUNG GIAN
    thapHaNoi(n - 1, nguon, trungGian, dich);

    // ② Chuyen dia lon nhat tu NGUON sang DICH
    soBuoc++;
    cout << "Buoc " << soBuoc << ": Chuyen dia " << n << " tu " << nguon
         << " sang " << dich << endl;

    // ③ Chuyen n-1 dia tu TRUNG GIAN sang DICH
    thapHaNoi(n - 1, trungGian, dich, nguon);
}

int main() {
    int n;
    cout << "Nhap so dia: ";
    cin >> n;

    thapHaNoi(n, 'A', 'C', 'B');

    cout << "\nTong so buoc: " << soBuoc << " (= 2^" << n << " - 1)" << endl;
    return 0;
}
```

Với `n = 3`:

```
Buoc 1: Chuyen dia 1 tu A sang C
Buoc 2: Chuyen dia 2 tu A sang B
Buoc 3: Chuyen dia 1 tu C sang B
Buoc 4: Chuyen dia 3 tu A sang C
Buoc 5: Chuyen dia 1 tu B sang A
Buoc 6: Chuyen dia 2 tu B sang C
Buoc 7: Chuyen dia 1 tu A sang C

Tong so buoc: 7 (= 2^3 - 1)
```

**Ý tưởng — đây là bài toán KINH ĐIỂN của đệ quy:**

Để chuyển `n` đĩa từ A sang C (dùng B làm trung gian):
1. Chuyển `n−1` đĩa trên cùng từ A → B (bài toán con)
2. Chuyển đĩa to nhất từ A → C (một bước)
3. Chuyển `n−1` đĩa từ B → C (bài toán con)

Nếu giải bằng vòng lặp, code sẽ rất phức tạp. Với đệ quy chỉ mất vài dòng.

**Số bước:** `T(n) = 2×T(n−1) + 1 = 2ⁿ − 1`

| n | Số bước |
|---|---|
| 3 | 7 |
| 10 | 1.023 |
| 20 | 1.048.575 |
| 64 | ~1,8×10¹⁹ |

💡 Theo truyền thuyết, các nhà sư đang chuyển tháp 64 đĩa; khi xong thì thế giới kết thúc. Với 1 bước/giây, việc đó cần **585 tỷ năm**.

### Bài 15.

| Tiêu chí | Đệ quy | Vòng lặp |
|---|---|---|
| **Tốc độ** | Chậm hơn (mỗi lời gọi tốn chi phí) | ✅ Nhanh hơn |
| **Bộ nhớ** | ⚠️ Tốn stack O(độ sâu) | ✅ O(1) |
| **Rủi ro** | ⚠️ Tràn stack | Lặp vô hạn (nhưng không crash) |
| **Code ngắn gọn** | ✅ Rất ngắn với bài toán đệ quy tự nhiên | Dài hơn |
| **Dễ hiểu** | ✅ Rõ khi bài toán có cấu trúc đệ quy | ✅ Rõ với bài toán tuần tự |
| **Debug** | ⚠️ Khó (nhiều tầng lời gọi) | ✅ Dễ |

**Lý do đệ quy chậm hơn:** mỗi lời gọi hàm phải lưu tham số, biến cục bộ, địa chỉ quay về lên stack, rồi khôi phục khi quay ra. Vòng lặp không có chi phí này.

**✅ 3 bài toán NÊN dùng đệ quy:**

① **Tháp Hà Nội** — định nghĩa bài toán vốn đã đệ quy; giải bằng vòng lặp rất rối

② **Duyệt cây / đồ thị** (DFS) — cấu trúc dữ liệu tự thân là đệ quy

```cpp
void duyet(Node* nut) {
    if (nut == nullptr) return;
    cout << nut->giaTri;
    duyet(nut->trai);
    duyet(nut->phai);
}
```

③ **Sinh hoán vị / tổ hợp, quay lui (backtracking)** — bài toán N quân hậu, giải Sudoku, tìm đường trong mê cung

**✅ 3 bài toán NÊN dùng vòng lặp:**

① **Tính tổng, tích, trung bình của dãy** — bản chất tuần tự

```cpp
for (int i = 0; i < n; i++) tong += a[i];      // O(1) bo nho
```

② **Fibonacci, giai thừa** — đệ quy thuần cho Fibonacci là O(2ⁿ), vòng lặp là O(n)

③ **Duyệt mảng, chuỗi, tìm kiếm tuyến tính** — không có cấu trúc đệ quy nào để tận dụng

**Nguyên tắc chọn:**

> Dùng đệ quy khi **bài toán tự nhiên có cấu trúc đệ quy** (bài toán lớn chia thành các bài toán con cùng dạng). Dùng vòng lặp khi bài toán **tuần tự**.

💡 **Mọi hàm đệ quy đều viết lại được bằng vòng lặp** (dùng stack thủ công nếu cần), nhưng đôi khi code sẽ phức tạp hơn nhiều. Ngược lại, mọi vòng lặp đều viết được bằng đệ quy — nhưng thường không nên.

💡 **Đệ quy đuôi (tail recursion)** — khi lời gọi đệ quy là thao tác **cuối cùng** — có thể được compiler tối ưu thành vòng lặp (bật `-O2`), loại bỏ nguy cơ tràn stack:

```cpp
// De quy duoi - co the duoc toi uu
int ucln(int a, int b) {
    if (b == 0) return a;
    return ucln(b, a % b);      // khong con phep tinh nao sau loi goi
}

// KHONG phai de quy duoi - con phep nhan sau loi goi
long long giaiThua(int n) {
    if (n <= 1) return 1;
    return n * giaiThua(n - 1);
}
```
