# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Whitepaper "VEXA, a Projected Constraints Stack by Axiovex Systems" (v1.0), November 4, 2026 (`docs/VEXA-WHITEPAPER-2026-11-04.pdf`): the epistemic stack behind Axiovex's research programs, with append-only claim ledgers, generated matrices and maps, a verification gate, and a spatial interface for Quest 3. The canonical source lives in AXIOVEX/vexa (`whitepaper/VEXA-WHITEPAPER-2026-11-04.pdf`); this repository carries the published copy, byte-identical to the source (SHA-256 verified at publication). Listed in `docs.json` (order 7) for the axiovexsystems.com/documents sync; served at the stable address https://axiovexsystems.com/documents/files/VEXA-WHITEPAPER-2026-11-04.pdf.
- Document manifest (`MANIFEST.json`) — November 3, 2026 — every root-level published document's source, version, content date, page count, and SHA-256 checksum, established with the issue #49 Phase 2b repairs and refreshed whenever a document changes. The `docs/workforce/` tree keeps its own manifest.
- Sources for the Capability Statement and the Arcturus introduction (`src/capability-statement/`, `src/arcturus-one-pager/`) — November 3, 2026 — both documents previously had no source in this repo; the new HTML sources reproduce the published designs and rebuild tagged PDFs by the same Chromium route as the other documents.
- AI 101 slide deck — accessible HTML companion (`docs/ai-101-beyond-the-chatbot-slides.html`) — November 3, 2026 — published from the deck's own source, version-matched to the deck PDF (v1.0.16).
- Whitepaper "Prompt Injection Is an Epistemic Attack" — November 3, 2026 (`docs/prompt-injection-epistemic-attack.pdf`) — Axiovex Systems research shared on this site: prompt injection reframed as an attack on what an agent believes about its principal's intent, with a layered defense measured by a planted-instruction battery, an adversarial red team (deterministic and model layers), and a model-tuning experiment, misses included. Sources in `src/epistemic-defense/`; listed in `docs.json` (order 6) for the axiovexsystems.com/documents sync; served at the stable address https://axiovexsystems.com/documents/files/prompt-injection-epistemic-attack.pdf.
- Axiovex Capability Statement, Version 1 — October 27, 2026 (`docs/axiovex-capability-statement.pdf`) — the company's one-page statement: the flagship Michigan data pipeline, the constraint-based planning method, core competencies, and proof of work, for boards, program operators, and contracting officers. Listed in `docs.json` (order 4) for the axiovexsystems.com/documents sync; served at the stable address https://axiovexsystems.com/documents/files/axiovex-capability-statement.pdf.
- Whitepaper "Endorsed by Experts" (`docs/endorsed-by-experts-prompt-injection.pdf`) — a real indirect prompt injection (authority capture) caught during ordinary research on 2026-10-22: the incident record, four documented cases, what stopped it, and a defence checklist. Sources in `src/whitepaper/`; listed in `docs.json` (order 3) for the axiovexsystems.com/documents sync.

### Changed
- Changelog attribution strike — November 10, 2026 — on the owner's order, the November 3, 2026 "Added" entry for "Prompt Injection Is an Epistemic Attack" is corrected in place: it originally credited the paper as ElectroHire research, and the credit now reads Axiovex Systems research, matching the November 4, 2026 correction entry below, which stands as the record of what the entry originally said. No document changed; this is a changelog-only correction.
- AXIOVEX Arcturus — Introduction, Version 3 — re-issued November 9, 2026 (`docs/arcturus-one-pager.pdf`) — notice fix only (compliance notice fix N-2): the footer now carries the copyright line "© 2026 Axiovex Systems, LLC. All rights reserved." No content changed; the version remains Version 3. New SHA-256: 1abb431d67910e75beaf26f6816499e656d4b936fd07e470b2247f35f6146e85 (2 pages, 176,931 bytes). Source in this repo (`src/arcturus-one-pager/index.html`). `MANIFEST.json` updated to match. Served at the same stable address: https://axiovexsystems.com/documents/files/arcturus-one-pager.pdf.
- Whitepaper "VEXA, a Projected Constraints Stack by Axiovex Systems" (v1.1) — re-issued November 9, 2026 (`docs/VEXA-WHITEPAPER-2026-11-04.pdf`) — notice fix only (compliance notice fix N-2): the title page now carries the copyright line "© 2026 Axiovex Systems, LLC. All rights reserved." No content changed; the version remains v1.1. New SHA-256: 4e8b728cf2b5efc416e3bd2e0acc212c866fa98d9e5b0e8d99d8db70553eb582 (10 pages, 866,372 bytes). Canonical source in AXIOVEX/vexa (`whitepaper/VEXA-WHITEPAPER-2026-11-04.pdf`, commit 7684b951); this repository carries the published copy, byte-identical to the source. `MANIFEST.json` updated to match. Served at the same stable address: https://axiovexsystems.com/documents/files/VEXA-WHITEPAPER-2026-11-04.pdf.
- AI 101: Beyond the Chatbot — slide deck, v1.0.17 — November 9, 2026 (`docs/ai-101-beyond-the-chatbot-slides.pdf`) — attribution correction: slide 17's YouTube link and QR code changed from `watch?v=CMFj75kBQlU` to `watch?v=7Pq-S557XQU`, and the credit line now reads CGP Grey, "What Happened to Horses Is Happening to Us" (originally published as "Humans Need Not Apply", 2014). Why: the printed link resolved to a video uploaded by Max Bocksch, not CGP Grey, so the deck attributed a third-party copy to the author. The correct CGP Grey upload is `7Pq-S557XQU`. Source: YouTube oEmbed responses for both video IDs, 2026-11-09; CGP Grey channel; independent citations of `7Pq-S557XQU` (found in our weekly review). The accessible HTML companion (`docs/ai-101-beyond-the-chatbot-slides.html`) is re-issued in step at v1.0.17. `MANIFEST.json` updated to match.
- AI 101: Beyond the Chatbot — handout, v1.0.17 — November 9, 2026 (`docs/ai-101-handout.pdf`) — the same attribution correction on page 1: the "Recommended viewing" link and QR code changed from `watch?v=CMFj75kBQlU` to `watch?v=7Pq-S557XQU`, and the credit line now names the video's current title, "What Happened to Horses Is Happening to Us" by CGP Grey (originally published as "Humans Need Not Apply", 2014). Why and source as the slide-deck entry above. `MANIFEST.json` updated to match.
- Whitepaper "VEXA, a Projected Constraints Stack by Axiovex Systems" (v1.1) — re-issued November 5, 2026 (`docs/VEXA-WHITEPAPER-2026-11-04.pdf`) — v1.1 edition: new Section 9 sets out the extension-of-mind mandate (Amendment A1); Section 5 gains FR-16 verdict reporting; Section 10 is updated with the Glossa Spec 090 generalization outcome; and the stated boundaries are updated. New SHA-256: 1cf473a92c9dd1c7d648d60afd1cf11dbaedf8028429fc32582f1463f40e2cd3 (10 pages). Canonical source in AXIOVEX/vexa (`whitepaper/VEXA-WHITEPAPER-2026-11-04.pdf`, commit c47d47d); this repository carries the published copy, byte-identical to the source. `MANIFEST.json` updated to match. Served at the same stable address: https://axiovexsystems.com/documents/files/VEXA-WHITEPAPER-2026-11-04.pdf.
- Whitepaper "Prompt Injection Is an Epistemic Attack" — re-issued November 4, 2026 (`docs/prompt-injection-epistemic-attack.pdf`) — presentational rebuild only: the paper is now typeset in the standard Axiovex document template (branded title page, navy/cyan branding system, running header and footer with page numbers), and the PDF is tagged with document language set; the previous issue was an unbranded, untagged render. No content changed: the text is `paper.md` verbatim, verified against the previous issue by a full pdftotext comparison in which every remaining difference was classified as template furniture, list-marker, or hyphenation/reflow artifact. New build source `src/epistemic-defense/build_pdf.py` (the previous issues were built with pandoc/LuaLaTeX). New SHA-256: 7e75603f6f1537ca3672bf3ebac8084de69dfff1ad7fcf900beb59c14bc57778 (12 pages). `MANIFEST.json` updated to match. Served at the same stable address: https://axiovexsystems.com/documents/files/prompt-injection-epistemic-attack.pdf.
- Whitepaper "VEXA, a Projected Constraints Stack by Axiovex Systems" (v1.0) — revised November 4, 2026 (`docs/VEXA-WHITEPAPER-2026-11-04.pdf`) — presentational revision only: footer page numbers now appear on all pages, and page-break rules keep each of the four figures whole with its caption. No content changed. New SHA-256: f77860678a4ed99e72528aa36842f73ff7de3534eea44099b719653210e49ad8 (9 pages). Canonical source in AXIOVEX/vexa (`whitepaper/VEXA-WHITEPAPER-2026-11-04.pdf`, commit 184cf2e); this repository carries the published copy, byte-identical to the source. `MANIFEST.json` updated to match. Served at the same stable address: https://axiovexsystems.com/documents/files/VEXA-WHITEPAPER-2026-11-04.pdf.
- Whitepaper "Prompt Injection Is an Epistemic Attack" — re-issued November 4, 2026 (`docs/prompt-injection-epistemic-attack.pdf`) — attribution correction: the paper was re-issued with corrected attribution — the research is Axiovex Systems'; the original issue (November 3, 2026) credited ElectroHire. The author line, the "About" section, and the references now credit Axiovex Systems, and the `docs.json` (order 6) description is corrected to match. No findings, results, or other content changed. New SHA-256: 5d25db36b6f86e1acb0d2f34371055d18c92b627eface27f1f993e1fd9a96a67 (11 pages). Sources in `src/epistemic-defense/` corrected to match; entry added to `MANIFEST.json`. Served at the same stable address: https://axiovexsystems.com/documents/files/prompt-injection-epistemic-attack.pdf.
- Axiovex Capability Statement, Version 6 — November 3, 2026 (`docs/axiovex-capability-statement.pdf`) — claim repairs from the issue #49 audit (Phase 2b): the platform paragraph's data-loss line is now labeled a design target ("redundancy by design, with no data loss from a single failure as the design target"); the feasibility differentiator reads "checked against every documented limit" and, where no workable plan exists under the model, "names the constraints that block it"; the isolation differentiator is framed as the boundary held by design. The leadership line was reconciled against the owner's direction of 2026-10-28 and is unchanged — it already reads exactly as approved ("President · Rockson Arnold, Chief of Strategy"). The document also gains an HTML source in this repo (`src/capability-statement/`) and a tagged PDF build. Footer rolled from Version 4 to Version 6: Version 5 was published on 2026-10-29 (funding language removed) and reverted the same day, and a version number is never reused for different content. Served at the same stable address: https://axiovexsystems.com/documents/files/axiovex-capability-statement.pdf.
- AXIOVEX Arcturus — Introduction, Version 3 — November 2026 (`docs/arcturus-one-pager.pdf`) — the document is now labeled a two-page introduction wherever it is described (the published filename is a stable address and does not change): "Where It Stands" and the etymology/version line move to page 2 as a complete closing page, ending the footer-only overflow page. The foresight line now states the 6-to-36-month figure as a proposed foresight horizon pending validation; the "Plan against reality" bullet names "which limits bind"; the proposed Act carries its current working title, the Workforce Foresight and Planning Pilot Act ("Efficient Distribution" was dropped); and "Join the pilot" is a working link to https://axiovexsystems.com/arcturus. First HTML source in this repo (`src/arcturus-one-pager/`); tagged PDF build. Footer rolled from Version 2 to Version 3. Served at the same stable address: https://axiovexsystems.com/documents/files/arcturus-one-pager.pdf.
- AI 101: Beyond the Chatbot — slide deck, v1.0.16 — November 3, 2026 (`docs/ai-101-beyond-the-chatbot-slides.pdf`) — rebuilt from the deck's own HTML instead of the PPTX export: the previous PDF carried every slide as a raster image with no extractable text; the new PDF has real selectable text in slide order, image alt text, a structure tree, document language, and working links (the "Humans Need Not Apply" video on the horses slide; email, website, and LinkedIn on the closing slide). Claim repairs: the closing slide now reads "We must be proactive rather than reactive. Waiting raises the risk of avoidable job losses and economic damage."; the horses slide no longer presents the analogy as a held-up warning ("The analogy still bites because capability keeps getting cheaper, broader, and easier to deploy." / "The lesson is not panic, and an analogy is not a prediction."); and the CMMC decision rule is scoped to environments approved for the data under the contract. An accessible HTML companion is published alongside (see Added). Revision stamp unified with the handout at v1.0.16 (the deck previously showed v1.0.14 · 2026-10-08).
- AI 101: Beyond the Chatbot — handout, v1.0.16 — November 3, 2026 (`docs/ai-101-handout.pdf`) — the glossary page is rebalanced into balanced multi-column flow at the page's own type scale: in the previous PDF the repair-shop analogy block rendered below the page-2 footer and was clipped mid-sentence; all glossary text is now fully visible on the page. The CMMC decision box is scoped to the same contract-terms wording as the deck. Tagged PDF build with document language. Revision stamps updated from v1.0.15 · 2026-10-27 to v1.0.16 · 2026-11-03 (both footer and materials block).
- Whitepaper "Endorsed by Experts" — reference and structure pass — November 3, 2026 (`docs/endorsed-by-experts-prompt-injection.pdf`) — no findings changed: the Sources now carry full citations and URLs for the OWASP LLM01:2025 prompt-injection entry, the EchoLeak disclosure (Aim Labs) and Microsoft's CVE-2025-32711 advisory, and the SafeBreach / "Invitation Is All You Need" research including its paper (arXiv:2508.12175), and every source URL is a working link. The PDF is rebuilt as a single tagged document with structure and document language (the previous PDF was untagged). Served at the same stable address: https://axiovexsystems.com/documents/files/endorsed-by-experts-prompt-injection.pdf.
- AXIOVEX Arcturus — One-Page Introduction, Version 2 re-issue — October 31, 2026 (`docs/arcturus-one-pager.pdf`) — two owner-approved corrections (register PD-12) and nothing else: the data section’s closing sentence now reads “Arcturus shares the least data a task needs and keeps a record of every disclosure. It is being built to be driven from this website or from your own AI assistant — in development, and not open access today: the pilot waitlist is the way in.”; and the “Find the match” bullet now closes “That matching is a designed capability still in development: it is not a live offer, and no matching is happening today.” The corrected text runs to two pages at the document’s original typesetting, with only the footer rule and the etymology/version line on page 2; the owner chose the faithful two-page build on 2026-10-31 over a one-page typesetting adjustment and over shortening the text. Footer stamp unchanged (Version 2). Served at the same stable address: https://axiovexsystems.com/documents/files/arcturus-one-pager.pdf.
- AXIOVEX Arcturus — One-Page Introduction, Version 2 — October 29, 2026 (`docs/arcturus-one-pager.pdf`) — content updated to the program's current course on the owner's direction (2026-10-29): the scope sentence now states plainly that Arcturus works on the resources organizations already have — not a job board, and no individual job seekers (owner's 2026-10-28 scope ruling); transferable skills are framed for workforces, not individuals; the foresight line carries its 6-to-36-month horizon ahead of displacement; the introduction line closes with the standing program policy — never paid per placement or per outcome; the data section states the distributed-custody design goal in design tense (no single party, Axiovex included, can read another organization's data alone, with record keys held under the organization's own control) and the Catena-X dataspace direction for manufacturing capability data; and "Where it stands" records that a federal pilot program written around this model exists today as a proposed concept, not yet introduced. Footer rolled from Version 1 to Version 2 per the owner's ruling of 2026-10-29, superseding the v1 production-notes rule that the stamp stays Version 1 while pre-production. Prepared on branch `spec-036/arcturus-one-pager-v2` for staging verification under website spec 036; served at the same stable address: https://axiovexsystems.com/documents/files/arcturus-one-pager.pdf.
- Axiovex Capability Statement, Version 4 — October 28, 2026 (`docs/axiovex-capability-statement.pdf`) — the leadership and contact lines are scrubbed to role language on the owner's direction (2026-10-28): the statement no longer names the president personally (leadership now reads "President · Rockson Arnold, Chief of Strategy"; the contact block "President — tristen@axiovexsystems.com"), applying the standing rule that partner-facing material frames relationships as the company's, in role language only — the same treatment as the Serrato re-brief one-pager. No other content changed. Footer rolled from Version 3 to Version 4 per the owner's document-versioning rule. Served at the same stable address: https://axiovexsystems.com/documents/files/axiovex-capability-statement.pdf.
- Axiovex Capability Statement, Version 3 — October 27, 2026 (`docs/axiovex-capability-statement.pdf`) — the Arcturus passage now tells the corrected program story (owner's Addendum I correction, 2026-10-27): Arcturus is a workforce and capability program, designed for state and federal funding and for Axiovex to manage, in which employers, universities, and workforce organizations participate — "not sold, licensed, or offered by subscription" — replacing Version 2's product framing. Broadened the same evening on the owner's direction (2026-10-27 22:47 ET) to carry the full corrected story: the platform (Arcturus runs on Cloudflare Workers — stateless solver instances, queued and checkpointed jobs, backups with retention locks, build-stamp provability; the public site on Cloudflare Pages), two new differentiators (AI-first access, honestly framed as in development — not open access today; and the AI-agent boundary Axiovex holds — server-side isolation between organizations, least-data release to agents, agent attestation with per-organization policies, a disclosure log of agent accesses), and support@axiovexsystems.com added to the contact block. The narrative also introduces Arcturus as Michigan&rsquo;s North Star — the fixed point every party to the work can steer by (the owner&rsquo;s framing, 2026-10-27 22:53 ET; a descriptor in Axiovex&rsquo;s own voice, never a rename and never an endorsement claim). Footer rolled from Version 2 to Version 3 per the owner's document-versioning rule. Prepared on branch `spec-036/capability-statement-v3` for staging verification with website spec 036; reaches the stable address https://axiovexsystems.com/documents/files/axiovex-capability-statement.pdf when the owner approves promotion (this branch merges to main first, so the website's document sync keeps Version 3).
- Axiovex Capability Statement, Version 2 — October 27, 2026 (`docs/axiovex-capability-statement.pdf`) — the flagship product is now named in the statement: Axiovex Arcturus, an optimization solver employers and universities can use, named in the pitch and the flagship differentiator. (Name corrected to Arcturus before Version 2 first reached the website — the live site still served Version 1 — so the correction stays within Version 2.) Footer rolled from Version 1 to Version 2 — the first published change after the statement's promotion to production, per the owner's document-versioning rule. Served at the same stable address: https://axiovexsystems.com/documents/files/axiovex-capability-statement.pdf.

## [1.0.15] - 2026-10-27 — handout

### Fixed
- Wording correction (owner-directed): the handout no longer describes any organization as a retraining partner. The public-leaders line now reads "Work with your local workforce agency and community college to make it real," and the content outline describes Michigan Works! and Macomb Community College factually, as public retraining services leaders can connect workers to.
- Updated the revision stamps on the handout from v1.0.12 to v1.0.15.

## [1.0.14] - 2026-10-08 — deck

### Fixed
- Cover speaker note: corrected the session timing split to match the sum of the per-slide timings — 41 minutes to teach (was 40) and 2 minutes of slack (was 3). The 10 minutes for Q&A and 7 minutes to commit and close are unchanged; the session still totals 60 minutes. No per-slide timings changed.
- Updated the revision stamps on the deck from v1.0.13 to v1.0.14.

## [1.0.13] - 2026-10-05 — deck

### Added
- New slide "Superintelligence is not a synonym for AI" — the ladder (narrow AI exists today; AGI and superintelligence are theoretical), inserted after the history slide, with speaker notes. Part of the AI → SI terminology update: AI remains the term for today's technology; SI is defined and reserved for superintelligence.
- Updated the revision stamps on the deck from v1.0.12 to v1.0.13 (two stale v1.0.11 stamps normalized).

## [1.0.12] - 2026-10-05 — handout

### Added
- Plain-Language Glossary (AI Basics): added "Narrow AI (ANI)", "General AI (AGI)", and "Superintelligence (SI)" entries defining the ladder and reserving SI for superintelligence.
- Updated the revision stamps on the handout from v1.0.11 to v1.0.12.


## [1.0.11] - 2026-09-30 — handout

### Added
- Plain-Language Glossary page: added the full repair-shop analogy as a callout under Risks and Controls (a difficult job passed between shifts: the customer complaint, service history, and prior notes are the context; an unperformed "fuel pump tested fine" is the hallucination; condensing "possible electrical fault — still unconfirmed" into "electrical fault" is context compression; the takeaway: keep the original records, separate verified facts from guesses, and check critical details before the next decision depends on them).
- Updated the revision stamps on the handout from v1.0.10 to v1.0.11.

## [1.0.12] - 2026-09-30 — deck

### Changed
- Hallucinations slide: replaced the Telestrations analogy with a repair-shop analogy (a difficult job passed between shifts: the customer complaint, service history, and prior notes are the context; an unperformed "fuel pump tested fine" is the hallucination; condensing "possible electrical fault — still unconfirmed" into "electrical fault" is context compression). The slide now carries the full walkthrough and takeaway: keep the original records, separate verified facts from guesses, and check critical details before the next decision depends on them.
- Speaker notes: the repair-shop walkthrough is now the main talking point; Telestrations is kept as an optional speaking point (not on the slide).
- Updated the revision stamps on the deck from v1.0.11 to v1.0.12.

## [1.0.10] - 2026-09-30 — handout

### Added
- Plain-Language Glossary: added a "Context compression" definition in Risks and Controls (condensing a long record into a short summary can lose an important qualification; example: "possible electrical fault — still unconfirmed" shortened to "electrical fault").
- Updated the revision stamps on the handout from v1.0.9 to v1.0.10.

## [1.0.11] - 2026-09-30 — deck

### Fixed
- Hallucinations slide: removed the large blank gap between the Telestrations
  analogy callout and the "Why it happens / How to contain it" panels. The
  callout was sitting in a stretched grid row; the slide now stacks its
  blocks compactly. Also synced the `.analogy` style into `slides/deck.css`,
  which had drifted out of the inlined copy in `index.html`.
- Updated the revision stamps on the deck from v1.0.10 to v1.0.11.

## [1.0.10] - 2026-09-30 — deck

### Changed
- Hallucinations slide now frames the failure mode with a Telestrations
  analogy: each player draws the previous player's guess and the picture
  drifts every round, the way a language model builds each word on the last
  so small errors compound into confident-sounding fiction. Speaker notes
  carry the same analogy. All other slide content is unchanged.
- Updated the revision stamps on the deck from v1.0.9 to v1.0.10.

## [1.0.9] - 2026-09-29 — deck

### Changed
- Reworded the slide 13 heading from "Three boundaries to set this week" to
  "Three boundaries to set first". The three items themselves are unchanged.
- Updated the revision stamps on the deck from v1.0.8 to v1.0.9.

## [1.0.9] - 2026-09-29 — handout

### Changed
- Reworded the handout heading from "Three boundaries to set this week" to
  "Three boundaries to set first". The three items themselves are unchanged.
- Updated the revision stamps on the handout from v1.0.8 to v1.0.9.

## [1.0.8] - 2026-09-29 — deck

### Changed
- Removed the personal name from the closing slide contact block; it now
  references Axiovex Systems with the email, website, and LinkedIn page.
- Updated the revision stamps on the deck from v1.0.7 to v1.0.8.

## [1.0.8] - 2026-09-29 — handout

### Changed
- Removed the personal name from the handout contact block; it now references
  Axiovex Systems with the email, website, and LinkedIn page.
- Updated the revision stamps on the handout from v1.0.7 to v1.0.8.

## [1.0.7] - 2026-09-29 — deck

### Changed
- Added the website (https://axiovexsystems.com) and LinkedIn page
  (https://www.linkedin.com/company/axiovexsystems) to the closing slide
  contact block, alongside the email.
- Updated the revision stamps on the deck from v1.0.6 to v1.0.7.

## [1.0.7] - 2026-09-29 — handout

### Changed
- Recommended-viewing link now shows the full URL
  (https://www.youtube.com/watch?v=CMFj75kBQlU) instead of the shortened
  youtu.be form; both resolve to the same video. Updated the revision stamps
  from v1.0.6 to v1.0.7.

## [1.0.6] - 2026-09-29 — handout

### Changed
- Added the website (https://axiovexsystems.com) and LinkedIn page
  (https://www.linkedin.com/company/axiovexsystems) to the handout contact
  block, alongside the email.
- Updated the revision stamps on the handout from v1.0.5 to v1.0.6.

## [1.0.6] - 2026-09-29 — deck

### Changed
- Updated the public contact email on the closing slide from
  start@axiovex-systems.com to start@axiovexsystems.com (primary domain).
- Updated the revision stamps on the deck from v1.0.5 to v1.0.6.

## [1.0.5] - 2026-09-29 — handout

### Changed
- Updated the public contact email on the handout from
  start@axiovex-systems.com to start@axiovexsystems.com (primary domain).
- Updated the revision stamps on the handout from v1.0.4 to v1.0.5.

## [1.0.5] - 2026-09-29 — deck

### Fixed
- Set the "Humans Need Not Apply" video URL displayed on deck slide 16 in a
  monospace face (DejaVu Sans Mono) so the lowercase "l" in the video ID is
  visually unmistakable from an uppercase "I". The URL text itself is
  unchanged and byte-identical: https://www.youtube.com/watch?v=CMFj75kBQlU
  The QR code was already correct and is unchanged.

### Changed
- Updated the revision stamps on the deck from v1.0.4 to v1.0.5. The handout
  and presenter guide are unchanged and remain at v1.0.4.

## [1.0.4] - 2026-09-29

### Fixed
- Corrected the "Humans Need Not Apply" video URL displayed on deck slide 16:
  the text had wrong character case in the video ID, so it led to a bad page.
  It now reads exactly https://www.youtube.com/watch?v=CMFj75kBQlU
  (lowercase "l" in the video ID). The QR code was already correct and is
  unchanged.

### Changed
- Updated the revision stamps on the deck, handout, and presenter guide from
  v1.0.3 to v1.0.4.

## [1.0.3] - 2026-09-29

### Changed
- Reworded the slide 13 / handout heading from "Three things to forbid this
  week" to "Three boundaries to set this week", with matching wording in the
  presenter guide. The three items themselves are unchanged.
- Removed the phone number from all materials. Contact blocks are now email
  only: start@axiovex-systems.com.
- Added a contact line to the GitHub Pages home page
  (start@axiovex-systems.com).
- Updated the revision stamps on the deck, handout, and presenter guide from
  v1.0.2 to v1.0.3.

### Fixed
- Corrected the printed "Humans Need Not Apply" video URL on handout page 1:
  the text had wrong character case in the video ID, so it led to a bad page.
  It now matches the correct address exactly:
  https://youtu.be/CMFj75kBQlU?is=8BTKniNg34Ya80FO (the QR code was already
  correct and is unchanged).

## [1.0.2] - 2026-09-29

### Changed
- Updated the contact email across the deck, handout, and presenter guide from
  the personal address to start@axiovex-systems.com.
- Updated the revision stamps on the deck, handout, and presenter guide from
  v1.0.1 to v1.0.2.

## [1.0.1] - 2026-09-29

### Fixed
- Corrected the displayed "Humans Need Not Apply" video URL on slide 16 of the
  deck: the printed text had wrong character case
  (https://www.youtube.com/watch?v=CMFj75KBQIU), which YouTube rejects because
  video IDs are case-sensitive. The displayed URL now matches the correct
  address exactly: https://youtu.be/CMFj75kBQlU?is=8BTKniNg34Ya80FO
  (the QR code payload was already correct and is unchanged).
- Updated the revision stamps on the deck, handout, and presenter guide from
  v1.0.0 to v1.0.1.

## [1.0.0] - 2026-09-29

### Added
- 20-slide "AI 101: Beyond the Chatbot" slide deck (PDF): a plain-language
  introduction to AI for manufacturing, engineering, defense, and public
  leaders, covering how AI works, agentic AI, practical adoption, governance,
  risks, and a closing commitment exercise.
- 2-page handout (PDF): key takeaways, QR codes linking to the hosted deck and
  handout, and a beginner glossary (tokens, context window, harness,
  abstention, hallucination, CUI, CMMC, and more).
- 12-page presenter guide (PDF): talking points, table exercise prompts, and
  timing notes matched to the deck order.
- Official AXIOVEX Systems branding across all materials (deep navy #081F32,
  electric cyan #00DEF6, near-white #F7FCFF).
- Version stamps (v1.0.0, 2026-09-29) on the deck, handout, and presenter
  guide, placed next to the copyright line.

### Changed
- Generalized all audience references so the materials are location-neutral
  and shareable with any group.

### Fixed
- Corrected the "Humans Need Not Apply" video link to its canonical YouTube
  URL in both the printed link and the QR code.

[unreleased]: https://github.com/AXIOVEX/shared-documents/compare/v1.0.4...HEAD
[1.0.4]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.4
[1.0.3]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.3
[1.0.2]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.2
[1.0.1]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.1
[1.0.0]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.0
