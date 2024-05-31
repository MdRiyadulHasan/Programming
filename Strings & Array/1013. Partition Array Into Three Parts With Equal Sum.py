from typing import List 
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total%3!=0:
            return False 
        target_sum = total//3 
        current_sum = 0
        count=0
        for n in arr:
            current_sum+=n
            if target_sum==current_sum:
                count+=1 
                current_sum = 0
        return count>=3

arr = [0,2,1,-6,6,-7,9,1,2,0,1]