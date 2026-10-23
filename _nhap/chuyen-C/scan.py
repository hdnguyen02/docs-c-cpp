import re
from pathlib import Path
pat = re.compile(r"iostream|\bcout\b|\bcin\b|std::|using namespace|bits/stdc|nullptr|vector<|```cpp|\bgetline\b|stringstream|\bnew int|delete\s*\[\]|#include <string>|#include <algorithm>|\.cpp\b|g\+\+")
files = sorted(Path("md-cpp").glob("[0-9]*.md")) + sorted(Path("md-cpp/solutions").glob("[0-9]*.md")) + sorted(Path("slides-cpp").glob("*.json"))
hits = 0
for f in files:
    for i, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        if pat.search(l):
            hits += 1; print(f"{f}:{i}: {l.strip()[:130]}")
print("TOTAL pattern hits", hits)
print("--- C++ mentions per file")
for f in files:
    n = f.read_text(encoding="utf-8").count("C++")
    if n: print(n, f)
print("--- 28tech mentions")
for f in files:
    n = f.read_text(encoding="utf-8").count("28tech")
    if n: print(n, f)
