class Solution(object):
    def maximumScore(self, nums, k):
        n = len(nums)
        res = nums[k]
        i = j = k
        min_val = nums[k]

        while i > 0 or j < n - 1:
            if i > 0 and (j == n - 1 or nums[i - 1] >= nums[j + 1]):
                i -= 1
                min_val = min(min_val, nums[i])
            else:
                j += 1
                min_val = min(min_val, nums[j])

            res = max(res, min_val * (j - i + 1))

        return res