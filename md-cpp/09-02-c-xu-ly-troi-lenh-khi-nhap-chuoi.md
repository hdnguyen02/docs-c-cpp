# [C]. Xử Lý Trôi Lệnh Khi Nhập Chuỗi

Khi nhập xâu ký tự từ bàn phím trong C bằng hàm fgets() ngay sau một lệnh scanf() đôi khi bạn sẽ thấy lệnh này bị trôi qua mà không thể nhập được nội dung cho nó. Trong bài học này mình sẽ giải thích lý do xảy ra trôi lệnh và cách xử lý.

**NỘI DUNG :**

- **Nguyên Nhân Và Cách Khắc Phục**
- **Video Tutorial** 

---

**Nguyên Nhân Và Cách Khắc Phục**

Bạn thử chạy mã nguồn sau và sẽ thấy sau khi nhập số cho n và ấn enter thì chưa kịp nhập nội dung cho xâu s đã bị trôi qua câu lệnh đó

Nội dung của xâu s là rỗng (chỉ chứa đúng ký tự xuống dòng `'\n'`)

```c
#include <stdio.h>

int main(void) {
    int n;
    printf("Nhap n : ");
    scanf("%d", &n);
    char s[100];
    printf("Nhap xau s : ");
    fgets(s, sizeof(s), stdin);
    printf("So n da nhap : %d\n", n);
    printf("Xau s : %s\n", s);
    return 0;
}
```

**Nguyên nhân :** 

Hàm fgets(s, size, stdin) khi bạn nhập xâu s sẽ đọc cho tới khi nó gặp được ký tự xuống dòng (enter) hoặc đã đọc đủ `size - 1` ký tự, những ký tự nó đọc được từ luồng vào `stdin` (kể cả ký tự enter) sẽ được lưu vào mảng s, sau đó fgets tự thêm ký tự kết thúc `'\0'`.

Khi bạn nhập scanf("%d", &n) sau đó ấn enter, thì giá trị mà bạn vừa nhập sẽ được gán cho n tuy nhiên ký tự enter ở cuối bạn nhập sẽ nằm lại trong luồng vào `stdin`, khi hàm fgets() đọc từ `stdin` thì sẽ gặp ký tự enter này do scanf ở câu lệnh trên để lại.

Do fgets() sẽ dừng nhập khi gặp enter nên nó sẽ dừng ngay tại lúc đó mà chưa hề nhập được ký tự nào khác, và dẫn đến xâu s của bạn chỉ chứa `"\n"`, tức là một dòng rỗng.

Vậy nếu trước hàm fgets() mà trong `stdin` có thừa kí tự enter (thông thường do scanf ở câu lệnh trước đó để lại) thì sẽ xảy ra trôi lệnh.

Lưu ý rằng nếu bạn dùng câu lệnh fgets() sau một câu lệnh fgets() thì bạn sẽ không bị trôi lệnh vì hàm fgets() đã lấy luôn ký tự enter ở cuối dòng ra khỏi luồng vào chứ không để lại như scanf (với điều kiện dòng đó không dài hơn kích thước mảng).

**Cách khắc phục :** 

Khi bạn biết nguyên nhân fgets() bị trôi lệnh là do đọc phải ký tự enter thừa trong luồng vào từ bàn phím nên để xử lý việc này bạn chỉ cần loại bỏ được ký tự enter này trước khi dùng fgets().

Bạn có thể dùng hàm **getchar()** để đọc bỏ đi 1 ký tự trong `stdin`, khi đó ký tự enter sẽ bị loại bỏ và hàm fgets() sẽ đợi bạn nhập nội dung sau đó ấn enter.

Cách an toàn hơn là dùng vòng lặp đọc bỏ **toàn bộ** phần còn lại của dòng (phòng khi người dùng gõ thừa dấu cách hoặc ký tự sau số):

```c
int c;
while ((c = getchar()) != '\n' && c != EOF);
```

Ngoài ra vì fgets() giữ lại ký tự `'\n'` trong xâu, bạn thường cần xoá nó đi sau khi đọc bằng hàm `strcspn()` của thư viện `<string.h>`:

```c
s[strcspn(s, "\n")] = '\0';   // thay '\n' dau tien (neu co) bang '\0'
```

Bây giờ bạn có thể chạy lại mã nguồn này và kiểm tra

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    int n;
    printf("Nhap n : ");
    scanf("%d", &n);
    char s[100];
    printf("Nhap xau s : ");
    getchar();                      // loai bo ky tu enter con sot lai
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = '\0';     // xoa '\n' o cuoi xau
    printf("So n da nhap : %d\n", n);
    printf("Xau s : %s\n", s);
    return 0;
}
```

Một cách khác là dùng scanf với định dạng `" %[^\n]"`: dấu cách ở đầu định dạng sẽ bỏ qua mọi khoảng trắng (kể cả enter thừa), còn `%[^\n]` đọc mọi ký tự cho tới khi gặp enter. Nên giới hạn độ dài để tránh tràn mảng, ví dụ với mảng 100 phần tử:

```c
scanf(" %99[^\n]", s);   // bo qua khoang trang dau, doc toi da 99 ky tu den het dong
```

Cách này tiện nhưng sẽ bỏ qua cả những dấu cách ở đầu dòng và không đọc được dòng rỗng.

**Lưu ý :** Tuyệt đối **không dùng hàm gets()**. Hàm này không giới hạn số ký tự đọc vào nên rất dễ gây tràn mảng, và đã bị **loại bỏ khỏi chuẩn C11**. Hãy dùng fgets() thay thế.

---

**Video String :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi.md](solutions/09-02-c-xu-ly-troi-lenh-khi-nhap-chuoi.md)

**Bài 1.** Chạy chương trình sau, mô tả hiện tượng và giải thích:

```c
int n; char s[100];
scanf("%d", &n);
fgets(s, sizeof(s), stdin);
printf("n = %d, s = [%s]", n, s);
```

**Bài 2.** Sửa chương trình bài 1 bằng `getchar()` và xoá ký tự `'\n'` ở cuối xâu.

**Bài 3.** Nhập tuổi (số) rồi nhập họ tên (có dấu cách) — xử lý đúng trôi lệnh.

**Bài 4.** Nhập `n`, sau đó nhập `n` dòng họ tên (lưu vào mảng 2 chiều `char ds[100][51]`). In ra tất cả.

**Bài 5.** So sánh `getchar()`, vòng lặp `while ((c = getchar()) != '\n' && c != EOF);` và `scanf("%*[^\n]"); getchar();`. Cái nào an toàn nhất?

**Bài 6.** Nhập xen kẽ số và chuỗi nhiều lần, xử lý trôi lệnh đúng ở mọi vị trí.

**Bài 7.** Chương trình sau vẫn lỗi dù đã có `getchar()`. Tìm nguyên nhân:

```c
char s1[100], s2[100];
fgets(s1, sizeof(s1), stdin);
getchar();
fgets(s2, sizeof(s2), stdin);
```

**Bài 8.** Viết hàm `int nhapSo(const char *loiNhac)` đọc số an toàn, bắt nhập lại nếu người dùng nhập chữ.

**Bài 9.** Viết hàm `void nhapChuoi(const char *loiNhac, char *s, int size)` đọc chuỗi an toàn sau khi đã đọc số.

**Bài 10.** Nhập một ký tự bằng `scanf(" %c", &c)` rồi nhập một dòng bằng `fgets`. Xử lý trôi lệnh.

**Bài 11.** Tìm hiểu `getchar()`, `ungetc()` và cách "xem trước" ký tự kế tiếp bằng `getchar()` + `ungetc()`. Viết ví dụ minh hoạ mỗi cách.

**Bài 12.** Giải thích giá trị trả về của `scanf` (số biến đọc được, `0`, `EOF`) cùng các hàm `feof()`, `ferror()`, `clearerr()`. Viết chương trình minh hoạ việc nhập sai và khôi phục.

**Bài 13.** Viết menu chương trình nhập cả số lẫn chuỗi, không bao giờ bị trôi lệnh.

**Bài 14.** Thay vì `scanf("%d")`, dùng `fgets` + `strtol` để đọc số. So sánh với cách dùng `scanf` kèm xoá bộ đệm.

**Bài 15.** Viết một "thư viện nhập liệu an toàn" gồm các hàm `nhapSoNguyen`, `nhapSoThuc`, `nhapChuoi`, `nhapKyTu`, `nhapLuaChon` — tất cả đều xử lý lỗi và trôi lệnh.
