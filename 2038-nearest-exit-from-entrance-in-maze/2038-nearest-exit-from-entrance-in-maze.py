from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        directions = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]
        n = len(maze)
        m = len(maze[0])

        q = deque()
        x, y = entrance
        q.append( ((x, y), 0) )
        visited = set()
        visited.add((x, y))

        while q:
            current, step = q.popleft()
            x, y = current
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if not (new_x < 0 or new_x >= n or new_y < 0 or new_y >= m) and maze[new_x][new_y]=='.' and (new_x, new_y) not in visited:
                    if new_x==0 or new_x==n-1 or new_y==0 or new_y==m-1:
                        return step+1
                    q.append( ( (new_x, new_y), step+1) )
                    visited.add( (new_x, new_y) )
        
        return -1

