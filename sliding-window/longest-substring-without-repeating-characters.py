# Pattern: Sliding window with a hashset to track characters in the current window
# Time: O(n) — each character is added and removed from the set at most once
# Space: O(min(n, alphabet_size)) for the set
# Key insight: right pointer expands the window one character at a time. when a duplicate is
#   found, shrink from the left by removing s[left] from the set and incrementing left until
#   the duplicate is gone. window size is always right - left + 1. track the max window size seen.
# Gotchas:
#   - Must remove s[left] from the set when shrinking, not just move left — otherwise the set
#     still thinks the character is in the window
#   - Don't track length with a counter (max_len += 1) — calculate it directly as
#     right - left + 1 and take the max
#   - Update max_len AFTER adding s[right] to the set, not inside the while loop
#   - Works on empty string — returns 0 since the for loop never executes
# Palantir framing: "this is a sliding window problem. I maintain a window of unique
#   characters using a set. I expand right, and when I hit a duplicate, I shrink from the
#   left until the window is valid again. O(n) time since each character enters and leaves
#   the set at most once. if asked to optimize further, I could use a hashmap storing
#   character → last index to jump the left pointer directly instead of shrinking one at a
#   time, going from worst case O(2n) to O(n)."

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
