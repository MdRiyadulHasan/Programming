from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        sorted_names = [name for name, height in sorted(zip(names, heights), key=lambda x: x[1], reverse=True)]
        return sorted_names
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Zip names and heights together, sort by height in descending order
        combined = list(zip(names, heights))
        
        # Sort by the second item (height) in descending order
        combined.sort(key=lambda x: x[1], reverse=True)
        
        # Extract the sorted names
        result = [name for name, height in combined]
        
        return result  # Return the sorted list of names