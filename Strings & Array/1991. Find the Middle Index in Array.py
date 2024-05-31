from typing import List 
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        currentSum = 0
        for i, n in enumerate(nums):
            if currentSum == total-currentSum-n:
                return i
            currentSum+=n 
        return -1
        