# Reading Michigan's labor market beyond the headline rate

## Coverage and interpretation

The review cutoff is September 26, 2026 in Detroit. Publication date, observation period and retrieval time are separate. The latest official monthly observations are not September job counts. A report generated today cannot measure unreported events today.

New public evidence covers Michigan and U.S. August labor conditions, July county and interstate comparisons, a multi-month state underutilization window, second-quarter graduate outcomes, July national labor turnover, September sentiment and official occupational projections. The following generated tables preserve those differences.

## Unemployment, participation and job quality

Michigan's August household statistics show fewer employed residents and a smaller labor force; its employer survey shows a much smaller payroll decline. These surveys cover different populations and concepts: residents versus jobs at establishments, with differences in self-employment, multiple jobholding and geography. Do not subtract the two to create a missing-jobs estimate. The official releases support concern about participation; they do not establish the cause of each departure. [S01, S03]

U-3 measures active unemployment. U-6 also includes marginal attachment and involuntary part-time employment with a broader denominator. The U-6 minus U-3 gap is a percentage-point comparison, not a headcount of hidden unemployed people. For the Michigan window in this release it is **4.1 percentage points**, computed as 9.1 minus 5.0. Both are averages over the same eleven observed months, excluding October 2025; BLS warns against strict comparisons with other windows. [S04]

National involuntary part-time employment, long-term unemployment and people outside the labor force who want a job provide complementary context. These groups overlap with broader measures. National graduate underemployment concerns employed degree holders in jobs that do not normally require a degree; it does not necessarily imply low wages, involuntary part-time work or wasted education. Do not apply the national percentage to a Michigan university's graduates. [S03, S05]

## County conditions and geographic limits

The BLS API returned county unemployment data through July for Macomb, Oakland and Wayne. The state's September 24 release discusses August counties, but its linked county endpoint returned empty records in this retrieval. We therefore publish verified July county values and flag August county detail as missing. The Detroit-Warren-Dearborn MSA is not the three-county total; the Detroit Metro Prosperity Region is another geography. Neither is silently substituted for an individual county. [S02, S20-S23]

Compare unadjusted county rates with unadjusted state rates in the same month and use year-over-year context. A seasonal summer drop does not necessarily show strengthening hiring. State August rates and national seasonally adjusted rates appear in separate tables where necessary. Ohio, California, Texas and Florida are comparison locations, not a counterfactual for Michigan policy. [S21-S28]

## Hiring, sentiment and indirect signals

National July job openings were 7.271 million; the hires, quits and layoffs/discharges rates were 3.2%, 1.9% and 1.0%, respectively, marked preliminary. A stock of openings is not the same as completed hiring. Low layoffs can coexist with difficult job finding, especially for inexperienced entrants. The latter is an interpretation to test, not a Michigan estimate inferred from national data. [S08]

The final September University of Michigan survey shows weaker national sentiment and expectations than August. Direct source retrieval resolved stale search results carrying preliminary numbers. Because this survey covers the United States, its university name must not be mistaken for Michigan geography. Sentiment can respond to prices and politics without producing a proportional change in hiring. [S06]

The Chicago Fed's September district activity index was -5, manufacturing +25 and nonmanufacturing -20. Both hiring indexes remained below zero despite improvement. Its downloadable report describes overall activity as near trend, while the web summary uses different wording; this report follows the dated PDF. Index signs are relative to contacts' historical responses, not employment growth percentages. [S07]

## An early-warning dashboard for Michigan

The following is a proposed monitoring design. Items labeled a gap are not measured in this edition. No unvalidated weighted composite score or recession probability is presented.

| Signal family | What to track and why | Current coverage / interpretation |
| --- | --- | --- |
| Labor availability | Participation, employment/population, prime-age employment, migration, retirements | State headline participation refreshed; prime-age, migration and retirements remain gaps |
| Hiring friction | Hires, openings, quits, vacancy duration, applicant-to-interview conversion | National JOLTS refreshed; Michigan employer-confirmed funnel data missing |
| Hidden slack | U-6, involuntary hours, graduate occupational match, long unemployment spells | Mixed national/state vintages disclosed; county U-6 not available |
| Production demand | Orders, backlog, overtime, temporary help, utilization, supplier cancellations | District survey included; plant-level and Michigan orders series not refreshed |
| Household pressure | Real earnings, rent, childcare, transport, debt delinquency, housing instability | Important constraints; no new comparable local estimates in this edition |
| Restructuring | WARN notices, closures, investment milestones, actual hiring at announced projects | WARN source located; no deduplicated event count or employment impact claimed |
| AI adoption | Task-level deployment, reviewed output quality, labor hours, junior hiring, revenue per worker | Employer measurements required; exposure categories are not adoption rates |
| Education pipeline | Completion, occupational match, paid placements, local retention, wages/hours | Historical repository outcomes remain historical; current local cohort outcomes missing |

Review monthly changes alongside revisions, same-month prior-year values and at least several observations where available. A proposed escalation rule is to convene a sector review when actual hiring weakens alongside reduced hours/orders across repeated observations. Choose thresholds prospectively from historical backtesting and decision costs; they are not established by this report.

## Scenarios through 2027

**Slow adjustment:** Employers adopt AI selectively, preserve headcount and change task mix. Response: paid task redesign, practical AI verification skills and entry-level work experience. Evidence that would challenge this scenario: broad persistent layoffs and falling hours across independent sources.

**Demand downturn plus automation:** Weak orders lead firms to eliminate routine tasks and delay hiring. Response: retain/redeploy before separation, use verified receiving vacancies, resize narrow cohorts, and protect transferable foundations. Trigger evidence must include realized orders/hiring/hours, not sentiment alone.

**Investment-led demand:** Manufacturing, infrastructure or healthcare projects convert into contracts and actual hiring. Response: expand modular training only after confirming milestones, mentors and placement capacity. Announced investment is not an available job.

These are conditional planning scenarios without probabilities. This edition does not issue a new numeric 12-month forecast: the refreshed mixed-frequency set is not a validated forecasting model, and the historical database needed to rerun the earlier model is unavailable. Old reference forecasts are not relabeled as current.

## Michigan industrial application

For Macomb manufacturing and defense suppliers, proposed priorities are equipment reliability, controls, precision inspection and secure engineering workflows. For Oakland's engineering and business employers, focus on verified software/data work and accountable professional services. For Wayne, evaluate production, logistics, healthcare and access constraints together. These are starting hypotheses for local employer interviews, not measured county shortages.

Before claiming a skills shortage, test whether wages, shift patterns, commute, childcare, recruitment rules or poor onboarding explain unfilled roles. Training cannot fix every vacancy. Employer skill-gap counts remain unknown until actual requisitions and assessed worker skills are available.
