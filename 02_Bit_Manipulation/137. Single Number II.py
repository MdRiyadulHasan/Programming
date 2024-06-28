from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n]=dic.get(n,0)+1
        for k,v in dic.items():
            if v==1:
                return k
        