class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)
        expected_sum = (n*(n+1))//2 
        actual_sum = sum(nums)
        return expected_sum-actual_sum
  
        