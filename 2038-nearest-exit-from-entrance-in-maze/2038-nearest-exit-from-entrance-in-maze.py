from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(maze), len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1], 0))
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while q:
            x, y, steps = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == '.' and (nx, ny) not in visited:
                    if (nx == 0 or nx == rows - 1 or ny == 0 or ny == cols - 1) and [nx, ny] != entrance:
                        return steps + 1
                    visited.add((nx, ny))
                    q.append((nx, ny, steps + 1))
        return -1
