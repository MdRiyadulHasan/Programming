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
# nums = [1, -2, -3, 4, -1, 2, 1, -5, 4, 6]
nums = [2,3,-2,4, -5]
ob = Solution()
ans = ob.maxProduct(nums)
print(ans)