from typing import List 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total<abs(target) or (target+total)%2==1:
            return 0
        subset_sum = (total+target)//2   
        dp = [0]*(subset_sum+1)
        dp[0]=1
        for num in nums:
            for i in range(subset_sum, num-1, -1):
                dp[i]+=dp[i-num] 
        return dp[-1]
nums = [2, 3, 5, 6, 8, 10]
target = 10
