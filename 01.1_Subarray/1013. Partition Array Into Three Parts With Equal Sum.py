# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/

from typing import List
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)

        if total_sum % 3 != 0:
            return False

        target_sum = total_sum // 3
        current_sum = 0
        count = 0

        for num in arr:
            current_sum += num

            if current_sum == target_sum:
                count += 1
                current_sum = 0

        # Check if we found exactly 3 segments with equal sums
        return count >= 3
arr = [0,2,1,-6,6,-7,9,1,2,0,1]
ob = Solution()
result = ob.canThreePartsEqualSum(arr)
print (result)