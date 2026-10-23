# [C++]. Ma Trận Và Mảng 2 Chiều C++

Mảng 2 chiều thường được sử dụng để lưu trữ dữ liệu cho các bài toán liên quan tới ma trận, trong bài viết này mình nhắc lại những khái niệm quan trọng với ma trận

**NỘI DUNG :** 

- **Ma Trận** 
- **Đường Chéo Chính, Phụ**
- **Tam Giác Trên, Dưới**
- **Ma Trận Chuyển Vị** 
- **Video Tutorial** 

---

**1. Ma Trận**

Ma trận là một khái niệm quan trọng trong môn học đại số tuyến tính nhưng nếu bạn chưa học đại số tuyến tính thì cũng không có vấn đề gì khó khăn khi tiếp cận với ma trận.

Ma trận là một bảng số gồm các hàng và các cột, ví dụ ma trận A có n hàng và m cột thì sẽ được ký hiệu : Anxm

Do đó khi cần lưu trữ ma trận trong lập trình C++ thì bạn chỉ cần sử dụng một mảng 2 chiều

Ma trận có số hàng và số cột bằng nhau gọi là ma trận vuông.

---

**2. Đường Chéo Chính, Phụ**

Trong ma trận vuông thì đường chéo chính chứa những phần tử có chỉ số hàng và cột bằng nhau

![](../images/ae06026adcd85da1.png)

**Ví dụ 1** : Liệt kê các số nguyên tố trên đường chéo chính

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

bool nt(int n){
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return false;
    }
    return n > 1;
}

int main(){
    int n = 4; //hang va cot deu la 4
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 11}
    };
    cout << "Cac so nguyen to tren duong cheo chinh : ";
    for(int i = 0; i < n; i++){
        if(nt(a[i][i])){
            cout << a[i][i] << " ";
        }
    }
    return 0;
}
```

Output :

```cpp
Cac so nguyen to tren duong cheo chinh : 3 5 11
```

Trong ma trận vuông thì đường chéo phụ chứa các phần tử như hình dưới

![](../images/175335ea815cd54f.png)

**Ví dụ 2** : Liệt kê các số nguyên tố trên đường chéo phụ

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

bool nt(int n){
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0) return false;
    }
    return n > 1;
}

int main(){
    int n = 4; //hang va cot deu la 4
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 17, 4, 1},
        {10, 2, 0, 11}
    };
    cout << "Cac so nguyen to tren duong cheo phu : ";
    for(int i = 0; i < n; i++){
        if(nt(a[i][n - i - 1])){
            cout << a[i][n - i - 1] << " ";
        }
    }
    return 0;
}
```

Output :

```cpp
Cac so nguyen to tren duong cheo phu : 7 17
```

---

**3. Tam Giác Trên, Dưới**

Tam giác dưới chứa các phần tử từ đường chéo chính đổ xuống, các phần tử màu vàng trong hình dưới

![](../images/e03d42194e80af8f.png)

**Ví dụ 1** : Tính tổng các phần tử trong tam giác dưới

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

int main(){
    int n = 4; //hang va cot deu la 4
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 17, 4, 1},
        {10, 2, 0, 11}
    };
    int tong = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j <= i; j++){
            tong += a[i][j];
        }
    }
    cout << "Tong cac so trong tam giac duoi : " << tong << endl;
    return 0;
}
```

Output :

```cpp
Tong cac so trong tam giac duoi : 57
```

Tam giác trên chứa các phần tử từ đường chéo chính đổ lên, các phần tử màu vàng trong hình dưới

![](../images/a8f26fed9242180a.png)

**Ví dụ 2** : Tính tổng các phần tử trong tam giác trên

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

int main(){
    int n = 4; //hang va cot deu la 4
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 17, 4, 1},
        {10, 2, 0, 11}
    };
    int tong = 0;
    for(int i = 0; i < n; i++){
        for(int j = i; j < n; j++){
            tong += a[i][j];
        }
    }
    cout << "Tong cac so trong tam giac tren : " << tong << endl;
    return 0;
}
```

Output :

```cpp
Tong cac so trong tam giac tren : 45
```

---

**4. Ma Trận Chuyển Vị**

Ma trận chuyển vị của ma trận A có n hàng và m cột là ma trận AT có m hàng và n cột, trong đó các phần tử ở hàng của ma trận A sẽ thành cột của của ma trận AT

![](../images/8513311f2b1371ca.png)

**Ví dụ** : In ra ma trận chuyển vị của ma trận A

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

int main(){
    int n = 3, m = 4;
    int a[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    int b[4][3];
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            b[i][j] = a[j][i];
        }
    }
    cout << "Ma tran chuyen vi : \n";
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cout << b[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output :

```cpp
Ma tran chuyen vi : 
1 5 9 
2 6 10 
3 7 11 
4 8 12
```

---

**Video Mảng 2 Chiều C++**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/08-03-c-ma-tran-va-mang-2-chieu-c.md](solutions/08-03-c-ma-tran-va-mang-2-chieu-c.md)

**Bài 1.** Tạo ma trận đơn vị kích thước `n × n` và in ra.

**Bài 2.** Tạo ma trận đường chéo với các giá trị do người dùng nhập.

**Bài 3.** Chuyển vị ma trận (transpose) — đổi hàng thành cột.

**Bài 4.** Chuyển vị ma trận vuông **tại chỗ** (không dùng ma trận phụ).

**Bài 5.** Xoay ma trận vuông 90° theo chiều kim đồng hồ.

**Bài 6.** Xoay ma trận vuông 90° ngược chiều kim đồng hồ, 180°, 270°.

**Bài 7.** Lật ma trận theo chiều ngang và theo chiều dọc.

**Bài 8.** Tính vết (trace) của ma trận — tổng các phần tử trên đường chéo chính.

**Bài 9.** Kiểm tra 2 ma trận có bằng nhau không.

**Bài 10.** Nhân ma trận với một số vô hướng (scalar).

**Bài 11.** Tạo ma trận ngẫu nhiên `n × m` với giá trị trong khoảng `[a, b]`.

**Bài 12.** Tạo ma trận tam giác Pascal dạng 2 chiều.

**Bài 13.** Kiểm tra ma trận có phải ma trận ma phương (magic square) không — tổng mọi hàng, cột, đường chéo đều bằng nhau.

**Bài 14.** Sinh ma trận ma phương bậc lẻ bằng phương pháp Siamese.

**Bài 15.** Viết một "thư viện ma trận" gồm các hàm: tạo, in, chuyển vị, xoay, so sánh, vết.
