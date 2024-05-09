def SelectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        min = i 
        for j in range(i+1, n-1):
            if nums[j]<nums[min]:
                min = j
        if nums[i]!=nums[min]:
            nums[min], nums[i] = nums[i], nums[min]
    return nums


if __name__ == '__main__':
    nums = [30,15,20,25,12,8,40,22,17]
    result = SelectionSort(nums)
    print(result)