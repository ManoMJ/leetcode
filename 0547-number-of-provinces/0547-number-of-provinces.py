class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        result = 0
        visited = set()
        for i in range(len(isConnected)):
            stack = [i]
            if i not in visited:
                result += 1
                while stack:
                    top = stack.pop()
                    for j, link in enumerate(isConnected[top]):
                        if link==1 and j not in visited:
                            visited.add(j)
                            stack.append(j)
                
        return result