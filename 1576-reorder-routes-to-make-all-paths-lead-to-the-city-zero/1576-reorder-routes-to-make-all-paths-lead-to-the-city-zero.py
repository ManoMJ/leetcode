from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.result = 0

        def dfs(current, visited):
             for road in graph[current]:
                if road not in visited:
                    if (current, road) in one_way:
                        self.result += 1
                    visited.add(road)
                    dfs(road, visited)

        one_way = set()
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            one_way.add((x, y))
      

        for road in graph[0]: 
            visited = {0, road}
            if (0, road) in one_way:
                self.result += 1
            dfs(road, visited)

        return self.result
        