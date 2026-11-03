# AI 101 deck source

HTML source for the "AI 101: Beyond the Chatbot" slide deck. The published
PDF is built from these files; `docs/ai-101-beyond-the-chatbot-slides.pdf`
is the distributable.

## Layout

- `index.html` — the full deck; each `<section class="slide">` is one slide.
- `slides/` — per-slide partials (inlined into `index.html`), `deck.css`
  (shared styles), `deck.json` (slide order manifest).
- `speaker_notes.json` — presenter notes, keyed by slide id.
- `media/` — logo assets, the video QR code, and AI-generated slide imagery.
- `validate/page-NN.png` — rendered slides at 2560x1440; these are the
  direct inputs to the pptx build.

## Rebuild

1. Edit `index.html` (or a partial in `slides/`, then re-inline).
2. Build the published PDF (requires the Playwright venv python +
   Chromium): `~/workspace/venvs/playwright/bin/python build_pdf.py`
   This prints the deck HTML directly, so the PDF carries real selectable
   text, reading order, image alt text, and links. (The older route —
   exporting the PDF from the PPTX — rasterized every slide and shipped a
   PDF with no text at all; do not use it for the published PDF.)
3. Copy `build/ai-101-beyond-the-chatbot-slides-final.pdf` to
   `docs/ai-101-beyond-the-chatbot-slides.pdf`, copy `index.html` to
   `docs/ai-101-beyond-the-chatbot-slides.html` (the accessible HTML
   companion, version-matched to the PDF), and bump the revision stamps
   and `CHANGELOG.md`.
4. Presenter PPTX (unchanged): render slides with
   `node render_slides.mjs`, then `python build_pptx_with_notes.py`.

## Notes

- Brand colors: navy `#081F32`, cyan `#00DEF6`, near-white `#F7FCFF`.
  Do not recolor or redraw the AXIOVEX logo.
- Public contact: `start@axiovexsystems.com`, website https://axiovexsystems.com, LinkedIn https://www.linkedin.com/company/axiovexsystems.
- Slide 16's video URL must read exactly
  `https://www.youtube.com/watch?v=CMFj75kBQlU` (lowercase "l" in the video
  ID). It is set in a monospace face so the "l" is unmistakable from "I".
