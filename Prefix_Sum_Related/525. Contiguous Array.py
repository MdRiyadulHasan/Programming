from typing import List 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_map = {0:-1}
        prefix_sum = 0
        max_length = 0
        for i,n in enumerate(nums):
            prefix_sum+=1 if n==1 else -1
            if prefix_sum in prefix_map:
                max_length = max(max_length, i-prefix_map[prefix_sum])
            else:
                prefix_map[prefix_sum]=i
        return max_length