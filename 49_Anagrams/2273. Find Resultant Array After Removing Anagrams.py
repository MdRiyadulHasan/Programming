class Solution:
    def removeAnagrams(self, words) :
        results = [words[0]]
        for i in range(1,len(words)):
            if sorted(words[i])!=sorted(words[i-1]):
                results.append(words[i])
        return results
words = ["abba","baba","bbaa","cd","cd"]