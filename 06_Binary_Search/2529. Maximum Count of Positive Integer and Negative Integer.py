class Solution:
    def maximumCount(self, nums) -> int:
        from bisect import bisect_left, bisect_right
        # count_P = 0
        # count_N = 0
        # for n in nums:
        #     if n<0:
        #         count_N+=1
        #     elif n>0:
        #         count_P+=1
        # return max(count_N, count_P)
        negative_count = bisect_left(nums,0)
        first_positive = bisect_right(nums,0)
        positive_count = len(nums)-first_positive
        return max(positive_count, negative_count)
        