# [C]. Switch Case

Trong bài học này chúng ta học thêm một cấu trúc rẽ nhánh nữa có phần ngắn gọn hơn so với if và else if đó là **switch case**.

**NỘI DUNG :**

- **Switch Case**
- **Video Tutorial**

**1.Switch Case**

Switch case sử dụng tương đối giống if và else if, nó cũng giúp bạn có thể kiểm tra nhiều điều kiện để thực hiện các rẽ nhánh khác nhau.

**Cú pháp :** 

```c
switch(value){
    case c1:
        //code
        break;
    case c2:
        //code
        break;
    ....
    case cn:
        //code
        break;
    default:
        //code
}
```

Cách hoạt động của switch case đó là sẽ so sánh lần lượt giá trị của value bên trong switch với giá trị của các hằng số trong các case là c1, c2, ... cn. Nếu giá trị của value bằng giá trị của case nào thì khối lệnh bên trong case đó sẽ được thực hiện.

Nếu giá trị của value không bằng bất cứ giá trị nào trong các case thì khối lệnh trong default sẽ được thực hiện, default trong switch case tương tự như else trong if else bạn đã học ở bài trước.

**Chú ý** : Trong C, `value` phải là biểu thức kiểu **số nguyên** (`int`, `char`, `long`, `enum`...) và các giá trị `c1, c2, ... cn` phải là **hằng số nguyên** (vd `1`, `'a'`), không được là biến.

Ví dụ 1:

```c
#include <stdio.h>

int main(){
    int n = 3;
    switch(n){
        case 1:
            printf("ONE\n");
            break;
        case 2:
            printf("TWO\n");
            break;
        case 3:
            printf("THREE\n");
            break;
        case 4:
            printf("FOUR\n");
            break;
        //Neu n khong phai la 1, 2, 3, 4
        default:
            printf("DEFAULT\n");
    }
    return 0;
}
```

Output :

```
THREE
```

**Chú ý** : Các câu lệnh bên trong case sẽ được kết thúc bởi câu lệnh break. Nếu không có câu lệnh break thì khi code trong nhánh nào được thực hiện, switch case sẽ không kết thúc ngay như else if mà sẽ thực hiện luôn các câu lệnh trong các rẽ nhánh bên dưới.

Ví dụ 2 :

```c
#include <stdio.h>

int main(){
    int n = 2;
    switch(n){
        case 1:
            printf("ONE\n");
        case 2:
            printf("TWO\n");
        case 3:
            printf("THREE\n");
        case 4:
            printf("FOUR\n");
        //Neu n khong phai la 1, 2, 3, 4
        default:
            printf("DEFAULT\n");
    }
    return 0;
}
```

Output : 

```
TWO
THREE
FOUR
DEFAULT
```

Ví dụ 3 : Nhập vào toán tử +, -, *, / và in ra kết quả tương ứng với 2 số a, b

```c
#include <stdio.h>

int main(){
    int a = 20, b = 5;
    char op;
    scanf(" %c", &op);
    switch(op){
        case '+':
            printf("%d\n", a + b);
            break;
        case '-':
            printf("%d\n", a - b);
            break;
        case '*':
            printf("%d\n", a * b);
            break;
        case '/':
            printf("%d\n", a / b);
            break;
        default:
            printf("INVALID INPUT\n");
    }
    return 0;
}
```

Ví dụ 4 : Nhập tháng và năm in ra số ngày của tháng, chú ý tháng 2 của năm nhuận có 29 ngày

```c
#include <stdio.h>

int main(){
    int m, y;
    printf("Nhap thang, nam : ");
    scanf("%d %d", &m, &y);
    switch(m){
        case 1: case 3: case 5: case 7: case 8: case 10 : case 12:
            printf("%d\n", 31);
            break;
        case 4: case 6 : case 9 : case 11:
            printf("%d\n", 30);
            break;
        case 2:
            if((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)){
                printf("%d\n", 29);
            }
            else{
                printf("%d\n", 28);
            }
            break;
        default:
            printf("Du lieu khong hop le !\n");
    }
    return 0;
}
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/03-03-c-switch-case.md](solutions/03-03-c-switch-case.md)

**Bài 1.** Nhập số từ 2–8, dùng `switch case` in ra tên thứ trong tuần.

**Bài 2.** Nhập một tháng, dùng `switch case` in ra số ngày của tháng đó (giả sử không phải năm nhuận).

**Bài 3.** Làm lại bài 2 nhưng có xét năm nhuận (nhập thêm năm).

**Bài 4.** Viết máy tính bỏ túi bằng `switch case`: nhập 2 số và 1 phép toán (`+ - * / %`).

**Bài 5.** Nhập một ký tự, dùng `switch case` kiểm tra xem nó có phải nguyên âm hay không.

**Bài 6.** Nhập một tháng, dùng `switch case` in ra tháng đó thuộc mùa nào (Xuân: 1–3, Hạ: 4–6, Thu: 7–9, Đông: 10–12).

**Bài 7.** Chạy đoạn code sau với `n = 2` và giải thích kết quả:

```c
switch (n) {
    case 1: printf("Mot ");
    case 2: printf("Hai ");
    case 3: printf("Ba ");
    default: printf("Khac");
}
```

**Bài 8.** Sửa chương trình bài 7 để mỗi trường hợp chỉ in đúng một từ.

**Bài 9.** Viết menu quản lý đơn giản: in ra 4 lựa chọn (1-Them, 2-Xoa, 3-Sua, 4-Thoat), nhập lựa chọn và dùng `switch case` in ra thông báo tương ứng.

**Bài 10.** Nhập điểm dạng số nguyên 0–10, dùng `switch case` in ra xếp loại (gợi ý: dùng nhiều `case` chung một khối).

**Bài 11.** Thử viết `switch` với biến kiểu `double`. Chép lại lỗi và giải thích vì sao `switch` không hỗ trợ số thực.

**Bài 12.** Nhập 1 ký tự đại diện cho đơn vị (`c` = Celsius, `f` = Fahrenheit) và một nhiệt độ, dùng `switch case` để chuyển đổi.

**Bài 13.** Lập bảng so sánh `switch case` với chuỗi `if else if`: khi nào dùng cái nào, ưu nhược điểm.

**Bài 14.** Viết chương trình nhập một ký tự chữ cái, dùng `switch case` in ra nó là nguyên âm, phụ âm; xử lý được cả chữ hoa lẫn chữ thường mà không phải viết 2 lần số case.

**Bài 15.** Viết chương trình chuyển số La Mã 1 ký tự (I, V, X, L, C, D, M) sang giá trị số bằng `switch case`.
