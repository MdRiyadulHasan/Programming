# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/
class Solution:
    def strStr( self, haystack: str, needle: str) -> int:
        n = len(needle) 
        l = len(haystack)
        for i in range(l-n+1):
            if haystack[i:i+n]==needle:
                return i 
        return -1

haystack = "sabdbutsad"
needle = "sad"
ob = Solution()
result = ob.strStr(haystack, needle)
print(result)
