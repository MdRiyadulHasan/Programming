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
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3