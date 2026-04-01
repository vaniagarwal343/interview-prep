# Pattern: String Matching + Proximity Check
# Time: O(n * m + A * B) where n is len(s), m is max(len(a), len(b)), A and B are number
#   of matches. brute force but passes.
# Space: O(A + B) — storing positions of a and b matches
# Key insight: break the problem into three simple steps: (1) find all positions where a
#   appears, (2) find all positions where b appears, (3) for each a-position, check if any
#   b-position is within k distance.
# How substring matching works:
#   - slide through s one position at a time
#   - at each position i, slice s[i:i+len(a)] and compare to a
#   - range goes to len(s) - len(a) + 1 to avoid slicing past the end
# Gotcha: when finding b positions, slice with len(b) not len(a). copy-paste bug that's
#   easy to miss — cost me a wrong answer.
# The break is important: once you find ANY b-position within k, this a-position is
#   beautiful. don't keep checking or you'll add duplicates.
# Optimization: since both a_pos and b_pos are sorted, you could binary search b_pos for
#   each a-position instead of the inner loop. would reduce to O(A log B).
# Palantir framing: "flag locations in intercepted text where two keywords appear within k
#   characters of each other"

class Solution:
    def beautifulIndices(self, s, a, b, k):
        a_pos = []
        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                a_pos.append(i)

        b_pos = []
        for i in range(len(s) - len(b) + 1):
            if s[i:i+len(b)] == b:
                b_pos.append(i)

        result = []
        for i in a_pos:
            for j in b_pos:
                if abs(i - j) <= k:
                    result.append(i)
                    break

        return result
