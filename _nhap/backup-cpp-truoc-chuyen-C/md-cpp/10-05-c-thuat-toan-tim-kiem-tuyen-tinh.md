# [C++].  Thuật Toán Tìm Kiếm Tuyến Tính

Trong bài viết này bạn sẽ học thuật toán rất phổ biến và dễ tiếp cận là thuật toán tìm kiếm tuyến tính - Linear search

**NỘI DUNG :** 

- **Tìm Kiếm Tuyến Tính**
- **Ví Dụ**
- **Video Tutorial**

**1. Tìm Kiếm Tuyến Tính**

Tìm kiếm là một công việc được thực hiện nhiều trong lập trình và trong thực tế, bạn có thể tìm kiếm trong dãy số hay trong danh sách sinh viên những sinh viên thỏa mãn điều kiện mong muốn.

Thuật toán tìm kiếm đơn giản nhất đó là thuật toán tìm kiếm tuyến tính - Linear search.

Giả sử bạn cần tìm kiếm xem phần tử X có xuất hiện trong mảng A[] hay không, ý tưởng của thuật toán rất đơn giản đó là duyệt tuần tự các phần tử trong mảng và so sánh giá trị cần tìm kiếm với các phần tử trong mảng.

Nếu gặp phần tử nào bằng phần tử X thì có thể kết luận tìm thấy, khi duyệt hết dãy số nhưng không tìm được giá trị X thì kết luận X không xuất hiện trong mảng.

Độ phức tạp : O(N)

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

bool linear_search(int a[], int n, int x){
    for(int i = 0; i < n; i++){
        if(a[i] == x)
            return true;
    }
    return false;
}

int main(){
    int a[10] = {1, 3, 2, 4, 1, 5, 8, 9, 2, 3};
    int n = 10, x = 8;
    if(linear_search(a, n, x)){
        cout << "FOUND\n";
    }
    else{
        cout << "NOT FOUND\n";
    }
}
```

Output :

```cpp
FOUND
```

Ngoài ra các biến thể của thuật toán tìm kiếm tuyến tính có thể kể đến như : Tìm vị trí đầu tiên (cuối cùng) của X trong mảng, đếm số lần xuất hiện của X trong mảng...

**Mã nguồn** : Tìm vị trí đầu tiên của X trong mảng

```cpp
#include "iostream"

using namespace std;

int firstPos(int a[], int n, int x){
    for(int i = 0; i < n; i++){
        if(a[i] == x){
            return i;
        }
    }
    return -1; // khong tim thay
}

int main(){
    int n = 10, x = 3;
    int a[10] = {6, 1, 2, 4, 3, 10, 9, 3, 8, 6};
    if(firstPos(a, n, x) != -1){
        cout << "Vi tri dau tien cua " << x << " : " << firstPos(a, n, x) << endl;
    }
    else{
        printf("NOT FOUND\n");
    }
    return 0;
}
```

Output :

```cpp
Vi tri dau tien cua 3 : 4
```

**Mã nguồn** : Đếm số lần xuất hiện của X trong mảng

```cpp
#include "iostream"

using namespace std;

int count(int a[], int n, int x){
    int res = 0;
    for(int i = 0; i < n; i++){
        if(a[i] == x){
            ++res;
        }
    }
    return res;
}

int main(){
    int n = 10, x = 3;
    int a[10] = {6, 1, 2, 4, 3, 10, 9, 3, 8, 6};
    cout << "So lan xuat hien cua " << x << " : " << count(a, n, x) << endl;
}
```

Output :

```cpp
So lan xuat hien cua 3 : 2
```

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-05-c-thuat-toan-tim-kiem-tuyen-tinh.md](solutions/10-05-c-thuat-toan-tim-kiem-tuyen-tinh.md)

**Bài 1.** Cài đặt tìm kiếm tuyến tính trả về vị trí đầu tiên của `x`, hoặc −1.

**Bài 2.** Tìm vị trí **cuối cùng** của `x` trong mảng.

**Bài 3.** Tìm **tất cả** vị trí xuất hiện của `x`.

**Bài 4.** Đếm số lần xuất hiện của `x` bằng tìm kiếm tuyến tính.

**Bài 5.** Tìm phần tử đầu tiên thoả một điều kiện (số nguyên tố, số chẵn, số chia hết cho k).

**Bài 6.** Dùng `find`, `find_if`, `count`, `count_if` của `<algorithm>` thay cho tự viết.

**Bài 7.** Tìm kiếm trong `vector<string>` — tìm chuỗi chứa một chuỗi con cho trước.

**Bài 8.** Tìm kiếm trong mảng struct theo một trường bất kỳ.

**Bài 9.** So sánh tìm kiếm tuyến tính và nhị phân: khi nào mỗi cái tốt hơn?

**Bài 10.** Cài đặt tìm kiếm tuyến tính với "lính canh" (sentinel) để bỏ bớt một phép so sánh mỗi vòng.

**Bài 11.** Tìm kiếm trong mảng 2 chiều, trả về cặp `(hàng, cột)`.

**Bài 12.** Tìm phần tử gần giá trị `x` nhất trong mảng chưa sắp xếp.

**Bài 13.** Tìm 2 phần tử có tổng bằng `x` bằng tìm kiếm tuyến tính lồng nhau. Sau đó tối ưu bằng `set`.

**Bài 14.** Đo thời gian tìm kiếm tuyến tính với phần tử ở đầu, giữa, cuối mảng và phần tử không tồn tại.

**Bài 15.** Viết chương trình quản lý danh bạ với chức năng tìm kiếm theo tên, số điện thoại, hoặc một phần tên.
