import re
from pathlib import Path
rows=[l.split("\t") for l in Path("_nhap/chuyen-C/mapping.tsv").read_text().splitlines()[1:] if l.strip()]
M={r[0]:r[1] for r in rows if r[0]!=r[1]}
files=list(Path("md-cpp").glob("*.md"))+list(Path("md-cpp/solutions").glob("*.md"))
fixed=0
for f in files:
    s=f.read_text(encoding="utf-8"); o=s
    for old,new in sorted(M.items(), key=lambda x:-len(x[0])):
        s=re.sub(re.escape(old)+r"(?=\.md)", new, s)
    if s!=o: f.write_text(s,encoding="utf-8"); fixed+=1; print("fixed", f)
bad=0
for f in files:
    for m in re.finditer(r"\]\(([^)#\s]+)(#[^)]*)?\)", f.read_text(encoding="utf-8")):
        t=m.group(1)
        if t.startswith("http"): continue
        if not (f.parent/t).exists(): bad+=1; print("BROKEN", f, t)
print("files fixed", fixed, "broken", bad)
