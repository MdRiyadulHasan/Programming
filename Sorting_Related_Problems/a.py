from typing import List 
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r = len(nums)-1
        current = 0
        while current<=r:
            if nums[current]==0:
                nums[l],nums[current]=nums[current], nums[l]
                l+=1
                current+=1
            elif nums[current]==2:
                nums[r], nums[current]=nums[current], nums[r]
                r-=1
            else:
                current+=1
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
