# Sliding Window

## Core Sub-Patterns

- **Fixed-size window:** window size is given (e.g., max sum of subarray of size k). Expand right, shrink left when window exceeds size. No condition to check — just maintain the size.
- **Variable-size window (shrink when invalid):** expand right until window becomes invalid, then shrink from left until it's valid again. Track the max/min valid window size. Classic signal: "longest/shortest substring/subarray with [constraint]".
- **Variable-size window (hashmap counting):** same as above but use a hashmap to count elements in the window. Useful when the constraint involves frequencies (e.g., "at most k distinct characters").

## #3 Longest Substring Without Repeating Characters

- **Pattern:** Variable-size sliding window with hashset
- Expand right, shrink left when duplicate found (remove s[left] from set), track max window size as right - left + 1.
- Time: O(n) | Space: O(min(n, alphabet_size))
