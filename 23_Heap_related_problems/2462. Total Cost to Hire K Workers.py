from typing import List 
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq
        l = 0
        r = len(costs)-1
        pq = []
        for i in range(candidates):
            if l<=r:
                heapq.heappush(pq, (costs[l], l))
                l+=1
            if l<=r:
                heapq.heappush(pq, (costs[r], r))
                r-=1
        # print(pq)
        total_costs = 0
        for _ in range(k):
            cost, idx = heapq.heappop(pq)
            total_costs+=cost
            if idx<l:
                if l<=r:
                    heapq.heappush(pq, (costs[l], l))
                    l+=1
            elif idx>r:
                if l<=r:
                    heapq.heappush(pq, (costs[r], r))
                    r-=1
        return total_costs
# Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
# Output: 11