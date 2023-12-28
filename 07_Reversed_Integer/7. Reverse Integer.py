# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        negattive = False
        if x<0:
            negattive = True
            x = -x
        s = str(x)
        rev = s[::-1]
        x = int(rev)
        if negattive:
            x = -x 
        if x<-2**31 or x>2**31-1:
            return 0
        return x
x = 123
ob = Solution()
result = ob.reverse(x)
print(result)
