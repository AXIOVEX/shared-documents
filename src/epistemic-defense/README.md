# Whitepaper — "Prompt Injection Is an Epistemic Attack"

Source for `docs/prompt-injection-epistemic-attack.pdf` (published
2026-11-03 on axiovexsystems.com/documents).

- `paper.md` — the paper text as published: *Prompt Injection Is an
  Epistemic Attack: Provenance, Claim Grading, and Layered Defense for
  AI Agents* (Axiovex Systems, 29 October 2026; the adaptive model-layer
  red-team results were added to Section 6 on 2026-10-30, before first
  publication).
- `build_pdf.py` — builds the branded PDF in the standard Axiovex
  document template: `paper.md` → styled HTML (branded title page +
  body) → Chromium print-to-PDF (tagged, document language set) →
  PyMuPDF running header/footer stamps, the same production route as
  the AI 101 handout and the "Endorsed by Experts" whitepaper
  (`src/whitepaper/`). Branding follows the Axiovex system: deep navy
  `#081F32`, steel `#405B70`, electric cyan `#00DEF6`, near-white
  `#F7FCFF`; Noto Sans body, Noto Serif Bold display headings; footer
  "© 2026 Axiovex Systems, LLC. All rights reserved." Rebuild with the
  Playwright venv python:

  ```sh
  ~/workspace/venvs/playwright/bin/python build_pdf.py
  # writes build/prompt-injection-epistemic-attack.pdf
  ```

  Copy the result over `docs/prompt-injection-epistemic-attack.pdf` to
  republish; the website sync picks it up from `docs.json`.
- Earlier issues (first publication through the attribution re-issue of
  2026-11-04) were built from the same `paper.md` with pandoc and the
  LuaLaTeX engine (TeX Live), DejaVu Serif/Sans fonts, one-inch
  margins, 11 pt, with no branding. The branded build changes the
  typesetting only; the text is `paper.md` verbatim.

The companion public repository — design documents, the agent-facing
skill, the battery, the screener, and the tuning experiment — is the
public `injection-defense` repository on GitHub. The tuned
adapter and the battery dataset are published on Hugging Face under
the `tpierson-eh` account.
