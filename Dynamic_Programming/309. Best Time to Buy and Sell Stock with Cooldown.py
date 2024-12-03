from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        buy = -prices[0]
        cooldown = 0
        sell = 0
        for i in range(1,len(prices)):
            prev_buy = buy
            buy = max(buy, cooldown-prices[i])
            cooldown = max(cooldown, sell)
            sell = prev_buy+prices[i]
        return max(cooldown, sell)
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]