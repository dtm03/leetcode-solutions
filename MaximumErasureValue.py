class Solution(object):
    def maximumUniqueSubarray(self, nums):
        l, r = 0, 0
        res = 0
        ws = 0
        seen = set()

        while r < len(nums):
            if nums[r] not in seen:
                ws += nums[r]
                seen.add(nums[r])
                r += 1
                res = max(res, ws)
            else:
                ws -= nums[l]
                seen.remove(nums[l])
                l += 1

        return res
