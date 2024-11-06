
def applyOperations(nums) :
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            nums[i]=nums[i]*2
            nums[i+1]=0
    k = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[k], nums[i]=nums[i], nums[k]
            k+=1
    return nums
        # return sorted(nums, key=lambda x:x==0)
        
       
nums = [1,2,2,1,1,0]
[1,4,0,2,0,0]
[1,4,2,0,0,0]