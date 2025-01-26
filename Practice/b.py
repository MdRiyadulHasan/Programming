from typing import List  
def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        n = len(nums1)+len(nums2)
        half = n//2
        l = 0
        r = len(nums1)-1
        while True:
            m1 = (l+r)//2
            m2 = half-m1-2
            nums1Left =nums1[m1] if m1>=0 else float("-inf")
            nums1Right = nums1[m1+1] if m1+1<len(nums1) else float("inf")
            nums2Left = nums2[m2] if m2>=0 else float("-inf")
            nums2Right = nums2[m2+1] if m2+1<len(nums2) else float("inf")
            if nums1Left<=nums2Right and nums2Left<=nums1Right:
                if n%2==0:
                    return ((max(nums1Left, nums2Left)+min(nums1Right, nums2Right))/2)
                else:
                    return min(nums1Right, nums2Right)
            elif nums1Right<nums2Left:
                l = m1+1
            else:
                r = m1-1
nums1 = [1,2,3,4,5,6,7,13,14,15,17,18]
nums2 = [8,9,10,11,12]
print(findMedianSortedArrays(nums1, nums2))