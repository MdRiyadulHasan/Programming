# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        if not s or not t:
            return ""
        res = ''
        targetDic = Counter(t)
        targetLen = len(targetDic)
        dic = {}
        currentLen = 0
        minLen = float('inf')
        l = 0
        for r,ch in enumerate(s):
            dic[ch]=dic.get(ch,0)+1
            if ch in targetDic and dic[ch]==targetDic[ch]:
                currentLen += 1
            while currentLen==targetLen:
                if r-l+1<minLen:
                    minLen = r-l+1
                    res = s[l:r+1]
                leftchar = s[l]
                dic[leftchar]-=1
                if leftchar in targetDic and dic[leftchar]<targetDic[leftchar]:
                    currentLen-=1
                l+=1
        return res

s = "ADOBECODEBANC"
t = "ABC"
ob = Solution()
result = ob.minWindow(s, t)
print(result)
