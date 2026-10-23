# [C]. Bài Tập Mảng 1 Chiều P2

Bài viết này mình sẽ hướng dẫn các bài tập liên quan tới tần suất và các giá trị khác nhau trong mảng.

**NỘI DUNG** 

- **Đếm Các Phần Tử Khác Nhau** 
- **Liệt Kê Các Phần Tử Khác Nhau**
- **Tần Suất Của Phần Tử Trong Mảng**
- **Video Tutorial**

---

**1.Đếm Các Phần Tử Khác Nhau**

Đếm các giá trị khác nhau trong mảng có nhiều thuật toán có thể giải quyết, trong bài này mình sẽ hướng dẫn các bạn cách giải quyết dễ tiếp cận nhất.

Trong các bài sau mình sẽ hướng dẫn thêm các phương pháp khác tối ưu hơn như sử dụng mảng đánh dấu, sắp xếp mảng...

**Thuật toán :** 

1. Duyệt qua các phần tử trong mảng từ chỉ số 0 tới N - 1
2. Đối với mỗi chỉ số i bạn cần xét các phần tử trong đoạn từ [0, i - 1], nếu chưa có phần tử nào trong đoạn trước chỉ số i bằng với phần tử ở chỉ số i thì ta sẽ có thêm 1 phần tử khác nhau trong mảng

Ví dụ mảng A[] = {1, 3, 4, 5, 5, 2, 4, 8, 1, 2, 3}

Xét chỉ số i = 4, khi đó A[i] = 5 và các phần tử trong đoạn trước A[i] là {1, 3, 4, 5} ta thấy A[i] bằng với 1 phần tử trong đoạn trước nó nên sẽ không đếm thêm 1 giá trị khác nhau trong mảng.

Xét chỉ số i = 5, khi đó A[i] = 2 và các phần tử đứng trước A[i] là {1, 3, 4, 5, 5,} không có phần tử nào giống với A[i] nên khi A[i] xuất hiện ta sẽ có thêm 1 giá trị khác nhau trong mảng.

**Code :** 

```c
#include <stdio.h>

int main(){
    int n = 10;
    int a[10] = {1, 3, 4, 5, 5, 2, 4, 1, 2, 3};
    int res = 0;
    for(int i = 0; i < n; i++){
        //Cần kiểm tra a[i] đã xuất hiện chưa?
        int check = 1;
        //Xét các phần tử đứng trước a[i]
        for(int j = 0; j < i; j++){
            if(a[i] == a[j]){
                check = 0;
                break;
            }
        }
        if(check == 1){
            ++res;
        }
    }
    printf("So luong gia tri khac nhau trong mang : %d\n", res);
    return 0;
}
```

Output :

```
So luong gia tri khac nhau trong mang : 5
```

---

**2. Liệt Kê Các Giá Trị Khác Nhau Trong Mảng**

Thuật toán để liệt kê các giá trị khác nhau trong mảng bạn tương tự như thuật toán trong mục 1, ở đây mình liệt kê theo thứ tự xuất hiện trong mảng.

Nếu bạn muốn liệt kê theo thứ tự từ bé đến lớn thì bạn cần sắp xếp mảng trước khi áp dụng thuật toán này.

**Code :** 

```c
#include <stdio.h>

int main(){
    int n = 10;
    int a[10] = {1, 3, 4, 5, 5, 2, 4, 1, 2, 3};
    printf("Cac gia tri khac nhau trong mang : \n");
    for(int i = 0; i < n; i++){
        //Cần kiểm tra a[i] đã xuất hiện chưa?
        int check = 1;
        //Xét các phần tử đứng trước a[i]
        for(int j = 0; j < i; j++){
            if(a[i] == a[j]){
                check = 0;
                break;
            }
        }
        if(check == 1){
            printf("%d ", a[i]);
        }
    }
    return 0;
}
```

Output :

```
Cac gia tri khac nhau trong mang : 
1 3 4 5 2
```

---

**3. Tần Suất Của Phần Tử Trong Mảng**

Bài toán yêu cầu các bạn liệt kê các giá trị xuất hiện trong mảng kèm theo số lần xuất hiện của nó.

Thuật toán giải quyết bài này tương tự với ở mục 1, mình sẽ hướng dẫn các bạn 2 cách. Cách 1 không dùng thêm mảng phụ và cách 2 thì cần thêm 1 mảng phụ để truy vết.

**Thuật toán 1 :** 

1. Duyệt qua các phần tử trong mảng từ chỉ số 0 tới N - 1
2. Đối với mỗi chỉ số i bạn cần xét các phần tử trong đoạn từ [0, i - 1], nếu chưa có phần tử nào trong đoạn trước chỉ số i bằng với phần tử ở chỉ số i thì ta sẽ đếm tần suất
3. Duyệt các phần tử từ chỉ số [i + 1, N - 1] và so sánh với A[i] để đếm số lần xuất hiện của A[i]

**Code :**

```c
#include <stdio.h>

int main(){
    int n = 10;
    int a[10] = {1, 3, 4, 5, 5, 2, 4, 5, 2, 3};
    for(int i = 0; i < n; i++){
        //Cần kiểm tra a[i] đã xuất hiện chưa?
        int check = 1;
        //Xét các phần tử đứng trước a[i]
        for(int j = 0; j < i; j++){
            if(a[i] == a[j]){
                check = 0;
                break;
            }
        }
        //Nếu a[i] chưa xuất hiện thì đếm tần suất
        if(check == 1){
            int dem = 1; // a[i]
            for(int j = i + 1; j < n; j++){
                if(a[i] == a[j]) ++dem;
            }
            printf("%d xuat hien %d lan\n", a[i], dem);
        }   
    }
    return 0;
}
```

Output :

```
1 xuat hien 1 lan
3 xuat hien 2 lan
4 xuat hien 2 lan
5 xuat hien 3 lan
2 xuat hien 2 lan
```

**Thuật toán 2 :** 

Ý tưởng là sử dụng một mảng đánh dấu B[] ban đầu có tất cả các phần tử là 0 để đánh dấu

1. Duyệt qua các phần tử ở chỉ số i trong mảng A[], nếu B[i] = 0 thì tiến hành đếm tần suất
2. Duyệt các phần tử j trong đoạn [i + 1, N - 1] và so sánh với A[i], nếu A[i] = A[j] thì tăng tần suất và cho B[j] = 1 để đấnh dấu

**Code :** 

```c
#include <stdio.h>

int main(){
    int n = 10;
    int a[10] = {1, 3, 4, 5, 5, 2, 4, 5, 2, 3};
    int b[10] = {0};
    for(int i = 0; i < n; i++){
        if(b[i] == 0){
            int dem = 1;
            for(int j = i + 1; j < n; j++){
                if(a[i] == a[j]){
                    ++dem;
                    b[j] = 1; // đánh dấu
                }
            }
            printf("%d xuat hien %d lan\n", a[i], dem);
        }
    }
    return 0;
}

```

Output :

```
1 xuat hien 1 lan
3 xuat hien 2 lan
4 xuat hien 2 lan
5 xuat hien 3 lan
2 xuat hien 2 lan
```

---

**Video Bài Tập Mảng 1 Chiều**

---

## 🎯 BÀI TẬP BỔ SUNG

> 📘 Lời giải tham khảo: [solutions/06-03-c-bai-tap-mang-1-chieu-p2.md](solutions/06-03-c-bai-tap-mang-1-chieu-p2.md)

**Bài 1.** Sắp xếp mảng tăng dần bằng thuật toán nổi bọt (Bubble Sort), in ra mảng sau mỗi lượt.

**Bài 2.** Sắp xếp mảng bằng thuật toán chọn trực tiếp (Selection Sort).

**Bài 3.** Sắp xếp mảng bằng thuật toán chèn trực tiếp (Insertion Sort).

**Bài 4.** So sánh số phép so sánh và số phép đổi chỗ của 3 thuật toán trên với cùng một mảng.

**Bài 5.** Loại bỏ các phần tử trùng lặp trong mảng, giữ lại lần xuất hiện đầu tiên.

**Bài 6.** Tìm phần tử xuất hiện đúng 1 lần trong mảng mà mọi phần tử khác đều xuất hiện 2 lần (dùng XOR).

**Bài 7.** Tính tổng tiền tố (prefix sum) của mảng, rồi trả lời nhanh các truy vấn "tổng từ vị trí `l` đến `r`".

**Bài 8.** Tìm dãy con liên tiếp có tổng bằng `S` cho trước.

**Bài 9.** Tìm `k` phần tử lớn nhất trong mảng.

**Bài 10.** Tìm phần tử trung vị (median) của mảng.

**Bài 11.** Trộn (shuffle) ngẫu nhiên các phần tử của mảng bằng thuật toán Fisher-Yates.

**Bài 12.** Tách mảng thành 2 nửa có tổng gần bằng nhau nhất (tìm bằng vét cạn với `n` nhỏ).

**Bài 13.** Đếm số cặp nghịch thế (cặp `i < j` mà `a[i] > a[j]`).

**Bài 14.** Nén mảng theo kiểu Run-Length Encoding: `[1,1,1,2,2,3]` → `1x3, 2x2, 3x1`.

**Bài 15.** Cho 2 mảng, tìm phần giao (các phần tử có ở cả hai) và phần hợp của chúng.
