from typing import List 
from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows = [tuple(row) for row in grid]
        cols = [tuple(col) for col in zip(*grid)]
        # cols = [tuple(grid[i][j] for i in range(n)) for j in range(n)]
        row_count = Counter(rows)
        col_count = Counter(cols)
        result = 0
        for row, count in row_count.items():
            result+=count*col_count.get(row,0)
        return result