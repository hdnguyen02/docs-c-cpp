#!/usr/bin/env python3
"""Tạo README.md liệt kê các file pptx theo chương, đọc thứ tự từ toc.json của khoá."""
import json, sys, glob
from pathlib import Path

def main(slidedir, pptdir, mddir, course):
    root = Path(__file__).parent
    toc = json.load(open(root / mddir / "toc.json", encoding="utf-8"))
    order = {}
    for ci, ch in enumerate(toc, 1):
        for li, (slug, t) in enumerate(ch["items"], 1):
            order[f"{ci:02d}-{li:02d}"] = (ch["chapter"], t)
    lines = [f"# {course} — bản slide (.pptx)", "",
             "Mỗi bài là một file PowerPoint cô đọng, không chèn ảnh.", ""]
    cur = None; n = 0
    for f in sorted(glob.glob(str(root / pptdir / "*.pptx"))):
        name = Path(f).name
        if name.endswith("-full.pptx"): continue
        key = name[:5]
        chap, title = order.get(key, ("Khác", Path(f).stem))
        if chap != cur:
            cur = chap; lines += [f"## {chap}", ""]
        lines.append(f"- [{title}]({name})"); n += 1
        if False: pass
    lines += ["", f"Tổng {n} bài."]
    (root / pptdir / "README.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"{pptdir}/README.md: {n} bài")

if __name__ == "__main__":
    main(*sys.argv[1:])
