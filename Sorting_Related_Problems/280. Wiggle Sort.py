def wiggleSort(nums):
    for i in range(len(nums) - 1):
        if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]

# Example usage
nums = [3, 5, 2, 1, 6, 4]
wiggleSort(nums)
print(nums)  # Output will be a valid wiggle sort like [3, 5, 1, 6, 2, 4]
