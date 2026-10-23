# [C++]. Câu Lệnh Break Và Continue

**Break** và **Continue** là hai câu lệnh được sử dụng phổ biến trong các vòng lặp, bài học này sẽ giúp các bạn hiểu rõ khi nào cần dùng 2 câu lệnh này và sử dụng chúng sao cho hợp lý.

**NỘI DUNG :** 

- **Câu Lệnh Break**
- **Câu Lệnh Continue**
- **Vidao Tutorial**

---

**1.Câu Lệnh Break**

Break được sử dụng khi bạn muốn dừng vòng lặp (for, while, do-while) ngay lập tức, thông thường câu lệnh break thường đi kèm với 1 điều kiện kích hoạt, ví dụ như sau khi tìm được đáp án trong vòng lặp.

Khi câu lệnh break được thực thi thì các câu lệnh bên dưới break trong vòng lặp sẽ không được thực hiện nốt, vòng lặp sẽ kết thúc ngay tại ví trí của câu lệnh break

Với vòng lặp lồng nhau thì câu lệnh break có ý nghĩa với vòng lặp gần nhất chứa nó.

**Xem xét ví dụ sau :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    int n = 5;
    for(int i = 1; i <= 5; i++){
        cout << i << " " << "codelab" << endl;
        if(i == 3){
            break;
        }
        cout << "C++ programming !\n";
    }
}
```

Output :

```cpp
1 codelab
C++ programming !
2 codelab
C++ programming !
3 codelab
```

**Giải thích :** 

1. Vòng lặp 1 : i = 1, in ra 1 codelab, break chưa thực hiện nên tiếp tục in ra C programming !
2. Vòng lặp 2 : i = 2, in ra 2 codelab, break chưa thực hiện nên tiếp tục in ra C programming !
3. Vòng lặp 3 : i = 3, in ra 3 codelab, do if đúng nên câu lệnh break được thực thi, vòng lặp kết thúc ngay mà không thực hiện câu lệnh in ra C programming !

Ví dụ 1 : Tìm Ước Chung Lớn Nhất của 2 số a và b

Ý tưởng : Duyệt từ số nhỏ hơn trong 2 số a và b về 1, nếu gặp số đầu tiên cả a và b chia hết thì in ra và dừng vòng lặp

```cpp
#include "iostream"

using namespace std;

int main(){
    int a = 18, b = 12;
    int min = a < b ? a : b;
    for(int i = min; i >= 1; i--){
        if((a % i == 0) && (b % i == 0)){
            cout << i << " ";
            break;
        }
    }
}
```

Output :

```cpp
6
```

Ví dụ 2 : In ra chữ số chẵn đầu tiên tính từ bên phải của số tự nhiên n

Ý tưởng : Tách từng chữ số của n bằng vòng lặp while, khi gặp chữ số chẵn thì dừng vòng lặp

```cpp
#include "iostream"

using namespace std;

int main(){
    int n = 12689791;
    while(n != 0){
        if(n % 2 == 0){ // n % 10 % 2 cũng được
            cout << n % 10 << endl; 
            break;
        }
        n /= 10;
    }
}
```

Output :

```cpp
8
```

Ví dụ 3 : Nhập 1 số nguyên từ bàn phím nếu nhập số âm thì yêu cầu nhập lại, nhập số không âm thì cho dừng

Ý tưởng : Dùng một vòng lặp lặp vĩnh viễn và kích hoạt câu lệnh break khi người dùng nhập số không âm

```cpp
#include "iostream"

using namespace std;

int main(){
    int n;
    while(true){
        cout << "Nhap n : ";
        cin >> n;
        if(n >= 0){
            break;
        }
        else{
            cout << "Nhap lai !\n";
        }
    }
}
```

Ví dụ 4 : Câu lệnh break với vòng for lồng nhau

```cpp
#include "iostream"

using namespace std;

int main(){
    for(int i = 1; i <= 2; i++){
        for(int j = 1; j <= 5; j++){
            cout << "codelab\n";
            if(j == 2){
                break; // có tác dụng dừng vòng for j
            }
            cout << "C++ programming !\n";
        }
    }
}
```

Output :

```cpp
codelab
C++ programming !
codelab
codelab
C++ programming !
codelab
```

---

**2.Câu Lệnh Continue** 

Câu lệnh continue khi được thực hiện nó sẽ bỏ qua các câu lệnh bên dưới nó trong vòng lặp và quay trở lại vòng lặp mới ngay.

Với vòng lặp lồng nhau thì câu lệnh continue có ý nghĩa với vòng lặp gần nhất chứa nó.

**Xem xét ví dụ sau :** 

```cpp
#include "iostream"

using namespace std;

int main(){
    for(int i = 1; i <= 4; i++){
        cout << "codelab\n";
        if(i % 2 == 0){
            continue;
        }
        cout << "C++\n";
    }
}
```

Output :

```cpp
codelab
C++
codelab
codelab
C++
codelab
```

**Giải thích :** 

1. Vòng lặp i = 1, in ra codelab, kiểm tra if không đúng nên tiếp tục thực hiện câu lệnh in ra C
2. Vòng lặp i = 2, in ra codelab, kiểm tra if đúng nên bỏ qua câu lệnh in ra C bên dưới mà quay trở lại luôn cập nhật i
3. Vòng lặp i = 3, in ra codelab, kiểm tra if không đúng nên tiếp tục thực hiện câu lệnh in ra C
4. Vòng lặp i = 4, in ra codelab, kiểm tra if đúng nên bỏ qua câu lệnh in ra C bên dưới mà quay trở lại luôn cập nhật i

Ví dụ 1 : Nhập vào các số tự nguyên, kết thúc nhập bằng cách nhập số 0 và chỉ tính tổng các số nguyên dương được nhập

```cpp
#include "iostream"

using namespace std;

int main(){
    int tong = 0, n;
    while(true){
        cout << "Nhap n : ";
        cin >> n;
        if(n < 0){
            continue; // bỏ qua các lệnh bên dưới
        }
        else if(n == 0){
            break;
        }
        tong += n;
    }
    cout << tong << endl;
}
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/04-04-cpp-cau-lenh-break-va-continue.md](solutions/04-04-cpp-cau-lenh-break-va-continue.md)

**Bài 1.** In các số từ 1 đến 20, nhưng dừng lại ngay khi gặp số chia hết cho 7.

**Bài 2.** In các số từ 1 đến 20, bỏ qua (không in) các số chia hết cho 3.

**Bài 3.** Nhập `n`, kiểm tra `n` có phải số nguyên tố không, dùng `break` để thoát sớm khi tìm thấy ước.

**Bài 4.** Nhập liên tục các số, dừng khi nhập số 0, in ra tổng các số dương (bỏ qua số âm bằng `continue`).

**Bài 5.** Tìm số đầu tiên trong khoảng [100, 1000] vừa chia hết cho 7 vừa chia hết cho 11.

**Bài 6.** In ra 10 số nguyên tố đầu tiên.

**Bài 7.** Dự đoán output rồi kiểm chứng:

```cpp
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    cout << i << " ";
}
cout << endl;
for (int i = 1; i <= 5; i++) {
    if (i == 3) break;
    cout << i << " ";
}
```

**Bài 8.** Chương trình sau bị **lặp vô hạn**. Tìm lỗi và sửa:

```cpp
int i = 1;
while (i <= 10) {
    if (i % 2 == 0) continue;
    cout << i << " ";
    i++;
}
```

**Bài 9.** Dùng vòng lặp lồng nhau in ra tất cả cặp `(i, j)` với `1 ≤ i, j ≤ 5`, nhưng dừng vòng trong khi `i + j > 6`.

**Bài 10.** `break` trong vòng lặp lồng nhau chỉ thoát vòng trong cùng. Viết chương trình chứng minh điều này, rồi đưa ra 2 cách thoát cả 2 vòng lặp.

**Bài 11.** Tìm cặp số `(a, b)` đầu tiên với `1 ≤ a, b ≤ 100` thoả `a² + b² = 2025`, dùng cờ để thoát cả 2 vòng lặp.

**Bài 12.** Nhập một dãy số, dừng khi gặp số âm. In ra số lớn nhất, bỏ qua các số bằng 0.

**Bài 13.** In ra các số từ 1 đến 100 nhưng bỏ qua các số vừa chia hết cho 3 vừa chia hết cho 5, và dừng khi tổng các số đã in vượt 1000.

**Bài 14.** Viết chương trình đọc điểm sinh viên: điểm hợp lệ 0–10 thì cộng vào tổng, điểm không hợp lệ thì `continue` (bỏ qua và báo lỗi), nhập `-1` thì `break`.

**Bài 15.** So sánh 3 cách thoát vòng lặp: `break`, `return`, `goto`. Nêu ưu nhược điểm và khi nào dùng cái nào.
