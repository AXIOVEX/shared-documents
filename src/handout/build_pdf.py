#!/usr/bin/env python3
"""Build the AI 101 handout PDF from index.html (Chromium print-to-PDF).

Same production route as before (headless Chromium, US Letter, zero margins),
with tagged output requested so the PDF carries a structure tree.
Run with the Playwright venv python:
    ~/workspace/venvs/playwright/bin/python build_pdf.py
Writes build/ai-101-handout.pdf; copy it over ../../docs/ai-101-handout.pdf
to republish.
"""
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent
BUILD = HERE / "build"
BUILD.mkdir(exist_ok=True)
OUT = BUILD / "ai-101-handout.pdf"

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
    "title": "AI 101: Beyond the Chatbot — Handout",
    "author": "Axiovex Systems, LLC",
    "subject": "Two-page handout for the AI 101 course: field guide (page 1) and plain-language glossary (page 2).",
    "creator": "Axiovex Systems, LLC",
})
doc.set_language("en-US")
doc.save(BUILD / "ai-101-handout-final.pdf", deflate=True)
print("pages:", doc.page_count, "->", BUILD / "ai-101-handout-final.pdf")
