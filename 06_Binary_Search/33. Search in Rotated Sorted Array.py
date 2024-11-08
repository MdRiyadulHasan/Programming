# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the mid element is the target
        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[left] <= nums[mid]:  # Left side is sorted
            if nums[left] <= target < nums[mid]:  # Target is in the left half
                right = mid - 1
            else:  # Target is in the right half
                left = mid + 1
        else:  # Right side is sorted
            if nums[mid] < target <= nums[right]:  # Target is in the right half
                left = mid + 1
            else:  # Target is in the left half
                right = mid - 1

    # If the target was not found
    return -1

# Test cases
print(search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # Output: -1

        