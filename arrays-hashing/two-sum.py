# Problem: Two Sum (#1)
# Link: https://leetcode.com/problems/two-sum/
# Pattern: hash map lookup
# Insight: for each number, check if its complement (target - num) is already
#          in the map. if not, store current number and index.
# Time: O(n), Space: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return (i, d[diff])
            d[num] = i
