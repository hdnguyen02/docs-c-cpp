#!/usr/bin/env python3
"""Render outline JSON (đã cô đọng) -> PowerPoint.

JSON mỗi bài:
{
  "title": "Vòng Lặp For",
  "course": "C++ Cơ Bản",
  "slides": [
    {"title": "...", "bullets": ["..."], "code": "...", "caption": "..."},
    ...
  ]
}
Quy tắc: bullets <= 5, mỗi bullet <= ~14 từ, code <= 14 dòng.
Layout tự chọn: chỉ bullet | bullet + code dưới | 2 cột bullet|code | chỉ code.
"""
import json, sys, glob, math, re
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE

W, H = Inches(13.333), Inches(7.5)
NAVY   = RGBColor(0x14, 0x2B, 0x45)
BLUE   = RGBColor(0x35, 0x98, 0xDB)
INK    = RGBColor(0x22, 0x2B, 0x38)
GREY   = RGBColor(0x76, 0x7F, 0x8C)
WHITE  = RGBColor(0xFF, 0xFF, 0xFF)
CODEBG = RGBColor(0x18, 0x22, 0x33)
CODEFG = RGBColor(0xE8, 0xEF, 0xF7)
FONT, MONO = "Calibri", "Consolas"

MARGIN   = Inches(0.78)
TOP_IN   = 1.62
BOT_IN   = 6.95
BODY_W   = W - MARGIN * 2
def IN(v): return Emu(int(v * 914400))

def rect(s, l, t, w, h, fill):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, l, t, w, h)
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    sh.line.fill.background(); sh.shadow.inherit = False
    return sh

def tbox(s, l, t, w, h, wrap=True):
    tb = s.shapes.add_textbox(l, t, w, h)
    tf = tb.text_frame
    tf.word_wrap = wrap
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    return tf

def run(p, text, size, color, bold=False, mono=False):
    r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.color.rgb = color
    r.font.name = MONO if mono else FONT
    r.font.bold = bold
    return r

def rich(p, text, size, color, bold=False):
    """**đậm** và `code` inline."""
    for part in re.split(r"(\*\*.+?\*\*|`[^`]+`)", text):
        if not part: continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            run(p, part[2:-2].replace("`", ""), size, color, bold=True)
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            r = run(p, part[1:-1], size * 0.95, BLUE, mono=True)
            if bold: r.font.bold = True
        else:
            run(p, part, size, color, bold=bold)

def code_font(code, box_w_in, max_h_in):
    lines = code.split("\n")
    n, mx = len(lines), max((len(l) for l in lines), default=0)
    fs = 16.0
    while fs > 8.5:
        if mx * fs * 0.60 / 72 <= box_w_in - 0.44 and n * fs * 1.42 / 72 <= max_h_in - 0.34:
            break
        fs -= 0.5
    return fs

def draw_code(s, code, l, t, w, h):
    fs = code_font(code, w / 914400, h / 914400)
    rect(s, l, t, w, h, CODEBG)
    tf = tbox(s, l + Inches(0.22), t + Inches(0.16), w - Inches(0.44), h - Inches(0.32), wrap=True)
    for i, ln in enumerate(code.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT; p.space_after = Pt(0); p.line_spacing = 1.0
        run(p, ln if ln.strip() else " ", fs, CODEFG, mono=True)

CPL_AT = {20: 78, 19: 82, 18: 87, 17: 92, 16: 98, 15: 104}

def bullet_size(bullets):
    n = len(bullets); longest = max((len(b) for b in bullets), default=0)
    if n <= 3 and longest <= 72: return 20
    if n <= 4 and longest <= 88: return 18
    if n <= 5: return 17
    return 16

def bullets_height(bullets, size):
    cpl = CPL_AT.get(int(size), 92)
    lh = size * 1.30 / 72
    gap = 0.20 if len(bullets) <= 4 else 0.13
    h = 0.0
    for b in bullets:
        plain = re.sub(r"[*`]", "", b)
        h += max(1, math.ceil(len(plain) / cpl)) * lh + gap
    return h

def draw_bullets(s, bullets, l, t, w, h, size=None):
    if size is None: size = bullet_size(bullets)
    tf = tbox(s, l, t, w, h)
    ind = int(Inches(0.34))
    for i, b in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(13 if len(bullets) <= 4 else 8)
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", str(ind)); pPr.set("indent", str(-ind))
        run(p, "▪   ", size, BLUE, bold=True)
        rich(p, b, size, INK)

def head(prs, title, kicker):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, WHITE)
    rect(s, MARGIN, Inches(0.66), Inches(0.09), Inches(0.56), BLUE)
    tf = tbox(s, MARGIN + Inches(0.26), Inches(0.54), W - MARGIN * 2 - Inches(0.3), Inches(0.82))
    p = tf.paragraphs[0]; rich(p, title, 27, NAVY, bold=True)
    kf = tbox(s, MARGIN, Inches(0.15), W - MARGIN * 2, Inches(0.3))
    kp = kf.paragraphs[0]; kp.alignment = PP_ALIGN.RIGHT
    run(kp, kicker, 10.5, GREY)
    return s

def title_slide(prs, title, subtitle, foot=""):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, NAVY)
    rect(s, 0, H - Inches(0.15), W, Inches(0.15), BLUE)
    rect(s, Inches(1.1), Inches(2.55), Inches(0.1), Inches(0.62), BLUE)
    tf = tbox(s, Inches(1.4), Inches(2.4), Inches(10.6), Inches(2.6))
    p = tf.paragraphs[0]; run(p, title, 40, WHITE, bold=True)
    p2 = tf.add_paragraph(); p2.space_before = Pt(14)
    run(p2, subtitle, 18, BLUE)
    if foot:
        p3 = tf.add_paragraph(); p3.space_before = Pt(26)
        run(p3, foot, 11, RGBColor(0x92, 0x9F, 0xB2))
    return s

def section_slide(prs, text, kicker):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    rect(s, 0, 0, W, H, NAVY)
    rect(s, MARGIN, Inches(3.3), Inches(0.1), Inches(0.75), BLUE)
    tf = tbox(s, MARGIN + Inches(0.3), Inches(3.2), W - MARGIN * 2, Inches(1.2))
    rich(tf.paragraphs[0], text, 30, WHITE, bold=True)
    kf = tbox(s, MARGIN, Inches(0.15), W - MARGIN * 2, Inches(0.3))
    kp = kf.paragraphs[0]; kp.alignment = PP_ALIGN.RIGHT
    run(kp, kicker, 10.5, RGBColor(0x8C, 0x9A, 0xAF))
    return s

def content_slide(prs, sl, kicker):
    if sl.get("type") == "section":
        return section_slide(prs, sl["title"], kicker)
    s = head(prs, sl["title"], kicker)
    bullets = sl.get("bullets") or []
    code = (sl.get("code") or "").rstrip()
    cap = sl.get("caption")
    y = TOP_IN
    if cap:
        tf = tbox(s, MARGIN, IN(y), BODY_W, Inches(0.4))
        rich(tf.paragraphs[0], cap, 15, GREY)
        y += 0.42
    avail = BOT_IN - y

    bsize = bullet_size(bullets) if bullets else 0
    bh = bullets_height(bullets, bsize) if bullets else 0.0
    ch = 0.0
    if code:
        fs = code_font(code, BODY_W / 914400, avail - bh - 0.25)
        ch = len(code.split("\n")) * fs * 1.42 / 72 + 0.40
    total = bh + ch + (0.25 if (bullets and code) else 0)
    if total < avail:                      # cân khối nội dung theo chiều dọc
        y += min((avail - total) * 0.35, 0.8)
    if bullets:
        draw_bullets(s, bullets, MARGIN, IN(y), BODY_W, IN(bh + 0.2), size=bsize)
        y += bh + 0.25
    if code:
        draw_code(s, code, MARGIN, IN(y), BODY_W, IN(min(ch, BOT_IN - y)))
    return s

def build(prs, data, kicker_prefix=""):
    title = data["title"]; course = data.get("course", "")
    title_slide(prs, title, course, data.get("source", ""))
    kicker = f"{kicker_prefix}{title}"
    for sl in data["slides"]:
        content_slide(prs, sl, kicker)

def main():
    a = sys.argv[1:]
    merge = "--merge" in a; a = [x for x in a if x != "--merge"]
    srcdir, outdir = a[0], a[1]
    course = a[2] if len(a) > 2 else ""
    root = Path(__file__).parent
    files = sorted(glob.glob(str(root / srcdir / "*.json")))
    out = root / outdir; out.mkdir(exist_ok=True)
    if merge:
        prs = Presentation(); prs.slide_width, prs.slide_height = W, H
        title_slide(prs, course, "Trọn bộ bài giảng", "")
        for i, f in enumerate(files, 1):
            build_inner = json.load(open(f, encoding="utf-8"))
            kicker = f"Bài {i} · {build_inner['title']}"
            section_slide(prs, f"Bài {i}. {build_inner['title']}", course)
            for sl in build_inner["slides"]:
                content_slide(prs, sl, kicker)
            print(f"  + {Path(f).stem}")
        dest = out / f"{outdir}-full.pptx"; prs.save(dest)
        print(f"\n{dest.name}: {len(prs.slides._sldIdLst)} slide")
    else:
        tot = 0
        for f in files:
            data = json.load(open(f, encoding="utf-8"))
            prs = Presentation(); prs.slide_width, prs.slide_height = W, H
            build(prs, data)
            n = len(prs.slides._sldIdLst); tot += n
            dest = out / (Path(f).stem + ".pptx"); prs.save(dest)
            print(f"  ok {dest.name}  ({n} slide)")
        print(f"\n{len(files)} file pptx, {tot} slide -> {out}")

if __name__ == "__main__":
    main()
