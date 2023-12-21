from typing import List 
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        l=0
        count = 0
        if k<=1:
            return 0
        for r in range(len(nums)):
            product*=nums[r]
            while product>=k:
                product//=nums[l]
                l = l+1
            count +=r-l+1
        return count
nums = [10,5,2,6]
k = 100
ob = Solution()
result = ob.numSubarrayProductLessThanK(nums,k) 
print(result)
