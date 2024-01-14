def BubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
if __name__ == '__main__':
    nums = [30,15,20,25,12,8,40,22,17]
    result = BubbleSort(nums)
    print(result)