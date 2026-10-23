# [C++]. Hàm stable_sort() Trong C++

Trong C++ có sẵn 2 hàm sắp xếp đó là **sort()** và **stable_sort()**, bài học trước mình đã hướng dẫn các bạn cách sử dụng hàm sort() và comparison function cho hàm sort(). Tiếp tục kiến thức về sắp xếp và tìm kiếm trong C++ mình sẽ hướng dẫn bạn hiểu về tính chất stable của thuật toán sắp xếp và cách sử dụng hàm stable_sort()

**NỘI DUNG :** 

- **Tính chất ổn định - stable của thuật toán sắp xếp**
- **Hàm stable_sort() trong C++**
- **Video tutorial** 

---

**1. Tính chất ổn định - stable của thuật toán sắp xếp**

Các thuật toán sắp xếp chia thành 2 loại là ổn định và không ổn định, các thuật toán sắp xếp không ổn định có thể kể đến như : sắp xếp nhanh quicksort, sắp xếp vun đống heap sort, sắp xếp chọn selection sort. Bên cạnh đó các thuật toán sắp xếp ổn định bao gồm : sắp xếp trộn merge sort, sắp xếp chèn insertion sort, tim sort, sắp xếp đếm phân phối counting sort.

Vậy tính ổn định của thuật toán sắp xếp là gì ?

Tính ổn định của thuật toán sắp xếp có thể hiểu đơn giản là khi bạn sắp xếp các phần tử trong mảng mà có cùng giá trị sắp xếp (ví dụ như giá trị về độ lớn, tổng chữ số ..) thì những phần tử này sẽ đứng cạnh nhau và duy trì thứ tự giống như thứ tự giữa chúng trong mảng ban đầu.

Ví dụ bạn có dãy số (111, 9, 3000, 18, 81, 1002, 2002) và muốn sắp xếp các phần tử này theo tổng chữ số tăng dần bằng thuật toán sắp xếp có tính chất stable thì mảng sẽ được sắp xếp theo thứ tự (111, 3000, 1002, 2002, 9, 18, 81) trong đó (111, 3000, 1002) có cùng tổng chữ số là 3 và chúng giữ đúng thứ tự ban đầu như thứ tự xuất hiện. Tương tự với cụm (9, 18, 81) có cùng tổng chữ số là 9.

Trong một số ngôn ngữ lập trình thì hàm sắp xếp được cài đặt bởi các thuật toán sắp xếp có tính ổn định, ví dụ như Java, Python, JS. Trong C++ thì hàm sort() mà bạn đã học ở bài trước không có tính ổn định, C++ cung cấp thêm hàm **stable_sort()** có tính chất stable, hàm này được cài đặt bởi thuật toán sắp xếp trộn Merge sort.

---

**2. Hàm stable_sort() trong C++**

Khi làm bài tập về sắp xếp nếu đề bài có thêm yêu cầu trong trường hợp các phần tử trong mảng, danh sách có cùng giá trị sắp xếp thì cần giữ nguyên thứ tự xuất hiện giữa các phần tử này thì khi đó bạn cần nghĩ ngay tới hàm **stable_sort()**

Cách sử dụng hàm stable_sort() giống với hàm sort(), chỉ khác nhau ở thuật toán mà họ đã cài đặt chúng.

**Ví dụ** : Sắp xếp dãy số theo tổng chữ số tăng dần và giữ nguyên thứ tự xuất hiện giữa chúng nếu có cùng tổng chữ số

```cpp
#include "iostream"
#include "algorithm"

using namespace std;

int tong(int n){
    int sum = 0;
    while(n){
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

bool cmp(int a, int b){
    return tong(a) < tong(b);
}

int main(){
    int a[] = {10002, 19, 3000, 111, 81, 45, 1002, 21, 10071, 203, 401};
    int n = 11;
    stable_sort(a, a + n, cmp);
    cout << "Mang sau khi sap xep : \n";
    for(int i = 0; i < n; i++){
        cout << a[i] << " ";
    }
}
```

Output :

```cpp
Mang sau khi sap xep : 
10002 3000 111 1002 21 203 401 81 45 10071 19
```

**Nhận xét** : Bạn chỉ cần xây dựng hàm so sánh để sắp xếp theo tổng chữ số tăng dần còn khi các số trong mảng có cùng tổng chữ số thì hàm stable_sort() sẽ giữ thứ tự tương đối giữa chúng.

---

**Video tutorial:**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/10-04-c-ham-stablesort-trong-c.md](solutions/10-04-c-ham-stablesort-trong-c.md)

**Bài 1.** Sắp xếp một `vector<pair<int,int>>` bằng `sort` và `stable_sort` theo `first`. So sánh kết quả.

**Bài 2.** Tạo ví dụ cụ thể chứng minh `sort` **không** ổn định (có thể phải thử với mảng lớn).

**Bài 3.** Sắp xếp danh sách sinh viên theo điểm, giữ nguyên thứ tự nhập ban đầu khi cùng điểm.

**Bài 4.** Sắp xếp nhiều tiêu chí bằng cách gọi `stable_sort` **nhiều lần** (từ tiêu chí phụ đến chính).

**Bài 5.** So sánh tốc độ `sort` và `stable_sort` trên mảng 1 triệu phần tử.

**Bài 6.** So sánh bộ nhớ sử dụng của `sort` và `stable_sort`.

**Bài 7.** Khi nào bắt buộc phải dùng `stable_sort`? Nêu 3 tình huống thực tế.

**Bài 8.** Làm cho `sort` trở nên "ổn định" bằng cách thêm chỉ số ban đầu vào tiêu chí so sánh.

**Bài 9.** Sắp xếp bảng dữ liệu nhiều cột: sắp theo cột A, rồi trong mỗi nhóm sắp theo cột B — bằng `stable_sort`.

**Bài 10.** Cài đặt Merge Sort tự viết và chứng minh nó ổn định.

**Bài 11.** Cài đặt Selection Sort và chứng minh nó **không** ổn định.

**Bài 12.** `stable_partition` là gì? Viết ví dụ tách số chẵn/lẻ giữ nguyên thứ tự.

**Bài 13.** Sắp xếp danh sách giao dịch theo ngày, cùng ngày thì giữ thứ tự thời gian nhập.

**Bài 14.** Lập bảng so sánh đầy đủ `sort`, `stable_sort`, `partial_sort`, `nth_element`.

**Bài 15.** Viết chương trình mô phỏng bảng xếp hạng nhiều vòng đấu: mỗi vòng sắp lại, người cùng điểm giữ thứ hạng vòng trước.
