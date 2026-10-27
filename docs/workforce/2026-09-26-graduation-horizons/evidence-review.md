# Evidence, corroboration and unresolved questions

## Source rule

An authoritative government statistical release may support an observation as a single source. Seek corroboration when practical; do not claim a source is certified unless that status is established. A second publication of the same BLS series checks transcription and consistency but is not independent evidence about the economy. Independent methods that point in the same direction can strengthen an interpretation while retaining their different definitions.

| Claim or input | Evidence check | Independence and result |
| --- | --- | --- |
| Michigan August unadjusted unemployment | MCDA state table against BLS state API: 5.2% | Same LAUS origin; agreement verifies publication consistency, not two independent surveys |
| Michigan household/payroll direction | MCDA household measures and employer survey | Different survey concepts; useful triangulation, not interchangeable counts |
| Weaker sentiment alongside hiring caution | National consumer survey and district employer survey | Different respondents/geographies; supports a cautious interpretation, not a quantified Michigan forecast |
| Radiology should not be declared obsolete | BLS/MCDA occupation projections and ACR workforce research | Complementary evidence with partly related public inputs; no fully independent causal estimate of AI impact |
| Curriculum/skills bridges | Official occupational evidence plus role-specific professional guidance | Recommendations are analyst proposals; employment effects need local validation |

## Challenges retained

**C01 - Sentiment vintage resolved.** Search retrieval exposed preliminary September sentiment of 47.8. The direct publisher response explicitly identifies final September and gives 48.1. This edition uses the final response, retains its raw hash, and does not average the two. A cached page title alone was not sufficient.

**C02 - Regional comparison resolved by definitions.** Detroit's year-over-year change differs from the median across regions; that is not itself a contradiction. The September 24 unadjusted regional data also differ from September 17 seasonally adjusted estimates. We preserve their separate definitions and do not treat those differences as agency error or combine them into a causal account of workforce departures.

**C03 - Survey wording differs.** The Chicago Fed HTML summary describes activity differently from its September PDF. The dated PDF states near-trend growth; this edition cites that PDF and reports the numeric index without translating it into an employment percentage.

**C04 - County coverage incomplete.** The linked state August county resource returned empty objects despite successful HTTP retrieval. BLS county API data reached July. August county unemployment remains unverified here. HTTP success is not evidence completeness.

**C05 - Projection vintages differ.** The statewide workbook is 2024-34; the Detroit Metro Prosperity Region workbook is 2022-32. Workbook headers were inspected. Neither filename proximity nor the common landing page makes these periods equal.

**C06 - Missing does not mean zero.** BLS source '-' values are retained as null. No interpolation is used. Older university outcomes, BEA prices, housing hardship and other historical baseline inputs were not reharvested or represented as newly verified current values.

## Integrity and reproducibility

The release contains typed observations, selected projection rows, source IDs, URLs, retrieval times, parser versions, original response hashes, public extract hashes and a separate append-only research ledger. Original retrieved pages/workbooks are held in the local immutable research cache. Limited factual extracts and BLS public API responses are distributed; full third-party articles are not republished. A raw response hash identifies exactly the bytes inspected but does not guarantee later retrieval from a changing website.

The research ledger validates retained event continuity and packaged artifact integrity. It is not the operational database ledger, an external timestamp service, or independent proof of statistical truth. The earlier database snapshot is preserved unchanged in its own edition. This session cannot assert a new database audit because its volume was unavailable.

AEE checks explicit claims, supporting evidence, dependencies and recovery needs. AEE does not independently verify every source or turn a proposal into a fact. Initial unsupported assessments and the zero-claim Markdown extraction issue were retained; substantive assessments use structured claim input. Validation evidence and unresolved gaps are in spec 009.

## What remains unknown

Current institution-specific placement/underemployment; local employer skill-gap counts; verified receiving vacancies and wages; actual AI adoption by task; causal displacement estimates; current training capacity/cost/funding; independent local forecasts; and an occupation extinction date. None is filled with a model-generated number. These gaps limit capacity/closure decisions, not the usefulness of a carefully bounded curriculum review.

## Attribution

Original analysis and report design: AXIOVEX / Michigan Workforce Intelligence, CC BY 4.0. Software: MIT. Source facts, data, graphics and provider material retain their own applicable terms. This report is not endorsed by BLS, Michigan agencies, the Federal Reserve, University of Michigan, ACR, SIIM, FDA or any named educational institution. Full repository license scope and provider notices accompany the package.
