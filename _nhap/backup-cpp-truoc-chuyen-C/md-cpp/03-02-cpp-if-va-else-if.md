# [C++]. If và Else If

Cấu trúc rẽ nhánh với câu lệnh **if else if** giúp bạn có thể kiểm tra nhiều điều kiện khác nhau thay vì một điều kiện duy nhất

**NỘI DUNG :** 

- **If else if**
- **Bài tập áp dụng**
- **Video tutorial**

**1.If Và Else If**

Trong trường hợp bài toán của bạn có nhiều rẽ nhánh khác nhau với các điều kiện tương ứng, nếu chỉ dùng if else thì bạn phải sử dụng if else lồng nhau dẫn tới code trở nên dài dòng và phức tạp.

If và else if giúp bạn có thể kiểm tra nhiều điều kiện và nó chỉ thực hiện duy nhất 1 khối lệnh trong các rẽ nhánh đó.

**Cú pháp :** 

```cpp
if(điều_kiện_1){
    //code 1
}
else if(điều_kiện_2){
    //code 2
}
else if(điều_kiện_3){
    //code 3
}
...
else if(điều_kiện_n){
    //code n
}
else{
    //Code else
}
```

**Lưu ý khi sử dụng if và else if :**

- Bạn có thể kiểm tra bao nhiêu điều kiện tùy ý
- Khối lệnh else có thể có hoặc không
- Khi rẽ nhánh nào được thực hiện thì các nhánh khác sẽ không được thực hiện, cấu trúc sẽ kết thúc

---

**2.Bài Tập Áp Dụng**

**Bài 1**. Nhập tháng và năm in ra số ngày của tháng, chú ý tháng 2 của năm nhuận có 29 ngày

```cpp
#include "iostream"

using namespace std;

int main(){
    int m, y;
    cout << "Nhap thang, nam : ";
    cin >> m >> y;
    if(m == 1 || m == 3 || m == 5 || m == 7 || m == 8 || m == 10 || m == 12){
        cout << 31 << endl;
    }
    else if(m == 4 || m == 6 || m == 9 || m == 11){
        cout << 30 << endl;
    }
    else if(m == 2){
        if((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0)){
            cout << 29 << endl;
        }
        else{
            cout << 28 << endl;
        }
    }
    else{
        cout << "Thang khong hop le !\n";
    }
}
```

**Bài 2**. Nhập 3 cạnh của tam giác là số nguyên, nếu 3 cạnh của tam giác đều in 1, cân in 2, vuông in 3, thường in 4. Giả sử 3 cạnh đã là 3 cạnh của tam giác hợp lệ

```cpp
#include "iostream"

using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    if(a == b && b == c){
        cout << 1 << endl;
    }
    else if((a == b) || (b == c) || (a == c)){
        cout << 2 << endl;
    }
    else if((a * a == b * b + c * c) || (b * b == a * a + c * c) || (c * c == a * a + b * b)){
        cout << 3 << endl;
    }
    else{
        cout << 4 << endl;
    }
}
```

---

**Video Tutorial :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/03-02-cpp-if-va-else-if.md](solutions/03-02-cpp-if-va-else-if.md)

**Bài 1.** Nhập một tháng (1–12), in ra tháng đó thuộc quý mấy trong năm.

**Bài 2.** Nhập một tháng và năm, in ra số ngày của tháng đó (chú ý năm nhuận).

**Bài 3.** Nhập số thứ tự ngày trong tuần (2–8), in ra tên ngày tương ứng (2 = Thứ Hai, …, 8 = Chủ Nhật).

**Bài 4.** Nhập điểm số từ 0–100, quy đổi sang thang chữ: A (≥90), B (≥80), C (≥70), D (≥60), F (<60).

**Bài 5.** Nhập chỉ số BMI, in ra phân loại: <18.5 Thiếu cân, 18.5–24.9 Bình thường, 25–29.9 Thừa cân, ≥30 Béo phì.

**Bài 6.** Nhập chiều cao (m) và cân nặng (kg), tính BMI rồi phân loại như bài 5.

**Bài 7.** Nhập 3 cạnh tam giác (số nguyên). In 1 nếu đều, 2 nếu cân, 3 nếu vuông, 4 nếu thường.

**Bài 8.** Nhập một ký tự, dùng chuỗi `else if` xác định nó là nguyên âm, phụ âm, chữ số hay ký tự khác.

**Bài 9.** Nhập nhiệt độ (°C), in ra: <0 "Bang gia", 0–15 "Lanh", 16–25 "Mat me", 26–35 "Nong", >35 "Rat nong".

**Bài 10.** Nhập số tiền và loại khách (1 = thường, 2 = thân thiết, 3 = VIP). Tính giảm giá lần lượt 0%, 10%, 20%.

**Bài 11.** Viết chương trình máy tính bỏ túi: nhập 2 số và một phép toán (`+`, `-`, `*`, `/`, `%`), in ra kết quả. Dùng `else if`.

**Bài 12.** Nhập một số nguyên `n` từ 1–999. In ra `n` có mấy chữ số.

**Bài 13.** Chương trình sau luôn in ra "Trung binh" dù nhập 9.5. Tìm lỗi và sửa:

```cpp
double d; cin >> d;
if (d >= 5.0) cout << "Trung binh";
else if (d >= 7.0) cout << "Kha";
else if (d >= 8.5) cout << "Gioi";
```

**Bài 14.** So sánh 2 cách viết dưới đây. Cách nào hiệu quả hơn khi `n = 100`? Vì sao?

```cpp
// Cach A
if (n < 10) ...
if (n >= 10 && n < 100) ...
if (n >= 100) ...

// Cach B
if (n < 10) ...
else if (n < 100) ...
else ...
```

**Bài 15.** Nhập giờ (0–23) và phút, in ra lời chào phù hợp và cho biết đang ở buổi sáng/trưa/chiều/tối, kèm định dạng giờ 12h (AM/PM).
