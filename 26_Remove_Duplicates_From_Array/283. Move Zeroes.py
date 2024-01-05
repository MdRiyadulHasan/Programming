# https://leetcode.com/problems/move-zeroes/

from typing import List 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[start], nums[i] = nums[i],nums[start]
                start+=1
        return nums 
ob = Solution()
nums = [0,1,0,3,12]
result = ob.moveZeroes(nums)
print(result)