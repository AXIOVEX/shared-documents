#!/usr/bin/env python3
"""Build the AI 101 slide-deck PDF from index.html with real, selectable text.

The previous published PDF was exported from the PPTX build, so every slide
was a raster image with no extractable text. This route prints the deck's own
HTML directly: each <section class="slide"> becomes one 1280x720 (960x540 pt)
page, DOM order is the reading order, image alt text and links carry into the
PDF, and tagged output is requested for a structure tree.

The PPTX build (render_slides.mjs + build_pptx_with_notes.py) is unchanged and
remains the presenter deck. Run with the Playwright venv python:
    ~/workspace/venvs/playwright/bin/python build_pdf.py
Writes build/ai-101-beyond-the-chatbot-slides.pdf; copy it over
../../docs/ai-101-beyond-the-chatbot-slides.pdf to republish.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
BUILD.mkdir(exist_ok=True)
OUT = BUILD / "ai-101-beyond-the-chatbot-slides.pdf"

PRINT_CSS = """
@page { size: 1280px 720px; margin: 0; }
html, body { margin: 0 !important; padding: 0 !important; background: none !important; }
section.slide { page-break-after: always; page-break-inside: avoid; margin: 0 !important; }
section.slide:last-of-type { page-break-after: auto; }
"""

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    pg = browser.new_page(viewport={"width": 1280, "height": 720})
    pg.goto((HERE / "index.html").resolve().as_uri())
    pg.evaluate("document.fonts.ready.then(() => true)")
    pg.add_style_tag(content=PRINT_CSS)
    n = pg.evaluate("document.querySelectorAll('section.slide').length")
    pg.pdf(path=str(OUT), width="1280px", height="720px", print_background=True,
           tagged=True, page_ranges="")
    browser.close()

import pymupdf
doc = pymupdf.open(OUT)
doc.set_metadata({
    "title": "AI 101: Beyond the Chatbot — Slide Deck",
    "author": "Axiovex Systems, LLC",
    "subject": "Slide deck for the AI 101 course: what modern AI is, where it helps, where it fails, and how to put it to work responsibly.",
    "creator": "Axiovex Systems, LLC",
})
doc.set_language("en-US")
final = BUILD / "ai-101-beyond-the-chatbot-slides-final.pdf"
doc.save(final, deflate=True)
print("slides in HTML:", n, "| PDF pages:", doc.page_count, "->", final)
