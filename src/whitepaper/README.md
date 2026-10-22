# Whitepaper — "Endorsed by Experts"

Source for `docs/endorsed-by-experts-prompt-injection.pdf` (published
2026-10-22; Axiovex website spec 031).

- `whitepaper.md` — the approved paper text, including the corrections
  list that records every change from the first draft and its basis.
- `build_pdf.py` — builds the branded PDF: markdown → styled HTML
  (title page + body) → Chromium print-to-PDF (the same production
  route as the AI 101 handout) → PyMuPDF merge with the running
  header/footer stamped on body pages.

Branding follows the Axiovex system (reference: the AI 101 handout):
deep navy `#081F32`, steel `#405B70`, electric cyan `#00DEF6`,
near-white `#F7FCFF`; Noto Sans body, Noto Serif Bold display
headings; footer "© 2026 Axiovex Systems, LLC. All rights reserved."

## Rebuild

Needs a Python environment with `markdown`, `playwright` (with
Chromium), and `pymupdf`, plus the Noto Sans / Noto Serif fonts:

```sh
python build_pdf.py   # writes build/endorsed-by-experts-prompt-injection.pdf
```

Copy the result over `docs/endorsed-by-experts-prompt-injection.pdf`
to republish; the website sync picks it up from `docs.json`.
