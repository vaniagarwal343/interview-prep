# Arrays & Hashing

## Key Ideas

- Use a hash map for O(1) lookup when you need to find pairs/complements in an array
- When you only need to check existence (not store values), use a set instead of a dict

## Common Tricks

- Store the value as key and index as value — lets you look up whether a complement exists and immediately get its index
- `len(nums) != len(set(nums))` is a quick duplicate check but doesn't short-circuit
- `dict.get(key, 0)` replaces if/else for counting — use it every time
- `Counter(s) == Counter(t)` is a one-liner for frequency comparison

## Mistakes to Watch For

- Don't store the current number before checking the complement, or you might match an element with itself
- Using a dict when a set is sufficient — interviewers notice when you pick the wrong data structure
