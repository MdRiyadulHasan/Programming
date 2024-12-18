class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows = len(word1)
        cols = len(word2)
        dp = [[0]*(cols+1) for _ in range(rows+1) ]
        print (dp)
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if word1[r-1]==word2[c-1]:
                    dp[r][c]=dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        lcs_len = dp[-1][-1]
        return rows+cols-2*(lcs_len)
# Input: word1 = "sea", word2 = "eat"
# Output: 2
