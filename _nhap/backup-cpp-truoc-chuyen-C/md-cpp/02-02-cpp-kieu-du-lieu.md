# [C++]. Kiểu Dữ Liệu

Kiểu Dữ Liệu trong ngôn ngữ lập trình C++ giúp bạn lưu trữ giá trị về số, ký tự, chuỗi ký tự, ... Trong bài viết này cùng mình điểm qua các kiểu dữ liệu chính thông dụng trong ngôn ngữ lập trình C++

**NỘI DUNG :** 

- **Kiểu Dữ Liệu Số Nguyên**
- **Kiểu Dữ Liệu Số Thực**
- **Kiểu Ký Tự**
- **Kiểu Đúng Sai**
- **Video Tutorial**

**1. Kiểu Dữ Liệu Số Nguyên**

Bảng sau liệt kê các kiểu dữ liệu số nguyên phổ biến trong ngôn ngữ lập trình C++

| **Kiểu dữ liệu** | **Kích thước (byte)** | **Giá trị có thể lưu** | **Phạm vi giá trị có thể lưu** |
| short | 2 | Số nguyên | -32,768 -> 32,767 |
| unsigned short | 2  | Số nguyên không âm | 0 -> 65,535 |
| int | 4 | Số nguyên | -2,147,483,648 -> 2,147,483,647 |
| unsigned int | 4 | Số nguyên không âm | 0 -> 4,294,967,295 |
| long long | 8 | Số nguyên | -9223372036854775808 -> 9223372036854775807 |
| unsigned long long | 8 | Số nguyên không âm | 0 -> 18446744073709551615 |

Dựa theo số byte mà kiểu dữ liệu cần để lưu trữ bạn có thể tính ra phạm vi giá trị mà số nguyên đó có thể lưu trữ.

Cách tính giới hạn của các kiểu dữ liệu số nguyên như sau : Từ số byte mà kiểu dữ liệu này cần để lưu trữ trong bộ nhớ bạn có thể tính ra số bit mà nó dùng để biểu diễn số nguyên (1 byte bằng 8 bit) . Từ số bit này bạn suy ra như sau

- Số nguyên có dấu : Kiểu dữ liệu có K bit sẽ lưu được giá trị từ 2(K - 1) tới 2(K-1) - 1, ví dụ kiểu **int** có 4 byte tương đương 32 bit sẽ lưu giá trị từ 231 tới 231 - 1
- Số nguyên không dấu : Kiểu dữ liệu có K bit sẽ lưu được giá trị từ 0 tới 2K - 1, ví dụ **unsigned int** có 4 byte sẽ lưu giá trị từ 0 tới 232 - 1

Thông thường kiểu dữ liệu số nguyên sẽ có kiểu không dấu tương ứng của nó, kiểu dữ liệu số nguyên sẽ sử dụng 1 bit để lưu dấu âm hay dấu dương còn kiểu số nguyên không dấu sẽ không cần bit để lưu dấu nên giải giá trị của nó thường gấp đôi giải giá trị của số nguyên có dấu tương ứng. Ví dụ số nguyên int có 32 bit thì sẽ mất 1 bit để lưu dấu còn 31 bit biểu diễn giá trị số, còn số nguyên unsigned int sẽ dùng cả 32 bit này để biểu diễn số.

**Một số lưu ý khi sử dụng số nguyên** :

- Số nguyên không thể lưu được phần thập phân
- Số nguyên sẽ bị tràn giá trị nếu bạn gán cho nó giá trị vượt phạm vi của nó có thể lưu
- Thông thường bạn chỉ sử dụng int và long long, ít khi sử dụng short.
- Nếu lưu số nguyên từ -2.109 tới 2.109 thì dùng int là đủ, nếu ngoài phạm vi này dùng long long

---

**2. Kiểu Dữ Liệu Số Thực**

Khi bạn muốn lưu kiểu dữ liệu có phần thập phân bạn cần sử dụng kiểu dữ liệu số thực, trong C++ có 3 kiểu dữ liệu lưu số thực gồm : float, double, long double

Khi sử dụng kiểu dữ liệu số thực bạn cần biết các kiểu dữ liệu này có thể lưu được bao nhiêu số sau dấu phảy thập phân để lựa chọn kiểu dữ liệu cho phù hợp với độ chính xác mong muốn của bài toán.

| **Kiểu dữ liệu** | **Kích thước (byte)** | **Độ chính xác** |
| float | 4 | 6 - 9 chữ số thập phân |
| double | 8 | 15 - 18 chữ số thập phân  |
| long double | 16  | 33 - 36 chữ số thập phân |

Kiểu dữ liệu số thực có thể lưu được số nguyên tuy nhiên bạn không nên sử dụng nó để lưu số nguyên vì bản chất số thực luôn có sai số nhất định và không thể lưu giá trị số thực đúng tuyệt đối 100%. Thông thường thì mình sẽ dùng số thực double trong các bài toán khi kết quả cần lưu phần thập phân.

---

**3. Kiểu Dữ Liệu Ký Tự**

Khi bạn cần lưu trữ một ký tự trong C++ thì bạn sử dụng kiểu dữ liệu char, thực tế char cũng được sử dụng để lưu số nguyên.

Tuy nhiên mỗi ký tự mà bạn thường sử dụng đều có mã ASCII tương ứng, thời điểm hiện tại bạn sẽ chưa biết mã ASCII là gì tuy nhiên bạn chỉ cần nhớ rằng char có thể lưu được số nguyên hoặc lưu được kí tự.

Các ký tự như : chữ cái, chữ số, kí tự đặc biệt... đều có thể lưu trữ bằng kiểu dữ liệu char

| **Kiểu dữ liệu** | **Kích thước (byte)** | **Giá trị có thể lưu** | **Phạm vi giá trị có thể lưu** |
| char | 1 | Số nguyên hoặc ký tự | -128 -> 127 |
| unsigned char | 1 | Số nguyên không âm hoặc ký tự | 0 -> 255 |

---

**4. Kiểu Đúng Sai**

Kiểu đúng sai hay luận lý được sử dụng để lưu trữ giá trị đúng (true) hoặc sai (false)

Trong ngôn ngữ lập trình C++ thì kiểu bool được sử dụng để lưu các giá trị đúng sai.

Kiểu dữ liệu này có kích thước là 1 byte

---

**Video hướng dẫn Kiểu Dữ Liệu và Biến trong C++ :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-02-cpp-kieu-du-lieu.md](solutions/02-02-cpp-kieu-du-lieu.md)

**Bài 1.** Viết chương trình in ra kích thước (số byte) của các kiểu: `char`, `bool`, `short`, `int`, `long long`, `float`, `double`, `long double` bằng toán tử `sizeof`.

**Bài 2.** Với mỗi kiểu số nguyên trong bảng của bài học, hãy tự tính lại phạm vi giá trị dựa vào số byte, rồi kiểm chứng bằng `numeric_limits` trong thư viện `<limits>`.

**Bài 3.** Chọn kiểu dữ liệu phù hợp nhất (tiết kiệm bộ nhớ nhất) để lưu các giá trị sau, giải thích lý do:

a) Tuổi của một người &nbsp;&nbsp; b) Dân số Việt Nam &nbsp;&nbsp; c) Dân số thế giới
d) Điểm trung bình môn &nbsp;&nbsp; e) Giới tính (nam/nữ) &nbsp;&nbsp; f) Ký tự xếp loại (A/B/C/D)
g) Số tiền trong tài khoản ngân hàng (VNĐ) &nbsp;&nbsp; h) Số ngày trong tháng

**Bài 4.** Khai báo một biến `int` và gán cho nó giá trị `3000000000`. In ra kết quả và giải thích hiện tượng quan sát được.

**Bài 5.** Viết chương trình minh hoạ **tràn số** (overflow): gán cho biến `short` giá trị lớn nhất của nó, rồi cộng thêm 1 và in kết quả.

**Bài 6.** Viết chương trình tính `2^31` bằng 2 cách: dùng `int` và dùng `long long`. So sánh 2 kết quả.

**Bài 7.** Khai báo biến `float` và `double` cùng gán giá trị `1.0/3.0`. In cả hai với 20 chữ số thập phân và giải thích sự khác nhau.

**Bài 8.** Chạy đoạn code sau và giải thích vì sao kết quả không phải `true`:

```cpp
double a = 0.1 + 0.2;
cout << (a == 0.3) << endl;
cout << setprecision(20) << a << endl;
```

**Bài 9.** Khai báo một biến `char` gán giá trị `'A'`. In ra biến đó ở dạng ký tự và dạng số nguyên.

**Bài 10.** Viết chương trình gán cho biến `char` giá trị `65`, `97`, `48` rồi in ra dưới dạng ký tự. Bạn thấy điều gì?

**Bài 11.** Khai báo biến `bool` và gán lần lượt các giá trị `0`, `1`, `5`, `-3`, `0.0`. In ra kết quả và rút ra kết luận.

**Bài 12.** Khai báo một biến `int` **không khởi tạo giá trị** rồi in ra. Chạy 3 lần, ghi lại kết quả và giải thích.

**Bài 13.** Viết chương trình khai báo đủ 6 kiểu (`int`, `long long`, `float`, `double`, `char`, `bool`) lưu thông tin một sinh viên: mã SV, số CMND, chiều cao, điểm TB, xếp loại, đã tốt nghiệp hay chưa. In tất cả ra màn hình.

**Bài 14.** Tìm hiểu và giải thích: vì sao `unsigned int` có phạm vi gấp đôi `int` nhưng cùng chiếm 4 byte?

**Bài 15.** Chạy đoạn code sau, dự đoán kết quả trước rồi giải thích:

```cpp
unsigned int a = 0;
a = a - 1;
cout << a << endl;
```
