class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
        if len(digits)<2:
            return -1 
        return sorted(digits, reverse=True)[1]
s = "dfa12321afd"