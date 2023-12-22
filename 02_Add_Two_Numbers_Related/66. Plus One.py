# https://leetcode.com/problems/plus-one/description/

from typing import List 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            total = digits[i]+carry
            carry = total//10
            digits[i] = total%10
            if total<10:
                return digits        
        if carry:
            digits.insert(0, carry)
        return digits
    
digits = [4,3,2,1]
ob = Solution()
result = ob.plusOne(digits)
print(result)