# Pattern: XOR (Bit Manipulation)
# Time: O(n) — single pass
# Space: O(1) — just one variable
# Key insight: XOR has three properties that solve this: self-canceling (a ^ a = 0),
#   identity (a ^ 0 = a), and commutativity (order doesn't matter). XOR every number
#   together — all pairs cancel to 0, leaving only the single number.
# How XOR works:
#   - compares bits: returns 1 if different, 0 if same
#   - 5 ^ 3 = 101 ^ 011 = 110 = 6
#   - a ^ a = 0 (any number XORed with itself is 0)
#   - a ^ 0 = a (XORing with 0 changes nothing)
# Walkthrough: [4,1,2,1,2] → 0^4=4, 4^1=5, 5^2=7, 7^1=6, 6^2=4. The 1s and 2s
#   canceled, 4 remains.
# Why not sorting: sort + linear scan works but is O(n log n). problem requires O(n)
#   time and O(1) space.
# Why not hashmap: frequency count works but uses O(n) space. problem requires O(1) space.
# Gotcha: this only works when exactly one element appears once and all others appear
#   exactly twice. variations (single number II, III) need different approaches.
# Palantir framing: "identify the unique signal in a stream of duplicated intercepted transmissions"

class Solution:
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num
        return result
