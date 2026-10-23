# [C]. Chèn Và Xóa Phần Tử

Trong bài viết này mình sẽ hướng dẫn các bạn cách chèn và xóa một phần tử trong mảng 1 chiều

**NỘI DUNG :**

- **Thao Tác Xóa**
- **Thao Tác Chèn**
- **Video Tutorial**

---

**1. Thao Tác Xóa**

Trong mảng 1 chiều thì kích thước mảng đã được khai báo cố định và không thể thay đổi, do đó khi xóa phần tử trong mảng thì thực chất mảng vẫn có kích thước như ban đầu.

Ban đầu mảng có N phần tử thì ở đây việc xóa phần tử trong mảng chỉ đơn giản là ta thay vì quản lý N phần tử trong mảng ban đầu thì ta quản lý N - 1 phần tử.

Bài toán : Cho mảng A[] gồm N phần tử, hãy xóa phần tử ở chỉ số K trong mảng

Ví dụ A[] = {2, 3, 1, 5, 8, 9, 4} và K = 3 thì mảng sau khi xóa sẽ là {2, 3, 1, 8, 9, 4}

**Thuật toán** : Dịch các phần tử từ chỉ số K + 1 tới chỉ số N - 1 sang trái, việc dịch sẽ được thực hiện từ trái qua phải. Sau đó giảm N đi 1 đơn vị vì bạn vừa xóa 1 phần tử trong mảng

**Code :** 

```c
#include <stdio.h>

int main(){
    int n = 7, k = 3;
    int a[7] = {2, 3, 1, 5, 8, 9, 4};
    for(int i = k; i < n - 1; i++){
        a[i] = a[i + 1];
    }
    --n;
    printf("Mang sau khi xoa : ");
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    return 0;
}
```

Output :

```
Mang sau khi xoa : 2 3 1 8 9 4
```

---

**2.Thao Tác Chèn**

Khi chèn phần tử vào trong mảng thì mảng của bạn cần thêm 1 ô nhớ để lưu phần tử được thêm, vì thế nếu khi khai báo mảng ban đầu bạn cần khai báo thêm 1 vài phần tử.

Bài toán : Cho mảng A[] gồm N phần tử, hãy chèn phần tử có giá trị X và chỉ số K trong mảng

Ví dụ A[] = {2, 3, 1, 5, 8, 9, 4} và X = 100, K = 3 thì mảng sau khi chèn sẽ là {2, 3, 1, 100, 5, 8, 9, 4}

**Thuật toán :**

1. Dịch các phần tử từ chỉ số K tới chỉ số N - 1 trong mảng sang phải 1 phần tử, việc dịch sẽ được thực hiện từ phải sang trái.
2. Gán A[K] = X
3. Tăng N lên 1 đơn vị

**Code :** 

```c
#include <stdio.h>

int main(){
    int n = 7, k = 3, x = 100;
    int a[10] = {2, 3, 1, 5, 8, 9, 4};
    for(int i = n - 1; i >= k; i--){
        a[i + 1] = a[i];
    }
    a[k] = x;
    ++n;
    printf("Mang sau khi chen : ");
    for(int i = 0; i < n; i++){
        printf("%d ", a[i]);
    }
    return 0;
}
```

Output :

```
Mang sau khi chen : 2 3 1 100 5 8 9 4
```

---

**Video Bài Tập Mảng 1 Chiều**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/06-05-c-chen-va-xoa-phan-tu.md](solutions/06-05-c-chen-va-xoa-phan-tu.md)

**Bài 1.** Viết hàm chèn giá trị `x` vào vị trí `k` trong mảng `n` phần tử.

**Bài 2.** Viết hàm xoá phần tử tại vị trí `k` khỏi mảng.

**Bài 3.** Chèn `x` vào đầu mảng và vào cuối mảng.

**Bài 4.** Xoá tất cả phần tử có giá trị bằng `x`.

**Bài 5.** Xoá tất cả phần tử âm khỏi mảng.

**Bài 6.** Xoá tất cả phần tử trùng lặp, chỉ giữ lần xuất hiện đầu tiên.

**Bài 7.** Cho mảng đã sắp xếp tăng dần, chèn `x` vào đúng vị trí để mảng vẫn sắp xếp.

**Bài 8.** Chèn giá trị 0 vào sau mỗi phần tử chẵn của mảng.

**Bài 9.** Xoá `k` phần tử liên tiếp bắt đầu từ vị trí `p`.

**Bài 10.** Chương trình sau có lỗi gì? Sửa lại:

```c
// Xoa phan tu tai vi tri k
for (int i = k; i < n; i++) a[i] = a[i + 1];
n--;
```

**Bài 11.** Chương trình sau xoá số âm nhưng bị sót. Tìm lỗi:

```c
for (int i = 0; i < n; i++) {
    if (a[i] < 0) {
        for (int j = i; j < n - 1; j++) a[j] = a[j + 1];
        n--;
    }
}
```

**Bài 12.** Viết hàm gộp 2 mảng thành 1 bằng cách chèn lần lượt từng phần tử của mảng B vào mảng A.

**Bài 13.** So sánh độ phức tạp của chèn/xoá ở đầu, giữa, cuối mảng. Giải thích vì sao.

**Bài 14.** Làm lại bài 1, 2, 4 với mảng cấp phát động (`malloc`/`realloc`/`free`) để mảng tự lớn lên khi chèn. So sánh với mảng tĩnh.

**Bài 15.** Viết chương trình quản lý danh sách số nguyên với menu: thêm cuối, chèn tại vị trí, xoá theo vị trí, xoá theo giá trị, hiển thị, thoát.
