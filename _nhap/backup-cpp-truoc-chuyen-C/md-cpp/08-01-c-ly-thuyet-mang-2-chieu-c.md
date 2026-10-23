# [C++]. Lý Thuyết Mảng 2 Chiều C++

Mảng 2 chiều là một mảng kiến thức quan trọng trong các ngôn ngữ lập trình, bài học này các bạn sẽ học cách sử dụng mảng 2 chiều trong C++

**NỘI DUNG :** 

- **Mảng 2 Chiều**
- **Nhập Xuất Mảng 2 Chiều**
- **Mảng 2 Chiều Và Hàm**
- **Video Tutorial** 

---

**1. Mảng 2 Chiều**

Trong ngôn ngữ C++ khi cần giải quyết các bài toán liên quan tới ma trận hoặc bảng số thì mảng 2 chiều là cấu trúc dữ liệu có thể giúp bạn lưu trữ dữ liệu đầu vào.

Mảng 2 chiều tương tự như một bảng số gồm hàng và cột, mảng 2 chiều chính là một mảng các mảng 1 chiều

Để truy cập các phần tử trong mảng 2 chiều ta thông qua chỉ số hàng và cột được đánh số từ 0

Chú ý để truy cập vào phần tử trong mảng 2 chiều ta luôn dùng chỉ số hàng trước, chỉ số cột sau

Cú pháp khai báo : **Data_type array_name[rows][cols];**

- **Data_type** : Kiểu dữ liệu của phần tử trong mảng như int, float, char, double..
- **array_name** : Tên mảng 2 chiều
- **rows** : Số hàng của mảng 2 chiều
- **cols** : Số cột của mảng 2 chiều

Ví dụ mảng a[4][4]

![](../images/ae22eff134f984fa.png)

Khai báo mảng 2 chiều bạn có thể khai báo thủ công như sau :

```cpp
#include "iostream"

using namespace std;

int main(){
    int a[3][4] = {
        {1, 2, 3, 1},
        {4, 1, 5, 2},
        {3, 7, 9, 0}
    };
    cout << "a[0][2] = " << a[0][2] << endl;
    cout << "a[1][3] = " << a[1][3] << endl; 
    return 0;
}
```

Output :

```cpp
a[0][2] = 3
a[1][3] = 2
```

**Chú ý** : Trong mảng 2 chiều bạn không được truy cập vào các chỉ số hàng hay cột không hợp lệ. Mình thấy có nhiều bạn có thói quen dùng chỉ số hàng và cột từ 1 thay vì từ 0, việc này cũng không có vấn đề gì nếu mảng của bạn đủ lớn để các chỉ số bạn dùng là hợp lệ. Vậy nên khi sử dụng thì nên biết mình làm vậy có đúng không để khai báo kích cỡ mảng 2 chiều cho phù hợp.

---

**2. Nhập Xuất Mảng 2 Chiều**

Các dạng bài tập về mảng 2 chiều đều cho các biết trước số lượng hàng và cột của mảng 2 chiều, bạn có thể khai báo mảng 2 chiều dựa vào hàng cột mà đề bài cung cấp hoặc sử dụng mảng 2 chiều có kích cố định thước đủ lớn.

Để in ra mảng 2 chiều bạn dùng 2 vòng lặp lồng nhau, vòng lặp ngoài duyệt qua hàng, vòng for trong duyệt qua từng cột của hàng.

**Ví dụ 1** : Nhập và xuất mảng 2 chiều với kích thước cố định :

Chú ý code bên dưới sẽ đúng nếu giới hạn mảng 2 chiều của đề bài không vượt quá 205 hàng và số cột không vượt quá 205.

Nếu đề bài cho số lượng hàng và cột lớn hơn bạn cần khai báo mảng 2 chiều lớn hơn để phù hợp với bài toán

```cpp
#include "iostream"

using namespace std;

int main(){
    int n, m; // n : hang, m : cot
    int a[205][205]; // 205 x 205
    cout << "Nhap so hang, cot : ";
    cin >> n >> m;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << "a[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }
    }
    cout << "Mang vua nhap :\n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

**Ví dụ 2** : Nhập mảng 2 chiều dựa vào số hàng, cột của đề bài

```cpp
#include "iostream"

using namespace std;

int main(){
    int n, m; // n : hang, m : cot
    cout << "Nhap so hang, cot : ";
    cin >> n >> m;
    int a[n][m];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << "a[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }
    }
    cout << "Mang vua nhap :\n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

---

**3. Mảng 2 Chiều Và Hàm**

Mảng 2 chiều có thể làm tham số của hàm, tuy nhiên khi hàm có tham số là mảng 2 chiều thì bạn cần chỉ định số lượng cột của mảng 2 chiều.

Khi gọi hàm thì đối số truyền vào phải có số cột giống với số cột của mảng 2 chiều trong tham số.

**Ví dụ 1**: Hàm nhập và xuất mảng

```cpp
#include "iostream"

using namespace std;

void nhap(int a[][205], int n, int m){
    cout << "Nhap mang : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << "a[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }
    }
}

void xuat(int a[][205], int n, int m){
    cout << "Mang 2 chieu : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

int main(){
    int n, m, a[205][205];
    cout << "Nhap so hang, cot : ";
    cin >> n >> m;
    nhap(a, n, m);
    xuat(a, n, m);
    return 0;
}
```

**Ví dụ 2** : Đếm số lượng số nguyên tố trong mảng 2 chiều

```cpp
#include "iostream"
#include "math.h"

using namespace std;

bool nt(int n){
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return false;
    }
    return n > 1;
}

void nhap(int a[][205], int n, int m){
    cout << "Nhap mang : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << "a[" << i << "][" << j << "] = ";
            cin >> a[i][j];
        }
    }
}

void xuat(int a[][205], int n, int m){
    cout << "Mang 2 chieu : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

int dem(int a[][205], int n, int m){
    int ans = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(nt(a[i][j])){
                ++ans;
            }
        }
    }
    return ans;
}

int main(){
    int n, m, a[205][205];
    cout << "Nhap so hang, cot : ";
    cin >> n >> m;
    nhap(a, n, m);
    xuat(a, n, m);
    cout << "So luong so nguyen to : " << dem(a, n, m) << endl;
    return 0;
}
```

---

**Video Mảng 2 Chiều C++**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/08-01-c-ly-thuyet-mang-2-chieu-c.md](solutions/08-01-c-ly-thuyet-mang-2-chieu-c.md)

**Bài 1.** Nhập ma trận `n × m` số nguyên rồi in ra dạng bảng có căn lề.

**Bài 2.** Tính tổng, trung bình cộng tất cả phần tử của ma trận.

**Bài 3.** Tìm phần tử lớn nhất, nhỏ nhất và vị trí (hàng, cột) của chúng.

**Bài 4.** Tính tổng từng hàng và tổng từng cột, in ra dạng bảng.

**Bài 5.** Đếm số phần tử dương, âm, bằng 0 trong ma trận.

**Bài 6.** In ra các phần tử ở viền (hàng đầu, hàng cuối, cột đầu, cột cuối) của ma trận.

**Bài 7.** Khai báo ma trận theo 3 cách: khởi tạo đầy đủ, khởi tạo thiếu, khởi tạo toàn 0. In kết quả.

**Bài 8.** Chứng minh ma trận 2 chiều được lưu liên tiếp trong bộ nhớ (in địa chỉ từng phần tử).

**Bài 9.** Viết hàm nhận ma trận 2 chiều làm tham số. Giải thích vì sao phải chỉ rõ số cột.

**Bài 10.** Tìm hàng có tổng lớn nhất và cột có tổng nhỏ nhất.

**Bài 11.** Chuyển ma trận thành mảng 1 chiều và ngược lại, dùng công thức `i * m + j`.

**Bài 12.** Kiểm tra ma trận có phải ma trận đơn vị không.

**Bài 13.** Đếm số phần tử là số nguyên tố trong ma trận.

**Bài 14.** Nhập ma trận rồi in ra theo thứ tự cột (duyệt theo cột thay vì theo hàng).

**Bài 15.** So sánh 3 cách khai báo ma trận: mảng tĩnh 2 chiều, `int**` động, `vector<vector<int>>`. Lập bảng ưu nhược điểm.
