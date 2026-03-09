# Problem: Valid Anagram (#242)
# Link: https://leetcode.com/problems/valid-anagram/
# Pattern: frequency counting
# Insight: count character frequencies in first string, decrement with second
#          string, check if all counts are zero. early exit if lengths differ.
#          one-liner: Counter(s) == Counter(t)
# Time: O(n), Space: O(n) where n is length of strings
# Pythonic tip: use dict.get(key, 0) instead of if/else for building count dicts

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for c in s:
            seen[c] = seen.get(c, 0) + 1
        for c in t:
            seen[c] = seen.get(c, 0) - 1
        for k in seen:
            if seen[k] != 0:
                return False
        return True
