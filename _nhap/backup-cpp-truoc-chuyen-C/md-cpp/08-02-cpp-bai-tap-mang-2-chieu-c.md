# [C++]. Bài Tập Mảng 2 Chiều C++

Bài viết này mình sẽ hướng dẫn các bạn những bài toán thường gặp trên mảng 2 chiều

**NỘI DUNG :** 

- **Bài Toán Liệt Kê**
- **Bài Toán Xét Hàng, Cột** 
- **Hoán Vị Hàng, Cột**
- **Sắp Xếp Ma Trận Theo Hàng, Cột**
- **Video Tutorial** 

---

**1. Bài Toán Liệt Kê**

Dạng bài này thường yêu cầu bạn đếm hoặc liệt kê các phần tử trong mảng 2 chiều thỏa mãn tính chất cho trước như : số nguyên tố, thuận nghịch, hoàn hảo, fibonacci...

Đối với dạng bài tập này bạn chỉ cần biết duyệt mảng 2 chiều là có thể làm được.

**Ví dụ 1** : Tìm phần tử nhỏ nhất, lớn nhất trong mảng 2 chiều

```cpp
#include "iostream"
#include "math.h"

using namespace std;

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    int min_val = 1000000000, max_val = -1000000000;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(a[i][j] > max_val){
                max_val = a[i][j];
            }
            if(a[i][j] < min_val){
                min_val = a[i][j];
            }
        }
    }
    cout << "Gia tri nho nhat : " << min_val << endl;
    cout << "Gia tri lon nhat : " << max_val << endl;
    return 0;
}
```

Output :

```cpp
Gia tri nho nhat : 0
Gia tri lon nhat : 10
```

**Ví dụ 2** : Liệt kê các số Fibonacci trong mảng 2 chiều

```cpp
#include "iostream"
#include "math.h"

using namespace std;

bool fibo(long long n){
    long long F[100];
    F[0] = 0; F[1] = 1;
    for(int i = 2; i <= 92; i++){
        F[i] = F[i - 1] + F[i - 2];
    }
    for(int i = 0; i <= 92; i++){
        if(n == F[i]) return true;
    }
    return false;
}

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    cout << "Cac so fibonacci : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(fibo(a[i][j])){
                cout << a[i][j] << " ";
            }
        }
    }
    return 0;
}
```

Output :

```cpp
Cac so fibonacci : 
3 1 0 2 5 3 3 1 2 0 3
```

---

**2. Bài Toán Xét Hàng, Cột**

Dạng bài tập này thường yêu cầu các bạn xét từng hàng hoặc từng cột của mảng 2 chiều.

Đối với bài toán xét theo hàng bạn duyệt như bình thường còn đối với bài toán duyệt theo cột thì bạn cần để vòng for ngoài duyệt theo cột và vòng for con bên trong duyệt theo hàng.

**Ví dụ 1** : Tính tổng từng hàng, từng cột của mảng 2 chiều

```cpp
#include "iostream"
#include "math.h"

using namespace std;

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    //Duyệt theo hàng, i là hàng, j là cột
    for(int i = 0; i < n; i++){
        int tong = 0;
        for(int j = 0; j < m; j++){
            tong += a[i][j];
        }
        cout << "Tong hang " << i + 1 << " : " << tong << endl;
    }
    //Duyệt theo cột, i là cột, j là hàng
    for(int i = 0; i < m; i++){
        int tong = 0;
        for(int j = 0; j < n; j++){
            tong += a[j][i];
        }
        cout << "Tong cot " << i + 1 << " : " << tong << endl;
    }
    return 0;
}
```

Output :

```cpp
Tong hang 1 : 11
Tong hang 2 : 20
Tong hang 3 : 15
Tong hang 4 : 15
Tong cot 1 : 18
Tong cot 2 : 15
Tong cot 3 : 14
Tong cot 4 : 14
```

**Ví dụ 2** : Tìm hàng có nhiều số nguyên tố nhất

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

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    //Duyệt theo hàng, i là hàng, j là cột
    int res = 0, hang = -1;
    for(int i = 0; i < n; i++){
        int dem = 0;
        for(int j = 0; j < m; j++){
            if(nt(a[i][j])){
                ++dem;
            }
        }
        if(dem > res){
            res = dem; hang = i;
        }
    }
    cout << "Hang " << hang << " co nhieu so nguyen to nhat\n";
    cout << "So luong so nguyen to : " << res << endl;
    return 0;
}
```

Output :

```cpp
Hang 1 co nhieu so nguyen to nhat
So luong so nguyen to : 3
```

**Ví dụ 3** : Tìm cột có nhiều số nguyên tố nhất, nếu có nhiều cột có cùng số nguyên tố thì chọn cột có số thứ tự lớn hơn

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

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    //Duyệt theo hàng, i là hàng, j là cột
    int res = 0, cot = -1;
    for(int i = 0; i < m; i++){
        int dem = 0;
        for(int j = 0; j < n; j++){
            if(nt(a[j][i])){
                ++dem;
            }
        }
        if(dem >= res){
            res = dem; cot = i;
        }
    }
    cout << "Cot " << cot << " co nhieu so nguyen to nhat\n";
    cout << "So luong so nguyen to : " << res << endl;
    return 0;
}
```

Output :

```cpp
Cot 3 co nhieu so nguyen to nhat
So luong so nguyen to : 3
```

---

**3. Hoán Vị Hàng, Cột**

Để hoán vị 2 hàng của mảng 2 chiều thì bạn duyệt qua từng cột còn để hoán vị 2 cột thì bạn lại duyệt qua từng hàng.

**Ví dụ 1** : Bài toán hoán vị 2 hàng

```cpp
#include "iostream"
#include "math.h"

using namespace std;

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    int h1 = 0, h2 = 3;
    for(int i = 0; i < m; i++){
        //a[h1][i] va a[h2][i]
        swap(a[h1][i], a[h2][i]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output :

```cpp
10 2 0 3 
2 5 10 3 
3 7 4 1 
3 1 0 7
```

**Ví dụ 2** : Bài toán hoán vị 2 cột

```cpp
#include "iostream"
#include "math.h"

using namespace std;

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    int c1 = 0, c2 = 3;
    for(int i = 0; i < n; i++){
        //a[i][c1] va a[i][c2]
        swap(a[i][c1], a[i][c2]);
    }
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output :

```cpp
7 1 0 3 
3 5 10 2 
1 7 4 3 
3 2 0 10
```

---

**4. Sắp Xếp Ma Trận Theo Hàng, Cột**

**Sắp xếp theo hàng** 

Sắp xếp theo hàng trên ma trận thì bạn có thể tự code một hàm sắp xếp mảng 1 chiều sau đó áp dụng với từng hàng của mảng 2 chiều.

Như mình có nhắc ở phần lý thuyết mảng 2 chiều thì mảng 2 chiều thực chất chính là 1 mảng các mảng 1 chiều, mỗi dòng trên mảng 2 chiều chính là 1 mảng 1 chiều.

**Cách 1** : Sắp xếp hàng bằng hàm sort()

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int main(){
    int n = 4, m = 4;
    int a[4][4] = {
        {3, 1, 0, 7},
        {2, 5, 10, 3},
        {3, 7, 4, 1},
        {10, 2, 0, 3}
    };
    for(int i = 0; i < n; i++){
        sort(a[i], a[i] + m);
    }
    cout << "Mang 2 chieu sap xep theo hang : \n";
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
```

Output :

```cpp
Mang 2 chieu sap xep theo hang : 
0 1 3 7 
2 3 5 10 
1 3 4 7 
0 2 3 10
```

---

**Video Mảng 2 Chiều C++**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/08-02-cpp-bai-tap-mang-2-chieu-c.md](solutions/08-02-cpp-bai-tap-mang-2-chieu-c.md)

**Bài 1.** Tính tổng các phần tử trên đường chéo chính và đường chéo phụ của ma trận vuông.

**Bài 2.** Tính tổng các phần tử nằm phía trên và phía dưới đường chéo chính.

**Bài 3.** Kiểm tra ma trận có đối xứng qua đường chéo chính không.

**Bài 4.** Hoán đổi 2 hàng bất kỳ, 2 cột bất kỳ của ma trận.

**Bài 5.** Sắp xếp các phần tử của ma trận tăng dần theo thứ tự duyệt hàng.

**Bài 6.** Sắp xếp từng hàng của ma trận tăng dần.

**Bài 7.** Tìm hàng có nhiều số nguyên tố nhất.

**Bài 8.** Tìm phần tử "yên ngựa" — nhỏ nhất trên hàng của nó và lớn nhất trên cột của nó.

**Bài 9.** Xoá một hàng và một cột khỏi ma trận.

**Bài 10.** Chèn một hàng mới vào ma trận tại vị trí `k`.

**Bài 11.** Kiểm tra ma trận có phải ma trận tam giác trên / tam giác dưới không.

**Bài 12.** Đếm số vùng liên thông các ô có giá trị 1 trong ma trận nhị phân (dùng DFS).

**Bài 13.** Tìm hình chữ nhật con có tổng lớn nhất trong ma trận (`n, m ≤ 50`).

**Bài 14.** Cho ma trận, tìm đường đi từ góc trên trái xuống góc dưới phải có tổng nhỏ nhất (chỉ đi xuống hoặc sang phải).

**Bài 15.** Cài đặt trò chơi "Dò mìn": ma trận có các quả mìn, tính số mìn xung quanh mỗi ô.
