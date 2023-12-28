# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        isNegative = False
        if s[0] in ['-','+']:
            if s[0]=='-':
                isNegative = True
            s= s[1:]
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        if isNegative:
            num = -num
        result = min(max(num, -2**31), 2**31-1)
       # nums = max(min(num,2**31-1), -2**31)
        return result
s = "words and 987"
ob = Solution()
result = ob.myAtoi(s)
print(result)