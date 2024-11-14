from typing import List
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    dic = {}
    for i, n in enumerate(nums):
        if n in dic and i -dic[n]<=k:
            return True
        dic[n] = i
       

nums = [1,2,3,1]
k = 3
containsNearbyDuplicate(nums, k)