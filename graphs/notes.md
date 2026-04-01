# Graphs

## Core Sub-Patterns

- **BFS:** shortest path, minimum steps. Uses a queue. Pick when the problem asks for fewest moves, closest node, or level-order traversal.
- **DFS:** connectivity, cycle detection, path finding. Uses recursion or stack. Pick when the problem asks "is there a path", "find all paths", or needs to explore deeply before backtracking.
- **Topological sort:** dependency ordering on DAGs. Uses indegree + queue (Kahn's algorithm). Pick when the problem says "order these given dependencies" or "can this schedule work".
- **Union find:** grouping, connectivity checks. Uses parent dict + find/union. Pick when the problem asks "how many groups", "are these connected", or "merge these sets". Best when you only care about whether nodes are in the same group, not the path between them.

## #721 Accounts Merge

- **Pattern:** Union Find (Disjoint Set)
- Union emails within each account, group by root, attach names at the end
- Time: O(n * α(n)) ≈ O(n) | Space: O(n)
