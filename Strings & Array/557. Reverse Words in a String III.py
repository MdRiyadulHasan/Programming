class Solution:
    def reverseWords(self, s: str) -> str:
        s =s.split()
        res = []
        for word in s:
            l = 0 
            r = len(word)-1
            word = list(word)
            while l < r:
                word[l], word[r] = word[r], word[l]
                l+=1
                r-=1
            res.append("".join(word))
        return " ".join(res)