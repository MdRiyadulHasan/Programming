from typing import List 
class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums):
            dp = [0]* len(nums) 
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i]= max(dp[i-1], dp[i-2]+nums[i])
            return dp[-1]

        n = len(nums) 
        if n==0:
            return 0 
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums) 
        return max(houseRobber(nums[:-1]), houseRobber(nums[1:]))
            
nums = [1,2,3,1]      
        