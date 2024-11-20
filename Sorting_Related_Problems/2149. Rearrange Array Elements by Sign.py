from typing import List 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative= [x for x in nums if x<0]
        positive = [x for x in nums if x>=0]
        result = []
        for p, n in zip(positive, negative):
            result.append(p)
            result.append(n)
        return result
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]