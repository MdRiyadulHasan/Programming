# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                price = prices[i]-prices[i-1]
                total += price
        return total    
ob = Solution()
prices =[7,1,5,3,6,4]
result = ob.maxProfit(prices)
print(result)
