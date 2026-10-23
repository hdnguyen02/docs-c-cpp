# [C++]. Tham Chiếu Và Tham Trị

Truyền tham chiếu trong C++ là một kỹ thuật giúp bạn có thể thay đổi giá trị của đối số sau khi lời gọi hàm kết thúc. Bài viết này mình sẽ giúp bạn phân biệt 2 cách xây dựng đối số trong C++ thông qua các ví dụ.

**NỘI DUNG :** 

- **Truyền Tham Trị**
- **Truyền Tham Chiếu**
- **Video Tutorial** 

---

**1. Truyền Tham Trị** 

**Truyền tham trị** - Pass by value là hình thức xây dựng tham số phổ biến cho hàm, như trong bài học trước về hàm thì mình đã chú ý về việc giá trị của đối số sẽ được gán cho tham số khi lời gọi hàm được thực hiện.

Xem xét ví dụ sau bạn sẽ hiểu rõ hơn về tham số và đối số, từ đó sẽ nắm được logic khi gọi hàm với cách truyền tham trị

Ở đây mình dùng toán tử địa chỉ (&) để in ra địa chỉ của biến trong bộ nhớ máy tính, địa chỉ thường được lưu dưới dạng số hexa.

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

void thaydoi(int n){
    cout << "Dia chi cua n trong bo nho may tinh : " << &n << endl;
    n += 100;
    cout << "Gia tri cua n trong ham thay doi : " << n << endl;
}

int main(){
    int m = 1000;
    cout << "Dia chi cua m trong bo nho may tinh : " << &m << endl;
    thaydoi(m);
    cout << "Gia tri cua m sau khi ham ket thuc : " << m << endl;
    return 0;
}
```

Output :

```cpp
Dia chi cua m trong bo nho may tinh : 0x6ffe1c
Dia chi cua n trong bo nho may tinh : 0x6ffdf0
Gia tri cua n trong ham thay doi : 1100
Gia tri cua m sau khi ham ket thuc : 1000
```

**Giải thích :** 

- n là tham số và m là đối số, giá trị của đối số m được gán cho n khi bạn gọi hàm thaydoi(m). Ở đây giá trị của m là 1000 sẽ được gán cho n và vì thế n cũng bằng 1000
- Địa chỉ của m trong máy tính là 0x6ffe1c, trong khi đó địa chỉ của n trong hàm thaydoi là 0x6ffdf0 điều này chứng tỏ n và m là 2 biến khác nhau, không cùng quản lý 1 ô nhớ trong máy tính
- Trong hàm thaydoi giá trị của n được tăng lên 100, khi đó n thành 1100 và ô nhớ 0x6ffdf0 (n đang quản lý) sẽ có giá trị là 1100
- Sau khi hàm thaydoi kết thúc thì giá trị của m vẫn sẽ là 1000, ô nhớ 0x6ffe1c không hề bị can thiệp gì khi hàm thay đổi thực thi

**Kết luận** : Khi hàm có tham số là tham trị thì đối số bạn truyền vào hàm và tham số của hàm là 2 biến khác nhau và việc bạn thay đổi tham số sẽ không ảnh hưởng gì tới đố số.

---

**2. Truyền Tham Chiếu**

**Truyền tham chiếu** - Pass by reference là cách thức xây dựng hàm với đối số là một tham chiếu, có thể hiểu đơn giản thì tham chiếu ở đây là địa chỉ của biến

Để xây dựng tham số là tham chiếu bạn thêm dấu & trước tên tham số khi xây dựng hàm.

Hàm khi truyền tham chiếu có thể giúp thay đổi giá trị của đối số sau khi lời gọi hàm kết thúc, hiểu đơn giản đây là phương pháp giúp hàm truy cập trực tiếp vào địa chỉ của đối số và thay đổi giá trị tại ô nhớ đó trong máy tính, dẫn đến giá trị của đối số sẽ bị thay đổi theo.

Xem xét ví dụ sau đây bạn sẽ hiểu rõ hơn về tham chiếu trong C++

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

void thaydoi(int &n){
    cout << "Dia chi cua n trong bo nho may tinh : " << &n << endl;
    n += 100;
}

int main(){
    int m = 1000;
    cout << "Dia chi cua m trong bo nho may tinh : " << &m << endl;
    thaydoi(m);
    cout << "Gia tri cua m sau khi ham ket thuc : " << m << endl;
    return 0;
}
```

Output :

```cpp
Dia chi cua m trong bo nho may tinh : 0x6ffe1c
Dia chi cua n trong bo nho may tinh : 0x6ffe1c
Gia tri cua m sau khi ham ket thuc : 1100
```

**Giải thích :** 

- Đối số m và tham số n trong trường hợp này đều quản lý ô nhớ có địa chỉ 0x6ffe1c trong máy tính
- Ở đây địa chỉ của m (0x6ffe1c) được gán cho địa chỉ của n (0x6ffe1c) vì thế những gì thay đổi đối với n và m thì đều thay đổi giá trị tại ô nhớ 0x6ffe1c
- Ban đầu n quản lý ô nhớ 0x6ffe1c đang có giá trị là 1000, sau đó n += 100 thì ô nhớ 0x6ffe1c lưu trữ giá trị 1100 và đây cũng là ô nhớ mà m đang quản lý, vì thế sau khi hàm kết thúc m cũng có giá trị là 1100

**Chú ý :** 

- Trong C không có truyền tham chiếu, bạn phải sử dụng con trỏ thay vì tham chiếu. Vậy nên nếu bạn đang học lập trình C thì đừng dùng nó một cách vô thức vì thấy người khác cũng dùng nó khi code C, thực tế đây là một hiểu nhầm
- Nếu tham số là tham chiếu thì bạn không thể truyền đối số là giá trị hằng số mà phải thông qua biến, ví dụ trong mã nguồn trên thì bạn không thể gọi thaydoi(1000) vì tham chiếu hoạt động dựa trên địa chỉ của đối số

Ví dụ về việc hoán đổi giá trị của 2 biến thông qua hàm bằng tham chiếu và tham trị :

```cpp
#include "iostream"

using namespace std;

void swap1(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
}

void swap2(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}

int main(){
    int x = 100, y = 200;
    swap1(x, y);
    cout << x << " " << y << endl;
    swap2(x, y);
    cout << x << " " << y << endl;
    return 0;
}
```

Output :

```cpp
100 200
200 100
```

**Kết luận :** Khi bạn cần xây dựng hàm và muốn những thay đổi trong hàm sẽ được giữ nguyên với đối số sau khi hàm kết thúc thì sử dụng truyền tham chiếu, cũng có một cách khác là sử dụng con trỏ nhưng bạn sẽ học kiến thức này sau.

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-03-c-tham-chieu-va-tham-tri.md](solutions/05-03-c-tham-chieu-va-tham-tri.md)

**Bài 1.** Viết hàm `void tangGapDoi(int x)` (tham trị) và `void tangGapDoi2(int &x)` (tham chiếu). Gọi cả hai và so sánh kết quả.

**Bài 2.** Viết hàm `void hoanDoi(int &a, int &b)` hoán đổi 2 số. Chứng minh nó hoạt động.

**Bài 3.** Viết lại hàm `hoanDoi` dùng tham trị và giải thích vì sao nó **không** hoạt động.

**Bài 4.** Viết hàm `void tinhTongHieu(int a, int b, int &tong, int &hieu)` trả về 2 kết quả qua tham chiếu.

**Bài 5.** Viết hàm `void nhapMang(int a[], int &n)` nhập mảng và cả số phần tử.

**Bài 6.** Viết hàm `void timMinMax(int a[], int n, int &mn, int &mx)` tìm cả min và max trong một lần duyệt.

**Bài 7.** Chương trình sau in ra gì? Giải thích:

```cpp
void f(int x, int &y) { x += 10; y += 10; }
int main(){
    int a = 1, b = 1;
    f(a, b);
    cout << a << " " << b;
}
```

**Bài 8.** Viết hàm nhận `string` theo 3 cách: `string s`, `string &s`, `const string &s`. Giải thích khác biệt về hiệu năng và tính an toàn.

**Bài 9.** Viết hàm `void chuanHoa(string &s)` chuyển toàn bộ chuỗi thành chữ thường, sửa trực tiếp trên chuỗi gốc.

**Bài 10.** Mảng được truyền vào hàm theo tham trị hay tham chiếu? Viết chương trình chứng minh.

**Bài 11.** Viết hàm `int& phanTu(int a[], int i)` trả về **tham chiếu** tới phần tử thứ `i`. Dùng nó để gán: `phanTu(a, 2) = 99;`

**Bài 12.** Chương trình sau có lỗi nguy hiểm gì? Giải thích:

```cpp
int& taoSo() {
    int x = 10;
    return x;
}
```

**Bài 13.** Viết hàm `void demChanLe(int a[], int n, int &chan, int &le)` đếm số lượng phần tử chẵn và lẻ.

**Bài 14.** So sánh tham chiếu (`&`) và con trỏ (`*`): lập bảng về cú pháp, khả năng gán lại, giá trị null, khi nào dùng cái nào.

**Bài 15.** Viết chương trình đo thời gian truyền một `vector<int>` 1 triệu phần tử vào hàm theo 2 cách (tham trị và `const` tham chiếu). So sánh kết quả.
