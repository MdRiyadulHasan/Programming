# https://leetcode.com/problems/merge-sorted-array/description/

from typing import List 
class Solution:
    def merge(self,nums1: List[int], m: int, nums2: List[int], n: int):
        l = (m+n)-1
        while m>0 and n>0:
            if nums1[m-1]<nums2[n-1]:
                nums1[l]=nums2[n-1]
                n=n-1
            else:
                nums1[l]=nums1[m-1]
                m = m-1 
            l=l-1 
        while n>0:
            nums1[l]= nums2[n-1]
            n-=1
            l-=1
        return nums1
            
       
       
ob = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
result = ob.merge(nums1,m,nums2,n)
print(result)