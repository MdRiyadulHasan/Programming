# https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import List 
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        if not num:
           ans= [int(d) for d in str(k)]
           return ans 
        result = []
        carry = 0
        for i in range(len(num)-1,-1,-1):
           total = num[i]+carry+(k%10)
           rem = total%10
           carry = total//10
           k = k//10
           result.append(rem)
        while k:
            total = carry+(k%10)
            rem = total%10
            carry = total//10
            k = k//10
            result.append(rem)
        if carry:
            result.append(carry)
        return result[::-1]     
num = [2,7,4] 
k = 181
ob = Solution()
result = ob.addToArrayForm(num,k)
print(result)
