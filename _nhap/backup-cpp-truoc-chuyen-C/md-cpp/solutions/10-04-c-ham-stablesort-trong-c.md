# Lời giải — [C++]. Hàm stable_sort() Trong C++

[← Quay lại bài học](../10-04-c-ham-stablesort-trong-c.md)

> **Ổn định (stable)** nghĩa là: các phần tử **bằng nhau** (theo tiêu chí so sánh) giữ nguyên **thứ tự tương đối ban đầu**.
> `sort` **không** ổn định; `stable_sort` **có**.

---

### Bài 1.

```cpp
#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

void in(const string& nhan, const vector<pair<int,char>>& v) {
    cout << nhan << ": ";
    for (const auto& [a, b] : v) cout << "(" << a << "," << b << ") ";
    cout << endl;
}

int main() {
    vector<pair<int,char>> goc = {
        {3,'a'}, {1,'b'}, {3,'c'}, {2,'d'}, {1,'e'}, {3,'f'}, {2,'g'}
    };

    in("Ban dau    ", goc);

    auto a = goc;
    sort(a.begin(), a.end(), [](const auto& x, const auto& y) {
        return x.first < y.first;
    });
    in("sort       ", a);

    auto b = goc;
    stable_sort(b.begin(), b.end(), [](const auto& x, const auto& y) {
        return x.first < y.first;
    });
    in("stable_sort", b);

    cout << "\nGiong nhau? " << boolalpha << (a == b) << endl;
    return 0;
}
```

Kết quả tham khảo:

```
Ban dau    : (3,a) (1,b) (3,c) (2,d) (1,e) (3,f) (2,g) 
sort       : (1,e) (1,b) (2,d) (2,g) (3,a) (3,c) (3,f) 
stable_sort: (1,b) (1,e) (2,d) (2,g) (3,a) (3,c) (3,f) 

Giong nhau? false
```

**Nhận xét:** với `stable_sort`, các cặp có `first = 1` giữ nguyên thứ tự `b` trước `e` (đúng như trong mảng gốc). Với `sort`, thứ tự bị đảo thành `e` trước `b`.

⚠️ Với mảng nhỏ (< 16 phần tử), `sort` dùng Insertion Sort nên **có thể** vẫn ổn định — kết quả phụ thuộc cài đặt và kích thước. Đó là lý do bài 2 cần mảng lớn.

### Bài 2.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Muc { int khoa; int thuTuGoc; };

int main() {
    const int N = 1000;

    // Tao mang lon voi nhieu gia tri khoa trung nhau
    vector<Muc> goc;
    for (int i = 0; i < N; i++)
        goc.push_back({i % 5, i});         // chi co 5 gia tri khoa khac nhau

    // ① sort
    auto a = goc;
    sort(a.begin(), a.end(), [](const Muc& x, const Muc& y) {
        return x.khoa < y.khoa;
    });

    // ② stable_sort
    auto b = goc;
    stable_sort(b.begin(), b.end(), [](const Muc& x, const Muc& y) {
        return x.khoa < y.khoa;
    });

    // Kiem tra tinh on dinh: thuTuGoc trong moi nhom phai TANG DAN
    auto kiemTraOnDinh = [](const vector<Muc>& v) {
        for (size_t i = 1; i < v.size(); i++)
            if (v[i].khoa == v[i-1].khoa && v[i].thuTuGoc < v[i-1].thuTuGoc)
                return false;
        return true;
    };

    cout << "Mang " << N << " phan tu, 5 gia tri khoa khac nhau" << endl;
    cout << boolalpha;
    cout << "sort        on dinh? " << kiemTraOnDinh(a) << endl;
    cout << "stable_sort on dinh? " << kiemTraOnDinh(b) << endl;

    // In 10 phan tu dau cua moi ket qua
    cout << "\n10 phan tu dau (sort):        ";
    for (int i = 0; i < 10; i++) cout << a[i].thuTuGoc << " ";
    cout << "\n10 phan tu dau (stable_sort): ";
    for (int i = 0; i < 10; i++) cout << b[i].thuTuGoc << " ";
    cout << endl;
    return 0;
}
```

Output:

```
Mang 1000 phan tu, 5 gia tri khoa khac nhau
sort        on dinh? false
stable_sort on dinh? true

10 phan tu dau (sort):        850 420 175 690 45 ...
10 phan tu dau (stable_sort): 0 5 10 15 20 25 30 35 40 45 
```

**Kết quả `stable_sort` có thứ tự gốc tăng đều `0, 5, 10, 15...`** — đúng như thứ tự ban đầu.

### Bài 3.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct SinhVien { string ten; double diem; };

int main() {
    // Thu tu nhap co y nghia (vi du: thu tu nop bai)
    vector<SinhVien> ds = {
        {"An",    9.0},
        {"Binh",  8.5},
        {"Chi",   9.0},
        {"Dung",  7.0},
        {"Em",    8.5},
        {"Phong", 9.0}
    };

    cout << "=== THU TU NHAP BAN DAU ===" << endl;
    for (size_t i = 0; i < ds.size(); i++)
        cout << "  " << i+1 << ". " << ds[i].ten << " - " << ds[i].diem << endl;

    // stable_sort: giu nguyen thu tu nhap khi CUNG DIEM
    stable_sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
        return a.diem > b.diem;
    });

    cout << "\n=== SAU KHI SAP THEO DIEM (stable_sort) ===" << endl;
    cout << fixed << setprecision(1);
    for (size_t i = 0; i < ds.size(); i++)
        cout << "  " << i+1 << ". " << left << setw(8) << ds[i].ten
             << " - " << ds[i].diem << endl;
    return 0;
}
```

Output:

```
=== SAU KHI SAP THEO DIEM (stable_sort) ===
  1. An       - 9.0
  2. Chi      - 9.0
  3. Phong    - 9.0
  4. Binh     - 8.5
  5. Em       - 8.5
  6. Dung     - 7.0
```

💡 An, Chi, Phong cùng 9.0 điểm và giữ nguyên thứ tự nhập — điều này **quan trọng** khi thứ tự nhập mang ý nghĩa (ai nộp bài trước).

### Bài 4.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct NhanVien {
    string ten;
    string phongBan;
    int    tuoi;
    double luong;
};

int main() {
    vector<NhanVien> ds = {
        {"An",    "IT",     25, 20},
        {"Binh",  "HR",     30, 15},
        {"Chi",   "IT",     28, 25},
        {"Dung",  "Sales",  25, 18},
        {"Em",    "IT",     25, 22},
        {"Phong", "HR",     35, 15}
    };

    // KY THUAT: goi stable_sort NHIEU LAN, tu tieu chi PHU den tieu chi CHINH
    //   ③ tieu chi phu nhat truoc
    stable_sort(ds.begin(), ds.end(),
                [](const NhanVien& a, const NhanVien& b) { return a.ten < b.ten; });

    //   ② tieu chi phu
    stable_sort(ds.begin(), ds.end(),
                [](const NhanVien& a, const NhanVien& b) { return a.tuoi < b.tuoi; });

    //   ① tieu chi chinh CUOI CUNG
    stable_sort(ds.begin(), ds.end(),
                [](const NhanVien& a, const NhanVien& b) { return a.phongBan < b.phongBan; });

    cout << "Sap theo: Phong ban -> Tuoi -> Ten" << endl;
    cout << "+----------+----------+------+--------+" << endl;
    cout << "| PHONG    | HO TEN   | TUOI | LUONG  |" << endl;
    cout << "+----------+----------+------+--------+" << endl;
    for (const auto& nv : ds)
        cout << "| " << left  << setw(8) << nv.phongBan
             << " | " << setw(8) << nv.ten
             << " | " << right << setw(4) << nv.tuoi
             << " | " << setw(6) << nv.luong << " |" << endl;
    cout << "+----------+----------+------+--------+" << endl;
    return 0;
}
```

Output:

```
+----------+----------+------+--------+
| PHONG    | HO TEN   | TUOI | LUONG  |
+----------+----------+------+--------+
| HR       | Binh     |   30 |     15 |
| HR       | Phong    |   35 |     15 |
| IT       | An       |   25 |     20 |
| IT       | Em       |   25 |     22 |
| IT       | Chi      |   28 |     25 |
| Sales    | Dung     |   25 |     18 |
+----------+----------+------+--------+
```

💡 **Kỹ thuật rất hay:** thay vì viết một comparator phức tạp nhiều `if`, gọi `stable_sort` nhiều lần theo thứ tự **ngược** (tiêu chí phụ trước, chính sau).

**Ưu điểm:** dễ đọc, dễ thêm/bớt tiêu chí, và mỗi comparator đơn giản.
**Nhược điểm:** chạy `n` lần sắp xếp thay vì 1 lần.

⚠️ **Chỉ hoạt động với `stable_sort`** — dùng `sort` sẽ phá vỡ kết quả của các lượt trước.

### Bài 5.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <chrono>
using namespace std;
using namespace std::chrono;

int main() {
    const int N = 1000000;

    vector<int> goc(N);
    for (int i = 0; i < N; i++) goc[i] = (i * 7919 + 13) % (N / 10);

    vector<int> a = goc;
    auto t1 = high_resolution_clock::now();
    sort(a.begin(), a.end());
    auto t2 = high_resolution_clock::now();
    auto tSort = duration_cast<milliseconds>(t2 - t1).count();

    vector<int> b = goc;
    t1 = high_resolution_clock::now();
    stable_sort(b.begin(), b.end());
    t2 = high_resolution_clock::now();
    auto tStable = duration_cast<milliseconds>(t2 - t1).count();

    cout << "Mang " << N << " phan tu:" << endl;
    cout << "  sort        : " << tSort   << " ms" << endl;
    cout << "  stable_sort : " << tStable << " ms" << endl;
    cout << "  Cham hon    : " << (double)tStable / max(1LL, tSort) << " lan" << endl;
    cout << "\nKet qua giong nhau: " << boolalpha << (a == b) << endl;
    return 0;
}
```

Kết quả tham khảo:

```
Mang 1000000 phan tu:
  sort        : 58 ms
  stable_sort : 84 ms
  Cham hon    : 1.45 lan

Ket qua giong nhau: true
```

**Nhận xét: `stable_sort` chậm hơn khoảng 30–50%.** Đây là cái giá phải trả cho tính ổn định.

### Bài 6.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    cout << "=== SO SANH BO NHO ===" << endl << endl;

    cout << "sort:" << endl;
    cout << "  Thuat toan  : Introsort (Quick + Heap + Insertion)" << endl;
    cout << "  Bo nho phu  : O(log n)  - chi cho stack de quy" << endl;
    cout << "  Voi n = 10^6: khoang 20 muc stack ~ vai tram byte" << endl;

    cout << "\nstable_sort:" << endl;
    cout << "  Thuat toan  : Merge Sort (co bo dem)" << endl;
    cout << "  Bo nho phu  : O(n)  - can mang tam bang kich thuoc du lieu" << endl;
    cout << "  Voi n = 10^6 int: khoang 4 MB bo nho phu" << endl;

    cout << "\nLuu y: neu khong du bo nho, stable_sort tu chuyen sang" << endl;
    cout << "thuat toan tai cho O(n log^2 n) - cham hon nhung khong ton RAM." << endl;

    // Minh hoa thuc te
    const int N = 10000000;
    cout << "\n--- Thuc te voi " << N << " int ---" << endl;
    cout << "Du lieu goc      : " << (double)N * sizeof(int) / (1024*1024) << " MB" << endl;
    cout << "sort can them    : ~0 MB" << endl;
    cout << "stable_sort can  : ~" << (double)N * sizeof(int) / (1024*1024) << " MB" << endl;
    return 0;
}
```

**Bảng so sánh bộ nhớ:**

| | `sort` | `stable_sort` |
|---|---|---|
| Thuật toán | Introsort | Merge Sort |
| Bộ nhớ phụ | **O(log n)** | **O(n)** |
| Với 10⁶ `int` | ~vài trăm byte | **~4 MB** |
| Với 10⁷ `int` | ~vài trăm byte | **~40 MB** |
| Khi thiếu bộ nhớ | — | Chuyển sang thuật toán tại chỗ O(n log²n) |

⚠️ **Với dữ liệu rất lớn, `stable_sort` có thể gây thiếu bộ nhớ.** Khi đó nó vẫn chạy được nhưng chậm hơn đáng kể.

### Bài 7.

**3 tình huống BẮT BUỘC dùng `stable_sort`:**

**① Sắp xếp nhiều tiêu chí bằng nhiều lượt** (như bài 4)

```cpp
stable_sort(ds.begin(), ds.end(), theoTen);       // tieu chi phu
stable_sort(ds.begin(), ds.end(), theoPhongBan);  // tieu chi chinh
// Dung sort se pha vo ket qua luot truoc
```

**② Thứ tự ban đầu mang ý nghĩa nghiệp vụ**

```cpp
// Danh sach giao dich theo thu tu THOI GIAN
// Sap theo so tien, nhung cung so tien thi giu thu tu thoi gian
stable_sort(giaoDich.begin(), giaoDich.end(), theoSoTien);
```

Ví dụ thực tế:
- Danh sách nộp bài (ai nộp trước được ưu tiên khi cùng điểm)
- Hàng đợi xử lý (FIFO trong cùng mức ưu tiên)
- Lịch sử giao dịch ngân hàng

**③ Giao diện người dùng — sắp xếp bảng theo cột**

```cpp
// Nguoi dung bam cot "Ten" -> sap theo ten
// Roi bam cot "Tuoi" -> sap theo tuoi, nhung cung tuoi van giu thu tu ten
```

Đây là hành vi người dùng **mong đợi** ở mọi bảng dữ liệu (Excel, Google Sheets đều làm vậy). Nếu dùng `sort`, mỗi lần bấm cột sẽ xáo trộn ngẫu nhiên.

**Khi nào KHÔNG cần `stable_sort`:**
- Sắp xếp số nguyên thuần tuý (các phần tử bằng nhau không phân biệt được)
- Comparator đã bao gồm tiêu chí phá hoà hoàn toàn (không có 2 phần tử nào "bằng nhau")
- Ưu tiên tốc độ và bộ nhớ

### Bài 8.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct SinhVien {
    string ten;
    double diem;
    int    thuTuGoc;          // them truong nay
};

int main() {
    vector<SinhVien> ds = {
        {"An", 9.0, 0}, {"Binh", 8.5, 1}, {"Chi", 9.0, 2},
        {"Dung", 7.0, 3}, {"Em", 8.5, 4}, {"Phong", 9.0, 5}
    };

    // Gan thu tu goc (neu chua co)
    for (size_t i = 0; i < ds.size(); i++) ds[i].thuTuGoc = i;

    // sort THONG THUONG nhung them thuTuGoc lam tieu chi phu
    // -> ket qua GIONG HET stable_sort
    sort(ds.begin(), ds.end(), [](const SinhVien& a, const SinhVien& b) {
        if (a.diem != b.diem) return a.diem > b.diem;
        return a.thuTuGoc < b.thuTuGoc;          // <- BI QUYET
    });

    cout << "Ket qua (sort + thuTuGoc = stable_sort):" << endl;
    for (const auto& sv : ds)
        cout << "  " << sv.ten << " - " << sv.diem
             << " (goc: " << sv.thuTuGoc << ")" << endl;
    return 0;
}
```

Output:

```
  An - 9 (goc: 0)
  Chi - 9 (goc: 2)
  Phong - 9 (goc: 5)
  Binh - 8.5 (goc: 1)
  Em - 8.5 (goc: 4)
  Dung - 7 (goc: 3)
```

💡 **Kỹ thuật này biến `sort` thành "ổn định":** thêm chỉ số ban đầu làm tiêu chí phá hoà cuối cùng. Khi đó **không còn 2 phần tử nào "bằng nhau"** nên thứ tự luôn xác định.

**So sánh 2 cách:**

| | `stable_sort` | `sort` + chỉ số |
|---|---|---|
| Tốc độ | Chậm hơn ~40% | ✅ Nhanh hơn |
| Bộ nhớ phụ | O(n) | ✅ O(log n) |
| Bộ nhớ dữ liệu | Không thêm | ⚠️ Thêm 4 byte/phần tử |
| Code | ✅ Đơn giản | Phải quản lý trường thêm |

### Bài 9.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Dong {
    string thanhPho;
    string quan;
    int    danSo;
};

int main() {
    vector<Dong> bang = {
        {"Ha Noi",   "Ba Dinh",   250},
        {"TP HCM",   "Quan 1",    180},
        {"Ha Noi",   "Cau Giay",  280},
        {"Da Nang",  "Hai Chau",  200},
        {"TP HCM",   "Quan 7",    360},
        {"Ha Noi",   "Dong Da",   400},
        {"TP HCM",   "Binh Thanh",490}
    };

    // ① Sap theo DAN SO giam dan (tieu chi PHU)
    stable_sort(bang.begin(), bang.end(),
                [](const Dong& a, const Dong& b) { return a.danSo > b.danSo; });

    // ② Sap theo THANH PHO (tieu chi CHINH) - stable_sort giu nguyen ket qua ①
    stable_sort(bang.begin(), bang.end(),
                [](const Dong& a, const Dong& b) { return a.thanhPho < b.thanhPho; });

    cout << "Nhom theo thanh pho, trong nhom sap theo dan so giam dan:" << endl;
    cout << "+------------+---------------+----------+" << endl;
    cout << "| THANH PHO  | QUAN          | DAN SO   |" << endl;
    cout << "+------------+---------------+----------+" << endl;

    string tpTruoc = "";
    for (const auto& d : bang) {
        if (d.thanhPho != tpTruoc && !tpTruoc.empty())
            cout << "+------------+---------------+----------+" << endl;
        cout << "| " << left  << setw(10) << (d.thanhPho == tpTruoc ? "" : d.thanhPho)
             << " | " << setw(13) << d.quan
             << " | " << right << setw(8) << d.danSo << " |" << endl;
        tpTruoc = d.thanhPho;
    }
    cout << "+------------+---------------+----------+" << endl;
    return 0;
}
```

Output:

```
+------------+---------------+----------+
| THANH PHO  | QUAN          | DAN SO   |
+------------+---------------+----------+
| Da Nang    | Hai Chau      |      200 |
+------------+---------------+----------+
| Ha Noi     | Dong Da       |      400 |
|            | Cau Giay      |      280 |
|            | Ba Dinh       |      250 |
+------------+---------------+----------+
| TP HCM     | Binh Thanh    |      490 |
|            | Quan 7        |      360 |
|            | Quan 1        |      180 |
+------------+---------------+----------+
```

💡 Đây chính là cách các phần mềm bảng tính thực hiện "sắp xếp nhiều cấp" (multi-level sort).

### Bài 10.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Muc { int khoa; char nhan; };

// Merge Sort - ON DINH
void tron(vector<Muc>& v, int trai, int giua, int phai) {
    vector<Muc> tam;
    int i = trai, j = giua + 1;

    while (i <= giua && j <= phai) {
        // DAU <= LA MAU CHOT: khi bang nhau, lay tu NUA TRAI truoc
        if (v[i].khoa <= v[j].khoa) tam.push_back(v[i++]);
        else                        tam.push_back(v[j++]);
    }
    while (i <= giua) tam.push_back(v[i++]);
    while (j <= phai) tam.push_back(v[j++]);

    for (size_t k = 0; k < tam.size(); k++) v[trai + k] = tam[k];
}

void mergeSort(vector<Muc>& v, int trai, int phai) {
    if (trai >= phai) return;
    int giua = trai + (phai - trai) / 2;
    mergeSort(v, trai, giua);
    mergeSort(v, giua + 1, phai);
    tron(v, trai, giua, phai);
}

int main() {
    vector<Muc> v = {
        {3,'a'}, {1,'b'}, {3,'c'}, {2,'d'}, {1,'e'}, {3,'f'}, {2,'g'}
    };

    cout << "Ban dau : ";
    for (const auto& m : v) cout << "(" << m.khoa << "," << m.nhan << ") ";
    cout << endl;

    mergeSort(v, 0, v.size() - 1);

    cout << "Sau sort: ";
    for (const auto& m : v) cout << "(" << m.khoa << "," << m.nhan << ") ";
    cout << endl;

    // Kiem tra on dinh
    bool onDinh = true;
    for (size_t i = 1; i < v.size(); i++)
        if (v[i].khoa == v[i-1].khoa && v[i].nhan < v[i-1].nhan) onDinh = false;

    cout << "\nOn dinh? " << boolalpha << onDinh << endl;
    return 0;
}
```

Output:

```
Ban dau : (3,a) (1,b) (3,c) (2,d) (1,e) (3,f) (2,g) 
Sau sort: (1,b) (1,e) (2,d) (2,g) (3,a) (3,c) (3,f) 

On dinh? true
```

💡 **Điểm mấu chốt tạo tính ổn định:** dấu `<=` trong `if (v[i].khoa <= v[j].khoa)`. Khi 2 phần tử bằng nhau, ta ưu tiên lấy từ **nửa trái** (xuất hiện trước trong mảng gốc).

⚠️ Đổi thành `<` sẽ làm thuật toán **mất tính ổn định**.

### Bài 11.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Muc { int khoa; char nhan; };

// Selection Sort - KHONG on dinh
void selectionSort(vector<Muc>& v) {
    int n = v.size();
    for (int i = 0; i < n - 1; i++) {
        int viTriMin = i;
        for (int j = i + 1; j < n; j++)
            if (v[j].khoa < v[viTriMin].khoa) viTriMin = j;

        if (viTriMin != i) swap(v[i], v[viTriMin]);    // <- PHEP SWAP PHA VO TINH ON DINH
    }
}

int main() {
    vector<Muc> v = {{2,'a'}, {2,'b'}, {1,'c'}};

    cout << "Ban dau : ";
    for (const auto& m : v) cout << "(" << m.khoa << "," << m.nhan << ") ";
    cout << endl;

    selectionSort(v);

    cout << "Sau sort: ";
    for (const auto& m : v) cout << "(" << m.khoa << "," << m.nhan << ") ";
    cout << endl;
    return 0;
}
```

Output:

```
Ban dau : (2,a) (2,b) (1,c) 
Sau sort: (1,c) (2,b) (2,a) 
```

**Phân tích vì sao mất ổn định:**

```
Buoc i=0: tim min trong [2a, 2b, 1c] -> la 1c (vi tri 2)
          swap(v[0], v[2])
          -> [1c, 2b, 2a]
          
          PHEP SWAP nay da NHAY 2a tu dau xuong cuoi,
          vuot qua 2b -> pha vo thu tu tuong doi!
```

Kết quả: `2b` đứng trước `2a`, trong khi ban đầu `2a` đứng trước.

**Tổng kết tính ổn định của các thuật toán:**

| Thuật toán | Ổn định? | Vì sao |
|---|---|---|
| Bubble Sort | ✅ Có | Chỉ đổi chỗ 2 phần tử **kề nhau** khi thực sự `>` |
| Insertion Sort | ✅ Có | Chèn vào **sau** các phần tử bằng nhau |
| Merge Sort | ✅ Có | Ưu tiên nửa trái khi bằng nhau |
| **Selection Sort** | ❌ **Không** | Phép swap nhảy qua nhiều phần tử |
| **Quick Sort** | ❌ **Không** | Phân hoạch dùng swap nhảy xa |
| **Heap Sort** | ❌ **Không** | Cấu trúc heap không giữ thứ tự |

### Bài 12.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void in(const string& nhan, const vector<int>& v) {
    cout << nhan << ": ";
    for (int x : v) cout << x << " ";
    cout << endl;
}

int main() {
    vector<int> goc = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    in("Ban dau        ", goc);

    // partition: KHONG dam bao thu tu
    vector<int> a = goc;
    auto it1 = partition(a.begin(), a.end(), [](int x) { return x % 2 == 0; });
    in("partition      ", a);
    cout << "  (so chan: " << (it1 - a.begin()) << " phan tu)" << endl;

    // stable_partition: GIU NGUYEN thu tu trong moi nhom
    vector<int> b = goc;
    auto it2 = stable_partition(b.begin(), b.end(), [](int x) { return x % 2 == 0; });
    in("stable_partition", b);
    cout << "  (so chan: " << (it2 - b.begin()) << " phan tu)" << endl;

    // Ung dung: tach roi sap xep tung nhom
    vector<int> c = {5, 2, 9, 4, 7, 6, 1, 8, 3};
    auto giua = stable_partition(c.begin(), c.end(), [](int x){ return x % 2 == 0; });
    sort(c.begin(), giua);       // sap nhom chan
    sort(giua, c.end());         // sap nhom le
    in("\nChan sap + le sap", c);
    return 0;
}
```

Output:

```
Ban dau        : 1 2 3 4 5 6 7 8 9 10 
partition      : 10 2 8 4 6 5 7 3 9 1 
  (so chan: 5 phan tu)
stable_partition: 2 4 6 8 10 1 3 5 7 9 
  (so chan: 5 phan tu)

Chan sap + le sap: 2 4 6 8 1 3 5 7 9 
```

**`partition` / `stable_partition`** chia mảng thành **2 nhóm** theo một điều kiện, trả về iterator tới **ranh giới** giữa 2 nhóm.

| | `partition` | `stable_partition` |
|---|---|---|
| Giữ thứ tự | ❌ Không | ✅ **Có** |
| Độ phức tạp | O(n) | O(n) hoặc O(n log n) |
| Bộ nhớ phụ | O(1) | O(n) |

💡 **Nhanh hơn `sort`** khi chỉ cần phân nhóm (không cần sắp xếp trong nhóm).

### Bài 13.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct GiaoDich {
    string ngay;          // "yyyy-mm-dd" de sap xep chuoi truc tiep
    string moTa;
    long long soTien;
};

int main() {
    // Danh sach theo THU TU NHAP (thu tu thoi gian thuc)
    vector<GiaoDich> ds = {
        {"2026-09-17", "Mua sach",      -250000},
        {"2026-09-15", "Nhan luong",   15000000},
        {"2026-09-17", "An trua",        -85000},
        {"2026-09-16", "Do xang",       -200000},
        {"2026-09-17", "Ca phe",         -45000},
        {"2026-09-15", "Tra tien nha", -5000000}
    };

    cout << "=== THU TU NHAP (theo thoi gian thuc) ===" << endl;
    for (size_t i = 0; i < ds.size(); i++)
        cout << "  " << i+1 << ". " << ds[i].ngay << " " << ds[i].moTa << endl;

    // stable_sort: cung ngay -> giu nguyen thu tu thoi gian nhap
    stable_sort(ds.begin(), ds.end(), [](const GiaoDich& a, const GiaoDich& b) {
        return a.ngay < b.ngay;
    });

    cout << "\n=== SAU KHI SAP THEO NGAY ===" << endl;
    cout << "+------------+-----------------+--------------+" << endl;
    cout << "| NGAY       | MO TA           | SO TIEN      |" << endl;
    cout << "+------------+-----------------+--------------+" << endl;

    string ngayTruoc = "";
    long long soDu = 0;
    for (const auto& gd : ds) {
        soDu += gd.soTien;
        cout << "| " << left  << setw(10) << (gd.ngay == ngayTruoc ? "" : gd.ngay)
             << " | " << setw(15) << gd.moTa
             << " | " << right << setw(12) << gd.soTien << " |" << endl;
        ngayTruoc = gd.ngay;
    }
    cout << "+------------+-----------------+--------------+" << endl;
    cout << "| " << left << setw(28) << "SO DU CUOI KY"
         << " | " << right << setw(12) << soDu << " |" << endl;
    cout << "+------------+-----------------+--------------+" << endl;
    return 0;
}
```

Output:

```
=== SAU KHI SAP THEO NGAY ===
+------------+-----------------+--------------+
| NGAY       | MO TA           | SO TIEN      |
+------------+-----------------+--------------+
| 2026-09-15 | Nhan luong      |     15000000 |
|            | Tra tien nha    |     -5000000 |
| 2026-09-16 | Do xang         |      -200000 |
| 2026-09-17 | Mua sach        |      -250000 |
|            | An trua         |       -85000 |
|            | Ca phe          |       -45000 |
+------------+-----------------+--------------+
```

💡 **Định dạng `"yyyy-mm-dd"` (ISO 8601)** cho phép sắp xếp chuỗi trực tiếp mà vẫn đúng thứ tự thời gian — đây là lý do chuẩn này được dùng rộng rãi trong cơ sở dữ liệu và API.

💡 Trong cùng một ngày, thứ tự giao dịch **giữ nguyên như lúc nhập** — điều bắt buộc với sổ kế toán.

### Bài 14.

**Bảng so sánh đầy đủ:**

| Hàm | Kết quả | Độ phức tạp | Bộ nhớ phụ | Ổn định | Dùng khi |
|---|---|---|---|---|---|
| **`sort`** | Toàn bộ được sắp xếp | O(n log n) | O(log n) | ❌ | Mặc định |
| **`stable_sort`** | Toàn bộ được sắp xếp | O(n log n) | **O(n)** | ✅ | Cần giữ thứ tự phần tử bằng nhau |
| **`partial_sort`** | `k` phần tử đầu đúng chỗ | O(n log k) | O(1) | ❌ | Chỉ cần top `k` |
| **`nth_element`** | Phần tử thứ `k` đúng chỗ | **O(n)** trung bình | O(1) | ❌ | Chỉ cần biết phần tử thứ `k` (trung vị) |
| `partition` | Chia 2 nhóm | O(n) | O(1) | ❌ | Chỉ cần phân nhóm |
| `stable_partition` | Chia 2 nhóm | O(n) | O(n) | ✅ | Phân nhóm giữ thứ tự |
| `is_sorted` | Kiểm tra | O(n) | O(1) | — | Kiểm tra |

**Ví dụ minh hoạ khác biệt với `{5, 2, 9, 1, 7, 3}`, `k = 3`:**

```cpp
sort          -> 1 2 3 5 7 9    (toan bo dung)
partial_sort  -> 1 2 3 9 7 5    (3 dau dung, phan sau bat ky)
nth_element   -> 2 1 3 5 9 7    (chi vi tri 2 dung: gia tri 3)
partition(le) -> 5 9 1 7 2 3    (le truoc, chan sau)
```

**Chọn hàm nào — theo nhu cầu:**

```
Can toan bo sap xep?
├─ Co ─ Can giu thu tu phan tu bang nhau?
│       ├─ Co  -> stable_sort
│       └─ Khong -> sort
└─ Khong ─ Can gi?
          ├─ Top k phan tu     -> partial_sort
          ├─ Phan tu thu k     -> nth_element
          └─ Chi phan nhom     -> partition / stable_partition
```

### Bài 15.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
using namespace std;

struct NguoiChoi {
    string ten;
    int    diem;
    int    hangTruoc;
};

void hienBang(const vector<NguoiChoi>& ds, const string& tieuDe) {
    cout << "\n=== " << tieuDe << " ===" << endl;
    cout << "+------+------------+-------+-----------+" << endl;
    cout << "| HANG | NGUOI CHOI | DIEM  | THAY DOI  |" << endl;
    cout << "+------+------------+-------+-----------+" << endl;

    for (size_t i = 0; i < ds.size(); i++) {
        int hangMoi = i + 1;
        int thayDoi = ds[i].hangTruoc - hangMoi;

        string mui;
        if      (ds[i].hangTruoc == 0) mui = "moi";
        else if (thayDoi > 0)  mui = "+" + to_string(thayDoi);
        else if (thayDoi < 0)  mui = to_string(thayDoi);
        else                   mui = "--";

        cout << "| " << left  << setw(4) << hangMoi
             << " | " << setw(10) << ds[i].ten
             << " | " << right << setw(5) << ds[i].diem
             << " | " << setw(9) << mui << " |" << endl;
    }
    cout << "+------+------------+-------+-----------+" << endl;
}

int main() {
    vector<NguoiChoi> ds = {
        {"An",    0, 0}, {"Binh",  0, 0}, {"Chi",   0, 0},
        {"Dung",  0, 0}, {"Em",    0, 0}, {"Phong", 0, 0}
    };

    // Diem tung vong cua tung nguoi
    int diemVong[3][6] = {
        {10, 15, 10, 8,  15, 12},        // vong 1
        {12,  8, 15, 20, 10, 12},        // vong 2
        {15, 15,  5, 10, 12, 18}         // vong 3
    };

    for (int vong = 0; vong < 3; vong++) {
        // Cong diem
        for (size_t i = 0; i < ds.size(); i++)
            ds[i].diem += diemVong[vong][i];

        // Luu hang hien tai truoc khi sap lai
        // (o day dung thu tu hien tai trong vector lam "hang truoc")
        for (size_t i = 0; i < ds.size(); i++)
            if (vong > 0) ds[i].hangTruoc = 0;   // se gan lai sau

        // Ghi lai hang cu
        vector<pair<string,int>> hangCu;
        for (size_t i = 0; i < ds.size(); i++) hangCu.push_back({ds[i].ten, (int)i + 1});

        // STABLE_SORT: diem giam dan, CUNG DIEM -> giu thu hang vong truoc
        stable_sort(ds.begin(), ds.end(), [](const NguoiChoi& a, const NguoiChoi& b) {
            return a.diem > b.diem;
        });

        // Cap nhat hangTruoc cho lan hien thi
        for (auto& p : ds)
            for (const auto& [ten, h] : hangCu)
                if (p.ten == ten) { p.hangTruoc = (vong == 0 ? 0 : h); break; }

        hienBang(ds, "SAU VONG " + to_string(vong + 1));
    }

    cout << "\n*** NHA VO DICH: " << ds[0].ten
         << " voi " << ds[0].diem << " diem ***" << endl;
    return 0;
}
```

Output (rút gọn):

```
=== SAU VONG 1 ===
+------+------------+-------+-----------+
| HANG | NGUOI CHOI | DIEM  | THAY DOI  |
+------+------------+-------+-----------+
| 1    | Binh       |    15 | moi       |
| 2    | Em         |    15 | moi       |
| 3    | Phong      |    12 | moi       |
| 4    | An         |    10 | moi       |
| 5    | Chi        |    10 | moi       |
| 6    | Dung       |     8 | moi       |
+------+------------+-------+-----------+

=== SAU VONG 3 ===
...
*** NHA VO DICH: Phong voi 42 diem ***
```

💡 **Vì sao phải dùng `stable_sort`:** Binh và Em cùng 15 điểm ở vòng 1. Nhờ `stable_sort`, thứ tự giữa họ được giữ nguyên qua các vòng thay vì nhảy loạn xạ — đây chính là cách các giải đấu thật xử lý (ai đạt điểm đó trước thì xếp trên).
