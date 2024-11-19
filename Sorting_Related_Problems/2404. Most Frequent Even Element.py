from collections import Counter
from typing import List
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:

        ctr = Counter(nums)

        return max([c for c in ctr if not c%2], key = lambda x:(ctr[x], -x), default = -1)
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        from collections import Counter
        nums.sort()
        dic = Counter(n for n in nums if n%2==0)
        return dic.most_common()[0][0] if dic else -1