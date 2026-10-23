# [C]. Nhập Xuất Với scanf Và printf

Thao tác nhập dữ liệu từ bàn phím và hiển thị dữ liệu ra màn hình là thao tác đầu tiên bạn cần thành thạo khi học bất cứ ngôn ngữ lập trình nào. Bài viết này mình sẽ hướng dẫn các bạn nhập xuất một cách thành thạo với hai hàm **printf** và **scanf** của ngôn ngữ C

**NỘI DUNG :** 

- **In Ra Màn Hình Với printf**
- **Đặc Tả Định Dạng (Format Specifier)**
- **Độ Rộng Và Độ Chính Xác**
- **Nhập Từ Bàn Phím Với scanf**
- **Video Tutorial**

---

**1. In Ra Màn Hình Với printf**

printf là một hàm giúp bạn có thể hiển thị nội dung như : số nguyên, số thực, giá trị của biến, đoạn text ra màn hình. Để sử dụng hàm này bạn cần khai báo thư viện **stdio.h** (standard input output)

Cú pháp :

```
printf("chuoi dinh dang", gia_tri_1, gia_tri_2, ...);
```

- **Chuỗi định dạng** là đoạn text nằm trong cặp nháy kép, sẽ được in ra y nguyên, ngoại trừ các **đặc tả** bắt đầu bằng dấu `%` (ví dụ `%d`)
- Mỗi đặc tả là một "chỗ trống", sẽ được thay lần lượt bằng các giá trị phía sau theo đúng thứ tự
- Để xuống dòng bạn dùng ký tự đặc biệt `\n` đặt ở vị trí bạn muốn xuống dòng

```c
printf("hello codelab\n");          // Hiển thị dòng hello codelab lên màn hình và xuống dòng
printf("%d\n", 100);                // Hiển thị số 100 lên màn hình và xuống dòng
printf("%f\n", banKinh);            // Hiển thị giá trị của biến banKinh (kiểu double) lên màn hình
```

Ví dụ 1 :

```c
#include <stdio.h>

int main(){
    printf("codelab blog\n");
    printf("%s %s\n", "codelab.dev", "C programming !");
    printf("%d %d %d\n", 100, 200, 300);
    int n = 282828;
    printf("Gia tri cua bien n : %d\n", n);
    
    return 0;
}
```

Output :

```
codelab blog
codelab.dev C programming !
100 200 300
Gia tri cua bien n : 282828
```

Một số ký tự đặc biệt (escape sequence) hay dùng trong chuỗi định dạng :

| **Ký tự** | **Ý nghĩa** |
|---|---|
| `\n` | Xuống dòng |
| `\t` | Dấu tab |
| `\\` | In ra dấu `\` |
| `\"` | In ra dấu nháy kép `"` |
| `%%` | In ra dấu `%` (vì `%` đứng một mình là bắt đầu đặc tả) |

---

**2. Đặc Tả Định Dạng (Format Specifier)**

Khác với nhiều ngôn ngữ khác, printf **không tự biết** kiểu của giá trị bạn truyền vào, bạn phải chỉ rõ bằng đặc tả. Dùng sai đặc tả (ví dụ in số thực bằng `%d`) sẽ cho ra kết quả rác, vì vậy đây là phần bạn cần học thuộc.

| **Đặc tả** | **Kiểu dữ liệu** | **Ví dụ** |
|---|---|---|
| `%d` | `int` | `printf("%d", 28);` |
| `%lld` | `long long` | `printf("%lld", 1000000000000LL);` |
| `%u` | `unsigned int` | `printf("%u", 4000000000u);` |
| `%f` | `float`, `double` (mặc định 6 chữ số thập phân) | `printf("%f", 3.14);` → `3.140000` |
| `%e` | số thực dạng khoa học | `printf("%e", 12345.678);` → `1.234568e+04` |
| `%c` | `char` (một ký tự) | `printf("%c", 'A');` |
| `%s` | chuỗi ký tự | `printf("%s", "codelab");` |
| `%zu` | `size_t` (kiểu trả về của `sizeof`) | `printf("%zu", sizeof(int));` |

Ví dụ 2 : Kiểu `bool` trong C (thư viện **stdbool.h**) thực chất là số nguyên, giá trị true sẽ được hiển thị số 1, ngược lại giá trị false sẽ được hiển thị số 0.

C không có đặc tả riêng để in chữ `true`/`false`, nếu muốn hiển thị như vậy bạn tự chọn chuỗi cần in bằng toán tử điều kiện `? :` (sẽ học kỹ ở bài toán tử).

```c
#include <stdio.h>
#include <stdbool.h>

int main(){
    bool check = true;
    bool used = false;
    printf("%d %d\n", check, used);
    printf("%s\n", check ? "true" : "false");
    printf("%s\n", used ? "true" : "false");
    return 0;
}
```

Output :

```
1 0
true
false
```

Ví dụ 3 : In ký tự và mã ASCII của nó. Vì `char` cũng là một số nguyên nhỏ nên cùng một biến có thể in bằng `%c` (ra ký tự) hoặc `%d` (ra mã số)

```c
#include <stdio.h>

int main(){
    char c = 'A';
    long long big = 1000000000000LL;
    printf("%c %d\n", c, c);
    printf("%lld\n", big);
    printf("Kich thuoc int : %zu byte\n", sizeof(int));
    return 0;
}
```

Output :

```
A 65
1000000000000
Kich thuoc int : 4 byte
```

---

**3. Độ Rộng Và Độ Chính Xác**

**Lưu ý khi in giá trị của số thực float, double**

Đối với kiểu dữ liệu số thực, đề bài thường yêu cầu bạn in ra các số này với độ chính xác nhất định, cụ thể là bao nhiêu chữ số phần thập phân

Để in ra giá trị số float, double với độ chính xác k chữ số sau dấu phẩy bạn viết đặc tả dạng **%.kf**, ví dụ `%.2f` là 2 chữ số thập phân. Số sẽ được **làm tròn** chứ không bị cắt.

Ví dụ 4 :

```c
#include <stdio.h>

int main(){
    float a = 30.192387f;
    double b = 9.18293;
    printf("%.2f\n", a);
    printf("%.10f\n", b);
    printf("%f\n", b);
    return 0;
}
```

Output :

```
30.19
9.1829300000
9.182930
```

Mỗi lệnh printf là độc lập: `%.2f` chỉ có tác dụng cho đúng giá trị nó đứng trước, lần in sau dùng `%f` lại quay về mặc định 6 chữ số.

**Xác định độ rộng khi in**

Khi bạn muốn in ra giá trị của 1 số, 1 biến hay đoạn text với độ rộng tương đương bao nhiêu ký tự bạn thêm số k vào giữa `%` và chữ cái đặc tả, ví dụ `%10d`. Nếu nội dung ngắn hơn k ký tự, phần thiếu sẽ được đệm dấu cách ở **bên trái** (căn phải).

- `%-10d` : thêm dấu trừ để **căn trái**, phần thiếu đệm dấu cách ở bên phải
- `%010d` : thêm số 0 đứng trước để đệm bằng **số 0** thay cho dấu cách (chỉ dùng cho số)
- `%8.2f` : kết hợp cả độ rộng 8 và 2 chữ số thập phân

Ví dụ 5:

```c
#include <stdio.h>

int main(){
    int n = 12345;
    printf("%10d|\n", n);
    printf("%010d|\n", n);
    printf("%-10d|\n", n);
    printf("%10s|\n", "codelab");
    printf("%8.2f|\n", 3.14159);
    return 0;
}
```

Output :

```
     12345|
0000012345|
12345     |
   codelab|
    3.14|
```

(Dấu `|` được in thêm để bạn thấy rõ vị trí kết thúc của mỗi ô.)

---

**4. Nhập Từ Bàn Phím Với scanf**

scanf là hàm giúp bạn có thể nhập dữ liệu từ bàn phím thay vì khởi tạo thủ công, scanf cũng nằm trong thư viện **stdio.h** và dùng các đặc tả giống printf

Cú pháp :

```
scanf("chuoi dac ta", &bien_1, &bien_2, ...);
```

```c
scanf("%d", &a);                  // Nhập giá trị cho a từ bàn phím
scanf("%d%d%d", &x, &y, &z);      // Nhập giá trị cho 3 biến x, y, z lần lượt từ bàn phím
```

**Dấu & bắt buộc phải có trước tên biến.** `&a` là **địa chỉ** của biến a trong bộ nhớ, scanf cần biết địa chỉ này để ghi giá trị vừa nhập vào đúng chỗ (bạn sẽ hiểu kỹ hơn ở chương con trỏ). Quên dấu `&` là lỗi rất hay gặp, chương trình vẫn biên dịch được nhưng sẽ chạy sai hoặc bị dừng đột ngột. Bật `-Wall` khi biên dịch để gcc cảnh báo lỗi này.

Khi nhập dữ liệu từ bàn phím bạn sẽ nhập dữ liệu xong sau đó enter, nếu bạn nhập nhiều số cùng 1 lúc thì cần có dấu cách giữa các số sau đó ấn enter sau số cuối cùng

Ví dụ trong câu lệnh thứ 2 ở trên khi nhập x, y, z thì bạn có thể nhập từng số rồi enter hoặc nhập 3 số cách nhau 1 dấu cách rồi mới enter cũng được.

Ví dụ 1 :

```c
#include <stdio.h>

int main(){
    int n, a, b, c;
    printf("Nhap gia tri cho n : ");
    scanf("%d", &n);
    printf("Gia tri n vua nhap la : %d\n", n);
    printf("Nhap gia tri cho a, b, c : ");
    scanf("%d%d%d", &a, &b, &c);
    printf("Gia tri a, b, c : %d %d %d\n", a, b, c);
    return 0;
}
```

**Bảng đặc tả khi nhập (chú ý khác với printf ở kiểu double) :**

| **Kiểu biến** | **scanf** | **printf** |
|---|---|---|
| `int` | `%d` | `%d` |
| `long long` | `%lld` | `%lld` |
| `float` | `%f` | `%f` |
| `double` | **`%lf`** | `%f` |
| `char` | `%c` (thường viết `" %c"`) | `%c` |
| chuỗi `char s[]` | `%s` (**không** có `&`) | `%s` |

Ví dụ 2 : Nhập số thực, ký tự và chuỗi

```c
#include <stdio.h>

int main(){
    double diem;
    char xepLoai;
    char ten[50];
    printf("Nhap ten (viet lien) : ");
    scanf("%49s", ten);
    printf("Nhap diem : ");
    scanf("%lf", &diem);
    printf("Nhap xep loai (A/B/C) : ");
    scanf(" %c", &xepLoai);
    printf("%s - %.2f - %c\n", ten, diem, xepLoai);
    return 0;
}
```

Ví dụ chạy :

```
Nhap ten (viet lien) : codelab
Nhap diem : 8.756
Nhap xep loai (A/B/C) : A
codelab - 8.76 - A
```

Giải thích những điểm cần chú ý :

- **double phải nhập bằng %lf**, dùng `%f` cho double trong scanf sẽ đọc sai giá trị. Khi in bằng printf thì `%f` dùng được cho cả float lẫn double.
- **Dấu cách trước %c** : sau khi nhập điểm, ký tự Enter vẫn còn nằm trong bộ đệm. `%c` đọc cả dấu cách và Enter nên sẽ "nuốt" luôn ký tự Enter đó. Viết `" %c"` (có dấu cách phía trước) để scanf bỏ qua mọi khoảng trắng rồi mới đọc ký tự.
- **Chuỗi không có &** : tên mảng `ten` bản thân nó đã là địa chỉ nên không viết `&ten`. Số 49 trong `%49s` giới hạn số ký tự đọc vào để không tràn mảng 50 phần tử (chừa 1 chỗ cho ký tự kết thúc chuỗi).
- `%s` chỉ đọc tới **khoảng trắng đầu tiên**, vì vậy nó chỉ nhập được một từ. Cách nhập cả dòng có dấu cách sẽ được học ở chương chuỗi ký tự.

---

**Video hướng dẫn Nhập Xuất trong C :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-05-c-nhap-xuat-voi-scanf-va-printf.md](solutions/02-05-c-nhap-xuat-voi-scanf-va-printf.md)

**Bài 1.** Nhập vào họ tên (không dấu, viết liền), tuổi và điểm trung bình của một sinh viên rồi in ra màn hình theo dạng:
`Sinh vien <ten>, <tuoi> tuoi, diem TB: <diem>`

**Bài 2.** Nhập 2 số nguyên `a`, `b` trên cùng một dòng, in ra tổng, hiệu, tích, thương của chúng.

**Bài 3.** Nhập vào bán kính hình tròn (số thực), tính và in ra chu vi, diện tích với **đúng 2 chữ số thập phân**.

**Bài 4.** Nhập một số thực, in ra số đó với lần lượt 0, 3, 6, 10 chữ số thập phân.

**Bài 5.** Nhập 3 số nguyên và in chúng ra theo cột, mỗi số chiếm độ rộng 10 ký tự, căn phải.

**Bài 6.** Làm lại bài 5 nhưng phần trống được lấp bằng dấu `*`. (Gợi ý: printf chỉ tự đệm được dấu cách hoặc số `0`, hãy tìm cách khác.)

**Bài 7.** Nhập một số nguyên có tối đa 6 chữ số, in ra số đó với độ rộng 8, các chỗ trống được điền số `0` ở phía trước (ví dụ `123` → `00000123`).

**Bài 8.** In ra bảng cửu chương 5 dưới dạng bảng có căn lề đẹp bằng đặc tả độ rộng:

```
 5 x  1 =  5
 5 x  2 = 10
 ...
 5 x 10 = 50
```

**Bài 9.** Nhập vào một số 0 hoặc 1, lưu vào biến `bool` rồi in ra dưới dạng `true`/`false`.

**Bài 10.** Nhập một ký tự và in ra: ký tự đó, mã ASCII của nó, và ký tự đứng ngay sau nó trong bảng mã.

**Bài 11.** Viết chương trình in ra bảng thông tin 3 sản phẩm (tên, số lượng, đơn giá, thành tiền) căn lề bằng đặc tả độ rộng: cột chữ căn trái (`%-...s`), cột số căn phải.

**Bài 12.** Nhập vào tổng số giây, in ra dưới dạng `hh:mm:ss` với mỗi phần luôn có 2 chữ số (ví dụ `3725` → `01:02:05`).

**Bài 13.** Chạy chương trình sau và giải thích vì sao dòng thứ hai lại in ra 6 chữ số thập phân chứ không phải 3:

```c
printf("%.3f\n", 1.23456);
printf("%f\n", 9.87654);
```

**Bài 14.** Nhập vào tên (có dấu cách, ví dụ `Nguyen Van A`) và in ra. Nếu chỉ dùng `scanf("%s", ...)` thì kết quả có gì bất thường? Hãy thử và ghi lại.

**Bài 15.** Nhập điểm 3 môn của 3 sinh viên rồi in ra bảng điểm hoàn chỉnh có tiêu đề, đường kẻ, cột điểm trung bình lấy 2 chữ số thập phân.
