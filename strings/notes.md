# Strings

## Core Sub-Patterns

- **Substring search:** sliding window over string, compare slices. Pick when looking for occurrences of a pattern within a larger string.
- **Two pointer on strings:** palindrome checks, comparing from both ends. Pick when the problem involves symmetry, reversal, or shrinking a window inward.
- **Hashmap for strings:** anagram detection, frequency counting. Pick when the problem involves character frequencies, permutations, or matching unordered content.
- **String + binary search:** when positions are sorted and you need proximity checks. Pick when you have sorted indices and need to find the closest match efficiently.

## #3006 Find Beautiful Indices

- **Pattern:** String Matching + Proximity Check
- Find all positions of a and b, then check if any a-position has a b-position within k distance
- Time: O(n * m + A * B) | Space: O(A + B)
