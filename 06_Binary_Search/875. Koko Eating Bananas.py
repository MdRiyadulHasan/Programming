from typing import List 
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_all(speed):
            total_hour=0
            for pile in piles:
                total_hour+=math.ceil(pile/speed)
            return total_hour<=h
        left = 1
        right = max(piles)
        while left<right:
            mid = (left+right)//2
            if can_eat_all(mid):
                right=mid
            else:
                left = mid+1
        return left