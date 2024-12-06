class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        result = []
        for word in title:
            if len(word)<=2:
                result.append(word.lower())
            else:
                result.append(word.capitalize())
        return " ".join(result) 
        