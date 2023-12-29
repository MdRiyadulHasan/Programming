# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        prev = 0
        num = 0
        for ch in s[::-1]:
            val = dic[ch]
            if val<prev:
                num-=val
            else:
                num +=val
            prev = val
        return num
s = "MCMXCIV"
ob = Solution()
result = ob.romanToInt(s)
print(result)
        