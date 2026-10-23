# [C++]. Lý Thuyết Số Và Toán Học

Học lập trình yêu cầu bạn cũng có những kiến thức cơ bản nhất định về toán học, toán học trong lập trình cũng giúp bạn nâng cao tư duy logic và khả năng suy luận.

Bài viết này mình tổng hợp những kiến thức về toán học và lý thuyết số mà bạn cần nắm vững khi học lập trình.

**NỘI DUNG :** 

- **Các Kiến Thức Toán Học Quan Trọng** 
- **Video Tutorial** 

---

**Các Kiến Thức Toán Học Quan Trọng**

Các bạn click vào link từng bài để xem chi tiết nội dung nhé

- [Số nguyên tố](https://blog.codelab.dev/c-so-nguyen-to)
- [Số chính phương](https://blog.codelab.dev/c-so-chinh-phuong)
- [Số thuận nghịch (đối xứng)](https://blog.codelab.dev/c-so-thuan-nghich)
- [Đếm (tính tổng) ước của số nguyên](https://blog.codelab.dev/c-tinh-tong-uoc-so-nguyen)
- [Số hoàn hảo (hoàn thiện)](https://blog.codelab.dev/c-so-hoan-hao)
- [Ước chung lớn nhất - Bội chung nhỏ nhất](https://blog.codelab.dev/c-uoc-chung-lon-nhat-boi-chung-nho-nhat)
- [Số Fibonacci](https://blog.codelab.dev/c-so-fibonacci)
- [Phân tích thừa số nguyên tố](https://blog.codelab.dev/c-phan-tich-thua-so-nguyen-to)
- [Sàng số nguyên tố Eratosthenes](https://blog.codelab.dev/sang-so-nguyen-to)
- [Lý thuyết Đồng Dư](https://blog.codelab.dev/ly-thuyet-dong-du)
- [Công thức Legendre](https://blog.codelab.dev/bac-thua-so-nguyen-to-trong-giai-thua)
- [Lũy thừa nhị phân](https://blog.codelab.dev/luy-thua-nhi-phan)

**Danh sách phát về lý thuyết số và tổ hợp :**

---

## 🎯 BÀI TẬP

> 📘 Lời giải tham khảo: [solutions/05-05-cpp-ly-thuyet-so-va-toan-hoc.md](solutions/05-05-cpp-ly-thuyet-so-va-toan-hoc.md)

Mỗi bài tập dưới đây tương ứng với một chủ đề trong danh sách kiến thức ở trên. Hãy viết mỗi lời giải thành một **hàm riêng** để tái sử dụng về sau.

**Bài 1.** Viết hàm `bool laNguyenTo(long long n)` kiểm tra số nguyên tố với độ phức tạp O(√n).

**Bài 2.** Viết hàm `bool laChinhPhuong(long long n)` kiểm tra số chính phương, xử lý đúng sai số của `sqrt`.

**Bài 3.** Viết hàm `bool laThuanNghich(long long n)` kiểm tra số thuận nghịch (đối xứng).

**Bài 4.** Viết hàm `int demUoc(long long n)` và `long long tongUoc(long long n)` với độ phức tạp O(√n).

**Bài 5.** Viết hàm `bool laHoanHao(long long n)` kiểm tra số hoàn hảo. In ra tất cả số hoàn hảo nhỏ hơn 10000.

**Bài 6.** Viết hàm `ucln` và `bcnn` cho `long long`, chú ý tránh tràn số khi tính BCNN.

**Bài 7.** Viết hàm `long long fibonacci(int n)` bằng vòng lặp. In ra 30 số Fibonacci đầu tiên.

**Bài 8.** Viết hàm phân tích một số ra thừa số nguyên tố, in dạng `360 = 2^3 * 3^2 * 5`.

**Bài 9.** Cài đặt sàng Eratosthenes: đánh dấu tất cả số nguyên tố ≤ 10⁶ và đếm xem có bao nhiêu số.

**Bài 10.** Dùng sàng ở bài 9 để trả lời nhanh 1000 truy vấn "n có phải số nguyên tố?".

**Bài 11.** Viết hàm luỹ thừa nhị phân `long long luyThuaNhanh(long long a, long long n, long long mod)` tính `a^n mod m`.

**Bài 12.** Tính `2^1000 mod (10^9+7)` bằng hàm ở bài 11.

**Bài 13.** Viết hàm đếm số chữ số 0 ở cuối của `n!` (công thức Legendre với cơ số 5).

**Bài 14.** Viết hàm kiểm tra 2 số có nguyên tố cùng nhau không (UCLN = 1). Đếm xem trong 1..100 có bao nhiêu số nguyên tố cùng nhau với 60.

**Bài 15.** Viết một **thư viện** `sohoc.h` + `sohoc.cpp` gộp tất cả các hàm trên, có header guard và chú thích Doxygen.
