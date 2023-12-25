# https://leetcode.com/problems/sliding-window-maximum/description/
from typing import List

class Solution:
     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1:
             return nums
        import heapq
        result = []
        numsWindow = [(-val,i) for i,val in enumerate(nums[:k])]
        heapq.heapify(numsWindow)
        result.append(-numsWindow[0][0])
        for i in range(k,len(nums)):
            while numsWindow[0][1]<=i-k:
                heapq.heappop(numsWindow)
            heapq.heappush(numsWindow, (-nums[i],i))
            result.append(-numsWindow[0][0])
        return result
nums = [1,3,-1,-3,5,3,6,7]
k = 3
ob = Solution()
result = ob.maxSlidingWindow(nums, k)
print(result)
