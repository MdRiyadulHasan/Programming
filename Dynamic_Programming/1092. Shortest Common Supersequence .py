class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        rows = len(str1)
        cols = len(str2)
        dp = [[0]*(cols+1) for _ in range(rows+1) ]
        print (dp)
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                if str1[r-1]==str2[c-1]:
                    dp[r][c]=dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        scs =[]
        i = rows
        j = cols
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                scs.append(str1[i-1])
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                scs.append(str1[i-1])
                i-=1
            else:
                scs.append(str2[j-1])
                j-=1
        while i>0:
            scs.append(str1[i-1])
            i-=1
        while j>0:
            scs.append(str2[j-1])
            j-=1
        return "".join(reversed(scs))
        

# Input: str1 = "abac", str2 = "cab"
# Output: "cabac"