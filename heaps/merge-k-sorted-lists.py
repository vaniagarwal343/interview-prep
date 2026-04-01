# Pattern: Min Heap (Priority Queue)
# Time: O(N log k) where N is total nodes across all lists, k is number of lists
# Space: O(k) — heap only holds one node per list at any time
# Key insight: all k lists are already sorted. don't throw that away by dumping everything
#   and re-sorting. instead, only compare the "fronts" of each list. the heap efficiently
#   picks the smallest front out of k candidates.
# How the heap works here:
#   - push the head of each list onto the heap at the start — these are your initial "fronts"
#   - pop the smallest front, attach it to your result
#   - that list now has a new front (node.next) — push it onto the heap
#   - repeat until heap is empty
# Tuple format: (node.val, counter, node)
#   - node.val: what the heap sorts by
#   - counter: tiebreaker so Python never compares ListNode objects (they're not comparable,
#     it'll crash)
#   - node: the actual object so we can access .next after popping
# Dummy node pattern: dummy = ListNode(0) is a fake head. tail tracks where to append.
#   avoids special-casing "is this the first node?" return dummy.next at the end.
# Gotchas:
#   - must check if node: before pushing — lists can contain None
#   - must increment counter every time you push, not just in the initial loop
#   - don't forget tail = tail.next after attaching — otherwise you keep overwriting the same spot
# Brute force alternative: dump all values into a list, sort, rebuild linked list. O(N log N).
#   valid first answer in interview but say why it's suboptimal.
# Still learning: linked list mechanics were the hard part, not the heap. need to internalize
#   that linked lists aren't iterable with for loops — you traverse with .next.
# Palantir framing: "merge k sorted intelligence feeds into a single prioritized stream"

import heapq

def merge_k_lists(lists):
    heap = []
    dummy = ListNode(0)
    tail = dummy
    counter = 0

    for node in lists:
        if node:
            heapq.heappush(heap, (node.val, counter, node))
            counter += 1

    while heap:
        val, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, counter, node.next))
            counter += 1

    return dummy.next
