class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1  # Special case: 2 → 1, 3 → 2
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        
        return dp[n]