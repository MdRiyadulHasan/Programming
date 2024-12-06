from collections import List 
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        from bisect import bisect_left
        products.sort()
        print(products)
        prefix = ""
        result = []
        for ch in searchWord:
            prefix+=ch
            start = bisect_left(products, prefix)
            suggestions = []
            for i in range(start, min(start+3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            result.append(suggestions)
        return result
