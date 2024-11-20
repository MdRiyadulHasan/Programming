class Solution:
    def customSortString(self, order: str, s: str) -> str:
        rank = {char:i for i, char in enumerate(order)}
        result = sorted(s, key = lambda x:rank.get(x, len(order)))
        return "".join(result)
# Input: order = "cba", s = "abcd"

# Output: "cbad"