from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        count = 0
        cumulativeSum = 0
        for n in nums:
            cumulativeSum +=n
            diff = cumulativeSum-k
            if diff in dic:
                count +=dic[diff]
            dic[cumulativeSum]=dic.get(cumulativeSum,0)+1
        return count
# Example usage
nums= [3, 4, 7, 2, -3, 1, 4, 2,1]
k= 7

solution_instance = Solution()
result = solution_instance.subarraySum(nums, k)
print(result)
