from typing import List
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        nums1 = sorted(items1, key=lambda x:x[0])
        nums2 = sorted(items2, key=lambda x:x[0])
        i,j=0,0
        res = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i][0]==nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]+nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0]<nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]])
                i+=1
            else:
                res.append([nums2[j][0], nums2[j][1]])
                j+=1
        while i<len(nums1):
            res.append([nums1[i][0], nums1[i][1]])
            i+=1
        while j<len(nums2):
            res.append([nums2[j][0], nums2[j][1]])
            j+=1

        return res
# Input: items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
# Output: [[1,6],[3,9],[4,5]]