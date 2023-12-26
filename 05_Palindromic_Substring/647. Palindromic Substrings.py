# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l = l-1
                r = r+1
            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                l=l-1
                r =r+1
        return count
s = "abc"
ob = Solution()
result = ob.countSubstrings(s)
print(result)
