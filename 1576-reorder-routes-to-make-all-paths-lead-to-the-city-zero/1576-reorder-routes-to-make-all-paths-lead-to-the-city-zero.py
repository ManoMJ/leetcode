from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.result = 0

        def dfs(current, visited):
             for road in graph[current]:
                if road not in visited:
                    if current not in one_way[road]:
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
            if 0 not in one_way[road]:
                self.result += 1
            dfs(road, visited)

        return self.result
        