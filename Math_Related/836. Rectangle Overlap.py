from typing import List 
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2=rec1
        x3,y3,x4,y4 = rec2
        if x2<=x3 or y2<=y3 or x4<=x1 or y4<=y1:
            return False
        return True