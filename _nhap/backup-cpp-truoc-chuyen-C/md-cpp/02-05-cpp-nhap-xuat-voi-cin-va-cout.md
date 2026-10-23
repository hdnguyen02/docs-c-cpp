# [C++]. Nhập Xuất Với Cin và Cout

Thao tác nhập dữ liệu từ bàn phím và hiển thị dữ liệu ra màn hình là thao tác đầu tiên bạn cần thành thạo khi học bất cứ ngôn ngữ lập trình nào. Bài viết này mình sẽ hướng dẫn các bạn nhập xuất một cách thành thạo với cin và cout

**NỘI DUNG :** 

- **In Ra Màn Hình Với Cout**
- **Nhập Từ Bàn Phím Với Cin**
- **Video Tutorial**

---

**1. In Ra Màn Hình Với Cout**

cout là một đối tượng giúp bạn có thể hiện thị nội dung như : số nguyên, số thực, giá trị của biến, đoạn text ra màn hình. Để sử dụng đối tượng này bạn cần khai báo thư viện "iostream" và sử dụng namespace std

cout được sử dụng đi kèm với toán tử chèn <<

```cpp
cout << "hello codelab" << endl; // Hiển thị dòng hello codelab lên màn hình và xuống dòng
cout << 100 << endl; // Hiển thị số 100 lên màn hình và xuống dòng
cout << banKinh << endl; // Hiển thị giá trị của biến banKinh lên màn hình
```

endl là một đối tượng đặc biệt giúp bạn có thể xuống dòng khi sử dụng cout, bạn sẽ thêm đối tượng này trong câu lệnh cout tại vị trí bạn muốn xuống dòng.

Ví dụ 1 :

```cpp
#include "iostream"

using namespace std;

int main(){
    cout << "codelab blog" << endl;
    cout << "codelab.dev" << " " << "C++ programming !" << endl;
    cout << 100 << " " << 200 << " " << 300 << endl;
    int n = 282828;
    cout << "Gia tri cua bien n : " << n << endl;
    
    return 0;
}
```

Output :

```cpp
codelab blog
codelab.dev C++ programming !
100 200 300
Gia tri cua bien n : 282828
```

Ví dụ 2 : Khi in ra giá trị của kiểu bool, nếu giá trị true sẽ được hiển thị số 1, ngược lại giá trị false sẽ được hiển thị số 0

Nếu bạn muốn hiển thị giá trị true, false bạn thêm cụm boolalpha trước biến bool này.

```cpp
#include "iostream"

using namespace std;

int main(){
    bool check = true;
    bool used = false;
    cout << check << " " << used << endl;
    cout << boolalpha << check << endl;
    cout << boolalpha << used << endl;
    return 0;
}
```

Output :

```cpp
1 0
true
false
```

**Lưu ý khi in giá trị của số thực float, double**

Đối với kiểu dữ liệu số thực, đề bài thường yêu cầu bạn in ra các số này với độ chính xác nhất định, cụ thể là bao nhiêu chữ số phần thập phân

Để in ra giá trị số float, double với độ chính xác k chữ số sau dấu phẩy bạn thêm cụm << fixed << setprecision(k) trước tên biến.

Thư viện chứa đối tượng setprecision là thư viện "iomanip", bạn cần thêm vào trước khi sử dụng.

Ví dụ 3 :

```cpp
#include "iostream"
#include "iomanip"

using namespace std;

int main(){
    float a = 30.192387;
    double b = 9.18293;
    cout << fixed << setprecision(2) << a << endl;
    cout << fixed << setprecision(10) << b << endl;
    return 0;
}
```

Output :

```cpp
30.19
9.1829300000
```

**Xác định độ rộng khi in với setw và setfill**

Khi bạn muốn in ra giá trị của 1 số, 1 biến hay đoạn text với độ rộng tương đương bao nhiêu dấu cách bạn có thể sử dụng setw(k) với k là độ rộng trước tên biến hay nội dung bạn muốn in.

Trong trường hợp bạn muốn thay thế các dấu cách khi nội dung bạn in ra không đủ độ rộng chỉ định bạn có thể sử dụng setfill(c) với c là ký tự bạn muốn thay thế cho các dấu cách trống.

Ví dụ 4:

```cpp
#include "iostream"
#include "iomanip"

using namespace std;

int main(){
    int n = 12345;
    cout << setw(10) << n << endl;
    cout << setw(10) << setfill('0') << n << endl;
    cout << setw(10) << setfill('#') << "codelab" << endl;
    return 0;
}
```

Output :

```cpp
     12345
0000012345
####codelab
```

---

**2. Nhập Từ Bàn Phím Với Cin**

cin là đối tượng giúp bạn có thể nhập dữ liệu từ bàn phím thay vì khởi tạo thủ công, cin nằm trong thư viện "iostream" và namespace std

cin đi kèm với toán tử nhập >>

```cpp
cin >> a; // Nhập giá trị cho a từ bàn phím
cin >> x >> y >> z; // Nhập giá trị cho 3 biến x, y, z lần lượt từ bàn phím
```

Khi nhập dữ liệu từ bàn phím bạn sẽ nhập dữ liệu xong sau đó enter, nếu bạn nhập nhiều số cùng 1 lúc thì cần có dấu cách giữa các số sau đó ấn enter sau số cuối cùng

Ví dụ trong câu lệnh thứ 2 ở trên khi nhập a, b, c thì bạn có thể nhập từng số rồi enter hoặc nhập 3 số cách nhau 1 dấu cách rồi mới enter cũng được.

Ví dụ 1 :

```cpp
#include "iostream"
#include "iomanip"

using namespace std;

int main(){
    int n, a, b, c;
    cout << "Nhap gia tri cho n : ";
    cin >> n;
    cout << "Gia tri n vua nhap la : " << n << endl;
    cout << "Nhap gia tri cho a, b, c : ";
    cin >> a >> b >> c;
    cout << "Gia tri a, b, c : " << a << " " << b << " " << c << endl;
    return 0;
}
```

---

**Video hướng dẫn Nhập Xuất trong C++ :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-05-cpp-nhap-xuat-voi-cin-va-cout.md](solutions/02-05-cpp-nhap-xuat-voi-cin-va-cout.md)

**Bài 1.** Nhập vào họ tên (không dấu, viết liền), tuổi và điểm trung bình của một sinh viên rồi in ra màn hình theo dạng:
`Sinh vien <ten>, <tuoi> tuoi, diem TB: <diem>`

**Bài 2.** Nhập 2 số nguyên `a`, `b` trên cùng một dòng, in ra tổng, hiệu, tích, thương của chúng.

**Bài 3.** Nhập vào bán kính hình tròn (số thực), tính và in ra chu vi, diện tích với **đúng 2 chữ số thập phân**.

**Bài 4.** Nhập một số thực, in ra số đó với lần lượt 0, 3, 6, 10 chữ số thập phân.

**Bài 5.** Nhập 3 số nguyên và in chúng ra theo cột, mỗi số chiếm độ rộng 10 ký tự, căn phải.

**Bài 6.** Làm lại bài 5 nhưng phần trống được lấp bằng dấu `*`.

**Bài 7.** Nhập một số nguyên có tối đa 6 chữ số, in ra số đó với độ rộng 8, các chỗ trống được điền số `0` ở phía trước (ví dụ `123` → `00000123`).

**Bài 8.** In ra bảng cửu chương 5 dưới dạng bảng có căn lề đẹp bằng `setw`:

```
 5 x  1 =  5
 5 x  2 = 10
 ...
 5 x 10 = 50
```

**Bài 9.** Nhập vào một biến `bool` (0 hoặc 1) rồi in ra dưới dạng `true`/`false`.

**Bài 10.** Nhập một ký tự và in ra: ký tự đó, mã ASCII của nó, và ký tự đó dưới dạng `char` được cộng thêm 1.

**Bài 11.** Viết chương trình in ra bảng thông tin 3 sản phẩm (tên, số lượng, đơn giá, thành tiền) căn lề bằng `setw` và `left`/`right`.

**Bài 12.** Nhập vào tổng số giây, in ra dưới dạng `hh:mm:ss` với mỗi phần luôn có 2 chữ số (ví dụ `3725` → `01:02:05`).

**Bài 13.** Chạy chương trình sau và giải thích vì sao dòng thứ hai vẫn in ra 3 chữ số thập phân mặc dù không có `setprecision`:

```cpp
cout << fixed << setprecision(3) << 1.23456 << endl;
cout << 9.87654 << endl;
```

**Bài 14.** Nhập vào tên (có dấu cách, ví dụ `Nguyen Van A`) và in ra. Nếu chỉ dùng `cin >>` thì kết quả có gì bất thường? Hãy thử và ghi lại.

**Bài 15.** Nhập điểm 3 môn của 3 sinh viên rồi in ra bảng điểm hoàn chỉnh có tiêu đề, đường kẻ, cột điểm trung bình lấy 2 chữ số thập phân.
