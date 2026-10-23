# [C++]. Bài Tập Về Dãy Số

Bài tập về dãy số là dạng bài tập gây nhiều khó khăn cho các bạn mới học, trong bài viết này mình sẽ hướng dẫn các bạn những bài tập về dãy số thường gặp.

**NỘI DUNG :** 

- **Dãy Con Cỡ K Có Tổng Lớn Nhất**
- **Dãy Con Giống Nhau Dài Nhất**
- **Dãy Con Khác Nhau Dài Nhất**
- **Kiểm Tra Mảng Tăng Dần**
- **Dãy Nguyên Tố Dài Nhất**
- **Video Tutorial**

**1. Dãy Con Cỡ K có Tổng Lớn Nhất**

Cho mảng A[] gồm N phần tử và số nguyên K, bạn hãy tính tổng các dãy con liên tiếp có K phần tử của mảng A[] và in ra màn hình

Ví dụ A[] = {3, 2, 1, 5, 6, 7, 2} và K = 3 các bạn sẽ có các dãy con : {3, 2,1}, {2, 1, 5}, {1, 5, 6}, {5, 6, 7}, {6, 7, 2}

**Thuật toán :** 

1. Duyệt các chỉ số i từ 0 tới N - K đại diện cho phần tử đầu tiên của dãy con
2. Tính tổng K phần tử liên tiếp từ chỉ số i và in ra màn hình

**Code :** 

```cpp
#include "iostream"
using namespace std;

int main(){
    int n = 7, k = 3;
    int a[7] = {3, 2, 1, 5, 6, 7, 2};
    int tong = 0;
    for(int i = 0; i <= n - k; i++){
        //reset giá trị của tổng ở mỗi dãy con
        tong = 0;
        for(int j = 0; j < k; j++){
            tong += a[i + j];
        }
        cout << "Tong day con bat dau tu chi so " << i << " : " << tong << endl;
    }
    return 0;
}
```

Output :

```cpp
Tong day con bat dau tu chi so 0 : 6
Tong day con bat dau tu chi so 1 : 8
Tong day con bat dau tu chi so 2 : 12
Tong day con bat dau tu chi so 3 : 18
Tong day con bat dau tu chi so 4 : 15
```

**2. Dãy Con Giống Nhau Dài Nhất**

Cho mảng A[] gồm N phần tử bạn hãy tìm độ dài của dãy con chứa các phần tử giống nhau dài nhất.

Ví dụ A[] = {1, 2, 2, 2, 3, 3, 5, 4, 4, 4, 4, 2} thì dãy con {4, 4, 4, 4} là dãy con dài nhất chứa các phần tử giống nhau

**Thuật toán :** 

1. Khởi tạo 1 biến đếm bằng 1 đại diện cho A[0]
2. Duyệt từ chỉ số 1 tới N - 1 và so sánh A[i] với A[i - 1]
3. Nếu A[i] = A[i - 1] thì tăng biến đếm
4. Nếu A[i] != A[i - 1] thì cập nhật kết quả thông qua biến đếm sau đó reset biến đếm về 1 để đếm lại dãy con bắt đầu từ A[i]

**Code :** 

```cpp
#include "iostream"
using namespace std;

int main(){
    int n = 12;
    int a[12] = {1, 2, 2, 2, 3, 3, 5, 4, 4, 4, 4, 2};
    int dem = 1, res = 1;
    for(int i = 1; i < n; i++){
        if(a[i] == a[i - 1]){
            ++dem;
        }
        else{
            if(res < dem){
                res = dem;
            }
            dem = 1;
        }
    }
    //Chú ý cập nhật dãy con dài nhất kết thúc tại A[n - 1]
    if(dem > res){
        res = dem;
    }
    cout << "Day co giong nhau dai nhat : " << res << endl;
    return 0;
}
```

Output :

```cpp
Day co giong nhau dai nhat : 4
```

Bạn thử làm thêm yêu cầu liệt kê tất cả các dãy con giống nhau dài nhất, ví dụ A[] = {1, 2, 2, 2, 3, 3, 5, 4, 4, 4, 3, 2} thì có 2 dãy con thỏa mãn là {2, 2, 2} và {4, 4, 4}

---

**3.Dãy Con Khác Nhau Dài Nhất**

Cho mảng A[] gồm N phần tử bạn hãy tìm độ dài lớn nhất của dãy con chứa các phần tử sao cho không có hai phần tử liền kề nào giống nhau.

Ví dụ A[] = {1, 2, 3, 2, 3, 3, 5, 4, 4, 4, 4, 2} thì dãy con {1, 2, 3, 2, 3} là dãy con cần tìm

**Thuật toán :** 

1. Khởi tạo 1 biến đếm bằng 1 đại diện cho A[0]
2. Duyệt từ chỉ số 1 tới N - 1 và so sánh A[i] với A[i - 1]
3. Nếu A[i] != A[i - 1] thì tăng biến đếm
4. Nếu A[i] = A[i - 1] thì cập nhật kết quả thông qua biến đếm sau đó reset biến đếm về 1 để đếm lại dãy con bắt đầu từ A[i]

**Code :** 

```cpp
#include "iostream"
using namespace std;

int main(){
    int n = 12;
    int a[12] = {1, 2, 3, 2, 3, 3, 5, 4, 4, 4, 4, 2};
    int dem = 1, res = 1;
    for(int i = 1; i < n; i++){
        if(a[i] != a[i - 1]){
            ++dem;
        }
        else{
            if(res < dem){
                res = dem;
            }
            dem = 1;
        }
    }
    //Chú ý cập nhật dãy con dài nhất kết thúc tại A[n - 1]
    if(dem > res){
        res = dem;
    }
    cout << "Day con lien ke khac nhau dai nhat : " << res << endl;
    return 0;
}
```

Output :

```cpp
Day con lien ke khac nhau dai nhat : 5
```

---

**4. Kiểm Tra Mảng Tăng Dần**

Bài toán yêu cầu bạn kiểm tra mảng A[] có N phần tử đã cho có tăng dần (giảm dần hay không), mảng tăng dần thỏa mãn yêu cầu phần tử đứng sau lớn hơn hoặc bằng phần tử đứng ngay trước nó.

Ví dụ A[] = {1, 2, 2, 3, 4, 5} là mảng tăng dần

**Thuật toán :** 

Xét N - 1 cặp phần tử đứng cạnh nhau, nếu N - 1 cặp phần tử này đều thỏa mãn phần tử đứng sau A[i] lớn hơn hoặc bằng phần tử ngay trước nó là A[i - 1] thì mảng tăng dần

Chú ý không cần kiểm tra A[0] và phần tử đứng trước nó.

**Code :** 

```cpp
#include "iostream"
using namespace std;

bool check(int a[], int n){
    for(int i = 1; i < n; i++){
        if(a[i] < a[i - 1]){
            return false;
        }
    }
    return true;
}

int main(){
    int n = 6;
    int a[6] = {1, 2, 2, 3, 4, 5};
    if(check(a, n)){
        cout << "Mang tang dan\n";
    }
    else{
        cout << "Mang khong tang dan\n";
    }
    return 0;
}
```

Output :

```cpp
Mang tang dan
```

---

**5. Dãy Nguyên Tố Dài Nhất**

Cho mảng A[] gồm N phần tử, hãy in ra dãy con dài nhất chứa toàn số nguyên tố, nếu có nhiều dãy con thỏa mãn thì chọn ra dãy con có tổng lớn nhất và xuất hiện đầu tiên.

Ví dụ A[] = {2, 3, 5, 8, 7, 11, 19, 4, 10, 23, 5} thì dãy con {7, 11, 19} có độ dài 3 và có tổng lớn nhất.

**Thuật toán :** 

1. Khởi tạo 1 biến đếm bằng 0 và một biến tổng bằng 0
2. Duyệt qua các phần tử A[i] trong mảng từ chỉ số 0 tới N - 1
3. Nếu phần tử A[i] là số nguyên tố thì tăng biến đếm và cộng thêm A[i] vào biến tổng
4. Nếu phần tử A[i] không phải là số nguyên tố thì cập nhật kết quả, sau đó reset biến đếm về 0 và tổng về 0

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

bool prime(int n){
    if(n < 2){
        return false;
    }
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

int main(){
    int n = 11;
    int a[11] = {2, 3, 5, 8, 7, 11, 19, 4, 10, 23, 5};
    int dem = 0, tong = 0;
    int res_dem = 0, res_tong = 0, start = -1;
    for(int i = 0; i < n; i++){
        if(prime(a[i])){
            ++dem;
            tong += a[i];
        }
        else{
            if(dem > res_dem){
                res_dem = dem;
                res_tong = tong;
                start = i - res_dem;
            }
            else if(dem == res_dem){
                if(tong > res_tong){
                    res_tong = tong;
                    start = i - res_dem;
                }
            }
            dem = 0; tong = 0;
        }
    }
    //cap nhat day con ket thuc tai a[n - 1]
    if(dem > res_dem){
        res_dem = dem;
        res_tong = tong;
        start = n - res_dem;
    }
    else if(dem == res_dem){
        if(tong > res_tong){
            res_tong = tong;
            start = n - res_dem;
        }
    }
    if(start == -1){
        cout << "Mang khong chua so nguyen to !\n";
    }
    else{
        for(int i = 0; i < res_dem; i++){
            cout << a[i + start] << ' ';
        }
    }
    return 0;
}
```

Output :

```cpp
7 11 19
```

---

**Video Bài Tập Mảng 1 Chiều**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/06-04-cpp-bai-tap-ve-day-so.md](solutions/06-04-cpp-bai-tap-ve-day-so.md)

**Bài 1.** In ra `n` số hạng đầu tiên của dãy `a[i] = i² + 1`.

**Bài 2.** In ra `n` số hạng của dãy truy hồi `a[1] = 1`, `a[i] = 2·a[i−1] + 3`.

**Bài 3.** Dãy Tribonacci: `T[0]=T[1]=0`, `T[2]=1`, `T[n] = T[n−1]+T[n−2]+T[n−3]`. In `n` số đầu.

**Bài 4.** Dãy Catalan: `C[0]=1`, `C[n] = Σ C[i]·C[n−1−i]`. In 15 số đầu.

**Bài 5.** In ra `n` số nguyên tố đầu tiên.

**Bài 6.** In ra `n` số chính phương đầu tiên và tổng của chúng.

**Bài 7.** In ra `n` số hoàn hảo đầu tiên.

**Bài 8.** Dãy Collatz: bắt đầu từ `n`, nếu chẵn chia 2, nếu lẻ nhân 3 cộng 1, lặp tới khi bằng 1. In toàn dãy và độ dài.

**Bài 9.** Tìm số `n` trong khoảng [1, 1000] có dãy Collatz dài nhất.

**Bài 10.** In ra `n` số hạng đầu của dãy `1, 11, 111, 1111, ...`

**Bài 11.** Dãy Look-and-Say: `1, 11, 21, 1211, 111221, ...` In `n` số hạng đầu.

**Bài 12.** Tìm số hạng thứ `n` của dãy số nguyên tố sinh đôi (cặp `p`, `p+2` đều nguyên tố).

**Bài 13.** Kiểm tra một dãy có phải cấp số cộng hay cấp số nhân không.

**Bài 14.** Cho dãy số, tìm số hạng tổng quát nếu nó là cấp số cộng hoặc cấp số nhân.

**Bài 15.** In tam giác số: dòng `i` chứa các số từ `1` đến `i`, rồi biến thể dòng `i` chứa `i` số liên tiếp bắt đầu từ số cuối dòng trước.
