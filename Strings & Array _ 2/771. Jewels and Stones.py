class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        jewels_count =Counter(jewels)
        print(jewels_count)
        return sum([jewels_count[jewel] for jewel in stones])
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3