# https://leetcode.com/problems/add-strings/description/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        result = ""
        while i>=0 or j>=0:
            n1 = int(num1[i]) if i>=0 else 0
            n2 = int(num2[j]) if j>=0 else 0
            addition = n1+n2+carry
            rem = addition%10
            carry = addition//10
            result = str(rem)+result
            i = i-1
            j = j-1
        if carry:
            result = str(carry)+result
        return result
    
    #     def str2int(s):
    #         num = 0
    #         for n in s:
    #             num = num*10+ord(n)-ord('0')
    #         return num
    #     val1 = str2int(num1)
    #     val2 = str2int(num2)
    #     result = str(val1+val2)
    #     return result

num1 = "11"
num2 = "123"
ob = Solution()
ans = ob.addStrings(num1, num2)
print(ans)

