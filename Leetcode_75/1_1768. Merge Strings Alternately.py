class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=0
        l2=0
        word = ""
        while l1<len(word1) and l2<len(word2):
            word +=word1[l1]
            word+=word2[l2]
            l1+=1
            l2+=1 
        while l1<len(word1):
            word+=word1[l1]
            l1+=1 
        while l2<len(word2):
            word+=word2[l2]
            l2+=1
        return word
word1 = "abcd"
word2 = "pq"
ob = Solution()
ans = ob.mergeAlternately(word1, word2)
print(ans)

        