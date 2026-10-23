# [C]. Bài Tập Thực Tế - Biến, Nhập Xuất Và Toán Tử

Bài viết này gồm 10 bài tập lấy từ các tình huống thực tế hằng ngày (hóa đơn, rút tiền ATM, gửi xe, lãi tiết kiệm...). Mục tiêu là giúp bạn luyện tập tổng hợp các kiến thức đã học: **kiểu dữ liệu, biến, nhập xuất với scanf/printf và toán tử**.

**NỘI DUNG :** 

- **Quy Ước Khi Làm Bài**
- **10 Bài Tập Thực Tế**
- **Bảng Tổng Hợp Kiến Thức**

---

**Quy Ước Khi Làm Bài**

- Chỉ dùng kiến thức đã học đến bài [Toán Tử - Operator](../md-cpp/02-07-c-toan-tu-operator.md). **Không dùng `if`, vòng lặp, hàm tự viết.**
- Khi cần chọn giữa 2 trường hợp, hãy dùng **toán tử 3 ngôi** `dieu_kien ? a : b`.
- Tiền tệ tính bằng đồng, là số nguyên. Giả sử người dùng luôn nhập dữ liệu hợp lệ (trừ khi đề yêu cầu kiểm tra).
- Biên dịch với cờ `-Wall` để gcc cảnh báo lỗi : `gcc bai1.c -o bai1 -Wall`
- Hãy tự làm trước, sau đó mới mở phần **Lời giải tham khảo**.

---

**Bài 1. Hóa Đơn Siêu Thị**

**Tình huống :** Bạn đi siêu thị mua 3 mặt hàng: **Gạo, Sữa, Trứng**. Máy tính tiền cần in ra một hóa đơn rõ ràng, có thuế VAT 8%.

**Yêu cầu :** Nhập số lượng và đơn giá của từng mặt hàng. Tính thành tiền từng món, tiền tạm tính, tiền VAT (8% của tạm tính, lấy phần nguyên) và tổng thanh toán. In kết quả ra màn hình như mẫu.

Ví dụ - Input :

```
2 25000
3 32000
10 3500
```

Output (phần kết quả) :

```
Gao : 50000
Sua : 96000
Trung : 35000
Tam tinh : 181000
VAT 8% : 14480
Tong thanh toan : 195480
```

**Kiến thức luyện tập :** Phép `*`, `+`, `/`, `%` · In ký tự `%` bằng `%%`

**Gợi ý :** VAT tính bằng `tamTinh * 8 / 100`. Thử viết `tamTinh * (8 / 100)` xem kết quả là bao nhiêu và giải thích vì sao.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	int sl1, sl2, sl3;
	int gia1, gia2, gia3;
	printf("Nhap so luong va don gia Gao : ");
	scanf("%d%d", &sl1, &gia1);
	printf("Nhap so luong va don gia Sua : ");
	scanf("%d%d", &sl2, &gia2);
	printf("Nhap so luong va don gia Trung : ");
	scanf("%d%d", &sl3, &gia3);

	int tien1 = sl1 * gia1;
	int tien2 = sl2 * gia2;
	int tien3 = sl3 * gia3;
	int tamTinh = tien1 + tien2 + tien3;
	int vat = tamTinh * 8 / 100;
	int tong = tamTinh + vat;

	printf("Gao : %d\n", tien1);
	printf("Sua : %d\n", tien2);
	printf("Trung : %d\n", tien3);
	printf("Tam tinh : %d\n", tamTinh);
	printf("VAT 8%% : %d\n", vat);
	printf("Tong thanh toan : %d\n", tong);
	return 0;
}
```

</details>

---

**Bài 2. Rút Tiền ATM**

**Tình huống :** Máy ATM có các loại tờ 500.000, 200.000, 100.000, 50.000, 20.000 và 10.000 đồng. Máy luôn trả **ít tờ nhất** có thể.

**Yêu cầu :** Nhập số tiền cần rút (là bội số của 10.000). In ra số tờ của từng mệnh giá và tổng số tờ.

Ví dụ - Input :

```
1730000
```

Output (phần kết quả) :

```
500.000 : 3 to
200.000 : 1 to
100.000 : 0 to
50.000 : 0 to
20.000 : 1 to
10.000 : 1 to
Tong so to : 6
```

**Kiến thức luyện tập :** Chia nguyên `/` và chia dư `%` · Gán lại giá trị cho biến

**Gợi ý :** Lấy mệnh giá lớn nhất trước: `so_to = tien / 500000`, phần còn lại là `tien % 500000`, tiếp tục với mệnh giá kế tiếp.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	int tien;
	printf("Nhap so tien can rut : ");
	scanf("%d", &tien);

	int to500 = tien / 500000;
	tien = tien % 500000;
	int to200 = tien / 200000;
	tien = tien % 200000;
	int to100 = tien / 100000;
	tien = tien % 100000;
	int to50 = tien / 50000;
	tien = tien % 50000;
	int to20 = tien / 20000;
	tien = tien % 20000;
	int to10 = tien / 10000;

	printf("500.000 : %d to\n", to500);
	printf("200.000 : %d to\n", to200);
	printf("100.000 : %d to\n", to100);
	printf("50.000 : %d to\n", to50);
	printf("20.000 : %d to\n", to20);
	printf("10.000 : %d to\n", to10);
	printf("Tong so to : %d\n", to500 + to200 + to100 + to50 + to20 + to10);
	return 0;
}
```

</details>

---

**Bài 3. Chia Tiền Đi Ăn Nhóm**

**Tình huống :** Nhóm bạn đi ăn, hóa đơn cần chia đều. Để tiện trả tiền mặt, mỗi người trả một số tiền **làm tròn lên bội số của 1.000** đồng, đảm bảo tổng tiền thu được không thiếu.

**Yêu cầu :** Nhập tổng hóa đơn và số người. In ra số tiền chia đều chính xáx, số tiền mỗi người phải trả sau khi làm tròn, tổng tiền thu được và số tiền dư.

Ví dụ - Input :

```
1250000 6
```

Output (phần kết quả) :

```
Chia deu chinh xac : 208333.33
Moi nguoi tra : 209000
Tong thu duoc : 1254000
Tien du : 4000
```

**Kiến thức luyện tập :** Ép kiểu `(double)` · Mẹo chia làm tròn số nguyên: sử dụng thư viện math

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	int tong, n;
	printf("Nhap tong hoa don va so nguoi : ");
	scanf("%d%d", &tong, &n);

	int moiNguoi = (tong + n - 1) / n;              // chia lam tron len
	int lamTron = (moiNguoi + 999) / 1000 * 1000;   // lam tron len boi so 1000
	int daThu = lamTron * n;

	printf("Chia deu chinh xac : %.2lf\n", (double)tong / n);
	printf("Moi nguoi tra : %d\n", lamTron);
	printf("Tong thu duoc : %d\n", daThu);
	printf("Tien du : %d\n", daThu - tong);
	return 0;
}
```

</details>

---

**Bài 4. Tính Phí Gửi Xe**

**Tình huống :** Bãi giữ xe tính phí **5.000 đồng/giờ**, chưa đủ 1 giờ thì tính tròn 1 giờ. Xe gửi **không quá 15 phút** được miễn phí.

**Yêu cầu :** Nhập số phút gửi xe. In ra tổng số giờ và phút gửi xe, số giờ tính tiền và phí phải trả.

Ví dụ 1 - Input :

```
100
```

Output (phần kết quả) :

```
Thoi gian gui : 1h 40p
So gio tinh tien : 1h 40p
Phi gui xe : ...
```

Ví dụ 2 - Input :

```
08:00
08:12
```

Output (phần kết quả) :

```
Thoi gian gui : 12 phut
So gio tinh tien : 1
Phi gui xe : 0 dong
```

**Kiến thức luyện tập :** scanf với định dạng `%d:%d` · Quy đổi về cùng đơn vị (phút) · Toán tử so sánh và toán tử 3 ngôi

**Gợi ý :** Đổi cả 2 mốc thời gian ra số phút tính từ 00:00 rồi trừ cho nhau. Số giờ tính tiền dùng mẹo làm tròn lên ở bài 3.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	int gioVao, phutVao, gioRa, phutRa;
	printf("Gio vao (hh:mm) : ");
	scanf("%d:%d", &gioVao, &phutVao);
	printf("Gio ra (hh:mm) : ");
	scanf("%d:%d", &gioRa, &phutRa);

	int soPhut = (gioRa * 60 + phutRa) - (gioVao * 60 + phutVao);
	int soGio = (soPhut + 59) / 60;
	int phi = soPhut <= 15 ? 0 : soGio * 5000;

	printf("Thoi gian gui : %d phut\n", soPhut);
	printf("So gio tinh tien : %d\n", soGio);
	printf("Phi gui xe : %d dong\n", phi);
	return 0;
}
```

</details>

---

**Bài 5. Chỉ Số BMI**

**Tình huống :** Chỉ số khối cơ thể BMI = cân nặng (kg) / (chiều cao (m))². Phân loại: **< 18.5** Thiếu cân, **< 25** Bình thường, **< 30** Thừa cân, còn lại là Béo phì.

**Yêu cầu :** Nhập cân nặng (số thực, kg) và chiều cao (số nguyên, cm). In ra BMI với 1 chữ số thập phân và phân loại tương ứng.

Ví dụ 1 - Input :

```
65 170
```

Output (phần kết quả) :

```
BMI = 22.5
Phan loai : Binh thuong
```

Ví dụ 2 - Input :

```
48 172
```

Output (phần kết quả) :

```
BMI = 16.2
Phan loai : Thieu can
```

**Kiến thức luyện tập :** Chia số thực và chia số nguyên · Đổi đơn vị · Toán tử 3 ngôi lồng nhau

**Gợi ý :** Chiều cao nhập vào là cm kiểu `int`, đổi ra mét bằng `chieuCao / 100.0`. Nếu viết `chieuCao / 100` thì sao?

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	double canNang;
	int chieuCao;
	printf("Nhap can nang (kg) va chieu cao (cm) : ");
	scanf("%lf%d", &canNang, &chieuCao);

	double m = chieuCao / 100.0;
	double bmi = canNang / (m * m);

	printf("BMI = %.1lf\n", bmi);
	printf("Phan loai : %s\n",
		bmi < 18.5 ? "Thieu can" :
		bmi < 25 ? "Binh thuong" :
		bmi < 30 ? "Thua can" : "Beo phi");
	return 0;
}
```

</details>

---

**Bài 6. Lãi Tiền Gửi Tiết Kiệm**

**Tình huống :** Ngân hàng tính lãi tiết kiệm theo công thức: **tiền lãi = tiền gửi × lãi suất năm (%) / 100 × số tháng / 12**.

**Yêu cầu :** Nhập số tiền gửi, lãi suất năm (có thể lẻ, ví dụ 5.5) và số tháng gửi. In ra tiền lãi và tổng tiền nhận được khi đáo hạn (làm tròn đến đồng).

Ví dụ - Input :

```
100000000 5.5 9
```

Output (phần kết quả) :

```
Tien lai : 4125000 dong
Tong nhan : 104125000 dong
```

**Kiến thức luyện tập :** Kiểu `long long`, `double` · Đặc tả `%lld`, `%lf`, `%.0lf` · Thứ tự thực hiện phép toán

**Gợi ý :** Chạy thử 2 cách viết sai sau và giải thích kết quả: (1) khai báo `tienGui` kiểu `int` rồi nhập 3 tỷ; (2) viết công thức thành `tienGui * laiSuat / 100 * (soThang / 12)`.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	long long tienGui;
	double laiSuat;
	int soThang;
	printf("Nhap so tien gui, lai suat (%%/nam), so thang : ");
	scanf("%lld%lf%d", &tienGui, &laiSuat, &soThang);

	double tienLai = tienGui * laiSuat / 100 * soThang / 12;
	double tongNhan = tienGui + tienLai;

	printf("Tien lai : %.0lf dong\n", tienLai);
	printf("Tong nhan : %.0lf dong\n", tongNhan);
	return 0;
}
```

</details>

---

**Bài 7. Xét Tuyển Đại Học**

**Tình huống :** Thí sinh **trúng tuyển** khi tổng điểm 3 môn Toán, Lý, Hóa cộng điểm ưu tiên **đạt điểm chuẩn**, đồng thời **không có môn nào bị điểm liệt** (điểm ≤ 1).

**Yêu cầu :** Nhập điểm 3 môn, điểm ưu tiên và điểm chuẩn. In ra tổng điểm (2 chữ số thập phân), kết quả trúng tuyển hay không và lý do.

Ví dụ 1 - Input :

```
8.5 7.75 7
0.5 24
```

Output (phần kết quả) :

```
Tong diem xet tuyen : 23.75
Ket qua : KHONG TRUNG TUYEN
Ly do : Thieu diem chuan
```

Ví dụ 2 - Input :

```
9 9.5 1
0 18
```

Output (phần kết quả) :

```
Tong diem xet tuyen : 19.50
Ket qua : KHONG TRUNG TUYEN
Ly do : Co mon bi diem liet
```

**Kiến thức luyện tập :** Kiểu `bool` · Toán tử so sánh · Toán tử logic `&&`, `||`, `!`

**Gợi ý :** Tạo 2 biến `bool`: `biLiet` (có ít nhất một môn ≤ 1) và `dat` (đủ điểm chuẩn **và** không bị liệt). Đặt tên biến rõ nghĩa sẽ giúp biểu thức logic dễ đọc hơn rất nhiều.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>
#include <stdbool.h>

int main(){
	double toan, ly, hoa, uuTien, diemChuan;
	printf("Nhap diem Toan, Ly, Hoa : ");
	scanf("%lf%lf%lf", &toan, &ly, &hoa);
	printf("Nhap diem uu tien va diem chuan : ");
	scanf("%lf%lf", &uuTien, &diemChuan);

	double tong = toan + ly + hoa + uuTien;
	bool biLiet = toan <= 1 || ly <= 1 || hoa <= 1;
	bool dat = tong >= diemChuan && !biLiet;

	printf("Tong diem xet tuyen : %.2lf\n", tong);
	printf("Ket qua : %s\n", dat ? "TRUNG TUYEN" : "KHONG TRUNG TUYEN");
	printf("Ly do : %s\n",
		biLiet ? "Co mon bi diem liet" :
		dat ? "Du diem chuan" : "Thieu diem chuan");
	return 0;
}
```

</details>

---

**Bài 8. Khuyến Mãi Mua 3 Tặng 1**

**Tình huống :** Cửa hàng chạy chương trình **mua 3 tặng 1**: cứ mỗi 4 sản phẩm khách lấy thì 1 sản phẩm được miễn phí. Ngoài ra, nếu tiền hàng **từ 300.000 đồng** trở lên thì được giảm thêm 5%.

**Yêu cầu :** Nhập số lượng sản phẩm khách lấy và đơn giá. In ra số sản phẩm được tặng, số sản phẩm tính tiền, tiền hàng, tiền được giảm và số tiền khách phải trả.

Ví dụ - Input :

```
10 45000
```

Output (phần kết quả) :

```
So san pham duoc tang : 2
So san pham tinh tien : 8
Tien hang : 360000
Giam them 5% : 18000
Khach tra : 342000
```

**Kiến thức luyện tập :** Chia nguyên · Toán tử so sánh · Toán tử 3 ngôi

**Gợi ý :** Số sản phẩm được tặng là `soLuong / 4`. Tiền giảm: `tienHang >= 300000 ? tienHang * 5 / 100 : 0`.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	int soLuong, donGia;
	printf("Nhap so luong lay va don gia : ");
	scanf("%d%d", &soLuong, &donGia);

	int soTang = soLuong / 4;
	int soTra = soLuong - soTang;
	int tienHang = soTra * donGia;
	int giamGia = tienHang >= 300000 ? tienHang * 5 / 100 : 0;

	printf("So san pham duoc tang : %d\n", soTang);
	printf("So san pham tinh tien : %d\n", soTra);
	printf("Tien hang : %d\n", tienHang);
	printf("Giam them 5%% : %d\n", giamGia);
	printf("Khach tra : %d\n", tienHang - giamGia);
	return 0;
}
```

</details>

---

**Bài 9. Hôm Nay Thứ Mấy**

**Tình huống :** Hôm nay là một ngày trong tuần, quy ước Thứ 2 → `2`, ..., Thứ 7 → `7`, Chủ nhật → `8`. Bạn muốn biết **sau n ngày** nữa (ví dụ ngày hết hạn một đơn hàng) sẽ là thứ mấy.

**Yêu cầu :** Nhập thứ của hôm nay và số ngày n (n ≥ 0). In ra sau n ngày sẽ là thứ mấy (in theo đúng quy ước số `2` → `8`).

Ví dụ 1 - Input :

```
6
100
```

Output (phần kết quả) :

```
Sau 100 ngay se la thu : 8
```

Ví dụ 2 - Input :

```
3
4
```

Output (phần kết quả) :

```
Sau 4 ngay se la thu : 7
```

**Kiến thức luyện tập :** Phép chia dư `%` cho các giá trị lặp vòng (tuần, giờ, tháng...)

**Gợi ý :** Dời giá trị về bắt đầu từ 0 (`thu - 2`), cộng thêm n, lấy dư cho 7, rồi dời ngược lại (`+ 2`).

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>

int main(){
	int thu, n;
	printf("Hom nay la thu may (2-7, 8 = Chu nhat) : ");
	scanf("%d", &thu);
	printf("Sau bao nhieu ngay : ");
	scanf("%d", &n);

	int ketQua = (thu - 2 + n) % 7 + 2;

	printf("Sau %d ngay se la thu : %d\n", n, ketQua);
	return 0;
}
```

</details>

---

**Bài 10. Kiểm Tra Ngày Hợp Lệ**

**Tình huống :** Các form đăng ký trên web thường phải kiểm tra ngày sinh người dùng nhập có tồn tại hay không. Tháng 4, 6, 9, 11 có 30 ngày; tháng 2 có 29 ngày nếu là năm nhuận, ngược lại 28 ngày; các tháng còn lại có 31 ngày.

**Yêu cầu :** Nhập ngày theo định dạng `dd/mm/yyyy`. In ra **HOP LE** hoặc **KHONG HOP LE**.

Ví dụ 1 - Input :

```
29/02/2024
```

Output (phần kết quả) :

```
HOP LE
```

Ví dụ 2 - Input :

```
31/04/2025
```

Output (phần kết quả) :

```
KHONG HOP LE
```

**Kiến thức luyện tập :** scanf với định dạng `%d/%d/%d` · Kết hợp toán tử logic, so sánh và 3 ngôi lồng nhau

**Gợi ý :** Đi từng bước: (1) tính biến `bool namNhuan`; (2) tính số ngày của tháng bằng toán tử 3 ngôi; (3) ngày hợp lệ khi tháng trong khoảng 1..12 **và** ngày trong khoảng 1..số ngày của tháng.

<details>
<summary><b>Lời giải tham khảo</b></summary>

```c
#include <stdio.h>
#include <stdbool.h>

int main(){
	int ngay, thang, nam;
	printf("Nhap ngay (dd/mm/yyyy) : ");
	scanf("%d/%d/%d", &ngay, &thang, &nam);

	bool namNhuan = (nam % 4 == 0 && nam % 100 != 0) || nam % 400 == 0;
	int soNgayCuaThang =
		thang == 2 ? (namNhuan ? 29 : 28) :
		(thang == 4 || thang == 6 || thang == 9 || thang == 11) ? 30 : 31;
	bool hopLe = thang >= 1 && thang <= 12 && ngay >= 1 && ngay <= soNgayCuaThang;

	printf("%s\n", hopLe ? "HOP LE" : "KHONG HOP LE");
	return 0;
}
```

</details>

---

**Bảng Tổng Hợp Kiến Thức**

| **Bài** | **Tình huống** | **Kiến thức chính** |
|---|---|---|
| 1 | Hóa đơn siêu thị | Toán tử toán học, in ký tự `%%` |
| 2 | Rút tiền ATM | `/` và `%` liên tiếp |
| 3 | Chia tiền đi ăn | Ép kiểu, chia làm tròn lên |
| 4 | Phí gửi xe | scanf `%d:%d`, quy đổi đơn vị, 3 ngôi |
| 5 | Chỉ số BMI | Chia số thực, 3 ngôi lồng nhau |
| 6 | Lãi tiết kiệm | `long long`, `double`, tràn số, thứ tự phép toán |
| 7 | Xét tuyển đại học | `bool`, toán tử logic |
| 8 | Mua 3 tặng 1 | Chia nguyên, so sánh, 3 ngôi |
| 9 | Hôm nay thứ mấy | `%` với giá trị lặp vòng |
| 10 | Kiểm tra ngày hợp lệ | Tổng hợp logic + so sánh + 3 ngôi |

**Thử thách mở rộng** (sau khi học `if` và vòng lặp) : quay lại bài 2 kiểm tra số tiền không phải bội số của 10.000, bài 4 xử lý trường hợp gửi xe qua đêm, bài 9 cho phép n âm (n ngày trước).
