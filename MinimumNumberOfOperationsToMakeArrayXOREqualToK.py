class Solution(object):
    def minOperations(self, nums, k):
        curr = 0
        for num in nums:
            curr ^= num

        diff = curr ^ k

        return bin(diff).count('1')