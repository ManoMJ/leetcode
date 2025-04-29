from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0]) 
        queue = deque() 
        fresh_count = 0 

        # Step 1: Initialize queue and count fresh oranges 
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r, c, 0)) # (row, col, minute) 
                elif grid[r][c] == 1: 
                    fresh_count += 1 
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        minutes_passed = 0 

        # Step 2: BFS to rot adjacent fresh oranges 
        while queue: 
            r, c, minute = queue.popleft() 
            minutes_passed = minute 

            # update the time 
            for dr, dc in directions: 
                nr, nc = r + dr, c + dc 

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: 
                    grid[nr][nc] = 2 
                    fresh_count -= 1 
                    queue.append((nr, nc, minute + 1)) 

        # Step 3: Check if all fresh oranges are rotted 
        return minutes_passed if fresh_count == 0 else -1