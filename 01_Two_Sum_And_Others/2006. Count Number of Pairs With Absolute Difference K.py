from typing import List
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        dic = {}
        for n in nums:
            count += dic.get(n-k, 0)
            count += dic.get(n+k, 0)
            dic[n] = dic.get(n,0)+1
        return count
    
nums = [1,2,2,1]
k = 1
ob = Solution()
ans = ob.countKDifference(nums,k)
print(ans)
# nums = [3,2,1,5,4]
# k = 2
