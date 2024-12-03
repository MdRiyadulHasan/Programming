from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        firstBuy = float('-inf')
        firstSell = 0
        secondBuy = float('-inf')
        secondSell = 0
        for price in prices:
            firstBuy = max(firstBuy, -price)
            firstSell = max(firstSell, firstBuy+price)
            secondBuy = max(secondBuy, firstSell-price)
            secondSell = max(secondSell, secondBuy+price)
        return secondSell