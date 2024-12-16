from typing import List 
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        rows = len(mat)
        cols = len(mat[0])
        result = []
        diagonals = {}
        for r in range(rows):
            for c in range(cols):
                if r+c not in diagonals:
                    diagonals[r+c]=[]
                diagonals[r+c].append(mat[r][c])
        for k in range(rows+cols-1):
            if k%2==0:
                result.extend(reversed(diagonals[k]))
            else:
                result.extend(diagonals[k])
        return result
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,4,7,5,3,6,8,9]
