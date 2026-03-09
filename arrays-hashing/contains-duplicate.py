# Problem: Contains Duplicate (#217)
# Link: https://leetcode.com/problems/contains-duplicate/
# Pattern: hash set lookup
# Insight: use a set to track seen numbers. if a number is already in the set,
#          there's a duplicate.
# Time: O(n), Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
