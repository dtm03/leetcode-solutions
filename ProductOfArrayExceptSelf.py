# Multiply left Side and right Side products of each number in the array

class Solution(object):
    def productExceptSelf(self, nums):

        left = [1]

        for i in range(1, len(nums)):
            left.append(nums[i - 1] * left[i - 1])

        right = 1

        for i in range(len(nums) -1, -1, -1):
            left[i] *= right
            right *= nums[i]

        return left