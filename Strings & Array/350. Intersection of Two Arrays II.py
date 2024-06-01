from typing import List 
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter 
        dic = Counter(nums1)
        print(dic)
        res = []
        for n in nums2:
            if dic[n]>0:
                res.append(n) 
                dic[n]-=1 
        return res
        