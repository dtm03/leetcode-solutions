# The goal is to find the maximum length of a contiguous subarray with an equal number of 0s and 1s

class Solution(object):
    def findMaxLength(self, nums):
        diff, res = 0, 0

        diff_index = {} # count[1] - count[0] -> index

        for i, n in enumerate(nums):
            if n == 0:
                diff -= 1
            else:
                diff += 1
            if diff not in diff_index:
                diff_index[diff] = i

            if diff == 0:
                res = i + 1
            else:
                res = max(res, i - diff_index[diff])

        return res

    '''
    class Solution(object):
    def findMaxLength(self, nums):
        zero, one = 0, 0
        res = 0

        diff_index = {} # count[1] - count[0] -> index

        for i, n in enumerate(nums):
            if n == 0:
                zero += 1
            else:
                one += 1
            if one - zero not in diff_index:
                diff_index[one - zero] = i

            if one == zero:
                res = one + zero
            else:
                res = max(res, i - diff_index[one - zero])

        return res
    '''