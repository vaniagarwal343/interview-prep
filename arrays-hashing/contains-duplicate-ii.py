# Pattern: Hashmap — "have I seen this before?" with index tracking
# Time: O(n) — single pass
# Space: O(n) — hashmap storing value → last index
# Key insight: this is Contains Duplicate I but with a distance constraint. instead of just
#   checking if a value exists, also check if the previous occurrence was within k positions.
# How it works:
#   - seen maps each value to the most recent index where it appeared
#   - for each number, check two things: (1) have I seen it before? (2) was it within k?
#   - if both true, return True immediately
#   - always update seen[num] = i so we track the most recent index
# Gotcha: seen[num] = i must be INSIDE the for loop (same indentation as the if). if it's
#   outside, you only record the last element's index and miss everything else.
# Why store last index only: if a value appears at indices 2, 7, 15 and k=5, we only care
#   about the closest previous occurrence. if 15-7 > k, then 15-2 > k too. so we only need
#   the most recent one.
# Palantir framing: "detect repeated access attempts within a k-second window"

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
        return False
