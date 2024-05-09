def insertion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        j = i-1
        key = nums[i]
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1]=key
    return nums
if __name__ =='__main__':
    nums = [10,5,7,2,15,1,6]
    ans = insertion_sort(nums)
    print(ans)