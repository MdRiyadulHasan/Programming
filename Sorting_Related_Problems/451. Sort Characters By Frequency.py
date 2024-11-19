class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        s = list(s)
        dic = Counter(s)
        result1 = sorted(dic, key = lambda x: dic[x], reverse= True)
        result = [ch*dic[ch] for ch in result1]
        return "".join(result)
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        s = list(s)
        dic = Counter(s) 
        result1 = sorted(dic.items(), key = lambda x:(-x[1], x[0]))
        print(result1)
        result = [ch*dic[ch] for ch, freq in result1]
        return "".join(result)