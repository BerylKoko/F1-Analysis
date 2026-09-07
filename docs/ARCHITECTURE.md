# Architecture

FastF1 exports versioned JSON; React/TypeScript renders it without a runtime Python dependency. Continuous values use linear interpolation; braking uses nearest sample. Relative elapsed time subtracts each driver’s time at the common start. This estimate is NOT the official lap delta.
