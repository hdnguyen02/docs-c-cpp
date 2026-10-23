# Lời giải — [C++]. Kiểu Pair

[← Quay lại bài học](../02-06-cpp-kieu-pair.md)

---

### Bài 1.

```cpp
#include <iostream>
#include <utility>
using namespace std;

int main() {
    // Cach 1: khai bao roi gan sau
    pair<int, int> A1;
    A1.first  = 3;
    A1.second = 7;
    cout << "Cach 1: " << A1.first << " " << A1.second << endl;

    // Cach 2: make_pair
    pair<int, int> A2 = make_pair(3, 7);
    cout << "Cach 2: " << A2.first << " " << A2.second << endl;

    // Cach 3: goi ham khoi tao
    pair<int, int> A3(3, 7);
    cout << "Cach 3: " << A3.first << " " << A3.second << endl;

    // Cach 4: danh sach khoi tao {}
    pair<int, int> A4 = {3, 7};
    cout << "Cach 4: " << A4.first << " " << A4.second << endl;

    return 0;
}
```

Output: cả 4 dòng đều in `3 7`.

**Nên dùng cách nào:** cách 4 (`= {3, 7}`) ngắn gọn và rõ nhất. `make_pair` hữu ích khi bạn không muốn viết lại kiểu dữ liệu (ví dụ khi truyền vào hàm).

### Bài 2.

```cpp
#include <iostream>
#include <utility>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    pair<double, double> A, B;

    cout << "Nhap toa do diem A (x y): ";
    cin >> A.first >> A.second;
    cout << "Nhap toa do diem B (x y): ";
    cin >> B.first >> B.second;

    double dx = B.first  - A.first;
    double dy = B.second - A.second;
    double kc = sqrt(dx * dx + dy * dy);

    cout << fixed << setprecision(3);
    cout << "Khoang cach AB = " << kc << endl;
    return 0;
}
```

Ví dụ:

```
Nhap toa do diem A (x y): 0 0
Nhap toa do diem B (x y): 3 4
Khoang cach AB = 5.000
```

### Bài 3.

```cpp
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main() {
    pair<string, int> nguoi;

    cout << "Nhap ten (viet lien): ";
    cin >> nguoi.first;
    cout << "Nhap tuoi: ";
    cin >> nguoi.second;

    cout << "Ho ten: " << nguoi.first << ", Tuoi: " << nguoi.second << endl;
    return 0;
}
```

### Bài 4.

```cpp
#include <iostream>
#include <utility>
using namespace std;

// Ham tra ve mot pair chua (tong, hieu)
pair<int, int> tinhTongHieu(int a, int b) {
    return {a + b, a - b};
}

int main() {
    int a, b;
    cout << "Nhap a va b: ";
    cin >> a >> b;

    pair<int, int> kq = tinhTongHieu(a, b);
    cout << "Tong = " << kq.first  << endl;
    cout << "Hieu = " << kq.second << endl;
    return 0;
}
```

**Đây là ứng dụng quan trọng nhất của `pair`:** một hàm trong C++ chỉ trả về được **một** giá trị. Muốn trả về 2 giá trị, `pair` là cách gọn nhất (không cần tham chiếu hay struct riêng).

### Bài 5.

```cpp
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main() {
    pair<string, pair<int, double>> monHoc = {"Lap trinh C++", {3, 8.5}};

    cout << "Ten mon    : " << monHoc.first                << endl;
    cout << "So tin chi : " << monHoc.second.first         << endl;
    cout << "Diem       : " << monHoc.second.second        << endl;
    return 0;
}
```

Output:

```
Ten mon    : Lap trinh C++
So tin chi : 3
Diem       : 8.5
```

⚠️ **Lưu ý:** với C++ cũ (trước C++11), phải viết `pair<int, pair<char, int> >` — có **dấu cách** giữa 2 dấu `>`, vì `>>` bị hiểu là toán tử dịch bit. Từ C++11 trở đi không cần nữa.

**Nhận xét:** `pair` lồng quá 2 tầng làm code rất khó đọc (`monHoc.second.second` là cái gì?). Khi cần lưu từ 3 trường trở lên, nên dùng `struct`:

```cpp
struct MonHoc {
    string ten;
    int soTinChi;
    double diem;
};
MonHoc m = {"Lap trinh C++", 3, 8.5};
cout << m.ten << " " << m.soTinChi << " " << m.diem;   // ro rang hon nhieu
```

### Bài 6.

```cpp
#include <iostream>
#include <utility>
#include <cmath>
using namespace std;

int main() {
    // 2 dinh doi dien cua hinh chu nhat (canh song song truc toa do)
    pair<pair<int,int>, pair<int,int>> hcn = {{1, 2}, {6, 9}};

    int x1 = hcn.first.first,  y1 = hcn.first.second;
    int x2 = hcn.second.first, y2 = hcn.second.second;

    int chieuDai = abs(x2 - x1);
    int chieuRong = abs(y2 - y1);

    cout << "Dinh 1    : (" << x1 << ", " << y1 << ")" << endl;
    cout << "Dinh 2    : (" << x2 << ", " << y2 << ")" << endl;
    cout << "Chieu dai : " << chieuDai << endl;
    cout << "Chieu rong: " << chieuRong << endl;
    cout << "Chu vi    : " << 2 * (chieuDai + chieuRong) << endl;
    cout << "Dien tich : " << chieuDai * chieuRong << endl;
    return 0;
}
```

Output:

```
Dinh 1    : (1, 2)
Dinh 2    : (6, 9)
Chieu dai : 5
Chieu rong: 7
Chu vi    : 24
Dien tich : 35
```

**Dùng `abs`** để công thức vẫn đúng dù người dùng nhập đỉnh nào trước.

### Bài 7.

```cpp
#include <iostream>
#include <utility>
using namespace std;

int main() {
    pair<int, int> p1 = {5, 10};
    pair<int, int> p2 = {5, 3};

    cout << boolalpha;
    cout << "p1 <  p2 : " << (p1 <  p2) << endl;   // false
    cout << "p1 >  p2 : " << (p1 >  p2) << endl;   // true
    cout << "p1 == p2 : " << (p1 == p2) << endl;   // false
    return 0;
}
```

**Quy tắc so sánh pair (so sánh từ điển — lexicographical):**

1. So sánh `first` trước.
2. Nếu `first` **khác nhau** → kết luận luôn, không xét `second`.
3. Nếu `first` **bằng nhau** → mới so sánh `second`.

Áp dụng cho `p1 = {5, 10}` và `p2 = {5, 3}`:
- `first` bằng nhau (5 = 5) → xét tiếp `second`
- `10 > 3` → `p1 > p2` ✔

Giống hệt cách xếp từ trong từ điển: so chữ cái đầu trước, bằng nhau mới xét chữ cái thứ hai.

**Ứng dụng cực kỳ hữu ích:** nhờ tính chất này, `sort` một mảng `pair` sẽ tự động sắp theo `first` tăng dần, và khi `first` bằng nhau thì sắp theo `second` tăng dần — **mà không cần viết hàm so sánh**.

### Bài 8.

```cpp
#include <iostream>
#include <utility>
using namespace std;

void inPair(const string& nhan, pair<int,int> p) {
    cout << nhan << " = {" << p.first << ", " << p.second << "}" << endl;
}

int main() {
    pair<int, int> p1 = {10, 20};
    pair<int, int> p2 = {30, 40};

    cout << "--- Ban dau ---" << endl;
    inPair("p1", p1);  inPair("p2", p2);

    p1.swap(p2);                       // Cach 1: phuong thuc swap cua pair
    cout << "--- Sau p1.swap(p2) ---" << endl;
    inPair("p1", p1);  inPair("p2", p2);

    swap(p1, p2);                      // Cach 2: ham swap tu do (<utility>)
    cout << "--- Sau swap(p1, p2) ---" << endl;
    inPair("p1", p1);  inPair("p2", p2);

    return 0;
}
```

Hai cách hoàn toàn tương đương về kết quả. `swap(p1, p2)` phổ biến hơn vì viết được cho mọi kiểu dữ liệu.

### Bài 9.

```cpp
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main() {
    const int N = 5;
    pair<string, int> hs[N];

    for (int i = 0; i < N; i++) {
        cout << "Hoc sinh " << i + 1 << " (ten diem): ";
        cin >> hs[i].first >> hs[i].second;
    }

    int viTriMax = 0;
    for (int i = 1; i < N; i++) {
        if (hs[i].second > hs[viTriMax].second) {
            viTriMax = i;
        }
    }

    cout << "\nHoc sinh diem cao nhat: " << hs[viTriMax].first
         << " (" << hs[viTriMax].second << " diem)" << endl;
    return 0;
}
```

### Bài 10.

```cpp
#include <iostream>
#include <utility>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    pair<string, int> hs[5] = {
        {"An",   8},
        {"Binh", 10},
        {"Chi",  8},
        {"Dung", 6},
        {"An2",  10}
    };

    // sort mac dinh: theo first (ten) truoc -> KHONG phai theo diem
    // Muon sap theo DIEM, ta dao vi tri hoac dung ham so sanh
    sort(hs, hs + 5, [](const pair<string,int>& a, const pair<string,int>& b) {
        return a.second < b.second;      // so sanh theo diem tang dan
    });

    for (int i = 0; i < 5; i++) {
        cout << hs[i].first << " - " << hs[i].second << endl;
    }
    return 0;
}
```

Output:

```
Dung - 6
An - 8
Chi - 8
Binh - 10
An2 - 10
```

**Khi 2 học sinh cùng điểm thì thứ tự ra sao?** Với `sort`, thứ tự của các phần tử bằng nhau là **không đảm bảo** (sort không ổn định — *not stable*). Ở ví dụ trên ta may mắn thấy An trước Chi, nhưng với dữ liệu lớn hơn thứ tự có thể đảo.

Hai cách xử lý:

```cpp
// Cach 1: dung stable_sort - giu nguyen thu tu ban dau cua cac phan tu bang nhau
stable_sort(hs, hs + 5, [](auto& a, auto& b){ return a.second < b.second; });

// Cach 2: bo sung tieu chi phu - bang diem thi xep theo ten
sort(hs, hs + 5, [](auto& a, auto& b){
    if (a.second != b.second) return a.second < b.second;
    return a.first < b.first;
});
```

Chi tiết xem bài [10-03 — Comparison function](../10-03-c-xay-dung-comparison-function-cho-ham-sort-trong-c.md) và [10-04 — stable_sort](../10-04-c-ham-stablesort-trong-c.md).

**Mẹo hay dùng:** nếu để `pair<diem, ten>` (điểm ở `first`) thì chỉ cần `sort(hs, hs+5)` là xong — tự động sắp theo điểm, bằng điểm thì theo tên.

### Bài 11.

```cpp
#include <iostream>
#include <utility>
#include <numeric>     // gcd (C++17)
using namespace std;

// Tim uoc chung lon nhat bang thuat toan Euclid
int ucln(int a, int b) {
    while (b != 0) {
        int tam = a % b;
        a = b;
        b = tam;
    }
    return a < 0 ? -a : a;
}

int main() {
    pair<int, int> ps;
    cout << "Nhap tu so va mau so: ";
    cin >> ps.first >> ps.second;

    if (ps.second == 0) {
        cout << "Mau so khong duoc bang 0!" << endl;
        return 1;
    }

    int d = ucln(ps.first, ps.second);
    ps.first  /= d;
    ps.second /= d;

    // Dua dau am len tu so
    if (ps.second < 0) {
        ps.first  = -ps.first;
        ps.second = -ps.second;
    }

    cout << "Phan so rut gon: " << ps.first << "/" << ps.second << endl;
    return 0;
}
```

Ví dụ:

```
Nhap tu so va mau so: 12 18
Phan so rut gon: 2/3
```

*(Từ C++17 có sẵn `std::gcd(a, b)` trong `<numeric>`, không cần tự viết.)*

### Bài 12.

```cpp
#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

// Hai khoang [a1,b1] va [a2,b2] chong lan khi:  a1 < b2  VA  a2 < b1
bool chongLan(pair<int,int> x, pair<int,int> y) {
    return x.first < y.second && y.first < x.second;
}

int main() {
    pair<int, int> cv[3];
    for (int i = 0; i < 3; i++) {
        cout << "Cong viec " << i + 1 << " (bat dau ket thuc): ";
        cin >> cv[i].first >> cv[i].second;
    }

    bool coChongLan = false;
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (chongLan(cv[i], cv[j])) {
                cout << "Cong viec " << i + 1 << " va " << j + 1
                     << " bi chong lan thoi gian!" << endl;
                coChongLan = true;
            }
        }
    }

    if (!coChongLan) {
        cout << "Khong co cong viec nao chong lan." << endl;
    }
    return 0;
}
```

Ví dụ:

```
Cong viec 1 (bat dau ket thuc): 1 5
Cong viec 2 (bat dau ket thuc): 4 8
Cong viec 3 (bat dau ket thuc): 9 12
Cong viec 1 va 2 bi chong lan thoi gian!
```

**Mẹo nhớ điều kiện chồng lấn:** dễ hơn là xét điều kiện **không** chồng lấn — khi việc này kết thúc trước khi việc kia bắt đầu (`b1 <= a2` hoặc `b2 <= a1`) — rồi phủ định.

### Bài 13.

```cpp
#include <iostream>
#include <utility>
#include <string>
using namespace std;

int main() {
    pair<int, string> p = {1, "An"};

    // Cach cu
    cout << p.first << " " << p.second << endl;

    // Cach 1: auto - chi rut gon phan khai bao kieu
    auto q = make_pair(2, string("Binh"));
    cout << q.first << " " << q.second << endl;

    // Cach 2: tie (C++11) - "go" pair ra 2 bien co san
    int id;
    string ten;
    tie(id, ten) = p;
    cout << id << " " << ten << endl;

    // Cach 3: structured binding (C++17) - GON NHAT, NEN DUNG
    auto [ma, hoTen] = p;
    cout << ma << " " << hoTen << endl;

    return 0;
}
```

**Structured binding** (`auto [a, b] = p;`) là cú pháp C++17 cho phép "tách" pair thành 2 biến có tên rõ nghĩa. Nó giải quyết đúng nhược điểm lớn nhất của `pair`: cái tên `.first`/`.second` không nói lên điều gì.

Cực kỳ hữu ích khi duyệt `map`:

```cpp
map<string, int> diem = {{"An", 9}, {"Binh", 8}};

// Cach cu - kho doc
for (auto it = diem.begin(); it != diem.end(); ++it)
    cout << it->first << ": " << it->second << endl;

// Cach C++17 - ro rang
for (auto [ten, d] : diem)
    cout << ten << ": " << d << endl;
```

Biên dịch cần chuẩn C++17: `g++ -std=c++17 main.cpp -o main`

### Bài 14.

```cpp
#include <iostream>
#include <utility>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    const int N = 5;
    pair<double, double> diem[N];

    for (int i = 0; i < N; i++) {
        cout << "Nhap toa do diem " << i + 1 << " (x y): ";
        cin >> diem[i].first >> diem[i].second;
    }

    int viTriGanNhat = 0;
    double kcMin = 1e18;

    for (int i = 0; i < N; i++) {
        // So sanh binh phuong khoang cach -> khong can sqrt, nhanh va chinh xac hon
        double kc2 = diem[i].first * diem[i].first
                   + diem[i].second * diem[i].second;
        if (kc2 < kcMin) {
            kcMin = kc2;
            viTriGanNhat = i;
        }
    }

    cout << fixed << setprecision(3);
    cout << "Diem gan goc O nhat: ("
         << diem[viTriGanNhat].first << ", "
         << diem[viTriGanNhat].second << ")"
         << " - khoang cach = " << sqrt(kcMin) << endl;
    return 0;
}
```

**Mẹo tối ưu:** khi chỉ cần *so sánh* khoảng cách chứ không cần giá trị thật, hãy so sánh **bình phương khoảng cách**. Vì `sqrt` là hàm đồng biến, thứ tự không đổi — mà tránh được phép căn tốn thời gian và tránh sai số làm tròn.

### Bài 15.

**3 tình huống `pair` tiện hơn hẳn 2 biến rời:**

1. **Hàm cần trả về 2 giá trị.** C++ chỉ cho `return` một thứ. Không có `pair` thì phải dùng tham chiếu (khó đọc) hoặc tạo `struct` riêng (dài dòng):

```cpp
pair<int,int> timMinMax(int a[], int n);      // gon
void timMinMax(int a[], int n, int& mn, int& mx);   // kho doc hon
```

2. **Lưu mảng các cặp và sắp xếp theo cặp.** Với 2 mảng rời (`ten[]` và `diem[]`), khi `sort` mảng điểm thì mảng tên **không đi theo** → dữ liệu bị lệch. Với `pair<string,int> hs[]`, sắp xếp là cả cặp di chuyển cùng nhau.

3. **Khi cần so sánh theo 2 tiêu chí.** `pair` có sẵn so sánh từ điển, nên `sort` hoạt động đúng ngay mà không cần viết comparator.

Ngoài ra `pair` còn là thành phần nền của `map` (mỗi phần tử của `map` chính là một `pair<key, value>`).

**1 tình huống `pair` làm code khó đọc hơn:**

Khi hai giá trị **không có quan hệ tự nhiên**, hoặc khi cần lưu **từ 3 trường trở lên**:

```cpp
// KHO DOC: .second.first la cai gi?
pair<string, pair<int, pair<double, bool>>> sv;
cout << sv.second.second.first;

// DE DOC: dung struct
struct SinhVien {
    string ten;
    int    tuoi;
    double diem;
    bool   daTotNghiep;
};
SinhVien sv;
cout << sv.diem;
```

**Quy tắc thực tế:** dùng `pair` cho **2 giá trị gắn bó tự nhiên** (toạ độ x-y, khoá-giá trị, bắt đầu-kết thúc). Từ 3 trường trở lên, hoặc khi tên `first`/`second` gây khó hiểu → chuyển sang `struct`.
