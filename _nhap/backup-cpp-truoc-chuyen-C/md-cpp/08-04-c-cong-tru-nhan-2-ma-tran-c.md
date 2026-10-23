# [C++]. Cộng, Trừ, Nhân 2 Ma Trận C++

Trong bài viết này mình sẽ hướng dẫn các bạn các phép toán trên ma trận bao gồm : Cộng, trừ và nhân 2 ma trận

**NỘI DUNG :** 

- **Cộng, Trừ 2 Ma Trận**
- **Nhân 2 Ma Trận**
- **Video Tutorial** 

---

**1. Cộng, Trừ 2 Ma Trận**

Điều kiện để 2 ma trận có thể cộng trừ với nhau đó là chúng cần có cùng số hàng và cột.

Giả sử cần cộng 2 ma trận A và B có cùng hàng và cột để tạo ra ma trận tổng C thì C[i][j] = A[i][j] + B[i][j]

![](../images/7b8e1eda687bdf0e.png)

Phép trừ 2 ma trận thì bạn làm tương tự

![](../images/6a32aca3fe05e41b.png)

**Code :** 

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

int main(){
    int n = 3, m = 4;
    int a[3][4] = {
        {2, 3, 1, 4},
        {2, 2, 0, 7},
        {1, 3, 5, 1}
    };
    int b[3][4] = {
        {2, 0, 7, 8},
        {1, 3, 5, 2},
        {3, 2, 8, 1}
    };
    int tong[3][4], hieu[3][4];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            tong[i][j] = a[i][j] + b[i][j];
            hieu[i][j] = a[i][j] - b[i][j];
        }
    }
    printf("Tong 2 ma tran : \n");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << tong[i][j] << " ";
        }
        cout << endl;
    }
    printf("Hieu 2 ma tran : \n");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << hieu[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output :

```cpp
Tong 2 ma tran : 
4 3 8 12 
3 5 5 9 
4 5 13 2 
Hieu 2 ma tran : 
0 3 -6 -4 
1 -1 -5 5 
-2 1 -3 0
```

---

**2. Nhân 2 Ma Trận**

Giả sử bạn cần nhân ma trận **A[n][m]** với ma trận **B[p][q]** thì điều kiện để xảy ra phép nhân ma trận đó là : Số cột của ma trận A bằng số hàng của ma trận B

Tức là m phải bằng p, khi đó ma trận tích sẽ có cỡ **C[n][q]**

Ví dụ :

A[3][4] x B[4][2] = C[3][2]

A[3][4] x B[4][5] = C[3][5]

A[2][4] X B[2][3] = Không xảy ra

![](../images/ac6645dafcc5faae.png)

Để tạo ra ma trận tích C thì **C[i][j] = ∑A[i][k] * B[k][j] **với k chạy từ 0 tới m (p)

Hiểu đơn giản thì khi tích phần tử C[i][j] bạn sẽ nhân lần lượt các phần tử ở hàng i của ma trận A với các phần tử ở cột j của ma trận b sau đó cộng dồn lại

**Code :** 

```cpp
#include "iostream"
#include "math.h"
#include "algorithm"

using namespace std;

int main(){
    int n = 2, m = 3, q = 2;
    //a[n][m], b[m][q]
    int a[n][m] = {
        {1, 2, 3},
        {4, 5, 6}
    };
    int b[m][q] = {
        {10, 11},
        {20, 22},
        {30, 33}
    };
    int c[n][q];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < q; j++){
            c[i][j] = 0;
            for(int k = 0; k < m; k++){
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    cout << "Tich 2 ma tran : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < q; j++){
            cout << c[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output :

```cpp
Tich 2 ma tran : 
140 154 
320 352
```

---

**Video Mảng 2 Chiều C++**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/08-04-c-cong-tru-nhan-2-ma-tran-c.md](solutions/08-04-c-cong-tru-nhan-2-ma-tran-c.md)

**Bài 1.** Viết hàm cộng 2 ma trận cùng kích thước.

**Bài 2.** Viết hàm trừ 2 ma trận cùng kích thước.

**Bài 3.** Viết hàm nhân 2 ma trận `A(n×m)` và `B(m×p)`.

**Bài 4.** Kiểm tra điều kiện để 2 ma trận cộng được và nhân được. Viết hàm kiểm tra.

**Bài 5.** Chứng minh bằng chương trình rằng phép nhân ma trận **không giao hoán** (`A×B ≠ B×A`).

**Bài 6.** Chứng minh `A × I = I × A = A` với `I` là ma trận đơn vị.

**Bài 7.** Tính luỹ thừa ma trận `A^k` bằng cách nhân lặp.

**Bài 8.** Tính `A^k` bằng luỹ thừa nhị phân (nhanh hơn nhiều khi `k` lớn).

**Bài 9.** Dùng luỹ thừa ma trận tính số Fibonacci thứ `n` với độ phức tạp O(log n).

**Bài 10.** Đếm số phép nhân cần thực hiện khi nhân 2 ma trận `n×n`. So sánh với `n³`.

**Bài 11.** Tính định thức ma trận 2×2 và 3×3 bằng công thức.

**Bài 12.** Tính định thức ma trận `n×n` bằng khử Gauss.

**Bài 13.** Kiểm tra `(A + B)ᵀ = Aᵀ + Bᵀ` và `(A × B)ᵀ = Bᵀ × Aᵀ` bằng chương trình.

**Bài 14.** Viết chương trình giải hệ phương trình tuyến tính 3 ẩn bằng quy tắc Cramer.

**Bài 15.** Mở rộng thư viện ma trận ở bài 08-03 thêm các hàm cộng, trừ, nhân, luỹ thừa, định thức.
