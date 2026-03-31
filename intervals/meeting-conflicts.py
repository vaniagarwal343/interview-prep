# Pattern: Intervals — Overlap Detection
# Time: O(n log n) — dominated by the sort
# Space: O(1) — no extra data structures
# Key insight: after sorting by start time, two consecutive intervals overlap if and only if
#   the next start < current end
# Gotchas:
#   - Sort first, then you only need to compare neighbors — no need for O(n²) pairwise comparison
#   - .sort() returns None — don't assign it
#   - range(len(meetings) - 1) to avoid index out of bounds
#   - Return True when conflict found (early exit), False at the end
# Palantir framing: "detect if any consultant has a scheduling conflict"

def has_conflict(meetings: list[list[int]]) -> bool:
    meetings.sort(key=lambda x: x[0])
    for i in range(len(meetings) - 1):
        if meetings[i + 1][0] < meetings[i][1]:
            return True
    return False
