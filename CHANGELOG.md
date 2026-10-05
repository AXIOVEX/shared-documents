# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
