from typing import List 
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        maxCount = 0 
        for r,n in enumerate((nums)):
            if n==1:
                maxCount = max(maxCount, r-l+1)
            else:
                l = r+1
nums = [1,1,0,1,1,1]