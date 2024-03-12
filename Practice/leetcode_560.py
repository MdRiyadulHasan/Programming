# https://leetcode.com/problems/subarray-sum-equals-k/
from typing import List
# {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1, 18: 1, 20: 1, 21: 1}
print("Hello world !............................")
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        count = 0
        cumulativeSum = 0
        for n in nums:
            cumulativeSum+=n
            diff = cumulativeSum-k
            if diff in dic:
               count+=dic[diff]
            dic[cumulativeSum]=dic.get(cumulativeSum,0)+1
        return count 
nums= [3, 4, 7, 2, -3, 1, 4, 2,1]
k= 7
solution_instance = Solution()
result = solution_instance.subarraySum(nums, k)
print(result)


