# Lời giải — [C]. Kiểu Cấu Trúc Struct

[← Quay lại bài học](../02-06-c-kieu-cau-truc-struct.md)

---

### Bài 1.

```c
#include <stdio.h>

struct Diem {
    int x;
    int y;
};

int main() {
    // Cach 1: khai bao roi gan tung truong
    struct Diem A1;
    A1.x = 3;
    A1.y = 7;
    printf("Cach 1: %d %d\n", A1.x, A1.y);

    // Cach 2: khoi tao theo thu tu cac truong
    struct Diem A2 = {3, 7};
    printf("Cach 2: %d %d\n", A2.x, A2.y);

    // Cach 3: khoi tao chi dinh ten truong (C99)
    struct Diem A3 = {.y = 7, .x = 3};
    printf("Cach 3: %d %d\n", A3.x, A3.y);

    return 0;
}
```

Output: cả 3 dòng đều in `3 7`.

**Nên dùng cách nào:** cách 2 (`= {3, 7}`) ngắn gọn khi struct ít trường và thứ tự rõ ràng. Cách 3 an toàn hơn khi struct nhiều trường: đọc là biết giá trị nào vào trường nào, và không bị sai nếu sau này ai đó đổi thứ tự khai báo trường.

⚠️ `{}` chỉ dùng được **lúc khai báo**. Viết `A1 = {3, 7};` sau khi đã khai báo là lỗi. Muốn gán lại cả struct, dùng *compound literal* (C99): `A1 = (struct Diem){3, 7};`.

### Bài 2.

```c
#include <stdio.h>
#include <math.h>

typedef struct {
    double x, y;
} Diem;

int main() {
    Diem A, B;

    printf("Nhap toa do diem A (x y): ");
    scanf("%lf%lf", &A.x, &A.y);
    printf("Nhap toa do diem B (x y): ");
    scanf("%lf%lf", &B.x, &B.y);

    double dx = B.x - A.x;
    double dy = B.y - A.y;
    double kc = sqrt(dx * dx + dy * dy);

    printf("Khoang cach AB = %.3f\n", kc);
    return 0;
}
```

Biên dịch: `gcc -std=c11 -Wall bai2.c -o bai2 -lm` (cần `-lm` vì dùng `sqrt` của `math.h`).

Ví dụ:

```
Nhap toa do diem A (x y): 0 0
Nhap toa do diem B (x y): 3 4
Khoang cach AB = 5.000
```

### Bài 3.

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    int tuoi;
} Nguoi;

int main() {
    Nguoi nguoi;

    printf("Nhap ten (viet lien): ");
    scanf("%49s", nguoi.ten);        // mang char -> khong co &
    printf("Nhap tuoi: ");
    scanf("%d", &nguoi.tuoi);        // int -> co &

    printf("Ho ten: %s, Tuoi: %d\n", nguoi.ten, nguoi.tuoi);
    return 0;
}
```

⚠️ Không gán chuỗi cho trường mảng bằng dấu `=`: `nguoi.ten = "An";` là **lỗi biên dịch** (mảng không gán được). Dùng khởi tạo lúc khai báo `Nguoi n = {"An", 20};` hoặc hàm `strcpy(nguoi.ten, "An");` của `string.h`.

### Bài 4.

```c
#include <stdio.h>

typedef struct {
    int tong;
    int hieu;
} TongHieu;

// Ham tra ve mot struct chua (tong, hieu)
TongHieu tinhTongHieu(int a, int b) {
    TongHieu kq = {a + b, a - b};
    return kq;
}

int main() {
    int a, b;
    printf("Nhap a va b: ");
    scanf("%d%d", &a, &b);

    TongHieu kq = tinhTongHieu(a, b);
    printf("Tong = %d\n", kq.tong);
    printf("Hieu = %d\n", kq.hieu);
    return 0;
}
```

**Đây là ứng dụng rất quan trọng của struct:** một hàm trong C chỉ trả về được **một** giá trị. Muốn trả về 2 giá trị, gói chúng vào struct là cách gọn và rõ nghĩa (cách còn lại là truyền con trỏ, sẽ học ở chương 5 và 7). Tên trường `kq.tong`, `kq.hieu` tự giải thích ý nghĩa.

### Bài 5.

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    int soTinChi;
    double diem;
} MonHoc;

int main() {
    MonHoc mon = {"LapTrinhC", 3, 8.5};

    printf("Mon hoc  : %s\n", mon.ten);
    printf("Tin chi  : %d\n", mon.soTinChi);
    printf("Diem     : %.1f\n", mon.diem);
    return 0;
}
```

Output:

```
Mon hoc  : LapTrinhC
Tin chi  : 3
Diem     : 8.5
```

**Nhận xét:** struct cho phép gom 3 trường với 3 kiểu khác nhau (mảng `char`, `int`, `double`) vào một biến, và mỗi trường có tên riêng nên đọc code không bị nhầm.

### Bài 6.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x, y;
} Diem;

typedef struct {
    Diem a;     // dinh thu nhat
    Diem b;     // dinh doi dien
} HinhChuNhat;

int main() {
    HinhChuNhat h;
    printf("Nhap dinh thu nhat (x y): ");
    scanf("%d%d", &h.a.x, &h.a.y);
    printf("Nhap dinh doi dien (x y): ");
    scanf("%d%d", &h.b.x, &h.b.y);

    int dai  = abs(h.b.x - h.a.x);
    int rong = abs(h.b.y - h.a.y);

    printf("Chu vi    = %d\n", 2 * (dai + rong));
    printf("Dien tich = %d\n", dai * rong);
    return 0;
}
```

Ví dụ:

```
Nhap dinh thu nhat (x y): 1 1
Nhap dinh doi dien (x y): 4 5
Chu vi    = 14
Dien tich = 12
```

**Dùng `abs`** (trong `stdlib.h`) để công thức vẫn đúng dù người dùng nhập đỉnh nào trước.

### Bài 7.

```c
#include <stdio.h>

typedef struct {
    int x, y;
} Cap;

// Tra ve -1 neu p < q, 0 neu bang nhau, 1 neu p > q (thu tu tu dien)
int soSanh(Cap p, Cap q) {
    if (p.x != q.x) return (p.x < q.x) ? -1 : 1;   // x khac nhau -> ket luan luon
    if (p.y != q.y) return (p.y < q.y) ? -1 : 1;   // x bang nhau -> moi xet y
    return 0;
}

int main() {
    Cap p1 = {5, 10};
    Cap p2 = {5, 3};

    int kq = soSanh(p1, p2);
    printf("soSanh(p1, p2) = %d\n", kq);
    printf("p1 <  p2 : %d\n", kq < 0);
    printf("p1 >  p2 : %d\n", kq > 0);
    printf("p1 == p2 : %d\n", kq == 0);
    return 0;
}
```

Output:

```
soSanh(p1, p2) = 1
p1 <  p2 : 0
p1 >  p2 : 1
p1 == p2 : 0
```

**Quy tắc so sánh từ điển (lexicographical):**

1. So sánh trường thứ nhất `x`.
2. Nếu `x` **khác nhau** → kết luận luôn, không xét `y`.
3. Nếu `x` **bằng nhau** → mới so sánh `y`.

Ở đây `x` bằng nhau (5 = 5), xét `y`: 10 > 3 nên `p1 > p2`.

**Vì sao không viết được `p1 < p2`?** Trong C, các toán tử `<`, `>`, `==`, `!=` chỉ áp dụng cho kiểu số (và con trỏ). C không biết struct của bạn nên so theo trường nào, thứ tự nào, nên trình biên dịch báo lỗi kiểu `invalid operands to binary <`. Bạn luôn phải tự viết hàm so sánh như trên.

💡 Hàm so sánh trả về số âm / 0 / số dương chính là "khuôn" mà hàm sắp xếp `qsort` của thư viện C yêu cầu — xem bài [10-03 — Xây dựng hàm so sánh cho qsort](../10-03-c-xay-dung-ham-so-sanh-cho-qsort.md).

### Bài 8.

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    double diem;
} SinhVien;

int main() {
    SinhVien a = {"An", 7.5};
    SinhVien b = {"Binh", 9.0};

    printf("Truoc: a = {%s, %.1f}, b = {%s, %.1f}\n", a.ten, a.diem, b.ten, b.diem);

    SinhVien tmp = a;   // copy CA struct, ke ca mang ten
    a = b;
    b = tmp;

    printf("Sau  : a = {%s, %.1f}, b = {%s, %.1f}\n", a.ten, a.diem, b.ten, b.diem);
    return 0;
}
```

Output:

```
Truoc: a = {An, 7.5}, b = {Binh, 9.0}
Sau  : a = {Binh, 9.0}, b = {An, 7.5}
```

**Điểm đáng chú ý:** mảng `char ten[50]` không gán trực tiếp được, nhưng khi nó nằm **bên trong struct** thì phép gán struct copy luôn cả mảng. Đó là lý do hoán đổi struct bằng biến tạm hoạt động trọn vẹn.

*(Muốn viết thành hàm `swap` dùng lại được, cần truyền con trỏ — xem chương 5 và chương 7.)*

### Bài 9.

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    int diem;
} HocSinh;

int main() {
    HocSinh hs[5] = {
        {"An", 8}, {"Binh", 6}, {"Chi", 9}, {"Dung", 7}, {"Em", 9}
    };

    int viTri = 0;
    for (int i = 1; i < 5; i++) {
        if (hs[i].diem > hs[viTri].diem) viTri = i;
    }

    printf("Hoc sinh diem cao nhat: %s (%d diem)\n", hs[viTri].ten, hs[viTri].diem);
    return 0;
}
```

Output:

```
Hoc sinh diem cao nhat: Chi (9 diem)
```

**Lưu ý:** dùng `>` (không phải `>=`) nên khi có nhiều học sinh cùng điểm cao nhất (Chi và Em), chương trình giữ người **xuất hiện đầu tiên**. Đổi thành `>=` sẽ lấy người cuối cùng.

### Bài 10.

```c
#include <stdio.h>

typedef struct {
    char ten[50];
    int diem;
} HocSinh;

int main() {
    HocSinh hs[5] = {
        {"An", 8}, {"Binh", 6}, {"Chi", 8}, {"Dung", 7}, {"Em", 6}
    };
    int n = 5;

    // Sap xep chon (selection sort) theo diem tang dan
    for (int i = 0; i < n - 1; i++) {
        int m = i;
        for (int j = i + 1; j < n; j++) {
            if (hs[j].diem < hs[m].diem) m = j;
        }
        HocSinh tmp = hs[i];     // hoan doi CA struct: ten di cung diem
        hs[i] = hs[m];
        hs[m] = tmp;
    }

    for (int i = 0; i < n; i++) {
        printf("%-5s %d\n", hs[i].ten, hs[i].diem);
    }
    return 0;
}
```

Output:

```
Binh  6
Em    6
Dung  7
Chi   8
An    8
```

**Khi 2 học sinh cùng điểm thì thứ tự ra sao?** Ban đầu An đứng trước Chi (cùng 8 điểm), nhưng sau khi sắp xếp Chi lại đứng trước An. Sắp xếp chọn **không ổn định** (*not stable*): thứ tự ban đầu của các phần tử bằng nhau có thể bị đảo, do phép hoán đổi "nhảy xa" (ở bước thứ hai, An bị đổi chỗ với Em và bị đẩy xuống cuối mảng, ra sau Chi). Hàm `qsort` của thư viện C cũng **không đảm bảo** ổn định.

**Nếu cần giữ đúng thứ tự ban đầu khi bằng điểm:**
- Thêm tiêu chí phụ khi so sánh (ví dụ so theo tên, hoặc theo chỉ số ban đầu), hoặc
- Dùng thuật toán sắp xếp ổn định như sắp xếp nổi bọt, sắp xếp chèn, merge sort.

Chi tiết xem bài [10-03 — Xây dựng hàm so sánh cho qsort](../10-03-c-xay-dung-ham-so-sanh-cho-qsort.md) và [10-04 — Sắp xếp ổn định và merge sort](../10-04-c-sap-xep-on-dinh-va-merge-sort.md).

### Bài 11.

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int tu, mau;
} PhanSo;

int gcd(int a, int b) {           // uoc chung lon nhat (thuat toan Euclid)
    a = abs(a); b = abs(b);
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    PhanSo ps;
    printf("Nhap tu va mau: ");
    scanf("%d%d", &ps.tu, &ps.mau);

    if (ps.mau == 0) {
        printf("Mau so phai khac 0!\n");
        return 0;
    }

    int g = gcd(ps.tu, ps.mau);
    if (g != 0) {
        ps.tu  /= g;
        ps.mau /= g;
    }

    // Dua dau am len tu so: 3/-4 -> -3/4
    if (ps.mau < 0) {
        ps.tu  = -ps.tu;
        ps.mau = -ps.mau;
    }

    printf("Phan so rut gon: %d/%d\n", ps.tu, ps.mau);
    return 0;
}
```

Ví dụ:

```
Nhap tu va mau: 12 -18
Phan so rut gon: -2/3
```

C không có sẵn hàm tính UCLN trong thư viện chuẩn, ta tự viết theo thuật toán Euclid (học kỹ ở bài [05-05 — Lý thuyết số và toán học](../05-05-c-ly-thuyet-so-va-toan-hoc.md)).

### Bài 12.

```c
#include <stdio.h>
#include <stdbool.h>

typedef struct {
    int batDau, ketThuc;
} CongViec;

bool chongLan(CongViec p, CongViec q) {
    // KHONG chong lan khi mot viec ket thuc truoc (hoac dung luc) viec kia bat dau
    return !(p.ketThuc <= q.batDau || q.ketThuc <= p.batDau);
}

int main() {
    CongViec cv[3] = { {1, 4}, {5, 7}, {3, 6} };
    bool coChongLan = false;

    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            if (chongLan(cv[i], cv[j])) {
                printf("Cong viec %d [%d, %d] chong lan cong viec %d [%d, %d]\n",
                       i + 1, cv[i].batDau, cv[i].ketThuc,
                       j + 1, cv[j].batDau, cv[j].ketThuc);
                coChongLan = true;
            }
        }
    }
    if (!coChongLan) printf("Khong co cong viec nao chong lan\n");
    return 0;
}
```

Output:

```
Cong viec 1 [1, 4] chong lan cong viec 3 [3, 6]
Cong viec 2 [5, 7] chong lan cong viec 3 [3, 6]
```

**Mẹo nhớ điều kiện chồng lấn:** dễ hơn là xét điều kiện **không** chồng lấn — khi việc này kết thúc trước khi việc kia bắt đầu (`p.ketThuc <= q.batDau` hoặc `q.ketThuc <= p.batDau`) — rồi phủ định.

### Bài 13.

```c
#include <stdio.h>

typedef struct {
    char c;
    int x;
} VD;

int main() {
    printf("sizeof(char) + sizeof(int) = %zu\n", sizeof(char) + sizeof(int));
    printf("sizeof(VD)                 = %zu\n", sizeof(VD));
    return 0;
}
```

Output thường gặp (gcc trên máy 32/64-bit phổ biến):

```
sizeof(char) + sizeof(int) = 5
sizeof(VD)                 = 8
```

**Giải thích — padding (căn lề bộ nhớ):** CPU đọc dữ liệu nhanh nhất khi một `int` 4 byte nằm ở địa chỉ chia hết cho 4. Vì vậy trình biên dịch chèn thêm **3 byte trống** sau `c` để `x` bắt đầu ở vị trí chia hết cho 4:

```
| c | _ | _ | _ | x x x x |
  0   1   2   3   4 ... 7      -> tong 8 byte
```

Hệ quả thực tế:
- `sizeof` của struct **có thể lớn hơn** tổng `sizeof` các trường. Luôn dùng `sizeof(TenStruct)`, đừng tự cộng tay.
- Thứ tự khai báo trường ảnh hưởng tới kích thước: xếp các trường lớn trước, nhỏ sau thường giúp giảm padding.
- Kích thước cụ thể phụ thuộc trình biên dịch và kiến trúc máy; chuẩn C chỉ đảm bảo không có padding **trước** trường đầu tiên.

### Bài 14.

```c
#include <stdio.h>

typedef struct {
    double x, y;
} Diem;

int main() {
    Diem d[5];
    for (int i = 0; i < 5; i++) {
        printf("Nhap diem %d (x y): ", i + 1);
        scanf("%lf%lf", &d[i].x, &d[i].y);
    }

    int best = 0;
    double bestKc2 = d[0].x * d[0].x + d[0].y * d[0].y;   // binh phuong khoang cach
    for (int i = 1; i < 5; i++) {
        double kc2 = d[i].x * d[i].x + d[i].y * d[i].y;
        if (kc2 < bestKc2) {
            bestKc2 = kc2;
            best = i;
        }
    }

    printf("Diem gan O nhat: (%.2f, %.2f)\n", d[best].x, d[best].y);
    return 0;
}
```

Ví dụ:

```
Nhap diem 1 (x y): 3 4
Nhap diem 2 (x y): -1 2
Nhap diem 3 (x y): 5 0
Nhap diem 4 (x y): 1 1
Nhap diem 5 (x y): 2 -2
Diem gan O nhat: (1.00, 1.00)
```

**Mẹo tối ưu:** khi chỉ cần *so sánh* khoảng cách chứ không cần giá trị thật, hãy so sánh **bình phương khoảng cách**. Vì `sqrt` là hàm đồng biến, thứ tự không đổi — mà tránh được phép căn tốn thời gian, tránh sai số làm tròn, và không cần link thêm `-lm`.

### Bài 15.

**3 tình huống struct tiện hơn hẳn biến/mảng rời:**

1. **Hàm cần trả về nhiều giá trị.** C chỉ cho `return` một thứ. Không có struct thì phải truyền con trỏ ra ngoài (khó đọc với người mới):

```c
// Voi struct: goi ham xong la co du ket qua, ten truong ro nghia
typedef struct { int thuong, du; } KetQuaChia;
KetQuaChia chia(int a, int b) { KetQuaChia k = {a / b, a % b}; return k; }
```

2. **Lưu danh sách bản ghi và sắp xếp.** Với 2 mảng rời (`ten[]` và `diem[]`), khi hoán đổi trong mảng điểm mà quên hoán đổi mảng tên thì dữ liệu bị **lệch** (điểm của người này gắn sang người khác). Với mảng struct `HocSinh hs[]`, một phép gán là cả bản ghi di chuyển cùng nhau.

3. **Dữ liệu có nhiều thuộc tính gắn bó.** Một sinh viên có tên, tuổi, điểm, lớp... Gom vào struct `SinhVien` thì truyền vào hàm chỉ cần 1 tham số thay vì 4, thêm thuộc tính mới cũng không phải sửa mọi lời gọi hàm.

**1 tình huống dùng struct là không cần thiết:**

Khi các giá trị **không có quan hệ tự nhiên** với nhau, hoặc chỉ dùng tạm trong vài dòng:

```c
// Khong can: dem va tong chi la 2 bien phu trong mot vong lap
typedef struct { int dem; long long tong; } TamThoi;   // thua

int dem = 0;          // du ro rang
long long tong = 0;
```

**Quy tắc thực tế:** dùng struct khi các giá trị **mô tả cùng một đối tượng** (toạ độ x-y, phân số tử-mẫu, bắt đầu-kết thúc, thông tin sinh viên). Đặt tên struct và tên trường có ý nghĩa — đó là lợi thế lớn nhất so với việc gọi chung chung "phần tử thứ nhất / thứ hai".
