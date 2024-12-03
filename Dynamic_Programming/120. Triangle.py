from typing import List 
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c]+=min(triangle[r+1][c], triangle[r+1][c+1])
        return triangle[0][0]
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11