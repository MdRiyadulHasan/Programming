from typing import List 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        r = 0
        c = col-1
        while r<row and c>=0:
            if matrix[r][c]==target:
                return True
            elif matrix[r][c]<target:
                r = r+1
            else:
                c = c-1
        return False
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20