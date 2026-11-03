# Axiovex Capability Statement — source

`index.html` is the source of truth for `docs/axiovex-capability-statement.pdf`
(the statement previously had no source in this repo; this HTML rebuild,
2026-11-03 under issue #49 Phase 2b, reproduces the published Version 4
design and carries the Phase 2b claim repairs).

## Rebuild

1. Edit `index.html`.
2. Build the PDF (requires the Playwright venv python + Chromium):
   `~/workspace/venvs/playwright/bin/python build_pdf.py` — US Letter, zero
   margins, tagged output.
3. Copy `build/axiovex-capability-statement-final.pdf` to
   `docs/axiovex-capability-statement.pdf`, roll the version/date in the
   footer per the owner's document-versioning rule, and add a `CHANGELOG.md`
   entry.

Version note: Version 5 was published on 2026-10-29 (funding language
removed on the owner's directive) and reverted the same day, restoring
Version 4. The sequence therefore continues at Version 6 — a version number
is never reused for different content.
