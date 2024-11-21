from typing import List
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {val:i for i,val in enumerate(list1) }
        print(dic)
        min_sum = float("inf")
        result = []
        for j, val in enumerate(list2):
            if val in list1:
                i = dic[val]
                index_sum = i+j
                if index_sum<min_sum:
                    min_sum = index_sum
                    result = [val]
                elif index_sum==min_sum:
                    result.append(val)
        return result


# Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
# Output: ["sad","happy"]