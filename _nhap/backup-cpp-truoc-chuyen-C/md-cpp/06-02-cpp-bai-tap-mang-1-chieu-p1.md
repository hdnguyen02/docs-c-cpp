# [C++]. Bài Tập Mảng 1 Chiều P1

Bài viết này mình sẽ hướng dẫn các bạn các dạng bài tập thường gặp trên mảng 1 chiều và cách giải quyết chúng

**NỘI DUNG :** 

- **Liệt Kê Và Đếm**
- **Tìm Max, Min**
- **Mảng Đối Xứng**
- **Đếm Cặp Phần Tử**
- **Video Tutorial**

---

**1. Liệt Kê Và Đếm**

Dạng bài tập liệt kê và đếm khá đơn giản, đề bài thường yêu cầu các bạn đếm hoặc liệt kê các phần tử trong mảng thỏa mãn tính chất cho trước. Ví dụ như số nguyên tố, thuận nghịch, số chẵn, lẻ...

Để giải bài tập này bạn cần chuẩn bị hàm kiểm tra tính chất mà đề bài yêu cầu, việc cần làm còn lại chỉ cần duyệt qua từng phần tử trong mảng và kiểm tra thỏa mãn yêu cầu thì sẽ đếm hoặc liệt kê

**Bài 1** : Liệt kê các số [nguyên tố](https://blog.codelab.dev/c-so-nguyen-to) trong mảng

```cpp
#include "iostream"
#include "math.h"
using namespace std;

bool nt(int n){
   if(n < 2)
      return false;
   for(int i = 2; i <= sqrt(n); i++){
      if(n % i == 0) return false;
   }
   return true;
}

int main(){
   int n = 10;
   int a[10] = {2, 3, 19, 88, 100, 28, 47, 31, 14, 25};
   cout << "Cac so nguyen to trong day : ";
   for(int i = 0; i < n; i++){
      if(nt(a[i])){
         cout << a[i] << ' ';
      }
   }
   return 0;
}
```

Output :

```cpp
Cac so nguyen to trong day : 2 3 19 47 31
```

**Ví dụ 2** : Đếm và liệt kê các số [thuận nghịch](https://blog.codelab.dev/c-so-thuan-nghich) trong mảng

```cpp
#include "iostream"
#include "math.h"
using namespace std;

bool tn(int n){
   int rev = 0, tmp = n;
   while(n != 0){
      rev = rev * 10 + n % 10;
      n /= 10;
   }
   return rev == tmp;
}

int main(){
   int n = 10;
   int a[10] = {2222, 3, 19, 88, 12321, 28, 4774, 31, 141, 25};
   int dem = 0;
   for(int i = 0; i < n; i++){
   if(tn(a[i])){
      ++dem;
      }
   }
   cout << "So luong so thuan nghich : " << dem << endl;
   cout << "Danh sach so thuan nghich : ";
   for(int i = 0; i < n; i++){
      if(tn(a[i])){
         cout << a[i] << " ";
      }
   }
   return 0;
}
```

Output :

```cpp
So luong so thuan nghich : 6
Danh sach so thuan nghich : 2222 3 88 12321 4774 141
```

**2.Tìm Max, Min**

Để tìm phần tử lớn nhất (nhỏ nhất) trong mảng ta có thể làm như sau :

1. Giả sử phần tử đầu tiên trong mảng là lớn nhất (nhỏ nhất)
2. Duyệt các phần tử còn lại trong mảng và so sánh sau đó cập nhật giá trị cho biến lớn nhất (nhỏ nhất)

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

int main(){
    int n = 10;
    int a[10] = {2222, 3, 19, 88, 12321, 28, 4774, 31, 141, 25};
    //Khởi tạo max min là phần tử a[0]
    int max_val = a[0], min_val = a[0];
    //Duyệt và cập nhật
    for(int i = 1; i < n; i++){
        if(a[i] < min_val){
            min_val = a[i];
        }
        if(a[i] > max_val){
            max_val = a[i];
        }
    }
    cout << "So lon nhat : " << max_val << endl;
    cout << "So nho nhat : " << min_val << endl;
    return 0;
}
```

Output :

```cpp
So lon nhat : 12321
So nho nhat : 3
```

Bạn cũng có thể tìm max bằng cách khởi tạo giá trị cho biến max_val một giá trị rất nhỏ (-109) để khi duyệt qua phần tử đầu tiên trong mảng thì giá trị của biến max_val sẽ được cập nhật ngay. Ngược lại khi tìm min bạn sẽ khởi tạo giá trị của min_val là một số rất lớn (109).

Tùy thuộc vào giới hạn của đề bài để bạn có thể quyết định khởi tạo giá trị phù hợp cho max_val và min_val, max_val sẽ khởi tạo nhỏ hơn giá trị nhỏ nhất mà đề bài cho, min_val sẽ khởi tạo là số lớn hơn giá trị lớn nhất mà đề bài cho. Ví dụ đề bài cho các phần tử trong mảng thuộc [0, 106] thì max_val bạn cần khởi tạo nhỏ hơn 0 và min_val bạn cần khởi tạo lớn hơn 106.

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

#define MIN -1000000000
#define MAX 1000000000

int main(){
    int n = 10;
    int a[10] = {2222, 3, 19, 88, 12321, 28, 4774, 31, 141, 25};
    int max_val = MIN, min_val = MAX;
    //Duyệt và cập nhật
    for(int i = 0; i < n; i++){
        if(a[i] < min_val){
            min_val = a[i];
        }
        if(a[i] > max_val){
            max_val = a[i];
        }
    }
    cout << "So lon nhat : " << max_val << endl;
    cout << "So nho nhat : " << min_val << endl;
    return 0;
}
```

Output :

```cpp
So lon nhat : 12321
So nho nhat : 3
```

---

**3. Mảng Đối Xứng**

**Kiểm tra mảng đối xứng**

Để kiểm tra mảng đối xứng bạn cần xét các cặp phần tử đối xứng với nhau, nếu 2 phần tử này có giá trị khác nhau có thể kết luận luôn mảng không đối xứng.

Xét thấy phần tử có chỉ số i thì phần tử đối xứng với nó sẽ có chỉ số n - i - 1, số cặp mà bạn cần phải xét sẽ là N / 2 với N là số lượng phần tử trong mảng. Ví dụ với mảng có 6 phần tử bạn cần xét 3 cặp, 5 phần tử bạn cần xét 2 cặp vì phần tử chính giữa sẽ đối xứng với chính nó nên không cần kiểm tra.

| a | 10 | 20 | 30 | 30 | 20 | 10 |
| i | 0 | 1 | 2 | 3 | 4 | 5 |
| n - i - 1 | 5 | 4 | 3 | 2 | 1 | 0 |

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

bool doixung(int a[], int n){
    // i <=> n - i - 1
    for(int i = 0; i < n / 2; i++){
        if(a[i] != a[n - i - 1]){
            return false;
        }
    }
    return true;
}

int main(){
    int n = 10;
    int a[10] = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
    cout << "Mang a doi xung : " << boolalpha << doixung(a, n) << endl;
    int m = 5;
    int b[5] = {1, 2, 3, 2, 3};
    cout << "Mang b doi xung : " << boolalpha << doixung(b, m) << endl;
    return 0;
}
```

Output :

```cpp
Mang a doi xung : true
Mang b doi xung : false
```

**Lật ngược mảng**

Bạn cũng có thể sử dụng code trên để lật ngược một mảng, bạn sẽ xét từng cặp phần tử trong mảng và hoán đối giá trị.

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

void reverse(int a[], int n){
    // i <=> n - i - 1
    for(int i = 0; i < n / 2; i++){
        //hoan doi gia tri a[i], a[n - i - 1]
        int tmp = a[i];
        a[i] = a[n - i - 1];
        a[n - i - 1] = tmp;
    }
}

int main(){
    int n = 10;
    int a[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    reverse(a, 10);
    cout << "Mang sau khi lat : \n";
    for(int i = 0; i < n; i++){
        cout << a[i] << ' ';
    }
    return 0;
}
```

Output :

```cpp
Mang sau khi lat : 
10 9 8 7 6 5 4 3 2 1
```

---

**4. Đếm Cặp Phần Tử**

Dạng bài tập này sẽ yêu cầu các bạn xét tất cả các cặp phần tử trong mảng A[] có N phần tử và kiểm tra tính chất của các cặp này, ví dụ đếm số cặp phần tử nguyên tố cùng nhau trong mảng, đếm cặp số có tổng bằng K ...

**Thuật toán :** 

1. Duyệt qua các chỉ số i từ 0 tới N - 2
2. Đối với mỗi chỉ số i sẽ xét các chỉ số j từ i + 1 tới N - 1
3. Xét cặp A[i], A[j]

Ví dụ mảng A[] = {3, 8, 9, 1, 10}

1. i = 0 : j = 1, 2, 3, 4 ta sẽ có các cặp A[i], A[j] lần lượt là (3, 8), (3, 9), (3, 1), (3, 10)
2. i = 1 : j = 2, 3, 4 ta sẽ có các cặp A[i], A[j] lần lượt là (8, 9), (8, 1), (8, 10)
3. i = 2 : j = 3, 4 ta sẽ có các cặp A[i], A[j] lần lượt là (9, 1), (9, 10)
4. i = 3 : j = 4 ta sẽ có các cặp A[i], A[j] lần lượt là (1, 10)

**Bài 1** : Liệt kê các cặp có tổng bằng K cho trước

```cpp
#include "iostream"
#include "math.h"
using namespace std;

int main(){
    int n = 10, k = 10;
    int a[10] = {2, 3, 5, 9, 1, 7, 4, 6, 3, 2};
    for(int i = 0; i < n - 1; i++){
        //a[i] 
        for(int j = i + 1; j < n; j++){
            if(a[i] + a[j] == k){
                cout << a[i] << " " << a[j] << endl;
            }
        }
    }
    return 0;
}
```

Output :

```cpp
(3, 7)
(9, 1)
(7, 3)
(4, 6)
```

**Bài 2** : Đếm số cặp nguyên tố cùng nhau trong mảng

**Chú ý** : 2 số nguyên tố cùng nhau là 2 số có [ước chung lớn nhất](https://blog.codelab.dev/c-uoc-chung-lon-nhat-boi-chung-nho-nhat) bằng 1.

```cpp
#include "iostream"
#include "math.h"
using namespace std;

int ucln(int a, int b){
    while(b != 0){
        int r = a % b;
        a = b; 
        b = r;
    }
    return a;
}

int main(){
    int n = 10;
    int a[10] = {2, 4, 6, 8, 5, 18, 20, 14, 10, 100};
    cout << "Cap so nguyen to cung nhau : \n";
    for(int i = 0; i < n - 1; i++){
        //a[i] 
        for(int j = i + 1; j < n; j++){
            if(ucln(a[i], a[j]) == 1){
                cout << a[i] << " " << a[j] << endl;
            }
        }
    }
    return 0;
}
```

Output :

```cpp
Cap so nguyen to cung nhau : 
2 5
4 5
6 5
8 5
5 18
5 14
```

---

**Video Bài Tập Mảng 1 Chiều**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/06-02-cpp-bai-tap-mang-1-chieu-p1.md](solutions/06-02-cpp-bai-tap-mang-1-chieu-p1.md)

**Bài 1.** Nhập mảng `n` số nguyên. Tính tổng các phần tử có giá trị lớn hơn trung bình cộng của mảng.

**Bài 2.** Tìm phần tử xuất hiện nhiều nhất trong mảng và số lần xuất hiện của nó.

**Bài 3.** Kiểm tra mảng có chứa phần tử trùng lặp hay không.

**Bài 4.** Tách mảng thành 2 mảng con: mảng số chẵn và mảng số lẻ, rồi in ra.

**Bài 5.** Tìm dãy con liên tiếp dài nhất gồm các phần tử tăng dần.

**Bài 6.** Tính tổng lớn nhất của một dãy con liên tiếp (bài toán Kadane).

**Bài 7.** Xoay mảng sang phải `k` vị trí (ví dụ `[1,2,3,4,5]` với `k=2` → `[4,5,1,2,3]`).

**Bài 8.** Gộp 2 mảng đã sắp xếp thành một mảng sắp xếp (không dùng `sort`).

**Bài 9.** Tìm 2 phần tử trong mảng có tổng bằng `x` cho trước.

**Bài 10.** Tìm phần tử "đỉnh" — phần tử lớn hơn cả 2 phần tử kề nó.

**Bài 11.** Dịch chuyển tất cả số 0 về cuối mảng, giữ nguyên thứ tự các phần tử khác.

**Bài 12.** Tìm khoảng cách lớn nhất giữa 2 phần tử bằng nhau trong mảng.

**Bài 13.** Cho mảng chứa các số từ 1 đến `n` nhưng thiếu đúng 1 số. Tìm số bị thiếu (không dùng mảng phụ).

**Bài 14.** Kiểm tra mảng có phải hoán vị của `1..n` không.

**Bài 15.** Nhập mảng, tìm tất cả các "điểm cân bằng" — vị trí mà tổng bên trái bằng tổng bên phải.
