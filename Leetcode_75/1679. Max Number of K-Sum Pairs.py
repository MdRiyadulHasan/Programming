from typing import List 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        dic = {}
        count = 0 
        for n in nums:
            diff = k-n  
            if dic.get(diff,0)>0:
                dic[diff]-=1
                count+=1  
            else:
                dic[n]=dic.get(n,0)+1
        return count
nums = [1,2,3,4]
k = 5