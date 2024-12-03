from typing import List 
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        max_nums = max(nums)
        dp = [0]*(max_nums+1)
        dp[1] = count[1]*1
        for i in range(2, max_nums+1):
            dp[i] = max(dp[i-1], dp[i-2]+i*count[i])
        return max(dp)
# Input: nums = [2,2,3,3,3,4]
# Output: 9