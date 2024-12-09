from typing import List 
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for r in range(rows):
            for c in  range(cols):
                if matrix[r][c]==row_min[r] and matrix[r][c]==col_max[c]:
                    result.append(matrix[r][c])
        return result
# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]