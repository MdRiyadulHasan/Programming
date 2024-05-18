from typing import List 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        results = []
        for n in candies:
            if n+extraCandies>=highest:
                results.append(True)
            else:
                results.append(False)
        return results 
candies = [2,3,5,1,3]
extraCandies = 3
ob = Solution()
ans = ob.kidsWithCandies(candies, extraCandies)
print(ans)
        