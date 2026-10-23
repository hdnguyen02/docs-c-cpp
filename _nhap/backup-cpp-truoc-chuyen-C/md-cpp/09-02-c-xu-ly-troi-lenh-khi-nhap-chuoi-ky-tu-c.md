# [C++]. Xử Lý Trôi Lệnh Khi Nhập Chuỗi Ký Tự C++

Khi nhập xâu ký tự từ bàn phím trong C++ bằng hàm getline() đôi khi bạn sẽ thấy lệnh này bị trôi qua mà không thể nhập được nội dung cho nó. Trong bài học này mình sẽ giải thích lý do xảy ra trôi lệnh và cách xử lý.

**NỘI DUNG :**

- **Nguyên Nhân Và Cách Khắc Phục**
- **Video Tutorial** 

---

**Nguyên Nhân Và Cách Khắc Phục**

Bạn thử chạy mã nguồn sau và sẽ thấy sau khi nhập số cho n và ấn enter thì chưa kịp nhập nội dung cho xâu s đã bị trôi qua câu lệnh đó

Nội dung của xâu s là rỗng

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
    int n; 
    cout << "Nhap n : "; 
    cin >> n;
    string s;
    cout << "Nhap xau s : ";
    getline(cin, s);
    cout << "So n da nhap : " << n << endl;
    cout << "Xau s : " << s << endl;
    return 0;
}
```

**Nguyên nhân :** 

Hàm getline() khi bạn nhập xâu s sẽ dừng nhập cho tới khi nó gặp được ký tự xuống dòng (enter), những ký tự nó đọc được từ luồng vào cin cho tới kí tự enter đó sẽ được gán cho string s.

Khi bạn nhập cin >> n sau đó ấn enter, thì giá trị mà bạn vừa nhập sẽ được gán cho n tuy nhiên ký tự enter ở cuối bạn nhập sẽ nằm trong luồng vào cin, khi hàm getline() đọc từ luồng cin thì sẽ gặp ký tự enter này do cin ở câu lệnh trên để lại.

Do getline() sẽ dừng nhập khi gặp enter nên nó sẽ dừng ngay tại lúc đó mà chưa hề nhập được ký tự nào và dẫn đến xâu s của bạn là một xâu rỗng

Vậy nếu trước hàm getline() mà trong luồng cin có thừa kí tự enter(thông thường do cin ở câu lệnh trước đó để lại) thì sẽ xảy ra trôi lệnh.

Lưu ý rằng nếu bạn dùng câu lệnh getline() sau một câu lệnh getline() thì bạn sẽ không bị trôi lệnh vì hàm getline() sẽ xử lý ký tự enter ở cuối dòng chứ không để lại trong luồng vào như câu lệnh cin.

**Cách khắc phục :** 

Khi bạn biết nguyên nhân getline() bị trôi lệnh là do đọc phải ký tự enter thừa trong luồng vào từ bàn phím nên để xử lý việc này bạn chỉ cần loại bỏ được ký tự enter này trước khi dùng getline().

Bạn có thể dùng hàm **cin.ignore(1)** hoặc** cin.ingore()** để loại bỏ đi 1 ký tự trong luồng cin, khi đó ký tự enter sẽ bị loại bỏ và hàm getline() sẽ đợi bạn nhập nội dung sau đó ấn enter.

Ngoài ra bạn cũng có thể sử dụng hàm getchar() vì hàm này sẽ đọc 1 ký tự trong luồng cin và đọc được ký tự enter thừa.

Bây giờ bạn có thể chạy lại mã nguồn này và kiểm tra

```cpp
#include "iostream"
#include "string"
using namespace std;

int main(){
    int n; 
    cout << "Nhap n : "; 
    cin >> n;
    string s;
    cout << "Nhap xau s : ";
    cin.ignore();
    getline(cin, s);
    cout << "So n da nhap : " << n << endl;
    cout << "Xau s : " << s << endl;
    return 0;
}
```

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi-ky-tu-c.md](solutions/09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi-ky-tu-c.md)

**Bài 1.** Chạy chương trình sau, mô tả hiện tượng và giải thích:

```cpp
int n; string s;
cin >> n;
getline(cin, s);
cout << "n = " << n << ", s = [" << s << "]";
```

**Bài 2.** Sửa chương trình bài 1 bằng `cin.ignore()`.

**Bài 3.** Nhập tuổi (số) rồi nhập họ tên (có dấu cách) — xử lý đúng trôi lệnh.

**Bài 4.** Nhập `n`, sau đó nhập `n` dòng họ tên. In ra tất cả.

**Bài 5.** So sánh `cin.ignore()`, `cin.ignore(1000, '\n')` và `cin.ignore(numeric_limits<streamsize>::max(), '\n')`. Cái nào an toàn nhất?

**Bài 6.** Nhập xen kẽ số và chuỗi nhiều lần, xử lý trôi lệnh đúng ở mọi vị trí.

**Bài 7.** Chương trình sau vẫn lỗi dù đã có `cin.ignore()`. Tìm nguyên nhân:

```cpp
string s1, s2;
getline(cin, s1);
cin.ignore();
getline(cin, s2);
```

**Bài 8.** Viết hàm `int nhapSo(const string& loiNhac)` đọc số an toàn, bắt nhập lại nếu người dùng nhập chữ.

**Bài 9.** Viết hàm `string nhapChuoi(const string& loiNhac)` đọc chuỗi an toàn sau khi đã đọc số.

**Bài 10.** Nhập một ký tự bằng `cin >> c` rồi nhập một dòng bằng `getline`. Xử lý trôi lệnh.

**Bài 11.** Tìm hiểu `cin.get()`, `cin.peek()`, `cin.putback()`. Viết ví dụ minh hoạ mỗi hàm.

**Bài 12.** Giải thích trạng thái lỗi của `cin` (`failbit`, `eofbit`, `badbit`). Viết chương trình minh hoạ và khôi phục bằng `cin.clear()`.

**Bài 13.** Viết menu chương trình nhập cả số lẫn chuỗi, không bao giờ bị trôi lệnh.

**Bài 14.** Thay vì `cin >>`, dùng `getline` + `stoi` để đọc số. So sánh với cách dùng `cin >>` kèm `ignore`.

**Bài 15.** Viết một "thư viện nhập liệu an toàn" gồm các hàm `nhapSoNguyen`, `nhapSoThuc`, `nhapChuoi`, `nhapKyTu`, `nhapLuaChon` — tất cả đều xử lý lỗi và trôi lệnh.
