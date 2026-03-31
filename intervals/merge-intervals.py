# Pattern: Intervals — Merge Overlapping
# Time: O(n log n) — dominated by the sort
# Space: O(n) — merged list in worst case stores all intervals
# Key insight: sort by start time, then sweep left to right. only compare against the last
#   interval in merged since everything is sorted.
# Gotchas:
#   - merged must be initialized as [meetings[0]] not meetings[0] — you need a list OF intervals
#   - merged.append([start, end]) not merged.append(start, end) — append takes one argument
#   - Use max(merged[-1][1], end) when extending, not just end — the current interval's end might be shorter
#   - merged[-1] = last interval in list, merged[-1][1] = end of that interval, merged[-1][0] = start of it
#   - .sort() sorts in place and returns None, so don't assign it to a variable
# Palantir framing: "consolidate overlapping consultant meetings into unified busy blocks"

def consolidate_meetings(meetings: list[list[int]]) -> list[list[int]]:
    meetings.sort(key=lambda x: x[0])
    merged = [meetings[0]]
    for start, end in meetings[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
