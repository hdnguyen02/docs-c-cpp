#!/usr/bin/env python3
"""Cào bài giảng blog.28tech.com.vn theo thứ tự nút "Bài tiếp" (menu #categoryTopic) -> Markdown."""
import re, sys, json, time, html as H, urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://blog.28tech.com.vn/"
OUT = Path(__file__).parent / "md"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"}

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "ignore")

# ---------- TOC ----------
def parse_toc(src):
    i = src.find('id="categoryTopic"'); menu = src[i:src.find('id="categoryTopicOverlay"', i)]
    chapters = []
    for ch in re.finditer(r'<a class="inner-title">(.*?)</a>\s*<ul>(.*?)</ul>', menu, re.S):
        items = [(u, H.unescape(re.sub(r"<[^>]+>", "", t)).strip())
                 for u, t in re.findall(r'<li data-url="([^"]+)">\s*<a[^>]*>(.*?)</a>', ch.group(2), re.S)]
        chapters.append({"chapter": H.unescape(ch.group(1)).strip(), "items": items})
    return chapters

# ---------- HTML -> Markdown ----------
def slice_div(src, cls):
    i = src.find(f'class="{cls}"')
    if i < 0: return ""
    start = src.rfind("<", 0, i); depth = 0
    for m in re.finditer(r"<(/?)div\b[^>]*>", src[start:]):
        depth += -1 if m.group(1) else 1
        if depth == 0: return src[start:start + m.end()]
    return ""

class MD(HTMLParser):
    BLOCK = {"p","div","h1","h2","h3","h4","h5","h6","ul","ol","li","pre","blockquote","table","tr","br","hr"}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.stack = []; self.list = []; self.pre = 0; self.href = None; self.row = None
    def txt(self, s):
        if self.pre: self.out.append(s); return
        s = re.sub(r"\s+", " ", s)
        if s.strip() or (self.out and not self.out[-1].endswith("\n")): self.out.append(s)
    def nl(self, n=1):
        cur = "".join(self.out[-3:])
        need = n - (len(cur) - len(cur.rstrip("\n")))
        if need > 0: self.out.append("\n" * need)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); self.stack.append(tag)
        if tag in ("h1","h2","h3","h4","h5","h6"): self.nl(2); self.out.append("#" * int(tag[1]) + " ")
        elif tag == "p": self.nl(2)
        elif tag == "br": self.out.append("\n")
        elif tag in ("ul","ol"): self.nl(1 if self.list else 2); self.list.append([tag, 0])
        elif tag == "li":
            self.nl(1)
            if self.list:
                self.list[-1][1] += 1; ind = "  " * (len(self.list) - 1)
                self.out.append(ind + (f"{self.list[-1][1]}. " if self.list[-1][0] == "ol" else "- "))
            else: self.out.append("- ")
        elif tag == "pre":
            lang = re.sub(r"^language-", "", (a.get("class") or "").split()[0]) if a.get("class") else "cpp"
            lang = {"c": "cpp", "": "cpp"}.get(lang, lang)
            self.nl(2); self.out.append(f"```{lang}\n"); self.pre += 1
        elif tag == "code" and not self.pre: self.out.append("`")
        elif tag in ("b","strong"): self.out.append("**")
        elif tag in ("i","em"): self.out.append("*")
        elif tag == "blockquote": self.nl(2); self.out.append("> ")
        elif tag == "hr": self.nl(2); self.out.append("---"); self.nl(2)
        elif tag == "a":
            self.href = a.get("href"); 
            if self.href and self.href.startswith("/"): self.href = BASE.rstrip("/") + self.href
            elif self.href and not re.match(r"https?://|#|mailto:", self.href): self.href = BASE + self.href
            if a.get("title") == "image" and self.href:
                u = self.href.replace("(", "%28").replace(")", "%29")
                self.nl(2); self.out.append(f"![]({u})"); self.nl(2); self.href = "IMG"; return
            if a.get("title") == "video" and a.get("data-mce-href"):
                self.href = "IMG"; return  # bỏ video, không lấy
            self.out.append("[")
        elif tag == "img":
            s = a.get("data-src") or a.get("src") or ""
            if s.startswith("/"): s = BASE.rstrip("/") + s
            if s and not s.startswith("data:"): self.nl(2); self.out.append(f"![{a.get('alt','')}]({s})"); self.nl(2)
        elif tag == "iframe":
            src = a.get("src") or a.get("data-src") or ""
            pass  # bỏ video, không lấy
        elif tag == "table": self.nl(2); self.row = []
        elif tag == "tr": self.row = []
        elif tag in ("td","th"): self.out.append("| ")
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag: self.stack.pop()
        if tag in ("h1","h2","h3","h4","h5","h6","p","blockquote"): self.nl(2)
        elif tag in ("ul","ol"):
            if self.list: self.list.pop()
            self.nl(1 if self.list else 2)
        elif tag == "li": self.nl(1)
        elif tag == "pre":
            self.pre -= 1
            s = "".join(self.out).rstrip("\n"); self.out = [s, "\n```\n\n"]
        elif tag == "code" and not self.pre: self.out.append("`")
        elif tag in ("b","strong"): self.out.append("**")
        elif tag in ("i","em"): self.out.append("*")
        elif tag == "a":
            if self.href == "IMG": pass
            elif self.href and not self.href.startswith("#"): self.out.append(f"]({self.href})")
            else:
                # bỏ ngoặc mở nếu không có link
                s = "".join(self.out); k = s.rfind("["); self.out = [s[:k] + s[k+1:]]
            self.href = None
        elif tag in ("td","th"): self.out.append(" ")
        elif tag == "tr": self.out.append("|\n")
        elif tag == "table": self.nl(2)
    def handle_data(self, d):
        if self.stack and self.stack[-1] in ("script","style"): return
        if self.href == "IMG": return
        self.txt(d)
    def result(self):
        s = "".join(self.out)
        s = s.replace("﻿", "").replace("\xa0", " ")
        s = re.sub(r"\*\*\*\*", "", s); s = re.sub(r"^\*\*\s*$\n?", "", s, flags=re.M); s = re.sub(r"(?<!\*)\*\*[ \t]+\*\*(?!\*)", " ", s); s = re.sub(r"[ \t]+\n", "\n", s); s = re.sub(r"\n{3,}", "\n\n", s)
        # fix bold sát chữ: "** abc **" -> "**abc**"
        s = re.sub(r"\*\*([ \t]+)([^*\n]*?)\*\*", r"\1**\2**", s)
        s = re.sub(r"\*\*([^*\n]*?)([ \t]+)\*\*", r"**\1**\2", s)
        s = re.sub(r"(\S)\*\*(\w)", lambda m: m.group(0) if m.group(1) == "*" else m.group(1) + "** " + m.group(2), s)
        s = re.sub(r"(\w)\*\*(\w)", r"\1 **\2", s)
        return s.strip() + "\n"

def to_md(fragment):
    p = MD(); p.feed(fragment); p.close(); return p.result()

def article_md(src, url):
    title = H.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", src, re.S).group(1))).strip()
    desc = to_md(slice_div(src, "article-description")).strip()
    body = to_md(slice_div(src, "article-content"))
    parts = [f"# {title}", "", f"> Nguồn: {url}", ""]
    if desc: parts += [desc, ""]
    parts += [body]
    return title, "\n".join(parts)

def safe(s): return re.sub(r"[^\w\- ]", "", s).strip().replace(" ", "-")[:80]

def main(limit=None, start="c-vi-sao-nen-hoc-lap-trinh-c", only=None, out=None, course="Khoá C++ 28Tech"):
    global OUT
    if out: OUT = Path(__file__).parent / out
    OUT.mkdir(exist_ok=True)
    toc = parse_toc(fetch(BASE + start))
    json.dump(toc, open(OUT / "toc.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    index = [f"# Mục lục — {course} (28Tech)", ""]; n = 0; fails = []
    for ci, ch in enumerate(toc, 1):
        index += [f"## {ci}. {ch['chapter']}", ""]
        for li, (slug, title) in enumerate(ch["items"], 1):
            if only and slug not in only: continue
            if limit and n >= limit: break
            n += 1
            fname = f"{ci:02d}-{li:02d}-{safe(slug)}.md"
            try:
                src = fetch(BASE + slug); t, md = article_md(src, BASE + slug)
                (OUT / fname).write_text(md, encoding="utf-8")
                print(f"[{n:3}] ok  {fname}  ({len(md)} chars)"); index.append(f"- [{t}]({fname})")
                time.sleep(0.8)
            except Exception as e:
                fails.append((slug, str(e))); print(f"[{n:3}] ERR {slug}: {e}"); index.append(f"- ~~{title}~~ (lỗi: {e})")
        index.append("")
        if limit and n >= limit: break
    (OUT / "README.md").write_text("\n".join(index), encoding="utf-8")
    print(f"\nDone: {n - len(fails)} ok, {len(fails)} lỗi, output -> {OUT}")
    for f in fails: print("  FAIL", f)

if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--only": main(only=set(args[1:]))
    elif args and args[0] == "--course": main(start=args[1], out=args[2], course=args[3])  # --course <slug bất kỳ trong khoá> <thư mục> <tên khoá>
    elif args and args[0] == "--toc":
        for ch in parse_toc(fetch(BASE + args[1])): print(f"{len(ch['items']):3}  {ch['chapter']}")
    else: main(limit=int(args[0]) if args else None)
