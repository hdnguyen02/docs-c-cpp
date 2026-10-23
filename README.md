# Bài giảng — bản Markdown và PowerPoint

## Nội dung

| Thư mục | Nội dung |
|---|---|
| `md-cpp/` `md-stl/` `md-ctdl/` | **Bản Markdown đầy đủ**, giữ nguyên văn bài giảng, có ảnh, không có link video |
| `ppt-cpp/` `ppt-stl/` `ppt-ctdl/` | **Bản PowerPoint cô đọng**, mỗi bài một file, không chèn ảnh |
| `slides-cpp/` `slides-stl/` `slides-ctdl/` | Outline JSON trung gian, sửa ở đây rồi render lại |
| `images/` | Ảnh tải về, dùng cho bản Markdown |
| `_nhap/` | Script thu thập, bảng đối chiếu nguồn, file nháp. **Không đem đi cùng bản trình chiếu.** |

Mỗi thư mục `md-*` và `ppt-*` có `README.md` là mục lục theo chương.

## Ba khoá

| Khoá | Số bài | Slide |
|---|---|---|
| C Cơ Bản (thư mục `*-cpp`) | 59 | 482 |
| CTDL & Giải Thuật | 19 | 169 |
| STL C++ | 13 | 79 |

## Chạy lại

```bash
# soát chất lượng outline trước khi render
python3 check_slides.py

# render outline JSON thành pptx
python3 render_slides.py slides-cpp ppt-cpp "C Cơ Bản"
python3 render_slides.py slides-cpp ppt-cpp "C Cơ Bản" --merge   # gộp cả khoá thành 1 file

# tạo lại mục lục cho thư mục pptx
python3 make_index.py slides-cpp ppt-cpp md-cpp "C Cơ Bản"
```

## Sửa nội dung slide

Sửa file JSON trong `slides-*/` rồi chạy lại `render_slides.py`. Cấu trúc và quy tắc cô đọng ghi trong `SLIDE-SPEC.md`.
