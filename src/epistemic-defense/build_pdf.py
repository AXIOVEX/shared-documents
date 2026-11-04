#!/usr/bin/env python3
"""Build the 'Prompt Injection Is an Epistemic Attack' whitepaper PDF in the
Axiovex branding system (the standard document template).

Route: paper.md (the canonical text, unchanged) -> branded HTML (title page +
body) -> Chromium print-to-PDF (the same production route as the AI 101
handout and the 'Endorsed by Experts' whitepaper in src/whitepaper/) -> merge +
stamp running header/footer with PyMuPDF -> final PDF.

Earlier issues of this paper (through the 2026-11-04 attribution re-issue)
were built from the same paper.md with pandoc/LuaLaTeX and carried no
branding. This build changes the typesetting only; the text is paper.md
verbatim, and the build is verified against the previous issue by a
pdftotext comparison before republication.

Run with the Playwright venv python:
    ~/workspace/venvs/playwright/bin/python build_pdf.py
Writes build/prompt-injection-epistemic-attack.pdf; copy it over
../../docs/prompt-injection-epistemic-attack.pdf to republish (the filename
is a stable published address and does not change).
"""
import base64, re
from pathlib import Path
import markdown
import pymupdf

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
BUILD.mkdir(exist_ok=True)
SRC_MD = HERE / "paper.md"
LOGO_SVG = HERE.parents[1] / "assets/axiovex-logo.svg"
OUT = BUILD / "prompt-injection-epistemic-attack.pdf"

TITLE = ("Prompt Injection Is an Epistemic Attack: Provenance, Claim "
         "Grading, and Layered Defense for AI Agents")
SHORT_TITLE = "Prompt Injection Is an Epistemic Attack"
AUTHOR = "Axiovex Systems"
DATE_LINE = "29 October 2026"

# ---------- paper body from the canonical markdown ----------
raw = SRC_MD.read_text(encoding="utf-8")
# strip the YAML front matter (title/author/date live on the title page)
body_md = re.sub(r"\A---\n.*?\n---\n", "", raw, flags=re.S)
assert body_md.lstrip().startswith("# Abstract"), "unexpected paper.md shape"

html_body = markdown.markdown(
    body_md, extensions=["extra", "sane_lists", "smarty"])

# wrap the abstract in a branded card
html_body = re.sub(
    r"(<h1>Abstract</h1>)(.*?)(?=<h1>)",
    lambda m: m.group(1) + '<div class="abstract">' + m.group(2) + "</div>",
    html_body, count=1, flags=re.S)
assert '<div class="abstract">' in html_body, "abstract wrap failed"

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
<title>""" + TITLE + """ — Axiovex Systems</title><style>
""" + CSS_COMMON + """
.titlepage { width:8.5in; height:11in; background:var(--navy); color:var(--near);
  padding:.62in .7in .55in; position:relative; overflow:hidden; }
.tp-top { display:flex; justify-content:space-between; align-items:flex-start; }
.kicker { font-size:9.5pt; font-weight:700; letter-spacing:1.6px; text-transform:uppercase; color:var(--cyan); padding-top:.1in; }
.tp-logo { width:2.05in; height:auto; }
.tp-rule { height:4px; background:var(--cyan); margin:.34in 0 .46in; }
.tp-type { font-size:10pt; font-weight:700; letter-spacing:1.4px; text-transform:uppercase; color:var(--cyan); margin:0 0 .14in; }
h1.tp-title { font-family:'Noto Serif','Liberation Serif',serif; font-weight:700; font-size:26.5pt;
  line-height:1.14; color:#FFFFFF; margin:0 0 .24in; }
.tp-sub { font-family:'Noto Serif','Liberation Serif',serif; font-size:14.5pt; line-height:1.42; color:var(--near); margin:0 0 .46in; max-width:6.5in; }
.tp-meta { border:1px solid rgba(184,213,223,.45); background:rgba(64,91,112,.28); padding:.24in .28in .1in; margin-bottom:.46in; }
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
  <p class="tp-type">AI agent security — authority, provenance, evidence</p>
  <h1 class="tp-title">Prompt Injection Is an Epistemic Attack: Provenance, Claim Grading, and Layered Defense for AI Agents</h1>
  <p class="tp-sub">A prompt injection does not primarily corrupt text. It corrupts what an agent believes about who instructed it and what its principal intends.</p>
  <div class="tp-meta">
    <div class="row"><div class="k">The battery</div><div class="v">56 planted instructions and 50 legitimate controls. The epistemic layer challenged 55 of 56 with no false challenges; a structural screen alone challenged 32 of 56 and falsely challenged 12% of controls.</div></div>
    <div class="row"><div class="k">The red team</div><div class="v">47 new attack phrasings the battery had never tried. After hardening aimed at the failure reasons: 45 of 47 challenged at the decision layer, and 23 of 25 on a sealed held-out set.</div></div>
    <div class="row"><div class="k">The tuning experiment</div><div class="v">A tuned small model challenged 27 of 56 plants (base model: 0 of 56) — and falsely challenged 16 of 28 legitimate controls. Tuning helps, over-flags, and is not sufficient alone.</div></div>
  </div>
  <p class="tp-open">It is, in that precise sense, an epistemic attack — an attack on the agent&rsquo;s evidence about authority.</p>
  <div class="tp-foot">
    <div class="tp-byline"><b>Axiovex Systems, LLC</b> &nbsp;·&nbsp; 29 October 2026 &nbsp;·&nbsp; Public</div>
    <div class="tp-strip"><span class="l">Landing is not damage</span><span class="r">© 2026 Axiovex Systems, LLC. All rights reserved.</span></div>
  </div>
</div>
</body></html>"""

BODY_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>""" + TITLE + """ — Axiovex Systems</title><style>
""" + CSS_COMMON + """
@page { size: Letter; margin: 1.02in .72in .88in .72in; }
body { font-size:10.3pt; line-height:1.5; }
h1 { font-family:'Noto Serif','Liberation Serif',serif; font-weight:700; font-size:16.5pt; line-height:1.2;
  color:var(--navy); border-bottom:2.5px solid var(--cyan); padding-bottom:5px; margin:26px 0 11px; break-after:avoid; }
h1:first-child { margin-top:0; }
h2 { font-family:'Noto Serif','Liberation Serif',serif; font-weight:700; font-size:12.8pt; line-height:1.25;
  color:var(--navy); margin:19px 0 7px; break-after:avoid; }
p { margin:0 0 9px; }
ul, ol { margin:2px 0 11px; padding-left:22px; }
li { margin-bottom:5px; }
strong { color:var(--navy); }
a { color:var(--steel); overflow-wrap:anywhere; }
code { font-family:'Noto Sans Mono','Liberation Mono',monospace; font-size:9.4pt; color:var(--steel); }
.abstract { background:var(--pale); border:1px solid var(--line); border-left:5px solid var(--cyan);
  padding:14px 18px 6px; margin:0 0 6px; }
.abstract p:last-child { margin-bottom:8px; }
hr { border:0; border-top:1px solid var(--line); margin:20px 0; }
</style></head><body>
""" + html_body + """
</body></html>"""

(BUILD / "title.html").write_text(TITLE_HTML, encoding="utf-8")
(BUILD / "body.html").write_text(BODY_HTML, encoding="utf-8")

# ---------- combine into ONE document and print once ----------
# Merging two separately printed PDFs (PyMuPDF insert_pdf) drops the PDF
# structure tree, so the tagged output is lost. Printing the title page and
# the body as a single HTML document — the title on a named zero-margin
# page — keeps one structure tree end to end.
import re as _re
def _style(doc):
    return _re.search(r"<style>(.*?)</style>", doc, flags=_re.S).group(1)
def _body(doc):
    return _re.search(r"<body>(.*?)</body>", doc, flags=_re.S).group(1)

COMBINED_HTML = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>""" + TITLE + """ — Axiovex Systems</title><style>
""" + _style(TITLE_HTML) + "\n" + _style(BODY_HTML) + """
@page title { size: Letter; margin: 0; }
.titlepage { page: title; break-after: page; }
</style></head><body>
""" + _body(TITLE_HTML) + "\n" + html_body + """
</body></html>"""
(BUILD / "combined.html").write_text(COMBINED_HTML, encoding="utf-8")

# ---------- render with Chromium via Playwright ----------
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    browser = pw.chromium.launch()
    pg = browser.new_page()
    pg.goto((BUILD / "combined.html").as_uri())
    pg.evaluate("document.fonts.ready.then(() => true)")
    pg.pdf(path=str(BUILD / "combined.pdf"), prefer_css_page_size=True,
           print_background=True, tagged=True)
    browser.close()

# ---------- stamp running header/footer on body pages ----------
# Header band follows the 'Endorsed by Experts' whitepaper; the footer
# carries the document lockup bottom-left and "Page N of M" bottom-right
# (the pattern set by the VEXA whitepaper revision), with the © line in
# the footer band.
NAVY = (8/255, 31/255, 50/255); CYAN = (0, 222/255, 246/255)
NEAR = (247/255, 252/255, 1.0); STEEL = (64/255, 91/255, 112/255)
W, H = 612, 792  # Letter points

out = pymupdf.open(BUILD / "combined.pdf")
first_body = 1  # page 0 is the title page

f_bold = pymupdf.Font(fontfile="/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf")
f_reg = pymupdf.Font(fontfile="/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf")
logo_img = logo_png.read_bytes()

def tw(page, text, x, y, font, size, color):
    w = pymupdf.TextWriter(page.rect)
    w.append((x, y), text, font=font, fontsize=size)
    w.write_text(page, color=color)

HEADER_TEXT = "PROMPT INJECTION IS AN EPISTEMIC ATTACK — AXIOVEX WHITEPAPER"
LOCKUP_TEXT = "Prompt Injection Is an Epistemic Attack · Axiovex Systems"
COPY_TEXT = "© 2026 Axiovex Systems, LLC. All rights reserved."
assert f_bold.text_length(LOCKUP_TEXT, fontsize=7.6) + \
    f_reg.text_length(COPY_TEXT, fontsize=7.6) + 104 < W, "footer texts collide"

for i in range(first_body, out.page_count):
    page = out[i]
    # header band
    page.draw_rect(pymupdf.Rect(0, 0, W, 40), color=None, fill=NAVY)
    page.draw_rect(pymupdf.Rect(0, 40, W, 43), color=None, fill=CYAN)
    tw(page, HEADER_TEXT, 52, 26, f_bold, 7.6, CYAN)
    # logo right (white logo png, aspect 1557x443)
    page.insert_image(pymupdf.Rect(W-52-118, 9, W-52, 9+118*443/1557), stream=logo_img)
    # footer band
    page.draw_rect(pymupdf.Rect(0, H-34, W, H), color=None, fill=NAVY)
    tw(page, LOCKUP_TEXT, 52, H-13, f_bold, 7.6, NEAR)
    ctext = COPY_TEXT
    tw_width = f_reg.text_length(ctext, fontsize=7.6)
    tw(page, ctext, W-52-tw_width, H-13, f_reg, 7.6, NEAR)
    ptext = f"Page {i+1} of {out.page_count}"
    pw_ = f_reg.text_length(ptext, fontsize=7.6)
    # page number sits just above footer band, right side, steel
    tw(page, ptext, W-52-pw_, H-44, f_reg, 7.6, STEEL)

out.set_metadata({
    "title": TITLE,
    "author": "Axiovex Systems, LLC",
    "subject": "Prompt injection reframed as an attack on what an agent believes about its principal's intent — provenance, claim grading, and a layered defense, measured with a planted-instruction battery, an adversarial red team, and a model-tuning experiment, misses included.",
    "creator": "Axiovex Systems, LLC",
})
out.set_language("en-US")
out.save(OUT, deflate=True)
print("pages:", out.page_count, "->", OUT)
