# [C++]. Cấp Phát Mảng Động

Cấp phát mảng động trong C++ được thực hiện thông qua 2 toán tử là **new** và **delete**. Đây là thao tác quan trọng khi xây dựng các cấu trúc dữ liệu như danh sách liên kết hay cây nhị phân.

**NỘI DUNG :** 

- **Cấp Phát Động Là Gì ?** 
- **Toán Tử New Và Delete**
- **Video Tutorial**

---

**1. Cấp Phát Động Là Gì?**

**Cấp phát động** - Dynamic memory allocation trong C/C++ là hình thức xin cấp phát vùng nhớ bởi lập trình viên.

Khi cấp phát động thì người lập trình sẽ chủ động xin cấp phát vùng nhớ khi cần và giải phóng vùng nhớ khi cần thu hồi.

Một số đặc điểm về cấp phát động bạn cần nhớ :

- Vùng nhớ sử dụng khi cấp phát động là vùng nhớ **heap** 
- Lập trình viên cần giải phóng vùng nhớ để tránh rò rỉ bộ nhớ (leak memory)
- Cấp phát động là thao tác chính để tạo nên các cấu trúc dữ liệu như cây nhị phân hay danh sách liên kết

**2. Toán Tử New Và Delete** 

**Toán tử new :** 

Vùng nhớ cấp phát động được xin cấp phát thông qua toán tử **new**, theo sau sẽ là kiểu dữ liệu. Trong trường hợp bạn xin cấp phát nhiều hơn 1 phần tử thì cần thêm số lượng phần tử trong đóng mở ngoặc vuông.

Toán tử new sẽ trả về con trỏ tới ô nhớ đầu tiên của vùng nhớ được cấp phát hoặc sẽ trả về con trỏ NULL nếu không cấp phát đủ bộ nhớ

**Cú pháp :** 

```cpp
pointer = new data_type
pointer = new data_type [num_of_elements]
```

Cú pháp thứ nhất sẽ xin cấp phát 1 phần tử còn cú pháp thứ 2 xin cấp phát 1 khối (tương tự như 1 mảng các phần tử).

Sau khi xin cấp phát 1 mảng động thì bạn có thể sử dụng mảng động thông qua con trỏ pointer tương tự như mảng 1 chiều.

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    int *ptr = new int[5];
    cout << "Gia tri cua ptr : " << ptr << endl;
    ptr[0] = 1;
    ptr[1] = 2;
    ptr[2] = 3;
    ptr[3] = 4;
    ptr[4] = 5;
    for(int i = 0; i < 5; i++){
        cout << ptr[i] << ' '; // hoac *(ptr + i)
    }
}
```

Output :

```cpp
Gia tri cua ptr : 0xca1510
1 2 3 4 5
```

Trong trường hợp vùng nhớ heap không đủ cấp phát thì chương trình sẽ ném ra ngoại lệ và trả về con trỏ NULL. Bạn có thể kiểm tra việc cấp phát có thành công hay không, trong ví dụ dưới đây mình sẽ in cấp phát vùng nhớ có cỡ 1013 phần tử int để việc cấp phát không thành công.

```cpp
#include "iostream"

using namespace std;

int main(){
    int *ptr = new int[10000000000000ll];
    return 0;
}
```

Output :

```cpp
terminate called after throwing an instance of 'std::bad_alloc'
  what():  std::bad_alloc
```

Để tránh chương trình ném ra ngoại lệ bạn có thể dùng thêm cơ chế **nothrow** để kiểm nghiệm việc ptr sẽ là NULL nếu không đủ bộ nhớ cấp phát

```cpp
#include "iostream"

using namespace std;

int main(){
    int *ptr = new(nothrow) int[10000000000000ll];
    if(ptr == NULL){
        cout << "Khong du bo nho cap phat !\n";
    }
    return 0;
}
```

Output :

```cpp
Khong du bo nho cap phat !
```

---

**Toán tử delete :** 

Toán tử **delete** được sử dụng để giải phóng vùng nhớ đã xin cấp phát trước đó bở toán tử new.

Việc này là cần thiết để tránh việc leak memory

**Cú pháp :** 

```cpp
delete pointer;
delete [] pointer;
```

Cú pháp thứ nhất để giải phóng vùng nhớ 1 phần tử được cấp phát trước đó còn cú pháp thứ 2 dùng khi bạn đã xin cấp phát 1 mảng các phần tử.

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    int n; cout << "Nhap so luong phan tu xin cap phat : ";
    cin >> n;
    int *ptr = new(nothrow) int[n];
    if(ptr == NULL){
        cout << "Khong du bo nho cap phat !\n";
    }
    else{
        cout << "Nhap cac phan tu trong day : ";
        for(int i = 0; i < n; i++){
            cin >> ptr[i];
        }
        cout << "Cac phan tu vua nhap : ";
        for(int i = 0; i < n; i++){
            cout << ptr[i] << ' ';
        }
        delete []ptr;
    }
    return 0;
}
```

---

**Xem thêm bài giảng về Con Trỏ của mình :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/07-04-c-cap-phat-mang-dong.md](solutions/07-04-c-cap-phat-mang-dong.md)

**Bài 1.** Nhập `n` từ bàn phím, cấp phát mảng động `n` phần tử, nhập giá trị, in ra rồi giải phóng.

**Bài 2.** Cấp phát một biến `int` động bằng `new`, gán giá trị, in ra rồi `delete`.

**Bài 3.** Cấp phát mảng động và khởi tạo tất cả phần tử bằng 0.

**Bài 4.** Viết hàm `int* taoMang(int n)` cấp phát và trả về mảng động đã điền giá trị `0..n-1`.

**Bài 5.** Viết hàm mở rộng mảng động: cấp phát mảng mới lớn hơn, copy dữ liệu cũ sang, giải phóng mảng cũ.

**Bài 6.** Cấp phát mảng 2 chiều động `n × m` và tính tổng các phần tử.

**Bài 7.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
int *a = new int[10];
delete a;
```

**Bài 8.** Chương trình sau bị rò rỉ bộ nhớ (memory leak). Tìm và sửa:

```cpp
for (int i = 0; i < 1000; i++) {
    int *p = new int[1000];
    // ... xu ly ...
}
```

**Bài 9.** Chương trình sau có lỗi gì? Giải thích:

```cpp
int *p = new int(5);
delete p;
cout << *p;
delete p;
```

**Bài 10.** So sánh mảng tĩnh và mảng động: lập bảng về kích thước, thời điểm xác định, vùng nhớ, giới hạn.

**Bài 11.** Tại sao mảng tĩnh `int a[10000000]` bị crash nhưng `new int[10000000]` thì không? Giải thích stack vs heap.

**Bài 12.** Viết chương trình mô phỏng `vector` đơn giản: cấp phát động, `push_back` tự mở rộng gấp đôi khi đầy.

**Bài 13.** Tìm hiểu `unique_ptr` và `make_unique`. Viết lại bài 1 bằng smart pointer.

**Bài 14.** Dùng công cụ phát hiện rò rỉ bộ nhớ (`valgrind` hoặc `-fsanitize=address`) kiểm tra chương trình ở bài 8.

**Bài 15.** Viết chương trình quản lý danh sách sinh viên với số lượng do người dùng nhập, dùng cấp phát động và giải phóng đúng cách.
