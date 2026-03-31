# Pattern: Prefix Sum + Hashmap
# Time: O(n) — single pass through array
# Space: O(n) — hashmap stores up to n unique prefix sums
# Key insight: if prefix[j] - prefix[i] = k, then subarray from i+1 to j sums to k
# Gotchas:
#   - Must seed seen = {0: -1} to catch subarrays starting at index 0
#   - Store FIRST occurrence of each prefix sum (not last) because we want longest subarray
#   - Store the INDEX as the value in the hashmap, not k or the element
#   - prefix - k is the complement to look up, not prefix - x
#   - When k = 0, we're looking for two indices with the same prefix sum
#   - If entire array sums to k, the {0: -1} seed gives length i - (-1) = full array
# Palantir framing: "longest consecutive stretch of days where total engagement change was exactly k"

def longest_streak(scores: list[int], k: int) -> int:
    seen = {0: -1}
    prefix = 0
    max_len = 0
    for i, x in enumerate(scores):
        prefix = prefix + x
        if prefix - k in seen:
            if (i - seen[prefix - k]) > max_len:
                max_len = i - seen[prefix - k]
        if prefix not in seen:
            seen[prefix] = i
    return max_len
