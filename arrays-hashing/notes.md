# Arrays & Hashing

## Key Ideas

- Use a hash map for O(1) lookup when you need to find pairs/complements in an array
- When you only need to check existence (not store values), use a set instead of a dict

## Common Tricks

- Store the value as key and index as value — lets you look up whether a complement exists and immediately get its index
- `len(nums) != len(set(nums))` is a quick duplicate check but doesn't short-circuit
- `dict.get(key, 0)` replaces if/else for counting — use it every time
- `Counter(s) == Counter(t)` is a one-liner for frequency comparison

## #325 Max Size Subarray Sum Equals k

- **Pattern:** Prefix Sum + Hashmap
- Use a running prefix sum and store first occurrence in a hashmap; check if `prefix - k` exists to find subarrays summing to k
- Time: O(n) | Space: O(n)

## #219 Contains Duplicate II

- **Pattern:** Hashmap with index tracking
- Like Contains Duplicate I (just existence check with a set), but adds a distance constraint — store value → most recent index, check if previous occurrence was within k
- Time: O(n) | Space: O(n)

## Mistakes to Watch For

- Don't store the current number before checking the complement, or you might match an element with itself
- Using a dict when a set is sufficient — interviewers notice when you pick the wrong data structure
