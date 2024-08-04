class Solution(object):
    def rangeSum(self, nums, n, left, right):
        sub = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub.append(sum(nums[i:j + 1]))
        sub.sort()
        res = sum(sub[left - 1:right])
        return res % (10 ** 9 + 7)