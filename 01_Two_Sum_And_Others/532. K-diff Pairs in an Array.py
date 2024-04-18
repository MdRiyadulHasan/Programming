# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
from collections import Counter
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freqCount = Counter(nums)
        print(freqCount)
        count = 0
        if k==0:
            for key, val in freqCount.items():
                if val>1:
                    count+=1
        else:
            for key, val in freqCount.items():
                if key+k in freqCount:
                    count+=1
        return count

ob = Solution()
nums = [3,1,4,1,5]
k = 2  
res = ob.findPairs(nums,k)
print(res)