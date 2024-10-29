#1347
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter 
        S = Counter(s)
        T = Counter(t) 
        return sum((S-T).values())