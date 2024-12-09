class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        emptyBootles = 0
        while numBottles>0:
            total_drunk+=numBottles
            emptyBootles+=numBottles
            numBottles = emptyBootles//numExchange
            emptyBootles = emptyBootles%numExchange
        return total_drunk
# Input: numBottles = 15, numExchange = 4
# Output: 19