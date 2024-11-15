class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count=0
        for a in arr1:
            default = True
            for b in arr2:
                if abs(a-b)<=d:
                    default = False
                    break
                if b-a>d:
                    break              
            if default:
                count+=1
        return count 
 arr1 = [4,5,8]
 arr2 = [10,9,1,8]
 d = 2