from typing import List 
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last_days = days[-1]
        travel_days = set(days)
        dp = [0]*(last_days+1)
        for i in range(1, last_days+1):
            if i not in travel_days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(
                    dp[max(0, i-1)]+costs[0],
                    dp[max(0, i-7)]+costs[1],
                    dp[max(0, i-30)]+costs[2]
                )
        return dp[-1]
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17