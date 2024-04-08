# The goal is to determine the number of contiguous subarrays whose are less than k if they are multiplied.

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):

        if k == 0:
            return 0

        p, c = 1, 0
        l = 0

        for r in range(len(nums)):
            p *= nums[r]
            while p >= k:
                if l > r:
                    return c
                p /= nums[l]
                l += 1
            c += r - l + 1

        return c