from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        maxProfit = 0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                maxProfit =max(maxProfit, prices[r]-prices[l])
            else:
                l=r
        return maxProfit