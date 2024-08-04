class Solution(object):
    def minSwaps(self, nums):
        total = nums.count(1)
        if total == 0:
            return 0

        nums = nums + nums[:total]
        res = nums[:total].count(0)
        curr = res

        for i in range(1, len(nums) - total + 1):
            if nums[i - 1] == 0:
                curr -= 1
            if nums[i + total - 1] == 0:
                curr += 1
            res = min(res, curr)

        return res

