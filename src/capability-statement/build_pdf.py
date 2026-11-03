#!/usr/bin/env python3
"""Build the Axiovex Capability Statement PDF from index.html.

Chromium print-to-PDF at US Letter, zero margins, tagged output; then a
PyMuPDF pass sets metadata and document language. Run with the Playwright
venv python:
    ~/workspace/venvs/playwright/bin/python build_pdf.py
Writes build/axiovex-capability-statement-final.pdf; copy it over
../../docs/axiovex-capability-statement.pdf to republish.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
BUILD.mkdir(exist_ok=True)
OUT = BUILD / "axiovex-capability-statement.pdf"

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    pg = browser.new_page()
    pg.goto((HERE / "index.html").resolve().as_uri())
    pg.evaluate("document.fonts.ready.then(() => true)")
    pg.pdf(path=str(OUT), prefer_css_page_size=True, print_background=True, tagged=True)
    browser.close()

import pymupdf
doc = pymupdf.open(OUT)
doc.set_metadata({
    "title": "Axiovex Systems — Capability Statement",
    "author": "Axiovex Systems, LLC",
    "subject": "One-page capability statement: core competencies, differentiators, past performance, codes and company data.",
    "creator": "Axiovex Systems, LLC",
})
doc.set_language("en-US")
final = BUILD / "axiovex-capability-statement-final.pdf"
doc.save(final, deflate=True)
print("pages:", doc.page_count, "->", final)
