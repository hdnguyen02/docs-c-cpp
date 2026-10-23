# Bậc Thừa Số Nguyên Tố Trong Giai Thừa

Bậc của thừa số nguyên tố p trong N giai thừa là số mũ x lớn nhất sao cho N! chia hết cho px . Bài viết này mình sẽ hướng dẫn các bạn tìm bậc của thừa số nguyên tố bằng cách thông thường và cách tối ưu bằng công thức Legendre.

**NỘI DUNG :** 

- **Bậc Của Thừa Số Nguyên Tố Trong Giai Thừa**
- **Công Thức Legendre**
- **Bài Toán Đếm Số 0 Của N!**
- **Bậc Của Hợp Số Trong Giai Thừa**
- **Video Tutorial**

---

**1. Bậc Của Thừa Số Nguyên Tố Trong Giai Thừa**

**Bài toán :** Cho số nguyên dương N và số nguyên tố p, tìm số x lớn nhất sao cho N! chia hết cho px . Ví dụ với N = 10 và p = 2 thì N! chia hết tối đa cho 28.

Bài toán này với N có thể rất lớn nên việc đi tính N! sau đó chia cho p để đếm số mũ là không khả thi. Việc đi tìm x ở bài toán trên tương tự như bạn đang cố gắng đi phân tích thừa số nguyên tố của N! nhưng không cần tính giá trị của N!

Ta có N! = 1.2.3.4....(N-1).N và vì p là số nguyên tố nên tích của N số từ 1 đến N trong N! chứa bao nhiêu số p thì đó là bậc của p trong N!. Việc xác định trong N! có bao nhiêu số p ta chỉ cần xét các bội số của p, vì p là số nguyên tố nên nó không thể được tạo ra bởi tích nhiều số nhỏ hơn nên ta không cần lo lắng việc này.

Ví dụ N = 10 thì N! = 10 ! = 1.2.3.4.5.6.7.8.9.10 và p = 2 thì rõ ràng chỉ có các số 2, 4, 6, 8, 10 là các bội số của 2 chứa số 2 trong phân tích thừa số nguyên tố của nó.

Dựa trên nhận xét trên thì ta có thuật toán ngây thơ như sau :

**Thuật toán :** 

- Duyệt các bội số của p nhỏ hơn hoặc bằng N
- Với mỗi bội số của p thì phân tích xem bội số đó chứa bao nhiêu số p

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

#define ll long long

int find_power(int n, int p){
	int res = 0, tmp;
	for(int i = p; i <= n; i += p){
		tmp = i;
		//Phan tich boi i cua p
		while(tmp % p == 0){
			++res;
			tmp /= p;
		}
	}
	return res;
}

int main(){
	cout << "Bac cua 2 trong 10 ! : " << find_power(10, 2) << endl;
	cout << "Bac cua 17 trong 1000000! : " << find_power(1000000, 17) << endl;
	return 0;
}
```

Output :

```cpp
Bac cua 2 trong 10 ! : 8
Bac cua 17 trong 1000000! : 62497
```

**2. Công Thức Legendre**

Công thức Legendre giúp bạn tìm bậc của thừa số nguyên tố trong giai thừa một cách hiệu quả hơn so với phương pháp thông thường trong mục 1.

Legendre's formular :

![](../images/926464f33112300e.png)

Hay :* *vp(n!) = n / p1 + n / p2 + ... + n / pL với pL ≤ n

Ở đây phép chia của n cho lũy thừa của p là phép chia nguyên

Ví dụ N = 35 và p = 3 thì bậc của 3 trong 35! = 35 / 3 + 35 / 9 + 35 / 27 = 11 + 3 + 1 = 15

Độ phức tạp của công thức này chỉ còn là O(logKN)

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

#define ll long long

int legendre(int n, int p){
	int res = 0;
	for(int i = p; i <= n; i *= p){
		res += n / i;
	}
	return res;
}

int main(){
	cout << "Bac cua 3 trong 35 ! : " << legendre(35, 3) << endl;
	cout << "Bac cua 17 trong 1000000! : " << legendre(1000000, 17) << endl;
	return 0;
}
```

Output :

```cpp
Bac cua 3 trong 35 ! : 15
Bac cua 17 trong 1000000! : 62497
```

**Giải thích công thức Legendre :** 

Thực chất công thức Legendre cũng ngầm tính số lần xuất hiện của thừa số nguyên tố p trong N! bằng cách đếm số bội của p nhỏ hơn hoặc bằng N. Ở đây mình sẽ lấy ví dụ vói N = 35 và p = 3

1. Khi tính N / p1 thì ta tính được số bội của p mà trong đó mỗi bội này chứa 1 số p. Với N = 35 và p = 3 thì ta sẽ có 11 số là 3, 6, 9, 12, 15...30, 33
2. Khi tính N / p2 thì ta tính được số bội số của p mà trong đó mỗi bội này chứa 2 số p. Với N = 35 và p = 3 thì ta có 3 số là 9, 18, 27 và vì 3 số này đã được đếm 1 lượt ở bước 1 rồi nên tới bước này ta đếm thêm mỗi số 1 lượt nữa vì bản thân chúng chứa ít nhất 2 số 3
3. Khi tính N / p3 thì ta tính được số bội số của p mà trong đó mỗi bội này chứa 3 số p. Với N = 35 và p = 3 thì ta có 1 số là 27, số 27 này bản thân nó chứa 3 số 3 và cũng được đếm 3 lần, 1 lần ở bước 1, 1 lần bước 2 và 1 lần ở bước 3
4. Tương tự như vậy cho tới khi ta xét tới lũy thừa pL ≤ N

**3. Bài Toán Đếm Số 0 của N!**

**Bài toán** : Cho số N (1 ≤ N ≤ 109) hãy đếm số lượng chữ số 0 liên tiếp tính từ cuối của N giai thừa

Link submit : [https://cses.fi/problemset/task/1618](https://cses.fi/problemset/task/1618)

**Thuật toán :** 

- Nhận thấy khi tính N! và có số 0 ở cuối nếu tích các số nhân với nhau xuất hiện số 10 mà 10 = 2 x 5 nên ta chỉ cần đếm số lượng số 2 trong N! và số lượng số 5 trong N! thì có thể suy ra số lượng số 10 xuất hiện trong N! và đây cũng chính là số các số 0 liên tiếp tính từ cuối
- Vì 2 < 5 nên trong N! bậc của 5 cũng sẽ nhỏ hơn bậc của 2, do đó số lượng cặp (2, 5) tối đa trong N! chính là bậc của 5 trong N!, bạn chỉ cần đi tính bậc của 5 trong N!

**Mã nguồn :** 

```cpp
#include "iostream"

using namespace std;

#define ll long long

int legendre(int n, int p){
	int res = 0;
	for(int i = p; i <= n; i *= p){
		res += n / i;
	}
	return res;
}

int main(){
	int n; cin >> n;
	cout << legendre(n, 5) << endl;
	return 0;
}
```

---

**4. Bậc Của Hợp Số Trong Giai Thừa**

Trong trường hợp số p không còn là số nguyên tố thì vấn đề sẽ phức tạp hơn khi ta cần tìm x, vì p có thể được tạo thành bởi các số nhỏ hơn p nhân lại với nhau. Ví dụ với p = 6 thì 6 có thể không chỉ xuất hiện trong các bội của 6 mà có thể tổ hợp được từ các số 2 và 3.

Với p là hợp số thì bạn cần phân tích thừa số nguyên tố của p và tìm các thừa số nguyên tố của p

Giả sử *p = p1e1 * p2e2 * p3e3 * ... *pkek*, với mỗi thừa số nguyên tố của p bạn cần biết bậc của nó trong N! lần lượt là *x1, x2, x3... xk*. Khi đó bậc của hợp số p trong N! sẽ là *min(x1 / e1, x2 / e2,..., xk / ek)*

**Video Tutorial :**
