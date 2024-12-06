from typing import List 
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        remove_count = n//20
        trimmed_arr = arr[remove_count:n-remove_count]
        mean = sum(trimmed_arr)/len(trimmed_arr)
        return round(mean, 5)
# Input: arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# Output: 4.77778