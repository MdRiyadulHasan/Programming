from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float("inf")
        for i in range(1, len(arr)):
            minDiff = min(minDiff, arr[i]-arr[i-1])
        result = []
        for i in range (1, len(arr)):
            if arr[i]-arr[i-1]==minDiff:
                result.append([arr[i-1], arr[i]])
        return result
# Input: arr = [4,2,1,3]
# Output: [[1,2],[2,3],[3,4]]