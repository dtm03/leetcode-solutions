# The goal is to finde the only number in an array that isn't a duplicate in linear runtime complexity and constant space.
# => Use XOR

class Solution(object):
    def singleNumber(self, nums):

        res = 0

        for n in nums:

            # XOR
            res = res ^ n

        return res