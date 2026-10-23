# [C++]. Đối Số Mặc Định Của Hàm

Đối số mặc định trong C++ giúp bạn có thể tự gán giá trị mặc định cho những đối số nếu bạn không cung cấp nó khi gọi hàm. Bài viết này mình sẽ giúp bạn cùng tìm hiểu một tính năng thú vị trong C++

**NỘI DUNG :** 

- **Đối Số Mặc Định**
- **Video Tutorial**

---

**1. Đối Số Mặc Định**

**Đối số mặc định** - Default Argument là giá trị mặc định sẽ được cung cấp cho hàm khi bạn xây dựng hàm, giá trị này sẽ được tự động gán nếu lời gọi hàm không cung cấp đối số tương ứng.

Trong trường hợp bạn cung cấp đối số cho đối số mặc định thì giá trị mặc định sẽ được ghi đè.

**Ví dụ** : Hàm có 4 tham số trong đó có 2 đối số mặc định, bạn có thể sử dụng hàm find này với 2, 3, hoặc 4 tham số.

Nếu khuyết tham số thứ 3, 4 thì giá trị mặc định sẽ được sử dụng

```cpp
#include "iostream"

using namespace std;

int find(int a, int b, int c = 3, int d = 4){
    cout << a << " " << b << " " << c << " " << d << endl;
    return a + b + c + d;
}

int main(){
    cout << find(1, 2) << endl;
    cout << find(1, 2, 10) << endl;
    cout << find(1, 2, 10, 20) << endl;
    return 0;
}
```

Output :

```cpp
1 2 3 4
10
1 2 10 4
17
1 2 10 20
33
```

**Giải thích :** 

- Hàm find(1, 2) vì khuyết đối số 3, và 4 nên c sẽ có giá trị mặc định là 3 và d có giá trị mặc định là 4
- Hàm find(1, 2, 10) vì khuyết đối số 4 d có giá trị mặc định là 4, giá trị của c đã được ghi đè thành 10
- Hàm find(1, 2, 10, 20) không bị khuyết đối số nên c được gán 10 và d được gán là 20

**Chú ý** : Bạn không thể xây dựng tham số thông thường sau tham số mặc định. Ví dụ xây dựng hàm như sau sẽ gây lỗi

```cpp
#include "iostream"

using namespace std;

int find(int a, int b, int c = 3, int d){
    cout << a << " " << b << " " << c << " " << d << endl;
    return a + b + c + d;
}

int main(){
    cout << find(1, 2) << endl;
    cout << find(1, 2, 10) << endl;
    cout << find(1, 2, 10, 20) << endl;
    return 0;
}
```

Output :

```cpp
error: default argument missing for parameter 4 of 'int find(int, int, int, int)'
```

**Những Chú Ý Về Đối Số Mặc Định**

- Đối số mặc định khác với đối số là hằng số
- Đối số mặc định sẽ được ghi đè giá trị nếu lời gọi hàm cung cấp giá trị tương ứng cho nó
- Khi một đối số mặc định được khai báo thì tất cả các đối số sau nó đều phải là đối số mặc định

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-04-cpp-doi-so-mac-dinh-cua-ham.md](solutions/05-04-cpp-doi-so-mac-dinh-cua-ham.md)

**Bài 1.** Viết hàm `void chao(string ten = "ban")` in ra `Xin chao <ten>`. Gọi hàm có và không có tham số.

**Bài 2.** Viết hàm `int luyThua(int a, int n = 2)` tính `a^n`, mặc định là bình phương.

**Bài 3.** Viết hàm `void inDuongKe(int doDai = 30, char kyTu = '-')` in ra một đường kẻ.

**Bài 4.** Viết hàm tính tiền `double tinhTien(double gia, int soLuong = 1, double giamGia = 0)`.

**Bài 5.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
void f(int a = 1, int b);
```

**Bài 6.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
int tong(int a, int b = 10);
...
int tong(int a, int b = 10) { return a + b; }
```

**Bài 7.** Viết hàm `void inMang(int a[], int n, string nhan = "Mang", char ngan = ' ')` in mảng với nhãn và ký tự ngăn cách tuỳ chọn.

**Bài 8.** Có thể bỏ qua tham số ở **giữa** khi gọi hàm không? Ví dụ với `f(int a, int b = 2, int c = 3)` gọi `f(1, , 5)`. Thử và giải thích.

**Bài 9.** Viết hàm nạp chồng `dienTich` và hàm dùng đối số mặc định làm cùng việc. So sánh 2 cách.

**Bài 10.** Chương trình sau có lỗi gì? Giải thích:

```cpp
void f(int a);
void f(int a, int b = 5);
...
f(3);
```

**Bài 11.** Viết hàm `string layNgay(int ngay, int thang, int nam = 2026, char ngan = '/')` trả về chuỗi ngày tháng định dạng.

**Bài 12.** Giá trị mặc định có thể là biểu thức hoặc lời gọi hàm không? Thử `void f(int x = 2 * 3)` và `void g(int x = tinhToan())`.

**Bài 13.** Viết hàm sắp xếp `void sapXep(int a[], int n, bool tangDan = true)` sắp xếp theo thứ tự tuỳ chọn.

**Bài 14.** Viết hàm vẽ hình chữ nhật `void veHCN(int cao, int rong = 0, char kyTu = '*')`; nếu `rong = 0` thì vẽ hình vuông.

**Bài 15.** Khi nào nên dùng đối số mặc định, khi nào nên dùng nạp chồng hàm? Lập bảng so sánh với ví dụ.
