# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                price = prices[r]-prices[l]
                maxProfit = max(maxProfit, price)
            else:
                l=r
            r+=1
        return maxProfit 

prices = [1,2,4,2,5,7,2,4,9,0,9]
ob = Solution()
result = ob.maxProfit(prices)
print(result)