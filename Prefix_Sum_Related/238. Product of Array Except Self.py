class Solution:
    def productExceptSelf( nums):
        n = len(nums)
        ans = [1]*n
        # print(ans)
        left_product = 1
        for i in range(n):
            ans[i] = left_product
            left_product*=nums[i]
        print(ans)
        right_product = 1
        for i in range(n-1,-1,-1):
            ans[i]*=right_product
            right_product*=nums[i]
        return ans
        
nums = [1,2,3,4]