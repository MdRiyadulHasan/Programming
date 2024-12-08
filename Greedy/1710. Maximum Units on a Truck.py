from typing import List 
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        totalUnit = 0
        for boxCount, unit in boxTypes:
            if truckSize==0:
                return totalUnit
            maxToLoad = min(boxCount, truckSize)
            totalUnit+=(maxToLoad*unit)
            truckSize-=maxToLoad
        return totalUnit
        