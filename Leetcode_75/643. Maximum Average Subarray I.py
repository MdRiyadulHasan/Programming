from typing import List 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = currentSum = sum(nums[:k])
        n = len(nums)
        for i in range(k,n):
            currentSum+=nums[i]-nums[i-k]
            maxSum = max(maxSum, currentSum)
        return maxSum/k
    
nums = [1,12,-5,-6,50,3]
k = 4