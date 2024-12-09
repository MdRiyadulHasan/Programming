class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        result = []
        for word in words:
            result.append(word[::-1])
        # return ' '.join(word[::-1] for word in words)
        return " ".join(result)
    
    