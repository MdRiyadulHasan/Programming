# https://leetcode.com/problems/longest-palindromic-subsequence/description/
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        L = len(s)
        dp = [[0]*L for _ in range(L)]
        for i in range(L-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,L):
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]= max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
s = "agbdba"
ob = Solution()
result = ob.longestPalindromeSubseq(s)
print(result)