# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Axiovex Capability Statement, Version 1 — October 27, 2026 (`docs/axiovex-capability-statement.pdf`) — the company's one-page statement: the flagship Michigan data pipeline, the constraint-based planning method, core competencies, and proof of work, for boards, program operators, and contracting officers. Listed in `docs.json` (order 4) for the axiovexsystems.com/documents sync; served at the stable address https://axiovexsystems.com/documents/files/axiovex-capability-statement.pdf.
- Whitepaper "Endorsed by Experts" (`docs/endorsed-by-experts-prompt-injection.pdf`) — a real indirect prompt injection (authority capture) caught during ordinary research on 2026-10-22: the incident record, four documented cases, what stopped it, and a defence checklist. Sources in `src/whitepaper/`; listed in `docs.json` (order 3) for the axiovexsystems.com/documents sync.

### Changed
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
