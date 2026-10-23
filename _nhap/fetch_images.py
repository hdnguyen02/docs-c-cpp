#!/usr/bin/env python3
"""Tải ảnh trong các file md về thư mục images/ và đổi link md sang đường dẫn local."""
import re, glob, hashlib, urllib.request, urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent
IMG = ROOT / "images"; IMG.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}

def grab(url):
    ext = Path(urllib.parse.urlparse(url).path).suffix.lower() or ".png"
    if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp"): ext = ".png"
    name = hashlib.md5(url.encode()).hexdigest()[:16] + ext
    dest = IMG / name
    if dest.exists(): return name, "cache"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r: data = r.read()
    dest.write_bytes(data)
    return name, f"{len(data)//1024}KB"

ok = fail = 0
for f in sorted(glob.glob(str(ROOT / "md-*/*.md"))):
    s = open(f, encoding="utf-8").read(); orig = s
    for url in set(re.findall(r"!\[\]\((https?://.+)\)", s)):
        try:
            name, info = grab(url); ok += 1
            s = s.replace(f"![]({url})", f"![](../images/{name})")
            print(f"  ok {name} {info}")
        except Exception as e:
            fail += 1; print(f"  ERR {e} <- {url}")
            if "404" in str(e):
                s = re.sub(r"!\[\]\(" + re.escape(url) + r"\)\n?", "", s); print("     -> gỡ ảnh chết khỏi md")
    if s != orig: open(f, "w", encoding="utf-8").write(s)
print(f"\nẢnh: {ok} ok, {fail} lỗi -> {IMG}")
