import json, re
from pathlib import Path
root = Path("/home/devnguyenho/Desktop/docs-cpp")
rows = [l.split("\t") for l in (root/"_nhap/chuyen-C/mapping.tsv").read_text(encoding="utf-8").splitlines()[1:] if l.strip()]
M = {r[0]: (r[1], r[2]) for r in rows}
chapters = ["Làm Quen Với Ngôn Ngữ C", "[C]. Kiểu Dữ Liệu - Toán Tử - Nhập Xuất", "[C]. Cấu Trúc Rẽ Nhánh",
  "[C]. Vòng Lặp", "[C]. Hàm Và Đệ Quy", "[C]. Mảng 1 Chiều", "[C]. Lý Thuyết Con Trỏ", "[C]. Mảng 2 Chiều",
  "[C]. Chuỗi Ký Tự", "[C]. Sắp Xếp Và Tìm Kiếm"]
toc = [{"chapter": c, "items": []} for c in chapters]
for old, (new, title) in M.items():
    toc[int(new[:2]) - 1]["items"].append([new[6:], title])
(root/"md-cpp/toc.json").write_text(json.dumps(toc, ensure_ascii=False, indent=2), encoding="utf-8")

L = ["# Mục lục — Khoá C Cơ Bản (codelab)", "",
     "> 🎯 Mỗi bài học đều có mục **BÀI TẬP** gồm **15 bài** ở cuối trang.",
     "> 📘 Lời giải tham khảo nằm trong thư mục [solutions/](solutions/README.md) — tổng cộng **885 bài giải** có code C chạy được kèm giải thích.", ""]
for i, ch in enumerate(toc, 1):
    L += [f"## {i}. {ch['chapter']}", ""]
    for slug, t in ch["items"]:
        stem = next(n for n, tt in M.values() if n.endswith(slug) and tt == t)
        L.append(f"- [{t}]({stem}.md)")
    L.append("")
(root/"md-cpp/README.md").write_text("\n".join(L), encoding="utf-8")

# solutions README: đổi header + mục lục + link; giữ bảng cuối (soát tay sau)
s = (root/"md-cpp/solutions/README.md").read_text(encoding="utf-8")
for old, (new, title) in sorted(M.items(), key=lambda x: -len(x[0])):
    s = s.replace(old + ".md", new + ".md")
def fix_line(m):
    stem = m.group(2)
    t = next(tt for n, tt in M.values() if n == stem)
    return f"- [{t}]({stem}.md)"
s = re.sub(r"^- \[(.+?)\]\(([0-9][^)]*?)\.md\)", fix_line, s, flags=re.M)
s = s.replace("Khoá C++ Cơ Bản", "Khoá C Cơ Bản").replace("code C++", "code C").replace("Làm quen với C++", "Làm quen với C")
s = s.replace("g++ -std=c++17 -Wall -Wextra -g main.cpp -o main", "gcc -std=c11 -Wall -Wextra -g main.c -o main -lm")
s = s.replace("`.cpp`", "`.c`").replace(" / `.cpp`", " / `.c`").replace("comparator cho `sort`", "hàm so sánh cho `qsort`")
(root/"md-cpp/solutions/README.md").write_text(s, encoding="utf-8")
print("ok")
