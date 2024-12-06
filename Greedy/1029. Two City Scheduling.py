from typing import List 
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        print(costs)
        n = len(costs)//2
        total_cost = 0
        for i in range(n):
            total_cost+=costs[i][0]
        for i in range(n, 2*n):
            total_cost+=costs[i][1]
        return total_cost
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859