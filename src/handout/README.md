# AI 101 handout source

HTML source for the "AI 101: Beyond the Chatbot" two-page handout. The
published PDF is built from these files;
`docs/ai-101-handout.pdf` is the distributable.

## Layout

- `index.html` — the full handout (2 pages, US Letter, zero print margin).
- `media/` — logo and QR code images (video QR, slides QR, handout QR).
- `OUTLINE.md` — content outline.
- `generate_qr.py`, `embed_qr.py`, `generate_course_material_qr.py` — the
  scripts used to generate and place the QR codes.

## Rebuild

1. Edit `index.html`.
2. Print to PDF from headless Chromium at US Letter size with zero margins
   (the stylesheet sets `@page { size: Letter; margin: 0; }`).
3. Copy the PDF to `docs/ai-101-handout.pdf` and bump the revision stamps
   and `CHANGELOG.md`.

## Notes

- Brand colors: navy `#081F32`, cyan `#00DEF6`, near-white `#F7FCFF`.
  Do not recolor or redraw the AXIOVEX logo.
- Public contact: `start@axiovexsystems.com`, website https://axiovexsystems.com, LinkedIn https://www.linkedin.com/company/axiovexsystems.
- The QR codes encode the canonical hosted URLs; regenerate them with the
  scripts above if those URLs change.
