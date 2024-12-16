from typing import List 
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        dic = Counter(nums)
        maxLength = 0
        for k in dic:
            if k+1 in dic:
                maxLength = max(maxLength, dic[k]+dic[k+1])
        return maxLength
# Input: nums = [1,3,2,2,5,2,3,7]

# Output: 5

