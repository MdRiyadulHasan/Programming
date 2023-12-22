# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str2int(s):
            res = 0
            for n in s:
                res = res * 10 + ord(n) - ord('0')
            return res
        
        val1 = str2int(num1)
        val2 = str2int(num2)
        ans = str(val1 * val2)
        return ans

num1 = "123"
num2 = "456"
solution = Solution()
result = solution.multiply(num1,num2)
print(result)
