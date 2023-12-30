# https://leetcode.com/problems/maximum-subarray/

from typing import List 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum +=n
            maxSum = max(maxSum, curSum)
            if curSum<0:
                curSum = 0
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
ob = Solution()
result = ob.maxSubArray(nums)
print(result)