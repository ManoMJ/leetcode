from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.result = 0

        def dfs(current, visited):
             for road in graph[current]:
                if road not in visited:
                    if road in one_way[current]:
                        self.result += 1
                    visited.add(road)
                    dfs(road, visited)

        one_way = defaultdict(list)
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            one_way[x].append(y)
      

        for road in graph[0]: 
            visited = {0, road}
            if [road, 0] not in connections:
                self.result += 1
            dfs(road, visited)

        return self.result
        