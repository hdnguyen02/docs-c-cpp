# [C]. Kiểu Cấu Trúc Struct

Struct (cấu trúc) trong C là kiểu dữ liệu do bạn tự định nghĩa, cho phép gom nhiều giá trị có liên quan với nhau vào chung một biến. Nó đem lại nhiều sự tiện lợi khi bạn cần lưu trữ dữ liệu theo nhóm, ví dụ như : Tọa độ Oxy (x, y), thời gian bắt đầu và kết thúc của một công việc, đỉnh đầu và cuối của một cạnh trên đồ thị, thông tin một sinh viên (tên, tuổi, điểm)...

**NỘI DUNG :** 

- **Khai Báo Và Sử Dụng Struct**
- **Đặt Tên Ngắn Với typedef struct**
- **Toán Tử Với Struct**
- **Mảng Struct**
- **Struct 2 Trường Để Lưu Dữ Liệu Theo Cặp**
- **Video Tutorial**

---

**1. Khai Báo Và Sử Dụng Struct**

struct là từ khoá có sẵn của C, không cần thêm thư viện nào. Mỗi struct gồm nhiều **trường** (member), mỗi trường có kiểu và tên riêng.

Nhìn chung struct giúp lưu trữ dữ liệu theo nhóm và có những đặc điểm sau :

- Mỗi trường được đặt một cái tên có ý nghĩa, ví dụ `x`, `y` hay `ten`, `tuoi`
- Các trường có thể có kiểu khác nhau : int, double, char, mảng char, thậm chí là một struct khác
- Để truy cập vào từng trường ta sử dụng **toán tử dấu chấm** : `bien.tenTruong`
- Bạn có thể gán, copy cả một biến struct như kiểu dữ liệu bạn thường gặp

Cú pháp khai báo :

```
//Bước 1 : Định nghĩa kiểu struct (thường đặt ngoài hàm main)
struct TenStruct {
    kieu_1 truong_1;
    kieu_2 truong_2;
    ...
};                      // chú ý dấu chấm phẩy

//Bước 2 : Khai báo biến có kiểu struct vừa định nghĩa

//Cách 1 : Khai báo rồi gán từng trường sau
struct TenStruct bien;
bien.truong_1 = value1;

//Cách 2 : Khởi tạo theo thứ tự các trường
struct TenStruct bien = {value1, value2};

//Cách 3 : Khởi tạo chỉ định tên trường (designated initializer, từ C99)
struct TenStruct bien = {.truong_2 = value2, .truong_1 = value1};
```

Với cách 2, các giá trị được gán lần lượt theo đúng thứ tự khai báo trường. Trường nào không được ghi giá trị trong `{}` sẽ tự nhận giá trị 0. Cách 3 ghi rõ tên trường nên không phụ thuộc thứ tự, đọc code dễ hiểu hơn.

Ví dụ 1: Các kiểu khai báo struct

```c
#include <stdio.h>

struct Diem {
    int x;
    int y;
};

struct KyHieu {
    char c;
    int ma;
};

int main(){
    struct Diem a;
    a.x = 28;
    a.y = 100;
    printf("%d %d\n", a.x, a.y);

    struct KyHieu b = {'@', 28};
    printf("%c %d\n", b.c, b.ma);

    struct Diem c = {.y = 20, .x = 10};
    printf("%d %d\n", c.x, c.y);
    return 0;
}
```

Output :

```
28 100
@ 28
10 20
```

Ví dụ 2 : struct lồng nhau

Một trường của struct có thể là một struct khác. Khi đó ta dùng nhiều dấu chấm liên tiếp để đi vào từng tầng.

```c
#include <stdio.h>

struct Diem {
    int x, y;
};

struct DoanThang {
    struct Diem dau;
    struct Diem cuoi;
};

int main(){
    struct DoanThang d = {{10, 20}, {30, 40}};
    printf("%d %d\n", d.dau.x, d.dau.y);
    printf("%d %d\n", d.cuoi.x, d.cuoi.y);

    d.cuoi.x = 99;
    printf("%d %d\n", d.cuoi.x, d.cuoi.y);
    return 0;
}
```

Output :

```
10 20
30 40
99 40
```

---

**2. Đặt Tên Ngắn Với typedef struct**

Mỗi lần khai báo biến bạn đều phải viết đủ `struct Diem`, khá dài dòng. Từ khoá **typedef** giúp đặt một tên mới cho kiểu, sau đó chỉ cần viết `Diem` là đủ.

```
typedef struct {
    kieu_1 truong_1;
    kieu_2 truong_2;
} TenKieu;

TenKieu bien = {value1, value2};
```

Ví dụ :

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    int tuoi;
    double diem;
} SinhVien;

int main(){
    SinhVien sv = {"codelab", 20, 8.5};
    printf("%s %d %.2f\n", sv.ten, sv.tuoi, sv.diem);

    printf("Nhap tuoi moi : ");
    scanf("%d", &sv.tuoi);
    printf("Tuoi sau khi nhap : %d\n", sv.tuoi);
    return 0;
}
```

Ví dụ chạy :

```
codelab 20 8.50
Nhap tuoi moi : 21
Tuoi sau khi nhap : 21
```

Khi nhập bằng scanf, `&sv.tuoi` là địa chỉ của trường `tuoi` (toán tử dấu chấm được thực hiện trước `&`). Riêng trường `ten` là mảng char nên nhập bằng `scanf("%49s", sv.ten)` không có `&`, giống như chuỗi thông thường.

Bạn sẽ gặp lại typedef kỹ hơn ở bài [02-09 — define, typedef và enum](02-09-c-define-typedef-va-enum.md). Từ đây trở đi các ví dụ sẽ dùng cách viết `typedef struct` cho gọn.

---

**3. Toán Tử Với Struct**

Ví dụ 1 . Toán tử gán `=` sẽ copy **toàn bộ** các trường của struct này sang struct kia, kể cả trường là mảng char

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    int tuoi;
} Nguoi;

int main(){
    Nguoi p = {"codelab", 28};
    Nguoi p1 = p;
    printf("%s %d\n", p1.ten, p1.tuoi);

    p1.tuoi = 30;
    printf("%d %d\n", p.tuoi, p1.tuoi);
    return 0;
}
```

Output :

```
codelab 28
28 30
```

`p1` là một bản sao độc lập, sửa `p1` không ảnh hưởng tới `p`.

Ví dụ 2 : So sánh 2 struct

C **không cho phép** dùng các toán tử so sánh `==`, `!=`, `<`, `>` trực tiếp trên struct, viết `p1 == p2` sẽ bị lỗi biên dịch. Bạn phải tự so sánh từng trường. Cách hay dùng là so sánh trường thứ nhất trước, nếu bằng nhau mới so sánh trường thứ hai (so sánh theo thứ tự từ điển).

```c
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int x, y;
} Cap;

int main(){
    Cap p1 = {10, 20};
    Cap p2 = {10, 21};
    Cap p3 = {5, 35};

    bool bang = (p1.x == p2.x) && (p1.y == p2.y);
    bool nhoHon = (p1.x < p2.x) || (p1.x == p2.x && p1.y < p2.y);
    bool lonHon = (p1.x > p3.x) || (p1.x == p3.x && p1.y > p3.y);

    printf("p1 == p2 : %s\n", bang ? "true" : "false");
    printf("p1 != p2 : %s\n", !bang ? "true" : "false");
    printf("p1 <  p2 : %s\n", nhoHon ? "true" : "false");
    printf("p1 >  p3 : %s\n", lonHon ? "true" : "false");
    return 0;
}
```

Output :

```
p1 == p2 : false
p1 != p2 : true
p1 <  p2 : true
p1 >  p3 : true
```

Ví dụ 3 : Hoán đổi 2 struct bằng biến tạm

C không có sẵn hàm swap, nhưng nhờ phép gán copy được cả struct nên bạn hoán đổi bằng một biến tạm giống như với số nguyên.

```c
#include <stdio.h>

typedef struct {
    int x, y;
} Cap;

int main(){
    Cap p1 = {10, 20};
    Cap p2 = {30, 40};
    printf("Ban dau : \n");
    printf("p1 = {%d, %d}\n", p1.x, p1.y);
    printf("p2 = {%d, %d}\n", p2.x, p2.y);

    Cap tmp = p1;
    p1 = p2;
    p2 = tmp;

    printf("Sau khi swap : \n");
    printf("p1 = {%d, %d}\n", p1.x, p1.y);
    printf("p2 = {%d, %d}\n", p2.x, p2.y);
    return 0;
}
```

Output :

```
Ban dau : 
p1 = {10, 20}
p2 = {30, 40}
Sau khi swap : 
p1 = {30, 40}
p2 = {10, 20}
```

---

**4. Mảng Struct**

Bạn có thể khai báo mảng mà mỗi phần tử là một struct. Truy cập trường của phần tử thứ i bằng `a[i].tenTruong`. (Vòng lặp for sẽ được học kỹ ở chương 4, mảng ở chương 6.)

Ví dụ : Nhập thông tin n sinh viên và in ra sinh viên có điểm cao nhất

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    double diem;
} SinhVien;

int main(){
    int n;
    SinhVien ds[100];
    printf("Nhap so sinh vien : ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%49s %lf", ds[i].ten, &ds[i].diem);
    }

    SinhVien best = ds[0];
    for (int i = 1; i < n; i++) {
        if (ds[i].diem > best.diem) best = ds[i];
    }
    printf("Diem cao nhat : %s %.2f\n", best.ten, best.diem);
    return 0;
}
```

Ví dụ chạy :

```
Nhap so sinh vien : 3
An 7.5
Binh 9.25
Chi 8
Diem cao nhat : Binh 9.25
```

Ưu điểm so với dùng 2 mảng rời `ten[]` và `diem[]` : tên và điểm của một sinh viên luôn đi cùng nhau, khi gán `best = ds[i]` là copy cả hai.

---

**5. Struct 2 Trường Để Lưu Dữ Liệu Theo Cặp**

Rất nhiều bài toán cần lưu dữ liệu **theo cặp** : toạ độ (x, y), đoạn thời gian (bắt đầu, kết thúc), phân số (tử, mẫu)... C không có kiểu "cặp" dựng sẵn, cách chuẩn là định nghĩa một struct 2 trường. Đặt tên trường có ý nghĩa còn giúp code dễ đọc hơn.

Một ứng dụng rất quan trọng : một hàm trong C chỉ `return` được **một** giá trị, nhưng giá trị đó có thể là một struct. Vì vậy muốn hàm trả về 2 giá trị, bạn gói chúng vào struct 2 trường (hàm sẽ được học ở chương 5).

```c
#include <stdio.h>

typedef struct {
    int thuong;
    int du;
} KetQuaChia;

KetQuaChia chia(int a, int b){
    KetQuaChia kq = {a / b, a % b};
    return kq;
}

int main(){
    KetQuaChia k = chia(17, 5);
    printf("17 / 5 = %d du %d\n", k.thuong, k.du);
    return 0;
}
```

Output :

```
17 / 5 = 3 du 2
```

---

**Video hướng dẫn Struct trong C :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/02-06-c-kieu-cau-truc-struct.md](solutions/02-06-c-kieu-cau-truc-struct.md)

**Bài 1.** Định nghĩa `struct Diem { int x; int y; };` rồi khai báo điểm A(3, 7) bằng cả 3 cách khai báo đã học (gán từng trường, `{}` theo thứ tự, `{}` chỉ định tên trường), in ra giá trị mỗi lần.

**Bài 2.** Nhập vào toạ độ 2 điểm A, B (mỗi điểm là một struct gồm 2 trường `double x, y`), tính và in ra khoảng cách giữa chúng.

**Bài 3.** Định nghĩa struct `Nguoi` gồm tên (mảng `char`, viết liền) và tuổi. Nhập từ bàn phím rồi in ra.

**Bài 4.** Viết hàm nhận 2 số nguyên, trả về một struct chứa (tổng, hiệu) của chúng. Trong `main` nhập 2 số rồi in kết quả.

**Bài 5.** Định nghĩa struct `MonHoc` gồm tên môn học, số tín chỉ, điểm. Khởi tạo một môn học và in ra đủ 3 thông tin với điểm lấy 1 chữ số thập phân.

**Bài 6.** Định nghĩa struct `HinhChuNhat` gồm 2 struct `Diem` là toạ độ 2 đỉnh đối diện. Nhập vào rồi tính chu vi và diện tích.

**Bài 7.** Cho `p1 = {5, 10}` và `p2 = {5, 3}` kiểu struct 2 trường `x, y`. Viết hàm `soSanh(p1, p2)` trả về -1, 0, 1 theo thứ tự từ điển (so `x` trước, bằng nhau mới so `y`). Dự đoán kết quả rồi chạy kiểm chứng. Vì sao không viết được `p1 < p2`?

**Bài 8.** Viết chương trình hoán đổi 2 struct `SinhVien` (tên, điểm) bằng biến tạm. In ra trước và sau khi hoán đổi.

**Bài 9.** Khai báo mảng 5 phần tử kiểu struct (tên, điểm) lưu thông tin 5 học sinh. In ra học sinh có điểm cao nhất.

**Bài 10.** Với mảng ở bài 9, sắp xếp mảng theo điểm tăng dần (tự cài thuật toán sắp xếp chọn hoặc nổi bọt, hoán đổi cả struct) và in kết quả. Quan sát: khi 2 học sinh cùng điểm thì thứ tự ra sao?

**Bài 11.** Định nghĩa struct `PhanSo` (tử, mẫu). Nhập một phân số, rút gọn rồi in ra.

**Bài 12.** Định nghĩa struct `CongViec` gồm thời gian bắt đầu và kết thúc. Cho 3 công việc, kiểm tra xem có 2 công việc nào bị chồng lấn thời gian không.

**Bài 13.** In ra `sizeof` của struct `{char c; int x;}` và so sánh với `sizeof(char) + sizeof(int)`. Kết quả có bằng nhau không? Tìm hiểu khái niệm **padding** (căn lề bộ nhớ) để giải thích.

**Bài 14.** Viết chương trình nhập toạ độ 5 điểm vào mảng struct (`double x, y`), tìm điểm gần gốc toạ độ O(0,0) nhất.

**Bài 15.** So sánh dùng struct với việc dùng các biến/mảng rời rạc. Nêu 3 tình huống mà struct tiện hơn hẳn và 1 tình huống mà dùng struct là không cần thiết.
