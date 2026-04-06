# Pattern: BFS on a 2D grid
# Time: O(m * n) where m = rows, n = cols
# Space: O(m * n) for visited set and queue
# Key insight: grid cells ARE the graph — neighbors are implicit via 4-directional offsets
#   (up/down/left/right), no need to build an adjacency list. Save the original color before
#   BFS starts so comparisons aren't corrupted by recoloring.
# How BFS works on a grid:
#   - queue (deque with popleft for O(1)), visited set to avoid cycles, process level by level
#   - for grid problems, replace adjacency list lookup with 4-directional offset loop
#   - multi-source BFS is the same pattern but push all starting nodes into the queue at once
# Gotchas:
#   - Must bounds-check BEFORE accessing image[nr][nc] or it crashes on edge pixels
#   - Save original color once outside the loop — if you capture it inside, it's already been changed
#   - image[r][c] not image[r, c] — python 2D lists use double brackets
#   - If original color == new color, BFS still works but you can short-circuit with an early
#     return for optimization
# Palantir framing: "this is a connected components problem on a grid. I'd use BFS because
#   we're exploring all reachable cells from a starting point. the grid itself serves as the
#   graph — each cell's neighbors are the 4 adjacent cells. time and space are both O(m*n)
#   in the worst case where the entire grid is one color."

from collections import deque

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        visited = {(sr, sc)}
        queue = deque([(sr, sc)])
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        original = image[sr][sc]

        while queue:
            r, c = queue.popleft()
            image[r][c] = color
            for dr, dc in offsets:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and (nr, nc) not in visited and image[nr][nc] == original:
                    visited.add((nr, nc))
                    queue.append((nr, nc))
                    image[nr][nc] = color

        return image
