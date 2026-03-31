# Intervals

## Core Sub-Patterns

- **Merge overlapping:** sort, sweep, extend or add
- **Sweep line:** turn intervals into +1/-1 events, sort, count (for "how many overlap at once" problems)

## #56 Merge Intervals

- **Pattern:** Intervals — Merge Overlapping
- Sort by start time, sweep left to right, extend last merged interval or append a new one
- Time: O(n log n) | Space: O(n)

## #252 Meeting Conflicts

- **Pattern:** Intervals — Overlap Detection
- Sort by start time, check if any next start < current end
- Time: O(n log n) | Space: O(1)
