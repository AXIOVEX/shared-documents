# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

[unreleased]: https://github.com/AXIOVEX/shared-documents/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.1
[1.0.0]: https://github.com/AXIOVEX/shared-documents/releases/tag/v1.0.0
