# Pattern: Topological sort (Kahn's algorithm) — BFS with in-degree tracking for cycle
#   detection in a directed graph
# Time: O(V + E) where V = numCourses, E = len(prerequisites)
# Space: O(V + E) for graph and indegree array
# Key insight: topological sort is just BFS where the queue starts with all nodes that have
#   in-degree 0 (no prerequisites). when you process a node, decrement its neighbors'
#   in-degrees. if a neighbor hits 0, it's now free to process — add to queue. if you
#   process all nodes, no cycle. if not, cycle exists.
# Gotchas:
#   - Read the edge direction carefully — [a, b] means b is a prereq for a, so the edge is
#     b → a, and indegree[a] += 1
#   - The cycle check is len(order) == numCourses, not len(order) == 0 — easy to flip
#   - Use defaultdict(list) for the adjacency list so you don't need to pre-initialize keys
# Palantir framing: "this is a dependency resolution problem — I'd model it as a directed
#   graph and use topological sort via Kahn's algorithm. I start by processing nodes with no
#   dependencies (in-degree 0), then propagate. if I can process all nodes, the dependencies
#   are satisfiable. if not, there's a circular dependency. O(V+E) time and space. if asked
#   for the actual ordering, I just return the order list instead of a boolean — that's
#   Course Schedule II."

from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for prereq, course in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return len(order) == numCourses
