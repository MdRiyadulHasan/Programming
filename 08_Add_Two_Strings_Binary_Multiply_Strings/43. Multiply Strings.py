class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str2int(s):
            res = 0
            for ch in s:
                res = res*10 + ord(ch)-ord('0')
            return res

        val1 = str2int(num1)
        val2 = str2int(num2)
        ans = str(val1*val2)
        return ans
ob = Solution()
num1 = "123"
num2 = "456"
result = ob.multiply(num1, num2)
print(result)
