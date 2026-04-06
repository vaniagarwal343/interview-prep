# Pattern: Hashmap + binary search. Hashmap stores key → sorted list of (timestamp, value)
#   pairs. Binary search finds the largest timestamp ≤ given timestamp.
# Time: set is O(1) amortized (just append). get is O(log n) where n = entries for that key.
# Space: O(total number of set calls)
# Key insight: since timestamps are guaranteed to be strictly increasing per key, the list is
#   always sorted for free — no need to sort on insert. the get operation is "find rightmost
#   value where timestamp ≤ target" which is a classic binary search boundary problem. save
#   the candidate answer when values[mid][0] ≤ timestamp and keep searching right for a
#   potentially better one.
# Gotchas:
#   - Check if key exists before accessing self.store[key] or it crashes
#   - append takes a tuple as one argument: append((timestamp, value)) not append(timestamp, value)
#   - Use self.store everywhere inside methods, not just store
#   - When values[mid][0] ≤ timestamp, save result BUT move lo = mid + 1 to keep searching —
#     the first valid answer isn't necessarily the best one
#   - Return "" if key doesn't exist or no timestamp is ≤ given timestamp
# Palantir framing: "set is O(1) since timestamps come in order. a naive get would linear
#   scan for O(n). since the list is sorted by timestamp, binary search gives us O(log n).
#   the trade-off is we're storing all historical values which uses more memory, but it gives
#   us fast lookups at any point in time. if asked about concurrent access, I'd discuss
#   read-write locks on per-key granularity."

class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]
        lo, hi = 0, len(values) - 1
        result = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return result
