from typing import List 
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = list(map(str, nums))
        print(nums_str)
        nums_str1 = [str(n) for n in nums]
        nums_str1.sort(key=lambda x:x*10, reverse=True)
        result =  "".join(nums_str1)
        return "0" if result[0]=="0" else result
nums = [3,30,34,5,9]
"9534330"