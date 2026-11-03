# AXIOVEX Arcturus — Introduction — source

`index.html` is the source of truth for `docs/arcturus-one-pager.pdf`
(the introduction previously had no source in this repo; this HTML rebuild,
2026-11-03 under issue #49 Phase 2b, reproduces the published Version 2
design at its original typesetting and carries the Phase 2b repairs).

The document is a **two-page introduction**. The published filename
(`arcturus-one-pager.pdf`) is a stable address that handouts and the
website link to, so it does not change; every label that describes the
document (this README, `docs.json`, the website documents page) names it
as a two-page introduction.

## Rebuild

1. Edit `index.html`.
2. Build the PDF (requires the Playwright venv python + Chromium):
   `~/workspace/venvs/playwright/bin/python build_pdf.py` — US Letter, zero
   margins, tagged output.
3. Copy `build/arcturus-one-pager-final.pdf` to
   `docs/arcturus-one-pager.pdf`, roll the version/date in the closing
   line per the owner's document-versioning rule, and add a `CHANGELOG.md`
   entry.
