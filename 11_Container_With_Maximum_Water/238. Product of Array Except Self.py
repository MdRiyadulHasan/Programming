# https://leetcode.com/problems/product-of-array-except-self/

from typing import List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        leftProduct = 1
        rightProduct = 1 
        for i in range(n):
            result[i]*=leftProduct
            leftProduct*=nums[i]
        for i in range(n-1,-1,-1):
            result[i]*=rightProduct
            rightProduct*=nums[i]
        return result
ob = Solution()      
nums = [1, 2, 3, 4]
result = ob.productExceptSelf(nums)
print(result)
