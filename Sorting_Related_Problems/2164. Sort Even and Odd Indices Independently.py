from typing import List 
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even_numbers = sorted([x for i, x in enumerate(nums) if i % 2 == 0]) 
        odd_numbers = sorted([x for i, x in enumerate(nums) if i % 2 != 0], reverse=True)
        even_index = 0
        odd_index = 0
        result = []
        for i in range(len(nums)):
            if i%2==0:
                result.append(even_numbers[even_index])
                even_index+=1
            else:
                result.append(odd_numbers[odd_index])
                odd_index+=1
        return result

# Input: nums = [4,1,2,3]
# Output: [2,3,4,1]