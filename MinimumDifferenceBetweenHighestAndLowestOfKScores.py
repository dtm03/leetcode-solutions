class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            min_diff = min(min_diff, nums[i + k - 1] - nums[i])
        return min_diff