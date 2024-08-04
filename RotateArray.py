class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        e = n - k
        nums[:] = nums[e:] + nums[:e]      