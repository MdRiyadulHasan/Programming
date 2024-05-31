from typing import List 
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        currentSum = 0 
        total = sum(nums)
        for i,n in enumerate(nums):
            if currentSum == total-currentSum-n:
                return i 
            currentSum+=n 
        return -1

nums = [1,7,3,6,5,6]