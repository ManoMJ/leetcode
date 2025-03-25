from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        unique_rows = Counter(tuple(row) for row in grid)
        transposed = Counter(list(zip(*grid)))

        result = 0
        for row in unique_rows.keys():
            if row in transposed:
                result += (unique_rows[row] * transposed[row])
        return result
