# Lời giải — [C]. IDE Học Lập Trình C

[← Quay lại bài học](../01-03-c-ide-hoc-lap-trinh-c.md)

---

### Bài 1.

**IDE = Integrated Development Environment** — Môi trường phát triển tích hợp.

4 chức năng chính:

1. **Soạn thảo code** — có tô màu cú pháp (syntax highlighting), gợi ý code (autocomplete), tự thụt lề.
2. **Biên dịch (compile)** — chuyển mã nguồn C thành file thực thi.
3. **Gỡ lỗi (debug)** — chạy từng dòng, đặt breakpoint, xem giá trị biến tại thời điểm chạy.
4. **Quản lý dự án và kiểm thử** — tổ chức nhiều file trong một project, chạy test, tích hợp Git.

### Bài 2.

| | Text Editor | Compiler |
|---|---|---|
| Nhiệm vụ | Soạn thảo, chỉnh sửa văn bản/code | Dịch mã nguồn sang mã máy |
| Kết quả tạo ra | File `.c` (văn bản) | File thực thi (`.exe`, hoặc file nhị phân) |
| Ví dụ | Notepad, Sublime Text, VSCode, VIM | gcc, clang, MSVC |

**Notepad KHÔNG phải IDE.** Notepad chỉ là text editor thuần tuý: nó không biên dịch được, không tô màu cú pháp, không debug được. Bạn vẫn có thể *viết* code C bằng Notepad, nhưng phải dùng một compiler riêng bên ngoài để chạy được code đó.

Lưu ý: **VSCode về bản chất cũng là một text editor**, nhưng nhờ cài thêm extension và trình biên dịch nên nó hoạt động như một IDE.

### Bài 3.

```
   main.c                   (mã nguồn C — người đọc được)
      │
      │  ① Tiền xử lý (Preprocessor)
      │     Xử lý #include, #define — chèn nội dung file header vào
      ▼
   main.i                   (mã nguồn đã được mở rộng)
      │
      │  ② Biên dịch (Compiler)
      │     Kiểm tra cú pháp, dịch sang hợp ngữ
      ▼
   main.s                   (mã Assembly)
      │
      │  ③ Hợp dịch (Assembler)
      ▼
   main.o                   (mã máy, chưa liên kết)
      │
      │  ④ Liên kết (Linker)
      │     Nối với thư viện chuẩn C (chứa printf, scanf, sqrt...)
      ▼
   main.exe / main          (file thực thi — máy chạy được)
      │
      │  ⑤ Chạy
      ▼
   Kết quả in ra màn hình
```

Trong thực tế khi bạn gõ `gcc main.c -o main`, cả 4 bước đầu diễn ra tự động và bạn chỉ thấy file thực thi ở cuối.

Nếu muốn xem từng bước:

```bash
gcc -E main.c -o main.i     # chỉ tiền xử lý
gcc -S main.c -o main.s     # dừng sau khi dịch sang assembly
gcc -c main.c -o main.o     # dừng sau khi tạo file object
gcc main.o -o main          # liên kết
```

### Bài 4.

Hướng dẫn cài theo hệ điều hành:

| Hệ điều hành | Cách cài |
|---|---|
| **Windows** | Tải DevC++ (bản Embarcadero hoặc Orwell) và cài như phần mềm thường — đã kèm sẵn compiler MinGW (có `gcc`). |
| **Windows (nâng cao)** | Cài VSCode + MinGW-w64, thêm đường dẫn `bin` của MinGW vào biến môi trường PATH. |
| **Linux (Ubuntu/Debian)** | `sudo apt update && sudo apt install build-essential` (có `gcc`, `make`) |
| **macOS** | `xcode-select --install` (cài Command Line Tools, có sẵn `clang`), hoặc cài XCode từ App Store. |

### Bài 5.

```bash
gcc --version
```

Kết quả ví dụ trên Linux:

```
gcc (Ubuntu 13.2.0-23ubuntu4) 13.2.0
```

Trên macOS, lệnh `gcc` thực chất gọi tới clang:

```bash
gcc --version
# Apple clang version 15.0.0 (clang-1500.3.9.4)
```

Nếu báo `command not found` / `'gcc' is not recognized` thì compiler chưa cài, hoặc (trên Windows) chưa thêm thư mục `bin` của MinGW vào biến môi trường **PATH**.

### Bài 6.

File `hello.c`:

```c
#include <stdio.h>

int main(void) {
    printf("Xin chao C\n");
    return 0;
}
```

Biên dịch và chạy bằng dòng lệnh:

```bash
# Linux / macOS
gcc hello.c -o hello
./hello

# Windows (cmd)
gcc hello.c -o hello.exe
hello.exe
```

Kết quả:

```
Xin chao C
```

### Bài 7.

```bash
gcc hello.c -o chaythu
./chaythu
```

Tuỳ chọn `-o` (output) quyết định **tên file thực thi** được tạo ra. Nếu bỏ `-o`, gcc sẽ tạo file mặc định tên `a.out` (Linux/macOS) hoặc `a.exe` (Windows).

### Bài 8.

Sửa file thành (thiếu `;`):

```c
#include <stdio.h>

int main(void) {
    printf("Xin chao C\n")
    return 0;
}
```

Thông báo lỗi:

```
hello.c: In function 'main':
hello.c:4:27: error: expected ';' before 'return'
    4 |     printf("Xin chao C\n")
      |                           ^
      |                           ;
    5 |     return 0;
      |     ~~~~~~
```

**Cách đọc:** `hello.c:4:27` nghĩa là **file hello.c, dòng 4, cột 27**. Thông điệp `expected ';' before 'return'` = "cần một dấu `;` trước từ khoá `return`".

⚠️ Lưu ý quan trọng: compiler báo lỗi ở **dòng 4**, nhưng nó phát hiện ra khi đọc tới `return` ở dòng 5. Nói chung, khi lỗi kiểu "expected ';'", hãy nhìn vào **dòng ngay phía trên** dòng chứa từ được nhắc tới.

### Bài 9.

| Tuỳ chọn | Ý nghĩa |
|---|---|
| `-o <tên>` | Đặt tên cho file thực thi đầu ra. Không có thì mặc định là `a.out`. |
| `-Wall` | **W**arning **all** — bật hầu hết cảnh báo hữu ích: biến khai báo mà không dùng, biến dùng khi chưa gán giá trị, sai đặc tả định dạng trong `printf`/`scanf`… Rất nên bật. |
| `-Wextra` | Bật thêm các cảnh báo mà `-Wall` bỏ qua (so sánh số có dấu với không dấu, tham số không dùng…). |
| `-std=c11` | Biên dịch theo chuẩn C11. Không có thì gcc dùng chuẩn mặc định của phiên bản đó (thường là `gnu17`, có thêm phần mở rộng riêng của GNU). |
| `-g` | Nhúng thông tin gỡ lỗi vào file thực thi, để dùng được debugger (gdb/lldb) và xem đúng tên biến, số dòng. |
| `-O2` | Tối ưu tốc độ chương trình (thường dùng khi nộp bài thi đấu). |
| `-lm` | Liên kết thư viện toán học (`libm`) — cần trên Linux khi dùng các hàm trong `<math.h>` như `sqrt`, `pow`. Đặt ở **cuối** lệnh. |
| `-fsanitize=address` | Phát hiện lỗi truy cập mảng ngoài biên, memory leak lúc chạy. Rất hữu ích khi học con trỏ. |

Lệnh biên dịch đầy đủ nên dùng khi học:

```bash
gcc -std=c11 -Wall -Wextra -g hello.c -o hello -lm
```

### Bài 10.

| Tiêu chí | DevC++ | Visual Studio Code |
|---|---|---|
| **Dễ cài đặt** | ⭐⭐⭐⭐⭐ Cài 1 lần là xong, đã kèm compiler | ⭐⭐ Phải cài thêm compiler (MinGW/gcc) + extension + cấu hình |
| **Dung lượng** | ⭐⭐⭐⭐⭐ Rất nhẹ (~100 MB) | ⭐⭐⭐ Nặng hơn (~350 MB + extension) |
| **Tính năng hỗ trợ** | ⭐⭐ Gợi ý code yếu, giao diện cũ, không có Git | ⭐⭐⭐⭐⭐ IntelliSense mạnh, Git tích hợp, hàng nghìn extension, terminal tích hợp |
| **Dùng lâu dài** | ⭐ Chỉ hợp học cơ bản, không dùng đi làm; bản gốc đã ngừng phát triển | ⭐⭐⭐⭐⭐ Dùng được cho mọi ngôn ngữ, mọi dự án, dùng suốt sự nghiệp |

**Kết luận:** người mới hoàn toàn có thể bắt đầu bằng DevC++ để không tốn thời gian cấu hình; nhưng nên chuyển sang VSCode sau khoảng 1–2 tháng, vì đó là công cụ bạn sẽ dùng lâu dài.

### Bài 11.

| Thao tác | DevC++ | VSCode | Code::Blocks |
|---|---|---|---|
| Biên dịch | `F9` | `Ctrl + Shift + B` | `Ctrl + F9` |
| Chạy | `F10` | `F5` (debug) / `Ctrl + F5` (chạy thường) | `Ctrl + F10` |
| Biên dịch & chạy | `F11` | (cấu hình task) | `F9` |
| Lưu file | `Ctrl + S` | `Ctrl + S` | `Ctrl + S` |
| Format code | `Ctrl + Shift + A` (AStyle) | `Shift + Alt + F` | `Ctrl + Shift + F` |

*(Trên macOS thay `Ctrl` bằng `Cmd`.)*

### Bài 12.

**Vì sao DevC++ không chạy trên macOS/Linux:** DevC++ được viết bằng Delphi cho Windows API, và nó đóng gói sẵn MinGW — bộ công cụ biên dịch dành riêng cho Windows. Nó không có bản build cho hệ điều hành khác.

Thay thế:

| Hệ điều hành | Nên dùng |
|---|---|
| **macOS** | XCode, hoặc VSCode + clang (cài qua `xcode-select --install`), hoặc CLion |
| **Linux** | VSCode + gcc, Code::Blocks, CLion, hoặc chỉ cần `vim`/`nano` + gcc trong terminal |

Lưu ý: trên Linux/macOS, trình biên dịch (`gcc`/`clang`) là **công cụ dòng lệnh có sẵn hoặc cài rất dễ**, nên bạn không nhất thiết phải có IDE — chỉ cần một text editor bất kỳ là code được.

### Bài 13.

**Debug** = gỡ lỗi: chạy chương trình ở chế độ đặc biệt cho phép dừng lại ở dòng bất kỳ và quan sát giá trị của từng biến tại thời điểm đó. Đây là cách tìm **lỗi logic** (chương trình chạy được nhưng cho kết quả sai) — loại lỗi mà compiler không thể báo.

Các khái niệm cần biết:

| Thuật ngữ | Ý nghĩa |
|---|---|
| **Breakpoint** | Điểm dừng — chương trình chạy tới dòng này sẽ tạm dừng |
| **Step Over** (`F10`) | Chạy dòng hiện tại rồi dừng ở dòng kế tiếp |
| **Step Into** (`F11`) | Nếu dòng hiện tại gọi hàm thì nhảy *vào bên trong* hàm đó |
| **Watch** | Danh sách biến cần theo dõi giá trị |
| **Call Stack** | Chuỗi các hàm đang gọi lồng nhau |

Các bước thực hành trong VSCode:

1. Biên dịch có kèm `-g`: `gcc -g hello.c -o hello`
2. Bấm vào lề trái, bên cạnh số dòng → xuất hiện chấm đỏ (breakpoint)
3. Bấm `F5` → chọn `C/C++ (GDB/LLDB)`
4. Chương trình dừng ở breakpoint; xem mục **Variables** ở khung bên trái để thấy giá trị biến
5. Dùng `F10` để chạy từng dòng

Debug bằng dòng lệnh với gdb:

```bash
gcc -g hello.c -o hello
gdb ./hello
(gdb) break main      # đặt breakpoint ở hàm main
(gdb) run             # chạy
(gdb) next            # chạy từng dòng
(gdb) print bien      # xem giá trị biến
(gdb) quit
```

### Bài 14.

**File `.exe`** (executable) là file chứa mã máy đã biên dịch xong, hệ điều hành Windows nạp vào bộ nhớ và chạy trực tiếp. Bạn không mở nó bằng text editor để đọc được, vì nội dung là mã nhị phân.

**Trên Linux/macOS file thực thi KHÔNG có đuôi.** Đuôi file trên các hệ này chỉ mang tính gợi ý cho người dùng; cái quyết định một file có chạy được hay không là **quyền thực thi (execute permission)**:

```bash
ls -l hello
# -rwxrwxr-x 1 user user 15960 Sep 17 11:00 hello
#    ↑  ↑  ↑
#    x  x  x  <- có quyền thực thi
```

Nếu file chưa có quyền chạy, cấp bằng: `chmod +x hello`

**Vì sao phải gõ `./hello` mà không phải `hello`:** khi bạn gõ một tên không có dấu `/`, shell chỉ tìm chương trình đó trong các thư mục liệt kê ở biến môi trường `PATH` (như `/usr/bin`, `/bin`) — **thư mục hiện tại không nằm trong PATH**. Dấu `./` nghĩa là "thư mục hiện tại", tức bạn chỉ rõ đường dẫn cho shell.

Đây là một biện pháp **bảo mật**: nếu thư mục hiện tại nằm trong PATH, kẻ xấu chỉ cần đặt vào thư mục của bạn một file tên `ls` chứa mã độc, và bạn sẽ chạy nhầm nó khi gõ `ls`.

```bash
echo $PATH        # xem các thư mục shell sẽ tìm
which gcc         # xem gcc nằm ở đâu
```

### Bài 15.

**Linux / macOS** — file `run-c.sh`:

```bash
#!/usr/bin/env bash
# Bien dich va chay mot file C
# Dung: ./run-c.sh hello.c

set -e                              # gap loi thi dung ngay

SRC="${1:-main.c}"                  # khong truyen tham so -> mac dinh main.c
[ $# -gt 0 ] && shift               # phan con lai la tham so cua chuong trinh

# cho phep go ten khong co duoi .c
[[ "$SRC" != *.c ]] && [ -f "$SRC.c" ] && SRC="$SRC.c"

if [ ! -f "$SRC" ]; then
    echo "Khong tim thay file '$SRC'" >&2
    exit 1
fi

OUT="${SRC%.c}"                     # bo duoi .c de lay ten file thuc thi
[[ "$OUT" != */* ]] && OUT="./$OUT" # them ./ de khong tim trong PATH

gcc -std=c11 -Wall -Wextra -g "$SRC" -o "$OUT" -lm
"$OUT" "$@"
```

Cấp quyền chạy và sử dụng:

```bash
chmod +x run-c.sh
./run-c.sh hello.c
```

Muốn gọi được từ mọi thư mục, chép vào thư mục nằm trong PATH:

```bash
cp run-c.sh ~/.local/bin/run-c
chmod +x ~/.local/bin/run-c
run-c hello.c        # goi tu bat ky dau
```

**Windows** — file `run-c.bat`:

```bat
@echo off
REM Dung: run-c.bat hello.c

if "%~1"=="" (
    set SRC=main.c
) else (
    set SRC=%~1
)

if not exist "%SRC%" (
    echo Khong tim thay file %SRC%
    exit /b 1
)

gcc -std=c11 -Wall -Wextra -g "%SRC%" -o "%~n1.exe"
if errorlevel 1 exit /b 1

"%~n1.exe"
```

Sử dụng:

```bat
run-c.bat hello.c
```
