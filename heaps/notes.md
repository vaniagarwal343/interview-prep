# Heaps

## Core Sub-Patterns

- **Min heap:** get the smallest of k things efficiently. Use for merge k streams, kth smallest. Pick when you repeatedly need the minimum from a changing set.
- **Max heap:** get the largest. In Python, negate values since `heapq` is min-only. Pick when you need the maximum and the set is changing.
- **Top-k:** push all, keep heap size at k. O(n log k). Pick when the problem asks for the k largest/smallest/most frequent elements.
- **Two heaps:** median finding. Max heap for lower half, min heap for upper half. Pick when you need a running median or need to balance two halves of a stream.

## #23 Merge K Sorted Lists

- **Pattern:** Min Heap (Priority Queue)
- Push head of each list onto heap, pop smallest, push its .next, repeat until empty
- Time: O(N log k) | Space: O(k)
