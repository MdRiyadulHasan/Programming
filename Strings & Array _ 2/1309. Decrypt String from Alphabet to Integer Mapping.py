class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = 0
        result = []
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                num = int(s[i:i+2])
                result.append(chr(96+num))
                i+=3
            else:
                num = int(s[i])
                result.append(chr(96+num))
                i+=1
        return "".join(result)