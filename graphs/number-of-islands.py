# Pattern: BFS on a 2D grid, multiple BFS calls to count connected components
# Time: O(m * n) where m = rows, n = cols — every cell visited at most once
# Space: O(m * n) for visited set and queue in worst case (entire grid is land)
# Key insight: the outer double for-loop scans every cell. when you hit a '1' that hasn't
#   been visited, that's a new island — increment counter and BFS to mark the entire island
#   as visited. the BFS itself is identical to flood fill (queue + 4-directional offsets +
#   bounds checking + visited set). the difference from flood fill is you're triggering BFS
#   multiple times, once per island.
# Gotchas:
#   - Grid values are strings '1' and '0', not integers — easy to miss in the inner BFS check
#   - Bounds check MUST come before grid access in the if condition or you get index out of
#     range on edge cells
#   - Add starting cell to both queue AND visited before entering the while loop, otherwise
#     you might process it twice
#   - Don't initialize queue with deque([(r,c)]) AND also append (r,c) — that adds the
#     start node twice
# Palantir framing: "this is a connected components counting problem. I'd scan every cell,
#   and when I find unvisited land, that's a new component — I BFS to mark all connected
#   land as visited and increment my count. O(m*n) time and space. if asked to optimize
#   space, I could modify the grid in-place instead of using a visited set, but that mutates
#   the input which I'd flag as a trade-off."

from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        visited = set()
        offset = {(0, 1), (0, -1), (1, 0), (-1, 0)}

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    queue = deque([(r, c)])
                    visited.add((r, c))
                    while queue:
                        cr, cc = queue.popleft()
                        for s, t in offset:
                            nr, nc = cr + s, cc + t
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited and grid[nr][nc] == '1':
                                visited.add((nr, nc))
                                queue.append((nr, nc))

        return islands
