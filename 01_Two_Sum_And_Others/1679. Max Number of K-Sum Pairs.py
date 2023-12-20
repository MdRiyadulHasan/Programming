from typing import List 
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        dic  = {}
        for n in nums:
            diff = k-n 
            if dic.get(diff,0)>0:
                count +=1
                dic[diff] -=1
            else:
                dic[n]=dic.get(n,0)+1
        return count

nums = [1,2,3,4]
k = 5
ob = Solution()
result = ob.maxOperations(nums,k)
print(result)
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1

 