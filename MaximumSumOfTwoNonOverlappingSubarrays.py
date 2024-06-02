class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        def max_sum(L, M):
            max_L = max_M = max_total = 0
            for i in range(L + M, len(nums) + 1):
                max_L = max(max_L, sum(nums[i - L - M:i - M]))
                max_M = max(max_M, sum(nums[i - L - M:i - L]))
                max_total = max(max_total, max_L + sum(nums[i - M:i]), max_M + sum(nums[i - L:i]))
            return max_total

        return max(max_sum(firstLen, secondLen), max_sum(secondLen, firstLen))