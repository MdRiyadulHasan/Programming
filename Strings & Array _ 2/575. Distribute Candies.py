from typing import List
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        maxAllowed = n//2
        minCandyLength = len(set(candyType))
        return min(maxAllowed, minCandyLength)
        

# Input: candyType = [1,1,2,2,3,3]
# Output: 3