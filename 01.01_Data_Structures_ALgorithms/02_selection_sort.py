def SelectionSort(nums):
    for i in range(len(nums)-1):
        min = i 
        for j in range(min+1, len(nums)):
            if nums[j]<nums[min]:
                min = j
        if min!=i:
            nums[min],nums[i]= nums[i], nums[min]
    return nums

if __name__ == '__main__':
    nums = [30,15,20,25,12,8,40,22,17]
    result = SelectionSort(nums)
    print(result)