# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/

from typing import List 
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s = 0
        L = len(arr) 
        for i in range(L):
            for j in range(i,L,2):
                s += sum(arr[i:j+1]) 
        return s
arr = [1,4,2,5,3]