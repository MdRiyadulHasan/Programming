from typing import List 
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        result = [[0]*row for _ in range(col)]  # Create the result matrix with the right dimensions
        
        for r in range(row):
            for c in range(col):
                result[c][r] = matrix[r][c]  # Swap the row and column indices
        return result

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]