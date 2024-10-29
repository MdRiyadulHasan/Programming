from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dic = {word:i for i, word in enumerate(words)}
        result = []
        print(word_dic)
        def isPalindrome(word):
            return word==word[::-1]
        for i, word in enumerate(words):
            n=len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]
                if isPalindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix  in word_dic and word_dic[reversed_suffix]!=i:
                        print("suffix", word_dic[reversed_suffix])
                        result.append([word_dic[reversed_suffix], i])
                if j!=n and isPalindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dic and word_dic[reversed_prefix]!=i:
                        print("Reversed prefix", word_dic[reversed_prefix])
                        result.append([i, word_dic[reversed_prefix]])
        return result

words = ["abcd","dcba","lls","s","sssll"]
ob = Solution()
ans = ob.palindromePairs(words)
print(ans)

        