from typing import List
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        from collections import Counter
        return Counter(target) == Counter(arr)

def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)

# Example usage
target = [7, 3, 1, 9]
arr = [9, 7, 3, 1]
print(canBeEqual(target, arr))  #