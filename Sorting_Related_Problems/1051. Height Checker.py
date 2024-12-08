from typing import List 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        print(expected)
        count = 0
        for i, j in zip(expected, heights):
            if i!=j:
                count+=1
        return count
