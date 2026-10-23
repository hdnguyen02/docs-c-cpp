# [C++]. Vòng Lặp Do-While

Trong bài học này bạn sẽ học vòng lặp còn lại trong ngôn ngữ lập trình C+ đó là vòng lặp **do-while** 

**NỘI DUNG :** 

- **Vòng Lặp Do-While**
- **Sơ Đồ Khối**
- **Video Tutorial** 

---

**1. Vòng Lặp Do-While** 

Nếu bạn đã hiểu rõ cách hoạt động của vòng lặp for và while thì vòng lặp do-while bạn cũng sẽ thấy sự tương đồng của nó với vòng lặp while.

Chỉ có 1 chút khác biệt đó là vòng lặp do-while thực hiện câu lệnh trước rồi mới kiểm tra điều kiện sau

 **Cú pháp :** 

```cpp
do{
    //Code
}while(condition);
```

Cách vòng lặp do-while hoạt động :

1. Code bên trong thân vòng lặp được thực hiện lần thứ nhất, sau đó điều kiện (condition) được kiểm tra
2. Nếu điều kiện trong while có giá trị sai vòng lặp do-while sẽ kết thúc
3. Nếu điều kiện trong while đúng, khối lệnh trong do được thực hiện thêm 1 lần nữa
4. Bước 3 được lặp đi lặp lại cho tới khi điều kiện trong while bị sai, nếu điều kiện này luôn đúng vòng lặp sẽ lặp vĩnh viễn

Ví dụ 1: In ra các số từ 1 đến n bằng do-while

```cpp
#include "iostream"

using namespace std;

int main(){
    int i = 1, n = 4;
    do{
        cout << i << ' ';
        ++i;
    }while(i <= n);
    return 0;
}
```

Output :

```cpp
1 2 3 4
```

Giải thích :

1. Vòng lặp thực hiện in ra i là 1, sau đó ++i thì i lên 2
2. Vòng lặp kiểm tra điều kiện lặp : i <= n tương tương 2 <= 4 có giá trị đúng nên tiếp tục in ra i là 2, ++i thì i tăng lên 3
3. Vòng lặp kiểm tra điều kiện lặp : i <= n tương tương 3 <= 4 có giá trị đúng nên tiếp tục in ra i là 3, ++i thì i tăng lên 4
4. Vòng lặp kiểm tra điều kiện lặp : i <= n tương tương 4 <= 4 có giá trị đúng nên tiếp tục in ra i là 4, ++i thì i tăng lên 5
5. Vòng lặp kiểm tra điều kiện lặp : i <= n tương tương 5 <= 4 có giá trị sai nên vòng lặp kết thúc

Ví dụ 2 : Nhập 1 số nguyên từ bàn phím nếu nhập số âm thì yêu cầu nhập lại, nhập số không âm thì cho dừng

```cpp
#include "iostream"

using namespace std;

int main(){
    int n;
    do{
        cout << "Nhap n : ";
        cin >> n;
    }while(n < 0);
    return 0;
}
```

---

**2. Sơ Đồ Khối** 

Các bạn lưu ý rằng vòng lặp do-while sẽ luôn thực hiện khối lệnh 1 lần đầu tiên trước khi kiểm tra điều kiện lặp.

![](../images/c82e54fcff262047.png)

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/04-03-cpp-vong-lap-do-while.md](solutions/04-03-cpp-vong-lap-do-while.md)

**Bài 1.** Dùng `do while` in các số từ 1 đến `n`.

**Bài 2.** Viết chương trình yêu cầu người dùng nhập một số dương; nếu nhập sai thì bắt nhập lại cho tới khi đúng.

**Bài 3.** Yêu cầu nhập điểm trong khoảng 0–10, lặp lại cho tới khi nhập hợp lệ.

**Bài 4.** Đếm số chữ số của `n` bằng `do while` (chú ý: cách này xử lý đúng luôn trường hợp `n = 0`).

**Bài 5.** Viết menu vòng lặp: hiện 4 lựa chọn, thực hiện theo lựa chọn, lặp lại cho tới khi chọn "Thoát".

**Bài 6.** Máy tính bỏ túi lặp lại: nhập 2 số và phép toán, in kết quả, hỏi "Tiep tuc? (y/n)", lặp nếu nhập `y`.

**Bài 7.** Trò chơi đoán số dùng `do while` thay vì `while(true)`.

**Bài 8.** Viết chương trình nhập mật khẩu, cho tối đa 3 lần thử; đúng thì in "Dang nhap thanh cong", hết lượt thì in "Tai khoan bi khoa".

**Bài 9.** So sánh `while` và `do while`: chạy 2 đoạn code sau với `n = 0` và giải thích khác biệt:

```cpp
// A
int i = n;  while (i > 0) { cout << i << " "; i--; }
// B
int i = n;  do { cout << i << " "; i--; } while (i > 0);
```

**Bài 10.** Đảo ngược một số nguyên bằng `do while`.

**Bài 11.** Nhập các số cho tới khi tổng vượt quá 100, in ra số lượng số đã nhập.

**Bài 12.** Viết chương trình mô phỏng máy ATM đơn giản: số dư ban đầu 1.000.000đ, menu rút/gửi/xem số dư/thoát, lặp bằng `do while`.

**Bài 13.** Chương trình sau có lỗi gì? Sửa lại:

```cpp
int i = 1;
do {
    cout << i << " ";
    i++;
} while (i <= 10)
```

**Bài 14.** Viết chương trình tính tổng các số nguyên nhập vào, dừng khi người dùng nhập `-1`, dùng `do while`.

**Bài 15.** Lập bảng so sánh 3 loại vòng lặp `for`, `while`, `do while` theo: số lần chạy tối thiểu, khi nào nên dùng, cú pháp.
