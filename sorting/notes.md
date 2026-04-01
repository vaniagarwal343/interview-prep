# Sorting

## Core Sub-Patterns

- **Sort + linear scan:** when the answer involves adjacent or nearby elements. Sort first, then one pass comparing neighbors. Pick when the problem asks for closest pair, minimum difference, or duplicate detection.
- **Sort + two pointers:** when looking for pairs with a target property. Sort first, then use left/right pointers moving inward. Pick when the problem asks for pairs summing to a target, triplets, or container problems.
- **Bucket sort:** when values are bounded (e.g. 1440 minutes in a day — this problem could also be solved with a boolean bucket of size 1440). O(n) time but O(range) space. Pick when the value range is small and known.

## #539 Minimum Time Difference

- **Pattern:** Sort + Linear Scan
- Convert times to minutes, sort, compare adjacent pairs + wrap-around through midnight
- Time: O(n log n) | Space: O(n)
