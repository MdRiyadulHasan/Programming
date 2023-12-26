# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = float("-inf")
        for i in range(len(s)):
            l = i 
            r = i 
            while l>=0 and r < len(s) and s[l]== s[r]:
                if maxLen<r-l+1:
                    maxLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r < len(s) and s[l]== s[r]:
                if maxLen<r-l+1:
                    maxLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res
    

s = "cbbd"
ob = Solution()
result = ob.longestPalindrome(s)
print(result)
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"