# https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL = s[l+1:r+1]
                skipR = s[l:r]
                return (skipL==skipL[::-1] or skipR==skipR[::-1])
            l=l+1
            r= r-1
        return True
s = "abca"
ob = Solution()
result = ob.validPalindrome(s)
print(result)