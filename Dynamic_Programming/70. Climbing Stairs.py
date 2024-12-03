class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
    
        dp = [0] * (n + 1)
        print("dp",dp)
        dp[1], dp[2] = 1, 2
        print(dp)
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
            