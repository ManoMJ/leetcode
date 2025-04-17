from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Store directed roads for fast lookup
        directed = set ((a, b) for a, b in connections)

        # Undirected graph representation
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):
            nonlocal count
            for neighbor in graph[node]:
                if neighbor != parent:
                    if (node, neighbor) in directed:
                        count += 1
                    dfs(neighbor, node)

        count = 0
        dfs(0, -1)
        return count