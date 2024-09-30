from typing import List 
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i,j,k=0,0,0
        res = []
        while i<len(arr1) and j<len(arr2) and k<len(arr3):
            if arr1[i]==arr2[j]==arr3[k]:
                res.append(arr1[i])
                i,j,k=i+1,j+1,k+1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr3[k]:
                j+=1
            else:
                k+=1
        return res
arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
# Output: [1,5]
        
# from collections import defaultdict
#         dic = defaultdict(int) 
#         for n in arr1:
#             dic[n]+=1 
#         for n in arr2:
#             dic[n]+=1
#         for n in arr3:
#             dic[n]+=1
#         res = []
#         for k, v in dic.items():
#             if v==3:
#                 res.append(k)
#         return res

