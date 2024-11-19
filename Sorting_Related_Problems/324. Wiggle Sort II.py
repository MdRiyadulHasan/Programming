def wiggleSort(nums):
    # Sort the array
    nums.sort()
    
    # Find the midpoint of the array
    n = len(nums)
    mid = (n - 1) // 2
    
    # Create two halves and reverse them to place larger values at the front
    left = nums[:mid + 1][::-1]  # Smaller half (reversed)
    right = nums[mid + 1:][::-1]  # Larger half (reversed)
    
    # Interleave elements from left and right
    for i in range(n):
        if i % 2 == 0:
            nums[i] = left.pop(0)  # Take from the left half for even indices
        else:
            nums[i] = right.pop(0)  # Take from the right half for odd indices

# Example usage
nums = [1, 5, 1, 1, 6, 4]
wiggleSort(nums)
print(nums)  # Output will be a valid wiggle sort like [1, 6, 1, 5, 1, 4]
