from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        maxProfit = 0 
        while r<len(prices):
            if prices[r]>prices[l]:
                maxProfit = max(maxProfit, prices[r]-prices[l])
            else:
                l = r 
            r+=1 
        return maxProfit
prices = [7,1,5,3,6,4]