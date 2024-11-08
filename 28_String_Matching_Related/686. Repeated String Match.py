class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        re = a
        count = 1
        while len(re) < len(b):
            re += a
            count += 1
        
        if b in re:
            return count
    
        re += a
        count += 1
        if b in re:
            return count

        return -1
a = "abcd"
b = "cdabcdab"