class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor]==1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        n = len(isConnected)
        visited = set()
        provinces = 0

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs(city)
                provinces += 1

        return provinces