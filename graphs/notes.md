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

## #733 Flood Fill

- **Pattern:** BFS on a 2D grid
- Grid cells are the graph — use 4-directional offsets instead of adjacency list. Save original color before BFS starts.
- Time: O(m * n) | Space: O(m * n)

## #200 Number of Islands

- **Pattern:** BFS on a 2D grid, multiple BFS calls to count connected components
- Outer loop scans every cell; each unvisited '1' triggers a BFS that marks the whole island. Same BFS as flood fill, just called multiple times.
- Time: O(m * n) | Space: O(m * n)

## #207 Course Schedule

- **Pattern:** Topological sort (Kahn's algorithm) — BFS with in-degree tracking for cycle detection
- Queue starts with in-degree 0 nodes; process a node, decrement neighbors' in-degrees, add to queue when they hit 0. If all nodes processed, no cycle.
- Time: O(V + E) | Space: O(V + E)
