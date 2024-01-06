# https://leetcode.com/problems/next-permutation/
from typing import List 
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first element i from the right such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i = i - 1

        # Step 2: If no such element is found, reverse the entire list and return
        if i == -1:
            nums.reverse()
            return

        # Step 3: Find the smallest element to the right of i that is greater than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j = j - 1

        # Step 4: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # Step 5: Reverse the subsequence to the right of i
        nums[i + 1:] = nums[i + 1:][::-1]
        # return nums
sol = Solution()
nums = [1, 4, 6, 5, 3]
sol.nextPermutation(nums)
print(nums)

