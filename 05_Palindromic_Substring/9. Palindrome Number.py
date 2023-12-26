# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome1(self, x: int) -> bool:
        num = x
        result = 0
        while x>0:
            result = result*10+(x%10)
            x = x//10
        return result==num    
    def isPalindrome(self,x: int) -> bool:
        s = str(x)
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l = l+1
            r = r-1
        return True

x = 121
ob = Solution()
result = ob.isPalindrome(x)
print(result)

