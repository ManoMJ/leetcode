from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,-1), (0,1), (-1,0), (1,0)]

        answer = 0
        rotten = deque()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==2:
                    rotten.append( (x, y,  0) )
                if not grid[x][y]==0:
                    answer += 1
        
        current = len(rotten)
        minute = 0
        while rotten:
            print(rotten)
            rx, ry, m = rotten.popleft()
            minute = m

            for dx, dy in directions:
                nx, ny = rx + dx, ry + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny]==1:
                    current += 1
                    grid[nx][ny] = 2
                    rotten.append( (nx, ny, m+1) )

    
        return minute if answer == current else -1
                