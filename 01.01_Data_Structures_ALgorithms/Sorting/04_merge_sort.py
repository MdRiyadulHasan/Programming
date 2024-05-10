def merge_sort(nums):
    if len(nums)==1:
        return 
    m = len(nums)//2
    left_arr = nums[:m]
    right_arr = nums[m:]
    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(nums, left_arr, right_arr)
def merge(nums, left_arr, right_arr):
    l, r,k=0,0,0
    while l<len(left_arr) and r<len(right_arr):
        if left_arr[l] < right_arr[r]:
            nums[k]= left_arr[l]
            l+=1
        else:
            nums[k]= right_arr[r]
            r+=1
        k+=1
    while l<len(left_arr):
        nums[k]= left_arr[l]
        l+=1
        k+=1
    while r<len(right_arr):
        nums[k]= right_arr[r]
        r+=1
        k+=1
if __name__ == '__main__':
    arr = [5,3,7,1,0,8,5]
    merge_sort(arr)
    print(arr)