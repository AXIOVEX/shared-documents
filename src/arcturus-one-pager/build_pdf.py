#!/usr/bin/env python3
"""Build the AXIOVEX Arcturus introduction PDF from index.html.

Two pages at the document's original typesetting: page 1 carries the
introduction through "Your Data Stays Yours"; page 2 carries "Where It
Stands", the pilot call to action (a live link), and the etymology/version
line — the previous build left page 2 as footer-only overflow.

Chromium print-to-PDF at US Letter, zero margins, tagged output; then a
PyMuPDF pass sets metadata and document language. Run with the Playwright
venv python:
    ~/workspace/venvs/playwright/bin/python build_pdf.py
Writes build/arcturus-one-pager-final.pdf; copy it over
../../docs/arcturus-one-pager.pdf to republish (the filename is a stable
published address and does not change).
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
BUILD.mkdir(exist_ok=True)
OUT = BUILD / "arcturus-one-pager.pdf"

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
    "title": "AXIOVEX Arcturus — Introduction",
    "author": "Axiovex Systems, LLC",
    "subject": "Two-page introduction to AXIOVEX Arcturus, Michigan's North Star: a projected constraint system for workforce and capability planning.",
    "creator": "Axiovex Systems, LLC",
})
doc.set_language("en-US")
final = BUILD / "arcturus-one-pager-final.pdf"
doc.save(final, deflate=True)
print("pages:", doc.page_count, "->", final)
