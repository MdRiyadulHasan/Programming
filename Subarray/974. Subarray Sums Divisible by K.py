from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store the cumulative sum modulo k and its frequency
        dic = {0: 1}
        count = 0
        cumulativeSum = 0

        # Iterate through the array
        for n in nums:
            cumulativeSum += n
            cumulativeSum %= k

            # Ensure cumulativeSum is non-negative
            if cumulativeSum < 0:
                cumulativeSum += k

            # Count subarrays with the same cumulative sum modulo k
            count += dic.get(cumulativeSum, 0)

            # Update the frequency of the current cumulative sum modulo k
            dic[cumulativeSum] = dic.get(cumulativeSum, 0) + 1

        return count

# Example usage:
nums = [4, 5, 0, -2, -3, 1]
k = 5
solution = Solution()
result = solution.subarraysDivByK(nums, k)
print("Number of subarrays divisible by", k, ":", result)
