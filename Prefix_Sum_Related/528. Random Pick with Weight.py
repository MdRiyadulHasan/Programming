from typing import List 
import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        prefix_sum = 0
        self.total_weights = 0
        for weight in w:
            prefix_sum+=weight
            self.prefix.append(prefix_sum)
        self.total_weights = prefix_sum 
        

    def pickIndex(self) -> int:
        target = random.randint(1,self.total_weights)
        l = 0
        r = len(self.prefix)-1
        while l<=r:
            mid = (l+r)//2
            if self.prefix[mid]==target:
                return mid
            elif self.prefix[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return l 
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()