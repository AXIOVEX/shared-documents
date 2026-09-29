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
2. Render slides (requires node/bun, the `playwright` package, Chromium):
   `node render_slides.mjs`
3. Build the pptx (requires `python-pptx` and `Pillow`):
   `python build_pptx_with_notes.py`
4. Export the PDF: open the pptx in LibreOffice and export, or
   `soffice --headless --convert-to pdf beginning-ai-course.pptx`
5. Copy the PDF to `docs/ai-101-beyond-the-chatbot-slides.pdf` and bump the
   revision stamps and `CHANGELOG.md`.

## Notes

- Brand colors: navy `#081F32`, cyan `#00DEF6`, near-white `#F7FCFF`.
  Do not recolor or redraw the AXIOVEX logo.
- Public contact: `start@axiovexsystems.com`, website https://axiovexsystems.com, LinkedIn https://www.linkedin.com/company/axiovexsystems.
- Slide 16's video URL must read exactly
  `https://www.youtube.com/watch?v=CMFj75kBQlU` (lowercase "l" in the video
  ID). It is set in a monospace face so the "l" is unmistakable from "I".
