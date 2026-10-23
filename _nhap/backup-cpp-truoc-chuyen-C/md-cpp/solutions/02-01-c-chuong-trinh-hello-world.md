# Lời giải — [C++]. Chương Trình Hello World

[← Quay lại bài học](../02-01-c-chuong-trinh-hello-world.md)

---

### Bài 1.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Xin chao, toi dang hoc C++" << endl;
    return 0;
}
```

### Bài 2.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Ho ten: Nguyen Van A" << endl;
    cout << "Lop: 12A1" << endl;
    cout << "So thich: Lap trinh" << endl;
    return 0;
}
```

### Bài 3.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Ho ten: Nguyen Van A\nLop: 12A1\nSo thich: Lap trinh\n";
    return 0;
}
```

**Giải thích:** `\n` là **ký tự** xuống dòng nằm ngay trong chuỗi, nên gộp được cả 3 dòng vào một lệnh `cout`.

### Bài 4.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "**********" << endl;
    cout << "**********" << endl;
    cout << "**********" << endl;
    cout << "**********" << endl;
    cout << "**********" << endl;
    return 0;
}
```

Hoặc gọn hơn:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "**********\n**********\n**********\n**********\n**********\n";
    return 0;
}
```

### Bài 5.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "*\n";
    cout << "**\n";
    cout << "***\n";
    cout << "****\n";
    cout << "*****\n";
    return 0;
}
```

*(Sau khi học vòng lặp `for` ở chương 4, bạn sẽ viết bài này chỉ bằng 3 dòng.)*

### Bài 6.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "  #####  " << endl;
    cout << " #     # " << endl;
    cout << "#        " << endl;
    cout << "#        " << endl;
    cout << "#        " << endl;
    cout << " #     # " << endl;
    cout << "  #####  " << endl;
    return 0;
}
```

### Bài 7.

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World !" << std::endl;
    std::cout << "codelab tutorial !" << std::endl;
    return 0;
}
```

**Giải thích:** `cout` và `endl` được định nghĩa trong namespace `std`. Không có dòng `using namespace std;` thì phải viết đầy đủ `std::cout`, `std::endl`. Toán tử `::` gọi là **toán tử phân giải phạm vi** (scope resolution operator).

### Bài 8.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Toi thich ngon ngu \"C++\" nhat." << endl;
    return 0;
}
```

**Giải thích:** dấu `"` dùng để đánh dấu đầu/cuối chuỗi, nên muốn in chính dấu `"` phải **thoát ký tự** bằng `\"`.

Các ký tự thoát (escape sequence) thường gặp:

| Viết | Ý nghĩa |
|---|---|
| `\n` | Xuống dòng |
| `\t` | Dấu tab |
| `\\` | Dấu `\` |
| `\"` | Dấu nháy kép |
| `\'` | Dấu nháy đơn |
| `\0` | Ký tự null (kết thúc chuỗi C) |

### Bài 9.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "C:\\Users\\Admin\\Documents\\cpp" << endl;
    return 0;
}
```

**Giải thích:** `\` là ký tự mở đầu chuỗi thoát, nên muốn in một dấu `\` phải viết `\\`.

⚠️ Nếu viết `cout << "C:\Users\Admin";` thì `\U` và `\A` không phải chuỗi thoát hợp lệ → compiler cảnh báo và kết quả sai.

Từ C++11 có thể dùng **raw string literal** để khỏi phải nhân đôi:

```cpp
cout << R"(C:\Users\Admin\Documents\cpp)" << endl;
```

### Bài 10.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "STT\tTen\t\tDiem" << endl;
    cout << "1\tAn\t\t9.5" << endl;
    cout << "2\tBinh\t8.0" << endl;
    cout << "3\tChi\t\t7.5" << endl;
    return 0;
}
```

**Giải thích:** `\t` nhảy tới mốc tab tiếp theo (thường cách nhau 8 ký tự). Vì "An" và "Chi" ngắn hơn "Binh", chúng cần **2 tab** mới sang được cột kế tiếp.

Đây chính là nhược điểm của `\t`: căn lề không ổn định. Cách chuẩn hơn là dùng `setw()` (xem bài [02-05](../02-05-cpp-nhap-xuat-voi-cin-va-cout.md)):

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    cout << left << setw(6) << "STT" << setw(10) << "Ten" << "Diem" << endl;
    cout << left << setw(6) << 1 << setw(10) << "An"   << 9.5 << endl;
    cout << left << setw(6) << 2 << setw(10) << "Binh" << 8.0 << endl;
    cout << left << setw(6) << 3 << setw(10) << "Chi"  << 7.5 << endl;
    return 0;
}
```

### Bài 11.

**Output:**

```
A
```

**Giải thích:** `return 0;` kết thúc hàm `main` ngay lập tức, tức là kết thúc chương trình. Mọi câu lệnh phía sau nó **không bao giờ được thực thi** — gọi là *dead code* (mã chết).

Nếu biên dịch với `-Wall`, compiler sẽ cảnh báo:

```
warning: will never be executed [-Wunreachable-code]
```

### Bài 12.

4 lỗi trong chương trình:

| # | Lỗi | Sửa |
|---|---|---|
| 1 | `Cout` viết hoa chữ C — C++ **phân biệt hoa thường** | `cout` |
| 2 | Thiếu `;` sau `cout << "Hello World"` | thêm `;` |
| 3 | Thiếu `;` sau `return 0` | thêm `;` |
| 4 | Thiếu `using namespace std;` (hoặc phải viết `std::cout`) | thêm dòng `using namespace std;` |

Chương trình sau khi sửa:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World";
    return 0;
}
```

### Bài 13.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Chuong trinh ket thuc voi ma 1" << endl;
    return 1;
}
```

Kiểm tra mã thoát:

```bash
# Linux / macOS
g++ baitap13.cpp -o baitap13
./baitap13
echo $?        # in ra: 1
```

```bat
REM Windows (cmd)
g++ baitap13.cpp -o baitap13.exe
baitap13.exe
echo %errorlevel%     REM in ra: 1
```

**Giải thích:** giá trị `main` trả về chính là **mã thoát (exit code)** báo cho hệ điều hành biết chương trình kết thúc thế nào. Theo quy ước: `0` = thành công, khác `0` = có lỗi. Các script tự động (build script, CI) dựa vào mã này để biết bước trước có thành công hay không.

### Bài 14.

```cpp
#include <iostream>
using namespace std;

int main() {
    // "\n" chi la mot KY TU xuong dong, duoc ghi vao bo dem (buffer)
    cout << "Dong 1 dung \\n" << "\n";

    // endl vua xuong dong VUA day (flush) toan bo bo dem ra man hinh ngay lap tuc
    cout << "Dong 2 dung endl" << endl;

    return 0;
}
```

| | `"\n"` | `endl` |
|---|---|---|
| Bản chất | Một ký tự trong chuỗi | Một hàm điều khiển (manipulator) |
| Chức năng | Xuống dòng | Xuống dòng **+ flush bộ đệm** |
| Tốc độ | Nhanh hơn | Chậm hơn (mỗi lần flush là một lời gọi hệ thống) |
| Nên dùng khi | In nhiều dữ liệu, bài thi đấu | Cần thấy kết quả ngay (debug), chương trình có thể crash |

**Flush là gì:** `cout` không ghi thẳng ra màn hình mà gom dữ liệu vào một vùng nhớ đệm (buffer), đầy mới đẩy ra một lần cho nhanh. `endl` ép đẩy ngay lập tức.

**Khuyến nghị:** khi in hàng nghìn dòng (bài thi đấu), dùng `"\n"` thay vì `endl` — chênh lệch tốc độ có thể tới vài lần.

### Bài 15.

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "+----------------------------+" << endl;
    cout << "|                            |" << endl;
    cout << "|      NGUYEN VAN A          |" << endl;
    cout << "|      C++ Developer         |" << endl;
    cout << "|      nguyenvana@mail.com   |" << endl;
    cout << "|                            |" << endl;
    cout << "+----------------------------+" << endl;
    return 0;
}
```

**Mẹo căn khung:** đếm số ký tự của dòng viền trên (`+` + 28 dấu `-` + `+` = 30 ký tự). Mọi dòng bên trong cũng phải đúng 30 ký tự: `|` + 28 ký tự nội dung (đệm bằng dấu cách) + `|`.
