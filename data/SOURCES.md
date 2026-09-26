# Data Sources and Conventions

## Season summary

`hamilton_seasons.csv` is assembled from season-level Formula 1 records.

Primary/current verification:
- Formula 1 official Lewis Hamilton driver page — current 2026 totals and career totals
- Formula 1 official results archive — historical race results and standings
- Formula 1 official team standings — constructor context

Cross-checks used for season tables:
- GP Rated — season totals, teammate head-to-heads, sprint-inclusive championship points
- Lap Ledger — season wins, podiums and poles

Points convention:
- `championship_points` uses sprint-inclusive championship points where applicable.
- 2026 is incomplete and marked YTD everywhere.

## Recent teammate comparison

`recent_teammate_comparisons.csv` contains season teammate comparisons for 2022–2026.

Race-duel convention:
- if only one teammate is classified, the duel goes to that driver
- if neither is classified, the race does not count
- points include sprint races

Official Formula 1 cross-checks:
- 2025 Ferrari end-of-year report: Leclerc 19–5 Hamilton in Grand Prix qualifying and Leclerc 18–3 Hamilton in comparable race head-to-head
- September 2026 teammate report: Leclerc 7–7 Hamilton in qualifying and Hamilton 8–6 Leclerc in races

## Analysis scope

The finished portfolio analysis is deliberately season-level. It tests the research question using:
- win, podium and pole rates per Grand Prix start
- recent teammate qualifying and race head-to-heads
- teammate-pair championship points share
- constructor championship position as team context

Telemetry and inferred mechanical diagnoses are excluded from the final argument because the available evidence does not support using them consistently across Hamilton's career.

## Image provenance

The site uses reusable Wikimedia Commons photography rather than Getty/F1 image hotlinks.

- Hero: **Lewis Hamilton 2008 Britain.jpg**, Marc Evans, CC BY-SA 2.0.
- Mercedes era: **Lewis Hamilton 2020 Tuscan Grand Prix - race day (cropped).jpg**, Eustace Bagge; crop by Danyele, CC BY-SA 4.0.
- Ferrari era: **2025 ImolaGP Lewis Hamilton.jpg**, Buczkowiak94, CC BY 4.0.

The site applies layout crops, overlays and desaturation for presentation.

## Source cautions

Do not mix:
- Grand Prix-only points with sprint-inclusive championship points
- Grand Prix qualifying with Sprint Qualifying
- teammate head-to-head definitions that handle DNFs differently

The teammate chart is descriptive, not causal. A teammate is a useful same-team benchmark, not a perfect control for setup, strategy, reliability or adaptation.
