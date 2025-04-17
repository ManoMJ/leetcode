from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        self.result = 0

        def dfs(current, parent):
             for road in graph[current]:
                if road != parent:
                    if (current, road) in one_way:
                        self.result += 1
                    dfs(road, current)

        one_way = set()
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            one_way.add( (x, y) )
      
        dfs(0, -1)

        return self.result
        