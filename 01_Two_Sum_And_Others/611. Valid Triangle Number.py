# https://leetcode.com/problems/valid-triangle-number/description/
from typing import List 
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range (len(nums)-1, 1, -1):
            l=0
            r = i-1
          
            while l<r:
                
                if nums[l]+nums[r]>nums[i]:
                    count = count + r-l
                    r = r-1
                else:
                    l = l+1
        return count
ob = Solution()
nums = [4,2,3,4]
res = ob.triangleNumber(nums)
print("res", res)