# https://leetcode.com/problems/subarrays-with-k-different-integers/description/

from typing import List 
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        dic1 = {}
        dic2 = {}
        count1 = 0
        count2 = 0
        l=0
        r=0
        result =0
        for n in nums:
            dic1[n]=dic1.get(n,0)+1
            if dic1[n]==1:
                count1+=1
            dic2[n]=dic2.get(n,0)+1
            if dic2[n]==1:
                count2+=1
            while count1>k:
                dic1[nums[l]]-=1
                if dic1[nums[l]]==0:
                    count1-=1
                l+=1
            while count2>k-1:
                dic2[nums[r]]-=1
                if dic2[nums[r]]==0:
                    count2-=1
                r+=1
            result += r-l
        return result
    
nums = [1,2,1,2,3]
k = 2
ob = Solution()
result = ob.subarraysWithKDistinct(nums, k)
print(result)