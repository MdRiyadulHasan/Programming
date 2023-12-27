# https://leetcode.com/problems/find-the-middle-index-in-array/description/

from typing import List
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftSum = 0
        for i, n in enumerate(nums):
            if leftSum == total-leftSum-n:
                return i
            leftSum+=n 
        return -1
nums = [2,3,-1,8,4]
ob = Solution()
result = ob.findMiddleIndex(nums)
print(result)