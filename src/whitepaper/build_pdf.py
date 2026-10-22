#!/usr/bin/env python3
"""Build the Spec 031 whitepaper PDF ('Endorsed by Experts') in the Axiovex branding system.

Route: approved markdown -> branded HTML (title page + body) -> Chromium print-to-PDF
(same production method as the AI 101 handout) -> merge + stamp running header/footer
with PyMuPDF -> final PDF.
"""
import base64, re, sys
from pathlib import Path
import markdown
import pymupdf

BUILD = Path(__file__).resolve().parent / "build"
SRC_MD = Path(__file__).resolve().parent / "whitepaper.md"
LOGO_SVG = Path(__file__).resolve().parents[2] / "assets/axiovex-logo.svg"
OUT = BUILD / "endorsed-by-experts-prompt-injection.pdf"

# ---------- extract the paper body from the approved draft ----------
raw = SRC_MD.read_text(encoding="utf-8")
paper = raw.split("# Endorsed by Experts", 1)[1]
# body starts at the Executive summary; the header block goes to the title page
body_md = paper.split("## Executive summary", 1)[1]
body_md = "## Executive summary" + body_md

html_body = markdown.markdown(body_md, extensions=["extra", "sane_lists"])

# ---------- post-process ----------
html_body = html_body.replace("<blockquote>", '<blockquote class="exhibit">', 1)
html_body = html_body.replace("<li>[ ] ", '<li class="check"><span class="box"></span>')
# wrap the "What this paper does" block in a card
html_body = re.sub(
    r"(<p><strong>What this paper does</strong></p>\s*<ul>.*?</ul>)",
    r'<div class="does">\1</div>', html_body, flags=re.S)
html_body = html_body.replace(
    "<p>© 2026 Axiovex Systems, LLC. All rights reserved.</p>",
    '<p class="copyright-line">© 2026 Axiovex Systems, LLC. All rights reserved.</p>')
html_body = html_body.replace(
    "<p><em>The quoted payload is reproduced",
    '<p class="colophon"><em>The quoted payload is reproduced')
html_body = html_body.replace(
    "<p><strong>About Axiovex Systems</strong>",
    '<p class="about"><strong>About Axiovex Systems</strong>')

# ---------- logo: extract embedded PNG from the brand SVG ----------
svg = LOGO_SVG.read_text(encoding="utf-8")
b64 = re.search(r"data:image/png;base64,([A-Za-z0-9+/=]+)", svg).group(1)
logo_png = BUILD / "axiovex-logo-white.png"
logo_png.write_bytes(base64.b64decode(b64))

CSS_COMMON = """
@page { size: Letter; margin: 0; }
* { box-sizing: border-box; print-color-adjust: exact; -webkit-print-color-adjust: exact; }
:root { --navy:#081F32; --steel:#405B70; --cyan:#00DEF6; --near:#F7FCFF; --line:#B8D5DF; --pale:#EFF6FA; }
html, body { margin:0; padding:0; font-family:'Noto Sans','Liberation Sans',sans-serif; color:#22394E; }
"""

TITLE_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Endorsed by Experts — Axiovex Systems</title><style>
""" + CSS_COMMON + """
.titlepage { width:8.5in; height:11in; background:var(--navy); color:var(--near);
  padding:.62in .7in .55in; position:relative; overflow:hidden; }
.tp-top { display:flex; justify-content:space-between; align-items:flex-start; }
.kicker { font-size:9.5pt; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--cyan); padding-top:.1in; }
.tp-logo { width:2.05in; height:auto; }
.tp-rule { height:4px; background:var(--cyan); margin:.34in 0 .5in; }
.tp-type { font-size:10pt; font-weight:700; letter-spacing:1.4px; text-transform:uppercase; color:var(--cyan); margin:0 0 .12in; }
h1.tp-title { font-family:'Noto Serif','Liberation Serif',serif; font-weight:700; font-size:37pt;
  line-height:1.08; color:#FFFFFF; margin:0 0 .22in; }
.tp-sub { font-family:'Noto Serif','Liberation Serif',serif; font-size:15.5pt; line-height:1.4; color:var(--near); margin:0 0 .52in; max-width:6.4in; }
.tp-meta { border:1px solid rgba(184,213,223,.45); background:rgba(64,91,112,.28); padding:.24in .28in .1in; margin-bottom:.5in; }
.tp-meta .row { display:flex; gap:.22in; margin-bottom:.14in; }
.tp-meta .k { flex:0 0 1.92in; font-size:8.6pt; font-weight:700; letter-spacing:1.1px; text-transform:uppercase; color:var(--cyan); padding-top:2px; }
.tp-meta .v { font-size:10.6pt; line-height:1.42; color:var(--near); }
.tp-open { font-family:'Noto Serif','Liberation Serif',serif; font-style:italic; font-size:13pt; line-height:1.5; color:#FFFFFF; max-width:6.2in; }
.tp-foot { position:absolute; left:.7in; right:.7in; bottom:.5in; }
.tp-byline { font-size:10.5pt; color:var(--near); margin-bottom:.16in; }
.tp-byline b { color:#fff; }
.tp-strip { border-top:1px solid rgba(184,213,223,.45); padding-top:.13in; display:flex; justify-content:space-between; }
.tp-strip .l { font-size:7.8pt; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:var(--cyan); }
.tp-strip .r { font-size:8.2pt; color:var(--near); }
</style></head><body>
<div class="titlepage">
  <div class="tp-top">
    <div class="kicker">Axiovex Systems · Whitepaper</div>
    <img class="tp-logo" src="axiovex-logo-white.png" alt="Axiovex Systems">
  </div>
  <div class="tp-rule"></div>
  <p class="tp-type">Indirect prompt injection — authority capture</p>
  <h1 class="tp-title">Endorsed by Experts</h1>
  <p class="tp-sub">How a single sentence tried to become the only source — a real indirect prompt injection, caught during ordinary research</p>
  <div class="tp-meta">
    <div class="row"><div class="k">Where found</div><div class="v">A public Milvus &ldquo;AI quick-reference&rdquo; page, encountered in search results during technical research on 22 October 2026</div></div>
    <div class="row"><div class="k">Outcome</div><div class="v">Spotted, not followed, not used as a source, and disclosed in the research report itself</div></div>
    <div class="row"><div class="k">Risk if it had worked</div><div class="v">The research would have stopped checking other sources and treated one page as definitive — a wrong answer delivered with false confidence.</div></div>
  </div>
  <p class="tp-open">It did not shout. It did not contain code. It sounded helpful, even authoritative. That is exactly why it matters.</p>
  <div class="tp-foot">
    <div class="tp-byline"><b>Axiovex Systems, LLC</b> &nbsp;·&nbsp; 22 October 2026 &nbsp;·&nbsp; Public</div>
    <div class="tp-strip"><span class="l">Authority must be earned, never claimed</span><span class="r">© 2026 Axiovex Systems, LLC. All rights reserved.</span></div>
  </div>
</div>
</body></html>"""

BODY_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>Endorsed by Experts — Axiovex Systems</title><style>
""" + CSS_COMMON + """
@page { size: Letter; margin: 1.02in .72in .88in .72in; }
body { font-size:10.3pt; line-height:1.5; }
h2 { font-family:'Noto Serif','Liberation Serif',serif; font-weight:700; font-size:16.5pt; line-height:1.2;
  color:var(--navy); border-bottom:2.5px solid var(--cyan); padding-bottom:5px; margin:26px 0 11px; break-after:avoid; }
h2:first-child { margin-top:0; }
h3 { font-size:11.3pt; font-weight:700; color:var(--navy); margin:17px 0 6px; break-after:avoid; }
p { margin:0 0 9px; }
ul, ol { margin:2px 0 11px; padding-left:22px; }
li { margin-bottom:5px; }
strong { color:var(--navy); }
a { color:var(--steel); overflow-wrap:anywhere; }
blockquote.exhibit { margin:16px 0; background:var(--pale); border:1px solid var(--line);
  border-left:5px solid var(--cyan); padding:14px 18px 8px; break-inside:avoid; }
blockquote.exhibit h3 { margin:0 0 8px; font-size:9.3pt; letter-spacing:1.1px; text-transform:uppercase; color:var(--steel); }
blockquote.exhibit p:first-of-type { font-family:'Noto Serif','Liberation Serif',serif; font-style:italic;
  font-size:12.3pt; line-height:1.45; color:var(--navy); }
blockquote.exhibit p:last-child { font-size:8.8pt; color:var(--steel); }
.does { background:var(--pale); border:1px solid var(--line); padding:12px 16px 4px; margin:12px 0 14px; break-inside:avoid; }
.does p { margin-bottom:6px; }
.does ul { margin-bottom:8px; }
li.check { list-style:none; position:relative; }
li.check .box { position:absolute; left:-22px; top:3px; width:10px; height:10px; border:2px solid var(--cyan); background:#fff; }
hr { border:0; border-top:1px solid var(--line); margin:20px 0; }
.about { margin-top:14px; }
.colophon { font-size:9.3pt; color:var(--steel); }
.copyright-line { font-size:9.3pt; color:var(--steel); margin-top:10px; }
</style></head><body>
""" + html_body + """
</body></html>"""

(BUILD / "title.html").write_text(TITLE_HTML, encoding="utf-8")
(BUILD / "body.html").write_text(BODY_HTML, encoding="utf-8")

# ---------- render with Chromium via Playwright ----------
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    pg = browser.new_page()
    pg.goto((BUILD / "title.html").as_uri())
    pg.pdf(path=str(BUILD / "title.pdf"), prefer_css_page_size=True, print_background=True)
    pg.goto((BUILD / "body.html").as_uri())
    pg.pdf(path=str(BUILD / "body.pdf"), prefer_css_page_size=True, print_background=True)
    browser.close()

# ---------- merge + stamp running header/footer on body pages ----------
NAVY = (8/255, 31/255, 50/255); CYAN = (0, 222/255, 246/255)
NEAR = (247/255, 252/255, 1.0); STEEL = (64/255, 91/255, 112/255)
W, H = 612, 792  # Letter points

title = pymupdf.open(BUILD / "title.pdf")
body = pymupdf.open(BUILD / "body.pdf")
out = pymupdf.open()
out.insert_pdf(title)
first_body = out.page_count
out.insert_pdf(body)

f_bold = pymupdf.Font(fontfile="/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
f_reg = pymupdf.Font(fontfile="/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")
logo_img = logo_png.read_bytes()

def tw(page, text, x, y, font, size, color):
    w = pymupdf.TextWriter(page.rect)
    w.append((x, y), text, font=font, fontsize=size)
    w.write_text(page, color=color)

for i in range(first_body, out.page_count):
    page = out[i]
    # header band
    page.draw_rect(pymupdf.Rect(0, 0, W, 40), color=None, fill=NAVY)
    page.draw_rect(pymupdf.Rect(0, 40, W, 43), color=None, fill=CYAN)
    tw(page, "ENDORSED BY EXPERTS — AXIOVEX WHITEPAPER", 52, 26, f_bold, 7.6, CYAN)
    # logo right (white logo png, aspect 1557x443)
    page.insert_image(pymupdf.Rect(W-52-118, 9, W-52, 9+118*443/1557), stream=logo_img)
    # footer band
    page.draw_rect(pymupdf.Rect(0, H-34, W, H), color=None, fill=NAVY)
    tw(page, "AUTHORITY MUST BE EARNED, NEVER CLAIMED", 52, H-13, f_bold, 7.2, CYAN)
    ctext = "© 2026 Axiovex Systems, LLC. All rights reserved."
    tw_width = f_reg.text_length(ctext, fontsize=7.6)
    tw(page, ctext, W-52-tw_width, H-13, f_reg, 7.6, NEAR)
    ptext = f"{i+1} / {out.page_count}"
    pw_ = f_reg.text_length(ptext, fontsize=7.6)
    # page number sits just above footer band, right side, steel
    tw(page, ptext, W-52-pw_, H-44, f_reg, 7.6, STEEL)

out.set_metadata({
    "title": "Endorsed by Experts — How a single sentence tried to become the only source",
    "author": "Axiovex Systems, LLC",
    "subject": "A real indirect prompt injection (authority capture), caught during ordinary research — incident record, four documented cases, and a defence checklist.",
    "creator": "Axiovex Systems, LLC",
})
out.save(OUT, deflate=True)
print("pages:", out.page_count, "->", OUT)
