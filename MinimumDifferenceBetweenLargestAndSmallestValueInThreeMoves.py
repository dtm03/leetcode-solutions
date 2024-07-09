class Solution(object):
    def minDifference(self, nums):
        if len(nums) <= 4:
            return 0
        nums.sort()
        return min(
            nums[-1] - nums[3],   # Changing the first three elements
            nums[-2] - nums[2],   # Changing the first two and the last one
            nums[-3] - nums[1],   # Changing the first one and the last two
            nums[-4] - nums[0]    # Changing the last three elements
        )