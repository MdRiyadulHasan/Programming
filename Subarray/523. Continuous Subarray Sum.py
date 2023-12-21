# https://leetcode.com/problems/continuous-subarray-sum/description/

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cumulativeSum = 0
        dic = {0: -1}  # Initialize with a dummy value to handle subarrays starting from the beginning
        for i, n in enumerate(nums):
            cumulativeSum += n

            cumulativeSum %= k

            if cumulativeSum in dic:
                # Check if the subarray length is at least 2
                if i - dic[cumulativeSum] > 1:
                    return True
            else:
                dic[cumulativeSum] = i

        return False

nums_example = [23, 2, 4, 6, 7]
k_example = 6

solution_instance = Solution()
result = solution_instance.checkSubarraySum(nums_example, k_example)

print(result)
