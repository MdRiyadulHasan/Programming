# https://leetcode.com/problems/maximum-product-subarray/submissions/

from typing import List 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = maxResult = nums[0]
        for n in nums[1:]:
            if n<0:
                curMax,curMin =curMin, curMax
            curMax = max(n, curMax*n)
            curMin = min(n, curMin*n)
            maxResult = max(maxResult, curMax)
        return maxResult
       
nums = [-2,-40,-5,-3,0,-8,-6,-5,-4,-9]
ob = Solution()
result = ob.maxProduct(nums)
print(result)
