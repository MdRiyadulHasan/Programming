# https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List 

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)
        half = n//2
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        l = 0
        r = len(nums1)-1
        while True:
            m1 = (l+r)//2
            m2 = half-m1-2
            nums1Left = nums1[m1] if m1>=0 else float('-inf')
            nums1Right = nums1[m1+1] if m1+1<len(nums1) else float('inf')
            nums2Left = nums2[m2] if m2>=0 else float('-inf')
            nums2Right = nums2[m2+1] if m2+1 <len(nums2) else float('inf')
            if nums1Left<=nums2Right and nums1Right>=nums2Left:
                if n%2==0:
                    return((max(nums1Left, nums2Left)+ min(nums1Right, nums2Right))/2)
                else:
                    return min(nums1Right, nums2Right)

            elif nums1Right<nums2Left:
                l = m1+1
            else:
                r = m1-1
# Example usage with arrays of size greater than 6
solution = Solution()
nums1 = [1, 3, 5, 7, 9]
nums2 = [2, 4, 6, 8, 10, 12, 14]
result = solution.findMedianSortedArrays(nums1, nums2)
print(result)

