# Binary Search

## Core Sub-Patterns

- **Classic binary search:** find exact target in sorted array. `lo <= hi`, check `mid`, move `lo` or `hi`.
- **Boundary search (leftmost/rightmost):** find first or last position satisfying a condition. Save candidate answer when condition is met, keep searching in the direction of a better answer.
- **Search on answer:** binary search on the answer space itself (e.g., minimum capacity, maximum distance). Pair with a feasibility check function.

## #981 Time Based Key-Value Store

- **Pattern:** Hashmap + binary search (boundary search for rightmost timestamp ≤ target)
- Timestamps come in sorted order for free. set is O(1) append, get is O(log n) binary search.
- Time: O(1) set / O(log n) get | Space: O(total set calls)
