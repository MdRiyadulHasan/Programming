from typing import List 
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix_sum = [0]*(n+1)
        for i in range(n):
            self.prefix_sum[i+1] =self.prefix_sum[i]+nums[i] 
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1]-self.prefix_sum[left]