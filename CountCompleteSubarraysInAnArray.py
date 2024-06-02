from collections import defaultdict

class Solution(object):
    def countCompleteSubarrays(self, nums):
        s = len(set(nums))
        ss = defaultdict(lambda: 0)
        css = 0
        l = 0
        res = 0
        for r in range(len(nums)):
            ss[nums[r]] += 1
            if ss[nums[r]] == 1: css += 1
            while css == s:
                res += len(nums) - r
                ss[nums[l]] -= 1
                if ss[nums[l]] == 0: css -= 1
                l += 1
        return res