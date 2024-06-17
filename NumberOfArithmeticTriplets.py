class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        nums = set(nums)
        res = 0

        for n in nums:
            if (n + diff) in nums and (n + 2*diff) in nums:
                res += 1

        return res