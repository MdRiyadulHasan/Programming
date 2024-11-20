from typing import List 
def sortArrayByParityII(nums: List[int]) -> List[int]:
    even_idx = 0  # Pointer for even indices
    odd_idx = 1   # Pointer for odd indices
    n = len(nums)
    
    while even_idx < n and odd_idx < n:
        # If the even index contains an odd number
        if nums[even_idx] % 2 == 1:
            # Swap it with the odd index if it contains an even number
            nums[even_idx], nums[odd_idx] = nums[odd_idx], nums[even_idx]
            odd_idx += 2
        else:
            even_idx += 2  # Move to the next even index
    
    return nums
nums = [4,3,1,7,2,6]
print(sortArrayByParityII(nums))
