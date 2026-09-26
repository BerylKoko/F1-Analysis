# The McQueen Effect

**Has Lewis Hamilton declined, or are perceptions of decline distorted by the standard set during his dominant years?**

An interactive career data story examining Lewis Hamilton from 2007 through the 2026 season-to-date. The project separates absolute results from teammate-relative performance and team competitiveness instead of treating wins as a direct proxy for driver ability.

## What the analysis finds

Hamilton’s visible results have declined substantially from the 2014–2020 Mercedes baseline. Across that seven-season period he won 73 of 137 starts (53.3%), finished on the podium in 111 (81.0%), and took 67 poles (48.9%).

But the post-2021 record does not form a clean, monotonic decline. Mercedes fell from Constructors’ champion in 2021 to P3, P2 and P4 in 2022–2024. Hamilton’s teammate-relative performance also moves unevenly: 2025 was a clear low point against Charles Leclerc, while 2026 YTD has rebounded to 7–7 in qualifying and 8–6 in race head-to-heads.

The conclusion is deliberately narrower than “Hamilton has not declined”: some dimensions have declined, especially recent qualifying performance, but peak-era dominance is not a neutral baseline and absolute results are strongly entangled with machinery and adaptation.

## Repository

- `index.html` — interactive visual data story
- `style.css` — editorial/scroll-driven presentation
- `analysis.js` — chart data and interactions
- `analysis.py` — reproducible season-level calculations
- `data/hamilton_seasons.csv` — career season summary
- `data/recent_teammate_comparisons.csv` — 2022–2026 teammate comparison
- `data/SOURCES.md` — source conventions
- `research/RESEARCH_DESIGN.md` — research design and metric rationale

## Method

1. Convert wins, podiums and poles to rates per Grand Prix start so seasons of different lengths are comparable.
2. Use 2014–2020 as the dominant-era baseline because Mercedes won seven consecutive Constructors’ Championships in those seasons.
3. Compare recent seasons with the teammate in the same team using qualifying H2H, race H2H and teammate-pair points share.
4. Put team championship position beside Hamilton’s outcomes to avoid reading car-dependent results as driver-only effects.
5. Mark 2026 as YTD and keep head-to-head conventions explicit.

## Sources and image provenance

Primary current and historical verification uses Formula 1’s official results archive and driver/team reports. The hero image is Marc Evans' 2008 British GP photograph (CC BY-SA 2.0). The 2020 W11 image is by Eustace Bagge, cropped by Danyele (CC BY-SA 4.0). The 2025 Ferrari image is by Buczkowiak94 (CC BY 4.0). Full data conventions are in `data/SOURCES.md`.

Beryl Koko · Cornell Information Science
