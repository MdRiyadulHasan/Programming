class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        from collections import Counter
        dic = Counter(s)
        max_heap = [(-freq, char) for char, freq in dic.items()]
        heapq.heapify(max_heap)
        print(max_heap)
        prev_char = None
        prev_count = 0
        result = []
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            if prev_char and prev_count<0:
                heapq.heappush(max_heap,(prev_count, prev_char))
            prev_char = char
            prev_count=count+1
        result = "".join(result)
        if len(result)!=len(s):
            return ""
        return result
                
# Input: s = "aab"
# Output: "aba"
            

        

        