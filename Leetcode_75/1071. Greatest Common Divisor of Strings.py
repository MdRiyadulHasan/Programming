# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a,b):
            while b:
                a,b = b,a%b 
            return a 
        if str1+str2 != str2+str1:
            return ""
        gcdLength = gcd(len(str1), len(str2))
        return str1[:gcdLength]
str1 = "ABABAB"
str2 = "ABAB"
ob = Solution()
result = ob.gcdOfStrings(str1, str2)
print(result)
