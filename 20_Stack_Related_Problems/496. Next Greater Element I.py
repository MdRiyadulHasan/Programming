from typing import List 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for n in nums2:
            while stack and stack[-1]<n:
                k = stack.pop()
                dic[k]= n 
            stack.append(n)
        return [dic.get(val,-1) for val in nums1]
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
nums = [1,2,3,4,3]
