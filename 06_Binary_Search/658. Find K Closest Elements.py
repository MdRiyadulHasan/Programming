# https://leetcode.com/problems/find-k-closest-elements/
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-k
        while l<r:
            m = (l+r)//2
            if x-arr[m]>arr[m+k]-x:
                l = m+1
            else:
                r = m
        return arr[l:l+k]

arr= [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
k= 5
x = 12