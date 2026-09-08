# Lap / Compare (F1-Analysis rehabilitation)

Compare historical fastest-race-lap telemetry: speed, throttle, braking and relative elapsed time at a shared distance. Python/FastF1 exports versioned JSON; React/TypeScript provides driver selection, keyboard inspection and a numeric data table.

The original Lewis Hamilton **McQueen Effect** concept remains project history. This tool does not diagnose driver decline or attribute a cause to telemetry differences.

## Run

```sh
npm ci
npm run dev
```

The committed Monza 2025 and Silverstone 2024 snapshots work without an API connection. See `telemetry.py --help` to regenerate data after installing requirements.txt. No live-race claims are made.

## Verify

```sh
npm run build
node --test tests/telemetry.test.mjs
```

## Interpretation

The relative time-gap trace aligns sample clocks at the first shared distance. It is an interpolated estimate, not official timing. Fastest race laps may have different tyres, fuel loads and traffic. Sector boundaries are not in these snapshots and are not drawn.

See docs/BEFORE.md, CHANGELOG.md, ARCHITECTURE.md and INTERVIEW.md for the original work, AI-assisted changes and interview preparation. The rehabilitation branch is separate from main. No public deployment is claimed.
