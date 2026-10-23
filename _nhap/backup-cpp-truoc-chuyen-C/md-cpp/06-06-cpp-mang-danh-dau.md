# [C++]. Mảng Đánh Dấu

Mảng đánh dấu là cái tên mình nghĩ ra cho kỹ thuật này, nó còn được gọi cái tên khác là "lùa bò vào chuồng". Đây là một kỹ thuật cực kỳ hay và tối ưu mà các bạn nên nắm được

**NỘI DUNG :** 

- **Lý Thuyết Mảng Đánh Dấu**
- **Bài Toán Liệt Kê Giá Trị Khác Nhau**
- **Bài Toán Tần Suất**
- **Video Tutorial**

---

**1. Lý Thuyết Mảng Đánh Dấu**

**Bài Toán** : Cho mảng A[] gồm N phần tử là các số nguyên trong đoạn [0, 106]. Hãy đếm các giá trị khác nhau trong mảng ?

Mình đã hướng dẫn các bạn cách sử dụng 2 vòng for lồng nhau để giải quyết bài toán trên, nếu bạn chưa biết cách làm đó có thể tham khảo [tại đây](https://blog.codelab.dev/c-bai-tap-mang-1-chieu-p2)

Để giải quyết bài toán trên bạn có thể dùng 1 mảng đánh dấu đủ lớn để đánh dấu sự xuất các giá trị trong mảng, vì các phần tử trong mảng đều nằm trong đoạn từ [0, 106] nên chỉ cần dùng một mảng số nguyên mà chỉ số của nó có thể đánh dấu được hết các giá trị [0, 106] là giải quyết được bài toán.

Ý tưởng ở đây đó là bạn sẽ sử dụng chỉ số của mảng đánh dấu để đánh dấu giá trị tương ứng với chỉ số đó đã xuất hiện trong mảng. Ban đầu tất cả các phần tử trong mảng đánh dấu có giá trị là 0, khi bạn gặp một giá trị trong mảng thì sẽ chuyển phần tử trong mảng đánh dấu tại chỉ số đó thành 1.

Ví dụ mảng đánh dấu là mark[] và khi gặp phần tử trong mảng A[] là 3 thì mark[3] = 1

Sau khi đánh dấu xong các giá trị xuất hiện thì bạn chỉ cần duyệt mảng đánh dấu và xem phần tử nào trong mảng đánh dấu có giá trị là 1 để đếm hoặc liệt kê.

**Code** :

```cpp
#include "iostream"
#include "math.h"
using namespace std;

//Chỉ số của mark là từ 0 tới 10^6, ban đầu toàn bộ mảng mark[] = 0

int mark[1000001]; 

int main(){
    int n = 8;
    int a[8] = {3, 1, 3, 0, 2, 4, 1, 6};
    //đánh dấu
    for(int i = 0; i < n; i++){
        //Lấy a[i] làm chỉ số và chuyển mark[a[i]] = 1
        mark[a[i]] = 1;
    }
    int dem = 0;
    //Bạn có thể duyệt từ i = 0 tới giá trị max trong mảng cũng được
    for(int i = 0; i <= 1000000; i++){
        if(mark[i] == 1){
            ++dem;
        }
    }
    cout << "So luong phan tu khac nhau : " << dem << endl;
    return 0;
}
```

Output :

```cpp
So luong phan tu khac nhau : 6
```

**Giải thích :**

Mảng mark ban đầu :

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ....... |
| mark[i] | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0..... |

i = 0, a[i] = 3, mark[3] = 1

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ....... |
| mark[i] | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0..... |

i = 1, a[i] = 1, mark[1] = 1

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ....... |
| mark[i] | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0..... |

i = 2, a[i] = 3, mark[3] = 1

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ....... |
| mark[i] | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0..... |

....

i = 7, a[i] = 6, mark[6] = 1

| i | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ....... |
| mark[i] | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0..... |

**Chú ý khi sử dụng mảng đánh dấu :** 

- Mảng đánh dấu không thể sử dụng được với số âm, vì chỉ số trong mảng không thể là số âm
- Mảng đánh dấu không sử dụng được khi giá trị cần đánh dấu vượt chỉ số của mảng mà bạn có thể khai báo
- Thông thường bạn chỉ áp dụng được kỹ thuật này khi các phần tử trong mảng có giá trị trong đoạn [0, 107]
- Chú ý sử dụng mảng đánh dấu đủ lớn để không lỗi bộ nhớ, ví dụ bạn cần đánh dấu các phần tử trong đoạn [0, 103] thì mảng cỡ 1001 là đủ rồi, hoặc có thể lớn hơn

---

**2.Bài Toán Liệt Kê Giá Trị Khác Nhau**

**Bài Toán 1** : Cho mảng A[] gồm N phần tử là số nguyên trong đoạn [0, 106], hãy liệt kê các giá trị khác nhau trong mảng theo thứ tự từ nhỏ tới lớn

Ý tưởng là sử dụng mảng đánh dấu sau đó liệt kê các số từ nhỏ tới lớn xuất hiện trong mảng và in ra nếu giá trị đó được đánh dấu.

**Code :**

```cpp
#include "iostream"
#include "math.h"
using namespace std;

int mark[1000001]; 

int main(){
    int n = 10;
    int a[10] = {3, 1, 3, 0, 2, 4, 1, 14, 12, 7};
    //đánh dấu
    int max_val = -1000000000;
    for(int i = 0; i < n; i++){
        //Lấy a[i] làm chỉ số và chuyển mark[a[i]] = 11
        mark[a[i]] = 1;
        if(a[i] > max_val){
            max_val = a[i];
        }
    }
    cout << "Cac gia tri khac nhau trong mang : ";
    for(int i = 0; i <= max_val; i++){
        if(mark[i] == 1){
            cout << i << " ";
        }
    }
    return 0;
}
```

Output :

```cpp
Cac gia tri khac nhau trong mang : 0 1 2 3 4 7 12 14
```

**Bài Toán 2** : Cho mảng A[] gồm N phần tử là số nguyên trong đoạn [0, 106], hãy liệt kê các giá trị khác nhau trong mảng theo thứ tự xuất hiện trong mảng, mỗi giá trị chỉ liệt kê 1 lần

Ý tưởng là sử dụng mảng đánh dấu sau đó liệt kê các theo thứ tự xuất hiện trong mảng và in ra nếu giá trị đó được đánh dấu.

Sau khi in ra giá trị thì bạn bỏ đánh dấu giá trị đó để tránh in trùng.

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

int mark[1000001]; 

int main(){
    int n = 10;
    int a[10] = {3, 1, 3, 0, 2, 4, 1, 14, 12, 7};
    //đánh dấu
    for(int i = 0; i < n; i++){
        //Lấy a[i] làm chỉ số và chuyển mark[a[i]] = 11
        mark[a[i]] = 1;
    }
    cout << "Gia tri khac nhau trong mang : ";
    for(int i = 0; i < n; i++){
        if(mark[a[i]] == 1){
            cout << a[i] << " ";
            //Bỏ đánh dấu
            mark[a[i]] = 0;
        }
    }
    return 0;
}
```

Output :

```cpp
Gia tri khac nhau trong mang : 3 1 0 2 4 14 12 7
```

---

**3. Bài Toán Tần Suất**

Mảng đánh dấu rất hữu dụng đối với những bài toán liên quan tới tần suất xuất hiện của phần tử trong mảng.

Trong bài toán liên quan tới tần suất thì mảng đánh dấu mark[] có vai trò đếm tần suất thay vì chỉ đánh dấu. Khi đánh dấu giá trị a[i] trong mảng thì bạn cần cho mark[a[i]] = 1 còn khi bạn muốn đếm xem a[i] đã xuất hiện bao nhiêu lần thì bạn thay đổi câu lệnh cập nhật thành mark[a[i]]++

**Bài toán** : Cho mảng A[] gồm N phần tử là số nguyên trong đoạn [0, 106], hãy đếm xem mỗi phần tử trong mảng xuất hiện bao nhiêu lần và in ra theo thứ tự từ nhỏ tới lớn.

**Code :** 

```cpp
#include "iostream"
#include "math.h"
using namespace std;

int mark[1000001]; 

int main(){
    int n = 10;
    int a[10] = {3, 1, 3, 0, 2, 4, 1, 14, 3, 2};
    //đếm tần suất
    int max_val = -1000000000;
    for(int i = 0; i < n; i++){
        //Lấy a[i] làm chỉ số và chuyển mark[a[i]] tăng thêm 1 đơn vị
        mark[a[i]]++;
        if(a[i] > max_val){
            max_val = a[i];
        }
    }
    for(int i = 0; i <= max_val; i++){
        if(mark[i]){
            cout << i << " xuat hien " << mark[i] << " lan\n";
        }
    }
    return 0;
}
```

Output :

```cpp
0 xuat hien 1 lan
1 xuat hien 2 lan
2 xuat hien 2 lan
3 xuat hien 3 lan
4 xuat hien 1 lan
14 xuat hien 1 lan
```

**Các bài toán sau bạn tự triển khai coi như bài tập :** 

Bài 1. Liệt kê các phần tử xuất hiện ít nhất 2 lần trong mảng theo thứ tự xuất hiện trong mảng, mỗi phần tử chỉ liệt kê 1 lần

Ví dụ A[] = {3, 1, 1, 1, 2, 3, 4, 0, 3, 2} thì output sẽ là 3, 1, 2

Bài 2. Liệt kê các phần tử xuất hiện đúng 1 lần trong mảng theo thứ tự xuất hiện trong mảng

Ví dụ A[] = {3, 1, 1, 1, 2, 3, 4, 0, 3, 2} thì output sẽ là 4, 0, 2

Bài 3. Liệt kê các phần tử xuất hiện nhiều nhất trong mảng, nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì liệt kê theo thứ tự xuất hiện trong mảng

Ví dụ A[] = {3, 1, 1, 1, 2, 3, 4, 0, 3, 2} thì output sẽ là 3, 1

Bài 4. Cho mảng A[] và B[], hãy liệt kê các giá trị thuộc 1 trong 2 mảng, mỗi giá trị liệt kê 1 lần theo thứ tự tăng dần

Ví dụ A[] = {3, 1, 2, 4, 4, 1, 5} và B[] = {0, 1, 2, 3, 5, 7} thì output là 0, 1, 2, 3, 4, 5, 7

---

**Video Bài Tập Mảng 1 Chiều**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/06-06-cpp-mang-danh-dau.md](solutions/06-06-cpp-mang-danh-dau.md)

**Bài 1.** Nhập mảng `n` số nguyên trong khoảng [0, 100]. Dùng mảng đánh dấu đếm số lần xuất hiện của mỗi giá trị.

**Bài 2.** Tìm phần tử xuất hiện nhiều nhất trong mảng bằng mảng đánh dấu.

**Bài 3.** Tìm phần tử xuất hiện đúng một lần trong mảng.

**Bài 4.** Tìm phần tử nhỏ nhất **không** xuất hiện trong mảng.

**Bài 5.** Kiểm tra mảng có phải hoán vị của `1..n` không, dùng mảng đánh dấu.

**Bài 6.** Loại bỏ phần tử trùng lặp trong mảng bằng mảng đánh dấu (chỉ với giá trị trong [0, 1000]).

**Bài 7.** Cho 2 mảng, tìm các phần tử chung bằng mảng đánh dấu.

**Bài 8.** Đếm tần suất xuất hiện của từng chữ cái trong một chuỗi (dùng mảng 26 phần tử).

**Bài 9.** Kiểm tra 2 chuỗi có phải đảo chữ (anagram) của nhau không.

**Bài 10.** Cho mảng số nguyên từ 1 đến `n` với đúng một số bị lặp và một số bị thiếu. Tìm cả hai.

**Bài 11.** Sắp xếp mảng bằng phương pháp đếm phân phối (Counting Sort) dùng mảng đánh dấu.

**Bài 12.** Cài đặt sàng Eratosthenes dùng mảng đánh dấu để tìm số nguyên tố ≤ 10⁶.

**Bài 13.** Cho dãy các thao tác `+x` (thêm x) và `-x` (xoá x), dùng mảng đánh dấu để trả lời các truy vấn "x có trong tập không?".

**Bài 14.** So sánh mảng đánh dấu với `set`/`map`: lập bảng về tốc độ, bộ nhớ, giới hạn giá trị, khi nào dùng cái nào.

**Bài 15.** Cho `n` khoảng `[l, r]`, dùng mảng đánh dấu (kỹ thuật sai phân) để đếm mỗi điểm được bao phủ bởi bao nhiêu khoảng.
