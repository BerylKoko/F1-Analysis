# The McQueen Effect — Research Design

## Core question

**Has Lewis Hamilton declined, or are perceptions of decline distorted by the standard set during his dominant years?**

This project separates three things that are easy to collapse into one story:

1. **absolute results** — wins, podiums, poles, championship position
2. **performance relative to the car/team** — teammate qualifying, race and points comparisons
3. **context** — how competitive the car was in each era

The goal is not to prove a predetermined answer. The analysis should show whether Hamilton's post-2021 results look like a steady driver decline, a car-era effect, a teammate-relative decline, an adaptation problem, or some combination of those.

---

## Time periods

These eras are defined from team/regulation context rather than from the results we want to find.

| Era | Seasons | Why it is separate |
|---|---:|---|
| McLaren | 2007–2012 | early-career baseline across strong and weaker McLarens |
| Mercedes transition | 2013 | first Mercedes season before hybrid dominance |
| Mercedes dominant era | 2014–2020 | Mercedes won every Constructors' Championship in this period |
| 2021 title fight | 2021 | competitive title fight rather than the same dominant baseline |
| Ground-effect Mercedes | 2022–2024 | regulation reset; Mercedes no longer the benchmark car |
| Ferrari adaptation | 2025 | first season after twelve years at Mercedes |
| Ferrari 2026 | 2026 YTD | current-season follow-up; keep clearly marked as incomplete |

The primary "dominant baseline" is **2014–2020**, chosen because it corresponds to Mercedes' seven straight Constructors' Championships rather than because it produces the strongest Hamilton numbers.

---

## Metrics

### A. Absolute outcome metrics

These describe what the public sees most often.

- wins per start
- podiums per start
- poles per start
- championship finishing position
- points per start
- average grid position
- average classified finish

Use **rates**, not raw totals, for cross-season comparison because season lengths changed substantially.

These metrics answer:

> Did Hamilton's visible results fall from the dominant-era baseline?

They do **not** answer why.

---

### B. Teammate-relative metrics

These are the most important controls for car performance because teammates share the same team and broadly the same machinery.

#### Qualifying
- qualifying head-to-head win rate
- average qualifying position vs teammate
- median qualifying position vs teammate
- qualifying lap delta to teammate
- **percentage qualifying delta**, not only seconds:
  `(HAM time - teammate time) / teammate time × 100`

Percentage delta is preferred across circuits because a 0.20 s gap means something different on a 60-second lap than on a 110-second lap.

#### Race
- race head-to-head win rate
- average finishing-position delta vs teammate
- teammate points share:
  `Hamilton points / (Hamilton points + teammate points)`
- races finished ahead when both cars are classified
- grid-to-finish position change

These metrics answer:

> Did Hamilton become less competitive even relative to the driver in the same car?

---

### C. Car competitiveness metrics

Absolute results are heavily affected by the car. We need season-level context beside Hamilton's numbers.

Use:

- constructor championship position
- team share of all constructor points
- team wins per race
- team podium rate
- teammate's championship position
- distance from the Constructors' champion where useful

A simple contextual index can combine standardized season-level values, but the raw components should remain visible so the index does not become a black box.

Possible **Car Competitiveness Index**:

`mean(z(constructor rank reversed), z(team win rate), z(team podium rate), z(team points share))`

Use this only as a visual aid; do not treat it as an objective measure of car quality.

---

### D. Conversion / race-execution metrics

These help separate one-lap pace from Sunday execution.

- average positions gained/lost from grid to finish
- share of classified races finishing ahead of starting position
- podium conversion from top-three starts
- win conversion from pole
- points scored when starting outside top five

These can identify seasons where qualifying weakened more than race performance.

---

### E. Reliability / incident controls

Do not count every bad finish as driver performance.

Track separately:

- DNF
- DNS
- DSQ
- obvious mechanical failure
- collision / incident
- races where one teammate did not finish

For teammate race comparisons, show both:

1. **all classified head-to-heads**
2. **clean comparison subset** where both drivers finish and neither has a major mechanical/penalty event

This prevents reliability from quietly driving the result.

---

## Main tests

### Test 1 — The visible decline

Compare Hamilton's season-level win, podium and pole rates against the 2014–2020 baseline.

Expected output:
- career line chart with era shading
- baseline band for 2014–2020

This shows the scale of the headline drop.

### Test 2 — Does the decline remain after controlling for the teammate?

Compare teammate-relative qualifying, race and points performance by season.

This is the most important test.

If absolute results collapse while teammate-relative performance stays strong, the car/context explanation becomes more plausible.

If both absolute and teammate-relative performance decline together, the evidence for a driver-performance decline becomes stronger.

### Test 3 — Qualifying vs race pace

Compare teammate-relative qualifying with teammate-relative race outcomes.

This matters because Hamilton's recent public narrative has often centered on qualifying. A decline concentrated in qualifying is analytically different from a broad race-performance decline.

### Test 4 — Car performance vs Hamilton performance

Plot car competitiveness beside:
- win rate
- podium rate
- teammate points share

Question:

> Do Hamilton's results move with the competitiveness of his team, and where do seasons depart from that relationship?

The interesting seasons are the residuals, not just the trend.

### Test 5 — 2025 vs 2026 Ferrari

Treat 2025 and 2026 separately.

2025 is a poor test of a simple age curve on its own because it combines:
- new team
- new car philosophy
- new engineering environment
- Leclerc as a strong incumbent benchmark

2026 YTD provides a natural follow-up. As of September 2026, official F1 data shows Hamilton third in the championship with 191 points, one Grand Prix win and five Grand Prix podiums, while the official Ferrari head-to-head is 7–7 in qualifying and Hamilton 8–6 ahead in races.

That rebound is worth testing against the simple hypothesis of steady year-by-year decline.

---

## Historical comparison ideas

The project should remain centered on Hamilton, but one contextual comparison can strengthen the analysis.

### Preferred comparison: teammate-adjusted aging

Compare Hamilton's teammate-relative performance after age 35 with a small set of long-career champions who continued into their late 30s or 40s.

Candidates:
- Fernando Alonso
- Michael Schumacher
- Kimi Räikkönen
- Nigel Mansell / Alain Prost if data quality is consistent

Do **not** compare raw wins by age because machinery dominates the result.

Use:
- qualifying teammate win rate
- race teammate win rate
- teammate points share

This is optional and should come after the Hamilton analysis works.

---

## Visual story structure

### 1. The impossible baseline
2014–2020 dominance shown as rates, not a trophy collage.

### 2. The drop
2022–2025 absolute outcomes fall sharply.

### 3. Same car, different question
Introduce teammate-relative analysis.

### 4. Where the decline actually appears
Separate qualifying from race performance.

### 5. The machine changed too
Put Mercedes/Ferrari competitiveness next to Hamilton's outcome metrics.

### 6. Ferrari: 2025 vs 2026
Show the first-year slump and current rebound without treating an incomplete 2026 season as final.

### 7. Answer the question carefully
The conclusion should report which dimensions declined, which recovered, and how much of the visible drop coincided with car/team context.

---

## Rules for the analysis

- do not use raw season totals when a rate is more comparable
- label 2026 as YTD everywhere
- distinguish Grand Prix points from sprint-inclusive championship points
- do not infer mechanical causes from telemetry without evidence
- do not treat a teammate comparison as a perfect car control
- document exclusions for every "clean" race comparison
- never manufacture telemetry or lap deltas
- keep sources attached to each dataset
