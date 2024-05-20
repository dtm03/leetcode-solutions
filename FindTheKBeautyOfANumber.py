class Solution(object):
    def divisorSubstrings(self, num, k):
        res = 0
        nums = str(num)
        for i in range(len(nums) - k + 1):
            sub = nums[i : i + k]
            if int(sub) != 0 and num % int(sub) == 0:
                res += 1
        return res