from typing import List 
from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # Count the frequency of each string
        freq = Counter(arr)
        
        # Iterate over the array and check for distinct strings
        distinct_count = 0
        for word in arr:
            if freq[word] == 1:  # Check if the string is distinct
                distinct_count += 1
                if distinct_count == k:  # Found the k-th distinct string
                    return word
        
        # If k-th distinct string doesn't exist, return ""
        return ""