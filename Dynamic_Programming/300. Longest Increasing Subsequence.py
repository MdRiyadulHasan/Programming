from typing import List 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
  
nums = [10,9,2,5,3,7,101,18]
nums = [1, 2, 1, 4, 6]