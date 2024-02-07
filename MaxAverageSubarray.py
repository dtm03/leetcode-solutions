# The goal is to find the maximum average value of any contiguous subarray of size k. => Use sliding window

class Solution(object):
    def findMaxAverage(self, nums, k):

        s = sum(nums[0 : k])
        ma= s

        for i in range(0, len(nums) - k):
            # Slides the window and computes the sum one time to the right
            s += nums[i + k] - nums[i]
            ma = max(ma, s)
        return ma/ float(k)
