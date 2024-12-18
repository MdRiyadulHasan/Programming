from typing import List 
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruit = 0
        left = 0
        dic = {}
        count=0
        for right, n in enumerate(fruits):
            dic[n] = dic.get(n,0)+1
            if dic[n]==1:
                count+=1
            while count>2:
                dic[fruits[left]]-=1
                if dic[fruits[left]]==0:
                    count-=1
                left+=1
            maxFruit = max(maxFruit, right-left+1)
        return maxFruit

# Input: fruits = [1,2,3,2,2]
# Output: 4