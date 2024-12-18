class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        rows = len(text1)
        cols = len(text2)
        dp = [[0]*(cols+1) for _ in range(rows+1) ]
        print (dp)
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if text1[r-1]==text2[c-1]:
                    dp[r][c]=dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[-1][-1]
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  