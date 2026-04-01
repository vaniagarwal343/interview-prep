# Pattern: Sort + Linear Scan
# Time: O(n log n) — dominated by the sort
# Space: O(n) — the converted times list
# Key insight: convert all times to total minutes (h*60 + m), sort them, then the minimum
#   difference must be between two adjacent values. don't forget the wrap-around between
#   the last and first time through midnight.
# How the conversion works:
#   - "HH:MM".split(":") gives ["HH", "MM"]
#   - int(h) * 60 + int(m) converts to total minutes since midnight
#   - 1440 = 24 * 60 = total minutes in a day
# Wrap-around check: (1440 - times[-1]) + times[0] calculates the distance going forward
#   through midnight from the last time to the first time
# Gotchas:
#   - loop goes to len(times) - 1 to avoid index out of bounds on times[i + 1]
#   - wrap-around check goes AFTER the loop, not inside it — it's a single check between
#     the last and first sorted values
#   - duplicate times means answer is 0 (handled naturally by adjacent diff being 0)
# Not an intervals problem — no overlaps or merging. just sorting and comparing neighbors.
# Palantir framing: "find the closest pair of scheduled events across a 24-hour ops cycle"

class Solution:
    def findMinDifference(self, timePoints):
        times = []
        for time in timePoints:
            h, m = time.split(":")
            minutes = int(h) * 60 + int(m)
            times.append(minutes)

        times.sort()

        minimum = float('inf')
        for i in range(len(times) - 1):
            minimum = min(minimum, times[i + 1] - times[i])

        wrap = (1440 - times[-1]) + times[0]
        minimum = min(minimum, wrap)

        return minimum
