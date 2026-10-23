# [C]. If Else

Trong bài viết này các bạn sẽ học cấu trúc rẽ nhánh với câu lệnh **if else** và **if else** lồng nhau thông qua các ví dụ trực quan.

**NỘI DUNG :** 

- **Câu lệnh if**
- **If else**
- **If else lồng nhau**
- **Bài tập luyện tập**
- **Video tutorial**

---

**1.Câu lệnh if**

Câu lệnh if được sử dụng khi bạn cần kiểm tra một điều kiện trước khi thực hiện những câu lệnh khi điều kiện đó có giá trị đúng

Ví dụ : Nếu n là số chẵn sẽ in ra "codelab"

**Cú pháp :** 

```c
if(điều_kiện){
    //Các câu lệnh 
}
```

Điều kiện ở trong if thường là các phép so sánh, biểu thức trả về giá trị đúng sai. Khi điều kiện này có giá trị đúng thì các câu lệnh bên trong ngoặc nhọn của if sẽ được thực hiện, ngược lại thì các câu lệnh này sẽ bị bỏ qua.

Ví dụ 1 : Kiểm tra n là 28 thì in ra codelab

```c
#include <stdio.h>

int main(){
    int n = 28;
    if(n == 28){
        printf("codelab\n");
    }
    if(n > 30){
        printf("blog codelab\n");
    }
    printf("end\n");
    return 0;
}
```

Output :

```
codelab
end
```

Ví dụ 2 : Kiểm tra n là số chẵn thì in ra "CHAN"

Để kiểm tra 1 số là số chẵn bạn tìm số dư của số đó với 2 và so sánh số dư đó với 0

```c
#include <stdio.h>

int main(){
    int n = 28;
    if((n % 2) == 0){
        printf("CHAN\n");
    }
    if((n % 2) != 0){
        printf("LE\n");
    }
    return 0;
}
```

Output :

```
CHAN
```

Ví dụ 3 : Kiểm tra n chia hết cho m

Để kiểm tra tính chia hết bạn tìm số dư của n với m và so sánh với 0

```c
#include <stdio.h>

int main(){
    int n = 28, m = 4;
    if((n % m) == 0){
        printf("Chia het\n");
    }
    if((n % m) != 0){
        printf("Khong chia het\n");
    }
    return 0;
}
```

Output :

```
Chia het
```

Ví dụ 4 : Kiểm tra n là một trong 4 số 2, 3, 5, 7 thì in ra YES

```c
#include <stdio.h>

int main(){
    int n = 5;
    if((n == 2) || (n == 3) || (n == 5) || (n == 7)){
        printf("YES\n");
    }
    return 0;
}
```

Output :

```
YES
```

**Chú ý** : Trong C các giá trị khác không được coi là đúng nên bạn có thể sử dụng nó để làm điều kiện cho if. Nếu số mà bạn truyền vào làm điều kiện cho if khác 0 thì code trong if sẽ thực thi và ngược lại.

Ví dụ 5 :

```c
#include <stdio.h>

int main(){
    int n = 28, m = 0;
    if(n){
        printf("%d khac 0\n", n);
    }
    if(m){
        printf("%d khac 0\n", m);
    }
    printf("END\n");
    return 0;
}
```

Output :

```
28 khac 0
END
```

**2. If Else**

Câu lệnh if sẽ giúp thực thi khi điều kiện trong if đúng, còn trong trường hợp sai thì khối lệnh bên trong else sẽ được thực hiện.

If có thể không cần đến else nhưng else thì cần if đi trước.

**Cú pháp** :

```c
if(điều_kiện){
    //Code này sẽ được thực hiện
    //khi điều kiện đúng
}
else{
    //Code này sẽ thực hiện khi điều 
    //kiện sai
}
```

Ví dụ 1 : Kiểm tra n là số chẵn nếu đúng in CHAN và codelab, sai in LE và codelab.dev

```c
#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
    if(n % 2 == 0){
        printf("CHAN\n");
        printf("codelab\n");
    }
    else{
        printf("LE\n");
        printf("codelab.dev\n");
    }
    return 0;
}
```

Output (khi nhập n = 28) :

```
CHAN
codelab
```

Ví dụ 2 : Kiểm tra nếu n là năm nhuận in ra YES, ngược lại in ra NO

Năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 và không chia hết cho 100

```c
#include <stdio.h>

int main(){
    int n = 2020;
    if((n % 400 == 0) || (n % 4 == 0 && n % 100 != 0)){
        printf("YES\n");
    }
    else{
        printf("NO\n");
    }
    return 0;
}
```

Output :

```
YES
```

---

**3. If Else Lồng Nhau**

If else có thể lồng vào nhau tức là bên trong khối if else cũng có thể có thêm nhiều câu lệnh if else khác.

Thông thường if else lồng nhau được sử dụng khi điều kiện của bài toán của bạn quá lớn và cần chia nhỏ ra làm nhiều phần để kiểm tra từng bước một.

Ví dụ 1 : Kiểm tra n nằm trong đoạn [20, 50] và chia hết cho ít nhất 1 trong 4 số 2, 3, 5, 7, nếu đúng in YES, ngược lại in NO

Code 1 : Sử dụng if else

```c
#include <stdio.h>

int main(){
    int n = 20;
    if((n >= 20 && n <= 50) && (n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0)){
        printf("YES\n");
    }
    else{
        printf("NO\n");
    }
    return 0;
}
```

Code 2 : Sử dụng if else lồng nhau

```c
#include <stdio.h>

int main(){
    int n = 20;
    if((n >= 20 && n <= 50)){
        if(n % 2 == 0 || n % 3 == 0 || n % 5 == 0 || n % 7 == 0){
            printf("YES\n");
        }
        else{
            printf("NO\n");
        }
    }
    else{
        printf("NO\n");
    }
    return 0;
}
```

**4. Bài Tập Luyện Tập**

Để có thể viết if else thành thạo bạn cần luyện tập nhiều và nắm được các câu lệnh kiểm tra thường gặp với if.

**Bài 1**. N có phải là số chẵn, đúng in 1 sai in 0

```c
#include <stdio.h>

int main(){
    int n; scanf("%d", &n);
    if(n % 2 == 0){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 2**. N có phải là số vừa chia hết cho 3 vừa chia hết cho 5, đúng in 1 sai in 0

```c
#include <stdio.h>

int main(){
    int n; scanf("%d", &n);
    if((n % 3 == 0) && (n % 5 == 0)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 3.** N có phải là số chia hết 3 nhưng không chia hết cho 7, đúng in 1 sai in 0

```c
#include <stdio.h>

int main(){
    int n; scanf("%d", &n);
    if((n % 3 == 0) && (n % 7 != 0)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 4**. N có phải là số chia hết cho 3 hoặc 7, đúng in "codelab" và "laptrinhC", sai in "codelab.dev" và "Java"

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    if((n % 3 == 0) || (n % 7 == 0)){
        printf("codelab\n");
        printf("laptrinhC\n");
    }
    else{
        printf("codelab.dev\n");
        printf("Java\n");
    }
    return 0;
}
```

**Bài 5.** N là số lớn hơn 30 và nhỏ hơn 50, đúng in 1 sai in 0

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    if((n > 30) && (n < 50)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 6**. N có phải là số không nhỏ hơn 30 và chia hết cho ít nhất một trong 3 số 2, 3, 5, đúng in 1 sai in 0

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    if((n >= 30) && (n % 2 == 0 || n % 3 == 0 || n % 5 == 0)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 7**. N có phải là số có 2 chữ số và có chữ tận cùng là một số nguyên tố

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    int r = n % 10; // chữ số cuối cùng
    if((n >= 10 && n <= 99) && (r == 2 || r == 3 || r == 5 || r == 7)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 8.** N có phải là số không vượt quá 100 và chia hết cho 23?

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    if((n <= 100) && (n % 23 == 0)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 9.** N không thuộc đoạn [10, 20]?

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    if((n < 10) || (n > 20)){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

**Bài 10.** N có chữ số tận cùng là bội số của 3

```c
#include <stdio.h>

int main(){
    int n; 
    scanf("%d", &n);
    if((n % 10) % 3 == 0){
        printf("1\n");
    }
    else{
        printf("0\n");
    }
    return 0;
}
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/03-01-c-if-else.md](solutions/03-01-c-if-else.md)

**Bài 1.** Nhập một số nguyên `n`. In ra `n` là số dương, số âm hay bằng 0.

**Bài 2.** Nhập 2 số nguyên `a`, `b`. In ra số lớn hơn; nếu bằng nhau thì thông báo "Hai so bang nhau".

**Bài 3.** Nhập 3 số nguyên, tìm và in ra số lớn nhất (dùng `if` lồng nhau, không dùng hàm hay macro `max`).

**Bài 4.** Nhập một số nguyên `n`. Kiểm tra `n` có chia hết cho cả 2, 3 và 5 hay không.

**Bài 5.** Nhập điểm trung bình (số thực 0–10). In ra xếp loại: ≥ 8.5 Giỏi, ≥ 7.0 Khá, ≥ 5.0 Trung bình, còn lại Yếu.

**Bài 6.** Nhập tuổi. In ra: < 6 "Mam non", 6–10 "Tieu hoc", 11–14 "THCS", 15–17 "THPT", ≥ 18 "Dai hoc/Di lam".

**Bài 7.** Nhập 3 số nguyên `a`, `b`, `c`. Kiểm tra chúng có tạo thành tam giác hợp lệ không (tổng 2 cạnh bất kỳ lớn hơn cạnh còn lại).

**Bài 8.** Nhập 3 cạnh tam giác hợp lệ. Xác định tam giác đó là đều, cân, vuông, vuông cân hay thường.

**Bài 9.** Nhập một ký tự. Kiểm tra nó là chữ hoa, chữ thường, chữ số hay ký tự đặc biệt (chỉ dùng `if` và so sánh mã ASCII).

**Bài 10.** Nhập một năm. Kiểm tra năm nhuận bằng `if` lồng nhau (không dùng toán tử logic gộp).

**Bài 11.** Nhập số điện tiêu thụ (kWh). Tính tiền điện theo bậc thang: 50 kWh đầu giá 1.800đ, 50 kWh tiếp giá 1.900đ, còn lại giá 2.200đ.

**Bài 12.** Nhập số tiền mua hàng. Tính giảm giá: ≥ 5 triệu giảm 15%, ≥ 2 triệu giảm 10%, ≥ 500 nghìn giảm 5%, còn lại không giảm. In ra số tiền phải trả.

**Bài 13.** Chương trình sau có lỗi logic. Tìm và giải thích:

```c
int n;
scanf("%d", &n);
if (n = 0) printf("Bang khong");
else printf("Khac khong");
```

**Bài 14.** Chương trình sau in ra gì với `n = 5`? Giải thích vì sao và sửa lại cho đúng ý đồ:

```c
int n; scanf("%d", &n);
if (n > 0);
    printf("So duong\n");
```

**Bài 15.** Nhập 4 số nguyên. Sắp xếp và in ra theo thứ tự tăng dần chỉ bằng `if` và hoán đổi bằng biến tạm (không dùng vòng lặp hay hàm `qsort`).
