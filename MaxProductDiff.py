# The goal is to find the maximum product difference between two pairs of numbers in a list.

class Solution(object):
    def maxProductDifference(self, nums):
        nums = sorted(nums)
        min_vals = nums[0] * nums[1]
        max_vals = nums[-1] * nums[-2]
        return max_vals - min_vals