from typing import List 
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if k>0 and nums[i]<0:
                nums[i]=-nums[i]
                k-=1
        if k>0 and k%2==1:
            nums.sort()
            nums[0]=-nums[0]
        return sum(nums)
nums = [2,-3,-1,5,-4]
k = 2