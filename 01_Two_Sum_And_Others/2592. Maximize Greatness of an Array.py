from typing import List
def maximizeGreatness(nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for num in nums:
            if nums[ans] < num:
                ans += 1
        return ans
nums = [1,3,5,2,1,3,1]
res = maximizeGreatness(nums)
print(res)