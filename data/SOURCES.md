# Data Sources

## Season summary

`hamilton_seasons.csv` is assembled from season-level Formula 1 records.

Primary/current verification:
- Formula 1 official Lewis Hamilton driver page — current 2026 totals and career totals
- Formula 1 official results archive — historical race results and standings

Cross-checks used for season tables:
- GP Rated — season totals, teammate head-to-heads, sprint-inclusive championship points
- Lap Ledger — season wins, podiums and poles

Points convention:
- `championship_points` uses sprint-inclusive championship points where applicable.
- 2026 is incomplete and marked YTD.

## Recent teammate comparison

`recent_teammate_comparisons.csv` uses GP Rated's season teammate tables for 2022–2026.

Race-duel convention from that source:
- if only one teammate is classified, the duel goes to that driver
- if neither is classified, the race does not count
- points include sprint races

Official F1 cross-checks:
- 2025 Ferrari end-of-year report: Leclerc 19–5 Hamilton in Grand Prix qualifying and Leclerc 18–3 Hamilton in comparable race head-to-head
- September 2026 F1 teammate report: Leclerc 7–7 Hamilton in qualifying and Hamilton 8–6 Leclerc in races

## Next raw dataset

For race-level and qualifying-time analysis, collect:

- season
- round
- circuit
- driver
- teammate
- constructor
- qualifying position
- best comparable qualifying time
- grid
- finish
- classification status
- points
- sprint points
- DNF / DNS / DSQ flags

Use official F1 result tables and FastF1 where coverage is reliable.

## Source cautions

Do not mix:
- Grand Prix-only points with sprint-inclusive championship points
- Grand Prix qualifying with Sprint Qualifying
- teammate head-to-head definitions that handle DNFs differently

Every final chart should state its convention.
