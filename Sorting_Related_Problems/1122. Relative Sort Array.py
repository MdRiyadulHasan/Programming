from typing import List 
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order_map = {char:i for i,char in enumerate(arr2)}
        print(order_map)
        arr1.sort(key=lambda x:(order_map.get(x,len(arr2)), x))
        return arr1
# Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# Output: [2,2,2,1,4,3,3,9,6,7,19]