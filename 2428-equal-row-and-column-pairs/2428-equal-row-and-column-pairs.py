class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        columns = [[] for i in range(len(grid)) ]
        
        i = 0
        for row in grid:
            while i < len(grid):
                columns[i].append(row[i])
                i+=1
            i=0
        
        for row in grid:
            for column in columns:
                if row == column:
                    answer += 1
        return answer
            
