from typing import List 
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums)-1
        while l<r:
            while l<r and nums[l]%2==0:
                l+=1
            while l<r and nums[r]%2==1:
                r-=1
            nums[l], nums[r]=nums[r], nums[l]
        return nums
    # return [x for x in nums if x%2==0]+[x for x in nums if x%2!=0]