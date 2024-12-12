from typing import List 
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        row_sum_one = [sum(row) for row in grid]
        col_sum_one = [sum(col) for col in zip(*grid)]
        row = len(grid)
        col = len(grid[0])
        new_mat =[[0]*col for _ in range(row)]
        print(new_mat)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                new_mat[r][c]=2*row_sum_one[r]-row+2*col_sum_one[c]-col
        return new_mat 
# Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
# Output: [[0,0,4],[0,0,4],[-2,-2,2]]