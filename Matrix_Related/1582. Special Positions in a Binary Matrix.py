from typing import List 
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_sum = [sum(row) for row in mat]
        cols_sum = [sum(col) for col in zip(*mat)]
        rows = len(mat)
        cols = len(mat[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==1 and rows_sum[r]==1 and cols_sum[c]==1:
                    count+=1
        return count