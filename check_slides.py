#!/usr/bin/env python3
"""Soát chất lượng outline JSON trước khi render."""
import json, glob, sys, re
from pathlib import Path

LIMITS = dict(max_slides=12, min_slides=4, max_bullets=6, max_bullet_words=18,
              max_code_lines=16, max_code_cols=84)

def check(f):
    errs, warns = [], []
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        return [f"JSON hỏng: {e}"], []
    for k in ("title", "course", "slides"):
        if not d.get(k): errs.append(f"thiếu trường '{k}'")
    sl = d.get("slides") or []
    if len(sl) > LIMITS["max_slides"]: warns.append(f"{len(sl)} slide (>{LIMITS['max_slides']})")
    if len(sl) < LIMITS["min_slides"]: warns.append(f"chỉ {len(sl)} slide")
    if sl and "ghi nhớ" not in (sl[-1].get("title") or "").lower():
        warns.append(f"slide cuối không phải 'Ghi nhớ': {sl[-1].get('title')!r}")
    for i, s in enumerate(sl, 1):
        if not s.get("title"): errs.append(f"slide {i}: thiếu title")
        if not s.get("bullets") and not s.get("code"):
            errs.append(f"slide {i}: rỗng, không bullets cũng không code")
        for b in (s.get("bullets") or []):
            w = len(re.sub(r"[*`]", "", b).split())
            if w > LIMITS["max_bullet_words"]:
                warns.append(f"slide {i}: bullet {w} từ — {b[:55]}...")
        if len(s.get("bullets") or []) > LIMITS["max_bullets"]:
            warns.append(f"slide {i}: {len(s['bullets'])} bullet")
        c = s.get("code")
        if c:
            lines = c.split("\n")
            if len(lines) > LIMITS["max_code_lines"]:
                warns.append(f"slide {i}: code {len(lines)} dòng")
            mx = max((len(l) for l in lines), default=0)
            if mx > LIMITS["max_code_cols"]:
                warns.append(f"slide {i}: code dòng dài {mx} ký tự")
    return errs, warns

def main():
    pats = sys.argv[1:] or ["slides-cpp", "slides-stl", "slides-ctdl"]
    tot = bad = 0
    for d in pats:
        files = sorted(glob.glob(f"{d}/*.json"))
        print(f"\n=== {d}: {len(files)} file")
        for f in files:
            tot += 1
            e, w = check(f)
            if e or w:
                print(f"  {Path(f).name}")
                for x in e: print(f"     LỖI  {x}"); 
                for x in w[:4]: print(f"     nhắc {x}")
                if e: bad += 1
    print(f"\nTổng {tot} file, {bad} file có lỗi chặn.")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
