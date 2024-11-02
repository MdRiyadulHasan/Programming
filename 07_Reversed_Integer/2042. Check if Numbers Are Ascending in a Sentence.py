class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        res =[]
        for word in s.split():
            if word.isdigit():
                if res and res[-1]>=int(word):
                    return False 
                res.append(int(word))
        return True 
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = -1
        for w in s.split():
            if w.isdigit():
                if int(w)<=prev:
                    return False 
                prev = int(w)
        return True