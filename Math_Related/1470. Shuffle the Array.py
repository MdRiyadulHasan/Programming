from typing import List 
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left_list = nums[:n]
        right_list = nums[n:]
        result = []
        for n1,n2 in zip(left_list, right_list):
            result.append(n1)
            result.append(n2)
        return result
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 