from typing import List 
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        from collections import Counter
        nums_count = Counter(nums)
        lonely_nums = [num for num in nums if nums_count[num]==1 and nums_count[num+1]==0 and nums_count[num-1]==0]
        
        return lonely_nums